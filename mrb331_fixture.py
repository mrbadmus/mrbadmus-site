"""mrb331_fixture.py — the throwaway world MRB-331's drives run in.

⚠️ THIS IS NOT A GATE. It seeds and it tears down; it proves nothing. It is
imported by `set_work_drive.py`, which does the proving.

WHY A WORLD OF ITS OWN, rather than reusing Rainford's fixture classes the way
`teacher_admin_real_drive.py` does: Rainford on TEST has exactly one academic
year, 2025-26, and it ended on 31 August 2026. `currentTeachingWeek()` returns
`null` the moment `now > end_date`, so on any date after that every Rainford
class has no current week, composes nothing, and can hold no week-scoped
assignment. A drive about setting work for THIS week cannot run there at all.

So MRB-331 seeds two schools of its own inside the working year, and every id
it writes begins `f3310000-` so a stray row is identifiable at a glance and
removable in one statement. No real school, teacher or child is touched, and no
name in here belongs to anybody.

Two schools, because the go-live hold is a property of a school and the drive
needs one school WITH a hold ahead and one WITHOUT, at the same moment, on the
same clock.

    python3 mrb331_fixture.py --seed      # idempotent; safe to re-run
    python3 mrb331_fixture.py --teardown  # removes every f3310000- row
    python3 mrb331_fixture.py --show      # what is there now
"""

import json
import os
import ssl
import sys
import time
import urllib.error
import urllib.request
from datetime import date, timedelta

REPO = os.path.dirname(os.path.abspath(__file__))
os.chdir(REPO)

BACKEND_ENV = "/Users/midebadmus/Documents/GitHub/mrbadmus---backend/.env"
CTX = ssl.create_default_context(cafile="/etc/ssl/cert.pem")

P = "f3310000-0000-0000-0000-0000000000"

SCHOOL_OPEN = P + "01"      # no hold — the ordinary case
SCHOOL_HELD = P + "02"      # assignments_open_from ahead of today
YEAR_OPEN   = P + "11"
YEAR_HELD   = P + "12"

# The classes. The set is chosen so that each named gate has exactly one class
# that can prove it and no other class that could pass it by accident.
C_KS3_A     = P + "21"      # 8a/Sc1  — the ordinary single-class set
C_KS3_B     = P + "22"      # 8b/Sc1  — the second class in a multi-class set
C_KS3_NOAUTO= P + "23"      # 9a/Sc1  — auto_assignments = false
C_KS4_TRIPLE= P + "24"      # 10a/Bi1 — KS4 triple higher biology: the scoping gate
# ⊕ MRB-335 (RISKS D15). This was `10b/Sc1`, and the name was a LIE about the
# row: the class was labelled combined FOUNDATION while MRB-263's naming
# convention reads set 1 as Higher. That did not matter while the tier was a
# column somebody typed; it matters now that `class_tier_rule()` derives the
# cohort FROM THE NAME on insert and `defaultTierFor()` lands the sheet on it.
# A fixture whose name and columns disagree cannot prove `tier_default_matches_rule`
# — it can only prove that whichever of the two the code happened to read came
# back. `Sc5` is the Foundation set number, so the name now says what the row says.
C_KS4_COMB  = P + "25"      # 10b/Sc5 — KS4 combined FOUNDATION: its control
# ⊕ MRB-335. The third KS4 cohort, and the one that has no other way of being
# reached: a SEPARATE-SCIENCES class whose science is not the same as the other
# seps class's. `10a/Bi1` alone cannot show that a physics class sees physics
# and nothing else — with one seps class in the world, "its own subject" and
# "the first subject" are the same answer. It is also the only class that makes
# `cohort_mismatch` provable at KS4 without leaving the pathway: 10a/Bi1 and
# 10c/Ph1 are BOTH triple higher and are still two cohorts, because the cohort
# carries the science.
C_KS4_SEPS  = P + "28"      # 10c/Ph1 — KS4 triple higher PHYSICS
C_KS3_HELD  = P + "26"      # 8h/Sc1  — in the held school
# ⚠️ SAME SCHOOL, DIFFERENT TEACHER — and the "same school" half is the point.
# A refusal check run against a class in ANOTHER school passes for the wrong
# reason: `assignments_teacher_write` requires school AND teaching, so a
# foreign-school class is refused by the school conjunct before the teaching
# one is even reached, and the check would stay green if the teaching test were
# deleted. This class isolates it. (The same trap is written up on
# `OTHER_PUPIL` in teacher_admin_real_drive.py.)
C_FOREIGN   = P + "27"      # 8z/Sc1  — nobody's, in the open school

