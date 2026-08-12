-- ═══════════════════════════════════════════════════════════════════════
-- KS3 — MrBadmusAI default sequence v1, as scheme-of-work rows.
--
-- ⚠️ GENERATED FILE — DO NOT EDIT BY HAND.
--    Regenerate with:  python3 ks3_seed_sow.py
--    Source of truth:  ks3_data/structure.py, ks3_data/default_sequence.py,
--                      ks3_data/school_schemes.py
--    Written to:       supabase/seeds/20260726181000_ks3_default_sequence.sql
--    Target table:     public.scheme_of_work_entries (GLOBAL — no school_id)
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
-- This is the PLATFORM DEFAULT: what a school with nothing
-- configured gets. It is derived from the statutory spine and the
-- prerequisite graph, not from any school's timetable
-- (architecture.md §7, ruled 2026-07-26). A school overrides it by
-- writing scheme_of_work_overrides rows — see the companion seed.
--
-- KS3 has no exam board, no tier and no pathway: all three are NULL
-- on every row here, which the §8.7 migration both permits and
-- requires.
--
-- half_term (1-6) is where in the year the lesson falls. It is
-- METADATA under §4.5 exactly as year_group is, derived by
-- ks3_data/half_terms.py from this same default sequence, and it
-- reaches no URL and no page byte. Requires migration
-- 20260806230345_ks3_scheme_of_work_half_term.sql.
--
-- Row counts, generated:
--
--   Y7  Biology 18 · Chemistry 19 · Physics 16
--   Y8  Biology 22 · Chemistry 22 · Physics 35
--   Y9  Biology 18 · Chemistry 14 · Physics 19
--   183 rows total, max academic_week 35 (ceiling 39)
--
-- Lessons per half term (HT1 … HT6), generated:
--
--   Y7 Biology     3  3  3  3  3  3   (18)
--   Y7 Chemistry   4  2  4  2  4  3   (19)
--   Y7 Physics     3  3  3  3  2  2   (16)
--   Y7 ALL        10  8 10  8  9  8   (53)
--   Y8 Biology     4  4  4  4  3  3   (22)
--   Y8 Chemistry   4  4  4  4  3  3   (22)
--   Y8 Physics     6  6  6  6  6  5   (35)
--   Y8 ALL        14 14 14 14 12 11   (79)
--   Y9 Biology     3  3  3  3  3  3   (18)
--   Y9 Chemistry   3  3  2  2  2  2   (14)
--   Y9 Physics     4  3  3  3  3  3   (19)
--   Y9 ALL        10  9  8  8  8  8   (51)
--
-- Every discipline appears in every half term of every year — that is
-- asserted in ks3_data/half_terms.py, not hoped for here.
--
-- ═══════════════════════════════════════════════════════════════════════

begin;

-- Preconditions. Failing here with a sentence beats failing later with a
-- NOT NULL violation on a subselect that quietly returned NULL.
do $$
begin
  if (select count(*) from public.subjects
       where name in ('Biology', 'Chemistry', 'Physics')) <> 3 then
    raise exception 'KS3 seed: public.subjects is missing one of Biology / '
                    'Chemistry / Physics. Seed the subjects table first.';
  end if;
end $$;

-- Idempotency: this file owns every KS3 row in the global table.
delete from public.scheme_of_work_entries where key_stage = 'KS3';

-- ── Year 7 · Biology — 18 lessons ─────────────────────────
insert into public.scheme_of_work_entries
  (key_stage, year_group, tier, pathway, subject_id, exam_board, academic_week, half_term, topic, subtopic, notes, active)
