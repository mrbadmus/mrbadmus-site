# Lean lessons: the plan and where we're up to

**Every Code or Design session working on lessons reads this file first, then
`LEAN-STANDARD.md`, and updates the progress log at the bottom before it finishes.**

Live copy: `docs/lessons/LEAN-PLAN.md` in the mrbadmus-site repo (the pilot
session puts it there). Copies also live in `~/Desktop/MrBadmus AI/Lesson standard/`
and in the Mr Badmus AI project (`claude/lean-lesson-plan.md`); the platform chat
keeps those in step after each report. If they differ, the repo copy wins.

## What we're doing

Pupils said the lessons are too wordy and sound like AI. Every KS3 and GCSE lesson
is being rebuilt to Mide's standard (`docs/lessons/LEAN-STANDARD.md`, also saved as
the `mrbadmus-lean-lessons` skill): curriculum check before and after, Start here
question, 3–4 key words, Key knowledge as tap cards and reveal tables, a Key fact
that carries the science, plain rungs, Dive deeper, no embedded sims, a plain
teacher's voice.

## Where everything is

| What | Where |
|---|---|
| The standard | `docs/lessons/LEAN-STANDARD.md` (repo) |
| This plan | `docs/lessons/LEAN-PLAN.md` (repo) |
| KS3 scheme of work + national curriculum sheet | `~/Desktop/MrBadmus AI/Curriculum/Rainford Scheme of Work/Ks3 SOW 25-26 (NEW).xlsx` |
| KS4 scheme of work + LO sheets | `~/Desktop/MrBadmus AI/Curriculum/Rainford Scheme of Work/NEW Ks4 SOW.xlsx` |
| AQA specs (8464 Combined, 8461/2/3 Triple) | `~/Desktop/MrBadmus AI/Curriculum/AQA/` |
| Per-lesson curriculum tables | `docs/lessons/<wave>/<lesson>.md` |
| Sims shortlist for Mide | `docs/lessons/SIMS-SHORTLIST.html` |
| KS3 lesson pages | `mrbadmus_site/ks3/<subject>/<topic>/` (185 lessons) |
| GCSE lesson pages | `mrbadmus_site/{combined,triple}/{foundation,higher}/...` (264 subtopics, 876 route pages) |

Never commit the curriculum files: the repo is public.

## The order

Rule: rebuild what Rainford pupils are being taught now first, then what they reach
next, so every lesson is ready before a class gets to it. GCSE Year 11 comes first
in each wave because it's their exam year. Unit order comes from the two schemes
of work.

**Wave 0: pilot (sets the pattern)**
- KS3 Breathing and gas exchange (5 lessons)
- GCSE Physics Unit 1 Energy, all routes
- Build the shared pieces once: tap cards, reveal table, Dive deeper, "Try it" sim link,
  plain rung labels
- Sims shortlist page for Mide

**Wave 1: autumn units (being taught now)**
- First: Year 11 Physics Unit 7 Magnetism and electromagnetism (moved up from Wave 2 on 12 Nov 2026: Mide teaches it to Year 11 on Monday 16 Nov)
- Year 11: Biology Unit 7 Ecology · Chemistry Unit 3 Quantitative chemistry · Physics Unit 6 Waves
- Year 10: Biology Unit 2 Organisation · Chemistry Unit 8 Chemical analysis · Physics Unit 3 Particle model of matter
- Year 9: Biology Unit 1 Cell biology · Chemistry Unit 1 Atomic structure and the periodic table
- Year 8 KS3: Bio 4 Bioenergetics (photosynthesis, respiration) · Chem 4 Atoms, elements and compounds · Phys 4 Energy
- Year 7 KS3: Bio 1 Cells and organisation · Chem 1 States of matter · Phys 1 Forces and motion

**Wave 2: next units (spring term)**
- Year 11: Chemistry Unit 2 Bonding, structure and properties · Physics Unit 8 Space · Chemistry Unit 4 Chemical changes
- Year 10: Chemistry Unit 9 Atmosphere · Physics Unit 4 Atomic structure · Chemistry Unit 10 Using resources · Biology Unit 3 Infection and response
- Year 8 KS3: Bio 5 Genetics and evolution · Chem 5 Acids and alkalis · Phys 5 Waves
- Year 7 KS3: Bio 2 Diet and digestion · Chem 2 Chemical reactions · Phys 2 Electricity and magnetism

**Wave 3: the rest of the schemes of work, in order**
- Year 11: Biology Unit 5 Homeostasis and response · Physics Unit 5 Forces · Chemistry Unit 5 Energy changes · Biology Unit 6 Inheritance, variation and evolution
- Year 10: Chemistry Unit 6 Rates · Physics Unit 2 Electricity · Biology Unit 4 Bioenergetics · Chemistry Unit 7 Organic chemistry
- Year 9 KS3: Bio 7 Health and disease · Chem 7 Rate of reaction · Phys 7 Exploring space
- Year 8 KS3: Bio 6 Ecosystems · Chem 6 Earth and atmosphere · Phys 6 Energy in matter
- Year 7 KS3: Bio 3 Reproduction · Chem 3 Materials · Phys 3 Space

