#!/usr/bin/env python3
"""MRB-348 WS-3 — consolidate multiple permissive RLS policies.

WHAT THIS IS FOR
================
Supabase's performance linter raises `multiple_permissive_policies` once per
(table, role, command) cell that has more than one PERMISSIVE policy. On
production that is 251 findings. The estate grants almost every policy to the
role `public`, and the linter expands `public` across the 4-5 concrete roles,
so "5 permissive SELECT policies on classes" is reported 20 times.

Permissive policies are OR'd, and Postgres evaluates every branch until one is
true. Folding a cell's policies into ONE policy, with the CHEAP self-check
written FIRST, is the win: the same boolean, short-circuiting earlier, and the
linter finding goes away.

THE TRANSFORM, PRECISELY
========================
Step 1 — normalise ALL.  A PERMISSIVE policy with cmd='ALL' also applies to
  SELECT, and cannot be folded into a SELECT-only policy without losing its
  write coverage. Each ALL policy is first expanded into four per-command
  equivalents:
      SELECT  USING (qual)
      DELETE  USING (qual)
      UPDATE  USING (qual) WITH CHECK (with_check IF PRESENT ELSE qual)
      INSERT  WITH CHECK (with_check IF PRESENT ELSE qual)
  ⚠️ That `ELSE qual` is load-bearing Postgres semantics, not a convenience:
  when an ALL/UPDATE/INSERT policy carries no WITH CHECK, Postgres uses the
  USING expression as the check. Dropping it would silently widen who may
  write; substituting `true` would widen it further still.

Step 2 — merge per (table, command).
      merged USING      = OR over every policy's USING      (SELECT/UPDATE/DELETE)
      merged WITH CHECK = OR over every policy's EFFECTIVE check (INSERT/UPDATE)
  where effective check = with_check if present else qual.

  ⚠️ WHY OR-ING THE TWO CLAUSES SEPARATELY IS EXACT, AND NOT AN APPROXIMATION.
  For an UPDATE under several permissive policies, Postgres requires the OLD
  row to satisfy at least one policy's USING and the NEW row to satisfy at
  least one policy's WITH CHECK -- and they need NOT be the same policy. So
  (U1 OR U2) with (C1 OR C2) is precisely the original behaviour. If Postgres
  had instead required one policy to satisfy both, this merge would be a real
  widening and the whole transform would be unsound.

Step 3 — order the branches cheapest first, so the OR short-circuits early:
      0  pure column predicate, no auth call at all
      1  bare self-check      <col> = (SELECT auth_user_id()) / (SELECT auth.uid()) = <col>
      2  request-constant     auth_user_has_scope('..'), auth_user_operator_active(), ...
      3  school equality      school_id = (SELECT auth_user_school_id())
      4  row-dependent call   auth_user_teaches_class(..), auth_user_is_member_of_class(..), ...
      5  EXISTS (...)         always last
  A composite branch takes the cost of its MOST EXPENSIVE component. Ties keep
  the original catalogue order, so the output is byte-reproducible.

Step 4 — what is deliberately NOT touched:
  * any RESTRICTIVE policy. Restrictive policies AND rather than OR; folding one
    into the OR would be a real security change, not a performance one. A table
    carrying any restrictive policy is skipped WHOLE, and named in the report.
  * any policy granted to a role other than `public`. Merging across differing
    GRANT sets changes who the policy reaches.
  * anything whose expression this tool cannot round-trip (Proof A below).

THE PROOFS
==========
Proof A  inverse transform, static and offline. Every generated merged
         expression is split back into its top-level OR branches with a real
         paren- and literal-aware scanner (NOT a regex on " OR ", which would
         happily split inside a string literal or a nested subquery), and the
         multiset of recovered branches must equal the multiset of the original
         per-policy expressions. Runs before anything is applied.
Proof B  visibility digest, dynamic, on TEST. Real users spanning every role
         sign in with the ANON key so RLS actually applies, and every affected
         table's full visible row set is hashed. Before vs after must match.
         ⚠️ A cell that is empty before and empty after proves nothing, so
         non-empty cells are counted and reported separately.
Proof C  rollback. Restores the exact original policies from the backup table,
         after which Proof B is re-run against the original baseline.

⚠️ PRODUCTION IS NOT A TARGET OF THIS SCRIPT. The ref is proven by decoding the
`ref` claim out of the service-role JWT -- never read off a label, a filename or
a --project flag, because those are what get mixed up. See `resolve_project`.

CLI
    --project test|prod     which credential set to load
    --check                 Proof A only
    --emit                  write the forward migration and its rollback
    --apply / --rollback    execute against the resolved project
    --verify-visibility     Proof B; use with --phase before|after|rolled-back
    --compare A B           diff two Proof B captures
"""

from __future__ import annotations

import argparse
import base64
import datetime as _dt
import hashlib
import json
import os
import re
import ssl
import sys
import time
import urllib.error
import urllib.request
from collections import defaultdict

# ---------------------------------------------------------------------------
# Project identity. Proven, never labelled.
# ---------------------------------------------------------------------------

PROD_REF = "urklkrwevjtlfbwnipjn"
TEST_REF = "qeppkiswvclkkwbxmlok"

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BACKEND_ENV = os.path.join(
    os.path.dirname(REPO), "mrbadmus---backend", ".env"
)

# The framework Python on this machine ships a trust store that fails against
# Supabase; every script in this repo pins the system bundle instead.
SSL_CTX = ssl.create_default_context(cafile="/etc/ssl/cert.pem")


def jwt_ref(token: str) -> str:
    """Read the project ref out of a Supabase JWT's payload.

    ⚠️ This is the ONLY thing allowed to decide which project we are pointed at.
    On 9 Sep 2026 TEST and production held identical row counts in both question
    banks, so no count and no glance at a table could tell them apart -- the
    key's own `ref` claim could. A label sitting beside a credential is not
    evidence about the credential.
    """
    try:
        payload = token.split(".")[1]
        payload += "=" * (-len(payload) % 4)
        return json.loads(base64.urlsafe_b64decode(payload))["ref"]
    except Exception as exc:  # noqa: BLE001
        raise SystemExit(f"cannot decode project ref from JWT: {exc}")


def _read_env_file(path: str) -> dict:
    out = {}
    if not os.path.exists(path):
        return out
    with open(path) as fh:
        for line in fh:
            line = line.strip()
            if "=" in line and not line.startswith("#"):
                k, v = line.split("=", 1)
                out[k.strip()] = v.strip().strip('"').strip("'")
    return out


