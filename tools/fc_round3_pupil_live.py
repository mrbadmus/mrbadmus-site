#!/usr/bin/env python3
"""fc_round3_pupil_live.py — Flashcards, round 3 (8 Oct 2026), the PUPIL side,
proved live on the TEST project with the real class page, the real engine and
the real database.

  UNIT 1 — a real attempt opens Secured. After Check, a mash ("asdf kkkk")
           leaves Secured greyed (disabled, aria-disabled, opacity .4) with
           Nearly / Not yet open; one real word opens it; own words after
           "I don't know" (the crude-oil card, in the pupil's words) open it.
  UNIT 2 — the Mr Badmus nudge. A 10-card deck finished with 3
           "I don't know, then secured" cards shows "A note from Mr Badmus"
           on Done; the same deck finished with 2 shows nothing.

On a phone (390x844) and a desktop (1280x800), light and dark. Screenshots:
r3-live-*.png under gate_tmp()/fc-round3-pupil-live (outside the repo, MRB-346
rule 5); pass --shots docs/experience/y-shots to refresh the committed set on
purpose.

HOW IT IS BUILT — the same way as tools/mrb354_secured_live.py (whose Deno
answer-check stand-in, backend starter, fetch pump and teardown it reuses):
a throwaway TEST world (one teacher, one class, two 10-card review decks, one
fresh pupil per configuration), the real class page served locally, a local
backend at origin/main for the page's boot reads, and the committed
`flashcard-answer-check` edge function under Deno with only the model call
swapped for a deterministic stand-in.

TEARDOWN deletes ONLY the ids this run created (the manifest is a snapshotted
id list — never a predicate), then proves nothing is left behind.

    MRB_BACKEND_DIR=<a checkout of the backend at origin/main> \
        python3 tools/fc_round3_pupil_live.py [--shots DIR]

TEST ONLY — the service key's own `ref` claim is checked before any write and
refused if it is not qeppkiswvclkkwbxmlok. No SQL is needed or applied.
"""
from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
import time
import uuid
from datetime import datetime, timedelta, timezone

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, REPO)
sys.path.insert(0, os.path.join(REPO, "tools"))
os.chdir(REPO)
import mrb351_acceptance as acc  # noqa: E402
import ks3_browser as cdp  # noqa: E402
import mrb351_pupil_flow_live as pf  # noqa: E402  (session_js only)
import mrb354_secured_live as m  # noqa: E402  (stand-in, backend, fetch pump, teardown)
import flashcard_homework_drive as drv  # noqa: E402  (Phone, check, FIT_JS, CONTRAST_JS)

check = drv.check
FAILS = drv.FAILS
settle = drv.settle

# ⊕ 9 Oct 2026 — this defaulted to docs/experience/y-shots, so every run
# overwrote committed reference images. MRB-346 rule 5: never into the repo by
# default. main() sets it from --shots, else gate_tmp()/fc-round3-pupil-live.
SHOTS_DIR = None
BACKEND_DIR = os.environ.get("MRB_BACKEND_DIR",
                             "/Users/midebadmus/Documents/GitHub/mrbadmus-backend-worktrees/fc-round3")
m.BACKEND_DIR = BACKEND_DIR

CRUDE = "Plankton died, were buried under sediment and compressed via heat and pressure over millions of years"
# (question, model answer, ONE real word a pupil would type) — the production
# "Organic Chemistry Quiz" shape; card 0 is the one from Y-REPORT.md.
DECK = [
    ("Describe how crude oil is formed.", CRUDE, "plankton"),
    ("What is a hydrocarbon?", "A compound made of hydrogen and carbon atoms only", "carbon"),
    ("What is the general formula of the alkanes?", "CnH2n+2", "CnH2n+2"),
    ("What is cracking?", "Breaking down long chain hydrocarbons into shorter, more useful molecules", "breaking"),
    ("What is the test for an alkene?", "Bromine water turns from orange to colourless", "bromine"),
    ("What is formed when an alkane burns completely?", "Carbon dioxide and water", "water"),
    ("What happens to viscosity as chain length increases?", "Viscosity increases as the chains get longer", "viscosity"),
    ("What is a functional group?", "The atom or group of atoms that gives a compound its characteristic reactions", "atom"),
    ("What is the unit of energy?", "Joules (J)", "J"),
    ("What does a catalyst do?", "It speeds up the reaction without being used up", "speeds"),
]
Q = [d[0] for d in DECK]
WORD = {d[0]: d[2] for d in DECK}
OWN_CRUDE = "plants died, got buried, heat and pressure"      # Mide's own test, in the pupil's words
MASH_Q = Q[3]                                                # the card that gets keyboard mash first

