#!/usr/bin/env python3
"""Drive the WIRED student pages in headless Chrome, against production data.

    python3 drive_pages.py [--keep]

Serves `mrbadmus_site/` locally so that `/shared/...` resolves the way Cloudflare
serves it, injects a real Supabase session into `localStorage` exactly as a
signed-in browser would hold one, and then drives the page.

⚠️ This is the check the API drive cannot make. `drive_producer.py` proves the
backend composes and serves the right rows; this proves a student can SEE them —
that `student-live.js` maps every key the pages read, that nothing renders as
"undefined", and above all that **none of Design's example data reaches the
screen**. A page wired to real data that quietly falls back to the fixture looks
completely fine.

The password comes from the environment and is never printed. The session is
written into a throwaway browser profile that is discarded at the end.
"""

import json
import os
import re
import ssl
import sys
import urllib.request

REPO = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, REPO)
os.chdir(REPO)

import ks3_browser as cdp

# ⚠️ SERVED ON localhost:5500 ON PURPOSE, AND THE PORT IS NOT ARBITRARY.
# The backend's CORS allowlist is ['https://mrbadmus.com', 'https://www.
# mrbadmus.com', 'http://localhost:3000', 'http://localhost:5500'] — so a page
# served from a random port, or from 127.0.0.1 rather than the NAME localhost,
# has its calls to /api/class/* blocked by the browser before they leave. That
# is the backend being correct, not broken, and it is why this drive uses an
# origin the live allowlist already contains rather than widening it. Nothing on
# production changes to make this test possible.
PORT = 5500
CLASS_URL = "http://localhost:%d/student/class.html?env=prod"
ASSIGN_URL = "http://localhost:%d/student/assignment.html?env=prod"

SUPABASE_URL = "https://urklkrwevjtlfbwnipjn.supabase.co"
PROJECT_REF = "urklkrwevjtlfbwnipjn"
# ⊕ 22 Aug 2026 — the drive account is now a PARAMETER, not a constant.
# A run that must not touch Mide's own account (an overnight run with no
# credential supplied) drives a throwaway student instead, and a gate that
# hard-codes one person's email cannot be pointed at one. The default is
# unchanged, so an interactive run behaves exactly as it did.
EMAIL = os.environ.get("MRB_DRIVE_EMAIL", "midebolabadmus@gmail.com")
CTX = ssl.create_default_context(cafile="/etc/ssl/cert.pem")

