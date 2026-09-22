#!/usr/bin/env python3
"""
mrb348_teacher_equiv.py — the SIX GENERATED TEACHER SCREENS render the same
page after round three's aggregate as before it.

    MRB_TEST_TEACHER_PASSWORD=… python3 mrb348_teacher_equiv.py --capture old
    MRB_TEST_TEACHER_PASSWORD=… python3 mrb348_teacher_equiv.py --capture new
    python3 mrb348_teacher_equiv.py --compare

WHY IT EXISTS

MRB-348 round three takes the six generated teacher screens off an unbounded
`assignment_submissions` pull and puts the summing in the database instead.
Nothing about that change is supposed to be visible. But WHICH VALUE REACHES
THE DOM is a property of Design's compiled template, node by node — a mean
computed one row short, a roster flag that stops being set, a per-paper column
that silently comes back empty are all changes to an expression inside a node,
not to the shape of the page. The only way to establish that nothing a teacher
SEES has moved is to look at what actually renders, on both trees, and diff it.

WHY THE EXISTING TEACHER GATES CANNOT DO THIS

`teacher_behaviour` and `teacher_reach` drive `teacher_fixtures/*-fixture.html`.
Those fixtures have NO NETWORK and never load `shared/teacher-live.js` at all —
their data is baked in by the generator. They are not merely likely to miss this
change; they are structurally incapable of seeing it, and their own `watches`
lists in `gate_registry.py` say so by naming the fixture generator and not the
live data layer. A gate that passes without looking is not evidence. This is the
same lesson CLAUDE.md already records about `student_parity` not watching the
ported student page.

So this signs in as REAL teachers on TEST, loads the REAL pages out of
`mrbadmus_site/`, and compares the rendered text, the control set and the
address — the same bar `teacher_behaviour` holds the fixtures to, applied to
the surface that actually changed.

THE TWO READERS

  A. mide.badmus@test-rainford.local — the realistic Rainford teacher: five
     classes, 28 assignments, 79 submissions. He is the reader the defect is
     about; a page that sums nothing sums his rows.
  B. hz_rich@test.mrbadmus — Rich Spedding, `staff_scopes.scope = 'hod'` for
     Science at the same school. He sees every Science class in the school and
     only his own department's work, so his two screens exercise the RLS
     asymmetry THROUGH THE RENDER rather than through a query count. An
     aggregate that widened or narrowed what a HoD may sum shows up here and
     nowhere else in this file.

THE IDS ARE RESOLVED ONCE AND HARD-CODED, ON PURPOSE

Every id below was read out of TEST with the service-role key, with the project
proven from the key's own JWT `ref` claim (CLAUDE.md item 8) and production's
ref refused. They are frozen into `CASES` rather than re-resolved per run
because a case list that re-resolves can silently compare two different worlds:
"the busiest class" and "a student with submissions" are both queries whose
answer can move between the old capture and the new one, and the diff would
then be a true report about two different pages.

⊕ DEVIATION FROM THE BRIEF, and it makes the check stronger, not weaker.

The brief asked for a second digest snapshot taken by PRESSING a scope chip on
`digest.html`. There is no such control. The digest's scope is decided by the
ADDRESS and by nothing else — `digestScope: MRB_Q('class') ? 'class' : 'all'`
in the state initialiser (see `teacher_rulings.py`, the `goDigest`/`goReport`
entries: "No `class` parameter IS `digestScope: 'all'` … so a reload cannot
lose it"). The in-product route to the class report is `goReport` on the class
screen, which is a NAVIGATION to `digest?class=<id>`. So the second view is its
own case, still keyed `digest-class`, reached the way the product reaches it.
Driving it by URL is also more deterministic than a click: the two captures are
guaranteed to be looking at the same scope rather than at whatever a chip
happened to be toggled to.

⚠️ READINESS IS QUIESCENCE, NOT PRESENCE — AND THAT IS NOT A TIDY-UP.

The obvious probe, and the one this file started with, asks whether the mount
host has content yet. On these screens that question is answered long before
the page is finished, and the gap is not small: `assignment.html?paper=1` was
caught being snapshotted in THREE different states from one URL on one tree —
during the first paint, before `load()` had resolved the class's paper list, so
it drew a different paper entirely; after the papers resolved but before the
lazy per-paper GRID read landed, at 317 characters; and finished, at 742. Two
`--capture old` runs against an UNCHANGED tree disagreed on that case and on
`student`.

So the snapshot the comparison will use is taken repeatedly and must come back
IDENTICAL `STABLE_SAMPLES` times running before it counts, and failing to go
quiet is recorded as an error rather than snapshotted anyway. A half-drawn page
that happens to match another half-drawn page is not evidence of anything. See
`_settle` below.

⚠️ PRECONDITION: NOTHING ELSE MAY BE DRIVING TEST WHILE THIS RUNS.

This is not boilerplate caution — it was caught happening. Three consecutive
`--capture old` runs against an UNCHANGED tree disagreed, and the cause was an
assignment titled `mrb336muczfmg5 FOREIGN TITLE` appearing on 10A and then
vanishing again: a throwaway-world row from another gate's fixture, created and
torn down by a drive running against the same TEST project at the same time. It
had already been deleted by the time the database was asked about it.

It is worth being precise about the damage, because it is not merely noise. The
foreign row carries no `due_at`, and `buildPapers` sorts due_at DESC **nulls
first** — so while it existed it took index 0 and shifted every paper down one.
`?paper=1` then rendered "Atomic Structure and the Periodic Table" instead of
"Acids and Alkalis quiz (Wk 22)": the right address, a stable page, the wrong
paper, and a 425-character difference that would have read as a regression in
the marking screen.

Two defences are built in below. `require` pins each case to the target it
NAMES and reloads until it is there, so no case can quietly compare two
different papers or two different classes. And it is only a defence, not a
cure: a foreign row still moves the counts on `student` and `digest-class`
while it exists. Run the two captures with the estate quiet.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import ssl
import sys
import time
import urllib.request

REPO = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, REPO)
os.chdir(REPO)

import ks3_browser as cdp  # noqa: E402

TEST_REF = "qeppkiswvclkkwbxmlok"
URL = "https://%s.supabase.co" % TEST_REF
CTX = ssl.create_default_context(cafile="/etc/ssl/cert.pem")
# Not 5537 — that is `mrb348_student_equiv.py`'s port, and the two harnesses
# are run back to back on the same machine.
PORT = 5538
# ⊕ The tree to serve. `mrbadmus_site` unless a caller names another.
#
# ⚠️ IT IS **NOT** HOW THE `fallback` CAPTURE WAS TAKEN, and the difference is
# the whole worth of that capture. The fallback — the page's behaviour when
# `public.teacher_class_rollup` is missing, which is production between the
# frontend push and the migration — was produced by RENAMING THE FUNCTION OUT
# OF TEST'S CATALOGUE for the length of one drive, then renaming it back and
# verifying the restoration from `pg_proc`. Simulating it by editing the
# page's own copy of `loadClassSummaries` would have proved only that a
# hand-written `throw` is caught; it would not have proved that PostgREST's
# real answer to a missing function reaches the catch at all.
SERVE_DIR = os.environ.get("MRB348_SERVE_DIR") or "mrbadmus_site"
OUT = os.environ.get("MRB_SHOTS") or os.path.expanduser("~/tmp/ks3-gates")

TEACHER_A = "mide.badmus@test-rainford.local"     # 5 classes / 28 / 79
TEACHER_B = "hz_rich@test.mrbadmus"               # HoD Science, same school

# ── the ids, resolved once out of TEST (read-only) ─────────────────────────
# 10A — the BUSIEST of reader A's five classes by a distance: 18 assignments
# and 47 submissions against 10Z Physics' 4/17, 8X1's 5/15, 8X2's 1/0 and
# 9Y1's 0/0. Six students on the roster.
BUSIEST = "2a000000-0000-0000-0000-000000000002"
# Hannah Patel, a member of 10A and the most-submitted student on it (17 of
# the class's 47 submissions). A student with NO submissions would render the
# empty arm of every panel, which is the one shape an aggregate cannot get
# wrong by summing short.
STUDENT = "29000000-0000-0000-0000-000000000006"
# `?paper=` is an INDEX into the class's own paper list, built newest-first by
# `buildPapers` (due_at DESC, nulls first).
#
# ⚠️ ON THIS SEED NO SINGLE PAPER EXERCISES BOTH HALVES OF THE SCREEN, so there
# are two marking cases rather than one. Checked against TEST: of 10A's
# eighteen assignments, the twelve-plus with submissions carry ZERO
# `assignment_questions` rows, and the one that carries fifteen of them has
# zero submissions. So:
#
#   · PAPER_MARKED (1) — "Acids and Alkalis quiz (Wk 22)", due 28 May 2026 and
#     long closed, three of six students in. This is the case that exercises
#     the SUBMISSION AGGREGATE — submitted 3/6, class mean 80%, the on-time
#     split — which is the half round three actually changes. Its question
#     breakdown is legitimately empty, and that is the data, not a failed read.
#   · PAPER_GRID (0) — "Atomic Structure and the Periodic Table", still open,
#     nothing in, but the only paper with a real question list. It draws the
#     fifteen-question breakdown and the full six-student grid, so the
#     per-question and per-student shapes are covered too, in their empty arm.
#
# Index 1 is also chosen deliberately from OUTSIDE the block of twelve
# assignments that share one due instant: inside that block the order is
# settled by a title tiebreak, and an index that depends on a tiebreak is an
# index that can point at a different paper on a different day.
PAPER_MARKED = 1
PAPER_GRID = 0
# ⚠️ With NO `?class=`, `load()` falls back to `c.CLASSES[0]` — the class list
# sorted by code with `localeCompare(..., {numeric: true})`, so 8X1 < 9Y1 <
# 10A < 10Z Physics and the fallback lands on **8X1**
# (2a000000-0000-0000-0000-000000000001), NOT on the busiest class. That is the
# whole point of case 6: the fallback reads a different class's rows through
# the same aggregate, and it is a path with no parameter to check it against.

# ⚠️ WHAT `require` MAY AND MAY NOT NAME, and the line is the whole point of it.
#
# It names the case's TARGET — which class, which student, which paper — and
# never a value round three could legitimately move. A class code, a person's
# name and a paper's title are IDENTITY: if they change, the case is no longer
# about the thing it says it is about, and comparing it would be comparing two
# different pages. A mean, a submitted count, an "on time" percentage or a
# roster flag are OUTPUT: requiring one of those would be writing the answer
# into the question, and a regression that changed it would show up as a
# retry-until-timeout rather than as the difference it is.
CASES = [
    # ── reader A: the realistic teacher ────────────────────────────────────
    dict(key="classes", who=TEACHER_A, page="classes.html", q="",
         expect_search="", require="10Z Physics",
         note="the class list — five classes, every one summed"),
    dict(key="digest", who=TEACHER_A, page="digest.html", q="",
         expect_search="", require="Weekly digest",
         note="the whole-school weekly digest, scope 'all'"),
    dict(key="digest-class", who=TEACHER_A, page="digest.html",
         q="?class=" + BUSIEST,
         expect_search="?class=" + BUSIEST, require="10A report",
         note="the SINGLE-CLASS report (10A) — `digestScope: 'class'`, whose "
              "rows read per-paper columns straight off the matrix. The most "
              "likely place for a difference to show"),
    dict(key="insights", who=TEACHER_A, page="insights.html", q="",
         expect_search="", require="Question difficulty",
         note="the charts screen — several papers in one round trip"),
    dict(key="class", who=TEACHER_A, page="class-detail.html",
         q="?class=" + BUSIEST,
         expect_search="?class=" + BUSIEST, require="Seating plan",
         note="10A, the busiest class, named in the address"),
    dict(key="class-fallback", who=TEACHER_A, page="class-detail.html", q="",
         expect_search="", require="8X1",
         note="NO `?class=` — the page falls back to the first class by code "
              "order (8X1), and `require` is what proves it did. A path round "
              "three has to get right, and one no parameter can be checked "
              "against"),
    dict(key="student", who=TEACHER_A, page="student-detail.html",
         q="?class=" + BUSIEST + "&student=" + STUDENT,
         expect_search="?class=" + BUSIEST + "&student=" + STUDENT,
         require="Hannah Patel",
         note="Hannah Patel of 10A — 17 submissions, the richest history on "
              "the seed"),
    dict(key="marking", who=TEACHER_A, page="assignment.html",
         q="?class=" + BUSIEST + "&paper=" + str(PAPER_MARKED),
         expect_search="?class=" + BUSIEST + "&paper=" + str(PAPER_MARKED),
         # ⚠️ THE TITLE, NOT THE INDEX. `?paper=` is a position in a list the
         # database can reorder under us — see the PRECONDITION note above,
         # where a foreign row with a null `due_at` took index 0 and made this
         # case render the wrong paper for 425 characters.
         require="Acids and Alkalis quiz (Wk 22)",
         note="the marking screen for a CLOSED, marked paper of 10A — the "
              "submission aggregate (3/6 in, mean 80%, the on-time split)"),
    dict(key="marking-grid", who=TEACHER_A, page="assignment.html",
         q="?class=" + BUSIEST + "&paper=" + str(PAPER_GRID),
         expect_search="?class=" + BUSIEST + "&paper=" + str(PAPER_GRID),
         require="Atomic Structure and the Periodic Table",
         note="the marking screen for the ONE 10A paper that has a question "
              "list — the fifteen-question breakdown and the full "
              "six-student grid, in their nothing-submitted-yet arm"),

    # ── reader B: the HoD ──────────────────────────────────────────────────
    dict(key="hod-classes", who=TEACHER_B, page="classes.html", q="",
         expect_search="", require="HZ 10B Physics",
         note="HoD Science — his own class list and his own department's "
              "work, through a standing that is not an ordinary teacher's"),
    dict(key="hod-digest", who=TEACHER_B, page="digest.html", q="",
         expect_search="", require="HZ 10B Physics",
         note="the same digest through the HoD's RLS standing"),
]


def anon_key():
    """⚠️ THE **TEST** ANON KEY. `config.js` carries both projects' keys and
    production's comes first, so a naive first-match read signs a TEST fixture
    into PRODUCTION and gets a 401 that reads as a bad password. Slice from
    `const TEST`, exactly as the rest of the estate's drives do."""
    src = open("shared/config.js", encoding="utf-8").read()
    return re.search(r"'(eyJ[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+)'",
                     src[src.index("const TEST"):]).group(1)


