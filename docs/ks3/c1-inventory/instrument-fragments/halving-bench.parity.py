# ks3_parity.py — halving-bench (c1-01 #s-cut)
#
# 1. PAGE CONSTANT — add beside C2_ATOM / C2_ELEM (~line 357):
#
#        C1_MODEL = "chemistry/particles-and-their-behaviour/particle-model.html"
#
# 2. DRIVE — add to DRIVES. ⚠️ `_unregistered_drives()` is FATAL, so the rows
#    below cannot be spliced without it. `bench-gate-opened` already exists and
#    is reused; this second one reaches the floor through the bench's own
#    controls, so a regression in the interaction path fails HERE rather than
#    being measured around.
#
#     "cut-floor-reached": r"""
# (function () {
#   var gate = document.querySelector('[data-benchgate]');
#   if (!gate) { return "no commit gate on the page"; }
#   gate.querySelector('.ks3-option').click();
#   var bench = document.querySelector('[data-cut]');
#   if (!bench) { return "the bench did not appear after the gate"; }
#   var floor = parseInt(bench.getAttribute('data-floor'), 10) || 0;
#   var ten = bench.querySelector('.ks3-cut-btn[data-step="10"]');
#   var one = bench.querySelector('.ks3-cut-btn[data-step="1"][data-act="cut"]');
#   if (!ten || !one) { return "the bench offers no cut controls"; }
#   for (var i = 0; i < floor; i++) {
#     if (!ten.hasAttribute('disabled')) { ten.click(); }
#     else if (!one.hasAttribute('disabled')) { one.click(); }
#     else { break; }
#   }
#   var count = bench.querySelector('[data-cut-out="count"]');
#   if (!count || parseInt(count.textContent, 10) !== floor) {
#     return "cutting stopped at " + (count && count.textContent) +
#            " of " + floor;
#   }
#   if (!document.querySelector('[data-verdict="floor"]:not([hidden])')) {
#     return "the floor was reached and the verdict never changed";
#   }
#   return "";
# })()
# """,
#
# 3. COMPONENTS — the four rows below. Each was chosen because it is the
#    property that makes this instrument DISTINCT; the mono readout LABEL is
#    deliberately not among them, because it is the shipped mono caption that
#    `.ks3-joint-tile-mono` and the budget line already pin.

    # ══ C1 · Particles and their behaviour (⊕ MRB-228) ═══════════════════

    # ── halving-bench (c1-01 #s-cut) ──
    # ⚠️ A LIGHT instrument, and this row is what proves it. Its sibling
    # `#s-gap` on the same page is ink-dark and uses `.ks3-canvas-frame`; if
    # this frame ever resolves to the muted rule (#C6B9A7) the bench has been
    # mapped onto the dark frame and every text token inside it is wrong.
    dict(name="cut bench frame is a 2px INK rule on the card ground",
         on=C1_MODEL, drive="bench-gate-opened", sel=".ks3-cut-frame",
         props={"background-color": "#FFFCF5", "border-top-color": "#221E1B",
                "border-top-width": "2px", "border-top-left-radius": "22px"}),
    # The readouts are the lesson — "watch the size, not the picture" — so they
    # are display type at 30px, not the 25px mono a sim readout takes. If this
    # row ever reports the mono face, the numbers have stopped being the
    # headline of the block.
    dict(name="cut readout value is display 700 30px ink", on=C1_MODEL,
         drive="bench-gate-opened", sel=".ks3-cut-value",
         props={"font-family": "Bricolage Grotesque", "font-weight": "700",
                "font-size": "30px", "color": "#221E1B"}),
    # ⚖️ The floor verdict is accent-TEXT and never the accent itself: it is
    # read at 30px but it is a state word, and #E4572E is 3.4:1. Measured in
    # the state, through 24 real cuts.
    dict(name="the floor verdict is accent-text, not the accent", on=C1_MODEL,
         drive="cut-floor-reached",
         sel='.ks3-cut-value [data-verdict="floor"]',
         props={"color": "#A93411"}),
    # ⚖️ The running note is a BAND panel on a 2px ink border — the same
    # treatment `claim-switch`'s note takes, and deliberately not amber. Amber
    # is a wrong idea being confronted; this paragraph is the state of the
    # model, and a student who has cut nothing has made no mistake.
    dict(name="cut note is a band panel on ink, never amber", on=C1_MODEL,
         drive="bench-gate-opened", sel=".ks3-cut-note",
         props={"background-color": "#F4E9D8", "border-top-color": "#221E1B",
                "border-top-width": "2px"}),