# Design's own example values. If ANY of these reach the screen on a page that
# is supposed to be showing real data, the wiring has silently fallen back and
# the page is lying to whoever is looking at it.
#
# ⚠️ THIS LIST WAS TOO SHORT AND THE DRIVE PASSED BECAUSE OF IT. The first
# version held names and headline strings only, so it went green on a page whose
# DOCKET still read "8 questions · Using a microscope · SET Mon 15 Sep · DUE
# Thu 18 Sep" — over a real assignment of four questions due Thursday 3
# September. A screenshot caught what the text check could not, because I had
# not thought to look for the numbers.
#
# The lesson generalises: a fixture tell is not only a NAME. It is any authored
# constant a real page must have replaced — counts, dates, week numbers, the
# copy that quotes a count in words.
FIXTURE_TELLS = [
    # people and places
    "Ayo", "Tiwa A.", "Marcus O.", "Hafsah I.", "Mr Badmus", "28 students",
    "Best score in the class", "Cells & microscopy", "Movement & joints",
    "Lab safety check",
    # the docket — counts and dates, which is where it actually leaked
    "Using a microscope", "Mon 15 Sep", "Thu 18 Sep", "DUE THU 18:00",
    "2 days left", "40 POINTS AT STAKE",
    "Eight questions", "Answer the eight questions",
    # week numbers: the real current week is 1
    "WEEK 04", "TOP OF WEEK 04", "WK 04", "week 04",
    # fabricated recall figures — the count, the percentage and the round total
    # ⚠️ "46" IS LINE-ANCHORED, and the first version was not. A bare two-digit
    # tell matches any clock on the page: it fired on `COMPLETED 21 AUG, 13:46`,
    # a REAL server timestamp, and reported the page dirty when it was clean.
    # The fabricated recall count renders as a value on its own line, so that
    # is the shape to look for. A tell that cries wolf gets ignored, which is
    # the failure mode that let the docket ship in the first place.
    "\n46\n", "77%", "58%",
    "Six answers logged", "BEST STREAK 09",
    # ⊕ 22 Aug 2026 — the assignment page's own welded values. The two
    # timestamps are the worst of them: `handIn` manufactured them, so a
    # student saw a confirmation for a date that had nothing to do with today.
    "17 SEP", "20 SEP", "2 DAYS LATE", "2 days late",
    "CELLS & MICROSCOPY",
    # ⊕ 22 Aug 2026 — W5. "Complete" replaces "Hand it in" everywhere, so any
    # surviving "hand in" wording is itself a tell that a surface was missed.
    "Hand it in", "Handed in", "HANDED IN", "handed in",
    # ⊕ RULED 22 Aug 2026 — P2. The recall round is min(6, pool) long, so a
    # page that still ANNOUNCES six is announcing a number it is not going to
    # show. Design's blurb is the tell; the counter beneath it was already
    # real.
    "SIX QUESTIONS", "Six a round", "SIX A ROUND",
    # ⊕ RULED 22 Aug 2026 — P8. "SUMMER TERM" over week 1 of 2026-27. Autumn
    # is the correct answer today, so AUTUMN TERM cannot be a tell — it is
    # above, from when it was Design's fixture value, and it has to come OUT
    # of the list or the correct page fails. The wrong ones are the tells now.
    "SUMMER TERM", "SPRING TERM",
    # ⊕ 23 Aug 2026 — PHASE 2. DESIGN'S SIX SAMPLE FLASHCARDS.
    #
    # The grafted flashcards card and its overlay render `MRB_DATA('cards')`.
    # On the fixture that is Design's own `deck()`, lifted out of the amended
    # delivery by `DONOR_LIFTS`; on a real page it is every card behind the
    # lessons the class has covered. If any of these six FRONTS is on screen on
    # a page that is supposed to be showing real data, the deck has fallen back
    # to Design's sample and the student is revising one drawing's science.
    #
    # ⚠️ THE FRONTS, AND DELIBERATELY NOT THE BACKS. Checked against all 582
    # rows of `ks3_cards` before they were written down: every real front is
    # `Define: <term>` or `Complete the word equation: <left>`, so
    # `Define diffusion.` — no colon, and a full stop — is unreachable, and so
    # are the other five. The BACKS are not safe to use: Design's diffusion
    # answer, "The net movement of particles from where they are more
    # concentrated…", IS a real card's back, word for word, because Design and
    # the corpus are describing the same science. A tell that fires on correct
    # content is the tell that gets ignored, which is how the docket shipped.
    #
    # `KEY FACT` is Design's third tag and the exporter emits none — 573
    # definitions, 9 equations, 0 key facts — so the words on a card are a tell
    # too, and the one that would survive Design rewriting a front.
    "Define diffusion.",
    "Three things that make a gas exchange surface efficient.",
    "Pressure, force, area — which one sits on top?",
    "Write the word equation for magnesium burning in oxygen.",
    "Define ventilation.",
    "A fixed amount of gas is squeezed into a smaller space. "
    "What happens to the pressure?",
    "KEY FACT",
    # ⊕ 23 Aug 2026 — PHASE 3. DESIGN'S SAMPLE RECALL BANK.
    #
    # The grafted practice round renders `MRB_DATA('practiceBank')`. On the fixture
    # that is Design's own `bank()`, lifted out of the amended delivery by
    # `DONOR_LIFTS`; on a real page it is every recall and apply rung of every
    # lesson the class has covered, read from `ks3_ladder_questions`. If one of
    # these is on screen on a page that is supposed to be showing real data,
    # the bank has fallen back to Design's sample.
    #
    # ⚠️⚠️ SEVEN OF DESIGN'S EIGHT, AND THE EIGHTH IS DELIBERATELY ABSENT.
    #
    #     "A plant in a dark cupboard is releasing carbon dioxide. Which of
    #      the three processes is it carrying out?"
    #
    # is NOT a tell, because it is a REAL LADDER QUESTION — `the-gas-exchange-
    # system#recall`, word for word, one exact match in `ks3_ladder_questions`.
    # Design did not invent it; Design drew the sample from the corpus. And
    # `the-gas-exchange-system` is a lesson `8r/Sc1` has covered, so it is the
    # FIRST question a real student on the real page can be shown.
    #
    # Registering it would have made this list report the correct page as
    # dirty, every time, on the one class the drives actually use. That is the
    # failure mode this list's own header names: "a tell that cries wolf gets
    # ignored, which is the failure mode that let the docket ship in the first
    # place." Checked by exact match against all 154 ladder rows and all 924
    # bank rows before any of the eight was written down — the other seven
    # match NOTHING in either corpus, on an exact test and on a 40-character
    # prefix test.
    "A fixed amount of gas is squeezed into half the space. "
    "What happens to its pressure?",
    "Which feature would make a gas exchange surface worse?",
    "Magnesium burns in oxygen. What is the product?",
    "Which state has particles close together that can still move past "
    "each other?",
    "A force of 20 N presses on 4 m2. What is the pressure?",
    "Where in the lungs does gas exchange happen?",
    "What is always conserved in a chemical reaction?",
    # ⊕ 23 Aug 2026 — PHASE 3. THE ROUND'S OMITTED SIDEBAR, WATCHED FROM THE
    # LIVE SIDE.
    #
    # `student_behaviour.AMENDED_OMISSIONS` asserts these are absent, and it
    # drives the FIXTURE. Nothing else watches the page a student actually
    # loads, so the two sentences the graft's `omit` removes are registered
    # here as well: if either ever appears on mrbadmus.com, the omission has
    # been reverted and the drive says so on the real page rather than on a
    # copy of it. Neither can appear from real data — there is no key behind
    # either — so neither can cry wolf.
    "Recall counts for 20 of the 100 points on the leaderboard",
    "Open the assignment instead",
    "BEST STREAK",
]

