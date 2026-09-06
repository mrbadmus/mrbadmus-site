-- ═══════════════════════════════════════════════════════════════════════
-- Rainford High School — the school's OWN KS4 scheme of work.
--
-- ⚠️ GENERATED FILE — DO NOT EDIT BY HAND.
--    Regenerate with:  python3 rainford_sow.py
--    Source of truth:  Rainford SOW/NEW Ks4 SOW.xlsx, sheet 'KS4 SOW '
--    Mapping:          rainford_sow.py MAP  ← review THAT, not this file
--    Written to:       supabase/seeds/20260906234500_rainford_ks4_overrides.sql
--    Target table:     public.scheme_of_work_overrides
--                      (PER-SCHOOL — every row carries school_id)
--
-- ═══════════════════════════════════════════════════════════════════════
-- ⚠️ THIS IS ONE SCHOOL'S SEQUENCE AND IS NEVER THE PLATFORM DEFAULT.
-- ═══════════════════════════════════════════════════════════════════════
--
-- Mide's standing ruling of 2026-07-26: "Rainford's SOW is reference
-- evidence, never a template — the platform must be school-agnostic."
--
-- The platform default is the AQA-spec order in
-- public.scheme_of_work_entries, written by ks4_seed_sow.py. This file
-- writes to a DIFFERENT TABLE and deletes only rows that already carry
-- Rainford's school_id and key_stage='KS4'. It cannot reach the global
-- table, KS3 rows, or any other school's rows.
--
-- Rainford BEGINS KS4 IN YEAR 9, so year_group runs 9, 10, 11.
--
-- tier comes from the spreadsheet column the lesson was written in.
-- pathway is NULL on every row: Rainford's sheet is ONE sequence per
-- tier, in which Triple-only lessons are marked inline with a (BIO),
-- (CHEM) or (PHYS) prefix rather than split into a second sequence.
-- Splitting it here would have meant inventing a Combined week order
-- Rainford has never written down. The marking is not lost: the prefix
-- survives verbatim in notes, and every mapped row's subtopic carries
-- the site's own triple_only flag.
--
--   Prefix check: 66 mapped entries carry a (BIO)/(CHEM)/(PHYS) prefix;
--   58 of them map to a subtopic the site independently flags
--   triple_only. 7 unprefixed entries map to a triple_only subtopic.
--
-- academic_week is a teaching ORDER, renumbered from 1 inside each
-- (year_group, subject, tier) block. Rainford's own running lesson
-- numbers (1..120, continuous across all three years) are NOT weeks and
-- are preserved in notes instead. Ceiling: 60, per the CHECK added by
-- migration 20260906230500.
--
-- Idempotent: every Rainford KS4 override row is deleted and rewritten,
-- inside one transaction. Re-running is safe and is how a change lands.
--
-- Rows emitted per block:
--
--   year   subject   tier        lessons
--   Y9     Biology   higher       19
--   Y9     Biology   foundation   19
--   Y9     Chemistry higher       20
--   Y9     Chemistry foundation   20
--   Y9     Physics   higher       17
--   Y9     Physics   foundation   17
--   Y10    Biology   higher       46
--   Y10    Biology   foundation   46
--   Y10    Chemistry higher       48
--   Y10    Chemistry foundation   46
--   Y10    Physics   higher       47
--   Y10    Physics   foundation   47
--   Y11    Biology   higher       55
--   Y11    Biology   foundation   54
--   Y11    Chemistry higher       44
--   Y11    Chemistry foundation   36
--   Y11    Physics   higher       46
--   Y11    Physics   foundation   43
--
--   670 rows · 550 carry a subtopic · 120 do not (named at the foot of
--   this file, every one of them, with the reason).
--
-- ═══════════════════════════════════════════════════════════════════════

begin;

-- Preconditions. Failing here with a sentence beats failing later with a
-- NOT NULL violation on a subselect that quietly returned NULL.
do $$
begin
  if not exists (select 1 from public.schools where name = 'Rainford High School') then
    raise exception 'Rainford KS4 seed: no school named %. Insert the school '
                    'row before seeding its scheme of work.', 'Rainford High School';
  end if;
  if (select count(*) from public.subjects
       where name in ('Biology', 'Chemistry', 'Physics')) <> 3 then
    raise exception 'Rainford KS4 seed: public.subjects is missing one of '
                    'Biology / Chemistry / Physics. Seed subjects first.';
  end if;
end $$;

-- Idempotency: this file owns every KS4 override row for this school, and
-- nothing else. KS3 rows, other schools' rows and the global table are all
-- outside the WHERE clause.
delete from public.scheme_of_work_overrides
 where key_stage = 'KS4'
   and school_id = (select id from public.schools where name = 'Rainford High School');

-- ── Year 9 · Biology · higher — 19 lessons ─────────────────────────
with school as (select id from public.schools where name = 'Rainford High School'),
     subject as (select id from public.subjects where name = 'Biology')
insert into public.scheme_of_work_overrides
  (school_id, key_stage, year_group, tier, pathway, subject_id,
   academic_week, topic, subtopic, notes)
select school.id, 'KS4', 9, 'higher', null, subject.id,
       v.academic_week, v.topic, v.subtopic, v.notes
  from school, subject, (values
  -- Unit 1 Cell biology
  (1::smallint, 'Unit 1 Cell biology'::text, 'animal-plant-cells'::text, 'L1 · Eukarytotes (Animal & plant cells)'::text),
  (2, 'Unit 1 Cell biology', 'cell-specialisation', 'L2 · Cell differentiation & specialisation'),
  (3, 'Unit 1 Cell biology', 'stem-cells', 'L3 · Stem cells'),
  (4, 'Unit 1 Cell biology', 'stem-cells', 'L4 · Uses of stem cells (w/ therapuetic cloning)'),
  (5, 'Unit 1 Cell biology', 'chromosomes-mitosis', 'L5 · Mitosis & the cell cycle'),
  (6, 'Unit 1 Cell biology', 'eukaryotes-prokaryotes', 'L6 · Prokaryotes'),
  (7, 'Unit 1 Cell biology', 'microscopy', 'L7 · Use of a light microscopes RP'),
  (8, 'Unit 1 Cell biology', 'microscopy', 'L8 · Types of microscope'),
  (9, 'Unit 1 Cell biology', 'microscopy', 'L9 · Magnification'),
  (10, 'Unit 1 Cell biology', null, 'L10 · Quiz & application  [no subtopic: assessment]'),
  (11, 'Unit 1 Cell biology', 'transport-in-cells', 'L11 · Diffusion & factors effecting diffusion'),
  (12, 'Unit 1 Cell biology', 'transport-in-cells', 'L12 · Osmosis'),
  (13, 'Unit 1 Cell biology', 'transport-in-cells', 'L13 · Osmosis RP'),
  (14, 'Unit 1 Cell biology', 'transport-in-cells', 'L14 · Osmosis RP 2'),
  (15, 'Unit 1 Cell biology', 'transport-in-cells', 'L15 · Active transport'),
  (16, 'Unit 1 Cell biology', 'transport-in-cells', 'L16 · Surface area : volume ratio'),
  (17, 'Unit 1 Cell biology', 'transport-in-cells', 'L17 · Exchange surfaces'),
  (18, 'Unit 1 Cell biology', null, 'L18 · Cell biology test  [no subtopic: assessment]'),
  (19, 'Unit 1 Cell biology', null, 'L19 · Test review  [no subtopic: assessment]')
) as v (academic_week, topic, subtopic, notes);

-- ── Year 9 · Biology · foundation — 19 lessons ─────────────────────────
with school as (select id from public.schools where name = 'Rainford High School'),
     subject as (select id from public.subjects where name = 'Biology')
insert into public.scheme_of_work_overrides
  (school_id, key_stage, year_group, tier, pathway, subject_id,
   academic_week, topic, subtopic, notes)
select school.id, 'KS4', 9, 'foundation', null, subject.id,
       v.academic_week, v.topic, v.subtopic, v.notes
  from school, subject, (values
  -- Unit 1 Cell biology
  (1::smallint, 'Unit 1 Cell biology'::text, 'animal-plant-cells'::text, 'L1 · Eukarytotes (Animal & plant cells)'::text),
  (2, 'Unit 1 Cell biology', 'cell-specialisation', 'L2 · Cell differentiation & specialisation'),
  (3, 'Unit 1 Cell biology', 'stem-cells', 'L3 · Stem cells'),
  (4, 'Unit 1 Cell biology', 'stem-cells', 'L4 · Uses of stem cells (w/ therapuetic cloning)'),
  (5, 'Unit 1 Cell biology', 'chromosomes-mitosis', 'L5 · Mitosis & the cell cycle'),
  (6, 'Unit 1 Cell biology', 'eukaryotes-prokaryotes', 'L6 · Prokaryotes'),
  (7, 'Unit 1 Cell biology', 'microscopy', 'L7 · Use of a light microscopes RP'),
  (8, 'Unit 1 Cell biology', 'microscopy', 'L8 · Types of microscope'),
  (9, 'Unit 1 Cell biology', 'microscopy', 'L9 · Magnification'),
  (10, 'Unit 1 Cell biology', null, 'L10 · Quiz & application  [no subtopic: assessment]'),
  (11, 'Unit 1 Cell biology', 'transport-in-cells', 'L11 · Diffusion & factors effecting diffusion'),
  (12, 'Unit 1 Cell biology', 'transport-in-cells', 'L12 · Osmosis'),
  (13, 'Unit 1 Cell biology', 'transport-in-cells', 'L13 · Osmosis RP'),
  (14, 'Unit 1 Cell biology', 'transport-in-cells', 'L14 · Osmosis RP 2'),
  (15, 'Unit 1 Cell biology', 'transport-in-cells', 'L15 · Active transport'),
  (16, 'Unit 1 Cell biology', 'transport-in-cells', 'L16 · Surface area : volume ratio'),
  (17, 'Unit 1 Cell biology', 'transport-in-cells', 'L17 · Exchange surfaces'),
  (18, 'Unit 1 Cell biology', null, 'L18 · Cell biology test  [no subtopic: assessment]'),
  (19, 'Unit 1 Cell biology', null, 'L19 · Test review  [no subtopic: assessment]')
) as v (academic_week, topic, subtopic, notes);

-- ── Year 9 · Chemistry · higher — 20 lessons ─────────────────────────
with school as (select id from public.schools where name = 'Rainford High School'),
     subject as (select id from public.subjects where name = 'Chemistry')
insert into public.scheme_of_work_overrides
  (school_id, key_stage, year_group, tier, pathway, subject_id,
   academic_week, topic, subtopic, notes)
select school.id, 'KS4', 9, 'higher', null, subject.id,
       v.academic_week, v.topic, v.subtopic, v.notes
  from school, subject, (values
  -- Unit 1 Atomic structure and the periodic table
  (1::smallint, 'Unit 1 Atomic structure and the periodic table'::text, 'subatomic-particles'::text, 'L1 · Structure of the atom'::text),
  (2, 'Unit 1 Atomic structure and the periodic table', 'electronic-structure', 'L2 · Electronic Structure'),
  (3, 'Unit 1 Atomic structure and the periodic table', 'relative-atomic-mass', 'L3 · Isotopes'),
  (4, 'Unit 1 Atomic structure and the periodic table', 'model-of-the-atom', 'L4 · Development of the Model of the Atom'),
  (5, 'Unit 1 Atomic structure and the periodic table', 'atoms-elements-compounds', 'L5 · Atoms, Elements & Compounds'),
  (6, 'Unit 1 Atomic structure and the periodic table', 'relative-formula-mass', 'L6 · Relative Formula Mass (Mr)'),
  (7, 'Unit 1 Atomic structure and the periodic table', 'conservation-of-mass', 'L7 · Conservation of Mass/Balancing Equations'),
  (8, 'Unit 1 Atomic structure and the periodic table', 'mixtures', 'L8 · Mixtures: Filtration & Evaporation'),
  (9, 'Unit 1 Atomic structure and the periodic table', 'mixtures', 'L9 · Mixtures: Simple Distillation'),
  (10, 'Unit 1 Atomic structure and the periodic table', null, 'L10 · Quiz & application  [no subtopic: assessment]'),
  (11, 'Unit 1 Atomic structure and the periodic table', 'periodic-table', 'L11 · The periodic table'),
  (12, 'Unit 1 Atomic structure and the periodic table', 'development-periodic-table', 'L12 · Development of the periodic table'),
  (13, 'Unit 1 Atomic structure and the periodic table', 'metals-non-metals', 'L13 · Metals and non-metals'),
  (14, 'Unit 1 Atomic structure and the periodic table', 'metallic-bonding', 'L14 · Metallic Bonding/Alloys'),
  (15, 'Unit 1 Atomic structure and the periodic table', 'group-0', 'L15 · Group 0 & (CHEM) Tranistion metals'),
  (16, 'Unit 1 Atomic structure and the periodic table', 'group-1', 'L16 · Group 1'),
  (17, 'Unit 1 Atomic structure and the periodic table', 'group-7', 'L17 · Group 7'),
  (18, 'Unit 1 Atomic structure and the periodic table', 'group-7', 'L18 · Displacement of Halogens'),
  (19, 'Unit 1 Atomic structure and the periodic table', null, 'L19 · Atomic Structure & Periodic Table Test  [no subtopic: assessment]'),
  (20, 'Unit 1 Atomic structure and the periodic table', null, 'L20 · Test Review  [no subtopic: assessment]')
) as v (academic_week, topic, subtopic, notes);

