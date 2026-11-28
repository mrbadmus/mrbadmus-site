#!/usr/bin/env python3
"""teacher_tools_drive.py — the teacher tools' FOUR VIEWS, driven and checked.

    python3 teacher_tools_drive.py

⊕ 16 Nov 2026 (picker + timer tidy). The picker (`shared/teacher-picker.js`)
and the classroom timer (`shared/teacher-timer.js`) have ONE state and four
views — Board, Timer full, Mini, Pop-out — and only one view shows at a time.
`teacher_picker_drive.py` proves what the picker and the timer DO; this gate
proves WHERE they show and that moving between views loses nothing:

    1. NEVER OVERLAP. With the board open and a timer running, no part of the
       timer floats over the board: it is the strip, inside the board's
       header (hit-tested with `elementFromPoint`), one row, <= 56px tall.
       The Mini and the Board are never both visible, nor the Mini and the
       full timer, sampled after every transition of every scenario.
    2. CLOSE AND MINIMISE are one real click on a visible >= 44px button that
       is wholly inside the viewport, in every view, at 390x844 and 1920x1080
       (and 1440x900).
    3. A RUNNING TIMER SURVIVES minimise -> Mini -> drag -> expand -> pop-out
       -> a pick from the pop-out -> pop-in -> pop-out -> the teacher closing
       the pop-out window. The reading only ever goes down, by the time that
       passed, and it is still running at the end.
    4. THE PICKER IN THE POP-OUT: a whole No-repeats cycle picked from the
       pop-out (M distinct names), a Skip that gives the ticket back (the
       count does not move and the skipped child comes round again), and back
       on the page the board shows the same last name and count.
    5. THE POP-OUT'S THEME mirrors the page's, light and dark, including a
       change made while it is open.
    6. NO POP-OUT BUTTON where the API is missing (removed by an init script);
       the Mini still works and still drags.
    7. ZERO requests and no new storage keys across all of it.
    8. CLICKER KEYS sent to the pop-out window (real CDP key events on its own
       target) pick and toggle the timer.
And the footprint Mide asked for (16 Nov 2026): the Mini at rest is <= 320px
wide at 1440, no wider than the viewport at 390, and no more than about 30%
of the viewport's height.

⚠️ EVERY PRESS IS A REAL CDP MOUSE CLICK OR KEY EVENT. `requestWindow` needs
the click's activation, which a synthetic `.click()` does not carry; and the
pop-out is its own page target (it has an `openerId`), so its clicks, keys
and screenshots go to THAT target.
"""

import json
import os
import sys
import time

REPO = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, REPO)

FIXTURE = "teacher_fixtures/class-detail-fixture.html"
SIZES = ((390, 844), (1440, 900), (1920, 1080))

REC = """
  window.__REQ__ = [];
  (function () {
    var f = window.fetch;
    window.fetch = function () { window.__REQ__.push(['fetch', String(arguments[0])]); return f.apply(this, arguments); };
    var o = XMLHttpRequest.prototype.open;
    XMLHttpRequest.prototype.open = function (m, u) { window.__REQ__.push([m, String(u)]); return o.apply(this, arguments); };
    var b = navigator.sendBeacon;
    if (b) { navigator.sendBeacon = function (u) { window.__REQ__.push(['beacon', String(u)]); return b.apply(navigator, arguments); }; }
  }());
  1
"""

# What is showing, sampled from the page (and the pop-out, when it is open).
VIS = r"""(function () {
  function shown(e) {
    if (!e || !e.isConnected) { return false; }
    var r = e.getBoundingClientRect(), cs = getComputedStyle(e);
    return r.width > 0 && r.height > 0 && cs.display !== 'none' && cs.visibility !== 'hidden';
  }
  var b = document.querySelector('[data-mrb-picker]');
  var t = document.querySelector('[data-tm="overlay"]');
  var m = document.querySelector('[data-mrb-tools="mini"]');
  var w = window.documentPictureInPicture && documentPictureInPicture.window;
  return JSON.stringify({
    board: shown(b), mini: shown(m), pip: !!w,
    full: !!(t && t.getAttribute('data-tm-view') === 'full' && shown(t)),
    strip: !!(t && t.getAttribute('data-tm-view') === 'strip' && shown(t)),
    tview: t ? t.getAttribute('data-tm-view') : (w && w.document.querySelector('[data-tm="overlay"]') ? 'pip' : null),
    pageTools: !!(shown(b) || shown(m) || (t && shown(t)))
  });
})()"""

# The timer's reading and state, wherever it is.
TM = r"""(function () {
  var w = window.documentPictureInPicture && documentPictureInPicture.window;
  var t = document.querySelector('[data-tm="overlay"]') ||
          (w && w.document.querySelector('[data-tm="overlay"]'));
  return JSON.stringify(t ? {r: t.getAttribute('data-tm-reading'), s: t.getAttribute('data-tm-state'),
                             v: t.getAttribute('data-tm-view'), b: Number(t.getAttribute('data-tm-beeps'))} : null);
})()"""