values
  -- B1 Cells and organisation
  ('KS3', 7, null, null, (select id from public.subjects where name = 'Biology'), null, 1, 1, 'Cells and organisation', 'life-processes', null, true),
  ('KS3', 7, null, null, (select id from public.subjects where name = 'Biology'), null, 2, 1, 'Cells and organisation', 'using-a-microscope', null, true),
  ('KS3', 7, null, null, (select id from public.subjects where name = 'Biology'), null, 3, 1, 'Cells and organisation', 'animal-and-plant-cells', null, true),
  ('KS3', 7, null, null, (select id from public.subjects where name = 'Biology'), null, 4, 2, 'Cells and organisation', 'specialised-cells', null, true),
  ('KS3', 7, null, null, (select id from public.subjects where name = 'Biology'), null, 5, 2, 'Cells and organisation', 'levels-of-organisation', null, true),
  ('KS3', 7, null, null, (select id from public.subjects where name = 'Biology'), null, 6, 2, 'Cells and organisation', 'unicellular-organisms', null, true),
  -- B2 Movement: skeleton and muscles
  ('KS3', 7, null, null, (select id from public.subjects where name = 'Biology'), null, 7, 3, 'Movement: skeleton and muscles', 'what-the-skeleton-does', null, true),
  ('KS3', 7, null, null, (select id from public.subjects where name = 'Biology'), null, 8, 3, 'Movement: skeleton and muscles', 'joints', null, true),
  ('KS3', 7, null, null, (select id from public.subjects where name = 'Biology'), null, 9, 3, 'Movement: skeleton and muscles', 'antagonistic-muscle-pairs', null, true),
  ('KS3', 7, null, null, (select id from public.subjects where name = 'Biology'), null, 10, 4, 'Movement: skeleton and muscles', 'biomechanics-forces-in-the-body', null, true),
  -- B3 Nutrition and digestion
  ('KS3', 7, null, null, (select id from public.subjects where name = 'Biology'), null, 11, 4, 'Nutrition and digestion', 'a-balanced-diet', null, true),
  ('KS3', 7, null, null, (select id from public.subjects where name = 'Biology'), null, 12, 4, 'Nutrition and digestion', 'food-tests', null, true),
  ('KS3', 7, null, null, (select id from public.subjects where name = 'Biology'), null, 13, 5, 'Nutrition and digestion', 'energy-in-food', 'Cross-reference (architecture.md §4.6): this lesson is owned by P2 Energy at home (Physics) and is taught from there. Listed here because Nutrition and digestion teaches the slot, not because the content is duplicated.', true),
  ('KS3', 7, null, null, (select id from public.subjects where name = 'Biology'), null, 14, 5, 'Nutrition and digestion', 'when-diet-goes-wrong', null, true),
  ('KS3', 7, null, null, (select id from public.subjects where name = 'Biology'), null, 15, 5, 'Nutrition and digestion', 'the-digestive-system', null, true),
  ('KS3', 7, null, null, (select id from public.subjects where name = 'Biology'), null, 16, 6, 'Nutrition and digestion', 'enzymes-in-digestion', null, true),
  ('KS3', 7, null, null, (select id from public.subjects where name = 'Biology'), null, 17, 6, 'Nutrition and digestion', 'absorption-and-the-small-intestine', null, true),
  ('KS3', 7, null, null, (select id from public.subjects where name = 'Biology'), null, 18, 6, 'Nutrition and digestion', 'bacteria-in-the-gut', null, true);

-- ── Year 7 · Chemistry — 19 lessons ─────────────────────────
insert into public.scheme_of_work_entries
  (key_stage, year_group, tier, pathway, subject_id, exam_board, academic_week, half_term, topic, subtopic, notes, active)
values
  -- C1 Particles and their behaviour
  ('KS3', 7, null, null, (select id from public.subjects where name = 'Chemistry'), null, 1, 1, 'Particles and their behaviour', 'particle-model', null, true),
  ('KS3', 7, null, null, (select id from public.subjects where name = 'Chemistry'), null, 2, 1, 'Particles and their behaviour', 'solids-liquids-and-gases', null, true),
  ('KS3', 7, null, null, (select id from public.subjects where name = 'Chemistry'), null, 3, 1, 'Particles and their behaviour', 'changes-of-state', null, true),
  ('KS3', 7, null, null, (select id from public.subjects where name = 'Chemistry'), null, 4, 1, 'Particles and their behaviour', 'gas-pressure', null, true),
  ('KS3', 7, null, null, (select id from public.subjects where name = 'Chemistry'), null, 5, 2, 'Particles and their behaviour', 'diffusion', null, true),
  ('KS3', 7, null, null, (select id from public.subjects where name = 'Chemistry'), null, 6, 2, 'Particles and their behaviour', 'testing-the-model', null, true),
  -- C2 Atoms, elements and compounds
  ('KS3', 7, null, null, (select id from public.subjects where name = 'Chemistry'), null, 7, 3, 'Atoms, elements and compounds', 'the-atom-daltons-model', null, true),
  ('KS3', 7, null, null, (select id from public.subjects where name = 'Chemistry'), null, 8, 3, 'Atoms, elements and compounds', 'elements', null, true),
  ('KS3', 7, null, null, (select id from public.subjects where name = 'Chemistry'), null, 9, 3, 'Atoms, elements and compounds', 'compounds', null, true),
  ('KS3', 7, null, null, (select id from public.subjects where name = 'Chemistry'), null, 10, 3, 'Atoms, elements and compounds', 'chemical-symbols', null, true),
  ('KS3', 7, null, null, (select id from public.subjects where name = 'Chemistry'), null, 11, 4, 'Atoms, elements and compounds', 'formulae', null, true),
  ('KS3', 7, null, null, (select id from public.subjects where name = 'Chemistry'), null, 12, 4, 'Atoms, elements and compounds', 'conservation-of-mass', null, true),
  -- C3 Mixtures and separation
  ('KS3', 7, null, null, (select id from public.subjects where name = 'Chemistry'), null, 13, 5, 'Mixtures and separation', 'pure-or-mixture', null, true),
  ('KS3', 7, null, null, (select id from public.subjects where name = 'Chemistry'), null, 14, 5, 'Mixtures and separation', 'dissolving-and-solutions', null, true),
  ('KS3', 7, null, null, (select id from public.subjects where name = 'Chemistry'), null, 15, 5, 'Mixtures and separation', 'filtration', null, true),
  ('KS3', 7, null, null, (select id from public.subjects where name = 'Chemistry'), null, 16, 5, 'Mixtures and separation', 'evaporation-and-crystallisation', null, true),
  ('KS3', 7, null, null, (select id from public.subjects where name = 'Chemistry'), null, 17, 6, 'Mixtures and separation', 'distillation', null, true),
  ('KS3', 7, null, null, (select id from public.subjects where name = 'Chemistry'), null, 18, 6, 'Mixtures and separation', 'chromatography', null, true),
  ('KS3', 7, null, null, (select id from public.subjects where name = 'Chemistry'), null, 19, 6, 'Mixtures and separation', 'proving-something-is-pure', null, true);

