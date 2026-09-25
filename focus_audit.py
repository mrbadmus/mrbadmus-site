#!/usr/bin/env python3
"""focus_audit.py — keyboard focus VISIBILITY audit.

    python3 focus_audit.py                  # every registered page
    python3 focus_audit.py student teacher   # only pages whose key contains a token
    python3 focus_audit.py --shots DIR       # also saves a handful of named
                                              # screenshots into DIR (1280 + 390)

Defect this exists to catch (found on production, 24 Sep 2026): a keyboard
user can Tab to a control on the student class page and see NOTHING change —
no outline, no box-shadow, no background, no border — because most controls
on the ported student/teacher pages are `<button style="all:unset;...">`
(Design's compiled markup keeps `all:unset` byte-identical, see
`build_student_port.py`'s module docstring) and an inline style beats any
stylesheet selector regardless of specificity, `:focus-visible` included.

── STREAM G FOLLOW-UP, 25 Sep 2026 — TWO CORRECTIONS TO THE METHOD ───────

The first version of this gate reported two false positives on the merged
tree, both worth naming because the fix for each is a different kind of
"measure truthfully" than the ring defect above:

1. `ks3_lesson` "failed" because the chat panel's close/image/input/send
   controls were "UNREACHED". They are unreached AT REST because the panel
   is `inert` while closed (`shared/mrbadmus.v2.js`'s own comment on
   `open()`: "hides it from the eye and the mouse and NOT from the
   keyboard... A page that ships the overlay `inert` opts into having it
   managed here") — Tab cannot reach an `inert` subtree by design, and
   reporting that as a defect was measuring the WRONG THING. Elements
   inside `[inert]` are now excluded from the "expected reachable" set
   entirely (§SCAN_JS), and pages that carry a chat panel get a SEPARATE,
   explicit check: open it with a real click, Tab through it, confirm all
   four controls are reached and ring, confirm Tab cannot escape it
   (`shared/mrbadmus.v2.js` now traps Tab inside `#chatOverlay` while it is
   open, the same pattern `shared/set-work.js`'s sheet already used), and
   confirm Escape closes it and returns focus to whichever button opened it
   (also new — `close()` used to drop focus on `<body>`).

2. `student_assignment` "failed" with unreached/no-change controls that
   were neither: `shared/student-runtime.js`'s `draw()` empties the whole
   mount and rebuilds it from scratch on an async data resolve, which used
   to strip every `data-mrb-fa` attribute this gate wrote, mid-sweep, and
   read as "Tab never reached these" for controls that were simply GIVEN
   NEW DOM NODES under Tab's feet. Elements are no longer identified by an
   attribute this gate writes once; each scan computes a STABLE KEY per
   element — `tag :: visible text :: position among duplicates of that
   pair` — and the candidate list is RE-SCANNED after every single Tab
   press. A `draw()` that re-renders the same visible content in the same
   order produces the same keys on the new nodes, so tracking survives the
   replacement it used to be defeated by.

── METHOD ──────────────────────────────────────────────────────────────

For every target page:

  1. Load it, let it settle, and — for anything with a SPA mount id — poll
     until the mount has actually rendered (`wait_for_mount`).
  2. Scan for every plausible Tab stop (the same selector shape
     `shared/set-work.js`'s own focus trap uses, PLUS `[role="button"]`/
     `[role="tab"]`/`[role="menuitem"]`/`[contenteditable]`), excluding
     anything inside an `[inert]` ancestor, and key each one by
     `tag::label::n`. Repeat until two consecutive scans agree (the tree
     has stopped moving) — this is the BASELINE.
  3. Press a REAL Tab key, N times, through `Input.dispatchKeyEvent`
     (`rawKeyDown` + `keyUp` — Tab has no `char` event). A JS-dispatched
     `KeyboardEvent` would not move focus at all (untrusted events run no
     default action), so this has to be a genuine input-layer press, the
     same reasoning `set_work_drive.py`'s `press_space` uses for Space.
  4. After EVERY press, RE-SCAN (not re-read a stale tag) and read which
     candidate — by key — is `document.activeElement`. Compare its style
     against that same key's style from the PREVIOUS scan (which was
     necessarily unfocused, since focus just arrived this press). Any of
     outline/box-shadow/background/border/colour/text-decoration differing
     counts as a visible change; all unchanged is the defect this reports.
     Keys seen in ANY scan across the whole sweep count as "expected", so a
     control a redraw only introduced partway through still has to be
     reached.
  5. Separately, once per page (not per press — nothing here needs
     redraw-tracking), scan for elements that look interactive (`onclick`,
     `cursor:pointer`, and not already inside `[inert]`) but carry no
     tabindex and aren't naturally focusable — a keyboard user cannot reach
     these AT ALL, regardless of ring.
  6. If the page carries `#chatOverlay`, additionally: click its
     `[data-open-chat]` launcher for real, confirm the panel opens, Tab
     through it (redraw-robust, same as step 4, scoped to the panel) and
     confirm every one of its controls is reached and rings, confirm Tab
     cannot walk out of it, then press Escape and confirm the panel closes
     AND focus returns to the launcher.

A "composer"/overlay page (the Set work sheet) is opened first via its own
public JS seam (`MRB_SET_WORK_OPEN('')`, the same function the page's own
"Set work" buttons call) so the audit measures the sheet's real controls,
not the page behind it.

Exit code is 1 if any page has an unreached-by-order problem, a
no-visible-change control, or a failed chat-panel check; 0 otherwise.
`--shots` never affects the exit code — it is a reporting side effect for
the run's screenshots.
"""

