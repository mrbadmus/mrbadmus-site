#!/usr/bin/env python3
"""theme_placement_drive.py — the Light/Dark/System control sits IN the
header, never on a row of its own.

Owner's defect (16 Oct 2026): "The Light/Dark/System switch sits on its own
row above the header on phones, wasting space. Put it inside the header (or
the menu) on every page family at 390, keeping it one tap away. Desktop
placement unchanged unless it also takes its own row."

For one representative page of EVERY family, at 390x844 and 1280x900, this
drive finds the visible theme control (theme.js's inline group, or its
compact one-button menu) and asserts:

  1. it lies inside the vertical band of the page's header/top bar (the
     first visible <header>/<nav>/topbar at the top of the page, or a named
     selector where the page's top bar is something else — a desktop
     sidebar's brand row);
  2. no OTHER visible theme control sits outside that band (the old fixed
     pill / in-flow row above the header is exactly this);
  3. at 390 the header is ONE row: height <= 72px;
  4. the control's tap target is >= 44x44 at 390.

Where a page keeps the control in its menu (the teacher bar's menu, the
parents marketing menu), the MENU BUTTON must be in the header band and
opening it must show a theme control (one tap to reach it).

How sign-in-only pages are measured (no backend, no Supabase):
  * consumer / org / go / parents pages: `consumer_dash_fixture.prescript()`
    — the same offline stub consumer_dash_drive uses (a stubbed session and
    canned /api/consumer/* answers), with the right `who` per page.
  * every other page: a pre-script that cancels any script-initiated
    navigation away from the page via the Navigation API (`navigate` event,
    preventDefault), so a signed-out redirect to auth.html cannot take the
    page away before its static header is measured.
  * teacher/today, import, seating: today_drive's offline teacher stub (a
    supabase client signed in as a teacher, the data layer's packs stubbed),
    so requireTeacherRole reveals the page as it does for a real teacher.
  * the generated teacher screens: build_teacher_port's own fixture page
    (teacher_fixtures/class-detail-fixture.html), which carries Design's
    values and needs no session. That tree is not copied into
    mrbadmus_site/, so it is served from the repo root.

Everything else is served from the BUILT mrbadmus_site/ — run
`python3 build_all.py` first. Screenshots go to gate_tmp()/theme_placement
(never into the repo tree).

    python3 theme_placement_drive.py [--only SUBSTR] [--shots DIR]
"""
from __future__ import annotations

import argparse
import json
import os
import sys
import time

REPO = os.path.dirname(os.path.abspath(__file__))
SITE = os.path.join(REPO, "mrbadmus_site")
sys.path.insert(0, REPO)

import ks3_browser as cdp  # noqa: E402
import consumer_dash_fixture as fx  # noqa: E402
import today_drive as td  # noqa: E402  (its offline teacher stubs)

WIDTHS = ((390, 844), (1280, 900))
MAX_HEAD_390 = 72

# Cancel any navigation the page's own script starts (a signed-out redirect).
BLOCK_NAV = r"""
(function(){
  window.__mrbBlocked = [];
  if (!window.navigation) return;
  window.navigation.addEventListener('navigate', function (e) {
    try {
      var u = new URL(e.destination.url);
      if (u.pathname !== location.pathname && e.cancelable) {
        e.preventDefault(); window.__mrbBlocked.push(u.pathname);
      }
    } catch (_) {}
  });
})();
"""

