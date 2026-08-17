"""Every authored key, against the code that reads it.

MRB-220. The B1 replay shipped 234 authored keys of which **146 were read by
nothing** — one of them an approved science correction that therefore never
reached a student. A key with no read site is invisible: the data says the
lesson teaches something, the page does not, and no gate fires because nothing
is broken. It is the cheapest possible way to lose content.

    python3 ks3_key_audit.py B2 C1 C2            # audit these units
    python3 ks3_key_audit.py --control B1 B2 C2  # ...against a known-good unit
    python3 ks3_key_audit.py --raw B2            # no control, every unread key

Exit status is 1 if any key is read by nothing, so this can gate a build.

── Why there is a CONTROL, and why a bare run over-reports ──────────────

A lesson record mixes two kinds of dict key and only one of them is a schema
field:

  * **Schema keys** — `rail`, `done_when`, `why_openers`. Named as string
    literals by a renderer. If one is unread, that is the defect this exists
    to catch.
  * **Content keys** — `mitochondria`, `chloroplasts`, `"400"`. Keys of an
    authored MAP, read by iterating the dict, never by literal name. A
    renderer that says `for part, val in parts.items()` mentions neither, and
    it is correct that it does not.

Nothing in the tree distinguishes them structurally, so a bare run reports
every content key as dead — 150 of them on B1, a unit that is verified and
correct. That is noise, and a gate that cries wolf is a gate people switch off.

So the default mode is DIFFERENTIAL. B1 is authored, reviewed and shipped, so
any key unread in B1 is either a content key or a pre-existing condition —
either way it is not something this run introduced. Subtracting B1's unread
set leaves the keys that are unread *and new*, which is exactly the failure
mode: a field authored in this run and never wired.

`--raw` gives the unsubtracted list when you want to audit the control itself.

⚠️ This is a LINT, not a proof. It answers "does any source file mention this
name?", not "does this lesson's value reach this page". A key named only in a
comment counts as read, and a key read on a branch that never runs counts as
read. It catches a field authored and then forgotten. The browser-driven
assertions in verify_ks3.py are what cover the rest.
"""

import re
import sys

# Consumed by ks3_data/__init__.py, structure.py or a unit normaliser rather
# than by a renderer, so "no read site" is correct for these and not a finding.
STRUCTURAL = {
    "code", "slug", "title", "discipline", "unit", "family", "lessons",
    "statutory_area", "split_rationale", "intro", "id", "kind", "type",
}

# Every file that legitimately reads an authored key. The generator and the
# runtime are the obvious two; the gates and the data layer read schema fields
# the renderers never touch (`covers`, `assumes`, `threads`), and omitting them
# reports those as dead.
SOURCES = (
    "build_ks3.py", "shared/ks3.js", "shared/ks3.css", "ks3_parity.py",
    "verify_ks3.py", "ks3_data/__init__.py", "ks3_data/structure.py",
    "ks3_statutory.py", "ks3_data/b1/__init__.py", "ks3_data/b2/__init__.py",
    "ks3_data/c1/__init__.py", "ks3_data/c2/__init__.py",
    # ⊕ MRB-244 — B3, B4 and B6's normalisers were missing. Every unit built
    # since C2 lifts instruments through its own `__init__.py`, and omitting
    # one reports the keys THAT file consumes as dead. An omission here is a
    # false POSITIVE, which is the failure that gets a gate switched off.
    # (B5's is deliberately absent: the unit is parked and does not build.)
    "ks3_data/b3/__init__.py", "ks3_data/b4/__init__.py",
    "ks3_data/b6/__init__.py",
)


def _keys(node, out):
    """Every dict key appearing anywhere in a literal tree."""
    if isinstance(node, dict):
        for k, v in node.items():
            if isinstance(k, str):
                out.add(k)
            _keys(v, out)
    elif isinstance(node, (list, tuple)):
        for v in node:
            _keys(v, out)


def unit_keys(unit):
    """lesson slug -> set of every key in that lesson record."""
    per = {}
    for lesson in unit.get("lessons") or []:
        ks = set()
        _keys(lesson, ks)
        per[lesson.get("slug") or "?"] = ks
    return per