def sign_in(email, key, pw):
    req = urllib.request.Request(
        URL + "/auth/v1/token?grant_type=password",
        data=json.dumps({"email": email, "password": pw}).encode(),
        headers={"apikey": key, "Content-Type": "application/json"},
        method="POST")
    return json.load(urllib.request.urlopen(req, timeout=30, context=CTX))


def put_session(page, base, sess):
    """The teacher pages open with `requireTeacherRole`, which reads the stored
    session out of localStorage and BOUNCES TO /auth.html when there isn't one.
    So the session has to be written against the same origin before the page
    that will use it is loaded — land on a `/teacher/...` URL first (the bounce
    is harmless; it stays on this origin), write the token, then navigate to
    the page being measured. Same move the student harness makes."""
    payload = json.dumps({
        "access_token": sess["access_token"],
        "refresh_token": sess.get("refresh_token", ""),
        "expires_at": int(time.time()) + int(sess.get("expires_in", 3600)),
        "expires_in": int(sess.get("expires_in", 3600)),
        "token_type": "bearer", "user": sess["user"],
    })
    page.goto(base + "/teacher/classes.html", settle=0.2)
    page.eval("localStorage.setItem(%s, %s)"
              % (json.dumps("sb-%s-auth-token" % TEST_REF), json.dumps(payload)))