-- ── Year 7 · Physics — 16 lessons ─────────────────────────
insert into public.scheme_of_work_entries
  (key_stage, year_group, tier, pathway, subject_id, exam_board, academic_week, half_term, topic, subtopic, notes, active)
values
  -- P3 Describing motion
  ('KS3', 7, null, null, (select id from public.subjects where name = 'Physics'), null, 1, 1, 'Describing motion', 'speed', null, true),
  ('KS3', 7, null, null, (select id from public.subjects where name = 'Physics'), null, 2, 1, 'Describing motion', 'distance-time-graphs', null, true),
  ('KS3', 7, null, null, (select id from public.subjects where name = 'Physics'), null, 3, 1, 'Describing motion', 'relative-motion', null, true),
  -- P4 Forces
  ('KS3', 7, null, null, (select id from public.subjects where name = 'Physics'), null, 4, 2, 'Forces', 'what-a-force-is', null, true),
  ('KS3', 7, null, null, (select id from public.subjects where name = 'Physics'), null, 5, 2, 'Forces', 'drawing-and-adding-forces', null, true),
  ('KS3', 7, null, null, (select id from public.subjects where name = 'Physics'), null, 6, 2, 'Forces', 'balanced-and-unbalanced', null, true),
  ('KS3', 7, null, null, (select id from public.subjects where name = 'Physics'), null, 7, 3, 'Forces', 'what-forces-do-to-motion', null, true),
  ('KS3', 7, null, null, (select id from public.subjects where name = 'Physics'), null, 8, 3, 'Forces', 'friction', null, true),
  ('KS3', 7, null, null, (select id from public.subjects where name = 'Physics'), null, 9, 3, 'Forces', 'air-and-water-resistance', null, true),
  ('KS3', 7, null, null, (select id from public.subjects where name = 'Physics'), null, 10, 4, 'Forces', 'moments', null, true),
  ('KS3', 7, null, null, (select id from public.subjects where name = 'Physics'), null, 11, 4, 'Forces', 'springs-and-hookes-law', null, true),
  ('KS3', 7, null, null, (select id from public.subjects where name = 'Physics'), null, 12, 4, 'Forces', 'non-contact-forces', null, true),
  -- P11 Matter and the particle model
  ('KS3', 7, null, null, (select id from public.subjects where name = 'Physics'), null, 13, 5, 'Matter and the particle model', 'density', null, true),
  ('KS3', 7, null, null, (select id from public.subjects where name = 'Physics'), null, 14, 5, 'Matter and the particle model', 'brownian-motion', null, true),
  ('KS3', 7, null, null, (select id from public.subjects where name = 'Physics'), null, 15, 6, 'Matter and the particle model', 'temperature-and-internal-energy', null, true),
  ('KS3', 7, null, null, (select id from public.subjects where name = 'Physics'), null, 16, 6, 'Matter and the particle model', 'why-ice-floats', null, true);

-- ── Year 8 · Biology — 22 lessons ─────────────────────────
insert into public.scheme_of_work_entries
  (key_stage, year_group, tier, pathway, subject_id, exam_board, academic_week, half_term, topic, subtopic, notes, active)
