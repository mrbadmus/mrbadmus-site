#!/usr/bin/env python3
"""verify_consumer_launch.py — the committed consumer launch state matches
launch.json. Fast gate, stdlib only, no browser.

⊕ 1 Oct 2026. The launch decision is COMMITTED CONFIG (`launch.json`,
`launch_config.py`) — see those files' docstrings for why. This gate is the
thing that would have caught `64a0cb303`: a build committed to `main` with
`mrbadmus_site/parents/*.html` carrying a `noindex` tag again, no
`sitemap.xml`, no `robots.txt`, no consumer 404/error pages, while
`launch.json` (and `shared/config.js`'s PROD block) still said the consumer
product is launched. That is not a style nit — a crawler reading those bytes
is told the opposite of what the business decided, and nothing before this
gate noticed.

What it checks, against the COMMITTED deploy tree (`mrbadmus_site/`, as it
sits in git — not a fresh build):

  a. existence (or, if un-launched, absence) of sitemap.xml, robots.txt,
     parents/404.html, parents/error.html, consumer/404.html,
     consumer/error.html, parents/social-card.png; sitemap.xml parses as
     XML and lists https://mrbadmus.com/parents/; robots.txt references the
     sitemap.
  b. every `generate_site_v5._PUBLIC_META` entry's deploy copy carries (or
     lacks) the static noindex tag exactly as `strip_noindex` says, and
     carries (or lacks) `rel="canonical"` + `og:title` to match.
  c. `shared/config.js`'s PROD block `CONSUMER_SIGNUP_ENABLED` agrees with
     the committed flag, in both the repo copy and the deploy copy.
  d. `launch_config.consumer_signup_enabled()`, with the environment
     override absent, returns the committed value — i.e. a plain
     `python3 build_all.py` launches (or doesn't) exactly as committed.

Its own decision of "committed ON or OFF" uses `launch_config.committed()`
with the environment variable deliberately ignored (checks d above is the
one place the environment matters at all) — this gate is asking "does the
committed TREE match the committed DECISION", not "does today's shell
environment happen to agree".

Run it:

    python3 verify_consumer_launch.py              # checks THIS repo
    python3 verify_consumer_launch.py --self-test   # proves the checks work
"""

import argparse
import json
import os
import re
import shutil
import sys
import tempfile
import xml.etree.ElementTree as ET

HERE = os.path.dirname(os.path.abspath(__file__))

# generate_site_v5 is imported for its `_PUBLIC_META` list ONLY. Importing it
# does no file I/O and triggers no build — it just defines functions and
# constants at module scope (confirmed: ~20ms, no writes). `launch_config`'s
# own import is side-effect-free for the same reason (it only reads
# launch.json lazily, inside its functions).
sys.path.insert(0, HERE)
import generate_site_v5 as gsv5  # noqa: E402
import launch_config  # noqa: E402

SITE_ORIGIN = "https://mrbadmus.com"

_ROBOTS_RE = re.compile(r'<meta\s+name="robots"\s+content="noindex"\s*/?>')
_CANONICAL_RE = re.compile(r'<link\s+rel="canonical"')
_OG_TITLE_RE = re.compile(r'<meta\s+property="og:title"')

_LAUNCH_FILES = [
    "mrbadmus_site/sitemap.xml",
    "mrbadmus_site/robots.txt",
    "mrbadmus_site/parents/404.html",
    "mrbadmus_site/parents/error.html",
    "mrbadmus_site/consumer/404.html",
    "mrbadmus_site/consumer/error.html",
    "mrbadmus_site/parents/social-card.png",
]

UNLAUNCHED_HINT = (
    "the committed build is un-launched while launch.json says ON — "
    "rebuild with python3 build_all.py (no env override) and commit "
    "mrbadmus_site/")
LAUNCHED_WHEN_OFF_HINT = (
    "the committed build is launched while launch.json says OFF — "
    "rebuild with python3 build_all.py (no env override) and commit "
    "mrbadmus_site/")


def _result(ok, msg):
    print(("  ✅ " if ok else "  ❌ ") + msg)
    return ok


