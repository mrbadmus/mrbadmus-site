// WIRE: each(root.querySelectorAll("[data-walkblock]"), wireRandomWalk);
//
// Goes in `wireInstruments()` in shared/ks3.js, in a new "⊕ C1 · Particles and
// their behaviour" group. Uses `each`, `toArray`, `setHidden`, `markStage`,
// `setCount`, `motionReduced` and `wireBenchGate`, all already in scope.

  /* ── random-walk-bench (c1-05 #s-walk) ──
     130 particles released on the left of a sealed tank, each taking a step
     in a random direction, over and over. Nothing else happens, and that is
     the argument.

     ⚖️ **THE TWO CROSSING COUNTERS ARE CLEARED BY "PUT THE DROP BACK" AND BY
     NOTHING ELSE.** Not when the tank evens out, not when the note changes,
     not when the run is paused. `PART-11` is the belief that particles move
     *in order to* spread out, and the only thing that dislodges it is watching
     both counters keep climbing — together, at the same rate — after the
     readout has already said "Spread out? Yes". The spreading finishes; the
     moving does not. `#s-think`'s reveal then argues from these two numbers in
     words, so zeroing them would leave that paragraph describing something the
     student cannot see.

     ⚖️ THE COUNTER CADENCE IS A DECISION, NOT AN ACCIDENT. Design's counters
     reach the DOM through `setState`, which `step()` calls at most every 20
     frames and usually every 40 — so they move in visible jumps roughly twice
     a second, and the interval is frame-COUNT based, which means a 120 Hz
     laptop reads the same page twice as fast. Two things are wanted at once:
     the numbers must be legible (a per-frame counter at 60–120 Hz is a blur,
     and comparing left-to-right against right-to-left is the entire point of
     having two of them), and they must visibly CLIMB (a counter that looks
     parked reads as movement having stopped, which is the misconception).
     So: a WALL-CLOCK cadence of `even.hz` = 3 per second, which is Design's
     own sampling rate (every 20 frames at 60 fps), applied to the repaint as
     well as the sample. Same feel on every display, three legible steps a
     second, and the irregular 20-or-40 flicker gone.

     ⚖️ REDUCED MOTION SCALES THE WALK, IT DOES NOT STOP IT (R4/R6), and it is
     asked EVERY TICK rather than once at construction — Design reads it in
     `componentDidMount` and never again, so an OS setting changed mid-lesson
     does nothing. At 0.4× the tank still evens out and both counters still
     climb; the student gets the whole experiment, more slowly.

     The walk itself is time-stepped at a fixed 60 steps a second rather than
     one step per frame, so the same dye takes the same time to spread on a
     90 Hz phone as on a 60 Hz monitor. Design's step lengths are unchanged;
     only what "a step" is timed against has moved off the refresh rate. */

  var WALK_RATE = 60;        // steps per second, fixed
  var WALK_CATCHUP = 6;      // most steps one frame may make up after a stall

  function wireRandomWalk(sec) {
    var wrap = sec.querySelector("[data-walk]");
    if (!wrap) { return; }
    var cfg;
    try { cfg = JSON.parse(wrap.getAttribute("data-cfg") || "{}"); }
    catch (err) { cfg = null; }
    if (!cfg || !cfg.particles) { return; }

    var canvas = wrap.querySelector("[data-walk-canvas]");
    var outR = wrap.querySelector("[data-walk-cross-right]");
    var outL = wrap.querySelector("[data-walk-cross-left]");
    var outEven = wrap.querySelector("[data-walk-even]");
    var evenYes = wrap.querySelector("[data-walk-even-yes]");
    var evenNo = wrap.querySelector("[data-walk-even-no]");
    var runBtn = wrap.querySelector("[data-walk-run]");
    var resetBtn = wrap.querySelector("[data-walk-reset]");
    var traceBtn = wrap.querySelector("[data-walk-trace]");
    var warmBtn = wrap.querySelector("[data-walk-warm]");
    var noteWrap = wrap.querySelector("[data-walk-note]");

    var N = cfg.particles;
    var SEED = cfg.seed, STEP = cfg.step, BOUND = cfg.bounds;
    var TOL = cfg.even.tolerance, HZ = cfg.even.hz || 3;
    var TRAIL = cfg.trail_max, BINS = cfg.bins, SLOW = cfg.reduced_scale;
    var CL = cfg.canvas_labels, ALT = cfg.alt, PHASE = cfg.progress;

    var parts = [];
    // ⚖️ The two numbers the lesson is about. Written by `walk()`, zeroed by
    // `reset()`, and touched nowhere else in this function.
    var crossR = 0, crossL = 0;
    var running = false, everRan = false, trace = false, warm = false;
    var even = false;
    // Has the tank EVER evened out. The rail reads this rather than `even`:
    // Design ticks stage 2 on the live flag, so pressing "Put the drop back"
    // un-ticks a stop the student already reached. Same defect as c1-06's
    // stage 4, and the same fix — a stop records what was reached, not what
    // is on screen now.
    var everEven = false;
    var left = N, right = 0;
    var acc = 0, last = 0, sampleAt = 0;

    function reset() {
      parts = [];
      for (var i = 0; i < N; i++) {
        parts.push({
          x: SEED.x[0] + Math.random() * (SEED.x[1] - SEED.x[0]),
          y: SEED.y[0] + Math.random() * (SEED.y[1] - SEED.y[0]),
          side: 0,
          trail: []
        });
      }
      crossR = 0;
      crossL = 0;
      left = N;
      right = 0;
    }

    /* One step for every particle: a random direction, a fixed length, and a
       reflecting wall that puts a particle back by exactly what it overshot,
       so the step length is conserved rather than clipped. */
    function walk(len) {
      for (var i = 0; i < parts.length; i++) {
        var p = parts[i];
        var ang = Math.random() * Math.PI * 2;
        p.x += Math.cos(ang) * len;
        p.y += Math.sin(ang) * len * STEP.y_scale;
        if (p.x < BOUND.x[0]) { p.x = BOUND.x[0] + (BOUND.x[0] - p.x); }
        if (p.x > BOUND.x[1]) { p.x = BOUND.x[1] - (p.x - BOUND.x[1]); }
        if (p.y < BOUND.y[0]) { p.y = BOUND.y[0] + (BOUND.y[0] - p.y); }
        if (p.y > BOUND.y[1]) { p.y = BOUND.y[1] - (p.y - BOUND.y[1]); }
        var side = p.x > 0.5 ? 1 : 0;
        if (side !== p.side) {
          if (side === 1) { crossR += 1; } else { crossL += 1; }
          p.side = side;
        }
        if (trace && i === 0) {
          p.trail.push([p.x, p.y]);
          if (p.trail.length > TRAIL) { p.trail.shift(); }
        }
      }
    }

    /* Evenness is a TOLERANCE, not an equality — within 9% of half the
       particles on each side. Exact halves would essentially never occur and
       the readout would never say Yes. */
    function sample() {
      right = 0;
      for (var i = 0; i < parts.length; i++) {
        if (parts[i].x > 0.5) { right += 1; }
      }
      left = parts.length - right;
      even = Math.abs(right - parts.length / 2) < parts.length * TOL;
      if (even && !everEven) {
        everEven = true;
        markStage(sec, true);
      }
    }

    function counts() {
      if (outR) { outR.textContent = String(crossR); }
      if (outL) { outL.textContent = String(crossL); }
    }

    function label(btn, attr, key) {
      if (!btn) { return; }
      each(btn.querySelectorAll("[data-" + attr + "]"), function (s) {
        setHidden(s, s.getAttribute("data-" + attr) !== key);
      });
    }

    function altText() {
      return (ALT.template || "")
        .split("{state}").join(even ? ALT.even : ALT.uneven)
        .split("{left}").join(String(left))
        .split("{right}").join(String(right));
    }

    /* Which of the four authored notes is showing. Design's own order, and
       tracing outranks evening out: a student who has asked to follow one
       particle is being answered about that particle. */
    function noteKey() {
      if (!everRan) { return "idle"; }
      if (trace) { return "tracing"; }
      if (even) { return "even"; }
      return "spreading";
    }

    function paint() {
      if (runBtn) {
        runBtn.setAttribute("aria-pressed", running ? "true" : "false");
        label(runBtn, "run-label",
              running ? "pause" : (everRan ? "continue" : "start"));
      }
      if (traceBtn) {
        traceBtn.setAttribute("aria-pressed", trace ? "true" : "false");
        label(traceBtn, "trace-label", trace ? "off" : "on");
      }
      if (warmBtn) {
        warmBtn.setAttribute("aria-pressed", warm ? "true" : "false");
        label(warmBtn, "warm-label", warm ? "off" : "on");
      }
      if (outEven) { outEven.setAttribute("data-walk-even", even ? "1" : "0"); }
      setHidden(evenYes, !even);
      setHidden(evenNo, even);
      if (noteWrap) {
        var key = noteKey();
        each(noteWrap.querySelectorAll("[data-note]"), function (p) {
          setHidden(p, p.getAttribute("data-note") !== key);
        });
      }
      // The block head's readout. `{phase}` is a live WORD rather than a
      // count, which is what `extra` is for; the count slot stays at zero.
      setCount(sec, 0, {
        phase: even ? PHASE.even : (everRan ? PHASE.spreading : PHASE.idle)
      });
      if (canvas && canvas.setAttribute) {
        canvas.setAttribute("aria-label", altText());
      }
    }

    function draw() {
      if (!canvas || !canvas.getContext || !parts.length) { return; }
      var ctx = canvas.getContext("2d");
      var W = 900, H = 320;
      ctx.setTransform(2, 0, 0, 2, 0, 0);
      // The opaque fill IS the clear — there is no `clearRect` here and none
      // is wanted; every pixel is repainted.
      ctx.fillStyle = "#FFFDF8";
      ctx.fillRect(0, 0, W, H);

      var bx = 56, by = 44, bw = W - 112, bh = H - 118;
      ctx.fillStyle = "#F3F6F5";
      ctx.fillRect(bx, by, bw, bh);

      // The dividing line the two counters count across. Dashed, because it
      // is a place to measure and not a wall.
      ctx.strokeStyle = "#B9AE9C";
      ctx.setLineDash([7, 6]);
      ctx.lineWidth = 2;
      ctx.beginPath();
      ctx.moveTo(bx + bw / 2, by);
      ctx.lineTo(bx + bw / 2, by + bh);
      ctx.stroke();
      ctx.setLineDash([]);

      if (trace && parts[0].trail.length > 1) {
        ctx.strokeStyle = "rgba(26,23,20,0.55)";
        ctx.lineWidth = 1.4;
        ctx.beginPath();
        for (var k = 0; k < parts[0].trail.length; k++) {
          var pt = parts[0].trail[k];
          var tx = bx + pt[0] * bw, ty = by + pt[1] * bh;
          if (k) { ctx.lineTo(tx, ty); } else { ctx.moveTo(tx, ty); }
        }
        ctx.stroke();
      }

      for (var i = 0; i < parts.length; i++) {
        var p = parts[i];
        var traced = trace && i === 0;
        ctx.beginPath();
        ctx.arc(bx + p.x * bw, by + p.y * bh, traced ? 8 : 5.5, 0, Math.PI * 2);
        ctx.fillStyle = traced ? "#1A1714" : "#8E44AD";
        ctx.fill();
        if (traced) {
          ctx.strokeStyle = "#E4572E";
          ctx.lineWidth = 3;
          ctx.stroke();
        }
      }

      ctx.strokeStyle = "#1A1714";
      ctx.lineWidth = 3;
      ctx.strokeRect(bx, by, bw, bh);

      // Readout one, drawn: how many are on each side, right now. These two
      // numbers are what "spread out" means, and they are the ones the
      // canvas `aria-label` carries for anyone who cannot see them.
      var nRight = 0;
      for (var j = 0; j < parts.length; j++) {
        if (parts[j].x > 0.5) { nRight += 1; }
      }
      var nLeft = parts.length - nRight;
      ctx.fillStyle = "#6B6055";
      ctx.font = '500 13px "DM Mono", ui-monospace, monospace';
      ctx.textAlign = "center";
      ctx.fillText(CL.left_half + nLeft, bx + bw * 0.25, by - 14);
      ctx.fillText(CL.right_half + nRight, bx + bw * 0.75, by - 14);

      // Readout two, drawn: the concentration profile along the tank. It is
      // the shape that flattens, and watching it flatten is what makes
      // "crowded to less crowded" a thing a student has seen rather than a
      // phrase they have been given.
      var counts18 = [], b;
      for (b = 0; b < BINS; b++) { counts18.push(0); }
      for (b = 0; b < parts.length; b++) {
        var idx = Math.floor(parts[b].x * BINS);
        if (idx < 0) { idx = 0; }
        if (idx > BINS - 1) { idx = BINS - 1; }
        counts18[idx] += 1;
      }
      var maxc = 1;
      for (b = 0; b < BINS; b++) {
        if (counts18[b] > maxc) { maxc = counts18[b]; }
      }
      var py0 = by + bh + 20, ph = 44;
      for (b = 0; b < BINS; b++) {
        var h = (counts18[b] / maxc) * ph;
        ctx.fillStyle = "#8E44AD";
        ctx.fillRect(bx + (b * bw) / BINS + 2, py0 + ph - h, bw / BINS - 4, h);
      }
      ctx.strokeStyle = "#D9CDBA";
      ctx.lineWidth = 2;
      ctx.beginPath();
      ctx.moveTo(bx, py0 + ph);
      ctx.lineTo(bx + bw, py0 + ph);
      ctx.stroke();
      ctx.fillStyle = "#6B6055";
      ctx.font = '500 11px "DM Mono", ui-monospace, monospace';
      ctx.textAlign = "left";
      ctx.fillText(CL.profile, bx, py0 + ph + 18);
    }

    function tick(now) {
      window.requestAnimationFrame(tick);
      var dt = last ? Math.min(0.1, (now - last) / 1000) : 0;
      last = now;
      if (running) {
        // Asked EVERY tick, not once at construction, and it scales the step
        // rather than stopping the run.
        var len = (warm ? STEP.warm : STEP.cool) * (motionReduced() ? SLOW : 1);
        acc += dt;
        var budget = WALK_CATCHUP;
        while (acc >= 1 / WALK_RATE && budget > 0) {
          walk(len);
          acc -= 1 / WALK_RATE;
          budget -= 1;
        }
        // A backgrounded tab banks minutes of `dt`; drop it rather than
        // sprinting through it when the student comes back.
        if (acc > 0.5) { acc = 0; }
        if (now >= sampleAt) {
          sampleAt = now + 1000 / HZ;
          sample();
          counts();
          paint();
        }
      }
      // Nothing is drawn while the commit gate still holds the bench closed.
      if (!wrap.hasAttribute("hidden")) { draw(); }
    }

    if (runBtn) {
      runBtn.addEventListener("click", function () {
        running = !running;
        // `everRan` latches on the first press, including the press that
        // pauses — the button then reads "Continue", never "Start the run".
        everRan = true;
        last = 0;
        paint();
      });
    }
    if (resetBtn) {
      resetBtn.addEventListener("click", function () {
        // ⚖️ The ONLY thing in this instrument that zeroes the counters.
        reset();
        running = false;
        even = false;
        acc = 0;
        counts();
        paint();
        if (!wrap.hasAttribute("hidden")) { draw(); }
      });
    }
    if (traceBtn) {
      traceBtn.addEventListener("click", function () {
        // The trail starts empty each time it is asked for, so what is drawn
        // is the path since the question was asked.
        if (parts[0]) { parts[0].trail = []; }
        trace = !trace;
        paint();
      });
    }
    if (warmBtn) {
      warmBtn.addEventListener("click", function () {
        warm = !warm;
        paint();
      });
    }

    reset();
    counts();
    paint();
    if (window.requestAnimationFrame) { window.requestAnimationFrame(tick); }
    wireBenchGate(sec);
  }
