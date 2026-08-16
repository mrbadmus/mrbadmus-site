#!/usr/bin/env python3
"""splice_c1.py — integrate the C1 instrument fragments into the engine.

Run from the repo root:  python3 <this> [frag_dir] [tag]

The six lesson authors wrote their instruments as fragment files rather than
editing the engine, because five of the engine's files have a single-writer
rule and six agents editing `build_ks3.py` concurrently is how you lose a
renderer without noticing. This puts them in, in one pass, in a deterministic
order.

**Re-runnable.** Everything it writes sits between BEGIN/END markers, and a
second run replaces the whole marked region rather than appending beside it.
That matters because the fragments arrive in waves, and a splice that appends
would silently ship two copies of a renderer — the second shadowing the first,
with only the second's bugs visible.
"""

import os
import re
import sys

FRAG = sys.argv[1] if len(sys.argv) > 1 else "scratchpad/c1/frag"
TAG = sys.argv[2] if len(sys.argv) > 2 else "C1 · Particles and their behaviour (MRB-228)"
KEY = TAG.split(" ")[0]

B = "/* ═══ BEGIN %s ═══ */" % KEY
E = "/* ═══ END %s ═══ */" % KEY
PB = "# ═══ BEGIN %s ═══" % KEY
PE = "# ═══ END %s ═══" % KEY


def kinds():
    out = set()
    for f in os.listdir(FRAG):
        m = re.match(r"^(.+?)\.(renderer\.py|css|js|parity\.py)$", f)
        if m:
            out.add(m.group(1))
    return sorted(out)


def read(kind, ext):
    p = os.path.join(FRAG, "%s.%s" % (kind, ext))
    return open(p, encoding="utf-8").read().rstrip() + "\n" if os.path.exists(p) else ""


def replace_region(text, begin, end, body, anchor, before=True):
    """Swap the marked region, or create it at `anchor` if absent."""
    block = "%s\n%s\n%s\n" % (begin, body.rstrip(), end)
    if begin in text:
        pre, rest = text.split(begin, 1)
        _old, post = rest.split(end, 1)
        return pre + block + post
    i = text.index(anchor)
    return (text[:i] + block + "\n" + text[i:]) if before else (
        text[:i + len(anchor)] + "\n" + block + text[i + len(anchor):])


def main():
    ks = kinds()
    if not ks:
        print("no fragments in %s" % FRAG)
        return 1
    print("splicing %d kind(s): %s\n" % (len(ks), ", ".join(ks)))

    # ── 1. build_ks3.py — renderer functions, then dispatch entries ──────
    src = open("build_ks3.py", encoding="utf-8").read()

    bodies, dispatch = [], []
    for k in ks:
        r = read(k, "renderer.py")
        if not r:
            print("  !! %s has no renderer — skipped" % k)
            continue
        for line in r.split("\n"):
            m = re.match(r'\s*#\s*DISPATCH:\s*(.+?),?\s*$', line)
            if m:
                dispatch.append("    " + m.group(1).rstrip(",") + ",")
        bodies.append(r)

    src = replace_region(
        src, PB.replace("#", "# renderers:", 1), PE.replace("#", "# renderers:", 1),
        "\n\n".join(bodies), "ACTIVITY_KIND_RENDERERS = {")

    # Dispatch entries go inside the dict, before its closing brace.
    dmark_b = "    # ═══ BEGIN %s dispatch ═══" % KEY
    dmark_e = "    # ═══ END %s dispatch ═══" % KEY
    if dmark_b in src:
        pre, rest = src.split(dmark_b, 1)
        _o, post = rest.split(dmark_e, 1)
        src = pre + dmark_b + "\n" + "\n".join(dispatch) + "\n" + dmark_e + post
    else:
        i = src.index("ACTIVITY_KIND_RENDERERS = {")
        j = src.index("\n}\n", i)
        src = (src[:j] + "\n" + dmark_b + "\n" + "\n".join(dispatch)
               + "\n" + dmark_e + src[j:])
    open("build_ks3.py", "w", encoding="utf-8").write(src)
    print("  build_ks3.py  — %d renderer(s), %d dispatch entr(ies)"
          % (len(bodies), len(dispatch)))

    # ── 2. shared/ks3.css — appended, in kind order ──────────────────────
    css = open("shared/ks3.css", encoding="utf-8").read()
    blocks = [read(k, "css") for k in ks if read(k, "css")]
    if B in css:
        pre, rest = css.split(B, 1)
        _o, post = rest.split(E, 1)
        css = pre + B + "\n" + "\n".join(blocks) + E + post
    else:
        css = css.rstrip() + "\n\n" + B + "\n" + "\n".join(blocks) + E + "\n"
    open("shared/ks3.css", "w", encoding="utf-8").write(css)
    print("  shared/ks3.css — %d block(s)" % len(blocks))

    # ── 3. shared/ks3.js — wire functions, then dispatch lines ───────────
    js = open("shared/ks3.js", encoding="utf-8").read()
    fns, wires = [], []
    for k in ks:
        t = read(k, "js")
        if not t:
            continue
        fns.append(t)
        for line in t.split("\n"):
            m = re.match(r'\s*(?://|/\*)\s*WIRE:\s*(each\(.+?\);)', line)
            if m:
                wires.append("    " + m.group(1))

    js = replace_region(js, B, E, "\n\n".join(fns), "  function wireInstruments(root) {")

    wb = "    // ═══ BEGIN %s wiring ═══" % KEY
    we = "    // ═══ END %s wiring ═══" % KEY
    if wb in js:
        pre, rest = js.split(wb, 1)
        _o, post = rest.split(we, 1)
        js = pre + wb + "\n" + "\n".join(wires) + "\n" + we + post
    else:
        anchor = "    wireCoverBar(root);"
        i = js.index(anchor)
        js = js[:i] + wb + "\n" + "\n".join(wires) + "\n" + we + "\n" + js[i:]
    open("shared/ks3.js", "w", encoding="utf-8").write(js)
    print("  shared/ks3.js  — %d wire fn(s), %d dispatch line(s)"
          % (len(fns), len(wires)))

    # ── 4. ks3_parity.py — COMPONENTS entries ───────────────────────────
    par = open("ks3_parity.py", encoding="utf-8").read()
    rows = [read(k, "parity.py") for k in ks if read(k, "parity.py")]
    pb, pe = "    %s" % PB, "    %s" % PE
    if pb in par:
        pre, rest = par.split(pb, 1)
        _o, post = rest.split(pe, 1)
        par = pre + pb + "\n" + "\n".join(rows) + pe + post
    else:
        lines = par.split("\n")
        s = next(i for i, l in enumerate(lines) if l.startswith("COMPONENTS = ["))
        d = 0
        for i in range(s, len(lines)):
            d += lines[i].count("[") - lines[i].count("]")
            if d == 0 and i > s:
                lines[i:i] = [pb] + "\n".join(rows).split("\n") + [pe]
                break
        par = "\n".join(lines)
    open("ks3_parity.py", "w", encoding="utf-8").write(par)
    print("  ks3_parity.py  — %d parity block(s)" % len(rows))

    print("\ndone.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
