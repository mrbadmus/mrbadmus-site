/* WIRE: each(root.querySelectorAll("[data-ebenchblock]"), wireEvidenceBench);
   — add to wireInstruments(), in the C1 group. Uses each / toArray /
   setHidden / setCount / markStage / appendAuthored, all already in scope. */

  /* ── evidence-bench (c1-06 #s-bench) ──
     Seven observations, each judged once and answered immediately. No gate:
     the seven judgements ARE the commitment, which is why this is the one
     flagship instrument in C1 that is open from the start.

     ⚖️ THE SCORED CALL IS LATCHED ON THE FIRST PRESS. Design recomputes the
     tally from live state, so a student who changes an answer after reading
     the verdict moves a number whose own sentence says "before opening the
     verdict". `data-called` records the first call and never moves; the
     buttons stay live because Design leaves them live and pressing again
     changes nothing else.

     ⚠️ NOTHING HERE MARKS THE STUDENT (R3 / MRB-196 R10). The verdict panel's
     ground is a fact about the model, decided at build time from `ok`. This
     function never compares a call to it except to count, and the count is
     never attached to a case. */
  function wireEvidenceBench(sec) {
    var wrap = sec.querySelector("[data-ebench]");
    if (!wrap) { return; }
    var cases = toArray(wrap.querySelectorAll(".ks3-ebench-case"));
    var total = parseInt(wrap.getAttribute("data-total"), 10) || cases.length;
    var panel = wrap.querySelector("[data-ebench-tally]");
    var line = wrap.querySelector("[data-tallyline]");
    var fmt = wrap.getAttribute("data-tally") || "";
    var allLabel = wrap.getAttribute("data-all") || "";
    // The block-head counter belongs to the shell, not to this instrument;
    // `setCount` writes it for every other counting block and this one only
    // reaches past it for the authored full-set label, which `_head_counter`
    // has no branch for.
    var counter = sec.querySelector("[data-count]");

    function judged() {
      var n = 0;
      each(cases, function (c) {
        if (c.getAttribute("data-open") === "1") { n += 1; }
      });
      return n;
    }

    /* How many the student CALLED right, from the latched first press. */
    function called() {
      var n = 0;
      each(cases, function (c) {
        var call = c.getAttribute("data-called");
        if (call !== null && call === c.getAttribute("data-ok")) { n += 1; }
      });
      return n;
    }

    function close() {
      if (line) {
        line.textContent = "";
        // Authored text, never textContent: the sentence carries an em dash
        // today and the helper is what draws → ✓ ✕ if one ever arrives.
        appendAuthored(line, fmt.split("{n}").join(String(called())));
      }
      if (panel) { setHidden(panel, false); }
      if (counter && allLabel) {
        counter.textContent = "";
        appendAuthored(counter, allLabel);
      }
      markStage(sec, true);
    }

    each(cases, function (c) {
      var btns = toArray(c.querySelectorAll(".ks3-ebench-btn"));
      each(btns, function (btn) {
        btn.addEventListener("click", function () {
          each(btns, function (b) { b.setAttribute("aria-pressed", "false"); });
          btn.setAttribute("aria-pressed", "true");
          if (c.getAttribute("data-called") === null) {
            c.setAttribute("data-called", btn.getAttribute("data-call"));
          }
          c.setAttribute("data-open", "1");
          setHidden(c.querySelector("[data-reveal]"), false);
          var n = judged();
          if (n >= total) { close(); } else { setCount(sec, n); }
        });
      });
    });

    setCount(sec, 0);
  }