def secs(r):
    t = 0
    for x in str(r or "0:00").split(":"):
        t = t * 60 + int(x)
    return t


class Run:
    def __init__(self, cdp, br, page, width, height):
        self.cdp, self.br, self.page = cdp, br, page
        self.w, self.h = width, height
        self.P = []
        self.vis = []
        self.pp = None

    def bad(self, m):
        self.P.append("%dpx: %s" % (self.w, m))

    def ev(self, js, timeout=30):
        return self.page.eval(js, timeout=timeout)

    def j(self, js):
        return json.loads(self.ev(js))

    def sample(self, where):
        v = self.j(VIS)
        v["at"] = where
        self.vis.append(v)
        if v["mini"] and v["board"]:
            self.bad("%s: the Mini and the board are both showing" % where)
        if v["mini"] and v["full"]:
            self.bad("%s: the Mini and the full timer are both showing" % where)
        if v["pip"] and v["pageTools"]:
            self.bad("%s: popped out, yet tools still show on the page %r" % (where, v))
        return v

    # ── real input ────────────────────────────────────────────────────
    def rect(self, sel, doc="document"):
        return json.loads(self.ev(
            "(function(){var d=%s;var e=d&&d.querySelector(%s);if(!e)return 'null';"
            "var b=e.getBoundingClientRect();return JSON.stringify({x:b.left,y:b.top,w:b.width,h:b.height,"
            "vw:d.defaultView.innerWidth,vh:d.defaultView.innerHeight});})()" % (doc, json.dumps(sel))))

    def click(self, sel, page=None, doc="document", label=None):
        r = self.rect(sel, doc)
        if not r:
            self.bad("no %s to press%s" % (sel, (" (" + label + ")") if label else ""))
            return False
        x, y = r["x"] + r["w"] / 2, r["y"] + r["h"] / 2
        for t in ("mousePressed", "mouseReleased"):
            try:
                (page or self.page).send("Input.dispatchMouseEvent",
                                         {"type": t, "x": x, "y": y, "button": "left", "clickCount": 1})
            except self.cdp.CDPError:
                # a press that closes its own window (the pop-out's "Back to
                # page") takes that target's socket with it — that IS the press
                if page is None or page is self.page:
                    raise
        time.sleep(0.25)
        return True

    def pclick(self, marker, doc="document", page=None, label=None):
        return self.click('[data-mrb-added="%s"]' % marker, page=page, doc=doc, label=label)

    def target_ok(self, marker, doc="document", what=""):
        """>= 44px both ways and wholly inside the viewport."""
        r = self.rect('[data-mrb-added="%s"]' % marker, doc)
        if not r:
            self.bad("%s: no %s" % (what, marker))
            return
        if r["w"] < 44 - 0.5 or r["h"] < 44 - 0.5:
            self.bad("%s: %s is %dx%d (floor 44)" % (what, marker, r["w"], r["h"]))
        if r["x"] < 0 or r["y"] < 0 or r["x"] + r["w"] > r["vw"] + 0.5 or r["y"] + r["h"] > r["vh"] + 0.5:
            self.bad("%s: %s is not wholly inside the viewport %r" % (what, marker, r))

    def drag(self, sel, dx, dy):
        r = self.rect(sel)
        x, y = r["x"] + 14, r["y"] + r["h"] / 2
        s = self.page.send
        s("Input.dispatchMouseEvent", {"type": "mousePressed", "x": x, "y": y, "button": "left", "buttons": 1, "clickCount": 1})
        for i in range(1, 9):
            s("Input.dispatchMouseEvent", {"type": "mouseMoved", "x": x + dx * i / 8, "y": y + dy * i / 8,
                                           "button": "left", "buttons": 1})
            time.sleep(0.02)
        s("Input.dispatchMouseEvent", {"type": "mouseReleased", "x": x + dx, "y": y + dy, "button": "left", "buttons": 0, "clickCount": 1})
        time.sleep(0.2)

    # ── the pop-out's own target ───────────────────────────────────────
    def pip_page(self):
        for _ in range(30):
            ts = self.page.send("Target.getTargets", {"filter": [{}]})["targetInfos"]
            pid = [t["targetId"] for t in ts if t["type"] == "page" and t.get("openerId")]
            if pid:
                self.pp = self.cdp.Page(self.cdp.WSClient(
                    "ws://127.0.0.1:%d/devtools/page/%s" % (self.br.port, pid[0])))
                return self.pp
            time.sleep(0.1)
        return None

    def pip_open(self):
        return self.ev("!!(window.documentPictureInPicture && documentPictureInPicture.window)")

    def key(self, page, k):
        import teacher_picker_drive as D
        D._kd(page, k); time.sleep(0.02); D._ku(page, k); time.sleep(0.45)


