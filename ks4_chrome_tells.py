#!/usr/bin/env python3
"""ks4_chrome_tells.py — Design's sample must not reach a student (MRB-301).

    "A shipped {{ subjectName }} is the failure mode of this entire run."

── WHAT THIS WATCHES ──────────────────────────────────────────────────────

Claude Design's 23 Aug 2026 chrome delivery is a CLICK-THROUGH, not a page.
It ships:

  · template tokens — {{ subjectName }}, {{ goHome }}, {{ paper1 }}, {{ t.open }}
  · directive elements and attributes — <sc-if>, <sc-for>, <x-import>,
    style-hover=, data-screen-label=, onClick=
  · placeholder links — every href in the file is "#"
  · and INVENTED NUMBERS: 68%, 80%, 76%, "14th of 212", "3 of 7 done",
    "6 of 24 topics", "4/7", "21/62", "7 topics", "10 topics", "11 units",
    plus two students who do not exist, CoralTrail56 and SlateHarrier9.

The numbers are the dangerous half. A stray `{{ subjectName }}` is obvious
the second anybody looks at the page. "Your best 68%" is not: it is
plausible, it is the right shape, and a student would simply believe it.
That is the same property `teacher_tells` was written for — Design's
invented school was plausible too — and it is why this gate exists rather
than a code review.

── THE CORPUS IS DERIVED, NOT TYPED ───────────────────────────────────────

Every banned token, percentage, fraction and handle below is parsed OUT OF
the vendored delivery on each run. `student_page_drive.py` records what a
hand-written list costs, in its own words: "THIS LIST WAS TOO SHORT AND THE
DRIVE PASSED BECAUSE OF IT."

The few phrases that ARE named literally (Design's drawn sample copy —
prose, which no regex can pick out of prose) are each asserted to be
PRESENT IN THE DELIVERY first. So a named phrase cannot quietly stop
meaning anything: if Design's file changes, this gate goes red and tells
you the phrase is gone, instead of continuing to search built pages for a
string nobody writes any more.

── AND IT CHECKS THE DESTINATIONS ─────────────────────────────────────────

Every link in the delivery is `href="#"`. "Every control wires to a REAL
destination" cannot be proved by reading the generator, so the last check
walks every internal href on every built chrome page and resolves it
against the built tree. A control that goes nowhere fails the build.

Run:  python3 ks4_chrome_tells.py
"""

import os
import re
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
DELIVERY = os.path.join(ROOT, "docs", "ks3", "design-reference", "chrome",
                        "MrBadmusAI Redesign.dc.html")
OUT = os.path.join(ROOT, "mrbadmus_site")

# The pages MRB-301 ported. Anything else in the built tree is another
# run's business and is not read here.
CHROME_GLOBS = [
    "index.html",
    "ks4.html",
    "{pw}/index.html",
    "{pw}/{tier}/index.html",
    "{pw}/{tier}/{subj}/index.html",
]

failures = []


def fail(msg):
    failures.append(msg)


def rel(p):
    return os.path.relpath(p, ROOT)


# ══════════════════════════════════════════════════════════════════════════
#  The pages under test
# ══════════════════════════════════════════════════════════════════════════

def chrome_pages():
    """Every page this run writes: the two landings, the pathway and tier
    pages, the twelve subject hubs, and every topic page.

    Derived by WALKING the built tree, not by listing: a topic page added
    to the spec tomorrow is covered without editing this file. Topic pages
    are the .html files that sit beside a directory of the same name —
    which is exactly what distinguishes a topic hub from the LESSON pages
    inside that directory, and the lesson pages are out of scope."""
    pages = []
    for name in ("index.html", "ks4.html"):
        p = os.path.join(OUT, name)
        if os.path.exists(p):
            pages.append(p)
    for pw in ("combined", "triple"):
        p = os.path.join(OUT, pw, "index.html")
        if os.path.exists(p):
            pages.append(p)
        for tier in ("foundation", "higher"):
            p = os.path.join(OUT, pw, tier, "index.html")
            if os.path.exists(p):
                pages.append(p)
            for subj in ("physics", "chemistry", "biology"):
                d = os.path.join(OUT, pw, tier, subj)
                if not os.path.isdir(d):
                    continue
                p = os.path.join(d, "index.html")
                if os.path.exists(p):
                    pages.append(p)
                for f in sorted(os.listdir(d)):
                    if f.endswith(".html") and f != "index.html":
                        pages.append(os.path.join(d, f))
    return pages


