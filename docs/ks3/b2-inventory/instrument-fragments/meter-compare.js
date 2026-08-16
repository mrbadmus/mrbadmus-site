/* WIRE: each(root.querySelectorAll("[data-metersblock]"), wireMeterCompare);
   — add to wireInstruments(), in the B2 group. Uses each / toArray /
   setHidden / setCount / markStage, all already in scope. */

  /* ═══════════════════════════════════════════════════════════════
     ── meter-compare (b2-04 #s-meters) — measured, not guessed ──

     Rank three muscle groups, then read what a force meter actually says
     about each of them: three readings and their mean.

     ⚖️ ONE COMMITMENT, ALL THREE CARDS. `job-sort` and `verdict-cards`
     reveal per item, the instant that item is decided, and that sequence
     is the pedagogy in both. It cannot be that here: the commitment is
     about the ORDER of the three groups, and revealing one card would
     give away part of the answer to the question still being asked.

     ⚠️ R3 — NOTHING MARKS. All three orderings render identically and all
     three open the same cards. There is no `data-correct` in this
     instrument and there must not be: `answer_index` is checked against
     the rows' own means at build time and never reaches the page. The
     choice also stays changeable — a student who reads the means and
     wants to change their mind is the block working, not a leak.

     ⚖️ THE MEAN IS THE SECOND LESSON, and it is why the readings are in
     the document rather than composed here: 312, 298 and 305 disagree,
     and the closing band says in words that one pull would have told you
     almost nothing. Nothing in this function builds a number.

     ⚖️ NOTHING ANIMATES and nothing counts, so `prefers-reduced-motion`
     has nothing to degrade and the reduced-motion experience is the
     complete one.
     ═══════════════════════════════════════════════════════════════ */
  function wireMeterCompare(sec) {
    var wrap = sec.querySelector("[data-meters]");
    if (!wrap) { return; }
    var opts = toArray(wrap.querySelectorAll(".ks3-option"));
    var panel = wrap.querySelector("[data-reveal]");
    if (!opts.length || !panel) { return; }

    each(opts, function (btn) {
      btn.addEventListener("click", function () {
        var i = btn.getAttribute("data-i");
        each(opts, function (b) {
          b.setAttribute("aria-pressed",
            b.getAttribute("data-i") === i ? "true" : "false");
        });
        if (panel.hasAttribute("hidden")) {
          setHidden(panel, false);
          // Announced for screen-reader users, who would otherwise get no
          // signal that three cards of data appeared below the buttons.
          panel.setAttribute("role", "status");
        }
        // The block-head readout is a two-state label here ("Not ranked yet"
        // → "Ranked"), not a count — there is one thing to report and it is
        // a boolean. `setCount` carries that shape.
        setCount(sec, 1);
        markStage(sec, true);   // `ranked`
      });
    });
  }
