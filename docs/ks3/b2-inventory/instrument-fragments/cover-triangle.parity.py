# ── PAGE CONSTANT ────────────────────────────────────────────────────────
# Measured on b2-04, the only page that renders the WIDENED triangle. b1-02
# renders the narrow one and is asserted separately, by byte-identity across
# the splice rather than by a resolved-style row — a rule that passes on both
# variants would prove nothing about either.
#
#     B2_BIO = "biology/movement-skeleton-and-muscles/biomechanics-forces-in-the-body.html"


# ── COMPONENTS entries ───────────────────────────────────────────────────
# Mutation-tested: each rule below was deliberately broken in shared/ks3.css
# and the row confirmed to fail before it was kept.

    # ── cover-triangle · triangle variant (b2-04's rule block) ──
    #
    # ⚠️ THIS ROW IS THE b1-02 GUARD. Every widened declaration is scoped
    # `[data-tri-layout="row"]`, and the row layout is what proves the scope
    # exists: if a future tidy-up moved the flex onto bare `.ks3-triangle`,
    # b1-02's centred stack would silently become a two-column row and this
    # row would still pass — so it asserts the SIDE panel's own flex basis,
    # which only the widened markup has an element for.
    dict(name="the widened triangle puts the reading beside the figure",
         on=B2_BIO, sel='.ks3-triangle[data-tri-layout="row"] .ks3-tri-row',
         props={"display": "flex", "flex-wrap": "wrap",
                "column-gap": "52px", "row-gap": "34px"}),
    dict(name="the side panel is left-aligned and can stack at 260px",
         on=B2_BIO, sel=".ks3-tri-side",
         props={"text-align": "left", "min-width": "260px"}),
    # The arrangement is the line a student writes down, so it is display type
    # at the same 30px the bar variant's result takes — one reading treatment
    # across both shapes of the same component, or a student meeting both
    # would read them as two different kinds of statement.
    dict(name="the covered cell's arrangement is 30px display type",
         on=B2_BIO, sel='.ks3-tri-result:not([hidden])',
         props={"font-size": "30px", "font-weight": "800",
                "color": "#221E1B"}),
    # ⚠️ THE ROW'S NOTE IS A BARE PARAGRAPH. b1-02's is an inset panel on a
    # 2px ink border, and that rule is still in the stylesheet above this one
    # — this row is what proves the override reaches, because a box around one
    # of five stacked blocks in a column reads as a callout rather than as the
    # sentence explaining the line above it.
    dict(name="the row variant's sentence is not the inset panel",
         on=B2_BIO, sel='.ks3-tri-note:not([hidden])',
         props={"border-top-width": "0px", "padding-top": "0px",
                "font-size": "19px"}),
    # The balanced condition, set apart. It is the statement that makes every
    # question on the page solvable, and it is deliberately NOT the 18px
    # ink-body the rule line above it takes.
    dict(name="the balanced condition is set apart in display type",
         on=B2_BIO, sel=".ks3-tri-condition",
         props={"font-family": "Bricolage Grotesque", "font-size": "21px",
                "font-weight": "700"}),


# ── DRIVES entries ───────────────────────────────────────────────────────

    # ⚠️ NO DRIVE IS NEEDED FOR THE RESTING MEASUREMENT, and that is the
    # point of `covered`: b2-04 opens with F already covered, so the result
    # line, the sentence and the pressed button are all in their final state
    # in the built HTML before a single line of JS runs. The rows above
    # measure that page as delivered.
    #
    # This drive exists to prove the RADIO contract — that the control never
    # returns to an uncovered state, which is the one behaviour that differs
    # from b1-02 and the one a regression would restore by accident.
    "triangle-radio-held": r"""
(function () {
  var tri = document.querySelector('[data-triangle][data-cover-mode="radio"]');
  if (!tri) { return "no radio-mode triangle on the page"; }
  var start = tri.getAttribute('data-covered');
  if (!start) { return "a radio triangle opened with nothing covered"; }
  var btn = tri.querySelector('.ks3-tri-btn[data-cover="' + start + '"]');
  if (!btn) { return "no button for the covered cell " + start; }
  // Press the ALREADY-covered cell. A toggle would uncover here; a radio
  // must not, because an uncovered triangle asks the student nothing.
  btn.click();
  if (tri.getAttribute('data-covered') !== start) {
    return "pressing the covered cell uncovered it — the radio has become a toggle";
  }
  var other = tri.querySelector('.ks3-tri-btn:not([data-cover="' + start + '"])');
  if (!other) { return "the triangle offers only one cover"; }
  other.click();
  var now = other.getAttribute('data-cover');
  if (tri.getAttribute('data-covered') !== now) {
    return "pressing a second cell did not move the cover";
  }
  if (!tri.querySelector('.ks3-tri-result[data-result="' + now + '"]:not([hidden])')) {
    return "the cover moved and the arrangement line did not follow it";
  }
  if (!tri.querySelector('.ks3-tri-note[data-note="' + now + '"]:not([hidden])')) {
    return "the cover moved and the sentence did not follow it";
  }
  if (tri.querySelectorAll('.ks3-tri-result:not([hidden])').length !== 1) {
    return "more than one arrangement line is showing";
  }
  return "";
})()
""",
