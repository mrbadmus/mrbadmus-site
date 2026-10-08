#!/usr/bin/env python3
"""Write ks4_lessons/start_here.py records into the batch 2/3 authored lessons.

  --apply SLUG...    first application (Ks4Choice hook -> Ks4Guess)
  --refresh SLUG...  re-render an already-applied lesson after a data edit
  --check            report applied / not applied; fail on a stale applied one
"""
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
from ks4_lessons import start_here as SH  # noqa: E402

SECTION_RE = re.compile(r'<section id="s-hook"[^>]*>.*?</section>', re.S)
OPT_START = "hookOptions: ["
OPT_END = "onHook: (i) => this.setState({ hook: i }),"
GUESS_OPT_RE = re.compile(r"hookOptions: \[.*?\n      \],\n      (?=onHook:)", re.S)


def path_for(slug):
    rec = SH.START_HERE.get(slug)
    if rec is None:
        raise SystemExit("%s: not in START_HERE" % slug)
    if rec["batch"] not in (SH.B2, SH.B3):
        raise SystemExit("%s: %s lessons are never edited here" % (slug, rec["batch"]))
    return os.path.join(ROOT, "ks4_lessons", "authored", rec["batch"], slug + ".dc.html")


def once(text, pat, slug, what):
    n = len(pat.findall(text)) if hasattr(pat, "findall") else text.count(pat)
    if n != 1:
        raise SystemExit("%s: anchor %s occurs %d times (need exactly 1)" % (slug, what, n))


def is_applied(text):
    return 'name="Ks4Guess"' in text


def apply(slug, refresh=False):
    p = path_for(slug)
    text = open(p, encoding="utf-8").read()
    applied = is_applied(text)
    if applied and not refresh:
        print("%s: already applied (no change)" % slug)
        return
    if refresh and not applied:
        raise SystemExit("%s: --refresh needs an applied lesson" % slug)
    once(text, SECTION_RE, slug, '<section id="s-hook">…</section>')
    sec = SECTION_RE.search(text)
    text = text[:sec.start()] + SH.render_section(slug) + text[sec.end():]
    if applied:
        once(text, GUESS_OPT_RE, slug, "two-option hookOptions span")
        m = GUESS_OPT_RE.search(text)
        text = text[:m.start()] + SH.render_options_js(slug) + text[m.end():]
    else:
        once(text, OPT_START, slug, OPT_START)
        once(text, OPT_END, slug, OPT_END)
        a = text.index(OPT_START)
        b = text.index(OPT_END)
        if b < a or "hookReveal:" not in text[a:b]:
            raise SystemExit("%s: hookOptions..onHook span lacks hookReveal" % slug)
        text = text[:a] + SH.render_options_js(slug) + text[b:]
        for old, new in SH.START_HERE[slug]["logic_swaps"]:
            once(text, old, slug, "logic swap " + old[:40])
            text = text.replace(old, new)
    open(p, "w", encoding="utf-8").write(text)
    print("%s: %s" % (slug, "refreshed" if refresh else "applied"))


def check():
    bad = 0
    for slug, rec in SH.START_HERE.items():
        if rec["batch"] not in (SH.B2, SH.B3):
            continue
        text = open(path_for(slug), encoding="utf-8").read()
        if not is_applied(text):
            print("%s: not applied" % slug)
            continue
        sec = SECTION_RE.search(text)
        m = GUESS_OPT_RE.search(text)
        ok = bool(sec and m and sec.group(0) == SH.render_section(slug)
                  and m.group(0) == SH.render_options_js(slug))
        print("%s: applied%s" % (slug, "" if ok else " — STALE (run --refresh)"))
        bad += not ok
    return 1 if bad else 0


def main(argv):
    if argv[:1] == ["--check"]:
        return check()
    if argv[:1] in (["--apply"], ["--refresh"]) and len(argv) > 1:
        for s in argv[1:]:
            apply(s, refresh=argv[0] == "--refresh")
        return 0
    print(__doc__)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
