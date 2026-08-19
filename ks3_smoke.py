#!/usr/bin/env python3
"""
ks3_smoke.py — the interactive smoke gate. MRB-257 decision 3.

    "Two §8.10 leaks and the b1-03 specimen defect all survived static gates
     because they exist only in load-order or post-interaction state. The
     audit harness (one fresh Chrome per page, drive every control) already
     exists — it is repackaged as ks3_smoke.py with a small invariant set."

WHY THIS EXISTS, in one sentence: every gate we had asked whether the machinery
RAN, and none asked whether what it printed was a sentence.

The three defects that motivated it are worth naming, because each defeats a
different existing gate:

  · `[object Object]` on b1-03's bench caption. Nothing throws. The console is
    clean, contrast passes, the rail ticks. It is a valid string as far as the
    build is concerned, and it was on a live page for weeks.
  · The b1-03 specimen control reading "Leaf cell" while the engine drew a
    cheek cell — a control whose LABEL and whose RENDER disagree. No static
    check looks at that, and the page teaches the inverse of its own lesson
    with zero interaction.
  · The `b4-04` slug leaking into prose on `what-drugs-do-to-the-body`, behind
    FOUR interactions. A load-state sweep cannot see it. A gate for this class
    was built during the B10/B11 run and this one still survived it.

So the invariants are checked at load AND after a scripted control sweep, and
one of them is about agreement between a control and the state it claims.

Usage
    python3 ks3_smoke.py                 # every built lesson
    python3 ks3_smoke.py B1 B5           # named units (matches the path)
    python3 ks3_smoke.py --static        # the garbage strings only, no browser
    python3 ks3_smoke.py --max-pages 6   # sample, for a quick local run

`--static` is the fast half: a pure text scan over the built tree with no
browser at all. It is cheap enough to run on every build. The full interactive
sweep runs per unit shipped.

Exit 0 clean · 1 an invariant failed · 2 harness error.
"""

import argparse
import html
from html.parser import HTMLParser
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ks3_browser as cdp

REPO = os.path.dirname(os.path.abspath(__file__))
BUILT = os.path.join(REPO, "mrbadmus_site", "ks3")

# ── invariant 1 · nothing that is not a sentence ──────────────────────────
#
# Each entry is (regex, what it means). These are matched against the page's
# VISIBLE TEXT, not its markup — markup legitimately contains braces, and a
# student reads text.
GARBAGE = [
    (r"\[object Object\]",      "a JS object stringified into prose"),
    (r"\{'",                    "a Python dict repr published as content"),
    (r"\bdict_keys\(",          "a Python dict_keys repr"),
    (r"\{[a-z_][a-z0-9_]*\}",   "an unexpanded {placeholder}"),
    (r"\bundefined\b",          "a JS undefined reaching the page"),
    (r"\bNaN\b",                "a failed calculation"),
    # ── §8.10 · no platform self-explanation, and no build metadata ──
    # These two are the C4 family: the audit found eleven lessons telling
    # students which asset id is "awaiting illustration". The strings are
    # lifted from Design's own pages, so they can be re-authored innocently
    # at any time; the gate is the only thing that makes that impossible.
    (r"awaiting illustration",           "build metadata (C4) shown to a student"),
    (r"declared in the lesson record",   "build metadata (C4) shown to a student"),
    # ── internal lesson slugs. b4-04 leaked twice, one of them only after
    # four interactions. Matches b1-01..b11-99, c1-01.., p1-01.. — the
    # scheme in ks3_data/structure.py.
    (r"\b[bcp](?:1[01]|[1-9])-\d{2}\b",  "an internal lesson slug in prose"),
]
GARBAGE = [(re.compile(p, re.I), why) for p, why in GARBAGE]

# `b1-01`-shaped strings are legitimate inside these — a figure id in a data
# attribute is not prose. We only ever scan visible text, but the id pattern is
# loose enough that a caption legitimately naming a figure would trip it, so
# allow an explicit escape hatch that has to be spelled out.
SLUG_OK = re.compile(r"\b(?:b\d+-[a-z]{3,})")   # e.g. b5-pollen-tube, not b5-01


