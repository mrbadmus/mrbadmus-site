#!/usr/bin/env python3
"""brand_fingerprint.py — how many different logos does mrbadmus.com show?

Renders one page from every page family in headless Chrome, finds the brand
mark in the page's header as a visitor sees it, and fingerprints it: the
chevron geometry and colours, the wordmark text, typeface and weight. Pages
whose fingerprints match wear the same mark; the number of distinct
fingerprints is the number of logos on the site.

    python3 brand_fingerprint.py                      # local build (serves the repo root)
    python3 brand_fingerprint.py --base https://mrbadmus.com
    python3 brand_fingerprint.py --themes light,dark --widths 360,1280 --shots DIR
    python3 brand_fingerprint.py --expect-one         # exit 1 unless every family shows the ONE mark

The wordmark's colour is NOT in the fingerprint — it is the one permitted
variant (ink on light, cream on dark) — but it is reported per theme and,
with --expect-one, checked: ink in light, cream in dark, unless the header is
dark in both themes (the lockup then carries mrb-brand--on-dark).

Written for the one-mark run (Mide's ruling, 13 Sep 2026).
"""

import argparse
import hashlib
import json
import os
import sys
import time
from pathlib import Path

import ks3_browser as cdp

HERE = Path(__file__).resolve().parent

# One representative page per family. The compiled student and teacher
# screens draw their header only once real data arrives, so they are
# measured on the fixture pages their port generators write beside them
# (same template, same rulings, fixture data). teacher_fixtures/ is not
# published, so on --base https://… those two rows report "no brand found";
# the live proof for them is the bytes check in docs/brand/ONE-MARK-REPORT.md.
FAMILIES = [
    ("landing",            "/index.html"),
    ("ks4-gcse-hub",       "/ks4.html"),
    ("ks4-pathway",        "/combined/index.html"),
    ("ks4-tier",           "/combined/higher/index.html"),
    ("ks4-subject-hub",    "/combined/higher/physics/index.html"),
    ("ks4-topic",          "/combined/higher/physics/energy.html"),
    ("ks4-lesson-classic", "/combined/higher/physics/energy/efficiency.html"),
    ("ks4-lesson-pilot",   "/combined/higher/chemistry/bonding/chemical-bonds.html"),
    ("ks3-hub",            "/ks3/index.html"),
    ("ks3-unit",           "/ks3/biology/inheritance-and-dna/index.html"),
    ("ks3-lesson",         "/ks3/biology/inheritance-and-dna/chromosomes-genes-and-dna.html"),
    ("student-class",      "/student/class-fixture.html"),
    ("student-assignment", "/student/assignment-fixture.html"),
    ("student-classes",    "/student/classes.html"),
    ("student-settings",   "/student/settings.html"),
    ("teacher-today",      "/teacher/today.html"),
    ("teacher-classes",    "/teacher_fixtures/classes-fixture.html"),
    ("teacher-admin",      "/teacher/admin.html"),
    ("teacher-class",      "/teacher_fixtures/class-detail-fixture.html"),
    ("teacher-timetable",  "/teacher/timetable.html"),
    ("teacher-seating",    "/teacher/seating.html"),
    ("teacher-profile",    "/teacher-profile.html"),
    ("auth",               "/auth.html"),
    ("leaderboard",        "/leaderboard.html"),
    ("past-papers",        "/past-papers.html"),
    ("weekly-challenge",   "/weekly-challenge.html"),
    ("my-challenges",      "/my-challenges.html"),
    ("revision",           "/revision.html"),
    ("profile-setup",      "/profile-setup.html"),
    ("reset-password",     "/reset-password.html"),
    ("404",                "/404.html"),
    ("parents-public",     "/parents/index.html"),
    ("parents-sign-in",    "/parents/sign-in.html"),
    ("consumer",           "/consumer/signup.html"),
    ("consumer-admin",     "/consumer/admin-accounts.html"),
    ("org",                "/org/index.html"),
    ("org-sign-in",        "/org/sign-in.html"),
    ("go",                 "/go/index.html"),
    ("3d-studio",          "/3d/index.html"),
]

