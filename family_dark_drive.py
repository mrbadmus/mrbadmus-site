#!/usr/bin/env python3
"""family_dark_drive.py — a family child's dark mode, and that school gets none of it.

    python3 family_dark_drive.py [--shots DIR]

shared/family-dark.css softens a child's dark lesson and practice to the parent's
ground (blind run 2, 9 Nov 2026). The contract is two-sided:

  1. a family child: the sheet loads, the ground is rgb(42,36,32), and every text
     sample reaches 4.5:1 (3:1 for large text and disabled controls), at rest and
     in the states the blind run failed: a chosen option on a KS3 and a KS4 lesson,
     and a marked practice review;
  2. a school pupil, or nobody signed in: the page never requests the sheet, and the
     ground is the school dark it always was.

Offline: served from the repo, the backend unreachable, sessions stubbed in storage.
"""
from __future__ import annotations

import argparse
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import contrast_audit as ca  # noqa: E402
import ks3_browser as cdp  # noqa: E402
import student_behaviour as sb  # noqa: E402

FAILS = []


def check(ok, what, detail=None):
    print(("  OK  " if ok else "  NO  ") + what + ("" if ok or detail is None else "  — %s" % (json.dumps(detail, ensure_ascii=False)[:900],)))
    if not ok:
        FAILS.append(what)


# On localhost config.js reads the TEST project's key. Both, so this cannot pass by
# simply not finding a session.
KEYS = ["sb-qeppkiswvclkkwbxmlok-auth-token", "sb-urklkrwevjtlfbwnipjn-auth-token"]
FUTURE = 4102444800
CHILD = {"access_token": "x.y.z", "refresh_token": "r", "expires_at": FUTURE, "user": {"id": "kid-ada", "email": "ada.comet@children.mrbadmus.internal"}}
PUPIL = {"access_token": "x.y.z", "refresh_token": "r", "expires_at": FUTURE, "user": {"id": "pupil-1", "email": "pupil@rainford.example"}}


def pre(session):
    return ("try{localStorage.setItem('mrb-theme','dark');%s}catch(e){}\n"
            "window.fetch=(function(f){return function(u,o){var s=String(u&&u.url||u);"
            "if(/onrender\\.com|supabase\\.co/.test(s)){return Promise.resolve(new Response('{}',{status:200,headers:{'Content-Type':'application/json'}}));}"
            "return f(u,o);};})(window.fetch);\n"
            % "".join(("localStorage.setItem(%s,%s);" % (json.dumps(k), json.dumps(json.dumps(session))) if session else "localStorage.removeItem(%s);" % json.dumps(k)) for k in KEYS))


KS3 = "ks3/chemistry/energy-changes-in-reactions/measuring-a-temperature-change.html"
KS4 = "combined/higher/biology/organisation/heart-blood-vessels.html"
PRACTICE = "student/assignment-fixture.html"
# Press the first answerable option; the state the blind run failed in.
PRESS = ("(function(){var o=document.querySelector('.ks3-option:not([disabled])');if(o){o.scrollIntoView();o.click();}"
         "return !!o;})()")
PRACTICE_REVIEW = None


def measure(p, label, width):
    p.eval("(document.getAnimations?document.getAnimations():[]).forEach(function(a){try{a.finish()}catch(e){}})")
    rows = p.eval(ca._MEASURE_JS) or []
    bad = []
    for row in rows:
        final, ground = ca.effective_fg(row["color"], row["chain"])
        if final is None:
            continue
        r = ca.contrast(final, ground)
        floor = ca.AA_LARGE if ca.is_large(row["fontSize"], row["fontWeight"]) else ca.AA_NORMAL
        if row["kind"] == "disabled-control" or row.get("disabled"):
            floor = ca.DISABLED_FLOOR
        if r < floor:
            bad.append({"r": round(r, 2), "floor": floor, "t": row["text"][:30], "sel": row["sel"][-70:],
                        "fg": ca.hexof(final), "bg": ca.hexof(ground), "raw": row["color"]})
    seen, uniq = set(), []
    for b in sorted(bad, key=lambda x: x["r"]):
        k = (b["fg"], b["bg"], b["sel"])
        if k not in seen:
            seen.add(k)
            uniq.append(b)
    check(not uniq, "%s @%d: %d samples, all at AA" % (label, width, len(rows)), uniq[:14])


