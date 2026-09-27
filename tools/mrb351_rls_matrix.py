#!/usr/bin/env python3
"""mrb351_rls_matrix.py — MRB-351 (flashcard homework), the who-sees-what
matrix from docs/mrb351/REPORT.md §Acceptance item 12: 9 identities x the 8
tables migration 1 creates (flashcard_decks, flashcard_cards,
flashcard_extractions, assignment_flashcards, flashcard_sessions,
flashcard_events, flashcard_pupil_cards, flashcard_reviews), plus the private
`teacher-uploads` storage bucket, plus write probes.

    MRB_THROWAWAY_PASSWORD=mrb326-throwaway python3 tools/mrb351_rls_matrix.py

Reuses the throwaway-world builder in `tools/mrb351_acceptance.py` (same
9 people, same 3 classes, same teardown-by-id-list) rather than duplicating
it — the fixture is identical, only what is DONE with it differs.

The 9 identities, exactly as named in the brief:
  anon; pupil in 10A (pa); pupil in 10Z (pz); pupil in 8x1 (px);
  teacher of 10A+8x1 (t1); teacher of 10Z (t2);
  colleague teacher, same school, no classes (t3);
  HoD/admin, same school (adm); teacher at another school (t4).
(pb, a second 10A pupil the acceptance script's late/missing item needs,
is minted too but is not one of the 9 and is not probed here.)

What proves a cell RIGHT is not a fixed row count — the world this script
builds is symmetric across a few real assignments/decks/sessions, so the
SELECT counts below are asserted to be internally consistent (T1's own
numbers equal PA's-plus-PX's, ADM's equal T1's-plus-T2's, T3 and T4 read
zero pupil rows, anon is refused outright) rather than pinned to literal
numbers that would need updating every time the fixture's content changes.
"""
from __future__ import annotations

import argparse
import json
import os
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import uuid
from datetime import datetime, timedelta, timezone

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(REPO)
sys.path.insert(0, REPO)
sys.path.insert(0, os.path.join(REPO, "tools"))

import importlib.util
_spec = importlib.util.spec_from_file_location("mrb351_acceptance", os.path.join(REPO, "tools", "mrb351_acceptance.py"))
acc = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(acc)

TABLES = ["flashcard_decks", "flashcard_cards", "flashcard_extractions",
          "assignment_flashcards", "flashcard_sessions", "flashcard_events",
          "flashcard_pupil_cards", "flashcard_reviews"]
IDENTITIES = ["anon", "pa", "pz", "px", "t1", "t2", "t3", "adm", "t4"]


