#!/usr/bin/env python3
"""teacher_admin_foreign_class_drive.py — MRB-325 ruling 5, both sides of it,
and MRB-326: the class that has NO teacher at all, and the toolset once
inside.

    python3 teacher_admin_foreign_class_drive.py
    python3 teacher_admin_foreign_class_drive.py --shots DIR

Ruling 5 lets a school_admin open a class they do not personally teach.
`teacher-live.js`'s `mergeForeignClass` does it, and the class header then
LEADS with "Acting as admin" (`teacher_rulings.py`, `klass.meta`). This drives
that, and — in the same run — drives a PLAIN TEACHER at the same class id and
demands the refusal.

⚑ WHY BOTH HALVES ARE IN ONE FILE.

The admin half on its own is not evidence. "The page opened" is what a
permissive page does too, and the change under test is precisely a widening of
who may open something. So the negative control is not a nicety here: it is the
half that says the door is a door. Same page, same fixture, same class id, one
field different — a `staff_scopes` row — and opposite outcomes.

⚑ HOW THE PERSONAS ARE DRIVEN, AND WHAT THAT DOES AND DOES NOT PROVE.

The real pages run: `teacher/class-detail.html` as built, the real guard, the
real `teacher-data.js`, the real `teacher-live.js`, the real rulings. Only the
Supabase CLIENT is stubbed — `admin_view_drive.py`'s mechanism, imported from
that file rather than copied so the two cannot drift — and the stub serves
fixture rows shaped exactly as PostgREST would return them.

⚠️ THE STUB MODELS RLS'S ROW VISIBILITY; IT DOES NOT PROVE RLS. That is the
  whole design of the two personas and it must be read honestly:

    admin (Ada, `staff_scopes.scope = 'school_admin'`)
        sees the school's `class_teachers` / `class_members` / `assignments`
        rows — what `class_teachers_admin_read` and its siblings grant.
    plain teacher (Amy, no scope row)
        sees only rows whose `teacher_id` is hers, and the members and
        assignments of the classes those rows name — what
        `class_teachers_own_all` grants.

  `teacher_world()` below builds the second by filtering the first. Whether
  the DATABASE really draws that line is a question for SQL under real roles,
  and it is answered there (MRB-303's report, and the policies themselves).
  What THIS proves is the half no SQL can: given those two row sets, the page
  opens for one and refuses the other, and says which it is doing.

  That split is not a shortcut taken for convenience. `hz_admin` and the rest
  of the admin-scoped fixtures have NO PASSWORD on the TEST project
  (`auth.users.encrypted_password IS NULL`, verified under MRB-303, not
  assumed) and a STANDING MRB-303 RULING BANS SETTING ONE, because those
  fixtures are what a security proof rests on and writing to them would spend
  the proof to make a drive convenient. This ticket does not override that
  ruling and does not try to.

⚠️ WHY `mergeForeignClass` CANNOT BE PERMISSIVE BY ACCIDENT, and why the
  negative control is testing something real: the security check in that
  function is `loadClassMatrices` ITSELF, not a role field read in JavaScript.
  It carries no client-side self-filter, so a non-empty pack IS the proof of
  the role. The plain-teacher persona's row set makes that read come back
  empty, `yearOfClass` throws `not_authorised`, and `run()`'s catch draws
  SAY.notMine. Nothing about the two runs differs except the rows.

⊕ MRB-326, 6 Sep 2026 — TWO THINGS THIS FILE COULD NOT SEE, AND BOTH SHIPPED.

  1. IT ONLY EVER DROVE A CLASS SOMEBODY ELSE TEACHES. `loadClassMatrices`
     drove off `class_teachers`, so what it really asked was "is there a live
     teacher link here I am allowed to see" — and on production 25 of the 69
     classes in 2026-27 have no live link AT ALL, their only teacher being an
     unclaimed `pending_staff` row. Those 25 refused an admin outright. The
     fixture that would have caught it already existed and was never pointed
     at: `admin_view_drive.C_NONE`, the class NOBODY teaches. Section B drives
     it, and drives a variant with the roster emptied too, because "no links,
     no members, no work" is three empty things at once and the page has to
     survive all three.

  2. IT PROVED "OPENS" AND NOTHING ELSE — so "opens but cannot act" shipped.
     Every write control on a class screen was refused by RLS for an admin,
     because no write policy on the estate had an admin arm. Section C is one
     fixture per capability: the control is PRESENT on the foreign class, and
     firing it produces the same write or navigation the owning teacher's
     press produces. Which of them the migration unblocks is written on each.

⚠️ WHAT SECTION C DOES AND DOES NOT PROVE. The stub records writes; it does
  not adjudicate them (see its own note in `admin_view_drive.STUB_JS`). So a
  green Section C says the control is on screen and fires the right write with
  the right arguments — the half no SQL can reach. Whether the DATABASE
  accepts that write is the other half, and it is proved separately, under
  real RLS with a real JWT, by `teacher_admin_real_drive.py`. Reading either
  half as the whole is how "opens but cannot act" got through the first time.

⛔ SCREENSHOTS GO OUTSIDE THE REPO by default (`/tmp`) — MRB-301's rule: a gate
  must not write into the tree it is attesting is clean.
"""

import argparse
import copy
import json
import os
import sys

REPO = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, REPO)
os.chdir(REPO)

import ks3_browser as cdp
# The stub mechanism, and the fixture SHAPES, from the file that established
# both. Imported rather than re-typed: a second copy of a PostgREST-shaped
# builder is a second thing to keep true.
import admin_view_drive as av

PORT = 5510

