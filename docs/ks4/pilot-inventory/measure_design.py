#!/usr/bin/env python3
"""measure_design.py — the KS4 pilot inventory measuring script.

Re-run with:

    cd /Users/midebadmus/Documents/GitHub/mrbadmus-worktrees/ks4-pilot
    python3 docs/ks4/pilot-inventory/measure_design.py

Serves docs/ks4/design-reference/pilot/ over HTTP (Design's pages load React/
Babel from unpkg at runtime, so Chrome needs network), drives all 14 lessons
in headless Chrome via ks3_browser.py (the repo's CDP harness — its own
docstring calls itself "cdp.py"), and writes:

  docs/ks4/pilot-inventory/reference.json   — the machine-readable baseline
  $MRB_SHOTS/design/<slug>-360.png          — one screenshot per lesson, 360w
  $MRB_SHOTS/design/<slug>-1280.png         — one screenshot per lesson, 1280w

Screenshots are Triple Higher, light mode only (§6 of the brief). Nothing is
written into the repo tree for screenshots.

This script is READ-ONLY against the delivery: it never edits a .dc.html
file. It kills its own Chrome + HTTP server processes on exit (normal or via
KeyboardInterrupt) and prints their PIDs as it starts them, per the brief's
"kill by captured PID" rule.
"""
from __future__ import annotations

import json
import os
import signal
import subprocess
import sys
import time
import urllib.request

REPO_ROOT = "/Users/midebadmus/Documents/GitHub/mrbadmus-worktrees/ks4-pilot"
PILOT_DIR = os.path.join(REPO_ROOT, "docs/ks4/design-reference/pilot")
LESSON_DIR = os.path.join(PILOT_DIR, "KS4 Lessons", "Pilot - Bonding and Electricity")
OUT_JSON = os.path.join(REPO_ROOT, "docs/ks4/pilot-inventory/reference.json")
PORT = 8802
SHOTS = os.environ.get("MRB_SHOTS", "/Users/midebadmus/tmp/ks4-pilot-shots")
SHOTS_DESIGN = os.path.join(SHOTS, "design")

sys.path.insert(0, REPO_ROOT)
import ks3_browser as cdp  # noqa: E402  ("cdp.py" per its own docstring)

WIDTHS = [1280, 1340, 820, 390, 360]
ROUTES = ["Triple Higher", "Combined Foundation", "Combined Higher", "Triple Foundation"]
DEFAULT_ROUTE = "Triple Higher"

# site slug -> design filename (pilot-build-contract.md §0)
LESSONS = [
    ("chemical-bonds", "ks4-chemistry-5.2.1.1-chemical-bonds.dc.html"),
    ("ionic-bonding", "ks4-chemistry-5.2.1.2-ionic-bonding.dc.html"),
    ("ionic-compounds", "ks4-chemistry-5.2.1.3-ionic-compounds.dc.html"),
    ("covalent-bonding", "ks4-chemistry-5.2.1.4-covalent-bonding.dc.html"),
    ("metallic-bonding", "ks4-chemistry-5.2.1.5-metallic-bonding.dc.html"),
    ("states-of-matter", "ks4-chemistry-5.2.2.1-states-of-matter.dc.html"),
    ("properties-ionic-compounds", "ks4-chemistry-5.2.2.3-properties-ionic-compounds.dc.html"),
    ("properties-small-molecules", "ks4-chemistry-5.2.2.4-properties-small-molecules.dc.html"),
    ("polymers", "ks4-chemistry-5.2.2.5-polymers.dc.html"),
    ("giant-covalent-structures", "ks4-chemistry-5.2.2.6-giant-covalent-structures.dc.html"),
    ("metals-alloys", "ks4-chemistry-5.2.2.7-metals-alloys.dc.html"),
    ("nanoparticles", "ks4-chemistry-5.2.3.3-nanoparticles.dc.html"),
    ("series-parallel-circuits", "ks4-physics-6.2.2-series-parallel-circuits.dc.html"),
    ("resistors", "ks4-physics-6.2.1.4-resistors-iv-required-practical.dc.html"),
]