# `#mrb-teacher` is the mount host every one of the six screens draws into.
# ⚠️ Do NOT reach for `[data-port-region]` first the way the student probe
# does: on these pages the FIRST such region is the sticky topbar, which is
# mounted and full of text ("MrBadmusAI", "Find a student", "Sign out") long
# before any of the screen's own rows exist — a probe anchored on it would
# report READY on a page with no data at all.
READY = """(function(){
    var h = document.querySelector('#mrb-teacher');
    if (!h) { return false; }
    if (document.querySelector('.skeleton, [data-skeleton]')) { return false; }
    var regions = h.querySelectorAll('[data-port-region]');
    var body = null;
    for (var i = 0; i < regions.length; i++) {
        if (regions[i].getAttribute('data-port-region') !== 'topbar') {
            body = regions[i];
            break;
        }
    }
    if (!body) { return false; }
    return ((body.innerText || body.textContent || '').trim().length > 80);
})()"""

# Visible text and the control set — the same two things `teacher_behaviour`
# compares on the fixtures, so a difference here is the same kind of difference
# it would have caught had it been able to see the live data layer.
SNAP = """(function(){
    var h = document.querySelector('#mrb-teacher') || document.body;
    var txt = (h.innerText || h.textContent || '')
              .replace(/\\s+/g, ' ').trim();
    var ctl = [];
    var nodes = h.querySelectorAll(
        'button, a, input, select, textarea, [role=button], [tabindex]');
    for (var i = 0; i < nodes.length; i++) {
        var n = nodes[i];
        ctl.push((n.tagName || '') + '|' +
                 ((n.innerText || n.value || n.getAttribute('aria-label') || '')
                   .replace(/\\s+/g,' ').trim().slice(0, 60)));
    }
    return { text: txt, controls: ctl, nodes: h.querySelectorAll('*').length,
             url: window.location.search };
})()"""


