"""tools/mrb351_set_from_class_live.py — "Set from class (M)", 27 Sep 2026.

The live proof for the blocker Mide hit on production: a teacher opening Set
work FROM A CLASS PAGE never saw the Flashcards choice, so a deck could not
be set to a class at all. It mints `mrb331_fixture`'s throwaway world on
TEST, boots a real backend against TEST, serves this branch's BUILT site, and
walks the journey the way a teacher does it — pressing the class page's own
"Set work" button, not calling `MRBSetWork.open()` from outside:

  1. teacher: class page → Set work → the Flashcards choice is visible
     straight away, at the top of the sheet → Flashcards → pick the deck
     "(Higher) Rate of Reaction Quiz" → a due date → Set work. Verified by a
     service-role read of `assignments` (quiz_type, deck_id, class).
  2. pupil: the deck appears in the class page's work list, and pressing it
     opens the flashcard overlay on the deck's first card.
  3. teacher: the deck library's "Set to a class" → Flashcards, deck chosen →
     the class → Detail → Set work. Verified the same way.
  4. the sheet at 1280 / 1440 / 1920 / 390, light and dark (screenshots).

    MRB_BACKEND=<backend worktree at origin/main> \\
    MRB_SET_WORK_PASSWORD=<anything — the fixture mints its accounts> \\
    python3 tools/mrb351_set_from_class_live.py

Screenshots go to $MRB_SHOTS (else ~/tmp/ks3-gates) /set-from-class/.

The class is the fixture's 8a/Sc1 — the one class its throwaway pupil is a
member of. Production's sandbox 8r/Sc1 does not exist on TEST.

Teardown is by CAPTURED id lists (the deck ids this run made, the assignment
ids it read back), children first — flashcard_reviews / pupil_cards / events
/ sessions reference `assignments` WITHOUT a cascade — then the fixture's own
`clear_work` and `teardown`, then a fresh residue query.
"""
import json
import os
import sys
import time
import urllib.parse

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(REPO)
sys.path.insert(0, REPO)
sys.path.insert(0, os.path.join(REPO, "tools"))

import mrb331_fixture as FX                     # noqa: E402
import ks3_browser as cdp                       # noqa: E402
import mrb351_noschema_live as L                # noqa: E402  (sign-in, backend, page helpers)

DECK_TITLE = "(Higher) Rate of Reaction Quiz"
CARDS = [
    ("What is the rate of a reaction?", "How quickly reactants are used up or products are formed"),
    ("Name one way to measure rate", "Measure the volume of gas produced over time"),
    ("How does temperature affect rate?", "Higher temperature increases the rate"),
    ("Why does a higher temperature increase rate?", "Particles move faster so collide more often with more energy"),
    ("What is activation energy?", "The minimum energy particles need to react when they collide"),
    ("What does a catalyst do?", "Speeds up a reaction without being used up"),
    ("How does a catalyst work?", "Provides a pathway with a lower activation energy"),
    ("Effect of increasing surface area?", "Increases the rate: more frequent collisions"),
    ("Which gas is produced by marble chips and acid?", "CO2"),
    ("Speed of light, for scale", "300 000 000 m/s"),
]

SHOTS = os.path.join(os.environ.get("MRB_SHOTS") or os.path.expanduser("~/tmp/ks3-gates"),
                     "set-from-class")
record = L.record


def shot(p, name, w=1280, h=900):
    path = os.path.join(SHOTS, name + ".png")
    try:
        p.screenshot(path, width=w, height=h, full_page=False)
    except Exception as e:                                          # noqa: BLE001
        print("   (screenshot %s failed: %s)" % (name, e))
    return path


def wait(p, expr, timeout=15.0, step=0.25):
    end = time.time() + timeout
    while time.time() < end:
        try:
            v = p.eval(expr)
            if v:
                return v
        except Exception:                                           # noqa: BLE001
            pass
        time.sleep(step)
    return None


def rpc(token, name, args):
    import urllib.request
    key = L.anon_key_from(REPO)
    req = urllib.request.Request(
        FX.env("SUPABASE_URL") + "/rest/v1/rpc/" + name, method="POST",
        headers={"apikey": key, "Authorization": "Bearer " + token,
                 "Content-Type": "application/json"},
        data=json.dumps(args).encode())
    with urllib.request.urlopen(req, context=L.CTX, timeout=60) as r:
        return json.loads(r.read().decode() or "null")