CONFIGS = [  # (tag, width, height, mobile, theme)
    ("phone-light", 390, 844, True, "light"),
    ("phone-dark", 390, 844, True, "dark"),
    ("desk-light", 1280, 800, False, "light"),
    ("desk-dark", 1280, 800, False, "dark"),
]


def build_world(c, manifest):
    ts = int(time.time())
    school, klass, year = str(uuid.uuid4()), str(uuid.uuid4()), str(uuid.uuid4())
    manifest.update({"schools": [school], "classes": [klass], "years": [year]})
    teacher_email = f"fc3-t-{ts}@throwaway.test"
    tid = c.admin_create_user(teacher_email, acc.THROWAWAY_PASSWORD)
    manifest.setdefault("users", []).append(tid)
    acc._ok("school", *c.write("schools", "POST", {"id": school, "name": f"FC3 {ts}", "code": f"FC3{ts}",
                                                    "kind": "school", "key_stages_supported": ["KS3", "KS4"]}))
    today = datetime.now(timezone.utc).date()
    start = f"{today.year if today.month >= 9 else today.year - 1}-09-01"
    end = f"{int(start[:4]) + 1}-08-31"
    acc._ok("year", *c.write("academic_years", "POST", {"id": year, "school_id": school, "name": "fc3",
                                                         "start_date": start, "end_date": end, "is_current": True}))
    acc._ok("class", *c.write("classes", "POST", {"id": klass, "school_id": school, "academic_year_id": year,
                                                   "name": f"8v/Sc{ts % 10}", "key_stage": "KS3", "year_group": 8}))
    acc._ok("t", *c.write("profiles", "PATCH", {"__match__": f"id=eq.{tid}", "role": "teacher", "school_id": school,
                                                 "first_name": "Tfc", "last_name": "Three", "display_name": "Tfc Three",
                                                 "username": f"fc3t{ts:x}"}))
    st, subj = c.select(None, "subjects", {"select": "id,name", "name": "eq.Chemistry"}, as_service=True)
    acc._ok("class_teachers", *c.write("class_teachers", "POST", {
        "class_id": klass, "teacher_id": tid, "role": "subject_teacher", "subject_id": subj[0]["id"]}))
    tok_t = c.sign_in(teacher_email, acc.THROWAWAY_PASSWORD)
    now = datetime.now(timezone.utc)
    cards = [{"question": q, "answer": a} for q, a, _ in DECK]
    aids = {}
    for key, title in (("A", "Organic A"), ("B", "Organic B")):
        st, deck = c.rpc(tok_t, "flashcard_deck_save", {
            "p_deck": None, "p_title": title, "p_cards": cards,
            "p_meta": {"source_kind": "typed", "subject": "chemistry"}, "p_finalise": True})
        if st != 200:
            acc.die(f"deck save {st} {deck}")
        manifest.setdefault("decks", []).append(deck["deck_id"])
        st, sw = c.rpc(tok_t, "flashcard_set_work", {
            "p_class_ids": [klass], "p_deck": deck["deck_id"], "p_mode": "review", "p_rule": "secure",
            "p_title": title, "p_release_at": (now - timedelta(minutes=1)).isoformat(),
            "p_due_at": (now + timedelta(days=5)).isoformat(), "p_note": None,
            "p_client_ref": f"fc3-{key}-{ts}"})
        if st != 200:
            acc.die(f"set work {st} {sw}")
        manifest.setdefault("assignments", []).extend(sw["assignment_ids"])
        aids[key] = sw["assignment_ids"][0]
    return {"school": school, "class": klass, "teacher": tid, "aids": aids, "ts": ts}