def anon_key_for_test() -> str:
    """Pull the TEST anon key out of shared/config.js.

    ⚠️ THE TRAP: production's anon key appears FIRST in that file. A naive
    first-match regex gets you production's key, which then 401s against TEST
    and reads exactly like a wrong password. Slice from `const TEST` onward.
    """
    src = open(os.path.join(REPO, "shared", "config.js")).read()
    idx = src.index("const TEST")
    m = re.search(r"ey[A-Za-z0-9_\-]+\.[A-Za-z0-9_\-]+\.[A-Za-z0-9_\-]+", src[idx:])
    if not m:
        raise SystemExit("no anon JWT found after `const TEST` in shared/config.js")
    return m.group(0)


def resolve_project(which: str, i_am_sure_production: bool):
    """Return (url, service_key, anon_key, ref), refusing production by default.

    The refusal keys off the DECODED ref, not off `which`. That is deliberate:
    if someone repoints the backend .env at production and still passes
    `--project test`, the label is wrong and the JWT is right.
    """
    if which == "test":
        env = _read_env_file(BACKEND_ENV)
        url = env.get("SUPABASE_URL")
        service = env.get("SUPABASE_SERVICE_ROLE_KEY")
        if not url or not service:
            raise SystemExit(f"SUPABASE_URL / SUPABASE_SERVICE_ROLE_KEY missing from {BACKEND_ENV}")
        anon = anon_key_for_test()
    else:
        url = os.environ.get("MRB_PROD_URL")
        service = os.environ.get("MRB_PROD_SERVICE_KEY")
        anon = os.environ.get("MRB_PROD_ANON_KEY", "")
        if not url or not service:
            raise SystemExit(
                "--project prod needs MRB_PROD_URL and MRB_PROD_SERVICE_KEY in the "
                "environment. They are deliberately not stored in this repo."
            )

    ref = jwt_ref(service)
    if ref == PROD_REF and not i_am_sure_production:
        raise SystemExit(
            "REFUSING: the service-role key's own `ref` claim says this is PRODUCTION\n"
            f"  ref decoded from the JWT : {ref}\n"
            f"  --project said           : {which}\n"
            "MRB-348 rehearses on TEST. Pass --i-am-sure-production only if a human\n"
            "has ruled this production write in the prompt, per CLAUDE.md."
        )
    if which == "test" and ref != TEST_REF:
        raise SystemExit(f"REFUSING: --project test but the JWT ref is {ref!r}, not TEST")

    # anon key must agree with the service key about which project this is
    if anon:
        aref = jwt_ref(anon)
        if aref != ref:
            raise SystemExit(
                f"REFUSING: anon key ref {aref!r} != service key ref {ref!r}. "
                "This is the shared/config.js first-match trap."
            )
    return url, service, anon, ref


# ---------------------------------------------------------------------------
# Transport
# ---------------------------------------------------------------------------


class Api:
    def __init__(self, url, service, anon):
        self.url, self.service, self.anon = url, service, anon

    def _req(self, path, *, method="GET", body=None, key=None, bearer=None, headers=None):
        key = key or self.service
        h = {
            "apikey": key,
            "Authorization": "Bearer " + (bearer or key),
            "Content-Type": "application/json",
        }
        h.update(headers or {})
        # ⚠️ Retry transients. A single read timeout part-way through Proof B
        # otherwise kills the whole capture and loses every cell already
        # measured -- which reads exactly like a failed proof when it is only a
        # dropped socket. A transport error is not evidence about RLS. An HTTP
        # status IS a real answer and is never retried.
        last = None
        for attempt in range(4):
            req = urllib.request.Request(
                self.url + path,
                method=method,
                data=json.dumps(body).encode() if body is not None else None,
                headers=h,
            )
            try:
                r = urllib.request.urlopen(req, context=SSL_CTX, timeout=180)
                return r.status, r.read(), dict(r.headers)
            except urllib.error.HTTPError as e:
                return e.code, e.read(), dict(e.headers)
            except (urllib.error.URLError, TimeoutError, OSError) as e:
                last = e
                if attempt < 3:
                    time.sleep(2 ** attempt)
        raise SystemExit(f"transport failed after 4 attempts on {path}: {last}")

    def sql(self, query):
        """Arbitrary SELECT via the temporary MRB-348 rehearsal RPC."""
        st, data, _ = self._req(
            "/rest/v1/rpc/mrb348_exec_sql", method="POST", body={"query": query}
        )
        if st != 200:
            raise SystemExit(f"sql failed {st}: {data[:500].decode(errors='replace')}\n{query[:400]}")
        return json.loads(data)

    def ddl(self, stmt):
        st, data, _ = self._req(
            "/rest/v1/rpc/mrb348_exec_ddl", method="POST", body={"stmt": stmt}
        )
        if st != 200:
            raise SystemExit(f"ddl failed {st}: {data[:800].decode(errors='replace')}\n{stmt[:600]}")
        return json.loads(data)

    def sign_in(self, email, password):
        st, data, _ = self._req(
            "/auth/v1/token?grant_type=password",
            method="POST",
            body={"email": email, "password": password},
            key=self.anon,
        )
        if st != 200:
            return None
        return json.loads(data)["access_token"]

    def select_as(self, token, table, order_cols):
        order = ",".join(f"{c}.asc" for c in order_cols) if order_cols else None
        path = f"/rest/v1/{table}?select=*"
        if order:
            path += f"&order={order}"
        st, data, _ = self._req(path, key=self.anon, bearer=token)
        return st, data


# ---------------------------------------------------------------------------
# SQL expression scanning -- paren, string-literal and identifier aware.
# ---------------------------------------------------------------------------


class Unparseable(Exception):
    """Raised when an expression uses syntax this scanner will not risk."""


def _skip_literal(expr, i):
    """Advance past a quoted literal starting at expr[i]. Returns new index."""
    ch = expr[i]
    n = len(expr)
    if ch == "'":
        i += 1
        while i < n:
            if expr[i] == "'":
                if i + 1 < n and expr[i + 1] == "'":  # doubled quote escape
                    i += 2
                    continue
                return i + 1
            i += 1
        raise Unparseable("unterminated single-quoted literal")
    if ch == '"':
        i += 1
        while i < n:
            if expr[i] == '"':
                if i + 1 < n and expr[i + 1] == '"':
                    i += 2
                    continue
                return i + 1
            i += 1
        raise Unparseable("unterminated double-quoted identifier")
    raise AssertionError


def _word_at(expr, i, word):
    """True if `word` sits at expr[i] as a whole word, case-insensitive."""
    n = len(expr)
    w = len(word)
    if expr[i : i + w].upper() != word:
        return False
    if i > 0 and (expr[i - 1].isalnum() or expr[i - 1] == "_"):
        return False
    j = i + w
    if j < n and (expr[j].isalnum() or expr[j] == "_"):
        return False
    return True