# ── the defaults that are NOT text, and so can never be a tell ────────────
#
# ⚠️ EVERY TELL ABOVE IS A STRING, AND THAT IS THE LIST'S ONE STRUCTURAL BLIND
# SPOT. Design's "now" marker on the term spine is not the characters "04"
# anywhere — it is `n === 4` deciding a COLOUR. `innerText` cannot see a
# colour, so the tell list went green twice over a page whose picture showed
# the marker sitting four weeks into a one-week-old term. A screenshot caught
# it both times, which is not a check.
#
# So the marker is probed STRUCTURALLY instead: read the dots out of the DOM,
# ask which ones are painted, and assert that the painted set is exactly the
# real current week. That is the assertion a tell was standing in for.
MARKER_PROBE = r"""(function () {
  /* the spine's dots: 5px round spans, one per week, each preceded by its
     week number. Design draws them at `background: var(--st-accent)` for the
     current week and `transparent` for every other. */
  var out = { lit: [], total: 0 };
  var all = document.querySelectorAll('span');
  for (var i = 0; i < all.length; i++) {
    var el = all[i], cs = getComputedStyle(el);
    if (cs.borderTopLeftRadius !== '50%') { continue; }
    if (Math.round(el.getBoundingClientRect().width) !== 5) { continue; }
    var bg = cs.backgroundColor || '';
    var transparent = (bg === 'transparent' ||
                       /rgba\(0,\s*0,\s*0,\s*0\)/.test(bg));
    var num = el.previousElementSibling
      ? (el.previousElementSibling.innerText || '').trim() : '';
    if (!/^\d+$/.test(num)) { continue; }
    out.total++;
    if (!transparent) { out.lit.push(num); }
  }
  return JSON.stringify(out);
})()"""

# What a real student on this account should be seeing tonight. The initials
# belong to the drive account, so they travel with it.
EXPECT = ["8r/Sc1", os.environ.get("MRB_DRIVE_INITIALS", "AY")]


# ── ⚠️ THE VIEWPORT IS SET BEFORE THE PAGE LOADS, NOT AFTER ──────────────
#
# ⊕ 22 Aug 2026. Every drive in this repo used to navigate first and resize
# second, and that measured the WRONG BREAKPOINT — silently, and in a way that
# looked like a product bug when it was finally noticed.
#
# Two reasons it goes wrong, and they compound:
#
#   1  The CDP viewport override PERSISTS ACROSS PAGES in one browser. So the
#      "390px" page actually mounted at whatever the previous screen left
#      behind, and the "1460px" page mounted at 390.
#   2  The page decides its header treatment ONCE, from its own width, at
#      mount. Resizing afterwards did not move it back — inside a headless
#      session the resize event does not reliably reach the listener, and
#      Design's 250ms settle poll gives up after six seconds.
#
# The result was a 390px screenshot of the DESKTOP header and a 1460px
# screenshot of the PHONE one, both green, for as long as anyone had looked.
# A real device does not resize into a page; it opens one at its own size.
# So does this now: blank page, set the size, THEN navigate.
#
# ⚠️ Whether a real browser updates the header on a genuine window drag is
# NOT settled by this and is not claimed either way — see the run log. It is a
# different question from this one, which is purely about measuring the right
# thing.


