#!/usr/bin/env python3
"""sandbox_class_check.py — the `sandbox_class` fast gate (27 Nov 2026).

8r/Sc1 stopped being the production sandbox on 16 Nov 2026: it is Mide's real
Year 8 class. The sandbox is now "Test class (Mr Badmus)", named once, in
sandbox_class.py. This gate fails the push if:

  1. the guard's decision is wrong on any of its shapes — the sandbox shape
     allowed; a stranger pupil, a stranger teacher, no pupils (8r/Sc1's own
     shape today), a deleted class and a missing class all refused;
  2. assert_writable() lets a retired id through on ANY project, or lets a
     production write through with no key to prove membership with;
  3. guard_request() misses a class id in a write's body or query string, or
     guards a read;
  4. any tracked script spells the retired 8r/Sc1 id, or the sandbox id
     anywhere but sandbox_class.py (one shared constant, never copied);
  5. a script reads MRB_DRIVE_CLASS without running assert_writable(), or the
     shared live client (tools/mrb351_acceptance.py Client._req) stops
     calling guard_request();
  6. the SQL read and the REST read stop applying the same active-row filters.

No network. Reads the tree with `git ls-files`.
"""

import inspect
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ROOT)
sys.path.insert(0, os.path.join(ROOT, "tools"))
import config_env  # noqa: E402
import sandbox_class as S  # noqa: E402

FAILS = []
PASSES = [0]


def check(ok, msg):
    if ok:
        PASSES[0] += 1
    else:
        FAILS.append(msg)
        print("  FAIL  " + msg)


def refused(fn, *a, **k):
    try:
        fn(*a, **k)
    except S.SandboxRefused:
        return True
    return False


SID = S.SANDBOX_CLASS_ID
RETIRED = next(iter(S.RETIRED))
OTHER = "00000000-0000-4000-8000-00000000c1a5"
MIDE, ANI = sorted(S.TEST_PUPILS)
TEACHER = next(iter(S.SANDBOX_TEACHERS))
TEST_URL = config_env.TEST["SUPABASE_URL"]
PROD_URL = config_env.PROD["SUPABASE_URL"]


def row(pupils, teachers=(), deleted=False, name="x"):
    return {"name": name, "deleted": deleted, "pupils": list(pupils),
            "teachers": list(teachers)}


# 1 — the decision
check(S.decide(SID, row([MIDE, ANI], [TEACHER])) is None,
      "the sandbox shape (two test pupils, Mr Badmus) is allowed")
check(S.decide(OTHER, row([MIDE.upper()])) is None,
      "a test pupil is matched case-insensitively")
check(refused(S.decide, OTHER, row([MIDE, "pupil@school.uk"])),
      "a class with one non-test pupil is refused")
check(refused(S.decide, OTHER, row([MIDE], [TEACHER, "colleague@school.uk"])),
      "a class with a teacher other than the sandbox teacher is refused")
check(refused(S.decide, OTHER, row([], [TEACHER, "colleague@school.uk"])),
      "8r/Sc1's shape today (no pupils, two real teachers) is refused")
check(refused(S.decide, OTHER, row([])), "an empty class is refused")
check(refused(S.decide, OTHER, row([MIDE], deleted=True)), "a deleted class is refused")
check(refused(S.decide, OTHER, None), "a class that cannot be read is refused")
check(refused(S.decide, RETIRED, row([MIDE])),
      "the retired 8r/Sc1 id is refused even with sandbox-shaped members")

# 2 — assert_writable
check(refused(S.assert_writable, RETIRED, TEST_URL),
      "retired id refused on TEST, no key")
check(refused(S.assert_writable, RETIRED, PROD_URL, "k"),
      "retired id refused on production")
check(refused(S.assert_writable, SID, PROD_URL),
      "production write with no service key is refused (fails closed)")
check(refused(S.assert_writable, SID, "https://elsewhere.example/"),
      "an unknown project is treated as production")
check(S.assert_writable(OTHER, TEST_URL) == OTHER,
      "a TEST write to a TEST class passes (TEST drives mint throwaways)")
check(refused(S.assert_writable, OTHER, TEST_URL, None, True),
      "enforce=True on TEST with no key is refused")
