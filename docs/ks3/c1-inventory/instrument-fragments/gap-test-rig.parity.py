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


# ── DRIVES entries ───────────────────────────────────────────────────────
# ⊕ This section SUPERSEDES the commented sketch in this file's header.
# Splice from here; the header copy is prose and is now out of date.
#
# ⚖️ THE TWO NAMES ARE TWO REAL STATES, and the rig separates them itself.
# `wireGapTestRig` keeps `choice` and `test` as independent variables:
# choosing unhides `[data-gap-rig]` and repaints an OPENING note, and only a
# test press sets `aria-pressed="true"`, swaps the note for an OUTCOME
# paragraph, and calls `markStage(sec, true)`. So `gap-answered` and
# `gap-tested` differ in three independent ways — the pressed attribute, which
# of the eight authored paragraphs is showing, and whether the rail stop has
# ticked — and neither name is a dressed-up copy of the other.

    # A claim has been made about the gap, and NO test has been run.
    #
    # This is what makes the three resting rows measurable at all: the caption,
    # the note wrapper and the test buttons all live inside `[data-gap-rig]`,
    # which the renderer emits `hidden` because the rig is not there to be
    # looked at until the student has said what it is going to show.
    #
    # ⚠️ THE EMPTY CHOICE, DELIBERATELY, AND THE REASON IS FIRST-MATCH.
    # `.ks3-gap-note p` is measured by `document.querySelector`, which takes
    # the first match — and the renderer emits `data-note="empty"` first. Only
    # the empty choice leaves THAT paragraph the one on screen; any filled
    # choice shows `data-note="filled"` instead and the row would be measuring
    # a display:none element and passing. `data-empty-choice` is read from the
    # markup, never assumed: it is positional, and the renderer validates it
    # against the choice list at build time for exactly that reason.
    #
    # The last guard is the one that keeps the pair honest — it asserts NO test
    # is lit, so the "at rest" row cannot silently start measuring a pressed
    # button and reporting it as the resting treatment.
    "gap-answered": r"""
(function () {
  var wrap = document.querySelector('[data-gap]');
  if (!wrap) { return "no gap rig on the page"; }
  var opts = wrap.querySelectorAll('.ks3-option');
  if (!opts.length) { return "the rig offers no choices"; }
  var empty = parseInt(wrap.getAttribute('data-empty-choice'), 10);
  if (isNaN(empty) || empty < 0 || empty >= opts.length) {
    return "the rig declares no usable empty choice (data-empty-choice=" +
           wrap.getAttribute('data-empty-choice') + ")";
  }
  opts[empty].click();
  var rig = wrap.querySelector('[data-gap-rig]');
  if (!rig || rig.hasAttribute('hidden')) {
    return "a choice was made and the rig never appeared";
  }
  if (!wrap.querySelector('.ks3-gap-caption')) {
    return "the rig opened with no control caption";
  }
  var p = wrap.querySelector('.ks3-gap-note p');
  if (!p) { return "the rig opened with no outcome paragraph at all"; }
  if (p.hasAttribute('hidden')) {
    return "the rig opened and its first outcome paragraph is still hidden";
  }
  if (wrap.querySelector('.ks3-gap-test[aria-pressed="true"]')) {
    return "a test is already running, so the resting-test row would not be resting";
  }
  return "";
})()
""",
    # A test is ON THE BENCH — the state the amber row measures.
    #
    # The choice is one that FILLS the gap, found by walking the list for the
    # first index that is not `data-empty-choice` rather than by assuming a
    # position. That lands the test on its `off` outcome, which is the whole
    # argument of the block: every wrong answer fails all three tests. The
    # amber is not a verdict on the student — it marks which test is running,
    # and the outcome paragraph is one tone whichever answer they gave.
    #
    # The stage check is the second, independent proof that a test really ran:
    # `markStage` only fires from the test handler, never from the choice
    # handler, so a regression that lit the button without repainting would
    # still fail here. The section is found by `closest('[data-gapblock]')`
    # rather than by its `#s-gap` id, so re-anchoring the lesson cannot turn
    # this into a silent pass.
    "gap-tested": r"""
(function () {
  var wrap = document.querySelector('[data-gap]');
  if (!wrap) { return "no gap rig on the page"; }
  var opts = wrap.querySelectorAll('.ks3-option');
  if (!opts.length) { return "the rig offers no choices"; }
  var empty = parseInt(wrap.getAttribute('data-empty-choice'), 10);
  if (isNaN(empty)) {
    return "the rig declares no empty choice, so a filled gap cannot be chosen";
  }
  var pick = null;
  for (var i = 0; i < opts.length; i++) {
    if (i !== empty) { pick = opts[i]; break; }
  }
  if (!pick) { return "the rig offers no choice that fills the gap"; }
  pick.click();
  var t = wrap.querySelector('.ks3-gap-test');
  if (!t) { return "the rig offers no tests"; }
  t.click();
  if (t.getAttribute('aria-pressed') !== 'true') {
    return "a test was run and its button never lit";
  }
  var sec = wrap.closest('[data-gapblock]');
  if (!sec) { return "the rig is not inside a gap block"; }
  if (sec.getAttribute('data-stage-done') !== '1') {
    return "a test was run and the stage never completed";
  }
  return "";
})()
""",
