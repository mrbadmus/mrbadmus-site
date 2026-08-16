/* WIRE: each(root.querySelectorAll("[data-gutblock]"), wireGutJourney);
   — add to wireInstruments(), in the B3 group. Uses each / toArray /
   setHidden / setCount / markStage, all already in scope. */

  /* ── gut-journey (b3-05 #s-journey) ──
     Follow one meal through seven stops, with a time chart under them
     that contradicts the intuition the lesson opens with.

     ⚖️ NOTHING HERE BUILDS A NUMBER OR A WIDTH. Every bar width is inline
     in the document, computed in `r_gut_journey` from the same `hours`
     the printed figure beside it is authored from. This function moves
     the HIGHLIGHT — which row is lit, which panel is shown — and nothing
     else. A width set here would be a second source for one quantity,
     and the two would eventually stop agreeing.

     ⚖️ THE OPEN STOP IS SEEDED AS VISITED, and that is a real difference
     from the c1-02 precedent rather than a copy of Design's defect.
     c1-02's bench counted the state it was ABOUT to show while the whole
     instrument was still behind a commit gate, so the readout claimed
     something the student could not yet have seen. There is no gate here:
     stop one is on screen, complete, from first paint. "1 of 7 stops
     visited" is therefore true at rest — and the stage still needs six
     more taps, so nothing ticks on load (MRB-208).

     ⚖️ EVERY STOP, not five of seven. The stage is the whole journey
     because the journey is the block's argument: a student who stops at
     the small intestine has met the organ that does the work and not the
     two that follow it, and egestion-is-not-excretion is on the last one.

     ⚖️ NOTHING ANIMATES and nothing counts, so `prefers-reduced-motion`
     has nothing to degrade here — the only transition in the component is
     the highlight's colour, and the stylesheet's own reduced-motion block
     already removes it. The reduced-motion experience is the complete
     one. */
  function wireGutJourney(sec) {
    var wrap = sec.querySelector("[data-gut]");
    if (!wrap) { return; }
    var tabs = toArray(wrap.querySelectorAll(".ks3-gut-tab"));
    var panels = toArray(wrap.querySelectorAll(".ks3-gut-stop"));
    var rows = toArray(wrap.querySelectorAll(".ks3-gut-row"));
    var total = parseInt(wrap.getAttribute("data-total"), 10) || panels.length;
    if (!panels.length) { return; }

    var seen = {};

    function show(id) {
      each(tabs, function (tab) {
        tab.setAttribute("aria-pressed",
          tab.getAttribute("data-stop") === id ? "true" : "false");
      });
      each(panels, function (p) {
        setHidden(p, p.getAttribute("data-stop") !== id);
      });
      each(rows, function (r) {
        if (r.getAttribute("data-stop") === id) {
          r.setAttribute("data-lit", "1");
        } else {
          r.removeAttribute("data-lit");
        }
      });
      seen[id] = true;
      var n = 0, k;
      for (k in seen) { if (seen[k]) { n += 1; } }
      setCount(sec, n);
      markStage(sec, n >= total);
    }

    each(tabs, function (tab) {
      tab.addEventListener("click", function () {
        show(tab.getAttribute("data-stop"));
      });
    });

    /* Seed from the panel that is actually showing rather than from index
       zero, so the renderer stays free to open on a different stop without
       the count and the picture disagreeing. */
    var open = wrap.querySelector(".ks3-gut-stop:not([hidden])");
    if (open) { show(open.getAttribute("data-stop")); }
  }
