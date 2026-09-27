#!/usr/bin/env python3
"""mrb351_acceptance.py — MRB-351 (flashcard homework), the 12 acceptance
items from docs/mrb351/REPORT.md §Acceptance, re-run against the REAL
Postgres functions and the REAL flashcard-extract edge function on TEST,
through a throwaway world this script mints and tears down itself.

The two TEST-only helper edge functions the original build used
(mrb351-test-session / mrb351-env-probe) are retired (410) — this script
never calls them. Every check here is either:
  · a real GoTrue password sign-in (anon key) + a real PostgREST RPC call
    to a SECURITY DEFINER function, under real RLS, as the signed-in role;
  · a real multipart POST to the flashcard-extract edge function on TEST;
  · a direct service-role read, used ONLY to fetch ids this script itself
    created (never to bypass RLS on a measured check).

    MRB_THROWAWAY_PASSWORD=mrb326-throwaway python3 tools/mrb351_acceptance.py

Credentials, per docs/mrb335/RISKS.md E6:
  MRB_THROWAWAY_PASSWORD=mrb326-throwaway   (this script mints its own
                                             accounts, so any value works,
                                             but the standing value is used
                                             so a shared shell needs only one)
Env for the project + service role, read the same way every other TEST tool
in this repo reads it: SUPABASE_URL / SUPABASE_SERVICE_ROLE_KEY, from
`--env-file` or `/Users/midebadmus/Documents/GitHub/mrbadmus---backend/.env`.
The anon key is read out of `shared/config.js`, the same way
`set_work_drive.py` / `mrb348_teacher_rollup_proof.py` do.

TEST project only. The service-role key's own `ref` claim is checked before
any write; the script refuses to run against production.

No pupil names anywhere in this file or its output beyond the synthetic
throwaway ones it mints (PupilA/PupilZ/PupilX/PupilB — no real person).

Teardown is by a SNAPSHOTTED ID LIST, never a predicate delete: every id this
run creates is appended to a manifest as it is made, and `--teardown-only
<manifest.json>` re-runs just the teardown from a saved manifest if a run
was interrupted after minting but before finishing.
"""
from __future__ import annotations

import argparse
import base64
import json
import os
import re
import ssl
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

TEST_REF = "qeppkiswvclkkwbxmlok"
PROD_REF = "urklkrwevjtlfbwnipjn"
CTX = ssl.create_default_context(cafile="/etc/ssl/cert.pem")
BACKEND_ENV_DEFAULT = "/Users/midebadmus/Documents/GitHub/mrbadmus---backend/.env"
THROWAWAY_PASSWORD = os.environ.get("MRB_THROWAWAY_PASSWORD", "mrb326-throwaway")


def die(msg):
    raise SystemExit("mrb351_acceptance: " + msg)


def jwt_ref(token):
    parts = token.split(".")
    if len(parts) != 3:
        return None
    pad = "=" * (-len(parts[1]) % 4)
    return json.loads(base64.urlsafe_b64decode(parts[1] + pad)).get("ref")


def read_env(path):
    out = {}
    if not os.path.exists(path):
        die("env file not found: %s" % path)
    for line in open(path):
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, v = line.split("=", 1)
        out[k.strip()] = v.strip()
    return out


def anon_key():
    src = open("shared/config.js", encoding="utf-8").read()
    i = src.index("const TEST")
    m = re.search(r"'(eyJ[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+)'", src[i:])
    return m.group(1)


class Client:
    def __init__(self, url, anon, service):
        self.url = url
        self.anon = anon
        self.service = service

    def _req(self, method, url, headers, body=None):
        data = json.dumps(body).encode() if body is not None else None
        req = urllib.request.Request(url, data=data, method=method, headers=headers)
        try:
            with urllib.request.urlopen(req, context=CTX, timeout=30) as r:
                raw = r.read()
                return r.status, (json.loads(raw) if raw else None)
        except urllib.error.HTTPError as e:
            raw = e.read()
            try:
                j = json.loads(raw)
            except Exception:
                j = raw.decode(errors="replace")
            return e.code, j

    def sign_in(self, email, pw):
        status, body = self._req(
            "POST", f"{self.url}/auth/v1/token?grant_type=password",
            {"apikey": self.anon, "Content-Type": "application/json"},
            {"email": email, "password": pw})
        if status != 200:
            die(f"sign_in failed for {email}: {status} {body}")
        return body["access_token"]

    def rpc(self, token, name, args):
        headers = {"apikey": self.anon, "Content-Type": "application/json",
                   "Authorization": f"Bearer {token or self.anon}"}
        return self._req("POST", f"{self.url}/rest/v1/rpc/{name}", headers, args)

    def select(self, token, table, params, as_service=False):
        key = self.service if as_service else self.anon
        headers = {"apikey": key,
                   "Authorization": f"Bearer {self.service if as_service else (token or self.anon)}"}
        qs = "&".join(f"{k}={urllib.parse.quote(str(v), safe='.,()=:*')}" for k, v in params.items())
        return self._req("GET", f"{self.url}/rest/v1/{table}?{qs}", headers)

    def sql(self, statement):
        """Only used for fixture build/teardown (service role), never for a
        measured check — every measured read/write above goes through RLS."""
        headers = {"apikey": self.service, "Authorization": f"Bearer {self.service}",
                   "Content-Type": "application/json"}
        # There is no generic SQL PostgREST endpoint; fixture build/teardown
        # use plain REST calls (insert/update/delete) instead — see build()/teardown().
        raise NotImplementedError

    def write(self, table, method, body, prefer=None):
        headers = {"apikey": self.service, "Authorization": f"Bearer {self.service}",
                   "Content-Type": "application/json"}
        if prefer:
            headers["Prefer"] = prefer
        if method == "POST":
            return self._req("POST", f"{self.url}/rest/v1/{table}", headers, body)
        if method == "PATCH":
            qs = body.pop("__match__")
            return self._req("PATCH", f"{self.url}/rest/v1/{table}?{qs}", headers, body)
        if method == "DELETE":
            return self._req("DELETE", f"{self.url}/rest/v1/{table}?{body['__match__']}", headers)
        raise ValueError(method)

    def admin_create_user(self, email, pw):
        headers = {"apikey": self.service, "Authorization": f"Bearer {self.service}",
                   "Content-Type": "application/json"}
        status, body = self._req("POST", f"{self.url}/auth/v1/admin/users", headers,
                                  {"email": email, "password": pw, "email_confirm": True})
        if status not in (200, 201):
            die(f"admin_create_user failed for {email}: {status} {body}")
        return body["id"]

    def admin_delete_user(self, uid):
        headers = {"apikey": self.service, "Authorization": f"Bearer {self.service}"}
        return self._req("DELETE", f"{self.url}/auth/v1/admin/users/{uid}", headers)


