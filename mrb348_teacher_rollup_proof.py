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


def cell_of(s, due_at):
    """`cellOf(s, paper)` — the one cell both the rows and the columns read."""
    if not s:
        return None
    stamp = s.get("completed_at") or s.get("submitted_at") or None
    done = bool(stamp) or s.get("status") == "complete"
    if not done:
        return None
    score = mx = pct = None
    if s.get("score") is not None and s.get("max_score") is not None \
            and s["max_score"] > 0:
        score, mx = s["score"], s["max_score"]
        pct = js_round(score / mx * 100)
    late = None
    if s.get("is_late") is not None:
        late = s["is_late"] is True
    elif stamp and due_at:
        late = stamp > due_at            # raw strings, as the JS compares them
    return {"stamp": stamp, "score": score, "max": mx, "pct": pct, "late": late}


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
        "subject:subject_id(id,name)")
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
            "completed_at,status,is_late,attempts,attempt_no")
            + "&assignment_id=" + in_list(aids) + "&deleted_at=is.null",
            key, token)

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
    papers = [dict({"id": a["id"], "due_at": a.get("due_at")},
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
            c = cell_of(mine.get(p["id"]), p["due_at"])
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
            c = cell_of(mine.get(p["id"]), p["due_at"])
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
            if c["stamp"] and (last is None or c["stamp"] > last):
                last = c["stamp"]
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
    klass = sr("classes?select=id,name,assignment_day_of_week&id=eq." + cid)
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
    try:
        A = sr("assignments", "POST", [
            {"class_id": cid, "title": "mrb348r3 marked",
             "subject_id": subject_id, "topic": "MRB-348 round three",
             "quiz_type": "topic_quiz", "due_at": t(3), "academic_week": 1,
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

        rows = [
            # ── the MARKED paper ────────────────────────────────────────
            # five graded cells: 5+3+2+8+1 = 19 out of 40 = 47.5 EXACTLY,
            # the rounding boundary, on purpose.
            # p0  is_late TRUE                      -> late
            {"assignment_id": marked, "student_id": p0, "score": 5,
             "max_score": 8, "submitted_at": t(4, 2), "completed_at": t(4, 2),
             "status": "complete", "is_late": True, "attempts": 1},
            # p1  is_late FALSE                     -> on time
            {"assignment_id": marked, "student_id": p1, "score": 3,
             "max_score": 8, "submitted_at": t(5, 1), "completed_at": t(5, 1),
             "status": "complete", "is_late": False, "attempts": 1},
            # p2  is_late NULL, stamp AFTER the deadline -> late by comparison
            {"assignment_id": marked, "student_id": p2, "score": 2,
             "max_score": 8, "submitted_at": t(2), "completed_at": t(2),
             "status": "complete", "is_late": None, "attempts": 1},
            # o1  OFF THE ROLL, is_late NULL, stamp BEFORE the deadline
            #     -> on time by comparison; in the column, not in the roster
            {"assignment_id": marked, "student_id": o1, "score": 8,
             "max_score": 8, "submitted_at": t(6), "completed_at": t(6),
             "status": "complete", "is_late": None, "attempts": 1},
            # o2  OFF THE ROLL, NO STAMP AT ALL, status complete -> a cell
            #     whose lateness is UNKNOWN, graded, and NOT "handed in"
            {"assignment_id": marked, "student_id": o2, "score": 1,
             "max_score": 8, "submitted_at": None, "completed_at": None,
             "status": "complete", "is_late": None, "attempts": 1},
            # p0's RETAKE, a better mark, attempts = 2 -> must lose
            {"assignment_id": marked, "student_id": p0, "score": 8,
             "max_score": 8, "submitted_at": t(3), "completed_at": t(3),
             "status": "complete", "is_late": False, "attempts": 2},
            # ── THIS WEEK's paper — OPEN, and RESULTS ARE LIVE ON IT ────
            # ⊕ Mide's 23 Sep 2026 ruling — extended to mirror production's
            # own shape (10h/Ph1, 24 Sep 2026): an OPEN set with TWO complete
            # on-time submissions and one in progress, the rest untouched.
            # p0 in progress, no stamp, not complete -> NO CELL at all
            {"assignment_id": thisweek, "student_id": p0, "score": None,
             "max_score": None, "submitted_at": None, "completed_at": None,
             "status": "in_progress", "is_late": None, "attempts": 1},
            # p1 handed in, inside the window, on time -> a cell, and now
            # counted in `marked`/`classMean` too: it is RELEASED, and
            # released is all "marked" means now.
            {"assignment_id": thisweek, "student_id": p1, "score": 4,
             "max_score": 4, "submitted_at": t(0, 1), "completed_at": t(0, 1),
             "status": "complete", "is_late": False, "attempts": 1},
            # p2 ALSO handed in, on time — the second "complete, on time"
            # result on a paper that has not closed. Its own cell also
            # proves `in_week` on a paper reached only through the NEW
            # "open counts as in-week" branch, independently of the
            # no-deadline paper below (which already does, on its own).
            {"assignment_id": thisweek, "student_id": p2, "score": 3,
             "max_score": 4, "submitted_at": t(0, 2), "completed_at": t(0, 2),
             "status": "complete", "is_late": False, "attempts": 1},
            # ── the NO-DEADLINE paper ───────────────────────────────────
            # completed_at with NO submitted_at: a cell, and NOT a
            # "submission handed in" for the card's count. Never marked.
            {"assignment_id": nodue, "student_id": p2, "score": 1,
             "max_score": 8, "submitted_at": None, "completed_at": t(1),
             "status": "complete", "is_late": None, "attempts": 1},
        ]
        S = sr("assignment_submissions", "POST", rows)
        made_subs = [s["id"] for s in S]
        print("  built %d assignments and %d submission rows\n"
              % (len(made), len(made_subs)))

        # ── BY HAND ──────────────────────────────────────────────────────
        # ⊕ Mide's 23 Sep 2026 ruling — RECOMPUTED, not just re-labelled.
        # `marked` now means RELEASED, and every one of this class's four
        # assignments has a NULL `release_at` (the baseline row, confirmed
        # live on TEST — one pre-existing paper, due 21 May 2026, zero
        # submissions — plus the three built here, none of which sets
        # `release_at`). So ALL FOUR are now `marked`, where before only the
        # "marked" paper (closed) was. The baseline paper contributes zero
        # to every sum regardless (nobody ever sat it), so it changes
        # nothing below — but `thisweek` and `nodue` are NEWLY counted in
        # `markedSub`/`markedOnTime`/`markedLate`/`markedLateUnknown`/
        # `classMean`, and in each pupil's `avg`, wherever that pupil has a
        # cell on one of them.
        n_assign = len(base_assign) + 3
        hand = {
            "student_count": 3,
            "assignment_count": n_assign,
            # submitted_at IS NOT NULL over the FIRST attempts: p0, p1, p2
            # and o1 on the marked paper, p1 AND p2 on this week's. o2's row
            # and the no-deadline cell have no submitted_at; the in-progress
            # row has none either. UNCHANGED BY THE RULING — submission_count
            # never was scoped to `marked`/`closed` — but +1 for p2's new
            # this-week submission: 5 -> 6.
            "submission_count": 6,
            "completion_pct": js_round(6 / (3 * n_assign) * 100),
            # markedSub etc. now sum over ALL FOUR released papers:
            # baseline(0) + marked(5) + thisweek(2, was 1) + nodue(1) = 8.
            # on_time:  0 + 2 + 2 + 0 = 4.  late: 0 + 2 + 0 + 0 = 2.
            # unknown:  0 + 1 + 0 + 1 = 2.
            "markedSub": 8, "markedOnTime": 4, "markedLate": 2,
            "markedLateUnknown": 2,
            "markedPct": js_round(4 / 6 * 100),
            # mean of the released columns' means that have one:
            # marked=48 (19/40), thisweek=88 (7/8 — p1's 4/4 + p2's 3/4),
            # nodue=13 (1/8). baseline has no cell so no mean (excluded).
            # (48 + 88 + 13) / 3 = 49.667 -> 50, half away from zero.
            "classMean": 50,
            # week0: ALL THREE. p1 and p2 via the OPEN "this week" paper —
            # the whole point of item 5: an open paper counts the moment a
            # pupil has a cell on it, not only once its due date falls in
            # the window. p0's own cell is on the "marked" paper, and
            # `t(3)` — three days before the run — lands INSIDE the current
            # teaching week's window whenever the fixture is run more than a
            # couple of days into that week (the window is the whole
            # calendar week, not "the last three days"); observed true on
            # TEST on 24 Sep 2026, confirmed by `w["start_at"]`/`w["end_at"]`
            # printed above. That was already true of the FIRST due-in-
            # window test, before this ruling — it is not something item 5
            # introduces — it was simply never exercised by round two's
            # values, which this by-hand block did not check against the
            # printed window either. `week0`/`flagged` below follow whatever
            # the actual window says, not a day-of-week assumption; JS and
            # SQL computing the SAME answer from the SAME window is the
            # actual proof, and both did.
            "week0": 3, "week1": 3,
            # Nobody: every pupil is now `in_week` (see above), and
            # `flagged` requires `!in_week`.
            "flagged": 0,
        }
        hand_cols = {"sub": 5, "asked": 5, "on_time": 2, "late": 2,
                     "unknown": 1, "marked_n": 5, "mean": 48}
        # ⊕ NEW — the open "this week" paper's own column, now that it
        # counts: two on-time cells out of a roster of three, one in
        # progress (no cell), mirroring 10h/Ph1 on production.
        hand_thisweek_cols = {"sub": 2, "asked": 3, "on_time": 2, "late": 0,
                              "unknown": 0, "marked_n": 2, "mean": 88}
        hand_students = {
            # p0: avg unaffected (no cell on either new paper), but
            # `in_week` is True via the PRE-EXISTING "marked" paper — its
            # due date falls inside the current window (see the note on
            # `week0` above). `on_time_week` stays False: p0's cell on
            # `marked` is LATE, not on time.
            p0: {"avg": 63, "in_week": True, "on_time_week": False,
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
        for sid in made_subs:
            sr("assignment_submissions?id=eq." + sid, "DELETE")
        for aid in made:
            sr("assignments?id=eq." + aid, "DELETE")
        back_a = sr("assignments?select=id&class_id=eq." + cid
                    + "&deleted_at=is.null")
        back_m = sr("class_members?select=student_id&class_id=eq." + cid
                    + "&deleted_at=is.null&left_at=is.null")
        left = sr("assignment_submissions?select=id&id=in.(%s)"
                  % ",".join(made_subs)) if made_subs else []
        print("\n  TORN DOWN by id: %d submissions, %d assignments removed. "
              "Class back at %d assignments / %d members (baseline %d / %d); "
              "%d fixture rows left behind."
              % (len(made_subs), len(made), len(back_a), len(back_m),
                 len(base_assign), len(roster), len(left)))


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
        return 1 if fixture(key, pw, srk) else 0

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
