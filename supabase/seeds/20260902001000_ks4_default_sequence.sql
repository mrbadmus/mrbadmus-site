-- ═══════════════════════════════════════════════════════════════════════
-- KS4 — AQA default sequence, as scheme-of-work rows.
--
-- ⚠️ GENERATED FILE — DO NOT EDIT BY HAND.
--    Regenerate with:  python3 ks4_seed_sow.py
--    Source of truth:  generate_site_v5.py (PATHWAY_TOPIC_MAP, SITE_DATA)
--                      all_subtopics_{biology,chemistry,physics}*.py
--    Written to:       supabase/seeds/20260902001000_ks4_default_sequence.sql
--    Target table:     public.scheme_of_work_entries (GLOBAL — no school_id)
--
-- Hand-editing this file makes it disagree with the site's own curriculum
-- data, and a scheme row that disagrees with the built pages is a teacher
-- pointing at a page that does not exist. Change the Python, re-run the
-- generator. Every href below was checked against mrbadmus_site/ at
-- generation time.
--
-- Idempotent: every KS4 row is deleted and rewritten, inside one
-- transaction. Re-running is safe and is the intended way to apply a change.
--
-- KS4 rows carry exam_board = 'AQA', a tier and a pathway on every row —
-- the same subtopic is taught in up to four blocks and the three columns
-- are what tells them apart. half_term is NULL throughout: the constraint
-- scheme_of_work_entries_half_term_is_ks3_only forbids it outside KS3.
--
-- ═══════════════════════════════════════════════════════════════════════
-- ⚠️ THIS SEED IS DELIBERATELY INCOMPLETE — 0 OF 865 ROWS ARE OMITTED.
-- ═══════════════════════════════════════════════════════════════════════
--
-- academic_week carries CHECK (academic_week BETWEEN 1 AND 52), and the
-- base unique key (key_stage, year_group, tier, pathway, subject_id,
-- exam_board, academic_week) allows one row per week. That caps a
-- (pathway, tier, subject) block at 104 rows across Years 10 and 11.
--
-- Five KS4 blocks are larger than that cap. Where a year's slice runs
-- past week 52 the remainder is dropped, and every dropped subtopic is
-- named in the OMITTED block at the foot of this file. Nothing vanishes
-- silently.
--
-- ➤ THE FIX IS A MIGRATION, NOT A GENERATOR CHANGE. Raise the KS4 ceiling
--   on academic_week to at least 48 — the largest year slice this
--   curriculum needs — and re-run `python3 ks4_seed_sow.py`. All 865 rows
--   are then emitted with no truncation whatsoever. Until that migration
--   lands, 0 subtopic pages have no scheme-of-work row.
--
-- Rows emitted per block, generated:
--
--   combined  foundation Biology    67
--   combined  foundation Chemistry  61
--   combined  foundation Physics    50
--   combined  higher     Biology    67
--   combined  higher     Chemistry  69
--   combined  higher     Physics    53
--   triple    foundation Biology    87
--   triple    foundation Chemistry  83
--   triple    foundation Physics    64
--   triple    higher     Biology    89
--   triple    higher     Chemistry  93
--   triple    higher     Physics    82
--
--   865 rows emitted, 0 omitted, 865 total pages in the curriculum.
--
-- ═══════════════════════════════════════════════════════════════════════

begin;

-- Preconditions. Failing here with a sentence beats failing later with a
-- NOT NULL violation on a subselect that quietly returned NULL.
do $$
begin
  if (select count(*) from public.subjects
       where name in ('Biology', 'Chemistry', 'Physics')) <> 3 then
    raise exception 'KS4 seed: public.subjects is missing one of Biology / '
                    'Chemistry / Physics. Seed the subjects table first.';
  end if;
end $$;

-- Idempotency: this file owns every KS4 row in the global table.
delete from public.scheme_of_work_entries where key_stage = 'KS4';

-- ── Combined · Foundation · Biology · Year 10 — 32 lessons ─────────────────────
insert into public.scheme_of_work_entries
  (key_stage, year_group, tier, pathway, subject_id, exam_board, academic_week, half_term, topic, subtopic, notes, active)
values
  -- cell-biology — Cell Biology
  ('KS4', 10, 'foundation', 'combined', (select id from public.subjects where name = 'Biology'), 'AQA', 1, null, 'Cell Biology', 'eukaryotes-prokaryotes', '/combined/foundation/biology/cell-biology/eukaryotes-prokaryotes.html', true),
  ('KS4', 10, 'foundation', 'combined', (select id from public.subjects where name = 'Biology'), 'AQA', 2, null, 'Cell Biology', 'animal-plant-cells', '/combined/foundation/biology/cell-biology/animal-plant-cells.html', true),
  ('KS4', 10, 'foundation', 'combined', (select id from public.subjects where name = 'Biology'), 'AQA', 3, null, 'Cell Biology', 'cell-specialisation', '/combined/foundation/biology/cell-biology/cell-specialisation.html', true),
  ('KS4', 10, 'foundation', 'combined', (select id from public.subjects where name = 'Biology'), 'AQA', 4, null, 'Cell Biology', 'microscopy', '/combined/foundation/biology/cell-biology/microscopy.html', true),
  ('KS4', 10, 'foundation', 'combined', (select id from public.subjects where name = 'Biology'), 'AQA', 5, null, 'Cell Biology', 'chromosomes-mitosis', '/combined/foundation/biology/cell-biology/chromosomes-mitosis.html', true),
  ('KS4', 10, 'foundation', 'combined', (select id from public.subjects where name = 'Biology'), 'AQA', 6, null, 'Cell Biology', 'stem-cells', '/combined/foundation/biology/cell-biology/stem-cells.html', true),
  ('KS4', 10, 'foundation', 'combined', (select id from public.subjects where name = 'Biology'), 'AQA', 7, null, 'Cell Biology', 'transport-in-cells', '/combined/foundation/biology/cell-biology/transport-in-cells.html', true),
  -- organisation — Organisation
  ('KS4', 10, 'foundation', 'combined', (select id from public.subjects where name = 'Biology'), 'AQA', 8, null, 'Organisation', 'principles-of-organisation', '/combined/foundation/biology/organisation/principles-of-organisation.html', true),
  ('KS4', 10, 'foundation', 'combined', (select id from public.subjects where name = 'Biology'), 'AQA', 9, null, 'Organisation', 'digestive-system', '/combined/foundation/biology/organisation/digestive-system.html', true),
  ('KS4', 10, 'foundation', 'combined', (select id from public.subjects where name = 'Biology'), 'AQA', 10, null, 'Organisation', 'enzymes', '/combined/foundation/biology/organisation/enzymes.html', true),
  ('KS4', 10, 'foundation', 'combined', (select id from public.subjects where name = 'Biology'), 'AQA', 11, null, 'Organisation', 'heart-blood-vessels', '/combined/foundation/biology/organisation/heart-blood-vessels.html', true),
  ('KS4', 10, 'foundation', 'combined', (select id from public.subjects where name = 'Biology'), 'AQA', 12, null, 'Organisation', 'blood', '/combined/foundation/biology/organisation/blood.html', true),
  ('KS4', 10, 'foundation', 'combined', (select id from public.subjects where name = 'Biology'), 'AQA', 13, null, 'Organisation', 'coronary-heart-disease', '/combined/foundation/biology/organisation/coronary-heart-disease.html', true),
  ('KS4', 10, 'foundation', 'combined', (select id from public.subjects where name = 'Biology'), 'AQA', 14, null, 'Organisation', 'health-disease', '/combined/foundation/biology/organisation/health-disease.html', true),
  ('KS4', 10, 'foundation', 'combined', (select id from public.subjects where name = 'Biology'), 'AQA', 15, null, 'Organisation', 'cancer', '/combined/foundation/biology/organisation/cancer.html', true),
  ('KS4', 10, 'foundation', 'combined', (select id from public.subjects where name = 'Biology'), 'AQA', 16, null, 'Organisation', 'plant-tissues', '/combined/foundation/biology/organisation/plant-tissues.html', true),
  ('KS4', 10, 'foundation', 'combined', (select id from public.subjects where name = 'Biology'), 'AQA', 17, null, 'Organisation', 'transpiration', '/combined/foundation/biology/organisation/transpiration.html', true),
  ('KS4', 10, 'foundation', 'combined', (select id from public.subjects where name = 'Biology'), 'AQA', 18, null, 'Organisation', 'translocation', '/combined/foundation/biology/organisation/translocation.html', true),
  -- infection-response — Infection and Response
  ('KS4', 10, 'foundation', 'combined', (select id from public.subjects where name = 'Biology'), 'AQA', 19, null, 'Infection and Response', 'communicable-diseases-defence', '/combined/foundation/biology/infection-response/communicable-diseases-defence.html', true),
  ('KS4', 10, 'foundation', 'combined', (select id from public.subjects where name = 'Biology'), 'AQA', 20, null, 'Infection and Response', 'viral-diseases', '/combined/foundation/biology/infection-response/viral-diseases.html', true),
  ('KS4', 10, 'foundation', 'combined', (select id from public.subjects where name = 'Biology'), 'AQA', 21, null, 'Infection and Response', 'bacterial-diseases', '/combined/foundation/biology/infection-response/bacterial-diseases.html', true),
  ('KS4', 10, 'foundation', 'combined', (select id from public.subjects where name = 'Biology'), 'AQA', 22, null, 'Infection and Response', 'fungal-protist-diseases', '/combined/foundation/biology/infection-response/fungal-protist-diseases.html', true),
  ('KS4', 10, 'foundation', 'combined', (select id from public.subjects where name = 'Biology'), 'AQA', 23, null, 'Infection and Response', 'vaccination', '/combined/foundation/biology/infection-response/vaccination.html', true),
  ('KS4', 10, 'foundation', 'combined', (select id from public.subjects where name = 'Biology'), 'AQA', 24, null, 'Infection and Response', 'antibiotics-painkillers', '/combined/foundation/biology/infection-response/antibiotics-painkillers.html', true),
  ('KS4', 10, 'foundation', 'combined', (select id from public.subjects where name = 'Biology'), 'AQA', 25, null, 'Infection and Response', 'drug-discovery-development', '/combined/foundation/biology/infection-response/drug-discovery-development.html', true),
  -- bioenergetics — Bioenergetics
  ('KS4', 10, 'foundation', 'combined', (select id from public.subjects where name = 'Biology'), 'AQA', 26, null, 'Bioenergetics', 'photosynthesis', '/combined/foundation/biology/bioenergetics/photosynthesis.html', true),
  ('KS4', 10, 'foundation', 'combined', (select id from public.subjects where name = 'Biology'), 'AQA', 27, null, 'Bioenergetics', 'rate-of-photosynthesis', '/combined/foundation/biology/bioenergetics/rate-of-photosynthesis.html', true),
  ('KS4', 10, 'foundation', 'combined', (select id from public.subjects where name = 'Biology'), 'AQA', 28, null, 'Bioenergetics', 'uses-of-glucose', '/combined/foundation/biology/bioenergetics/uses-of-glucose.html', true),
  ('KS4', 10, 'foundation', 'combined', (select id from public.subjects where name = 'Biology'), 'AQA', 29, null, 'Bioenergetics', 'aerobic-respiration', '/combined/foundation/biology/bioenergetics/aerobic-respiration.html', true),
  ('KS4', 10, 'foundation', 'combined', (select id from public.subjects where name = 'Biology'), 'AQA', 30, null, 'Bioenergetics', 'anaerobic-respiration', '/combined/foundation/biology/bioenergetics/anaerobic-respiration.html', true),
  ('KS4', 10, 'foundation', 'combined', (select id from public.subjects where name = 'Biology'), 'AQA', 31, null, 'Bioenergetics', 'response-to-exercise', '/combined/foundation/biology/bioenergetics/response-to-exercise.html', true),
  ('KS4', 10, 'foundation', 'combined', (select id from public.subjects where name = 'Biology'), 'AQA', 32, null, 'Bioenergetics', 'metabolism', '/combined/foundation/biology/bioenergetics/metabolism.html', true);

-- ── Combined · Foundation · Biology · Year 11 — 35 lessons ─────────────────────
insert into public.scheme_of_work_entries
  (key_stage, year_group, tier, pathway, subject_id, exam_board, academic_week, half_term, topic, subtopic, notes, active)
values
  -- homeostasis — Homeostasis and Response
  ('KS4', 11, 'foundation', 'combined', (select id from public.subjects where name = 'Biology'), 'AQA', 1, null, 'Homeostasis and Response', 'homeostasis', '/combined/foundation/biology/homeostasis/homeostasis.html', true),
  ('KS4', 11, 'foundation', 'combined', (select id from public.subjects where name = 'Biology'), 'AQA', 2, null, 'Homeostasis and Response', 'nervous-system', '/combined/foundation/biology/homeostasis/nervous-system.html', true),
  ('KS4', 11, 'foundation', 'combined', (select id from public.subjects where name = 'Biology'), 'AQA', 3, null, 'Homeostasis and Response', 'reflex-actions', '/combined/foundation/biology/homeostasis/reflex-actions.html', true),
  ('KS4', 11, 'foundation', 'combined', (select id from public.subjects where name = 'Biology'), 'AQA', 4, null, 'Homeostasis and Response', 'endocrine-system', '/combined/foundation/biology/homeostasis/endocrine-system.html', true),
  ('KS4', 11, 'foundation', 'combined', (select id from public.subjects where name = 'Biology'), 'AQA', 5, null, 'Homeostasis and Response', 'blood-glucose-diabetes', '/combined/foundation/biology/homeostasis/blood-glucose-diabetes.html', true),
  ('KS4', 11, 'foundation', 'combined', (select id from public.subjects where name = 'Biology'), 'AQA', 6, null, 'Homeostasis and Response', 'human-reproduction-hormones', '/combined/foundation/biology/homeostasis/human-reproduction-hormones.html', true),
  ('KS4', 11, 'foundation', 'combined', (select id from public.subjects where name = 'Biology'), 'AQA', 7, null, 'Homeostasis and Response', 'contraception-fertility', '/combined/foundation/biology/homeostasis/contraception-fertility.html', true),
  ('KS4', 11, 'foundation', 'combined', (select id from public.subjects where name = 'Biology'), 'AQA', 8, null, 'Homeostasis and Response', 'reaction-time', '/combined/foundation/biology/homeostasis/reaction-time.html', true),
  -- inheritance — Inheritance, Variation and Evolution
  ('KS4', 11, 'foundation', 'combined', (select id from public.subjects where name = 'Biology'), 'AQA', 9, null, 'Inheritance, Variation and Evolution', 'sexual-asexual-reproduction', '/combined/foundation/biology/inheritance/sexual-asexual-reproduction.html', true),
  ('KS4', 11, 'foundation', 'combined', (select id from public.subjects where name = 'Biology'), 'AQA', 10, null, 'Inheritance, Variation and Evolution', 'dna-genome', '/combined/foundation/biology/inheritance/dna-genome.html', true),
  ('KS4', 11, 'foundation', 'combined', (select id from public.subjects where name = 'Biology'), 'AQA', 11, null, 'Inheritance, Variation and Evolution', 'genetic-inheritance', '/combined/foundation/biology/inheritance/genetic-inheritance.html', true),
  ('KS4', 11, 'foundation', 'combined', (select id from public.subjects where name = 'Biology'), 'AQA', 12, null, 'Inheritance, Variation and Evolution', 'inherited-disorders', '/combined/foundation/biology/inheritance/inherited-disorders.html', true),
  ('KS4', 11, 'foundation', 'combined', (select id from public.subjects where name = 'Biology'), 'AQA', 13, null, 'Inheritance, Variation and Evolution', 'sex-determination', '/combined/foundation/biology/inheritance/sex-determination.html', true),
  ('KS4', 11, 'foundation', 'combined', (select id from public.subjects where name = 'Biology'), 'AQA', 14, null, 'Inheritance, Variation and Evolution', 'variation', '/combined/foundation/biology/inheritance/variation.html', true),
  ('KS4', 11, 'foundation', 'combined', (select id from public.subjects where name = 'Biology'), 'AQA', 15, null, 'Inheritance, Variation and Evolution', 'evolution-natural-selection', '/combined/foundation/biology/inheritance/evolution-natural-selection.html', true),
  ('KS4', 11, 'foundation', 'combined', (select id from public.subjects where name = 'Biology'), 'AQA', 16, null, 'Inheritance, Variation and Evolution', 'selective-breeding', '/combined/foundation/biology/inheritance/selective-breeding.html', true),
  ('KS4', 11, 'foundation', 'combined', (select id from public.subjects where name = 'Biology'), 'AQA', 17, null, 'Inheritance, Variation and Evolution', 'genetic-engineering', '/combined/foundation/biology/inheritance/genetic-engineering.html', true),
  ('KS4', 11, 'foundation', 'combined', (select id from public.subjects where name = 'Biology'), 'AQA', 18, null, 'Inheritance, Variation and Evolution', 'evidence-for-evolution', '/combined/foundation/biology/inheritance/evidence-for-evolution.html', true),
  ('KS4', 11, 'foundation', 'combined', (select id from public.subjects where name = 'Biology'), 'AQA', 19, null, 'Inheritance, Variation and Evolution', 'fossils-extinction', '/combined/foundation/biology/inheritance/fossils-extinction.html', true),
  ('KS4', 11, 'foundation', 'combined', (select id from public.subjects where name = 'Biology'), 'AQA', 20, null, 'Inheritance, Variation and Evolution', 'resistant-bacteria', '/combined/foundation/biology/inheritance/resistant-bacteria.html', true),
  -- ecology — Ecology
  ('KS4', 11, 'foundation', 'combined', (select id from public.subjects where name = 'Biology'), 'AQA', 21, null, 'Ecology', 'ecosystems', '/combined/foundation/biology/ecology/ecosystems.html', true),
  ('KS4', 11, 'foundation', 'combined', (select id from public.subjects where name = 'Biology'), 'AQA', 22, null, 'Ecology', 'abiotic-biotic-factors', '/combined/foundation/biology/ecology/abiotic-biotic-factors.html', true),
  ('KS4', 11, 'foundation', 'combined', (select id from public.subjects where name = 'Biology'), 'AQA', 23, null, 'Ecology', 'adaptations', '/combined/foundation/biology/ecology/adaptations.html', true),
  ('KS4', 11, 'foundation', 'combined', (select id from public.subjects where name = 'Biology'), 'AQA', 24, null, 'Ecology', 'food-chains-webs', '/combined/foundation/biology/ecology/food-chains-webs.html', true),
  ('KS4', 11, 'foundation', 'combined', (select id from public.subjects where name = 'Biology'), 'AQA', 25, null, 'Ecology', 'population-competition', '/combined/foundation/biology/ecology/population-competition.html', true),
  ('KS4', 11, 'foundation', 'combined', (select id from public.subjects where name = 'Biology'), 'AQA', 26, null, 'Ecology', 'biodiversity', '/combined/foundation/biology/ecology/biodiversity.html', true),
  ('KS4', 11, 'foundation', 'combined', (select id from public.subjects where name = 'Biology'), 'AQA', 27, null, 'Ecology', 'waste-management', '/combined/foundation/biology/ecology/waste-management.html', true),
  ('KS4', 11, 'foundation', 'combined', (select id from public.subjects where name = 'Biology'), 'AQA', 28, null, 'Ecology', 'land-use', '/combined/foundation/biology/ecology/land-use.html', true),
  ('KS4', 11, 'foundation', 'combined', (select id from public.subjects where name = 'Biology'), 'AQA', 29, null, 'Ecology', 'deforestation', '/combined/foundation/biology/ecology/deforestation.html', true),
  ('KS4', 11, 'foundation', 'combined', (select id from public.subjects where name = 'Biology'), 'AQA', 30, null, 'Ecology', 'global-warming', '/combined/foundation/biology/ecology/global-warming.html', true),
  ('KS4', 11, 'foundation', 'combined', (select id from public.subjects where name = 'Biology'), 'AQA', 31, null, 'Ecology', 'maintaining-biodiversity', '/combined/foundation/biology/ecology/maintaining-biodiversity.html', true),
  ('KS4', 11, 'foundation', 'combined', (select id from public.subjects where name = 'Biology'), 'AQA', 32, null, 'Ecology', 'carbon-cycle', '/combined/foundation/biology/ecology/carbon-cycle.html', true),
  ('KS4', 11, 'foundation', 'combined', (select id from public.subjects where name = 'Biology'), 'AQA', 33, null, 'Ecology', 'water-cycle', '/combined/foundation/biology/ecology/water-cycle.html', true),
  ('KS4', 11, 'foundation', 'combined', (select id from public.subjects where name = 'Biology'), 'AQA', 34, null, 'Ecology', 'decomposition', '/combined/foundation/biology/ecology/decomposition.html', true),
  ('KS4', 11, 'foundation', 'combined', (select id from public.subjects where name = 'Biology'), 'AQA', 35, null, 'Ecology', 'sampling-techniques', '/combined/foundation/biology/ecology/sampling-techniques.html', true);

-- ── Combined · Foundation · Chemistry · Year 10 — 28 lessons ─────────────────────
insert into public.scheme_of_work_entries
  (key_stage, year_group, tier, pathway, subject_id, exam_board, academic_week, half_term, topic, subtopic, notes, active)
values
  -- atomic-structure — Atomic Structure and the Periodic Table
  ('KS4', 10, 'foundation', 'combined', (select id from public.subjects where name = 'Chemistry'), 'AQA', 1, null, 'Atomic Structure and the Periodic Table', 'atoms-elements-compounds', '/combined/foundation/chemistry/atomic-structure/atoms-elements-compounds.html', true),
  ('KS4', 10, 'foundation', 'combined', (select id from public.subjects where name = 'Chemistry'), 'AQA', 2, null, 'Atomic Structure and the Periodic Table', 'mixtures', '/combined/foundation/chemistry/atomic-structure/mixtures.html', true),
  ('KS4', 10, 'foundation', 'combined', (select id from public.subjects where name = 'Chemistry'), 'AQA', 3, null, 'Atomic Structure and the Periodic Table', 'model-of-the-atom', '/combined/foundation/chemistry/atomic-structure/model-of-the-atom.html', true),
  ('KS4', 10, 'foundation', 'combined', (select id from public.subjects where name = 'Chemistry'), 'AQA', 4, null, 'Atomic Structure and the Periodic Table', 'subatomic-particles', '/combined/foundation/chemistry/atomic-structure/subatomic-particles.html', true),
  ('KS4', 10, 'foundation', 'combined', (select id from public.subjects where name = 'Chemistry'), 'AQA', 5, null, 'Atomic Structure and the Periodic Table', 'relative-atomic-mass', '/combined/foundation/chemistry/atomic-structure/relative-atomic-mass.html', true),
  ('KS4', 10, 'foundation', 'combined', (select id from public.subjects where name = 'Chemistry'), 'AQA', 6, null, 'Atomic Structure and the Periodic Table', 'electronic-structure', '/combined/foundation/chemistry/atomic-structure/electronic-structure.html', true),
  ('KS4', 10, 'foundation', 'combined', (select id from public.subjects where name = 'Chemistry'), 'AQA', 7, null, 'Atomic Structure and the Periodic Table', 'periodic-table', '/combined/foundation/chemistry/atomic-structure/periodic-table.html', true),
  ('KS4', 10, 'foundation', 'combined', (select id from public.subjects where name = 'Chemistry'), 'AQA', 8, null, 'Atomic Structure and the Periodic Table', 'development-periodic-table', '/combined/foundation/chemistry/atomic-structure/development-periodic-table.html', true),
  ('KS4', 10, 'foundation', 'combined', (select id from public.subjects where name = 'Chemistry'), 'AQA', 9, null, 'Atomic Structure and the Periodic Table', 'metals-non-metals', '/combined/foundation/chemistry/atomic-structure/metals-non-metals.html', true),
  ('KS4', 10, 'foundation', 'combined', (select id from public.subjects where name = 'Chemistry'), 'AQA', 10, null, 'Atomic Structure and the Periodic Table', 'group-0', '/combined/foundation/chemistry/atomic-structure/group-0.html', true),
  ('KS4', 10, 'foundation', 'combined', (select id from public.subjects where name = 'Chemistry'), 'AQA', 11, null, 'Atomic Structure and the Periodic Table', 'group-1', '/combined/foundation/chemistry/atomic-structure/group-1.html', true),
  ('KS4', 10, 'foundation', 'combined', (select id from public.subjects where name = 'Chemistry'), 'AQA', 12, null, 'Atomic Structure and the Periodic Table', 'group-7', '/combined/foundation/chemistry/atomic-structure/group-7.html', true),
  -- bonding — Bonding, Structure and Properties of Matter
  ('KS4', 10, 'foundation', 'combined', (select id from public.subjects where name = 'Chemistry'), 'AQA', 13, null, 'Bonding, Structure and Properties of Matter', 'chemical-bonds', '/combined/foundation/chemistry/bonding/chemical-bonds.html', true),
  ('KS4', 10, 'foundation', 'combined', (select id from public.subjects where name = 'Chemistry'), 'AQA', 14, null, 'Bonding, Structure and Properties of Matter', 'ionic-bonding', '/combined/foundation/chemistry/bonding/ionic-bonding.html', true),
  ('KS4', 10, 'foundation', 'combined', (select id from public.subjects where name = 'Chemistry'), 'AQA', 15, null, 'Bonding, Structure and Properties of Matter', 'ionic-compounds', '/combined/foundation/chemistry/bonding/ionic-compounds.html', true),
  ('KS4', 10, 'foundation', 'combined', (select id from public.subjects where name = 'Chemistry'), 'AQA', 16, null, 'Bonding, Structure and Properties of Matter', 'covalent-bonding', '/combined/foundation/chemistry/bonding/covalent-bonding.html', true),
  ('KS4', 10, 'foundation', 'combined', (select id from public.subjects where name = 'Chemistry'), 'AQA', 17, null, 'Bonding, Structure and Properties of Matter', 'metallic-bonding', '/combined/foundation/chemistry/bonding/metallic-bonding.html', true),
  ('KS4', 10, 'foundation', 'combined', (select id from public.subjects where name = 'Chemistry'), 'AQA', 18, null, 'Bonding, Structure and Properties of Matter', 'states-of-matter', '/combined/foundation/chemistry/bonding/states-of-matter.html', true),
  ('KS4', 10, 'foundation', 'combined', (select id from public.subjects where name = 'Chemistry'), 'AQA', 19, null, 'Bonding, Structure and Properties of Matter', 'properties-ionic-compounds', '/combined/foundation/chemistry/bonding/properties-ionic-compounds.html', true),
  ('KS4', 10, 'foundation', 'combined', (select id from public.subjects where name = 'Chemistry'), 'AQA', 20, null, 'Bonding, Structure and Properties of Matter', 'properties-small-molecules', '/combined/foundation/chemistry/bonding/properties-small-molecules.html', true),
  ('KS4', 10, 'foundation', 'combined', (select id from public.subjects where name = 'Chemistry'), 'AQA', 21, null, 'Bonding, Structure and Properties of Matter', 'polymers', '/combined/foundation/chemistry/bonding/polymers.html', true),
  ('KS4', 10, 'foundation', 'combined', (select id from public.subjects where name = 'Chemistry'), 'AQA', 22, null, 'Bonding, Structure and Properties of Matter', 'giant-covalent-structures', '/combined/foundation/chemistry/bonding/giant-covalent-structures.html', true),
  ('KS4', 10, 'foundation', 'combined', (select id from public.subjects where name = 'Chemistry'), 'AQA', 23, null, 'Bonding, Structure and Properties of Matter', 'metals-alloys', '/combined/foundation/chemistry/bonding/metals-alloys.html', true),
  -- quantitative — Quantitative Chemistry
  ('KS4', 10, 'foundation', 'combined', (select id from public.subjects where name = 'Chemistry'), 'AQA', 24, null, 'Quantitative Chemistry', 'conservation-of-mass', '/combined/foundation/chemistry/quantitative/conservation-of-mass.html', true),
  ('KS4', 10, 'foundation', 'combined', (select id from public.subjects where name = 'Chemistry'), 'AQA', 25, null, 'Quantitative Chemistry', 'relative-formula-mass', '/combined/foundation/chemistry/quantitative/relative-formula-mass.html', true),
  ('KS4', 10, 'foundation', 'combined', (select id from public.subjects where name = 'Chemistry'), 'AQA', 26, null, 'Quantitative Chemistry', 'mass-changes-reactions', '/combined/foundation/chemistry/quantitative/mass-changes-reactions.html', true),
  ('KS4', 10, 'foundation', 'combined', (select id from public.subjects where name = 'Chemistry'), 'AQA', 27, null, 'Quantitative Chemistry', 'chemical-measurements', '/combined/foundation/chemistry/quantitative/chemical-measurements.html', true),
  ('KS4', 10, 'foundation', 'combined', (select id from public.subjects where name = 'Chemistry'), 'AQA', 28, null, 'Quantitative Chemistry', 'concentration-of-solutions', '/combined/foundation/chemistry/quantitative/concentration-of-solutions.html', true);