# ⚠️ THE KS4 ROWS CARRY NO TIER, NO PATHWAY AND NO SUBJECT, and that is the
# point rather than an omission. `classes_apply_tier_rule` fills all three from
# the NAME on insert and stamps `tier_pathway_source = 'rule'`. A fixture that
# typed them in would be seeding the answer the drive is about to check, and
# `tier_default_matches_rule` would then be a check on this file. What the
# columns hold is the DATABASE's reading of the name; `normalise_ks4()` below
# only ever repairs a row an earlier run left disagreeing with it.
CLASSES = [
    # (id,           name,      key_stage, year, school,      year_id,   auto)
    (C_KS3_A,     "8a/Sc1",  "KS3",  8, SCHOOL_OPEN, YEAR_OPEN, True),
    (C_KS3_B,     "8b/Sc1",  "KS3",  8, SCHOOL_OPEN, YEAR_OPEN, True),
    (C_KS3_NOAUTO,"9a/Sc1",  "KS3",  9, SCHOOL_OPEN, YEAR_OPEN, False),
    (C_KS4_TRIPLE,"10a/Bi1", "KS4", 10, SCHOOL_OPEN, YEAR_OPEN, True),
    (C_KS4_COMB,  "10b/Sc5", "KS4", 10, SCHOOL_OPEN, YEAR_OPEN, True),
    (C_KS4_SEPS,  "10c/Ph1", "KS4", 10, SCHOOL_OPEN, YEAR_OPEN, True),
    (C_KS3_HELD,  "8h/Sc1",  "KS3",  8, SCHOOL_HELD, YEAR_HELD, True),
    (C_FOREIGN,   "8z/Sc1",  "KS3",  8, SCHOOL_OPEN, YEAR_OPEN, True),
]

# The teacher is linked to every class EXCEPT this one.
NOT_TAUGHT = {C_FOREIGN}

# The people. Emails are @throwaway.test, which is not a deliverable domain, so
# a stray password reset cannot reach a real inbox.
TEACHER_EMAIL = "mrb331_teacher@throwaway.test"
ADMIN_EMAIL   = "mrb331_admin@throwaway.test"
PUPIL_EMAIL   = "mrb331_pupil@throwaway.test"
PUPIL_B_EMAIL = "mrb331_pupil_b@throwaway.test"
EMAILS = [TEACHER_EMAIL, ADMIN_EMAIL, PUPIL_EMAIL, PUPIL_B_EMAIL]

# ⚠️ NOT `MRB_THROWAWAY_PASSWORD`, and the difference is load-bearing.
# Two drives shared that one name while meaning two different passwords:
# `teacher_admin_real_drive.py` signs into MRB-326 accounts that are
# PRE-SEEDED on TEST and therefore has exactly one correct value, while this
# fixture CREATES its accounts and re-asserts whatever password it is handed,
# so any value works. Running both from one shell meant either the mrb326
# accounts got a password they were not seeded with, or this drive silently
# adopted mrb326's. The collision was invisible in the direction that matters:
# set_work went green on any value and teacher_admin_real answered a bare
# "sign-in FAILED ... HTTP 403" with nothing pointing at the password.
ENV_SWITCH = "MRB_SET_WORK_PASSWORD"

SUBJECT_SCIENCE = "26000000-0000-0000-0000-000000000001"
SUBJECT_BIOLOGY = "f06e297f-1a44-47d3-9c93-bb616c968cc7"
SUBJECT_PHYSICS = "b7cc103d-53af-45d4-b9fc-4dba20994009"

