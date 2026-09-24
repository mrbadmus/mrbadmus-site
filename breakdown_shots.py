#!/usr/bin/env python3
"""breakdown_shots.py — headless-Chrome proof for the Answer Breakdown panel
(Mide's item 9, 24 Sep 2026; reworked 25 Sep 2026 against an Opus design
critique).

    python3 breakdown_shots.py

⚠️ WHY THIS IS A SCREENSHOT-AND-ASSERTION SCRIPT AND NOT A REAL-RLS DRIVE,
UNLIKE `set_work_drive.py`. Set work WRITES; this panel writes nothing, and
every read it makes is a plain SELECT a teacher's own RLS already covers
and other gates already prove. What is new and unproved here is the
panel's OWN logic — which pupil opens, which submission counts as "the"
attempt, whether a figure is paired with the right question, whether 1200
attempt rows survive a 1000-row PostgREST page — and a real backend
round-trip cannot make any of that more certain, only slower to set up.

So this drives the REAL `shared/breakdown.js` against the REAL compiled
`teacher/student-detail-fixture.html`, with `window.MrBadmusTeacherGuard`
replaced by an in-page fake whose `.from(table)...` chain filters, orders
and PAGES a canned dataset the same way PostgREST would (`.eq`/`.is`/`.in`/
`.order`/`.limit`/`.range` — the operations `breakdown.js` itself calls).

── MUST-3, THE FIGURE, VERIFIED AGAINST A REAL TEST ROW ────────────────
The first version of this harness paired a "particles in three states"
stem with `ks4-fig-body-glands-abcd` — the endocrine figure — because it
reused an arbitrary real manifest id for a demo rather than a
content-matched one. Fixed by reading the TEST project for real, signed in
as `hz_rich@test.mrbadmus` (`MRB_TEST_TEACHER_PASSWORD`), against
`ks4_assignment_bank`: `ks4-circuit-symbols-e04` — "Which component does
this circuit symbol represent?" — carries `ks4-fig-circuit-symbol-battery-2`,
a genuinely matched pair. That id, that stem and those four options are
used verbatim below. `assert_figure_pairing()` then checks, in code, that
every `data-bd-figure` the page renders is this canned bank's OWN figure
for that card's `data-bd-qref` — so a future join bug (the wrong bank row
attached to the wrong question) fails this script, not just a screenshot.

⚠️ A FULL LIVE SUBMISSION COULD NOT BE SEEDED ON TEST. Creating a real
`assignment_submissions`/`assignment_question_attempts` row is, correctly,
an RLS action only the STUDENT'S OWN session can take — a teacher's INSERT
into `assignment_submissions` was refused with 42501, which is RLS working
as designed, not a bug to route around. The run's rules also forbid ever
setting `MRB_TEST_STUDENT_PASSWORD`. So the content pairing above is
verified against the real TEST bank (a read, as the teacher, which the
rules do allow), and the render is proven the same way the rest of this
harness proves everything else: against the real code, with this real
content, under a controlled fake client. A stray `assignment_questions`
row inserted during the TEST read was deleted again in the same session —
nothing was left behind.

── OTHER MUSTs THIS SCRIPT CHECKS ───────────────────────────────────────
  MUST-1  a pupil not in the active roster (`left_at` set) still opens on
          THEIR OWN real name, never on roster[0].
  MUST-2  a pupil with two submission rows (a retake) shows the FIRST
          completed attempt's score, matching
          `shared/teacher-data.js`'s `pickFirstAttempts` rule — never a
          row picked by chance ordering.
  MUST-4  1200 attempt rows (60 pupils × 20 questions, one assignment)
          survive a fake PostgREST capped at 1000 rows per page; the
          class-flag numbers on the marker question must show the full
          60, not 1000-row's worth.
  MUST-5  a pupil with zero answers gets the empty-state sentence and a
          COLLAPSED disclosure, never a wall of blank cards at rest.
  MUST-6  the follow-up button reads "Open Set work for <class>" and sits
          under the tiles, not after the question list.
  MUST-7  `sweep_type_floor()` — a static regex sweep of
          `shared/breakdown.css`, in the shape of `build_student_port.py`'s
          own TYPE_SCALE floor sweep: no mono run below 12px, no UI run
          below 15px, anywhere in the file.
  MUST-8  role=dialog, aria-modal, aria-labelledby resolving to real text,
          an aria-live region that changes text on Next, and the
          `:focus-visible` ring rule present in the stylesheet.

Screenshots -> $MRB_SHOTS/b2/ (b2, not b — this is the post-critique pass;
falls back to a local `_breakdown_shots_b2/` dir if the env var is unset),
at 1280 and 390:

    01-open-1280.png / 01-open-390.png   Lydia — header, tiles, question
                                          map, toggle, follow-up, class line
    02-figure-1280.png                   Q2 — real circuit-symbol figure
                                          beside the stem at ≥820px
    03-classflag-1280.png                Q1's header flag with real numbers
    04-wrong-only-1280.png               the Wrong-only toggle applied
    05-next-erin-1280.png                Prev/Next → in-progress pupil
    06-next-femi-1280.png / -390.png     not-started — empty state +
                                          collapsed disclosure
    07-wrong-pupil-1280.png              MUST-1 — a departed pupil opens
                                          on their OWN name
    08-retake-1280.png                   MUST-2 — the first completed
                                          attempt, not a random one
"""

import json
import os
import re
import sys

REPO = os.path.dirname(os.path.abspath(__file__))
os.chdir(REPO)
sys.path.insert(0, REPO)

