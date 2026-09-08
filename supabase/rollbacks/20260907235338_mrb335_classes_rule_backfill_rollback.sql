-- ROLLBACK for 20260907235338_mrb335_classes_rule_backfill.sql (MRB-335).
--
-- Apply MANUALLY only. Then:
--   delete from supabase_migrations.schema_migrations where version = '20260907235338';
--
-- ⚠️ THIS ONE CANNOT BE UNDONE EXACTLY, AND THAT HAS TO BE SAID OUT LOUD.
-- The forward migration writes `tier_pathway_source = 'rule'`, and `rule` is
-- also what the INSERT trigger writes — so after it has run there is no column
-- that distinguishes "the backfill filled this" from "the trigger filled this
-- at INSERT". Clearing every `rule` row would also clear classes created since
-- MRB-335 landed, which the backfill never touched.
--
-- So this file does NOT clear anything by default. Read the two statements,
-- decide which rows you mean, and run them with an explicit id list.
--
-- Take the inventory FIRST — this is what you will not be able to reconstruct:
--
--   select id, name, tier, science_pathway, science_subject, tier_pathway_source
--     from public.classes
--    where key_stage = 'KS4' and tier_pathway_source = 'rule'
--    order by name;
--
-- ⚠️ AND CLEARING IS NOT NEUTRAL. A KS4 class with no tier and no pathway is
-- served BASE CONTENT by `ks4BankScope()` — foundation, not triple. That is
-- safe, and it is also a third of the pool a Higher Triple class should get,
-- delivered silently. Undoing this migration makes every class it touched
-- quietly under-served rather than visibly broken.

-- (a) undo §2 — the science derived from the timetable, for the Triple classes
--     whose NAME the rule cannot read. Restrict to the ids you actually mean.
--
-- update public.classes
--    set science_subject = null
--  where id in ('...', '...');

-- (b) undo §1 — the tier/pathway/science derived from the name.
--
-- update public.classes
--    set tier = null, science_pathway = null, science_subject = null,
--        tier_pathway_source = null
--  where id in ('...', '...');

-- (c) the column comment, back to what 20260907211350 set.
comment on column public.classes.tier_pathway_source is
  'rule = derived from the class name by classes_apply_tier_rule on INSERT. admin = a person set it (POST /api/admin/class-tier), and the rule must never overwrite it. NULL = neither.';