def visible_text_js():
    """Text a student can actually read: no script/style, no hidden subtrees."""
    return """
    (function () {
      function vis(el) {
        var s = window.getComputedStyle(el);
        if (s.display === 'none' || s.visibility === 'hidden') return false;
        if (el.hasAttribute && el.hasAttribute('hidden')) return false;
        return true;
      }
      var out = [], walk = document.createTreeWalker(
        document.body, NodeFilter.SHOW_TEXT, {
          acceptNode: function (n) {
            var p = n.parentElement;
            if (!p) return NodeFilter.FILTER_REJECT;
            if (/^(SCRIPT|STYLE|TEMPLATE)$/.test(p.tagName))
              return NodeFilter.FILTER_REJECT;
            for (var e = p; e && e !== document.body; e = e.parentElement) {
              if (!vis(e)) return NodeFilter.FILTER_REJECT;
            }
            return NodeFilter.FILTER_ACCEPT;
          }
        });
      var n; while ((n = walk.nextNode())) { out.push(n.nodeValue); }
      return out.join(' ').replace(/\\s+/g, ' ');
    })()
    """


# ── invariant 2 · the rail is a ratchet ───────────────────────────────────
#
# MRB-208: "nothing un-finishes it". MRB-257 decision 2 makes it a gate:
# "after any sequence of control presses, data-stage-done may never decrease."
# Two instruments were taking credit away — one for emptying a plate, one for
# exploring a second drug, which is the instrument's own invitation.
RAIL_JS = """
(function () {
  var out = [];
  document.querySelectorAll('section[data-stage-done]').forEach(function (s) {
    out.push([s.id, s.getAttribute('data-stage-done')]);
  });
  return JSON.stringify(out);
})()
"""


# ── invariant 3 · a control's claim matches the render ────────────────────
#
# The b1-03 defect exactly: a button shipping aria-pressed="true" while the
# engine drew a different specimen. We cannot know what a canvas "means", so
# we assert the weaker, checkable thing: within one radio-style group, exactly
# one control claims to be pressed, and the count never silently becomes zero
# or two. That is what went wrong on b1-03 — DOM order disagreed with the
# authored pressed state, so two sources of truth existed at once.
PRESSED_JS = """
(function () {
  // ⚠️ THE GROUP IS THE PARENT ELEMENT, not the section.
  //
  // Keying on the section lumped every `.ks3-option` in `#s-bench` into one
  // "group" — eleven buttons belonging to three separate questions — so
  // answering two questions looked like two controls pressed in one radio
  // group. That is a grouping artifact reported as a defect, and it is the
  // second false alarm this check produced; a gate that cries wolf gets
  // switched off, and this one guards a real defect (b1-03's specimen control
  // claiming "Leaf cell" while the engine drew cheek).
  //
  // Controls that exclude one another are SIBLINGS under one list or panel.
  // So the parent node is the group, and nothing coarser is safe.
  var groups = new Map(), out = [], seq = 0;
  document.querySelectorAll('main [aria-pressed]').forEach(function (b) {
    var p = b.parentElement;
    if (!p) { return; }
    if (!p.__ks3grp) { p.__ks3grp = 'g' + (++seq) + ':' + (p.className || p.tagName); }
    var rec = groups.get(p.__ks3grp) || {on: 0, n: 0, preset: false};
    rec.n += 1;
    if (b.getAttribute('aria-pressed') === 'true') { rec.on += 1; }
    // ⊕ MRB-257 phase 4 — PRESETS OVER A CONTINUOUS CONTROL ARE NOT A RADIO
    // GROUP. `changes-of-state`'s `.ks3-hb-jumps` are shortcuts onto a scrub
    // slider, and `wireHeatingBench` lights one only while the scrub is
    // within 3 units of it. Dragging the slider between two presets therefore
    // leaves none pressed, and that is CORRECT — "none of the presets is
    // where you are" is a true statement about a continuous control. Marked
    // structurally, not by page name: the group is a preset row when its
    // buttons carry a numeric value hook and the instrument around them
    // holds a range input driving the same value.
    if (b.hasAttribute('data-v')) {
      var block = b.closest('[data-instrument]') || b.closest('section');
      if (block && block.querySelector('input[type=range]')) {
        rec.preset = true;
      }
    }
    groups.set(p.__ks3grp, rec);
  });
  groups.forEach(function (v, k) { out.push([k, v.on, v.n, v.preset]); });
  return JSON.stringify(out);
})()
"""



