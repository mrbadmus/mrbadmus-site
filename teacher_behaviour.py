#!/usr/bin/env python3
"""teacher_behaviour.py — the ported teacher pages, driven.

    python3 teacher_behaviour.py                # all twelve fixtures
    python3 teacher_behaviour.py classes        # one page (substring match)
    python3 teacher_behaviour.py --shots DIR    # also write screenshots

⊕ MRB-287, 24 Aug 2026.

── WHY THIS EXISTS ──────────────────────────────────────────────────────

`teacher_tells.py` reads the built pages' BYTES. It can prove that Design's
invented school is not in the file; it cannot prove that anything renders,
that a button does something, or that an empty class produces an empty state
rather than a stack trace. Every check it makes would pass on a page that is
blank.

This is the gate that opens the pages. It is the teacher-side twin of
`ks3_instrument_liveness` — "the only gate that PRESSES THE BUTTONS" — and it
exists for the reason that file gives: every other gate measures the page at
rest, so a dead control passes all of them and does nothing when a teacher
touches it.

── WHAT IT DRIVES, AND WHY NOT THE LIVE PAGES ───────────────────────────

The twelve fixtures: six screens x {populated, empty}.

⚠️ IT DOES NOT DRIVE THE LIVE PAGES, and that is a real limit rather than an
oversight. A live teacher page begins with `requireTeacherRole`, so reaching
one needs a teacher account and a password. This run had neither
(`MRB_DRIVE_PASSWORD` unset), and a gate that signs in to production is a gate
that fails when Render is asleep — which is why `student_page_drive.py` and
`student_controls_drive.py` are both EXCLUDED from the registry for exactly
this reason.

What the fixtures CAN prove is everything between the data arriving and the
pixels: that every screen mounts, that every binding resolves, that every
control does something, and that the empty shapes render as states rather
than as errors. What they cannot prove is that the SEAM returns the right
rows. That is `teacher_tells` (nothing invented reaches the page) plus review,
and it is stated here rather than implied.

── THE EMPTY HALF ───────────────────────────────────────────────────────

Half the fixtures are empty on purpose, because empty states are the half of
the product that ships broken. A populated fixture exercises the path where
every array has something in it; it is the other path that throws on
`rows[0]`, divides by `length`, and renders `null%`.

The five shapes, from the port's own emission:

    no classes in the year being viewed · a class with no roster · a class
    with students but no work set · a paper with nobody's submission · a grid
    whose paper was not prefetched

⊕ MRB-287 E1 — the first two are also PAST-YEAR, and that is a second
property on one fixture rather than a thirteenth and fourteenth. They are what
drive MRB-261's read-only rule: a finished year offers no write controls and
says which year it is. Between them they cover both halves — the classes
screen (the import action absent, the year selector reachable on an empty
grid) and the class page (the shoutout write surface absent, the feed still
readable).

⚠️ ⊕ CORRECTED 2 Sep 2026 (MRB-306 Phase 2a screen 2). The last clause read
"the shoutout composer and the bulk opener absent". That was true of v2 and
had SILENTLY STOPPED BEING TRUE: Design's v3 deleted the composer's own two
nodes, so the `WRAP` rows naming them went with it, and the bulk opener that
survived (nodes 215 and 276) was never wrapped. Driving the past-year fixture
showed a live "Shoutouts" button in its header while this paragraph asserted
it was absent — a docstring describing a guarantee no code was making any
more. Both nodes are wrapped on `canWrite` now and the sentence is true
again; see `WRAP["class-detail.html"]` for the ruling.

⚠️ AND NOTE WHAT THAT COST: nothing here FAILED. This gate does not assert
the read-only guarantee, it describes it, and no other gate on the page
noticed either. The absence was found by opening the page and reading it.

── THE RELOAD ───────────────────────────────────────────────────────────

Every page is driven, RELOADED, and driven again. This is not padding: a
reload is where the runtime's field-value preservation, the `?v=` stamps and
any state written at mount get a second chance to disagree with each other,
and MRB-287's own brief records that three of the worst defects of the month
surfaced on the second pass rather than the first.
"""

import json
import os
import re
import sys

import teacher_rulings as R

REPO = os.path.dirname(os.path.abspath(__file__))
# The fixtures are NOT in `teacher/`. That directory is published to
# mrbadmus.com and round-tripped back over itself by generate_site_v5, and
# these pages render Design's invented school — see the note in
# build_teacher_port.py, which records the two wrong ways of fixing that
# before this one.
PAGE_DIR = "teacher_fixtures"

# ⛔ NO `import`: it is not ported, so there is no `import-fixture.html` to
# drive. `teacher/import.html` is the hand-written wizard again — see
# IMPORT_NOT_PORTED in teacher_rulings.py. It is not covered by any gate here,
# which is exactly where it was before the port and is stated rather than
# implied.
SCREENS = ["classes", "class-detail", "student-detail", "assignment",
           "digest", "insights"]

# Every fixture, and what it is supposed to be showing. The empty ones name
# their shape so a failure says which state broke rather than just "empty".
EMPTY_SHAPE = {
    # ⊕ MRB-287 E1 — BOTH OF THE FIRST TWO GAINED A SECOND PROPERTY, and the
    # note says so rather than going stale. They are the only fixtures in the
    # set where the academic year in view is a FINISHED one, which is what
    # drives MRB-261's read-only rule: the year selector reachable on an empty
    # grid, and the write controls absent on a class page. See EMPTY_SHAPES in
    # build_teacher_port.py for the reasoning, and `_shape_past_year` for what
    # it actually changes.
    # ⊕ 2 Sep 2026 (MRB-306 Phase 2a screen 2) — KEYED BY (screen, slug),
    # because a screen may now name more than one empty state. `empty` is the
    # slug the original twelve carry, so every existing line reads the same.
    ("classes", "empty"): "no classes in the year being viewed, and that year is past",
    ("class-detail", "empty"): "a class with no roster, in a past (read-only) year",
    # ⊕ THE THIRTEENTH. A LIVE class, roster present, work set, nobody in yet
    # — the state a class is in from the moment work is set until the first
    # child answers. See EMPTY_SHAPES["class-detail.html"] for why it is
    # justified as a RECURRING shape rather than as any class's shape today.
    ("class-detail", "nosubs"): "a live class with work set and nobody in yet",
    ("class-detail", "gridmissing"):
        "no grid fetched at all — which is every class-detail render in "
        "production",
    ("student-detail", "empty"): "a student with no submissions",
    # ⊕ 2 Sep 2026 (MRB-306 Phase 2a screen 7) — THE THREE THE CHARTS
    # SCREEN HAD NO ANSWER FOR. `insights-empty` withholds a GRID, which
    # reaches ONE of the six chart kinds; the other five were rendering
    # Design's eight populated classes in both of this page's fixtures, so
    # "empty scopes honest" was untested for `submissions`, `spread`,
    # `ontime`, `means` and `engagement` in either scope. Between them these
    # three are the three shapes the working year is actually in.
    ("insights", "nolive"):
        "rosters imported and no work set anywhere — `live` is empty, and "
        "so is the class scope",
    ("insights", "noroster"):
        "the scoped class has no roster at all — 66 of the working year's "
        "69 classes",
    ("insights", "single"):
        "one class, one marked paper set in an EARLIER teaching week, two "
        "children — every superlative is over a set of one, and `week[0]` "
        "and `colSub[0]` disagree by construction",

    ("assignment", "empty"): "a paper nobody has submitted",
    # ⊕ 2 Sep 2026 (MRB-306 Phase 2a screen 5) — THE TWO THE SET HAD NO
    # ANSWER FOR. `written` is the only paper in the estate that is not eight
    # questions out of eight marks, which is what makes the `/max` ruling
    # visible at all; the two `gridmissing` shapes are key-ABSENT, which is a
    # different branch of `gridFor` from `insights-empty`'s key-present-null
    # and is the branch that threw live on 26 Aug 2026.
    ("assignment", "written"):
        "5 questions out of 7 marks, Q4 written, and the lowest-scoring "
        "question carrying no stem text",
    ("assignment", "gridmissing"):
        "one open assignment and no grid fetched — the key is absent",
    # ⊕ CORRECTED 2 Sep 2026 (MRB-306 Phase 2a screen 6). This read "no live
    # classes to digest", which is not what the shaper makes and not what the
    # fixture shows: `_shape_no_work` blanks ONE class and SEVEN stay live.
    # The sentence mattered — it is the reason the zero-live-classes guards
    # (the em dash on Mean score and On time, and the `NaN%` guard) were
    # believed covered when nothing exercised them. `nolive` below is the
    # fixture that actually reaches them.
    ("digest", "empty"): "one class with students and no work set — seven "
                         "still live",
    ("digest", "nolive"): "no live class at all: rosters imported, nothing "
                          "set yet — the first week of a school year",
    ("insights", "empty"): "nothing marked to chart",
}


