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
  return JSON.stringify({
    bench:  one('[data-bench-surface="bench"]'),
    board:  one('[data-bench-surface="board"]'),
    docket: one('[data-bench-docket]'),
    avatar: one('[data-bench-avatar]'),
    text:   leaves(document.querySelector('[data-bench-surface="bench"]')),
    theme:  document.documentElement.getAttribute('data-bench-theme')
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


# ══════════════════════════════════════════════════════════════════════════
# the self-proof
# ══════════════════════════════════════════════════════════════════════════

def _prove(page, baseline):
    """Break the page on purpose; require the assertions to see it.

    Two injections, one per KIND of check this gate makes, because they fail in
    different ways and a proof of one is not a proof of the other:

      · an EQUALITY check — the docket's theme-independence. Injected: a docket
        painted black.
      · an ARITHMETIC check — a contrast floor. Injected: an ink so close to
        harbour's ground that the ratio collapses to about 1.1:1.

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
    return 0


if __name__ == "__main__":
    sys.exit(main())
