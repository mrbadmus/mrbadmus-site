#!/usr/bin/env python3
"""family_dark_drive.py — a family child's dark mode, and that school gets none of it.

    python3 family_dark_drive.py [--shots DIR]

shared/family-dark.css softens a child's dark lesson and practice to the parent's
ground (blind run 2, 9 Nov 2026). The contract is two-sided:

  1. a family child: the sheet loads, the ground is rgb(42,36,32), and every text
     sample reaches 4.5:1;
  2. a school pupil, or nobody signed in: the page never requests the sheet, and the
     ground is the school dark it always was.

The floor is 4.5:1 on everything a child reads, in the states and not just at rest:
idle, selected, confirmed right, confirmed wrong, spent, handed in, and the buttons and
links a finish screen adds.

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
            # Keep the practice page's instance, to set a scenario on it.
            "(function(){var r;Object.defineProperty(window,'MrBadmusStudentRuntime',{configurable:true,get:function(){return r;},"
            "set:function(v){var m=v.mount;v.mount=function(o){return window.__fdInst=m(o);};r=v;}});})();\n"
            "window.fetch=(function(f){return function(u,o){var s=String(u&&u.url||u);"
            "if(/onrender\\.com|supabase\\.co/.test(s)){return Promise.resolve(new Response('{}',{status:200,headers:{'Content-Type':'application/json'}}));}"
            "return f(u,o);};})(window.fetch);\n"
            % "".join(("localStorage.setItem(%s,%s);" % (json.dumps(k), json.dumps(json.dumps(session))) if session else "localStorage.removeItem(%s);" % json.dumps(k)) for k in KEYS))


KS3 = "ks3/chemistry/energy-changes-in-reactions/measuring-a-temperature-change.html"
KS4 = "combined/higher/biology/organisation/heart-blood-vessels.html"
PRACTICE = "student/assignment-fixture.html"
# The states the blind runs failed in. Every option in a state, every button and link
# on the page. KS3: a wrong answer in one group, a right one in the next.
KS3_STATES = r"""(async function(){
  var groups=[].slice.call(document.querySelectorAll('.ks3-options,[data-options]')), n=0;
  var want=['0','1'];
  groups.forEach(function(g){
    var w=want[n%2], o=g.querySelector('.ks3-option[data-correct="'+w+'"]:not([disabled])')||g.querySelector('.ks3-option:not([disabled])');
    if(o){o.click();n++;}
  });
  await new Promise(function(r){setTimeout(r,500);});
  return {groups:groups.length,pressed:n,chosen:document.querySelectorAll('.ks3-option[aria-pressed="true"]').length,
    right:document.querySelectorAll('.ks3-option.is-correct').length,wrong:document.querySelectorAll('.ks3-option.is-wrong').length,
    spent:document.querySelectorAll('.ks3-option.is-spent').length};
})()"""
# KS4: press a lettered option in every block in turn; a press redraws the block, so ask again each time.
KS4_STATES = r"""(async function(){
  var tried={},n=0;
  function letters(){return [].slice.call(document.querySelectorAll('button')).filter(function(b){
    return /^[ABCD]\n/.test((b.innerText||'').trim())&&b.offsetParent&&!b.disabled;});}
  for(var i=0;i<80;i++){
    var all=letters(),b=null,bi=-1;
    for(var k=0;k<all.length;k++){var t=all[k].innerText;if(!tried[t]){b=all[k];bi=k;break;}}
    if(!b){break;}
    tried[b.innerText]=1;b.click();n++;
    await new Promise(function(r){setTimeout(r,70);});
  }
  await new Promise(function(r){setTimeout(r,400);});
  var dis=[].slice.call(document.querySelectorAll('button[disabled]')).filter(function(b){return /^[ABCD]\n/.test((b.innerText||'').trim());});
  return {pressed:n,spent:dis.length,faded:dis.filter(function(b){return /opacity/.test(b.getAttribute('style')||'');}).length,
    chosen:document.querySelectorAll('button[aria-pressed="true"]').length};
})()"""
# The links a child's finish screens add, which appear only once a lesson is done.
BACK_LINKS = r"""(function(){
  var m=document.querySelector('main')||document.body,d=document.createElement('div');d.id='fd-samples';d.style.cssText='padding:20px;display:flex;gap:12px;flex-wrap:wrap';
  d.innerHTML='<a class="btn btn--primary" href="#">Back to Today</a><a class="ks3-btn is-primary" href="#">Back to Today</a>';m.appendChild(d);return true;
})()"""
PRACTICE_HANDED = r"""(function(){
  var inst=window.__fdInst;var l=inst&&inst.logic;
  if(!l||!l.seedFor){return 'no logic';}
  l.setState(l.seedFor('Handed in'));return 'ok';
})()"""


def measure(p, label, width):
    p.eval("(document.getAnimations?document.getAnimations():[]).forEach(function(a){try{a.finish()}catch(e){}})")
    rows = p.eval(ca._MEASURE_JS) or []
    bad = []
    for row in rows:
        final, ground = ca.effective_fg(row["color"], row["chain"])
        if final is None:
            continue
        r = ca.contrast(final, ground)
        floor = 4.5      # the owner's bar for a family child: every sample, large or spent
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
            pause = lambda ms: p.eval("new Promise(function(r){setTimeout(r,%d);})" % ms, timeout=10)
            for width in (390, 1440):
                for label, path in (("KS3 lesson", KS3), ("KS4 lesson", KS4), ("practice", PRACTICE)):
                    go(path, CHILD, width)
                    st = state(p)
                    check(st["sheet"] and st["theme"] == "dark", "%s @%d: the sheet is on" % (label, width), st)
                    check(st["bg"] == "rgb(42, 36, 32)", "%s @%d: the softened ground" % (label, width), st)
                    measure(p, label + ", idle", width)
                    if path == KS3:
                        got = p.eval(KS3_STATES, timeout=20)
                        check(got["right"] and got["wrong"] and got["spent"], "KS3 @%d: right, wrong and spent options all reached" % width, got)
                        measure(p, "KS3 lesson, confirmed right, wrong and spent", width)
                        p.eval(BACK_LINKS)
                        measure(p, "KS3 lesson, buttons and links", width)
                    elif path == KS4:
                        got = p.eval(KS4_STATES, timeout=60)
                        check(got["pressed"] and got["faded"], "KS4 @%d: chosen and spent options reached" % width, got)
                        measure(p, "KS4 lesson, chosen and spent", width)
                        p.eval(BACK_LINKS)
                        measure(p, "KS4 lesson, buttons and links", width)
                    else:
                        p.eval(sb._OPT % 0)
                        pause(300)
                        measure(p, "practice, an option selected before confirm", width)
                        for n in range(3):
                            p.eval(sb._OPT % n)
                            pause(300)
                            p.eval(sb._CLICK % json.dumps("Confirm answer"))
                            pause(900)
                            measure(p, "practice, answer %d confirmed" % (n + 1), width)
                            p.eval(sb._CLICK % json.dumps("Next"))
                            pause(400)
                        h = p.eval(PRACTICE_HANDED)
                        pause(800)
                        check(h == "ok" and "YOU CHOSE" in p.eval("document.body.innerText"), "practice @%d: handed in, with its wrong answers" % width, h)
                        measure(p, "practice, handed in", width)
                        p.eval(sb._CLICK % json.dumps("Look at it"))
                        pause(600)
                        measure(p, "practice, reviewing a question", width)
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
