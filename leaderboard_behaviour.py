"""leaderboard_behaviour.py — every control on the leaderboard does something.

MRB-290, the slow gate. Drives the fixtures in `leaderboard_fixtures/`
headless, on load AND again after a reload, and asserts:

  · the page mounts and every binding resolves (`data-mrb-misses` is 0)
  · every control is PRESSED — the tier toggle, the four subject filters,
    the week rail's prev/next/This week, every week chip, every row's
    expand and collapse
  · no press leaves the page blank
  · no computed value reaches the copy — `null%`, `NaN`, `undefined`,
    `-Infinity`, `[object Object]`
  · the console stays quiet

and then the same over the thin states Design never drew.

⚠️ IT DRIVES THE FIXTURES, NOT THE LIVE PAGE, and the difference is the
scope of what this gate can claim. The live page reads
`GET /api/weekly-leaderboard/board` off a Render dyno and, for the viewer's
own row, a Supabase session. Driving it needs a credential and a warm
backend, which is the same reason `student_controls_drive` and
`teacher_behaviour` are fixture-driven. So this gate proves everything
between the data arriving and the pixels, and NOTHING about whether the seam
asks for the right rows. That sentence is here rather than in a report
because a gate whose scope is overstated is worse than no gate.

⚑ THE PRESS LOOP RE-QUERIES EVERY ITERATION, and that is not a style choice.
`teacher_behaviour` collected its clickables once and was found to be
pressing 2 controls of 27 while its summary line said "every control moved
something": the runtime's `draw()` empties the host and rebuilds it, so every
handle collected before a press is detached by that press. The ratio pressed
is PRINTED rather than rounded up to "every control", for the same reason.

── The fixtures, and what each is for ───────────────────────────────────

  leaderboard-fixture.html            Design's own sample, Higher/Overall,
                                      the live week — a full board, a podium,
                                      a cut line, movement and streaks
  leaderboard-empty-fixture.html      a week nobody sat. ⚠️ NOT A CORNER:
                                      this was the LIVE state of
                                      Higher/Overall on 25 Aug 2026
  leaderboard-weekone-fixture.html    the first week of a year — every
                                      `move` null (NEW), every streak 1
  leaderboard-thin-fixture.html       ONE entrant. The state that found
                                      RULINGS R16, where the podium hides and
                                      Design's list still starts at index 3
                                      so the board draws nothing at all
  leaderboard-outside-fixture.html    a viewer below the cut — present in
                                      `me`, absent from `board`, so the
                                      sticky pinned row is the only place
                                      they appear
  leaderboard-signedout-fixture.html  no session — no `me`, no pinned row,
                                      no YOU badge, board still renders
  leaderboard-error-fixture.html      the fetch failed. Every control stays
                                      live, because the press IS the retry
"""

import os
import re
import sys
import time

REPO = os.path.dirname(os.path.abspath(__file__))
PAGE_DIR = "leaderboard_fixtures"

FIXTURES = [
    ("leaderboard-fixture.html",
     "Design's own sample, Higher/Overall, the live week"),
    ("leaderboard-empty-fixture.html",
     "a week nobody sat — the live landing state on 25 Aug 2026"),
    ("leaderboard-weekone-fixture.html",
     "week one — every move NEW, no streak possible"),
    ("leaderboard-thin-fixture.html",
     "one entrant — the state that found R16"),
    ("leaderboard-outside-fixture.html",
     "a viewer below the cut — pinned row only"),
    ("leaderboard-signedout-fixture.html",
     "no session — no pinned row, no YOU badge"),
    ("leaderboard-avatars-fixture.html",
     "rows with a real avatar_url — R25, faces inside Design's disc"),
    ("leaderboard-podium-fixture.html",
     "the viewer is RANK 2, on the podium — R32"),
    ("leaderboard-loading-fixture.html",
     "no payload yet — R30, the live cold-start window"),
    ("leaderboard-error-fixture.html",
     "the fetch failed — every control still live"),
]

