"""P7 — *Light*, as one module per lesson.

Seven lessons, a complete unit. The package layout follows `ks3_data/p6/`
exactly.

Every lesson is authored against Claude Design's delivered pages in
`docs/ks3/design-reference/p7/`. Her page wins outright: the hooks, the
bench gates, the branch notes, every ladder rung and both attempt panels
are ported from her `RAIL`, `DONE()`, `RUNGS`, `SELF_RUNGS`, `CFIFA_EX`
and `lessonVals()` — never inferred from her HTML, which renders all of
them from `{{ }}` holes and would report a match against anything.

── ⚖️ THE OWNERSHIP MAP — SIX STATEMENTS OVER SEVEN SLOTS ─────────────

    p7-01  light-travels               LGT.01 whole + LGT.02 whole
    p7-02  reflection-mirrors-and-...  LGT.03a "diffuse scattering and
                                       specular reflection at a surface"
                                       + LGT.04a "imaging in mirrors"
    p7-03  refraction                  LGT.04b "the refraction of light"
    p7-04  lenses-and-images           LGT.04c "the pinhole camera, and the
                                       action of a convex lens in focusing"
    p7-05  the-eye-and-the-camera      LGT.04d "the human eye" + LGT.05 whole
    p7-06  colour-and-the-spectrum     LGT.06a "colours and the different
                                       frequencies of light; white light and
                                       prisms (qualitative only)"
    p7-07  why-things-look-coloured    LGT.03b "absorption" + LGT.06b
                                       "differential colour effects"

The `.a` / `.b` / `.c` / `.d` sub-IDs are minted in
`ks3_data/substatements.py` under the rule that file already carries.
`LGT.04` takes the widest split in the key stage — four clauses, four
lessons — which is exactly the case Design's FLAG 1 predicted a coverage
gate would read as one statement claimed four times.

── ⚖️ HER §3 FORMULA RULINGS, KEPT ────────────────────────────────────

`p7-01` takes a TRIANGLE for `d = c × t`. `p7-02` takes a BALANCE BEAM
for `r = i` — an equality is not a product and not a sum, so there is
nothing to cover and the beam carries no cover buttons (the `p1-08`
precedent). Every other lesson carries no block.

── ⚖️ HER FLAG 4 STANDS, AND IT IS MIDE'S ────────────────────────────

`p7-04` computes an image height. `h_image = h_object × (v ÷ u)` is a
genuine product and would take a triangle cleanly; she leaves it out
because `LGT.04` says *qualitative* for the convex lens, the pinhole
clause carries no arithmetic at all, and a triangle over three lengths
invites magnification, which is GCSE. The bench prints its working in the
readout sub-line (`300 mm × v ÷ u`) instead.

**"This is the one place in the two units where a reviewer might
reasonably want a block that is not there."** That is her sentence and it
is passed through unresolved.

── ⚖️ HER FLAG 8: `p7-05`'s BENCH HOLDS TWO INSTRUMENTS ──────────────

An eye and a camera, switched by a toggle that redraws the whole
cross-section. It brushes against "one practical per bench" and it is
deliberate: the comparison IS the lesson, the toggle names which
instrument is drawn, and a student is never left with two answers to
"describe the apparatus". Built as drawn; she asks a reviewer to ratify
it or ask for two figures instead.

── ⚠️ HER FLAG 10: `p7-06` AND `p7-07` USE HUE AS PART OF THE MESSAGE ─

Colour is the subject, so it cannot be avoided. Every state also carries
the colour AS A WORD in a readout tile and in the note, the ladder is
answerable from the words alone, and the legal line declares the screen
colours as approximations of spectral colours. Two channels, always.

── ⚠️ "ALMOST BLACK", NEVER "BLACK" ──────────────────────────────────

Everywhere in `p7-07` where a surface has nothing to send back. Real dyes
and real lamps are broad bands and the perfect case does not occur; her
legal line says so and the word is load-bearing rather than a hedge to be
tidied.

── FOUR RAIL STOPS PER LESSON ────────────────────────────────────────

Measured off Design's own `RAIL` constant on each page:

    p7-01  s-hook s-race   s-formula s-ladder
    p7-02  s-hook s-ray    s-beam    s-ladder
    p7-03  s-hook s-block  s-inout   s-ladder
    p7-04  s-hook s-camera s-lens    s-ladder
    p7-05  s-hook s-eye    s-parts   s-ladder
    p7-06  s-hook s-prism  s-band    s-ladder
    p7-07  s-hook s-lamp   s-grid    s-ladder

⚠️ **FIVE BAND STOPS TICK EARLIER THAN THEIR BENCH.** On `p7-03` …
`p7-07` Design's `DONE` gives the band section `s.gate !== null` while
the bench needs the gate AND a control touched. Each bench marks its own
sibling through `band_anchor` / `band_at`, as in P4 and P6.
`mirrors` would tick them LATE and the manifest derives no mirror for
them — her two expressions differ, so they are not a mirror pair.

⚠️ **MRB-208** — on `p7-01` and `p7-02` the formula stop goes on the
ATTEMPT PANEL, because `s.buildOpen` is what her own `DONE` reads and
`buildOpen` is set by the attempt panel's Check button.

── ⚖️ THE `LIGHT` FAMILY OPENS HERE ──────────────────────────────────

See the ruling in `docs/ks3/misconception-register.md`. `LIGHT-01` …
`LIGHT-28` are minted by these seven lessons.

── ⊕ ONE HEAD ROW PER BENCH, AND IT IS THE ENGINE'S ──────────────────

P4, P5 and P6 each author `eyebrow`, `heading` and `progress` on the
activity AND draw a second head row inside the instrument, so every bench
in those three units ships its eyebrow and its `<h2>` TWICE — measured in
the built bytes of `pressure-force-over-area.html` and
`sound-needs-a-medium.html`, not inferred.

P7 does not. `r_activity`'s `.ks3-blockhead` IS Design's row — eyebrow
and heading on the left, a right-aligned mono readout on the right — and
it is what MRB-220 built the head counter for. So every P7 bench authors
`head_counter` with Design's own two states and the drawers emit no head
of their own; the wiring drives the shared `[data-count]` element through
`setCount`. One eyebrow, one heading, one readout, in her layout.
"""

