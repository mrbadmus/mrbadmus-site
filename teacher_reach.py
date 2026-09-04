#!/usr/bin/env python3
"""teacher_reach.py — every teacher control REACHABLE on a real phone.

    python3 teacher_reach.py                 # every screen, every state
    python3 teacher_reach.py assignment      # one screen (substring match)
    python3 teacher_reach.py --shots DIR     # also write screenshots

⊕ MRB-306 Phase 3, 4 Sep 2026. Ruled by Mide.

── WHY THIS EXISTS, IN ONE SENTENCE ─────────────────────────────────────

A green overflow probe once passed over a button a teacher could not reach.

── THE LONGER VERSION, BECAUSE THE SHAPE MATTERS MORE THAN THE INSTANCE ─

On 3 Sep 2026 the written-feedback sheet shipped with its footer — the
"Save changes" button, the whole point of the sheet — off the right-hand
edge of the panel at a real 390px. The teacher could open the sheet, type a
paragraph, and have nowhere to press.

⚠️ **THE OVERFLOW PROBE OF THE DAY COULD NOT SEE IT, and it was not a bug in
the probe.** It asked the only question overflow probes ask: does anything
stick out past `document.documentElement.clientWidth`? Nothing did. The
panel is `overflow:auto`, so the footer overflowed THE PANEL and the panel
absorbed it — the document was the right width, every element was in the
DOM, the console was quiet, and the button was unreachable. The defect was
found by taking a photograph and looking at it.

That is a class of failure, not an incident:

    an element being IN THE DOCUMENT is not the same as being ON THE SCREEN,
    and being ON THE SCREEN is not the same as being PRESSABLE.

`teacher_behaviour.py` proves the first two — every screen mounts, every
binding resolves, every control moves something. It drives at 1460x1200,
where nothing is cramped, and it presses controls with `.click()`, which
reaches an element a human's finger cannot. So it cannot see this, and it is
not being asked to: adding a width to it would double a twenty-minute gate
to measure a different property.

This gate measures the third thing, at the widths a phone actually has.

── WHAT "REACHABLE" MEANS HERE, PRECISELY ───────────────────────────────

For every control on the page, at each width:

  1. scroll every SCROLLABLE ANCESTOR — not just the window — so the control
     is brought into its container's view. ⚠️ This is the step the old probe
     had no equivalent of, and it is the step that turns an `overflow:auto`
     panel from a hiding place into a container that can be scrolled;
  2. then take its box. Zero width or zero height is unreachable;
  3. then check the box is INSIDE THE VIEWPORT — a control whose centre is
     at x = 431 on a 390px screen is not reachable however scrolled;
  4. then HIT-TEST at its centre with `document.elementFromPoint`. If
     something else is on top — a sticky footer, a modal scrim, a header
     that follows you down — the control is covered, and covered is
     unreachable. The element that covers it is NAMED, because "unreachable"
     without "behind what" costs an hour.

A control that fails any of the four is reported with which one and where.

── AND IT PRESSES, BECAUSE THE HARD CASES ARE ONLY REACHABLE AFTER A PRESS ─

The Save button that started this is not on the page at rest. It is inside a
sheet that a glyph in a 30-row grid opens. So a sweep of the page as loaded
would have missed it exactly as thoroughly as the overflow probe did.

So this gate drives the same ordinal sweep `teacher_behaviour` does — every
control, re-queried from the live DOM after every press, because the runtime
rebuilds the host wholesale on `setState` and a handle taken before a press
is detached after it — and re-runs the reachability check on EVERYTHING
CURRENTLY ON THE PAGE after every press. Controls it has already cleared are
skipped by signature, so the cost is one extra evaluation per press.

⚠️ IT IS NOT A SECOND DEAD-CONTROL GATE. It does not assert that a press
changes anything; `teacher_behaviour` does that, at a width where the whole
page fits, and duplicating it here would mean two gates going red for one
defect and neither being the one to read. What this gate asserts about the
resulting state is the thing that width DOES decide:

    · every control revealed by a press is itself reachable;
    · nothing renders a computed value (`NaN`, `null%`, `undefined`,
      `[object …]`) at a narrow width that did not at a wide one — a
      different branch of a layout is a different branch of the code;
    · the document never scrolls SIDEWAYS. A page a teacher must pan is a
      page whose controls move under their thumb.

── THE STATES IT DRIVES ─────────────────────────────────────────────────

Every fixture `build_teacher_port.py` writes, DERIVED from `EMPTY_SHAPES`
and `variant_files` rather than listed here — the same rule
`teacher_behaviour.fixtures()` follows, and for the same reason: a
nineteenth fixture must not be able to exist without a gate driving it.

That covers, by name: populated · no classes in the year · a class with no
roster · students but no work set · nobody handed in · a MISSING GRID KEY
(both the key-absent and key-present-null branches — the 26 Aug 2026 live
crash) · a real-shaped written paper · no live class at all · a scoped class
with no roster · one-of-everything · and READ-ONLY on all three screens that
have a write surface, including the marking screen's, which is new in this
unit and which the previous one recorded as missing.

⚠️ TWO OF THE TEACHER'S TEN SCREENS ARE NOT HERE, and it is said rather than
implied. `today.html` and `timetable.html` are HAND-WRITTEN — they have no
fixture machinery to derive from — and `today.html`'s four timetable states,
including the empty one, are driven by `today_drive.py`, which already
includes a 390px case. `admin.html`'s Messages surface is driven by
`admin_view_drive.py`, which signs in for real and is EXCLUDED from the
registry for that reason. Neither of those two does the hit test this file
does; extending them is the next unit, and it is written down in the MRB-306
Phase 3 report rather than left for someone to notice.
"""