# Finds the brand as a visitor sees it: the first element in the top band of
# the page whose OWN text is the brand name, walked up to the link/box that
# also holds its chevron. Falls back to a chevron-only mark.
FIND_JS = r"""
(() => {
  const NAME = /^\s*Mr\s?Badmus(\s?AI)?(\s+KS3)?\s*$/i;
  const visible = e => { const r = e.getBoundingClientRect(); const s = getComputedStyle(e);
    return r.width > 0 && r.height > 0 && s.visibility !== 'hidden' && s.display !== 'none' && r.top < 420 && r.bottom > -5; };
  let word = null;
  const walker = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT);
  while (walker.nextNode()) {
    const t = walker.currentNode;
    const txt = t.textContent.replace(/[·|·—-]+$/, '');
    if (!t.parentElement || !NAME.test(txt)) continue;
    if (visible(t.parentElement)) { word = t.parentElement; break; }
  }
  let box = null;
  if (word) {
    box = word;
    for (let i = 0; i < 4 && box.parentElement; i++) {
      if (box.querySelector('svg,img') || box.tagName === 'A') { if (box.querySelector('svg,img')) break; }
      box = box.parentElement;
    }
    if (!box.querySelector('svg,img')) box = word.closest('a') || word;
  } else {
    const m = [...document.querySelectorAll('[data-mrb-mark], header svg, nav svg')].find(visible);
    box = m ? (m.closest('a') || m) : null;
  }
  if (!box) return {found: false};
  const svgs = [...box.querySelectorAll('svg')].filter(visible).slice(0, 2).map(s => {
    const shapes = [...s.querySelectorAll('path,polyline,line,rect,circle,text')].map(p => {
      const cs = getComputedStyle(p);
      return [p.tagName, (p.getAttribute('d') || p.getAttribute('points') || '').replace(/\s+/g, ' ').trim(),
              cs.stroke, cs.strokeOpacity, cs.strokeWidth, cs.fill, cs.fillOpacity, p.getAttribute('transform') || ''];
    });
    return {viewBox: s.getAttribute('viewBox'), shapes};
  });
  const imgs = [...box.querySelectorAll('img')].filter(visible).map(i => i.getAttribute('src'));
  const wcs = word ? getComputedStyle(word) : null;
  const r = box.getBoundingClientRect();
  const mr = (box.querySelector('svg') || box).getBoundingClientRect();
  return {
    found: true,
    word: word ? word.textContent.trim() : null,
    family: wcs ? wcs.fontFamily.split(',')[0].replace(/["']/g, '').trim() : null,
    weight: wcs ? wcs.fontWeight : null,
    wordColor: wcs ? wcs.color : null,
    wordSize: wcs ? wcs.fontSize : null,
    svgs, imgs,
    markSize: [Math.round(mr.width), Math.round(mr.height)],
    rect: [r.left, r.top, r.width, r.height],
    partial: !!box.querySelector('[data-mrb-mark]'),
    ground: (() => { let e = box; while (e) { const c = getComputedStyle(e).backgroundColor;
      if (c && c !== 'transparent' && !/rgba\([^)]*,\s*0\)$/.test(c)) return c; e = e.parentElement; }
      return getComputedStyle(document.documentElement).backgroundColor || 'rgb(255, 255, 255)'; })(),
    onDark: !!(box.closest('.mrb-brand--on-dark')),
    theme: document.documentElement.getAttribute('data-theme'),
    url: location.pathname,
    title: document.title,
  };
})()
"""

# Fonts the wordmark may name: the partial's alias and the family behind it.
WORD_FAMILIES = {"MrBadmus Wordmark": "Bricolage Grotesque"}
INK, CREAM = "rgb(34, 30, 27)", "rgb(251, 243, 230)"

# Where a page deliberately shows NO mark, by ruling, at or below a width.
# student/assignment.html is Design's exam task bar: below her `wide`
# breakpoint the bar holds back-link, class, clock and HANDED IN chip, and the
# lockup would push the clock off a 360px screen (lane C, one-mark run; the
# reasoning is beside RULED_BRAND in student_rulings.py). No mark is not a
# second mark; it is reported, never counted as one.
NO_MARK_BY_RULING = {"student-assignment": 719}


