"""week_truth_fixture.py — the throwaway TEST world SPEC-A's walk runs in.

⚠️ THIS IS NOT A GATE. It seeds and it tears down; `week_truth_drive.py` does
the proving. Modelled on `mrb331_fixture.py` — same `api()`/`upsert()`/
`ensure_user()` primitives (imported, not retyped), same "every id begins
with one prefix so a stray row is identifiable at a glance" discipline, same
teardown-by-snapshotted-id-list.

Every id here begins `f3530000-` (unused by any other fixture in the repo —
checked against `f3260000-` and `f3310000-`, the other two). No real school,
teacher or child is touched, and nothing here is TEST's Rainford data.

    MRB_WEEK_TRUTH_PASSWORD=<pw> python3 week_truth_fixture.py --seed
    MRB_WEEK_TRUTH_PASSWORD=<pw> python3 week_truth_fixture.py --teardown
    MRB_WEEK_TRUTH_PASSWORD=<pw> python3 week_truth_fixture.py --show

⚠️ WHY A WORLD OF ITS OWN, not MRB-331's. MRB-331's school is seeded against
"the working year" computed from TODAY — correct for a drive run on the day
it is written, wrong for SPEC-A, which needs the WEEKS THEMSELVES (4, 5, 6 of
a named year) to sit at fixed calendar dates no matter what day this runs on,
so the frozen clocks in `week_truth_drive.py` land where the spec says they
do. So this fixture's academic year is pinned to literal dates
(2026-09-01 → 2027-08-31), never derived from `date.today()`.
"""

import os
import sys
import uuid

REPO = os.path.dirname(os.path.abspath(__file__))
os.chdir(REPO)
sys.path.insert(0, REPO)

import mrb331_fixture as FX  # noqa: E402  (after chdir, deliberately)

P = "f3530000-0000-0000-0000-0000000000"

# ⚠️ EVERY NAMED CONSTANT BELOW IS `P` PLUS EXACTLY TWO HEX CHARS, AND THAT
# IS NOT COSMETIC — `P` is 34 characters (an otherwise-valid UUID's first
# four groups plus ten zeros of the fifth), so anything appended must be
# EXACTLY two characters or the result is not a UUID at all and every
# insert using it fails a type cast. A bulk list (pupils, submissions,
# questions, attempts) cannot fit inside two hex characters' worth of
# values keeping a readable scheme, so those use `wtid()` below instead —
# a deterministic uuid5 keyed by a readable name, always a real UUID by
# construction, and IDEMPOTENT (the same name always makes the same id, so
# re-running `--seed` upserts the same rows rather than duplicating them).
_NS = uuid.uuid5(uuid.NAMESPACE_URL, "https://mrbadmus.com/x-week-truth")


def wtid(name):
    return str(uuid.uuid5(_NS, name))

SCHOOL = P + "01"
YEAR = P + "11"          # 2026-09-01 → 2027-08-31, pinned — see module doc

# ── the three classes ────────────────────────────────────────────────────
C_PH1 = P + "21"      # 10h/Ph1 — the live defect, 17 pupils
C_SC1 = P + "22"      # 8r/Sc1  — MRB-335's own shape, 2 pupils
C_ONE = P + "23"      # 9r/Sc2  — exactly one set ever, 3 pupils

CLASSES = [
    # (id, name, key_stage, year_group)
    (C_PH1, "10h/Ph1", "KS4", 10),
    (C_SC1, "8r/Sc1", "KS3", 8),
    (C_ONE, "9r/Sc2", "KS3", 9),
]

TEACHER_EMAIL = "wt_teacher@throwaway.test"
EMAILS = [TEACHER_EMAIL]

N_PH1, N_SC1, N_ONE = 17, 2, 3
PUPILS = {}   # class_id -> [email, ...], filled by `pupil_emails()`


def pupil_emails():
    if not PUPILS:
        PUPILS[C_PH1] = ["wt_ph1_%02d@throwaway.test" % i for i in range(1, N_PH1 + 1)]
        PUPILS[C_SC1] = ["wt_sc1_%02d@throwaway.test" % i for i in range(1, N_SC1 + 1)]
        PUPILS[C_ONE] = ["wt_one_%02d@throwaway.test" % i for i in range(1, N_ONE + 1)]
        for v in PUPILS.values():
            EMAILS.extend(v)
    return PUPILS


DECK = P + "31"          # one throwaway flashcard deck, for 8r/Sc1's three

