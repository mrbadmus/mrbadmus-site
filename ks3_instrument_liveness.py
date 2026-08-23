#!/usr/bin/env python3
"""ks3_instrument_liveness.py — does the instrument actually DO anything?

    python3 ks3_instrument_liveness.py            # every unit with built pages
    python3 ks3_instrument_liveness.py C3         # one unit
    python3 ks3_instrument_liveness.py --list     # what it would cover, no browser

── Why this exists ──────────────────────────────────────────────────────

An instrument fails in a way that looks like success. The markup renders, the
buttons are there, the colours are right, the page passes parity and passes
overflow and passes contrast — and nothing happens when a student presses the
button, because the marker attribute never reached the dispatch list in
`wireInstruments`, or the wire function threw on the way in.

Every other KS3 gate measures the page AT REST. This one presses the buttons.

The check is deliberately generic rather than per-instrument: for each marker
block on the page, find the controls inside it, click the first one that looks
like a control, and assert the block's own DOM changed. A wired instrument
responds to its own controls. A dead one is inert, and inert is exactly what
you cannot see in a screenshot.

It also fails on any console error raised during load, because a wire function
that throws takes every instrument after it in the dispatch list down with it —
which is the failure mode that hurts most and shows least.

── ⊕ MRB-282, 23 Aug 2026 · IT COVERED FOUR UNITS OF THIRTY-THREE ──────

This gate used to carry two hand-written tables: `INSTRUMENTS`, thirty-one
rows of (unit, marker, family), and `UNIT_DIRS`, four rows — C3, C8, C9, C10.
Everything else was invisible to it. All eleven biology units, all twelve
physics units, and C1, C2, C4, C5, C6, C7 had never had a button pressed by
this or by anything else, because this is the only gate that presses buttons.

And it ended a run by printing

    ✅ every registered instrument responded to its own controls.

which is TRUE, and reads as total coverage, and is not. "Registered" meant
"in the table above", not "in the registry" — 31 families of the 158 that
`ks3_art` actually registers. That sentence is the eleventh instance this week
of a gate whose output overstates its own scope, and it is the reason a
partial gate is more dangerous than a missing one: nobody goes looking for a
gate that says it already looked.

So neither table exists any more. BOTH are derived:

  UNITS      from `ks3_data.build_units()` — every unit, its built directory
             computed from its discipline and slug. A unit with no built
             directory is REPORTED by name, never skipped quietly.
  FAMILIES   from `ks3_art.load().kind_shell` — the registry that the
             generator itself dispatches on. A family that reaches the
             dispatch table now reaches this gate on the same commit, with
             nothing to remember.

Adding a unit or an instrument no longer means adding a line here. That was
the whole point of `ks3_art` being discovered rather than listed (MRB-271),
and a gate with its own private copy of the list defeats it.

The page is now loaded ONCE and every marker on it probed against that one
load. The old shape loaded a page per (marker, page) pair, so a page with
three instruments was fetched three times — widening from 4 units to 33 costs
less wall-clock than it looks like it should.
"""

import os
import re
import sys

import ks3_browser as cdp