# ── check (a) — the launch-only artefacts ───────────────────────────────

def check_existence(root, committed_on):
    results = []
    for rel in _LAUNCH_FILES:
        fp = os.path.join(root, rel)
        exists = os.path.exists(fp)
        if committed_on:
            results.append(_result(exists, "exists: %s" % rel))
        else:
            results.append(_result(not exists, "absent (un-launched): %s" % rel))

    if not committed_on:
        return results

    sitemap_fp = os.path.join(root, "mrbadmus_site/sitemap.xml")
    if os.path.exists(sitemap_fp):
        try:
            tree = ET.parse(sitemap_fp)
            ns = "{http://www.sitemaps.org/schemas/sitemap/0.9}"
            locs = [el.text for el in tree.getroot().findall("%surl/%sloc" % (ns, ns))]
            results.append(_result(
                any(loc == SITE_ORIGIN + "/parents/" for loc in locs),
                "sitemap.xml lists %s/parents/" % SITE_ORIGIN))
        except ET.ParseError as exc:
            results.append(_result(False, "sitemap.xml parses as XML (%s)" % exc))
    else:
        results.append(_result(False, "sitemap.xml parses as XML (file missing)"))

    robots_fp = os.path.join(root, "mrbadmus_site/robots.txt")
    if os.path.exists(robots_fp):
        with open(robots_fp, encoding="utf-8") as fh:
            robots_txt = fh.read()
        results.append(_result(
            "Sitemap:" in robots_txt and "sitemap.xml" in robots_txt,
            "robots.txt references the sitemap"))
    else:
        results.append(_result(False, "robots.txt references the sitemap (file missing)"))

    return results


# ── check (b) — the per-page head tags ──────────────────────────────────

def check_public_meta(root, committed_on):
    results = []
    for entry in gsv5._PUBLIC_META:
        fp = os.path.join(root, "mrbadmus_site", entry["path"].lstrip("/"))
        if not os.path.exists(fp):
            results.append(_result(False, "%s exists" % entry["path"]))
            continue
        with open(fp, encoding="utf-8") as fh:
            html = fh.read()

        has_noindex = bool(_ROBOTS_RE.search(html))
        has_canonical = bool(_CANONICAL_RE.search(html))
        has_og_title = bool(_OG_TITLE_RE.search(html))

        if committed_on:
            if entry["strip_noindex"]:
                results.append(_result(not has_noindex,
                    "%s: noindex stripped" % entry["path"]))
                results.append(_result(has_canonical,
                    "%s: carries rel=canonical" % entry["path"]))
                results.append(_result(has_og_title,
                    "%s: carries og:title" % entry["path"]))
            else:
                results.append(_result(has_noindex,
                    "%s: keeps its noindex (ruled)" % entry["path"]))
                # Still gets a canonical + card even though it stays noindex
                # — see _PUBLIC_META's own docstring (the footer links it).
                results.append(_result(has_canonical,
                    "%s: carries rel=canonical" % entry["path"]))
                results.append(_result(has_og_title,
                    "%s: carries og:title" % entry["path"]))
        else:
            # Inverse: publish_consumer_launch() never ran, so nothing was
            # stripped and no launch-only tags were added, on ANY entry —
            # strip_noindex describes what a LAUNCHED build does, not the
            # un-launched baseline.
            results.append(_result(has_noindex,
                "%s: noindex NOT stripped (un-launched)" % entry["path"]))
            results.append(_result(not has_canonical,
                "%s: no canonical added (un-launched)" % entry["path"]))
            results.append(_result(not has_og_title,
                "%s: no og:title added (un-launched)" % entry["path"]))

    return results


# ── check (c) — shared/config.js's PROD block ───────────────────────────

_PROD_BLOCK_RE = re.compile(r'const\s+PROD\s*=\s*\{(.*?)\n\s*\};', re.DOTALL)
_FLAG_RE = re.compile(r'CONSUMER_SIGNUP_ENABLED:\s*(true|false)')


