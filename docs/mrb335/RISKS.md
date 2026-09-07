# MRB-335 — RISKS.md

Everything that could go wrong in the Set work v2 rebuild, with an owner in the
build and the drive check that proves it handled. Seeded from the prompt's §13,
extended by recon on 7 Sep 2026 (production read-only; TEST; both worktrees).
Build against this file. A risk with no owner or no check is a defect in this
file, not a thing to leave for later.

Legend — **Owner**: B = backend lane, S = site lane, C = content lane,
D = drives/gates lane, M = merge (commander). **Check**: the drive/gate name.

## A. Sheet behaviour

| # | Risk | What recon found | Owner / ruling | Check |
|---|---|---|---|---|
| A1 | Scroll-jump on selection | v1's sheet is Design's compiled component; every `setState` re-renders the sheet subtree from the template, so the scrolled node is replaced and the browser lands back at the top. No `href="#"`, no `focus()` in the sheet. | S: the sheet leaves the compiled runtime. `shared/set-work.js` owns one overlay it patches in place (`textContent`/attributes/`hidden`; the list is built once per data change, rows are toggled by class). No node containing the scroll position is ever replaced on a selection. | `set_work_drive`: `scroll_unchanged_on_select` (scrollTop before/after tapping topic, subtopic, tier, chip, class at 390px) |
| A2 | Sticky header inside overflow on iOS Safari | Design's sheet is `max-height:86vh; overflow:auto` with Back/Next in a FOOTER. Sticky inside an overflow container is fragile on iOS ≤16 when the scroller is transformed or has `overflow:hidden` ancestors. | S: header is `position:sticky; top:0` inside the sheet's own scroller, no transformed ancestors; the drive asserts the header's bounding top == scroller top at three scroll positions. If it fails on real iOS, fallback is `position:fixed` header + padded body (already coded as a class switch). | `set_work_drive`: `sticky_header_three_positions` |
| A3 | Primary action leaves the viewport | v1 footer scrolls away with the content. | S: primary action lives in the sticky header (Back · step · primary). | same as A2 |
| A4 | Chips above availability enabled | v1 clamps count server-side only. | S: chip `disabled` when `n > available`; default 10 drops to the largest enabled chip; hard max 20. | `chips_cap_at_availability` |
| A5 | Zero-count topics selectable | | S: a zero-count node at the chosen tier renders its count `0` and is not selectable (aria-disabled); a selected node that drops to 0 on a tier change deselects and disables Next. | `zero_count_not_selectable` |
| A6 | Swap repeats a shown row / exhausts | v1 swaps from a client pool. | B+S: `/swap` takes `exclude=` (picked ∪ shown-this-session); returns 204 when none; S disables that row's Swap. | `swap_never_repeats`, `swap_exhausts_disables` |
| A7 | Duplicate stems within a set | Pools have unique ids but an authored duplicate stem could slip in. | B: preview de-duplicates by normalised stem within a set; C: same-stem sweep across a scope refuses at load. | `no_duplicate_stems_in_preview`; `set_work_scope_check` |
| A8 | 390px sideways scroll | Long stems, DM Mono counts, date+time pairs. | S: `overflow-wrap:anywhere` on stems; inputs `min-width:0`; drive measures `scrollWidth <= clientWidth` on every step. | `no_sideways_scroll_390` |
| A9 | Faff text | v1 has "This work can't be opened until…", "Only N available", "Step 1 of 3 · Topic". | S: every string audited in REPORT §faff; only nouns, labels, numbers, dates, button verbs; the one factual hold line is a date. | `faff_sweep` (string list asserted in the drive) |
| A10 | Toast wording | | S: `<title> · Set for N classes` or `<title> · <class>`. | `toast_after_set` |
| A11 | Title over 80 chars / empty | | S: `maxlength=80`, primary disabled when empty; B: 400 `bad_title`. | `title_bounds` |

## B. Dates and time