def split_top_level_or(expr):
    """Split an SQL boolean on its TOP-LEVEL `OR`s.

    ⚠️ Deliberately not a regex on " OR ". A regex splits inside string
    literals ('a OR b'), inside nested parens, and inside identifiers, and each
    of those would make the round-trip proof pass for the wrong reason.
    """
    if "$" in expr:
        # dollar-quoting would need tag tracking; refuse rather than guess.
        raise Unparseable("expression contains '$' (possible dollar-quoting)")
    parts, depth, start, i, n = [], 0, 0, 0, len(expr)
    while i < n:
        ch = expr[i]
        if ch in "'\"":
            i = _skip_literal(expr, i)
            continue
        if ch == "(":
            depth += 1
            i += 1
            continue
        if ch == ")":
            depth -= 1
            if depth < 0:
                raise Unparseable("unbalanced parentheses")
            i += 1
            continue
        if depth == 0 and ch in "oO" and _word_at(expr, i, "OR"):
            parts.append(expr[start:i])
            start = i + 2
            i += 2
            continue
        i += 1
    if depth != 0:
        raise Unparseable("unbalanced parentheses")
    parts.append(expr[start:])
    return [p.strip() for p in parts if p.strip()]


def strip_outer_parens(expr):
    """Remove ONE enclosing paren pair, if it genuinely encloses the whole expr."""
    e = expr.strip()
    if not e.startswith("(") or not e.endswith(")"):
        return e
    depth, i, n = 0, 0, len(e)
    while i < n:
        ch = e[i]
        if ch in "'\"":
            i = _skip_literal(e, i)
            continue
        if ch == "(":
            depth += 1
        elif ch == ")":
            depth -= 1
            if depth == 0:
                # the opening paren closes here; only strippable if that is the end
                return e[1:-1].strip() if i == n - 1 else e
        i += 1
    return e


def norm_ws(expr):
    """Collapse whitespace so deparsed newlines/indentation cannot fake a diff."""
    return re.sub(r"\s+", " ", (expr or "").strip())


# ---------------------------------------------------------------------------
# Step 3 -- branch cost
# ---------------------------------------------------------------------------

ROW_DEPENDENT = (
    "auth_user_teaches_class",
    "auth_user_is_member_of_class",
    "auth_user_is_hod_of_dept",
    "auth_user_is_hod_of_subject_dept",
    "auth_user_is_subject_teacher_of_class",
    "class_school_id",
    "submission_class_id",
    "submission_student_id",
    "parent_owns_child",
    "guardian_of_child",
)
REQUEST_CONSTANT = (
    "auth_user_has_scope",
    "auth_user_operator_active",
    "auth_user_is_platform_operator",
    "auth_user_role",
    "auth_user_department",
    "auth_user_id",
    "auth.uid",
    "auth.role",
    "auth.jwt",
)

# `(SELECT auth.uid() AS uid) = id` / `id = (SELECT auth_user_id() AS ...)`
_UID_CALL = r"\(\s*SELECT\s+(?:auth\.uid|auth_user_id)\(\)(?:\s+AS\s+\w+)?\s*\)"
_COL = r"[\w.]+"
SELF_CHECK = re.compile(
    rf"^(?:{_UID_CALL}\s*=\s*{_COL}|{_COL}\s*=\s*{_UID_CALL})$", re.I
)


def branch_cost(expr):
    """Cost tier of one OR branch; a composite takes its dearest component."""
    bare = norm_ws(strip_outer_parens(expr))
    if SELF_CHECK.match(bare):
        return 1
    costs = []
    if re.search(r"\bEXISTS\s*\(", bare, re.I):
        costs.append(5)
    for fn in ROW_DEPENDENT:
        if re.search(rf"\b{re.escape(fn)}\s*\(", bare):
            costs.append(4)
            break
    if re.search(r"\bauth_user_school_id\s*\(", bare):
        costs.append(3)
    for fn in REQUEST_CONSTANT:
        if re.search(rf"{re.escape(fn)}\s*\(", bare):
            costs.append(2)
            break
    return max(costs) if costs else 0


# ---------------------------------------------------------------------------
# Steps 1 + 2 -- expand ALL, then plan the merges
# ---------------------------------------------------------------------------

CMDS = ("SELECT", "INSERT", "UPDATE", "DELETE")


def load_policies(api):
    return api.sql(
        "select schemaname, tablename, policyname, permissive, roles::text as roles, "
        "cmd, qual, with_check from pg_policies where schemaname='public' "
        "order by tablename, policyname"
    )


def expand(policy):
    """Step 1. Yield (cmd, using, check) entries for one policy.

    For a non-ALL policy this is the policy itself. For ALL it is the four
    per-command equivalents -- see the module docstring on why `ELSE qual`.
    """
    q, wc, cmd = policy["qual"], policy["with_check"], policy["cmd"]
    if cmd == "ALL":
        eff = wc if wc is not None else q
        return [
            ("SELECT", q, None),
            ("DELETE", q, None),
            ("UPDATE", q, eff),
            ("INSERT", None, eff),
        ]
    if cmd == "INSERT":
        return [("INSERT", None, wc if wc is not None else q)]
    if cmd == "UPDATE":
        return [("UPDATE", q, wc if wc is not None else q)]
    return [(cmd, q, None)]


def build_plan(policies):
    """Return (plan, skips). plan[table] -> {'drop': [...], 'create': [...]}"""
    skips = []
    by_table = defaultdict(list)
    for p in policies:
        by_table[p["tablename"]].append(p)

    # Step 4 -- refusals, decided per table before any merging.
    eligible = {}
    for table, pols in by_table.items():
        restrictive = [p for p in pols if p["permissive"] != "PERMISSIVE"]
        if restrictive:
            skips.append(
                {
                    "table": table,
                    "scope": "whole table",
                    "reason": "carries RESTRICTIVE policies, which AND rather than OR; "
                    "folding them into the OR would be a security change",
                    "policies": [p["policyname"] for p in restrictive],
                }
            )
            continue
        pub, nonpub = [], []
        for p in pols:
            (pub if p["roles"] == "{public}" else nonpub).append(p)
        for p in nonpub:
            skips.append(
                {
                    "table": table,
                    "scope": p["policyname"],
                    "reason": f"granted to {p['roles']}, not {{public}}; merging across "
                    "differing GRANT sets would change who the policy reaches",
                    "policies": [p["policyname"]],
                }
            )
        eligible[table] = pub

    plan = {}
    for table, pols in eligible.items():
        # expand every eligible policy into per-command entries
        entries = defaultdict(list)  # cmd -> [(policy, using, check)]
        for p in pols:
            for cmd, using, check in expand(p):
                entries[cmd].append((p, using, check))

        # which cells are actually multi-permissive?
        multi_cmds = {c for c, v in entries.items() if len(v) > 1}
        if not multi_cmds:
            continue

        # ⚠️ A policy caught by ONE multi cell must be dropped, and then EVERY
        # command it covered has to be reconstructed -- otherwise dropping an
        # ALL policy to merge its SELECT branch silently destroys its INSERT,
        # UPDATE and DELETE coverage. This is the trap the whole plan turns on.
        in_scope = set()
        for c in multi_cmds:
            for p, _u, _k in entries[c]:
                in_scope.add(p["policyname"])

        drop = [p for p in pols if p["policyname"] in in_scope]
        unprovable = None
        create = []
        for cmd in CMDS:
            rows = [(p, u, k) for (p, u, k) in entries.get(cmd, []) if p["policyname"] in in_scope]
            if not rows:
                continue
            try:
                merged = merge_cell(table, cmd, rows)
            except Unparseable as exc:
                unprovable = f"{cmd}: {exc}"
                break
            create.append(merged)
        if unprovable:
            skips.append(
                {
                    "table": table,
                    "scope": "whole table",
                    "reason": f"expression could not be scanned safely ({unprovable})",
                    "policies": sorted(in_scope),
                }
            )
            continue
        plan[table] = {"drop": drop, "create": create}
    return plan, skips