STABLE_SAMPLES = 8        # consecutive identical snapshots …
STABLE_GAP = 0.5          # … 500ms apart, so four full seconds of no change
TARGET_TRIES = 4          # reloads allowed before a case is called a failure


def _settle(page, deadline_s):
    """
    ⚠️ MOUNTED IS NOT FINISHED, AND ON THESE SCREENS THE GAP IS HUGE.

    A first probe that only asked "is the mount host non-empty" was measured
    capturing THREE different pages from one URL on one tree:

      · `assignment.html?paper=1` snapshotted during the first paint, before
        `load()` had resolved the class's paper list — so it rendered paper 0
        ("Atomic Structure and the Periodic Table", still open, nothing
        submitted) under an address that says `paper=1`;
      · the same URL snapshotted after the papers resolved but before the
        lazy per-paper GRID read landed — the right paper, 317 characters,
        "No question-by-question marks for this paper yet";
      · and the finished screen — the right paper, 742 characters, the full
        fifteen-question grid, 494 nodes.

    Two `--capture old` runs against an UNCHANGED tree disagreed on that case
    and on `student` as well. A harness that unstable cannot say anything
    about round three: every real difference would be buried in noise, and any
    noise could be read as a real difference.

    So readiness is QUIESCENCE, not presence: once the mount has content, take
    the very snapshot the comparison will use and require it to come back
    IDENTICAL `STABLE_SAMPLES` times running. Failing to reach quiescence is
    reported as an error rather than snapshotted anyway — a half-drawn page
    that matches another half-drawn page is not evidence of anything.
    """
    end = time.time() + deadline_s
    while time.time() < end:
        try:
            if page.eval(READY, timeout=5) is True:
                break
        except Exception:
            pass
        time.sleep(0.08)
    else:
        return None

    last, runs = None, 0
    while time.time() < end:
        try:
            s = page.eval(SNAP, timeout=15)
        except Exception:
            s = None
        if s is not None and s == last:
            runs += 1
            if runs >= STABLE_SAMPLES:
                return s
        else:
            runs, last = 0, s
        time.sleep(STABLE_GAP)
    return None


