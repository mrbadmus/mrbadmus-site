#!/usr/bin/env python3
"""student_themes.py — the colour gate on the PORTED student class page.

    python3 student_themes.py

Exit 0 clean, 1 on any divergence.

── Why this file exists: nothing was watching the port's colour ─────────

`student_parity.py` does NOT watch the ported page. That is measured, not
supposed: its `PAIRS`, its `COUNT_SOURCES` and the `ks3_parity.ST_SWEEP_PAGES`
it drives all name the PREVIEW pair — `student/class-preview.html` — which
`build_student.py` writes by snapshotting Design's own standalone in headless
Chrome with NO RULINGS APPLIED. The preview is a photograph of Design's file.
Parity therefore proves that a photograph matches its subject, which is true
and says nothing whatever about `student/class.html`.

`student_behaviour.py` is the only gate that drives the port, and it compares
visible TEXT and the CONTROL list. Neither of those can see a colour. A page
rendered entirely in one hue, or in two that cannot be told apart, passes every
drive it makes — the words are all still there.

So between the two of them there was an exact hole, and Design's amendments
just walked into it. The 21 Aug delivery made the bench, the term spine and the
leaderboard card THEMEABLE: six themes, a new default, and a token set
(`--b-ground --b-ink --b-muted --b-ember`) that every one of those surfaces now
reads its colour from. That is precisely and only a colour change. Until this
file existed it would have shipped unwatched.

── What this gate is, and what it refuses to be ─────────────────────────

It is not a screenshot comparison. It reads COMPUTED style off the live page
and does arithmetic on it — WCAG 2.1 relative luminance, sRGB linearised, the
real formula rather than a cheap approximation, because the whole value of a
contrast gate is that its number is the number a student's eye is subject to.

Design's README states its own contrast figures. This file transcribes them
(see `THEMES`) and then MEASURES rather than trusts them. The AA floor of 4.5
is the gate. Design's stated arithmetic is a claim, checked and reported beside
the measurement, and a divergence in it is a row to read, not a build to stop:
if Design says 6.09 and the page delivers 6.02, the student is fine and the
README is 0.07 out. If Design says 6.09 and the page delivers 3.1, the student
is not fine, and that is the failure this exists for.

── The self-proof ───────────────────────────────────────────────────────

A sweep that finds nothing has said nothing until it has been shown finding
something — the same standard `student_parity.py` holds its layers E/F/H to and
`student_behaviour._prove_additions` holds its registry to. So before it reports
anything, this file breaks the page on purpose, twice, and requires its own
assertions to go red; then unbreaks it and requires them to go green. If an
injected violation is NOT caught, the run FAILS saying exactly that — its
silence would otherwise be indistinguishable from a mechanism that cannot see.
"""

import os
import sys
import time

SITE = "mrbadmus_site"
PAGE = "student/class-fixture.html"

# ⚠️ THE FIXTURE, NOT THE PRODUCTION PAGE — the same choice, for the same
# reason, that `student_behaviour.py` documents at length. `class.html` carries
# no data of its own; it mounts whatever the database held that morning. The
# fixture is the same bytes apart from its banner and its last two script tags,
# and it is what has known values to drive. Colour is a property of the CSS and
# the markup, neither of which the data seam touches, so driving the fixture
# measures the production page's palette exactly.

VIEWPORT = (1460, 1200)

AA = 4.5          # WCAG 2.1 AA for small text — these tokens all carry some.
STATED_TOL = 0.15  # beyond this, Design's stated figure gets a row. Not a fail.

# ── the RENDERED-TEXT sweep, and why asserting the tokens was not enough ─
#
# ⊕ 23 Aug 2026 — ADDED AFTER THIS GATE PASSED A 1.78:1 LABEL.
#
# Everything above asserts the `--b-*` TOKENS: that `--b-ink`, `--b-muted` and
# `--b-ember` each clear AA against `--b-ground`. All eighteen figures were
# green, and three of the bench's most important words were invisible anyway.
#
# The gap is exact. The bench checklist — "Open it" / "Answer the eight
# questions" / "Hand it in" — was not painted in ANY of those three tokens. It
# was painted `--st-room-text`, a token the theme bridge had missed, fixed at
# `#B7AA98` and declared "readable text on dark". On the five dark themes it
# measured 5.55:1. On CHALK, whose ground is the light `#EFE2CB`, it measured
# **1.78:1** — and this gate had nothing whatever to say about it, because the
# question it asked was "are the theme's tokens legible on the theme's ground",
# and the answer to that was, truthfully, yes.
#
# So it now asks the question a student's eye actually asks: EVERY text-bearing
# leaf inside the bench, on every one of the seven cases, against whatever is
# really painted behind it. That assertion cannot be satisfied by a token the
# text does not use, which is the whole difference.
#
# ── the one registered exception ────────────────────────────────────────
#
# The docket's header band reads "This week's assignment" at #7A6E5F on
# #F2E8D6 — 4.09:1, below the floor. It is registered rather than fixed, and
# rather than the floor being lowered to fit it, for three reasons that are
# checked rather than asserted:
#
#   · it is DESIGN'S OWN docket styling, not a theme token;
#   · it is THEME-INDEPENDENT — identical on all seven cases, which is itself
#     the ruling the docket check enforces two functions down;
#   · it is PRE-EXISTING. It measured 4.09 before the themes existed and the
#     themes did not move it. Failing this unit for it would be reporting an
#     old defect as a new regression.
#
# ⚠️ IT IS ASSERTED IN BOTH DIRECTIONS, and the second direction is the point.
# Exempting a string is easy and rots silently: the day Design darkens that
# band, a bare exemption keeps quietly excusing a string that no longer needs
# it, and the gate is one row weaker forever with nobody told. So the entry
# must still be FOUND, on every case, at these exact colours and within `tol`
# of this ratio. If Design fixes it, this registration goes RED as stale and
# whoever is here next deletes it. An exception that cannot go stale is a hole.
#
# ⚠️ NOT A FLOOR CHANGE. `AA` stays 4.5 for everything else. One string is
# named, at one pair of colours, with its ratio pinned; nothing else in the
# bench is excused by it, and a SECOND string appearing at 4.2 fails.
BENCH_TEXT_EXCEPTIONS = [
    {
        "name": "the docket's header band",
        "text": "This week’s assignment",
        "fg": "#7A6E5F",
        "bg": "#F2E8D6",
        "ratio": 4.09,
        "tol": 0.06,
        "why": "Design's own docket styling, theme-independent, and it "
               "measured 4.09 before the bench themes existed — the themes "
               "did not move it.",
    },
]

# ── page chrome: espresso, fixed, and the two near-blacks still standing ─
#
# ⊕ 23 Aug 2026 — PHASE 1a. Design's amended README, change 1:
#
#     "no page chrome is near-black any more. Page-chrome dark is now
#      espresso #4A3728 (10.4:1 on cream) — top rule, work-row and legend
#      DONE dots."
#
# Everything above this point measures the BENCH. This measures the page the
# bench sits on, and it exists because that is a different problem with a
# different failure mode: the bench's colours MOVE with the theme and must
# stay legible on each; page chrome must NOT move with the theme at all.
#
# ⚠️ THE FIXEDNESS IS THE ASSERTION, not a side note. Page chrome routed
# through a `--b-*` token would put the theme's ground on the cream page —
# `#EFE2CB` on `#FBF3E6` is about 1.1:1 on chalk — which is the defect
# `student_rulings.py` records refusing on the term spine's `numColor`. So
# `--pg-strong` is read off `:root` on all seven cases and required to be the
# same fixed hex every time.
PAGE_STRONG = "#4A3728"
PAGE_GROUND = "#FBF3E6"
PAGE_STRONG_RATIO = 10.20       # measured; Design's README states 10.4
PAGE_STRONG_TOL = 0.05

# How many marks the page-chrome rule is expected to paint, by kind. A count
# is asserted for the same reason every `one()` selector above reports one:
# a selector that matches nothing must fail, not pass quietly.
#
#   legend-done     1  the term spine's legend dot beside the word DONE
#   work-row-done   3  one per MARKED row in the fixture's work list
#   tile-seg        4  the week tiles' done segments, found without an index
#                      by their own `background:var(--pg-strong)`
PAGE_STRONG_MARKS = {"legend-done": 1, "work-row-done": 3, "tile-seg": 4}

# ── the near-blacks that are still on the page, and why each is allowed ──
#
# Design's sentence is absolute — "no page chrome is near-black any more" —
# and the page is not there yet, because two of the elements it is about are
# owned by units that have not landed. Registering them beats either lying
# about the property or dropping the sweep: each must still be FOUND, at its
# registered colour, on every case. When Phase 2b replaces the recall card and
# the leaderboard's week chips take the bench theme, these two go stale and
# this gate says so instead of quietly excusing elements that no longer exist.
PAGE_CHROME_EXCEPTIONS = [
    {
        "tpl": "136",
        "bg": "#15110C",
        "name": "the sidebar RECALL card",
        "why": "Design's C2 replaces this card wholesale with the themed "
               "flashcards card. It stops existing; it does not turn "
               "espresso. Not this unit's to move.",
    },
    {
        "tpl": "256",
        "bg": "#221E1B",
        "name": "the leaderboard's selected week chip",
        "why": "Design's change 1 says the week chips take the BENCH THEME, "
               "not espresso. Unfinished theme work, not page chrome.",
    },
]