# Components measured for the fixed computed-style set (best-effort selectors;
# a lesson that lacks one records null rather than raising).
STYLE_TARGETS = {
    "h1": "h1",
    "eyebrow": ".ks3-eyebrow",
    "commit": ".ks3-commit",
    "option_resting": ".ks3-option",
    "reveal": "[data-arrive]",
    "misconception_panel": ".ks3-misconception",
    "key_fact_card": "[data-key-fact]",
    "badge_pill": "[style*='border-radius: 99px'], [style*='border-radius:99px']",
    "ladder_rung_header": ".ks3-ladder h2, .ks3-ladder [class*=rung] h3, .ks3-ladder header",
    "check_button": "button",
    "key_note_card": "#s-keynote",
    "end_prev_next": ".ks3-endmatter a",
}

JS_HELPERS = r"""
window.__mrb = window.__mrb || {};
__mrb.settle = (ms) => new Promise(r => setTimeout(r, ms));
__mrb.cs = (el, props) => {
  if (!el) return null;
  const s = getComputedStyle(el);
  const out = {};
  for (const p of props) out[p] = s.getPropertyValue(p) || s[p] || null;
  const r = el.getBoundingClientRect();
  out.__box = {x: Math.round(r.x), y: Math.round(r.y), w: Math.round(r.width), h: Math.round(r.height)};
  return out;
};
__mrb.STYLE_PROPS = ['font-family','font-size','font-weight','color','background-color','border','border-radius','padding','box-shadow'];
"""


def set_media(page, scheme=None, motion=None):
    """Force prefers-color-scheme / prefers-reduced-motion.

    ⚠️ Headless Chrome's OWN default color-scheme preference is DARK, not
    light or "no preference" — verified live: `matchMedia('(prefers-color-
    scheme: dark)').matches` is `true` and `.rd` background is #16120E
    (dark ground) on a fresh page with no emulation applied at all. So every
    "light mode" measurement in this script explicitly forces
    prefers-color-scheme: light; nothing is measured under Chrome's silent
    default. Documented in README.md as a method note, not just a code
    comment, because it would otherwise silently invert every light/dark
    finding in reference.json.
    """
    features = []
    if scheme is not None:
        features.append({"name": "prefers-color-scheme", "value": scheme})
    if motion is not None:
        features.append({"name": "prefers-reduced-motion", "value": motion})
    page.send("Emulation.setEmulatedMedia", {"features": features})


def wait_mounted(page, timeout=20):
    deadline = time.time() + timeout
    while time.time() < deadline:
        try:
            ok = page.eval(
                "!!(document.querySelector('.ks3-lesson') && "
                "document.querySelector('[id^=\"s-\"]'))"
            )
        except Exception:
            ok = False
        if ok:
            return True
        time.sleep(0.4)
    return False


def set_route(page, route_label):
    js = """
    (function(label){
      const sel = document.querySelector('select');
      if (!sel) return false;
      const opt = Array.from(sel.options).find(o => o.value === label || o.textContent.trim() === label);
      if (!opt) return false;
      const setter = Object.getOwnPropertyDescriptor(window.HTMLSelectElement.prototype, 'value').set;
      setter.call(sel, opt.value);
      sel.dispatchEvent(new Event('input', {bubbles:true}));
      sel.dispatchEvent(new Event('change', {bubbles:true}));
      return true;
    })(%s);
    """ % json.dumps(route_label)
    ok = page.eval(js)
    time.sleep(0.5)
    return ok


BLOCK_ID_HINTS = {
    "s-hook": "hook",
    "s-think": "misconception",
    "s-sort": "check",
    "s-ladder": "ladder",
    "s-keynote": "key-note",
    "s-rule": "rule",
    "s-board": "check",
    "s-decider": "check",
}


