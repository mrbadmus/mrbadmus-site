# ks3_parity.py — gap-test-rig (c1-01 #s-gap)
#
# Uses the same C1_MODEL constant the halving-bench fragment adds.
#
# DRIVES — two, and both are required before the rows below can be spliced
# (`_unregistered_drives()` is fatal). The rig does not exist until a claim has
# been made about what it will show, so every state here is behind a click.
#
#     "gap-answered": r"""
# (function () {
#   var wrap = document.querySelector('[data-gap]');
#   if (!wrap) { return "no gap rig on the page"; }
#   var opt = wrap.querySelector('.ks3-option');
#   if (!opt) { return "the rig offers no choices"; }
#   opt.click();
#   var rig = wrap.querySelector('[data-gap-rig]');
#   if (!rig || rig.hasAttribute('hidden')) {
#     return "a choice was made and the rig never appeared";
#   }
#   return "";
# })()
# """,
#
#     "gap-tested": r"""
# (function () {
#   var wrap = document.querySelector('[data-gap]');
#   if (!wrap) { return "no gap rig on the page"; }
#   // The choice that FILLS the gap, so the test lands on its `off` outcome —
#   // the failure that is the whole argument of the block.
#   var empty = parseInt(wrap.getAttribute('data-empty-choice'), 10);
#   var opts = wrap.querySelectorAll('.ks3-option');
#   var pick = opts[empty === 0 ? 1 : 0];
#   if (!pick) { return "the rig offers no choices"; }
#   pick.click();
#   var t = wrap.querySelector('.ks3-gap-test');
#   if (!t) { return "the rig offers no tests"; }
#   t.click();
#   if (t.getAttribute('aria-pressed') !== 'true') {
#     return "a test was run and its button never lit";
#   }
#   var sec = document.getElementById('s-gap');
#   if (!sec || sec.getAttribute('data-stage-done') !== '1') {
#     return "a test was run and the stage never completed";
#   }
#   return "";
# })()
# """,
#
# COMPONENTS — four rows.

    # ── gap-test-rig (c1-01 #s-gap) ──
    # ⚠️ Both text rows exist to prove the SPECIFICITY scoping. `.ks3-dark p`
    # is (0,1,1) and a bare instrument class is (0,1,0): unscoped, the caption
    # and the outcome paragraph both lose to the block they sit in and render
    # in its body colour. That defect shipped with the zoom instrument on B1
    # and bit B2 again, which is why it is pinned rather than assumed.
    dict(name="gap control caption is mono 12px uppercase on-dark-muted",
         on=C1_MODEL, drive="gap-answered", sel=".ks3-gap-caption",
         props={"font-family": "DM Mono", "font-size": "12px",
                "color": "#C6B9A7", "text-transform": "uppercase"}),
    dict(name="gap outcome is on-dark BODY, not the block's own colour",
         on=C1_MODEL, drive="gap-answered", sel=".ks3-gap-note p",
         props={"color": "#E7DECE", "font-size": "19px"}),
    # The dark branch of the segmented control, resting: on-dark text on the
    # muted rule. If this resolves to ink the rig has been painted as a light
    # instrument and the buttons vanish into the block.
    dict(name="a gap test at rest is on-dark text on the muted rule",
         on=C1_MODEL, drive="gap-answered", sel=".ks3-gap-test",
         props={"color": "#FBF3E6", "border-top-color": "#C6B9A7",
                "border-top-width": "2px", "min-height": "44px"}),
    # ⚖️ The RUNNING test is the alert amber with ink on it — the shipped dark
    # pressed state, measured in the state through the rig's own controls.
    # Amber here is not a verdict on the student: it marks which test is on the
    # bench, and the outcome paragraph is one tone whichever answer they gave.
    dict(name="the running gap test is alert amber with ink on it",
         on=C1_MODEL, drive="gap-tested",
         sel='.ks3-gap-test[aria-pressed="true"]',
         props={"background-color": "#FFC53D", "color": "#221E1B",
                "border-top-color": "#FFC53D"}),
