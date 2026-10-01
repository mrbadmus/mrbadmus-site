#!/usr/bin/env python3
"""MRB-351 §5 — drive `teacher/flashcards.html`, one flashcard set's progress.

    python3 flashcard_progress_drive.py              # everything
    python3 flashcard_progress_drive.py --shots DIR  # screenshots somewhere else

It drives the REAL page (served from the repo root) with a STUBBED client:
`window.supabase` answers `flashcard_progress`, `flashcard_pupil_detail` and
`flashcard_edit_assignment` from fixtures shaped exactly like the SQL in
20260924180100_mrb351_flashcards_functions.sql, and `fetch` records the
fire-and-forget answer-check call. Nothing is written to either project.

What it proves:
  · the default sort is least progress first (Missing, Not started, In
    progress by secured, Done late, Done), and every column sorts both ways
    with `aria-sort` saying so;
  · make mode shows Made, review mode does not; no Answers column in either
    (Sharpen B2), and no chips under the title (B1);
  · the per-pupil panel (shared/flashcard-breakdown.js, Sharpen B3): the
    centred shell, prev/next in table order, per card one state chip, the
    latest written answer + verdict, the model answer, Tries, a closed
    History; both the MRB-352 keys and the old function's degrade;
  · polling flips a row to Done on an open tab, without a reload;
  · the CSV is the table as displayed, UTF-8 with a BOM;
  · Rushed is a small inline marker, never a block;
  · no horizontal page scroll at 360 / 390, the table scrolls in its own box
    and the pupil column is sticky;
  · no explanatory copy, no mono label under 12px, tap targets >= 44px;
  · and, separately, that teacher-live.js's `cellOf` never grades a
    flashcard set: one MCQ paper at 50% and one flashcard set at 100% give a
    class mean and pupil averages of 50; and that `buildRoster`'s `lastIso`
    folds in a flashcard SITTING (not just a completed cell) via GREATEST,
    outranking an older completion and standing alone for a sitting-only
    pupil — the JS twin of `teacher_class_rollup_v2`
    (20260927100000_mrb351_rollup_v2_live_results_kinds.sql, which
    superseded 20260924180200_mrb351_rollup_kind.sql's edit to v1).

Exits non-zero on any failure.
"""

import argparse, json, os, re, sys, time
from datetime import datetime, timedelta, timezone

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import ks3_browser as cdp

TEACHER = "11111111-1111-4111-8111-111111111111"
ASSIGN = "aaaaaaaa-0000-4000-8000-000000000001"
CLASS = "cccccccc-0000-4000-8000-000000000001"