_old = os.environ.get("MRB_SANDBOX_ENFORCE")
os.environ["MRB_SANDBOX_ENFORCE"] = "1"
check(S.enforced(TEST_URL), "MRB_SANDBOX_ENFORCE=1 turns enforcement on for TEST")
if _old is None:
    del os.environ["MRB_SANDBOX_ENFORCE"]
else:
    os.environ["MRB_SANDBOX_ENFORCE"] = _old
# A production check that reads membership: stub the fetch, prove decide() runs.
_real = S.fetch_membership
try:
    S.fetch_membership = lambda c, u, k: row([MIDE, "pupil@school.uk"])
    check(refused(S.assert_writable, SID, PROD_URL, "k"),
          "production: a fetched non-test pupil is refused")
    S.fetch_membership = lambda c, u, k: row([MIDE, ANI], [TEACHER])
    check(S.assert_writable(SID, PROD_URL, "k") == SID,
          "production: the fetched sandbox shape is allowed")

    def boom(c, u, k):
        raise S.urllib.error.URLError("down")
    S.fetch_membership = boom
    check(refused(S.assert_writable, SID, PROD_URL, "k"),
          "production: a membership read that fails is refused")
finally:
    S.fetch_membership = _real

# 3 — guard_request
check(S.class_ids_in({"rows": [{"class_id": "a"}], "p_class_ids": ["b", "a"]},
                     "https://h/rest/v1/class_members?class_id=eq." + RETIRED)
      == ["a", "b", RETIRED], "class ids found in nested body and query string")
check(S.class_ids_in(None, "https://h/rest/v1/classes?id=in.(%s)" % RETIRED) == [RETIRED],
      "an id= filter on /classes is a class id")
check(S.guard_request("GET", "https://h/rest/v1/x?class_id=eq." + RETIRED, None, TEST_URL)
      is None, "reads are not guarded")
check(refused(S.guard_request, "PATCH", "https://h/rest/v1/x?class_id=eq." + RETIRED,
              {}, TEST_URL), "a PATCH filtered on the retired id is refused")
check(refused(S.guard_request, "POST", "https://h/rest/v1/rpc/x",
              {"p_class_ids": [OTHER, RETIRED]}, TEST_URL),
      "an RPC naming the retired id among others is refused")

# 4 — the tree
files = subprocess.run(["git", "ls-files"], cwd=ROOT, capture_output=True,
                       text=True, check=True).stdout.split()
CODE = (".py", ".sh", ".js", ".mjs", ".cjs", ".ts", ".html", ".json", ".sql")
SKIP = ("docs/", "mrbadmus_site/", "supabase/migrations/", "supabase/data-ops/")
OWN = {"sandbox_class.py", "sandbox_class_check.py"}
for f in files:
    if not f.endswith(CODE) or f.startswith(SKIP) or f in OWN:
        continue
    try:
        src = open(os.path.join(ROOT, f), encoding="utf-8", errors="replace").read()
    except OSError:
        continue
    check(RETIRED not in src, "%s spells the retired 8r/Sc1 id" % f)
    check(SID not in src, "%s copies the sandbox id; import sandbox_class" % f)
    if f.endswith(".py") and re.search(r"environ(?:\.get\(|\[)\s*['\"]MRB_DRIVE_CLASS", src):
        check("sandbox_class.assert_writable(" in src,
              "%s reads MRB_DRIVE_CLASS but never runs assert_writable()" % f)

# 5 — the shared live client
import mrb351_acceptance as acc  # noqa: E402
check("sandbox_class.guard_request(" in inspect.getsource(acc.Client._req),
      "tools/mrb351_acceptance.py Client._req calls sandbox_class.guard_request()")
check(refused(acc.Client(TEST_URL, "a", "s").write, "assignments", "POST",
              {"class_id": RETIRED}), "the shared client refuses a write to 8r/Sc1")

# 6 — the two reads agree
sql = S.membership_sql(SID)
rest = inspect.getsource(S.fetch_membership)
for sql_f, rest_f in (("m.left_at is null", "left_at=is.null"),
                      ("m.deleted_at is null", "deleted_at=is.null"),
                      ("t.ended_at > now()", "ended_at.gt.now()"),
                      ("t.deleted_at is null", "deleted_at=is.null")):
    check(sql_f in sql and rest_f in rest,
          "both reads apply the filter %r / %r" % (sql_f, rest_f))

print("\nsandbox_class: %d passed, %d failed" % (PASSES[0], len(FAILS)))
sys.exit(1 if FAILS else 0)