# ── Design's own stated figures, transcribed ─────────────────────────────
#
# From `docs/ks3/design-reference/class-view-amendments/README.txt`, lines
# 47-75, section "BENCH THEMES". These are DESIGN'S OWN NUMBERS, copied here
# verbatim so that a change to either side shows up as a disagreement rather
# than as a silent re-baselining.
#
# ⚠️ This gate MEASURES these; it does not trust them. The hexes are asserted
# against the page's computed tokens. The ratios are recomputed from the
# measured hexes and reported beside Design's claim. The AA floor is the gate.
#
#   name       ground     ink        ink_r   muted      muted_r  ember      ember_r
THEMES = [
    ("harbour",  "#20363F", "#FBF3E6", 11.48, "#A9BFC6", 6.60, "#F79E76", 6.09),
    ("clay",     "#6B4A33", "#FBF3E6",  7.19, "#E0CDB4", 5.11, "#FFC4A6", 5.16),
    ("chalk",    "#EFE2CB", "#221E1B", 12.93, "#6A5C4C", 5.05, "#A93411", 5.15),
    ("moss",     "#294036", "#FBF3E6", 10.14, "#B4C6B6", 6.22, "#F79E76", 5.37),
    ("damson",   "#38243A", "#FBF3E6", 12.87, "#C6AFC4", 6.97, "#F79E76", 6.82),
    ("graphite", "#1A1512", "#FBF3E6", 16.44, "#A99C8C", 6.74, "#F0855C", 7.08),
]
BY_NAME = {t[0]: t for t in THEMES}
DEFAULT_THEME = "harbour"      # README: "(absent = harbour)"
OLD_DEFAULT = "graphite"       # README: "GRAPHITE (the old default, opt-in)"

# The seven cases. `None` is the attribute ABSENT, and it is not a seventh
# theme — it is the DEFAULT, and the amendment's entire point is that the
# default moved off graphite. A default that silently reverts is the failure
# this case catches, so it is asserted twice: absent == harbour, and
# absent != graphite.
CASES = [None] + [t[0] for t in THEMES]

# ── ⊕ 23 Aug 2026 — PHASE 1b. THE PICKER ─────────────────────────────────
#
# Everything above measures what a theme LOOKS like once it is on. None of it
# can see whether a student can choose one: the seven cases are driven by
# setting `data-bench-theme` from the outside, which is exactly what no student
# can do. Six correct themes and no way to reach five of them is the state this
# page shipped in on 23 August, and every assertion in this file was green
# throughout it.
#
# So this half presses the swatches. Design's order, Design's labels, and the
# labels are asserted rather than derived from `THEMES` — the six words are
# what a student reads, and a gate that generated them from the same list the
# page is built from could not see them go wrong together.
PICKER_LABELS = ["CLAY", "CHALK", "MOSS", "HARBOUR", "DAMSON", "GRAPHITE"]

# The order the six are PRESSED in. Not alphabetical and not Design's: it
# starts on the swatch the page is NOT on, so the very first press is a real
# change of state rather than a no-op that would prove nothing, and it ends on
# HARBOUR so the page is left on the default for anything that runs after.
PICKER_ORDER = ["CHALK", "CLAY", "GRAPHITE", "MOSS", "DAMSON", "HARBOUR"]

# The tick inside a selected swatch is a GRAPHIC, not text, so it is held to
# WCAG's non-text floor rather than to AA 4.5. The word under the swatch is
# text and is held to AA like everything else on this page.
NONTEXT_AA = 3.0


# ══════════════════════════════════════════════════════════════════════════
# colour arithmetic — WCAG 2.1, written out rather than approximated
# ══════════════════════════════════════════════════════════════════════════

def parse_colour(s):
    """`rgb(r, g, b)` / `rgba(r, g, b, a)` / `#rrggbb` -> (r, g, b, a) ints+float.

    Raises on anything else. A colour this file cannot parse is a finding, not
    a thing to guess at: `transparent` on a surface that is supposed to carry
    the theme ground is exactly the defect a lenient parser would swallow.
    """
    s = (s or "").strip()
    if s.startswith("#"):
        h = s[1:]
        if len(h) == 3:
            h = "".join(c * 2 for c in h)
        if len(h) != 6:
            raise ValueError("unparseable hex colour %r" % s)
        return (int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16), 1.0)
    if s.startswith("rgb"):
        inner = s[s.index("(") + 1:s.rindex(")")]
        parts = [p.strip() for p in inner.replace("/", ",").split(",") if p.strip()]
        if len(parts) not in (3, 4):
            raise ValueError("unparseable rgb colour %r" % s)
        r, g, b = (int(round(float(p))) for p in parts[:3])
        a = float(parts[3]) if len(parts) == 4 else 1.0
        return (r, g, b, a)
    raise ValueError("unparseable colour %r" % s)


def hexof(c):
    return "#%02X%02X%02X" % (c[0], c[1], c[2])


def _linear(channel):
    """sRGB companding, inverted. WCAG 2.1 relative-luminance definition."""
    c = channel / 255.0
    if c <= 0.04045:
        return c / 12.92
    return ((c + 0.055) / 1.055) ** 2.4


def luminance(c):
    """WCAG 2.1 relative luminance of an opaque sRGB colour."""
    return (0.2126 * _linear(c[0])
            + 0.7152 * _linear(c[1])
            + 0.0722 * _linear(c[2]))


def contrast(fg, bg):
    """WCAG 2.1 contrast ratio. 1.0 (identical) to 21.0 (black on white)."""
    a, b = luminance(fg), luminance(bg)
    lo, hi = (a, b) if a < b else (b, a)
    return (hi + 0.05) / (lo + 0.05)


# ══════════════════════════════════════════════════════════════════════════
# reading the page
# ══════════════════════════════════════════════════════════════════════════

# One eval per case. Every selector reports its COUNT as well as its values,
# because a selector that matches nothing must be a failure and not an empty
# pass — "the docket was identical on all seven themes" is a lie if there was
# no docket on any of them.
_MEASURE = r"""
(function(){
  function one(sel){
    var ns = document.querySelectorAll(sel);
    if (ns.length !== 1) return {n: ns.length};
    var n = ns[0], cs = getComputedStyle(n);
    return {n: 1, bg: cs.backgroundColor, color: cs.color,
            ink:   (cs.getPropertyValue('--b-ink')   || '').trim(),
            muted: (cs.getPropertyValue('--b-muted') || '').trim(),
            ember: (cs.getPropertyValue('--b-ember') || '').trim(),
            ground:(cs.getPropertyValue('--b-ground')|| '').trim()};
  }
  // Every TEXT-BEARING LEAF inside the bench, with the ground actually
  // painted behind it. A leaf is an element with no element children and some
  // non-whitespace text — so a wrapper `<div>` is not measured twice through
  // its own children, and a spacer `<span>` with nothing in it is not measured
  // at all.
  //
  // `ground` walks OUTWARD FROM THE ELEMENT ITSELF, not from its parent: a
  // chip that paints its own background is the ground its own text sits on,
  // and starting at the parent would measure that text against the card
  // behind the chip. The whole opaque stack is returned rather than just the
  // first hit, so the Python side can say so when the nearest ground is
  // semi-transparent instead of silently treating it as opaque.
  function leaves(root){
    var out = [];
    if (!root) return out;
    root.querySelectorAll('*').forEach(function(el){
      if (el.children.length) return;
      var t = (el.textContent || '').trim();
      if (!t) return;
      var stack = [], p = el;
      while (p) {
        var bg = getComputedStyle(p).backgroundColor;
        if (bg && !/rgba\(0,\s*0,\s*0,\s*0\)/.test(bg)) stack.push(bg);
        p = p.parentElement;
      }
      out.push({text: t.replace(/\s+/g, ' '),
                color: getComputedStyle(el).color,
                stack: stack});
    });
    return out;
  }
  // ── page chrome ────────────────────────────────────────────────────
  // Everything OUTSIDE the themed surfaces. `near` requires an opaque paint:
  // `rgba(0,0,0,0)` parses as three zeroes and is not a black background, and
  // reading it as one reports every transparent wrapper on the page.
  function nearBlack(s){
    var m = /^rgba?\((\d+),\s*(\d+),\s*(\d+)(?:,\s*([\d.]+))?\)$/.exec(s||'');
    if (!m) return false;
    if (m[4] != null && +m[4] < 0.5) return false;
    return +m[1] < 70 && +m[2] < 70 && +m[3] < 70;
  }
  function chrome(){
    var out = [];
    document.querySelectorAll('*').forEach(function(el){
      if (el.closest('[data-bench-surface]')) return;
      if (el.closest('[data-bench-docket]')) return;
      var r = el.getBoundingClientRect();
      if (!r.width || !r.height) return;
      var bg = getComputedStyle(el).backgroundColor;
      if (!nearBlack(bg)) return;
      out.push({tpl: el.getAttribute('data-dc-tpl') || '', bg: bg,
                text: (el.textContent || '').trim()
                        .replace(/\s+/g, ' ').slice(0, 30)});
    });
    return out;
  }
  // The espresso marks. The two dots carry the attribute `SET_ATTR` gives
  // them; the week-tile segments are found by the declaration the LOGIC
  // ruling wrote, so no `data-dc-tpl` index is baked into this gate.
  function marks(){
    var out = [];
    document.querySelectorAll('[data-page-strong]').forEach(function(el){
      out.push({kind: el.getAttribute('data-page-strong'),
                bg: getComputedStyle(el).backgroundColor});
    });
    document.querySelectorAll('[style*="var(--pg-strong)"]').forEach(
      function(el){
        if (el.hasAttribute('data-page-strong')) return;
        out.push({kind: 'tile-seg', bg: getComputedStyle(el).backgroundColor});
      });
    return out;
  }
  return JSON.stringify({
    bench:  one('[data-bench-surface="bench"]'),
    board:  one('[data-bench-surface="board"]'),
    docket: one('[data-bench-docket]'),
    avatar: one('[data-bench-avatar]'),
    text:   leaves(document.querySelector('[data-bench-surface="bench"]')),
    marks:  marks(),
    chrome: chrome(),
    pgStrong: (getComputedStyle(document.documentElement)
                 .getPropertyValue('--pg-strong') || '').trim(),
    pageGround: getComputedStyle(document.body).backgroundColor,
    theme:  document.documentElement.getAttribute('data-bench-theme')
  });
})()
"""