| # | Risk | Found | Owner / ruling | Check |
|---|---|---|---|---|
| B1 | BST→GMT boundary (25 Oct 2026) | Server has `ukOffsetMsAt()` (last-Sunday rule, manual) and `londonMidnightInstant`. Client has `Intl`. | S: client converts London date+time → UTC ISO with `Intl.DateTimeFormat('en-GB',{timeZone:'Europe/London'})` offset probing; B: stores timestamptz, formats London manually via `ukOffsetMsAt`. Round-trip test at 24 Oct 23:30, 25 Oct 00:30, 01:30, 26 Oct 07:00. | `bst_boundary_roundtrip` |
| B2 | Server `toLocaleString(timeZone)` crash on Render | Small-ICU Node. | B: banned; lint grep in the backend test refuses `toLocaleString(` with `timeZone`. | backend unit test `no_tz_toLocaleString` |
| B3 | due ≤ release | | B: 400 `bad_due_at`; S: due field outlined + primary disabled. | `due_before_release_rejected` |
| B4 | Release in the past | | B: `release_at ≥ now − 5 min` when "Later"; S: "Now" sends null. | `release_in_past_rejected` |
| B5 | Due > 365 d | | B: 400. | `due_too_far_rejected` |
| B6 | Hold clamp silently moving release | v1 stores `max(requested, open_from)`. | B unchanged; S shows the single factual line `Assignments open 14 Sep 2026` only when the clamp applies (from `/scope`'s `open_from`). | `hold_clamp_single_line` |
| B7 | `datetime-local` on Safari | | S: paired `<input type=date>` + `<input type=time>`. | manual 390px pass |
| B8 | Default due +7 d 18:00, release later default 07:00 | | S computes in London time. | `defaults_london` |

## C. Scope, tier, pathway, pool

| # | Risk | Found | Owner / ruling | Check |
|---|---|---|---|---|
| C1 | Tier spoofing | Class tier governs auto; request tier governs Set work. | B: tier validated against key stage (KS4 foundation/higher; KS3 easy/medium/hard); pathway ALWAYS from the class; a tier not valid for the key stage → 400. | `spoofed_tier_rejected` |
| C2 | Scope spoofing | | B: scope must be a node of the class's tree (pathway + seps subject); else 400 `scope_not_for_class`. | `scope_spoof_rejected` |
| C3 | question_id from another pool/topic | | B: every id re-read from the bank under scope+tier+pathway filters at write; missing → 400 `questions_not_in_scope`. | `foreign_question_rejected` (the meiosis-in-Energy-changes case) |
| C4 | Cohort mixing in multi-class | v1 offered all classes. | B: cohort = (key_stage, science_pathway, science_subject-for-triple); mismatch → 400 `cohort_mismatch`; S offers only cohort matches. | `cohort_mismatch_rejected`, `sheet_offers_same_cohort_only` |
| C5 | Seps class leaks other subjects | | B: `/scope` returns only the class subject's tree for triple classes; S: no subject chips for seps. | `seps_sees_own_subject_only` |
| C6 | Combined leaks `triple_only` | | B: `triple_only=false` filter for combined in every count/preview/swap/write read. | `combined_no_triple_only` |
| C7 | Space physics on combined | `space` is triple-only at topic level in PATHWAY_TOPIC_MAP; all 5 subtopics triple_only. | B: topic omitted from combined trees (all subtopics triple_only ⇒ topic omitted). | `space_absent_on_combined` |
| C8 | Paper map slug mismatch | Slugs: biology cell-biology, organisation, infection-response, bioenergetics (P1); homeostasis, inheritance, ecology (P2). chemistry atomic-structure, bonding, quantitative, chemical-changes, energy-changes (P1); rates-equilibrium, organic, analysis, atmosphere, resources (P2). physics energy, electricity, particle-model, atomic-structure (P1); forces, waves, magnetism (P2); space (triple-only, paper 2 — never on combined). | B: `KS4_PAPER` map keyed by (subject, topic); a topic missing from the map fails the backend unit test. | backend unit test `paper_map_complete` |
| C9 | KS3 band column missing | `ks3_assignment_bank.band` exists: easier/standard/harder, 4 per lesson per band. | Easy=easier, Medium=standard, Hard=harder. | `ks3_three_tiers` |
| C10 | Non-MCQ rows leak | Neither bank has a type column; every row has exactly four options (prod: 0 rows ≠ 4). | B: preview asserts 4 options and one correct; C: loaders refuse otherwise. | `set_work_scope_check` |
| C11 | Tier default wrong for class | Prod: all 38 current KS4 classes match the rule. | B: default = class tier (KS4) / medium (KS3); S shows it selected. | `tier_default_matches_rule` (one Foundation `…Sc5`, one Higher `…Bi1`) |
| C12 | Changing tier does not re-count | | B returns counts for every tier in `/scope`; S re-renders counts in place. | `tier_change_recounts` |
| C13 | "Last set" tag wrong | v1 computed per sow entry. | B: per topic (`scope_ref` topic, or subtopic's topic) from `assignments` where `source='teacher'` and `deleted_at is null`, for THIS class, this academic year. | `last_set_tag` |
| C14 | Round-robin clustering | | B: preview spreads across subtopics round-robin, shuffled within each; prefers ids not set to this class this year. | `spread_across_subtopics` |
| C15 | `academic_week` on teacher rows | Always written from `release_at` (v1). | B unchanged. | existing week drives |

## D. Data model and downstream consumers

| # | Risk | Found | Owner / ruling | Check |
|---|---|---|---|---|
| D1 | Consumers assuming `sow_entry_id` | Column is `source_sow_entry_id`, already nullable and superseded (MRB-239); no consumer joins it. | S/B: none needed; drive renders every consumer with a v2 row anyway. | `consumers_render_null_sow` |
| D2 | `topic` NOT NULL, `subject_id` NOT NULL | v1 wrote `topic` from the sow row. | B writes `topic` = topic title, `subtopic` = subtopic slug or NULL, `subject_id` = the science's id (Biology/Chemistry/Physics), `quiz_type` = topic_quiz / subtopic_quiz. | same |
| D3 | Reteach panel / marking grid / digest / print / charts on NULL scope | They read `title`, `topic`, `academic_week`, `due_at`, never the scheme. | D: drive opens each with a v2 assignment. | `consumers_render_null_sow` |
| D4 | Student current-assignment title/subject | reads `title`, `subject_id`, `release_at`. | unchanged | `student_sees_after_release`, `student_404_before_release` |
| D5 | New columns and RLS | RLS is row-level; new columns inherit the row policies; no column grants exist. | B: migration adds `set_tier`, `scope_kind`, `scope_ref`, `subject`, `paper` with CHECKs; rollback pair. | migration verified on TEST then prod |
| D6 | Backfill of v1 rows | Prod has ONE teacher row (8r/Sc1 fixture, 18 Aug) with `source_sow_entry_id` NULL; nothing to derive. TEST has seeded teacher rows with no questions. | B: backfill is a no-op guarded UPDATE (`where source='teacher' and source_sow_entry_id is not null`). | counts before/after |
| D7 | Auto composition regressing when the bank grows | `composeFromBank` takes EVERY row of the band from a lesson until `size`; more rows per lesson-band would change every auto set. | C+B: new rows take `bank_position ≥ 12` (KS4 per subtopic, KS3 per lesson); the AUTO read filters `bank_position < 12` in `bankFor` (JS) and `compose_assignment` (Python) identically; Set work reads all positions. | backend unit test `auto_ignores_positions_ge_12`; `auto_composition_unchanged` drive; `verify_week_truth` |
| D8 | Python↔DB checksum drift | `export_ks4_questions.py --verify` and the KS3 equivalent. | C: `--verify` after every load; checksum recorded in REPORT. | `ks4_pool_check`, export `--verify` |
| D9 | Anon read exposure | Both banks: `authenticated` SELECT only. | M: re-check after load (anon `select count` = 0 rows / 401). | prod read at merge |
| D10 | Class `science_subject` for seps | `classes` has no subject column; teacher-data derives a pill from `class_teachers.subject_id`. | B: add `classes.science_subject` (biology/chemistry/physics/NULL) + `tier_pathway_source` (rule/admin/NULL); BEFORE INSERT trigger fills NULL tier/pathway/subject from the name rule for KS4; BEFORE UPDATE marks `admin` when values change without the source being set. | `tier_rule_trigger` (backend/SQL test on TEST) |
| D11 | Rule overwriting admin values on re-import | roster-import find-or-creates by name → existing rows are not re-inserted. | Trigger fills only NULLs; admin edits set `source='admin'`. | `reimport_keeps_admin_value` |
| D12 | Admin edit not audited | `audit_log` insert pattern exists (`school.assignments_open_from.set`). | B: `POST /api/admin/class-tier` writes `class.tier_pathway.set` with `acting_as_admin: true`, from/to. | `admin_edit_audited` |
| D13 | 17 empty KS4 classes | Expected; Mide importing. | Untouched. | — |
| D14 | Mide's v1 test assignments on prod | None since 7 Sep 00:00 UK; only the 18 Aug 8r/Sc1 fixture row. | Listed in REPORT, untouched. | — |
| D15 | TEST fixture class names not rule-shaped | `10b/Sc1` is labelled combined foundation but the rule reads `Sc1` as higher. | D: rename to `10b/Sc5`; add `10c/Ph1` (seps physics) and keep `10a/Bi1`. | `tier_default_matches_rule` |

## E. Gates, deploy, environment

| # | Risk | Owner / ruling | Check |
|---|---|---|---|
| E1 | `ks4_pool_check` / `ks4_pool_drive` assert "tier from class" for Set work | D: reworded to request-tier for Set work, class-tier for auto. | both gates green |
| E2 | `pool_ownership` on new routes | D: the three v2 routes named in the gate's allowed reads. | `pool_ownership` |
| E3 | Render env / CORS | New routes under the same `app.use(cors)`; no new env. Unauthenticated → 401 (drive against prod after deploy). | `prod_401_unauth` |
| E4 | Immutable cache serving stale JS | Read the `?v=` stamp from the deployed page, fetch with a nonce, `cmp` with the built file. | `check_ks4_live.sh`-style step in the merge log |
| E5 | Gate receipts invalidated by a late byte | Run the slow gates ONCE on the final tree, after the last commit. | `prepush_gate` |
| E6 | Credential drift mistaken for a finding | Env names: `MRB_SET_WORK_PASSWORD` (any), `MRB_THROWAWAY_PASSWORD=mrb326-throwaway`, `MRB_TEST_TEACHER_PASSWORD=mrb293-drive-only`. | — |
| E7 | Disk | 5.2 GB at start; `df -h` before content generation and before gates; no new worktrees for content lanes (they edit files in `set-work-v2` and never build). | — |
| E8 | Concurrent lanes in one worktree | Content lanes edit only `ks4_data/questions/**` and `ks3_data/<unit>/questions_*.py`; site lane alone runs `build_all.py`; commander commits. | — |
| E9 | `pkill -f` | Banned; PIDs captured. | — |
| E10 | Drive presses | `element.click()`, metrics before navigate, one browser per persona, sign in via auth.html. | — |
| E11 | 390px + 1280 sideways scroll on every screen the sheet touches | S + D. | `no_sideways_scroll_390` |
| E12 | Edge function deploy needed? | No: the tier rule is a DB trigger, so roster-import needs no change and no function deploy. | — |
| E13 | `one_pool_per_assignment` NOT VALID | Unchanged; v2 rows carry `band` and no `rung`, so they satisfy it. | — |
| E14 | Teacher pages are generated | The sheet trigger in `teacher_rulings.py` opens `MRBSetWork`; the compiled sheet node returns to DEAD; `teacher_tells`/`teacher_behaviour` updated. | `teacher_behaviour`, `teacher_tells` |