import json
import os
import sys
import time

REPO = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, REPO)
import ks3_browser as cdp  # noqa: E402

MAX_TABS = 200  # a generous cap; the busiest fixture here has ~80 stops


# ── the scan: candidates (keyed, styled, redraw-survivable) + who's active ─
#
# ⚠️ ONE SELECTOR, deliberately the same shape `shared/set-work.js`'s own
# `FOCUSABLE` constant uses (`button,[href],input,select,textarea,
# [tabindex]`), widened with the ARIA-role and contenteditable cases a
# custom control can carry instead of a native tag. Anything hidden,
# zero-sized, `disabled`/`tabindex="-1"`, or inside `[inert]` is excluded —
# Tab could never reach any of those either.
#
# ⚠️ THE KEY IS CONTENT, NOT AN ATTRIBUTE THIS SCRIPT WROTE. `tag :: label ::
# n` (n = how many earlier candidates in DOM order share the same tag+label)
# survives a `draw()` that discards the DOM node and replaces it with a new
# one rendering the same thing in the same order — which is exactly the
# shape `shared/student-runtime.js` tears pages down and rebuilds them in.
# An attribute tag does not survive that; content does.
SCAN_JS = r"""
(function () {
  var sel = 'button,[href],input,select,textarea,[tabindex],' +
            '[role="button"],[role="tab"],[role="menuitem"],' +
            '[role="link"],[contenteditable="true"]';
  var scope = %(scope)s;
  var root = scope ? document.querySelector(scope) : document;
  if (!root) { return JSON.stringify({error: 'scope not found: ' + scope}); }
  var nodes = Array.prototype.slice.call(root.querySelectorAll(sel));
  var active = document.activeElement;
  function styleOf(cs) {
    return {
      outline: [cs.outlineWidth, cs.outlineStyle, cs.outlineColor].join(' '),
      boxShadow: cs.boxShadow,
      background: cs.backgroundColor,
      border: [cs.borderTopWidth, cs.borderTopStyle,
               cs.borderTopColor].join(' '),
      color: cs.color,
      textDecoration: cs.textDecorationLine
    };
  }
  var counts = {};
  var out = [];
  nodes.forEach(function (el) {
    var r = el.getBoundingClientRect();
    if (!r.width || !r.height) { return; }
    var cs = getComputedStyle(el);
    if (cs.visibility === 'hidden' || cs.display === 'none') { return; }
    if (el.disabled) { return; }
    var ti = el.getAttribute('tabindex');
    if (ti !== null && parseInt(ti, 10) < 0) { return; }
    // Stream G follow-up — an `inert` ancestor removes an element from the
    // tab order BY DESIGN (the closed chat panel's `data-inert-when-closed`
    // is exactly this); it is not a reachability defect and does not belong
    // in the "expected reachable at rest" set at all.
    if (el.closest('[inert]')) { return; }
    var label = (el.innerText || el.getAttribute('aria-label') ||
                 el.getAttribute('title') || el.getAttribute('placeholder') ||
                 '').trim().replace(/\s+/g, ' ').slice(0, 60);
    var base = el.tagName.toLowerCase() + '::' + (label || '(no label)');
    var n = counts[base] || 0;
    counts[base] = n + 1;
    out.push({
      key: base + '::' + n,
      tag: el.tagName.toLowerCase(),
      cls: (el.getAttribute('class') || '').slice(0, 60),
      label: label || '(no label)',
      style: styleOf(cs),
      active: el === active
    });
  });
  return JSON.stringify({candidates: out});
})()
"""