SCHOOL = av.SCHOOL
YEAR = av.YEAR
ADMIN = av.ADMIN          # Ada Nwosu — school_admin scope
AMY = av.AMY              # a plain teacher, no scope row
RICH = av.RICH            # hod, and the teacher of the class under test

C_OWN_ADMIN = av.C_DUP    # 8r/Sc1 — Ada's own class, so `base()` has a list
C_OWN_AMY = av.C_CO       # 10h/Sc1 — Amy's own class, same reason
C_FOREIGN = av.C_RICH     # 10h/Ph1 — RICH's class. Foreign to BOTH personas.

# ⊕ MRB-326 — 9r/Sc4, the class NOBODY teaches. Foreign to both personas in a
# second, harder way: there is no `class_teachers` row for it belonging to
# ANYONE, so the driver query comes back empty no matter who asks. This is the
# production shape — 25 of 69 classes this year — and the case the old code
# refused with the sentence meant for somebody else's class.
C_UNSTAFFED = av.C_NONE

# The refusal, taken from the source of truth rather than retyped: if
# SAY.notMine is ever reworded, this file must follow it or say so.
REFUSAL = "That class is not one of yours."

# The roster of the foreign class. Four active students and one who left, so
# "real rows, not an empty state" is a claim with something behind it — and so
# a departed student can be shown NOT to be on it.
ROSTER = [
    ("ee000000-0000-0000-0000-000000001201", "Priya", "Raman"),
    ("ee000000-0000-0000-0000-000000001202", "Callum", "Frost"),
    ("ee000000-0000-0000-0000-000000001203", "Nadia", "Okafor"),
    ("ee000000-0000-0000-0000-000000001204", "Joel", "Attah"),
]
DEPARTED = ("ee000000-0000-0000-0000-000000001205", "Ex", "Student")

PAPER = "ee000000-0000-0000-0000-000000003001"


def tables():
    """The whole school's rows — i.e. what an admin's RLS read returns."""
    t = copy.deepcopy(av.TABLES)

    # A roster worth asserting on, on the foreign class.
    t["class_members"] = [m for m in t["class_members"]
                          if m["class_id"] != C_FOREIGN]
    for sid, first, last in ROSTER:
        t["class_members"].append(av.member(C_FOREIGN, sid, first, last))
    t["class_members"].append(
        av.member(C_FOREIGN, DEPARTED[0], DEPARTED[1], DEPARTED[2],
                  left=av.PAST))

    # One assignment, so the class is in Design's "live" state rather than the
    # no-work one — the state a teacher opening someone else's class is
    # looking at real work in.
    t["assignments"] = [{
        "id": PAPER, "class_id": C_FOREIGN, "title": "Week 1 · Forces",
        "due_at": av.NOW, "created_at": av.PAST, "academic_week": 1,
        "subject_id": av.SUBJ_PH, "deleted_at": None,
        "subject": {"id": av.SUBJ_PH, "name": "Physics"},
    }]
    t["assignment_submissions"] = [{
        "id": "ee000000-0000-0000-0000-000000004001",
        "assignment_id": PAPER, "student_id": ROSTER[0][0],
        "score": 7, "max_score": 10, "total_time_seconds": 420,
        "submitted_at": av.NOW, "completed_at": av.NOW, "status": "complete",
        "is_late": False, "attempts": 1, "attempt_no": 1, "deleted_at": None,
    }]

    # Nothing in either fixture needs a timetable; the class screen's
    # "lesson today" read (ruling 6) is allowed to come back empty and drop
    # its segment, which is what `klass.meta`'s .filter(Boolean) is for.
    t["timetable_entries"] = []
    t["school_period_times"] = []
    return t


def teacher_world(uid, t):
    """The same rows, narrowed to what a PLAIN teacher's RLS read returns.

    `class_teachers_self_read` shows a teacher their own link rows and nothing
    else; the members and assignments policies hang off the classes those rows
    name. So: keep this teacher's links, keep only the classes they reach
    through them, and drop everything else. Narrowing the ADMIN world rather
    than writing a second fixture is deliberate — one fixture, one difference,
    and the difference is the scope.

    ⊕ MRB-326 — AND IT NOW NARROWS `classes` TOO, WHICH IT DID NOT BEFORE.
    That omission was invisible while `loadClassMatrices` drove off
    `class_teachers` alone: nothing ever asked this world for a `classes` row,
    so the table sat unfiltered and harmless. The moment the fallback read
    landed, it stopped being harmless — the FIRST run of this drive after the
    change showed Amy opening BOTH foreign classes in full, with the eyebrow
    and the roster, because the fixture was handing her every class in the
    school.

    ⚠️ THAT WAS THE FIXTURE, NOT THE PRODUCT, AND THE DIFFERENCE MATTERS.
    `classes_teacher_read` is `school_id = auth_user_school_id() AND
    auth_user_teaches_class(id)`, so the real database returns a plain teacher
    nothing for a class she does not teach — which is why the fallback is a
    security boundary at all. The line below models that policy, exactly as
    the three above it model theirs. But a model of a policy is not the
    policy: this half is proved for real, with a real JWT under real RLS,
    by `teacher_admin_real_drive.py` step 1, and that is the check to trust
    if the two ever disagree.
    """
    t = copy.deepcopy(t)
    t["class_teachers"] = [r for r in t["class_teachers"]
                           if r["teacher_id"] == uid]
    mine = {r["class_id"] for r in t["class_teachers"]}
    t["classes"] = [r for r in t.get("classes", []) if r["id"] in mine]
    t["class_members"] = [r for r in t["class_members"] if r["class_id"] in mine]
    t["assignments"] = [r for r in t["assignments"] if r["class_id"] in mine]
    keep = {a["id"] for a in t["assignments"]}
    t["assignment_submissions"] = [r for r in t["assignment_submissions"]
                                   if r["assignment_id"] in keep]
    # A plain teacher holds no scope row and cannot read the staff table.
    t["staff_scopes"] = [r for r in t["staff_scopes"] if r["profile_id"] == uid]
    t["pending_staff"] = []
    return t