values
  -- B4 Breathing and gas exchange
  ('KS3', 8, null, null, (select id from public.subjects where name = 'Biology'), null, 1, 1, 'Breathing and gas exchange', 'the-gas-exchange-system', null, true),
  ('KS3', 8, null, null, (select id from public.subjects where name = 'Biology'), null, 2, 1, 'Breathing and gas exchange', 'how-breathing-works', null, true),
  ('KS3', 8, null, null, (select id from public.subjects where name = 'Biology'), null, 3, 1, 'Breathing and gas exchange', 'alveoli-built-for-exchange', null, true),
  ('KS3', 8, null, null, (select id from public.subjects where name = 'Biology'), null, 4, 1, 'Breathing and gas exchange', 'exercise-asthma-and-smoking', null, true),
  ('KS3', 8, null, null, (select id from public.subjects where name = 'Biology'), null, 5, 2, 'Breathing and gas exchange', 'stomata-and-gas-exchange-in-plants', null, true),
  -- B5 Reproduction
  ('KS3', 8, null, null, (select id from public.subjects where name = 'Biology'), null, 6, 2, 'Reproduction', 'human-reproductive-systems', null, true),
  ('KS3', 8, null, null, (select id from public.subjects where name = 'Biology'), null, 7, 2, 'Reproduction', 'gametes-and-fertilisation', null, true),
  ('KS3', 8, null, null, (select id from public.subjects where name = 'Biology'), null, 8, 2, 'Reproduction', 'the-menstrual-cycle', null, true),
  ('KS3', 8, null, null, (select id from public.subjects where name = 'Biology'), null, 9, 3, 'Reproduction', 'gestation-placenta-and-birth', null, true),
  ('KS3', 8, null, null, (select id from public.subjects where name = 'Biology'), null, 10, 3, 'Reproduction', 'lifestyle-and-the-developing-foetus', null, true),
  ('KS3', 8, null, null, (select id from public.subjects where name = 'Biology'), null, 11, 3, 'Reproduction', 'flowers-and-pollination', null, true),
  ('KS3', 8, null, null, (select id from public.subjects where name = 'Biology'), null, 12, 3, 'Reproduction', 'fertilisation-seeds-and-fruit', null, true),
  ('KS3', 8, null, null, (select id from public.subjects where name = 'Biology'), null, 13, 4, 'Reproduction', 'seed-dispersal', null, true),
  -- B7 Photosynthesis
  ('KS3', 8, null, null, (select id from public.subjects where name = 'Biology'), null, 14, 4, 'Photosynthesis', 'the-photosynthesis-reaction', null, true),
  ('KS3', 8, null, null, (select id from public.subjects where name = 'Biology'), null, 15, 4, 'Photosynthesis', 'leaves-built-for-the-job', null, true),
  ('KS3', 8, null, null, (select id from public.subjects where name = 'Biology'), null, 16, 4, 'Photosynthesis', 'testing-a-leaf-for-starch', null, true),
  ('KS3', 8, null, null, (select id from public.subjects where name = 'Biology'), null, 17, 5, 'Photosynthesis', 'why-almost-all-life-depends-on-it', null, true),
  -- B8 Respiration
  ('KS3', 8, null, null, (select id from public.subjects where name = 'Biology'), null, 18, 5, 'Respiration', 'aerobic-respiration', null, true),
  ('KS3', 8, null, null, (select id from public.subjects where name = 'Biology'), null, 19, 5, 'Respiration', 'why-every-cell-respires', null, true),
  ('KS3', 8, null, null, (select id from public.subjects where name = 'Biology'), null, 20, 6, 'Respiration', 'anaerobic-respiration-in-humans', null, true),
  ('KS3', 8, null, null, (select id from public.subjects where name = 'Biology'), null, 21, 6, 'Respiration', 'fermentation', null, true),
  ('KS3', 8, null, null, (select id from public.subjects where name = 'Biology'), null, 22, 6, 'Respiration', 'aerobic-vs-anaerobic', null, true);

-- ── Year 8 · Chemistry — 22 lessons ─────────────────────────
insert into public.scheme_of_work_entries
  (key_stage, year_group, tier, pathway, subject_id, exam_board, academic_week, half_term, topic, subtopic, notes, active)
