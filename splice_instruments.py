#!/usr/bin/env python3
"""splice_instruments.py — fold a unit's instrument fragments into the engine.

    python3 splice_instruments.py <frag_dir> "<TAG>"

    python3 splice_instruments.py docs/ks3/c1-inventory/instrument-fragments \\
            "C1 · Particles and their behaviour (MRB-228)"

The first word of the TAG is the KEY, and the KEY names the BEGIN/END markers
this writes between. One key per unit keeps units from overwriting each other's
spliced regions.

⊕ Promoted out of `docs/ks3/c1-inventory/` on 16 Aug 2026 (MRB-228), once B2
became its second caller. It was never C1-specific — the unit is an argument —
but leaving it filed under C1 meant every later unit reaching into C1's
inventory folder for a tool, which is how a shared thing quietly becomes
somebody's private copy.

Lesson authors write their instruments as fragment files rather than editing
the engine, because five of the engine's files have a single-writer rule and
several agents editing `build_ks3.py` concurrently is how you lose a renderer
without noticing. This puts them in, in one pass, in a deterministic order.

Four files per instrument kind, in `<frag_dir>`:

    <kind>.renderer.py   the r_<kind_with_underscores>() function, plus a
                         `# DISPATCH:` line giving its ACTIVITY_KIND_RENDERERS
                         row. The DRAWING function is DERIVED from the kind and
                         checked against the file — see the ACTIVITY_KIND_FN
                         splice below for why that second registry exists.
    <kind>.css           the complete CSS block
    <kind>.js            the wire<Name>() function, plus a `// WIRE:` line
    <kind>.parity.py     COMPONENTS rows, DRIVES entries and a commented page
                         constant, in `# ── … ──` sections

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
    """Swap the marked region, or create it at `anchor` if absent.

    ⚠️ IDEMPOTENT, and it was not (MRB-228). The block used to be built with a
    trailing newline AND a separator newline added at insert time, so every
    re-run put back one more blank line than it removed and the file grew by a
    line per splice — one in `build_ks3.py`, one in `shared/ks3.js`, one in
    `ks3_parity.py`, every time.

    Harmless to render and corrosive to everything else: two runs over the same
    fragments produced different bytes, so "byte-identical output" became a
    claim about how many times someone had run the splice. The separator now
    belongs to the insert path only; the replace path returns what it was
    given, exactly.
    """
    block = "%s\n%s\n%s" % (begin, body.rstrip(), end)
    if begin in text:
        pre, rest = text.split(begin, 1)
        _old, post = rest.split(end, 1)
        return pre + block + post
    i = text.index(anchor)
    return (text[:i] + block + "\n\n" + text[i:]) if before else (
        text[:i + len(anchor)] + "\n" + block + text[i + len(anchor):])


def split_parity(text):
    """Cut a parity fragment into (COMPONENTS rows, DRIVES pairs).

    Sections are named by their `# -- HEADER --` rules. Everything before the
    first header — and the whole of a fragment carrying no headers at all — is
    COMPONENTS rows, because that is what a fragment is by default.
    """
    sect = {"COMPONENTS": [], "DRIVES": []}
    cur = "COMPONENTS"
    for line in text.split("\n"):
        m = re.match(r'^#\s*──+\s*(PAGE CONSTANT|COMPONENTS|DRIVES)\b', line)
        if m:
            # A `PAGE CONSTANT` section holds only commentary once its
            # constants have been derived, and commentary is legal anywhere
            # inside a list literal, so it rides along with COMPONENTS.
            cur = "DRIVES" if m.group(1) == "DRIVES" else "COMPONENTS"
        sect[cur].append(line)
    return "\n".join(sect["COMPONENTS"]), "\n".join(sect["DRIVES"])


def splice_into(text, header, closer, begin, end, blocks):
    """Put `blocks` inside the literal opened by `header`, before its close.

    The close is found as the first line that is EXACTLY `closer` at column
    zero. Counting bracket depth would be wrong here: `DRIVES` holds raw
    JavaScript inside raw triple-quoted strings, and that JavaScript is full of
    braces that balance nothing in Python.

    Re-runnable: a second call replaces the marked region rather than adding a
    second copy beside it.
    """
    body = begin + "\n" + "\n".join(blocks) + "\n" + end
    if begin in text:
        pre, rest = text.split(begin, 1)
        _old, post = rest.split(end, 1)
        return pre + body + post
    lines = text.split("\n")
    s = next(i for i, l in enumerate(lines) if l.startswith(header))
    for i in range(s + 1, len(lines)):
        if lines[i] == closer:
            lines[i:i] = body.split("\n")
            break
    else:
        raise ValueError("%r is never closed by a bare %r" % (header, closer))
    return "\n".join(lines)


def main():
    ks = kinds()
    if not ks:
        print("no fragments in %s" % FRAG)
        return 1
    print("splicing %d kind(s): %s\n" % (len(ks), ", ".join(ks)))

    # ── 1. build_ks3.py — renderer functions, then dispatch entries ──────
    src = open("build_ks3.py", encoding="utf-8").read()

    # A kind is an ACTIVITY KIND if and only if its fragment registers a shell.
    #
    # ⊕ MRB-228. `cover-triangle` is the case that settles this: it is a
    # sub-key of the `formula` BLOCK, like its bar sibling, so it has no shell,
    # no marker attribute and no rail contract — it is read, not done. Its
    # fragment therefore carries no `# DISPATCH:` line at all, and the ABSENCE
    # is the declaration. Deriving it that way rather than from a magic
    # `DISPATCH: none` keeps the two registries in step by construction: no
    # shell means no drawing-function row, and build_ks3 asserts exactly that
    # pairing on import.
    bodies, dispatch, activities = [], [], set()
    for k in ks:
        r = read(k, "renderer.py")
        if not r:
            print("  !! %s has no renderer — skipped" % k)
            continue
        for line in r.split("\n"):
            m = re.match(r'\s*#\s*DISPATCH:\s*(.+?),?\s*$', line)
            if not m:
                continue
            # `# DISPATCH: none` — the fragment is NOT an activity kind and
            # registers nothing in either table. `cover-triangle` is the first:
            # it is a sub-key of the `formula` BLOCK, exactly as its bar
            # variant is, so it has no shell, no marker attribute and no rail
            # contract. Before this, "none" plus the sentence explaining it was
            # spliced into the dict as if it were a row, and the file stopped
            # parsing — which is the good failure, but "not an activity kind"
            # is a thing a fragment must be able to SAY rather than a thing it
            # says by breaking the build.
            if re.match(r'(?i)none\b', m.group(1)):
                continue
            dispatch.append("    " + m.group(1).rstrip(",") + ",")
            activities.add(k)
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
    # ⊕ MRB-228 — the SECOND registry, and the one whose absence cost the
    # whole of C1's first integration. A `DISPATCH:` line registers the shell;
    # it does not register the function that draws into it. That function name
    # is derivable — every instrument renderer is `r_<kind with underscores>` —
    # so it is derived rather than asked for, and checked against the fragment
    # so a renamed function fails here instead of rendering nothing.
    renderfn = []
    for k in ks:
        r = read(k, "renderer.py")
        if not r or k not in activities:
            continue
        fname = "r_" + k.replace("-", "_")
        if ("def %s(" % fname) not in r:
            print("  !! %s.renderer.py defines no %s() — the kind would "
                  "register a shell and draw nothing" % (k, fname))
            continue
        renderfn.append('    "%s": %s%s,' % (k, " " * max(0, 22 - len(k)), fname))

    # Create the region if this unit has never been spliced before, exactly as
    # the shell dispatch above does. The first cut required the marker to exist
    # already, which is fine for the unit the script was written for and wrong
    # for the second one — B2 hit it immediately.
    src = splice_into(src, "ACTIVITY_KIND_FN = {", "}",
                      "    # ═══ BEGIN %s renderfn ═══" % KEY,
                      "    # ═══ END %s renderfn ═══" % KEY, renderfn)

    open("build_ks3.py", "w", encoding="utf-8").write(src)
    print("  build_ks3.py  — %d renderer(s), %d shell entr(ies), %d draw fn(s)"
          % (len(bodies), len(dispatch), len(renderfn)))

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

    # ── 4. ks3_parity.py — page constants, COMPONENTS rows, DRIVES ──────
    #
    # A parity fragment has up to THREE sections and they belong in three
    # different places in the file:
    #
    #     # ── PAGE CONSTANT ──        commented `NAME = "path.html"` lines
    #     # ── COMPONENTS entries ──   `dict(...)` rows, for `COMPONENTS`
    #     # ── DRIVES entries ──       `"name": r"""..."""` pairs, for `DRIVES`
    #
    # The first cut of this splice knew only about COMPONENTS, so it dropped
    # each fragment's DRIVES pairs into the middle of the COMPONENTS list. That
    # is a SyntaxError, which is the good outcome — a `"key": value` pair is
    # not a list element and Python says so. It would have been far worse if it
    # had parsed. A fragment carrying no section header at all is COMPONENTS
    # rows, which is what most of them are.
    par = open("ks3_parity.py", encoding="utf-8").read()

    seen_const, consts, rows, drives = {}, [], [], []
    for k in ks:
        frag = read(k, "parity.py")
        if not frag:
            continue
        comp, drv = split_parity(frag)
        # Page constants are DERIVED from the whole fragment, not from one
        # section. Three fragments declare theirs under a `PAGE CONSTANT`
        # header and the other ten declare theirs in a preamble comment, and
        # both are the same statement: "this instrument needs this page". A
        # constant is emitted once, by whichever fragment asks first; a second
        # fragment naming the same page is agreeing, not conflicting.
        for name, val in re.findall(
                r'^#\s+([A-Z][A-Z0-9_]*)\s*=\s*("[^"]*")\s*$', frag, re.M):
            if name in seen_const:
                if seen_const[name] != val:
                    print("  !! %s declares %s = %s, already %s"
                          % (k, name, val, seen_const[name]))
                continue
            seen_const[name] = val
            consts.append("%s = %s" % (name, val))
        if comp.strip():
            rows.append(comp.rstrip())
        if drv.strip():
            drives.append(drv.rstrip())

    # Page constants land immediately above `COMPONENTS = [`, which is the one
    # position that is definitionally before every use of them.
    par = replace_region(par, PB, PE, "\n".join(consts).rstrip(),
                         "COMPONENTS = [")
    par = splice_into(par, "COMPONENTS = [", "]",
                      "    %s rows" % PB, "    %s rows" % PE, rows)
    par = splice_into(par, "DRIVES = {", "}",
                      "    %s drives" % PB, "    %s drives" % PE, drives)
    open("ks3_parity.py", "w", encoding="utf-8").write(par)
    print("  ks3_parity.py  — %d page constant(s), %d COMPONENTS block(s), "
          "%d DRIVES block(s)" % (len(seen_const), len(rows), len(drives)))

    print("\ndone.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
