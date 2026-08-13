/* ═══════════════════════════════════════════════════════════════
   KS3 — lesson interactions.  Built to docs/ks3/design-reference/SPEC.md:
   §5 (the mastery ladder), §6 (the simulations), §8 (R1–R19).

   Four jobs, and nothing else:

   Law 4 / R3 — predict before reveal. No stateful reveal is shown until
           the student has committed to a prediction, and an activity
           option NEVER marks correctness: it shows only that it was
           chosen. Only the ladder marks right and wrong.
   R4  — one tap flips one card. `aria-expanded` is the truth.
   R8  — write, then check, then mark. Four rungs, all four count, the
         score reads out of 4, and "Retry my misses" reopens a
         self-marked rung with the written answer kept.
   R18 / R19 — one model drives both simulation readings, and each
         simulation shows temperature in its own honest way.

   Never punish: no streaks, no guilt copy, no XP, no timers.
   ═══════════════════════════════════════════════════════════════ */
(function () {
  "use strict";

  /* ── storage ────────────────────────────────────────────────────
     Two keys per lesson, both introduced by MRB-184:

       ks3_ladder4_<slug>   the best score, OUT OF FOUR
       ks3_work_<slug>      the student's own writing + tick state

     The old `ks3_best_<slug>` key holds bests out of TWO. It is
     deliberately never read, never migrated and never compared against
     this scale: a 1-of-2 best measured against a 4-scale would tell a
     student they had got worse when they had not. It is left exactly
     where it is.

     Every access is wrapped: private mode must degrade to "works but
     does not save", never throw. */
  var BEST_PREFIX = "ks3_ladder4_";
  var WORK_PREFIX = "ks3_work_";

  function readStore(key) {
    try {
      var v = window.localStorage.getItem(key);
      return v === null ? null : JSON.parse(v);
    } catch (e) { return null; }          // private mode, or corrupt JSON
  }

  function writeStore(key, value) {
    try {
      window.localStorage.setItem(key, JSON.stringify(value));
    } catch (e) { /* private mode — the lesson works, it just doesn't save */ }
  }

  /* ── the drawn marks (SPEC §9.3) ────────────────────────────────
     ✓ and ✕ are NOT in the latin woff2 subsets Design shipped, so typed
     as characters they drop to a system font mid-badge. Both marks are
     inline SVG on currentColor instead. R2 makes them load-bearing —
     colour is never the only signal — so do NOT "simplify" these back
     to characters. */
  var TICK_SVG = '<svg class="ks3-mark" viewBox="0 0 24 24" aria-hidden="true">'
    + '<path d="M4 13l5 5L20 7"/></svg>';
  var CROSS_SVG = '<svg class="ks3-mark" viewBox="0 0 24 24" aria-hidden="true">'
    + '<path d="M6 6l12 12M18 6L6 18"/></svg>';

  function each(list, fn) { Array.prototype.forEach.call(list, fn); }
  function toArray(list) { return Array.prototype.slice.call(list); }

  /* ── injecting AUTHORED text (SPEC §9.3, second half) ───────────
     Authored copy uses → as chemistry notation ("Evaporation is
     liquid → gas"), and that content is science, not styling: it is
     never edited to suit a font. build_ks3.py draws all three marks
     wherever it emits TEXT, but it deliberately cannot do so inside an
     attribute value — the SVG carries double quotes, so substituting
     into `data-feedback="…"` would terminate the attribute and emit
     broken markup (see its own warning above MARKS). The correction
     strings therefore reach this file with the literal character still
     in them, and drawing them is this renderer's job.

     The paths are identical to build_ks3.py's MARK_ARROW / MARK_TICK /
     MARK_CROSS on purpose: one definition per mark, no drift.

     Because the SVG is aria-hidden, a spoken equivalent goes beside it.
     It is a visually-hidden SPAN rather than an aria-label on the
     paragraph: the feedback is a role="status" live region, and a live
     region is announced from its CONTENT, so a word in the content is
     the only version certain to be read out. ks3.css has no
     visually-hidden utility class, so the span is styled inline rather
     than inventing a class the stylesheet does not have. */
  var SR_CLIP = "position:absolute;width:1px;height:1px;padding:0;margin:-1px;"
    + "overflow:hidden;clip:rect(0,0,0,0);clip-path:inset(50%);"
    + "white-space:nowrap;border:0";
  var AUTHORED_MARKS = [
    ["→", '<svg class="ks3-mark ks3-mark-arrow" viewBox="0 0 24 24" '
      + 'aria-hidden="true"><path d="M4 12h15M13 6l6 6-6 6"/></svg>', "to"],
    ["✓", TICK_SVG, "tick"],
    ["✕", CROSS_SVG, "cross"]
  ];
  var MARK_RE = /[→✓✕]/;

  // Appends authored text to `parent` as text nodes, with any mark it
  // contains DRAWN between them. Never use textContent for authored text.
  function appendAuthored(parent, text) {
    var s = String(text);
    while (s.length) {
      var m = s.match(MARK_RE);
      if (!m) { parent.appendChild(document.createTextNode(s)); return; }
      if (m.index > 0) {
        parent.appendChild(document.createTextNode(s.slice(0, m.index)));
      }
      var ch = s.charAt(m.index), i, mark = null;
      for (i = 0; i < AUTHORED_MARKS.length; i++) {
        if (AUTHORED_MARKS[i][0] === ch) { mark = AUTHORED_MARKS[i]; }
      }
      if (mark) {
        // Both halves are constants defined above — no authored text is
        // ever passed through insertAdjacentHTML.
        parent.insertAdjacentHTML("beforeend",
          mark[1] + '<span style="' + SR_CLIP + '">' + mark[2] + "</span>");
      }
      s = s.slice(m.index + 1);
    }
  }

  /* ⚠️ `hidden` is the source of truth, and it is backed up with an
     inline display on purpose. ks3.css gives `.ks3-ticks` a
     `display: flex` and `.ks3-tally` a `display: inline-block`, and an
     AUTHOR display beats the UA stylesheet's `[hidden] { display: none }`
     regardless of specificity — the same trap `.ks3-card-back[hidden]`
     already documents in the stylesheet. R8 turns entirely on the
     criteria being genuinely unreadable before the button is pressed, so
     this cannot be left to trust. */
  function setHidden(el, on) {
    if (!el) { return; }
    if (on) {
      el.setAttribute("hidden", "");
      el.style.display = "none";
    } else {
      el.removeAttribute("hidden");
      el.style.display = "";
    }
  }

  /* ═══════════════════════════════════════════════════════════════
     Law 4 / R3 — a reveal is gated behind a committed prediction.

     R3 is the load-bearing half and the easiest to lose: an activity
     option shows that it was CHOSEN and nothing else. It never takes
     is-correct or is-wrong, and it never disables, because only the
     mastery ladder marks correctness. If activities started marking, the
     student would read the whole page as a test and committing before
     revealing would lose its point.
     ═══════════════════════════════════════════════════════════════ */
  function wirePredictions(root) {
    each(root.querySelectorAll("[data-activity]"), function (block) {
      var reveal = block.querySelector("[data-reveal]");
      var options = block.querySelectorAll(".ks3-option");
      if (!options.length) { return; }

      each(options, function (btn) {
        btn.setAttribute("aria-pressed", "false");
        btn.addEventListener("click", function () {
          each(options, function (b) { b.setAttribute("aria-pressed", "false"); });
          btn.setAttribute("aria-pressed", "true");
          if (reveal && reveal.hasAttribute("hidden")) {
            setHidden(reveal, false);
            // Announce the reveal for screen-reader users, who would
            // otherwise get no signal that new content appeared.
            reveal.setAttribute("role", "status");
          }
        });
      });
    });
  }

  /* ── the "Check your answer" disclosure on a check block ──
     Same principle as R8 on the ladder: a visible list of success
     criteria IS the answer, so it is not on the page until the student
     asks for it. */
  function wireCriteria(root) {
    each(root.querySelectorAll("[data-criteria-btn]"), function (btn) {
      var sib = btn.nextElementSibling;
      var wrap = null;
      if (sib && sib.hasAttribute && sib.hasAttribute("data-criteria")) {
        wrap = sib;
      } else {
        var scope = (btn.closest && btn.closest("[data-activity]")) || btn.parentNode;
        wrap = scope && scope.querySelector ? scope.querySelector("[data-criteria]") : null;
      }
      if (!wrap) { return; }

      btn.setAttribute("aria-expanded", "false");
      setHidden(wrap, true);
      btn.addEventListener("click", function () {
        var open = btn.getAttribute("aria-expanded") === "true";
        btn.setAttribute("aria-expanded", open ? "false" : "true");
        setHidden(wrap, open);
        btn.textContent = open ? "Check your answer" : "Hide the list";
      });
    });
  }

  /* ═══════════════════════════════════════════════════════════════
     R8 — the mastery ladder.  MRB-184's ruling of 9 August 2026.

     Four rungs. Two the page marks, two the student marks — and ALL
     FOUR COUNT. The score reads out of 4.

     What changed, and why the old behaviour was a defect: the ladder
     used to score only the button rungs and read "You got N of 2",
     which told a student that the two rungs where they did the actual
     explaining were worth nothing. The written rungs are the harder
     half of the ladder; they are now marked by the student against
     explicit criteria and counted the same as the others.

     The criteria are NOT on the page until "Check my answer" is
     pressed. That is the whole ruling: a visible checklist is the
     answer, so revealing it early would remove the reason to write.
     A partial tick is honest and is NEVER a failure — "2 of 4 ticked —
     not yet" takes the neutral band, never an error tone.
     ═══════════════════════════════════════════════════════════════ */
  function wireLadder(ladder) {
    var slug = ladder.getAttribute("data-lesson") || "lesson";
    var scoreEl = ladder.querySelector("[data-score]");
    var noteEl = ladder.querySelector("[data-score-note]");
    var rungs = [];                                  // scorable rungs, page order
    var work = readStore(WORK_PREFIX + slug) || {};
    var WHO = "";

    // The best is read ONCE, at load, and the score line is compared against
    // that snapshot rather than against a value this sitting keeps raising.
    // Otherwise a first-ever attempt announces "That's your best yet — up 1"
    // the moment the second rung lands, which is meaningless: there was no
    // earlier attempt to be up on. "Your best" means the best the student
    // walked in with.
    var stored = readStore(BEST_PREFIX + slug);
    var bestAtLoad = null;
    if (stored && typeof stored.got === "number") { bestAtLoad = stored.got; }
    else if (typeof stored === "number") { bestAtLoad = stored; }
    var bestSaved = bestAtLoad;

    /* ── "Retry my misses" ── */
    var retryWrap = document.createElement("div");
    retryWrap.className = "ks3-retry-wrap";
    var retry = document.createElement("button");
    retry.type = "button";
    retry.className = "ks3-retry";
    retry.textContent = "Retry my misses";
    var retryNote = document.createElement("p");
    retryNote.className = "ks3-retry-note";
    retryNote.textContent =
      "Reopens only the rungs you missed, and puts your cursor on the first one.";
    retryWrap.appendChild(retry);
    retryWrap.appendChild(retryNote);
    ladder.appendChild(retryWrap);
    setHidden(retryWrap, true);

    function saveWork() {
      var out = {};
      rungs.forEach(function (r) {
        if (r.mode !== "self") { return; }
        out[r.key] = {
          text: r.answer ? r.answer.value : "",
          ticks: r.boxes.map(function (b) { return b.checked ? 1 : 0; }),
          shown: r.shown ? 1 : 0
        };
      });
      writeStore(WORK_PREFIX + slug, out);
    }

    // "You marked rungs 3 and 4 yourself." — built from the rung numbers
    // actually present, so it stays true if a lesson ever puts the
    // self-marked rungs somewhere else.
    function whoMarked() {
      var nums = [];
      rungs.forEach(function (r, i) { if (r.mode === "self") { nums.push(i + 1); } });
      if (!nums.length) { return ""; }
      var list = nums.length === 1
        ? String(nums[0])
        : nums.slice(0, -1).join(", ") + " and " + nums[nums.length - 1];
      return "You marked rung" + (nums.length > 1 ? "s " : " ") + list + " yourself.";
    }

    function refresh() {
      var got = 0, resolved = 0, misses = 0, total = rungs.length;
      rungs.forEach(function (r) {
        if (r.resolved) { resolved += 1; }
        if (r.met) { got += 1; }
        // A miss: page-marked and answered wrongly, or self-marked, shown,
        // and not every criterion ticked.
        if (r.resolved && !r.met) { misses += 1; }
      });

      if (scoreEl) {
        scoreEl.textContent = resolved
          ? "You got " + got + " of " + total + "."
          : "Not started yet.";
      }
      if (noteEl) {
        var lead = "";
        if (resolved && bestAtLoad !== null) {
          if (got > bestAtLoad) {
            lead = "That's your best yet — up " + (got - bestAtLoad) + ". ";
          } else if (got < bestAtLoad) {
            lead = "Your best so far is " + bestAtLoad + " of " + total + ". ";
          }
        }
        noteEl.textContent = lead + WHO;
      }
      if (resolved && (bestSaved === null || got > bestSaved)) {
        bestSaved = got;
        writeStore(BEST_PREFIX + slug, { got: got, total: total });
      }
      setHidden(retryWrap, misses === 0);
    }

    /* ── rungs the page marks: one attempt, then locked ── */
    function wireMarked(rung, rec) {
      var options = toArray(rung.querySelectorAll(".ks3-option"));
      rec.options = options;
      // The resting letter badges (A/B/C/D), kept so a retry can put them
      // back exactly as authored.
      rec.badges = options.map(function (b) {
        var m = b.querySelector(".ks3-opt-mark");
        return m ? m.innerHTML : "";
      });

      // R2 — the feedback carries the WORD and a drawn mark, not just a
      // colour, so it survives being printed in greyscale.
      function feedback(correct, correction) {
        if (!rec.fb) {
          rec.fb = document.createElement("p");
          rec.fb.setAttribute("role", "status");
          rung.appendChild(rec.fb);
        }
        rec.fb.className = "ks3-feedback " + (correct ? "is-correct" : "is-wrong");
        rec.fb.innerHTML = '<span class="ks3-feedback-word">'
          + (correct ? TICK_SVG + " Correct." : CROSS_SVG + " Not quite.")
          + "</span>";
        // Law 10: the correction addresses THIS misconception, not a
        // generic "wrong, try again". It is AUTHORED text and may carry a
        // literal → , so it is appended mark-aware rather than as
        // textContent.
        if (!correct && correction) {
          appendAuthored(rec.fb, " " + correction);
        }
      }

      each(options, function (btn) {
        btn.addEventListener("click", function () {
          if (rec.resolved) { return; }
          rec.resolved = true;
          rung.setAttribute("data-locked", "1");
          var correct = btn.getAttribute("data-correct") === "1";
          rec.met = correct;

          each(options, function (b) {
            b.disabled = true;
            var mark = b.querySelector(".ks3-opt-mark");
            if (b.getAttribute("data-correct") === "1") {
              b.classList.add("is-correct");
              if (mark) { mark.innerHTML = TICK_SVG; }
            } else if (b === btn) {
              b.classList.add("is-wrong");
              if (mark) { mark.innerHTML = CROSS_SVG; }
            } else {
              b.classList.add("is-spent");     // untouched, and now spent
            }
          });
          feedback(correct, btn.getAttribute("data-feedback"));
          refresh();
        });
      });

      rec.reopen = function () {
        rung.removeAttribute("data-locked");
        rec.resolved = false;
        rec.met = false;
        options.forEach(function (b, i) {
          b.disabled = false;
          b.classList.remove("is-correct", "is-wrong", "is-spent");
          var mark = b.querySelector(".ks3-opt-mark");
          if (mark) { mark.innerHTML = rec.badges[i]; }
          if (b.hasAttribute("aria-pressed")) { b.setAttribute("aria-pressed", "false"); }
        });
        if (rec.fb) {
          rec.fb.parentNode.removeChild(rec.fb);
          rec.fb = null;
        }
      };
    }

    /* ── rungs the student marks: write, then check, then mark ── */
    function wireSelf(rung, rec) {
      var answer = rung.querySelector("[data-answer]");
      var checkBtn = rung.querySelector("[data-check]");
      var ticks = rung.querySelector("[data-ticks]");
      var tally = rung.querySelector("[data-tally]");
      var boxes = ticks ? toArray(ticks.querySelectorAll("[data-crit]")) : [];
      rec.answer = answer;
      rec.boxes = boxes;

      function tell() {
        var n = 0, all = boxes.length;
        boxes.forEach(function (b) { if (b.checked) { n += 1; } });
        rec.met = all > 0 && n === all;
        if (!tally) { return; }
        tally.textContent = rec.met
          ? "All " + all + " ticked — rung met."
          : n + " of " + all + " ticked — not yet";
        tally.className = "ks3-tally" + (rec.met ? " is-met" : "");
        if (rec.shown) { setHidden(tally, false); }
      }

      function show() {
        rec.shown = true;
        rec.resolved = true;
        setHidden(ticks, false);
        if (checkBtn) {
          checkBtn.setAttribute("aria-expanded", "true");
          checkBtn.textContent = "Hide the list";
        }
        tell();
      }

      // Folding the list away again is purely visual — the rung keeps
      // whatever it was marked.
      function collapse() {
        setHidden(ticks, true);
        setHidden(tally, true);
        if (checkBtn) {
          checkBtn.setAttribute("aria-expanded", "false");
          checkBtn.textContent = "Check my answer";
        }
      }

      if (checkBtn) {
        checkBtn.setAttribute("aria-expanded", "false");
        checkBtn.addEventListener("click", function () {
          if (checkBtn.getAttribute("aria-expanded") === "true") { collapse(); }
          else { show(); }
          saveWork();
          refresh();
        });
      }
      boxes.forEach(function (b) {
        b.addEventListener("change", function () { tell(); saveWork(); refresh(); });
      });
      if (answer) {
        answer.addEventListener("input", function () { saveWork(); });
      }

      rec.reopen = function () {
        rec.shown = false;
        rec.resolved = false;
        rec.met = false;
        boxes.forEach(function (b) { b.checked = false; });
        if (tally) { tally.textContent = ""; tally.className = "ks3-tally"; }
        collapse();
        // The WRITING stays. A retry on a self-marked rung is for
        // revising an answer, not for starting again from a blank box.
        saveWork();
      };

      // Restore this student's own work, so a returning student sees
      // their own writing rather than an empty box.
      var saved = work[rec.key];
      if (saved) {
        if (answer && typeof saved.text === "string") { answer.value = saved.text; }
        var anyTicked = false;
        if (saved.ticks && saved.ticks.length) {
          boxes.forEach(function (b, i) {
            b.checked = !!saved.ticks[i];
            if (b.checked) { anyTicked = true; }
          });
        }
        // Already-seen criteria are not a leak; hiding a ticked box would
        // be a lie about the state.
        if (saved.shown || anyTicked) { show(); } else { collapse(); }
      } else {
        collapse();
      }
    }

    each(ladder.querySelectorAll(".ks3-rung"), function (rung) {
      var mode = rung.getAttribute("data-mode");
      var hasTicks = !!rung.querySelector("[data-ticks]");
      var hasOptions = rung.querySelectorAll(".ks3-option").length > 0;
      var self = mode === "self" || (!mode && hasTicks);
      var rec = {
        key: rung.getAttribute("data-rung") || ("rung" + (rungs.length + 1)),
        el: rung,
        mode: self ? "self" : "marked",
        resolved: false,
        met: false,
        shown: false,
        options: [],
        boxes: [],
        fb: null
      };
      // A rung with nothing to score is not counted in the total, so the
      // score can never read out of more than the student can answer.
      if (self && hasTicks) {
        rungs.push(rec);
        wireSelf(rung, rec);
      } else if (!self && hasOptions) {
        rungs.push(rec);
        wireMarked(rung, rec);
      }
    });

    retry.addEventListener("click", function () {
      var first = null;
      rungs.forEach(function (r) {
        if (!(r.resolved && !r.met)) { return; }
        if (r.reopen) { r.reopen(); }
        if (!first) { first = r.el; }
      });
      refresh();
      if (first) {
        var h = first.querySelector("h3");
        if (h && h.focus) { h.focus(); }
      }
    });

    WHO = whoMarked();
    refresh();
  }

  /* ═══════════════════════════════════════════════════════════════
     Flip cards / click-to-reveal.  R4.

     A card is a <button>, not a div with a click handler, so keyboard
     and screen-reader users get it for free. `aria-expanded` carries the
     state and `.is-flipped` is only its visual consequence. One tap
     flips one card: no hover reveal, no auto flip. The dog-ear is the
     only affordance and CSS removes it when the card opens, because
     there is no longer anything underneath.
     ═══════════════════════════════════════════════════════════════ */
  function wireCards(root) {
    each(root.querySelectorAll(".ks3-card-btn"), function (btn) {
      var back = btn.querySelector(".ks3-card-back");
      btn.setAttribute("aria-expanded", "false");
      btn.addEventListener("click", function () {
        var open = btn.getAttribute("aria-expanded") === "true";
        btn.setAttribute("aria-expanded", open ? "false" : "true");
        btn.classList.toggle("is-flipped", !open);
        setHidden(back, open);
      });
    });
  }

  /* ═══════════════════════════════════════════════════════════════
     Particle labs.  R5, R6, R15, R18, R19.

     Three sims, one engine. Each is a box of particles on a canvas;
     what differs is what the particles do and what is measured.

       particle-states — arrangement and motion across solid/liquid/gas
       gas-pressure    — pressure, and the wall pushes that make it
       diffusion       — two populations random-walking into each other

     THE POINT OF EACH, so nobody "tidies" the physics away:

     * particle-states must show particles VIBRATING in the solid, never
       frozen. PART-04 is "particles in a solid are completely still",
       and a still solid teaches the misconception the lesson exists to
       kill.
     * gas-pressure must show pressure as wall pushes. PART-08 is
       "pressure is particles pushing each other". If the readout were
       just a number that goes up, the sim has not confronted anything.
     * diffusion must show movement in BOTH directions. PART-11 is that
       particles "want" to spread out. Watching orange cross right while
       blue crosses left is what makes randomness visible; a one-way
       spreading animation would confirm the misconception instead.

     R5 — the sim will not run until the student has committed to a
     prediction. It renders one frozen frame behind a blurred veil, with
     the caption still readable because the caption holds the
     instructions for the prediction.

     R6 — reduced motion is a COMPLETE experience: no animation loop at
     all, 1,400 settling steps, one representative frame, and a written
     readout that carries the entire result. Every control change
     re-settles from scratch.
     ═══════════════════════════════════════════════════════════════ */

  var REDUCED = window.matchMedia
    && window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  // The controls a lab can ask for. build_ks3.py validates authored
  // `sim.controls` against the same closed list (SIM_CONTROLS) and FAILS
  // THE BUILD on anything else, so a lesson can never ship a control
  // panel that silently does nothing — which is what happened when the
  // content authored `state`, `medium`, `release` and `number of
  // particles` against a JS that implemented only two of them.
  var CONTROL_LABELS = {
    temperature: "Temperature",
    volume:      "Space to move in",
    particles:   "How many particles",
    medium:      "What it spreads through",
    // MRB-198 — the microscope's three, and system-parts' one.
    specimen:      "Slide on the stage",
    magnification: "Magnification",
    focus:         "Focus",
    part:          "Switch one part off"
  };

  // SPEC §6 populations.
  var SIM_POP = { "particle-states": 64, "gas-pressure": 90, "diffusion": 120 };

  // R18's reference population: 100% on the `particles` slider is 90 dots.
  var REF_DOTS = 90;
  var PCT_MIN = 10, PCT_MAX = 200;

  // 1 kPa = 1000 Pa = 1000 N/m². N/m² is the KS3 statutory phrasing and
  // is offered so force-per-area stays visible.
  var UNITS = [["kPa", 1], ["Pa", 1000], ["N/m²", 1000]];

  var UID = 0;

  function cssVar(el, name, fallback) {
    try {
      var v = getComputedStyle(el).getPropertyValue(name);
      return (v && v.trim()) || fallback;
    } catch (e) { return fallback; }
  }

  function rand(a, b) { return a + Math.random() * (b - a); }

  // "1 orange particles" is the kind of thing a Year 7 notices and an
  // adult reads straight past. The readout is student-facing text, so it
  // agrees.
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

  /* ── the R5 / Law 4 / R6 power scaffold, shared by every sim kind ──
     Extracted unchanged from the particle engine when MRB-198 added two
     non-particle kinds: the LOCKING is the same law for all of them, and
     two copies of it is how one copy quietly stops gating. hooks:
       draw()   — paint one frame at the current state (the frozen frame
                  behind the veil)
       settle() — R6: compute the settled state for the CURRENT controls,
                  draw one representative frame, write the full readout
       start()  — begin animating (never called under REDUCED)
       stop()   — halt animating                                          */
  function wireGate(sim, hooks) {
    var activity = sim.closest ? sim.closest("[data-activity]") : null;
    var gated = activity && activity.querySelectorAll(".ks3-option").length > 0;

    function unlock() {
      sim.removeAttribute("data-locked");
      if (REDUCED) {
        // One representative frame, then the words. Nothing is
        // motion-only, so this is a complete experience, not a stub.
        hooks.settle();
      } else {
        hooks.start();
      }
    }

    if (gated) {
      sim.setAttribute("data-locked", "1");
      each(activity.querySelectorAll(".ks3-option"), function (btn) {
        btn.addEventListener("click", unlock);
      });
      hooks.draw();   // the frozen first frame behind the veil
    } else {
      unlock();
    }

    // Don't burn a phone battery animating a lab three screens away.
    if (window.IntersectionObserver && !REDUCED) {
      new window.IntersectionObserver(function (entries) {
        entries.forEach(function (en) {
          if (sim.getAttribute("data-locked") === "1") { return; }
          if (en.isIntersecting) { hooks.start(); } else { hooks.stop(); }
        });
      }, { threshold: 0.05 }).observe(sim);
    }
    document.addEventListener("visibilitychange", function () {
      if (document.hidden) { hooks.stop(); }
      else if (sim.getAttribute("data-locked") !== "1") { hooks.start(); }
    });
  }

  // R15 — one control shell for every engine: a real <label> with a real
  // for=, wrapping the visible label text. The input goes in after.
  // Returns null when CONTROL_LABELS has no entry: a control labelled
  // "undefined" is the empty-control-panel defect in a new costume, and
  // refusing here is what lets the parity sim audit count the drift
  // (declared vs rendered) instead of shipping it.
  function controlShell(name) {
    if (!CONTROL_LABELS.hasOwnProperty(name)) { return null; }
    var id = "ks3-sim-" + name + "-" + (++UID);
    var wrap = document.createElement("label");
    wrap.className = "ks3-sim-control";
    wrap.setAttribute("for", id);
    wrap.appendChild(document.createTextNode(CONTROL_LABELS[name]));
    return { wrap: wrap, id: id };
  }

  // MRB-210 §2 — one place that knows how a range control is bound.
  // A range fires `input` on every movement and `change` when the value
  // settles; which of the two arrives depends on the input path, not on
  // the element. Design's approved B1-06 binds both to the same handler
  // and so do we. Bound twice, the handler can run twice for one drag,
  // which is why every handler behind this is idempotent — it reads
  // `input.value` and recomputes, rather than stepping a counter.
  function onRange(el, fn) {
    el.addEventListener("input", fn);
    el.addEventListener("change", fn);
  }

  function wireSim(sim) {
    // MRB-198 — dispatch. The two B1 instruments are not particle labs:
    // they share the gate scaffold and the readout discipline, nothing else.
    var simKind = sim.getAttribute("data-sim");
    if (simKind === "microscope") { return wireMicroscope(sim); }
    if (simKind === "system-parts") { return wireSystemParts(sim); }

    var canvas = sim.querySelector(".ks3-sim-canvas");
    if (!canvas || !canvas.getContext) { return; }
    var ctx = canvas.getContext("2d");
    var kind = sim.getAttribute("data-sim");
    var W = canvas.width, H = canvas.height;

    var ink = cssVar(sim, "--ks3-ink", "#221E1B");
    var accent = cssVar(sim, "--ks3-accent", "#E4572E");
    var blue = cssVar(sim, "--ks3-blue", "#2F5CE0");
    var ruleStrong = cssVar(sim, "--ks3-rule-strong", "#C3B191");

    // Controls are parsed first: whether the lab has a `particles` slider
    // decides how many particles have to be allocated (the slider runs to
    // 200% of the reference population).
    var wanted = [];
    (sim.getAttribute("data-controls") || "").split(",").forEach(function (name) {
      name = name.trim();
      if (CONTROL_LABELS.hasOwnProperty(name) && wanted.indexOf(name) < 0) {
        wanted.push(name);
      }
    });
    var hasParticles = wanted.indexOf("particles") >= 0;
    var pop = SIM_POP[kind] || REF_DOTS;
    if (hasParticles) { pop = Math.round(REF_DOTS * PCT_MAX / 100); }

    var state = {
      temp: 50,          // slider 0-100. What it MEANS differs by kind (R19)
      space: 100,        // 30-100, the right wall as a % of the box width
      pct: 100,          // 10-200, a % of R18's reference population
      medium: "gas",     // gas | liquid — diffusion is far slower in a liquid
      units: "kPa",
      running: false,
      lastSay: 0,
      // particle-states uses fewer, larger particles so a tight lattice
      // reads as a lump of touching particles rather than a dusting.
      particles: makeParticles(pop, W, H,
        { lattice: kind === "particle-states", spacing: 16 })
    };
    var dotR = kind === "particle-states" ? 7 : 4.4;

    /* ── R18: ONE model drives BOTH readings ──────────────────────
         kelvin              = 100 + (slider / 100) * 400      (100 K … 500 K)
         factor              = (particles / 100) * (kelvin / 300) * (100 / space)
         pressure in kPa     = 100 * factor
         wall hits per second = factor * 60

       Both figures come from the same `factor`, so they cannot drift
       apart. The wall-hit figure is NOT counted from the animation:
       counting it is exactly how the two readings used to disagree, and
       R18 forbids it. There is deliberately no hit counter anywhere in
       this file — if you add one, you have reintroduced the defect. */
    function kelvin() {
      // R19 — the slider means something different in each lab.
      // diffusion's slider IS degrees Celsius (0-100), the range a real
      // school experiment spans, so its absolute temperature is 273.15 K
      // higher. The other two run 100 K to 500 K, and 50 is exactly 300 K.
      if (kind === "diffusion") { return state.temp + 273.15; }
      return 100 + (state.temp / 100) * 400;
    }
    function factor() {
      return (state.pct / 100) * (kelvin() / 300) * (100 / state.space);
    }
    function pressureKPa() { return 100 * factor(); }
    function wallHitsPerSec() { return factor() * 60; }

    // R19 — gas-pressure shows °C COMPUTED FROM KELVIN (−173 / 27 / 227 at
    // the three anchor points), never the raw slider value, and the
    // pressure scaling is never done in Celsius: that is the classic error
    // this rule exists to prevent. diffusion's slider is already °C.
    function celsius() {
      if (kind === "diffusion") { return Math.round(state.temp); }
      return Math.round(kelvin() - 273.15);
    }

    // Root-mean-square speed goes as √T, so speed is driven from ABSOLUTE
    // temperature. Do NOT "simplify" this to state.temp: for gas-pressure
    // the slider is not proportional to T, and what is on screen would
    // then disagree with the pressure figure beside it.
    var BASE_SPEED = 1.6;
    function speed() { return BASE_SPEED * Math.sqrt(kelvin() / 300); }

    // The `particles` slider is a PERCENTAGE of the reference population,
    // not a raw count: 100% is 90 dots.
    function dotCount() {
      var n = Math.round(REF_DOTS * state.pct / 100);
      if (n < 10) { n = 10; }
      if (n > state.particles.length) { n = state.particles.length; }
      return n;
    }

    // Only the dots in play are stepped, drawn and counted. Slicing rather
    // than hiding keeps step(), draw() and the diffusion count reading the
    // same population — a readout counting particles that are not on
    // screen is worse than no readout.
    function inPlay() {
      return hasParticles ? state.particles.slice(0, dotCount()) : state.particles;
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

    function step() {
      var wallX = kind === "gas-pressure" ? W * (state.space / 100) : W;
      var v = speed();
      var t = state.temp;

      // A liquid is crowded: a particle gets nowhere before it hits a
      // neighbour. Slower travel plus far more frequent scattering is what
      // makes diffusion visibly slower in a liquid than in a gas, which is
      // the point the `medium` control exists to make.
      var scatter = 0.04;
      if (state.medium === "liquid") { v *= 0.35; scatter = 0.16; }

      inPlay().forEach(function (p) {
        if (kind === "particle-states" && t < 66) {
          // Solid and liquid: a spring back to the lattice home. Strong
          // when cold (vibration on the spot), weak when warm (particles
          // slide past each other but stay touching). This branch models
          // vibration AMPLITUDE, which is why it reads the slider band
          // rather than the speed above.
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
          p.vx = (p.vx / m) * v;
          p.vy = (p.vy / m) * v;
        }
        p.x += p.vx; p.y += p.vy;

        // Walls. Each bounce off a wall is one push — which is the whole of
        // what pressure is in this model. It is SHOWN, not counted: the
        // figure beside it comes from the same model that positions these
        // particles (R18).
        if (p.x < 4) { p.x = 4; p.vx = -p.vx; }
        if (p.x > wallX - 4) { p.x = wallX - 4; p.vx = -p.vx; }
        if (p.y < 4) { p.y = 4; p.vy = -p.vy; }
        if (p.y > H - 4) { p.y = H - 4; p.vy = -p.vy; }
      });
    }

    function draw() {
      var wallX = kind === "gas-pressure" ? W * (state.space / 100) : W;
      ctx.clearRect(0, 0, W, H);

      if (kind === "gas-pressure" && wallX < W - 1) {
        ctx.fillStyle = ruleStrong;
        ctx.fillRect(wallX, 0, W - wallX, H);
        ctx.fillStyle = ink;
        ctx.fillRect(wallX - 2, 0, 3, H);
      }
      if (kind === "diffusion") {
        // SPEC §6 — the centre line is where "crossed over" is measured,
        // so it has to be visible.
        ctx.save();
        ctx.strokeStyle = ruleStrong;
        ctx.lineWidth = 2;
        if (ctx.setLineDash) { ctx.setLineDash([6, 6]); }
        ctx.beginPath();
        ctx.moveTo(W / 2, 0);
        ctx.lineTo(W / 2, H);
        ctx.stroke();
        ctx.restore();
      }
      inPlay().forEach(function (p) {
        var colour = accent;
        if (kind === "diffusion" && p.team === 1) { colour = blue; }
        drawDot(ctx, p, dotR, colour);
      });
    }

    /* ── the readout ──
       Built once and then updated in place. Rebuilding it would destroy
       the units <select> mid-interaction, taking the student's focus and
       their chosen unit with it. */
    var readout = sim.querySelector(".ks3-sim-readout");
    var figureEl = null, unitsSel = null, sentenceEl = null;
    if (readout) {
      if (kind === "gas-pressure") {
        figureEl = document.createElement("span");
        figureEl.className = "ks3-sim-figure";
        unitsSel = document.createElement("select");
        unitsSel.className = "ks3-sim-units";
        unitsSel.setAttribute("aria-label", "Pressure units");
        UNITS.forEach(function (u) {
          var opt = document.createElement("option");
          opt.value = u[0];
          opt.textContent = u[0];
          unitsSel.appendChild(opt);
        });
        unitsSel.value = "kPa";
        unitsSel.addEventListener("change", function () {
          state.units = unitsSel.value;
          report();
        });
        readout.appendChild(figureEl);
        readout.appendChild(document.createTextNode(" "));
        readout.appendChild(unitsSel);
        readout.appendChild(document.createTextNode(" "));
      }
      sentenceEl = document.createElement("span");
      readout.appendChild(sentenceEl);
    }

    function say(txt) { if (sentenceEl) { sentenceEl.textContent = txt; } }

    function report() {
      if (kind === "gas-pressure") {
        var mult = 1;
        UNITS.forEach(function (u) { if (u[0] === state.units) { mult = u[1]; } });
        if (figureEl) {
          figureEl.textContent = String(Math.round(pressureKPa() * mult));
        }
        say("Wall hits per second: " + Math.round(wallHitsPerSec())
            + ". Every hit is one push — that IS the pressure. The gas is at "
            + celsius() + " °C.");
      } else if (kind === "particle-states") {
        say(stateName(state.temp) + " — "
            + (state.temp < 33
               ? "particles are touching, in a regular pattern, and vibrating on the spot."
               : state.temp < 66
                 ? "particles are still touching, but jumbled and sliding past each other."
                 : "particles are far apart and moving freely in every direction."));
      } else if (kind === "diffusion") {
        var mid = W / 2, rightOrange = 0, leftBlue = 0;
        inPlay().forEach(function (p) {
          if (p.team === 0 && p.x > mid) { rightOrange++; }
          if (p.team === 1 && p.x < mid) { leftBlue++; }
        });
        say("At " + celsius() + " °C: "
            + plural(rightOrange, "orange particle") + " crossed to the right, and "
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
      for (var i = 0; i < SETTLE_STEPS; i++) { step(); }
      draw();
      report();
    }

    // The written readout only changes with the controls for two of the
    // three labs (R18 locks both gas figures to the sliders). Diffusion's
    // crossing counts change as the walk proceeds, so that one — and only
    // that one — is re-read on a cadence.
    function sample(now) {
      if (!state.lastSay) { state.lastSay = now; return; }
      if (now - state.lastSay < 500) { return; }
      state.lastSay = now;
      report();
    }

    var raf = null;
    function loop(now) {
      if (!state.running) { return; }
      step();
      draw();
      if (kind === "diffusion") { sample(now || 0); }
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

    /* ── controls, built from data-controls so the markup stays
       declarative. R15: every one is a real control with a real label. */
    var controls = sim.querySelector(".ks3-sim-controls");
    var valueEls = {};
    var bandEls = [];

    function valueText(name) {
      if (name === "temperature") { return celsius() + " °C"; }
      if (name === "volume") { return state.space + "%"; }
      if (name === "particles") { return dotCount() + " particles"; }
      return "";
    }

    function syncControls() {
      Object.keys(valueEls).forEach(function (name) {
        valueEls[name].textContent = valueText(name);
      });
      if (bandEls.length) {
        var band = state.temp < 33 ? 0 : (state.temp < 66 ? 1 : 2);
        bandEls.forEach(function (el, i) {
          if (i === band) { el.classList.add("is-on"); }
          else { el.classList.remove("is-on"); }
        });
      }
    }

    function afterControlChange() {
      syncControls();
      if (sim.getAttribute("data-locked") === "1") { return; }
      if (REDUCED) {
        settle();                       // R6 — re-settle from scratch
      } else {
        if (!state.running) { draw(); }
        report();                       // the figures track the slider at once
      }
    }

    if (controls) {
      wanted.forEach(function (name) {
        var id = "ks3-sim-" + name + "-" + (++UID);
        var wrap = document.createElement("label");
        wrap.className = "ks3-sim-control";
        wrap.setAttribute("for", id);   // a real for=, not just wrapping
        wrap.appendChild(document.createTextNode(CONTROL_LABELS[name]));

        // `medium` is a two-way choice, not a quantity, so it gets a select
        // rather than a slider with two meaningful stops.
        if (name === "medium") {
          var sel = document.createElement("select");
          sel.id = id;
          [["gas", "In a gas"], ["liquid", "In a liquid"]].forEach(function (o) {
            var opt = document.createElement("option");
            opt.value = o[0];
            opt.textContent = o[1];
            sel.appendChild(opt);
          });
          sel.addEventListener("change", function () {
            state.medium = sel.value;
            afterControlChange();
          });
          wrap.appendChild(sel);
          controls.appendChild(wrap);
          return;
        }

        var input = document.createElement("input");
        input.type = "range";
        input.id = id;
        if (name === "volume") {
          input.min = "30"; input.max = "100"; input.value = "100";
        } else if (name === "particles") {
          input.min = String(PCT_MIN); input.max = String(PCT_MAX); input.value = "100";
        } else {
          input.min = "0"; input.max = "100"; input.value = "50";
        }
        onRange(input, function () {
          if (name === "temperature") {
            state.temp = Number(input.value);
          } else if (name === "particles") {
            state.pct = Number(input.value);
          } else {
            state.space = Number(input.value);
            // Pull anything the moving wall just swallowed back inside. The
            // running loop would fix this on its next step, but reduced
            // motion has no next step and would paint particles sitting in
            // the solid block of the piston.
            var wallX = W * (state.space / 100);
            state.particles.forEach(function (p) {
              if (p.x > wallX - 4) { p.x = wallX - 4; }
            });
          }
          afterControlChange();
        });
        wrap.appendChild(input);

        // R19 — particle-states shows NO temperature number anywhere:
        // a Celsius reading would imply a melting and a boiling point for
        // a model that names no substance. It gets a solid / liquid / gas
        // band strip instead, so the changes are findable by dragging.
        if (name === "temperature" && kind === "particle-states") {
          var strip = document.createElement("div");
          strip.className = "ks3-sim-bands";
          ["Solid", "Liquid", "Gas"].forEach(function (word) {
            var b = document.createElement("span");
            b.className = "ks3-sim-band";
            b.textContent = word;
            strip.appendChild(b);
            bandEls.push(b);
          });
          wrap.appendChild(strip);
        } else {
          var val = document.createElement("span");
          val.className = "ks3-sim-value";
          valueEls[name] = val;
          wrap.appendChild(val);
        }
        controls.appendChild(wrap);
      });
    }
    syncControls();
    report();          // never leave the readout empty, even while locked

    /* ── R5: locked until a prediction is committed ── */
    wireGate(sim, { draw: draw, settle: settle, start: start, stop: stop });
  }

  /* ═══════════════════════════════════════════════════════════════
     MRB-198 · THE MICROSCOPE — B1's L2 flagship, re-used in L6.

     ONE MODEL DRIVES EVERY READING (R18's discipline, carried over):

       total magnification = ×10 eyepiece × objective (×4 / ×10 / ×40)
       field of view (mm)  = 180 / magnification
                             ×40 → 4.5 mm · ×100 → 1.8 mm · ×400 → 0.45 mm
       pixels per mm       = field diameter in px / field of view
       depth of field      = 2200 / magnification  (55 · 22 · 5.5)
       layer sharpness     = 1 − |focal plane − layer depth| / depth of field

     The mm figure, the drawn size of every cell, the count of cells
     across the view and the blur are ALL computed from those five
     lines. No figure in the readout is invented (the review pack's
     1.8 mm ÷ 6 onion cells falls straight out: 1.8 / 0.30).

     THE POINT, so nobody "tidies" the physics away: turning the
     magnification up must do all three of (a) make everything larger,
     (b) SHRINK the field of view, (c) throw the image OUT OF FOCUS
     until the focus is corrected. (b) is fov = 180/mag. (c) is the
     depth of field narrowing PLUS the objectives not being parfocal —
     OBJ_FOCUS_SHIFT racks the focal plane further down at each step
     up, exactly like the school microscopes these students use. A
     version that only scales the drawing is decoration, and it is the
     version L2 exists to beat: CELL-02 is "the highest magnification
     is always the best one".

     Focus racks through the DEPTH of the slide (0–100), so a thick
     specimen — pond water above all — can never be sharp all at once:
     different layers come sharp in turn. Law 9: the magnification
     change is a real zoom transition, never a frame swap; reduced
     motion gets the settled frame and the full written readout.
     ═══════════════════════════════════════════════════════════════ */

  var EYEPIECE = 10;
  var OBJECTIVES = [4, 10, 40];
  var OBJ_FOCUS_SHIFT = [0, 10, 22];
  var FIELD_AT_1X_MM = 180;

  // The SAME classification rule as _specimen_kind() in build_ks3.py.
  // The build fails on a name neither side knows; the parity gate's sim
  // audit checks the rendered result, so the two cannot drift silently.
  function specimenKind(name) {
    var n = String(name).toLowerCase();
    if (n.indexOf("pond") >= 0) { return "pond"; }
    if (n.indexOf("cheek") >= 0) { return "cheek"; }
    if (n.indexOf("onion") >= 0) {
      return (n.indexOf("dropped") >= 0 || n.indexOf("bubble") >= 0)
        ? "bubbles" : "onion";
    }
    return null;
  }

  function wireMicroscope(sim) {
    var canvas = sim.querySelector(".ks3-sim-canvas");
    if (!canvas || !canvas.getContext) { return; }
    var ctx = canvas.getContext("2d");
    var W = canvas.width, H = canvas.height;

    var ink = cssVar(sim, "--ks3-ink", "#221E1B");
    var card = cssVar(sim, "--ks3-card", "#FFFCF5");
    var band = cssVar(sim, "--ks3-band", "#F4E9D8");
    var accent = cssVar(sim, "--ks3-accent", "#E4572E");
    var muted = cssVar(sim, "--ks3-ink-muted", "#5F564F");
    // Subject identity, not a correctness mark: chloroplasts and the
    // Euglena are GREEN because biology's hue is, and R3 is untouched —
    // nothing here marks an answer.
    var bio = cssVar(sim, "--ks3-biology", "#12A150");

    var specimens;
    try {
      specimens = JSON.parse(sim.getAttribute("data-specimens") || "[]");
    } catch (err) { specimens = []; }
    if (!specimens.length) { return; }

    var FIELD_R = 96, CX = W / 2, CY = H / 2;
    var CELL_W = 0.30, CELL_H = 0.13;   // an onion cell, mm (≈0.3 across)
    var CHEEK_D = 0.06;                 // a cheek cell, mm

    // Slide content is generated once per slide, in mm about the field
    // centre, so racking the controls looks at the SAME slide.
    function buildContent(kindName) {
      var i, out;
      if (kindName === "bubbles") {
        out = [];
        for (i = 0; i < 7; i++) {
          out.push({ x: rand(-2.2, 2.2), y: rand(-1.2, 1.2),
                     d: rand(0.35, 0.95) });
        }
        return { bubbles: out };
      }
      if (kindName === "cheek") {
        out = [];
        for (i = 0; i < 26; i++) {
          out.push({ x: rand(-2.6, 2.6), y: rand(-1.4, 1.4),
                     d: rand(0.052, 0.07), depth: rand(22, 48),
                     wob: rand(0, Math.PI * 2) });
        }
        return { cells: out };
      }
      if (kindName === "pond") {
        // Three whole organisms (L6's cast), at three DEPTHS — the wet
        // mount is thick, which is why ×400 can never sharpen all three.
        return { swimmers: [
          { type: "paramecium", x: -0.5, y: 0.15, depth: 16,
            speed: 0.55, hdg: rand(0, Math.PI * 2), phase: 0 },
          { type: "euglena", x: 0.55, y: -0.3, depth: 38,
            speed: 0.12, hdg: rand(0, Math.PI * 2), phase: 0 },
          { type: "amoeba", x: 0.1, y: 0.55, depth: 62,
            speed: 0.02, hdg: rand(0, Math.PI * 2), phase: rand(0, 9) }
        ] };
      }
      return {};   // onion tiles procedurally; nothing to pre-place
    }

    var state = {
      slide: 0,                     // index into specimens[]
      obj: 0,                       // index into OBJECTIVES — start LOWEST
      // Sharp on the onion layer (depth 30) at the lowest lens, on
      // purpose: the lesson only works if the opening view is GOOD and
      // turning the magnification up is what breaks it. Opening soft
      // would make the readout's "packed in rows like bricks" a claim
      // the picture does not honour, and would blunt the whole point.
      focus: 30,
      dispMag: EYEPIECE * OBJECTIVES[0],   // what the canvas shows NOW
      running: false, dirty: true, lastSay: 0, last: 0,
      content: null
    };
    state.content = buildContent(specimenKind(specimens[0]));

    function mag() { return EYEPIECE * OBJECTIVES[state.obj]; }
    function fovMM() { return FIELD_AT_1X_MM / mag(); }
    function focal() { return state.focus + OBJ_FOCUS_SHIFT[state.obj]; }
    function dof() { return 2200 / mag(); }
    function sharpOf(depth) {
      var s = 1 - Math.abs(focal() - depth) / dof();
      return s < 0 ? 0 : s;
    }

    // Law 9 — while the zoom transition runs, the CANVAS derives its
    // depth of field and focal shift from the magnification currently
    // displayed, interpolating the objective shift on the same log
    // scale the zoom sweeps. The image therefore slides out of focus
    // AS it grows, one continuous movement — never sharp, snap, blurred.
    // The readout keeps the settled model's figures (they are what the
    // student records), so nothing written ever shows a mid-zoom value.
    function viewSharp(depth) {
      var m = state.dispMag;
      var lo = EYEPIECE * OBJECTIVES[0];
      var hi = EYEPIECE * OBJECTIVES[OBJECTIVES.length - 1];
      var pos = Math.log(m / lo) / Math.log(hi / lo)
                * (OBJECTIVES.length - 1);
      if (pos < 0) { pos = 0; }
      if (pos > OBJECTIVES.length - 1) { pos = OBJECTIVES.length - 1; }
      var i = Math.floor(pos), f = pos - i;
      var shift = OBJ_FOCUS_SHIFT[i]
        + (OBJ_FOCUS_SHIFT[Math.min(i + 1, OBJ_FOCUS_SHIFT.length - 1)]
           - OBJ_FOCUS_SHIFT[i]) * f;
      var s = 1 - Math.abs((state.focus + shift) - depth) / (2200 / m);
      return s < 0 ? 0 : s;
    }
    function fovText() {
      var f = fovMM();
      return (f >= 1 ? String(Math.round(f * 10) / 10) : f.toFixed(2)) + " mm";
    }
    function kindNow() { return specimenKind(specimens[state.slide]); }

    // ── drawing ──
    var canFilter = typeof ctx.filter === "string";

    function blurFor(sharp) { return Math.min(8, (1 - sharp) * 7); }

    function layer(sharp, paint) {
      // A blurred layer is DRAWN blurred — the mechanism has to be
      // visible, not narrated only. Where canvas filters are missing
      // (very old WebKit) the layer fades instead: less honest about
      // optics, still unmistakably "not sharp".
      ctx.save();
      if (sharp < 0.92) {
        if (canFilter) { ctx.filter = "blur(" + blurFor(sharp).toFixed(1) + "px)"; }
        else { ctx.globalAlpha = 0.25 + 0.75 * sharp; }
      }
      paint();
      ctx.restore();
    }

    function mmFont(px, weight) {
      ctx.font = (weight || 400) + " " + px + "px 'Instrument Sans', system-ui, sans-serif";
    }

    function drawOnionLayer(ppm, sharp, dim) {
      var w = CELL_W * ppm, h = CELL_H * ppm;
      layer(sharp, function () {
        var r, c, x, y, row = 0;
        ctx.lineWidth = Math.max(1.2, 0.012 * ppm);
        ctx.strokeStyle = ink;
        ctx.fillStyle = card;
        if (dim) { ctx.globalAlpha *= 0.8; }
        for (r = -Math.ceil(FIELD_R / h) - 1; r * h < FIELD_R + h; r++) {
          row = r;
          for (c = -Math.ceil(FIELD_R / w) - 1; c * w < FIELD_R + w; c++) {
            x = CX + c * w + ((row % 2) ? w / 2 : 0);
            y = CY + r * h;
            ctx.fillRect(x, y, w - 1, h - 1);
            ctx.strokeRect(x, y, w - 1, h - 1);
            if (w > 22) {
              // The nucleus resolves once a cell is drawn large enough.
              ctx.beginPath();
              ctx.arc(x + w * (0.28 + 0.4 * (((r * 7 + c * 13) % 5) / 5)),
                      y + h / 2, Math.max(1.6, 0.014 * ppm), 0, Math.PI * 2);
              ctx.fillStyle = muted;
              ctx.fill();
              ctx.fillStyle = card;
            }
          }
        }
      });
    }

    function drawBubbles(ppm) {
      var sb = viewSharp(12), sc = viewSharp(38);
      drawOnionLayer(ppm, sc, true);
      layer(sb, function () {
        state.content.bubbles.forEach(function (b) {
          var x = CX + b.x * ppm, y = CY + b.y * ppm, r = (b.d / 2) * ppm;
          ctx.beginPath();
          ctx.arc(x, y, r, 0, Math.PI * 2);
          ctx.fillStyle = band;
          ctx.globalAlpha *= 0.92;
          ctx.fill();
          ctx.globalAlpha /= 0.92;
          // The thick dark rim is the tell (CELL-01's confrontation).
          ctx.lineWidth = Math.max(3, 0.05 * ppm);
          ctx.strokeStyle = ink;
          ctx.stroke();
        });
      });
    }

    function drawCheek(ppm) {
      state.content.cells.forEach(function (cell) {
        layer(viewSharp(cell.depth), function () {
          var x = CX + cell.x * ppm, y = CY + cell.y * ppm;
          var r = (cell.d / 2) * ppm, k;
          ctx.beginPath();
          for (k = 0; k <= 10; k++) {
            var a = cell.wob + (k / 10) * Math.PI * 2;
            var rr = r * (0.85 + 0.15 * Math.sin(a * 3 + cell.wob));
            if (k === 0) { ctx.moveTo(x + rr * Math.cos(a), y + rr * Math.sin(a)); }
            else { ctx.lineTo(x + rr * Math.cos(a), y + rr * Math.sin(a)); }
          }
          ctx.closePath();
          ctx.fillStyle = card;
          ctx.fill();
          ctx.lineWidth = Math.max(1, 0.008 * ppm);
          ctx.strokeStyle = muted;
          ctx.stroke();
          ctx.beginPath();
          ctx.arc(x, y, Math.max(1.2, r * 0.22), 0, Math.PI * 2);
          ctx.fillStyle = ink;
          ctx.fill();
        });
      });
    }

    function drawSwimmer(s, ppm) {
      var x = CX + s.x * ppm, y = CY + s.y * ppm, k;
      ctx.save();
      ctx.translate(x, y);
      ctx.rotate(s.hdg);
      if (s.type === "euglena") {
        var eL = 0.10 * ppm, eW = 0.035 * ppm;
        ctx.beginPath();
        ctx.ellipse(0, 0, eL / 2, eW / 2, 0, 0, Math.PI * 2);
        ctx.fillStyle = bio;
        ctx.fill();
        ctx.lineWidth = 1;
        ctx.strokeStyle = ink;
        ctx.stroke();
        ctx.beginPath();               // the eyespot, at the front
        ctx.arc(eL * 0.32, 0, Math.max(1.2, eW * 0.16), 0, Math.PI * 2);
        ctx.fillStyle = accent;
        ctx.fill();
        ctx.beginPath();               // the flagellum, beating ahead
        ctx.moveTo(eL / 2, 0);
        for (k = 1; k <= 8; k++) {
          ctx.lineTo(eL / 2 + k * eL * 0.09,
                     Math.sin(k * 1.1 + s.phase * 9) * eW * 0.3);
        }
        ctx.lineWidth = Math.max(1, eW * 0.08);
        ctx.strokeStyle = ink;
        ctx.stroke();
      } else if (s.type === "paramecium") {
        var pL = 0.18 * ppm, pW = 0.07 * ppm;
        ctx.beginPath();
        ctx.ellipse(0, 0, pL / 2, pW / 2, 0, 0, Math.PI * 2);
        ctx.fillStyle = card;
        ctx.fill();
        ctx.lineWidth = Math.max(1, pW * 0.05);
        ctx.strokeStyle = ink;
        ctx.stroke();
        for (k = 0; k < 26; k++) {     // cilia all round, mid-beat
          var a = (k / 26) * Math.PI * 2;
          var cx1 = Math.cos(a) * pL / 2, cy1 = Math.sin(a) * pW / 2;
          var tick = 1 + 0.35 * Math.sin(k + s.phase * 14);
          ctx.beginPath();
          ctx.moveTo(cx1, cy1);
          ctx.lineTo(cx1 * (1 + 0.10 * tick), cy1 * (1 + 0.22 * tick));
          ctx.stroke();
        }
        ctx.beginPath();               // oral groove
        ctx.arc(-pL * 0.1, pW * 0.16, pW * 0.16, 0.3, Math.PI - 0.3);
        ctx.stroke();
        for (k = 0; k < 2; k++) {      // contractile vacuoles
          ctx.beginPath();
          ctx.arc((k ? 1 : -1) * pL * 0.28, 0, pW * 0.13, 0, Math.PI * 2);
          ctx.strokeStyle = muted;
          ctx.stroke();
          ctx.strokeStyle = ink;
        }
      } else {                         // amoeba
        var aR = 0.125 * ppm;
        ctx.beginPath();
        for (k = 0; k <= 14; k++) {
          var aa = (k / 14) * Math.PI * 2;
          var rr = aR * (0.7 + 0.3 * Math.sin(aa * 3 + s.phase));
          if (k === 0) { ctx.moveTo(rr * Math.cos(aa), rr * Math.sin(aa)); }
          else { ctx.lineTo(rr * Math.cos(aa), rr * Math.sin(aa)); }
        }
        ctx.closePath();
        ctx.fillStyle = band;
        ctx.fill();
        ctx.lineWidth = Math.max(1.2, aR * 0.04);
        ctx.strokeStyle = ink;
        ctx.stroke();
        ctx.beginPath();
        ctx.arc(0, 0, Math.max(1.5, aR * 0.16), 0, Math.PI * 2);
        ctx.fillStyle = muted;
        ctx.fill();
      }
      ctx.restore();
    }

    function drawPond(ppm) {
      state.content.swimmers.forEach(function (s) {
        layer(viewSharp(s.depth), function () { drawSwimmer(s, ppm); });
      });
    }

    function draw() {
      var ppm = (FIELD_R * 2) / (FIELD_AT_1X_MM / state.dispMag);
      ctx.clearRect(0, 0, W, H);
      // The dark surround and the bright circular field: the view down
      // the tube, not a screen-shaped picture of one.
      ctx.fillStyle = ink;
      ctx.fillRect(0, 0, W, H);
      ctx.save();
      ctx.beginPath();
      ctx.arc(CX, CY, FIELD_R, 0, Math.PI * 2);
      ctx.clip();
      ctx.fillStyle = card;
      ctx.fillRect(CX - FIELD_R, CY - FIELD_R, FIELD_R * 2, FIELD_R * 2);
      var kn = kindNow();
      if (kn === "onion") { drawOnionLayer(ppm, viewSharp(30), false); }
      else if (kn === "bubbles") { drawBubbles(ppm); }
      else if (kn === "cheek") { drawCheek(ppm); }
      else if (kn === "pond") { drawPond(ppm); }
      ctx.restore();
      ctx.beginPath();
      ctx.arc(CX, CY, FIELD_R, 0, Math.PI * 2);
      ctx.lineWidth = 3;
      ctx.strokeStyle = ink;
      ctx.stroke();
    }

    // ── the readout: the whole result, in words, all of it computed ──
    var readout = sim.querySelector(".ks3-sim-readout");
    function say(txt) { if (readout) { readout.textContent = txt; } }

    function inViewSwimmers() {
      var half = fovMM() / 2, out = [];
      state.content.swimmers.forEach(function (s) {
        if (Math.sqrt(s.x * s.x + s.y * s.y) < half + 0.05) { out.push(s); }
      });
      return out;
    }

    var SWIMMER_WORDS = {
      euglena: "a Euglena — green, with a whip to swim with and an orange eyespot",
      paramecium: "a Paramecium — a slipper shape covered in beating cilia",
      amoeba: "an Amoeba — a slow grey blob pushing out pseudopods"
    };

    function whatYouSee() {
      var kn = kindNow(), s, n, ppm = (FIELD_R * 2) / fovMM();
      if (kn === "onion") {
        s = sharpOf(30);
        if (s >= 0.7) {
          n = Math.round(fovMM() / CELL_W);
          return (n <= 1
            ? "A single onion cell more than fills the view — straight sides, "
              + "part of a row."
            : "About " + n + " onion cells fit across the view — straight "
              + "sides, packed in rows like bricks.")
            + (CELL_W * ppm > 22 ? " Each has a small nucleus." : "");
        }
        if (s >= 0.3) {
          return "The rows are there, but soft — turn the focus until the "
            + "cell walls come sharp.";
        }
        return "A bright blur, nothing sharp. The focus is nowhere near the "
          + "specimen — turn it slowly and watch.";
      }
      if (kn === "bubbles") {
        var sb = sharpOf(12), sc = sharpOf(38);
        if (sb >= 0.6) {
          return "Perfectly round circles with a thick dark rim, floating "
            + "apart from each other. They look like cells; they are air "
            + "bubbles, trapped when the coverslip was dropped flat"
            + (sc < 0.4 ? " — and the onion cells are a blur underneath."
                        : ".");
        }
        if (sc >= 0.6) {
          return "Past the bubbles: rows of onion cells come sharp in the "
            + "gaps, but the blurred bubble rims still hide most of the "
            + "slide. A slide this bad is worth making again.";
        }
        return "Bright circles and shadows, none of it sharp — rack the "
          + "focus down through the slide.";
      }
      if (kn === "cheek") {
        if (CHEEK_D * ppm < 6) {
          return "Dozens of pale specks scattered across the view — too "
            + "small to make anything out at ×" + mag() + ".";
        }
        var best = 0, count = 0, half = fovMM() / 2;
        state.content.cells.forEach(function (cell) {
          var inV = Math.sqrt(cell.x * cell.x + cell.y * cell.y) < half;
          var sh = sharpOf(cell.depth);
          if (inV) { count++; if (sh > best) { best = sh; } }
        });
        if (!count) { return "Empty slide just here — the smear is patchy."; }
        if (best >= 0.6) {
          return count + " cheek cell" + (count === 1 ? "" : "s")
            + " in view — soft and rounded, each with a darker nucleus. "
            + "They sit at slightly different depths: nudge the focus and "
            + "different ones come sharp.";
        }
        return "Rounded shadows in the view, none sharp — bring the focus "
          + "through the smear slowly.";
      }
      if (kn === "pond") {
        var vis = inViewSwimmers();
        if (!vis.length) {
          return "Empty water just now. At ×" + mag() + " the view is only "
            + fovText() + " wide — drop back to ×40 to find something, "
            + "then work up.";
        }
        // Same honesty rule the cheek slide runs on: do not name a
        // feature the drawing is too small to show. A Paramecium is
        // 0.18 mm, which is 8 pixels across a ×40 field — a moving
        // speck, and saying so IS the lesson. It resolves from ×100.
        if (0.18 * ppm < 14) {
          return vis.length + " tiny specks drifting and darting about the "
            + "view — alive, clearly, but far too small at ×" + mag()
            + " to tell what any of them is. Found something? Turn the "
            + "magnification up.";
        }
        var bits = [], anyBlur = false;
        vis.forEach(function (sw) {
          var sh = sharpOf(sw.depth);
          if (sh < 0.6) { anyBlur = true; }
          bits.push(SWIMMER_WORDS[sw.type]
                    + (sh >= 0.6 ? " (sharp)" : " (a blur at another depth)"));
        });
        return "In view: " + bits.join("; ") + "."
          + (anyBlur ? " The water is deeper than the lens can focus — "
                       + "layers come sharp in turn." : "")
          + (mag() === 400 && vis.some(function (sw) { return sw.type === "paramecium"; })
             ? " The Paramecium will not stay long: at ×400 it crosses the "
               + "whole view in under a second."
             : "");
      }
      return "";
    }

    function report() {
      say("Total magnification ×" + mag() + " · field of view " + fovText()
          + ". " + whatYouSee());
    }

    // ── motion ──
    function stepSwimmers(dt) {
      if (kindNow() !== "pond") { return; }
      state.content.swimmers.forEach(function (s) {
        s.phase += dt * (s.type === "paramecium" ? 3 : 1);
        if (Math.random() < (s.type === "amoeba" ? 0.002 : 0.02)) {
          s.hdg += rand(-1.2, 1.2);
        }
        s.x += Math.cos(s.hdg) * s.speed * dt;
        s.y += Math.sin(s.hdg) * s.speed * dt;
        // Steer back toward the middle of the mount, softly — the drop
        // of water is bigger than the field but not infinite.
        var d = Math.sqrt(s.x * s.x + s.y * s.y);
        if (d > 2.3) {
          s.hdg = Math.atan2(-s.y, -s.x) + rand(-0.5, 0.5);
        }
      });
    }

    var raf = null;
    function animating() {
      return kindNow() === "pond" || Math.abs(state.dispMag - mag()) > 0.5;
    }
    function loop(now) {
      if (!state.running) { return; }
      var dt = state.last ? Math.min(50, now - state.last) / 1000 : 0.016;
      state.last = now;
      stepSwimmers(dt);
      if (Math.abs(state.dispMag - mag()) > 0.5) {
        // Law 9 — the zoom is a movement through magnifications, on a
        // log scale so ×40 → ×400 sweeps evenly, never a frame swap.
        var ratio = mag() / state.dispMag;
        var stepR = Math.pow(ratio, Math.min(1, dt * 3.2));
        state.dispMag *= stepR;
        if (Math.abs(state.dispMag - mag()) <= 0.5) { state.dispMag = mag(); }
        state.dirty = true;
      }
      if (animating() || state.dirty) {
        draw();
        state.dirty = false;
      }
      if (kindNow() === "pond") {
        // Organisms swim in and out of view, so — like diffusion's
        // crossing counts — this one readout re-reads on a cadence.
        if (!state.lastSay) { state.lastSay = now; }
        else if (now - state.lastSay > 700) { state.lastSay = now; report(); }
      }
      raf = window.requestAnimationFrame(loop);
    }
    function start() {
      if (state.running || REDUCED) { return; }
      state.running = true;
      state.last = 0;
      state.dirty = true;
      raf = window.requestAnimationFrame(loop);
    }
    function stop() {
      state.running = false;
      if (raf) { window.cancelAnimationFrame(raf); raf = null; }
    }

    // R6 — one representative frame at the CURRENT controls. The pond
    // settles 1,400 steps first so the frame is mid-swim, not the pose
    // the slide was mounted in; every control change re-settles.
    var SETTLE_STEPS = 1400;
    function settle() {
      var i;
      for (i = 0; i < SETTLE_STEPS; i++) { stepSwimmers(1 / 60); }
      state.dispMag = mag();
      draw();
      report();
    }

    function afterControlChange() {
      if (sim.getAttribute("data-locked") === "1") { return; }
      if (REDUCED) {
        settle();                     // R6 — re-settle from scratch
      } else {
        state.dirty = true;
        report();                     // the figures track the control at once
        if (!state.running) { draw(); }
      }
    }

    // ── controls (R15: real select / range, real labels) ──
    var controls = sim.querySelector(".ks3-sim-controls");
    if (controls) {
      (sim.getAttribute("data-controls") || "").split(",").forEach(function (name) {
        name = name.trim();
        var shell, input;
        if (name === "specimen") {
          shell = controlShell(name);
          if (!shell) { return; }
          input = document.createElement("select");
          input.id = shell.id;
          specimens.forEach(function (label, i) {
            var opt = document.createElement("option");
            opt.value = String(i);
            opt.textContent = label;
            input.appendChild(opt);
          });
          input.addEventListener("change", function () {
            state.slide = Number(input.value);
            state.content = buildContent(kindNow());
            afterControlChange();
          });
          shell.wrap.appendChild(input);
          controls.appendChild(shell.wrap);
        } else if (name === "magnification") {
          shell = controlShell(name);
          if (!shell) { return; }
          input = document.createElement("select");
          input.id = shell.id;
          OBJECTIVES.forEach(function (o, i) {
            var opt = document.createElement("option");
            opt.value = String(i);
            opt.textContent = "×" + (EYEPIECE * o)
              + (i === 0 ? " — lowest lens"
                 : (i === OBJECTIVES.length - 1 ? " — highest lens" : ""));
            input.appendChild(opt);
          });
          input.addEventListener("change", function () {
            state.obj = Number(input.value);
            afterControlChange();
          });
          shell.wrap.appendChild(input);
          controls.appendChild(shell.wrap);
        } else if (name === "focus") {
          shell = controlShell(name);
          if (!shell) { return; }
          input = document.createElement("input");
          input.type = "range";
          input.min = "0"; input.max = "100"; input.value = String(state.focus);
          input.id = shell.id;
          // Deliberately no number beside it: a fine-focus wheel is
          // unnumbered, and what the position MEANS is the readout's job.
          //
          // MRB-210 §2 — bound on BOTH `input` and `change`, matching
          // Design's approved B1-06 (`onChange={...} onInput={...}` on
          // the same handler). `input` alone covers a mouse or touch
          // drag and keyboard arrows in current browsers, but it is not
          // the only path to a range value: some assistive technologies
          // and automation set `.value` and fire `change` only, and that
          // interaction would silently do nothing. Verified by driving
          // all 12 range controls across the full control matrix on all
          // 183 lesson pages — before this, `change` reached the handler
          // on exactly none of them.
          onRange(input, function () {
            state.focus = Number(input.value);
            afterControlChange();
          });
          shell.wrap.appendChild(input);
          controls.appendChild(shell.wrap);
        }
      });
    }

    report();          // never leave the readout empty, even while locked
    wireGate(sim, { draw: draw, settle: settle, start: start, stop: stop });
  }

  /* ═══════════════════════════════════════════════════════════════
     MRB-198 · SYSTEM-PARTS — the SYSTEM family's perturbation
     flagship (B1 L3, L4, L5), and the pattern for 47 lessons.

     §6, verbatim: "the characteristic KS3 error is knowing the parts
     and not the interaction, so the flagship must be perturbation,
     never labelling." There is deliberately NO mode in which this
     component just names parts: the only control switches one off,
     and the only spectacle is the failure CLIMBING THE LEVELS. If you
     find yourself adding clickable hotspots to a labelled diagram,
     stop — that is the thing this component exists instead of.

     Everything is DERIVED from the payload, never scripted per
     lesson:
       · the layout — a part sits one row above the things it needs
         (longest dependent chain), so providers rest at the bottom
         and the whole drawing reads as "everything stands on the
         membrane" / "the organism stands on its cells";
       · the cascade — switch a part off and every part whose `needs`
         list touches a stopped part stops in the next wave, wave by
         wave (Law 9: the spread is animated as movement; reduced
         motion draws the settled end state and the readout carries
         the whole result);
       · the scale rule — a part flagged `one_of_many` is ONE
         INSTANCE of a large population (a single muscle cell in a
         tissue of thousands). Switching it off stops only itself:
         the parts that need its KIND still have the rest. That
         contrast — one cell is nothing, one tissue is everything —
         is what having levels of organisation buys, and the payload
         states it as data so the engine never scripts it.

     R3: stopped/working is SIM STATE, not correctness — no green
     tick, no red cross on any option, and the marks drawn here are
     drawn strokes (the font subsets carry no ✕ glyph, and text is
     the readout's job anyway).
     ═══════════════════════════════════════════════════════════════ */

  function wireSystemParts(sim) {
    var canvas = sim.querySelector(".ks3-sim-canvas");
    if (!canvas || !canvas.getContext) { return; }
    var ctx = canvas.getContext("2d");
    var W = canvas.width, H = canvas.height;

    var ink = cssVar(sim, "--ks3-ink", "#221E1B");
    var card = cssVar(sim, "--ks3-card", "#FFFCF5");
    var spent = cssVar(sim, "--ks3-option-spent", "#EBDFCB");
    var accent = cssVar(sim, "--ks3-accent", "#E4572E");
    var ruleStrong = cssVar(sim, "--ks3-rule-strong", "#C3B191");

    var parts;
    try {
      parts = JSON.parse(sim.getAttribute("data-parts") || "[]");
    } catch (err) { parts = []; }
    if (!parts.length) { return; }

    var byId = {};
    parts.forEach(function (p) { byId[p.id] = p; });

    // Row = the longest chain of dependents ABOVE a part. Sinks (the
    // organism, the delivered oxygen) land on row 0 at the top; the
    // deepest providers rest on the bottom row. Derived, not authored.
    var dependents = {};
    parts.forEach(function (p) {
      (p.needs || []).forEach(function (n) {
        (dependents[n] = dependents[n] || []).push(p.id);
      });
    });
    var upMemo = {};
    function up(id) {
      if (upMemo.hasOwnProperty(id)) { return upMemo[id]; }
      var deps = dependents[id] || [], best = 0, i;
      upMemo[id] = 0;                  // build_ks3.py proved acyclicity
      for (i = 0; i < deps.length; i++) {
        var d = 1 + up(deps[i]);
        if (d > best) { best = d; }
      }
      upMemo[id] = best;
      return best;
    }
    var nRows = 0;
    parts.forEach(function (p) {
      if (up(p.id) + 1 > nRows) { nRows = up(p.id) + 1; }
    });

    var rows = [];
    (function () {
      var i;
      for (i = 0; i < nRows; i++) { rows.push([]); }
      parts.forEach(function (p) { rows[up(p.id)].push(p); });
    })();

    var PAD = 10;
    var rowH = (H - PAD * 2) / nRows;
    // The GAP between rows is where the dependency edges are drawn, and
    // the edges are what make a cascade read as a cascade rather than as
    // boxes changing colour. A 5-level payload leaves 40px per row, so
    // boxes take at most 60% of it and the remaining 16px carries the
    // travelling dashed line.
    var boxH = Math.min(30, rowH * 0.6);
    var geom = {};
    rows.forEach(function (row, r) {
      row.forEach(function (p, i) {
        var cw = (W - PAD * 2) / row.length;
        geom[p.id] = {
          x: PAD + cw * (i + 0.5),
          y: PAD + r * rowH + rowH / 2,
          w: Math.min(cw - 10, 158),
          h: boxH
        };
      });
    });

    // name → up to two lines, splitting at " (" so "Cell wall (plant
    // only)" keeps its qualifier without overflowing the box.
    function nameLines(p) {
      var m = /^(.*?)\s*(\(.*\))$/.exec(p.name);
      return m ? [m[1], m[2]] : [p.name];
    }

    var state = { off: null, waves: [], shown: 0, absorbed: false, anim: null };

    function cascade(offId) {
      // The knock-on is DERIVED: wave 0 is the switched-off part; each
      // later wave is every still-working part one of whose needs has
      // stopped. one_of_many absorbs the failure at wave 0.
      var stopped = {}, waves = [[offId]], absorbed = false;
      stopped[offId] = true;
      if (byId[offId].one_of_many) {
        absorbed = true;
      } else {
        for (;;) {
          var next = [];
          parts.forEach(function (p) {
            if (stopped[p.id]) { return; }
            var hit = (p.needs || []).some(function (n) { return stopped[n]; });
            if (hit) { next.push(p.id); }
          });
          if (!next.length) { break; }
          next.forEach(function (id) { stopped[id] = true; });
          waves.push(next);
        }
      }
      return { waves: waves, absorbed: absorbed };
    }

    function stoppedNow() {
      var out = {}, i, j;
      for (i = 0; i < state.shown && i < state.waves.length; i++) {
        for (j = 0; j < state.waves[i].length; j++) {
          out[state.waves[i][j]] = i;
        }
      }
      return out;
    }

    function partFont(px) {
      ctx.font = "600 " + px + "px 'Instrument Sans', system-ui, sans-serif";
    }

    function drawNode(p, stoppedWave, isOrigin) {
      var g = geom[p.id];
      var x = g.x - g.w / 2, y = g.y - g.h / 2;
      var stoppedHere = stoppedWave !== undefined;
      ctx.fillStyle = stoppedHere ? spent : card;
      ctx.fillRect(x, y, g.w, g.h);
      if (stoppedHere) {
        // Diagonal hatch: the drawn "stopped" state. Ink on the spent
        // fill, so the mark holds well past 3:1 (R1).
        ctx.save();
        ctx.beginPath();
        ctx.rect(x, y, g.w, g.h);
        ctx.clip();
        ctx.strokeStyle = ink;
        ctx.globalAlpha = 0.18;
        ctx.lineWidth = 1;
        var hx;
        for (hx = -g.h; hx < g.w; hx += 7) {
          ctx.beginPath();
          ctx.moveTo(x + hx, y + g.h);
          ctx.lineTo(x + hx + g.h, y);
          ctx.stroke();
        }
        ctx.restore();
      }
      ctx.lineWidth = isOrigin ? 3 : 2;
      ctx.strokeStyle = isOrigin ? accent : ink;
      if (stoppedHere && !isOrigin && ctx.setLineDash) { ctx.setLineDash([5, 3]); }
      ctx.strokeRect(x, y, g.w, g.h);
      if (ctx.setLineDash) { ctx.setLineDash([]); }

      var lines = nameLines(p);
      var fpx = lines.length > 1 ? 10 : 11;
      partFont(fpx);
      while (fpx > 8.5) {
        var wide = false, li;
        for (li = 0; li < lines.length; li++) {
          if (ctx.measureText(lines[li]).width > g.w - 12) { wide = true; }
        }
        if (!wide) { break; }
        fpx -= 0.5;
        partFont(fpx);
      }
      ctx.fillStyle = ink;
      ctx.textAlign = "center";
      ctx.textBaseline = "middle";
      if (lines.length > 1) {
        ctx.fillText(lines[0], g.x, g.y - fpx * 0.62);
        ctx.fillText(lines[1], g.x, g.y + fpx * 0.62);
      } else {
        ctx.fillText(lines[0], g.x, g.y);
      }

      if (stoppedHere) {
        // A drawn stop-mark in the corner — strokes, never a ✕ glyph.
        var mx = x + g.w - 11, my = y + 4;
        ctx.lineWidth = 2;
        ctx.strokeStyle = isOrigin ? accent : ink;
        ctx.beginPath();
        ctx.moveTo(mx, my); ctx.lineTo(mx + 7, my + 7);
        ctx.moveTo(mx + 7, my); ctx.lineTo(mx, my + 7);
        ctx.stroke();
      }
    }

    function drawEdges(stopped, pulseT) {
      parts.forEach(function (p) {
        (p.needs || []).forEach(function (n) {
          var a = geom[n], b = geom[p.id];
          var failing = stopped[n] !== undefined && stopped[p.id] !== undefined
                        && !state.absorbed;
          ctx.beginPath();
          ctx.moveTo(a.x, a.y - a.h / 2);
          ctx.lineTo(b.x, b.y + b.h / 2);
          ctx.lineWidth = failing ? 2.5 : 2;
          ctx.strokeStyle = failing ? accent : ruleStrong;
          if (failing && ctx.setLineDash) {
            // Law 9 — the failure travels ALONG the edge as movement.
            ctx.setLineDash([6, 5]);
            ctx.lineDashOffset = -(pulseT || 0) * 30;
          }
          ctx.stroke();
          if (ctx.setLineDash) { ctx.setLineDash([]); ctx.lineDashOffset = 0; }
        });
      });
    }

    var pulse = 0;
    function draw() {
      var stopped = stoppedNow();
      ctx.clearRect(0, 0, W, H);
      drawEdges(stopped, pulse);
      parts.forEach(function (p) {
        drawNode(p, stopped[p.id], state.off === p.id);
      });
    }

    // ── the readout: what still works · what has stopped ──
    var readout = sim.querySelector(".ks3-sim-readout");
    function say(txt) { if (readout) { readout.textContent = txt; } }

    function names(ids) {
      return ids.map(function (id) { return byId[id].name; });
    }

    function report() {
      if (!state.off) {
        say("Every part is working. Switch one off, and predict what stops "
            + "first before you look.");
        return;
      }
      var p = byId[state.off];
      var head = "The " + p.name.toLowerCase() + " is off. Its job — "
                 + p.job.toLowerCase() + " — is not being done. ";
      if (state.absorbed) {
        say(head + "Almost nothing else happens: it is one of thousands "
            + "doing that job, and the rest cover for it. Everything else "
            + "still works.");
        return;
      }
      var later = [], i;
      for (i = 1; i < state.waves.length; i++) {
        later.push(names(state.waves[i]).join(" and "));
      }
      var stillOn = parts.filter(function (q) {
        return !state.waves.some(function (w) { return w.indexOf(q.id) >= 0; });
      });
      say(head
          + (later.length
             ? "Stopped, in the order the failure spread: "
               + later.join(", then ") + ". "
             : "Nothing else depends on it, so nothing else stops. ")
          + (stillOn.length
             ? "Still working: " + names(stillOn.map(function (q) { return q.id; })).join(", ") + "."
             : "Nothing is still working."));
    }

    // ── the cascade, animated wave by wave (Law 9) ──
    var raf = null, waveT = 0, lastT = 0;
    var WAVE_MS = 550;

    function animate(now) {
      if (!lastT) { lastT = now; }
      var dt = now - lastT;
      lastT = now;
      pulse += dt / 1000;
      waveT += dt;
      if (waveT >= WAVE_MS && state.shown < state.waves.length) {
        state.shown++;
        waveT = 0;
      }
      draw();
      if (state.shown < state.waves.length || state.absorbed === false
          && state.shown === state.waves.length && pulse < 60) {
        // Keep the dashed pulse moving while a failure is on screen —
        // a frozen "spreading" mark reads as a finished one.
        raf = window.requestAnimationFrame(animate);
      }
    }

    function stopAnim() {
      if (raf) { window.cancelAnimationFrame(raf); raf = null; }
      lastT = 0;
    }

    function applyOff(offId) {
      stopAnim();
      state.off = offId;
      if (!offId) {
        state.waves = [];
        state.shown = 0;
        state.absorbed = false;
        draw();
        report();
        return;
      }
      var c = cascade(offId);
      state.waves = c.waves;
      state.absorbed = c.absorbed;
      if (REDUCED) {
        state.shown = state.waves.length;   // R6: the end state, at once
        draw();
      } else {
        state.shown = 1;                    // the switched-off part, now
        waveT = 0;
        draw();
        raf = window.requestAnimationFrame(animate);
      }
      report();   // the words carry the WHOLE result either way (R6)
    }

    // ── the one control: a part selector, never a slider (R15) ──
    var controls = sim.querySelector(".ks3-sim-controls");
    var shell = controls ? controlShell("part") : null;
    if (shell) {
      var sel = document.createElement("select");
      sel.id = shell.id;
      var optAll = document.createElement("option");
      optAll.value = "";
      optAll.textContent = "Every part on";
      sel.appendChild(optAll);
      parts.forEach(function (p) {
        var opt = document.createElement("option");
        opt.value = p.id;
        opt.textContent = "Switch off: " + p.name;
        sel.appendChild(opt);
      });
      sel.addEventListener("change", function () {
        if (sim.getAttribute("data-locked") === "1") { return; }
        applyOff(sel.value || null);
      });
      shell.wrap.appendChild(sel);
      controls.appendChild(shell.wrap);
    }

    function settle() {
      if (state.off) {
        state.shown = state.waves.length;
      }
      draw();
      report();
    }
    function start() { draw(); report(); }

    report();          // never leave the readout empty, even while locked
    wireGate(sim, { draw: draw, settle: settle, start: start, stop: stopAnim });
  }

  function wireSims(root) {
    each(root.querySelectorAll(".ks3-sim"), wireSim);
  }

  function init() {
    wirePredictions(document);
    wireCriteria(document);
    wireCards(document);
    wireSims(document);
    each(document.querySelectorAll(".ks3-ladder"), wireLadder);
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
