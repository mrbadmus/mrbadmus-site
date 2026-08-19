#!/usr/bin/env python3
"""
ks3_prose_swap.py — apply the audit's prose replacements AT SOURCE, and prove it.

MRB-257 decision 6, which is the whole reason this file exists:

    "The 43 prose replacements are applied in the source records, never the
     built tree. Each string was verified once in the *served HTML* — but
     edits happen in `ks3_data/` records, where a string may be composed by
     the generator. Locate each in source; if not present verbatim, find the
     composing site; a string matching zero or 2+ times in the build output
     after the edit fails loudly."

So this is not a sed wrapper. It is a gate with an edit inside it. For every
swap it asserts, against the BUILT tree:

  before the edit   the old string appears EXACTLY ONCE on the named page
  after  the edit   the old string appears ZERO times
                    the new string appears EXACTLY ONCE
                    no OTHER page changed

The last one is the one that matters and the one a careless `sed -i` over
ks3_data/ gets wrong: a sentence authored once can be rendered on two pages,
and a swap that silently edits a second lesson is exactly the kind of thing
this whole audit exists to stop.

A swap whose old string is NOT in the source verbatim is not an error — the
generator composes some of these. Such a swap is reported as COMPOSED and
skipped, with the built-page evidence, so a human can find the composing site
and author the fix there. Guessing at a composing site is how you break a
lesson silently.

Usage
    python3 ks3_prose_swap.py --check          # report only, change nothing
    python3 ks3_prose_swap.py --apply          # apply the ones that are safe
    python3 ks3_prose_swap.py --apply --only 4.3
Exit codes: 0 all good · 1 a swap failed its own assertion · 2 harness error.
"""

import argparse
import ast
import hashlib
import html
import os
import re
import subprocess
import sys

REPO = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(REPO, "ks3_data")
BUILT = os.path.join(REPO, "mrbadmus_site", "ks3")

# ── the swap table ────────────────────────────────────────────────────────
# Filled from docs/ks3/audits/2026-08-18-ks3-biology.md, WS4.
# id     the audit's own finding number, so a failure names the finding
# page   built-tree path fragment, enough to identify one file uniquely
# old    the exact current string
# new    the exact replacement ("" means cut the sentence outright)
# The audit's "Left alone deliberately" list is binding and nothing on it
# appears here. Do not add to this table without a finding number.
SWAPS = []   # populated by load_swaps()


def load_swaps(path):
    """Read the swap table from a TSV sidecar so the table is data, not code.

    Kept out of this file deliberately: the strings are long, contain quotes
    and em-dashes, and a Python-literal table of them is a merge conflict
    waiting to happen. The sidecar is authored once from the audit and
    reviewed as prose.
    """
    swaps = []
    with open(path, encoding="utf-8") as fh:
        for n, line in enumerate(fh, 1):
            line = line.rstrip("\n")
            if not line.strip() or line.startswith("#"):
                continue
            parts = line.split("\t")
            if len(parts) != 4:
                sys.stderr.write(
                    "%s:%d — expected 4 tab-separated fields, got %d\n"
                    % (path, n, len(parts)))
                sys.exit(2)
            sid, page, old, new = parts
            swaps.append({"id": sid.strip(), "page": page.strip(),
                          "old": old, "new": new})
    return swaps


# ── built-tree helpers ────────────────────────────────────────────────────

def built_pages():
    out = {}
    for root, _dirs, files in os.walk(BUILT):
        for f in files:
            if f.endswith(".html"):
                p = os.path.join(root, f)
                out[os.path.relpath(p, BUILT)] = p
    return out


def resolve_page(frag, pages):
    hits = [rel for rel in pages if frag in rel]
    if len(hits) != 1:
        return None, hits
    return hits[0], hits


