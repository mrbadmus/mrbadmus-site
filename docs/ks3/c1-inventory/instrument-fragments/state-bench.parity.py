# ks3_parity.COMPONENTS entries for `state-bench` (c1-02 #s-bench).
#
# The page constant this needs does not exist yet — add it beside the other
# per-lesson constants (ks3_parity.py ~line 357, where C2_ATOM … C2_MASS live):
#
#     C1_STATES = "chemistry/particles-and-their-behaviour/solids-liquids-and-gases.html"
#
# ⚠️ Not `LESSON`. That constant is c1-04 (`gas-pressure.html`), which renders
# no state bench at all — a component measured on a page without it reports
# "selector not present" and PASSES, which is the absence-of-assertion failure
# MRB-198 closed one level down.
#
# `drive="bench-gate-opened"` on all four: C6 gates the bench by ABSENCE, so
# nothing inside `[data-benchbody]` exists in the layout until the commit is
# answered. The existing driver is reused unchanged — it clicks the first
# option, asserts the gate goes and asserts the body arrives, which is exactly
# the contract `wireStateBench` implements for itself.

    # ── state-bench (c1-02 #s-bench) ──
    # ⚖️ The frame is the LIGHT twin of `.ks3-canvas-frame`, and the two must
    # not converge. If this ever resolves to `--ks3-on-dark-muted` over
    # `--ks3-dark-panel`, the bench has been repainted for an ink block that
    # c1-02 does not have — its only dark grounds are the hook and the keynote,
    # and the particle drawing is cream on cream.
    dict(name="state bench frame is CARD on a 2px ink border", on=C1_STATES,
         drive="bench-gate-opened", sel=".ks3-sbench-frame",
         props={"background-color": "#FFFCF5", "border-top-color": "#221E1B",
                "border-top-width": "2px",
                "border-top-left-radius": "22px"}),
    # ⚖️ The chosen state keeps INK text, deliberately. `.ks3-seg-btn`'s chosen
    # state goes to `--ks3-accent-text`, and on this bench the three state
    # buttons are a picker rather than an answer — accent text on the chosen
    # one would read as a verdict (R3 / MRB-196 R10). The size is C1's own
    # 16px, not drift 4's 17px; §1.6 (d) has that ruling reopened on a
    # six-pages-against-one count and this block does not pre-empt it.
    dict(name="chosen state button is accent-tint on ink text, at C1's 16px",
         on=C1_STATES, drive="bench-gate-opened",
         sel='.ks3-sbench-seg[aria-pressed="true"]',
         props={"background-color": "#FCE7DE", "border-top-color": "#E4572E",
                "color": "#221E1B", "font-size": "16px"}),
    # The panel holding whichever of the eight notes is live: BAND on a 2px ink
    # border, which is the KEY FACT treatment and deliberately not a tint. The
    # note is the sentence that settles what the student has just done, not a
    # verdict on it.
    dict(name="bench note is a BAND panel on ink", on=C1_STATES,
         drive="bench-gate-opened", sel=".ks3-sbench-note",
         props={"background-color": "#F4E9D8", "border-top-color": "#221E1B",
                "border-top-width": "2px"}),
    # ⚠️ THE SPECIFICITY GUARD, and the reason it is a row rather than a
    # comment. The text rule is `.ks3-sbench .ks3-sbench-note-text` at (0,2,0),
    # because `.ks3-dark p` is (0,1,1) and would beat a bare instrument class
    # at (0,1,0) — the defect B1 shipped with the zoom note and B2 was bitten
    # by again. c1-02 has no dark block today; this is what keeps that true if
    # the bench is ever reused on a page that does.
    dict(name="bench note text is INK body copy, not the block's own colour",
         on=C1_STATES, drive="bench-gate-opened", sel=".ks3-sbench-note-text",
         props={"color": "#221E1B", "font-size": "19px",
                "line-height": "30.4px"}),