def _ordered_branches(rows, which):
    """Collect, cost-order and de-duplicate the branches of one clause."""
    out = []
    for idx, (p, using, check) in enumerate(rows):
        expr = using if which == "using" else check
        if expr is None:
            continue
        out.append({"policy": p["policyname"], "expr": expr, "cost": branch_cost(expr), "idx": idx})
    out.sort(key=lambda b: (b["cost"], b["idx"]))
    return out


def merge_cell(table, cmd, rows):
    """Step 2 + 3. Build the merged policy for one (table, cmd) cell."""
    name = f"{table}_{cmd.lower()}_merged"
    using_branches = _ordered_branches(rows, "using") if cmd != "INSERT" else []
    check_branches = _ordered_branches(rows, "check") if cmd in ("INSERT", "UPDATE") else []

    def join(branches):
        if not branches:
            return None
        # every branch is individually parenthesised, so the top-level split in
        # Proof A recovers exactly one branch per piece
        return "\n    OR ".join(f"({b['expr']})" for b in branches)

    merged = {
        "table": table,
        "cmd": cmd,
        "name": name,
        "using": join(using_branches),
        "check": join(check_branches),
        "using_branches": using_branches,
        "check_branches": check_branches,
        "sources": [p["policyname"] for p, _u, _k in rows],
    }
    # Proof A is run here too, at build time, so an unprovable merge never even
    # reaches the emitter.
    proof_a_one(merged)
    return merged


# ---------------------------------------------------------------------------
# Proof A -- inverse transform
# ---------------------------------------------------------------------------


def proof_a_one(merged):
    """Assert the merged clause splits back into exactly its source branches."""
    for clause in ("using", "check"):
        expr = merged[clause]
        if expr is None:
            continue
        originals = [norm_ws(b["expr"]) for b in merged[clause + "_branches"]]
        pieces = split_top_level_or(expr)
        recovered = [norm_ws(strip_outer_parens(p)) for p in pieces]
        if sorted(recovered) != sorted(originals):
            raise Unparseable(
                f"round-trip failed on {merged['table']}.{merged['cmd']} {clause}: "
                f"{len(recovered)} recovered vs {len(originals)} original"
            )
    return True


def proof_a(plan):
    failures, checked, branches = [], 0, 0
    for table, spec in sorted(plan.items()):
        for merged in spec["create"]:
            for clause in ("using", "check"):
                if merged[clause] is None:
                    continue
                checked += 1
                originals = [norm_ws(b["expr"]) for b in merged[clause + "_branches"]]
                branches += len(originals)
                try:
                    recovered = [
                        norm_ws(strip_outer_parens(p))
                        for p in split_top_level_or(merged[clause])
                    ]
                except Unparseable as exc:
                    failures.append(f"{table}.{merged['cmd']}.{clause}: {exc}")
                    continue
                if sorted(recovered) != sorted(originals):
                    failures.append(
                        f"{table}.{merged['cmd']}.{clause}: multiset mismatch "
                        f"({len(recovered)} vs {len(originals)})"
                    )
    return {"clauses_checked": checked, "branches_checked": branches, "failures": failures}


# ---------------------------------------------------------------------------
# Emitters
# ---------------------------------------------------------------------------


def sql_lit(s):
    if s is None:
        return "null"
    return "$mrb348$" + s + "$mrb348$"


