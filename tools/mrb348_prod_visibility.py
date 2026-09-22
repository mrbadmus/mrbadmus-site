#!/usr/bin/env python3
"""
MRB-348 round three — the PRODUCTION visibility baseline for the RLS
consolidation, and the comparison that decides whether the rollback goes in.

    python3 tools/mrb348_prod_visibility.py --emit-sql > before.sql
    # paste before.sql into the Supabase connector against urklkrwevjtlfbwnipjn,
    # save the single `capture` cell it returns to a file, then:
    python3 tools/mrb348_prod_visibility.py --ingest raw_before.txt \
            --phase before --out docs/mrb348/prod-visibility-before.json

    # ... the chat applies the migration ...

    python3 tools/mrb348_prod_visibility.py --emit-sql > after.sql   # IDENTICAL SQL
    python3 tools/mrb348_prod_visibility.py --ingest raw_after.txt \
            --phase after --out docs/mrb348/prod-visibility-after.json
    python3 tools/mrb348_prod_visibility.py --compare \
            docs/mrb348/prod-visibility-before.json \
            docs/mrb348/prod-visibility-after.json

==========================================================================
WHY THIS EXISTS AT ALL
==========================================================================
Round two's report states a production BEFORE baseline of "290 cells, 126
non-empty, 16,147 rows". Those are AGGREGATES. The per-cell digests were
computed through the connector and never written to a file, so there was
nothing left to compare an after-capture AGAINST — the stated proof could
not actually have been completed. This script is that gap closed: the
capture is emitted as one pinned SQL statement, and both phases run the
same bytes.

==========================================================================
⚠️ WHY THE DIGEST IS OVER PRIMARY KEYS AND NOT OVER ROW CONTENT
==========================================================================
The TEST rehearsal hashed whole rows, which is right on a database nobody
is using. Production is a live site: children are submitting work while the
capture runs. A whole-row digest moves when a pupil edits an answer, and
that is not a policy change — it is Tuesday. A capture that cannot tell
those two apart would raise a false alarm on almost every table, and a
proof that cries wolf is worse than no proof, because the real signal is
then argued away.

So the digest is over the VISIBLE PRIMARY KEY SET. What an RLS policy
decides is exactly which rows a person may see; a merge that is faithful
leaves that set untouched, whatever the rows say.

⚠️ AND THE CAPTURE IS FROZEN AT AN INSTANT. Rows INSERTED between the two
captures would still move a key set, so every table is filtered to
`created_at <= FREEZE_AT`, with FREEZE_AT pinned in this file and therefore
identical in both phases. `platform_flags` has no `created_at` and takes no
filter — it is a tiny configuration table that does not churn.

A row DELETED between the captures can still move a cell. That is rare, it
is investigable (the count moves too), and it is named here rather than
hidden: on a mismatch, read the count before concluding the policy moved.

==========================================================================
⚠️ THE IDENTITIES ARE PRODUCTION'S REAL STANDINGS, AND THERE ARE ONLY FIVE
==========================================================================
Production holds exactly five distinct standings, measured rather than
assumed. Two identities are pinned per standing (lowest and highest id, so
the selection is reproducible and carries no judgement), except the single
operator, plus the signed-out `anon` role: 9 + 1 = 10 identities.

⚠️ PRODUCTION HAS NO `hod` AND NO `slt` SCOPE HOLDER. The policies for both
exist and were merged, so this capture CANNOT prove those two branches on
production — only TEST's rehearsal did, where fixtures for them exist. That
is a real limit of this proof and is stated in the report rather than
papered over.

No personal data leaves the database: the capture is counts and hashes.
"""

import argparse
import hashlib
import json
import sys
from datetime import datetime, timezone

PROD_REF = "urklkrwevjtlfbwnipjn"

# Pinned so both phases filter at the same instant. Set once, never edited
# between a before and its after.
FREEZE_AT = "2026-09-22T18:00:00Z"

# (label, user id or None for anon, role)
IDENTITIES = [
    ("operator_admin",     "3e0b7f6f-474e-457f-9825-3936e03ddcc7", "authenticated"),
    ("student_noschool_hi", "ffc788ae-d99b-4da4-a243-1c03f5ba1a6b", "authenticated"),
    ("student_noschool_lo", "0071bf7e-2643-40c5-a217-7f8ffb97fd59", "authenticated"),
    ("student_member_hi",  "ffb7298c-c11a-4bc1-bbca-4be4ac5b5bc3", "authenticated"),
    ("student_member_lo",  "008826b6-084f-49ee-b61e-76586ec771d7", "authenticated"),
    ("teacher_hi",         "eaf8052b-1cf3-4d00-8a5d-911f321c2407", "authenticated"),
    ("teacher_lo",         "00cf5738-dbf3-48ed-9fc7-be60bca96450", "authenticated"),
    ("school_admin_hi",    "7a1888de-bf1b-4974-844d-2213554613a0", "authenticated"),
    ("school_admin_lo",    "1966814c-2d24-46c2-a967-bdc955c3a487", "authenticated"),
    ("anon",               None,                                   "anon"),
]