# The school's TIMETABLE subject for a class, which is a different fact from the
# pool's `subject` and is what `classSubjectId()` files auto work under. A seps
# class is taught by a specialist, so its link carries that science.
SUBJECT_BY_CODE = {"/Bi": SUBJECT_BIOLOGY, "/Ph": SUBJECT_PHYSICS}


def timetable_subject(name):
    for code, sid in SUBJECT_BY_CODE.items():
        if code in name:
            return sid
    return SUBJECT_SCIENCE


def env(name):
    for line in open(BACKEND_ENV, encoding="utf-8"):
        if line.startswith(name + "="):
            return line.split("=", 1)[1].strip()
    raise SystemExit("no %s in %s" % (name, BACKEND_ENV))


def api(method, path, body=None, prefer=None, tries=4):
    """One GoTrue/PostgREST call as the service role.

    ⚠️ IT RETRIES TRANSPORT FAILURES, AND ONLY THOSE. Seeding and teardown make
    dozens of calls back to back, and TLS to Supabase intermittently drops the
    handshake outright — `UNEXPECTED_EOF_WHILE_READING`, or a handshake
    timeout, with no status and no body. That is somebody else's weather, and a
    gate that goes red on it is a gate people learn to re-run rather than read.

    An HTTP answer is never retried, however unwelcome: a 400 has considered
    the request and refused it, and asking again does not change its mind. Only
    a failure to get an answer at all is tried again.
    """
    url, svc = env("SUPABASE_URL"), env("SUPABASE_SERVICE_ROLE_KEY")
    headers = {"apikey": svc, "Authorization": "Bearer " + svc,
               "Content-Type": "application/json"}
    if prefer:
        headers["Prefer"] = prefer
    last = None
    for attempt in range(tries):
        req = urllib.request.Request(
            url + path, method=method, headers=headers,
            data=json.dumps(body).encode() if body is not None else None)
        try:
            with urllib.request.urlopen(req, context=CTX, timeout=30) as r:
                raw = r.read().decode()
                return r.status, (json.loads(raw) if raw.strip() else {})
        except urllib.error.HTTPError as e:
            return e.code, e.read().decode()[:500]
        except (urllib.error.URLError, ssl.SSLError, OSError) as e:
            last = e
            time.sleep(1.5 * (attempt + 1))
    raise SystemExit("%s %s failed after %d tries: %s"
                     % (method, path.split("?")[0], tries, last))


def sql(statement):
    """DDL-free SQL through PostgREST's rpc-less path is not available, so the
    fixture speaks to the tables directly. Kept as a helper so the callers read
    as statements rather than as HTTP."""
    raise NotImplementedError  # tables are written through `upsert` below


def upsert(table, rows, on_conflict="id"):
    """⚠️ `resolution=merge-duplicates` IS NOT OPTIONAL. Without the Prefer
    header PostgREST ignores `on_conflict` entirely and a re-run — or, for
    `profiles`, the very first run, because a trigger has already written the
    row — comes back 409 on the primary key."""
    st, d = api("POST", "/rest/v1/%s?on_conflict=%s" % (table, on_conflict),
                rows, prefer="resolution=merge-duplicates")
    if st not in (200, 201, 204):
        raise SystemExit("upsert %s failed %s: %s" % (table, st, d))
    return d


def password():
    pw = os.environ.get(ENV_SWITCH, "")
    if not pw:
        raise SystemExit(
            "Set %s to seed sign-in-able accounts.\n"
            "  %s=<something-throwaway> python3 mrb331_fixture.py --seed"
            % (ENV_SWITCH, ENV_SWITCH))
    return pw


def find_user(email):
    st, users = api("GET", "/auth/v1/admin/users?per_page=1000")
    if st != 200:
        raise SystemExit("could not list users: %s %s" % (st, users))
    for u in (users.get("users") or []):
        if (u.get("email") or "").lower() == email.lower():
            return u["id"]
    return None


