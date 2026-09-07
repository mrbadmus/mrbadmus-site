-- MRB-335 — a class says which cohort it is, and the NAME says it first.
--
-- ⚠️ VERSION IS LOAD-BEARING. Applied to TEST through MCP `apply_migration`,
-- which records its OWN `schema_migrations` version rather than reading a
-- filename. TEST recorded 20260907211350, so this file carries it. It was
-- WRITTEN as 20260908000200 and renamed to match what TEST actually recorded.
--
-- Set work v2 asks a question v1 never had to: WHICH COHORT is this class, so
-- that the sheet can show it the right tree and offer the right sibling classes
-- to set alongside it. A cohort is (key_stage, science_pathway, science_subject)
-- — and `classes` has no `science_subject` column at all. Today a separate
-- science is inferred from `class_teachers.subject_id`, which is the TEACHER's
-- timetable subject: it is right most of the time, it is a join away, and it is
-- silently wrong for a co-taught class or a teacher who covers two sciences.
--
-- ⚠️ AND 36 OF RAINFORD'S 38 KS4 CLASSES HAVE NO TIER AND NO PATHWAY (MRB-332).
-- That is not an import bug to chase; it is what the roster CSV carries. The
-- names, however, are exact — `10h/Ph1`, `11r/Sc1`, `10A/Bi1` — and Rainford's
-- own naming convention (MRB-263) encodes the whole cohort in them. So the name
-- is the source, and the rule is applied by the DATABASE rather than by an
-- importer, because there are two importers (the edge function and the admin
-- screen) and there will be a third.

-- ── 1. the two new columns ────────────────────────────────────────────
alter table public.classes
  add column if not exists science_subject text;

alter table public.classes
  drop constraint if exists classes_science_subject_check;
alter table public.classes
  add constraint classes_science_subject_check
  check (science_subject is null
         or science_subject in ('biology', 'chemistry', 'physics'));

-- `rule` = the trigger below derived it from the name. `admin` = a person set
-- it, through `POST /api/admin/class-tier`, and the rule must never quietly
-- overwrite it. NULL = neither has happened.
--
-- ⚠️ THIS COLUMN IS THE WHOLE DEFENCE AGAINST RE-IMPORT (RISKS D11). The edge
-- function find-or-creates by exact `(school_id, academic_year_id, name)`, so
-- an existing class is UPDATEd rather than re-INSERTed — and the fill only ever
-- happens on INSERT. `admin` is what makes that visible rather than merely true.
alter table public.classes
  add column if not exists tier_pathway_source text;

alter table public.classes
  drop constraint if exists classes_tier_pathway_source_check;
alter table public.classes
  add constraint classes_tier_pathway_source_check
  check (tier_pathway_source is null
         or tier_pathway_source in ('rule', 'admin'));

-- ── 2. the KS4-only guard, widened ────────────────────────────────────
--
-- `classes_tier_only_ks4_check` said tier and pathway may only be set on a KS4
-- row. `science_subject` is the same kind of fact and must join it, or a KS3
-- class could be filed under Biology — which at KS3 means nothing, since a KS3
-- class is taught all three sciences by definition.
alter table public.classes
  drop constraint if exists classes_tier_only_ks4_check;
alter table public.classes
  add constraint classes_tier_only_ks4_check
  check (((tier is null) and (science_pathway is null) and (science_subject is null))
         or key_stage = 'KS4');

-- ── 3. `class_tier_rule(name)` — the naming convention, as a function ──
--
-- MRB-263's convention: year number, lowercase band letter, slash, subject code
-- with a single capital, set number — `7h/Sc5`, `10h/Ph1`, `11r/Sc1`. The band
-- letter is case-insensitive because `10A/Bi1` is a real class on Rainford's
-- roster.
--
--     /Sc  → combined, no separate science
--     /Bi /Ch /Ph → triple, that science
--     set number 4 or 5 → foundation; anything else → higher
--     any other shape at all → all three NULL
--
-- ⚠️ NULL IS A REAL ANSWER AND IT IS THE SAFE ONE. A name the convention does
-- not cover — `Year 10 Mixed`, `10 Set 1`, a typo — yields nothing, the trigger
-- fills nothing, and the class stays exactly as unset as it was. It does NOT
-- guess. An unset KS4 class is served base content by `ks4BankScope()`, which is
-- correct for everybody; a guessed Higher Triple class is not.
--
-- ⚠️ THE SUBJECT CODE IS CASE-SENSITIVE, deliberately, and only the band letter
-- is not. `Sc` is the convention; `SC1` or `sc1` is a name that does not follow
-- it, and the honest answer to a name that does not follow the convention is
-- NULL rather than a best guess at what was meant.
--
-- Mirrored in JS as `classTierRule()` in the backend's `set-work-scope.js`, for
-- the admin route's defaulting. `test_set_work_v2.js` drives the two against
-- the same five names — the mirror is the kind of thing that drifts, so it is
-- checked rather than trusted.
create or replace function public.class_tier_rule(p_name text)
returns table (tier text, pathway text, subject text)
language sql
immutable
set search_path = public, pg_temp
as $$
  select
    case when m is null then null
         when m[2] in ('4', '5') then 'foundation'
         else 'higher' end,
    case when m is null then null
         when m[1] = 'Sc' then 'combined'
         else 'triple' end,
    case when m is null then null
         when m[1] = 'Bi' then 'biology'
         when m[1] = 'Ch' then 'chemistry'
         when m[1] = 'Ph' then 'physics'
         else null end
  from (
    select regexp_match(coalesce(p_name, ''),
                        '^[0-9]{1,2}[A-Za-z]/(Sc|Bi|Ch|Ph)([0-9]+)$') as m
  ) t;
