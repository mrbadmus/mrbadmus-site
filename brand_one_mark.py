#!/usr/bin/env python3
"""brand_one_mark.py — the gate that keeps mrbadmus.com at ONE logo.

Mide's ruling, 13 Sep 2026: one mark everywhere — the forward double chevron
(front solid, back faded) + the wordmark "MrBadmus". Before the one-mark run
(27 Sep 2026) the site carried seven: a gold-to-rust gradient chevron, KS3's
single upward chevron, three hand-copied double chevrons (two with the solid
and faded halves mirrored), a plain-text staff wordmark and a Bricolage 800
"MrBadmusAI". Every one of them was a copy somebody made in good faith. This
gate makes a copy impossible to ship.

It checks, statically and fast:

  1. THE KIT. shared/brand/*.svg are Design's kit (docs/brand/source/) with
     only the <metadata> provenance stripped — never redrawn.
  2. THE JS COPY. shared/brand/brand.js is exactly what brand.py writes.
  3. EVERY PUBLISHED PAGE. In mrbadmus_site/, any SVG that draws the double
     chevron is byte-for-byte brand.MARK_SVG — or, on a page whose header is
     drawn in JavaScript, the page loads /shared/brand/brand.js. No page carries
     a retired mark (the gradient `navGrad`, KS3's `M4 16L12 7`, `ks3-brand`,
     a mirrored chevron), the octopus or the alembic.
  4. THE NAME. No <title>, og:/twitter: tag, meta name or brand element says
     "MrBadmusAI" / "Mr Badmus AI" / "MrBadmus AI". (Feature labels naming
     the tutor — "Ask MrBadmusAI" — are body copy, parked for Mide, and are
     not checked here.)
  5. THE SOURCES. No generator or shared script outside brand.py spells out
     the chevron's paths — a page gets the mark from brand.py or brand.js.

    python3 brand_one_mark.py            # gate: exit 1 on any violation
    python3 brand_one_mark.py --report   # counts only, never fails
"""

import argparse
import re
import subprocess
import sys
from pathlib import Path

import brand

HERE = Path(__file__).resolve().parent
SITE = HERE / "mrbadmus_site"

FRONT = "M12 3.5 L19.5 11 L12 18.5"
BACK = "M3.5 3.5 L11 11 L3.5 18.5"

# Retired marks, by the bytes that identify each. Checked in published HTML
# and in the shared CSS/JS a page loads.
RETIRED = {
    "gold-to-rust gradient chevron": re.compile(r'id="navGrad"|url\(#navGrad\)'),
    "KS3 single upward chevron": re.compile(r'M4 16L12 7l8 9|class="ks3-brand"'),
    "KS3 favicon (upward chevron)": re.compile(r"PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTQgMTZM"),
    "inline data: favicon": re.compile(r'<link[^>]+rel="icon"[^>]+href="data:'),
    "octopus logo": re.compile(r"🐙|octopus", re.I),
    "alembic emoji": re.compile(r"⚗"),
}

OLD_NAME = re.compile(r"MrBadmusAI|Mr Badmus AI|MrBadmus AI")
TITLE_RE = re.compile(r"<title>(.*?)</title>", re.S)
META_RE = re.compile(r'<meta[^>]+(?:property|name)="(?:og:[^"]*|twitter:[^"]*|application-name|apple-mobile-web-app-title|author)"[^>]*>')
SVG_RE = re.compile(r"<svg\b.*?</svg>", re.S)

# Published pages that are not pages a visitor reads: Design's fixtures and
# previews carry Design's own drawing on purpose (they are parity references),
# and Google's site-verification stub has no chrome at all.
SKIP_PAGES = (
    re.compile(r"-fixture\.html$"),
    re.compile(r"-preview\.html$"),
    re.compile(r"^google[0-9a-f]+\.html$"),
)

# Sources allowed to spell out the chevron's paths.
PATH_OWNERS = {"brand.py", "shared/brand/brand.js", "shared/brand/mrbadmus-chevron.svg",
               "shared/brand/mrbadmus-favicon.svg", "shared/brand/mrbadmus-app-icon-light.svg",
               "shared/brand/mrbadmus-app-icon-dark.svg", "shared/brand/mrbadmus-lockup-light.svg",
               "shared/brand/mrbadmus-lockup-dark.svg", "brand_one_mark.py", "brand_fingerprint.py"}
# Tracked trees that hold other people's drawings on purpose (Design's
# deliveries, frozen references, reports) — not sources of a published page.
SOURCE_SKIP = re.compile(
    r"^(docs/|mrbadmus_site/|_design-reference/|KS3 P\d+ lessons/|ks3-[^/]+/|\.design-sync/|"
    r"combined/|triple/|ks3/|"
    r"teacher_fixtures/|leaderboard_fixtures/|student_templates\.json$|"
    r"3d-studio/reference/|.*\.dc\.html$|.*\.md$)")