import json
import os
import sys

REPO = os.path.dirname(os.path.abspath(__file__))
PAGE_DIR = "teacher_fixtures"

# The widths. 390 is the iPhone the school's children and its teachers
# actually carry; 360 is the commonest Android and is where a 390-clean
# layout most often stops being clean.
WIDTHS = ((390, 844), (360, 780))

# Computed values that must never reach a teacher's screen. Same list as
# teacher_behaviour's, kept in step deliberately: a narrow layout is a
# different branch, and the branch that only runs at 360 has the same right
# to be checked.
RENDER_TELLS = ("NaN", "null%", "undefined", "Infinity", "[object ")


def fixtures():
    """(screen, filename) for every fixture the port writes.

    ⚠️ DERIVED, NOT LISTED. `build_teacher_port.EMPTY_SHAPES` is the
    authority, exactly as it is for `teacher_behaviour.fixtures()`. A
    hand-written copy of the fixture list here would be a second list to
    forget to update, which is the failure `gate_registry.py` exists for one
    level up.
    """
    import build_teacher_port as BTP
    import teacher_behaviour as TB
    by_out = {sp["out"]: sp for sp in BTP.PAGES}
    out = []
    for s in TB.SCREENS:
        spec = by_out["%s.html" % s]
        out.append((s, "%s-fixture.html" % s, "full"))
        for slug, _note, _shaper in BTP.EMPTY_SHAPES[spec["out"]]:
            out.append((s, BTP.variant_files(spec, slug)[0], slug))
    return out