# ── assignments ──────────────────────────────────────────────────────────
#
# 10h/Ph1 — byte for byte the live bug report (SPEC-A "The bug" section).
A_COS = P + "41"   # Changes of State — closed, 8/17
A_TEMP = P + "42"  # Temperature — closes Mon 5 Oct 17:00Z
A_DEL1 = P + "43"  # deleted "Energy" row #1 — must stay invisible
A_DEL2 = P + "44"  # deleted "Energy" row #2

# 8r/Sc1 — SPEC-A §56.
A_AUTO1 = P + "51"   # week-1 auto set, due Thu 3 Sep 17:00Z, both done
A_T1 = P + "52"      # teacher set A, due Tue 15 Sep 17:00Z
A_T2 = P + "53"      # teacher set B, due Tue 15 Sep 17:00Z
A_T3 = P + "54"      # teacher set C, due Wed 16 Sep 06:00Z
A_FC1 = P + "55"     # flashcards, due Mon 5 Oct, same day as the MCQ
A_MCQ1 = P + "56"    # MCQ, due Mon 5 Oct 17:00Z, both done
A_FC2 = P + "57"     # flashcards, due Fri 9 Oct
A_FC3 = P + "58"     # flashcards, due Sat 10 Oct
A_OLD = P + "59"     # due 25 Aug — before term start, oldest bucket

# 9r/Sc2 — exactly one set, ever.
A_ONE = P + "61"


def password():
    pw = os.environ.get("MRB_WEEK_TRUTH_PASSWORD", "")
    if not pw:
        raise SystemExit(
            "Set MRB_WEEK_TRUTH_PASSWORD to seed a sign-in-able teacher.\n"
            "  MRB_WEEK_TRUTH_PASSWORD=<something-throwaway> "
            "python3 week_truth_fixture.py --seed")
    return pw


# ⚠️ THIS FIXTURE DOES NOT USE `FX.ensure_user`/`FX.find_user`. TEST's GoTrue
# admin LIST endpoint (`GET /auth/v1/admin/users`, which both of those call)
# answered 500 "Database error finding users" on every attempt, 4 Oct 2026 —
# a TEST-side fault, not this fixture's; single-user creation, single-user
# GET-by-id and ordinary PostgREST reads/writes all work. So user creation
# here never lists first (this world is seeded exactly once, into nothing),
# and every created id is written to `MANIFEST` immediately and persisted to
# disk — the SNAPSHOTTED id list `teardown()` deletes by, which is the
# correct shape for a teardown regardless of whether the admin listing ever
# comes back.
MANIFEST_PATH = os.path.join(REPO, ".week_truth_fixture_ids.json")


def create_user(email, pw):
    st, d = FX.api("POST", "/auth/v1/admin/users",
                    {"email": email, "password": pw, "email_confirm": True})
    if st != 200:
        raise SystemExit("create %s failed %s: %s" % (email, st, d))
    return d["id"]


def save_manifest(emails_to_ids):
    import json
    with open(MANIFEST_PATH, "w", encoding="utf-8") as fh:
        json.dump(emails_to_ids, fh, indent=2)


def load_manifest():
    import json
    if not os.path.exists(MANIFEST_PATH):
        return {}
    with open(MANIFEST_PATH, encoding="utf-8") as fh:
        return json.load(fh)