# Run ONCE per page (not per Tab press — nothing about a redraw changes what
# this measures, and it is the expensive full-DOM sweep of the two).
UNREACHABLE_JS = r"""
(function () {
  var sel = 'button,[href],input,select,textarea,[tabindex],' +
            '[role="button"],[role="tab"],[role="menuitem"],' +
            '[role="link"],[contenteditable="true"]';
  var scope = %(scope)s;
  var root = scope ? document.querySelector(scope) : document;
  if (!root) { return JSON.stringify({error: 'scope not found: ' + scope}); }
  var suspects = [];
  var all = root.querySelectorAll('*');
  for (var j = 0; j < all.length && suspects.length < 200; j++) {
    var e = all[j];
    if (e.closest('[inert]')) { continue; }  // unreachable BY DESIGN, not a defect
    if (e.closest(sel)) { continue; }  // it or an ancestor is already a
                                        // real Tab stop — a decorative
                                        // icon/label inside a button is
                                        // not a separate defect
    var hasClick = !!e.getAttribute('onclick');
    var cur = getComputedStyle(e).cursor === 'pointer';
    if (!hasClick && !cur) { continue; }
    var rr = e.getBoundingClientRect();
    if (!rr.width || !rr.height) { continue; }
    // Only the OUTERMOST clickable-looking element counts. A `cursor:
    // pointer` card commonly wraps a name, an avatar and a stat line, each
    // of which also computes `pointer` by inheritance — reporting all of
    // them for one real click target is noise, not N defects.
    var dup = false, anc = e.parentElement;
    while (anc && anc !== root.parentElement) {
      if (getComputedStyle(anc).cursor === 'pointer' ||
          anc.getAttribute('onclick')) { dup = true; break; }
      anc = anc.parentElement;
    }
    if (dup) { continue; }
    suspects.push({
      tag: e.tagName.toLowerCase(),
      cls: (e.getAttribute('class') || '').slice(0, 60),
      label: (e.innerText || '').trim().replace(/\s+/g, ' ').slice(0, 40)
    });
  }
  return JSON.stringify({unreachable_candidates: suspects});
})()
"""


def press_tab(p, shift=False):
    """A REAL Tab key through CDP — see press_space() in set_work_drive.py
    for why a JS-dispatched KeyboardEvent cannot stand in for this: an
    untrusted event runs no default action, so focus would never move."""
    mods = 8 if shift else 0  # CDP modifier bit: Shift = 8
    common = {"key": "Tab", "code": "Tab", "windowsVirtualKeyCode": 9,
              "nativeVirtualKeyCode": 9, "modifiers": mods}
    p.send("Input.dispatchKeyEvent", dict(common, type="rawKeyDown"))
    p.send("Input.dispatchKeyEvent", dict(common, type="keyUp"))
    time.sleep(0.06)


def press_escape(p):
    """A REAL Escape key — same reasoning as press_tab."""
    common = {"key": "Escape", "code": "Escape", "windowsVirtualKeyCode": 27,
              "nativeVirtualKeyCode": 27}
    p.send("Input.dispatchKeyEvent", dict(common, type="rawKeyDown"))
    p.send("Input.dispatchKeyEvent", dict(common, type="keyUp"))
    time.sleep(0.15)


# ⊕ experience run, 25 Sep 2026 (Mide's item 3) — a named key press through
# CDP, generalised out of `press_tab`/`press_escape` rather than adding a
# third near-duplicate: `audit_pupil_reach` below needs ArrowDown, ArrowUp
# and Enter, and a JS-dispatched `KeyboardEvent` cannot stand in for any of
# them for the same reason it cannot for Tab (untrusted, runs no default
# action) — Enter's default action is irrelevant here since the app's own
# `keydown` listener reads `e.key` itself, but the other two still move a
# CSS class this way and nowhere else.
_KEYS = {
    "ArrowDown": (40, 40), "ArrowUp": (38, 38), "Enter": (13, 13),
}


def press_key(p, key):
    vk, nvk = _KEYS[key]
    common = {"key": key, "code": key, "windowsVirtualKeyCode": vk,
              "nativeVirtualKeyCode": nvk}
    p.send("Input.dispatchKeyEvent", dict(common, type="rawKeyDown"))
    p.send("Input.dispatchKeyEvent", dict(common, type="keyUp"))
    time.sleep(0.1)


def audit_pupil_reach(browser, port):
    """Mide's item 3 (this experience run): "a keyboard-only teacher cannot
    open Lydia's or Annabel's page at all." Two things the AT-REST sweep in
    `audit_page` cannot see, because both only exist once the overlay is
    open: the search box taking focus on open, and the result list
    answering the arrow keys and Enter as a listbox. (The four `tabindex="0"`
    cards/rows — the OTHER half of item 3 — ARE at-rest controls and are
    already proven by the ordinary `teacher_classes`/`teacher_class_detail`
    sweep above; this function is the part that sweep structurally cannot
    reach.)

    Two fresh pages, not one, because `Enter` on a result row is a REAL
    `MRB_GO` navigation — the page under test is gone once it fires, so the
    Escape half needs its own page opened after it, exactly as
    `audit_chat_panel` gets a clean page per call rather than reusing one
    mid-navigation.

    Returns a dict of booleans/counts; `main()` turns it into pass/fail.
    """
    url = "http://127.0.0.1:%d/teacher_fixtures/class-detail-fixture.html" % port

    p1 = browser.page(url)
    reach = _pupil_reach_drive(p1)

    p2 = browser.page(url)
    esc = _pupil_escape_drive(p2)

    reach.update(esc)
    return reach


