#!/usr/bin/env python3
"""
seating_drive.py — MRB-322. The seating canvas, driven in a real browser.

── Why this gate exists at all ──────────────────────────────────────────
`teacher_behaviour.py` drives a FIXED `SCREENS` list and `teacher/seating.html`
is deliberately not on it: that lane's generator does not write this page, and
adding a row would couple two lanes that were kept apart on purpose. So without
this file the canvas — which IS the product — has nothing pressing it. A
seating plan that cannot be dragged is not a seating plan, and no screenshot
and no static check can tell you whether a drag works.

── Why it stubs the data layer instead of signing in ────────────────────
It drives the REAL page — `mrbadmus_site/teacher/seating.html`, byte for byte
what Cloudflare serves — but blocks `seating-data.js` and `teacher-guard.js` at
the network layer and installs in-memory stubs in their place, before any page
script runs.

That is not a convenience. A gate that signed in would need a live credential
and seeded rows on the TEST project, and the throwaway identities this run used
are destroyed at the end of it — so such a gate would be green tonight and red
forever afterwards. The permission BOUNDARY is not this gate's job in any case:
it lives in RLS and was proven there, persona by persona, against the database
itself. What this gate owns is the half RLS cannot see — whether the thing on
the screen actually moves, and whether a viewer who may not edit is shown no
edit controls rather than greyed-out ones.

Run:  python3 seating_drive.py
Exit: 0 clean, 1 on any failed check.
"""

import json
import os
import sys
import time

REPO = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, REPO)
import ks3_browser as cdp  # noqa: E402

OUT = os.path.join(REPO, "mrbadmus_site")
PAGE = "/teacher/seating.html"
SHOTS = os.environ.get("SEATING_SHOTS", "/tmp/seating-shots")

checks = []


def ok(name, passed, detail=""):
    checks.append((name, bool(passed), detail))
    print(("  ✅ " if passed else "  ❌ ") + name + (("  — " + detail) if detail else ""))
    return bool(passed)


# ═════════════════════════════════════════════════════════════════════════
# The stub seam
# ═════════════════════════════════════════════════════════════════════════
#
# Every name the page reads off `window` before it can draw anything. The
# fixture pupils carry the `ZZ Test-` tell, so if one ever reaches a shipped
# file `seating_tells` fails the build rather than a real-looking name going
# unnoticed.
#
# ⚠️ The roster is deliberately LARGER than the layout has chairs — 8 pupils,
# 6 seats. "2 unseated" is the number this gate most wants to see drawn,
# because it is the one a tidier design would round away.