def seed():
    pw = password()
    emails = pupil_emails()
    manifest = {}   # email -> auth user id, written to disk as we go

    FX.upsert("schools", [{"id": SCHOOL, "name": "X Week Truth School",
                            "code": "XWEEKTRUTH", "assignments_open_from": None}])
    FX.upsert("academic_years", [{"id": YEAR, "school_id": SCHOOL,
                                   "name": "2026-27", "start_date": "2026-09-01",
                                   "end_date": "2027-08-31"}])
    FX.upsert("classes", [
        {"id": cid, "school_id": SCHOOL, "academic_year_id": YEAR, "name": name,
         "key_stage": ks, "year_group": yg, "auto_assignments": False}
        for (cid, name, ks, yg) in CLASSES
    ])

    teacher = create_user(TEACHER_EMAIL, pw)
    manifest[TEACHER_EMAIL] = teacher
    save_manifest(manifest)
    FX.upsert("profiles", [
        # ⚠️ `tier`/`science_pathway` default to 'higher'/'combined' at the
        # COLUMN level, and `profiles_tier_only_ks4_check` refuses either
        # being non-null without `key_stage = 'KS4'` — a check that bites a
        # profile with no `key_stage` at all (every pupil and teacher here)
        # unless the payload says NULL explicitly, which overrides the
        # default; omitting the key does not.
        {"id": teacher, "role": "teacher", "school_id": SCHOOL,
         "first_name": "Wendy", "last_name": "Teachlock",
         "tier": None, "science_pathway": None},
    ])
    FX.upsert("class_teachers", [
        {"id": P + "7" + str(i), "class_id": cid, "teacher_id": teacher,
         "role": "subject_teacher",
         "subject_id": FX.SUBJECT_PHYSICS if cid == C_PH1 else FX.SUBJECT_SCIENCE}
        for i, (cid, *_rest) in enumerate(CLASSES)
    ], on_conflict="id")

    pupil_ids = {}
    for cid, cemails in emails.items():
        ids = []
        for em in cemails:
            uid = create_user(em, pw)
            manifest[em] = uid
            save_manifest(manifest)   # after EVERY create — a crash mid-seed
            ids.append(uid)           # still leaves a complete snapshot
        pupil_ids[cid] = ids

    FX.upsert("profiles", [
        {"id": uid, "role": "student", "school_id": SCHOOL,
         "first_name": "Pupil", "last_name": em.split("@")[0],
         "tier": None, "science_pathway": None}
        for cid, ids in pupil_ids.items()
        for uid, em in zip(ids, emails[cid])
    ])
    # Every ROW needs its own id (not one per class) — built directly, never
    # the one-id-per-class mistake that would collapse a class's whole
    # roster onto a single upserted row.
    rows = []
    for cid, ids in pupil_ids.items():
        for uid in ids:
            rows.append({"id": wtid("class_members:%s:%s" % (cid, uid)),
                         "class_id": cid, "student_id": uid,
                         "joined_via": "admin_added"})
    FX.upsert("class_members", rows, on_conflict="id")

    FX.upsert("flashcard_decks", [
        {"id": DECK, "school_id": SCHOOL, "created_by": teacher,
         "title": "X Week Truth deck", "key_stage": "KS3", "subject": "biology",
         "source_kind": "typed", "status": "ready", "shared_with_school": True,
         "card_count": 10},
    ])

    def a(id_, cid, title, topic, subtopic, due, release, week=None,
          source="teacher", kind="mcq_set", deleted=False, deck=None,
          subject_id=None):
        row = {
            "id": id_, "class_id": cid, "teacher_id": teacher,
            "subject_id": subject_id or (FX.SUBJECT_PHYSICS if cid == C_PH1 else FX.SUBJECT_SCIENCE),
            "topic": topic, "subtopic": subtopic, "title": title,
            "quiz_type": "flashcards" if kind == "flashcards" else "subtopic_quiz",
            "due_at": due, "release_at": release,
            "source": source, "auto_generated": source == "auto",
            "academic_week": week, "set_by": teacher if source == "teacher" else None,
            "school_id": SCHOOL, "kind": kind,
            # ⚠️ EVERY ROW IN ONE BULK UPSERT MUST CARRY THE SAME KEYS —
            # PostgREST refuses a batch whose objects disagree on their key
            # set ("All object keys must match", PGRST102) — so the
            # flashcard-only and deleted-only columns are always present,
            # NULL where this row is neither.
            "deck_id": (deck or DECK) if kind == "flashcards" else None,
            "flashcard_mode": "review" if kind == "flashcards" else None,
            "completion_rule": "secure" if kind == "flashcards" else None,
            "deleted_at": due if deleted else None,
            "deleted_by": teacher if deleted else None,
        }
        return row

    FX.upsert("assignments", [
        a(A_COS, C_PH1, "Particle Model of Matter · Changes of State",
          "Particle Model of Matter", "Changes of State",
          due="2026-09-28T08:00:00+00:00", release="2026-09-20T09:00:00+00:00", week=4),
        a(A_TEMP, C_PH1,
          "Particle Model of Matter · Temperature Changes and Specific Heat Capacity",
          "Particle Model of Matter", "Temperature Changes and Specific Heat Capacity",
          due="2026-10-05T17:00:00+00:00", release="2026-09-28T14:45:00+00:00", week=5),
        a(A_DEL1, C_PH1, "Energy · Energy stores (deleted)", "Energy", "Energy stores",
          due="2026-09-21T08:00:00+00:00", release="2026-09-14T09:00:00+00:00", week=3,
          deleted=True),
        a(A_DEL2, C_PH1, "Energy · Energy transfers (deleted)", "Energy", "Energy transfers",
          due="2026-09-14T08:00:00+00:00", release="2026-09-07T09:00:00+00:00", week=2,
          deleted=True),

        a(A_AUTO1, C_SC1, "Week 1 auto set", "Cells", "Cell structure",
          due="2026-09-03T17:00:00+00:00", release=None, week=1, source="auto"),
        a(A_T1, C_SC1, "Teacher set A", "Cells", "Microscopy",
          due="2026-09-15T17:00:00+00:00", release="2026-09-08T18:42:00+00:00"),
        a(A_T2, C_SC1, "Teacher set B", "Cells", "Specialised cells",
          due="2026-09-15T17:00:00+00:00", release="2026-09-08T18:42:00+00:00"),
        a(A_T3, C_SC1, "Teacher set C", "Cells", "Diffusion",
          due="2026-09-16T06:00:00+00:00", release="2026-09-08T18:42:00+00:00"),
        a(A_FC1, C_SC1, "Flashcards — due with the MCQ", "Cells", "Key terms",
          due="2026-10-05T00:00:00+00:00", release="2026-09-28T00:00:00+00:00",
          kind="flashcards"),
        a(A_MCQ1, C_SC1, "MCQ — due Mon 5 Oct", "Cells", "Osmosis",
          due="2026-10-05T17:00:00+00:00", release="2026-09-28T17:21:00+00:00"),
        a(A_FC2, C_SC1, "Flashcards — due Fri 9 Oct", "Cells", "More key terms",
          due="2026-10-09T17:00:00+00:00", release="2026-09-28T00:00:00+00:00",
          kind="flashcards"),
        a(A_FC3, C_SC1, "Flashcards — due Sat 10 Oct", "Cells", "Even more key terms",
          due="2026-10-10T17:00:00+00:00", release="2026-09-28T00:00:00+00:00",
          kind="flashcards"),
        a(A_OLD, C_SC1, "Old set, before term start", "Cells", "Cell organelles",
          due="2026-08-25T17:00:00+00:00", release="2026-08-18T09:00:00+00:00"),

        a(A_ONE, C_ONE, "The only set this class has ever had", "Forces", "Speed",
          due="2026-09-22T17:00:00+00:00", release="2026-09-15T09:00:00+00:00", week=3),
    ])

    # ── submissions ──────────────────────────────────────────────────────
    ph1 = pupil_ids[C_PH1]
    sc1 = pupil_ids[C_SC1]
    one = pupil_ids[C_ONE]

    def sub(id_, aid, sid, score, mx, completed, late=False, status="complete"):
        return {"id": id_, "assignment_id": aid, "student_id": sid,
                "score": score, "max_score": mx, "status": status,
                "submitted_at": completed, "completed_at": completed,
                "started_at": completed, "is_late": late}

    subs = []
    n = 0

    def nid():
        nonlocal n
        n += 1
        return wtid("assignment_submissions:%d" % n)

    # Changes of State — 8 of 17, out of the paper's own 8 questions
    # (`mkq`'s default), a believable spread of scores, all handed in
    # comfortably before the Mon 28 Sep 08:00Z deadline.
    cos_scores = [7, 6, 5, 7, 5, 6, 8, 4]
    cos_completed = ["2026-09-23T15:00:00+00:00", "2026-09-23T19:30:00+00:00",
                      "2026-09-24T08:15:00+00:00", "2026-09-24T17:45:00+00:00",
                      "2026-09-25T12:00:00+00:00", "2026-09-26T09:30:00+00:00",
                      "2026-09-26T20:00:00+00:00", "2026-09-27T21:10:00+00:00"]
    for i, sc in enumerate(cos_scores):
        subs.append(sub(nid(), A_COS, ph1[i], sc, 8, cos_completed[i], late=False))
    # Temperature — 3 of 17, still mid-sitting at the "mon" clock (18:00 BST
    # deadline), closed by "tue".
    temp_scores = [6, 5, 7]
    temp_completed = ["2026-10-02T16:00:00+00:00", "2026-10-03T11:00:00+00:00",
                        "2026-10-04T20:00:00+00:00"]
    for i, sc in enumerate(temp_scores):
        subs.append(sub(nid(), A_TEMP, ph1[i], sc, 8, temp_completed[i]))

    # 8r/Sc1.
    subs.append(sub(nid(), A_AUTO1, sc1[0], 6, 8, "2026-09-02T17:00:00+00:00"))
    subs.append(sub(nid(), A_AUTO1, sc1[1], 7, 8, "2026-09-02T18:00:00+00:00"))
    subs.append(sub(nid(), A_T1, sc1[0], 5, 8, "2026-09-14T17:00:00+00:00"))
    subs.append(sub(nid(), A_T2, sc1[1], 6, 8, "2026-09-14T18:00:00+00:00"))
    subs.append(sub(nid(), A_T3, sc1[0], 8, 8, "2026-09-15T20:00:00+00:00"))
    subs.append(sub(nid(), A_MCQ1, sc1[0], 9, 10, "2026-10-04T17:00:00+00:00"))
    subs.append(sub(nid(), A_MCQ1, sc1[1], 4, 10, "2026-10-04T18:00:00+00:00"))

    # 9r/Sc2 — the one set, nobody has done it yet (an ordinary open state).
    FX.upsert("assignment_submissions", subs, on_conflict="id")

    # ── per-question questions + attempts, for the two papers the walk
    #    checks the weakest-two-questions bars and the SQL cross-check on
    #    (SPEC-A §57) ────────────────────────────────────────────────────
    def mkq(aid, letter, n_q=8):
        # ⚠️ `one_pool_per_assignment` (MRB-288/MRB-335) requires `band` SET
        # and `rung` NULL on every `assignment_questions` row — the DB-level
        # proof that a set's questions came from a bank pool, not the
        # authored ladder. `rung` only belongs on the ladder's own mirror.
        return [{"id": wtid("assignment_questions:%s:%d" % (letter, i)),
                 "assignment_id": aid, "position": i,
                 "source_ref": "physics/particle-model/changes-of-state#q%d" % i,
                 "band": ["easier", "standard", "standard", "harder"][i % 4]}
                for i in range(n_q)]

    FX.upsert("assignment_questions", mkq(A_COS, "cos"), on_conflict="id")
    FX.upsert("assignment_questions", mkq(A_TEMP, "temp"), on_conflict="id")

    # Attempts: for Changes of State, make Q3 and Q6 the clear weakest (most
    # wrong), everything else mostly right — so the reteach card's own two
    # bars are provably "Q3"/"Q6" and the SQL in RESULT-A.md can recompute
    # the same two percentages from these very rows.
    cos_wrong = {3: [0, 1, 2, 3, 5], 6: [0, 1, 2, 4, 6, 7]}  # q index -> wrong pupil indices
    attempts = []
    sub_by_pupil_cos = {}
    for i, s in enumerate(subs):
        if s["assignment_id"] == A_COS:
            sub_by_pupil_cos[s["student_id"]] = s["id"]
    an = 0

    def aid_():
        nonlocal an
        an += 1
        return wtid("assignment_question_attempts:%d" % an)

    for i, pid in enumerate(ph1[:len(cos_scores)]):
        subid = sub_by_pupil_cos[pid]
        for q in range(8):
            wrong = i in cos_wrong.get(q, [])
            attempts.append({
                "id": aid_(), "submission_id": subid, "question_index": q,
                "question_ref": "cos-q%d" % q, "question_text": "Changes of State Q%d" % (q + 1),
                "is_correct": (not wrong), "rung": ["recall", "apply", "explain", "produce"][q % 4],
            })
    FX.upsert("assignment_question_attempts", attempts, on_conflict="id")

    print("seeded:")
    print("  school    %s" % SCHOOL)
    print("  year      2026-09-01 → 2027-08-31 (%s)" % YEAR)
    print("  classes   10h/Ph1 (%d pupils), 8r/Sc1 (%d), 9r/Sc2 (%d)"
          % (N_PH1, N_SC1, N_ONE))
    print("  teacher   %s  %s" % (TEACHER_EMAIL, teacher))


