/* WIRE: each(root.querySelectorAll("[data-foldblock]"), wireFoldBuilder);
   — add to wireInstruments(), in a new B3 group. Uses each / toArray /
   setHidden / setCount / markStage, all already in scope. */

  /* ═══════════════════════════════════════════════════════════════
     ── fold-builder (b3-07 #s-fold) — build the surface up ──

     Three toggles, three multipliers, one area. Start at half a square
     metre of plain tube and end at about thirty, with the length written
     beside it never moving.

     ⚖️ ONLY THE NUMBERS ARE BUILT HERE. All four notes are in the
     document — one per COUNT of levels, not one per level — and this
     function swaps which is shown. Every sentence a student reads about
     the folding was authored in the lesson record, so the em dashes and
     the `<em>` survive and nothing science-bearing is assembled from an
     attribute. What IS assembled is an area and a multiple, which is
     what an arithmetic readout is for.

     ⚠️ THE NUMBER FORMAT IS DUPLICATED, DELIBERATELY. `areaText` and
     `multText` below are the same rule as `_fold_area_text` /
     `_fold_multiple_text` in build_ks3.py, which fill the RESTING
     render. Two copies of four lines buys HTML that already says
     "0.50 m²" before any script runs — the same trade `head_counter`'s
     `start` makes one level up. `Math.round` and Python's `int(v + 0.5)`
     were matched on purpose; `round()` would have rounded half to even
     and disagreed at exactly 10.5.

     ⚖️ THE STOP LATCHES, and Design's own predicate does not. Design
     recomputes `s.on.folds && s.on.villi && s.on.microvilli` every
     render, so a student who builds all three levels and then switches
     one back off to look at it again has their rail stop taken away
     from them. MRB-208 ruled the rail records PARTICIPATION: a stop
     ticks when the activity is finished, and nothing un-finishes it.
     So `markStage` is only ever called with `true` here. The BAR and
     the NOTE still follow the live state, because those are claims
     about the model currently on screen and would be false if they
     latched.

     ⚖️ NOTHING TICKS AND NOTHING COUNTS DOWN. NOTES-B3 §6 is explicit
     that `enzyme-run` is the only instrument in the unit with a timer;
     the one animation here is a CSS width transition, which the
     stylesheet degrades under `prefers-reduced-motion` itself. There is
     no rate for this function to scale, and the reduced-motion
     experience is the complete one. (Same standing as `meter-compare`.)
     ═══════════════════════════════════════════════════════════════ */
  function wireFoldBuilder(sec) {
    var wrap = sec.querySelector("[data-fold]");
    if (!wrap) { return; }
    var levels = toArray(wrap.querySelectorAll("[data-level]"));
    if (!levels.length) { return; }

    var areaEl = wrap.querySelector("[data-fold-area]");
    var barEl = wrap.querySelector("[data-fold-bar]");
    var multEl = wrap.querySelector("[data-fold-multiple]");
    var notes = toArray(wrap.querySelectorAll("[data-note]"));

    var base = parseFloat(wrap.getAttribute("data-base"));
    if (!base || base <= 0) { return; }
    var areaFmt = wrap.getAttribute("data-area-format") || "{a}";
    var multFmt = wrap.getAttribute("data-multiple-format") || "{x}";

    function factorOf(li) {
      var f = parseFloat(li.getAttribute("data-factor"));
      return f > 0 ? f : 1;
    }

    // The full stack, computed once: the bar is a fraction of what the
    // finished model comes to, not of a magic number.
    var most = base;
    each(levels, function (li) { most *= factorOf(li); });

    function areaText(v) {
      if (v < 1) { return v.toFixed(2); }
      if (v < 10) { return v.toFixed(1); }
      return String(Math.round(v));
    }
    function multText(r) {
      return r < 10 ? r.toFixed(1) : String(Math.round(r));
    }

    function refresh() {
      var area = base, on = 0;
      each(levels, function (li) {
        if (li.getAttribute("data-on") === "1") {
          area *= factorOf(li);
          on += 1;
        }
      });
      if (areaEl) {
        areaEl.textContent = areaFmt.split("{a}").join(areaText(area));
      }
      if (multEl) {
        multEl.textContent = multFmt.split("{x}").join(multText(area / base));
      }
      if (barEl) {
        // A floor of 2%, so the plain tube is a visible sliver rather than
        // an empty track that reads as "no data" instead of "half a square
        // metre".
        barEl.style.width = Math.max(2, (area / most) * 100).toFixed(1) + "%";
        barEl.setAttribute("data-full", on === levels.length ? "1" : "0");
      }
      each(notes, function (p) {
        setHidden(p, p.getAttribute("data-note") !== String(on));
      });
      setCount(sec, on);
      if (on === levels.length) { markStage(sec, true); }
    }

    each(levels, function (li) {
      var btn = li.querySelector("[data-fold-toggle]");
      if (!btn) { return; }
      btn.addEventListener("click", function () {
        var on = li.getAttribute("data-on") !== "1";
        li.setAttribute("data-on", on ? "1" : "0");
        btn.setAttribute("aria-pressed", on ? "true" : "false");
        // Both faces were finished at build time — "Add this level" and
        // "On · ×7" — so nothing here composes a label out of a factor.
        btn.textContent = btn.getAttribute(on ? "data-label-on"
                                              : "data-label-off") || "";
        refresh();
      });
    });

    // Opens on the plain tube: 0 of 3, 0.50 m², ×1.0, note zero. That is
    // what the HTML already says, so this call changes nothing on load — it
    // is here so there is exactly one place the readout is computed.
    refresh();
  }
