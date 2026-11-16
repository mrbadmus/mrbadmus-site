# -*- coding: utf-8 -*-
"""ks3_fixtures — hidden classic KS3 pages that the checks read instead of real lessons.

Mide's ruling (14 Nov 2026): "our checks should not depend on real lessons. Every time a
unit goes lean we will hit this again. Build one small hidden fixture page for each classic
page type the checks need ... It must not be in navigation, the sitemap or search."

WHAT A FIXTURE IS

    ks3_fixtures/<source slug, underscores>.py   exports UNIT, SOURCE_SLUG, FROZEN_FROM, LESSON

`LESSON` is a FROZEN SNAPSHOT of one classic lesson exactly as `ks3_data.build_units()`
handed it to the generator on the commit named in FROZEN_FROM (Start here merged, no lean
record). It is a Python literal, written by `tools/freeze_ks3_fixtures.py`, and it is never
regenerated to make a check pass: a fixture is frozen so that a check reading it sees what
it saw the day it was moved here, and keeps seeing it after the real lesson goes lean.

`build_ks3.build_ks3()` renders each one with the same `lesson_page()` every lesson uses, at

    /ks3/_fixtures/fixture-<source slug>.html

under the slug `fixture-<source slug>`. That one renaming is what makes it safe:

  * the lean overlay is keyed by slug, so a lean record for `gas-pressure` never reaches
    `fixture-gas-pressure`, and the fixture stays classic;
  * every id the page can send is `<slug>#...` (shared/ks3.js, shared/mrbadmus.v2.js), so a
    save from a fixture is `fixture-gas-pressure#...` and can never land on a real pupil's
    question id;
  * the file name is the slug, so the activity-save drives' own "the id belongs to this
    page" rule (`question_id.split("#")[0] == page basename`) still holds.

WHERE A FIXTURE IS NOT

A fixture is not in `ks3_data`, so nothing that reads the curriculum sees it: navigation,
unit and year pages, next/previous, "Before this lesson", the lesson picker, the curriculum
tree, the scheme of work, Set work, both question banks and the ladder mirror, flashcards,
knowledge points, ID maps and the lesson-contract baseline. It carries
`<meta name="robots" content="noindex,nofollow">`, `_headers` sends `X-Robots-Tag` for the
whole folder, the sitemap is consumer pages only, and the site search index is a hand-kept
KS4 list. `audit()` proves the first of those on every build: a page anywhere in the KS3
tree that links to a fixture stops the build.

Run after a build:   python3 -m ks3_fixtures --check
"""
import copy
import importlib
import os
import pkgutil
import re

DIR = "_fixtures"                 # under the KS3 output root: ks3/_fixtures/
PREFIX = "fixture-"
ROBOTS = '<meta name="robots" content="noindex,nofollow"/>'
_VIEWPORT = '<meta name="viewport" content="width=device-width, initial-scale=1"/>'

_CACHE = None


def _modules():
    for m in sorted(x.name for x in pkgutil.iter_modules(__path__)):
        if m.startswith("_"):
            continue
        yield m, importlib.import_module("%s.%s" % (__name__, m))


def fixtures():
    """[{name, unit, source, slug, frozen_from, lesson}] in file order. `lesson` is a deep
    copy of the frozen record with its slug renamed; the module's own LESSON is untouched."""
    global _CACHE
    if _CACHE is None:
        out, seen = [], set()
        for m, mod in _modules():
            src = mod.SOURCE_SLUG
            if m != src.replace("-", "_"):
                raise ValueError("ks3_fixtures: %s.py freezes %r; the file must be named %s.py"
                                 % (m, src, src.replace("-", "_")))
            if mod.LESSON.get("slug") != src:
                raise ValueError("ks3_fixtures.%s: LESSON['slug'] is %r, SOURCE_SLUG %r"
                                 % (m, mod.LESSON.get("slug"), src))
            if mod.LESSON.get("lean"):
                raise ValueError("ks3_fixtures.%s: the frozen lesson carries a lean record; a "
                                 "fixture is a CLASSIC page" % m)
            if src in seen:
                raise ValueError("ks3_fixtures: two fixtures for %r" % src)
            seen.add(src)
            lesson = copy.deepcopy(mod.LESSON)
            lesson["slug"] = PREFIX + src
            out.append({"name": m, "unit": mod.UNIT, "source": src, "slug": PREFIX + src,
                        "frozen_from": mod.FROZEN_FROM, "lesson": lesson})
        _CACHE = out
    return _CACHE


def rel(source):
    """The fixture's path under the KS3 root, e.g. `_fixtures/fixture-gas-pressure.html`."""
    return "%s/%s%s.html" % (DIR, PREFIX, source)


def href(source):
    return "/ks3/" + rel(source)


def is_fixture_path(path):
    """True for any path inside the fixture folder, in any spelling the checks use
    (`ks3/_fixtures/...`, `/ks3/_fixtures/...`, `_fixtures/...`, an absolute file path)."""
    p = str(path).replace(os.sep, "/")
    return ("/%s/" % DIR) in ("/" + p)


def by_path(path):
    """The fixture a page path names, or None."""
    if not is_fixture_path(path):
        return None
    base = str(path).replace(os.sep, "/").rsplit("/", 1)[-1]
    for f in fixtures():
        if base == f["slug"] + ".html":
            return f
    return None