# ⚠️ THE EYEBROW IS READ AS ITS OWN ELEMENT, NOT AS A SUBSTRING OF THE SCREEN.
# The first version of this drive asserted "'Acting as admin' comes before
# ' student' in the region's text", and that assertion PASSED WHILE THE FIRST
# ONE FAILED — because the topbar carries a "Pick a student" button, so the
# thing it found first was a button label, and -1 (not present at all) is less
# than any index. A position check over a whole screen can be satisfied by
# furniture. `metaText` is the ONE element the ruling writes, found by its own
# words, so "leads" means leads that line.
#
# ⚠️ AND IT IS UPPERCASED ON SCREEN. The eyebrow is drawn with a
# text-transform, and `innerText` reports the transformed text, so every
# comparison here is case-insensitive. The RULING's string is 'Acting as
# admin'; the CSS's is 'ACTING AS ADMIN'; asserting the first against the
# second is how a correct page reads as broken.
READ_JS = r"""(function () {
  var host = document.getElementById('mrb-teacher');
  var region = host ? host.querySelector('[data-port-region="class"]') : null;
  var state = host ? host.querySelector('[data-mrb-state]') : null;
  function txt(el) { return el ? (el.innerText || '').replace(/\s+/g, ' ').trim() : ''; }

  /* The deepest element whose own text carries the marker — i.e. the eyebrow
     itself rather than every ancestor that contains it. */
  var meta = null;
  if (region) {
    var all = region.querySelectorAll('*');
    for (var i = 0; i < all.length; i++) {
      var t = (all[i].textContent || '').toUpperCase();
      if (t.indexOf('ACTING AS ADMIN') >= 0) { meta = all[i]; }
    }
  }
  return JSON.stringify({
    at: location.pathname + location.search,
    drawn: !!region,
    state: state ? state.getAttribute('data-mrb-state') : '',
    stateText: txt(state),
    regionText: txt(region),
    metaText: txt(meta),
    bodyText: (document.body.innerText || '').replace(/\s+/g, ' ').trim(),
    nodes: host ? host.getElementsByTagName('*').length : 0
  });
})()"""


# The teacher pages ping the Render backend's /api/health on boot. There is no
# backend in a gate run and there must not be one — every browser gate here is
# offline by design — so the browser logs a CORS failure that says nothing
# about this page. Filtered by name, never by widening the check.
def real_errors(errs):
    noise = ("favicon", "mrbadmus-backend.onrender.com")
    return [e for e in errs if not any(n in e for n in noise)]


def open_as(b, base, uid, world, classId, shot):
    """Mount class-detail as `uid`, with `world` as the rows RLS would return."""
    p = b.page("about:blank", settle=0.2)
    # ⚠️ THE IDENTIFIER IS KEPT SO THE STUB CAN BE TAKEN OUT AGAIN — the same
    # reason admin_view_drive keeps it. `addScriptToEvaluateOnNewDocument` is
    # per TARGET, this drive reuses one target, and a stub left armed would
    # follow the browser into the next persona and answer as the wrong one.
    armed = p.send("Page.addScriptToEvaluateOnNewDocument",
                   {"source": av.stub_world(uid, tables=world)}).get("identifier")
    p.set_viewport(1280, 1400)
    p.goto("%s/teacher/class-detail.html?class=%s" % (base, classId), settle=6.0)
    got = json.loads(p.eval(READ_JS))
    errs = real_errors(p.console_errors())
    if shot:
        p.screenshot(shot, width=1280)
    if armed:
        p.send("Page.removeScriptToEvaluateOnNewDocument", {"identifier": armed})
    return got, errs


# ═════════════════════════════════════════════════════════════════════════
# MRB-326 — the machinery Sections B and C need
# ═════════════════════════════════════════════════════════════════════════

def mount(b, base, uid, world, url):
    """Open `url` as `uid` and HAND THE PAGE BACK STILL ARMED.

    `open_as` above reads once and disarms, which is all Section A needs.
    Section C has to press things and then read what the press did, so the
    stub must stay in place across several evals. The caller disarms — and
    must, for the reason `open_as` documents: `addScriptToEvaluateOnNewDocument`
    is per TARGET, this drive reuses one, and a stub left armed answers as the
    wrong persona on the next page.
    """
    p = b.page("about:blank", settle=0.2)
    armed = p.send("Page.addScriptToEvaluateOnNewDocument",
                   {"source": av.stub_world(uid, tables=world)}).get("identifier")
    p.set_viewport(1280, 1600)
    p.goto(url, settle=6.0)
    return p, armed


def disarm(p, armed):
    if armed:
        p.send("Page.removeScriptToEvaluateOnNewDocument", {"identifier": armed})


def writes(p):
    """Every write the stubbed client was asked to make, in order."""
    return json.loads(p.eval(
        "JSON.stringify((window.__MRB_STUB__ && window.__MRB_STUB__.writes) || [])"))


def wrote(ws, table, op=None):
    return [w for w in ws
            if w.get("table") == table and (op is None or w.get("op") == op)]


# Press a control by its ruling marker. Returns how many it found, so a
# fixture can tell "pressed nothing" from "pressed and nothing happened" —
# they look identical from the far side and only one of them is a defect.
PRESS_JS = r"""(function(){
  var n = document.querySelectorAll(%s);
  if (!n.length) { return 0; }
  n[%d].click();
  return n.length;
})()"""