$$;

comment on function public.class_tier_rule(text) is
  'MRB-335: Rainford''s class-naming convention (MRB-263) as a function. Returns one row of (tier, pathway, subject); all three NULL for a name the convention does not cover. Mirrored in JS as classTierRule() in the backend''s set-work-scope.js.';

-- ── 4. BACKFILL, and it runs BEFORE the trigger exists ────────────────
--
-- ⚠️ THE ORDER IS DELIBERATE. The trigger below stamps `admin` on any UPDATE
-- that moves tier, pathway or subject — which is exactly what these two
-- statements do. Creating the trigger first would make the backfill label every
-- row it touched as a person's decision, which is the opposite of true.

-- 4a. `science_subject` for the separate sciences, where the row already agrees
--     with the rule that it is Triple. A row whose pathway says combined is left
--     alone even if its NAME says Biology: the stored value is somebody's
--     decision and the name is only evidence.
update public.classes c
   set science_subject = (select r.subject from public.class_tier_rule(c.name) r)
 where c.key_stage = 'KS4'
   and c.science_subject is null
   and c.science_pathway = 'triple'
   and (select r.subject from public.class_tier_rule(c.name) r) is not null;

-- 4b. `tier_pathway_source` for rows that already carry a tier or a pathway:
--     `rule` when what is stored is exactly what the name would have produced,
--     `admin` when it is not — because somebody put it there.
--
-- ⚠️ A ROW WITH NEITHER STAYS NULL. "The rule produced (null, null) and the row
-- holds (null, null), so they agree, so it is `rule`" is arithmetically true and
-- a lie: nothing ruled anything. NULL is the honest record of an unset class.
update public.classes c
   set tier_pathway_source = case
         when c.tier is not distinct from
              (select r.tier from public.class_tier_rule(c.name) r)
          and c.science_pathway is not distinct from
              (select r.pathway from public.class_tier_rule(c.name) r)
         then 'rule' else 'admin' end
 where c.key_stage = 'KS4'
   and c.tier_pathway_source is null
   and (c.tier is not null or c.science_pathway is not null);

-- ── 5. the trigger ────────────────────────────────────────────────────
--
-- BEFORE INSERT OR UPDATE, and the two arms do different jobs.
--
-- INSERT — fill what is NULL, and only what is NULL. A caller who names a tier
-- is obeyed; the rule is a default, not an authority. `tier_pathway_source`
-- records which of the two happened, so a later reader can tell a derived class
-- from a decided one.
--
-- UPDATE — never re-derive. The rule ran once, at birth; a name that changes
-- later must not silently re-tier a class that a head of department has since
-- corrected by hand. What the UPDATE arm does instead is WITNESS: if tier,
-- pathway or subject moved and nobody said why, that was a person, and the row
-- says `admin` from then on.
--
-- ⚠️ THE ESCAPE HATCH IS SETTING `tier_pathway_source` EXPLICITLY, and it
-- governs the LABEL, not the fill. Both arms leave a caller-supplied source
-- alone — which is how a seed, a repair script or a future importer can write
-- `rule` on purpose — while the INSERT arm still fills a NULL tier or pathway
-- from the name. Measured on TEST: `10q/Ch4` inserted with only
-- `tier_pathway_source = 'admin'` came out foundation/triple/chemistry and kept
-- its `admin` label.
create or replace function public.classes_apply_tier_rule()
returns trigger
language plpgsql
set search_path = public, pg_temp
as $$
declare
  r record;
  filled boolean := false;
begin
  if NEW.key_stage is distinct from 'KS4' then
    return NEW;
  end if;

  select * into r from public.class_tier_rule(NEW.name);

  if TG_OP = 'INSERT' then
    if NEW.tier is null and NEW.science_pathway is null and r.tier is not null then
      NEW.tier := r.tier;
      NEW.science_pathway := r.pathway;
      filled := true;
    end if;
    if NEW.science_subject is null
       and r.subject is not null
       and NEW.science_pathway = 'triple' then
      NEW.science_subject := r.subject;
      filled := true;
    end if;
    if NEW.tier_pathway_source is null then
      if filled then
        NEW.tier_pathway_source := 'rule';
      elsif NEW.tier is not null or NEW.science_pathway is not null then
        NEW.tier_pathway_source := case
          when NEW.tier is not distinct from r.tier
           and NEW.science_pathway is not distinct from r.pathway
          then 'rule' else 'admin' end;
      end if;
    end if;
    return NEW;
  end if;

  if (NEW.tier, NEW.science_pathway, NEW.science_subject)
       is distinct from (OLD.tier, OLD.science_pathway, OLD.science_subject)
     and NEW.tier_pathway_source is not distinct from OLD.tier_pathway_source then
    NEW.tier_pathway_source := 'admin';
  end if;

  return NEW;
end;
$$;

drop trigger if exists classes_apply_tier_rule on public.classes;
create trigger classes_apply_tier_rule
  before insert or update on public.classes
  for each row execute function public.classes_apply_tier_rule();

comment on column public.classes.science_subject is
  'biology|chemistry|physics for a separate-sciences KS4 class; NULL for combined and for every KS3 class. Part of the Set work cohort (key_stage, science_pathway, science_subject). Filled from the name rule on INSERT.';
comment on column public.classes.tier_pathway_source is
  'rule = derived from the class name by classes_apply_tier_rule on INSERT. admin = a person set it (POST /api/admin/class-tier), and the rule must never overwrite it. NULL = neither.';