# ⊕ MRB-290 R25. Per fixture: (discs that must carry a face, discs that must
# carry letters). `None` means "not asserted here". The avatars fixture is
# built with a mix on purpose — some rows have a face, some have none, and
# one carries a hostile URL the seam must reject back to a monogram.
# ⊕ R32 — EXACTLY how many YOU chips each fixture must render, not merely
# "at most one". "At most" passes when the marker is MISSING, which is the
# defect Mide reported: he was rank 2 and nothing said so. A fixture whose
# viewer is on screen must show exactly one; a fixture with no viewer on
# screen must show none.
YOU_EXPECT = {
    "leaderboard-podium-fixture.html":
        (1, "the viewer is rank 2 — the podium chip R32 adds"),
    "leaderboard-outside-fixture.html":
        (1, "the viewer is below the cut — the pinned row is the only place"),
    "leaderboard-signedout-fixture.html":
        (0, "there is no viewer at all"),
    "leaderboard-loading-fixture.html":
        (0, "no payload has arrived, so no row is anyone's"),
    "leaderboard-empty-fixture.html":
        (0, "nobody sat this week"),
    "leaderboard-error-fixture.html":
        (0, "the fetch failed; there are no rows to mark"),
    "leaderboard-thin-fixture.html":
        (0, "one entrant, and it is not the viewer"),
}

AVATAR_EXPECT = {
    "leaderboard-avatars-fixture.html": dict(faces_min=3, letters_min=1),
    # Design's own sample carries no avatar at all, so every disc must be a
    # monogram. This is the negative case: a stray `url(` here would mean the
    # binding is inventing an image.
    "leaderboard-fixture.html": dict(faces_min=0, faces_max=0, letters_min=4),
}

# ⚠️ SUBSTRING, CASE-SENSITIVE, AND DELIBERATELY NARROW. Each of these is a
# computed value reaching the screen, which means the branch that produced it
# has no guard. `null%` is the one this port was most likely to ship: the
# endpoint returns `median_pct: null` on an empty week and Design writes
# `median + '%'` with no null branch (RULINGS R15).
RENDER_TELLS = ["null%", "NaN", "undefined", "-Infinity", "Infinity",
                "[object Object]", "nullm", "null/", "/null", "NEW ENTRYNEW"]

# ⊕ MRB-290 R30 — WORD-BOUNDED, and the substring list above could not have
# caught what these do. The live page read "TOP 10 ONLY · null SAT THIS WEEK"
# while loading: a bare `null` with a space either side, which matches none of
# `null%`, `nullm`, `null/` or `/null`. Word boundaries catch the value
# standing on its own as a word — which is exactly how an unguarded
# interpolation of a null renders inside a sentence.
WORD_TELLS = ["null", "undefined", "NaN", "Infinity"]

# What a state must SAY. A thin state that renders nothing at all still
# passes a blank check if the page was already short, so each of these
# fixtures names a string that must be on the page for the state to have
# rendered as a state rather than as an absence.
MUST_SAY = {
    "leaderboard-empty-fixture.html": ["NO ENTRIES"],
    "leaderboard-thin-fixture.html": ["ALL 1 LISTED"],
    "leaderboard-outside-fixture.html": ["YOU"],
    "leaderboard-error-fixture.html": ["COULD NOT LOAD"],
    # R30: the footer keeps its label and loses only the clause it has no
    # fact for; the cut value names the state.
    "leaderboard-loading-fixture.html": ["LOADING", "TOP 10 ONLY"],
    "leaderboard-weekone-fixture.html": ["NEW"],
}

# ⚠️ EACH ENTRY CARRIES ITS OWN REASON, and it does so because the first
# version did not. One shared message — written for the YOU badge — was
# printed for every token, so a correct failure on "LOCKED" was explained as
# "badging a row as the viewer's when there is no viewer". A gate that fails
# for the right reason and says the wrong one sends the next reader to the
# wrong file.
MUST_NOT_SAY = {
    "leaderboard-signedout-fixture.html": [
        ("YOU", "there is no signed-in viewer here, and badging a row as "
                "the viewer's when there is no viewer is how a student is "
                "shown somebody else's standing as their own"),
    ],
    "leaderboard-loading-fixture.html": [
        ("LOCKED", "the payload has not arrived, so the week is not locked "
                   "— it is unknown. Rendering unknown as one of the two "
                   "real answers is MRB-287's 'ON TIME 0' again (R30)"),
        ("SAT THIS WEEK", "the footer's clause survived with no number to "
                          "put in it. R30 drops the clause entirely rather "
                          "than dashing it"),
    ],
}