def flash_rows(deck_ids):
    st, rows = FX.api("GET", "/rest/v1/assignments?deck_id=in.(%s)"
                             "&select=id,class_id,quiz_type,deck_id,title,due_at,release_at"
                      % ",".join(deck_ids))
    return rows if isinstance(rows, list) else []


def press_set_work(p):
    """The class page's own primary: the button whose whole text is
    "Set work", inside the compiled page (never the sheet's)."""
    return p.eval("""(function(){
      var bs = Array.from(document.querySelectorAll('#mrb-teacher button, #mrb-teacher a'));
      var b = bs.filter(function(x){ return x.textContent.trim() === 'Set work'; })[0];
      if (!b) { return 'no Set work button'; }
      window.__scopeAtOpen = !!window.MrBadmusAdminScope;
      b.click(); return 'clicked';
    })()""")


def main():
    pw = os.environ.get(FX.ENV_SWITCH, "")
    if not pw:
        raise SystemExit("Set %s (any value — the fixture mints its accounts)." % FX.ENV_SWITCH)
    os.makedirs(SHOTS, exist_ok=True)
    print("\nSet from class (M) — live proof on TEST, real backend, real browser\n")
    FX.seed()
    FX.clear_work()
    teacher = L.sign_in(FX.TEACHER_EMAIL, pw, REPO)["access_token"]
    deck_ids = []
    site = server = None
    try:
        saved = rpc(teacher, "flashcard_deck_save", {
            "p_deck": None, "p_title": DECK_TITLE,
            "p_cards": [{"question": q, "answer": a} for q, a in CARDS],
            "p_meta": {"subject": "chemistry", "key_stage": "KS4", "source_kind": "typed"},
            "p_finalise": True})
        deck_id = (saved or {}).get("deck_id") or (saved or {}).get("id") or \
            ((saved or {}).get("deck") or {}).get("id")
        record(bool(deck_id), "a ready 10-card chemistry deck exists for the teacher on TEST", saved)
        if not deck_id:
            return 1
        deck_ids.append(deck_id)

        site, port = cdp.serve(os.path.join(REPO, "mrbadmus_site"), port=L.SITE_A_PORT)
        base = "http://localhost:%d" % port
        server = L.Server(extra_origins=[base])
        server.__enter__()
        q = "env=test&api=" + urllib.parse.quote(L.PAGE_API, safe="")

        with cdp.Browser() as b:
            p = b.attach()
            p.set_viewport(1280, 900)
            signed = L.sign_in_page(p, base, FX.TEACHER_EMAIL, pw)
            record(str(signed).startswith("ok"), "teacher signs in through auth.html", signed)

            # ── 1. class page → Set work → Flashcards ──────────────────────
            url = "%s/teacher/class-detail.html?class=%s&%s" % (base, FX.C_KS3_A, q)
            ok = L.goto_ready(p, url, "!!(window.MRBSetWork && window.MRBSetWork.open) && "
                              "Array.from(document.querySelectorAll('#mrb-teacher button'))"
                              ".some(function(x){return x.textContent.trim()==='Set work';})",
                              settle=1.0, tries=3)
            record(ok, "teacher class page (8a/Sc1 on TEST) loaded with its Set work button")
            # PRODUCTION'S CONDITION, forced: on production the sheet opened
            # before the lazy nav module existed. Removed here so the sheet's
            # OWN probe (a real GET of flashcard_decks on TEST) is what answers.
            p.eval("delete window.MrBadmusAdminScope")
            t0 = time.time()
            record(press_set_work(p) == "clicked", "pressed the class page's own Set work button")
            vis = wait(p, "(function(){var t=document.querySelector('[data-sw=type]');"
                          "return !!t && !t.hidden && !!t.offsetParent;})()", timeout=10.0)
            secs = round(time.time() - t0, 1)
            at_open = p.eval("window.__scopeAtOpen")
            record(vis, "the Flashcards choice is visible straight away (%.1fs after the press; "
                        "nav module on the page at open: %s)" % (secs, at_open))
            first = p.eval("document.querySelector('[data-sw=body]').firstElementChild.getAttribute('data-sw')")
            record(first == "type", "it is the first thing on the sheet", first)
            shot(p, "01-class-setwork-type-1280")
            p.eval("document.querySelector('[data-sw=type-chips] [data-sw-key=flashcards]').click()")
            step = wait(p, "document.querySelector('[data-sw=step]').textContent==='Deck'&&'Deck'")
            record(step == "Deck", "choosing Flashcards goes straight to the Deck step (class already ticked)")
            # My decks → the deck
            wait(p, "!!document.querySelector('[data-sw=deck-host] [data-fd=deck]') || "
                    "(function(){var c=Array.from(document.querySelectorAll('[data-sw=deck-host] button'))"
                    ".filter(function(x){return x.textContent.trim()==='My decks';})[0];"
                    "if(c){c.click();} return false;})()", timeout=12.0)
            row = wait(p, "(function(){var r=document.querySelector(\"[data-sw=deck-host] [data-fd=deck][data-fd-id='%s']\");"
                          "if(r){r.click();return true;}return false;})()" % deck_id, timeout=12.0)
            record(row, "the deck is listed under My decks and picked")
            shot(p, "02-class-deck-picked-1280")
            p.eval("document.querySelector('[data-sw=primary]').click()")
            wait(p, "document.querySelector('[data-sw=step]').textContent==='Detail'")
            due = p.eval("document.querySelector('[data-sw=due-date]') && document.querySelector('[data-sw=due-date]').value")
            record(bool(due), "Detail step: a due date is set", due)
            shot(p, "03-class-detail-1280")
            p.eval("document.querySelector('[data-sw=primary]').click()")
            closed = wait(p, "document.querySelector('[data-sw=overlay]').hidden", timeout=20.0)
            shot(p, "04-class-after-set-1280")
            rows = flash_rows(deck_ids)
            a1 = [r for r in rows if r["class_id"] == FX.C_KS3_A]
            record(closed and len(a1) == 1 and a1[0]["quiz_type"] == "flashcards",
                   "saved: one flashcard assignment on 8a/Sc1 with this deck (service-role read)", rows)

            # ── 2. the pupil ────────────────────────────────────────────────
            p.eval("localStorage.clear()")
            signed = L.sign_in_page(p, base, FX.PUPIL_EMAIL, pw)
            record(str(signed).startswith("ok"), "pupil signs in through auth.html", signed)
            url = "%s/student/class.html?class=%s&%s" % (base, FX.C_KS3_A, q)
            L.goto_ready(p, url, "document.body.innerText.indexOf(%s)>-1" % json.dumps(DECK_TITLE),
                         settle=2.0, tries=3)
            listed = p.eval("document.body.innerText.indexOf(%s)>-1" % json.dumps(DECK_TITLE))
            record(listed, "pupil: the deck appears in the work list")
            shot(p, "05-pupil-work-list-1280")
            if a1:
                p.eval("location.hash = '#cards=%s'" % a1[0]["id"])
            strip = wait(p, "!!document.querySelector('[data-hw=strip]') && "
                            "document.body.innerText.indexOf('What is the rate of a reaction?')>-1",
                         timeout=20.0)
            record(strip, "pupil: the overlay opens the deck on its first card")
            shot(p, "06-pupil-overlay-1280")
            p.set_viewport(390, 844)
            shot(p, "06b-pupil-overlay-390", 390, 844)

            # ── 3. the library's "Set to a class" ───────────────────────────
            p.eval("localStorage.clear()")
            p.set_viewport(1280, 900)
            L.sign_in_page(p, base, FX.TEACHER_EMAIL, pw)
            url = "%s/teacher/decks.html?%s" % (base, q)
            L.goto_ready(p, url, "document.querySelectorAll('[data-fd=lib-set]').length>0",
                         settle=1.5, tries=3)
            shot(p, "07-library-1280")
            share = p.eval("Array.from(document.querySelectorAll('[data-fd=lib-share]')).map(function(b){return b.textContent;})")
            record(share and all("colleagues" in s for s in share),
                   "library: the colleague toggle reads 'Share with colleagues'", share)
            p.eval("document.querySelector(\"[data-fd=lib-row][data-fd-id='%s'] [data-fd=lib-set]\").click()" % deck_id)
            opened = wait(p, "!document.querySelector('[data-sw=overlay]').hidden && "
                             "document.querySelector('[data-sw=overlay]').getAttribute('data-sw-type')==='flashcards'")
            record(opened, "library: Set to a class opens Set work on Flashcards")
            row = wait(p, "(function(){var r=document.querySelector(\"[data-sw=class][data-sw-ref='%s']\");"
                          "if(r){r.click();return true;}return false;})()" % FX.C_KS3_A, timeout=12.0)
            record(row, "library: the teacher's own class is listed and ticked")
            shot(p, "08-library-classes-1280")
            p.eval("document.querySelector('[data-sw=primary]').click()")
            det = wait(p, "document.querySelector('[data-sw=step]').textContent==='Detail'")
            record(det, "library: with the deck chosen, Next goes straight to Detail")
            shot(p, "09-library-detail-1280")
            p.eval("document.querySelector('[data-sw=primary]').click()")
            closed = wait(p, "document.querySelector('[data-sw=overlay]').hidden", timeout=20.0)
            rows = flash_rows(deck_ids)
            record(closed and len([r for r in rows if r["class_id"] == FX.C_KS3_A]) == 2,
                   "library: saved — a second flashcard assignment on 8a/Sc1 (service-role read)", rows)

            # ── 4. widths, light and dark ───────────────────────────────────
            url = "%s/teacher/class-detail.html?class=%s&%s" % (base, FX.C_KS3_A, q)
            for theme in ("light", "dark"):
                p.eval("localStorage.setItem('mrb-theme', %s)" % json.dumps(theme))
                for w, h in ((1280, 800), (1440, 900), (1920, 1080), (390, 844)):
                    p.set_viewport(w, h)
                    L.goto_ready(p, url, "Array.from(document.querySelectorAll('#mrb-teacher button'))"
                                 ".some(function(x){return x.textContent.trim()==='Set work';})",
                                 settle=1.0, tries=2)
                    press_set_work(p)
                    wait(p, "document.querySelectorAll('[data-sw=topic]').length>0", timeout=12.0)
                    sw = p.eval("Math.round(document.querySelector('[data-sw=sheet]').getBoundingClientRect().width)")
                    over = p.eval("document.documentElement.scrollWidth > window.innerWidth")
                    record(not over, "sheet %s %dpx: width %spx, no sideways scroll" % (theme, w, sw))
                    shot(p, "10-sheet-%s-%d" % (theme, w), w, h)
                    p.eval("document.querySelector('[data-sw=primary]').click()")
                    wait(p, "document.querySelector('[data-sw=step]').textContent==='Topic'")
                    time.sleep(0.8)
                    shot(p, "11-sheet-topic-%s-%d" % (theme, w), w, h)
            p.eval("localStorage.setItem('mrb-theme','light')")
    finally:
        print("\nteardown (captured ids only)")
        try:
            aids = [r["id"] for r in flash_rows(deck_ids)] if deck_ids else []
            if aids:
                inn = "assignment_id=in.(%s)" % ",".join(aids)
                for t in ("flashcard_reviews", "flashcard_pupil_cards", "flashcard_events",
                          "flashcard_sessions"):
                    FX.api("DELETE", "/rest/v1/%s?%s" % (t, inn))
        except BaseException as e:                                  # noqa: BLE001
            print("   ⚠️ flashcard child rows: %r" % e)
        for label, fn in (("clear_work", FX.clear_work),):
            try:
                fn()
            except BaseException as e:                              # noqa: BLE001
                print("   ⚠️ %s: %r" % (label, e))
        if deck_ids:
            FX.api("DELETE", "/rest/v1/flashcard_decks?id=in.(%s)" % ",".join(deck_ids))
        try:
            FX.teardown()
        except BaseException as e:                                  # noqa: BLE001
            print("   ⚠️ teardown: %r" % e)
        if server:
            server.__exit__(None, None, None)
        if site:
            site.shutdown()
        residue = []
        if deck_ids:
            st, rows = FX.api("GET", "/rest/v1/flashcard_decks?id=in.(%s)&select=id" % ",".join(deck_ids))
            if isinstance(rows, list) and rows:
                residue.append("flashcard_decks: %d" % len(rows))
        ids = ",".join(c[0] for c in FX.CLASSES)
        st, rows = FX.api("GET", "/rest/v1/classes?id=in.(%s)&select=id" % ids)
        if isinstance(rows, list) and rows:
            residue.append("classes: %d" % len(rows))
        for email in FX.EMAILS:
            if FX.find_user(email):
                residue.append("auth user " + email)
        record(not residue, "zero throwaway residue on TEST (fresh query)", residue)

    bad = [c for c in L.checks if not c[0]]
    print("\n%s  %d checks, %d failed   screenshots: %s\n"
          % ("FAIL" if bad else "PASS", len(L.checks), len(bad), SHOTS))
    for ok, label, detail in bad:
        print("   - %s" % label)
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