# ── the probe ────────────────────────────────────────────────────────────
#
# One evaluation for the whole sweep, for the reason teacher_behaviour gives:
# the DOM is rebuilt on every `setState`, so a Python-side loop holding
# element handles would be holding handles to elements that no longer exist.
_REACH_JS = r"""
(async function () {
  var host = document.querySelector('#mrb-teacher');
  if (!host) { return JSON.stringify({error: 'no #mrb-teacher host'}); }

  function frame() {
    return new Promise(function (r) {
      requestAnimationFrame(function () { requestAnimationFrame(r); });
    });
  }

  /* ⚑ WAIT FOR THE ANIMATIONS BEFORE MEASURING ANYTHING, and this is not
     politeness — it is the difference between measuring the page and
     measuring a lie about it.

     Every screen root Design drew carries `animation: shin .18s ease-out`,
     and `student-runtime` REBUILDS THE HOST on every `setState` — so that
     animation restarts on every single press. While a transform animation
     is running, the animated element becomes the CONTAINING BLOCK for its
     `position:fixed` descendants. The feedback sheet is `position:fixed;
     inset:0; z-index:60`; for 180ms after each press it is therefore laid
     out against a 3204px-tall screen root instead of against the viewport,
     and a hit test at its Save button's coordinates lands on whatever grid
     row happens to be at that point.

     The first version of this file measured two frames after the press —
     about 32ms into that 180ms — and reported the sheet's Save, Remove,
     Close and textarea as "covered by div 'SI Sana Iqbal …'". Every one of
     those was the probe photographing a page mid-flinch. Nothing was wrong
     with the sheet: opened at rest, its Save button hit-tests to itself.

     Capped, because an INFINITE animation would never resolve and a gate
     that hangs is a gate that gets disabled. */
  function settled() {
    var anims;
    try { anims = document.getAnimations ? document.getAnimations() : []; }
    catch (e) { anims = []; }
    var waits = anims.map(function (a) {
      return a.finished ? a.finished.catch(function () {}) : null;
    }).filter(Boolean);
    var cap = new Promise(function (r) { setTimeout(r, 300); });
    return Promise.race([Promise.all(waits), cap]).then(frame);
  }

  /* Navigation recorded, never followed — same stubs and same reasoning as
     teacher_behaviour: letting one fire would tear the page down mid-sweep
     and take every remaining control with it, and a press that reaches
     MRB_GO has proved it is wired either way. */
  var navs = [];
  window.MRB_GO = function (s, p) { navs.push(s); };
  window.MRB_BACK = function () { navs.push('<back>'); };
  window.MRB_HOME = function () { navs.push('<home>'); };

  function disabledLooking(el) {
    if (el.disabled) { return true; }
    if (el.getAttribute('aria-disabled') === 'true') { return true; }
    var cur = (el.style && el.style.cursor) || '';
    return cur === 'default' || cur === 'not-allowed';
  }

  /* The same definition of "looks pressable" teacher_behaviour uses, and
     `[data-mrb-added]` as well as `[data-dc-tpl]` for the same reason:
     markup this port INSERTS carries no `i`, so it has no `data-dc-tpl`,
     and a sweep keyed on Design's numbering alone cannot see the controls
     the port added. */
  /* ⚑ A MODAL IS MODAL, AND WITHOUT THIS THE GATE LIES IN BOTH DIRECTIONS.
     ⚠️ Found by running it. The ordinal sweep opened the student-search
     overlay (`position:fixed`, z-index 70) and then went on pressing the
     marking grid UNDERNEATH it — `.click()` reaches through a scrim in a way
     a finger cannot — and opened the feedback sheet (z-index 60) beneath the
     search results. The gate then correctly reported the sheet's Save,
     Remove, Close and textarea as covered "by div 'SI Sana Iqbal 7H/SC5
     59%'", which is a search RESULT ROW. Every one of those four was real
     geometry in a state no teacher can reach.

     That is a false alarm and a blind spot at once: while the sweep is
     pressing things behind a scrim it is not pressing the things in FRONT of
     it, which is where the button that started this gate lives.

     So: if a full-screen `position:fixed` scrim is up, the page IS that
     scrim. Only its descendants are pressable, and the topmost one wins —
     which is what a browser does with pointer events anyway. Sized rather
     than named, so it catches Design's four overlays, the port's two sheets
     and any future one, and does not catch the toast (also fixed, 200px
     wide). */
  function modalRoot() {
    var all = host.querySelectorAll('*'), best = null, bestZ = -1;
    for (var i = 0; i < all.length; i++) {
      var el = all[i], cs = getComputedStyle(el);
      if (cs.position !== 'fixed' || cs.visibility === 'hidden') { continue; }
      var r = el.getBoundingClientRect();
      if (r.width < vw * 0.9 || r.height < vh * 0.9) { continue; }
      var z = parseInt(cs.zIndex, 10);
      if (isNaN(z)) { z = 0; }
      if (z >= bestZ) { bestZ = z; best = el; }
    }
    return best;
  }

  function clickable() {
    var scope = modalRoot() || host;
    var all = scope.querySelectorAll('[data-dc-tpl],[data-mrb-added]'),
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

  function label(el) {
    var t = (el.innerText || el.getAttribute('aria-label') ||
             el.getAttribute('title') || el.value || '').trim();
    return t.replace(/\s+/g, ' ').slice(0, 60);
  }

  /* A stable-ish name for a control, so one already cleared is not measured
     again after every one of four hundred presses. Not an identity — the
     runtime rebuilds the node — but the same button in the same place under
     the same words is the same button for this purpose. */
  function sig(el) {
    return el.tagName + '|' + (el.getAttribute('data-dc-tpl') || '') + '|' +
           (el.getAttribute('data-mrb-added') || '') + '|' + label(el);
  }

  /* ⚑ THE STEP THE OLD PROBE HAD NO EQUIVALENT OF. Walk UP from the control
     and scroll every ancestor that can scroll, not just the window. An
     `overflow:auto` panel absorbs its own overflow — the document stays the
     right width and the button stays off the edge of the panel — so a check
     that only scrolls the window is measuring a container it never entered.
     `scrollIntoView` on the element does most of this in one call in modern
     Chrome; the explicit walk is kept because it also handles a HORIZONTAL
     overflow, which is the axis the Save button was lost on and the one
     `block: 'center'` says nothing about. */
  function bringIn(el) {
    var n = el.parentElement;
    while (n && n !== document.body) {
      var cs = getComputedStyle(n);
      var scrolls = /(auto|scroll|overlay)/.test(cs.overflow + cs.overflowX +
                                                 cs.overflowY);
      if (scrolls && (n.scrollWidth > n.clientWidth ||
                      n.scrollHeight > n.clientHeight)) {
        var r = el.getBoundingClientRect(), p = n.getBoundingClientRect();
        if (r.left < p.left) { n.scrollLeft -= (p.left - r.left) + 8; }
        else if (r.right > p.right) { n.scrollLeft += (r.right - p.right) + 8; }
        if (r.top < p.top) { n.scrollTop -= (p.top - r.top) + 8; }
        else if (r.bottom > p.bottom) { n.scrollTop += (r.bottom - p.bottom) + 8; }
      }
      n = n.parentElement;
    }
    try { el.scrollIntoView({block: 'center', inline: 'nearest'}); }
    catch (e) { el.scrollIntoView(); }
  }

  var vw = document.documentElement.clientWidth;
  var vh = document.documentElement.clientHeight;

  /* The four questions, in order, so a failure says WHICH one.
     ⚠️ THE POINT TESTED IS THE CENTRE OF THE VISIBLE PART, NOT THE CENTRE OF
     THE BOX, and getting that wrong was the first version's own defect —
     found by running it. The marking grid's student rows are wider than a
     390px screen by design: they scroll sideways inside their own container,
     and a teacher presses the part in front of them. Their geometric centre
     is at x = -81, so a centre-of-box test called every row on the screen
     unreachable while a finger would have hit all of them.
     A finger presses what it can see, so the test point is the middle of the
     INTERSECTION of the control's box with the viewport — and the
     intersection has to be big enough to aim at: the whole control where the
     control is small, and at least a 24x16 target where it is large. One
     visible pixel is not reachability. */
  function reach(el) {
    bringIn(el);
    var r = el.getBoundingClientRect();
    if (r.width < 1 || r.height < 1) {
      return {ok: false, why: 'has no box (' + Math.round(r.width) + 'x' +
                              Math.round(r.height) + ')'};
    }
    var L = Math.max(r.left, 0), R = Math.min(r.right, vw);
    var T = Math.max(r.top, 0), B = Math.min(r.bottom, vh);
    var visW = R - L, visH = B - T;
    var needW = Math.min(r.width, 24), needH = Math.min(r.height, 16);
    if (visW < needW || visH < needH) {
      return {ok: false, why: 'only ' + Math.max(0, Math.round(visW)) + 'x' +
             Math.max(0, Math.round(visH)) + ' of its ' + Math.round(r.width) +
             'x' + Math.round(r.height) + ' box is on a ' + vw + 'x' + vh +
             ' screen (it needs at least ' + Math.round(needW) + 'x' +
             Math.round(needH) + ' to aim at), after scrolling every ' +
             'scrollable container it sits in'};
    }
    var cx = L + visW / 2, cy = T + visH / 2;
    var hit = document.elementFromPoint(Math.round(cx), Math.round(cy));
    if (!hit) { return {ok: false, why: 'nothing hit-tests at its centre'}; }
    if (hit === el || el.contains(hit) || hit.contains(el)) {
      return {ok: true};
    }
    var who = hit.tagName.toLowerCase() +
              (hit.className && typeof hit.className === 'string'
                 ? '.' + hit.className.split(/\s+/)[0] : '') +
              (label(hit) ? ' ' + JSON.stringify(label(hit)) : '');
    return {ok: false, why: 'covered at its centre by ' + who};
  }

  var cleared = {}, bad = [], checked = 0;

  function anyNew() {
    var list = clickable();
    for (var i = 0; i < list.length; i++) {
      if (!cleared[sig(list[i])]) { return true; }
    }
    return false;
  }

  async function sweepReach(when) {
    /* ⚠️ THE SETTLE IS PAID ONLY WHEN THERE IS SOMETHING NEW TO MEASURE.
       Most of four hundred presses reveal no control this sweep has not
       already cleared, and waiting 300ms after each of them would turn a
       four-minute gate into an hour-long one — which is how a gate stops
       being run. */
    if (!anyNew()) { return; }
    await settled();
    var list = clickable();
    for (var i = 0; i < list.length; i++) {
      var el = list[i], s = sig(el);
      if (cleared[s]) { continue; }
      var got = reach(el);
      checked += 1;
      if (got.ok) { cleared[s] = 1; }
      else {
        cleared[s] = 1;      /* reported once, not once per press */
        bad.push({label: label(el) || '(no label)',
                  tag: el.tagName.toLowerCase(),
                  tpl: el.getAttribute('data-dc-tpl') || null,
                  added: el.getAttribute('data-mrb-added') || null,
                  when: when, why: got.why});
      }
    }
  }

  function pressEl(el) {
    var tg = el.tagName.toLowerCase();
    if (tg === 'input' || tg === 'textarea') {
      el.focus(); el.value = 'zz';
      el.dispatchEvent(new Event('input', {bubbles: true}));
    } else if (tg === 'select') {
      el.focus();
      if (el.options && el.options.length > 1) { el.selectedIndex = 1; }
      el.dispatchEvent(new Event('change', {bubbles: true}));
    } else { el.click(); }
  }

  await sweepReach('at rest');

  /* ⛔ TWO CONTROLS ARE HIT-TESTED AND NOT PRESSED, and they are the two
     `teacher_behaviour.EXEMPT_OFFDOM` already names — `Sign out` and
     `Print`. Neither has a DOM consequence, and on a FIXTURE `signOut`
     genuinely throws: `MrBadmusTeacherGuard` is `undefined` there by
     design (a fixture has no config.js, no SDK and no session), so
     `guard.signOut()` raises inside a click listener, where a try/catch
     around `.click()` cannot see it and Chrome logs it as uncaught.
     ⚠️ EXEMPT FROM BEING PRESSED, NOT FROM BEING MEASURED. Both are still
     swept for reachability like everything else — this gate's whole
     question is whether a teacher can get to them, and an exemption that
     also excused that would hide the defect it exists to find. */
  var NOPRESS = __NOPRESS__;

  /* ⚠️ ADDRESSED BY SIGNATURE, NOT BY ORDINAL, AND THE MODAL RULE IS WHY.
     `teacher_behaviour` walks `list[j]` because its list only ever grows or
     shrinks a little. Here the list COLLAPSES to a modal's five controls the
     moment one opens, so an ordinal walk sitting at j = 20 would find
     `j >= list.length` and end the sweep — silently, having pressed a
     quarter of the page and reported a clean run.
     A signature is not an identity (the runtime rebuilds every node on every
     redraw) but the same button, in the same place, under the same words, is
     the same button for the purpose of "have I pressed this yet". */
  /* ⚑ AND A MODAL HAS TO BE DISMISSED, OR THE SWEEP ENDS INSIDE IT.
     ⚠️ Also found by running it: the run reported "100 controls hit-tested,
     12 pressed" and was green. The student-search overlay has NO close
     button — a teacher dismisses it with Escape or by pressing the scrim —
     so once the sweep had typed into its one field there was nothing left
     in scope, the loop found no unpressed control and stopped, having swept
     a fifth of the page and said so in a passing summary. That is the
     overstated-scope failure `gate_registry.py` was written about, and the
     count being printed is what made it visible.
     Dismissing is what a teacher does, in the order a teacher does it:
     Escape first, then a press on the scrim itself. Capped, so a modal that
     refuses both ends the sweep rather than spinning it. */
  var dismissed = 0;
  async function dismiss() {
    var m = modalRoot();
    if (!m || dismissed >= 12) { return false; }
    dismissed += 1;
    document.dispatchEvent(new KeyboardEvent('keydown',
        {key: 'Escape', code: 'Escape', keyCode: 27, bubbles: true}));
    await frame();
    if (modalRoot() === m) { m.click(); await frame(); }
    return modalRoot() !== m;
  }

  var pressedSig = {}, pressed = 0, errors = [], CAP = 400;
  for (var j = 0; j < CAP; j++) {
    var list = clickable(), c = null;
    for (var q = 0; q < list.length; q++) {
      if (!pressedSig[sig(list[q])]) { c = list[q]; break; }
    }
    if (!c && modalRoot()) {
      if (await dismiss()) { continue; }
    }
    if (!c) { break; }
    pressedSig[sig(c)] = 1;
    var lab = label(c);
    if (NOPRESS.indexOf(lab) === -1) {
      try { pressEl(c); pressed += 1; }
      catch (e) { errors.push(lab + ': ' + (e && e.message)); }
      await frame();
    }
    /* ⚑ AFTER EVERY PRESS, not once at the end. The sheet that started this
       gate is only on the page between the press that opens it and the
       press that closes it, and a check at the end of the sweep would find
       the page back where it started. */
    await sweepReach('after pressing ' + JSON.stringify(lab || '(no label)'));
  }

  /* Sideways scroll, measured after the whole sweep as well as before it: a
     press can open a panel that pushes the page wider, and the page a
     teacher is left holding is the one that matters.
     ⚠️ MEASURED FROM SCROLL POSITION ZERO. The sweep pans the page to bring
     controls into view, and a page scrolled right reports a `scrollWidth`
     that includes where it has been taken to. */
  window.scrollTo(0, window.scrollY);
  await frame();
  var side = document.documentElement.scrollWidth > vw + 1;
  var widest = [];
  if (side) {
    var all = document.querySelectorAll('*');
    for (var k = 0; k < all.length; k++) {
      var rr = all[k].getBoundingClientRect();
      if (rr.width && rr.right > vw + 1) {
        widest.push((all[k].getAttribute('data-dc-tpl') ?
                       'node ' + all[k].getAttribute('data-dc-tpl') :
                       all[k].tagName.toLowerCase()) +
                    ' to ' + Math.round(rr.right) + 'px');
        if (widest.length >= 3) { break; }
      }
    }
  }

  return JSON.stringify({
    bad: bad, checked: checked, pressed: pressed, errors: errors,
    sideways: side, widest: widest,
    docW: document.documentElement.scrollWidth, vw: vw,
    text: (host.innerText || '')
  });
})()
"""