PIPDOC = "(window.documentPictureInPicture&&documentPictureInPicture.window&&documentPictureInPicture.window.document)"


def fresh(cdp, br, port, w, h, no_pip=False):
    page = br.attach()
    if no_pip:
        page.send("Page.addScriptToEvaluateOnNewDocument",
                  {"source": "try{delete window.documentPictureInPicture;}catch(e){}"
                             "try{Object.defineProperty(window,'documentPictureInPicture',{value:undefined,configurable:true});"
                             "delete window.documentPictureInPicture;}catch(e){}"})
    page.goto("http://127.0.0.1:%d/%s" % (port, FIXTURE))
    page.set_viewport(w, h)
    page.send("Emulation.setEmulatedMedia",
              {"features": [{"name": "prefers-reduced-motion", "value": "reduce"}]})
    page.eval("window.localStorage.clear(); window.sessionStorage.clear(); 1")
    page.eval(REC)
    return page


def open_board(R, start_timer=True):
    R.pclick("pick-open", label="the class page's Pick a student")
    R.pclick("pick-go")
    if start_timer:
        R.pclick("pick-timer")
        R.pclick("tm-toggle")


def geometry(R):
    """1 and 2 (and the footprint), at this size."""
    W = "%dx%d" % (R.w, R.h)
    open_board(R)
    v = R.sample("board + running timer")
    if not v["strip"]:
        R.bad("board with a running timer: the timer is %r, wanted the strip" % v["tview"])
    g = R.j(r"""(function () {
      var b = document.querySelector('[data-mrb-picker]'), t = document.querySelector('[data-tm="overlay"]');
      var h = b.querySelector('[data-mrb-tm-slot]').parentNode;
      var tr = t.getBoundingClientRect(), hr = h.getBoundingClientRect(), br = b.getBoundingClientRect();
      var name = b.querySelector('[data-mrb-name]').getBoundingClientRect();
      var go = b.querySelector('[data-mrb-added="pick-go"]').getBoundingClientRect();
      var pts = [[tr.left + 4, tr.top + tr.height / 2], [tr.left + tr.width / 2, tr.top + tr.height / 2],
                 [tr.right - 4, tr.top + tr.height / 2]];
      var hits = pts.map(function (p) { var e = document.elementFromPoint(p[0], p[1]);
        return !!e && t.contains(e) && b.contains(e); });
      /* anything of the timer's anywhere OUTSIDE the board? */
      var stray = Array.prototype.slice.call(document.querySelectorAll('[data-tm="overlay"],[data-mrb-tools]'))
        .filter(function (e) { return !b.contains(e) && e.getBoundingClientRect().width > 0; }).length;
      /* the stage is untouched: nothing of the timer over the name or Pick */
      var over = [name, go].some(function (r) { return !(r.bottom <= tr.top || r.top >= tr.bottom ||
                                                          r.right <= tr.left || r.left >= tr.right); });
      return JSON.stringify({inBoard: b.contains(t), inHeader: h.contains(t), hits: hits, stray: stray,
        h: tr.height, w: tr.width, bw: br.width, overStage: over,
        rows: Math.round(tr.height / 44), within: tr.left >= hr.left - .5 && tr.right <= hr.right + .5 &&
                                                   tr.top >= hr.top - .5 && tr.bottom <= hr.bottom + .5});
    })()""")
    if not (g["inBoard"] and g["inHeader"] and g["within"]):
        R.bad("%s: the strip is not inside the board's header layout box: %r" % (W, g))
    if not all(g["hits"]):
        R.bad("%s: elementFromPoint across the strip did not land on it inside the board: %r" % (W, g["hits"]))
    if g["stray"]:
        R.bad("%s: %d timer/tools element(s) on the page outside the board" % (W, g["stray"]))
    if g["h"] > 56:
        R.bad("%s: the strip is %spx tall (limit 56, one row)" % (W, g["h"]))
    if g["w"] > g["bw"] + 0.5:
        R.bad("%s: the strip is wider than the board" % W)
    if g["overStage"]:
        R.bad("%s: the strip overlaps the name or the Pick button" % W)
    strip_kids = R.j("""JSON.stringify(Array.prototype.map.call(document.querySelectorAll(
        '[data-tm="overlay"] [data-mrb-added]'), function (e) { return e.getAttribute('data-mrb-added'); }))""")
    extra = [k for k in strip_kids if k not in ("tm-digits", "tm-toggle", "tm-expand", "tm-live", "tm-done")]
    if extra:
        R.bad("%s: the strip carries more than digits, start/pause and expand: %r" % (W, extra))
    for m in ("pick-min", "pick-close", "tm-expand", "tm-toggle"):
        R.target_ok(m, what=W + " board")

    # full over the board: minimise goes back to the strip, one click
    R.pclick("tm-expand")
    v = R.sample("expand from the strip")
    if not v["full"]:
        R.bad("%s: the strip's expand did not open the full timer (%r)" % (W, v["tview"]))
    for m in ("tm-min", "tm-close", "tm-sub-30"):
        R.target_ok(m, what=W + " full")
    R.pclick("tm-min")
    v = R.sample("minimise the full timer over the board")
    if not (v["strip"] and v["board"]):
        R.bad("%s: minimise from full with the board underneath did not return to the strip: %r" % (W, v))

    # board minimise -> Mini, one click
    R.pclick("pick-min")
    v = R.sample("board minimise")
    if not v["mini"] or v["board"]:
        R.bad("%s: the board's minimise did not go to the Mini: %r" % (W, v))
    mini = R.rect('[data-mrb-tools="mini"]')
    if R.w == 1440 and mini["w"] > 320.5:
        R.bad("%s: the Mini is %dpx wide (limit 320)" % (W, mini["w"]))
    if mini["w"] > mini["vw"] + 0.5:
        R.bad("%s: the Mini is wider than the viewport" % W)
    if mini["h"] > 0.31 * mini["vh"]:
        R.bad("%s: the Mini is %dpx tall, %.0f%% of the viewport (limit about 30%%)"
              % (W, mini["h"], 100.0 * mini["h"] / mini["vh"]))
    rows = R.j("""JSON.stringify((function(){var m=document.querySelector('[data-mrb-tools="mini"]');
      var t=m.querySelector('[data-tm="overlay"]'), s=m.querySelector('[data-mrb-pick-section]');
      return {t: t ? t.getBoundingClientRect().height : 0, s: s ? s.getBoundingClientRect().height : 0};})())""")
    if rows["t"] > 60 or rows["s"] > 60:
        R.bad("%s: the Mini's timer/picker rows are %r tall — one row each" % (W, rows))
    if not (mini["x"] + mini["w"] > mini["vw"] - 40 and mini["y"] + mini["h"] > mini["vh"] - 40):
        R.bad("%s: the Mini does not start at the bottom right: %r" % (W, mini))
    for m in ("tools-expand", "tools-close", "tools-mute", "tm-toggle", "pick-go", "pick-skip"):
        R.target_ok(m, what=W + " Mini")
    # expand -> board, one click; then X closes the board, Mini with the timer
    R.pclick("tools-expand")
    v = R.sample("Mini expand")
    if not v["board"] or v["mini"]:
        R.bad("%s: the Mini's expand did not return to the board: %r" % (W, v))
    R.pclick("pick-close")
    v = R.sample("board X with a timer running")
    if v["board"] or not v["mini"] or v["tview"] != "mini":
        R.bad("%s: closing the board did not leave the running timer in the Mini: %r" % (W, v))
    # Mini expand (no board) -> full; minimise -> Mini
    R.pclick("tools-expand")
    v = R.sample("Mini expand, no board")
    if not v["full"]:
        R.bad("%s: the Mini's expand with no board did not open the full timer" % W)
    R.pclick("tm-min")
    v = R.sample("full minimise, no board")
    if not v["mini"]:
        R.bad("%s: minimise from full with no board did not go to the Mini" % W)
    # the Mini's X: one click closes it and its tools
    R.pclick("tools-close")
    v = R.sample("Mini X")
    t = R.j(TM)
    if v["mini"] or t is not None:
        R.bad("%s: the Mini's X left %r / timer %r" % (W, v, t))
    # full X: one click
    R.ev("window.MrBadmusTimer.open({view: 'full'}); 1")
    for m in ("tm-min", "tm-close", "tm-mute", "tm-toggle"):
        R.target_ok(m, what=W + " full, idle")
    R.pclick("tm-close")
    if R.j(TM) is not None:
        R.bad("%s: the full timer's X did not close it" % W)


