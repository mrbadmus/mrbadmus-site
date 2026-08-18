"""⊕ MRB-249 — regenerate `docs/ks3/rail-manifest.md` from Design's own pages.

The manifest records the rail **as Design drew it**, so that
`ks3_parity.check_rail_matches_design` has an outside reference to check the
built rail against. Without one, the rail gate could only ever ask "can the
stops we emitted tick?" — and the defect it missed was a stop we never emitted.

Reads `docs/ks3/design-reference/<unit>/<stem>.dc.html` — Design's delivered
pages, which ARE in git. ⊕ Amended 18 Aug 2026 (MRB-248). This used to read
the deliveries from `KS3 B*/` at the repo root and note that they were
"deliberately NOT in git". They were not deliberately anything: they were ten
untracked folders that existed on one laptop, and this gate's reference source
therefore existed nowhere else. A gate whose input is missing does not fail
loudly — `main()` prints "nothing to do" and returns 0. So on every machine
but that one, the rail gate passed by having nothing to check.

The manifest is still the checked-in record, and still the thing
`ks3_parity.check_rail_matches_design` reads. The difference is that the
source it is derived FROM is now checked in too, so `--write` is reproducible
and the drift report is meaningful anywhere.

    python3 ks3_rail_manifest.py            # report drift, exit 1 if any
    python3 ks3_rail_manifest.py --write    # rewrite §1

`--write` is deliberately not the default. A generator that silently rewrites
its own gate's reference turns a failing gate into a passing one, which is the
one thing a gate may never do.
"""

import glob
import os
import re
import sys

MANIFEST = os.path.join("docs", "ks3", "rail-manifest.md")
HEADING = "## 1. Drawn rails"


def _slug(stem):
    """`b8-01-aerobic-respiration` → `aerobic-respiration`, the built filename.

    The subject letter matters: chemistry and physics deliveries are `c1-01-`
    and `p2-03-`, and a biology-only pattern silently left every C1 and C2
    lesson without a row — which the gate then reported as twelve unrecorded
    pages rather than as a bug in here. Caught by exactly that message.
    """
    return re.sub(r"^[a-z]\d+-\d+-", "", stem)


def drawn_rails(repo_root="."):
    """{slug: (design_stem, [anchors] | None, {mirror: target})} from Design."""
    # One delivery location. There used to be two — the root `KS3 B*/` folders
    # and the frozen reference set — and B2 lived in both with identical bytes.
    # MRB-248 folded the root folders in, so the frozen set is now the whole
    # record. The duplicate-detection below is kept anyway: it costs nothing
    # and it is the thing that would catch a unit being delivered twice under
    # two stems, which is a real way for a redelivery to go wrong.
    sources = sorted(glob.glob(os.path.join(
        repo_root, "docs", "ks3", "design-reference", "*", "*.dc.html")))
    out = {}
    for path in sources:
        stem = os.path.basename(path)[:-len(".dc.html")]
        with open(path, encoding="utf-8") as fh:
            page = fh.read()
        rail = re.search(r"const RAIL\s*=\s*(\[.*?\]);", page, re.S)
        if not rail:
            out.setdefault(_slug(stem), (stem, None, {}))
            continue
        ids = re.findall(r"id:\s*'([^']+)'", rail.group(1))

        # The mirror map is DERIVED, never declared: two stops mirror when
        # Design's `isDone()` returns the identical expression for both. That
        # is the only place she states it, and deriving it means the manifest
        # cannot drift from her logic by being transcribed wrong.
        # Scanned page-wide rather than inside a named `function isDone`,
        # because Design writes the same logic two ways: B3–B11 use a named
        # function, while B1 and C1 inline it as an IIFE —
        # `const done = (function (id) { if (id === 's-scale') return … })(r.id)`.
        # A regex anchored on the named form silently found nothing on the
        # inlined pages, which made two real mirrors (`c1-02`'s `s-matrix` and
        # `c1-05`'s `s-scale`) look like stops with conditions of their own.
        # The `id === '…' ) return …;` clause is unambiguous on its own.
        conds = {}
        for cid, expr in re.findall(
                r"id === '([^']+)'\)\s*return\s+([^;]+);", page):
            conds.setdefault(cid, re.sub(r"\s+", " ", expr).strip())
        mirrors = {}
        for i, cid in enumerate(ids):
            expr = conds.get(cid)
            if not expr:
                continue
            for j in range(i):
                if conds.get(ids[j]) == expr:
                    mirrors[cid] = ids[j]
                    break
        slug = _slug(stem)
        prev = out.get(slug)
        if prev is not None and prev[1] is not None and (prev[1], prev[2]) != (ids, mirrors):
            raise RuntimeError(
                "%s is delivered twice with different rails: %s says %s / %s, "
                "%s says %s / %s. Reconcile the deliveries; the manifest may "
                "not pick a winner."
                % (slug, prev[0], prev[1], prev[2], stem, ids, mirrors))
        if prev is None or prev[1] is None:
            out[slug] = (stem, ids, mirrors)
    return out


