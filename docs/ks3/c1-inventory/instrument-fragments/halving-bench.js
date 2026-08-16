/* WIRE: each(root.querySelectorAll("[data-cutblock]"), wireHalvingBench); */

  /* ═══════════════════════════════════════════════════════════════
     C1 · Particles and their behaviour  (⊕ MRB-228)

     ── halving-bench (c1-01 #s-cut) ──

     ⚖️ THE FLOOR IS STICKY. Reaching 24 cuts ticks the rail stop and
     undoing a cut does not untick it. Design's `reachedFloor` is a
     one-way flag and this keeps it one-way: what a student found out at
     the floor cannot be un-found by pressing undo, and MRB-208 has the
     rail recording participation rather than current position.

     ⚖️ NOTHING ANIMATES. "Cut ten more times" moves the count by ten in
     one frame because ten halvings is not a journey — the point is that
     the number falls off a cliff and the substance does not change. So
     `prefers-reduced-motion` has nothing to degrade here (the same note
     `wireClaimSwitch` carries), and the reduced-motion experience is the
     complete one rather than a lesser one.

     The size ladder is duplicated in `build_ks3.py` (`_size_label`) on
     purpose: the resting page has to render "10 mm" and its aria-label
     before any JS runs. Two implementations, one composition, checked at
     both ends of the ladder.
     ═══════════════════════════════════════════════════════════════ */
  function wireHalvingBench(sec) {
    var wrap = sec.querySelector("[data-cut]");
    if (!wrap) { return; }

    var FLOOR = parseInt(wrap.getAttribute("data-floor"), 10) || 0;
    var START = parseFloat(wrap.getAttribute("data-start-cm")) || 1;
    var GRAIN = parseInt(wrap.getAttribute("data-grain"), 10) || 0;
    var FULL = wrap.getAttribute("data-full") || "";
    var ALT = wrap.getAttribute("data-alt") || "";
    var ALT_SMOOTH = wrap.getAttribute("data-alt-smooth") || "";
    var ALT_GRAINY = wrap.getAttribute("data-alt-grainy") || "";
    var L_GHOST = wrap.getAttribute("data-label-ghost") || "";
    var L_ONE = wrap.getAttribute("data-label-one") || "";
    var L_MANY = wrap.getAttribute("data-label-many") || "";
    var L_START = wrap.getAttribute("data-label-start") || "";
    var L_END = wrap.getAttribute("data-label-end") || "";

    var canvas = wrap.querySelector("[data-cut-canvas]");
    var outCount = wrap.querySelector('[data-cut-out="count"]');
    var outSize = wrap.querySelector('[data-cut-out="size"]');
    var verdicts = toArray(wrap.querySelectorAll("[data-verdict]"));
    var notes = toArray(wrap.querySelectorAll("[data-note]"));
    var btns = toArray(wrap.querySelectorAll(".ks3-cut-btn"));
    var counter = sec.querySelector("[data-count]");

    var n = 0;
    var reached = false;

    /* Design's `sig()`. `Math.round` on the top branch, one trailing zero
       stripped on the bottom one — reproduced rather than tidied, because
       the same formatter runs at build time in Python and the two have to
       agree digit for digit. */
    function sig(v) {
      if (v >= 100) { return String(Math.round(v)); }
      if (v >= 10) { return v.toFixed(1).replace(/\.0$/, ""); }
      return v.toFixed(2).replace(/0$/, "").replace(/\.$/, "");
    }

    /* 1 cm / 2ⁿ, in the unit that keeps it readable. µ is U+00B5, which
       both faces this lands in — the display face in the readout, DM Mono
       on the canvas — actually carry. */
    function sizeLabel(k) {
      var cm = START / Math.pow(2, k);
      if (cm >= 0.1) { return sig(cm * 10) + " mm"; }
      if (cm >= 1e-4) { return sig(cm * 1e4) + " µm"; }
      return sig(cm * 1e7) + " nm";
    }

    function grainy() { return n >= FLOOR - GRAIN; }

    function branch() {
      // Design's own order: the floor first, then the grain, then the
      // untouched cube, then the long middle.
      if (n >= FLOOR) { return "at_floor"; }
      if (grainy()) { return "near_floor"; }
      if (n === 0) { return "at_start"; }
      return "mid";
    }

    function altText() {
      return ALT.replace("{n}", String(n))
        .replace("{size}", sizeLabel(n))
        .replace("{tail}", grainy() ? ALT_GRAINY : ALT_SMOOTH);
    }

    function draw() {
      if (!canvas || !canvas.getContext) { return; }
      var ctx = canvas.getContext("2d");
      var W = 900, H = 320;
      ctx.setTransform(1, 0, 0, 1, 0, 0);
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      ctx.setTransform(2, 0, 0, 2, 0, 0);
      ctx.fillStyle = "#FFFDF8";
      ctx.fillRect(0, 0, W, H);

      var cx = W / 2, cy = H / 2 - 4;
      var box = 176;

      // The ghost of the piece before this cut, at twice the size. Its top
      // and bottom edges run off the canvas on purpose — the piece you
      // just halved does not fit any more, which is the whole point.
      if (n > 0) {
        ctx.strokeStyle = "#D9CDBA";
        ctx.lineWidth = 2;
        ctx.setLineDash([7, 6]);
        ctx.strokeRect(cx - box, cy - box, box * 2, box * 2);
        ctx.setLineDash([]);
        ctx.fillStyle = "#A79A88";
        ctx.font = '500 13px "DM Mono", ui-monospace, monospace';
        ctx.textAlign = "left";
        // ⊕ CLAMPED, and this is a correction. Design draws this caption at
        // `cy - box - 10`, which is y = -30 in a 320-tall design space: the
        // string is painted off the top of the canvas and no student has
        // ever seen it. Clamped to the first line inside the frame, so the
        // label lands where the ghost box actually is.
        ctx.fillText(L_GHOST, cx - box, Math.max(cy - box - 10, 16));
      }

      if (!grainy()) {
        ctx.fillStyle = "#F2E4CB";
        ctx.fillRect(cx - box / 2, cy - box / 2, box, box);
        ctx.fillStyle = "#FBF3E6";
        ctx.fillRect(cx - box / 2, cy - box / 2, box, box * 0.22);
        ctx.strokeStyle = "#1A1714";
        ctx.lineWidth = 2.5;
        ctx.strokeRect(cx - box / 2, cy - box / 2, box, box);
      } else {
        // Close to the floor the piece stops being a block and resolves
        // into a countable number of particles. `across` is 2^(FLOOR - n),
        // so it doubles every time a cut is undone and is 1 at the floor.
        var across = Math.max(1, Math.pow(2, FLOOR - n));
        var r = (box / across) / 2;
        ctx.save();
        for (var row = 0; row < across; row++) {
          for (var col = 0; col < across; col++) {
            ctx.beginPath();
            ctx.arc(cx - box / 2 + r + col * r * 2,
                    cy - box / 2 + r + row * r * 2, r * 0.92, 0, Math.PI * 2);
            ctx.fillStyle = "#E8D3AC";
            ctx.fill();
            ctx.strokeStyle = "#8A7355";
            ctx.lineWidth = Math.min(2.5, r * 0.28);
            ctx.stroke();
            if (r > 12) {
              ctx.beginPath();
              ctx.arc(cx - box / 2 + r + col * r * 2 - r * 0.3,
                      cy - box / 2 + r + row * r * 2 - r * 0.32,
                      r * 0.24, 0, Math.PI * 2);
              ctx.fillStyle = "rgba(255,255,255,0.7)";
              ctx.fill();
            }
          }
        }
        ctx.restore();
        ctx.strokeStyle = "#1A1714";
        ctx.lineWidth = 2.5;
        ctx.strokeRect(cx - box / 2, cy - box / 2, box, box);
        ctx.fillStyle = "#A93411";
        ctx.font = '500 13px "DM Mono", ui-monospace, monospace';
        ctx.textAlign = "center";
        // ⚑ The count is across ONE FACE, and the words say PARTICLES LEFT.
        // Design's wording, kept exactly (see the lesson module's science
        // note): the drawing is a cross-section, so a face count is what is
        // on screen, but a cube 16 particles on an edge holds 16³.
        ctx.fillText(across === 1 ? L_ONE
                     : L_MANY.replace("{n}", String(across * across)),
                     cx, cy + box / 2 + 24);
      }

      // The scale bar: the number is the lesson, so it gets its own rule.
      ctx.strokeStyle = "#1A1714";
      ctx.lineWidth = 2;
      ctx.beginPath();
      ctx.moveTo(cx - box / 2, cy + box / 2 + 46);
      ctx.lineTo(cx + box / 2, cy + box / 2 + 46);
      ctx.moveTo(cx - box / 2, cy + box / 2 + 40);
      ctx.lineTo(cx - box / 2, cy + box / 2 + 52);
      ctx.moveTo(cx + box / 2, cy + box / 2 + 40);
      ctx.lineTo(cx + box / 2, cy + box / 2 + 52);
      ctx.stroke();
      ctx.fillStyle = "#1A1714";
      ctx.font = '600 15px "DM Mono", ui-monospace, monospace';
      ctx.textAlign = "center";
      ctx.fillText(sizeLabel(n), cx, cy + box / 2 + 72);

      // How far down to the floor, drawn rather than counted.
      var bw = (W - 120) / FLOOR;
      for (var i = 0; i < FLOOR; i++) {
        ctx.fillStyle = i < n ? "#E4572E" : "#E4DACA";
        ctx.fillRect(60 + i * bw + 2, H - 20, bw - 4, 8);
      }
      ctx.fillStyle = "#6B6055";
      ctx.font = '500 12px "DM Mono", ui-monospace, monospace';
      ctx.textAlign = "left";
      ctx.fillText(L_START, 60, H - 28);
      ctx.textAlign = "right";
      ctx.fillText(L_END, W - 60, H - 28);

      if (canvas.setAttribute) { canvas.setAttribute("aria-label", altText()); }
    }

    function repaint() {
      if (outCount) { outCount.textContent = String(n); }
      if (outSize) { outSize.textContent = sizeLabel(n); }
      // Emit-both-show-one: the word is in the document and the state is
      // which one is hidden, so nothing science-bearing is built in JS and
      // the accent on "Floor" is the stylesheet's, not a style attribute.
      each(verdicts, function (v) {
        setHidden(v, v.getAttribute("data-verdict")
                  !== (n >= FLOOR ? "floor" : "open"));
      });
      var want = branch();
      each(notes, function (p) {
        setHidden(p, p.getAttribute("data-note") !== want);
      });
      each(btns, function (b) {
        var end = b.getAttribute("data-dis") === "at_start"
          ? n <= 0 : n >= FLOOR;
        if (end) { b.setAttribute("disabled", ""); }
        else { b.removeAttribute("disabled"); }
      });
      // The head counter reads "floor reached" at the floor, which is a
      // third shape `setCount` does not carry; every other state is its
      // ordinary "{n} of {total}".
      if (n >= FLOOR && FULL && counter) { counter.textContent = FULL; }
      else { setCount(sec, n); }
      draw();
      if (n >= FLOOR) { reached = true; }
      if (reached) { markStage(sec, true); }
    }

    each(btns, function (b) {
      b.addEventListener("click", function () {
        var step = parseInt(b.getAttribute("data-step"), 10) || 0;
        if (b.getAttribute("data-act") === "undo") { step = -step; }
        var next = Math.max(0, Math.min(FLOOR, n + step));
        if (next === n) { return; }
        n = next;
        repaint();
      });
    });

    repaint();
    wireBenchGate(sec);
  }
