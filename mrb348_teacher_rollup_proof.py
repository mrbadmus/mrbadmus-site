#!/usr/bin/env python3
"""
mrb348_teacher_rollup_proof.py — `public.teacher_class_rollup_v2` returns
exactly what the browser would have computed for itself, for every value the
six teacher screens draw about a class they are not focused on.

⊕ Mide's 23 Sep 2026 ruling ("results are live") points this at
`teacher_class_rollup_v2`, a NEW function beside the untouched
`teacher_class_rollup` — production DDL could not change in that run, so the
JS ships behind a new RPC name rather than an edit to the old one. `marked`
now means RELEASED, not "the deadline has passed"; `closed` is the new column
carrying the old test; `in_week` widens to include an open paper regardless
of its due date; `on_time_week` is new. See `paper_state()` below and
`supabase/migrations/20260924010000_rollup_live_results.sql`.

    MRB_TEST_TEACHER_PASSWORD=… python3 mrb348_teacher_rollup_proof.py
    MRB_TEST_TEACHER_PASSWORD=… python3 mrb348_teacher_rollup_proof.py --fixture

THE METHOD, and it is round two's (docs/mrb348/teacher-aggregate.md §3)

  1. Replay `loadClassMatrices()`'s EXACT PostgREST reads, signed in as a real
     user under real RLS **with the anon key** — never the service-role key,
     which bypasses RLS and would prove nothing about what a reader may see.
  2. Translate `pickFirstAttempts`, `buildPapers`, `cellOf`, `buildMatrix`,
     `buildRoster` and `buildClassEntry` line for line, including their string
     comparisons on timestamps, which is what the JavaScript actually does.
  3. Ask the RPC, as the SAME user, in the same instant, with the same clock
     and the same teaching-week windows.
  4. Derive from the RPC's answer exactly what `matrixFromRollup()` in
     `shared/teacher-live.js` derives from it.
  5. Diff, cell by cell.

⚠️ THE TWO CLOCKS ARE PASSED, NOT ASSUMED. `p_now` and `p_windows` are the
browser's own `Date.now()` and `computeWeekWindow()`, sent to the function, so
the two sides cannot disagree about which deadlines have passed or which week
a paper is in. `computeWeekWindow` is translated here rather than re-invented
— including MRB-330's Sunday rule — and the translation is asserted against
the JavaScript's own arithmetic in `week_window()`'s docstring.

⚠️ TEST ONLY. The project ref is proven out of the service-role JWT's own
`ref` claim before the fixture is built, never read off a label; the script
refuses on the production ref. The service-role key is used for NOTHING but
building and tearing down the adversarial fixture — every measured read on
both sides is made as the signed-in user with the anon key.
"""
from __future__ import annotations

import argparse
import base64
import json
import os
import re
import ssl
import sys
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timedelta, timezone

REPO = os.path.dirname(os.path.abspath(__file__))
os.chdir(REPO)

TEST_REF = "qeppkiswvclkkwbxmlok"
PROD_REF = "urklkrwevjtlfbwnipjn"
URL = "https://%s.supabase.co" % TEST_REF
CTX = ssl.create_default_context(cafile="/etc/ssl/cert.pem")
BACKEND_ENV = os.environ.get(
    "MRB_BACKEND", "/Users/midebadmus/Documents/GitHub/mrbadmus---backend") + "/.env"

READERS = [
    ("mide.badmus@test-rainford.local", "teacher, the realistic 5-class world"),
    ("hz_amy@test.mrbadmus", "teacher, one class"),
    ("hz_rich@test.mrbadmus", "HOD — sees every class in the school but only "
                              "their own department's work"),
]

MAX_SAFE_INTEGER = 9007199254740991


# ── credentials ────────────────────────────────────────────────────────────

def read_env(path):
    out = {}
    with open(path) as fh:
        for line in fh:
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                k, v = line.split("=", 1)
                out[k] = v.strip().strip('"').strip("'")
    return out


def jwt_ref(token):
    """The project ref out of the key's own payload. Never off a label."""
    p = token.split(".")[1]
    p += "=" * (-len(p) % 4)
    return json.loads(base64.urlsafe_b64decode(p)).get("ref")


def anon_key():
    """⚠️ The TEST anon key, not the first one in the file — config.js carries
    both projects' and production's comes first."""
    src = open("shared/config.js", encoding="utf-8").read()
    return re.search(r"'(eyJ[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+)'",
                     src[src.index("const TEST"):]).group(1)


def service_key():
    env = read_env(BACKEND_ENV)
    srk = env.get("SUPABASE_SERVICE_ROLE_KEY", "")
    ref = jwt_ref(srk)
    if ref == PROD_REF:
        raise SystemExit("REFUSING: that credential is PRODUCTION. TEST only.")
    if ref != TEST_REF:
        raise SystemExit("REFUSING: ref %r is neither TEST nor known." % ref)
    if env.get("SUPABASE_URL", "").split("//")[-1].split(".")[0] != ref:
        raise SystemExit("REFUSING: the URL's ref and the key's ref disagree.")
    return srk, ref


def sign_in(email, key, pw):
    req = urllib.request.Request(
        URL + "/auth/v1/token?grant_type=password",
        data=json.dumps({"email": email, "password": pw}).encode(),
        headers={"apikey": key, "Content-Type": "application/json"},
        method="POST")
    return json.load(urllib.request.urlopen(req, timeout=30, context=CTX))


def rest(path, key, token, method="GET", body=None, prefer=None):
    hdr = {"apikey": key, "Authorization": "Bearer " + token,
           "Content-Type": "application/json"}
    if prefer:
        hdr["Prefer"] = prefer
    data = json.dumps(body).encode() if body is not None else None
    req = urllib.request.Request(URL + "/rest/v1/" + path, data=data,
                                 headers=hdr, method=method)
    try:
        r = urllib.request.urlopen(req, timeout=60, context=CTX)
        raw = r.read().decode()
        return json.loads(raw) if raw.strip() else []
    except urllib.error.HTTPError as e:
        raise SystemExit("REST %s %s -> %s %s"
                         % (method, path[:120], e.code, e.read().decode()[:400]))


# ── the JavaScript, translated ─────────────────────────────────────────────

def iso_now():
    """`new Date(now).toISOString()` — millisecond precision, trailing Z."""
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.") \
        + "%03dZ" % (datetime.now(timezone.utc).microsecond // 1000)


