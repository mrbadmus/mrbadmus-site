#!/usr/bin/env python3
"""KS4 figure-text audit: no <svg> text on a KS4 lesson page may draw smaller than 11 CSS px at 390 px wide.

Loose-ends run, 17 Oct 2026 (fix 7a). Design's figures are `<svg viewBox style="width:100%">` with text sized in
viewBox units, so the size a pupil sees is  font-size x rendered-width / viewBox-width.  The generic fix lives in
shared/ks4-runtime.js figFit() + build_ks4.KS4_FIG_CSS (a phone-only min-width so the smallest label reaches 11px,
in a sideways-scrolling frame). This tool is the proof, and the gate (gate_registry: ks4_figure_text) that keeps it.

How a size is measured: for every <text>/<tspan> that actually draws (has a client rect, non-empty string) the
effective px is  computed font-size x hypot(ctm.a, ctm.b)  where ctm = element.getScreenCTM(). That folds in the
viewBox scale, any CSS width, and any transform; getBoundingClientRect().height is NOT used (it depends on the glyphs).

How figures are reached: a lesson page is loaded at 390x844 / DPR 1, scrolled top to bottom (lazy sections), then
every enabled <button> inside #ks4-mount is clicked ONE at a time (hook picks, tabs, steps, level toggles), and the
figures are re-measured after each click; a figure is identified by its markup, so one drawn twice counts once.
One route per lesson by default (the lesson's Triple Higher page, else its first route); --all-routes walks all four,
which matters only where a figure differs by route. Read-only: nothing is written under the repo, results go to
$MRB_SHOTS / gate_tmp().

  python3 tools/ks4_figure_text_audit.py                       # audit every built lesson, print the table
  python3 tools/ks4_figure_text_audit.py --check               # same, exit 1 if any text < 11px (the gate)
  python3 tools/ks4_figure_text_audit.py --only menstrual-cycle,human-reproduction-hormones --all-routes
  python3 tools/ks4_figure_text_audit.py --batch batch-8 --out /tmp/audit
Needs a built site (mrbadmus_site/) and headless Chrome; it does not build anything.
"""
import argparse
import json
import os
import sys
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)

import ks3_browser  # noqa: E402
import ks4_lessons  # noqa: E402

FLOOR = 11.0
WIDTH, HEIGHT = 390, 844
SITE = os.path.join(ROOT, "mrbadmus_site")
MAX_CLICKS = 60

MEASURE_JS = r"""
(function () {
  var out = [];
  var svgs = document.querySelectorAll('#ks4-mount svg, main svg, svg');
  var seen = new Set();
  Array.prototype.forEach.call(svgs, function (svg) {
    if (seen.has(svg)) { return; } seen.add(svg);
    var vb = svg.viewBox && svg.viewBox.baseVal;
    if (!vb || vb.width < 100) { return; }            // icons / chevrons: no figure text
    var texts = svg.querySelectorAll('text');
    if (!texts.length) { return; }
    var rect = svg.getBoundingClientRect();
    var col = svg.parentElement ? svg.parentElement.clientWidth : 0;
    var rec = { key: (svg.getAttribute('aria-label') || '') + '|' + vb.width + 'x' + vb.height + '|' + svg.innerHTML.length + '|' + svg.innerHTML.slice(0, 160) + svg.innerHTML.slice(-160),
                alt: svg.getAttribute('aria-label') || '', vb: [vb.width, vb.height], width: Math.round(rect.width),
                scrollW: Math.round(rect.width), colW: col,
                drawn: rect.width > 0 && rect.height > 0, nodes: [] };
    Array.prototype.forEach.call(svg.querySelectorAll('text, tspan'), function (t) {
      var s = (t.tagName.toLowerCase() === 'text' && t.querySelector('tspan')) ? '' : (t.textContent || '').trim();
      if (!s) { return; }
      if (!t.getClientRects().length) { return; }
      var cs = getComputedStyle(t);
      if (cs.display === 'none' || cs.visibility === 'hidden') { return; }
      var m = t.getScreenCTM && t.getScreenCTM();
      if (!m) { return; }
      var fs = parseFloat(cs.fontSize);
      rec.nodes.push({ s: s.slice(0, 40), fs: fs, px: Math.round(fs * Math.hypot(m.a, m.b) * 100) / 100 });
    });
    if (rec.nodes.length) { out.push(rec); }
  });
  return JSON.stringify(out);
})()
"""

CLICK_JS = r"""
(function (i) {
  var mount = document.getElementById('ks4-mount') || document.body;
  var btns = Array.prototype.filter.call(mount.querySelectorAll('button'), function (b) {
    if (b.disabled || !b.getClientRects().length) { return false; }
    if (b.closest('nav, header, [data-tutor], #mrb-chat, .mrb-chat')) { return false; }
    return true;
  });
  if (i >= btns.length) { return -1; }
  btns[i].click();
  return btns.length;
})(%d)
"""

SCROLL_JS = r"""
(function () { var h = document.documentElement.scrollHeight, y = 0;
  return new Promise(function (res) { (function step() { window.scrollTo(0, y); y += 600;
    if (y < h + 600) { setTimeout(step, 60); } else { window.scrollTo(0, 0); res(true); } })(); }); })()
"""


def lessons(batch=None, only=None, all_routes=False):
    out = []
    names = ["pilot"] + sorted(ks4_lessons.batch_modules())
    for name in names:
        if batch and name != batch:
            continue
        for L in ks4_lessons.lessons_for_batch(name):
            if only and L["slug"] not in only:
                continue
            routes = list(L["routes"])
            if not all_routes:
                routes = ["TH"] if "TH" in routes else routes[:1]
            for r in routes:
                out.append((name, L["slug"], r))
    return out


