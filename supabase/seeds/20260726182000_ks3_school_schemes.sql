-- ═══════════════════════════════════════════════════════════════════════
-- KS3 — real schools' configured sequences, as override rows.
--
-- ⚠️ GENERATED FILE — DO NOT EDIT BY HAND.
--    Regenerate with:  python3 ks3_seed_sow.py
--    Source of truth:  ks3_data/structure.py, ks3_data/default_sequence.py,
--                      ks3_data/school_schemes.py
--    Written to:       supabase/seeds/20260726182000_ks3_school_schemes.sql
--    Target table:     public.scheme_of_work_overrides (PER-SCHOOL — has school_id)
--
-- Hand-editing this file makes it disagree with ks3_data/, and a scheme row
-- that disagrees with the lesson registry is a school pointing at a lesson
-- that does not exist. Change the Python, re-run the generator.
--
-- Requires migrations 20260726120000_ks3_scheme_of_work_entries.sql and
-- 20260727081530_ks3_scheme_of_work_overrides.sql (architecture.md §8.7):
-- without them KS3 rows either cannot be inserted or can be duplicated.
--
-- Idempotent: every KS3 row in scope is deleted and rewritten, inside one
-- transaction. Re-running is safe and is the intended way to apply a change.
--
-- SEED DATA and reference evidence. **Never the default, never a
-- template.** These rows describe what one named school teaches and
-- when; the platform default lives in the companion seed against
-- scheme_of_work_entries.
--
-- Each block below is one school laying its own order over the
-- default — which is the whole of what architecture.md §4.5 asks a
-- reorder to cost: rows in this table, and nothing else. No page
-- path and no page byte depends on any of it.
--
-- 1 school, 183 rows.
--
-- ═══════════════════════════════════════════════════════════════════════

begin;

do $$
begin
  if (select count(*) from public.subjects
       where name in ('Biology', 'Chemistry', 'Physics')) <> 3 then
    raise exception 'KS3 seed: public.subjects is missing one of Biology / '
                    'Chemistry / Physics. Seed the subjects table first.';
  end if;
end $$;


-- ═══════════════════════════════════════════════════════════════════════
-- Rainford High School  (schools.slug = 'rainford-high')
--
-- Source: MRB-103 locked year map, ratification comment 6 Jul 2026, by Ayo; ruled against Rainford's actual scheme of work.
--
-- Row counts, generated:
--
--   Y7  Biology 26 · Chemistry 31 · Physics 33
--   Y8  Biology 29 · Chemistry 24 · Physics 37
--   Y9  Biology 3
--   183 rows total, max academic_week 37 (ceiling 39)
--
-- ═══════════════════════════════════════════════════════════════════════

do $$
begin
  if not exists (select 1 from public.schools where slug = 'rainford-high') then
    raise exception 'KS3 seed: no school with slug %. Insert the school row '
                    'before seeding its scheme of work.', 'rainford-high';
  end if;
end $$;

-- Idempotency: this block owns every KS3 override row for this school.
delete from public.scheme_of_work_overrides
 where key_stage = 'KS3'
   and school_id = (select id from public.schools where slug = 'rainford-high');

-- ── Year 7 · Biology — 26 lessons ─────────────────────────
insert into public.scheme_of_work_overrides
  (school_id, key_stage, year_group, tier, pathway, subject_id, academic_week, topic, subtopic, notes)