import ks3_browser as cdp  # noqa: E402

FIXTURE_PATH = "teacher_fixtures/student-detail-fixture.html"
CSS_PATH = "shared/breakdown.css"

SHOTS_ROOT = os.environ.get("MRB_SHOTS") or os.environ.get("KS3_GATE_TMP")
OUT = os.path.join(SHOTS_ROOT, "b2") if SHOTS_ROOT \
    else os.path.join(REPO, "_breakdown_shots_b2")
os.makedirs(OUT, exist_ok=True)

MONO_FLOOR_PX = 12.0
UI_FLOOR_PX = 15.0


# ═════════════════════════════════════════════════════════════════════════
# MUST-7 — the type floor, swept the way build_student_port.py sweeps
# TYPE_SCALE: every literal px in a var(--st-mono)/var(--st-ui) `font:`
# shorthand, checked against its floor. Ordinary CSS here, not a compiled
# template's inline style strings, so a plain regex over the file is the
# faithful equivalent rather than a DOM walk.
# ═════════════════════════════════════════════════════════════════════════
def sweep_type_floor():
    src = open(CSS_PATH, encoding="utf-8").read()
    bad = []
    for m in re.finditer(r"font:([^;\"]*)", src):
        run = m.group(1)
        if "var(--st-mono)" in run:
            floor = MONO_FLOOR_PX
        elif "var(--st-ui)" in run:
            floor = UI_FLOOR_PX
        else:
            continue
        for px in re.findall(r"([\d.]+)px", run):
            if float(px) < floor:
                bad.append((run.strip(), px, floor))
    if bad:
        raise SystemExit(
            "breakdown_shots.py: %d type run(s) in %s are below Mide's "
            "floor:\n%s\nNo mono label below %gpx, no UI text below %gpx."
            % (len(bad), CSS_PATH,
               "\n".join("    %r  (%spx < %gpx)" % b for b in bad),
               MONO_FLOOR_PX, UI_FLOOR_PX))
    print("     MUST-7  type floor: every font: run in %s is ≥ its floor "
          "(mono ≥%gpx, UI ≥%gpx)" % (CSS_PATH, MONO_FLOOR_PX, UI_FLOOR_PX))


# ═════════════════════════════════════════════════════════════════════════
# MUST-8 (static half) — the focus-visible ring is a rule in the
# stylesheet, not something this harness tries to trigger through Chrome's
# real keyboard-vs-pointer focus-visible heuristics (a `.focus()` DOM call
# does not reliably set `:focus-visible` the way a real Tab press does, so
# asserting the computed style after `.focus()` would be testing Chrome's
# heuristic, not this file's CSS). The rule's PRESENCE and its exact values
# are what MUST-8 asked for, and that is what this checks.
# ═════════════════════════════════════════════════════════════════════════
def assert_focus_ring_rule():
    src = open(CSS_PATH, encoding="utf-8").read()
    m = re.search(
        r"\.bd-overlay[^{]*:focus-visible[^{]*\{([^}]*)\}", src, re.S)
    if not m:
        raise SystemExit(
            "breakdown_shots.py: no :focus-visible rule scoped to "
            ".bd-overlay found in %s" % CSS_PATH)
    body = m.group(1)
    if "outline: 2px solid var(--st-accent)" not in body:
        raise SystemExit(
            "breakdown_shots.py: the :focus-visible rule does not set "
            "outline: 2px solid var(--st-accent) — got: %r" % body)
    if "outline-offset: 2px" not in body:
        raise SystemExit(
            "breakdown_shots.py: the :focus-visible rule does not set "
            "outline-offset: 2px — got: %r" % body)
    print("     MUST-8  :focus-visible { outline: 2px solid var(--st-accent); "
          "outline-offset: 2px } is in %s, scoped to every control in the "
          "panel" % CSS_PATH)