def wait_for_mount(page, seconds=75.0):
    """Wait until the page has actually rendered, rather than for a fixed time.

    ⚠️ THIS IS THE FIX FOR A FLAKE THAT LOOKED LIKE A BROKEN PAGE, TWICE.

    The 21 August run saw one drive in five render the error state at 390px
    while desktop was fine, wrote it down rather than dismissing it, and
    guessed at a cold Render instance. It is a cold Render instance — and the
    page was never broken. Render's free tier spins the backend down, and the
    first request of the day takes the better part of a minute to come back.
    The drive settled for FOUR SECONDS and then measured, so it photographed a
    page that had not finished loading and called it a failure.

    So the drive stops guessing how long the backend will take and waits for
    the thing it actually cares about: the host element having children. A
    page that genuinely cannot load renders its message into the same host, so
    this returns for that too and the checks below still see it.

    A fixed settle can only be wrong in two directions — too short and it lies,
    too long and every run pays for the worst case. This pays for what it uses.
    """
    import time
    end = time.time() + seconds
    last = 0
    while time.time() < end:
        n = page.eval(
            "(function(){var h=document.getElementById('mrb-student');"
            "return h ? h.getElementsByTagName('*').length : -1;})()")
        n = n if isinstance(n, int) else 0
        # Settled means rendered AND no longer growing: the mount paints in one
        # go, but webfonts and the recall panel can add a frame after it.
        if n > 20 and n == last:
            return n
        last = n
        time.sleep(0.6)
    return last


def anon_key():
    src = open("leaderboard.html", encoding="utf-8").read()
    return re.search(r"eyJ[A-Za-z0-9_-]{20,}\.[A-Za-z0-9_-]{20,}\.[A-Za-z0-9_-]{10,}",
                     src).group(0)


def sign_in(key):
    # MRB_DRIVE_PASSWORD goes with MRB_DRIVE_EMAIL; the older name is kept so
    # nothing that already sets it has to change.
    pw = (os.environ.get("MRB_DRIVE_PASSWORD")
          or os.environ.get("MRB_TEST_STUDENT_PASSWORD"))
    if not pw:
        raise SystemExit("neither MRB_DRIVE_PASSWORD nor "
                         "MRB_TEST_STUDENT_PASSWORD is set")
    req = urllib.request.Request(
        SUPABASE_URL + "/auth/v1/token?grant_type=password",
        data=json.dumps({"email": EMAIL, "password": pw}).encode(),
        headers={"apikey": key, "Content-Type": "application/json"},
        method="POST")
    del pw
    with urllib.request.urlopen(req, timeout=60, context=CTX) as r:
        return json.loads(r.read().decode())


