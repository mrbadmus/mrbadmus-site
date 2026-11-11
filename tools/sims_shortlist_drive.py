#!/usr/bin/env python3
"""sims_shortlist_drive.py: screenshot and exercise every simulation block still on a lesson page.

Reads /private/tmp/claude-501/lean-sims.json (lesson key -> routes, tags, blocks). For the first
route of each lesson: opens it at 390x844 (DPR 2, light), finds each listed block, screenshots
it, presses its controls like a pupil (ranges to middle then high, up to 4 buttons, a tap on the
canvas centre), screenshots it again and records whether anything changed.

Output goes to /private/tmp/claude-501/sims-shortlist/ (results.json + img/), never the repo.

    python3 tools/sims_shortlist_drive.py [--only a,b] [--limit N] [--redo]
"""
import argparse
import hashlib
import json
import os
import re
import sys
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
import ks3_browser as cdp  # noqa: E402

INPUT = "/private/tmp/claude-501/lean-sims.json"
OUT = "/private/tmp/claude-501/sims-shortlist"
RESULTS = os.path.join(OUT, "results.json")
W, H, DPR = 390, 844, 2
MAX_BLOCK_H = 1100
BLOCK = ["https://*", "wss://*", "http://localhost*"]   # every outside host, the live backend and database included

FIND = r"""
function find(id, cls, idx){
  var el = id ? document.querySelector('[data-activity="'+id+'"]') : null;
  if(!el && cls){ var all=document.querySelectorAll('.'+cls); el = all[idx||0] || null; }
  return el;
}
"""

# Candidates for a lesson whose block list is empty (KS4): the nearest section around each control.
AUTO = r"""
(function(){
  var seen=[], out=[];
  document.querySelectorAll('input[type=range],canvas,.ks3-sim,[data-instrument]').forEach(function(c){
    var host=c.closest('[data-activity],section,figure,.card')||c.parentElement;
    if(seen.indexOf(host)<0){seen.push(host);out.push(host);}
  });
  window.__auto=out;
  return out.map(function(h,i){return [h.getAttribute('data-activity')||('auto'+i), h.className&&h.className.split?h.className.split(' ')[0]:'']});
})()
"""

SIG = r"""
(function(el){
  var s=el.innerText+'|'+el.outerHTML.replace(/\s+/g,' ');
  var h=0;for(var i=0;i<s.length;i++){h=(h*31+s.charCodeAt(i))|0;}
  return h;
})
"""

CANVAS_HASH = r"""
(function(el){
  var out=[];var cs=el.querySelectorAll('canvas');
  for(var i=0;i<cs.length;i++){
    try{var u=cs[i].toDataURL();var h=0;for(var j=0;j<u.length;j+=7){h=(h*31+u.charCodeAt(j))|0;}out.push(h);}
    catch(e){out.push('x');}
  }
  return out.join(',');
})
"""

INFO = r"""
(function(el){
  var r=el.getBoundingClientRect();
  var vw=document.documentElement.clientWidth;
  var ranges=el.querySelectorAll('input[type=range]').length;
  var btns=el.querySelectorAll('button:not([disabled]),[role=button]:not([aria-disabled=true]),input[type=button]:not([disabled])').length;
  var canv=el.querySelectorAll('canvas').length;
  var txt=(el.innerText||'').trim();
  var label=!!el.querySelector('h2,h3,h4,legend,label,figcaption,[aria-label]')||txt.length>=20;
  return {w:Math.round(r.width),h:Math.round(r.height),vw:vw,
    blockOverflow:(r.right>vw+1||r.left<-1||el.scrollWidth>el.clientWidth+1),
    pageOverflow:document.documentElement.scrollWidth>window.innerWidth+1,
    ranges:ranges,buttons:btns,canvases:canv,controls:ranges+btns+canv,
    hasLabel:label,textLen:txt.length,
    visible:r.width>0&&r.height>0};
})
"""

PRESS = r"""
(function(el){
  var done={ranges:0,buttons:0};
  function fire(i,v){
    var set=Object.getOwnPropertyDescriptor(HTMLInputElement.prototype,'value').set;
    set.call(i,v);
    i.dispatchEvent(new Event('input',{bubbles:true}));
    i.dispatchEvent(new Event('change',{bubbles:true}));
  }
  var rs=el.querySelectorAll('input[type=range]');
  rs.forEach(function(i){
    var lo=+i.min||0,hi=(i.max===''?100:+i.max),st=+i.step||1;
    var mid=Math.round((lo+(hi-lo)*0.5)/st)*st;
    fire(i,String(mid));done.ranges++;
  });
  return done;
})
"""