HOST = "#mrb-leaderboard"

_DRIVE_JS = r"""
(async function () {
  var host = document.querySelector("__HOST__");
  if (!host) { return {fatal: 'no mount point'}; }

  function frame() {
    return new Promise(function (r) {
      requestAnimationFrame(function () { requestAnimationFrame(r); });
    });
  }
  /* ⚠️ `railScroll` IS IN THE SNAPSHOT BECAUSE SCROLLING COUNTS AS DEAD
     WITHOUT IT. The rail's prev/next buttons call `el.scrollBy()`, which
     changes no text, no node count and no render count — so a liveness
     check built on those three reports two working controls as dead, every
     run, on every fixture. That is the same false-confidence shape as a
     check that reports dead ones as working. */
  function railScroll() {
    var r = document.getElementById('ks4-week-rail');
    return r ? r.scrollLeft : -1;
  }
  function snap() {
    return {
      text: host.innerText || '',
      renders: host.getAttribute('data-mrb-renders'),
      misses: host.getAttribute('data-mrb-misses'),
      nodes: host.querySelectorAll('*').length,
      rail: railScroll()
    };
  }
  /* The six monogram discs, measured. R25: a disc carries a face or letters
     and never both. */
  function avatars() {
    var out = {faces: 0, letters: 0, both: 0};
    var discs = host.querySelectorAll('[style*="border-radius: 50%"]');
    for (var q = 0; q < discs.length; q++) {
      var st = discs[q].getAttribute('style') || '';
      if (st.indexOf('background-image') < 0) { continue; }
      var hasFace = /background-image:\s*url\(/.test(st);
      var hasText = (discs[q].textContent || '').trim().length > 0;
      if (hasFace) { out.faces++; }
      if (hasText) { out.letters++; }
      if (hasFace && hasText) { out.both++; }
    }
    return out;
  }
  function disabledLooking(el) {
    return el.disabled === true || el.getAttribute('aria-disabled') === 'true';
  }
  /* ⚑ RE-QUERIED EVERY ITERATION. `draw()` does `host.textContent = ''` and
     rebuilds, so a handle collected before a press is detached by it. The
     teacher gate collected once and pressed 2 of 27 while reporting that it
     had pressed everything. */
  function clickable() {
    var all = host.querySelectorAll('[data-dc-tpl]'), out = [];
    for (var i = 0; i < all.length; i++) {
      var el = all[i], tag = el.tagName.toLowerCase();
      var press = tag === 'button' || tag === 'a' ||
                  el.getAttribute('role') === 'button' ||
                  (el.style && el.style.cursor === 'pointer');
      if (press && !disabledLooking(el)) { out.push(el); }
    }
    return out;
  }

  /* ⚑ THE STATE-DEPENDENT ASSERTIONS ARE MEASURED HERE, BEFORE ANY PRESS,
     AND THIS IS THE WHOLE POINT OF THE FIRST VERSION BEING WRONG.
     Each fixture exists to hold ONE state — one entrant, week one, faces in
     the discs. The drive then presses every control, which changes tier,
     subject and week, so by the time the loop ends the page is showing a
     DIFFERENT view and the fixture's state is gone. Asserting `ALL 1 LISTED`
     against that final text reported four fixtures as broken while every one
     of them was rendering correctly — a gate confidently measuring the wrong
     moment, which is exactly the failure MRB-287 §7 records inside the gate
     written to catch dead controls. Initial state here; liveness across the
     whole drive below. */
  var first = snap();
  var firstAvatars = avatars();

  /* ⊕ AT MOST ONE "YOU" CHIP, EVER — and this check exists because a fixture
     shipped with two and no gate noticed. The outside-top-10 fixture renamed
     its `me` row but left VIEWER as Design's AmberYew12, so board row 09 wore
     a YOU badge via `deco`'s `isYou` AND the pinned row wore another. The
     real seam cannot produce that: `me` arrives on a payload keyed by the
     authenticated user and the viewer name comes from that same user's
     profile, so they are one person by construction. Two chips means a
     student is being shown someone else's standing as their own.
     ⚠️ WORD-BOUNDED. A bare "YOU" substring also matches Design's own
     "YOUR STANDING" heading, which is on every render. */
  function youChips(t) { return ((t || '').match(/\bYOU\b/g) || []).length; }

  /* A rail with nothing to scroll makes its two scroll buttons genuinely
     inert. Measured rather than assumed, and reported rather than excused:
     on a fixture with one week there is no scrolling to do. */
  var rail = document.getElementById('ks4-week-rail');
  var railScrollable = !!(rail && rail.scrollWidth > rail.clientWidth + 2);

  var seen = {}, dead = [], blanked = [], errors = [];
  /* ⚠️ NO RATIO IS REPORTED, AND THAT IS DELIBERATE. The clickable set is
     not fixed: expanding a row adds three breakdown cards, changing the week
     changes how many rows there are. So "pressed" can legitimately exceed
     the count taken at load, and the first version printed "183 of 163
     controls pressed" — a denominator that is not a denominator. What is
     true and useful is the number of DISTINCT controls pressed and how many
     were still clickable at the end; both are printed, neither is divided. */
  var pressed = 0, found = 0;
  var CAP = 400;

  for (var j = 0; j < CAP; j++) {
    var list = clickable();
    if (list.length > found) { found = list.length; }
    if (j >= list.length) { break; }
    var c = list[j];
    var label = (c.innerText || c.getAttribute('aria-label') || c.tagName)
                .slice(0, 40).replace(/\s+/g, ' ').trim();
    var idx = c.getAttribute('data-dc-tpl');
    var key = idx + '|' + label;
    if (seen[key]) { continue; }
    seen[key] = 1;

    var before = snap();
    try { c.click(); pressed++; }
    catch (e) { errors.push(idx + ' ' + label + ': ' + e.message); continue; }
    await frame();
    var after = snap();
    /* ⚠️ SMOOTH SCROLL IS ASYNCHRONOUS AND TWO FRAMES IS NOT ENOUGH TO SEE
       IT. The rail's prev/next call `scrollBy({behavior:'smooth'})`, which
       animates over roughly 300ms; measured after two rAF the scrollLeft has
       moved by nothing or by a pixel or two, so a correct control reads as
       dead. Rather than loosen the liveness rule, give a control that looks
       dead a second, longer look — bounded, and only when the fast path
       already said no. */
    if (!(after.text !== before.text || after.renders !== before.renders ||
          after.nodes !== before.nodes || after.rail !== before.rail)) {
      await new Promise(function (r) { setTimeout(r, 420); });
      after = snap();
    }
    var moved = after.text !== before.text ||
                after.renders !== before.renders ||
                after.nodes !== before.nodes ||
                after.rail !== before.rail;
    /* ⚠️ EXEMPT ONLY WHEN THE RAIL MEASURABLY CANNOT SCROLL. The two rail
       buttons carry an SVG and no text, so `label` falls back to the tag
       name — they are identified here by having no text at all. On a fixture
       with one week (or none) `scrollWidth === clientWidth` and there is
       genuinely nothing for them to move; on any other fixture they are held
       to the same rule as everything else. Conditioned on a measurement, not
       on a name. */
    var inertScrollBtn = !railScrollable &&
                         (c.innerText || '').trim() === '';
    if (!moved && !inertScrollBtn) {
      dead.push({i: idx, label: label, tag: c.tagName.toLowerCase(),
                 inertRail: !railScrollable});
    }
    /* A press that empties the page passes the liveness check above,
       because a blank page is a very large change. */
    if ((after.text || '').trim().length < 40 &&
        (before.text || '').trim().length >= 40) {
      blanked.push({i: idx, label: label,
                    left: (after.text || '').trim().length});
    }
  }

  /* ⊕ R33 — THE RAIL FOLLOWS THE SELECTION.
     Press the OLDEST chip (the far end from where the mount snap leaves the
     rail, so a rail that does not follow leaves it off screen), then assert
     the chip that is now selected is inside the rail's visible scroll range.
     Then press it AGAIN — a redraw where the selection has NOT changed — and
     assert it is still in view, which is R28's preserve path proving it does
     not yank a student away from what they just chose. */
  var railFollow = null;
  var rr = document.getElementById('ks4-week-rail');
  if (rr && rr.children.length > 2 && rr.scrollWidth > rr.clientWidth + 2) {
    function inView(i) {
      var el = document.getElementById('ks4-week-rail');
      var c = el && el.children[i];
      if (!c) { return null; }
      return c.offsetLeft >= el.scrollLeft - 3 &&
             (c.offsetLeft + c.offsetWidth) <= el.scrollLeft + el.clientWidth + 3;
    }
    rr.children[0].click();
    await frame();
    await new Promise(function (r) { setTimeout(r, 500); });
    var afterSelect = inView(0);
    var el2 = document.getElementById('ks4-week-rail');
    if (el2 && el2.children[0]) { el2.children[0].click(); }
    await frame();
    await new Promise(function (r) { setTimeout(r, 500); });
    var afterRedraw = inView(0);
    railFollow = {tested: true, afterSelect: afterSelect,
                  afterRedraw: afterRedraw};
  } else {
    railFollow = {tested: false};
  }

  var s = snap();
  return {railFollow: railFollow, found: found, pressed: pressed, dead: dead, blanked: blanked,
          errors: errors, misses: s.misses, renders: s.renders,
          text: s.text, len: (s.text || '').trim().length,
          youFirst: youChips(first.text), youLast: youChips(s.text),
          firstText: first.text, firstLen: (first.text || '').trim().length,
          faces: firstAvatars.faces, letters: firstAvatars.letters,
          both: firstAvatars.both, railScrollable: railScrollable};
})()
""".replace("__HOST__", HOST)
# ⚠️ A TOKEN REPLACE, NOT %-FORMATTING. This JavaScript contains literal
# percent signs — `border-radius: 50%` is how a monogram disc is found — and
# `%` formatting reads every one of them as a specifier. Doubling them to
# escape would put `50%%` inside a selector that has to match real markup,
# which fails silently by matching nothing.


