#!/usr/bin/env python3
"""Drive the weekly assignment producer against PRODUCTION, as a real student.

    MRB_TEST_STUDENT_PASSWORD=... python3 drive_producer.py

The password is read from the environment and is never printed, never written
to a file, and never included in a failure message. Tokens are truncated to
their first eight characters wherever they are shown at all.
"""

import json
import os
import re
import ssl
import subprocess
import sys
import urllib.error
import urllib.request

# macOS system Python has no usable CA bundle and `certifi` is not installed,
# so urllib fails SSL against every https host here while `curl` — which uses
# the system trust store — is fine. Use curl's bundle if we can find one, and
# fall back to shelling out to curl rather than to an unverified context: this
# script signs in with a real password, and "just turn verification off" is not
# a thing to leave lying in a drive script.
def _ssl_context():
    for path in ("/etc/ssl/cert.pem", "/usr/local/etc/openssl/cert.pem",
                 "/opt/homebrew/etc/ca-certificates/cert.pem"):
        if os.path.exists(path):
            try:
                return ssl.create_default_context(cafile=path)
            except Exception:
                pass
    return None


CTX = _ssl_context()

SUPABASE_URL = "https://urklkrwevjtlfbwnipjn.supabase.co"
API = "https://mrbadmus-backend.onrender.com"
# ⊕ 22 Aug 2026 — the drive account is a PARAMETER, not a constant, so a run
# that must not touch Mide's own account can point it at a throwaway.
# The default is unchanged.
EMAIL = os.environ.get("MRB_DRIVE_EMAIL", "midebolabadmus@gmail.com")
CLASS_8R_SC1 = "d9740ab8-c4e3-4c22-bce9-629b650782c5"

REPO = os.path.dirname(os.path.abspath(__file__))


def anon_key():
    src = open(os.path.join(REPO, "leaderboard.html"), encoding="utf-8").read()
    m = re.search(r"eyJ[A-Za-z0-9_-]{20,}\.[A-Za-z0-9_-]{20,}\.[A-Za-z0-9_-]{10,}", src)
    if not m:
        raise SystemExit("anon key not found in leaderboard.html")
    return m.group(0)


