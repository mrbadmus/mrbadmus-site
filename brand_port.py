"""brand_port.py — the one mark, on the pages the compiled Design ports emit.

Mide's ruling, 13 Sep 2026: ONE mark on every page (see brand.py). The two
compiled ports — build_student_port.py and build_teacher_port.py — render
Design's templates with shared/student-runtime.js, and Design's templates
carry her own copy of the header brand (a `MrBadmusDS.BrandMark` import and
a "MrBadmusAI" text span on the student pages; a "MrBadmusAI" text span on
the teacher screens). A ruling cannot type the kit's SVG into a template —
that would be a second drawing — so the ports replace Design's brand run with
ONE node, `{"t": "brand"}`, and the runtime draws it at mount from
`window.MrBadmusBrand` (shared/brand/brand.js, written by brand.py).

This module is the machinery both ports share, so the two cannot come to
disagree about what a brand substitution asserts. The rulings themselves are
declared where every other ruling of each port is: `RULED_BRAND` in
student_rulings.py and teacher_rulings.py.
"""

import brand

# The shared assets a page carrying the brand node must load, relative to
# /shared/ — each port adds these to its STAMPED_DEPS so every one carries a
# content-hash `?v=` stamp like the rest of the page's shared assets.
BRAND_DEPS = ("brand/brand.js", "brand/brand.css",
              "brand/mrbadmus-favicon.svg", "brand/mrbadmus-icon-light-512.png")

# <head>: the kit's favicon + app icon + the lockup's stylesheet (brand.py's
# own brand_head(), unstamped — the port's stamp_versions() stamps it), then
# brand.js, which must be loaded before the runtime mounts.
HEAD = brand.brand_head() + "\n" + '<script src="/shared/brand/brand.js"></script>\n'

OLD_NAME = "MrBadmusAI"


def _walk(n, fn):
    if isinstance(n, dict):
        fn(n)
        for kid in n.get("c") or []:
            _walk(kid, fn)


def _holds_design_mark(nodes):
    found = []

    def see(n):
        if n.get("t") == "import" and n.get("from") == "MrBadmusDS.BrandMark":
            found.append("import")
        if n.get("t") == "#" and isinstance(n.get("v"), str) and n["v"].strip() == OLD_NAME:
            found.append("text")

    for n in nodes:
        _walk(n, see)
    return found


def _handlers(nodes):
    found = []

    def see(n):
        for slot in ("on", "onch", "oninput", "onkey"):
            if n.get(slot):
                found.append((n.get("i"), slot, n[slot]))

    for n in nodes:
        _walk(n, see)
    return found


def replace_brand_run(roots, run, why, who, where):
    """Replace the consecutive sibling nodes `run` (template indices) with ONE
    `{"t": "brand"}` node, in place. Returns the parent's index.

    Refuses — stopping the build — when the run is not found, is not a run of
    consecutive siblings, does not hold Design's mark, or carries a handler.
    The click stays with the control AROUND the run, untouched.
    """
    run = list(run)
    hits = []

    def find(parent):
        kids = parent.get("c") or []
        idx = [k.get("i") if isinstance(k, dict) else None for k in kids]
        if run[0] in idx:
            hits.append((parent, idx.index(run[0])))

    for r in roots:
        _walk(r, find)
    if len(hits) != 1:
        raise SystemExit(
            "%s: the one-mark ruling (%s) replaces template node(s) %s, and "
            "node %s is %d places in the template, not one. Design has "
            "redrawn the header; re-anchor %s. (%s)"
            % (who, where, run, run[0], len(hits), where, why))
    parent, pos = hits[0]
    kids = parent["c"]
    got = [k.get("i") if isinstance(k, dict) else None
           for k in kids[pos:pos + len(run)]]
    if got != run:
        raise SystemExit(
            "%s: the one-mark ruling (%s) names %s as consecutive siblings, "
            "and the template holds %s there. Re-anchor %s. (%s)"
            % (who, where, run, got, where, why))
    doomed = kids[pos:pos + len(run)]
    if not _holds_design_mark(doomed):
        raise SystemExit(
            "%s: the one-mark ruling (%s) replaces nodes %s, and they hold "
            "neither Design's BrandMark import nor a %r text node. Whatever "
            "sits at those indices now is not the brand; re-anchor %s. (%s)"
            % (who, where, run, OLD_NAME, where, why))
    live = _handlers(doomed)
    if live:
        raise SystemExit(
            "%s: the one-mark ruling (%s) would remove nodes carrying "
            "handlers %s. The brand's click lives on the control AROUND the "
            "run and must survive it; re-anchor %s. (%s)"
            % (who, where, live, where, why))
    kids[pos:pos + len(run)] = [{"t": "brand", "i": run[0]}]
    return parent.get("i")