-- ── Combined · Foundation · Chemistry · Year 11 — 33 lessons ─────────────────────
insert into public.scheme_of_work_entries
  (key_stage, year_group, tier, pathway, subject_id, exam_board, academic_week, half_term, topic, subtopic, notes, active)
values
  -- chemical-changes — Chemical Changes
  ('KS4', 11, 'foundation', 'combined', (select id from public.subjects where name = 'Chemistry'), 'AQA', 1, null, 'Chemical Changes', 'reactivity-series', '/combined/foundation/chemistry/chemical-changes/reactivity-series.html', true),
  ('KS4', 11, 'foundation', 'combined', (select id from public.subjects where name = 'Chemistry'), 'AQA', 2, null, 'Chemical Changes', 'extraction-of-metals', '/combined/foundation/chemistry/chemical-changes/extraction-of-metals.html', true),
  ('KS4', 11, 'foundation', 'combined', (select id from public.subjects where name = 'Chemistry'), 'AQA', 3, null, 'Chemical Changes', 'oxidation-reduction', '/combined/foundation/chemistry/chemical-changes/oxidation-reduction.html', true),
  ('KS4', 11, 'foundation', 'combined', (select id from public.subjects where name = 'Chemistry'), 'AQA', 4, null, 'Chemical Changes', 'reactions-of-acids', '/combined/foundation/chemistry/chemical-changes/reactions-of-acids.html', true),
  ('KS4', 11, 'foundation', 'combined', (select id from public.subjects where name = 'Chemistry'), 'AQA', 5, null, 'Chemical Changes', 'salts-neutralisation', '/combined/foundation/chemistry/chemical-changes/salts-neutralisation.html', true),
  ('KS4', 11, 'foundation', 'combined', (select id from public.subjects where name = 'Chemistry'), 'AQA', 6, null, 'Chemical Changes', 'ph-scale', '/combined/foundation/chemistry/chemical-changes/ph-scale.html', true),
  ('KS4', 11, 'foundation', 'combined', (select id from public.subjects where name = 'Chemistry'), 'AQA', 7, null, 'Chemical Changes', 'electrolysis-principles', '/combined/foundation/chemistry/chemical-changes/electrolysis-principles.html', true),
  ('KS4', 11, 'foundation', 'combined', (select id from public.subjects where name = 'Chemistry'), 'AQA', 8, null, 'Chemical Changes', 'electrolysis-molten', '/combined/foundation/chemistry/chemical-changes/electrolysis-molten.html', true),
  ('KS4', 11, 'foundation', 'combined', (select id from public.subjects where name = 'Chemistry'), 'AQA', 9, null, 'Chemical Changes', 'electrolysis-extraction', '/combined/foundation/chemistry/chemical-changes/electrolysis-extraction.html', true),
  ('KS4', 11, 'foundation', 'combined', (select id from public.subjects where name = 'Chemistry'), 'AQA', 10, null, 'Chemical Changes', 'electrolysis-aqueous', '/combined/foundation/chemistry/chemical-changes/electrolysis-aqueous.html', true),
  -- energy-changes — Energy Changes
  ('KS4', 11, 'foundation', 'combined', (select id from public.subjects where name = 'Chemistry'), 'AQA', 11, null, 'Energy Changes', 'exothermic-endothermic', '/combined/foundation/chemistry/energy-changes/exothermic-endothermic.html', true),
  ('KS4', 11, 'foundation', 'combined', (select id from public.subjects where name = 'Chemistry'), 'AQA', 12, null, 'Energy Changes', 'reaction-profiles', '/combined/foundation/chemistry/energy-changes/reaction-profiles.html', true),
  -- rates-equilibrium — Rate and Extent of Chemical Change
  ('KS4', 11, 'foundation', 'combined', (select id from public.subjects where name = 'Chemistry'), 'AQA', 13, null, 'Rate and Extent of Chemical Change', 'calculating-rates', '/combined/foundation/chemistry/rates-equilibrium/calculating-rates.html', true),
  ('KS4', 11, 'foundation', 'combined', (select id from public.subjects where name = 'Chemistry'), 'AQA', 14, null, 'Rate and Extent of Chemical Change', 'factors-affecting-rate', '/combined/foundation/chemistry/rates-equilibrium/factors-affecting-rate.html', true),
  ('KS4', 11, 'foundation', 'combined', (select id from public.subjects where name = 'Chemistry'), 'AQA', 15, null, 'Rate and Extent of Chemical Change', 'collision-theory', '/combined/foundation/chemistry/rates-equilibrium/collision-theory.html', true),
  ('KS4', 11, 'foundation', 'combined', (select id from public.subjects where name = 'Chemistry'), 'AQA', 16, null, 'Rate and Extent of Chemical Change', 'catalysts', '/combined/foundation/chemistry/rates-equilibrium/catalysts.html', true),
  ('KS4', 11, 'foundation', 'combined', (select id from public.subjects where name = 'Chemistry'), 'AQA', 17, null, 'Rate and Extent of Chemical Change', 'reversible-reactions-equilibrium', '/combined/foundation/chemistry/rates-equilibrium/reversible-reactions-equilibrium.html', true),
  -- organic — Organic Chemistry
  ('KS4', 11, 'foundation', 'combined', (select id from public.subjects where name = 'Chemistry'), 'AQA', 18, null, 'Organic Chemistry', 'crude-oil-hydrocarbons', '/combined/foundation/chemistry/organic/crude-oil-hydrocarbons.html', true),
  ('KS4', 11, 'foundation', 'combined', (select id from public.subjects where name = 'Chemistry'), 'AQA', 19, null, 'Organic Chemistry', 'fractional-distillation', '/combined/foundation/chemistry/organic/fractional-distillation.html', true),
  ('KS4', 11, 'foundation', 'combined', (select id from public.subjects where name = 'Chemistry'), 'AQA', 20, null, 'Organic Chemistry', 'properties-of-hydrocarbons', '/combined/foundation/chemistry/organic/properties-of-hydrocarbons.html', true),
  ('KS4', 11, 'foundation', 'combined', (select id from public.subjects where name = 'Chemistry'), 'AQA', 21, null, 'Organic Chemistry', 'cracking-alkenes', '/combined/foundation/chemistry/organic/cracking-alkenes.html', true),
  -- analysis — Chemical Analysis
  ('KS4', 11, 'foundation', 'combined', (select id from public.subjects where name = 'Chemistry'), 'AQA', 22, null, 'Chemical Analysis', 'pure-substances', '/combined/foundation/chemistry/analysis/pure-substances.html', true),
  ('KS4', 11, 'foundation', 'combined', (select id from public.subjects where name = 'Chemistry'), 'AQA', 23, null, 'Chemical Analysis', 'formulations', '/combined/foundation/chemistry/analysis/formulations.html', true),
  ('KS4', 11, 'foundation', 'combined', (select id from public.subjects where name = 'Chemistry'), 'AQA', 24, null, 'Chemical Analysis', 'chromatography', '/combined/foundation/chemistry/analysis/chromatography.html', true),
  ('KS4', 11, 'foundation', 'combined', (select id from public.subjects where name = 'Chemistry'), 'AQA', 25, null, 'Chemical Analysis', 'testing-for-gases', '/combined/foundation/chemistry/analysis/testing-for-gases.html', true),
  -- atmosphere — Chemistry of the Atmosphere
  ('KS4', 11, 'foundation', 'combined', (select id from public.subjects where name = 'Chemistry'), 'AQA', 26, null, 'Chemistry of the Atmosphere', 'composition-of-atmosphere', '/combined/foundation/chemistry/atmosphere/composition-of-atmosphere.html', true),
  ('KS4', 11, 'foundation', 'combined', (select id from public.subjects where name = 'Chemistry'), 'AQA', 27, null, 'Chemistry of the Atmosphere', 'early-atmosphere', '/combined/foundation/chemistry/atmosphere/early-atmosphere.html', true),
  ('KS4', 11, 'foundation', 'combined', (select id from public.subjects where name = 'Chemistry'), 'AQA', 28, null, 'Chemistry of the Atmosphere', 'greenhouse-gases', '/combined/foundation/chemistry/atmosphere/greenhouse-gases.html', true),
  ('KS4', 11, 'foundation', 'combined', (select id from public.subjects where name = 'Chemistry'), 'AQA', 29, null, 'Chemistry of the Atmosphere', 'atmospheric-pollutants', '/combined/foundation/chemistry/atmosphere/atmospheric-pollutants.html', true),
  -- resources — Using Resources
  ('KS4', 11, 'foundation', 'combined', (select id from public.subjects where name = 'Chemistry'), 'AQA', 30, null, 'Using Resources', 'earths-resources', '/combined/foundation/chemistry/resources/earths-resources.html', true),
  ('KS4', 11, 'foundation', 'combined', (select id from public.subjects where name = 'Chemistry'), 'AQA', 31, null, 'Using Resources', 'potable-water', '/combined/foundation/chemistry/resources/potable-water.html', true),
  ('KS4', 11, 'foundation', 'combined', (select id from public.subjects where name = 'Chemistry'), 'AQA', 32, null, 'Using Resources', 'life-cycle-assessment', '/combined/foundation/chemistry/resources/life-cycle-assessment.html', true),
  ('KS4', 11, 'foundation', 'combined', (select id from public.subjects where name = 'Chemistry'), 'AQA', 33, null, 'Using Resources', 'reducing-use-of-resources', '/combined/foundation/chemistry/resources/reducing-use-of-resources.html', true);

-- ── Combined · Foundation · Physics · Year 10 — 23 lessons ─────────────────────
insert into public.scheme_of_work_entries
  (key_stage, year_group, tier, pathway, subject_id, exam_board, academic_week, half_term, topic, subtopic, notes, active)
values
  -- energy — Energy
  ('KS4', 10, 'foundation', 'combined', (select id from public.subjects where name = 'Physics'), 'AQA', 1, null, 'Energy', 'energy-stores-systems', '/combined/foundation/physics/energy/energy-stores-systems.html', true),
  ('KS4', 10, 'foundation', 'combined', (select id from public.subjects where name = 'Physics'), 'AQA', 2, null, 'Energy', 'changes-in-energy', '/combined/foundation/physics/energy/changes-in-energy.html', true),
  ('KS4', 10, 'foundation', 'combined', (select id from public.subjects where name = 'Physics'), 'AQA', 3, null, 'Energy', 'energy-changes-in-systems', '/combined/foundation/physics/energy/energy-changes-in-systems.html', true),
  ('KS4', 10, 'foundation', 'combined', (select id from public.subjects where name = 'Physics'), 'AQA', 4, null, 'Energy', 'power', '/combined/foundation/physics/energy/power.html', true),
  ('KS4', 10, 'foundation', 'combined', (select id from public.subjects where name = 'Physics'), 'AQA', 5, null, 'Energy', 'energy-transfers-in-a-system', '/combined/foundation/physics/energy/energy-transfers-in-a-system.html', true),
  ('KS4', 10, 'foundation', 'combined', (select id from public.subjects where name = 'Physics'), 'AQA', 6, null, 'Energy', 'efficiency', '/combined/foundation/physics/energy/efficiency.html', true),
  ('KS4', 10, 'foundation', 'combined', (select id from public.subjects where name = 'Physics'), 'AQA', 7, null, 'Energy', 'energy-resources', '/combined/foundation/physics/energy/energy-resources.html', true),
  -- electricity — Electricity
  ('KS4', 10, 'foundation', 'combined', (select id from public.subjects where name = 'Physics'), 'AQA', 8, null, 'Electricity', 'circuit-symbols', '/combined/foundation/physics/electricity/circuit-symbols.html', true),
  ('KS4', 10, 'foundation', 'combined', (select id from public.subjects where name = 'Physics'), 'AQA', 9, null, 'Electricity', 'electrical-charge-current', '/combined/foundation/physics/electricity/electrical-charge-current.html', true),
  ('KS4', 10, 'foundation', 'combined', (select id from public.subjects where name = 'Physics'), 'AQA', 10, null, 'Electricity', 'current-resistance-pd', '/combined/foundation/physics/electricity/current-resistance-pd.html', true),
  ('KS4', 10, 'foundation', 'combined', (select id from public.subjects where name = 'Physics'), 'AQA', 11, null, 'Electricity', 'resistors', '/combined/foundation/physics/electricity/resistors.html', true),
  ('KS4', 10, 'foundation', 'combined', (select id from public.subjects where name = 'Physics'), 'AQA', 12, null, 'Electricity', 'series-parallel-circuits', '/combined/foundation/physics/electricity/series-parallel-circuits.html', true),
  ('KS4', 10, 'foundation', 'combined', (select id from public.subjects where name = 'Physics'), 'AQA', 13, null, 'Electricity', 'direct-alternating-pd', '/combined/foundation/physics/electricity/direct-alternating-pd.html', true),
  ('KS4', 10, 'foundation', 'combined', (select id from public.subjects where name = 'Physics'), 'AQA', 14, null, 'Electricity', 'mains-electricity', '/combined/foundation/physics/electricity/mains-electricity.html', true),
  ('KS4', 10, 'foundation', 'combined', (select id from public.subjects where name = 'Physics'), 'AQA', 15, null, 'Electricity', 'power-electricity', '/combined/foundation/physics/electricity/power-electricity.html', true),
  ('KS4', 10, 'foundation', 'combined', (select id from public.subjects where name = 'Physics'), 'AQA', 16, null, 'Electricity', 'energy-transfers-appliances', '/combined/foundation/physics/electricity/energy-transfers-appliances.html', true),
  ('KS4', 10, 'foundation', 'combined', (select id from public.subjects where name = 'Physics'), 'AQA', 17, null, 'Electricity', 'national-grid', '/combined/foundation/physics/electricity/national-grid.html', true),
  -- particle-model — Particle Model of Matter
  ('KS4', 10, 'foundation', 'combined', (select id from public.subjects where name = 'Physics'), 'AQA', 18, null, 'Particle Model of Matter', 'density-of-materials', '/combined/foundation/physics/particle-model/density-of-materials.html', true),
  ('KS4', 10, 'foundation', 'combined', (select id from public.subjects where name = 'Physics'), 'AQA', 19, null, 'Particle Model of Matter', 'changes-of-state', '/combined/foundation/physics/particle-model/changes-of-state.html', true),
  ('KS4', 10, 'foundation', 'combined', (select id from public.subjects where name = 'Physics'), 'AQA', 20, null, 'Particle Model of Matter', 'internal-energy', '/combined/foundation/physics/particle-model/internal-energy.html', true),
  ('KS4', 10, 'foundation', 'combined', (select id from public.subjects where name = 'Physics'), 'AQA', 21, null, 'Particle Model of Matter', 'temperature-changes-shc', '/combined/foundation/physics/particle-model/temperature-changes-shc.html', true),
  ('KS4', 10, 'foundation', 'combined', (select id from public.subjects where name = 'Physics'), 'AQA', 22, null, 'Particle Model of Matter', 'specific-latent-heat', '/combined/foundation/physics/particle-model/specific-latent-heat.html', true),
  ('KS4', 10, 'foundation', 'combined', (select id from public.subjects where name = 'Physics'), 'AQA', 23, null, 'Particle Model of Matter', 'particle-motion-pressure', '/combined/foundation/physics/particle-model/particle-motion-pressure.html', true);

-- ── Combined · Foundation · Physics · Year 11 — 27 lessons ─────────────────────
insert into public.scheme_of_work_entries
  (key_stage, year_group, tier, pathway, subject_id, exam_board, academic_week, half_term, topic, subtopic, notes, active)
values
  -- atomic-structure — Atomic Structure
  ('KS4', 11, 'foundation', 'combined', (select id from public.subjects where name = 'Physics'), 'AQA', 1, null, 'Atomic Structure', 'structure-of-atom', '/combined/foundation/physics/atomic-structure/structure-of-atom.html', true),
  ('KS4', 11, 'foundation', 'combined', (select id from public.subjects where name = 'Physics'), 'AQA', 2, null, 'Atomic Structure', 'mass-number-isotopes', '/combined/foundation/physics/atomic-structure/mass-number-isotopes.html', true),
  ('KS4', 11, 'foundation', 'combined', (select id from public.subjects where name = 'Physics'), 'AQA', 3, null, 'Atomic Structure', 'development-atomic-model', '/combined/foundation/physics/atomic-structure/development-atomic-model.html', true),
  ('KS4', 11, 'foundation', 'combined', (select id from public.subjects where name = 'Physics'), 'AQA', 4, null, 'Atomic Structure', 'radioactive-decay', '/combined/foundation/physics/atomic-structure/radioactive-decay.html', true),
  ('KS4', 11, 'foundation', 'combined', (select id from public.subjects where name = 'Physics'), 'AQA', 5, null, 'Atomic Structure', 'nuclear-equations', '/combined/foundation/physics/atomic-structure/nuclear-equations.html', true),
  ('KS4', 11, 'foundation', 'combined', (select id from public.subjects where name = 'Physics'), 'AQA', 6, null, 'Atomic Structure', 'half-lives', '/combined/foundation/physics/atomic-structure/half-lives.html', true),
  ('KS4', 11, 'foundation', 'combined', (select id from public.subjects where name = 'Physics'), 'AQA', 7, null, 'Atomic Structure', 'radioactive-contamination', '/combined/foundation/physics/atomic-structure/radioactive-contamination.html', true),
  -- forces — Forces
  ('KS4', 11, 'foundation', 'combined', (select id from public.subjects where name = 'Physics'), 'AQA', 8, null, 'Forces', 'scalar-vector-quantities', '/combined/foundation/physics/forces/scalar-vector-quantities.html', true),
  ('KS4', 11, 'foundation', 'combined', (select id from public.subjects where name = 'Physics'), 'AQA', 9, null, 'Forces', 'contact-noncontact-forces', '/combined/foundation/physics/forces/contact-noncontact-forces.html', true),
  ('KS4', 11, 'foundation', 'combined', (select id from public.subjects where name = 'Physics'), 'AQA', 10, null, 'Forces', 'gravity', '/combined/foundation/physics/forces/gravity.html', true),
  ('KS4', 11, 'foundation', 'combined', (select id from public.subjects where name = 'Physics'), 'AQA', 11, null, 'Forces', 'resultant-forces', '/combined/foundation/physics/forces/resultant-forces.html', true),
  ('KS4', 11, 'foundation', 'combined', (select id from public.subjects where name = 'Physics'), 'AQA', 12, null, 'Forces', 'work-done-energy-transfer', '/combined/foundation/physics/forces/work-done-energy-transfer.html', true),
  ('KS4', 11, 'foundation', 'combined', (select id from public.subjects where name = 'Physics'), 'AQA', 13, null, 'Forces', 'forces-elasticity', '/combined/foundation/physics/forces/forces-elasticity.html', true),
  ('KS4', 11, 'foundation', 'combined', (select id from public.subjects where name = 'Physics'), 'AQA', 14, null, 'Forces', 'distance-speed-velocity', '/combined/foundation/physics/forces/distance-speed-velocity.html', true),
  ('KS4', 11, 'foundation', 'combined', (select id from public.subjects where name = 'Physics'), 'AQA', 15, null, 'Forces', 'distance-time-graphs', '/combined/foundation/physics/forces/distance-time-graphs.html', true),
  ('KS4', 11, 'foundation', 'combined', (select id from public.subjects where name = 'Physics'), 'AQA', 16, null, 'Forces', 'acceleration', '/combined/foundation/physics/forces/acceleration.html', true),
  ('KS4', 11, 'foundation', 'combined', (select id from public.subjects where name = 'Physics'), 'AQA', 17, null, 'Forces', 'newtons-laws', '/combined/foundation/physics/forces/newtons-laws.html', true),
  ('KS4', 11, 'foundation', 'combined', (select id from public.subjects where name = 'Physics'), 'AQA', 18, null, 'Forces', 'stopping-distance-braking', '/combined/foundation/physics/forces/stopping-distance-braking.html', true),
  -- waves — Waves
  ('KS4', 11, 'foundation', 'combined', (select id from public.subjects where name = 'Physics'), 'AQA', 19, null, 'Waves', 'transverse-longitudinal-waves', '/combined/foundation/physics/waves/transverse-longitudinal-waves.html', true),
  ('KS4', 11, 'foundation', 'combined', (select id from public.subjects where name = 'Physics'), 'AQA', 20, null, 'Waves', 'properties-of-waves', '/combined/foundation/physics/waves/properties-of-waves.html', true),
  ('KS4', 11, 'foundation', 'combined', (select id from public.subjects where name = 'Physics'), 'AQA', 21, null, 'Waves', 'types-of-em-waves', '/combined/foundation/physics/waves/types-of-em-waves.html', true),
  ('KS4', 11, 'foundation', 'combined', (select id from public.subjects where name = 'Physics'), 'AQA', 22, null, 'Waves', 'properties-em-waves-1', '/combined/foundation/physics/waves/properties-em-waves-1.html', true),
  ('KS4', 11, 'foundation', 'combined', (select id from public.subjects where name = 'Physics'), 'AQA', 23, null, 'Waves', 'properties-em-waves-2', '/combined/foundation/physics/waves/properties-em-waves-2.html', true),
  ('KS4', 11, 'foundation', 'combined', (select id from public.subjects where name = 'Physics'), 'AQA', 24, null, 'Waves', 'uses-em-waves', '/combined/foundation/physics/waves/uses-em-waves.html', true),
  -- magnetism — Magnetism and Electromagnetism
  ('KS4', 11, 'foundation', 'combined', (select id from public.subjects where name = 'Physics'), 'AQA', 25, null, 'Magnetism and Electromagnetism', 'poles-of-a-magnet', '/combined/foundation/physics/magnetism/poles-of-a-magnet.html', true),
  ('KS4', 11, 'foundation', 'combined', (select id from public.subjects where name = 'Physics'), 'AQA', 26, null, 'Magnetism and Electromagnetism', 'magnetic-fields', '/combined/foundation/physics/magnetism/magnetic-fields.html', true),
  ('KS4', 11, 'foundation', 'combined', (select id from public.subjects where name = 'Physics'), 'AQA', 27, null, 'Magnetism and Electromagnetism', 'electromagnetism', '/combined/foundation/physics/magnetism/electromagnetism.html', true);

-- ── Combined · Higher · Biology · Year 10 — 32 lessons ─────────────────────
insert into public.scheme_of_work_entries
  (key_stage, year_group, tier, pathway, subject_id, exam_board, academic_week, half_term, topic, subtopic, notes, active)
values
  -- cell-biology — Cell Biology
  ('KS4', 10, 'higher', 'combined', (select id from public.subjects where name = 'Biology'), 'AQA', 1, null, 'Cell Biology', 'eukaryotes-prokaryotes', '/combined/higher/biology/cell-biology/eukaryotes-prokaryotes.html', true),
  ('KS4', 10, 'higher', 'combined', (select id from public.subjects where name = 'Biology'), 'AQA', 2, null, 'Cell Biology', 'animal-plant-cells', '/combined/higher/biology/cell-biology/animal-plant-cells.html', true),
  ('KS4', 10, 'higher', 'combined', (select id from public.subjects where name = 'Biology'), 'AQA', 3, null, 'Cell Biology', 'cell-specialisation', '/combined/higher/biology/cell-biology/cell-specialisation.html', true),
  ('KS4', 10, 'higher', 'combined', (select id from public.subjects where name = 'Biology'), 'AQA', 4, null, 'Cell Biology', 'microscopy', '/combined/higher/biology/cell-biology/microscopy.html', true),
  ('KS4', 10, 'higher', 'combined', (select id from public.subjects where name = 'Biology'), 'AQA', 5, null, 'Cell Biology', 'chromosomes-mitosis', '/combined/higher/biology/cell-biology/chromosomes-mitosis.html', true),
  ('KS4', 10, 'higher', 'combined', (select id from public.subjects where name = 'Biology'), 'AQA', 6, null, 'Cell Biology', 'stem-cells', '/combined/higher/biology/cell-biology/stem-cells.html', true),
  ('KS4', 10, 'higher', 'combined', (select id from public.subjects where name = 'Biology'), 'AQA', 7, null, 'Cell Biology', 'transport-in-cells', '/combined/higher/biology/cell-biology/transport-in-cells.html', true),
  -- organisation — Organisation
  ('KS4', 10, 'higher', 'combined', (select id from public.subjects where name = 'Biology'), 'AQA', 8, null, 'Organisation', 'principles-of-organisation', '/combined/higher/biology/organisation/principles-of-organisation.html', true),
  ('KS4', 10, 'higher', 'combined', (select id from public.subjects where name = 'Biology'), 'AQA', 9, null, 'Organisation', 'digestive-system', '/combined/higher/biology/organisation/digestive-system.html', true),
  ('KS4', 10, 'higher', 'combined', (select id from public.subjects where name = 'Biology'), 'AQA', 10, null, 'Organisation', 'enzymes', '/combined/higher/biology/organisation/enzymes.html', true),
  ('KS4', 10, 'higher', 'combined', (select id from public.subjects where name = 'Biology'), 'AQA', 11, null, 'Organisation', 'heart-blood-vessels', '/combined/higher/biology/organisation/heart-blood-vessels.html', true),
  ('KS4', 10, 'higher', 'combined', (select id from public.subjects where name = 'Biology'), 'AQA', 12, null, 'Organisation', 'blood', '/combined/higher/biology/organisation/blood.html', true),
  ('KS4', 10, 'higher', 'combined', (select id from public.subjects where name = 'Biology'), 'AQA', 13, null, 'Organisation', 'coronary-heart-disease', '/combined/higher/biology/organisation/coronary-heart-disease.html', true),
  ('KS4', 10, 'higher', 'combined', (select id from public.subjects where name = 'Biology'), 'AQA', 14, null, 'Organisation', 'health-disease', '/combined/higher/biology/organisation/health-disease.html', true),
  ('KS4', 10, 'higher', 'combined', (select id from public.subjects where name = 'Biology'), 'AQA', 15, null, 'Organisation', 'cancer', '/combined/higher/biology/organisation/cancer.html', true),
  ('KS4', 10, 'higher', 'combined', (select id from public.subjects where name = 'Biology'), 'AQA', 16, null, 'Organisation', 'plant-tissues', '/combined/higher/biology/organisation/plant-tissues.html', true),
  ('KS4', 10, 'higher', 'combined', (select id from public.subjects where name = 'Biology'), 'AQA', 17, null, 'Organisation', 'transpiration', '/combined/higher/biology/organisation/transpiration.html', true),
  ('KS4', 10, 'higher', 'combined', (select id from public.subjects where name = 'Biology'), 'AQA', 18, null, 'Organisation', 'translocation', '/combined/higher/biology/organisation/translocation.html', true),
  -- infection-response — Infection and Response
  ('KS4', 10, 'higher', 'combined', (select id from public.subjects where name = 'Biology'), 'AQA', 19, null, 'Infection and Response', 'communicable-diseases-defence', '/combined/higher/biology/infection-response/communicable-diseases-defence.html', true),
  ('KS4', 10, 'higher', 'combined', (select id from public.subjects where name = 'Biology'), 'AQA', 20, null, 'Infection and Response', 'viral-diseases', '/combined/higher/biology/infection-response/viral-diseases.html', true),
  ('KS4', 10, 'higher', 'combined', (select id from public.subjects where name = 'Biology'), 'AQA', 21, null, 'Infection and Response', 'bacterial-diseases', '/combined/higher/biology/infection-response/bacterial-diseases.html', true),
  ('KS4', 10, 'higher', 'combined', (select id from public.subjects where name = 'Biology'), 'AQA', 22, null, 'Infection and Response', 'fungal-protist-diseases', '/combined/higher/biology/infection-response/fungal-protist-diseases.html', true),
  ('KS4', 10, 'higher', 'combined', (select id from public.subjects where name = 'Biology'), 'AQA', 23, null, 'Infection and Response', 'vaccination', '/combined/higher/biology/infection-response/vaccination.html', true),
  ('KS4', 10, 'higher', 'combined', (select id from public.subjects where name = 'Biology'), 'AQA', 24, null, 'Infection and Response', 'antibiotics-painkillers', '/combined/higher/biology/infection-response/antibiotics-painkillers.html', true),
  ('KS4', 10, 'higher', 'combined', (select id from public.subjects where name = 'Biology'), 'AQA', 25, null, 'Infection and Response', 'drug-discovery-development', '/combined/higher/biology/infection-response/drug-discovery-development.html', true),
  -- bioenergetics — Bioenergetics
  ('KS4', 10, 'higher', 'combined', (select id from public.subjects where name = 'Biology'), 'AQA', 26, null, 'Bioenergetics', 'photosynthesis', '/combined/higher/biology/bioenergetics/photosynthesis.html', true),
  ('KS4', 10, 'higher', 'combined', (select id from public.subjects where name = 'Biology'), 'AQA', 27, null, 'Bioenergetics', 'rate-of-photosynthesis', '/combined/higher/biology/bioenergetics/rate-of-photosynthesis.html', true),
  ('KS4', 10, 'higher', 'combined', (select id from public.subjects where name = 'Biology'), 'AQA', 28, null, 'Bioenergetics', 'uses-of-glucose', '/combined/higher/biology/bioenergetics/uses-of-glucose.html', true),
  ('KS4', 10, 'higher', 'combined', (select id from public.subjects where name = 'Biology'), 'AQA', 29, null, 'Bioenergetics', 'aerobic-respiration', '/combined/higher/biology/bioenergetics/aerobic-respiration.html', true),
  ('KS4', 10, 'higher', 'combined', (select id from public.subjects where name = 'Biology'), 'AQA', 30, null, 'Bioenergetics', 'anaerobic-respiration', '/combined/higher/biology/bioenergetics/anaerobic-respiration.html', true),
  ('KS4', 10, 'higher', 'combined', (select id from public.subjects where name = 'Biology'), 'AQA', 31, null, 'Bioenergetics', 'response-to-exercise', '/combined/higher/biology/bioenergetics/response-to-exercise.html', true),
  ('KS4', 10, 'higher', 'combined', (select id from public.subjects where name = 'Biology'), 'AQA', 32, null, 'Bioenergetics', 'metabolism', '/combined/higher/biology/bioenergetics/metabolism.html', true);