# ── ⊕ 23 Aug 2026 — driving the picker ───────────────────────────────────
#
# One eval per press, and each returns the WHOLE reading, so a case is a
# self-contained record: what was pressed, what the attribute says, what the
# bench is painted, and what all six swatches look like at that moment. The
# alternative — press, then measure in a second call — cannot tell a swatch
# that never ticked from a reading taken too early.
_OPEN_SHEET = r"""(function(){
  var r = document.querySelector('.rd[data-mode="ks3"]');
  if (!r) return 'no design root';
  if (r.querySelector('[data-port-region="account-sheet"]')) return 'already';
  var hit = null;
  r.querySelectorAll('button,a').forEach(function(e){
    if (!hit && (e.innerText||'').replace(/\s+/g,' ').trim() === 'Settings') hit = e;
  });
  if (!hit) return 'no Settings control';
  hit.click();
  return 'ok';
})()"""

_PRESS_SWATCH = """(function(label){
  var r = document.querySelector('.rd[data-mode="ks3"]');
  var sheet = r && r.querySelector('[data-port-region="account-sheet"]');
  if (!sheet) return 'no sheet';
  var hit = null;
  sheet.querySelectorAll('.sw').forEach(function(e){
    if ((e.textContent||'').trim() === label) hit = e;
  });
  if (!hit) return 'no swatch';
  hit.click();
  return 'ok';
})(%s)"""

_PICKER = r"""
(function(){
  var r = document.querySelector('.rd[data-mode="ks3"]');
  if (!r) return JSON.stringify({error:'no design root'});
  var sheet = r.querySelector('[data-port-region="account-sheet"]');
  if (!sheet) return JSON.stringify({open:false});
  // The opaque stack behind an element, starting at the element itself — the
  // same rule `leaves()` above uses, and for the same reason: a chip that
  // paints its own ground is the ground its own ink sits on.
  function stack(el){
    var out = [], p = el;
    while (p) {
      var bg = getComputedStyle(p).backgroundColor;
      if (bg && !/rgba\(0,\s*0,\s*0,\s*0\)/.test(bg)) out.push(bg);
      p = p.parentElement;
    }
    return out;
  }
  var sw = [].map.call(sheet.querySelectorAll('.sw'), function(e){
    var chip = e.firstElementChild, label = e.lastElementChild,
        tick = e.querySelector('.swtick');
    return {
      label: (label ? label.textContent : '').trim(),
      on: e.getAttribute('data-on'),
      outline: getComputedStyle(e).outlineStyle,
      chip: chip ? getComputedStyle(chip).backgroundColor : null,
      labelColor: label ? getComputedStyle(label).color : null,
      labelStack: label ? stack(label) : [],
      tickOpacity: tick ? getComputedStyle(tick).opacity : null,
      tickBg: tick ? getComputedStyle(tick).backgroundColor : null,
      tickInk: tick ? getComputedStyle(tick).color : null
    };
  });
  var bench = r.querySelector('[data-bench-surface="bench"]');
  var board = r.querySelector('[data-bench-surface="board"]');
  return JSON.stringify({
    open: true, sw: sw,
    attr: document.documentElement.getAttribute('data-bench-theme'),
    bench: bench ? getComputedStyle(bench).backgroundColor : null,
    board: board ? getComputedStyle(board).backgroundColor : null
  });
})()
"""

_SET = ("(function(t){var e=document.documentElement;"
        "if(t===null){e.removeAttribute('data-bench-theme');}"
        "else{e.setAttribute('data-bench-theme',t);}return 1;})(%s)")

_INJECT = ("(function(css){var s=document.getElementById('__mrb_theme_proof');"
           "if(!s){s=document.createElement('style');"
           "s.id='__mrb_theme_proof';document.head.appendChild(s);}"
           "s.textContent=css;return 1;})(%s)")

_UNINJECT = ("(function(){var s=document.getElementById('__mrb_theme_proof');"
             "if(s)s.parentNode.removeChild(s);return 1;})()")


def _measure(page):
    import json
    return json.loads(page.eval(_MEASURE))


def _select(page, theme):
    import json
    page.eval(_SET % ("null" if theme is None else json.dumps(theme)))
    time.sleep(0.35)


def label_of(case):
    return "attribute ABSENT" if case is None else case


# ══════════════════════════════════════════════════════════════════════════
# the assertions — pure functions over a measurement, so the self-proof can
# run the SAME code against a deliberately broken reading
# ══════════════════════════════════════════════════════════════════════════

def check_surfaces(case, m):
    """1 + 2 — bench and board both painted the theme's ground."""
    name = case or DEFAULT_THEME
    want = BY_NAME[name][1]
    disp = label_of(case)
    rows, problems = [], []
    for key, human in (("bench", "the bench"),
                       ("board", "the leaderboard card")):
        got = m[key]
        if got.get("n") != 1:
            rows.append((disp, "%s ground" % human, "FAIL",
                         "%d element(s) matched" % got.get("n", 0)))
            problems.append(
                "%s — [data-bench-surface=\"%s\"] matched %d elements, not 1. "
                "The gate cannot measure a surface that is not on the page: "
                "restore the attribute in Design's delivery under "
                "docs/ks3/design-reference/student/ and rebuild with "
                "python3 build_all.py."
                % (disp, "bench" if key == "bench" else "board",
                   got.get("n", 0)))
            continue
        c = parse_colour(got["bg"])
        if c[3] != 1.0:
            rows.append((disp, "%s ground" % human, "FAIL",
                         "not opaque: %s" % got["bg"]))
            problems.append(
                "%s — %s is painted %s, which is not opaque. A themed surface "
                "must carry its own ground or the contrast figures below are "
                "measuring the wrong backdrop. Set background to "
                "var(--b-ground) on that element." % (disp, human, got["bg"]))
            continue
        if hexof(c) != want:
            rows.append((disp, "%s ground" % human, "FAIL",
                         "%s, wanted %s" % (hexof(c), want)))
            problems.append(
                "%s — %s is painted %s but the theme's ground is %s. Design's "
                "ruling is that the leaderboard card and its week chips take "
                "the bench theme so the whole page moves together; point that "
                "element's background at var(--b-ground)."
                % (disp, human, hexof(c), want))
        else:
            rows.append((disp, "%s ground" % human, "PASS", want))
    return rows, problems


def check_tokens(case, m):
    """3 — the resolved token trio on the bench equals Design's table."""
    name = case or DEFAULT_THEME
    _n, _ground, want_ink, _ir, want_muted, _mr, want_ember, _er = BY_NAME[name]
    disp = label_of(case)
    rows, problems = [], []
    b = m["bench"]
    if b.get("n") != 1:
        return rows, problems   # already reported by check_surfaces
    for tok, want in (("ink", want_ink), ("muted", want_muted),
                      ("ember", want_ember)):
        raw = b.get(tok) or ""
        try:
            got = hexof(parse_colour(raw))
        except ValueError:
            rows.append((disp, "--b-%s" % tok, "FAIL", "unreadable %r" % raw))
            problems.append(
                "%s — --b-%s resolved to %r, which is not a colour. The theme "
                "block for this theme is missing that token; add it to the "
                "[data-bench-theme=\"%s\"] rule in Design's delivery."
                % (disp, tok, raw, name))
            continue
        if got != want:
            rows.append((disp, "--b-%s" % tok, "FAIL",
                         "%s, wanted %s" % (got, want)))
            problems.append(
                "%s — --b-%s is %s but Design's table says %s. Either the "
                "theme block drifted or the README did; reconcile the two "
                "before shipping, because every contrast figure on this theme "
                "is computed from this value." % (disp, tok, got, want))
        else:
            rows.append((disp, "--b-%s" % tok, "PASS", want))
    return rows, problems


def check_contrast(case, m):
    """4 — ink/muted/ember on ground, each at or above the AA floor.

    Returns (rows, problems, figures) where `figures` is
    [(theme, token, measured, stated)] for the comparison table.
    """
    name = case or DEFAULT_THEME
    t = BY_NAME[name]
    stated = {"ink": t[3], "muted": t[5], "ember": t[7]}
    disp = label_of(case)
    rows, problems, figures = [], [], []
    b = m["bench"]
    if b.get("n") != 1:
        return rows, problems, figures
    try:
        ground = parse_colour(b.get("ground") or "")
    except ValueError:
        rows.append((disp, "contrast on ground", "FAIL", "no --b-ground"))
        problems.append(
            "%s — --b-ground did not resolve to a colour, so no contrast "
            "figure on this theme could be computed. Add the token to the "
            "theme block." % disp)
        return rows, problems, figures

    got = []
    for tok in ("ink", "muted", "ember"):
        try:
            fg = parse_colour(b.get(tok) or "")
        except ValueError:
            continue     # already reported by check_tokens
        r = contrast(fg, ground)
        got.append((tok, r))
        figures.append((name, tok, r, stated[tok]))
        if r < AA:
            problems.append(
                "%s — %s on the theme ground measures %.2f:1, below the AA "
                "floor of %.1f. Design's README claims %.2f for this pair. "
                "This token carries small text on this theme, so it must be "
                "darkened (or the ground lightened) in the "
                "[data-bench-theme=\"%s\"] block until it clears %.1f — do "
                "not lower the floor."
                % (disp, tok, r, AA, stated[tok], name, AA))
    if not got:
        return rows, problems, figures
    worst = min(r for _tok, r in got)
    detail = " · ".join("%s %.2f" % (tok, r) for tok, r in got)
    rows.append((disp, "contrast on ground (AA floor %.1f)" % AA,
                 "PASS" if worst >= AA else "FAIL", detail))
    return rows, problems, figures