def press(p, sel, idx=0, settle=1.2):
    n = p.eval(PRESS_JS % (json.dumps(sel), idx))
    if settle:
        p.eval("new Promise(function(r){setTimeout(r,%d);})" % int(settle * 1000))
    return n


# ⊕ MRB-326, 6 Sep 2026 — PRESSING A CONTROL DESIGN DREW, WHICH CARRIES NO
# MARKER. Every other control this file presses was ADDED by a ruling, so it
# has a `data-mrb-added` hook to find it by. The reminder is not: it is
# Design's own node 236 inside the homework card, and the port wires it
# (`on: glance.remind`) without adding an attribute. So it is found the way a
# teacher finds it — by its words, inside the class region — and the label is
# returned alongside the count so a green run says WHICH button it pressed.
PRESS_TEXT_JS = r"""(function(){
  var region = document.querySelector(%s);
  if (!region) { return JSON.stringify({found: 0, label: '', reason: 'no region'}); }
  var all = region.querySelectorAll('button');
  var hits = [];
  for (var i = 0; i < all.length; i++) {
    var t = (all[i].innerText || '').replace(/\s+/g, ' ').trim();
    if (t.indexOf(%s) === 0) { hits.push(all[i]); }
  }
  if (!hits.length) { return JSON.stringify({found: 0, label: '', reason: 'no match'}); }
  var label = (hits[0].innerText || '').replace(/\s+/g, ' ').trim();
  hits[0].click();
  return JSON.stringify({found: hits.length, label: label, reason: ''});
})()"""


def press_text(p, region_sel, prefix, settle=1.2):
    """Press the first button under `region_sel` whose text starts `prefix`."""
    got = json.loads(p.eval(PRESS_TEXT_JS
                            % (json.dumps(region_sel), json.dumps(prefix))))
    if settle:
        p.eval("new Promise(function(r){setTimeout(r,%d);})" % int(settle * 1000))
    return got


# ⚠️ A FRAMEWORK-RENDERED FIELD DOES NOT NOTICE `.value =`. Design's runtime
# binds on `input`/`change`, so a value assigned without them is a value the
# page has never heard of — the control looks filled and sends nothing, which
# is precisely the "confirmation of a write that never happened" shape
# `build_teacher_port.py` warns about. Both events, every time.
FILL_JS = r"""(function(){
  var el = document.querySelector(%s);
  if (!el) { return 'no-element'; }
  el.value = %s;
  el.dispatchEvent(new Event('input', {bubbles: true}));
  el.dispatchEvent(new Event('change', {bubbles: true}));
  return el.value;
})()"""


def fill(p, sel, value, settle=0.6):
    got = p.eval(FILL_JS % (json.dumps(sel), json.dumps(value)))
    if settle:
        p.eval("new Promise(function(r){setTimeout(r,%d);})" % int(settle * 1000))
    return got


def text_of(p, sel):
    return p.eval(
        "(function(){var e=document.querySelector(%s);"
        "return e?(e.innerText||'').replace(/\\s+/g,' ').trim():'';})()"
        % json.dumps(sel))


def classless_admin_world(t):
    """The admin's world with the admin's OWN class links taken away.

    ⊕ MRB-326. Ada teaches 8r/Sc1 in `av.LINKS`, deliberately — "so `base()`
    has a list". That convenience hid a defect for a whole ticket: the real
    person ruling 5 exists for is a school_admin who teaches NOTHING, and for
    them `c.CLASSES` is empty, which `teacher-live.js`'s no-classes guard used
    to treat as a reason to refuse the page BEFORE it had looked at `?class=`.
    Every class in their own school answered "You are not teaching any classes
    this year" — a sentence about their timetable, in front of a class they
    were entitled to open.

    It took a real sign-in to find (`teacher_admin_real_drive`, step 2). This
    world is so that it cannot come back without this file going red too.
    """
    t = copy.deepcopy(t)
    t["class_teachers"] = [r for r in t["class_teachers"] if r["teacher_id"] != ADMIN]
    return t


