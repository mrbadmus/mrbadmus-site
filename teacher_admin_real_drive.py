#!/usr/bin/env python3
"""teacher_admin_real_drive.py — MRB-326, under REAL RLS with REAL sign-ins.

    MRB_THROWAWAY_PASSWORD=mrb326-throwaway python3 teacher_admin_real_drive.py
    …                                       python3 teacher_admin_real_drive.py --shots DIR
    …                                       python3 teacher_admin_real_drive.py --keep

⚑ WHY THIS FILE EXISTS ALONGSIDE `teacher_admin_foreign_class_drive.py`.

That gate drives the real pages against a STUBBED Supabase client. It is
honest about what that proves — the stub models row visibility, it does not
adjudicate it — and it proves the half no SQL can reach: the control is on
screen, the press fires the right write with the right arguments. What it
cannot prove is the half that actually protects a child's data.

This file is that half, and it is the reason MRB-303 could not have it: the
`hz_*` admin fixtures carry NO PASSWORD on TEST and a standing ruling bans
setting one, because writing to the fixtures a security proof rests on spends
the proof. So MRB-326 uses two accounts created FOR IT, in the same fixture
school, holding nothing anyone else's evidence depends on:

    mrb326_teacher@throwaway.test   plain teacher, teaches 7z/Sc9, no scope
    mrb326_admin@throwaway.test     school_admin scope, teaches NOTHING

Both sign in for real. Every read and every write below goes through
PostgREST as those users, with their own JWTs, against the real policies.

⚑ THE THREE CLASSES, AND WHY IT IS THREE.

    7z/Sc9          the teacher's OWN class          — the control
    HZ 10B Physics  taught by SOMEBODY ELSE          — MRB-325 ruling 5
    HZ 10M Maths    taught by NOBODY AT ALL          — MRB-326

The third is the one that shipped broken. `loadClassMatrices` drove off
`class_teachers`, so its real question was "is there a live teacher link here
I can see" — and on production 25 of the 69 classes in 2026-27 have no live
link at all, their only teacher being an unclaimed `pending_staff` row. Those
25 refused a school_admin with the sentence written for somebody else's
class. Two foreign classes of different KINDS, not one, because the fix
changes which read authorises them and only the third exercises the new read.

⚑ WHAT THE WRITES PROVE, AND THE TRAP IN MEASURING THEM.

⚠️ AN UPDATE THAT RLS MATCHES NOTHING FOR IS A 200, NOT A 403. PostgREST
  cannot distinguish "no such row" from "not yours" without leaking which,
  so it returns success and an empty body. Measured before this ticket's
  migration, the admin's marking write returned exactly that: HTTP 200, body
  `[]`. Anything checking only the status code would have called it a pass.
  So every write here asks for `Prefer: return=representation` and asserts on
  the ROW COMING BACK. An INSERT is honest (403/42501) and is asserted that
  way; an UPDATE is not, and is asserted on its returning row.

⚠️ AND THE SUCCESSES BELOW ARE ONLY SUCCESSES BECAUSE OF THE MIGRATION.
  `20260906044802_mrb326_admin_write_authority` is what turns each of these
  from a refusal into a row. Run this against a project without it and the
  four write checks go red, correctly — that is the gate doing its job, not a
  broken drive.

⛔ IT WRITES ROWS, AND IT CLEANS THEM UP. Every row it creates is soft-deleted
  or hard-deleted at the end of the run, with the SAME JWT that wrote it where
  a policy allows and with a listed id where none does. `--keep` skips the
  cleanup and prints the ids, for when a failure needs inspecting. That is the
  reason this file is registered with a `needs_env` switch rather than run on
  every push: a push must never depend on the network, and it must certainly
  never write to a shared project by accident.

⛔ SCREENSHOTS GO OUTSIDE THE REPO by default (`/tmp`) — MRB-301's rule.

⛔ NO REAL NAMES. Every person here is a throwaway fixture on the sandbox
  project. Nothing in this file names a real member of staff or a real child.
"""