# ── invariant 3b · a control that is clicked must become the pressed one ──
#
# This is the one that actually stands for b1-03, and the weaker "exactly one
# pressed" check above does NOT: under the original bug the specimen control
# shipped aria-pressed="true" on "Leaf cell" while `wireCellBench` seeded its
# state from `specBtns[0]` ("cheek") and `refresh()` never repainted the
# buttons. Exactly one button was pressed at load and exactly one after — the
# count invariant passes the whole way through, while the page teaches that a
# leaf cell has no wall, no vacuole and no chloroplasts, under a gate question
# about a leaf cell.
#
# What was actually broken is cheaper to state: you press a control and it does
# not become the pressed one. That generalises without knowing anything about
# any instrument, and it is what MRB-253 asked for — "a control's label and the
# state the engine renders must agree".
#
# Radio-like groups only, decided by the group's own load state, for the same
# reason as above: in a toggle bank a second press legitimately turns it OFF.
CLICK_FOLLOWS_JS = """
(function () {
  var seq = 0, groups = new Map(), bad = [];
  document.querySelectorAll('main [aria-pressed]').forEach(function (b) {
    var p = b.parentElement; if (!p) { return; }
    if (!p.__ks3g) { p.__ks3g = ++seq; }
    var g = groups.get(p.__ks3g) || [];
    g.push(b); groups.set(p.__ks3g, g);
  });

  // ⚠️ THE PROGRESS READOUT IS EXCLUDED FROM THE FINGERPRINT.
  // `[data-count]` is the head counter every instrument carries — "0 of 4
  // joints tried". Pressing a control legitimately advances it, so including
  // it made every radio group on `joints` and `antagonistic-muscle-pairs`
  // look like a load disagreement. Two false alarms, and this check only
  // earns its place if it is quiet when nothing is wrong.
  function fingerprint(root) {
    var out = [], w = document.createTreeWalker(root, NodeFilter.SHOW_TEXT, {
      acceptNode: function (n) {
        for (var e = n.parentElement; e && e !== root; e = e.parentElement) {
          if (e.hasAttribute && e.hasAttribute('data-count')) {
            return NodeFilter.FILTER_REJECT;
          }
        }
        return NodeFilter.FILTER_ACCEPT;
      }
    });
    var n; while ((n = w.nextNode())) { out.push(n.nodeValue); }
    return out.join(' ').replace(/[\\s]+/g, ' ').trim();
  }

  groups.forEach(function (btns) {
    if (btns.length < 2) { return; }
    var on = btns.filter(function (b) {
      return b.getAttribute('aria-pressed') === 'true'; });
    if (on.length !== 1) { return; }          // not radio-like

    // ══ THE LOAD-STATE AGREEMENT CHECK — the b1-03 assertion ══
    //
    // Pressing the control that ALREADY claims to be pressed must be a no-op.
    // If the section's rendered text changes, what was on screen at load was
    // not what the pressed control said was on screen. That is exactly b1-03:
    // the specimen button read "Leaf cell" while `wireCellBench` seeded from
    // DOM order and drew a cheek cell, so the page taught that a leaf cell has
    // no wall, no vacuole and no chloroplasts — with zero interaction, under a
    // gate question about a leaf cell.
    //
    // The count-based invariant above cannot see this: exactly one control was
    // pressed before and exactly one after, the whole way through.
    //
    // ⊕ The companion "a clicked control becomes the pressed one" check was
    // REMOVED. Load state cannot reliably tell a radio group from a toggle
    // bank, and in a toggle bank a second press legitimately turns a control
    // OFF — which the check read as the click being ignored, six times on
    // `specialised-cells` alone. It added no signal the load check does not
    // already carry, and noise in a gate is not free.
    var host = btns[0].closest('section') || document.body;
    var before = fingerprint(host);
    try { on[0].click(); } catch (e) { return; }
    var after = fingerprint(host);
    if (before !== after) {
      bad.push('LOAD DISAGREEMENT | "'
        + (on[0].textContent || '').trim().slice(0, 40)
        + '" shipped aria-pressed="true", but pressing it CHANGED the section — '
        + 'so the engine was not rendering what the control claimed');
    }
  });
  return JSON.stringify(bad);
})()
"""