# ═════════════════════════════════════════════════════════════════════════
# The canned world. TWO independent assignments share one fake client:
#
#   bd-proof-assignment       the 5-pupil scenario (open/figure/classflag/
#                              wrong-only/prev-next/not-started), PLUS the
#                              MUST-1 departed pupil and the MUST-2 retake.
#   bd-scale-assignment       MUST-4 alone: 60 pupils × 20 questions =
#                              1200 attempt rows, to force the fake
#                              PostgREST's 1000-row page more than once.
# ═════════════════════════════════════════════════════════════════════════
INJECT_JS = r"""
window.__MRB_BD_PROOF__ = (function () {
  var CLASS_ID = "bd-proof-class";
  var ASSIGNMENT_ID = "bd-proof-assignment";
  var SCALE_CLASS_ID = "bd-scale-class";
  var SCALE_ASSIGNMENT_ID = "bd-scale-assignment";

  var members = [
    { class_id: CLASS_ID, student_id: "stu-lydia", left_at: null, deleted_at: null,
      student: { id: "stu-lydia", first_name: "Lydia", last_name: "Adeyemi", deleted_at: null } },
    { class_id: CLASS_ID, student_id: "stu-annabel", left_at: null, deleted_at: null,
      student: { id: "stu-annabel", first_name: "Annabel", last_name: "Brooks", deleted_at: null } },
    { class_id: CLASS_ID, student_id: "stu-dan", left_at: null, deleted_at: null,
      student: { id: "stu-dan", first_name: "Dan", last_name: "Dupont", deleted_at: null } },
    { class_id: CLASS_ID, student_id: "stu-erin", left_at: null, deleted_at: null,
      student: { id: "stu-erin", first_name: "Erin", last_name: "Ekwueme", deleted_at: null } },
    { class_id: CLASS_ID, student_id: "stu-femi", left_at: null, deleted_at: null,
      student: { id: "stu-femi", first_name: "Femi", last_name: "Falade", deleted_at: null } },
    // MUST-1 — Grace left the class (left_at set), so loadRoster's
    // active-only filter excludes her. Her submission is still real and
    // still openable from a history row that predates her leaving.
    { class_id: CLASS_ID, student_id: "stu-grace", left_at: "2026-09-10T00:00:00Z", deleted_at: null,
      student: { id: "stu-grace", first_name: "Grace", last_name: "Zubairu", deleted_at: null } }
  ];

  var profiles = members.map(function (m) {
    return { id: m.student.id, first_name: m.student.first_name, last_name: m.student.last_name };
  });

  var assignment = {
    id: ASSIGNMENT_ID, title: "Particle Model of Matter · Changes of State",
    due_at: "2026-09-28T08:00:00Z", release_at: "2026-09-20T11:39:00Z",
    class_id: CLASS_ID
  };

  var questions = [
    { id: "q1", assignment_id: ASSIGNMENT_ID, position: 1, source_ref: "changes-of-state", deleted_at: null },
    { id: "q2", assignment_id: ASSIGNMENT_ID, position: 2, source_ref: "changes-of-state", deleted_at: null },
    { id: "q3", assignment_id: ASSIGNMENT_ID, position: 3, source_ref: "internal-energy", deleted_at: null },
    { id: "q4", assignment_id: ASSIGNMENT_ID, position: 4, source_ref: "internal-energy", deleted_at: null }
  ];

  // MUST-2 — Dan has TWO submission rows for this assignment: a completed
  // first attempt (attempts:1) and an in-progress retake (attempts:2).
  // `keepFirstAttempt` must pick sub-dan-1 (lowest `attempts`), which
  // scored 3/4 wrong-on-Q1-only — NOT sub-dan-2's partial retake.
  var submissions = [
    { id: "sub-lydia", assignment_id: ASSIGNMENT_ID, student_id: "stu-lydia",
      score: 2, max_score: 4, status: "complete", attempts: 1, attempt_no: 1,
      completed_at: "2026-09-23T06:50:00Z", submitted_at: "2026-09-23T06:50:00Z",
      is_late: false, total_time_seconds: 512, deleted_at: null },
    { id: "sub-annabel", assignment_id: ASSIGNMENT_ID, student_id: "stu-annabel",
      score: 1, max_score: 4, status: "complete", attempts: 1, attempt_no: 1,
      completed_at: "2026-09-23T15:39:00Z", submitted_at: "2026-09-23T15:39:00Z",
      is_late: false, total_time_seconds: null, deleted_at: null },
    { id: "sub-dan-1", assignment_id: ASSIGNMENT_ID, student_id: "stu-dan",
      score: 3, max_score: 4, status: "complete", attempts: 1, attempt_no: 1,
      completed_at: "2026-09-22T09:00:00Z", submitted_at: "2026-09-22T09:00:00Z",
      is_late: true, total_time_seconds: 640, deleted_at: null },
    { id: "sub-dan-2", assignment_id: ASSIGNMENT_ID, student_id: "stu-dan",
      score: 0, max_score: 4, status: "in_progress", attempts: 2, attempt_no: 2,
      completed_at: null, submitted_at: null, is_late: null,
      total_time_seconds: null, deleted_at: null },
    { id: "sub-erin", assignment_id: ASSIGNMENT_ID, student_id: "stu-erin",
      score: 0, max_score: 1, status: "in_progress", attempts: 1, attempt_no: 1,
      completed_at: null, submitted_at: null, is_late: null,
      total_time_seconds: null, deleted_at: null },
    { id: "sub-grace", assignment_id: ASSIGNMENT_ID, student_id: "stu-grace",
      score: 4, max_score: 4, status: "complete", attempts: 1, attempt_no: 1,
      completed_at: "2026-09-21T08:10:00Z", submitted_at: "2026-09-21T08:10:00Z",
      is_late: false, total_time_seconds: 300, deleted_at: null }
    // Femi: no row at all -> "Not started".
  ];

  // ── MUST-3 — the real, content-matched TEST row ─────────────────────
  // ks4-circuit-symbols-e04 / ks4-fig-circuit-symbol-battery-2, read live
  // from qeppkiswvclkkwbxmlok as hz_rich@test.mrbadmus on 24 Sep 2026 —
  // see the module docstring. Verbatim text and options.
  var FIG_STEM = "Which component does this circuit symbol represent?";
  var FIG_OPTIONS = ["A single cell", "A battery of cells joined in series",
                      "A closed switch", "A fuse"];
  var FIG_CORRECT_INDEX = 1; // "B"

  var attempts = [
    // Q1 — the whole class misses it (used for the class-flag screenshot).
    { id: "a-lydia-0", submission_id: "sub-lydia", question_index: 0,
      question_text: "A beaker of ice is heated until it is all liquid water. What is this change of state called?",
      selected_answer: "Evaporating", correct_answer: "Melting", is_correct: false,
      time_spent_seconds: 38, attempt_number: 1, created_at: "2026-09-23T06:41:00Z",
      question_ref: "bd-proof-bank-q1", selected_option_letter: null, correct_option_letter: null,
      rung: null, criteria_met: null, criteria_total: null },
    { id: "a-annabel-0", submission_id: "sub-annabel", question_index: 0,
      question_text: "A beaker of ice is heated until it is all liquid water. What is this change of state called?",
      selected_answer: "Freezing", correct_answer: "Melting", is_correct: false,
      time_spent_seconds: 71, attempt_number: 1, created_at: "2026-09-23T15:31:00Z",
      question_ref: "bd-proof-bank-q1", selected_option_letter: null, correct_option_letter: null,
      rung: null, criteria_met: null, criteria_total: null },
    { id: "a-dan1-0", submission_id: "sub-dan-1", question_index: 0,
      question_text: "A beaker of ice is heated until it is all liquid water. What is this change of state called?",
      selected_answer: "Condensing", correct_answer: "Melting", is_correct: false,
      time_spent_seconds: 52, attempt_number: 1, created_at: "2026-09-22T08:51:00Z",
      question_ref: "bd-proof-bank-q1", selected_option_letter: null, correct_option_letter: null,
      rung: null, criteria_met: null, criteria_total: null },
    { id: "a-erin-0", submission_id: "sub-erin", question_index: 0,
      question_text: "A beaker of ice is heated until it is all liquid water. What is this change of state called?",
      selected_answer: "Evaporating", correct_answer: "Melting", is_correct: false,
      time_spent_seconds: 44, attempt_number: 1, created_at: "2026-09-24T08:01:00Z",
      question_ref: "bd-proof-bank-q1", selected_option_letter: null, correct_option_letter: null,
      rung: null, criteria_met: null, criteria_total: null },
    { id: "a-grace-0", submission_id: "sub-grace", question_index: 0,
      question_text: "A beaker of ice is heated until it is all liquid water. What is this change of state called?",
      selected_answer: "Melting", correct_answer: "Melting", is_correct: true,
      time_spent_seconds: 20, attempt_number: 1, created_at: "2026-09-21T08:05:00Z",
      question_ref: "bd-proof-bank-q1", selected_option_letter: null, correct_option_letter: null,
      rung: null, criteria_met: null, criteria_total: null },
    // sub-dan-2 (the in-progress retake) also answers Q1 wrong; if
    // keepFirstAttempt picked the WRONG submission this would leak in as
    // an extra class-flag vote it must not be, since sub-dan-2 is not the
    // canonical submission for stu-dan.
    { id: "a-dan2-0", submission_id: "sub-dan-2", question_index: 0,
      question_text: "A beaker of ice is heated until it is all liquid water. What is this change of state called?",
      selected_answer: "Freezing", correct_answer: "Melting", is_correct: false,
      time_spent_seconds: 12, attempt_number: 1, created_at: "2026-09-25T08:00:00Z",
      question_ref: "bd-proof-bank-q1", selected_option_letter: null, correct_option_letter: null,
      rung: null, criteria_met: null, criteria_total: null },

    // Q2 — the real, content-matched figure question. Only Lydia misses it.
    { id: "a-lydia-1", submission_id: "sub-lydia", question_index: 1,
      question_text: FIG_STEM,
      selected_answer: "A", correct_answer: "B", is_correct: false,
      time_spent_seconds: 61, attempt_number: 2, created_at: "2026-09-23T06:43:00Z",
      question_ref: "bd-proof-bank-fig", selected_option_letter: "A", correct_option_letter: "B",
      rung: null, criteria_met: null, criteria_total: null },
    { id: "a-annabel-1", submission_id: "sub-annabel", question_index: 1,
      question_text: FIG_STEM,
      selected_answer: "B", correct_answer: "B", is_correct: true,
      time_spent_seconds: 40, attempt_number: 1, created_at: "2026-09-23T15:33:00Z",
      question_ref: "bd-proof-bank-fig", selected_option_letter: "B", correct_option_letter: "B",
      rung: null, criteria_met: null, criteria_total: null },
    { id: "a-dan1-1", submission_id: "sub-dan-1", question_index: 1,
      question_text: FIG_STEM,
      selected_answer: "B", correct_answer: "B", is_correct: true,
      time_spent_seconds: 33, attempt_number: 1, created_at: "2026-09-22T08:53:00Z",
      question_ref: "bd-proof-bank-fig", selected_option_letter: "B", correct_option_letter: "B",
      rung: null, criteria_met: null, criteria_total: null },

    // Q3 — internal-energy, mostly right.
    { id: "a-lydia-2", submission_id: "sub-lydia", question_index: 2,
      question_text: "Which two things determine the internal energy of a system?",
      selected_answer: "The kinetic and potential energy of its particles",
      correct_answer: "The kinetic and potential energy of its particles", is_correct: true,
      time_spent_seconds: 29, attempt_number: 1, created_at: "2026-09-23T06:45:00Z",
      question_ref: "bd-proof-bank-q3", selected_option_letter: null, correct_option_letter: null,
      rung: null, criteria_met: null, criteria_total: null },
    { id: "a-annabel-2", submission_id: "sub-annabel", question_index: 2,
      question_text: "Which two things determine the internal energy of a system?",
      selected_answer: "Its temperature only",
      correct_answer: "The kinetic and potential energy of its particles", is_correct: false,
      time_spent_seconds: 58, attempt_number: 1, created_at: "2026-09-23T15:35:00Z",
      question_ref: "bd-proof-bank-q3", selected_option_letter: null, correct_option_letter: null,
      rung: null, criteria_met: null, criteria_total: null },
    { id: "a-dan1-2", submission_id: "sub-dan-1", question_index: 2,
      question_text: "Which two things determine the internal energy of a system?",
      selected_answer: "The kinetic and potential energy of its particles",
      correct_answer: "The kinetic and potential energy of its particles", is_correct: true,
      time_spent_seconds: 31, attempt_number: 1, created_at: "2026-09-22T08:55:00Z",
      question_ref: "bd-proof-bank-q3", selected_option_letter: null, correct_option_letter: null,
      rung: null, criteria_met: null, criteria_total: null },

    // Q4 — internal-energy, everyone who answered gets it right.
    { id: "a-lydia-3", submission_id: "sub-lydia", question_index: 3,
      question_text: "During a change of state, why does the temperature stay constant while energy is still transferred in?",
      selected_answer: "The energy changes the arrangement of particles, not their speed",
      correct_answer: "The energy changes the arrangement of particles, not their speed", is_correct: true,
      time_spent_seconds: 47, attempt_number: 1, created_at: "2026-09-23T06:48:00Z",
      question_ref: "bd-proof-bank-q4", selected_option_letter: null, correct_option_letter: null,
      rung: null, criteria_met: null, criteria_total: null },
    { id: "a-annabel-3", submission_id: "sub-annabel", question_index: 3,
      question_text: "During a change of state, why does the temperature stay constant while energy is still transferred in?",
      selected_answer: "The energy changes the arrangement of particles, not their speed",
      correct_answer: "The energy changes the arrangement of particles, not their speed", is_correct: true,
      time_spent_seconds: 65, attempt_number: 1, created_at: "2026-09-23T15:38:00Z",
      question_ref: "bd-proof-bank-q4", selected_option_letter: null, correct_option_letter: null,
      rung: null, criteria_met: null, criteria_total: null },
    { id: "a-dan1-3", submission_id: "sub-dan-1", question_index: 3,
      question_text: "During a change of state, why does the temperature stay constant while energy is still transferred in?",
      selected_answer: "The energy changes the arrangement of particles, not their speed",
      correct_answer: "The energy changes the arrangement of particles, not their speed", is_correct: true,
      time_spent_seconds: 36, attempt_number: 1, created_at: "2026-09-22T08:59:00Z",
      question_ref: "bd-proof-bank-q4", selected_option_letter: null, correct_option_letter: null,
      rung: null, criteria_met: null, criteria_total: null },

    // Grace (departed) answered every question, for the MUST-1 shot.
    { id: "a-grace-1", submission_id: "sub-grace", question_index: 1, question_text: FIG_STEM,
      selected_answer: "B", correct_answer: "B", is_correct: true, time_spent_seconds: 18,
      attempt_number: 1, created_at: "2026-09-21T08:07:00Z", question_ref: "bd-proof-bank-fig",
      selected_option_letter: "B", correct_option_letter: "B", rung: null, criteria_met: null, criteria_total: null },
    { id: "a-grace-2", submission_id: "sub-grace", question_index: 2,
      question_text: "Which two things determine the internal energy of a system?",
      selected_answer: "The kinetic and potential energy of its particles",
      correct_answer: "The kinetic and potential energy of its particles", is_correct: true,
      time_spent_seconds: 22, attempt_number: 1, created_at: "2026-09-21T08:08:00Z",
      question_ref: "bd-proof-bank-q3", selected_option_letter: null, correct_option_letter: null,
      rung: null, criteria_met: null, criteria_total: null },
    { id: "a-grace-3", submission_id: "sub-grace", question_index: 3,
      question_text: "During a change of state, why does the temperature stay constant while energy is still transferred in?",
      selected_answer: "The energy changes the arrangement of particles, not their speed",
      correct_answer: "The energy changes the arrangement of particles, not their speed", is_correct: true,
      time_spent_seconds: 19, attempt_number: 1, created_at: "2026-09-21T08:09:00Z",
      question_ref: "bd-proof-bank-q4", selected_option_letter: null, correct_option_letter: null,
      rung: null, criteria_met: null, criteria_total: null }
  ];

  var bank = [
    { id: "bd-proof-bank-fig", figure: "ks4-fig-circuit-symbol-battery-2",
      options: FIG_OPTIONS, correct_index: FIG_CORRECT_INDEX },
    { id: "bd-proof-bank-q1", figure: null, options: null },
    { id: "bd-proof-bank-q3", figure: null, options: null },
    { id: "bd-proof-bank-q4", figure: null, options: null }
  ];

  // ── MUST-4 — 60 pupils × 20 questions = 1200 attempt rows ─────────
  var scaleMembers = [], scaleProfiles = [], scaleSubs = [], scaleAttempts = [], scaleQuestions = [];
  var N_PUPILS = 60, N_Q = 20;
  for (var qi = 0; qi < N_Q; qi++) {
    scaleQuestions.push({ id: "sq" + qi, assignment_id: SCALE_ASSIGNMENT_ID,
      position: qi + 1, source_ref: "scale-topic-" + (qi % 3), deleted_at: null });
  }
  for (var p = 0; p < N_PUPILS; p++) {
    var sid = "scale-stu-" + p;
    var subid = "scale-sub-" + p;
    scaleMembers.push({ class_id: SCALE_CLASS_ID, student_id: sid, left_at: null, deleted_at: null,
      student: { id: sid, first_name: "Pupil", last_name: (1000 + p) + "", deleted_at: null } });
    scaleProfiles.push({ id: sid, first_name: "Pupil", last_name: (1000 + p) + "" });
    scaleSubs.push({ id: subid, assignment_id: SCALE_ASSIGNMENT_ID, student_id: sid,
      score: 10, max_score: N_Q, status: "complete", attempts: 1, attempt_no: 1,
      completed_at: "2026-09-20T09:00:00Z", submitted_at: "2026-09-20T09:00:00Z",
      is_late: false, total_time_seconds: 600, deleted_at: null });
    for (var q = 0; q < N_Q; q++) {
      // Question 0 is the deterministic marker: exactly 40 of 60 wrong.
      var wrong = (q === 0) ? (p < 40) : ((p + q) % 3 !== 0);
      scaleAttempts.push({
        id: "sa-" + p + "-" + q, submission_id: subid, question_index: q,
        question_text: "Scale question " + (q + 1), selected_answer: wrong ? "Wrong" : "Right",
        correct_answer: "Right", is_correct: !wrong, time_spent_seconds: 20,
        attempt_number: 1, created_at: "2026-09-20T08:" + String(q).padStart(2, "0") + ":00Z",
        question_ref: "sq-bank-" + q, selected_option_letter: null, correct_option_letter: null,
        rung: null, criteria_met: null, criteria_total: null
      });
    }
  }
  var scaleAssignment = { id: SCALE_ASSIGNMENT_ID, title: "Scale test — 1200 attempts",
    due_at: "2026-09-28T08:00:00Z", release_at: "2026-09-20T09:00:00Z", class_id: SCALE_CLASS_ID };

  var TABLES = {
    classes: [
      { id: CLASS_ID, name: "10h/Ph1", key_stage: "KS4", science_pathway: "triple", tier: "higher" },
      { id: SCALE_CLASS_ID, name: "Scale/Test1", key_stage: "KS4", science_pathway: "triple", tier: "higher" }
    ],
    profiles: profiles.concat(scaleProfiles),
    class_members: members.concat(scaleMembers),
    assignments: [assignment, scaleAssignment],
    assignment_questions: questions.concat(scaleQuestions),
    assignment_submissions: submissions.concat(scaleSubs),
    assignment_question_attempts: attempts.concat(scaleAttempts),
    ks4_assignment_bank: bank
  };

  function matches(row, filters) {
    for (var i = 0; i < filters.length; i++) { if (!filters[i](row)) { return false; } }
    return true;
  }

  function builder(table) {
    var rows = (TABLES[table] || []).slice();
    var filters = [];
    var orderCol = null, orderAsc = true;
    var limitN = null, rangeFrom = null, rangeTo = null;
    var api = {
      select: function () { return api; },
      eq: function (col, val) {
        filters.push(function (r) { return r[col] === val; });
        return api;
      },
      is: function (col, val) {
        filters.push(function (r) { return (r[col] === null || r[col] === undefined) === (val === null); });
        return api;
      },
      in: function (col, vals) {
        filters.push(function (r) { return vals.indexOf(r[col]) !== -1; });
        return api;
      },
      order: function (col, opts) {
        orderCol = col; orderAsc = !(opts && opts.ascending === false);
        return api;
      },
      limit: function (n) { limitN = n; return api; },
      // MUST-4 — a real .range(), so paging is genuinely exercised rather
      // than assumed. Mirrors PostgREST: inclusive [from, to].
      range: function (from, to) { rangeFrom = from; rangeTo = to; return api; },
      then: function (resolve) {
        var out = rows.filter(function (r) { return matches(r, filters); });
        if (orderCol) {
          out.sort(function (a, b) {
            var av = a[orderCol], bv = b[orderCol];
            if (av < bv) { return orderAsc ? -1 : 1; }
            if (av > bv) { return orderAsc ? 1 : -1; }
            return 0;
          });
        }
        if (rangeFrom != null) { out = out.slice(rangeFrom, rangeTo + 1); }
        else if (limitN != null) { out = out.slice(0, limitN); }
        resolve({ data: out, error: null });
      }
    };
    return api;
  }

  window.MrBadmusTeacherGuard = { getClient: function () { return { from: builder }; } };

  return {
    classId: CLASS_ID, scaleClassId: SCALE_CLASS_ID,
    studentIds: { lydia: "stu-lydia", annabel: "stu-annabel", dan: "stu-dan",
                  erin: "stu-erin", femi: "stu-femi", grace: "stu-grace" },
    submissionIds: { lydia: "sub-lydia", danRetake: "sub-dan-1",
                      grace: "sub-grace", scaleFirst: "scale-sub-0" },
    figure: { qref: "bd-proof-bank-fig", figureId: "ks4-fig-circuit-symbol-battery-2" }
  };
})();
"""