# ── controls whose effect is real and is NOT in the DOM ──────────────────
#
# Two of Design's controls do something a DOM diff cannot see. They are
# exempt from the dead-control check and from NOTHING else — each is asserted
# to still be PRESENT on the page, so an exemption can never quietly become a
# deletion.
#
# ⚠️ EXEMPTED BY WHAT THEY DO, NOT BY WHERE THEY ARE. A node-number allowlist
# would excuse the same index on a future page where it meant something else.
EXEMPT_OFFDOM = {
    "signOut": "leaves the session. `MrBadmusTeacherGuard.signOut()` clears "
               "the Supabase session and redirects; on a fixture there is no "
               "session to clear, so it returns having changed no markup. It "
               "does NOT throw — the guard is loaded — which is why it lands "
               "in the dead list rather than the error list.",
    "doPrint": "opens the browser's print dialog via `window.print()`. There "
               "is no DOM consequence by design, and headless Chrome has no "
               "dialog to open.",
}

# The label each exempt handler renders, so the assertion can find it.
EXEMPT_LABELS = {"signOut": "Sign out", "doPrint": "Print"}


def fixtures():
    """(screen, filename, is_empty, slug) for every fixture the port writes.

    ⊕ 2 Sep 2026 (MRB-306 Phase 2a screen 2) — DERIVED FROM THE BUILD, NOT
    LISTED HERE. This used to hardcode "exactly two per screen", which meant a
    thirteenth fixture could be generated by `build_teacher_port.py` and never
    driven by anything, with both scripts green. The build's own
    `EMPTY_SHAPES` and `variant_files` are the authority now, so a variant
    cannot be added without this gate picking it up.

    ⚠️ EVERY VARIANT COUNTS AS `is_empty`. That flag gates the `needs_data`
    additions — the four shoutout-delete controls that hang off a feed row —
    and every empty shaper in the set leaves `FEED[cid]` empty, so there is
    correctly nothing to delete on any of them.
    """
    import build_teacher_port as BTP
    by_out = {sp["out"]: sp for sp in BTP.PAGES}
    out = []
    for s in SCREENS:
        spec = by_out["%s.html" % s]
        out.append((s, "%s-fixture.html" % s, False, None))
        for slug, _note, _shaper in BTP.EMPTY_SHAPES[spec["out"]]:
            out.append((s, BTP.variant_files(spec, slug)[0], True, slug))
    unnoted = [(s, g) for s, _f, e, g in out if e and (s, g) not in EMPTY_SHAPE]
    if unnoted:
        raise SystemExit(
            "teacher_behaviour.py: %s has no line in EMPTY_SHAPE.\n"
            "  Every empty fixture says which state it is showing, so a "
            "failure names the state rather than just \"empty\"."
            % ", ".join("%s/%s" % k for k in unnoted))
    return out