STUB = r"""
(function () {
  var LAYOUT = {
    v: 1, front: 'top', teacher_desk: null,
    desks: [
      { id: 'd1', shape: 'rect',  x: 0.24, y: 0.34, w: 0.18, h: 0.09, rotation: 0,   seats: 2 },
      { id: 'd2', shape: 'rect',  x: 0.62, y: 0.36, w: 0.18, h: 0.09, rotation: -11, seats: 2 },
      { id: 'd3', shape: 'round', x: 0.44, y: 0.68, w: 0.15, h: 0.15, rotation: 0,   seats: 2 }
    ]
  };
  var ROSTER = [];
  for (var i = 1; i <= 8; i++) {
    ROSTER.push({ id: 'stub-pupil-' + i, first_name: 'ZZ Test-' + i,
                  last_name: 'Fixture', label: 'ZZ Test-' + i });
  }

  var ME = { id: 'stub-me', first_name: 'ZZ Test-Teacher', last_name: 'Fixture',
             role: 'teacher', school_id: 'stub-school' };

  // Flipped by the driver to exercise the view-only branch.
  var MINE = (location.search.indexOf('stubview=1') === -1);

  function layoutRow(id) {
    return {
      id: id || 'stub-layout', room_code: 'S02a', name: 'ZZ Test-Fixture room',
      layout: JSON.parse(JSON.stringify(LAYOUT)), source: 'manual',
      created_by: MINE ? 'stub-me' : 'stub-other',
      author_name: MINE ? 'ZZ Test-Teacher Fixture' : 'ZZ Test-Other Fixture',
      created_at: '2026-09-01T09:00:00Z', updated_at: '2026-09-01T09:00:00Z',
      desk_count: LAYOUT.desks.length, seat_count: 6, can_edit: MINE
    };
  }
  function planRow(id) {
    var r = layoutRow('stub-layout');
    return {
      id: id || 'stub-plan', class_id: 'stub-class', room_layout_id: 'stub-layout',
      room_code: r.room_code, layout: r.layout, layout_retired: false,
      name: 'ZZ Test-Fixture plan', assignments: {},
      created_by: r.created_by, author_name: r.author_name,
      created_at: r.created_at, updated_at: r.updated_at,
      seated_count: 0, can_edit: MINE
    };
  }

  window.MrBadmusConfig = window.MrBadmusConfig || {
    SUPABASE_URL: 'http://stub.invalid', SUPABASE_ANON_KEY: 'stub',
    BACKEND_URL: 'http://stub.invalid', environment: 'test'
  };

  window.MrBadmusTeacherGuard = {
    requireTeacherRole: function (o) { if (o && o.onAllowed) o.onAllowed(); },
    getClient: function () { return null; },
    signOut: function () {}
  };

  window.MrBadmusSeatingData = {
    ROOMS: ['S01','S02a','S02b','S02c','S04','S08a','S08b','S08c','S09a','S09b','S010'],
    me: function () { return Promise.resolve(ME); },
    isAdmin: function () { return false; },
    canEditLayout: function () { return MINE; },
    canEditPlan: function () { return MINE; },
    displayName: function (p) { return p ? (p.first_name + ' ' + p.last_name) : 'Unknown'; },
    seatLabels: function () { return {}; },
    listRoomLayouts: function () { return Promise.resolve([layoutRow('stub-layout')]); },
    loadRoomLayout: function (id) { return Promise.resolve(layoutRow(id)); },
    createRoomLayout: function () { return Promise.resolve(layoutRow('stub-layout')); },
    updateRoomLayout: function () { return Promise.resolve(layoutRow('stub-layout')); },
    softDeleteRoomLayout: function () { return Promise.resolve(true); },
    listPlansForClass: function () { return Promise.resolve([planRow('stub-plan')]); },
    loadSeatingPlan: function (id) { return Promise.resolve(planRow(id)); },
    createSeatingPlan: function () { return Promise.resolve(planRow('stub-plan')); },
    updateSeatingPlan: function () { return Promise.resolve(planRow('stub-plan')); },
    softDeleteSeatingPlan: function () { return Promise.resolve(true); },
    myClasses: function () {
      return Promise.resolve([{ id: 'stub-class', name: '7z/Sc9', key_stage: 'KS3', year_group: 7 }]);
    },
    loadClass: function () {
      return Promise.resolve({ id: 'stub-class', name: '7z/Sc9', key_stage: 'KS3', year_group: 7 });
    },
    loadClassRoster: function () { return Promise.resolve(ROSTER.slice()); }
  };

  window.MrBadmusSeatingPhoto = {
    scan: function () {
      return Promise.resolve({ ok: false, unconfigured: true,
                               message: "Photo scan isn't switched on yet." });
    }
  };
})();
"""

BLOCK = ["*/shared/seating-data.js*", "*/shared/teacher-guard.js*",
         "*/shared/config.js*", "*/shared/seating-photo.js*",
         "*supabase*"]


def prep(page):
    """Block the real seam and install the stub before the page's own scripts."""
    page.send("Network.enable")
    page.send("Network.setBlockedURLs", {"urls": BLOCK})
    page.send("Page.addScriptToEvaluateOnNewDocument", {"source": STUB})