PRESS_HIGH = r"""
(function(el){
  function fire(i,v){
    var set=Object.getOwnPropertyDescriptor(HTMLInputElement.prototype,'value').set;
    set.call(i,v);
    i.dispatchEvent(new Event('input',{bubbles:true}));
    i.dispatchEvent(new Event('change',{bubbles:true}));
  }
  el.querySelectorAll('input[type=range]').forEach(function(i){
    var lo=+i.min||0,hi=(i.max===''?100:+i.max),st=+i.step||1;
    fire(i,String(Math.round((lo+(hi-lo)*0.9)/st)*st));
  });
})
"""

CLICK_BUTTONS = r"""
(function(el){
  var n=0,names=[];
  var bs=el.querySelectorAll('button:not([disabled]),[role=button]:not([aria-disabled=true]),input[type=button]:not([disabled])');
  for(var i=0;i<bs.length&&n<4;i++){
    var b=bs[i];
    if(b.closest('a[href]')||b.getAttribute('href'))continue;
    var r=b.getBoundingClientRect();if(!r.width||!r.height)continue;
    names.push((b.innerText||b.value||b.getAttribute('aria-label')||'').trim().slice(0,30));
    try{b.click();}catch(e){}
    n++;
  }
  return {clicked:n,names:names};
})
"""


# Each snippet is pasted straight after `return`; a leading newline there makes JavaScript return
# undefined (automatic semicolon insertion), so they are trimmed once, here.
SIG, CANVAS_HASH, INFO, PRESS, PRESS_HIGH, CLICK_BUTTONS = (
    s.strip() for s in (SIG, CANVAS_HASH, INFO, PRESS, PRESS_HIGH, CLICK_BUTTONS))


def slugify(s):
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")[:90]


def load_results():
    try:
        with open(RESULTS) as fh:
            return json.load(fh)
    except (OSError, ValueError):
        return {}


def save_results(res):
    os.makedirs(OUT, exist_ok=True)
    tmp = RESULTS + ".tmp"
    with open(tmp, "w") as fh:
        json.dump(res, fh, indent=1)
    os.replace(tmp, RESULTS)


def setup(b):
    page = b.page("about:blank")
    page.send("Network.enable")
    page.send("Network.setBlockedURLs", {"urls": BLOCK})
    page.send("Emulation.setDeviceMetricsOverride",
              {"width": W, "height": H, "deviceScaleFactor": DPR, "mobile": True})
    page.send("Emulation.setEmulatedMedia", {"features": [{"name": "prefers-color-scheme", "value": "light"}]})
    page.send("Page.addScriptToEvaluateOnNewDocument",
              {"source": "try{localStorage.setItem('mrb-theme','light')}catch(e){}"})
    return page


def js(page, expr):
    raw = page.eval("JSON.stringify(%s)" % expr)
    return json.loads(raw) if raw else None


def shot(page, sel_js, path):
    """Screenshot the block's own rectangle after scrolling it into view."""
    r = js(page, "(function(){%s var el=%s;el.scrollIntoView({block:'start'});"
                 "var b=el.getBoundingClientRect();return {x:b.left+scrollX,y:b.top+scrollY,w:b.width,h:b.height}})()"
           % (FIND, sel_js))
    time.sleep(0.5)
    r = js(page, "(function(){%s var el=%s;var b=el.getBoundingClientRect();"
                 "return {x:b.left+scrollX,y:b.top+scrollY,w:b.width,h:b.height}})()" % (FIND, sel_js))
    clip = {"x": max(0, r["x"]), "y": max(0, r["y"]), "width": max(1, min(r["w"], W)),
            "height": max(1, min(r["h"], MAX_BLOCK_H)), "scale": 1}
    res = page.send("Page.captureScreenshot", {"format": "jpeg", "quality": 60,
                                               "captureBeyondViewport": True, "clip": clip})
    import base64
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "wb") as fh:
        fh.write(base64.b64decode(res["data"]))


def tap_canvas(page, sel_js):
    r = js(page, "(function(){%s var el=%s;var c=el.querySelector('canvas');if(!c)return null;"
                 "c.scrollIntoView({block:'center'});var b=c.getBoundingClientRect();"
                 "return {x:b.left+b.width/2,y:b.top+b.height/2,ok:b.width>0&&b.height>0}})()" % (FIND, sel_js))
    if not r or not r.get("ok"):
        return False
    time.sleep(0.2)
    for t, extra in (("mousePressed", {"buttons": 1, "clickCount": 1}), ("mouseReleased", {"clickCount": 1})):
        page.send("Input.dispatchMouseEvent", dict({"type": t, "x": r["x"], "y": r["y"], "button": "left"}, **extra))
    return True