def capture(tag, pw):
    """
    ⚠️ A DISCARDED WARM-UP LOAD PER CASE, AND IT IS NOT OPTIONAL.

    Kept verbatim from `mrb348_student_equiv.py`, and on the teacher side there
    are TWO reasons for it rather than one:

      1. A COLD CONNECTION. The first read of the run pays a cold Supabase TLS
         handshake and, on any screen that touches the backend, a Render cold
         start. That is latency, not content — but a read that times out under
         `withDeadline` renders the EMPTY arm of a panel, and an empty arm on
         one side and a filled one on the other is a difference that reads
         exactly like a regression in the aggregate.

      2. LAZY AUTO-COMPOSITION. The week's assignment is composed on first
         read, not by a cron. Whichever side of the comparison runs FIRST can
         therefore CREATE a row the other side then also sees — an extra
         assignment in the digest's count, an extra column in the matrix, an
         extra row on the class screen. The student harness watched exactly
         this happen and it looked spectacular and was entirely the harness.

    One discarded load per case first, then the measured one. Both sides then
    observe the same composed, warm world.
    """
    key = anon_key()
    server, port = cdp.serve(SERVE_DIR, PORT)
    base = "http://127.0.0.1:%d" % port
    snaps, who = {}, None
    try:
        with cdp.Browser() as b:
            page = b.attach()
            for c in CASES:
                if c["who"] != who:
                    put_session(page, base, sign_in(c["who"], key, pw))
                    who = c["who"]
                url = base + "/teacher/" + c["page"] + c["q"]

                # The discarded warm-up. See the note above: it is what makes
                # the two captures describe the same world.
                page.goto(url, settle=0.3)
                _settle(page, 60)

                # …then the measured load, reloaded until the page is quiet AND
                # is showing the target this case names. A page that has gone
                # still on the WRONG paper is stable and useless; only a fresh
                # navigation can move it, so the retry is a `goto`, not more
                # waiting.
                s, why = None, "never settled"
                for attempt in range(TARGET_TRIES):
                    page.goto(url, settle=0.3)
                    cand = _settle(page, 60)
                    if cand is None:
                        continue
                    if c["require"] in cand["text"]:
                        s = cand
                        break
                    why = "settled on the wrong target (wanted %r)" % c["require"]
                if s is None:
                    snaps[c["key"]] = {"error": why}
                    print("  ❌ %-15s %s" % (c["key"], why))
                    continue
                snaps[c["key"]] = s
                print("  ✅ %-15s %6d chars, %3d controls, %4d nodes, url=%r"
                      % (c["key"], len(s["text"]), len(s["controls"]),
                         s["nodes"], s["url"]))
    finally:
        try:
            server.shutdown()
        except Exception:
            pass
    os.makedirs(OUT, exist_ok=True)
    path = os.path.join(OUT, "mrb348_teacher_%s.json" % tag)
    with open(path, "w") as fh:
        json.dump(snaps, fh, indent=2)
    print("  wrote %s" % path)
    return snaps