def ensure_user(email, pw):
    """Create the auth user if absent; return its id either way.

    ⚠️ A TRIGGER CREATES THE `profiles` ROW, not this function. Supabase's
    handle_new_user writes one with `role = 'student'` and a generated
    username the moment the auth user exists, so seeding a profile here would
    race it and lose. The caller UPDATES the row the trigger made.
    """
    uid = find_user(email)
    if uid:
        # Re-assert the password so a re-run is usable even if the previous
        # run used a different one.
        api("PUT", "/auth/v1/admin/users/" + uid, {"password": pw})
        return uid
    st, d = api("POST", "/auth/v1/admin/users",
                {"email": email, "password": pw, "email_confirm": True})
    if st != 200:
        raise SystemExit("create %s failed %s: %s" % (email, st, d))
    return d["id"]


def rule_for(name):
    """What `class_tier_rule(name)` says, asked of the DATABASE.

    ⚠️ NOT A PYTHON MIRROR OF THE RULE, deliberately. The rule already exists
    twice — as SQL (the authority, because the trigger runs it) and as JS
    (`classTierRule()` in set-work-scope.js, for the admin route's defaulting)
    — and `test_set_work_v2.js` drives those two against each other. A third
    copy here would be a copy nothing checks, in the one file whose job is to
    build the world the checks run in: it would drift, and the drive would
    then measure this file's opinion of the rule rather than the database's.
    """
    st, rows = api("POST", "/rest/v1/rpc/class_tier_rule", {"p_name": name})
    if st != 200 or not isinstance(rows, list) or not rows:
        raise SystemExit("class_tier_rule(%r) → %s %s" % (name, st, str(rows)[:200]))
    r = rows[0]
    return (r.get("tier"), r.get("pathway"), r.get("subject"))


def ks4_rows():
    """The KS4 fixture classes as the database currently holds them."""
    ks4 = [(cid, name) for (cid, name, ks, *_r) in CLASSES if ks == "KS4"]
    if not ks4:
        return [], {}
    st, rows = api("GET", "/rest/v1/classes?id=in.(%s)&select=id,name,tier,"
                          "science_pathway,science_subject,tier_pathway_source"
                   % ",".join(c for c, _n in ks4))
    return ks4, ({r["id"]: r for r in rows} if isinstance(rows, list) else {})


def ks4_mismatches(ks4, have):
    """Every KS4 fixture row whose cohort is not what its NAME says it is."""
    out = []
    for cid, name in ks4:
        row = have.get(cid)
        if not row:
            out.append((cid, name, "absent", None))
            continue
        want = rule_for(name)
        got = (row.get("tier"), row.get("science_pathway"),
               row.get("science_subject"))
        if got != want or row.get("tier_pathway_source") != "rule":
            out.append((cid, name,
                        "%s src=%s" % ("/".join(str(g) for g in got),
                                       row.get("tier_pathway_source")),
                        "%s src=rule" % "/".join(str(w) for w in want)))
    return out


