#!/usr/bin/env python3
"""breakdown_shots.py — headless-Chrome proof for the Answer Breakdown panel
(Mide's item 9, 24 Sep 2026).

    python3 breakdown_shots.py

⚠️ WHY THIS IS A SCREENSHOT SCRIPT AND NOT A REAL-RLS DRIVE, UNLIKE
`set_work_drive.py`. Set work WRITES — `mrb331_fixture.py` spins up a real
TEST-project world specifically so its checks can prove a real INSERT
succeeds under real RLS. The Answer Breakdown panel does not write anything
at all: every read it makes is a plain `SELECT` a teacher's own RLS already
covers (`assignment_submissions`, `assignment_question_attempts`,
`assignment_questions`, `class_members`, the two bank tables), all already
proved by other gates and by production itself. What is NEW and UNPROVED
here is the panel's own rendering — grouping by topic, the tick/cross marks,
the "most of the class got this wrong" flag, the figure, Prev/Next — and
that is a client-side question a real backend round-trip cannot make any
more certain, only slower and more fragile to set up.

So this drives the REAL `shared/breakdown.js` against the REAL compiled
`teacher/student-detail-fixture.html`, with `window.MrBadmusTeacherGuard`
replaced by a tiny in-page fake whose `.from(table)...` chain filters a
canned in-memory dataset the same way PostgREST would filter a real one
(`.eq`/`.is`/`.in`/`.order`/`.limit`, nothing else — the same four
operations `breakdown.js` itself calls). Nothing about `breakdown.js` is
stubbed or bypassed; only the network boundary is.

⚠️ THE FIGURE IS REAL. Rather than fake `window.MRBFigures` too, the canned
data names a real id out of the manifest this page already loads
(`/shared/figures-ks4.js`, served for real by `ks3_browser.serve`), so the
screenshot proves the SAME figure path a live page uses, not a drawing that
only exists in this harness.

── THE FIVE PUPILS, AND WHY EACH ONE ───────────────────────────────────

    Lydia    complete, 2/4 — gets Q2 (has a figure) WRONG: the headline
             "wrong answer with a figure" row.
    Annabel  complete, 1/4 — also wrong on Q1, which the whole class
             mostly missed (see Q1 below).
    Dan      complete, 3/4 — wrong on Q1 only.
    Erin     in_progress, 0/1 so far (only reached Q1) — the "In progress,
             blank answers below" state.
    Femi     no submission row at all — the "Not started" state, and the
             pupil Next lands on last.

Q1 (changes-of-state, no figure): Lydia, Annabel, Dan and Erin all get it
wrong — 4 of 4 answered, 100% wrong, well past the "≥3 answered, ≥50% wrong"
bar, so it is the one row the class-wide flag should appear on. Q2 (same
topic, WITH a figure): only Lydia misses it — 1 of 3 answered, 33% wrong,
below the bar — a deliberate contrast so the screenshot proves the flag is
selective rather than always-on. Q3/Q4 (internal-energy) are mostly right,
to show a second, cleanly-scored topic group.

Screenshots -> $MRB_SHOTS/b/ (falls back to a local `_breakdown_shots/` dir
if the env var is unset), at 1280 and 390:

    01-open-1280.png / 01-open-390.png        the panel on open (Lydia)
    02-wrong-figure-1280.png                  Lydia's Q2 — wrong, with the
                                               figure and the correct answer
    03-topics-1280.png                        the two topic groups, scrolled
                                               to show both tallies
    04-classflag-1280.png                     Q1's "Most of the class got
                                               this wrong" tag
    05-next-erin-1280.png                     Prev/Next -> Erin, in progress
    06-next-femi-1280.png / -390.png          Prev/Next -> Femi, not started
"""

import os
import sys

REPO = os.path.dirname(os.path.abspath(__file__))
os.chdir(REPO)
sys.path.insert(0, REPO)

import ks3_browser as cdp  # noqa: E402

FIXTURE_PATH = "teacher_fixtures/student-detail-fixture.html"

SHOTS_ROOT = os.environ.get("MRB_SHOTS") or os.environ.get("KS3_GATE_TMP")
OUT = os.path.join(SHOTS_ROOT, "b") if SHOTS_ROOT \
    else os.path.join(REPO, "_breakdown_shots")
