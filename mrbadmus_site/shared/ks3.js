/* ═══════════════════════════════════════════════════════════════
   KS3 — lesson interactions.  architecture.md §5.0, §5.8.

   Three jobs, and nothing else:

   Law 4 — predict before reveal. No stateful reveal is shown until
           the student has committed to a prediction. An unspoken
           wrong belief is invisible to its holder; committing is
           what drags it into the open.
   Law 8 — the mastery ladder persists, and "retry my misses" works.
   Law 9 — motion is animated, and reduced-motion users get the
           instant swap (handled in ks3.css, honoured here by not
           forcing any inline animation).

   Persistence uses localStorage on the same pattern as bonding v2
   (`quiz_best_<id>`), per §8.7. Server-side progress is Phase 5.

   Never punish: no streaks, no guilt copy, no XP, no timers.
   ═══════════════════════════════════════════════════════════════ */
(function () {
  "use strict";

  var STORE_PREFIX = "ks3_best_";

  function readBest(id) {
    try {
      var v = window.localStorage.getItem(STORE_PREFIX + id);
      return v === null ? null : JSON.parse(v);
    } catch (e) { return null; }
  }

  function writeBest(id, value) {
    try {
      window.localStorage.setItem(STORE_PREFIX + id, JSON.stringify(value));
    } catch (e) { /* private mode — the lesson still works, just not saved */ }
  }

  /* ── Law 4: a reveal is gated behind a committed prediction ── */
  function wirePredictions(root) {
    var blocks = root.querySelectorAll("[data-activity]");
    Array.prototype.forEach.call(blocks, function (block) {
      var reveal = block.querySelector("[data-reveal]");
      var options = block.querySelectorAll(".ks3-option");
      if (!options.length) { return; }

      Array.prototype.forEach.call(options, function (btn) {
        btn.setAttribute("aria-pressed", "false");
        btn.addEventListener("click", function () {
          Array.prototype.forEach.call(options, function (b) {
            b.setAttribute("aria-pressed", "false");
          });
          btn.setAttribute("aria-pressed", "true");
          if (reveal && reveal.hasAttribute("hidden")) {
            reveal.removeAttribute("hidden");
            // Announce the reveal for screen-reader users, who would
            // otherwise get no signal that new content appeared.
            reveal.setAttribute("role", "status");
          }
        });
      });
    });
  }

  /* ── Law 8: the four-rung ladder ── */
  function wireLadder(ladder) {
    var lessonId = ladder.getAttribute("data-lesson") || "lesson";
    var rungs = ladder.querySelectorAll(".ks3-rung");
    var answered = {};
    var missed = {};

    function scoreLine() {
      var got = 0, total = 0;
      Object.keys(answered).forEach(function (k) {
        total += 1;
        if (answered[k]) { got += 1; }
      });
      return { got: got, total: total };
    }

    var summary = document.createElement("div");
    summary.className = "ks3-ladder-summary";
    summary.setAttribute("role", "status");
    ladder.appendChild(summary);

    var retry = document.createElement("button");
    retry.type = "button";
    retry.className = "ks3-retry";
    retry.textContent = "Retry my misses";
    retry.hidden = true;
    ladder.appendChild(retry);

    function refresh() {
      var s = scoreLine();
      if (!s.total) { summary.textContent = ""; return; }
      var best = readBest(lessonId);
      var txt = "You got " + s.got + " of " + s.total + ".";
      if (best && typeof best.got === "number") {
        if (s.got > best.got) {
          txt += " That's your best yet — up " + (s.got - best.got) + ".";
        } else {
          txt += " Your best so far is " + best.got + ".";
        }
      }
      summary.textContent = txt;
      if (!best || s.got > best.got) { writeBest(lessonId, s); }
      retry.hidden = Object.keys(missed).length === 0;
    }

    Array.prototype.forEach.call(rungs, function (rung) {
      var key = rung.getAttribute("data-rung");
      var options = rung.querySelectorAll(".ks3-option");
      if (!options.length) { return; }

      var fb = document.createElement("p");
      fb.className = "ks3-feedback";
      fb.setAttribute("role", "status");
      rung.appendChild(fb);

      Array.prototype.forEach.call(options, function (btn) {
        btn.addEventListener("click", function () {
          if (rung.getAttribute("data-locked") === "1") { return; }
          rung.setAttribute("data-locked", "1");

          var correct = btn.getAttribute("data-correct") === "1";
          answered[key] = correct;
          if (correct) { delete missed[key]; } else { missed[key] = true; }

          Array.prototype.forEach.call(options, function (b) {
            b.disabled = true;
            if (b.getAttribute("data-correct") === "1") {
              b.classList.add("is-correct");
            }
          });
          if (!correct) { btn.classList.add("is-wrong"); }

          // Law 10: the feedback corrects THIS misconception, not a
          // generic "wrong, try again".
          fb.textContent = correct
            ? "Correct."
            : (btn.getAttribute("data-feedback") || "Not quite.");
          refresh();
        });
      });
    });

    retry.addEventListener("click", function () {
      Array.prototype.forEach.call(rungs, function (rung) {
        var key = rung.getAttribute("data-rung");
        if (!missed[key]) { return; }
        rung.removeAttribute("data-locked");
        delete answered[key];
        var fb = rung.querySelector(".ks3-feedback");
        if (fb) { fb.textContent = ""; }
        Array.prototype.forEach.call(rung.querySelectorAll(".ks3-option"),
          function (b) {
            b.disabled = false;
            b.classList.remove("is-correct", "is-wrong");
            b.setAttribute("aria-pressed", "false");
          });
      });
      missed = {};
      retry.hidden = true;
      var first = ladder.querySelector(".ks3-rung:not([data-locked]) .ks3-option");
      if (first) { first.focus(); }
      refresh();
    });

    refresh();
  }

  /* ═══════════════════════════════════════════════════════════════
     Flip cards / click-to-reveal.  MRB-177 principle 3.

     A card is a <button>, not a div with a click handler, so keyboard
     and screen-reader users get it for free. `aria-expanded` carries
     the state; the 3D flip is CSS and reduced-motion turns it into an
     instant swap (Law 9's fallback).

     Discernment, per the ruling: a card is for a fact worth WONDERING
     about for a second. A definition the student must simply absorb is
     not improved by hiding it, so not every fact becomes a card — that
     decision lives in the content, not here.
     ═══════════════════════════════════════════════════════════════ */
  function wireCards(root) {
    var cards = root.querySelectorAll(".ks3-card-btn");
    Array.prototype.forEach.call(cards, function (btn) {
      var back = btn.querySelector(".ks3-card-back");
      btn.setAttribute("aria-expanded", "false");
      btn.addEventListener("click", function () {
        var open = btn.getAttribute("aria-expanded") === "true";
        btn.setAttribute("aria-expanded", open ? "false" : "true");
        btn.classList.toggle("is-flipped", !open);
        if (back) {
          if (open) { back.setAttribute("hidden", ""); }
          else { back.removeAttribute("hidden"); }
        }
      });
    });
  }

  /* ═══════════════════════════════════════════════════════════════
     Particle labs.  Law 9 — "motion is meaning".

     Three sims, one engine. Each is a box of particles on a canvas;
     what differs is what the particles do and what is measured.

       particle-states — arrangement and motion across solid/liquid/gas
       gas-pressure    — collisions per second against the walls
       diffusion       — two populations random-walking into each other

     THE POINT OF EACH, so nobody "tidies" the physics away:

     * particle-states must show particles VIBRATING in the solid, never
       frozen. PART-04 is "particles in a solid are completely still",
       and a still solid teaches the misconception the lesson is trying
       to kill.
     * gas-pressure must show pressure as a COUNT OF WALL HITS. PART-08
       is "pressure is particles pushing each other". If the readout is
       just a number that goes up, the sim has not confronted anything.
     * diffusion must show movement in BOTH directions. PART-11 is that
       particles "want" to spread out. Watching red cross right while
       blue crosses left is what makes randomness visible; a one-way
       spreading animation would confirm the misconception instead.

     Law 4 — the sim will not run until the student has committed to a
     prediction. It renders frozen with a "predict first" cover.

     Reduced motion: no animation loop at all. One representative frame
     is drawn and the readout carries the result in words, so the
     content is never motion-dependent.
     ═══════════════════════════════════════════════════════════════ */

  var REDUCED = window.matchMedia
    && window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  // The controls a lab can ask for. build_ks3.py validates authored
  // `sim.controls` against this same list and FAILS THE BUILD on anything
  // else, so a lesson can never ship a control panel that silently does
  // nothing — which is what happened when the content authored `state`,
  // `medium`, `release` and `number of particles` against a JS that
  // implemented only two of them.
  var CONTROL_LABELS = {
    temperature: "Temperature",
    volume:      "Space to move in",
    particles:   "How many particles",
    medium:      "What it spreads through"
  };

  function cssVar(el, name, fallback) {
    try {
      var v = getComputedStyle(el).getPropertyValue(name);
      return (v && v.trim()) || fallback;
    } catch (e) { return fallback; }
  }

  function rand(a, b) { return a + Math.random() * (b - a); }

  // "1 orange particles" is the kind of thing a Year 7 notices and an adult
  // reads straight past. The readout is student-facing text, so it agrees.
  function plural(n, noun) {
    return n + " " + noun + (n === 1 ? " has" : "s have");
  }

  function makeParticles(n, w, h, opts) {
    var ps = [], i, cols = Math.ceil(Math.sqrt(n));

    // The lattice is packed TIGHT — spacing is a bit over one diameter, so
    // the particles are touching. This is the whole point of the solid and
    // liquid states and it is easy to get wrong: spreading the lattice over
    // the full box draws a solid that looks exactly like a gas, which
    // teaches the opposite of what the lesson is for. The gas state earns
    // its spread by having no spring holding it, not by starting spread out.
    var spacing = (opts && opts.spacing) || 16;
    var rows = Math.ceil(n / cols);
    var ox = (w - (cols - 1) * spacing) / 2;
    var oy = (h - (rows - 1) * spacing) / 2;

    for (i = 0; i < n; i++) {
      var hx = ox + (i % cols) * spacing;
      var hy = oy + Math.floor(i / cols) * spacing;
      ps.push({
        x: opts && opts.lattice ? hx : rand(8, w - 8),
        y: opts && opts.lattice ? hy : rand(8, h - 8),
        hx: hx, hy: hy,                   // lattice home, for solid and liquid
        vx: rand(-1, 1), vy: rand(-1, 1),
        team: i % 2
      });
    }
    return ps;
  }

  function drawDot(ctx, p, r, colour) {
    ctx.beginPath();
    ctx.arc(p.x, p.y, r, 0, Math.PI * 2);
    ctx.fillStyle = colour;
    ctx.fill();
  }

  function wireSim(sim) {
    var canvas = sim.querySelector(".ks3-sim-canvas");
    if (!canvas || !canvas.getContext) { return; }
    var ctx = canvas.getContext("2d");
    var kind = sim.getAttribute("data-sim");
    var readout = sim.querySelector(".ks3-sim-readout");
    var W = canvas.width, H = canvas.height;

    var ink = cssVar(sim, "--text", "#241C14");
    var accent = cssVar(sim, "--accent", "#C4490F");
    var cool = cssVar(sim, "--physics", "#1D6FB8");
    var rule = cssVar(sim, "--border", "#D4C7AD");

    var state = {
      temp: 50,          // 0-100, drives speed and (for states) bonding
      volume: 100,       // 0-100, right wall position as a % of W
      medium: "gas",     // gas | liquid — diffusion is far slower in a liquid
      active: null,      // how many particles are in play (null = all)
      running: false,
      hits: 0, hitRate: 0, lastSample: 0,
      // particle-states uses fewer, larger particles so a tight lattice
      // reads as a lump of touching particles rather than a dusting.
      particles: makeParticles(
        kind === "diffusion" ? 120 : (kind === "particle-states" ? 64 : 90),
        W, H,
        { lattice: kind === "particle-states", spacing: 17 })
    };
    var dotR = kind === "particle-states" ? 7 : 4;

    // Only the first `active` particles are in play. Slicing rather than
    // hiding keeps step(), draw() and the diffusion count reading the same
    // population — a readout counting particles that are not on screen is
    // worse than no readout.
    function inPlay() {
      return state.active === null
        ? state.particles
        : state.particles.slice(0, state.active);
    }

    if (kind === "diffusion") {
      // Two populations, cleanly separated, so the mixing is the story.
      state.particles.forEach(function (p, i) {
        p.team = i % 2;
        p.x = p.team === 0 ? rand(8, W * 0.45) : rand(W * 0.55, W - 8);
        p.y = rand(8, H - 8);
      });
    }

    function stateName(t) {
      return t < 33 ? "Solid" : (t < 66 ? "Liquid" : "Gas");
    }

    function say(txt) { if (readout) { readout.textContent = txt; } }

    function step() {
      var wallX = kind === "gas-pressure" ? W * (state.volume / 100) : W;
      var speed = 0.4 + (state.temp / 100) * 2.4;
      var t = state.temp;

      // A liquid is crowded: a particle gets nowhere before it hits a
      // neighbour. Slower travel plus far more frequent scattering is what
      // makes diffusion visibly slower in a liquid than in a gas, which is
      // the point the `medium` control exists to make.
      var scatter = 0.04;
      if (state.medium === "liquid") { speed *= 0.35; scatter = 0.16; }

      inPlay().forEach(function (p) {
        if (kind === "particle-states" && t < 66) {
          // Solid and liquid: a spring back to the lattice home. Strong
          // when cold (vibration on the spot), weak when warm (particles
          // slide past each other but stay touching).
          var k = t < 33 ? 0.06 : 0.022;
          p.vx += (p.hx - p.x) * k + rand(-0.5, 0.5) * (0.3 + t / 60);
          p.vy += (p.hy - p.y) * k + rand(-0.5, 0.5) * (0.3 + t / 60);
          p.vx *= 0.86; p.vy *= 0.86;
        } else {
          // Gas, and both other sims: straight lines between collisions.
          //
          // The scattering below is not decoration — without it a particle
          // keeps its heading forever, merely bouncing off walls, and two
          // populations that start apart STAY apart. Diffusion then never
          // happens and the sim quietly teaches that it doesn't. Real
          // particles change direction because they hit each other, so a
          // per-frame chance of a new heading is the cheap honest model of
          // that, and it is what makes the walk actually random.
          if (Math.random() < scatter) {
            var ang = rand(0, Math.PI * 2);
            p.vx = Math.cos(ang); p.vy = Math.sin(ang);
          }
          var m = Math.sqrt(p.vx * p.vx + p.vy * p.vy) || 1;
          p.vx = (p.vx / m) * speed;
          p.vy = (p.vy / m) * speed;
        }
        p.x += p.vx; p.y += p.vy;

        // Walls. Each bounce off the right-hand wall is one "push", which
        // is the whole of what pressure is in this model.
        if (p.x < 4) { p.x = 4; p.vx = -p.vx; state.hits++; }
        if (p.x > wallX - 4) { p.x = wallX - 4; p.vx = -p.vx; state.hits++; }
        if (p.y < 4) { p.y = 4; p.vy = -p.vy; state.hits++; }
        if (p.y > H - 4) { p.y = H - 4; p.vy = -p.vy; state.hits++; }
      });
    }

    function draw() {
      var wallX = kind === "gas-pressure" ? W * (state.volume / 100) : W;
      ctx.clearRect(0, 0, W, H);

      if (kind === "gas-pressure" && wallX < W - 1) {
        ctx.fillStyle = rule;
        ctx.fillRect(wallX, 0, W - wallX, H);
        ctx.fillStyle = ink;
        ctx.fillRect(wallX - 2, 0, 3, H);
      }
      inPlay().forEach(function (p) {
        var colour = ink;
        if (kind === "diffusion") { colour = p.team === 0 ? accent : cool; }
        drawDot(ctx, p, dotR, colour);
      });
    }

    // Sampling and wording are separate on purpose. The old single function
    // returned early on its first call (nothing to compare against yet) and
    // again inside the 500ms window — which meant a reduced-motion reader,
    // who gets exactly one call, never saw a readout at all. The words are
    // the whole experience when there is no animation, so they cannot be a
    // side effect of the timer.
    function sample(now) {
      if (!state.lastSample) { state.lastSample = now; return; }
      if (now - state.lastSample < 500) { return; }
      state.hitRate = Math.round(state.hits * (1000 / (now - state.lastSample)));
      state.hits = 0;
      state.lastSample = now;
      report();
    }

    function report() {
      if (kind === "gas-pressure") {
        say("Wall hits per second: " + state.hitRate
            + " — that IS the pressure. Squeeze the gas or heat it and "
            + "the hits get more frequent.");
      } else if (kind === "particle-states") {
        say(stateName(state.temp) + " — "
            + (state.temp < 33
               ? "particles are touching, in a regular pattern, and vibrating on the spot."
               : state.temp < 66
                 ? "particles are still touching, but jumbled and sliding past each other."
                 : "particles are far apart and moving freely in every direction."));
      } else if (kind === "diffusion") {
        var mid = W / 2, rightRed = 0, leftBlue = 0;
        inPlay().forEach(function (p) {
          if (p.team === 0 && p.x > mid) { rightRed++; }
          if (p.team === 1 && p.x < mid) { leftBlue++; }
        });
        say(plural(rightRed, "orange particle") + " crossed to the right, and "
            + plural(leftBlue, "blue one") + " crossed to the left. Both ways "
            + "at once — nothing is pushing them, and nothing is trying to "
            + "spread out.");
      }
    }

    // Reduced motion gets ONE frame, so that frame has to be the settled
    // state at the CURRENT control values — not the state the sim happened
    // to reach before the reader touched anything. Every control change
    // therefore re-settles from scratch rather than just repainting.
    var SETTLE_STEPS = 1400;
    function settle() {
      state.hits = 0;
      for (var i = 0; i < SETTLE_STEPS; i++) { step(); }
      state.hitRate = Math.round(state.hits / (SETTLE_STEPS / 60));
      draw();
      report();
    }

    var raf = null;
    function loop(now) {
      if (!state.running) { return; }
      step(); draw(); sample(now || 0);
      raf = window.requestAnimationFrame(loop);
    }

    function start() {
      if (state.running || REDUCED) { return; }
      state.running = true;
      raf = window.requestAnimationFrame(loop);
    }
    function stop() {
      state.running = false;
      if (raf) { window.cancelAnimationFrame(raf); raf = null; }
    }

    // ── controls, built from data-controls so the markup stays declarative
    var controls = sim.querySelector(".ks3-sim-controls");
    var wanted = (sim.getAttribute("data-controls") || "").split(",");
    if (controls) {
      wanted.forEach(function (name) {
        name = name.trim();
        if (!CONTROL_LABELS.hasOwnProperty(name)) { return; }
        var id = "sim-" + name + "-" + Math.floor(Math.random() * 1e6);
        var wrap = document.createElement("label");
        wrap.className = "ks3-sim-control";
        wrap.setAttribute("for", id);
        wrap.textContent = CONTROL_LABELS[name];

        // `medium` is a two-way choice, not a quantity, so it gets a select
        // rather than a slider with two meaningful stops.
        if (name === "medium") {
          var sel = document.createElement("select");
          sel.id = id;
          [["gas", "In a gas"], ["liquid", "In a liquid"]].forEach(function (o) {
            var opt = document.createElement("option");
            opt.value = o[0]; opt.textContent = o[1];
            sel.appendChild(opt);
          });
          sel.addEventListener("change", function () {
            state.medium = sel.value;
            if (REDUCED && sim.getAttribute("data-locked") !== "1") { settle(); }
          });
          wrap.appendChild(sel);
          controls.appendChild(wrap);
          return;
        }

        var input = document.createElement("input");
        input.type = "range";
        input.id = id;
        input.min = name === "volume" ? "30" : (name === "particles" ? "10" : "0");
        input.max = name === "particles" ? String(state.particles.length) : "100";
        input.value = name === "volume" ? "100"
          : (name === "particles" ? String(state.particles.length) : "50");
        input.addEventListener("input", function () {
          if (name === "temperature") {
            state.temp = Number(input.value);
          } else if (name === "particles") {
            state.active = Number(input.value);
          } else {
            state.volume = Number(input.value);
            // Pull anything the moving wall just swallowed back inside. The
            // running loop would fix this on its next step, but reduced
            // motion has no next step and would paint particles sitting in
            // the solid block of the piston.
            var wallX = W * (state.volume / 100);
            state.particles.forEach(function (p) {
              if (p.x > wallX - 4) { p.x = wallX - 4; }
            });
          }
          if (REDUCED && sim.getAttribute("data-locked") !== "1") { settle(); }
        });
        wrap.appendChild(input);
        controls.appendChild(wrap);
      });
    }

    // ── Law 4: locked until a prediction is committed.
    var activity = sim.closest ? sim.closest("[data-activity]") : null;
    var gated = activity && activity.querySelectorAll(".ks3-option").length > 0;

    function unlock() {
      sim.removeAttribute("data-locked");
      if (REDUCED) {
        // One representative frame, then the words. Nothing is
        // motion-only, so this is a complete experience, not a stub.
        settle();
      } else {
        start();
      }
    }

    if (gated) {
      sim.setAttribute("data-locked", "1");
      Array.prototype.forEach.call(activity.querySelectorAll(".ks3-option"),
        function (btn) { btn.addEventListener("click", unlock); });
      draw();   // frozen first frame behind the cover
    } else {
      unlock();
    }

    // Don't burn a phone battery animating a lab three screens away.
    if (window.IntersectionObserver && !REDUCED) {
      new window.IntersectionObserver(function (entries) {
        entries.forEach(function (en) {
          if (sim.getAttribute("data-locked") === "1") { return; }
          if (en.isIntersecting) { start(); } else { stop(); }
        });
      }, { threshold: 0.05 }).observe(sim);
    }
    document.addEventListener("visibilitychange", function () {
      if (document.hidden) { stop(); }
      else if (sim.getAttribute("data-locked") !== "1") { start(); }
    });
  }

  function wireSims(root) {
    Array.prototype.forEach.call(root.querySelectorAll(".ks3-sim"), wireSim);
  }

  function init() {
    wirePredictions(document);
    wireCards(document);
    wireSims(document);
    Array.prototype.forEach.call(
      document.querySelectorAll(".ks3-ladder"), wireLadder);
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