def check_bench_text(case, m):
    """7 — every rendered word on the bench clears AA against its real ground.

    The assertion the token figures above could not make. See
    `BENCH_TEXT_EXCEPTIONS` for the one registered exception and why it is
    asserted in both directions rather than merely skipped.
    """
    disp = label_of(case)
    rows, problems = [], []
    b = m["bench"]
    if b.get("n") != 1:
        return rows, problems      # already reported by check_surfaces
    leaves = m.get("text") or []
    if not leaves:
        rows.append((disp, "every bench word clears AA", "FAIL",
                     "no text found inside the bench"))
        problems.append(
            "%s — the sweep found NO text-bearing element inside "
            "[data-bench-surface=\"bench\"]. A sweep over nothing passes "
            "everything, so this is a failure and not an empty pass: either "
            "the bench rendered empty or the walk is pointed at the wrong "
            "node. Check the page mounted before re-reading any row above."
            % disp)
        return rows, problems

    # Each exception may be spent at most once per case, so a second string at
    # the same colours cannot hide behind the first one's registration.
    unspent = list(BENCH_TEXT_EXCEPTIONS)
    hit = {}
    worst, worst_of, measured = None, None, 0

    for leaf in leaves:
        stack = leaf.get("stack") or []
        if not stack:
            problems.append(
                "%s — %r inside the bench has NO painted ground anywhere in "
                "its ancestry, so there is nothing to measure its colour "
                "against. The bench must carry an opaque ground; see "
                "check_surfaces." % (disp, leaf["text"][:60]))
            continue
        ground = parse_colour(stack[0])
        if ground[3] != 1.0:
            rows.append((disp, "every bench word clears AA", "FAIL",
                         "ground %s is not opaque" % stack[0]))
            problems.append(
                "%s — the nearest painted ground behind %r is %s, which is "
                "not opaque, so its contrast cannot be computed without "
                "guessing what shows through. This gate does not guess: give "
                "that element an opaque background, or paint the text against "
                "one." % (disp, leaf["text"][:60], stack[0]))
            continue
        fg = parse_colour(leaf["color"])
        if fg[3] != 1.0:
            # Same refusal to guess as the ground case above, in the other
            # direction: text at 60% opacity is not the colour it names, and
            # compositing it here would invent a figure and then assert on it.
            rows.append((disp, "every bench word clears AA", "FAIL",
                         "text colour %s is not opaque" % leaf["color"]))
            problems.append(
                "%s — %r is painted %s, which is not opaque, so the ratio it "
                "actually delivers depends on what shows through and cannot "
                "be computed from the colour alone. Give that text an opaque "
                "colour — on a themed surface it should be taking a --b-* "
                "token anyway." % (disp, leaf["text"][:60], leaf["color"]))
            continue
        r = contrast(fg, ground)

        exc = None
        for e in unspent:
            if (leaf["text"] == e["text"]
                    and hexof(fg) == e["fg"] and hexof(ground) == e["bg"]):
                exc = e
                break
        if exc is not None:
            unspent.remove(exc)
            hit[exc["name"]] = r
            continue

        measured += 1
        if worst is None or r < worst:
            worst, worst_of = r, leaf

    if worst is not None and worst < AA:
        rows.append((disp, "every bench word clears AA", "FAIL",
                     "%.2f — %s" % (worst, worst_of["text"][:44])))
        problems.append(
            "%s — the bench renders %r at %s on %s, which measures %.2f:1, "
            "below the AA floor of %.1f. This is text a student is being "
            "asked to read on the theme they chose. Find the token it is "
            "painted in and map it onto the theme family in _THEME_BRIDGE "
            "(build_student_port.py) the way the other ten are mapped — do "
            "NOT lower the floor and do NOT register it as an exception "
            "unless it is genuinely theme-independent and pre-existing."
            % (disp, worst_of["text"][:60], hexof(parse_colour(worst_of["color"])),
               hexof(parse_colour(worst_of["stack"][0])), worst, AA))
    elif worst is not None:
        rows.append((disp, "every bench word clears AA (%d words)" % measured,
                     "PASS", "worst %.2f" % worst))

    # ── the registered exceptions, asserted the OTHER way ────────────────
    for e in BENCH_TEXT_EXCEPTIONS:
        got = hit.get(e["name"])
        if got is None:
            rows.append((disp, "exception: %s" % e["name"], "FAIL",
                         "no longer present as registered"))
            problems.append(
                "%s — the registered exception %s (%r at %s on %s, %.2f:1) "
                "was NOT found on the page as registered. Either it was "
                "fixed, restyled or removed. This is a STALE REGISTRATION, "
                "not a rendering fault: if the string now clears %.1f, delete "
                "its entry from BENCH_TEXT_EXCEPTIONS in student_themes.py so "
                "the floor covers it again. An exemption nobody revisits is "
                "how a gate quietly loses a row."
                % (disp, e["name"], e["text"][:40], e["fg"], e["bg"],
                   e["ratio"], AA))
            continue
        if abs(got - e["ratio"]) > e["tol"]:
            rows.append((disp, "exception: %s" % e["name"], "FAIL",
                         "%.2f, registered %.2f" % (got, e["ratio"])))
            problems.append(
                "%s — the registered exception %s now measures %.2f:1 where "
                "it is registered at %.2f (tolerance %.2f). Its colours still "
                "match but its contrast has moved, so the registration no "
                "longer describes it. Re-measure and update the entry — or "
                "delete it, if it now clears %.1f."
                % (disp, e["name"], got, e["ratio"], e["tol"], AA))
        else:
            rows.append((disp, "exception: %s" % e["name"], "NOTE",
                         "%.2f, still as registered (%.2f)" % (got, e["ratio"])))
    return rows, problems


def check_docket(case, m, baseline):
    """5 — the docket is paper and ink on EVERY theme.

    Design's ruling, README section "ACCENT BEHAVIOUR ON A THEME": *the docket
    stays paper #FFFCF5 + ink on every theme: the marking moment is
    deliberately theme-independent, so nothing competes with it.* So this is
    not "the docket is legible" — it is "the docket does not move". `baseline`
    is the pair captured in the ABSENT case; every other case must match it
    EXACTLY, byte for byte on the computed string.
    """
    disp = label_of(case)
    rows, problems = [], []
    d = m["docket"]
    if d.get("n") != 1:
        rows.append((disp, "docket stays paper and ink", "FAIL",
                     "%d element(s) matched" % d.get("n", 0)))
        problems.append(
            "%s — [data-bench-docket] matched %d elements, not 1. The docket "
            "is the marking moment and this gate's theme-independence ruling "
            "has nothing to hold; restore the attribute in Design's delivery "
            "and rebuild." % (disp, d.get("n", 0)))
        return rows, problems
    pair = (d["bg"], d["color"])
    if baseline is not None and pair != baseline:
        rows.append((disp, "docket stays paper and ink", "FAIL",
                     "%s/%s, wanted %s/%s"
                     % (pair[0], pair[1], baseline[0], baseline[1])))
        problems.append(
            "%s — the docket is painted %s on %s where every other theme "
            "paints it %s on %s. Design ruled the docket theme-independent so "
            "that nothing competes with the marking moment; the leak is a "
            "theme token reaching it. The guard is the "
            "`[data-bench-docket]{--st-paper:var(--st-docket-paper)}` rule — "
            "check it still wins over whatever now sets the docket's "
            "background." % (disp, pair[1], pair[0], baseline[1], baseline[0]))
    else:
        rows.append((disp, "docket stays paper and ink", "PASS",
                     "%s on %s" % (pair[1], pair[0])))

    # …and it must be READABLE, which "identical everywhere" alone does not
    # promise: a docket rendered paper-on-paper is identical on all seven.
    try:
        fg, bg = parse_colour(d["color"]), parse_colour(d["bg"])
    except ValueError:
        return rows, problems
    r = contrast(fg, bg)
    if r < AA:
        rows.append((disp, "docket ink on its paper", "FAIL", "%.2f" % r))
        problems.append(
            "%s — the docket's ink measures %.2f:1 on its own paper, below "
            "the AA floor of %.1f. This is the surface a student reads their "
            "mark off; darken --st-ink or lighten --st-docket-paper."
            % (disp, r, AA))
    else:
        rows.append((disp, "docket ink on its paper", "PASS", "%.2f" % r))
    return rows, problems


