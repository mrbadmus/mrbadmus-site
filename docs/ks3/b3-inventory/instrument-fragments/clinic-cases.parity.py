# ── PAGE CONSTANT ────────────────────────────────────────────────────────
# One drawn instance, on b3-04.
#
#     B3_WRONG = "biology/nutrition-and-digestion/when-diet-goes-wrong.html"


# ── COMPONENTS entries ───────────────────────────────────────────────────
# Every value below is read out of `shared/tokens.css`, not estimated:
#   --ks3-alert #FFC53D · --ks3-on-dark #FBF3E6 · --ks3-on-dark-muted #C6B9A7
#   --ks3-dark-panel #3E3730 · --ks3-ground #FBF3E6 · --ks3-ink #221E1B
#   --ks3-accent-text #A93411 · --ks3-r-panel 20px
# Mutation-tested: each rule was deliberately broken in shared/ks3.css and the
# row confirmed to fail before it was kept.

    # ── clinic-cases (b3-04 #s-cases) ──
    #
    # ⚠️ THE THREE ROWS BELOW ARE THE SPECIFICITY PROOF, and they are the
    # reason this instrument has a parity entry at all. `.ks3-dark p` is
    # (0,1,1); every bare class in the fragment is (0,1,0) and LOSES. Unscoped,
    # all three of these paragraphs resolve to `--ks3-on-dark-body` #E7DECE —
    # which is a plausible-looking panel and a broken one, and it is invisible
    # to reading the CSS.
    dict(name="the intake line is amber mono, not another sentence of prose",
         on=B3_WRONG, drive="clinic-diagnosed", sel=".ks3-clinic-intake",
         props={"font-family": "DM Mono", "font-size": "16px",
                "color": "#FFC53D"}),
    # ⚖️ THE VERDICT INVERTS. It sits on the CREAM ground inside an ink block,
    # so its paragraphs have to be pulled back to ink explicitly. Left to
    # `.ks3-dark p` they would paint #E7DECE on #FBF3E6 — 1.2:1, the answer
    # rendered invisible on the one panel that carries it.
    dict(name="the verdict panel inverts to the page ground", on=B3_WRONG,
         drive="clinic-diagnosed", sel=".ks3-clinic-verdict",
         props={"background-color": "#FBF3E6",
                "border-top-left-radius": "20px"}),
    dict(name="the answer is ink display type on that cream, not on-dark body",
         on=B3_WRONG, drive="clinic-diagnosed", sel=".ks3-clinic-answer",
         props={"font-family": "Bricolage Grotesque", "font-size": "26px",
                "font-weight": "800", "color": "#221E1B"}),
    # ⚖️ THE SPENT STATE IS THE ONLY THING THIS BLOCK PAINTS ABOUT THE ANSWER,
    # and it dims what was NOT chosen. R3: nothing marks correctness here, so
    # this row asserts a dim and there is deliberately no green/red row to
    # pair it with anywhere in this instrument.
    dict(name="after diagnosis the unticked imbalances dim, and nothing marks",
         on=B3_WRONG, drive="clinic-diagnosed",
         sel='.ks3-clinic-panel[data-open="1"] .ks3-clinic-pick[aria-pressed="false"]',
         props={"opacity": "0.45"}),


# ── DRIVES entries ───────────────────────────────────────────────────────

    # The verdict does not exist in the document's layout until a clinic has
    # been diagnosed, so every measurement above needs this. It reaches that
    # state through the instrument's OWN controls — a pick, then the reveal
    # button — and never by setting an attribute.
    "clinic-diagnosed": r"""
(function () {
  var sec = document.querySelector('[data-clinicblock]');
  if (!sec) { return "no clinic-cases on the page"; }
  if (sec.getAttribute('data-stage-done') === '1') {
    return "the stop ticked on load";
  }
  var wrap = sec.querySelector('[data-clinic]');
  var panel = wrap && wrap.querySelector('.ks3-clinic-panel:not([hidden])');
  if (!panel) { return "no clinic panel is showing"; }
  var picks = panel.querySelectorAll('.ks3-clinic-pick');
  var btn = panel.querySelector('[data-clinic-reveal]');
  if (picks.length < 2 || !btn) { return "the clinic offers no imbalances to tick"; }
  if (!btn.hasAttribute('disabled')) {
    return "the diagnosis was available before anything was ticked";
  }
  // ⚠️ TWO ticks, on one clinic, because the multi-select IS the instrument.
  // A single-select would drop the first when the second is pressed, and this
  // check would then catch it.
  picks[0].click();
  picks[1].click();
  if (panel.querySelectorAll('.ks3-clinic-pick[aria-pressed="true"]').length !== 2) {
    return "two imbalances were ticked and the block kept only one";
  }
  if (btn.hasAttribute('disabled')) {
    return "two imbalances are ticked and the diagnosis is still locked";
  }
  btn.click();
  var v = panel.querySelector('[data-reveal]');
  if (!v || v.hasAttribute('hidden')) {
    return "the diagnosis was opened and the verdict is still hidden";
  }
  if (!panel.querySelector('.ks3-clinic-answer') ||
      !panel.querySelector('.ks3-clinic-verdict-label')) {
    return "the verdict opened without its answer or its label";
  }
  // R3, asserted here as well as globally: nothing in this block marks.
  if (wrap.querySelector('.ks3-clinic-pick[data-correct], .ks3-clinic-pick.is-correct, .ks3-clinic-pick.is-wrong')) {
    return "an imbalance button was marked — this block marks nothing";
  }
  // One clinic of five, so the stop must NOT have ticked yet: the argument is
  // the five held against each other.
  if (sec.getAttribute('data-stage-done') === '1') {
    return "the stop ticked on one clinic of five";
  }
  return "";
})()
""",