# ── the probe ────────────────────────────────────────────────────────────
#
# One evaluation per page rather than a round trip per control: the DOM is
# rebuilt wholesale on every `setState`, so a Python-side loop holding element
# handles would be holding handles to elements that no longer exist. The press
# and the before/after comparison have to happen inside one script.
#
# "Something changed" is measured as the host's own serialised text plus its
# render counter. A control that renders the same text twice has still done
# something if the counter moved (a no-op re-render is legal — Design has
# toggles that land on the state they were already in), but a control that
# moves NEITHER is dead.
_DRIVE_JS = r"""
(async function () {
  var EXEMPT = __EXEMPT__;
  var ADDED = __ADDED__;
  /* {marker: template index}. An addition whose opener is one of DESIGN'S
     nodes rather than an earlier addition — see the reveal loop. */
  var OPENERS = __OPENERS__;
  var host = document.querySelector('#mrb-teacher');
  if (!host) { return JSON.stringify({error: 'no #mrb-teacher host'}); }

  /* ⚠️ THE REDRAW IS ON A FRAME, NOT ON THE CLICK. `setState` calls the
     runtime's `schedule`, which defers the rebuild to `requestAnimationFrame`.
     The first version of this probe snapshotted synchronously after `.click()`
     and therefore read the DOM as it was BEFORE the control acted — so it
     reported all 29 controls on the classes screen as dead, including the
     filter tabs and the nav. Two frames, because the callback queue is
     drained on the frame after the one that draws. */
  function frame() {
    return new Promise(function (r) {
      requestAnimationFrame(function () { requestAnimationFrame(r); });
    });
  }

  /* Navigation is recorded, not followed. Six of Design's handlers now set
     `window.location.href` through `MRB_GO`, and letting one fire would tear
     down the page mid-sweep and take the remaining controls with it. Stubbing
     the helper keeps the press REAL — the handler still runs, still computes
     its destination, and still proves it is wired — while the browser stays
     put. A press that reaches MRB_GO is alive by definition. */
  var navs = [];
  var realGo = window.MRB_GO, realBack = window.MRB_BACK;
  var realHome = window.MRB_HOME;
  window.MRB_GO = function (screen, params) {
    navs.push({screen: screen, params: params || null});
  };
  window.MRB_BACK = function () { navs.push({screen: '<back>', params: null}); };
  /* ⊕ MRB-304 — the brand mark leaves the teacher portal for /index.html.
     Stubbed for exactly the reason MRB_GO is: unstubbed, the very first
     press of the top bar would navigate this fixture to the public homepage
     and take every remaining control on the page with it. The press still
     runs the real handler, so it still proves the control is wired. */
  window.MRB_HOME = function () { navs.push({screen: '<home>', params: null}); };

  function snap() {
    return {
      text: host.innerText || '',
      renders: host.getAttribute('data-mrb-renders'),
      misses: host.getAttribute('data-mrb-misses'),
      nodes: host.querySelectorAll('*').length
    };
  }

  var first = snap();

  /* ⚑ RE-QUERIED EVERY ITERATION, AND THIS IS THE WHOLE POINT.
     The runtime's `draw()` does `host.textContent = ""` and rebuilds, so
     EVERY element handle taken before a press is detached the moment that
     press causes a re-render. The first version of this loop collected all
     the controls once and then skipped any that `host.contains()` no longer
     held — which, after the very first state change, was all of them.

     Measured on the classes screen: 27 controls found, **2 pressed**. The
     gate reported PASS on twelve fixtures while pressing almost nothing, and
     its own summary line said "every control moved something". That is the
     overstated-scope defect `gate_registry.py` exists to stop, sitting inside
     the gate meant to catch dead controls.

     So the list is rebuilt from the live DOM on every pass and the press is
     addressed by ORDINAL. The page may legitimately grow or shrink under the
     sweep (an overlay opens, a filter empties a grid), so the bound is a
     generous cap rather than a fixed count, and what was actually pressed is
     REPORTED rather than assumed. */
  /* A control that PRESENTS AS DISABLED is not a dead control, and telling
     the two apart is the whole job of this gate.

     The week rail's forward arrow is the case that taught it. At the newest
     week Design sets `cursor: default` and drops the colour to
     `--st-rule-strong`, and the handler is guarded by `if (!fwdOff)`. Pressing
     it changes nothing — correctly. It was reported as dead only because the
     first version treated every `<button>` as pressable regardless of how it
     was painted.

     The ticket's rule is "nothing that LOOKS pressable but is not". A dimmed
     button with a default cursor does not look pressable, so it is excluded
     from the sweep by that appearance rather than by an allowlist of node
     numbers — an allowlist would drift, and would also excuse the arrow at
     the middle of the rail where it should work. */
  function disabledLooking(el) {
    if (el.disabled) { return true; }
    if (el.getAttribute('aria-disabled') === 'true') { return true; }
    var cur = (el.style && el.style.cursor) || '';
    if (cur === 'default' || cur === 'not-allowed') { return true; }
    return false;
  }

  /* ⊕ MRB-287, 24 Aug 2026 — `[data-mrb-added]` AS WELL, AND THIS WAS A HOLE.
     Every element the runtime draws from one of Design's nodes carries
     `data-dc-tpl`, written from that node's `i`. Markup this port INSERTS
     carries no `i` on purpose — `teacher_rulings.INSERT_AT` says so, because
     Design's numbering is what every other ruling is anchored on and it must
     not move — so an inserted element has no `data-dc-tpl` and this sweep
     could not see it. Nothing was going unpressed while both insertions were
     empty states with no control in them. The shoutout delete is four
     controls, and a delete button no gate can press is precisely the dead
     control this file exists to catch. */
  function clickable() {
    var all = host.querySelectorAll('[data-dc-tpl],[data-mrb-added]'),
        out = [];
    for (var i = 0; i < all.length; i++) {
      var el = all[i], tag = el.tagName.toLowerCase();
      var press = tag === 'button' || tag === 'a' || tag === 'select' ||
                  tag === 'input' || tag === 'textarea' ||
                  el.getAttribute('role') === 'button' ||
                  (el.style && el.style.cursor === 'pointer');
      if (press && !disabledLooking(el)) { out.push(el); }
    }
    return out;
  }

  var dead = [], blanked = [], pressed = 0, errors = [], seen = {};
  var present = [];
  var found = clickable().length;
  var CAP = 400;

  for (var j = 0; j < CAP; j++) {
    var list = clickable();
    if (j >= list.length) { break; }
    var c = list[j];

    var label = (c.innerText || c.getAttribute('aria-label') ||
                 c.getAttribute('placeholder') || c.tagName)
                .slice(0, 40).replace(/\s+/g, ' ').trim();
    var idx = c.getAttribute('data-dc-tpl') ||
              c.getAttribute('data-mrb-added');
    var key = idx + '|' + label;
    if (seen[key]) { continue; }   // already pressed this exact control
    seen[key] = 1;

    /* NOT PRESSED, AND PRESENCE RECORDED INSTEAD.
       Two controls must not be swept. `Sign out` ends the session — on a live
       page that would tear the sweep down halfway and on a fixture it throws,
       because the guard arrives with `teacher-live.js` and a fixture loads
       only the runtime. `Print` opens a browser dialog. Neither has a DOM
       consequence to measure, and pressing them is actively wrong rather than
       merely uninformative.
       Their EXISTENCE is what this gate can honestly check, so that is what
       it checks. */
    if (EXEMPT.indexOf(label) !== -1) { present.push(label); continue; }

    var before = snap();
    var navsBefore = navs.length;
    try {
      var tg = c.tagName.toLowerCase();
      if (tg === 'input' || tg === 'textarea') {
        c.focus();
        c.value = 'zz';
        c.dispatchEvent(new Event('input', {bubbles: true}));
      } else if (tg === 'select') {
        c.focus();
        if (c.options && c.options.length > 1) { c.selectedIndex = 1; }
        c.dispatchEvent(new Event('change', {bubbles: true}));
      } else {
        c.click();
      }
      pressed++;
    } catch (e) {
      errors.push(idx + ' ' + label + ': ' + e.message);
      continue;
    }
    await frame();
    var after = snap();
    var moved = after.text !== before.text ||
                after.renders !== before.renders ||
                after.nodes !== before.nodes ||
                navs.length > navsBefore;
    if (!moved) {
      dead.push({i: idx, label: label, tag: c.tagName.toLowerCase()});
    }

    /* ⚑ AND DID IT LEAVE A PAGE BEHIND? "Changed" is not the same as
       "worked". Node 78 — the "Import" link on an empty class card — ran
       Design's `setState({screen: 'import'})`; on `classes.html` the screen
       is pinned and Design's import screen is pruned, so every screen `<if>`
       went false and the page rendered NOTHING. A blank page is a very large
       change in text, nodes and renders, so the liveness test above passes
       it, and the press that emptied the dashboard is recorded as healthy. */
    if ((after.text || '').trim().length < 40 &&
        (before.text || '').trim().length >= 40) {
      blanked.push({i: idx, label: label,
                    tag: c.tagName.toLowerCase(),
                    left: (after.text || '').trim().length});
    }
  }

  /* ══ ⊕ MRB-287 · THE ADDITIONS, PRESSED ON PURPOSE ══════════════════

     The sweep above walks controls BY ORDINAL, and that is right for
     Design's own dashboard: it presses whatever is on screen, in order,
     without a list of what should be there. What it cannot promise is that
     any PARTICULAR control was reached — a control that lives inside a sheet
     another control opens is reachable only while that sheet is open, and the
     ordinal walk closes sheets as readily as it opens them. Measured on
     class-detail: the sweep pressed the shoutout "Remove" button and the
     confirm sheet's close X, and then never came back for "Remove shoutout" —
     the press that actually writes.

     For Design's controls that is a coverage limit and has always been one.
     For markup THIS PORT ADDED it is not acceptable: an addition is the one
     thing on the page nobody drew, nobody reviewed against a delivery, and
     nobody can find by comparing two files. So every entry in
     `teacher_rulings.AMENDED_ADDITIONS` ruled onto this page is pressed HERE,
     by name, and must move something.

     ⚠️ IT RE-OPENS RATHER THAN GIVING UP. An addition that is not on screen
     is not absent — it may be behind an earlier one. Each earlier addition is
     pressed in turn until the wanted control appears; if none of them reveals
     it, THAT is the failure, and it is reported as unreachable rather than as
     dead. `build_teacher_port` has already proved the markup is in the file,
     so "in the file and unreachable" is a real and separate defect. */
  var added = [], addedDead = [], addedGone = [], addedNav = {};
  for (var t = 0; t < ADDED.length; t++) {
    var want = ADDED[t];
    var sel = '[data-mrb-added="' + want + '"]';
    var el = host.querySelector(sel);

    /* ⊕ MRB-287 E1 — AN OPENER THAT IS ONE OF DESIGN'S OWN NODES.
       The loop below reveals an addition by pressing EARLIER ADDITIONS, which
       works for the shoutout sheet — every step of it is markup this port
       added. It cannot work for the year list: that sits behind Design's node
       86, the "Previous years" toggle she drew and this port only rewired. So
       an addition may name an opener by TEMPLATE INDEX, and it is pressed
       first. Without it the year options are reported unreachable — correctly,
       from this gate's point of view, which is exactly why the gate had to be
       taught rather than the marker moved. */
    if (!el && OPENERS[want] != null) {
      var byTpl = host.querySelector('[data-dc-tpl="' + OPENERS[want] + '"]');
      if (byTpl) {
        byTpl.click();
        await frame();
        el = host.querySelector(sel);
      }
    }

    for (var u = 0; u < t && !el; u++) {
      var opener = host.querySelector('[data-mrb-added="' + ADDED[u] + '"]');
      if (!opener) { continue; }
      opener.click();
      await frame();
      el = host.querySelector(sel);
    }
    if (!el) { addedGone.push(want); continue; }
    var aLabel = (el.innerText || el.getAttribute('aria-label') || el.tagName)
                 .slice(0, 40).replace(/\s+/g, ' ').trim();
    var aBefore = snap(), aNavs = navs.length;
    try {
      el.click();
      added.push(want + '|' + aLabel);
    } catch (e) {
      errors.push(want + ' ' + aLabel + ': ' + e.message);
      continue;
    }
    await frame();
    var aAfter = snap();
    /* WHERE the press said it was going, not just that it moved. A control
       whose whole job is to navigate proves nothing by re-rendering. */
    if (navs.length > aNavs) { addedNav[want] = navs[navs.length - 1]; }
    if (aAfter.text === aBefore.text && aAfter.renders === aBefore.renders &&
        aAfter.nodes === aBefore.nodes && navs.length === aNavs) {
      addedDead.push({i: want, label: aLabel,
                      tag: el.tagName.toLowerCase()});
    }
  }

  window.MRB_GO = realGo;
  window.MRB_BACK = realBack;
  window.MRB_HOME = realHome;

  return JSON.stringify({
    error: '',
    first: first,
    last: snap(),
    controls: found,
    pressed: pressed,
    navs: navs.length,
    dead: dead,
    blanked: blanked,
    present: present,
    added: added,
    addedDead: addedDead,
    addedGone: addedGone,
    addedNav: addedNav,
    errors: errors
  });
})()
"""