def compare(against="new"):
    fails = []
    a = json.load(open(os.path.join(OUT, "mrb348_teacher_old.json")))
    b = json.load(open(os.path.join(OUT, "mrb348_teacher_%s.json" % against)))
    print("\n  comparing OLD (before MRB-348 round three) with %s\n"
          % against.upper())
    for c in CASES:
        k = c["key"]
        oldc, newc = a.get(k, {}), b.get(k, {})
        print("  %s — %s" % (k, c["note"]))
        if oldc.get("error") or newc.get("error"):
            fails.append("%s: %s / %s" % (k, oldc.get("error"), newc.get("error")))
            print("     ❌ %s / %s" % (oldc.get("error"), newc.get("error")))
            continue
        same_text = oldc.get("text") == newc.get("text")
        same_ctl = oldc.get("controls") == newc.get("controls")
        print("     %s visible text   (%d vs %d chars)"
              % ("✅" if same_text else "❌",
                 len(oldc.get("text", "")), len(newc.get("text", ""))))
        print("     %s control set    (%d vs %d)"
              % ("✅" if same_ctl else "❌",
                 len(oldc.get("controls", [])), len(newc.get("controls", []))))
        if not same_text:
            fails.append(k + ": visible text differs")
            ot, nt = oldc.get("text", ""), newc.get("text", "")
            for i in range(min(len(ot), len(nt))):
                if ot[i] != nt[i]:
                    print("        first difference at char %d:" % i)
                    print("        old …%s…" % ot[max(0, i-60):i+60])
                    print("        new …%s…" % nt[max(0, i-60):i+60])
                    break
            else:
                print("        one is a prefix of the other")
        if not same_ctl:
            fails.append(k + ": control set differs")
            so, sn = set(oldc.get("controls", [])), set(newc.get("controls", []))
            for x in sorted(so - sn)[:6]:
                print("        only OLD: %s" % x)
            for x in sorted(sn - so)[:6]:
                print("        only NEW: %s" % x)

        # The address, asserted on its own rather than folded into the text
        # comparison — a page that rewrote its own URL (dropping a `?class=`,
        # normalising a `?paper=`) would be invisible in innerText, and the
        # digest reads its SCOPE off exactly that string.
        want = c["expect_search"]
        got_old, got_new = oldc.get("url", ""), newc.get("url", "")
        ok = (got_old == want and got_new == want)
        print("     %s address        old=%r new=%r (expected %r)"
              % ("✅" if ok else "❌", got_old, got_new, want))
        if not ok:
            fails.append(k + ": address differs from the expected search")
        print()

    if fails:
        print("  ❌ %d difference(s):" % len(fails))
        for f in fails:
            print("     · %s" % f)
        return 1
    print("  ✅ every case renders the same visible text, the same controls, "
          "and the same address.")
    return 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--capture", choices=["old", "new", "fallback"])
    ap.add_argument("--compare", action="store_true")
    ap.add_argument("--against", default="new", choices=["new", "fallback"],
                    help="which capture to hold OLD against (default: new)")
    a = ap.parse_args()
    if a.capture:
        pw = os.environ.get("MRB_TEST_TEACHER_PASSWORD")
        if not pw:
            raise SystemExit("$MRB_TEST_TEACHER_PASSWORD is not set.")
        print("capturing %s" % a.capture.upper())
        capture(a.capture, pw)
        return 0
    if a.compare:
        return compare(a.against)
    ap.print_help()
    return 2


if __name__ == "__main__":
    sys.exit(main())