def _pupil_reach_drive(p):
    wait_for_mount(p, "mrb-teacher")

    if not real_click(p, ".mrb-findbtn"):
        return {"fail": "could not click the Find-a-student trigger"}
    time.sleep(0.2)

    # ⚠️ NOT `.offsetParent` — the overlay is `position:fixed` (it has to
    # be, to sit over the whole page), and a fixed element's `offsetParent`
    # is `null` by spec whether or not it is on screen. `getBoundingClientRect`
    # is what `real_click`/`SCAN_JS` already use for "is this actually
    # visible" for the same reason.
    opened = p.eval(
        "(function(){var el=document.querySelector("
        "'[data-port-region=\"overlay-search\"]');"
        "if(!el) return false; var r=el.getBoundingClientRect();"
        "return r.width>0 && r.height>0;})()")
    if not opened:
        return {"fail": "clicking Find a student did not open the overlay"}

    focused_input = p.eval(
        "(function(){var box=document.querySelector("
        "'[data-port-region=\"overlay-search\"]');"
        "var input=box&&box.querySelector('input');"
        "return !!(input && document.activeElement===input);})()")

    rows_at_open = p.eval(
        "document.querySelectorAll('[data-port-region=\"overlay-search\"] "
        "[data-dc-tpl=\"665\"]').length")

    press_key(p, "ArrowDown")
    active_after_one = p.eval(
        "(function(){var a=document.querySelector('[data-dc-tpl=\"665\"]"
        ".mrb-active');return a?a.textContent.trim().slice(0,40):null;})()")

    press_key(p, "ArrowDown")
    active_after_two = p.eval(
        "(function(){var a=document.querySelector('[data-dc-tpl=\"665\"]"
        ".mrb-active');return a?a.textContent.trim().slice(0,40):null;})()")
    moved = bool(active_after_one) and active_after_two != active_after_one

    url_before = p.eval("window.location.href")
    press_key(p, "Enter")
    time.sleep(0.2)
    url_after = p.eval("window.location.href")
    # ⚠️ MATCHED URL-ENCODED TOO, AND ON PURPOSE. This fixture has no real
    # signed-in session, so `MRB_GO`'s real `window.location.href` write
    # takes the browser to the REAL `/teacher/student-detail.html`, which
    # then redirects to `auth.html?return=...` for exactly the same reason
    # any other page on this site would with nobody signed in. That
    # redirect is proof the navigation fired with the right target, not a
    # different outcome from it — the intended URL is encoded inside
    # `return=`.
    enter_navigated = (url_after != url_before) and (
        "student=" in url_after or "student%3D" in url_after)

    return {
        "focused_input": focused_input,
        "rows_at_open": rows_at_open,
        "active_after_one": active_after_one,
        "moved_on_second_arrow": moved,
        "enter_navigated": enter_navigated,
        "url_after_enter": url_after,
    }


def _pupil_escape_drive(p):
    wait_for_mount(p, "mrb-teacher")
    real_click(p, ".mrb-findbtn")
    time.sleep(0.2)
    press_escape(p)
    time.sleep(0.15)
    closed = not p.eval(
        "(function(){var el=document.querySelector("
        "'[data-port-region=\"overlay-search\"]');"
        "if(!el) return false; var r=el.getBoundingClientRect();"
        "return r.width>0 && r.height>0;})()")
    returned = p.eval(
        "!!(document.activeElement && "
        "document.activeElement.classList.contains('mrb-findbtn'))")
    return {"closed_on_escape": closed, "focus_returned": returned}


def real_click(p, selector):
    """A REAL mouse click at the centre of `selector`'s first match, through
    CDP — the chat launcher's `open()` reads `document.activeElement` to
    remember who to give focus back to, and a click is what a keyboard-free
    user actually does; a synthetic `.click()` also skips the native
    focus-on-click a real button press gives for free."""
    sel_json = json.dumps(selector)
    # ⚠️ SCROLL AND MEASURE ARE TWO SEPARATE ROUND-TRIPS, NOT ONE. `styles.css`
    # sets `html{scroll-behavior:smooth}` sitewide, and even
    # `scrollIntoView({behavior:'instant'})` was observed to leave
    # `getBoundingClientRect()` reporting the PRE-scroll position when read
    # in the same script execution right after it, on the KS3 lesson page —
    # the click landed, hit whatever was under the button's old position,
    # and silently did nothing. Splitting them across two `eval()` calls
    # (each a real CDP round-trip) reliably lets the scroll actually land
    # before the position is measured.
    scrolled = p.eval(
        "(function(){var el=document.querySelector(%s); if(!el) return false;"
        "el.scrollIntoView({block:'center', behavior:'instant'}); return true;})()"
        % sel_json)
    if not scrolled:
        return False
    time.sleep(0.08)
    rect = p.eval(
        "(function(){var el=document.querySelector(%s); if(!el) return null;"
        "var r=el.getBoundingClientRect(); return [r.x+r.width/2, r.y+r.height/2];})()"
        % sel_json)
    if not rect:
        return False
    x, y = rect
    p.send("Input.dispatchMouseEvent", {"type": "mouseMoved", "x": x, "y": y})
    p.send("Input.dispatchMouseEvent",
           {"type": "mousePressed", "x": x, "y": y, "button": "left", "clickCount": 1})
    p.send("Input.dispatchMouseEvent",
           {"type": "mouseReleased", "x": x, "y": y, "button": "left", "clickCount": 1})
    time.sleep(0.1)
    return True


