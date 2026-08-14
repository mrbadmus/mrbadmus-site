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
  // Motion is a preference, not per-lesson progress: it is deliberately
  // NOT slug-keyed, so answering it once answers it for the key stage.
  var MOTION_KEY = "ks3_motion";

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
      // ⊕ An instrument owns every option inside it. `build_ks3.py` has
      // claimed this exclusion in a comment since B1 round two and the check
      // did not exist, which on the seven-tests board would have wired all
      // four specimen panels' predictions to one another and unhidden
      // specimen one's verdict panel on any of them — `querySelector`
      // returns the FIRST [data-reveal] in the section, and on that board it
      // is a verdict, not a gate.
      if (block.hasAttribute("data-instrument")) { return; }
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
    part:          "Switch one part off",
    // MRB-211 — the bench's two. These are the generic words; a lesson that
    // has better ones says so in `control_labels` and they win, exactly as
    // B1-06 says "Mount" where the engine says "Slide on the stage".
    centre:        "Move the slide to",
    motion:        "Movement"
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
  function controlShell(name, caption) {
    if (!CONTROL_LABELS.hasOwnProperty(name)) { return null; }
    var id = "ks3-sim-" + name + "-" + (++UID);
    var wrap = document.createElement("label");
    wrap.className = "ks3-sim-control";
    wrap.setAttribute("for", id);
    wrap.appendChild(document.createTextNode(caption || CONTROL_LABELS[name]));
    return { wrap: wrap, id: id };
  }

  /* MRB-211 — the same shell for a control that is a ROW OF BUTTONS rather
     than one input: Design draws the bench's mount, objective, centre and
     motion groups as segmented buttons, and a two-state toggle is a button
     with `aria-pressed`, not a select with two options.

     A <label for=> cannot carry a group — `for` names one labelable element
     and there are three here — so the caption becomes a <span> and the row
     is a `role="group"` named by it. That is the same accessible name a
     <label> would have given, reached the way a group has to reach it.
     R15 is honoured on its terms: a real caption, really associated, and no
     control on the panel that does nothing. */
  function segShell(name, caption) {
    if (!CONTROL_LABELS.hasOwnProperty(name)) { return null; }
    var id = "ks3-sim-" + name + "-" + (++UID);
    var wrap = document.createElement("div");
    wrap.className = "ks3-sim-control ks3-sim-control-seg";
    var cap = document.createElement("span");
    cap.className = "ks3-sim-control-caption";
    cap.id = id;
    cap.appendChild(document.createTextNode(caption || CONTROL_LABELS[name]));
    var row = document.createElement("div");
    row.className = "ks3-sim-seg";
    row.setAttribute("role", "group");
    row.setAttribute("aria-labelledby", id);
    wrap.appendChild(cap);
    wrap.appendChild(row);
    return { wrap: wrap, row: row, id: id };
  }

  // One segmented button. `aria-pressed` is the state — R2: the state carries
  // a word and a border, never colour alone — and R3 is untouched, because
  // nothing here is an answer: it is where the slide is and whether it moves.
  function segButton(text, pressed) {
    var b = document.createElement("button");
    b.type = "button";
    b.className = "ks3-sim-seg-btn";
    b.setAttribute("aria-pressed", pressed ? "true" : "false");
    b.appendChild(document.createTextNode(text));
    return b;
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
       depth of field      = OBJ_DOF_MM — a TABLE, not a formula
                             ×40 → 0.100 mm · ×100 → 0.040 · ×400 → 0.008
       focus wheel (0–100) = −0.09 mm … +0.09 mm through the specimen
       a layer is SHARP    = |focal plane − depth| < 0.6 × depth of field

     Everything is in MILLIMETRES on the slide, exactly as Design's two
     approved pages are. The mm figure, the drawn size of every cell, the
     count of cells across the view and the blur are ALL computed from
     those lines. No figure in the readout is invented (the review pack's
     1.8 mm ÷ 6 onion cells falls straight out: 1.8 / 0.30).

     ONE kernel, TWO renderers, FOUR blur laws (MRB-210):
       · the kernel is the mm model above, and it is the same instrument
         on every slide and in every lesson;
       · tessellation-with-N-layers tiles a payload's layers[] and takes
         each layer's blur from its OWN depth — onion (N=3), cheek (N=1),
         and the onion bed under the bubbles;
       · scatter-with-per-item-depth walks a list whose every item carries
         a depth and blurs each one independently — pond organisms, pond
         bacteria, bubbles.
     The blur CAP and FACTOR are per specimen because Design tuned them
     per specimen: a bacterium two pixels wide cannot carry an 11 px
     blur. Those are rendering choices and travel with the payload. The
     optics are not a choice and live in one table.

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

     Focus racks through the DEPTH of the slide (0–100 on the wheel,
     0.18 mm of real travel), so a thick specimen — pond water above
     all — can never be sharp all at once:
     different layers come sharp in turn. Law 9: the magnification
     change is a real zoom transition, never a frame swap; reduced
     motion gets the settled frame and the full written readout.
     ═══════════════════════════════════════════════════════════════ */

  var EYEPIECE = 10;
  var OBJECTIVES = [4, 10, 40];
  var FIELD_AT_1X_MM = 180;

  // ── MRB-210: the single KS3 microscope depth-of-field table ──────────
  // Ruled by Mide, 13 Aug 2026. Design implemented the microscope inline
  // twice and the two approved pages disagreed: B1-02 had 0.30 / 0.09 /
  // 0.012 mm, B1-06 had 0.100 / 0.040 / 0.008. B1-06's stands for all of
  // KS3 — B1-02's is roughly three times too generous at the low power and
  // does not describe a school microscope. The same instrument behaving
  // differently in two lessons a fortnight apart is a science error, not a
  // per-lesson design choice, so this is an engine constant and NOT a
  // payload field.
  //
  // Deliberately a TABLE and not a law. Depth of field falls faster than
  // magnification does — these three stand in the ratio 1 : 2.5 : 12.5
  // while the magnifications are 1 : 2.5 : 10 — so the old `2200 / mag`
  // could not express it. That formula happened to land within 1% at ×40
  // and ×100 and was 24% too generous at ×400, which is the one place the
  // lesson depends on the window being cruelly thin.
  var OBJ_DOF_MM = [0.100, 0.040, 0.008];   // index matches OBJECTIVES

  // The focus wheel is a 0..100 slider; both approved pages map it to the
  // same 0.18 mm of travel through the specimen, centred on the slide.
  var FOCUS_MIN_MM = -0.09, FOCUS_SPAN_MM = 0.18;

  // Sharp = within 0.6 of a depth of field, both approved pages.
  var SHARP_FRACTION = 0.6;

  // Non-parfocal focus offsets, in SLIDER UNITS: racking up a lens
  // carries the focal plane further down, exactly like the school
  // microscopes these students use. These exist in NEITHER of Design's
  // approved pages — Code added them under MRB-198, and Mide ruled on
  // 13 Aug 2026 that they STAY: they sit inside an instrument Design
  // drew, the approved pages are silent on parfocality, and they are how
  // the component teaches the registered misconception CELL-02, "the
  // highest magnification is always the best one". Without them, turning
  // the lens up only scales the drawing, and nothing is learned.
  var OBJ_FOCUS_SHIFT = [0, 10, 22];

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

    /* ── MRB-211 · G9 — TWO MOUNTS ON ONE INSTRUMENT ──────────────────
       `data-specimens` is the classifier list and stays exactly what
       MRB-198 shipped, so an instrument with no mounts (B1-02) reads a
       synthesised list here and behaves identically. `data-mounts` adds
       what a mount is beyond a slide model: the caption on its button,
       its own cast of organisms, and the three strings that must switch
       WITH the slide — the note under the bench, the caption under the
       canvas, and the canvas's own aria-label. Design authored one of
       each per mount, so one per instrument would be wrong for both. */
    var mounts = [];
    try {
      mounts = JSON.parse(sim.getAttribute("data-mounts") || "[]") || [];
    } catch (err2) { mounts = []; }
    if (!mounts.length) {
      mounts = specimens.map(function (name, i) {
        return { id: String(i), label: String(name), specimen: String(name) };
      });
    }

    var bench = {};
    try {
      bench = JSON.parse(sim.getAttribute("data-bench") || "{}") || {};
    } catch (err3) { bench = {}; }
    var BENCH_CENTRES = bench.centres || [];
    var CENTRE_ON = bench.centreOn || null;   // null = every mount
    var MOTION = bench.motion || null;
    var RESOLVE = bench.resolve || null;
    var CAPTIONS = bench.labels || {};

    var FIELD_R = 96, CX = W / 2, CY = H / 2;
    // D2's onion cell: 0.30 mm across, 0.115 mm deep. The 0.13 mm this
    // engine carried before MRB-210 was not Design's figure, and it made
    // the count of cells DOWN a column disagree with the approved page.
    var CELL_W = 0.30, CELL_H = 0.115;
    var CHEEK_D = 0.06;                 // a cheek cell, mm — D6's cellMm

    // Design's specimen colours, from the approved pages. These are
    // pigment on a slide, not interface chrome, so they are literals
    // rather than theme tokens — an onion epidermis is the same brown in
    // either theme, and R3 is untouched (nothing here marks an answer).
    var ONION_MID = "#8A6A3C", ONION_EDGE = "#A98A5E";
    var ONION_NUCLEUS = "#7A5A2E";
    var BACT_DOT = "#6E6152", BACT_ROD = "#7C6E5C";

    // D6 gates fine structure on `px > 44`, measured on ITS canvas, whose
    // field radius is 252 px. This field is 96 px, so the same FRACTION of
    // the view is 16.8 px here. Taking the literal 44 would deny the
    // Euglena its eyespot and the cheek cell its nucleus at EVERY
    // magnification this microscope has — while the readout names both —
    // and it would not reproduce D6's page either. Scaled, the gate opens
    // and shuts on exactly the same (specimen × lens) combinations D6's
    // page opens and shuts on.
    var DESIGN_FIELD_R = 252, DESIGN_DETAIL_PX = 44;
    function detailAt(px) {
      return px > DESIGN_DETAIL_PX * (FIELD_R / DESIGN_FIELD_R);
    }

    // The bubble slide's two depths. This slide appears on NO approved
    // Design page: it is kept because B1-02's authored payload really does
    // declare it ("onion skin — coverslip dropped flat"), it confronts the
    // registered misconception `bubble-or-cell`, and B1-02's authored
    // reveal text depends on comparing the two onion slides. The figures
    // are the old slider-unit depths 12 and 38 carried across the same
    // 0..100 → −0.09..+0.09 mm mapping, so the slide racks exactly as it
    // did — and the arithmetic lands where the physics wants it: the
    // bubbles sit ABOVE the tissue, trapped under the coverslip.
    var BUBBLE_DEPTH_MM = -0.0684, BUBBLE_BED_DEPTH_MM = -0.0216;

    // Swimming speeds in mm/s, by kind — this engine's, not Design's; see
    // the note in buildContent.
    var ORG_SPEED = { paramecium: 0.55, euglena: 0.12, amoeba: 0.02 };

    // Slide content is generated once per slide, in MILLIMETRES about the
    // field centre, so racking the controls looks at the SAME slide.
    function buildContent(kindName, mount) {
      var i, out;
      if (kindName === "onion") {
        // D2 draws the onion as three layers of epidermis, 0.055 mm apart.
        // Racking through them IS the lesson; one layer taught the
        // opposite — that a slide is flat and focus is a knob you set once.
        return { layers: [
          { depth: -0.055, alpha: 0.72, stroke: ONION_EDGE },
          { depth:  0.000, alpha: 1.00, stroke: ONION_MID },
          { depth:  0.055, alpha: 0.72, stroke: ONION_EDGE }
        ] };
      }
      if (kindName === "cheek") {
        // A smear is a SHEET. One layer at one depth, so racking finds
        // nothing behind it — which is what B1-06 exists to contrast
        // against the pond's three-dimensional world. The 26 cells at 26
        // random depths this engine drew before taught the exact opposite
        // of the page's own words.
        return { layers: [{ depth: 0.000, alpha: 1.00 }] };
      }
      if (kindName === "bubbles") {
        out = [];
        for (i = 0; i < 7; i++) {
          out.push({ x: rand(-2.2, 2.2), y: rand(-1.2, 1.2),
                     d: rand(0.35, 0.95), depth: BUBBLE_DEPTH_MM });
        }
        return {
          bubbleDepth: BUBBLE_DEPTH_MM,
          onionDepth: BUBBLE_BED_DEPTH_MM,
          // one bed of onion tissue under the trapped air
          layers: [{ depth: BUBBLE_BED_DEPTH_MM, alpha: 0.80,
                     stroke: ONION_EDGE }],
          bubbles: out
        };
      }
      if (kindName === "pond") {
        // D6's cast of seven, verbatim: positions, depths, lengths and
        // shape seeds are all in mm on the slide. A mount that carries its
        // own cast wins — B1-06 authors these same seven — and it is COPIED,
        // because the swimmers are stepped in place and a mount must open
        // where it was drawn, not where it was last left.
        var authored = mount && mount.organisms;
        var orgs = (authored && authored.length) ? authored.map(function (o) {
          return { kind: o.kind, x: o.x, y: o.y,
                   depth: o.depth, len: o.len, seed: o.seed };
        }) : [
          { kind: "amoeba",     x: -0.90, y:  0.30, depth: -0.045, len: 0.30, seed: 0.4 },
          { kind: "paramecium", x:  0.15, y: -0.10, depth:  0.000, len: 0.25, seed: 1.1 },
          { kind: "euglena",    x:  0.58, y:  0.46, depth:  0.050, len: 0.05, seed: 2.3 },
          { kind: "euglena",    x: -0.30, y: -0.58, depth: -0.020, len: 0.05, seed: 3.7 },
          { kind: "paramecium", x:  1.45, y:  0.95, depth:  0.030, len: 0.25, seed: 0.8 },
          { kind: "amoeba",     x:  1.95, y: -1.15, depth: -0.070, len: 0.30, seed: 2.9 },
          { kind: "euglena",    x: -1.60, y:  1.10, depth:  0.015, len: 0.05, seed: 1.6 }
        ];
        // Design's page holds the cast still and gives the student a
        // `centre` control to pan to each one. This engine has no centre
        // control, so the organisms SWIM — the engine's own behaviour
        // since MRB-198, and the reason the pond readout re-reads on a
        // cadence and R6 settles 1,400 steps before drawing a frame. It is
        // also the honest thing: a wet mount is the one slide where being
        // alive is visible. Motion is layered ON the approved payload,
        // never over it: x, y, depth, len and seed are D6's, and the
        // heading is DERIVED from the seed rather than drawn at random, so
        // the slide opens the same way every time — the same discipline
        // the bacteria field is built on.
        for (i = 0; i < orgs.length; i++) {
          orgs[i].speed = ORG_SPEED[orgs[i].kind] || 0.1;
          orgs[i].hdg = orgs[i].seed * 1.7;
          orgs[i].phase = orgs[i].seed;
        }
        // 54 bacteria, at 0.002 mm. They stay two pixels of nothing at
        // every magnification, which is the point: you can see THAT they
        // are there, not WHAT they are. Deterministic LCG, verbatim from
        // D6, so the slide is the same slide every time it is opened.
        var bact = [], n = 0, a, b, c;
        for (i = 0; i < 54; i++) {
          n = (n * 1103515245 + 12345) % 2147483648; a = n / 2147483648;
          n = (n * 1103515245 + 12345) % 2147483648; b = n / 2147483648;
          n = (n * 1103515245 + 12345) % 2147483648; c = n / 2147483648;
          bact.push({ x: (a - 0.5) * 3.4, y: (b - 0.5) * 3.4,
                      depth: (c - 0.5) * 0.14, rot: a * 6.28 });
        }
        return { organisms: orgs, bacteria: bact };
      }
      return {};   // unknown kind: draws nothing, says nothing, throws nothing
    }

    function startSlide() {
      var i;
      for (i = 0; i < mounts.length; i++) {
        if (bench.start && mounts[i].id === bench.start) { return i; }
      }
      return 0;
    }

    var state = {
      slide: startSlide(),          // index into mounts[] / specimens[]
      obj: 0,                       // index into OBJECTIVES — start LOWEST
      // Design's own default (B1-02 line 630), and it has to be 50 now
      // that depths are in mm: 50 puts the focal plane exactly ON the
      // middle layer at the lowest lens. The lesson only works if the
      // opening view is GOOD and turning the magnification up is what
      // breaks it — opening soft would make the readout's "packed in rows
      // like bricks" a claim the picture does not honour. With the ruled
      // table and the non-parfocal shifts this default gives the whole
      // teaching ladder: ×40 holds all three layers at once, ×100 holds
      // the middle one and loses the others, ×400 loses everything until
      // the focus is corrected. The old 30 was tuned for slider-unit
      // depths; carried across unchanged it would have left ×400
      // ACCIDENTALLY sharp (focus 30 + shift 22 = 52 ≈ the middle of the
      // wheel = 0.000 mm), which is precisely CELL-02 going untaught.
      focus: 50,
      dispMag: EYEPIECE * OBJECTIVES[0],   // what the canvas shows NOW
      running: false, dirty: true, lastSay: 0, last: 0,
      // MRB-211 — which centre the field is on, and whether the mount is
      // alive. `motion` defaults to the payload's, which is ON: the words
      // are "Swimming" and "Held still", and the bench opens alive.
      centre: null,
      motion: !MOTION || MOTION.on !== false,
      content: null
    };

    function mountNow() { return mounts[state.slide] || {}; }
    state.content = buildContent(specimenKind(specimens[state.slide]),
                                 mountNow());

    /* ── MRB-211 · G10 — where the field is centred ────────────────────
       The centre control is offered PER MOUNT: B1-06 offers it on the pond
       and not on the cheek smear, because a tessellated sheet has nothing
       to pan to. Where it is not offered the field sits at the origin, so
       every instrument that predates this behaves exactly as it did. */
    function centresHere() {
      if (!BENCH_CENTRES.length) { return null; }
      if (CENTRE_ON && CENTRE_ON.indexOf(mountNow().id) < 0) { return null; }
      return BENCH_CENTRES;
    }

    // Preallocated: this is read once per organism per frame and 61 fresh
    // objects a frame is a garbage collector's problem, not a model's.
    var CTR = { x: 0, y: 0 };
    function effectiveCentre() {
      var cs = centresHere(), i;
      if (!cs) { return null; }
      for (i = 0; i < cs.length; i++) {
        if (cs[i].id === state.centre) { return cs[i]; }
      }
      // Design's own fallback (`CENTRES.find(...) || CENTRES[1]`): with
      // nothing chosen the field opens on the SECOND centre — B1-06's
      // slipper, the one organism sitting at depth 0.000 — so the bench
      // opens on something rather than on the origin. The button for it is
      // drawn pressed, because it is where the slide actually is.
      return cs[cs.length > 1 ? 1 : 0];
    }
    function centreMM() {
      var c = effectiveCentre();
      CTR.x = c ? c.x : 0;
      CTR.y = c ? c.y : 0;
      return CTR;
    }

    /* ⚑ F33 — THE ORGANISMS STOP SWIMMING WHERE THERE IS A CENTRE CONTROL.
       Design's approved B1-06 says so in student-facing prose — "Real ones
       swim out of the field in seconds. These are held for you, and the
       slide moves when you ask it to" — and the standing law is that where
       the page teaches one thing in words and the engine does another, the
       page wins. It is also the only coherent reading: a control that pans
       the field to the blob is a lie if the blob has drifted off by the
       time the student looks up, and centring and focusing are two separate
       operations precisely BECAUSE the cast holds still while the wheel
       moves. So `pinned()` removes the TRANSLATION only. The organisms stay
       alive — cilia beat, vacuoles fill and empty, the Euglena bends — and
       THAT is what the motion toggle governs, which is why its two words
       are "Swimming" and "Held still" rather than "On" and "Off". An
       instrument with no centre control (B1-02, and any lesson that only
       wants a wet mount) swims exactly as MRB-198 shipped it. */
    function pinned() { return !!centresHere(); }

    function mag() { return EYEPIECE * OBJECTIVES[state.obj]; }
    function fovMM() { return FIELD_AT_1X_MM / mag(); }

    // Slider units -> depth in mm through the specimen.
    function focusMM(units) {
      return FOCUS_MIN_MM + (units / 100) * FOCUS_SPAN_MM;
    }
    // The focal plane, including the non-parfocal offset for this lens.
    function focalMM() {
      return focusMM(state.focus + OBJ_FOCUS_SHIFT[state.obj]);
    }
    function dofMM() { return OBJ_DOF_MM[state.obj]; }
    function sharpWindowMM() { return SHARP_FRACTION * dofMM(); }
    // How far a given depth sits from the focal plane, in mm.
    function offMM(depthMM) { return Math.abs(depthMM - focalMM()); }
    // Design's readouts count what is SHARP as a boolean, not on a ramp.
    function isSharp(depthMM) { return offMM(depthMM) < sharpWindowMM(); }

    // Law 9 — mid-zoom the canvas must use the optics of the magnification
    // it is DISPLAYING, or the image would snap between focus states
    // instead of sliding. Depth of field is now a table, so it is
    // interpolated on the same log-magnification axis the zoom sweeps;
    // geometric interpolation, because the table falls geometrically.
    //
    // The position is found by BRACKETING the displayed magnification
    // between two objectives rather than by mapping the whole ×40..×400
    // span onto 0..2. That matters: ×4/×10/×40 are not evenly spaced in
    // log, so the even mapping lands on 0.80 at a settled ×100, and the
    // canvas would then draw with a 0.048 mm depth of field and a 7.96
    // unit focus shift while the readout below it reported 0.040 mm and
    // 10. Bracketing lands exactly on an integer at every settled
    // magnification, so what is drawn and what is written are the same
    // instrument — which is the whole reason this table exists.
    function viewPos() {
      var m = state.dispMag, i, a, b;
      if (m <= EYEPIECE * OBJECTIVES[0]) { return 0; }
      for (i = 1; i < OBJECTIVES.length; i++) {
        a = EYEPIECE * OBJECTIVES[i - 1];
        b = EYEPIECE * OBJECTIVES[i];
        if (m <= b) { return (i - 1) + Math.log(m / a) / Math.log(b / a); }
      }
      return OBJECTIVES.length - 1;
    }
    function viewDofMM() {
      var pos = viewPos(), i = Math.floor(pos), f = pos - i;
      var j = Math.min(i + 1, OBJ_DOF_MM.length - 1);
      return Math.exp(Math.log(OBJ_DOF_MM[i])
                      + (Math.log(OBJ_DOF_MM[j]) - Math.log(OBJ_DOF_MM[i])) * f);
    }
    function viewOffMM(depthMM) {
      var pos = viewPos(), i = Math.floor(pos), f = pos - i;
      var j = Math.min(i + 1, OBJ_FOCUS_SHIFT.length - 1);
      var shift = OBJ_FOCUS_SHIFT[i] + (OBJ_FOCUS_SHIFT[j] - OBJ_FOCUS_SHIFT[i]) * f;
      return Math.abs(focusMM(state.focus + shift) - depthMM);
    }
    function fovText() {
      var f = fovMM();
      return (f >= 1 ? String(Math.round(f * 10) / 10) : f.toFixed(2)) + " mm";
    }
    function kindNow() { return specimenKind(specimens[state.slide]); }

    // ── drawing ──
    var canFilter = typeof ctx.filter === "string";

    // Blur in px. Design tuned cap and factor per specimen — a bacterium
    // two pixels wide cannot carry an 11px blur — so both travel with the
    // payload rather than being one engine constant.
    function blurPx(off, dof, cap, factor) {
      var b = (off / dof) * factor;
      return b > cap ? cap : b;
    }

    // The four blur laws, verbatim from Design's approved pages:
    //   onion layers   D2 line 683 — cap 9,  factor 3.2
    //   cheek cells    D6 line 872 — cap 8,  factor 2.6
    //   pond organisms D6 line 851 — cap 11, factor 3.0
    //   bacteria       D6 line 836 — cap 6,  factor 2.2
    // All four survive rather than one winning, because these are
    // RENDERING choices about a drawing, not claims about optics. The
    // optics are the one table above, and there is only ever one of those.
    var BLUR_ONION = { cap: 9, factor: 3.2 };
    var BLUR_CHEEK = { cap: 8, factor: 2.6 };
    var BLUR_POND = { cap: 11, factor: 3.0 };
    var BLUR_BACTERIA = { cap: 6, factor: 2.2 };

    function layer(blur, paint) {
      // A blurred layer is DRAWN blurred — the mechanism has to be
      // visible, not narrated only. Where canvas filters are missing
      // (very old WebKit) the layer fades instead: less honest about
      // optics, still unmistakably "not sharp".
      ctx.save();
      if (blur > 0.05) {
        if (canFilter) { ctx.filter = "blur(" + blur.toFixed(2) + "px)"; }
        else {
          var a = 1 - blur / 12;
          ctx.globalAlpha = a < 0.25 ? 0.25 : a;
        }
      }
      paint();
      ctx.restore();
    }

    function roundRectPath(x, y, w, h, r) {
      ctx.beginPath();
      ctx.moveTo(x + r, y);
      ctx.lineTo(x + w - r, y);
      ctx.quadraticCurveTo(x + w, y, x + w, y + r);
      ctx.lineTo(x + w, y + h - r);
      ctx.quadraticCurveTo(x + w, y + h, x + w - r, y + h);
      ctx.lineTo(x + r, y + h);
      ctx.quadraticCurveTo(x, y + h, x, y + h - r);
      ctx.lineTo(x, y + r);
      ctx.quadraticCurveTo(x, y, x + r, y);
      ctx.closePath();
    }

    /* ── RENDERER 1 of 2 · tessellation with N layers ──────────────────
       Drives onion (N=3), cheek (N=1), and the bed of onion tissue under
       the bubbles. Walks the payload's layers[], takes each layer's blur
       from its OWN depth, and hands a tiler the job of covering the field.
       `par` is the parallax index: −1 / 0 / +1 for three layers (D2's
       `li - 1`), 0 for one, so a single-layer payload sits square. */
    function drawTessellation(ppm, payload, tile, law) {
      var layers = payload && payload.layers;
      if (!layers || !layers.length) { return; }
      var dof = viewDofMM(), mid = (layers.length - 1) / 2;
      layers.forEach(function (lay, li) {
        var blur = blurPx(viewOffMM(lay.depth), dof, law.cap, law.factor);
        layer(blur, function () {
          if (lay.alpha !== undefined) { ctx.globalAlpha *= lay.alpha; }
          tile(ppm, lay, li, li - mid);
        });
      });
    }

    /* ── RENDERER 2 of 2 · scatter with per-item depth ─────────────────
       Drives the pond (organisms and bacteria, two passes with two laws)
       and the bubbles. Walks a list whose every item carries its own
       depth, and blurs each one independently — which is what makes a wet
       mount read as a volume of water rather than a picture of one. */
    function drawScatter(ppm, items, law, paint) {
      if (!items || !items.length) { return; }
      var dof = viewDofMM();
      items.forEach(function (it) {
        var blur = blurPx(viewOffMM(it.depth), dof, law.cap, law.factor);
        layer(blur, function () { paint(it, ppm); });
      });
    }

    // D2 lines 690-715, verbatim: the rounded-rect cell, the one-in-four
    // nucleus, and the per-layer parallax that makes three layers read as
    // three DEPTHS instead of one thicker drawing.
    function tileOnion(ppm, lay, li, par) {
      var fov = FIELD_AT_1X_MM / state.dispMag;
      var cols = Math.ceil(fov / CELL_W) + 3;
      var rows = Math.ceil(fov / CELL_H) + 3;
      var w = CELL_W * ppm, h = CELL_H * ppm;
      var rad = Math.min(w, h) * 0.28;
      var r, q, x, y, stagger;
      ctx.lineWidth = Math.max(1.2, ppm * 0.006);
      ctx.strokeStyle = lay.stroke || ink;
      for (r = -1; r < rows; r++) {
        for (q = -1; q < cols; q++) {
          stagger = (r % 2 === 0 ? 0 : CELL_W * 0.5) + par * CELL_W * 0.22;
          x = CX - FIELD_R + (q * CELL_W + stagger) * ppm;
          y = CY - FIELD_R + (r * CELL_H + par * CELL_H * 0.3) * ppm;
          roundRectPath(x, y, w, h, rad);
          ctx.stroke();
          if ((q + r * 3 + li) % 4 === 0) {
            // A thin section cuts through some nuclei and misses others,
            // so Design draws roughly one cell in four with one.
            ctx.beginPath();
            ctx.fillStyle = ONION_NUCLEUS;
            ctx.arc(x + w * 0.42, y + h * 0.5,
                    Math.max(1.5, h * 0.2), 0, Math.PI * 2);
            ctx.fill();
          }
        }
      }
    }

    // D6 lines 862-877, verbatim, with one change: this engine clips to
    // the field CIRCLE, so cells are culled against that circle instead of
    // against D6's canvas box. Identical image inside the clip, about a
    // fifth of the work at ×40 — and this engine, unlike D6's page,
    // re-tiles on every frame of the zoom transition.
    function tileCheek(ppm) {
      var step = CHEEK_D * ppm * 1.04;
      var n = Math.ceil((FIELD_R * 2) / step) + 2;
      var px = CHEEK_D * ppm, detail = detailAt(px);
      var lim = FIELD_R + step, i, j, x, y, dx, dy;
      for (i = -n; i <= n; i++) {
        for (j = -n; j <= n; j++) {
          x = CX + i * step + ((j % 2) ? step * 0.5 : 0);
          y = CY + j * step * 0.88;
          dx = x - CX; dy = y - CY;
          if (dx * dx + dy * dy > lim * lim) { continue; }
          ctx.save();
          ctx.translate(x, y);
          drawCheekCell(px, (i * 3 + j * 7) % 6, detail);
          ctx.restore();
        }
      }
    }

    // This engine's own cheek cell — theme tokens, R3-safe — resized onto
    // D6's tessellation: px across, a per-cell variant for the wobble, and
    // the nucleus behind the detail gate so nothing fine is drawn at a
    // size where it could only be a smudge.
    function drawCheekCell(px, variant, detail) {
      var R = px / 2, k, a, rr;
      ctx.beginPath();
      for (k = 0; k <= 10; k++) {
        a = variant + (k / 10) * Math.PI * 2;
        rr = R * (0.85 + 0.15 * Math.sin(a * 3 + variant));
        if (k === 0) { ctx.moveTo(rr * Math.cos(a), rr * Math.sin(a)); }
        else { ctx.lineTo(rr * Math.cos(a), rr * Math.sin(a)); }
      }
      ctx.closePath();
      ctx.fillStyle = card;
      ctx.fill();
      ctx.lineWidth = Math.max(1.1, px * 0.026);
      ctx.strokeStyle = muted;
      ctx.stroke();
      if (!detail) { return; }
      ctx.beginPath();
      ctx.arc(0, 0, Math.max(1.2, R * 0.22), 0, Math.PI * 2);
      ctx.fillStyle = ink;
      ctx.fill();
    }

    // D6 lines 830-844, verbatim. 0.002 mm: two pixels of nothing at every
    // magnification this microscope has, which is exactly the point. The
    // rod branch is Design's and is kept as drawn, though no objective
    // here reaches the 2.6 px it needs.
    function drawBacterium(b, ppm) {
      // G10 — the field is a WINDOW on the slide, so panning subtracts the
      // centre here rather than translating the context: the cull below has
      // to test where the dot really lands, or panning would drop the ones
      // that just came into view.
      var c = centreMM();
      var x = CX + (b.x - c.x) * ppm, y = CY + (b.y - c.y) * ppm;
      if (x < -20 || x > W + 20 || y < -20 || y > H + 20) { return; }
      var px = Math.max(0.6, 0.002 * ppm);
      ctx.save();
      // D6 sets alpha outright; multiplying instead keeps the no-filter
      // fallback's fade from being thrown away.
      ctx.globalAlpha *= 0.8;
      ctx.translate(x, y);
      ctx.rotate(b.rot);
      if (px < 2.6) {
        ctx.beginPath();
        ctx.arc(0, 0, Math.max(0.7, px), 0, Math.PI * 2);
        ctx.fillStyle = BACT_DOT;
        ctx.fill();
      } else {
        roundRectPath(-px / 2, -px * 0.2, px, px * 0.4, px * 0.2);
        ctx.fillStyle = BACT_ROD;
        ctx.fill();
      }
      ctx.restore();
    }

    // This engine's own organisms, sized from the payload's `len` in mm
    // and gated by D6's detail rule, so cilia, eyespot, flagellum, oral
    // groove and vacuoles only draw when the organism is big enough for
    // them to mean anything. Below the gate you get an outline that moves,
    // which is the honest ×40 and ×100 view and is what D6's own RESOLVE
    // copy promises.
    function drawOrganism(p, ppm) {
      var px = p.len * ppm;
      var c = centreMM();
      var x = CX + (p.x - c.x) * ppm, y = CY + (p.y - c.y) * ppm, k;
      if (x < -px || x > W + px || y < -px || y > H + px) { return; }
      var detail = detailAt(px);
      ctx.save();
      ctx.translate(x, y);
      ctx.rotate(p.hdg);
      if (p.kind === "euglena") {
        var eL = px, eW = px * 0.35;
        ctx.beginPath();
        ctx.ellipse(0, 0, eL / 2, eW / 2, 0, 0, Math.PI * 2);
        ctx.fillStyle = bio;
        ctx.fill();
        ctx.lineWidth = Math.max(1, px * 0.020);
        ctx.strokeStyle = ink;
        ctx.stroke();
        if (detail) {
          ctx.beginPath();             // the eyespot, at the front
          ctx.arc(eL * 0.32, 0, Math.max(1.2, eW * 0.16), 0, Math.PI * 2);
          ctx.fillStyle = accent;
          ctx.fill();
          ctx.beginPath();             // the flagellum, beating ahead
          ctx.moveTo(eL / 2, 0);
          for (k = 1; k <= 8; k++) {
            ctx.lineTo(eL / 2 + k * eL * 0.09,
                       Math.sin(k * 1.1 + p.phase * 9) * eW * 0.3);
          }
          ctx.lineWidth = Math.max(1, eW * 0.08);
          ctx.strokeStyle = ink;
          ctx.stroke();
        }
      } else if (p.kind === "paramecium") {
        var pL = px, pW = px * 0.389;
        ctx.beginPath();
        ctx.ellipse(0, 0, pL / 2, pW / 2, 0, 0, Math.PI * 2);
        ctx.fillStyle = card;
        ctx.fill();
        ctx.lineWidth = Math.max(1, pW * 0.05);
        ctx.strokeStyle = ink;
        ctx.stroke();
        if (detail) {
          for (k = 0; k < 26; k++) {   // cilia all round, mid-beat
            var a = (k / 26) * Math.PI * 2;
            var cx1 = Math.cos(a) * pL / 2, cy1 = Math.sin(a) * pW / 2;
            var tick = 1 + 0.35 * Math.sin(k + p.phase * 14);
            ctx.beginPath();
            ctx.moveTo(cx1, cy1);
            ctx.lineTo(cx1 * (1 + 0.10 * tick), cy1 * (1 + 0.22 * tick));
            ctx.stroke();
          }
          ctx.beginPath();             // oral groove
          ctx.arc(-pL * 0.1, pW * 0.16, pW * 0.16, 0.3, Math.PI - 0.3);
          ctx.stroke();
          for (k = 0; k < 2; k++) {    // contractile vacuoles
            ctx.beginPath();
            ctx.arc((k ? 1 : -1) * pL * 0.28, 0, pW * 0.13, 0, Math.PI * 2);
            ctx.strokeStyle = muted;
            ctx.stroke();
            ctx.strokeStyle = ink;
          }
        }
      } else {                         // amoeba
        var aR = px / 2;
        ctx.beginPath();
        for (k = 0; k <= 14; k++) {
          var aa = (k / 14) * Math.PI * 2;
          var rr = aR * (0.7 + 0.3 * Math.sin(aa * 3 + p.phase));
          if (k === 0) { ctx.moveTo(rr * Math.cos(aa), rr * Math.sin(aa)); }
          else { ctx.lineTo(rr * Math.cos(aa), rr * Math.sin(aa)); }
        }
        ctx.closePath();
        ctx.fillStyle = band;
        ctx.fill();
        ctx.lineWidth = Math.max(1.2, aR * 0.04);
        ctx.strokeStyle = ink;
        ctx.stroke();
        if (detail) {
          ctx.beginPath();
          ctx.arc(0, 0, Math.max(1.5, aR * 0.16), 0, Math.PI * 2);
          ctx.fillStyle = muted;
          ctx.fill();
        }
      }
      ctx.restore();
    }

    function drawBubble(b, ppm) {
      var c = centreMM();
      var x = CX + (b.x - c.x) * ppm, y = CY + (b.y - c.y) * ppm;
      var r = (b.d / 2) * ppm;
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
      var kn = kindNow(), p = state.content;
      if (kn === "onion") {
        drawTessellation(ppm, p, tileOnion, BLUR_ONION);
      } else if (kn === "cheek") {
        drawTessellation(ppm, p, tileCheek, BLUR_CHEEK);
      } else if (kn === "bubbles") {
        drawTessellation(ppm, p, tileOnion, BLUR_ONION);
        // The bubbles are furniture on an onion slide, so they take the
        // onion's law; Design has no bubble slide to have tuned one.
        drawScatter(ppm, p.bubbles, BLUR_ONION, drawBubble);
      } else if (kn === "pond") {
        drawScatter(ppm, p.bacteria, BLUR_BACTERIA, drawBacterium);
        drawScatter(ppm, p.organisms, BLUR_POND, drawOrganism);
      }
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

    function inViewOrganisms() {
      var half = fovMM() / 2, out = [], c = centreMM();
      // Measured from where the FIELD is, not from the origin: pan to the
      // blob and the readout has to be about the blob's neighbourhood.
      (state.content.organisms || []).forEach(function (s) {
        var dx = s.x - c.x, dy = s.y - c.y;
        if (Math.sqrt(dx * dx + dy * dy) < half + 0.05) { out.push(s); }
      });
      return out;
    }

    var SWIMMER_WORDS = {
      euglena: "a Euglena — green, with a whip to swim with and an orange eyespot",
      paramecium: "a Paramecium — a slipper shape covered in beating cilia",
      amoeba: "an Amoeba — a slow grey blob pushing out pseudopods"
    };

    // D6's nicknames, for the "in focus" line — the words a student would
    // actually use at the bench before they have the Latin.
    var ORG_NICKNAME = {
      amoeba: "the blob",
      paramecium: "the slipper",
      euglena: "the green spindle"
    };

    // D6's two verbatim notes. They are the sentences that make the
    // contrast between the two slides land, so they are reproduced exactly.
    var BACTERIA_NOTE = " The dots scattered between them are bacteria, "
      + "about 0.002 mm long. Even at ×400 they are two pixels of nothing — "
      + "you can see that they are there, not what they are. Every organism "
      + "on this slide is doing all seven life processes for itself.";
    var SMEAR_NOTE = " One layer, one shape, no movement. Racking the focus "
      + "finds nothing behind them, because a smear is a sheet. Every cell "
      + "here does one job, and none of them is an organism.";

    // G9 — a mount may bring its own note, and B1-06's two are these two
    // sentences verbatim. Reading the payload rather than the constant is
    // what stops the pair drifting: one of them is the lesson's, and the
    // lesson is the one that can be re-authored.
    function mountNote(fallback) {
      var n = mountNow().note;
      return n ? " " + n : fallback;
    }

    // The lesson answering its own gate, keyed by TOTAL magnification and
    // live-switched with the turret. Absent on every instrument that does
    // not author it, so nothing else gains a sentence.
    function resolveNote() {
      var n = RESOLVE && RESOLVE[String(mag())];
      return n ? " What you can resolve: " + n : "";
    }

    function dofText() {
      var d = dofMM();
      return (d >= 0.1 ? d.toFixed(2) : d.toFixed(3)) + " mm";
    }

    // How many cells fit across the view: 600 / magnification for the
    // onion (15 · 6 · 1½) and 3000 / magnification for a cheek smear
    // (75 · 30 · 7½). The ×400 figure is a HALF, and D2's recording table
    // prints it as "1½" — so the readout has to say a half too. A student
    // who copies "2" out of the readout into a table that wants 1½ has
    // been misled by us, and this whole ticket exists to stop the engine
    // and the approved page saying different things.
    function cellsAcross(cellMm) {
      var v = fovMM() / cellMm, whole = Math.floor(v);
      if (Math.abs(v - whole - 0.5) < 0.01) {
        return (whole ? String(whole) : "") + "½";
      }
      return String(Math.round(v));
    }

    function whatYouSee() {
      var kn = kindNow(), ppm = (FIELD_R * 2) / fovMM();
      if (kn === "onion") {
        var layers = state.content.layers || [];
        var nSharp = 0;
        layers.forEach(function (l) { if (isSharp(l.depth)) { nSharp++; } });
        // Band the sentence on the layer NEAREST the focal plane, not on the
        // middle one. Keying it to the middle layer let the readout say "a
        // bright blur, nothing sharp" in the same breath as "1 of the 3 layers
        // is inside the depth of field", whenever an OUTER layer was the one in
        // focus — which at ×40 is most of the wheel. What the student sees is
        // whichever layer is closest to sharp, wherever it sits in the stack.
        var midL = layers[0] || { depth: 0 };
        layers.forEach(function (l) {
          if (offMM(l.depth) < offMM(midL.depth)) { midL = l; }
        });
        // How many layers hold at once is COMPUTED, never asserted: it is
        // the depth of field doing its work, and at ×400 it is the whole
        // reason the highest lens is not the best one.
        var depthNote = " " + (nSharp === layers.length
          ? "All " + layers.length + " layers are inside the depth of field "
            + "at once — at ×" + mag() + " that is " + dofText()
            + ", deeper than the layers are apart."
          : (nSharp === 0
            ? "None of the " + layers.length + " layers is inside the depth "
              + "of field — at ×" + mag() + " that is only " + dofText()
              + " deep."
            : "Only " + nSharp + " of the " + layers.length + " layers "
              + (nSharp === 1 ? "is" : "are") + " inside the depth of field — "
              + "at ×" + mag() + " that is only " + dofText() + " deep, so "
              + "the rest sit outside it."));
        if (isSharp(midL.depth)) {
          return (fovMM() / CELL_W < 1
            ? "A single onion cell more than fills the view — straight sides, "
              + "part of a row."
            : "About " + cellsAcross(CELL_W) + " onion cells fit across the "
              + "view — straight sides, packed in rows like bricks.")
            + (CELL_W * ppm > 22
               ? " Some of them show a small dark nucleus." : "")
            + depthNote;
        }
        if (offMM(midL.depth) < 2 * sharpWindowMM()) {
          return "The rows are there, but soft — turn the focus until the "
            + "cell walls come sharp." + depthNote;
        }
        return "A bright blur, nothing sharp. The focus is nowhere near the "
          + "specimen — turn it slowly and watch." + depthNote;
      }
      if (kn === "bubbles") {
        var bD = state.content.bubbleDepth, oD = state.content.onionDepth;
        if (isSharp(bD)) {
          return "Perfectly round circles with a thick dark rim, floating "
            + "apart from each other. They look like cells; they are air "
            + "bubbles, trapped when the coverslip was dropped flat"
            + (offMM(oD) > 2 * sharpWindowMM()
               ? " — and the onion cells are a blur underneath." : ".");
        }
        if (isSharp(oD)) {
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
            + "small to make anything out at ×" + mag() + "." + mountNote(SMEAR_NOTE);
        }
        var sheet = (state.content.layers || [{ depth: 0 }])[0];
        if (isSharp(sheet.depth)) {
          return "About " + cellsAcross(CHEEK_D) + " cheek cells fit across "
            + "the view — soft, rounded, tessellated edge to edge with no gaps"
            + (detailAt(CHEEK_D * ppm) ? ", each with a darker nucleus" : "")
            + "." + mountNote(SMEAR_NOTE);
        }
        return "Rounded shadows in the view, none sharp — bring the focus "
          + "through the smear slowly." + mountNote(SMEAR_NOTE);
      }
      if (kn === "pond") {
        var vis = inViewOrganisms();
        if (!vis.length) {
          return "Empty water just now. At ×" + mag() + " the view is only "
            + fovText() + " wide — drop back to ×40 to find something, "
            + "then work up." + mountNote(BACTERIA_NOTE);
        }
        // Same honesty rule the cheek slide runs on: do not name a feature
        // the drawing is too small to show. The biggest thing here is a
        // Paramecium at 0.25 mm, which is 11 pixels across a ×40 field — a
        // moving speck, and saying so IS the lesson. It resolves from ×100.
        var biggest = 0;
        vis.forEach(function (sw) {
          var p = sw.len * ppm;
          if (p > biggest) { biggest = p; }
        });
        if (biggest < 14) {
          return vis.length + " tiny specks drifting and darting about the "
            + "view — alive, clearly, but far too small at ×" + mag()
            + " to tell what any of them is. Found something? Turn the "
            + "magnification up." + mountNote(BACTERIA_NOTE);
        }
        var bits = [], anyBlur = false, focusSet = [];
        vis.forEach(function (sw) {
          var sh = isSharp(sw.depth);
          if (!sh) { anyBlur = true; }
          bits.push(SWIMMER_WORDS[sw.kind]
                    + (sh ? " (sharp)" : " (a blur at another depth)"));
          if (sh && focusSet.indexOf(ORG_NICKNAME[sw.kind]) < 0) {
            focusSet.push(ORG_NICKNAME[sw.kind]);
          }
        });
        return "In view: " + bits.join("; ") + "."
          + (anyBlur ? " The water is deeper than the lens can focus — "
                       + "layers come sharp in turn." : "")
          + " In focus: "
          + (focusSet.length ? focusSet.join(", ") : "nothing sharp") + "."
          + (mag() === 400 && vis.some(function (sw) { return sw.kind === "paramecium"; })
             ? " The Paramecium will not stay long: at ×400 it crosses the "
               + "whole view in under a second."
             : "")
          + mountNote(BACTERIA_NOTE);
      }
      return "";
    }

    function report() {
      say("Total magnification ×" + mag() + " · field of view " + fovText()
          + ". " + whatYouSee() + resolveNote());
    }

    // ── motion ──
    function stepOrganisms(dt) {
      if (kindNow() !== "pond") { return; }
      // G11 — the student's own stillness switch, on top of the OS's. With
      // it off the cilia stop, the vacuoles freeze and the Euglena stops
      // bending: the drawing is complete, just still.
      if (!state.motion) { return; }
      (state.content.organisms || []).forEach(function (s) {
        s.phase += dt * (s.kind === "paramecium" ? 3 : 1);
        // F33 — with a centre control the cast is held and the SLIDE moves.
        // Everything above this line is life in place; everything below is
        // travel, and travel is what the page's own caption denies.
        if (pinned()) { return; }
        if (Math.random() < (s.kind === "amoeba" ? 0.002 : 0.02)) {
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
      return (kindNow() === "pond" && state.motion)
        || Math.abs(state.dispMag - mag()) > 0.5;
    }
    function loop(now) {
      if (!state.running) { return; }
      var dt = state.last ? Math.min(50, now - state.last) / 1000 : 0.016;
      state.last = now;
      stepOrganisms(dt);
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
      // Organisms swim in and out of view, so — like diffusion's crossing
      // counts — this one readout re-reads on a cadence. A PINNED mount has
      // no such churn: the cast is where the student left it and the
      // readout only changes when a control does, so re-reading it would be
      // noise on a line a screen reader is announcing.
      if (kindNow() === "pond" && !pinned() && state.motion) {
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
      for (i = 0; i < SETTLE_STEPS; i++) { stepOrganisms(1 / 60); }
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
    var captionEl = sim.querySelector(".ks3-sim-caption");
    var declared = (sim.getAttribute("data-controls") || "").split(",")
      .map(function (s) { return s.trim(); })
      .filter(function (s) { return s; });
    var wraps = {};                   // control name -> its rendered wrapper
    var centreBtns = [], motionBtn = null;

    /* G9 — the three strings that switch WITH the slide. Design authored a
       caption and an aria-label per mount because they say different things
       about different slides; one per instrument would be wrong for both. */
    function syncMount() {
      var m = mountNow();
      if (captionEl && m.caption) { captionEl.textContent = m.caption; }
      if (m.alt) { canvas.setAttribute("aria-label", m.alt); }
    }

    // The wrapper that should follow `name`, so a control removed and put
    // back lands where it was declared rather than on the end of the row.
    function nextWrapAfter(name) {
      var i = declared.indexOf(name), j;
      for (j = i + 1; j < declared.length; j++) {
        var w = wraps[declared[j]];
        if (w && w.parentNode === controls) { return w; }
      }
      return null;
    }

    /* G10 — the centre group is offered PER MOUNT, and where it is not
       offered it is removed from the DOM rather than disabled. Same
       discipline as R5's gate: a control the student cannot use is not
       drawn, because a dead button is a promise the instrument breaks. On
       B1-06 that is four control groups on the pond and three on the cheek
       smear, exactly as the approved page measures. */
    function syncCentre() {
      var w = wraps.centre;
      if (!w) { return; }
      if (centresHere()) {
        if (w.parentNode !== controls) {
          controls.insertBefore(w, nextWrapAfter("centre"));
        }
        paintCentre();
      } else if (w.parentNode === controls) {
        controls.removeChild(w);
      }
    }

    function paintCentre() {
      var c = effectiveCentre();
      centreBtns.forEach(function (b) {
        b.setAttribute("aria-pressed",
                       (c && b.getAttribute("data-centre") === c.id)
                         ? "true" : "false");
      });
    }

    function paintMotion() {
      if (!motionBtn) { return; }
      var words = (MOTION && MOTION.labels) || ["Swimming", "Held still"];
      // The button says what the slide IS doing, which is Design's own
      // wording rule, and `aria-pressed` carries the same fact for anyone
      // who cannot see which of the two is lit.
      motionBtn.textContent = state.motion ? words[0] : words[1];
      motionBtn.setAttribute("aria-pressed", state.motion ? "true" : "false");
    }

    if (controls) {
      declared.forEach(function (name) {
        var shell, input;
        if (name === "specimen") {
          shell = controlShell(name, CAPTIONS[name]);
          if (!shell) { return; }
          input = document.createElement("select");
          input.id = shell.id;
          mounts.forEach(function (m, i) {
            var opt = document.createElement("option");
            opt.value = String(i);
            opt.textContent = m.label;
            input.appendChild(opt);
          });
          input.value = String(state.slide);
          input.addEventListener("change", function () {
            state.slide = Number(input.value);
            state.content = buildContent(kindNow(), mountNow());
            syncMount();
            syncCentre();
            afterControlChange();
          });
          shell.wrap.appendChild(input);
          wraps[name] = shell.wrap;
          controls.appendChild(shell.wrap);
        } else if (name === "centre") {
          if (!BENCH_CENTRES.length) { return; }
          shell = segShell(name, CAPTIONS[name]);
          if (!shell) { return; }
          BENCH_CENTRES.forEach(function (c) {
            var btn = segButton(c.label, false);
            btn.setAttribute("data-centre", c.id);
            btn.addEventListener("click", function () {
              // Panning is a pure translation of the field. It moves the
              // SLIDE and nothing else — in particular it does not touch
              // the wheel, so the readout can go on naming a different
              // organism as the one in focus. That is the lesson: centring
              // and focusing are two operations and the bench makes the
              // student do both.
              state.centre = c.id;
              paintCentre();
              afterControlChange();
            });
            centreBtns.push(btn);
            shell.row.appendChild(btn);
          });
          wraps[name] = shell.wrap;
          controls.appendChild(shell.wrap);
        } else if (name === "motion") {
          shell = segShell(name, CAPTIONS[name]);
          if (!shell) { return; }
          motionBtn = segButton("", state.motion);
          motionBtn.addEventListener("click", function () {
            state.motion = !state.motion;
            paintMotion();
            // Coming back to life needs the loop restarted: `animating()`
            // is false while the mount is still, so the frame that was
            // painted last is the frame that stays.
            if (state.motion && !REDUCED
                && sim.getAttribute("data-locked") !== "1") {
              start();
            }
            afterControlChange();
          });
          shell.row.appendChild(motionBtn);
          paintMotion();
          wraps[name] = shell.wrap;
          controls.appendChild(shell.wrap);
        } else if (name === "magnification") {
          shell = controlShell(name, CAPTIONS[name]);
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
          wraps[name] = shell.wrap;
          controls.appendChild(shell.wrap);
        } else if (name === "focus") {
          shell = controlShell(name, CAPTIONS[name]);
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
          wraps[name] = shell.wrap;
          controls.appendChild(shell.wrap);
        }
      });
    }

    // The opening mount may be one that offers no centre control, so the
    // group's presence is settled from the state and not from the order the
    // controls happened to be built in.
    syncMount();
    syncCentre();

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

  /* ═══════════════════════════════════════════════════════════════
     CLASSIFY's two instruments — the seven-tests board and the
     three-way sorter.

     `build_ks3.py` has emitted their markup since B1 round two, and there
     was **no CSS for any of their 44 classes and no JS for any of their
     13 `data-*` attributes**. The kinds gate passed them because it reads
     the dispatch table, and a dispatch-table entry is not a component.

     What a student actually got was `<ul class="ks3-lamps">` as a bullet
     list of bare default buttons that did nothing when tapped. Both of
     these set `data-stage-done` themselves, because an instrument knows
     what finished means and the rail does not (MRB-208).
     ═══════════════════════════════════════════════════════════════ */

  function markStage(sec, done) {
    if (sec) { sec.setAttribute("data-stage-done", done ? "1" : "0"); }
  }

  function wireBoard(sec) {
    var tabs = toArray(sec.querySelectorAll(".ks3-tab"));
    var panels = toArray(sec.querySelectorAll(".ks3-board-panel"));
    if (!panels.length) { return; }

    // All four panels are in the document and only one is shown, so each
    // specimen's progress is independent with no state to keep — the DOM is
    // the state, and switching back shows a panel exactly as it was left.
    function show(id) {
      each(tabs, function (tab) {
        tab.setAttribute("aria-pressed",
          tab.getAttribute("data-specimen") === id ? "true" : "false");
      });
      each(panels, function (p) {
        setHidden(p, p.getAttribute("data-specimen") !== id);
      });
    }
    each(tabs, function (tab) {
      tab.addEventListener("click", function () {
        show(tab.getAttribute("data-specimen"));
      });
    });

    // ⚖️ The stage is done when EVERY specimen has had all its tests run.
    // Design's own `boardComplete` is per-specimen and gates that panel's
    // verdict, which is right for the verdict and wrong for the rail: the
    // instrument's argument is the COMPARISON — the candle scores 6 and is
    // dead, the seed scores 3 and is alive — and `r_test_board` refuses a
    // one-specimen board in as many words, because "a board with one
    // specimen teaches that a score settles it, which is the misconception
    // it exists to break". One specimen tested is half a lesson. The rail
    // stop is `all_tests_run` with no threshold, and the eyebrow Design
    // wrote is "Your turn · test four things".
    function refreshStage() {
      var whole = true;
      each(panels, function (p) {
        var lamps = p.querySelectorAll(".ks3-lamp");
        for (var i = 0; i < lamps.length; i++) {
          if (!lamps[i].hasAttribute("data-state")) { whole = false; return; }
        }
      });
      markStage(sec, whole);
    }

    each(panels, function (panel) {
      var tests = panel.querySelector("[data-board-tests]");
      var gate = toArray(panel.querySelectorAll(".ks3-board-predict .ks3-option"));
      var lamps = toArray(panel.querySelectorAll(".ks3-lamp"));
      var tally = panel.querySelector("[data-board-tally]");
      var instruction = panel.querySelector("[data-board-instruction]");
      var verdict = panel.querySelector(".ks3-board-verdict");

      // Law 4, per panel: this specimen's prediction opens this specimen's
      // board. The choice stays changeable and never disables — R3's runtime
      // assertion fails an activity option that is disabled, and fails a
      // group whose options do not all render alike, which a one-way gate
      // produces the moment its unchosen sibling stays resting.
      each(gate, function (btn) {
        btn.addEventListener("click", function () {
          each(gate, function (b) { b.setAttribute("aria-pressed", "false"); });
          btn.setAttribute("aria-pressed", "true");
          if (tests && tests.hasAttribute("hidden")) {
            setHidden(tests, false);
            tests.setAttribute("role", "status");
          }
        });
      });

      function repaint() {
        var run = 0, lit = 0;
        each(lamps, function (l) {
          if (!l.hasAttribute("data-state")) { return; }
          run += 1;
          if (l.getAttribute("data-state") === "yes") { lit += 1; }
        });
        if (tally) {
          tally.textContent = lit + " of " + lamps.length + " lit";
        }
        if (run === lamps.length) {
          if (instruction) { instruction.textContent = "All seven tested."; }
          if (verdict && verdict.hasAttribute("hidden")) {
            setHidden(verdict, false);
            verdict.setAttribute("role", "status");
          }
        }
        refreshStage();
      }

      each(lamps, function (lamp) {
        lamp.addEventListener("click", function () {
          // A test is run once. Re-tapping must not un-run it: the finding
          // is a property of the specimen, not a toggle the student owns.
          if (lamp.hasAttribute("data-state")) { return; }
          var yes = lamp.getAttribute("data-yes") === "1";
          lamp.setAttribute("data-state", yes ? "yes" : "no");
          lamp.setAttribute("aria-pressed", "true");
          var word = lamp.querySelector("[data-lamp-verdict]");
          if (word) { word.textContent = yes ? "Yes" : "No"; }
          repaint();
        });
      });

      repaint();
    });

    if (panels.length) {
      show(panels[0].getAttribute("data-specimen"));
    }
  }

  function wireSort(sec) {
    var rows = toArray(sec.querySelectorAll(".ks3-sortrow"));
    var btn = sec.querySelector("[data-sort-reveal]");
    var progress = sec.querySelector("[data-sort-progress]");
    var selfcheck = sec.querySelector("[data-selfcheck]");
    if (!rows.length) { return; }

    var total = rows.length;
    var word = (progress && progress.getAttribute("data-total-word")) || String(total);

    function sortedCount() {
      var n = 0;
      each(rows, function (row) {
        if (row.querySelector('.ks3-sort-chip[aria-pressed="true"]')) { n += 1; }
      });
      return n;
    }

    function repaint() {
      var n = sortedCount();
      each(rows, function (row) {
        var on = !!row.querySelector('.ks3-sort-chip[aria-pressed="true"]');
        row.setAttribute("data-sorted", on ? "1" : "0");
      });
      if (progress) {
        progress.textContent = n < total
          ? n + " of " + total + " sorted"
          : "All " + word + " sorted";
      }
      if (btn) {
        if (n < total) { btn.setAttribute("disabled", ""); }
        else { btn.removeAttribute("disabled"); }
      }
    }

    each(rows, function (row) {
      var chips = toArray(row.querySelectorAll(".ks3-sort-chip"));
      each(chips, function (chip) {
        chip.addEventListener("click", function () {
          // Freely changeable until the reveal, and changeable after it too:
          // nothing here marks anybody, so there is nothing to protect.
          each(chips, function (c) { c.setAttribute("aria-pressed", "false"); });
          chip.setAttribute("aria-pressed", "true");
          repaint();
        });
      });
    });

    if (btn) {
      btn.addEventListener("click", function () {
        if (sortedCount() < total) { return; }
        // The evidence lands on all rows at once. R3: after the reveal a
        // wrong row is pixel-identical to a right one — the page says what
        // settles each item and never whether the student had it.
        each(rows, function (row) {
          setHidden(row.querySelector("[data-reveal]"), false);
        });
        btn.setAttribute("aria-expanded", "true");
        // MRB-196's self-check arrives only now, because before the evidence
        // is showing there is nothing to compare an answer against.
        if (selfcheck) {
          setHidden(selfcheck, false);
          selfcheck.setAttribute("role", "status");
        }
        markStage(sec, true);
      });
    }

    // The self-check's options mark nothing and gate nothing; they are a
    // commitment the student makes to themselves. `wirePredictions` skips
    // this whole section, so they are wired here.
    if (selfcheck) {
      var scOpts = toArray(selfcheck.querySelectorAll(".ks3-option"));
      each(scOpts, function (o) {
        o.addEventListener("click", function () {
          each(scOpts, function (b) { b.setAttribute("aria-pressed", "false"); });
          o.setAttribute("aria-pressed", "true");
        });
      });
    }

    repaint();
  }

  /* R7 / Law 9 — the Motion switch. Motion carries meaning here (a flame
     flickers and gives off soot, which is half the argument the hook makes),
     so it cannot simply be deleted for everyone. It gets a control instead,
     and the OS setting pre-answers it: a student who has already asked their
     device for less motion does not have to ask again on every page. */
  function wireMotion(root) {
    var btns = toArray(root.querySelectorAll("[data-motion-set]"));
    if (!btns.length) { return; }

    function set(state) {
      document.documentElement.setAttribute("data-motion", state);
      each(btns, function (b) {
        b.setAttribute("aria-pressed",
          b.getAttribute("data-motion-set") === state ? "true" : "false");
      });
      writeStore(MOTION_KEY, state);
    }

    each(btns, function (b) {
      b.addEventListener("click", function () {
        set(b.getAttribute("data-motion-set"));
      });
    });

    var saved = readStore(MOTION_KEY);
    set(saved === "off" || saved === "on" ? saved : (REDUCED ? "off" : "on"));
  }

  /* CONTRAST's flagship. Four cases, each independent, all four in the
     document with one shown — the same trick the board uses, so a student who
     goes back to cell 1 finds it exactly as they left it and no state has to
     be kept anywhere but the DOM.

     ⚖️ MRB-196: whether the student agreed is NOT computed. Design computes it
     and spends it on the why paragraph's colour, ~6 ΔL* — a mark nobody can
     read and a mark all the same. The self-check asks them instead. */
  function wireSettles(sec) {
    var panels = toArray(sec.querySelectorAll(".ks3-case-panel"));
    var tabs = toArray(sec.querySelectorAll(".ks3-case-tab"));
    var selfcheck = sec.querySelector("[data-selfcheck]");
    if (!panels.length) { return; }

    function show(id) {
      each(tabs, function (tab) {
        tab.setAttribute("aria-pressed",
          tab.getAttribute("data-case") === id ? "true" : "false");
      });
      each(panels, function (p) {
        setHidden(p, p.getAttribute("data-case") !== id);
      });
    }
    each(tabs, function (tab) {
      tab.addEventListener("click", function () {
        show(tab.getAttribute("data-case"));
      });
    });

    // The rail stop is `all_cases_revealed`, threshold 4 — every case opened,
    // not merely every fact marked on one of them. One case is one cell; the
    // lesson's argument is the four held against each other.
    function refreshStage() {
      var all = true;
      each(panels, function (p) {
        if (p.getAttribute("data-open") !== "1") { all = false; }
      });
      markStage(sec, all);
      if (all && selfcheck) {
        setHidden(selfcheck, false);
        selfcheck.setAttribute("role", "status");
      }
    }

    each(panels, function (panel) {
      var feats = toArray(panel.querySelectorAll(".ks3-feature"));
      var btn = panel.querySelector("[data-settle-reveal]");
      var prog = panel.querySelector("[data-settle-progress]");
      var verdict = panel.querySelector("[data-case-verdict]");
      var total = feats.length;
      var fmt = (prog && prog.getAttribute("data-format")) || "{n} of {total} marked";
      var opened = (prog && prog.getAttribute("data-opened")) || "Opened";

      function marked() {
        var n = 0;
        each(feats, function (f) {
          if (f.querySelector('.ks3-settle-choice[aria-pressed="true"]')) { n += 1; }
        });
        return n;
      }

      function repaint() {
        var n = marked();
        var isOpen = panel.getAttribute("data-open") === "1";
        if (prog) {
          prog.textContent = isOpen ? opened
            : fmt.replace("{n}", n).replace("{total}", total);
        }
        if (btn) {
          if (n < total || isOpen) { btn.setAttribute("disabled", ""); }
          else { btn.removeAttribute("disabled"); }
        }
      }

      each(feats, function (feat) {
        var choices = toArray(feat.querySelectorAll(".ks3-settle-choice"));
        each(choices, function (c) {
          c.addEventListener("click", function () {
            if (panel.getAttribute("data-open") === "1") { return; }
            each(choices, function (b) { b.setAttribute("aria-pressed", "false"); });
            c.setAttribute("aria-pressed", "true");
            repaint();
          });
        });
      });

      if (btn) {
        btn.addEventListener("click", function () {
          if (marked() < total || panel.getAttribute("data-open") === "1") { return; }
          panel.setAttribute("data-open", "1");
          each(feats, function (f) {
            setHidden(f.querySelector("[data-reveal]"), false);
            each(f.querySelectorAll(".ks3-settle-choice"), function (c) {
              c.setAttribute("disabled", "");
            });
          });
          setHidden(verdict, false);
          if (verdict) { verdict.setAttribute("role", "status"); }
          repaint();
          refreshStage();
        });
      }

      repaint();
    });

    if (selfcheck) {
      var scOpts = toArray(selfcheck.querySelectorAll(".ks3-option"));
      each(scOpts, function (o) {
        o.addEventListener("click", function () {
          each(scOpts, function (b) { b.setAttribute("aria-pressed", "false"); });
          o.setAttribute("aria-pressed", "true");
        });
      });
    }

    show(panels[0].getAttribute("data-case"));
  }


  /* ═══════════════════════════════════════════════════════════════
     SYSTEM's bench and its sabotage engine (b1-04, the SYSTEM
     reference screen — 32 slots).

     The four cell drawings and the three canvas helpers below are
     ported VERBATIM from Design's approved b1-04, method bodies
     unchanged, class methods turned into functions. They are Design's
     drawings and the standing law is to reproduce them, so they are
     not retouched, retimed or re-coloured. The 26 hex literals in them
     that have no KS3 token are Design's own and stay Design's own;
     inventing tokens for them would claim a design decision nobody
     made.
     ═══════════════════════════════════════════════════════════════ */

  function ell(ctx, x, y, rx, ry, rot) {
    ctx.beginPath();
    ctx.ellipse(x, y, Math.max(0.5, rx), Math.max(0.5, ry), rot || 0, 0, Math.PI * 2);
  }

  // ⚠️ b1-04's mitochondrion takes a SCALE; b1-03's does not, and the two
  // pages draw different sizes. Ported into one file they collided under
  // one name and the later definition silently won for both. Scoped.
  function mitoScaled(ctx, x, y, rot, k) {
    ctx.save();
    ctx.translate(x, y); ctx.rotate(rot); ctx.scale(k, k);
    ell(ctx, 0, 0, 22, 11, 0);
    ctx.fillStyle = '#C96C3C'; ctx.fill();
    ctx.lineWidth = 2 / k; ctx.strokeStyle = '#8B4523'; ctx.stroke();
    ctx.beginPath();
    ctx.moveTo(-14, 0);
    ctx.quadraticCurveTo(-9, -6, -4, 0);
    ctx.quadraticCurveTo(1, 6, 6, 0);
    ctx.quadraticCurveTo(11, -6, 15, 0);
    ctx.lineWidth = 1.8 / k; ctx.strokeStyle = '#F6E2D2'; ctx.stroke();
    ctx.restore();
  }

  function arrow(ctx, x1, y1, x2, y2, col) {
    ctx.beginPath();
    ctx.moveTo(x1, y1); ctx.lineTo(x2, y2);
    ctx.lineWidth = 3; ctx.strokeStyle = col; ctx.stroke();
    const a = Math.atan2(y2 - y1, x2 - x1);
    ctx.beginPath();
    ctx.moveTo(x2, y2);
    ctx.lineTo(x2 - 12 * Math.cos(a - 0.42), y2 - 12 * Math.sin(a - 0.42));
    ctx.moveTo(x2, y2);
    ctx.lineTo(x2 - 12 * Math.cos(a + 0.42), y2 - 12 * Math.sin(a + 0.42));
    ctx.stroke();
  }

  function drawRed(ctx, W, H, sab, dark) {
    const cy = H * 0.5;
    const narrow = sab === 'sphere';
    const vh = narrow ? 116 : 150;
    ctx.fillStyle = dark ? '#241A18' : '#F8E9E5';
    ctx.beginPath();
    ctx.moveTo(0, cy - vh / 2);
    ctx.lineTo(W * 0.62, cy - vh / 2);
    ctx.quadraticCurveTo(W * 0.72, cy - vh / 2, W * 0.74, cy - (narrow ? 44 : vh / 2));
    ctx.lineTo(W, cy - (narrow ? 44 : vh / 2));
    ctx.lineTo(W, cy + (narrow ? 44 : vh / 2));
    ctx.lineTo(W * 0.74, cy + (narrow ? 44 : vh / 2));
    ctx.quadraticCurveTo(W * 0.72, cy + vh / 2, W * 0.62, cy + vh / 2);
    ctx.lineTo(0, cy + vh / 2);
    ctx.closePath();
    ctx.fill();
    ctx.lineWidth = 4; ctx.strokeStyle = dark ? '#7A6A62' : '#221E1B'; ctx.stroke();

    const xs = narrow ? [140, 330, 500] : [180, 450, 720];
    xs.forEach((x, i) => {
      ctx.save();
      ctx.translate(x, cy + (i === 1 ? 0 : (i === 0 ? -12 : 14)));
      if (narrow) {
        ell(ctx, 0, 0, 64, 62, 0);
        ctx.fillStyle = '#C2372B'; ctx.fill();
        ctx.lineWidth = 3; ctx.strokeStyle = '#7E1F16'; ctx.stroke();
      } else {
        ctx.rotate(i === 1 ? 0 : (i === 0 ? -0.18 : 0.14));
        ctx.beginPath();
        ctx.moveTo(-86, 0);
        ctx.bezierCurveTo(-70, -38, -28, -13, 0, -13);
        ctx.bezierCurveTo(28, -13, 70, -38, 86, 0);
        ctx.bezierCurveTo(70, 38, 28, 13, 0, 13);
        ctx.bezierCurveTo(-28, 13, -70, 38, -86, 0);
        ctx.closePath();
        ctx.fillStyle = '#C2372B'; ctx.fill();
        ctx.lineWidth = 3; ctx.strokeStyle = '#7E1F16'; ctx.stroke();
      }
      const dots = sab === 'nucleus' ? 6 : 15;
      ctx.fillStyle = '#8E2318';
      for (let d = 0; d < dots; d++) {
        const a = (d / dots) * Math.PI * 2 + i;
        const rr2 = narrow ? 38 : 58;
        ell(ctx, Math.cos(a) * rr2 * 0.9, Math.sin(a) * (narrow ? 34 : 8), 5, 4, 0);
        ctx.fill();
      }
      if (sab === 'nucleus') {
        ell(ctx, 0, 0, 30, narrow ? 26 : 13, 0);
        ctx.fillStyle = '#7C6AA6'; ctx.fill();
        ctx.lineWidth = 2.5; ctx.strokeStyle = '#453A69'; ctx.stroke();
      }
      ctx.restore();
    });

    if (narrow) {
      ctx.setLineDash([9, 7]);
      arrow(ctx, 620, cy, 700, cy, '#B23A2A');
      ctx.setLineDash([]);
    }
  }

  function drawRoot(ctx, W, H, sab, dark) {
    const soilX = 260;
    ctx.fillStyle = dark ? '#241E17' : '#E9DCC2';
    ctx.fillRect(soilX, 0, W - soilX, H);
    ctx.fillStyle = dark ? '#2E271E' : '#DCCBA9';
    [[380, 120, 58], [520, 90, 44], [660, 150, 66], [800, 96, 50], [340, 300, 52],
     [470, 340, 62], [620, 300, 46], [760, 360, 58], [400, 470, 60], [560, 480, 48],
     [700, 470, 56], [840, 440, 62], [880, 240, 54]].forEach((p) => {
      ell(ctx, p[0], p[1], p[2], p[2] * 0.82, 0.3);
      ctx.fill();
    });

    ctx.fillStyle = dark ? '#1A1611' : '#F3E8D2';
    ctx.fillRect(0, 0, soilX, H);
    ctx.lineWidth = 4; ctx.strokeStyle = dark ? '#7A6A62' : '#221E1B';
    ctx.beginPath(); ctx.moveTo(soilX, 0); ctx.lineTo(soilX, H); ctx.stroke();

    rr(ctx, 60, 150, 200, 260, 20);
    ctx.fillStyle = '#D9C48D'; ctx.fill();
    ctx.lineWidth = 3; ctx.strokeStyle = '#221E1B'; ctx.stroke();
    rr(ctx, 76, 166, 168, 228, 14);
    ctx.fillStyle = '#F5ECD8'; ctx.fill();
    rr(ctx, 104, 214, 118, 140, 34);
    ctx.fillStyle = '#E4EDE9'; ctx.fill();
    ctx.lineWidth = 2; ctx.strokeStyle = '#9AB0A6'; ctx.stroke();

    const hairEnd = sab === 'short' ? 340 : 800;
    ctx.beginPath();
    ctx.moveTo(240, 234);
    ctx.quadraticCurveTo((240 + hairEnd) / 2, 214, hairEnd, 248);
    ctx.quadraticCurveTo((240 + hairEnd) / 2, 262, 240, 292);
    ctx.closePath();
    ctx.fillStyle = '#F5ECD8'; ctx.fill();
    ctx.lineWidth = 3; ctx.strokeStyle = '#221E1B'; ctx.stroke();

    ell(ctx, 150, 195, 32, 24, 0);
    ctx.fillStyle = '#7C6AA6'; ctx.fill();
    ctx.lineWidth = 2.5; ctx.strokeStyle = '#453A69'; ctx.stroke();

    if (sab !== 'mito') {
      [[110, 380, 0.4], [200, 384, -0.3], [156, 262, 1.4], [212, 300, 0.2], [96, 300, 1.2], [180, 158, 0.5]]
        .forEach((m) => mitoScaled(ctx, m[0], m[1], m[2], 0.9));
    }

    const wcol = '#2F5CE0';
    const waterAt = sab === 'short' ? [[400, 200, 350, 232], [400, 300, 352, 262]] :
      [[430, 150, 372, 224], [560, 130, 508, 226], [700, 170, 650, 236], [470, 400, 412, 274], [640, 410, 588, 268], [810, 350, 790, 274]];
    waterAt.forEach((a) => arrow(ctx, a[0], a[1], a[2], a[3], wcol));

    if (sab !== 'mito') {
      ctx.setLineDash([]);
      [[520, 250, 440, 250]].forEach((a) => arrow(ctx, a[0], a[1], a[2], a[3], '#A93411'));
    } else {
      ctx.setLineDash([8, 7]);
      ctx.globalAlpha = 0.5;
      arrow(ctx, 520, 250, 470, 250, '#A93411');
      ctx.globalAlpha = 1;
      ctx.setLineDash([]);
    }
  }

  function drawSperm(ctx, W, H, sab, dark) {
    const cy = H * 0.5;
    ell(ctx, 190, cy, 74, 52, 0);
    ctx.fillStyle = '#E7DECE'; ctx.fill();
    ctx.lineWidth = 3.5; ctx.strokeStyle = dark ? '#C6B9A7' : '#221E1B'; ctx.stroke();
    ctx.save();
    ctx.beginPath();
    ell(ctx, 190, cy, 74, 52, 0);
    ctx.clip();
    ctx.fillStyle = '#C8B49A';
    ctx.beginPath();
    ctx.moveTo(116, cy - 60); ctx.lineTo(170, cy - 60); ctx.lineTo(150, cy + 60); ctx.lineTo(116, cy + 60);
    ctx.closePath(); ctx.fill();
    ctx.restore();
    ell(ctx, 208, cy, 40, 34, 0);
    ctx.fillStyle = '#7C6AA6'; ctx.fill();
    ctx.lineWidth = 2.5; ctx.strokeStyle = '#453A69'; ctx.stroke();

    rr(ctx, 262, cy - 26, 104, 52, 16);
    ctx.fillStyle = '#F5ECD8'; ctx.fill();
    ctx.lineWidth = 3; ctx.strokeStyle = dark ? '#C6B9A7' : '#221E1B'; ctx.stroke();
    if (sab !== 'mito') {
      [[288, cy - 8, 0.5], [318, cy + 9, -0.4], [346, cy - 7, 0.3], [300, cy + 14, 0.9]]
        .forEach((m) => mitoScaled(ctx, m[0], m[1], m[2], 0.62));
    }

    if (sab !== 'notail') {
      const limp = sab === 'mito';
      const end = limp ? 620 : 850;
      const amp = limp ? 10 : 46;
      ctx.beginPath();
      for (let x = 366; x <= end; x += 4) {
        const t = (x - 366) / (end - 366);
        const y = cy + Math.sin(t * Math.PI * (limp ? 1.6 : 3.1)) * amp * (0.35 + t * 0.8);
        if (x === 366) ctx.moveTo(x, y); else ctx.lineTo(x, y);
      }
      ctx.lineWidth = limp ? 7 : 10;
      ctx.lineCap = 'round';
      ctx.strokeStyle = dark ? '#C6B9A7' : '#221E1B';
      ctx.stroke();
      if (limp) {
        ctx.setLineDash([8, 8]);
        ctx.beginPath();
        ctx.moveTo(end, cy + 6); ctx.lineTo(760, cy + 10);
        ctx.lineWidth = 4; ctx.strokeStyle = '#8F857B'; ctx.stroke();
        ctx.setLineDash([]);
      }
    }
  }

  function drawNerve(ctx, W, H, sab, dark) {
    const cy = H * 0.5;
    const ink = dark ? '#C6B9A7' : '#221E1B';
    const relay = sab === 'short';
    const somas = relay ? [[120, cy], [420, cy], [700, cy]] : [[130, cy]];
    const axonTo = relay ? [340, 640, 880] : [820];

    somas.forEach((s, si) => {
      const sx = s[0], sy = s[1];
      [[-1.9, 66], [-2.5, 58], [2.4, 62], [1.9, 54], [-3.1, 50]].forEach((d) => {
        const a = d[0], L = d[1] * (relay ? 0.62 : 1);
        ctx.beginPath();
        ctx.moveTo(sx, sy);
        ctx.lineTo(sx + Math.cos(a) * L, sy + Math.sin(a) * L);
        ctx.lineTo(sx + Math.cos(a) * (L + 22) - 8, sy + Math.sin(a) * (L + 22) - 6);
        ctx.moveTo(sx + Math.cos(a) * L, sy + Math.sin(a) * L);
        ctx.lineTo(sx + Math.cos(a) * (L + 22) + 6, sy + Math.sin(a) * (L + 22) + 8);
        ctx.lineWidth = 4; ctx.lineCap = 'round'; ctx.strokeStyle = ink; ctx.stroke();
      });
      const R = relay ? 40 : 58;
      ell(ctx, sx, sy, R, R * 0.92, 0);
      ctx.fillStyle = '#F5ECD8'; ctx.fill();
      ctx.lineWidth = 3.5; ctx.strokeStyle = ink; ctx.stroke();
      ell(ctx, sx, sy, R * 0.44, R * 0.42, 0);
      ctx.fillStyle = '#7C6AA6'; ctx.fill();
      ctx.lineWidth = 2.5; ctx.strokeStyle = '#453A69'; ctx.stroke();

      const x0 = sx + R, x1 = axonTo[si];
      ctx.beginPath();
      ctx.moveTo(x0, sy); ctx.lineTo(x1, sy);
      ctx.lineWidth = 15; ctx.lineCap = 'round'; ctx.strokeStyle = '#F5ECD8'; ctx.stroke();
      ctx.lineWidth = 17; ctx.strokeStyle = ink; ctx.stroke();
      ctx.lineWidth = 11; ctx.strokeStyle = '#F5ECD8'; ctx.stroke();

      if (sab !== 'sheath') {
        const seg = relay ? 74 : 108;
        for (let x = x0 + 18; x + seg < x1; x += seg + 16) {
          rr(ctx, x, sy - 19, seg, 38, 15);
          ctx.fillStyle = '#EFD9A8'; ctx.fill();
          ctx.lineWidth = 3; ctx.strokeStyle = ink; ctx.stroke();
        }
      }

      [[-0.5, 1], [0, 1], [0.5, 1]].forEach((d) => {
        ctx.beginPath();
        ctx.moveTo(x1, sy);
        ctx.lineTo(x1 + 34, sy + d[0] * 44);
        ctx.lineTo(x1 + 56, sy + d[0] * 62);
        ctx.lineWidth = 4; ctx.lineCap = 'round'; ctx.strokeStyle = ink; ctx.stroke();
        ell(ctx, x1 + 58, sy + d[0] * 64, 8, 8, 0);
        ctx.fillStyle = ink; ctx.fill();
      });

      if (relay && si < somas.length - 1) {
        ctx.setLineDash([6, 6]);
        ctx.beginPath();
        ctx.moveTo(x1 + 68, sy - 60); ctx.lineTo(x1 + 68, sy + 60);
        ctx.lineWidth = 3; ctx.strokeStyle = '#A93411'; ctx.stroke();
        ctx.setLineDash([]);
      }
    });
  }


  var CELL_DRAWINGS = { red: drawRed, root: drawRoot, sperm: drawSperm, nerve: drawNerve };

  // Design's own framing: every cell is drawn in a fixed 900x560 design space
  // and scaled to fit, on a 2x backing store.
  function paintCell(canvas, dark, sab) {
    if (!canvas || !canvas.getContext) { return; }
    var fn = CELL_DRAWINGS[canvas.getAttribute("data-drawing")];
    if (!fn) { return; }
    var ctx = canvas.getContext("2d");
    var W = canvas.width / 2, H = canvas.height / 2;
    ctx.setTransform(1, 0, 0, 1, 0, 0);
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    ctx.setTransform(2, 0, 0, 2, 0, 0);
    ctx.fillStyle = dark ? "#100D0A" : "#FFFCF5";
    ctx.fillRect(0, 0, W, H);
    var k = Math.min(W / 900, H / 560);
    ctx.save();
    ctx.translate((W - 900 * k) / 2, (H - 560 * k) / 2);
    ctx.scale(k, k);
    fn(ctx, 900, 560, sab, dark);
    ctx.restore();
  }

  /* The bench. Emit-all-show-one, like the board — the DOM is the state.
     The chosen cell is broadcast, because the sabotage section follows it:
     `bench` in the payload names this section's anchor, and the two
     instruments share a cast. */
  function wireBench(sec) {
    var bench = sec.querySelector(".ks3-bench");
    if (!bench) { return; }
    var btns = toArray(bench.querySelectorAll(".ks3-bench-cell"));
    var figures = toArray(bench.querySelectorAll(".ks3-bench-figure"));
    var panels = toArray(bench.querySelectorAll(".ks3-bench-panel"));
    var seen = {};

    function show(id) {
      bench.setAttribute("data-current", id);
      each(btns, function (b) {
        b.setAttribute("aria-pressed",
          b.getAttribute("data-cell") === id ? "true" : "false");
      });
      each(figures, function (f) {
        var on = f.getAttribute("data-cell") === id;
        setHidden(f, !on);
        // Painted on first show rather than on load: four 1800x1120 canvases
        // is real work for a phone, and three of them are behind a button.
        if (on && !f.hasAttribute("data-painted")) {
          paintCell(f.querySelector("canvas"), false, null);
          f.setAttribute("data-painted", "1");
        }
      });
      each(panels, function (p) {
        setHidden(p, p.getAttribute("data-cell") !== id);
      });
      seen[id] = true;
      // The rail stop is `all_specimens_seen`: the bench's claim is that the
      // same seven parts are tuned four different ways, and you have not seen
      // that until you have seen all four.
      markStage(sec, Object.keys(seen).length === btns.length);
      var name = "";
      each(btns, function (b) {
        if (b.getAttribute("data-cell") === id) {
          var n = b.querySelector(".ks3-bench-cell-name");
          name = n ? n.textContent : "";
        }
      });
      document.dispatchEvent(new CustomEvent("ks3:cell", {
        detail: { anchor: sec.id, cell: id, name: name }
      }));
    }

    each(btns, function (b) {
      b.addEventListener("click", function () {
        show(b.getAttribute("data-cell"));
      });
    });
    show(bench.getAttribute("data-current") || btns[0].getAttribute("data-cell"));
  }

  /* The sabotage engine. Every (cell x sabotage) panel is in the document;
     the pair showing is the bench's cell and this section's chosen sabotage
     for that cell. Law 4 gates the chain behind the prediction. */
  function wireSabotage(sec) {
    var wrap = sec.querySelector(".ks3-sab");
    if (!wrap) { return; }
    var tabs = toArray(wrap.querySelectorAll(".ks3-sab-tab"));
    var panels = toArray(wrap.querySelectorAll(".ks3-sab-panel"));
    var prog = wrap.querySelector("[data-sab-progress]");
    var specimen = wrap.querySelector("[data-sab-specimen]");
    var total = parseInt(wrap.getAttribute("data-total"), 10) || panels.length;
    var cell = null, chosen = {};

    function ranCount() {
      var n = 0;
      each(panels, function (p) { if (p.getAttribute("data-run") === "1") { n += 1; } });
      return n;
    }

    function paint() {
      each(tabs, function (tb) {
        var mine = tb.getAttribute("data-cell") === cell;
        setHidden(tb, !mine);
        tb.setAttribute("aria-pressed",
          mine && tb.getAttribute("data-sab") === chosen[cell] ? "true" : "false");
      });
      each(panels, function (p) {
        setHidden(p, !(p.getAttribute("data-cell") === cell
                       && p.getAttribute("data-sab") === chosen[cell]));
      });
      if (prog) {
        prog.textContent = ranCount() + " of " + total + " sabotages run";
      }
      // `predictions_made`, threshold 4 — four sabotages followed out, not all
      // eight. The threshold is the lesson's, not the instrument's.
      markStage(sec, ranCount() >= 4);
    }

    function setCell(id, name) {
      cell = id;
      if (!chosen[cell]) {
        var first = null;
        each(tabs, function (tb) {
          if (!first && tb.getAttribute("data-cell") === cell) {
            first = tb.getAttribute("data-sab");
          }
        });
        chosen[cell] = first;
      }
      if (specimen && name) { specimen.textContent = name; }
      paint();
    }

    each(tabs, function (tb) {
      tb.addEventListener("click", function () {
        chosen[tb.getAttribute("data-cell")] = tb.getAttribute("data-sab");
        paint();
      });
    });

    each(panels, function (panel) {
      var opts = toArray(panel.querySelectorAll(".ks3-option"));
      var chain = panel.querySelector("[data-reveal]");
      var pick = panel.querySelector("[data-sab-pick]");
      each(opts, function (o, i) {
        o.addEventListener("click", function () {
          each(opts, function (b) { b.setAttribute("aria-pressed", "false"); });
          o.setAttribute("aria-pressed", "true");
          // ⊕ F4's precedent, already taken on the board: Design REMOVES the
          // prediction once made. It stays here, chosen and still changeable,
          // because R3's runtime assertion fails an activity option that is
          // disabled and fails a group whose options do not all render alike
          // — which a removed or frozen sibling produces immediately.
          if (pick) {
            var label = o.querySelector(".ks3-opt-label");
            pick.textContent = "You said: " + (label ? label.textContent : "");
          }
          if (chain && chain.hasAttribute("hidden")) {
            setHidden(chain, false);
            chain.setAttribute("role", "status");
            paintCell(panel.querySelector(".ks3-sab-canvas"), true,
                      panel.getAttribute("data-sab"));
          }
          panel.setAttribute("data-run", "1");
          paint();
        });
      });
    });

    document.addEventListener("ks3:cell", function (ev) {
      if (!wrap.getAttribute("data-bench-ref")
          || ev.detail.anchor === wrap.getAttribute("data-bench-ref")) {
        setCell(ev.detail.cell, ev.detail.name);
      }
    });
  }


  /* ═══════════════════════════════════════════════════════════════
     b1-05's three instruments. All three rendered as EMPTY sections.
     The four zoom drawings and `rr` below are ported VERBATIM from
     Design's approved b1-05.
     ═══════════════════════════════════════════════════════════════ */

  function rr(ctx, x, y, w, h, r) {
    ctx.beginPath();
    ctx.moveTo(x + r, y);
    ctx.lineTo(x + w - r, y);
    ctx.quadraticCurveTo(x + w, y, x + w, y + r);
    ctx.lineTo(x + w, y + h - r);
    ctx.quadraticCurveTo(x + w, y + h, x + w - r, y + h);
    ctx.lineTo(x + r, y + h);
    ctx.quadraticCurveTo(x, y + h, x, y + h - r);
    ctx.lineTo(x, y + r);
    ctx.quadraticCurveTo(x, y, x + r, y);
    ctx.closePath();
  }

  function drawPlant(ctx, faded) {
    const stemX = 450, ground = 348;
    ctx.fillStyle = '#EFE3C9';
    ctx.fillRect(0, ground, 900, 500 - ground);
    ctx.lineWidth = 3; ctx.strokeStyle = '#221E1B';
    ctx.beginPath(); ctx.moveTo(0, ground); ctx.lineTo(900, ground); ctx.stroke();

    ctx.save();
    if (faded) ctx.globalAlpha = 0.26;
    ctx.lineWidth = 6; ctx.strokeStyle = '#8A6A3C'; ctx.lineCap = 'round';
    [[-1, 96], [1, 104], [-1, 52], [1, 60]].forEach((r, i) => {
      ctx.beginPath();
      ctx.moveTo(stemX, ground);
      ctx.quadraticCurveTo(stemX + r[0] * r[1] * 0.6, ground + 40, stemX + r[0] * r[1], ground + 96 + i * 8);
      ctx.stroke();
    });
    ctx.restore();

    ctx.save();
    if (faded === 'root') ctx.globalAlpha = 1;
    ctx.lineWidth = 11; ctx.strokeStyle = '#5E7A3A'; ctx.lineCap = 'round';
    ctx.beginPath(); ctx.moveTo(stemX, ground); ctx.lineTo(stemX, 104); ctx.stroke();
    [[-1, 262, 0.24], [1, 208, -0.26], [-1, 150, 0.2]].forEach((b) => {
      ctx.beginPath();
      ctx.moveTo(stemX, b[1]);
      ctx.quadraticCurveTo(stemX + b[0] * 52, b[1] - 16, stemX + b[0] * 112, b[1] - 34);
      ctx.lineWidth = 7; ctx.stroke();
      leafShape(ctx, stemX + b[0] * 186, b[1] - 52, 168, 76, b[2] * b[0]);
      ctx.fillStyle = '#5E9440'; ctx.fill();
      ctx.lineWidth = 3; ctx.strokeStyle = '#2F5326'; ctx.stroke();
      ctx.strokeStyle = '#5E7A3A';
    });
    leafShape(ctx, stemX, 88, 150, 70, -0.12);
    ctx.fillStyle = '#5E9440'; ctx.fill();
    ctx.lineWidth = 3; ctx.strokeStyle = '#2F5326'; ctx.stroke();
    ctx.restore();
  }

  function drawOneLeaf(ctx) {
    ctx.save();
    ctx.translate(450, 250);
    ctx.beginPath();
    ctx.moveTo(-330, 0);
    ctx.quadraticCurveTo(-120, -172, 330, 0);
    ctx.quadraticCurveTo(-120, 172, -330, 0);
    ctx.closePath();
    ctx.fillStyle = '#5E9440'; ctx.fill();
    ctx.lineWidth = 4; ctx.strokeStyle = '#2F5326'; ctx.stroke();
    ctx.lineWidth = 6; ctx.strokeStyle = '#3E6B2C';
    ctx.beginPath(); ctx.moveTo(-330, 0); ctx.lineTo(310, 0); ctx.stroke();
    ctx.lineWidth = 3;
    for (let i = -4; i <= 4; i++) {
      if (i === 0) continue;
      const x = i * 62;
      const up = i % 2 === 0 ? -1 : 1;
      ctx.beginPath();
      ctx.moveTo(x - 40, 0);
      ctx.quadraticCurveTo(x, up * 40, x + 78, up * 72);
      ctx.stroke();
    }
    ctx.restore();
  }

  function drawLeafSection(ctx) {
    const x0 = 90, x1 = 810;
    rr(ctx, x0, 90, x1 - x0, 66, 8);
    ctx.fillStyle = '#EFE6D2'; ctx.fill();
    ctx.lineWidth = 3; ctx.strokeStyle = '#221E1B'; ctx.stroke();
    for (let x = x0 + 90; x < x1; x += 90) {
      ctx.beginPath(); ctx.moveTo(x, 90); ctx.lineTo(x, 156);
      ctx.lineWidth = 2; ctx.strokeStyle = '#C3B191'; ctx.stroke();
    }
    for (let i = 0; i < 8; i++) {
      const x = x0 + 16 + i * 90;
      rr(ctx, x, 164, 62, 130, 12);
      ctx.fillStyle = '#EFF3E4'; ctx.fill();
      ctx.lineWidth = 3; ctx.strokeStyle = '#221E1B'; ctx.stroke();
      for (let j = 0; j < 7; j++) {
        ell(ctx, x + 16 + (j % 2) * 28, 182 + j * 16, 11, 7, 0.2);
        ctx.fillStyle = '#4F7C3B'; ctx.fill();
      }
    }
    for (let i = 0; i < 5; i++) {
      const x = x0 + 40 + i * 150;
      [[x, 330], [x + 70, 372], [x + 4, 402]].forEach((p, k) => {
        ell(ctx, p[0], p[1], 42, 28, k * 0.4);
        ctx.fillStyle = '#EFF3E4'; ctx.fill();
        ctx.lineWidth = 3; ctx.strokeStyle = '#221E1B'; ctx.stroke();
        ell(ctx, p[0] - 10, p[1], 9, 6, 0);
        ctx.fillStyle = '#4F7C3B'; ctx.fill();
      });
    }
    rr(ctx, x0, 428, x1 - x0, 58, 8);
    ctx.fillStyle = '#EFE6D2'; ctx.fill();
    ctx.lineWidth = 3; ctx.strokeStyle = '#221E1B'; ctx.stroke();
  }

  function drawOneCell(ctx) {
    rr(ctx, 300, 46, 300, 420, 26);
    ctx.fillStyle = '#D9C48D'; ctx.fill();
    ctx.lineWidth = 3; ctx.strokeStyle = '#221E1B'; ctx.stroke();
    rr(ctx, 318, 64, 264, 384, 20);
    ctx.fillStyle = '#F5ECD8'; ctx.fill();
    ctx.lineWidth = 2.2; ctx.strokeStyle = '#A2603A'; ctx.stroke();
    rr(ctx, 372, 158, 156, 220, 48);
    ctx.fillStyle = '#E4EDE9'; ctx.fill();
    ctx.lineWidth = 2; ctx.strokeStyle = '#9AB0A6'; ctx.stroke();
    [[350, 100], [420, 88], [492, 100], [556, 128], [560, 226], [556, 330], [492, 414],
     [420, 424], [352, 400], [344, 300], [348, 200]].forEach((p, i) => {
      ctx.save();
      ctx.translate(p[0], p[1]); ctx.rotate(i * 0.5);
      ell(ctx, 0, 0, 25, 15, 0);
      ctx.fillStyle = '#4F7C3B'; ctx.fill();
      ctx.lineWidth = 2; ctx.strokeStyle = '#2F5326'; ctx.stroke();
      ctx.restore();
    });
    ell(ctx, 346, 258, 26, 36, 0);
    ctx.fillStyle = '#7C6AA6'; ctx.fill();
    ctx.lineWidth = 2.5; ctx.strokeStyle = '#453A69'; ctx.stroke();
  }

  function leafShape(ctx, cx, cy, L, Wd, rot) {
    ctx.save();
    ctx.translate(cx, cy); ctx.rotate(rot);
    ctx.beginPath();
    ctx.moveTo(-L / 2, 0);
    ctx.quadraticCurveTo(-L / 6, -Wd / 2, L / 2, 0);
    ctx.quadraticCurveTo(-L / 6, Wd / 2, -L / 2, 0);
    ctx.closePath();
    ctx.restore();
  }

  var ZOOM_DRAWINGS = {
    "plant": function (ctx) { drawPlant(ctx, false); },
    "plant-shoot": function (ctx) { drawPlant(ctx, "shoot"); },
    "one-leaf": drawOneLeaf,
    "leaf-section": drawLeafSection,
    "one-cell": drawOneCell
  };

  function wireZoom(sec) {
    var wrap = sec.querySelector(".ks3-zoom");
    if (!wrap) { return; }
    var canvas = wrap.querySelector("[data-zoom-canvas]");
    var range = wrap.querySelector("[data-zoom-range]");
    var ticks = toArray(wrap.querySelectorAll(".ks3-zoom-tick"));
    var panels = toArray(wrap.querySelectorAll(".ks3-zoom-panel"));
    var step = wrap.querySelector("[data-zoom-step]");
    var size = wrap.querySelector("[data-zoom-size]");
    var levels, space;
    try { levels = JSON.parse(wrap.getAttribute("data-zoom-levels")); }
    catch (err) { return; }
    space = (wrap.getAttribute("data-space") || "900,500").split(",");
    var SW = parseFloat(space[0]), SH = parseFloat(space[1]);
    var boxLabel = wrap.getAttribute("data-box-label") || "";
    var fmt = (step && step.getAttribute("data-format")) || "Stop {n} of {total}";
    var seen = {};

    function paint(i) {
      if (!canvas || !canvas.getContext) { return; }
      var lv = levels[i];
      var fn = ZOOM_DRAWINGS[lv.drawing];
      if (!fn) { return; }
      var ctx = canvas.getContext("2d");
      var W = canvas.width / 2, H = canvas.height / 2;
      ctx.setTransform(1, 0, 0, 1, 0, 0);
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      ctx.setTransform(2, 0, 0, 2, 0, 0);
      ctx.fillStyle = "#FFFCF5";
      ctx.fillRect(0, 0, W, H);
      var k = Math.min(W / SW, H / SH);
      ctx.save();
      ctx.translate((W - SW * k) / 2, (H - SH * k) / 2);
      ctx.scale(k, k);
      fn(ctx);
      // The orange box: where the next stop down is hiding inside this one.
      // Authored per level, so the drawing and the box cannot drift apart.
      var b = lv.box;
      if (b) {
        ctx.setLineDash([11, 8]);
        ctx.lineWidth = 4;
        ctx.strokeStyle = "#E4572E";
        rr(ctx, b[0], b[1], b[2], b[3], 12);
        ctx.stroke();
        ctx.setLineDash([]);
        rr(ctx, b[0], b[1] - 30, 176, 26, 8);
        ctx.fillStyle = "#E4572E"; ctx.fill();
        ctx.fillStyle = "#FBF3E6";
        ctx.font = '500 14px "DM Mono", ui-monospace, monospace';
        ctx.textAlign = "left";
        ctx.textBaseline = "middle";
        ctx.fillText(boxLabel, b[0] + 12, b[1] - 16);
      }
      ctx.restore();
      canvas.setAttribute("aria-label", lv.alt || "");
    }

    function show(i) {
      i = Math.max(0, Math.min(levels.length - 1, i));
      if (range) { range.value = String(i); }
      each(ticks, function (tk) {
        tk.setAttribute("aria-pressed",
          parseInt(tk.getAttribute("data-zoom"), 10) === i ? "true" : "false");
      });
      each(panels, function (p) {
        setHidden(p, parseInt(p.getAttribute("data-zoom"), 10) !== i);
      });
      if (step) {
        step.textContent = fmt.replace("{n}", i + 1).replace("{total}", levels.length);
      }
      if (size) { size.textContent = levels[i].size || ""; }
      paint(i);
      seen[i] = true;
      // `all_stops_seen`, threshold 5 — the ladder is the point, not any rung.
      markStage(sec, Object.keys(seen).length === levels.length);
    }

    if (range) { onRange(range, function () { show(parseInt(range.value, 10) || 0); }); }
    each(ticks, function (tk) {
      tk.addEventListener("click", function () {
        show(parseInt(tk.getAttribute("data-zoom"), 10));
      });
    });
    show(range ? (parseInt(range.value, 10) || 0) : 0);
  }

  /* The awkward eight. The mark lands on the ROW and never on a chip. */
  function wireHard(sec) {
    var rows = toArray(sec.querySelectorAll(".ks3-hardrow"));
    var btn = sec.querySelector("[data-hard-reveal]");
    var prog = sec.querySelector("[data-hard-progress]");
    if (!rows.length) { return; }
    var total = rows.length;
    var fmt = (prog && prog.getAttribute("data-format")) || "{n} of {total} placed";

    function placed() {
      var n = 0;
      each(rows, function (r) {
        if (r.querySelector('.ks3-rung-chip[aria-pressed="true"]')) { n += 1; }
      });
      return n;
    }
    function repaint() {
      var n = placed();
      if (prog) { prog.textContent = fmt.replace("{n}", n).replace("{total}", total); }
      if (btn) {
        if (n < total) { btn.setAttribute("disabled", ""); }
        else { btn.removeAttribute("disabled"); }
      }
    }
    each(rows, function (row) {
      var chips = toArray(row.querySelectorAll(".ks3-rung-chip"));
      each(chips, function (c) {
        c.addEventListener("click", function () {
          each(chips, function (b) { b.setAttribute("aria-pressed", "false"); });
          c.setAttribute("aria-pressed", "true");
          repaint();
        });
      });
    });
    if (btn) {
      btn.addEventListener("click", function () {
        if (placed() < total) { return; }
        each(rows, function (row) {
          var chosen = row.querySelector('.ks3-rung-chip[aria-pressed="true"]');
          var right = chosen
            && chosen.getAttribute("data-rung") === row.getAttribute("data-answer");
          row.setAttribute("data-open", "1");
          row.setAttribute("data-right", right ? "1" : "0");
          setHidden(row.querySelector("[data-reveal]"), false);
        });
        btn.setAttribute("aria-expanded", "true");
        markStage(sec, true);   // `answers_opened`
      });
    }
    repaint();
  }

  /* Take a level out. Four cases, commit then consequence. */
  function wireRemoval(sec) {
    var wrap = sec.querySelector(".ks3-removal");
    if (!wrap) { return; }
    var tabs = toArray(wrap.querySelectorAll(".ks3-removal-tab"));
    var panels = toArray(wrap.querySelectorAll(".ks3-removal-panel"));
    var prog = wrap.querySelector("[data-removal-progress]");
    var total = parseInt(wrap.getAttribute("data-total"), 10) || panels.length;
    var fmt = (prog && prog.getAttribute("data-format")) || "{n} of {total} explored";

    function explored() {
      var n = 0;
      each(panels, function (p) { if (p.getAttribute("data-run") === "1") { n += 1; } });
      return n;
    }
    function repaint() {
      var n = explored();
      if (prog) { prog.textContent = fmt.replace("{n}", n).replace("{total}", total); }
      // `all_cases_explored`, threshold 4.
      markStage(sec, n >= total);
    }
    function show(id) {
      each(tabs, function (tb) {
        tb.setAttribute("aria-pressed",
          tb.getAttribute("data-case") === id ? "true" : "false");
      });
      each(panels, function (p) {
        setHidden(p, p.getAttribute("data-case") !== id);
      });
    }
    each(tabs, function (tb) {
      tb.addEventListener("click", function () { show(tb.getAttribute("data-case")); });
    });
    each(panels, function (panel) {
      var opts = toArray(panel.querySelectorAll(".ks3-option"));
      var out = panel.querySelector("[data-reveal]");
      each(opts, function (o) {
        o.addEventListener("click", function () {
          each(opts, function (b) { b.setAttribute("aria-pressed", "false"); });
          o.setAttribute("aria-pressed", "true");
          if (out && out.hasAttribute("hidden")) {
            setHidden(out, false);
            out.setAttribute("role", "status");
          }
          panel.setAttribute("data-run", "1");
          repaint();
        });
      });
    });
    repaint();
    if (panels.length) { show(panels[0].getAttribute("data-case")); }
  }


  /* ═══════════════════════════════════════════════════════════════
     b1-03's three instruments. b1-03 is the approved reference screen
     for MODEL — 50 lesson slots — and all three rendered as empty
     sections. The cell drawings, `rr`, `ell` and `blob` below are
     ported VERBATIM from Design's approved b1-03.
     ═══════════════════════════════════════════════════════════════ */

  var CVW = 900, CVH = 560;

  // Design's authored positions for b1-03's chloroplasts and the two
  // mitochondria scatters. Ported with the drawings that read them —
  // `MITO_CHEEK` was missed on the first pass and `#s-bench` threw
  // ReferenceError on every load, so the canvas stayed blank.
  var CHLORO = [[300, 126, -0.2], [392, 112, 0.1], [486, 124, -0.15], [578, 114, 0.2], [664, 132, -0.1],
    [706, 222, 1.5], [700, 330, 1.4], [620, 438, 0.15], [520, 452, -0.1], [420, 440, 0.2], [316, 450, -0.15],
    [176, 404, 1.3], [180, 196, 1.45]];
  var MITO_LEAF = [[258, 140, 0.6], [742, 182, 1.2], [700, 392, -0.5], [268, 438, 0.3]];
  var MITO_CHEEK = [[250, 214, 0.5], [302, 368, -0.4], [600, 196, 0.3], [650, 352, -0.5], [392, 196, 0.9],
    [420, 392, 0.1], [694, 272, 1.3], [224, 300, 1.4]];

  function blob(ctx, cx, cy, rx, ry, seed) {
    ctx.beginPath();
    for (let i = 0; i <= 150; i++) {
      const t = (i / 150) * Math.PI * 2;
      const k = 1 + 0.055 * Math.sin(3 * t + seed) + 0.032 * Math.cos(5 * t - seed);
      const x = cx + Math.cos(t) * rx * k;
      const y = cy + Math.sin(t) * ry * k;
      if (i === 0) ctx.moveTo(x, y); else ctx.lineTo(x, y);
    }
    ctx.closePath();
  }

  function leafBody(ctx, mode, stained) {
    const lw = mode === 'scope' ? 1.9 : 1;
    rr(ctx, 118, 58, 664, 444, 34);
    ctx.fillStyle = mode === 'scope' ? '#CFB98A' : '#D9C48D';
    ctx.fill();
    ctx.lineWidth = 2.6 * lw; ctx.strokeStyle = '#221E1B'; ctx.stroke();

    rr(ctx, 138, 78, 624, 404, 26);
    ctx.fillStyle = mode === 'scope' ? '#EDF2E1' : '#F5ECD8';
    ctx.fill();
    if (mode === 'diagram') { ctx.lineWidth = 2.2; ctx.strokeStyle = '#A2603A'; ctx.stroke(); }

    rr(ctx, 236, 176, 428, 208, 72);
    ctx.fillStyle = mode === 'scope' ? '#E3EDE2' : '#E4EDE9';
    ctx.fill();
    ctx.lineWidth = (mode === 'scope' ? 1.4 : 2) * lw; ctx.strokeStyle = '#9AB0A6'; ctx.stroke();

    ctx.save();
    if (mode === 'scope') ctx.filter = 'blur(0.7px)';
    CHLORO.forEach((c) => {
      ctx.save();
      ctx.translate(c[0], c[1]); ctx.rotate(c[2]);
      ell(ctx, 0, 0, 27, 16, 0);
      ctx.fillStyle = mode === 'scope' ? '#5C8544' : '#4F7C3B';
      ctx.fill();
      ctx.lineWidth = 2 * lw; ctx.strokeStyle = '#2F5326'; ctx.stroke();
      if (mode === 'diagram') {
        ctx.lineWidth = 3; ctx.strokeStyle = '#6E9C52';
        [-11, 0, 11].forEach((dx) => { ctx.beginPath(); ctx.moveTo(dx, -6); ctx.lineTo(dx, 6); ctx.stroke(); });
      }
      ctx.restore();
    });
    ctx.restore();

    if (mode === 'diagram') {
      MITO_LEAF.forEach((m) => mito(ctx, m[0], m[1], m[2]));
    }
    nucleus(ctx, 188, 300, 44, 52, mode, stained);
  }

  function cheekBody(ctx, cx, cy, seed, mode, stained) {
    const lw = mode === 'scope' ? 1.9 : 1;
    const dx = cx - 450, dy = cy - 286;
    blob(ctx, cx, cy, 298, 168, seed);
    ctx.fillStyle = mode === 'scope' ? '#EFE8DA' : '#F5ECD8';
    ctx.fill();
    ctx.lineWidth = 2.6 * lw; ctx.strokeStyle = mode === 'scope' ? '#B0A48E' : '#221E1B'; ctx.stroke();
    if (mode === 'diagram') {
      blob(ctx, cx, cy, 288, 158, seed);
      ctx.lineWidth = 1.8; ctx.strokeStyle = '#A2603A'; ctx.stroke();
      MITO_CHEEK.forEach((m) => mito(ctx, m[0] + dx, m[1] + dy, m[2]));
    }
    nucleus(ctx, 466 + dx, 272 + dy, 66, 60, mode, stained);
  }

  function mito(ctx, x, y, rot) {
    ctx.save();
    ctx.translate(x, y); ctx.rotate(rot);
    ell(ctx, 0, 0, 26, 13, 0);
    ctx.fillStyle = '#C96C3C'; ctx.fill();
    ctx.lineWidth = 2; ctx.strokeStyle = '#8B4523'; ctx.stroke();
    ctx.beginPath();
    ctx.moveTo(-17, 0);
    ctx.quadraticCurveTo(-11, -7, -5, 0);
    ctx.quadraticCurveTo(1, 7, 7, 0);
    ctx.quadraticCurveTo(13, -7, 18, 0);
    ctx.lineWidth = 2; ctx.strokeStyle = '#F6E2D2'; ctx.stroke();
    ctx.restore();
  }

  function nucleus(ctx, x, y, rx, ry, mode, stained) {
    if (mode === 'scope') {
      ctx.save();
      ctx.filter = 'blur(1.1px)';
      ell(ctx, x, y, rx, ry, 0);
      ctx.fillStyle = stained ? '#4A3C7A' : '#DCD2BE';
      ctx.globalAlpha = stained ? 0.92 : 0.6;
      ctx.fill();
      ctx.restore();
      return;
    }
    ell(ctx, x, y, rx, ry, 0);
    ctx.fillStyle = '#7C6AA6'; ctx.fill();
    ctx.lineWidth = 2.5; ctx.strokeStyle = '#453A69'; ctx.stroke();
    ell(ctx, x, y, rx - 7, ry - 7, 0);
    ctx.lineWidth = 1.5; ctx.strokeStyle = '#9C8DC0'; ctx.stroke();
    ell(ctx, x + rx * 0.28, y - ry * 0.24, 13, 11, 0);
    ctx.fillStyle = '#3E3260'; ctx.fill();
  }

  function drawDiagram(ctx, sp) {
    ctx.fillStyle = '#FFFCF5';
    ctx.fillRect(0, 0, CVW, CVH);
    if (sp === 'leaf') leafBody(ctx, 'diagram', false);
    else cheekBody(ctx, 450, 286, 0.8, 'diagram', false);
  }

  function drawScope(ctx, sp, stained) {
    ctx.fillStyle = '#100D0A';
    ctx.fillRect(0, 0, CVW, CVH);
    ctx.save();
    ctx.beginPath();
    ctx.arc(450, 280, 250, 0, Math.PI * 2);
    ctx.clip();
    ctx.fillStyle = sp === 'leaf' ? '#E8EFDF' : '#EBE4D6';
    ctx.fillRect(0, 0, CVW, CVH);

    const k = 0.52;
    if (sp === 'leaf') {
      for (let i = -2; i <= 2; i++) {
        for (let j = -2; j <= 2; j++) {
          ctx.save();
          ctx.translate(450 + i * 664 * k, 280 + j * 444 * k);
          ctx.scale(k, k);
          ctx.translate(-450, -280);
          leafBody(ctx, 'scope', stained);
          ctx.restore();
        }
      }
    } else {
      [[450, 280, 0.8], [172, 356, 2.1], [742, 214, 1.3], [516, 470, 3.0], [300, 118, 0.4]].forEach((b) => {
        ctx.save();
        ctx.translate(b[0], b[1]);
        ctx.scale(k, k);
        ctx.translate(-450, -286);
        cheekBody(ctx, 450, 286, b[2], 'scope', stained);
        ctx.restore();
      });
    }
    ctx.restore();

    ctx.beginPath();
    ctx.arc(450, 280, 250, 0, Math.PI * 2);
    ctx.lineWidth = 11; ctx.strokeStyle = '#100D0A'; ctx.stroke();
    ctx.lineWidth = 3; ctx.strokeStyle = '#4A4038'; ctx.stroke();
  }

  // Ported from Design's `drawMarker`, with the part passed in rather than
  // read off component state. The dim, dashed ring is the "there but you
  // cannot see it" case, and it is the instrument's whole argument.
  function drawPartMarker(ctx, part, sp, scope) {
    if (!part) { return; }
    var marks = (part.mark || {})[sp];
    if (!marks || !marks.length) { return; }
    var k = scope ? 0.52 : 1;
    var dim = scope && !part.visible;
    var hue = dim ? "#8F857B" : "#E4572E";
    var pts = marks.map(function (m) {
      return { x: 450 + (m.x - 450) * k, y: 280 + (m.y - 280) * k,
               r: Math.max(11, m.r * k) };
    });
    ctx.save();
    if (dim) { ctx.setLineDash([7, 6]); }
    pts.forEach(function (p, i) {
      ctx.beginPath();
      ctx.arc(p.x, p.y, p.r + 5, 0, Math.PI * 2);
      ctx.lineWidth = i === 0 ? 4 : 2.4;
      ctx.strokeStyle = hue;
      ctx.globalAlpha = i === 0 ? 1 : 0.6;
      ctx.stroke();
    });
    ctx.restore();
    var a = pts[0];
    var bx = a.x + (a.x > 450 ? -(a.r + 26) : a.r + 26);
    var by = a.y - (a.r + 24);
    ctx.beginPath();
    ctx.arc(bx, by, 19, 0, Math.PI * 2);
    ctx.fillStyle = hue; ctx.fill();
    ctx.lineWidth = 2.5; ctx.strokeStyle = scope ? "#100D0A" : "#221E1B"; ctx.stroke();
    ctx.fillStyle = "#FBF3E6";
    ctx.font = '800 21px "Bricolage Grotesque", system-ui, sans-serif';
    ctx.textAlign = "center";
    ctx.textBaseline = "middle";
    ctx.fillText(part.num, bx, by + 1);
  }

  function wireCellBench(sec) {
    var wrap = sec.querySelector(".ks3-bench");
    if (!wrap) { return; }
    var spec;
    try { spec = JSON.parse(wrap.getAttribute("data-cellbench")); }
    catch (err) { return; }

    var canvas = wrap.querySelector("[data-bench-canvas]");
    var caption = wrap.querySelector("[data-bench-caption]");
    var tally = wrap.querySelector("[data-bench-tally]");
    var partBtns = toArray(wrap.querySelectorAll(".ks3-part"));
    var specBtns = toArray(sec.querySelectorAll(".ks3-bench-specimen"));
    var viewBtns = toArray(sec.querySelectorAll(".ks3-bench-view"));
    var gate = sec.querySelector("[data-bench-gate]");
    var R = {
      num: wrap.querySelector("[data-readout-num]"),
      name: wrap.querySelector("[data-readout-name]"),
      where: wrap.querySelector("[data-readout-where]"),
      job: wrap.querySelector("[data-readout-job]"),
      detail: wrap.querySelector("[data-readout-detail]"),
      scope: wrap.querySelector("[data-readout-scope]"),
      scopeWord: wrap.querySelector("[data-readout-scope-word]"),
      scopeNote: wrap.querySelector("[data-readout-scope-note]")
    };

    var specimen = specBtns.length ? specBtns[0].getAttribute("data-specimen")
                                   : spec.specimens[0].id;
    var view = viewBtns.length ? viewBtns[0].getAttribute("data-view") : "diagram";
    var partId = spec.parts[0].id;
    var gateAnswered = !gate;
    var seen = {};

    function specDef(id) {
      for (var i = 0; i < spec.specimens.length; i++) {
        if (spec.specimens[i].id === id) { return spec.specimens[i]; }
      }
      return spec.specimens[0];
    }
    function partDef(id) {
      for (var i = 0; i < spec.parts.length; i++) {
        if (spec.parts[i].id === id) { return spec.parts[i]; }
      }
      return spec.parts[0];
    }

    function paint() {
      if (!canvas || !canvas.getContext) { return; }
      var ctx = canvas.getContext("2d");
      var scope = view === "scope";
      ctx.setTransform(1, 0, 0, 1, 0, 0);
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      ctx.setTransform(2, 0, 0, 2, 0, 0);
      if (scope) { drawScope(ctx, specimen, false); }
      else { drawDiagram(ctx, specimen); }
      drawPartMarker(ctx, partDef(partId), specimen, scope);
      ctx.filter = "none";
      var sp = specDef(specimen);
      canvas.setAttribute("aria-label", sp.alt || "");
      if (caption) { caption.textContent = sp.caption || ""; }
      if (tally) { tally.textContent = sp.tally || ""; }
    }

    function readout() {
      var p = partDef(partId);
      var sp = specDef(specimen);
      var scope = view === "scope";
      // A part that is not in THIS cell reads as absent, whatever the drawing
      // shows — that is the "not there" half of the discrimination.
      var absent = p.where === "plant" && !((p.mark || {})[specimen] || []).length;
      var wl = spec.where_labels || {};
      var key = absent ? "absent" : p.where;
      if (R.num) { R.num.textContent = p.num; }
      if (R.name) { R.name.textContent = p.name; }
      if (R.where) {
        R.where.textContent = (wl[key] || {}).pill || "";
        R.where.setAttribute("data-where", key);
      }
      if (R.job) { R.job.textContent = p.job; }
      if (R.detail) {
        R.detail.textContent = absent && sp.absent_detail ? sp.absent_detail : p.detail;
      }
      // The scope line only exists in the scope view — before the student
      // switches, "you cannot see this one" has nothing to mean.
      setHidden(R.scope, !scope);
      if (scope) {
        var words = spec.scope_words || {};
        if (R.scopeWord) {
          R.scopeWord.textContent = p.visible ? (words.visible || "") : (words.hidden || "");
        }
        if (R.scopeNote) { R.scopeNote.textContent = p.scope_note || ""; }
      }
      each(partBtns, function (b) {
        b.setAttribute("aria-pressed",
          b.getAttribute("data-part") === partId ? "true" : "false");
      });
      // Every tag reads for the CURRENT specimen, so switching the cell
      // repaints the list as well as the drawing.
      each(partBtns, function (b) {
        var pd = partDef(b.getAttribute("data-part"));
        var gone = pd.where === "plant" && !((pd.mark || {})[specimen] || []).length;
        var tag = b.querySelector(".ks3-part-tag");
        if (tag) {
          tag.textContent = ((spec.where_labels || {})[gone ? "absent" : pd.where] || {}).tag
            || (gone ? (specDef(specimen).absent_tag || "") : "");
        }
      });
      seen[specimen + ":" + view] = true;
      markStage(sec, gateAnswered && Object.keys(seen).length >= 2);
    }

    function refresh() { paint(); readout(); }

    each(partBtns, function (b) {
      b.addEventListener("click", function () {
        partId = b.getAttribute("data-part");
        refresh();
      });
    });
    each(specBtns, function (b) {
      b.addEventListener("click", function () {
        specimen = b.getAttribute("data-specimen");
        each(specBtns, function (x) {
          x.setAttribute("aria-pressed",
            x.getAttribute("data-specimen") === specimen ? "true" : "false");
        });
        refresh();
      });
    });
    // Law 4: the scope view is locked until the gate is answered. Guessing
    // how many parts survive a school microscope is the commitment the second
    // view exists to test.
    each(viewBtns, function (b) {
      if (b.getAttribute("data-locked") === "1" && gate) {
        b.setAttribute("disabled", "");
      }
      b.addEventListener("click", function () {
        if (b.hasAttribute("disabled")) { return; }
        view = b.getAttribute("data-view");
        each(viewBtns, function (x) {
          x.setAttribute("aria-pressed",
            x.getAttribute("data-view") === view ? "true" : "false");
        });
        refresh();
      });
    });
    if (gate) {
      var opts = toArray(gate.querySelectorAll(".ks3-option"));
      each(opts, function (o) {
        o.addEventListener("click", function () {
          each(opts, function (x) { x.setAttribute("aria-pressed", "false"); });
          o.setAttribute("aria-pressed", "true");
          gateAnswered = true;
          each(viewBtns, function (x) { x.removeAttribute("disabled"); });
          readout();
        });
      });
    }
    refresh();
  }

  /* The two-way sorter. Nothing is marked here and the intro says so. */
  function wirePairs(sec) {
    var rows = toArray(sec.querySelectorAll(".ks3-pairrow"));
    var btn = sec.querySelector("[data-pair-reveal]");
    var prog = sec.querySelector("[data-pair-progress]");
    var panel = sec.querySelector("[data-pair-panel]");
    if (!rows.length) { return; }
    var total = rows.length;
    var unit = (prog && prog.getAttribute("data-unit")) || "sent";

    function sent() {
      var n = 0;
      each(rows, function (r) {
        if (r.querySelector('.ks3-pair-chip[aria-pressed="true"]')) { n += 1; }
      });
      return n;
    }
    function repaint() {
      var n = sent();
      each(rows, function (r) {
        r.setAttribute("data-sent",
          r.querySelector('.ks3-pair-chip[aria-pressed="true"]') ? "1" : "0");
      });
      if (prog) { prog.textContent = n + " of " + total + " " + unit; }
      if (btn) {
        if (n < total) { btn.setAttribute("disabled", ""); }
        else { btn.removeAttribute("disabled"); }
      }
    }
    each(rows, function (row) {
      var chips = toArray(row.querySelectorAll(".ks3-pair-chip"));
      each(chips, function (c) {
        c.addEventListener("click", function () {
          each(chips, function (b) { b.setAttribute("aria-pressed", "false"); });
          c.setAttribute("aria-pressed", "true");
          repaint();
        });
      });
    });
    if (btn) {
      btn.addEventListener("click", function () {
        if (sent() < total) { return; }
        each(rows, function (r) { setHidden(r.querySelector("[data-reveal]"), false); });
        setHidden(panel, false);
        btn.setAttribute("aria-expanded", "true");
        markStage(sec, true);   // `answers_opened`
      });
    }
    repaint();
  }

  /* Build it, then run it. The cell tells you what you got away with. */
  function wireFit(sec) {
    var wrap = sec.querySelector(".ks3-fit");
    if (!wrap) { return; }
    var spec;
    try { spec = JSON.parse(wrap.getAttribute("data-fit-spec")); }
    catch (err) { return; }
    var L = spec.labels || {};

    var tabs = toArray(wrap.querySelectorAll(".ks3-fit-tab"));
    var list = wrap.querySelector("[data-fit-parts]");
    var runBtn = wrap.querySelector("[data-fit-run]");
    var clearBtn = wrap.querySelector("[data-fit-clear]");
    var prog = wrap.querySelector("[data-fit-progress]");
    var out = wrap.querySelector("[data-reveal]");
    var verdict = wrap.querySelector("[data-fit-verdict]");
    var findings = wrap.querySelector("[data-fit-findings]");
    var note = wrap.querySelector("[data-fit-note]");
    var jobLabel = wrap.querySelector(".ks3-fit-job-label");
    var jobText = wrap.querySelector(".ks3-fit-job-text");
    var jobWhere = wrap.querySelector(".ks3-fit-job-where");
    var installLabel = wrap.querySelector(".ks3-fit-install-label");

    // The parts list is the BENCH's, named by `parts_from`, so a part cannot
    // exist in the builder and not on the bench.
    var bench = document.querySelector("[data-cellbench]");
    var allParts = [];
    if (bench) {
      try { allParts = JSON.parse(bench.getAttribute("data-cellbench")).parts; }
      catch (err) { allParts = []; }
    }

    var current = spec.specimens[0].id;
    var installed = {};
    var ran = {};

    function def(id) {
      for (var i = 0; i < spec.specimens.length; i++) {
        if (spec.specimens[i].id === id) { return spec.specimens[i]; }
      }
      return spec.specimens[0];
    }

    function renderParts() {
      if (!list) { return; }
      list.innerHTML = "";
      var chosen = installed[current] || {};
      allParts.forEach(function (p) {
        var li = document.createElement("li");
        var b = document.createElement("button");
        b.type = "button";
        b.className = "ks3-fit-part";
        b.setAttribute("data-part", p.id);
        b.setAttribute("aria-pressed", chosen[p.id] ? "true" : "false");
        b.appendChild(document.createTextNode(p.name));
        b.addEventListener("click", function () {
          var c = installed[current] || (installed[current] = {});
          if (c[p.id]) { delete c[p.id]; } else { c[p.id] = true; }
          renderParts();
          repaint();
        });
        li.appendChild(b);
        list.appendChild(li);
      });
    }

    function count() { return Object.keys(installed[current] || {}).length; }

    function repaint() {
      if (installLabel) { installLabel.textContent = L.install || ""; }
      if (jobLabel) { jobLabel.textContent = L.job || ""; }
      var d = def(current);
      if (jobText) { jobText.textContent = d.job || ""; }
      if (jobWhere) { jobWhere.textContent = d.where || ""; }
      if (clearBtn) { clearBtn.textContent = L.clear || ""; }
      if (runBtn) {
        runBtn.textContent = ran[current] ? (L.rerun || "") : (L.run || "");
        if (!count()) { runBtn.setAttribute("disabled", ""); }
        else { runBtn.removeAttribute("disabled"); }
      }
      if (prog) {
        prog.textContent = count()
          ? count() + " " + (L.installed || "")
          : (L.empty || "");
      }
      each(tabs, function (tb) {
        tb.setAttribute("aria-pressed",
          tb.getAttribute("data-fit") === current ? "true" : "false");
      });
      markStage(sec, Object.keys(ran).length === spec.specimens.length);
    }

    function run() {
      var d = def(current);
      var chosen = installed[current] || {};
      var needs = d.needs || [];
      var missing = needs.filter(function (id) { return !chosen[id]; });
      var extra = Object.keys(chosen).filter(function (id) {
        return needs.indexOf(id) < 0;
      });
      ran[current] = true;
      var W = spec.finding_words || {};
      if (verdict) {
        verdict.textContent = !missing.length && !extra.length
          ? (spec.verdicts || {}).ok || "It runs."
          : ((spec.verdicts || {}).problem || "It runs, after a fashion.");
      }
      if (findings) {
        findings.innerHTML = "";
        function add(kind, id, word) {
          var p = null;
          allParts.forEach(function (x) { if (x.id === id) { p = x; } });
          var li = document.createElement("li");
          li.className = "ks3-fit-finding";
          li.setAttribute("data-kind", kind);
          var s = document.createElement("strong");
          s.appendChild(document.createTextNode((p ? p.name : id) + "."));
          li.appendChild(s);
          li.appendChild(document.createTextNode(" " + word));
          findings.appendChild(li);
        }
        missing.forEach(function (id) {
          add("missing", id, (spec.consequence || {})[id] || W.missing || "");
        });
        extra.forEach(function (id) {
          add("extra", id, (d.waste || {})[id] || spec.waste_fallback || "");
        });
      }
      if (note) { note.textContent = d.note || ""; }
      setHidden(out, false);
      if (out) { out.setAttribute("role", "status"); }
      repaint();
    }

    each(tabs, function (tb) {
      tb.addEventListener("click", function () {
        current = tb.getAttribute("data-fit");
        setHidden(out, true);
        renderParts();
        repaint();
      });
    });
    if (runBtn) { runBtn.addEventListener("click", function () { if (count()) { run(); } }); }
    if (clearBtn) {
      clearBtn.addEventListener("click", function () {
        installed[current] = {};
        setHidden(out, true);
        renderParts();
        repaint();
      });
    }
    renderParts();
    repaint();
  }


  /* ═══════════════════════════════════════════════════════════════
     b1-02 — MRB-204's remaining three formula components and the
     step critique. Ruled by Mide: a KS3 formula gets all four, in
     order, and steps 3 and 4 are the ones that teach.
     ═══════════════════════════════════════════════════════════════ */

  function wireCritique(sec) {
    var steps = toArray(sec.querySelectorAll(".ks3-step"));
    var btn = sec.querySelector("[data-steps-reveal]");
    var prog = sec.querySelector("[data-steps-progress]");
    if (!steps.length) { return; }
    var zero = (prog && prog.getAttribute("data-zero")) || "Pick at least one";

    function picked() {
      var n = 0;
      each(steps, function (s) {
        if (s.querySelector('.ks3-step-btn[aria-pressed="true"]')) { n += 1; }
      });
      return n;
    }
    function repaint() {
      var n = picked();
      if (prog) {
        prog.textContent = n
          ? n + " of " + steps.length + " marked"
          : zero;
      }
      if (btn) {
        if (!n) { btn.setAttribute("disabled", ""); }
        else { btn.removeAttribute("disabled"); }
      }
    }
    each(steps, function (s) {
      var b = s.querySelector(".ks3-step-btn");
      // A checkbox set: each toggles on its own and never unpicks a sibling.
      b.addEventListener("click", function () {
        b.setAttribute("aria-pressed",
          b.getAttribute("aria-pressed") === "true" ? "false" : "true");
        repaint();
      });
    });
    if (btn) {
      btn.addEventListener("click", function () {
        if (!picked()) { return; }
        each(steps, function (s) { setHidden(s.querySelector("[data-reveal]"), false); });
        btn.setAttribute("aria-expanded", "true");
        markStage(sec, true);   // `steps_opened`
      });
    }
    repaint();
  }

  /* MRB-204 step 3. One way — there is no collapse, because unshowing a step
     teaches nothing and gives a student a way to lose their place. */
  function wireStepper(sec) {
    var wrap = sec.querySelector("[data-stepper]");
    if (!wrap) { return; }
    var lines = toArray(wrap.querySelectorAll("[data-step]"));
    var btn = wrap.querySelector("[data-step-next]");
    var total = lines.length;
    var shown = 0;
    var nextWord = wrap.getAttribute("data-next") || "Show the next step";
    var doneWord = wrap.getAttribute("data-done") || "All steps shown";
    if (!btn) { return; }
    btn.addEventListener("click", function () {
      if (shown >= total) { return; }
      setHidden(lines[shown], false);
      shown += 1;
      if (shown >= total) {
        btn.textContent = doneWord;
        btn.setAttribute("disabled", "");
        markStage(sec, true);   // `all_steps_shown`
      } else {
        btn.textContent = nextWord;
      }
    });
  }

  /* MRB-204 step 4. Law 5's "the same artifact, produced by the student". */
  function wireConstruct(sec) {
    var wrap = sec.querySelector(".ks3-construct");
    if (!wrap) { return; }
    var inputs = toArray(wrap.querySelectorAll("[data-fifa-input]"));
    var btn = wrap.querySelector("[data-construct-check]");
    var hint = wrap.querySelector("[data-construct-hint]");
    var out = wrap.querySelector("[data-reveal]");
    var tally = wrap.querySelector("[data-construct-tally]");
    var ticks = toArray(wrap.querySelectorAll("[data-crit]"));

    function written() {
      var n = 0;
      each(inputs, function (i) { if (i.value.trim()) { n += 1; } });
      return n;
    }
    function repaint() {
      var n = written();
      // ⊕ Design's Check accepts an EMPTY attempt and reveals the full model.
      // A student who taps it first has been handed the answer before writing
      // anything, which is the whole thing steps 3 and 4 exist to prevent.
      if (btn) {
        if (!n) { btn.setAttribute("disabled", ""); }
        else { btn.removeAttribute("disabled"); }
      }
      if (hint) {
        hint.textContent = n
          ? n + " of " + inputs.length + " written"
          : "Write at least one step first";
      }
    }
    each(inputs, function (i) {
      i.addEventListener("input", repaint);
      i.addEventListener("change", repaint);
    });
    if (btn) {
      btn.addEventListener("click", function () {
        if (!written()) { return; }
        setHidden(out, false);
        if (out) { out.setAttribute("role", "status"); }
        btn.setAttribute("aria-expanded", "true");
      });
    }
    // R8: the student marks themselves. Nothing here checks their arithmetic.
    each(ticks, function (c) {
      c.addEventListener("change", function () {
        var all = ticks.every(function (x) { return x.checked; });
        setHidden(tally, !all);
        markStage(sec, all);   // `attempt_checked`
      });
    });
    repaint();
  }

  /* MRB-204 step 2. Cover the one you want. */
  function wireTriangle(root) {
    each(root.querySelectorAll("[data-triangle]"), function (tri) {
      var btns = toArray(tri.querySelectorAll(".ks3-tri-btn"));
      var notes = toArray(tri.querySelectorAll(".ks3-tri-note"));
      each(btns, function (b) {
        b.addEventListener("click", function () {
          var key = b.getAttribute("data-cover");
          var on = tri.getAttribute("data-covered") === key;
          if (on) { tri.removeAttribute("data-covered"); }
          else { tri.setAttribute("data-covered", key); }
          each(btns, function (x) {
            x.setAttribute("aria-pressed",
              !on && x.getAttribute("data-cover") === key ? "true" : "false");
          });
          each(notes, function (n) {
            setHidden(n, on || n.getAttribute("data-note") !== key);
          });
        });
      });
    });
  }

  function wireInstruments(root) {
    each(root.querySelectorAll("[data-board]"), wireBoard);
    each(root.querySelectorAll("[data-sort]"), wireSort);
    each(root.querySelectorAll("[data-settles]"), wireSettles);
    // The sabotage engine listens for the bench's cell, so it is wired
    // FIRST — otherwise the bench's opening broadcast lands on nothing.
    each(root.querySelectorAll("[data-sabotage]"), wireSabotage);
    each(root.querySelectorAll("[data-benchblock]"), wireBench);
    each(root.querySelectorAll("[data-zoomblock]"), wireZoom);
    each(root.querySelectorAll("[data-hard]"), wireHard);
    each(root.querySelectorAll("[data-removal]"), wireRemoval);
    // The builder reads the bench's parts list, so the bench is wired first.
    each(root.querySelectorAll("[data-cellbench]"), wireCellBench);
    each(root.querySelectorAll("[data-pairs]"), wirePairs);
    each(root.querySelectorAll("[data-fitblock]"), wireFit);
    each(root.querySelectorAll("[data-critique]"), wireCritique);
    each(root.querySelectorAll("[data-construct]"), wireConstruct);
    each(root.querySelectorAll("[data-stepper]"), function (w) {
      wireStepper(w.closest("[data-activity]") || w.parentNode);
    });
    wireTriangle(root);
  }

  // ── the progress rail (MRB-208 rule 2) ──────────────────────────────
  //
  // ⚖️ BOTH VARIANTS TICK ON COMPLETION, AND NOTHING IS TICKED ON LOAD.
  //
  // Design's delivered narrow variant was IntersectionObserver-driven only, so
  // it read "4 / 4" with a full accent bar for a student who had scrolled to
  // the bottom and answered nothing — and below 1340px it is the only rail a
  // student ever sees. Ruled on MRB-208: the rail records PARTICIPATION, which
  // is what keeps it consistent with R3. A stop ticks when the activity is
  // finished, right or wrong.
  //
  // What stays scroll-driven is the side rail's CURRENT ring and the top bar's
  // CURRENT LABEL — those answer "where am I", not "how far have I got", and
  // Design drew them that way. Count and fill are completion.
  //
  // A stage is done when its section says so. Any component may declare its own
  // completion by setting `data-stage-done="1"` on the section, which is the
  // contract an instrument should use — it knows what finished means and the
  // rail does not. `doneByDom` is the fallback for plain option blocks, and it
  // is deliberately generous in the same direction as the ruling: a commitment
  // made is a stage done.
  function doneByDom(sec) {
    if (!sec) { return false; }
    // ⚠️ The declaration is AUTHORITATIVE in both directions. This used to
    // check only for "1" and fall through to the heuristics below on "0",
    // which is how an instrument that says plainly "I am not finished" got
    // overruled by a guess. Measured on b1-06: `#s-scope` ticked on PAGE LOAD,
    // because the last clause matches any `aria-pressed="true"` and the sim's
    // motion toggle and fallback centre button are both built pressed while
    // the sim is still locked. MRB-208 ruled that nothing is ticked on load.
    if (sec.hasAttribute("data-stage-done")) {
      return sec.getAttribute("data-stage-done") === "1";
    }

    // The mastery ladder: every rung either answered or self-checked.
    var rungs = sec.querySelectorAll(".ks3-rung");
    if (rungs.length) {
      for (var r = 0; r < rungs.length; r++) {
        var marked = rungs[r].querySelector('.ks3-option[aria-pressed="true"], .ks3-option.is-correct, .ks3-option.is-wrong');
        var checked = rungs[r].querySelector("[data-ticks]:not([hidden])");
        if (!marked && !checked) { return false; }
      }
      return true;
    }

    // A reveal that has been opened is an activity carried through to its end.
    var opened = sec.querySelector('[data-reveal]:not([hidden]), .ks3-reveal-btn[aria-expanded="true"]');
    if (opened) { return true; }

    // Otherwise: any commitment at all inside this section — but a COMMITMENT,
    // which is an answer button. A bare `[aria-pressed="true"]` also matches
    // every segmented sim control and every specimen tab, and those are built
    // pressed to show where the slide is, not to record that a student decided
    // anything. Same defect as the one above, reached by a different route.
    return !!sec.querySelector('.ks3-option[aria-pressed="true"]');
  }

  function wireRail(wrap) {
    var stages;
    try { stages = JSON.parse(wrap.getAttribute("data-rail-stages") || "[]"); }
    catch (err) { stages = []; }
    if (!stages.length) { return; }

    var nodes = toArray(wrap.querySelectorAll('[data-rail="side"] li'));
    var count = wrap.querySelector("[data-rail-count]");
    var label = wrap.querySelector("[data-rail-label]");
    var fill = wrap.querySelector("[data-rail-fill]");
    var active = 0;

    function sectionFor(i) { return document.getElementById(stages[i].anchor); }

    function paint() {
      var done = 0;
      for (var i = 0; i < stages.length; i++) {
        var isDone = doneByDom(sectionFor(i));
        if (isDone) { done++; }
        var li = nodes[i];
        if (li) {
          li.classList.toggle("is-done", isDone);
          li.classList.toggle("is-current", i === active && !isDone);
          var chip = li.querySelector(".ks3-rail-chip");
          // The drawn mark, never a typed ✓ — same rule as the ladder's.
          if (chip) {
            var hasMark = !!chip.querySelector("svg");
            if (isDone && !hasMark) { chip.innerHTML = TICK_SVG; }
            else if (!isDone && hasMark) { chip.textContent = String(i + 1); }
          }
        }
      }
      if (count) { count.textContent = done + " / " + stages.length; }
      if (fill) { fill.style.width = (done / stages.length * 100) + "%"; }
      if (label) { label.textContent = stages[active].label || ""; }
    }

    // Scroll drives CURRENT only. Same rootMargin Design used, so the stage
    // changes at the same scroll position it does on the approved page.
    if (window.IntersectionObserver) {
      var io = new IntersectionObserver(function (entries) {
        for (var i = 0; i < entries.length; i++) {
          if (!entries[i].isIntersecting) { continue; }
          var idx = stages.map(function (s) { return s.anchor; })
                          .indexOf(entries[i].target.id);
          if (idx >= 0) { active = idx; }
        }
        paint();
      }, { rootMargin: "-45% 0px -50% 0px" });
      for (var i = 0; i < stages.length; i++) {
        var sec = sectionFor(i);
        if (sec) { io.observe(sec); }
      }
    }

    // Completion is recomputed after anything the student does. Cheap, and it
    // cannot go stale the way a set of per-component callbacks can.
    each(["click", "change", "input"], function (evt) {
      document.addEventListener(evt, function () { window.setTimeout(paint, 0); }, true);
    });
    paint();
  }

  function init() {
    wirePredictions(document);
    wireCriteria(document);
    wireCards(document);
    wireSims(document);
    wireInstruments(document);
    wireMotion(document);
    each(document.querySelectorAll(".ks3-ladder"), wireLadder);
    each(document.querySelectorAll(".ks3-rails"), wireRail);
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
