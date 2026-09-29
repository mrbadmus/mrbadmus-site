#!/usr/bin/env python3
"""flashcard_set_names_rls.py — the RLS proof for `flashcard_set_names`
(MRB-352 Stage D2), as a real pupil against TEST.

Two throwaway worlds (two schools, each with a class, a teacher, a pupil and a
flashcard homework). Pupil A can see set A and cannot see set B. As pupil A:

  1  insert a name for set A                          → allowed
  2  update that name                                 → allowed
  3  insert a name for set B (invisible)              → refused
  4  update the row's assignment_id onto set B        → refused (Fable's case:
                                                        the UPDATE with-check
                                                        now carries the same
                                                        visibility test)
  5  insert a row claiming to be pupil B              → refused
  6  pupil B reads nothing of pupil A's               → 0 rows
  7  anon reads nothing                               → refused / 0 rows
  8  TRUNCATE is not granted to authenticated         → (catalogue, via the
                                                        rehearsal query; noted)

TEST ONLY (the service key's own ref claim). Teardown by snapshotted ids.
"""
import json
import os
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, REPO)
sys.path.insert(0, os.path.join(REPO, "tools"))
import mrb351_acceptance as acc  # noqa: E402
import mrb351_pupil_flow_live as pf  # noqa: E402
import flashcards_library_live as lib  # noqa: E402

FAILS = []


def check(ok, what):
    print(("  PASS " if ok else "  FAIL ") + what)
    if not ok:
        FAILS.append(what)


def main():
    env = acc.read_env(lib.DEFAULT_ENV)
    url, service = env["SUPABASE_URL"], env["SUPABASE_SERVICE_ROLE_KEY"]
    ref = acc.jwt_ref(service)
    if ref != acc.TEST_REF:
        acc.die(f"refusing: service key ref {ref} is not TEST ({acc.TEST_REF})")
    print(f"credential ref, proven from the key payload: {ref} => TEST")
    c = acc.Client(url, acc.anon_key(), service)
    ma, mb = {}, {}
    try:
        wa = lib.build(c, ma, "rlsA")
        wb = lib.build(c, mb, "rlsB")
        tok_a = c.sign_in(wa["people"]["p"]["email"], acc.THROWAWAY_PASSWORD)
        tok_b = c.sign_in(wb["people"]["p"]["email"], acc.THROWAWAY_PASSWORD)
        pa, pb = wa["people"]["p"]["id"], wb["people"]["p"]["id"]
        A, B = wa["aid"], wb["aid"]
        T = f"{url}/rest/v1/flashcard_set_names"

        def as_(tok, method, path, body=None):
            h = {"apikey": c.anon, "Authorization": f"Bearer {tok}", "Content-Type": "application/json",
                 "Prefer": "return=representation"}
            return c._req(method, T + path, h, body)

        st, vis = c.select(tok_a, "assignments", {"id": f"in.({A},{B})", "select": "id"})
        check(st == 200 and [r["id"] for r in vis] == [A], "pupil A sees set A and not set B (%s)" % vis)

        st, body = as_(tok_a, "POST", "", {"pupil_id": pa, "assignment_id": A, "name": "Mine"})
        check(st == 201, "1 insert a name for a visible set → %s" % st)
        st, body = as_(tok_a, "PATCH", f"?pupil_id=eq.{pa}&assignment_id=eq.{A}", {"name": "Mine again"})
        check(st == 200 and body and body[0]["name"] == "Mine again", "2 update it → %s %s" % (st, body))
        st, body = as_(tok_a, "POST", "", {"pupil_id": pa, "assignment_id": B, "name": "Not mine"})
        check(st in (401, 403) or (isinstance(body, dict) and body.get("code") == "42501"),
              "3 insert a name for an INVISIBLE set → refused (%s %s)" % (st, str(body)[:120]))
        st, body = as_(tok_a, "PATCH", f"?pupil_id=eq.{pa}&assignment_id=eq.{A}", {"assignment_id": B})
        check(st in (401, 403) or (isinstance(body, dict) and body.get("code") == "42501"),
              "4 UPDATE the row's assignment_id onto an invisible set → refused (%s %s)" % (st, str(body)[:160]))
        st, rows = c.select(None, "flashcard_set_names", {"pupil_id": f"eq.{pa}", "select": "assignment_id,name"},
                            as_service=True)
        check(rows == [{"assignment_id": A, "name": "Mine again"}], "   …and the row is unchanged (%s)" % rows)
        st, body = as_(tok_a, "POST", "", {"pupil_id": pb, "assignment_id": A, "name": "Forged"})
        check(st in (401, 403) or (isinstance(body, dict) and body.get("code") == "42501"),
              "5 insert as another pupil → refused (%s)" % st)
        st, body = as_(tok_b, "GET", "?select=assignment_id,name")
        check(st == 200 and body == [], "6 pupil B reads none of pupil A's names (%s)" % body)
        st, body = as_(c.anon, "GET", "?select=assignment_id,name")
        check(st in (401, 403) or body == [], "7 anon reads nothing (%s %s)" % (st, str(body)[:100]))
    finally:
        for m in (ma, mb):
            if m.get("assignments"):
                c.write("flashcard_set_names", "DELETE",
                        {"__match__": f"assignment_id=in.({','.join(m['assignments'])})"})
            pf.teardown(c, m)
        left = []
        for m in (ma, mb):
            for ids in (m.get("schools", []),):
                if ids:
                    st, rows = c.select(None, "schools", {"id": f"in.({','.join(ids)})", "select": "id"},
                                        as_service=True)
                    left += rows or []
        check(not left, "teardown by snapshotted id list left nothing behind (%s)" % left)
    if FAILS:
        print("\n  FAIL — %d check(s)" % len(FAILS))
        sys.exit(1)
    print("\n  PASS — flashcard_set_names RLS, as a real pupil on TEST")


if __name__ == "__main__":
    main()