values
  -- C4 Chemical reactions
  ('KS3', 8, null, null, (select id from public.subjects where name = 'Chemistry'), null, 1, 1, 'Chemical reactions', 'chemical-vs-physical-change', null, true),
  ('KS3', 8, null, null, (select id from public.subjects where name = 'Chemistry'), null, 2, 1, 'Chemical reactions', 'reactions-rearrange-atoms', null, true),
  ('KS3', 8, null, null, (select id from public.subjects where name = 'Chemistry'), null, 3, 1, 'Chemical reactions', 'word-equations', null, true),
  ('KS3', 8, null, null, (select id from public.subjects where name = 'Chemistry'), null, 4, 1, 'Chemical reactions', 'mass-in-a-reaction', null, true),
  ('KS3', 8, null, null, (select id from public.subjects where name = 'Chemistry'), null, 5, 2, 'Chemical reactions', 'symbol-equations-and-balancing', null, true),
  -- C5 Types of reaction
  ('KS3', 8, null, null, (select id from public.subjects where name = 'Chemistry'), null, 6, 2, 'Types of reaction', 'combustion', null, true),
  ('KS3', 8, null, null, (select id from public.subjects where name = 'Chemistry'), null, 7, 2, 'Types of reaction', 'thermal-decomposition', null, true),
  ('KS3', 8, null, null, (select id from public.subjects where name = 'Chemistry'), null, 8, 2, 'Types of reaction', 'oxidation', null, true),
  ('KS3', 8, null, null, (select id from public.subjects where name = 'Chemistry'), null, 9, 3, 'Types of reaction', 'displacement', null, true),
  ('KS3', 8, null, null, (select id from public.subjects where name = 'Chemistry'), null, 10, 3, 'Types of reaction', 'which-reaction-is-this', null, true),
  -- C6 Acids and alkalis
  ('KS3', 8, null, null, (select id from public.subjects where name = 'Chemistry'), null, 11, 3, 'Acids and alkalis', 'acids-and-alkalis', null, true),
  ('KS3', 8, null, null, (select id from public.subjects where name = 'Chemistry'), null, 12, 3, 'Acids and alkalis', 'the-ph-scale-and-indicators', null, true),
  ('KS3', 8, null, null, (select id from public.subjects where name = 'Chemistry'), null, 13, 4, 'Acids and alkalis', 'neutralisation', null, true),
  ('KS3', 8, null, null, (select id from public.subjects where name = 'Chemistry'), null, 14, 4, 'Acids and alkalis', 'acid-plus-metal', null, true),
  ('KS3', 8, null, null, (select id from public.subjects where name = 'Chemistry'), null, 15, 4, 'Acids and alkalis', 'acid-plus-alkali', null, true),
  ('KS3', 8, null, null, (select id from public.subjects where name = 'Chemistry'), null, 16, 4, 'Acids and alkalis', 'making-a-pure-dry-salt', null, true),
  ('KS3', 8, null, null, (select id from public.subjects where name = 'Chemistry'), null, 17, 5, 'Acids and alkalis', 'catalysts', null, true),
  -- C8 The periodic table
  ('KS3', 8, null, null, (select id from public.subjects where name = 'Chemistry'), null, 18, 5, 'The periodic table', 'metals-and-non-metals', null, true),
  ('KS3', 8, null, null, (select id from public.subjects where name = 'Chemistry'), null, 19, 5, 'The periodic table', 'mendeleev', null, true),
  ('KS3', 8, null, null, (select id from public.subjects where name = 'Chemistry'), null, 20, 6, 'The periodic table', 'groups-and-periods', null, true),
  ('KS3', 8, null, null, (select id from public.subjects where name = 'Chemistry'), null, 21, 6, 'The periodic table', 'patterns-you-can-predict', null, true),
  ('KS3', 8, null, null, (select id from public.subjects where name = 'Chemistry'), null, 22, 6, 'The periodic table', 'metal-and-non-metal-oxides', null, true);

-- ── Year 8 · Physics — 35 lessons ─────────────────────────
insert into public.scheme_of_work_entries
  (key_stage, year_group, tier, pathway, subject_id, exam_board, academic_week, half_term, topic, subtopic, notes, active)