def normalise_ks4(fresh_ids):
    """Read the KS4 rows back and, on a FRESH insert, assert rather than repair.

    ⊕ MRB-335, second pass. The first version of this function read the rows
    and repaired any that disagreed with their name — and it ran immediately
    after the INSERT that the trigger had just filled. That is a repair placed
    exactly where it can hide the thing the drive is about to measure: if
    `classes_apply_tier_rule` stopped filling tomorrow, every fresh row would
    come out NULL, this would quietly write the right answer in, and
    `tier_default_matches_rule` would go green on a trigger that had died.
    A fixture is allowed to build a world; it is not allowed to supply an
    answer the checks are looking for.

    So the two cases are now separated, and only one of them is a repair:

      A ROW INSERTED BY THIS RUN is the trigger's own output. It is READ BACK
      and ASSERTED. A mismatch is a hard failure with the row printed, because
      the only thing that could have produced it is the trigger not doing its
      job — and that is a finding about the database, not a mess to tidy.

      A ROW THAT ALREADY EXISTED is a legacy row from an older seed, which the
      trigger never touches: it only DERIVES on INSERT. `10b/Sc1` was seeded
      as combined FOUNDATION while its name said set 1, so MRB-335's backfill
      correctly stamped it `admin`, and renaming it to `10b/Sc5` cannot undo
      that. Those are repaired, once, loudly, and named.

    ⚠️ `tier_pathway_source` IS SENT EXPLICITLY ON THE REPAIR, and that is what
    stops it labelling itself. The trigger's UPDATE arm stamps `admin` when the
    triple moves AND the source is unchanged from OLD; naming a new source
    means the row records what actually decided it — the rule — rather than
    recording this script as a head of department.
    """
    ks4, have = ks4_rows()
    if not ks4:
        return

    bad = ks4_mismatches(ks4, have)

    # ── the assertion, on rows this run created ──────────────────────
    fresh_bad = [b for b in bad if b[0] in fresh_ids]
    if fresh_bad:
        raise SystemExit(
            ("mrb331_fixture: the class-name trigger did not fill %d row(s) "
             "it had just inserted.\n"
             "  `classes_apply_tier_rule` is what makes a KS4 class's cohort "
             "follow its name (MRB-263 / MRB-335), and these rows came out of "
             "the INSERT disagreeing with it. That is a finding about the "
             "database, not something this fixture may write over — doing so "
             "would make `tier_default_matches_rule` pass on a dead trigger.\n"
             % len(fresh_bad))
            + "\n".join("    %-9s is %s, the rule says %s"
                         % (name, got, want) for _c, name, got, want in fresh_bad))
    fresh_ok = [c for c, _n in ks4 if c in fresh_ids]
    if fresh_ok:
        print("  trigger   filled %d fresh KS4 row(s) from their names, all "
              "src=rule" % len(fresh_ok))

    # ── the repair, on rows that predate this run ────────────────────
    fixed = []
    for cid, name, got, want in bad:
        if cid in fresh_ids:
            continue
        w = rule_for(name)
        st, _ = api("PATCH", "/rest/v1/classes?id=eq." + cid,
                    {"tier": w[0], "science_pathway": w[1],
                     "science_subject": w[2], "tier_pathway_source": "rule"})
        if st not in (200, 204):
            raise SystemExit("could not normalise %s: %s" % (name, st))
        fixed.append("%s %s → %s" % (name, got, want))
    if fixed:
        print("  repaired  %d LEGACY row(s) the trigger never saw (it derives "
              "on INSERT only): %s" % (len(fixed), "; ".join(fixed)))

        # ⚠️ AND THE REPAIR IS ITSELF READ BACK. A PATCH that PostgREST
        # accepted and matched no row answers 200 with an empty body — the
        # same silent no-op `/api/class/auto-assignments` was rewritten to
        # refuse. Never trust a write you did not read.
        _ks4, again = ks4_rows()
        still = ks4_mismatches(_ks4, again)
        if still:
            raise SystemExit(
                "mrb331_fixture: the repair did not take on %d row(s): %s"
                % (len(still), "; ".join("%s is %s" % (n, g)
                                         for _c, n, g, _w in still)))


