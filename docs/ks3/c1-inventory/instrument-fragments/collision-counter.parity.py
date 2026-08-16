# Splice point: `COMPONENTS` in ks3_parity.py, in a new
# "C1 · Particles and their behaviour (⊕ MRB-228)" section.
#
# Requires one page constant beside the C2 ones (~line 360):
#
#     C1_PRESSURE = "chemistry/particles-and-their-behaviour/gas-pressure.html"
#
# Every row below uses the EXISTING `bench-gate-opened` drive: the bench does
# not exist in the document's layout until the commit gate is answered, so a
# measurement without it would report on an element that is `hidden`.
#
# Each row pins the property that makes the component DISTINCT, in the sense
# the file's own rule requires — break the CSS rule deliberately and the row
# fails.

    # ══ C1 · Particles and their behaviour (⊕ MRB-228) ═══════════════════

    # ── collision-counter (c1-04 #s-bench) ──
    # ⚠️ A LIGHT block. This is the row that catches the whole instrument
    # being mapped to `practical`: the frame's rule is 2px INK on a card
    # ground, and on ink it would report `#C6B9A7` over `#221E1B` — the
    # canvas's own cream drawing in a black surround, and every label in the
    # control strip resolving to its on-dark value.
    dict(name="counter canvas frame is a 2px INK rule on a card radius",
         on=C1_PRESSURE, drive="bench-gate-opened", sel=".ks3-counter-stage",
         props={"background-color": "#FFFCF5", "border-top-color": "#221E1B",
                "border-top-width": "2px", "border-top-left-radius": "22px",
                "overflow-x": "hidden"}),
    # The control strip is INSET, not card: it has to read as the bench's
    # panel rather than as more of the drawing above it, and the 2px ink rule
    # between them is the join.
    dict(name="counter control strip is inset under a 2px ink rule",
         on=C1_PRESSURE, drive="bench-gate-opened",
         sel=".ks3-counter-controls",
         props={"background-color": "#F7EFE1", "border-top-color": "#221E1B",
                "border-top-width": "2px"}),
    # Three captioned groups in one instrument. The captions are the only
    # thing telling a student that the second group is not more of the first
    # — the same argument as `muscle-pair`'s, with a third group.
    dict(name="counter group caption is a mono ink-muted label",
         on=C1_PRESSURE, drive="bench-gate-opened",
         sel=".ks3-counter-grouplabel",
         props={"font-family": "DM Mono", "font-size": "12px",
                "color": "#5F564F", "text-transform": "uppercase"}),
    # ⚖️ The live note takes the BAND-on-ink treatment — the KEY FACT
    # treatment, deliberately, and deliberately NOT a verdict tone. It is the
    # sentence the bench just proved, not a mark on anything the student did.
    # If it ever resolves to the accent tint it starts reading as feedback.
    dict(name="counter note is BAND on a 2px ink border, never a verdict tone",
         on=C1_PRESSURE, drive="bench-gate-opened", sel=".ks3-counter-note",
         props={"background-color": "#F4E9D8", "border-top-color": "#221E1B",
                "border-top-width": "2px", "font-size": "19px",
                "color": "#221E1B"}),