def drive_block(page, key, n, bid, bcls, idx, slug):
    sel = "find(%s,%s,%d)" % (json.dumps(bid), json.dumps(bcls), idx)
    out = {"id": bid, "class": bcls, "found": False}
    present = js(page, "(function(){%s return !!%s})()" % (FIND, sel))
    if not present:
        return out
    out["found"] = True
    base = "(function(){%s var el=%s;return " % (FIND, sel)
    info = js(page, base + INFO + "(el)})()")
    out.update(info)
    out["sig_before"] = js(page, base + SIG + "(el)})()")
    out["canvas_before"] = js(page, base + CANVAS_HASH + "(el)})()")
    before = "img/%s-%d-before.jpg" % (slug, n)
    after = "img/%s-%d-after.jpg" % (slug, n)
    shot(page, sel, os.path.join(OUT, before))
    page.console_errors()
    url0 = page.eval("location.href")
    js(page, base + PRESS + "(el)})()")
    time.sleep(0.4)
    js(page, base + PRESS_HIGH + "(el)})()")
    time.sleep(0.4)
    out["buttons_clicked"] = js(page, base + CLICK_BUTTONS + "(el)})()")
    time.sleep(0.6)
    out["canvas_tapped"] = tap_canvas(page, sel)
    time.sleep(0.6)
    out["navigated"] = page.eval("location.href") != url0
    if out["navigated"]:
        page.goto(url0, settle=2.0)
    out["sig_after"] = js(page, base + SIG + "(el)})()")
    out["canvas_after"] = js(page, base + CANVAS_HASH + "(el)})()")
    out["responded"] = (out["sig_before"] != out["sig_after"]) or (out["canvas_before"] != out["canvas_after"])
    out["console_errors"] = [e for e in page.console_errors() if "ERR_BLOCKED_BY_CLIENT" not in e][:5]
    shot(page, sel, os.path.join(OUT, after))
    out["before_img"], out["after_img"] = before, after
    return out


def drive_lesson(page, base, key, entry):
    route = entry["routes"][0]
    slug = slugify(key)
    page.goto(base + "/" + route, settle=2.5)
    time.sleep(0.4)
    errs0 = [e for e in page.console_errors() if "ERR_BLOCKED_BY_CLIENT" not in e][:5]
    blocks = entry.get("blocks") or []
    auto = False
    if not blocks:
        blocks = js(page, AUTO) or []
        auto = True
    rec = {"path": key, "route": route, "tags": entry.get("tags", []), "auto_detected": auto,
           "load_errors": errs0,
           "title": page.eval("(document.querySelector('h1')||{}).innerText||document.title") or "",
           "blocks": []}
    seen_cls = {}
    for n, (bid, bcls) in enumerate(blocks):
        idx = seen_cls.get(bcls, 0)
        seen_cls[bcls] = idx + 1
        if auto:
            # auto hosts are addressed by position in window.__auto
            bid_ = None
            sel_cls = None
            # make the host findable by a temporary attribute
            page.eval("(function(){var h=window.__auto[%d];if(h)h.setAttribute('data-activity','__sims%d')})()" % (n, n))
            bid_ = "__sims%d" % n
            rec["blocks"].append(drive_block(page, key, n, bid_, sel_cls, 0, slug))
        else:
            rec["blocks"].append(drive_block(page, key, n, bid, bcls, idx, slug))
    return rec


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--only", default="")
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--redo", action="store_true")
    a = ap.parse_args()
    with open(INPUT) as fh:
        lessons = json.load(fh)
    only = [s for s in a.only.split(",") if s]
    keys = [k for k in sorted(lessons) if not only or any(s in k or s in lessons[k]["routes"][0] for s in only)]
    res = load_results()
    todo = [k for k in keys if a.redo or k not in res]
    if a.limit:
        todo = todo[:a.limit]
    print("%d lessons selected, %d to drive" % (len(keys), len(todo)), flush=True)
    os.makedirs(OUT, exist_ok=True)
    server, port = cdp.serve(os.path.join(ROOT, "mrbadmus_site"))
    base = "http://127.0.0.1:%d" % port
    b = cdp.Browser().start()
    page = setup(b)
    try:
        for i, key in enumerate(todo, 1):
            rec = None
            for attempt in (1, 2):
                try:
                    rec = drive_lesson(page, base, key, lessons[key])
                    break
                except Exception as e:  # CDP, JS, socket: restart Chrome and retry once
                    err = "%s: %s" % (type(e).__name__, e)
                    print("  ! %s attempt %d: %s" % (key, attempt, err), flush=True)
                    try:
                        b.close()
                    except Exception:
                        pass
                    b = cdp.Browser().start()
                    page = setup(b)
                    rec = {"path": key, "route": lessons[key]["routes"][0], "failed": err, "blocks": []}
            res[key] = rec
            save_results(res)
            print("[%d/%d] %s: %d blocks%s" % (i, len(todo), key, len(rec["blocks"]),
                                              "  FAILED" if rec.get("failed") else ""), flush=True)
    finally:
        try:
            b.close()
        except Exception:
            pass
        server.shutdown()


if __name__ == "__main__":
    main()
