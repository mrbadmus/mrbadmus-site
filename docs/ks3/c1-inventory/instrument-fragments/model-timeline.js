/* WIRE: each(root.querySelectorAll("[data-mtlblock]"), wireModelTimeline);
   — add to wireInstruments(), in the C1 group. Uses each / toArray /
   setHidden / markStage, all already in scope. */

  /* ── model-timeline (c1-06 #s-history) ──
     Five models, one detail card, emit-all-show-one: every card is in the
     document and one is shown, so going back to a model finds it as it was
     and no authored sentence is ever rebuilt from an attribute.

     ⚖️ THE STAGE PREDICATE IS A SET AND IT NEVER EMPTIES. Design's page ticks
     on `history !== 1` — an inequality against the DEFAULT — so the stage
     ticks when any other model is opened and UNTICKS when a student who has
     read all five returns to Dalton. A rail stop that goes backwards is worse
     than one that never moved. What the page means is "has looked at more
     than the one it opened on", which is a set: seed it with the default,
     add on every press, tick at two, never remove. Same class of defect as
     c1-04's `Math.max(touched, N)`.

     No timer, no animation, nothing to scale under reduced motion. */
  function wireModelTimeline(sec) {
    var wrap = sec.querySelector("[data-mtl]");
    if (!wrap) { return; }
    var btns = toArray(wrap.querySelectorAll(".ks3-mtl-step"));
    var cards = toArray(wrap.querySelectorAll(".ks3-mtl-card"));
    if (!btns.length) { return; }

    // The row opens on Dalton, not on Democritus. Seeding the set with the
    // default is what makes "more than the default" mean what it says.
    var seen = {};
    seen[wrap.getAttribute("data-default") || "0"] = true;

    function counted() {
      var n = 0, k;
      for (k in seen) { if (seen[k]) { n += 1; } }
      return n;
    }

    each(btns, function (btn) {
      btn.addEventListener("click", function () {
        var i = btn.getAttribute("data-step");
        each(btns, function (b) {
          b.setAttribute("aria-pressed",
            b.getAttribute("data-step") === i ? "true" : "false");
        });
        each(cards, function (c) {
          setHidden(c, c.getAttribute("data-step") !== i);
        });
        seen[i] = true;
        // Sticky in one direction only: a stage that has been reached stays
        // reached, whatever the student looks at next.
        if (counted() >= 2) { markStage(sec, true); }
      });
    });
  }
