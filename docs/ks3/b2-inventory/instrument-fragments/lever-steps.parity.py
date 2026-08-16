# ── PAGE CONSTANT ────────────────────────────────────────────────────────
# One drawn instance, on b2-04.
#
#     B2_BIO = "biology/movement-skeleton-and-muscles/biomechanics-forces-in-the-body.html"


# ── COMPONENTS entries ───────────────────────────────────────────────────
# Mutation-tested: each rule was deliberately broken in shared/ks3.css and the
# row confirmed to fail before it was kept.

    # ── lever-steps (b2-04 #s-build) ──
    #
    # ⚖️ THE TWO MRB-204 STEP-4 BLOCKS MUST LOOK THE SAME. This row's values
    # are `.ks3-pick-opt`'s, deliberately: c2-06 asks a chemistry student to
    # pick between three candidate equations and b2-04 asks a biology student
    # to do exactly that, and a student meeting both would otherwise read them
    # as two different kinds of task. If either drifts, this fails.
    dict(name="a candidate equation is left-aligned mono on the option border",
         on=B2_BIO, sel=".ks3-lstep-opt",
         props={"font-family": "DM Mono", "font-size": "16px",
                "text-align": "left", "min-height": "44px",
                "border-top-color": "#DDCFB6"}),
    # R3 lives in this row. The chosen pick takes the accent BORDER and tint
    # and nothing else — no green, no mark, no verdict — because only the
    # mastery ladder marks correctness. A regression that added `is-correct`
    # styling here would turn the whole page into a test.
    dict(name="a chosen equation is chosen, never correct", on=B2_BIO,
         drive="lsteps-committed",
         sel='.ks3-lstep-opt[aria-pressed="true"]',
         props={"border-top-color": "#E4572E",
                "background-color": "#FCE7DE"}),
    # ⚠️ THE MODEL ANSWER INVERTS TO INK inside a light block, and the chip is
    # ALERT rather than the accent the worked example upstairs uses. Two FIFA
    # sets on one page, same four letters, two grounds — and the accent does
    # not carry on ink, which is why the pair changes.
    dict(name="the model answer lands on ink with an alert chip", on=B2_BIO,
         drive="lsteps-opened", sel=".ks3-lstep-chip",
         props={"background-color": "#FFC53D", "color": "#221E1B",
                "width": "34px"}),
    # ⚖️ The closing line quotes the student's answer beside the worked one in
    # ordinary on-dark body copy — NOT a verdict colour. It is a comparison
    # the student makes, never a mark the page makes (R3 / MRB-196 R10).
    dict(name="the closing comparison is body copy, not a verdict", on=B2_BIO,
         drive="lsteps-opened", sel=".ks3-lstep-close",
         props={"color": "#E7DECE", "font-size": "19px"}),


# ── DRIVES entries ───────────────────────────────────────────────────────

    # Two picks and a number with a unit — the three commitments the block
    # asks for. Which options are pressed is deliberately unspecified: under
    # R3 all three in a ladder render identically and none of them is marked.
    #
    # ⊕ THIS DRIVE IS ALSO THE RAIL CORRECTION'S ASSERTION. It fails if the
    # stop ticks before the third commitment — which is what Design's own
    # `buildOpen` predicate did, one tap after arriving.
    "lsteps-committed": r"""
(function () {
  var sec = document.querySelector('[data-lstepblock]');
  if (!sec) { return "no lever-steps on the page"; }
  var wrap = sec.querySelector('[data-lstep]');
  var btn = wrap.querySelector('[data-lstep-open]');
  var ans = wrap.querySelector('[data-lstep-ans]');
  var unit = wrap.querySelector('[data-lstep-unit]');
  if (!btn || !ans || !unit) { return "the block is missing a commitment control"; }
  if (sec.getAttribute('data-stage-done') === '1') {
    return "the stop ticked on load";
  }
  var g0 = wrap.querySelector('.ks3-lstep-opt[data-group="0"]');
  var g1 = wrap.querySelector('.ks3-lstep-opt[data-group="1"]');
  if (!g0 || !g1) { return "the block offers fewer than two pick ladders"; }
  g0.click();
  g1.click();
  if (sec.getAttribute('data-stage-done') === '1') {
    return "the stop ticked on two picks — the answer is the third commitment";
  }
  ans.value = '160';
  ans.dispatchEvent(new Event('input', { bubbles: true }));
  if (sec.getAttribute('data-stage-done') === '1') {
    return "the stop ticked on a number with no unit";
  }
  if (!btn.hasAttribute('disabled')) {
    return "the open button unlocked before a unit was chosen";
  }
  unit.value = 'N';
  unit.dispatchEvent(new Event('change', { bubbles: true }));
  if (sec.getAttribute('data-stage-done') !== '1') {
    return "all three lines committed and the stop has not ticked";
  }
  if (btn.hasAttribute('disabled')) {
    return "all three lines committed and the button is still locked";
  }
  return "";
})()
""",
    # The reveal panel does not exist in the document's layout until the
    # button is pressed, so every measurement inside it needs this. It also
    # asserts the LIVE COUPLING: the closing line has to quote the force the
    # rig implies, which is the block's whole claim to be the same problem.
    "lsteps-opened": r"""
(function () {
  var sec = document.querySelector('[data-lstepblock]');
  if (!sec) { return "no lever-steps on the page"; }
  var wrap = sec.querySelector('[data-lstep]');
  var g0 = wrap.querySelector('.ks3-lstep-opt[data-group="0"]');
  var g1 = wrap.querySelector('.ks3-lstep-opt[data-group="1"]');
  var ans = wrap.querySelector('[data-lstep-ans]');
  var unit = wrap.querySelector('[data-lstep-unit]');
  var btn = wrap.querySelector('[data-lstep-open]');
  if (!g0 || !g1 || !ans || !unit || !btn) { return "the block is incomplete"; }
  g0.click(); g1.click();
  ans.value = '160';
  ans.dispatchEvent(new Event('input', { bubbles: true }));
  unit.value = 'N';
  unit.dispatchEvent(new Event('change', { bubbles: true }));
  btn.click();
  var panel = wrap.querySelector('[data-reveal]');
  if (!panel || panel.hasAttribute('hidden')) {
    return "the three lines were committed, the button pressed, and the panel is still hidden";
  }
  if (!wrap.querySelector('.ks3-lstep-chip')) {
    return "the model answer opened with no steps in it";
  }
  var close = wrap.querySelector('[data-lstep-close]');
  if (!close || close.textContent.indexOf('160') < 0) {
    return "the closing line does not quote the student's own answer back";
  }
  if (/[{}]/.test(wrap.textContent)) {
    return "an unfilled template reached the page: " + wrap.textContent.slice(0, 120);
  }
  var locked = wrap.querySelector('.ks3-lstep-opt:not([disabled])');
  if (locked) {
    return "the model is on screen and a pick can still be changed";
  }
  return "";
})()
""",