def stripped_world(base_world, class_id):
    """The same world with `class_id`'s ROSTER removed as well as its links.

    Section B's second case. A class with no teacher link, no members and no
    work is three empty collections at once, and `buildClassEntry` has to
    reach Design's "empty" state off all three rather than throwing on the
    first one it meets.
    """
    t = copy.deepcopy(base_world)
    t["class_members"] = [m for m in t["class_members"] if m["class_id"] != class_id]
    t["assignments"] = [a for a in t["assignments"] if a["class_id"] != class_id]
    return t


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--shots", default="/tmp/mrb325-foreign-class")
    args = ap.parse_args()
    os.makedirs(args.shots, exist_ok=True)

    fails = []

    def check(ok_, what, detail=""):
        print("     %s %s%s" % ("✅" if ok_ else "❌", what,
                                ("  — " + detail) if detail else ""))
        if not ok_:
            fails.append(what)

    print("\n🔑  MRB-325 ruling 5 — an admin opens a class they do not teach\n")
    print("     the class under test: %s (taught by Rich, foreign to both "
          "personas)\n" % C_FOREIGN)

    admin_world = tables()
    plain_world = teacher_world(AMY, admin_world)

    # Guard the fixture itself. Both of these are true by construction above,
    # and a fixture that quietly stopped being foreign would turn this whole
    # file green while proving nothing at all.
    own_admin = {r["class_id"] for r in admin_world["class_teachers"]
                 if r["teacher_id"] == ADMIN}
    own_amy = {r["class_id"] for r in plain_world["class_teachers"]}
    check(C_FOREIGN not in own_admin,
          "the fixture: the class is NOT one the admin teaches", repr(sorted(own_admin)))
    check(C_FOREIGN not in own_amy and own_amy,
          "the fixture: nor one the plain teacher teaches, and she has her own",
          repr(sorted(own_amy)))
    check(not any(r["class_id"] == C_FOREIGN
                  for r in plain_world["class_teachers"]),
          "the fixture: a plain teacher's row set cannot see the class at all")

    server, port = cdp.serve("mrbadmus_site", port=PORT)
    base = "http://localhost:%d" % port

    try:
        with cdp.Browser() as b:

            # ── the positive: a school_admin opens it ────────────────────
            print("\n  ── Ada Nwosu · school_admin, opening Rich's class ──")
            got, errs = open_as(b, base, ADMIN, admin_world, C_FOREIGN,
                                os.path.join(args.shots, "admin-foreign-class.png"))

            check(REFUSAL not in got["bodyText"],
                  "1. the refusal state is ABSENT",
                  got["stateText"][:70] or "nothing said")
            check(got["state"] != "unavailable",
                  "…and the page is not in its unavailable state",
                  repr(got["state"]))
            check(got["drawn"], "…the class screen actually rendered",
                  "at %s, %d node(s)" % (got["at"], got["nodes"]))

            meta = got["metaText"].upper()
            check("ACTING AS ADMIN" in meta,
                  "2. the class header carries 'Acting as admin'",
                  got["metaText"][:80] or "no eyebrow carried it")
            # It leads rather than trails — Mide's reason is that a wide roster
            # below must never be mistaken for the admin's own class — so the
            # position within the eyebrow is asserted, not just its presence.
            check(meta.startswith("ACTING AS ADMIN") and "STUDENT" in meta,
                  "…and it LEADS that line, ahead of the student count",
                  got["metaText"][:80])

            missing = [n for _, f, l in ROSTER
                       for n in ["%s %s" % (f, l)]
                       if n not in got["regionText"]]
            check(not missing,
                  "3. the real roster rendered — every active student is on it",
                  "missing: %s" % (", ".join(missing) or "none"))
            check("%s %s" % (DEPARTED[1], DEPARTED[2]) not in got["regionText"],
                  "…and the departed student is not")
            check("Week 1 · Forces" in got["regionText"],
                  "…and the class's real work is on it too")

            check(not errs, "console stayed quiet", "; ".join(errs[:2]))

            # ── the negative control: a plain teacher, same class ────────
            print("\n  ── Amy Barlow · a plain teacher, the SAME class ────")
            got2, errs2 = open_as(b, base, AMY, plain_world, C_FOREIGN,
                                  os.path.join(args.shots, "teacher-foreign-class.png"))

            check(REFUSAL in got2["bodyText"],
                  "4. the refusal DOES appear for a plain teacher",
                  got2["stateText"][:70] or got2["bodyText"][:70])
            check(got2["state"] == "unavailable",
                  "…drawn as the page's own unavailable state",
                  repr(got2["state"]))
            check(not got2["drawn"],
                  "…and no class screen was rendered behind it",
                  "%d node(s)" % got2["nodes"])
            leaked = [n for _, f, l in ROSTER for n in ["%s %s" % (f, l)]
                      if n in got2["bodyText"]]
            check(not leaked, "…and not one of the class's students leaked",
                  ", ".join(leaked) or "none")
            check("Acting as admin" not in got2["bodyText"],
                  "…and nothing claimed she was acting as an admin")

            # A plain teacher's own class must still open — otherwise the
            # refusal above proves only that the fixture is broken.
            print("\n  ── …and her OWN class still opens ──────────────────")
            got3, _ = open_as(b, base, AMY, plain_world, C_OWN_AMY,
                              os.path.join(args.shots, "teacher-own-class.png"))
            check(got3["drawn"] and REFUSAL not in got3["bodyText"],
                  "5. the same teacher opens her own class normally",
                  got3["regionText"][:70])
            check("Acting as admin" not in got3["regionText"],
                  "…without the admin marker, because she is not one")

            # ═══════════════════════════════════════════════════════════
            #  SECTION B — MRB-326 · the class NOBODY teaches
            # ═══════════════════════════════════════════════════════════
            print("\n  ══ B · 9r/Sc4 — a class with NO teacher link at all ══")

            got4, errs4 = open_as(b, base, ADMIN, admin_world, C_UNSTAFFED,
                                  os.path.join(args.shots, "admin-unstaffed-class.png"))
            check(got4["drawn"] and REFUSAL not in got4["bodyText"],
                  "B1. the admin opens a class NOBODY teaches",
                  got4["stateText"][:70] or got4["regionText"][:70])
            check("ACTING AS ADMIN" in got4["metaText"].upper(),
                  "…and it is marked 'Acting as admin' like any foreign class",
                  got4["metaText"][:80] or "no eyebrow carried it")
            check(not errs4, "…console stayed quiet", "; ".join(errs4[:2]))

            # ⚠️ THE NULL PILL IS THE POINT, NOT A DEFECT. `derivePill` reads
            # `class_teachers.subject_id`, and this class has no link to read
            # one off, so it has no subject to name. A pill invented here
            # would be the page asserting something the database does not.
            check("Stu Five" in got4["regionText"] and "Stu Six" in got4["regionText"],
                  "…and its real roster rendered off the members read alone",
                  got4["regionText"][:70])

            # …and with the roster and the work taken away too.
            bare = stripped_world(admin_world, C_UNSTAFFED)
            got5, errs5 = open_as(b, base, ADMIN, bare, C_UNSTAFFED,
                                  os.path.join(args.shots, "admin-unstaffed-empty.png"))
            check(got5["drawn"] and REFUSAL not in got5["bodyText"],
                  "B2. no links, no members, NO work — the page still opens",
                  got5["stateText"][:70] or got5["regionText"][:70])
            check(not errs5,
                  "…and three empty collections at once threw nothing",
                  "; ".join(errs5[:2]))

            # The negative control, again, on the harder class. Without this
            # B1 proves only that `classes` returns rows to somebody.
            plain_bare = teacher_world(AMY, admin_world)
            got6, _ = open_as(b, base, AMY, plain_bare, C_UNSTAFFED,
                              os.path.join(args.shots, "teacher-unstaffed-class.png"))
            check(REFUSAL in got6["bodyText"] and not got6["drawn"],
                  "B3. …and a plain teacher is STILL refused it",
                  got6["stateText"][:70] or got6["bodyText"][:70])
            check("Stu Five" not in got6["bodyText"],
                  "…with not one of its students behind the refusal")

            # ── B4 · the admin who teaches NOTHING ────────────────────
            # Not a variation on B1: a different code path entirely. This one
            # never reached `load()` at all, so `?class=` was unread and the
            # refusal was about the admin's timetable rather than about the
            # class. See `classless_admin_world` for why the fixture could not
            # see it until now.
            nothing = classless_admin_world(admin_world)
            got7, errs7 = open_as(b, base, ADMIN, nothing, C_FOREIGN,
                                  os.path.join(args.shots, "admin-teaches-nothing.png"))
            check(got7["drawn"] and REFUSAL not in got7["bodyText"],
                  "B4. an admin who teaches NO class of their own still opens one",
                  got7["stateText"][:70] or got7["bodyText"][:70])
            check("You are not teaching any classes" not in got7["bodyText"],
                  "…and is not told about their own empty timetable instead",
                  got7["bodyText"][:80])
            check("ACTING AS ADMIN" in got7["metaText"].upper(),
                  "…and the eyebrow still says which hat they are wearing",
                  got7["metaText"][:80] or "no eyebrow carried it")
            check(not errs7, "…console stayed quiet", "; ".join(errs7[:2]))

            # ═══════════════════════════════════════════════════════════
            #  SECTION C — MRB-326 · one fixture per capability
            # ═══════════════════════════════════════════════════════════
            #
            # All on C_FOREIGN, as the admin. The question each asks is the
            # one the MRB-325 gate never did: not "does it open" but "is the
            # control there, and does pressing it do what a teacher's press
            # does". The stub records the write; RLS is proved elsewhere.
            print("\n  ══ C · the full toolset, inside a class Ada does not teach ══")
            klass_url = "%s/teacher/class-detail.html?class=%s" % (base, C_FOREIGN)

            # ── C1 · Import CSV ───────────────────────────────────────
            # No policy needed. `teacher/import.html` never consults
            # class_teachers — it lists staff by `school_id` — and
            # `supabase/functions/roster-import/index.ts` authorises on
            # `role IN (teacher,hod,admin)` AND `school_id`, not on teaching
            # the class. So the capability was never blocked; this fixture
            # exists so that if somebody ever ADDS an ownership check there,
            # it goes red instead of quietly locking admins out of onboarding.
            p1, a1 = mount(b, base, ADMIN, admin_world, base + "/teacher/import.html")
            imp = json.loads(p1.eval(r"""(function(){
              var body = (document.body.innerText||'').replace(/\s+/g,' ').trim();
              return JSON.stringify({
                body: body.slice(0, 400),
                fileInputs: document.querySelectorAll('input[type=file]').length,
                at: location.pathname});})()"""))
            p1.screenshot(os.path.join(args.shots, "admin-import.png"), width=1280)
            disarm(p1, a1)
            check(REFUSAL not in imp["body"] and imp["fileInputs"] >= 1,
                  "C1. IMPORT — the wizard mounts for an admin, with its file input",
                  "%d file input(s) at %s" % (imp["fileInputs"], imp["at"]))

            # ── C2 · Pick a student ───────────────────────────────────
            # No policy needed. The pool is `loadClassMatrices().members`, so
            # this capability was blocked for exactly as long as the class
            # itself was — it is fixed by (a), not by the migration.
            p2, a2 = mount(b, base, ADMIN, admin_world, klass_url)
            found = press(p2, '[data-mrb-added="pick-open"]', settle=1.5)
            picked = p2.eval(
                "(document.body.innerText||'').replace(/\\s+/g,' ')")
            p2.screenshot(os.path.join(args.shots, "admin-picker.png"), width=1280)
            disarm(p2, a2)
            check(found >= 1, "C2. PICK A STUDENT — the control is on the page",
                  "%d control(s)" % found)
            names_in_picker = [n for _, f, l in ROSTER
                               for n in ["%s %s" % (f, l)] if n in picked]
            check(len(names_in_picker) == len(ROSTER),
                  "…and pressing it offers the FOREIGN class's own roster",
                  "%d/%d names" % (len(names_in_picker), len(ROSTER)))

            # ── C3 · Seating plan ─────────────────────────────────────
            # No policy needed: `seating_plans` and `room_layouts` already
            # carry `auth_user_has_scope('school_admin')` arms (MRB-322), and
            # `seating.html` is reached by hash with the class id rather than
            # through its own `myClasses()` picker — which drives off
            # class_teachers and would show an admin nothing.
            p3, a3 = mount(b, base, ADMIN, admin_world, klass_url)
            # ⚠️ MRB_SEATING IS STUBBED BECAUSE IT NAVIGATES. Letting the real
            # one run tears the page out from under the next eval — the exact
            # "Inspected target navigated or closed" failure `teacher_rulings`
            # records for this control. Stubbing records the destination,
            # which is the thing under test anyway.
            p3.eval("window.__seat=[];window.MRB_SEATING=function(id){window.__seat.push(id);};1")
            seat_found = press(p3, '[data-mrb-added="class-seating"]', settle=1.0)
            seat = json.loads(p3.eval("JSON.stringify(window.__seat||[])"))
            disarm(p3, a3)
            check(seat_found >= 1, "C3. SEATING — the control is on the page",
                  "%d control(s)" % seat_found)
            check(seat == [C_FOREIGN],
                  "…and pressing it opens THIS class's plan, not the landing",
                  repr(seat))

            # ── C4 · Marking ──────────────────────────────────────────
            # The marking screen itself needs no policy to READ. A score
            # WRITE does, and `submissions_admin_write` supplies it — but
            # there is no client-side score write anywhere in the estate
            # today (grep: nothing calls `.update()` on assignment_submissions),
            # so the policy is proved by PostgREST in the real drive rather
            # than by a control here. What is proved here is that the screen
            # opens on a class the admin does not teach.
            p4, a4 = mount(b, base, ADMIN, admin_world,
                           "%s/teacher/assignment.html?class=%s" % (base, C_FOREIGN))
            # ⚠️ THE REGION IS NAMED, and a bare `[data-port-region]` is the
            # wrong element. `assignment.html` draws TWO — `topbar` first —
            # so the unnamed selector returns the nav, whose text is the same
            # on every screen and contains none of the paper. The first run
            # of this fixture asserted against exactly that and reported a
            # correct page as broken, which is the failure mode READ_JS's own
            # note at the top of this file already records once.
            mark = json.loads(p4.eval(r"""(function(){
              var r = document.querySelector('[data-port-region="marking"]');
              return JSON.stringify({
                drawn: !!r,
                text: r ? (r.innerText||'').replace(/\s+/g,' ').trim().slice(0,400) : ''
              });})()"""))
            p4.screenshot(os.path.join(args.shots, "admin-marking.png"), width=1280)
            disarm(p4, a4)
            check(mark["drawn"] and REFUSAL not in mark["text"],
                  "C4. MARKING — the marking screen opens on the foreign class",
                  mark["text"][:70])
            check("Week 1 · Forces" in mark["text"],
                  "…showing the class's real paper", mark["text"][:70])

            # ── C5 · Feedback ─────────────────────────────────────────
            # ⚑ UNBLOCKED BY THE MIGRATION. `submission_feedback_insert` is
            # `teacher_id = auth.uid() AND auth_user_teaches_class(...)`;
            # before `submission_feedback_admin_insert` this press got a bare
            # 42501. Driven on student-detail, which is where the control is
            # drawn on a submission-history row.
            p5, a5 = mount(b, base, ADMIN, admin_world,
                           "%s/teacher/student-detail.html?class=%s&student=%s"
                           % (base, C_FOREIGN, ROSTER[0][0]))
            fb_found = press(p5, '[data-mrb-added="feedback-open"]', settle=1.2)
            fill(p5, '[data-mrb-added="feedback-body"]',
                 "MRB-326 fixture: an admin's written feedback.")
            press(p5, '[data-mrb-added="feedback-save"]', settle=1.5)
            fb_writes = wrote(writes(p5), "submission_feedback")
            p5.screenshot(os.path.join(args.shots, "admin-feedback.png"), width=1280)
            disarm(p5, a5)
            check(fb_found >= 1, "C5. FEEDBACK — the control is on the page",
                  "%d control(s)" % fb_found)
            check(len(fb_writes) == 1 and fb_writes[0]["op"] == "insert",
                  "…and saving writes ONE row to submission_feedback",
                  json.dumps(fb_writes)[:120])
            if fb_writes:
                row = (fb_writes[0].get("rows") or [{}])[0]
                # `teacher_id` is the conjunct the admin policy KEEPS. A press
                # that wrote a colleague's id would pass RLS's scope test and
                # still be wrong, so it is asserted here rather than assumed.
                check(row.get("teacher_id") == ADMIN,
                      "…authored as the ADMIN, not as the class's teacher",
                      repr(row.get("teacher_id")))

            # ── C6 · Shoutouts ────────────────────────────────────────
            # ⚑ UNBLOCKED BY THE MIGRATION. `class_shoutouts_insert` requires
            # `auth_user_teaches_class`; `class_shoutouts_admin_insert` is the
            # arm that lets an admin praise a child in a class they do not
            # teach, and it keeps both of the teacher policy's other
            # conjuncts — `author_id = auth.uid()` and recipient-is-a-member.
            p6, a6 = mount(b, base, ADMIN, admin_world, klass_url)
            opt = p6.eval(r"""(function(){
              var sel = document.querySelector('[data-mrb-added="shoutout-recipient"]');
              if (!sel) { return ''; }
              for (var i = 0; i < sel.options.length; i++) {
                if (sel.options[i].value) { return sel.options[i].value; } }
              return '';})()""")
            fill(p6, '[data-mrb-added="shoutout-recipient"]', opt)
            # ⚠️ DO NOT PRESS A TEMPLATE HERE. The first one is ALREADY
            # selected when the composer opens (`MRB_FIRST_TEMPLATE`), and the
            # buttons are a TOGGLE — so a press on it selects nothing, it
            # DESELECTS the default, and Send then refuses with "Pick a
            # template, or write a message". The first run of this fixture did
            # exactly that and read as "the admin cannot send a shoutout".
            # The message is filled instead: it exercises the textarea, and
            # the write carries both it and the still-selected template.
            fill(p6, '[data-mrb-added="shoutout-note"]',
                 "MRB-326 fixture: an admin's shoutout.")
            send_found = press(p6, '[data-mrb-added="shoutout-send"]', settle=2.0)
            so_writes = wrote(writes(p6), "class_shoutouts", "insert")
            p6.screenshot(os.path.join(args.shots, "admin-shoutout.png"), width=1280)
            disarm(p6, a6)
            check(send_found >= 1 and bool(opt),
                  "C6. SHOUTOUTS — composer and recipient list are on the page",
                  "recipient %s" % (opt[:8] or "NONE"))
            check(len(so_writes) >= 1,
                  "…and Send writes to class_shoutouts",
                  json.dumps(so_writes)[:120])
            if so_writes:
                row = (so_writes[0].get("rows") or [{}])[0]
                check(row.get("class_id") == C_FOREIGN and row.get("author_id") == ADMIN,
                      "…on THIS class, authored as the admin",
                      "class=%s author=%s" % (str(row.get("class_id"))[:8],
                                              str(row.get("author_id"))[:8]))
                check(row.get("recipient_id") == opt,
                      "…to the child who was chosen",
                      repr(str(row.get("recipient_id"))[:8]))

            # ── C7 · Reminders ────────────────────────────────────────
            # ⚑ UNBLOCKED BY THE MIGRATION, and by a policy the MRB-325 draft
            # never named: `student_notifications_teacher_send` is `sent_by =
            # auth.uid() AND auth_user_teaches_class(class_id)`, so the
            # Remind control was refused for an admin exactly like the other
            # three. `student_notifications_admin_send` is its admin arm.
            #
            # ⊕ RE-ANCHORED, MRB-326 post-review, 6 Sep 2026. This pressed
            # `[data-mrb-remind] button` — the banner `drawRemindControl`
            # injected above the class header. That banner is DELETED (Mide's
            # redundancy ruling: it sat above a card that already said "2 of 2
            # in"), and with it the only element carrying that attribute. A
            # selector matching nothing would have made this capability read
            # as "the control is not drawn" forever, so the anchor moves to
            # where the reminder now lives: Design's node 236, the dark
            # "Remind all N" button INSIDE the homework card, wired to
            # `glance.remind` by teacher_rulings.py and rendered only when
            # `glance.hasChase` — i.e. only when there is somebody to chase.
            #
            # ⚠️ THE FIXTURE IS WHAT MAKES THE BUTTON EXIST. `tables()` sets
            # one live paper on the foreign class and ONE submission against
            # four active students, so three children owe it, `kChase` is
            # non-empty, and the card draws the button. The assertion below
            # guards that shape rather than trusting it: a fixture that
            # quietly went all-in would delete the button and this capability
            # would go green having pressed nothing.
            p7, a7 = mount(b, base, ADMIN, admin_world, klass_url)
            rem = press_text(p7, '[data-port-region="class"]', "Remind all",
                             settle=1.8)
            rem_found, rem_line = rem["found"], rem["label"]
            rem_writes = wrote(writes(p7), "student_notifications")
            p7.screenshot(os.path.join(args.shots, "admin-remind.png"), width=1280)
            disarm(p7, a7)
            check(rem_found >= 1,
                  "C7. REMINDERS — the control is drawn on the foreign class",
                  rem_line[:70] or ("no control (%s)" % rem["reason"]))
            check(rem_line == "Remind all %d" % (len(ROSTER) - 1),
                  "…labelled for the children who actually owe the paper",
                  repr(rem_line))
            check(len(rem_writes) == 1 and rem_writes[0]["op"] == "upsert",
                  "…and pressing it UPSERTS student_notifications",
                  json.dumps(rem_writes)[:120])
            if rem_writes:
                rows_ = rem_writes[0].get("rows") or []
                # Three of the four have not handed in; the fourth has, and
                # chasing a child who already submitted is the defect this
                # asserts against.
                check(len(rows_) == len(ROSTER) - 1,
                      "…for exactly the students who have not handed in",
                      "%d row(s)" % len(rows_))
                check(all(r.get("sent_by") == ADMIN for r in rows_),
                      "…sent as the admin, which is the conjunct RLS keeps")
                # ⚠️ ignoreDuplicates is what makes a second press honest.
                check((rem_writes[0].get("opts") or {}).get("ignoreDuplicates") is True,
                      "…and still through the rate limit, not around it",
                      json.dumps(rem_writes[0].get("opts")))

            # ── C8 · Digest / Print report ────────────────────────────
            # No policy needed — the digest derives from `base()`, so it was
            # blocked for as long as the class was and is fixed by (a).
            p8, a8 = mount(b, base, ADMIN, admin_world,
                           "%s/teacher/digest.html?class=%s" % (base, C_FOREIGN))
            dig = json.loads(p8.eval(r"""(function(){
              var r = document.querySelector('[data-port-region]');
              return JSON.stringify({drawn: !!r,
                text: r ? (r.innerText||'').replace(/\s+/g,' ').trim().slice(0,300) : ''});
              })()"""))
            p8.screenshot(os.path.join(args.shots, "admin-digest.png"), width=1280)
            disarm(p8, a8)
            check(dig["drawn"] and REFUSAL not in dig["text"],
                  "C8. DIGEST — the printable report opens on the foreign class",
                  dig["text"][:70])

    finally:
        server.shutdown()

    print("\n" + "─" * 68)
    if fails:
        print("❌ teacher_admin_foreign_class_drive: %d check(s) failed"
              % len(fails))
        for f in fails:
            print("   · " + f)
        return 1
    print("✅ teacher_admin_foreign_class_drive: every check passed. "
          "Screenshots in %s" % args.shots)
    return 0


if __name__ == "__main__":
    sys.exit(main())