def survive_and_pip(R):
    """3, 4, 5, 8 — the long run through every view, at one size."""
    import teacher_picker_drive as D
    open_board(R, start_timer=False)
    # a fresh cycle
    R.ev("(function(){var r=document.querySelector('[data-mrb-added=\"pick-reset\"]');if(r){r.click();}return 1;})()")
    R.pclick("pick-timer")
    R.pclick("tm-toggle")
    t0 = time.time()
    r0 = secs(R.j(TM)["r"])
    log = [(0.0, r0, "start")]

    def read(at):
        t = R.j(TM)
        if not t:
            R.bad("%s: the timer is gone" % at)
            return
        el = time.time() - t0
        log.append((el, secs(t["r"]), at))
        if t["s"] not in ("running", "warn"):
            R.bad("%s: the timer is %r, wanted running" % (at, t["s"]))

    R.pclick("pick-min"); R.sample("minimise"); read("minimise -> Mini")
    before = R.rect('[data-mrb-tools="mini"]')
    R.drag('[data-mrb-added="tools-head"]', -500, -300)
    after = R.rect('[data-mrb-tools="mini"]')
    R.sample("drag"); read("drag")
    if abs(after["x"] - before["x"]) < 100 or abs(after["y"] - before["y"]) < 100:
        R.bad("dragging the Mini's header did not move it: %r -> %r" % (before, after))
    if after["x"] < 0 or after["y"] < 0 or after["x"] + after["w"] > after["vw"] or after["y"] + after["h"] > after["vh"]:
        R.bad("the dragged Mini left the viewport: %r" % after)
    R.pclick("tools-expand"); R.sample("expand"); read("expand -> board")
    R.pclick("pick-popout")
    time.sleep(0.8)
    if not R.pip_open():
        R.bad("the board's pop-out did not open a Picture-in-Picture window")
        return
    R.sample("pop-out from the board"); read("pop-out")
    pp = R.pip_page()
    if not pp:
        R.bad("no CDP target for the pop-out window")
        return
    pip_w = R.j("JSON.stringify([%s.defaultView.innerWidth, %s.defaultView.innerHeight])" % (PIPDOC, PIPDOC))
    for m in ("tools-back", "tools-mute", "tm-toggle", "pick-go"):
        R.target_ok(m, doc=PIPDOC, what="pop-out")
    # the title follows the brand rule
    title = R.ev("%s.title" % PIPDOC)
    if not str(title).endswith(" | MrBadmus"):
        R.bad("the pop-out's title is %r, wanted '… | MrBadmus'" % title)

    # ── 4. a whole No-repeats cycle from the pop-out, with a Skip ──────
    cnt = lambda: R.ev("%s.querySelector('[data-mrb-pick-section]').getAttribute('data-pick-count')" % PIPDOC)
    nm = lambda: R.ev("%s.querySelector('[data-mrb-pick-section] [data-mrb-name]').textContent.trim()" % PIPDOC)
    m0 = cnt()
    import re
    mm = re.match(r"^Picked (\d+) of (\d+)$", str(m0))
    if not mm:
        R.bad("the pop-out's picker count reads %r" % m0)
        return
    done0, M = int(mm.group(1)), int(mm.group(2))
    names = []
    # done0 is 1 (the board's pick before popping): pick until one is left
    while True:
        k = int(re.match(r"^Picked (\d+)", cnt()).group(1))
        if k >= M - 1:
            break
        R.pclick("pick-go", doc=PIPDOC, page=pp)
        names.append(nm())
        if cnt() != "Picked %d of %d" % (k + 1, M):
            R.bad("after a pop-out pick the count read %r, wanted Picked %d of %d" % (cnt(), k + 1, M))
            break
    read("picks from the pop-out")
    skipped = nm()
    c_before = cnt()
    R.pclick("pick-skip", doc=PIPDOC, page=pp)
    landed = nm()
    if cnt() != c_before:
        R.bad("Skip moved the count %r -> %r (the skipped ticket goes back)" % (c_before, cnt()))
    if landed == skipped:
        R.bad("Skip landed on the skipped pupil again (%r)" % skipped)
    R.pclick("pick-go", doc=PIPDOC, page=pp)
    last = nm()
    if last != skipped:
        R.bad("after Skip the last ticket in the hat was not the skipped pupil's "
              "(%r, skipped %r)" % (last, skipped))
    if cnt() != "Picked %d of %d" % (M, M):
        R.bad("the cycle from the pop-out ended at %r, wanted Picked %d of %d" % (cnt(), M, M))
    golabel = R.ev("%s.querySelector('[data-mrb-added=\"pick-go\"]').textContent.trim()" % PIPDOC)
    if golabel != "Everyone picked":
        R.bad("a spent cycle's Pick in the pop-out reads %r" % golabel)
    # every name drawn in the pop-out is distinct
    if len(set(names + [landed])) != len(names) + 1:
        R.bad("No repeats repeated in the pop-out: %r" % (names + [landed],))
    read("cycle + Skip in the pop-out")

    # ── 8. clicker keys to the pop-out window ──────────────────────────
    st0 = R.j(TM)["s"]
    R.key(pp, "PageUp")
    st1 = R.j(TM)["s"]
    R.key(pp, "ArrowLeft")
    st2 = R.j(TM)["s"]
    if not (st0 in ("running", "warn") and st1 == "paused" and st2 in ("running", "warn")):
        R.bad("the clicker's Back sent to the pop-out did not pause then resume: %r" % [st0, st1, st2])
    # (forward keys pick: checked below, once the spent cycle has been
    # started again on the board and the tools popped out from the Mini)

    # ── 5. theme ────────────────────────────────────────────────────────
    th = []
    for t in ("dark", "light", "dark"):
        R.ev("document.documentElement.setAttribute('data-theme','%s'); 1" % t)
        time.sleep(0.15)
        th.append(R.j("JSON.stringify([%s.documentElement.getAttribute('data-theme'),"
                      "getComputedStyle(%s.body).backgroundColor])" % (PIPDOC, PIPDOC)))
    if [x[0] for x in th] != ["dark", "light", "dark"]:
        R.bad("the pop-out did not mirror the page's theme while open: %r" % th)
    if th[0][1] == th[1][1]:
        R.bad("the pop-out's background did not change with the theme: %r" % th)
    R.ev("document.documentElement.setAttribute('data-theme','light'); 1")

    # ── pop in ──────────────────────────────────────────────────────────
    R.pclick("tools-back", doc=PIPDOC, page=pp)
    time.sleep(0.4)
    if R.pip_open():
        R.bad("Back to page left the pop-out open")
    v = R.sample("pop in")
    read("pop in -> Mini")
    if not v["mini"]:
        R.bad("Back to page did not return the tools as the Mini: %r" % v)
    R.pclick("tools-expand")
    bd = R.j("""JSON.stringify((function(){var b=document.querySelector('[data-mrb-picker]');
      var c=''; b.querySelectorAll('div').forEach(function(d){var t=(d.textContent||'').trim();
      if(/^Picked \\d+ of \\d+$/.test(t)){c=t;}});
      return {name: b.querySelector('[data-mrb-name]').textContent.trim(), count: c};})())""")
    if bd["name"] != last or bd["count"] != "Picked %d of %d" % (M, M):
        R.bad("after pop-in the board shows %r, wanted %r and Picked %d of %d" % (bd, last, M, M))
    R.sample("board after pop-in"); read("board after pop-in")

    # Start again, pop out from the MINI, pick by the clicker's forward key
    R.pclick("pick-reset")
    R.pclick("pick-min")
    R.pclick("tools-popout")
    time.sleep(0.8)
    if not R.pip_open():
        R.bad("the Mini's pop-out did not open a window")
        return
    R.sample("pop-out from the Mini"); read("pop-out from the Mini")
    pp = R.pip_page()
    c0 = cnt()
    R.key(pp, "PageDown")
    R.key(pp, "ArrowRight")
    c2 = cnt()
    if (c0, c2) != ("Picked 0 of %d" % M, "Picked 2 of %d" % M):
        R.bad("two forward keys sent to the pop-out moved the count %r -> %r" % (c0, c2))
    read("clicker picks in the pop-out")
    R.key(pp, "Escape")
    if not R.pip_open():
        R.bad("Escape in the pop-out closed it")
    read("Escape in the pop-out")

    # the teacher closes the window with its own X -> pagehide
    R.ev("documentPictureInPicture.window.close(); 1")
    time.sleep(0.6)
    v = R.sample("the teacher closes the pop-out")
    read("pop-out closed by the teacher")
    if R.pip_open() or not v["mini"]:
        R.bad("closing the pop-out window did not bring the Mini back: %r" % v)
    if R.ev("%s ? 1 : 0" % "document.querySelector('[data-mrb-tools=\"mini\"] [data-mrb-pick-section]')") != 1:
        R.bad("the picker did not come back with the Mini")

    # the reading only ever went down, by the time that passed
    for (ta, ra, a), (tb, rb, b) in zip(log, log[1:]):
        if rb > ra:
            R.bad("the reading went UP between %r (%s) and %r (%s)" % (a, ra, b, rb))
    el, rl, _ = log[-1]
    if abs((r0 - rl) - el) > 2.5:
        R.bad("over %.1fs the reading fell by %ds — a view change moved the clock" % (el, r0 - rl))
    t = R.j(TM)
    if not t or t["s"] not in ("running", "warn"):
        R.bad("at the end the timer is %r, wanted running" % (t,))
    # ── sound while popped out; −30 s clamps at 0 and finishes ─────────
    R.pclick("tools-popout")
    time.sleep(0.8)
    pp = R.pip_page()
    b0 = R.j(TM)["b"]
    for _ in range(14):
        if R.j(TM)["s"] == "done":
            break
        R.pclick("tm-sub-30", doc=PIPDOC, page=pp)
    tz = R.j(TM)
    if tz["s"] != "done" or tz["r"] != "0:00":
        R.bad("−30 s pressed to zero in the pop-out left %r, wanted done at 0:00" % (tz,))
    if tz["b"] <= b0:
        R.bad("the countdown finished in the pop-out without its sound (beeps %d -> %d)"
              % (b0, tz["b"]))
    pip_vis = R.ev("%s.querySelector('[data-mrb-added=\"tm-done\"]') ? 1 : 0" % PIPDOC)
    if pip_vis != 1:
        R.bad("the pop-out does not show the finished state")
    # the PAGE's own "Pick a student", pressed while popped out, brings
    # the tools back to the page as the board — state untouched
    if not R.pip_open():
        R.bad("(set-up) the pop-out closed before the page-button check")
    R.pclick("pick-open")
    time.sleep(0.4)
    v = R.sample("page's Pick a student while popped out")
    tz2 = R.j(TM)
    if R.pip_open() or not v["board"]:
        R.bad("the page's Pick a student while popped out did not bring the board back: %r" % v)
    if not tz2 or tz2["s"] != "done":
        R.bad("bringing the tools back changed the timer: %r" % (tz2,))
    print("     %-6s survive: %d view changes over %.0fs, reading %s -> %s, still %s; "
          "pop-out %sx%s; cycle of %d with a Skip"
          % ("%dpx" % R.w, len(log) - 1, el, r0, rl, t and t["s"], pip_w[0], pip_w[1], M))


