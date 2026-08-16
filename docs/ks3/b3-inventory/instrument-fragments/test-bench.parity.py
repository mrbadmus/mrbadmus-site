# ── PAGE CONSTANT ────────────────────────────────────────────────────────
# One drawn instance, on b3-02.
#
#     B3_TESTS = "biology/nutrition-and-digestion/food-tests.html"


# ── COMPONENTS entries ───────────────────────────────────────────────────
# Mutation-tested: each rule was deliberately broken in shared/ks3.css and the
# row confirmed to fail before it was kept.

    # ── test-bench (b3-02 #s-bench) ──
    #
    # ⚠️ THE ROW THAT WOULD OTHERWISE SHIP BROKEN. The result panel is CREAM
    # inside an ink-dark block, so the honest note has to resolve to
    # `--ks3-ink`. `.ks3-dark p` is (0,1,1) and a bare `.ks3-tbench-why` is
    # (0,1,0): unscoped it paints `--ks3-on-dark-body` #E7DECE on #FBF3E6 —
    # the four false-negative explanations, which are the entire point of the
    # lesson, present and unreadable.
    # ⚖️ CORRECTED (MRB-228) — see the note in band-commit.parity.py. The
    # background belongs to `.ks3-tbench-result`, not to the paragraph in it.
    dict(name="the honest note is ink on the cream result panel", on=B3_TESTS,
         drive="bench-run", sel=".ks3-tbench-why",
         props={"color": "#221E1B", "font-size": "18px"}),
    dict(name="the result panel is the page ground on an ink block",
         on=B3_TESTS, drive="bench-run", sel=".ks3-tbench-result",
         props={"background-color": "#FBF3E6"}),
    # ⚖️ THE CLAIM LINE IS RULED OFF, and the rule is load-bearing rather than
    # decorative: above it is what happened, below it is what the student may
    # write down. Losing the rule runs the observation and the licensed claim
    # together, which is precisely the slip the lesson exists to stop.
    dict(name="the claim line is ruled off from the explanation", on=B3_TESTS,
         drive="bench-run", sel=".ks3-tbench-claim",
         props={"border-top-color": "#E0D2B9", "border-top-width": "2px",
                "padding-top": "12px", "color": "#221E1B"}),
    # ⚖️ THE TUBE IS THE ONE PLACE IN THE KEY STAGE WHERE A COLOUR IS REAL.
    # This row asserts the tube's own frame comes from tokens while its FILL
    # does not — the fill is checked in the drive below, against the reagent's
    # authored hex. A token creeping onto the fill would tint an observation.
    dict(name="the tube frame is the muted rule, 62px wide", on=B3_TESTS,
         sel=".ks3-tbench-tube",
         props={"border-top-color": "#C6B9A7", "border-top-width": "3px",
                "width": "62px", "height": "168px"}),
    # Design's dark tab pair, shared with band-commit and person-ledger: lit is
    # alert with ink text, resting transparent on the muted rule.
    dict(name="a chosen bench tab is alert with ink text", on=B3_TESTS,
         sel='.ks3-tbench-tab[aria-pressed="true"]',
         props={"background-color": "#FFC53D", "color": "#221E1B",
                "min-height": "44px"}),