values
  -- B1 Cells and organisation
  ((select id from public.schools where slug = 'rainford-high'), 'KS3', 7, null, null, (select id from public.subjects where name = 'Biology'), 1, 'Cells and organisation', 'life-processes', null),
  ((select id from public.schools where slug = 'rainford-high'), 'KS3', 7, null, null, (select id from public.subjects where name = 'Biology'), 2, 'Cells and organisation', 'using-a-microscope', null),
  ((select id from public.schools where slug = 'rainford-high'), 'KS3', 7, null, null, (select id from public.subjects where name = 'Biology'), 3, 'Cells and organisation', 'animal-and-plant-cells', null),
  ((select id from public.schools where slug = 'rainford-high'), 'KS3', 7, null, null, (select id from public.subjects where name = 'Biology'), 4, 'Cells and organisation', 'specialised-cells', null),
  ((select id from public.schools where slug = 'rainford-high'), 'KS3', 7, null, null, (select id from public.subjects where name = 'Biology'), 5, 'Cells and organisation', 'levels-of-organisation', null),
  ((select id from public.schools where slug = 'rainford-high'), 'KS3', 7, null, null, (select id from public.subjects where name = 'Biology'), 6, 'Cells and organisation', 'unicellular-organisms', null),
  -- B2 Movement: skeleton and muscles
  ((select id from public.schools where slug = 'rainford-high'), 'KS3', 7, null, null, (select id from public.subjects where name = 'Biology'), 7, 'Movement: skeleton and muscles', 'what-the-skeleton-does', null),
  ((select id from public.schools where slug = 'rainford-high'), 'KS3', 7, null, null, (select id from public.subjects where name = 'Biology'), 8, 'Movement: skeleton and muscles', 'joints', null),
  ((select id from public.schools where slug = 'rainford-high'), 'KS3', 7, null, null, (select id from public.subjects where name = 'Biology'), 9, 'Movement: skeleton and muscles', 'antagonistic-muscle-pairs', null),
  ((select id from public.schools where slug = 'rainford-high'), 'KS3', 7, null, null, (select id from public.subjects where name = 'Biology'), 10, 'Movement: skeleton and muscles', 'biomechanics-forces-in-the-body', null),
  -- B3 Nutrition and digestion
  ((select id from public.schools where slug = 'rainford-high'), 'KS3', 7, null, null, (select id from public.subjects where name = 'Biology'), 11, 'Nutrition and digestion', 'a-balanced-diet', null),
  ((select id from public.schools where slug = 'rainford-high'), 'KS3', 7, null, null, (select id from public.subjects where name = 'Biology'), 12, 'Nutrition and digestion', 'food-tests', null),
  ((select id from public.schools where slug = 'rainford-high'), 'KS3', 7, null, null, (select id from public.subjects where name = 'Biology'), 13, 'Nutrition and digestion', 'energy-in-food', 'Cross-reference (architecture.md §4.6): this lesson is owned by P2 Energy at home (Physics) and is taught from there. Listed here because Nutrition and digestion teaches the slot, not because the content is duplicated.'),
  ((select id from public.schools where slug = 'rainford-high'), 'KS3', 7, null, null, (select id from public.subjects where name = 'Biology'), 14, 'Nutrition and digestion', 'when-diet-goes-wrong', null),
  ((select id from public.schools where slug = 'rainford-high'), 'KS3', 7, null, null, (select id from public.subjects where name = 'Biology'), 15, 'Nutrition and digestion', 'the-digestive-system', null),
  ((select id from public.schools where slug = 'rainford-high'), 'KS3', 7, null, null, (select id from public.subjects where name = 'Biology'), 16, 'Nutrition and digestion', 'enzymes-in-digestion', null),
  ((select id from public.schools where slug = 'rainford-high'), 'KS3', 7, null, null, (select id from public.subjects where name = 'Biology'), 17, 'Nutrition and digestion', 'absorption-and-the-small-intestine', null),
  ((select id from public.schools where slug = 'rainford-high'), 'KS3', 7, null, null, (select id from public.subjects where name = 'Biology'), 18, 'Nutrition and digestion', 'bacteria-in-the-gut', null),
  -- B5 Reproduction
  ((select id from public.schools where slug = 'rainford-high'), 'KS3', 7, null, null, (select id from public.subjects where name = 'Biology'), 19, 'Reproduction', 'human-reproductive-systems', null),
  ((select id from public.schools where slug = 'rainford-high'), 'KS3', 7, null, null, (select id from public.subjects where name = 'Biology'), 20, 'Reproduction', 'gametes-and-fertilisation', null),
  ((select id from public.schools where slug = 'rainford-high'), 'KS3', 7, null, null, (select id from public.subjects where name = 'Biology'), 21, 'Reproduction', 'the-menstrual-cycle', null),
  ((select id from public.schools where slug = 'rainford-high'), 'KS3', 7, null, null, (select id from public.subjects where name = 'Biology'), 22, 'Reproduction', 'gestation-placenta-and-birth', null),
  ((select id from public.schools where slug = 'rainford-high'), 'KS3', 7, null, null, (select id from public.subjects where name = 'Biology'), 23, 'Reproduction', 'lifestyle-and-the-developing-foetus', null),
  ((select id from public.schools where slug = 'rainford-high'), 'KS3', 7, null, null, (select id from public.subjects where name = 'Biology'), 24, 'Reproduction', 'flowers-and-pollination', null),
  ((select id from public.schools where slug = 'rainford-high'), 'KS3', 7, null, null, (select id from public.subjects where name = 'Biology'), 25, 'Reproduction', 'fertilisation-seeds-and-fruit', null),
  ((select id from public.schools where slug = 'rainford-high'), 'KS3', 7, null, null, (select id from public.subjects where name = 'Biology'), 26, 'Reproduction', 'seed-dispersal', null);

-- ── Year 7 · Chemistry — 31 lessons ─────────────────────────
insert into public.scheme_of_work_overrides
  (school_id, key_stage, year_group, tier, pathway, subject_id, academic_week, topic, subtopic, notes)