values
  -- P5 Pressure
  ('KS3', 8, null, null, (select id from public.subjects where name = 'Physics'), null, 1, 1, 'Pressure', 'pressure-force-over-area', null, true),
  ('KS3', 8, null, null, (select id from public.subjects where name = 'Physics'), null, 2, 1, 'Pressure', 'pressure-in-liquids', null, true),
  ('KS3', 8, null, null, (select id from public.subjects where name = 'Physics'), null, 3, 1, 'Pressure', 'upthrust-floating-and-sinking', null, true),
  ('KS3', 8, null, null, (select id from public.subjects where name = 'Physics'), null, 4, 1, 'Pressure', 'atmospheric-pressure', null, true),
  -- P1 Energy transfers
  ('KS3', 8, null, null, (select id from public.subjects where name = 'Physics'), null, 5, 1, 'Energy transfers', 'energy-stores', null, true),
  ('KS3', 8, null, null, (select id from public.subjects where name = 'Physics'), null, 6, 1, 'Energy transfers', 'energy-transfers-before-and-after', null, true),
  ('KS3', 8, null, null, (select id from public.subjects where name = 'Physics'), null, 7, 2, 'Energy transfers', 'conservation-of-energy', null, true),
  ('KS3', 8, null, null, (select id from public.subjects where name = 'Physics'), null, 8, 2, 'Energy transfers', 'heating-and-thermal-equilibrium', null, true),
  ('KS3', 8, null, null, (select id from public.subjects where name = 'Physics'), null, 9, 2, 'Energy transfers', 'conduction', null, true),
  ('KS3', 8, null, null, (select id from public.subjects where name = 'Physics'), null, 10, 2, 'Energy transfers', 'radiation', null, true),
  ('KS3', 8, null, null, (select id from public.subjects where name = 'Physics'), null, 11, 2, 'Energy transfers', 'insulation', null, true),
  ('KS3', 8, null, null, (select id from public.subjects where name = 'Physics'), null, 12, 2, 'Energy transfers', 'simple-machines', null, true),
  -- P6 Waves and sound
  ('KS3', 8, null, null, (select id from public.subjects where name = 'Physics'), null, 13, 3, 'Waves and sound', 'waves-on-water', null, true),
  ('KS3', 8, null, null, (select id from public.subjects where name = 'Physics'), null, 14, 3, 'Waves and sound', 'transverse-waves-and-superposition', null, true),
  ('KS3', 8, null, null, (select id from public.subjects where name = 'Physics'), null, 15, 3, 'Waves and sound', 'how-sound-is-made', null, true),
  ('KS3', 8, null, null, (select id from public.subjects where name = 'Physics'), null, 16, 3, 'Waves and sound', 'sound-is-longitudinal', null, true),
  ('KS3', 8, null, null, (select id from public.subjects where name = 'Physics'), null, 17, 3, 'Waves and sound', 'frequency-pitch-and-loudness', null, true),
  ('KS3', 8, null, null, (select id from public.subjects where name = 'Physics'), null, 18, 3, 'Waves and sound', 'sound-needs-a-medium', null, true),
  ('KS3', 8, null, null, (select id from public.subjects where name = 'Physics'), null, 19, 4, 'Waves and sound', 'echoes-reflection-and-absorption', null, true),
  ('KS3', 8, null, null, (select id from public.subjects where name = 'Physics'), null, 20, 4, 'Waves and sound', 'hearing-and-auditory-range', null, true),
  ('KS3', 8, null, null, (select id from public.subjects where name = 'Physics'), null, 21, 4, 'Waves and sound', 'ultrasound-at-work', null, true),
  -- P7 Light
  ('KS3', 8, null, null, (select id from public.subjects where name = 'Physics'), null, 22, 4, 'Light', 'light-travels', null, true),
  ('KS3', 8, null, null, (select id from public.subjects where name = 'Physics'), null, 23, 4, 'Light', 'reflection-mirrors-and-scattering', null, true),
  ('KS3', 8, null, null, (select id from public.subjects where name = 'Physics'), null, 24, 4, 'Light', 'refraction', null, true),
  ('KS3', 8, null, null, (select id from public.subjects where name = 'Physics'), null, 25, 5, 'Light', 'lenses-and-images', null, true),
  ('KS3', 8, null, null, (select id from public.subjects where name = 'Physics'), null, 26, 5, 'Light', 'the-eye-and-the-camera', null, true),
  ('KS3', 8, null, null, (select id from public.subjects where name = 'Physics'), null, 27, 5, 'Light', 'colour-and-the-spectrum', null, true),
  ('KS3', 8, null, null, (select id from public.subjects where name = 'Physics'), null, 28, 5, 'Light', 'why-things-look-coloured', null, true),
  -- P8 Electric circuits
  ('KS3', 8, null, null, (select id from public.subjects where name = 'Physics'), null, 29, 5, 'Electric circuits', 'current-and-circuits', null, true),
  ('KS3', 8, null, null, (select id from public.subjects where name = 'Physics'), null, 30, 5, 'Electric circuits', 'series-and-parallel', null, true),
  ('KS3', 8, null, null, (select id from public.subjects where name = 'Physics'), null, 31, 6, 'Electric circuits', 'current-at-a-junction', null, true),
  ('KS3', 8, null, null, (select id from public.subjects where name = 'Physics'), null, 32, 6, 'Electric circuits', 'potential-difference', null, true),
  ('KS3', 8, null, null, (select id from public.subjects where name = 'Physics'), null, 33, 6, 'Electric circuits', 'resistance', null, true),
  ('KS3', 8, null, null, (select id from public.subjects where name = 'Physics'), null, 34, 6, 'Electric circuits', 'conductors-and-insulators', null, true),
  ('KS3', 8, null, null, (select id from public.subjects where name = 'Physics'), null, 35, 6, 'Electric circuits', 'building-and-measuring-a-circuit', null, true);

-- ── Year 9 · Biology — 18 lessons ─────────────────────────
insert into public.scheme_of_work_entries
  (key_stage, year_group, tier, pathway, subject_id, exam_board, academic_week, half_term, topic, subtopic, notes, active)