def _prod_flag(path):
    if not os.path.exists(path):
        return None, "file missing: %s" % path
    with open(path, encoding="utf-8") as fh:
        js = fh.read()
    block = _PROD_BLOCK_RE.search(js)
    if not block:
        return None, "no `const PROD = {...}` block found in %s" % path
    m = _FLAG_RE.search(block.group(1))
    if not m:
        return None, "no CONSUMER_SIGNUP_ENABLED in PROD block of %s" % path
    return (m.group(1) == "true"), None


def check_config_js(root, committed_on):
    results = []
    for rel in ("shared/config.js", "mrbadmus_site/shared/config.js"):
        fp = os.path.join(root, rel)
        flag, err = _prod_flag(fp)
        if err:
            results.append(_result(False, "%s: %s" % (rel, err)))
            continue
        results.append(_result(
            flag == committed_on,
            "%s: PROD.CONSUMER_SIGNUP_ENABLED is %s (committed says %s)"
            % (rel, flag, committed_on)))
    return results


# ── check (d) — launch_config agrees with itself, env absent ───────────

def check_plain_build_launches():
    saved = os.environ.pop("CONSUMER_SIGNUP_ENABLED", None)
    try:
        committed_value = launch_config.committed()
        effective = launch_config.consumer_signup_enabled()
        ok = effective == committed_value
        return [_result(ok,
            "a plain build (no env override) launches exactly as committed "
            "(committed=%s, effective=%s)" % (committed_value, effective))]
    finally:
        if saved is not None:
            os.environ["CONSUMER_SIGNUP_ENABLED"] = saved


# ── running everything against one root ─────────────────────────────────

def run_all(root, committed_on, label):
    print("\n── %s (committed %s) ──" % (label, "ON" if committed_on else "OFF"))
    results = []
    print(" [a] launch-only artefacts")
    results += check_existence(root, committed_on)
    print(" [b] per-page head tags")
    results += check_public_meta(root, committed_on)
    print(" [c] shared/config.js PROD block")
    results += check_config_js(root, committed_on)
    print(" [d] launch_config, env absent")
    results += check_plain_build_launches()

    passed = sum(1 for r in results if r)
    total = len(results)
    print("\n  summary: %d/%d checks passed" % (passed, total))

    if not all(results):
        hint = UNLAUNCHED_HINT if committed_on else LAUNCHED_WHEN_OFF_HINT
        print("  ⚠️  %s" % hint)

    return all(results)


# ── --self-test: prove the checks actually catch a corrupted tree ───────

def _write_head_page(fp, *, noindex, canonical, og_title):
    tags = []
    if noindex:
        tags.append('<meta name="robots" content="noindex"/>')
    if canonical:
        tags.append('<link rel="canonical" href="https://mrbadmus.com/parents/"/>')
    if og_title:
        tags.append('<meta property="og:title" content="Test"/>')
    html = "<!DOCTYPE html><html><head>%s</head><body></body></html>" % "".join(tags)
    os.makedirs(os.path.dirname(fp), exist_ok=True)
    with open(fp, "w", encoding="utf-8") as fh:
        fh.write(html)


