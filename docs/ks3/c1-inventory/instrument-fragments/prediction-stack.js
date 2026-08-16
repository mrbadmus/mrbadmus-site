// WIRE: each(root.querySelectorAll("[data-predictblock]"), wirePredictionStack);
//
// Splice point: `wireInstruments()` in shared/ks3.js, in the new
// "C1 · Particles and their behaviour" group, beside wireCollisionCounter.
// Uses the file's existing `each`, `toArray`, `setHidden` and `markStage`.

  /* ── prediction-stack (c1-04 #s-predict) ──
     Three predictions, one shared option set, one shared fallback.

     ⚖️ A PREDICTION MAY BE CHANGED. Design's state is a map from
     prediction id to index and a second press overwrites it, so a
     student who reads "go back to the bench and try it" can come back
     and answer again — which is exactly what that sentence asks them to
     do. Locking the row after one press would make the instruction
     impossible to follow.

     ⚖️ THE PANEL CARRIES THE VERDICT, NOT THE OPTION. The chosen button
     keeps the ordinary chosen treatment; what changes is the panel's
     border and which of the two notes is showing. Nothing inside the
     option list marks the student.

     Both notes are already in the document — this only unhides one, so
     no student-facing string is ever built here. */
  function wirePredictionStack(sec) {
    var wrap = sec.querySelector("[data-predictstack]");
    if (!wrap) { return; }
    var panels = toArray(wrap.querySelectorAll(".ks3-predict"));
    var total = parseInt(wrap.getAttribute("data-total"), 10) || panels.length;
    var answered = {};

    each(panels, function (panel) {
      var id = panel.getAttribute("data-prediction");
      var answer = parseInt(panel.getAttribute("data-answer"), 10);
      var opts = toArray(panel.querySelectorAll(".ks3-predict-btn"));
      var right = panel.querySelector('[data-tone="right"]');
      var wrong = panel.querySelector('[data-tone="wrong"]');

      each(opts, function (btn) {
        btn.addEventListener("click", function () {
          var i = parseInt(btn.getAttribute("data-i"), 10);
          each(opts, function (b) {
            b.setAttribute("aria-pressed", b === btn ? "true" : "false");
          });
          var ok = i === answer;
          panel.setAttribute("data-right", ok ? "1" : "0");
          setHidden(right, !ok);
          setHidden(wrong, ok);

          answered[id] = true;
          var n = 0, k;
          for (k in answered) { if (answered[k]) { n += 1; } }
          if (n >= total) { markStage(sec, true); }
        });
      });
    });
  }