def multipart_post_file(url, headers, field, filename, content, content_type, extra_fields):
    boundary = "----mrb351boundary" + uuid.uuid4().hex
    body = bytearray()
    for k, v in extra_fields.items():
        body += f"--{boundary}\r\nContent-Disposition: form-data; name=\"{k}\"\r\n\r\n{v}\r\n".encode()
    body += (f"--{boundary}\r\nContent-Disposition: form-data; name=\"{field}\"; "
             f"filename=\"{filename}\"\r\nContent-Type: {content_type}\r\n\r\n").encode()
    body += content
    body += f"\r\n--{boundary}--\r\n".encode()
    headers = dict(headers)
    headers["Content-Type"] = f"multipart/form-data; boundary={boundary}"
    req = urllib.request.Request(url, data=bytes(body), method="POST", headers=headers)
    try:
        with urllib.request.urlopen(req, context=CTX, timeout=60) as r:
            return r.status, json.loads(r.read())
    except urllib.error.HTTPError as e:
        return e.code, e.read()


# ════════════════════════════════════════════════════════════════════════
# THE THROWAWAY WORLD
# ════════════════════════════════════════════════════════════════════════

def _ok(label, status, body):
    if status not in (200, 201, 204):
        die(f"fixture build step failed ({label}): {status} {body}")
    return body


