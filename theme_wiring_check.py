#!/usr/bin/env python3
"""theme_wiring_check — every served page carries the site theme wiring.

Theme run, 26 Sep 2026 (Mide's ruling: light by default, a Light / Dark /
System control on every page). A page is wired when:

  1. its <head> contains theme_head.THEME_HEAD byte for byte, BEFORE its first
     stylesheet (so the theme is set before anything paints);
  2. it loads /shared/theme.js;
  3. it carries a control slot — `data-mrb-theme` — either in its static
     markup or inside the compiled template a runtime mounts (the student,
     teacher and leaderboard pages render their header from JSON).

Scope: every .html under mrbadmus_site/, minus the EXEMPT list below, each
with its reason. A new page family that forgets the wiring turns this red.

Usage: python3 theme_wiring_check.py [--root mrbadmus_site] [--list]
"""
from __future__ import annotations

import argparse
import os
import re
import sys

from theme_head import THEME_HEAD

HERE = os.path.dirname(os.path.abspath(__file__))

# path prefix (relative to the served root) -> why it is not a themed page
EXEMPT = {
    "3d/": "3D Studio — a separate Vite app with its own build (3d-studio/); see docs/theme/REPORT.md",
    "teacher_fixtures/": "gate fixtures, not served to users",
    "student/class-fixture.html": "gate fixture (student_behaviour drives it with Design's values)",
    "student/assignment-fixture.html": "gate fixture",
}
EXEMPT_RE = [
    (re.compile(r"(^|/)[^/]*-fixture\.html$"), "gate fixture"),
    (re.compile(r"(^|/)[^/]*-preview\.html$"), "Design-fidelity preview snapshot (build_student.py), not linked"),
]

STYLESHEET = re.compile(r"<link[^>]+rel=[\"']?stylesheet", re.I)
REDIRECT = re.compile(r"<meta[^>]+http-equiv=[\"']?refresh", re.I)


def exempt_reason(rel: str) -> str | None:
    for pre, why in EXEMPT.items():
        if rel == pre or rel.startswith(pre):
            return why
    for rx, why in EXEMPT_RE:
        if rx.search(rel):
            return why
    return None


def check(path: str) -> list[str]:
    with open(path, encoding="utf-8", errors="replace") as fh:
        html = fh.read()
    if REDIRECT.search(html) and len(html) < 2000:
        return []  # a bare redirect stub paints nothing
    problems = []
    head_end = html.lower().find("</head>")
    head = html[: head_end if head_end >= 0 else len(html)]
    i = head.find(THEME_HEAD)
    if i < 0:
        problems.append("no pre-paint THEME_HEAD snippet in <head>")
    else:
        m = STYLESHEET.search(head)
        if m and m.start() < i:
            problems.append("THEME_HEAD comes after the first stylesheet")
    if "/shared/theme.js" not in html:
        problems.append("does not load /shared/theme.js")
    if "data-mrb-theme" not in html:
        problems.append("no data-mrb-theme control slot")
    return problems


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=os.path.join(HERE, "mrbadmus_site"))
    ap.add_argument("--list", action="store_true", help="print every page's status")
    args = ap.parse_args()

    bad, ok, skipped = {}, 0, {}
    for d, _dirs, files in os.walk(args.root):
        for f in files:
            if not f.endswith(".html"):
                continue
            full = os.path.join(d, f)
            rel = os.path.relpath(full, args.root).replace(os.sep, "/")
            why = exempt_reason(rel)
            if why:
                skipped[rel] = why
                continue
            probs = check(full)
            if probs:
                bad[rel] = probs
            else:
                ok += 1
                if args.list:
                    print("ok   ", rel)
    for rel in sorted(bad):
        print("FAIL ", rel, "—", "; ".join(bad[rel]))
    print("theme_wiring_check: %d wired, %d not wired, %d exempt" % (ok, len(bad), len(skipped)))
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