values
  -- C1 Particles and their behaviour
  ((select id from public.schools where slug = 'rainford-high'), 'KS3', 7, null, null, (select id from public.subjects where name = 'Chemistry'), 1, 'Particles and their behaviour', 'particle-model', null),
  ((select id from public.schools where slug = 'rainford-high'), 'KS3', 7, null, null, (select id from public.subjects where name = 'Chemistry'), 2, 'Particles and their behaviour', 'solids-liquids-and-gases', null),
  ((select id from public.schools where slug = 'rainford-high'), 'KS3', 7, null, null, (select id from public.subjects where name = 'Chemistry'), 3, 'Particles and their behaviour', 'changes-of-state', null),
  ((select id from public.schools where slug = 'rainford-high'), 'KS3', 7, null, null, (select id from public.subjects where name = 'Chemistry'), 4, 'Particles and their behaviour', 'gas-pressure', null),
  ((select id from public.schools where slug = 'rainford-high'), 'KS3', 7, null, null, (select id from public.subjects where name = 'Chemistry'), 5, 'Particles and their behaviour', 'diffusion', null),
  ((select id from public.schools where slug = 'rainford-high'), 'KS3', 7, null, null, (select id from public.subjects where name = 'Chemistry'), 6, 'Particles and their behaviour', 'testing-the-model', null),
  -- C3 Mixtures and separation
  ((select id from public.schools where slug = 'rainford-high'), 'KS3', 7, null, null, (select id from public.subjects where name = 'Chemistry'), 7, 'Mixtures and separation', 'pure-or-mixture', null),
  ((select id from public.schools where slug = 'rainford-high'), 'KS3', 7, null, null, (select id from public.subjects where name = 'Chemistry'), 8, 'Mixtures and separation', 'dissolving-and-solutions', null),
  ((select id from public.schools where slug = 'rainford-high'), 'KS3', 7, null, null, (select id from public.subjects where name = 'Chemistry'), 9, 'Mixtures and separation', 'filtration', null),
  ((select id from public.schools where slug = 'rainford-high'), 'KS3', 7, null, null, (select id from public.subjects where name = 'Chemistry'), 10, 'Mixtures and separation', 'evaporation-and-crystallisation', null),
  ((select id from public.schools where slug = 'rainford-high'), 'KS3', 7, null, null, (select id from public.subjects where name = 'Chemistry'), 11, 'Mixtures and separation', 'distillation', null),
  ((select id from public.schools where slug = 'rainford-high'), 'KS3', 7, null, null, (select id from public.subjects where name = 'Chemistry'), 12, 'Mixtures and separation', 'chromatography', null),
  ((select id from public.schools where slug = 'rainford-high'), 'KS3', 7, null, null, (select id from public.subjects where name = 'Chemistry'), 13, 'Mixtures and separation', 'proving-something-is-pure', null),
  -- C4 Chemical reactions
  ((select id from public.schools where slug = 'rainford-high'), 'KS3', 7, null, null, (select id from public.subjects where name = 'Chemistry'), 14, 'Chemical reactions', 'chemical-vs-physical-change', null),
  ((select id from public.schools where slug = 'rainford-high'), 'KS3', 7, null, null, (select id from public.subjects where name = 'Chemistry'), 15, 'Chemical reactions', 'reactions-rearrange-atoms', null),
  ((select id from public.schools where slug = 'rainford-high'), 'KS3', 7, null, null, (select id from public.subjects where name = 'Chemistry'), 16, 'Chemical reactions', 'word-equations', null),
  ((select id from public.schools where slug = 'rainford-high'), 'KS3', 7, null, null, (select id from public.subjects where name = 'Chemistry'), 17, 'Chemical reactions', 'mass-in-a-reaction', null),
  ((select id from public.schools where slug = 'rainford-high'), 'KS3', 7, null, null, (select id from public.subjects where name = 'Chemistry'), 18, 'Chemical reactions', 'symbol-equations-and-balancing', null),
  -- C5 Types of reaction
  ((select id from public.schools where slug = 'rainford-high'), 'KS3', 7, null, null, (select id from public.subjects where name = 'Chemistry'), 19, 'Types of reaction', 'combustion', null),
  ((select id from public.schools where slug = 'rainford-high'), 'KS3', 7, null, null, (select id from public.subjects where name = 'Chemistry'), 20, 'Types of reaction', 'thermal-decomposition', null),
  ((select id from public.schools where slug = 'rainford-high'), 'KS3', 7, null, null, (select id from public.subjects where name = 'Chemistry'), 21, 'Types of reaction', 'oxidation', null),
  ((select id from public.schools where slug = 'rainford-high'), 'KS3', 7, null, null, (select id from public.subjects where name = 'Chemistry'), 22, 'Types of reaction', 'displacement', null),
  ((select id from public.schools where slug = 'rainford-high'), 'KS3', 7, null, null, (select id from public.subjects where name = 'Chemistry'), 23, 'Types of reaction', 'which-reaction-is-this', null),
  -- C7 Energy changes in reactions
  ((select id from public.schools where slug = 'rainford-high'), 'KS3', 7, null, null, (select id from public.subjects where name = 'Chemistry'), 24, 'Energy changes in reactions', 'energy-and-changes-of-state', null),
  ((select id from public.schools where slug = 'rainford-high'), 'KS3', 7, null, null, (select id from public.subjects where name = 'Chemistry'), 25, 'Energy changes in reactions', 'exothermic-reactions', null),
  ((select id from public.schools where slug = 'rainford-high'), 'KS3', 7, null, null, (select id from public.subjects where name = 'Chemistry'), 26, 'Energy changes in reactions', 'endothermic-reactions', null),
  ((select id from public.schools where slug = 'rainford-high'), 'KS3', 7, null, null, (select id from public.subjects where name = 'Chemistry'), 27, 'Energy changes in reactions', 'measuring-a-temperature-change', null),
  -- C9 Metals and materials
  ((select id from public.schools where slug = 'rainford-high'), 'KS3', 7, null, null, (select id from public.subjects where name = 'Chemistry'), 28, 'Metals and materials', 'the-reactivity-series', null),
  ((select id from public.schools where slug = 'rainford-high'), 'KS3', 7, null, null, (select id from public.subjects where name = 'Chemistry'), 29, 'Metals and materials', 'predicting-displacement', null),
  ((select id from public.schools where slug = 'rainford-high'), 'KS3', 7, null, null, (select id from public.subjects where name = 'Chemistry'), 30, 'Metals and materials', 'getting-metals-out-of-rocks', null),
  ((select id from public.schools where slug = 'rainford-high'), 'KS3', 7, null, null, (select id from public.subjects where name = 'Chemistry'), 31, 'Metals and materials', 'ceramics-polymers-and-composites', null);

-- ── Year 7 · Physics — 33 lessons ─────────────────────────
insert into public.scheme_of_work_overrides
  (school_id, key_stage, year_group, tier, pathway, subject_id, academic_week, topic, subtopic, notes)