def visible_text(html_src):
    """Strip tags and unescape, so a swap is matched against what a student
    reads rather than against markup. A sentence split across a <strong> is
    still one sentence to a reader and must be to us."""
    s = re.sub(r"(?is)<(script|style)\b.*?</\1>", " ", html_src)
    s = re.sub(r"(?s)<[^>]+>", "", s)
    s = html.unescape(s)
    return re.sub(r"\s+", " ", s)


def snapshot():
    return {rel: hashlib.sha256(open(p, "rb").read()).hexdigest()
            for rel, p in built_pages().items()}


def build():
    r = subprocess.run([sys.executable, "build_ks3.py"], cwd=REPO,
                       capture_output=True, text=True)
    if r.returncode != 0:
        sys.stderr.write("build_ks3.py failed:\n%s\n%s\n" % (r.stdout[-4000:],
                                                             r.stderr[-4000:]))
        sys.exit(2)


# ── source-record helpers ─────────────────────────────────────────────────
#
# The records are Python, and the sentences we are editing are routinely split
# across ADJACENT STRING LITERALS:
#
#     "Each step down is inside the one above it. Watch the scale column: "
#     "it drops by roughly a factor of a thousand at every step, and nothing "
#     "new is added — you are looking at the same material, closer."
#
# A plain substring search over the file text finds none of those, which is why
# the first run of this harness reported 39 of 51 swaps as "COMPOSED" and sent
# them off for hand-authoring they did not need.
#
# `ast` already solves it: the parser folds implicit concatenation into a single
# `ast.Constant`, so the node carries the RECONSTRUCTED sentence, and its
# lineno/col_offset..end_lineno/end_col_offset span covers the whole literal
# group. We match against the node's value and rewrite the node's source span.
#
# This is also what makes the edit safe. We are not doing a textual replace and
# hoping; we are replacing one parsed expression with another, and re-parsing
# afterwards to prove the file still means what it says.

def source_files():
    out = []
    for root, _dirs, files in os.walk(DATA):
        if "__pycache__" in root:
            continue
        for f in files:
            if f.endswith(".py"):
                out.append(os.path.join(root, f))
    return sorted(out)


def _line_offsets(src):
    offs, n = [0], 0
    for line in src.splitlines(keepends=True):
        n += len(line)
        offs.append(n)
    return offs


def _col_to_char(line, byte_col):
    """Convert one of ast's BYTE columns into a character index.

    ⚠️ THIS IS NOT PEDANTRY, IT CORRUPTS SOURCE. `ast` reports `col_offset` and
    `end_col_offset` as offsets into the line's UTF-8 ENCODING, while a Python
    string index counts CHARACTERS. On a corpus written in ASCII the two agree
    and the bug is invisible; this corpus is not written in ASCII. Every one of
    these records uses typographic punctuation — `—` is 3 bytes, `’` and `“`
    are 3 each — so any literal whose FINAL line carries them reports an end
    column past the real one, and the span swallows the source that follows it.

    Found by the 3b-i pass: five of fifty-one swaps refused with "edit did not
    re-parse". On swap 4.1 the overshoot was exactly 4 characters — two `’` at
    2 extra bytes each — which ate the closing `),` and left an unbalanced
    bracket. The forty-six that applied cleanly had ASCII-only final lines.

    Nothing was corrupted, because `edit_source` re-parses before it writes and
    refused all five. That assertion existed for a defect I had not thought of,
    which is the argument for writing it.
    """
    raw = line.encode("utf-8")[:byte_col]
    return len(raw.decode("utf-8", errors="ignore"))


def _span(src, node):
    """Character span of a node in the source, from its 1-indexed line/col."""
    offs = _line_offsets(src)
    lines = src.splitlines(keepends=True)
    start_line = lines[node.lineno - 1]
    end_line = lines[node.end_lineno - 1]
    return (offs[node.lineno - 1] + _col_to_char(start_line, node.col_offset),
            offs[node.end_lineno - 1] + _col_to_char(end_line, node.end_col_offset))


