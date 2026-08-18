"""B8 — Respiration, as one module per lesson.

Authored against Claude Design's approved reference screens in
`KS3 B8 lessons/`, under the MRB-220 build contract
(`docs/ks3/mrb-220-build-contract.md`) and the payload schema written for this
run at `docs/ks3/b8-inventory/PAYLOAD-SCHEMA.md`. Shape follows `ks3_data/b7/`,
which follows B5, B4, B3, C1, C2, B2 and B1: each module exports a single
`LESSON` dict and this file collects them.

Every student-facing string is lifted byte-identical from the approved page.

── ⚠️ DESIGN DRAWS FOUR RAIL STOPS PER PAGE. THREE CAN TICK. ─────────────

Measured before dispatch this time, in the schema's §7, rather than four times
over by four authors afterwards. On every B8 page one rail stop is anchored to
the BAND section — `#s-summary` (b8-01), `#s-jobs` (b8-02), `#s-equation`
(b8-03), `#s-two` (b8-04), `#s-table` (b8-05) — and every one of those renders
as a core `rule` (b8-05: `comparison`), which is a `<section class="ks3-rule">`
of static cards.

`ks3_parity.check_rail_reachable()` requires the anchored section to contain one
of five literal DOM signals — `data-stage-done`, `class="ks3-rung`,
`data-reveal`, `ks3-reveal-btn`, `class="ks3-option`. The band sections carry
none, so a stop on one could never tick and FAILS the build.

It appears to work on Design's own page only because Design's `isDone()` aliases
the band stop to the bench's PRIVATE state — `s-summary` returns `s.exits`,
`s-jobs` and `s-two` return the bench's seen-count, `s-equation` returns
`everRecovered`, `s-table` returns the opened-count. Aliasing it here would tick
a stop for something the student did in a different section, which is exactly
what MRB-208's completion rule exists to prevent.

**Three stops per lesson; the band stop is dropped and its ANCHOR IS KEPT**, so
hash links, `elicited_by` and `confronted_by` still resolve. Same call as B7's
four pages, b4-03 `#s-built`, b5-06 `#s-designs`, b6-03 `#s-four`, c1-02
`#s-matrix` and eight others. NOTES-B8 §4's "four in all five" is reported, not
silently followed.

── `#s-think` is `confrontation` on all five, NOT `predict` ──────────────

Measured on all five pages: `ks3-block ks3-misconception` containing a quoted
belief, a paragraph, a 2px alert rule, a second quoted belief and a second
paragraph. No options list, no reveal, no button, no state. Contract §2 R1's
`predict` branch applies where `#s-think` asks for a commitment and then
reveals; B8 does not ask for one. So `confrontation`, as B1 and B7 have it.
`#s-think` is not a rail stop on any B8 page — Design's `RAIL` never lists it —
so `confrontation` emitting no `data-stage-done` costs nothing.

── Instrument blocks are ACTIVITIES, not block types ────────────────────

Same argument and mechanism as B1–B7, C1 and C2. §5.1.1's block vocabulary is
CLOSED and MRB-203's registry fails the build on a block type with no registered
component, so an instrument is authored inline in `core` — where its position in
the document is obvious — and `_normalise()` lifts it into `activities[]`,
leaving the right SHELL behind it.

⚠️ Measured from Design's own markup on all five pages, character for character,
not inherited from the kind name (contract §4: B1 got two of six wrong that way):

    b8-01 #s-bench   ks3-block ks3-dark ks3-practical   dark → practical
    b8-02 #s-bench   ks3-block ks3-dark ks3-practical   dark → practical
    b8-03 #s-bench   ks3-block ks3-dark ks3-practical   dark → practical
    b8-04 #s-bench   ks3-block ks3-dark ks3-practical   dark → practical
    b8-05 #s-bench   ks3-block ks3-dark ks3-practical   dark → practical

⚠️ ALL FIVE ARE ON INK. `.ks3-dark p` is (0,1,1) and beats a bare instrument
class at (0,1,0), so every text rule in every B8 instrument is written under
`.ks3-dark …` at (0,2,0). This trap has now bitten eleven builds and was
re-laid in B7's own brand-new stylesheet hours after being gated. Since MRB-245
`ks3_parity.check_dark_text_specificity()` resolves the real cascade winner on
every element on every ink ground and fails when a generic `.ks3-dark <type>`
rule beats a component's colour — but the rules are still written scoped,
because a gate that fires is not the same as a defect that never happened.

── Nothing in this unit animates, and nothing uses a timer ──────────────

All five instruments are DOM-only: no `<canvas>`, no `requestAnimationFrame`,
no `setTimeout`, no `setInterval`. Grepped across all five approved pages and
returns zero on every term. There is therefore no rAF loop in the B8 runtime
for `prefers-reduced-motion` to be checked inside (MRB-220 R4, the b2-03 slip),
and the B8 stylesheet adds no transition for the platform-wide reduced-motion
rule to have to remove.

── Figures: EMPTY ON ALL FIVE, and that is measured, not an omission ─────

`<img>`, `<figure>` and `<picture>` appear ZERO times across the five pages.
The only SVG on any page is UI furniture: the nav chevron, the rail tick, the
drawn equation arrow (b8-01 and b8-03 only), the endmatter link arrows and the
ladder marks. §4.10 allows an empty `figures` for a lesson carried by its
interactives. NOTES-B8 flag 21 names a mitochondrion and a labelled
leaf-and-lung gas-flow figure as the obvious candidates and records that neither
is in `docs/ks3/diagram-manifest.md`. Nothing is declared, because declaring a
slot means writing a caption and a caption would pre-empt the ruling flag 21
asks for. Mide's to rule on; the flag is not dropped.

── Misconceptions: the `RESP` family, opened by this unit ───────────────

`RESP-01`..`RESP-10`, two per lesson, written into
`docs/ks3/misconception-register.md` by the ENGINE pass before any authoring
pass named one. `RESP-11`..`RESP-15` are pre-allocated one per lesson as spares;
any that go unclaimed stay **permanently unused** — the same discipline as
`PLANT-09`..`12`, `DRUG-07` and `REPRO-17`/`20`/`21`/`23`.

⚑ NOTES-B8 §5 states these ten were already written into the register with a new
prefix row. **They were not** — the file carried fourteen prefixes and no `RESP`
row of any kind when B8 was picked up. `NOTES-B5` and `NOTES-B7` made the same
claim about `REPRO` and `PLANT`. Third occurrence; one process note rather than
ten.
"""