BASELINE = False
BASELINE_JS = ("(function(){var s=document.createElement('style');"
               "s.textContent='[data-fig-fit]>svg{min-width:0!important}';document.head.appendChild(s);return true;})()")


def audit_page(browser, base, slug, route):
    url = base + ks4_lessons.site_url(slug, route)
    page = browser.attach()
    page.send("Emulation.setDeviceMetricsOverride",
              {"width": WIDTH, "height": HEIGHT, "deviceScaleFactor": 1, "mobile": False})
    page.goto(url, settle=0.6)
    if BASELINE:
        page.eval(BASELINE_JS)
    page.eval(SCROLL_JS, timeout=60)
    figs = {}

    def collect():
        for rec in json.loads(page.eval(MEASURE_JS) or "[]"):
            if rec["key"] not in figs:
                figs[rec["key"]] = rec

    collect()
    clicks = 0
    for i in range(MAX_CLICKS):
        n = page.eval(CLICK_JS % i)
        if n is None or n < 0:
            break
        clicks += 1
        time.sleep(0.12)
        if page.eval("location.pathname") != ks4_lessons.site_url(slug, route):
            page.goto(url, settle=0.6)
            continue
        collect()
    rows = []
    for idx, rec in enumerate(figs.values()):
        small = [n for n in rec["nodes"] if n["px"] < FLOOR]
        rows.append({
            "lesson": slug, "route": route, "figure": idx + 1, "alt": rec["alt"][:80],
            "viewbox": rec["vb"], "rendered_width": rec["width"],
            "scroll_width": rec.get("scrollW"), "column_width": rec.get("colW"),
            "text_nodes": len(rec["nodes"]), "smallest_px": min(n["px"] for n in rec["nodes"]),
            "below_floor": len(small), "samples": [n["s"] for n in sorted(small, key=lambda n: n["px"])[:4]],
        })
    return rows, clicks


def markdown(rows, bad, pages):
    lines = ["# KS4 figure text at %d px wide" % WIDTH, "",
             "%d page(s), %d figure(s), %d with text under %gpx." % (pages, len(rows), len(bad), FLOOR), ""]
    if bad:
        lines += ["| lesson | route | fig | alt | smallest px | nodes < %g | samples |" % FLOOR, "|---|---|---|---|---|---|---|"]
        for r in sorted(bad, key=lambda r: r["smallest_px"]):
            lines.append("| %s | %s | %d | %s | %.1f | %d / %d | %s |" % (
                r["lesson"], r["route"], r["figure"], r["alt"].replace("|", "/"), r["smallest_px"],
                r["below_floor"], r["text_nodes"], "; ".join(r["samples"]).replace("|", "/")))
    return "\n".join(lines) + "\n"


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--check", action="store_true", help="exit 1 if any figure text renders under 11px")
    ap.add_argument("--batch", help="pilot | batch-N only")
    ap.add_argument("--only", help="comma-separated lesson slugs")
    ap.add_argument("--all-routes", action="store_true")
    ap.add_argument("--baseline", action="store_true",
                    help="switch the phone text-floor CSS off first: the 'before' count the fix is measured against")
    ap.add_argument("--out", help="directory for audit.json / audit.md (default: gate_tmp()/ks4-figure-text)")
    args = ap.parse_args(argv)
    global BASELINE
    BASELINE = args.baseline

    if not os.path.isdir(SITE):
        print("ks4_figure_text_audit: mrbadmus_site/ is missing - build first (python3 build_all.py).")
        return 2
    only = set(args.only.split(",")) if args.only else None
    todo = lessons(args.batch, only, args.all_routes)
    missing = [(s, r) for _, s, r in todo
               if not os.path.exists(SITE + ks4_lessons.site_url(s, r))]
    if missing:
        print("ks4_figure_text_audit: %d built page(s) missing, first: %s %s" % (len(missing), *missing[0]))
        return 2

    server, port = ks3_browser.serve(SITE)
    base = "http://127.0.0.1:%d" % port
    rows, failures = [], []
    try:
        with ks3_browser.Browser() as browser:
            for n, (_, slug, route) in enumerate(todo, 1):
                try:
                    r, clicks = audit_page(browser, base, slug, route)
                except Exception as e:  # a page that cannot be driven is a finding, not a pass
                    failures.append("%s %s: %s" % (slug, route, e))
                    continue
                rows += r
                low = [x for x in r if x["below_floor"]]
                print("[%3d/%d] %-44s %s  figures %d  clicks %2d  %s" % (
                    n, len(todo), slug, route, len(r), clicks,
                    ("UNDER %gpx: %d fig(s), smallest %.1f" % (FLOOR, len(low), min(x["smallest_px"] for x in low)))
                    if low else "ok"), flush=True)
    finally:
        server.shutdown()

    bad = [r for r in rows if r["below_floor"]]
    out = args.out or os.path.join(ks3_browser.gate_tmp(), "ks4-figure-text")
    os.makedirs(out, exist_ok=True)
    with open(os.path.join(out, "audit.json"), "w", encoding="utf-8") as fh:
        json.dump({"width": WIDTH, "floor": FLOOR, "figures": rows, "undriveable": failures}, fh, indent=1)
    with open(os.path.join(out, "audit.md"), "w", encoding="utf-8") as fh:
        fh.write(markdown(rows, bad, len(todo)))
    print("\n%d page(s), %d figure(s), %d under %gpx, %d page(s) not driveable. Report: %s" % (
        len(todo), len(rows), len(bad), FLOOR, len(failures), out))
    for f in failures:
        print("  NOT DRIVEABLE:", f)
    if args.check and (bad or failures):
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
