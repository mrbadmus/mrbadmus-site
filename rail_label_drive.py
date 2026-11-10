#!/usr/bin/env python3
"""rail_label_drive.py — the sticky progress strip names the section on screen.

B2C small fixes (26 Oct 2026). The strip at the top of every lesson (KS3:
`shared/ks3.js` wireRail, `[data-rail-label]`; KS4: `shared/ks4-lib.js`
observe(), ks4_rulings R23, the `[data-rail="top"]` link) shows the name of
the section being read. It named the wrong one because (a) it was only
recomputed on scroll/resize (KS3) or when a section ENTERED a narrow band
(KS4), so a layout change with no scroll, or a band resting on the hero or a
gap, left it stale; and (b) a line fixed part-way down the screen can never
be reached by the last short sections, so the foot of the page named one or
two sections too early.

For one KS3 lesson and one KS4 lesson, at 390x844 and 1280x900, this checks:

  1. TOP. Scrolled to 0 the strip names the FIRST section.
  2. SWEEP. Scrolling down in steps, the strip names, at every stop, the
     section whose top is the greatest at or above the reading line (KS3 50%
     of the screen, KS4 45%, both sliding to the bottom edge over the last
     part-screen of scroll) — and the named section never moves backwards.
  3. BOTTOM. Scrolled to the end the strip names the LAST section.
  4. BACK TO TOP. After the sweep, scrolled back to 0, it names the first
     section again (KS4's band observer kept the last one).
  5. LAYOUT CHANGE, NO SCROLL. With a section just past the line, a block is
     inserted at the end of the section above it (as an answer's feedback
     would be); with no scroll event at all the strip must move back to that
     section within a second.

Network: every request off 127.0.0.1 is blocked (no production calls).
Screenshots go to $MRB_SHOTS (ks3_browser.gate_tmp()), never into the repo.

Run:  python3 rail_label_drive.py [--shots DIR]
"""

import argparse
import os
import sys
import time

import ks3_browser as cdp

ROOT = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(ROOT, "mrbadmus_site")

PAGES = [
    ("KS3", "/ks3/biology/cells-and-organisation/using-a-microscope.html", 0.5),
    ("KS4", "/combined/foundation/biology/ecology/carbon-cycle.html", 0.45),
]
SIZES = [(390, 844), (1280, 900)]
BLOCK = ["https://*", "wss://*", "http://localhost*", "*supabase.co*", "*onrender.com*"]

FAILS = []


def fail(msg):
    FAILS.append(msg)
    print("  FAIL  " + msg)


def ok(msg):
    print("  ok    " + msg)


# One reader for both key stages. `ids` are the sections in rail order;
# `shown` is the index of the section the strip names right now; `expect` is
# the section whose top is the greatest at or above the reading line.
READ = r"""
(function (kind, frac) {
  var ids = [], shown = -1, label = '', strip = true;
  if (kind === 'KS3') {
    var wrap = document.querySelector('.ks3-rails');
    var st = JSON.parse(wrap.getAttribute('data-rail-stages') || '[]');
    ids = st.map(function (s) { return s.anchor; });
    label = (document.querySelector('[data-rail-label]') || {}).textContent || '';
    label = label.trim();
    for (var i = 0; i < st.length; i++) { if ((st[i].label || '') === label) { shown = i; break; } }
  } else {
    ids = Array.prototype.map.call(
      document.querySelectorAll('[data-rail="side"] a[href^="#"]'),
      function (a) { return a.getAttribute('href').slice(1); });
    var top = document.querySelector('[data-rail="top"] a[href^="#"]');
    label = top ? top.textContent.trim() : '';
    shown = top ? ids.indexOf(top.getAttribute('href').slice(1)) : -1;
    strip = !!top;
  }
  var doc = document.documentElement, vh = innerHeight;
  var max = Math.max(0, doc.scrollHeight - vh), y = scrollY;
  var left = Math.max(0, max - y), slide = vh * (1 - frac);
  var line = vh * frac + (left < slide ? slide - left : 0);
  var exp = -1, expTop = -Infinity, first = -1, firstTop = Infinity, tops = [];
  ids.forEach(function (id, k) {
    var el = document.getElementById(id);
    var r = el && el.getBoundingClientRect();
    if (!r || (!r.width && !r.height)) { tops.push(null); return; }
    tops.push(Math.round(r.top));
    if (r.top < firstTop) { first = k; firstTop = r.top; }
    if (r.top <= line && r.top >= expTop) { exp = k; expTop = r.top; }
  });
  return { ids: ids, shown: shown, label: label, strip: strip, expect: exp >= 0 ? exp : first,
           y: y, max: max, vh: vh, line: Math.round(line), tops: tops };
})(%r, %r)
"""

NO_ANCHOR = "document.documentElement.style.overflowAnchor='none';1"


def read(page, kind, frac):
    return page.eval(READ % (kind, frac))


def scroll_to(page, y, wait=0.35):
    # `instant`: KS3's html carries scroll-behavior: smooth, and a smooth
    # scroll still under way is not a resting place to read the label at.
    page.eval("window.scrollTo({top: %d, left: 0, behavior: 'instant'}); 1" % int(y))
    time.sleep(wait)


