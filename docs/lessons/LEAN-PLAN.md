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
| 13 Nov 2026 | Lean Wave 1 GCSE (Code) | Unit 1, Y11 Physics Unit 7 Magnetism and electromagnetism: 10 lessons, 21 pages (poles, magnetic fields, electromagnetism on all four routes; Fleming's rule and motors on Higher; loudspeakers, induced p.d., generators, microphones, transformers on Triple Higher). Spec faults fixed: "RP21" removed (not an AQA required practical); magnetic materials, attraction-only, induced magnets losing magnetism, compass as evidence of a magnetic core added; neutral points and horseshoe fields out. 17 new figures (`figlib/ks4lean_mag.py`). Examiner pass, blind key pass 131 questions plus 23 re-checked after fixes, 0 disagreements, pupil walk 21/21 at 390 px. Words (teaching text, Triple Higher): 8,509 → 5,648 (−34%), plus 954 in Dive deeper. Tables in `docs/lessons/wave1/`. Question IDs kept (606 kept, 206 added, 49 removed); ID map `docs/b2c/id-maps/physics-magnetism.json`; new questions tagged (backend f23451f). Site 0a770f6afc | Done | `check_ks4_live.py --batch batch-lean` all 53 byte-for-byte; asset stamps match |
| 15 Nov 2026 | Lean Wave 1 GCSE (Code) | Unit 2, Biology Ecology: 23 lessons, 75 pages across the four routes. 15 Design lessons rebuilt as lean records that keep their ladder and practice set; 8 older lessons (biodiversity, waste management, land use, global warming, carbon cycle, water cycle, decomposition, food security) rebuilt in full and replacing their old pages. Nine new figures (`figlib/ks4lean_eco.py`). Examiner pass and blind second key pass; pupil walk at 390 px. Words (teaching text, Triple Higher): 14,638 → 12,352 (−16%), plus 2,027 in Dive deeper; three lessons grew where spec points were missing (ecosystems, population and competition, sampling). Tables in `docs/lessons/wave1/`. Question IDs kept (2,166 kept, 90 added, 1,072 removed); ID map `docs/b2c/id-maps/biology-ecology.json`; new questions tagged (backend 35dcf1f). Bank question `ks4-food-chains-webs-h13` reworded so it no longer describes a diagram, loaded to production, and taken off the family exclusions (backend 214ffbe). Contract check: the open "Your turn" tab after a reload is no longer compared (Mide's ruling, 14 Nov). Site b0f107eee3 | Done | `check_ks4_live.py --batch batch-lean` all 128 byte-for-byte; asset stamps match |
| 17 Nov 2026 | Lean Wave 1 GCSE (Code) | Unit 3, Chemistry Quantitative chemistry: 11 lessons, 31 pages across the four routes (conservation of mass, mass changes, chemical measurements, relative formula mass, concentration on all routes; moles, amounts in equations, using moles on Higher; percentage yield and atom economy on Triple; new Triple Higher lesson **Volumes of gases** (4.3.5), with its 12 bank questions loaded to production). Mide's 16 Nov rulings applied: the 24 dm³ corner on the triangle, with 24 000 cm³ noted once; water is a liquid at room temperature; Moles trimmed; CFIFA spelled out at the first worked example; the ladder question that repeated practice Q1 replaced. Examiner pass and blind second key pass (gas volumes 29/29); pupil walk at 390 px. Words (teaching text, Triple Higher, the 10 existing lessons): 7,107 → 6,834 (−4%); Volumes of gases adds 843. Tables in `docs/lessons/wave1/`. Question IDs kept (923 kept, 63 added, 345 removed); ID map `docs/b2c/id-maps/chemistry-quantitative.json`; new questions tagged and the gas-volumes subtopic added to the curriculum tree (backend fbceb16). Bank question `ks4-testing-for-gases-h16` (a 4.3.5 gas-volume question wrongly served to Combined Foundation) rewritten as the hydrogen squeaky-pop test and reloaded to production (backend 34036a5). Five Chemistry figures still use their old drawings; the redraws follow with the Ecology figures. Pushed together with the KS3 quiz batch (lean/ks3-quiz-batch 7efa5213f5), because each side's frozen-window guard needed the other's production rows. Site 60148d81c3 | Done | `check_ks4_live.py --batch batch-lean` all 159 byte-for-byte; asset stamps match; the 35 quantitative files and option-label.js md5-match live |
| 17 Nov 2026 | Lean Wave 1 GCSE (Code) | Figures and a live fix. Ecology's 11 older drawings and Quantitative's 5 (measurement number line, volume apparatus, open and sealed flasks, mole-ratio bars, one-mole masses) redrawn as lean figures (`figlib/ks4lean_ecofig.py`, `figlib/ks4lean_chemfig.py`); 52 placements open and fit at 390 px. **Live fix:** on every lean page a chemical formula stopped at its first subscript ("CaCO₃(s) → CaO(s) + CO₂(g)" read "CaCO"), because the runtime's redraw removed the pieces the subscript script had added. `ks4_lessons/batch5_ext.js` now puts the formula back together after a redraw; batch-5 pages share the file and change by stamp only (batches 4–11 compared before and after: no formula text changes). `lean_pilot_drive.py` gains a check that fails on any formula line shorter than its source (red on the old script, green on the fix). Site 31bb79149d | Done | `check_ks4_live.py` batch-lean 159 and batch-5 42 byte-for-byte; both scripts md5-match live; live browser check on 5 Quantitative pages: 87 formula lines, 0 cut |
| 14 Nov 2026 | Lean Wave 1 KS3 (Code) | Unit 2, Y8 Chem 4 Atoms, elements and compounds (C2): 6 lessons rebuilt (the atom, elements, compounds, chemical symbols, formulae, conservation of mass). Benches replaced by drawn figures (`ks3_art/c2.py`: particle-boxes, open-sealed-flask). Words on the 6 pages: 10,259 → 6,732 (−34%). Tables in `docs/lessons/wave1/`. Blind key pass 18/18 agree; examiner pass and 390 px pupil walk fixes applied. Question IDs kept; 35 retired as null in `docs/b2c/id-maps/C2.json` (the Think first commits and where-the-model-runs-out are not drawn; `lean_id_map` now marks a KS3 id removed when the built page never mentions it). Stored options/keys left as they are (export gate) and listed for Mide. SOW gap: no Chem 4 row for conservation of mass. Site 0d26f0f4cb | Done | `check_ks3_live.sh C2` all 6 live on this build's assets; text spot-checked |
| 14 Nov 2026 | Lean Wave 1 KS3 (Code) | Unit 3, Y8 Phys 4 Energy: 9 lessons rebuilt. P1 energy stores, conservation of energy, energy transfers before and after, simple machines (the four heating lessons belong to Phys 6 and stay classic); P2 energy in food, power ratings, calculating energy transferred, reading a fuel bill, fuels and energy resources. 15 benches replaced by drawn figures (`ks3_art/p1.py`: formula-triangle, store-bars, sankey, lever-trade; `ks3_art/p2.py`: fossil-fuel-formation). Words on the 9 pages: 15,102 → 10,341 (−32%; fuels grew 1,167 → 1,474 to cover fossil-fuel formation and renewables). Tables in `docs/lessons/wave1/`. Blind key pass 27/27 agree; examiner pass and 390 px pupil walk fixes applied. Question IDs kept; ID maps `docs/b2c/id-maps/P1.json` (18 retired) and `P2.json` (19 retired, incl. the calorimeter's per-run rows). Save-drive cases on the retired benches proved retired; the pupil and slider cases moved to live pages. Stored options/keys left as they are and listed for Mide. SOW gaps: 10a work done and 11b efficiency have no own page; energy in food has no Phys 4 row; calculating energy has no SOW row. Site 14d40d3dea | Done | `check_ks3_live.sh P1 P2 C2` all 19 live on this build's assets; text spot-checked |
| 14 Nov 2026 | Lean Wave 1 KS3 (Code) | Unit 6 (taken before 4 and 5, which are blocked), Y7 Phys 1 Forces and motion, subset: 4 lessons rebuilt (what a force is, drawing and adding forces, friction in P4; speed in P3). Held classic because gates use them as their sample page: mass vs weight, distance-time graphs, moments. Benches replaced by drawn figures (`ks3_art/p4.py`: force-arrows, newtonmeter). The 1060 px resultant beam was dropped from the lean page (it overflowed a phone). Words on the 4 pages: 7,767 → 5,047 (−35%). Tables in `docs/lessons/wave1/`. Blind key pass 12/12 agree; examiner pass and 390 px pupil walk fixes applied; QUESTION-AUDIT friction produce fixed. Question IDs kept; ID maps `docs/b2c/id-maps/P3.json` (4 retired) and `P4.json` (9 retired). Stored options/keys left as they are and listed for Mide. SOW gaps: weight (9b) is on the held mass-vs-weight page; Hooke's law has no SOW row. Units 4 (B1 Cells) and 5 (C1 Particles) are built on branches `lean/ks3-wave1-p4` and `lean/ks3-wave1-c1`, unpushed, waiting on gate rulings from Mide. Site 6d05dc72e6 | Done | `check_ks3_live.sh P3 P4` all 12 live on this build's assets; text spot-checked |
| 16 Nov 2026 | Lean Wave 1 KS3 (Code) | Unit 4, Y7 Bio 1 Cells and organisation (B1): 5 lessons rebuilt (using a microscope, animal and plant cells, specialised cells, levels of organisation, unicellular organisms); life-processes held for the quiz batch. Words on the 5 pages: 8,135 → 4,163 (−49%). Tables in `docs/lessons/wave1/`. verify_ks3's classic-shape checks now read the hidden fixture once a lesson is lean (2e046eeec4). Question IDs kept; ID map `docs/b2c/id-maps/B1.json`. Site 74153226f8 | Done | `check_ks3_live.sh B1` live on this build's assets; pages byte-compared with the build |
| 16 Nov 2026 | Lean Wave 1 KS3 (Code) | Unit 5, Y7 Chem 1 Particles and their behaviour (C1): 6 lessons rebuilt (particle model, solids liquids and gases, changes of state, gas pressure, diffusion, testing the model). Benches replaced by drawn figures; every new figure record carries a caption (MRB-254) with the page captions unchanged. Words on the 6 pages: 6,760 → 3,994 (−41%). Tables in `docs/lessons/wave1/`. Question IDs kept; ID map `docs/b2c/id-maps/C1.json` (27 retired). Site a74f9b2834 | Done | `check_ks3_live.sh C1` live on this build's assets; pages byte-compared with the build |
| 16–17 Nov 2026 | Lean Wave 1 KS3 (Code) | Quiz batch: Mide's approved option wording for B1, B7, B8, C1, C2, P1, P2, P4, P6, P7 and P12 (207 edits: 96 ladder options, 51 page-text, 16 stems, plus feedback and bank text), loaded to production with Mide's go-ahead (TEST first; frozen-window snapshot before, re-check after; only p12-06-s01/s02 feedback differs, as ruled). Production after the load: `ks3_assignment_bank` 16,946, `ks3_ladder_questions` 370, `ks3_cards` 869, all equal to Python. Backend knowledge points first (a090839, 46 KS3 keys). life-processes and why-almost-all-life-depends-on-it became lean (words 2,830 → 1,495, −47%). Landed in one combined push with GCSE Chemistry, because each unit's frozen-window gate needed the other's rows. Site 60148d81c3 | Done | `check_ks3_live.sh` 71/71 live on this build's assets; every KS3 page byte-compared with the build |
| 17 Nov 2026 | Lean Wave 1 KS3 (Code) | Unit 6 completed, Y7 Phys 1 Forces and motion: the three held lessons rebuilt (distance-time graphs in P3, moments in P4, mass vs weight in P12). Moments follows the Rainford KS3 scheme of work (row 12b), so the principle of moments is taught with a CFIFA worked example on a drawn seesaw (`ks3_art/p4.py`: an unknown distance is drawn to scale and labelled "? m"); the curriculum table says which line was followed. Retired widgets listed in `ks3_instrument_liveness.py` (graph-plot, journey-match, spanner-rig). Words on the 3 pages: 3,675 → 2,450 (−33%; distance-time graphs 733 → 753). Question IDs kept; ID maps `docs/b2c/id-maps/P3.json`, `P4.json` and new `P12.json`. Moments Rung 2 option wording ruled by Mide and queued for the next quiz batch (`docs/lessons/wave1/QUIZ-BATCH-NEXT.md`). Site c00e2674c8 | Done | `check_ks3_live.sh P3 P4 P12` all 18 live on this build's assets; the three physics folders byte-compared with the build |
| 17 Nov 2026 | Lean Wave 1 KS3 (Code) | Lean lesson check, two KS3 rules from Mide (16 Nov): Start here is the first block, and Easy mistakes names every misconception the lesson declares (each pair may carry the id; it renders as `data-misconception`). All 48 lean KS3 lessons tagged. 13 new lines and 4 reworded corrections, as ruled; three misconception statements reworded (RESP-09, RESP-07, ATOM-10) and ENER-30 minted for "Electricity is an energy resource". The 8 lessons that landed after the ruling sheet (C1, life-processes, why-almost-all) needed tags only; their wording notes are listed for Mide. `docs/ks3/misconception-register.md` and the lesson spec tables updated. Site: the commit carrying this row | Done | `check_ks3_live.sh` on every lean KS3 unit |