def indirect_reads(node, out):
    """Key names a renderer reaches through a POINTER rather than by name.

    ⊕ MRB-244. b6-01 authored `drugs[].entry` and the audit called it dead.
    It is not: `r_route_tracer` reads it as ``d[st["body_from"]]``, and the
    authored `body_from` is the string ``"entry"``. The literal scan cannot
    see through that, so a key whose text demonstrably reaches the built page
    was reported as content that never reaches a student — the exact claim the
    audit exists to make, made backwards.

    A `*_from` value IS a read site, by construction: it is the author naming
    which key the renderer should dereference. Counting it is narrower than an
    exemption for `entry` would have been — nothing is waved through by name,
    and a key stops counting the moment no pointer names it.
    """
    if isinstance(node, dict):
        for k, v in node.items():
            if isinstance(k, str) and k.endswith("_from") and isinstance(v, str):
                out.add(v)
            indirect_reads(v, out)
    elif isinstance(node, (list, tuple)):
        for v in node:
            indirect_reads(v, out)
    return out


def read_sites():
    """Every identifier the generator, runtime, gates and data layer mention."""
    seen = set()
    for path in SOURCES:
        try:
            with open(path, "r", encoding="utf-8") as fh:
                src = fh.read()
        except OSError:
            continue
        seen |= set(re.findall(r"[\"']([A-Za-z_0-9][A-Za-z0-9_+\- ]*)[\"']", src))
        seen |= set(re.findall(r"\.get\(\s*[\"']([^\"']+)[\"']", src))
        seen |= set(re.findall(r"\.([A-Za-z_][A-Za-z0-9_]*)\b", src))
    return seen


def main(argv):
    sys.path.insert(0, ".")
    import ks3_data

    args = [a for a in argv[1:]]
    raw = "--raw" in args
    if raw:
        args.remove("--raw")
    control = "B1"
    if "--control" in args:
        i = args.index("--control")
        control = args[i + 1]
        del args[i:i + 2]
    wanted = {a.upper() for a in args}

    units = {(u.get("code") or "").upper(): u for u in ks3_data.build_units()}
    targets = [c for c in sorted(wanted or units) if c in units]
    if not targets:
        print("no units matched %s" % (sorted(wanted) or "<all>"))
        return 1

    reads = read_sites()
    # ⊕ MRB-244 — pointer-dereferenced keys, gathered from the authored data
    # itself rather than from the source scan. See `indirect_reads`.
    for _u in units.values():
        indirect_reads(_u.get("lessons") or [], reads)

    def unread(code):
        out = {}
        for slug, keys in unit_keys(units[code]).items():
            dead = {k for k in keys if k not in STRUCTURAL and k not in reads}
            if dead:
                out[slug] = dead
        return out

    baseline = set()
    if not raw and control in units:
        for dead in unread(control).values():
            baseline |= dead
        print("control: %s — %d unread key name(s) subtracted as content keys "
              "or pre-existing\n" % (control, len(baseline)))

    total = 0
    skipped = []
    for code in targets:
        if not raw and code == control:
            # A unit cannot be its own control: its dead keys go into the
            # baseline and are then subtracted from themselves, so the audit
            # can only ever come back empty.
            skipped.append(code)
            continue
        found = {slug: sorted(d - baseline) for slug, d in unread(code).items()}
        found = {s: d for s, d in found.items() if d}
        n = sum(len(d) for d in found.values())
        keys_seen = sum(len(k) for k in unit_keys(units[code]).values())
        if n:
            total += n
            print("%s — %d key(s) read by NOTHING" % (code, n))
            for slug, dead in sorted(found.items()):
                print("   %-34s %s" % (slug, ", ".join(dead)))
        else:
            print("%-4s ✓ every authored key has a read site "
                  "(%d keys over %d lessons)"
                  % (code, keys_seen, len(unit_keys(units[code]))))

    # ⊕ MRB-242 — a run that audited NOTHING used to print the same green tick
    # as a run that audited everything. `ks3_key_audit.py B1` skipped B1 as its
    # own control, checked no units at all, and reported "✓ no dead authored
    # keys" — which is how B1's 103 dead keys (the `fit-parts` verdict badge
    # and all five of its headlines among them) sat behind a passing gate. A
    # gate that cannot fail is not a gate.
    if skipped and not [c for c in targets if c not in skipped]:
        print("\n✗ nothing was audited: %s %s its own control, so every dead "
              "key would be subtracted from itself.\n"
              "  Re-run as `--raw %s` to see its real dead keys, or name a "
              "different `--control`."
              % (", ".join(skipped),
                 "is" if len(skipped) == 1 else "are",
                 " ".join(skipped)))
        return 1
    if skipped:
        print("\n! skipped %s — a unit cannot be its own control. Audit it "
              "with `--raw` or a different `--control`." % ", ".join(skipped))

    if total:
        print("\n✗ %d authored key(s) read by nothing. A key with no read "
              "site is content that never reaches a student." % total)
        return 1
    print("\n✓ no dead authored keys")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
