#!/usr/bin/env python3
"""rebalance_ladder.py — move the correct answer's POSITION on marked ladder rungs.

    python3 tools/rebalance_ladder.py --plan            # print the plan, write nothing
    python3 tools/rebalance_ladder.py --apply C5        # rewrite one unit's files
    python3 tools/rebalance_ladder.py --apply-all       # rewrite every unit

── Why this exists (MRB-278, 21 Aug 2026) ───────────────────────────────

Measured on the BUILT pages, every one of the 58 marked ladder rungs across
all of Chemistry had its correct answer as the FIRST option — 100%. Across the
whole key stage the fourth option was correct 0 times out of 174, and index 0
held 59.2%. A student pressing the first button on every rung of any chemistry
lesson scored full marks without reading a word, and no student ever needed to
consider option four anywhere in KS3.

That is the same defect MRB-177 exists to prevent (a question that can be
answered without the science), one axis over: MRB-177 gates LENGTH, which is
position-independent by construction, so it never saw this.

── The one rule this tool obeys ─────────────────────────────────────────

MOVE THE ANSWER, NEVER REWRITE THE OPTION. Every option's source text is
spliced verbatim, byte for byte, into a new position. Nothing is retyped,
reflowed or reworded. Word counts are therefore identical and MRB-177 stays
green BY CONSTRUCTION, not by luck — and that is asserted after every run.

`feedback` is keyed by the index of the WRONG option it corrects, so the keys
are remapped with the options. A correction follows its own distractor; it
never lands on a different one.

── Why byte offsets ─────────────────────────────────────────────────────

`ast` reports col_offset in UTF-8 BYTES. These files carry ⚑, ⚠️ and — in
their comments, so character-indexed slicing silently cuts option text in the
wrong place. Everything here works on the encoded bytes and decodes only at
the end. Edits are applied BACK-TO-FRONT so that earlier spans keep their
offsets while later ones are replaced.
"""
import argparse, ast, hashlib, io, os, sys
from collections import Counter, defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(ROOT, "ks3_data")


def _h(s):
    return int(hashlib.sha256(s.encode("utf-8")).hexdigest(), 16)


def _lesson_files():
    for unit in sorted(os.listdir(DATA)):
        d = os.path.join(DATA, unit)
        if not os.path.isdir(d):
            continue
        for fn in sorted(os.listdir(d)):
            if fn.startswith("lesson_") and fn.endswith(".py"):
                yield unit, os.path.join(d, fn)


def _span(src_b, node, lines_b):
    """(start, end) byte offsets of `node` in the encoded source."""
    start = lines_b[node.lineno - 1] + node.col_offset
    end = lines_b[node.end_lineno - 1] + node.end_col_offset
    return start, end


def _line_starts(src_b):
    out, pos = [0], 0
    for ln in src_b.splitlines(keepends=True):
        pos += len(ln)
        out.append(pos)
    return out


def _dict_get(node, key):
    for k, v in zip(node.keys, node.values):
        if isinstance(k, ast.Constant) and k.value == key:
            return v
    return None


def scan(path):
    """Every marked ladder rung in one file: (slug, rung, nodes...)."""
    src_b = open(path, "rb").read()
    tree = ast.parse(src_b.decode("utf-8"))
    slug = None
    for n in ast.walk(tree):
        if isinstance(n, ast.Dict):
            s = _dict_get(n, "slug")
            if isinstance(s, ast.Constant) and isinstance(s.value, str) and slug is None:
                slug = s.value

    # A lesson may assign its ladder from a module-level name rather than
    # inline it (b1-03 does). Resolve those, or the rewriter silently skips
    # two real rungs while the gate still measures them — a fix nothing can
    # apply is worse than a finding.
    named = {}
    for n in tree.body:
        if isinstance(n, ast.Assign) and isinstance(n.value, ast.Dict):
            for t in n.targets:
                if isinstance(t, ast.Name):
                    named[t.id] = n.value

    ladders = []
    for n in ast.walk(tree):
        if not isinstance(n, ast.Dict):
            continue
        lad = _dict_get(n, "ladder")
        if isinstance(lad, ast.Name):
            lad = named.get(lad.id)
        if isinstance(lad, ast.Dict) and not any(lad is x for x in ladders):
            ladders.append(lad)

    rungs = []
    for lad in ladders:
        for k, v in zip(lad.keys, lad.values):
            if not (isinstance(k, ast.Constant) and isinstance(v, ast.Dict)):
                continue
            opts = _dict_get(v, "options")
            ans = _dict_get(v, "answer")
            fb = _dict_get(v, "feedback")
            if not isinstance(opts, ast.List) or not isinstance(ans, ast.Constant):
                continue
            if not all(isinstance(o, ast.Constant) for o in opts.elts):
                continue
            rungs.append(dict(rung=k.value, opts=opts, ans=ans, fb=fb))
    return src_b, slug, rungs