# ── DRIVES entries ───────────────────────────────────────────────────────

    # The result panel does not exist in the layout until a combination has
    # been predicted, so every panel row above needs this.
    #
    # ⚠️ IT RUNS THE TEST THE WAY A STUDENT DOES — one `.click()` on a real
    # prediction button. There is no run control to reach for: in this block
    # predicting IS running, and a drive that unhid the panel directly would
    # prove the stylesheet while leaving that mechanism unasserted.
    "bench-run": r"""
(function () {
  var sec = document.querySelector('[data-tbenchblock]');
  if (!sec) { return "no test-bench on the page"; }
  var wrap = sec.querySelector('[data-tbench]');
  if (!wrap) { return "the block drew no bench"; }
  if (sec.getAttribute('data-stage-done') === '1') {
    return "the stop ticked on load";
  }
  var tube = wrap.querySelector('[data-tube]');
  if (!tube) { return "the bench drew no tube"; }
  var resting = getComputedStyle(tube).backgroundColor;
  if (tube.getAttribute('data-run') !== '0') {
    return "the tube reports a run before anything was run";
  }
  var predict = wrap.querySelector('[data-predict]');
  if (!predict || predict.hasAttribute('hidden')) {
    return "an unrun combination is not asking for a prediction";
  }
  if (!wrap.querySelector('.ks3-tbench-prompt:not([hidden])')) {
    return "the prediction gate opened with no prompt showing";
  }
  if (wrap.querySelectorAll('.ks3-tbench-prompt:not([hidden])').length !== 1) {
    return "more than one prediction prompt is showing at once";
  }
  var opt = predict.querySelector('.ks3-option');
  if (!opt) { return "the prediction gate offers no options"; }
  opt.click();
  var panel = wrap.querySelector('.ks3-tbench-result:not([hidden])');
  if (!panel) { return "a prediction was made and no result opened"; }
  if (wrap.querySelectorAll('.ks3-tbench-result:not([hidden])').length !== 1) {
    return "more than one result panel is showing at once";
  }
  if (!panel.querySelector('.ks3-tbench-claim')) {
    return "a result opened with no claim line — the claim line is the lesson";
  }
  if (!panel.querySelector('.ks3-tbench-verdict:not([hidden])')) {
    return "a result opened without saying whether the prediction matched";
  }
  if (!predict.hasAttribute('hidden')) {
    return "the combination has run and the prediction gate is still asking";
  }
  if (tube.getAttribute('data-run') !== '1') {
    return "the test ran and the tube still reads unrun";
  }
  // ⚖️ THE FILL IS THE REAGENT'S OWN COLOUR. It has to CHANGE on a positive
  // and it must never resolve to an accent token — #E4572E is --ks3-accent
  // and #FFC53D is --ks3-alert, and either on this element would be tinting
  // an observation.
  var after = getComputedStyle(tube).backgroundColor;
  if (after === 'rgb(228, 87, 46)' || after === 'rgb(255, 197, 61)') {
    return "the tube fill resolved to an accent token, not a reagent colour";
  }
  if (!panel.getAttribute('data-colour')) {
    return "the result panel carries no reagent colour for the tube";
  }
  if (panel.getAttribute('data-outcome') === 'pos' && after === resting) {
    return "a positive result left the tube the colour it started";
  }
  // R3: the prediction options are commitments, not answers.
  if (wrap.querySelector('.ks3-option[data-correct], .ks3-option[disabled], .ks3-option.is-correct, .ks3-option.is-wrong')) {
    return "a prediction option was marked or disabled";
  }
  return "";
})()
""",

    # The rail stop asks for FOUR combinations, not one, so it needs its own
    # drive: `bench-run` deliberately stops at one to prove the panel, and a
    # stop that ticked there would be a rail that lies in the student's favour.
    "bench-four": r"""
(function () {
  var sec = document.querySelector('[data-tbenchblock]');
  if (!sec) { return "no test-bench on the page"; }
  var wrap = sec.querySelector('[data-tbench]');
  var target = parseInt(wrap.getAttribute('data-target'), 10) || 4;
  var tests = wrap.querySelectorAll('.ks3-tbench-tab[data-test]');
  if (tests.length < target) {
    return "fewer tests on the bench than the rail stop asks for";
  }
  for (var i = 0; i < target; i++) {
    tests[i].click();
    var opt = wrap.querySelector('[data-predict] .ks3-option');
    if (!opt) { return "a fresh combination offered no prediction"; }
    if (i === target - 1 && sec.getAttribute('data-stage-done') === '1') {
      return "the stop ticked before the last combination was run";
    }
    opt.click();
  }
  if (sec.getAttribute('data-stage-done') !== '1') {
    return "four combinations have been run and the stop has not ticked";
  }
  return "";
})()
""",