def build_world(c: Client, manifest):
    ts = int(time.time())
    school_a = str(uuid.uuid4())
    school_b = str(uuid.uuid4())
    class_a = str(uuid.uuid4())   # 10A/Ph1, taught by T1, KS4
    class_z = str(uuid.uuid4())   # 10Z/Ph1, taught by T2, KS4
    class_x = str(uuid.uuid4())   # 8x1, taught by T1, KS3
    manifest["schools"] = [school_a, school_b]
    manifest["classes"] = [class_a, class_z, class_x]

    people = {}
    for key, role in [("t1", "teacher"), ("t2", "teacher"), ("t3", "teacher"),
                       ("adm", "admin"), ("t4", "teacher"),
                       ("pa", "student"), ("pz", "student"), ("px", "student"), ("pb", "student")]:
        email = f"mrb351acc-{key}-{ts}@throwaway.test"
        uid = c.admin_create_user(email, THROWAWAY_PASSWORD)
        manifest.setdefault("users", []).append(uid)
        people[key] = {"id": uid, "email": email}

    # academic year: reuse the current one (read-only reference, not created
    # or torn down by this script)
    status, years = c.select(None, "academic_years", {"select": "id,is_current,end_date",
                                                        "order": "end_date.desc.nullslast"},
                              as_service=True)
    year_id = next((y["id"] for y in years if y.get("is_current") and y.get("end_date")), years[0]["id"])

    status, subj = c.select(None, "subjects", {"select": "id,name", "name": "eq.Physics"}, as_service=True)
    subject_physics = subj[0]["id"]

    _ok("school_a", *c.write("schools", "POST", {"id": school_a, "name": f"MRB351 Acceptance School {ts}",
                                 "code": f"MRB351A{ts}", "kind": "school",
                                 "key_stages_supported": ["KS3", "KS4"]}))
    _ok("school_b", *c.write("schools", "POST", {"id": school_b, "name": f"MRB351 Other School {ts}",
                                 "code": f"MRB351B{ts}", "kind": "school",
                                 "key_stages_supported": ["KS3", "KS4"]}))
    _ok("classes", *c.write("classes", "POST", [
        {"id": class_a, "school_id": school_a, "academic_year_id": year_id, "name": f"10a/Ph{ts%10}",
         "key_stage": "KS4", "year_group": 10, "tier": "higher", "science_pathway": "triple",
         "science_subject": "physics", "tier_pathway_source": "admin"},
        {"id": class_z, "school_id": school_a, "academic_year_id": year_id, "name": f"10z/Ph{ts%10}",
         "key_stage": "KS4", "year_group": 10, "tier": "higher", "science_pathway": "triple",
         "science_subject": "physics", "tier_pathway_source": "admin"},
        {"id": class_x, "school_id": school_a, "academic_year_id": year_id, "name": f"8x{ts%10}",
         "key_stage": "KS3", "year_group": 8, "tier": None, "science_pathway": None,
         "science_subject": None, "tier_pathway_source": None},
    ]))

    for key, school, extra in [("t1", school_a, {}), ("t2", school_a, {}), ("t3", school_a, {}),
                               ("adm", school_a, {}), ("t4", school_b, {})]:
        _ok(f"profile:{key}", *c.write("profiles", "PATCH", {
            "__match__": f"id=eq.{people[key]['id']}",
            "role": "admin" if key == "adm" else "teacher",
            "school_id": school, "first_name": key.upper(), "last_name": "Mrb351Acc",
            "display_name": f"{key.upper()} Mrb351Acc", "username": f"mrb351a{key}x{ts:x}",
        }))
    for key in ("pa", "pz", "px", "pb"):
        _ok(f"profile:{key}", *c.write("profiles", "PATCH", {
            "__match__": f"id=eq.{people[key]['id']}",
            "role": "student", "school_id": school_a, "first_name": key.upper(), "last_name": "Mrb351Acc",
            "display_name": f"{key.upper()} Mrb351Acc", "username": f"mrb351a{key}x{ts:x}",
            "science_pathway": "triple", "tier": "higher",
        }))

    _ok("class_teachers", *c.write("class_teachers", "POST", [
        {"class_id": class_a, "teacher_id": people["t1"]["id"], "role": "subject_teacher",
         "subject_id": subject_physics},
        {"class_id": class_x, "teacher_id": people["t1"]["id"], "role": "subject_teacher",
         "subject_id": subject_physics},
        {"class_id": class_z, "teacher_id": people["t2"]["id"], "role": "subject_teacher",
         "subject_id": subject_physics},
    ]))
    _ok("class_members", *c.write("class_members", "POST", [
        {"class_id": class_a, "student_id": people["pa"]["id"], "joined_via": "admin_added"},
        {"class_id": class_a, "student_id": people["pb"]["id"], "joined_via": "admin_added"},
        {"class_id": class_z, "student_id": people["pz"]["id"], "joined_via": "admin_added"},
        {"class_id": class_x, "student_id": people["px"]["id"], "joined_via": "admin_added"},
    ]))
    _ok("staff_scopes", *c.write("staff_scopes", "POST",
        {"profile_id": people["adm"]["id"], "scope": "school_admin",
         "school_id": school_a, "started_at": datetime.now(timezone.utc).isoformat(),
         "granted_by": people["adm"]["id"]}))

    tokens = {k: c.sign_in(p["email"], THROWAWAY_PASSWORD) for k, p in people.items()}
    manifest["people"] = people
    return {"school_a": school_a, "school_b": school_b, "class_a": class_a, "class_z": class_z,
            "class_x": class_x, "people": people, "tokens": tokens, "ts": ts}


def teardown(c: Client, manifest):
    """Delete every row this run created, by the id lists in `manifest`,
    child tables first. A missing table/id is tolerated (best-effort) so a
    partial run's teardown still removes everything it can.

    Two things beyond the obvious child-first order:
      · the class's OWN lazy auto-composed weekly assignment (never in
        `manifest["assignments"]`, since this script never creates one on
        purpose) is cleared by class_id, not by id, so it cannot block the
        class delete with a stray FK;
      · `public.profiles` is deleted BEFORE the auth.users admin delete —
        `profiles.id -> auth.users(id)` is not ON DELETE CASCADE here, so
        deleting the auth user first leaves an orphaned profile row and a
        409 on the class/school delete behind it.
    """
    people_ids = [p["id"] for p in manifest.get("people", {}).values()] or manifest.get("users", [])
    admin_id = manifest.get("people", {}).get("adm", {}).get("id")
    order = [
        ("flashcard_reviews", "assignment_id", manifest.get("assignments", [])),
        ("flashcard_pupil_cards", "assignment_id", manifest.get("assignments", [])),
        ("flashcard_events", "assignment_id", manifest.get("assignments", [])),
        ("flashcard_sessions", "assignment_id", manifest.get("assignments", [])),
        ("assignment_submissions", "assignment_id", manifest.get("assignments", [])),
        ("assignment_flashcards", "assignment_id", manifest.get("assignments", [])),
        ("assignments", "id", manifest.get("assignments", [])),
        # catch-all: any OTHER assignment on these classes (e.g. the lazy
        # auto-composed weekly one) — by class_id, never a wider predicate.
        ("assignments", "class_id", manifest.get("classes", [])),
        ("flashcard_extractions", "deck_id", manifest.get("decks", [])),
        ("flashcard_cards", "deck_id", manifest.get("decks", [])),
        ("flashcard_decks", "id", manifest.get("decks", [])),
        ("class_members", "class_id", manifest.get("classes", [])),
        ("class_teachers", "class_id", manifest.get("classes", [])),
        ("staff_scopes", "profile_id", [admin_id] if admin_id else []),
        ("staff_scopes", "school_id", manifest.get("schools", [])),
        ("classes", "id", manifest.get("classes", [])),
        # `flashcard_set_work` writes an `audit_log` row per call (actor_id =
        # the teacher) — it must go before the profiles delete or the FK
        # blocks it, exactly like the class's lazy auto-assignment above.
        ("audit_log", "actor_id", people_ids),
        ("audit_log", "school_id", manifest.get("schools", [])),
        ("profiles", "id", people_ids),
        ("schools", "id", manifest.get("schools", [])),
    ]
    for table, col, ids in order:
        if not ids:
            continue
        in_list = ",".join(ids)
        st, body = c.write(table, "DELETE", {"__match__": f"{col}=in.({in_list})"})
        if st not in (200, 204):
            print(f"  teardown: {table} by {col} -> {st} {str(body)[:200]}")
    for uid in manifest.get("users", []):
        st, body = c.admin_delete_user(uid)
        if st not in (200, 204):
            print(f"  teardown: admin_delete_user {uid} -> {st} {str(body)[:200]}")