def styles_differ(a, b):
    for k in ("outline", "boxShadow", "background", "border", "color",
              "textDecoration"):
        if a.get(k) != b.get(k):
            return True
    return False


def wait_for_mount(page, mount_id, seconds=40.0, poll=0.25):
    """Poll until an SPA mount has actually rendered children. Same shape as
    student_controls_drive.wait_for_mount; duplicated rather than imported
    because that module drives a different fixture set with its own CLI."""
    end, last = time.time() + seconds, 0
    expr = ("(function(){var h=document.getElementById(%r);"
            "return h?h.getElementsByTagName('*').length:-1;})()" % mount_id)
    while time.time() < end:
        n = page.eval(expr)
        n = n if isinstance(n, int) else 0
        if n > 20 and n == last:
            return n
        last = n
        time.sleep(poll)
    return last


def wait_js_condition(page, expr, seconds=10.0, poll=0.15):
    end = time.time() + seconds
    while time.time() < end:
        if page.eval(expr):
            return True
        time.sleep(poll)
    return False


def scan(p, scope_json):
    raw = p.eval(SCAN_JS % {"scope": scope_json})
    try:
        return json.loads(raw)
    except (TypeError, ValueError):
        return {"error": "could not parse scan result: %r" % (raw,)}


def capture_stable_scan(p, scope_json, tries=8, wait=0.4):
    """Scan, but only trust it once the tree has stopped being torn down and
    redrawn out from under us.

    ⚠️ THIS IS NOT PARANOIA. `shared/student-runtime.js`'s `draw()` empties
    the whole mount host and rebuilds it from scratch on every `setState` —
    the class/assignment pages fire an async data read right after first
    paint and redraw once it resolves. Content-based keys survive a redraw
    that reproduces the same content in the same order; they do NOT survive
    one still IN PROGRESS, caught mid-teardown with half the tree gone. So
    this still polls until two consecutive scans agree on the same set of
    keys, in the same order, before treating the result as the baseline —
    the ONGOING robustness (surviving a redraw that happens mid-sweep, after
    this baseline) comes from re-scanning on every Tab press instead, in
    `audit_page` below.
    """
    prev = None
    data = {}
    for _ in range(tries):
        data = scan(p, scope_json)
        if "error" in data:
            return data
        sig = tuple(c["key"] for c in data["candidates"])
        if sig == prev and sig:
            return data
        prev = sig
        time.sleep(wait)
    return data if "error" not in data else data


def sweep_tabs(p, scope_json, presses, seen, expected, prev_style):
    """Press Tab `presses` times, re-scanning (scoped to `scope_json`) after
    every single press, tracking which KEYS get focused and whether each
    one's style changed from its own last-seen unfocused reading.

    Mutates and returns (seen, expected, prev_style, visited, no_change) —
    `seen`/`expected`/`prev_style` are threaded through so a caller can
    keep sweeping (e.g. the chat-panel check re-uses this after its own
    initial scan) without losing what came before.
    """
    visited = set()
    no_change = []
    no_change_keys = set()
    escaped = 0

    for _ in range(presses):
        press_tab(p)
        data = scan(p, scope_json)
        if "error" in data:
            continue
        cur_by_key = {c["key"]: c for c in data["candidates"]}
        for k, c in cur_by_key.items():
            seen[k] = c
        expected |= set(cur_by_key)
        active_c = next((c for c in data["candidates"] if c["active"]), None)
        if active_c is not None:
            k = active_c["key"]
            visited.add(k)
            if k not in no_change_keys:
                base_style = prev_style.get(k)
                if base_style is not None and not styles_differ(base_style, active_c["style"]):
                    no_change_keys.add(k)
                    no_change.append(active_c)
        else:
            escaped += 1
        prev_style = cur_by_key

    return seen, expected, prev_style, visited, no_change, escaped


# ── the chat panel: opened for real, Tab-trapped, and returns focus ───────

CHAT_HAS_JS = "!!document.getElementById('chatOverlay')"


