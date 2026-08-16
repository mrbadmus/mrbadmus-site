// WIRE: each(root.querySelectorAll("[data-sbenchblock]"), wireStateBench);
//
// ⚠️ Wire the BENCH BEFORE the matrix in `wireInstruments()` — same reason the
// sabotage engine goes before the cell bench and the builder after it. The
// matrix reads the bench's published attributes and listens for its broadcast;
// it also does one standing read of its own at wire time, so the order is a
// tidiness rather than a correctness dependency.

  /* ═══ C1 · Particles and their behaviour (⊕ MRB-228) ═══════════════
     state-bench (c1-02 #s-bench) — one substance, three arrangements.

     ⚖️ THE FIXED-SIZE REFERENCE PARTICLE IS DRAWN IN EVERY STATE AND IN
     EVERY SETTING, unconditionally, and there is no branch below that
     can skip it. NOTES §3 flag 3 makes it non-negotiable: it is the
     drawn form of the one sentence the lesson exists to defend, and a
     bench that drops it for room is a bench that has lost its argument.

     ⚖️ REDUCED MOTION SCALES THE RATE, IT DOES NOT STOP THE CLOCK.
     Design reads `prefers-reduced-motion` once in `componentDidMount`
     and then kills `moving` outright, which on THIS lesson deletes the
     content: the difference between vibrating and travelling is the
     thing the student is being asked to look at, and its own resting
     note says "switch the motion off and on and watch the difference".
     R6 says reduced motion is a complete experience and never a lesser
     one, and the build contract says to scale rather than stop. So the
     rate drops to a third and the mechanism still runs. The student's
     OWN "Freeze the motion" is absolute — that is a choice, not a
     safety setting — and so is the site's Motion control. Asked every
     frame, so an OS setting changed mid-lesson needs no reload. */

  // Design's own constants, kept per-FRAME and converted at the call site, so
  // every number below can still be read against page lines 511–590.
  var SB_FPS = 60;                     // the frame rate Design's numbers assume
  var SB_RM_RATE = 0.35;               // reduced motion: a third speed, not zero

  function sbRate(motion) {
    if (!motion) { return 0; }
    // The site's own Motion control is an explicit request and wins outright.
    if (document.documentElement.getAttribute("data-motion") === "off") {
      return 0;
    }
    // `B2_RM` is the one `prefers-reduced-motion` media query in this file;
    // referenced rather than re-created so there is a single copy of it.
    return (B2_RM && B2_RM.matches) ? SB_RM_RATE : 1;
  }

  function wireStateBench(sec) {
    var wrap = sec.querySelector("[data-sbench]");
    if (!wrap) { return; }
    var states;
    try { states = JSON.parse(wrap.getAttribute("data-states") || "[]"); }
    catch (err) { states = []; }
    if (!states.length) { return; }

    var body = wrap.querySelector(".ks3-sbench-body");
    var canvas = wrap.querySelector("[data-sbench-canvas]");
    var notes = toArray(wrap.querySelectorAll("[data-note]"));
    var gate = sec.querySelector("[data-benchgate]");
    var FULL = wrap.getAttribute("data-full") || "";
    var BANNER_GAS = wrap.getAttribute("data-banner-gas") || "";
    var BANNER_OTHER = wrap.getAttribute("data-banner-other") || "";
    var REFERENCE = wrap.getAttribute("data-reference") || "";

    var idx = 0;
    var motion = true, trails = false, squash = false;
    var seen = {};
    var phase = 0, last = 0, dirty = true, raf = null;

    // 48 particles, seeded once. The solid uses the first 40 as a 10 × 4
    // lattice, the liquid the first 40 loose, the gas the first 22.
    var parts = [];
    for (var i = 0; i < 48; i++) {
      parts.push({ x: Math.random(), y: Math.random(),
                   vx: (Math.random() - 0.5), vy: (Math.random() - 0.5),
                   ph: Math.random() * 6.28, trail: [] });
    }

    function clearTrails() {
      // ⊕ Design keeps every particle's trail across a state change and across
      // a squash, so switching gas → liquid with the paths on draws the GAS's
      // long straight runs inside the liquid for the next 26 frames, and
      // squashing a gas leaves a path crossing the piston it has just moved.
      // Both are pictures of something that did not happen. The history is
      // dropped whenever the thing it is a history OF changes.
      for (var k = 0; k < parts.length; k++) { parts[k].trail.length = 0; }
    }

    // ── the drawing ──────────────────────────────────────────────────
    // Design space 900 × 310, backing store 1800 × 620, setTransform(2,…).
    // No clearRect: the opaque ground fill covers the frame.

    function drawP(ctx, x, y) {
      ctx.beginPath();
      ctx.arc(x, y, 13, 0, Math.PI * 2);
      ctx.fillStyle = "#D98A4A";
      ctx.fill();
      ctx.strokeStyle = "#5A3212";
      ctx.lineWidth = 2;
      ctx.stroke();
      ctx.beginPath();
      ctx.arc(x - 4, y - 5, 4, 0, Math.PI * 2);
      ctx.fillStyle = "rgba(255,255,255,0.62)";
      ctx.fill();
    }

    function draw() {
      if (!canvas || !canvas.getContext) { return; }
      var ctx = canvas.getContext("2d");
      var W = 900, H = 310;
      var st = states[idx] || states[0];
      var key = st.key;
      var moving = sbRate(motion) > 0;

      ctx.setTransform(1, 0, 0, 1, 0, 0);
      ctx.setTransform(2, 0, 0, 2, 0, 0);
      ctx.fillStyle = "#FFFDF8";
      ctx.fillRect(0, 0, W, H);

      var boxX = 70, boxW = W - 140;
      // A gas gives way and a solid or liquid barely moves: 92px against 8px.
      // That ratio IS the answer to "try to squash it", drawn.
      var lidDrop = squash ? (key === "gas" ? 92 : 8) : 0;
      var boxY = 42 + lidDrop, boxH = H - 110 - lidDrop;

      ctx.fillStyle = "#F6EEE0";
      ctx.fillRect(boxX, boxY, boxW, boxH);
      ctx.strokeStyle = "#1A1714";
      ctx.lineWidth = 3;
      ctx.beginPath();
      ctx.moveTo(boxX, boxY - 6);
      ctx.lineTo(boxX, boxY + boxH);
      ctx.lineTo(boxX + boxW, boxY + boxH);
      ctx.lineTo(boxX + boxW, boxY - 6);
      ctx.stroke();

      if (squash) {
        ctx.fillStyle = "#E4572E";
        ctx.fillRect(boxX - 6, boxY - 16, boxW + 12, 12);
        ctx.fillStyle = "#A93411";
        ctx.font = '500 13px "DM Mono", ui-monospace, monospace';
        ctx.textAlign = "center";
        ctx.fillText(key === "gas" ? BANNER_GAS : BANNER_OTHER,
                     W / 2, boxY - 24);
      }

      var p, x, y, n, j;
      if (key === "solid") {
        var cols = 10, rows = 4;
        var gx = boxW / (cols + 1);
        var gy = Math.min(46, boxH / (rows + 1));
        var y0 = boxY + boxH - rows * gy - 12;
        for (var row = 0; row < rows; row++) {
          for (var col = 0; col < cols; col++) {
            p = parts[row * cols + col];
            var bx = boxX + gx * (col + 1);
            var by = y0 + gy * (row + 1);
            j = moving ? 4.5 : 0;
            x = bx + Math.sin(phase * 2.4 + p.ph) * j;
            y = by + Math.cos(phase * 2.1 + p.ph * 1.7) * j;
            if (trails) {
              // A home position, drawn as a ring. The trail of a solid is a
              // circle the size of the wobble — that is the whole point, and
              // it is why it is drawn as a ring rather than a path.
              ctx.strokeStyle = "rgba(228,87,46,0.5)";
              ctx.lineWidth = 1.5;
              ctx.beginPath();
              ctx.arc(bx, by, 5.5, 0, Math.PI * 2);
              ctx.stroke();
            }
            drawP(ctx, x, y);
          }
        }
      } else if (key === "liquid") {
        var surface = boxY + boxH * 0.42;
        for (n = 0; n < 40; n++) {
          p = parts[n];
          x = boxX + 22 + p.x * (boxW - 44);
          y = surface + 14 + p.y * (boxY + boxH - surface - 40);
          if (trails) {
            p.trail.push([x, y]);
            if (p.trail.length > 26) { p.trail.shift(); }
            ctx.strokeStyle = "rgba(228,87,46,0.35)";
            ctx.lineWidth = 1.8;
            ctx.beginPath();
            for (var q = 0; q < p.trail.length; q++) {
              if (q) { ctx.lineTo(p.trail[q][0], p.trail[q][1]); }
              else { ctx.moveTo(p.trail[q][0], p.trail[q][1]); }
            }
            ctx.stroke();
          }
          drawP(ctx, x, y);
        }
        ctx.strokeStyle = "#8A7355";
        ctx.setLineDash([6, 5]);
        ctx.lineWidth = 2;
        ctx.beginPath();
        ctx.moveTo(boxX, surface);
        ctx.lineTo(boxX + boxW, surface);
        ctx.stroke();
        ctx.setLineDash([]);
      } else {
        for (n = 0; n < 22; n++) {
          p = parts[n];
          x = boxX + 20 + p.x * (boxW - 40);
          y = boxY + 20 + p.y * (boxH - 40);
          if (trails) {
            p.trail.push([x, y]);
            if (p.trail.length > 34) { p.trail.shift(); }
            ctx.strokeStyle = "rgba(228,87,46,0.32)";
            ctx.lineWidth = 1.8;
            ctx.beginPath();
            for (var g = 0; g < p.trail.length; g++) {
              if (g) { ctx.lineTo(p.trail[g][0], p.trail[g][1]); }
              else { ctx.moveTo(p.trail[g][0], p.trail[g][1]); }
            }
            ctx.stroke();
          }
          drawP(ctx, x, y);
        }
      }

      // ⚖️ THE FIXED-SIZE REFERENCE PARTICLE. Unconditional, outside every
      // branch above, at the same radius the box uses. NOTES §3 flag 3.
      ctx.fillStyle = "#6B6055";
      ctx.font = '500 12px "DM Mono", ui-monospace, monospace';
      ctx.textAlign = "left";
      ctx.fillText(REFERENCE, boxX + 34, H - 30);
      drawP(ctx, boxX + 14, H - 34);

      ctx.textAlign = "right";
      ctx.fillStyle = "#A93411";
      ctx.font = '500 14px "DM Mono", ui-monospace, monospace';
      ctx.fillText((st.label || "").toUpperCase(), boxX + boxW, 30);
    }

    // ── the clock ────────────────────────────────────────────────────
    // ⊕ TIME-BASED, not frame-count-based. Design advances `this.tick += 1`
    // per frame, so its bench runs at double speed on a 120 Hz screen and at a
    // crawl on a loaded Chromebook. `dtf` is "how many of Design's frames has
    // this frame been worth", so every constant below is still Design's own
    // per-frame number and the motion is the same speed everywhere.
    function advance(dtf) {
      var key = (states[idx] || states[0]).key;
      var p, n;
      phase += 0.05 * dtf;
      if (key === "liquid") {
        for (n = 0; n < 40; n++) {
          p = parts[n];
          p.x += p.vx * 0.0016 * dtf;
          p.y += p.vy * 0.0009 * dtf;
          if (p.x < 0.03 || p.x > 0.97) { p.vx *= -1; }
          if (p.y < 0.02 || p.y > 0.98) { p.vy *= -1; }
        }
      } else if (key === "gas") {
        for (n = 0; n < 22; n++) {
          p = parts[n];
          p.x += p.vx * 0.006 * dtf;
          p.y += p.vy * 0.006 * dtf;
          if (p.x < 0.02) { p.x = 0.02; p.vx *= -1; }
          if (p.x > 0.98) { p.x = 0.98; p.vx *= -1; }
          if (p.y < 0.02) { p.y = 0.02; p.vy *= -1; }
          if (p.y > 0.98) { p.y = 0.98; p.vy *= -1; }
        }
      }
    }

    function loop(now) {
      raf = window.requestAnimationFrame(loop);
      var r = sbRate(motion);
      var dtf = 0;
      if (r > 0 && last) {
        // Clamped, so a backgrounded tab returning does not teleport the
        // particles across the box in one step.
        dtf = Math.min(0.05, (now - last) / 1000) * SB_FPS * r;
      }
      last = now;
      // A hidden bench is a bench nobody is looking at: behind its gate, off
      // screen, or in a background tab. Costing a Chromebook a repaint for it
      // buys nothing.
      if (body.hasAttribute("hidden") || document.hidden) { return; }
      if (dtf > 0) { advance(dtf); dirty = true; }
      if (!dirty) { return; }
      dirty = false;
      draw();
    }

    // ── the note, the counter and the stage ──────────────────────────
    function show(id) {
      each(notes, function (el) {
        setHidden(el, el.getAttribute("data-note") !== id);
      });
    }

    function repaint() {
      var st = states[idx] || states[0];
      var key = st.key;

      // Design's rule, in Design's order (page line 723 shares it with the
      // matrix): squash first, then paths, then the resting note.
      if (squash) { show("squash:" + (key === "gas" ? "gas" : "other")); }
      else if (trails) { show("trails:" + key); }
      else { show("rest:" + key); }

      if (canvas) { canvas.setAttribute("aria-label", st.alt || ""); }

      // The single source of truth for the bench's settings. `state-matrix`
      // reads these; nothing anywhere keeps a second copy.
      wrap.setAttribute("data-state", key);
      wrap.setAttribute("data-motion", motion ? "1" : "0");
      wrap.setAttribute("data-trails", trails ? "1" : "0");
      wrap.setAttribute("data-squash", squash ? "1" : "0");
      // The broadcast carries NO state — it is only "look again". Anything
      // that put the values in the event would be a second copy of them.
      document.dispatchEvent(new CustomEvent("ks3:statebench"));

      var n = 0, k;
      for (k in seen) { if (seen[k]) { n += 1; } }
      var count = sec.querySelector("[data-count]");
      if (FULL && count && n >= states.length) { count.textContent = FULL; }
      else { setCount(sec, n); }
      markStage(sec, n >= states.length);

      dirty = true;
    }

    // ── controls ─────────────────────────────────────────────────────
    each(toArray(wrap.querySelectorAll("[data-sbench-state]")), function (b) {
      b.addEventListener("click", function () {
        var key = b.getAttribute("data-sbench-state");
        var next = -1;
        for (var m = 0; m < states.length; m++) {
          if (states[m].key === key) { next = m; }
        }
        if (next < 0) { return; }
        idx = next;
        // Design's own rule (line 707): choosing a state releases the piston.
        // A student who squashed a gas and then asked for a liquid is asking
        // to see a liquid, not a liquid under a piston they cannot see.
        squash = false;
        seen[key] = true;
        clearTrails();
        each(toArray(wrap.querySelectorAll("[data-sbench-state]")),
             function (o) {
               o.setAttribute("aria-pressed",
                 o.getAttribute("data-sbench-state") === key ? "true" : "false");
             });
        var sq = wrap.querySelector("[data-sbench-squash]");
        if (sq) { sq.setAttribute("aria-pressed", "false"); }
        repaint();
      });
    });

    function label(btn, on) {
      each(toArray(btn.querySelectorAll("[data-lbl]")), function (s) {
        setHidden(s, s.getAttribute("data-lbl") !== (on ? "on" : "off"));
      });
      btn.setAttribute("aria-pressed", on ? "true" : "false");
    }

    var mBtn = wrap.querySelector("[data-sbench-motion]");
    if (mBtn) {
      mBtn.addEventListener("click", function () {
        motion = !motion;
        // ⊕ `aria-pressed` follows the TINT: pressed means FROZEN, which is
        // what the lit button means and what Design's own paths toggle does.
        // Design announces the opposite (line 709) — see the renderer.
        label(mBtn, !motion);
        // Freezing must land even when nothing else is moving.
        last = 0;
        repaint();
      });
    }
    var tBtn = wrap.querySelector("[data-sbench-trails]");
    if (tBtn) {
      tBtn.addEventListener("click", function () {
        trails = !trails;
        if (!trails) { clearTrails(); }
        label(tBtn, trails);
        repaint();
      });
    }
    var sBtn = wrap.querySelector("[data-sbench-squash]");
    if (sBtn) {
      sBtn.addEventListener("click", function () {
        squash = !squash;
        clearTrails();
        sBtn.setAttribute("aria-pressed", squash ? "true" : "false");
        repaint();
      });
    }

    // ── the gate ─────────────────────────────────────────────────────
    // The same DOM contract as `wireBenchGate` — the gate goes, the body
    // arrives — reimplemented here for one reason: `wireBenchGate` also sets
    // `role="status"` on `[data-benchbody]`, and on this bench that wraps the
    // canvas, six controls and the note in one live region, so every toggle
    // would re-announce the whole instrument. The note has its own tight
    // `role="status"` and announces exactly the sentence that changed.
    if (gate) {
      each(toArray(gate.querySelectorAll(".ks3-option")), function (btn) {
        btn.addEventListener("click", function () {
          each(toArray(gate.querySelectorAll(".ks3-option")), function (o) {
            o.setAttribute("aria-pressed", "false");
          });
          btn.setAttribute("aria-pressed", "true");
          setHidden(gate, true);
          setHidden(body, false);
          // The gate IS the first state observation — the bench opens on the
          // state it opens on, and answering the gate is the moment a student
          // first sees it. This is what moves the counter 0 → 1; it opens at
          // 0 rather than at Design's 1, which counted a state nobody had
          // been shown yet (map §2.5.1).
          seen[states[0].key] = true;
          last = 0;
          repaint();
        });
      });
    } else {
      // No gate authored: the bench is open from the start, so the state it
      // opens on has been seen.
      seen[states[0].key] = true;
    }

    // Nothing has been seen until the gate is answered, so the counter opens
    // at 0 and the stage opens unticked (MRB-208).
    repaint();
    if (window.requestAnimationFrame) { raf = window.requestAnimationFrame(loop); }
  }
