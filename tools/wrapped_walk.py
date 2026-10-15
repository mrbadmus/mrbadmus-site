#!/usr/bin/env python3
"""wrapped_walk.py — walks MrBadmus Wrapped and screenshots every card.

NOT a gate (it asserts only that the share PNG is 1080x1920 and that every
story opens); it is the evidence run for the Wrapped build. tools/ is not a
root script, so gate_registry's coverage() does not look at it.

Two modes:

  --harness   serves the REPO ROOT, opens docs/wrapped/harness.html and feeds
              shared/wrapped.js the canned JSON in docs/wrapped/canned.json
              through the localhost-only MRBWrapped.open({data}) hook. Needs no
              database, no build.

  (default)   serves mrbadmus_site/, signs in on auth.html?env=test as each
              TEST account and opens the real class page with ?wrapped=preview.
              Env: WRAPPED_BUSY_EMAIL WRAPPED_LIGHT_EMAIL WRAPPED_ZERO_EMAIL
                   WRAPPED_TEACHER_EMAIL WRAPPED_PASSWORD WRAPPED_CLASS_ID

Drives the installed Chrome (playwright, channel="chrome"); downloads nothing.
Screenshots go to --shots (default ~/tmp/wrapped-shots), never into the repo.

    python3 tools/wrapped_walk.py --harness
    python3 tools/wrapped_walk.py --shots ~/tmp/wrapped-live
"""
import argparse
import functools
import http.server
import json
import os
import socketserver
import struct
import sys
import threading

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
VIEWPORTS = [("phone", 390, 844), ("desktop", 1440, 900)]
THEMES = ["light", "dark"]
SETTLE_MS = 3000
ONLY = None


class Quiet(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *a):
        pass


def serve(directory):
    handler = functools.partial(Quiet, directory=directory)
    socketserver.ThreadingTCPServer.allow_reuse_address = True
    srv = socketserver.ThreadingTCPServer(("127.0.0.1", 0), handler)
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    return srv, srv.server_address[1]


def png_size(path):
    with open(path, "rb") as fh:
        head = fh.read(24)
    if head[:8] != b"\x89PNG\r\n\x1a\n":
        return None
    return struct.unpack(">II", head[16:24])


def card_count(page):
    return page.evaluate("document.querySelectorAll('.wr-bars i').length")


def walk_story(page, tag, shots, problems, share=False, rm=False):
    page.wait_for_selector(".wr-bars i", timeout=15000)
    page.wait_for_timeout(600)
    n = card_count(page)
    for i in range(n):
        page.wait_for_timeout(SETTLE_MS)
        kind = page.evaluate("document.querySelector('.wr-card')?.dataset.kind || '?'")
        path = os.path.join(shots, "%s-%02d-%s%s.png" % (tag, i + 1, kind, "-rm" if rm else ""))
        page.screenshot(path=path)
        # nothing may overflow the stage sideways
        over = page.evaluate("""() => { const s = document.querySelector('.wr-stage').getBoundingClientRect();
            const bad = []; document.querySelectorAll('.wr-card *').forEach(e => { if (e.closest('.wr-art')) return; const r = e.getBoundingClientRect();
            if (r.width && (r.right > s.right + 2 || r.left < s.left - 2)) bad.push(e.className || e.tagName); });
            return bad.slice(0, 4); }""")
        if over:
            problems.append("%s card %d overflows: %s" % (tag, i + 1, over))
        if kind == "summary" and share:
            with page.expect_download(timeout=20000) as dl:
                page.get_by_role("button", name="Save image").click()
            out = os.path.join(shots, "%s-share.png" % tag)
            dl.value.save_as(out)
            size = png_size(out)
            if size != (1080, 1920):
                problems.append("%s share image is %r, not 1080x1920" % (tag, size))
            else:
                print("  share image ok:", out)
        if i < n - 1:
            page.keyboard.press("ArrowRight")
    page.keyboard.press("Escape")
    page.wait_for_timeout(300)
    if page.evaluate("!!document.querySelector('.wr-ov')"):
        problems.append("%s: Escape did not close the story" % tag)