def units(only=None):
    """(code, dir, authored_pages) per unit, plus the slots there is nothing
    to press on, plus the units whose built pages are missing entirely.

    Derived from `ks3_data.build_units()`, so a new unit is covered by this
    gate on the commit that builds it.

    ⚠️ AN UNAUTHORED SLOT IS NOT A FAILURE AND IS NOT COVERAGE EITHER. The
    structure-first guarantee (architecture.md §11 decision 8) ships a slot
    with no lesson as an honest ~3.4 KB coming-soon page: no instruments, no
    activities, nothing a student can press. Today that is the whole of
    physics (P1-P12, 70 slots), plus `acid-plus-alkali` in C6 and
    `metal-and-non-metal-oxides` in C8, both of which are ruled and recorded
    in their unit modules.

    They are counted and named in the coverage line rather than silently
    dropped, because "185 pages" and "113 pages with an instrument" are two
    very different claims and the difference is exactly what a reader of a
    green run needs to know.
    """
    import ks3_data
    found, soon, missing = [], [], []
    for u in ks3_data.build_units():
        if only and u["code"].upper() != only:
            continue
        d = os.path.join("ks3", u["discipline"], u["slug"])
        if not os.path.isdir(d):
            missing.append((u["code"], d))
            continue
        pages = []
        for lesson in u["lessons"]:
            p = lesson["slug"] + ".html"
            if not os.path.isfile(os.path.join(d, p)):
                missing.append((u["code"], os.path.join(d, p)))
            elif lesson.get("authored"):
                pages.append(p)
            else:
                soon.append((u["code"], lesson["slug"]))
        if pages:
            found.append((u["code"], d, pages))
    return found, soon, missing


_MARKER = re.compile(r"data-[a-z0-9-]+")

# family -> the verbatim attribute string the generator writes into the shell
# tag, e.g. `data-instrument data-pairs data-stage-done="0"`. Filled by
# families(). Page selection matches on THIS rather than on the marker alone:
# see the note in main().
SIGNATURE = {}
_NOT_A_MARKER = ("data-instrument", "data-stage-done")


def families():
    """family name -> marker attribute, from the ks3_art registry itself.

    `KIND_SHELL` maps a family to `(shell class, marker attributes)`, and the
    marker attributes are the string the generator writes into the block tag.
    The marker is the one `data-` attribute in there that is not the generic
    `data-instrument` flag or the `data-stage-done` counter.
    """
    import ks3_art
    reg = ks3_art.load()
    out, static, broken = {}, [], []
    for fam, value in sorted(reg.kind_shell.items()):
        attrs = value[1] if isinstance(value, (tuple, list)) and len(value) > 1 else ""
        attrs = attrs or ""
        marks = [m for m in _MARKER.findall(attrs) if m not in _NOT_A_MARKER]
        if marks:
            out[fam] = marks[0]
            SIGNATURE[fam] = attrs.strip()
        elif "data-instrument" in attrs:
            # Flagged for dispatch and carrying nothing to dispatch ON. This
            # is a defect: wireInstruments would have no selector to find it
            # by, so the block ships with controls that reach no wire.
            broken.append(fam)
        else:
            # STATIC, and legitimately so. `model-limit` (ks3_art/c2.py) is a
            # two-card teaching panel with no commitment and no control — it
            # carries no `data-instrument` flag, so nothing dispatches to it
            # and there is nothing that could be dead. It is named in the
            # coverage line rather than counted as covered, because a family
            # this gate cannot press is a family this gate does not watch.
            static.append(fam)
    return out, static, broken, reg


