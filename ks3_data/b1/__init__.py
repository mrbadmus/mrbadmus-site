"""B1 — Cells and organisation, as one module per lesson.

Round two of B1 is authored **one lesson to a file**, against Claude Design's
approved reference screens in `docs/ks3/design-reference/b1/` and the measured
inventories in `docs/ks3/b1-inventory/`. That is a change from round one, where
all six lessons shared `ks3_data/biology_b1_cells.py`: the round-two records
carry an instrument's whole payload each — two microscope mounts, a seven-row
comparison, sixteen marked judgements — and one file per lesson keeps a diff
readable and lets six agents author six lessons without colliding.

Each module exports a single `LESSON` dict, shaped by `architecture.md` §4.8
and its §4.8.1 / §4.8.2 amendments. Identity fields (`slug`, `title`, `family`)
must match the lesson's slot in `ks3_data/structure.py` exactly — slugs are
permanent (§8.4) and scheme-of-work rows, progress records and `requires` edges
all point at them.

`lessons()` below is what `biology_b1_cells.py` collects, and it is where the
round-one records came out.

── Instrument blocks are ACTIVITIES, not new block types ────────────────

§5.1.1's block vocabulary is CLOSED — "a lesson is assembled from these types
and no others; a new type requires an amendment to this document" — and
MRB-203's registry fails the build on a block type with no registered
component. B1 round two legitimately added four types (`key-fact`, `rule`,
`formula`, `comparison`), each of which is a LAYOUT: a shell with prose in it.

The instruments are not that. `system-bench`, `sabotage`, `zoom-ladder`,
`sort-task`, `removal-cases` and `settles-it` are interactive tasks with a
demand, a commitment and a reveal — which is exactly what §5.5's activity
record is for, and what `activities[].kind` already distinguishes. Admitting
each as a page-level segment would grow the vocabulary by six for no gain and
would put an instrument on the same footing as `hook` and `summary`.

The six lesson modules were authored in parallel and two of them expressed
their instruments as block types with the payload inline. Rather than rewrite
~300KB of verified byte-identical content with a script — the one edit most
likely to silently corrupt a string that crosses the examiner gate — the
normalisation happens here, once, in code that can be read.

The other direction was available and is worse: registering six new block types
would make the registry agree with the data by widening the rule, which is the
failure MRB-203 exists to stop, one level up.
"""

import importlib
import pkgutil

# Instrument block types seen in authored B1 data, mapped to the §5.1.1 segment
# they render as. `practical` is the hands-on/simulated investigation shell;
# `check` is the do-it-yourself counterpart. The distinction follows what the
# student is asked to do, not how complicated the widget is.
#
# ⚠️ The segment decides the SHELL, and `practical` is ink-dark. Two of these
# were wrong and it took a layer-C assertion to say so: `system-bench` and
# `zoom-ladder` were mapped to `practical`, and Design draws both as a plain
# light `ks3-block`. The zoom instrument's accent-text gain label was resolving
# to `--ks3-on-dark-body` because `.ks3-dark p` was winning — a whole
# instrument painted on the wrong ground, on the reference screens for SYSTEM
# (32 slots) and on the page Mide rejected by name.
#
# Measured from Design's own markup:
#   #s-tuned  ks3-block                          light  → check
#   #s-zoom   ks3-block                          light  → check
#   #s-hard   ks3-block                          light  → check
#   #s-settle ks3-block                          light  → check
#   #s-break  ks3-block ks3-dark ks3-practical   dark   → practical  (both pages)
_INSTRUMENT_SEGMENTS = {
    "system-bench":   "check",
    "sabotage":       "practical",
    "zoom-ladder":    "check",
    "removal-cases":  "practical",
    "settles-it":     "check",
    "sort-task":      "check",
}


def _normalise(lesson):
    """Lift inline instrument blocks into `activities[]`. Returns the lesson."""
    core = lesson.get("core") or []
    acts = list(lesson.get("activities") or [])
    known = {a.get("id") for a in acts}
    out = []

    for block in core:
        kind = block.get("type")
        segment = _INSTRUMENT_SEGMENTS.get(kind)
        if not segment:
            out.append(block)
            continue

        # The anchor is the only stable name an inline instrument has, and it is
        # already unique within the lesson because it is a DOM id.
        act_id = block.get("id") or block.get("anchor") or kind
        if act_id in known:
            raise ValueError(
                "%s: instrument %r collides with an existing activity id"
                % (lesson.get("slug"), act_id))
        known.add(act_id)

        payload = {k: v for k, v in block.items()
                   if k not in ("type", "anchor", "id")}
        payload.update({"id": act_id, "kind": kind})
        payload.setdefault("demand", "investigate")
        acts.append(payload)
        out.append({"type": segment, "id": act_id,
                    "anchor": block.get("anchor")})

    lesson["core"] = out
    lesson["activities"] = acts
    return lesson


def lessons():
    """The six B1 lesson records, in slot order, normalised."""
    found = []
    for mod in sorted(m.name for m in pkgutil.iter_modules(__path__)):
        if not mod.startswith("lesson_"):
            continue
        m = importlib.import_module("%s.%s" % (__name__, mod))
        record = getattr(m, "LESSON", None)
        if record is not None:
            found.append(_normalise(dict(record)))
    return found