# Strings that must never be on a rendered teacher page. These are RENDER-time
# failures the byte-level gate cannot see, because each one is produced by
# arithmetic rather than written in the source.
#
# ⚠️ `null%` AND `NaN` ARE THE POINT. The seam returns `null` for a percentage
# with nothing markable behind it — deliberately, so that "nothing to measure"
# cannot be confused with "zero". `null + '%'` renders the four characters
# `null%`, and a teacher reads that as a broken page; `0%` would be worse
# still, because they would read it as a fact.
RENDER_TELLS = ["null%", "NaN", "undefined", "-Infinity", "Infinity",
                "[object Object]", "null/", "/null", "null students"]


# ⊕ 2 Sep 2026 (MRB-306 Phase 2a screen 7) — THE CHART CROSS PRODUCT.
#
# ⚑ THE SWEEP ABOVE PRESSES EVERY CONTROL ONCE, IN DOM ORDER, AND ON THIS
# SCREEN THAT COVERS HALF THE PAGE. The insights region runs
# [Back] [All classes] [8r/Sc1] [Print] then the six chart chips — so the
# sweep presses BOTH scope tabs before it reaches the first chip, leaves the
# scope on the CLASS, and then draws all six charts scoped to that class. The
# six whole-school charts are never drawn at all.
#
# That is not a hypothetical. `chartFor`'s `questions / all` branch read
# `this.STEMS`, a class field `DROP_FIELDS` deletes, and threw
# `TypeError: Cannot read properties of undefined` — taking the entire Charts
# page down — on the delivery's own populated fixture. This gate drove that
# fixture, on load and after a reload, and passed it, printing "the console
# stayed quiet". The defect was found by pressing the chips by hand. It was
# then RE-INTRODUCED deliberately, on 2 Sep 2026, to check whether this file
# could see it: five insights fixtures, still all green. It could not.
#
# So the chart kinds are driven as a CROSS PRODUCT — every scope re-pressed
# before every kind, so each of the twelve cells is drawn from a known state
# and after a redraw — and each cell is then asked the question this screen
# exists to answer: a chart with nothing to plot must SAY SO. A card with no
# tiles and no series and no caption is a chart drawn as zero.
_CHART_JS = r"""
(async function(){
  var out = {cells: [], err: null};
  try {
    /* ⚠️ RE-QUERIED EVERY TIME, NEVER HELD. The runtime REPLACES the
       `[data-port-region]` element on a redraw, so a reference taken once
       goes detached on the first press: the buttons found through it are no
       longer in the document, clicking them changes nothing a reader can
       see, and reading the title back through it returns the card as it was
       before any of this started. The first version of this probe did hold
       it, reported twelve clean cells, and every one of the twelve was the
       SAME cell — the chart the page happened to open on. It passed a page
       carrying three deliberately re-introduced defects. */
    var reg = function(){ return document.querySelector('[data-port-region="insights"]'); };
    if(!reg()){ out.err = 'no [data-port-region="insights"] on the page'; return JSON.stringify(out); }
    var txt = function(e){ return e ? (e.textContent||'').replace(/\s+/g,' ').trim() : ''; };
    var frame = function(){ return new Promise(function(r){
      requestAnimationFrame(function(){ setTimeout(r, 40); }); }); };
    var buttons = function(){ var r = reg();
      return r ? Array.prototype.slice.call(r.querySelectorAll('button')) : []; };
    var labels = buttons().map(txt);
    var pi = labels.indexOf('Print');
    if(pi < 1){ out.err = 'the Print button is not in the insights region, so the scope tabs cannot be located'; return JSON.stringify(out); }
    var scopes = labels.slice(Math.max(0, pi - 2), pi);
    var kinds = labels.slice(pi + 1);
    if(!scopes.length || !kinds.length){ out.err = 'found ' + scopes.length + ' scope tab(s) and ' + kinds.length + ' chart chip(s)'; return JSON.stringify(out); }
    out.scopes = scopes; out.kinds = kinds;
    var press = async function(label){
      var b = buttons().filter(function(e){ return txt(e) === label; })[0];
      if(!b){ return false; }
      b.click(); await frame(); await frame(); return true;
    };
    for(var si = 0; si < scopes.length; si++){
      for(var ki = 0; ki < kinds.length; ki++){
        var cell = {scope: scopes[si], kind: kinds[ki]};
        if(!(await press(scopes[si]))){ cell.miss = 'scope tab vanished'; out.cells.push(cell); continue; }
        if(!(await press(kinds[ki]))){ cell.miss = 'chart chip vanished'; out.cells.push(cell); continue; }
        var r = reg();
        var h2 = r ? r.querySelector('h2') : null;
        var card = h2 ? h2.parentElement.parentElement : null;
        if(!card){ cell.miss = 'no chart card'; out.cells.push(cell); continue; }
        var kids = Array.prototype.slice.call(card.children);
        cell.title = txt(h2);
        cell.note = txt(kids[1]);
        cell.tiles = kids[2] ? kids[2].children.length : 0;
        cell.body = kids.slice(3).map(txt).join('').length;
        cell.text = txt(card);
        out.cells.push(cell);
      }
    }
  } catch(e){ out.err = String((e && e.stack) || e); }
  return JSON.stringify(out);
})()
"""


