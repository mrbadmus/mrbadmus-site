"""P6 — *Waves and sound*, as one module per lesson.

Nine lessons, a complete unit. The package layout follows `ks3_data/p4/`
and `ks3_data/p5/` exactly.

Every lesson is authored against Claude Design's delivered pages in
`docs/ks3/design-reference/p6/`. Her page wins outright.

── ⚖️ THE OWNERSHIP MAP — SIX STATEMENTS OVER NINE SLOTS ──────────────

P6 is the SURPLUS-SLOT case again, and more so than P5: six statements,
nine lessons, ratio 0.67. Three of the six are compound and are split at
the clause; the other three are whole.

    p6-01  waves-on-water           OBW.01a "undulations which travel
                                    through water with transverse motion"
    p6-02  transverse-waves-...     OBW.01b "reflected" + OBW.01c "add or
                                    cancel – superposition"
    p6-03  how-sound-is-made        SND.03a "produced by vibrations of
                                    objects, in loudspeakers" + SND.03b
                                    "detected by their effects on
                                    microphone diaphragm and the ear drum"
    p6-04  sound-is-longitudinal    SND.03c "sound waves are longitudinal"
    p6-05  frequency-pitch-...      SND.01a "frequencies of sound waves,
                                    measured in hertz (Hz)"
    p6-06  sound-needs-a-medium     SND.02 whole
    p6-07  echoes-reflection-...    SND.01b "echoes, reflection and
                                    absorption of sound"
    p6-08  hearing-and-auditory-... SND.04 whole
    p6-09  ultrasound-at-work       EAW.01 whole

The `.a` / `.b` / `.c` sub-IDs are minted in `ks3_data/substatements.py`
under the rule that file already carries. This is the third unit in this
run to use it; see the P4 package note for why Design's FLAG 1 asked for a
notation that already existed.

── ⚖️ HER FLAG 2 IS HONOURED: `p6-01` NAMES NO FREQUENCY ──────────────

A wave has one, and `p6-01` is about the SHAPE of a wave rather than its
rate. A hertz readout on the ripple tank would make it a second claimant
of `SND.01`, which `p6-05` owns. The tank reports amplitude and wavelength
in millimetres and describes the paddle rate in words only —
`r_ripple_tank` refuses a payload carrying a frequency at all.

`p6-03` DOES report "how many times a second" for each source, because the
alternative is a bench that names a quantity it will not let a student
read. It teaches no pitch and claims no clause of `SND.01`. Design asks a
reviewer who reads Hz-anywhere as a claim to say so; it is a two-line
change.

── ⚖️ HER FLAG 3 STANDS, AND IT IS MIDE'S ────────────────────────────

`p6-09` computes a depth from an echo time — `d = v × t` followed by
halving — and carries NO formula block. `p6-06` owns that triangle and
`p6-07` owns the halving bar, one and two lessons back, and a third speed
block in the same unit would be the fourth `d = v × t` triangle in two
units. The gauge prints its own working line by line and both owning
lessons are carried as edges.

**If the contract requires a block wherever a page computes, `p6-09` needs
one and it will be a duplicate.** That is her sentence and it is a ruling,
not a lane's call.

── ⚖️ HER FLAG 5: `d = v × t` APPEARS THREE TIMES, AND THAT IS KEPT ───

`p6-06` teaches it, `p6-07` uses it inside a worked example as given data,
and `p7-01` will teach it again for light. No lesson assumes the others:
each states the relationship from nothing and carries the others as edges.
She asks a reviewer to check it reads as reinforcement rather than as a
missing single-source ruling. Nothing here changes it.

── ⊖ HER FLAG 6: THE STEEL SPEED IS 5000 m/s AND STAYS ───────────────

Published values run 5000–5900 m/s. She uses 5000 in both `p6-06` and
`p6-09` for consistency, and `p6-09`'s legal line states the range. Kept:
the number is declared, the two pages agree, and standardising on 5900
would need both pages and one rung changing together — which is a
corpus-wide decision, not a P6 one.

── ⚠️ HER FLAG 7: THE AUDITORY RANGES ARE CONTESTED, AND SAY SO ──────

Human 20–20 000, dog 67–45 000, cat 45–64 000, bat 2000–110 000, elephant
16–12 000, mouse 1000–91 000. These are the commonly published set, and
studies disagree partly because they disagree about how quiet a sound must
be before an animal counts as hearing it. The foot line says so. She marks
this *"contested enough to be worth a reviewer's source of record"*, and
it is flagged rather than resolved.

── ⚖️ SAFEGUARDING ON `p6-08` AND `p6-09` ────────────────────────────

Both carry Childline and 0800 1111 inline, in small type, at the bottom
edge above the legal line, through the engine's `safeguarding_note` slot —
which is exactly the treatment §8.10 rules for it. `p6-08` because hearing
damage is the student's own body and the loss is permanent; `p6-09`
because a scan is a thing to be anxious about. This closes audit finding
6.4 for two of the three pages she names; the third is `p7-05`, which is
P7's.

── FOUR RAIL STOPS PER LESSON ────────────────────────────────────────

Measured off Design's own `RAIL` constant on each page:

    p6-01  s-hook s-parts  s-tank    s-ladder
    p6-02  s-hook s-meet   s-bar     s-ladder
    p6-03  s-hook s-stages s-chain   s-ladder
    p6-04  s-hook s-slinky s-compare s-ladder
    p6-05  s-hook s-signal s-formula s-ladder
    p6-06  s-hook s-range  s-formula s-ladder
    p6-07  s-hook s-cliff  s-bar     s-ladder
    p6-08  s-hook s-range  s-chart   s-ladder
    p6-09  s-hook s-gauge  s-uses    s-ladder

⚠️ **THREE BAND STOPS TICK EARLIER THAN THEIR BENCH** — `s-compare`,
`s-chart` and `s-uses` all take `gate !== null` while the bench needs the
gate AND a control touched. Each bench marks its own sibling, as in P4;
`mirrors` would tick them late.

⚠️ **`p6-03`'s `s-stages` TICKS ON THE HOOK**, not on the bench: Design's
`DONE` reads `if (id === 's-stages') return s.hookChoice !== null`. It sits
ABOVE the bench on her page, which is why. Measured, not inferred.

⚠️ **MRB-208** — on `p6-02`, `p6-05`, `p6-06` and `p6-07` the formula stop
goes on the ATTEMPT PANEL, because `s.buildOpen` is what her own `DONE`
reads.

── ⚖️ THE `WAVE` FAMILY OPENS HERE ───────────────────────────────────

See the ruling in `docs/ks3/misconception-register.md`. `WAVE-01` …
`WAVE-36` are minted by these nine lessons.
"""

import importlib
import pkgutil

_INSTRUMENT_SEGMENTS = {
    # Every P6 bench is `ks3-block ks3-dark ks3-practical`.
    "ripple-tank":         "practical",
    "superposition-lanes": "practical",
    "vibration-chain":     "practical",
    "slinky-dual":         "practical",
    "scope-trace":         "practical",
    "medium-range":        "practical",
    "echo-range":          "practical",
    "log-range":           "practical",
    "flaw-gauge":          "practical",
    # The band sections and the anatomy figure are bare `ks3-block`.
    "wave-anatomy":        "check",
    "wave-band":           "check",
}

# ⚠️ `p6-attempt` IS NOT IN THE TABLE ABOVE, for the same reason it is not
# in P4's or P5's: it is authored in `activities[]` beside the two worked
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
    """The authored P6 lesson records, in slot order, normalised."""
    found = []
    for mod in sorted(m.name for m in pkgutil.iter_modules(__path__)):
        if not mod.startswith("lesson_"):
            continue
        m = importlib.import_module("%s.%s" % (__name__, mod))
        record = getattr(m, "LESSON", None)
        if record is not None:
            found.append(_normalise(dict(record)))
    return found
