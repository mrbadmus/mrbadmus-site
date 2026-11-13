#!/usr/bin/env python3
"""lean_pilot_drive.py: walks every lean pilot page at 390px in headless Chrome.

The 5 KS3 lessons and the 8 energy lessons on all four routes (37 pages). On each page:

  structure   only lean sections on the page; no bench, simulation or canvas; one
              instrument shell on KS3 (Start here); KS4 route cards exactly as the record says
              (Higher-only absent on CF/TF, Triple-only absent on CF/CH); required practical
              numbered 14 on Combined and 1 on Triple
  Start here  both options, reply is the record's, no "Good guess" / "Fair guess"
  cards       every card opens and closes by tap and by keyboard (Enter, Space); a swipe
              opens and closes one; Dive deeper opens; reveal cells open one by one and
              "Show all" opens and closes the table
  practice    every option of the marked rungs and the quiz bank that can be clicked
  survival    a card stays open after a rail scroll update and after answering a question
  health      no console errors, no horizontal overflow with everything open

and, in dark, every page loads, opens everything and has no overflow or console error.
Light and dark screenshots of how-breathing-works and efficiency go to $MRB_SHOTS.

Every request off 127.0.0.1 is blocked. Nothing is written into the repo.

    python3 lean_pilot_drive.py [--only SUBSTRING] [--no-dark]
"""
import argparse
import json
import os
import sys
import time

import config_env
import glob
import ks3_browser as cdp

ROOT = os.path.dirname(os.path.abspath(__file__))
os.chdir(ROOT)
sys.path.insert(0, ROOT)

W, H = 390, 844
BLOCK = ["https://*", "wss://*", "http://localhost*", "*supabase.co*",
         "*%s*" % config_env.PROD_BACKEND_PLATFORM]
ROUTES = ["CF", "CH", "TF", "TH"]
ROUTE_DIR = {"CF": "combined/foundation", "CH": "combined/higher",
             "TF": "triple/foundation", "TH": "triple/higher"}
FLAG_ROUTES = {"isHigher": {"CH", "TH"}, "isTriple": {"TF", "TH"}, "notHigher": {"CF", "TF"},
               "notTriple": {"CF", "CH"}, "isTH": {"TH"}}
SHOT_PAGES = ("how-breathing-works", "efficiency")

CAPTURING = False
FAILS = []
PASSED = []
QUIZ_SIZES = {}
POSTED = {}


def fail(page, msg):
    FAILS.append("%s: %s" % (page, msg))
    print("  FAIL  %s: %s" % (page, msg))


class Drive:
    def __init__(self, page, tag):
        self.p, self.tag = page, tag
        self.checks = 0

    def js(self, expr):
        raw = self.p.eval("JSON.stringify((function(){%s})())" % expr)
        return json.loads(raw) if raw else None

    def check(self, cond, msg):
        self.checks += 1
        if not cond:
            fail(self.tag, msg)
        return cond

    def harvest(self):
        """Move what the page has posted so far into self.posted (the page keeps none after a reload)."""
        time.sleep(0.7)                   # a post goes out after its token promise resolves
        got = self.js("var p=window.__posted||[];window.__posted=[];return p")
        self.posted = getattr(self, "posted", []) + (got or [])

    def key(self, k):
        code = {"Enter": (13, "\r"), " ": (32, " ")}[k]
        base = {"key": k, "code": "Space" if k == " " else k,
                "windowsVirtualKeyCode": code[0], "nativeVirtualKeyCode": code[0]}
        self.p.send("Input.dispatchKeyEvent", dict(base, type="keyDown", text=code[1]))
        self.p.send("Input.dispatchKeyEvent", dict(base, type="keyUp"))
        time.sleep(0.12)

    def click_at(self, sel, idx=0):
        r = self.js("var e=document.querySelectorAll(%s)[%d];e.scrollIntoView({block:'center',behavior:'instant'});"
                    "var b=e.getBoundingClientRect();return [b.left+b.width/2,b.top+b.height/2]"
                    % (json.dumps(sel), idx))
        time.sleep(0.5)
        r = self.js("var e=document.querySelectorAll(%s)[%d];var b=e.getBoundingClientRect();"
                    "return [b.left+b.width/2,b.top+b.height/2]" % (json.dumps(sel), idx))
        for t in ("mousePressed", "mouseReleased"):
            self.p.send("Input.dispatchMouseEvent", {"type": t, "x": r[0], "y": r[1],
                                                       "button": "left", "clickCount": 1})
        time.sleep(0.2)


def load(page, url, settle=2.5):
    page.goto(url, settle=settle)
    time.sleep(0.4)


# ── in-page readers ─────────────────────────────────────────────────────

CARD_STATE = """
var btns=document.querySelectorAll('.lean-card-btn');var b=btns[%d];var c=b.closest('.lean-card');
var body=c.querySelector('.lean-card-body');
return {exp:b.getAttribute('aria-expanded'),open:c.hasAttribute('data-lean-open'),
        vis:body.offsetHeight>0, tag:b.tagName};
"""
OVERFLOW = ("var d=document.documentElement;return {sw:d.scrollWidth,cw:d.clientWidth,"
            "bw:document.body.scrollWidth};")
STRUCT = """
var out={ids:[],bad:[],instr:document.querySelectorAll('[data-instrument]').length,
  bench:document.querySelectorAll('canvas,.ks3-bell,[data-sim],[data-bench],.ks3-sim').length,
  titles:[].map.call(document.querySelectorAll('.lean-card-title'),function(x){return x.textContent.trim()}),
  words:document.querySelectorAll('.lean-word').length,
  h1:(document.querySelector('h1')||{}).textContent,
  bigq:!!document.querySelector('.ks3-bigq'), draft:!!document.querySelector('.ks3-review-flag'),
  keynote:!!document.querySelector('.ks3-keynote,#s-keynote'),
  fact:!!document.querySelector('.lean-fact'), deeper:!!document.querySelector('.lean-deeper-btn'),
  rungs:[].map.call(document.querySelectorAll('.ks3-rung h3'),function(x){return x.textContent.trim()}),
  text:document.body.innerText};
var lesson=document.querySelector('.ks3-lesson');
[].forEach.call(lesson.children,function(c){ if(c.id) out.ids.push(c.id); });
return out;
"""
ALLOWED_IDS = {"s-hook", "s-words", "s-knowledge", "s-fact", "s-ladder", "s-deeper"}