-- ── Year 9 · Chemistry · foundation — 20 lessons ─────────────────────────
with school as (select id from public.schools where name = 'Rainford High School'),
     subject as (select id from public.subjects where name = 'Chemistry')
insert into public.scheme_of_work_overrides
  (school_id, key_stage, year_group, tier, pathway, subject_id,
   academic_week, topic, subtopic, notes)
select school.id, 'KS4', 9, 'foundation', null, subject.id,
       v.academic_week, v.topic, v.subtopic, v.notes
  from school, subject, (values
  -- Unit 1 Atomic structure and the periodic table
  (1::smallint, 'Unit 1 Atomic structure and the periodic table'::text, 'subatomic-particles'::text, 'L1 · Structure of the atom'::text),
  (2, 'Unit 1 Atomic structure and the periodic table', 'electronic-structure', 'L2 · Electronic Structure'),
  (3, 'Unit 1 Atomic structure and the periodic table', 'relative-atomic-mass', 'L3 · Isotopes'),
  (4, 'Unit 1 Atomic structure and the periodic table', 'model-of-the-atom', 'L4 · Development of the Model of the Atom'),
  (5, 'Unit 1 Atomic structure and the periodic table', 'atoms-elements-compounds', 'L5 · Atoms, Elements & Compounds'),
  (6, 'Unit 1 Atomic structure and the periodic table', 'relative-formula-mass', 'L6 · Relative Formula Mass (Mr)'),
  (7, 'Unit 1 Atomic structure and the periodic table', 'conservation-of-mass', 'L7 · Conservation of Mass/Balancing Equations'),
  (8, 'Unit 1 Atomic structure and the periodic table', 'mixtures', 'L8 · Mixtures: Filtration & Evaporation'),
  (9, 'Unit 1 Atomic structure and the periodic table', 'mixtures', 'L9 · Mixtures: Simple Distillation'),
  (10, 'Unit 1 Atomic structure and the periodic table', null, 'L10 · Quiz & application  [no subtopic: assessment]'),
  (11, 'Unit 1 Atomic structure and the periodic table', 'periodic-table', 'L11 · The periodic table'),
  (12, 'Unit 1 Atomic structure and the periodic table', 'development-periodic-table', 'L12 · Development of the periodic table'),
  (13, 'Unit 1 Atomic structure and the periodic table', 'metals-non-metals', 'L13 · Metals and non-metals'),
  (14, 'Unit 1 Atomic structure and the periodic table', 'metallic-bonding', 'L14 · Metallic Bonding/Alloys'),
  (15, 'Unit 1 Atomic structure and the periodic table', 'group-0', 'L15 · Group 0 & (CHEM) Tranistion metals'),
  (16, 'Unit 1 Atomic structure and the periodic table', 'group-1', 'L16 · Group 1'),
  (17, 'Unit 1 Atomic structure and the periodic table', 'group-7', 'L17 · Group 7'),
  (18, 'Unit 1 Atomic structure and the periodic table', 'group-7', 'L18 · Displacement of Halogens'),
  (19, 'Unit 1 Atomic structure and the periodic table', null, 'L19 · Atomic Structure & Periodic Table Test  [no subtopic: assessment]'),
  (20, 'Unit 1 Atomic structure and the periodic table', null, 'L20 · Test Review  [no subtopic: assessment]')
) as v (academic_week, topic, subtopic, notes);

-- ── Year 9 · Physics · higher — 17 lessons ─────────────────────────
with school as (select id from public.schools where name = 'Rainford High School'),
     subject as (select id from public.subjects where name = 'Physics')
insert into public.scheme_of_work_overrides
  (school_id, key_stage, year_group, tier, pathway, subject_id,
   academic_week, topic, subtopic, notes)
select school.id, 'KS4', 9, 'higher', null, subject.id,
       v.academic_week, v.topic, v.subtopic, v.notes
  from school, subject, (values
  -- Unit 1 Energy
  (1::smallint, 'Unit 1 Energy'::text, 'energy-stores-systems'::text, 'L1 · Energy stores & systems'::text),
  (2, 'Unit 1 Energy', 'energy-transfers-in-a-system', 'L2 · Conservation of energy'),
  (3, 'Unit 1 Energy', 'energy-transfers-in-a-system', 'L3 · Energy transfers in a system'),
  (4, 'Unit 1 Energy', 'work-done-energy-transfer', 'L4 · Work done'),
  (5, 'Unit 1 Energy', 'changes-in-energy', 'L5 · Kinetic energy'),
  (6, 'Unit 1 Energy', 'changes-in-energy', 'L6 · Elastic potential energy'),
  (7, 'Unit 1 Energy', 'changes-in-energy', 'L7 · Gravitational potential energy'),
  (8, 'Unit 1 Energy', null, 'L8 · Quiz & application  [no subtopic: assessment]'),
  (9, 'Unit 1 Energy', 'power', 'L9 · Power'),
  (10, 'Unit 1 Energy', 'efficiency', 'L10 · Energy efficiency'),
  (11, 'Unit 1 Energy', 'thermal-conductivity', 'L11 · Thermal conductivity'),
  (12, 'Unit 1 Energy', 'thermal-conductivity', 'L12 · Thermal insulators investigation'),
  (13, 'Unit 1 Energy', 'energy-resources', 'L13 · Non-renewable energy: Fossil Fuels'),
  (14, 'Unit 1 Energy', 'energy-resources', 'L14 · Non-renewable energy: Nuclear'),
  (15, 'Unit 1 Energy', 'energy-resources', 'L15 · Renewable energy'),
  (16, 'Unit 1 Energy', null, 'L16 · Energy Test  [no subtopic: assessment]'),
  (17, 'Unit 1 Energy', null, 'L17 · Test Review  [no subtopic: assessment]')
) as v (academic_week, topic, subtopic, notes);

-- ── Year 9 · Physics · foundation — 17 lessons ─────────────────────────
with school as (select id from public.schools where name = 'Rainford High School'),
     subject as (select id from public.subjects where name = 'Physics')
insert into public.scheme_of_work_overrides
  (school_id, key_stage, year_group, tier, pathway, subject_id,
   academic_week, topic, subtopic, notes)
select school.id, 'KS4', 9, 'foundation', null, subject.id,
       v.academic_week, v.topic, v.subtopic, v.notes
  from school, subject, (values
  -- Unit 1 Energy
  (1::smallint, 'Unit 1 Energy'::text, 'energy-stores-systems'::text, 'L1 · Energy stores & systems'::text),
  (2, 'Unit 1 Energy', 'energy-transfers-in-a-system', 'L2 · Conservation of energy'),
  (3, 'Unit 1 Energy', 'energy-transfers-in-a-system', 'L3 · Energy transfers in a system'),
  (4, 'Unit 1 Energy', 'work-done-energy-transfer', 'L4 · Work done'),
  (5, 'Unit 1 Energy', 'changes-in-energy', 'L5 · Kinetic energy'),
  (6, 'Unit 1 Energy', 'changes-in-energy', 'L6 · Elastic potential energy'),
  (7, 'Unit 1 Energy', 'changes-in-energy', 'L7 · Gravitational potential energy'),
  (8, 'Unit 1 Energy', null, 'L8 · Quiz & application  [no subtopic: assessment]'),
  (9, 'Unit 1 Energy', 'power', 'L9 · Power'),
  (10, 'Unit 1 Energy', 'efficiency', 'L10 · Energy efficiency'),
  (11, 'Unit 1 Energy', 'thermal-conductivity', 'L11 · Thermal conductivity'),
  (12, 'Unit 1 Energy', 'thermal-conductivity', 'L12 · Thermal insulators investigation'),
  (13, 'Unit 1 Energy', 'energy-resources', 'L13 · Non-renewable energy: Fossil Fuels'),
  (14, 'Unit 1 Energy', 'energy-resources', 'L14 · Non-renewable energy: Nuclear'),
  (15, 'Unit 1 Energy', 'energy-resources', 'L15 · Renewable energy'),
  (16, 'Unit 1 Energy', null, 'L16 · Energy Test  [no subtopic: assessment]'),
  (17, 'Unit 1 Energy', null, 'L17 · Test Review  [no subtopic: assessment]')
) as v (academic_week, topic, subtopic, notes);

-- ── Year 10 · Biology · higher — 46 lessons ─────────────────────────
with school as (select id from public.schools where name = 'Rainford High School'),
     subject as (select id from public.subjects where name = 'Biology')
insert into public.scheme_of_work_overrides
  (school_id, key_stage, year_group, tier, pathway, subject_id,
   academic_week, topic, subtopic, notes)
select school.id, 'KS4', 10, 'higher', null, subject.id,
       v.academic_week, v.topic, v.subtopic, v.notes
  from school, subject, (values
  -- Unit 2 Organisation
  (1::smallint, 'Unit 2 Organisation'::text, 'principles-of-organisation'::text, 'L20 · Levels of Organisation - Cells, Tissues & Organs (w/digestive system)'::text),
  (2, 'Unit 2 Organisation', 'digestive-system', 'L21 · Villi & Bile'),
  (3, 'Unit 2 Organisation', 'digestive-system', 'L22 · Food tests'),
  (4, 'Unit 2 Organisation', 'digestive-system', 'L23 · Food tests Part 2'),
  (5, 'Unit 2 Organisation', 'enzymes', 'L24 · Enzymes lock & key & digestive enzymes'),
  (6, 'Unit 2 Organisation', 'enzymes', 'L25 · Factors affecting enzymes'),
  (7, 'Unit 2 Organisation', 'enzymes', 'L26 · Amylase RP'),
  (8, 'Unit 2 Organisation', 'enzymes', 'L27 · Amylase RP 2'),
  (9, 'Unit 2 Organisation', null, 'L28 · Quiz & application  [no subtopic: assessment]'),
  (10, 'Unit 2 Organisation', 'heart-blood-vessels', 'L29 · Heart & circulatory system'),
  (11, 'Unit 2 Organisation', 'blood', 'L30 · Blood & Vessels'),
  (12, 'Unit 2 Organisation', 'coronary-heart-disease', 'L31 · CHD & treatments'),
  (13, 'Unit 2 Organisation', null, 'L32 · Breathing & gas exchange  [no subtopic: absent]'),
  (14, 'Unit 2 Organisation', 'plant-tissues', 'L33 · Structure of a leaf & gas exchange'),
  (15, 'Unit 2 Organisation', null, 'L34 · Transport in plants  [no subtopic: ambiguous]'),
  (16, 'Unit 2 Organisation', null, 'L35 · Organisation test  [no subtopic: assessment]'),
  (17, 'Unit 2 Organisation', null, 'L36 · Test review  [no subtopic: assessment]'),
  -- Unit 3 Infection & response
  (18, 'Unit 3 Infection & response', 'health-disease', 'L37 · Non-commincable disease, health issues & risk factors'),
  (19, 'Unit 3 Infection & response', 'cancer', 'L38 · Cancer and Lifestyle'),
  (20, 'Unit 3 Infection & response', 'viral-diseases', 'L39 · Viral Diseases - Measlea, HIV, TMV'),
  (21, 'Unit 3 Infection & response', 'bacterial-diseases', 'L40 · Bacterial Diseases'),
  (22, 'Unit 3 Infection & response', 'fungal-protist-diseases', 'L41 · Protist Diseases & fungal diseases'),
  (23, 'Unit 3 Infection & response', 'communicable-diseases-defence', 'L42 · Human defence systems'),
  (24, 'Unit 3 Infection & response', 'vaccination', 'L43 · Vaccination'),
  (25, 'Unit 3 Infection & response', 'monoclonal-antibodies', 'L44 · (BIO) Monoclonal antibodies'),
  (26, 'Unit 3 Infection & response', 'antibiotics-painkillers', 'L45 · Antibiotics & painkillers'),
  (27, 'Unit 3 Infection & response', 'culturing-microorganisms', 'L46 · (BIO) Culturing microorganisms RP'),
  (28, 'Unit 3 Infection & response', 'culturing-microorganisms', 'L47 · (BIO) Culturing microorganisms RP2'),
  (29, 'Unit 3 Infection & response', 'drug-discovery-development', 'L48 · Discovery of drugs and Trials'),
  (30, 'Unit 3 Infection & response', 'plant-disease-detection-defence', 'L49 · (BIO) Plant disease'),
  (31, 'Unit 3 Infection & response', null, 'L50 · Infection & response test  [no subtopic: assessment]'),
  -- Unit 4 Bioenergetics
  (32, 'Unit 4 Bioenergetics', 'photosynthesis', 'L51 · Photosynthesis & uses of glucose'),
  (33, 'Unit 4 Bioenergetics', 'photosynthesis', 'L52 · Testing a leaf for starch'),
  (34, 'Unit 4 Bioenergetics', 'rate-of-photosynthesis', 'L53 · Limiting factors of photosynthesis'),
  (35, 'Unit 4 Bioenergetics', 'rate-of-photosynthesis', 'L54 · Photosynthesis RP'),
  (36, 'Unit 4 Bioenergetics', 'rate-of-photosynthesis', 'L55 · Photosynthesis RP 2'),
  (37, 'Unit 4 Bioenergetics', 'aerobic-respiration', 'L56 · Aerobic respiration & uses of energy from respiration'),
  (38, 'Unit 4 Bioenergetics', 'anaerobic-respiration', 'L57 · Anaerobic respiration & fermentation'),
  (39, 'Unit 4 Bioenergetics', 'response-to-exercise', 'L58 · Response to exercise'),
  (40, 'Unit 4 Bioenergetics', 'metabolism', 'L59 · Metabolism'),
  (41, 'Unit 4 Bioenergetics', null, 'L60 · Bioenergetics test  [no subtopic: assessment]'),
  (42, 'Unit 4 Bioenergetics', null, 'L61 · Test review  [no subtopic: assessment]'),
  -- Unit 7 Ecology
  (43, 'Unit 7 Ecology', 'ecosystems', 'L62 · Ecosystems, biotic & abiotic factors'),
  (44, 'Unit 7 Ecology', 'sampling-techniques', 'L63 · Types of sampling'),
  (45, 'Unit 7 Ecology', 'sampling-techniques', 'L64 · Sampling RP'),
  (46, 'Unit 7 Ecology', 'sampling-techniques', 'L65 · Sampling RP 2')
) as v (academic_week, topic, subtopic, notes);

