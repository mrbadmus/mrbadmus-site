# ── PAGE CONSTANT ────────────────────────────────────────────────────────
# One drawn instance, on b3-05.
#
#     B3_GUT = "biology/nutrition-and-digestion/the-digestive-system.html"


# ── COMPONENTS entries ───────────────────────────────────────────────────
# Every value below is read out of `shared/tokens.css`, not estimated:
#   --ks3-alert #FFC53D · --ks3-on-dark #FBF3E6 · --ks3-on-dark-muted #C6B9A7
#   --ks3-on-dark-body #E7DECE · --ks3-dark-panel #3E3730 · --ks3-ink #221E1B
#   --ks3-ground #FBF3E6 · --ks3-r-card 22px · --ks3-r-panel 20px
# Mutation-tested: each rule was deliberately broken in shared/ks3.css and the
# row confirmed to fail before it was kept.

    # ── gut-journey (b3-05 #s-journey) ──
    #
    # ⚖️ THE TIME TILE IS THE QUANTITY THE WHOLE BLOCK ARGUES FROM, and this
    # row is the one that matters pedagogically: 23px mono at weight 500,
    # against the 18px/700 the other two tiles take. Level the three and the
    # panel reads as three equal facts, which is precisely how "four hours in
    # the stomach, sixteen in the small intestine" gets missed — and it would
    # be invisible to reading the CSS, because three matching tiles look tidy.
    dict(name="the time tile is larger mono, not one fact of three",
         on=B3_GUT, sel='.ks3-gut-tile[data-tile="time"] .ks3-gut-tilevalue',
         props={"font-family": "DM Mono", "font-size": "23px",
                "color": "#FBF3E6"}),
    dict(name="the other two tiles stay 18px body weight", on=B3_GUT,
         sel='.ks3-gut-tile[data-tile="absorbs"] .ks3-gut-tilevalue',
         props={"font-family": "Instrument Sans", "font-size": "18px",
                "font-weight": "700", "color": "#FBF3E6"}),
    # ⚠️ SPECIFICITY. The note sits on the CREAM ground inside an ink block, so
    # it must be pulled back to ink at (0,2,0). `.ks3-dark p` is (0,1,1) and a
    # bare `.ks3-gut-note` is (0,1,0): unscoped it paints #E7DECE on #FBF3E6 at
    # about 1.2:1 — seven invisible paragraphs, one per stop.
    dict(name="the worth-knowing note inverts to cream and reads in ink",
         on=B3_GUT, sel=".ks3-gut-note",
         props={"background-color": "#FBF3E6", "color": "#221E1B",
                "font-size": "18px"}),
    # ⚖️ THE LIT ROW IS THE ONLY THING THE RUNTIME MOVES ON THIS CHART. The
    # width is inline from the Python; if this row ever fails, the highlight
    # has been re-implemented somewhere that can also touch the width.
    dict(name="the chart lights the current organ's bar in amber", on=B3_GUT,
         drive="gut-stomach", sel='.ks3-gut-row[data-lit="1"] .ks3-gut-bar',
         props={"background-color": "#FFC53D"}),


# ── DRIVES entries ───────────────────────────────────────────────────────

    # Drives the journey to the STOMACH — stop three, and the one the lesson's
    # argument turns on. Reached through the instrument's own tab, never by
    # setting an attribute.
    "gut-stomach": r"""
(function () {
  var sec = document.querySelector('[data-gutblock]');
  if (!sec) { return "no gut-journey on the page"; }
  if (sec.getAttribute('data-stage-done') === '1') {
    return "the stop ticked on load";
  }
  var wrap = sec.querySelector('[data-gut]');
  var tabs = wrap ? wrap.querySelectorAll('.ks3-gut-tab') : [];
  if (tabs.length < 7) { return "the journey draws fewer than seven stops"; }
  var tab = wrap.querySelector('.ks3-gut-tab[data-stop="stomach"]');
  if (!tab) { return "the journey has no stomach stop"; }
  tab.click();
  var panel = wrap.querySelector('.ks3-gut-stop[data-stop="stomach"]');
  if (!panel || panel.hasAttribute('hidden')) {
    return "the stomach tab was pressed and its panel is still hidden";
  }
  if (wrap.querySelectorAll('.ks3-gut-stop:not([hidden])').length !== 1) {
    return "more than one stop panel is showing at once";
  }
  if (panel.querySelectorAll('.ks3-gut-tile').length !== 3) {
    return "a stop panel arrived without all three tiles";
  }
  var lit = wrap.querySelectorAll('.ks3-gut-row[data-lit="1"]');
  if (lit.length !== 1 || lit[0].getAttribute('data-stop') !== 'stomach') {
    return "the chart is not lighting the stop that is showing";
  }
  // ⚠️ THE BAR WIDTHS ARE THE PYTHON'S AND MUST SURVIVE A TAB PRESS. If the
  // wiring ever starts computing them, this is where it shows up.
  var bar = lit[0].querySelector('.ks3-gut-bar');
  if (!bar || !/^\s*\d/.test(bar.style.width || '')) {
    return "the lit bar has no inline width from the build";
  }
  // Three of seven visited (mouth seeded, stomach pressed) — the stop must not
  // have ticked: the whole journey is the argument.
  if (sec.getAttribute('data-stage-done') === '1') {
    return "the stop ticked before the journey was finished";
  }
  return "";
})()
""",