# Press the first thing inside the block that a student could press. Buttons
# first, then the radio/option controls the KS3 instruments use.
#
# ⚠️ SOME INSTRUMENTS ARE DELIBERATELY LOCKED, and an unlock is not a defect.
# C3's dissolving bench ships `hidden` behind `data-dlab-lock`, which names a
# PREDICT BLOCK elsewhere on the page: answer that and the bench arrives in the
# space the question was occupying (`ks3.js:17708`). A liveness check that
# cannot tell "locked" from "dead" reports every gated instrument as broken and
# is worse than no check at all — so this opens the gates first, by answering
# one option in every other activity block on the page, and only then presses
# the instrument's own controls.
PROBE = """
(function (sel) {
  function visible(c) {
    if (c.disabled) return false;
    var box = c.getBoundingClientRect();
    return !!(box.width || box.height);
  }
  // ⚠️ `[data-instrument]` IS PART OF THE SELECTOR, and it is load-bearing.
  // B1's `settles-it` uses `data-settles` twice: once as the instrument's
  // marker on the section, and once as a per-feature value on each of the
  // twelve `<li data-settles="0|1">` inside it. A bare `[data-settles]`
  // therefore matched thirteen elements, nine of them inside case panels
  // that are hidden until their tab is chosen, and reported all twelve
  // features as INERT instruments. The shell is the thing this gate has an
  // opinion about, and the shell is what carries `data-instrument`.
  var blocks = document.querySelectorAll('[data-instrument][' + sel + ']');
  if (!blocks.length) return { found: 0 };

  // Open any gate. An option click is what `openBench` and its siblings listen
  // for; answering a question the student would answer anyway is not cheating
  // the gate, it is reaching the instrument.
  var unlocked = 0;
  for (var b = 0; b < blocks.length; b++) {
    var blk = blocks[b];
    var box = blk.getBoundingClientRect();
    if (box.width || box.height) continue;              // already open
    var gates = document.querySelectorAll('[data-activity]');
    for (var g = 0; g < gates.length; g++) {
      if (gates[g].contains(blk) || blk.contains(gates[g])) continue;
      var opt = gates[g].querySelector('.ks3-option');
      if (opt && visible(opt)) { try { opt.click(); unlocked++; } catch (e) {} }
    }
  }

  var out = [];
  for (var b2 = 0; b2 < blocks.length; b2++) {
    var block = blocks[b2];
    var before = block.innerHTML;

    // ⚠️ SOME INSTRUMENTS ARE WRITTEN INTO, NOT PRESSED. C5's `rule-write`
    // is a textarea and a button that stays `disabled` until 60 characters
    // are in it (`wireRuleWrite`, shared/ks3.js). A probe that only clicks
    // sees one disabled button, calls the instrument inert, and is wrong.
    // Typing is a press. Fill every text field first, fire the events the
    // wiring listens for, and only then look for something to click.
    var typed = 0;
    var fields = block.querySelectorAll('textarea, input[type="text"], input:not([type])');
    for (var t = 0; t < fields.length; t++) {
      var f = fields[t];
      if (f.disabled || f.readOnly) continue;
      f.value = 'A student answer long enough to satisfy any minimum-commit '
              + 'threshold an instrument might set before it will respond.';
      try {
        f.dispatchEvent(new Event('input', { bubbles: true }));
        f.dispatchEvent(new Event('change', { bubbles: true }));
        typed++;
      } catch (e) { return { error: String(e) }; }
    }

    var controls = block.querySelectorAll(
      'button, [role="button"], input, select, textarea, [data-opt], .ks3-option, [tabindex]');
    var clicked = null, changed = false, tried = 0;
    for (var i = 0; i < controls.length; i++) {
      var c = controls[i];
      if (!visible(c)) continue;
      tried++;
      clicked = (c.tagName + (c.className ? '.' + String(c.className).split(' ')[0] : ''));
      try { c.click(); } catch (e) { return { error: String(e) }; }
      if (block.innerHTML !== before) { changed = true; break; }
    }
    out.push({
      controls: controls.length,
      reachable: tried,
      typed: typed,
      clicked: clicked,
      changed: changed,
      unlocked: unlocked,
      open: !!(block.getBoundingClientRect().width || block.getBoundingClientRect().height)
    });
  }
  return { found: blocks.length, blocks: out };
})(%s)
"""


