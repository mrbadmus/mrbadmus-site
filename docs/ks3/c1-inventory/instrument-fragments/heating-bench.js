/* WIRE: each(root.querySelectorAll("[data-hbblock]"), wireHeatingBench);   // inside wireInstruments()

   Splice into shared/ks3.js beside the other C1 instruments. It calls
   `wireBenchGate(sec)` itself, exactly as `wireBalanceBench` does, so the
   commit gate needs no separate registration. */

  /* ── heating-bench (c1-03 #s-curve) ──
     Scrub through a run at constant power and watch the temperature stop
     twice while the state changes.

     ⚖️ THE MASS TILE IS NOT WIRED, AND THAT IS THE LESSON. There is no
     `[data-hb-mass]` to bind to: the readout is markup, it says 50.0 g
     through every frame of the run, and the one number that could report
     a loss is the one number nothing here can move.

     ⚖️ EVERY BOUNDARY COMES OUT OF `keys`. The five bands, the two
     shaded plateaus and the flask's melt and boil fractions are derived
     from the same authored breakpoints the curve is drawn from, so the
     picture, the bands and the readouts cannot disagree. Design's page
     writes the boundaries three times (`phaseAt` and the two flask
     fractions) and they have to be kept in step by hand.

     ⚠️ Emit-both-show-one for the phase word and the five plateau notes.
     Those notes are the science of the block; none of them is ever
     rebuilt from an attribute, so `<em>` survives and no sentence is
     assembled in JS.

     ⊕ There is no animation loop here — the drawing is a pure function
     of the scrub position, so a frame is only ever produced by a student
     moving the control. `prefers-reduced-motion` has nothing to degrade
     and nothing is degraded: the bench is the same complete instrument
     either way. */
  function wireHeatingBench(sec) {
    var wrap = sec.querySelector("[data-hb]");
    if (!wrap) { return; }
    var cfg;
    try { cfg = JSON.parse(wrap.getAttribute("data-cfg") || "{}"); }
    catch (err) { cfg = {}; }
    var KEYS = cfg.keys || [];
    var PH = cfg.phases || [];
    var G = cfg.graph || {};
    if (KEYS.length < 2 || PH.length !== KEYS.length - 1) { return; }

    var canvas = wrap.querySelector("[data-hb-canvas]");
    var scrub = wrap.querySelector("[data-hb-scrub]");
    var tempEl = wrap.querySelector("[data-hb-temp]");
    var words = toArray(wrap.querySelectorAll(".ks3-hb-phase"));
    var notes = toArray(wrap.querySelectorAll(".ks3-hb-note"));
    var jumps = toArray(wrap.querySelectorAll(".ks3-hb-jump"));
    var total = parseInt(wrap.getAttribute("data-total"), 10) || 0;

    /* U+2212 MINUS on the visible readout, ASCII on the spoken one — a
       screen reader makes "minus 20" of `-20` and much less of `−20`. */
    var MINUS = "−";
    var UNIT = cfg.unit || "";

    /* Design's canvas palette, lifted (c1-03 lines 467–612). These are
       paint, not tokens: canvas takes no CSS custom properties, and the
       four instruments already in the key stage hardcode theirs too. */
    var PAPER = "#FFFDF8", GRID = "#E4DACA", AXIS = "#1A1714",
        LABEL = "#6B6055", BAND = "rgba(228,87,46,0.10)", BANDTEXT = "#A93411",
        GHOST = "#D9CDBA", LIVE = "#E4572E", GLASS = "#F6EEE0",
        DOT = "#D98A4A", DOTLINE = "#5A3212";
    var MONO = '"DM Mono", ui-monospace, monospace';

    var value = parseInt(scrub && scrub.value, 10) || 0;
    var visited = {};

    function num(v, fallback) {
      return (typeof v === "number" && isFinite(v)) ? v : fallback;
    }
    /* Halves UP, and the Python renderer floors `t + 0.5` for the same
       reason: the resting readout and the first repaint must agree. */
    function round(t) { return Math.round(t); }

    function tempAt(x) {
      for (var i = 0; i < KEYS.length - 1; i++) {
        var x0 = KEYS[i][0], t0 = KEYS[i][1],
            x1 = KEYS[i + 1][0], t1 = KEYS[i + 1][1];
        if (x <= x1) { return t0 + (t1 - t0) * ((x - x0) / (x1 - x0)); }
      }
      return KEYS[KEYS.length - 1][1];
    }
    function phaseAt(x) {
      for (var i = 0; i < KEYS.length - 1; i++) {
        if (x < KEYS[i + 1][0]) { return i; }
      }
      return KEYS.length - 2;
    }
    function isPlateau(i) { return KEYS[i][1] === KEYS[i + 1][1]; }
    function fill(tpl, t, label) {
      return String(tpl || "").split("{t}").join(String(round(t)))
        .split("{phase}").join(String(label || "").toLowerCase());
    }

    var plateaus = [];
    for (var pi = 0; pi < KEYS.length - 1; pi++) {
      if (isPlateau(pi)) { plateaus.push(pi); }
    }
    var firstPlateau = plateaus.length ? plateaus[0] : -1;
    var lastPlateau = plateaus.length ? plateaus[plateaus.length - 1] : -1;

    function draw() {
      if (!canvas || !canvas.getContext) { return; }
      var ctx = canvas.getContext("2d");
      var W = 900, H = 330;
      ctx.setTransform(1, 0, 0, 1, 0, 0);
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      ctx.setTransform(2, 0, 0, 2, 0, 0);
      ctx.fillStyle = PAPER;
      ctx.fillRect(0, 0, W, H);

      var x = value, i = phaseAt(x), ph = PH[i] || {};
      var tmin = num(G.t_min, -30), tmax = num(G.t_max, 130);

      // ── the curve, left ──
      var gx = 62, gy = 40, gw = 470, gh = H - 110;
      function px(v) { return gx + (v / 100) * gw; }
      function py(t) { return gy + gh - ((t - tmin) / (tmax - tmin)) * gh; }

      ctx.strokeStyle = GRID;
      ctx.lineWidth = 1.5;
      each(G.grid || [], function (t) {
        ctx.beginPath();
        ctx.moveTo(gx, py(t));
        ctx.lineTo(gx + gw, py(t));
        ctx.stroke();
      });

      ctx.strokeStyle = AXIS;
      ctx.lineWidth = 2.5;
      ctx.beginPath();
      ctx.moveTo(gx, gy);
      ctx.lineTo(gx, gy + gh);
      ctx.lineTo(gx + gw, gy + gh);
      ctx.stroke();

      ctx.fillStyle = LABEL;
      ctx.font = '500 12px ' + MONO;
      ctx.textAlign = "right";
      each(G.ticks || [], function (t) {
        ctx.fillText((t < 0 ? MINUS : "") + Math.abs(t), gx - 8, py(t) + 4);
      });
      ctx.textAlign = "left";
      ctx.fillText(G.y_label || "", gx - 4, gy - 14);
      ctx.textAlign = "right";
      ctx.fillText(G.x_label || "", gx + gw, gy + gh + 22);

      // The shaded plateaus, and their captions. Both come out of `keys`,
      // so a plateau cannot be shaded in one place and not another.
      each(plateaus, function (p) {
        ctx.fillStyle = BAND;
        ctx.fillRect(px(KEYS[p][0]), gy,
                     px(KEYS[p + 1][0]) - px(KEYS[p][0]), gh);
        ctx.fillStyle = BANDTEXT;
        ctx.font = '500 11px ' + MONO;
        ctx.textAlign = "center";
        ctx.fillText((PH[p] || {}).band || "",
                     (px(KEYS[p][0]) + px(KEYS[p + 1][0])) / 2, gy + 14);
      });

      // The whole run ghosted, then the part that has been reached.
      ctx.lineWidth = 3.5;
      ctx.lineJoin = "round";
      ctx.strokeStyle = GHOST;
      ctx.beginPath();
      each(KEYS, function (k, n) {
        if (n) { ctx.lineTo(px(k[0]), py(k[1])); }
        else { ctx.moveTo(px(k[0]), py(k[1])); }
      });
      ctx.stroke();

      ctx.strokeStyle = LIVE;
      ctx.beginPath();
      ctx.moveTo(px(KEYS[0][0]), py(KEYS[0][1]));
      for (var v = 0; v <= x; v += 1) { ctx.lineTo(px(v), py(tempAt(v))); }
      ctx.stroke();

      ctx.beginPath();
      ctx.arc(px(x), py(tempAt(x)), 8, 0, Math.PI * 2);
      ctx.fillStyle = LIVE;
      ctx.fill();
      ctx.strokeStyle = AXIS;
      ctx.lineWidth = 2.5;
      ctx.stroke();

      // ── the sealed flask, right ──
      var fx = 596, fy = 44, fw = 250, fh = H - 120;
      ctx.fillStyle = GLASS;
      ctx.fillRect(fx, fy, fw, fh);
      ctx.strokeStyle = AXIS;
      ctx.lineWidth = 3;
      ctx.strokeRect(fx, fy, fw, fh);

      ctx.save();
      ctx.beginPath();
      ctx.rect(fx + 2, fy + 2, fw - 4, fh - 4);
      ctx.clip();

      function drawP(cxp, cyp, r) {
        ctx.beginPath();
        ctx.arc(cxp, cyp, r, 0, Math.PI * 2);
        ctx.fillStyle = DOT;
        ctx.fill();
        ctx.strokeStyle = DOTLINE;
        ctx.lineWidth = 1.8;
        ctx.stroke();
      }

      // The population is constant across every routine below — 40
      // particles in, 40 particles out, whatever state they are in.
      var N = 40, rr = 10;
      var frac = (x - KEYS[i][0]) / (KEYS[i + 1][0] - KEYS[i][0]);
      var row, col, idx, n;

      // ⚠️ Which routine runs is decided by the SHAPE OF THE CURVE, not by
      // a phase id: before the first plateau it is a solid, between the two
      // it is a liquid, after the last it is a gas. An authored id could be
      // renamed; the physics of the curve cannot.
      if (i < firstPlateau) {
        for (row = 0; row < 5; row++) {
          for (col = 0; col < 8; col++) {
            drawP(fx + 26 + col * 28, fy + fh - 24 - row * 26, rr);
          }
        }
      } else if (i === firstPlateau) {
        for (row = 0; row < 5; row++) {
          for (col = 0; col < 8; col++) {
            idx = row * 8 + col;
            var molten = idx < frac * N;
            var jx = molten ? Math.sin(idx * 2.7) * 9 : 0;
            var jy = molten ? Math.cos(idx * 1.9) * 7 : 0;
            drawP(fx + 26 + col * 28 + jx, fy + fh - 24 - row * 26 + jy, rr);
          }
        }
      } else if (i < lastPlateau) {
        for (n = 0; n < N; n++) {
          drawP(fx + 30 + ((n * 53) % (fw - 60)),
                fy + fh - 22 - ((n * 37) % (fh * 0.6)) - Math.sin(n * 2.399) * 4,
                rr);
        }
      } else if (i === lastPlateau) {
        var nLiquid = Math.round(N * (1 - frac));
        for (n = 0; n < nLiquid; n++) {
          drawP(fx + 30 + ((n * 53) % (fw - 60)),
                fy + fh - 22 - ((n * 37) % (fh * 0.5)), rr);
        }
        for (n = 0; n < N - nLiquid; n++) {
          drawP(fx + 24 + ((n * 71) % (fw - 48)),
                fy + 26 + ((n * 43) % Math.max(20, fh * 0.5)), rr);
        }
      } else {
        for (n = 0; n < 24; n++) {
          drawP(fx + 22 + ((n * 91) % (fw - 44)),
                fy + 22 + ((n * 67) % (fh - 44)), rr);
        }
      }
      ctx.restore();

      // The banner exists only while a state is changing, which is why
      // only a plateau carries one (the renderer refuses any other).
      if (ph.banner) {
        ctx.fillStyle = BANDTEXT;
        ctx.font = '500 12px ' + MONO;
        ctx.textAlign = "center";
        ctx.fillText(ph.banner, fx + fw / 2, fy + 20);
      }

      ctx.fillStyle = LABEL;
      ctx.font = '500 12px ' + MONO;
      ctx.textAlign = "left";
      ctx.fillText((cfg.flask || {}).caption || "", fx, fy + fh + 22);

      if (canvas.setAttribute) {
        canvas.setAttribute("aria-label",
          fill((cfg.alt || {}).template, tempAt(x), ph.label));
      }
    }

    function repaint() {
      var i = phaseAt(value), ph = PH[i] || {};
      var T = tempAt(value);

      if (tempEl) {
        var r = round(T);
        tempEl.textContent = (r < 0 ? MINUS : "") + Math.abs(r) + " " + UNIT;
      }
      each(words, function (el, n) { setHidden(el, n !== i); });
      each(notes, function (el, n) { setHidden(el, n !== i); });
      each(jumps, function (b) {
        var v = parseInt(b.getAttribute("data-v"), 10) || 0;
        b.setAttribute("aria-pressed",
                       Math.abs(value - v) < 3 ? "true" : "false");
      });
      if (scrub) {
        scrub.value = String(value);
        scrub.setAttribute("aria-valuetext", fill(cfg.valuetext, T, ph.label));
      }
      draw();

      // ⚖️ BOTH plateaus, and only by LANDING on one. A student who has
      // watched the temperature refuse to rise once has seen the argument;
      // the lesson is that it happens twice, and for very different
      // amounts of energy. The jump buttons are the affordance for anyone
      // who cannot drag.
      if (isPlateau(i)) { visited[i] = true; }
      var n = 0, k;
      for (k in visited) { if (visited[k]) { n += 1; } }
      setCount(sec, n);
      if (total && n >= total) { markStage(sec, true); }
    }

    function set(v) {
      v = Math.max(0, Math.min(100, isNaN(v) ? 0 : v));
      value = v;
      repaint();
    }

    if (scrub) {
      scrub.addEventListener("input", function () {
        set(parseInt(scrub.value, 10));
      });
      // Some browsers fire only `change` for a keyboard step.
      scrub.addEventListener("change", function () {
        set(parseInt(scrub.value, 10));
      });
    }
    each(jumps, function (b) {
      b.addEventListener("click", function () {
        set(parseInt(b.getAttribute("data-v"), 10));
      });
    });

    repaint();
    wireBenchGate(sec);
  }
