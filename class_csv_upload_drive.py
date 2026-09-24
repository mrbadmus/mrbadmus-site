#!/usr/bin/env python3
"""class_csv_upload_drive.py — MRB (feat/class-csv-upload), real bytes on TEST.

    MRB_THROWAWAY_PASSWORD=<the fixture password> python3 class_csv_upload_drive.py

One command. It spawns `deno run` itself (the ACTUAL
supabase/functions/roster-import/index.ts, no edits, no stub) on :8000 for
the duration of the run and tears it down after — no separate terminal, no
Docker, no Supabase-CLI login/PAT needed for this: `Deno.serve` + two env
vars is all the file itself needs. Requires Deno on PATH (`brew install
deno`); SKIPS cleanly, by name, if it isn't. Every request below
goes through that process, into the real TEST Postgres, through real RLS-
bypassing service-role reads plus the function's own real auth.getUser() JWT
check. Uses the two real throwaway accounts MRB-326 already established in
that project (mrb326_admin@throwaway.test — a live staff_scopes school_admin
grant; mrb326_teacher@throwaway.test — plain teacher, no scope), signed in
for real via password grant — no stubbed session. Password comes from
$MRB_THROWAWAY_PASSWORD, the same switch teacher_admin_real_drive.py reads;
absent, this drive SKIPS rather than failing (gate_registry.py needs_env).

⚠️ TEST IS MISSING A MIGRATION, discovered by this drive (20 Sep 2026):
`supabase/migrations/20260629195630_add_profiles_external_student_id.sql`
was never applied to the TEST project (qeppkiswvclkkwbxmlok) — its `profiles`
table has no `external_student_id` column. That is a PRE-EXISTING gap in
roster-import's write path, unrelated to this ticket's `id`-path change: ANY
real (non-dry-run) call to roster-import against TEST fails on
`profile_write_failed` because `desired.external_student_id` is spread into
every profile upsert unconditionally. It went unnoticed because most existing
roster-import drives (`import_year_drive.py`) stub `functions.invoke` and
never reach a real write. Applying that migration to TEST needs a Supabase
PAT or DB password, neither available to this non-interactive session — flag
for Mide. Until it's applied, run this drive against a copy of index.ts with
the `external_student_id` read/write temporarily removed (three spots: the
`existingProfile` select + type, the `desired` object, and the `changed`
comparison) to route around the gap and prove the actual logic under test —
NOT against the committed file, which is correct and unmodified for
production (where the column already exists).

Creates ONE new class (current year, this drive's own) + ONE new class in a
freshly-created past academic year (for the wrong-year refusal), and however
many throwaway auth users the CSV rows create. Everything this script creates
is torn down at the end by a SNAPSHOTTED id list (never a predicate delete).
"""
import json
import os
import re
import shutil
import ssl
import subprocess
import sys
import time
import urllib.error
import urllib.request

REPO = os.path.dirname(os.path.abspath(__file__))
FN_DIR = os.path.join(REPO, "supabase", "functions", "roster-import")
URL = "https://qeppkiswvclkkwbxmlok.supabase.co"
FN = "http://localhost:8000"
SCHOOL = "d0233615-3ee7-4b1b-a8ff-c912c5196d62"
YEAR_2627 = "2f560a43-73b9-422a-8fc7-ec46524a288a"
ADMIN_EMAIL = "mrb326_admin@throwaway.test"
ADMIN_ID = "f3260000-0000-0000-0000-000000000002"
TEACHER_EMAIL = "mrb326_teacher@throwaway.test"
ENV_SWITCH = "MRB_THROWAWAY_PASSWORD"  # same fixture accounts, same switch as teacher_admin_real_drive.py
PW = os.environ.get(ENV_SWITCH)
CTX = ssl.create_default_context(cafile="/etc/ssl/cert.pem")

with open("/Users/midebadmus/Documents/GitHub/mrbadmus---backend/.env", encoding="utf-8") as f:
    SRK = re.search(r"SUPABASE_SERVICE_ROLE_KEY=(\S+)", f.read()).group(1)

# ⊕ MRB-348 r5: read this repo's own config.js. It used to name the absolute path of the
# class-csv-upload worktree, which was pruned after merging, so the gate crashed before driving anything.
with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "shared", "config.js"), encoding="utf-8") as f:
    src = f.read()
    ANON = re.search(r"'(eyJ[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+)'", src[src.index("const TEST"):]).group(1)

created = {"classes": [], "auth_users": [], "profiles": [], "class_members": [], "academic_years": []}
fails = []


def check(ok, what, detail=""):
    print("  %s %s%s" % ("PASS" if ok else "FAIL", what, ("  -- " + detail) if detail else ""))
    if not ok:
        fails.append(what)


