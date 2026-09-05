#!/usr/bin/env python3
"""teacher_admin_foreign_class_drive.py — MRB-325 ruling 5, both sides of it.

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

    `class_teachers_own_all` shows a teacher their own link rows and nothing
    else; the members and assignments policies hang off the classes those rows
    name. So: keep this teacher's links, keep only the classes they reach
    through them, and drop everything else. Narrowing the ADMIN world rather
    than writing a second fixture is deliberate — one fixture, one difference,
    and the difference is the scope.
    """
    t = copy.deepcopy(t)
    t["class_teachers"] = [r for r in t["class_teachers"]
                           if r["teacher_id"] == uid]
    mine = {r["class_id"] for r in t["class_teachers"]}
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