def no_api(R):
    """6 — no pop-out anywhere, the Mini still works and drags."""
    has = R.ev("'documentPictureInPicture' in window")
    if has:
        R.bad("the init script did not remove the API (test set-up)")
    open_board(R)
    if R.ev("!!document.querySelector('[data-mrb-added=\"pick-popout\"]')"):
        R.bad("no API, yet the board offers pop-out")
    R.pclick("tm-expand")
    if R.ev("!!document.querySelector('[data-mrb-added=\"tm-popout\"]')"):
        R.bad("no API, yet the full timer offers pop-out")
    R.pclick("tm-min")
    R.pclick("pick-min")
    v = R.sample("no API: Mini")
    if not v["mini"]:
        R.bad("no API: minimise did not show the Mini")
    if R.ev("!!document.querySelector('[data-mrb-added=\"tools-popout\"]')"):
        R.bad("no API, yet the Mini offers pop-out")
    b = R.rect('[data-mrb-tools="mini"]')
    R.drag('[data-mrb-added="tools-head"]', -300, -200)
    a = R.rect('[data-mrb-tools="mini"]')
    if abs(a["y"] - b["y"]) < 100:
        R.bad("no API: the Mini did not drag: %r -> %r" % (b, a))
    c0 = R.ev("document.querySelector('[data-mrb-pick-section]').getAttribute('data-pick-count')")
    R.pclick("pick-go")
    c1 = R.ev("document.querySelector('[data-mrb-pick-section]').getAttribute('data-pick-count')")
    if c0 == c1:
        R.bad("no API: Pick in the Mini did nothing (%r)" % c1)