def emit_forward(plan, skips, ref, generated_at):
    n_drop = sum(len(v["drop"]) for v in plan.values())
    n_create = sum(len(v["create"]) for v in plan.values())
    L = []
    A = L.append
    A("-- MRB-348 WS-3 — consolidate multiple permissive RLS policies.")
    A("-- A PERFORMANCE migration with NO semantic change.")
    A("--")
    A("-- " + "=" * 74)
    A("-- WHAT WAS WRONG")
    A("-- " + "=" * 74)
    A("-- Supabase's performance linter raises `multiple_permissive_policies` once")
    A("-- per (table, role, command) cell holding more than one PERMISSIVE policy.")
    A("-- Production reports 251 findings. Nearly every policy on this estate is")
    A("-- granted to `public`, and the linter expands `public` across the 4-5")
    A("-- concrete roles, so ONE table with 5 permissive SELECT policies is")
    A("-- reported 20 times.")
    A("--")
    A("-- Permissive policies are OR'd, and Postgres walks every branch until one")
    A("-- is true. MRB-347 made each branch cheap by hoisting the per-request auth")
    A("-- calls into InitPlans; it did not reduce the NUMBER of branches, nor fix")
    A("-- their order. This migration does both: one policy per (table, command),")
    A("-- with the cheapest branch written first.")
    A("--")
    A("-- " + "=" * 74)
    A("-- THE TRANSFORM")
    A("-- " + "=" * 74)
    A("-- Step 1. Every PERMISSIVE cmd='ALL' policy is expanded into four")
    A("--   per-command equivalents before anything is merged, because an ALL")
    A("--   policy also applies to SELECT and cannot be folded into a SELECT-only")
    A("--   policy without losing its write coverage:")
    A("--       SELECT  USING (qual)")
    A("--       DELETE  USING (qual)")
    A("--       UPDATE  USING (qual) WITH CHECK (with_check IF PRESENT ELSE qual)")
    A("--       INSERT  WITH CHECK (with_check IF PRESENT ELSE qual)")
    A("--")
    A("--   ⚠️ THE TRAP, and it is a silent one: that `ELSE qual` is Postgres")
    A("--   semantics, not a convenience. When an ALL/UPDATE/INSERT policy carries")
    A("--   no WITH CHECK, Postgres uses the USING expression AS the check.")
    A("--   Writing `true` there instead -- the obvious-looking default -- would")
    A("--   hand every authenticated user the right to write any row.")
    A("--")
    A("-- Step 2. Per (table, command):")
    A("--       merged USING      = OR over every policy's USING")
    A("--       merged WITH CHECK = OR over every policy's EFFECTIVE check,")
    A("--                           where effective = with_check if present else qual")
    A("--")
    A("--   ⚠️ WHY OR-ING THE TWO CLAUSES SEPARATELY IS EXACT. For an UPDATE under")
    A("--   several permissive policies, Postgres requires the OLD row to satisfy")
    A("--   at least one policy's USING and the NEW row to satisfy at least one")
    A("--   policy's WITH CHECK -- and they need NOT be the same policy. So")
    A("--   (U1 OR U2) with (C1 OR C2) is precisely the original behaviour. Had")
    A("--   Postgres instead required a single policy to satisfy both, this merge")
    A("--   would be a real widening and the transform would be unsound.")
    A("--")
    A("-- Step 3. Branches are ordered cheapest-first so the OR short-circuits:")
    A("--       0 pure column predicate   1 bare self-check   2 request-constant")
    A("--       3 school equality         4 row-dependent call   5 EXISTS (last)")
    A("--   A composite branch takes the cost of its dearest component.")
    A("--")
    A("-- Step 4. NOT TOUCHED, on purpose:")
    A("--   * RESTRICTIVE policies -- they AND rather than OR, so folding one into")
    A("--     the OR would be a security change. Any table carrying one is skipped")
    A("--     whole.")
    A("--   * policies granted to a role other than `public` -- merging across")
    A("--     differing GRANT sets changes who the policy reaches.")
    A("--   Both are listed at the foot of this file with their reasons.")
    A("--")
    A("-- " + "=" * 74)
    A("-- WHY THIS FILE IS GENERATED AND PINNED, WHERE MRB-347's WAS SELF-APPLYING")
    A("-- " + "=" * 74)
    A("-- MRB-347 rewrote whatever it found at apply time, because its transform")
    A("-- was idempotent and per-policy: hoisting a call it had already hoisted was")
    A("-- a no-op. THIS transform is neither. It drops policies and creates new")
    A("-- ones, and the merged expression depends on the exact set of policies")
    A("-- present. Run against a catalogue it was not generated from, a")
    A("-- self-applying version would merge the wrong set and say nothing.")
    A("--")
    A("-- So this file carries the expected qual/with_check of EVERY policy it")
    A("-- drops, and the guard block below refuses to proceed if the live")
    A("-- catalogue differs by so much as a byte. TEST and production policy sets")
    A("-- are NOT identical (141 policies on TEST, 153 on production), so this")
    A("-- matters: applied to a catalogue it does not match, this migration")
    A("-- ABORTS rather than mis-merging.")
    A("--")
    A(f"-- GENERATED FROM: project ref {ref} at {generated_at}")
    A(f"-- Drops {n_drop} policies across {len(plan)} tables; creates {n_create}.")
    A("--")
    A("-- ⚠️ To land this on production, REGENERATE it against production's own")
    A("--    catalogue rather than applying this file:")
    A("--        python3 tools/rls_consolidate.py --project prod --emit \\")
    A("--            --i-am-sure-production")
    A("--    The guard will otherwise abort, which is the safe direction.")
    A("--")
    A("-- REVERSIBLE: every original policy is kept in public.mrb348_policy_backup.")
    A("-- See supabase/rollbacks/ for the undo.")
    A("-- " + "=" * 74)
    A("")
    A("begin;")
    A("")
    A("create table if not exists public.mrb348_policy_backup (")
    A("  schemaname text, tablename text, policyname text, permissive text,")
    A("  roles text, cmd text, qual text, with_check text,")
    A("  taken_at timestamptz default now()")
    A(");")
    A("revoke all on public.mrb348_policy_backup from public, anon, authenticated;")
    A("")
    A("insert into public.mrb348_policy_backup")
    A("  (schemaname, tablename, policyname, permissive, roles, cmd, qual, with_check)")
    A("select schemaname, tablename, policyname, permissive, roles::text, cmd, qual, with_check")
    A("from pg_policies")
    A("where schemaname = 'public'")
    A("  and not exists (select 1 from public.mrb348_policy_backup b")
    A("                  where b.tablename = pg_policies.tablename")
    A("                    and b.policyname = pg_policies.policyname);")
    A("")
    A("-- " + "-" * 74)
    A("-- GUARD. Abort unless every policy this migration drops is present with")
    A("-- exactly the expression it was generated against. This is what makes a")
    A("-- catalogue-pinned migration safe to attempt on an environment that may")
    A("-- have drifted.")
    A("-- " + "-" * 74)
    A("do $guard$")
    A("declare expected record; live record; n int := 0;")
    A("begin")
    A("  for expected in")
    A("    select * from (values")
    rowsql = []
    for table, spec in sorted(plan.items()):
        for p in sorted(spec["drop"], key=lambda x: x["policyname"]):
            rowsql.append(
                f"      ({sql_lit(table)}, {sql_lit(p['policyname'])}, "
                f"{sql_lit(p['cmd'])}, {sql_lit(p['qual'])}, {sql_lit(p['with_check'])})"
            )
    A(",\n".join(rowsql))
    A("    ) as t(tablename, policyname, cmd, qual, with_check)")
    A("  loop")
    A("    select pg_policies.qual, pg_policies.with_check, pg_policies.cmd,")
    A("           pg_policies.permissive, pg_policies.roles::text as roles")
    A("      into live")
    A("    from pg_policies")
    A("    where schemaname = 'public'")
    A("      and tablename = expected.tablename")
    A("      and policyname = expected.policyname;")
    A("")
    A("    if not found then")
    A("      raise exception 'MRB-348 aborted: policy %.% not found. This migration is "
      "pinned to the catalogue it was generated from -- regenerate it with "
      "tools/rls_consolidate.py against THIS database.', expected.tablename, expected.policyname;")
    A("    end if;")
    A("    if live.permissive <> 'PERMISSIVE' then")
    A("      raise exception 'MRB-348 aborted: %.% is RESTRICTIVE here but was PERMISSIVE "
      "when generated. Restrictive policies AND rather than OR and must never be merged.',")
    A("        expected.tablename, expected.policyname;")
    A("    end if;")
    A("    if live.roles <> '{public}' then")
    A("      raise exception 'MRB-348 aborted: %.% is granted to % here, not {public}.',")
    A("        expected.tablename, expected.policyname, live.roles;")
    A("    end if;")
    A("    if live.cmd is distinct from expected.cmd")
    A("       or live.qual is distinct from expected.qual")
    A("       or live.with_check is distinct from expected.with_check then")
    A("      raise exception 'MRB-348 aborted: %.% has drifted from the catalogue this "
      "migration was generated against. Regenerate rather than forcing.',")
    A("        expected.tablename, expected.policyname;")
    A("    end if;")
    A("    n := n + 1;")
    A("  end loop;")
    A(f"  if n <> {n_drop} then")
    A(f"    raise exception 'MRB-348 aborted: guard matched % policies, expected %', n, {n_drop};")
    A("  end if;")
    A("  raise notice 'MRB-348 guard: % policies verified byte-identical', n;")
    A("end $guard$;")
    A("")
    A("-- " + "-" * 74)
    A("-- THE MERGE, table by table.")
    A("-- " + "-" * 74)
    for table, spec in sorted(plan.items()):
        A("")
        A(f"-- ---- {table} " + "-" * max(0, 66 - len(table)))
        srcs = sorted(p["policyname"] for p in spec["drop"])
        A(f"--   {len(srcs)} policies -> {len(spec['create'])}")
        for s in srcs:
            A(f"--     - {s}")
        for p in sorted(spec["drop"], key=lambda x: x["policyname"]):
            A(f'drop policy "{p["policyname"]}" on public.{table};')
        for m in spec["create"]:
            A("")
            A(f"-- {m['cmd']}: " + ", ".join(m["sources"]))
            order = m["using_branches"] or m["check_branches"]
            if order:
                A("--   branch order (cost: policy)")
                for b in order:
                    A(f"--     {b['cost']}: {b['policy']}")
            A(f'create policy "{m["name"]}" on public.{table}')
            A(f"  as permissive for {m['cmd'].lower()} to public")
            if m["using"] is not None:
                A(f"  using (\n    {m['using']}\n  )")
            if m["check"] is not None:
                A(f"  with check (\n    {m['check']}\n  )")
            A(";")
    A("")
    A("-- " + "-" * 74)
    A("-- POST-CONDITIONS")
    A("-- " + "-" * 74)
    A("do $post$")
    A("declare n_restrictive int; n_multi int;")
    A("begin")
    A("  select count(*) into n_restrictive")
    A("  from pg_policies where schemaname='public' and permissive <> 'PERMISSIVE';")
    A("  if n_restrictive > 0 then")
    A("    raise exception 'MRB-348 aborted: % restrictive policies present after merge; "
      "this migration must never create one', n_restrictive;")
    A("  end if;")
    A("")
    A("  -- every table this migration touched must now hold exactly one PUBLIC")
    A("  -- permissive policy per command it covers")
    A("  select count(*) into n_multi from (")
    A("    select tablename, cmd from pg_policies")
    A("    where schemaname='public' and roles::text='{public}'")
    A("      and tablename in (" + ", ".join(sql_lit(t) for t in sorted(plan)) + ")")
    A("    group by tablename, cmd having count(*) > 1")
    A("  ) d;")
    A("  if n_multi > 0 then")
    A("    raise exception 'MRB-348: % (table,cmd) cells still hold multiple public "
      "policies', n_multi;")
    A("  end if;")
    A("  raise notice 'MRB-348: merge complete, 0 restrictive, 0 multi-permissive public cells';")
    A("end $post$;")
    A("")
    A("commit;")
    A("")
    A("-- " + "=" * 74)
    A("-- LEFT ALONE, AND WHY")
    A("-- " + "=" * 74)
    for s in skips:
        A(f"--   {s['table']}.{s['scope']}")
        A(f"--       {s['reason']}")
    if not skips:
        A("--   (nothing skipped)")
    return "\n".join(L) + "\n"