def structure(d, rec, ks, route, slug):
    s = d.js(STRUCT)
    d.check(set(s["ids"]) <= ALLOWED_IDS, "unexpected section ids %s" % sorted(set(s["ids"]) - ALLOWED_IDS))
    for want in ("s-hook", "s-words", "s-knowledge", "s-fact", "s-ladder", "s-deeper"):
        d.check(want in s["ids"], "missing section %s" % want)
    d.check(s["bench"] == 0, "embedded bench/simulation markup (%d)" % s["bench"])
    if ks == 3:
        d.check(s["instr"] == 1, "%d instrument shells (want 1, Start here)" % s["instr"])
    d.check(not s["bigq"], "big question still on the page")
    d.check(not s["draft"], "Draft flag still on the page")
    d.check(not s["keynote"], "Key note still on the page")
    d.check(s["words"] in (3, 4), "%d key words" % s["words"])
    d.check("Good guess" not in s["text"] and "Fair guess" not in s["text"],
            "'Good guess' / 'Fair guess' on the page")
    low = s["text"].lower()
    d.check("learn it" not in low and "as on the equation sheet" not in low and "on the sheet" not in low,
            "'Learn it', 'As on the equation sheet' or an 'On the sheet' chip on the page")
    if ks == 3 or s["rungs"]:
        d.check(all(r in ("Rung 1", "Rung 2", "Rung 3", "Rung 4") for r in s["rungs"]) and len(s["rungs"]) == 4,
                "rung labels %s" % s["rungs"])
    if ks == 4:
        want = set()
        for it in rec["knowledge"] + rec["deeper"]:
            if it["kind"] != "card":
                continue
            r = it.get("routes")
            if not r or route in set(r):
                want.add(it["title"])
        got = set(s["titles"])
        d.check(got == want, "route cards on %s: extra %s, missing %s"
                % (route, sorted(got - want), sorted(want - got)))
        if slug == "energy-changes-in-systems":
            rp = [t for t in s["titles"] if t.startswith("Required practical")]
            num = "14" if route in ("CF", "CH") else "1"
            d.check(len(rp) == 1 and rp[0].startswith("Required practical %s:" % num),
                    "required practical card %s on %s" % (rp, route))
        if slug == "thermal-conductivity":
            pass
    else:
        d.check(len(s["titles"]) >= 1, "no cards")


def start_here(d, rec, ks, route):
    st = rec["start"]
    replies = {o[0]: o[1] for o in st["options"]}
    if ks == 3:
        n = d.js("return document.querySelectorAll('#s-hook .ks3-option').length")
        d.check(n == 2, "Start here has %d options" % n)
        for i in range(n):
            r = d.js("var o=document.querySelectorAll('#s-hook .ks3-option')[%d];o.click();"
                     "var lab=o.querySelector('.ks3-opt-label').textContent.trim();"
                     "var vis=[].filter.call(document.querySelectorAll('#s-hook .ks3-keyed-reply'),"
                     "function(p){return !p.hidden});"
                     "return {lab:lab,n:vis.length,text:vis[0]&&vis[0].textContent.trim(),"
                     "done:document.getElementById('s-hook').getAttribute('data-stage-done')}" % i)
            d.check(r["n"] == 1 and r["text"] == replies.get(r["lab"]),
                    "Start here option %r: reply %r, want %r" % (r["lab"], r["text"], replies.get(r["lab"])))
            d.check(r["done"] == "1", "Start here did not mark its rail stop")
    else:
        seen = []
        for visit in range(2):
            if visit == 1:
                if hasattr(d, "posted") or CAPTURING:
                    d.harvest()
                load(d.p, d.url)
            labs = d.js("return [].map.call(document.querySelectorAll('#s-hook button'),function(b){"
                        "return b.textContent.replace(/^(This|Or this|Your guess)/,'').trim()})")
            d.check(len(labs) == 2, "Start here has %d options" % len(labs))
            if len(labs) != 2:
                return
            want = next((l for l in labs if l not in seen), labs[0])
            idx = labs.index(want)
            d.js("document.querySelectorAll('#s-hook button')[%d].click();1" % idx)
            time.sleep(0.4)
            seen.append(want)
            txt = d.js("var s=document.querySelector('#s-hook [role=status]');return s?s.textContent.trim():null")
            lab = next((k for k in replies if want.endswith(k) or k in want), None)
            d.check(txt is not None and lab is not None and txt == replies[lab],
                    "Start here option %r: reply %r, want %r" % (want, txt, replies.get(lab)))
        d.check(len(set(seen)) == 2, "the two options were not both exercised: %s" % seen)