-- ── Year 10 · Biology · foundation — 46 lessons ─────────────────────────
with school as (select id from public.schools where name = 'Rainford High School'),
     subject as (select id from public.subjects where name = 'Biology')
insert into public.scheme_of_work_overrides
  (school_id, key_stage, year_group, tier, pathway, subject_id,
   academic_week, topic, subtopic, notes)
select school.id, 'KS4', 10, 'foundation', null, subject.id,
       v.academic_week, v.topic, v.subtopic, v.notes
  from school, subject, (values
  -- Unit 2 Organisation
  (1::smallint, 'Unit 2 Organisation'::text, 'principles-of-organisation'::text, 'L20 · Levels of Organisation - Cells, Tissues & Organs (w/digestive system)'::text),
  (2, 'Unit 2 Organisation', 'digestive-system', 'L21 · Villi & Bile'),
  (3, 'Unit 2 Organisation', 'digestive-system', 'L22 · Food tests RP'),
  (4, 'Unit 2 Organisation', 'digestive-system', 'L23 · Food tests RP2'),
  (5, 'Unit 2 Organisation', 'enzymes', 'L24 · Enzymes lock & key & digestive enzymes'),
  (6, 'Unit 2 Organisation', 'enzymes', 'L25 · Factors affecting enzymes'),
  (7, 'Unit 2 Organisation', 'enzymes', 'L26 · Amylase RP'),
  (8, 'Unit 2 Organisation', 'enzymes', 'L27 · Amylase RP 2'),
  (9, 'Unit 2 Organisation', null, 'L28 · Quiz & application  [no subtopic: assessment]'),
  (10, 'Unit 2 Organisation', 'heart-blood-vessels', 'L29 · Heart & circulatory system'),
  (11, 'Unit 2 Organisation', 'blood', 'L30 · Blood & Vessels'),
  (12, 'Unit 2 Organisation', 'coronary-heart-disease', 'L31 · CHD & treatments'),
  (13, 'Unit 2 Organisation', null, 'L32 · Breathing & gas exchange  [no subtopic: absent]'),
  (14, 'Unit 2 Organisation', 'plant-tissues', 'L33 · Structure of a leaf & gas exchange'),
  (15, 'Unit 2 Organisation', null, 'L34 · Transport in plants  [no subtopic: ambiguous]'),
  (16, 'Unit 2 Organisation', null, 'L35 · Organisation test  [no subtopic: assessment]'),
  (17, 'Unit 2 Organisation', null, 'L36 · Test review  [no subtopic: assessment]'),
  -- Unit 3 Infection & response
  (18, 'Unit 3 Infection & response', 'health-disease', 'L37 · Non-commincable disease, health issues & risk factors'),
  (19, 'Unit 3 Infection & response', 'cancer', 'L38 · Cancer and lifestyle'),
  (20, 'Unit 3 Infection & response', 'viral-diseases', 'L39 · Viral Diseases - Measlea, HIV, TMV'),
  (21, 'Unit 3 Infection & response', 'bacterial-diseases', 'L40 · Bacterial Diseases'),
  (22, 'Unit 3 Infection & response', 'fungal-protist-diseases', 'L41 · Protist Diseases & fungal diseases'),
  (23, 'Unit 3 Infection & response', 'communicable-diseases-defence', 'L42 · Human defence systems'),
  (24, 'Unit 3 Infection & response', 'vaccination', 'L43 · Vaccination'),
  (25, 'Unit 3 Infection & response', 'monoclonal-antibodies', 'L44 · (BIO) Monoclonal antibodies'),
  (26, 'Unit 3 Infection & response', 'antibiotics-painkillers', 'L45 · Antibiotics & painkillers'),
  (27, 'Unit 3 Infection & response', 'culturing-microorganisms', 'L46 · (BIO) Culturing microorganisms RP'),
  (28, 'Unit 3 Infection & response', 'culturing-microorganisms', 'L47 · (BIO) Culturing microorganisms RP2'),
  (29, 'Unit 3 Infection & response', 'drug-discovery-development', 'L48 · Discovery of drugs and Trials'),
  (30, 'Unit 3 Infection & response', 'plant-disease-detection-defence', 'L49 · (BIO) Plant disease'),
  (31, 'Unit 3 Infection & response', null, 'L50 · Infection & response test  [no subtopic: assessment]'),
  -- Unit 4 Bioenergetics
  (32, 'Unit 4 Bioenergetics', 'photosynthesis', 'L51 · Photosynthesis & uses of glucose'),
  (33, 'Unit 4 Bioenergetics', 'photosynthesis', 'L52 · Testing a leaf for starch'),
  (34, 'Unit 4 Bioenergetics', 'rate-of-photosynthesis', 'L53 · Limiting factors of photosynthesis'),
  (35, 'Unit 4 Bioenergetics', 'rate-of-photosynthesis', 'L54 · Photosynthesis RP'),
  (36, 'Unit 4 Bioenergetics', 'rate-of-photosynthesis', 'L55 · Photosynthesis RP 2'),
  (37, 'Unit 4 Bioenergetics', 'aerobic-respiration', 'L56 · Aerobic respiration & uses of energy from respiration'),
  (38, 'Unit 4 Bioenergetics', 'anaerobic-respiration', 'L57 · Anaerobic respiration & fermentation'),
  (39, 'Unit 4 Bioenergetics', 'response-to-exercise', 'L58 · Response to exercise'),
  (40, 'Unit 4 Bioenergetics', 'metabolism', 'L59 · Metabolism'),
  (41, 'Unit 4 Bioenergetics', null, 'L60 · Bioenergetics test  [no subtopic: assessment]'),
  (42, 'Unit 4 Bioenergetics', null, 'L61 · Test review  [no subtopic: assessment]'),
  -- Unit 7 Ecology
  (43, 'Unit 7 Ecology', 'ecosystems', 'L62 · Ecosystems, biotic & abiotic factors'),
  (44, 'Unit 7 Ecology', 'sampling-techniques', 'L63 · Types of sampling'),
  (45, 'Unit 7 Ecology', 'sampling-techniques', 'L64 · Sampling RP'),
  (46, 'Unit 7 Ecology', 'sampling-techniques', 'L65 · Sampling RP 2')
) as v (academic_week, topic, subtopic, notes);

-- ── Year 10 · Chemistry · higher — 48 lessons ─────────────────────────
with school as (select id from public.schools where name = 'Rainford High School'),
     subject as (select id from public.subjects where name = 'Chemistry')
insert into public.scheme_of_work_overrides
  (school_id, key_stage, year_group, tier, pathway, subject_id,
   academic_week, topic, subtopic, notes)
select school.id, 'KS4', 10, 'higher', null, subject.id,
       v.academic_week, v.topic, v.subtopic, v.notes
  from school, subject, (values
  -- Unit 8 Chemical analysis
  (1::smallint, 'Unit 8 Chemical analysis'::text, 'pure-substances'::text, 'L21 · Pure Substances, Formulations & Testing For Gases'::text),
  (2, 'Unit 8 Chemical analysis', 'chromatography', 'L22 · Chromatography RP'),
  (3, 'Unit 8 Chemical analysis', 'chromatography', 'L23 · Chromatography RP 2'),
  (4, 'Unit 8 Chemical analysis', 'flame-tests', 'L24 · (CHEM) Tests for positive ions (Flame Tests) & Flame Emission Spectroscopy'),
  (5, 'Unit 8 Chemical analysis', 'metal-hydroxides', 'L25 · (CHEM) Tests for positive ions (reaction with metal hydroxide)'),
  (6, 'Unit 8 Chemical analysis', 'carbonates-halides-sulfates', 'L26 · (CHEM) Tests for negative ions'),
  (7, 'Unit 8 Chemical analysis', null, 'L27 · (CHEM) Tests for ions RP  [no subtopic: ambiguous]'),
  -- Unit 9 Chemistry of the atmosphere
  (8, 'Unit 9 Chemistry of the atmosphere', 'early-atmosphere', 'L28 · History & Evolution of the Atmosphere'),
  (9, 'Unit 9 Chemistry of the atmosphere', 'greenhouse-gases', 'L29 · Greenhouse Gases / Climate change'),
  (10, 'Unit 9 Chemistry of the atmosphere', 'atmospheric-pollutants', 'L30 · Atmospheric Pollutants & Carbon Footprint'),
  (11, 'Unit 9 Chemistry of the atmosphere', null, 'L31 · Quiz & application  [no subtopic: assessment]'),
  (12, 'Unit 9 Chemistry of the atmosphere', null, 'L32 · (CHEM) Chemical Analysis & Atmosphere Test  [no subtopic: assessment]'),
  (13, 'Unit 9 Chemistry of the atmosphere', null, 'L33 · (CHEM) Chemical Analysis & Atmosphere Test Review  [no subtopic: assessment]'),
  -- Unit 10 Using resources
  (14, 'Unit 10 Using resources', 'earths-resources', 'L34 · Using the Earth''s Resources & Recycling'),
  (15, 'Unit 10 Using resources', 'potable-water', 'L35 · Potable Water RP 1'),
  (16, 'Unit 10 Using resources', 'potable-water', 'L36 · Potable Water RP 2'),
  (17, 'Unit 10 Using resources', 'potable-water', 'L37 · Waste Water Treatment/Evaluate obtaining potable water'),
  (18, 'Unit 10 Using resources', 'alternative-metal-extraction', 'L38 · Alternative methods of extracting metals (HT only)'),
  (19, 'Unit 10 Using resources', 'corrosion-prevention', 'L39 · (CHEM) Corrosion & Alloys'),
  (20, 'Unit 10 Using resources', 'ceramics-polymers-composites', 'L40 · (CHEM) Ceramics, polymers and composites'),
  (21, 'Unit 10 Using resources', 'life-cycle-assessment', 'L41 · Life Cycle Assessment'),
  (22, 'Unit 10 Using resources', 'npk-fertilisers', 'L42 · (CHEM) NPK fertilisers'),
  (23, 'Unit 10 Using resources', null, 'L43 · Chemical Analysis, Chemistry of the Atmosphere & Using Resources Test  [no subtopic: assessment]'),
  (24, 'Unit 10 Using resources', null, 'L44 · Chemical Analysis, Chemistry of the Atmosphere & Using Resources Test Review  [no subtopic: assessment]'),
  -- Unit 6 The rate and extent of chemical change
  (25, 'Unit 6 The rate and extent of chemical change', 'calculating-rates', 'L45 · Rates of Reaction (Spec point)/Calculating Rates Graphically'),
  (26, 'Unit 6 The rate and extent of chemical change', 'factors-affecting-rate', 'L46 · Factors Affecting Rates'),
  (27, 'Unit 6 The rate and extent of chemical change', 'factors-affecting-rate', 'L47 · Rate of Reaction RP (Measuring the volume of a gas produced)'),
  (28, 'Unit 6 The rate and extent of chemical change', 'factors-affecting-rate', 'L48 · Rate of Reaction RP (Measuring a change in colour or turbidity)'),
  (29, 'Unit 6 The rate and extent of chemical change', 'factors-affecting-rate', 'L49 · Rates RP Application'),
  (30, 'Unit 6 The rate and extent of chemical change', 'catalysts', 'L50 · Catalysts/Reversible Reactions'),
  (31, 'Unit 6 The rate and extent of chemical change', 'effect-of-conditions-equilibrium', 'L51 · The effect of changing conditions at equilibrium  [HT ONLY]'),
  (32, 'Unit 6 The rate and extent of chemical change', 'haber-process', 'L52 · (CHEM) Haber process'),
  (33, 'Unit 6 The rate and extent of chemical change', null, 'L53 · Rates & Equilibrium Test  [no subtopic: assessment]'),
  (34, 'Unit 6 The rate and extent of chemical change', null, 'L54 · Rates & Equilibrium Test Review  [no subtopic: assessment]'),
  -- Unit 2 Bonding, structure, and the properties of matter
  (35, 'Unit 2 Bonding, structure, and the properties of matter', 'covalent-bonding', 'L55 · Covalent Bonding/Dot & Cross Diagrams'),
  (36, 'Unit 2 Bonding, structure, and the properties of matter', 'properties-small-molecules', 'L56 · Properties of Simple Molecules'),
  -- Unit 7 Organic Chemistry
  (37, 'Unit 7 Organic Chemistry', 'crude-oil-hydrocarbons', 'L57 · Crude Oil, Hydrocarbons & Alkanes'),
  (38, 'Unit 7 Organic Chemistry', 'properties-of-hydrocarbons', 'L58 · Properties of Hydrocarbons & Fractional Distillation'),
  (39, 'Unit 7 Organic Chemistry', 'properties-of-hydrocarbons', 'L59 · Combustion'),
  (40, 'Unit 7 Organic Chemistry', 'cracking-alkenes', 'L60 · Cracking'),
  (41, 'Unit 7 Organic Chemistry', 'reactions-of-alkenes', 'L61 · (CHEM) Reactions of Alkenes'),
  (42, 'Unit 7 Organic Chemistry', 'alcohols', 'L62 · (CHEM) Alcohols'),
  (43, 'Unit 7 Organic Chemistry', 'carboxylic-acids', 'L63 · (CHEM) Carboxylic Acids & Esters'),
  (44, 'Unit 7 Organic Chemistry', 'addition-polymerisation', 'L64 · (CHEM) Addition Polymerisation'),
  (45, 'Unit 7 Organic Chemistry', 'condensation-polymerisation', 'L65 · (CHEM) Condensation Polymerisation'),
  (46, 'Unit 7 Organic Chemistry', 'amino-acids', 'L66 · (CHEM) Amino Acids, DNA & Natural Polymers'),
  (47, 'Unit 7 Organic Chemistry', null, 'L67 · Organic & Bonding Test  [no subtopic: assessment]'),
  (48, 'Unit 7 Organic Chemistry', null, 'L68 · Organic & Bonding Test Review  [no subtopic: assessment]')
) as v (academic_week, topic, subtopic, notes);