def emit_rollback(plan, ref, generated_at):
    L = []
    A = L.append
    A("-- ROLLBACK for MRB-348 WS-3 (consolidate multiple permissive RLS policies).")
    A("--")
    A("-- Apply MANUALLY only -- the Supabase CLI never reads supabase/rollbacks/.")
    A("--")
    A("-- Drops the merged policies and recreates every original from")
    A("-- public.mrb348_policy_backup, which the forward migration filled.")
    A("--")
    A("-- ⚠️ Unlike the MRB-347 rollback, this one cannot be a simple ALTER: the")
    A("-- forward migration DROPPED policies and CREATED differently-named ones, so")
    A("-- restoring means recreating objects, including their permissive flag, their")
    A("-- roles and their command. All four are stored in the backup table for")
    A("-- exactly this reason -- a rollback that restored the expressions but not the")
    A("-- GRANT set would quietly change who each policy reaches.")
    A("--")
    A("-- ⚠️ This returns the estate to the many-branch policies and to the 251")
    A("-- linter findings. The forward migration was proven semantically identical")
    A("-- (inverse-transform round-trip plus before/after visibility digests across")
    A("-- every role), so rolling back buys nothing but latency. Use it only if the")
    A("-- merge is implicated in an actual incident.")
    A("--")
    A(f"-- Pairs with the forward migration generated from ref {ref} at {generated_at}.")
    A("")
    A("begin;")
    A("")
    A("do $rb$")
    A("declare r record; stmt text; n_drop int := 0; n_restore int := 0;")
    A("begin")
    A("  if to_regclass('public.mrb348_policy_backup') is null then")
    A("    raise exception 'MRB-348 rollback: backup table missing, cannot restore';")
    A("  end if;")
    A("")
    A("  -- 1. drop the merged policies this ticket created")
    A("  for r in")
    A("    select tablename, policyname from pg_policies")
    A("    where schemaname = 'public'")
    A("      and policyname like '%\\_merged'")
    A("      and not exists (select 1 from public.mrb348_policy_backup b")
    A("                      where b.tablename = pg_policies.tablename")
    A("                        and b.policyname = pg_policies.policyname)")
    A("  loop")
    A("    execute format('drop policy %I on public.%I', r.policyname, r.tablename);")
    A("    n_drop := n_drop + 1;")
    A("  end loop;")
    A("")
    A("  -- 2. recreate every original that is no longer present")
    A("  for r in select * from public.mrb348_policy_backup loop")
    A("    if not exists (select 1 from pg_policies")
    A("                   where schemaname = 'public'")
    A("                     and tablename = r.tablename")
    A("                     and policyname = r.policyname) then")
    A("      stmt := format('create policy %I on public.%I as %s for %s to %s',")
    A("                     r.policyname, r.tablename,")
    A("                     case when r.permissive = 'PERMISSIVE' then 'permissive'")
    A("                          else 'restrictive' end,")
    A("                     r.cmd,")
    A("                     -- roles came out of pg_policies as a {a,b} array literal")
    A("                     array_to_string(")
    A("                       (select array_agg(quote_ident(x))")
    A("                        from unnest(string_to_array(trim(both '{}' from r.roles), ','))")
    A("                             as x), ', '));")
    A("      if r.qual is not null then")
    A("        stmt := stmt || format(' using (%s)', r.qual);")
    A("      end if;")
    A("      if r.with_check is not null then")
    A("        stmt := stmt || format(' with check (%s)', r.with_check);")
    A("      end if;")
    A("      execute stmt;")
    A("      n_restore := n_restore + 1;")
    A("    end if;")
    A("  end loop;")
    A("")
    A("  raise notice 'MRB-348 rollback: dropped % merged, restored % original',")
    A("               n_drop, n_restore;")
    A("end $rb$;")
    A("")
    A("commit;")
    A("")
    A("-- Optional, once you are certain you will not roll back again:")
    A("--   drop table public.mrb348_policy_backup;")
    return "\n".join(L) + "\n"