def open_close_cards(d):
    n = d.js("return document.querySelectorAll('.lean-card-btn').length")
    inside = d.js("return [].map.call(document.querySelectorAll('.lean-card-btn'),function(b){return !!b.closest('.lean-deeper')})")
    for i in range(n):
        if inside[i]:
            continue
        s0 = d.js(CARD_STATE % i)
        d.check(s0["exp"] == "false" and not s0["open"] and not s0["vis"], "card %d not closed at load: %s" % (i, s0))
        if i == 0:
            d.click_at(".lean-card-btn", 0)
        else:
            d.js("document.querySelectorAll('.lean-card-btn')[%d].click()" % i)
        time.sleep(0.1)
        s1 = d.js(CARD_STATE % i)
        d.check(s1["exp"] == "true" and s1["open"] and s1["vis"], "card %d did not open by tap: %s" % (i, s1))
        d.js("document.querySelectorAll('.lean-card-btn')[%d].click()" % i)
        s2 = d.js(CARD_STATE % i)
        d.check(s2["exp"] == "false" and not s2["open"] and not s2["vis"], "card %d did not close by tap: %s" % (i, s2))
        # keyboard: a real button gets Enter to open and Space to close
        d.js("document.querySelectorAll('.lean-card-btn')[%d].focus()" % i)
        d.key("Enter")
        s3 = d.js(CARD_STATE % i)
        d.check(s3["exp"] == "true" and s3["vis"], "card %d did not open by Enter: %s" % (i, s3))
        d.key(" ")
        s4 = d.js(CARD_STATE % i)
        d.check(s4["exp"] == "false" and not s4["vis"], "card %d did not close by Space: %s" % (i, s4))


SWIPE = """
var c=document.querySelectorAll('.lean-card')[%d];c.scrollIntoView({block:'center',behavior:'instant'});
var b=c.getBoundingClientRect();var y=b.top+Math.min(26,b.height/2);
function ev(t,x,yy){c.dispatchEvent(new PointerEvent(t,{bubbles:true,composed:true,cancelable:true,
 pointerId:7,pointerType:'touch',isPrimary:true,clientX:x,clientY:yy,button:0}));}
ev('pointerdown',300,y);ev('pointermove',220,y+3);ev('pointerup',140,y+4);
return c.hasAttribute('data-lean-open');
"""
SCROLLISH = """
var c=document.querySelectorAll('.lean-card')[%d];c.scrollIntoView({block:'center',behavior:'instant'});
var b=c.getBoundingClientRect();var y=b.top+20;
function ev(t,x,yy){c.dispatchEvent(new PointerEvent(t,{bubbles:true,composed:true,cancelable:true,
 pointerId:8,pointerType:'touch',isPrimary:true,clientX:x,clientY:yy,button:0}));}
ev('pointerdown',200,y);ev('pointerup',215,y+120);
return c.hasAttribute('data-lean-open');
"""


def swipe(d):
    d.js("var c=document.querySelectorAll('.lean-card')[0];if(c.hasAttribute('data-lean-open'))"
         "c.querySelector('.lean-card-btn').click();1")
    d.check(d.js(SWIPE % 0) is True, "a swipe did not open the first card")
    d.check(d.js(CARD_STATE % 0)["exp"] == "true", "swipe did not set aria-expanded")
    time.sleep(0.5)
    d.check(d.js(SWIPE % 0) is False, "a second swipe did not close the first card")
    time.sleep(0.5)
    d.check(d.js(SCROLLISH % 0) is False, "a vertical drag opened a card")
    time.sleep(0.5)


def reveals(d):
    n = d.js("return document.querySelectorAll('[data-lean-reveal]').length")
    for t in range(n):
        base = "document.querySelectorAll('[data-lean-reveal]')[%d]" % t
        cells = d.js("return %s.querySelectorAll('[data-lean-cell]').length" % base)
        vis0 = d.js("return [].filter.call(%s.querySelectorAll('.lean-cell-text'),function(x){return x.offsetHeight>0}).length" % base)
        d.check(vis0 == 0, "table %d shows %d answers before any tap" % (t, vis0))
        d.js("%s.scrollIntoView({block:'center',behavior:'instant'});1" % base)
        d.js("%s.querySelector('[data-lean-showall]').click();1" % base)
        v = d.js("return [].filter.call(%s.querySelectorAll('.lean-cell-text'),function(x){return x.offsetHeight>0}).length+'|'+%s.querySelector('[data-lean-showall]').getAttribute('aria-pressed')" % (base, base))
        d.check(v == "%d|true" % cells, "Show all on table %d: %s (want %d|true)" % (t, v, cells))
        d.js("%s.querySelector('[data-lean-showall]').click();1" % base)
        v = d.js("return [].filter.call(%s.querySelectorAll('.lean-cell-text'),function(x){return x.offsetHeight>0}).length" % base)
        d.check(v == 0, "Show all did not close table %d again (%s visible)" % (t, v))
        for c in range(cells):
            d.js("%s.querySelectorAll('[data-lean-cell]')[%d].click();1" % (base, c))
            r = d.js("var x=%s.querySelectorAll('[data-lean-cell]')[%d];"
                     "return {e:x.getAttribute('aria-expanded'),v:x.querySelector('.lean-cell-text').offsetHeight>0}" % (base, c))
            d.check(r["e"] == "true" and r["v"], "cell %d of table %d did not reveal: %s" % (c, t, r))
        if t == 0:
            d.click_at("[data-lean-cell]", 0) if False else None


def deeper(d):
    d.check(d.js("var b=document.querySelector('.lean-deeper-btn');return b.getAttribute('aria-expanded')") == "false",
            "Dive deeper not closed at load")
    d.check(d.js("return document.querySelector('.lean-deeper-body').offsetHeight") == 0, "Dive deeper body visible at load")
    d.js("document.querySelector('.lean-deeper-btn').click();1")
    d.check(d.js("return document.querySelector('.lean-deeper-body').offsetHeight>0"), "Dive deeper did not open")
    d.check(d.js("return document.querySelector('.lean-deeper-btn').getAttribute('aria-expanded')") == "true",
            "Dive deeper aria-expanded not true")
    n = d.js("return document.querySelectorAll('.lean-card-btn').length")
    inside = d.js("return [].map.call(document.querySelectorAll('.lean-card-btn'),function(b){return !!b.closest('.lean-deeper')})")
    for i in range(n):
        if inside[i]:
            d.js("document.querySelectorAll('.lean-card-btn')[%d].click();1" % i)
            s = d.js(CARD_STATE % i)
            d.check(s["exp"] == "true" and s["vis"], "Dive deeper card %d did not open: %s" % (i, s))