**Wave 4: anything left** (site lessons not in either scheme of work, Triple-only
extras), checked against the AQA spec.

Mide can reorder any of this. If a class is further on than the plan assumes,
move their units up.

## How a batch runs

1. Read this plan and the standard. Take the next unit(s) marked "to do" in the
   current wave, about one unit per session (the pilot will set the real pace).
2. For each lesson: curriculum table first, then rewrite, then tick it off line by line.
3. Pages still in the old pre-Design format (capital-letter headings, emojis, no
   Start here) are rebuilt into the new shape, not just trimmed.
4. Opus examiner pass on the science; independent pupil walk at 390 px on every route.
5. Keep question IDs (`docs/b2c/LESSON-DEPENDENCIES.md`). Run `tools/lean_id_map.py`
   (writes `docs/lessons/<wave>/ID-MAP-*.json` and `docs/b2c/id-maps/<unit>.json`), then
   `tools/lesson_contract_check.py --unit <unit>` static and `--drive`: both must say SAFE.
   Push the backend's `knowledge-points.json` before the site if any tag changed.
6. Push, check live, then update the progress log below and commit it.
7. List anything the standard didn't cover, so the platform chat can add it.

Design batches (new KS4 lessons) follow the same standard and the same curriculum check.

## Progress log

| Date | Session | What | Status | Live check |
|---|---|---|---|---|
| 8 Nov 2026 | Platform chat | Standard agreed with Mide; plan written | Done | n/a |
| 11 Nov 2026 | Pilot (Code) | Wave 0. Shared pieces built once (`lean_blocks.py`, `shared/lean.css`, `shared/lean.js`): tap cards, reveal table, Key fact, Dive deeper, "Try it" link, plain "Rung 1–4". KS3 B4 Breathing and gas exchange (5 lessons) and GCSE Physics Energy (8 lessons × 4 routes = 32 pages) rebuilt; embedded sims removed. Words on the 13 lessons: 11,500 → 6,273 (−45%). Curriculum tables in `docs/lessons/pilot/`. Question IDs kept; retired activities listed as null in `docs/b2c/id-maps/B4.json` and `physics-energy.json`; 96 new questions tagged (backend `knowledge-points.json`). Site 872e1dd97, backend 0e39677 | Done | `check_ks3_live.sh B4` all 5 live on this build's assets; `check_ks4_live.py --batch batch-lean` all 32 byte-for-byte; lean.css/lean.js stamps match the commit |
| | Pace | About one unit per session. A KS3 unit of 5 lessons or a GCSE topic of ~8 lessons × 4 routes, with its curriculum tables, examiner pass, pupil walk, id map and the full push guard, fills a session. The push guard alone is ~2 hours when the saved-answers drive has to re-run. Two small KS3 units together is the most to try. | | |
| 13 Nov 2026 | Lean Wave 1 KS3 (Code) | Unit 1, Y8 Bio 4 Bioenergetics: 8 lessons rebuilt (photosynthesis reaction, leaves, starch test; aerobic, why every cell respires, anaerobic in humans, fermentation, aerobic vs anaerobic). "Why almost all life depends on it" HELD: its stored Rung 2 options carry spaced dashes the option-label rule refuses; needs a production ladder reload (record parked in `docs/lessons/wave1/held/`). B4 exercise-asthma-and-smoking: brain-stem line removed. Words on the 8 pages: 14,901 → 8,658 (−42%). Tables in `docs/lessons/wave1/`. Question IDs kept; ID maps `docs/b2c/id-maps/B7.json`, `B8.json`. Blind key pass 27/27 agree. Stored options/keys left as they are (export gate) and listed for Mide. Site 6a87b04d9d | Done | `check_ks3_live.sh B7 B8 B4` all 14 live on this build's assets; text spot-checked |
| 13 Nov 2026 | Lean Wave 1 GCSE (Code) | Unit 1, Y11 Physics Unit 7 Magnetism and electromagnetism: 10 lessons, 21 pages (poles, magnetic fields, electromagnetism on all four routes; Fleming's rule and motors on Higher; loudspeakers, induced p.d., generators, microphones, transformers on Triple Higher). Spec faults fixed: "RP21" removed (not an AQA required practical); magnetic materials, attraction-only, induced magnets losing magnetism, compass as evidence of a magnetic core added; neutral points and horseshoe fields out. 17 new figures (`figlib/ks4lean_mag.py`). Examiner pass, blind key pass 154/154 agree, pupil walk 21/21 at 390 px. Words (teaching text, Triple Higher): 8,509 → 5,648 (−34%), plus 954 in Dive deeper. Tables in `docs/lessons/wave1/`. Question IDs kept (606 kept, 206 added, 49 removed); ID map `docs/b2c/id-maps/physics-magnetism.json`; new questions tagged (backend f23451f). Site 0a770f6afc | Done | `check_ks4_live.py --batch batch-lean` all 53 byte-for-byte; asset stamps match |