import importlib
import pkgutil

# Instrument block types seen in authored B8 data, mapped to the §5.1.1 segment
# they render as — measured from Design's markup, see the table above.
#
# ⚠️ Written in ONE pass, by the engine pass, deliberately. Five authors worked
# this unit in parallel and this dict is the one file they would all have had to
# edit; parallel writes to a single dict lose entries silently, and a lost entry
# here does not fail the build — it renders the instrument as an unlifted block
# and the page ships a bare list past a green kinds gate.
_INSTRUMENT_SEGMENTS = {
    "mass-ledger":   "practical",
    "cell-demand":   "practical",
    "oxygen-debt":   "practical",
    "fermenter":     "practical",
    "route-decider": "practical",
}

# Keys that stay on the BLOCK when an instrument is lifted, because they
# describe where the block sits in the document rather than what the
# instrument does.
_BLOCK_KEYS = ("type", "anchor", "id", "ground")


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

        payload = {k: v for k, v in block.items() if k not in _BLOCK_KEYS}
        payload.update({"id": act_id, "kind": kind})
        payload.setdefault("demand", "investigate")
        acts.append(payload)

        shell = {"type": segment, "id": act_id, "anchor": block.get("anchor")}
        # `ground` is a property of the BLOCK Design drew, not of the instrument
        # inside it, so it stays on the shell.
        if block.get("ground"):
            shell["ground"] = block["ground"]
        out.append(shell)

    lesson["core"] = out
    lesson["activities"] = acts
    return lesson


def lessons():
    """The authored B8 lesson records, in slot order, normalised.

    A slot with no module here renders an honest coming-soon page — that is the
    structure-first guarantee (§11 decision 8) and not a gap to be apologised
    for. B8 reaches five of five.
    """
    found = []
    for mod in sorted(m.name for m in pkgutil.iter_modules(__path__)):
        if not mod.startswith("lesson_"):
            continue
        m = importlib.import_module("%s.%s" % (__name__, mod))
        record = getattr(m, "LESSON", None)
        if record is not None:
            found.append(_normalise(dict(record)))
    return found