os.makedirs(OUT, exist_ok=True)

# ── the canned world, and the fake Supabase client that serves it ───────
#
# ⚠️ FOUR OPERATIONS ONLY — `.eq`, `.is`, `.in`, `.order`/`.limit` — because
# those are the only four `shared/breakdown.js` calls. A richer fake would
# be a second implementation of PostgREST filtering to keep in step with;
# this one only has to agree with breakdown.js's OWN four calls, which is
# checked by reading that file, not guessed at.
INJECT_JS = r"""
window.__MRB_BD_PROOF__ = (function () {
  var CLASS_ID = "bd-proof-class";
  var ASSIGNMENT_ID = "bd-proof-assignment";

  var TABLES = {
    classes: [
      { id: CLASS_ID, name: "10h/Ph1", key_stage: "KS4",
        science_pathway: "triple", tier: "higher" }
    ],
    class_members: [
      { class_id: CLASS_ID, student_id: "stu-lydia", left_at: null, deleted_at: null,
        student: { id: "stu-lydia", first_name: "Lydia", last_name: "Adeyemi", deleted_at: null } },
      { class_id: CLASS_ID, student_id: "stu-annabel", left_at: null, deleted_at: null,
        student: { id: "stu-annabel", first_name: "Annabel", last_name: "Brooks", deleted_at: null } },
      { class_id: CLASS_ID, student_id: "stu-dan", left_at: null, deleted_at: null,
        student: { id: "stu-dan", first_name: "Dan", last_name: "Dupont", deleted_at: null } },
      { class_id: CLASS_ID, student_id: "stu-erin", left_at: null, deleted_at: null,
        student: { id: "stu-erin", first_name: "Erin", last_name: "Ekwueme", deleted_at: null } },
      { class_id: CLASS_ID, student_id: "stu-femi", left_at: null, deleted_at: null,
        student: { id: "stu-femi", first_name: "Femi", last_name: "Falade", deleted_at: null } }
    ],
    assignments: [
      { id: ASSIGNMENT_ID, title: "Particle Model of Matter · Changes of State",
        due_at: "2026-09-28T08:00:00Z", release_at: "2026-09-20T11:39:00Z",
        class_id: CLASS_ID }
    ],
    assignment_questions: [
      { id: "q1", assignment_id: ASSIGNMENT_ID, position: 1, source_ref: "changes-of-state", deleted_at: null },
      { id: "q2", assignment_id: ASSIGNMENT_ID, position: 2, source_ref: "changes-of-state", deleted_at: null },
      { id: "q3", assignment_id: ASSIGNMENT_ID, position: 3, source_ref: "internal-energy", deleted_at: null },
      { id: "q4", assignment_id: ASSIGNMENT_ID, position: 4, source_ref: "internal-energy", deleted_at: null }
    ],
    assignment_submissions: [
      { id: "sub-lydia", assignment_id: ASSIGNMENT_ID, student_id: "stu-lydia",
        score: 2, max_score: 4, status: "complete",
        completed_at: "2026-09-23T06:50:00Z", submitted_at: "2026-09-23T06:50:00Z",
        is_late: false, total_time_seconds: 512, deleted_at: null },
      { id: "sub-annabel", assignment_id: ASSIGNMENT_ID, student_id: "stu-annabel",
        score: 1, max_score: 4, status: "complete",
        completed_at: "2026-09-23T15:39:00Z", submitted_at: "2026-09-23T15:39:00Z",
        is_late: false, total_time_seconds: null, deleted_at: null },
      { id: "sub-dan", assignment_id: ASSIGNMENT_ID, student_id: "stu-dan",
        score: 3, max_score: 4, status: "complete",
        completed_at: "2026-09-22T09:00:00Z", submitted_at: "2026-09-22T09:00:00Z",
        is_late: true, total_time_seconds: 640, deleted_at: null },
      { id: "sub-erin", assignment_id: ASSIGNMENT_ID, student_id: "stu-erin",
        score: 0, max_score: 1, status: "in_progress",
        completed_at: null, submitted_at: null, is_late: null,
        total_time_seconds: null, deleted_at: null }
      /* Femi: no row at all -> "Not started". */
    ],
    assignment_question_attempts: [
      // Q1 — the whole class misses it.
      { submission_id: "sub-lydia", question_index: 0,
        question_text: "A beaker of ice is heated until it is all liquid water. What is this change of state called?",
        selected_answer: "Evaporating", correct_answer: "Melting", is_correct: false,
        time_spent_seconds: 38, attempt_number: 1, created_at: "2026-09-23T06:41:00Z",
        question_ref: "bd-proof-bank-q1", selected_option_letter: "B", correct_option_letter: "A",
        rung: null, criteria_met: null, criteria_total: null },
      { submission_id: "sub-annabel", question_index: 0,
        question_text: "A beaker of ice is heated until it is all liquid water. What is this change of state called?",
        selected_answer: "Freezing", correct_answer: "Melting", is_correct: false,
        time_spent_seconds: 71, attempt_number: 1, created_at: "2026-09-23T15:31:00Z",
        question_ref: "bd-proof-bank-q1", selected_option_letter: "C", correct_option_letter: "A",
        rung: null, criteria_met: null, criteria_total: null },
      { submission_id: "sub-dan", question_index: 0,
        question_text: "A beaker of ice is heated until it is all liquid water. What is this change of state called?",
        selected_answer: "Condensing", correct_answer: "Melting", is_correct: false,
        time_spent_seconds: 52, attempt_number: 1, created_at: "2026-09-22T08:51:00Z",
        question_ref: "bd-proof-bank-q1", selected_option_letter: "D", correct_option_letter: "A",
        rung: null, criteria_met: null, criteria_total: null },
      { submission_id: "sub-erin", question_index: 0,
        question_text: "A beaker of ice is heated until it is all liquid water. What is this change of state called?",
        selected_answer: "Evaporating", correct_answer: "Melting", is_correct: false,
        time_spent_seconds: 44, attempt_number: 1, created_at: "2026-09-24T08:01:00Z",
        question_ref: "bd-proof-bank-q1", selected_option_letter: "B", correct_option_letter: "A",
        rung: null, criteria_met: null, criteria_total: null },

      // Q2 — has a figure. Only Lydia misses it.
      { submission_id: "sub-lydia", question_index: 1,
        question_text: "The diagram shows particles in three states. Which label, A, B, C or D, marks a gas?",
        selected_answer: "C", correct_answer: "B", is_correct: false,
        time_spent_seconds: 61, attempt_number: 2, created_at: "2026-09-23T06:43:00Z",
        question_ref: "bd-proof-bank-fig", selected_option_letter: "C", correct_option_letter: "B",
        rung: null, criteria_met: null, criteria_total: null },
      { submission_id: "sub-annabel", question_index: 1,
        question_text: "The diagram shows particles in three states. Which label, A, B, C or D, marks a gas?",
        selected_answer: "B", correct_answer: "B", is_correct: true,
        time_spent_seconds: 40, attempt_number: 1, created_at: "2026-09-23T15:33:00Z",
        question_ref: "bd-proof-bank-fig", selected_option_letter: "B", correct_option_letter: "B",
        rung: null, criteria_met: null, criteria_total: null },
      { submission_id: "sub-dan", question_index: 1,
        question_text: "The diagram shows particles in three states. Which label, A, B, C or D, marks a gas?",
        selected_answer: "B", correct_answer: "B", is_correct: true,
        time_spent_seconds: 33, attempt_number: 1, created_at: "2026-09-22T08:53:00Z",
        question_ref: "bd-proof-bank-fig", selected_option_letter: "B", correct_option_letter: "B",
        rung: null, criteria_met: null, criteria_total: null },

      // Q3 — internal-energy, mostly right.
      { submission_id: "sub-lydia", question_index: 2,
        question_text: "Which two things determine the internal energy of a system?",
        selected_answer: "The kinetic and potential energy of its particles",
        correct_answer: "The kinetic and potential energy of its particles", is_correct: true,
        time_spent_seconds: 29, attempt_number: 1, created_at: "2026-09-23T06:45:00Z",
        question_ref: "bd-proof-bank-q3", selected_option_letter: "A", correct_option_letter: "A",
        rung: null, criteria_met: null, criteria_total: null },
      { submission_id: "sub-annabel", question_index: 2,
        question_text: "Which two things determine the internal energy of a system?",
        selected_answer: "Its temperature only",
        correct_answer: "The kinetic and potential energy of its particles", is_correct: false,
        time_spent_seconds: 58, attempt_number: 1, created_at: "2026-09-23T15:35:00Z",
        question_ref: "bd-proof-bank-q3", selected_option_letter: "B", correct_option_letter: "A",
        rung: null, criteria_met: null, criteria_total: null },
      { submission_id: "sub-dan", question_index: 2,
        question_text: "Which two things determine the internal energy of a system?",
        selected_answer: "The kinetic and potential energy of its particles",
        correct_answer: "The kinetic and potential energy of its particles", is_correct: true,
        time_spent_seconds: 31, attempt_number: 1, created_at: "2026-09-22T08:55:00Z",
        question_ref: "bd-proof-bank-q3", selected_option_letter: "A", correct_option_letter: "A",
        rung: null, criteria_met: null, criteria_total: null },

      // Q4 — internal-energy, everyone who answered gets it right.
      { submission_id: "sub-lydia", question_index: 3,
        question_text: "During a change of state, why does the temperature stay constant while energy is still transferred in?",
        selected_answer: "The energy changes the arrangement of particles, not their speed",
        correct_answer: "The energy changes the arrangement of particles, not their speed", is_correct: true,
        time_spent_seconds: 47, attempt_number: 1, created_at: "2026-09-23T06:48:00Z",
        question_ref: "bd-proof-bank-q4", selected_option_letter: "A", correct_option_letter: "A",
        rung: null, criteria_met: null, criteria_total: null },
      { submission_id: "sub-annabel", question_index: 3,
        question_text: "During a change of state, why does the temperature stay constant while energy is still transferred in?",
        selected_answer: "The energy changes the arrangement of particles, not their speed",
        correct_answer: "The energy changes the arrangement of particles, not their speed", is_correct: true,
        time_spent_seconds: 65, attempt_number: 1, created_at: "2026-09-23T15:38:00Z",
        question_ref: "bd-proof-bank-q4", selected_option_letter: "A", correct_option_letter: "A",
        rung: null, criteria_met: null, criteria_total: null },
      { submission_id: "sub-dan", question_index: 3,
        question_text: "During a change of state, why does the temperature stay constant while energy is still transferred in?",
        selected_answer: "The energy changes the arrangement of particles, not their speed",
        correct_answer: "The energy changes the arrangement of particles, not their speed", is_correct: true,
        time_spent_seconds: 36, attempt_number: 1, created_at: "2026-09-22T08:59:00Z",
        question_ref: "bd-proof-bank-q4", selected_option_letter: "A", correct_option_letter: "A",
        rung: null, criteria_met: null, criteria_total: null }
    ],
    // A real manifest id (`figures-ks4.js`, loaded for real by this page)
    // stands in for the bank's own figure column, so the drawing on screen
    // is the SAME figure path a live page uses, not one invented here.
    ks4_assignment_bank: [
      { id: "bd-proof-bank-fig", figure: "ks4-fig-body-glands-abcd" },
      { id: "bd-proof-bank-q1", figure: null },
      { id: "bd-proof-bank-q3", figure: null },
      { id: "bd-proof-bank-q4", figure: null }
    ]
  };

  function matches(row, filters) {
    for (var i = 0; i < filters.length; i++) { if (!filters[i](row)) { return false; } }
    return true;
  }

  function builder(table) {
    var rows = (TABLES[table] || []).slice();
    var filters = [];
    var limitN = null;
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
      order: function () { return api; },
      limit: function (n) { limitN = n; return api; },
      then: function (resolve) {
        var out = rows.filter(function (r) { return matches(r, filters); });
        if (limitN != null) { out = out.slice(0, limitN); }
        resolve({ data: out, error: null });
      }
    };
    return api;
  }

  window.MrBadmusTeacherGuard = { getClient: function () { return { from: builder }; } };

  return { classId: CLASS_ID, studentIds: {
    lydia: "stu-lydia", annabel: "stu-annabel", dan: "stu-dan",
    erin: "stu-erin", femi: "stu-femi" } };
})();
"""