def check_page_chrome(case, m):
    """7 — the espresso page chrome, and it does NOT take the theme.

    ⊕ 23 Aug 2026 — PHASE 1a. Three assertions, and the middle one is the one
    with a defect behind it:

      a  `--pg-strong` on `:root` is the fixed hex #4A3728 on every case. Page
         chrome routed through a THEME token would put `--b-ground` on the
         cream page — about 1.1:1 on chalk — and the page would look right on
         the five dark themes while a student on the light one saw nothing.
      b  every mark the rule paints measures that hex, at the expected COUNT
         per kind. A count is asserted because the rule needs `!important` to
         beat Design's inline `background:var(--st-ink)`, and a rule that
         parses, matches and LOSES leaves a page that looks exactly as if the
         rule were absent — which is precisely how the avatar inversion
         shipped broken once already.
      c  no OTHER near-black background survives outside the themed surfaces,
         except the two registered in `PAGE_CHROME_EXCEPTIONS`, each of which
         must still be found at its registered colour.

    The contrast figure is reported rather than gated at AA: these are graphic
    marks, not text, and 10.20:1 on the cream ground is well clear either way.
    It is pinned to a tolerance (`PAGE_STRONG_TOL`) so that a drift in
    Design's token shows up as a disagreement instead of as a silent
    re-baselining.
    """
    disp = label_of(case)
    rows, problems = [], []

    got = (m.get("pgStrong") or "").upper()
    if got != PAGE_STRONG:
        rows.append((disp, "--pg-strong is fixed, not themed", "FAIL",
                     "%s, wanted %s" % (got or "(undeclared)", PAGE_STRONG)))
        problems.append(
            "%s — :root reports --pg-strong=%r, not %s. Espresso is a PAGE "
            "token and must be the same on all seven cases; a value that "
            "moves with the theme is the cream-ground defect the term spine's "
            "`numColor` note records refusing."
            % (disp, got or "(undeclared)", PAGE_STRONG))
    else:
        rows.append((disp, "--pg-strong is fixed, not themed", "PASS", got))

    marks = m.get("marks") or []
    seen = {}
    wrong = []
    for mk in marks:
        seen[mk["kind"]] = seen.get(mk["kind"], 0) + 1
        try:
            if hexof(parse_colour(mk["bg"])) != PAGE_STRONG:
                wrong.append((mk["kind"], mk["bg"]))
        except ValueError:
            wrong.append((mk["kind"], mk["bg"]))
    for kind, want in sorted(PAGE_STRONG_MARKS.items()):
        n = seen.get(kind, 0)
        if n != want:
            rows.append((disp, "espresso mark · %s" % kind, "FAIL",
                         "%d found, wanted %d" % (n, want)))
            problems.append(
                "%s — %d %r mark(s) on the page, not %d. Either the ruling "
                "stopped matching Design's node or the fixture's data "
                "changed; both are findings, and an espresso rule painting "
                "nothing passes silently unless the count is asserted."
                % (disp, n, kind, want))
        else:
            rows.append((disp, "espresso mark · %s" % kind, "PASS",
                         "%d at %s" % (n, PAGE_STRONG)))
    if wrong:
        rows.append((disp, "espresso marks all measure %s" % PAGE_STRONG,
                     "FAIL", "%d wrong: %s" % (len(wrong), wrong[:3])))
        problems.append(
            "%s — %d mark(s) carrying the page-chrome rule are not painted "
            "%s: %s. The rule needs !important to beat Design's inline "
            "declaration; check _PAGE_STRONG in build_student_port.py still "
            "carries it." % (disp, len(wrong), PAGE_STRONG, wrong[:4]))
    else:
        rows.append((disp, "espresso marks all measure %s" % PAGE_STRONG,
                     "PASS", "%d mark(s)" % len(marks)))
        try:
            r = contrast(parse_colour(PAGE_STRONG), parse_colour(PAGE_GROUND))
            delta = abs(r - PAGE_STRONG_RATIO)
            rows.append((disp, "espresso on the cream page ground",
                         "PASS" if delta <= PAGE_STRONG_TOL else "NOTE",
                         "%.2f:1 (pinned %.2f)" % (r, PAGE_STRONG_RATIO)))
        except ValueError:
            pass

    # c — the sweep, and its registry
    found = m.get("chrome") or []
    reg = {(e["tpl"], e["bg"].upper()): e for e in PAGE_CHROME_EXCEPTIONS}
    hit = set()
    strays = []
    for c in found:
        try:
            key = (c["tpl"], hexof(parse_colour(c["bg"])))
        except ValueError:
            strays.append(c)
            continue
        if key in reg:
            hit.add(key)
        else:
            strays.append(c)
    if strays:
        rows.append((disp, "no unregistered near-black page chrome", "FAIL",
                     "%d: %s" % (len(strays),
                                 [(c["tpl"], c["bg"]) for c in strays[:3]])))
        problems.append(
            "%s — %d near-black background(s) outside the themed surfaces "
            "are not registered: %s. Design's amendment says no page chrome "
            "is near-black any more. Either move it to var(--pg-strong) or "
            "register it in PAGE_CHROME_EXCEPTIONS with a reason."
            % (disp, len(strays),
               [(c["tpl"], c["bg"], c["text"]) for c in strays[:4]]))
    else:
        rows.append((disp, "no unregistered near-black page chrome", "PASS",
                     "%d registered survivor(s)" % len(hit)))
    for key, e in sorted(reg.items()):
        if key in hit:
            rows.append((disp, "registered survivor · %s" % e["name"][:26],
                         "PASS", "still %s at node %s" % (e["bg"], e["tpl"])))
        else:
            rows.append((disp, "registered survivor · %s" % e["name"][:26],
                         "FAIL", "not found"))
            problems.append(
                "%s — the registered near-black exception %r (node %s, %s) is "
                "no longer on the page at that colour. Either the unit that "
                "owns it has landed — in which case DELETE the registration — "
                "or something else moved it. An exception that cannot go "
                "stale is a hole." % (disp, e["name"], e["tpl"], e["bg"]))
    return rows, problems


def check_avatar(case, m):
    """6 — the leader's initials are visible.

    ⚠️ THIS ASSERTION HAS A REAL DEFECT BEHIND IT. Before the
    `[data-bench-avatar]{background:var(--b-ink);color:var(--b-ground)}`
    inversion was added, Chalk rendered the initials as rgb(34,30,27) on
    rgb(34,30,27) — ink on ink, a 1.00:1 disc with the leader's name inside it
    and nothing whatever to see. Every text gate passed: the letters were in
    the DOM. So this checks the two are not the same colour AND that they
    clear AA, and the first clause is not redundant with the second — it is
    what names the failure correctly when it recurs.
    """
    disp = label_of(case)
    rows, problems = [], []
    a = m["avatar"]
    if a.get("n") != 1:
        rows.append((disp, "leader initials legible", "FAIL",
                     "%d element(s) matched" % a.get("n", 0)))
        problems.append(
            "%s — [data-bench-avatar] matched %d elements, not 1. Restore the "
            "attribute in Design's delivery and rebuild; without it the "
            "invert rule has nothing to select and Chalk goes invisible "
            "again." % (disp, a.get("n", 0)))
        return rows, problems
    fg, bg = parse_colour(a["color"]), parse_colour(a["bg"])
    if hexof(fg) == hexof(bg):
        rows.append((disp, "leader initials legible", "FAIL",
                     "ink == ground, %s" % hexof(fg)))
        problems.append(
            "%s — the leader's initials are %s on %s: the same colour, so the "
            "avatar is a blank disc. This is the Chalk defect returning. The "
            "fix is the [data-bench-avatar] invert rule "
            "(background:var(--b-ink); color:var(--b-ground)) — check it is "
            "still emitted and still !important."
            % (disp, hexof(fg), hexof(bg)))
        return rows, problems
    r = contrast(fg, bg)
    if r < AA:
        rows.append((disp, "leader initials legible", "FAIL", "%.2f" % r))
        problems.append(
            "%s — the leader's initials measure %.2f:1 against their disc, "
            "below the AA floor of %.1f. Invert the avatar against this "
            "theme's tokens rather than tinting it." % (disp, r, AA))
    else:
        rows.append((disp, "leader initials legible", "PASS", "%.2f" % r))
    return rows, problems


def check_default(measures):
    """The default did not silently revert.

    Design: "(absent = harbour)", and GRAPHITE is "the old default, opt-in".
    Both halves are asserted, because only the first one is a contract and
    only the second one catches the regression that matters: a build that
    quietly restores the previous `:root` block satisfies "absent resolves to
    SOMETHING" perfectly.
    """
    rows, problems = [], []
    absent = measures[None]["bench"]
    if absent.get("n") != 1:
        return rows, problems
    got = {k: (absent.get(k) or "") for k in ("ground", "ink", "muted", "ember")}
    got = {k: (hexof(parse_colour(v)) if v else "") for k, v in got.items()}

    def tokens_of(name):
        t = BY_NAME[name]
        return {"ground": t[1], "ink": t[2], "muted": t[4], "ember": t[6]}

    want = tokens_of(DEFAULT_THEME)
    old = tokens_of(OLD_DEFAULT)
    if got != want:
        rows.append(("attribute ABSENT", "absent resolves to %s" % DEFAULT_THEME,
                     "FAIL", "ground %s, wanted %s"
                     % (got["ground"], want["ground"])))
        problems.append(
            "the default theme has moved: with no data-bench-theme attribute "
            "the bench resolves to ground %s, but Design's contract is "
            "\"absent = %s\" (%s). Fix the bare :root token block in Design's "
            "delivery — it is the one that defines the default, and no "
            "attribute selector can cover for it."
            % (got["ground"], DEFAULT_THEME, want["ground"]))
    else:
        rows.append(("attribute ABSENT", "absent resolves to %s" % DEFAULT_THEME,
                     "PASS", want["ground"]))
    if got == old:
        rows.append(("attribute ABSENT", "default is NOT the old %s" % OLD_DEFAULT,
                     "FAIL", old["ground"]))
        problems.append(
            "the default has REVERTED to %s (%s), the theme Design demoted to "
            "opt-in. The whole point of the amendment is that page chrome is "
            "no longer near-black by default; restore %s in the bare :root "
            "block." % (OLD_DEFAULT, old["ground"], DEFAULT_THEME))
    else:
        rows.append(("attribute ABSENT", "default is NOT the old %s" % OLD_DEFAULT,
                     "PASS", "%s, not %s" % (got["ground"], old["ground"])))
    return rows, problems