# ══════════════════════════════════════════════════════════════════════════
#  The corpus, parsed out of Design's own file
# ══════════════════════════════════════════════════════════════════════════

def load_delivery():
    if not os.path.exists(DELIVERY):
        raise SystemExit(
            "ks4_chrome_tells.py: the vendored delivery is missing —\n  %s\n"
            "  This gate DERIVES what it bans from that file. Without it there\n"
            "  is no corpus, and a gate with no corpus passes everything, which\n"
            "  is worse than no gate. Restore it from the delivery folder."
            % rel(DELIVERY))
    return open(DELIVERY, encoding="utf-8").read()


# ── CSS is not copy ───────────────────────────────────────────────────────
#
# The first run of this gate failed on all 118 pages for `100%`, scraped out
# of Design's `width:100%` and matched against the chat modal's identical
# `width:100%`. A CSS length is not an invented statistic, and a gate that
# cries wolf on every page is a gate somebody switches off.
#
# So both the DERIVE side and the CHECK side read the same reduced view:
# style attributes and <style> blocks removed, everything else — including
# Design's <script type="text/x-dc"> logic, which is where her invented
# `done:` counts and state strings live — kept. Inline JS on a built page is
# deliberately still read: a hardcoded name hiding in a script is precisely
# what this is for.
_STYLE_BLOCK = re.compile(r"<style\b[^>]*>.*?</style>", re.S | re.I)
_STYLE_ATTR = re.compile(r'\sstyle="[^"]*"', re.I)


def without_css(html):
    return _STYLE_ATTR.sub(" ", _STYLE_BLOCK.sub(" ", html))


def derive(src):
    """Everything mechanical: tokens, numbers, handles."""
    src = without_css(src)
    tokens = sorted(set(re.findall(r"\{\{[^}]*\}\}", src)))

    # Percentages and fractions Design drew. None of them can legitimately
    # appear on a chrome page: no percentage and no x-of-y is server-
    # rendered anywhere in this run, because there is no KS4 progress model
    # and the two live leaderboard surfaces fill their numbers from the API
    # at runtime, after this file has read the bytes.
    pcts = sorted(set(re.findall(r"\b\d{1,3}%", src)))
    fracs = sorted(set(re.findall(r"\b\d+ ?/ ?\d+\b", src)))
    of_n = sorted(set(re.findall(r"\b\d+ of \d+\b", src)))
    ordinals = sorted(set(re.findall(r"\b\d+(?:st|nd|rd|th) of \d+\b", src)))

    # Design's invented students. Real handles come from the SAME generator
    # vocabulary (shared/username-generator.js), so a shape match would fire
    # on real students — these are pinned exactly, the way leaderboard_tells
    # pins its sixty-one.
    handles = sorted(set(re.findall(r"\b[A-Z][a-z]{2,}[A-Z][a-z]{2,}\d{1,3}\b", src)))

    return dict(tokens=tokens, pcts=pcts, fracs=fracs, of_n=of_n,
                ordinals=ordinals, handles=handles)


# Design's drawn sample PROSE. A regex cannot pick a sentence out of a
# sentence, so these are named — and every one is asserted present in the
# delivery below, which is what stops the list rotting into decoration.
SAMPLE_PROSE = [
    ("Energy transfers",              "the invented name of 'this week's challenge'"),
    ("closes Sunday",                 "wrong as well as invented — the week turns "
                                      "over Friday 10:15 UK (server getWeekStart)"),
    ("Beat it and you move up",       "an invented consequence of an invented rank"),
    ("Jump back in",                  "the resume card, which needs a progress model "
                                      "that does not exist"),
    ("Last opened:",                  "the same, on the science picker"),
    ("Half finished",                 "a per-subtopic progress state"),
    ("Not started",                   "a per-subtopic progress state"),
    ("You are here",                  "the KS3 year-picker badge — KS3 is out of "
                                      "scope entirely and none of it may leak"),
    ("Autumn 2",                      "the invented KS3 half-term"),
    ("Follow the chain",              "Design's placeholder where a KS3 unit count "
                                      "belonged"),
    ("Your tier so far",              "the dropped progress card's heading"),
    ("Your progress here",            "the same, on the topic page"),
    ("Your best",                     "an authenticated per-student score"),
    ("Your rank",                     "an authenticated per-student position"),
]