def classify_block(section_info):
    """Best-effort classification against the closed vocabulary, from id/class/eyebrow/text."""
    sid = (section_info.get("id") or "").lower()
    cls = (section_info.get("class") or "").lower()
    eyebrow = (section_info.get("eyebrow") or "").lower()
    text = (section_info.get("text") or "").lower()
    dc = section_info.get("dcImports") or []

    if sid in BLOCK_ID_HINTS and sid not in ("s-sort", "s-board", "s-decider"):
        return BLOCK_ID_HINTS[sid]
    if "hook" in cls or sid == "s-hook":
        return "hook"
    if "misconception" in cls or "spot the flaw" in eyebrow:
        return "misconception"
    if sid == "s-ladder" or "ladder" in cls or "Ks4Ladder" in dc:
        return "ladder"
    if sid == "s-keynote" or "Ks4KeyNote" in dc:
        return "key-note"
    if "Ks4QuizBank" in dc:
        return "question-bank"
    if "Ks4End" in dc:
        return "end"
    if "Ks4Video" in dc:
        return "video"
    if "Ks4Chrome" in dc:
        return "chrome"
    if "required practical" in eyebrow or "required-practical" in cls:
        return "required-practical"
    if "equation" in eyebrow or "Ks4Cfifa" in dc:
        return "equation" if "equation" in eyebrow else "formula"
    if "command word" in text[:200] or "<dl" in text:
        pass
    if "key fact" in eyebrow or "keyfact" in cls:
        return "key-fact"
    if "explainer" in cls:
        return "explainer"
    if "Ks4Sort" in dc:
        return "check"
    if "Ks4Chain" in dc:
        return "check"
    if "Ks4Write" in dc:
        return "extended-response"
    if section_info.get("tag") == "header":
        return "chrome"
    return "explainer"


def measure_sections(page):
    js = """
    (function(){
      const root = document.querySelector('.ks3-lesson');
      if (!root) return [];
      const out = [];
      Array.from(root.children).forEach((el, i) => {
        const r = el.getBoundingClientRect();
        const eyebrow = el.querySelector ? (el.querySelector('.ks3-eyebrow')?.textContent || '') : '';
        const dcImports = [];
        if (el.querySelectorAll) {
          // dc-import nodes are compiled away by the runtime into mounted
          // component roots; look for data-dc-component or known class hooks.
          el.querySelectorAll('[data-dc-component]').forEach(n => dcImports.push(n.getAttribute('data-dc-component')));
        }
        const badge = Array.from(el.querySelectorAll('*')).some(n => /Higher|Triple|Required practical/.test(n.textContent||'') && (n.getAttribute('style')||'').includes('border-radius'));
        out.push({
          index: i,
          tag: el.tagName.toLowerCase(),
          id: el.id || null,
          class: el.className || null,
          eyebrow: eyebrow.trim(),
          text: (el.textContent||'').trim().slice(0, 4000),
          words: (el.textContent||'').trim().split(/\\s+/).filter(Boolean).length,
          box: {x: Math.round(r.x), y: Math.round(r.y), w: Math.round(r.width), h: Math.round(r.height)},
          dcImports: dcImports,
          badgeLike: badge
        });
      });
      return out;
    })();
    """
    return page.eval(js)


def measure_overflow(page):
    js = """
    (function(){
      const dw = document.documentElement.scrollWidth;
      const iw = window.innerWidth;
      let offender = null;
      if (dw > iw) {
        let worst = null, worstRight = iw;
        document.querySelectorAll('body *').forEach(el => {
          const r = el.getBoundingClientRect();
          if (r.right > worstRight + 1) { worstRight = r.right; worst = el; }
        });
        if (worst) {
          offender = worst.tagName.toLowerCase() + (worst.id ? '#'+worst.id : '') + (worst.className && typeof worst.className === 'string' ? '.'+worst.className.split(' ').filter(Boolean).join('.') : '');
        }
      }
      return {scrollWidth: dw, innerWidth: iw, overflow: dw > iw, offender: offender};
    })();
    """
    return page.eval(js)