def state(p):
    return p.eval("({sheet:!!document.querySelector('link[href*=\"family-dark\"]'),"
                  "session:(function(){try{return JSON.parse(localStorage.getItem(MrBadmusConfig.AUTH_STORAGE_KEY)).user.email}catch(e){return null}})(),"
                  "bg:getComputedStyle(document.body).backgroundColor,"
                  "theme:document.documentElement.getAttribute('data-theme')})")


def settle(p, cond="document.readyState==='complete'", ms=6000):
    p.eval("(async function(){var t=Date.now();while(Date.now()-t<%d){if(%s)return true;await new Promise(function(r){setTimeout(r,60);});}return false;})()" % (ms, cond),
           timeout=ms / 1000 + 10)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--shots", default=None)
    args = ap.parse_args()
    shots = args.shots or os.path.join(cdp.gate_tmp(), "family-dark")
    os.makedirs(shots, exist_ok=True)
    server, port = cdp.serve(HERE, 0)
    try:
        with cdp.Browser() as b:
            p = b.attach()
            ident = None

            def go(path, session, width):
                nonlocal ident
                if ident is not None:
                    p.send("Page.removeScriptToEvaluateOnNewDocument", {"identifier": ident})
                ident = p.send("Page.addScriptToEvaluateOnNewDocument", {"source": pre(session)}).get("identifier")
                p.set_viewport(width, 1400 if width > 500 else 1800)
                p.goto("http://127.0.0.1:%d/%s" % (port, path))
                settle(p)
                # The practice fixture runs the page without its live loader, which is
                # what brings config.js on student/assignment.html. Load it as that does.
                if path == PRACTICE:
                    p.eval("new Promise(function(r){var s=document.createElement('script');s.src='/shared/config.js';s.onload=r;s.onerror=r;document.head.appendChild(s);})", timeout=10)
                p.eval("new Promise(function(r){setTimeout(r,700);})", timeout=10)

            print("\n── school gets none of it ──")
            for who, sess in (("a school pupil", PUPIL), ("nobody signed in", None)):
                for path in (KS3, KS4, PRACTICE):
                    go(path, sess, 1280)
                    st = state(p)
                    check(not st["sheet"], "%s on %s: the sheet is never requested" % (who, path), st)
                    check(st["session"] == (sess and sess["user"]["email"]), "%s on %s: that really was the session the page read" % (who, path), st)
                    want = "rgb(22, 18, 13)" if path == PRACTICE else "rgb(22, 18, 14)"
                    check(st["bg"] == want or path == PRACTICE and st["bg"] in ("rgb(22, 18, 13)", "rgb(22, 18, 14)"),
                          "%s on %s: the ground is the school dark" % (who, path), st)

            print("\n── a family child ──")
            for width in (390, 1280):
                for label, path in (("KS3 lesson", KS3), ("KS4 lesson", KS4), ("practice", PRACTICE)):
                    go(path, CHILD, width)
                    st = state(p)
                    check(st["sheet"] and st["theme"] == "dark", "%s @%d: the sheet is on" % (label, width), st)
                    check(st["bg"] == "rgb(42, 36, 32)", "%s @%d: the softened ground" % (label, width), st)
                    measure(p, label, width)
                    if path in (KS3, KS4):
                        if p.eval(PRESS):
                            p.eval("new Promise(function(r){setTimeout(r,500);})", timeout=10)
                            measure(p, label + ", an option chosen", width)
                    if path == PRACTICE:
                        # The review a child reads: each confirmed answer, right and wrong.
                        for n in range(3):
                            p.eval(sb._OPT % n)
                            p.eval("new Promise(function(r){setTimeout(r,300);})", timeout=10)
                            p.eval(sb._CLICK % json.dumps("Confirm answer"))
                            p.eval("new Promise(function(r){setTimeout(r,900);})", timeout=10)
                            measure(p, "practice, answer %d confirmed" % (n + 1), width)
                            p.eval(sb._CLICK % json.dumps("Next"))
                            p.eval("new Promise(function(r){setTimeout(r,400);})", timeout=10)
                    if width == 390:
                        p.screenshot(os.path.join(shots, "%s-390.png" % label.replace(" ", "-")))
    finally:
        server.shutdown()
    print("\n%s — %d failure(s)" % ("PASS" if not FAILS else "FAIL", len(FAILS)))
    for f in FAILS:
        print("   ✗ " + f)
    return 1 if FAILS else 0


if __name__ == "__main__":
    raise SystemExit(main())
