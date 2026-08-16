# ── PAGE CONSTANT ────────────────────────────────────────────────────────
# One drawn instance, on b3-07. Splice the constant beside the other unit
# constants in ks3_parity.py, inside the B3 group.
#
#     B3_VILLUS = "biology/nutrition-and-digestion/absorption-and-the-small-intestine.html"


# ── COMPONENTS entries ───────────────────────────────────────────────────
# Mutation-tested: each rule was deliberately broken in shared/ks3.css and the
# row confirmed to fail before it was kept. Every hex below is read out of
# shared/tokens.css, not estimated.

    # ── fold-builder (b3-07 #s-fold) ──
    #
    # ⚠️ THIS ROW EXISTS TO PROVE THE SPECIFICITY SCOPING. `.ks3-dark p` is
    # (0,1,1) and a bare `.ks3-fold-note` is (0,1,0), so unscoped the note
    # loses and takes the BLOCK's on-dark body copy instead of the PANEL's.
    # Here the two happen to resolve to the same token, which is exactly what
    # makes it dangerous: the defect would be invisible to reading and to the
    # eye, and would surface the first time the panel's treatment moved. The
    # row pins the panel's own value so the cascade is asserted rather than
    # assumed.
    dict(name="the area note is the panel's body copy, not the block's",
         on=B3_VILLUS, sel=".ks3-fold-note:not([hidden])",
         props={"color": "#E7DECE", "font-size": "19px",
                "font-family": "Instrument Sans"}),
    # The readout is the block's payoff and the number is MONO, not display
    # type: it changes six times while a student watches, and a proportional
    # face would make it jump on every toggle. Alert amber on the dark panel
    # is a value being reported, never a mistake being marked.
    dict(name="the area readout is mono alert on a dark panel", on=B3_VILLUS,
         sel=".ks3-fold-area",
         props={"font-family": "DM Mono", "font-size": "26px",
                "color": "#FFC53D"}),
    dict(name="the readout sits on the nested dark panel at card radius",
         on=B3_VILLUS, sel=".ks3-fold-readout",
         props={"background-color": "#3E3730",
                "border-top-left-radius": "22px"}),
    # ⚖️ THE ROW THAT MATTERS PEDAGOGICALLY. The bar is amber while the model
    # is part-built and green only when all three levels are on — and green
    # here is "this is the finished thing", not "you were right": there is no
    # question in this block and nothing to be right about. If this ever
    # resolves to `--ks3-ok` #12A150 at a count below three, the instrument has
    # started congratulating a student for a state, which is the first step
    # towards an activity that marks (R3).
    dict(name="the bar turns green only with all three levels on",
         on=B3_VILLUS, drive="fold-all-on", sel=".ks3-fold-bar",
         props={"background-color": "#12A150"}),


# ── DRIVES entries ───────────────────────────────────────────────────────

    # All three levels ON, through the instrument's own three buttons and
    # nothing else — no attribute is set by hand, so a regression in the
    # toggle path fails here rather than being stepped over.
    "fold-all-on": r"""
(function () {
  var sec = document.querySelector('[data-foldblock]');
  if (!sec) { return "no fold-builder on the page"; }
  var wrap = sec.querySelector('[data-fold]');
  if (!wrap) { return "the block has no fold-builder in it"; }
  if (sec.getAttribute('data-stage-done') === '1') {
    return "the stop ticked on load";
  }
  var bar = wrap.querySelector('[data-fold-bar]');
  if (!bar) { return "the readout has no bar"; }
  if (bar.getAttribute('data-full') === '1') {
    return "the bar was already full before any level was added";
  }
  var toggles = wrap.querySelectorAll('[data-fold-toggle]');
  if (toggles.length < 3) {
    return "the builder offers " + toggles.length + " levels, not three";
  }
  for (var i = 0; i < toggles.length; i++) { toggles[i].click(); }
  if (bar.getAttribute('data-full') !== '1') {
    return "every level is on and the bar has not filled";
  }
  // The note is indexed by the COUNT of levels, so the last one is the
  // finished model's. A note stuck at index 0 means emit-both-show-one has
  // stopped swapping and the student is reading about a plain tube.
  var shown = wrap.querySelector('.ks3-fold-note:not([hidden])');
  if (!shown) { return "no area note is showing"; }
  if (shown.getAttribute('data-note') !== String(toggles.length)) {
    return "the note showing is for " + shown.getAttribute('data-note')
      + " level(s), not " + toggles.length;
  }
  if (wrap.querySelectorAll('.ks3-fold-note:not([hidden])').length !== 1) {
    return "more than one area note is showing at once";
  }
  if (sec.getAttribute('data-stage-done') !== '1') {
    return "every level is on and the stop has not ticked";
  }
  // ⚖️ THE STOP LATCHES. Switching a level back off must leave the rail
  // alone — MRB-208 says a stop ticks when the activity is finished, and
  // nothing un-finishes it. The bar and the note are allowed to follow the
  // live state; the rail is not.
  toggles[0].click();
  if (sec.getAttribute('data-stage-done') !== '1') {
    return "the stop un-ticked when a level was switched back off";
  }
  toggles[0].click();
  // R3, asserted here as well as globally: three toggles are not answers, so
  // nothing in this instrument may be marked, spent or disabled.
  if (wrap.querySelector('.ks3-option, [data-correct], .is-correct, .is-wrong')) {
    return "the fold builder is marking something — this block asks no question";
  }
  return "";
})()
""",