-- ── Combined · Higher · Biology · Year 11 — 35 lessons ─────────────────────
insert into public.scheme_of_work_entries
  (key_stage, year_group, tier, pathway, subject_id, exam_board, academic_week, half_term, topic, subtopic, notes, active)
values
  -- homeostasis — Homeostasis and Response
  ('KS4', 11, 'higher', 'combined', (select id from public.subjects where name = 'Biology'), 'AQA', 1, null, 'Homeostasis and Response', 'homeostasis', '/combined/higher/biology/homeostasis/homeostasis.html', true),
  ('KS4', 11, 'higher', 'combined', (select id from public.subjects where name = 'Biology'), 'AQA', 2, null, 'Homeostasis and Response', 'nervous-system', '/combined/higher/biology/homeostasis/nervous-system.html', true),
  ('KS4', 11, 'higher', 'combined', (select id from public.subjects where name = 'Biology'), 'AQA', 3, null, 'Homeostasis and Response', 'reflex-actions', '/combined/higher/biology/homeostasis/reflex-actions.html', true),
  ('KS4', 11, 'higher', 'combined', (select id from public.subjects where name = 'Biology'), 'AQA', 4, null, 'Homeostasis and Response', 'endocrine-system', '/combined/higher/biology/homeostasis/endocrine-system.html', true),
  ('KS4', 11, 'higher', 'combined', (select id from public.subjects where name = 'Biology'), 'AQA', 5, null, 'Homeostasis and Response', 'blood-glucose-diabetes', '/combined/higher/biology/homeostasis/blood-glucose-diabetes.html', true),
  ('KS4', 11, 'higher', 'combined', (select id from public.subjects where name = 'Biology'), 'AQA', 6, null, 'Homeostasis and Response', 'human-reproduction-hormones', '/combined/higher/biology/homeostasis/human-reproduction-hormones.html', true),
  ('KS4', 11, 'higher', 'combined', (select id from public.subjects where name = 'Biology'), 'AQA', 7, null, 'Homeostasis and Response', 'contraception-fertility', '/combined/higher/biology/homeostasis/contraception-fertility.html', true),
  ('KS4', 11, 'higher', 'combined', (select id from public.subjects where name = 'Biology'), 'AQA', 8, null, 'Homeostasis and Response', 'reaction-time', '/combined/higher/biology/homeostasis/reaction-time.html', true),
  -- inheritance — Inheritance, Variation and Evolution
  ('KS4', 11, 'higher', 'combined', (select id from public.subjects where name = 'Biology'), 'AQA', 9, null, 'Inheritance, Variation and Evolution', 'sexual-asexual-reproduction', '/combined/higher/biology/inheritance/sexual-asexual-reproduction.html', true),
  ('KS4', 11, 'higher', 'combined', (select id from public.subjects where name = 'Biology'), 'AQA', 10, null, 'Inheritance, Variation and Evolution', 'dna-genome', '/combined/higher/biology/inheritance/dna-genome.html', true),
  ('KS4', 11, 'higher', 'combined', (select id from public.subjects where name = 'Biology'), 'AQA', 11, null, 'Inheritance, Variation and Evolution', 'genetic-inheritance', '/combined/higher/biology/inheritance/genetic-inheritance.html', true),
  ('KS4', 11, 'higher', 'combined', (select id from public.subjects where name = 'Biology'), 'AQA', 12, null, 'Inheritance, Variation and Evolution', 'inherited-disorders', '/combined/higher/biology/inheritance/inherited-disorders.html', true),
  ('KS4', 11, 'higher', 'combined', (select id from public.subjects where name = 'Biology'), 'AQA', 13, null, 'Inheritance, Variation and Evolution', 'sex-determination', '/combined/higher/biology/inheritance/sex-determination.html', true),
  ('KS4', 11, 'higher', 'combined', (select id from public.subjects where name = 'Biology'), 'AQA', 14, null, 'Inheritance, Variation and Evolution', 'variation', '/combined/higher/biology/inheritance/variation.html', true),
  ('KS4', 11, 'higher', 'combined', (select id from public.subjects where name = 'Biology'), 'AQA', 15, null, 'Inheritance, Variation and Evolution', 'evolution-natural-selection', '/combined/higher/biology/inheritance/evolution-natural-selection.html', true),
  ('KS4', 11, 'higher', 'combined', (select id from public.subjects where name = 'Biology'), 'AQA', 16, null, 'Inheritance, Variation and Evolution', 'selective-breeding', '/combined/higher/biology/inheritance/selective-breeding.html', true),
  ('KS4', 11, 'higher', 'combined', (select id from public.subjects where name = 'Biology'), 'AQA', 17, null, 'Inheritance, Variation and Evolution', 'genetic-engineering', '/combined/higher/biology/inheritance/genetic-engineering.html', true),
  ('KS4', 11, 'higher', 'combined', (select id from public.subjects where name = 'Biology'), 'AQA', 18, null, 'Inheritance, Variation and Evolution', 'evidence-for-evolution', '/combined/higher/biology/inheritance/evidence-for-evolution.html', true),
  ('KS4', 11, 'higher', 'combined', (select id from public.subjects where name = 'Biology'), 'AQA', 19, null, 'Inheritance, Variation and Evolution', 'fossils-extinction', '/combined/higher/biology/inheritance/fossils-extinction.html', true),
  ('KS4', 11, 'higher', 'combined', (select id from public.subjects where name = 'Biology'), 'AQA', 20, null, 'Inheritance, Variation and Evolution', 'resistant-bacteria', '/combined/higher/biology/inheritance/resistant-bacteria.html', true),
  -- ecology — Ecology
  ('KS4', 11, 'higher', 'combined', (select id from public.subjects where name = 'Biology'), 'AQA', 21, null, 'Ecology', 'ecosystems', '/combined/higher/biology/ecology/ecosystems.html', true),
  ('KS4', 11, 'higher', 'combined', (select id from public.subjects where name = 'Biology'), 'AQA', 22, null, 'Ecology', 'abiotic-biotic-factors', '/combined/higher/biology/ecology/abiotic-biotic-factors.html', true),
  ('KS4', 11, 'higher', 'combined', (select id from public.subjects where name = 'Biology'), 'AQA', 23, null, 'Ecology', 'adaptations', '/combined/higher/biology/ecology/adaptations.html', true),
  ('KS4', 11, 'higher', 'combined', (select id from public.subjects where name = 'Biology'), 'AQA', 24, null, 'Ecology', 'food-chains-webs', '/combined/higher/biology/ecology/food-chains-webs.html', true),
  ('KS4', 11, 'higher', 'combined', (select id from public.subjects where name = 'Biology'), 'AQA', 25, null, 'Ecology', 'population-competition', '/combined/higher/biology/ecology/population-competition.html', true),
  ('KS4', 11, 'higher', 'combined', (select id from public.subjects where name = 'Biology'), 'AQA', 26, null, 'Ecology', 'biodiversity', '/combined/higher/biology/ecology/biodiversity.html', true),
  ('KS4', 11, 'higher', 'combined', (select id from public.subjects where name = 'Biology'), 'AQA', 27, null, 'Ecology', 'waste-management', '/combined/higher/biology/ecology/waste-management.html', true),
  ('KS4', 11, 'higher', 'combined', (select id from public.subjects where name = 'Biology'), 'AQA', 28, null, 'Ecology', 'land-use', '/combined/higher/biology/ecology/land-use.html', true),
  ('KS4', 11, 'higher', 'combined', (select id from public.subjects where name = 'Biology'), 'AQA', 29, null, 'Ecology', 'deforestation', '/combined/higher/biology/ecology/deforestation.html', true),
  ('KS4', 11, 'higher', 'combined', (select id from public.subjects where name = 'Biology'), 'AQA', 30, null, 'Ecology', 'global-warming', '/combined/higher/biology/ecology/global-warming.html', true),
  ('KS4', 11, 'higher', 'combined', (select id from public.subjects where name = 'Biology'), 'AQA', 31, null, 'Ecology', 'maintaining-biodiversity', '/combined/higher/biology/ecology/maintaining-biodiversity.html', true),
  ('KS4', 11, 'higher', 'combined', (select id from public.subjects where name = 'Biology'), 'AQA', 32, null, 'Ecology', 'carbon-cycle', '/combined/higher/biology/ecology/carbon-cycle.html', true),
  ('KS4', 11, 'higher', 'combined', (select id from public.subjects where name = 'Biology'), 'AQA', 33, null, 'Ecology', 'water-cycle', '/combined/higher/biology/ecology/water-cycle.html', true),
  ('KS4', 11, 'higher', 'combined', (select id from public.subjects where name = 'Biology'), 'AQA', 34, null, 'Ecology', 'decomposition', '/combined/higher/biology/ecology/decomposition.html', true),
  ('KS4', 11, 'higher', 'combined', (select id from public.subjects where name = 'Biology'), 'AQA', 35, null, 'Ecology', 'sampling-techniques', '/combined/higher/biology/ecology/sampling-techniques.html', true);

-- ── Combined · Higher · Chemistry · Year 10 — 31 lessons ─────────────────────
insert into public.scheme_of_work_entries
  (key_stage, year_group, tier, pathway, subject_id, exam_board, academic_week, half_term, topic, subtopic, notes, active)
values
  -- atomic-structure — Atomic Structure and the Periodic Table
  ('KS4', 10, 'higher', 'combined', (select id from public.subjects where name = 'Chemistry'), 'AQA', 1, null, 'Atomic Structure and the Periodic Table', 'atoms-elements-compounds', '/combined/higher/chemistry/atomic-structure/atoms-elements-compounds.html', true),
  ('KS4', 10, 'higher', 'combined', (select id from public.subjects where name = 'Chemistry'), 'AQA', 2, null, 'Atomic Structure and the Periodic Table', 'mixtures', '/combined/higher/chemistry/atomic-structure/mixtures.html', true),
  ('KS4', 10, 'higher', 'combined', (select id from public.subjects where name = 'Chemistry'), 'AQA', 3, null, 'Atomic Structure and the Periodic Table', 'model-of-the-atom', '/combined/higher/chemistry/atomic-structure/model-of-the-atom.html', true),
  ('KS4', 10, 'higher', 'combined', (select id from public.subjects where name = 'Chemistry'), 'AQA', 4, null, 'Atomic Structure and the Periodic Table', 'subatomic-particles', '/combined/higher/chemistry/atomic-structure/subatomic-particles.html', true),
  ('KS4', 10, 'higher', 'combined', (select id from public.subjects where name = 'Chemistry'), 'AQA', 5, null, 'Atomic Structure and the Periodic Table', 'relative-atomic-mass', '/combined/higher/chemistry/atomic-structure/relative-atomic-mass.html', true),
  ('KS4', 10, 'higher', 'combined', (select id from public.subjects where name = 'Chemistry'), 'AQA', 6, null, 'Atomic Structure and the Periodic Table', 'electronic-structure', '/combined/higher/chemistry/atomic-structure/electronic-structure.html', true),
  ('KS4', 10, 'higher', 'combined', (select id from public.subjects where name = 'Chemistry'), 'AQA', 7, null, 'Atomic Structure and the Periodic Table', 'periodic-table', '/combined/higher/chemistry/atomic-structure/periodic-table.html', true),
  ('KS4', 10, 'higher', 'combined', (select id from public.subjects where name = 'Chemistry'), 'AQA', 8, null, 'Atomic Structure and the Periodic Table', 'development-periodic-table', '/combined/higher/chemistry/atomic-structure/development-periodic-table.html', true),
  ('KS4', 10, 'higher', 'combined', (select id from public.subjects where name = 'Chemistry'), 'AQA', 9, null, 'Atomic Structure and the Periodic Table', 'metals-non-metals', '/combined/higher/chemistry/atomic-structure/metals-non-metals.html', true),
  ('KS4', 10, 'higher', 'combined', (select id from public.subjects where name = 'Chemistry'), 'AQA', 10, null, 'Atomic Structure and the Periodic Table', 'group-0', '/combined/higher/chemistry/atomic-structure/group-0.html', true),
  ('KS4', 10, 'higher', 'combined', (select id from public.subjects where name = 'Chemistry'), 'AQA', 11, null, 'Atomic Structure and the Periodic Table', 'group-1', '/combined/higher/chemistry/atomic-structure/group-1.html', true),
  ('KS4', 10, 'higher', 'combined', (select id from public.subjects where name = 'Chemistry'), 'AQA', 12, null, 'Atomic Structure and the Periodic Table', 'group-7', '/combined/higher/chemistry/atomic-structure/group-7.html', true),
  -- bonding — Bonding, Structure and Properties of Matter
  ('KS4', 10, 'higher', 'combined', (select id from public.subjects where name = 'Chemistry'), 'AQA', 13, null, 'Bonding, Structure and Properties of Matter', 'chemical-bonds', '/combined/higher/chemistry/bonding/chemical-bonds.html', true),
  ('KS4', 10, 'higher', 'combined', (select id from public.subjects where name = 'Chemistry'), 'AQA', 14, null, 'Bonding, Structure and Properties of Matter', 'ionic-bonding', '/combined/higher/chemistry/bonding/ionic-bonding.html', true),
  ('KS4', 10, 'higher', 'combined', (select id from public.subjects where name = 'Chemistry'), 'AQA', 15, null, 'Bonding, Structure and Properties of Matter', 'ionic-compounds', '/combined/higher/chemistry/bonding/ionic-compounds.html', true),
  ('KS4', 10, 'higher', 'combined', (select id from public.subjects where name = 'Chemistry'), 'AQA', 16, null, 'Bonding, Structure and Properties of Matter', 'covalent-bonding', '/combined/higher/chemistry/bonding/covalent-bonding.html', true),
  ('KS4', 10, 'higher', 'combined', (select id from public.subjects where name = 'Chemistry'), 'AQA', 17, null, 'Bonding, Structure and Properties of Matter', 'metallic-bonding', '/combined/higher/chemistry/bonding/metallic-bonding.html', true),
  ('KS4', 10, 'higher', 'combined', (select id from public.subjects where name = 'Chemistry'), 'AQA', 18, null, 'Bonding, Structure and Properties of Matter', 'states-of-matter', '/combined/higher/chemistry/bonding/states-of-matter.html', true),
  ('KS4', 10, 'higher', 'combined', (select id from public.subjects where name = 'Chemistry'), 'AQA', 19, null, 'Bonding, Structure and Properties of Matter', 'properties-ionic-compounds', '/combined/higher/chemistry/bonding/properties-ionic-compounds.html', true),
  ('KS4', 10, 'higher', 'combined', (select id from public.subjects where name = 'Chemistry'), 'AQA', 20, null, 'Bonding, Structure and Properties of Matter', 'properties-small-molecules', '/combined/higher/chemistry/bonding/properties-small-molecules.html', true),
  ('KS4', 10, 'higher', 'combined', (select id from public.subjects where name = 'Chemistry'), 'AQA', 21, null, 'Bonding, Structure and Properties of Matter', 'polymers', '/combined/higher/chemistry/bonding/polymers.html', true),
  ('KS4', 10, 'higher', 'combined', (select id from public.subjects where name = 'Chemistry'), 'AQA', 22, null, 'Bonding, Structure and Properties of Matter', 'giant-covalent-structures', '/combined/higher/chemistry/bonding/giant-covalent-structures.html', true),
  ('KS4', 10, 'higher', 'combined', (select id from public.subjects where name = 'Chemistry'), 'AQA', 23, null, 'Bonding, Structure and Properties of Matter', 'metals-alloys', '/combined/higher/chemistry/bonding/metals-alloys.html', true),
  -- quantitative — Quantitative Chemistry
  ('KS4', 10, 'higher', 'combined', (select id from public.subjects where name = 'Chemistry'), 'AQA', 24, null, 'Quantitative Chemistry', 'conservation-of-mass', '/combined/higher/chemistry/quantitative/conservation-of-mass.html', true),
  ('KS4', 10, 'higher', 'combined', (select id from public.subjects where name = 'Chemistry'), 'AQA', 25, null, 'Quantitative Chemistry', 'relative-formula-mass', '/combined/higher/chemistry/quantitative/relative-formula-mass.html', true),
  ('KS4', 10, 'higher', 'combined', (select id from public.subjects where name = 'Chemistry'), 'AQA', 26, null, 'Quantitative Chemistry', 'mass-changes-reactions', '/combined/higher/chemistry/quantitative/mass-changes-reactions.html', true),
  ('KS4', 10, 'higher', 'combined', (select id from public.subjects where name = 'Chemistry'), 'AQA', 27, null, 'Quantitative Chemistry', 'chemical-measurements', '/combined/higher/chemistry/quantitative/chemical-measurements.html', true),
  ('KS4', 10, 'higher', 'combined', (select id from public.subjects where name = 'Chemistry'), 'AQA', 28, null, 'Quantitative Chemistry', 'concentration-of-solutions', '/combined/higher/chemistry/quantitative/concentration-of-solutions.html', true),
  ('KS4', 10, 'higher', 'combined', (select id from public.subjects where name = 'Chemistry'), 'AQA', 29, null, 'Quantitative Chemistry', 'moles', '/combined/higher/chemistry/quantitative/moles.html', true),
  ('KS4', 10, 'higher', 'combined', (select id from public.subjects where name = 'Chemistry'), 'AQA', 30, null, 'Quantitative Chemistry', 'amounts-in-equations', '/combined/higher/chemistry/quantitative/amounts-in-equations.html', true),
  ('KS4', 10, 'higher', 'combined', (select id from public.subjects where name = 'Chemistry'), 'AQA', 31, null, 'Quantitative Chemistry', 'using-moles-calculations', '/combined/higher/chemistry/quantitative/using-moles-calculations.html', true);

-- ── Combined · Higher · Chemistry · Year 11 — 38 lessons ─────────────────────
insert into public.scheme_of_work_entries
  (key_stage, year_group, tier, pathway, subject_id, exam_board, academic_week, half_term, topic, subtopic, notes, active)
values
  -- chemical-changes — Chemical Changes
  ('KS4', 11, 'higher', 'combined', (select id from public.subjects where name = 'Chemistry'), 'AQA', 1, null, 'Chemical Changes', 'reactivity-series', '/combined/higher/chemistry/chemical-changes/reactivity-series.html', true),
  ('KS4', 11, 'higher', 'combined', (select id from public.subjects where name = 'Chemistry'), 'AQA', 2, null, 'Chemical Changes', 'extraction-of-metals', '/combined/higher/chemistry/chemical-changes/extraction-of-metals.html', true),
  ('KS4', 11, 'higher', 'combined', (select id from public.subjects where name = 'Chemistry'), 'AQA', 3, null, 'Chemical Changes', 'oxidation-reduction', '/combined/higher/chemistry/chemical-changes/oxidation-reduction.html', true),
  ('KS4', 11, 'higher', 'combined', (select id from public.subjects where name = 'Chemistry'), 'AQA', 4, null, 'Chemical Changes', 'reactions-of-acids', '/combined/higher/chemistry/chemical-changes/reactions-of-acids.html', true),
  ('KS4', 11, 'higher', 'combined', (select id from public.subjects where name = 'Chemistry'), 'AQA', 5, null, 'Chemical Changes', 'salts-neutralisation', '/combined/higher/chemistry/chemical-changes/salts-neutralisation.html', true),
  ('KS4', 11, 'higher', 'combined', (select id from public.subjects where name = 'Chemistry'), 'AQA', 6, null, 'Chemical Changes', 'ph-scale', '/combined/higher/chemistry/chemical-changes/ph-scale.html', true),
  ('KS4', 11, 'higher', 'combined', (select id from public.subjects where name = 'Chemistry'), 'AQA', 7, null, 'Chemical Changes', 'electrolysis-principles', '/combined/higher/chemistry/chemical-changes/electrolysis-principles.html', true),
  ('KS4', 11, 'higher', 'combined', (select id from public.subjects where name = 'Chemistry'), 'AQA', 8, null, 'Chemical Changes', 'electrolysis-molten', '/combined/higher/chemistry/chemical-changes/electrolysis-molten.html', true),
  ('KS4', 11, 'higher', 'combined', (select id from public.subjects where name = 'Chemistry'), 'AQA', 9, null, 'Chemical Changes', 'electrolysis-extraction', '/combined/higher/chemistry/chemical-changes/electrolysis-extraction.html', true),
  ('KS4', 11, 'higher', 'combined', (select id from public.subjects where name = 'Chemistry'), 'AQA', 10, null, 'Chemical Changes', 'electrolysis-aqueous', '/combined/higher/chemistry/chemical-changes/electrolysis-aqueous.html', true),
  ('KS4', 11, 'higher', 'combined', (select id from public.subjects where name = 'Chemistry'), 'AQA', 11, null, 'Chemical Changes', 'strong-weak-acids', '/combined/higher/chemistry/chemical-changes/strong-weak-acids.html', true),
  ('KS4', 11, 'higher', 'combined', (select id from public.subjects where name = 'Chemistry'), 'AQA', 12, null, 'Chemical Changes', 'half-equations', '/combined/higher/chemistry/chemical-changes/half-equations.html', true),
  -- energy-changes — Energy Changes
  ('KS4', 11, 'higher', 'combined', (select id from public.subjects where name = 'Chemistry'), 'AQA', 13, null, 'Energy Changes', 'exothermic-endothermic', '/combined/higher/chemistry/energy-changes/exothermic-endothermic.html', true),
  ('KS4', 11, 'higher', 'combined', (select id from public.subjects where name = 'Chemistry'), 'AQA', 14, null, 'Energy Changes', 'reaction-profiles', '/combined/higher/chemistry/energy-changes/reaction-profiles.html', true),
  ('KS4', 11, 'higher', 'combined', (select id from public.subjects where name = 'Chemistry'), 'AQA', 15, null, 'Energy Changes', 'bond-energy-calculations', '/combined/higher/chemistry/energy-changes/bond-energy-calculations.html', true),
  -- rates-equilibrium — Rate and Extent of Chemical Change
  ('KS4', 11, 'higher', 'combined', (select id from public.subjects where name = 'Chemistry'), 'AQA', 16, null, 'Rate and Extent of Chemical Change', 'calculating-rates', '/combined/higher/chemistry/rates-equilibrium/calculating-rates.html', true),
  ('KS4', 11, 'higher', 'combined', (select id from public.subjects where name = 'Chemistry'), 'AQA', 17, null, 'Rate and Extent of Chemical Change', 'factors-affecting-rate', '/combined/higher/chemistry/rates-equilibrium/factors-affecting-rate.html', true),
  ('KS4', 11, 'higher', 'combined', (select id from public.subjects where name = 'Chemistry'), 'AQA', 18, null, 'Rate and Extent of Chemical Change', 'collision-theory', '/combined/higher/chemistry/rates-equilibrium/collision-theory.html', true),
  ('KS4', 11, 'higher', 'combined', (select id from public.subjects where name = 'Chemistry'), 'AQA', 19, null, 'Rate and Extent of Chemical Change', 'catalysts', '/combined/higher/chemistry/rates-equilibrium/catalysts.html', true),
  ('KS4', 11, 'higher', 'combined', (select id from public.subjects where name = 'Chemistry'), 'AQA', 20, null, 'Rate and Extent of Chemical Change', 'reversible-reactions-equilibrium', '/combined/higher/chemistry/rates-equilibrium/reversible-reactions-equilibrium.html', true),
  ('KS4', 11, 'higher', 'combined', (select id from public.subjects where name = 'Chemistry'), 'AQA', 21, null, 'Rate and Extent of Chemical Change', 'effect-of-conditions-equilibrium', '/combined/higher/chemistry/rates-equilibrium/effect-of-conditions-equilibrium.html', true),
  -- organic — Organic Chemistry
  ('KS4', 11, 'higher', 'combined', (select id from public.subjects where name = 'Chemistry'), 'AQA', 22, null, 'Organic Chemistry', 'crude-oil-hydrocarbons', '/combined/higher/chemistry/organic/crude-oil-hydrocarbons.html', true),
  ('KS4', 11, 'higher', 'combined', (select id from public.subjects where name = 'Chemistry'), 'AQA', 23, null, 'Organic Chemistry', 'fractional-distillation', '/combined/higher/chemistry/organic/fractional-distillation.html', true),
  ('KS4', 11, 'higher', 'combined', (select id from public.subjects where name = 'Chemistry'), 'AQA', 24, null, 'Organic Chemistry', 'properties-of-hydrocarbons', '/combined/higher/chemistry/organic/properties-of-hydrocarbons.html', true),
  ('KS4', 11, 'higher', 'combined', (select id from public.subjects where name = 'Chemistry'), 'AQA', 25, null, 'Organic Chemistry', 'cracking-alkenes', '/combined/higher/chemistry/organic/cracking-alkenes.html', true),
  -- analysis — Chemical Analysis
  ('KS4', 11, 'higher', 'combined', (select id from public.subjects where name = 'Chemistry'), 'AQA', 26, null, 'Chemical Analysis', 'pure-substances', '/combined/higher/chemistry/analysis/pure-substances.html', true),
  ('KS4', 11, 'higher', 'combined', (select id from public.subjects where name = 'Chemistry'), 'AQA', 27, null, 'Chemical Analysis', 'formulations', '/combined/higher/chemistry/analysis/formulations.html', true),
  ('KS4', 11, 'higher', 'combined', (select id from public.subjects where name = 'Chemistry'), 'AQA', 28, null, 'Chemical Analysis', 'chromatography', '/combined/higher/chemistry/analysis/chromatography.html', true),
  ('KS4', 11, 'higher', 'combined', (select id from public.subjects where name = 'Chemistry'), 'AQA', 29, null, 'Chemical Analysis', 'testing-for-gases', '/combined/higher/chemistry/analysis/testing-for-gases.html', true),
  -- atmosphere — Chemistry of the Atmosphere
  ('KS4', 11, 'higher', 'combined', (select id from public.subjects where name = 'Chemistry'), 'AQA', 30, null, 'Chemistry of the Atmosphere', 'composition-of-atmosphere', '/combined/higher/chemistry/atmosphere/composition-of-atmosphere.html', true),
  ('KS4', 11, 'higher', 'combined', (select id from public.subjects where name = 'Chemistry'), 'AQA', 31, null, 'Chemistry of the Atmosphere', 'early-atmosphere', '/combined/higher/chemistry/atmosphere/early-atmosphere.html', true),
  ('KS4', 11, 'higher', 'combined', (select id from public.subjects where name = 'Chemistry'), 'AQA', 32, null, 'Chemistry of the Atmosphere', 'greenhouse-gases', '/combined/higher/chemistry/atmosphere/greenhouse-gases.html', true),
  ('KS4', 11, 'higher', 'combined', (select id from public.subjects where name = 'Chemistry'), 'AQA', 33, null, 'Chemistry of the Atmosphere', 'atmospheric-pollutants', '/combined/higher/chemistry/atmosphere/atmospheric-pollutants.html', true),
  -- resources — Using Resources
  ('KS4', 11, 'higher', 'combined', (select id from public.subjects where name = 'Chemistry'), 'AQA', 34, null, 'Using Resources', 'earths-resources', '/combined/higher/chemistry/resources/earths-resources.html', true),
  ('KS4', 11, 'higher', 'combined', (select id from public.subjects where name = 'Chemistry'), 'AQA', 35, null, 'Using Resources', 'potable-water', '/combined/higher/chemistry/resources/potable-water.html', true),
  ('KS4', 11, 'higher', 'combined', (select id from public.subjects where name = 'Chemistry'), 'AQA', 36, null, 'Using Resources', 'life-cycle-assessment', '/combined/higher/chemistry/resources/life-cycle-assessment.html', true),
  ('KS4', 11, 'higher', 'combined', (select id from public.subjects where name = 'Chemistry'), 'AQA', 37, null, 'Using Resources', 'reducing-use-of-resources', '/combined/higher/chemistry/resources/reducing-use-of-resources.html', true),
  ('KS4', 11, 'higher', 'combined', (select id from public.subjects where name = 'Chemistry'), 'AQA', 38, null, 'Using Resources', 'alternative-metal-extraction', '/combined/higher/chemistry/resources/alternative-metal-extraction.html', true);