def drive(b, base, kind, path, frac, size, shots):
    w, h = size
    tag = "%s %dx%d" % (kind, w, h)
    page = b.page("about:blank")
    page.send("Network.enable")
    page.send("Network.setBlockedURLs", {"urls": BLOCK})
    page.set_viewport(w, h)
    page.goto(base + path, settle=2.5)
    page.eval(NO_ANCHOR)
    s = read(page, kind, frac)
    if len(s["ids"]) < 3:
        fail("%s: only %d rail sections found" % (tag, len(s["ids"])))
        return

    # The highest resting place at which the strip is drawn: KS3 always; KS4
    # only past 140px (Design's Ks4Chrome `scrolled`), so its "top" is 150.
    top_y = 150 if kind == "KS4" else 0

    # 1. top
    scroll_to(page, top_y)
    s = read(page, kind, frac)
    (ok if s["shown"] == 0 else fail)("%s top (y=%d): names section %d (%r), want 0" % (tag, top_y, s["shown"], s["label"]))

    # 2. sweep
    steps, prev, bad, hidden = 30, -1, 0, 0
    for n in range(steps + 1):
        scroll_to(page, s["max"] * n / steps, wait=0.25)
        r = read(page, kind, frac)
        if not r["strip"]:
            hidden += 1
            continue
        if r["shown"] != r["expect"]:
            bad += 1
            if bad <= 3:
                fail("%s sweep y=%d: names %d (%r), section at the line is %d; line %d, tops %s"
                     % (tag, r["y"], r["shown"], r["label"], r["expect"], r["line"], r["tops"]))
        if r["shown"] < prev:
            fail("%s sweep y=%d: went BACK from %d to %d while scrolling down" % (tag, r["y"], prev, r["shown"]))
        prev = max(prev, r["shown"])
        if n == steps // 2 and shots:
            page.screenshot(os.path.join(shots, "rail-%s-%d-mid.png" % (kind.lower(), w)), width=w, height=h, full_page=False)
    if not bad:
        ok("%s sweep: %d stops (%d with the strip not drawn), label = section at the line every time"
           % (tag, steps + 1, hidden))

    # 3. bottom
    scroll_to(page, s["max"] + 50)
    r = read(page, kind, frac)
    last = len(r["ids"]) - 1
    (ok if r["shown"] == last else fail)("%s bottom: names section %d (%r), want the last (%d)" % (tag, r["shown"], r["label"], last))
    if shots:
        page.screenshot(os.path.join(shots, "rail-%s-%d-bottom.png" % (kind.lower(), w)), width=w, height=h, full_page=False)

    # 4. back to top
    scroll_to(page, top_y)
    r = read(page, kind, frac)
    (ok if r["shown"] == 0 else fail)("%s back to top (y=%d): names section %d (%r), want 0" % (tag, top_y, r["shown"], r["label"]))

    # 5. layout change with no scroll: put section k's top just above the line,
    # then grow the page by a screen IMMEDIATELY ABOVE section k (as feedback
    # opening at the end of the section before it would). No scroll happens.
    k = 2 if len(r["ids"]) > 3 else 1
    top_k = page.eval("document.getElementById(%r).getBoundingClientRect().top + scrollY" % r["ids"][k])
    scroll_to(page, max(top_y, top_k - h * frac + 20), wait=0.6)
    before = read(page, kind, frac)
    y0 = before["y"]
    # ⊕ 10 Nov 2026: grown by a STYLE RULE on section k-1, not an inserted
    # <div>. A KS4 lesson re-syncs its DOM to its template when the label
    # changes and drops any node the template doesn't own, so an inserted
    # div vanished the moment the strip reacted and the check read the old
    # layout. A rule in <head> survives that, as template-driven growth does.
    page.eval(r"""(function (id, hgt) {
      var s = document.createElement('style');
      s.setAttribute('data-rail-drive', '1');
      s.textContent = '#' + CSS.escape(id) + ' { padding-bottom: ' + hgt + 'px !important; }';
      document.head.appendChild(s);
      return 1; })(%r, %d)""" % (before["ids"][k - 1], h))
    time.sleep(1.0)
    after = read(page, kind, frac)
    page.eval("document.querySelectorAll('[data-rail-drive]').forEach(function (e) { e.remove(); }); 1")
    if abs(after["y"] - y0) > 1:
        fail("%s layout change: the page scrolled (%d -> %d), the check is void" % (tag, y0, after["y"]))
    elif before["shown"] != k:
        fail("%s layout change: setup named %d, want %d; tops %s" % (tag, before["shown"], k, before["tops"]))
    else:
        (ok if after["shown"] == after["expect"] == k - 1 else fail)(
            "%s layout change, no scroll: %d -> %d (section at the line now %d; tops %s -> %s)"
            % (tag, before["shown"], after["shown"], after["expect"], before["tops"], after["tops"]))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--shots", default=None, help="screenshot dir (default: $MRB_SHOTS / gate tmp)")
    a = ap.parse_args()
    shots = a.shots or os.path.join(cdp.gate_tmp(), "rail_label_drive")
    os.makedirs(shots, exist_ok=True)
    for _k, p, _f in PAGES:
        if not os.path.exists(OUT + p):
            print("missing built page %s — run build_all.py first" % p)
            return 2
    server, port = cdp.serve(OUT)
    base = "http://127.0.0.1:%d" % port
    try:
        with cdp.Browser() as b:
            for kind, path, frac in PAGES:
                for size in SIZES:
                    print("\n%s %s at %dx%d" % (kind, path, size[0], size[1]))
                    drive(b, base, kind, path, frac, size, shots)
    finally:
        server.shutdown()
    print("\nscreenshots: %s" % shots)
    print("%s" % ("FAILED: %d" % len(FAILS) if FAILS else "rail_label_drive: all checks passed"))
    return 1 if FAILS else 0


if __name__ == "__main__":
    sys.exit(main())