# ---------------------------------------------------------------------------
# Proof B -- visibility digest
# ---------------------------------------------------------------------------

FIXTURE_PASSWORD = os.environ.get("MRB348_FIXTURE_PASSWORD", "mrb348-perf-drive!7Qx")

PROOF_B_USERS = [
    "hz_s1@test.mrbadmus",
    "hz_s2@test.mrbadmus",
    "hz_snull@test.mrbadmus",
    "hz_amy@test.mrbadmus",
    "hz_ben@test.mrbadmus",
    "hz_t2@test.mrbadmus",
    "hz_rich@test.mrbadmus",
    "hz_slt@test.mrbadmus",
    "hz_admin@test.mrbadmus",
    "hz_legacyadmin@test.mrbadmus",
]


def primary_keys(api, tables):
    rows = api.sql(
        "select c.relname as tablename, a.attname as col, "
        "array_position(i.indkey::int2[], a.attnum) as pos "
        "from pg_index i "
        "join pg_class c on c.oid = i.indrelid "
        "join pg_namespace n on n.oid = c.relnamespace "
        "join pg_attribute a on a.attrelid = c.oid and a.attnum = any(i.indkey) "
        "where i.indisprimary and n.nspname = 'public' "
        "order by c.relname, pos"
    )
    pk = defaultdict(list)
    for r in rows:
        if r["tablename"] in tables:
            pk[r["tablename"]].append(r["col"])
    return pk


def digest_rows(payload):
    """Stable hash of a visible row set. Key order is normalised by json.dumps."""
    try:
        rows = json.loads(payload)
    except Exception:  # noqa: BLE001
        return None, None
    if not isinstance(rows, list):
        return None, None
    canon = json.dumps(rows, sort_keys=True, separators=(",", ":"), default=str)
    return len(rows), hashlib.sha256(canon.encode()).hexdigest()[:32]


def verify_visibility(api, tables, phase, out_path):
    pk = primary_keys(api, set(tables))
    capture = {"phase": phase, "at": _dt.datetime.now(_dt.timezone.utc).isoformat(), "cells": {}}
    signed_in, failed_signin = [], []
    for email in PROOF_B_USERS:
        token = api.sign_in(email, FIXTURE_PASSWORD)
        if not token:
            failed_signin.append(email)
            continue
        signed_in.append(email)
        for table in sorted(tables):
            st, data = api.select_as(token, table, pk.get(table, []))
            if st != 200:
                capture["cells"][f"{email}|{table}"] = {"status": st, "n": None, "digest": None}
                continue
            n, d = digest_rows(data)
            capture["cells"][f"{email}|{table}"] = {"status": st, "n": n, "digest": d}
    capture["signed_in"] = signed_in
    capture["failed_signin"] = failed_signin
    capture["tables"] = sorted(tables)
    with open(out_path, "w") as fh:
        json.dump(capture, fh, indent=1)
    nonempty = sum(1 for v in capture["cells"].values() if (v["n"] or 0) > 0)
    rows = sum(v["n"] or 0 for v in capture["cells"].values())
    print(f"[proof B / {phase}] users signed in : {len(signed_in)}  (failed: {len(failed_signin)})")
    print(f"[proof B / {phase}] cells captured  : {len(capture['cells'])}")
    print(f"[proof B / {phase}] NON-EMPTY cells : {nonempty}   rows fingerprinted: {rows}")
    print(f"[proof B / {phase}] written to      : {out_path}")
    return capture


def compare_captures(a_path, b_path):
    a = json.load(open(a_path))
    b = json.load(open(b_path))
    keys = sorted(set(a["cells"]) | set(b["cells"]))
    mismatches, count_mismatches, nonempty, compared = [], 0, 0, 0
    for k in keys:
        ca, cb = a["cells"].get(k), b["cells"].get(k)
        if ca is None or cb is None:
            mismatches.append(f"{k}: present in only one capture")
            continue
        compared += 1
        if (ca["n"] or 0) > 0 or (cb["n"] or 0) > 0:
            nonempty += 1
        if ca["status"] != cb["status"]:
            mismatches.append(f"{k}: status {ca['status']} -> {cb['status']}")
        if ca["n"] != cb["n"]:
            count_mismatches += 1
            mismatches.append(f"{k}: row count {ca['n']} -> {cb['n']}")
        elif ca["digest"] != cb["digest"]:
            mismatches.append(f"{k}: digest changed ({ca['n']} rows)")
    rows = sum(v["n"] or 0 for v in a["cells"].values())
    print(f"[proof B] {a['phase']} -> {b['phase']}")
    print(f"[proof B] cells compared      : {compared}")
    print(f"[proof B] NON-EMPTY cells     : {nonempty}   <- the cells that actually prove something")
    print(f"[proof B] rows fingerprinted  : {rows}")
    print(f"[proof B] row-count mismatches: {count_mismatches}")
    print(f"[proof B] MISMATCHES          : {len(mismatches)}")
    for m in mismatches[:60]:
        print("    !", m)
    return mismatches


# ---------------------------------------------------------------------------
# Apply
# ---------------------------------------------------------------------------


def apply_sql_file(api, path):
    """Send a generated migration through the temporary rehearsal DDL seam.

    ⚠️ `begin;` / `commit;` are stripped, and that is NOT a weakening of the
    atomicity the file asks for. The seam is a PL/pgSQL function, and a function
    cannot open or close a transaction -- leaving them in raises 2D000 rather
    than committing early. A PostgREST RPC call is itself already wrapped in one
    transaction, so the whole file still lands all-or-nothing: if the guard block
    raises, every drop and create in the file rolls back with it.

    This path exists only for the TEST rehearsal. Production applies the file as
    written, through the Supabase CLI, where begin/commit are honoured normally.
    """
    sql = open(path).read()
    stripped = re.sub(r"(?im)^\s*(begin|commit)\s*;\s*$", "", sql)
    api.ddl(stripped)
    print(f"[apply] {os.path.basename(path)} applied (transaction: the RPC's own)")


# ---------------------------------------------------------------------------