-- ── Combined · Higher · Physics · Year 10 — 23 lessons ─────────────────────
insert into public.scheme_of_work_entries
  (key_stage, year_group, tier, pathway, subject_id, exam_board, academic_week, half_term, topic, subtopic, notes, active)
values
  -- energy — Energy
  ('KS4', 10, 'higher', 'combined', (select id from public.subjects where name = 'Physics'), 'AQA', 1, null, 'Energy', 'energy-stores-systems', '/combined/higher/physics/energy/energy-stores-systems.html', true),
  ('KS4', 10, 'higher', 'combined', (select id from public.subjects where name = 'Physics'), 'AQA', 2, null, 'Energy', 'changes-in-energy', '/combined/higher/physics/energy/changes-in-energy.html', true),
  ('KS4', 10, 'higher', 'combined', (select id from public.subjects where name = 'Physics'), 'AQA', 3, null, 'Energy', 'energy-changes-in-systems', '/combined/higher/physics/energy/energy-changes-in-systems.html', true),
  ('KS4', 10, 'higher', 'combined', (select id from public.subjects where name = 'Physics'), 'AQA', 4, null, 'Energy', 'power', '/combined/higher/physics/energy/power.html', true),
  ('KS4', 10, 'higher', 'combined', (select id from public.subjects where name = 'Physics'), 'AQA', 5, null, 'Energy', 'energy-transfers-in-a-system', '/combined/higher/physics/energy/energy-transfers-in-a-system.html', true),
  ('KS4', 10, 'higher', 'combined', (select id from public.subjects where name = 'Physics'), 'AQA', 6, null, 'Energy', 'efficiency', '/combined/higher/physics/energy/efficiency.html', true),
  ('KS4', 10, 'higher', 'combined', (select id from public.subjects where name = 'Physics'), 'AQA', 7, null, 'Energy', 'energy-resources', '/combined/higher/physics/energy/energy-resources.html', true),
  -- electricity — Electricity
  ('KS4', 10, 'higher', 'combined', (select id from public.subjects where name = 'Physics'), 'AQA', 8, null, 'Electricity', 'circuit-symbols', '/combined/higher/physics/electricity/circuit-symbols.html', true),
  ('KS4', 10, 'higher', 'combined', (select id from public.subjects where name = 'Physics'), 'AQA', 9, null, 'Electricity', 'electrical-charge-current', '/combined/higher/physics/electricity/electrical-charge-current.html', true),
  ('KS4', 10, 'higher', 'combined', (select id from public.subjects where name = 'Physics'), 'AQA', 10, null, 'Electricity', 'current-resistance-pd', '/combined/higher/physics/electricity/current-resistance-pd.html', true),
  ('KS4', 10, 'higher', 'combined', (select id from public.subjects where name = 'Physics'), 'AQA', 11, null, 'Electricity', 'resistors', '/combined/higher/physics/electricity/resistors.html', true),
  ('KS4', 10, 'higher', 'combined', (select id from public.subjects where name = 'Physics'), 'AQA', 12, null, 'Electricity', 'series-parallel-circuits', '/combined/higher/physics/electricity/series-parallel-circuits.html', true),
  ('KS4', 10, 'higher', 'combined', (select id from public.subjects where name = 'Physics'), 'AQA', 13, null, 'Electricity', 'direct-alternating-pd', '/combined/higher/physics/electricity/direct-alternating-pd.html', true),
  ('KS4', 10, 'higher', 'combined', (select id from public.subjects where name = 'Physics'), 'AQA', 14, null, 'Electricity', 'mains-electricity', '/combined/higher/physics/electricity/mains-electricity.html', true),
  ('KS4', 10, 'higher', 'combined', (select id from public.subjects where name = 'Physics'), 'AQA', 15, null, 'Electricity', 'power-electricity', '/combined/higher/physics/electricity/power-electricity.html', true),
  ('KS4', 10, 'higher', 'combined', (select id from public.subjects where name = 'Physics'), 'AQA', 16, null, 'Electricity', 'energy-transfers-appliances', '/combined/higher/physics/electricity/energy-transfers-appliances.html', true),
  ('KS4', 10, 'higher', 'combined', (select id from public.subjects where name = 'Physics'), 'AQA', 17, null, 'Electricity', 'national-grid', '/combined/higher/physics/electricity/national-grid.html', true),
  -- particle-model — Particle Model of Matter
  ('KS4', 10, 'higher', 'combined', (select id from public.subjects where name = 'Physics'), 'AQA', 18, null, 'Particle Model of Matter', 'density-of-materials', '/combined/higher/physics/particle-model/density-of-materials.html', true),
  ('KS4', 10, 'higher', 'combined', (select id from public.subjects where name = 'Physics'), 'AQA', 19, null, 'Particle Model of Matter', 'changes-of-state', '/combined/higher/physics/particle-model/changes-of-state.html', true),
  ('KS4', 10, 'higher', 'combined', (select id from public.subjects where name = 'Physics'), 'AQA', 20, null, 'Particle Model of Matter', 'internal-energy', '/combined/higher/physics/particle-model/internal-energy.html', true),
  ('KS4', 10, 'higher', 'combined', (select id from public.subjects where name = 'Physics'), 'AQA', 21, null, 'Particle Model of Matter', 'temperature-changes-shc', '/combined/higher/physics/particle-model/temperature-changes-shc.html', true),
  ('KS4', 10, 'higher', 'combined', (select id from public.subjects where name = 'Physics'), 'AQA', 22, null, 'Particle Model of Matter', 'specific-latent-heat', '/combined/higher/physics/particle-model/specific-latent-heat.html', true),
  ('KS4', 10, 'higher', 'combined', (select id from public.subjects where name = 'Physics'), 'AQA', 23, null, 'Particle Model of Matter', 'particle-motion-pressure', '/combined/higher/physics/particle-model/particle-motion-pressure.html', true);

-- ── Combined · Higher · Physics · Year 11 — 30 lessons ─────────────────────
insert into public.scheme_of_work_entries
  (key_stage, year_group, tier, pathway, subject_id, exam_board, academic_week, half_term, topic, subtopic, notes, active)
values
  -- atomic-structure — Atomic Structure
  ('KS4', 11, 'higher', 'combined', (select id from public.subjects where name = 'Physics'), 'AQA', 1, null, 'Atomic Structure', 'structure-of-atom', '/combined/higher/physics/atomic-structure/structure-of-atom.html', true),
  ('KS4', 11, 'higher', 'combined', (select id from public.subjects where name = 'Physics'), 'AQA', 2, null, 'Atomic Structure', 'mass-number-isotopes', '/combined/higher/physics/atomic-structure/mass-number-isotopes.html', true),
  ('KS4', 11, 'higher', 'combined', (select id from public.subjects where name = 'Physics'), 'AQA', 3, null, 'Atomic Structure', 'development-atomic-model', '/combined/higher/physics/atomic-structure/development-atomic-model.html', true),
  ('KS4', 11, 'higher', 'combined', (select id from public.subjects where name = 'Physics'), 'AQA', 4, null, 'Atomic Structure', 'radioactive-decay', '/combined/higher/physics/atomic-structure/radioactive-decay.html', true),
  ('KS4', 11, 'higher', 'combined', (select id from public.subjects where name = 'Physics'), 'AQA', 5, null, 'Atomic Structure', 'nuclear-equations', '/combined/higher/physics/atomic-structure/nuclear-equations.html', true),
  ('KS4', 11, 'higher', 'combined', (select id from public.subjects where name = 'Physics'), 'AQA', 6, null, 'Atomic Structure', 'half-lives', '/combined/higher/physics/atomic-structure/half-lives.html', true),
  ('KS4', 11, 'higher', 'combined', (select id from public.subjects where name = 'Physics'), 'AQA', 7, null, 'Atomic Structure', 'radioactive-contamination', '/combined/higher/physics/atomic-structure/radioactive-contamination.html', true),
  -- forces — Forces
  ('KS4', 11, 'higher', 'combined', (select id from public.subjects where name = 'Physics'), 'AQA', 8, null, 'Forces', 'scalar-vector-quantities', '/combined/higher/physics/forces/scalar-vector-quantities.html', true),
  ('KS4', 11, 'higher', 'combined', (select id from public.subjects where name = 'Physics'), 'AQA', 9, null, 'Forces', 'contact-noncontact-forces', '/combined/higher/physics/forces/contact-noncontact-forces.html', true),
  ('KS4', 11, 'higher', 'combined', (select id from public.subjects where name = 'Physics'), 'AQA', 10, null, 'Forces', 'gravity', '/combined/higher/physics/forces/gravity.html', true),
  ('KS4', 11, 'higher', 'combined', (select id from public.subjects where name = 'Physics'), 'AQA', 11, null, 'Forces', 'resultant-forces', '/combined/higher/physics/forces/resultant-forces.html', true),
  ('KS4', 11, 'higher', 'combined', (select id from public.subjects where name = 'Physics'), 'AQA', 12, null, 'Forces', 'work-done-energy-transfer', '/combined/higher/physics/forces/work-done-energy-transfer.html', true),
  ('KS4', 11, 'higher', 'combined', (select id from public.subjects where name = 'Physics'), 'AQA', 13, null, 'Forces', 'forces-elasticity', '/combined/higher/physics/forces/forces-elasticity.html', true),
  ('KS4', 11, 'higher', 'combined', (select id from public.subjects where name = 'Physics'), 'AQA', 14, null, 'Forces', 'distance-speed-velocity', '/combined/higher/physics/forces/distance-speed-velocity.html', true),
  ('KS4', 11, 'higher', 'combined', (select id from public.subjects where name = 'Physics'), 'AQA', 15, null, 'Forces', 'distance-time-graphs', '/combined/higher/physics/forces/distance-time-graphs.html', true),
  ('KS4', 11, 'higher', 'combined', (select id from public.subjects where name = 'Physics'), 'AQA', 16, null, 'Forces', 'acceleration', '/combined/higher/physics/forces/acceleration.html', true),
  ('KS4', 11, 'higher', 'combined', (select id from public.subjects where name = 'Physics'), 'AQA', 17, null, 'Forces', 'newtons-laws', '/combined/higher/physics/forces/newtons-laws.html', true),
  ('KS4', 11, 'higher', 'combined', (select id from public.subjects where name = 'Physics'), 'AQA', 18, null, 'Forces', 'stopping-distance-braking', '/combined/higher/physics/forces/stopping-distance-braking.html', true),
  ('KS4', 11, 'higher', 'combined', (select id from public.subjects where name = 'Physics'), 'AQA', 19, null, 'Forces', 'momentum', '/combined/higher/physics/forces/momentum.html', true),
  -- waves — Waves
  ('KS4', 11, 'higher', 'combined', (select id from public.subjects where name = 'Physics'), 'AQA', 20, null, 'Waves', 'transverse-longitudinal-waves', '/combined/higher/physics/waves/transverse-longitudinal-waves.html', true),
  ('KS4', 11, 'higher', 'combined', (select id from public.subjects where name = 'Physics'), 'AQA', 21, null, 'Waves', 'properties-of-waves', '/combined/higher/physics/waves/properties-of-waves.html', true),
  ('KS4', 11, 'higher', 'combined', (select id from public.subjects where name = 'Physics'), 'AQA', 22, null, 'Waves', 'types-of-em-waves', '/combined/higher/physics/waves/types-of-em-waves.html', true),
  ('KS4', 11, 'higher', 'combined', (select id from public.subjects where name = 'Physics'), 'AQA', 23, null, 'Waves', 'properties-em-waves-1', '/combined/higher/physics/waves/properties-em-waves-1.html', true),
  ('KS4', 11, 'higher', 'combined', (select id from public.subjects where name = 'Physics'), 'AQA', 24, null, 'Waves', 'properties-em-waves-2', '/combined/higher/physics/waves/properties-em-waves-2.html', true),
  ('KS4', 11, 'higher', 'combined', (select id from public.subjects where name = 'Physics'), 'AQA', 25, null, 'Waves', 'uses-em-waves', '/combined/higher/physics/waves/uses-em-waves.html', true),
  -- magnetism — Magnetism and Electromagnetism
  ('KS4', 11, 'higher', 'combined', (select id from public.subjects where name = 'Physics'), 'AQA', 26, null, 'Magnetism and Electromagnetism', 'poles-of-a-magnet', '/combined/higher/physics/magnetism/poles-of-a-magnet.html', true),
  ('KS4', 11, 'higher', 'combined', (select id from public.subjects where name = 'Physics'), 'AQA', 27, null, 'Magnetism and Electromagnetism', 'magnetic-fields', '/combined/higher/physics/magnetism/magnetic-fields.html', true),
  ('KS4', 11, 'higher', 'combined', (select id from public.subjects where name = 'Physics'), 'AQA', 28, null, 'Magnetism and Electromagnetism', 'electromagnetism', '/combined/higher/physics/magnetism/electromagnetism.html', true),
  ('KS4', 11, 'higher', 'combined', (select id from public.subjects where name = 'Physics'), 'AQA', 29, null, 'Magnetism and Electromagnetism', 'flemings-left-hand-rule', '/combined/higher/physics/magnetism/flemings-left-hand-rule.html', true),
  ('KS4', 11, 'higher', 'combined', (select id from public.subjects where name = 'Physics'), 'AQA', 30, null, 'Magnetism and Electromagnetism', 'electric-motors', '/combined/higher/physics/magnetism/electric-motors.html', true);

-- ── Triple · Foundation · Biology · Year 10 — 46 lessons ─────────────────────
insert into public.scheme_of_work_entries
  (key_stage, year_group, tier, pathway, subject_id, exam_board, academic_week, half_term, topic, subtopic, notes, active)
values
  -- cell-biology — Cell Biology
  ('KS4', 10, 'foundation', 'triple', (select id from public.subjects where name = 'Biology'), 'AQA', 1, null, 'Cell Biology', 'eukaryotes-prokaryotes', '/triple/foundation/biology/cell-biology/eukaryotes-prokaryotes.html', true),
  ('KS4', 10, 'foundation', 'triple', (select id from public.subjects where name = 'Biology'), 'AQA', 2, null, 'Cell Biology', 'animal-plant-cells', '/triple/foundation/biology/cell-biology/animal-plant-cells.html', true),
  ('KS4', 10, 'foundation', 'triple', (select id from public.subjects where name = 'Biology'), 'AQA', 3, null, 'Cell Biology', 'cell-specialisation', '/triple/foundation/biology/cell-biology/cell-specialisation.html', true),
  ('KS4', 10, 'foundation', 'triple', (select id from public.subjects where name = 'Biology'), 'AQA', 4, null, 'Cell Biology', 'microscopy', '/triple/foundation/biology/cell-biology/microscopy.html', true),
  ('KS4', 10, 'foundation', 'triple', (select id from public.subjects where name = 'Biology'), 'AQA', 5, null, 'Cell Biology', 'chromosomes-mitosis', '/triple/foundation/biology/cell-biology/chromosomes-mitosis.html', true),
  ('KS4', 10, 'foundation', 'triple', (select id from public.subjects where name = 'Biology'), 'AQA', 6, null, 'Cell Biology', 'stem-cells', '/triple/foundation/biology/cell-biology/stem-cells.html', true),
  ('KS4', 10, 'foundation', 'triple', (select id from public.subjects where name = 'Biology'), 'AQA', 7, null, 'Cell Biology', 'transport-in-cells', '/triple/foundation/biology/cell-biology/transport-in-cells.html', true),
  ('KS4', 10, 'foundation', 'triple', (select id from public.subjects where name = 'Biology'), 'AQA', 8, null, 'Cell Biology', 'culturing-microorganisms', '/triple/foundation/biology/cell-biology/culturing-microorganisms.html', true),
  -- organisation — Organisation
  ('KS4', 10, 'foundation', 'triple', (select id from public.subjects where name = 'Biology'), 'AQA', 9, null, 'Organisation', 'principles-of-organisation', '/triple/foundation/biology/organisation/principles-of-organisation.html', true),
  ('KS4', 10, 'foundation', 'triple', (select id from public.subjects where name = 'Biology'), 'AQA', 10, null, 'Organisation', 'digestive-system', '/triple/foundation/biology/organisation/digestive-system.html', true),
  ('KS4', 10, 'foundation', 'triple', (select id from public.subjects where name = 'Biology'), 'AQA', 11, null, 'Organisation', 'enzymes', '/triple/foundation/biology/organisation/enzymes.html', true),
  ('KS4', 10, 'foundation', 'triple', (select id from public.subjects where name = 'Biology'), 'AQA', 12, null, 'Organisation', 'heart-blood-vessels', '/triple/foundation/biology/organisation/heart-blood-vessels.html', true),
  ('KS4', 10, 'foundation', 'triple', (select id from public.subjects where name = 'Biology'), 'AQA', 13, null, 'Organisation', 'blood', '/triple/foundation/biology/organisation/blood.html', true),
  ('KS4', 10, 'foundation', 'triple', (select id from public.subjects where name = 'Biology'), 'AQA', 14, null, 'Organisation', 'coronary-heart-disease', '/triple/foundation/biology/organisation/coronary-heart-disease.html', true),
  ('KS4', 10, 'foundation', 'triple', (select id from public.subjects where name = 'Biology'), 'AQA', 15, null, 'Organisation', 'health-disease', '/triple/foundation/biology/organisation/health-disease.html', true),
  ('KS4', 10, 'foundation', 'triple', (select id from public.subjects where name = 'Biology'), 'AQA', 16, null, 'Organisation', 'cancer', '/triple/foundation/biology/organisation/cancer.html', true),
  ('KS4', 10, 'foundation', 'triple', (select id from public.subjects where name = 'Biology'), 'AQA', 17, null, 'Organisation', 'plant-tissues', '/triple/foundation/biology/organisation/plant-tissues.html', true),
  ('KS4', 10, 'foundation', 'triple', (select id from public.subjects where name = 'Biology'), 'AQA', 18, null, 'Organisation', 'transpiration', '/triple/foundation/biology/organisation/transpiration.html', true),
  ('KS4', 10, 'foundation', 'triple', (select id from public.subjects where name = 'Biology'), 'AQA', 19, null, 'Organisation', 'translocation', '/triple/foundation/biology/organisation/translocation.html', true),
  -- infection-response — Infection and Response
  ('KS4', 10, 'foundation', 'triple', (select id from public.subjects where name = 'Biology'), 'AQA', 20, null, 'Infection and Response', 'communicable-diseases-defence', '/triple/foundation/biology/infection-response/communicable-diseases-defence.html', true),
  ('KS4', 10, 'foundation', 'triple', (select id from public.subjects where name = 'Biology'), 'AQA', 21, null, 'Infection and Response', 'viral-diseases', '/triple/foundation/biology/infection-response/viral-diseases.html', true),
  ('KS4', 10, 'foundation', 'triple', (select id from public.subjects where name = 'Biology'), 'AQA', 22, null, 'Infection and Response', 'bacterial-diseases', '/triple/foundation/biology/infection-response/bacterial-diseases.html', true),
  ('KS4', 10, 'foundation', 'triple', (select id from public.subjects where name = 'Biology'), 'AQA', 23, null, 'Infection and Response', 'fungal-protist-diseases', '/triple/foundation/biology/infection-response/fungal-protist-diseases.html', true),
  ('KS4', 10, 'foundation', 'triple', (select id from public.subjects where name = 'Biology'), 'AQA', 24, null, 'Infection and Response', 'vaccination', '/triple/foundation/biology/infection-response/vaccination.html', true),
  ('KS4', 10, 'foundation', 'triple', (select id from public.subjects where name = 'Biology'), 'AQA', 25, null, 'Infection and Response', 'antibiotics-painkillers', '/triple/foundation/biology/infection-response/antibiotics-painkillers.html', true),
  ('KS4', 10, 'foundation', 'triple', (select id from public.subjects where name = 'Biology'), 'AQA', 26, null, 'Infection and Response', 'drug-discovery-development', '/triple/foundation/biology/infection-response/drug-discovery-development.html', true),
  ('KS4', 10, 'foundation', 'triple', (select id from public.subjects where name = 'Biology'), 'AQA', 27, null, 'Infection and Response', 'plant-disease-detection-defence', '/triple/foundation/biology/infection-response/plant-disease-detection-defence.html', true),
  -- bioenergetics — Bioenergetics
  ('KS4', 10, 'foundation', 'triple', (select id from public.subjects where name = 'Biology'), 'AQA', 28, null, 'Bioenergetics', 'photosynthesis', '/triple/foundation/biology/bioenergetics/photosynthesis.html', true),
  ('KS4', 10, 'foundation', 'triple', (select id from public.subjects where name = 'Biology'), 'AQA', 29, null, 'Bioenergetics', 'rate-of-photosynthesis', '/triple/foundation/biology/bioenergetics/rate-of-photosynthesis.html', true),
  ('KS4', 10, 'foundation', 'triple', (select id from public.subjects where name = 'Biology'), 'AQA', 30, null, 'Bioenergetics', 'uses-of-glucose', '/triple/foundation/biology/bioenergetics/uses-of-glucose.html', true),
  ('KS4', 10, 'foundation', 'triple', (select id from public.subjects where name = 'Biology'), 'AQA', 31, null, 'Bioenergetics', 'aerobic-respiration', '/triple/foundation/biology/bioenergetics/aerobic-respiration.html', true),
  ('KS4', 10, 'foundation', 'triple', (select id from public.subjects where name = 'Biology'), 'AQA', 32, null, 'Bioenergetics', 'anaerobic-respiration', '/triple/foundation/biology/bioenergetics/anaerobic-respiration.html', true),
  ('KS4', 10, 'foundation', 'triple', (select id from public.subjects where name = 'Biology'), 'AQA', 33, null, 'Bioenergetics', 'response-to-exercise', '/triple/foundation/biology/bioenergetics/response-to-exercise.html', true),
  ('KS4', 10, 'foundation', 'triple', (select id from public.subjects where name = 'Biology'), 'AQA', 34, null, 'Bioenergetics', 'metabolism', '/triple/foundation/biology/bioenergetics/metabolism.html', true),
  -- homeostasis — Homeostasis and Response
  ('KS4', 10, 'foundation', 'triple', (select id from public.subjects where name = 'Biology'), 'AQA', 35, null, 'Homeostasis and Response', 'homeostasis', '/triple/foundation/biology/homeostasis/homeostasis.html', true),
  ('KS4', 10, 'foundation', 'triple', (select id from public.subjects where name = 'Biology'), 'AQA', 36, null, 'Homeostasis and Response', 'nervous-system', '/triple/foundation/biology/homeostasis/nervous-system.html', true),
  ('KS4', 10, 'foundation', 'triple', (select id from public.subjects where name = 'Biology'), 'AQA', 37, null, 'Homeostasis and Response', 'reflex-actions', '/triple/foundation/biology/homeostasis/reflex-actions.html', true),
  ('KS4', 10, 'foundation', 'triple', (select id from public.subjects where name = 'Biology'), 'AQA', 38, null, 'Homeostasis and Response', 'thermoregulation', '/triple/foundation/biology/homeostasis/thermoregulation.html', true),
  ('KS4', 10, 'foundation', 'triple', (select id from public.subjects where name = 'Biology'), 'AQA', 39, null, 'Homeostasis and Response', 'endocrine-system', '/triple/foundation/biology/homeostasis/endocrine-system.html', true),
  ('KS4', 10, 'foundation', 'triple', (select id from public.subjects where name = 'Biology'), 'AQA', 40, null, 'Homeostasis and Response', 'blood-glucose-diabetes', '/triple/foundation/biology/homeostasis/blood-glucose-diabetes.html', true),
  ('KS4', 10, 'foundation', 'triple', (select id from public.subjects where name = 'Biology'), 'AQA', 41, null, 'Homeostasis and Response', 'human-reproduction-hormones', '/triple/foundation/biology/homeostasis/human-reproduction-hormones.html', true),
  ('KS4', 10, 'foundation', 'triple', (select id from public.subjects where name = 'Biology'), 'AQA', 42, null, 'Homeostasis and Response', 'contraception-fertility', '/triple/foundation/biology/homeostasis/contraception-fertility.html', true),
  ('KS4', 10, 'foundation', 'triple', (select id from public.subjects where name = 'Biology'), 'AQA', 43, null, 'Homeostasis and Response', 'reaction-time', '/triple/foundation/biology/homeostasis/reaction-time.html', true),
  ('KS4', 10, 'foundation', 'triple', (select id from public.subjects where name = 'Biology'), 'AQA', 44, null, 'Homeostasis and Response', 'the-brain', '/triple/foundation/biology/homeostasis/the-brain.html', true),
  ('KS4', 10, 'foundation', 'triple', (select id from public.subjects where name = 'Biology'), 'AQA', 45, null, 'Homeostasis and Response', 'the-eye', '/triple/foundation/biology/homeostasis/the-eye.html', true),
  ('KS4', 10, 'foundation', 'triple', (select id from public.subjects where name = 'Biology'), 'AQA', 46, null, 'Homeostasis and Response', 'defects-of-the-eye', '/triple/foundation/biology/homeostasis/defects-of-the-eye.html', true);

-- ── Triple · Foundation · Biology · Year 11 — 41 lessons ─────────────────────
insert into public.scheme_of_work_entries
  (key_stage, year_group, tier, pathway, subject_id, exam_board, academic_week, half_term, topic, subtopic, notes, active)