def rest(method, path, key, body=None, extra_headers=None, prefer=None):
    headers = {"apikey": key, "Authorization": "Bearer %s" % key, "Content-Type": "application/json"}
    if prefer:
        headers["Prefer"] = prefer
    if extra_headers:
        headers.update(extra_headers)
    data = json.dumps(body).encode() if body is not None else None
    req = urllib.request.Request(URL + path, data=data, headers=headers, method=method)
    try:
        with urllib.request.urlopen(req, timeout=30, context=CTX) as r:
            raw = r.read().decode()
            return r.status, (json.loads(raw) if raw else None)
    except urllib.error.HTTPError as e:
        raw = e.read().decode()
        return e.code, (json.loads(raw) if raw else raw)


def sign_in(email):
    req = urllib.request.Request(
        URL + "/auth/v1/token?grant_type=password",
        data=json.dumps({"email": email, "password": PW}).encode(),
        headers={"apikey": ANON, "Content-Type": "application/json"},
        method="POST")
    with urllib.request.urlopen(req, timeout=30, context=CTX) as r:
        return json.loads(r.read().decode())["access_token"]


def call_fn(jwt, payload):
    req = urllib.request.Request(
        FN, data=json.dumps(payload).encode(),
        headers={"Authorization": "Bearer %s" % jwt, "Content-Type": "application/json"},
        method="POST")
    try:
        with urllib.request.urlopen(req, timeout=30, context=CTX) as r:
            return r.status, json.loads(r.read().decode())
    except urllib.error.HTTPError as e:
        return e.code, json.loads(e.read().decode())


def user_id_for_email(email):
    status, data = rest("POST", "/rest/v1/rpc/user_id_for_email", SRK, {"p_email": email})
    return data if isinstance(data, str) else None


def start_function():
    """Spawns the real edge function locally on :8000, pointed at TEST."""
    proc = subprocess.Popen(
        ["deno", "run", "--allow-net", "--allow-env", "index.ts"],
        cwd=FN_DIR,
        env=dict(os.environ, SUPABASE_URL=URL, SUPABASE_SERVICE_ROLE_KEY=SRK),
        stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
        text=True,
    )
    deadline = time.time() + 30
    while time.time() < deadline:
        if proc.poll() is not None:
            print(proc.stdout.read())
            raise RuntimeError("deno exited before serving — see output above")
        try:
            req = urllib.request.Request(FN, method="OPTIONS")
            with urllib.request.urlopen(req, timeout=2, context=CTX):
                return proc
        except (urllib.error.URLError, ConnectionError):
            time.sleep(0.5)
    proc.kill()
    raise RuntimeError("deno never answered on :8000 within 30s")


def stop_function(proc):
    proc.terminate()
    try:
        proc.wait(timeout=5)
    except subprocess.TimeoutExpired:
        proc.kill()


def run_scenarios():
    print("== setup ==")
    admin_jwt = sign_in(ADMIN_EMAIL)
    teacher_jwt = sign_in(TEACHER_EMAIL)
    print("  signed in as both throwaway accounts")

    try:
        _run_body(admin_jwt, teacher_jwt)
    finally:
        _teardown()