values
  -- P3 Describing motion
  ((select id from public.schools where slug = 'rainford-high'), 'KS3', 7, null, null, (select id from public.subjects where name = 'Physics'), 1, 'Describing motion', 'speed', null),
  ((select id from public.schools where slug = 'rainford-high'), 'KS3', 7, null, null, (select id from public.subjects where name = 'Physics'), 2, 'Describing motion', 'distance-time-graphs', null),
  ((select id from public.schools where slug = 'rainford-high'), 'KS3', 7, null, null, (select id from public.subjects where name = 'Physics'), 3, 'Describing motion', 'relative-motion', null),
  -- P4 Forces
  ((select id from public.schools where slug = 'rainford-high'), 'KS3', 7, null, null, (select id from public.subjects where name = 'Physics'), 4, 'Forces', 'what-a-force-is', null),
  ((select id from public.schools where slug = 'rainford-high'), 'KS3', 7, null, null, (select id from public.subjects where name = 'Physics'), 5, 'Forces', 'drawing-and-adding-forces', null),
  ((select id from public.schools where slug = 'rainford-high'), 'KS3', 7, null, null, (select id from public.subjects where name = 'Physics'), 6, 'Forces', 'balanced-and-unbalanced', null),
  ((select id from public.schools where slug = 'rainford-high'), 'KS3', 7, null, null, (select id from public.subjects where name = 'Physics'), 7, 'Forces', 'what-forces-do-to-motion', null),
  ((select id from public.schools where slug = 'rainford-high'), 'KS3', 7, null, null, (select id from public.subjects where name = 'Physics'), 8, 'Forces', 'friction', null),
  ((select id from public.schools where slug = 'rainford-high'), 'KS3', 7, null, null, (select id from public.subjects where name = 'Physics'), 9, 'Forces', 'air-and-water-resistance', null),
  ((select id from public.schools where slug = 'rainford-high'), 'KS3', 7, null, null, (select id from public.subjects where name = 'Physics'), 10, 'Forces', 'moments', null),
  ((select id from public.schools where slug = 'rainford-high'), 'KS3', 7, null, null, (select id from public.subjects where name = 'Physics'), 11, 'Forces', 'springs-and-hookes-law', null),
  ((select id from public.schools where slug = 'rainford-high'), 'KS3', 7, null, null, (select id from public.subjects where name = 'Physics'), 12, 'Forces', 'non-contact-forces', null),
  -- P8 Electric circuits
  ((select id from public.schools where slug = 'rainford-high'), 'KS3', 7, null, null, (select id from public.subjects where name = 'Physics'), 13, 'Electric circuits', 'current-and-circuits', null),
  ((select id from public.schools where slug = 'rainford-high'), 'KS3', 7, null, null, (select id from public.subjects where name = 'Physics'), 14, 'Electric circuits', 'series-and-parallel', null),
  ((select id from public.schools where slug = 'rainford-high'), 'KS3', 7, null, null, (select id from public.subjects where name = 'Physics'), 15, 'Electric circuits', 'current-at-a-junction', null),
  ((select id from public.schools where slug = 'rainford-high'), 'KS3', 7, null, null, (select id from public.subjects where name = 'Physics'), 16, 'Electric circuits', 'potential-difference', null),
  ((select id from public.schools where slug = 'rainford-high'), 'KS3', 7, null, null, (select id from public.subjects where name = 'Physics'), 17, 'Electric circuits', 'resistance', null),
  ((select id from public.schools where slug = 'rainford-high'), 'KS3', 7, null, null, (select id from public.subjects where name = 'Physics'), 18, 'Electric circuits', 'conductors-and-insulators', null),
  ((select id from public.schools where slug = 'rainford-high'), 'KS3', 7, null, null, (select id from public.subjects where name = 'Physics'), 19, 'Electric circuits', 'building-and-measuring-a-circuit', null),
  -- P9 Static electricity
  ((select id from public.schools where slug = 'rainford-high'), 'KS3', 7, null, null, (select id from public.subjects where name = 'Physics'), 20, 'Static electricity', 'charging-by-rubbing', null),
  ((select id from public.schools where slug = 'rainford-high'), 'KS3', 7, null, null, (select id from public.subjects where name = 'Physics'), 21, 'Static electricity', 'forces-between-charges', null),
  ((select id from public.schools where slug = 'rainford-high'), 'KS3', 7, null, null, (select id from public.subjects where name = 'Physics'), 22, 'Static electricity', 'electric-fields', null),
  -- P10 Magnetism and electromagnetism
  ((select id from public.schools where slug = 'rainford-high'), 'KS3', 7, null, null, (select id from public.subjects where name = 'Physics'), 23, 'Magnetism and electromagnetism', 'magnets-and-poles', null),
  ((select id from public.schools where slug = 'rainford-high'), 'KS3', 7, null, null, (select id from public.subjects where name = 'Physics'), 24, 'Magnetism and electromagnetism', 'magnetic-fields', null),
  ((select id from public.schools where slug = 'rainford-high'), 'KS3', 7, null, null, (select id from public.subjects where name = 'Physics'), 25, 'Magnetism and electromagnetism', 'the-earth-is-a-magnet', null),
  ((select id from public.schools where slug = 'rainford-high'), 'KS3', 7, null, null, (select id from public.subjects where name = 'Physics'), 26, 'Magnetism and electromagnetism', 'electromagnets', null),
  ((select id from public.schools where slug = 'rainford-high'), 'KS3', 7, null, null, (select id from public.subjects where name = 'Physics'), 27, 'Magnetism and electromagnetism', 'how-a-motor-works', null),
  -- P12 Space
  ((select id from public.schools where slug = 'rainford-high'), 'KS3', 7, null, null, (select id from public.subjects where name = 'Physics'), 28, 'Space', 'gravity-and-weight', null),
  ((select id from public.schools where slug = 'rainford-high'), 'KS3', 7, null, null, (select id from public.subjects where name = 'Physics'), 29, 'Space', 'mass-vs-weight', null),
  ((select id from public.schools where slug = 'rainford-high'), 'KS3', 7, null, null, (select id from public.subjects where name = 'Physics'), 30, 'Space', 'gravity-earth-moon-and-sun', null),
  ((select id from public.schools where slug = 'rainford-high'), 'KS3', 7, null, null, (select id from public.subjects where name = 'Physics'), 31, 'Space', 'the-sun-stars-and-galaxies', null),
  ((select id from public.schools where slug = 'rainford-high'), 'KS3', 7, null, null, (select id from public.subjects where name = 'Physics'), 32, 'Space', 'seasons-and-the-tilt', null),
  ((select id from public.schools where slug = 'rainford-high'), 'KS3', 7, null, null, (select id from public.subjects where name = 'Physics'), 33, 'Space', 'how-far-is-a-light-year', null);