def _drive_picker(page, url):
    """Open the account sheet and press all six swatches. Returns a reading.

    ⚠️ THE PAGE IS RELOADED FIRST, and that is not tidiness. The seven cases
    above move `data-bench-theme` from OUTSIDE the component, which no student
    can do and which leaves the attribute and the component's own `theme`
    state disagreeing. Pressing a swatch from that state would measure a
    situation the product cannot be in. A reload puts both back where a
    student finds them: no attribute, and harbour.
    """
    import json
    out = {"opened": None, "cases": {}, "at_open": None,
           "expect": list(PICKER_ORDER)}
    page.goto(url)
    time.sleep(2.6)
    out["opened"] = page.eval(_OPEN_SHEET)
    time.sleep(0.5)
    out["at_open"] = json.loads(page.eval(_PICKER))
    for name in PICKER_ORDER:
        got = page.eval(_PRESS_SWATCH % json.dumps(name))
        time.sleep(0.45)
        m = json.loads(page.eval(_PICKER))
        m["pressed"] = got
        out["cases"][name] = m
    return out


def check_picker(pk):
    """Six swatches, one tick, the theme it names, and a legible chip.

    Pure over the reading, like every other check here, so the self-proof can
    run the same code against a deliberately broken page.
    """
    rows, problems = [], []
    lbl = "the picker"

    if pk["opened"] != "ok" and pk["opened"] != "already":
        rows.append((lbl, "Settings opens the account sheet", "FAIL",
                     str(pk["opened"])))
        problems.append(
            "the account sheet could not be opened: %r. Six themes exist and "
            "no student can reach five of them, which is the exact state this "
            "half of the gate was written for. Everything below is unmeasured."
            % pk["opened"])
        return rows, problems
    rows.append((lbl, "Settings opens the account sheet", "PASS",
                 "the account-sheet region is on screen"))

    at_open = pk["at_open"]
    if not at_open.get("open"):
        rows.append((lbl, "the sheet renders its picker", "FAIL",
                     "no account-sheet region after the press"))
        problems.append(
            "the account sheet did not render. A grafted subtree whose `if` "
            "reads an undefined name renders NOTHING, silently — check that "
            "`accountOpen` is in renderVals.")
        return rows, problems

    got_labels = [x["label"] for x in at_open["sw"]]
    if got_labels != PICKER_LABELS:
        rows.append((lbl, "six swatches, in Design's order", "FAIL",
                     "%d: %s" % (len(got_labels), got_labels)))
        problems.append(
            "the picker shows %d swatch(es) %s; Design draws six, %s. A "
            "missing swatch is a theme a student cannot choose; a reordered "
            "one is Design's drawing altered without a ruling."
            % (len(got_labels), got_labels, PICKER_LABELS))
    else:
        rows.append((lbl, "six swatches, in Design's order", "PASS",
                     " ".join(PICKER_LABELS)))

    # The swatch preview strip must show the theme it names. This is the one
    # place the page states a theme's colour OUTSIDE the theme's own rules —
    # `--t-clay` and friends — so it is the one place the two can drift apart
    # and leave a student picking a colour they were not shown.
    for x in at_open["sw"]:
        name = x["label"].lower()
        if name not in BY_NAME or not x.get("chip"):
            continue
        want = BY_NAME[name][1]
        got = hexof(parse_colour(x["chip"]))
        if got.lower() != want.lower():
            rows.append((lbl, "the %s swatch shows %s" % (name, want),
                         "FAIL", got))
            problems.append(
                "the %s swatch previews %s and the %s bench is painted %s. "
                "The preview is Design's `--t-%s` and the bench is Design's "
                "`--b-ground` under `[data-bench-theme=\"%s\"]`; they are two "
                "statements of one colour and they have drifted. A student is "
                "being shown one thing and given another."
                % (name, got, name, want, name, name))
        else:
            rows.append((lbl, "the %s swatch shows %s" % (name, want),
                         "PASS", got))

    # The themes this reading actually covers. A FULL run covers all six and
    # says so; the self-proof drives one on purpose, so it names the one it
    # drove rather than being told six are missing.
    expect = pk.get("expect") or PICKER_ORDER
    if [n for n in expect if n in pk["cases"]] != list(expect):
        rows.append((lbl, "every swatch was pressed", "FAIL",
                     "pressed %s of %s" % (sorted(pk["cases"]), list(expect))))
        problems.append(
            "the picker drive reached %s and was asked for %s. A theme that "
            "was never pressed is a theme this run says nothing about."
            % (sorted(pk["cases"]), list(expect)))
    for name in expect:
        m = pk["cases"].get(name) or {}
        key = name.lower()
        if m.get("pressed") != "ok":
            rows.append((lbl, "%s is pressable" % key, "FAIL",
                         str(m.get("pressed"))))
            problems.append(
                "the %s swatch could not be pressed: %r. A swatch that is on "
                "the page and does not respond is a dead control, and the "
                "text-and-controls gate cannot see one."
                % (key, m.get("pressed")))
            continue

        # 1 — the attribute the six CSS rules key on.
        if m.get("attr") != key:
            rows.append((lbl, "%s sets data-bench-theme" % key, "FAIL",
                         "attribute reads %r" % m.get("attr")))
            problems.append(
                "pressing the %s swatch left data-bench-theme=%r. The six "
                "`[data-bench-theme]` rules key on that attribute and nothing "
                "else, so the page is not wearing the theme the student "
                "chose." % (key, m.get("attr")))
        else:
            rows.append((lbl, "%s sets data-bench-theme" % key, "PASS", key))

        # 2 — the bench and the board actually moved. The attribute being
        #     right and the paint being wrong is a rule that did not match.
        want = BY_NAME[key][1]
        for surf in ("bench", "board"):
            if not m.get(surf):
                continue
            got = hexof(parse_colour(m[surf]))
            if got.lower() != want.lower():
                rows.append((lbl, "%s paints the %s" % (key, surf), "FAIL",
                             "%s, wanted %s" % (got, want)))
                problems.append(
                    "pressing %s left the %s painted %s and Design's ground "
                    "for that theme is %s." % (key, surf, got, want))
            else:
                rows.append((lbl, "%s paints the %s" % (key, surf), "PASS",
                             got))

        # 3 — EXACTLY ONE tick, on the swatch that was pressed. Both halves
        #     are the assertion: two ticks is as wrong as none, and a page
        #     with the right theme and the wrong tick is a page lying about
        #     which preference it holds.
        on = [x["label"] for x in m.get("sw", []) if x.get("on") == "1"]
        if on != [name]:
            rows.append((lbl, "%s is the only swatch ticked" % key, "FAIL",
                         "ticked: %s" % (on or "none")))
            problems.append(
                "after pressing %s the swatches marked data-on=\"1\" are %s. "
                "Exactly one may be, and it must be the one pressed — the "
                "tick is the page's statement of which theme is saved."
                % (key, on or "none"))
        else:
            rows.append((lbl, "%s is the only swatch ticked" % key, "PASS",
                         name))

        # 4 — and the tick is VISIBLE. `data-on` is an attribute; the mark a
        #     student sees is `--tick-o`, and a rule that stopped matching
        #     would leave the attribute perfectly correct and the swatch
        #     showing nothing at all.
        lit = [x["label"] for x in m.get("sw", [])
               if x.get("tickOpacity") not in (None, "0")
               and float(x["tickOpacity"]) > 0.5]
        if lit != [name]:
            rows.append((lbl, "%s shows its tick, alone" % key, "FAIL",
                         "lit: %s" % (lit or "none")))
            problems.append(
                "after pressing %s the visible ticks are %s. `data-on` is set "
                "correctly but `.sw[data-on=\"1\"] .swtick{--tick-o:1}` is not "
                "reaching it, so the student sees no confirmation of their "
                "own choice." % (key, lit or "none"))
        else:
            rows.append((lbl, "%s shows its tick, alone" % key, "PASS",
                         "opacity 1"))

        # 5 — LEGIBILITY. The six words a student reads, and the tick they
        #     look for. Measured against the ground each actually sits on
        #     rather than against the one it is assumed to sit on.
        for x in m.get("sw", []):
            gstack = [c for c in (x.get("labelStack") or [])]
            if not x.get("labelColor") or not gstack:
                continue
            ratio = contrast(parse_colour(x["labelColor"]),
                             parse_colour(gstack[0]))
            if ratio + 1e-9 < AA:
                rows.append((lbl, "%s · the %s label reads"
                             % (key, x["label"].lower()), "FAIL",
                             "%.2f:1" % ratio))
                problems.append(
                    "with %s selected, the %s swatch's label measures %.2f:1 "
                    "against its own ground (%s on %s), below AA %.1f."
                    % (key, x["label"].lower(), ratio,
                       hexof(parse_colour(x["labelColor"])),
                       hexof(parse_colour(gstack[0])), AA))
        sel = [x for x in m.get("sw", []) if x.get("label") == name]
        if sel and sel[0].get("tickBg") and sel[0].get("tickInk"):
            ratio = contrast(parse_colour(sel[0]["tickInk"]),
                             parse_colour(sel[0]["tickBg"]))
            if ratio + 1e-9 < NONTEXT_AA:
                rows.append((lbl, "%s · the tick mark reads" % key, "FAIL",
                             "%.2f:1" % ratio))
                problems.append(
                    "the tick inside the %s swatch measures %.2f:1 against "
                    "its own disc, below the %.1f:1 floor for a non-text "
                    "mark. Design gives each swatch its own tick colours; "
                    "this one's pair does not separate." % (key, ratio,
                                                            NONTEXT_AA))
            else:
                rows.append((lbl, "%s · the tick mark reads" % key, "PASS",
                             "%.2f:1" % ratio))
    if not any(v == "FAIL" for _l, _n, v, _d in rows):
        rows.append((lbl, "every label clears AA %.1f" % AA, "PASS",
                     "%d swatch label(s) measured across %d theme(s)"
                     % (len(PICKER_LABELS) * len(expect), len(expect))))
    return rows, problems


# ══════════════════════════════════════════════════════════════════════════
# the self-proof
# ══════════════════════════════════════════════════════════════════════════