def _wired_handlers(path):
    """Every handler name an un-pruned node in this page's template calls."""
    body = open(path, encoding="utf-8").read()
    m = re.search(r"window\.__MRB_TPL__=(\{.*?\});", body, re.S)
    if not m:
        raise SystemExit("teacher_behaviour.py: %s has no __MRB_TPL__" % path)
    tree = json.loads(m.group(1))
    out = set()

    def walk(n):
        if isinstance(n, dict):
            if n.get("on"):
                out.add(n["on"])
            if n.get("onch"):
                out.add(n["onch"])
            for c in n.get("c") or []:
                walk(c)

    for r in tree.get("roots") or []:
        walk(r)
    return out


# ── ⊕ MRB-287 · the three nodes the search-truncation probe needs ────────
#
# ⚑ DERIVED FROM THE SHIPPED TEMPLATE, NOT TYPED. Design's search overlay is
# kept on four of the six pages and pruned on the other two, and the node
# numbers are hers — a table of them here would be a fifth place they are
# written down and the first one to go stale. The probe asks the page which
# element opens the search, which one takes the typing, and which one carries
# the caption, and skips the page entirely if any is absent.
def _search_nodes(path):
    body = open(path, encoding="utf-8").read()
    m = re.search(r"window\.__MRB_TPL__=(\{.*?\});", body, re.S)
    tree = json.loads(m.group(1))
    out = {"opener": None, "input": None, "foot": None, "row": None}

    def walk(n):
        if not isinstance(n, dict):
            return
        if n.get("on") == "openSearch":
            out["opener"] = n.get("i")
        if n.get("onch") == "setSearch":
            out["input"] = n.get("i")
        # The result ROW, so the probe can count what is actually on screen
        # rather than trust the cap. Design's `<for list="{{ searchResults }}">`
        # has exactly one child and that child is the row.
        if n.get("t") == "for" and n.get("e") == "searchResults":
            kids = [c for c in (n.get("c") or []) if isinstance(c, dict)]
            out["row"] = kids[0].get("i") if len(kids) == 1 else None
        for c in n.get("c") or []:
            if (isinstance(c, dict) and c.get("t") == "#"
                    and isinstance(c.get("v"), dict)):
                for part in c["v"].get("parts") or []:
                    if isinstance(part, dict) and part.get("e") == "searchFoot":
                        out["foot"] = n.get("i")
            walk(c)

    for r in tree.get("roots") or []:
        walk(r)
    return out


# ── ⊕ MRB-287 · the search cap, declared or not ──────────────────────────
#
# ⛔ THE DEFECT THIS EXISTS FOR: `.slice(0, 12)` on the search results, with
# nothing on screen saying so. Design sized it to a fifteen-name sample; the
# pool behind it is now every student the teacher teaches. A cap that is
# silent is indistinguishable from a complete answer, and no gate that
# measures a page at rest can see the difference — the page looks identical
# whether twelve matched or two hundred did.
#
# ⚠️ THE EXPECTATION IS DERIVED, NOT PATTERN-MATCHED ON THE WORDING. Asserting
# the caption's exact sentence would make this a copy test that goes red when
# the words are improved. What it asserts is a PROPERTY of the numbers in it:
#
#     truncating  (matched > rows)  → the caption's integers must include the
#                                     match total AND the row count. A caption
#                                     that never names the total is the silent
#                                     cap, whatever it says.
#     not         (matched == rows) → every integer in the caption must equal
#                                     that count. This is what forbids
#                                     "showing 12 of 12" and any other second
#                                     number invented where nothing was
#                                     withheld.
#     nothing matched               → the caption must still SAY something.
#                                     Design's line rendered "0 OF 60
#                                     STUDENTS": two numbers and no sentence.
_SEARCH_JS = r"""
(async function () {
  var N = __NODES__;
  function frame(){return new Promise(function(r){
    requestAnimationFrame(function(){requestAnimationFrame(r);});});}
  var host = document.querySelector('#mrb-teacher');
  var pool = (window.__MRB_DATA__ && window.__MRB_DATA__.searchPool) || [];
  var opener = host.querySelector('[data-dc-tpl="' + N.opener + '"]');
  if (!opener) { return JSON.stringify({skip: 'no search opener on screen'}); }
  opener.click();
  await frame();

  /* The three queries are taken from the POOL rather than written here, so
     they cannot stop matching when the fixture changes: everything, one whole
     name (exactly one row unless two children share it), and a string no name
     contains. */
  function hits(q) {
    var n = 0;
    for (var z = 0; z < pool.length; z++) {
      if (!q || String(pool[z].name || '').toLowerCase().indexOf(q) > -1) {
        n++; }
    }
    return n;
  }
  var whole = pool.length ? String(pool[0].name || '').toLowerCase() : 'zz';
  /* ⚑ THE FOURTH CASE IS THE ONE THAT FORBIDS "SHOWING 12 OF 12": SEVERAL
     matches, none withheld. Found by trying single letters rather than
     written down, so it cannot stop being that case when the fixture data
     changes. Reported as skipped if no letter lands in the range. */
  var several = '';
  var abc = 'abcdefghijklmnopqrstuvwxyz';
  for (var L = 0; L < abc.length && !several; L++) {
    var h = hits(abc[L]);
    if (h > 1 && h < 12) { several = abc[L]; }
  }
  var cases = [{q: '', why: 'no query — the whole pool'},
               {q: whole, why: 'one whole name'},
               {q: 'qzqzqz', why: 'a string nothing contains'}];
  if (several) {
    cases.splice(1, 0, {q: several,
                        why: 'several matches, none withheld'}); }
  var out = [];
  for (var i = 0; i < cases.length; i++) {
    var el = host.querySelector('[data-dc-tpl="' + N.input + '"]');
    if (!el) { return JSON.stringify({skip: 'search input not on screen'}); }
    el.focus();
    el.value = cases[i].q;
    el.dispatchEvent(new Event('input', {bubbles: true}));
    await frame();
    var foot = host.querySelector('[data-dc-tpl="' + N.foot + '"]');
    var rows = host.querySelectorAll('[data-dc-tpl="' + N.row + '"]').length;
    var q = cases[i].q;
    var matched = 0;
    for (var j = 0; j < pool.length; j++) {
      var nm = String(pool[j].name || '').toLowerCase();
      if (!q || nm.indexOf(q) > -1) { matched++; }
    }
    var text = foot ? (foot.innerText || '').trim() : null;
    out.push({q: q, why: cases[i].why, rows: rows, matched: matched,
              pool: pool.length, text: text,
              nums: text ? (text.match(/\d+/g) || []).map(Number) : []});
  }
  return JSON.stringify({skip: '', pool: pool.length, cases: out,
                         several: several || null});
})()
"""