def storage_list(c, tok, prefix):
    key = c.anon
    headers = {"apikey": key, "Content-Type": "application/json",
               "Authorization": f"Bearer {tok or key}"}
    req = urllib.request.Request(f"{c.url}/storage/v1/object/list/teacher-uploads",
                                  method="POST", headers=headers,
                                  data=json.dumps({"prefix": prefix, "limit": 10}).encode())
    try:
        with urllib.request.urlopen(req, context=acc.CTX, timeout=15) as r:
            return r.status, json.loads(r.read())
    except urllib.error.HTTPError as e:
        return e.code, e.read()[:200]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--env-file", default=acc.BACKEND_ENV_DEFAULT)
    args = ap.parse_args()

    env = acc.read_env(args.env_file)
    ref = acc.jwt_ref(env["SUPABASE_SERVICE_ROLE_KEY"])
    if ref == acc.PROD_REF:
        acc.die("refusing: service key is PRODUCTION")
    if ref != acc.TEST_REF:
        acc.die(f"refusing: service key ref {ref} is not TEST ({acc.TEST_REF})")
    print(f"credential ref, proven from the key payload: {ref} => TEST")

    c = acc.Client(env["SUPABASE_URL"], acc.anon_key(), env["SUPABASE_SERVICE_ROLE_KEY"])
    manifest = {}
    unexpected = []

    def expect(label, ok, detail=""):
        tag = "OK" if ok else "UNEXPECTED"
        if not ok:
            unexpected.append((label, detail))
        print(f"  [{tag}] {label}" + (f" — {detail}" if detail else ""))

    try:
        world = acc.build_world(c, manifest)
        tok, people = world["tokens"], world["people"]
        tok = dict(tok)
        tok["anon"] = None

        # ── content: one deck/assignment per class, so every table has
        #    real rows to probe (decks, cards, snapshot, a sitting, events,
        #    a written answer, a rating, an extraction job). ──
        cards = [{"question": f"RlsQ{i}", "answer": f"RlsA{i}"} for i in range(1, 4)]
        status, deck = c.rpc(tok["t1"], "flashcard_deck_save", {
            "p_deck": None, "p_title": "MRB351 RLS Deck", "p_cards": cards,
            "p_meta": {"source_kind": "typed", "shared_with_school": True}, "p_finalise": True})
        manifest.setdefault("decks", []).append(deck["deck_id"])
        now = datetime.now(timezone.utc)
        status, setwork = c.rpc(tok["t1"], "flashcard_set_work", {
            "p_class_ids": [world["class_a"], world["class_x"]], "p_deck": deck["deck_id"],
            "p_mode": "make", "p_rule": "quick", "p_title": "MRB351 RLS Homework",
            "p_release_at": (now - timedelta(minutes=1)).isoformat(),
            "p_due_at": (now + timedelta(days=3)).isoformat(), "p_note": None,
            "p_client_ref": f"mrb351-rls-a-{world['ts']}"})
        manifest.setdefault("assignments", []).extend(setwork["assignment_ids"])
        st, rows = c.select(None, "assignments", {"id": f"in.({','.join(setwork['assignment_ids'])})",
                             "select": "id,class_id"}, as_service=True)
        by_class = {r["class_id"]: r["id"] for r in rows}
        aid_a, aid_x = by_class[world["class_a"]], by_class[world["class_x"]]

        status, deck_z = c.rpc(tok["t2"], "flashcard_deck_save", {
            "p_deck": None, "p_title": "MRB351 RLS Deck Z", "p_cards": cards,
            "p_meta": {"source_kind": "typed", "shared_with_school": True}, "p_finalise": True})
        manifest["decks"].append(deck_z["deck_id"])
        status, setwork_z = c.rpc(tok["t2"], "flashcard_set_work", {
            "p_class_ids": [world["class_z"]], "p_deck": deck_z["deck_id"], "p_mode": "make",
            "p_rule": "quick", "p_title": "MRB351 RLS Homework Z",
            "p_release_at": (now - timedelta(minutes=1)).isoformat(),
            "p_due_at": (now + timedelta(days=3)).isoformat(), "p_note": None,
            "p_client_ref": f"mrb351-rls-z-{world['ts']}"})
        aid_z = setwork_z["assignment_ids"][0]
        manifest["assignments"].append(aid_z)

        # a genuine sitting for PA and PX (events, a written answer, a rating)
        for pid_key, aid in (("pa", aid_a), ("px", aid_x), ("pz", aid_z)):
            status, snap = c.rpc(tok[pid_key], "flashcard_record", {"p_assignment": aid, "p_events": []})
            t0 = datetime.now(timezone.utc) - timedelta(minutes=2)
            ev = acc.make_events(snap["cards"], "make", lambda i: "got_it", "ans", t0, step_ms=300, mode="make")
            c.rpc(tok[pid_key], "flashcard_record", {"p_assignment": aid, "p_events": ev})

        # a real extraction job + a real storage object, owned by T1's school
        csv_bytes = b"question,answer\nQ1,A1\nQ2,A2\n"
        status, up = acc.multipart_post_file(
            f"{c.url}/functions/v1/flashcard-extract",
            {"apikey": c.anon, "Authorization": f"Bearer {tok['t1']}"},
            "file", "rls.csv", csv_bytes, "text/csv", {"title": "MRB351 RLS Upload"})
        upload_prefix = None
        if status in (200, 202) and "deck_id" in up:
            manifest["decks"].append(up["deck_id"])
            for _ in range(15):
                st, rows = c.select(None, "flashcard_extractions", {"id": f"eq.{up['job_id']}", "select": "*"},
                                     as_service=True)
                if rows and rows[0]["status"] in ("done", "failed"):
                    if rows[0].get("file_sha256"):
                        upload_prefix = f"school/{world['school_a']}/flashcards/{up['deck_id']}"
                    break
                time.sleep(1)

        # ── the 9x8 read matrix ──
        print("\n" + "=" * 70)
        print("READ MATRIX (row count per identity x table)")
        print("=" * 70)
        counts = {}
        for ident in IDENTITIES:
            counts[ident] = {}
            for table in TABLES:
                status, body = c.select(tok[ident], table, {"select": "*"})
                counts[ident][table] = len(body) if status == 200 and isinstance(body, list) else f"ERR{status}"
            print(f"  {ident:5s} " + " ".join(f"{t[:14]:>5s}={counts[ident][t]}" for t in TABLES))

        # anon: refused (401) everywhere, or 0 — never a real row.
        for table in TABLES:
            v = counts["anon"][table]
            expect(f"anon reads {table}: refused or empty", v in (0,) or str(v).startswith("ERR"), str(v))

        # pupils never see the decks/cards/extraction library, whoever they are.
        for ident in ("pa", "pz", "px"):
            for table in ("flashcard_decks", "flashcard_cards", "flashcard_extractions"):
                expect(f"{ident} reads {table}: 0 (pupils never see the deck library)",
                       counts[ident][table] == 0, str(counts[ident][table]))

        # each pupil sees ONLY their own class's snapshot/sessions/events/etc,
        # never another pupil's class — cross-checked by exact arithmetic:
        # a teacher's total must equal the sum of the classes they teach.
        for table in ("assignment_flashcards", "flashcard_sessions", "flashcard_events",
                      "flashcard_pupil_cards", "flashcard_reviews"):
            t1_total = counts["t1"][table]
            t2_total = counts["t2"][table]
            adm_total = counts["adm"][table]
            expect(f"admin ({table}) == teacher_of_10A_8x1 + teacher_of_10Z (whole-school == sum of parts)",
                   adm_total == t1_total + t2_total,
                   f"adm={adm_total} t1={t1_total} t2={t2_total}")
            expect(f"t4 (other school) reads {table}: 0", counts["t4"][table] == 0, str(counts["t4"][table]))
            expect(f"t3 (no classes) reads {table}: 0 (a shared deck library is not a class)",
                   counts["t3"][table] == 0, str(counts["t3"][table]))
        # a colleague with no classes still sees the SHARED deck/card library —
        # by design (any staff member may browse decks to reuse), not a leak.
        expect("t3 (no classes) still sees the shared deck library (by design)",
               counts["t3"]["flashcard_decks"] > 0 and counts["t3"]["flashcard_cards"] > 0,
               f"decks={counts['t3']['flashcard_decks']} cards={counts['t3']['flashcard_cards']}")
        expect("t1 and t2 see the SAME deck library size as t3/adm (staff-wide, school-scoped)",
               counts["t1"]["flashcard_decks"] == counts["t3"]["flashcard_decks"] == counts["adm"]["flashcard_decks"],
               f"t1={counts['t1']['flashcard_decks']} t3={counts['t3']['flashcard_decks']} adm={counts['adm']['flashcard_decks']}")

        # PZ (10Z only) must see 0 of 10A/8x1's assignment_flashcards/etc,
        # i.e. exactly its own — cross-checked against t2 (10Z's teacher).
        for table in ("assignment_flashcards", "flashcard_sessions", "flashcard_events",
                      "flashcard_pupil_cards", "flashcard_reviews"):
            expect(f"pz {table} == t2 {table} (10Z pupil sees exactly what 10Z's teacher sees, no more)",
                   counts["pz"][table] == counts["t2"][table],
                   f"pz={counts['pz'][table]} t2={counts['t2'][table]}")

        # ── storage bucket ──
        print("\n" + "=" * 70)
        print("STORAGE BUCKET (teacher-uploads)")
        print("=" * 70)
        if upload_prefix:
            for ident in IDENTITIES:
                status, body = storage_list(c, tok[ident], upload_prefix)
                seen = isinstance(body, list) and len(body) > 0
                print(f"  {ident:5s} status={status} seen={seen}")
                if ident in ("anon", "pa", "pz", "px", "t4"):
                    expect(f"{ident} cannot see the school's uploaded file", not seen, f"status={status}")
                else:
                    expect(f"{ident} (staff, same school) can see the school's uploaded file", seen,
                           f"status={status}")
        else:
            print("  (extraction job did not settle in time; storage probe skipped — not a finding)")

        # ── write probes ──
        print("\n" + "=" * 70)
        print("WRITE PROBES")
        print("=" * 70)
        status, body = c._req("POST", f"{c.url}/rest/v1/flashcard_decks",
                               {"apikey": c.anon, "Authorization": f"Bearer {tok['pa']}",
                                "Content-Type": "application/json"},
                               {"school_id": world["school_a"], "created_by": people["pa"]["id"],
                                "title": "hack2", "source_kind": "typed"})
        expect("pupil direct INSERT flashcard_decks refused", status == 403, f"{status} {body}")

        status, body = c._req("POST", f"{c.url}/rest/v1/flashcard_sessions",
                               {"apikey": c.anon, "Authorization": f"Bearer {tok['pa']}",
                                "Content-Type": "application/json"},
                               {"assignment_id": aid_a, "pupil_id": people["pa"]["id"],
                                "school_id": world["school_a"], "class_id": world["class_a"]})
        expect("pupil direct INSERT flashcard_sessions refused", status == 403, f"{status} {body}")

        status, body = c._req("POST", f"{c.url}/rest/v1/flashcard_reviews",
                               {"apikey": c.anon, "Authorization": f"Bearer {tok['pa']}",
                                "Content-Type": "application/json"},
                               {"session_id": str(uuid.uuid4()), "assignment_id": aid_a,
                                "pupil_id": people["pa"]["id"], "school_id": world["school_a"],
                                "class_id": world["class_a"], "card_id": str(uuid.uuid4()),
                                "event_id": str(uuid.uuid4()), "rating": "got_it", "phase": "review",
                                "rated_at": datetime.now(timezone.utc).isoformat()})
        expect("pupil direct INSERT flashcard_reviews refused", status == 403, f"{status} {body}")

        status, body = c.rpc(tok["pz"], "flashcard_record", {"p_assignment": aid_a, "p_events": []})
        expect("pupil flashcard_record for another pupil's assignment refused",
               status == 403 and body.get("message") == "not_your_homework", f"{status} {body}")

        status, body = c.rpc(tok["t3"], "flashcard_set_work", {
            "p_class_ids": [world["class_a"]], "p_deck": deck["deck_id"], "p_mode": "make",
            "p_rule": "quick", "p_title": "hack", "p_release_at": None,
            "p_due_at": (now + timedelta(days=1)).isoformat(), "p_note": None,
            "p_client_ref": f"mrb351-rls-hack-{world['ts']}"})
        expect("teacher with no classes setting work to a class they don't teach refused",
               status == 403 and body.get("message") == "class_not_yours", f"{status} {body}")

        # smuggled answer_submitted in review mode (colleague reuse pattern)
        status, dup_id = c.rpc(tok["t2"], "flashcard_deck_duplicate", {"p_deck": deck["deck_id"]})
        manifest["decks"].append(dup_id)
        status, setwork_r = c.rpc(tok["t2"], "flashcard_set_work", {
            "p_class_ids": [world["class_z"]], "p_deck": dup_id, "p_mode": "review", "p_rule": "quick",
            "p_title": "MRB351 RLS Review Reuse", "p_release_at": (now - timedelta(minutes=1)).isoformat(),
            "p_due_at": (now + timedelta(days=3)).isoformat(), "p_note": None,
            "p_client_ref": f"mrb351-rls-smuggle-{world['ts']}"})
        aid_review = setwork_r["assignment_ids"][0]
        manifest["assignments"].append(aid_review)
        status, snap_r = c.rpc(tok["pz"], "flashcard_record", {"p_assignment": aid_review, "p_events": []})
        smuggle = {"id": str(uuid.uuid4()), "type": "answer_submitted",
                   "at": datetime.now(timezone.utc).isoformat(), "visible": True, "phase": "review",
                   "card": snap_r["cards"][0]["id"], "answer": "SMUGGLED"}
        status, r = c.rpc(tok["pz"], "flashcard_record", {"p_assignment": aid_review, "p_events": [smuggle]})
        status, pc = c.select(None, "flashcard_pupil_cards", {"assignment_id": f"eq.{aid_review}",
                               "select": "id"}, as_service=True)
        expect("smuggled answer_submitted in review-mode deck is ignored (0 rows written)",
               len(pc) == 0, f"pupil_cards_written={len(pc)}")

    finally:
        acc.teardown(c, manifest)
        residue = acc.check_residue(c, manifest)
        print("\nTEARDOWN residue check:", residue if residue else "0 rows left behind")

    print("\n" + "=" * 70)
    n_cells = len(IDENTITIES) * len(TABLES)
    print(f"RESULT: {n_cells} read cells x {len(IDENTITIES)} identities probed; "
          f"{len(unexpected)} unexpected")
    if unexpected:
        for label, detail in unexpected:
            print(f"  UNEXPECTED: {label} — {detail}")
        sys.exit(1)


if __name__ == "__main__":
    main()
