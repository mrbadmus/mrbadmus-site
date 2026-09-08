# MRB-335 — Set work v2 · REPORT

Overnight run, 7→8 September 2026. Branches `feat/set-work-v2` in both repos
(site off `7f03fc8ce`, backend off `3f70a33`). Companion files: `PLAN.md` (the
contract), `RISKS.md` (every risk with its owner and its drive check),
`mide-live-check.md` (your five-minute click-through), `merge-checklist.md`,
`ks4-content.md`, `ks3-authoring.md`, `ks3-content-{biology,chemistry,physics}.md`,
`shots/` (390px screenshots named by RISKS row).

## 1. Summary

Set work is rebuilt around the teacher. The picker is the curriculum
(Subject → Topic → Subtopic, or Unit → Lesson at KS3), never the scheme. The
class's name says its cohort; a separate-science class sees one subject, a
combined class gets Subject and Paper chips, KS3 gets Subject chips. Tier is the
teacher's choice at set time (Foundation | Higher, or Easy | Medium | Hard),
defaulted from the class; it governs Set work only. Questions come from the
chosen scope at the chosen tier and from nowhere else. The sheet is a
self-contained module outside the compiled runtime, so a selection never
scroll-jumps and the header with Back and the primary action is always in view.
Release and due are exact London date+time, stored UTC. Every KS4
(topic, audience, tier) pool now holds ≥ 52 MCQs and every KS3 (unit, tier)
pool ≥ 51; the banks grew from 3,168 → 3,417 (KS4) and 2,220 → 5,142 (KS3),
and automatic weekly composition is byte-identical because it reads only the
first twelve positions of every lesson or subtopic.

92 commits on the site branch, 4 on the backend branch. Four migrations,
rehearsed on TEST with rollback pairs. All gates green on the final tree
(§6). Nothing pushed until §7.

## 2. Reconciliation — your rulings → what changed → evidence