def _search_problems(what, c):
    """One search state, judged on the NUMBERS in its caption."""
    out = []
    where = "%s: search %s (%s)" % (what, ("with %r" % c["q"]) if c["q"]
                                    else "with no query", c["why"])
    if c["text"] is None:
        return ["%s — the caption node is not on screen at all. Design draws "
                "it under every search; a search with no footer is a search "
                "that cannot tell you it was cut short." % where]
    if not c["text"]:
        # Blank is legal ONLY where the helper deliberately renders nothing,
        # which is a count it could not be sure of — and a fixture always has
        # its pool, so a blank here is a real miss.
        return ["%s — the caption is EMPTY. Blanks over invented numbers is "
                "the rule for an unknown count, and this count is known "
                "(%d matched of a pool of %d)."
                % (where, c["matched"], c["pool"])]
    nums = c["nums"]
    if c["matched"] == 0:
        return out            # a sentence, no numbers: that is the state
    # ⚠️ THE COUNT OF NUMBERS MATTERS, NOT JUST WHICH ONES. The first
    # version of this asked only whether the wrong numbers were present, and
    # a falsification run walked straight through it: with the truncation
    # clause emitted unconditionally the caption read "3 MATCHES · SHOWING 3",
    # whose integers are {3} — exactly the set a correct caption has. A
    # redundant clause is invisible to a set. So the whole multiset is
    # pinned: a caption may carry the numbers the state has and no others,
    # once each.
    if c["matched"] > c["rows"]:
        want = sorted([c["matched"], c["rows"]])
        if sorted(nums) != want:
            out.append(
                "%s — %d matched and %d are on screen, so the caption should "
                "carry exactly those two numbers. %r carries %s. A caption "
                "that never names the match total is the silent cap: a "
                "teacher reads twelve rows as the whole answer."
                % (where, c["matched"], c["rows"], c["text"], nums or "none"))
    else:
        if nums != [c["matched"]]:
            out.append(
                "%s — nothing was withheld (%d matched, %d shown), so the "
                "caption should carry that one number once. %r carries %s. A "
                "\"showing N of N\" clause where nothing is hidden is noise, "
                "and noise is how a teacher learns to stop reading the line "
                "that will later matter."
                % (where, c["matched"], c["rows"], c["text"], nums or "none"))
    return out


