-- BANK-FLAGS.sql — KS4 route-flag corrections (Mide, 2 Oct 2026), the DATABASE half.
--
-- NOT a migration. Not under supabase/migrations on purpose: it changes rows
-- of reference content, not schema. The chat applies it to PRODUCTION
-- (project ref urklkrwevjtlfbwnipjn) AFTER the PR that carries it merges,
-- and rehearses it on TEST (qeppkiswvclkkwbxmlok) first.
--
-- What it does: `ks4_assignment_bank.tier` / `.triple_only` are derived from
-- `ks4_data.classify()` (first appearance of the subtopic across the twelve
-- route files). The PR moved eight subtopics' routes, so classify() now
-- flags them differently, and ks4_data/questions/** was re-flagged to match
-- (only those two values; 468 questions; no other field changed). This
-- brings the mirror into line with the authored corpus.
--
--   slug                              rows  before                after
--   meiosis                            64   foundation, triple    foundation, base
--   classification-living-organisms    64   foundation, triple    foundation, base
--   thermal-conductivity               70   foundation, triple    foundation, base
--   resolving-forces                   54   higher,     triple    higher,     not triple
--   free-body-diagrams                 54   higher,     triple    higher,     not triple
--   motion-in-a-circle                 54   higher,     triple    higher,     not triple
--   wave-front-refraction              54   higher,     triple    higher,     not triple
--   dark-matter-dark-energy            54   higher,     triple    foundation, triple
--                                     ---
--                                     468  (96 of them inside the frozen
--                                           window, bank_position 0–11)
--
-- No id, band, bank_position, text, options or correct_index changes.
-- frozen_window_guard.py reads production and compares tier/triple_only on
-- every frozen row, so it is RED from the moment the PR's corpus is checked
-- out until this is applied, and green after.

-- ── PRE-CHECK (expect 8 rows, counts as in the table, all "before" flags) ──
select subtopic_slug, tier, triple_only, count(*)
from public.ks4_assignment_bank
where subtopic_slug in ('meiosis','classification-living-organisms',
  'thermal-conductivity','resolving-forces','free-body-diagrams',
  'motion-in-a-circle','wave-front-refraction','dark-matter-dark-energy')
group by 1,2,3 order by 1;

-- ── APPLY ──────────────────────────────────────────────────────────────
begin;

update public.ks4_assignment_bank
   set triple_only = false
 where subtopic_slug in ('meiosis','classification-living-organisms','thermal-conductivity')
   and tier = 'foundation' and triple_only = true;             -- expect 198

update public.ks4_assignment_bank
   set triple_only = false
 where subtopic_slug in ('resolving-forces','free-body-diagrams',
                         'motion-in-a-circle','wave-front-refraction')
   and tier = 'higher' and triple_only = true;                 -- expect 216

update public.ks4_assignment_bank
   set tier = 'foundation'
 where subtopic_slug = 'dark-matter-dark-energy'
   and tier = 'higher' and triple_only = true;                 -- expect 54

-- Abort unless exactly 468 rows now carry the new flags.
do $$
declare n int;
begin
  select count(*) into n from public.ks4_assignment_bank
   where (subtopic_slug in ('meiosis','classification-living-organisms','thermal-conductivity')
          and tier='foundation' and triple_only=false)
      or (subtopic_slug in ('resolving-forces','free-body-diagrams','motion-in-a-circle','wave-front-refraction')
          and tier='higher' and triple_only=false)
      or (subtopic_slug='dark-matter-dark-energy' and tier='foundation' and triple_only=true);
  if n <> 468 then
    raise exception 'BANK-FLAGS: expected 468 re-flagged rows, found %', n;
  end if;
end $$;

commit;

-- ── ROLLBACK (restores the pre-PR flags exactly) ───────────────────────
-- begin;
-- update public.ks4_assignment_bank set triple_only = true
--  where subtopic_slug in ('meiosis','classification-living-organisms','thermal-conductivity')
--    and tier = 'foundation' and triple_only = false;          -- expect 198
-- update public.ks4_assignment_bank set triple_only = true
--  where subtopic_slug in ('resolving-forces','free-body-diagrams',
--                          'motion-in-a-circle','wave-front-refraction')
--    and tier = 'higher' and triple_only = false;              -- expect 216
-- update public.ks4_assignment_bank set tier = 'higher'
--  where subtopic_slug = 'dark-matter-dark-energy'
--    and tier = 'foundation' and triple_only = true;           -- expect 54
-- commit;
--
-- ── PROOF AFTER APPLY ─────────────────────────────────────────────────
--   python3 export_ks4_questions.py --verify --project prod   (mirror == corpus, flags included)
--   python3 frozen_window_guard.py             (green again)