def render(units_by_code, registry, neighbours, lesson_page, canon):
    """[(path under the KS3 root, html)] — every fixture, through the real lesson_page().

    The unit is the source lesson's real unit (its trail, colour and tutor topic), and the
    endmatter's previous/next are the source lesson's own, so the page reads exactly as the
    source page did. Links go OUT to real pages; nothing links IN."""
    out = []
    for f in fixtures():
        unit = units_by_code[f["unit"]]
        nb = {f["slug"]: (neighbours or {}).get(f["source"], (None, None))}
        html = lesson_page(unit, f["lesson"], registry, units_by_code, nb)
        # lesson_page() names the page /ks3/<discipline>/<unit>/<slug>.html; a fixture lives
        # in the fixture folder, so its canonical and og:url name where it really is.
        wrong = canon("/ks3/%s/%s/%s.html" % (unit["discipline"], unit["slug"], f["slug"]))
        right = canon(href(f["source"]))
        if wrong not in html:
            raise ValueError("ks3_fixtures: %s has no canonical %s to repoint" % (f["slug"], wrong))
        html = html.replace(wrong, right)
        if html.count(_VIEWPORT) != 1:
            raise ValueError("ks3_fixtures: %s: expected one viewport tag to sit the robots tag "
                             "after" % f["slug"])
        html = html.replace(_VIEWPORT, _VIEWPORT + "\n" + ROBOTS, 1)
        out.append((rel(f["source"]), html))
    return out


_FIXTURE_LINK = re.compile(r"/ks3/%s/|[\"'(]%s/" % (re.escape(DIR), re.escape(DIR)))


def audit(site_root, ks3_dir="ks3", scan_root=None):
    """Problems, as strings. Empty means every fixture is hidden and namespaced.

    `site_root` is the served root (mrbadmus_site/). Read from the BUILT pages, because the
    question is what a browser and a crawler find, not what the records meant. The "linked
    from nowhere" sweep reads every page under `scan_root` (default: the whole site; the
    KS3 build passes its own tree, which is the only tree it writes)."""
    problems = []
    ks3_root = os.path.join(site_root, ks3_dir)
    want = {rel(f["source"]): f for f in fixtures()}
    for r, f in sorted(want.items()):
        p = os.path.join(ks3_root, r)
        if not os.path.isfile(p):
            problems.append("fixture page missing: /%s/%s (run the KS3 build)" % (ks3_dir, r))
            continue
        html = open(p, encoding="utf-8").read()
        if html.count(ROBOTS) != 1:
            problems.append("/%s/%s does not carry exactly one %s" % (ks3_dir, r, ROBOTS))
        if 'data-ks3-lesson="%s"' % f["slug"] not in html:
            problems.append("/%s/%s: body is not stamped data-ks3-lesson=%r" % (ks3_dir, r, f["slug"]))
        for m in re.finditer(r'data-lesson="([^"]*)"', html):
            if m.group(1) != f["slug"]:
                problems.append("/%s/%s: a ladder is keyed %r, not the fixture slug %r — its "
                                "answers would save under a real lesson's ids"
                                % (ks3_dir, r, m.group(1), f["slug"]))
        if 'data-ks3-lesson="%s"' % f["source"] in html or 'data-lesson="%s"' % f["source"] in html:
            problems.append("/%s/%s carries the REAL slug %r as a save key" % (ks3_dir, r, f["source"]))
    extra = []
    fdir = os.path.join(ks3_root, DIR)
    if os.path.isdir(fdir):
        for name in sorted(os.listdir(fdir)):
            if "%s/%s" % (DIR, name) not in want:
                extra.append(name)
    for name in extra:
        problems.append("/%s/%s/%s is in the fixture folder and is not a registered fixture"
                        % (ks3_dir, DIR, name))
    # Nothing links IN: no page outside the folder names it, anywhere on the site.
    for dp, _dn, fn in os.walk(scan_root or site_root):
        for name in fn:
            if not name.endswith((".html", ".js", ".json", ".xml", ".txt")):
                continue
            p = os.path.join(dp, name)
            if is_fixture_path(os.path.relpath(p, site_root)):
                continue
            try:
                txt = open(p, encoding="utf-8").read()
            except (UnicodeDecodeError, OSError):
                continue
            if _FIXTURE_LINK.search(txt):
                problems.append("%s names the hidden fixture folder (/ks3/%s/): fixtures are "
                                "linked from nowhere" % (os.path.relpath(p, site_root), DIR))
    return problems


def main(argv=None):
    import argparse
    ap = argparse.ArgumentParser(prog="python3 -m ks3_fixtures",
                                 description="Prove the hidden KS3 fixture pages are built, "
                                             "noindex, namespaced and linked from nowhere.")
    ap.add_argument("--check", action="store_true", help="audit the built site (the default)")
    ap.add_argument("--site", default="mrbadmus_site", help="the served root to audit")
    ap.add_argument("--list", action="store_true", help="list the fixtures and exit")
    a = ap.parse_args(argv)
    if a.list:
        for f in fixtures():
            print("%-4s %-36s /ks3/%s  (frozen from %s)"
                  % (f["unit"], f["source"], rel(f["source"]), f["frozen_from"]))
        return 0
    problems = audit(a.site)
    for p in problems:
        print("  FAIL  " + p)
    print("ks3_fixtures: %d fixture page(s), %s"
          % (len(fixtures()), "%d problem(s)" % len(problems) if problems else "all hidden and namespaced"))
    return 1 if problems else 0