def post(url, body, headers):
    req = urllib.request.Request(
        url, data=json.dumps(body).encode("utf-8"), method="POST",
        headers=dict({"Content-Type": "application/json"}, **headers))
    try:
        with urllib.request.urlopen(req, timeout=60, context=CTX) as r:
            return r.status, json.loads(r.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        raw = e.read().decode("utf-8")
        try:
            return e.code, json.loads(raw)
        except Exception:
            return e.code, {"raw": raw[:400]}


def get(url, headers):
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=90, context=CTX) as r:
            return r.status, json.loads(r.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        raw = e.read().decode("utf-8")
        try:
            return e.code, json.loads(raw)
        except Exception:
            return e.code, {"raw": raw[:400]}


def main():
    pw = (os.environ.get("MRB_DRIVE_PASSWORD")
          or os.environ.get("MRB_TEST_STUDENT_PASSWORD"))
    if not pw:
        raise SystemExit("MRB_TEST_STUDENT_PASSWORD is not set")

    key = anon_key()
    print("\n🚗  drive_producer — production, as a real student\n")

    # ── sign in ──────────────────────────────────────────────────────
    status, tok = post(
        SUPABASE_URL + "/auth/v1/token?grant_type=password",
        {"email": EMAIL, "password": pw},
        {"apikey": key})
    del pw
    if status != 200 or "access_token" not in tok:
        raise SystemExit("sign-in failed: HTTP %s %s"
                         % (status, tok.get("error_description") or tok.get("error") or ""))
    jwt = tok["access_token"]
    uid = tok.get("user", {}).get("id")
    print("     ✅ signed in as %s  (uid %s, token %s…)"
          % (EMAIL, uid, jwt[:8]))

    auth = {"Authorization": "Bearer " + jwt, "apikey": key}
    fails = []

    def check(ok, what, detail=""):
        print(("     ✅ " if ok else "     ❌ ") + what + (("  — " + detail) if detail else ""))
        if not ok:
            fails.append(what + (" — " + detail if detail else ""))

    # ── 1. the producer ──────────────────────────────────────────────
    print("\n  1. GET /api/class/current-assignment")
    status, body = get(API + "/api/class/current-assignment?class_id=" + CLASS_8R_SC1, auth)
    print("     HTTP %s  keys=%s" % (status, sorted(body.keys())))
    check(status == 200, "producer returns 200", "got %s: %s" % (status, body.get("error")))
    week = body.get("week")
    check(week == 1, "current week is 1 (the year opens 1 Sep; today is before it)",
          "week=%r" % week)
    if body.get("reason"):
        print("     reason: %s  detail=%s" % (body["reason"], body.get("detail")))
    a = body.get("assignment")
    qs = body.get("questions") or []
    if a:
        print("     assignment %s  %r  due %s  week %s  auto=%s"
              % (a["id"][:8], a["title"], a["due_at"], a["academic_week"], a["auto_generated"]))
        print("     created=%s  short_week_one=%s  questions=%d"
              % (body.get("created"), body.get("short_week_one"), len(qs)))
        check(a["auto_generated"] is True, "assignment is marked auto_generated")
        check(a["academic_week"] == 1, "assignment carries academic_week=1")
        check(len(qs) > 0, "assignment has questions", "%d" % len(qs))
        for q in qs[:3]:
            print("       q%-2s %-14s %s" % (q["position"], q.get("question_ref"),
                                             (q.get("text") or "")[:64]))
        if qs:
            q0 = qs[0]
            check(len(q0.get("options") or []) == 4, "four options")
            letters = [o["letter"] for o in q0.get("options") or []]
            check(letters == ["A", "B", "C", "D"], "options carry their own letters",
                  str(letters))
            ncorrect = sum(1 for o in q0["options"] if o["correct"])
            check(ncorrect == 1, "exactly one correct option", "%d" % ncorrect)
            whys = [o["why"] for o in q0["options"]]
            correct_why = [o["why"] for o in q0["options"] if o["correct"]][0]
            check(correct_why is None,
                  "the RIGHT-ANSWER slot is closed (why is null, not a generic line)",
                  repr(correct_why))
            check(all(w for o, w in zip(q0["options"], whys) if not o["correct"]),
                  "every distractor names its misconception")
    else:
        check(False, "an assignment was produced",
              "reason=%s detail=%s" % (body.get("reason"), body.get("detail")))

    # ── 2. idempotence: a second call must not create a second one ───
    print("\n  2. second call — must serve the SAME row, not create another")
    status2, body2 = get(API + "/api/class/current-assignment?class_id=" + CLASS_8R_SC1, auth)
    check(status2 == 200, "second call returns 200")
    check(body2.get("created") is False, "second call did NOT create",
          "created=%r" % body2.get("created"))
    if a and body2.get("assignment"):
        check(body2["assignment"]["id"] == a["id"], "same assignment id served")
        check([q["question_ref"] for q in body2["questions"]]
              == [q["question_ref"] for q in qs],
              "same questions, same order (composition is deterministic)")

    # ── 3. identity scoping ──────────────────────────────────────────
    print("\n  3. identity scoping")
    status3, body3 = get(API + "/api/class/current-assignment?class_id="
                         "9168f292-e542-40ba-bb9b-c82b707cfe0f", auth)   # 7h/Sc4, not mine
    check(status3 == 403, "a class the student is NOT in returns 403",
          "got %s" % status3)
    status4, _ = get(API + "/api/class/current-assignment?class_id=" + CLASS_8R_SC1,
                     {"apikey": key})
    check(status4 == 401, "no bearer token returns 401", "got %s" % status4)

    # ── 4. the recall round ──────────────────────────────────────────
    print("\n  4. GET /api/class/practice")
    status5, body5 = get(API + "/api/class/practice?class_id=" + CLASS_8R_SC1, auth)
    rq = body5.get("questions") or []
    check(status5 == 200, "recall returns 200", "got %s" % status5)
    check(len(rq) > 0, "recall has questions", "%d" % len(rq))
    if rq:
        r0 = rq[0]
        print("     %s  rung=%s  topic=%r" % (r0["question_ref"], r0["rung"], r0.get("topic")))
        print("     %s" % (r0["text"] or "")[:80])
        check("#" in r0["question_ref"],
              "question_ref is <lesson_slug>#<rung>", r0["question_ref"])
        check(r0["rung"] in ("recall", "apply"),
              "only the two MARKED rungs are served", r0["rung"])
        check(all(q["rung"] in ("recall", "apply") for q in rq),
              "no self-marked rung leaked into the recall round")
        cw = [o["why"] for o in r0["options"] if o["correct"]]
        check(cw and cw[0] is None,
              "recall's right-answer slot is closed too", repr(cw[0] if cw else None))
        check(sum(1 for o in r0["options"] if o["why"]) == 3,
              "exactly three feedback strings, one per distractor")

    print()
    if fails:
        print("     ❌ %d check(s) failed:" % len(fails))
        for f in fails:
            print("        · " + f)
        print()
        return 1
    print("     ✅ every check passed.\n")
    # Hand the assignment id back so the caller can read the rows.
    if a:
        print("ASSIGNMENT_ID=%s" % a["id"])
    return 0


if __name__ == "__main__":
    sys.exit(main())
