# PAGE CONSTANT (add beside the other C1 page constants in ks3_parity.py):
#
#     C1_STATE = "chemistry/particles-and-their-behaviour/changes-of-state.html"
#
# DRIVE: none new. The bench lives behind C6's commit gate, so every row below
# that measures the instrument itself uses the SHIPPED `bench-gate-opened`
# drive; `#s-curve` is the only gate on this page, which is what that drive
# selects. The mass tile is measured on the same driven load.

    # ── heating-bench (c1-03 #s-curve) ──
    # ⚠️ A LIGHT bench. If the frame row ever reports `#3E3730` or the note
    # row reports on-dark body copy, the instrument has been mapped to
    # `practical` and the graph's paper has become a hole in an ink block —
    # the exact trap the payload map names for this lesson.
    dict(name="heating bench frame is a 2px INK rule on a card ground",
         on=C1_STATE, drive="bench-gate-opened", sel=".ks3-hb-frame",
         props={"background-color": "#FFFCF5", "border-top-color": "#221E1B",
                "border-top-width": "2px", "border-top-left-radius": "22px",
                "overflow-x": "hidden"}),

    # ⚖️ THE CONSTANT IS A FULL READOUT. `Mass in the flask · 50.0 g` is
    # hard-coded markup and it is the confrontation of the lesson, so it is
    # asserted at the same 30px display type as the two tiles that DO move.
    # If it ever resolves as a caption, the one number that says nothing was
    # lost has been quietly demoted below the two that change.
    dict(name="the constant mass reads as a full display-type readout",
         on=C1_STATE, drive="bench-gate-opened", sel=".ks3-hb-mass",
         props={"font-family": "Bricolage Grotesque", "font-size": "30px",
                "font-weight": "700", "color": "#221E1B"}),

    # 44px of control around a 10px track, and the reset appearance is what
    # makes it a drawn control rather than a browser default. No `width`: it
    # is 100% of a column whose px value follows the viewport, and this
    # harness pins none.
    dict(name="the scrub clears the 44px tap target", on=C1_STATE,
         drive="bench-gate-opened", sel=".ks3-hb-scrub",
         props={"height": "44px", "appearance": "none",
                "accent-color": "#E4572E"}),

    # The plateau note takes the KEY FACT treatment — band on a 2px ink rule
    # — because the sentence it carries while the thermometer is stuck is the
    # fact the lesson exists to deliver. Never amber: this is not a wrong
    # idea being confronted.
    dict(name="the plateau note is a BAND panel on ink", on=C1_STATE,
         drive="bench-gate-opened", sel=".ks3-hb-note",
         props={"background-color": "#F4E9D8", "border-top-color": "#221E1B",
                "border-top-width": "2px", "font-size": "19px",
                "color": "#221E1B"}),