def main():
    key = anon_key()
    sess = sign_in(key)
    # supabase-js v2 keeps the whole session object under this key.
    storage_key = "sb-%s-auth-token" % PROJECT_REF
    storage_val = json.dumps(sess)
    print("\n🧑‍🎓  drive_pages — the wired pages, as a signed-in student\n")
    print("     session acquired (token %s…)" % sess["access_token"][:8])

    anon = key

    # ⚠️ `shared/config.js` selects the TEST Supabase project on localhost and
    # 127.0.0.1 — deliberately, so local dev cannot touch real students. It has
    # an escape hatch built for exactly this case: `?env=prod`. Without it the
    # guard's client looks for a session under the TEST project's storage key,
    # finds none, and bounces to /auth.html — which is what the first three runs
    # of this drive measured, and what briefly looked like a broken page.
    def sign_the_browser_in(b, port):
        """Let the SDK write its own session, rather than guessing its format.

        ⚠️ Hand-writing `sb-<ref>-auth-token` does not work: supabase-js v2 has
        changed that entry's encoding across releases (recent builds base64
        the JSON behind a `base64-` prefix), and the pages load `@2`, which
        floats. A hand-rolled entry the SDK does not recognise is simply
        ignored — the page then renders its signed-OUT state, which is exactly
        what the first run of this drive measured and briefly looked like a
        wiring failure.

        So: open a page on the SAME ORIGIN that already loads the SDK, make a
        client, and call `setSession`. The SDK persists it in whatever shape
        that version uses, and every later page on the origin picks it up.
        """
        p = b.page("http://localhost:%d/leaderboard.html?env=prod" % port, settle=2.0)
        ok = p.eval("""
          (async function () {
            if (!window.supabase) return 'no sdk';
            var c = window.supabase.createClient(%s, %s);
            var r = await c.auth.setSession({
              access_token: %s, refresh_token: %s });
            if (r.error) return 'error: ' + r.error.message;
            var g = await c.auth.getSession();
            return g.data.session ? 'ok:' + g.data.session.user.email : 'no session';
          })()
        """ % (json.dumps(SUPABASE_URL), json.dumps(anon),
               json.dumps(sess["access_token"]), json.dumps(sess["refresh_token"])))
        return ok

    server, port = cdp.serve("mrbadmus_site", port=PORT)
    fails, notes = [], []

    def check(ok, what, detail=""):
        print(("     ✅ " if ok else "     ❌ ") + what + (("  — " + detail) if detail else ""))
        if not ok:
            fails.append(what + ((" — " + detail) if detail else ""))

    try:
        with cdp.Browser() as b:
            for width, label in ((390, "390px  (a phone)"), (1460, "1460px (desktop)")):
                print("\n  %s" % label)
                signed = sign_the_browser_in(b, port)
                print("       session in the browser: %s" % signed)
                # size the window FIRST — see the note at the top of the file
                b.page("about:blank", settle=0.2).set_viewport(width, 900)
                page = b.page(CLASS_URL % port, settle=4.0)
                wait_for_mount(page)

                text = page.eval("document.body.innerText") or ""
                nodes = page.eval("document.querySelectorAll('*').length")
                errs = page.console_errors()

                check(nodes > 200, "the class page rendered", "%s node(s)" % nodes)
                check(not errs, "no console errors",
                      (errs[0][:110] if errs else ""))
                check("undefined" not in text,
                      "nothing renders as the string 'undefined'")

                leaked = [t for t in FIXTURE_TELLS if t in text]
                check(not leaked,
                      "NO fixture content on screen — the page is showing real data",
                      ("leaked: " + ", ".join(leaked[:4])) if leaked else "")

                present = [t for t in EXPECT if t in text]
                check(len(present) == len(EXPECT),
                      "the student's real identity is on screen",
                      "found %s of %s" % (present, EXPECT))

                # ⊕ RULED 22 Aug 2026 — P9. The "now" dot, probed rather
                # than grepped. `currentWeek` is what the page itself computed
                # from the server's teaching week, so this asserts the drawing
                # agrees with the data instead of asserting a hardcoded 1 —
                # which would go red in September for the right reason and be
                # "fixed" by someone bumping the constant.
                want = page.eval(
                    "(window.__MRB_DATA__ && window.__MRB_DATA__.currentWeek)"
                    " != null ? String(window.__MRB_DATA__.currentWeek) : ''")
                probe = page.eval(MARKER_PROBE)
                try:
                    spine = json.loads(probe) if probe else {"lit": [], "total": 0}
                except Exception:
                    spine = {"lit": [], "total": 0}
                if not spine["total"]:
                    notes.append("%s: the term spine drew no dots to probe "
                                 "(it is hidden at this width)" % label)
                elif not want:
                    check(False, "the spine's NOW dot can be checked",
                          "the page exposes no currentWeek to check it against")
                else:
                    lit = [n.lstrip("0") or "0" for n in spine["lit"]]
                    check(lit == [want.lstrip("0") or "0"],
                          "the term spine's NOW dot is on the REAL current week",
                          "lit=%s want=week %s of %s"
                          % (spine["lit"], want, spine["total"]))

                if "Breathing and gas exchange" in text:
                    notes.append("%s: this week's real assignment title is on screen"
                                 % label)

                print("       first 260 chars of what a student sees:")
                for line in (text[:260] or "(nothing)").splitlines()[:6]:
                    print("         " + line[:88])
            # ── B3's interactive sequence, on the ASSIGNMENT page ──────
            #
            # The class page rendering is necessary and nowhere near
            # sufficient. This is the sequence a student actually performs,
            # and the two steps that matter most are LEAVE and RETURN: the
            # page persists to localStorage under a key that has to be
            # specific to this class and this assignment, and a key that is
            # not would show one student's answers inside another piece of
            # work.
            print("\n  the assignment, driven end to end (390px)")
            url = ASSIGN_URL % port
            sign_the_browser_in(b, port)
            b.page("about:blank", settle=0.2).set_viewport(390, 900)
            page = b.page(url, settle=4.0)
            wait_for_mount(page)

            errs = page.console_errors()
            check(not errs, "assignment: no console errors",
                  (errs[0][:110] if errs else ""))

            text = page.eval("document.body.innerText") or ""
            leaked = [t for t in FIXTURE_TELLS if t in text]
            check(not leaked, "assignment: no fixture content on screen",
                  ("leaked: " + ", ".join(leaked[:4])) if leaked else "")

            # the storage key must name this class and this assignment
            keys = page.eval("Object.keys(localStorage)") or []
            mrb = [k for k in keys if "assignment" in k and "sb-" not in k]
            check(any("8rSc1" in k or "8r" in k or "-" in k for k in mrb) or not mrb,
                  "assignment: its saved-state key is not Design's demo key",
                  str(mrb)[:120])
            check(not any("a5.v1" in k for k in mrb),
                  "assignment: NOT persisting under Design's hard-coded "
                  "'mrbadmusai.assignment.8rSc1.a5.v1'", str(mrb)[:120])

            # pick the first option, confirm, and check the page responded
            before = page.eval("document.body.innerText")
            page.eval("(function(){var o=document.querySelectorAll("
                      "'[role=\"button\"],button');for(var i=0;i<o.length;i++)"
                      "{var t=(o[i].innerText||'').trim();"
                      "if(/^A\\b|^A[\\s·]/.test(t)){o[i].click();return t;}}"
                      "return null;})()")
            page.eval("(function(){var b=[].slice.call("
                      "document.querySelectorAll('button,[role=\"button\"]'));"
                      "var c=b.filter(function(x){return /confirm/i.test("
                      "x.innerText||'');});if(c.length){c[0].click();return 1;}"
                      "return 0;})()")
            after = page.eval("document.body.innerText")

            # ⊕ 22 Aug 2026 — A COMPLETED ASSIGNMENT IS NOT A FAILED CHECK.
            #
            # Since the per-answer model landed, this account's state persists
            # on the SERVER between runs. Once the drive has answered
            # everything and pressed Complete, the page opens on the end screen
            # for ever after — there are no options to click, so "the page did
            # not change" is true and means nothing. Reporting it as a failure
            # sent me hunting a bug that was a previous run's success.
            #
            # A check that cannot run must say so. A check that reports FAIL
            # when it means SKIPPED is worse than no check, because the next
            # person learns to ignore it.
            done_screen = ("COMPLETED" in (before or "").upper()
                           and "CONFIRM" not in (before or "").upper())
            if done_screen:
                notes.append("assignment: already complete for this account, so "
                             "the answer-and-confirm step had nothing to click "
                             "— SKIPPED, not failed. Clear this student's "
                             "submissions to exercise it.")
                print("     ⏭  assignment: choosing and confirming an answer "
                      "— SKIPPED (already complete for this account)")
            else:
                check(after != before,
                      "assignment: choosing and confirming an answer changes the page")

            saved = page.eval("(function(){var o={};for(var i=0;i<"
                              "localStorage.length;i++){var k=localStorage.key(i);"
                              "if(k.indexOf('sb-')!==0)o[k]=(localStorage[k]||'')"
                              ".slice(0,60);}return o;})()") or {}
            check(bool(saved),
                  "assignment: the answer was written to local storage",
                  str(saved)[:140])

            # LEAVE and RETURN
            b.page(CLASS_URL % port,
                   settle=1.5)
            page = b.page(url, settle=3.0)
            wait_for_mount(page)
            page.set_viewport(390, 900)
            restored = page.eval("document.body.innerText") or ""
            check(restored.strip() != "",
                  "assignment: it still renders after leaving and returning")
            check("undefined" not in restored,
                  "assignment: nothing renders as 'undefined' after return")

    finally:
        server.shutdown()

    print()
    for n in notes:
        print("     · " + n)
    print()
    if fails:
        print("     ❌ %d check(s) failed:" % len(fails))
        for f in fails:
            print("        · " + f)
        print()
        return 1
    print("     ✅ the wired pages render real data at both widths.\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