import importlib
import pkgutil

_INSTRUMENT_SEGMENTS = {
    # Every P7 bench is `ks3-block ks3-dark ks3-practical`.
    "two-speed-race":   "practical",
    "ray-surface":      "practical",
    "refraction-block": "practical",
    "pinhole-camera":   "practical",
    "eye-camera":       "practical",
    "prism-bench":      "practical",
    "colour-bench":     "practical",
    # The fixed figures are bare `ks3-block` on the band ground.
    "light-band":       "check",
}

# ⚠️ `p7-attempt` IS NOT IN THE TABLE ABOVE, for the same reason it is not
# in P4's, P5's or P6's: it is authored in `activities[]` beside the worked
# examples and placed in `core` as a `check` naming its id.

_BLOCK_KEYS = ("type", "anchor", "id")


def _normalise(lesson):
    """Lift inline instrument blocks into `activities[]`. Returns the lesson."""
    core = lesson.get("core") or []
    acts = list(lesson.get("activities") or [])
    known = {a.get("id") for a in acts}
    out = []

    for block in core:
        kind = block.get("type")
        segment = _INSTRUMENT_SEGMENTS.get(kind)
        if segment is None:
            out.append(block)
            continue

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
        out.append({"type": segment, "id": act_id,
                    "anchor": block.get("anchor")})

    lesson["core"] = out
    lesson["activities"] = acts
    return lesson


def lessons():
    """The authored P7 lesson records, in slot order, normalised."""
    found = []
    for mod in sorted(m.name for m in pkgutil.iter_modules(__path__)):
        if not mod.startswith("lesson_"):
            continue
        m = importlib.import_module("%s.%s" % (__name__, mod))
        record = getattr(m, "LESSON", None)
        if record is not None:
            found.append(_normalise(dict(record)))
    return found