def _lum(rgb):
    import re as _re
    v = [int(x) / 255 for x in _re.findall(r"\d+", rgb)[:3]]
    v = [c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4 for c in v]
    return 0.2126 * v[0] + 0.7152 * v[1] + 0.0722 * v[2]


def contrast(a, b):
    la, lb = sorted((_lum(a), _lum(b)), reverse=True)
    return (la + 0.05) / (lb + 0.05)


def fingerprint(d):
    """The mark, minus the one permitted variant (the wordmark's colour)."""
    if not d.get("found"):
        return "NONE", "no brand found" + (f" ({d['error']})" if d.get("error") else "")
    fam = WORD_FAMILIES.get(d["family"], d["family"])
    key = {"word": d["word"], "family": fam, "weight": d["weight"],
           "svgs": d["svgs"], "imgs": d["imgs"]}
    h = hashlib.sha1(json.dumps(key, sort_keys=True).encode()).hexdigest()[:10]
    desc = f'"{d["word"]}" {fam} {d["weight"]}; ' + (
        "; ".join(f'svg {s["viewBox"]} ×{len(s["shapes"])}' for s in d["svgs"]) or "no svg") + (
        f'; img {d["imgs"]}' if d["imgs"] else "")
    return h, desc


# Signed-in pages send a signed-out browser to /auth.html (or stay blank
# behind a guard). The mark is in the page's own header either way, so the
# guard, Supabase and the backend are blocked and the body is revealed —
# the header is measured as the page ships it, never through a redirect.
BLOCK = ["*teacher-guard.js*", "*student-guard.js*"]
REVEAL_JS = ("(()=>{for(const e of [document.documentElement,document.body]){if(!e)continue;"
             "e.style.setProperty('visibility','visible','important');e.style.setProperty('opacity','1','important');"
             "e.hidden=false;if(getComputedStyle(e).display==='none')e.style.setProperty('display','block','important')};return 1})()")


def serve_build():
    """mrbadmus_site/ as published, falling back to the repo root for the
    unpublished fixture trees (teacher_fixtures/)."""
    import http.server
    import threading
    site, root = HERE / "mrbadmus_site", HERE

    class H(http.server.SimpleHTTPRequestHandler):
        def translate_path(self, path):
            p = super().translate_path(path)
            rel = os.path.relpath(p, os.getcwd())
            for base in (site, root):
                cand = base / rel
                if cand.exists():
                    return str(cand)
            return str(site / rel)

        def log_message(self, *a):
            pass

    srv = http.server.ThreadingHTTPServer(("127.0.0.1", 0), H)
    srv.daemon_threads = True
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    return srv, srv.server_address[1]


def set_theme(page, url, theme):
    page.goto(url)
    page.eval(f"(()=>{{try{{localStorage.setItem('mrb-theme','{theme}')}}catch(e){{}};return 1}})()")
    page.goto(url)
    page.eval(REVEAL_JS)