# name, path, server, fixture kwargs (None = BLOCK_NAV only), options
#   head: {width: selector} for the header band when it is not auto-found
#         (a desktop sidebar's brand row)
#   max_head: the 390 one-row cap, where a page's single row is drawn taller
PAGES = [
    ("ks4-classic", "combined/higher/physics/atomic-structure/development-atomic-model.html", "site", None, {}),
    ("ks4-pilot", "combined/foundation/biology/cell-biology/chromosomes-mitosis.html", "site", None, {}),
    ("ks3-lesson", "ks3/biology/cells-and-organisation/animal-and-plant-cells.html", "site", None, {}),
    ("student-class", "student/class-fixture.html", "site", None, {}),
    ("teacher-generated", "teacher_fixtures/class-detail-fixture.html", "repo", None, {}),
    ("teacher-today", "teacher/today.html", "site", "teacher", {}),
    ("teacher-import", "teacher/import.html", "site", "teacher", {}),
    ("teacher-seating", "teacher/seating.html", "site", "teacher", {}),
    ("consumer-today", "consumer/today.html", "site", dict(who="child"), {}),
    ("consumer-exam", "consumer/exam.html", "site", dict(who="child"), {}),
    ("consumer-unit-check", "consumer/unit-check.html?unit=B5", "site", dict(who="child"), {}),
    ("consumer-signup", "consumer/signup.html", "site", dict(signed_in=False, state="none", kids=0),
     {"head": {1280: ".su-rail-top"}}),
    ("consumer-account", "consumer/account.html", "site", dict(state="trialing", kids=2), {}),
    ("consumer-overview", "consumer/overview.html", "site", dict(state="trialing", kids=2),
     {"head": {1280: ".dk-side-top"}}),
    # The report is a printable sheet with no page header; its top bar is
    # the sheet's own brand row, where the control now ends.
    ("consumer-report", "consumer/report.html?child=kid-ada", "site", dict(state="trialing", kids=2),
     {"head": {390: ".rpt-brandrow", 1280: ".rpt-brandrow"}}),
    ("consumer-verify", "consumer/verify.html", "site", dict(signed_in=False), {}),
    ("consumer-checkout-return", "consumer/checkout-return.html", "site", dict(state="trialing", kids=2),
     {"head": {1280: ".su-rail-top"}}),
    # Design's marketing header: one row (brand, Start free, menu) drawn at
    # 82px by its own padding — the cap measures rows, not her spacing.
    ("parents-index", "parents/index.html", "site", dict(signed_in=False), {"max_head": 84}),
    ("parents-sign-in", "parents/sign-in.html", "site", dict(signed_in=False), {}),
    ("go", "go/index.html", "site", dict(signed_in=False), {}),
    ("org-index", "org/index.html", "site", dict(who="org"), {"head": {1280: ".og-side-brand"}}),
    ("org-sign-in", "org/sign-in.html", "site", dict(signed_in=False, who="org"), {}),
    ("auth", "auth.html", "site", None, {}),
    ("index", "index.html", "site", None, {}),
    ("leaderboard", "leaderboard.html", "site", None, {}),
    ("simulation", "simulations/physics/circuit-lab/index.html", "site", None, {}),
]

MENU_BUTTONS = ".tb-menu, .pb-menu-btn, .nav-burger"

MEASURE = r"""
(function (headSel, menuSel) {
  function vis(e) {
    if (!e) return false;
    var r = e.getBoundingClientRect();
    if (r.width < 2 || r.height < 2) return false;
    for (var n = e; n && n.nodeType === 1; n = n.parentElement) {
      var s = getComputedStyle(n);
      if (s.display === 'none' || s.visibility === 'hidden' || +s.opacity === 0) return false;
      if (n.tagName === 'DETAILS' && !n.open && n !== e && !e.closest('summary')) return false;
    }
    return true;
  }
  function box(e) { var r = e.getBoundingClientRect();
    return {top: Math.round(r.top), bottom: Math.round(r.bottom), left: Math.round(r.left),
            right: Math.round(r.right), w: Math.round(r.width), h: Math.round(r.height)}; }
  window.scrollTo(0, 0);
  var head = null;
  if (headSel) {
    var cands = document.querySelectorAll(headSel);
    for (var i = 0; i < cands.length; i++) if (vis(cands[i])) { head = cands[i]; break; }
  } else {
    var all = document.querySelectorAll('[data-port-region="topbar"], header, nav, [role="banner"]');
    for (var j = 0; j < all.length; j++) {
      var c = all[j]; if (!vis(c)) continue;
      var r = c.getBoundingClientRect();
      if (r.top > 130 || r.width < innerWidth * 0.5) continue;
      if (c.closest('.mrb-theme-pop, .tb-menu-box, .pb-menu, #nav-drawer')) continue;
      head = c; break;
    }
  }
  // Visible theme controls: a compact menu's button, or an inline group
  // (not one inside a popover / menu panel).
  var ctrls = [];
  document.querySelectorAll('.mrb-theme-menu > summary').forEach(function (s) { if (vis(s)) ctrls.push(s); });
  document.querySelectorAll('fieldset.mrb-theme').forEach(function (f) {
    if (f.closest('.mrb-theme-pop')) return;
    if (vis(f)) ctrls.push(f);
  });
  var out = {head: head ? box(head) : null,
             headTag: head ? (head.tagName.toLowerCase() + (head.id ? '#' + head.id : '') +
                              (head.className && typeof head.className === 'string' ? '.' + head.className.trim().split(/\s+/).join('.') : '')) : null,
             ctrls: ctrls.map(function (e) {
               var b = box(e);
               var tgt = e.tagName === 'SUMMARY' ? e : e.querySelector('label');
               b.tap = tgt ? box(tgt) : null;
               b.kind = e.tagName === 'SUMMARY' ? 'compact' : 'group';
               b.inHead = head ? head.contains(e) : false;
               return b; }),
             menu: null, blocked: window.__mrbBlocked || [],
             vw: innerWidth, slots: document.querySelectorAll('[data-mrb-theme]').length};
  var mb = null;
  if (head) {
    var ms = head.querySelectorAll(menuSel);
    for (var k = 0; k < ms.length; k++) if (vis(ms[k])) { mb = ms[k]; break; }
  }
  if (mb) { out.menu = box(mb); out.menu.tap = box(mb); }
  return out;
})(%s, %s)
"""