def _prove(page, baseline):
    """Break the page on purpose; require the assertions to see it.

    One injection per KIND of check this gate makes, because they fail in
    different ways and a proof of one is not a proof of the other:

      · an EQUALITY check — the docket's theme-independence. Injected: a docket
        painted black.
      · an ARITHMETIC check — a contrast floor. Injected: an ink so close to
        harbour's ground that the ratio collapses to about 1.1:1.
      · the RENDERED-TEXT sweep — injected: the real 1.78:1 bench label.
      · the PAGE-CHROME check, in both halves — injected: the espresso marks
        forced back to near-black (the `!important` failure), and an
        unregistered near-black painted onto a page section.

    Each is injected, re-measured, and required to produce at least one
    problem; then removed, re-measured, and required to produce none. A gate
    that stays quiet through a deliberate violation has proved only that it is
    quiet.
    """
    import json
    rows, problems = [], []
    disp = "the self-proof"

    _select(page, None)

    # (a) the equality check can see a moved docket.
    page.eval(_INJECT % json.dumps(
        "[data-bench-docket]{background:#000 !important}"))
    time.sleep(0.35)
    _r, broke = check_docket(None, _measure(page), baseline)
    page.eval(_UNINJECT)
    time.sleep(0.35)
    _r, clean = check_docket(None, _measure(page), baseline)
    if not broke:
        problems.append(
            "SELF-PROOF FAILED: a docket forcibly painted #000 was NOT caught "
            "by the docket assertion. Every clean docket row in this run is "
            "therefore worthless — a mechanism that cannot see a black docket "
            "on a paper docket cannot see anything. Fix the docket check "
            "before reading any other line of this report.")
        rows.append((disp, "the docket check can see a moved docket", "FAIL",
                     "injected violation went unnoticed"))
    elif clean:
        problems.append(
            "SELF-PROOF FAILED: the docket assertion still reports a problem "
            "after the injected style was removed — %s. The injection did not "
            "come back out cleanly, so nothing after it can be trusted."
            % clean[0][:90])
        rows.append((disp, "the docket check can see a moved docket", "FAIL",
                     "page not clean after the injection was removed"))
    else:
        rows.append((disp, "the docket check can see a moved docket", "PASS",
                     "red while injected, green once removed"))

    # (b) the arithmetic check can see a collapsed ratio. #25404A on harbour's
    # #20363F is about 1.15:1 — legible to no one, and a value a careless
    # palette edit could genuinely produce.
    page.eval(_INJECT % json.dumps(
        '[data-bench-surface="bench"]{--b-ink:#25404A !important}'))
    time.sleep(0.35)
    _r, broke2, _f = check_contrast(None, _measure(page))
    page.eval(_UNINJECT)
    time.sleep(0.35)
    _r, clean2, _f = check_contrast(None, _measure(page))
    if not broke2:
        problems.append(
            "SELF-PROOF FAILED: an ink of #25404A on harbour's #20363F ground "
            "— about 1.15:1, invisible — was NOT caught by the contrast "
            "assertion. Every contrast figure below is therefore unproven: "
            "the arithmetic may be running on the wrong element, or on a "
            "token that no longer resolves. Fix the contrast check first.")
        rows.append((disp, "the contrast check can see a collapsed ratio",
                     "FAIL", "injected low-contrast ink went unnoticed"))
    elif clean2:
        problems.append(
            "SELF-PROOF FAILED: the contrast assertion still reports a "
            "problem after the injected style was removed — %s. The page did "
            "not return to its real palette." % clean2[0][:90])
        rows.append((disp, "the contrast check can see a collapsed ratio",
                     "FAIL", "page not clean after the injection was removed"))
    else:
        rows.append((disp, "the contrast check can see a collapsed ratio",
                     "PASS", "red while injected, green once removed"))

    # (c) the RENDERED-TEXT sweep can see an unreadable label. This is the
    # proof that matters most, because this assertion exists precisely because
    # the other two were green while three bench labels sat at 1.78:1 — a
    # widened gate that cannot demonstrate seeing the defect it was widened for
    # has widened nothing.
    #
    # ⚠️ INJECTED ON `--st-room-text`, THE EXACT TOKEN THAT CAUSED IT, and set
    # to the exact value it was stuck at (#B7AA98) — so this replays the real
    # defect on harbour rather than a synthetic one. On harbour's #20363F that
    # is 5.55:1 and would NOT fail, so the injection also puts the bench on
    # chalk's light ground, which is where the pair collapses to 1.78.
    page.eval(_INJECT % json.dumps(
        '[data-bench-surface="bench"]{--b-ground:#EFE2CB !important;'
        '--st-room-text:#B7AA98 !important}'))
    time.sleep(0.35)
    _r, broke3 = check_bench_text(None, _measure(page))
    page.eval(_UNINJECT)
    time.sleep(0.35)
    _r, clean3 = check_bench_text(None, _measure(page))
    if not broke3:
        problems.append(
            "SELF-PROOF FAILED: the bench checklist forced back to #B7AA98 on "
            "a light #EFE2CB ground — 1.78:1, the exact defect this sweep was "
            "added for — was NOT caught. Every 'every bench word clears AA' "
            "row in this run is worthless: the walk is finding no leaves, or "
            "reading the wrong ground, or the exception list is swallowing "
            "them. Fix the sweep before reading any other line.")
        rows.append((disp, "the text sweep can see an unreadable label",
                     "FAIL", "injected 1.78:1 label went unnoticed"))
    elif clean3:
        problems.append(
            "SELF-PROOF FAILED: the bench text sweep still reports a problem "
            "after the injected style was removed — %s. The page did not "
            "return to its real palette." % clean3[0][:90])
        rows.append((disp, "the text sweep can see an unreadable label",
                     "FAIL", "page not clean after the injection was removed"))
    else:
        rows.append((disp, "the text sweep can see an unreadable label",
                     "PASS", "red while injected, green once removed"))

    # (d) the PAGE-CHROME sweep can see a near-black that is not registered,
    # and it can see an espresso mark that lost its fight with an inline
    # declaration. Two injections, because the check has two halves and each
    # half has its own way of being blind.
    #
    # ⚠️ THE FIRST ONE REPLAYS THE REAL FAILURE MODE OF THIS RULE. `_PAGE_STRONG`
    # only paints because of `!important`: Design's dots carry
    # `background:var(--st-ink)` INLINE, and an inline declaration outranks any
    # selector. Written without the keyword the rule parses, matches, and
    # loses, and the page looks exactly as if the rule were not there — which
    # is how the avatar inversion shipped broken once already. Forcing the
    # marks back to #221E1B is that failure, exactly.
    page.eval(_INJECT % json.dumps(
        "[data-page-strong]{background-color:#221E1B !important}"))
    time.sleep(0.35)
    _r, broke4 = check_page_chrome(None, _measure(page))
    page.eval(_UNINJECT)
    time.sleep(0.35)
    _r, clean4 = check_page_chrome(None, _measure(page))
    if not broke4:
        problems.append(
            "SELF-PROOF FAILED: the espresso marks forced back to near-black "
            "#221E1B were NOT caught. Every page-chrome row in this run is "
            "worthless — the selector is finding nothing, or the hex "
            "comparison is not running. Fix check_page_chrome first.")
        rows.append((disp, "the chrome check can see a lost espresso mark",
                     "FAIL", "injected near-black marks went unnoticed"))
    elif clean4:
        problems.append(
            "SELF-PROOF FAILED: the page-chrome assertion still reports a "
            "problem after the injected style was removed — %s. The page did "
            "not return to its real palette." % clean4[0][:90])
        rows.append((disp, "the chrome check can see a lost espresso mark",
                     "FAIL", "page not clean after the injection was removed"))
    else:
        rows.append((disp, "the chrome check can see a lost espresso mark",
                     "PASS", "red while injected, green once removed"))

    # The second half: an UNREGISTERED near-black on the page ground. The hero
    # is chosen because it is a large page element that no unit owns and that
    # carries no background of its own, so the injection is unambiguous.
    page.eval(_INJECT % json.dumps(
        '[data-dc-tpl="39"]{background-color:#101010 !important}'))
    time.sleep(0.35)
    _r, broke5 = check_page_chrome(None, _measure(page))
    page.eval(_UNINJECT)
    time.sleep(0.35)
    _r, clean5 = check_page_chrome(None, _measure(page))
    if not broke5:
        problems.append(
            "SELF-PROOF FAILED: a page section forcibly painted #101010 on "
            "the cream ground was NOT caught by the near-black sweep. "
            "Design's amendment says no page chrome is near-black any more, "
            "and this run cannot tell whether that is true.")
        rows.append((disp, "the chrome sweep can see a new near-black",
                     "FAIL", "injected near-black went unnoticed"))
    elif clean5:
        problems.append(
            "SELF-PROOF FAILED: the near-black sweep still reports a problem "
            "after the injected style was removed — %s." % clean5[0][:90])
        rows.append((disp, "the chrome sweep can see a new near-black",
                     "FAIL", "page not clean after the injection was removed"))
    else:
        rows.append((disp, "the chrome sweep can see a new near-black",
                     "PASS", "red while injected, green once removed"))
    return rows, problems


