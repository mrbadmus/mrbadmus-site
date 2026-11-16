#!/usr/bin/env python3
"""freeze_ks3_fixtures.py — write a frozen classic snapshot of a KS3 lesson into ks3_fixtures/.

    python3 tools/freeze_ks3_fixtures.py gas-pressure moments       # freeze two lessons
    python3 tools/freeze_ks3_fixtures.py --check                     # every fixture still loads,
                                                                      # round-trips and is classic

A fixture is the hidden classic page a check reads instead of a real lesson (see
ks3_fixtures/__init__.py). Its LESSON is the lesson exactly as ks3_data.build_units() hands
it to the generator — the authored record with its Start here merged — and WITHOUT any lean
record, so it is classic even if the real lesson has already gone lean.

It REFUSES to overwrite a fixture that exists. Frozen means frozen: a fixture is rewritten
only on purpose (`--refreeze`), never to make a failing check pass, because a check that is
green on a refrozen fixture has stopped testing what it tested.
"""
import argparse
import ast
import os
import pprint
import subprocess
import sys

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, HERE)
os.chdir(HERE)

OUT = os.path.join(HERE, "ks3_fixtures")


def classic_lesson(slug):
    """(unit code, the classic lesson as build_units() merges it, minus any lean record)."""
    import ks3_data
    from ks3_data import start_here, structure
    authored = ks3_data._authored_modules()
    for code, unit in authored.items():
        for lesson in unit.get("lessons", []):
            if lesson["slug"] != slug:
                continue
            out = start_here.apply(dict(lesson))
            out["authored"] = True
            slot = next(s for s in structure.unit_index()[code]["lesson_slots"] if s["slug"] == slug)
            out.setdefault("family", slot["family"])
            # When there is no lean record the generator's own merge must agree, byte for byte.
            from ks3_data import lean as lean_records
            if slug not in lean_records.records():
                built = next(l for u in ks3_data.build_units() if u["code"] == code
                             for l in u["lessons"] if l["slug"] == slug)
                if built != out:
                    raise SystemExit("freeze: %s differs from build_units()'s own merge" % slug)
            return code, out
    raise SystemExit("freeze: no authored KS3 lesson has the slug %r" % slug)


def head_sha():
    r = subprocess.run(["git", "-C", HERE, "rev-parse", "--short=10", "HEAD"], capture_output=True, text=True)
    return r.stdout.strip() or "unknown"


def write(slug, refreeze=False):
    path = os.path.join(OUT, slug.replace("-", "_") + ".py")
    if os.path.exists(path) and not refreeze:
        raise SystemExit("freeze: %s exists. Fixtures are frozen; pass --refreeze only on purpose."
                         % os.path.relpath(path, HERE))
    code, lesson = classic_lesson(slug)
    body = pprint.pformat(lesson, indent=1, width=100, sort_dicts=False)
    if ast.literal_eval(body) != lesson:
        raise SystemExit("freeze: %s does not round-trip as a Python literal" % slug)
    sha = head_sha()
    text = ('# -*- coding: utf-8 -*-\n'
            '"""Frozen classic snapshot of KS3 %s `%s` (ks3_fixtures/__init__.py).\n\n'
            'Written by tools/freeze_ks3_fixtures.py from %s. Do not edit, and do not refreeze to\n'
            'make a check pass: the checks that read this page assert what it held on that commit.\n'
            '"""\n\n'
            'UNIT = %r\n'
            'SOURCE_SLUG = %r\n'
            'FROZEN_FROM = %r\n\n'
            'LESSON = %s\n') % (code, slug, sha, code, slug, sha, body)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(text)
    print("froze %-4s %-36s -> %s (%d bytes)" % (code, slug, os.path.relpath(path, HERE), len(text)))


def check():
    import ks3_fixtures as F
    bad = 0
    for f in F.fixtures():
        src = open(os.path.join(OUT, f["name"] + ".py"), encoding="utf-8").read()
        tree = ast.parse(src)
        lit = [n.value for n in tree.body if isinstance(n, ast.Assign)
               and any(getattr(t, "id", None) == "LESSON" for t in n.targets)]
        try:
            ast.literal_eval(lit[0])
        except (ValueError, IndexError):
            print("  FAIL  %s: LESSON is not a plain literal" % f["name"])
            bad += 1
            continue
        print("  ok    %-4s %-36s %s" % (f["unit"], f["source"], F.rel(f["source"])))
    print("%d fixture(s), %d problem(s)" % (len(F.fixtures()), bad))
    return 1 if bad else 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("slugs", nargs="*")
    ap.add_argument("--refreeze", action="store_true")
    ap.add_argument("--check", action="store_true")
    a = ap.parse_args()
    if a.check or not a.slugs:
        return check()
    for s in a.slugs:
        write(s, a.refreeze)
    return 0


if __name__ == "__main__":
    sys.exit(main())