# ── the control sweep ─────────────────────────────────────────────────────
#
# Clicks every enabled control once, in DOM order, re-reading state as it
# goes. Deliberately NOT exhaustive over combinations — the audit did that
# once, with 17 agents. This is the regression net: cheap enough to run per
# unit shipped, and it reaches post-interaction state, which is the whole
# point. Range inputs are stepped to both extremes and the middle.
SWEEP_JS = """
(function () {
  var pressed = 0;
  var btns = Array.prototype.slice.call(
    document.querySelectorAll('main button:not([disabled])'));
  for (var i = 0; i < btns.length && i < %(cap)d; i++) {
    try { btns[i].click(); pressed++; } catch (e) {}
  }
  document.querySelectorAll('main input[type=range]').forEach(function (r) {
    [r.min, String((Number(r.min) + Number(r.max)) / 2), r.max].forEach(function (v) {
      try {
        r.value = v;
        r.dispatchEvent(new Event('input',  {bubbles: true}));
        r.dispatchEvent(new Event('change', {bubbles: true}));
      } catch (e) {}
    });
  });
  return pressed;
})()
"""


class _Split(HTMLParser):
    """Split served HTML into what a student sees AT LOAD and what is templated.

    The distinction is load-bearing and cost one false alarm to learn. A
    `{placeholder}` inside a `hidden` panel is CORRECT — it is an unfilled
    template the engine writes into before revealing; `the-photosynthesis-
    reaction` ships `More than one thing is missing: {missing}.` exactly that
    way. Flagging it would be the gate crying wolf, and a gate that cries wolf
    gets switched off.

    But hidden content is also precisely where the worst leak hid: the `b4-04`
    slug on `what-drugs-do-to-the-body` sits behind FOUR interactions, and a
    load-state sweep is why it survived the gate built to catch it.

    So we keep both and judge them differently: everything is checked in hidden
    content EXCEPT the placeholder pattern, which is only a defect where a
    student can actually read it.
    """

    SKIP = {"script", "style", "template"}

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.vis, self.hid = [], []
        self._depth_hidden = 0
        self._skip = 0
        self._stack = []

    def handle_starttag(self, tag, attrs):
        if tag in self.SKIP:
            self._skip += 1
            return
        d = dict(attrs)
        hidden = ("hidden" in d) or (d.get("aria-hidden") == "true") \
            or ("display:none" in (d.get("style") or "").replace(" ", ""))
        self._stack.append((tag, hidden))
        if hidden:
            self._depth_hidden += 1

    def handle_endtag(self, tag):
        if tag in self.SKIP:
            self._skip = max(0, self._skip - 1)
            return
        for i in range(len(self._stack) - 1, -1, -1):
            if self._stack[i][0] == tag:
                if self._stack[i][1]:
                    self._depth_hidden = max(0, self._depth_hidden - 1)
                del self._stack[i:]
                break

    def handle_data(self, data):
        if self._skip:
            return
        (self.hid if self._depth_hidden else self.vis).append(data)

    @staticmethod
    def _norm(parts):
        return re.sub(r"\s+", " ", "".join(parts))

    def result(self):
        return self._norm(self.vis), self._norm(self.hid)


PLACEHOLDER_RX = re.compile(r"\{[a-z_][a-z0-9_]*\}")



# ── proving the gate ──────────────────────────────────────────────────────
#
# Build contract §6.5: "Every new assertion mutation-tested — an assertion that
# still passes against a deliberately broken page is not an assertion."
#
# A garbage gate is exactly the kind that rots quietly: tighten a regex by one
# character and it silently stops matching, and nothing tells you, because a
# clean run and a broken gate look identical. So the gate carries its own
# mutation test and it is not optional — `--self-test` injects one specimen per
# pattern and fails if any specimen is not caught.
SPECIMENS = [
    ("[object Object]",                       "a JS object stringified into prose"),
    ("{'headline': 'x', 'body': 'y'}",        "a Python dict repr published as content"),
    ("dict_keys(['a'])",                      "a Python dict_keys repr"),
    ("you have {count} left",                 "an unexpanded {placeholder}"),
    ("the answer is undefined",               "a JS undefined reaching the page"),
    ("it took NaN seconds",                   "a failed calculation"),
    ("awaiting illustration",                 "build metadata (C4) shown to a student"),
    ("declared in the lesson record",         "build metadata (C4) shown to a student"),
    ("that is b4-04's subject",               "an internal lesson slug in prose"),
]