def close_pip_window(R):
    """The teacher's own X on the pop-out window — its target closed."""
    ts = R.page.send("Target.getTargets", {"filter": [{}]})["targetInfos"]
    pid = [t["targetId"] for t in ts if t["type"] == "page" and t.get("openerId")]
    if pid:
        R.page.send("Target.closeTarget", {"targetId": pid[0]})
    time.sleep(0.9)


def hide_in_pip(R):
    """⊕ Mac check, 27 Nov 2026 — B in a TIMER-ONLY pop-out hides the timer
    and changes nothing else: the window stays open, and B again shows the
    timer there, still running. It used to close the pop-out and leave the
    timer hidden on the page with nothing visible."""
    import teacher_picker_drive as D
    R.pclick("timer-open", label="the class page's Timer")
    if (R.j(TM) or {}).get("s") not in ("running", "warn"):
        R.pclick("tm-toggle")
    R.pclick("tm-popout")
    time.sleep(0.8)
    pp = R.pip_page()
    if not R.pip_open() or not pp:
        R.bad("hide in pop-out: the timer's pop-out did not open")
        return

    def press_b():
        try:
            D._kd(pp, "b"); time.sleep(0.02); D._ku(pp, "b")
        except R.cdp.CDPError:
            pass  # the window closing under the key is the bug this checks
        time.sleep(0.6)

    press_b()
    if not R.pip_open():
        R.bad("B in a timer-only pop-out closed the pop-out (%r)" % R.j(VIS))
        return
    v = R.sample("B in the pop-out")
    if v["pageTools"]:
        R.bad("B in the pop-out put tools back on the page: %r" % v)
    press_b()
    v = R.sample("B again in the pop-out")
    t = R.j(TM) or {}
    if not R.pip_open() or not v["pip"]:
        R.bad("B again did not show the timer in the pop-out: %r" % v)
    if t.get("s") not in ("running", "warn"):
        R.bad("after B, B in the pop-out the timer is %r, wanted running" % t)
    close_pip_window(R)