OPEN_MENU = r"""
(function (menuSel, headSel) {
  var b = document.querySelector(menuSel);
  var bs = document.querySelectorAll(menuSel);
  for (var i = 0; i < bs.length; i++) { var r = bs[i].getBoundingClientRect(); if (r.width > 2) { b = bs[i]; break; } }
  if (!b) return false;
  b.click();
  return true;
})(%s)
"""

AFTER_MENU = r"""
(function () {
  function vis(e) { var r = e.getBoundingClientRect(); if (r.width < 2 || r.height < 2) return false;
    for (var n = e; n && n.nodeType === 1; n = n.parentElement) { var s = getComputedStyle(n);
      if (s.display === 'none' || s.visibility === 'hidden') return false; } return true; }
  var n = 0;
  document.querySelectorAll('fieldset.mrb-theme, .mrb-theme-menu > summary').forEach(function (e) { if (vis(e)) n++; });
  return n;
})()
"""

FAILS: list[str] = []
LINES: list[str] = []


def check(ok, label, evidence=""):
    line = ("  OK  " if ok else "  XX  ") + label + (("  — " + str(evidence)[:260]) if evidence else "")
    print(line)
    if not ok:
        FAILS.append(label)
    return ok


def teacher_prescript():
    """today_drive's offline teacher: a stubbed supabase client signed in as
    a teacher with three classes, and the data layer's packs stubbed."""
    pre = "window.__MRB_STUB__=%s;\n" % json.dumps({"uid": td.TEACHER, "tables": td.TABLES, "log": []})
    pre += td.STUB_JS + (td.PACKS % json.dumps({}))
    pre += td.CLASSES_JS % json.dumps(td.TABLES.get("classes", []))
    return pre + td.PACK_JS