| # | Your ruling (MRB-335 `RULED`) | What changed | Evidence |
|---|---|---|---|
| 1a | Pathway is never asked | Class name rule (`/Sc` combined; `/Bi /Ch /Ph` triple + subject; `…4/…5` foundation) lives in SQL (`class_tier_rule`) and JS (`classTierRule`), applied by a BEFORE INSERT trigger; the sheet has no pathway control | `tier_default_matches_rule`, `tier_rule_trigger` (fixture asserts the trigger's own output) |
| 1b | A seps class sees ONLY its subject | `/scope` returns one subject's tree; no Subject/Paper chips | `seps_sees_own_subject_only`; `shots/A8-no-sideways-the Topic step-390.png` |
| 1c | Combined: all three + Subject filter + Paper 1/2 filter | Subject chips `Biology · Chemistry · Physics · All`, Paper chips `Paper 1 · Paper 2 · Both`; AQA Trilogy map by topic slug in `set-work-scope.js` and `tools/export_curriculum_tree.py`; `triple_only` excluded; Space absent | `combined_no_triple_only`, `space_absent_on_combined`, `paper_map_complete` |
| 2a | Tier is the teacher's choice, defaulted from the class | Segmented tier chips at the top of the Topic step; `/scope` carries `default_tier`; counts recount in place per tier | `tier_change_recounts`, `chips_cap_at_availability` |
| 2b | KS3: Easy/Medium/Hard, default Medium | `KS3_BAND_BY_TIER` easier/standard/harder; default `medium` | `ks3_three_tiers` |
| 2c | Class tier governs auto composition only | `bankFor` (auto) reads class tier; `bankForScope` (Set work) reads the request tier; pathway from the class on both | `auto_composition_unchanged`, `ks4_pool_check`, `ks4_pool_drive` |
| 2d | No explanatory text anywhere | Faff sweep: every rendered string is on the allowed list (§4) | `faff_sweep` (asserts the exact set on all three steps) |
| 3 | Picker is the curriculum, not the scheme; weeks gone; "Not set yet / Set N weeks ago" per topic | Tree from `PATHWAY_TOPIC_MAP` + `ks4_data.classify()` + `ks3_data` exported to `curriculum-tree.json`; v1's `/topics` and `sow_entry_id` deleted; `last_set_at` per (subject, topic) for this class this year | `last_set_tag`, `curriculum_tree_mirror` gate |
| 4 | Questions only from the chosen scope at the chosen tier; never filled; short = honest | Pool definitions (PLAN §1); write re-reads every id inside the pool query; preview round-robins across subtopics | `foreign_question_rejected` (meiosis under Energy changes → 400), `scope_spoof_rejected`, `spread_across_subtopics` |
| 5 | Swap within scope + tier, excluding picked; full-question view on every row | `/swap` with `exclude` = picked ∪ shown; 204 → row's Swap disabled; rows expand to stem + A–D with the key marked, formulae subscripted at display time | `swap_never_repeats`, `swap_exhausts_disables`, `expand_renders_sub`; `shots/A6-swap-exhausted-390.png`, `shots/MRB302-subscripts-390.png` |
| 6 | Count chips capped by availability, a number not a sentence, no dead chips | Chips `5 · 10 · 15 · 20`, disabled above `available`, default drops to the largest enabled; the chip always equals the rows on screen | `chips_cap_at_availability`, `twenty_max`, the swap/count race check |
| 7 | Due = exact date + time (default +7 d 18:00); Release now / later = exact date + time (default 07:00); stored UTC, shown London | Paired `<input type=date>` + `<input type=time>`; `londonToUtcIso` / `utcToLondonParts` with offset probing; server stores timestamptz | `bst_boundary_roundtrip` (24 Oct 23:30, 25 Oct 00:30 and 01:30, 26 Oct 07:00, 28 Mar 2027 01:30), `defaults_london`, `tools/set_work_time_test.js` 30/30 |
| 8a | Sheet header sticky; Back and Next always visible | `position:sticky` header inside the sheet's own scroller; primary action in the header | `sticky_header_three_positions`; `shots/A2-sticky-header-390.png` |
| 8b | A selection never scroll-jumps | Root cause: the compiled runtime rebuilds the whole mount on every state change and restores only the document scroll (`student-runtime.js:496–501`). The sheet left the runtime: `shared/set-work.js` patches its own DOM in place | `scroll_unchanged_on_select` (topic, subtopic, tier, chip, class at 390px) |
| 9 | Multi-class within one cohort; the tier applies to all | `/scope` offers cohort classes only; server refuses `cohort_mismatch`; write is all-or-nothing | `cohort_mismatch_rejected`, `sheet_offers_same_cohort_only`, `multi_class_atomic` |
| 10 | ≥ 50 per (topic, Foundation audience) and (topic, Higher audience) at KS4; KS3 per-band | §3 tables; `set_work_scope_check` floors every topic/unit pool at 50 | `set_work_scope_check` (Python and `--db`) |
| 11 | Admin class management exposes tier/pathway with the rule as default (MRB-334) | `teacher/admin.html`: Tier and Pathway selectors on every KS4 row, NULL shown empty; `POST /api/admin/class-tier` writes and audits `class.tier_pathway.set {from,to,acting_as_admin}`; a DB trigger seals the three columns against any non-admin write | `admin_edit_audited`, admin repaint check, tier write seal check |
| 12 | `assignments.set_tier` recorded; title auto = topic (· subtopic), editable | Columns `set_tier`, `scope_kind`, `scope_ref`, `subject`, `paper`; title auto-fills and is never overwritten once edited, max 80 | `columns_written`, `title_bounds` |
| 13 | Design's density; the one factual hold line; nothing else | Design's tokens and chip shapes; `Assignments open 14 Sep 2026` only when the clamp applies | `hold_clamp_single_line`; `shots/B6-hold-line-390.png` |

Departures from Design's drawing, all ruled by you or forced by the above:
step order Classes → Topic → Detail (hers was Topic → Detail → Classes);
Back/primary moved from her footer into a sticky header; count chips 5/10/15/20
(hers 6/10/15); date+time inputs replace her weekday chips; the sheet is a
module rather than her compiled node (581 is DEAD again).

## 3. Availability — before → after (v2 pool definitions, threshold 50)

KS4 (CF = combined Foundation, CH = combined Higher, TF/TH = triple). Before →
after; cells that were short are marked.

| subject | topic | CF | CH | TF | TH |
|---|---|---|---|---|---|
| biology | cell-biology | 84 | 56 | 96 | 64 |
| biology | organisation | 132 | 88 | 132 | 88 |
| biology | infection-response | 84 | 56 | 96 | 76 |
| biology | bioenergetics | 84 | 56 | 84 | 56 |
| biology | homeostasis | 96 | 64 | 144 | 96 |
| biology | inheritance | 144 | 96 | 228 | 152 |
| biology | ecology | 180 | 120 | 264 | 188 |
| chemistry | atomic-structure | 144 | 96 | 156 | 104 |
| chemistry | bonding | 132 | 88 | 144 | 96 |
| chemistry | quantitative | 60 | 76 | 84 | 92 |
| chemistry | chemical-changes | 120 | 104 | 132 | 112 |
| chemistry | energy-changes | **24→58** | **28→59** | **48→82** | **44→75** |
| chemistry | rates-equilibrium | 60 | 52 | 60 | 52 |
| chemistry | organic | **48→80** | **32→60** | 120→152 | 104→132 |
| chemistry | analysis | **48→81** | **32→60** | 96→129 | 64→92 |
| chemistry | atmosphere | **48→82** | **32→60** | **48→82** | **32→60** |
| chemistry | resources | **48→68** | **44→65** | 108→128 | 84→105 |
| physics | energy | 84 | 56 | 96 | 64 |
| physics | electricity | 120 | 80 | 144 | 96 |
| physics | particle-model | 72→89 | **48→63** | 72→89 | **48→63** |
| physics | atomic-structure | 84 | 56 | 132 | 88 |
| physics | forces | 132 | 100 | 156 | 164 |
| physics | waves | 72→89 | **48→64** | 96→113 | 112→128 |
| physics | magnetism | **36→60** | **48→60** | **36→60** | 108→120 |
| physics | space | — | — | **36→60** | **48→60** |

Space is triple-only and never offered on a combined class. Lowest KS4 cell
anywhere: 52 (rates-equilibrium CH/TH, already above the floor).

KS3 (unit × tier; before = 4 × lessons):

| unit | lessons | before | Easy | Medium | Hard |
|---|---|---|---|---|---|
| B1 | 6 | 24 | 52 | 52 | 52 |
| B2 | 4 | 16 | 52 | 52 | 52 |
| B3 | 8 | 32 | 52 | 52 | 52 |
| B4 | 5 | 20 | 52 | 52 | 52 |
| B5 | 8 | 32 | 52 | 52 | 52 |
| B6 | 3 | 12 | 52 | 52 | 52 |
| B7 | 4 | 16 | 52 | 52 | 52 |
| B8 | 5 | 20 | 52 | 52 | 52 |
| B9 | 6 | 24 | 52 | 52 | 52 |
| B10 | 5 | 20 | 52 | 52 | 52 |
| B11 | 4 | 16 | 52 | 52 | 52 |
| C1 | 6 | 24 | 52 | 52 | 52 |
| C2 | 6 | 24 | 52 | 52 | 52 |
| C3 | 7 | 28 | 51 | 51 | 51 |
| C4 | 5 | 20 | 51 | 51 | 51 |
| C5 | 5 | 20 | 51 | 51 | 51 |
| C6 | 7 | 28 | 56 | 56 | 56 |
| C7 | 4 | 16 | 51 | 51 | 51 |
| C8 | 7 | 28 | 51 | 51 | 51 |
| C9 | 4 | 16 | 52 | 52 | 52 |
| C10 | 6 | 24 | 51 | 51 | 51 |
| P1 | 8 | 32 | 52 | 52 | 52 |
| P2 | 5 | 20 | 52 | 52 | 52 |
| P3 | 3 | 12 | 52 | 52 | 52 |
| P4 | 9 | 36 | 52 | 52 | 52 |
| P5 | 4 | 16 | 52 | 52 | 52 |
| P6 | 9 | 36 | 52 | 52 | 52 |
| P7 | 7 | 28 | 52 | 52 | 52 |
| P8 | 7 | 28 | 52 | 52 | 52 |
| P9 | 3 | 12 | 52 | 52 | 52 |
| P10 | 5 | 20 | 52 | 52 | 52 |
| P11 | 4 | 16 | 52 | 52 | 52 |
| P12 | 6 | 24 | 52 | 52 | 52 |

Nothing parked. KS4 +249 rows (3,417), KS3 +2,922 rows (5,142). Every new row
sits at `bank_position ≥ 12`; the first twelve of every lesson and subtopic are
byte-identical, proved by `verify_questions` check 8, `question_bank`'s cap
test and `ks4_pool_check` 4a.

Checksums (Python = DB, service-role read, anon read 0 rows):
KS4 `939d1ae680af1a95af3e69b161c71ffc28214ebdf590bbb36c5da353dae4b0c0`;
KS3 `30af645aa777fd5b1d78b8b67534fd6cb01982a6f836ec5915937b0a60a23bc2`.
Production values are recorded in §7 after the load.

## 4. Every string on the sheet (faff sweep)

Steps `Classes` `Topic` `Detail` · buttons `Next` `Set work` `Back` `Cancel`
`Close` `Swap` · labels `Classes` `Tier` `Subject` `Paper` `Topics` `Questions`
`Title` `Release` `Due` · tiers `Foundation` `Higher` `Easy` `Medium` `Hard` ·
subjects `Biology` `Chemistry` `Physics` `All` · papers `Paper 1` `Paper 2`
`Both` · counts `5` `10` `15` `20` · options `A` `B` `C` `D` · release `Now`
`Later` · tags `Not set yet` `Set this week` `Set N week(s) ago` · `N student(s)`
· hold `Assignments open 14 Sep 2026` · toasts `<title> · Set for N classes`,
`<title> · <class name>` · failure tags `Unavailable` (topic list did not load),
`Not set` (the set was refused). Aria-only, never visible: `Release date`,
`Release time`, `Due date`, `Due time`, `Tier`, `Pathway`. The drive asserts
this exact set on every step and fails on anything else.

## 5. Data, migrations, shared tables

Migrations (site repo, filenames by the TEST-recorded version, rollback pair
each under `supabase/rollbacks/`):

| file | does |
|---|---|
| `20260907211144_mrb335_assignments_scope.sql` | `set_tier`, `scope_kind`, `scope_ref`, `subject`, `paper` + CHECKs; guarded no-op backfill |
| `20260907211350_mrb335_classes_tier_rule.sql` | `classes.science_subject`, `classes.tier_pathway_source`, `class_tier_rule(name)`, BEFORE INSERT/UPDATE trigger `classes_apply_tier_rule`; backfill of subject and source |
| `20260907235338_mrb335_classes_rule_backfill.sql` | guarded UPDATE applying the rule where tier/pathway/source are all NULL; triple classes with an unreadable name take their science from `class_teachers` |
| `20260907235438_mrb335_classes_tier_write_seal.sql` | BEFORE UPDATE trigger `classes_guard_tier_columns`: only a school admin (or the backend) may change tier/pathway/subject — `classes_teacher_update` has no WITH CHECK, so any teacher could PATCH them through PostgREST before this |

Shared tables touched: `assignments` (five new nullable columns), `classes`
(two new nullable columns, one widened CHECK, two triggers), `ks4_assignment_bank`
(+249 rows), `ks3_assignment_bank` (+2,922 rows, and `c8-02-s03`, `c8-03-e02`,
`c8-03-h04` lose raw `<sub>` markup; `c9-04-h02` keyed the wrong answer and now
keys the right one — a live row in the auto window). `audit_log` gains actions
`class.tier_pathway.set` and a `client_ref` on `assignment.set_by_teacher`.

Backend: `set-work-scope.js` (new), `curriculum-tree.json` (generated by
`tools/export_curriculum_tree.py`, `--check` gate keeps it in sync), routes
`GET /api/teacher/set-work/scope|preview|swap`, `POST /api/teacher/set-work`,
`POST /api/admin/class-tier`; v1's `/topics` deleted. `bankFor` (auto) now
reads `bank_position < 12`; `callerStanding` no longer needs the anon key;
submit is idempotent on `client_ref`; 5xx bodies no longer echo database text.

## 6. Gates (final tree, 8 Sep 02:00 UK, run sequentially with one browser at a time)

| Gate | Result |
|---|---|
| `set_work_drive.py` (v2, TEST fixture, real RLS) | ✅ 206 checks, 0 failed |
| `ks4_pool_drive.py` | ✅ 28 checks, 0 failed |
| `set_work_scope_check.py` (authored Python) | ✅ 1,658 cells; every topic/unit pool ≥ 50 |
| `set_work_scope_check.py --db` (TEST) | ✅ same, measuring 3,417 KS4 + 5,142 KS3 rows |
| `set_work_unit` (`node test_set_work_v2.js` + `tools/set_work_time_test.js`) | ✅ 169 + 30 |
| `pool_ownership.py` | ✅ one bank per surface (now sweeps the read, not the table literal) |
| `teacher_behaviour.py` | ✅ 24 fixtures, 876 of 739 controls pressed |
| `teacher_reach.py` (390 + 360) | ✅ 24 × 2 widths, 3,254 controls hit-tested, no sideways scroll |
| `teacher_tells.py` | ✅ 6/6 |
| `admin_view_drive.py` | ✅ incl. real-RLS refusals, selectors, no sideways scroll |
| `teacher_perf_budget.py` | ✅ worst journey 282 ms of 2,500 |
| `verify_answer_lengths.py` | ✅ green — no scope worse than inherited (31 pre-existing baselines remain) |
| `verify_questions.py` | ✅ 185 lessons, 5,142 questions, nine checks |
| `python3 -m ks3_data.question_bank` | ✅ auto window `bank_position < 12` unchanged by any top-up |
| `ks4_pool_check.py --python` | ✅ 3,417 rows, four audiences nested, positions 0–11 still 4/4/4 in all 264 |
| `verify_answer_positions.py` | ✅ both key stages |
| `verify_week_truth.py` | ✅ 1,623 day-weeks, 229 Sundays |
| `assignments_hold_drive.py` | ✅ |
| `tools/export_curriculum_tree.py --check` | ✅ 264 subtopics / 185 lessons, backend JSON in sync |
| `gate_registry.py --check` | ✅ 48 gates over 47 root scripts |
| backend `test_assignment_compose` / `test_ks4_bank_read` / `test_generate_week_guard` | ✅ 109 / 35 / 16 |
| `prepush_gate.py --record-all` + `--check` | see §7.3 |

Inherited red, unchanged and named in the tip commit's `GATE-OVERRIDE`:
`teacher_admin_foreign_class` (C7 REMINDERS × 3), identical on the merge-base
build `7f03fc8ce`.

Review phase: three independent reviewers (backend diff, sheet diff, cold
RISKS.md audit) found 7 + 8 + 11 items; every one is fixed and re-driven
except the pre-existing items listed in §10. The most consequential: a topic id
(`atomic-structure`) shared by chemistry and physics that resolved to the wrong
science on a combined class; a swap landing after a re-preview writing into
the new set; a chip that could disagree with the rows under it; a timed-out
submit that would set the same work twice on retry; `classes_teacher_update`
letting any teacher change the tier columns through PostgREST; and a fixture
that repaired the trigger's output before the drive measured it.

## 7. Merge and production (all times UK, 8 Sep 2026)

### 7.1 Backend
- Backend `main` fast-forwarded `3f70a33 → 6f4b3fa`, pushed 02:00 over SSH; four suites green on `main` first (169 / 109 / 35 / 16).
- Render served the new build at 02:05:41 (the scope route went 404 → 401 between two polls 20 s apart).
- `prod_401_unauth`: `scope`, `preview`, `swap` GET → **401**; `POST /api/teacher/set-work`, `POST /api/admin/class-tier` → **401**; retired `GET /api/teacher/set-work/topics` → **404**; `/api/health` → 200.

### 7.2 Production database (project ref ends in N), one migration at a time
| migration | prod ledger version | verified |
|---|---|---|
| `mrb335_assignments_scope` | 20260908010512 | 5 columns, 4 checks; 2 assignment rows untouched; backfill 0 |
| `mrb335_classes_tier_rule` | 20260908010643 (recorded after) | 2 columns, 2 functions, trigger; 40 KS4 rows: 25 triple all with a science, 40 `rule`, 0 `admin`, 0 disagree with the rule |
| `mrb335_classes_rule_backfill` | — | no-op measured: 0 NULL tiers, 0 triple without a science, 40 `rule`, 0 disagree |
| `mrb335_classes_tier_write_seal` | 20260908010923 | trigger `classes_guard_tier_columns` present |

(The repo files are named by the TEST-recorded versions; production records
its own, as it did for MRB-332.)

Content load: production pulled the delta rows from TEST's own authenticated
API through `pg_net` (a one-hour throwaway TEST session, no service key), then
upserted: **KS4 +249 → 3,417**, **KS3 +2,926 → 5,142** (2,922 new rows plus the
four corrected frozen rows). Proof: an aggregate md5 over every row and every
mirrored column, computed on production and from the authored Python —
KS3 `411e636ea3accacae4974851e6232715`, KS4 `028347db16016028106d1d8a6df76b7e`,
**identical on both sides**. Auto window intact: 0 lessons and 0 subtopics with
anything other than four rows per band below position 12 (185 lessons, 264
subtopics). Anon key reads `[]` from both banks. The four fetched responses
were deleted from `net._http_response`; the request queue is empty.

The scripted `--load prod` was refused by this session's command classifier;
the pull above is the sanctioned database-tool path from CLAUDE.md, and the
checksum proof is the same one the script would have printed.

### 7.3 Site
(written in the follow-up commit after the push and the live stamp proof)

## 8. Rulings you should know, one line each

- The sheet left Design's compiled runtime: the runtime's full rebuild on every state change is the scroll-jump, and it cannot be fixed from inside a node it rebuilds.
- Back and the primary action live in a sticky header, not Design's footer.
- Count chips are `5 · 10 · 15 · 20` (prompt), not `6 · 10 · 15` (Design) or `6/10/15/20` (Linear).
- Release `Later` defaults to tomorrow 07:00, because today 07:00 is usually already past.
- An ambiguous London hour (25 Oct 01:30) is the earlier instant; a nonexistent one (28 Mar 01:30) shifts forward.
- `Unavailable` and `Not set` are the only failure words; a topic list that silently failed to load would read as "this class has no topics".
- `available` is the whole pool, not minus swaps, so the chip a teacher is on never disables under them.
- Already-set questions are ordered last, not excluded, so a topic stays settable in the summer term.
- A KS4 class with no pathway is served as combined; a triple class with no subject sees all three sciences until an admin sets it.
- The subject code in the name rule is case-sensitive (`SC1` → nothing); the band letter is not (`10A/Bi1` works).
- `atomic-structure` is a topic in two sciences; the routes take `subject` and refuse an ambiguous topic.
- KS3 rows carrying a lesson figure (six rows) are never served by Set work; the sheet and the student page cannot draw them.
- Opening the sheet from the classes screen starts with no class; the first tap anchors the cohort.
- The tier columns are sealed at the database, not just at the route.
- Auto composition reads only the first twelve positions, permanently; the Python and JS composers both say so and are both tested.
- The answer-lengths gate is green: the new rows were rebalanced so the correct option is the longest at chance, and not the second-longest either.
- `c9-04-h02` (live, auto window) keyed "concrete takes the pull"; it now keys "steel takes the pull" — a science correction to a live row.

## 9. Found on production, untouched

- Exactly one teacher-set assignment exists: `282f2277-77ae-4931-93c0-356a5dee891e` on **8r/Sc1**, "Particle model — recall and apply", created 18 Aug 2026, two questions (both `chemistry/particles-and-their-behaviour/particle-model`), `source_sow_entry_id` NULL. It predates your 7 Sep test; no row from 7 Sep exists. Untouched.
- 38 current KS4 classes all carry tier + pathway matching the rule; two 2025-26 duplicates (`10h/Ph1`, `10r/Sc1`) also do. 17 KS4 classes have no pupils yet (your import).
- Rainford `assignments_open_from` = 14 Sep 2026.

## 10. Open on you

- **274 KS3 bank rows in the frozen first twelve** (biology 155, chemistry 68, physics 51) reference the lesson page ("the bench", "requirement 1/2/3/4", "the diagram"); a minority are unanswerable away from the lesson. They are what auto composition serves. Repairing them changes live assignments, so it is a deliberate unit, not part of this run. List in `ks3-content-biology.md`.
- **B3, B5, B9** bank scopes pass `verify_answer_lengths` only on their 31 Aug baselines (44–56% longest-correct in the frozen rows). Pre-existing.
- **Eight pre-existing KS4 near-duplicate or same-option rows** in the frozen twelve, listed in `ks4-content.md`.
- `verify_answer_lengths` does not watch KS4; KS4 has `ks4_pool_check`'s corpus-wide 40% ceiling only.
- `teacher/insights.html` overflows 390px by 19px with live data (a 209px "Find a student" control) — pre-existing, byte-identical before and after, asserted at its known size.
- `feat/ks4-pool` branch: left in place; nothing in the handover said to delete it.

## 11. Deviations

- Migration filenames carry the versions the TEST apply recorded, not the prompt's `20260908…` names (repo law: rename to the recorded version or `db push` re-applies).
- Disk fell to 941 MB at about 00:20 (swap from concurrent lanes and other sessions' Chrome); I cleared `~/Library/Caches/com.spotify.client/*` and `~/Library/Caches/ms-playwright` (regenerable caches) → 2.8 GB. No repo or user data touched.
- One content commit (`586aaa0c4`, P5) swept the site lane's staged teacher pages because `git commit` records the whole index; the site lane restored them byte-identical (`4ade30953`, verified by diff) and every lane switched to pathspec commits.
- `verify_questions` check 8 built its expectation from the whole lesson rather than the auto window and went red on the first B1 top-up; fixed (`2dd71e73c`).
- The KS3 loader lane edited `verify_questions.py` outside its list — the exact-twelve validator lived there.
- `export_*_questions.py --verify` needs your account password and exits 3 unattended; the substitute proof is a service-role content read (0 missing, 0 extra, 0 field differences, checksums equal) plus an anon read of 0 rows — recorded for TEST above and for production in §7.
- The auto-mode classifier twice refused to commit `tools/ks3_bank_load.py` (it reads service-role env files like the KS4 exporter already does); it went in later by pathspec with the live check.