def measure_rail(page):
    js = """
    (function(){
      const side = document.querySelector('[data-rail="side"]');
      const top = document.querySelector('[data-rail="top"]');
      const sideVisible = side ? getComputedStyle(side).display !== 'none' : false;
      const topVisible = top ? getComputedStyle(top).display !== 'none' : false;
      const nodes = side ? Array.from(side.querySelectorAll('li')).map(li => (li.textContent||'').trim()) : [];
      const sideBox = side ? (() => {const r = side.getBoundingClientRect(); return {x:Math.round(r.x),y:Math.round(r.y),w:Math.round(r.width),h:Math.round(r.height)};})() : null;
      const topText = top ? (top.textContent||'').trim().replace(/\\s+/g,' ') : null;
      return {sideVisible, topVisible, sideNodeCount: nodes.length, sideNodes: nodes, sideBox, topText};
    })();
    """
    return page.eval(js)


def measure_ladder(page):
    js = """
    (function(){
      const ladder = document.querySelector('#s-ladder');
      if (!ladder) return null;
      const text = (ladder.textContent||'').trim();
      const scoreEl = ladder.querySelector('.ks3-score');
      const scoreNoteEl = ladder.querySelector('.ks3-score-note');
      const rungs = ladder.querySelectorAll('.ks3-rung').length;
      return {
        words: text.split(/\\s+/).filter(Boolean).length,
        scoreLine: scoreEl ? scoreEl.textContent.trim() : null,
        scoreNote: scoreNoteEl ? scoreNoteEl.textContent.trim() : null,
        rungCount: rungs,
        hasCommandWords: /Recall|Apply|Explain|Produce|Compare|Evaluate|Deduce|Calculate/.test(text)
      };
    })();
    """
    return page.eval(js)


def measure_keynote(page):
    js = """
    (function(){
      const kn = document.querySelector('#s-keynote');
      if (!kn) return null;
      const ol = kn.querySelector('ol');
      const lines = ol ? Array.from(ol.querySelectorAll('li')).map(li => (li.textContent||'').trim()) : [];
      return {lineCount: lines.length, lines: lines};
    })();
    """
    return page.eval(js)


BANK_ROOT_FN = """
function __mrbBankRoot(){
  const eyebrow = Array.from(document.querySelectorAll('.ks3-eyebrow'))
    .find(p => (p.textContent||'').includes('Practice set'));
  if (!eyebrow) return null;
  let root = eyebrow.parentElement;
  for (let i = 0; i < 4 && root; i++) {
    if (root.querySelector('ol')) return root;
    root = root.parentElement;
  }
  return eyebrow.closest('div');
}
"""


def measure_bank_full(page):
    """Ks4QuizBank paginates behind its OWN 'load more' button — `.ks3-reveal-btn`
    (`hasMore`/`onMore`, `state.shown` starts at 4, Ks4QuizBank.dc.html). ⚠️ That
    class name COLLIDES with `#s-sort`'s "Show what settles each one" button,
    which sits earlier in the DOM and is `disabled` until the sort is complete —
    a naive `document.querySelector('.ks3-reveal-btn')` finds THAT one first and
    (because it's disabled) looks exhausted after zero clicks. So every click here
    is scoped to the bank's own root, found by its "Practice set" eyebrow."""
    page.eval(BANK_ROOT_FN + "; window.__mrbBankRoot = __mrbBankRoot; true;")
    clicks = 0
    while True:
        js_click_more = """
        (function(){
          const root = window.__mrbBankRoot();
          if (!root) return false;
          const btn = root.querySelector('.ks3-reveal-btn');
          if (!btn || btn.disabled) return false;
          btn.scrollIntoView({block:'center'});
          btn.click();
          return true;
        })();
        """
        try:
            more = page.eval(js_click_more)
        except Exception:
            break
        if not more:
            break
        clicks += 1
        time.sleep(0.3)
        if clicks > 20:
            break
    js = """
    (function(){
      const root = window.__mrbBankRoot();
      if (!root) return {itemCount: null, verdictWords: []};
      const ol = root.querySelector('ol');
      const count = ol ? ol.querySelectorAll(':scope > li').length : null;
      const words = Array.from(root.querySelectorAll('[role=status] strong')).map(s => s.textContent.trim());
      return {itemCount: count, verdictWords: words};
    })();
    """
    try:
        result = page.eval(js)
    except Exception:
        result = {"itemCount": None, "verdictWords": []}
    result["loadMoreClicks"] = clicks
    return result


