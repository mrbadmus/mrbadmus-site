# ── PAGE CONSTANT ────────────────────────────────────────────────────────
# One drawn instance, on b2-04.
#
#     B2_BIO = "biology/movement-skeleton-and-muscles/biomechanics-forces-in-the-body.html"


# ── COMPONENTS entries ───────────────────────────────────────────────────
# Mutation-tested: each rule was deliberately broken in shared/ks3.css and the
# row confirmed to fail before it was kept.

    # ── meter-compare (b2-04 #s-meters) ──
    #
    # ⚖️ THE READINGS ARE EVIDENCE, NOT SMALL PRINT. This row is the one that
    # matters pedagogically: 17px mono in ink-BODY, not a 13px muted caption.
    # Shrink them and the card teaches that the mean is the measurement and
    # the spread is a footnote, which is exactly the idea the closing band
    # exists to break — and it would be invisible to reading the CSS, because
    # a caption under a headline looks tidy.
    dict(name="the three readings are evidence, at readable mono", on=B2_BIO,
         drive="meters-ranked", sel=".ks3-meters-readings",
         props={"font-family": "DM Mono", "font-size": "17px",
                "color": "#3B342E"}),
    dict(name="the mean is the card's headline in display type", on=B2_BIO,
         drive="meters-ranked", sel=".ks3-meters-mean",
         props={"font-family": "Bricolage Grotesque", "font-size": "30px",
                "font-weight": "800"}),
    # A 2px INK border, not the `--ks3-option-border` the commit buttons take.
    # These cards are the measurements and the heavier rule is what separates
    # data from a control on the same cream ground.
    dict(name="a meter card is a card on ink, not on the option border",
         on=B2_BIO, drive="meters-ranked", sel=".ks3-meters-card",
         props={"border-top-color": "#221E1B", "border-top-width": "2px",
                "background-color": "#FFFCF5"}),
    # 34rem, Design's own measure. Three candidate orderings are read against
    # each other, and a full-width button on a 60rem column is a target the
    # eye has to travel to compare with the one above it.
    dict(name="the ranking options keep Design's 34rem measure", on=B2_BIO,
         sel=".ks3-meters-commit .ks3-options",
         props={"max-width": "544px"}),


# ── DRIVES entries ───────────────────────────────────────────────────────

    # The cards do not exist in the document's layout until an ordering is
    # committed, so every measurement above needs this. Which ordering is
    # deliberately unspecified: under R3 all three render identically and all
    # three open the same cards, and `check_r3_runtime()` asserts that rather
    # than trusting it.
    "meters-ranked": r"""
(function () {
  var sec = document.querySelector('[data-metersblock]');
  if (!sec) { return "no meter-compare on the page"; }
  var wrap = sec.querySelector('[data-meters]');
  var opt = wrap && wrap.querySelector('.ks3-option');
  if (!opt) { return "the block offers no ranking options"; }
  if (sec.getAttribute('data-stage-done') === '1') {
    return "the stop ticked on load";
  }
  opt.click();
  var panel = wrap.querySelector('[data-reveal]');
  if (!panel || panel.hasAttribute('hidden')) {
    return "an ordering was committed and the cards are still hidden";
  }
  if (wrap.querySelectorAll('.ks3-meters-card').length < 2) {
    return "the reveal opened with fewer than two groups to compare";
  }
  // ⚠️ ALL THE CARDS, NOT ONE. The commitment is about the ORDER of the
  // three, so revealing them a card at a time would answer part of the
  // question still being asked.
  if (wrap.querySelectorAll('.ks3-meters-card').length
      !== wrap.querySelectorAll('.ks3-meters-mean').length) {
    return "a card arrived without its mean";
  }
  if (sec.getAttribute('data-stage-done') !== '1') {
    return "an ordering was committed and the stop has not ticked";
  }
  // R3, asserted here as well as globally: a ranking is a commitment, not an
  // answer, so nothing may be marked or spent.
  if (wrap.querySelector('.ks3-option[data-correct], .ks3-option.is-correct, .ks3-option.is-wrong, .ks3-option[disabled]')) {
    return "a ranking option was marked or disabled — this block marks nothing";
  }
  return "";
})()
""",
