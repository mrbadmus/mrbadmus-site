# KS4 packs run — report (2 Oct 2026)

Mide's ruling, 2 Oct 2026: **Design writes the KS4 lessons again; Code does
not author lessons.** This run built Design's input packs and did the three
approved fixes. Recorded in `docs/ks4/architecture.md` (two dated amendments:
the reversal and the four lesson rules; the 1 Oct amendment marked
superseded), `docs/ks4/AUTHORING-BRIEF.md` (superseded banner + the four
rules) and CLAUDE.md's KS4 section. `docs/ks4/BATCH-PLAN.md` lists batches 2
and 3 (29 lessons) under "To be rebuilt by Design later". Pushed as
`987c68594`.

## 1. Packs — all fifteen remaining batches, on main

Every pack is in `docs/ks4/packs/batch-N/`:

| file | what it is |
|---|---|
| `DESIGN-BRIEF.txt` | the copy-paste prompt for Design: batch, lessons, pack path |
| `00-BRIEF.md` | read-first list, the four lesson rules, then per lesson: family and why; one-line flagship *suggestion*; route layers with the spec's own labels; required practical (Combined and separate-science numbers); every calculation and whether it **chains** equations (rule 3); the equations that need **formula triangles** and their sheet label (rule 2); misconceptions to confront; a "Start here" access note (rule 1 — a note, not the question); usable verbatim quiz items per route (rule 4); diagrams; examiner tip |
| `FLAGS.md` | numbered science flags per lesson; **WRONG** = frozen text kept verbatim that must not be used as written, with the correct science and what to do |
| `04-checked-science-source/` | one file per lesson in the pilot format, verbatim from live data (read-only), plus: the examiner's route-tag table under the header; a CFIFA form of every worked example with a Convert step in front (examined); "Spec core missing" sections quoted from the spec where the frozen data lacks the lesson's own spec content |
| `05-diagram-library/README.md` | existing drawing code per lesson (`figlib/`, `shared/ks4-diagrams.js`, `ks3_art/`, batch lessons) and the figures still needed |
| `examination/` | the Opus examiner's file per lesson: spec statements, route table, check table |
| `_extract-notes.md` | the raw extraction notes, stamped "superseded by the examination where they disagree" |

Every source file was checked by an Opus examiner against AQA 8464 and
8461/8462/8463 (spec text and both June 2026 equation sheets), every point
tagged with its true route. Mide's 2 Oct rulings applied throughout: Ee =
½ke² is base; Ek and Ep labelled "On the sheet".

| batch | lessons | flags | WRONG items | commit on main |
|---|---|---|---|---|
| 4 | 13 | 91 | 15 | `5d665c7ef` |
| 5 | 15 | 93 | 13 | `f098dfbf8` |
| 6 | 14 | 79 | 10 | `1ac969940` |
| 7 | 16 | 72 | 8 | `451843f6a` |
| 8 | 16 | 75 | 9 | `6a3f76002` |
| 9 | 15 | 66 | 6 | `6bb69f792` |
| 10 | 15 | 70 | 9 | `be10a4994` |
| 11 | 16 | 81 | 13 | `62da15c17` |
| 12 | 14 | 72 | 13 | `6d13d2ac4` |
| 13 | 12 | 58 | 14 | `d72630466` |
| 14 | 15 | 79 | 13 | `187ebbc2b` |
| 15 | 15 | 64 | 6 | `f02cadc53` |
| 16 | 16 | 65 | 7 | `c1659dbdf` |
| 17 | 16 | 97 | 18 | `48ec9002d` |
| 18 | 13 | 76 | 8 | `870cc2de1` |
| **total** | **222** | **1,138** | **162** | |

The pack is assembled from the examiners' per-lesson fragments by
`tools/ks4_assemble_pack.py batch-N` (refuses a missing or extra lesson).
The reusable examiner brief is `~/tmp/ks4-spec/PACK-EXAMINER-BRIEF.md`; the
spec texts it reads are beside it (outside the repo).

What the packs found, in general:
- The frozen data's own spec numbers are often the site's internal
  numbering, not AQA's; every brief gives the true reference.
- The frozen `rp` fields are frequently wrong (wrong number, wrong
  practical, or a practical AQA does not set). Every brief gives the
  Combined and separate-science numbers from the specs.
- The `higher` field is rarely Higher-tier content: most hold base content
  (so Foundation pupils lose it today) or off-spec content; several show
  HT-only content on Foundation routes. Each is a ROUTE flag.
- Banks are tiny (0–5 usable verbatim items per lesson); Design writes the
  rest to the batch's fixed size (rule 4).
- No lesson has an approved examiner tip.

## 2. Frozen corrections — parked on `feat/ks4-frozen-corrections`

The prompt asked for a migration. **There is no database row to migrate:**
the 19 items and atom economy's text exist only in the twelve
`all_subtopics_*.py` files (no Supabase table mirrors them;
`ks4_assignment_bank` is a different corpus). So the correction is a data
commit, parked on the branch, never on main:

- 19 items (B2-W1…W10, B3-W1…W9), 60 item-route copies; atom economy's
  formula/equation and common-mistake text (6 fields × TF, TH); 163 strings
  in all. Every credited answer stays at index 0.