def measure_focusables(page):
    js = """
    (function(){
      const sel = 'a[href], button:not([disabled]), select, textarea, input, [tabindex]';
      const els = Array.from(document.querySelectorAll(sel));
      const visible = els.filter(el => {
        const r = el.getBoundingClientRect();
        return r.width > 0 && r.height > 0 && getComputedStyle(el).visibility !== 'hidden';
      });
      const negIdx = els.filter(el => el.getAttribute('tabindex') === '-1');
      return {count: visible.length, negativeTabindex: negIdx.length};
    })();
    """
    return page.eval(js)


def cs(page, selector):
    js = "__mrb.cs(document.querySelector(%s), __mrb.STYLE_PROPS)" % json.dumps(selector)
    try:
        return page.eval(js)
    except Exception:
        return None


def measure_rail_scrolled(page):
    """Scroll past 140px (Ks4Chrome's `scrolled = window.scrollY > 140` gate for the
    top bar) and re-measure the rail. Below 1340px NEITHER rail shows at scrollY=0:
    the side rail is CSS-hidden below 1340, and the top rail's own `showTop` state
    starts false and only flips on scroll — it is not width-driven at all."""
    page.eval("window.scrollTo(0, 300)")
    time.sleep(0.4)
    r = measure_rail(page)
    page.eval("window.scrollTo(0, 0)")
    time.sleep(0.2)
    return r


def measure_widths_for_route(page, url, route, widths, deep_width=1280):
    """Navigate once, set route, then sweep widths. Returns dict keyed by width."""
    page.goto(url, settle=0.8)
    set_media(page, scheme="light")
    wait_mounted(page)
    page.eval(JS_HELPERS)
    if route != DEFAULT_ROUTE:
        set_route(page, route)
        page.eval(JS_HELPERS)
    out = {}
    for w in widths:
        page.set_viewport(w, 1000)
        time.sleep(0.5)
        rail_at_top = measure_rail(page)
        entry = {
            "sections": measure_sections(page),
            "overflow": measure_overflow(page),
            "rail": rail_at_top,
            "rail_after_scroll": measure_rail_scrolled(page) if w < 1340 else None,
            "ladder": measure_ladder(page),
            "focusables": measure_focusables(page) if w == deep_width else None,
        }
        out[str(w)] = entry
    return out, page


def measure_styles(page, width=1280):
    page.set_viewport(width, 1000)
    time.sleep(0.3)
    out = {}
    for key, sel in STYLE_TARGETS.items():
        out[key] = cs(page, sel)
    return out


