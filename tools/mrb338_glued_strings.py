#!/usr/bin/env python3
"""Implicitly-concatenated string literals that lost the space between them.

⊕ 12 Sep 2026. A repair lane wrapped new option text across source lines:

    "text": "…more air than it "
            "canever hold"          # ← the space belongs on ONE side only

Python's implicit concatenation adds NO whitespace, so the text reaching the
child read `canever`, `airfits`, `newtissue`.

⚠️ **EVERY GATE WENT GREEN on that corrupted text.** leafcheck ✅,
shape_tell 0.0%, verify_answer_lengths OK — because a missing space SHORTENS a
string without changing its shape, its option count, its key or its id. Only
reading the rendered option caught it, and only because the lane happened to
look.

This finds it at source level, which is where it is unambiguous: two adjacent
string literals where the left does not end in a space or an opening bracket
and the right does not begin with one, and the join lands mid-word.
"""
import ast, os, sys

def glued(path):
    try:
        tree = ast.parse(open(path, encoding="utf-8").read())
    except SyntaxError as e:
        return [("%s does not parse: %s" % (path, e.msg), 0)]
    out = []
    for node in ast.walk(tree):
        if not isinstance(node, ast.JoinedStr) and isinstance(node, ast.Constant):
            continue
    # implicit concatenation is folded by the parser, so compare source segments
    src = open(path, encoding="utf-8").read().split("\n")
    import re
    STR = re.compile(r'"((?:[^"\\]|\\.)*)"\s*$')
    NXT = re.compile(r'^\s*"((?:[^"\\]|\\.)*)"')
    for i in range(len(src) - 1):
        a, b = STR.search(src[i]), NXT.search(src[i + 1])
        if not (a and b):
            continue
        left, right = a.group(1), b.group(1)
        if not left or not right:
            continue
        # a join is safe if either side carries the separator
        if left.endswith((" ", "(", "[", "-", "—", "/", "\\n")) or right.startswith((" ", ")", ",", ".", ";", ":")):
            continue
        # mid-word join: letter meets letter
        if left[-1].isalnum() and right[0].isalnum():
            out.append(("%s:%d  …%s|%s…" % (path, i + 1, left[-18:], right[:18]), 1))
    return out

def main():
    hits = []
    for p in sys.argv[1:]:
        if os.path.exists(p):
            hits += glued(p)
    for h, _ in hits:
        print("  ⚠️  " + h)
    print("\nglued-strings: %d suspect join(s) across %d file(s)"
          % (len(hits), len(sys.argv) - 1))
    print("⚠️  Reported, never failed — a deliberate mid-word join is legal.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