-- ── Year 10 · Chemistry · foundation — 46 lessons ─────────────────────────
with school as (select id from public.schools where name = 'Rainford High School'),
     subject as (select id from public.subjects where name = 'Chemistry')
insert into public.scheme_of_work_overrides
  (school_id, key_stage, year_group, tier, pathway, subject_id,
   academic_week, topic, subtopic, notes)
select school.id, 'KS4', 10, 'foundation', null, subject.id,
       v.academic_week, v.topic, v.subtopic, v.notes
  from school, subject, (values
  -- Unit 8 Chemical analysis
  (1::smallint, 'Unit 8 Chemical analysis'::text, 'pure-substances'::text, 'L21 · Pure Substances, Formulations & Testing For Gases'::text),
  (2, 'Unit 8 Chemical analysis', 'chromatography', 'L22 · Chromatography RP'),
  (3, 'Unit 8 Chemical analysis', 'chromatography', 'L23 · Chromatography RP 2'),
  (4, 'Unit 8 Chemical analysis', 'flame-tests', 'L24 · (CHEM) Tests for positive ions (Flame Tests) & Flame Emission Spectroscopy'),
  (5, 'Unit 8 Chemical analysis', 'metal-hydroxides', 'L25 · (CHEM) Tests for positive ions (reaction with metal hydroxide)'),
  (6, 'Unit 8 Chemical analysis', 'carbonates-halides-sulfates', 'L26 · (CHEM) Tests for negative ions'),
  (7, 'Unit 8 Chemical analysis', null, 'L27 · (CHEM) Tests for ions RP  [no subtopic: ambiguous]'),
  -- Unit 9 Chemistry of the atmosphere
  (8, 'Unit 9 Chemistry of the atmosphere', 'early-atmosphere', 'L28 · History & Evolution of the Atmosphere'),
  (9, 'Unit 9 Chemistry of the atmosphere', 'greenhouse-gases', 'L29 · Greenhouse Gases / Climate change'),
  (10, 'Unit 9 Chemistry of the atmosphere', 'atmospheric-pollutants', 'L30 · Atmospheric Pollutants & Carbon Footprint'),
  (11, 'Unit 9 Chemistry of the atmosphere', null, 'L31 · Quiz & application  [no subtopic: assessment]'),
  (12, 'Unit 9 Chemistry of the atmosphere', null, 'L32 · (CHEM) Chemical Analysis & Atmosphere Test  [no subtopic: assessment]'),
  (13, 'Unit 9 Chemistry of the atmosphere', null, 'L33 · (CHEM) Chemical Analysis & Atmosphere Test Review  [no subtopic: assessment]'),
  -- Unit 10 Using resources
  (14, 'Unit 10 Using resources', 'earths-resources', 'L34 · Using the Earth''s Resources & Recycling'),
  (15, 'Unit 10 Using resources', 'potable-water', 'L35 · Potable Water RP 1'),
  (16, 'Unit 10 Using resources', 'potable-water', 'L36 · Potable Water RP 2'),
  (17, 'Unit 10 Using resources', 'potable-water', 'L37 · Waste Water Treatment/Evaluate obtaining potable water'),
  (18, 'Unit 10 Using resources', 'corrosion-prevention', 'L39 · (CHEM) Corrosion & Alloys'),
  (19, 'Unit 10 Using resources', 'ceramics-polymers-composites', 'L40 · (CHEM) Ceramics, polymers and composites'),
  (20, 'Unit 10 Using resources', 'life-cycle-assessment', 'L41 · Life Cycle Assessment'),
  (21, 'Unit 10 Using resources', 'npk-fertilisers', 'L42 · (CHEM) NPK fertilisers'),
  (22, 'Unit 10 Using resources', null, 'L43 · Chemical Analysis, Chemistry of the Atmosphere & Using Resources Test  [no subtopic: assessment]'),
  (23, 'Unit 10 Using resources', null, 'L44 · Chemical Analysis, Chemistry of the Atmosphere & Using Resources Test Review  [no subtopic: assessment]'),
  -- Unit 6 The rate and extent of chemical change
  (24, 'Unit 6 The rate and extent of chemical change', 'calculating-rates', 'L45 · Rates of Reaction (Spec point)/Calculating Rates Graphically'),
  (25, 'Unit 6 The rate and extent of chemical change', 'factors-affecting-rate', 'L46 · Factors Affecting Rates'),
  (26, 'Unit 6 The rate and extent of chemical change', 'factors-affecting-rate', 'L47 · Rate of Reaction RP (Measuring the volume of a gas produced)'),
  (27, 'Unit 6 The rate and extent of chemical change', 'factors-affecting-rate', 'L48 · Rate of Reaction RP (Measuring a change in colour or turbidity)'),
  (28, 'Unit 6 The rate and extent of chemical change', 'factors-affecting-rate', 'L49 · Rates RP Application'),
  (29, 'Unit 6 The rate and extent of chemical change', 'catalysts', 'L50 · Catalysts/Reversible Reactions'),
  (30, 'Unit 6 The rate and extent of chemical change', 'haber-process', 'L52 · (CHEM) Haber process'),
  (31, 'Unit 6 The rate and extent of chemical change', null, 'L53 · Rates & Equilibrium Test  [no subtopic: assessment]'),
  (32, 'Unit 6 The rate and extent of chemical change', null, 'L54 · Rates & Equilibrium Test Review  [no subtopic: assessment]'),
  -- Unit 2 Bonding, structure, and the properties of matter
  (33, 'Unit 2 Bonding, structure, and the properties of matter', 'covalent-bonding', 'L55 · Covalent Bonding/Dot & Cross Diagrams'),
  (34, 'Unit 2 Bonding, structure, and the properties of matter', 'properties-small-molecules', 'L56 · Properties of Simple Molecules'),
  -- Unit 7 Organic Chemistry
  (35, 'Unit 7 Organic Chemistry', 'crude-oil-hydrocarbons', 'L57 · Crude Oil, Hydrocarbons & Alkanes'),
  (36, 'Unit 7 Organic Chemistry', 'properties-of-hydrocarbons', 'L58 · Properties of Hydrocarbons & Fractional Distillation'),
  (37, 'Unit 7 Organic Chemistry', 'properties-of-hydrocarbons', 'L59 · Combustion'),
  (38, 'Unit 7 Organic Chemistry', 'cracking-alkenes', 'L60 · Cracking'),
  (39, 'Unit 7 Organic Chemistry', 'reactions-of-alkenes', 'L61 · (CHEM) Reactions of Alkenes'),
  (40, 'Unit 7 Organic Chemistry', 'alcohols', 'L62 · (CHEM) Alcohols'),
  (41, 'Unit 7 Organic Chemistry', 'carboxylic-acids', 'L63 · (CHEM) Carboxylic Acids & Esters'),
  (42, 'Unit 7 Organic Chemistry', 'addition-polymerisation', 'L64 · (CHEM) Addition Polymerisation'),
  (43, 'Unit 7 Organic Chemistry', 'condensation-polymerisation', 'L65 · (CHEM) Condensation Polymerisation'),
  (44, 'Unit 7 Organic Chemistry', 'amino-acids', 'L66 · (CHEM) Amino Acids'),
  (45, 'Unit 7 Organic Chemistry', null, 'L67 · Organic & Bonding Test  [no subtopic: assessment]'),
  (46, 'Unit 7 Organic Chemistry', null, 'L68 · Organic & Bonding Test Review  [no subtopic: assessment]')
) as v (academic_week, topic, subtopic, notes);

-- ── Year 10 · Physics · higher — 47 lessons ─────────────────────────
with school as (select id from public.schools where name = 'Rainford High School'),
     subject as (select id from public.subjects where name = 'Physics')
insert into public.scheme_of_work_overrides
  (school_id, key_stage, year_group, tier, pathway, subject_id,
   academic_week, topic, subtopic, notes)
select school.id, 'KS4', 10, 'higher', null, subject.id,
       v.academic_week, v.topic, v.subtopic, v.notes
  from school, subject, (values
  -- Unit 3 Particle model of matter
  (1::smallint, 'Unit 3 Particle model of matter'::text, 'density-of-materials'::text, 'L18 · Density'::text),
  (2, 'Unit 3 Particle model of matter', 'density-of-materials', 'L19 · Density RP'),
  (3, 'Unit 3 Particle model of matter', 'changes-of-state', 'L20 · Changing states of matter'),
  (4, 'Unit 3 Particle model of matter', 'changes-of-state', 'L21 · Changing states of matter - Investigation'),
  (5, 'Unit 3 Particle model of matter', 'internal-energy', 'L22 · Internal energy'),
  (6, 'Unit 3 Particle model of matter', 'temperature-changes-shc', 'L23 · Specific heat capacity'),
  (7, 'Unit 3 Particle model of matter', 'temperature-changes-shc', 'L24 · Specific heat capacity RP'),
  (8, 'Unit 3 Particle model of matter', 'specific-latent-heat', 'L25 · Specific latent heat'),
  (9, 'Unit 3 Particle model of matter', 'particle-motion-pressure', 'L26 · Particle model and pressure'),
  (10, 'Unit 3 Particle model of matter', 'particle-motion-pressure', 'L27 · (PHYS) Pressure and volume'),
  (11, 'Unit 3 Particle model of matter', null, 'L28 · Particle model of matter Test  [no subtopic: assessment]'),
  (12, 'Unit 3 Particle model of matter', null, 'L29 · Test Review  [no subtopic: assessment]'),
  -- Unit 4 Atomic structure
  (13, 'Unit 4 Atomic structure', 'structure-of-atom', 'L30 · Atoms, isotopes and excited electrons'),
  (14, 'Unit 4 Atomic structure', 'development-atomic-model', 'L31 · History of the atom'),
  (15, 'Unit 4 Atomic structure', 'radioactive-decay', 'L32 · Nuclear radiation'),
  (16, 'Unit 4 Atomic structure', 'radioactive-decay', 'L33 · Alpha, beta and gamma radiation'),
  (17, 'Unit 4 Atomic structure', 'nuclear-equations', 'L34 · Radioactive decay equations'),
  (18, 'Unit 4 Atomic structure', 'half-lives', 'L35 · Half-life'),
  (19, 'Unit 4 Atomic structure', 'half-lives', 'L36 · Half-life 2'),
  (20, 'Unit 4 Atomic structure', 'radioactive-contamination', 'L37 · Dangers and uses of nuclear radiation'),
  (21, 'Unit 4 Atomic structure', 'nuclear-fission', 'L38 · (PHYS) Nuclear fission'),
  (22, 'Unit 4 Atomic structure', 'nuclear-fusion', 'L39 · (PHYS) Nuclear fusion'),
  (23, 'Unit 4 Atomic structure', 'uses-of-nuclear-radiation', 'L40 · (PHYS) Nuclear radiation in medicine'),
  (24, 'Unit 4 Atomic structure', null, 'L41 · Atomic structure Test  [no subtopic: assessment]'),
  (25, 'Unit 4 Atomic structure', null, 'L42 · Test Review  [no subtopic: assessment]'),
  -- Unit 2 Electricity
  (26, 'Unit 2 Electricity', 'circuit-symbols', 'L43 · Circuit symbols and building circuits'),
  (27, 'Unit 2 Electricity', 'electrical-charge-current', 'L44 · Current and Charge'),
  (28, 'Unit 2 Electricity', 'series-parallel-circuits', 'L45 · Series and parallel investigation'),
  (29, 'Unit 2 Electricity', 'series-parallel-circuits', 'L46 · Series Rules'),
  (30, 'Unit 2 Electricity', 'series-parallel-circuits', 'L47 · Parallel Rules'),
  (31, 'Unit 2 Electricity', 'current-resistance-pd', 'L48 · Resistance and Ohms Law'),
  (32, 'Unit 2 Electricity', 'series-parallel-circuits', 'L49 · Resistance in series and parallel RP'),
  (33, 'Unit 2 Electricity', 'current-resistance-pd', 'L50 · Resistance in a wire RP'),
  (34, 'Unit 2 Electricity', 'resistors', 'L51 · IV Characteristics - inc components LDR, thermistors etc'),
  (35, 'Unit 2 Electricity', 'resistors', 'L52 · IV Graphs RP Collect Data'),
  (36, 'Unit 2 Electricity', 'resistors', 'L53 · IV characteristics Review and draw graphs'),
  (37, 'Unit 2 Electricity', 'current-resistance-pd', 'L54 · Harder Ohm''s Law Application'),
  (38, 'Unit 2 Electricity', null, 'L55 · Quiz & application  [no subtopic: assessment]'),
  (39, 'Unit 2 Electricity', 'direct-alternating-pd', 'L56 · AC and DC'),
  (40, 'Unit 2 Electricity', 'mains-electricity', 'L57 · Cables and plugs'),
  (41, 'Unit 2 Electricity', 'power-electricity', 'L58 · Power'),
  (42, 'Unit 2 Electricity', 'energy-transfers-appliances', 'L59 · Energy Transfer'),
  (43, 'Unit 2 Electricity', 'national-grid', 'L60 · National Grid'),
  (44, 'Unit 2 Electricity', 'static-charge', 'L61 · (PHYS) Static Charges'),
  (45, 'Unit 2 Electricity', 'electric-fields', 'L62 · (PHYS) Electric Fields'),
  (46, 'Unit 2 Electricity', null, 'L63 · Electrcity Test  [no subtopic: assessment]'),
  (47, 'Unit 2 Electricity', null, 'L64 · Test Review  [no subtopic: assessment]')
) as v (academic_week, topic, subtopic, notes);