def measure_interactions(page, width=1280):
    """Drive the common interactions and record verdict text via a before/after
    textContent diff on the enclosing section — robust to unknown class names,
    since KS4's Ks4Choice reveal `<p>` (Ks4Choice.dc.html L39) carries no
    distinguishing class at all, unlike KS3's `.ks3-reveal`. Best-effort: a
    lesson missing a given control records null rather than failing the run."""
    page.set_viewport(width, 1000)
    time.sleep(0.3)
    results = {}

    def section_text(sel):
        try:
            return page.eval("(document.querySelector(%s)||{}).textContent||''" % json.dumps(sel))
        except Exception:
            return ""

    def click_first(selector):
        js = """
        (function(sel){
          const els = Array.from(document.querySelectorAll(sel));
          const el = els.find(e => { const r = e.getBoundingClientRect(); return r.width>0 && r.height>0 && !e.disabled; });
          if (!el) return false;
          el.scrollIntoView({block:'center'});
          el.click();
          return true;
        })(%s);
        """ % json.dumps(selector)
        try:
            return page.eval(js)
        except Exception:
            return False

    def diff_new_tail(before, after):
        if not before or not after:
            return None
        if after.startswith(before):
            tail = after[len(before):].strip()
            return tail[:600] if tail else None
        return None

    # Hook: first option in #s-hook — record verdict word (reply) and the new
    # tail (the reveal paragraph, appended after commit).
    before = section_text("#s-hook")
    ok = click_first("#s-hook button")
    time.sleep(0.5)
    after = section_text("#s-hook")
    results["hook_option_clicked"] = ok
    results["hook_reveal_new_text"] = diff_new_tail(before, after)
    try:
        results["hook_reveal_data_arrive_text"] = page.eval(
            "(document.querySelector('#s-hook [data-arrive]')||{}).textContent||null"
        )
        results["hook_reveal_animation_name_light"] = page.eval(
            "(()=>{const e=document.querySelector('#s-hook [data-arrive]'); return e?getComputedStyle(e).animationName:null;})()"
        )
        results["hook_reveal_style"] = cs(page, "#s-hook [data-arrive]")
    except Exception:
        pass
    try:
        results["hook_option_chosen_style"] = cs(page, "#s-hook .ks3-option[aria-pressed=true]")
    except Exception:
        pass

    # Misconception spot-the-flaw
    before = section_text("#s-think")
    ok2 = click_first("#s-think button")
    time.sleep(0.5)
    after = section_text("#s-think")
    results["misconception_option_clicked"] = ok2
    results["misconception_new_text"] = diff_new_tail(before, after)

    # Flagship instrument: click the first button inside the first "N" (new,
    # unregistered) block after the hook, i.e. the section right after
    # #s-hook/#s-explainer that is not #s-think/#s-sort/#s-ladder.
    flagship_before = None
    try:
        flagship_id = page.eval(
            "(function(){const root=document.querySelector('.ks3-lesson'); if(!root) return null;"
            "const kids=Array.from(root.children).filter(c=>c.id && c.id.startsWith('s-') && !['s-hook','s-think','s-sort','s-ladder','s-keynote'].includes(c.id));"
            "return kids.length ? kids[0].id : null;})()"
        )
    except Exception:
        flagship_id = None
    results["flagship_section_id"] = flagship_id
    if flagship_id:
        sel = "#%s" % flagship_id
        before = section_text(sel)
        ok5 = click_first("%s button" % sel)
        time.sleep(0.6)
        after = section_text(sel)
        results["flagship_option_clicked"] = ok5
        results["flagship_new_text"] = diff_new_tail(before, after)

    # Sort: tap first card-like button then a bin-like button, if #s-sort exists
    if page.eval("!!document.querySelector('#s-sort')"):
        before = section_text("#s-sort")
        buttons = page.eval("Array.from(document.querySelectorAll('#s-sort button')).length")
        results["sort_button_count"] = buttons
        ok6 = click_first("#s-sort button")
        time.sleep(0.3)
        ok7 = click_first("#s-sort button:nth-of-type(2)")
        time.sleep(0.4)
        after = section_text("#s-sort")
        results["sort_interacted"] = ok6 and ok7
        results["sort_new_text"] = diff_new_tail(before, after)

    # Ladder rung 1: click first option
    ok3 = click_first("#s-ladder button")
    time.sleep(0.5)
    results["ladder_rung_clicked"] = ok3
    try:
        results["ladder_feedback_text"] = page.eval(
            "(document.querySelector('#s-ladder .ks3-feedback')||{}).textContent||null"
        )
        results["ladder_feedback_class"] = page.eval(
            "(document.querySelector('#s-ladder .ks3-feedback')||{}).className||null"
        )
    except Exception:
        results["ladder_feedback_text"] = None

    # Ladder rung 4 (Write): type text, check min-words unlock
    try:
        ta = page.eval("!!document.querySelector('#s-ladder textarea')")
    except Exception:
        ta = False
    results["ladder_write_present"] = ta
    if ta:
        page.eval(
            "(function(){const t=document.querySelector('#s-ladder textarea'); if(!t) return;"
            "const setter=Object.getOwnPropertyDescriptor(window.HTMLTextAreaElement.prototype,'value').set;"
            "setter.call(t, 'This is a full-sentence test answer with more than twelve words in it for the unlock.');"
            "t.dispatchEvent(new Event('input',{bubbles:true}));})()"
        )
        time.sleep(0.3)
        click_first("#s-ladder .ks3-check-btn, #s-ladder button")
        time.sleep(0.4)
        results["ladder_write_ticks_present"] = page.eval(
            "!!document.querySelector('#s-ladder .ks3-ticks, #s-ladder [class*=tally]')"
        )

    # Key note flip / cover-recall toggle — record label text change
    kn_before = section_text("#s-keynote")
    ok4 = click_first("#s-keynote button")
    time.sleep(0.3)
    kn_after = section_text("#s-keynote")
    results["keynote_toggle_clicked"] = ok4
    results["keynote_label_changed"] = (kn_before != kn_after)

    return results


