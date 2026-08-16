# ks3_parity.py — COMPONENTS entries for `random-walk-bench` (c1-05 #s-walk).
#
# Needs the page constant, beside the C2 block near line 362:
#
#     # ⊕ C1 · Particles and their behaviour (rebuild, MRB-228). Same rule
#     # again: a component is registered on the page that RENDERS it. Both new
#     # C1 kinds live only on c1-05, so both are measured there.
#     C1_DIFF = "chemistry/particles-and-their-behaviour/diffusion.html"
#
# `bench-gate-opened` is the existing generic drive and needs no new entry:
# c1-05 has exactly one `[data-benchgate]`, and the bench is `hidden` until it
# is answered, so three of the four rows below cannot be measured without it.
#
# ⚠️ NOT mutation-tested by the authoring agent — no browser in this run. Each
# row names the property that makes its component distinct and would resolve to
# a different value if the rule were dropped; the commander should break each
# rule once and confirm the row fails before these are kept.

    # ══ C1 · Particles and their behaviour (⊕ MRB-228) ═══════════════════

    # ── random-walk-bench (c1-05 #s-walk) ──
    # ⚠️ A LIGHT block, and this row is the guard on that. The frame is
    # `--ks3-card` on a 2px INK rule; if it ever reports `#C6B9A7` the bench
    # has been mapped onto `.ks3-canvas-frame`, which is the DARK twin, and the
    # tank ends up outlined in an on-dark colour on cream. If it reports
    # `#221E1B` as the BACKGROUND, the block has been mapped to `practical`
    # and every text token in the instrument resolves wrong.
    dict(name="walk frame is a card on a 2px ink rule, not the dark frame",
         on=C1_DIFF, drive="bench-gate-opened", sel=".ks3-walk-frame",
         props={"background-color": "#FFFCF5", "border-top-color": "#221E1B",
                "border-top-width": "2px", "border-top-left-radius": "22px"}),

    # ⚖️ THE TWO COUNTERS ARE THE LESSON. They are display 700 at 30px so that
    # a student can watch them climb side by side after the tank has evened
    # out — the confrontation of PART-11 is a comparison between two numbers,
    # and a caption-sized readout is a number you check rather than watch.
    # `tabular-nums` is what stops them jittering sideways as they gain digits.
    dict(name="crossing counters are display 700 30px, tabular",
         on=C1_DIFF, drive="bench-gate-opened", sel=".ks3-walk-readout-value",
         props={"font-family": "Bricolage Grotesque", "font-weight": "700",
                "font-size": "30px", "color": "#221E1B",
                "font-variant-numeric": "tabular-nums"}),

    # The live note takes the KEY FACT treatment — band on a 2px ink border —
    # deliberately, and not a tint or a dim: the bench is telling the student
    # what they are looking at, and it is never marking them.
    dict(name="walk note is a band panel on ink", on=C1_DIFF,
         drive="bench-gate-opened", sel=".ks3-walk-note",
         props={"background-color": "#F4E9D8", "border-top-color": "#221E1B",
                "border-top-width": "2px"}),

    # ⚖️ THE CONTRAST FIX, and the reason it is scoped rather than global.
    # `.ks3-commit` is `--ks3-alert` because every other commit in the key
    # stage sits on ink. This one sits on `--ks3-inset` cream, where amber is
    # unreadable, so the block repaints it `--ks3-accent-text` — the 6:1
    # orange. No `drive`: the gate is what the page opens on.
    dict(name="the light bench's commit is accent-TEXT, never the amber",
         on=C1_DIFF, sel=".ks3-walk-block .ks3-benchgate .ks3-commit",
         props={"color": "#A93411", "font-size": "22px",
                "font-weight": "700"}),
