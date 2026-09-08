-- MRB-335 — the classes that already exist meet the rule.
--
-- ⚠️ VERSION IS LOAD-BEARING. TEST recorded 20260907235338; written as
-- 20260908000300 and renamed to match. MCP `apply_migration` stamps its own
-- version rather than reading a filename, and a mismatch makes `db push`
-- re-apply the whole file.
--
-- Rehearsed on TEST 8 Sep 2026: §1 changed 0 rows (no TEST class has a
-- rule-readable name with all three columns still NULL) and §2 changed 2 —
-- `10X1 Biology` → biology and `10Z Physics` → physics, both from their single
-- timetabled science, both keeping the `admin` source they already carried.
--
-- ⚠️ THIS IS A THIRD FILE RATHER THAN AN EDIT TO 20260907211350. That one is
-- applied on TEST; editing an applied migration means the file and the database
-- disagree and `supabase db push` re-runs neither. Forward-only, always.
--
-- ── WHY THE FIRST BACKFILL WAS NOT ENOUGH ──────────────────────────────
--
-- 20260907211350 §4a filled `science_subject` from the name rule, but only
-- `where science_pathway = 'triple'` — i.e. only for a class that ALREADY knew
-- it was Triple. On TEST that was every triple class and the section looked
-- complete.
--
-- On production it is nearly nobody. 36 of Rainford's 38 KS4 classes carry NO
-- tier and NO pathway (MRB-332): the roster CSV does not have those columns.
-- So on production `10A/Bi1` is a KS4 class with three NULLs, §4a's
-- `science_pathway = 'triple'` predicate does not match it, and it stays
-- subjectless — while the trigger, which WOULD have read its name correctly,
-- only fires on INSERT and that row was inserted months ago.
--
-- The result would be 36 classes whose Set work sheet offers all three sciences
-- and whose pool is base content, on a roster whose NAMES say exactly what each
-- one is.
--
-- ⚠️ SO §1 BELOW APPLIES ALL THREE COLUMNS, not just tier and pathway. Filling
-- tier and pathway and leaving `science_subject` NULL would leave `10A/Bi1` as
-- "Triple, science unknown" — which reads as a separate-sciences class that
-- sees all three sciences' trees, and is worse than the NULL it started from.

-- ── 1. the name rule, applied to rows nobody has touched ──────────────
--
-- ⚠️ THE GUARD IS THREE NULLS, AND EACH IS DOING WORK. `tier` and
-- `science_pathway` NULL means nothing has been decided. `tier_pathway_source`
-- NULL means nothing has been decided BY ANYBODY — a row that a person cleared
-- by hand carries `admin` and must not be silently re-filled from its name,
-- which is the whole point of that column (RISKS D11). A row the rule cannot
-- read (`rule_tier is null`) is left exactly as it was: NULL is the safe
-- answer, and `ks4BankScope()` serves such a class base content, which is
-- correct for everybody.
update public.classes c
   set tier             = (select r.tier    from public.class_tier_rule(c.name) r),
       science_pathway  = (select r.pathway from public.class_tier_rule(c.name) r),
       science_subject  = (select r.subject from public.class_tier_rule(c.name) r),
       tier_pathway_source = 'rule'
 where c.key_stage = 'KS4'
   and c.tier is null
   and c.science_pathway is null
   and c.tier_pathway_source is null
   and (select r.tier from public.class_tier_rule(c.name) r) is not null;

-- ── 2. the separate sciences whose NAME the rule cannot read ──────────
--
-- `10X1 Biology`, `10Z Physics` — real class names that predate the convention.
-- They are already marked Triple by somebody, so the pathway is settled and only
-- the science is missing; and the timetable already knows it, because
-- `class_teachers.subject_id` is what the teacher is timetabled to teach that
-- class for.
--
-- ⚠️ ONLY WHEN IT IS UNAMBIGUOUS. `exactly one of Biology / Chemistry /
-- Physics` means: one distinct science across every live teacher link. A
-- co-taught class whose two teachers are filed under different sciences, or one
-- filed under `Science` or `Maths`, yields NULL and is left for a person. This
-- is a derivation from adjacent data, not a fact, and the moment it needs a
-- tie-break it stops being one.
--
-- ⚠️ COMBINED CLASSES ARE NOT TOUCHED. `10A` is combined and its teacher is
-- filed under Physics; a combined class has no separate science, and copying
-- the teacher's timetable subject onto it would invent one.
--
-- `tier_pathway_source` is written explicitly so the trigger stands back. It is
-- `rule` rather than `admin` because no person decided this — the platform
-- derived it. See the widened column comment at the foot of this file.
update public.classes c
   set science_subject = sub.name,
       tier_pathway_source = coalesce(c.tier_pathway_source, 'rule')
  from (
    select ct.class_id, min(lower(s.name)) as name
      from public.class_teachers ct
      join public.subjects s on s.id = ct.subject_id
     where ct.ended_at is null
       and ct.deleted_at is null
       and s.name in ('Biology', 'Chemistry', 'Physics')
     group by ct.class_id
    having count(distinct s.name) = 1
  ) sub
 where c.id = sub.class_id
   and c.key_stage = 'KS4'
   and c.science_pathway = 'triple'
   and c.science_subject is null
   -- Only where the NAME could not answer. If the rule can read the name, §1
   -- above (or the INSERT trigger) has already had its say and is the better
   -- authority: a class named `10a/Bi1` is Biology even if a chemist covers it.
   and (select r.subject from public.class_tier_rule(c.name) r) is null;

-- ── 3. `tier_pathway_source` means "who decided", not "which rule" ─────
--
-- Widened by §2: the platform can now derive a science from the timetable as
-- well as from the name, and both are `rule` because the alternative value
-- means a person typed it. A reader who takes `rule` to mean "the name rule
-- specifically" would conclude, wrongly, that `10Z Physics` has a name the
-- convention covers.
comment on column public.classes.tier_pathway_source is
  'WHO decided this class''s tier/pathway/science. rule = the platform derived it — from the class name (classes_apply_tier_rule, on INSERT) or, for a Triple class whose name the convention cannot read, from its single timetabled science (MRB-335 backfill). admin = a person set it, through POST /api/admin/class-tier, and the platform must never overwrite it. NULL = neither.';