values
  -- B6 Health and drugs
  ('KS3', 9, null, null, (select id from public.subjects where name = 'Biology'), null, 1, 1, 'Health and drugs', 'what-drugs-do-to-the-body', null, true),
  ('KS3', 9, null, null, (select id from public.subjects where name = 'Biology'), null, 2, 1, 'Health and drugs', 'alcohol-and-smoking', null, true),
  ('KS3', 9, null, null, (select id from public.subjects where name = 'Biology'), null, 3, 1, 'Health and drugs', 'substance-misuse-and-decisions', null, true),
  -- B9 Ecosystems and interdependence
  ('KS3', 9, null, null, (select id from public.subjects where name = 'Biology'), null, 4, 2, 'Ecosystems and interdependence', 'food-chains-and-food-webs', null, true),
  ('KS3', 9, null, null, (select id from public.subjects where name = 'Biology'), null, 5, 2, 'Ecosystems and interdependence', 'predator-and-prey', null, true),
  ('KS3', 9, null, null, (select id from public.subjects where name = 'Biology'), null, 6, 2, 'Ecosystems and interdependence', 'disturbing-a-food-web', null, true),
  ('KS3', 9, null, null, (select id from public.subjects where name = 'Biology'), null, 7, 3, 'Ecosystems and interdependence', 'pollinators-and-food-security', null, true),
  ('KS3', 9, null, null, (select id from public.subjects where name = 'Biology'), null, 8, 3, 'Ecosystems and interdependence', 'toxic-build-up-in-a-food-chain', null, true),
  ('KS3', 9, null, null, (select id from public.subjects where name = 'Biology'), null, 9, 3, 'Ecosystems and interdependence', 'sampling-an-ecosystem', null, true),
  -- B10 Inheritance and DNA
  ('KS3', 9, null, null, (select id from public.subjects where name = 'Biology'), null, 10, 4, 'Inheritance and DNA', 'variation-continuous-and-discontinuous', null, true),
  ('KS3', 9, null, null, (select id from public.subjects where name = 'Biology'), null, 11, 4, 'Inheritance and DNA', 'chromosomes-genes-and-dna', null, true),
  ('KS3', 9, null, null, (select id from public.subjects where name = 'Biology'), null, 12, 4, 'Inheritance and DNA', 'how-we-worked-out-dna', null, true),
  ('KS3', 9, null, null, (select id from public.subjects where name = 'Biology'), null, 13, 5, 'Inheritance and DNA', 'passing-it-on-heredity', null, true),
  ('KS3', 9, null, null, (select id from public.subjects where name = 'Biology'), null, 14, 5, 'Inheritance and DNA', 'what-makes-a-species', null, true),
  -- B11 Evolution, extinction and biodiversity
  ('KS3', 9, null, null, (select id from public.subjects where name = 'Biology'), null, 15, 5, 'Evolution, extinction and biodiversity', 'variation-and-competitive-success', null, true),
  ('KS3', 9, null, null, (select id from public.subjects where name = 'Biology'), null, 16, 6, 'Evolution, extinction and biodiversity', 'natural-selection', null, true),
  ('KS3', 9, null, null, (select id from public.subjects where name = 'Biology'), null, 17, 6, 'Evolution, extinction and biodiversity', 'when-the-environment-changes-extinction', null, true),
  ('KS3', 9, null, null, (select id from public.subjects where name = 'Biology'), null, 18, 6, 'Evolution, extinction and biodiversity', 'biodiversity-and-gene-banks', null, true);

-- ── Year 9 · Chemistry — 14 lessons ─────────────────────────
insert into public.scheme_of_work_entries
  (key_stage, year_group, tier, pathway, subject_id, exam_board, academic_week, half_term, topic, subtopic, notes, active)
values
  -- C7 Energy changes in reactions
  ('KS3', 9, null, null, (select id from public.subjects where name = 'Chemistry'), null, 1, 1, 'Energy changes in reactions', 'energy-and-changes-of-state', null, true),
  ('KS3', 9, null, null, (select id from public.subjects where name = 'Chemistry'), null, 2, 1, 'Energy changes in reactions', 'exothermic-reactions', null, true),
  ('KS3', 9, null, null, (select id from public.subjects where name = 'Chemistry'), null, 3, 1, 'Energy changes in reactions', 'endothermic-reactions', null, true),
  ('KS3', 9, null, null, (select id from public.subjects where name = 'Chemistry'), null, 4, 2, 'Energy changes in reactions', 'measuring-a-temperature-change', null, true),
  -- C9 Metals and materials
  ('KS3', 9, null, null, (select id from public.subjects where name = 'Chemistry'), null, 5, 2, 'Metals and materials', 'the-reactivity-series', null, true),
  ('KS3', 9, null, null, (select id from public.subjects where name = 'Chemistry'), null, 6, 2, 'Metals and materials', 'predicting-displacement', null, true),
  ('KS3', 9, null, null, (select id from public.subjects where name = 'Chemistry'), null, 7, 3, 'Metals and materials', 'getting-metals-out-of-rocks', null, true),
  ('KS3', 9, null, null, (select id from public.subjects where name = 'Chemistry'), null, 8, 3, 'Metals and materials', 'ceramics-polymers-and-composites', null, true),
  -- C10 The Earth and its atmosphere
  ('KS3', 9, null, null, (select id from public.subjects where name = 'Chemistry'), null, 9, 4, 'The Earth and its atmosphere', 'inside-the-earth', null, true),
  ('KS3', 9, null, null, (select id from public.subjects where name = 'Chemistry'), null, 10, 4, 'The Earth and its atmosphere', 'three-ways-to-make-a-rock', null, true),
  ('KS3', 9, null, null, (select id from public.subjects where name = 'Chemistry'), null, 11, 5, 'The Earth and its atmosphere', 'the-rock-cycle', null, true),
  ('KS3', 9, null, null, (select id from public.subjects where name = 'Chemistry'), null, 12, 5, 'The Earth and its atmosphere', 'a-planet-with-limits', null, true),
  ('KS3', 9, null, null, (select id from public.subjects where name = 'Chemistry'), null, 13, 6, 'The Earth and its atmosphere', 'whats-in-the-air', null, true),
  ('KS3', 9, null, null, (select id from public.subjects where name = 'Chemistry'), null, 14, 6, 'The Earth and its atmosphere', 'carbon-dioxide-humans-and-climate', null, true);