import argparse
import json
import os
import re
import ssl
import sys
import urllib.error
import urllib.request

REPO = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, REPO)
os.chdir(REPO)

import ks3_browser as cdp

REF = "qeppkiswvclkkwbxmlok"                  # TEST. Never production.
URL = "https://%s.supabase.co" % REF
PORT = 5512
CTX = ssl.create_default_context(cafile="/etc/ssl/cert.pem")

# The fixture school and the working year both accounts sit in.
SCHOOL = "d0233615-3ee7-4b1b-a8ff-c912c5196d62"
YEAR = "2f560a43-73b9-422a-8fc7-ec46524a288a"

TEACHER_EMAIL = "mrb326_teacher@throwaway.test"
ADMIN_EMAIL = "mrb326_admin@throwaway.test"

C_OWN = "f3260000-0000-0000-0000-000000000101"     # 7z/Sc9 — the teacher's
C_OTHER = "ee000000-0000-0000-0000-000000000402"   # HZ 10B Physics — someone's
C_NOBODY = "ee000000-0000-0000-0000-000000000403"  # HZ 10M Maths — nobody's

# The throwaway paper and submission seeded on 7z/Sc9 for this drive. Without
# a submission there is nothing to mark and nothing to write feedback against,
# and an UPDATE matching zero rows proves nothing at all (see the trap above).
PAPER = "f3260000-0000-0000-0000-000000000201"
SUBMISSION = "f3260000-0000-0000-0000-000000000301"
PUPIL = "f3260000-0000-0000-0000-000000000011"

# A current member of HZ 10B Physics — the class the plain teacher does NOT
# teach. ⚠️ THE NEGATIVE CONTROL NEEDS A REAL MEMBER OF THAT CLASS, not the
# throwaway pupil: `class_shoutouts_insert` requires BOTH
# `auth_user_teaches_class` AND recipient-is-a-current-member, so a non-member
# recipient would be refused for the wrong reason and the check would pass
# while proving nothing about the teaching conjunct.
OTHER_PUPIL = "ee000000-0000-0000-0000-000000001102"

REFUSAL = "That class is not one of yours."

ENV_SWITCH = "MRB_THROWAWAY_PASSWORD"


def anon_key():
    src = open("shared/config.js", encoding="utf-8").read()
    return re.search(r"'(eyJ[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+)'",
                     src[src.index("const TEST"):]).group(1)


def service_key():
    """The TEST project's service-role key, for CLEANUP ONLY — or None.

    ⚠️ IT IS NOT USED TO PROVE ANYTHING. Every check in this file runs on a
    real user's JWT under real RLS; a service-role key bypasses RLS entirely
    and a proof carried on one would prove nothing at all. It is here for the
    one job no user JWT can do: `student_notifications` has NO delete policy
    for anybody, so the reminder row this drive writes cannot be removed by
    the account that wrote it, and the unique index
    `(student_id, assignment_id, sent_on)` then makes the drive
    UNRE-RUNNABLE ON THE SAME DAY — the second run's honest 201 becomes a 409
    and the gate goes red for a reason that has nothing to do with the code.

    Read from the backend repo's `.env`, the same place `teacher_landing_drive`
    reads it. Absent, cleanup degrades to listing the ids and says so.
    """
    path = "/Users/midebadmus/Documents/GitHub/mrbadmus---backend/.env"
    try:
        for line in open(path, encoding="utf-8"):
            if line.startswith("SUPABASE_SERVICE_ROLE_KEY="):
                return line.split("=", 1)[1].strip()
    except OSError:
        pass
    return None


def call(method, path, key, bearer, body=None, prefer=None):
    """One PostgREST/GoTrue call. Returns (status, parsed-or-text)."""
    headers = {"apikey": key, "Authorization": "Bearer " + bearer,
               "Content-Type": "application/json"}
    if prefer:
        headers["Prefer"] = prefer
    req = urllib.request.Request(
        URL + path,
        data=(json.dumps(body).encode() if body is not None else None),
        headers=headers, method=method)
    try:
        with urllib.request.urlopen(req, timeout=60, context=CTX) as r:
            raw = r.read().decode()
            return r.status, (json.loads(raw) if raw.strip() else None)
    except urllib.error.HTTPError as e:
        raw = e.read().decode()
        try:
            return e.code, json.loads(raw)
        except ValueError:
            return e.code, raw[:300]