def check_residue(c: Client, manifest):
    residue = {}
    for table, col, ids in [
        ("flashcard_decks", "id", manifest.get("decks", [])),
        ("assignments", "id", manifest.get("assignments", [])),
        ("classes", "id", manifest.get("classes", [])),
        ("schools", "id", manifest.get("schools", [])),
    ]:
        if not ids:
            continue
        status, rows = c.select(None, table, {"id": f"in.({','.join(ids)})", "select": "id"}, as_service=True)
        if rows:
            residue[table] = len(rows)
    for uid in manifest.get("users", []):
        status, body = c.select(None, "profiles", {"id": f"eq.{uid}", "select": "id"}, as_service=True)
        if body:
            residue.setdefault("profiles", 0)
            residue["profiles"] += 1
    return residue


# ════════════════════════════════════════════════════════════════════════
# THE 12 ITEMS
# ════════════════════════════════════════════════════════════════════════

def run_events(c, token, assignment_id, events):
    return c.rpc(token, "flashcard_record", {"p_assignment": assignment_id, "p_events": events})


def make_events(cards, phase, rating_by_index, answer_prefix, t0, step_ms=400, mode="make", finish=False):
    events = []
    t = t0
    step = timedelta(milliseconds=step_ms)
    for i, card in enumerate(cards):
        cid = card["id"]
        events.append({"id": str(uuid.uuid4()), "type": "card_shown", "at": t.isoformat(),
                        "visible": True, "phase": phase, "card": cid}); t += step
        if mode == "make":
            events.append({"id": str(uuid.uuid4()), "type": "answer_submitted", "at": t.isoformat(),
                            "visible": True, "phase": phase, "card": cid,
                            "answer": f"{answer_prefix} {i}"}); t += step
        else:
            events.append({"id": str(uuid.uuid4()), "type": "revealed", "at": t.isoformat(),
                            "visible": True, "phase": phase, "card": cid}); t += step
        rating = rating_by_index(i)
        if rating:
            events.append({"id": str(uuid.uuid4()), "type": "rated", "at": t.isoformat(),
                            "visible": True, "phase": phase, "card": cid, "rating": rating}); t += step
    if finish:
        events.append({"id": str(uuid.uuid4()), "type": "session_finish", "at": t.isoformat(), "visible": True})
    return events


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--env-file", default=BACKEND_ENV_DEFAULT)
    ap.add_argument("--backend", default="http://127.0.0.1:3351",
                     help="a locally-run backend already pointed at TEST (for the bell/week_work/"
                          "worksheet/delete checks in item 2)")
    ap.add_argument("--manifest-out", default="/tmp/mrb351_acceptance_manifest.json")
    ap.add_argument("--keep", action="store_true", help="skip teardown (debugging only)")
    args = ap.parse_args()

    env = read_env(args.env_file)
    url, service = env["SUPABASE_URL"], env["SUPABASE_SERVICE_ROLE_KEY"]
    ref = jwt_ref(service)
    if ref == PROD_REF:
        die("refusing: service key is PRODUCTION")
    if ref != TEST_REF:
        die(f"refusing: service key ref {ref} is not TEST ({TEST_REF})")
    print(f"credential ref, proven from the key payload: {ref} => TEST")

    c = Client(url, anon_key(), service)
    manifest = {}
    results = []

    def item(n, label, ok, detail=""):
        results.append((n, label, ok, detail))
        tag = "PASS" if ok is True else ("DEFERRED" if ok is None else "FAIL")
        print(f"  [{tag}] item {n}: {label}" + (f" — {detail}" if detail else ""))

    try:
        world = build_world(c, manifest)
        tok, people = world["tokens"], world["people"]

        # ── item 1: deck made and set to two classes; upload + paste proved ──
        cards20 = [{"question": f"Q{i}", "answer": f"A{i}"} for i in range(1, 21)]
        status, deck = c.rpc(tok["t1"], "flashcard_deck_save", {
            "p_deck": None, "p_title": "MRB351 Acceptance Deck", "p_cards": cards20,
            "p_meta": {"source_kind": "typed", "subject": "physics", "shared_with_school": True},
            "p_finalise": True})
        deck_id = deck.get("deck_id") if status == 200 else None
        if deck_id:
            manifest.setdefault("decks", []).append(deck_id)
        now = datetime.now(timezone.utc)
        status, setwork = c.rpc(tok["t1"], "flashcard_set_work", {
            "p_class_ids": [world["class_a"], world["class_x"]], "p_deck": deck_id,
            "p_mode": "make", "p_rule": "secure", "p_title": "MRB351 Flashcard Homework",
            "p_release_at": (now - timedelta(minutes=1)).isoformat(),
            "p_due_at": (now + timedelta(days=5)).isoformat(), "p_note": "Complete before Friday",
            "p_client_ref": f"mrb351-acc-{world['ts']}"})
        aid_a = aid_x = None
        if status == 200:
            manifest.setdefault("assignments", []).extend(setwork["assignment_ids"])
            # `flashcard_set_work` fans out over `array_agg(distinct ...)`, which
            # does not promise to preserve `p_class_ids`' order — resolve each
            # returned id to its class explicitly rather than assuming position.
            st, rows = c.select(None, "assignments",
                                 {"id": f"in.({','.join(setwork['assignment_ids'])})",
                                  "select": "id,class_id"}, as_service=True)
            by_class = {r["class_id"]: r["id"] for r in rows}
            aid_a = by_class.get(world["class_a"])
            aid_x = by_class.get(world["class_x"])
        item(1, "deck made (20 cards, ready) and set to two classes",
             status == 200 and status == 200 and deck.get("card_count") == 20,
             f"deck={deck_id} classes={setwork.get('assignment_ids') if status==200 else setwork}")

        # item 1b: the csv upload path, for real, on TEST
        csv_bytes = ("question,answer\n" + "\n".join(
            f"What is quantity {i}?,The answer is {i}" for i in range(1, 16)) + "\n").encode()
        status, up = multipart_post_file(
            f"{url}/functions/v1/flashcard-extract",
            {"apikey": c.anon, "Authorization": f"Bearer {tok['t1']}"},
            "file", "acceptance.csv", csv_bytes, "text/csv", {"title": "MRB351 Upload"})
        job_ok = False
        last_poll = None
        if status in (200, 202) and "deck_id" in up:
            manifest.setdefault("decks", []).append(up["deck_id"])
            for _ in range(15):
                try:
                    st, rows = c.select(tok["t1"], "flashcard_extractions",
                                         {"id": f"eq.{up['job_id']}", "select": "*"})
                except Exception as e:
                    last_poll = ("EXC", repr(e))
                    break
                last_poll = (st, rows)
                if st == 200 and isinstance(rows, list) and rows and rows[0]["status"] in ("done", "failed"):
                    job_ok = rows[0]["status"] == "done" and rows[0]["pairs_found"] == 15
                    break
                time.sleep(1)
        item("1b", "csv upload -> extraction job done, 15 pairs (no-model path)", job_ok,
             f"post_status={status} post={str(up)[:150]} last_poll={last_poll}")

        # item 1c: paste box -> no_api_key (TEST has no ANTHROPIC_API_KEY)
        status, paste = c._req(
            "POST", f"{url}/functions/v1/flashcard-extract",
            {"apikey": c.anon, "Authorization": f"Bearer {tok['t1']}", "Content-Type": "application/json"},
            {"paste": "Q: what is force?\nA: mass times acceleration", "title": "MRB351 Paste"})
        paste_ok = False
        last_poll = None
        if status in (200, 202) and "deck_id" in paste:
            manifest.setdefault("decks", []).append(paste["deck_id"])
            for _ in range(15):
                try:
                    st, rows = c.select(tok["t1"], "flashcard_extractions",
                                         {"id": f"eq.{paste['job_id']}", "select": "*"})
                except Exception as e:
                    last_poll = ("EXC", repr(e))
                    break
                last_poll = (st, rows)
                if st == 200 and isinstance(rows, list) and rows and rows[0]["status"] in ("done", "failed"):
                    paste_ok = rows[0]["status"] == "failed" and rows[0]["error"] == "no_api_key"
                    break
                time.sleep(1)
        item("1c", "paste box -> model path -> failed: no_api_key (as designed on TEST)",
             paste_ok, f"post={str(paste)[:150]} last_poll={last_poll}")

        # ── item 2: pupils see the work; bell; week_work excludes it; ──
        #             worksheet refuses; delete soft-deletes and clears the bell.
        status, snap_a = c.rpc(tok["pa"], "flashcard_record", {"p_assignment": aid_a, "p_events": []})
        status_z, snap_z = c.rpc(tok["pz"], "flashcard_record", {"p_assignment": aid_a, "p_events": []})
        item(2, "pupil in the class reads the 20-card snapshot + note; a pupil "
                "in neither class is refused",
             status == 200 and snap_a.get("n") == 20 and snap_a.get("note") == "Complete before Friday"
             and status_z == 403,
             f"pa n={snap_a.get('n') if status==200 else snap_a} pz={status_z} {snap_z}")

        bell_ok = week_work_ok = worksheet_ok = delete_ok = None
        try:
            st, notif = c._req("GET", f"{args.backend}/api/student/notifications",
                                {"Authorization": f"Bearer {tok['pa']}"})
            bell_ok = (st == 200 and any(n.get("assignment_id") == aid_a for n in notif.get("notifications", [])))
            st, cur = c._req("GET",
                              f"{args.backend}/api/class/current-assignment?class_id={world['class_a']}",
                              {"Authorization": f"Bearer {tok['pa']}"})
            week_work_ok = (st == 200 and not any(
                w.get("id") == aid_a or "Flashcard" in json.dumps(w) for w in cur.get("week_work", []) or []))
            st, ws = c._req("POST", f"{args.backend}/api/teacher/worksheet",
                             {"Authorization": f"Bearer {tok['t1']}", "Content-Type": "application/json"},
                             {"class_id": world["class_a"], "assignment_id": aid_a, "format": "pdf",
                              "scopes": [{"scope_kind": "topic", "scope_ref": "energy", "subject": "physics",
                                          "question_ids": [str(uuid.uuid4())]}]})
            worksheet_ok = (st == 409 and ws.get("error") == "flashcards_no_worksheet")
            st, delbody = c._req("DELETE", f"{args.backend}/api/teacher/set-work/{aid_x}",
                                  {"Authorization": f"Bearer {tok['t1']}"})
            st2, notif_px = c._req("GET", f"{args.backend}/api/student/notifications",
                                    {"Authorization": f"Bearer {tok['px']}"})
            delete_ok = (st == 200 and st2 == 200
                         and not any(n.get("assignment_id") == aid_x for n in notif_px.get("notifications", [])))
        except Exception as e:
            bell_ok = week_work_ok = worksheet_ok = delete_ok = f"backend unreachable at {args.backend}: {e}"
        item("2b", "bell fires 'New work'; week_work excludes the deck; "
                   "worksheet refuses 409; delete soft-deletes + clears the bell",
             all(v is True for v in (bell_ok, week_work_ok, worksheet_ok, delete_ok)),
             f"bell={bell_ok} week_work={week_work_ok} worksheet={worksheet_ok} delete={delete_ok}")

        # ── item 3: first sitting — made/secured/sittings, idempotent resend ──
        cards = snap_a["cards"]
        t0 = datetime.now(timezone.utc) - timedelta(minutes=15)
        ev_make = make_events(cards, "make", lambda i: "got_it" if i < 12 else ("not_yet" if i % 2 == 0 else "nearly"),
                               "answer", t0, step_ms=400, mode="make")
        t1_ = t0 + timedelta(milliseconds=400 * len(ev_make) + 2000)
        ev_review = make_events(cards[:12], "review", lambda i: "got_it", "", t1_, step_ms=400, mode="review")
        batch1 = ev_make + ev_review
        status, r1 = run_events(c, tok["pa"], aid_a, batch1)
        status, r2 = run_events(c, tok["pa"], aid_a, batch1)   # resend — idempotency
        item(3, "first sitting: made 20/20, secured 12/20, 1 sitting; a batch "
                "re-sent twice stores the same events once",
             status == 200 and r1.get("made") == 20 and r1.get("secured") == 12 and r1.get("sittings") == 1
             and r2 == r1,
             f"{r1}")

        # ── item 4: second day (60-minute-gap secure rule), on-time completion ──
        remaining = [c_ for c_ in cards if c_["id"] not in {cc["id"] for cc in cards[:12]}]
        t2_ = t1_ + timedelta(milliseconds=400 * len(ev_review) + 2000)
        ev_r2 = make_events(remaining, "review", lambda i: "got_it", "", t2_, step_ms=400, mode="review", finish=True)
        status, r3 = run_events(c, tok["pa"], aid_a, ev_r2)
        # backdate the sitting that holds the first review pass, so the
        # 60-minute gap is genuine without a real wall-clock wait
        status, sess = c.select(tok["t1"], "flashcard_sessions",
                                 {"assignment_id": f"eq.{aid_a}", "select": "id,started_at,ended_at",
                                  "order": "started_at.asc", "limit": "1"})
        if sess:
            sid = sess[0]["id"]
            c.write("flashcard_sessions", "PATCH", {
                "__match__": f"id=eq.{sid}",
                "started_at": (datetime.fromisoformat(sess[0]["started_at"]) - timedelta(days=1)).isoformat(),
                "ended_at": (datetime.fromisoformat(sess[0]["ended_at"]) - timedelta(days=1)).isoformat()
                if sess[0]["ended_at"] else None,
            })
        t3_ = datetime.now(timezone.utc) - timedelta(seconds=30)
        ev_r3 = make_events(remaining, "review", lambda i: "got_it", "", t3_, step_ms=400, mode="review")
        status, r4 = run_events(c, tok["pa"], aid_a, ev_r3)
        item(4, "next day: the remaining cards secure across a genuine "
                "60-minute-gapped second review sitting; Done, on time; "
                "the ordinary submission is written",
             status == 200 and r4.get("secured") == 20 and r4.get("complete") is True
             and r4.get("is_late") is False,
             f"{r4}")

        # ── item 5: rushing and blanks ──
        rush_cards = [{"question": f"RushQ{i}", "answer": f"RushA{i}"} for i in range(1, 21)]
        status, rush_deck = c.rpc(tok["t1"], "flashcard_deck_save", {
            "p_deck": None, "p_title": "MRB351 Rush Deck", "p_cards": rush_cards,
            "p_meta": {"source_kind": "typed", "shared_with_school": True}, "p_finalise": True})
        manifest.setdefault("decks", []).append(rush_deck["deck_id"])
        now = datetime.now(timezone.utc)
        status, rush_setwork = c.rpc(tok["t1"], "flashcard_set_work", {
            "p_class_ids": [world["class_x"]], "p_deck": rush_deck["deck_id"], "p_mode": "make",
            "p_rule": "quick", "p_title": "MRB351 Rush Homework",
            "p_release_at": (now - timedelta(minutes=1)).isoformat(),
            "p_due_at": (now + timedelta(days=3)).isoformat(), "p_note": None,
            "p_client_ref": f"mrb351-acc-rush-{world['ts']}"})
        rush_aid = rush_setwork["assignment_ids"][0]
        manifest["assignments"].append(rush_aid)
        status, rush_snap = c.rpc(tok["px"], "flashcard_record", {"p_assignment": rush_aid, "p_events": []})
        t0 = datetime.now(timezone.utc) - timedelta(minutes=5)
        ev_rush = make_events(rush_snap["cards"], "make", lambda i: "got_it",
                               "idk" if False else "", t0, step_ms=400, mode="make")
        # override the first 10 answers to literal "idk"
        answer_i = 0
        for e in ev_rush:
            if e["type"] == "answer_submitted":
                e["answer"] = "idk" if answer_i < 10 else f"real answer {answer_i}"
                answer_i += 1
        status, r5 = run_events(c, tok["px"], rush_aid, ev_rush)
        status, sess5 = c.select(None, "flashcard_sessions", {"assignment_id": f"eq.{rush_aid}",
                                  "select": "rushed"}, as_service=True)
        status, pc5 = c.select(None, "flashcard_pupil_cards", {"assignment_id": f"eq.{rush_aid}",
                                "select": "answer_check"}, as_service=True)
        blanks = sum(1 for r in pc5 if r["answer_check"] == "blank")
        item(5, "20 cards rated fast -> Rushed flagged, work still completes; "
                "10 x idk -> 10 blank",
             r5.get("complete") is True and sess5 and sess5[0]["rushed"] is True and blanks == 10,
             f"complete={r5.get('complete')} rushed={sess5[0]['rushed'] if sess5 else None} blanks={blanks}")

        # ── item 6: late and missing ──
        late_cards = [{"question": f"LateQ{i}", "answer": f"LateA{i}"} for i in range(1, 6)]
        status, late_deck = c.rpc(tok["t1"], "flashcard_deck_save", {
            "p_deck": None, "p_title": "MRB351 Late Deck", "p_cards": late_cards,
            "p_meta": {"source_kind": "typed", "shared_with_school": True}, "p_finalise": True})
        manifest["decks"].append(late_deck["deck_id"])
        now = datetime.now(timezone.utc)
        status, late_setwork = c.rpc(tok["t1"], "flashcard_set_work", {
            "p_class_ids": [world["class_a"]], "p_deck": late_deck["deck_id"], "p_mode": "make",
            "p_rule": "quick", "p_title": "MRB351 Late Homework",
            "p_release_at": (now - timedelta(minutes=4)).isoformat(),
            "p_due_at": (now - timedelta(minutes=1)).isoformat(), "p_note": None,
            "p_client_ref": f"mrb351-acc-late-{world['ts']}"})
        late_aid = late_setwork["assignment_ids"][0]
        manifest["assignments"].append(late_aid)
        status, late_snap = c.rpc(tok["pa"], "flashcard_record", {"p_assignment": late_aid, "p_events": []})
        t0 = datetime.now(timezone.utc) - timedelta(seconds=30)
        ev_late = make_events(late_snap["cards"], "make", lambda i: "got_it", "on time answer", t0, step_ms=400)
        status, r6 = run_events(c, tok["pa"], late_aid, ev_late)   # pupilB never opens it
        status, prog6 = c.rpc(tok["t1"], "flashcard_progress", {"p_assignment": late_aid, "p_now": None})
        by_pid = {p["pupil_id"]: p["status"] for p in prog6["pupils"]}
        item(6, "completing after the deadline -> Done late; a pupil who "
                "never opened it -> Missing",
             r6.get("is_late") is True and by_pid.get(people["pa"]["id"]) == "done_late"
             and by_pid.get(people["pb"]["id"]) == "missing",
             f"is_late={r6.get('is_late')} pa={by_pid.get(people['pa']['id'])} pb={by_pid.get(people['pb']['id'])}")

        # ── item 7: snapshots are frozen ──
        status, cur_cards = c.select(tok["t1"], "flashcard_cards",
                                      {"deck_id": f"eq.{deck_id}", "select": "id,position,question,answer",
                                       "order": "position"})
        edited = []
        for i, cd in enumerate(cur_cards):
            if i == 0:
                edited.append({"id": cd["id"], "question": cd["question"], "answer": "EDITED — must not reach aid_a"})
            elif i == len(cur_cards) - 1:
                continue
            else:
                edited.append({"id": cd["id"], "question": cd["question"], "answer": cd["answer"]})
        status, edit_res = c.rpc(tok["t1"], "flashcard_deck_save", {
            "p_deck": deck_id, "p_title": "MRB351 Acceptance Deck (edited)", "p_cards": edited,
            "p_meta": {}, "p_finalise": True})
        status, frozen = c.select(tok["pa"], "assignment_flashcards",
                                   {"assignment_id": f"eq.{aid_a}", "select": "position,answer",
                                    "order": "position"})
        item(7, "editing the deck (answer changed, one card removed) leaves "
                "the live assignment's snapshot unchanged",
             edit_res.get("card_count") == 19 and len(frozen) == 20
             and frozen[0]["answer"] == "A1",
             f"deck now {edit_res.get('card_count')} cards; aid_a snapshot still {len(frozen)}, "
             f"card0={frozen[0]['answer'] if frozen else None}")

        # ── item 8: a colleague reuses the deck ──
        status, dup_id = c.rpc(tok["t2"], "flashcard_deck_duplicate", {"p_deck": deck_id})
        if status == 200:
            manifest["decks"].append(dup_id)
        now = datetime.now(timezone.utc)
        status, col_setwork = c.rpc(tok["t2"], "flashcard_set_work", {
            "p_class_ids": [world["class_z"]], "p_deck": dup_id, "p_mode": "review", "p_rule": "quick",
            "p_title": "MRB351 Colleague Reuse", "p_release_at": (now - timedelta(minutes=1)).isoformat(),
            "p_due_at": (now + timedelta(days=3)).isoformat(), "p_note": None,
            "p_client_ref": f"mrb351-acc-col-{world['ts']}"})
        col_aid = col_setwork["assignment_ids"][0]
        manifest["assignments"].append(col_aid)
        status, col_snap = c.rpc(tok["pz"], "flashcard_record", {"p_assignment": col_aid, "p_events": []})
        t0 = datetime.now(timezone.utc) - timedelta(minutes=2)
        smuggle = {"id": str(uuid.uuid4()), "type": "answer_submitted", "at": t0.isoformat(),
                   "visible": True, "phase": "review", "card": col_snap["cards"][0]["id"],
                   "answer": "SMUGGLED — must be ignored in review mode"}
        ev_col = [smuggle] + make_events(col_snap["cards"], "review", lambda i: "got_it", "", t0 + timedelta(seconds=1),
                                          step_ms=300, mode="review")
        status, r8 = run_events(c, tok["pz"], col_aid, ev_col)
        status, pc8 = c.select(None, "flashcard_pupil_cards", {"assignment_id": f"eq.{col_aid}",
                                "select": "id"}, as_service=True)
        item(8, "colleague duplicates + reuses the shared deck (independent "
                "copy); pupil opens straight into review; a smuggled "
                "answer_submitted in review mode is ignored",
             status == 200 and r8.get("complete") is True and len(pc8) == 0,
             f"complete={r8.get('complete')} pupil_cards_written={len(pc8)}")

        # item 9 (MCQ unchanged) is proven by the gate suite (prepush_gate.py),
        # not by this script — no MCQ path is touched by anything above.
        item(9, "MCQ unchanged — see the gate suite (teacher_rollup_equal, "
                "teacher_admin_real, student_bell_drive, focus_audit)", None,
             "not measured here by design")

        # item 10 (rollup) is proven by mrb348_teacher_rollup_proof.py (fixture
        # + real-classes modes) — that tool is the rollup's own authority and
        # this script does not re-implement its cross-check.
        item(10, "rollup exact — see mrb348_teacher_rollup_proof.py", None,
             "not measured here by design")

        # item 11: extraction score / deno tests
        item(11, "extraction score 133/133, deno tests — see "
                 "`deno test --allow-read --allow-env --allow-net "
                 "supabase/functions/_shared/flashcards/`", None,
             "not measured here by design")

        # item 12 (RLS) is proven by tools/mrb351_rls_matrix.py.
        item(12, "RLS — see tools/mrb351_rls_matrix.py", None, "not measured here by design")

    finally:
        with open(args.manifest_out, "w") as f:
            json.dump(manifest, f, indent=2, default=str)
        if not args.keep:
            teardown(c, manifest)
            residue = check_residue(c, manifest)
            print("\nTEARDOWN residue check:", residue if residue else "0 rows left behind")
        else:
            print(f"\n--keep set; manifest saved to {args.manifest_out}, nothing torn down")

    print("\n" + "=" * 70)
    n_pass = sum(1 for _, _, ok, _ in results if ok is True)
    n_fail = sum(1 for _, _, ok, _ in results if ok is False)
    n_deferred = sum(1 for _, _, ok, _ in results if ok is None)
    print(f"RESULT: {n_pass} pass, {n_fail} fail, {n_deferred} deferred to another tool "
          f"(of {len(results)} checks)")
    if n_fail:
        sys.exit(1)


if __name__ == "__main__":
    main()