def open_everything(d):
    d.js("document.querySelectorAll('.lean-card-btn').forEach(function(b){var c=b.closest('.lean-card');"
         "if(!c.hasAttribute('data-lean-open'))b.click()});"
         "var dd=document.querySelector('.lean-deeper-btn');if(dd.getAttribute('aria-expanded')!=='true')dd.click();"
         "document.querySelectorAll('[data-lean-showall]').forEach(function(b){if(b.getAttribute('aria-pressed')!=='true')b.click()});"
         "document.querySelectorAll('[data-lean-word]').forEach(function(b){if(b.getAttribute('aria-expanded')!=='true')b.click()});1")
    time.sleep(0.3)


def overflow(d, label="everything open"):
    o = d.js(OVERFLOW)
    d.check(o["sw"] <= o["cw"] and o["bw"] <= o["cw"], "horizontal overflow with %s: %s" % (label, o))


# ── formula triangles ───────────────────────────────────────────────────

def triangle_cards(rec):
    """[(card title, [cells per triangle, ...], [equation dict or None, ...])] in page order."""
    out = []
    for it in rec["knowledge"] + rec["deeper"]:
        if it.get("kind") != "card":
            continue
        groups, eqs = [], []
        for p in it["body"]:
            slot = p.get("slot", "") if isinstance(p, dict) else ""
            if slot.startswith("triangle:"):
                eq = (rec.get("equations") or {})[slot.split(":", 1)[1]]
                groups.append(1 + len(eq["bottom"]))
                eqs.append(eq)
            elif slot in ("triangle-energy", "triangle-power"):
                groups.append(3)          # the legacy EQ_E / EQ_P: one top, two bottom
                eqs.append(None)
        if groups:
            out.append((it["title"], groups, eqs))
    return out


CELLS = "button[aria-label^='Find '], button[aria-label^='One half']"


def triangles(d, rec):
    """Tap every cell of every triangle: the line under it changes, with the half and root
    extra steps where the equation has them, and a triangle never says it is on the sheet."""
    for title, groups, eqs in triangle_cards(rec):
        i = d.js("var t=[].map.call(document.querySelectorAll('.lean-card-title'),function(x){return x.textContent.trim()});"
                 "return t.indexOf(%s)" % json.dumps(title))
        d.check(i >= 0, "card %r not found" % title)
        if i < 0:
            continue
        labels = d.js("var c=document.querySelectorAll('.lean-card')[%d];"
                      "return [].map.call(c.querySelectorAll(%s),function(b){return b.getAttribute('aria-label')})" % (i, json.dumps(CELLS)))
        d.check(len(labels) == sum(groups), "card %r has %d triangle cells, want %d" % (title, len(labels), sum(groups)))
        at = 0
        for g, eq in zip(groups, eqs):
            lo = at
            at += g
            d.check("written out" in d.js("var c=document.querySelectorAll('.lean-card')[%d];"
                                          "var b=c.querySelectorAll(%s)[%d];var e=b;"
                                          "while(e.parentElement&&e.parentElement.querySelectorAll(%s).length<=%d){e=e.parentElement}"
                                          "return e.innerText.toLowerCase()" % (i, json.dumps(CELLS), lo, json.dumps(CELLS), g)),
                    "triangle in %r does not start on 'Written out'" % title)
            for k in range(g):
                lab = labels[lo + k]
                scope = ("var c=document.querySelectorAll('.lean-card')[%d];var b=c.querySelectorAll(%s)[%d];"
                         "var e=b;while(e.parentElement&&e.parentElement.querySelectorAll(%s).length<=%d){e=e.parentElement}"
                         % (i, json.dumps(CELLS), lo + k, json.dumps(CELLS), g))
                if lab.startswith("One half"):
                    d.check(d.js(scope + "return b.disabled"), "the one-half cell in %r is tappable" % title)
                    continue
                d.js(scope + "b.click();1")
                time.sleep(0.12)
                txt = d.js(scope + "return e.innerText.toLowerCase()")
                is_top = (k == 0)
                want = ["side by side"] if is_top else ["one over the other"]
                if eq is not None and not is_top:
                    item = eq["bottom"][k - 1]
                    if any(x.get("half") for x in eq["bottom"] if x is not item):
                        want.append("is the same as")
                    if item.get("root"):
                        want.append("square-root both sides")
                for w in want:
                    d.check(w in txt, "triangle %r, cell %r: %r missing after the tap" % (title, lab, w))
                d.check("on the sheet" not in txt and "as on the equation sheet" not in txt,
                        "triangle %r still claims the equation sheet" % title)
        o = d.js(OVERFLOW)
        d.check(o["sw"] <= o["cw"], "overflow after tapping the triangles in %r: %s" % (title, o))


# ── figures: fitted to the card only where every label stays at 11px or more ────────

FIG_INFO = """
return [].map.call(document.querySelectorAll('[data-lean-fig]'), function (f, i) {
  var svg = f.querySelector('svg'), box = svg && svg.parentNode;
  var min = Infinity;
  if (svg) [].forEach.call(svg.querySelectorAll('text, tspan'), function (t) {
    if (t.tagName.toLowerCase() === 'text' && t.querySelector('tspan')) return;
    if (t.hasAttribute('baseline-shift') || !(t.textContent || '').trim() || !t.getClientRects().length) return;
    var m = t.getScreenCTM && t.getScreenCTM(); if (!m) return;
    var px = parseFloat(getComputedStyle(t).fontSize) * Math.hypot(m.a, m.b);
    if (px >= 0.05 && px < min) min = px;
  });
  return {i: i, vb: !!(svg && svg.getAttribute('viewBox')), avail: box ? box.clientWidth : 0,
          svgw: svg ? Math.round(svg.getBoundingClientRect().width) : 0,
          over: box ? box.scrollWidth - box.clientWidth : 0,
          fits: f.hasAttribute('data-lean-fits'), btn: !!f.querySelector('button'),
          minpx: min === Infinity ? null : Math.round(min * 100) / 100,
          ks4: !!f.closest('#ks4-mount'), card: !!f.closest('.lean-card')};
});
"""
FIGS = {}