def sign_in(email, password, key):
    """A real password grant. ⚠️ VERIFY HERE, NOT IN THE BROWSER.

    A sign-in that fails inside `auth.setSession` presents as a blank page and
    a silent console, and is indistinguishable from a rendering bug. Doing it
    over HTTP first means a credential problem says so in one line.
    """
    st, body = call("POST", "/auth/v1/token?grant_type=password", key, key,
                    {"email": email, "password": password})
    if st != 200 or not isinstance(body, dict) or "access_token" not in body:
        raise SystemExit(
            "\n❌ sign-in FAILED for %s — HTTP %s\n   %s\n"
            "   Not guessed around: fix the account or the password and re-run."
            % (email, st, json.dumps(body)[:300]))
    return body


def real_errors(errs):
    noise = ("favicon", "mrbadmus-backend.onrender.com")
    return [e for e in errs if not any(n in e for n in noise)]


READ_JS = r"""(function () {
  var host = document.getElementById('mrb-teacher');
  var region = host ? host.querySelector('[data-port-region="class"]') : null;
  var state = host ? host.querySelector('[data-mrb-state]') : null;
  function txt(el) { return el ? (el.innerText || '').replace(/\s+/g, ' ').trim() : ''; }
  /* The DEEPEST element carrying the marker — the eyebrow itself, not every
     ancestor containing it. And the eyebrow is UPPERCASED by a
     text-transform, which `innerText` reports, so every comparison on it is
     case-insensitive. Both traps are recorded in
     teacher_admin_foreign_class_drive.py, which met them first. */
  var meta = null;
  if (region) {
    var all = region.querySelectorAll('*');
    for (var i = 0; i < all.length; i++) {
      if ((all[i].textContent || '').toUpperCase().indexOf('ACTING AS ADMIN') >= 0) {
        meta = all[i];
      }
    }
  }
  return JSON.stringify({
    at: location.pathname + location.search,
    drawn: !!region,
    state: state ? state.getAttribute('data-mrb-state') : '',
    metaText: txt(meta),
    regionText: txt(region).slice(0, 400),
    bodyText: (document.body.innerText || '').replace(/\s+/g, ' ').trim().slice(0, 900)
  });
})()"""