def seed():
    pw = password()
    today = date.today()
    # The working year, not a literal: the drive must run on any date.
    y_start = date(today.year if today.month >= 9 else today.year - 1, 9, 1)
    y_end = date(y_start.year + 1, 8, 31)
    hold_on = today + timedelta(days=8)     # comfortably ahead, never today

    upsert("schools", [
        {"id": SCHOOL_OPEN, "name": "MRB-331 Set Work School",
         "code": "MRB331OPEN", "assignments_open_from": None},
        {"id": SCHOOL_HELD, "name": "MRB-331 Held School",
         "code": "MRB331HELD",
         "assignments_open_from": hold_on.isoformat()},
    ])
    upsert("academic_years", [
        {"id": YEAR_OPEN, "school_id": SCHOOL_OPEN, "name": "%d-%s"
         % (y_start.year, str(y_end.year)[2:]),
         "start_date": y_start.isoformat(), "end_date": y_end.isoformat()},
        {"id": YEAR_HELD, "school_id": SCHOOL_HELD, "name": "%d-%s"
         % (y_start.year, str(y_end.year)[2:]),
         "start_date": y_start.isoformat(), "end_date": y_end.isoformat()},
    ])
    # ⚠️ NO tier / science_pathway / science_subject COLUMN IN THE PAYLOAD AT
    # ALL, and the absence is load-bearing in BOTH directions. On a first run
    # the KS4 rows insert with all three NULL, so `classes_apply_tier_rule`
    # fills them from the name — which is the fact the drive then measures. On
    # a re-run PostgREST's `ON CONFLICT DO UPDATE` only touches the columns the
    # payload names, so a rename cannot disturb a cohort, and the trigger's
    # UPDATE arm (which stamps `admin` when the triple MOVES) never fires.
    # ⚠️ WHICH ROWS THIS RUN CREATED IS READ BEFORE THE UPSERT, NOT AFTER.
    # It is the only way to tell the trigger's own output from a legacy row —
    # and telling them apart is what lets `normalise_ks4` ASSERT on the first
    # and repair only the second.
    _pre_ks4, pre_have = ks4_rows()
    upsert("classes", [
        {"id": cid, "school_id": sch, "academic_year_id": yr, "name": name,
         "key_stage": ks, "year_group": yg, "auto_assignments": auto}
        for (cid, name, ks, yg, sch, yr, auto) in CLASSES
    ])
    normalise_ks4({cid for cid, _n in _pre_ks4 if cid not in pre_have})

    teacher = ensure_user(TEACHER_EMAIL, pw)
    admin = ensure_user(ADMIN_EMAIL, pw)
    pupil = ensure_user(PUPIL_EMAIL, pw)
    pupil_b = ensure_user(PUPIL_B_EMAIL, pw)

    upsert("profiles", [
        {"id": teacher, "role": "teacher", "school_id": SCHOOL_OPEN,
         "first_name": "Tess", "last_name": "Thrower"},
        {"id": admin, "role": "admin", "school_id": SCHOOL_OPEN,
         "first_name": "Adele", "last_name": "Thrower"},
        {"id": pupil, "role": "student", "school_id": SCHOOL_OPEN,
         "first_name": "Pip", "last_name": "Thrower"},
        {"id": pupil_b, "role": "student", "school_id": SCHOOL_HELD,
         "first_name": "Pim", "last_name": "Thrower"},
    ])

    # The teacher teaches everything in the open school; the held school's
    # class too, so one account can drive the hold case without a second
    # sign-in. `subject_id` is what `classSubjectId()` files the work under.
    upsert("class_teachers", [
        {"id": P + "3" + str(i), "class_id": cid, "teacher_id": teacher,
         "role": "subject_teacher",
         "subject_id": timetable_subject(name)}
        for i, (cid, name, *_rest) in enumerate(CLASSES)
        if cid not in NOT_TAUGHT
    ], on_conflict="id")

    upsert("class_members", [
        {"id": P + "41", "class_id": C_KS3_A, "student_id": pupil,
         "joined_via": "admin_added"},
        {"id": P + "42", "class_id": C_KS3_B, "student_id": pupil,
         "joined_via": "admin_added"},
        {"id": P + "43", "class_id": C_KS3_NOAUTO, "student_id": pupil,
         "joined_via": "admin_added"},
        {"id": P + "44", "class_id": C_KS4_TRIPLE, "student_id": pupil,
         "joined_via": "admin_added"},
        {"id": P + "45", "class_id": C_KS3_HELD, "student_id": pupil_b,
         "joined_via": "admin_added"},
    ], on_conflict="id")

    print("seeded:")
    print("  schools   %s (open)  %s (held from %s)"
          % (SCHOOL_OPEN[:13], SCHOOL_HELD[:13], hold_on))
    print("  year      %s → %s" % (y_start, y_end))
    print("  classes   %d" % len(CLASSES))
    print("  teacher   %s  %s" % (TEACHER_EMAIL, teacher))
    print("  admin     %s  %s" % (ADMIN_EMAIL, admin))
    print("  pupil     %s  %s" % (PUPIL_EMAIL, pupil))
    print("  pupil B   %s  %s" % (PUPIL_B_EMAIL, pupil_b))


