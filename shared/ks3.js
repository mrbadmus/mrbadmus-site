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

  /* ── the visit log (MRB-212) ────────────────────────────────────
     ks3_visits — { "<slug>": { t: <epoch ms>, done: <bool> } }

     One key for the whole key stage rather than one per lesson: the hub's
     picker has to sort ALL published lessons on open, and 183 separate
     getItem calls to answer one question is the wrong shape.

     It records that a lesson was OPENED, which is what "pick up where you
     left off" means. `done` is set by the ladder when a student resolves
     all four rungs — a finished lesson drops out of the picker rather
     than nagging from the top of it.

     Capped at the 50 most recent so it cannot grow without bound on a
     shared classroom machine. Same wrapped access as everything else:
     private mode degrades to "works but does not remember", never throws.

     ⚠️ Deliberately LOCAL ONLY. Server-side progress logging is broken
     platform-wide; this neither calls it nor waits on it. */
  var VISITS_KEY = "ks3_visits";
  var VISITS_CAP = 50;

  function readVisits() {
    var v = readStore(VISITS_KEY);
    return (v && typeof v === "object" && !(v instanceof Array)) ? v : {};
  }

  function writeVisits(map) {
    var slugs = Object.keys(map);
    if (slugs.length > VISITS_CAP) {
      slugs.sort(function (a, b) { return (map[b].t || 0) - (map[a].t || 0); });
      var trimmed = {};
      slugs.slice(0, VISITS_CAP).forEach(function (s) { trimmed[s] = map[s]; });
      map = trimmed;
    }
    writeStore(VISITS_KEY, map);
  }

  /* Merges, never replaces: opening a finished lesson again refreshes its
     timestamp without un-finishing it. */
  function markVisit(slug, done) {
    if (!slug) { return; }
    var map = readVisits();
    var rec = map[slug] || {};
    rec.t = Date.now();
    if (done) { rec.done = true; }
    map[slug] = rec;
    writeVisits(map);
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
      /* MRB-212: all four rungs resolved means finished, whatever the
         score. The picker stops offering it — "pick up where you left
         off" is about unfinished work, not about marks. */
      if (resolved) { markVisit(slug, true); }
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
    medium:      "What it spreads through"
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

  function wireSim(sim) {
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
        input.addEventListener("input", function () {
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
      each(activity.querySelectorAll(".ks3-option"), function (btn) {
        btn.addEventListener("click", unlock);
      });
      draw();   // the frozen first frame behind the veil
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
    each(root.querySelectorAll(".ks3-sim"), wireSim);
  }

  /* ── the hub's lesson picker (MRB-212) ──────────────────────────
     A disclosure button over two groups. The server rendered every
     published lesson into "Start something new"; this moves the ones the
     browser has seen into "Pick up where you left off" and hides whichever
     group ends up empty.

     Every row is already a real <a href> — nothing here creates a control,
     it only reorders and hides. With this function never running, the panel
     is still a correct (if unsorted) list of every published lesson. */
  var RESUME_MAX = 5;
  var NEW_MAX = 10;

  function wirePicker(root) {
    var btn = root.querySelector(".ks3-picker-btn");
    var panel = root.querySelector(".ks3-picker-panel");
    if (!btn || !panel) { return; }

    var groups = {};
    each(panel.querySelectorAll(".ks3-picker-group"), function (g) {
      groups[g.getAttribute("data-group")] = g;
    });
    // Cached at wire time: arrange() detaches every row before re-placing
    // them, so the DOM cannot be the list of what exists.
    var rows = toArray(panel.querySelectorAll("li[data-slug]"));

    function links() { return toArray(panel.querySelectorAll("a")); }

    function arrange() {
      var visits = readVisits();
      var resume = [];
      var fresh = [];
      rows.forEach(function (li) {
        var rec = visits[li.getAttribute("data-slug")];
        if (rec && rec.t && !rec.done) {
          resume.push(li);
        } else if (!rec) {
          fresh.push(li);
        }
        // A finished lesson appears in neither group.
        if (li.parentNode) { li.parentNode.removeChild(li); }
      });
      resume.sort(function (a, b) {
        return (visits[b.getAttribute("data-slug")].t
                - visits[a.getAttribute("data-slug")].t);
      });
      fill(groups.resume, resume.slice(0, RESUME_MAX));
      fill(groups["new"], fresh.slice(0, NEW_MAX));
    }

    function fill(group, items) {
      if (!group) { return; }
      var ul = group.querySelector(".ks3-picker-list");
      items.forEach(function (li) { ul.appendChild(li); });
      setHidden(group, items.length === 0);
    }

    function isOpen() { return btn.getAttribute("aria-expanded") === "true"; }

    function open() {
      arrange();
      btn.setAttribute("aria-expanded", "true");
      setHidden(panel, false);
      var first = links()[0];
      if (first) { first.focus(); }
    }

    function close(refocus) {
      btn.setAttribute("aria-expanded", "false");
      setHidden(panel, true);
      if (refocus) { btn.focus(); }
    }

    btn.addEventListener("click", function () {
      if (isOpen()) { close(false); } else { open(); }
    });

    // Escape closes from anywhere inside, and hands focus back to the
    // control that opened it — otherwise focus is stranded on a hidden row.
    panel.addEventListener("keydown", function (ev) {
      if (ev.key === "Escape" || ev.key === "Esc") {
        ev.preventDefault();
        close(true);
        return;
      }
      if (ev.key !== "ArrowDown" && ev.key !== "ArrowUp") { return; }
      var all = links();
      var i = all.indexOf(document.activeElement);
      if (i < 0) { return; }
      ev.preventDefault();
      var next = ev.key === "ArrowDown" ? i + 1 : i - 1;
      if (next < 0) { next = all.length - 1; }
      if (next >= all.length) { next = 0; }
      all[next].focus();
    });

    btn.addEventListener("keydown", function (ev) {
      if (isOpen() && (ev.key === "Escape" || ev.key === "Esc")) {
        ev.preventDefault();
        close(true);
      }
    });

    // Click or tap outside. `pointerdown` rather than `click` so a tap that
    // starts outside closes it without also firing at the new target.
    document.addEventListener("pointerdown", function (ev) {
      if (!isOpen()) { return; }
      if (panel.contains(ev.target) || btn.contains(ev.target)) { return; }
      close(false);
    });
  }

  function init() {
    wirePredictions(document);
    wireCriteria(document);
    wireCards(document);
    wireSims(document);
    each(document.querySelectorAll(".ks3-ladder"), wireLadder);
    wirePicker(document);
    // The page IS a lesson — record the visit. `data-ks3-lesson` is on
    // <body> for every lesson page, written or not, which is why the
    // ladder's own `data-lesson` could not be the source.
    markVisit(document.body ? document.body.getAttribute("data-ks3-lesson") : null);
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