def audit_chat_panel(p):
    """The chat panel is `inert` at rest, so its controls are correctly
    excluded from the "at rest" sweep above (see the module docstring). This
    is the SEPARATE check the coordinator asked for: open it for real, Tab
    through it, confirm the trap `shared/mrbadmus.v2.js` now implements
    holds, and confirm Escape both closes the panel and gives focus back to
    whichever button opened it.

    Returns None if the page has no chat panel at all; otherwise a dict —
    see `main()` for how it is turned into pass/warn/fail lines.
    """
    if not p.eval(CHAT_HAS_JS):
        return None

    # ⚠️ TWO SHAPES, NOT ONE. KS3 lesson pages give the launcher
    # `[data-open-chat]` (build_ks3.py's `.ks3-tutor-cta`); the KS4/root
    # `.chat-fab` button instead carries a bare `onclick="MrBadmus.open()"`
    # (index.html) — the same widget, wired two different ways depending on
    # which generator wrote the page. Missing the second shape is exactly
    # the kind of false "no launcher" this pass exists to stop reporting.
    marked = p.eval("""(function(){
      var els = document.querySelectorAll(
        '[data-open-chat], [onclick*="MrBadmus.open"]');
      for (var i=0;i<els.length;i++){
        var r = els[i].getBoundingClientRect();
        if (r.width && r.height){ els[i].setAttribute('data-mrb-launcher-check',''); return true; }
      }
      return false;
    })()""")
    if not marked:
        return {"warn": "chat overlay present but no visible launcher "
                         "([data-open-chat] or onclick=MrBadmus.open) found"}

    if not real_click(p, "[data-mrb-launcher-check]"):
        return {"warn": "could not click the chat launcher"}
    # open()'s own 100ms setTimeout focuses #ci; give it room to land.
    time.sleep(0.25)

    opened = p.eval("(function(){var ov=document.getElementById('chatOverlay');"
                     "return !!(ov && ov.classList.contains('open'));})()")
    if not opened:
        return {"fail": "clicking the launcher did not open #chatOverlay"}

    scope_json = json.dumps("#chatOverlay")
    data = capture_stable_scan(p, scope_json)
    if "error" in data:
        return {"fail": "chat panel: %s" % data["error"]}

    seen = {c["key"]: c for c in data["candidates"]}
    expected = set(seen)
    prev_style = {c["key"]: c["style"] for c in data["candidates"]}

    # A few presses past the panel's own control count, to prove the trap
    # WRAPS rather than merely "hasn't escaped yet" after exactly N presses.
    presses = len(expected) + 4
    seen, expected, prev_style, visited, no_change, escaped = sweep_tabs(
        p, scope_json, presses, seen, expected, prev_style)

    unreached = [seen[k] for k in expected if k not in visited]

    press_escape(p)
    time.sleep(0.15)
    closed = p.eval("(function(){var ov=document.getElementById('chatOverlay');"
                     "return !ov.classList.contains('open');})()")
    returned = bool(p.eval(
        "!!(document.activeElement && document.activeElement.hasAttribute('data-mrb-launcher-check'))"))
    p.eval("(function(){var el=document.querySelector('[data-mrb-launcher-check]');"
           "if(el) el.removeAttribute('data-mrb-launcher-check');})()")

    return {
        "expected_count": len(expected),
        "visited": len(visited),
        "no_change": no_change,
        "unreached": unreached,
        "escaped": escaped,
        "closed": closed,
        "returned_focus": returned,
    }


# ── the page list ───────────────────────────────────────────────────────
#
# `pre_js`, when given, is evaluated once after the page (and its mount, if
# any) has settled, and BEFORE the baseline scan — this is how the Set work
# sheet gets opened before it is measured.

PAGES = [
    dict(key="student_class", url="/student/class-fixture.html",
         mount="mrb-student"),
    dict(key="student_assignment", url="/student/assignment-fixture.html",
         mount="mrb-student"),

    dict(key="teacher_classes", url="/teacher_fixtures/classes-fixture.html",
         mount="mrb-teacher"),
    dict(key="teacher_class_detail",
         url="/teacher_fixtures/class-detail-fixture.html",
         mount="mrb-teacher"),
    dict(key="teacher_student_detail",
         url="/teacher_fixtures/student-detail-fixture.html",
         mount="mrb-teacher"),
    dict(key="teacher_assignment",
         url="/teacher_fixtures/assignment-fixture.html",
         mount="mrb-teacher"),
    dict(key="teacher_digest", url="/teacher_fixtures/digest-fixture.html",
         mount="mrb-teacher"),
    dict(key="teacher_insights",
         url="/teacher_fixtures/insights-fixture.html",
         mount="mrb-teacher"),

    # The Set work sheet: same fixture, opened via its own public seam.
    # `MRB_SET_WORK_OPEN` is the function the page's own "Set work" buttons
    # call (see teacher_fixtures/class-detail-fixture.html) — an empty
    # classId is a real, ruled state (MRB-335: the sheet opens with no
    # class preselected) rather than a synthetic shortcut.
    dict(key="set_work_sheet", url="/teacher_fixtures/class-detail-fixture.html",
         mount="mrb-teacher", pre_js="MRB_SET_WORK_OPEN('');",
         wait_js="!!(document.querySelector('.sw-overlay') && "
                 "document.querySelector('.sw-overlay').offsetParent)",
         scope=".sw-overlay"),

    # Hand-written teacher pages.
    dict(key="teacher_today", url="/teacher/today.html"),
    dict(key="teacher_timetable", url="/teacher/timetable.html"),
    dict(key="teacher_admin", url="/teacher/admin.html"),
    dict(key="teacher_import", url="/teacher/import.html"),

    # Root / public pages.
    dict(key="root_auth", url="/auth.html"),
    dict(key="root_leaderboard", url="/leaderboard.html"),
    dict(key="root_index", url="/index.html"),

    # One representative KS3 lesson page (built output).
    dict(key="ks3_lesson",
         url="/mrbadmus_site/ks3/chemistry/the-periodic-table/mendeleev.html"),
]


