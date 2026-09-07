"""set_work_drive.py — MRB-331. A teacher sets work; a student does it.

⚠️ EVERY CHECK HERE RUNS ON A REAL USER'S JWT AGAINST THE REAL TEST PROJECT,
through a locally-run backend. Nothing is stubbed, and nothing is proved on a
service-role key: service role bypasses RLS entirely, so a proof carried on one
would prove nothing about what a teacher or a child can actually do. The
service key appears in exactly one place — `mrb331_fixture.py`, to build and
tear down the world — and never inside a check.

WHY A DRIVE AND NOT A UNIT TEST. The properties this ticket has to establish are
all seams between things that are individually fine:

  · a class may hold an auto AND a teacher-set assignment in one week, and the
    week lookup must not choke on the pair (`maybeSingle()` did);
  · work set before the school's go-live date must appear ON that date and not
    before, to the child, under RLS;
  · switching a class's automatic work off must stop composition and nothing
    else — the teacher-set work, the marking, the feedback and the reminders
    all have to keep working;
  · a KS4 class must be offered its own correctly-scoped scheme and must be
    refused a KS3 question, including on the eight slugs that collide.

None of those is visible from either side alone.

    MRB_SET_WORK_PASSWORD=<pw> python3 set_work_drive.py
    MRB_SET_WORK_PASSWORD=<pw> python3 set_work_drive.py --keep   # leave the world

⚠️ MRB_SET_WORK_PASSWORD, not MRB_THROWAWAY_PASSWORD — this drive creates its
own accounts and accepts any value, where teacher_admin_real_drive.py signs
into pre-seeded ones and accepts exactly one. See mrb331_fixture.ENV_SWITCH.
"""

import json
import os
import re
import ssl
import subprocess
import sys
import time
import urllib.error
import urllib.request
from datetime import datetime, timedelta, timezone

REPO = os.path.dirname(os.path.abspath(__file__))
os.chdir(REPO)
sys.path.insert(0, REPO)

import mrb331_fixture as FX          # noqa: E402  (after chdir, deliberately)

BACKEND = "/Users/midebadmus/Documents/GitHub/mrbadmus---backend"
PORT = 5531
API = "http://127.0.0.1:%d" % PORT
CTX = ssl.create_default_context(cafile="/etc/ssl/cert.pem")

# ⚠️ ONE CLOCK, READ ONCE, USED EVERYWHERE. The drive sets work, then asks
# whether it released; both questions are about the same instant. Reading
# `now()` twice a few hundred milliseconds apart is how a check that is about
# "before or after the hold" starts failing once a month at a boundary.
NOW = datetime.now(timezone.utc)
DUE = NOW + timedelta(days=7)

# ⚠️ THE HELD SCHOOL NEEDS A LATER DUE DATE THAN THE OPEN ONE, and the reason
# is a property worth keeping rather than a wrinkle to work around: the hold
# pushes RELEASE forward, and the backend refuses `due_at` that falls before
# release ("The due date has to be after the work appears"). The fixture's hold
# is 8 days out, so a due date of NOW + 7 is legitimately refused there. The
# first run of this drive hit exactly that and read as a bug in the code; it
# was the code being right. `check_hold` asserts the refusal deliberately
# below, and then uses a date that clears the hold.
DUE_HELD = NOW + timedelta(days=21)

checks = []


def record(ok, label, detail=""):
    checks.append((ok, label, detail))
    print("   %s  %s%s" % ("✅" if ok else "❌", label,
                           ("\n        " + detail) if detail else ""))
    return ok


def anon_key():
    """The TEST project's anon key, read out of the page config rather than
    typed — the same source `teacher_admin_real_drive.py` uses."""
    src = open("shared/config.js", encoding="utf-8").read()
    return re.search(r"'(eyJ[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+)'",
                     src[src.index("const TEST"):]).group(1)


def sign_in(email, pw, tries=4):
    """A real GoTrue password grant. Returns the access token.

    ⚠️ IT RETRIES, AND THAT IS NOT PADDING. Four accounts sign in back to back
    at the top of this drive, and GoTrue answered the third with a bare TLS
    `UNEXPECTED_EOF_WHILE_READING` — no status, no body, just a dropped
    handshake. A gate that goes red on somebody else's transient network is a
    gate people learn to re-run rather than read, and a gate people re-run
    without reading is not a gate. A real refusal (a 400 for bad credentials)
    still fails immediately; only a transport-level failure is retried.
    """
    key = anon_key()
    last = None
    for attempt in range(tries):
        req = urllib.request.Request(
            FX.env("SUPABASE_URL") + "/auth/v1/token?grant_type=password",
            method="POST",
            headers={"apikey": key, "Content-Type": "application/json"},
            data=json.dumps({"email": email, "password": pw}).encode())
        try:
            with urllib.request.urlopen(req, context=CTX, timeout=30) as r:
                return json.loads(r.read().decode())["access_token"]
        except urllib.error.HTTPError as e:
            # An answer, and it said no. Retrying will not change its mind.
            raise SystemExit("sign-in refused for %s: %s %s"
                             % (email, e.code, e.read().decode()[:200]))
        except (urllib.error.URLError, ssl.SSLError, OSError) as e:
            last = e
            time.sleep(1.5 * (attempt + 1))
    raise SystemExit("sign-in for %s failed after %d tries: %s"
                     % (email, tries, last))