def main():
    ap = argparse.ArgumentParser(description="MRB-348 WS-3 RLS policy consolidation")
    ap.add_argument("--project", choices=["test", "prod"], required=True)
    ap.add_argument("--i-am-sure-production", action="store_true")
    ap.add_argument("--check", action="store_true", help="Proof A only")
    ap.add_argument("--emit", action="store_true", help="write migration + rollback")
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--rollback", action="store_true")
    ap.add_argument("--verify-visibility", action="store_true")
    ap.add_argument("--phase", default="before")
    ap.add_argument("--tables-from", help="reuse the table list from a prior capture JSON")
    ap.add_argument("--compare", nargs=2, metavar=("A", "B"))
    ap.add_argument("--out-dir", default=os.path.join(REPO, "supabase"))
    ap.add_argument("--catalogue", help=(
        "read the policy catalogue from a JSON file instead of connecting. "
        "See OFFLINE CATALOGUE MODE in the module docstring."))
    ap.add_argument("--stamp", help="timestamp for generated filenames, YYYYMMDDHHMMSS")
    args = ap.parse_args()

    if args.compare:
        sys.exit(1 if compare_captures(*args.compare) else 0)

    if args.catalogue:
        # ⚠️ OFFLINE: NO CONNECTION IS OPENED AT ALL, so there is no credential
        # to prove a ref from and `resolve_project` is deliberately not called.
        # What names the target instead is the catalogue file's own `ref` field,
        # which the dumper wrote out of `pg_policies` on the project it read —
        # and `--project` must AGREE with it or this refuses. A file that says
        # production cannot be emitted as TEST, and vice versa: the mismatch is
        # the whole failure this check exists to catch, because the generated
        # SQL pins the exact policy bodies it expects to drop and the two
        # projects' bodies genuinely differ (production's
        # `profiles_teacher_read_students` carries `cm.deleted_at IS NULL` and
        # TEST's does not).
        book = json.load(open(args.catalogue))
        ref = book.get("ref")
        want = PROD_REF if args.project == "prod" else TEST_REF
        if ref != want:
            raise SystemExit(
                f"REFUSING: --project {args.project} expects ref {want}, but the "
                f"catalogue {args.catalogue!r} was dumped from {ref!r}.")
        if ref == PROD_REF and not args.i_am_sure_production:
            raise SystemExit(
                "REFUSING: that catalogue is PRODUCTION's. Pass "
                "--i-am-sure-production if you mean it.")
        if args.apply or args.rollback or args.verify_visibility:
            raise SystemExit(
                "--catalogue is generate-only. It cannot apply, roll back or "
                "verify: those need a live connection, and the whole point of "
                "this mode is that there isn't one.")
        print(f"[project] ref taken from the catalogue file: {ref}")
        print(f"[project] {'PRODUCTION' if ref == PROD_REF else 'TEST'}  (offline)")
        policies = book["policies"]
        print(f"[catalogue] {len(policies)} policies, read from {args.catalogue}")
        plan, skips = build_plan(policies)
        n_drop = sum(len(v["drop"]) for v in plan.values())
        n_create = sum(len(v["create"]) for v in plan.values())
        print(f"[plan] {len(plan)} tables consolidated: {n_drop} policies -> {n_create}")
        print(f"[plan] {len(skips)} skips")
        pa = proof_a(plan)
        print(f"[proof A] clauses checked : {pa['clauses_checked']}")
        print(f"[proof A] branches checked: {pa['branches_checked']}")
        print(f"[proof A] round-trip failures: {len(pa['failures'])}")
        for f in pa["failures"]:
            print("    !", f)
        if pa["failures"]:
            sys.exit("Proof A failed -- nothing emitted.")
        if args.check:
            return
        if not args.emit:
            raise SystemExit("--catalogue does nothing without --check or --emit.")
        stamp = args.stamp or _dt.datetime.now().strftime("%Y%m%d%H%M%S")
        gen_at = _dt.datetime.now(_dt.timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
        fwd = os.path.join(args.out_dir, "migrations",
                           f"{stamp}_mrb348_rls_consolidate.sql")
        rbk = os.path.join(args.out_dir, "rollbacks",
                           f"{stamp}_mrb348_rls_consolidate_rollback.sql")
        with open(fwd, "w") as fh:
            fh.write(emit_forward(plan, skips, ref, gen_at))
        with open(rbk, "w") as fh:
            fh.write(emit_rollback(plan, ref, gen_at))
        print(f"[emit] {fwd}")
        print(f"[emit] {rbk}")
        return

    url, service, anon, ref = resolve_project(args.project, args.i_am_sure_production)
    print(f"[project] ref proven from the service-role JWT payload: {ref}")
    print(f"[project] {'PRODUCTION' if ref == PROD_REF else 'TEST'}  url={url}")
    api = Api(url, service, anon)

    if args.verify_visibility:
        # ⚠️ The table list must be PINNED across phases, not recomputed. After
        # the merge there are no multi-permissive cells left, so recomputing the
        # plan here would yield an empty table list and the "after" capture would
        # compare zero cells against the baseline and call it a pass. That is the
        # exact shape of a proof that proves nothing.
        if args.tables_from:
            tables = json.load(open(args.tables_from))["tables"]
        else:
            plan, _ = build_plan(load_policies(api))
            tables = sorted(plan)
            if not tables:
                raise SystemExit(
                    "no multi-permissive cells found, so no table list could be derived.\n"
                    "If this is a post-merge phase, pass --tables-from <before-capture.json>."
                )
        out = os.environ.get(
            "MRB348_CAPTURE",
            os.path.join("/private/tmp/claude-501", f"mrb348_visibility_{args.phase}.json"),
        )
        verify_visibility(api, tables, args.phase, out)
        return

    if args.rollback:
        path = os.path.join(args.out_dir, "rollbacks", args.stamp + "_mrb348_rls_consolidate_rollback.sql")
        apply_sql_file(api, path)
        return

    policies = load_policies(api)
    print(f"[catalogue] {len(policies)} policies in schema public")
    plan, skips = build_plan(policies)

    n_drop = sum(len(v["drop"]) for v in plan.values())
    n_create = sum(len(v["create"]) for v in plan.values())
    print(f"[plan] {len(plan)} tables consolidated: {n_drop} policies -> {n_create}")
    print(f"[plan] {len(skips)} skips")

    pa = proof_a(plan)
    print(f"[proof A] clauses checked : {pa['clauses_checked']}")
    print(f"[proof A] branches checked: {pa['branches_checked']}")
    print(f"[proof A] round-trip failures: {len(pa['failures'])}")
    for f in pa["failures"]:
        print("    !", f)
    if pa["failures"]:
        sys.exit("Proof A failed -- nothing emitted, nothing applied.")

    if args.check:
        return

    stamp = args.stamp or _dt.datetime.now().strftime("%Y%m%d%H%M%S")
    gen_at = _dt.datetime.now(_dt.timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    fwd = os.path.join(args.out_dir, "migrations", f"{stamp}_mrb348_rls_consolidate.sql")
    rbk = os.path.join(args.out_dir, "rollbacks", f"{stamp}_mrb348_rls_consolidate_rollback.sql")

    if args.emit:
        with open(fwd, "w") as fh:
            fh.write(emit_forward(plan, skips, ref, gen_at))
        with open(rbk, "w") as fh:
            fh.write(emit_rollback(plan, ref, gen_at))
        print(f"[emit] {fwd}")
        print(f"[emit] {rbk}")

    if args.apply:
        apply_sql_file(api, fwd)


if __name__ == "__main__":
    main()