def audit_page(browser, port, spec):
    url = "http://127.0.0.1:%d%s" % (port, spec["url"])
    p = browser.page(url)

    if spec.get("mount"):
        wait_for_mount(p, spec["mount"])
    else:
        time.sleep(0.3)

    if spec.get("pre_js"):
        try:
            p.eval(spec["pre_js"])
        except Exception as e:  # noqa: BLE001
            return {"error": "pre_js failed: %s" % e}
    if spec.get("wait_js"):
        wait_js_condition(p, spec["wait_js"])
        time.sleep(0.25)

    scope_json = json.dumps(spec.get("scope")) if spec.get("scope") else "null"
    data = capture_stable_scan(p, scope_json)
    if "error" in data:
        return data

    seen = {c["key"]: c for c in data["candidates"]}
    expected = set(seen)
    prev_style = {c["key"]: c["style"] for c in data["candidates"]}

    # ⚠️ A MARGIN, NOT AN EXACT COUNT. `leaderboard.html` proved why: one
    # press out of a run can land on an element that did not exist at
    # baseline-capture time (a search overlay's input, mounted on focus of
    # the control that opens it) — a REAL control this sweep was never
    # asked to expect yet. Pressing exactly `len(expected)` times then runs
    # out one short of the last real stop, which reads as "unreached" for a
    # control that was never actually unreachable. The margin absorbs a
    # handful of such stops without materially slowing the sweep.
    presses = min(len(expected) + 10, MAX_TABS)
    seen, expected, prev_style, visited, no_change, _escaped = sweep_tabs(
        p, scope_json, presses, seen, expected, prev_style)

    unreached = [seen[k] for k in expected if k not in visited]

    unreach_raw = p.eval(UNREACHABLE_JS % {"scope": scope_json})
    try:
        unreach_data = json.loads(unreach_raw)
    except (TypeError, ValueError):
        unreach_data = {"unreachable_candidates": []}

    result = {
        "count": len(expected),
        "visited": len(visited),
        "no_change": no_change,
        "unreached": unreached,
        "unreachable_candidates": unreach_data.get("unreachable_candidates", []),
    }
    result["chat"] = audit_chat_panel(p)
    return result


def take_named_shots(browser, port, shots_dir):
    """A handful of named before/after-style screenshots for the report —
    not part of the pass/fail contract. `tabs` is a FIXED, checked count per
    target rather than "land on the first tagged control": that landed once
    on an off-screen tooltip card, which proved nothing to a human looking
    at the PNG. A small fixed count lands on an always-in-viewport nav-level
    control at both widths."""
    targets = [
        ("student_class", "/student/class-fixture.html", "mrb-student", None,
         None, None, 2),
        ("teacher_class_detail", "/teacher_fixtures/class-detail-fixture.html",
         "mrb-teacher", None, None, None, 2),
        ("set_work_sheet", "/teacher_fixtures/class-detail-fixture.html",
         "mrb-teacher", "MRB_SET_WORK_OPEN('');",
         "!!(document.querySelector('.sw-overlay') && "
         "document.querySelector('.sw-overlay').offsetParent)", ".sw-overlay",
         2),
    ]
    for name, url, mount, pre_js, wait_js, scope, tabs in targets:
        for width in (1280, 390):
            full = "http://127.0.0.1:%d%s" % (port, url)
            p = browser.page(full)
            if mount:
                wait_for_mount(p, mount)
            if pre_js:
                p.eval(pre_js)
            if wait_js:
                wait_js_condition(p, wait_js)
                time.sleep(0.25)
            scope_json = json.dumps(scope) if scope else "null"
            capture_stable_scan(p, scope_json)
            landed = None
            for _ in range(tabs):
                press_tab(p)
                data = scan(p, scope_json)
                if "error" not in data:
                    landed = next((c for c in data["candidates"] if c["active"]), landed)
            out = os.path.join(shots_dir, "%s-%d.png" % (name, width))
            p.screenshot(out, width=width, height=900, full_page=False)
            print("     shot: %s  (focused: %s)"
                  % (out, (landed or {}).get("tag")))