def open_class(b, base, sess, key, class_id, shot):
    """Sign the browser in for real, then open the class screen."""
    p = b.page("%s/leaderboard.html?env=test" % base, settle=2.0)
    signed = p.eval("""
      (async function () {
        var c = window.supabase.createClient(%s, %s);
        var r = await c.auth.setSession({access_token: %s, refresh_token: %s});
        return r.error ? 'error: ' + r.error.message : 'ok';
      })()
    """ % (json.dumps(URL), json.dumps(key),
           json.dumps(sess["access_token"]), json.dumps(sess["refresh_token"])))
    p.set_viewport(1280, 1500)
    p.goto("%s/teacher/class-detail.html?class=%s&env=test" % (base, class_id),
           settle=7.0)
    got = json.loads(p.eval(READ_JS))
    got["signed"] = signed
    got["errors"] = real_errors(p.console_errors())
    if shot:
        p.screenshot(shot, width=1280)
    return got


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--shots", default="/tmp/mrb326-shots")
    ap.add_argument("--keep", action="store_true",
                    help="leave the rows this run writes on TEST, and list them")
    args = ap.parse_args()
    os.makedirs(args.shots, exist_ok=True)

    password = os.environ.get(ENV_SWITCH)
    if not password:
        print("\n⏭  teacher_admin_real_drive SKIPPED — %s is not set.\n"
              "    It signs in over the network and WRITES rows on the TEST\n"
              "    project, so it never runs by accident. Set it to run.\n"
              % ENV_SWITCH)
        return 0

    key = anon_key()
    fails = []
    written = []          # (table, id) for the report, whatever cleanup does

    def check(ok_, what, detail=""):
        print("     %s %s%s" % ("✅" if ok_ else "❌", what,
                                ("  — " + detail) if detail else ""))
        if not ok_:
            fails.append(what)

    print("\n🔐  MRB-326 — a real admin, a real teacher, real RLS (TEST)\n")

    teacher = sign_in(TEACHER_EMAIL, password, key)
    admin = sign_in(ADMIN_EMAIL, password, key)
    T_ID, A_ID = teacher["user"]["id"], admin["user"]["id"]
    print("     teacher %s   admin %s" % (T_ID, A_ID))

    # Guard the fixture. Both of these are the premise of everything below,
    # and a fixture that quietly stopped being true would turn the run green
    # while proving nothing — the admin must teach NOTHING, or "opens a class
    # they do not teach" is not what is being measured.
    st, links = call("GET",
                     "/rest/v1/class_teachers?select=class_id&teacher_id=eq.%s"
                     "&ended_at=is.null&deleted_at=is.null" % A_ID,
                     key, admin["access_token"])
    check(st == 200 and links == [],
          "the fixture: the admin teaches no class at all", repr(links))
    st, links = call("GET",
                     "/rest/v1/class_teachers?select=class_id&teacher_id=eq.%s"
                     "&ended_at=is.null&deleted_at=is.null" % T_ID,
                     key, teacher["access_token"])
    check(st == 200 and [r["class_id"] for r in (links or [])] == [C_OWN],
          "the fixture: the teacher teaches exactly 7z/Sc9", repr(links))
    st, nobody = call("GET",
                      "/rest/v1/class_teachers?select=class_id&class_id=eq.%s"
                      "&ended_at=is.null&deleted_at=is.null" % C_NOBODY,
                      key, admin["access_token"])
    check(st == 200 and nobody == [],
          "the fixture: HZ 10M Maths has NO live teacher link, seen as admin",
          repr(nobody))

    # ⚠️ CLEAR THIS DRIVE'S OWN REMINDER ROWS BEFORE MEASURING ANYTHING.
    # Not a convenience: without it a second run on the same day meets the
    # rate limit's unique index and reports 409 for a write that RLS would
    # have accepted — a red gate describing the previous run rather than this
    # tree. Scoped to `sent_by = <this drive's admin>`, so it cannot touch a
    # row any other fixture or person put there.
    svc = service_key()
    if svc:
        st, _ = call("DELETE",
                     "/rest/v1/student_notifications?sent_by=eq.%s" % A_ID,
                     svc, svc)
        print("     cleared this drive's prior reminder rows (HTTP %s)" % st)
    else:
        print("     ⚠️ no service key — a reminder row from an earlier run "
              "today will make check 3d red on the rate limit, not on RLS.")

    server, port = cdp.serve("mrbadmus_site", port=PORT)
    base = "http://localhost:%d" % port

    try:
        with cdp.Browser() as b:

            # ── 1 · the plain teacher ───────────────────────────────────
            print("\n  ── 1 · the plain teacher, signed in for real ──────")
            g = open_class(b, base, teacher, key, C_OWN,
                           os.path.join(args.shots, "real-teacher-own.png"))
            check(g["signed"] == "ok", "signed in", str(g["signed"]))
            check(g["drawn"] and REFUSAL not in g["bodyText"],
                  "1a. her OWN class opens", g["regionText"][:70])
            check("ACTING AS ADMIN" not in g["metaText"].upper()
                  and "Acting as admin" not in g["bodyText"],
                  "…and nothing claims she is acting as an admin",
                  g["metaText"][:80])

            g = open_class(b, base, teacher, key, C_OTHER,
                           os.path.join(args.shots, "real-teacher-foreign.png"))
            check(REFUSAL in g["bodyText"] and not g["drawn"],
                  "1b. a class taught by somebody else is REFUSED",
                  g["bodyText"][:70])

            # ⚠️ THE SAME QUESTION IN SQL, because the page refusing is not
            # the same claim as the database refusing. This is the check that
            # says the `classes` fallback is a boundary and not a hole.
            st, rows = call("GET", "/rest/v1/classes?select=id,name&id=eq.%s"
                            % C_NOBODY, key, teacher["access_token"])
            check(st == 200 and rows == [],
                  "1c. …and `classes` itself returns her NOTHING for an "
                  "unstaffed class", "HTTP %s %s" % (st, json.dumps(rows)[:80]))

            # ── 2 · the admin ───────────────────────────────────────────
            print("\n  ── 2 · the school_admin, signed in for real ───────")
            for label, cid, shot in [
                ("2a. the plain teacher's class", C_OWN, "real-admin-own.png"),
                ("2b. a colleague's class", C_OTHER, "real-admin-foreign.png"),
                ("2c. a class NOBODY teaches", C_NOBODY, "real-admin-nobody.png"),
            ]:
                g = open_class(b, base, admin, key, cid,
                               os.path.join(args.shots, shot))
                check(g["drawn"] and REFUSAL not in g["bodyText"],
                      "%s opens" % label,
                      g["regionText"][:70] or g["bodyText"][:70])
                check("ACTING AS ADMIN" in g["metaText"].upper(),
                      "…marked 'Acting as admin'",
                      g["metaText"][:80] or "no eyebrow carried it")
                check(not g["errors"], "…console stayed quiet",
                      "; ".join(g["errors"][:2]))

    finally:
        server.shutdown()

    # ── 3 · the writes, under real RLS, with the admin's own JWT ───────
    #
    # On 7z/Sc9 — a class the admin does not teach, whose teacher is a
    # different real account. Each of these was measured refused before
    # 20260906044802 and the refusals are quoted in this ticket's report.
    print("\n  ── 3 · the WRITES, as the admin, on a class she does not teach ──")
    A = admin["access_token"]

    # 3a · MARKING. ⚠️ Asserted on the RETURNING ROW, never the status: the
    # pre-migration refusal for this exact call was HTTP 200 with body `[]`.
    st, body = call("PATCH", "/rest/v1/assignment_submissions?id=eq." + SUBMISSION,
                    key, A, {"score": 9}, prefer="return=representation")
    marked = isinstance(body, list) and len(body) == 1 and body[0].get("score") == 9
    check(st == 200 and marked,
          "3a. MARKING — the admin's UPDATE returns the changed row",
          "HTTP %s %s" % (st, json.dumps(body)[:90]))

    # 3b · SHOUTOUT.
    st, body = call("POST", "/rest/v1/class_shoutouts", key, A,
                    {"class_id": C_OWN, "author_id": A_ID, "recipient_id": PUPIL,
                     "template_key": "top_of_class",
                     "message": "MRB-326 drive row — safe to delete."},
                    prefer="return=representation")
    so_id = body[0]["id"] if st in (200, 201) and isinstance(body, list) and body else None
    if so_id:
        written.append(("class_shoutouts", so_id))
    check(so_id is not None,
          "3b. SHOUTOUT — posted on a class the admin does not teach",
          "HTTP %s %s" % (st, json.dumps(body)[:90]))

    # 3c · FEEDBACK. The submission fixture exists, so this is a real write
    # against a real row rather than an insert-nowhere.
    st, body = call("POST", "/rest/v1/submission_feedback", key, A,
                    {"submission_id": SUBMISSION, "teacher_id": A_ID,
                     "body": "MRB-326 drive row — safe to delete."},
                    prefer="return=representation")
    fb_id = body[0]["id"] if st in (200, 201) and isinstance(body, list) and body else None
    if fb_id:
        written.append(("submission_feedback", fb_id))
    check(fb_id is not None,
          "3c. FEEDBACK — written against a real submission",
          "HTTP %s %s" % (st, json.dumps(body)[:90]))

    # 3d · REMINDER. The table the MRB-325 draft never named.
    st, body = call("POST", "/rest/v1/student_notifications", key, A,
                    {"student_id": PUPIL, "class_id": C_OWN,
                     "assignment_id": PAPER, "kind": "reminder", "sent_by": A_ID},
                    prefer="return=representation")
    rem_id = body[0]["id"] if st in (200, 201) and isinstance(body, list) and body else None
    if rem_id:
        written.append(("student_notifications", rem_id))
    check(rem_id is not None,
          "3d. REMINDER — the control's write is no longer refused",
          "HTTP %s %s" % (st, json.dumps(body)[:90]))

    # 3e · THE NEGATIVE CONTROL ON THE WRITES, and it is not optional. Every
    # check above is a widening, and four widenings on their own prove only
    # that the policies are permissive — not that they are policies. The same
    # call, with the PLAIN TEACHER'S JWT, on the class she does NOT teach, to
    # a child who really is on that class's roster so that the only conjunct
    # she fails is the one under test.
    st, body = call("POST", "/rest/v1/class_shoutouts", key,
                    teacher["access_token"],
                    {"class_id": C_OTHER, "author_id": T_ID,
                     "recipient_id": OTHER_PUPIL, "template_key": "top_of_class",
                     "message": "MRB-326 negative control — must be refused."},
                    prefer="return=representation")
    check(st == 403,
          "3e. …and a plain teacher is STILL refused the same write elsewhere",
          "HTTP %s %s" % (st, json.dumps(body)[:90]))

    # ── 4 · put it back ────────────────────────────────────────────────
    print("\n  ── 4 · cleanup ───────────────────────────────────────────")
    if args.keep:
        print("     --keep: rows LEFT on TEST —")
        for table, rid in written:
            print("       %s  %s" % (table, rid))
        print("       assignment_submissions %s (score set to 9)" % SUBMISSION)
    else:
        # ⚠️ SOFT DELETE WHERE THE SCHEMA SAYS SOFT. `class_shoutouts` and
        # `submission_feedback` have NO delete policy for anyone — retention
        # is deliberate and an admin does not get to erase praise or written
        # feedback outright, which is the same rule a teacher lives under.
        # `student_notifications` has no `deleted_at` column at all, so its
        # row is listed for removal rather than pretended away.
        for table, rid in written:
            if table == "student_notifications":
                continue
            st, body = call("PATCH", "/rest/v1/%s?id=eq.%s" % (table, rid), key, A,
                            {"deleted_at": "now()"}, prefer="return=representation")
            gone = isinstance(body, list) and len(body) == 1
            check(gone, "     soft-deleted the %s row it wrote" % table,
                  "HTTP %s %s" % (st, rid))
        # The mark, put back to what the fixture had.
        st, body = call("PATCH", "/rest/v1/assignment_submissions?id=eq." + SUBMISSION,
                        key, A, {"score": 5}, prefer="return=representation")
        check(isinstance(body, list) and len(body) == 1 and body[0].get("score") == 5,
              "     restored the throwaway submission's score to 5",
              "HTTP %s" % st)
        leftover = [r for t, r in written if t == "student_notifications"]
        if leftover and svc:
            for rid in leftover:
                st, _ = call("DELETE", "/rest/v1/student_notifications?id=eq." + rid,
                             svc, svc)
                check(st in (200, 204),
                      "     removed the student_notifications row it wrote",
                      "HTTP %s %s" % (st, rid))
        elif leftover:
            print("     ⚠️ student_notifications has no soft-delete column and no\n"
                  "        delete policy, and no service key was available.\n"
                  "        Row(s) LEFT on TEST, for removal by service role:")
            for rid in leftover:
                print("          %s" % rid)

    print("\n" + "─" * 68)
    if fails:
        print("❌ teacher_admin_real_drive: %d check(s) failed" % len(fails))
        for f in fails:
            print("   · " + f)
        return 1
    print("✅ teacher_admin_real_drive: every check passed, under real RLS. "
          "Screenshots in %s" % args.shots)
    return 0


if __name__ == "__main__":
    sys.exit(main())