def figures(d):
    info = d.js(FIG_INFO)
    FIGS[d.tag] = [(f["svgw"], f["avail"], f["fits"], f["minpx"]) for f in info]
    for f in info:
        w = "figure %d (svg %s, room %s, smallest text %spx)" % (f["i"], f["svgw"], f["avail"], f["minpx"])
        d.check(f["vb"], "%s has no viewBox" % w)
        d.check(f["card"], "%s is not inside a lean card" % w)
        d.check(not f["btn"], "%s carries a button" % w)
        if f["fits"]:
            d.check(f["over"] <= 1 and f["svgw"] <= f["avail"] + 1, "%s overflows its card when fitted: scroll over %s" % (w, f["over"]))
        if f["minpx"] is not None and (f["fits"] or f["ks4"]):
            d.check(f["minpx"] >= 10.99, "%s draws text under 11px" % w)


def touch_drag_slider(d):
    """A real touch drag along a slider inside a card moves the slider and leaves the card open."""
    n = d.js("return document.querySelectorAll('.lean-card input[type=range]').length")
    if not n:
        return
    d.p.send("Emulation.setTouchEmulationEnabled", {"enabled": True, "maxTouchPoints": 1})
    try:
        d.js("var i=document.querySelector('.lean-card input[type=range]');var c=i.closest('.lean-card');"
             "if(!c.hasAttribute('data-lean-open'))c.querySelector('.lean-card-btn').click();"
             "i.scrollIntoView({block:'center',behavior:'instant'});1")
        time.sleep(0.4)
        r = d.js("var i=document.querySelector('.lean-card input[type=range]');var b=i.getBoundingClientRect();"
                 "return {x:b.left,y:b.top+b.height/2,w:b.width,v:i.value}")
        y = r["y"]
        x0, x1 = r["x"] + r["w"] * 0.2, r["x"] + r["w"] * 0.85
        d.p.send("Input.dispatchTouchEvent", {"type": "touchStart", "touchPoints": [{"x": x0, "y": y}]})
        for k in range(1, 9):
            d.p.send("Input.dispatchTouchEvent", {"type": "touchMove", "touchPoints": [{"x": x0 + (x1 - x0) * k / 8, "y": y}]})
            time.sleep(0.03)
        d.p.send("Input.dispatchTouchEvent", {"type": "touchEnd", "touchPoints": []})
        time.sleep(0.4)
        after = d.js("var i=document.querySelector('.lean-card input[type=range]');"
                     "return {v:i.value,open:i.closest('.lean-card').hasAttribute('data-lean-open')}")
        d.check(after["v"] != r["v"], "a touch drag did not move the slider (%s -> %s)" % (r["v"], after["v"]))
        d.check(after["open"], "a touch drag along the slider closed its card")
    finally:
        d.p.send("Emulation.setTouchEmulationEnabled", {"enabled": False})


# ── what the page says, after the round-3 findings ──────────────────────

# AQA numbers a subject's sections from 4 in its own Triple spec, and from 4 (biology), 5 (chemistry)
# or 6 (physics) in Combined Science 8464; a lean page's eyebrow names only its own route's spec.
SPEC_TRIPLE = {"biology": "8461", "chemistry": "8462", "physics": "8463"}
SPEC_COMBINED_PART = {"biology": "4", "chemistry": "5", "physics": "6"}


def ks4_words(d, route, subject):
    h2 = d.js("return [].map.call(document.querySelectorAll('h2'),function(h){return h.textContent.trim()})")
    d.check("Practice" in h2 and "Exam ladder" not in h2, "practice heading: %s" % h2)
    d.check("Questions on this lesson" in h2 and not any(x.startswith("Five questions") for x in h2), "quiz heading: %s" % h2)
    txt = d.js("return document.body.innerText.toLowerCase()")
    d.check("you write it, then you mark it" not in txt, "the Rung 4 tag line is still there")
    m = d.js("var s=document.querySelectorAll('#s-ladder .ks3-rung-self');var t=s.length?s[s.length-1].innerText:'';"
             "return (t.match(/\\b\\d+ marks?\\b/gi)||[]).length")
    d.check(m <= 1, "Rung 4 shows its marks %d times (once is right)" % m)
    eb = d.js("return document.querySelector('.ks3-lesson-head .ks3-eyebrow').textContent.trim()")
    tri = route in ("TF", "TH")
    others = [c for c in SPEC_TRIPLE.values()] + ["8464"]
    want = ("(%s) 4." % SPEC_TRIPLE[subject]) if tri else ("(8464) %s." % SPEC_COMBINED_PART[subject])
    mine = SPEC_TRIPLE[subject] if tri else "8464"
    d.check(want in eb and not any(c in eb for c in others if c != mine),
            "spec eyebrow on %s reads %r" % (route, eb))


def tap_targets(d, ks):
    small = d.js("return [].slice.call(document.querySelectorAll('.ks3-endmatter li > a, .ks3-endmatter .ks3-tutor-cta'))"
                 ".filter(function(a){return a.getBoundingClientRect().height>0 && a.getBoundingClientRect().height<43.5})"
                 ".map(function(a){return a.textContent.trim().slice(0,30)+' '+Math.round(a.getBoundingClientRect().height)})")
    d.check(not small, "links under 44px tall: %s" % small)


KS3_BAD = r"(?i)(\bbench\b|\bhook\b|four requirements)"