def self_test():
    """Inject one specimen per pattern; every one must be caught."""
    bad = 0
    print("  self-test: %d specimens, one per garbage pattern" % len(SPECIMENS))
    for text, expect in SPECIMENS:
        found = []
        scan("teaching prose " + text + " more prose", "self", "SPECIMEN", found)
        got = [f for f in found if expect in f]
        if got:
            print("     caught   %-38r -> %s" % (text[:36], expect))
        else:
            print("     MISSED   %-38r -> expected %s" % (text[:36], expect))
            bad += 1

    # And the one thing that must NOT be caught: a placeholder inside a
    # template. If this starts failing, the visible/hidden split has broken and
    # the gate is about to start crying wolf.
    sp = _Split()
    sp.feed("<div hidden><p>missing: {missing}.</p></div><p>real prose</p>")
    vis, hid = sp.result()
    noise = []
    scan(hid, "template", "SPECIMEN", noise, skip=PLACEHOLDER_RX)
    if noise:
        print("     LEAK     a templated {placeholder} was flagged: %s" % noise[0])
        bad += 1
    else:
        print("     ignored  a {placeholder} inside a hidden template, correctly")
    if "{missing}" in vis:
        print("     LEAK     hidden content leaked into the visible split")
        bad += 1

    print()
    if bad:
        print("  ❌ ks3_smoke self-test: %d pattern(s) not doing their job" % bad)
        return 1
    print("  ✅ ks3_smoke self-test: every pattern catches its specimen")
    return 0


def built_lessons(units):
    out = []
    for root, _d, files in os.walk(BUILT):
        for f in sorted(files):
            if not f.endswith(".html") or f == "index.html":
                continue
            p = os.path.join(root, f)
            rel = os.path.relpath(p, BUILT)
            if "Coming soon" in open(p, encoding="utf-8", errors="replace").read():
                continue
            if units and not any(u.lower() in rel.lower() for u in units):
                continue
            out.append((rel, p))
    return sorted(out)


def scan(text, where, rel, problems, skip=None):
    for rx, why in GARBAGE:
        if skip is not None and rx.pattern == skip.pattern:
            continue
        for m in rx.finditer(text):
            hit = m.group(0)
            if rx.pattern.startswith(r"\b[bcp]") and SLUG_OK.search(hit):
                continue
            i = max(0, m.start() - 60)
            problems.append(
                "%s [%s] %s — %r\n        …%s…"
                % (rel, where, why, hit, text[i:m.end() + 60].strip()))