-- ── Year 8 · Biology — 29 lessons ─────────────────────────
insert into public.scheme_of_work_overrides
  (school_id, key_stage, year_group, tier, pathway, subject_id, academic_week, topic, subtopic, notes)
values
  -- B4 Breathing and gas exchange
  ((select id from public.schools where slug = 'rainford-high'), 'KS3', 8, null, null, (select id from public.subjects where name = 'Biology'), 1, 'Breathing and gas exchange', 'the-gas-exchange-system', null),
  ((select id from public.schools where slug = 'rainford-high'), 'KS3', 8, null, null, (select id from public.subjects where name = 'Biology'), 2, 'Breathing and gas exchange', 'how-breathing-works', null),
  ((select id from public.schools where slug = 'rainford-high'), 'KS3', 8, null, null, (select id from public.subjects where name = 'Biology'), 3, 'Breathing and gas exchange', 'alveoli-built-for-exchange', null),
  ((select id from public.schools where slug = 'rainford-high'), 'KS3', 8, null, null, (select id from public.subjects where name = 'Biology'), 4, 'Breathing and gas exchange', 'exercise-asthma-and-smoking', null),
  ((select id from public.schools where slug = 'rainford-high'), 'KS3', 8, null, null, (select id from public.subjects where name = 'Biology'), 5, 'Breathing and gas exchange', 'stomata-and-gas-exchange-in-plants', null),
  -- B7 Photosynthesis
  ((select id from public.schools where slug = 'rainford-high'), 'KS3', 8, null, null, (select id from public.subjects where name = 'Biology'), 6, 'Photosynthesis', 'the-photosynthesis-reaction', null),
  ((select id from public.schools where slug = 'rainford-high'), 'KS3', 8, null, null, (select id from public.subjects where name = 'Biology'), 7, 'Photosynthesis', 'leaves-built-for-the-job', null),
  ((select id from public.schools where slug = 'rainford-high'), 'KS3', 8, null, null, (select id from public.subjects where name = 'Biology'), 8, 'Photosynthesis', 'testing-a-leaf-for-starch', null),
  ((select id from public.schools where slug = 'rainford-high'), 'KS3', 8, null, null, (select id from public.subjects where name = 'Biology'), 9, 'Photosynthesis', 'why-almost-all-life-depends-on-it', null),
  -- B8 Respiration
  ((select id from public.schools where slug = 'rainford-high'), 'KS3', 8, null, null, (select id from public.subjects where name = 'Biology'), 10, 'Respiration', 'aerobic-respiration', null),
  ((select id from public.schools where slug = 'rainford-high'), 'KS3', 8, null, null, (select id from public.subjects where name = 'Biology'), 11, 'Respiration', 'why-every-cell-respires', null),
  ((select id from public.schools where slug = 'rainford-high'), 'KS3', 8, null, null, (select id from public.subjects where name = 'Biology'), 12, 'Respiration', 'anaerobic-respiration-in-humans', null),
  ((select id from public.schools where slug = 'rainford-high'), 'KS3', 8, null, null, (select id from public.subjects where name = 'Biology'), 13, 'Respiration', 'fermentation', null),
  ((select id from public.schools where slug = 'rainford-high'), 'KS3', 8, null, null, (select id from public.subjects where name = 'Biology'), 14, 'Respiration', 'aerobic-vs-anaerobic', null),
  -- B9 Ecosystems and interdependence
  ((select id from public.schools where slug = 'rainford-high'), 'KS3', 8, null, null, (select id from public.subjects where name = 'Biology'), 15, 'Ecosystems and interdependence', 'food-chains-and-food-webs', null),
  ((select id from public.schools where slug = 'rainford-high'), 'KS3', 8, null, null, (select id from public.subjects where name = 'Biology'), 16, 'Ecosystems and interdependence', 'predator-and-prey', null),
  ((select id from public.schools where slug = 'rainford-high'), 'KS3', 8, null, null, (select id from public.subjects where name = 'Biology'), 17, 'Ecosystems and interdependence', 'disturbing-a-food-web', null),
  ((select id from public.schools where slug = 'rainford-high'), 'KS3', 8, null, null, (select id from public.subjects where name = 'Biology'), 18, 'Ecosystems and interdependence', 'pollinators-and-food-security', null),
  ((select id from public.schools where slug = 'rainford-high'), 'KS3', 8, null, null, (select id from public.subjects where name = 'Biology'), 19, 'Ecosystems and interdependence', 'toxic-build-up-in-a-food-chain', null),
  ((select id from public.schools where slug = 'rainford-high'), 'KS3', 8, null, null, (select id from public.subjects where name = 'Biology'), 20, 'Ecosystems and interdependence', 'sampling-an-ecosystem', null),
  -- B10 Inheritance and DNA
  ((select id from public.schools where slug = 'rainford-high'), 'KS3', 8, null, null, (select id from public.subjects where name = 'Biology'), 21, 'Inheritance and DNA', 'variation-continuous-and-discontinuous', null),
  ((select id from public.schools where slug = 'rainford-high'), 'KS3', 8, null, null, (select id from public.subjects where name = 'Biology'), 22, 'Inheritance and DNA', 'chromosomes-genes-and-dna', null),
  ((select id from public.schools where slug = 'rainford-high'), 'KS3', 8, null, null, (select id from public.subjects where name = 'Biology'), 23, 'Inheritance and DNA', 'how-we-worked-out-dna', null),
  ((select id from public.schools where slug = 'rainford-high'), 'KS3', 8, null, null, (select id from public.subjects where name = 'Biology'), 24, 'Inheritance and DNA', 'passing-it-on-heredity', null),
  ((select id from public.schools where slug = 'rainford-high'), 'KS3', 8, null, null, (select id from public.subjects where name = 'Biology'), 25, 'Inheritance and DNA', 'what-makes-a-species', null),
  -- B11 Evolution, extinction and biodiversity
  ((select id from public.schools where slug = 'rainford-high'), 'KS3', 8, null, null, (select id from public.subjects where name = 'Biology'), 26, 'Evolution, extinction and biodiversity', 'variation-and-competitive-success', null),
  ((select id from public.schools where slug = 'rainford-high'), 'KS3', 8, null, null, (select id from public.subjects where name = 'Biology'), 27, 'Evolution, extinction and biodiversity', 'natural-selection', null),
  ((select id from public.schools where slug = 'rainford-high'), 'KS3', 8, null, null, (select id from public.subjects where name = 'Biology'), 28, 'Evolution, extinction and biodiversity', 'when-the-environment-changes-extinction', null),
  ((select id from public.schools where slug = 'rainford-high'), 'KS3', 8, null, null, (select id from public.subjects where name = 'Biology'), 29, 'Evolution, extinction and biodiversity', 'biodiversity-and-gene-banks', null);