def ks3_words(d):
    r = d.js("var m=document.querySelector('main').cloneNode(true);"
             "[].forEach.call(m.querySelectorAll('.ks3-legal,.lean-sr,svg'),function(x){x.remove()});"
             "var t=m.innerText;return {dash:(t.match(/ \u2014 /g)||[]).length,bad:(t.match(new RegExp(%s.slice(4),'gi'))||[])}" % json.dumps(KS3_BAD))
    d.check(r["dash"] == 0, "%d spaced em dash(es) left in the page text outside the legal text" % r["dash"])
    d.check(not r["bad"], "words that belong to removed content: %s" % r["bad"])


# ── practice ────────────────────────────────────────────────────────────

def ks3_practice(d, strict=True):
    """Every option of both marked rungs is clicked; the rung locks on the first, so the
    wrong option of rung 1 and the right option of rung 2 carry the feedback check."""
    info = d.js("return [].map.call(document.querySelectorAll('.ks3-rung[data-mode=marked]'),function(r){"
                "return [].map.call(r.querySelectorAll('.ks3-option'),function(o){"
                "return {c:o.getAttribute('data-correct'),f:o.getAttribute('data-feedback')}})})")
    d.check(len(info) == 2, "%d marked rungs" % len(info))
    for ri, opts in enumerate(info):
        for oi, o in enumerate(opts):
            if o["c"] == "0":
                d.check(bool(o["f"]), "rung %d option %d has no feedback" % (ri + 1, oi))
    for ri, want_correct in ((0, "0"), (1, "1")):
        r = d.js("var rung=document.querySelectorAll('.ks3-rung[data-mode=marked]')[%d];"
                 "var os=[].slice.call(rung.querySelectorAll('.ks3-option'));"
                 "var o=os.filter(function(x){return x.getAttribute('data-correct')==='%s'})[0];"
                 "var fb=o.getAttribute('data-feedback');o.click();"
                 "var t=rung.innerText;return {fb:fb,txt:t,res:rung.getAttribute('data-rung-resolved')}" % (ri, want_correct))
        time.sleep(0.2)
        d.check(r["res"] in ("0", "1"), "rung %d did not resolve after a click" % (ri + 1))
        if want_correct == "0" and r["fb"]:
            d.check(r["fb"][:30] in r["txt"], "rung %d wrong-option feedback not shown: %r" % (ri + 1, r["fb"][:40]))
    # clicking the remaining options must not error
    d.js("document.querySelectorAll('.ks3-rung[data-mode=marked] .ks3-option').forEach(function(o){o.click()});1")
    # the self-marked rungs
    for ri in (0, 1):
        d.js("var r=document.querySelectorAll('.ks3-rung-self')[%d];var t=r.querySelector('textarea');"
             "t.value='A written answer that is long enough to count as a real attempt at the question.';"
             "t.dispatchEvent(new Event('input',{bubbles:true}));1" % ri)
        time.sleep(0.15)
        d.js("var r=document.querySelectorAll('.ks3-rung-self')[%d];var b=r.querySelector('[data-check]');b.disabled=false;b.click();1" % ri)
        shown = d.js("return !document.querySelectorAll('.ks3-rung-self')[%d].querySelector('[data-ticks]').hidden" % ri)
        if strict:      # a child session marks a written answer on the server first, so only the plain walk asserts it
            d.check(shown, "self-marked rung %d did not show its success list" % (ri + 3))
        d.js("document.querySelectorAll('.ks3-rung-self')[%d].querySelectorAll('[data-crit]').forEach(function(c){c.click()});1" % ri)
    d.check(d.js("return document.querySelector('[data-score]').textContent.length>0"), "no ladder score line")
    if strict:
        ticks = d.js("return [].filter.call(document.querySelectorAll('.ks3-tick label'),function(l){return l.getBoundingClientRect().height>0})"
                     ".map(function(l){return Math.round(l.getBoundingClientRect().height)})")
        d.check(ticks and min(ticks) >= 44, "tick rows are under 44px tall: %s" % sorted(set(ticks))[:4])


def ks4_click_buttons(d, section_js, skip=("Check", "Tap a link", "Show", "Next", "Retry")):
    """Click every enabled option-like button in a section, one at a time (a locked item
    disables its siblings). Returns how many were clicked."""
    clicked = 0
    for _ in range(80):
        r = d.js("var sec=%s;if(!sec)return null;var bs=[].slice.call(sec.querySelectorAll('button'));"
                 "var skip=%s;var b=bs.filter(function(x){var t=x.textContent.trim();"
                 "return !x.disabled&&t&&!skip.some(function(s){return t.indexOf(s)===0})&&!x.dataset.leanDone&&x.offsetParent!==null})[0];"
                 "if(!b)return 0;b.dataset.leanDone='1';b.scrollIntoView({block:'center',behavior:'instant'});b.click();return 1"
                 % (section_js, json.dumps(list(skip))))
        if not r:
            break
        clicked += 1
        time.sleep(0.05)
    return clicked


def ks4_practice(d):
    n = ks4_click_buttons(d, "document.getElementById('s-ladder')")
    d.check(n >= 4, "only %d practice buttons clicked" % n)
    # the quiz bank is the section after the ladder; its size is the lesson's data
    q = "document.getElementById('s-ladder').nextElementSibling"
    size = d.js("var s=%s;return [].filter.call(s.querySelectorAll('button'),function(b){return /^A/.test(b.textContent.trim())}).length" % q)
    n2 = ks4_click_buttons(d, q)
    QUIZ_SIZES[d.tag] = size
    d.check(size >= 1 and n2 >= size, "quiz bank: %d question(s), %d option(s) clicked" % (size, n2))
    d.js("document.querySelectorAll('[data-lean-done]').forEach(function(x){delete x.dataset.leanDone});1")