def measure(p, name, path, base, fixture, opts, shots):
    for (w, h) in WIDTHS:
        tag = "%s@%d" % (name, w)
        if fixture == "teacher":
            pre = BLOCK_NAV + teacher_prescript()
        else:
            pre = BLOCK_NAV + (fx.prescript(**fixture) if fixture is not None else "")
        ident = p.send("Page.addScriptToEvaluateOnNewDocument", {"source": pre}).get("identifier")
        try:
            p.set_viewport(w, h)
            url = base + "/" + path
            p.goto(url, settle=0.3)
            p.eval("try{localStorage.setItem('mrb-theme','light')}catch(e){}")
            p.goto(url, settle=1.6)
            p.set_viewport(w, h)
            time.sleep(0.3)
            head_sel = (opts.get("head") or {}).get(w)
            m = p.eval(MEASURE % (json.dumps(head_sel), json.dumps(MENU_BUTTONS)))
            shot = os.path.join(shots, "%s-%d.png" % (name, w))
            try:
                p.screenshot(shot, width=w, height=h, full_page=False)
            except Exception as e:  # a screenshot failure is not a placement finding
                print("     (screenshot failed: %s)" % e)
            head = m.get("head")
            if not check(head is not None, tag + ": a header/top bar is found",
                         "selector %s" % head_sel if head_sel else "auto"):
                continue
            ev = "%s %s..%s" % (m.get("headTag"), head["top"], head["bottom"])
            band_ok = lambda b: b["top"] >= head["top"] - 8 and b["bottom"] <= head["bottom"] + 8
            ctrls = m.get("ctrls") or []
            if ctrls:
                inside = [c for c in ctrls if band_ok(c)]
                outside = [c for c in ctrls if not band_ok(c)]
                check(len(inside) >= 1, tag + ": theme control inside the header band",
                      ev + " ctrls " + json.dumps([(c["kind"], c["top"], c["bottom"]) for c in ctrls]))
                check(not outside, tag + ": no theme control on a row of its own",
                      json.dumps([(c["kind"], c["top"], c["bottom"]) for c in outside]) if outside else "")
                clipped = [c for c in ctrls if c["left"] < 0 or c["right"] > m["vw"] + 1]
                check(not clipped, tag + ": theme control fully on screen (not cut off at the edge)",
                      json.dumps([(c["kind"], c["left"], c["right"]) for c in clipped]) if clipped else "")
                if w == 390 and inside:
                    t = inside[0].get("tap") or inside[0]
                    check(t["w"] >= 44 and t["h"] >= 44, tag + ": tap target >= 44x44",
                          "%dx%d" % (t["w"], t["h"]))
            else:
                menu = m.get("menu")
                if check(menu is not None and band_ok(menu),
                         tag + ": no visible theme control, so its menu button is in the header band",
                         ev + " menu " + json.dumps(menu)):
                    p.eval(OPEN_MENU % json.dumps(MENU_BUTTONS))
                    time.sleep(0.4)
                    n = p.eval(AFTER_MENU)
                    check(n >= 1, tag + ": opening the menu shows the theme control (one tap)", "%s visible" % n)
                    if w == 390:
                        check(menu["w"] >= 40 and menu["h"] >= 40, tag + ": menu tap target", "%dx%d" % (menu["w"], menu["h"]))
            if w == 390:
                cap = opts.get("max_head", MAX_HEAD_390)
                check(head["h"] <= cap, tag + ": header is one row (<= %dpx)" % cap,
                      "%dpx" % head["h"])
            LINES.append("%-26s %4d  head %-40s h=%-3d ctrls=%s" % (
                name, w, (m.get("headTag") or "")[:40], head["h"],
                ",".join("%s@%d-%d" % (c["kind"], c["top"], c["bottom"]) for c in ctrls) or
                ("menu@%d-%d" % (m["menu"]["top"], m["menu"]["bottom"]) if m.get("menu") else "none")))
        except Exception as e:
            check(False, tag + ": page measured", repr(e))
        finally:
            p.send("Page.removeScriptToEvaluateOnNewDocument", {"identifier": ident})


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--only", default=None, help="run only pages whose name contains this")
    ap.add_argument("--shots", default=None)
    args = ap.parse_args()
    shots = args.shots or os.path.join(cdp.gate_tmp(), "theme_placement")
    os.makedirs(shots, exist_ok=True)
    if not os.path.isdir(SITE):
        print("theme_placement_drive: no mrbadmus_site/ — run python3 build_all.py first")
        return 1
    site, sport = cdp.serve(SITE)
    repo, rport = cdp.serve(REPO)
    bases = {"site": "http://127.0.0.1:%d" % sport, "repo": "http://127.0.0.1:%d" % rport}
    try:
        with cdp.Browser() as b:
            p = b.attach()
            for name, path, srv, fixture, opts in PAGES:
                if args.only and args.only not in name:
                    continue
                print("── " + name + "  /" + path)
                measure(p, name, path, bases[srv], fixture, opts, shots)
    finally:
        site.shutdown()
        repo.shutdown()
    print("\nsummary")
    for line in LINES:
        print("  " + line)
    print("\nshots: " + shots)
    print("%s — %d failure(s)" % ("PASS" if not FAILS else "FAIL", len(FAILS)))
    for f in FAILS:
        print("   ✗ " + f)
    return 1 if FAILS else 0


if __name__ == "__main__":
    raise SystemExit(main())