-- ── Year 10 · Physics · foundation — 47 lessons ─────────────────────────
with school as (select id from public.schools where name = 'Rainford High School'),
     subject as (select id from public.subjects where name = 'Physics')
insert into public.scheme_of_work_overrides
  (school_id, key_stage, year_group, tier, pathway, subject_id,
   academic_week, topic, subtopic, notes)
select school.id, 'KS4', 10, 'foundation', null, subject.id,
       v.academic_week, v.topic, v.subtopic, v.notes
  from school, subject, (values
  -- Unit 3 Particle model of matter
  (1::smallint, 'Unit 3 Particle model of matter'::text, 'density-of-materials'::text, 'L18 · Density'::text),
  (2, 'Unit 3 Particle model of matter', 'density-of-materials', 'L19 · Density RP'),
  (3, 'Unit 3 Particle model of matter', 'changes-of-state', 'L20 · Changing states of matter'),
  (4, 'Unit 3 Particle model of matter', 'changes-of-state', 'L21 · Changing states of matter - Investigation'),
  (5, 'Unit 3 Particle model of matter', 'internal-energy', 'L22 · Internal energy'),
  (6, 'Unit 3 Particle model of matter', 'temperature-changes-shc', 'L23 · Specific heat capacity'),
  (7, 'Unit 3 Particle model of matter', 'temperature-changes-shc', 'L24 · Specific heat capacity RP'),
  (8, 'Unit 3 Particle model of matter', 'specific-latent-heat', 'L25 · Specific latent heat'),
  (9, 'Unit 3 Particle model of matter', 'particle-motion-pressure', 'L26 · Particle model and pressure'),
  (10, 'Unit 3 Particle model of matter', 'particle-motion-pressure', 'L27 · (PHYS) Pressure and volume'),
  (11, 'Unit 3 Particle model of matter', null, 'L28 · Particle model of matter Test  [no subtopic: assessment]'),
  (12, 'Unit 3 Particle model of matter', null, 'L29 · Test Review  [no subtopic: assessment]'),
  -- Unit 4 Atomic structure
  (13, 'Unit 4 Atomic structure', 'structure-of-atom', 'L30 · Atoms, isotopes and excited electrons'),
  (14, 'Unit 4 Atomic structure', 'development-atomic-model', 'L31 · History of the atom'),
  (15, 'Unit 4 Atomic structure', 'radioactive-decay', 'L32 · Nuclear radiation'),
  (16, 'Unit 4 Atomic structure', 'radioactive-decay', 'L33 · Alpha, beta and gamma radiation'),
  (17, 'Unit 4 Atomic structure', 'nuclear-equations', 'L34 · Radioactive decay equations'),
  (18, 'Unit 4 Atomic structure', 'half-lives', 'L35 · Half-life'),
  (19, 'Unit 4 Atomic structure', 'half-lives', 'L36 · Half-life 2'),
  (20, 'Unit 4 Atomic structure', 'radioactive-contamination', 'L37 · Dangers and uses of nuclear radiation'),
  (21, 'Unit 4 Atomic structure', 'nuclear-fission', 'L38 · (PHYS) Nuclear fission'),
  (22, 'Unit 4 Atomic structure', 'nuclear-fusion', 'L39 · (PHYS) Nuclear fusion'),
  (23, 'Unit 4 Atomic structure', 'uses-of-nuclear-radiation', 'L40 · (PHYS) Nuclear radiation in medicine'),
  (24, 'Unit 4 Atomic structure', null, 'L41 · Atomic structure Test  [no subtopic: assessment]'),
  (25, 'Unit 4 Atomic structure', null, 'L42 · Test Review  [no subtopic: assessment]'),
  -- Unit 2 Electricity
  (26, 'Unit 2 Electricity', 'circuit-symbols', 'L43 · Circuit symbols and building circuits'),
  (27, 'Unit 2 Electricity', 'electrical-charge-current', 'L44 · Current and Charge'),
  (28, 'Unit 2 Electricity', 'series-parallel-circuits', 'L45 · Series and parallel investigation'),
  (29, 'Unit 2 Electricity', 'series-parallel-circuits', 'L46 · Series Rules'),
  (30, 'Unit 2 Electricity', 'series-parallel-circuits', 'L47 · Parallel Rules'),
  (31, 'Unit 2 Electricity', 'current-resistance-pd', 'L48 · Resistance and Ohms Law'),
  (32, 'Unit 2 Electricity', 'series-parallel-circuits', 'L49 · Resistance in series and parallel RP'),
  (33, 'Unit 2 Electricity', 'current-resistance-pd', 'L50 · Resistance in a wire RP'),
  (34, 'Unit 2 Electricity', 'resistors', 'L51 · IV Characteristics - inc components LDR, thermistors etc'),
  (35, 'Unit 2 Electricity', 'resistors', 'L52 · IV Graphs RP Collect Data'),
  (36, 'Unit 2 Electricity', 'resistors', 'L53 · IV characteristics Review and draw graphs'),
  (37, 'Unit 2 Electricity', 'current-resistance-pd', 'L54 · Extra Ohm''s law'),
  (38, 'Unit 2 Electricity', null, 'L55 · Quiz & application  [no subtopic: assessment]'),
  (39, 'Unit 2 Electricity', 'direct-alternating-pd', 'L56 · AC and DC'),
  (40, 'Unit 2 Electricity', 'mains-electricity', 'L57 · Cables and plugs'),
  (41, 'Unit 2 Electricity', 'power-electricity', 'L58 · Power'),
  (42, 'Unit 2 Electricity', 'energy-transfers-appliances', 'L59 · Energy Transfer'),
  (43, 'Unit 2 Electricity', 'national-grid', 'L60 · National Grid'),
  (44, 'Unit 2 Electricity', 'static-charge', 'L61 · (PHYS) Static Charges'),
  (45, 'Unit 2 Electricity', 'electric-fields', 'L62 · (PHYS) Electric Fields'),
  (46, 'Unit 2 Electricity', null, 'L63 · Electrcity Test  [no subtopic: assessment]'),
  (47, 'Unit 2 Electricity', null, 'L64 · Test Review  [no subtopic: assessment]')
) as v (academic_week, topic, subtopic, notes);

-- ── Year 11 · Biology · higher — 55 lessons ─────────────────────────
with school as (select id from public.schools where name = 'Rainford High School'),
     subject as (select id from public.subjects where name = 'Biology')
insert into public.scheme_of_work_overrides
  (school_id, key_stage, year_group, tier, pathway, subject_id,
   academic_week, topic, subtopic, notes)
select school.id, 'KS4', 11, 'higher', null, subject.id,
       v.academic_week, v.topic, v.subtopic, v.notes
  from school, subject, (values
  -- Unit 7 Ecology
  (1::smallint, 'Unit 7 Ecology'::text, 'food-chains-webs'::text, 'L66 · Food chains'::text),
  (2, 'Unit 7 Ecology', 'trophic-levels', 'L67 · (BIO) Trophic levels & pyramdid of biomass'),
  (3, 'Unit 7 Ecology', 'adaptations', 'L68 · Adaptations (Animal, plant & extremophiles)'),
  (4, 'Unit 7 Ecology', 'population-competition', 'L69 · Competition  & predator prey relationships'),
  (5, 'Unit 7 Ecology', 'carbon-cycle', 'L70 · Carbon cycle'),
  (6, 'Unit 7 Ecology', 'decomposition', 'L71 · (BIO)  Decomposition'),
  (7, 'Unit 7 Ecology', 'decomposition', 'L72 · (BIO) Anaerobic decay & biogas'),
  (8, 'Unit 7 Ecology', 'decomposition', 'L73 · (BIO) Decay RP'),
  (9, 'Unit 7 Ecology', 'decomposition', 'L74 · (BIO) Decay RP 2'),
  (10, 'Unit 7 Ecology', 'water-cycle', 'L75 · Water cycle'),
  (11, 'Unit 7 Ecology', null, 'L76 · Quiz & application  [no subtopic: assessment]'),
  (12, 'Unit 7 Ecology', 'biodiversity', 'L77 · Biodiversity & maintaining biodiversity'),
  (13, 'Unit 7 Ecology', 'land-use', 'L78 · Land use & deforestation'),
  (14, 'Unit 7 Ecology', 'waste-management', 'L79 · Pollution & waste mangement'),
  (15, 'Unit 7 Ecology', 'global-warming', 'L80 · Global warming  (w/ BIO- Impact of environmental change)'),
  (16, 'Unit 7 Ecology', 'factors-affecting-food-security', 'L81 · (BIO) Factors effecting food security & intensive farming'),
  (17, 'Unit 7 Ecology', 'sustainable-fisheries', 'L82 · (BIO) Sustainable fisheries'),
  (18, 'Unit 7 Ecology', 'role-of-biotechnology', 'L83 · (BIO) Mycroprotein'),
  (19, 'Unit 7 Ecology', null, 'L84 · Ecology test  [no subtopic: assessment]'),
  (20, 'Unit 7 Ecology', null, 'L85 · Test review  [no subtopic: assessment]'),
  -- Unit 5 Homeostasis & response
  (21, 'Unit 5 Homeostasis & response', 'homeostasis', 'L86 · Homeostasis'),
  (22, 'Unit 5 Homeostasis & response', 'reflex-actions', 'L87 · Reflex action'),
  (23, 'Unit 5 Homeostasis & response', 'reaction-time', 'L88 · Reaction time RP'),
  (24, 'Unit 5 Homeostasis & response', 'reaction-time', 'L89 · Reaction time RP 2'),
  (25, 'Unit 5 Homeostasis & response', 'the-brain', 'L90 · (BIO) The Brain'),
  (26, 'Unit 5 Homeostasis & response', 'the-eye', 'L91 · (BIO) The Eye'),
  (27, 'Unit 5 Homeostasis & response', 'defects-of-the-eye', 'L92 · (BIO) Problems with the eye'),
  (28, 'Unit 5 Homeostasis & response', 'thermoregulation', 'L93 · (BIO) Thermoregulation'),
  (29, 'Unit 5 Homeostasis & response', 'blood-glucose-diabetes', 'L94 · Blood glucose & diabetes'),
  (30, 'Unit 5 Homeostasis & response', null, 'L95 · (BIO) Removing waste product w/deamination  [no subtopic: absent]'),
  (31, 'Unit 5 Homeostasis & response', null, 'L96 · (BIO) Kidney & ADH  [no subtopic: absent]'),
  (32, 'Unit 5 Homeostasis & response', null, 'L97 · (BIO) Kidney failure  [no subtopic: absent]'),
  (33, 'Unit 5 Homeostasis & response', 'human-reproduction-hormones', 'L98 · Hormones in the menstrual cycle'),
  (34, 'Unit 5 Homeostasis & response', 'contraception-fertility', 'L99 · Contraception & IVF'),
  (35, 'Unit 5 Homeostasis & response', 'endocrine-system', 'L100 · Negative feedback and adrenaline , thyroxine'),
  (36, 'Unit 5 Homeostasis & response', null, 'L101 · Plant Hormones  [no subtopic: absent]'),
  (37, 'Unit 5 Homeostasis & response', null, 'L102 · Growth of seedling RP  [no subtopic: absent]'),
  -- Unit 6 Inheritance, variation & evolution
  (38, 'Unit 6 Inheritance, variation & evolution', null, 'L103 · Growth of seedling RP2  [no subtopic: absent]'),
  (39, 'Unit 6 Inheritance, variation & evolution', null, 'L104 · Homeostasis and response  test  [no subtopic: assessment]'),
  (40, 'Unit 6 Inheritance, variation & evolution', null, 'L105 · Test review  [no subtopic: assessment]'),
  (41, 'Unit 6 Inheritance, variation & evolution', 'sexual-asexual-reproduction', 'L106 · Asexual and sexual reproduction'),
  (42, 'Unit 6 Inheritance, variation & evolution', 'meiosis', 'L107 · Meisosis'),
  (43, 'Unit 6 Inheritance, variation & evolution', 'dna-genome', 'L108 · DNA, Genes & Human Genome Project'),
  (44, 'Unit 6 Inheritance, variation & evolution', 'dna-structure', 'L109 · (BIO) Protein synthesis'),
  (45, 'Unit 6 Inheritance, variation & evolution', 'genetic-inheritance', 'L110 · Genetic inheritance'),
  (46, 'Unit 6 Inheritance, variation & evolution', 'inherited-disorders', 'L111 · Inherited diseases and sex determination'),
  (47, 'Unit 6 Inheritance, variation & evolution', 'understanding-genetics', 'L112 · (BIO) Understanding genetics'),
  (48, 'Unit 6 Inheritance, variation & evolution', 'genetic-engineering', 'L113 · Genetic engineering  & selective breeding'),
  (49, 'Unit 6 Inheritance, variation & evolution', 'cloning', 'L114 · (BIO) Cloning'),
  (50, 'Unit 6 Inheritance, variation & evolution', 'variation', 'L115 · Variation & Evolution'),
  (51, 'Unit 6 Inheritance, variation & evolution', 'theory-of-evolution', 'L116 · (BIO) Theories of evolution & speciation'),
  (52, 'Unit 6 Inheritance, variation & evolution', 'fossils-extinction', 'L117 · Fossils and extinction'),
  (53, 'Unit 6 Inheritance, variation & evolution', 'classification-living-organisms', 'L118 · Classification'),
  (54, 'Unit 6 Inheritance, variation & evolution', null, 'L119 · Inheritance varation & evolution  test  [no subtopic: assessment]'),
  (55, 'Unit 6 Inheritance, variation & evolution', null, 'L120 · Test review  [no subtopic: assessment]')
) as v (academic_week, topic, subtopic, notes);