def iso(dt):
    return dt.astimezone(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S+00:00")


NOW = datetime.now(timezone.utc)


def pupil(pid, first, last, status, made, known, secured, sittings, active,
          think, rushed, last_ago, answers, completed=None):
    return {"pupil_id": pid, "first_name": first, "last_name": last,
            "display_name": first, "status": status, "made": made,
            "known": known, "secured": secured, "sittings": sittings,
            "active_ms": active, "median_think_ms": think,
            "median_write_ms": None, "rushed": rushed,
            "last_active": iso(NOW - last_ago) if last_ago is not None else None,
            "answers": dict(zip(["match", "partial", "no", "blank", "pending"], answers)),
            "completed_at": completed}


def progress(mode="make", rule="secure", phase=1):
    ps = [
        pupil("p-ann", "Ann", "Able", "done", 10, 10, 10, 2, 612000, 4200, False,
              timedelta(minutes=3), [8, 1, 1, 0, 0], iso(NOW)),
        pupil("p-ben", "Ben", "Brown", "in_progress", 10, 7, 5, 1, 300000, 2500, False,
              timedelta(days=1, hours=1), [5, 2, 2, 1, 0]),
        pupil("p-cat", "Cat", "Cole", "in_progress", 6, 3, 2, 1, 125000, 900, True,
              timedelta(minutes=70), [2, 1, 1, 0, 2]),
        pupil("p-dan", "Dan", "Dale", "not_started", 0, 0, 0, 0, 0, None, False,
              None, [0, 0, 0, 0, 0]),
        pupil("p-eve", "Eve", "Eyre", "done_late", 10, 10, 10, 3, 900000, 5100, False,
              timedelta(days=2), [9, 1, 0, 0, 0], iso(NOW)),
        # ⊕ Design port A five-state follow-up — made/known/secured match
        # DETAIL_MIX exactly (2 secured + 2 got_it = 4 known, 8/10 made).
        pupil("p-fay", "Fay", "Ford", "missing", 8, 4, 2, 1, 60000, 3000, False,
              timedelta(days=3), [1, 0, 1, 1, 0]),
    ]
    if phase == 2:
        for p in ps:
            if p["pupil_id"] == "p-cat":
                p.update(status="done", made=10, known=10, secured=10, sittings=2,
                         completed_at=iso(NOW), last_active=iso(NOW))
    done = sum(1 for p in ps if p["status"] in ("done", "done_late"))
    return {
        "assignment": {"id": ASSIGN, "title": "Atomic structure", "class_id": CLASS,
                       "class_name": "8r/Sc1", "mode": mode, "rule": rule,
                       # 15:00 London (BST) on Friday 3 October 2026
                       "due_at": "2026-10-03T14:00:00+00:00",
                       "release_at": "2026-09-21T06:00:00+00:00",
                       "note": "Bring your planner", "deck_id": "dddddddd-0000-4000-8000-000000000001"},
        "n": 10, "now": iso(NOW),
        "class": {"pupils": len(ps), "done": done,
                  "completion_pct": round(done / len(ps) * 100),
                  "avg_sittings": 1.6,
                  "reteach": [
                      {"card_id": "c2", "position": 1, "question": "Name the particle with no charge",
                       "answer": "Neutron", "not_yet": 4},
                      {"card_id": "c1", "position": 0, "question": "What is the formula of carbon dioxide? CO2",
                       "answer": "CO2", "not_yet": 2}]},
        "pupils": ps,
    }


DETAIL_BEN = {
    "pupil": {"id": "p-ben", "first_name": "Ben", "last_name": "Brown", "display_name": "Ben"},
    "cards": [
        {"id": "c1", "position": 0, "question": "What is the formula of carbon dioxide?",
         "answer": "CO2", "mine": "CO2 gas", "check": "match", "written_ms": 34000,
         "secured": True, "known": True, "shown": 4,
         "ratings": [{"rating": "nearly", "phase": "make", "at": iso(NOW - timedelta(days=1, hours=2)), "think_ms": 3000, "session_id": "s1"},
                     {"rating": "got_it", "phase": "review", "at": iso(NOW - timedelta(days=1, hours=1)), "think_ms": 2000, "session_id": "s1"},
                     {"rating": "got_it", "phase": "review", "at": iso(NOW - timedelta(days=1)), "think_ms": 1800, "session_id": "s2"}]},
        {"id": "c2", "position": 1, "question": "Name the particle with no charge",
         "answer": "Neutron", "mine": "electron", "check": "no", "written_ms": 12000,
         "secured": False, "known": False,
         "ratings": [{"rating": "not_yet", "phase": "make", "at": iso(NOW - timedelta(days=1, hours=2)), "think_ms": 900, "session_id": "s1"},
                     {"rating": "not_yet", "phase": "review", "at": iso(NOW - timedelta(days=1, hours=1)), "think_ms": 700, "session_id": "s1"},
                     # ⊕ Sharpen B3 — the MRB-352 keys: a review rating that
                     # carried a typed answer (the panel's latest answer).
                     {"rating": "nearly", "phase": "review", "at": iso(NOW - timedelta(days=1)), "think_ms": 800, "session_id": "s2",
                      "answer": "a neutron", "answer_check": "match"}]},
        {"id": "c3", "position": 2, "question": "What is the charge on a proton?",
         "answer": "+1", "mine": "positive", "check": "pending", "written_ms": 8000,
         "secured": False, "known": True, "ratings": []},
    ],
    "sessions": [
        {"id": "s1", "started_at": iso(NOW - timedelta(days=1, hours=2)),
         "ended_at": iso(NOW - timedelta(days=1, hours=1)), "open": False,
         "active_ms": 240000, "cards_seen": 10, "cards_rated": 12, "cards_made": 10,
         "median_think_ms": 2500, "rushed": False},
        {"id": "s2", "started_at": iso(NOW - timedelta(days=1)),
         "ended_at": iso(NOW - timedelta(hours=23)), "open": False,
         "active_ms": 60000, "cards_seen": 10, "cards_rated": 10, "cards_made": 0,
         "median_think_ms": 700, "rushed": True},
    ],
}

# ⊕ Sharpen B3 — a pupil read through the PRE-MRB-352 function: no `shown`,
# no `answer`/`answer_check` on any rating. Drives the degrade branches.
DETAIL_CAT = {
    "pupil": {"id": "p-cat", "first_name": "Cat", "last_name": "Cole", "display_name": "Cat"},
    "cards": [
        {"id": "c1", "position": 0, "question": "What is the formula of carbon dioxide?",
         "answer": "CO2", "mine": "C O 2", "check": "partial", "written_ms": 20000,
         "secured": False, "known": True,
         "ratings": [{"rating": "got_it", "phase": "make", "at": iso(NOW - timedelta(hours=2)), "think_ms": 900, "session_id": "s9"},
                     {"rating": "got_it", "phase": "review", "at": iso(NOW - timedelta(hours=1)), "think_ms": 800, "session_id": "s9"}]},
        {"id": "c2", "position": 1, "question": "Name the particle with no charge",
         "answer": "Neutron", "mine": None, "check": None, "written_ms": None,
         "secured": False, "known": False, "ratings": []},
        # a BLANK make answer: "" with check `blank` is still an answer
        {"id": "c3", "position": 2, "question": "What is the charge on a proton?",
         "answer": "+1", "mine": "", "check": "blank", "written_ms": 4000,
         "secured": False, "known": False, "ratings": []},
    ],
    "sessions": [
        {"id": "s9", "started_at": iso(NOW - timedelta(hours=2)), "ended_at": iso(NOW - timedelta(hours=1)),
         "open": False, "active_ms": 125000, "cards_seen": 2, "cards_rated": 2, "cards_made": 1,
         "median_think_ms": 900, "rushed": True}],
}

# ⊕ Fable review — a REVIEW-mode pupil read through the pre-MRB-352
# function: rated cards with no `answer` on any rating and no `mine`. The
# panel must NOT say "No written answer" on those (it cannot know); only the
# untouched card says it.
DETAIL_REVIEW = {
    "pupil": {"id": "p-ben", "first_name": "Ben", "last_name": "Brown", "display_name": "Ben"},
    "cards": [
        {"id": "c1", "position": 0, "question": "What is the formula of carbon dioxide?",
         "answer": "CO2", "mine": None, "check": None, "written_ms": None,
         "secured": True, "known": True,
         "ratings": [{"rating": "got_it", "phase": "review", "at": iso(NOW - timedelta(hours=3)), "think_ms": 2000, "session_id": "r1"},
                     {"rating": "got_it", "phase": "review", "at": iso(NOW - timedelta(hours=2)), "think_ms": 1800, "session_id": "r1"}]},
        {"id": "c2", "position": 1, "question": "Name the particle with no charge",
         "answer": "Neutron", "mine": None, "check": None, "written_ms": None,
         "secured": False, "known": False,
         "ratings": [{"rating": "not_yet", "phase": "review", "at": iso(NOW - timedelta(hours=2)), "think_ms": 700, "session_id": "r1"}]},
        {"id": "c3", "position": 2, "question": "What is the charge on a proton?",
         "answer": "+1", "mine": None, "check": None, "written_ms": None,
         "secured": False, "known": False, "ratings": []},
    ],
    "sessions": [{"id": "r1", "started_at": iso(NOW - timedelta(hours=3)), "ended_at": iso(NOW - timedelta(hours=2)),
                  "open": False, "active_ms": 90000, "cards_seen": 3, "cards_rated": 3, "cards_made": 0,
                  "median_think_ms": 1800, "rushed": False}],
}

# ⊕ MRB-353 — a ready-made (review) deck read through the CURRENT function:
# typed review answers, one checked 20 s ago and still pending (a check IS
# in flight → "Checking"), one pending from 3 minutes ago (no check in
# flight → no chip), one decided.
DETAIL_FRESH = {
    "pupil": {"id": "p-cat", "first_name": "Cat", "last_name": "Cole", "display_name": "Cat"},
    "cards": [
        {"id": "f1", "position": 0, "question": "What is the unit of charge?", "answer": "The coulomb (C)",
         "mine": None, "check": None, "written_ms": None, "secured": False, "known": False, "shown": 1,
         "ratings": [{"rating": "nearly", "phase": "review", "at": iso(NOW - timedelta(seconds=20)), "think_ms": 900,
                      "session_id": "q1", "answer": "coulombs I think", "answer_check": "pending"}]},
        {"id": "f2", "position": 1, "question": "What is the unit of current?", "answer": "The ampere (A)",
         "mine": None, "check": None, "written_ms": None, "secured": False, "known": False, "shown": 1,
         "ratings": [{"rating": "not_yet", "phase": "review", "at": iso(NOW - timedelta(minutes=3)), "think_ms": 900,
                      "session_id": "q1", "answer": "volts maybe", "answer_check": "pending"}]},
        {"id": "f3", "position": 2, "question": "What is the unit of resistance?", "answer": "The ohm",
         "mine": None, "check": None, "written_ms": None, "secured": False, "known": True, "shown": 2,
         "ratings": [{"rating": "got_it", "phase": "review", "at": iso(NOW - timedelta(minutes=4)), "think_ms": 900,
                      "session_id": "q1", "answer": "it is the ohm", "answer_check": "match"},
                     {"rating": "got_it", "phase": "review", "at": iso(NOW - timedelta(minutes=2)), "think_ms": 800,
                      "session_id": "q1", "answer": "ohms", "answer_check": "match"}]},
    ],
    "sessions": [{"id": "q1", "started_at": iso(NOW - timedelta(minutes=5)), "ended_at": iso(NOW - timedelta(seconds=15)),
                  "open": True, "active_ms": 90000, "cards_seen": 3, "cards_rated": 4, "cards_made": 0,
                  "median_think_ms": 900, "rushed": False}],
}

# ⊕ Design port A five-state follow-up, 30 Sep 2026 — Fay's real per-card
# detail: exactly two of each state (Secured/Got it/Nearly/Not yet/Not
# seen), so the progress table's strip is proved drawing all five kinds of
# cell from one row, not just exercising each state across different rows.
# Fay's own `pupil(...)` row below is updated to made=8/known=4/secured=2
# to match (2 secured + 2 got_it = 4 known; 8 of 10 cards have a written
# answer).
DETAIL_MIX = {
    "pupil": {"id": "p-fay", "first_name": "Fay", "last_name": "Ford", "display_name": "Fay"},
    "cards": [
        {"id": "m1", "position": 0, "question": "Mix Q1 — secured", "answer": "A1",
         "mine": "a1", "check": "match", "written_ms": 4000, "secured": True, "known": True, "shown": 2,
         "ratings": [{"rating": "got_it", "phase": "review", "at": iso(NOW - timedelta(hours=5)), "think_ms": 900, "session_id": "sm"},
                     {"rating": "got_it", "phase": "review", "at": iso(NOW - timedelta(hours=4)), "think_ms": 800, "session_id": "sm"}]},
        {"id": "m2", "position": 1, "question": "Mix Q2 — secured", "answer": "A2",
         "mine": "a2", "check": "match", "written_ms": 4000, "secured": True, "known": True, "shown": 2,
         "ratings": [{"rating": "got_it", "phase": "review", "at": iso(NOW - timedelta(hours=5)), "think_ms": 900, "session_id": "sm"},
                     {"rating": "got_it", "phase": "review", "at": iso(NOW - timedelta(hours=4)), "think_ms": 800, "session_id": "sm"}]},
        {"id": "m3", "position": 2, "question": "Mix Q3 — got it", "answer": "A3",
         "mine": "a3", "check": "match", "written_ms": 3500, "secured": False, "known": True, "shown": 1,
         "ratings": [{"rating": "got_it", "phase": "review", "at": iso(NOW - timedelta(hours=2)), "think_ms": 700, "session_id": "sm"}]},
        {"id": "m4", "position": 3, "question": "Mix Q4 — got it", "answer": "A4",
         "mine": "a4", "check": "match", "written_ms": 3500, "secured": False, "known": True, "shown": 1,
         "ratings": [{"rating": "got_it", "phase": "review", "at": iso(NOW - timedelta(hours=2)), "think_ms": 700, "session_id": "sm"}]},
        {"id": "m5", "position": 4, "question": "Mix Q5 — nearly", "answer": "A5",
         "mine": "a5", "check": "partial", "written_ms": 3000, "secured": False, "known": False, "shown": 1,
         "ratings": [{"rating": "nearly", "phase": "review", "at": iso(NOW - timedelta(hours=1)), "think_ms": 700, "session_id": "sm"}]},
        {"id": "m6", "position": 5, "question": "Mix Q6 — nearly", "answer": "A6",
         "mine": "a6", "check": "partial", "written_ms": 3000, "secured": False, "known": False, "shown": 1,
         "ratings": [{"rating": "nearly", "phase": "review", "at": iso(NOW - timedelta(hours=1)), "think_ms": 700, "session_id": "sm"}]},
        {"id": "m7", "position": 6, "question": "Mix Q7 — not yet", "answer": "A7",
         "mine": "a7", "check": "no", "written_ms": 3000, "secured": False, "known": False, "shown": 1,
         "ratings": [{"rating": "not_yet", "phase": "review", "at": iso(NOW - timedelta(minutes=50)), "think_ms": 700, "session_id": "sm"}]},
        {"id": "m8", "position": 7, "question": "Mix Q8 — not yet", "answer": "A8",
         "mine": "a8", "check": "no", "written_ms": 3000, "secured": False, "known": False, "shown": 1,
         "ratings": [{"rating": "not_yet", "phase": "review", "at": iso(NOW - timedelta(minutes=50)), "think_ms": 700, "session_id": "sm"}]},
        {"id": "m9", "position": 8, "question": "Mix Q9 — not seen", "answer": "A9",
         "mine": None, "check": None, "written_ms": None, "secured": False, "known": False, "ratings": []},
        {"id": "m10", "position": 9, "question": "Mix Q10 — not seen", "answer": "A10",
         "mine": None, "check": None, "written_ms": None, "secured": False, "known": False, "ratings": []},
    ],
    "sessions": [{"id": "sm", "started_at": iso(NOW - timedelta(hours=5)), "ended_at": iso(NOW - timedelta(minutes=50)),
                  "open": False, "active_ms": 60000, "cards_seen": 8, "cards_rated": 8, "cards_made": 8,
                  "median_think_ms": 800, "rushed": False}],
}

# Anyone else: nothing done yet.
DETAIL_NONE = {
    "pupil": {"id": "p-x", "first_name": "X", "last_name": "X", "display_name": "X"},
    "cards": [{"id": "c1", "position": 0, "question": "What is the formula of carbon dioxide?",
               "answer": "CO2", "mine": None, "check": None, "written_ms": None,
               "secured": False, "known": False, "ratings": []}],
    "sessions": [],
}

STUB_JS = r"""
(function () {
  var F = window.__FP__;
  F.calls = []; F.fetches = []; F.phase = 1;
  function Q(table) {
    var api = {
      select: function () { return api; }, order: function () { return api; },
      limit: function () { return api; }, eq: function () { return api; },
      is: function () { return api; }, in: function () { return api; },
      single: function () { api._one = true; return api; },
      maybeSingle: function () { api._one = true; return api; },
      then: function (res, rej) {
        var rows = (F.tables[table] || []).slice();
        /* `status` as real supabase-js returns it: the flashcards capability
           probe decides on the status, not on `error` (a HEAD 404 has none). */
        var out = api._one ? {data: rows[0] || null, error: rows.length ? null : {code: 'PGRST116'},
                              status: rows.length ? 200 : 406}
                           : {data: rows, error: null, status: 200};
        return Promise.resolve(out).then(res, rej);
      }
    };
    return api;
  }
  var user = {id: F.uid, aud: 'authenticated', role: 'authenticated',
              email: 'stub@drive.invalid', app_metadata: {}, user_metadata: {}};
  var client = {
    from: Q,
    rpc: function (name, args) {
      F.calls.push({name: name, args: args});
      if (name === 'flashcard_progress') {
        return Promise.resolve({data: F.phase === 2 ? F.progress2 : F.progress, error: null});
      }
      if (name === 'flashcard_pupil_detail') {
        return Promise.resolve({data: F.detail[args.p_pupil] || F.detail['*'], error: null});
      }
      if (name === 'flashcard_edit_assignment') {
        return Promise.resolve({data: {ok: true}, error: null});
      }
      return Promise.resolve({data: null, error: {message: 'unknown_rpc'}});
    },
    auth: {
      getUser: function () { return Promise.resolve({data: {user: user}, error: null}); },
      getSession: function () {
        return Promise.resolve({data: {session: {user: user, access_token: 'stub'}}, error: null});
      },
      signOut: function () { return Promise.resolve({error: null}); },
      onAuthStateChange: function () { return {data: {subscription: {unsubscribe: function () {}}}}; }
    }
  };
  var sdk = {createClient: function () { return client; }};
  Object.defineProperty(window, 'supabase', {
    configurable: true, get: function () { return sdk; }, set: function () {}
  });
  var realFetch = window.fetch;
  window.fetch = function (url, opts) {
    var u = String(url && url.url || url);
    if (/functions\/v1\//.test(u) || /onrender\.com/.test(u)) {
      F.fetches.push({url: u, method: opts && opts.method, body: opts && opts.body});
      return Promise.resolve(new Response('{"ok":true}', {status: 200,
        headers: {'Content-Type': 'application/json'}}));
    }
    return realFetch.apply(this, arguments);
  };
})();
"""


def stub(progress1, progress2, detail):
    fx = {"uid": TEACHER,
          "tables": {"profiles": [{"id": TEACHER, "role": "teacher", "first_name": "Tess",
                                   "last_name": "Teacher", "school_id": "s", "deleted_at": None}],
                     "staff_scopes": [],
                     # ⊕ Set from class (M), 27 Sep 2026 — formulae are drawn
                     # only on a Chemistry assignment; start() reads it here.
                     "assignments": [{"id": ASSIGN, "subject": {"name": "Chemistry"}}]},
          "progress": progress1, "progress2": progress2, "detail": detail}
    return "window.__FP__=%s;\n%s" % (json.dumps(fx), STUB_JS)


def wait_for(p, expr, timeout=8.0, step=0.1):
    end = time.time() + timeout
    while time.time() < end:
        try:
            if p.eval(expr):
                return True
        except cdp.JSError:
            pass
        time.sleep(step)
    return False


ORDER = "Array.prototype.map.call(document.querySelectorAll('#fp-table tbody tr.fp-row'),function(r){return r.getAttribute('data-pupil');})"

RANK = {"missing": 0, "not_started": 1, "in_progress": 2, "done_late": 3, "done": 4}


def value_of(p, key):
    if key == "pupil":
        return (p["last_name"] + " " + p["first_name"]).lower()
    if key == "status":
        return RANK[p["status"]]
    if key == "made":
        return p["made"]
    if key == "secured":
        return p["secured"]
    if key == "sittings":
        return p["sittings"]
    if key == "time":
        return p["active_ms"]
    if key == "answers":
        return p["answers"]["match"]
    if key == "last":
        return p["last_active"]
    raise KeyError(key)


def monotonic(vals, desc):
    present = [v for v in vals if v is not None]
    # nulls always sink, whichever way
    if vals[:len(present)] != present:
        return False
    for a, b in zip(present, present[1:]):
        if (b > a) if desc else (b < a):
            return False
    return True


# Visible text that is NOT data: labels, counts, buttons. Anything that reads
# like a sentence of explanation fails.
COPY_JS = r"""
(function(){
  var out = [];
  var roots = [document.getElementById('fp-main'), document.querySelector('[data-fb="overlay"]')];
  roots.forEach(function (root) {
    if (!root) return;
    var w = document.createTreeWalker(root, NodeFilter.SHOW_TEXT);
    var n;
    while ((n = w.nextNode())) {
      var t = n.nodeValue.replace(/\s+/g, ' ').trim();
      if (!t) continue;
      var e = n.parentElement;
      if (!e || e.closest('[data-fp-data],[data-fb-data],.fp-name,.bd-title,.bd-eyebrow,.bd-nav-word,.fp-title,.fp-crumb,.fb-ses-when')) continue;
      if (e.closest('[hidden]')) continue;
      var cs = getComputedStyle(e);
      if (cs.display === 'none' || cs.visibility === 'hidden') continue;
      out.push(t);
    }
  });
  return out;
})()
"""

FORBIDDEN = re.compile(r"(\bthis page\b|\bclick\b|\btap\b|\byou can\b|\bwill\b|\bhere\b|"
                       r"\bhow\b|\bshows?\b|\bwhen\b|\. [A-Z])", re.I)

PANEL_JS = r"""
(function(){
  var o=document.querySelector('[data-fb="overlay"]'), sh=o.querySelector('.bd-sheet');
  var r=sh.getBoundingClientRect(), sub=o.querySelector('.bd-subtitle');
  function t(q){var e=o.querySelector(q);return e?e.textContent:'';}
  return {
    shell: o.parentElement===document.body && getComputedStyle(o).position==='fixed' && !!sh,
    shellInfo: {parent:o.parentElement.tagName, pos:getComputedStyle(o).position},
    title:t('.bd-title'), eyebrow:t('.bd-eyebrow'), subtitle:sub.textContent,
    subVisible: !!sub.offsetParent, chip:t('.fb-status'),
    text: sh.innerText,
    tiles: Array.prototype.map.call(o.querySelectorAll('.bd-stat-label'),function(e){return e.textContent;}),
    tileVals: Array.prototype.map.call(o.querySelectorAll('.bd-stat-value'),function(e){return e.textContent;}),
    tileSubs: Array.prototype.map.call(o.querySelectorAll('.bd-stat'),function(e){var s=e.querySelector('.bd-stat-sub');return s?s.textContent:null;}),
    verdicts: t('[data-fb="verdicts"]'),
    filter: Array.prototype.map.call(o.querySelectorAll('.bd-toggle-btn'),function(e){return e.textContent;}),
    cards: Array.prototype.map.call(o.querySelectorAll('.fb-card'),function(c){
      var h=c.querySelector('details.fb-history');
      return {id:c.getAttribute('data-card'), states:c.querySelectorAll('.fb-state').length,
        state:(c.querySelector('.fb-state')||{}).textContent,
        hasAns:!!c.querySelector('.fb-ans'),
        answer:(c.querySelector('.fb-ans-text')||{}).textContent,
        none:!!(c.querySelector('.fb-ans')&&c.querySelector('.fb-ans').classList.contains('is-none')),
        verdict:(c.querySelector('.fb-verdict')||{}).textContent||null,
        model:(c.querySelector('.fb-model-text')||{}).textContent,
        // ⊕ design-port-fix, 30 Sep 2026 — scoped to `.fb-model` specifically.
        // Design port A (shared/flashcard-breakdown.js) gave the ANSWER
        // box's own header the SAME class, `.fb-model-label` ("Latest
        // answer"), to read as a symmetric pair with the model box's
        // header ("Model answer") — so a bare `.fb-model-label` query
        // returns whichever renders FIRST in DOM order (the answer box,
        // always, when both exist), never the model box this assertion is
        // actually about. Pre-existing on the merged port, found while
        // verifying this fix run; unrelated to any of the nine must-fixes.
        modelLabel:(c.querySelector('.fb-model .fb-model-label')||{}).innerText,
        tries:(c.querySelector('.fb-tries')||{}).textContent,
        hasHist:!!h, histOpen:!!(h&&h.open),
        theirLabel:/their answer/i.test(c.innerText)};}),
    sub: !!o.querySelector('.fb-card[data-card="c1"] .fb-model-text sub'),
    sittings: t('.fb-sittings > summary'), sitOpen: !!(o.querySelector('.fb-sittings')||{}).open,
    rect:{l:r.left,r:r.right,w:r.width,vw:window.innerWidth},
    centred: Math.abs((r.left) - (window.innerWidth - r.right)) < 4 && r.width < window.innerWidth,
    docOverflow: document.documentElement.style.overflow
  };
})()
"""

A11Y_JS = r"""
(function(){
  var small = [], tiny = [];
  document.querySelectorAll('#fp-main *, [data-fb="overlay"] *').forEach(function (e) {
    if (e.closest('[hidden]')) return;
    var cs = getComputedStyle(e);
    if (cs.display === 'none') return;
    var hasText = Array.prototype.some.call(e.childNodes, function (c) {
      return c.nodeType === 3 && c.nodeValue.trim(); });
    if (hasText && /DM Mono/.test(cs.fontFamily) && parseFloat(cs.fontSize) < 12) {
      small.push(e.className + ' ' + cs.fontSize);
    }
  });
  document.querySelectorAll('.fp-sort, .fp-name, .fp-actions .btn').forEach(function (b) {
    if (b.closest('[hidden]')) return;
    var r = b.getBoundingClientRect();
    if (r.width && r.height < 43.5) tiny.push((b.className || b.tagName) + ' ' + Math.round(r.height));
  });
  return {small: small, tiny: tiny};
})()
"""


def cellof_check(b, base, check):
    """teacher-live.js's `cellOf`, run for real: its `run()` is switched off
    and `buildPapers` / `buildMatrix` are called on a fixture pack."""
    src = open(os.path.join(HERE, "shared", "teacher-live.js"), encoding="utf-8").read()
    anchor = "  run().catch(function (err) {"
    if src.count(anchor) != 1:
        check(False, "cellOf: teacher-live.js's run() call found exactly once")
        return
    src = src.replace(anchor, "  (function () { return Promise.resolve(); })().catch(function (err) {")
    p = b.page("about:blank", settle=0.2)
    p.send("Page.addScriptToEvaluateOnNewDocument",
           {"source": "window.fetch=function(){return Promise.reject(new Error('offline'));};"})
    p.goto(base + "/teacher/flashcards.html?drive=cellof", settle=0.3)
    p.eval(src + "\n;true")
    probe = r"""
    (function (asFlash) {
      var L = window.MrBadmusTeacherLive;
      var pack = {
        members: [{student_id: 's1', first_name: 'A', last_name: 'One', joined_at: '2026-09-01T00:00:00+00:00'},
                  {student_id: 's2', first_name: 'B', last_name: 'Two', joined_at: '2026-09-01T00:00:00+00:00'},
                  {student_id: 's3', first_name: 'C', last_name: 'Three', joined_at: '2026-09-01T00:00:00+00:00'}],
        assignments: [
          {id: 'm1', title: 'Quiz', due_at: '2026-09-10T14:00:00+00:00', kind: 'mcq_set'},
          {id: 'f1', title: 'Deck', due_at: '2026-09-12T14:00:00+00:00', kind: asFlash ? 'flashcards' : 'mcq_set'}],
        submissions: [
          /* ⊕ Sharpen C5 — x1 revised a day after it was marked; x2's
             `updated_at` is 1 s after completion (the in-flight-answer race,
             inside the 2 s slack), so it is NOT revised. */
          {id: 'x1', assignment_id: 'm1', student_id: 's1', score: 4, max_score: 8, status: 'complete',
           completed_at: '2026-09-09T10:00:00+00:00', submitted_at: '2026-09-09T10:00:00+00:00', is_late: false,
           updated_at: '2026-09-10T09:00:00+00:00'},
          {id: 'x2', assignment_id: 'm1', student_id: 's2', score: 4, max_score: 8, status: 'complete',
           completed_at: '2026-09-09T11:00:00+00:00', submitted_at: '2026-09-09T11:00:00+00:00', is_late: false,
           updated_at: '2026-09-09T11:00:01+00:00'},
          {id: 'x3', assignment_id: 'f1', student_id: 's1', score: 10, max_score: 10, status: 'complete',
           completed_at: '2026-09-11T10:00:00+00:00', submitted_at: '2026-09-11T10:00:00+00:00', is_late: false},
          {id: 'x4', assignment_id: 'f1', student_id: 's2', score: 10, max_score: 10, status: 'complete',
           completed_at: '2026-09-13T10:00:00+00:00', submitted_at: '2026-09-13T10:00:00+00:00', is_late: true}],
        week: {start_at: '2026-09-07T00:00:00.000Z', end_at: '2026-09-14T00:00:00.000Z'},
        /* ⊕ MRB-351 landing (27 Sep 2026) — Source 2 of `lastIso`
           (the last-activity rule in supabase/MRB351-APPLY.md): a flashcard SITTING, not a completed cell.
           s1 has a real cell (x3, 09-11) but a LATER sitting (09-16) that
           never became a submission — the sitting must win. s3 has NO
           submission of any kind — the sitting is the only signal there is.
           s2 gets none, proving an absent entry changes nothing. */
        flashcardLastActive: { s1: '2026-09-16T08:00:00+00:00', s3: '2026-09-17T09:00:00+00:00' }
      };
      var now = Date.parse('2026-09-20T12:00:00Z');
      var papers = L.buildPapers(pack, now);
      var mx = L.buildMatrix(pack, papers, now);
      var roster = L.buildRoster(pack, mx, now);
      var byId = {};
      roster.forEach(function (r) { byId[r.id] = r; });
      var fi = papers.filter(function (p) { return p.id === 'f1'; })[0].idx;
      return {classMean: mx.classMean, s1: mx.studentAvg.s1, s2: mx.studentAvg.s2,
              flashMean: mx.colMean[fi], flashSub: mx.colSub[fi], flashLate: mx.colLate[fi],
              flashKind: papers[fi].kind, submitted: mx.rows.map(function (r) { return r.submitted[fi]; }),
              newest: L.newestMarkedIdx(papers), mcqIdx: papers.filter(function (p) { return p.id === 'm1'; })[0].idx,
              s1Last: byId.s1.lastIso, s1LastLabel: byId.s1.last,
              s2Last: byId.s2.lastIso,
              s3Last: byId.s3.lastIso, s3LastLabel: byId.s3.last,
              revisedMcq: (function () {
                var mi = papers.filter(function (p) { return p.id === 'm1'; })[0].idx;
                return mx.rows.map(function (r) { return !!(r.revised && r.revised[mi]); });
              })(),
              revisedNoStamp: L.isRevised({status: 'complete', completed_at: '2026-09-09T10:00:00+00:00'}),
              revisedInProgress: L.isRevised({status: 'in_progress', completed_at: null,
                                              updated_at: '2026-09-10T09:00:00+00:00'})};
    })(%s)
    """
    got = p.eval(probe % "true")
    ctl = p.eval(probe % "false")
    print("   cellOf probe:", json.dumps(got), " control:", json.dumps(ctl))
    check(got and got["classMean"] == 50, "cellOf: class mean 50 with one MCQ at 50% and one flashcard set at 100%",
          str(got and got["classMean"]))
    check(got and got["s1"] == 50 and got["s2"] == 50, "cellOf: every pupil average 50")
    check(got and got["flashMean"] is None, "cellOf: the flashcard column has no mean")
    # ⊕ MRB-351 landing (27 Sep 2026) — a THIRD member, `submitted[2]`, joined
    # this fixture for the roster/lastIso checks below (s3 has no submission
    # of any kind); `[True, True, False]` reflects that, not a change to
    # what "handed in" means.
    check(got and got["flashSub"] == 2 and got["submitted"] == [True, True, False],
          "cellOf: a finished flashcard set IS handed in (2 of 2)")
    check(got and got["flashLate"] == 1, "cellOf: lateness still counts on a flashcard set")
    check(got and got["newest"] == got["mcqIdx"], "newestMarkedIdx skips the flashcard set")
    check(ctl and ctl["classMean"] == 75, "cellOf control: the same pack as two MCQ sets reads 75",
          "proves the probe can see a difference")
    # ⊕ Sharpen C5 — "revised after marking": the backend's isRevised(),
    # run for real through buildMatrix — beyond the 2 s slack only.
    check(got and got["revisedMcq"] == [True, False, False],
          "buildMatrix: revised[] is true for a row changed after marking, false inside "
          "the 2 s slack and for a pupil with no row", got and str(got["revisedMcq"]))
    check(got and got["revisedNoStamp"] is False and got["revisedInProgress"] is False,
          "isRevised: no updated_at, or not complete, is never revised")
    # ⊕ MRB-351 landing (27 Sep 2026) — the last-activity rule in supabase/MRB351-APPLY.md, source 2.
    check(got and got["s1Last"] == "2026-09-16T08:00:00+00:00",
          "roster: a flashcard SITTING newer than a completed cell (either MCQ or deck) wins",
          got and got["s1Last"])
    check(got and got["s1LastLabel"] not in (None, "No activity yet"),
          "roster: that pupil's row reads a real relative time, not 'No activity yet'",
          got and got["s1LastLabel"])
    check(got and got["s2Last"] == "2026-09-13T10:00:00+00:00",
          "roster: a pupil with no flashcardLastActive entry is unaffected (cell-only, as before)",
          got and got["s2Last"])
    check(got and got["s3Last"] == "2026-09-17T09:00:00+00:00",
          "roster: a pupil with ONLY a deck sitting (no submission of any kind) shows that time",
          got and got["s3Last"])
    check(got and got["s3LastLabel"] not in (None, "No activity yet"),
          "roster: a sitting-only pupil reads a real relative time, not 'No activity yet'",
          got and got["s3LastLabel"])


def sharpen_matrix_check(b, base, check):
    """⊕ Sharpen B4/B5/B6 — teacher-live.js's real `buildPapers` /
    `buildMatrix` / `weekScoreLines` / `buildClassEntry`, on fixture packs,
    with `run()` switched off exactly as `cellof_check` does."""
    src = open(os.path.join(HERE, "shared", "teacher-live.js"), encoding="utf-8").read()
    anchor = "  run().catch(function (err) {"
    src = src.replace(anchor, "  (function () { return Promise.resolve(); })().catch(function (err) {")
    p = b.page("about:blank", settle=0.2)
    p.send("Page.addScriptToEvaluateOnNewDocument",
           {"source": "window.fetch=function(){return Promise.reject(new Error('offline'));};"})
    p.goto(base + "/teacher/flashcards.html?drive=sharpen", settle=0.3)
    p.eval(src + "\n;true")
    got = p.eval(r"""
    (function () {
      var L = window.MrBadmusTeacherLive;
      function mem(n) { var out = []; for (var i = 1; i <= n; i++) {
        out.push({student_id: 's' + i, first_name: 'P' + i, last_name: 'Pupil' + (i < 10 ? '0' + i : i),
                  joined_at: '2026-09-01T00:00:00+00:00'}); } return out; }
      function sub(aid, sid, score, max) { return {id: aid + sid, assignment_id: aid, student_id: sid,
        score: score, max_score: max, status: 'complete', completed_at: '2026-09-29T09:00:00+00:00',
        submitted_at: '2026-09-29T09:00:00+00:00', is_late: false}; }
      var now = Date.parse('2026-09-29T12:00:00Z');   // Tuesday
      var week = {start_at: '2026-09-27T23:00:00.000Z', end_at: '2026-10-04T23:00:00.000Z'};
      /* B4/B5 — one open MCQ, one open deck. */
      var pack = {
        members: mem(3), week: week, flashcardLastActive: {},
        assignments: [
          {id: 'm1', title: 'Quiz', release_at: '2026-09-28T06:00:00+00:00', due_at: '2026-10-05T08:00:00+00:00', kind: 'mcq_set'},
          {id: 'f1', title: 'Deck', release_at: '2026-09-28T06:00:00+00:00', due_at: '2026-10-05T08:00:00+00:00', kind: 'flashcards'}],
        submissions: [sub('m1', 's1', 7, 10), sub('m1', 's3', 4, 10), sub('f1', 's3', 10, 10)],
        flashcards: {f1: {n: 10, pupils: {
          s1: {status: 'in_progress', secured: 6, sittings: 3, made: 8},
          s2: {status: 'not_started', secured: 0, sittings: 0, made: 0},
          s3: {status: 'done', secured: 10, sittings: 2, made: 10}}}}
      };
      var papers = L.buildPapers(pack, now);
      var mx = L.buildMatrix(pack, papers, now);
      var fi = papers.filter(function (x) { return x.id === 'f1'; })[0].idx;
      var mi = papers.filter(function (x) { return x.id === 'm1'; })[0].idx;
      var idxs = [mi, fi].sort(function (a, b) { return a - b; });
      var r1 = mx.byId.s1, r2 = mx.byId.s2, r3 = mx.byId.s3;
      /* a pack whose deck read failed: no `flashcards` */
      var pack0 = JSON.parse(JSON.stringify(pack)); delete pack0.flashcards;
      var mx0 = L.buildMatrix(pack0, L.buildPapers(pack0, now), now);
      /* B6 — last week's set due Mon 09:00 (7 in), this week's open set (1 in). */
      var subs6 = [];
      for (var i = 1; i <= 7; i++) { subs6.push(sub('old', 's' + i, 5, 10)); }
      subs6.push(sub('new', 's9', 6, 10));
      var pack6 = {members: mem(17), week: week, flashcardLastActive: {}, flashcards: {},
        departed_count: 0,
        assignments: [
          {id: 'old', title: 'Changes of state', release_at: '2026-09-21T06:00:00+00:00', due_at: '2026-09-28T08:00:00+00:00', kind: 'mcq_set'},
          {id: 'new', title: 'Density', release_at: '2026-09-28T06:00:00+00:00', due_at: '2026-10-05T08:00:00+00:00', kind: 'mcq_set'}],
        submissions: subs6};
      var cls = {id: 'c6', name: '10h/Ph1', year_group: 10, key_stage: 'KS4'};
      var e6 = L.buildClassEntry(cls, pack6, [], null, now).entry;
      var pack7 = JSON.parse(JSON.stringify(pack6));
      pack7.assignments = pack7.assignments.slice(0, 1);
      pack7.submissions = pack7.submissions.filter(function (x) { return x.assignment_id === 'old'; });
      var e7 = L.buildClassEntry(cls, pack7, [], null, now).entry;
      /* nothing open, one set scheduled for Thursday 09:00 London */
      var pack9 = JSON.parse(JSON.stringify(pack7));
      pack9.assignments.push({id: 'sch', title: 'Next', release_at: '2026-10-01T08:00:00+00:00',
                              due_at: '2026-10-08T08:00:00+00:00', kind: 'mcq_set'});
      var e9 = L.buildClassEntry(cls, pack9, [], null, now).entry;
      /* the rolled-up path: a partial matrix, names from `roll.currentDone` */
      var roll = {papers: [{assignment_id: 'new', sub: 1, on_time: 1, late: 0, unknown: 0, marked_n: 1, mean: 60, off_roster: 0},
                           {assignment_id: 'old', sub: 7, on_time: 7, late: 0, unknown: 0, marked_n: 7, mean: 50, off_roster: 0}],
                  students: [], metrics: {}, currentDone: {s9: true}};
      var e8 = L.buildClassEntry(cls, pack6, [], null, now, roll).entry;
      return {
        fc1: [r1.fcStatus[fi], r1.fcSecured[fi], r1.fcN[fi], r1.fcSittings[fi]],
        fcMcq: [r1.fcStatus[mi], r1.fcSecured[mi]],
        started1: r1.startedInWeek, started2: r2.startedInWeek,
        sub3: r3.submitted[fi], sub1: r1.submitted[fi],
        noRead: [mx0.byId.s1.fcStatus[fi], mx0.byId.s1.startedInWeek],
        ws1: L.weekScoreLines(r1, idxs, papers), ws2: L.weekScoreLines(r2, idxs, papers),
        ws3: L.weekScoreLines(r3, idxs, papers), wsNone: L.weekScoreLines(r2, [], papers),
        cur: (L.currentSet(L.buildPapers(pack6, now)) || {}).id,
        card6: e6.cardWeek, chase6: (e6.cardChase || []).length, week6: e6.week,
        card7: e7.cardWeek, chase7: e7.cardChase, curId7: e7.currentSetId,
        card8: e8.cardWeek, chase8: (e8.cardChase || []).length,
        card9: e9.cardWeek, opens9: e9.cardOpens, opens7: e7.cardOpens
      };
    })()
    """)
    print("   sharpen probe:", json.dumps(got))
    check(got["fc1"] == ["in_progress", 6, 10, 3], "B4: a deck's per-pupil progress lands on the matrix row", str(got["fc1"]))
    check(got["fcMcq"] == [None, None], "B4: an MCQ paper carries no deck progress")
    check(got["started1"] is True and got["started2"] is False, "B4: a deck in progress counts as started this week")
    check(got["sub3"] is True and got["sub1"] is False, "B4: a deck is handed in only once complete (no fake row)")
    check(got["noRead"] == [None, False], "B4: a failed deck read leaves the row exactly as before")
    # papers newest-first: both released the same moment, so assert as a set of lines
    check(sorted(got["ws1"]) == sorted(["7/10", "6/10 secured"]), "B5: MCQ 7/10 and deck 6/10 secured", str(got["ws1"]))
    check(got["ws2"] == ["—", "—"], "B5: a not-started pupil reads a dash per paper", str(got["ws2"]))
    check(sorted(got["ws3"]) == sorted(["4/10", "10/10 secured"]), "B5: a finished deck reads its secured count, never a percent", str(got["ws3"]))
    check(got["wsNone"] == ["—"], "B5: no paper in the week reads one dash")
    check(got["cur"] == "new", "B6: the current set is the newest OPEN paper")
    check(got["card6"] == [1, 17], "B6: the card counts the current set (1 of 17), not last week's (7)", str(got["card6"]))
    check(got["chase6"] == 16, "B6: 16 names to chase on the current set", str(got["chase6"]))
    check(got["week6"][0] == 8, "B6: `week` (the charts' in-week count) is unchanged", str(got["week6"]))
    check(got["card7"] is None and got["curId7"] is None and got["opens7"] is None,
          "B6: nothing open and nothing scheduled → no card count (the card says no work open)")
    check(got["card9"] is None and got["opens9"] == "opens Thu 09:00",
          "B6: nothing open but a set scheduled → the card says when it opens", str(got["opens9"]))
    check(got["card8"] == [1, 17] and got["chase8"] == 16, "B6: the rolled-up path reads the same numbers and names",
          "%s %s" % (got["card8"], got["chase8"]))


def static_checks(check):
    """The generated screens carry the kind split (they are regenerated only
    by build_teacher_port.py; this reads what it wrote)."""
    def read(rel):
        return open(os.path.join(HERE, rel), encoding="utf-8").read()
    cd = read("teacher/class-detail.html")
    check("p.kind === 'flashcards' ? MRB_GO('flashcards', { assignment: p.id })" in cd,
          "class screen: a flashcard row opens the flashcards page")
    check("showDl: p.kind !== 'flashcards'" in cd, "class screen: no Download on a flashcard row")
    check("kind: p.kind, deckId: p.deck_id" in cd, "class screen: Edit carries the kind to MRBSetWork.edit")
    asg = read("teacher/assignment.html")
    check("showDl: pp.kind !== 'flashcards'" in asg, "marking screen: no Download on a flashcard set")
    sd = read("teacher/student-detail.html")
    check("stRow.submitted[i] === true ? '' : null" in sd, "student screen: an ungraded set reads handed in")
    # ⊕ 27 Sep 2026 (MRB-351 landing, merge with main) — RE-POINTED, NOT
    # WEAKENED. This used to check for the literal `stGraded`, MRB-351's own
    # local filter (`stMarked.filter(h => h.pct != null)`) over the average.
    # Main's Stream N (NF1, 25 Sep 2026) rewrote the SAME line first in
    # teacher_rulings.LOGIC's applied order, to `kMx.studentAvg[st.id]` — the
    # shared sum(score)/sum(max) average `buildMatrix` computes once in
    # shared/teacher-live.js, which is null-for-flashcards BY CONSTRUCTION
    # (`cellOf` never sets `score`/`max` on an ungraded cell, so it can never
    # enter the sum — see the `cellOf probe` above, `flashMean is None`).
    # `stGraded` no longer exists anywhere in the built page: re-adding it on
    # top of `kMx.studentAvg[st.id]` would be filtering a field with no
    # `.pct`. This checks the mechanism that actually ships instead.
    check("kMx.studentAvg[st.id]" in sd,
          "student screen: the average is over graded rows only (via kMx.studentAvg, "
          "not a local stGraded filter — see teacher_rulings.py's 27 Sep note)")
    check("flashcards:'flashcards.html'" in cd, "MRB_PAGE names flashcards.html")
    # ⊕ Sharpen B4-B6 — the rulings as the generated pages ship them.
    check("bdCan: isDeck ? fcSit > 0 : !!fbSub" in sd, "B4: Breakdown on a deck row from its first sitting")
    check('"e":"h.bdCan"' in sd.replace(" ", ""), "B4: the Breakdown control is gated on bdCan")
    check("window.MRBFlashcardBreakdown.open({ assignmentId: p.id," in sd, "B4: a deck row opens the flashcard panel")
    check("' secured' : '—')" in sd, "B4: a deck row's score is N/M secured")
    check("stRow.fcStatus[i] === 'in_progress'" in sd, "B4: a deck in progress reads In progress")
    check('/shared/flashcard-breakdown.js' in sd, "B4: the student screen loads the flashcard panel")
    check("weekScore: wIdxs.length ? MRB_WEEK_SCORE(kMx.byId[r.id], wIdxs, kPapers) : ''" in cd,
          "B5: the roster row carries weekScore (blank when nothing is in the week, C6 T13)")
    check('"data-mrb-cell":"week-score"' in cd.replace(" ", ""), "B5: the class screen draws the score cell")
    cl = read("teacher/classes.html")
    check("const cardW = ('cardWeek' in c) ? c.cardWeek : c.week;" in cl, "B6: the card reads the current set")
    tl = read("shared/teacher-live.js")
    check('window.location.replace(flashcardsUrl(fcHit.id))' in tl,
          "marking screen: a flashcard set redirects to its progress page")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--shots", default=os.path.join(cdp.gate_tmp(), "flashcard-progress"))
    args = ap.parse_args()
    os.makedirs(args.shots, exist_ok=True)

    fails = []

    def check(ok, what, detail=""):
        print("   %s  %s%s" % ("PASS" if ok else "FAIL", what, ("  - " + detail) if detail else ""))
        if not ok:
            fails.append(what)

    static_checks(check)

    server, port = cdp.serve(HERE)
    base = "http://127.0.0.1:%d" % port
    url = base + "/teacher/flashcards.html?assignment=" + ASSIGN
    try:
        with cdp.Browser() as b:
            # ── make mode, desktop ─────────────────────────────────────────
            p = b.page("about:blank", settle=0.2)
            p.send("Page.addScriptToEvaluateOnNewDocument",
                   {"source": stub(progress(), progress(phase=2),
                                   {"p-ben": DETAIL_BEN, "p-cat": DETAIL_CAT, "p-fay": DETAIL_MIX,
                                    "*": DETAIL_NONE})})
            p.set_viewport(1280, 800)
            p.goto(url, settle=0.5)
            ok = wait_for(p, "document.querySelectorAll('#fp-table tbody tr.fp-row').length===6")
            check(ok, "page renders six pupil rows")
            if not ok:
                print(p.eval("document.body.innerText.slice(0,500)"))
                raise SystemExit(1)
            p.eval("window.__fp_marker = 1; true")

            head = p.eval("document.getElementById('fp-head').innerText")
            check("Atomic structure" in head, "header: the title")
            bc = p.eval("(function(){var a=document.getElementById('fp-bar-crumb');"
                        "return a&&!a.hidden?{t:a.textContent,h:a.getAttribute('href')}:null;})()")
            check(bool(bc) and bc["t"] == "‹ 8r/Sc1" and "class-detail.html?class=" + CLASS in bc["h"],
                  "C6 T46: the bar carries the parent class, not an eyebrow", str(bc))
            check("8r/Sc1" not in head and "FLASHCARDS" not in head.upper().split("\n")[0:1],
                  "C6 T46: no class eyebrow above the title", head.replace("\n", " | "))
            check("Due Sat 3 Oct, 15:00" in head, "header: due in London time", head.replace("\n", " | "))
            # ⊕ Sharpen B1 — the chips under the title are gone.
            check(not any(x in head for x in ("Pupils write the answers", "Secure", "10 cards")),
                  "header: no mode / rule / card-count chips (B1)", head.replace("\n", " | "))
            check(head.count("Atomic structure") == 1, "header: the title once")
            check(p.eval("document.querySelectorAll('#fp-head .fp-chip, #fp-head .fp-chips').length") == 0,
                  "header: no chip nodes at all")
            check("Bring your planner" in head, "header: the teacher's note")
            check(p.eval("!!document.getElementById('fp-edit') && !!document.getElementById('fp-csv')"),
                  "header: Edit and Export CSV")
            strip = p.eval("document.getElementById('fp-strip').innerText")
            check("2/6" in strip and "33%" not in strip and "1.6" in strip,
                  "strip: done (one form, C6 T44) and average sittings",
                  strip.replace("\n", " | "))
            check("Name the particle with no charge" in strip, "strip: reteach list")
            check(p.eval("!!document.querySelector('#fp-reteach sub')"), "strip: formulae render with <sub>")

            p.screenshot(os.path.join(args.shots, "fp-desktop.png"), width=1280, height=800, full_page=True)
            fx = progress()["pupils"]
            order = p.eval(ORDER)
            check(order == ["p-fay", "p-dan", "p-cat", "p-ben", "p-eve", "p-ann"],
                  "default sort: least progress first", str(order))

            cols = p.eval("Array.prototype.map.call(document.querySelectorAll('#fp-table thead .fp-sort'),"
                          "function(b){return b.getAttribute('data-sort');})")
            # ⊕ Design port A, 30 Sep 2026 — Per card / Rushed are CUT, as
            # ruled and as drawn (Rushed rides in the Time cell now; see
            # the check on tr[data-pupil="p-cat"] .fp-rushed below, which
            # is unchanged because it never named a column).
            check(cols == ["pupil", "status", "made", "secured", "sittings", "time",
                           "last"], "make mode: every column, Made included, no Answers (B2), "
                  "no Per card/Rushed (design port A)", str(cols))
            byid = {x["pupil_id"]: x for x in fx}
            for key in cols:
                for want in ("ascending", "descending"):
                    p.eval("document.querySelector('.fp-sort[data-sort=\"%s\"]').click(); true" % key)
                    time.sleep(0.05)
                    aria = p.eval("document.querySelector('.fp-sort[data-sort=\"%s\"]').parentElement"
                                  ".getAttribute('aria-sort')" % key)
                    o = p.eval(ORDER)
                    vals = [value_of(byid[i], key) for i in o]
                    check(aria == want and monotonic(vals, want == "descending"),
                          "sort %s %s" % (key, want), "%s %s" % (aria, vals))

            # Rushed: an inline marker in Cat's row, never a block.
            r = p.eval("(function(){var e=document.querySelector('tr[data-pupil=\"p-cat\"] .fp-rushed');"
                       "if(!e)return null;var r=e.getBoundingClientRect();"
                       "return {t:e.textContent,h:r.height,d:getComputedStyle(e).display};})()")
            check(bool(r) and r["t"] == "Rushed" and r["h"] < 30 and r["d"] != "block",
                  "Rushed: a small inline marker", str(r))
            check(p.eval("document.querySelectorAll('tr.fp-row .fp-rushed').length") == 1,
                  "Rushed: only on the rushed pupil")
            hdrs = p.eval("Array.prototype.map.call(document.querySelectorAll('#fp-table thead th'),function(t){return t.textContent.trim();})")
            check(not any(h_.lower().startswith("answers") for h_ in hdrs), "B2: no Answers header in make mode", str(hdrs))
            check(p.eval("document.querySelector('tr[data-pupil=\"p-ben\"] .fp-sec').getAttribute('data-known')") == "7",
                  "Secured: known-once carried for the secure rule")

            # ⊕ Design port A five-state follow-up, 30 Sep 2026 — the
            # Secured strip's real per-card breakdown, via
            # flashcard_pupil_detail (reusing shared/flashcard-breakdown.js's
            # own cardState() — see stripCounts() in flashcard-progress.js).
            # Fay's row (DETAIL_MIX) carries exactly two of each state; wait
            # for her detail fetch (queued on first render — she has
            # sittings=1) to land and repaint before asserting.
            ok = wait_for(p, "document.querySelectorAll('tr[data-pupil=\"p-fay\"] .strip i').length===10")
            check(ok, "five-state strip: Fay's detail fetch landed and repainted")
            kinds = p.eval("Array.prototype.map.call(document.querySelectorAll("
                           "'tr[data-pupil=\"p-fay\"] .strip i'),function(e){return e.className;})")
            counts = {k: kinds.count(k) for k in ("k-sec", "k-got", "k-near", "k-no", "k-un")}
            check(counts == {"k-sec": 2, "k-got": 2, "k-near": 2, "k-no": 2, "k-un": 2},
                  "five-state strip: one row draws all five kinds of cell, two each", str(counts))
            check(kinds == ["k-sec"] * 2 + ["k-got"] * 2 + ["k-near"] * 2 + ["k-no"] * 2 + ["k-un"] * 2,
                  "five-state strip: cells sorted best to worst", str(kinds))
            aria = p.eval("document.querySelector('tr[data-pupil=\"p-fay\"] .strip').getAttribute('aria-label')")
            check(aria == "2 secured, 2 got it, 2 nearly, 2 not yet, 2 not seen",
                  "five-state strip: aria-label names all five counts", aria)

            # the answer-check edge function was fired, with the assignment id
            f = p.eval("window.__FP__.fetches")
            hit = [x for x in f if "flashcard-answer-check" in x["url"]]
            check(bool(hit) and hit[0]["method"] == "POST" and
                  json.loads(hit[0]["body"]) == {"assignment_id": ASSIGN},
                  "answer check: POSTed once on open with {assignment_id}", str(hit))
            pc = [c for c in p.eval("window.__FP__.calls") if c["name"] == "flashcard_progress"]
            check(bool(pc) and pc[0]["args"]["p_assignment"] == ASSIGN and
                  re.match(r"^\d{4}-\d\d-\d\dT", pc[0]["args"]["p_now"] or ""),
                  "progress rpc: p_assignment and an ISO p_now")


            # ⊕ Sharpen C1 — one baseline: fixed layout, a colgroup, one line per cell
            tl = p.eval("""(function(){var t=document.getElementById('fp-table');
              var cols=t.querySelectorAll('colgroup col').length, ths=t.querySelectorAll('thead th').length;
              var lefts=Array.prototype.map.call(t.querySelectorAll('thead th'),function(h){return Math.round(h.getBoundingClientRect().left);});
              var ok=true; t.querySelectorAll('tbody tr.fp-row').forEach(function(r){
                Array.prototype.forEach.call(r.children,function(c,i){if(Math.abs(Math.round(c.getBoundingClientRect().left)-lefts[i])>1)ok=false;});});
              var tall=Array.prototype.filter.call(t.querySelectorAll('tbody td'),function(c){return c.scrollWidth>c.clientWidth+1&&getComputedStyle(c).textOverflow!=='ellipsis';}).length;
              return {layout:getComputedStyle(t).tableLayout, cols:cols, ths:ths, aligned:ok, spill:tall};})()""")
            check(tl["layout"] == "fixed" and tl["cols"] == tl["ths"],
                  "C1: the table is table-layout: fixed with one <col> per column", str(tl))
            check(tl["aligned"] and tl["spill"] == 0, "C1: every cell sits under its header; nothing spills", str(tl))

            # ── the per-pupil panel (Sharpen B3) ───────────────────────────
            p.eval("document.querySelector('.fp-sort[data-sort=\"pupil\"]').click(); true")
            table_order = p.eval(ORDER)
            p.eval("document.querySelector('tr[data-pupil=\"p-ben\"]').click(); true")
            ok = wait_for(p, "document.querySelectorAll('[data-fb=\"overlay\"] .fb-card').length===3")
            check(ok, "panel: opens on a row with every card")
            d = p.eval(PANEL_JS)
            check(d["shell"], "panel: the centred breakdown shell ([data-fb=overlay] .bd-sheet, fixed on <body>)", str(d["shellInfo"]))
            check(d["title"] == "Ben Brown" and d["eyebrow"] == "Atomic structure", "panel: eyebrow = set title, title = pupil",
                  "%s / %s" % (d["eyebrow"], d["title"]))
            check(d["subtitle"] == "" and not d["subVisible"], "panel: subtitle empty and hidden (C2 rule)")
            check(not re.search(r"Pupil \d+ of \d+", d["text"]), "panel: no 'Pupil N of M'")
            check(d["chip"] == "In progress", "panel: one status chip in the title row", d["chip"])
            check(d["tiles"] == ["SECURED", "TIME", "HANDED IN"], "panel: three tiles", str(d["tiles"]))
            check(d["tileVals"][0] == "5 / 10" and d["tileSubs"][0] == "made 10 / 10",
                  "panel: SECURED 5 / 10, made 10 / 10 (make mode)", str(d["tileVals"]) + str(d["tileSubs"]))
            check(d["tileVals"][1] == "5:00" and d["tileSubs"][1] == "2 sittings",
                  "panel: TIME is summed active time, with the sittings count", str(d["tileVals"]) + str(d["tileSubs"]))
            # ⊕ 1 Oct 2026 (sweep fix C6, corrected) — HANDED IN reads "—"
            # for every status that is neither done nor done_late (TIME's
            # own convention, just above). The first fix made this tile
            # read "In progress" — the SAME word the status chip two lines
            # up already shows — which traded the original contradiction
            # (this tile said "Not yet" while the table pill said
            # "Missing" for the same row, SWEEP C6 on Aisha) for a
            # different defect: a label repeating what the chip already
            # says (REVIEW.md #6, the no-redundant-text rule). Old value
            # (before either fix) was "Not yet"; this fix's value was
            # "In progress"; now "—".
            check(d["tileVals"][2] == "—",
                  "panel: HANDED IN is '—' for an unfinished pupil (chip says why)",
                  d["tileVals"][2])
            check(d["verdicts"] == "5 right · 2 nearly · 2 wrong · 1 blank",
                  "panel: B2's verdict words under the tiles", d["verdicts"])
            check(d["filter"] == ["All 3", "Not secured 2"], "panel: All / Not secured filter", str(d["filter"]))
            cards = {c["id"]: c for c in d["cards"]}
            check(all(c["states"] == 1 for c in d["cards"]), "panel: exactly one state chip per card",
                  str([c["states"] for c in d["cards"]]))
            check(cards["c1"]["state"] == "Secured" and cards["c2"]["state"] == "Nearly"
                  and cards["c3"]["state"] == "Not seen", "panel: card state = Secured / latest rating / Not seen",
                  str([c["state"] for c in d["cards"]]))
            check(cards["c2"]["answer"] == "a neutron" and cards["c2"]["verdict"] == "Right",
                  "panel: latest written answer comes from a review rating when it carries one (MRB-352 key)",
                  str(cards["c2"]))
            check(cards["c1"]["answer"] == "CO2 gas" and cards["c1"]["verdict"] == "Right",
                  "panel: else the make-pass answer and its verdict", str(cards["c1"]))
            # ⊕ MRB-353 — Ben's c3 answer is pending but 23 hours old: no
            # check is in flight for it, so no chip (never a false Checking).
            check(cards["c3"]["answer"] == "positive" and cards["c3"]["verdict"] is None,
                  "panel: a pending answer over a minute old shows no chip (MRB-353)", str(cards["c3"]))
            check(cards["c2"]["model"] == "Neutron" and cards["c2"]["modelLabel"] == "MODEL ANSWER",
                  "panel: the model answer, one label", str(cards["c2"]))
            check(cards["c1"]["tries"] == "Tries: 4" and cards["c2"]["tries"] == "Tries: 3",
                  "panel: Tries = shown when present, else rated passes (degrade)",
                  "%s / %s" % (cards["c1"]["tries"], cards["c2"]["tries"]))
            check(all(not c["histOpen"] for c in d["cards"] if c["hasHist"]) and cards["c2"]["hasHist"],
                  "panel: History is closed by default")
            check("First try" not in d["text"] and "Later tries" not in d["text"],
                  "panel: no phase words visible while History is closed")
            check(not any(c["theirLabel"] for c in d["cards"]), "panel: no 'Their answer' caption beside a verdict chip")
            check(d["sub"], "panel: formulae render with <sub>")
            check(d["sittings"] == "History" and not d["sitOpen"],
                  "panel: one History disclosure (the sittings) under the cards, closed", d["sittings"])
            check(d["centred"], "panel: centred on desktop, not a right-hand drawer", str(d["rect"]))
            check(d["docOverflow"] == "hidden", "panel: the page behind does not scroll while open")
            p.eval("document.querySelector('[data-fb=\"overlay\"] .fb-card[data-card=\"c2\"] details.fb-history').open = true; true")
            rr = p.eval(r"""Array.prototype.map.call(document.querySelectorAll('[data-fb="overlay"] .fb-card[data-card="c2"] .fb-rates > *'),function(r){
                  return r.classList.contains('fb-phase') ? '['+r.textContent+']' : r.getAttribute('data-rating');})""")
            check(rr == ["[First try]", "not_yet", "[Later tries]", "not_yet", "nearly"],
                  "panel: History groups the ratings under First try / Later tries (MRB-353)", str(rr))
            tip = p.eval("(document.querySelector('[data-fb=\"overlay\"] .fb-card[data-card=\"c2\"] .fb-rate[data-phase=\"make\"]')||{}).title||''")
            check(tip.startswith("Not yet · First try · "), "panel: a rating's tooltip names the phase and the time", tip)
            p.eval("document.querySelector('[data-fb=\"overlay\"] .fb-sittings').open = true; true")
            check(p.eval("document.querySelectorAll('[data-fb=\"overlay\"] .fb-session').length") == 2 and
                  p.eval("document.querySelectorAll('[data-fb=\"overlay\"] .fb-session .fb-rushed').length") == 1,
                  "panel: the sittings timeline with a rushed marker")
            # the filter
            p.eval("document.querySelector('[data-fb=\"filter-open\"]').click(); true")
            check(p.eval("document.querySelectorAll('[data-fb=\"overlay\"] .fb-card').length") == 2,
                  "panel: Not secured hides the secured card")
            p.eval("document.querySelector('[data-fb=\"filter-all\"]').click(); true")
            p.screenshot(os.path.join(args.shots, "fb-panel-desktop.png"), width=1280, height=800, full_page=False)
            # prev / next walk the table's order
            names = []
            nxt = "document.querySelector('[data-fb=\"next\"]')"
            prv = "document.querySelector('[data-fb=\"prev\"]')"
            check(p.eval(prv + ".querySelector('.bd-nav-word').textContent") == "Ann Able" and
                  p.eval(nxt + ".querySelector('.bd-nav-word').textContent") == "Cat Cole",
                  "panel: prev / next carry the neighbours' names")
            p.eval(nxt + ".click(); true")
            wait_for(p, "document.querySelector('[data-fb=\"overlay\"]').getAttribute('data-fb-student')==='p-cat' && !!document.querySelector('[data-fb=\"overlay\"] .fb-card')")
            dc = p.eval(PANEL_JS)
            check(dc["title"] == "Cat Cole", "panel: next goes to the next row in table order")
            # ⊕ MRB-353 — Cat's 2 pending answers are from 70 minutes ago:
            # nothing is checking them now, so the line does not say so.
            check(dc["verdicts"] == "2 right · 1 nearly · 1 wrong",
                  "panel: Cat's verdict words (an old pending answer is not 'checking')", dc["verdicts"])
            cc = {c["id"]: c for c in dc["cards"]}
            check(cc["c1"]["answer"] == "C O 2" and cc["c1"]["verdict"] == "Nearly" and cc["c1"]["tries"] == "Tries: 2",
                  "panel degrade (old function): make answer, Nearly, Tries = rated passes", str(cc["c1"]))
            check(cc["c2"]["answer"] == "No written answer" and cc["c2"]["none"] and cc["c2"]["tries"] == "Tries: 0",
                  "panel degrade: no written answer reads 'No written answer'", str(cc["c2"]))
            check(dc["tileSubs"][1] == "1 sitting · rushed", "panel: a rushed pupil's time line says so", dc["tileSubs"][1])
            check(cc["c3"]["answer"] == "" and cc["c3"]["verdict"] == "Blank" and cc["c3"]["tries"] == "Tries: 1",
                  "panel: a blank make answer keeps its Blank verdict, and Tries is never 0 beside an answer",
                  str(cc["c3"]))
            walked = [p.eval("document.querySelector('[data-fb=\"overlay\"]').getAttribute('data-fb-student')")]
            for _ in range(8):
                if p.eval(nxt + ".disabled"):
                    break
                p.eval(nxt + ".click(); true"); time.sleep(0.05)
                walked.append(p.eval("document.querySelector('[data-fb=\"overlay\"]').getAttribute('data-fb-student')"))
            check(walked == table_order[2:] and p.eval(nxt + ".disabled"),
                  "panel: next walks the table order and disables at the end", "%s vs %s" % (walked, table_order))
            for _ in range(8):
                if p.eval(prv + ".disabled"):
                    break
                p.eval(prv + ".click(); true"); time.sleep(0.05)
            check(p.eval("document.querySelector('[data-fb=\"overlay\"]').getAttribute('data-fb-student')") == table_order[0]
                  and p.eval(prv + ".disabled"), "panel: prev disables at the first row")
            wait_for(p, "!!document.querySelector('[data-fb=\"overlay\"] .fb-card')")
            check("hasn't started" not in p.eval("document.querySelector('[data-fb=\"overlay\"] .bd-body').innerText"),
                  "panel: Ann (done) is not described as not started")
            # the poll must not repaint an open panel
            opens = p.eval("document.querySelector('[data-fb=\"overlay\"]').getAttribute('data-fb-opens')")
            p.eval("window.__fb_mark = document.querySelector('[data-fb=\"overlay\"] .bd-title'); true")
            p.eval("window.MRBFlashcardProgress.refresh(); true")
            time.sleep(0.6)
            check(p.eval("window.__fb_mark === document.querySelector('[data-fb=\"overlay\"] .bd-title') && "
                         "document.querySelector('[data-fb=\"overlay\"]').getAttribute('data-fb-opens')==='%s' && "
                         "!document.querySelector('[data-fb=\"overlay\"]').hidden" % opens),
                  "panel: a poll does not repaint or close the open panel")
            copy_drawer = p.eval(COPY_JS)
            a11y_drawer = p.eval(A11Y_JS)
            p.eval("document.dispatchEvent(new KeyboardEvent('keydown',{key:'Escape',bubbles:true})); true")
            check(p.eval("document.querySelector('[data-fb=\"overlay\"]').hidden"), "panel: Escape closes it")
            check(p.eval("document.documentElement.style.overflow") in ("", "visible"), "panel: page scroll restored on close")

            # ── CSV ────────────────────────────────────────────────────────
            p.eval("document.querySelector('.fp-sort[data-sort=\"pupil\"]').click(); true")  # pupil desc
            p.eval("document.getElementById('fp-csv').click(); true")
            csv = p.eval("window.__MRB_FP_LAST_CSV__")
            lines = csv["text"].lstrip("﻿").strip().split("\r\n") if csv else []
            check(bool(csv) and csv["text"].startswith("﻿"), "CSV: UTF-8 BOM")
            check(bool(csv) and csv["name"] == "8r-Sc1-Atomic-structure.csv", "CSV: filename from class + title",
                  csv and csv["name"])
            # ⊕ Design port A — Per card/Rushed dropped from the CSV header
            # too (COLUMNS is the one source for both the table and the
            # export); Rushed's fact rides inside the Time cell's own text.
            check(lines and lines[0] == "Pupil,Status,Made,Secured,Known once,Sittings,Time,Last active",
                  "CSV: the displayed columns", lines and lines[0])
            check(len(lines) == 7, "CSV: one row per pupil")
            disp = p.eval("Array.prototype.map.call(document.querySelectorAll('#fp-table tbody tr.fp-row .fp-name'),"
                          "function(b){return b.textContent;})")
            check([l.split(",")[0] for l in lines[1:]] == disp, "CSV: in the order displayed", str(disp))
            cat = [l for l in lines if l.startswith("Cat Cole")]
            check(bool(cat) and cat[0].startswith("Cat Cole,In progress,6/10,2/10,3/10,1,2:05 (rushed),")
                  and "pending" not in cat[0] and re.search(r",20\d\d-(0[1-9]|1[0-2])-\d\d \d\d:\d\d$", cat[0]),
                  "CSV: a row's values, Rushed folded into the Time cell", cat and cat[0])

            # ── polling flips a row to Done without a reload ───────────────
            p.eval("window.__FP__.phase = 2; true")
            t0 = time.time()
            ok = wait_for(p, "document.querySelector('tr[data-pupil=\"p-cat\"]').getAttribute('data-status')==='done'",
                          timeout=13.0, step=0.25)
            check(ok, "live: Cat flips to Done by polling", "%.1fs" % (time.time() - t0))
            check(p.eval("window.__fp_marker === 1"), "live: no reload")
            check("3/6" in p.eval("document.getElementById('fp-strip').innerText"), "live: the strip recounts")

            # copy + a11y on the main page
            copy = p.eval(COPY_JS) + copy_drawer
            bad = sorted(set(t for t in copy if len(t) > 48 or FORBIDDEN.search(t)))
            check(not bad, "no explanatory copy", str(bad))
            a = p.eval(A11Y_JS)
            check(not a["small"] and not a11y_drawer["small"], "no mono label under 12px",
                  str(a["small"] + a11y_drawer["small"]))
            check(not a["tiny"], "tap targets >= 44px", str(a["tiny"]))
            errs = [e for e in p.console_errors() if "favicon" not in e and "supabase" not in e.lower()]
            check(not errs, "no console errors", str(errs[:3]))

            # ── Edit ───────────────────────────────────────────────────────
            p.eval("document.getElementById('fp-edit').click(); true")
            ed = p.eval("({open:!document.getElementById('fp-edit-back').hidden,"
                        "d:document.getElementById('fp-ed-due-date').value,"
                        "t:document.getElementById('fp-ed-due-time').value,"
                        "rel:document.getElementById('fp-ed-rel-wrap').hidden})")
            check(ed["open"] and ed["d"] == "2026-10-03" and ed["t"] == "15:00" and ed["rel"],
                  "Edit: opens on the London due time; release locked once released", str(ed))
            p.eval("document.getElementById('fp-ed-title').value='Atoms';"
                   "document.getElementById('fp-ed-due-time').value='16:30';"
                   "document.getElementById('fp-ed-save').click(); true")
            wait_for(p, "document.getElementById('fp-edit-back').hidden")
            ec = [c for c in p.eval("window.__FP__.calls") if c["name"] == "flashcard_edit_assignment"]
            check(bool(ec) and ec[0]["args"] == {"p_id": ASSIGN, "p_title": "Atoms",
                                                 "p_due_at": "2026-10-03T15:30:00.000Z",
                                                 "p_note": "Bring your planner", "p_release_at": None},
                  "Edit: rpc flashcard_edit_assignment with the UTC instant", str(ec and ec[0]["args"]))

            # ── phones: 360 and 390 ────────────────────────────────────────
            for w in (360, 390):
                p.set_viewport(w, 844, settle=0.3)
                m = p.eval("({page: document.documentElement.scrollWidth - document.documentElement.clientWidth,"
                           "box: (function(){var s=document.getElementById('fp-scroll');"
                           "return s.scrollWidth - s.clientWidth;})(),"
                           "sticky: getComputedStyle(document.querySelector('tbody .fp-col-pupil')).position,"
                           "hidden: Array.prototype.map.call(document.querySelectorAll('#fp-table thead th'),"
                           "function(t){return getComputedStyle(t).display;})})")
                check(m["page"] <= 1, "%dpx: no horizontal page scroll" % w, str(m))
                # ⊕ Design port A, 30 Sep 2026 — ruled: "Phone: Pupil (with a
                # status chip under the name) and Secured only, nothing
                # ellipsised." Every other column hides below 640px, and the
                # table's own min-width floor lifts with it, so the two that
                # remain fit the box exactly — no INTERNAL scroll either now,
                # which used to be the point of this check (five more
                # columns lived off-screen to the right). The real thing
                # being proved is now the column count, not a scrollbar.
                check(m["box"] <= 1, "%dpx: the table needs no scroll either — only Pupil/Secured remain" % w, str(m))
                check(m["hidden"].count("none") == 5 and m["hidden"][0] != "none",
                      "%dpx: Status/Made/Sittings/Time/Last active hidden, Pupil/Secured shown" % w, str(m["hidden"]))
                check(m["sticky"] == "sticky", "%dpx: the pupil column is sticky" % w)
                if w == 390:
                    p.screenshot(os.path.join(args.shots, "fp-phone-390.png"), width=390, height=844, full_page=True)
                    p.eval("document.getElementById('fp-scroll').scrollLeft = 400; true")
                    time.sleep(0.2)
                    left = p.eval("(function(){var a=document.querySelector('tbody .fp-col-pupil').getBoundingClientRect();"
                                  "var s=document.getElementById('fp-scroll').getBoundingClientRect();"
                                  "return Math.abs(a.left-s.left)<2;})()")
                    check(left, "390px: pupil column stays put while the table scrolls")
                    p.eval("document.getElementById('fp-scroll').scrollLeft = 0; true")
                    p.eval("document.querySelector('tr[data-pupil=\"p-ben\"]').click(); true")
                    wait_for(p, "document.querySelectorAll('[data-fb=\"overlay\"] .fb-card').length===3")
                    full = p.eval("(function(){var r=document.querySelector('[data-fb=\"overlay\"] .bd-sheet').getBoundingClientRect();"
                                  "return r.left<=1 && r.width>=window.innerWidth-1;})()")
                    check(full, "390px: the panel is a full-screen sheet")
                    ov = p.eval("(function(){var s=document.querySelector('[data-fb=\"overlay\"] .bd-sheet');"
                                "return Math.max(document.documentElement.scrollWidth - document.documentElement.clientWidth,"
                                " s.scrollWidth - s.clientWidth);})()")
                    check(ov <= 1, "390px: no sideways scroll with the panel open", str(ov))
                    tap = p.eval("(function(){return Array.prototype.map.call(document.querySelectorAll("
                                 "'[data-fb=\"overlay\"] .bd-close, [data-fb=\"overlay\"] .bd-nav-btn'),"
                                 "function(b){return Math.round(b.getBoundingClientRect().height);});})()")
                    check(all(x >= 44 for x in tap), "390px: close / prev / next are 44px targets", str(tap))
                    p.screenshot(os.path.join(args.shots, "fb-panel-390.png"), width=390, height=844, full_page=False)
                    p.eval("document.querySelector('[data-fb=\"close\"]').click(); true")

            # ── review mode ───────────────────────────────────────────────
            p2 = b.page("about:blank", settle=0.2)
            rv = progress(mode="review", rule="quick")
            p2.send("Page.addScriptToEvaluateOnNewDocument",
                    {"source": stub(rv, rv, {"p-ben": DETAIL_REVIEW, "p-cat": DETAIL_FRESH, "*": DETAIL_NONE})})
            p2.set_viewport(1280, 800)
            p2.goto(url, settle=0.5)
            wait_for(p2, "document.querySelectorAll('#fp-table tbody tr.fp-row').length===6")
            cols2 = p2.eval("Array.prototype.map.call(document.querySelectorAll('#fp-table thead .fp-sort'),"
                            "function(b){return b.getAttribute('data-sort');})")
            # ⊕ Design port A — 6, not 8: Per card/Rushed cut (see the make
            # mode check above for the same change).
            check("made" not in cols2 and "answers" not in cols2 and len(cols2) == 6,
                  "review mode: no Made, no Answers, no Per card/Rushed", str(cols2))
            h2 = p2.eval("document.getElementById('fp-head').innerText")
            check(not any(x in h2 for x in ("Ready-made cards", "Quick", "10 cards")), "review mode: no chips (B1)")
            hdr2 = p2.eval("Array.prototype.map.call(document.querySelectorAll('#fp-table thead th'),function(t){return t.textContent.trim();})")
            check(not any(h_.lower().startswith("answers") for h_ in hdr2), "B2: no Answers header in review mode")
            check(p2.eval("document.querySelector('tr[data-pupil=\"p-ben\"] .fp-sec').getAttribute('data-known')") is None,
                  "review/quick: no known-once layer")
            p2.eval("document.querySelector('tr[data-pupil=\"p-ben\"]').click(); true")
            wait_for(p2, "document.querySelectorAll('[data-fb=\"overlay\"] .fb-card').length===3")
            r2 = p2.eval(PANEL_JS)
            check(r2["verdicts"] == "" and r2["tileSubs"][0] is None,
                  "review mode panel: no verdict line, no 'made' line", str(r2["tileSubs"]))
            check(len([c for c in r2["cards"] if c["model"]]) == 3, "review mode panel: every card has its model answer")
            rc = {c["id"]: c for c in r2["cards"]}
            check(rc["c1"]["hasAns"] is False and rc["c2"]["hasAns"] is False,
                  "review mode, old function: a RATED card with no answer in the payload draws no answer box "
                  "(never a false 'No written answer')", str([rc["c1"], rc["c2"]]))
            check(rc["c3"]["answer"] == "No written answer",
                  "review mode: only the untouched card says 'No written answer'", str(rc["c3"]))
            check(rc["c1"]["tries"] == "Tries: 2" and rc["c2"]["tries"] == "Tries: 1",
                  "review mode, old function: Tries = rated passes")
            p2.eval("document.querySelector('[data-fb=\"overlay\"] .fb-card[data-card=\"c1\"] details.fb-history').open = true; true")
            rr2 = p2.eval(r"""Array.prototype.map.call(document.querySelectorAll('[data-fb="overlay"] .fb-card[data-card="c1"] .fb-rates > *'),function(r){
                  return r.classList.contains('fb-phase') ? '['+r.textContent+']' : r.getAttribute('data-rating');})""")
            tip2 = p2.eval("(document.querySelector('[data-fb=\"overlay\"] .fb-card[data-card=\"c1\"] .fb-rate')||{}).title||''")
            check(rr2 == ["got_it", "got_it"] and "try" not in tip2.lower() and "tries" not in tip2.lower(),
                  "ready-made deck: History shows only the ratings, no First try / Later tries label (MRB-353)",
                  "%s / %s" % (rr2, tip2))
            p2.eval("document.querySelector('[data-fb=\"close\"]').click(); true")
            # ⊕ MRB-353 — Checking only while a check is in flight.
            p2.eval("document.querySelector('tr[data-pupil=\"p-cat\"]').click(); true")
            wait_for(p2, "document.querySelector('[data-fb=\"overlay\"]').getAttribute('data-fb-student')==='p-cat' && document.querySelectorAll('[data-fb=\"overlay\"] .fb-card').length===3")
            fc = {c["id"]: c for c in p2.eval(PANEL_JS)["cards"]}
            check(fc["f1"]["answer"] == "coulombs I think" and fc["f1"]["verdict"] == "Checking",
                  "MRB-353: a typed review answer checked 20 s ago and still pending reads Checking", str(fc["f1"]))
            check(fc["f2"]["answer"] == "volts maybe" and fc["f2"]["verdict"] is None,
                  "MRB-353: a pending review answer 3 minutes old shows no chip", str(fc["f2"]))
            check(fc["f3"]["answer"] == "ohms" and fc["f3"]["verdict"] == "Right",
                  "MRB-353: a decided review answer shows its verdict", str(fc["f3"]))
            p2.eval("document.querySelector('[data-fb=\"close\"]').click(); true")
            p2.eval("document.getElementById('fp-csv').click(); true")
            csv2 = p2.eval("window.__MRB_FP_LAST_CSV__")
            check(csv2["text"].lstrip("﻿").split("\r\n")[0] ==
                  "Pupil,Status,Secured,Sittings,Time,Last active",
                  "review CSV: the displayed columns (design port A: no Per card/Rushed)")
            p2.screenshot(os.path.join(args.shots, "fp-review-desktop.png"), width=1280, height=800, full_page=True)

            # ── not found ─────────────────────────────────────────────────
            p3 = b.page("about:blank", settle=0.2)
            p3.send("Page.addScriptToEvaluateOnNewDocument", {"source": stub(None, None, {})
                     .replace("return Promise.resolve({data: F.phase === 2 ? F.progress2 : F.progress, error: null});",
                              "return Promise.resolve({data: null, error: {message: 'not_found'}});")})
            p3.goto(url, settle=0.8)
            wait_for(p3, "!document.getElementById('fp-notice').hidden")
            check(p3.eval("document.getElementById('fp-notice-title').textContent") == "Flashcard set not found",
                  "not found: a short label")

            # ── cellOf ────────────────────────────────────────────────────
            cellof_check(b, base, check)
            sharpen_matrix_check(b, base, check)
    finally:
        server.shutdown()

    print("\n   screenshots: %s" % args.shots)
    if fails:
        print("\n❌ flashcard_progress_drive: %d failure(s)" % len(fails))
        for f_ in fails:
            print("   · " + f_)
        return 1
    print("\n✅ flashcard_progress_drive: all checks passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