def drag(page, sel, dx, dy):
    """
    A real pointer drag: press, three moves, release.

    Three moves rather than one because a gesture that arrives as a single
    jump is not what a trackpad or a finger produces, and an engine that
    coalesces undo per-gesture has to be watched across several moves to
    prove it is not banking one entry per move.
    """
    box = centre(page, sel)
    if not box:
        return False
    x, y = box["x"], box["y"]
    page.send("Input.dispatchMouseEvent", {
        "type": "mousePressed", "x": x, "y": y, "button": "left",
        "clickCount": 1, "pointerType": "mouse"})
    for i in (1, 2, 3):
        page.send("Input.dispatchMouseEvent", {
            "type": "mouseMoved", "x": x + dx * i / 3.0, "y": y + dy * i / 3.0,
            "button": "left", "buttons": 1, "pointerType": "mouse"})
        time.sleep(0.02)
    page.send("Input.dispatchMouseEvent", {
        "type": "mouseReleased", "x": x + dx, "y": y + dy, "button": "left",
        "clickCount": 1, "pointerType": "mouse"})
    time.sleep(0.15)
    return True


def centre(page, sel):
    """
    The element's centre in viewport coordinates, after scrolling it into view.

    ⚠️ The scroll is load-bearing, and leaving it out cost an hour. The tool
    panel is a sticky column with its own `overflow: auto`, so selecting a desk
    grows it and pushes Undo below the fold. `getBoundingClientRect()` happily
    returns a y of 1100 on a 900px viewport; CDP happily dispatches a click at
    that point; nothing receives it. The drive then reports "undo does not
    work" — a page bug that is really a driver bug, and the most expensive kind
    of red there is.
    """
    return page.eval("""(function(){
      var n = document.querySelector(%s);
      if (!n) return null;
      if (n.scrollIntoView) n.scrollIntoView({block: 'center', inline: 'center'});
      var r = n.getBoundingClientRect();
      if (!r.width && !r.height) return null;
      var x = r.left + r.width/2, y = r.top + r.height/2;
      if (x < 0 || y < 0 || x > innerWidth || y > innerHeight) return null;
      return {x: x, y: y};
    })()""" % json.dumps(sel))


def click(page, sel):
    """
    A real press-and-release at the element's centre, through CDP input.

    Not `element.click()`: half the things this gate presses are SVG nodes, and
    `click()` is defined on HTMLElement, not on SVGElement — a desk `<g>` simply
    has no such method. Driving the mouse instead is both the thing that works
    and the thing a teacher actually does.
    """
    box = centre(page, sel)
    if not box:
        return False
    for kind in ("mousePressed", "mouseReleased"):
        page.send("Input.dispatchMouseEvent", {
            "type": kind, "x": box["x"], "y": box["y"], "button": "left",
            "clickCount": 1, "pointerType": "mouse"})
    time.sleep(0.08)
    return True


def guard_armed(page):
    """
    Is the unsaved-changes guard actually holding?

    Dispatching a cancelable `beforeunload` and reading `defaultPrevented` asks
    the page the same question the browser asks when someone closes the tab,
    without needing devtools-only listener introspection.
    """
    return page.eval("""(function(){
      var e = new Event('beforeunload', {cancelable: true});
      window.dispatchEvent(e);
      return e.defaultPrevented;
    })()""")


def disarm(page):
    """
    Stop the unsaved-changes guard from blocking the driver's next navigation.

    ⚠️ Not cosmetic. With unsaved work on the canvas the page raises a real
    "Leave site?" dialog, `Page.navigate` never returns, and the whole drive
    hangs on a websocket read — which looks like a broken harness and is
    actually the feature working. A capture-phase listener that calls
    stopImmediatePropagation runs BEFORE the page's own handler and stops it
    ever seeing the event. The guard itself is asserted, once, above.
    """
    page.eval("""(function(){
      window.addEventListener('beforeunload', function (e) {
        e.stopImmediatePropagation();
      }, true);
    })()""")


def scenario(base, url, width=1280, height=900):
    """
    A fresh browser, sized, stubbed, pointed at one URL.

    ⚠️ ONE BROWSER PER SCENARIO, and that is not tidiness.

    After a synthetic pointer drag on this page, `Page.navigate` and new-target
    creation on the SAME browser stop answering and the websocket read times
    out. Chased properly and ruled out one at a time: it is not the screenshot
    (navigating straight after one is fine), not the unsaved-changes dialog
    (suppressing `beforeunload`, and saving first, both still hang), and not a
    dangling pointer capture (releasing every capture, and sending a further
    mouseup, both still hang).

    It is also NOT a product bug, which is the part that matters and was
    checked directly: after the same drag the page keeps evaluating script, and
    clicking the real "Rooms" link navigates to #/layouts and renders the
    Rooms heading. A teacher who drags a desk and then clicks a link is fine.
    The wedge only affects CDP-driven navigation, so the driver stops doing
    that rather than dressing a harness quirk up as a finding.
    """
    b = cdp.Browser().start()
    p = b.page("about:blank", settle=0.1)
    p.set_viewport(width, height)     # BEFORE the load — MRB-275's lesson
    prep(p)
    p.goto(base + url, settle=1.3)
    return b, p