-- ── Year 8 · Chemistry — 24 lessons ─────────────────────────
insert into public.scheme_of_work_overrides
  (school_id, key_stage, year_group, tier, pathway, subject_id, academic_week, topic, subtopic, notes)
values
  -- C2 Atoms, elements and compounds
  ((select id from public.schools where slug = 'rainford-high'), 'KS3', 8, null, null, (select id from public.subjects where name = 'Chemistry'), 1, 'Atoms, elements and compounds', 'the-atom-daltons-model', null),
  ((select id from public.schools where slug = 'rainford-high'), 'KS3', 8, null, null, (select id from public.subjects where name = 'Chemistry'), 2, 'Atoms, elements and compounds', 'elements', null),
  ((select id from public.schools where slug = 'rainford-high'), 'KS3', 8, null, null, (select id from public.subjects where name = 'Chemistry'), 3, 'Atoms, elements and compounds', 'compounds', null),
  ((select id from public.schools where slug = 'rainford-high'), 'KS3', 8, null, null, (select id from public.subjects where name = 'Chemistry'), 4, 'Atoms, elements and compounds', 'chemical-symbols', null),
  ((select id from public.schools where slug = 'rainford-high'), 'KS3', 8, null, null, (select id from public.subjects where name = 'Chemistry'), 5, 'Atoms, elements and compounds', 'formulae', null),
  ((select id from public.schools where slug = 'rainford-high'), 'KS3', 8, null, null, (select id from public.subjects where name = 'Chemistry'), 6, 'Atoms, elements and compounds', 'conservation-of-mass', null),
  -- C6 Acids and alkalis
  ((select id from public.schools where slug = 'rainford-high'), 'KS3', 8, null, null, (select id from public.subjects where name = 'Chemistry'), 7, 'Acids and alkalis', 'acids-and-alkalis', null),
  ((select id from public.schools where slug = 'rainford-high'), 'KS3', 8, null, null, (select id from public.subjects where name = 'Chemistry'), 8, 'Acids and alkalis', 'the-ph-scale-and-indicators', null),
  ((select id from public.schools where slug = 'rainford-high'), 'KS3', 8, null, null, (select id from public.subjects where name = 'Chemistry'), 9, 'Acids and alkalis', 'neutralisation', null),
  ((select id from public.schools where slug = 'rainford-high'), 'KS3', 8, null, null, (select id from public.subjects where name = 'Chemistry'), 10, 'Acids and alkalis', 'acid-plus-metal', null),
  ((select id from public.schools where slug = 'rainford-high'), 'KS3', 8, null, null, (select id from public.subjects where name = 'Chemistry'), 11, 'Acids and alkalis', 'acid-plus-alkali', null),
  ((select id from public.schools where slug = 'rainford-high'), 'KS3', 8, null, null, (select id from public.subjects where name = 'Chemistry'), 12, 'Acids and alkalis', 'making-a-pure-dry-salt', null),
  ((select id from public.schools where slug = 'rainford-high'), 'KS3', 8, null, null, (select id from public.subjects where name = 'Chemistry'), 13, 'Acids and alkalis', 'catalysts', null),
  -- C8 The periodic table
  ((select id from public.schools where slug = 'rainford-high'), 'KS3', 8, null, null, (select id from public.subjects where name = 'Chemistry'), 14, 'The periodic table', 'metals-and-non-metals', null),
  ((select id from public.schools where slug = 'rainford-high'), 'KS3', 8, null, null, (select id from public.subjects where name = 'Chemistry'), 15, 'The periodic table', 'mendeleev', null),
  ((select id from public.schools where slug = 'rainford-high'), 'KS3', 8, null, null, (select id from public.subjects where name = 'Chemistry'), 16, 'The periodic table', 'groups-and-periods', null),
  ((select id from public.schools where slug = 'rainford-high'), 'KS3', 8, null, null, (select id from public.subjects where name = 'Chemistry'), 17, 'The periodic table', 'patterns-you-can-predict', null),
  ((select id from public.schools where slug = 'rainford-high'), 'KS3', 8, null, null, (select id from public.subjects where name = 'Chemistry'), 18, 'The periodic table', 'metal-and-non-metal-oxides', null),
  -- C10 The Earth and its atmosphere
  ((select id from public.schools where slug = 'rainford-high'), 'KS3', 8, null, null, (select id from public.subjects where name = 'Chemistry'), 19, 'The Earth and its atmosphere', 'inside-the-earth', null),
  ((select id from public.schools where slug = 'rainford-high'), 'KS3', 8, null, null, (select id from public.subjects where name = 'Chemistry'), 20, 'The Earth and its atmosphere', 'three-ways-to-make-a-rock', null),
  ((select id from public.schools where slug = 'rainford-high'), 'KS3', 8, null, null, (select id from public.subjects where name = 'Chemistry'), 21, 'The Earth and its atmosphere', 'the-rock-cycle', null),
  ((select id from public.schools where slug = 'rainford-high'), 'KS3', 8, null, null, (select id from public.subjects where name = 'Chemistry'), 22, 'The Earth and its atmosphere', 'a-planet-with-limits', null),
  ((select id from public.schools where slug = 'rainford-high'), 'KS3', 8, null, null, (select id from public.subjects where name = 'Chemistry'), 23, 'The Earth and its atmosphere', 'whats-in-the-air', null),
  ((select id from public.schools where slug = 'rainford-high'), 'KS3', 8, null, null, (select id from public.subjects where name = 'Chemistry'), 24, 'The Earth and its atmosphere', 'carbon-dioxide-humans-and-climate', null);