def drive(pg, port, path, what, label):
    """One fixture, one pass. Returns a list of problem strings."""
    problems = []
    url = "http://127.0.0.1:%d/%s/%s" % (port, PAGE_DIR, path)
    if what == "load":
        pg.goto(url, settle=1.2)
    else:
        pg.eval("location.reload()")
        time.sleep(1.6)

    got = pg.eval(_DRIVE_JS)
    if not isinstance(got, dict) or got.get("fatal"):
        return ["%s/%s: %s — the page did not mount at all."
                % (path, what, (got or {}).get("fatal", "no result"))], 0, 0

    tag = "%s/%s" % (path, what)

    if got.get("misses") not in ("0", 0, None):
        problems.append(
            "%s: %s unresolved binding(s). A `{{ }}` that resolves to "
            "nothing renders as an empty string, so this is invisible on a "
            "screenshot and load-bearing on a leaderboard."
            % (tag, got.get("misses")))

    if got.get("firstLen", 0) < 200:
        problems.append(
            "%s: the page settled at %d character(s) of text. %s should "
            "render as a STATE, not as an absence."
            % (tag, got.get("firstLen", 0), label))

    # ⚠️ THE INITIAL RENDER, NOT THE FINAL ONE. Each fixture holds one
    # state; the drive presses every control and navigates away from it.
    text = got.get("firstText") or ""
    after_text = got.get("text") or ""
    for tell in WORD_TELLS:
        for when, hay in (("on load", text), ("after the drive", after_text)):
            if re.search(r"\b%s\b" % tell, hay):
                problems.append(
                    "%s: the word %r stands alone in the copy %s. That is a "
                    "value with no guard reaching a student inside a "
                    "sentence — the shape that put 'TOP 10 ONLY \u00b7 null "
                    "SAT THIS WEEK' on the live page (R30)."
                    % (tag, tell, when))

    for tell in RENDER_TELLS:
        if tell in text or tell in after_text:
            problems.append(
                "%s: rendered %r. That is a computed value reaching the "
                "copy, not a written one — the branch that produces it has "
                "no guard." % (tag, tell))

    for want in MUST_SAY.get(path, []):
        if want not in text:
            problems.append(
                "%s: does not say %r. %s — and a state that renders nothing "
                "to say which state it is in is a blank with extra steps."
                % (tag, want, label))
    for never, why in MUST_NOT_SAY.get(path, []):
        # ⚠️ WORD-BOUNDED. A plain substring "YOU" matches Design's own
        # "YOUR STANDING" heading, which is on every render including the
        # signed-out one — the first version failed this fixture for a
        # heading rather than for a badge.
        if re.search(r"\b%s\b" % re.escape(never), text):
            problems.append("%s: says %r — %s." % (tag, never, why))

    # ⊕ AT MOST ONE "YOU" CHIP, on every fixture, before and after the drive.
    #
    # ⚑ ADDED BECAUSE A FIXTURE SHIPPED WITH TWO AND EVERY GATE WAS GREEN.
    # The outside-top-10 fixture renamed its `me` row to TestViewer99 and left
    # VIEWER as Design's AmberYew12, so board row 09 wore a YOU badge through
    # `deco`'s `isYou` and the pinned row wore a second one. Found by LOOKING
    # at the screenshot. The real seam cannot reach that state — `me` arrives
    # on a payload keyed by the authenticated user and the viewer name comes
    # from that same user's profile — which is exactly why a fixture could
    # drift there unchallenged: nothing downstream of the seam was asserting
    # the invariant the seam happens to guarantee.
    want_you = YOU_EXPECT.get(path)
    for when, n in (("on load", got.get("youFirst", 0)),
                    ("after the drive", got.get("youLast", 0))):
        if n > 1:
            problems.append(
                "%s: %d 'YOU' chips render %s, and a page has exactly one "
                "viewer. Two means one of them is on somebody else's row — "
                "a student shown another student's standing as their own. "
                "The pinned row, the podium chip and the in-board row are "
                "the same person by construction; if a fixture disagrees, "
                "the fixture is wrong." % (tag, n, when))
        # ⊕ R32. Only the INITIAL render is pinned to an exact count: the
        # drive changes tier, subject and week, and on another week the
        # viewer legitimately is somewhere else or nowhere.
        elif want_you is not None and when == "on load" \
                and n != want_you[0]:
            problems.append(
                "%s: %d 'YOU' chip(s) render on load and exactly %d was "
                "expected — %s. A missing marker passes any 'at most one' "
                "check, and a missing marker is the defect Mide reported: "
                "rank 2, and nothing on the board said so."
                % (tag, n, want_you[0], want_you[1]))

    # ⊕ MRB-290 R33 — the rail follows the selection.
    rf = got.get("railFollow") or {}
    if rf.get("tested"):
        if not rf.get("afterSelect"):
            problems.append(
                "%s: after pressing the oldest week chip, that chip is "
                "OUTSIDE the rail's visible scroll range. Mide's report "
                "exactly: the board loads the week he chose and the rail "
                "leaves him hunting for it (R33)." % tag)
        if not rf.get("afterRedraw"):
            problems.append(
                "%s: the selected week chip left the visible range on a "
                "redraw where the selection did NOT change. That is R28's "
                "preserve path yanking a student away from what they just "
                "chose — the opposite failure to R33's, and just as "
                "disorienting." % tag)

    # ⊕ MRB-290 R25 — identity is frozen, and the avatar is half of it.
    if got.get("both"):
        problems.append(
            "%s: %d disc(s) render BOTH a face and initials. R25 empties "
            "`initials` only when there is an image to put in its place, so "
            "letters over a student's photograph means the two halves of "
            "that ruling have come apart." % (tag, got["both"]))

    want = AVATAR_EXPECT.get(path)
    if want:
        faces, letters = got.get("faces", 0), got.get("letters", 0)
        if "faces_min" in want and faces < want["faces_min"]:
            problems.append(
                "%s: %d disc(s) render an avatar image and at least %d were "
                "expected. The live leaderboard shows faces today; a port "
                "that quietly stopped would take every student's avatar "
                "away and no other check would notice."
                % (tag, faces, want["faces_min"]))
        if "faces_max" in want and faces > want["faces_max"]:
            problems.append(
                "%s: %d disc(s) render an avatar image and at most %d were "
                "expected. This fixture carries no `avatar_url` at all, so "
                "an image here is one the binding invented."
                % (tag, faces, want["faces_max"]))
        if "letters_min" in want and letters < want["letters_min"]:
            problems.append(
                "%s: only %d disc(s) fall back to Design's initials "
                "monogram and at least %d were expected. A row with no "
                "avatar must still have a face-shaped thing in it, not an "
                "empty circle." % (tag, letters, want["letters_min"]))

    for d in got.get("dead", []):
        problems.append(
            "%s: control %s (%s %r) moved nothing.%s Design's density, "
            "topCount, showPodium and showWeekTops are editor props and are "
            "pinned as constants (R22), so nothing on this page is allowed "
            "to be a decorative switch."
            % (tag, d["i"], d["tag"], d["label"],
               " The week rail is not scrollable on this fixture, so its two"
               " scroll buttons have nothing to move." if d.get("inertRail")
               else ""))

    for d in got.get("blanked", []):
        problems.append(
            "%s: control %s (%r) BLANKED the page — %d character(s) of text "
            "left. A press that empties the leaderboard is not a working "
            "control, and it passes the liveness check above because a blank "
            "page is a very large change." % (tag, d["i"], d["label"],
                                              d["left"]))

    for e in got.get("errors", []):
        problems.append("%s: control threw — %s" % (tag, e))

    for line in pg.console_errors():
        if "favicon" in line:
            continue
        problems.append("%s: console error — %s" % (tag, line[:200]))

    return problems, got.get("pressed", 0), got.get("found", 0)