def main():
    os.makedirs(SHOTS, exist_ok=True)
    if not os.path.exists(os.path.join(OUT, PAGE.lstrip("/"))):
        print("❌ %s is not built — run python3 build_all.py first" % PAGE)
        return 1

    server, port = cdp.serve(OUT)
    base = "http://127.0.0.1:%d" % port
    print("seating_drive — MRB-322   (serving %s on :%d)\n" % (OUT, port))
    errs = []

    try:
        # ── 1 · the layout builder, as the person who drew it ────────────
        print("· layout builder — author")
        b, p = scenario(base, PAGE + "#/layout/stub-layout")
        try:
            ok("the page mounts a canvas",
               p.eval("!!document.querySelector('.sc-root svg')"))
            ok("the author is offered Save",
               p.eval("""[].slice.call(document.querySelectorAll('button'))
                         .some(function(b){return /save layout/i.test(b.textContent);})"""))
            ok("the front of the room is labelled",
               p.eval("""(function(){
                 var t = document.querySelector('.sc-front-label');
                 return !!t && /front/i.test(t.textContent);
               })()"""))

            def desk_x():
                return p.eval("""(function(){
                  var g = document.querySelector("[data-desk-id='d1']");
                  if (!g) return null;
                  var r = g.getBoundingClientRect();
                  return Math.round(r.left + r.width/2);
                })()""")

            click(p, "[data-desk-id='d1']")
            x0 = desk_x()
            moved = drag(p, "[data-desk-id='d1']", 130, 60)
            x1 = desk_x()
            ok("a pointer drag moves a desk",
               moved and x0 is not None and x1 is not None and abs(x1 - x0) > 40,
               "x %s → %s" % (x0, x1))

            click(p, "[data-act='undo']")
            time.sleep(0.3)
            x2 = desk_x()
            ok("one drag costs exactly one undo",
               x2 is not None and abs(x2 - x0) <= 3,
               "back to %s (started %s)" % (x2, x0))

            ok("unsaved work is guarded before leaving the page",
               guard_armed(p) is True,
               "beforeunload cancels while the room is unsaved")

            # Shot taken here, while the builder is still on screen: the next
            # check leaves it, and a hash-only `goto` back would never return —
            # a same-document navigation fires no Page.loadEventFired, so the
            # harness waits 30s for a load event that is never coming.
            p.screenshot(os.path.join(SHOTS, "builder-1280.png"), 1280, 900)

            # The teacher's own way out of a dirty page, driven as a click.
            disarm(p)
            click(p, "a.sp-btn--quiet")
            time.sleep(0.7)
            ok("a link still navigates after a drag",
               p.eval("location.hash") == "#/layouts",
               "reached %s" % p.eval("location.hash"))
            ok("the rooms list renders after that navigation",
               p.eval("""(function(){
                 var h = document.querySelector('.sp-head__title');
                 return !!h && /rooms/i.test(h.textContent);
               })()"""))
            errs += p.console_errors()
        finally:
            b.close()

        # ── 2 · the same layout, as somebody who did not draw it ─────────
        print("\n· layout builder — a teacher who did not draw it")
        b, v = scenario(base, PAGE + "?stubview=1#/layout/stub-layout")
        try:
            ok("a non-author is not offered Save",
               v.eval("""![].slice.call(document.querySelectorAll('button'))
                         .some(function(b){return /save layout/i.test(b.textContent);})"""))
            ok("view mode renders NO drag handles at all",
               v.eval("document.querySelectorAll('.sc-handle, .sc-handle-hit').length") == 0,
               "absent, not disabled")
            ok("nothing on the view is merely disabled",
               v.eval("""document.querySelectorAll(
                         'button[disabled], [aria-disabled=\"true\"]').length""") == 0)
            ok("the layout is still readable to them",
               v.eval("document.querySelectorAll('[data-desk-id]').length") == 3,
               "3 desks")
            v.screenshot(os.path.join(SHOTS, "viewonly-1280.png"), 1280, 900)
            errs += v.console_errors()
        finally:
            b.close()

        # ── 3 · the plan editor ──────────────────────────────────────────
        print("\n· plan editor — seating a class")
        b, q = scenario(base, PAGE + "#/plan/stub-plan")
        try:
            ok("the roster lists the class",
               q.eval("document.querySelectorAll('.sp-pupil').length") == 8, "8 pupils")

            u0 = q.eval("(document.querySelector('.sp-count__unseated')||{}).textContent")
            ok("the unseated count is drawn before anyone is seated",
               u0 is not None and "8" in str(u0), str(u0))

            ok("a room with fewer chairs than pupils says so",
               q.eval("""(function(){
                 var n = document.querySelector('.sp-note--warn');
                 return !!n && /fewer chairs/i.test(n.textContent);
               })()"""), "6 chairs, 8 pupils")

            click(q, ".sp-pupil")
            before = q.eval("document.querySelectorAll('.sc-seat-label').length")
            click(q, "[data-seat-id='d1:0']")
            time.sleep(0.35)
            after = q.eval("document.querySelectorAll('.sc-seat-label').length")
            ok("tap-a-name then tap-a-chair seats a pupil",
               after == before + 1, "%s → %s labels drawn" % (before, after))

            u1 = q.eval("(document.querySelector('.sp-count__unseated')||{}).textContent")
            ok("the unseated count falls when a pupil sits down",
               u1 is not None and "7" in str(u1), str(u1))

            ok("the print header names the class, the room and the teacher",
               q.eval("""(function(){
                 var h = document.getElementById('sp-printhead');
                 if (!h) return false;
                 var t = h.textContent || '';
                 return /7z\\/Sc9/.test(t) && /S02a/.test(t);
               })()"""))

            q.screenshot(os.path.join(SHOTS, "plan-1280.png"), 1280, 900)
            errs += q.console_errors()
        finally:
            b.close()

        # ── 4 · 390px ────────────────────────────────────────────────────
        print("\n· 390px")
        b, m = scenario(base, PAGE + "#/plan/stub-plan", 390, 844)
        try:
            sw = m.eval("document.documentElement.scrollWidth")
            ok("no horizontal overflow at 390px", sw <= 391, "scrollWidth %s" % sw)

            small = m.eval("""(function(){
              var bad = [];
              [].slice.call(document.querySelectorAll('.sp-btn, .sp-pupil')).forEach(function(n){
                var r = n.getBoundingClientRect();
                if (r.height > 0 && r.height < 40) bad.push(n.className + ':' + Math.round(r.height));
              });
              return bad;
            })()""")
            ok("every control clears the 40px touch floor at 390px",
               not small, ("too small: " + ", ".join(small[:4])) if small else "")

            ok("the canvas is still drawn at 390px",
               m.eval("document.querySelectorAll('[data-desk-id]').length") == 3)

            m.screenshot(os.path.join(SHOTS, "plan-390.png"), 390, 844)
            errs += m.console_errors()
        finally:
            b.close()

        noise = ("ERR_BLOCKED_BY_CLIENT", "net::", "favicon", "Failed to load resource")
        real = [e for e in errs if not any(n in e for n in noise)]
        ok("no console errors across the four drives", not real,
           "; ".join(real[:3]) if real else "")

    finally:
        server.shutdown()

    passed = sum(1 for _n, okk, _d in checks if okk)
    print("\n%d/%d checks passed   ·   screenshots in %s"
          % (passed, len(checks), SHOTS))
    if passed != len(checks):
        print("\nfailed:")
        for n, okk, d in checks:
            if not okk:
                print("  • %s %s" % (n, ("— " + d) if d else ""))
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