values
  -- inheritance — Inheritance, Variation and Evolution
  ('KS4', 11, 'foundation', 'triple', (select id from public.subjects where name = 'Biology'), 'AQA', 1, null, 'Inheritance, Variation and Evolution', 'sexual-asexual-reproduction', '/triple/foundation/biology/inheritance/sexual-asexual-reproduction.html', true),
  ('KS4', 11, 'foundation', 'triple', (select id from public.subjects where name = 'Biology'), 'AQA', 2, null, 'Inheritance, Variation and Evolution', 'meiosis', '/triple/foundation/biology/inheritance/meiosis.html', true),
  ('KS4', 11, 'foundation', 'triple', (select id from public.subjects where name = 'Biology'), 'AQA', 3, null, 'Inheritance, Variation and Evolution', 'advantages-sexual-asexual', '/triple/foundation/biology/inheritance/advantages-sexual-asexual.html', true),
  ('KS4', 11, 'foundation', 'triple', (select id from public.subjects where name = 'Biology'), 'AQA', 4, null, 'Inheritance, Variation and Evolution', 'dna-genome', '/triple/foundation/biology/inheritance/dna-genome.html', true),
  ('KS4', 11, 'foundation', 'triple', (select id from public.subjects where name = 'Biology'), 'AQA', 5, null, 'Inheritance, Variation and Evolution', 'dna-structure', '/triple/foundation/biology/inheritance/dna-structure.html', true),
  ('KS4', 11, 'foundation', 'triple', (select id from public.subjects where name = 'Biology'), 'AQA', 6, null, 'Inheritance, Variation and Evolution', 'genetic-inheritance', '/triple/foundation/biology/inheritance/genetic-inheritance.html', true),
  ('KS4', 11, 'foundation', 'triple', (select id from public.subjects where name = 'Biology'), 'AQA', 7, null, 'Inheritance, Variation and Evolution', 'inherited-disorders', '/triple/foundation/biology/inheritance/inherited-disorders.html', true),
  ('KS4', 11, 'foundation', 'triple', (select id from public.subjects where name = 'Biology'), 'AQA', 8, null, 'Inheritance, Variation and Evolution', 'sex-determination', '/triple/foundation/biology/inheritance/sex-determination.html', true),
  ('KS4', 11, 'foundation', 'triple', (select id from public.subjects where name = 'Biology'), 'AQA', 9, null, 'Inheritance, Variation and Evolution', 'variation', '/triple/foundation/biology/inheritance/variation.html', true),
  ('KS4', 11, 'foundation', 'triple', (select id from public.subjects where name = 'Biology'), 'AQA', 10, null, 'Inheritance, Variation and Evolution', 'evolution-natural-selection', '/triple/foundation/biology/inheritance/evolution-natural-selection.html', true),
  ('KS4', 11, 'foundation', 'triple', (select id from public.subjects where name = 'Biology'), 'AQA', 11, null, 'Inheritance, Variation and Evolution', 'theory-of-evolution', '/triple/foundation/biology/inheritance/theory-of-evolution.html', true),
  ('KS4', 11, 'foundation', 'triple', (select id from public.subjects where name = 'Biology'), 'AQA', 12, null, 'Inheritance, Variation and Evolution', 'selective-breeding', '/triple/foundation/biology/inheritance/selective-breeding.html', true),
  ('KS4', 11, 'foundation', 'triple', (select id from public.subjects where name = 'Biology'), 'AQA', 13, null, 'Inheritance, Variation and Evolution', 'genetic-engineering', '/triple/foundation/biology/inheritance/genetic-engineering.html', true),
  ('KS4', 11, 'foundation', 'triple', (select id from public.subjects where name = 'Biology'), 'AQA', 14, null, 'Inheritance, Variation and Evolution', 'cloning', '/triple/foundation/biology/inheritance/cloning.html', true),
  ('KS4', 11, 'foundation', 'triple', (select id from public.subjects where name = 'Biology'), 'AQA', 15, null, 'Inheritance, Variation and Evolution', 'evidence-for-evolution', '/triple/foundation/biology/inheritance/evidence-for-evolution.html', true),
  ('KS4', 11, 'foundation', 'triple', (select id from public.subjects where name = 'Biology'), 'AQA', 16, null, 'Inheritance, Variation and Evolution', 'understanding-genetics', '/triple/foundation/biology/inheritance/understanding-genetics.html', true),
  ('KS4', 11, 'foundation', 'triple', (select id from public.subjects where name = 'Biology'), 'AQA', 17, null, 'Inheritance, Variation and Evolution', 'fossils-extinction', '/triple/foundation/biology/inheritance/fossils-extinction.html', true),
  ('KS4', 11, 'foundation', 'triple', (select id from public.subjects where name = 'Biology'), 'AQA', 18, null, 'Inheritance, Variation and Evolution', 'resistant-bacteria', '/triple/foundation/biology/inheritance/resistant-bacteria.html', true),
  ('KS4', 11, 'foundation', 'triple', (select id from public.subjects where name = 'Biology'), 'AQA', 19, null, 'Inheritance, Variation and Evolution', 'classification-living-organisms', '/triple/foundation/biology/inheritance/classification-living-organisms.html', true),
  -- ecology — Ecology
  ('KS4', 11, 'foundation', 'triple', (select id from public.subjects where name = 'Biology'), 'AQA', 20, null, 'Ecology', 'ecosystems', '/triple/foundation/biology/ecology/ecosystems.html', true),
  ('KS4', 11, 'foundation', 'triple', (select id from public.subjects where name = 'Biology'), 'AQA', 21, null, 'Ecology', 'abiotic-biotic-factors', '/triple/foundation/biology/ecology/abiotic-biotic-factors.html', true),
  ('KS4', 11, 'foundation', 'triple', (select id from public.subjects where name = 'Biology'), 'AQA', 22, null, 'Ecology', 'adaptations', '/triple/foundation/biology/ecology/adaptations.html', true),
  ('KS4', 11, 'foundation', 'triple', (select id from public.subjects where name = 'Biology'), 'AQA', 23, null, 'Ecology', 'food-chains-webs', '/triple/foundation/biology/ecology/food-chains-webs.html', true),
  ('KS4', 11, 'foundation', 'triple', (select id from public.subjects where name = 'Biology'), 'AQA', 24, null, 'Ecology', 'population-competition', '/triple/foundation/biology/ecology/population-competition.html', true),
  ('KS4', 11, 'foundation', 'triple', (select id from public.subjects where name = 'Biology'), 'AQA', 25, null, 'Ecology', 'biodiversity', '/triple/foundation/biology/ecology/biodiversity.html', true),
  ('KS4', 11, 'foundation', 'triple', (select id from public.subjects where name = 'Biology'), 'AQA', 26, null, 'Ecology', 'waste-management', '/triple/foundation/biology/ecology/waste-management.html', true),
  ('KS4', 11, 'foundation', 'triple', (select id from public.subjects where name = 'Biology'), 'AQA', 27, null, 'Ecology', 'land-use', '/triple/foundation/biology/ecology/land-use.html', true),
  ('KS4', 11, 'foundation', 'triple', (select id from public.subjects where name = 'Biology'), 'AQA', 28, null, 'Ecology', 'deforestation', '/triple/foundation/biology/ecology/deforestation.html', true),
  ('KS4', 11, 'foundation', 'triple', (select id from public.subjects where name = 'Biology'), 'AQA', 29, null, 'Ecology', 'global-warming', '/triple/foundation/biology/ecology/global-warming.html', true),
  ('KS4', 11, 'foundation', 'triple', (select id from public.subjects where name = 'Biology'), 'AQA', 30, null, 'Ecology', 'maintaining-biodiversity', '/triple/foundation/biology/ecology/maintaining-biodiversity.html', true),
  ('KS4', 11, 'foundation', 'triple', (select id from public.subjects where name = 'Biology'), 'AQA', 31, null, 'Ecology', 'carbon-cycle', '/triple/foundation/biology/ecology/carbon-cycle.html', true),
  ('KS4', 11, 'foundation', 'triple', (select id from public.subjects where name = 'Biology'), 'AQA', 32, null, 'Ecology', 'water-cycle', '/triple/foundation/biology/ecology/water-cycle.html', true),
  ('KS4', 11, 'foundation', 'triple', (select id from public.subjects where name = 'Biology'), 'AQA', 33, null, 'Ecology', 'decomposition', '/triple/foundation/biology/ecology/decomposition.html', true),
  ('KS4', 11, 'foundation', 'triple', (select id from public.subjects where name = 'Biology'), 'AQA', 34, null, 'Ecology', 'trophic-levels', '/triple/foundation/biology/ecology/trophic-levels.html', true),
  ('KS4', 11, 'foundation', 'triple', (select id from public.subjects where name = 'Biology'), 'AQA', 35, null, 'Ecology', 'pyramids-of-biomass', '/triple/foundation/biology/ecology/pyramids-of-biomass.html', true),
  ('KS4', 11, 'foundation', 'triple', (select id from public.subjects where name = 'Biology'), 'AQA', 36, null, 'Ecology', 'transfer-of-biomass', '/triple/foundation/biology/ecology/transfer-of-biomass.html', true),
  ('KS4', 11, 'foundation', 'triple', (select id from public.subjects where name = 'Biology'), 'AQA', 37, null, 'Ecology', 'sampling-techniques', '/triple/foundation/biology/ecology/sampling-techniques.html', true),
  ('KS4', 11, 'foundation', 'triple', (select id from public.subjects where name = 'Biology'), 'AQA', 38, null, 'Ecology', 'factors-affecting-food-security', '/triple/foundation/biology/ecology/factors-affecting-food-security.html', true),
  ('KS4', 11, 'foundation', 'triple', (select id from public.subjects where name = 'Biology'), 'AQA', 39, null, 'Ecology', 'farming-techniques', '/triple/foundation/biology/ecology/farming-techniques.html', true),
  ('KS4', 11, 'foundation', 'triple', (select id from public.subjects where name = 'Biology'), 'AQA', 40, null, 'Ecology', 'sustainable-fisheries', '/triple/foundation/biology/ecology/sustainable-fisheries.html', true),
  ('KS4', 11, 'foundation', 'triple', (select id from public.subjects where name = 'Biology'), 'AQA', 41, null, 'Ecology', 'role-of-biotechnology', '/triple/foundation/biology/ecology/role-of-biotechnology.html', true);

-- ── Triple · Foundation · Chemistry · Year 10 — 43 lessons ─────────────────────
insert into public.scheme_of_work_entries
  (key_stage, year_group, tier, pathway, subject_id, exam_board, academic_week, half_term, topic, subtopic, notes, active)
values
  -- atomic-structure — Atomic Structure and the Periodic Table
  ('KS4', 10, 'foundation', 'triple', (select id from public.subjects where name = 'Chemistry'), 'AQA', 1, null, 'Atomic Structure and the Periodic Table', 'atoms-elements-compounds', '/triple/foundation/chemistry/atomic-structure/atoms-elements-compounds.html', true),
  ('KS4', 10, 'foundation', 'triple', (select id from public.subjects where name = 'Chemistry'), 'AQA', 2, null, 'Atomic Structure and the Periodic Table', 'mixtures', '/triple/foundation/chemistry/atomic-structure/mixtures.html', true),
  ('KS4', 10, 'foundation', 'triple', (select id from public.subjects where name = 'Chemistry'), 'AQA', 3, null, 'Atomic Structure and the Periodic Table', 'model-of-the-atom', '/triple/foundation/chemistry/atomic-structure/model-of-the-atom.html', true),
  ('KS4', 10, 'foundation', 'triple', (select id from public.subjects where name = 'Chemistry'), 'AQA', 4, null, 'Atomic Structure and the Periodic Table', 'subatomic-particles', '/triple/foundation/chemistry/atomic-structure/subatomic-particles.html', true),
  ('KS4', 10, 'foundation', 'triple', (select id from public.subjects where name = 'Chemistry'), 'AQA', 5, null, 'Atomic Structure and the Periodic Table', 'relative-atomic-mass', '/triple/foundation/chemistry/atomic-structure/relative-atomic-mass.html', true),
  ('KS4', 10, 'foundation', 'triple', (select id from public.subjects where name = 'Chemistry'), 'AQA', 6, null, 'Atomic Structure and the Periodic Table', 'electronic-structure', '/triple/foundation/chemistry/atomic-structure/electronic-structure.html', true),
  ('KS4', 10, 'foundation', 'triple', (select id from public.subjects where name = 'Chemistry'), 'AQA', 7, null, 'Atomic Structure and the Periodic Table', 'periodic-table', '/triple/foundation/chemistry/atomic-structure/periodic-table.html', true),
  ('KS4', 10, 'foundation', 'triple', (select id from public.subjects where name = 'Chemistry'), 'AQA', 8, null, 'Atomic Structure and the Periodic Table', 'development-periodic-table', '/triple/foundation/chemistry/atomic-structure/development-periodic-table.html', true),
  ('KS4', 10, 'foundation', 'triple', (select id from public.subjects where name = 'Chemistry'), 'AQA', 9, null, 'Atomic Structure and the Periodic Table', 'metals-non-metals', '/triple/foundation/chemistry/atomic-structure/metals-non-metals.html', true),
  ('KS4', 10, 'foundation', 'triple', (select id from public.subjects where name = 'Chemistry'), 'AQA', 10, null, 'Atomic Structure and the Periodic Table', 'group-0', '/triple/foundation/chemistry/atomic-structure/group-0.html', true),
  ('KS4', 10, 'foundation', 'triple', (select id from public.subjects where name = 'Chemistry'), 'AQA', 11, null, 'Atomic Structure and the Periodic Table', 'group-1', '/triple/foundation/chemistry/atomic-structure/group-1.html', true),
  ('KS4', 10, 'foundation', 'triple', (select id from public.subjects where name = 'Chemistry'), 'AQA', 12, null, 'Atomic Structure and the Periodic Table', 'group-7', '/triple/foundation/chemistry/atomic-structure/group-7.html', true),
  ('KS4', 10, 'foundation', 'triple', (select id from public.subjects where name = 'Chemistry'), 'AQA', 13, null, 'Atomic Structure and the Periodic Table', 'transition-metals', '/triple/foundation/chemistry/atomic-structure/transition-metals.html', true),
  -- bonding — Bonding, Structure and Properties of Matter
  ('KS4', 10, 'foundation', 'triple', (select id from public.subjects where name = 'Chemistry'), 'AQA', 14, null, 'Bonding, Structure and Properties of Matter', 'chemical-bonds', '/triple/foundation/chemistry/bonding/chemical-bonds.html', true),
  ('KS4', 10, 'foundation', 'triple', (select id from public.subjects where name = 'Chemistry'), 'AQA', 15, null, 'Bonding, Structure and Properties of Matter', 'ionic-bonding', '/triple/foundation/chemistry/bonding/ionic-bonding.html', true),
  ('KS4', 10, 'foundation', 'triple', (select id from public.subjects where name = 'Chemistry'), 'AQA', 16, null, 'Bonding, Structure and Properties of Matter', 'ionic-compounds', '/triple/foundation/chemistry/bonding/ionic-compounds.html', true),
  ('KS4', 10, 'foundation', 'triple', (select id from public.subjects where name = 'Chemistry'), 'AQA', 17, null, 'Bonding, Structure and Properties of Matter', 'covalent-bonding', '/triple/foundation/chemistry/bonding/covalent-bonding.html', true),
  ('KS4', 10, 'foundation', 'triple', (select id from public.subjects where name = 'Chemistry'), 'AQA', 18, null, 'Bonding, Structure and Properties of Matter', 'metallic-bonding', '/triple/foundation/chemistry/bonding/metallic-bonding.html', true),
  ('KS4', 10, 'foundation', 'triple', (select id from public.subjects where name = 'Chemistry'), 'AQA', 19, null, 'Bonding, Structure and Properties of Matter', 'states-of-matter', '/triple/foundation/chemistry/bonding/states-of-matter.html', true),
  ('KS4', 10, 'foundation', 'triple', (select id from public.subjects where name = 'Chemistry'), 'AQA', 20, null, 'Bonding, Structure and Properties of Matter', 'properties-ionic-compounds', '/triple/foundation/chemistry/bonding/properties-ionic-compounds.html', true),
  ('KS4', 10, 'foundation', 'triple', (select id from public.subjects where name = 'Chemistry'), 'AQA', 21, null, 'Bonding, Structure and Properties of Matter', 'properties-small-molecules', '/triple/foundation/chemistry/bonding/properties-small-molecules.html', true),
  ('KS4', 10, 'foundation', 'triple', (select id from public.subjects where name = 'Chemistry'), 'AQA', 22, null, 'Bonding, Structure and Properties of Matter', 'polymers', '/triple/foundation/chemistry/bonding/polymers.html', true),
  ('KS4', 10, 'foundation', 'triple', (select id from public.subjects where name = 'Chemistry'), 'AQA', 23, null, 'Bonding, Structure and Properties of Matter', 'giant-covalent-structures', '/triple/foundation/chemistry/bonding/giant-covalent-structures.html', true),
  ('KS4', 10, 'foundation', 'triple', (select id from public.subjects where name = 'Chemistry'), 'AQA', 24, null, 'Bonding, Structure and Properties of Matter', 'metals-alloys', '/triple/foundation/chemistry/bonding/metals-alloys.html', true),
  ('KS4', 10, 'foundation', 'triple', (select id from public.subjects where name = 'Chemistry'), 'AQA', 25, null, 'Bonding, Structure and Properties of Matter', 'nanoparticles', '/triple/foundation/chemistry/bonding/nanoparticles.html', true),
  -- quantitative — Quantitative Chemistry
  ('KS4', 10, 'foundation', 'triple', (select id from public.subjects where name = 'Chemistry'), 'AQA', 26, null, 'Quantitative Chemistry', 'conservation-of-mass', '/triple/foundation/chemistry/quantitative/conservation-of-mass.html', true),
  ('KS4', 10, 'foundation', 'triple', (select id from public.subjects where name = 'Chemistry'), 'AQA', 27, null, 'Quantitative Chemistry', 'relative-formula-mass', '/triple/foundation/chemistry/quantitative/relative-formula-mass.html', true),
  ('KS4', 10, 'foundation', 'triple', (select id from public.subjects where name = 'Chemistry'), 'AQA', 28, null, 'Quantitative Chemistry', 'mass-changes-reactions', '/triple/foundation/chemistry/quantitative/mass-changes-reactions.html', true),
  ('KS4', 10, 'foundation', 'triple', (select id from public.subjects where name = 'Chemistry'), 'AQA', 29, null, 'Quantitative Chemistry', 'chemical-measurements', '/triple/foundation/chemistry/quantitative/chemical-measurements.html', true),
  ('KS4', 10, 'foundation', 'triple', (select id from public.subjects where name = 'Chemistry'), 'AQA', 30, null, 'Quantitative Chemistry', 'percentage-yield', '/triple/foundation/chemistry/quantitative/percentage-yield.html', true),
  ('KS4', 10, 'foundation', 'triple', (select id from public.subjects where name = 'Chemistry'), 'AQA', 31, null, 'Quantitative Chemistry', 'atom-economy', '/triple/foundation/chemistry/quantitative/atom-economy.html', true),
  ('KS4', 10, 'foundation', 'triple', (select id from public.subjects where name = 'Chemistry'), 'AQA', 32, null, 'Quantitative Chemistry', 'concentration-of-solutions', '/triple/foundation/chemistry/quantitative/concentration-of-solutions.html', true),
  -- chemical-changes — Chemical Changes
  ('KS4', 10, 'foundation', 'triple', (select id from public.subjects where name = 'Chemistry'), 'AQA', 33, null, 'Chemical Changes', 'reactivity-series', '/triple/foundation/chemistry/chemical-changes/reactivity-series.html', true),
  ('KS4', 10, 'foundation', 'triple', (select id from public.subjects where name = 'Chemistry'), 'AQA', 34, null, 'Chemical Changes', 'extraction-of-metals', '/triple/foundation/chemistry/chemical-changes/extraction-of-metals.html', true),
  ('KS4', 10, 'foundation', 'triple', (select id from public.subjects where name = 'Chemistry'), 'AQA', 35, null, 'Chemical Changes', 'oxidation-reduction', '/triple/foundation/chemistry/chemical-changes/oxidation-reduction.html', true),
  ('KS4', 10, 'foundation', 'triple', (select id from public.subjects where name = 'Chemistry'), 'AQA', 36, null, 'Chemical Changes', 'reactions-of-acids', '/triple/foundation/chemistry/chemical-changes/reactions-of-acids.html', true),
  ('KS4', 10, 'foundation', 'triple', (select id from public.subjects where name = 'Chemistry'), 'AQA', 37, null, 'Chemical Changes', 'salts-neutralisation', '/triple/foundation/chemistry/chemical-changes/salts-neutralisation.html', true),
  ('KS4', 10, 'foundation', 'triple', (select id from public.subjects where name = 'Chemistry'), 'AQA', 38, null, 'Chemical Changes', 'ph-scale', '/triple/foundation/chemistry/chemical-changes/ph-scale.html', true),
  ('KS4', 10, 'foundation', 'triple', (select id from public.subjects where name = 'Chemistry'), 'AQA', 39, null, 'Chemical Changes', 'titrations', '/triple/foundation/chemistry/chemical-changes/titrations.html', true),
  ('KS4', 10, 'foundation', 'triple', (select id from public.subjects where name = 'Chemistry'), 'AQA', 40, null, 'Chemical Changes', 'electrolysis-principles', '/triple/foundation/chemistry/chemical-changes/electrolysis-principles.html', true),
  ('KS4', 10, 'foundation', 'triple', (select id from public.subjects where name = 'Chemistry'), 'AQA', 41, null, 'Chemical Changes', 'electrolysis-molten', '/triple/foundation/chemistry/chemical-changes/electrolysis-molten.html', true),
  ('KS4', 10, 'foundation', 'triple', (select id from public.subjects where name = 'Chemistry'), 'AQA', 42, null, 'Chemical Changes', 'electrolysis-extraction', '/triple/foundation/chemistry/chemical-changes/electrolysis-extraction.html', true),
  ('KS4', 10, 'foundation', 'triple', (select id from public.subjects where name = 'Chemistry'), 'AQA', 43, null, 'Chemical Changes', 'electrolysis-aqueous', '/triple/foundation/chemistry/chemical-changes/electrolysis-aqueous.html', true);

-- ── Triple · Foundation · Chemistry · Year 11 — 40 lessons ─────────────────────
insert into public.scheme_of_work_entries
  (key_stage, year_group, tier, pathway, subject_id, exam_board, academic_week, half_term, topic, subtopic, notes, active)
values
  -- energy-changes — Energy Changes
  ('KS4', 11, 'foundation', 'triple', (select id from public.subjects where name = 'Chemistry'), 'AQA', 1, null, 'Energy Changes', 'exothermic-endothermic', '/triple/foundation/chemistry/energy-changes/exothermic-endothermic.html', true),
  ('KS4', 11, 'foundation', 'triple', (select id from public.subjects where name = 'Chemistry'), 'AQA', 2, null, 'Energy Changes', 'reaction-profiles', '/triple/foundation/chemistry/energy-changes/reaction-profiles.html', true),
  ('KS4', 11, 'foundation', 'triple', (select id from public.subjects where name = 'Chemistry'), 'AQA', 3, null, 'Energy Changes', 'cells-and-batteries', '/triple/foundation/chemistry/energy-changes/cells-and-batteries.html', true),
  ('KS4', 11, 'foundation', 'triple', (select id from public.subjects where name = 'Chemistry'), 'AQA', 4, null, 'Energy Changes', 'fuel-cells', '/triple/foundation/chemistry/energy-changes/fuel-cells.html', true),
  -- rates-equilibrium — Rate and Extent of Chemical Change
  ('KS4', 11, 'foundation', 'triple', (select id from public.subjects where name = 'Chemistry'), 'AQA', 5, null, 'Rate and Extent of Chemical Change', 'calculating-rates', '/triple/foundation/chemistry/rates-equilibrium/calculating-rates.html', true),
  ('KS4', 11, 'foundation', 'triple', (select id from public.subjects where name = 'Chemistry'), 'AQA', 6, null, 'Rate and Extent of Chemical Change', 'factors-affecting-rate', '/triple/foundation/chemistry/rates-equilibrium/factors-affecting-rate.html', true),
  ('KS4', 11, 'foundation', 'triple', (select id from public.subjects where name = 'Chemistry'), 'AQA', 7, null, 'Rate and Extent of Chemical Change', 'collision-theory', '/triple/foundation/chemistry/rates-equilibrium/collision-theory.html', true),
  ('KS4', 11, 'foundation', 'triple', (select id from public.subjects where name = 'Chemistry'), 'AQA', 8, null, 'Rate and Extent of Chemical Change', 'catalysts', '/triple/foundation/chemistry/rates-equilibrium/catalysts.html', true),
  ('KS4', 11, 'foundation', 'triple', (select id from public.subjects where name = 'Chemistry'), 'AQA', 9, null, 'Rate and Extent of Chemical Change', 'reversible-reactions-equilibrium', '/triple/foundation/chemistry/rates-equilibrium/reversible-reactions-equilibrium.html', true),
  -- organic — Organic Chemistry
  ('KS4', 11, 'foundation', 'triple', (select id from public.subjects where name = 'Chemistry'), 'AQA', 10, null, 'Organic Chemistry', 'crude-oil-hydrocarbons', '/triple/foundation/chemistry/organic/crude-oil-hydrocarbons.html', true),
  ('KS4', 11, 'foundation', 'triple', (select id from public.subjects where name = 'Chemistry'), 'AQA', 11, null, 'Organic Chemistry', 'fractional-distillation', '/triple/foundation/chemistry/organic/fractional-distillation.html', true),
  ('KS4', 11, 'foundation', 'triple', (select id from public.subjects where name = 'Chemistry'), 'AQA', 12, null, 'Organic Chemistry', 'properties-of-hydrocarbons', '/triple/foundation/chemistry/organic/properties-of-hydrocarbons.html', true),
  ('KS4', 11, 'foundation', 'triple', (select id from public.subjects where name = 'Chemistry'), 'AQA', 13, null, 'Organic Chemistry', 'cracking-alkenes', '/triple/foundation/chemistry/organic/cracking-alkenes.html', true),
  ('KS4', 11, 'foundation', 'triple', (select id from public.subjects where name = 'Chemistry'), 'AQA', 14, null, 'Organic Chemistry', 'structure-of-alkenes', '/triple/foundation/chemistry/organic/structure-of-alkenes.html', true),
  ('KS4', 11, 'foundation', 'triple', (select id from public.subjects where name = 'Chemistry'), 'AQA', 15, null, 'Organic Chemistry', 'reactions-of-alkenes', '/triple/foundation/chemistry/organic/reactions-of-alkenes.html', true),
  ('KS4', 11, 'foundation', 'triple', (select id from public.subjects where name = 'Chemistry'), 'AQA', 16, null, 'Organic Chemistry', 'alcohols', '/triple/foundation/chemistry/organic/alcohols.html', true),
  ('KS4', 11, 'foundation', 'triple', (select id from public.subjects where name = 'Chemistry'), 'AQA', 17, null, 'Organic Chemistry', 'carboxylic-acids', '/triple/foundation/chemistry/organic/carboxylic-acids.html', true),
  ('KS4', 11, 'foundation', 'triple', (select id from public.subjects where name = 'Chemistry'), 'AQA', 18, null, 'Organic Chemistry', 'addition-polymerisation', '/triple/foundation/chemistry/organic/addition-polymerisation.html', true),
  ('KS4', 11, 'foundation', 'triple', (select id from public.subjects where name = 'Chemistry'), 'AQA', 19, null, 'Organic Chemistry', 'dna-naturally-occurring-polymers', '/triple/foundation/chemistry/organic/dna-naturally-occurring-polymers.html', true),
  -- analysis — Chemical Analysis
  ('KS4', 11, 'foundation', 'triple', (select id from public.subjects where name = 'Chemistry'), 'AQA', 20, null, 'Chemical Analysis', 'pure-substances', '/triple/foundation/chemistry/analysis/pure-substances.html', true),
  ('KS4', 11, 'foundation', 'triple', (select id from public.subjects where name = 'Chemistry'), 'AQA', 21, null, 'Chemical Analysis', 'formulations', '/triple/foundation/chemistry/analysis/formulations.html', true),
  ('KS4', 11, 'foundation', 'triple', (select id from public.subjects where name = 'Chemistry'), 'AQA', 22, null, 'Chemical Analysis', 'chromatography', '/triple/foundation/chemistry/analysis/chromatography.html', true),
  ('KS4', 11, 'foundation', 'triple', (select id from public.subjects where name = 'Chemistry'), 'AQA', 23, null, 'Chemical Analysis', 'testing-for-gases', '/triple/foundation/chemistry/analysis/testing-for-gases.html', true),
  ('KS4', 11, 'foundation', 'triple', (select id from public.subjects where name = 'Chemistry'), 'AQA', 24, null, 'Chemical Analysis', 'flame-tests', '/triple/foundation/chemistry/analysis/flame-tests.html', true),
  ('KS4', 11, 'foundation', 'triple', (select id from public.subjects where name = 'Chemistry'), 'AQA', 25, null, 'Chemical Analysis', 'metal-hydroxides', '/triple/foundation/chemistry/analysis/metal-hydroxides.html', true),
  ('KS4', 11, 'foundation', 'triple', (select id from public.subjects where name = 'Chemistry'), 'AQA', 26, null, 'Chemical Analysis', 'carbonates-halides-sulfates', '/triple/foundation/chemistry/analysis/carbonates-halides-sulfates.html', true),
  ('KS4', 11, 'foundation', 'triple', (select id from public.subjects where name = 'Chemistry'), 'AQA', 27, null, 'Chemical Analysis', 'instrumental-methods', '/triple/foundation/chemistry/analysis/instrumental-methods.html', true),
  -- atmosphere — Chemistry of the Atmosphere
  ('KS4', 11, 'foundation', 'triple', (select id from public.subjects where name = 'Chemistry'), 'AQA', 28, null, 'Chemistry of the Atmosphere', 'composition-of-atmosphere', '/triple/foundation/chemistry/atmosphere/composition-of-atmosphere.html', true),
  ('KS4', 11, 'foundation', 'triple', (select id from public.subjects where name = 'Chemistry'), 'AQA', 29, null, 'Chemistry of the Atmosphere', 'early-atmosphere', '/triple/foundation/chemistry/atmosphere/early-atmosphere.html', true),
  ('KS4', 11, 'foundation', 'triple', (select id from public.subjects where name = 'Chemistry'), 'AQA', 30, null, 'Chemistry of the Atmosphere', 'greenhouse-gases', '/triple/foundation/chemistry/atmosphere/greenhouse-gases.html', true),
  ('KS4', 11, 'foundation', 'triple', (select id from public.subjects where name = 'Chemistry'), 'AQA', 31, null, 'Chemistry of the Atmosphere', 'atmospheric-pollutants', '/triple/foundation/chemistry/atmosphere/atmospheric-pollutants.html', true),
  -- resources — Using Resources
  ('KS4', 11, 'foundation', 'triple', (select id from public.subjects where name = 'Chemistry'), 'AQA', 32, null, 'Using Resources', 'earths-resources', '/triple/foundation/chemistry/resources/earths-resources.html', true),
  ('KS4', 11, 'foundation', 'triple', (select id from public.subjects where name = 'Chemistry'), 'AQA', 33, null, 'Using Resources', 'potable-water', '/triple/foundation/chemistry/resources/potable-water.html', true),
  ('KS4', 11, 'foundation', 'triple', (select id from public.subjects where name = 'Chemistry'), 'AQA', 34, null, 'Using Resources', 'life-cycle-assessment', '/triple/foundation/chemistry/resources/life-cycle-assessment.html', true),
  ('KS4', 11, 'foundation', 'triple', (select id from public.subjects where name = 'Chemistry'), 'AQA', 35, null, 'Using Resources', 'reducing-use-of-resources', '/triple/foundation/chemistry/resources/reducing-use-of-resources.html', true),
  ('KS4', 11, 'foundation', 'triple', (select id from public.subjects where name = 'Chemistry'), 'AQA', 36, null, 'Using Resources', 'corrosion-prevention', '/triple/foundation/chemistry/resources/corrosion-prevention.html', true),
  ('KS4', 11, 'foundation', 'triple', (select id from public.subjects where name = 'Chemistry'), 'AQA', 37, null, 'Using Resources', 'alloys-useful-materials', '/triple/foundation/chemistry/resources/alloys-useful-materials.html', true),
  ('KS4', 11, 'foundation', 'triple', (select id from public.subjects where name = 'Chemistry'), 'AQA', 38, null, 'Using Resources', 'ceramics-polymers-composites', '/triple/foundation/chemistry/resources/ceramics-polymers-composites.html', true),
  ('KS4', 11, 'foundation', 'triple', (select id from public.subjects where name = 'Chemistry'), 'AQA', 39, null, 'Using Resources', 'haber-process', '/triple/foundation/chemistry/resources/haber-process.html', true),
  ('KS4', 11, 'foundation', 'triple', (select id from public.subjects where name = 'Chemistry'), 'AQA', 40, null, 'Using Resources', 'npk-fertilisers', '/triple/foundation/chemistry/resources/npk-fertilisers.html', true);

