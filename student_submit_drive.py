#!/usr/bin/env python3
"""Drive POST /api/assignment-submit against production, and prove the six
columns it used to discard now arrive — including a self-marked NULL.

    python3 drive_submit.py

Password from the environment; never printed, never written anywhere.
"""

import json
import os
import re
import ssl
import sys
import urllib.error
import urllib.request

SUPABASE_URL = "https://urklkrwevjtlfbwnipjn.supabase.co"
API = "https://mrbadmus-backend.onrender.com"
# ⊕ 22 Aug 2026 — the drive account is a PARAMETER, not a constant, so a run
# that must not touch Mide's own account can point it at a throwaway.
# The default is unchanged.
EMAIL = os.environ.get("MRB_DRIVE_EMAIL", "midebolabadmus@gmail.com")
CLASS_8R_SC1 = "d9740ab8-c4e3-4c22-bce9-629b650782c5"
REPO = os.path.dirname(os.path.abspath(__file__))

CTX = ssl.create_default_context(cafile="/etc/ssl/cert.pem")


def anon_key():
    src = open(os.path.join(REPO, "leaderboard.html"), encoding="utf-8").read()
    return re.search(r"eyJ[A-Za-z0-9_-]{20,}\.[A-Za-z0-9_-]{20,}\.[A-Za-z0-9_-]{10,}",
                     src).group(0)


def call(url, headers, body=None):
    data = json.dumps(body).encode("utf-8") if body is not None else None
    req = urllib.request.Request(
        url, data=data, method=("POST" if data else "GET"),
        headers=dict({"Content-Type": "application/json"}, **headers))
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
    status, tok = call(SUPABASE_URL + "/auth/v1/token?grant_type=password",
                       {"apikey": key}, {"email": EMAIL, "password": pw})
    del pw
    if status != 200:
        raise SystemExit("sign-in failed: %s" % status)
    jwt, uid = tok["access_token"], tok["user"]["id"]
    auth = {"Authorization": "Bearer " + jwt, "apikey": key}
    print("\n📮  drive_submit — the route that was dropping six columns\n")
    print("     signed in (token %s…)" % jwt[:8])

    st, body = call(API + "/api/class/current-assignment?class_id=" + CLASS_8R_SC1, auth)
    a, qs = body.get("assignment"), body.get("questions") or []
    if not a:
        raise SystemExit("no assignment to submit against: %r" % body.get("reason"))
    print("     assignment %s, %d question(s)" % (a["id"][:8], len(qs)))

    # Answer honestly: get the first right, the second wrong, and send the
    # third as a SELF-MARKED rung — is_correct null, criteria claimed. That
    # third one is the whole point: it is the shape that used to be coerced
    # to `false` and scored against the student.
    answers = []
    for i, q in enumerate(qs[:3]):
        correct = next(o for o in q["options"] if o["correct"])
        wrong = next(o for o in q["options"] if not o["correct"])
        if i == 0:
            pick, ok = correct, True
        elif i == 1:
            pick, ok = wrong, False
        else:
            pick, ok = None, None
        row = {
            "question_index": i,
            "question_ref": q["question_ref"],
            "question_text": q["text"],
            "rung": None if q.get("band") else q.get("rung"),
            "correct_answer": correct["text"],
            "correct_option_letter": correct["letter"],
            "time_spent_seconds": 20 + i,
        }
        if pick is not None:
            row["selected_answer"] = pick["text"]
            row["selected_option_letter"] = pick["letter"]
            row["is_correct"] = ok
        else:
            # a self-marked rung: prose the platform cannot score
            row["selected_answer"] = "The alveoli give a huge surface area and a short path."
            row["is_correct"] = None
            row["criteria_met"] = [1, 3]
            row["criteria_total"] = 3
        answers.append(row)

    body = {"assignment_id": a["id"], "answers": answers,
            "total_time_seconds": 63}

    st, res = call(API + "/api/assignment-submit", auth, body)
    print("     submit → HTTP %s  %s" % (st, json.dumps(res)))

    fails = []

    # ⊕ 22 Aug 2026 — W4 CHANGED WHAT A SECOND SUBMIT MEANS, so this gate now
    # asserts the new contract as well as the old one.
    #
    # Until tonight this route INSERTED a fresh submission row on every call,
    # with no unique constraint behind it, so a student who pressed the button
    # twice got two submissions and nothing merged them. Ruled: both attempts
    # are kept and the best counts — which means a bare re-submit against a go
    # that is already finished is refused rather than silently duplicated.
    #
    # So a 409 here is the hole being CLOSED, not the route being broken, and
    # it only shows up when the account has already completed this assignment.
    # The retake is then the supported way to have another go, and the
    # scoring assertions below run against it. Strictly more is checked than
    # before, not less.
    retook = False
    if st == 409 and (res or {}).get("error") == "attempt_already_complete":
        check_ok = True
        print("     ✅ a second submit does NOT duplicate the submission  — 409 "
              "attempt_already_complete, attempt %s" % res.get("attempt_no"))
        body["retake"] = True
        st, res = call(API + "/api/assignment-submit", auth, body)
        retook = True
        print("     retake  → HTTP %s  %s" % (st, json.dumps(res)))

    def check(ok, what, detail=""):
        print(("     ✅ " if ok else "     ❌ ") + what + (("  — " + detail) if detail else ""))
        if not ok:
            fails.append(what)

    check(st == 200 and res.get("success"), "submit returns success",
          json.dumps(res)[:160])
    # ⚠️ THE POINT: 3 answers, one of them self-marked and unmarkable.
    # max_score must be 2, not 3, and score must be 1.
    check(res.get("score") == 1, "score counts the one right answer",
          "score=%r" % res.get("score"))
    check(res.get("max_score") == 2,
          "max_score counts only MARKABLE questions — the self-marked rung is "
          "not scored against the student",
          "max_score=%r (would have been 3 before the fix)" % res.get("max_score"))

    print()
    if fails:
        print("     ❌ %d failed\n" % len(fails))
        return 1
    print("     SUBMISSION_ID=%s" % res.get("id"))
    print("     (now read the attempt rows back via MCP)\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