-- ── Year 8 · Physics — 37 lessons ─────────────────────────
insert into public.scheme_of_work_overrides
  (school_id, key_stage, year_group, tier, pathway, subject_id, academic_week, topic, subtopic, notes)
values
  -- P1 Energy transfers
  ((select id from public.schools where slug = 'rainford-high'), 'KS3', 8, null, null, (select id from public.subjects where name = 'Physics'), 1, 'Energy transfers', 'energy-stores', 'Energy ruled Y8 on strict Rainford, against the Y7 consensus of Ark and both Opus 4.8 passes. Revisable — year is soft (§4.5).'),
  ((select id from public.schools where slug = 'rainford-high'), 'KS3', 8, null, null, (select id from public.subjects where name = 'Physics'), 2, 'Energy transfers', 'energy-transfers-before-and-after', null),
  ((select id from public.schools where slug = 'rainford-high'), 'KS3', 8, null, null, (select id from public.subjects where name = 'Physics'), 3, 'Energy transfers', 'conservation-of-energy', null),
  ((select id from public.schools where slug = 'rainford-high'), 'KS3', 8, null, null, (select id from public.subjects where name = 'Physics'), 4, 'Energy transfers', 'heating-and-thermal-equilibrium', null),
  ((select id from public.schools where slug = 'rainford-high'), 'KS3', 8, null, null, (select id from public.subjects where name = 'Physics'), 5, 'Energy transfers', 'conduction', null),
  ((select id from public.schools where slug = 'rainford-high'), 'KS3', 8, null, null, (select id from public.subjects where name = 'Physics'), 6, 'Energy transfers', 'radiation', null),
  ((select id from public.schools where slug = 'rainford-high'), 'KS3', 8, null, null, (select id from public.subjects where name = 'Physics'), 7, 'Energy transfers', 'insulation', null),
  ((select id from public.schools where slug = 'rainford-high'), 'KS3', 8, null, null, (select id from public.subjects where name = 'Physics'), 8, 'Energy transfers', 'simple-machines', null),
  -- P2 Energy at home
  ((select id from public.schools where slug = 'rainford-high'), 'KS3', 8, null, null, (select id from public.subjects where name = 'Physics'), 9, 'Energy at home', 'energy-in-food', null),
  ((select id from public.schools where slug = 'rainford-high'), 'KS3', 8, null, null, (select id from public.subjects where name = 'Physics'), 10, 'Energy at home', 'power-ratings-in-watts', null),
  ((select id from public.schools where slug = 'rainford-high'), 'KS3', 8, null, null, (select id from public.subjects where name = 'Physics'), 11, 'Energy at home', 'calculating-energy-transferred', null),
  ((select id from public.schools where slug = 'rainford-high'), 'KS3', 8, null, null, (select id from public.subjects where name = 'Physics'), 12, 'Energy at home', 'reading-a-fuel-bill', null),
  ((select id from public.schools where slug = 'rainford-high'), 'KS3', 8, null, null, (select id from public.subjects where name = 'Physics'), 13, 'Energy at home', 'fuels-and-energy-resources', null),
  -- P5 Pressure
  ((select id from public.schools where slug = 'rainford-high'), 'KS3', 8, null, null, (select id from public.subjects where name = 'Physics'), 14, 'Pressure', 'pressure-force-over-area', null),
  ((select id from public.schools where slug = 'rainford-high'), 'KS3', 8, null, null, (select id from public.subjects where name = 'Physics'), 15, 'Pressure', 'pressure-in-liquids', null),
  ((select id from public.schools where slug = 'rainford-high'), 'KS3', 8, null, null, (select id from public.subjects where name = 'Physics'), 16, 'Pressure', 'upthrust-floating-and-sinking', null),
  ((select id from public.schools where slug = 'rainford-high'), 'KS3', 8, null, null, (select id from public.subjects where name = 'Physics'), 17, 'Pressure', 'atmospheric-pressure', null),
  -- P6 Waves and sound
  ((select id from public.schools where slug = 'rainford-high'), 'KS3', 8, null, null, (select id from public.subjects where name = 'Physics'), 18, 'Waves and sound', 'waves-on-water', null),
  ((select id from public.schools where slug = 'rainford-high'), 'KS3', 8, null, null, (select id from public.subjects where name = 'Physics'), 19, 'Waves and sound', 'transverse-waves-and-superposition', null),
  ((select id from public.schools where slug = 'rainford-high'), 'KS3', 8, null, null, (select id from public.subjects where name = 'Physics'), 20, 'Waves and sound', 'how-sound-is-made', null),
  ((select id from public.schools where slug = 'rainford-high'), 'KS3', 8, null, null, (select id from public.subjects where name = 'Physics'), 21, 'Waves and sound', 'sound-is-longitudinal', null),
  ((select id from public.schools where slug = 'rainford-high'), 'KS3', 8, null, null, (select id from public.subjects where name = 'Physics'), 22, 'Waves and sound', 'frequency-pitch-and-loudness', null),
  ((select id from public.schools where slug = 'rainford-high'), 'KS3', 8, null, null, (select id from public.subjects where name = 'Physics'), 23, 'Waves and sound', 'sound-needs-a-medium', null),
  ((select id from public.schools where slug = 'rainford-high'), 'KS3', 8, null, null, (select id from public.subjects where name = 'Physics'), 24, 'Waves and sound', 'echoes-reflection-and-absorption', null),
  ((select id from public.schools where slug = 'rainford-high'), 'KS3', 8, null, null, (select id from public.subjects where name = 'Physics'), 25, 'Waves and sound', 'hearing-and-auditory-range', null),
  ((select id from public.schools where slug = 'rainford-high'), 'KS3', 8, null, null, (select id from public.subjects where name = 'Physics'), 26, 'Waves and sound', 'ultrasound-at-work', null),
  -- P7 Light
  ((select id from public.schools where slug = 'rainford-high'), 'KS3', 8, null, null, (select id from public.subjects where name = 'Physics'), 27, 'Light', 'light-travels', null),
  ((select id from public.schools where slug = 'rainford-high'), 'KS3', 8, null, null, (select id from public.subjects where name = 'Physics'), 28, 'Light', 'reflection-mirrors-and-scattering', null),
  ((select id from public.schools where slug = 'rainford-high'), 'KS3', 8, null, null, (select id from public.subjects where name = 'Physics'), 29, 'Light', 'refraction', null),
  ((select id from public.schools where slug = 'rainford-high'), 'KS3', 8, null, null, (select id from public.subjects where name = 'Physics'), 30, 'Light', 'lenses-and-images', null),
  ((select id from public.schools where slug = 'rainford-high'), 'KS3', 8, null, null, (select id from public.subjects where name = 'Physics'), 31, 'Light', 'the-eye-and-the-camera', null),
  ((select id from public.schools where slug = 'rainford-high'), 'KS3', 8, null, null, (select id from public.subjects where name = 'Physics'), 32, 'Light', 'colour-and-the-spectrum', null),
  ((select id from public.schools where slug = 'rainford-high'), 'KS3', 8, null, null, (select id from public.subjects where name = 'Physics'), 33, 'Light', 'why-things-look-coloured', null),
  -- P11 Matter and the particle model
  ((select id from public.schools where slug = 'rainford-high'), 'KS3', 8, null, null, (select id from public.subjects where name = 'Physics'), 34, 'Matter and the particle model', 'density', null),
  ((select id from public.schools where slug = 'rainford-high'), 'KS3', 8, null, null, (select id from public.subjects where name = 'Physics'), 35, 'Matter and the particle model', 'brownian-motion', null),
  ((select id from public.schools where slug = 'rainford-high'), 'KS3', 8, null, null, (select id from public.subjects where name = 'Physics'), 36, 'Matter and the particle model', 'temperature-and-internal-energy', null),
  ((select id from public.schools where slug = 'rainford-high'), 'KS3', 8, null, null, (select id from public.subjects where name = 'Physics'), 37, 'Matter and the particle model', 'why-ice-floats', null);

-- ── Year 9 · Biology — 3 lessons ─────────────────────────
insert into public.scheme_of_work_overrides
  (school_id, key_stage, year_group, tier, pathway, subject_id, academic_week, topic, subtopic, notes)
values
  -- B6 Health and drugs
  ((select id from public.schools where slug = 'rainford-high'), 'KS3', 9, null, null, (select id from public.subjects where name = 'Biology'), 1, 'Health and drugs', 'what-drugs-do-to-the-body', null),
  ((select id from public.schools where slug = 'rainford-high'), 'KS3', 9, null, null, (select id from public.subjects where name = 'Biology'), 2, 'Health and drugs', 'alcohol-and-smoking', null),
  ((select id from public.schools where slug = 'rainford-high'), 'KS3', 9, null, null, (select id from public.subjects where name = 'Biology'), 3, 'Health and drugs', 'substance-misuse-and-decisions', null);

commit;