# (table, primary key column). The 29 tables the consolidation touches or
# neighbours, with their real single-column primary keys read from the
# catalogue rather than assumed — two of them are NOT `id`.
TABLES = [
    ("academic_years", "id"),
    ("assignment_question_attempts", "id"),
    ("assignment_questions", "id"),
    ("assignment_submissions", "id"),
    ("assignments", "id"),
    ("audit_log", "id"),
    ("class_members", "id"),
    ("class_shoutouts", "id"),
    ("class_teachers", "id"),
    ("classes", "id"),
    ("family_messages", "id"),
    ("pending_staff", "id"),
    ("platform_flags", "key"),
    ("platform_operator_activations", "id"),
    ("platform_operators", "id"),
    ("profiles", "id"),
    ("quiz_question_attempts", "id"),
    ("quiz_scores", "id"),
    ("scheme_of_work_overrides", "id"),
    ("school_period_times", "id"),
    ("school_subject_settings", "id"),
    ("schools", "id"),
    ("staff_scopes", "id"),
    ("student_notifications", "id"),
    ("submission_feedback", "id"),
    ("subscriptions", "org_id"),
    ("timetable_entries", "id"),
    ("weekly_challenges", "id"),
    ("weekly_scores", "id"),
]

# The one table with no `created_at`, so no freeze filter is possible.
NO_CREATED_AT = {"platform_flags"}


def emit_sql() -> str:
    idents = ",\n      ".join(
        "({}, {}, {})".format(
            _lit(label), "null" if uid is None else _lit(uid), _lit(role))
        for label, uid, role in IDENTITIES)
    tables = ",\n      ".join(
        "({}, {}, {})".format(_lit(t), _lit(pk),
                              "false" if t in NO_CREATED_AT else "true")
        for t, pk in TABLES)
    return SQL_TEMPLATE.format(
        idents=idents, tables=tables, freeze=_lit(FREEZE_AT))


def _lit(s: str) -> str:
    return "'" + str(s).replace("'", "''") + "'"


SQL_TEMPLATE = """-- MRB-348 round three — production visibility capture.
-- READ ONLY. Runs entirely inside a transaction that ends in ROLLBACK, and
-- every setting it changes is set LOCAL, so nothing survives the statement.
-- Generated by tools/mrb348_prod_visibility.py -- do not hand-edit; regenerate.
begin;
create temp table mrb348_cap(ident text, tbl text, n bigint, digest text) on commit drop;
do $cap$
declare
  ident record; t record; cnt bigint; dig text; sql text;
  freeze_at constant timestamptz := {freeze};
begin
  for ident in select * from (values
      {idents}
    ) v(label, uid, rol)
  loop
    for t in select * from (values
      {tables}
    ) x(tbl, pk, has_created)
    loop
      -- Become the person. `true` makes both settings transaction-local, so
      -- the rollback at the foot of this file is not the only thing undoing
      -- them.
      if ident.uid is null then
        perform set_config('request.jwt.claims', '', true);
      else
        perform set_config('request.jwt.claims',
                 json_build_object('sub', ident.uid, 'role', ident.rol)::text, true);
      end if;
      perform set_config('role', ident.rol, true);

      sql := format(
        'select count(*), coalesce(md5(string_agg(k, E''\\n'' order by k)), ''-'') '
        'from (select %I::text as k from public.%I%s) s',
        t.pk, t.tbl,
        case when t.has_created then format(' where created_at <= %L', freeze_at)
             else '' end);
      -- ⚠️ A GRANT REFUSAL IS NOT AN EMPTY RESULT, AND MUST NOT LOOK LIKE ONE.
      -- `anon` has no SELECT grant on several of these tables, so the read
      -- raises `insufficient_privilege` before RLS is ever consulted. Letting
      -- that abort the capture loses the other 289 cells; recording it as 0
      -- rows would state that anon CAN reach the table and finds it empty,
      -- which is a different and weaker fact. It is its own state.
      begin
        execute sql into cnt, dig;
      exception when insufficient_privilege then
        cnt := -1; dig := 'denied';
      end;

      -- Back to the privileged role BEFORE writing the temp table, or the
      -- insert is attempted as a pupil.
      perform set_config('role', 'none', true);
      insert into mrb348_cap values (ident.label, t.tbl, cnt, dig);
    end loop;
  end loop;
end $cap$;

-- One row, one blob: 290 lines of `ident|table|count|digest`. Returned as a
-- single value so the whole capture survives a connector round trip intact.
select string_agg(ident || '|' || tbl || '|' || n || '|' || digest, E'\\n'
                  order by ident, tbl) as capture,
       count(*)::int                        as cells,
       count(*) filter (where n > 0)::int   as non_empty,
       count(*) filter (where n < 0)::int   as grant_denied,
       sum(greatest(n, 0))::bigint          as rows_fingerprinted
from mrb348_cap;
rollback;
"""