-- ── Year 11 · Biology · foundation — 54 lessons ─────────────────────────
with school as (select id from public.schools where name = 'Rainford High School'),
     subject as (select id from public.subjects where name = 'Biology')
insert into public.scheme_of_work_overrides
  (school_id, key_stage, year_group, tier, pathway, subject_id,
   academic_week, topic, subtopic, notes)
select school.id, 'KS4', 11, 'foundation', null, subject.id,
       v.academic_week, v.topic, v.subtopic, v.notes
  from school, subject, (values
  -- Unit 7 Ecology
  (1::smallint, 'Unit 7 Ecology'::text, 'food-chains-webs'::text, 'L66 · Food chains'::text),
  (2, 'Unit 7 Ecology', 'trophic-levels', 'L67 · (BIO) Trophic levels & pyramdid of biomass'),
  (3, 'Unit 7 Ecology', 'adaptations', 'L68 · Adaptations (Animal, plant & extremophiles)'),
  (4, 'Unit 7 Ecology', 'population-competition', 'L69 · Competition  & predator prey relationships'),
  (5, 'Unit 7 Ecology', 'carbon-cycle', 'L70 · Carbon cycle'),
  (6, 'Unit 7 Ecology', 'decomposition', 'L71 · (BIO)  Decomposition'),
  (7, 'Unit 7 Ecology', 'decomposition', 'L72 · (BIO) Anaerobic decay & biogas'),
  (8, 'Unit 7 Ecology', 'decomposition', 'L73 · (BIO) Decay RP'),
  (9, 'Unit 7 Ecology', 'decomposition', 'L74 · (BIO) Decay RP 2'),
  (10, 'Unit 7 Ecology', 'water-cycle', 'L75 · Water cycle'),
  (11, 'Unit 7 Ecology', null, 'L76 · Quiz & application  [no subtopic: assessment]'),
  (12, 'Unit 7 Ecology', 'biodiversity', 'L77 · Biodiversity & maintaining biodiversity'),
  (13, 'Unit 7 Ecology', 'land-use', 'L78 · Land use & deforestation'),
  (14, 'Unit 7 Ecology', 'waste-management', 'L79 · Pollution & waste mangement'),
  (15, 'Unit 7 Ecology', 'global-warming', 'L80 · Global warming  (w/ BIO- Impact of environmental change)'),
  (16, 'Unit 7 Ecology', 'factors-affecting-food-security', 'L81 · (BIO) Factors effecting food security & intensive farming'),
  (17, 'Unit 7 Ecology', 'sustainable-fisheries', 'L82 · (BIO) Sustainable fisheries'),
  (18, 'Unit 7 Ecology', 'role-of-biotechnology', 'L83 · (BIO) Mycoprotein'),
  (19, 'Unit 7 Ecology', null, 'L84 · Ecology test  [no subtopic: assessment]'),
  (20, 'Unit 7 Ecology', null, 'L85 · Test review  [no subtopic: assessment]'),
  -- Unit 5 Homeostasis & response
  (21, 'Unit 5 Homeostasis & response', 'homeostasis', 'L86 · Homeostasis'),
  (22, 'Unit 5 Homeostasis & response', 'reflex-actions', 'L87 · Reflex action'),
  (23, 'Unit 5 Homeostasis & response', 'reaction-time', 'L88 · Reaction time RP'),
  (24, 'Unit 5 Homeostasis & response', 'reaction-time', 'L89 · Reaction time RP 2'),
  (25, 'Unit 5 Homeostasis & response', 'the-brain', 'L90 · (BIO) The Brain'),
  (26, 'Unit 5 Homeostasis & response', 'the-eye', 'L91 · (BIO) The Eye'),
  (27, 'Unit 5 Homeostasis & response', 'defects-of-the-eye', 'L92 · (BIO) Problems with the eye'),
  (28, 'Unit 5 Homeostasis & response', 'thermoregulation', 'L93 · (BIO) Thermoregulation'),
  (29, 'Unit 5 Homeostasis & response', 'blood-glucose-diabetes', 'L94 · Blood glucose & diabetes'),
  (30, 'Unit 5 Homeostasis & response', null, 'L95 · (BIO) Removing waste product w/deamination  [no subtopic: absent]'),
  (31, 'Unit 5 Homeostasis & response', null, 'L96 · (BIO) Kidney & ADH  [no subtopic: absent]'),
  (32, 'Unit 5 Homeostasis & response', null, 'L97 · (BIO) Kidney failure  [no subtopic: absent]'),
  (33, 'Unit 5 Homeostasis & response', 'human-reproduction-hormones', 'L98 · Hormones in the menstrual cycle'),
  (34, 'Unit 5 Homeostasis & response', 'contraception-fertility', 'L99 · Contraception'),
  (35, 'Unit 5 Homeostasis & response', null, 'L101 · Plant Hormones  [no subtopic: absent]'),
  (36, 'Unit 5 Homeostasis & response', null, 'L102 · Growth of seedling RP  [no subtopic: absent]'),
  -- Unit 6 Inheritance, variation & evolution
  (37, 'Unit 6 Inheritance, variation & evolution', null, 'L103 · Growth of seedling RP2  [no subtopic: absent]'),
  (38, 'Unit 6 Inheritance, variation & evolution', null, 'L104 · Homeostasis and response  test  [no subtopic: assessment]'),
  (39, 'Unit 6 Inheritance, variation & evolution', null, 'L105 · Test review  [no subtopic: assessment]'),
  (40, 'Unit 6 Inheritance, variation & evolution', 'sexual-asexual-reproduction', 'L106 · Asexual and sexual reproduction'),
  (41, 'Unit 6 Inheritance, variation & evolution', 'meiosis', 'L107 · Meisosis'),
  (42, 'Unit 6 Inheritance, variation & evolution', 'dna-genome', 'L108 · DNA, Genes & Human Genome Project'),
  (43, 'Unit 6 Inheritance, variation & evolution', 'dna-structure', 'L109 · (BIO) Protein synthesis'),
  (44, 'Unit 6 Inheritance, variation & evolution', 'genetic-inheritance', 'L110 · Genetic inheritance'),
  (45, 'Unit 6 Inheritance, variation & evolution', 'inherited-disorders', 'L111 · Inherited diseases and sex determination'),
  (46, 'Unit 6 Inheritance, variation & evolution', 'understanding-genetics', 'L112 · (BIO) Understanding genetics'),
  (47, 'Unit 6 Inheritance, variation & evolution', 'genetic-engineering', 'L113 · Genetic engineering  & selective breeding'),
  (48, 'Unit 6 Inheritance, variation & evolution', 'cloning', 'L114 · (BIO) Cloning'),
  (49, 'Unit 6 Inheritance, variation & evolution', 'variation', 'L115 · Variation & Evolution'),
  (50, 'Unit 6 Inheritance, variation & evolution', 'theory-of-evolution', 'L116 · (BIO) Theories of evolution & speciation'),
  (51, 'Unit 6 Inheritance, variation & evolution', 'fossils-extinction', 'L117 · Fossils and extinction'),
  (52, 'Unit 6 Inheritance, variation & evolution', 'classification-living-organisms', 'L118 · Classification'),
  (53, 'Unit 6 Inheritance, variation & evolution', null, 'L119 · Inheritance varation & evolution  test  [no subtopic: assessment]'),
  (54, 'Unit 6 Inheritance, variation & evolution', null, 'L120 · Test review  [no subtopic: assessment]')
) as v (academic_week, topic, subtopic, notes);

-- ── Year 11 · Chemistry · higher — 44 lessons ─────────────────────────
with school as (select id from public.schools where name = 'Rainford High School'),
     subject as (select id from public.subjects where name = 'Chemistry')
insert into public.scheme_of_work_overrides
  (school_id, key_stage, year_group, tier, pathway, subject_id,
   academic_week, topic, subtopic, notes)
select school.id, 'KS4', 11, 'higher', null, subject.id,
       v.academic_week, v.topic, v.subtopic, v.notes
  from school, subject, (values
  -- Unit 3 Quantitative chemistry
  (1::smallint, 'Unit 3 Quantitative chemistry'::text, 'conservation-of-mass'::text, 'L69 · Balancing Equations/Relative Formula Mass Recap'::text),
  (2, 'Unit 3 Quantitative chemistry', 'moles', 'L70 · Moles [HT ONLY]'),
  (3, 'Unit 3 Quantitative chemistry', 'amounts-in-equations', 'L71 · Amount of substance in equations  [HT ONLY]'),
  (4, 'Unit 3 Quantitative chemistry', 'amounts-in-equations', 'L72 · Masses to balance equations [HT ONLY]'),
  (5, 'Unit 3 Quantitative chemistry', 'using-moles-calculations', 'L73 · Limiting Reactants [HT ONLY]'),
  (6, 'Unit 3 Quantitative chemistry', 'percentage-yield', 'L74 · (CHEM) Percentage Yield'),
  (7, 'Unit 3 Quantitative chemistry', 'atom-economy', 'L75 · (CHEM) Atom Economy'),
  (8, 'Unit 3 Quantitative chemistry', null, 'L76 · (CHEM) Quiz & Application  [no subtopic: assessment]'),
  (9, 'Unit 3 Quantitative chemistry', 'concentration-of-solutions', 'L77 · Concentration of Solutions'),
  (10, 'Unit 3 Quantitative chemistry', 'titrations', 'L78 · (CHEM) Titrations RP 1'),
  (11, 'Unit 3 Quantitative chemistry', 'titrations', 'L79 · (CHEM) Titration RP 2'),
  (12, 'Unit 3 Quantitative chemistry', null, 'L80 · (CHEM) Gas Calculations  [no subtopic: absent]'),
  (13, 'Unit 3 Quantitative chemistry', null, 'L81 · Quantitative Chemistry Test  [no subtopic: assessment]'),
  (14, 'Unit 3 Quantitative chemistry', null, 'L82 · Quantitative Chemistry Test Review  [no subtopic: assessment]'),
  -- Unit 2 Bonding, structure, and the properties of matter
  (15, 'Unit 2 Bonding, structure, and the properties of matter', 'ionic-bonding', 'L83 · Ionic Bonding'),
  (16, 'Unit 2 Bonding, structure, and the properties of matter', 'properties-ionic-compounds', 'L84 · Properties of Ionic Compounds'),
  -- Unit 4 Chemical changes
  (17, 'Unit 4 Chemical changes', 'reactivity-series', 'L85 · Reactions of metals with oxygen and water'),
  (18, 'Unit 4 Chemical changes', 'reactivity-series', 'L86 · The reactivity series'),
  (19, 'Unit 4 Chemical changes', 'extraction-of-metals', 'L87 · Extraction of metals/reduction with carbon'),
  (20, 'Unit 4 Chemical changes', 'oxidation-reduction', 'L88 · Oxidation and reduction (in terms of electrons) [HT ONLY]'),
  (21, 'Unit 4 Chemical changes', 'reactions-of-acids', 'L89 · Reactions of acids and metals/Naming salts/Working out chemical formula'),
  (22, 'Unit 4 Chemical changes', 'reactions-of-acids', 'L90 · Reactions of acids and bases/Ionic Equations'),
  (23, 'Unit 4 Chemical changes', 'reactions-of-acids', 'L91 · Reactions of Acids and metal carbonates/Making Salts RP Theory'),
  (24, 'Unit 4 Chemical changes', 'salts-neutralisation', 'L92 · Making Salts RP'),
  (25, 'Unit 4 Chemical changes', 'ph-scale', 'L93 · pH Scale & Neutralisation'),
  (26, 'Unit 4 Chemical changes', 'strong-weak-acids', 'L94 · Strong & Weak Acids [HT ONLY]'),
  (27, 'Unit 4 Chemical changes', 'electrolysis-molten', 'L95 · Electrolysis of Molten Ionic Compounds'),
  (28, 'Unit 4 Chemical changes', 'half-equations', 'L96 · Electrolysis of Molten Ionic Compounds (Half Equations) [HT ONLY]'),
  (29, 'Unit 4 Chemical changes', 'electrolysis-extraction', 'L97 · Electrolysis of Aluminium Oxide'),
  (30, 'Unit 4 Chemical changes', 'electrolysis-aqueous', 'L98 · Electrolysis of Aqueous Solutions'),
  (31, 'Unit 4 Chemical changes', 'electrolysis-aqueous', 'L99 · Electrolysis of Aqueous Solutions RP'),
  (32, 'Unit 4 Chemical changes', null, 'L100 · Chemical Changes Test  [no subtopic: assessment]'),
  (33, 'Unit 4 Chemical changes', null, 'L101 · Chemical Changes Test Review  [no subtopic: assessment]'),
  -- Unit 5 Energy changes
  (34, 'Unit 5 Energy changes', 'exothermic-endothermic', 'L102 · Exothermic & Endothermic Reactions'),
  (35, 'Unit 5 Energy changes', 'exothermic-endothermic', 'L103 · Exothermic & Endothermic Reactions RP'),
  (36, 'Unit 5 Energy changes', 'reaction-profiles', 'L104 · Reaction Profiles & Catalysts'),
  (37, 'Unit 5 Energy changes', 'bond-energy-calculations', 'L105 · Bond Energy Calculations [HT ONLY]'),
  (38, 'Unit 5 Energy changes', 'cells-and-batteries', 'L106 · (CHEM) Chemical cells and batteries'),
  (39, 'Unit 5 Energy changes', 'fuel-cells', 'L107 · (CHEM) Fuel cells'),
  -- Unit 2 Bonding, structure, and the properties of matter
  (40, 'Unit 2 Bonding, structure, and the properties of matter', 'giant-covalent-structures', 'L108 · Giant Covalent Structures'),
  (41, 'Unit 2 Bonding, structure, and the properties of matter', 'giant-covalent-structures', 'L109 · Graphene & Fullerenes'),
  (42, 'Unit 2 Bonding, structure, and the properties of matter', 'nanoparticles', 'L110 · (CHEM) Nanoparticles'),
  (43, 'Unit 2 Bonding, structure, and the properties of matter', null, 'L111 · Energy Changes & Giant Covalent Test  [no subtopic: assessment]'),
  (44, 'Unit 2 Bonding, structure, and the properties of matter', null, 'L112 · Energy Changes & Giant Covalent Test Review  [no subtopic: assessment]')
) as v (academic_week, topic, subtopic, notes);

