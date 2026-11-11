#!/usr/bin/env python3
"""tools/picker_timer_shots.py — screenshots of the picker's settings panel and
the classroom timer, for review.

    python3 tools/picker_timer_shots.py [--out DIR]

Writes PNGs to docs/picker-timer/shots/ (default) at 390x844 (device scale 2),
1440x900 and 1920x1080, light and dark. It drives the class-detail FIXTURE the
way `teacher_picker_drive.py` does (served by `ks3_browser.serve`, pressed by
`data-mrb-added` marker) and borrows that file's page-side helpers.

Light gets every scene; dark gets the four that carry the most colour (the
weighted panel, the pick-next panel, the full timer and the last-ten-seconds
digits), which keeps the set to a size a person will actually look at.
"""
import base64
import time
import json
import os
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, REPO)

import ks3_browser as cdp                                   # noqa: E402
import teacher_picker_drive as D                            # noqa: E402

FIXTURE = D.FIXTURE
VIEWPORTS = (("390", 390, 844, 2), ("1440", 1440, 900, 1),
             ("1920", 1920, 1080, 1))
DARK_SCENES = ("settings-weighted", "picknext-panel", "timer-full",
               "timer-warn", "settings-clicker-keys", "clicker-celebration")


def js(page, body, timeout=60):
    return json.loads(page.eval(D.wrap(D.TIMER_PRE, body +
                                        "\nreturn JSON.stringify(out);"),
                                timeout=timeout))


def shot(page, out, name, w, h, dpr):
    page.send("Emulation.setDeviceMetricsOverride",
              {"width": w, "height": h, "deviceScaleFactor": dpr,
               "mobile": False})
    time.sleep(0.25)
    res = page.send("Page.captureScreenshot",
                    {"format": "png", "fromSurface": True})
    with open(os.path.join(out, name), "wb") as fh:
        fh.write(base64.b64decode(res["data"]))
    print("   wrote", name)


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
                    scenes = []

                    def want(name):
                        return theme == "light" or name in DARK_SCENES

                    def snap(name):
                        if want(name):
                            shot(page, out, "%s-%s-%s.png" % (name, tag, theme),
                                 w, h, dpr)

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
                    js(page, "await click('pick-settings');"
                             "await click('pick-go'); await wait(100);")
                    snap("picknext-board")
                    # timer floating over the picker
                    js(page, "q('pick-timer').click(); await frame();"
                             "await tclick('tm-preset-300');"
                             "await tclick('tm-toggle'); await wait(1300);")
                    snap("timer-float-over-picker")
                    js(page, "q('pick-timer').click(); await frame();"
                             "await wait(300);")
                    snap("timer-full")
                    js(page, "await tclick('tm-close');"
                             "window.MrBadmusTimer.open({view:'full'});"
                             "await frame();"
                             "tq('tm-custom-min').value='0';"
                             "tq('tm-custom-sec').value='14';"
                             "await tclick('tm-custom-set');"
                             "await tclick('tm-toggle');"
                             "await waitFor(() => state()==='warn', 8000);"
                             "await tclick('tm-toggle');")
                    snap("timer-warn")
                    js(page, "await tclick('tm-close');")
                    # the clicker: its line in the settings panel...
                    js(page, "await click('pick-settings');")
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