def call(method, path, token, body=None):
    """One call to the locally-run backend, as a signed-in person."""
    req = urllib.request.Request(
        API + path, method=method,
        headers={"Authorization": "Bearer " + token,
                 "Content-Type": "application/json"},
        data=json.dumps(body).encode() if body is not None else None)
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            raw = r.read().decode()
            return r.status, (json.loads(raw) if raw.strip() else {})
    except urllib.error.HTTPError as e:
        raw = e.read().decode()
        try:
            return e.code, json.loads(raw)
        except ValueError:
            return e.code, raw[:400]


class Server:
    """The backend, run locally against TEST, for the life of the drive.

    ⚠️ IT MUST BE THIS REPO'S BACKEND AND THIS RUN'S CODE. Pointing the drive
    at the deployed Render instance would test whatever is on main, which is
    precisely not what is being changed here.
    """

    def __enter__(self):
        # ⚠️ SUPPLY THE ANON KEY. The standing check (`callerClient`) runs the
        # caller's own JWT through `auth_user_has_scope`, so the DATABASE
        # decides who is a school admin rather than the backend guessing. That
        # needs the anon key, and the repo's `.env` does not carry one. Without
        # it the admin path answers 500 `scope_check_failed` — honest, but it
        # means the drive would never exercise the 403 it is there to prove.
        # The key is the one already hardcoded in `shared/config.js`; anon keys
        # are designed to be public.
        env = dict(os.environ, PORT=str(PORT), SUPABASE_ANON_KEY=anon_key())
        self.p = subprocess.Popen(
            ["node", "server.js"], cwd=BACKEND, env=env,
            stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        deadline = time.time() + 45
        while time.time() < deadline:
            if self.p.poll() is not None:
                out = self.p.stdout.read()[:2000]
                raise SystemExit("backend exited on boot:\n" + out)
            try:
                with urllib.request.urlopen(API + "/api/health", timeout=3):
                    return self
            except Exception:
                time.sleep(0.4)
        raise SystemExit("backend did not come up on :%d" % PORT)

    def __exit__(self, *exc):
        self.p.terminate()
        try:
            self.p.wait(timeout=10)
        except subprocess.TimeoutExpired:
            self.p.kill()


# ════════════════════════════════════════════════════════════════════════
# 1 · THE SHEET OFFERS THE RIGHT SCHEME, SCOPED TO THE CLASS
# ════════════════════════════════════════════════════════════════════════
def check_topics(t_teacher):
    print("\n1 · what the sheet offers")

    st, ks3 = call("GET", "/api/teacher/set-work/topics?class_id=" + FX.C_KS3_A,
                   t_teacher)
    record(st == 200, "KS3 class: topics load", "status %s" % st)
    if st != 200:
        return None
    rows = ks3.get("topics") or []
    record(bool(rows), "KS3 class: the scheme is not empty",
           "%d rows" % len(rows))
    record(ks3.get("has_bank") is True, "KS3 class: has_bank is true")
    with_qs = [r for r in rows if r.get("available", 0) > 0]
    record(len(with_qs) > 20,
           "KS3 class: most lessons have banked questions",
           "%d of %d rows have available > 0" % (len(with_qs), len(rows)))

    # ── the tier/pathway scoping, proved by DIFFERENCE ──────────────────
    #
    # A count on its own proves nothing: a route that ignored tier and
    # pathway entirely would still return "some rows" for both classes. What
    # proves the scoping is that the two KS4 classes are offered DIFFERENT
    # schemes, and specifically that the Triple Higher class is offered
    # lessons the Combined Foundation class is not.
    st, trip = call("GET", "/api/teacher/set-work/topics?class_id=" +
                    FX.C_KS4_TRIPLE, t_teacher)
    st2, comb = call("GET", "/api/teacher/set-work/topics?class_id=" +
                     FX.C_KS4_COMB, t_teacher)
    if st != 200 or st2 != 200:
        record(False, "KS4 classes: topics load", "%s / %s" % (st, st2))
        return None
    t_slugs = {r["lesson_slug"] for r in trip.get("topics") or []}
    c_slugs = {r["lesson_slug"] for r in comb.get("topics") or []}
    only_triple = t_slugs - c_slugs
    record(bool(only_triple),
           "KS4: the Triple Higher class is offered lessons the Combined "
           "Foundation class is not",
           "%d triple-only lessons, e.g. %s"
           % (len(only_triple), ", ".join(sorted(only_triple)[:3])))
    record(trip.get("tier") == "higher" and trip.get("pathway") == "triple",
           "KS4: the route reports the class's own tier and pathway",
           "%s / %s" % (trip.get("tier"), trip.get("pathway")))

    # ── THE COLLISION. This is the check that would have failed. ────────
    #
    # Eight KS4 subtopic slugs are byte-identical to KS3 lesson slugs, twelve
    # bank rows each. A topics route that counted `available` by joining on
    # `lesson_slug` alone would report 12 on those eight and 0 everywhere
    # else — which looks like a partially-stocked KS4 bank rather than like a
    # bug, and a teacher would set the twelve.
    COLLIDING = {"aerobic-respiration", "catalysts", "changes-of-state",
                 "chromatography", "conservation-of-mass",
                 "distance-time-graphs", "electric-fields", "magnetic-fields"}
    offered = {r["lesson_slug"]: r.get("available", 0)
               for r in trip.get("topics") or []}
    hit = sorted(s for s in COLLIDING if offered.get(s, 0) > 0)
    record(not hit,
           "KS4: no KS3 questions leak through a colliding lesson slug",
           "leaked on: %s" % ", ".join(hit) if hit
           else "all eight colliding slugs report available = 0")
    record(trip.get("has_bank") is False,
           "KS4: has_bank is false — the sheet says so rather than "
           "offering an empty list")
    record(all(r.get("available", 0) == 0 for r in trip.get("topics") or []),
           "KS4: every lesson reports available = 0")
    return rows


# ════════════════════════════════════════════════════════════════════════
# 2 · SETTING WORK — ONE CLASS, THEN SEVERAL
# ════════════════════════════════════════════════════════════════════════
def pick_lesson(rows, want=10):
    """A lesson a set of `want` questions can actually be drawn around.

    ⚠️ NOT "a lesson with `want` questions in it" — there is no such lesson.
    The bank holds twelve questions per lesson, four in each of three bands, so
    `available` is at most 4 on every row in the estate. A set of ten is drawn
    the way the weekly producer draws one: this lesson first, then the lessons
    before it in the scheme, nearest first (`composeFromBank`, Mide's ruling of
    20 Aug 2026). So what this needs is a lesson with questions of its own AND
    enough scheme BEHIND it to fill from — which means late in the sequence,
    not merely well stocked.
    """
    usable = [r for r in rows if r.get("available", 0) > 0]
    if not usable:
        return None
    return sorted(usable, key=lambda r: -(r.get("academic_week") or 0))[0]


def check_set_single(t_teacher, rows):
    print("\n2 · a teacher sets work on one class")
    lesson = pick_lesson(rows, want=4)
    if not lesson:
        return record(False, "a lesson with enough banked questions exists"), None
    record(True, "chose a lesson", "%s · %d available"
           % (lesson["lesson_slug"], lesson["available"]))

    st, prev = call("GET", "/api/teacher/set-work/preview?class_id=%s"
                    "&sow_entry_id=%s&count=4" % (FX.C_KS3_A, lesson["id"]),
                    t_teacher)
    record(st == 200 and len(prev.get("picked") or []) == 4,
           "preview returns the requested number of questions",
           "status %s, %d picked, %d in the swap pool"
           % (st, len(prev.get("picked") or []), len(prev.get("pool") or [])))
    if st != 200:
        return False, None

    # The swap pool must be DISJOINT from the picked set — a "swap" that could
    # hand back a question already on the sheet is a swap that sometimes does
    # nothing, which is the dead-control shape one level down.
    picked_ids = [q["id"] for q in prev["picked"]]
    pool_ids = [q["id"] for q in prev.get("pool") or []]
    record(not (set(picked_ids) & set(pool_ids)),
           "the swap pool holds no question already picked")
    record(len(set(picked_ids)) == len(picked_ids),
           "the picked questions are distinct")

    # Swap one, exactly as the sheet does, and set THAT.
    chosen = picked_ids[:]
    swapped = None
    if pool_ids:
        swapped = pool_ids[0]
        chosen[1] = swapped

    st, made = call("POST", "/api/teacher/set-work", t_teacher, {
        "class_ids": [FX.C_KS3_A],
        "sow_entry_id": lesson["id"],
        "question_ids": chosen,
        "title": "Set work drive · single class",
        "due_at": DUE.isoformat(),
        "release_at": None,
    })
    ok = record(st == 200 and len(made.get("created") or []) == 1,
                "the work is set on one class",
                "status %s %s" % (st, json.dumps(made)[:200]))
    if not ok:
        return False, None
    aid = made["created"][0]["assignment_id"]
    record(made.get("released_now") is True,
           "a school with no hold releases it immediately")

    # It must have the questions the teacher chose, in the order chosen —
    # including the swap. Read it back through the API, not the DB.
    st, back = call("GET", "/api/class/current-assignment?class_id=%s"
                    "&assignment_id=%s" % (FX.C_KS3_A, aid), t_teacher)
    got = [q.get("question_ref") for q in back.get("questions") or []]
    record(got == chosen,
           "the stored questions are the ones chosen, in order",
           "wanted %s\n        got    %s" % (chosen, got))
    if swapped:
        record(swapped in got and picked_ids[1] not in got,
               "the swapped question replaced the one it was swapped for",
               "%s in, %s out" % (swapped, picked_ids[1]))
    record((back.get("assignment") or {}).get("title")
           == "Set work drive · single class",
           "the teacher's title is stored verbatim")
    return True, aid


def check_set_multi(t_teacher, rows):
    print("\n3 · the same work, set to several classes at once")
    lesson = pick_lesson(rows, want=6)
    if not lesson:
        return record(False, "a lesson with 6+ banked questions exists")
    st, prev = call("GET", "/api/teacher/set-work/preview?class_id=%s"
                    "&sow_entry_id=%s&count=6" % (FX.C_KS3_A, lesson["id"]),
                    t_teacher)
    ids = [q["id"] for q in (prev.get("picked") or [])]
    st, made = call("POST", "/api/teacher/set-work", t_teacher, {
        "class_ids": [FX.C_KS3_A, FX.C_KS3_B],
        "sow_entry_id": lesson["id"],
        "question_ids": ids,
        "title": "Set work drive · two classes",
        "due_at": DUE.isoformat(),
        "release_at": None,
    })
    created = made.get("created") or []
    ok = record(st == 200 and len(created) == 2,
                "one press sets the work on both classes",
                "status %s, %d created" % (st, len(created)))
    if not ok:
        return False
    record(len({c["class_id"] for c in created}) == 2,
           "the two rows are on two different classes")
    record(len({c["assignment_id"] for c in created}) == 2,
           "each class gets an assignment of its OWN, not a shared row — "
           "marking, feedback and completion are per class")

    # ⚠️ A PARTIAL SET IS WORSE THAN A REFUSAL. If one class in the list is
    # not the teacher's, the whole request must fail — otherwise the teacher
    # sees an error and has no way to know which half of it landed.
    st, refused = call("POST", "/api/teacher/set-work", t_teacher, {
        "class_ids": [FX.C_KS3_A, FX.C_FOREIGN],
        "sow_entry_id": lesson["id"],
        "question_ids": ids,
        "title": "Set work drive · should never exist",
        "due_at": DUE.isoformat(), "release_at": None,
    })
    record(st == 403, "a class the teacher does not teach refuses the request",
           "status %s %s" % (st, json.dumps(refused)[:160]))
    st2, listing = call("GET", "/api/class/current-assignment?class_id=" +
                        FX.C_KS3_A, t_teacher)
    titles = [w.get("title") for w in (listing.get("week_work") or [])]
    record("Set work drive · should never exist" not in titles,
           "the refused request wrote NOTHING to the class that WAS the "
           "teacher's — the refusal is all-or-nothing",
           "week_work titles: %s" % titles)
    return True


# ════════════════════════════════════════════════════════════════════════
# 4 · THE GO-LIVE HOLD — SET IT NOW, IT ARRIVES ON THE DATE
# ════════════════════════════════════════════════════════════════════════
def check_hold(t_teacher, t_pupil_b):
    print("\n4 · work set before the school's go-live date")
    st, topics = call("GET", "/api/teacher/set-work/topics?class_id=" +
                      FX.C_KS3_HELD, t_teacher)
    rows = [r for r in (topics.get("topics") or []) if r.get("available", 0) >= 3]
    if st != 200 or not rows:
        return record(False, "the held school's class offers a lesson",
                      "status %s, %d usable rows" % (st, len(rows)))
    lesson = rows[0]
    st, prev = call("GET", "/api/teacher/set-work/preview?class_id=%s"
                    "&sow_entry_id=%s&count=3" % (FX.C_KS3_HELD, lesson["id"]),
                    t_teacher)
    ids = [q["id"] for q in (prev.get("picked") or [])]

    # ── first, that a due date BEFORE the hold releases it is refused ───
    #
    # The hold moves release forward. A due date that lands before the work
    # even appears would give a child an assignment that is already overdue on
    # the day it arrives, which is worse than not setting it.
    st, early = call("POST", "/api/teacher/set-work", t_teacher, {
        "class_ids": [FX.C_KS3_HELD], "sow_entry_id": lesson["id"],
        "question_ids": ids, "title": "Set work drive · due before release",
        "due_at": DUE.isoformat(), "release_at": None,
    })
    record(st == 400 and (early or {}).get("error") == "bad_due_at",
           "a due date that falls before the hold releases the work is "
           "refused", "status %s %s" % (st, json.dumps(early)[:140]))

    # The teacher asks for it NOW. The school is not open until later.
    st, made = call("POST", "/api/teacher/set-work", t_teacher, {
        "class_ids": [FX.C_KS3_HELD], "sow_entry_id": lesson["id"],
        "question_ids": ids, "title": "Set work drive · held",
        "due_at": DUE_HELD.isoformat(), "release_at": None,
    })
    ok = record(st == 200 and made.get("created"),
                "the teacher CAN set work before the school opens",
                "status %s" % st)
    if not ok:
        return False
    record(made.get("released_now") is False,
           "…but it is not released now")
    held_until = made.get("held_until") or made["created"][0].get("release_at")
    record(bool(held_until) and held_until[:10] >= FX.date.today().isoformat(),
           "it is held to the school's open-from date, not to 'now'",
           "held until %s" % held_until)

    # ⚠️ THE CHILD IS THE PROOF, NOT THE PAYLOAD. The route could report a
    # future release and still hand the questions over. Ask the child.
    st, seen = call("GET", "/api/class/current-assignment?class_id=" +
                    FX.C_KS3_HELD, t_pupil_b)
    titles = [w.get("title") for w in (seen.get("week_work") or [])]
    record("Set work drive · held" not in titles,
           "the child in that class cannot see it yet",
           "child's week_work: %s" % titles)
    aid = made["created"][0]["assignment_id"]
    st, direct = call("GET", "/api/class/current-assignment?class_id=%s"
                      "&assignment_id=%s" % (FX.C_KS3_HELD, aid), t_pupil_b)
    record(st == 404,
           "…and cannot reach it by its id either — 404, not 403, so the "
           "refusal does not disclose that work exists",
           "status %s" % st)

    # Now move the school's open date into the past and ask again. Nothing
    # about the assignment changes; only the clock does.
    FX.api("PATCH", "/rest/v1/schools?id=eq." + FX.SCHOOL_HELD,
           {"assignments_open_from": (FX.date.today() -
                                      FX.timedelta(days=1)).isoformat()})
    FX.api("PATCH", "/rest/v1/assignments?id=eq." + aid,
           {"release_at": (NOW - timedelta(minutes=1)).isoformat()})
    st, direct2 = call("GET", "/api/class/current-assignment?class_id=%s"
                       "&assignment_id=%s" % (FX.C_KS3_HELD, aid), t_pupil_b)
    record(st == 200 and (direct2.get("assignment") or {}).get("id") == aid,
           "once the release passes, the same child CAN reach the same work",
           "status %s" % st)
    record(len(direct2.get("questions") or []) == len(ids),
           "…with its questions, which RLS was hiding a moment ago",
           "%d questions" % len(direct2.get("questions") or []))

    # ⚠️ IT IS DELIBERATELY NOT IN THIS WEEK'S `week_work`, AND THAT IS RIGHT.
    # The hold pushed release into next week, and `academic_week` is computed
    # from the release — work that appears next Monday is next week's work. A
    # check that demanded it in THIS week's list would be demanding a bug.
    titles2 = [w.get("title") for w in (direct2.get("week_work") or [])]
    record("Set work drive · held" not in titles2,
           "…and is filed under the week it RELEASES in, not the week it "
           "was set in", "this week's week_work: %s" % titles2)
    return True


# ════════════════════════════════════════════════════════════════════════
# 5 · THE AUTO SWITCH — COMPOSITION STOPS, NOTHING ELSE DOES
# ════════════════════════════════════════════════════════════════════════
def check_auto_off(t_teacher, t_pupil, rows):
    print("\n5 · a class with the automatic weekly work switched off")

    # First: the control. A class with it ON composes when a child opens it.
    st, on = call("GET", "/api/class/current-assignment?class_id=" +
                  FX.C_KS3_A, t_pupil)
    record(st == 200 and (on.get("assignment") or on.get("reason")),
           "control: a class with auto ON still composes",
           "reason %r, assignment %s" % (on.get("reason"),
                                         bool(on.get("assignment"))))

    # ⚠️ DRIVE THE WEEK, DO NOT ASSERT ON A FLAG. The claim is "compose
    # skips", and the only thing that can establish it is a child opening the
    # class and no assignment appearing.
    st, off = call("GET", "/api/class/current-assignment?class_id=" +
                   FX.C_KS3_NOAUTO, t_pupil)
    record(st == 200 and off.get("reason") == "auto_assignments_off",
           "a class with auto OFF composes nothing, and says why",
           "status %s reason %r" % (st, off.get("reason")))
    record(off.get("assignment") is None,
           "…and hands back no assignment")

    # It must still be settable BY HAND. That is the entire point: Rainford
    # runs Sparx, and the switch turns off the weekly producer, not the class.
    st, topics = call("GET", "/api/teacher/set-work/topics?class_id=" +
                      FX.C_KS3_NOAUTO, t_teacher)
    usable = [r for r in (topics.get("topics") or []) if r.get("available", 0) >= 3]
    if not usable:
        return record(False, "the auto-off class offers a lesson")
    st, prev = call("GET", "/api/teacher/set-work/preview?class_id=%s"
                    "&sow_entry_id=%s&count=3" % (FX.C_KS3_NOAUTO,
                                                  usable[0]["id"]), t_teacher)
    st, made = call("POST", "/api/teacher/set-work", t_teacher, {
        "class_ids": [FX.C_KS3_NOAUTO], "sow_entry_id": usable[0]["id"],
        "question_ids": [q["id"] for q in (prev.get("picked") or [])],
        "title": "Set work drive · auto is off here",
        "due_at": DUE.isoformat(), "release_at": None,
    })
    record(st == 200 and made.get("created"),
           "a teacher can still set work on a class with auto off",
           "status %s" % st)
    st, seen = call("GET", "/api/class/current-assignment?class_id=" +
                    FX.C_KS3_NOAUTO, t_pupil)
    titles = [w.get("title") for w in (seen.get("week_work") or [])]
    record("Set work drive · auto is off here" in titles,
           "and the child in that class sees it", "week_work: %s" % titles)

    # And the switch itself, through its route, both ways.
    st, flip = call("POST", "/api/class/auto-assignments", t_teacher,
                    {"class_id": FX.C_KS3_NOAUTO, "auto_assignments": True})
    record(st == 200 and flip.get("auto_assignments") is True,
           "the toggle turns it back on, and reports the stored value",
           "status %s %s" % (st, json.dumps(flip)[:140]))
    st, flip2 = call("POST", "/api/class/auto-assignments", t_teacher,
                     {"class_id": FX.C_FOREIGN, "auto_assignments": False})
    record(st in (403, 404),
           "a teacher cannot flip a class they do not teach",
           "status %s" % st)
    call("POST", "/api/class/auto-assignments", t_teacher,
         {"class_id": FX.C_KS3_NOAUTO, "auto_assignments": False})
    return True


# ════════════════════════════════════════════════════════════════════════
# 6 · AUTO AND TEACHER-SET IN THE SAME WEEK — THE REGRESSION
# ════════════════════════════════════════════════════════════════════════
def check_both_in_one_week(t_pupil, t_teacher):
    """⚠️ THE CHECK THIS WHOLE TICKET COULD HAVE FAILED ON, SILENTLY.

    `assignments_class_week_uniq` used to be `(class_id, academic_week)`, and
    three lookups in server.js found the week's work with `.maybeSingle()`.
    The moment a class holds an auto AND a teacher-set assignment in the same
    week — which is the entire point of Set work — that returns two rows and
    PostgREST turns `maybeSingle()` into an error. Not for the teacher: for
    every CHILD in the class, on the page they open to do their homework.

    Nothing else in this drive would catch it. The set succeeds, the row is
    correct, the RLS is correct, and the class page is simply broken.
    """
    print("\n6 · a class holding auto AND teacher-set work in one week")

    # Make the child compose the auto assignment first, so both exist.
    st, first = call("GET", "/api/class/current-assignment?class_id=" +
                     FX.C_KS3_A, t_pupil)
    record(st == 200, "the child's class page loads at all",
           "status %s %s" % (st, json.dumps(first)[:200]))
    if st != 200:
        return False

    auto = [w for w in (first.get("week_work") or []) if w.get("source") == "auto"]
    teach = [w for w in (first.get("week_work") or []) if w.get("source") == "teacher"]
    record(bool(auto) and bool(teach),
           "the week really does hold both kinds at once",
           "%d auto, %d teacher-set" % (len(auto), len(teach)))
    record((first.get("assignment") or {}).get("auto_generated") is True,
           "the bench still serves the AUTO assignment when there is one")

    # The teacher's own view of the same week must not choke either.
    st, prog = call("GET", "/api/class/progress?class_id=" + FX.C_KS3_A,
                    t_teacher)
    record(st == 200, "the teacher's class progress loads on the same week",
           "status %s %s" % (st, json.dumps(prog)[:160]))
    return True


# ════════════════════════════════════════════════════════════════════════
# 7 · THE ROUND TRIP — a child does it, a teacher marks and replies
# ════════════════════════════════════════════════════════════════════════
def check_round_trip(t_teacher, t_pupil, aid):
    """"Teacher-set work is an ordinary assignment" is a CLAIM. Until
    something has answered it, completed it, scored it, written feedback on it
    and chased it, it is not a fact."""
    print("\n7 · a child completes teacher-set work; the teacher marks it")

    st, paper = call("GET", "/api/class/current-assignment?class_id=%s"
                     "&assignment_id=%s" % (FX.C_KS3_A, aid), t_pupil)
    qs = paper.get("questions") or []
    record(st == 200 and qs,
           "the child can open the teacher-set assignment by its id",
           "status %s, %d questions" % (st, len(qs)))
    if st != 200 or not qs:
        return False

    # Answer every question, one at a time, exactly as the page does.
    right = 0
    for i, q in enumerate(qs):
        opts = q.get("options") or []
        # Answer the first one wrong on purpose, so the score is not a
        # tautology and the marking has something to be wrong about.
        want_correct = (i != 0)
        pick = next((o for o in opts if bool(o.get("correct")) == want_correct),
                    opts[0] if opts else None)
        if not pick:
            continue
        if bool(pick.get("correct")):
            right += 1
        correct = next((o for o in opts if o.get("correct")), {})
        st, _ = call("POST", "/api/assignment/answer", t_pupil, {
            "assignment_id": aid,
            "answer": {
                "question_index": i,
                "question_ref": q.get("question_ref"),
                "question_text": q.get("text"),
                "selected_answer": pick.get("text"),
                "correct_answer": correct.get("text"),
                "selected_option_letter": pick.get("letter"),
                "correct_option_letter": correct.get("letter"),
                "is_correct": bool(pick.get("correct")),
                "time_spent_seconds": 7,
            },
            "retake": False,
        })
        if st != 200:
            record(False, "answer %d saved" % i, "status %s" % st)
            return False
    record(True, "every answer saved, one at a time",
           "%d of %d correct on purpose" % (right, len(qs)))

    st, done = call("POST", "/api/assignment/complete", t_pupil,
                    {"assignment_id": aid, "total_time_seconds": 60})
    record(st == 200 and done.get("submission", {}).get("status") == "complete",
           "the child completes it", "status %s %s" % (st, json.dumps(done)[:180]))
    record(done.get("score") == right and done.get("max_score") == len(qs),
           "it is scored by the server, on the answers actually given",
           "score %s of %s (expected %s of %s)"
           % (done.get("score"), done.get("max_score"), right, len(qs)))

    # ── the teacher's side of the same piece of work ────────────────────
    st, prog = call("GET", "/api/class/progress?class_id=%s&assignment_id=%s"
                    % (FX.C_KS3_A, aid), t_teacher)
    people = prog.get("students") or []
    mine = [p for p in people if p.get("state") == "complete"]
    record(st == 200 and mine,
           "the teacher sees it as complete on the marking screen",
           "status %s, %d of %d complete" % (st, len(mine), len(people)))
    record(any(p.get("score") == right for p in mine),
           "…with the score the child actually got",
           "scores: %s" % [p.get("score") for p in mine])
    return True


def rest(method, path, token, body=None, prefer=None):
    """PostgREST as a signed-in person, under real RLS.

    ⚠️ FEEDBACK AND REMINDERS HAVE NO BACKEND ROUTE. `shared/teacher-data.js`
    writes both straight from the browser through RLS
    (`insertSubmissionFeedback`, `sendReminders`), so driving them through the
    API would test a path that does not exist. This is how the page does it.
    """
    key = anon_key()
    headers = {"apikey": key, "Authorization": "Bearer " + token,
               "Content-Type": "application/json"}
    if prefer:
        headers["Prefer"] = prefer
    req = urllib.request.Request(
        FX.env("SUPABASE_URL") + path, method=method, headers=headers,
        data=json.dumps(body).encode() if body is not None else None)
    try:
        with urllib.request.urlopen(req, context=CTX, timeout=30) as r:
            raw = r.read().decode()
            return r.status, (json.loads(raw) if raw.strip() else {})
    except urllib.error.HTTPError as e:
        return e.code, e.read().decode()[:300]


# ════════════════════════════════════════════════════════════════════════
# 8 · FEEDBACK AND THE CHASE, ON THE TEACHER-SET PIECE OF WORK
# ════════════════════════════════════════════════════════════════════════
def check_feedback_and_chase(t_teacher, t_pupil, aid, teacher_id, pupil_id):
    print("\n8 · written feedback and a reminder, on teacher-set work")

    st, subs = rest("GET", "/rest/v1/assignment_submissions"
                           "?assignment_id=eq.%s&student_id=eq.%s"
                           "&select=id,status,score,max_score" % (aid, pupil_id),
                    t_teacher)
    record(st == 200 and isinstance(subs, list) and subs,
           "the teacher can read the child's submission on this assignment",
           "status %s %s" % (st, json.dumps(subs)[:160]))
    if not (isinstance(subs, list) and subs):
        return False
    sub_id = subs[0]["id"]

    body = "Good work on this one — check question 1 again."
    st, wrote = rest("POST", "/rest/v1/submission_feedback", t_teacher,
                     {"submission_id": sub_id, "teacher_id": teacher_id,
                      "body": body},
                     prefer="return=representation")
    record(st in (200, 201) and isinstance(wrote, list) and wrote,
           "the teacher writes feedback on it, through RLS",
           "status %s %s" % (st, json.dumps(wrote)[:160]))

    # ⚠️ THE CHILD IS THE PROOF. An insert that RLS accepted but the student
    # cannot read is a comment nobody receives.
    st, read_back = rest("GET", "/rest/v1/submission_feedback"
                                "?submission_id=eq.%s&select=body" % sub_id,
                         t_pupil)
    got = [r.get("body") for r in read_back] if isinstance(read_back, list) else []
    record(body in got, "the child can read it back",
           "child sees: %s" % json.dumps(got)[:160])

    # The chase. `student_notifications` is what "Remind all" writes.
    st, sent = rest("POST", "/rest/v1/student_notifications", t_teacher,
                    {"student_id": pupil_id, "assignment_id": aid,
                     "class_id": FX.C_KS3_A, "kind": "reminder",
                     "sent_by": teacher_id,
                     "sent_on": FX.date.today().isoformat()},
                    prefer="return=representation,resolution=ignore-duplicates")
    record(st in (200, 201),
           "a reminder can be sent against the teacher-set assignment",
           "status %s %s" % (st, json.dumps(sent)[:200]))
    st, mine = rest("GET", "/rest/v1/student_notifications"
                           "?assignment_id=eq.%s&select=kind" % aid, t_teacher)
    record(isinstance(mine, list) and any(r.get("kind") == "reminder"
                                          for r in mine),
           "…and the teacher's chase list sees it",
           "rows: %s" % json.dumps(mine)[:160])
    return True


# ════════════════════════════════════════════════════════════════════════
def main():
    pw = os.environ.get(FX.ENV_SWITCH, "")
    if not pw:
        print("Set %s. This drive signs throwaway accounts in for real."
              % FX.ENV_SWITCH)
        return 2

    print("\n🧾  MRB-331 — a teacher sets work, a child does it\n")
    FX.seed()
    gone = FX.clear_work()
    if gone:
        print("  cleared %d assignment(s) from a previous run" % gone)

    t_teacher = sign_in(FX.TEACHER_EMAIL, pw)
    t_pupil = sign_in(FX.PUPIL_EMAIL, pw)
    t_pupil_b = sign_in(FX.PUPIL_B_EMAIL, pw)
    teacher_id = FX.find_user(FX.TEACHER_EMAIL)
    pupil_id = FX.find_user(FX.PUPIL_EMAIL)

    with Server():
        rows = check_topics(t_teacher)
        aid = None
        if rows:
            ok, aid = check_set_single(t_teacher, rows)
            check_set_multi(t_teacher, rows)
        check_hold(t_teacher, t_pupil_b)
        check_auto_off(t_teacher, t_pupil, rows or [])
        check_both_in_one_week(t_pupil, t_teacher)
        if aid:
            if check_round_trip(t_teacher, t_pupil, aid):
                check_feedback_and_chase(t_teacher, t_pupil, aid,
                                         teacher_id, pupil_id)

    if "--keep" not in sys.argv:
        print("\nclearing the throwaway world")
        FX.teardown()
    else:
        print("\n--keep: the throwaway world is left standing")

    bad = [c for c in checks if not c[0]]
    print("\n%s  %d checks, %d failed\n"
          % ("❌" if bad else "✅", len(checks), len(bad)))
    for ok, label, detail in bad:
        print("   · %s" % label)
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
