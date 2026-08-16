# Splice point: `COMPONENTS` in ks3_parity.py, in the C1 section, directly
# after the collision-counter rows. Uses the same page constant:
#
#     C1_PRESSURE = "chemistry/particles-and-their-behaviour/gas-pressure.html"
#
# ⚠️ THE LAST TWO ROWS NEED A NEW DRIVE. The answered states only exist after
# a click, and no shipped drive reaches them: `dark-option-chosen` clicks the
# first `.ks3-dark .ks3-option`, which on this page is in `#s-hook`, and these
# are segmented buttons rather than lettered options. Splice this into `DRIVES`
# beside the other C1/C2 entries, or drop the two driven rows:
#
#     # Two predictions in one document: one answered right, so the panel
#     # takes the alert border, and one answered wrong, so the shared
#     # fallback note is on screen in its own tone. Both states reached
#     # through the instrument's own buttons, so a regression in the
#     # interaction path fails HERE rather than being measured around.
#     "prediction-answered": r"""
# (function () {
#   var panels = document.querySelectorAll('.ks3-predict');
#   if (panels.length < 2) { return "need 2 predictions, found " + panels.length; }
#   function pick(panel, correct) {
#     var want = parseInt(panel.getAttribute('data-answer'), 10);
#     var opts = panel.querySelectorAll('.ks3-predict-btn');
#     for (var i = 0; i < opts.length; i++) {
#       if ((i === want) === correct) { opts[i].click(); return true; }
#     }
#     return false;
#   }
#   if (!pick(panels[0], true))  { return "no correct option in prediction 1"; }
#   if (!pick(panels[1], false)) { return "no wrong option in prediction 2"; }
#   if (panels[0].getAttribute('data-right') !== '1') {
#     return "the answered prediction did not take its verdict state";
#   }
#   return "";
# })()
# """,

    # ── prediction-stack (c1-04 #s-predict) ──
    # Three panels nested inside an ink-dark block: `--ks3-dark-panel` on the
    # muted rule, which is the same nesting `joint-bench`'s tiles use. If this
    # ever reports the block's own `#221E1B` the panels have stopped being
    # panels and the three predictions read as one wall of text.
    dict(name="prediction panel is a dark panel on a 2px muted rule",
         on=C1_PRESSURE, sel=".ks3-predict",
         props={"background-color": "#3E3730", "border-top-color": "#C6B9A7",
                "border-top-width": "2px", "border-top-left-radius": "20px"}),
    # ⚖️ THE SPECIFICITY ROW. `.ks3-dark p` is (0,1,1) and a bare
    # `.ks3-predict-q` is (0,1,0): unscoped, the question renders in on-dark
    # BODY copy at whatever weight the cascade leaves it, which is the defect
    # B1 shipped and B2 repeated. `#FBF3E6` at 600 is the proof it is scoped.
    dict(name="prediction question is on-dark 600, not on-dark body",
         on=C1_PRESSURE, sel=".ks3-predict-q",
         props={"color": "#FBF3E6", "font-size": "18px",
                "font-weight": "600"}),
    # The panel — never the option — carries the verdict.
    dict(name="a matched prediction takes the ALERT border, on the panel",
         on=C1_PRESSURE, drive="prediction-answered",
         sel='.ks3-predict[data-right="1"]',
         props={"border-top-color": "#FFC53D", "border-top-width": "2px",
                "background-color": "#3E3730"}),
    # The one shared fallback, in the ink-dark palette's lit colour. 7.4:1 on
    # the panel; if it ever falls back to on-dark body it stops being
    # distinguishable from the note that says the student had it right.
    dict(name="the shared wrong-answer note is alert, not on-dark body",
         on=C1_PRESSURE, drive="prediction-answered",
         sel='.ks3-predict-note[data-tone="wrong"]',
         props={"color": "#FFC53D", "font-size": "17px"}),


# ── DRIVES entries ───────────────────────────────────────────────────────
# ⊕ This section SUPERSEDES the commented sketch in this file's header.
# Splice from here; the header copy is prose and is now out of date.

    # Two predictions in one document: one answered WRONGLY, so the shared
    # fallback note is on screen in its own tone, and one answered RIGHTLY, so
    # its panel takes the alert border. Both states reached through the
    # instrument's own buttons, so a regression in the interaction path fails
    # HERE rather than being measured around.
    #
    # ⚠️ THE ORDER IS LOAD-BEARING, AND IT IS THE OPPOSITE OF THE OBVIOUS ONE.
    # Both rows are measured with `document.querySelector`, which takes the
    # FIRST match in document order, and `.ks3-predict-note[data-tone="wrong"]`
    # carries no `:not([hidden])` — every panel emits both notes and hides one.
    # Answer panel 1 right and its wrong note stays `hidden`, so that row would
    # resolve to a display:none paragraph, still report a colour, and PASS
    # having measured nothing a student can see. Answering panel 1 wrong puts a
    # visible wrong note at the head of the document, and panel 2 right is then
    # the first `[data-right="1"]`. Both rows land on live elements.
    #
    # The answer index is read from each panel's own `data-answer` and matched
    # against the buttons' `data-i`, so re-authoring which option is correct —
    # or how many options there are — cannot quietly invert this.
    "prediction-answered": r"""
(function () {
  var panels = document.querySelectorAll('.ks3-predict');
  if (panels.length < 2) {
    return "need 2 predictions to hold both states at once, found " +
           panels.length;
  }
  function pick(panel, correct) {
    var want = parseInt(panel.getAttribute('data-answer'), 10);
    if (isNaN(want)) { return false; }
    var opts = panel.querySelectorAll('.ks3-predict-btn');
    for (var i = 0; i < opts.length; i++) {
      var idx = parseInt(opts[i].getAttribute('data-i'), 10);
      if ((idx === want) === correct) { opts[i].click(); return true; }
    }
    return false;
  }
  if (!pick(panels[0], false)) { return "no wrong option in prediction 1"; }
  if (!pick(panels[1], true)) { return "no correct option in prediction 2"; }
  if (panels[0].getAttribute('data-right') !== '0') {
    return "prediction 1 was answered wrongly and did not record it";
  }
  if (panels[1].getAttribute('data-right') !== '1') {
    return "prediction 2 was answered correctly and did not record it";
  }
  var note = panels[0].querySelector('.ks3-predict-note[data-tone="wrong"]');
  if (!note) { return "prediction 1 carries no wrong-answer note"; }
  if (note.hasAttribute('hidden')) {
    return "a prediction was answered wrongly and the shared note is still hidden";
  }
  return "";
})()
""",