-- ── Year 9 · Physics — 19 lessons ─────────────────────────
insert into public.scheme_of_work_entries
  (key_stage, year_group, tier, pathway, subject_id, exam_board, academic_week, half_term, topic, subtopic, notes, active)
values
  -- P2 Energy at home
  ('KS3', 9, null, null, (select id from public.subjects where name = 'Physics'), null, 1, 1, 'Energy at home', 'energy-in-food', null, true),
  ('KS3', 9, null, null, (select id from public.subjects where name = 'Physics'), null, 2, 1, 'Energy at home', 'power-ratings-in-watts', null, true),
  ('KS3', 9, null, null, (select id from public.subjects where name = 'Physics'), null, 3, 1, 'Energy at home', 'calculating-energy-transferred', null, true),
  ('KS3', 9, null, null, (select id from public.subjects where name = 'Physics'), null, 4, 1, 'Energy at home', 'reading-a-fuel-bill', null, true),
  ('KS3', 9, null, null, (select id from public.subjects where name = 'Physics'), null, 5, 2, 'Energy at home', 'fuels-and-energy-resources', null, true),
  -- P9 Static electricity
  ('KS3', 9, null, null, (select id from public.subjects where name = 'Physics'), null, 6, 2, 'Static electricity', 'charging-by-rubbing', null, true),
  ('KS3', 9, null, null, (select id from public.subjects where name = 'Physics'), null, 7, 2, 'Static electricity', 'forces-between-charges', null, true),
  ('KS3', 9, null, null, (select id from public.subjects where name = 'Physics'), null, 8, 3, 'Static electricity', 'electric-fields', null, true),
  -- P10 Magnetism and electromagnetism
  ('KS3', 9, null, null, (select id from public.subjects where name = 'Physics'), null, 9, 3, 'Magnetism and electromagnetism', 'magnets-and-poles', null, true),
  ('KS3', 9, null, null, (select id from public.subjects where name = 'Physics'), null, 10, 3, 'Magnetism and electromagnetism', 'magnetic-fields', null, true),
  ('KS3', 9, null, null, (select id from public.subjects where name = 'Physics'), null, 11, 4, 'Magnetism and electromagnetism', 'the-earth-is-a-magnet', null, true),
  ('KS3', 9, null, null, (select id from public.subjects where name = 'Physics'), null, 12, 4, 'Magnetism and electromagnetism', 'electromagnets', null, true),
  ('KS3', 9, null, null, (select id from public.subjects where name = 'Physics'), null, 13, 4, 'Magnetism and electromagnetism', 'how-a-motor-works', null, true),
  -- P12 Space
  ('KS3', 9, null, null, (select id from public.subjects where name = 'Physics'), null, 14, 5, 'Space', 'gravity-and-weight', null, true),
  ('KS3', 9, null, null, (select id from public.subjects where name = 'Physics'), null, 15, 5, 'Space', 'mass-vs-weight', null, true),
  ('KS3', 9, null, null, (select id from public.subjects where name = 'Physics'), null, 16, 5, 'Space', 'gravity-earth-moon-and-sun', null, true),
  ('KS3', 9, null, null, (select id from public.subjects where name = 'Physics'), null, 17, 6, 'Space', 'the-sun-stars-and-galaxies', null, true),
  ('KS3', 9, null, null, (select id from public.subjects where name = 'Physics'), null, 18, 6, 'Space', 'seasons-and-the-tilt', null, true),
  ('KS3', 9, null, null, (select id from public.subjects where name = 'Physics'), null, 19, 6, 'Space', 'how-far-is-a-light-year', null, true);

commit;
