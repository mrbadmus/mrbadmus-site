# ── PAGE CONSTANT ────────────────────────────────────────────────────────
# One drawn instance, on b3-01. Splice the constant beside the other unit
# constants in ks3_parity.py.
#
#     B3_DIET = "biology/nutrition-and-digestion/a-balanced-diet.html"


# ── COMPONENTS entries ───────────────────────────────────────────────────
# Mutation-tested: each rule was deliberately broken in shared/ks3.css and the
# row confirmed to fail before it was kept.

    # ── band-commit (b3-01 #s-plate) ──
    #
    # ⚠️ THIS ROW EXISTS TO PROVE THE SPECIFICITY SCOPING, and it is the one
    # that would otherwise ship broken. The why panel is CREAM (`--ks3-ground`)
    # inside an ink-dark block, so its note has to resolve to `--ks3-ink`.
    # `.ks3-dark p` is (0,1,1) and a bare `.ks3-plate-note` is (0,1,0), so
    # unscoped the note loses and paints `--ks3-on-dark-body` #E7DECE on cream
    # #FBF3E6 — a 1.1:1 sentence that is technically present and unreadable,
    # and invisible to anyone reading the stylesheet. Same defect class as B1's
    # zoom instrument and B2's muscle bench.
    # ⚖️ CORRECTED (MRB-228). One row asked the note for the PANEL's
    # background and resolved `rgba(0, 0, 0, 0)` — a paragraph has no ground of
    # its own. Split: the note's own claim is that it beats `.ks3-dark p`
    # (0,1,1) and stays ink; the panel's claim is the cream ground it sits on.
    dict(name="the why note is ink on the cream panel, not on-dark body",
         on=B3_DIET, drive="plate-opened", sel=".ks3-plate-note",
         props={"color": "#221E1B", "font-size": "18px"}),
    dict(name="the why panel is the page ground on an ink block",
         on=B3_DIET, drive="plate-opened", sel=".ks3-plate-why",
         props={"background-color": "#FBF3E6"}),
    # Design's dark segmented pair, identical to `.ks3-sim-seg-btn`'s: lit is
    # the alert yellow carrying INK text, resting is transparent on the muted
    # rule. ⚖️ Amber here is CHOSEN, never wrong — nothing in this instrument
    # marks a mistake, and this row pins the colour to the pressed state so a
    # later pass cannot quietly repurpose it.
    dict(name="a chosen band is alert with ink text", on=B3_DIET,
         drive="plate-opened", sel='.ks3-plate-band[aria-pressed="true"]',
         props={"background-color": "#FFC53D", "color": "#221E1B",
                "border-top-color": "#FFC53D", "min-height": "44px"}),
    # The row is the ONLY thing in the block that reports whether the student
    # had it, and it does so with the block's own lit rule rather than with a
    # marking colour. If this row ever resolves to `--ks3-ok` #12A150 or
    # `--ks3-ok-tint` #E4F7EB, an activity has started marking (R3).
    dict(name="a correctly placed row is the dark panel on an alert rule",
         on=B3_DIET, drive="plate-opened",
         sel='.ks3-plate-row[data-state="hit"]',
         props={"background-color": "#3E3730", "border-top-color": "#FFC53D",
                "border-top-width": "2px", "border-top-left-radius": "20px"}),
    # The verdict is the block's payoff and is set in display type, not body:
    # "3 of 7 in the right band." has to read as a headline or the three
    # branches under it read as a footnote to a number nobody noticed.
    dict(name="the verdict headline is display 800 on on-dark", on=B3_DIET,
         drive="plate-opened", sel=".ks3-plate-vhead",
         props={"font-family": "Bricolage Grotesque", "font-size": "27px",
                "font-weight": "800", "color": "#FBF3E6"}),


# ── DRIVES entries ───────────────────────────────────────────────────────

    # Nothing measured above exists in the document's layout until all seven
    # rows are committed and the reveal is opened, so every row needs this.
    #
    # ⚠️ IT COMMITS THROUGH THE REAL CONTROLS. Seven `.click()`s on seven band
    # buttons and one on the reveal, exactly as a student would — never by
    # setting `data-state` or unhiding a panel, because a drive that reaches
    # the state by hand proves the stylesheet and nothing about the gate.
    #
    # Which band is deliberately unspecified: it presses the FIRST option in
    # every row, so on Design's payload some rows are right and some are wrong
    # and both `hit` and `miss` states exist to be measured.
    "plate-opened": r"""
(function () {
  var sec = document.querySelector('[data-plateblock]');
  if (!sec) { return "no band-commit on the page"; }
  var wrap = sec.querySelector('[data-plate]');
  if (!wrap) { return "the block drew no plate"; }
  if (sec.getAttribute('data-stage-done') === '1') {
    return "the stop ticked on load";
  }
  var rows = wrap.querySelectorAll('.ks3-plate-row');
  if (rows.length < 2) { return "fewer than two rows to commit"; }
  var open = wrap.querySelector('[data-plate-open]');
  if (!open) { return "the block offers no reveal"; }
  if (!open.disabled) {
    return "the reveal was open before anything was committed — the gate is the lesson";
  }
  // Commit every row but the last, and check the gate is still shut.
  for (var i = 0; i < rows.length; i++) {
    if (i === rows.length - 1) {
      if (!open.disabled) {
        return "the reveal unlocked with a row still uncommitted";
      }
    }
    var b = rows[i].querySelector('.ks3-plate-band');
    if (!b) { return "a row offers no bands"; }
    b.click();
  }
  if (open.disabled) {
    return "every row is committed and the reveal is still locked";
  }
  open.click();
  var verdict = wrap.querySelector('[data-plate-verdict]');
  if (!verdict || verdict.hasAttribute('hidden')) {
    return "the reveal was pressed and the verdict is still hidden";
  }
  if (!wrap.querySelector('.ks3-plate-why:not([hidden])')) {
    return "the verdict opened with no row explanation showing";
  }
  if (!verdict.querySelector('.ks3-plate-vwhy:not([hidden])')) {
    return "the verdict opened on none of its three branches";
  }
  if (verdict.querySelectorAll('.ks3-plate-vwhy:not([hidden])').length !== 1) {
    return "the verdict opened on more than one branch at once";
  }
  if (!wrap.querySelector('.ks3-plate-row[data-state="hit"]')
      && !wrap.querySelector('.ks3-plate-row[data-state="miss"]')) {
    return "no row reported whether it was placed correctly";
  }
  // R3, asserted here as well as globally: the band buttons are commitments,
  // not answers, so nothing on them may be marked.
  if (wrap.querySelector('.ks3-plate-band[data-correct], .ks3-plate-band.is-correct, .ks3-plate-band.is-wrong')) {
    return "a band button was marked — this block marks no control";
  }
  if (wrap.querySelector('svg.ks3-mark')) {
    return "a drawn tick or cross appears inside band-commit";
  }
  if (sec.getAttribute('data-stage-done') !== '1') {
    return "the answers are open and the stop has not ticked";
  }
  return "";
})()
""",