def run_harness(pw, base, shots, problems):
    canned = json.load(open(os.path.join(ROOT, "docs", "wrapped", "canned.json")))
    personas = [("busy", "pupil"), ("light", "pupil"), ("classband", "pupil"),
                ("zero", "pupil"), ("teacher", "teacher")]
    browser = pw.chromium.launch(channel="chrome")
    try:
        for vp, w, h in VIEWPORTS:
            for theme in THEMES:
                for key, role in personas:
                    if ONLY and key != ONLY:
                        continue
                    ctx = browser.new_context(viewport={"width": w, "height": h}, accept_downloads=True)
                    page = ctx.new_page()
                    page.goto("%s/docs/wrapped/harness.html?theme=%s" % (base, theme))
                    page.wait_for_function("!!window.MRBWrapped")
                    page.evaluate("r => MRBWrapped.dev({role: r})", role)
                    page.evaluate("d => MRBWrapped.open({data: d})", canned[key])
                    tag = "%s-%s-%s-%s" % (vp, theme, key, role)
                    print("walking", tag)
                    walk_story(page, tag, shots, problems, share=(role == "pupil" and key != "zero"))
                    ctx.close()
    finally:
        browser.close()


def sign_in(page, base, email, pw):
    page.goto("%s/auth.html?env=test" % base)
    page.wait_for_selector("#signin-email", timeout=20000)
    page.fill("#signin-email", email)
    page.fill("#signin-password", pw)
    page.click("#btn-signin")
    page.wait_for_function("Object.keys(localStorage).some(k => k.indexOf('-auth-token') > -1)", timeout=30000)


def run_live(pw, base, shots, problems):
    env = os.environ
    need = ["WRAPPED_BUSY_EMAIL", "WRAPPED_LIGHT_EMAIL", "WRAPPED_ZERO_EMAIL",
            "WRAPPED_TEACHER_EMAIL", "WRAPPED_PASSWORD", "WRAPPED_CLASS_ID"]
    missing = [k for k in need if not env.get(k)]
    if missing:
        sys.exit("missing env: " + ", ".join(missing))
    cls = env["WRAPPED_CLASS_ID"]
    personas = [("busy", "WRAPPED_BUSY_EMAIL", "pupil"), ("light", "WRAPPED_LIGHT_EMAIL", "pupil"),
                ("zero", "WRAPPED_ZERO_EMAIL", "pupil"), ("teacher", "WRAPPED_TEACHER_EMAIL", "teacher")]
    browser = pw.chromium.launch(channel="chrome")
    try:
        for key, var, role in personas:
            if ONLY and key != ONLY:
                continue
            for vp, w, h in VIEWPORTS:
                for theme in THEMES:
                    ctx = browser.new_context(viewport={"width": w, "height": h}, accept_downloads=True)
                    ctx.add_init_script("try{localStorage.setItem('mrb-theme','%s')}catch(e){}" % theme)
                    page = ctx.new_page()
                    sign_in(page, base, env[var], env["WRAPPED_PASSWORD"])
                    path = ("/teacher/class-detail.html" if role == "teacher" else "/student/class.html")
                    page.goto("%s%s?class=%s&env=test&wrapped=preview" % (base, path, cls))
                    tag = "%s-%s-%s-%s" % (vp, theme, key, role)
                    print("walking", tag)
                    try:
                        page.wait_for_selector(".wr-ov", timeout=45000)
                        walk_story(page, tag, shots, problems, share=(role == "pupil" and key != "zero"))
                    except Exception as e:  # noqa: BLE001
                        problems.append("%s: %s" % (tag, str(e).splitlines()[0]))
                    ctx.close()
    finally:
        browser.close()