-- ── Year 11 · Chemistry · foundation — 36 lessons ─────────────────────────
with school as (select id from public.schools where name = 'Rainford High School'),
     subject as (select id from public.subjects where name = 'Chemistry')
insert into public.scheme_of_work_overrides
  (school_id, key_stage, year_group, tier, pathway, subject_id,
   academic_week, topic, subtopic, notes)
select school.id, 'KS4', 11, 'foundation', null, subject.id,
       v.academic_week, v.topic, v.subtopic, v.notes
  from school, subject, (values
  -- Unit 3 Quantitative chemistry
  (1::smallint, 'Unit 3 Quantitative chemistry'::text, 'conservation-of-mass'::text, 'L69 · Balancing Equations/Relative Formula Mass Recap'::text),
  (2, 'Unit 3 Quantitative chemistry', 'percentage-yield', 'L74 · (CHEM) Percentage Yield'),
  (3, 'Unit 3 Quantitative chemistry', 'atom-economy', 'L75 · (CHEM) Atom Economy'),
  (4, 'Unit 3 Quantitative chemistry', null, 'L76 · (CHEM) Quiz & Application  [no subtopic: assessment]'),
  (5, 'Unit 3 Quantitative chemistry', 'concentration-of-solutions', 'L77 · Concentration of Solutions'),
  (6, 'Unit 3 Quantitative chemistry', 'titrations', 'L78 · (CHEM) Titrations RP 1'),
  (7, 'Unit 3 Quantitative chemistry', 'titrations', 'L79 · (CHEM) Titration RP 2'),
  (8, 'Unit 3 Quantitative chemistry', null, 'L80 · (CHEM) Gas Calculations  [no subtopic: absent]'),
  (9, 'Unit 3 Quantitative chemistry', null, 'L81 · Quantitative Chemistry Test  [no subtopic: assessment]'),
  (10, 'Unit 3 Quantitative chemistry', null, 'L82 · Quantitative Chemistry Test Review  [no subtopic: assessment]'),
  -- Unit 2 Bonding, structure, and the properties of matter
  (11, 'Unit 2 Bonding, structure, and the properties of matter', 'ionic-bonding', 'L83 · Ionic Bonding'),
  (12, 'Unit 2 Bonding, structure, and the properties of matter', 'properties-ionic-compounds', 'L84 · Properties of Ionic Compounds'),
  -- Unit 4 Chemical changes
  (13, 'Unit 4 Chemical changes', 'reactivity-series', 'L85 · Reactions of metals with oxygen and water'),
  (14, 'Unit 4 Chemical changes', 'reactivity-series', 'L86 · The reactivity series'),
  (15, 'Unit 4 Chemical changes', 'extraction-of-metals', 'L87 · Extraction of metals/reduction with carbon'),
  (16, 'Unit 4 Chemical changes', 'reactions-of-acids', 'L89 · Reactions of acids and metals/Naming salts/Working out chemical formula'),
  (17, 'Unit 4 Chemical changes', 'reactions-of-acids', 'L90 · Reactions of acids and bases/Ionic Equations'),
  (18, 'Unit 4 Chemical changes', 'reactions-of-acids', 'L91 · Reactions of Acids and metal carbonates/Making Salts RP Theory'),
  (19, 'Unit 4 Chemical changes', 'salts-neutralisation', 'L92 · Making Salts RP'),
  (20, 'Unit 4 Chemical changes', 'ph-scale', 'L93 · pH Scale & Neutralisation'),
  (21, 'Unit 4 Chemical changes', 'electrolysis-molten', 'L95 · Electrolysis of Molten Ionic Compounds'),
  (22, 'Unit 4 Chemical changes', 'electrolysis-extraction', 'L97 · Electrolysis of Aluminium Oxide'),
  (23, 'Unit 4 Chemical changes', 'electrolysis-aqueous', 'L98 · Electrolysis of Aqueous Solutions'),
  (24, 'Unit 4 Chemical changes', 'electrolysis-aqueous', 'L99 · Electrolysis of Aqueous Solutions RP'),
  (25, 'Unit 4 Chemical changes', null, 'L100 · Chemical Changes Test  [no subtopic: assessment]'),
  (26, 'Unit 4 Chemical changes', null, 'L101 · Chemical Changes Test Review  [no subtopic: assessment]'),
  -- Unit 5 Energy changes
  (27, 'Unit 5 Energy changes', 'exothermic-endothermic', 'L102 · Exothermic & Endothermic Reactions'),
  (28, 'Unit 5 Energy changes', 'exothermic-endothermic', 'L103 · Exothermic & Endothermic Reactions RP'),
  (29, 'Unit 5 Energy changes', 'reaction-profiles', 'L104 · Reaction Profiles & Catalysts'),
  (30, 'Unit 5 Energy changes', 'cells-and-batteries', 'L106 · (CHEM) Chemical cells and batteries'),
  (31, 'Unit 5 Energy changes', 'fuel-cells', 'L107 · (CHEM) Fuel cells'),
  -- Unit 2 Bonding, structure, and the properties of matter
  (32, 'Unit 2 Bonding, structure, and the properties of matter', 'giant-covalent-structures', 'L108 · Giant Covalent Structures'),
  (33, 'Unit 2 Bonding, structure, and the properties of matter', 'giant-covalent-structures', 'L109 · Graphene & Fullerenes'),
  (34, 'Unit 2 Bonding, structure, and the properties of matter', 'nanoparticles', 'L110 · (CHEM) Nanoparticles'),
  (35, 'Unit 2 Bonding, structure, and the properties of matter', null, 'L111 · Energy Changes & Giant Covalent Test  [no subtopic: assessment]'),
  (36, 'Unit 2 Bonding, structure, and the properties of matter', null, 'L112 · Energy Changes & Giant Covalent Test Review  [no subtopic: assessment]')
) as v (academic_week, topic, subtopic, notes);

-- ── Year 11 · Physics · higher — 46 lessons ─────────────────────────
with school as (select id from public.schools where name = 'Rainford High School'),
     subject as (select id from public.subjects where name = 'Physics')
insert into public.scheme_of_work_overrides
  (school_id, key_stage, year_group, tier, pathway, subject_id,
   academic_week, topic, subtopic, notes)
select school.id, 'KS4', 11, 'higher', null, subject.id,
       v.academic_week, v.topic, v.subtopic, v.notes
  from school, subject, (values
  -- Unit 6 Waves
  (1::smallint, 'Unit 6 Waves'::text, 'properties-of-waves'::text, 'L65 · Waves prop'::text),
  (2, 'Unit 6 Waves', 'properties-of-waves', 'L66 · Wave RP'),
  (3, 'Unit 6 Waves', 'properties-em-waves-1', 'L67 · (PHYS) Reflection RP'),
  (4, 'Unit 6 Waves', 'properties-em-waves-1', 'L68 · Refraction RP'),
  (5, 'Unit 6 Waves', 'lenses', 'L69 · (PHYS)Lenses'),
  (6, 'Unit 6 Waves', 'sound-waves-hearing', 'L70 · (PHYS)Sounds and sonar'),
  (7, 'Unit 6 Waves', 'waves-detection-exploration', 'L71 · (PHYS)Ultrasound'),
  (8, 'Unit 6 Waves', 'waves-detection-exploration', 'L72 · (PHYS) Seismic SLOP'),
  (9, 'Unit 6 Waves', 'types-of-em-waves', 'L73 · EM spec and uses'),
  (10, 'Unit 6 Waves', 'infrared-black-bodies', 'L74 · Infrared RP'),
  (11, 'Unit 6 Waves', 'infrared-black-bodies', 'L75 · (PHYS) Black Body'),
  (12, 'Unit 6 Waves', 'uses-em-waves', 'L76 · Communication and high energy'),
  (13, 'Unit 6 Waves', null, 'L77 · Waves Test  [no subtopic: assessment]'),
  (14, 'Unit 6 Waves', null, 'L78 · Test Review  [no subtopic: assessment]'),
  -- Unit 8 Space physics
  (15, 'Unit 8 Space physics', 'red-shift-big-bang', 'L79 · (PHYS) Origin of the universe and red shift'),
  (16, 'Unit 8 Space physics', 'stellar-evolution', 'L80 · (PHYS) Life Cycle of a Star'),
  (17, 'Unit 8 Space physics', 'motion-in-a-circle', 'L81 · (PHYS) Circular Motion'),
  -- Unit 7 Magnetism & electromagnetism
  (18, 'Unit 7 Magnetism & electromagnetism', 'magnetic-fields', 'L82 · Mag fields'),
  (19, 'Unit 7 Magnetism & electromagnetism', 'electromagnetism', 'L83 · Electromagnets and (PHYS) Uses'),
  (20, 'Unit 7 Magnetism & electromagnetism', 'flemings-left-hand-rule', 'L84 · Motor and FLH rule (HT only)'),
  (21, 'Unit 7 Magnetism & electromagnetism', 'electric-motors', 'L85 · F = BIL, SLOP, DC motor (HT only)'),
  (22, 'Unit 7 Magnetism & electromagnetism', 'induced-potential', 'L86 · (PHYS) Generator'),
  (23, 'Unit 7 Magnetism & electromagnetism', 'uses-generator-effect', 'L87 · (PHYS) Alternators and dynamos'),
  (24, 'Unit 7 Magnetism & electromagnetism', 'loudspeakers-headphones', 'L88 · (PHYS) Loudspeakers, microphones and transformers'),
  (25, 'Unit 7 Magnetism & electromagnetism', null, 'L89 · Quiz & application  [no subtopic: assessment]'),
  -- Unit 5 Forces
  (26, 'Unit 5 Forces', 'gravity', 'L90 · Mass and Weight'),
  (27, 'Unit 5 Forces', 'forces-elasticity', 'L91 · Hooke''s law and RP'),
  (28, 'Unit 5 Forces', 'forces-elasticity', 'L92 · Hooke''s Law graph and Qs'),
  (29, 'Unit 5 Forces', 'scalar-vector-quantities', 'L93 · vectors, scalars, forces N1L'),
  (30, 'Unit 5 Forces', 'newtons-laws', 'L94 · N3L'),
  (31, 'Unit 5 Forces', 'resolving-forces', 'L95 · Resolving forces'),
  (32, 'Unit 5 Forces', 'resolving-forces', 'L96 · Parallelogram of forces (HT Only)'),
  (33, 'Unit 5 Forces', 'moments-levers-gears', 'L97 · (PHYS) Moments'),
  (34, 'Unit 5 Forces', 'distance-time-graphs', 'L98 · Speed, distance time graphs'),
  (35, 'Unit 5 Forces', 'distance-speed-velocity', 'L99 · Velocity'),
  (36, 'Unit 5 Forces', 'acceleration', 'L100 · Terminal velocity'),
  (37, 'Unit 5 Forces', 'acceleration', 'L101 · Acceleration'),
  (38, 'Unit 5 Forces', 'newtons-laws', 'L102 · F = ma RP'),
  (39, 'Unit 5 Forces', 'stopping-distance-braking', 'L103 · (PHYS) Braking forces'),
  (40, 'Unit 5 Forces', 'momentum', 'L104 · Momentum'),
  (41, 'Unit 5 Forces', 'momentum', 'L105 · (PHYS) Changing momentum'),
  (42, 'Unit 5 Forces', 'pressure-in-a-fluid', 'L106 · (PHYS) Pressure'),
  (43, 'Unit 5 Forces', 'pressure-in-a-fluid', 'L107 · (PHYS) Atmospheric Pressure'),
  (44, 'Unit 5 Forces', 'pressure-in-a-fluid', 'L108 · (PHYS) Presure in fluids'),
  (45, 'Unit 5 Forces', null, 'L109 · Forces Test  [no subtopic: assessment]'),
  (46, 'Unit 5 Forces', null, 'L110 · Test Review  [no subtopic: assessment]')
) as v (academic_week, topic, subtopic, notes);