def manifest_rails(repo_root="."):
    """{slug: ([anchors], {mirror: target})} as recorded in the manifest."""
    with open(os.path.join(repo_root, MANIFEST), encoding="utf-8") as fh:
        text = fh.read()
    at = text.find(HEADING)
    if at < 0:
        raise RuntimeError(
            "%s has no %r heading. An empty registry makes every check "
            "vacuously pass, so this raises rather than returning nothing."
            % (MANIFEST, HEADING))
    out = {}
    for line in text[at:].splitlines():
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) != 4 or not cells[0].startswith("`"):
            continue
        slug = cells[0].strip("`")
        ids = None if cells[2] == "—" else cells[2].split()
        mirrors = {}
        if cells[3] != "—":
            for pair in cells[3].split():
                k, _, v = pair.partition("=")
                mirrors[k] = v
        out[slug] = (ids, mirrors)
    return out


def _rows(rails):
    lines = []
    for slug, (stem, ids, mirrors) in sorted(rails.items(), key=lambda kv: kv[1][0]):
        shown = " ".join(ids) if ids else "—"
        mir = " ".join("%s=%s" % kv for kv in sorted(mirrors.items())) or "—"
        lines.append("| `%s` | `%s` | %s | %s |" % (slug, stem, shown, mir))
    return "\n".join(lines) + "\n"


def main(argv):
    write = "--write" in argv
    rails = drawn_rails()
    if not rails:
        # Not "nothing to do" and not 0. An empty source set is the exact
        # shape of the defect MRB-248 found: the reference the gate derives
        # from went missing, and a green exit code reported that as health.
        print("no Design deliveries found under "
              "'docs/ks3/design-reference/*/*.dc.html'.")
        print("The manifest is derived from those pages, so an empty source "
              "set means the gate has nothing to check — which is a failure, "
              "not a pass.")
        return 1
    recorded = manifest_rails()
    drift = []
    for slug, (stem, ids, mirrors) in sorted(rails.items()):
        have = recorded.get(slug)
        if have is None:
            drift.append("%s: drawn by %s, absent from the manifest" % (slug, stem))
        elif have[0] != ids or have[1] != mirrors:
            drift.append("%s: manifest says %s / %s, Design draws %s / %s"
                         % (slug, have[0], have[1], ids, mirrors))
    if write:
        with open(MANIFEST, encoding="utf-8") as fh:
            text = fh.read()
        at = text.find(HEADING)
        head = text[:at] + HEADING + "\n\n| slug | design page | stops | mirrors |\n|---|---|---|---|\n"
        with open(MANIFEST, "w", encoding="utf-8") as fh:
            fh.write(head + _rows(rails))
        print("rewrote %s — %d rows" % (MANIFEST, len(rails)))
        return 0
    for line in drift:
        print("  ✗ " + line)
    print("%d lessons drawn, %d drifted" % (len(rails), len(drift)))
    return 1 if drift else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