def ingest(path: str, phase: str) -> dict:
    raw = open(path).read().strip()
    cells = {}
    total = 0
    non_empty = 0
    denied = 0
    for line in raw.splitlines():
        line = line.strip()
        if not line:
            continue
        parts = line.split("|")
        if len(parts) != 4:
            sys.exit(f"REFUSING: malformed capture line: {line!r}")
        ident, tbl, n, digest = parts
        n = int(n)
        cells[f"{ident}/{tbl}"] = {"n": n, "digest": digest}
        total += max(n, 0)
        if n > 0:
            non_empty += 1
        elif n < 0:
            denied += 1
    expected = len(IDENTITIES) * len(TABLES)
    if len(cells) != expected:
        sys.exit(f"REFUSING: {len(cells)} cells, expected {expected}. "
                 "A partial capture is not a baseline.")
    return {
        "ref": PROD_REF,
        "phase": phase,
        "freeze_at": FREEZE_AT,
        "captured_at": datetime.now(timezone.utc).isoformat(),
        "method": "md5 of the sorted visible PRIMARY KEY set, per identity x table",
        "cells": len(cells),
        "non_empty": non_empty,
        "grant_denied": denied,
        "rows_fingerprinted": total,
        "capture_md5": hashlib.md5(raw.encode()).hexdigest(),
        "digests": cells,
    }


def compare(a_path: str, b_path: str) -> int:
    a = json.load(open(a_path))
    b = json.load(open(b_path))
    for k in ("ref", "freeze_at"):
        if a[k] != b[k]:
            sys.exit(f"REFUSING: {k} differs between the two captures "
                     f"({a[k]!r} vs {b[k]!r}). They are not comparable.")
    moved, vanished = [], []
    for key, av in a["digests"].items():
        bv = b["digests"].get(key)
        if bv is None:
            vanished.append(key)
        elif bv["digest"] != av["digest"] or bv["n"] != av["n"]:
            moved.append((key, av, bv))
    print(f"[compare] {a['phase']} -> {b['phase']}  ref {a['ref']}")
    print(f"[compare] cells            : {a['cells']} vs {b['cells']}")
    print(f"[compare] NON-EMPTY cells  : {a['non_empty']} vs {b['non_empty']}")
    print(f"[compare] grant-denied     : {a.get('grant_denied')} vs {b.get('grant_denied')}")
    print(f"[compare] rows fingerprinted: {a['rows_fingerprinted']} vs "
          f"{b['rows_fingerprinted']}")
    print(f"[compare] cells absent in the second capture: {len(vanished)}")
    print(f"[compare] DIGESTS MOVED    : {len(moved)}")
    for key, av, bv in moved:
        print(f"    ⚠️  {key}: n {av['n']} -> {bv['n']}, "
              f"digest {av['digest'][:12]} -> {bv['digest'][:12]}")
    if moved or vanished:
        print("\n⚠️  A MOVED CELL IS NOT AUTOMATICALLY A POLICY DEFECT. Check the")
        print("    count first: a row DELETED between the captures moves a key set")
        print("    without any policy having changed. A moved digest with an")
        print("    UNCHANGED count, or any count that GREW, is the serious shape.")
        print("    If the merge is implicated, the rollback goes in:")
        print("    supabase/rollbacks/20260922040000_mrb348_rls_consolidate_rollback.sql")
        return 1
    print("\n✅ 0 digests moved. Visibility is identical for every identity on "
          "every table.")
    return 0


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--emit-sql", action="store_true")
    ap.add_argument("--ingest", metavar="RAW")
    ap.add_argument("--phase", choices=["before", "after"])
    ap.add_argument("--out", metavar="JSON")
    ap.add_argument("--compare", nargs=2, metavar=("A", "B"))
    args = ap.parse_args()

    if args.emit_sql:
        print(emit_sql())
        return
    if args.compare:
        sys.exit(compare(*args.compare))
    if args.ingest:
        if not args.phase or not args.out:
            sys.exit("--ingest needs --phase and --out")
        book = ingest(args.ingest, args.phase)
        with open(args.out, "w") as fh:
            json.dump(book, fh, indent=1, sort_keys=True)
            fh.write("\n")
        print(f"[ingest] {book['cells']} cells, {book['non_empty']} non-empty, "
              f"{book['rows_fingerprinted']} rows -> {args.out}")
        return
    ap.print_help()


if __name__ == "__main__":
    main()
