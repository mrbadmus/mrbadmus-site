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
    # ⊕ MRB-245 — B5's is here now. This list used to carry the note "B5's is
    # deliberately absent: the unit is parked and does not build", which was
    # true when it was written and stopped being true when B5 shipped. A
    # parked unit's omission is harmless; a shipped unit's is the false
    # positive described above, waiting for the first key only its normaliser
    # reads.
    # ⊕ MRB-245 — B7's, added with the unit. `_normalise()` there consumes
    # `core`, `activities`, `type`, `anchor`, `id`, `ground` and `demand`, and
    # omitting the file reports whatever only it reads as dead — the false
    # positive described above, and the one that gets a gate switched off.
    "ks3_data/b3/__init__.py", "ks3_data/b4/__init__.py",
    "ks3_data/b5/__init__.py", "ks3_data/b6/__init__.py",
    "ks3_data/b7/__init__.py",
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


# ── the dereference pattern ───────────────────────────────────────────────
#
# ⊕ MRB-245. A renderer that says `jobs[answer]` reads EVERY key of `jobs`,
# and names none of them. The literal scan cannot see that, so B3, C2 and B5
# were red on 26 keys whose text demonstrably reaches the built page — the
# audit's own claim, made backwards, for a second time.
#
# Taught the way `*_from` was taught, and for the same reason: the evidence is
# a piece of SYNTAX in the source, never a name on a list here. Nothing is
# waved through, and a map stops counting the moment no dynamic subscript
# reaches it.
#
# Two spellings, because the generator uses both:
#   `jobs[k]`, `runs[key()]`, `results[id]`, `colours[at.s]`  — bare name
#   `f["has"][tst["id"]]`                                     — literal first
#
# ⚠️ WHAT IS DELIBERATELY REFUSED, because this is the half that keeps it a
# gate rather than an exemption:
#   * A LITERAL subscript. `notes["iodine"]` names its key and the plain scan
#     already sees it; counting it would free the map's other eight keys off
#     the back of one.
#   * An integer or slice subscript — `verdicts[0]`, `args[1:]`. A list index
#     is not a map lookup, and without this every local list in the generator
#     would free an authored dict that happened to share its variable name.
#   * A subscript computed from a quoted literal, `runs["%s:%s" % (r, v)]`.
#     It IS a dynamic read, and it is still not counted: a map reachable ONLY
#     that way stays red, which is the conservative direction.
#   * Keys BELOW the first level, and keys of dicts inside a LIST under the
#     name. Only the map's own immediate keys are freed.
#   * Any map whose own key name has no read site. If nothing reads `jobs`,
#     `jobs` never reaches a renderer and its contents are dead with it.
#
# Proved by the two keys this does NOT free: `c2-04`'s `origin` and `c2-02`'s
# `element` are flagged dead-by-intent in their own source, sit in dicts that
# are only ever reached by literal key, and stay red.
_DEREF_PATTERNS = (
    # `NAME[` followed by something that is not a quote, a digit or a sign —
    # i.e. an expression, not a literal key and not a list index.
    re.compile(r"\b([A-Za-z_][A-Za-z0-9_]*)\s*\[\s*(?![\"'\d\-:\]])"),
    # `["NAME"][` — the map reached by literal key, then dereferenced.
    re.compile(r"[\"']([A-Za-z_][A-Za-z0-9_]*)[\"']\s*\]\s*\[\s*(?![\"'\d\-:\]])"),
    # `.NAME[` and the runtime's guarded spelling `(cfg.NAME || {})[k]`, which
    # reaches the map through a member access and an empty-object default. The
    # name is still written down; only the punctuation around it differs.
    re.compile(r"\.([A-Za-z_][A-Za-z0-9_]*)\s*(?:\|\|\s*\{\s*\}\s*)?\)?\s*"
               r"\[\s*(?![\"'\d\-:\]])"),
)

# A map can be RENAMED as it crosses into the payload, and then dereferenced
# under its new name: `"liquids": a.get("liquid_colours")` in the generator,
# `(cfg.liquids || {})[rxn]` in the runtime. `c2-06`'s `marble` and `magnesium`
# are read on every frame and were still red, because the authored name and the
# dereferenced name are different words.
#
# Followed the same way as everything else here — by matching the alias where
# it is WRITTEN. One hop only, and only from a literal key to a literal key.
_ALIAS = re.compile(
    r"[\"']([A-Za-z_][A-Za-z0-9_]*)[\"']\s*:\s*"
    r"[A-Za-z_][A-Za-z0-9_]*\s*(?:\.get\(\s*|\[\s*)[\"']([A-Za-z_][A-Za-z0-9_]*)[\"']")


def deref_maps(reads):
    """Names whose authored MAP a source file dereferences dynamically.

    `reads` gates the result: a map nothing reads by name cannot be reached to
    be dereferenced, so its keys are not freed either.
    """
    found, alias = set(), {}
    for path in SOURCES:
        try:
            with open(path, "r", encoding="utf-8") as fh:
                src = fh.read()
        except OSError:
            continue
        for pat in _DEREF_PATTERNS:
            found |= set(pat.findall(src))
        for new, old in _ALIAS.findall(src):
            alias.setdefault(new, set()).add(old)
    # One hop, and only INTO the set: a name that is dereferenced frees the
    # authored name it was renamed from, never the other way round.
    for new in list(found):
        found |= alias.get(new, set())
    return {n for n in found if n in reads}


def dereferenced_map_reads(node, deref, out, key=None):
    """Immediate keys of every authored map a renderer dereferences.

    `key` is the authored name the dict sits under. It is deliberately NOT
    carried through a list: `verdicts: [{...}]` is a list of records whose keys
    are schema fields, not a map whose keys are content.
    """
    if isinstance(node, dict):
        if key in deref:
            out |= {k for k in node if isinstance(k, str)}
        for k, v in node.items():
            dereferenced_map_reads(v, deref, out,
                                   k if isinstance(k, str) else None)
    elif isinstance(node, (list, tuple)):
        for v in node:
            dereferenced_map_reads(v, deref, out, None)
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
    # ⊕ MRB-245 — keys of a map the generator or the runtime dereferences with
    # a dynamic subscript. Harvested AFTER `reads`, because a map nothing reads
    # by name cannot be dereferenced either. See `deref_maps`.
    _deref = deref_maps(reads)
    for _u in units.values():
        dereferenced_map_reads(_u.get("lessons") or [], _deref, reads)

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