def str_nodes(path):
    """Every SHIPPED string constant in a record, with its reconstructed value.

    Docstrings are excluded, and the exclusion is load-bearing rather than
    tidiness. These records carry long explanatory headers that quote the very
    prose they author — `energy_in_food_and_what_you_need.py` documents the
    sentence "You will meet that in Physics, in the unit Energy at home." in
    its header AND ships it at line 458. Counting the header made that swap
    look like it had two homes and would change more than one page, and the
    harness correctly refused to touch it.

    A docstring is the first statement of a module, class or function body. It
    is documentation by definition and reaches no student, so it is not a site.
    """
    src = open(path, encoding="utf-8").read()
    try:
        tree = ast.parse(src)
    except SyntaxError:
        return src, []

    docstrings = set()
    for node in ast.walk(tree):
        if isinstance(node, (ast.Module, ast.FunctionDef, ast.AsyncFunctionDef,
                             ast.ClassDef)):
            body = getattr(node, "body", None)
            if (body and isinstance(body[0], ast.Expr)
                    and isinstance(body[0].value, ast.Constant)
                    and isinstance(body[0].value.value, str)):
                docstrings.add(id(body[0].value))

    out = []
    for node in ast.walk(tree):
        if (isinstance(node, ast.Constant) and isinstance(node.value, str)
                and id(node) not in docstrings):
            out.append(node)
    return src, out


def find_in_source(needle):
    """Where does this sentence live? Returns [(path, node_count)] .

    Counts OCCURRENCES, not nodes: one node containing the sentence twice is
    still two occurrences and still means a single edit would change more than
    the audited page.
    """
    hits = []
    for path in source_files():
        _src, nodes = str_nodes(path)
        n = sum(nd.value.count(needle) for nd in nodes)
        if n:
            hits.append((path, n))
    return hits


def _render_literal(value, indent):
    """Re-emit a string as adjacent literals wrapped to the house width.

    The records wrap prose at roughly 76 columns as adjacent literals, and a
    swap that collapsed a four-line sentence onto one 300-character line would
    make every future diff on that lesson unreadable. So we re-wrap rather than
    re-flow onto one line.
    """
    body = value.replace("\\", "\\\\").replace('"', '\\"')
    width = max(28, 74 - len(indent))
    if len(body) <= width:
        return '"%s"' % body
    parts, line = [], ""
    for word in body.split(" "):
        cand = (line + " " + word) if line else word
        if len(cand) > width and line:
            parts.append(line + " ")
            line = word
        else:
            line = cand
    if line:
        parts.append(line)
    sep = "\n" + indent
    return sep.join('"%s"' % p for p in parts)


def edit_source(path, old, new):
    """Replace `old` with `new` inside the one string node that holds it.

    Returns the original file text so the caller can revert. Raises if the
    node is not unique or the result does not re-parse.
    """
    src, nodes = str_nodes(path)
    holders = [nd for nd in nodes if old in nd.value]
    if len(holders) != 1 or holders[0].value.count(old) != 1:
        raise ValueError("expected exactly one holding node, got %d" % len(holders))
    node = holders[0]
    start, end = _span(src, node)
    indent = " " * node.col_offset
    literal = _render_literal(node.value.replace(old, new, 1), indent)
    updated = src[:start] + literal + src[end:]
    try:
        ast.parse(updated)
    except SyntaxError as exc:
        raise ValueError("edit did not re-parse: %s" % exc)
    open(path, "w", encoding="utf-8").write(updated)
    return src


# ── the gate ──────────────────────────────────────────────────────────────