def _build_good_fixture(root, flag_value):
    """A synthetic, minimal tree that should PASS every check for a build
    committed to `flag_value` (True = launched). Hand-built rather than
    produced by actually running generate_site_v5.py — this script's job is
    to test the CHECKS, not to re-run the generator, and the self-test must
    not depend on (or trigger) a real build."""
    os.makedirs(os.path.join(root, "mrbadmus_site/parents"), exist_ok=True)
    os.makedirs(os.path.join(root, "mrbadmus_site/consumer"), exist_ok=True)
    os.makedirs(os.path.join(root, "shared"), exist_ok=True)
    os.makedirs(os.path.join(root, "mrbadmus_site/shared"), exist_ok=True)

    for entry in gsv5._PUBLIC_META:
        fp = os.path.join(root, "mrbadmus_site", entry["path"].lstrip("/"))
        if flag_value:
            _write_head_page(fp,
                noindex=not entry["strip_noindex"],
                canonical=True, og_title=True)
        else:
            _write_head_page(fp, noindex=True, canonical=False, og_title=False)

    if flag_value:
        with open(os.path.join(root, "mrbadmus_site/sitemap.xml"), "w", encoding="utf-8") as fh:
            fh.write(
                '<?xml version="1.0" encoding="UTF-8"?>\n'
                '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
                '  <url><loc>https://mrbadmus.com/parents/</loc></url>\n'
                '</urlset>\n')
        with open(os.path.join(root, "mrbadmus_site/robots.txt"), "w", encoding="utf-8") as fh:
            fh.write("User-agent: *\nSitemap: https://mrbadmus.com/sitemap.xml\n")
        for tree in ("parents", "consumer"):
            for name in ("404.html", "error.html"):
                fp = os.path.join(root, "mrbadmus_site", tree, name)
                with open(fp, "w", encoding="utf-8") as fh:
                    fh.write("<!DOCTYPE html><html><body>status page</body></html>")
        with open(os.path.join(root, "mrbadmus_site/parents/social-card.png"), "wb") as fh:
            fh.write(b"\x89PNG\r\n\x1a\nfake")

    flag_js = "true" if flag_value else "false"
    config_js = (
        "(function(){\n"
        "  const PROD = {\n"
        "    SUPABASE_URL: 'x',\n"
        "    CONSUMER_SIGNUP_ENABLED: %s,\n"
        "  };\n"
        "})();\n" % flag_js)
    for rel in ("shared/config.js", "mrbadmus_site/shared/config.js"):
        with open(os.path.join(root, rel), "w", encoding="utf-8") as fh:
            fh.write(config_js)


def self_test():
    print("── verify_consumer_launch.py --self-test ──")
    tmp = tempfile.mkdtemp(prefix="consumer-launch-selftest-")
    try:
        # 1. A good, launched fixture must pass every check.
        _build_good_fixture(tmp, True)
        print("\n1. good launched fixture — expect ALL checks to pass")
        good_ok = run_all(tmp, True, "self-test fixture (good, launched)")
        if not good_ok:
            print("\n❌ SELF-TEST FAILED: the good fixture did not pass its own "
                  "checks — the checks (or the fixture builder) are wrong.")
            return False

        # 2. Corrupt it: re-add a noindex to a strip_noindex page, and delete
        #    sitemap.xml. Both should now be caught.
        print("\n2. corrupting the fixture — noindex reinjected into "
              "parents/index.html, sitemap.xml deleted")
        index_fp = os.path.join(tmp, "mrbadmus_site/parents/index.html")
        with open(index_fp, encoding="utf-8") as fh:
            html = fh.read()
        html = html.replace("<head>", '<head><meta name="robots" content="noindex"/>', 1)
        with open(index_fp, "w", encoding="utf-8") as fh:
            fh.write(html)
        os.remove(os.path.join(tmp, "mrbadmus_site/sitemap.xml"))

        print("\n3. re-running the checks — expect the two corruptions to FAIL")
        corrupted_ok = run_all(tmp, True, "self-test fixture (corrupted)")

        if corrupted_ok:
            print("\n❌ SELF-TEST FAILED: corrupting the fixture did not make "
                  "any check fail — the checks are not catching the regression "
                  "they exist to catch.")
            return False

        print("\n✅ SELF-TEST PASSED: the good fixture passed cleanly, and "
              "the corrupted fixture (reinjected noindex + missing sitemap.xml) "
              "was caught.")
        return True
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", nargs="?", default=None,
                         help="repo root to check (default: this script's own directory)")
    parser.add_argument("--self-test", action="store_true",
                         help="prove the checks catch a corrupted tree, using a "
                              "synthetic fixture in a temp dir; ignores `root`")
    args = parser.parse_args()

    if args.self_test:
        return 0 if self_test() else 1

    root = args.root or HERE

    # This gate's own decision deliberately ignores any ambient environment
    # override — it is asking whether the COMMITTED tree matches the
    # COMMITTED decision, not whether today's shell happens to agree.
    saved = os.environ.pop("CONSUMER_SIGNUP_ENABLED", None)
    try:
        committed_on = launch_config.committed()
    finally:
        if saved is not None:
            os.environ["CONSUMER_SIGNUP_ENABLED"] = saved

    ok = run_all(root, committed_on, "committed tree")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