def clear_work():
    """Remove every assignment on the fixture classes, leaving the world.

    ⚠️ A DRIVE THAT CANNOT BE RUN TWICE IN A DAY IS A GATE THAT GOES RED FOR A
    REASON THAT HAS NOTHING TO DO WITH THE CODE. The set-work checks assert on
    what a class's week holds, so yesterday's run — or the run five minutes
    ago — would be counted as today's. `teacher_admin_real_drive.py` hit the
    same wall on `student_notifications` and wrote it up; this is the same
    lesson applied one table over.
    """
    ids = ",".join(c[0] for c in CLASSES)
    st, mine = api("GET", "/rest/v1/assignments?class_id=in.(%s)&select=id" % ids)
    if not isinstance(mine, list) or not mine:
        return 0
    aids = ",".join(a["id"] for a in mine)
    st, subs = api("GET", "/rest/v1/assignment_submissions"
                          "?assignment_id=in.(%s)&select=id" % aids)
    if isinstance(subs, list) and subs:
        sids = ",".join(s["id"] for s in subs)
        api("DELETE", "/rest/v1/assignment_question_attempts"
                      "?submission_id=in.(%s)" % sids)
        api("DELETE", "/rest/v1/submission_feedback?submission_id=in.(%s)" % sids)
        api("DELETE", "/rest/v1/assignment_submissions?id=in.(%s)" % sids)
    api("DELETE", "/rest/v1/student_notifications?assignment_id=in.(%s)" % aids)
    api("DELETE", "/rest/v1/assignment_questions?assignment_id=in.(%s)" % aids)
    api("DELETE", "/rest/v1/assignments?id=in.(%s)" % aids)
    return len(mine)