def print_chat_result(key, chat):
    """Returns True if the chat-panel check found a problem."""
    if chat is None:
        return False
    if "warn" in chat:
        print("       WARN chat panel: %s" % chat["warn"])
        return False
    if "fail" in chat:
        print("       FAIL chat panel: %s" % chat["fail"])
        return True
    bad = (chat["no_change"] or chat["unreached"] or chat["escaped"]
           or not chat["closed"] or not chat["returned_focus"])
    if not bad:
        print("       chat panel ✅  opened for real, %d/%d control(s) "
              "reached and ringed, Tab could not escape it, Esc closed it "
              "and returned focus to the launcher"
              % (chat["visited"], chat["expected_count"]))
        return False
    print("       chat panel ❌  %d/%d reached, %d no-visible-change, "
          "%d unreached, escaped-the-trap %s, closed-on-Esc %s, "
          "focus-returned-to-launcher %s"
          % (chat["visited"], chat["expected_count"], len(chat["no_change"]),
             len(chat["unreached"]), bool(chat["escaped"]), chat["closed"],
             chat["returned_focus"]))
    for el in chat["no_change"][:10]:
        print("         NO CHANGE  <%s class=%r> %r"
              % (el["tag"], el["cls"], el["label"]))
    for el in chat["unreached"][:10]:
        print("         UNREACHED  <%s class=%r> %r"
              % (el["tag"], el["cls"], el["label"]))
    return True


def main(argv):
    filters = [a for a in argv if not a.startswith("-")]
    shots_dir = None
    if "--shots" in argv:
        shots_dir = argv[argv.index("--shots") + 1]
        os.makedirs(shots_dir, exist_ok=True)

    todo = [pg for pg in PAGES
            if not filters or any(f in pg["key"] for f in filters)]

    print("\nfocus_audit — keyboard focus visibility, %d page(s)\n"
          % len(todo))

    server, port = cdp.serve(REPO)
    failed = 0
    try:
        for spec in todo:
            with cdp.Browser() as b:
                result = audit_page(b, port, spec)
            if "error" in result:
                failed += 1
                print("  %-24s ❌ %s" % (spec["key"], result["error"]))
                continue
            chat = result.pop("chat", None)
            problems = len(result["no_change"]) + len(result["unreached"])
            if problems:
                print("  %-24s ❌ %d/%d visited, %d no-visible-change, "
                      "%d unreached, %d unreachable-candidate(s)"
                      % (spec["key"], result["visited"], result["count"],
                         len(result["no_change"]), len(result["unreached"]),
                         len(result["unreachable_candidates"])))
                for el in result["no_change"][:20]:
                    print("       NO CHANGE  <%s class=%r> %r"
                          % (el["tag"], el["cls"], el["label"]))
                for el in result["unreached"][:10]:
                    print("       UNREACHED  <%s class=%r> %r"
                          % (el["tag"], el["cls"], el["label"]))
                for el in result["unreachable_candidates"][:10]:
                    print("       NOT FOCUSABLE AT ALL  <%s class=%r> %r"
                          % (el["tag"], el["cls"], el["label"]))
            else:
                print("  %-24s ✅  %d/%d control(s), all show a visible "
                      "change on Tab" % (spec["key"], result["visited"],
                                          result["count"]))
            chat_bad = print_chat_result(spec["key"], chat)
            if problems or chat_bad:
                failed += 1

        # ⊕ experience run, 25 Sep 2026 (Mide's item 3) — the part of "reach
        # a pupil by keyboard" the AT-REST sweep above cannot see (see
        # `audit_pupil_reach`'s own docstring). Same filter convention as
        # `todo`: runs unless a filter was given and none of it matches.
        pupil_key = "teacher_pupil_reach"
        if not filters or any(f in pupil_key for f in filters):
            with cdp.Browser() as b:
                pr = audit_pupil_reach(b, port)
            bad = [k for k in ("focused_input", "moved_on_second_arrow",
                                "enter_navigated", "closed_on_escape",
                                "focus_returned")
                   if not pr.get(k)]
            if "fail" in pr:
                failed += 1
                print("  %-24s ❌ %s" % (pupil_key, pr["fail"]))
            elif bad or not pr.get("rows_at_open"):
                failed += 1
                print("  %-24s ❌ focus-on-open %s · %d result row(s) at "
                      "open · arrows moved %s · Enter navigated %s "
                      "(-> %s) · Esc closed %s · focus returned %s"
                      % (pupil_key, pr.get("focused_input"),
                         pr.get("rows_at_open", 0),
                         pr.get("moved_on_second_arrow"),
                         pr.get("enter_navigated"),
                         pr.get("url_after_enter"),
                         pr.get("closed_on_escape"),
                         pr.get("focus_returned")))
            else:
                print("  %-24s ✅  focus lands in the search box on open, "
                      "%d result row(s), the arrow keys move the "
                      "highlighted row, Enter opens the pupil, Esc closes "
                      "and returns focus to \"Find a student\""
                      % (pupil_key, pr["rows_at_open"]))

        if shots_dir:
            print("\n  shots -> %s" % shots_dir)
            with cdp.Browser() as b:
                take_named_shots(b, port, shots_dir)
    finally:
        server.shutdown()

    print()
    if failed:
        print("  FAIL  %d of %d page(s).\n" % (failed, len(todo)))
        return 1
    print("  PASS  every page: every reachable control shows a visible "
          "change on Tab, Tab reaches everything expected, and every "
          "chat panel opens, traps Tab, and returns focus on close.\n")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