def add_pupil(c, manifest, w, tag):
    email = f"fc3-p-{tag}-{w['ts']}@throwaway.test"
    uid = c.admin_create_user(email, acc.THROWAWAY_PASSWORD)
    manifest.setdefault("users", []).append(uid)
    acc._ok("p", *c.write("profiles", "PATCH", {"__match__": f"id=eq.{uid}", "role": "student", "school_id": w["school"],
                                                 "first_name": "Pfc", "last_name": tag.title(), "display_name": f"Pfc {tag}",
                                                 "username": f"fc3p{abs(hash(tag)) % 10000}{w['ts']:x}", "science_pathway": "combined",
                                                 "tier": "higher"}))
    acc._ok("class_members", *c.write("class_members", "POST", {"class_id": w["class"], "student_id": uid,
                                                                 "joined_via": "admin_added"}))
    return email


def snap(page, name):
    os.makedirs(SHOTS_DIR, exist_ok=True)
    m.shot(page, SHOTS_DIR, name)


def got_state(P):
    return P.q("""(function(){var b=document.querySelector('[data-hw="got_it"]'); if(!b) return null;
      return {disabled: b.disabled, aria: b.getAttribute('aria-disabled'),
              opacity: parseFloat(getComputedStyle(b).opacity)};})()""")


def play(P, page, seen, tag, label, idk_fronts, own_words, first_pass_mash, want_nudge, shots_prefix):
    """Drive one 10-card deck to Done. idk_fronts: cards met with "I don't know" first.
    own_words: {question: own-words text} used after I don't know (default: that card's one word)."""
    shown = {}
    mashed = False
    for _ in range(60):
        s = P.st()
        if s.get("end1") is not None:
            if s.get("retryPass"):
                P.click('[data-hw="retry-pass"]')
                continue
            break
        f = s["front"]
        if f is None:
            time.sleep(0.3)
            continue
        n = shown.get(f, 0)
        shown[f] = n + 1
        if n == 0 and f in idk_fronts:
            P.click('[data-hw="idk"]')
            P.type(own_words.get(f, WORD[f]))
            P.click('[data-hw="check"]')
            s = m.wait_chip(P, page, seen)
            g = got_state(P)
            check("got_it" in s["enabled"] and g["disabled"] is False,
                  f"{tag}/{label}: own words after I don't know ({f[:28]}...) open Secured")
            P.click('[data-hw="got_it"]')
            continue
        if f == MASH_Q and first_pass_mash and not mashed:
            mashed = True
            P.type("asdf kkkk")
            P.click('[data-hw="check"]')
            s = m.wait_chip(P, page, seen)
            g = got_state(P)
            check(sorted(s["enabled"]) == ["nearly", "not_yet"] and g["disabled"] is True and g["aria"] == "true"
                  and abs(g["opacity"] - 0.4) < 0.02,
                  f"{tag}/{label}: after a mash Check Secured is greyed (disabled, aria-disabled, opacity .4) "
                  f"and Nearly / Not yet are open (got {s['enabled']} {g})")
            P.q("window.MRBHomework.active.rate('got_it')")        # what the 3 key and swipe-right call
            settle(0.3)
            check(P.st()["front"] == f and P.st()["rating"], f"{tag}/{label}: the 3 key / swipe do nothing while floored")
            snap(page, f"r3-live-greyed-secured-{tag}")
            P.click('[data-hw="not_yet"]')
            continue
        P.type(WORD[f])
        P.click('[data-hw="check"]')
        s = m.wait_chip(P, page, seen)
        g = got_state(P)
        if n == 0 and f == Q[5]:
            check(g["disabled"] is False and abs(g["opacity"] - 1) < 0.02,
                  f"{tag}/{label}: one real word ({WORD[f]!r}) opens Secured")
        if f == MASH_Q and n > 0:
            check(g["disabled"] is False,
                  f"{tag}/{label}: back on Try again, a real word opens Secured on the card that was mashed")
        P.click('[data-hw="got_it"]')
    settle(1.0)
    s = P.st()
    check(s["end1"] == "10 of 10 secured" and s["done"] == "Done", f"{tag}/{label}: finished, 10 of 10 secured, Done (got {s['end1']!r})")
    has = P.q("!!document.querySelector('[data-hw=\"nudge\"]')")
    check(has is want_nudge, f"{tag}/{label}: the nudge is {'shown' if want_nudge else 'absent'} (got {has})")
    if want_nudge:
        label_t = P.q("(document.querySelector('[data-hw=\"nudge-label\"]')||{}).textContent") or ""
        body = P.q("(document.querySelector('[data-hw=\"nudge-text\"]')||{}).textContent") or ""
        check(label_t.strip().lower() == "a note from mr badmus" and body.startswith("Nice one for finishing."),
              f"{tag}/{label}: the note reads as agreed")
        f = P.q(drv.FIT_JS)
        inside = lambda r: r is not None and r["top"] >= -0.5 and r["bottom"] <= f["vh"] + 0.5
        check(inside(f["nudge"]) and inside(f["done"]) and inside(f["again"]) and (f["dlgScroll"] or 0) <= 1,
              f"{tag}/{label}: nudge, Done and Revise inside the screen, the dialog does not scroll")
        ct = P.q("(%s)('[data-hw=\"nudge-text\"]')" % drv.CONTRAST_JS)
        check(ct is not None and ct >= 4.5, f"{tag}/{label}: nudge text contrast {ct and round(ct, 2)} >= 4.5")
    snap(page, f"r3-live-{'nudge' if want_nudge else 'no-nudge'}-{tag}")
    return s