def mini_after_popin(R):
    """⊕ Mac check, 27 Nov 2026 — a Mini dragged to the bottom edge, popped
    out, then the pop-out closed by its own X: the Mini comes back wholly on
    screen. It was placed before its timer row had its real height and hung
    32px off the bottom at 1440x900."""
    open_board(R)
    R.pclick("pick-min")
    R.drag('[data-mrb-added="tools-head"]', -300, 400)
    R.pclick("tools-popout")
    time.sleep(0.8)
    if not R.pip_open():
        R.bad("Mini after pop-in: the pop-out did not open")
        return
    close_pip_window(R)
    m = R.rect('[data-mrb-tools="mini"]')
    if not m:
        R.bad("Mini after pop-in: no Mini came back")
    elif m["x"] < 0 or m["y"] < 0 or m["x"] + m["w"] > m["vw"] + 0.5 or m["y"] + m["h"] > m["vh"] + 0.5:
        R.bad("Mini after pop-in is not wholly on screen: %r" % m)


def main(argv):
    import ks3_browser as cdp
    if not os.path.exists(os.path.join(REPO, FIXTURE)):
        print("\nteacher_tools_drive.py: not built — %s\n  Run `python3 build_teacher_port.py` first." % FIXTURE)
        return 1
    print("\n🧰  teacher_tools_drive — four views, one at a time\n")
    server, port = cdp.serve(REPO)
    problems = []
    samples = 0
    try:
        for w, h in SIZES:
            with cdp.Browser() as br:
                page = fresh(cdp, br, port, w, h)
                ls0 = page.eval("Object.keys(localStorage).length + ':' + Object.keys(sessionStorage).length")
                R = Run(cdp, br, page, w, h)
                geometry(R)
                if w == 1440:
                    page = fresh(cdp, br, port, w, h)
                    R.page = page
                    survive_and_pip(R)
                    for check in (hide_in_pip, mini_after_popin):
                        # each check gets a fresh page; the run's own page is
                        # held to zero requests here, before it is replaced
                        reqs0 = json.loads(R.page.eval("JSON.stringify(window.__REQ__||[])"))
                        if reqs0:
                            R.bad("%d request(s) before %s: %r" % (len(reqs0), check.__name__, reqs0[:4]))
                        page = fresh(cdp, br, port, w, h)
                        R.page = page
                        check(R)
                reqs = json.loads(R.page.eval("JSON.stringify(window.__REQ__ || [])"))
                ls1 = R.page.eval("Object.keys(localStorage).length + ':' + Object.keys(sessionStorage).length")
                if reqs:
                    R.bad("%d request(s): %r" % (len(reqs), reqs[:4]))
                if ls1 != "0:0" or ls0 != "0:0":
                    R.bad("storage keys %s -> %s, wanted none" % (ls0, ls1))
                errs = R.page.console_errors()
                if errs:
                    R.bad("console errors: %r" % errs[:3])
                problems.extend(R.P)
                samples += len(R.vis)
                print("     %-6s %s  %d view sample(s), %d request(s), storage %s"
                      % ("%dpx" % w, "❌" if R.P else "✅", len(R.vis), len(reqs), ls1))
            if w == 390:
                with cdp.Browser() as br:
                    page = fresh(cdp, br, port, w, h, no_pip=True)
                    R = Run(cdp, br, page, w, h)
                    no_api(R)
                    problems.extend(R.P)
                    samples += len(R.vis)
                    print("     %-6s %s  no Picture-in-Picture: no pop-out offered, the Mini works and drags"
                          % ("%dpx" % w, "❌" if R.P else "✅"))
    finally:
        server.shutdown()
    print()
    if problems:
        print("  FAIL  %d problem(s):\n" % len(problems))
        for p in problems:
            print("     · %s" % p)
        print()
        return 1
    print("  PASS  %d size(s), %d view samples. One view at a time: the running timer\n"
          "        is a <=56px strip inside the board's header (hit-tested), never\n"
          "        over it; the Mini never shows with the board or the full timer and\n"
          "        is <=320px wide at 1440 and <=30%% of the viewport tall; close and\n"
          "        minimise are one real click on a >=44px button inside the viewport\n"
          "        in every view. A running timer survived minimise, drag, expand,\n"
          "        pop-out, picks, pop-in and the teacher closing the window, its\n"
          "        reading only falling by the time that passed. A whole No-repeats\n"
          "        cycle ran from the pop-out with a Skip that gave its ticket back;\n"
          "        the board agreed after pop-in. The pop-out mirrored light/dark live,\n"
          "        took clicker keys on its own window, and Escape there did nothing.\n"
          "        No API: no pop-out button, and the Mini still works and drags.\n"
          "        Zero requests, zero storage keys.\n" % (len(SIZES), samples))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
