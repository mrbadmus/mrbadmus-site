/* WIRE: each(root.querySelectorAll("[data-tbenchblock]"), wireTestBench);
   — add to wireInstruments(), in the B3 group. Uses each / toArray /
   setHidden / setCount / markStage, all already in scope. */

  /* ═══════════════════════════════════════════════════════════════
     ── test-bench (b3-02 #s-bench) — the prediction runs the test ──

     Five foods × four tests. Pick a pair, say what you expect, and the
     saying is what runs it: there is no separate run button, because a
     student who can see the colour first has not predicted anything.

     ⚖️ THE RUN LATCHES, AND SO DOES THE PREDICTION. Design re-reads the
     stored prediction every render, so a student who changed their answer
     after the tube had changed colour would be told "You predicted this"
     — the block would congratulate them for the thing it exists to stop.
     The first press of a combination is the one that scores it, exactly
     as c1-06's evidence bench latches its first call. Pressing again
     still MOVES the pressed state (R3 requires every option to render
     alike whichever was chosen), it simply does not rewrite history.

     ⚖️ NOTHING IS ASSEMBLED HERE. All twenty prompts, all twenty results,
     all twenty claim lines, the four methods and the nine tube-state
     names are already in the document, and this function only changes
     which is hidden. That is what keeps the em dashes, the curly quotes
     and the `<strong>` in the claim line intact — and every one of those
     sentences is the science of the lesson rather than chrome.

     ⚠️ R3 — NOTHING MARKS. The two prediction options are ordinary
     activity options: they show that they were chosen and nothing else,
     they are never disabled, and neither carries `data-correct`. The
     verdict line that follows reports whether the prediction matched the
     tube — which is a fact about the world, printed in the result panel,
     not a mark on a button.

     ⚖️ NOTHING RUNS ON A CLOCK. The tube's colour transition is a CSS
     one and `prefers-reduced-motion` turns it off in the stylesheet, so
     there is nothing to scale here and the reduced-motion experience is
     the complete one: the state line beside the tube says the colour in
     words either way (R2).
     ═══════════════════════════════════════════════════════════════ */
  function wireTestBench(sec) {
    var wrap = sec.querySelector("[data-tbench]");
    if (!wrap) { return; }
    var predictWrap = wrap.querySelector("[data-predict]");
    var opts = toArray(wrap.querySelectorAll(".ks3-option"));
    var tube = wrap.querySelector("[data-tube]");
    var state = wrap.querySelector("[data-state]");
    if (!predictWrap || !opts.length || !tube || !state) { return; }

    var target = parseInt(wrap.getAttribute("data-target"), 10) || 4;
    var ran = {};         // "food:test" -> the option index pressed FIRST
    var count = 0;

    function key() {
      return wrap.getAttribute("data-food") + ":" + wrap.getAttribute("data-test");
    }

    function paint() {
      var k = key();
      var food = wrap.getAttribute("data-food");
      var test = wrap.getAttribute("data-test");
      var testTab = wrap.querySelector(".ks3-tbench-tab[data-test='" + test + "']");
      var done = Object.prototype.hasOwnProperty.call(ran, k);
      var result = wrap.querySelector("[data-result='" + k + "']");

      each(wrap.querySelectorAll(".ks3-tbench-tab[data-food]"), function (b) {
        b.setAttribute("aria-pressed",
          b.getAttribute("data-food") === food ? "true" : "false");
      });
      each(wrap.querySelectorAll(".ks3-tbench-tab[data-test]"), function (b) {
        b.setAttribute("aria-pressed",
          b.getAttribute("data-test") === test ? "true" : "false");
      });
      each(wrap.querySelectorAll("[data-lfood]"), function (s) {
        setHidden(s, s.getAttribute("data-lfood") !== food);
      });
      each(wrap.querySelectorAll("[data-ltest]"), function (s) {
        setHidden(s, s.getAttribute("data-ltest") !== test);
      });
      each(wrap.querySelectorAll("[data-method]"), function (p) {
        setHidden(p, p.getAttribute("data-method") !== test);
      });
      each(wrap.querySelectorAll("[data-detects]"), function (p) {
        setHidden(p, p.getAttribute("data-detects") !== test);
      });
      each(wrap.querySelectorAll("[data-prompt]"), function (p) {
        setHidden(p, p.getAttribute("data-prompt") !== k);
      });
      each(wrap.querySelectorAll("[data-result]"), function (d) {
        setHidden(d, !done || d.getAttribute("data-result") !== k);
      });

      /* An unrun combination shows the reagent's UNCHANGED colour — the
         negative — because that is what is in the tube before the food goes
         in. The colours ride on the test tab for exactly this: the resting
         tube needs one before any result panel exists. */
      var colour = done && result
        ? result.getAttribute("data-colour")
        : (testTab ? testTab.getAttribute("data-neg") : "");
      if (colour) { tube.style.background = colour; }
      tube.setAttribute("data-run", done ? "1" : "0");

      // The state line: nine authored spans, one shown. Never composed.
      var outcome = done && result ? result.getAttribute("data-outcome") : "";
      var want = outcome ? test + ":" + outcome : "rest";
      each(state.querySelectorAll("[data-sname]"), function (s) {
        setHidden(s, s.getAttribute("data-sname") !== want);
      });

      // Gating by ABSENCE, as C6's bench gate does: a combination that has
      // been run has no question left to ask.
      setHidden(predictWrap, done);
      each(opts, function (b) {
        b.setAttribute("aria-pressed",
          done && String(ran[k]) === b.getAttribute("data-i") ? "true" : "false");
      });
      if (done && result) {
        /* Option 0 is "Yes — it will change colour" and option 1 is "No".
           The prediction matched if the yes/no the student pressed agrees
           with the outcome the payload records for this combination. */
        var hit = (ran[k] === 0) === (outcome === "pos");
        each(result.querySelectorAll("[data-verdict]"), function (p) {
          setHidden(p, p.getAttribute("data-verdict") !== (hit ? "hit" : "miss"));
        });
      }
      setCount(sec, count);
      if (count >= target) { markStage(sec, true); }   // `four_run`
    }

    each(wrap.querySelectorAll(".ks3-tbench-tab[data-food]"), function (b) {
      b.addEventListener("click", function () {
        wrap.setAttribute("data-food", b.getAttribute("data-food"));
        paint();
      });
    });
    each(wrap.querySelectorAll(".ks3-tbench-tab[data-test]"), function (b) {
      b.addEventListener("click", function () {
        wrap.setAttribute("data-test", b.getAttribute("data-test"));
        paint();
      });
    });

    each(opts, function (btn) {
      btn.addEventListener("click", function () {
        var k = key();
        // The FIRST press is the one that scores. A later press moves the
        // pressed state and nothing else — see the header.
        if (!Object.prototype.hasOwnProperty.call(ran, k)) {
          ran[k] = parseInt(btn.getAttribute("data-i"), 10);
          count += 1;
          paint();
          return;
        }
        each(opts, function (b) { b.setAttribute("aria-pressed", b === btn ? "true" : "false"); });
      });
    });

    paint();
  }