def main():
    global SHOTS_DIR
    ap = argparse.ArgumentParser()
    ap.add_argument("--shots", default=None,
                    help="screenshot dir (default: gate_tmp()/fc-round3-pupil-live, outside "
                         "the repo; pass docs/experience/y-shots to refresh the committed set)")
    a = ap.parse_args()
    SHOTS_DIR = os.path.abspath(a.shots) if a.shots else os.path.join(cdp.gate_tmp(), "fc-round3-pupil-live")
    print(f"screenshots -> {SHOTS_DIR}")
    env = acc.read_env(acc.BACKEND_ENV_DEFAULT)
    url, service = env["SUPABASE_URL"], env["SUPABASE_SERVICE_ROLE_KEY"]
    ref = acc.jwt_ref(service)
    if ref != acc.TEST_REF:
        acc.die(f"refusing: service key ref {ref} is not TEST ({acc.TEST_REF})")
    print(f"credential ref, proven from the key payload: {ref} => TEST (writing to TEST only)")
    if not os.path.isdir(BACKEND_DIR):
        acc.die(f"backend checkout missing: {BACKEND_DIR} (set MRB_BACKEND_DIR to a checkout at origin/main)")
    c = acc.Client(url, acc.anon_key(), service)
    manifest = {}
    work = os.path.join(os.environ.get("MRB_SHOTS", os.path.expanduser("~/tmp/fc-round3")), "live")
    os.makedirs(work, exist_ok=True)
    mpath = os.path.join(work, "manifest.json")
    stub_log = os.path.join(work, "stub.log")

    sport, bport = m.free_port(), m.free_port()
    origin = f"http://127.0.0.1:{sport}"
    api = f"http://localhost:{bport}"
    backend_proc = deno_proc = site_server = None
    try:
        w = build_world(c, manifest)
        json.dump(manifest, open(mpath, "w"), indent=1)
        backend_proc = m.start_backend(bport, origin, work)
        deno_proc = m.start_deno(url, service, work, stub_log)
        site_server, _ = cdp.serve(REPO, sport)
        print(f"backend {api}, site {origin}, deno :{m.DENO_PORT}")

        for tag, width, height, mobile, theme in CONFIGS:
            print(f"\n── {tag}: {width}x{height} {'phone' if mobile else 'desktop'}, {theme} ──")
            email = add_pupil(c, manifest, w, tag.replace("-", ""))
            json.dump(manifest, open(mpath, "w"), indent=1)
            st, sess = c._req("POST", f"{url}/auth/v1/token?grant_type=password",
                              {"apikey": c.anon, "Content-Type": "application/json"},
                              {"email": email, "password": acc.THROWAWAY_PASSWORD})
            if st != 200:
                acc.die(f"sign-in {email} -> {st} {sess}")
            br = cdp.Browser().start()
            try:
                page = br.attach()
                page.send("Emulation.setDeviceMetricsOverride",
                          {"width": width, "height": height, "deviceScaleFactor": 2 if mobile else 1, "mobile": mobile})
                if mobile:
                    page.send("Emulation.setTouchEmulationEnabled", {"enabled": True, "maxTouchPoints": 5})
                try:
                    page.send("Emulation.setFocusEmulationEnabled", {"enabled": True})
                except cdp.CDPError:
                    pass
                m.enable_fetch(page)
                page.send("Page.addScriptToEvaluateOnNewDocument", {"source": pf.session_js(ref, sess)})
                P = drv.Phone(page, width, height, 0, None)
                seen: set = set()

                # deck A: 3 cards met with "I don't know" then secured -> the nudge
                s = m.open_deck(P, page, origin, api, w["aids"]["A"])
                check(s["strip"] and s["writing"] and s["front"] == Q[0], f"{tag}: deck A opens on the crude-oil card")
                if theme == "dark":
                    P.q("document.documentElement.setAttribute('data-theme','dark')")
                    settle(0.4)
                play(P, page, seen, tag, "A (3 idk)", {Q[0], Q[1], Q[2]}, {Q[0]: OWN_CRUDE}, True, True, "A")
                P.click('[data-hw="done"]')

                # deck B: only 2 -> no nudge
                s = m.open_deck(P, page, origin, api, w["aids"]["B"])
                check(s["strip"] and s["writing"] and s["front"] == Q[0], f"{tag}: deck B opens on the crude-oil card")
                if theme == "dark":
                    P.q("document.documentElement.setAttribute('data-theme','dark')")
                    settle(0.4)
                play(P, page, seen, tag, "B (2 idk)", {Q[1], Q[2]}, {}, False, False, "B")
                errs = m.no_fav(page.console_errors())
                check(not errs, f"{tag}: no console errors ({errs[:2]})")
            finally:
                br.close()
    finally:
        if site_server is not None:
            site_server.shutdown()
            site_server.server_close()
        m.stop_deno(deno_proc)
        m.stop_backend(backend_proc)
        if manifest.get("classes"):
            # ONLY the ids this run created: the manifest is the snapshot.
            st, extra = c.select(None, "assignments", {"class_id": f"in.({','.join(manifest['classes'])})",
                                                        "select": "id"}, as_service=True)
            manifest["auto_assignments"] = [x["id"] for x in (extra or []) if x["id"] not in manifest.get("assignments", [])]
            json.dump(manifest, open(mpath, "w"), indent=1)
            m.teardown(c, manifest)
            residue = {}
            for table, ids in (("schools", manifest.get("schools", [])), ("classes", manifest.get("classes", [])),
                               ("assignments", manifest.get("assignments", []) + manifest.get("auto_assignments", [])),
                               ("profiles", manifest.get("users", []))):
                if ids:
                    st, rows = c.select(None, table, {"id": f"in.({','.join(ids)})", "select": "id"}, as_service=True)
                    if rows:
                        residue[table] = len(rows)
            check(not residue, "teardown by snapshotted id list left nothing behind (%s)" % residue)

    print(f"\n  {len(FAILS)} failed" if FAILS else "\n  all checks passed")
    for f in FAILS:
        print("  - " + f)
    return 1 if FAILS else 0


if __name__ == "__main__":
    sys.exit(main())
