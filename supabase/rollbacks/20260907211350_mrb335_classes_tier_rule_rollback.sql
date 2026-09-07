-- ROLLBACK for 20260907211350_mrb335_classes_tier_rule.sql (MRB-335).
--
-- Apply MANUALLY only. After it succeeds, remove the registry row:
--
--   delete from supabase_migrations.schema_migrations
--    where version = '20260907211350';
--
-- ⚠️ THE ORDER BELOW IS LOAD-BEARING. The trigger goes FIRST. Dropping the
-- columns while it is still installed would leave `classes_apply_tier_rule()`
-- referring to `NEW.science_subject`, which no longer exists — and a plpgsql
-- trigger resolves its field references at RUN time, so the failure would not
-- appear here. It would appear the next time anybody inserted a class, as a
-- roster import that suddenly refuses every row.
--
-- ⚠️ IT ALSO DESTROYS THE ADMIN DECISIONS. `tier_pathway_source = 'admin'`
-- records that a person corrected a class by hand, and nothing else holds that
-- fact — `audit_log` holds the events, but the current state does not survive.
-- Count first:
--
--   select tier_pathway_source, count(*) from public.classes group by 1;
--
-- `tier` and `science_pathway` are NOT dropped: they existed before MRB-335 and
-- the values the trigger filled are correct. What is lost is the record of
-- WHICH of them the rule filled.

drop trigger if exists classes_apply_tier_rule on public.classes;
drop function if exists public.classes_apply_tier_rule();
drop function if exists public.class_tier_rule(text);

alter table public.classes drop constraint if exists classes_tier_only_ks4_check;
alter table public.classes
  add constraint classes_tier_only_ks4_check
  check (((tier is null) and (science_pathway is null)) or key_stage = 'KS4');

alter table public.classes drop constraint if exists classes_tier_pathway_source_check;
alter table public.classes drop constraint if exists classes_science_subject_check;

alter table public.classes drop column if exists tier_pathway_source;
alter table public.classes drop column if exists science_subject;