def _run_body(admin_jwt, teacher_jwt):
    # current-year class, this drive's own
    status, cls = rest("POST", "/rest/v1/classes", SRK, {
        "school_id": SCHOOL, "academic_year_id": YEAR_2627, "name": "99Z/CsvTest1",
        "key_stage": "KS4", "year_group": 10, "tier": "higher", "science_pathway": "combined",
    }, prefer="return=representation")
    check(status in (200, 201), "create own TEST class", str((status, cls)))
    class_id = cls[0]["id"]
    created["classes"].append(class_id)

    # a past academic year + a class in it, for the wrong-year refusal
    status, yr = rest("POST", "/rest/v1/academic_years", SRK, {
        "school_id": SCHOOL, "name": "2024-25-csvtest", "start_date": "2024-09-01", "end_date": "2025-08-31",
    }, prefer="return=representation")
    check(status in (200, 201), "create past academic year", str((status, yr)))
    wrong_year_id = yr[0]["id"]
    created["academic_years"].append(wrong_year_id)

    status, cls2 = rest("POST", "/rest/v1/classes", SRK, {
        "school_id": SCHOOL, "academic_year_id": wrong_year_id, "name": "99Z/CsvWrongYear",
        "key_stage": "KS4", "year_group": 10, "tier": "higher", "science_pathway": "combined",
    }, prefer="return=representation")
    check(status in (200, 201), "create wrong-year TEST class", str((status, cls2)))
    wrong_class_id = cls2[0]["id"]
    created["classes"].append(wrong_class_id)

    # pre-existing student account (for the "mixed existing + new" scenario) —
    # created directly, NOT through the CSV pipeline, so the drive proves the
    # pipeline correctly finds-and-attaches an account it did not create.
    pre_email = "csvtest.pre.existing@throwaway.test"
    status, pu = rest("POST", "/auth/v1/admin/users", SRK, {
        "email": pre_email, "email_confirm": True,
    })
    check(status in (200, 201), "pre-create an existing student account", str((status, pu)))
    pre_uid = pu["id"] if isinstance(pu, dict) else pu.get("id")
    created["auth_users"].append(pre_uid)
    status, _ = rest("PATCH", "/rest/v1/profiles?id=eq.%s" % pre_uid, SRK, {
        "role": "student", "school_id": SCHOOL, "key_stage": "KS4",
        "first_name": "Pre", "last_name": "Existing",
    }, prefer="return=minimal")
    check(status in (200, 201, 204), "profile for pre-existing student (PATCH: auth trigger already stubbed the row)")
    created["profiles"].append(pre_uid)

    print("\n== scenario 1: non-admin cannot call it ==")
    payload_probe = {"dryRun": True, "classes": [{"id": class_id, "name": "99Z/CsvTest1"}],
                      "students": [{"rowIndex": 1, "email": "irrelevant@throwaway.test", "className": "99Z/CsvTest1"}]}
    status, resp = call_fn(teacher_jwt, payload_probe)
    check(status == 403 and resp.get("error") == "admin_only", "non-admin refused 403 admin_only", str((status, resp)))

    print("\n== scenario 1b: a REVOKED school_admin scope is refused (regression for the Opus-review finding) ==")
    # staff_scopes is revoked by setting ended_at, never by deleting. The
    # first cut of the admin gate filtered started_at/deleted_at but not
    # ended_at, so an ex-admin whose grant had already ended still passed.
    # ended_at must land strictly after started_at (2026-09-05) or the
    # staff_scopes_window_check constraint refuses the write.
    status, _ = rest("PATCH", "/rest/v1/staff_scopes?profile_id=eq.%s&scope=eq.school_admin" % ADMIN_ID, SRK,
                      {"ended_at": "2026-09-10T00:00:00Z"}, prefer="return=minimal")
    check(status in (200, 204), "expire the admin fixture's school_admin scope")
    status, resp = call_fn(admin_jwt, payload_probe)
    check(status == 403 and resp.get("error") == "admin_only", "revoked school_admin scope refused 403 admin_only", str((status, resp)))
    status, _ = rest("PATCH", "/rest/v1/staff_scopes?profile_id=eq.%s&scope=eq.school_admin" % ADMIN_ID, SRK,
                      {"ended_at": None}, prefer="return=minimal")
    check(status in (200, 204), "restore the admin fixture's school_admin scope")

    print("\n== scenario 2: wrong-year class refused ==")
    payload_wy = {"dryRun": True, "classes": [{"id": wrong_class_id, "name": "99Z/CsvWrongYear"}],
                  "students": [{"rowIndex": 1, "email": "irrelevant2@throwaway.test", "className": "99Z/CsvWrongYear"}]}
    status, resp = call_fn(admin_jwt, payload_wy)
    check(status == 400 and resp.get("error") == "class_wrong_year", "wrong-year class refused", str((status, resp)))

    print("\n== scenario 2b: academicYearName cannot be used to name a class's own wrong year as \"working\" (regression) ==")
    payload_wy_named = dict(payload_wy, academicYearName="2024-25-csvtest")
    status, resp = call_fn(admin_jwt, payload_wy_named)
    check(status == 400 and resp.get("error") == "class_wrong_year",
          "academicYearName override ignored on the id-path; still refused", str((status, resp)))

    print("\n== scenario 3: all-new pupils — create + attach ==")
    new_rows = [
        {"rowIndex": 1, "email": "csvtest.new1@throwaway.test", "firstName": "New", "lastName": "One", "className": "99Z/CsvTest1"},
        {"rowIndex": 2, "email": "csvtest.new2@throwaway.test", "firstName": "New", "lastName": "Two", "className": "99Z/CsvTest1"},
    ]
    payload3 = {"dryRun": False, "classes": [{"id": class_id, "name": "99Z/CsvTest1"}], "students": new_rows}
    status, resp = call_fn(admin_jwt, payload3)
    ok = status == 200 and resp.get("ok") and resp["counts"]["studentsCreated"] == 2 and resp["counts"]["studentsAttached"] == 2
    check(ok, "2 new pupils created + attached", str((status, resp)))
    for r in new_rows:
        uid = user_id_for_email(r["email"])
        if uid:
            created["auth_users"].append(uid)
            created["profiles"].append(uid)

    print("\n== scenario 4: re-upload the SAME csv — zero new duplicates ==")
    status, resp = call_fn(admin_jwt, payload3)
    counts = resp.get("counts", {})
    ok = (status == 200 and resp.get("ok")
          and counts.get("studentsCreated") == 0
          and counts.get("studentsAttached") == 0
          and counts.get("studentsAlreadyAttached") == 2)
    check(ok, "re-upload: 0 created, 0 newly attached, 2 already-attached", str((status, counts)))

    print("\n== scenario 5: mixed existing-account + new pupil ==")
    mixed_rows = [
        {"rowIndex": 1, "email": pre_email, "firstName": "Pre", "lastName": "Existing", "className": "99Z/CsvTest1"},
        {"rowIndex": 2, "email": "csvtest.new3@throwaway.test", "firstName": "New", "lastName": "Three", "className": "99Z/CsvTest1"},
    ]
    payload5 = {"dryRun": False, "classes": [{"id": class_id, "name": "99Z/CsvTest1"}], "students": mixed_rows}
    status, resp = call_fn(admin_jwt, payload5)
    counts5 = resp.get("counts", {})
    ok = (status == 200 and resp.get("ok")
          and counts5.get("studentsCreated") == 1
          and counts5.get("studentsAttached") == 2)
    check(ok, "mixed: 1 created, 2 attached (1 pre-existing account + 1 new)", str((status, counts5)))
    uid3 = user_id_for_email("csvtest.new3@throwaway.test")
    if uid3:
        created["auth_users"].append(uid3)
        created["profiles"].append(uid3)

    print("\n== verify: no duplicate auth users / profiles after the re-upload ==")
    all_emails = [r["email"] for r in new_rows] + [pre_email, "csvtest.new3@throwaway.test"]
    dup_found = False
    for email in all_emails:
        uid = user_id_for_email(email)
        # user_id_for_email returns a single id (or null) by construction — a
        # non-null scalar here already proves "exactly one", since the RPC
        # cannot return more than one row. Cross-check profiles count too.
        status2, profs = rest("GET", "/rest/v1/profiles?id=eq.%s&select=id" % uid, SRK)
        if not isinstance(profs, list) or len(profs) != 1:
            dup_found = True
    check(not dup_found, "no duplicate profiles for any of the 4 CSV-touched emails")

    status, members = rest("GET", "/rest/v1/class_members?class_id=eq.%s&select=id,student_id&deleted_at=is.null&left_at=is.null" % class_id, SRK)
    member_ids = {m["student_id"] for m in members} if isinstance(members, list) else set()
    expected = {user_id_for_email(e) for e in all_emails}
    check(member_ids == expected, "class_members has exactly the 4 expected students, no dupes", str(member_ids))
    for m in members:
        created["class_members"].append(m["id"])


