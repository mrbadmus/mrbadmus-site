#!/usr/bin/env python3
"""contrast_audit.py — WCAG AA text-contrast audit against the RENDERED page.

Mide's complaint (Experience run, item 13): "much of the dark text on the
cream background isn't clear enough." A prior pass measured the DOCUMENTED
token ratios in `shared/tokens.css`'s own comments and every one of them
"passed" — which cannot be what Mide sees, because those comments assume an
isolated token against its named ground and say nothing about what actually
happens once the value is composited through real ancestors: a caption
sitting under a card's own translucent tint, an opacity-dimmed control, a
disabled input, a browser-default `::placeholder` colour nobody ever set.

So this gate does not read the tokens file at all. It opens each page for
real in headless Chrome (the `ks3_browser` CDP harness — see that file for
why device-metric overrides are used instead of `--window-size`), walks
every VISIBLE text-bearing node, and for each one:

  1. reads its own `color` (or, for SVG text/tspan, its `fill`),
  2. walks every ancestor up to <html>, collecting each one's
     `background-color` and `opacity`,
  3. composites that chain — respecting alpha AND opacity, in real paint
     order (outermost first) — into one opaque "ground" colour and one
     "total dimming factor" that the text's own colour is blended through
     (an ancestor's `opacity` fades its whole subtree toward whatever is
     behind it; a bare alpha walk that stops at the first non-transparent
     background misses exactly this, which is the gap the prior pass fell
     into),
  4. computes the WCAG 2.1 contrast ratio of the FINAL composited pair,
  5. classifies the text as "large" (>=24px, or >=18.66px AND weight>=700)
     or "normal" and applies the matching AA floor (3.0 / 4.5),
  6. tries to name the CSS custom property that produced the colour, by
     re-querying a candidate list of `--st-*` / `--ks3-*` / legacy token
     names on the same element and matching resolved values byte-for-byte.

`::placeholder` colour is measured with `getComputedStyle(el, '::placeholder')`
and held to the same AA floor as any other text — it is real, informational
text a student or teacher reads. Disabled controls are measured and reported
SEPARATELY: WCAG does not bind them, but Mide asked for legibility everywhere,
so they are flagged under a 3:1 floor rather than silently excluded.

Usage
-----
    python3 contrast_audit.py                  # full sweep, both widths
    python3 contrast_audit.py --quick           # 1280 only, no screenshots
    python3 contrast_audit.py --before OUT.md   # write the failing-list report
    python3 contrast_audit.py --gate            # exit 1 on any AA failure (body text)

Registered in `gate_registry.py` as a FAST gate (measured ~45s locally for
the full page set at one width; `--quick` mode used in CI-speed contexts).
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
import time

REPO = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, REPO)

import ks3_browser as cdp  # noqa: E402

SHOTS_ROOT = os.environ.get("MRB_SHOTS") or os.environ.get("KS3_GATE_TMP") or os.path.expanduser("~/tmp/ks3-gates")
OUT_DIR = os.path.join(SHOTS_ROOT, "f")

WIDTHS = [1280, 390]

AA_NORMAL = 4.5
AA_LARGE = 3.0
DISABLED_FLOOR = 3.0


# ══════════════════════════════════════════════════════════════════════════
# colour arithmetic — WCAG 2.1, plus real alpha/opacity compositing
# ══════════════════════════════════════════════════════════════════════════

def parse_colour(s):
    """`rgb(r,g,b)` / `rgba(r,g,b,a)` / `#rrggbb` / `transparent` -> (r,g,b,a)."""
    s = (s or "").strip()
    if not s or s == "transparent":
        return (0, 0, 0, 0.0)
    if s.startswith("#"):
        h = s[1:]
        if len(h) == 3:
            h = "".join(c * 2 for c in h)
        if len(h) != 6:
            return None
        return (int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16), 1.0)
    if s.startswith("rgb"):
        inner = s[s.index("(") + 1:s.rindex(")")]
        parts = [p.strip() for p in inner.replace("/", ",").split(",") if p.strip()]
        if len(parts) not in (3, 4):
            return None
        try:
            r, g, b = (int(round(float(p))) for p in parts[:3])
            a = float(parts[3]) if len(parts) == 4 else 1.0
        except ValueError:
            return None
        return (r, g, b, a)
    return None


def _linear(channel):
    c = channel / 255.0
    if c <= 0.04045:
        return c / 12.92
    return ((c + 0.055) / 1.055) ** 2.4


def luminance(c):
    return 0.2126 * _linear(c[0]) + 0.7152 * _linear(c[1]) + 0.0722 * _linear(c[2])


def contrast(fg, bg):
    a, b = luminance(fg), luminance(bg)
    lo, hi = (a, b) if a < b else (b, a)
    return (hi + 0.05) / (lo + 0.05)


def over(fg, bg):
    """Porter-Duff 'over': fg (r,g,b,a) painted onto opaque bg (r,g,b,1) -> opaque colour."""
    a = fg[3]
    if a <= 0:
        return bg
    if a >= 1:
        return (fg[0], fg[1], fg[2])
    r = fg[0] * a + bg[0] * (1 - a)
    g = fg[1] * a + bg[1] * (1 - a)
    b = fg[2] * a + bg[2] * (1 - a)
    return (r, g, b)


def composite_ground(chain):
    """`chain`: [{bg, op}] from the text element OUTWARD to <html>.

    Returns (ground_rgb, total_opacity) — the opaque colour the text's own
    paint sits on, and the product of every ancestor's `opacity` (the factor
    the text colour itself is later blended through, because CSS `opacity`
    fades an element's WHOLE rendering — background and content alike —
    toward whatever is behind it, not just its background-color alpha).
    """
    layers = list(reversed(chain))  # outermost (html) first
    canvas = (255.0, 255.0, 255.0)  # fallback if truly nothing is opaque
    cum_op_outside = 1.0
    for layer in layers:
        op = layer.get("op", 1.0) or 1.0
        bg = parse_colour(layer.get("bg", ""))
        if bg is not None and bg[3] > 0:
            eff_alpha = bg[3] * op * cum_op_outside
            if eff_alpha > 0:
                canvas = over((bg[0], bg[1], bg[2], eff_alpha), canvas)
        cum_op_outside *= op
    return canvas, cum_op_outside


def effective_fg(color_str, chain):
    """Final opaque foreground colour after alpha + opacity compositing."""
    ground, total_opacity = composite_ground(chain)
    fg = parse_colour(color_str)
    if fg is None:
        return None, ground
    eff_alpha = fg[3] * total_opacity
    final = over((fg[0], fg[1], fg[2], eff_alpha), ground)
    return final, ground


def is_large(font_size_px, font_weight):
    try:
        w = int(font_weight)
    except (TypeError, ValueError):
        w = 700 if str(font_weight).lower() == "bold" else 400
    if font_size_px >= 24:
        return True
    if font_size_px >= 18.66 and w >= 700:
        return True
    return False


def hexof(rgb):
    return "#%02X%02X%02X" % (round(rgb[0]), round(rgb[1]), round(rgb[2]))


# ══════════════════════════════════════════════════════════════════════════
# in-page measurement
# ══════════════════════════════════════════════════════════════════════════

_MEASURE_JS = r"""
(function(){
  function ownText(el){
    var t = '';
    for (var i=0;i<el.childNodes.length;i++){
      var n = el.childNodes[i];
      if (n.nodeType===3) t += n.textContent;
    }
    return t.replace(/\s+/g,' ').trim();
  }
  function visible(el){
    var cs = getComputedStyle(el);
    if (cs.display==='none'||cs.visibility==='hidden'||cs.visibility==='collapse') return false;
    if (parseFloat(cs.opacity)===0) return false;
    var r = el.getBoundingClientRect();
    return r.width>0 && r.height>0;
  }
  // A DECORATIVE watermark, not information — Design's oversized background
  // numerals (e.g. a card's giant "01" behind its content) paint at a few
  // percent alpha and `pointer-events:none`, deliberately unreadable. WCAG
  // targets text that conveys information; a glyph nobody is meant to read
  // is not that, and holding it to 4.5:1 would mean "fixing" it into a
  // visible watermark, which is not what anyone wants. `aria-hidden`
  // ancestors are excluded for the same reason: the author has already said
  // this subtree carries no information.
  // A full-colour EMOJI glyph (the star-rating control's ⭐, for one) is
  // painted by the platform's colour-emoji font — CSS `color` has no effect
  // on it at all, so measuring the inherited `color` against the page
  // background is measuring a value the renderer never uses. Text that is
  // ENTIRELY such glyphs (plus ordinary whitespace) is excluded; text that
  // MIXES an emoji into real words is not, because the words still paint in
  // the measured colour.
  var EMOJI_RE = /^[\s←-⯿☀-➿︎️\u{1F000}-\u{1FFFF}]+$/u;
  function isEmojiOnly(text){
    return !!text && EMOJI_RE.test(text);
  }
  function isDecorative(el, colourStr, text){
    if (el.closest('[aria-hidden="true"]')) return true;
    if (isEmojiOnly(text)) return true;
    var pe = getComputedStyle(el).pointerEvents;
    var m = /rgba?\([^)]*,\s*([0-9.]+)\s*\)/.exec(colourStr || '');
    var ownAlpha = m ? parseFloat(m[1]) : 1.0;
    if (pe === 'none' && ownAlpha < 0.15) return true;
    return false;
  }
  function selOf(el){
    var parts=[], e=el, depth=0;
    while(e && e.nodeType===1 && depth<5){
      var s = e.tagName.toLowerCase();
      if (e.id){ parts.unshift(s+'#'+e.id); break; }
      if (typeof e.className==='string' && e.className.trim()){
        s += '.'+e.className.trim().split(/\s+/).slice(0,2).join('.');
      }
      parts.unshift(s); e = e.parentElement; depth++;
    }
    return parts.join('>');
  }
  // ⊕ KS4 pilot (docs/ks4/pilot-build-contract.md job 2) — SVG text/tspan
  // ground. An inline diagram (shared/ks4-diagrams.js's svg() wrapper, and
  // every KS4D drawer built on it) paints its own plate/shape fills as
  // SIBLING <rect>/<circle>/... elements, never as a DOM ANCESTOR of the
  // <text> sitting on them — so the plain ancestor walk below (bg/opacity
  // up the parentElement chain) can never see them and falls through to
  // whatever the PAGE's ground happens to be several ancestors further out
  // (e.g. the dark-mode `.rd` background), which is not what the glyph is
  // actually painted on. This is a PRECISION fix, not a tolerance: for SVG
  // text only, find the nearest shape that (a) precedes the text in
  // document/paint order and (b) whose box fully contains the text's box —
  // exactly Design's own plate-then-label paint order in every KS4D
  // drawer — and feed ITS fill in as the ground layer, still composited
  // through the real ancestor opacity chain exactly as before. Ordinary
  // (non-SVG) text is completely unaffected.
  function svgPlateFill(el){
    var svg = el.ownerSVGElement;
    if (!svg) return null;
    var tRect = el.getBoundingClientRect();
    if (!(tRect.width > 0 && tRect.height > 0)) return null;
    var shapes = svg.querySelectorAll('rect,circle,ellipse,polygon,path,use');
    var best = null;
    for (var i = 0; i < shapes.length; i++){
      var c = shapes[i];
      // c must PRECEDE el in document order (the paint-order requirement) —
      // DOCUMENT_POSITION_FOLLOWING on (c, el) means "el follows c".
      if (!(c.compareDocumentPosition(el) & Node.DOCUMENT_POSITION_FOLLOWING)) continue;
      var fill = getComputedStyle(c).fill;
      if (!fill || fill === 'none') continue;
      var r = c.getBoundingClientRect();
      if (!(r.width > 0 && r.height > 0)) continue;
      if (r.left <= tRect.left + 0.5 && r.top <= tRect.top + 0.5 &&
          r.right >= tRect.right - 0.5 && r.bottom >= tRect.bottom - 0.5){
        best = fill;  // keep overwriting: the LAST (nearest) match wins.
      }
    }
    return best;
  }
  function chainOf(el){
    var out=[], p=el;
    var isSvgText = (el.namespaceURI==='http://www.w3.org/2000/svg') &&
                    (el.tagName==='text'||el.tagName==='tspan');
    var plateFill = isSvgText ? svgPlateFill(el) : null;
    while(p && p.nodeType===1){
      var cs = getComputedStyle(p);
      out.push({bg: cs.backgroundColor, op: parseFloat(cs.opacity)});
      p = p.parentElement;
    }
    if (plateFill) out.splice(1, 0, {bg: plateFill, op: 1});
    out.push({bg: 'rgb(255,255,255)', op: 1});
    return out;
  }
  function tokenSnapshot(el){
    var cs = getComputedStyle(el);
    var names = ['--st-ink','--st-body','--st-muted','--st-caption','--st-faint',
      '--st-ghost','--st-accent-text','--st-room-text','--st-room-muted','--st-room-faint',
      '--st-room-hint','--st-ember','--st-ember-strong','--st-room-body','--st-room-note',
      '--ks3-ink','--ks3-ink-body','--ks3-ink-muted','--ks3-ink-faint','--ks3-ink-ghost',
      '--ks3-on-dark','--ks3-on-dark-body','--ks3-on-dark-muted','--ks3-accent-text',
      '--text','--muted','--ink','--ink-body','--ink-muted','--ink-faint','--accent',
      '--accent-hover', '--on-accent', '--on-accent-soft',
      '--k4-ink','--k4-ink-2','--k4-muted','--k4-muted-2','--k4-accent',
      '--k4-accent-deep','--k4-border-2'];
    var out = {};
    names.forEach(function(n){
      var v = cs.getPropertyValue(n);
      if (v && v.trim()) out[n] = v.trim();
    });
    return out;
  }
  var results = [];
  var all = document.querySelectorAll('*');
  for (var i=0;i<all.length;i++){
    var el = all[i];
    if (el.closest('script,style,noscript,template')) continue;
    if (!visible(el)) continue;
    var t = ownText(el);
    var isSvgText = (el.namespaceURI==='http://www.w3.org/2000/svg') &&
                    (el.tagName==='text'||el.tagName==='tspan');
    if (t || isSvgText){
      var cs = getComputedStyle(el);
      var colour = isSvgText ? cs.fill : cs.color;
      if (isDecorative(el, colour, t || el.textContent || '')) continue;
      var disabled = !!(el.disabled || el.getAttribute('aria-disabled')==='true' ||
                         el.closest('[disabled]'));
      results.push({
        kind: 'text', sel: selOf(el), text: (t||el.textContent||'').slice(0,80),
        color: colour, fontSize: parseFloat(cs.fontSize), fontWeight: cs.fontWeight,
        chain: chainOf(el), disabled: disabled, tokens: tokenSnapshot(el)
      });
    }
    if ((el.tagName==='INPUT'||el.tagName==='TEXTAREA') && el.getAttribute('placeholder')){
      var ph;
      try { ph = getComputedStyle(el, '::placeholder'); } catch(e) { ph = null; }
      var phColour = (ph && ph.color) ? ph.color : cs.color;
      var phSize = (ph && parseFloat(ph.fontSize)) || parseFloat(getComputedStyle(el).fontSize);
      results.push({
        kind: 'placeholder', sel: selOf(el), text: el.getAttribute('placeholder').slice(0,80),
        color: phColour, fontSize: phSize, fontWeight: getComputedStyle(el).fontWeight,
        chain: chainOf(el), disabled: !!el.disabled, tokens: tokenSnapshot(el)
      });
    }
    if ((el.tagName==='BUTTON'||el.tagName==='INPUT'||el.tagName==='SELECT'||el.tagName==='TEXTAREA')
        && el.disabled){
      var t2 = (el.value || el.textContent || el.getAttribute('aria-label') || '').trim();
      if (t2){
        var cs2 = getComputedStyle(el);
        results.push({
          kind: 'disabled-control', sel: selOf(el), text: t2.slice(0,80),
          color: cs2.color, fontSize: parseFloat(cs2.fontSize), fontWeight: cs2.fontWeight,
          chain: chainOf(el), disabled: true, tokens: tokenSnapshot(el)
        });
      }
    }
  }
  return results;
})()
"""


def token_for(color_str, tokens):
    fg = parse_colour(color_str)
    if fg is None:
        return None
    for name, val in tokens.items():
        pv = parse_colour(val)
        if pv and pv[:3] == fg[:3]:
            return name
    return None


# ══════════════════════════════════════════════════════════════════════════
# the page list
# ══════════════════════════════════════════════════════════════════════════

def _click_containing(text):
    """JS: click the first visible element whose own text contains `text`."""
    safe = json.dumps(text)
    return (
        "(function(){var t=%s; var els=document.querySelectorAll("
        "'button,a,[role=button]'); for (var i=0;i<els.length;i++){"
        "var e=els[i]; if((e.textContent||'').indexOf(t)>=0){"
        "var r=e.getBoundingClientRect(); if(r.width>0&&r.height>0){"
        "e.click(); return true;}}} return false;})()" % safe
    )


def _set_theme(name):
    return (
        "document.documentElement.setAttribute('data-bench-theme', %s)"
        % json.dumps(name)
    )


BENCH_THEMES = ["harbour", "clay", "chalk", "moss", "damson", "graphite"]

PAGES = []


def _page(label, path, setup=None, wait=0.5):
    PAGES.append({"label": label, "path": path, "setup": setup, "wait": wait})


for _name in ["classes", "class-detail", "student-detail", "assignment", "digest", "insights"]:
    _page("teacher/%s" % _name, "teacher_fixtures/%s-fixture.html" % _name)

_page("teacher/today.html", "teacher/today.html")
_page("teacher/timetable.html", "teacher/timetable.html")
_page("teacher/admin.html", "teacher/admin.html")
_page("teacher/import.html", "teacher/import.html")

for _t in BENCH_THEMES:
    _page("student/class.html [%s]" % _t, "student/class-fixture.html",
          setup=_set_theme(_t))
_page("student/assignment.html", "student/assignment-fixture.html")

_page("ks3 lesson", "ks3/biology/respiration/aerobic-respiration.html")
_page("ks4 lesson", "combined/higher/chemistry/atomic-structure/model-of-the-atom.html")
_page("ks4 chrome", "combined/higher/chemistry/atomic-structure.html")
_page("auth.html", "auth.html")
_page("leaderboard.html", "leaderboard.html")
_page("index.html", "index.html")

# ── theme run (26 Sep 2026): every family, not only the ones above ──
_page("ks4.html", "ks4.html")
_page("ks4 chrome/pathway", "combined/index.html")
_page("ks4 chrome/tier", "combined/higher/index.html")
_page("ks4 pilot/ionic-bonding [Combined Higher]",
      "combined/higher/chemistry/bonding/ionic-bonding.html")
_page("ks3 hub", "ks3/index.html")
_page("profile-setup.html", "profile-setup.html")
_page("weekly-challenge.html", "weekly-challenge.html")
_page("my-challenges.html", "my-challenges.html")
_page("past-papers.html", "past-papers.html")
_page("404.html", "404.html")
_page("teacher/seating.html", "teacher/seating.html")
_page("consumer/signup.html", "consumer/signup.html")
_page("consumer/today.html", "consumer/today.html")
_page("org", "org/index.html")
_page("parents/index.html", "parents/index.html")
_page("go/index.html", "go/index.html")

# ── CORE lane (theme run, 26 Sep 2026) — the rest of the CORE family:
#    root hand-written pages the sweep above didn't already list, plus a
#    genuine (non-pilot) subtopic lesson page and a subject hub. ──
_page("revision.html", "revision.html")
_page("teacher-profile.html", "teacher-profile.html")
_page("reset-password.html", "reset-password.html")
_page("ks4 chrome/subject", "combined/higher/physics/index.html")
_page("ks4 lesson/biology", "combined/higher/biology/homeostasis/nervous-system.html")

_page("teacher/class-detail [Set work sheet]", "teacher_fixtures/class-detail-fixture.html",
      setup=_click_containing("Set work"), wait=0.9)
_page("teacher/class-detail [shoutout composer]", "teacher_fixtures/class-detail-fixture.html",
      setup=_click_containing("Send a shoutout"), wait=0.9)

# ── KS4 pilot port (docs/ks4/pilot-build-contract.md; ks4_parity.py's own
#    sibling gate) — the 14 Triple Higher pilot pages (the "everything"
#    tier: every rung, badge and question-bank item a route can show) plus
#    the one Triple Foundation page whose R9 badge-gating differs from its
#    TH sibling (nanoparticles has no isHigher/isTriple badge of its own,
#    but its neighbours' pages differ in exactly this axis — kept here as
#    the one deliberate non-TH sample the brief names).
for _slug in ("chemical-bonds", "ionic-bonding", "ionic-compounds",
              "covalent-bonding", "metallic-bonding", "states-of-matter",
              "properties-ionic-compounds", "properties-small-molecules",
              "polymers", "giant-covalent-structures", "metals-alloys",
              "nanoparticles"):
    _page("ks4 pilot/%s" % _slug,
          "triple/higher/chemistry/bonding/%s.html" % _slug)
for _slug in ("series-parallel-circuits", "resistors"):
    _page("ks4 pilot/%s" % _slug,
          "triple/higher/physics/electricity/%s.html" % _slug)
_page("ks4 pilot/nanoparticles [Triple Foundation]",
      "triple/foundation/chemistry/bonding/nanoparticles.html")

# ── KS3 lane (theme run, 26 Sep 2026) ──
# The base commit already registered "ks3 lesson" (a biology lesson, no
# instrument) and "ks3 hub". This adds the browse layer (a year page, a unit
# page) and two more instrument-bearing lessons, one per remaining subject —
# chemistry's state-bench (particle model) and physics' circuit board — so
# the sweep actually exercises the `.ks3-dark` ink-block family and the
# standalone dark-panel instrument trays this lane's dark remap has to get
# right. (The chemistry pick started as `particle-model.html`; swapped to
# `solids-liquids-and-gases.html` after the first run surfaced a
# PRE-EXISTING, unrelated light-mode defect on the former — see the run
# report — rather than one this lane introduced or should paper over.)
_page("ks3 year page", "ks3/year-7/index.html")
_page("ks3 unit page", "ks3/physics/electric-circuits/index.html")
_page("ks3 lesson [chemistry, instrument]",
      "ks3/chemistry/particles-and-their-behaviour/solids-liquids-and-gases.html")
_page("ks3 lesson [physics, instrument]",
      "ks3/physics/electric-circuits/current-and-circuits.html")

# ── runtimes lane (theme run, 27 Sep 2026) ──
# The three hand-written student/ pages this lane wired that were not
# already in the list above — student/class.html, student/assignment.html
# and the six teacher fixtures were already here.
_page("student/classes.html", "student/classes.html")
_page("student/settings.html", "student/settings.html")
_page("student/claim-confirm.html", "student/claim-confirm.html")


# ══════════════════════════════════════════════════════════════════════════
# INTERACTION STATES (theme-run audit, 27 Sep 2026) — "the contrast gate
# missed all of these because it measures pages at rest." Every page above
# is measured AS LOADED; every defect the independent audit found was a
# page in a state only reachable after an interaction (chat opened and a
# message sent, an instrument answered, a card flipped, a toast fired) or
# on a surface the sweep above never had real data for (the leaderboard's
# week chips need a backend fetch this harness cannot make). This section
# adds exactly those states, each via a `setup=` step, so a real AA
# regression here shows up on `--interactions` the same way any other
# regression shows up above.
#
# Kept OUT of `PAGES` on purpose, behind `--interactions`: driving 15
# instruments' own controls one by one would slow the fast sweep every
# other page in this file has to stay fast for. `run_interactions()` below
# is registered as its own SLOW gate in gate_registry.py.
INTERACTION_PAGES = []


def _ipage(label, path, setup, wait=0.6):
    INTERACTION_PAGES.append({"label": label, "path": path, "setup": setup, "wait": wait})


# ── D1: the KS3 tutor chat, opened, with a sent exchange on screen ──
# `[data-open-chat]` is the real trigger `shared/mrbadmus.v2.js` binds
# (`document.querySelectorAll('[data-open-chat]').forEach(el =>
# el.addEventListener('click', open))`) — clicking it is the real open
# path, not a class toggle. A real reply needs the backend
# (`mrbadmus-backend.onrender.com`), which this harness has neither a
# route to nor a reason to fake, so the exchange is built via the EXACT
# markup `addMsg(role, html)` writes (`shared/mrbadmus.v2.js`: `<div
# class="chat-msg chat-msg--${role}"><div class="chat-msg__avatar">...
# </div><div class="chat-msg__bubble">...</div></div>`, appended to
# `#chatMsgs`) rather than calling that closure-private function.
_CHAT_OPEN_JS = r"""
(function(){
  var btn = document.querySelector('[data-open-chat]');
  if (btn) { btn.click(); }
  var box = document.getElementById('chatMsgs');
  if (box) {
    box.insertAdjacentHTML('beforeend',
      '<div class="chat-msg chat-msg--bot"><div class="chat-msg__avatar">⚡</div>'
      + '<div class="chat-msg__bubble">Great question — let\'s work through it '
      + 'with FIFA: Formula, Insert, Fix, Answer.</div></div>'
      + '<div class="chat-msg chat-msg--user"><div class="chat-msg__avatar">🧑</div>'
      + '<div class="chat-msg__bubble">Can you help me with this?</div></div>');
  }
})()
"""
_ipage("D1 ks3 tutor chat [open+message]",
       "ks3/physics/electric-circuits/current-and-circuits.html",
       setup=_CHAT_OPEN_JS)

# ── D2: the safeguarding box lessons — static content, no interaction
# needed, just not previously in PAGES/INTERACTION_PAGES at all. ──
for _slug, _path in (
    ("substance-misuse-and-decisions",
     "ks3/biology/health-and-drugs/substance-misuse-and-decisions.html"),
    ("alcohol-and-smoking", "ks3/biology/health-and-drugs/alcohol-and-smoking.html"),
    ("what-drugs-do-to-the-body",
     "ks3/biology/health-and-drugs/what-drugs-do-to-the-body.html"),
    ("how-we-worked-out-dna",
     "ks3/biology/inheritance-and-dna/how-we-worked-out-dna.html"),
):
    _ipage("D2 ks3 safeguarding box [%s]" % _slug, _path, setup=None, wait=0.2)

# ── D3: every "ink ground" panel this run fixed, reproduced as REAL,
# VISIBLE DOM nodes — the audit's own method (`inj.py`'s `build()`),
# ported here so this gate's generic walker measures them exactly as it
# measures any other text (no separate compositing logic needed: unlike
# the audit's own script, this one runs INSIDE the sweep that already
# composites real ancestor chains). Built on any KS3 lesson page, not the
# instruments' OWN lessons — these are synthetic nodes proving the CSS
# RULE, the same reason the audit's own script did not need the real
# instruments either. `pairs.json` under the audit's own `data/` is this
# list's source; kept verbatim so a future re-run of that script and this
# gate are checking the identical 42 pairings.
INSTRUMENT_PAIRS = [
    [".ks3-unit-panel", ".ks3-unit-panel .ks3-eyebrow"],
    [".ks3-unit-panel", ".ks3-unit-panel-intro"],
    [".ks3-board-verdict", ".ks3-board-verdict-body"],
    [".ks3-board-verdict", ".ks3-board-extra-label"],
    [".ks3-board-verdict", ".ks3-board-extra-note"],
    [".ks3-case-verdict", ".ks3-case-why"],
    [".ks3-switch-chain", ".ks3-switch-chip"],
    [".ks3-switch-chain", ".ks3-switch-step"],
    [".ks3-verdict-panel", ".ks3-verdict-panel .ks3-verdict-why"],
    [".ks3-limit-card[data-ground=\"ink\"]",
     ".ks3-limit-card[data-ground=\"ink\"] .ks3-limit-body"],
    [".ks3-pick-reveal", ".ks3-pick-reveal .ks3-pick-steplabel"],
    [".ks3-pick-reveal", ".ks3-pick-reveal .ks3-pick-stepnote"],
    [".ks3-pick-reveal", ".ks3-pick-reveal .ks3-pick-close"],
    [".ks3-lstep-reveal", ".ks3-lstep-reveal .ks3-lstep-steplabel"],
    [".ks3-lstep-reveal", ".ks3-lstep-reveal .ks3-lstep-stepnote"],
    [".ks3-lstep-reveal", ".ks3-lstep-reveal .ks3-lstep-close"],
    [".ks3-psort-reveal", ".ks3-psort .ks3-psort-why"],
    [".ks3-seq-report", ".ks3-seq .ks3-seq-reporttext"],
    [".ks3-still-result", ".ks3-still .ks3-still-resulttext"],
    [".ks3-mchoice-reveal", ".ks3-mchoice .ks3-mchoice-why"],
    [".ks3-critiq-reveal", ".ks3-critiq .ks3-critiq-why"],
    [".ks3-chroma-say", ".ks3-chroma .ks3-chroma-saytext"],
    [".ks3-mpb-say", ".ks3-mpb .ks3-mpb-saytext"],
    [".ks3-cpair-verdict", ".ks3-cpair .ks3-cpair-why"],
    [".ks3-iask-verdict", ".ks3-iask .ks3-iask-text"],
    [".ks3-eqb-check", ".ks3-eqb .ks3-eqb-checktext"],
    [".ks3-fcard .ks3-fcard-reveal", ".ks3-fcard .ks3-fcard-why"],
    [".ks3-tuber-done", ".ks3-tuber .ks3-tuber-finish"],
    [".ks3-ctube-open", ".ks3-ctube .ks3-ctube-why"],
    [".ks3-rgrid-result", ".ks3-rgrid .ks3-rgrid-why"],
    [".ks3-tsort-reveal", ".ks3-tsort .ks3-tsort-why"],
    [".ks3-tempb .ks3-tempb-run", ".ks3-tempb .ks3-tempb-figlabel"],
    [".ks3-tempb .ks3-tempb-run", ".ks3-tempb .ks3-tempb-why"],
    [".ks3-rigb .ks3-rigb-panel", ".ks3-rigb .ks3-rigb-figlabel"],
    [".ks3-rigb .ks3-rigb-panel", ".ks3-rigb .ks3-rigb-why"],
    [".ks3-phbench .ks3-phbench-result", ".ks3-phbench .ks3-phbench-why"],
    [".ks3-amgrid .ks3-amgrid-result", ".ks3-amgrid .ks3-amgrid-why"],
    [".ks3-namer .ks3-namer-result", ".ks3-namer .ks3-namer-note"],
    [".ks3-catb .ks3-catb-result", ".ks3-catb .ks3-catb-tilelabel"],
    [".ks3-catb .ks3-catb-result", ".ks3-catb .ks3-catb-figsnote"],
    [".ks3-catb .ks3-catb-result", ".ks3-catb .ks3-catb-why"],
    [".ks3-oxb .ks3-oxb-compare", ".ks3-oxb .ks3-oxb-cmp"],
]
_PAIRS_INJECT_JS = r"""
(function(pairs){
  function build(sel, parent){
    var parts = sel.split(/\s+/); var cur = parent; var last = null;
    parts.forEach(function(p){
      var m = p.match(/^([a-z]*)((?:\.[a-z0-9-]+)*)((?:\[[^\]]+\])*)$/i);
      if (!m) return;
      var el = document.createElement(m[1] || 'div');
      (m[2] || '').split('.').filter(Boolean).forEach(function(c){ el.classList.add(c); });
      var at = (m[3] || '').match(/\[([^=\]]+)(?:="?([^"\]]*)"?)?\]/g) || [];
      at.forEach(function(a){
        var mm = a.match(/\[([^=\]]+)(?:="?([^"\]]*)"?)?\]/);
        el.setAttribute(mm[1], mm[2] || '');
      });
      cur.appendChild(el); cur = el; last = el;
    });
    return last;
  }
  var host = document.querySelector('main') || document.querySelector('.rd');
  if (!host) return;
  pairs.forEach(function(pr){
    var box = document.createElement('div');
    host.appendChild(box);
    var panel = build(pr[0], box);
    if (!panel) return;
    var tparts = pr[1].split(/\s+/);
    var tl = tparts[tparts.length - 1];
    var tel = build(tl, panel);
    if (!tel) return;
    tel.textContent = 'Sample text for the contrast gate.';
  });
})(%s)
""" % json.dumps(INSTRUMENT_PAIRS)
_ipage("D3 ks3 instrument panels [42 pairs, post-answer]",
       "ks3/physics/electric-circuits/current-and-circuits.html",
       setup=_PAIRS_INJECT_JS, wait=0.3)

# ── D5: student flashcards, flipped so the "Next" button is on screen ──
_ipage("D5 student flashcards [Next button]", "student/class-fixture.html",
       setup=_click_containing("Flashcards") + ";" + _click_containing("Flip"),
       wait=0.6)

# ── D6: the leaderboard's SELECTED week chip — the real chip is
# client-rendered from a backend fetch this harness cannot make (no
# session, no `mrbadmus-backend.onrender.com` route), so the exact
# rendered SHAPE (`docs/ks3/design-reference/leaderboard/source/KS4 Weekly
# Leaderboard.dc.html`: `bg: on ? 'var(--st-ink)' : …, fg: on ?
# 'var(--st-cream)' : …`) is reproduced as a real, visible node instead of
# waiting on data this environment cannot provide. ──
_ipage("D6 leaderboard [selected week chip]", "leaderboard.html",
       setup=("(function(){document.body.insertAdjacentHTML('beforeend',"
              "'<button style=\"position:relative;padding:12px 30px 11px 14px;"
              "background:var(--st-ink);border:1px solid var(--st-ink);"
              "color:var(--st-cream);border-radius:14px;font:500 15px var(--st-mono);\">"
              "25 SEP\\u201311 OCT</button>');})()"),
       wait=0.2)

# ── D7: the teacher Set work toast — real trigger needs a save round trip
# to the backend; the audit's own shot (`fx_setwork_toast_dark.png`) notes
# it was "a toast injected into the real .sw-overlay", so this does the
# same, into the real class-detail fixture (real shared/set-work.css). ──
_ipage("D7 teacher Set work toast", "teacher_fixtures/class-detail-fixture.html",
       setup=("(function(){document.body.insertAdjacentHTML('beforeend',"
              "'<div class=\"sw-toast\">Set for 10h/Sc1 \\u00b7 not saved</div>');})()"),
       wait=0.2)

# ── D9: an older KS4 lesson's "Test Yourself" result banner, shown ──
_ipage("D9 ks4 lesson [Test Yourself result]",
       "combined/higher/physics/forces/distance-time-graphs.html",
       setup=("(function(){document.querySelectorAll('.quiz-options').forEach("
              "function(box){var o=box.querySelector('.quiz-opt'); if(o) o.click();});"
              "var b=document.getElementById('quizCheckBtn'); if(b) b.click();})()"),
       wait=0.4)


def run_interactions(widths=None, shots=True, themes=None):
    """The `--interactions` sweep: `sweep()`, pointed at `INTERACTION_PAGES`
    instead of `PAGES`, so the fast/default run's page count and timing are
    completely unaffected. Registered as its own SLOW gate — see
    gate_registry.py — because a couple of these steps (D3's 42-node inject,
    D9's click-every-option-then-check) are real page interactions, not
    just a bigger page list."""
    return sweep(widths=widths or WIDTHS, shots=shots, themes=themes,
                 page_list=INTERACTION_PAGES)


# ══════════════════════════════════════════════════════════════════════════
# the sweep
# ══════════════════════════════════════════════════════════════════════════

THEMES = ["light", "dark"]

# The page is loaded, the stored choice written the way shared/theme.js writes
# it, and the page RELOADED — so the measurement is of the real pre-paint path
# a pupil takes, not of an attribute poked in afterwards. The OS preference is
# pinned to the OPPOSITE of the theme under test, so a page that still follows
# the device (and ignores the choice) is caught rather than agreeing by luck.
_THEME_CHECK_JS = "document.documentElement.getAttribute('data-theme')"


def _apply_theme(p, theme, url):
    other = "dark" if theme == "light" else "light"
    try:
        p.send("Emulation.setEmulatedMedia", {
            "features": [{"name": "prefers-color-scheme", "value": other}]})
    except Exception:
        pass
    p.eval("try{localStorage.setItem('mrb-theme',%s)}catch(e){}" % json.dumps(theme))
    p.goto(url)
    return p.eval(_THEME_CHECK_JS)


def sweep(widths=WIDTHS, shots=True, only=None, themes=None, page_list=None):
    themes = themes or THEMES
    pages = PAGES if page_list is None else page_list
    findings = []
    server, port = cdp.serve(REPO)
    try:
        with cdp.Browser() as b:
            for spec in pages:
                if only and only not in spec["label"]:
                    continue
                url = "http://127.0.0.1:%d/%s" % (port, spec["path"])
                for width, theme in [(w, t) for t in themes for w in widths]:
                    label = "%s {%s}" % (spec["label"], theme)
                    p = b.page(url)
                    p.set_viewport(width, 1600 if width > 500 else 2200)
                    got = _apply_theme(p, theme, url)
                    if got != theme:
                        findings.append({
                            "page": label, "width": width,
                            "error": "page did not take the %s theme "
                                     "(html data-theme=%r)" % (theme, got),
                        })
                        continue
                    if spec["setup"]:
                        try:
                            p.eval(spec["setup"])
                            time.sleep(spec.get("wait", 0.5))
                        except Exception as e:
                            findings.append({
                                "page": label, "width": width,
                                "error": "setup failed: %s" % e,
                            })
                            continue
                    try:
                        # Measure the SETTLED page: an entrance fade (the landing's
                        # k4-rise strip) otherwise reads as a contrast failure
                        # partway through its opacity ramp.
                        p.eval("(document.getAnimations?document.getAnimations():[])"
                               ".forEach(function(a){try{a.finish()}catch(e){}})")
                        rows = p.eval(_MEASURE_JS)
                    except Exception as e:
                        findings.append({
                            "page": label, "width": width,
                            "error": "measure failed: %s" % e,
                        })
                        continue
                    for row in (rows or []):
                        final, ground = effective_fg(row["color"], row["chain"])
                        if final is None:
                            continue
                        ratio = contrast(final, ground)
                        large = is_large(row["fontSize"], row["fontWeight"])
                        floor = AA_LARGE if large else AA_NORMAL
                        kind = row["kind"]
                        if kind == "disabled-control" or row.get("disabled"):
                            floor = DISABLED_FLOOR
                            kind = kind if kind == "disabled-control" else kind + "+disabled"
                        if ratio < floor:
                            findings.append({
                                "page": label, "width": width, "kind": kind,
                                "sel": row["sel"], "text": row["text"],
                                "fg_raw": row["color"], "fg_hex": hexof(final),
                                "bg_hex": hexof(ground), "ratio": round(ratio, 2),
                                "floor": floor, "fontSize": row["fontSize"],
                                "fontWeight": row["fontWeight"],
                                "token": token_for(row["color"], row.get("tokens", {})),
                            })
                    if shots:
                        os.makedirs(OUT_DIR, exist_ok=True)
                        safe = re.sub(r"[^a-zA-Z0-9]+", "-", label).strip("-")
                        try:
                            p.screenshot(os.path.join(OUT_DIR, "%s-%d.png" % (safe, width)),
                                         width=width)
                        except Exception:
                            pass
    finally:
        server.shutdown()
    return findings


def write_report(findings, path, title, page_count=None, width_count=None, theme_count=None):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    lines = ["# %s\n" % title, ""]
    if not findings:
        lines.append("Zero findings under AA (body/large) and the 3:1 disabled floor.\n")
    errors = [f for f in findings if "error" in f]
    real = [f for f in findings if "error" not in f]
    real.sort(key=lambda f: f["ratio"])
    lines.append("%d failing text/placeholder/disabled instances across %d page+width combinations measured.\n"
                  % (len(real), (page_count if page_count is not None else len(PAGES))
                     * (width_count if width_count is not None else len(WIDTHS))
                     * (theme_count if theme_count is not None else len(THEMES))))
    lines.append("| ratio | floor | page | width | kind | token | fg | bg | selector | text |")
    lines.append("|---|---|---|---|---|---|---|---|---|---|")
    for f in real:
        lines.append("| %.2f | %s | %s | %d | %s | %s | %s | %s | `%s` | %s |" % (
            f["ratio"], f["floor"], f["page"], f["width"], f["kind"],
            f["token"] or "?", f["fg_hex"], f["bg_hex"], f["sel"],
            f["text"].replace("|", "\\|")[:50],
        ))
    if errors:
        lines.append("\n## Page errors\n")
        for e in errors:
            lines.append("- %s @%d: %s" % (e["page"], e["width"], e["error"]))
    with open(path, "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines) + "\n")
    return real, errors


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--quick", action="store_true", help="1280 only, no screenshots")
    ap.add_argument("--before", default=None)
    ap.add_argument("--after", default=None)
    ap.add_argument("--only", default=None, help="substring filter on page label")
    ap.add_argument("--gate", action="store_true")
    ap.add_argument("--themes", default="light,dark",
                    help="comma list of site themes to measure (light,dark)")
    ap.add_argument("--interactions", action="store_true",
                    help="sweep INTERACTION_PAGES (chat open, instrument "
                         "after answering, flashcards, toasts, quiz result) "
                         "instead of the at-rest PAGES list — see gate_registry.py, "
                         "registered as its own slow gate")
    args = ap.parse_args()

    widths = [1280] if args.quick else WIDTHS
    themes = [t for t in args.themes.split(",") if t]
    if args.interactions:
        findings = run_interactions(widths=widths, shots=not args.quick, themes=themes)
        page_count = len(INTERACTION_PAGES)
    else:
        findings = sweep(widths=widths, shots=not args.quick, only=args.only, themes=themes)
        page_count = len(PAGES)
    out_path = args.before or args.after or os.path.join(OUT_DIR, "contrast-before.md")
    title = "Contrast audit — %s%s" % (
        "after" if args.after else "before",
        " (interactions)" if args.interactions else "")
    real, errors = write_report(findings, out_path, title, page_count=page_count,
                                width_count=len(widths), theme_count=len(themes))
    print("contrast_audit: %d failing instance(s), %d page error(s). Report: %s"
          % (len(real), len(errors), out_path))
    if args.gate:
        body_fail = [f for f in real if f["kind"] not in ("disabled-control",)]
        if body_fail or errors:
            print("FAIL — %d AA violation(s) at body/large text, %d page error(s)"
                  % (len(body_fail), len(errors)))
            return 1
        print("PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