def check_one(sw, pages):
    """Return (status, detail). Status is one of OK / COMPOSED / MISSING /
    AMBIGUOUS. Nothing is written here."""
    rel, hits = resolve_page(sw["page"], pages)
    if rel is None:
        return "AMBIGUOUS", "page fragment matched %d files: %s" % (
            len(hits), ", ".join(sorted(hits)[:4]))

    text = visible_text(open(pages[rel], encoding="utf-8").read())
    want = re.sub(r"\s+", " ", sw["old"]).strip()
    n = text.count(want)
    if n == 0:
        return "MISSING", "old string not on %s (already applied? re-audit)" % rel
    if n > 1:
        return "AMBIGUOUS", "old string appears %d times on %s" % (n, rel)

    src_hits = find_in_source(sw["old"])
    if not src_hits:
        return "COMPOSED", ("on %s exactly once, but in no string literal in "
                            "ks3_data/ even after adjacent-literal folding — the "
                            "generator or an instrument in shared/ks3.js composes "
                            "it. Needs a hand-authored fix at the composing "
                            "site." % rel)
    if len(src_hits) > 1 or src_hits[0][1] > 1:
        where = ", ".join("%s x%d" % (os.path.relpath(p, REPO), c)
                          for p, c in src_hits)
        return "AMBIGUOUS", "source has %d occurrences (%s) — one edit would " \
                            "change more than the audited page" % (
                                sum(c for _p, c in src_hits), where)
    return "OK", "%s  <-  %s" % (rel, os.path.relpath(src_hits[0][0], REPO))


def apply_one(sw, pages):
    """Edit the source, rebuild, and prove the built tree moved exactly as
    promised. Reverts its own edit if any assertion fails — a half-applied
    swap is worse than an unapplied one."""
    status, detail = check_one(sw, pages)
    if status != "OK":
        return status, detail

    rel, _ = resolve_page(sw["page"], pages)
    path = find_in_source(sw["old"])[0][0]
    before = snapshot()
    try:
        original = edit_source(path, sw["old"], sw["new"])
    except ValueError as exc:
        return "FAILED", "source edit refused: %s" % exc
    build()

    after = snapshot()
    moved = sorted(r for r in after if before.get(r) != after.get(r))
    text = visible_text(open(built_pages()[rel], encoding="utf-8").read())
    old_left = text.count(re.sub(r"\s+", " ", sw["old"]).strip())
    new_want = re.sub(r"\s+", " ", sw["new"]).strip()
    new_seen = text.count(new_want) if new_want else None

    problems = []
    if old_left != 0:
        problems.append("old string still present %dx" % old_left)
    if new_want and new_seen != 1:
        problems.append("new string appears %dx, wanted exactly 1" % new_seen)
    if moved != [rel]:
        problems.append("changed %d page(s): %s" % (len(moved), ", ".join(moved[:6])))

    if problems:
        open(path, "w", encoding="utf-8").write(original)
        build()
        return "FAILED", "; ".join(problems) + "  (reverted)"
    return "APPLIED", "%s  via %s" % (rel, os.path.relpath(path, REPO))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--table", default=os.path.join(REPO, "ks3_prose_swaps.tsv"))
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--only", action="append", default=[])
    a = ap.parse_args()

    if not os.path.isdir(BUILT):
        sys.stderr.write("no built tree at %s — run build_ks3.py first\n" % BUILT)
        return 2

    swaps = load_swaps(a.table)
    if a.only:
        swaps = [s for s in swaps if s["id"] in a.only]
        if not swaps:
            sys.stderr.write("no swap matched --only %s\n" % a.only)
            return 2

    pages = built_pages()
    tally = {}
    bad = 0
    for sw in swaps:
        if a.apply:
            status, detail = apply_one(sw, pages)
            pages = built_pages()
        else:
            status, detail = check_one(sw, pages)
        tally[status] = tally.get(status, 0) + 1
        if status in ("FAILED", "AMBIGUOUS"):
            bad += 1
        print("  %-9s %-6s %s" % (status, sw["id"], detail))

    print()
    print("  " + " · ".join("%s %d" % (k, v) for k, v in sorted(tally.items())))
    if bad:
        print("\n  %d swap(s) could not be made safely. Nothing was left "
              "half-applied." % bad)
        return 1
    if tally.get("COMPOSED"):
        print("\n  %d swap(s) are generator-composed and need a hand-authored "
              "fix at the composing site. They are NOT done." % tally["COMPOSED"])
    return 0


if __name__ == "__main__":
    sys.exit(main())
