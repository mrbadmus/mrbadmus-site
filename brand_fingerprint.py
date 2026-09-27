#!/usr/bin/env python3
"""brand_fingerprint.py — how many different logos does mrbadmus.com show?

Renders one page from every page family in headless Chrome, finds the brand
mark in the page's header as a visitor sees it, and fingerprints it: the
chevron geometry and colours, the wordmark text, typeface and weight. Pages
whose fingerprints match wear the same mark; the number of distinct
fingerprints is the number of logos on the site.

    python3 brand_fingerprint.py                      # local build (serves mrbadmus_site/)
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

# One representative page per family. Signed-in surfaces are measured on the
# fixture/preview pages their generators publish beside them (same template,
# same header) because the live page redirects a signed-out browser away.
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
    ("teacher-classes",    "/teacher/classes.html"),
    ("teacher-admin",      "/teacher/admin.html"),
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
    ("org",                "/org/index.html"),
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
    return r.width > 0 && r.height > 0 && s.visibility !== 'hidden' && s.display !== 'none' && r.top < 160 && r.bottom > -5; };
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
    onDark: !!(box.closest('.mrb-brand--on-dark')),
    theme: document.documentElement.getAttribute('data-theme'),
    title: document.title,
  };
})()
"""

# Fonts the wordmark may name: the partial's alias and the family behind it.
WORD_FAMILIES = {"MrBadmus Wordmark": "Bricolage Grotesque"}
INK, CREAM = "rgb(34, 30, 27)", "rgb(251, 243, 230)"


def fingerprint(d):
    """The mark, minus the one permitted variant (the wordmark's colour)."""
    if not d.get("found"):
        return "NONE", "no brand found"
    fam = WORD_FAMILIES.get(d["family"], d["family"])
    key = {"word": d["word"], "family": fam, "weight": d["weight"],
           "svgs": d["svgs"], "imgs": d["imgs"]}
    h = hashlib.sha1(json.dumps(key, sort_keys=True).encode()).hexdigest()[:10]
    desc = f'"{d["word"]}" {fam} {d["weight"]}; ' + (
        "; ".join(f'svg {s["viewBox"]} ×{len(s["shapes"])}' for s in d["svgs"]) or "no svg") + (
        f'; img {d["imgs"]}' if d["imgs"] else "")
    return h, desc


def set_theme(page, url, theme):
    page.goto(url)
    page.eval(f"(()=>{{try{{localStorage.setItem('mrb-theme','{theme}')}}catch(e){{}};return 1}})()")
    page.goto(url)


def clip_png(page, rect, path, pad=12):
    import base64
    x, y, w, h = rect
    clip = {"x": max(0, x - pad), "y": max(0, y - pad), "width": w + 2 * pad, "height": h + 2 * pad, "scale": 2}
    res = page.send("Page.captureScreenshot", {"format": "png", "clip": clip, "captureBeyondViewport": False})
    Path(path).write_bytes(base64.b64decode(res["data"]))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--base", default=None, help="site origin; default serves ./mrbadmus_site")
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
        server, port = cdp.serve(str(HERE / "mrbadmus_site"))
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
                    if a.expect_one and d.get("found"):
                        want = CREAM if (theme == "dark" or d.get("onDark")) else INK
                        if d.get("wordColor") and d["wordColor"] != want:
                            problems.append(f"{tag}: wordmark {d['wordColor']}, want {want}")
    if server:
        server.shutdown()

    by_fp = {}
    for r in rows:
        by_fp.setdefault(r["fp"], []).append(r)
    print(f"\n{len(by_fp)} distinct mark(s) across {len({r['family'] for r in rows})} families\n")
    for fp, rs in sorted(by_fp.items(), key=lambda kv: -len(kv[1])):
        fams_ = sorted({r["family"] for r in rs})
        print(f"  [{fp}] {rs[0]['desc']}")
        print(f"      {len(fams_)} families: {', '.join(fams_)}")
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