-- ── Triple · Foundation · Physics · Year 10 — 37 lessons ─────────────────────
insert into public.scheme_of_work_entries
  (key_stage, year_group, tier, pathway, subject_id, exam_board, academic_week, half_term, topic, subtopic, notes, active)
values
  -- energy — Energy
  ('KS4', 10, 'foundation', 'triple', (select id from public.subjects where name = 'Physics'), 'AQA', 1, null, 'Energy', 'energy-stores-systems', '/triple/foundation/physics/energy/energy-stores-systems.html', true),
  ('KS4', 10, 'foundation', 'triple', (select id from public.subjects where name = 'Physics'), 'AQA', 2, null, 'Energy', 'changes-in-energy', '/triple/foundation/physics/energy/changes-in-energy.html', true),
  ('KS4', 10, 'foundation', 'triple', (select id from public.subjects where name = 'Physics'), 'AQA', 3, null, 'Energy', 'energy-changes-in-systems', '/triple/foundation/physics/energy/energy-changes-in-systems.html', true),
  ('KS4', 10, 'foundation', 'triple', (select id from public.subjects where name = 'Physics'), 'AQA', 4, null, 'Energy', 'power', '/triple/foundation/physics/energy/power.html', true),
  ('KS4', 10, 'foundation', 'triple', (select id from public.subjects where name = 'Physics'), 'AQA', 5, null, 'Energy', 'energy-transfers-in-a-system', '/triple/foundation/physics/energy/energy-transfers-in-a-system.html', true),
  ('KS4', 10, 'foundation', 'triple', (select id from public.subjects where name = 'Physics'), 'AQA', 6, null, 'Energy', 'efficiency', '/triple/foundation/physics/energy/efficiency.html', true),
  ('KS4', 10, 'foundation', 'triple', (select id from public.subjects where name = 'Physics'), 'AQA', 7, null, 'Energy', 'energy-resources', '/triple/foundation/physics/energy/energy-resources.html', true),
  ('KS4', 10, 'foundation', 'triple', (select id from public.subjects where name = 'Physics'), 'AQA', 8, null, 'Energy', 'thermal-conductivity', '/triple/foundation/physics/energy/thermal-conductivity.html', true),
  -- electricity — Electricity
  ('KS4', 10, 'foundation', 'triple', (select id from public.subjects where name = 'Physics'), 'AQA', 9, null, 'Electricity', 'circuit-symbols', '/triple/foundation/physics/electricity/circuit-symbols.html', true),
  ('KS4', 10, 'foundation', 'triple', (select id from public.subjects where name = 'Physics'), 'AQA', 10, null, 'Electricity', 'electrical-charge-current', '/triple/foundation/physics/electricity/electrical-charge-current.html', true),
  ('KS4', 10, 'foundation', 'triple', (select id from public.subjects where name = 'Physics'), 'AQA', 11, null, 'Electricity', 'current-resistance-pd', '/triple/foundation/physics/electricity/current-resistance-pd.html', true),
  ('KS4', 10, 'foundation', 'triple', (select id from public.subjects where name = 'Physics'), 'AQA', 12, null, 'Electricity', 'resistors', '/triple/foundation/physics/electricity/resistors.html', true),
  ('KS4', 10, 'foundation', 'triple', (select id from public.subjects where name = 'Physics'), 'AQA', 13, null, 'Electricity', 'series-parallel-circuits', '/triple/foundation/physics/electricity/series-parallel-circuits.html', true),
  ('KS4', 10, 'foundation', 'triple', (select id from public.subjects where name = 'Physics'), 'AQA', 14, null, 'Electricity', 'direct-alternating-pd', '/triple/foundation/physics/electricity/direct-alternating-pd.html', true),
  ('KS4', 10, 'foundation', 'triple', (select id from public.subjects where name = 'Physics'), 'AQA', 15, null, 'Electricity', 'mains-electricity', '/triple/foundation/physics/electricity/mains-electricity.html', true),
  ('KS4', 10, 'foundation', 'triple', (select id from public.subjects where name = 'Physics'), 'AQA', 16, null, 'Electricity', 'power-electricity', '/triple/foundation/physics/electricity/power-electricity.html', true),
  ('KS4', 10, 'foundation', 'triple', (select id from public.subjects where name = 'Physics'), 'AQA', 17, null, 'Electricity', 'energy-transfers-appliances', '/triple/foundation/physics/electricity/energy-transfers-appliances.html', true),
  ('KS4', 10, 'foundation', 'triple', (select id from public.subjects where name = 'Physics'), 'AQA', 18, null, 'Electricity', 'national-grid', '/triple/foundation/physics/electricity/national-grid.html', true),
  ('KS4', 10, 'foundation', 'triple', (select id from public.subjects where name = 'Physics'), 'AQA', 19, null, 'Electricity', 'static-charge', '/triple/foundation/physics/electricity/static-charge.html', true),
  ('KS4', 10, 'foundation', 'triple', (select id from public.subjects where name = 'Physics'), 'AQA', 20, null, 'Electricity', 'electric-fields', '/triple/foundation/physics/electricity/electric-fields.html', true),
  -- particle-model — Particle Model of Matter
  ('KS4', 10, 'foundation', 'triple', (select id from public.subjects where name = 'Physics'), 'AQA', 21, null, 'Particle Model of Matter', 'density-of-materials', '/triple/foundation/physics/particle-model/density-of-materials.html', true),
  ('KS4', 10, 'foundation', 'triple', (select id from public.subjects where name = 'Physics'), 'AQA', 22, null, 'Particle Model of Matter', 'changes-of-state', '/triple/foundation/physics/particle-model/changes-of-state.html', true),
  ('KS4', 10, 'foundation', 'triple', (select id from public.subjects where name = 'Physics'), 'AQA', 23, null, 'Particle Model of Matter', 'internal-energy', '/triple/foundation/physics/particle-model/internal-energy.html', true),
  ('KS4', 10, 'foundation', 'triple', (select id from public.subjects where name = 'Physics'), 'AQA', 24, null, 'Particle Model of Matter', 'temperature-changes-shc', '/triple/foundation/physics/particle-model/temperature-changes-shc.html', true),
  ('KS4', 10, 'foundation', 'triple', (select id from public.subjects where name = 'Physics'), 'AQA', 25, null, 'Particle Model of Matter', 'specific-latent-heat', '/triple/foundation/physics/particle-model/specific-latent-heat.html', true),
  ('KS4', 10, 'foundation', 'triple', (select id from public.subjects where name = 'Physics'), 'AQA', 26, null, 'Particle Model of Matter', 'particle-motion-pressure', '/triple/foundation/physics/particle-model/particle-motion-pressure.html', true),
  -- atomic-structure — Atomic Structure
  ('KS4', 10, 'foundation', 'triple', (select id from public.subjects where name = 'Physics'), 'AQA', 27, null, 'Atomic Structure', 'structure-of-atom', '/triple/foundation/physics/atomic-structure/structure-of-atom.html', true),
  ('KS4', 10, 'foundation', 'triple', (select id from public.subjects where name = 'Physics'), 'AQA', 28, null, 'Atomic Structure', 'mass-number-isotopes', '/triple/foundation/physics/atomic-structure/mass-number-isotopes.html', true),
  ('KS4', 10, 'foundation', 'triple', (select id from public.subjects where name = 'Physics'), 'AQA', 29, null, 'Atomic Structure', 'development-atomic-model', '/triple/foundation/physics/atomic-structure/development-atomic-model.html', true),
  ('KS4', 10, 'foundation', 'triple', (select id from public.subjects where name = 'Physics'), 'AQA', 30, null, 'Atomic Structure', 'radioactive-decay', '/triple/foundation/physics/atomic-structure/radioactive-decay.html', true),
  ('KS4', 10, 'foundation', 'triple', (select id from public.subjects where name = 'Physics'), 'AQA', 31, null, 'Atomic Structure', 'nuclear-equations', '/triple/foundation/physics/atomic-structure/nuclear-equations.html', true),
  ('KS4', 10, 'foundation', 'triple', (select id from public.subjects where name = 'Physics'), 'AQA', 32, null, 'Atomic Structure', 'half-lives', '/triple/foundation/physics/atomic-structure/half-lives.html', true),
  ('KS4', 10, 'foundation', 'triple', (select id from public.subjects where name = 'Physics'), 'AQA', 33, null, 'Atomic Structure', 'radioactive-contamination', '/triple/foundation/physics/atomic-structure/radioactive-contamination.html', true),
  ('KS4', 10, 'foundation', 'triple', (select id from public.subjects where name = 'Physics'), 'AQA', 34, null, 'Atomic Structure', 'background-radiation', '/triple/foundation/physics/atomic-structure/background-radiation.html', true),
  ('KS4', 10, 'foundation', 'triple', (select id from public.subjects where name = 'Physics'), 'AQA', 35, null, 'Atomic Structure', 'uses-of-nuclear-radiation', '/triple/foundation/physics/atomic-structure/uses-of-nuclear-radiation.html', true),
  ('KS4', 10, 'foundation', 'triple', (select id from public.subjects where name = 'Physics'), 'AQA', 36, null, 'Atomic Structure', 'nuclear-fission', '/triple/foundation/physics/atomic-structure/nuclear-fission.html', true),
  ('KS4', 10, 'foundation', 'triple', (select id from public.subjects where name = 'Physics'), 'AQA', 37, null, 'Atomic Structure', 'nuclear-fusion', '/triple/foundation/physics/atomic-structure/nuclear-fusion.html', true);

-- ── Triple · Foundation · Physics · Year 11 — 27 lessons ─────────────────────
insert into public.scheme_of_work_entries
  (key_stage, year_group, tier, pathway, subject_id, exam_board, academic_week, half_term, topic, subtopic, notes, active)
values
  -- forces — Forces
  ('KS4', 11, 'foundation', 'triple', (select id from public.subjects where name = 'Physics'), 'AQA', 1, null, 'Forces', 'scalar-vector-quantities', '/triple/foundation/physics/forces/scalar-vector-quantities.html', true),
  ('KS4', 11, 'foundation', 'triple', (select id from public.subjects where name = 'Physics'), 'AQA', 2, null, 'Forces', 'contact-noncontact-forces', '/triple/foundation/physics/forces/contact-noncontact-forces.html', true),
  ('KS4', 11, 'foundation', 'triple', (select id from public.subjects where name = 'Physics'), 'AQA', 3, null, 'Forces', 'gravity', '/triple/foundation/physics/forces/gravity.html', true),
  ('KS4', 11, 'foundation', 'triple', (select id from public.subjects where name = 'Physics'), 'AQA', 4, null, 'Forces', 'resultant-forces', '/triple/foundation/physics/forces/resultant-forces.html', true),
  ('KS4', 11, 'foundation', 'triple', (select id from public.subjects where name = 'Physics'), 'AQA', 5, null, 'Forces', 'work-done-energy-transfer', '/triple/foundation/physics/forces/work-done-energy-transfer.html', true),
  ('KS4', 11, 'foundation', 'triple', (select id from public.subjects where name = 'Physics'), 'AQA', 6, null, 'Forces', 'forces-elasticity', '/triple/foundation/physics/forces/forces-elasticity.html', true),
  ('KS4', 11, 'foundation', 'triple', (select id from public.subjects where name = 'Physics'), 'AQA', 7, null, 'Forces', 'moments-levers-gears', '/triple/foundation/physics/forces/moments-levers-gears.html', true),
  ('KS4', 11, 'foundation', 'triple', (select id from public.subjects where name = 'Physics'), 'AQA', 8, null, 'Forces', 'pressure-in-a-fluid', '/triple/foundation/physics/forces/pressure-in-a-fluid.html', true),
  ('KS4', 11, 'foundation', 'triple', (select id from public.subjects where name = 'Physics'), 'AQA', 9, null, 'Forces', 'distance-speed-velocity', '/triple/foundation/physics/forces/distance-speed-velocity.html', true),
  ('KS4', 11, 'foundation', 'triple', (select id from public.subjects where name = 'Physics'), 'AQA', 10, null, 'Forces', 'distance-time-graphs', '/triple/foundation/physics/forces/distance-time-graphs.html', true),
  ('KS4', 11, 'foundation', 'triple', (select id from public.subjects where name = 'Physics'), 'AQA', 11, null, 'Forces', 'acceleration', '/triple/foundation/physics/forces/acceleration.html', true),
  ('KS4', 11, 'foundation', 'triple', (select id from public.subjects where name = 'Physics'), 'AQA', 12, null, 'Forces', 'newtons-laws', '/triple/foundation/physics/forces/newtons-laws.html', true),
  ('KS4', 11, 'foundation', 'triple', (select id from public.subjects where name = 'Physics'), 'AQA', 13, null, 'Forces', 'stopping-distance-braking', '/triple/foundation/physics/forces/stopping-distance-braking.html', true),
  -- waves — Waves
  ('KS4', 11, 'foundation', 'triple', (select id from public.subjects where name = 'Physics'), 'AQA', 14, null, 'Waves', 'transverse-longitudinal-waves', '/triple/foundation/physics/waves/transverse-longitudinal-waves.html', true),
  ('KS4', 11, 'foundation', 'triple', (select id from public.subjects where name = 'Physics'), 'AQA', 15, null, 'Waves', 'properties-of-waves', '/triple/foundation/physics/waves/properties-of-waves.html', true),
  ('KS4', 11, 'foundation', 'triple', (select id from public.subjects where name = 'Physics'), 'AQA', 16, null, 'Waves', 'types-of-em-waves', '/triple/foundation/physics/waves/types-of-em-waves.html', true),
  ('KS4', 11, 'foundation', 'triple', (select id from public.subjects where name = 'Physics'), 'AQA', 17, null, 'Waves', 'properties-em-waves-1', '/triple/foundation/physics/waves/properties-em-waves-1.html', true),
  ('KS4', 11, 'foundation', 'triple', (select id from public.subjects where name = 'Physics'), 'AQA', 18, null, 'Waves', 'properties-em-waves-2', '/triple/foundation/physics/waves/properties-em-waves-2.html', true),
  ('KS4', 11, 'foundation', 'triple', (select id from public.subjects where name = 'Physics'), 'AQA', 19, null, 'Waves', 'uses-em-waves', '/triple/foundation/physics/waves/uses-em-waves.html', true),
  ('KS4', 11, 'foundation', 'triple', (select id from public.subjects where name = 'Physics'), 'AQA', 20, null, 'Waves', 'lenses', '/triple/foundation/physics/waves/lenses.html', true),
  ('KS4', 11, 'foundation', 'triple', (select id from public.subjects where name = 'Physics'), 'AQA', 21, null, 'Waves', 'infrared-black-bodies', '/triple/foundation/physics/waves/infrared-black-bodies.html', true),
  -- magnetism — Magnetism and Electromagnetism
  ('KS4', 11, 'foundation', 'triple', (select id from public.subjects where name = 'Physics'), 'AQA', 22, null, 'Magnetism and Electromagnetism', 'poles-of-a-magnet', '/triple/foundation/physics/magnetism/poles-of-a-magnet.html', true),
  ('KS4', 11, 'foundation', 'triple', (select id from public.subjects where name = 'Physics'), 'AQA', 23, null, 'Magnetism and Electromagnetism', 'magnetic-fields', '/triple/foundation/physics/magnetism/magnetic-fields.html', true),
  ('KS4', 11, 'foundation', 'triple', (select id from public.subjects where name = 'Physics'), 'AQA', 24, null, 'Magnetism and Electromagnetism', 'electromagnetism', '/triple/foundation/physics/magnetism/electromagnetism.html', true),
  -- space — Space Physics
  ('KS4', 11, 'foundation', 'triple', (select id from public.subjects where name = 'Physics'), 'AQA', 25, null, 'Space Physics', 'solar-system-gravity', '/triple/foundation/physics/space/solar-system-gravity.html', true),
  ('KS4', 11, 'foundation', 'triple', (select id from public.subjects where name = 'Physics'), 'AQA', 26, null, 'Space Physics', 'stellar-evolution', '/triple/foundation/physics/space/stellar-evolution.html', true),
  ('KS4', 11, 'foundation', 'triple', (select id from public.subjects where name = 'Physics'), 'AQA', 27, null, 'Space Physics', 'red-shift-big-bang', '/triple/foundation/physics/space/red-shift-big-bang.html', true);

-- ── Triple · Higher · Biology · Year 10 — 47 lessons ─────────────────────
insert into public.scheme_of_work_entries
  (key_stage, year_group, tier, pathway, subject_id, exam_board, academic_week, half_term, topic, subtopic, notes, active)
values
  -- cell-biology — Cell Biology
  ('KS4', 10, 'higher', 'triple', (select id from public.subjects where name = 'Biology'), 'AQA', 1, null, 'Cell Biology', 'eukaryotes-prokaryotes', '/triple/higher/biology/cell-biology/eukaryotes-prokaryotes.html', true),
  ('KS4', 10, 'higher', 'triple', (select id from public.subjects where name = 'Biology'), 'AQA', 2, null, 'Cell Biology', 'animal-plant-cells', '/triple/higher/biology/cell-biology/animal-plant-cells.html', true),
  ('KS4', 10, 'higher', 'triple', (select id from public.subjects where name = 'Biology'), 'AQA', 3, null, 'Cell Biology', 'cell-specialisation', '/triple/higher/biology/cell-biology/cell-specialisation.html', true),
  ('KS4', 10, 'higher', 'triple', (select id from public.subjects where name = 'Biology'), 'AQA', 4, null, 'Cell Biology', 'microscopy', '/triple/higher/biology/cell-biology/microscopy.html', true),
  ('KS4', 10, 'higher', 'triple', (select id from public.subjects where name = 'Biology'), 'AQA', 5, null, 'Cell Biology', 'chromosomes-mitosis', '/triple/higher/biology/cell-biology/chromosomes-mitosis.html', true),
  ('KS4', 10, 'higher', 'triple', (select id from public.subjects where name = 'Biology'), 'AQA', 6, null, 'Cell Biology', 'stem-cells', '/triple/higher/biology/cell-biology/stem-cells.html', true),
  ('KS4', 10, 'higher', 'triple', (select id from public.subjects where name = 'Biology'), 'AQA', 7, null, 'Cell Biology', 'transport-in-cells', '/triple/higher/biology/cell-biology/transport-in-cells.html', true),
  ('KS4', 10, 'higher', 'triple', (select id from public.subjects where name = 'Biology'), 'AQA', 8, null, 'Cell Biology', 'culturing-microorganisms', '/triple/higher/biology/cell-biology/culturing-microorganisms.html', true),
  -- organisation — Organisation
  ('KS4', 10, 'higher', 'triple', (select id from public.subjects where name = 'Biology'), 'AQA', 9, null, 'Organisation', 'principles-of-organisation', '/triple/higher/biology/organisation/principles-of-organisation.html', true),
  ('KS4', 10, 'higher', 'triple', (select id from public.subjects where name = 'Biology'), 'AQA', 10, null, 'Organisation', 'digestive-system', '/triple/higher/biology/organisation/digestive-system.html', true),
  ('KS4', 10, 'higher', 'triple', (select id from public.subjects where name = 'Biology'), 'AQA', 11, null, 'Organisation', 'enzymes', '/triple/higher/biology/organisation/enzymes.html', true),
  ('KS4', 10, 'higher', 'triple', (select id from public.subjects where name = 'Biology'), 'AQA', 12, null, 'Organisation', 'heart-blood-vessels', '/triple/higher/biology/organisation/heart-blood-vessels.html', true),
  ('KS4', 10, 'higher', 'triple', (select id from public.subjects where name = 'Biology'), 'AQA', 13, null, 'Organisation', 'blood', '/triple/higher/biology/organisation/blood.html', true),
  ('KS4', 10, 'higher', 'triple', (select id from public.subjects where name = 'Biology'), 'AQA', 14, null, 'Organisation', 'coronary-heart-disease', '/triple/higher/biology/organisation/coronary-heart-disease.html', true),
  ('KS4', 10, 'higher', 'triple', (select id from public.subjects where name = 'Biology'), 'AQA', 15, null, 'Organisation', 'health-disease', '/triple/higher/biology/organisation/health-disease.html', true),
  ('KS4', 10, 'higher', 'triple', (select id from public.subjects where name = 'Biology'), 'AQA', 16, null, 'Organisation', 'cancer', '/triple/higher/biology/organisation/cancer.html', true),
  ('KS4', 10, 'higher', 'triple', (select id from public.subjects where name = 'Biology'), 'AQA', 17, null, 'Organisation', 'plant-tissues', '/triple/higher/biology/organisation/plant-tissues.html', true),
  ('KS4', 10, 'higher', 'triple', (select id from public.subjects where name = 'Biology'), 'AQA', 18, null, 'Organisation', 'transpiration', '/triple/higher/biology/organisation/transpiration.html', true),
  ('KS4', 10, 'higher', 'triple', (select id from public.subjects where name = 'Biology'), 'AQA', 19, null, 'Organisation', 'translocation', '/triple/higher/biology/organisation/translocation.html', true),
  -- infection-response — Infection and Response
  ('KS4', 10, 'higher', 'triple', (select id from public.subjects where name = 'Biology'), 'AQA', 20, null, 'Infection and Response', 'communicable-diseases-defence', '/triple/higher/biology/infection-response/communicable-diseases-defence.html', true),
  ('KS4', 10, 'higher', 'triple', (select id from public.subjects where name = 'Biology'), 'AQA', 21, null, 'Infection and Response', 'viral-diseases', '/triple/higher/biology/infection-response/viral-diseases.html', true),
  ('KS4', 10, 'higher', 'triple', (select id from public.subjects where name = 'Biology'), 'AQA', 22, null, 'Infection and Response', 'bacterial-diseases', '/triple/higher/biology/infection-response/bacterial-diseases.html', true),
  ('KS4', 10, 'higher', 'triple', (select id from public.subjects where name = 'Biology'), 'AQA', 23, null, 'Infection and Response', 'fungal-protist-diseases', '/triple/higher/biology/infection-response/fungal-protist-diseases.html', true),
  ('KS4', 10, 'higher', 'triple', (select id from public.subjects where name = 'Biology'), 'AQA', 24, null, 'Infection and Response', 'vaccination', '/triple/higher/biology/infection-response/vaccination.html', true),
  ('KS4', 10, 'higher', 'triple', (select id from public.subjects where name = 'Biology'), 'AQA', 25, null, 'Infection and Response', 'antibiotics-painkillers', '/triple/higher/biology/infection-response/antibiotics-painkillers.html', true),
  ('KS4', 10, 'higher', 'triple', (select id from public.subjects where name = 'Biology'), 'AQA', 26, null, 'Infection and Response', 'drug-discovery-development', '/triple/higher/biology/infection-response/drug-discovery-development.html', true),
  ('KS4', 10, 'higher', 'triple', (select id from public.subjects where name = 'Biology'), 'AQA', 27, null, 'Infection and Response', 'plant-disease-detection-defence', '/triple/higher/biology/infection-response/plant-disease-detection-defence.html', true),
  ('KS4', 10, 'higher', 'triple', (select id from public.subjects where name = 'Biology'), 'AQA', 28, null, 'Infection and Response', 'monoclonal-antibodies', '/triple/higher/biology/infection-response/monoclonal-antibodies.html', true),
  -- bioenergetics — Bioenergetics
  ('KS4', 10, 'higher', 'triple', (select id from public.subjects where name = 'Biology'), 'AQA', 29, null, 'Bioenergetics', 'photosynthesis', '/triple/higher/biology/bioenergetics/photosynthesis.html', true),
  ('KS4', 10, 'higher', 'triple', (select id from public.subjects where name = 'Biology'), 'AQA', 30, null, 'Bioenergetics', 'rate-of-photosynthesis', '/triple/higher/biology/bioenergetics/rate-of-photosynthesis.html', true),
  ('KS4', 10, 'higher', 'triple', (select id from public.subjects where name = 'Biology'), 'AQA', 31, null, 'Bioenergetics', 'uses-of-glucose', '/triple/higher/biology/bioenergetics/uses-of-glucose.html', true),
  ('KS4', 10, 'higher', 'triple', (select id from public.subjects where name = 'Biology'), 'AQA', 32, null, 'Bioenergetics', 'aerobic-respiration', '/triple/higher/biology/bioenergetics/aerobic-respiration.html', true),
  ('KS4', 10, 'higher', 'triple', (select id from public.subjects where name = 'Biology'), 'AQA', 33, null, 'Bioenergetics', 'anaerobic-respiration', '/triple/higher/biology/bioenergetics/anaerobic-respiration.html', true),
  ('KS4', 10, 'higher', 'triple', (select id from public.subjects where name = 'Biology'), 'AQA', 34, null, 'Bioenergetics', 'response-to-exercise', '/triple/higher/biology/bioenergetics/response-to-exercise.html', true),
  ('KS4', 10, 'higher', 'triple', (select id from public.subjects where name = 'Biology'), 'AQA', 35, null, 'Bioenergetics', 'metabolism', '/triple/higher/biology/bioenergetics/metabolism.html', true),
  -- homeostasis — Homeostasis and Response
  ('KS4', 10, 'higher', 'triple', (select id from public.subjects where name = 'Biology'), 'AQA', 36, null, 'Homeostasis and Response', 'homeostasis', '/triple/higher/biology/homeostasis/homeostasis.html', true),
  ('KS4', 10, 'higher', 'triple', (select id from public.subjects where name = 'Biology'), 'AQA', 37, null, 'Homeostasis and Response', 'nervous-system', '/triple/higher/biology/homeostasis/nervous-system.html', true),
  ('KS4', 10, 'higher', 'triple', (select id from public.subjects where name = 'Biology'), 'AQA', 38, null, 'Homeostasis and Response', 'reflex-actions', '/triple/higher/biology/homeostasis/reflex-actions.html', true),
  ('KS4', 10, 'higher', 'triple', (select id from public.subjects where name = 'Biology'), 'AQA', 39, null, 'Homeostasis and Response', 'thermoregulation', '/triple/higher/biology/homeostasis/thermoregulation.html', true),
  ('KS4', 10, 'higher', 'triple', (select id from public.subjects where name = 'Biology'), 'AQA', 40, null, 'Homeostasis and Response', 'endocrine-system', '/triple/higher/biology/homeostasis/endocrine-system.html', true),
  ('KS4', 10, 'higher', 'triple', (select id from public.subjects where name = 'Biology'), 'AQA', 41, null, 'Homeostasis and Response', 'blood-glucose-diabetes', '/triple/higher/biology/homeostasis/blood-glucose-diabetes.html', true),
  ('KS4', 10, 'higher', 'triple', (select id from public.subjects where name = 'Biology'), 'AQA', 42, null, 'Homeostasis and Response', 'human-reproduction-hormones', '/triple/higher/biology/homeostasis/human-reproduction-hormones.html', true),
  ('KS4', 10, 'higher', 'triple', (select id from public.subjects where name = 'Biology'), 'AQA', 43, null, 'Homeostasis and Response', 'contraception-fertility', '/triple/higher/biology/homeostasis/contraception-fertility.html', true),
  ('KS4', 10, 'higher', 'triple', (select id from public.subjects where name = 'Biology'), 'AQA', 44, null, 'Homeostasis and Response', 'reaction-time', '/triple/higher/biology/homeostasis/reaction-time.html', true),
  ('KS4', 10, 'higher', 'triple', (select id from public.subjects where name = 'Biology'), 'AQA', 45, null, 'Homeostasis and Response', 'the-brain', '/triple/higher/biology/homeostasis/the-brain.html', true),
  ('KS4', 10, 'higher', 'triple', (select id from public.subjects where name = 'Biology'), 'AQA', 46, null, 'Homeostasis and Response', 'the-eye', '/triple/higher/biology/homeostasis/the-eye.html', true),
  ('KS4', 10, 'higher', 'triple', (select id from public.subjects where name = 'Biology'), 'AQA', 47, null, 'Homeostasis and Response', 'defects-of-the-eye', '/triple/higher/biology/homeostasis/defects-of-the-eye.html', true);