def teardown():
    """Remove everything this file made, children first, and PROVE it.

    ⚠️ ORDER IS FK ORDER, AND GETTING IT WRONG FAILS SILENTLY. The first
    version of this deleted `assignments` before `student_notifications`, which
    references them — Postgres refused, `api()` returned the 409, teardown
    ignored the status, printed "torn down" and left seven classes, two schools
    and six assignments on TEST. A teardown that reports success without
    checking is worse than one that crashes: the litter is then somebody else's
    problem, discovered later, by someone who does not know what it is.

    ⚠️ `profiles` BEFORE `auth.users`. `profiles_id_fkey` references
    `auth.users(id)`, and deleting the auth user first returns a bare 500 from
    GoTrue with no indication that a foreign key was the reason.

    So: every delete's status is checked, and the whole thing is re-queried at
    the end. If anything survives, this says what and exits non-zero.
    """
    ids = ",".join(c[0] for c in CLASSES)
    problems = []

    def rm(path, what):
        st, d = api("DELETE", "/rest/v1/" + path)
        if st not in (200, 204):
            problems.append("%s → %s %s" % (what, st, str(d)[:160]))

    st, mine = api("GET", "/rest/v1/assignments?class_id=in.(%s)&select=id" % ids)
    if isinstance(mine, list) and mine:
        aids = ",".join(a["id"] for a in mine)
        st, subs = api("GET", "/rest/v1/assignment_submissions"
                              "?assignment_id=in.(%s)&select=id" % aids)
        if isinstance(subs, list) and subs:
            sids = ",".join(s["id"] for s in subs)
            rm("assignment_question_attempts?submission_id=in.(%s)" % sids,
               "answer attempts")
            rm("submission_feedback?submission_id=in.(%s)" % sids, "feedback")
            rm("assignment_submissions?id=in.(%s)" % sids, "submissions")
        # BEFORE the assignments they point at.
        rm("student_notifications?assignment_id=in.(%s)" % aids, "reminders")
        rm("assignment_questions?assignment_id=in.(%s)" % aids, "questions")
        rm("assignments?id=in.(%s)" % aids, "assignments")

    for table in ("student_notifications", "class_members", "class_teachers"):
        rm("%s?class_id=in.(%s)" % (table, ids), table)
    rm("classes?id=in.(%s)" % ids, "classes")
    rm("academic_years?id=in.(%s,%s)" % (YEAR_OPEN, YEAR_HELD), "academic years")

    # ⚠️ `audit_log` REFERENCES `profiles`, AND THE SET-WORK ROUTES WRITE TO IT.
    # Every `assignment.set_by_teacher` and `class.auto_assignments.set` row
    # this drive causes names the acting teacher, so the teacher's profile
    # cannot be removed until those rows are. That is the routes behaving
    # correctly — an audited write is the point — and the teardown's job to
    # account for, not theirs to stop doing.
    for email in EMAILS:
        uid = find_user(email)
        if uid:
            rm("audit_log?actor_id=eq." + uid, "audit rows for " + email)

    for email in EMAILS:
        uid = find_user(email)
        if uid:
            rm("profiles?id=eq." + uid, "profile for " + email)
            st, d = api("DELETE", "/auth/v1/admin/users/" + uid)
            if st not in (200, 204):
                problems.append("auth user %s → %s" % (email, st))
    # ⚠️ A PROFILE THIS FILE DID NOT CREATE CAN STILL PIN THE SCHOOL.
    # `profiles.school_id` references `schools`, and anything that signs an
    # account into the throwaway school — a concurrent lane's drive, an
    # abandoned run — leaves a row keyed to a person this file knows nothing
    # about. DETACHED, never deleted: removing somebody else's profile to tidy
    # up my own school is a far worse outcome than leaving a null school_id on
    # a throwaway account. The detach is reported so it is not silent.
    st, strays = api("GET", "/rest/v1/profiles?school_id=in.(%s,%s)"
                            "&select=id,username" % (SCHOOL_OPEN, SCHOOL_HELD))
    if isinstance(strays, list) and strays:
        for row in strays:
            api("PATCH", "/rest/v1/profiles?id=eq." + row["id"],
                {"school_id": None})
        print("     detached %d profile(s) this file did not create: %s"
              % (len(strays), ", ".join(r.get("username") or r["id"][:8]
                                        for r in strays)))

    rm("schools?id=in.(%s,%s)" % (SCHOOL_OPEN, SCHOOL_HELD), "schools")

    # ── the proof ───────────────────────────────────────────────────────
    left = []
    for table, filt in (("classes", "id=in.(%s)" % ids),
                        ("academic_years", "id=in.(%s,%s)" % (YEAR_OPEN, YEAR_HELD)),
                        ("schools", "id=in.(%s,%s)" % (SCHOOL_OPEN, SCHOOL_HELD))):
        st, rows = api("GET", "/rest/v1/%s?%s&select=id" % (table, filt))
        if isinstance(rows, list) and rows:
            left.append("%s: %d" % (table, len(rows)))
    for email in EMAILS:
        if find_user(email):
            left.append("auth user " + email)

    if problems or left:
        print("⚠️  teardown did NOT finish")
        for p in problems:
            print("     refused: " + p)
        for l in left:
            print("     survives: " + l)
        raise SystemExit(1)
    print("torn down — nothing of f3310000- survives on TEST")


def show():
    """⚠️ `in.(...)` NOT `like.` — `classes.id` is a uuid, and PostgREST hands
    `like` straight to Postgres as `uuid ~~ unknown`, which has no operator and
    comes back as a 404 that reads like a missing route."""
    st, rows = api("GET", "/rest/v1/classes?id=in.(%s)"
                          "&select=id,name,key_stage,year_group,tier,"
                          "science_pathway,science_subject,tier_pathway_source,"
                          "auto_assignments&order=name"
                   % ",".join(c[0] for c in CLASSES))
    if not isinstance(rows, list):
        print(st, rows)
        return
    for r in rows:
        print("  %-9s %-4s Y%-2s %-11s %-9s %-10s src=%-5s auto=%s"
              % (r["name"], r["key_stage"], r["year_group"],
                 r["tier"] or "-", r["science_pathway"] or "-",
                 r["science_subject"] or "-",
                 r["tier_pathway_source"] or "-",
                 r["auto_assignments"]))


if __name__ == "__main__":
    arg = sys.argv[1] if len(sys.argv) > 1 else "--show"
    {"--seed": seed, "--teardown": teardown, "--show": show,
     "--clear-work": clear_work}.get(arg, show)()