def survival(d, ks, answer):
    """A card opened before a rail scroll update, and before an answer, is still open after."""
    d.js("window.scrollTo(0,0);1")
    time.sleep(0.2)
    d.js("document.querySelectorAll('.lean-card-btn')[0].click();1")
    d.check(d.js(CARD_STATE % 0)["open"], "could not open the card to test survival")
    for y in (300, 900, 1800, 400, 0):
        d.js("window.scrollTo({top:%d,behavior:'instant'});window.dispatchEvent(new Event('scroll'));1" % y)
        time.sleep(0.35)
    s = d.js(CARD_STATE % 0)
    d.check(s["open"] and s["exp"] == "true" and s["vis"], "card closed after a rail scroll update: %s" % s)
    pressed = d.js("var b=document.querySelector('[data-lean-showall]');if(!b)return null;"
                   "if(b.getAttribute('aria-pressed')!=='true')b.click();return b.getAttribute('aria-pressed')")
    if pressed is not None:
        for y in (500, 0):
            d.js("window.scrollTo({top:%d,behavior:'instant'});window.dispatchEvent(new Event('scroll'));1" % y)
            time.sleep(0.35)
        d.check(d.js("return document.querySelector('[data-lean-showall]').getAttribute('aria-pressed')") == "true",
                "Show all lost its pressed state after a rail scroll update")
    answer()
    time.sleep(0.4)
    s = d.js(CARD_STATE % 0)
    d.check(s["open"] and s["exp"] == "true" and s["vis"], "card closed after answering a question: %s" % s)
    if ks == 3:
        done = d.js("return [].map.call(document.querySelectorAll('.ks3-rail li'),function(l){return l.classList.contains('is-done')})")
        d.check(len(done) == 3 and done[1], "KS3 rail: Key knowledge stop not ticked after a card opened: %s" % done)
    else:
        txt = d.js("return [].map.call(document.querySelectorAll('[data-rail=\"side\"] a'),function(a){"
                   "var c=a.firstElementChild;return c?c.textContent.trim():''})")
        d.check(len(txt) == 3 and txt[1] == "", "KS4 rail: Key knowledge stop not ticked after a card opened: %s" % txt)


# ── the walk ────────────────────────────────────────────────────────────

_THEME_SCRIPT = {}


def theme(page, scheme):
    """Force light or dark for the NEXT navigations. `b.page()` hands back the same tab each
    time, so the previous scheme's start-up script is removed first."""
    old = _THEME_SCRIPT.pop("id", None)
    if old:
        page.send("Page.removeScriptToEvaluateOnNewDocument", {"identifier": old})
    page.send("Emulation.setEmulatedMedia", {"features": [{"name": "prefers-color-scheme", "value": scheme}]})
    r = page.send("Page.addScriptToEvaluateOnNewDocument",
                  {"source": "try{localStorage.setItem('mrb-theme','%s')}catch(e){}" % scheme})
    _THEME_SCRIPT["id"] = r.get("identifier")


def pages():
    import ks3_data
    import ks3_data.lean as k3
    import ks4_lessons
    reg = ks3_data.lesson_registry()
    for slug in sorted(k3.records()):
        l = reg[slug]
        disc = ks3_data.structure.unit_index()[l["_unit"]]["discipline"]
        yield (3, slug, None, "/ks3/%s/%s/%s.html" % (disc, l["_unit_slug"], slug), k3.records()[slug])
    for L in ks4_lessons.lean_lessons():
        # a lesson exists only on its own routes (Fleming's rule: CH and TH; transformers: TH)
        for r in [r for r in ROUTES if r in (L.get("routes") or ROUTES)]:
            yield (4, L["slug"], r, "/%s/%s/%s/%s.html" % (ROUTE_DIR[r], L["subject"], L["topic_id"], L["slug"]), L["lean"])


def setup(b, scheme):
    page = b.page("about:blank")
    page.send("Network.enable")
    page.send("Network.setBlockedURLs", {"urls": BLOCK})
    page.set_viewport(W, H)
    return page


def walk_light(page, base, ks, slug, route, path, rec, shots):
    tag = "ks%d %s%s" % (ks, slug, (" " + route) if route else "")
    theme(page, "light")
    d = Drive(page, tag)
    d.url = base + path
    load(page, d.url)
    page.console_errors()
    d.check(d.js("return document.documentElement.getAttribute('data-theme')") == "light", "page is not in light theme")
    structure(d, rec, ks, route, slug)
    start_here(d, rec, ks, route)
    open_close_cards(d)
    swipe(d)
    reveals(d)
    deeper(d)
    open_everything(d)
    overflow(d)
    if ks == 4:
        triangles(d, rec)
        ks4_words(d, route, path.split("/")[2])
    else:
        ks3_words(d)
    figures(d)
    tap_targets(d, ks)
    touch_drag_slider(d)
    if shots and slug in SHOT_PAGES and route in (None, "CH"):
        page.screenshot(os.path.join(shots, "%s-light-open.png" % tag.replace(" ", "-")), width=W, height=H)
    answer = (lambda: ks3_practice(d)) if ks == 3 else (lambda: ks4_practice(d))
    d.js("document.querySelectorAll('.lean-card-btn').forEach(function(b){var c=b.closest('.lean-card');if(c.hasAttribute('data-lean-open'))b.click()});1")
    survival(d, ks, answer)
    overflow(d, "answers shown")
    errs = [e for e in page.console_errors() if "ERR_BLOCKED_BY_CLIENT" not in e and config_env.PROD_BACKEND_HOST not in e]
    d.check(not errs, "console errors: %s" % errs[:3])
    return d.checks


