#!/usr/bin/env python3
"""List every token `formulae()` subscripted in the built key stage.

⊕ MRB-302. The subscript pass converts a token only when every symbol in it
is a real element AND there are two or more element groups (or the token is
one of a short list of genuinely subscripted single-element species). Those
rules kill the unit codes — C1, C6, P11, B2 — but they cannot kill a token
that happens to spell two real symbols and a number. `KS3` is exactly that:
potassium, sulfur, three, and it shipped as KS₃ on the first build.

It was caught by MEASURING, not by reasoning, and the next collision will be
caught the same way. Run this after adding content that mentions a formula,
and read the list: every line should be a chemical formula you recognise.
Anything that is not one goes in `_NOT_FORMULAE` in `ks3_art/kit.py`.

    python3 tools/audit_formula_subscripts.py

Two entries look wrong and are not: MgO2 and Na1Cl1 are the deliberately
WRONG formulae c4-05 and c2-05 ask a student to criticise.
"""
import collections
import glob
import io
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONVERTED = re.compile(
    r"[A-Z][A-Za-z]*<sub>\d+</sub>(?:[A-Z][a-z]?(?:<sub>\d+</sub>)?)*")


def main():
    os.chdir(ROOT)
    if not glob.glob("ks3/**/*.html", recursive=True):
        print("no built key stage — run python3 build_all.py first")
        return 2
    seen = collections.Counter()
    where = collections.defaultdict(set)
    for path in glob.glob("ks3/**/*.html", recursive=True):
        text = io.open(path, encoding="utf-8", errors="ignore").read()
        for m in CONVERTED.finditer(text):
            flat = m.group(0).replace("<sub>", "").replace("</sub>", "")
            seen[flat] += 1
            where[flat].add(path)
    if not seen:
        print("nothing subscripted — that is itself worth checking")
        return 1
    print("%d distinct token(s) subscripted in the built key stage:\n"
          % len(seen))
    for tok in sorted(seen):
        files = sorted(where[tok])
        print("  %5d  %-10s  %s%s"
              % (seen[tok], tok, files[0],
                 "  (+%d more)" % (len(files) - 1) if len(files) > 1 else ""))
    print("\nEvery line above should be a chemical formula. If one is not, add"
          "\nit to _NOT_FORMULAE in ks3_art/kit.py and rebuild.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
