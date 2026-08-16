# ── PAGE CONSTANT ────────────────────────────────────────────────────────
# Shares C1_TEST with the other two c1-06 instruments:
#
# C1_TEST = "chemistry/particles-and-their-behaviour/testing-the-model.html"


# ── COMPONENTS entries ───────────────────────────────────────────────────
# Every row was mutation-tested: the rule was deliberately broken in
# shared/ks3.css and the row confirmed to fail before it was kept.

    # ── model-timeline (c1-06 #s-history) ──
    #
    # ⚠️ THE THIRD CONTROL GEOMETRY. `.ks3-seg-btn` and `.ks3-sim-seg-btn` are
    # both centred single lines; this one is LEFT-ALIGNED at `10px 14px`. If it
    # ever resolves to `center`, the year and the name stop stacking against a
    # common left edge and the five positions cannot be read down the row —
    # which is the whole reason it was not folded into `seg()`.
    dict(name="timeline step is a LEFT-ALIGNED 44px control", on=C1_TEST,
         sel=".ks3-mtl-step",
         props={"text-align": "left", "min-height": "44px",
                "padding-left": "14px", "padding-top": "10px",
                "background-color": "#FBF3E6",
                "border-top-color": "#DDCFB6"}),
    # The two-line stack. `display: block` on the year is the only thing making
    # the button two lines; inline, the year and the name run together and the
    # control collapses into a long label.
    dict(name="timeline year is a mono line of its own", on=C1_TEST,
         sel=".ks3-mtl-year",
         props={"display": "block", "font-family": "DM Mono",
                "font-size": "12px"}),
    # The chosen step takes the accent tint and nothing else — R3: it shows it
    # was chosen, and there is nothing here to be right or wrong about.
    dict(name="the open model takes the accent tint, never a verdict",
         on=C1_TEST, sel='.ks3-mtl-step[aria-pressed="true"]',
         props={"background-color": "#FCE7DE", "border-top-color": "#E4572E"}),
    # 26px display, and the muted rule-topped line under it. The claim has to
    # out-rank the body from the scroll position; "What broke it:" has to
    # survive being skimmed, which is why the label is ink and the line is not.
    dict(name="timeline claim is display 700 at 26px", on=C1_TEST,
         sel=".ks3-mtl-claim",
         props={"font-family": "Bricolage Grotesque", "font-weight": "700",
                "font-size": "26px"}),

# ⊖ No drive. The default card is open at rest — the row opens on Dalton, not
# on Democritus — so every measured selector exists in the resting document.
# That is itself worth knowing: if `default_index` ever stopped being honoured,
# `.ks3-mtl-step[aria-pressed="true"]` would match nothing and the row above
# would report a missing selector rather than passing quietly.