# Design's directive vocabulary. Each is specific enough that a single
# occurrence in built HTML means the delivery was pasted rather than ported.
DIRECTIVES = [
    ("<sc-if",             "Design's conditional element"),
    ("<sc-for",            "Design's repeater element"),
    ("<x-import",          "Design's component import"),
    ("<x-dc",              "the design-component root"),
    ("style-hover=",       "Design's hover attribute — not a real CSS hook"),
    ("data-screen-label=", "the click-through's screen marker"),
    ("hint-placeholder",   "the editor's placeholder hint"),
    ("hint-size=",         "the editor's size hint"),
    ("data-comment-anchor=", "an editor comment anchor"),
    ("data-dc-script",     "the design-component logic block"),
    ("onClick=",           "capital C — a React prop, inert in real HTML"),
    ("DCLogic",            "Design's component base class"),
    ("renderVals",         "Design's binding method"),
]


# ══════════════════════════════════════════════════════════════════════════
#  Checks
# ══════════════════════════════════════════════════════════════════════════

def check_prose_still_in_delivery(src):
    for phrase, why in SAMPLE_PROSE:
        if phrase not in src:
            fail("SAMPLE_PROSE names %r (%s) but it is NOT in the vendored "
                 "delivery any more. Either Design's file changed or the "
                 "phrase was mistyped — a named phrase that matches nothing "
                 "is a check that has quietly stopped watching."
                 % (phrase, why))


def check_pages(pages, corpus):
    for path in pages:
        raw = open(path, encoding="utf-8").read()
        html = without_css(raw)

        for tok in corpus["tokens"]:
            if tok in html:
                fail("%s ships Design's template token %s" % (rel(path), tok))
        # Bare braces catch a token this run invented that Design never did.
        # Checked against the RAW page: an unsubstituted binding inside a
        # style attribute (`background:{{ subjectHue }}` is one Design drew)
        # is every bit as broken as one in the copy.
        for brace in ("{{", "}}"):
            if brace in raw:
                fail("%s ships a bare %r — an unsubstituted binding"
                     % (rel(path), brace))

        for needle, why in DIRECTIVES:
            if needle in raw:
                fail("%s ships Design's directive %r (%s)" % (rel(path), needle, why))

        for group in ("pcts", "fracs", "of_n", "ordinals"):
            for n in corpus[group]:
                if n in html:
                    fail("%s ships the invented value %r, read out of the "
                         "delivery. No number of this shape is server-rendered "
                         "on a chrome page." % (rel(path), n))

        for h in corpus["handles"]:
            if h in html:
                fail("%s ships %r — a student Design invented" % (rel(path), h))

        for phrase, why in SAMPLE_PROSE:
            if phrase in html:
                fail("%s ships Design's sample copy %r (%s)" % (rel(path), phrase, why))


def check_destinations(pages):
    """Every internal href resolves to something the build actually wrote.

    The delivery's controls all pointed at "#". This is the check that says
    they do not any more — and it resolves against the BUILT TREE rather
    than the repo root, because the built tree is what Cloudflare serves."""
    href_re = re.compile(r'href="([^"]+)"')
    # The search control is an href="#" with an onclick, exactly as the live
    # nav has always had it: it is a button that degrades to nothing, not a
    # link that goes nowhere. Allowed by its full shape, not by "#" alone.
    search_control = 'href="#" class="nav-icon-link" title="Search topics"'

    for path in pages:
        html = open(path, encoding="utf-8").read()
        for href in href_re.findall(html):
            if href.startswith(("http://", "https://", "mailto:", "data:")):
                continue
            if href.startswith("#"):
                if search_control in html and href == "#":
                    continue
                fail("%s has a fragment-only href %r — a control that goes "
                     "nowhere" % (rel(path), href))
                continue
            target = href.split("?")[0].split("#")[0]
            if not target.startswith("/"):
                fail("%s has a relative href %r — every route on these pages "
                     "is absolute" % (rel(path), href))
                continue
            dest = os.path.join(OUT, target.lstrip("/"))
            if os.path.isdir(dest):
                dest = os.path.join(dest, "index.html")
            if not os.path.exists(dest):
                fail("%s links %r and the build wrote no such file (%s)"
                     % (rel(path), href, rel(dest)))