def collect():
    """Every rung in the key stage, with its file."""
    out = []
    for unit, path in _lesson_files():
        src_b, slug, rungs = scan(path)
        for r in rungs:
            out.append(dict(unit=unit.upper(), path=path, slug=slug,
                            rung=r["rung"], n=len(r["opts"].elts),
                            answer=r["ans"].value))
    return out


def plan(rungs):
    """Deterministic, balanced target index per rung.

    Hash-shuffled order so the sequence a student sees is not a walkable
    cycle; then each rung takes the least-used index IN ITS UNIT, tie-broken
    by least-used globally and then by hash. Same answer on every machine and
    every run — the build stays reproducible.
    """
    order = sorted(rungs, key=lambda r: _h("%s|%s" % (r["slug"], r["rung"])))
    gl, byu, out = Counter(), defaultdict(Counter), {}
    for r in order:
        uc = byu[r["unit"]]
        best = min(range(r["n"]),
                   key=lambda i: (uc.get(i, 0), gl.get(i, 0),
                                  _h("%s|%s|%d" % (r["slug"], r["rung"], i))))
        out[(r["slug"], r["rung"])] = best
        uc[best] += 1
        gl[best] += 1
    return out


def rewrite_file(path, targets, dry=False):
    """Apply the plan to one file. Returns (n_rungs_moved, report)."""
    src_b, slug, rungs = scan(path)
    lines_b = _line_starts(src_b)
    edits, moved, report = [], 0, []

    for r in rungs:
        key = (slug, r["rung"])
        if key not in targets:
            continue
        old_ans = r["ans"].value
        tgt = targets[key]
        n = len(r["opts"].elts)
        if tgt == old_ans:
            continue

        # P[j] = index in the OLD list of the option that now sits at j.
        others = [i for i in range(n) if i != old_ans]
        P, it = [None] * n, iter(others)
        P[tgt] = old_ans
        for j in range(n):
            if P[j] is None:
                P[j] = next(it)

        # options: splice each old element's source verbatim into its new slot
        spans = [_span(src_b, o, lines_b) for o in r["opts"].elts]
        texts = [src_b[a:b] for a, b in spans]
        for j in range(n):
            if P[j] != j:
                edits.append((spans[j][0], spans[j][1], texts[P[j]]))

        # answer
        a, b = _span(src_b, r["ans"], lines_b)
        edits.append((a, b, str(tgt).encode()))

        # feedback: a correction follows its own distractor
        if isinstance(r["fb"], ast.Dict):
            for k in r["fb"].keys:
                if not (isinstance(k, ast.Constant) and isinstance(k.value, int)):
                    continue
                old_i = k.value
                new_i = P.index(old_i)
                if new_i != old_i:
                    ka, kb = _span(src_b, k, lines_b)
                    edits.append((ka, kb, str(new_i).encode()))
        moved += 1
        report.append("%s · %s: answer %d -> %d" % (slug, r["rung"], old_ans, tgt))

    if not edits:
        return 0, report
    for a, b, rep in sorted(edits, key=lambda e: -e[0]):
        src_b = src_b[:a] + rep + src_b[b:]
    if not dry:
        open(path, "wb").write(src_b)
    return moved, report


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--plan", action="store_true")
    ap.add_argument("--apply")
    ap.add_argument("--apply-all", action="store_true")
    a = ap.parse_args()

    rungs = collect()
    tg = plan(rungs)

    if a.plan:
        gl, byu = Counter(), defaultdict(Counter)
        for r in rungs:
            t = tg[(r["slug"], r["rung"])]
            gl[t] += 1
            byu[r["unit"]][t] += 1
        print("rungs: %d" % len(rungs))
        print("global:", [gl.get(i, 0) for i in range(4)])
        for u in sorted(byu):
            c = byu[u]
            print("  %-5s %s" % (u, [c.get(i, 0) for i in range(4)]))
        return 0

    units = None
    if a.apply:
        units = {x.strip().upper() for x in a.apply.split(",")}
    elif not a.apply_all:
        ap.error("one of --plan / --apply / --apply-all")

    total = 0
    for unit, path in _lesson_files():
        if units and unit.upper() not in units:
            continue
        m, rep = rewrite_file(path, tg)
        total += m
        for line in rep:
            print("   ", line)
    print("moved %d rung(s)" % total)
    return 0


if __name__ == "__main__":
    sys.exit(main())