-- ── Triple · Higher · Biology · Year 11 — 42 lessons ─────────────────────
insert into public.scheme_of_work_entries
  (key_stage, year_group, tier, pathway, subject_id, exam_board, academic_week, half_term, topic, subtopic, notes, active)
values
  -- inheritance — Inheritance, Variation and Evolution
  ('KS4', 11, 'higher', 'triple', (select id from public.subjects where name = 'Biology'), 'AQA', 1, null, 'Inheritance, Variation and Evolution', 'sexual-asexual-reproduction', '/triple/higher/biology/inheritance/sexual-asexual-reproduction.html', true),
  ('KS4', 11, 'higher', 'triple', (select id from public.subjects where name = 'Biology'), 'AQA', 2, null, 'Inheritance, Variation and Evolution', 'meiosis', '/triple/higher/biology/inheritance/meiosis.html', true),
  ('KS4', 11, 'higher', 'triple', (select id from public.subjects where name = 'Biology'), 'AQA', 3, null, 'Inheritance, Variation and Evolution', 'advantages-sexual-asexual', '/triple/higher/biology/inheritance/advantages-sexual-asexual.html', true),
  ('KS4', 11, 'higher', 'triple', (select id from public.subjects where name = 'Biology'), 'AQA', 4, null, 'Inheritance, Variation and Evolution', 'dna-genome', '/triple/higher/biology/inheritance/dna-genome.html', true),
  ('KS4', 11, 'higher', 'triple', (select id from public.subjects where name = 'Biology'), 'AQA', 5, null, 'Inheritance, Variation and Evolution', 'dna-structure', '/triple/higher/biology/inheritance/dna-structure.html', true),
  ('KS4', 11, 'higher', 'triple', (select id from public.subjects where name = 'Biology'), 'AQA', 6, null, 'Inheritance, Variation and Evolution', 'genetic-inheritance', '/triple/higher/biology/inheritance/genetic-inheritance.html', true),
  ('KS4', 11, 'higher', 'triple', (select id from public.subjects where name = 'Biology'), 'AQA', 7, null, 'Inheritance, Variation and Evolution', 'inherited-disorders', '/triple/higher/biology/inheritance/inherited-disorders.html', true),
  ('KS4', 11, 'higher', 'triple', (select id from public.subjects where name = 'Biology'), 'AQA', 8, null, 'Inheritance, Variation and Evolution', 'sex-determination', '/triple/higher/biology/inheritance/sex-determination.html', true),
  ('KS4', 11, 'higher', 'triple', (select id from public.subjects where name = 'Biology'), 'AQA', 9, null, 'Inheritance, Variation and Evolution', 'variation', '/triple/higher/biology/inheritance/variation.html', true),
  ('KS4', 11, 'higher', 'triple', (select id from public.subjects where name = 'Biology'), 'AQA', 10, null, 'Inheritance, Variation and Evolution', 'evolution-natural-selection', '/triple/higher/biology/inheritance/evolution-natural-selection.html', true),
  ('KS4', 11, 'higher', 'triple', (select id from public.subjects where name = 'Biology'), 'AQA', 11, null, 'Inheritance, Variation and Evolution', 'theory-of-evolution', '/triple/higher/biology/inheritance/theory-of-evolution.html', true),
  ('KS4', 11, 'higher', 'triple', (select id from public.subjects where name = 'Biology'), 'AQA', 12, null, 'Inheritance, Variation and Evolution', 'selective-breeding', '/triple/higher/biology/inheritance/selective-breeding.html', true),
  ('KS4', 11, 'higher', 'triple', (select id from public.subjects where name = 'Biology'), 'AQA', 13, null, 'Inheritance, Variation and Evolution', 'genetic-engineering', '/triple/higher/biology/inheritance/genetic-engineering.html', true),
  ('KS4', 11, 'higher', 'triple', (select id from public.subjects where name = 'Biology'), 'AQA', 14, null, 'Inheritance, Variation and Evolution', 'cloning', '/triple/higher/biology/inheritance/cloning.html', true),
  ('KS4', 11, 'higher', 'triple', (select id from public.subjects where name = 'Biology'), 'AQA', 15, null, 'Inheritance, Variation and Evolution', 'evidence-for-evolution', '/triple/higher/biology/inheritance/evidence-for-evolution.html', true),
  ('KS4', 11, 'higher', 'triple', (select id from public.subjects where name = 'Biology'), 'AQA', 16, null, 'Inheritance, Variation and Evolution', 'understanding-genetics', '/triple/higher/biology/inheritance/understanding-genetics.html', true),
  ('KS4', 11, 'higher', 'triple', (select id from public.subjects where name = 'Biology'), 'AQA', 17, null, 'Inheritance, Variation and Evolution', 'fossils-extinction', '/triple/higher/biology/inheritance/fossils-extinction.html', true),
  ('KS4', 11, 'higher', 'triple', (select id from public.subjects where name = 'Biology'), 'AQA', 18, null, 'Inheritance, Variation and Evolution', 'resistant-bacteria', '/triple/higher/biology/inheritance/resistant-bacteria.html', true),
  ('KS4', 11, 'higher', 'triple', (select id from public.subjects where name = 'Biology'), 'AQA', 19, null, 'Inheritance, Variation and Evolution', 'classification-living-organisms', '/triple/higher/biology/inheritance/classification-living-organisms.html', true),
  -- ecology — Ecology
  ('KS4', 11, 'higher', 'triple', (select id from public.subjects where name = 'Biology'), 'AQA', 20, null, 'Ecology', 'ecosystems', '/triple/higher/biology/ecology/ecosystems.html', true),
  ('KS4', 11, 'higher', 'triple', (select id from public.subjects where name = 'Biology'), 'AQA', 21, null, 'Ecology', 'abiotic-biotic-factors', '/triple/higher/biology/ecology/abiotic-biotic-factors.html', true),
  ('KS4', 11, 'higher', 'triple', (select id from public.subjects where name = 'Biology'), 'AQA', 22, null, 'Ecology', 'adaptations', '/triple/higher/biology/ecology/adaptations.html', true),
  ('KS4', 11, 'higher', 'triple', (select id from public.subjects where name = 'Biology'), 'AQA', 23, null, 'Ecology', 'food-chains-webs', '/triple/higher/biology/ecology/food-chains-webs.html', true),
  ('KS4', 11, 'higher', 'triple', (select id from public.subjects where name = 'Biology'), 'AQA', 24, null, 'Ecology', 'population-competition', '/triple/higher/biology/ecology/population-competition.html', true),
  ('KS4', 11, 'higher', 'triple', (select id from public.subjects where name = 'Biology'), 'AQA', 25, null, 'Ecology', 'biodiversity', '/triple/higher/biology/ecology/biodiversity.html', true),
  ('KS4', 11, 'higher', 'triple', (select id from public.subjects where name = 'Biology'), 'AQA', 26, null, 'Ecology', 'waste-management', '/triple/higher/biology/ecology/waste-management.html', true),
  ('KS4', 11, 'higher', 'triple', (select id from public.subjects where name = 'Biology'), 'AQA', 27, null, 'Ecology', 'land-use', '/triple/higher/biology/ecology/land-use.html', true),
  ('KS4', 11, 'higher', 'triple', (select id from public.subjects where name = 'Biology'), 'AQA', 28, null, 'Ecology', 'deforestation', '/triple/higher/biology/ecology/deforestation.html', true),
  ('KS4', 11, 'higher', 'triple', (select id from public.subjects where name = 'Biology'), 'AQA', 29, null, 'Ecology', 'global-warming', '/triple/higher/biology/ecology/global-warming.html', true),
  ('KS4', 11, 'higher', 'triple', (select id from public.subjects where name = 'Biology'), 'AQA', 30, null, 'Ecology', 'maintaining-biodiversity', '/triple/higher/biology/ecology/maintaining-biodiversity.html', true),
  ('KS4', 11, 'higher', 'triple', (select id from public.subjects where name = 'Biology'), 'AQA', 31, null, 'Ecology', 'carbon-cycle', '/triple/higher/biology/ecology/carbon-cycle.html', true),
  ('KS4', 11, 'higher', 'triple', (select id from public.subjects where name = 'Biology'), 'AQA', 32, null, 'Ecology', 'water-cycle', '/triple/higher/biology/ecology/water-cycle.html', true),
  ('KS4', 11, 'higher', 'triple', (select id from public.subjects where name = 'Biology'), 'AQA', 33, null, 'Ecology', 'decomposition', '/triple/higher/biology/ecology/decomposition.html', true),
  ('KS4', 11, 'higher', 'triple', (select id from public.subjects where name = 'Biology'), 'AQA', 34, null, 'Ecology', 'trophic-levels', '/triple/higher/biology/ecology/trophic-levels.html', true),
  ('KS4', 11, 'higher', 'triple', (select id from public.subjects where name = 'Biology'), 'AQA', 35, null, 'Ecology', 'pyramids-of-biomass', '/triple/higher/biology/ecology/pyramids-of-biomass.html', true),
  ('KS4', 11, 'higher', 'triple', (select id from public.subjects where name = 'Biology'), 'AQA', 36, null, 'Ecology', 'transfer-of-biomass', '/triple/higher/biology/ecology/transfer-of-biomass.html', true),
  ('KS4', 11, 'higher', 'triple', (select id from public.subjects where name = 'Biology'), 'AQA', 37, null, 'Ecology', 'sampling-techniques', '/triple/higher/biology/ecology/sampling-techniques.html', true),
  ('KS4', 11, 'higher', 'triple', (select id from public.subjects where name = 'Biology'), 'AQA', 38, null, 'Ecology', 'environmental-change', '/triple/higher/biology/ecology/environmental-change.html', true),
  ('KS4', 11, 'higher', 'triple', (select id from public.subjects where name = 'Biology'), 'AQA', 39, null, 'Ecology', 'factors-affecting-food-security', '/triple/higher/biology/ecology/factors-affecting-food-security.html', true),
  ('KS4', 11, 'higher', 'triple', (select id from public.subjects where name = 'Biology'), 'AQA', 40, null, 'Ecology', 'farming-techniques', '/triple/higher/biology/ecology/farming-techniques.html', true),
  ('KS4', 11, 'higher', 'triple', (select id from public.subjects where name = 'Biology'), 'AQA', 41, null, 'Ecology', 'sustainable-fisheries', '/triple/higher/biology/ecology/sustainable-fisheries.html', true),
  ('KS4', 11, 'higher', 'triple', (select id from public.subjects where name = 'Biology'), 'AQA', 42, null, 'Ecology', 'role-of-biotechnology', '/triple/higher/biology/ecology/role-of-biotechnology.html', true);

-- ── Triple · Higher · Chemistry · Year 10 — 48 lessons ─────────────────────
insert into public.scheme_of_work_entries
  (key_stage, year_group, tier, pathway, subject_id, exam_board, academic_week, half_term, topic, subtopic, notes, active)
values
  -- atomic-structure — Atomic Structure and the Periodic Table
  ('KS4', 10, 'higher', 'triple', (select id from public.subjects where name = 'Chemistry'), 'AQA', 1, null, 'Atomic Structure and the Periodic Table', 'atoms-elements-compounds', '/triple/higher/chemistry/atomic-structure/atoms-elements-compounds.html', true),
  ('KS4', 10, 'higher', 'triple', (select id from public.subjects where name = 'Chemistry'), 'AQA', 2, null, 'Atomic Structure and the Periodic Table', 'mixtures', '/triple/higher/chemistry/atomic-structure/mixtures.html', true),
  ('KS4', 10, 'higher', 'triple', (select id from public.subjects where name = 'Chemistry'), 'AQA', 3, null, 'Atomic Structure and the Periodic Table', 'model-of-the-atom', '/triple/higher/chemistry/atomic-structure/model-of-the-atom.html', true),
  ('KS4', 10, 'higher', 'triple', (select id from public.subjects where name = 'Chemistry'), 'AQA', 4, null, 'Atomic Structure and the Periodic Table', 'subatomic-particles', '/triple/higher/chemistry/atomic-structure/subatomic-particles.html', true),
  ('KS4', 10, 'higher', 'triple', (select id from public.subjects where name = 'Chemistry'), 'AQA', 5, null, 'Atomic Structure and the Periodic Table', 'relative-atomic-mass', '/triple/higher/chemistry/atomic-structure/relative-atomic-mass.html', true),
  ('KS4', 10, 'higher', 'triple', (select id from public.subjects where name = 'Chemistry'), 'AQA', 6, null, 'Atomic Structure and the Periodic Table', 'electronic-structure', '/triple/higher/chemistry/atomic-structure/electronic-structure.html', true),
  ('KS4', 10, 'higher', 'triple', (select id from public.subjects where name = 'Chemistry'), 'AQA', 7, null, 'Atomic Structure and the Periodic Table', 'periodic-table', '/triple/higher/chemistry/atomic-structure/periodic-table.html', true),
  ('KS4', 10, 'higher', 'triple', (select id from public.subjects where name = 'Chemistry'), 'AQA', 8, null, 'Atomic Structure and the Periodic Table', 'development-periodic-table', '/triple/higher/chemistry/atomic-structure/development-periodic-table.html', true),
  ('KS4', 10, 'higher', 'triple', (select id from public.subjects where name = 'Chemistry'), 'AQA', 9, null, 'Atomic Structure and the Periodic Table', 'metals-non-metals', '/triple/higher/chemistry/atomic-structure/metals-non-metals.html', true),
  ('KS4', 10, 'higher', 'triple', (select id from public.subjects where name = 'Chemistry'), 'AQA', 10, null, 'Atomic Structure and the Periodic Table', 'group-0', '/triple/higher/chemistry/atomic-structure/group-0.html', true),
  ('KS4', 10, 'higher', 'triple', (select id from public.subjects where name = 'Chemistry'), 'AQA', 11, null, 'Atomic Structure and the Periodic Table', 'group-1', '/triple/higher/chemistry/atomic-structure/group-1.html', true),
  ('KS4', 10, 'higher', 'triple', (select id from public.subjects where name = 'Chemistry'), 'AQA', 12, null, 'Atomic Structure and the Periodic Table', 'group-7', '/triple/higher/chemistry/atomic-structure/group-7.html', true),
  ('KS4', 10, 'higher', 'triple', (select id from public.subjects where name = 'Chemistry'), 'AQA', 13, null, 'Atomic Structure and the Periodic Table', 'transition-metals', '/triple/higher/chemistry/atomic-structure/transition-metals.html', true),
  -- bonding — Bonding, Structure and Properties of Matter
  ('KS4', 10, 'higher', 'triple', (select id from public.subjects where name = 'Chemistry'), 'AQA', 14, null, 'Bonding, Structure and Properties of Matter', 'chemical-bonds', '/triple/higher/chemistry/bonding/chemical-bonds.html', true),
  ('KS4', 10, 'higher', 'triple', (select id from public.subjects where name = 'Chemistry'), 'AQA', 15, null, 'Bonding, Structure and Properties of Matter', 'ionic-bonding', '/triple/higher/chemistry/bonding/ionic-bonding.html', true),
  ('KS4', 10, 'higher', 'triple', (select id from public.subjects where name = 'Chemistry'), 'AQA', 16, null, 'Bonding, Structure and Properties of Matter', 'ionic-compounds', '/triple/higher/chemistry/bonding/ionic-compounds.html', true),
  ('KS4', 10, 'higher', 'triple', (select id from public.subjects where name = 'Chemistry'), 'AQA', 17, null, 'Bonding, Structure and Properties of Matter', 'covalent-bonding', '/triple/higher/chemistry/bonding/covalent-bonding.html', true),
  ('KS4', 10, 'higher', 'triple', (select id from public.subjects where name = 'Chemistry'), 'AQA', 18, null, 'Bonding, Structure and Properties of Matter', 'metallic-bonding', '/triple/higher/chemistry/bonding/metallic-bonding.html', true),
  ('KS4', 10, 'higher', 'triple', (select id from public.subjects where name = 'Chemistry'), 'AQA', 19, null, 'Bonding, Structure and Properties of Matter', 'states-of-matter', '/triple/higher/chemistry/bonding/states-of-matter.html', true),
  ('KS4', 10, 'higher', 'triple', (select id from public.subjects where name = 'Chemistry'), 'AQA', 20, null, 'Bonding, Structure and Properties of Matter', 'properties-ionic-compounds', '/triple/higher/chemistry/bonding/properties-ionic-compounds.html', true),
  ('KS4', 10, 'higher', 'triple', (select id from public.subjects where name = 'Chemistry'), 'AQA', 21, null, 'Bonding, Structure and Properties of Matter', 'properties-small-molecules', '/triple/higher/chemistry/bonding/properties-small-molecules.html', true),
  ('KS4', 10, 'higher', 'triple', (select id from public.subjects where name = 'Chemistry'), 'AQA', 22, null, 'Bonding, Structure and Properties of Matter', 'polymers', '/triple/higher/chemistry/bonding/polymers.html', true),
  ('KS4', 10, 'higher', 'triple', (select id from public.subjects where name = 'Chemistry'), 'AQA', 23, null, 'Bonding, Structure and Properties of Matter', 'giant-covalent-structures', '/triple/higher/chemistry/bonding/giant-covalent-structures.html', true),
  ('KS4', 10, 'higher', 'triple', (select id from public.subjects where name = 'Chemistry'), 'AQA', 24, null, 'Bonding, Structure and Properties of Matter', 'metals-alloys', '/triple/higher/chemistry/bonding/metals-alloys.html', true),
  ('KS4', 10, 'higher', 'triple', (select id from public.subjects where name = 'Chemistry'), 'AQA', 25, null, 'Bonding, Structure and Properties of Matter', 'nanoparticles', '/triple/higher/chemistry/bonding/nanoparticles.html', true),
  -- quantitative — Quantitative Chemistry
  ('KS4', 10, 'higher', 'triple', (select id from public.subjects where name = 'Chemistry'), 'AQA', 26, null, 'Quantitative Chemistry', 'conservation-of-mass', '/triple/higher/chemistry/quantitative/conservation-of-mass.html', true),
  ('KS4', 10, 'higher', 'triple', (select id from public.subjects where name = 'Chemistry'), 'AQA', 27, null, 'Quantitative Chemistry', 'relative-formula-mass', '/triple/higher/chemistry/quantitative/relative-formula-mass.html', true),
  ('KS4', 10, 'higher', 'triple', (select id from public.subjects where name = 'Chemistry'), 'AQA', 28, null, 'Quantitative Chemistry', 'mass-changes-reactions', '/triple/higher/chemistry/quantitative/mass-changes-reactions.html', true),
  ('KS4', 10, 'higher', 'triple', (select id from public.subjects where name = 'Chemistry'), 'AQA', 29, null, 'Quantitative Chemistry', 'chemical-measurements', '/triple/higher/chemistry/quantitative/chemical-measurements.html', true),
  ('KS4', 10, 'higher', 'triple', (select id from public.subjects where name = 'Chemistry'), 'AQA', 30, null, 'Quantitative Chemistry', 'percentage-yield', '/triple/higher/chemistry/quantitative/percentage-yield.html', true),
  ('KS4', 10, 'higher', 'triple', (select id from public.subjects where name = 'Chemistry'), 'AQA', 31, null, 'Quantitative Chemistry', 'atom-economy', '/triple/higher/chemistry/quantitative/atom-economy.html', true),
  ('KS4', 10, 'higher', 'triple', (select id from public.subjects where name = 'Chemistry'), 'AQA', 32, null, 'Quantitative Chemistry', 'concentration-of-solutions', '/triple/higher/chemistry/quantitative/concentration-of-solutions.html', true),
  ('KS4', 10, 'higher', 'triple', (select id from public.subjects where name = 'Chemistry'), 'AQA', 33, null, 'Quantitative Chemistry', 'moles', '/triple/higher/chemistry/quantitative/moles.html', true),
  ('KS4', 10, 'higher', 'triple', (select id from public.subjects where name = 'Chemistry'), 'AQA', 34, null, 'Quantitative Chemistry', 'amounts-in-equations', '/triple/higher/chemistry/quantitative/amounts-in-equations.html', true),
  ('KS4', 10, 'higher', 'triple', (select id from public.subjects where name = 'Chemistry'), 'AQA', 35, null, 'Quantitative Chemistry', 'using-moles-calculations', '/triple/higher/chemistry/quantitative/using-moles-calculations.html', true),
  -- chemical-changes — Chemical Changes
  ('KS4', 10, 'higher', 'triple', (select id from public.subjects where name = 'Chemistry'), 'AQA', 36, null, 'Chemical Changes', 'reactivity-series', '/triple/higher/chemistry/chemical-changes/reactivity-series.html', true),
  ('KS4', 10, 'higher', 'triple', (select id from public.subjects where name = 'Chemistry'), 'AQA', 37, null, 'Chemical Changes', 'extraction-of-metals', '/triple/higher/chemistry/chemical-changes/extraction-of-metals.html', true),
  ('KS4', 10, 'higher', 'triple', (select id from public.subjects where name = 'Chemistry'), 'AQA', 38, null, 'Chemical Changes', 'oxidation-reduction', '/triple/higher/chemistry/chemical-changes/oxidation-reduction.html', true),
  ('KS4', 10, 'higher', 'triple', (select id from public.subjects where name = 'Chemistry'), 'AQA', 39, null, 'Chemical Changes', 'reactions-of-acids', '/triple/higher/chemistry/chemical-changes/reactions-of-acids.html', true),
  ('KS4', 10, 'higher', 'triple', (select id from public.subjects where name = 'Chemistry'), 'AQA', 40, null, 'Chemical Changes', 'salts-neutralisation', '/triple/higher/chemistry/chemical-changes/salts-neutralisation.html', true),
  ('KS4', 10, 'higher', 'triple', (select id from public.subjects where name = 'Chemistry'), 'AQA', 41, null, 'Chemical Changes', 'ph-scale', '/triple/higher/chemistry/chemical-changes/ph-scale.html', true),
  ('KS4', 10, 'higher', 'triple', (select id from public.subjects where name = 'Chemistry'), 'AQA', 42, null, 'Chemical Changes', 'titrations', '/triple/higher/chemistry/chemical-changes/titrations.html', true),
  ('KS4', 10, 'higher', 'triple', (select id from public.subjects where name = 'Chemistry'), 'AQA', 43, null, 'Chemical Changes', 'electrolysis-principles', '/triple/higher/chemistry/chemical-changes/electrolysis-principles.html', true),
  ('KS4', 10, 'higher', 'triple', (select id from public.subjects where name = 'Chemistry'), 'AQA', 44, null, 'Chemical Changes', 'electrolysis-molten', '/triple/higher/chemistry/chemical-changes/electrolysis-molten.html', true),
  ('KS4', 10, 'higher', 'triple', (select id from public.subjects where name = 'Chemistry'), 'AQA', 45, null, 'Chemical Changes', 'electrolysis-extraction', '/triple/higher/chemistry/chemical-changes/electrolysis-extraction.html', true),
  ('KS4', 10, 'higher', 'triple', (select id from public.subjects where name = 'Chemistry'), 'AQA', 46, null, 'Chemical Changes', 'electrolysis-aqueous', '/triple/higher/chemistry/chemical-changes/electrolysis-aqueous.html', true),
  ('KS4', 10, 'higher', 'triple', (select id from public.subjects where name = 'Chemistry'), 'AQA', 47, null, 'Chemical Changes', 'strong-weak-acids', '/triple/higher/chemistry/chemical-changes/strong-weak-acids.html', true),
  ('KS4', 10, 'higher', 'triple', (select id from public.subjects where name = 'Chemistry'), 'AQA', 48, null, 'Chemical Changes', 'half-equations', '/triple/higher/chemistry/chemical-changes/half-equations.html', true);

-- ── Triple · Higher · Chemistry · Year 11 — 45 lessons ─────────────────────
insert into public.scheme_of_work_entries
  (key_stage, year_group, tier, pathway, subject_id, exam_board, academic_week, half_term, topic, subtopic, notes, active)