def _prove_picker(page, url):
    """⊕ 23 Aug 2026 — PHASE 1b. The picker half, proved the same way.

    ⚑ AND IT NEEDS ITS OWN PROOF FOR A REASON THE OTHERS DO NOT HAVE. Every
    injection above breaks a COLOUR, and the checks above read colours. These
    checks read a state attribute, an opacity and a control response — three
    things a CSS injection cannot reach by accident, and three places where a
    selector that matched nothing would report a clean picker exactly as a
    healthy one does.

    Two injections, one per kind of claim:

      · THE TICK. `.sw[data-on="1"] .swtick{--tick-o:0}` leaves `data-on`
        perfectly correct and takes the mark off the screen. That is precisely
        the failure the tick check exists for, and it is one line away from
        being real: the whole state treatment is two rules in a stylesheet
        grafted out of Design's delivery.
      · THE LABEL. The six words forced to their own card ground, which is
        1.00:1. Design's swatch labels are `--pg-ink` on `--pg-card` today and
        neither is a theme token, so nothing in the six themes can move
        them — which is exactly the kind of "cannot happen" that a gate is
        for.
    """
    import json
    rows, problems = [], []
    disp = "the self-proof"

    def read():
        return json.loads(page.eval(_PICKER))

    # The page is already sitting with the sheet open on harbour, from
    # `_drive_picker`. Re-press one swatch after each injection so the reading
    # is of a real selection rather than of whatever was last on screen.
    page.eval(_INJECT % json.dumps(
        '.sw[data-on="1"] .swtick{--tick-o:0 !important}'))
    time.sleep(0.35)
    page.eval(_PRESS_SWATCH % json.dumps("MOSS"))
    time.sleep(0.45)
    broke = check_picker({"opened": "already", "at_open": read(),
                          "expect": ["MOSS"],
                          "cases": {"MOSS": dict(read(), pressed="ok")}})[1]
    page.eval(_UNINJECT)
    time.sleep(0.35)
    page.eval(_PRESS_SWATCH % json.dumps("MOSS"))
    time.sleep(0.45)
    clean = check_picker({"opened": "already", "at_open": read(),
                          "expect": ["MOSS"],
                          "cases": {"MOSS": dict(read(), pressed="ok")}})[1]
    if not broke:
        problems.append(
            "SELF-PROOF FAILED: the selected swatch's tick was forced to zero "
            "opacity and the picker check did NOT notice. `data-on` was still "
            "right, so every 'the tick moved' row in this run is worthless — "
            "it is asserting an attribute and calling it a mark on a screen.")
        rows.append((disp, "the picker check can see a tick that stopped "
                     "showing", "FAIL", "injected --tick-o:0 went unnoticed"))
    elif clean:
        problems.append(
            "SELF-PROOF FAILED: the picker still reports a problem after the "
            "injected style was removed — %s." % clean[0][:90])
        rows.append((disp, "the picker check can see a tick that stopped "
                     "showing", "FAIL", "not clean after the injection"))
    else:
        rows.append((disp, "the picker check can see a tick that stopped "
                     "showing", "PASS", "red while injected, green once "
                     "removed"))

    page.eval(_INJECT % json.dumps(
        ".sw > span:last-child{color:var(--pg-card) !important}"))
    time.sleep(0.35)
    page.eval(_PRESS_SWATCH % json.dumps("CLAY"))
    time.sleep(0.45)
    broke2 = check_picker({"opened": "already", "at_open": read(),
                           "expect": ["CLAY"],
                           "cases": {"CLAY": dict(read(), pressed="ok")}})[1]
    page.eval(_UNINJECT)
    time.sleep(0.35)
    page.eval(_PRESS_SWATCH % json.dumps("HARBOUR"))
    time.sleep(0.45)
    clean2 = check_picker({"opened": "already", "at_open": read(),
                           "expect": ["HARBOUR"],
                           "cases": {"HARBOUR": dict(read(), pressed="ok")}})[1]
    if not broke2:
        problems.append(
            "SELF-PROOF FAILED: the six swatch labels were painted their own "
            "card ground — 1.00:1, invisible — and the legibility sweep did "
            "not see it. It is measuring something other than what a student "
            "reads.")
        rows.append((disp, "the picker check can see an unreadable swatch "
                     "label", "FAIL", "injected 1.00:1 label went unnoticed"))
    elif clean2:
        problems.append(
            "SELF-PROOF FAILED: the picker still reports a problem after the "
            "label injection was removed — %s." % clean2[0][:90])
        rows.append((disp, "the picker check can see an unreadable swatch "
                     "label", "FAIL", "not clean after the injection"))
    else:
        rows.append((disp, "the picker check can see an unreadable swatch "
                     "label", "PASS", "red while injected, green once "
                     "removed"))
    return rows, problems


# ══════════════════════════════════════════════════════════════════════════
# the run
# ══════════════════════════════════════════════════════════════════════════

def run(cdp):
    rows, problems, figures = [], [], []
    server, port = cdp.serve(SITE)
    url = "http://127.0.0.1:%d/%s" % (port, PAGE)
    measures = {}
    try:
        with cdp.Browser() as b:
            page = b.attach()
            page.set_viewport(*VIEWPORT)
            page.goto(url)
            time.sleep(2.6)

            # The ABSENT case first — it supplies the docket baseline that the
            # other six are held to, and it is the case the self-proof breaks.
            for case in CASES:
                _select(page, case)
                m = _measure(page)
                if case is not None and m.get("theme") != case:
                    problems.append(
                        "the page root reports data-bench-theme=%r after it "
                        "was set to %r. Something is rewriting the attribute; "
                        "no reading in this run is reliable."
                        % (m.get("theme"), case))
                measures[case] = m

            baseline = None
            d0 = measures[None]["docket"]
            if d0.get("n") == 1:
                baseline = (d0["bg"], d0["color"])

            # ⚠️ THE SELF-PROOF RUNS BEFORE ANYTHING IS REPORTED, the same
            # ordering `student_behaviour.run` uses, so a machinery that
            # cannot see never gets as far as reporting clean.
            prows, pproblems = _prove(page, baseline)
            rows.extend(prows)
            problems.extend(pproblems)

            # ⊕ 23 Aug 2026 — PHASE 1b. THE PICKER, PRESSED.
            #
            # Last, and from a fresh load. Everything above drives the theme
            # from outside the component; this is the only part of the file
            # that does what a student does. It reloads first — see
            # `_drive_picker` — so it starts from the state a student finds.
            pk = _drive_picker(page, url)
            r, p_ = check_picker(pk)
            rows.extend(r)
            problems.extend(p_)
            r, p_ = _prove_picker(page, url)
            rows.extend(r)
            problems.extend(p_)
    finally:
        server.shutdown()

    drows, dproblems = check_default(measures)
    rows.extend(drows)
    problems.extend(dproblems)

    for case in CASES:
        m = measures[case]
        for fn in (check_surfaces, check_tokens):
            r, p = fn(case, m)
            rows.extend(r)
            problems.extend(p)
        r, p, f = check_contrast(case, m)
        rows.extend(r)
        problems.extend(p)
        figures.extend(f)
        r, p = check_docket(case, m, baseline)
        rows.extend(r)
        problems.extend(p)
        r, p = check_avatar(case, m)
        rows.extend(r)
        problems.extend(p)
        r, p = check_bench_text(case, m)
        rows.extend(r)
        problems.extend(p)
        # ⊕ 23 Aug 2026 — PHASE 1a. The page the bench sits on.
        r, p = check_page_chrome(case, m)
        rows.extend(r)
        problems.extend(p)

    # The 18 — six named themes × three tokens — measured against Design's own
    # stated arithmetic. NOT a gate: a row here says the README is out, and the
    # README is a claim this file checks rather than a thing it enforces.
    seen = set()
    for name, tok, got, stated in figures:
        if (name, tok) in seen:
            continue
        seen.add((name, tok))
        delta = abs(got - stated)
        rows.append(("Design's stated figures, measured",
                     "%s · %s on ground" % (name, tok),
                     "NOTE" if delta > STATED_TOL else "PASS",
                     "measured %.2f · README %.2f · Δ %.2f"
                     % (got, stated, delta)))
    return rows, problems


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    sys.path.insert(0, here)
    os.chdir(here)

    fixture = os.path.join(SITE, PAGE)
    if not os.path.exists(fixture):
        print("── the ported student page's colour, measured ──")
        print("\n  1 PROBLEM(S):")
        print("    · %s does not exist, so there is nothing to measure. Run "
              "python3 build_all.py to write it, then re-run this gate."
              % fixture)
        return 1

    import ks3_browser as cdp

    print("── the ported student page's colour, measured ──")
    rows, problems = run(cdp)
    last = None
    for page, label, verdict, detail in rows:
        if page != last:
            print("\n  %s" % page)
            last = page
        print("    %-4s %-42s %s" % (verdict, label[:42], detail[:80]))

    print()
    if problems:
        print("  %d PROBLEM(S):" % len(problems))
        for p in problems:
            print("    · %s" % p)
        return 1
    print("  PASS  seven cases (six themes and the attribute absent); bench "
          "and leaderboard both take the theme ground, every token matches "
          "Design's table, all %d contrast figures clear AA %.1f, the docket "
          "is identical on all seven, the avatar is legible on each, and "
          "every rendered word inside the bench clears AA %.1f against its "
          "own painted ground on all seven — with %d registered exception(s), "
          "each asserted still present at its registered colours and ratio."
          % (len(CASES) * 3, AA, AA, len(BENCH_TEXT_EXCEPTIONS)))
    print("        And the PICKER a student uses to choose one: Settings "
          "opens Design's account sheet, six swatches in Design's order, "
          "each previewing the ground its theme paints; every one pressed, "
          "each setting data-bench-theme, painting the bench and the "
          "leaderboard card, and leaving exactly one tick — its own — "
          "visible. Every swatch label clears AA %.1f and every tick clears "
          "%.1f:1 as a non-text mark." % (AA, NONTEXT_AA))
    print("        And the PAGE the bench sits on: --pg-strong fixed at %s "
          "on all seven, %d espresso mark(s) measuring it, %.2f:1 on the "
          "cream ground, and no near-black page chrome outside the %d "
          "registered survivor(s) — each asserted still present."
          % (PAGE_STRONG, sum(PAGE_STRONG_MARKS.values()),
             PAGE_STRONG_RATIO, len(PAGE_CHROME_EXCEPTIONS)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