def drive(page, path, is_empty, cdp, port, shots=None, slug=None):
    """Problems, as strings, for one fixture. Driven twice — load and reload."""
    problems = []
    tally = {"found": 0, "pressed": 0, "added": 0, "search": 0,
             "nosev": 0, "charts": 0}
    # ⚠️ THE TEMPLATE, NOT THE SOURCE. Every page ships the WHOLE logic
    # class — all six screens' `renderVals` — and prunes only the MARKUP. So
    # `doPrint` is a string in all six files while the Print BUTTON exists on
    # two, and asking "is the handler named in this file" said Print should be
    # on the assignment screen, where its node was pruned. The exact question
    # is whether a node that survived pruning is WIRED to the handler, and the
    # shipped template tree is the only thing that answers it.
    src = _wired_handlers(os.path.join(PAGE_DIR, path))
    # ⊕ MRB-287 — the controls THIS PORT added to Design's delivery, on this
    # page, in the order they are registered. Read from the register rather
    # than listed here, so an addition cannot be made without this gate
    # pressing it. `page` is the screen name; the register's `pages` names the
    # emitted filenames — ⊕ MRB-304, always a tuple, because the "My classes"
    # link in the top bar is chrome and is on all six.
    # ⚠️ AND `needs_data` ADDITIONS ARE NOT EXPECTED ON THE EMPTY FIXTURE.
    # The four shoutout-delete controls hang off a feed row; the empty
    # class-detail shape is a class with no roster and `FEED[cid] == []`, so
    # there is nothing to remove and correctly nothing to press. Demanding
    # them there would be demanding a delete button on an empty feed. They
    # are still pressed, by name, on the populated fixture.
    added_here = [a["marker"] for a in R.AMENDED_ADDITIONS
                  if page + ".html" in a["pages"]
                  and not (is_empty and a.get("needs_data"))]
    added_why = {a["marker"]: a for a in R.AMENDED_ADDITIONS}
    # ⊕ MRB-287 E1 — additions revealed by one of DESIGN'S nodes rather than
    # by an earlier addition. See the probe's note beside OPENERS.
    openers = {a["marker"]: a["opener_tpl"] for a in R.AMENDED_ADDITIONS
               if a.get("opener_tpl") is not None}
    # ⊕ MRB-287 — the search overlay's three nodes, if this page keeps it.
    search_nodes = _search_nodes(os.path.join(PAGE_DIR, path))
    with cdp.Browser() as b:
        pg = b.attach()
        pg.set_viewport(1460, 1200)
        url = "http://127.0.0.1:%d/%s/%s" % (port, PAGE_DIR, path)

        for pass_n, what in ((1, "load"), (2, "reload")):
            if pass_n == 1:
                pg.goto(url, settle=1.2)
            else:
                pg.eval("location.reload()")
                import time
                time.sleep(1.6)

            # ⚠️ THE SHOT IS TAKEN AT REST, BEFORE THE SWEEP. The first
            # version photographed after driving, which meant every review
            # screenshot showed the page in whatever state the LAST control
            # left it — the classes screen came out with the student-search
            # overlay open across the middle of it. A human reviewing these is
            # asking "what does a teacher see when they arrive", and that is
            # the frame before any button is pressed.
            if shots and pass_n == 1:
                out = os.path.join(shots, "%s%s.png"
                                   % (page, ("-" + (slug or "empty"))
                                      if is_empty else ""))
                pg.screenshot(out, full_page=True)

            probe = (_DRIVE_JS
                     .replace("__EXEMPT__",
                              json.dumps(sorted(EXEMPT_LABELS.values())))
                     .replace("__ADDED__", json.dumps(added_here))
                     .replace("__OPENERS__", json.dumps(openers)))
            got = json.loads(pg.eval(probe))
            if got.get("error"):
                problems.append("%s: %s" % (what, got["error"]))
                continue

            if pass_n == 1:
                tally["found"] += got.get("controls", 0)
                tally["pressed"] += got.get("pressed", 0)
                tally["added"] += len(got.get("added") or [])

            first, last = got["first"], got["last"]

            # 1. It mounted.
            if not first["renders"] or int(first["renders"]) < 1:
                problems.append(
                    "%s: never rendered — the host carries no "
                    "data-mrb-renders. The page is blank." % what)
                continue

            # 2. Every binding resolved. A miss is a `{{ }}` the runtime could
            #    not look up, which renders as nothing at all — invisible in a
            #    screenshot, because what is missing does not draw.
            if first["misses"] and int(first["misses"]) > 0:
                problems.append(
                    "%s: %s unresolved binding(s) at mount. A miss renders as "
                    "nothing, so this is invisible on screen."
                    % (what, first["misses"]))

            # 3. Something is actually on the page. An empty fixture is
            #    allowed to be sparse; it is not allowed to be blank, because
            #    a blank page is indistinguishable from a crash.
            text = (first["text"] or "").strip()
            if len(text) < 40:
                problems.append(
                    "%s: rendered only %d character(s) of text. An empty "
                    "state is a STATE — it has to say something. This is a "
                    "blank page, which reads as a crash." % (what, len(text)))

            # 4. No arithmetic leaked into the copy.
            for tell in RENDER_TELLS:
                if tell in text:
                    problems.append(
                        "%s: rendered %r. That is a computed value reaching "
                        "the screen, not a written one — the branch that "
                        "produces it has no guard." % (what, tell))

            # 5. No dead controls — minus the two whose effect is not in
            #    the DOM, each of which must still be PRESENT to be excused.
            # ⚠️ EXPECTED PER PAGE, AND DERIVED RATHER THAN LISTED.
            # `Sign out` is in the top bar on all six screens; `Print` is on
            # the digest and the charts only. A hand-written table of which
            # control belongs on which page is the drifting artefact this
            # repo keeps learning about, so the expectation is read from the
            # page's OWN source: if the built file wires the handler, the
            # control has to be on the rendered page. If it does not, there
            # is nothing being exempted there and nothing to hide.
            saw = set(got.get("present") or [])
            for handler, label in EXEMPT_LABELS.items():
                if label in saw:
                    continue
                if handler not in src:
                    continue          # not wired on this screen at all
                problems.append(
                    "%s: this page wires %s, so %r should be on it — and the "
                    "sweep never saw it. %r is exempt from being PRESSED (%s); "
                    "an exemption that also excused it being GONE would hide a "
                    "deletion." % (what, handler, label, label,
                                   EXEMPT_OFFDOM[handler]))

            for d in got["dead"]:
                problems.append(
                    "%s: control %s (%s %r) changed nothing — no text, no "
                    "node count, no re-render. Nothing that looks pressable "
                    "may do nothing."
                    % (what, d["i"], d["tag"], d["label"]))

            # 5b. ⊕ MRB-287 — and every ADDITION was reachable and live.
            #     These are the controls this port put on a teacher's screen
            #     that Design did not draw. `build_teacher_port` proves each
            #     is in the emitted bytes; this proves a teacher can get to
            #     it and that it does something when they do.
            for m in got.get("addedGone", []):
                a = added_why.get(m, {})
                problems.append(
                    "%s: the addition %r (%s) is registered on this page and "
                    "the build proved it is IN the file — and nothing on "
                    "screen reveals it. Markup in the file that no press can "
                    "reach is a control that does not exist. (%s)"
                    % (what, a.get("label", m), m,
                       a.get("why", "").split(".")[0]))
            for d in got.get("addedDead", []):
                problems.append(
                    "%s: the addition %r (%s %r) changed nothing when "
                    "pressed. Design did not draw this control — it is here "
                    "because it was asked for, which makes a dead one worse "
                    "than a missing one."
                    % (what, d["i"], d["tag"], d["label"]))

            # 5c. ⊕ MRB-287 E1 — AND IT WENT WHERE IT SAID IT WOULD.
            #
            # ⚑ "MOVED" IS NOT "WORKED" FOR A CONTROL THAT NAVIGATES. The
            # check above is satisfied by any nav at all, so a year option
            # wired to the wrong screen — or to the right screen with no year
            # on it, which is the whole point of the control — passes it. The
            # register names the destination and the parameter that must
            # carry a value, and the recorded nav is compared against both.
            #
            # ⚠️ THE PARAMETER IS CHECKED FOR A VALUE, NOT FOR A PARTICULAR
            # ONE. Which uuid is right depends on which option the sweep
            # reached, and pinning it here would pin the fixture's ordering
            # rather than the control's behaviour. Empty is the failure that
            # matters: `MRB_GO` DROPS an empty param, so a year link that
            # computed nothing navigates to the working year and looks
            # exactly like a working control.
            navs_seen = got.get("addedNav") or {}
            for m in added_here:
                want_nav = (added_why.get(m) or {}).get("expect_nav")
                if not want_nav:
                    continue
                got_nav = navs_seen.get(m)
                if not got_nav:
                    problems.append(
                        "%s: the addition %r navigates nowhere. It is "
                        "registered to open %r, and pressing it reached "
                        "MRB_GO not at all."
                        % (what, m, want_nav.get("screen")))
                    continue
                if got_nav.get("screen") != want_nav.get("screen"):
                    problems.append(
                        "%s: the addition %r is registered to open %r and "
                        "pressing it went to %r instead."
                        % (what, m, want_nav.get("screen"),
                           got_nav.get("screen")))
                key = want_nav.get("param")
                val = (got_nav.get("params") or {}).get(key)
                if key and not val:
                    problems.append(
                        "%s: the addition %r reached %r with no %r "
                        "parameter (%r). MRB_GO DROPS an empty param, so "
                        "this navigates to the default and is "
                        "indistinguishable from a control that works — "
                        "which for a year selector means silently landing "
                        "the teacher back on the working year."
                        % (what, m, got_nav.get("screen"), key, val))

            # 6. And no press emptied the page. See the probe's note on
            #    node 78 — the control that navigated a pinned-screen page
            #    into a screen it had pruned, and blanked it.
            for d in got.get("blanked", []):
                problems.append(
                    "%s: control %s (%s %r) BLANKED the page — %d character(s) "
                    "of text left. A press that empties the dashboard is not a "
                    "working control, and it passes the liveness check above "
                    "because a blank page is a very large change."
                    % (what, d["i"], d["tag"], d["label"], d["left"]))

            # 7. Nothing threw while being pressed.
            for e in got["errors"]:
                problems.append("%s: pressing %s threw" % (what, e))

            # 7b. ⊕ MRB-287 — the search cap is DECLARED, in every state.
            #     Driven here rather than by the sweep above: the sweep types
            #     a fixed `zz` into every text field, which is the ONE case
            #     that can never truncate. A cap only lies when it bites.
            # ⚠️ A SKIP IS RECORDED, NEVER SWALLOWED. Two of the six pages
            #    prune the search overlay (`searchOpen` is not in their
            #    `overlays`), so "not here" is legitimate — but a probe that
            #    quietly does nothing on a page that DOES have the overlay is
            #    exactly the overstated coverage this file keeps catching. The
            #    tally below is printed, and a skip on a page whose template
            #    still wires `openSearch` is a problem.
            have = all(search_nodes.get(k) is not None
                       for k in ("opener", "input", "foot", "row"))
            if not have:
                # The legitimate absence is the WHOLE overlay being pruned.
                # ⊕ CORRECTED 2 Sep 2026 — this named digest.html and
                # insights.html as the two pages without `searchOpen`, and
                # BOTH have it now: screen 6 added it to the digest and
                # screen 7 to insights, because on both of them the top bar's
                # "Find a student" button shipped with no sheet to open and
                # pressing it did nothing at all. No page in the set prunes
                # the overlay today; the branch stays because a future one
                # may. The absence that is
                # NOT legitimate is the overlay being present with its caption
                # or its result row missing: the probe would then run on
                # nothing and this fixture would report a clean sweep.
                if search_nodes.get("input") is not None:
                    problems.append(
                        "%s: this page keeps the search overlay (the input is "
                        "in its template) and %s is not, so the cap check "
                        "measured nothing."
                        % (what, " and ".join(
                            k for k in ("foot", "row")
                            if search_nodes.get(k) is None) or "its opener"))
            else:
                got_s = json.loads(pg.eval(
                    _SEARCH_JS.replace("__NODES__",
                                       json.dumps(search_nodes))))
                if got_s.get("skip"):
                    problems.append(
                        "%s: the search cap check could not run — %s. The "
                        "overlay is in this page's template, so it should "
                        "have opened." % (what, got_s["skip"]))
                else:
                    for c in got_s["cases"]:
                        problems.extend(_search_problems(what, c))
                    if pass_n == 1:
                        tally["search"] += len(got_s["cases"])
                        if not got_s.get("several"):
                            tally["nosev"] += 1

            # 7c. ⊕ THE CHART CROSS PRODUCT — see the note beside _CHART_JS.
            #     Six kinds x both scopes, each drawn from a re-pressed scope
            #     so every cell is a redraw, and each one asked whether it
            #     says what it has.
            if page == "insights":
                got_c = json.loads(pg.eval(_CHART_JS))
                if got_c.get("err"):
                    problems.append("%s: the chart sweep could not run — %s"
                                    % (what, got_c["err"]))
                else:
                    cells = got_c.get("cells") or []
                    want = len(got_c.get("scopes") or []) * len(
                        got_c.get("kinds") or [])
                    if len(cells) != want or want < 12:
                        problems.append(
                            "%s: the chart sweep drew %d of %d cell(s) — %d "
                            "scope(s) x %d kind(s). Six kinds and two scopes "
                            "is twelve." % (what, len(cells), want,
                                            len(got_c.get("scopes") or []),
                                            len(got_c.get("kinds") or [])))
                    # ⚑ SIX KINDS, SIX TITLES. A chart whose `renderVals`
                    #   THREW never redraws, so the card still shows the
                    #   PREVIOUS kind — the page looks fine and the chip
                    #   looks pressed. A repeated title inside one scope is
                    #   that, and it is what the STEMS crash looked like from
                    #   the outside before it was found by hand.
                    for sc in (got_c.get("scopes") or []):
                        seen = {}
                        for c in cells:
                            if c.get("scope") != sc or c.get("miss"):
                                continue
                            seen.setdefault(c.get("title"), []).append(
                                c.get("kind"))
                        for t, ks in seen.items():
                            if len(ks) > 1:
                                problems.append(
                                    "%s: under %r, %s all draw the SAME card "
                                    "(%r). A chart that does not redraw is a "
                                    "chart whose render threw."
                                    % (what, sc, " and ".join(ks), t))
                    for c in cells:
                        where = "%s / %s" % (c.get("scope"), c.get("kind"))
                        if c.get("miss"):
                            problems.append("%s: chart %s — %s"
                                            % (what, where, c["miss"]))
                            continue
                        if pass_n == 1:
                            tally["charts"] += 1
                        if not c.get("title"):
                            problems.append(
                                "%s: chart %s drew no title. The card is "
                                "there and it does not say what it is."
                                % (what, where))
                        # ⚑ "EMPTY SCOPES HONEST", AS A CHECK RATHER THAN A
                        #   HOPE. No tiles, no series and no caption is an
                        #   empty card, and an empty card reads as zero.
                        if (not c.get("tiles") and not c.get("body")
                                and not c.get("note")):
                            problems.append(
                                "%s: chart %s has nothing to plot and says "
                                "nothing — no tile, no series, no caption. "
                                "An empty chart must state that it is empty."
                                % (what, where))
                        # ⚑ AND NOTHING MAY RENDER AS A COMPUTATION THAT
                        #   FAILED. `undefined/16` and `NaN` were both on
                        #   this screen on 2 Sep 2026, on a class with no
                        #   papers, in the two tiles a teacher reads first.
                        for bad in ("undefined", "NaN", "null%", "Infinity",
                                    "[object "):
                            if bad in (c.get("text") or ""):
                                problems.append(
                                    "%s: chart %s renders %r on screen"
                                    % (what, where, bad))

            # 8. And the console stayed quiet. A page can render correctly and
            #    still be throwing on every state change — the throw happens
            #    after the draw, which is the shape of bug that survives a
            #    screenshot.
            for line in pg.console_errors():
                if "favicon" in line:
                    continue
                problems.append("%s: console error — %s" % (what, line[:200]))

    return problems, tally


