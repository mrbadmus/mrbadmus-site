/* WIRE: each(root.querySelectorAll("[data-erunblock]"), wireEnzymeRun);
   — add to wireInstruments(), in the B3 group. Uses each / toArray /
   setHidden / setCount / markStage / motionReduced, all already in scope. */

  /* ── enzyme-run (b3-06 #s-bench) ──
     One tube, two dials and a run. Substrate falls, product rises, and the
     enzyme count does not move.

     ⚖️ THE THIRD COUNTER IS THE LESSON, so there is nothing in this
     function that touches it. `r_enzyme_run` emits it with no
     `data-value` and no `data-bar`; there is no handle here to take hold
     of, and that is deliberate rather than an omission. The same
     construction as `heating-bench`'s mass tile.

     ⚖️ THE DENATURE LATCH FIRES ON THE TEMPERATURE CONTROL, not inside
     the tick. NOTES-B3 flag 16 records what the other arrangement cost: a
     student who dragged to 60 °C, watched the rate read 0% and dragged
     back to 37 °C was shown a full recovery to 100%, so the instrument
     built to kill "cooling brings it back" was demonstrating it. Dragging
     the slider is the cheaper interaction and it must be the one that
     latches. Switching enzyme and taking a fresh tube both RE-latch while
     the tube is still hot, which closes the obvious loophole.

     ⚖️ REDUCED MOTION SCALES THE RATE AND NEVER STOPS THE COUNTER. The
     run is the argument — substrate down, product up, enzyme unchanged —
     so a reduced-motion student must reach the same end state, and does:
     every one of the authored ticks happens, each one further apart. It
     is asked INSIDE the tick, so an OS setting or the page's Motion
     control changed mid-run takes effect without a reload.

     ⚠️ NOTHING IS ASSEMBLED FROM WORDS HERE. Six temperature notes and
     three verdicts are all in the document, eight hidden; this function
     swaps which one is shown. Only two live numbers are substituted, the
     tick count and the rate percentage, and both are substituted into
     authored format strings.

     ⊕ ONE ADDITION, where Design's page is silent: the verdict shows
     whenever a run has FINISHED, whatever finished it. Design shows it on
     twenty ticks or on denaturing, so a rate of exactly zero that is NOT
     denatured — stomach protease dropped into pH 8, one press of one
     button — finished on its first tick and showed nothing at all. The
     "slow" verdict that exists to send the student back to the pH dial
     never appeared. Design's three branches are unchanged. */
  function wireEnzymeRun(sec) {
    var wrap = sec.querySelector("[data-erun]");
    if (!wrap) { return; }
    var cfg;
    try { cfg = JSON.parse(wrap.getAttribute("data-cfg") || "{}"); }
    catch (err) { cfg = {}; }
    var L = cfg.labels || {};
    var BANDS = cfg.bands || {};
    var OPT = cfg.opt_ph || {};
    if (!L.rate || !BANDS.optimum) { return; }

    var ztabs = toArray(wrap.querySelectorAll(".ks3-erun-enzyme"));
    var ptabs = toArray(wrap.querySelectorAll(".ks3-erun-ph"));
    var slider = wrap.querySelector("[data-temp]");
    var tempVal = wrap.querySelector("[data-temp-value]");
    var notes = toArray(wrap.querySelectorAll(".ks3-erun-tempnote"));
    var equations = toArray(wrap.querySelectorAll(".ks3-erun-equation"));
    var names = toArray(wrap.querySelectorAll(".ks3-erun-countername"));
    var rateEl = wrap.querySelector("[data-rate]");
    var clockEl = wrap.querySelector("[data-clock]");
    var runBtn = wrap.querySelector("[data-run]");
    var resetBtn = wrap.querySelector("[data-reset]");
    var verdict = wrap.querySelector("[data-reveal]");
    var verdicts = toArray(wrap.querySelectorAll(".ks3-erun-verdicttext"));
    var subVal = wrap.querySelector('[data-value="substrate"]');
    var prodVal = wrap.querySelector('[data-value="product"]');
    var subBar = wrap.querySelector('[data-bar="substrate"]');
    var prodBar = wrap.querySelector('[data-bar="product"]');
    if (!slider || !runBtn) { return; }

    var DENATURE = Number(cfg.denature_c);
    var OPTIMUM = Number(cfg.optimum_c);
    var RISE = Number(cfg.rise_exponent);
    var FALL = Number(cfg.fall_divisor);
    var SPAN = Number(cfg.ph_span);
    var TICKS = Number(cfg.ticks) || 20;
    var TICK_MS = Number(cfg.tick_ms) || 160;
    var PER_TICK = Number(cfg.units_per_tick) || 90;
    var START_SUB = Number(cfg.start_substrate) || 1000;
    var RM = Number(cfg.reduced_motion_scale) || 0.35;
    var SLOW = Number(cfg.slow_below_pct) || 25;

    var enzyme = ztabs.length ? ztabs[0].getAttribute("data-enzyme") : "";
    var ph = ptabs.length ? Number(ptabs[0].getAttribute("data-ph")) : 7;
    each(ptabs, function (b) {
      if (b.getAttribute("aria-pressed") === "true") {
        ph = Number(b.getAttribute("data-ph"));
      }
    });
    var temp = Number(slider.value);
    var substrate = START_SUB;
    var product = 0;
    var denatured = temp >= DENATURE;
    var running = false;
    var clock = 0;
    var everRan = false;
    var finished = false;
    var timer = null;

    function fill(tpl, map) {
      var out = String(tpl || ""), k;
      for (k in map) {
        if (Object.prototype.hasOwnProperty.call(map, k)) {
          out = out.split("{" + k + "}").join(String(map[k]));
        }
      }
      return out;
    }

    /* ⚠️ `_erun_rate` in build_ks3.py IS THIS FUNCTION. The resting page
       prints a rate computed there and the first repaint recomputes it
       here; if the two ever disagree the number visibly jumps on load. A
       change to one is a change to both. */
    function rateFor() {
      if (denatured || temp >= DENATURE) { return 0; }
      var tTerm = temp <= OPTIMUM
        ? Math.pow(temp / OPTIMUM, RISE)
        : Math.max(0, 1 - Math.pow((temp - OPTIMUM) / FALL, 2));
      var gap = Math.abs(ph - Number(OPT[enzyme]));
      var pTerm = Math.max(0, 1 - gap / SPAN);
      return Math.max(0, Math.min(1, tTerm * pTerm));
    }

    function noteKey() {
      if (denatured && temp >= DENATURE) { return "denatured_hot"; }
      if (denatured) { return "denatured_cool"; }
      if (temp >= Number(BANDS.past_optimum)) { return "past_optimum"; }
      if (temp >= Number(BANDS.optimum)) { return "optimum"; }
      if (temp >= Number(BANDS.cold)) { return "cold"; }
      return "freezing";
    }

    function repaint() {
      var pct = Math.round(rateFor() * 100);
      var tempText = fill(cfg.temp_format, { t: temp });

      if (tempVal) { tempVal.textContent = tempText; }
      slider.setAttribute("aria-valuetext", tempText);
      var key = noteKey();
      each(notes, function (el) {
        setHidden(el, el.getAttribute("data-note") !== key);
      });
      each(equations, function (el) {
        setHidden(el, el.getAttribute("data-enzyme") !== enzyme);
      });
      each(names, function (el) {
        setHidden(el, el.getAttribute("data-enzyme") !== enzyme);
      });
      if (rateEl) { rateEl.textContent = fill(L.rate, { pct: pct }); }
      if (subVal) {
        subVal.textContent = fill(cfg.units_format, { n: substrate });
      }
      if (prodVal) {
        prodVal.textContent = fill(cfg.units_format, { n: product });
      }
      if (subBar) {
        subBar.style.width = (substrate / START_SUB * 100).toFixed(1) + "%";
      }
      if (prodBar) {
        prodBar.style.width = (product / START_SUB * 100).toFixed(1) + "%";
      }
      if (clockEl) {
        clockEl.textContent = clock
          ? fill(L.clock, { n: clock, total: TICKS })
          : L.clock_fresh;
      }
      runBtn.textContent = running ? L.running : (clock ? L.more : L.start);
      if (running || substrate === 0) { runBtn.setAttribute("disabled", ""); }
      else { runBtn.removeAttribute("disabled"); }

      /* ⊕ Any finished run shows a verdict — see the header. Which branch
         is Design's, unchanged: denatured first, then a rate too low to be
         doing anything, then the run that worked. */
      if (finished && !running) {
        var which = denatured ? "denatured" : (pct < SLOW ? "slow" : "worked");
        each(verdicts, function (el) {
          setHidden(el, el.getAttribute("data-verdict") !== which);
        });
        setHidden(verdict, false);
      }

      setCount(sec, everRan ? 1 : 0);
      markStage(sec, everRan);
    }

    function stop() {
      if (timer) { clearTimeout(timer); timer = null; }
      running = false;
    }

    function tick() {
      /* Asked EVERY tick, so an OS setting or the page's Motion control
         changed mid-run takes effect without a reload — and the reaction
         slows rather than stopping, so every authored tick still happens
         and the reduced-motion student reaches the same end state. */
      var scale = motionReduced() ? RM : 1;
      var rate = rateFor();
      var converted = Math.min(substrate, Math.round(rate * PER_TICK));
      substrate -= converted;
      product += converted;
      clock += 1;
      if (clock >= TICKS || (converted === 0 && rate === 0) || !substrate) {
        finished = true;
        stop();
      } else {
        timer = setTimeout(tick, TICK_MS / scale);
      }
      repaint();
    }

    each(ztabs, function (b) {
      b.addEventListener("click", function () {
        stop();
        enzyme = b.getAttribute("data-enzyme");
        each(ztabs, function (o) {
          o.setAttribute("aria-pressed", o === b ? "true" : "false");
        });
        /* A new tube of a different enzyme — but a tube still above the
           threshold denatures it at once, which closes the loophole of
           switching enzyme to escape the latch. */
        substrate = START_SUB;
        product = 0;
        clock = 0;
        finished = false;
        denatured = temp >= DENATURE;
        setHidden(verdict, true);
        repaint();
      });
    });

    each(ptabs, function (b) {
      b.addEventListener("click", function () {
        ph = Number(b.getAttribute("data-ph"));
        each(ptabs, function (o) {
          o.setAttribute("aria-pressed", o === b ? "true" : "false");
        });
        /* The counters deliberately do NOT reset: changing the pH and
           running on is how a student sees the same tube go faster. */
        repaint();
      });
    });

    function onTemp() {
      temp = Number(slider.value);
      /* THE LATCH. Once above the threshold, always denatured — cooling
         does not clear it and only a fresh tube does. */
      if (temp >= DENATURE) { denatured = true; }
      repaint();
    }
    /* Bound to both, because some browsers fire only `change` for a
       keyboard step. */
    slider.addEventListener("input", onTemp);
    slider.addEventListener("change", onTemp);

    runBtn.addEventListener("click", function () {
      if (running || substrate === 0) { return; }
      stop();
      running = true;
      everRan = true;
      finished = false;
      clock = 0;
      setHidden(verdict, true);
      repaint();
      /* ⊕ THE FIRST TICK HAPPENS ON THE PRESS, not one interval later.
         Design schedules every tick including the first, so pressing Run
         gives 160 ms of nothing — and when the rate is zero, 160 ms of
         nothing followed by a run that is already over. `tick()` schedules
         its own successor, so this shortens the run by one interval and
         changes nothing else. */
      tick();
    });

    if (resetBtn) {
      resetBtn.addEventListener("click", function () {
        stop();
        substrate = START_SUB;
        product = 0;
        clock = 0;
        finished = false;
        /* Re-latches if the tube is still hot: a fresh tube in a hot bath
           is a fresh enzyme that denatures on arrival. */
        denatured = temp >= DENATURE;
        setHidden(verdict, true);
        repaint();
      });
    }

    repaint();
  }