def closed_gate(pw, base, problems):
    """release_at is in the future on TEST: nobody outside the preview list may see Wrapped."""
    env = os.environ
    cls = env["WRAPPED_CLASS_ID"]
    cases = [
        ("busy pupil, no wrapped=preview", "WRAPPED_BUSY_EMAIL", "/student/class.html", ""),
        ("non-preview pupil, wrapped=preview", "WRAPPED_PUPIL_NONPREVIEW_EMAIL", "/student/class.html", "&wrapped=preview"),
        ("non-preview teacher, wrapped=preview", "WRAPPED_TEACHER_OTHER_EMAIL", "/teacher/class-detail.html", "&wrapped=preview"),
    ]
    browser = pw.chromium.launch(channel="chrome")
    try:
        for label, var, path, extra in cases:
            if not env.get(var):
                problems.append("closed gate (%s): env %s missing" % (label, var))
                continue
            ctx = browser.new_context(viewport={"width": 390, "height": 844})
            page = ctx.new_page()
            try:
                sign_in(page, base, env[var], env["WRAPPED_PASSWORD"])
                page.goto("%s%s?class=%s&env=test%s" % (base, path, cls, extra))
                page.wait_for_load_state("load")
                page.wait_for_timeout(6000)
                seen = page.evaluate("""() => ({btn: document.querySelectorAll('[data-mrb-added="wrapped-open"]').length,
                    ov: document.querySelectorAll('.wr-ov').length})""")
                print("closed gate:", label, seen)
                if seen["btn"] or seen["ov"]:
                    problems.append("closed gate FAILED (%s): %r" % (label, seen))
            except Exception as e:  # noqa: BLE001
                problems.append("closed gate (%s): %s" % (label, str(e).splitlines()[0]))
            ctx.close()
    finally:
        browser.close()


def reduced_motion(pw, base, shots, problems):
    env = os.environ
    browser = pw.chromium.launch(channel="chrome")
    try:
        ctx = browser.new_context(viewport={"width": 390, "height": 844}, reduced_motion="reduce", accept_downloads=True)
        ctx.add_init_script("try{localStorage.setItem('mrb-theme','light')}catch(e){}")
        page = ctx.new_page()
        sign_in(page, base, env["WRAPPED_BUSY_EMAIL"], env["WRAPPED_PASSWORD"])
        page.goto("%s/student/class.html?class=%s&env=test&wrapped=preview" % (base, env["WRAPPED_CLASS_ID"]))
        tag = "phone-light-busy-pupil-rm"
        print("walking", tag)
        try:
            page.wait_for_selector(".wr-ov", timeout=45000)
            walk_story(page, tag, shots, problems, rm=True)
        except Exception as e:  # noqa: BLE001
            problems.append("%s: %s" % (tag, str(e).splitlines()[0]))
        ctx.close()
    finally:
        browser.close()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--shots", default=os.path.expanduser("~/tmp/wrapped-shots"))
    ap.add_argument("--harness", action="store_true")
    ap.add_argument("--vp", help="only this viewport: phone | desktop")
    ap.add_argument("--theme", help="only this theme: light | dark")
    ap.add_argument("--persona", help="only this persona (busy, light, classband, zero, teacher)")
    a = ap.parse_args()
    global VIEWPORTS, THEMES, ONLY
    if a.vp:
        VIEWPORTS = [v for v in VIEWPORTS if v[0] == a.vp]
    if a.theme:
        THEMES = [a.theme]
    ONLY = a.persona
    os.makedirs(a.shots, exist_ok=True)
    from playwright.sync_api import sync_playwright
    srv, port = serve(ROOT if a.harness else os.path.join(ROOT, "mrbadmus_site"))
    base = "http://localhost:%d" % port
    problems = []
    try:
        with sync_playwright() as pw:
            (run_harness if a.harness else run_live)(pw, base, a.shots, problems)
            if not a.harness and not ONLY:
                closed_gate(pw, base, problems)
                reduced_motion(pw, base, a.shots, problems)
    finally:
        srv.shutdown()
    if problems:
        print("\nPROBLEMS")
        for p in problems:
            print(" -", p)
        return 1
    print("\nwalk clean; shots in", a.shots)
    return 0


if __name__ == "__main__":
    sys.exit(main())