def family(rel):
    p = rel.split("/")
    if p[0] in ("combined", "triple"):
        return "ks4"
    if p[0] in ("ks3", "student", "teacher", "consumer", "parents", "org", "go", "3d"):
        return p[0]
    return "root"


def strip_kit(svg):
    svg = re.sub(r"\s*<metadata>.*?</metadata>", "", svg, flags=re.S)
    return svg.replace(' xmlns:c2pa="http://c2pa.org/manifest"', "")


def check_kit(errs):
    src = HERE / "docs/brand/source"
    for f in sorted(src.glob("*.svg")):
        shipped = HERE / "shared/brand" / f.name
        if not shipped.exists():
            errs.append(f"kit: shared/brand/{f.name} missing")
        elif shipped.read_text(encoding="utf-8") != strip_kit(f.read_text(encoding="utf-8")):
            errs.append(f"kit: shared/brand/{f.name} is not Design's kit file minus <metadata>")
    if (HERE / "shared/brand/brand.js").read_text(encoding="utf-8") != brand.brand_js():
        errs.append("kit: shared/brand/brand.js is stale — run python3 brand.py (or the build)")


def check_pages(errs, counts):
    for path in sorted(SITE.rglob("*.html")):
        rel = path.relative_to(SITE).as_posix()
        if any(r.search(rel) for r in SKIP_PAGES):
            continue
        html = path.read_text(encoding="utf-8", errors="replace")
        fam = family(rel)
        c = counts.setdefault(fam, {"pages": 0, "one-mark": 0, "runtime": 0, "violations": 0})
        c["pages"] += 1
        bad = []
        for label, rx in RETIRED.items():
            if rx.search(html):
                bad.append(label)
        chevrons = [s for s in SVG_RE.findall(html) if FRONT in s or BACK in s]
        foreign = [s for s in chevrons if s != brand.MARK_SVG]
        if foreign:
            bad.append(f"{len(foreign)} chevron SVG(s) not drawn by brand.py")
        runtime = "/shared/brand/brand.js" in html
        if brand.MARK_SVG in html:
            c["one-mark"] += 1
        elif runtime:
            c["runtime"] += 1
        m = TITLE_RE.search(html)
        if m and OLD_NAME.search(m.group(1)):
            bad.append(f"title says {OLD_NAME.search(m.group(1)).group(0)!r}")
        for meta in META_RE.findall(html):
            if OLD_NAME.search(meta):
                bad.append("meta tag carries the old name")
                break
        for a in re.findall(r'<a[^>]+class="[^"]*\b(?:mrb-brand|nav-brand|tb-brand|brand)\b[^"]*"[^>]*>.*?</a>', html, re.S):
            if OLD_NAME.search(re.sub(r"<[^>]+>", "", a)):
                bad.append("brand link says the old name")
                break
        if bad:
            c["violations"] += 1
            errs.append(f"{rel}: " + "; ".join(bad))


def check_sources(errs):
    files = subprocess.run(["git", "ls-files"], cwd=HERE, capture_output=True, text=True).stdout.split("\n")
    for rel in files:
        if not rel or rel in PATH_OWNERS or SOURCE_SKIP.match(rel):
            continue
        if not rel.endswith((".py", ".js", ".ts", ".tsx", ".css")):
            continue
        p = HERE / rel
        if not p.is_file():
            continue
        t = p.read_text(encoding="utf-8", errors="replace")
        if FRONT in t or BACK in t:
            errs.append(f"source {rel}: spells out the chevron — take it from brand.py / brand.js")
        for label in ("gold-to-rust gradient chevron", "KS3 single upward chevron"):
            if RETIRED[label].search(t) and not rel.endswith("brand_one_mark.py"):
                errs.append(f"source {rel}: carries the retired {label}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--report", action="store_true")
    ap.add_argument("--limit", type=int, default=40)
    a = ap.parse_args()
    errs, counts = [], {}
    check_kit(errs)
    check_pages(errs, counts)
    check_sources(errs)
    print("brand_one_mark — pages by family (one-mark = carries brand.py's mark; runtime = draws it from brand.js)")
    for fam, c in sorted(counts.items()):
        print(f"  {fam:9} {c['pages']:5} pages  {c['one-mark']:5} one-mark  {c['runtime']:4} runtime  {c['violations']:5} with violations")
    if errs:
        print(f"\n{len(errs)} violation(s):")
        for e in errs[: a.limit]:
            print("  ✗", e)
        if len(errs) > a.limit:
            print(f"  … and {len(errs) - a.limit} more")
    else:
        print("\n✅ one mark: no retired mark, no foreign chevron, no old name in chrome.")
    return 0 if (a.report or not errs) else 1


if __name__ == "__main__":
    sys.exit(main())