def drive(screen, path, slug, cdp, port, width, height, shots=None):
    """Problems, as strings, for one fixture at one width."""
    problems = []
    what = "%s/%s @%d" % (screen, slug, width)
    with cdp.Browser() as b:
        pg = b.attach()
        # ⚠️ THE VIEWPORT IS SET BEFORE THE NAVIGATION, not after. A page laid
        # out at the default width and then narrowed has already run its
        # mount at the wrong width, and `cqw`-based type does not always
        # re-resolve — this repo has paid for that once already, in
        # student_controls_drive.
        pg.set_viewport(width, height)
        url = "http://127.0.0.1:%d/%s/%s" % (port, PAGE_DIR, path)
        pg.goto(url, settle=1.2)

        if shots:
            pg.screenshot(os.path.join(shots, "%s-%s-%d.png"
                                       % (screen, slug, width)),
                          width=width, height=height, full_page=True)

        import teacher_behaviour as TB
        raw = pg.eval(_REACH_JS.replace(
            "__NOPRESS__", json.dumps(sorted(TB.EXEMPT_LABELS.values()))))
        got = json.loads(raw)
        if got.get("error"):
            return ["%s: %s" % (what, got["error"])], {"checked": 0,
                                                       "pressed": 0}

        for d in got["bad"]:
            problems.append(
                "%s: %s %r (%s) is NOT REACHABLE %s — %s. It is in the "
                "document and it cannot be pressed; that is the failure this "
                "gate exists for."
                % (what, d["tag"], d["label"],
                   d["added"] or ("node " + str(d["tpl"])),
                   d["when"], d["why"]))

        if got["sideways"]:
            problems.append(
                "%s: the document scrolls SIDEWAYS (%dpx of content in a "
                "%dpx viewport; widest: %s). A page a teacher has to pan is "
                "a page whose controls move under their thumb — the content "
                "goes out from under them as they scroll down it."
                % (what, got["docW"], got["vw"],
                   ", ".join(got.get("widest") or []) or "not identified"))

        for tell in RENDER_TELLS:
            if tell in (got.get("text") or ""):
                problems.append(
                    "%s: rendered %r. A narrow layout is a different branch, "
                    "and this one has no guard." % (what, tell))

        for e in got.get("errors") or []:
            problems.append("%s: pressing threw — %s" % (what, e))

        for line in pg.console_errors():
            if "favicon" in line:
                continue
            problems.append("%s: console error — %s" % (what, line[:200]))

    return problems, {"checked": got["checked"], "pressed": got["pressed"]}


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
        print("\nteacher_reach.py: not built — %s\n"
              "  Run `python3 build_teacher_port.py` first."
              % ", ".join(missing))
        return 1

    print("\n📱  teacher_reach — every teacher control reachable on a real "
          "phone\n")
    print("     %d fixture(s) x %s — each control brought into view through "
          "every\n     scrollable container it sits in, then hit-tested at "
          "its own centre\n"
          % (len(todo), " and ".join("%dpx" % w for w, _h in WIDTHS)))

    server, port = cdp.serve(REPO)
    failed = 0
    total = {"checked": 0, "pressed": 0}
    try:
        for screen, path, slug in todo:
            row = []
            fixture_failed = False
            for width, height in WIDTHS:
                problems, tally = drive(screen, path, slug, cdp, port,
                                        width, height, shots)
                total["checked"] += tally["checked"]
                total["pressed"] += tally["pressed"]
                if problems:
                    fixture_failed = True
                    row.extend(problems)
            if fixture_failed:
                failed += 1
                print("     %-16s %-12s ❌ %d problem(s)"
                      % (screen, slug, len(row)))
                for p in row[:8]:
                    print("        · %s" % p)
                if len(row) > 8:
                    print("        · … and %d more" % (len(row) - 8))
            else:
                print("     %-16s %-12s ✅" % (screen, slug))
    finally:
        server.shutdown()

    print()
    if failed:
        print("  FAIL  %d of %d fixture(s).\n" % (failed, len(todo)))
        return 1
    # The counts are printed rather than rounded up to "every control", for
    # the reason teacher_behaviour's summary line records: a gate that
    # overstates what it measured is worse than one that measures less.
    print("  PASS  %d fixture(s) x %d width(s). %d control(s) hit-tested at "
          "their own\n        centre after being scrolled into view, over %d "
          "press(es). Nothing was\n        in the document and out of reach, "
          "no page scrolled sideways, and no\n        computed value reached "
          "the copy at a narrow width.\n"
          % (len(todo), len(WIDTHS), total["checked"], total["pressed"]))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