def teardown():
    pupil_emails()
    manifest = load_manifest()
    if not manifest:
        print("⚠️  no %s — nothing to tear down by, or seed never "
              "ran (or ran before this file could write one)" % MANIFEST_PATH)
    ids = ",".join(c[0] for c in CLASSES)
    problems = []

    def uid_of(email):
        # The snapshotted list, never a predicate — see the module note on
        # `MANIFEST_PATH` for why this fixture cannot use the admin LIST
        # endpoint `FX.find_user` calls.
        return manifest.get(email)

    def rm(path, what):
        st, d = FX.api("DELETE", "/rest/v1/" + path)
        if st not in (200, 204):
            problems.append("%s → %s %s" % (what, st, str(d)[:160]))

    st, mine = FX.api("GET", "/rest/v1/assignments?class_id=in.(%s)&select=id" % ids)
    if isinstance(mine, list) and mine:
        aids = ",".join(a["id"] for a in mine)
        st, subs = FX.api("GET", "/rest/v1/assignment_submissions"
                                 "?assignment_id=in.(%s)&select=id" % aids)
        if isinstance(subs, list) and subs:
            sids = ",".join(s["id"] for s in subs)
            rm("assignment_question_attempts?submission_id=in.(%s)" % sids, "attempts")
            rm("submission_feedback?submission_id=in.(%s)" % sids, "feedback")
            rm("assignment_submissions?id=in.(%s)" % sids, "submissions")
        rm("student_notifications?assignment_id=in.(%s)" % aids, "reminders")
        rm("assignment_questions?assignment_id=in.(%s)" % aids, "questions")
        rm("assignments?id=in.(%s)" % aids, "assignments")
        # deleted rows too — `?select=id` above only returns non-deleted by
        # RLS/default view in some setups; be explicit.
    st, deleted_rows = FX.api("GET", "/rest/v1/assignments?class_id=in.(%s)"
                                     "&deleted_at=not.is.null&select=id" % ids)
    if isinstance(deleted_rows, list) and deleted_rows:
        daids = ",".join(a["id"] for a in deleted_rows)
        rm("assignment_questions?assignment_id=in.(%s)" % daids, "deleted-row questions")
        rm("assignments?id=in.(%s)" % daids, "deleted assignments")

    for table in ("student_notifications", "class_members", "class_teachers"):
        rm("%s?class_id=in.(%s)" % (table, ids), table)
    rm("classes?id=in.(%s)" % ids, "classes")
    rm("flashcard_decks?id=eq.%s" % DECK, "flashcard deck")
    rm("academic_years?id=eq.%s" % YEAR, "academic year")

    for email in EMAILS:
        uid = uid_of(email)
        if uid:
            rm("audit_log?actor_id=eq." + uid, "audit rows for " + email)
    for email in EMAILS:
        uid = uid_of(email)
        if uid:
            rm("profiles?id=eq." + uid, "profile for " + email)
            st, d = FX.api("DELETE", "/auth/v1/admin/users/" + uid)
            if st not in (200, 204):
                problems.append("auth user %s → %s" % (email, st))

    st, strays = FX.api("GET", "/rest/v1/profiles?school_id=eq.%s&select=id,username" % SCHOOL)
    if isinstance(strays, list) and strays:
        for row in strays:
            FX.api("PATCH", "/rest/v1/profiles?id=eq." + row["id"], {"school_id": None})
        print("     detached %d profile(s) this file did not create: %s"
              % (len(strays), ", ".join(r.get("username") or r["id"][:8] for r in strays)))

    rm("schools?id=eq.%s" % SCHOOL, "school")

    left = []
    for table, filt in (("classes", "id=in.(%s)" % ids),
                        ("academic_years", "id=eq.%s" % YEAR),
                        ("schools", "id=eq.%s" % SCHOOL)):
        st, rows = FX.api("GET", "/rest/v1/%s?%s&select=id" % (table, filt))
        if isinstance(rows, list) and rows:
            left.append("%s: %d" % (table, len(rows)))
    for email in EMAILS:
        uid = uid_of(email)
        if uid:
            # Single GET-by-id, proven to work on TEST even while the admin
            # LIST endpoint 500s (see the module note on `MANIFEST_PATH`).
            st, _d = FX.api("GET", "/auth/v1/admin/users/" + uid)
            if st == 200:
                left.append("auth user " + email)

    if problems or left:
        print("⚠️  teardown did NOT finish")
        for p in problems:
            print("     refused: " + p)
        for l in left:
            print("     survives: " + l)
        raise SystemExit(1)
    if os.path.exists(MANIFEST_PATH):
        os.remove(MANIFEST_PATH)
    print("torn down — nothing of f3530000- survives on TEST")


def show():
    ids = ",".join(c[0] for c in CLASSES)
    st, rows = FX.api("GET", "/rest/v1/classes?id=in.(%s)&select=id,name,tier,"
                             "science_pathway,science_subject" % ids)
    print(rows)
    st, a = FX.api("GET", "/rest/v1/assignments?class_id=in.(%s)"
                          "&select=id,title,due_at,release_at,deleted_at&order=due_at" % ids)
    print(a)


if __name__ == "__main__":
    if "--seed" in sys.argv:
        seed()
    elif "--teardown" in sys.argv:
        teardown()
    elif "--show" in sys.argv:
        show()
    else:
        raise SystemExit(__doc__)