def walk_dark(page, base, ks, slug, route, path, rec, shots):
    tag = "ks%d %s%s dark" % (ks, slug, (" " + route) if route else "")
    theme(page, "dark")
    d = Drive(page, tag)
    load(page, base + path)
    page.console_errors()
    t = d.js("return document.documentElement.getAttribute('data-theme')")
    d.check(t == "dark", "html[data-theme] is %r in dark" % t)
    bg = d.js("var c=document.querySelector('.lean-card');return [getComputedStyle(c).backgroundColor,"
              "getComputedStyle(c).color,getComputedStyle(document.body).backgroundColor]")
    d.check(bg[0] != bg[1], "card text and ground are the same colour in dark: %s" % bg)
    if shots and slug in SHOT_PAGES and route in (None, "CH"):
        page.screenshot(os.path.join(shots, "%s-dark-closed.png" % tag.replace(" ", "-").replace("-dark", "")), width=W, height=H)
    open_everything(d)
    overflow(d)
    if shots and slug in SHOT_PAGES and route in (None, "CH"):
        page.screenshot(os.path.join(shots, "%s-dark-open.png" % tag.replace(" ", "-").replace("-dark", "")), width=W, height=H)
    errs = [e for e in page.console_errors() if "ERR_BLOCKED_BY_CLIENT" not in e and config_env.PROD_BACKEND_HOST not in e]
    d.check(not errs, "console errors in dark: %s" % errs[:3])
    return d.checks


# ── the ids a page really posts ─────────────────────────────────────────

CAPTURE_JS = r"""
(function () {
  try { localStorage.setItem(%(key)s, JSON.stringify({access_token: 'drive', refresh_token: 'drive',
        expires_at: 4102444800, user: {id: 'drive-child', email: 'drive@children.mrbadmus.internal'}})); } catch (e) {}
  window.__posted = window.__posted || [];
  var real = window.fetch;
  window.fetch = function (u, o) {
    try {
      if (String(u).indexOf('/api/consumer/child/answer') >= 0 && o && o.body) {
        window.__posted.push(JSON.parse(o.body));           // recorded, never sent
        return Promise.resolve({ ok: true, status: 204, json: function () { return Promise.resolve({}); } });
      }
    } catch (e) {}
    return real.apply(this, arguments);
  };
})();
"""


def id_map():
    out = {}
    for f in glob.glob(os.path.join(ROOT, "docs", "lessons", "*", "ID-MAP-*.json")):
        with open(f, encoding="utf-8") as fh:
            for qid, e in json.load(fh)["ids"].items():
                out[qid] = e["status"]
    return out


def walk_ids(page, base, ks, slug, route, path, rec, idmap):
    """A child session whose answer sends are recorded, not sent: every question_id the page
    posts when it is answered must be in the ID map as kept or added."""
    global CAPTURING
    tag = "ks%d %s%s ids" % (ks, slug, (" " + route) if route else "")
    CAPTURING = True
    theme(page, "light")
    key = "sb-%s-auth-token" % config_env.TEST_REF
    r = page.send("Page.addScriptToEvaluateOnNewDocument", {"source": CAPTURE_JS % {"key": json.dumps(key)}})
    try:
        d = Drive(page, tag)
        d.posted = []
        d.url = base + path
        load(page, d.url)
        page.console_errors()
        start_here(d, rec, ks, route)
        (lambda x: ks3_practice(x, strict=False) if ks == 3 else ks4_practice(x))(d)
        d.harvest()
    finally:
        page.send("Page.removeScriptToEvaluateOnNewDocument", {"identifier": r.get("identifier")})
        CAPTURING = False
    ids = [b.get("question_id") for b in d.posted]
    named = [i for i in ids if i]
    d.check(len(named) >= 3, "only %d answer(s) with an id were posted" % len(named))
    for i in sorted(set(named)):
        st = idmap.get(i)
        d.check(st in ("kept", "added"), "posted question_id %r is %s in the ID map (need kept or added)"
                % (i, "listed " + st if st else "NOT in it"))
    d.check(all(b.get("lesson_slug") == slug for b in d.posted), "a post names the wrong lesson")
    POSTED[tag] = {"ids": sorted(set(named)), "no_id": len(ids) - len(named)}
    return d.checks


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--only", default="")
    ap.add_argument("--no-dark", action="store_true")
    ap.add_argument("--no-ids", action="store_true", help="skip the posted-question-id pass")
    a = ap.parse_args()
    shots = os.environ.get("MRB_SHOTS") or cdp.gate_tmp()
    os.makedirs(shots, exist_ok=True)
    server, port = cdp.serve(os.path.join(ROOT, "mrbadmus_site"))
    base = "http://127.0.0.1:%d" % port
    total = n = 0
    idmap = id_map()
    try:
        todo = [p for p in pages() if a.only in p[1] and True]
        with cdp.Browser() as b:
            light = setup(b, "light")
            dark = None if a.no_dark else setup(b, "dark")
            for (ks, slug, route, path, rec) in todo:
                before = len(FAILS)
                c = walk_light(light, base, ks, slug, route, path, rec, shots)
                if not a.no_dark:
                    c += walk_dark(dark, base, ks, slug, route, path, rec, shots)
                if not a.no_ids:
                    c += walk_ids(light, base, ks, slug, route, path, rec, idmap)
                total += c
                n += 1
                print("  %s  %s%s: %d checks" % ("ok  " if len(FAILS) == before else "FAIL", slug,
                                                (" " + route) if route else "", c), flush=True)
    finally:
        server.shutdown()
    print("\nposted question ids per page: %s" % json.dumps({k: len(v["ids"]) for k, v in sorted(POSTED.items())}))
    allp = sorted({i for v in POSTED.values() for i in v["ids"]})
    print("distinct posted ids: %d (kept or added in the map: %d)" % (len(allp), sum(1 for i in allp if idmap.get(i) in ("kept", "added"))))
    print("\nfigures (natural width / room) per page: %s" % json.dumps({k: v for k, v in sorted(FIGS.items()) if v}))
    print("\nquiz bank size per page: %s" % json.dumps(QUIZ_SIZES, sort_keys=True))
    print("\n%d page(s), %d checks, %d failure(s). Screenshots: %s" % (n, total, len(FAILS), shots))
    for f in FAILS:
        print("  - " + f)
    return 1 if FAILS else 0


if __name__ == "__main__":
    sys.exit(main())