def check_walls(pages):
    """The scope wall, asserted rather than remembered.

    A chrome page must carry `data-chrome="ks4"` and link the chrome
    stylesheet; nothing else in the built tree may do either. That is what
    keeps ~865 lesson pages and the whole KS3 estate out of this run."""
    chrome = set(pages)
    for page in pages:
        html = open(page, encoding="utf-8").read()
        if 'data-chrome="ks4"' not in html:
            fail("%s is a chrome page but does not set data-chrome=\"ks4\" — "
                 "ks4-chrome.css cannot reach it" % rel(page))
        if "/shared/ks4-chrome.css" not in html:
            fail("%s is a chrome page but does not link ks4-chrome.css" % rel(page))

    strays = []
    for root, subdirs, files in os.walk(OUT):
        if os.path.abspath(root) == os.path.abspath(OUT):
            # ks3/ and 3d/ belong to other generators; this run proves it
            # never touched them, and walking them here would only ever
            # produce a false positive about somebody else's tree.
            for d in ("ks3", "3d"):
                if d in subdirs:
                    subdirs.remove(d)
        for f in files:
            if not f.endswith(".html"):
                continue
            p = os.path.join(root, f)
            if p in chrome:
                continue
            html = open(p, encoding="utf-8", errors="replace").read()
            if 'data-chrome="ks4"' in html or "/shared/ks4-chrome.css" in html:
                strays.append(rel(p))
    for s in strays:
        fail("%s is NOT a chrome page but wears the chrome — MRB-301's scope "
             "wall says only the seven chrome makers may" % s)


# ══════════════════════════════════════════════════════════════════════════

def main():
    if not os.path.isdir(OUT):
        raise SystemExit(
            "ks4_chrome_tells.py: %s does not exist — run build_all.py first."
            % rel(OUT))

    src = load_delivery()
    corpus = derive(src)
    pages = chrome_pages()

    if len(pages) < 100:
        raise SystemExit(
            "ks4_chrome_tells.py: only %d chrome pages found under %s.\n"
            "  The build writes 116 (2 landings, 2 pathway, 4 tier, 12 subject\n"
            "  hubs, 98 topics). A gate measuring a fraction of the surface is\n"
            "  the 'too short a list' failure this file's docstring warns about."
            % (len(pages), rel(OUT)))

    check_prose_still_in_delivery(src)
    check_pages(pages, corpus)
    check_destinations(pages)
    check_walls(pages)

    print("ks4_chrome_tells — %d chrome pages" % len(pages))
    print("  corpus derived from %s:" % rel(DELIVERY))
    print("    %2d template tokens   %2d percentages   %2d fractions"
          % (len(corpus["tokens"]), len(corpus["pcts"]), len(corpus["fracs"])))
    print("    %2d 'n of n'          %2d ordinals      %2d invented handles %s"
          % (len(corpus["of_n"]), len(corpus["ordinals"]),
             len(corpus["handles"]), corpus["handles"]))
    print("    %2d directives        %2d named sample phrases (all present in "
          "the delivery)" % (len(DIRECTIVES), len(SAMPLE_PROSE)))

    if failures:
        print("\n❌ ks4_chrome_tells: %d failure(s)\n" % len(failures))
        for f in failures:
            print("   • %s" % f)
        return 1

    print("\n✅ ks4_chrome_tells: no sample value, token, directive or dead "
          "destination on any chrome page; nothing outside them wears the chrome.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