def shot(pg, name, width):
    height = 1000 if width >= 1280 else 844
    pg.screenshot(os.path.join(OUT, "%s-%d.png" % (name, width)),
                  width=width, height=height, full_page=True)


# ⊕ THE BRIEF'S "no_sideways_scroll_390-style check", RUN AGAINST THE REAL
# PANEL RATHER THAN INFERRED FROM A SCREENSHOT. `document.scrollingElement`
# is the DOCUMENT's own scroller; the panel's `.bd-sheet`/`.bd-body` are
# their OWN `overflow:auto` containers and are supposed to scroll — this
# only asks whether either one dragged the PAGE sideways, the same question
# every other overflow probe in this repo asks.
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


def main():
    if not os.path.exists(FIXTURE_PATH):
        print("breakdown_shots.py: not built — run "
              "`python3 build_teacher_port.py` first.")
        return 1

    server, port = cdp.serve(REPO)
    try:
        with cdp.Browser() as b:
            pg = b.attach()
            pg.set_viewport(1280, 1400)
            pg.goto("http://127.0.0.1:%d/%s" % (port, FIXTURE_PATH), settle=1.2)
            pg.eval(INJECT_JS)

            proof = pg.eval("window.__MRB_BD_PROOF__")
            class_id = proof["classId"]
            students = proof["studentIds"]

            pg.eval(
                "window.MRBBreakdown.open({classId:%s, studentId:%s, "
                "submissionId:'sub-lydia'});"
                % (repr_js(class_id), repr_js(students["lydia"]))
            )
            wait(pg)
            shot(pg, "01-open", 1280)
            assert_no_sideways(pg, 1280, "panel open")
            shot(pg, "01-open", 390)
            assert_no_sideways(pg, 390, "panel open")

            # scroll to Lydia's Q2 — wrong, with the figure — for a close shot
            pg.eval(
                "(function(){var qs=document.querySelectorAll('.bd-q');"
                "if(qs[1]){qs[1].scrollIntoView({block:'center'});}})();"
            )
            wait(pg)
            shot(pg, "02-wrong-figure", 1280)

            pg.eval("document.querySelector('.bd-body').scrollTop=0;")
            wait(pg)
            shot(pg, "03-topics", 1280)

            pg.eval(
                "(function(){var t=document.querySelector('.bd-q-tag.is-classflag');"
                "if(t){t.closest('.bd-q').scrollIntoView({block:'center'});}})();"
            )
            wait(pg)
            shot(pg, "04-classflag", 1280)

            # Roster order is surname order: Adeyemi(Lydia,0), Brooks(Annabel,1),
            # Dupont(Dan,2), Ekwueme(Erin,3), Falade(Femi,4) — three presses
            # from Lydia reaches Erin, a fourth reaches Femi.
            for _ in range(3):
                pg.eval("document.querySelector('[data-mrb-added=\"breakdown-next\"]').click();")
                wait(pg)
            shot(pg, "05-next-erin", 1280)

            pg.eval("document.querySelector('[data-mrb-added=\"breakdown-next\"]').click();")
            wait(pg)
            shot(pg, "06-next-femi", 1280)
            assert_no_sideways(pg, 1280, "not-started pupil")
            shot(pg, "06-next-femi", 390)
            assert_no_sideways(pg, 390, "not-started pupil")

            # The brief's full width sweep — 360 and 820 join 390 and 1280.
            for w in (360, 820):
                pg.set_viewport(w, 900)
                wait(pg)
                assert_no_sideways(pg, w, "not-started pupil")

            errs = pg.console_errors()
            print("\n\U0001f4f7  breakdown_shots — 6 screenshot(s) written to %s" % OUT)
            if errs:
                print("     ⚠️  %d console error(s):" % len(errs))
                for e in errs[:10]:
                    print("        · %s" % e[:200])
            else:
                print("     console stayed quiet")
    finally:
        server.shutdown()
    return 0


def repr_js(s):
    return "'" + str(s).replace("'", "\\'") + "'"


def wait(pg):
    pg.eval("null")
    import time
    time.sleep(0.5)


if __name__ == "__main__":
    sys.exit(main())