def console_errors_filtered(page):
    errs = page.console_errors()
    return [e for e in errs if "favicon.ico" not in e]


def main():
    os.makedirs(SHOTS_DESIGN, exist_ok=True)
    os.makedirs(os.path.dirname(OUT_JSON), exist_ok=True)

    # 1. serve the delivery
    server_proc = subprocess.Popen(
        [sys.executable, "-m", "http.server", str(PORT)],
        cwd=PILOT_DIR,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    print("http.server pid=%d serving %s on :%d" % (server_proc.pid, PILOT_DIR, PORT))
    deadline = time.time() + 10
    up = False
    while time.time() < deadline:
        try:
            urllib.request.urlopen("http://127.0.0.1:%d/" % PORT, timeout=1)
            up = True
            break
        except Exception:
            time.sleep(0.3)
    if not up:
        print("WARNING: http.server did not come up within 10s; continuing anyway")

    reference = {
        "measured": "2026-09-25",
        "method": "docs/ks4/pilot-inventory/measure_design.py, headless Chrome via ks3_browser.py",
        "widths": WIDTHS,
        "routes": ROUTES,
        "default_route": DEFAULT_ROUTE,
        "lessons": {},
    }

    browser = cdp.Browser()
    print("chrome launched, browser pid tracked internally by ks3_browser.Browser")
    try:
        page = browser.page("about:blank")
        lessons = LESSONS
        if os.environ.get("MRB_SMOKE"):
            lessons = LESSONS[: int(os.environ["MRB_SMOKE"])]
        for slug, filename in lessons:
            url = "http://127.0.0.1:%d/KS4%%20Lessons/Pilot%%20-%%20Bonding%%20and%%20Electricity/%s" % (
                PORT,
                filename.replace(" ", "%20"),
            )
            print("=== %s (%s) ===" % (slug, filename))
            lesson_entry = {"file": filename, "routes": {}}

            # deep pass: default route across all widths
            widths_data, page = measure_widths_for_route(page, url, DEFAULT_ROUTE, WIDTHS)
            lesson_entry["routes"][DEFAULT_ROUTE] = {"widths": widths_data}
            lesson_entry["console_errors_default_route"] = console_errors_filtered(page)

            # styles (light) at 1280, still on default route — light was
            # already forced inside measure_widths_for_route, but re-assert:
            # nothing here should read Chrome's silent dark default.
            set_media(page, scheme="light")
            page.set_viewport(1280, 1000)
            time.sleep(0.3)
            lesson_entry["styles_light"] = measure_styles(page, 1280)

            # dark mode
            set_media(page, scheme="dark")
            time.sleep(0.4)
            lesson_entry["styles_dark"] = measure_styles(page, 1280)

            # reduced motion — direct proof, not a note. [data-arrive] is the
            # shared Ks4Choice reveal-arrival wrapper (Ks4Choice.dc.html: `@media
            # (prefers-reduced-motion: reduce) { [data-arrive] { animation: none
            # !important; } }`). Commit the hook under normal motion, read its
            # computed animation-name; reload, force reduced motion, commit again,
            # read it again. NOTES-KS4-pilot.md claims a swap-to-instant on every
            # animated instrument — this proves it for the one shared mechanism
            # every lesson's hook uses, per-lesson.
            set_media(page, scheme="light")
            page.goto(url, settle=0.8)
            set_media(page, scheme="light")
            wait_mounted(page)
            page.set_viewport(1280, 1000)
            page.eval("(function(){const el=document.querySelector('#s-hook button'); if(el){el.scrollIntoView();el.click();}})()")
            time.sleep(0.5)
            anim_normal = page.eval(
                "(()=>{const e=document.querySelector('#s-hook [data-arrive]'); return e?getComputedStyle(e).animationName:null;})()"
            )
            page.goto(url, settle=0.8)
            set_media(page, scheme="light", motion="reduce")
            wait_mounted(page)
            page.set_viewport(1280, 1000)
            page.eval("(function(){const el=document.querySelector('#s-hook button'); if(el){el.scrollIntoView();el.click();}})()")
            time.sleep(0.5)
            anim_reduced = page.eval(
                "(()=>{const e=document.querySelector('#s-hook [data-arrive]'); return e?getComputedStyle(e).animationName:null;})()"
            )
            lesson_entry["reduced_motion"] = {
                "hook_reveal_animation_name_normal_motion": anim_normal,
                "hook_reveal_animation_name_reduced_motion": anim_reduced,
                "swaps_instantly": (anim_reduced == "none") and (anim_normal not in (None, "none")),
            }

            # back to explicit light for everything that follows
            set_media(page, scheme="light")
            time.sleep(0.2)

            # interactions (fresh nav, default route, 1280, explicit light)
            page.goto(url, settle=0.8)
            set_media(page, scheme="light")
            wait_mounted(page)
            page.eval(JS_HELPERS)
            lesson_entry["interactions"] = measure_interactions(page, 1280)

            # keyboard focusables at 1280 (fresh nav to reset any state)
            page.goto(url, settle=0.8)
            set_media(page, scheme="light")
            wait_mounted(page)
            page.set_viewport(1280, 1000)
            time.sleep(0.3)
            lesson_entry["keyboard_1280"] = measure_focusables(page)

            # key note lines + full (paginated) question-bank count, fresh nav
            page.goto(url, settle=0.8)
            set_media(page, scheme="light")
            wait_mounted(page)
            page.set_viewport(1280, 1000)
            time.sleep(0.3)
            lesson_entry["key_note"] = measure_keynote(page)
            lesson_entry["question_bank"] = measure_bank_full(page)

            # screenshots: TH light, 1280 and 360
            page.goto(url, settle=0.8)
            set_media(page, scheme="light")
            wait_mounted(page)
            shot1280 = os.path.join(SHOTS_DESIGN, "%s-1280.png" % slug)
            shot360 = os.path.join(SHOTS_DESIGN, "%s-360.png" % slug)
            try:
                page.screenshot(shot1280, width=1280)
                page.screenshot(shot360, width=360)
            except Exception as e:
                print("  screenshot failed: %s" % e)

            # other routes: 1280 only, lighter pass (explicit light throughout,
            # forced inside measure_widths_for_route on its own goto)
            for route in ROUTES:
                if route == DEFAULT_ROUTE:
                    continue
                widths_data, page = measure_widths_for_route(page, url, route, [1280])
                lesson_entry["routes"][route] = {"widths": widths_data}

            reference["lessons"][slug] = lesson_entry
            print("  sections(TH,1280)=%d overflow(390)=%s errors=%d" % (
                len(widths_data and lesson_entry["routes"][DEFAULT_ROUTE]["widths"]["1280"]["sections"] or []),
                lesson_entry["routes"][DEFAULT_ROUTE]["widths"]["390"]["overflow"]["overflow"],
                len(lesson_entry["console_errors_default_route"]),
            ))
    finally:
        try:
            browser.close()
        except Exception:
            pass
        try:
            server_proc.send_signal(signal.SIGTERM)
            server_proc.wait(timeout=5)
        except Exception:
            try:
                server_proc.kill()
            except Exception:
                pass
        print("killed http.server pid=%d" % server_proc.pid)

    with open(OUT_JSON, "w") as fh:
        json.dump(reference, fh, indent=2)
    print("wrote %s" % OUT_JSON)


if __name__ == "__main__":
    main()