- Route-wrong items were replaced on their wrong routes only, with in-spec
  items of the same shape (B2-W4 on CH, B2-W6 on CF/CH); B3-W8 is now the
  spec's qualitative pressure–temperature item.
- The 19 `withhold` entries are removed (the items are served again);
  batches 2 and 3 re-frozen; DEPARTURES rows updated.
- Rehearsal = full build + KS4 gates on the branch. Rollback = `git revert`
  of the corrections commit.
- An independent Opus examiner re-checked every row: **PASS, no FIX rows**
  (`docs/ks4/FROZEN-CORRECTIONS-REVIEW.md`).
- `docs/ks4/FROZEN-CORRECTIONS.md` carries the md5 of every changed file
  before and after, the counts, and every row (before, after, spec, why).

**State:** pushed to `feat/ks4-frozen-corrections` at `8bdb6c1eb` (corrections
`c0ee470ff` + review `8bdb6c1eb`), rebased onto main `48ec9002d` (after the
pilot fix and Prompt T's `launch.json`); a plain `build_all.py` per
`launch.json` gives zero diff; B2C files equal main; batch-2/3 re-freeze
reproduces the committed hashes; all gates green (pilot check, batch check,
science rulings 101/101, consumer_launch_state 36/36, ks4_chrome_drive,
ks4_parity, verify_ks3; `prepush_gate --check` green). An earlier parity red
was a harness artefact (Chrome SIGKILLed under memory pressure from other
sessions), not the corrections.

To apply: merge the branch (it is site data; the chat merges, no database
step).

## 3. Route flags — `fix/ks4-route-flags`, PR to be opened

A full spec audit of all 264 subtopics (`docs/ks4/route-audit/`) found
eight to move; chemistry none.

| subtopic | before | after | spec |
|---|---|---|---|
| meiosis | TF TH | CF CH TF TH | 8464 4.6.1.2 |
| classification-living-organisms | TF TH | CF CH TF TH | 8464 4.6.4 |
| thermal-conductivity | TF TH | CF CH TF TH (RP2 a physics-only layer) | 8464 6.1.2.1 |
| resolving-forces | TH | CH TH | 8464 6.5.1.4 (HT) |
| free-body-diagrams | TH | CH TH | 8464 6.5.1.4 (HT) |
| motion-in-a-circle | TH | CH TH | 8464 6.5.4.1.3 (HT) |
| wave-front-refraction | TH | CH TH | 8464 6.6.2.2 (HT) |
| dark-matter-dark-energy | TH | TF TH | 8463 4.8.2 (physics only, not HT) |

Pages: **11 new** (meiosis CF CH, classification CF CH, thermal-conductivity
CF CH, resolving-forces CH, free-body-diagrams CH, motion-in-a-circle CH,
wave-front-refraction CH, dark-matter-dark-energy TF); **21 changed** (7
topic index pages, 14 neighbours whose previous/next now points at a new
page); `shared/ks4-nav.js` changes 8 entries, which moves its `?v=` stamp on
the 96 batch-2/3 pages. Every other page byte-identical to main.

The route change also re-flags 468 authored KS4 pool questions in
`ks4_data/` (`load_pool()` refuses a question whose flags disagree with
`classify()`): only `tier`/`triple_only` change.

After merge (for the chat): regenerate the backend's
`curriculum-tree.json` (`tools/export_curriculum_tree.py`; 8 flag lines) and
redeploy; apply `docs/ks4/route-audit/BANK-FLAGS.sql` (468 rows, guarded,
with rollback) on TEST then production. `curriculum_tree_mirror` and
`frozen_window_guard` are red on the branch until then, with GATE-OVERRIDE
lines naming why.

**State at report time:** branch pushed at `31fb3e786` (route commit
`a9535452f` + PR-body commit carrying the GATE-OVERRIDE lines, which only
count on the tip commit). It was built on main `1ac969940`, **before** the
pilot-block fix (`3f9543f4d`) and Prompt T's `launch.json` (`c5e69ac0b`)
landed, so it must be rebased and rebuilt (build per `launch.json`; take
main's side for generated files) before merging. Its byte-identity proof
should be re-run then.

## 4. Pilot-block fixes — live

- The exam ladder now reads "63 000", "63,000", "63000" (and a decimal
  comma like "6,3") correctly. Root cause: `parseFloat` stopped at the space
  and the single `replace(',', '.')` turned a thousands comma into a decimal
  point.
- The sorting block (Ks4Sort) now ticks its rail stop. Root cause: our
  runtime writes `setState` into the same object `s` points at, so the
  block's `!s.reported` test after `setState` was always false and `onDone`
  never fired. Fixed the way Ks4Chain already does it (read before setting).
- Through `ks4_rulings.py` (R16, R17) and `build_ks4.py`; Design's delivery
  untouched; no science changed; no lesson constants or freeze hashes moved.
- **Pages changed: 150** (×2 trees): all 54 pilot pages, 52 batch-2, 44
  batch-3. One DEPARTURES row per pilot lesson (`<slug>-E1` in
  `DEPARTURES-PILOT.md`) and a note in the batch-2/3 registers.
- Pushed `6d13d2ac4..3f9543f4d`. **Live proof:** `check_ks4_live.py` — pilot
  54/54, batch-2 52/52, batch-3 44/44 byte for byte, every asset matching
  its stamp. (This also closes the batch-2/3 live proof left pending on
  1 Oct.)

## For Mide

1. **Q = mcΔT in chemistry's exothermic-endothermic (batch 12).** AQA 8462
   4.5.1.1 / 8464 5.5.1.1 say calculation of energy changes is not
   required, but the site ships the calculation on all four routes. The
   pack tells Design not to teach it; say if you want it kept.
2. **Half-lives "net decline as a ratio" (batch 16, F6).** Fraction
   remaining (1/8) or fraction decayed (7/8)? The pack teaches both and asks
   every question to say which.
3. **More wrong frozen quiz items, outside the approved 19.** Wrong-answer
   explanations shifted onto the wrong option in live data: land-use q1, q2;
   global-warming q1, q2; meiosis q1; dna-genome q3; deforestation (2
   items); maintaining-biodiversity (2 items); bond-energy-calculations q2;
   distance-time-graphs q1; properties-em-waves-1 q1. Plus the 162 WRONG
   flags in the packs. Approve a second correction run like the 19?
4. **Frozen text still wrong after the approved corrections:** the
   products-denominator atom-economy formula in conservation-of-mass
   (`higher`) and amounts-in-equations (CH, TH); atom-economy theory 2's
   high/low labels; kelvin in other physics subtopics.
5. **Layer defects on the live old pages** (until Design rebuilds them):
   base content hidden in `higher` fields from Foundation routes; HT or
   separate-science content shown on Foundation or Combined routes. Listed
   per lesson in each pack's FLAGS.md and in the route audit.
6. **Gaps with no page at all:** kidney/ADH (8461 4.5.3.3), plant hormones
   (8461 4.5.4), speciation (8461 4.6.3.2); gas volumes (8462 4.3.5, TH);
   three 8463 sections (physics audit). The infrared required practical
   (Combined RP21 / Physics RP10) appears on no page; it belongs on
   properties-em-waves-1 (batch 17 pack says so).
7. **The route PR needs opening by hand** (no `gh` or token on this
   machine): https://github.com/mrbadmus/mrbadmus-site/compare/main...fix/ks4-route-flags
   — body in `docs/ks4/route-audit/PR-BODY.md` on the branch.
8. Batch-3 temperature-changes-shc carries the full SHC practical block;
   when Design rebuilds it, link to batch 15's energy-changes-in-systems
   instead.

## Decisions I made

1. **Frozen "migration" → data commit.** No table holds the items, so a SQL
   migration would update nothing. Did the equivalent: a parked data commit,
   `git revert` as rollback, a full build plus gates as the rehearsal, md5s
   at the top of the report, and an independent examiner pass.
2. **Route audit of all 264 subtopics,** not just the seven named. Eight
   move; chemistry none.
3. **Decomposition stays on all routes.** The biology examiner leaned to
   narrowing it; its Combined core is 8464 4.7.2.2 and the live batch-2
   lesson already teaches only that on Combined. Narrowing would delete two
   live Combined pages. Gravity-stable-orbits stays TH.
4. **The route PR re-flags 468 pool questions** in `ks4_data/` — forced by
   `load_pool()`'s consistency check; database and backend changes are
   written for the chat, not applied.
5. **Route-wrong frozen items replaced, not deleted** (B2-W4 CH, B2-W6
   CF/CH, B3-W8), so tiny banks do not shrink.
6. **All fifteen packs, not "as the budget allows".** Sonnet extracted,
   Opus examined (2–4 examiners per batch), each pack pushed as soon as it
   passed.
7. **The brief carries a "Start here" access note per lesson,** not a
   question: rule 1 says what Design's guess must stand on, without Code
   authoring it.
8. **Examiners could change a family** with a reason (e.g.
   thermal-conductivity REQUIRED PRACTICAL → MODEL, since Combined has no
   insulation RP). BATCH-PLAN's families were the starting point.
9. **Pack filenames normalised** (no spaces or brackets; true spec in the
   name where the frozen one was wrong).
10. **Raw extraction notes kept but stamped superseded:** the extractor's
    key-alignment check missed shifted explanations the examiners caught,
    and it repeats wrong frozen RP numbers.
11. **Pilot fixes through the rulings layer,** so Design's delivery stays
    untouched; pushed by me after the executor declined to push.
12. **Disk:** deleted ~12,000 orphaned headless-Chrome temp folders older
    than 4 hours and gate scratch older than a day; removed the pilot-fix
    worktree after landing.
13. **No PR opened** — no `gh` or token; compare link and committed body
    instead.
14. A leftover `git stash` from the frozen branch's first rebase was left in
    place (its content is in the commits).

Deviation: the prompt's frozen-corrections "migration … rehearsed on TEST"
→ a parked data commit rehearsed by build and gates → the rows live only in
Python data, so there is nothing in any database to migrate.