-- ── Year 11 · Physics · foundation — 43 lessons ─────────────────────────
with school as (select id from public.schools where name = 'Rainford High School'),
     subject as (select id from public.subjects where name = 'Physics')
insert into public.scheme_of_work_overrides
  (school_id, key_stage, year_group, tier, pathway, subject_id,
   academic_week, topic, subtopic, notes)
select school.id, 'KS4', 11, 'foundation', null, subject.id,
       v.academic_week, v.topic, v.subtopic, v.notes
  from school, subject, (values
  -- Unit 6 Waves
  (1::smallint, 'Unit 6 Waves'::text, 'properties-of-waves'::text, 'L65 · Waves prop'::text),
  (2, 'Unit 6 Waves', 'properties-of-waves', 'L66 · Wave RP'),
  (3, 'Unit 6 Waves', 'properties-em-waves-1', 'L67 · (PHYS) Reflection RP'),
  (4, 'Unit 6 Waves', 'properties-em-waves-1', 'L68 · Refraction RP'),
  (5, 'Unit 6 Waves', 'lenses', 'L69 · (PHYS)Lenses'),
  (6, 'Unit 6 Waves', 'sound-waves-hearing', 'L70 · (PHYS)Sounds and sonar'),
  (7, 'Unit 6 Waves', 'waves-detection-exploration', 'L71 · (PHYS)Ultrasound'),
  (8, 'Unit 6 Waves', 'waves-detection-exploration', 'L72 · (PHYS) Seismic SLOP'),
  (9, 'Unit 6 Waves', 'types-of-em-waves', 'L73 · EM spec and uses'),
  (10, 'Unit 6 Waves', 'infrared-black-bodies', 'L74 · Infrared RP'),
  (11, 'Unit 6 Waves', 'infrared-black-bodies', 'L75 · (PHYS) Black Body'),
  (12, 'Unit 6 Waves', 'uses-em-waves', 'L76 · Communication and high energy'),
  (13, 'Unit 6 Waves', null, 'L77 · Waves Test  [no subtopic: assessment]'),
  (14, 'Unit 6 Waves', null, 'L78 · Test Review  [no subtopic: assessment]'),
  -- Unit 8 Space physics
  (15, 'Unit 8 Space physics', 'red-shift-big-bang', 'L79 · (PHYS) Origin of the universe and red shift'),
  (16, 'Unit 8 Space physics', 'stellar-evolution', 'L80 · (PHYS) Life Cycle of a Star'),
  (17, 'Unit 8 Space physics', 'motion-in-a-circle', 'L81 · (PHYS) Circular Motion'),
  -- Unit 7 Magnetism & electromagnetism
  (18, 'Unit 7 Magnetism & electromagnetism', 'magnetic-fields', 'L82 · Mag fields'),
  (19, 'Unit 7 Magnetism & electromagnetism', 'electromagnetism', 'L83 · Electromagnets'),
  (20, 'Unit 7 Magnetism & electromagnetism', 'induced-potential', 'L86 · (PHYS) Generator'),
  (21, 'Unit 7 Magnetism & electromagnetism', 'uses-generator-effect', 'L87 · (PHYS) Alternators and dynamos'),
  (22, 'Unit 7 Magnetism & electromagnetism', 'loudspeakers-headphones', 'L88 · (PHYS) Loudspeakers, microphones and transformers'),
  (23, 'Unit 7 Magnetism & electromagnetism', null, 'L89 · Quiz & application  [no subtopic: assessment]'),
  -- Unit 5 Forces
  (24, 'Unit 5 Forces', 'gravity', 'L90 · Mass and Weight'),
  (25, 'Unit 5 Forces', 'forces-elasticity', 'L91 · Hooke''s law and RP'),
  (26, 'Unit 5 Forces', 'forces-elasticity', 'L92 · Hooke''s Law graph and Qs'),
  (27, 'Unit 5 Forces', 'scalar-vector-quantities', 'L93 · vectors, scalars, forces N1L'),
  (28, 'Unit 5 Forces', 'newtons-laws', 'L94 · N3L'),
  (29, 'Unit 5 Forces', 'resultant-forces', 'L95 · Resultant forces'),
  (30, 'Unit 5 Forces', 'moments-levers-gears', 'L97 · (PHYS) Moments'),
  (31, 'Unit 5 Forces', 'distance-time-graphs', 'L98 · Spped, distance time graphs'),
  (32, 'Unit 5 Forces', 'distance-speed-velocity', 'L99 · Velocity'),
  (33, 'Unit 5 Forces', 'acceleration', 'L100 · Terminal velocity'),
  (34, 'Unit 5 Forces', 'acceleration', 'L101 · Acceleration'),
  (35, 'Unit 5 Forces', 'newtons-laws', 'L102 · F = ma RP'),
  (36, 'Unit 5 Forces', 'stopping-distance-braking', 'L103 · (PHYS) Braking forces'),
  (37, 'Unit 5 Forces', 'momentum', 'L104 · Momentum'),
  (38, 'Unit 5 Forces', 'momentum', 'L105 · (PHYS) Changing momentum'),
  (39, 'Unit 5 Forces', 'pressure-in-a-fluid', 'L106 · (PHYS) Pressure'),
  (40, 'Unit 5 Forces', 'pressure-in-a-fluid', 'L107 · (PHYS) Atmospheric Pressure'),
  (41, 'Unit 5 Forces', 'pressure-in-a-fluid', 'L108 · (PHYS) Presure in fluids'),
  (42, 'Unit 5 Forces', null, 'L109 · Forces Test  [no subtopic: assessment]'),
  (43, 'Unit 5 Forces', null, 'L110 · Test Review  [no subtopic: assessment]')
) as v (academic_week, topic, subtopic, notes);

commit;


-- ═══════════════════════════════════════════════════════════════════════
-- ⚠️ UNMAPPED — 60 distinct lessons with subtopic = NULL.
-- ═══════════════════════════════════════════════════════════════════════
--
-- These rows ARE in the table. They hold Rainford's real teaching order
-- and their verbatim titles; only `subtopic` is NULL, because no
-- platform page honestly corresponds. Nothing here was guessed at: a
-- wrong slug points a teacher at the wrong lesson and says nothing
-- about it, which is worse than a gap that names itself.
--
-- By reason:
--
--   assessment   50
--   absent        8
--   ambiguous     2
--
-- Full list — year, subject, Rainford's own lesson number, verbatim
-- text, and the tier column(s) it was written in:
--
--   ── Year 9 · Biology ──
--     L10   H+F [assessment]  Quiz & application
--     L18   H+F [assessment]  Cell biology test
--     L19   H+F [assessment]  Test review
--
--   ── Year 9 · Chemistry ──
--     L10   H+F [assessment]  Quiz & application
--     L19   H+F [assessment]  Atomic Structure & Periodic Table Test
--     L20   H+F [assessment]  Test Review
--
--   ── Year 9 · Physics ──
--     L8    H+F [assessment]  Quiz & application
--     L16   H+F [assessment]  Energy Test
--     L17   H+F [assessment]  Test Review
--
--   ── Year 10 · Biology ──
--     L28   H+F [assessment]  Quiz & application
--     L32   H+F [absent]  Breathing & gas exchange
--            ↳ AQA 4.2.2.3 "the lungs" — breathing and alveolar gas exchange. No platform subtopic covers it; the nearest, transport-in-cells, is cell-level exchange, not the ventilation system.
--     L34   H+F [ambiguous]  Transport in plants
--            ↳ names neither platform title. "Transport in plants" is transpiration AND translocation in equal measure, and picking one would silently hide the other.
--     L35   H+F [assessment]  Organisation test
--     L36   H+F [assessment]  Test review
--     L50   H+F [assessment]  Infection & response test
--     L60   H+F [assessment]  Bioenergetics test
--     L61   H+F [assessment]  Test review
--
--   ── Year 10 · Chemistry ──
--     L27   H+F [ambiguous]  (CHEM) Tests for ions RP
--            ↳ the AQA required practical "identification of ions by chemical and spectroscopic means" spans flame-tests, metal-hydroxides and carbonates-halides-sulfates equally. No one of the three is the lesson.
--     L31   H+F [assessment]  Quiz & application
--     L32   H+F [assessment]  (CHEM) Chemical Analysis & Atmosphere Test
--     L33   H+F [assessment]  (CHEM) Chemical Analysis & Atmosphere Test Review
--     L43   H+F [assessment]  Chemical Analysis, Chemistry of the Atmosphere & Using Resources Test
--     L44   H+F [assessment]  Chemical Analysis, Chemistry of the Atmosphere & Using Resources Test Review
--     L53   H+F [assessment]  Rates & Equilibrium Test
--     L54   H+F [assessment]  Rates & Equilibrium Test Review
--     L67   H+F [assessment]  Organic & Bonding Test
--     L68   H+F [assessment]  Organic & Bonding Test Review
--
--   ── Year 10 · Physics ──
--     L28   H+F [assessment]  Particle model of matter Test
--     L29   H+F [assessment]  Test Review
--     L41   H+F [assessment]  Atomic structure Test
--     L42   H+F [assessment]  Test Review
--     L55   H+F [assessment]  Quiz & application
--     L63   H+F [assessment]  Electrcity Test
--     L64   H+F [assessment]  Test Review
--
--   ── Year 11 · Biology ──
--     L76   H+F [assessment]  Quiz & application
--     L84   H+F [assessment]  Ecology test
--     L85   H+F [assessment]  Test review
--     L95   H+F [absent]  (BIO) Removing waste product w/deamination
--            ↳ AQA 4.5.3.4 "maintaining water and nitrogen balance" — deamination and urea. Only metabolism mentions deamination in passing; there is no excretion page.
--     L96   H+F [absent]  (BIO) Kidney & ADH
--            ↳ AQA 4.5.3.4 — the kidney, nephron and ADH. No platform subtopic; endocrine-system names ADH only as a hormone.
--     L97   H+F [absent]  (BIO) Kidney failure
--            ↳ AQA 4.5.3.4 — kidney failure, dialysis and transplant. No platform subtopic.
--     L101  H+F [absent]  Plant Hormones
--            ↳ AQA 4.5.4 "plant hormones" — auxin, phototropism, gravitropism. No platform subtopic mentions any of the three.
--     L102  H+F [absent]  Growth of seedling RP
--            ↳ AQA 4.5.4 RP "the effect of light or gravity on seedling growth". No platform subtopic; it belongs to the missing plant-hormones page.
--     L103  H+F [absent]  Growth of seedling RP2
--            ↳ AQA 4.5.4 RP, second period. Same gap as the lesson before it.
--     L104  H+F [assessment]  Homeostasis and response  test
--     L105  H+F [assessment]  Test review
--     L119  H+F [assessment]  Inheritance varation & evolution  test
--     L120  H+F [assessment]  Test review
--
--   ── Year 11 · Chemistry ──
--     L76   H+F [assessment]  (CHEM) Quiz & Application
--     L80   H+F [absent]  (CHEM) Gas Calculations
--            ↳ AQA 4.3.4.3 "use of amount of substance in relation to volumes of gases" — the molar gas volume, 24 dm3. No platform subtopic mentions it; the quantitative topic's ten pages stop at concentration.
--     L81   H+F [assessment]  Quantitative Chemistry Test
--     L82   H+F [assessment]  Quantitative Chemistry Test Review
--     L100  H+F [assessment]  Chemical Changes Test
--     L101  H+F [assessment]  Chemical Changes Test Review
--     L111  H+F [assessment]  Energy Changes & Giant Covalent Test
--     L112  H+F [assessment]  Energy Changes & Giant Covalent Test Review
--
--   ── Year 11 · Physics ──
--     L77   H+F [assessment]  Waves Test
--     L78   H+F [assessment]  Test Review
--     L89   H+F [assessment]  Quiz & application
--     L109  H+F [assessment]  Forces Test
--     L110  H+F [assessment]  Test Review
--
-- ═══════════════════════════════════════════════════════════════════════
