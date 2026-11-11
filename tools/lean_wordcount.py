#!/usr/bin/env python3
"""tools/lean_wordcount.py: words on each lean pilot page, before and after.

    python3 tools/lean_wordcount.py [--ref origin/main] [--route CH]

For every lean lesson (KS3 records in ks3_data/lean, KS4 lessons in the lean batch) it
prints two numbers for the page as it was on --ref (default origin/main, via `git show`)
and as it is in the working tree's mrbadmus_site/:

    core    words from the lesson heading down to the Practice section: the teaching a
            pupil reads before the questions (Start here, key words, key knowledge, key
            fact on a lean page; everything above the ladder on an old page)
    deeper  words in Dive deeper (a lean page only; an old page has none)

Words are counted from the page's visible text (scripts, styles and tags removed). A KS4
page is counted on one route (--route, default CH) because the four routes differ only by
their route-gated cards. The Practice section, quiz and end matter are not counted.
"""
import argparse
import html
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)

ROUTE_DIR = {"CF": "combined/foundation", "CH": "combined/higher",
             "TF": "triple/foundation", "TH": "triple/higher"}


def words(fragment):
    t = re.sub(r"(?is)<(script|style|svg)\b.*?</\1>", " ", fragment)
    t = re.sub(r"<[^>]+>", " ", t)
    return len(html.unescape(t).split())


def split(page):
    """(core_words, deeper_words) for one page's html."""
    m = re.search(r"(?is)<h1\b", page)
    body = page[m.start():] if m else page
    deeper = 0
    d = re.search(r'(?is)<section class="lean-sec lean-sec-deeper".*?</section>', body)
    if d:
        deeper = words(d.group(0))
        body = body.replace(d.group(0), " ")
    cut = re.search(r'(?i)id="s-ladder"|class="ks3-ladder"|class="ks3-block ks3-ladder"', body)
    core = words(body[:cut.start()] if cut else body)
    return core, deeper


def git_show(ref, path):
    r = subprocess.run(["git", "show", "%s:%s" % (ref, path)], cwd=ROOT,
                       capture_output=True, text=True)
    return r.stdout if r.returncode == 0 else None


def pages(route):
    import ks3_data
    import ks3_data.lean as k3
    import ks4_lessons
    reg = ks3_data.lesson_registry()
    for slug in sorted(k3.records()):
        l = reg[slug]
        disc = ks3_data.structure.unit_index()[l["_unit"]]["discipline"]
        yield "ks3 " + slug, "mrbadmus_site/ks3/%s/%s/%s.html" % (disc, l["_unit_slug"], slug)
    for L in ks4_lessons.lean_lessons():
        r = route if route in L["routes"] else L["routes"][-1]
        yield "ks4 " + L["slug"], "mrbadmus_site/%s/%s/%s/%s.html" % (
            ROUTE_DIR[r], L["subject"], L["topic_id"], L["slug"])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--ref", default="origin/main")
    ap.add_argument("--route", default="CH")
    a = ap.parse_args()
    print("%-34s %12s %12s %10s %10s" % ("page", "core before", "core after", "deeper", "change"))
    tb = ta = 0
    for name, path in pages(a.route):
        before = git_show(a.ref, path)
        after = open(os.path.join(ROOT, path), encoding="utf-8").read() \
            if os.path.exists(os.path.join(ROOT, path)) else None
        cb = split(before)[0] if before else None
        ca, da = split(after) if after else (None, None)
        if cb is not None and ca is not None:
            tb, ta = tb + cb, ta + ca
        chg = ("%+d%%" % round((ca - cb) * 100.0 / cb)) if cb and ca is not None else "-"
        print("%-34s %12s %12s %10s %10s" % (name, cb if cb is not None else "-",
                                              ca if ca is not None else "-",
                                              da if da is not None else "-", chg))
    if tb:
        print("%-34s %12d %12d %10s %10s" % ("total", tb, ta, "", "%+d%%" % round((ta - tb) * 100.0 / tb)))


if __name__ == "__main__":
    main()
