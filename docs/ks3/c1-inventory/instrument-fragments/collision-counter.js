// WIRE: each(root.querySelectorAll("[data-counterblock]"), wireCollisionCounter);
//
// Splice point: `wireInstruments()` in shared/ks3.js, in the new
// "C1 · Particles and their behaviour" group. The function below belongs
// beside the other instrument wirings and uses the file's existing helpers:
// `each`, `toArray`, `setHidden`, `setCount`, `markStage`, `motionReduced`
// and `wireBenchGate`.

  /* ═══ C1 · Particles and their behaviour (⊕ MRB-228) ═══════════════
     ── collision-counter (c1-04 #s-bench) ──

     The one instrument in the key stage that COUNTS. Every wall bounce
     pushes a timestamp; entries older than the window are shifted off;
     the number on screen is the length of that array. It is not a
     formula dressed up as a measurement, and that difference is the
     whole reason a student believes "smaller box, same particles, same
     speed — and the count is up".

     ⚖️ THE BUMPS TOGGLE IS PART-08's CONFRONTATION. Grey rings are drawn
     wherever two particles are within `bump_threshold` of each other,
     there are dozens of them, and not one of them touches `hits`. The
     wrong idea is "pressure is the particles pushing each other", and
     this is the instrument that shows those pushes happening and then
     shows them counting for nothing.

     ⚖️ REDUCED MOTION SCALES THE SPEED, IT DOES NOT STOP THE GAS.
     Design's own 0.35 — but asked EVERY FRAME rather than once at
     construction (ruling R4, which corrected exactly this slip on
     b2-03). A stopped gas has a wall-hit count of zero, which is not a
     lesser experience, it is a broken one.

     ⊕ FRAME-RATE INDEPENDENCE, where the page is silent. Design's step
     is a fixed distance PER FRAME, so the same gas reads roughly twice
     the hits per second on a 120 Hz display as on a 60 Hz one — the one
     number the lesson is about would depend on the student's monitor.
     The step is normalised to 60 Hz here, so the motion is identical at
     60 Hz and the count means the same thing everywhere.

     ⚠️ The note branches use literal indices 0 / 1 / 2, exactly as
     Design writes them: index 0 is the coldest, largest and fewest, 1 is
     the middle, 2 is the hottest, smallest and most. The renderer raises
     unless there are exactly three of each, so the indices cannot drift
     out from under this. */

  // Design's own canvas literals (page 512–606). None of these is a KS3
  // token: this is a drawing, and the drawing has its own cream that is
  // one notch warmer than `--ks3-card`, its own near-black that is one
  // notch warmer than `--ks3-ink`, and a particle orange that exists
  // nowhere else in the system.
  var COUNTER_INK = {
    ground: "#FFFDF8",   // the canvas's own paper
    dash: "#E4DACA",     // full-size reference outline, and the bar track
    box: "#F6EEE0",      // the container's fill
    line: "#1A1714",     // the container's outline, and the big number
    particle: "#D98A4A",
    particleEdge: "#5A3212",
    flash: "228,87,46",  // the accent, as rgb components for the fade
    bump: "rgba(120,110,98,0.75)",
    label: "#6B6055",    // 6.0:1 on the canvas ground
    bar: "#E4572E"
  };

  function wireCollisionCounter(sec) {
    var wrap = sec.querySelector("[data-counter]");
    if (!wrap) { return; }
    var cfg;
    try { cfg = JSON.parse(wrap.getAttribute("data-cfg") || "{}"); }
    catch (err) { cfg = {}; }

    var canvas = wrap.querySelector("[data-counter-canvas]");
    var bumpBtn = wrap.querySelector("[data-counter-bumps]");
    var noteEls = toArray(wrap.querySelectorAll("[data-note]"));
    var btns = toArray(wrap.querySelectorAll(".ks3-counter-btn"));
    var total = parseInt(wrap.getAttribute("data-total"), 10) || 3;
    var fullLabel = wrap.getAttribute("data-full-label") || "";

    var TEMPS = cfg.temps || [];
    var VOLS = cfg.vols || [];
    var COUNTS = cfg.counts || [];
    var CL = cfg.canvas_labels || {};
    var ALT = cfg.alt || {};
    var WINDOW = Number(cfg.window_ms) || 1000;
    var FLASH = Number(cfg.flash_ms) || 420;
    var RM = Number(cfg.reduced_motion_scale) || 0.35;
    var STEP = Number(cfg.step_per_frame) || 0.0075;
    var BUMP_T = Number(cfg.bump_threshold) || 0.0022;
    var FULL = Number(cfg.pressure_full) || 170;
    if (!TEMPS.length || !VOLS.length || !COUNTS.length) { return; }

    var start = cfg.start || {};
    var state = {
      temp: Number(start.temp) || 0,
      vol: Number(start.vol) || 0,
      count: Number(start.count) || 0
    };
    var marks = false;
    // ⊕ CORRECTED. Design keeps `touched = Math.max(prev.touched, N)` with
    // N = 1 / 2 / 3, so pressing ONLY the particle-count button sets it to 3,
    // ticks the stage and prints "all controls tried" when one was. The
    // predicate wants a SET: three DISTINCT groups, in any order.
    var tried = {};

    var hits = [];
    var flashes = [];
    var pairs = [];
    var parts = [];
    var last = 0;
    var lastAlt = 0;

    var most = 0;
    each(COUNTS, function (c) { most = Math.max(most, Number(c.n) || 0); });

    function seed() {
      parts = [];
      for (var i = 0; i < most; i++) {
        var a = Math.random() * Math.PI * 2;
        parts.push({
          x: 0.08 + Math.random() * 0.84,
          y: 0.08 + Math.random() * 0.84,
          dx: Math.cos(a),
          dy: Math.sin(a)
        });
      }
    }

    function live() { return Number(COUNTS[state.count].n) || 0; }

    function step(now, dt) {
      // Asked every frame, so an OS setting or the page's Motion control
      // changed mid-lesson takes effect without a reload — and the gas
      // slows rather than stopping, so the count keeps running.
      var scale = motionReduced() ? RM : 1;
      // Design's distance is per FRAME. Normalised to 60 Hz so the count
      // is a property of the gas rather than of the monitor.
      var speed = (Number(TEMPS[state.temp].speed_multiplier) || 0)
        * scale * STEP * dt * 60;
      var n = live();
      pairs = [];
      for (var i = 0; i < n; i++) {
        var p = parts[i];
        p.x += p.dx * speed;
        p.y += p.dy * speed;
        var hit = false;
        if (p.x < 0.02) { p.x = 0.02; p.dx = Math.abs(p.dx); hit = true; }
        if (p.x > 0.98) { p.x = 0.98; p.dx = -Math.abs(p.dx); hit = true; }
        if (p.y < 0.02) { p.y = 0.02; p.dy = Math.abs(p.dy); hit = true; }
        if (p.y > 0.98) { p.y = 0.98; p.dy = -Math.abs(p.dy); hit = true; }
        if (hit) {
          hits.push(now);
          flashes.push({ x: p.x, y: p.y, t: now });
        }
      }
      // ⚖️ The bumps are found, drawn, and never counted. That omission is
      // the teaching; it is not an optimisation and must not become one.
      if (marks) {
        for (var a = 0; a < n; a++) {
          for (var b = a + 1; b < n; b++) {
            var pa = parts[a], pb = parts[b];
            var dx = pa.x - pb.x, dy = pa.y - pb.y;
            if (dx * dx + dy * dy < BUMP_T) {
              pairs.push([(pa.x + pb.x) / 2, (pa.y + pb.y) / 2]);
            }
          }
        }
      }
      // The rolling window IS the measurement: what is left in the array
      // is what happened in the last second, counted, not modelled.
      while (hits.length && now - hits[0] > WINDOW) { hits.shift(); }
      flashes = flashes.filter(function (f) { return now - f.t < FLASH; });
    }

    // The three status lines are a mono table, so the values line up in a
    // column whatever the labels are. Design hard-codes the padding as
    // literal spaces; this measures it instead, from the longest label.
    var pad = 0;
    each(["temperature", "container", "particles"], function (k) {
      pad = Math.max(pad, (CL[k] || "").length);
    });
    function col(label) {
      var s = CL[label] || "";
      while (s.length < pad + 2) { s += " "; }
      return s;
    }

    function draw(now) {
      if (!canvas || !canvas.getContext) { return; }
      var ctx = canvas.getContext("2d");
      var W = 900, H = 340;
      ctx.setTransform(1, 0, 0, 1, 0, 0);
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      ctx.setTransform(2, 0, 0, 2, 0, 0);
      ctx.fillStyle = COUNTER_INK.ground;
      ctx.fillRect(0, 0, W, H);

      var scale = Number(VOLS[state.vol].scale) || 1;
      var maxW = 520, maxH = 236;
      var bw = maxW * scale, bh = maxH * scale;
      var bx = 60 + (maxW - bw) / 2, by = 46 + (maxH - bh) / 2;

      // The full-size box stays drawn as a dashed ghost at every setting,
      // so "smaller" is visible as a comparison rather than as a memory.
      ctx.strokeStyle = COUNTER_INK.dash;
      ctx.setLineDash([6, 6]);
      ctx.lineWidth = 2;
      ctx.strokeRect(60, 46, maxW, maxH);
      ctx.setLineDash([]);

      ctx.fillStyle = COUNTER_INK.box;
      ctx.fillRect(bx, by, bw, bh);
      ctx.strokeStyle = COUNTER_INK.line;
      ctx.lineWidth = 3;
      ctx.strokeRect(bx, by, bw, bh);

      each(flashes, function (f) {
        var age = (now - f.t) / FLASH;
        ctx.beginPath();
        ctx.arc(bx + f.x * bw, by + f.y * bh, 6 + age * 20, 0, Math.PI * 2);
        ctx.strokeStyle = "rgba(" + COUNTER_INK.flash + ","
          + (0.85 * (1 - age)).toFixed(3) + ")";
        ctx.lineWidth = 3;
        ctx.stroke();
      });

      if (marks) {
        each(pairs, function (b) {
          ctx.beginPath();
          ctx.arc(bx + b[0] * bw, by + b[1] * bh, 15, 0, Math.PI * 2);
          ctx.strokeStyle = COUNTER_INK.bump;
          ctx.lineWidth = 2;
          ctx.stroke();
        });
      }

      var n = live();
      var r = 9;
      var i;
      for (i = 0; i < n; i++) {
        var p = parts[i];
        ctx.beginPath();
        ctx.arc(bx + p.x * bw, by + p.y * bh, r, 0, Math.PI * 2);
        ctx.fillStyle = COUNTER_INK.particle;
        ctx.fill();
        ctx.strokeStyle = COUNTER_INK.particleEdge;
        ctx.lineWidth = 1.8;
        ctx.stroke();
      }

      // ⚖️ THE REFERENCE PARTICLE. Fixed radius, bottom left, at EVERY
      // setting — this is the visual proof that "heating makes particles
      // swell" is false, and `#s-think`'s reveal points straight at it.
      // If it ever scales with anything, that section stops being true.
      ctx.beginPath();
      ctx.arc(74, H - 34, r, 0, Math.PI * 2);
      ctx.fillStyle = COUNTER_INK.particle;
      ctx.fill();
      ctx.strokeStyle = COUNTER_INK.particleEdge;
      ctx.lineWidth = 1.8;
      ctx.stroke();
      ctx.fillStyle = COUNTER_INK.label;
      ctx.font = '500 12px "DM Mono", ui-monospace, monospace';
      ctx.textAlign = "left";
      ctx.fillText(CL.reference || "", 92, H - 30);

      // ── the live readout ──
      // ⚑ NOTES flag 6 — a COUNT and a BAR, never a pascal. There is no
      // unit anywhere here, deliberately: p = F/A is a KS4 calculation.
      var count = hits.length;
      var px = 620;
      ctx.fillStyle = COUNTER_INK.label;
      ctx.font = '500 12px "DM Mono", ui-monospace, monospace';
      ctx.fillText(CL.hits || "", px, 66);
      ctx.fillStyle = COUNTER_INK.line;
      ctx.font = '700 58px "Bricolage Grotesque", system-ui, sans-serif';
      ctx.fillText(String(count), px, 122);

      ctx.fillStyle = COUNTER_INK.label;
      ctx.font = '500 12px "DM Mono", ui-monospace, monospace';
      ctx.fillText(CL.pressure || "", px, 158);
      var barW = 220, barH = 22;
      ctx.fillStyle = COUNTER_INK.dash;
      ctx.fillRect(px, 168, barW, barH);
      ctx.fillStyle = COUNTER_INK.bar;
      ctx.fillRect(px, 168, barW * Math.min(1, count / FULL), barH);
      ctx.strokeStyle = COUNTER_INK.line;
      ctx.lineWidth = 2;
      ctx.strokeRect(px, 168, barW, barH);

      ctx.fillStyle = COUNTER_INK.label;
      ctx.font = '500 12px "DM Mono", ui-monospace, monospace';
      ctx.fillText(col("temperature")
        + (TEMPS[state.temp].label || "").toUpperCase(), px, 216);
      ctx.fillText(col("container")
        + (VOLS[state.vol].label || "").toUpperCase(), px, 236);
      ctx.fillText(col("particles") + n, px, 256);
    }

    /* Design's six branches, in Design's order of evaluation. The order is
       load-bearing: `bumps` wins over everything because when the rings
       are on they are the subject, and `smaller_box` is narrower than
       `hot` so it has to be asked first. */
    function noteKey() {
      if (marks) { return "bumps"; }
      if (state.vol > 0 && state.temp === 1) { return "smaller_box"; }
      if (state.temp === 2) { return "hot"; }
      if (state.temp === 0) { return "cold"; }
      if (state.count === 2) { return "more_particles"; }
      return "resting";
    }

    function repaintNote() {
      var key = noteKey();
      each(noteEls, function (el) {
        setHidden(el, el.getAttribute("data-note") !== key);
      });
    }

    function altText(h) {
      return (ALT.template || "")
        .split("{temp}").join((TEMPS[state.temp].label || "").toLowerCase())
        .split("{vol}").join((VOLS[state.vol].label || "").toLowerCase())
        .split("{n}").join(String(live()))
        .split("{hits}").join(String(h));
    }

    function setAlt() {
      if (canvas) { canvas.setAttribute("aria-label", altText(hits.length)); }
    }

    /* The head counter. `setCount` owns the element for every value the
       format string can express; Design writes a different SENTENCE at
       the top ("all controls tried", page 691) and `_head_counter` has a
       `zero` hook but no `full` one, so the terminal label is written
       here — on the same element, from the same authored payload. */
    function progress() {
      var n = 0, k;
      for (k in tried) { if (tried[k]) { n += 1; } }
      if (n >= total && fullLabel) {
        var el = sec.querySelector("[data-count]");
        if (el) { el.textContent = fullLabel; }
      } else {
        setCount(sec, n);
      }
      if (n >= total) { markStage(sec, true); }
    }

    each(btns, function (b) {
      b.addEventListener("click", function () {
        var group = b.getAttribute("data-group");
        var i = parseInt(b.getAttribute("data-i"), 10) || 0;
        if (!(group in state)) { return; }
        state[group] = i;
        each(btns, function (x) {
          if (x.getAttribute("data-group") === group) {
            x.setAttribute("aria-pressed", x === b ? "true" : "false");
          }
        });
        tried[group] = true;
        progress();
        repaintNote();
        setAlt();
      });
    });

    if (bumpBtn) {
      var showLabel = bumpBtn.querySelector("[data-bump-show]");
      var hideLabel = bumpBtn.querySelector("[data-bump-hide]");
      bumpBtn.addEventListener("click", function () {
        marks = !marks;
        bumpBtn.setAttribute("aria-pressed", marks ? "true" : "false");
        setHidden(showLabel, marks);
        setHidden(hideLabel, !marks);
        if (!marks) { pairs = []; }
        // ⚠️ NOT one of the three controls. The head says "3 controls" and
        // means the three that change the GAS; this one changes what is
        // drawn on top of it. Design does not count it either.
        repaintNote();
      });
    }

    function tick(now) {
      var dt = Math.min(0.05, (now - (last || now)) / 1000);
      last = now;
      step(now, dt);
      draw(now);
      // The label is state-bound, but the state includes a number that
      // moves every frame. Rewritten once a second — often enough that a
      // screen reader arriving at the canvas gets a current reading,
      // rarely enough that it is not sixty attribute writes a second.
      if (now - lastAlt > 1000) { lastAlt = now; setAlt(); }
      window.requestAnimationFrame(tick);
    }

    seed();
    repaintNote();
    setAlt();
    setCount(sec, 0);
    draw(0);
    if (window.requestAnimationFrame) { window.requestAnimationFrame(tick); }
    wireBenchGate(sec);
  }