def main():
    argv = sys.argv[1:]
    listing = "--list" in argv
    rest = [a for a in argv if not a.startswith("-")]
    only = rest[0].upper() if rest else None

    fams, static, broken, _reg = families()
    covered, soon, no_pages = units(only)
    if only and not covered and not soon and not no_pages:
        raise SystemExit("no unit named %r — see ks3_data/structure.py" % only)

    marker_of = fams
    by_marker = {}
    for fam, marker in marker_of.items():
        by_marker.setdefault(marker, []).append(fam)

    # ── which pages carry which markers, read from the built HTML ───────
    # ⚠️ A PAGE IS SELECTED BY THE SHELL SIGNATURE, NOT BY THE MARKER ALONE.
    # `data-pairs` is B1's `sort-pairs` marker AND was, until MRB-282, a
    # count attribute on C9's extraction bench (`data-pairs="24"`). Selecting
    # pages on the bare marker put both C9 pages on the plan, where the probe
    # correctly found no instrument shell and the gate called that a defect.
    # The signature — `data-instrument data-pairs data-stage-done="0"`,
    # verbatim as ks3_art writes it — cannot be matched by an unrelated
    # attribute of the same name.
    sig_of = {m: SIGNATURE[f] for f, m in marker_of.items()}
    plan = []          # (unit, dir, page, [markers on it])
    sources = {}       # (unit, page) -> built HTML
    seen_markers = set()
    for unit, d, pages in covered:
        for p in pages:
            src = open(os.path.join(d, p), encoding="utf-8").read()
            sources[(unit, p)] = src
            here = sorted(m for m in by_marker if sig_of[m] in src)
            if here:
                seen_markers.update(here)
            plan.append((unit, d, p, here))

    pressable = [row for row in plan if row[3]]
    quiet = [row for row in plan if not row[3]]
    soon_units = sorted({u for u, _s in soon})
    print("\n🔌  ks3_instrument_liveness — pressing the buttons\n")
    print("     COVERAGE, stated so it cannot be read as more than it is:\n")
    print("       %3d unit(s) with at least one authored lesson: %s"
          % (len(covered), " ".join(u for u, _d, _p in covered)))
    print("       %3d authored page(s), of which %d carry an instrument and "
          "%d do not" % (len(plan), len(pressable), len(quiet)))
    print("       %3d unauthored slot(s) NOT driven — coming-soon pages with "
          "nothing to press,\n           across %s"
          % (len(soon), " ".join(soon_units) or "no unit"))
    # ⚠️ FAMILIES AND MARKERS ARE NOT THE SAME COUNT, and reporting one as
    # the other misstates coverage in whichever direction happens to flatter.
    # B5 deliberately puts five families on `data-b5cblock` and two on
    # `data-cmpblock` — one wire function serving several — so 157 families
    # wear 152 distinct markers. Both numbers are printed.
    covered_fams = sorted(f for f, m in marker_of.items() if m in seen_markers)
    print("       %3d instrument family(ies) registered by ks3_art, wearing "
          "%d distinct\n           marker(s); %d family(ies) found in the "
          "built HTML"
          % (len(marker_of), len(set(marker_of.values())), len(covered_fams)))
    if static:
        print("       %3d STATIC family(ies) this gate cannot press, because "
              "they carry no\n           data-instrument flag and no marker: %s"
              % (len(static), ", ".join(static)))
    if only:
        print("\n     ⚠️  ONE UNIT ONLY (%s) — this is not a full run." % only)

    failures = []
    for unit, d in no_pages:
        failures.append("%s — no built pages under %s. The unit is in "
                        "structure.py and nothing generated it, so no gate "
                        "here or anywhere else is looking at it." % (unit, d))
    for fam in broken:
        failures.append("family %r declares data-instrument and no marker "
                        "attribute, so wireInstruments has no selector to "
                        "find its block by" % fam)
    # ⚠️ ONLY MEANINGFUL ON A FULL RUN. "This marker is on no page" is a
    # statement about the whole key stage; asserting it after scanning one
    # unit reports all 150 families the other twenty units place. A single-
    # unit run says so instead of pretending it looked everywhere.
    if only:
        print("\n     (a single-unit run cannot say which families are "
              "unplaced key-stage-wide;\n      that check is skipped, by "
              "name, and needs a full run.)")
    else:
        for marker in sorted(set(marker_of.values()) - seen_markers):
            failures.append("%s — marker %s appears on NO built page: the "
                            "instrument is registered and not emitted"
                            % ("/".join(sorted(by_marker[marker])), marker))

    # ── a marker on a page that does not host its instrument ────────────
    #
    # `shared/ks3.js` dispatches on the bare attribute — `each(root.query
    # SelectorAll("[data-pairs]"), wirePairs)` — over the WHOLE document. So
    # an unrelated element wearing a marker attribute gets another family's
    # wire function called on it. Today those functions bail on a missing
    # child and nothing breaks, which is the wire being defensive rather than
    # the markup being right; it is the collision MRB-279 ruled build-blocking
    # one level down, on the shell class.
    #
    # Reuse of a marker as an inner data attribute INSIDE its own instrument
    # is a different thing and is not reported here: B1 does it seven times
    # (`data-settles="0"` on each feature of the settles bench), the wire
    # function is called on the shell and on its own descendants, and it is
    # written to tolerate that. What is reported is a marker turning up on a
    # page that hosts no instrument of that family at all.
    _tag = re.compile(r"<[a-zA-Z][^>]*>")
    for (unit, p), src in sorted(sources.items()):
        # Cheap first pass: almost no page mentions almost any marker, and
        # tag-by-tag over 152 markers x 113 pages is minutes rather than
        # seconds. Only markers actually present in the text are worth
        # locating.
        suspect = [(m, f) for m, f in sorted(by_marker.items())
                   if m in src and sig_of[m] not in src]
        if not suspect:
            continue
        for tag in _tag.findall(src):
            if "data-instrument" in tag:
                continue
            for marker, fams in suspect:
                if re.search(r"\b" + re.escape(marker) + r"(\b|=)", tag):
                    failures.append(
                        "%s/%s carries %s, which is the instrument marker for "
                        "%s (ks3_art) and is not an instrument here. "
                        "shared/ks3.js dispatches that family's wire function "
                        "on it document-wide."
                        % (unit, p, marker, "/".join(sorted(fams))))

    if listing:
        print()
        for unit, d, p, here in plan:
            print("     %-4s %-46s %s" % (unit, p, " ".join(here) or "—"))
        print()
        for f in failures:
            print("        · " + f)
        return 1 if failures else 0

    # ── the sweep ───────────────────────────────────────────────────────
    #
    # Observations first, verdicts after. A block that renders NO CONTROL
    # cannot be dead in the sense this gate exists to catch — there is
    # nothing a student could press — but it cannot simply be waved through
    # either, because a renderer that dropped its buttons looks exactly the
    # same. The distinction is derivable and needs no hand-written list of
    # exceptions:
    #
    #   a family that renders zero controls on EVERY placement is STATIC by
    #   design; a family that renders controls on one page and none on
    #   another has LOST them, and that is a failure.
    #
    # Three families are static today and all three say so in their own
    # source: `confrontation` (ks3_art/core.py — a "Think again" misconception
    # panel, drawn by its block type, with no KIND_FN at all), `scale-cards`
    # (shared/ks3.js:10166 — "no behaviour to attach … `data-scalecards`
    # selects nothing in shared/ks3.js and is not meant to") and
    # `state-matrix` (a table lit from `data-from="s-bench"`, which responds
    # to the instrument above it rather than to a control of its own).
    #
    # They still carry `data-instrument`, and that is correct: the attribute's
    # job is to keep `wirePredictions` out (shared/ks3.js:372), which is a
    # property of the KIND rather than of today's markup.
    server, port = cdp.serve(".")
    seen_blocks = []          # (unit, family, page, index, block-result)
    try:
        with cdp.Browser() as b:
            current = None
            for unit, d, p, here in pressable:
                if unit != current:
                    current = unit
                    n = len([r for r in pressable if r[0] == unit])
                    print("\n     %s — %d page(s) with instruments\n" % (unit, n))
                page = b.page("http://127.0.0.1:%d/%s/%s" % (port, d, p))
                errs = page.console_errors()
                if errs:
                    failures.append("%s/%s — console error during load: %s"
                                    % (unit, p, errs[0]))
                    print("       \u274c %-44s console error" % p)
                    continue
                bad_here = []
                for marker in here:
                    name = "/".join(sorted(by_marker[marker]))
                    res = page.eval(PROBE % repr(marker))
                    if res.get("error"):
                        bad_here.append(name)
                        failures.append("%s/%s on %s — clicking threw: %s"
                                        % (unit, name, p, res["error"]))
                        continue
                    blocks = res.get("blocks") or []
                    if not blocks:
                        bad_here.append(name)
                        failures.append(
                            "%s/%s on %s — the marker is in the HTML and no "
                            "shell carrying it is found at runtime"
                            % (unit, name, p))
                        continue
                    for i, blk in enumerate(blocks):
                        seen_blocks.append((unit, name, p, i + 1, blk))
                        if not blk.get("changed") and blk.get("controls"):
                            bad_here.append(name)
                if bad_here:
                    print("       \u274c %-44s %s"
                          % (p, ", ".join(sorted(set(bad_here)))))
                else:
                    print("       \u2705 %-44s %d instrument(s)" % (p, len(here)))
    finally:
        server.shutdown()

    # ── verdicts ────────────────────────────────────────────────────────
    by_family = {}
    for unit, name, p, idx, blk in seen_blocks:
        by_family.setdefault(name, []).append((unit, p, idx, blk))

    static_families, pressed_blocks, static_blocks = [], 0, 0
    for name, rows in sorted(by_family.items()):
        with_controls = [r for r in rows if r[3].get("controls")]
        if not with_controls:
            static_families.append((name, len(rows)))
            static_blocks += len(rows)
            continue
        if len(with_controls) != len(rows):
            for unit, p, idx, blk in rows:
                if blk.get("controls"):
                    continue
                failures.append(
                    "%s/%s on %s — block %d renders NO control, while the "
                    "same family renders %d elsewhere. A family is static "
                    "everywhere or nowhere; this one lost its controls on "
                    "one page."
                    % (unit, name, p, idx, with_controls[0][3]["controls"]))
        for unit, p, idx, blk in with_controls:
            if blk.get("changed"):
                pressed_blocks += 1
                continue
            failures.append(
                "%s/%s on %s — block %d is INERT: %d control(s), %d "
                "reachable, %d field(s) typed into, %d gate(s) opened, block "
                "%s, clicked %s, DOM unchanged. The marker renders and "
                "nothing responds."
                % (unit, name, p, idx, blk["controls"], blk.get("reachable", 0),
                   blk.get("typed", 0), blk.get("unlocked", 0),
                   "visible" if blk.get("open") else "STILL HIDDEN",
                   blk.get("clicked")))

    print()
    if failures:
        print("     ❌ %d failure(s):\n" % len(failures))
        for f in failures:
            print("        · " + f)
        print()
        return 1
    # ⚠️ SAY WHAT WAS COVERED, NOT "everything". The sentence this replaces
    # read as total coverage while four units of thirty-three were measured.
    print("     ✅ %d instrument block(s) responded to their own controls, "
          "across %d page(s)\n        in %d unit(s), covering %d of the %d "
          "families ks3_art registers."
          % (pressed_blocks, len(pressable), len(covered), len(covered_fams),
             len(marker_of)))
    # ⚠️ SAY WHAT WAS NOT COVERED, IN THE SAME BREATH. The sentence this
    # replaces was "every registered instrument responded to its own
    # controls", printed while four units of twenty-one were measured.
    print("        NOT pressed: %d block(s) of %d static family(ies) (%s), "
          "%d authored page(s)\n        with no instrument, %d unauthored "
          "coming-soon slot(s).\n"
          % (static_blocks, len(static_families),
             ", ".join("%s x%d" % f for f in static_families) or "none",
             len(quiet), len(soon)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