def to_iso(dt_local):
    u = dt_local.astimezone(timezone.utc)
    return u.strftime("%Y-%m-%dT%H:%M:%S.") + "%03dZ" % (u.microsecond // 1000)


def week_window(anchor):
    """`computeWeekWindow(assignmentDayOfWeek)` from shared/teacher-data.js.

    Browser-LOCAL time, the class's own anchor day, and MRB-330's rule that a
    Sunday belongs to the week that is coming. JS `getDay()` is Sun=0..Sat=6;
    Python's `weekday()` is Mon=0..Sun=6, so `(weekday() + 1) % 7` is the
    translation and nothing else changes.
    """
    fallback = anchor is None
    anchor_day = 1 if fallback else anchor
    now = datetime.now()
    js_day = (now.weekday() + 1) % 7
    today = 1 if js_day == 0 else js_day
    days_since = (today - anchor_day + 7) % 7
    start = now
    if js_day == 0:
        start = start + timedelta(days=1)
    start = start - timedelta(days=days_since)
    start = start.replace(hour=0, minute=0, second=0, microsecond=0)
    end = start + timedelta(days=7)
    return {"start_at": to_iso(start.astimezone()),
            "end_at": to_iso(end.astimezone())}


def pick_first_attempts(subs):
    """`pickFirstAttempts()` — lower `attempts` wins; tie → earlier
    `submitted_at`; NULL attempts worst; NULL stamp worst within a tie. The
    stamp comparison is on the RAW STRINGS, as the JS does it."""
    by = {}
    for s in subs:
        if not s.get("assignment_id") or not s.get("student_id"):
            continue
        k = s["assignment_id"] + ":" + s["student_id"]
        cur = by.get(k)
        if cur is None:
            by[k] = s
            continue
        ca = MAX_SAFE_INTEGER if cur.get("attempts") is None else cur["attempts"]
        na = MAX_SAFE_INTEGER if s.get("attempts") is None else s["attempts"]
        if na < ca:
            by[k] = s
            continue
        if na == ca:
            cts = cur.get("submitted_at") or "￿"
            nts = s.get("submitted_at") or "￿"
            if nts < cts:
                by[k] = s
    return by


def cell_of(s, due_at, kind=None):
    """`cellOf(s, paper)` — the one cell both the rows and the columns read.

    ⊕ MRB-351 landing, stream B — `kind` is the paper's `assignments.kind`.
    A flashcard cell (`kind == "flashcards"`) is a cell in every other
    respect (stamp, late) but is NEVER graded: its score/max_score is a
    completion stamp (N/N), not a mark. Exactly `cellOf`'s own
    `graded = !(paper && paper.kind === "flashcards")` in
    shared/teacher-live.js, and the SQL twin in
    20260927100000_mrb351_rollup_v2_live_results_kinds.sql's `cells` CTE.
    """
    if not s:
        return None
    stamp = s.get("completed_at") or s.get("submitted_at") or None
    done = bool(stamp) or s.get("status") == "complete"
    if not done:
        return None
    score = mx = pct = None
    if kind != "flashcards" and s.get("score") is not None \
            and s.get("max_score") is not None and s["max_score"] > 0:
        score, mx = s["score"], s["max_score"]
        pct = js_round(score / mx * 100)
    late = None
    if s.get("is_late") is not None:
        late = s["is_late"] is True
    elif stamp and due_at:
        late = stamp > due_at            # raw strings, as the JS compares them
    return {"stamp": stamp, "score": score, "max": mx, "pct": pct, "late": late}


def activity_at(s):
    """`activity[p]` in `buildMatrix` (shared/teacher-live.js, Mide's 25 Sep
    2026 ruling, experience run item 7) — wider than `cellOf`'s `stamp`. A
    first-attempt row that IS a cell contributes its own stamp; one that
    exists but is not (yet) a cell — `started_at` set, no `completed_at`
    yet — contributes `started_at`, because a pupil mid-way through an open
    paper was otherwise invisible to "last active". Kind-independent, same
    as the SQL twin's `activity` CTE in
    20260927100000_mrb351_rollup_v2_live_results_kinds.sql (added there in
    the Opus review, 27 Sep 2026, alongside this python translation)."""
    if not s:
        return None
    stamp = s.get("completed_at") or s.get("submitted_at") or None
    done = bool(stamp) or s.get("status") == "complete"
    return stamp if done else s.get("started_at")


def js_round(x):
    """`Math.round` — half AWAY FROM ZERO, not Python's banker's rounding."""
    import math
    return int(math.floor(x + 0.5)) if x >= 0 else -int(math.floor(-x + 0.5))


# ── the read, replayed ─────────────────────────────────────────────────────

def in_list(ids):
    return "in.(%s)" % ",".join(ids)


def load_class_matrices(key, token, ids, with_subs=True):
    """`loadClassMatrices(classIds)`, read for read."""
    links = rest("class_teachers?select=" + urllib.parse.quote(
        "class_id,subject_id,subject:subject_id(id,name),"
        "class:class_id(id,name,key_stage,year_group,tier,science_pathway,"
        "assignment_day_of_week,deleted_at,academic_year_id)")
        + "&class_id=" + in_list(ids) + "&deleted_at=is.null&ended_at=is.null",
        key, token)
    members = rest("class_members?select=" + urllib.parse.quote(
        "class_id,student_id,joined_at,left_at,"
        "student:student_id(id,first_name,last_name,avatar_url,deleted_at)")
        + "&class_id=" + in_list(ids) + "&deleted_at=is.null", key, token)
    assigns = rest("assignments?select=" + urllib.parse.quote(
        "id,class_id,title,due_at,release_at,source,set_by,set_tier,scope_kind,"
        "scope_ref,set_subject:subject,paper,created_at,academic_week,subject_id,"
        "subject:subject_id(id,name),kind")
        + "&class_id=" + in_list(ids) + "&deleted_at=is.null", key, token)

    by_class = {}
    for row in links:
        k = row.get("class")
        if not k or k.get("deleted_at"):
            continue
        by_class.setdefault(k["id"], {"klass": k})
    missing = [i for i in ids if i not in by_class]
    if missing:
        for k in rest("classes?select=" + urllib.parse.quote(
                "id,name,key_stage,year_group,tier,science_pathway,"
                "assignment_day_of_week,deleted_at,academic_year_id,school_id")
                + "&id=" + in_list(missing) + "&deleted_at=is.null", key, token):
            if not k.get("deleted_at"):
                by_class.setdefault(k["id"], {"klass": k})

    subs = []
    aids = [a["id"] for a in assigns if a["class_id"] in by_class]
    if with_subs and aids:
        subs = rest("assignment_submissions?select=" + urllib.parse.quote(
            "id,assignment_id,student_id,score,max_score,submitted_at,"
            "completed_at,started_at,status,is_late,attempts,attempt_no")
            + "&assignment_id=" + in_list(aids) + "&deleted_at=is.null",
            key, token)

    # ⊕ Opus review, 27 Sep 2026 — a flashcard sitting is activity even
    # before the deck is finished (no `assignment_submissions` row exists
    # until then). Read directly, under the SAME real RLS as everything else
    # here — `flashcard_sessions_select`'s teacher-of-class branch — never
    # through the SECURITY DEFINER rollup. `class_id` is denormalised onto
    # the table (MRB-351 migration 1), so this needs no join through
    # `assignments` to scope by class. See the last-activity rule in supabase/MRB351-APPLY.md.
    fsess = []
    if with_subs and by_class:
        fsess = rest("flashcard_sessions?select=" + urllib.parse.quote(
            "assignment_id,pupil_id,class_id,last_seen_at")
            + "&class_id=" + in_list(list(by_class.keys())), key, token)

    class_of_assignment = {a["id"]: a["class_id"] for a in assigns}
    first = pick_first_attempts(subs)
    packs = {}
    for cid, e in by_class.items():
        k = e["klass"]
        packs[cid] = {
            "class": k,
            "week": week_window(k.get("assignment_day_of_week")),
            "members": [m for m in members
                        if m["class_id"] == cid and m.get("student")
                        and not m["student"].get("deleted_at")
                        and m.get("left_at") is None],
            "assignments": [a for a in assigns if a["class_id"] == cid],
            "submissions": [s for s in first.values()
                            if class_of_assignment.get(s["assignment_id"]) == cid],
            "flashcard_sessions": [s for s in fsess if s["class_id"] == cid],
        }
    return packs, len(members), len(assigns), len(subs)


# ── what the page derives, from the submissions (today) ────────────────────

def paper_state(a, now_iso):
    """⊕ Mide's 23 Sep 2026 ruling — `marked` IS RELEASED, `closed` IS THE
    DEADLINE TEST `marked` USED TO BE. Translates `buildPapers` in
    shared/teacher-live.js: a NULL `release_at` is released (MRB-336,
    unchanged); `closed` is `due_at IS NOT NULL AND due_at <= now`, exactly
    what `marked` meant before this ruling."""
    release_at = a.get("release_at")
    return {
        "marked": (release_at is None) or (release_at <= now_iso),
        "closed": bool(a.get("due_at")) and not (a["due_at"] > now_iso),
    }


def js_values(pack, now_iso):
    """`buildPapers` + `buildMatrix` + `buildRoster` + `buildClassEntry`, for
    every value a class NOT in focus contributes to a screen."""
    papers = [dict({"id": a["id"], "due_at": a.get("due_at"),
                    "kind": a.get("kind") or "mcq_set"},
                   **paper_state(a, now_iso))
              for a in pack["assignments"]]
    due_of = {p["id"]: p["due_at"] for p in papers}
    members = pack["members"]
    active = set(m["student"]["id"] for m in members)
    w = pack["week"]

    by_student = {}
    for s in pack["submissions"]:
        by_student.setdefault(s["student_id"], {})[s["assignment_id"]] = s

    cols = {}
    for p in papers:
        sub = on = lt = unk = graded = off = 0
        tot = totmax = 0
        for sid, mine in by_student.items():
            c = cell_of(mine.get(p["id"]), p["due_at"], p["kind"])
            if not c:
                continue
            sub += 1
            if sid not in active:
                off += 1
            if c["late"] is True:
                lt += 1
            elif c["late"] is False:
                on += 1
            else:
                unk += 1
            if c["score"] is not None and c["max"]:
                tot += c["score"]
                totmax += c["max"]
                graded += 1
        cols[p["id"]] = {
            "sub": sub, "asked": len(members) + off, "on_time": on, "late": lt,
            "unknown": unk, "marked_n": graded,
            "mean": js_round(tot / totmax * 100) if totmax > 0 else None,
        }

    marked_ids = [p["id"] for p in papers if p["marked"]]

    # ⊕ Opus review, 27 Sep 2026 — a flashcard SITTING is activity even
    # before the deck is finished (no `assignment_submissions` row exists
    # until then; see `activity_at()` and the last-activity rule in supabase/MRB351-APPLY.md). Per pupil,
    # MAX(last_seen_at) over this class's own non-deleted, released
    # flashcard assignments — `pack["assignments"]` is already deleted_at-
    # filtered by `load_class_matrices`, exactly like the SQL's `asg`.
    released_flashcard_ids = {p["id"] for p in papers
                              if p["kind"] == "flashcards" and p["marked"]}
    flashcard_last_seen = {}
    for fs in pack.get("flashcard_sessions", []):
        if fs["assignment_id"] not in released_flashcard_ids:
            continue
        v = fs.get("last_seen_at")
        pid = fs["pupil_id"]
        if v and (pid not in flashcard_last_seen or v > flashcard_last_seen[pid]):
            flashcard_last_seen[pid] = v

    students = {}
    for m in members:
        sid = m["student"]["id"]
        mine = by_student.get(sid, {})
        tot = totmax = 0
        in_week = False
        on_time_week = False
        last = None
        missing_marked = False
        for p in papers:
            s_row = mine.get(p["id"])
            c = cell_of(s_row, p["due_at"], p["kind"])
            # ⊕ Mide's 25 Sep 2026 ruling (experience run, item 7) — ACTIVITY,
            # computed for EVERY first-attempt row, cell or not, BEFORE the
            # `if not c: continue` guard below — an in-progress row
            # (`started_at` set, no cell yet) must still count. See
            # `activity_at()`'s own docstring.
            av = activity_at(s_row)
            if av and (last is None or av > last):
                last = av
            # ⊕ Mide's 23 Sep 2026 ruling, item 2 — `missing_marked` is a
            # CLOSED paper with no cell, not a released one. `p["marked"]`
            # used to BE the closed test; now it means released, so this
            # reads `p["closed"]` instead — unchanged in effect.
            if p["closed"] and not c:
                missing_marked = True
            if not c:
                continue
            # Item 6 — a pupil's average is sum(score)/sum(max) over cells
            # on RELEASED papers. `p["marked"]` IS released now, so this is
            # unchanged text over a changed population.
            if p["marked"] and c["score"] is not None and c["max"]:
                tot += c["score"]
                totmax += c["max"]
            # ⊕ Mide's 23 Sep 2026 ruling, item 5 — "this week's homework" is
            # a paper that is OPEN (released, not yet closed) OR whose
            # due_at falls inside the window; `buildMatrix`'s `inWeekPaper`.
            # A pupil's `in_week` is true only when they have a CELL on one
            # (this test sits after the `if not c: continue` guard, same as
            # the JS). `on_time_week` is the same test plus `late is False`.
            p_open = p["marked"] and not p["closed"]
            in_win = bool(p["due_at"] and p["due_at"] >= w["start_at"]
                          and p["due_at"] < w["end_at"])
            if p_open or in_win:
                in_week = True
                if c["late"] is False:
                    on_time_week = True
        # ⊕ Opus review, 27 Sep 2026 — fold in the flashcard-sitting signal
        # computed above, GREATEST-style (a later flashcard sitting can beat
        # an earlier MCQ completion, or vice versa).
        fc_last = flashcard_last_seen.get(sid)
        if fc_last and (last is None or fc_last > last):
            last = fc_last
        students[sid] = {
            "avg": js_round(tot / totmax * 100) if totmax > 0 else None,
            "in_week": in_week, "on_time_week": on_time_week, "last_at": last,
            "missing_marked": missing_marked,
        }
    return assemble(pack, cols, students, marked_ids, papers)


def assemble(pack, cols, students, marked_ids, papers):
    """Everything downstream of the columns and the rows — identical on both
    sides ON PURPOSE: these sums are done in JavaScript either way, so the
    proof is about their INPUTS."""
    members = pack["members"]
    handed = [s for s in pack["submissions"] if s.get("submitted_at")]
    last_activity = None
    for s in handed:
        if last_activity is None or s["submitted_at"] > last_activity:
            last_activity = s["submitted_at"]
    denom = len(members) * len(pack["assignments"])

    marked_sub = sum(cols[i]["sub"] for i in marked_ids)
    marked_on = sum(cols[i]["on_time"] for i in marked_ids)
    marked_late = sum(cols[i]["late"] for i in marked_ids)
    marked_unk = sum(cols[i]["unknown"] for i in marked_ids)
    known = marked_on + marked_late
    means = [cols[i]["mean"] for i in marked_ids if cols[i]["mean"] is not None]

    week0 = sum(1 for m in members if students[m["student"]["id"]]["in_week"])
    last_iso = None
    for m in members:
        v = students[m["student"]["id"]]["last_at"]
        if v and (last_iso is None or v > last_iso):
            last_iso = v
    flags = sum(1 for m in members
                if (not students[m["student"]["id"]]["in_week"])
                and (students[m["student"]["id"]]["missing_marked"]
                     or (students[m["student"]["id"]]["avg"] is not None
                         and students[m["student"]["id"]]["avg"] < 50)))
    return {
        "student_count": len(members),
        "assignment_count": len(pack["assignments"]),
        "submission_count": len(handed),
        "completion_pct": None if denom == 0
                          else js_round(len(handed) / denom * 100),
        "last_activity_at": last_activity,
        "classMean": js_round(sum(means) / len(means)) if means else None,
        "markedSub": marked_sub, "markedOnTime": marked_on,
        "markedLate": marked_late, "markedLateUnknown": marked_unk,
        "markedPct": js_round(marked_on / known * 100) if known else None,
        "week0": week0, "week1": len(members), "lastIso": last_iso,
        "flagged": flags,
        "cols": cols, "students": students,
    }


# ── what the page derives, from the rollup (after) ─────────────────────────

def rollup_values(pack, roll, now_iso):
    """`matrixFromRollup()` in shared/teacher-live.js, translated. The pack
    here carries NO submissions at all — that is the point."""
    papers = [dict({"id": a["id"], "due_at": a.get("due_at")},
                   **paper_state(a, now_iso))
              for a in pack["assignments"]]
    members = pack["members"]
    prow = {p["assignment_id"]: p for p in roll["papers"]}
    srow = {s["student_id"]: s for s in roll["students"]}

    cols = {}
    for p in papers:
        r = prow.get(p["id"]) or {"sub": 0, "off_roster": 0, "on_time": 0,
                                  "late": 0, "unknown": 0, "marked_n": 0,
                                  "mean": None}
        cols[p["id"]] = {
            "sub": r["sub"], "asked": len(members) + r["off_roster"],
            "on_time": r["on_time"], "late": r["late"], "unknown": r["unknown"],
            "marked_n": r["marked_n"], "mean": r["mean"],
        }
    students = {}
    for m in members:
        sid = m["student"]["id"]
        r = srow.get(sid) or {"avg": None, "in_week": False,
                              "on_time_week": False, "last_at": None,
                              "missing_marked": False}
        students[sid] = {"avg": r["avg"], "in_week": r["in_week"],
                         "on_time_week": r.get("on_time_week", False),
                         "last_at": r["last_at"],
                         "missing_marked": r["missing_marked"]}
    marked_ids = [p["id"] for p in papers if p["marked"]]

    # The three values the rollup answers directly rather than by summing.
    out = assemble({"members": members, "assignments": pack["assignments"],
                    "submissions": []}, cols, students, marked_ids, papers)
    out["submission_count"] = roll["summary"]["submissions_completed"]
    out["completion_pct"] = roll["summary"]["completion_pct"]
    out["last_activity_at"] = roll["summary"]["last_activity_at"]
    out["sql_class_mean"] = roll["summary"]["class_mean"]
    out["sql_member_count"] = roll["summary"]["active_member_count"]
    out["sql_assignment_count"] = roll["summary"]["assignment_count"]
    return out


# ── comparison ─────────────────────────────────────────────────────────────

SCALARS = ["student_count", "assignment_count", "submission_count",
           "completion_pct", "last_activity_at", "classMean", "markedSub",
           "markedOnTime", "markedLate", "markedLateUnknown", "markedPct",
           "week0", "week1", "lastIso", "flagged"]


def same_instant(a, b):
    """Timestamps come back from PostgREST as `…+00:00` and out of jsonb the
    same way, but a format difference must not be read as a value difference:
    compare the INSTANT."""
    if a is None or b is None:
        return a is None and b is None
    def p(x):
        return datetime.fromisoformat(x.replace("Z", "+00:00"))
    try:
        return p(a) == p(b)
    except ValueError:
        return a == b


def compare(cid, js, sq, fails):
    for k in SCALARS:
        a, b = js.get(k), sq.get(k)
        ok = same_instant(a, b) if k in ("last_activity_at", "lastIso") \
            else a == b
        if not ok:
            fails.append("%s · %s: js=%r sql=%r" % (cid[-4:], k, a, b))
    # SQL's own class_mean, against the mean-of-marked-column-means the page
    # computes. Two implementations, and they must not be allowed to drift.
    if js["classMean"] != sq.get("sql_class_mean"):
        fails.append("%s · class_mean(SQL)=%r vs classMean(page)=%r"
                     % (cid[-4:], sq.get("sql_class_mean"), js["classMean"]))
    if js["student_count"] != sq.get("sql_member_count"):
        fails.append("%s · active_member_count" % cid[-4:])
    if js["assignment_count"] != sq.get("sql_assignment_count"):
        fails.append("%s · assignment_count" % cid[-4:])
    for pid, a in js["cols"].items():
        b = sq["cols"].get(pid)
        if b is None:
            fails.append("%s · paper %s missing from rollup" % (cid[-4:], pid[-4:]))
            continue
        for k in a:
            if a[k] != b[k]:
                fails.append("%s · paper %s %s: js=%r sql=%r"
                             % (cid[-4:], pid[-4:], k, a[k], b[k]))
    for sid, a in js["students"].items():
        b = sq["students"].get(sid)
        if b is None:
            fails.append("%s · pupil %s missing" % (cid[-4:], sid[-4:]))
            continue
        for k in a:
            ok = same_instant(a[k], b[k]) if k == "last_at" else a[k] == b[k]
            if not ok:
                fails.append("%s · pupil %s %s: js=%r sql=%r"
                             % (cid[-4:], sid[-4:], k, a[k], b[k]))


def cells_compared(js):
    return len(SCALARS) + 3 + 7 * len(js["cols"]) + 4 * len(js["students"])


def run_reader(email, note, key, pw, ids):
    sess = sign_in(email, key, pw)
    token = sess["access_token"]
    now_iso = iso_now()

    packs, nmem, nasg, nsub = load_class_matrices(key, token, ids)
    windows = {cid: {"start": p["week"]["start_at"], "end": p["week"]["end_at"]}
               for cid, p in packs.items()}
    rows = rest("rpc/teacher_class_rollup_v2", key, token, method="POST",
                body={"p_class_ids": ids, "p_now": now_iso,
                      "p_windows": windows})
    roll = {r["class_id"]: r for r in rows}

    fails = []
    cells = 0
    for cid, pack in sorted(packs.items()):
        if cid not in roll:
            fails.append("%s · visible to the read, ABSENT from the rollup"
                         % cid[-4:])
            continue
        js = js_values(pack, now_iso)
        sq = rollup_values(pack, roll[cid], now_iso)
        cells += cells_compared(js)
        compare(cid, js, sq, fails)
    for cid in roll:
        if cid not in packs:
            fails.append("%s · returned by the rollup, INVISIBLE to the read"
                         % cid[-4:])

    print("  %-42s asked %2d · read sees %2d · rollup %2d · rows fetched %3d "
          "· cells %4d · %s"
          % (email, len(ids), len(packs), len(roll), nmem + nasg + nsub, cells,
             "❌ %d" % len(fails) if fails else "✅ 0 mismatches"))
    print("      %s" % note)
    for f in fails[:25]:
        print("        · %s" % f)
    return len(fails), cells, (nmem, nasg, nsub), packs


# ── the adversarial fixture ────────────────────────────────────────────────

FIXTURE_NOTE = """
Built on a clean TEST class, exercised through BOTH paths, then torn down by a
SNAPSHOTTED ID LIST — never a predicate. CLAUDE.md records a predicate wipe
killing four real rows; a `delete where title like 'mrb348%'` is exactly that
shape.

It is aimed at the values ROUND TWO DID NOT COVER, because round two already
proved the other six:
  · a paper whose deadline is in the CURRENT teaching week (week[0])
  · a departed pupil's submission — in the column's `asked`, not in the roster
  · `is_late` TRUE, FALSE and NULL-with-a-deadline and NULL-without — the
    tri-state, all four ways of reaching it
  · a pupil with no cell on a marked paper (missing_marked → flag)
  · a pupil whose average is exactly under and exactly over the flag's 50%
  · a column mean landing on an exact .5 boundary
"""


def fixture(key, pw, srk):
    print(FIXTURE_NOTE)
    hdr_sr = {"apikey": srk, "Authorization": "Bearer " + srk,
              "Content-Type": "application/json",
              "Prefer": "return=representation"}

    def sr(path, method="GET", body=None):
        data = json.dumps(body).encode() if body is not None else None
        req = urllib.request.Request(URL + "/rest/v1/" + path, data=data,
                                     headers=hdr_sr, method=method)
        try:
            r = urllib.request.urlopen(req, timeout=60, context=CTX)
            raw = r.read().decode()
            return json.loads(raw) if raw.strip() else []
        except urllib.error.HTTPError as e:
            raise SystemExit("SR %s %s -> %s %s"
                             % (method, path[:90], e.code,
                                e.read().decode()[:300]))

    # Round two's clean class: 3 members, 1 assignment, 0 submissions.
    cid = "2a000000-0000-0000-0000-000000000004"   # 8X2 — Monday anchor, 3
                                                  # members, ONE pre-existing
                                                  # marked paper nobody sat
    klass = sr("classes?select=id,name,assignment_day_of_week,school_id&id=eq." + cid)
    if not klass:
        raise SystemExit("fixture class %s is gone; pick another clean class"
                         % cid)
    anchor = klass[0].get("assignment_day_of_week")
    w = week_window(anchor)
    print("  class %s (%s) · anchor %s · this week %s -> %s"
          % (cid[-4:], klass[0]["name"], anchor, w["start_at"], w["end_at"]))

    base_members = sr("class_members?select=student_id&class_id=eq." + cid
                      + "&deleted_at=is.null&left_at=is.null")
    roster = sorted(r["student_id"] for r in base_members)
    base_assign = sr("assignments?select=id&class_id=eq." + cid
                     + "&deleted_at=is.null")
    if len(roster) != 3:
        raise SystemExit("fixture class has %d members; expected 3"
                         % len(roster))
    others = sr("class_members?select=student_id&class_id=neq." + cid
                + "&deleted_at=is.null&limit=60")
    offs = []
    for r in others:
        if r["student_id"] not in roster and r["student_id"] not in offs:
            offs.append(r["student_id"])
        if len(offs) == 2:
            break
    if len(offs) < 2:
        raise SystemExit("need two off-roster pupils for the departed case")
    subj = sr("assignments?select=subject_id&class_id=eq." + cid + "&limit=1")
    subject_id = subj[0]["subject_id"] if subj else None

    now = datetime.now(timezone.utc)
    # ⚠️ AN HOUR BEFORE THE WINDOW CLOSES, NOT A DAY AFTER IT OPENS. The first
    # draft used `start + 1 day`, which on any day but Monday is a deadline
    # that has ALREADY PASSED — so the paper was in this week AND marked, and
    # it walked into every marked-paper total. The two properties are
    # independent and this fixture wants exactly one of them: in the window,
    # still open.
    in_week_due = datetime.fromisoformat(
        w["end_at"].replace("Z", "+00:00")) - timedelta(hours=1)
    p0, p1, p2 = roster
    o1, o2 = offs

    def t(days, hours=0):
        return (now - timedelta(days=days, hours=hours)).isoformat()

    made, made_subs = [], []
    made_deck2 = made_session2 = None
    TEACHER_ID = "28000000-0000-0000-0000-000000000001"   # mide.badmus, this class's own teacher
    try:
        A = sr("assignments", "POST", [
            {"class_id": cid, "title": "mrb348r3 marked",
             "subject_id": subject_id, "topic": "MRB-348 round three",
             "quiz_type": "topic_quiz",
             # ⊕ Opus review, 27 Sep 2026 — WAS `t(3)`, which the by-hand
             # values below assumed landed OUTSIDE the current teaching
             # week's window, true on 24 Sep 2026 but not guaranteed on any
             # other day (a week's window is exactly 7 days; "3 days ago" can
             # fall either side of its start depending where "now" sits in
             # the week — this is what actually flaked on 27 Sep 2026, three
             # days after the value was hand-checked). `t(8)` is a
             # DETERMINISTIC placement: the window is `[start, start+7d)`,
             # `now` is always inside it, so `now - 8d < start - 1d < start`
             # for EVERY possible position of `now` in the window — always
             # strictly before the window opens, on any day, forever. p0/p1/
             # p2/o1's submission timestamps below are shifted by the same
             # +5 days so their relative gaps to this due date — and the
             # is_late-by-comparison results for p2/o1 — are unchanged.
             "due_at": t(8), "academic_week": 1,
             # `assignments_source_agrees_with_auto_generated` — a teacher-set
             # row must say so in BOTH columns.
             "source": "teacher", "auto_generated": False},
            {"class_id": cid, "title": "mrb348r3 this week",
             "subject_id": subject_id, "topic": "MRB-348 round three",
             "quiz_type": "topic_quiz", "due_at": in_week_due.isoformat(),
             "academic_week": 2,
             "source": "teacher", "auto_generated": False},
            {"class_id": cid, "title": "mrb348r3 no deadline",
             "subject_id": subject_id, "topic": "MRB-348 round three",
             "quiz_type": "topic_quiz", "due_at": None, "academic_week": 3,
             # `assignments_source_agrees_with_auto_generated` — a teacher-set
             # row must say so in BOTH columns.
             "source": "teacher", "auto_generated": False},
        ])
        # Keyed by TITLE rather than by position: PostgREST's return order is
        # not a contract, and picking the wrong paper here would make every
        # number below wrong in a way that still looked plausible.
        by_title = {a["title"]: a["id"] for a in A}
        marked = by_title["mrb348r3 marked"]
        thisweek = by_title["mrb348r3 this week"]
        nodue = by_title["mrb348r3 no deadline"]
        made = [marked, thisweek, nodue]

        # ⊕ Opus review, 27 Sep 2026 — A FLASHCARD SITTING CAN OUTRANK AN MCQ
        # COMPLETION. One more (released, open-forever, zero submissions from
        # anyone) flashcard assignment in this SAME class, with a single
        # `flashcard_sessions` row for p1, timed AFTER p1's most recent MCQ
        # activity (their `thisweek` completion, `t(0, 1)` below). Inert on
        # every existing hand value except `assignment_count` (this is the
        # class's 5th released paper, not its 4th) — nobody ever submits it,
        # so its own column reads sub=0/on_time=0/late=0/unknown=0/
        # marked_n=0/mean=None (the flashcard-kind rule, proven separately in
        # `fixture_flashcards()`), and `due_at IS NULL` means it can never be
        # `closed`, so it never touches `missing_marked` either. The deck
        # needs its own `flashcard_decks` row purely to satisfy
        # `assignments_flashcard_shape`'s FK — no cards, no set-work RPC.
        deck2 = sr("flashcard_decks", "POST", [{
            "school_id": klass[0]["school_id"], "created_by": TEACHER_ID,
            "title": "mrb348r3 flashcard probe", "source_kind": "typed",
            "status": "ready",
        }])
        made_deck2 = deck2[0]["id"]
        FA = sr("assignments", "POST", [{
            "class_id": cid, "school_id": klass[0]["school_id"],
            "subject_id": subject_id, "teacher_id": TEACHER_ID,
            "set_by": TEACHER_ID, "title": "mrb348r3 flashcard probe",
            "topic": "MRB-348 round three", "quiz_type": "flashcards",
            "source": "teacher", "auto_generated": False,
            "due_at": None, "kind": "flashcards", "deck_id": made_deck2,
            "flashcard_mode": "review", "completion_rule": "quick",
        }])
        flash_probe = FA[0]["id"]
        made.append(flash_probe)
        p1_sitting_at = t(0, 0.1)   # ~6 minutes ago — after p1's t(0, 1)
        FS2 = sr("flashcard_sessions", "POST", [{
            "assignment_id": flash_probe, "pupil_id": p1,
            "school_id": klass[0]["school_id"], "class_id": cid,
            "started_at": t(0, 0.2), "last_seen_at": p1_sitting_at,
        }])
        made_session2 = FS2[0]["id"]
        p1_sitting_at = FS2[0]["last_seen_at"]

        rows = [
            # ── the MARKED paper ────────────────────────────────────────
            # five graded cells: 5+3+2+8+1 = 19 out of 40 = 47.5 EXACTLY,
            # the rounding boundary, on purpose. Every stamp here is shifted
            # +5 days from the original draft (see the due_at comment above)
            # to keep the SAME gap to the new `due_at = t(8)`.
            # p0  is_late TRUE                      -> late
            {"assignment_id": marked, "student_id": p0, "score": 5,
             "max_score": 8, "submitted_at": t(9, 2), "completed_at": t(9, 2),
             "started_at": None,
             "status": "complete", "is_late": True, "attempts": 1},
            # p1  is_late FALSE                     -> on time
            {"assignment_id": marked, "student_id": p1, "score": 3,
             "max_score": 8, "submitted_at": t(10, 1), "completed_at": t(10, 1),
             "started_at": None,
             "status": "complete", "is_late": False, "attempts": 1},
            # p2  is_late NULL, stamp AFTER the deadline -> late by comparison
            {"assignment_id": marked, "student_id": p2, "score": 2,
             "max_score": 8, "submitted_at": t(7), "completed_at": t(7),
             "started_at": None,
             "status": "complete", "is_late": None, "attempts": 1},
            # o1  OFF THE ROLL, is_late NULL, stamp BEFORE the deadline
            #     -> on time by comparison; in the column, not in the roster
            {"assignment_id": marked, "student_id": o1, "score": 8,
             "max_score": 8, "submitted_at": t(11), "completed_at": t(11),
             "started_at": None,
             "status": "complete", "is_late": None, "attempts": 1},
            # o2  OFF THE ROLL, NO STAMP AT ALL, status complete -> a cell
            #     whose lateness is UNKNOWN, graded, and NOT "handed in"
            {"assignment_id": marked, "student_id": o2, "score": 1,
             "max_score": 8, "submitted_at": None, "completed_at": None,
             "started_at": None,
             "status": "complete", "is_late": None, "attempts": 1},
            # p0's RETAKE, a better mark, attempts = 2 -> must lose
            {"assignment_id": marked, "student_id": p0, "score": 8,
             "max_score": 8, "submitted_at": t(8), "completed_at": t(8),
             "started_at": None,
             "status": "complete", "is_late": False, "attempts": 2},
            # ── THIS WEEK's paper — OPEN, and RESULTS ARE LIVE ON IT ────
            # ⊕ Mide's 23 Sep 2026 ruling — extended to mirror production's
            # own shape (10h/Ph1, 24 Sep 2026): an OPEN set with TWO complete
            # on-time submissions and one in progress, the rest untouched.
            # p0 in progress, no stamp, not complete -> NO CELL at all.
            # ⊕ Opus review, 27 Sep 2026 — `started_at` set explicitly
            # (real rows get it from the app at the first answer; the
            # column has NO database default, so leaving it out here would
            # silently insert NULL and give `activity_at()` nothing to read
            # — the opposite of what this row exists to test).
            {"assignment_id": thisweek, "student_id": p0, "score": None,
             "max_score": None, "submitted_at": None, "completed_at": None,
             "started_at": t(0, 2),
             "status": "in_progress", "is_late": None, "attempts": 1},
            # p1 handed in, inside the window, on time -> a cell, and now
            # counted in `marked`/`classMean` too: it is RELEASED, and
            # released is all "marked" means now.
            {"assignment_id": thisweek, "student_id": p1, "score": 4,
             "max_score": 4, "submitted_at": t(0, 1), "completed_at": t(0, 1),
             "started_at": None,
             "status": "complete", "is_late": False, "attempts": 1},
            # p2 ALSO handed in, on time — the second "complete, on time"
            # result on a paper that has not closed. Its own cell also
            # proves `in_week` on a paper reached only through the NEW
            # "open counts as in-week" branch, independently of the
            # no-deadline paper below (which already does, on its own).
            {"assignment_id": thisweek, "student_id": p2, "score": 3,
             "max_score": 4, "submitted_at": t(0, 2), "completed_at": t(0, 2),
             "started_at": None,
             "status": "complete", "is_late": False, "attempts": 1},
            # ── the NO-DEADLINE paper ───────────────────────────────────
            # completed_at with NO submitted_at: a cell, and NOT a
            # "submission handed in" for the card's count. Never marked.
            {"assignment_id": nodue, "student_id": p2, "score": 1,
             "max_score": 8, "submitted_at": None, "completed_at": t(1),
             "started_at": None,
             "status": "complete", "is_late": None, "attempts": 1},
        ]
        S = sr("assignment_submissions", "POST", rows)
        made_subs = [s["id"] for s in S]
        print("  built %d assignments and %d submission rows\n"
              % (len(made), len(made_subs)))
        # ⊕ Opus review, 27 Sep 2026 — "an in-progress row": p0's `thisweek`
        # row above is `status: in_progress`, no stamps — its `started_at`
        # (DB-defaulted at insert time) is the row's own activity instant
        # per `activity_at()`/the SQL `activity` CTE. Captured here, from the
        # actual inserted row, rather than assumed.
        p0_inprogress = next(s for s in S
                             if s["assignment_id"] == thisweek and s["student_id"] == p0)
        p0_started_at = p0_inprogress["started_at"]

        # ── BY HAND ──────────────────────────────────────────────────────
        # ⊕ Mide's 23 Sep 2026 ruling — RECOMPUTED, not just re-labelled.
        # `marked` now means RELEASED, and every one of this class's five
        # assignments has a NULL `release_at` (the baseline row, confirmed
        # live on TEST — one pre-existing paper, due 21 May 2026, zero
        # submissions — plus the four built here, none of which sets
        # `release_at`). So ALL FIVE are now `marked`, where before only the
        # "marked" paper (closed) was. The baseline paper AND the flashcard
        # probe both contribute zero to every sum below (nobody ever sat
        # either) — but `thisweek` and `nodue` are NEWLY counted in
        # `markedSub`/`markedOnTime`/`markedLate`/`markedLateUnknown`/
        # `classMean`, and in each pupil's `avg`, wherever that pupil has a
        # cell on one of them.
        n_assign = len(base_assign) + 4
        hand = {
            "student_count": 3,
            "assignment_count": n_assign,
            # submitted_at IS NOT NULL over the FIRST attempts: p0, p1, p2
            # and o1 on the marked paper, p1 AND p2 on this week's. o2's row
            # and the no-deadline cell have no submitted_at; the in-progress
            # row and the flashcard probe (a SITTING, never a submission)
            # have none either. UNCHANGED BY THE RULING — submission_count
            # never was scoped to `marked`/`closed` — but +1 for p2's new
            # this-week submission: 5 -> 6.
            "submission_count": 6,
            "completion_pct": js_round(6 / (3 * n_assign) * 100),
            # markedSub etc. now sum over ALL FIVE released papers:
            # baseline(0) + marked(5) + thisweek(2, was 1) + nodue(1) +
            # flashcard probe(0) = 8. on_time: 0+2+2+0+0=4.
            # late: 0+2+0+0+0=2. unknown: 0+1+0+1+0=2.
            "markedSub": 8, "markedOnTime": 4, "markedLate": 2,
            "markedLateUnknown": 2,
            "markedPct": js_round(4 / 6 * 100),
            # mean of the released columns' means that have one:
            # marked=48 (19/40), thisweek=88 (7/8 — p1's 4/4 + p2's 3/4),
            # nodue=13 (1/8). baseline and the flashcard probe have no cell
            # so no mean (excluded, same reason).
            # (48 + 88 + 13) / 3 = 49.667 -> 50, half away from zero.
            "classMean": 50,
            # ⊕ Opus review, 27 Sep 2026 — WAS 3 ("ALL THREE"), the exact
            # value this fixture's `due_at = t(3)` flaked on: whether p0's
            # marked-paper due date fell inside the CURRENT teaching week
            # depended on where "now" sat in the week when the fixture ran,
            # not on anything the fixture actually controlled. `due_at` is
            # now `t(8)` — DETERMINISTICALLY before the window opens, every
            # day (see the comment on it, above) — so p0 has NO in-week
            # source at all: their only cell is the (now permanently closed
            # and out-of-window) marked paper. week0 is p1 and p2 only, via
            # the OPEN "this week" paper — the whole point of item 5: an
            # open paper counts the moment a pupil has a cell on it, not
            # only once its due date falls in the window.
            "week0": 2, "week1": 3,
            # p0 alone: `!in_week` (now always true for them) AND
            # `missing_marked` (true for everyone, via the pre-existing
            # baseline closed paper nobody ever sat — unaffected by any of
            # this). p1 and p2 are `in_week`, so `flagged` never asks about
            # their `missing_marked` at all.
            "flagged": 1,
        }
        hand_cols = {"sub": 5, "asked": 5, "on_time": 2, "late": 2,
                     "unknown": 1, "marked_n": 5, "mean": 48}
        # ⊕ NEW — the open "this week" paper's own column, now that it
        # counts: two on-time cells out of a roster of three, one in
        # progress (no cell), mirroring 10h/Ph1 on production.
        hand_thisweek_cols = {"sub": 2, "asked": 3, "on_time": 2, "late": 0,
                              "unknown": 0, "marked_n": 2, "mean": 88}
        hand_students = {
            # p0: avg unaffected (no cell on either new paper). `in_week` is
            # now DETERMINISTICALLY False — their only cell (the "marked"
            # paper) is permanently closed and permanently outside this
            # week's window (see the `week0` note above); `on_time_week`
            # stays False regardless (p0's cell on `marked` is LATE anyway).
            p0: {"avg": 63, "in_week": False, "on_time_week": False,
                 "missing_marked": True},
            # p1: avg now draws on `marked` (3/8) AND `thisweek` (4/4) —
            # (3+4)/(8+4) = 7/12 = 58.33 -> 58 (was 38, marked-only).
            # `in_week`/`on_time_week` both True via the open thisweek cell.
            p1: {"avg": 58, "in_week": True, "on_time_week": True,
                 "missing_marked": True},
            # p2: avg now draws on `marked` (2/8), `nodue` (1/8) AND
            # `thisweek` (3/4) — (2+1+3)/(8+8+4) = 6/20 = 30 (was 25,
            # marked+nodue only). `in_week` was already True via `nodue`
            # being open; `on_time_week` is NEW — nodue's lateness is
            # unknown (no due_at), but thisweek's cell is on time.
            p2: {"avg": 30, "in_week": True, "on_time_week": True,
                 "missing_marked": True},
        }

        token = sign_in("mide.badmus@test-rainford.local", key,
                        pw)["access_token"]
        now_iso = iso_now()
        packs, *_ = load_class_matrices(key, token, [cid])
        windows = {cid: {"start": packs[cid]["week"]["start_at"],
                         "end": packs[cid]["week"]["end_at"]}}
        rows_out = rest("rpc/teacher_class_rollup_v2", key, token, method="POST",
                        body={"p_class_ids": [cid], "p_now": now_iso,
                              "p_windows": windows})
        js = js_values(packs[cid], now_iso)
        sq = rollup_values(packs[cid], rows_out[0], now_iso)

        fails = []
        print("  %-24s %8s %8s %8s" % ("value", "by hand", "JS", "SQL"))
        for k, want in hand.items():
            a, b = js.get(k), sq.get(k)
            ok = (want == a == b)
            print("  %-24s %8s %8s %8s  %s"
                  % (k, want, a, b, "OK" if ok else "MISMATCH"))
            if not ok:
                fails.append("%s: hand=%r js=%r sql=%r" % (k, want, a, b))
        print()
        for k, want in hand_cols.items():
            a, b = js["cols"][marked][k], sq["cols"][marked][k]
            ok = (want == a == b)
            print("  marked column %-10s %8s %8s %8s  %s"
                  % (k, want, a, b, "OK" if ok else "MISMATCH"))
            if not ok:
                fails.append("marked.%s: hand=%r js=%r sql=%r"
                             % (k, want, a, b))
        print()
        for k, want in hand_thisweek_cols.items():
            a, b = js["cols"][thisweek][k], sq["cols"][thisweek][k]
            ok = (want == a == b)
            print("  thisweek column %-7s %8s %8s %8s  %s"
                  % (k, want, a, b, "OK" if ok else "MISMATCH"))
            if not ok:
                fails.append("thisweek.%s: hand=%r js=%r sql=%r"
                             % (k, want, a, b))
        print()
        for sid, want in hand_students.items():
            for k, v in want.items():
                a, b = js["students"][sid][k], sq["students"][sid][k]
                ok = (v == a == b)
                print("  pupil %s %-16s %8s %8s %8s  %s"
                      % (sid[-4:], k, v, a, b, "OK" if ok else "MISMATCH"))
                if not ok:
                    fails.append("pupil %s %s: hand=%r js=%r sql=%r"
                                 % (sid[-4:], k, v, a, b))

        # ⊕ Opus review, 27 Sep 2026 — "an in-progress row": p0's `thisweek`
        # attempt is in_progress (no cell at all — `p["closed"]` is False for
        # an open paper, so it is not `missing_marked` either), but its
        # `started_at` is the pupil's MOST RECENT activity in this class (2
        # hours ago, against ~9 days ago for their one completed cell). Both
        # sides must read it, even though there is no cell to read it FROM.
        for side, students in (("js", js["students"]), ("sql", sq["students"])):
            got = students[p0]["last_at"]
            ok = same_instant(got, p0_started_at)
            print("  p0 (in-progress row) %-4s last_at=%s (want started_at %s)  %s"
                  % (side, got, p0_started_at, "OK" if ok else "MISMATCH"))
            if not ok:
                fails.append("p0 %s last_at: got %r, want in-progress started_at %r"
                             % (side, got, p0_started_at))

        # ⊕ Opus review, 27 Sep 2026 — "a [flashcard] sitting newer than an
        # MCQ completion": p1's most recent MCQ activity is their `thisweek`
        # completion (~1 hour ago); the flashcard-probe sitting above is
        # ~6 minutes ago. `last_at` must read the SITTING, on both sides.
        for side, students in (("js", js["students"]), ("sql", sq["students"])):
            got = students[p1]["last_at"]
            ok = same_instant(got, p1_sitting_at)
            print("  p1 (flashcard probe) %-4s last_at=%s (want the sitting %s)  %s"
                  % (side, got, p1_sitting_at, "OK" if ok else "MISMATCH"))
            if not ok:
                fails.append("p1 %s last_at: got %r, want the flashcard sitting %r"
                             % (side, got, p1_sitting_at))

        # and then every remaining cell of the class, both paths
        compare(cid, js, sq, fails)
        # Each pupil dict in `hand_students` carries 4 keys (avg, in_week,
        # on_time_week, missing_marked); sum their lengths rather than
        # hardcoding, so this count cannot go stale the next time a key is
        # added or removed.
        per_pupil_keys = sum(len(v) for v in hand_students.values())
        print("\n  %s  %d values, three ways (by hand, in JS, in SQL)"
              % ("PASS" if not fails else "FAIL %d" % len(fails),
                 len(hand) + len(hand_cols) + len(hand_thisweek_cols)
                 + per_pupil_keys + cells_compared(js)))
        for f in fails:
            print("     - %s" % f)
        return len(fails)
    finally:
        # ⚠️ BY A SNAPSHOTTED ID LIST, NEVER A PREDICATE. CLAUDE.md records a
        # predicate wipe killing four real rows, and
        # `delete where title like 'mrb348%'` is exactly that shape.
        if made_session2:
            sr("flashcard_sessions?id=eq." + made_session2, "DELETE")
        for sid in made_subs:
            sr("assignment_submissions?id=eq." + sid, "DELETE")
        for aid in made:
            sr("assignments?id=eq." + aid, "DELETE")
        if made_deck2:
            sr("flashcard_decks?id=eq." + made_deck2, "DELETE")
        back_a = sr("assignments?select=id&class_id=eq." + cid
                    + "&deleted_at=is.null")
        back_m = sr("class_members?select=student_id&class_id=eq." + cid
                    + "&deleted_at=is.null&left_at=is.null")
        left = sr("assignment_submissions?select=id&id=in.(%s)"
                  % ",".join(made_subs)) if made_subs else []
        print("\n  TORN DOWN by id: %d submissions, %d assignments removed "
              "(incl. the flashcard probe + its session + its deck). "
              "Class back at %d assignments / %d members (baseline %d / %d); "
              "%d fixture rows left behind."
              % (len(made_subs), len(made), len(back_a), len(back_m),
                 len(base_assign), len(roster), len(left)))


FLASHCARD_FIXTURE_NOTE = """
MRB-351 landing, stream B — the flashcard kind split against the SAME rollup
proof method as round two/three: a fresh, ISOLATED throwaway class (never
2a...004, so its numbers cannot collide with the round-two/three fixture run
either side of it), torn down by a SNAPSHOTTED ID LIST, never a predicate.

Every assignment in this class is `kind = 'flashcards'`. That is deliberate:
it is the direct, minimal proof of "a class whose only released work is
flashcards -> class mean null" (E6 asked for this case explicitly), and it
also isolates the kind-split predicate from any MCQ column that could hide a
mismatch by coincidence.

Three flashcard papers:
  · OPEN, finished ON TIME    — a cell (on_time), never graded
  · CLOSED, finished LATE     — a cell (late), never graded
  · CLOSED, never completed   — no cell -> missing_marked for every pupil

The deck and the OPEN assignment are created through the REAL functions
(`flashcard_deck_save`, `flashcard_set_work`), signed in as the class's real
teacher (mide.badmus@test-rainford.local, who genuinely teaches this new
class via a fresh class_teachers row) — proving the kind-determining columns
(`kind`, `deck_id`, `flashcard_mode`, `completion_rule`, `quiz_type`) are
exactly what the RPC itself writes, not a hand-typed guess. The completion
write (what `flashcard_record` does when a pupil finishes) is reproduced by
a direct service-role INSERT matching `flashcard_record`'s own INSERT
byte-for-byte (score = max_score = card count, `is_late` stamped at
completion) — the same shortcut the pre-existing round-two/three fixture
already takes for every one of its MCQ submissions, since exercising
`flashcard_record` itself would need a throwaway PUPIL sign-in, which is a
separate, larger piece of scaffolding than this rollup proof needs. The
CLOSED/late and CLOSED/missing papers are built the same direct-insert way,
because Set work v2 refuses a release or due date in the past
(`release_past`/`due_before_release`) — a genuinely closed paper cannot be
created through the live RPC at all, on TEST or on production.
"""


def fixture_flashcards(key, pw, srk):
    print(FLASHCARD_FIXTURE_NOTE)
    hdr_sr = {"apikey": srk, "Authorization": "Bearer " + srk,
              "Content-Type": "application/json",
              "Prefer": "return=representation"}

    def sr(path, method="GET", body=None):
        data = json.dumps(body).encode() if body is not None else None
        req = urllib.request.Request(URL + "/rest/v1/" + path, data=data,
                                     headers=hdr_sr, method=method)
        try:
            r = urllib.request.urlopen(req, timeout=60, context=CTX)
            raw = r.read().decode()
            return json.loads(raw) if raw.strip() else []
        except urllib.error.HTTPError as e:
            raise SystemExit("SR %s %s -> %s %s"
                             % (method, path[:90], e.code,
                                e.read().decode()[:300]))

    TEACHER = "mide.badmus@test-rainford.local"
    TEACHER_ID = "28000000-0000-0000-0000-000000000001"
    SCHOOL_ID = "d0233615-3ee7-4b1b-a8ff-c912c5196d62"
    ACADEMIC_YEAR_ID = "2f560a43-73b9-422a-8fc7-ec46524a288a"
    # Maya / Felix / Amara — the real 8X2 roster, reused as members of this
    # NEW class too (a profile can belong to more than one class; nothing
    # about them is mutated, and removing them from THIS class's roster at
    # teardown does not touch their 8X2 membership).
    PUPILS = ["29000000-0000-0000-0000-00000000000e",
              "29000000-0000-0000-0000-00000000000f",
              "29000000-0000-0000-0000-000000000010"]
    p_open, p_late, p_missing = PUPILS

    made_class = made_ct = made_members = made_asg = made_subs = None
    made_deck = None
    made_session = None
    class_id = None
    try:
        now = datetime.now(timezone.utc)

        def t(days, hours=0):
            return (now - timedelta(days=days, hours=hours)).isoformat()

        # ── the class, isolated ──────────────────────────────────────────
        C = sr("classes", "POST", [{
            "school_id": SCHOOL_ID, "academic_year_id": ACADEMIC_YEAR_ID,
            "name": "mrb351proof-flashcards-only", "key_stage": "KS3",
            "year_group": 8, "assignment_day_of_week": 1,
        }])
        class_id = C[0]["id"]
        made_class = class_id

        CT = sr("class_teachers", "POST", [{
            "class_id": class_id, "teacher_id": TEACHER_ID,
            "role": "subject_teacher", "subject_id": "26000000-0000-0000-0000-000000000001",
        }])
        made_ct = CT[0]["id"]

        MEM = sr("class_members", "POST",
                 [{"class_id": class_id, "student_id": pid, "joined_via": "admin_added"}
                  for pid in PUPILS])
        made_members = [m["id"] for m in MEM]

        print("  class %s created, teacher attached, %d members"
              % (class_id[-4:], len(made_members)))

        # ── the deck + the OPEN assignment, through the REAL functions ────
        token = sign_in(TEACHER, key, pw)["access_token"]
        deck_body = {"p_deck": None, "p_title": "mrb351 proof deck",
                     "p_cards": [{"question": "Q1", "answer": "A1"},
                                 {"question": "Q2", "answer": "A2"}],
                     "p_meta": {"source_kind": "typed"}, "p_finalise": True}
        deck_out = rest("rpc/flashcard_deck_save", key, token, "POST", deck_body)
        deck_id = deck_out["deck_id"]
        made_deck = deck_id
        print("  deck %s saved via flashcard_deck_save: %r" % (deck_id[-4:], deck_out))

        # p_release_at: None -> the RPC defaults it to its own now(), which
        # is always within the "not more than 5 minutes in the past" rule;
        # t(0, 1) (an hour ago) would trip `release_past` and refuse.
        set_body = {"p_class_ids": [class_id], "p_deck": deck_id,
                    "p_mode": "review", "p_rule": "quick",
                    "p_title": "mrb351 proof — open, on time",
                    "p_release_at": None,
                    "p_due_at": (now + timedelta(days=10)).isoformat()}
        set_out = rest("rpc/flashcard_set_work", key, token, "POST", set_body)
        aid_open = set_out["assignment_ids"][0]
        print("  assignment %s set via flashcard_set_work: %r"
              % (aid_open[-4:], set_out))

        # ── the two CLOSED papers: Set work v2 refuses a past release/due,
        # so these are the same direct-insert shape as the MCQ fixture. ────
        SUBJECT_ID = "26000000-0000-0000-0000-000000000001"
        A = sr("assignments", "POST", [
            {"class_id": class_id, "school_id": SCHOOL_ID, "subject_id": SUBJECT_ID,
             "teacher_id": TEACHER_ID, "set_by": TEACHER_ID,
             "title": "mrb351 proof — closed, late", "topic": "mrb351 proof",
             "quiz_type": "flashcards", "source": "teacher",
             "auto_generated": False, "key_stage": "KS3", "year_group": 8,
             "release_at": t(5), "due_at": t(3),
             "kind": "flashcards", "deck_id": deck_id,
             "flashcard_mode": "review", "completion_rule": "quick"},
            {"class_id": class_id, "school_id": SCHOOL_ID, "subject_id": SUBJECT_ID,
             "teacher_id": TEACHER_ID, "set_by": TEACHER_ID,
             "title": "mrb351 proof — closed, missing", "topic": "mrb351 proof",
             "quiz_type": "flashcards", "source": "teacher",
             "auto_generated": False, "key_stage": "KS3", "year_group": 8,
             "release_at": t(5), "due_at": t(3),
             "kind": "flashcards", "deck_id": deck_id,
             "flashcard_mode": "review", "completion_rule": "quick"},
        ])
        by_title = {a["title"]: a["id"] for a in A}
        aid_late = by_title["mrb351 proof — closed, late"]
        aid_missing = by_title["mrb351 proof — closed, missing"]
        made_asg = [aid_open, aid_late, aid_missing]

        # ── completions, written exactly as flashcard_record's own INSERT
        # does it: score = max_score = card count (2), is_late stamped at
        # completion against the assignment's own due_at. ─────────────────
        S = sr("assignment_submissions", "POST", [
            # p_open finishes comfortably inside the open window -> on time.
            {"assignment_id": aid_open, "student_id": p_open, "score": 2,
             "max_score": 2, "submitted_at": t(0, 0.5), "completed_at": t(0, 0.5),
             "started_at": t(0, 1), "status": "complete", "is_late": False,
             "attempts": 1, "attempt_no": 1},
            # p_late finishes two days after the paper closed -> late.
            {"assignment_id": aid_late, "student_id": p_late, "score": 2,
             "max_score": 2, "submitted_at": t(1), "completed_at": t(1),
             "started_at": t(1, 1), "status": "complete", "is_late": True,
             "attempts": 1, "attempt_no": 1},
            # aid_missing: nobody submits. p_missing is on the roster and
            # never opens it -> missing_marked for every pupil on this column.
        ])
        made_subs = [s["id"] for s in S]
        print("  built 3 flashcard assignments (1 via the real RPC, 2 direct) "
              "and %d submission rows" % len(made_subs))

        # ── p_missing: A DECK SITTING, AND NOTHING ELSE (Opus review,
        # 27 Sep 2026) — p_missing never submits anything in this class (see
        # aid_missing above), so before this row they have NO activity signal
        # at all. One `flashcard_sessions` row, no submission, proves the
        # sitting alone is enough: "a pupil with only a deck sitting" from
        # the review's own wording.
        FS = sr("flashcard_sessions", "POST", [{
            "assignment_id": aid_open, "pupil_id": p_missing,
            "school_id": SCHOOL_ID, "class_id": class_id,
            "started_at": t(0, 1), "last_seen_at": t(0, 0.5),
        }])
        made_session = FS[0]["id"]
        session_last_seen = FS[0]["last_seen_at"]
        print("  flashcard session %s for p_missing (deck sitting only, no "
              "submission): last_seen_at=%s" % (made_session[-4:], session_last_seen))

        # ── read, exactly as the round-two/three method does ──────────────
        now_iso = iso_now()
        packs, *_ = load_class_matrices(key, token, [class_id])
        pack = packs[class_id]
        windows = {class_id: {"start": pack["week"]["start_at"],
                              "end": pack["week"]["end_at"]}}
        rows_out = rest("rpc/teacher_class_rollup_v2", key, token, method="POST",
                        body={"p_class_ids": [class_id], "p_now": now_iso,
                              "p_windows": windows})
        js = js_values(pack, now_iso)
        sq = rollup_values(pack, rows_out[0], now_iso)

        fails = []

        # E6's own case, stated directly: every released paper is
        # `kind = 'flashcards'`, so no column is ever graded, so the class
        # mean must be null on BOTH sides.
        for label, val in (("js classMean", js["classMean"]),
                           ("sql class_mean", sq.get("sql_class_mean"))):
            ok = val is None
            print("  %-16s %8s  %s" % (label, val, "OK" if ok else "MISMATCH — expected null"))
            if not ok:
                fails.append("%s: expected null, got %r" % (label, val))

        # Every column: marked_n == 0 and mean is None, js AND sql, even
        # though on_time/late are non-zero (a flashcard cell counts as a
        # cell everywhere except being graded).
        for aid, label, want_on_time, want_late in (
                (aid_open, "open/on-time", 1, 0),
                (aid_late, "closed/late", 0, 1),
                (aid_missing, "closed/missing", 0, 0)):
            for side, cols in (("js", js["cols"]), ("sql", sq["cols"])):
                c = cols[aid]
                ok = (c["marked_n"] == 0 and c["mean"] is None
                      and c["on_time"] == want_on_time and c["late"] == want_late)
                print("  %-14s %-4s sub=%s on_time=%s late=%s marked_n=%s mean=%s  %s"
                      % (label, side, c["sub"], c["on_time"], c["late"],
                         c["marked_n"], c["mean"], "OK" if ok else "MISMATCH"))
                if not ok:
                    fails.append("%s %s: %r" % (label, side, c))

        # missing_marked: true for every pupil on the closed/missing paper's
        # class (all three never submitted it), false-contribution check for
        # p_open/p_late who are NOT missing anything closed (aid_late they
        # DID submit, even though late; aid_missing they did not).
        for pid, label in ((p_open, "p_open"), (p_late, "p_late"),
                           (p_missing, "p_missing")):
            for side, students in (("js", js["students"]), ("sql", sq["students"])):
                mm = students[pid]["missing_marked"]
                ok = mm is True   # nobody submitted aid_missing; all 3 owe it
                print("  %-10s %-4s missing_marked=%s  %s"
                      % (label, side, mm, "OK" if ok else "MISMATCH"))
                if not ok:
                    fails.append("%s %s missing_marked: got %r, want True"
                                 % (label, side, mm))

        # avg: p_open's and p_late's cells are both ungraded, so avg is null
        # for everyone — a flashcard-only class has no average, by design.
        for pid in PUPILS:
            for side, students in (("js", js["students"]), ("sql", sq["students"])):
                av = students[pid]["avg"]
                if av is not None:
                    fails.append("%s %s avg: expected null (ungraded class), got %r"
                                 % (pid[-4:], side, av))

        # ⊕ Opus review, 27 Sep 2026 — "a pupil with only a deck sitting":
        # p_missing has NO cell anywhere in this class (never opens
        # aid_missing, and aid_open/aid_late are p_open's/p_late's), so their
        # ONLY activity signal is the flashcard_sessions row above. Both
        # sides must read it as p_missing's last_at, not null.
        for side, students in (("js", js["students"]), ("sql", sq["students"])):
            got = students[p_missing]["last_at"]
            ok = same_instant(got, session_last_seen)
            print("  p_missing  %-4s last_at=%s (want the sitting %s)  %s"
                  % (side, got, session_last_seen, "OK" if ok else "MISMATCH"))
            if not ok:
                fails.append("p_missing %s last_at: got %r, want sitting %r"
                             % (side, got, session_last_seen))

        # and then every remaining cell of the class, both paths — the
        # generic JS==SQL diff, exactly as round two/three's compare() does.
        compare(class_id, js, sq, fails)
        cells = cells_compared(js)
        print("\n  %s  %d generic cells + 13 flashcard-specific assertions"
              % ("PASS" if not fails else "FAIL %d" % len(fails), cells))
        for f in fails:
            print("     - %s" % f)
        return len(fails)
    finally:
        # ⚠️ BY SNAPSHOTTED IDS ONLY, NEVER A PREDICATE.
        if made_session:
            sr("flashcard_sessions?id=eq." + made_session, "DELETE")
        if made_subs:
            for sid in made_subs:
                sr("assignment_submissions?id=eq." + sid, "DELETE")
        if made_asg:
            for aid in made_asg:
                sr("assignment_flashcards?assignment_id=eq." + aid, "DELETE")
                sr("assignments?id=eq." + aid, "DELETE")
        if made_deck:
            sr("flashcard_cards?deck_id=eq." + made_deck, "DELETE")
            sr("flashcard_decks?id=eq." + made_deck, "DELETE")
        if made_members:
            for mid in made_members:
                sr("class_members?id=eq." + mid, "DELETE")
        if made_ct:
            sr("class_teachers?id=eq." + made_ct, "DELETE")
        if made_class:
            sr("classes?id=eq." + made_class, "DELETE")
        left_class = sr("classes?select=id&id=eq." + (made_class or "00000000-0000-0000-0000-000000000000"))
        print("\n  TORN DOWN by id: class %s, %s teacher row, %s members, "
              "%s assignments, %s submissions, deck. Class row remaining "
              "after teardown: %d (want 0)."
              % ((made_class or "?")[-4:], 1 if made_ct else 0,
                 len(made_members or []), len(made_asg or []),
                 len(made_subs or []), len(left_class)))


ROWS_NOTE = """
ROWS FETCHED PER SCREEN, on the basis round two's §4 used: the three reads
`loadClassMatrices` makes (members + assignments + submissions) plus, after
this ticket, one rollup row per class whose submissions were NOT fetched.

⚠️ It counts ROWS, not requests or bytes, and it is measured against the
realistic TEST teacher rather than projected. The December projection in the
report is arithmetic on top of this, and is labelled as such.
"""


def rows_per_screen(key, pw):
    print(ROWS_NOTE)
    email = "mide.badmus@test-rainford.local"
    token = sign_in(email, key, pw)["access_token"]
    ids = [r["id"] for r in rest("classes?select=id&deleted_at=is.null", key,
                                 token)]
    packs, nmem, nasg, nsub = load_class_matrices(key, token, ids)
    per_class = {}
    for cid, p in sorted(packs.items()):
        per_class[cid] = (len(p["members"]), len(p["assignments"]),
                          len(p["submissions"]))
    print("  %s sees %d classes" % (email, len(packs)))
    for cid, (m, a, s) in per_class.items():
        print("    %s  %2d members · %2d assignments · %2d submissions"
              % (cid[-4:], m, a, s))
    total_m = sum(v[0] for v in per_class.values())
    total_a = sum(v[1] for v in per_class.values())
    total_s = sum(v[2] for v in per_class.values())
    before = total_m + total_a + total_s
    busiest = max(per_class, key=lambda c: per_class[c][2])
    quietest = min(per_class, key=lambda c: per_class[c][2])

    screens = [
        ("classes.html", []),
        ("digest.html", []),
        ("insights.html", []),
        ("class-detail.html ?class=%s (busiest)" % busiest[-4:], [busiest]),
        ("class-detail.html ?class=%s (quietest)" % quietest[-4:], [quietest]),
        ("assignment.html  (one paper of %s)" % busiest[-4:], [busiest]),
        ("student-detail.html (%s)" % busiest[-4:], [busiest]),
        ("class-detail.html with NO ?class=", None),
    ]
    print("\n  %-44s %8s %8s %8s" % ("screen", "before", "after", "saving"))
    for name, scope in screens:
        if scope is None:
            after = before
            rollup = 0
        else:
            subs = sum(per_class[c][2] for c in scope)
            rollup = len([c for c in per_class if c not in scope])
            after = total_m + total_a + subs + rollup
        print("  %-44s %8d %8d %8s%s"
              % (name, before, after, before - after,
                 "" if rollup == 0 else "   (%d rollup rows)" % rollup))
    print("\n  before = %d (%d members + %d assignments + %d submissions)"
          % (before, total_m, total_a, total_s))
    return 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--fixture", action="store_true",
                    help="build, prove and tear down the adversarial fixture")
    ap.add_argument("--rows", action="store_true",
                    help="tabulate rows fetched per screen, before and after")
    a = ap.parse_args()

    pw = os.environ.get("MRB_TEST_TEACHER_PASSWORD")
    if not pw:
        raise SystemExit("$MRB_TEST_TEACHER_PASSWORD is not set.")
    srk, ref = service_key()
    key = anon_key()
    print("credential ref, proven from the key payload : %s" % ref)
    print("=> TEST. Every measured read below is made with the ANON key as a "
          "signed-in user, under real RLS.\n")

    if a.rows:
        return rows_per_screen(key, pw)

    if a.fixture:
        f1 = fixture(key, pw, srk)
        print("\n" + "=" * 78 + "\n")
        f2 = fixture_flashcards(key, pw, srk)
        return 1 if (f1 or f2) else 0

    ids = [r["id"] for r in
           json.loads(urllib.request.urlopen(urllib.request.Request(
               URL + "/rest/v1/classes?select=id&deleted_at=is.null&order=id",
               headers={"apikey": srk, "Authorization": "Bearer " + srk}),
               timeout=30, context=CTX).read().decode())]
    print("asking about all %d classes on TEST, for every reader\n" % len(ids))

    total_f = total_c = 0
    for email, note in READERS:
        f, c, counts, _ = run_reader(email, note, key, pw, ids)
        total_f += f
        total_c += c
        print()
    print("  %d values compared, %d mismatches" % (total_c, total_f))
    return 1 if total_f else 0


if __name__ == "__main__":
    sys.exit(main())