def main(argv=None):
    os.chdir(REPO)
    import ks3_browser as cdp

    print("\n\U0001F3C6  leaderboard_behaviour — every control, every "
          "state, twice\n")

    missing = [f for f, _ in FIXTURES
               if not os.path.exists(os.path.join(PAGE_DIR, f))]
    if missing:
        raise SystemExit(
            "leaderboard_behaviour.py: %d fixture(s) missing from %s/: %s\n"
            "  Run `python3 build_leaderboard_port.py`. Driving a subset and "
            "reporting a pass is the overstated-scope defect gate_registry "
            "exists to stop."
            % (len(missing), PAGE_DIR, ", ".join(missing)))

    server, port = cdp.serve(REPO)
    failed = 0
    total_pressed = total_found = 0
    try:
        with cdp.Browser() as b:
            pg = b.attach()
            pg.set_viewport(1460, 1200)
            for path, label in FIXTURES:
                problems = []
                pressed = found = 0
                for what in ("load", "reload"):
                    p, pr, fd = drive(pg, port, path, what, label)
                    problems += p
                    pressed = max(pressed, pr)
                    found = max(found, fd)
                total_pressed += pressed
                total_found += found
                if problems:
                    failed += 1
                    print("     %-38s ❌ %d problem(s)"
                          % (path, len(problems)))
                    for q in problems:
                        print("          · %s" % q)
                else:
                    print("     %-38s ✅  %d distinct control(s) pressed "
                          "(%d clickable at the widest render)  — %s"
                          % (path, pressed, found, label))
    finally:
        try:
            server.shutdown()
        except Exception:
            pass

    if failed:
        print("\n  FAIL  %d of %d fixture(s).\n" % (failed, len(FIXTURES)))
        return 1
    print("\n  PASS  %d fixture(s), %d distinct control(s) pressed across "
          "them.\n        Every fixture mounted, every binding resolved, "
          "nothing pressed left\n        the page blank, no computed value "
          "reached the copy, and the console\n        stayed quiet — on load "
          "and again after a reload.\n" % (len(FIXTURES), total_pressed))
    print("     ⚠️  Fixture-driven. This proves everything between the data\n"
          "         arriving and the pixels, and nothing about whether the "
          "seam\n         asks the backend for the right rows.\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