values
  -- energy-changes — Energy Changes
  ('KS4', 11, 'higher', 'triple', (select id from public.subjects where name = 'Chemistry'), 'AQA', 1, null, 'Energy Changes', 'exothermic-endothermic', '/triple/higher/chemistry/energy-changes/exothermic-endothermic.html', true),
  ('KS4', 11, 'higher', 'triple', (select id from public.subjects where name = 'Chemistry'), 'AQA', 2, null, 'Energy Changes', 'reaction-profiles', '/triple/higher/chemistry/energy-changes/reaction-profiles.html', true),
  ('KS4', 11, 'higher', 'triple', (select id from public.subjects where name = 'Chemistry'), 'AQA', 3, null, 'Energy Changes', 'cells-and-batteries', '/triple/higher/chemistry/energy-changes/cells-and-batteries.html', true),
  ('KS4', 11, 'higher', 'triple', (select id from public.subjects where name = 'Chemistry'), 'AQA', 4, null, 'Energy Changes', 'fuel-cells', '/triple/higher/chemistry/energy-changes/fuel-cells.html', true),
  ('KS4', 11, 'higher', 'triple', (select id from public.subjects where name = 'Chemistry'), 'AQA', 5, null, 'Energy Changes', 'bond-energy-calculations', '/triple/higher/chemistry/energy-changes/bond-energy-calculations.html', true),
  -- rates-equilibrium — Rate and Extent of Chemical Change
  ('KS4', 11, 'higher', 'triple', (select id from public.subjects where name = 'Chemistry'), 'AQA', 6, null, 'Rate and Extent of Chemical Change', 'calculating-rates', '/triple/higher/chemistry/rates-equilibrium/calculating-rates.html', true),
  ('KS4', 11, 'higher', 'triple', (select id from public.subjects where name = 'Chemistry'), 'AQA', 7, null, 'Rate and Extent of Chemical Change', 'factors-affecting-rate', '/triple/higher/chemistry/rates-equilibrium/factors-affecting-rate.html', true),
  ('KS4', 11, 'higher', 'triple', (select id from public.subjects where name = 'Chemistry'), 'AQA', 8, null, 'Rate and Extent of Chemical Change', 'collision-theory', '/triple/higher/chemistry/rates-equilibrium/collision-theory.html', true),
  ('KS4', 11, 'higher', 'triple', (select id from public.subjects where name = 'Chemistry'), 'AQA', 9, null, 'Rate and Extent of Chemical Change', 'catalysts', '/triple/higher/chemistry/rates-equilibrium/catalysts.html', true),
  ('KS4', 11, 'higher', 'triple', (select id from public.subjects where name = 'Chemistry'), 'AQA', 10, null, 'Rate and Extent of Chemical Change', 'reversible-reactions-equilibrium', '/triple/higher/chemistry/rates-equilibrium/reversible-reactions-equilibrium.html', true),
  ('KS4', 11, 'higher', 'triple', (select id from public.subjects where name = 'Chemistry'), 'AQA', 11, null, 'Rate and Extent of Chemical Change', 'effect-of-conditions-equilibrium', '/triple/higher/chemistry/rates-equilibrium/effect-of-conditions-equilibrium.html', true),
  -- organic — Organic Chemistry
  ('KS4', 11, 'higher', 'triple', (select id from public.subjects where name = 'Chemistry'), 'AQA', 12, null, 'Organic Chemistry', 'crude-oil-hydrocarbons', '/triple/higher/chemistry/organic/crude-oil-hydrocarbons.html', true),
  ('KS4', 11, 'higher', 'triple', (select id from public.subjects where name = 'Chemistry'), 'AQA', 13, null, 'Organic Chemistry', 'fractional-distillation', '/triple/higher/chemistry/organic/fractional-distillation.html', true),
  ('KS4', 11, 'higher', 'triple', (select id from public.subjects where name = 'Chemistry'), 'AQA', 14, null, 'Organic Chemistry', 'properties-of-hydrocarbons', '/triple/higher/chemistry/organic/properties-of-hydrocarbons.html', true),
  ('KS4', 11, 'higher', 'triple', (select id from public.subjects where name = 'Chemistry'), 'AQA', 15, null, 'Organic Chemistry', 'cracking-alkenes', '/triple/higher/chemistry/organic/cracking-alkenes.html', true),
  ('KS4', 11, 'higher', 'triple', (select id from public.subjects where name = 'Chemistry'), 'AQA', 16, null, 'Organic Chemistry', 'structure-of-alkenes', '/triple/higher/chemistry/organic/structure-of-alkenes.html', true),
  ('KS4', 11, 'higher', 'triple', (select id from public.subjects where name = 'Chemistry'), 'AQA', 17, null, 'Organic Chemistry', 'reactions-of-alkenes', '/triple/higher/chemistry/organic/reactions-of-alkenes.html', true),
  ('KS4', 11, 'higher', 'triple', (select id from public.subjects where name = 'Chemistry'), 'AQA', 18, null, 'Organic Chemistry', 'alcohols', '/triple/higher/chemistry/organic/alcohols.html', true),
  ('KS4', 11, 'higher', 'triple', (select id from public.subjects where name = 'Chemistry'), 'AQA', 19, null, 'Organic Chemistry', 'carboxylic-acids', '/triple/higher/chemistry/organic/carboxylic-acids.html', true),
  ('KS4', 11, 'higher', 'triple', (select id from public.subjects where name = 'Chemistry'), 'AQA', 20, null, 'Organic Chemistry', 'addition-polymerisation', '/triple/higher/chemistry/organic/addition-polymerisation.html', true),
  ('KS4', 11, 'higher', 'triple', (select id from public.subjects where name = 'Chemistry'), 'AQA', 21, null, 'Organic Chemistry', 'condensation-polymerisation', '/triple/higher/chemistry/organic/condensation-polymerisation.html', true),
  ('KS4', 11, 'higher', 'triple', (select id from public.subjects where name = 'Chemistry'), 'AQA', 22, null, 'Organic Chemistry', 'amino-acids', '/triple/higher/chemistry/organic/amino-acids.html', true),
  ('KS4', 11, 'higher', 'triple', (select id from public.subjects where name = 'Chemistry'), 'AQA', 23, null, 'Organic Chemistry', 'dna-naturally-occurring-polymers', '/triple/higher/chemistry/organic/dna-naturally-occurring-polymers.html', true),
  -- analysis — Chemical Analysis
  ('KS4', 11, 'higher', 'triple', (select id from public.subjects where name = 'Chemistry'), 'AQA', 24, null, 'Chemical Analysis', 'pure-substances', '/triple/higher/chemistry/analysis/pure-substances.html', true),
  ('KS4', 11, 'higher', 'triple', (select id from public.subjects where name = 'Chemistry'), 'AQA', 25, null, 'Chemical Analysis', 'formulations', '/triple/higher/chemistry/analysis/formulations.html', true),
  ('KS4', 11, 'higher', 'triple', (select id from public.subjects where name = 'Chemistry'), 'AQA', 26, null, 'Chemical Analysis', 'chromatography', '/triple/higher/chemistry/analysis/chromatography.html', true),
  ('KS4', 11, 'higher', 'triple', (select id from public.subjects where name = 'Chemistry'), 'AQA', 27, null, 'Chemical Analysis', 'testing-for-gases', '/triple/higher/chemistry/analysis/testing-for-gases.html', true),
  ('KS4', 11, 'higher', 'triple', (select id from public.subjects where name = 'Chemistry'), 'AQA', 28, null, 'Chemical Analysis', 'flame-tests', '/triple/higher/chemistry/analysis/flame-tests.html', true),
  ('KS4', 11, 'higher', 'triple', (select id from public.subjects where name = 'Chemistry'), 'AQA', 29, null, 'Chemical Analysis', 'metal-hydroxides', '/triple/higher/chemistry/analysis/metal-hydroxides.html', true),
  ('KS4', 11, 'higher', 'triple', (select id from public.subjects where name = 'Chemistry'), 'AQA', 30, null, 'Chemical Analysis', 'carbonates-halides-sulfates', '/triple/higher/chemistry/analysis/carbonates-halides-sulfates.html', true),
  ('KS4', 11, 'higher', 'triple', (select id from public.subjects where name = 'Chemistry'), 'AQA', 31, null, 'Chemical Analysis', 'instrumental-methods', '/triple/higher/chemistry/analysis/instrumental-methods.html', true),
  -- atmosphere — Chemistry of the Atmosphere
  ('KS4', 11, 'higher', 'triple', (select id from public.subjects where name = 'Chemistry'), 'AQA', 32, null, 'Chemistry of the Atmosphere', 'composition-of-atmosphere', '/triple/higher/chemistry/atmosphere/composition-of-atmosphere.html', true),
  ('KS4', 11, 'higher', 'triple', (select id from public.subjects where name = 'Chemistry'), 'AQA', 33, null, 'Chemistry of the Atmosphere', 'early-atmosphere', '/triple/higher/chemistry/atmosphere/early-atmosphere.html', true),
  ('KS4', 11, 'higher', 'triple', (select id from public.subjects where name = 'Chemistry'), 'AQA', 34, null, 'Chemistry of the Atmosphere', 'greenhouse-gases', '/triple/higher/chemistry/atmosphere/greenhouse-gases.html', true),
  ('KS4', 11, 'higher', 'triple', (select id from public.subjects where name = 'Chemistry'), 'AQA', 35, null, 'Chemistry of the Atmosphere', 'atmospheric-pollutants', '/triple/higher/chemistry/atmosphere/atmospheric-pollutants.html', true),
  -- resources — Using Resources
  ('KS4', 11, 'higher', 'triple', (select id from public.subjects where name = 'Chemistry'), 'AQA', 36, null, 'Using Resources', 'earths-resources', '/triple/higher/chemistry/resources/earths-resources.html', true),
  ('KS4', 11, 'higher', 'triple', (select id from public.subjects where name = 'Chemistry'), 'AQA', 37, null, 'Using Resources', 'potable-water', '/triple/higher/chemistry/resources/potable-water.html', true),
  ('KS4', 11, 'higher', 'triple', (select id from public.subjects where name = 'Chemistry'), 'AQA', 38, null, 'Using Resources', 'life-cycle-assessment', '/triple/higher/chemistry/resources/life-cycle-assessment.html', true),
  ('KS4', 11, 'higher', 'triple', (select id from public.subjects where name = 'Chemistry'), 'AQA', 39, null, 'Using Resources', 'reducing-use-of-resources', '/triple/higher/chemistry/resources/reducing-use-of-resources.html', true),
  ('KS4', 11, 'higher', 'triple', (select id from public.subjects where name = 'Chemistry'), 'AQA', 40, null, 'Using Resources', 'corrosion-prevention', '/triple/higher/chemistry/resources/corrosion-prevention.html', true),
  ('KS4', 11, 'higher', 'triple', (select id from public.subjects where name = 'Chemistry'), 'AQA', 41, null, 'Using Resources', 'alloys-useful-materials', '/triple/higher/chemistry/resources/alloys-useful-materials.html', true),
  ('KS4', 11, 'higher', 'triple', (select id from public.subjects where name = 'Chemistry'), 'AQA', 42, null, 'Using Resources', 'ceramics-polymers-composites', '/triple/higher/chemistry/resources/ceramics-polymers-composites.html', true),
  ('KS4', 11, 'higher', 'triple', (select id from public.subjects where name = 'Chemistry'), 'AQA', 43, null, 'Using Resources', 'haber-process', '/triple/higher/chemistry/resources/haber-process.html', true),
  ('KS4', 11, 'higher', 'triple', (select id from public.subjects where name = 'Chemistry'), 'AQA', 44, null, 'Using Resources', 'npk-fertilisers', '/triple/higher/chemistry/resources/npk-fertilisers.html', true),
  ('KS4', 11, 'higher', 'triple', (select id from public.subjects where name = 'Chemistry'), 'AQA', 45, null, 'Using Resources', 'alternative-metal-extraction', '/triple/higher/chemistry/resources/alternative-metal-extraction.html', true);

-- ── Triple · Higher · Physics · Year 10 — 37 lessons ─────────────────────
insert into public.scheme_of_work_entries
  (key_stage, year_group, tier, pathway, subject_id, exam_board, academic_week, half_term, topic, subtopic, notes, active)
values
  -- energy — Energy
  ('KS4', 10, 'higher', 'triple', (select id from public.subjects where name = 'Physics'), 'AQA', 1, null, 'Energy', 'energy-stores-systems', '/triple/higher/physics/energy/energy-stores-systems.html', true),
  ('KS4', 10, 'higher', 'triple', (select id from public.subjects where name = 'Physics'), 'AQA', 2, null, 'Energy', 'changes-in-energy', '/triple/higher/physics/energy/changes-in-energy.html', true),
  ('KS4', 10, 'higher', 'triple', (select id from public.subjects where name = 'Physics'), 'AQA', 3, null, 'Energy', 'energy-changes-in-systems', '/triple/higher/physics/energy/energy-changes-in-systems.html', true),
  ('KS4', 10, 'higher', 'triple', (select id from public.subjects where name = 'Physics'), 'AQA', 4, null, 'Energy', 'power', '/triple/higher/physics/energy/power.html', true),
  ('KS4', 10, 'higher', 'triple', (select id from public.subjects where name = 'Physics'), 'AQA', 5, null, 'Energy', 'energy-transfers-in-a-system', '/triple/higher/physics/energy/energy-transfers-in-a-system.html', true),
  ('KS4', 10, 'higher', 'triple', (select id from public.subjects where name = 'Physics'), 'AQA', 6, null, 'Energy', 'efficiency', '/triple/higher/physics/energy/efficiency.html', true),
  ('KS4', 10, 'higher', 'triple', (select id from public.subjects where name = 'Physics'), 'AQA', 7, null, 'Energy', 'energy-resources', '/triple/higher/physics/energy/energy-resources.html', true),
  ('KS4', 10, 'higher', 'triple', (select id from public.subjects where name = 'Physics'), 'AQA', 8, null, 'Energy', 'thermal-conductivity', '/triple/higher/physics/energy/thermal-conductivity.html', true),
  -- electricity — Electricity
  ('KS4', 10, 'higher', 'triple', (select id from public.subjects where name = 'Physics'), 'AQA', 9, null, 'Electricity', 'circuit-symbols', '/triple/higher/physics/electricity/circuit-symbols.html', true),
  ('KS4', 10, 'higher', 'triple', (select id from public.subjects where name = 'Physics'), 'AQA', 10, null, 'Electricity', 'electrical-charge-current', '/triple/higher/physics/electricity/electrical-charge-current.html', true),
  ('KS4', 10, 'higher', 'triple', (select id from public.subjects where name = 'Physics'), 'AQA', 11, null, 'Electricity', 'current-resistance-pd', '/triple/higher/physics/electricity/current-resistance-pd.html', true),
  ('KS4', 10, 'higher', 'triple', (select id from public.subjects where name = 'Physics'), 'AQA', 12, null, 'Electricity', 'resistors', '/triple/higher/physics/electricity/resistors.html', true),
  ('KS4', 10, 'higher', 'triple', (select id from public.subjects where name = 'Physics'), 'AQA', 13, null, 'Electricity', 'series-parallel-circuits', '/triple/higher/physics/electricity/series-parallel-circuits.html', true),
  ('KS4', 10, 'higher', 'triple', (select id from public.subjects where name = 'Physics'), 'AQA', 14, null, 'Electricity', 'direct-alternating-pd', '/triple/higher/physics/electricity/direct-alternating-pd.html', true),
  ('KS4', 10, 'higher', 'triple', (select id from public.subjects where name = 'Physics'), 'AQA', 15, null, 'Electricity', 'mains-electricity', '/triple/higher/physics/electricity/mains-electricity.html', true),
  ('KS4', 10, 'higher', 'triple', (select id from public.subjects where name = 'Physics'), 'AQA', 16, null, 'Electricity', 'power-electricity', '/triple/higher/physics/electricity/power-electricity.html', true),
  ('KS4', 10, 'higher', 'triple', (select id from public.subjects where name = 'Physics'), 'AQA', 17, null, 'Electricity', 'energy-transfers-appliances', '/triple/higher/physics/electricity/energy-transfers-appliances.html', true),
  ('KS4', 10, 'higher', 'triple', (select id from public.subjects where name = 'Physics'), 'AQA', 18, null, 'Electricity', 'national-grid', '/triple/higher/physics/electricity/national-grid.html', true),
  ('KS4', 10, 'higher', 'triple', (select id from public.subjects where name = 'Physics'), 'AQA', 19, null, 'Electricity', 'static-charge', '/triple/higher/physics/electricity/static-charge.html', true),
  ('KS4', 10, 'higher', 'triple', (select id from public.subjects where name = 'Physics'), 'AQA', 20, null, 'Electricity', 'electric-fields', '/triple/higher/physics/electricity/electric-fields.html', true),
  -- particle-model — Particle Model of Matter
  ('KS4', 10, 'higher', 'triple', (select id from public.subjects where name = 'Physics'), 'AQA', 21, null, 'Particle Model of Matter', 'density-of-materials', '/triple/higher/physics/particle-model/density-of-materials.html', true),
  ('KS4', 10, 'higher', 'triple', (select id from public.subjects where name = 'Physics'), 'AQA', 22, null, 'Particle Model of Matter', 'changes-of-state', '/triple/higher/physics/particle-model/changes-of-state.html', true),
  ('KS4', 10, 'higher', 'triple', (select id from public.subjects where name = 'Physics'), 'AQA', 23, null, 'Particle Model of Matter', 'internal-energy', '/triple/higher/physics/particle-model/internal-energy.html', true),
  ('KS4', 10, 'higher', 'triple', (select id from public.subjects where name = 'Physics'), 'AQA', 24, null, 'Particle Model of Matter', 'temperature-changes-shc', '/triple/higher/physics/particle-model/temperature-changes-shc.html', true),
  ('KS4', 10, 'higher', 'triple', (select id from public.subjects where name = 'Physics'), 'AQA', 25, null, 'Particle Model of Matter', 'specific-latent-heat', '/triple/higher/physics/particle-model/specific-latent-heat.html', true),
  ('KS4', 10, 'higher', 'triple', (select id from public.subjects where name = 'Physics'), 'AQA', 26, null, 'Particle Model of Matter', 'particle-motion-pressure', '/triple/higher/physics/particle-model/particle-motion-pressure.html', true),
  -- atomic-structure — Atomic Structure
  ('KS4', 10, 'higher', 'triple', (select id from public.subjects where name = 'Physics'), 'AQA', 27, null, 'Atomic Structure', 'structure-of-atom', '/triple/higher/physics/atomic-structure/structure-of-atom.html', true),
  ('KS4', 10, 'higher', 'triple', (select id from public.subjects where name = 'Physics'), 'AQA', 28, null, 'Atomic Structure', 'mass-number-isotopes', '/triple/higher/physics/atomic-structure/mass-number-isotopes.html', true),
  ('KS4', 10, 'higher', 'triple', (select id from public.subjects where name = 'Physics'), 'AQA', 29, null, 'Atomic Structure', 'development-atomic-model', '/triple/higher/physics/atomic-structure/development-atomic-model.html', true),
  ('KS4', 10, 'higher', 'triple', (select id from public.subjects where name = 'Physics'), 'AQA', 30, null, 'Atomic Structure', 'radioactive-decay', '/triple/higher/physics/atomic-structure/radioactive-decay.html', true),
  ('KS4', 10, 'higher', 'triple', (select id from public.subjects where name = 'Physics'), 'AQA', 31, null, 'Atomic Structure', 'nuclear-equations', '/triple/higher/physics/atomic-structure/nuclear-equations.html', true),
  ('KS4', 10, 'higher', 'triple', (select id from public.subjects where name = 'Physics'), 'AQA', 32, null, 'Atomic Structure', 'half-lives', '/triple/higher/physics/atomic-structure/half-lives.html', true),
  ('KS4', 10, 'higher', 'triple', (select id from public.subjects where name = 'Physics'), 'AQA', 33, null, 'Atomic Structure', 'radioactive-contamination', '/triple/higher/physics/atomic-structure/radioactive-contamination.html', true),
  ('KS4', 10, 'higher', 'triple', (select id from public.subjects where name = 'Physics'), 'AQA', 34, null, 'Atomic Structure', 'background-radiation', '/triple/higher/physics/atomic-structure/background-radiation.html', true),
  ('KS4', 10, 'higher', 'triple', (select id from public.subjects where name = 'Physics'), 'AQA', 35, null, 'Atomic Structure', 'uses-of-nuclear-radiation', '/triple/higher/physics/atomic-structure/uses-of-nuclear-radiation.html', true),
  ('KS4', 10, 'higher', 'triple', (select id from public.subjects where name = 'Physics'), 'AQA', 36, null, 'Atomic Structure', 'nuclear-fission', '/triple/higher/physics/atomic-structure/nuclear-fission.html', true),
  ('KS4', 10, 'higher', 'triple', (select id from public.subjects where name = 'Physics'), 'AQA', 37, null, 'Atomic Structure', 'nuclear-fusion', '/triple/higher/physics/atomic-structure/nuclear-fusion.html', true);

-- ── Triple · Higher · Physics · Year 11 — 45 lessons ─────────────────────
insert into public.scheme_of_work_entries
  (key_stage, year_group, tier, pathway, subject_id, exam_board, academic_week, half_term, topic, subtopic, notes, active)
values
  -- forces — Forces
  ('KS4', 11, 'higher', 'triple', (select id from public.subjects where name = 'Physics'), 'AQA', 1, null, 'Forces', 'scalar-vector-quantities', '/triple/higher/physics/forces/scalar-vector-quantities.html', true),
  ('KS4', 11, 'higher', 'triple', (select id from public.subjects where name = 'Physics'), 'AQA', 2, null, 'Forces', 'contact-noncontact-forces', '/triple/higher/physics/forces/contact-noncontact-forces.html', true),
  ('KS4', 11, 'higher', 'triple', (select id from public.subjects where name = 'Physics'), 'AQA', 3, null, 'Forces', 'gravity', '/triple/higher/physics/forces/gravity.html', true),
  ('KS4', 11, 'higher', 'triple', (select id from public.subjects where name = 'Physics'), 'AQA', 4, null, 'Forces', 'resultant-forces', '/triple/higher/physics/forces/resultant-forces.html', true),
  ('KS4', 11, 'higher', 'triple', (select id from public.subjects where name = 'Physics'), 'AQA', 5, null, 'Forces', 'resolving-forces', '/triple/higher/physics/forces/resolving-forces.html', true),
  ('KS4', 11, 'higher', 'triple', (select id from public.subjects where name = 'Physics'), 'AQA', 6, null, 'Forces', 'free-body-diagrams', '/triple/higher/physics/forces/free-body-diagrams.html', true),
  ('KS4', 11, 'higher', 'triple', (select id from public.subjects where name = 'Physics'), 'AQA', 7, null, 'Forces', 'work-done-energy-transfer', '/triple/higher/physics/forces/work-done-energy-transfer.html', true),
  ('KS4', 11, 'higher', 'triple', (select id from public.subjects where name = 'Physics'), 'AQA', 8, null, 'Forces', 'forces-elasticity', '/triple/higher/physics/forces/forces-elasticity.html', true),
  ('KS4', 11, 'higher', 'triple', (select id from public.subjects where name = 'Physics'), 'AQA', 9, null, 'Forces', 'moments-levers-gears', '/triple/higher/physics/forces/moments-levers-gears.html', true),
  ('KS4', 11, 'higher', 'triple', (select id from public.subjects where name = 'Physics'), 'AQA', 10, null, 'Forces', 'pressure-in-a-fluid', '/triple/higher/physics/forces/pressure-in-a-fluid.html', true),
  ('KS4', 11, 'higher', 'triple', (select id from public.subjects where name = 'Physics'), 'AQA', 11, null, 'Forces', 'upthrust-floating', '/triple/higher/physics/forces/upthrust-floating.html', true),
  ('KS4', 11, 'higher', 'triple', (select id from public.subjects where name = 'Physics'), 'AQA', 12, null, 'Forces', 'distance-speed-velocity', '/triple/higher/physics/forces/distance-speed-velocity.html', true),
  ('KS4', 11, 'higher', 'triple', (select id from public.subjects where name = 'Physics'), 'AQA', 13, null, 'Forces', 'distance-time-graphs', '/triple/higher/physics/forces/distance-time-graphs.html', true),
  ('KS4', 11, 'higher', 'triple', (select id from public.subjects where name = 'Physics'), 'AQA', 14, null, 'Forces', 'acceleration', '/triple/higher/physics/forces/acceleration.html', true),
  ('KS4', 11, 'higher', 'triple', (select id from public.subjects where name = 'Physics'), 'AQA', 15, null, 'Forces', 'newtons-laws', '/triple/higher/physics/forces/newtons-laws.html', true),
  ('KS4', 11, 'higher', 'triple', (select id from public.subjects where name = 'Physics'), 'AQA', 16, null, 'Forces', 'stopping-distance-braking', '/triple/higher/physics/forces/stopping-distance-braking.html', true),
  ('KS4', 11, 'higher', 'triple', (select id from public.subjects where name = 'Physics'), 'AQA', 17, null, 'Forces', 'motion-in-a-circle', '/triple/higher/physics/forces/motion-in-a-circle.html', true),
  ('KS4', 11, 'higher', 'triple', (select id from public.subjects where name = 'Physics'), 'AQA', 18, null, 'Forces', 'momentum', '/triple/higher/physics/forces/momentum.html', true),
  -- waves — Waves
  ('KS4', 11, 'higher', 'triple', (select id from public.subjects where name = 'Physics'), 'AQA', 19, null, 'Waves', 'transverse-longitudinal-waves', '/triple/higher/physics/waves/transverse-longitudinal-waves.html', true),
  ('KS4', 11, 'higher', 'triple', (select id from public.subjects where name = 'Physics'), 'AQA', 20, null, 'Waves', 'sound-waves-hearing', '/triple/higher/physics/waves/sound-waves-hearing.html', true),
  ('KS4', 11, 'higher', 'triple', (select id from public.subjects where name = 'Physics'), 'AQA', 21, null, 'Waves', 'waves-detection-exploration', '/triple/higher/physics/waves/waves-detection-exploration.html', true),
  ('KS4', 11, 'higher', 'triple', (select id from public.subjects where name = 'Physics'), 'AQA', 22, null, 'Waves', 'properties-of-waves', '/triple/higher/physics/waves/properties-of-waves.html', true),
  ('KS4', 11, 'higher', 'triple', (select id from public.subjects where name = 'Physics'), 'AQA', 23, null, 'Waves', 'types-of-em-waves', '/triple/higher/physics/waves/types-of-em-waves.html', true),
  ('KS4', 11, 'higher', 'triple', (select id from public.subjects where name = 'Physics'), 'AQA', 24, null, 'Waves', 'properties-em-waves-1', '/triple/higher/physics/waves/properties-em-waves-1.html', true),
  ('KS4', 11, 'higher', 'triple', (select id from public.subjects where name = 'Physics'), 'AQA', 25, null, 'Waves', 'properties-em-waves-2', '/triple/higher/physics/waves/properties-em-waves-2.html', true),
  ('KS4', 11, 'higher', 'triple', (select id from public.subjects where name = 'Physics'), 'AQA', 26, null, 'Waves', 'uses-em-waves', '/triple/higher/physics/waves/uses-em-waves.html', true),
  ('KS4', 11, 'higher', 'triple', (select id from public.subjects where name = 'Physics'), 'AQA', 27, null, 'Waves', 'wave-front-refraction', '/triple/higher/physics/waves/wave-front-refraction.html', true),
  ('KS4', 11, 'higher', 'triple', (select id from public.subjects where name = 'Physics'), 'AQA', 28, null, 'Waves', 'lenses', '/triple/higher/physics/waves/lenses.html', true),
  ('KS4', 11, 'higher', 'triple', (select id from public.subjects where name = 'Physics'), 'AQA', 29, null, 'Waves', 'infrared-black-bodies', '/triple/higher/physics/waves/infrared-black-bodies.html', true),
  ('KS4', 11, 'higher', 'triple', (select id from public.subjects where name = 'Physics'), 'AQA', 30, null, 'Waves', 'radiation-balance-temperature', '/triple/higher/physics/waves/radiation-balance-temperature.html', true),
  -- magnetism — Magnetism and Electromagnetism
  ('KS4', 11, 'higher', 'triple', (select id from public.subjects where name = 'Physics'), 'AQA', 31, null, 'Magnetism and Electromagnetism', 'poles-of-a-magnet', '/triple/higher/physics/magnetism/poles-of-a-magnet.html', true),
  ('KS4', 11, 'higher', 'triple', (select id from public.subjects where name = 'Physics'), 'AQA', 32, null, 'Magnetism and Electromagnetism', 'magnetic-fields', '/triple/higher/physics/magnetism/magnetic-fields.html', true),
  ('KS4', 11, 'higher', 'triple', (select id from public.subjects where name = 'Physics'), 'AQA', 33, null, 'Magnetism and Electromagnetism', 'electromagnetism', '/triple/higher/physics/magnetism/electromagnetism.html', true),
  ('KS4', 11, 'higher', 'triple', (select id from public.subjects where name = 'Physics'), 'AQA', 34, null, 'Magnetism and Electromagnetism', 'flemings-left-hand-rule', '/triple/higher/physics/magnetism/flemings-left-hand-rule.html', true),
  ('KS4', 11, 'higher', 'triple', (select id from public.subjects where name = 'Physics'), 'AQA', 35, null, 'Magnetism and Electromagnetism', 'electric-motors', '/triple/higher/physics/magnetism/electric-motors.html', true),
  ('KS4', 11, 'higher', 'triple', (select id from public.subjects where name = 'Physics'), 'AQA', 36, null, 'Magnetism and Electromagnetism', 'loudspeakers-headphones', '/triple/higher/physics/magnetism/loudspeakers-headphones.html', true),
  ('KS4', 11, 'higher', 'triple', (select id from public.subjects where name = 'Physics'), 'AQA', 37, null, 'Magnetism and Electromagnetism', 'induced-potential', '/triple/higher/physics/magnetism/induced-potential.html', true),
  ('KS4', 11, 'higher', 'triple', (select id from public.subjects where name = 'Physics'), 'AQA', 38, null, 'Magnetism and Electromagnetism', 'uses-generator-effect', '/triple/higher/physics/magnetism/uses-generator-effect.html', true),
  ('KS4', 11, 'higher', 'triple', (select id from public.subjects where name = 'Physics'), 'AQA', 39, null, 'Magnetism and Electromagnetism', 'microphones', '/triple/higher/physics/magnetism/microphones.html', true),
  ('KS4', 11, 'higher', 'triple', (select id from public.subjects where name = 'Physics'), 'AQA', 40, null, 'Magnetism and Electromagnetism', 'transformers', '/triple/higher/physics/magnetism/transformers.html', true),
  -- space — Space Physics
  ('KS4', 11, 'higher', 'triple', (select id from public.subjects where name = 'Physics'), 'AQA', 41, null, 'Space Physics', 'solar-system-gravity', '/triple/higher/physics/space/solar-system-gravity.html', true),
  ('KS4', 11, 'higher', 'triple', (select id from public.subjects where name = 'Physics'), 'AQA', 42, null, 'Space Physics', 'gravity-stable-orbits', '/triple/higher/physics/space/gravity-stable-orbits.html', true),
  ('KS4', 11, 'higher', 'triple', (select id from public.subjects where name = 'Physics'), 'AQA', 43, null, 'Space Physics', 'stellar-evolution', '/triple/higher/physics/space/stellar-evolution.html', true),
  ('KS4', 11, 'higher', 'triple', (select id from public.subjects where name = 'Physics'), 'AQA', 44, null, 'Space Physics', 'red-shift-big-bang', '/triple/higher/physics/space/red-shift-big-bang.html', true),
  ('KS4', 11, 'higher', 'triple', (select id from public.subjects where name = 'Physics'), 'AQA', 45, null, 'Space Physics', 'dark-matter-dark-energy', '/triple/higher/physics/space/dark-matter-dark-energy.html', true);

commit;


-- ═══════════════════════════════════════════════════════════════════════
-- ⚠️ OMITTED — 0 subtopic pages with no scheme-of-work row.
-- ═══════════════════════════════════════════════════════════════════════
--
-- None. Every subtopic in the curriculum has a row above.
--
