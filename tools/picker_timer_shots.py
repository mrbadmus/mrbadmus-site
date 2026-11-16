#!/usr/bin/env python3
"""tools/picker_timer_shots.py — screenshots of the picker, the classroom
timer and their four views, for review.

    python3 tools/picker_timer_shots.py [--out DIR]

Writes PNGs to docs/picker-timer/shots/ (default) at 390x844 (device scale 2),
1440x900 and 1920x1080, light and dark. It drives the class-detail FIXTURE the
way `teacher_picker_drive.py` and `teacher_tools_drive.py` do (served by
`ks3_browser.serve`, pressed by `data-mrb-added` marker; the pop-out with a
real CDP click, because `requestWindow` needs the click's activation).

⚑ THE POP-OUT IS PHOTOGRAPHED ITSELF, not a mock-up: it is its own page
target (it has an `openerId`), so this attaches to that target and captures
it with `Page.captureScreenshot`. "Small" is the window as opened; "large"
emulates a 960x600 window on that same target (`setDeviceMetricsOverride`),
which is what a teacher dragging its corner gets — its digits and name are
sized in container units, so they grow with it.

Every scene is taken in both themes, at every viewport.
"""
import base64
import json
import os
import sys
import time

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, REPO)

import ks3_browser as cdp                                   # noqa: E402
import teacher_picker_drive as D                            # noqa: E402
import teacher_tools_drive as TD                            # noqa: E402

FIXTURE = D.FIXTURE
VIEWPORTS = (("390", 390, 844, 2), ("1440", 1440, 900, 1),
             ("1920", 1920, 1080, 1))


def js(page, body, timeout=60):
    return json.loads(page.eval(D.wrap(D.TIMER_PRE, body +
                                        "\nreturn JSON.stringify(out);"),
                                timeout=timeout))


def save(res, path):
    with open(path, "wb") as fh:
        fh.write(base64.b64decode(res["data"]))
    print("   wrote", os.path.basename(path))


def shot(page, out, name, w, h, dpr):
    page.send("Emulation.setDeviceMetricsOverride",
              {"width": w, "height": h, "deviceScaleFactor": dpr,
               "mobile": False})
    time.sleep(0.25)
    save(page.send("Page.captureScreenshot",
                   {"format": "png", "fromSurface": True}),
         os.path.join(out, name))


def pip_shot(pp, out, name, size=None):
    if size:
        pp.send("Emulation.setDeviceMetricsOverride",
                {"width": size[0], "height": size[1], "deviceScaleFactor": 1,
                 "mobile": False})
    else:
        pp.send("Emulation.clearDeviceMetricsOverride", {})
    time.sleep(0.3)
    save(pp.send("Page.captureScreenshot", {"format": "png"}),
         os.path.join(out, name))


def main(argv):
    out = os.path.join(REPO, "docs", "picker-timer", "shots")
    if "--out" in argv:
        out = argv[argv.index("--out") + 1]
    os.makedirs(out, exist_ok=True)
    server, port = cdp.serve(REPO)
    try:
        for tag, w, h, dpr in VIEWPORTS:
            for theme in ("light", "dark"):
                with cdp.Browser() as br:
                    page = br.page("http://127.0.0.1:%d/%s" % (port, FIXTURE))
                    page.set_viewport(w, h)
                    page.send("Emulation.setDeviceMetricsOverride",
                              {"width": w, "height": h,
                               "deviceScaleFactor": dpr, "mobile": False})
                    D._motion(page, True)
                    page.eval("window.localStorage.clear(); 1")
                    page.eval("document.documentElement.setAttribute("
                              "'data-theme','%s'); 1" % theme)
                    R = TD.Run(cdp, br, page, w, h)

                    def snap(name):
                        shot(page, out, "%s-%s-%s.png" % (name, tag, theme),
                             w, h, dpr)

                    def psnap(pp, name, size=None):
                        pip_shot(pp, out, "%s-%s-%s.png" % (name, tag, theme),
                                 size)

                    js(page, "await openPicker(); await click('pick-go');"
                             "await wait(100);")
                    snap("board-settings-closed")
                    js(page, "await click('pick-settings');")
                    snap("settings-open")
                    js(page, "await plusRow(0, 4); await plusRow(1, 1);")
                    snap("settings-weighted")
                    js(page, "q('pick-set-name', rows()[3]).click();"
                             "await frame();")
                    snap("picknext-panel")
                    page.eval("(document.querySelector('[data-mrb-added="
                              "\"pick-set-panel\"]')||{}).scrollTop = 0; 1")
                    snap("settings-back")
                    js(page, "await click('pick-set-back'); await wait(150);")
                    snap("board-after-back")
                    js(page, "await click('pick-go'); await wait(100);")
                    snap("picknext-board")
                    # ⊕ 16 Nov 2026 — the four views
                    # 1. the board with the timer docked in its header
                    js(page, "await click('pick-timer');"
                             "await tclick('tm-toggle'); await wait(1300);")
                    snap("board-timer-strip")
                    # 2. full timer, running: −30 s / +30 s / +1 min
                    js(page, "await tclick('tm-expand'); await wait(300);")
                    snap("timer-full-remove")
                    # 3. the Mini (timer + picker) on the page, then dragged
                    js(page, "await tclick('tm-min'); await click('pick-min');"
                             "await wait(200);")
                    snap("mini-timer-picker")
                    R.drag('[data-mrb-added="tools-head"]', -(w - 360),
                           -(h - 260))
                    snap("mini-dragged")
                    # 4. the pop-out, photographed on its own target
                    if R.pclick("tools-popout"):
                        time.sleep(0.9)
                        pp = R.pip_page()
                        if pp:
                            psnap(pp, "popout-small")
                            psnap(pp, "popout-large", (960, 600))
                            pp.send("Emulation.clearDeviceMetricsOverride", {})
                            R.pclick("tools-back", doc=TD.PIPDOC, page=pp)
                            time.sleep(0.4)
                    # the finished state: a short countdown run to the end
                    js(page, "await click('tools-close');"
                             "window.MrBadmusTimer.open({view:'full'});"
                             "await frame();"
                             "tq('tm-custom-min').value='0';"
                             "tq('tm-custom-sec').value='14';"
                             "await tclick('tm-custom-set');"
                             "await tclick('tm-toggle');"
                             "await waitFor(() => state()==='warn', 8000);"
                             "await tclick('tm-toggle');")
                    snap("timer-warn")
                    js(page, "await tclick('tm-toggle');"
                             "await waitFor(() => state()==='done', 14000);"
                             "await wait(200);")
                    snap("timer-finished")
                    js(page, "await tclick('tm-reset');"
                             "await tclick('tm-preset-300');")
                    snap("timer-full")
                    js(page, "await tclick('tm-close');")
                    # the clicker: its line in the settings panel...
                    js(page, "await openPicker(); await click('pick-settings');")
                    page.eval("(document.querySelector('[data-mrb-added="
                              "\"pick-set-clicker\"]')||{scrollIntoView(){}})"
                              ".scrollIntoView({block:'center'}); 1")
                    snap("settings-clicker-keys")
                    js(page, "await click('pick-settings');")
                    # ...and the celebration, caught mid-animation, motion on
                    D._motion(page, False)
                    D._kd(page, "PageDown")
                    for _ in range(22):
                        time.sleep(0.033)
                        D._kd(page, "PageDown", repeat=True)
                    time.sleep(0.45)
                    snap("clicker-celebration")
                    D._ku(page, "PageDown")
                    time.sleep(1.6)
    finally:
        server.shutdown()
    print("done:", out)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