def _teardown():
    print("\n== teardown (by snapshotted id list) ==")
    for cm_id in created["class_members"]:
        rest("DELETE", "/rest/v1/class_members?id=eq.%s" % cm_id, SRK)
    for uid in created["profiles"]:
        rest("DELETE", "/rest/v1/profiles?id=eq.%s" % uid, SRK)
    for uid in created["auth_users"]:
        rest("DELETE", "/auth/v1/admin/users/%s" % uid, SRK)
    for cid in created["classes"]:
        rest("DELETE", "/rest/v1/classes?id=eq.%s" % cid, SRK)
    for yid in created["academic_years"]:
        rest("DELETE", "/rest/v1/academic_years?id=eq.%s" % yid, SRK)
    print("  torn down: %d class_members, %d profiles, %d auth users, %d classes, %d academic_years" % (
        len(created["class_members"]), len(created["profiles"]), len(created["auth_users"]),
        len(created["classes"]), len(created["academic_years"])))


def main():
    if not PW:
        print("SKIP — %s not set (see teacher_admin_real_drive.py's ENV_SWITCH)" % ENV_SWITCH)
        sys.exit(0)
    if not shutil.which("deno"):
        print("SKIP — deno not on PATH (brew install deno); this drive runs "
              "the real edge function file locally, not a stub")
        sys.exit(0)

    proc = start_function()
    try:
        run_scenarios()
    finally:
        stop_function(proc)

    print("\n== result ==")
    if fails:
        print("FAILED: %s" % fails)
        sys.exit(1)
    print("ALL PASS")


if __name__ == "__main__":
    main()