def unit_of(rel):
    parts = rel.split(os.sep)
    return os.sep.join(parts[:2]) if len(parts) > 1 else rel


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("units", nargs="*", help="path fragments, e.g. B1 reproduction")
    ap.add_argument("--static", action="store_true",
                    help="garbage strings only, no browser — cheap, every build")
    ap.add_argument("--max-pages", type=int, default=0)
    ap.add_argument("--click-cap", type=int, default=60)
    ap.add_argument("--self-test", action="store_true",
                    help="prove each garbage pattern catches its specimen")
    a = ap.parse_args()

    if a.self_test:
        return self_test()

    if not os.path.isdir(BUILT):
        sys.stderr.write("no built tree at %s — run build_ks3.py first\n" % BUILT)
        return 2

    pages = built_lessons(a.units)
    if a.max_pages:
        pages = pages[:a.max_pages]
    if not pages:
        sys.stderr.write("no built lesson matched %s\n" % (a.units or "(all)"))
        return 2

    problems = []

    # ── the static half ───────────────────────────────────────────────────
    for rel, path in pages:
        sp = _Split()
        sp.feed(open(path, encoding="utf-8", errors="replace").read())
        vis, hid = sp.result()
        scan(vis, "served", rel, problems)
        # Templates are checked for everything a student must never meet, but
        # NOT for unfilled placeholders — that is what a template is.
        scan(hid, "template", rel, problems, skip=PLACEHOLDER_RX)

    print("  static: scanned %d built lesson(s) for %d garbage patterns"
          % (len(pages), len(GARBAGE)))
    if a.static:
        return report(problems)

    # ── the interactive half ──────────────────────────────────────────────
    server, port = cdp.serve(os.path.join(REPO, "mrbadmus_site"))
    try:
        for rel, _p in pages:
            url = "http://localhost:%d/ks3/%s" % (port, rel.replace(os.sep, "/"))
            # ⚠️ A FRESH BROWSER PER PAGE, and this is not caution — the KS3
            # canvas loops keep running after the driver moves on, and one
            # shared browser accumulates enough of them to drop the DevTools
            # socket around the twelfth page. Learned in the MRB-220 run and
            # written into the build contract's harness notes.
            try:
                with cdp.Browser() as b:
                    pg = b.page(url)

                    load_txt = pg.eval(visible_text_js())
                    scan(load_txt, "load", rel, problems)
                    rail0 = json.loads(pg.eval(RAIL_JS))
                    press0 = json.loads(pg.eval(PRESSED_JS))

                    for line in json.loads(pg.eval(CLICK_FOLLOWS_JS)):
                        problems.append(
                            "%s [control] %s. A control and the state it claims "
                            "must agree — this is how b1-03 taught, on load and "
                            "with no interaction, that a leaf cell has no wall, "
                            "no vacuole and no chloroplasts." % (rel, line))

                    pg.eval(SWEEP_JS % {"cap": a.click_cap})

                    after_txt = pg.eval(visible_text_js())
                    scan(after_txt, "after-sweep", rel, problems)
                    rail1 = json.loads(pg.eval(RAIL_JS))
                    press1 = json.loads(pg.eval(PRESSED_JS))

                    before = dict(rail0)
                    for sid, done in rail1:
                        was = before.get(sid, "0")
                        if was == "1" and done != "1":
                            problems.append(
                                "%s [rail] stage %s went %s -> %s. MRB-208: "
                                "nothing un-finishes it." % (rel, sid, was, done))

                    # ⚠️ ONLY RADIO-LIKE GROUPS ARE CONSTRAINED, and the group's
                    # own load state is what says whether it is one.
                    #
                    # The first cut of this asserted "at most one pressed" on
                    # every group and produced 41 findings across the corpus,
                    # every one of them wrong: `s-fold`'s three levels and
                    # `s-jobs`' five switches are TOGGLE BANKS, where all-on is
                    # the state the block exists to reach. Proven not guessed —
                    # five flagged pages had built HTML byte-identical to HEAD.
                    #
                    # A gate that cries wolf gets switched off, which would have
                    # cost the one real defect this invariant is for: b1-03's
                    # specimen control shipping aria-pressed="true" while the
                    # engine rendered a different specimen. That IS a radio
                    # group — exactly one pressed at load — so the empirical
                    # test is also the correct one. If a group opens with
                    # exactly one control pressed, mutual exclusion is what it
                    # means, and it must still hold after the sweep.
                    b0 = {k: (on, n, preset) for k, on, n, preset in press0}
                    for key, on, n, preset in press1:
                        was = b0.get(key)
                        if not was or was[1] < 2 or was[0] != 1:
                            continue          # toggle bank, or new — not radio
                        if on > 1:
                            problems.append(
                                "%s [aria-pressed] '%s' opened with exactly one of "
                                "%d controls pressed, so it is a radio group — and "
                                "after the sweep %d of them claim to be pressed at "
                                "once" % (rel, key, n, on))
                        elif on == 0 and not (preset or was[2]):
                            # ⚠️ "TWO OR MORE PRESSED" IS STILL A DEFECT ON A
                            # PRESET ROW and is deliberately NOT excused above:
                            # presets are still mutually exclusive positions on
                            # the same control. Only the empty state is
                            # legitimate, and only because the control they are
                            # presets FOR has values between them.
                            problems.append(
                                "%s [aria-pressed] radio group '%s' had a pressed "
                                "control and now has none" % (rel, key, ))

                    for e in pg.console_errors():
                        problems.append("%s [console] %s" % (rel, e))
            except Exception as exc:                       # noqa: BLE001
                problems.append("%s [harness] %s: %s"
                                % (rel, type(exc).__name__, exc))
            print("    driven %s" % rel)
    finally:
        server.shutdown()

    return report(problems)


def report(problems):
    print()
    if not problems:
        print("  ✅ ks3_smoke: clean")
        return 0
    by_unit = {}
    for p in problems:
        by_unit.setdefault(unit_of(p.split(" ")[0]), []).append(p)
    for unit in sorted(by_unit):
        print("  ── %s" % unit)
        for p in by_unit[unit]:
            print("     %s" % p)
    print()
    print("  ❌ ks3_smoke: %d problem(s)" % len(problems))
    return 1


if __name__ == "__main__":
    sys.exit(main())