def clip_png(page, rect, path, pad=12):
    import base64
    x, y, w, h = rect
    clip = {"x": max(0, x - pad), "y": max(0, y - pad), "width": w + 2 * pad, "height": h + 2 * pad, "scale": 2}
    res = page.send("Page.captureScreenshot", {"format": "png", "clip": clip, "captureBeyondViewport": False})
    Path(path).write_bytes(base64.b64decode(res["data"]))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--base", default=None, help="site origin; default serves the local build")
    ap.add_argument("--themes", default="light")
    ap.add_argument("--widths", default="1280")
    ap.add_argument("--shots", default=None, help="screenshot dir (default $MRB_SHOTS/brand or gate tmp)")
    ap.add_argument("--full-shots", action="store_true", help="also save a viewport screenshot per page")
    ap.add_argument("--only", default=None, help="comma list of family names")
    ap.add_argument("--json", default=None)
    ap.add_argument("--expect-one", action="store_true")
    a = ap.parse_args()

    server = None
    base = a.base
    if not base:
        server, port = serve_build()
        base = f"http://127.0.0.1:{port}"
    base = base.rstrip("/")
    shots = Path(a.shots or os.path.join(os.environ.get("MRB_SHOTS") or cdp.gate_tmp(), "brand"))
    shots.mkdir(parents=True, exist_ok=True)
    fams = FAMILIES
    if a.only:
        want = set(a.only.split(","))
        fams = [f for f in FAMILIES if f[0] in want]

    rows, problems = [], []
    with cdp.Browser() as b:
        page = b.page("about:blank")
        page.send("Network.enable")
        page.send("Network.setBlockedURLs", {"urls": BLOCK})
        # The consumer product is behind CONSUMER_SIGNUP_ENABLED (off on the
        # live site). Its pages are measured in the ON state, exactly as the
        # consumer drives do, so the header that WILL ship is the one counted.
        from mrb327_marketing_drive import FLAG_ON_JS
        page.send("Page.addScriptToEvaluateOnNewDocument", {"source": FLAG_ON_JS})
        for theme in a.themes.split(","):
            for width in [int(w) for w in a.widths.split(",")]:
                page.set_viewport(width, 900)
                for fam, path in fams:
                    url = base + path
                    try:
                        set_theme(page, url, theme)
                        time.sleep(0.4)
                        d = page.eval(FIND_JS)
                    except Exception as e:  # noqa: BLE001 — a page that will not load is a row, not a crash
                        d = {"found": False, "error": str(e)[:120]}
                    if (fam != "404" and d.get("found")
                            and str(d.get("title", "")).startswith("Page not found")):
                        # An unpublished path (teacher_fixtures/ on the live
                        # site) serves the 404 page, which wears the mark too;
                        # counting it would prove the 404 page, not the family.
                        # ⊕ Stage B (28 Sep 2026) — except for the `404` family
                        # itself, whose page IS the 404 page: excluding it
                        # made `--expect-one` report 2 marks on every run.
                        d = {"found": False, "error": "served the 404 page"}
                    fp, desc = fingerprint(d)
                    tag = f"{fam}-{theme}-{width}"
                    if d.get("found"):
                        try:
                            clip_png(page, d["rect"], shots / f"mark-{tag}.png")
                        except Exception:
                            pass
                    if a.full_shots:
                        try:
                            page.screenshot(str(shots / f"page-{tag}.png"), width=width, height=900, full_page=False)
                        except Exception:
                            pass
                    rows.append({"family": fam, "path": path, "theme": theme, "width": width,
                                 "fp": fp, "desc": desc, "data": d})
                    if not (d.get("found") and d.get("partial")) and width <= NO_MARK_BY_RULING.get(fam, -1):
                        rows[-1]["fp"], rows[-1]["desc"] = "RULED-NONE", "no mark at this width, by ruling"
                    if a.expect_one and d.get("found") and rows[-1]["fp"] != "RULED-NONE":
                        # The one variant: ink or cream, whichever reads on
                        # the ground the header actually sits on.
                        wc, g = d.get("wordColor"), d.get("ground")
                        if wc not in (INK, CREAM):
                            problems.append(f"{tag}: wordmark {wc} is neither ink nor cream")
                        elif g and contrast(wc, g) < 4.5:
                            problems.append(f"{tag}: wordmark {wc} on {g} is {contrast(wc, g):.2f}:1 (< 4.5)")
    if server:
        server.shutdown()

    by_fp, ruled = {}, [r for r in rows if r["fp"] == "RULED-NONE"]
    for r in rows:
        if r["fp"] == "RULED-NONE":
            continue
        by_fp.setdefault(r["fp"], []).append(r)
    print(f"\n{len(by_fp)} distinct mark(s) across {len({r['family'] for r in rows})} families\n")
    for fp, rs in sorted(by_fp.items(), key=lambda kv: -len(kv[1])):
        fams_ = sorted({r["family"] for r in rs})
        print(f"  [{fp}] {rs[0]['desc']}")
        print(f"      {len(fams_)} families: {', '.join(fams_)}")
    for r in ruled:
        print(f"  (ruled) {r['family']} {r['theme']} {r['width']}px — no mark by ruling")
    if a.json:
        Path(a.json).write_text(json.dumps(rows, indent=1))
    print(f"\n  crops: {shots}")
    if a.expect_one:
        if len(by_fp) != 1 or "NONE" in by_fp:
            problems.insert(0, f"{len(by_fp)} distinct marks (want exactly 1)")
        for p in problems:
            print("  FAIL", p)
        return 1 if problems else 0
    return 0


if __name__ == "__main__":
    sys.exit(main())