def main(argv):
    os.chdir(REPO)
    shots = None
    if "--shots" in argv:
        shots = argv[argv.index("--shots") + 1]
        os.makedirs(shots, exist_ok=True)
        argv = [a for a in argv if a != "--shots" and a != shots]
    only = [a for a in argv if not a.startswith("-")]

    sys.path.insert(0, REPO)
    import ks3_browser as cdp

    todo = [f for f in fixtures()
            if not only or any(o in f[1] for o in only)]
    missing = [f[1] for f in todo
               if not os.path.exists(os.path.join(PAGE_DIR, f[1]))]
    if missing:
        print("\nteacher_behaviour.py: not built — %s\n"
              "  Run `python3 build_teacher_port.py` first."
              % ", ".join(missing))
        return 1

    print("\n🖐  teacher_behaviour — the ported teacher pages, driven and "
          "pressed\n")
    # ⊕ 2 Sep 2026 — no longer "screens x 2": a screen may name more than one
    # empty state, so the count is reported rather than multiplied out.
    _empties = sorted({g for _s, _f, e, g in todo if e})
    print("     %d fixture(s) across %d screen(s): populated + %s, each "
          "driven\n             on load AND after a reload\n"
          % (len(todo), len({f[0] for f in todo}), "/".join(_empties)))

    server, port = cdp.serve(REPO)
    failed = 0
    total = {"found": 0, "pressed": 0, "added": 0, "search": 0,
             "nosev": 0, "charts": 0}
    try:
        for page, path, is_empty, slug in todo:
            problems, tally = drive(page, path, is_empty, cdp, port, shots,
                                    slug=slug)
            total["found"] += tally["found"]
            total["pressed"] += tally["pressed"]
            total["added"] += tally["added"]
            total["search"] += tally["search"]
            total["nosev"] += tally["nosev"]
            total["charts"] += tally["charts"]
            tag = (slug or "empty") if is_empty else "full "
            if problems:
                failed += 1
                print("     %-16s %s ❌ %d problem(s)"
                      % (page, tag, len(problems)))
                if is_empty:
                    print("        (%s)" % EMPTY_SHAPE.get((page, slug), ""))
                for p in problems[:10]:
                    print("        · %s" % p)
                if len(problems) > 10:
                    print("        · … and %d more" % (len(problems) - 10))
            else:
                print("     %-16s %s ✅  %d/%d control(s) pressed%s%s%s"
                      % (page, tag, tally["pressed"], tally["found"],
                         (" · %d addition(s) pressed by name"
                          % tally["added"]) if tally["added"] else "",
                         (" · %d search state(s)"
                          % tally["search"]) if tally["search"] else "",
                         (" · %d chart cell(s)"
                          % tally["charts"]) if tally["charts"] else ""))
    finally:
        server.shutdown()

    print()
    if failed:
        print("  FAIL  %d of %d fixture(s).\n" % (failed, len(todo)))
        return 1
    # ⚠️ THE RATIO IS PRINTED, NOT ROUNDED UP TO "every control".
    # This gate's summary used to say "every control moved something" while
    # its sweep was pressing two of twenty-seven — the handles it held were
    # detached by the first re-render and the loop skipped the rest in
    # silence. A gate that overstates what it measured is worse than one that
    # measures less, so the count it actually achieved is on the line.
    #
    # pressed < found is normal and not a failure: a press legitimately
    # removes other controls from the page (an overlay closes, a filter
    # empties a grid), and a control that is gone cannot be pressed.
    if total["search"]:
        # ⚑ SAID OUT LOUD, for the same reason the additions are. This is the
        # only check in the file that types a query and reads a sentence back,
        # and a silent cap is invisible to every other one.
        print("     %d search state(s) driven — the whole pool, several "
              "matches, one match and none — and the caption's numbers "
              "checked against what was on screen" % total["search"])
        if total["nosev"]:
            print("     ⚠️  %d fixture(s) had no single letter matching "
                  "between 2 and 11 names, so the several-matches state went "
                  "undriven there" % total["nosev"])
        print()
    if total["added"]:
        # ⚑ SAID OUT LOUD, because a coverage claim nobody can see is the
        # defect this gate's own summary line was written to stop. These are
        # the controls Design did not draw, pressed BY NAME out of
        # teacher_rulings.AMENDED_ADDITIONS rather than by ordinal.
        print("     %d addition(s) pressed by name: %s"
              % (total["added"],
                 ", ".join("%s (%s)" % (a["label"], a["marker"])
                           for a in R.AMENDED_ADDITIONS)))
        print()
    print("  PASS  %d fixture(s), %d of %d control(s) pressed. Every fixture "
          "mounted, every\n        binding resolved, nothing pressed left the "
          "page blank, no computed value\n        reached the copy, and the "
          "console stayed quiet — on load and again after\n        a reload.\n"
          % (len(todo), total["pressed"], total["found"]))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