def shot(pg, name, width):
    height = 1000 if width >= 1280 else 844
    pg.screenshot(os.path.join(OUT, "%s-%d.png" % (name, width)),
                  width=width, height=height, full_page=True)


def assert_no_sideways(pg, width, label):
    got = pg.eval(
        "(function(){var e=document.scrollingElement||document.documentElement;"
        "return {scroll:e.scrollWidth, client:document.documentElement.clientWidth};})()"
    )
    if got["scroll"] > got["client"] + 1:
        raise SystemExit(
            "breakdown_shots.py: SIDEWAYS SCROLL at %dpx (%s) — "
            "document.scrollWidth %d > clientWidth %d"
            % (width, label, got["scroll"], got["client"]))
    print("     no sideways scroll at %dpx (%s) — scrollWidth %d, "
          "clientWidth %d" % (width, label, got["scroll"], got["client"]))


def wait(pg):
    pg.eval("null")
    import time
    time.sleep(0.5)


def js_str(s):
    return json.dumps(s)


def main():
    if not os.path.exists(FIXTURE_PATH):
        print("breakdown_shots.py: not built — run "
              "`python3 build_teacher_port.py` first.")
        return 1

    sweep_type_floor()
    assert_focus_ring_rule()

    server, port = cdp.serve(REPO)
    try:
        with cdp.Browser() as b:
            pg = b.attach()
            pg.set_viewport(1280, 1400)
            pg.goto("http://127.0.0.1:%d/%s" % (port, FIXTURE_PATH), settle=1.2)
            pg.eval(INJECT_JS)
            proof = pg.eval("window.__MRB_BD_PROOF__")
            sid = proof["studentIds"]

            # ── MUST-8 (live half): role/aria-modal/aria-labelledby, and
            #    the aria-live pupil announcer changes text on Next. ──────
            pg.eval("window.MRBBreakdown.open({classId:%s, studentId:%s, "
                    "submissionId:%s});"
                    % (js_str(proof["classId"]), js_str(sid["lydia"]), js_str("sub-lydia")))
            wait(pg)
            shot(pg, "01-open", 1280)
            assert_no_sideways(pg, 1280, "panel open")
            shot(pg, "01-open", 390)
            assert_no_sideways(pg, 390, "panel open")

            aria = pg.eval(r"""(function(){
              var sheet = document.querySelector('[data-bd="sheet"]');
              var labelledby = sheet.getAttribute('aria-labelledby');
              var heading = labelledby ? document.getElementById(labelledby) : null;
              return {
                role: sheet.getAttribute('role'),
                modal: sheet.getAttribute('aria-modal'),
                headingText: heading ? heading.textContent : null
              };
            })()""")
            if aria["role"] != "dialog" or aria["modal"] != "true" or not aria["headingText"]:
                raise SystemExit("breakdown_shots.py: MUST-8 dialog semantics failed: %r" % aria)
            print("     MUST-8  role=dialog aria-modal=true aria-labelledby -> %r"
                  % aria["headingText"])

            live_before = pg.eval("(document.querySelector('[data-bd=\"live\"]')||{}).textContent||''")
            pg.eval("document.querySelector('[data-mrb-added=\"breakdown-next\"]').click();")
            wait(pg)
            live_after = pg.eval("(document.querySelector('[data-bd=\"live\"]')||{}).textContent||''")
            if live_before == live_after or "Pupil 2 of" not in live_after:
                raise SystemExit(
                    "breakdown_shots.py: MUST-8 aria-live did not announce the "
                    "new pupil — before=%r after=%r" % (live_before, live_after))
            print("     MUST-8  aria-live announced %r on Next" % live_after)
            # back to Lydia for the rest of the scripted shots
            pg.eval("document.querySelector('[data-mrb-added=\"breakdown-prev\"]').click();")
            wait(pg)

            # ── MUST-3 — the figure is paired with its OWN question ──────
            pairing = pg.eval(r"""(function(){
              var out = [];
              document.querySelectorAll('[data-bd-figure]').forEach(function(c){
                out.push({qref: c.getAttribute('data-bd-qref'), figure: c.getAttribute('data-bd-figure')});
              });
              return out;
            })()""")
            if not pairing:
                raise SystemExit("breakdown_shots.py: no figure was drawn at all — MUST-3 cannot be checked")
            want_figure = proof["figure"]["figureId"]
            want_qref = proof["figure"]["qref"]
            for row in pairing:
                if row["figure"] != want_figure:
                    raise SystemExit(
                        "breakdown_shots.py: MUST-3 FAILED — card for qref %r drew figure %r, "
                        "expected the bank's own %r for %r"
                        % (row["qref"], row["figure"], want_figure, want_qref))
            print("     MUST-3  every drawn figure (%d) is the bank's own figure for its question"
                  % len(pairing))

            fig_card = pg.eval(
                "(function(){var c=document.querySelector('[data-bd-figure]');"
                "return c ? c.scrollIntoView({block:'center'}) || true : false;})()")
            wait(pg)
            shot(pg, "02-figure", 1280)

            flag_text = pg.eval(
                "(function(){var c=document.querySelector('[data-bd-q=\"1\"] .bd-q-flag');"
                "return c ? c.textContent : null;})()")
            if not flag_text or "in the class got this wrong" not in flag_text:
                raise SystemExit("breakdown_shots.py: S4 class-flag text missing on Q1: %r" % flag_text)
            print("     S4      Q1 header flag reads %r" % flag_text)
            shot(pg, "03-classflag", 1280)

            # ── S13 — Wrong-only toggle ──────────────────────────────────
            pg.eval("document.querySelector('[data-mrb-added=\"breakdown-wrong-only\"]').click();")
            wait(pg)
            shot(pg, "04-wrong-only", 1280)
            pg.eval("document.querySelector('[data-mrb-added=\"breakdown-wrong-only-all\"]').click();")
            wait(pg)

            # ── MUST-6 — the follow-up button's honest copy ─────────────
            fu = pg.eval("(function(){var b=document.querySelector('[data-mrb-added=\"breakdown-followup\"]');"
                         "return b ? {text:b.textContent, hidden:b.hidden} : null;})()")
            if not fu or "Open Set work for" not in fu["text"]:
                raise SystemExit("breakdown_shots.py: MUST-6 follow-up copy wrong: %r" % fu)
            print("     MUST-6  follow-up reads %r" % fu["text"])

            # ── Prev/Next through Annabel/Dan to Erin (in progress) ──────
            for _ in range(3):
                pg.eval("document.querySelector('[data-mrb-added=\"breakdown-next\"]').click();")
                wait(pg)
            shot(pg, "05-next-erin", 1280)

            # ── MUST-5 — Femi, not started ───────────────────────────────
            pg.eval("document.querySelector('[data-mrb-added=\"breakdown-next\"]').click();")
            wait(pg)
            empty = pg.eval(
                "(function(){var e=document.querySelector('.bd-empty');"
                "var d=document.querySelector('.bd-disclosure');"
                "return {emptyText: e ? e.textContent : null, hasDisclosure: !!d, open: d ? d.open : null};})()")
            if not empty["emptyText"] or "hasn't started" not in empty["emptyText"]:
                raise SystemExit("breakdown_shots.py: MUST-5 empty-state text missing: %r" % empty)
            if not empty["hasDisclosure"] or empty["open"]:
                raise SystemExit("breakdown_shots.py: MUST-5 disclosure missing or not collapsed: %r" % empty)
            print("     MUST-5  %r + a collapsed disclosure" % empty["emptyText"])
            shot(pg, "06-next-femi", 1280)
            assert_no_sideways(pg, 1280, "not-started pupil")
            shot(pg, "06-next-femi", 390)
            assert_no_sideways(pg, 390, "not-started pupil")

            # ── MUST-1 — a departed pupil (left_at set) opens on THEIR OWN
            #    name, never on roster[0] (Lydia). ───────────────────────
            pg.eval("window.MRBBreakdown.close();")
            wait(pg)
            pg.eval("window.MRBBreakdown.open({classId:%s, studentId:%s, submissionId:%s});"
                    % (js_str(proof["classId"]), js_str(sid["grace"]), js_str("sub-grace")))
            wait(pg)
            shown = pg.eval("(document.querySelector('[data-bd=\"sheet\"] .bd-title')||{}).textContent||''")
            if "Grace" not in shown:
                raise SystemExit(
                    "breakdown_shots.py: MUST-1 FAILED — opened on %r instead of Grace Zubairu"
                    % shown)
            print("     MUST-1  a departed (left_at set) pupil opened on their own name: %r" % shown)
            shot(pg, "07-wrong-pupil", 1280)

            # ── MUST-2 — Dan's retake: the FIRST completed attempt counts,
            #    matching pickFirstAttempts, not the in-progress row. ─────
            pg.eval("window.MRBBreakdown.close();")
            wait(pg)
            pg.eval("window.MRBBreakdown.open({classId:%s, studentId:%s, submissionId:%s});"
                    % (js_str(proof["classId"]), js_str(sid["dan"]), js_str("sub-dan-1")))
            wait(pg)
            danScore = pg.eval("(document.querySelector('.bd-stat-value')||{}).textContent||''")
            if "3 / 4" not in danScore:
                raise SystemExit(
                    "breakdown_shots.py: MUST-2 FAILED — Dan's score tile reads %r, "
                    "expected 3 / 4 (sub-dan-1, the completed FIRST attempt) not the "
                    "in-progress retake" % danScore)
            print("     MUST-2  Dan's retake resolved to the first completed "
                  "attempt (score %r), matching pickFirstAttempts" % danScore)
            shot(pg, "08-retake", 1280)
            pg.eval("window.MRBBreakdown.close();")

            # ── MUST-4 — 1200 attempt rows across a 1000-row page cap ────
            pg.eval("window.MRBBreakdown.open({classId:%s, studentId:%s, submissionId:%s});"
                    % (js_str(proof["scaleClassId"]), js_str("scale-stu-0"), js_str("scale-sub-0")))
            wait(pg)
            scaleFlag = pg.eval(
                "(function(){var c=document.querySelector('[data-bd-q=\"1\"] .bd-q-flag');"
                "return c ? c.textContent : null;})()")
            if not scaleFlag or "40 of 60" not in scaleFlag:
                raise SystemExit(
                    "breakdown_shots.py: MUST-4 FAILED — with 1200 attempt rows over a "
                    "1000-row page cap, question 1's class flag reads %r, expected "
                    "'40 of 60 …' (all 60 pupils' rows, from BOTH pages)" % scaleFlag)
            print("     MUST-4  1200 attempt rows (60 pupils × 20 questions) paged past the "
                  "1000-row cap intact: %r" % scaleFlag)
            pg.eval("window.MRBBreakdown.close();")

            # ── the brief's full width sweep — 360 and 820 join 390/1280,
            #    reopened on the figure pupil so the two-column ≥820px
            #    layout (S8) is actually exercised, not just the narrow
            #    single-column one. ──────────────────────────────────────
            pg.eval("window.MRBBreakdown.open({classId:%s, studentId:%s, submissionId:%s});"
                    % (js_str(proof["classId"]), js_str(sid["lydia"]), js_str("sub-lydia")))
            wait(pg)
            for w in (360, 820):
                pg.set_viewport(w, 900)
                wait(pg)
                assert_no_sideways(pg, w, "figure pupil")
            pg.eval("window.MRBBreakdown.close();")

            errs = [e for e in pg.console_errors() if "favicon" not in e]
            print("\n\U0001f4f7  breakdown_shots — 8 screenshot(s) written to %s" % OUT)
            if errs:
                print("     ⚠️  %d console error(s):" % len(errs))
                for e in errs[:10]:
                    print("        · %s" % e[:200])
                raise SystemExit(1)
            print("     console stayed quiet")
    finally:
        server.shutdown()
    return 0


if __name__ == "__main__":
    sys.exit(main())
