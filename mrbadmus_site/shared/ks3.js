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
    var badge = wrap.querySelector("[data-fit-badge]");
    var verdict = wrap.querySelector("[data-fit-verdict]");
    var findings = wrap.querySelector("[data-fit-findings]");
    var note = wrap.querySelector("[data-fit-note]");
    var jobLabel = wrap.querySelector(".ks3-fit-job-label");
    var jobText = wrap.querySelector(".ks3-fit-job-text");
    var jobWhere = wrap.querySelector(".ks3-fit-job-where");
    var installLabel = wrap.querySelector(".ks3-fit-install-label");

    // The parts list is the BENCH's, named by `parts_from`, so a part cannot
    // exist in the builder and not on the bench.
    //
    // ⊕ MRB-242 — resolve the bench through the id `parts_from` NAMES, never
    // through `document.querySelector("[data-cellbench]")`. Two emitters chose
    // that attribute name: the cell-bench SECTION carries it valueless as the
    // JS dispatch marker, and the bench's own <div> carries the JSON payload.
    // The section comes first in the document, so the old line got `""`, threw
    // in JSON.parse, and the bare `catch` below rendered zero chips and left
    // the run button permanently disabled — the whole instrument, silently.
    // The failure is now LOUD, because a silent one is what shipped this.
    var benchSec = spec.parts_from
      ? document.querySelector('[data-activity="' + spec.parts_from + '"]')
      : null;
    var bench = benchSec && benchSec.querySelector("[data-cellbench]");
    var allParts = [];
    if (bench) {
      try { allParts = JSON.parse(bench.getAttribute("data-cellbench")).parts || []; }
      catch (err) {
        console.error("wireFit: parts_from=" + spec.parts_from +
                      " resolved to a bench whose payload will not parse", err);
      }
    }
    if (!allParts.length) {
      console.error("wireFit: no parts to install. parts_from=" +
                    JSON.stringify(spec.parts_from) + " named " +
                    (benchSec ? "a section with no [data-cellbench] payload"
                              : "no activity on this page") + ".");
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
        // ⊕ MRB-242 — Design's chip is a numbered pill, and the number is the
        // SAME number the bench gave that part. It is the bench's badge
        // component (`.ks3-part-num`), reused rather than copied: one badge,
        // a dark branch in the stylesheet, exactly as the segmented control
        // is one control with two class names.
        if (p.num) {
          var n = document.createElement("span");
          n.className = "ks3-part-num";
          n.setAttribute("aria-hidden", "true");
          n.appendChild(document.createTextNode(p.num));
          b.appendChild(n);
        }
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
        // ⊕ MRB-242 — Design's foot hint is "3 of 7 installed": the total is
        // the parts list's own length, so it cannot disagree with the chips
        // above it. The shipped line dropped "of 7" and read "3 installed".
        prog.textContent = count()
          ? count() + " of " + allParts.length + " " + (L.installed || "")
          : (L.empty || "");
      }
      each(tabs, function (tb) {
        tb.setAttribute("aria-pressed",
          tb.getAttribute("data-fit") === current ? "true" : "false");
      });
      // ⊕ MRB-242 — the BLOCK-HEAD counter Design draws beside the <h2>:
      // "0 of 4 cells run". Cells RUN, not cells touched — the same predicate
      // the stage below ticks on, so the head and the rail cannot disagree.
      setCount(sec, Object.keys(ran).length);
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
      // ⊕ MRB-242 — THREE states, not two, and Design's own line is the rule:
      //   const status = missing.length ? 'fails' : (extra.length ? 'waste' : 'works');
      // (b1-03 reference, line 961). Anything missing fails outright — a cell
      // short of a part does not get partial credit for the parts it has;
      // complete-but-with-spares is `waste`; only exactly-the-needs `works`.
      //
      // This read `verdicts.ok` / `verdicts.problem`, which nothing authors,
      // so it always fell through to two strings hardcoded here and the
      // lesson's five headlines and three badges never reached a student.
      // Those fallbacks are gone: `r_fit_parts` fails the BUILD on a missing
      // headline, so there is nothing left for a fallback to cover, and
      // inventing student-facing prose in the engine is what caused this.
      var V = spec.verdicts || {};
      var status = missing.length ? "fails" : (extra.length ? "waste" : "works");
      var vd = V[status] || {};
      // One part short reads "One part short."; two or more substitute the
      // count into the plural headline, which is authored with `{n}`.
      var headline = status === "fails"
        ? (missing.length === 1
             ? vd.headline_one
             : String(vd.headline_many || "").replace(/\{n\}/g, missing.length))
        : vd.headline;
      if (badge) {
        badge.textContent = vd.badge || "";
        // The state drives the pill's fill in the stylesheet — alert tint,
        // band, accent tint — exactly as Design branches `verdictBadgeStyle`.
        badge.setAttribute("data-state", status);
      }
      if (verdict) { verdict.textContent = headline || ""; }
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
    // ⊕ MRB-220 (map N5). Two readouts Design draws and the shipped stepper
    // had no field for: a live "Step {n} of 4" in the block head, and the
    // sentence beside the button that hands the student on to the next block.
    var doneNote = wrap.querySelector("[data-step-donenote]");
    if (!btn) { return; }
    setCount(sec, 0);
    btn.addEventListener("click", function () {
      if (shown >= total) { return; }
      setHidden(lines[shown], false);
      shown += 1;
      setCount(sec, shown);
      if (shown >= total) {
        btn.textContent = doneWord;
        btn.setAttribute("disabled", "");
        if (doneNote) { setHidden(doneNote, false); }
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

  /* MRB-204 step 2. Cover the one you want.
     ⊖ SUPERSEDED 16 Aug 2026 (MRB-228) and deleted here. The B2 splice appends
     a widened `wireTriangle` in this same function scope, and the later
     declaration wins for the whole scope — so this body has been unreachable
     since b2-04 landed, and every call already resolved to the widened one.
     Deleting unreachable code cannot change behaviour, and leaving it is the
     exact hazard the splice markers exist to prevent: two copies of one
     function, with only the live one's bugs visible. The widened version is
     below, beside the rest of the B2 wiring. */

  /* ═══════════════════════════════════════════════════════════════
     B2 · Movement: skeleton and muscles  (⊕ 16 Aug 2026, MRB-220)

     Four instruments, and two pieces three of them share.

     ⚖️ REDUCED MOTION IS ASKED EVERY FRAME, not once at construction.
     Design's b2-03 reads `prefers-reduced-motion` in `componentDidMount`
     and never consults it again, so the arm animates under reduced
     motion; its own sibling b2-02 checks correctly inside the tick. That
     is a slip rather than an intention, and a ruling already covers it
     (R6: reduced motion is a COMPLETE experience, never a lesser one),
     so it is corrected here rather than reproduced. Asking live also
     means the Motion control and an OS setting changed mid-lesson both
     take effect without a reload.
     ═══════════════════════════════════════════════════════════════ */

  var B2_RM = window.matchMedia
    && window.matchMedia("(prefers-reduced-motion: reduce)");

  function motionReduced() {
    if (document.documentElement.getAttribute("data-motion") === "off") {
      return true;
    }
    return !!(B2_RM && B2_RM.matches);
  }

  /* The block head's live progress readout. Three authored shapes — a count
     ("3 of 6 decided"), a two-state label ("Meter fitted") and a count with
     a bespoke zero ("All three claims on" → "2 switched off") — one element
     and one updater, so a fourth cannot arrive as a fourth copy. */
  function setCount(sec, n, extra) {
    var el = sec && sec.querySelector("[data-count]");
    if (!el) { return; }
    var fmt = el.getAttribute("data-format");
    // ⊕ C2. `data-zero` is opt-in, so every shipped counter still opens on
    // its own "0 of 6 decided" and only c2-01's reads a sentence at zero.
    var zero = el.getAttribute("data-zero");
    if (fmt && zero && !n) { el.textContent = zero; return; }
    // ⊕ C2. `extra` carries the live numbers that are NOT the count —
    // c2-02's budget line quotes both "{left}" and "{n}" and the two move
    // independently. Constants like "{budget}" were baked in at build time.
    if (fmt && extra) {
      for (var k in extra) {
        if (Object.prototype.hasOwnProperty.call(extra, k)) {
          fmt = fmt.split("{" + k + "}").join(String(extra[k]));
        }
      }
    }
    if (fmt) {
      // ⊕ CLAMPED. b2-03's counter runs over a mixed key space — four
      // contraction modes and two kill switches — so a student who tries
      // three modes and both switches reads "5 of 4 settings tried" on
      // Design's own page. Clamping does not contradict the drawn label; it
      // is the label meaning what it says. What ticks is unchanged.
      var total = parseInt(el.getAttribute("data-total"), 10);
      if (!isNaN(total) && n > total) { n = total; }
      el.textContent = fmt.replace("{n}", String(n))
        .replace("{total}", el.getAttribute("data-total") || "");
    } else {
      el.textContent = n ? (el.getAttribute("data-on") || "")
                         : (el.getAttribute("data-off") || "");
    }
  }

  /* C6's commit gate. Answered, the gate is GONE and the instrument
     arrives in the space the question was occupying — gating by absence,
     which is what Design draws on three of the four B2 pages. */
  function wireBenchGate(sec) {
    var gate = sec.querySelector("[data-benchgate]");
    var body = sec.querySelector("[data-benchbody]");
    if (!gate || !body) { return; }
    each(gate.querySelectorAll(".ks3-option"), function (btn) {
      btn.addEventListener("click", function () {
        each(gate.querySelectorAll(".ks3-option"), function (b) {
          b.setAttribute("aria-pressed", "false");
        });
        btn.setAttribute("aria-pressed", "true");
        setHidden(gate, true);
        setHidden(body, false);
        body.setAttribute("role", "status");
      });
    });
  }

  /* job-sort — the per-item sorter. Each row opens the instant IT is
     decided, which is the whole difference from `sort-task`: a student
     finds out about item 1 before committing on item 2.

     ⚖️ Nothing marks correctness (R3 / MRB-196 R10). The chosen option
     keeps the ordinary chosen treatment, the rest dim, the ROW's border
     goes to ink, and the why paragraph is one tone either way. */
  function wireJobSort(sec) {
    var wrap = sec.querySelector("[data-jobsort]");
    if (!wrap) { return; }
    var items = toArray(wrap.querySelectorAll(".ks3-jobsort-item"));
    var total = parseInt(wrap.getAttribute("data-total"), 10) || items.length;
    var closer = wrap.querySelector("[data-jobsort-close]");

    function decided() {
      var n = 0;
      each(items, function (it) {
        if (it.getAttribute("data-open") === "1") { n += 1; }
      });
      return n;
    }

    each(items, function (item) {
      var opts = toArray(item.querySelectorAll(".ks3-jobsort-opt"));
      each(opts, function (btn) {
        btn.addEventListener("click", function () {
          // One commitment per row, and it is final: the reveal is
          // already on screen, so a second pick would be choosing after
          // reading the answer.
          if (item.getAttribute("data-open") === "1") { return; }
          each(opts, function (b) {
            b.setAttribute("aria-pressed", "false");
            b.setAttribute("disabled", "");
          });
          btn.setAttribute("aria-pressed", "true");
          item.setAttribute("data-open", "1");
          setHidden(item.querySelector("[data-reveal]"), false);
          var n = decided();
          setCount(sec, n);
          if (n >= total) {
            if (closer) { setHidden(closer, false); }
            markStage(sec, true);
          }
        });
      });
    });
    setCount(sec, 0);
  }

  /* system-switch — take one part away and follow the damage.
     Emit-all-show-one: four panels in the document, one shown, so going
     back to a part finds it exactly as it was left. */
  function wireSwitch(sec) {
    var wrap = sec.querySelector("[data-switch-block]");
    if (!wrap) { return; }
    var tabs = toArray(wrap.querySelectorAll(".ks3-switch-tab"));
    var panels = toArray(wrap.querySelectorAll(".ks3-switch-panel"));
    var total = parseInt(wrap.getAttribute("data-total"), 10) || panels.length;
    var all = wrap.querySelector("[data-switch-all]");
    var readyHint = wrap.getAttribute("data-hint-ready") || "";
    var doneHint = wrap.getAttribute("data-hint-done") || "";

    each(tabs, function (tab) {
      tab.addEventListener("click", function () {
        var id = tab.getAttribute("data-part");
        each(tabs, function (b) {
          b.setAttribute("aria-pressed",
            b.getAttribute("data-part") === id ? "true" : "false");
        });
        each(panels, function (p) {
          setHidden(p, p.getAttribute("data-part") !== id);
        });
      });
    });

    function opened() {
      var n = 0;
      each(panels, function (p) {
        if (p.getAttribute("data-open") === "1") { n += 1; }
      });
      return n;
    }

    each(panels, function (panel) {
      var opts = toArray(panel.querySelectorAll(".ks3-option"));
      var btn = panel.querySelector("[data-switch]");
      var hint = panel.querySelector("[data-switch-hint]");
      var chain = panel.querySelector("[data-switch-chain]");

      each(opts, function (o) {
        o.addEventListener("click", function () {
          // A prediction made before the switch is thrown stays visible
          // and stops being changeable once it has been tested — the
          // student's own guess is the evidence the chain is read
          // against.
          if (panel.getAttribute("data-open") === "1") { return; }
          each(opts, function (b) { b.setAttribute("aria-pressed", "false"); });
          o.setAttribute("aria-pressed", "true");
          if (btn) { btn.removeAttribute("disabled"); }
          if (hint) { hint.textContent = readyHint; }
        });
      });

      if (!btn) { return; }
      btn.addEventListener("click", function () {
        if (panel.getAttribute("data-open") === "1") { return; }
        if (!panel.querySelector('.ks3-option[aria-pressed="true"]')) { return; }
        panel.setAttribute("data-open", "1");
        each(opts, function (b) { b.setAttribute("disabled", ""); });
        setHidden(chain, false);
        btn.textContent = btn.getAttribute("data-done-label") || "";
        btn.setAttribute("disabled", "");
        if (hint) { hint.textContent = doneHint; }
        var n = opened();
        setCount(sec, n);
        if (n >= total) {
          if (all) { setHidden(all, false); }
          markStage(sec, true);
        }
      });
    });
    setCount(sec, 0);
  }

  /* ── joint-bench (b2-02) ──
     A two-bone linkage drawn from the payload. The allowed sweep, the
     glyph radius, the hinge groove, the fixed joint's seam and the twist
     verdict are all functions of `bend[]` and `twist`, which is why a
     fifth joint needs data and no drawing code.

     ⚖️ THE REFUSAL IS DRAWN. A pivot and a fixed joint get a disabled
     slider, the literal readout `locked` and a label saying the joint
     does not bend — three coordinated readouts a generic range control
     cannot give, and the reason this is an instrument, not a `sim`. */
  function wireJointBench(sec) {
    var wrap = sec.querySelector("[data-jointbench]");
    if (!wrap) { return; }
    var joints;
    try { joints = JSON.parse(wrap.getAttribute("data-joints") || "[]"); }
    catch (err) { joints = []; }
    if (!joints.length) { return; }

    var canvas = wrap.querySelector("[data-joint-canvas]");
    var slider = wrap.querySelector("[data-angle]");
    var angleLabel = wrap.querySelector("[data-angle-label]");
    var angleValue = wrap.querySelector("[data-angle-value]");
    var twistBtn = wrap.querySelector("[data-twist]");
    var twistNote = wrap.querySelector("[data-twist-note]");
    var tabs = toArray(wrap.querySelectorAll(".ks3-joint-tab"));
    var total = parseInt(wrap.getAttribute("data-total"), 10) || joints.length;

    var LOCKED = wrap.getAttribute("data-locked") || "locked";
    var TW_OFF = wrap.getAttribute("data-twist-off") || "";
    var TW_ON = wrap.getAttribute("data-twist-on") || "";
    var TW_IDLE = wrap.getAttribute("data-twist-idle") || "";
    var ALT = wrap.getAttribute("data-alt") || "";
    var ALT_CAN = wrap.getAttribute("data-alt-can") || "";
    var ALT_CANNOT = wrap.getAttribute("data-alt-cannot") || "";

    var current = joints[0].id;
    var angles = {};
    var twists = {};
    var tried = {};
    var spin = 0;
    var last = 0;
    each(joints, function (j) { angles[j.id] = j.start; });

    function joint() {
      for (var i = 0; i < joints.length; i++) {
        if (joints[i].id === current) { return joints[i]; }
      }
      return joints[0];
    }

    function tile(key, value) {
      var el = wrap.querySelector('[data-tile="' + key + '"]');
      if (el) { el.textContent = value; }
    }

    function draw() {
      if (!canvas || !canvas.getContext) { return; }
      var ctx = canvas.getContext("2d");
      var W = 900, H = 370;
      ctx.setTransform(1, 0, 0, 1, 0, 0);
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      ctx.setTransform(2, 0, 0, 2, 0, 0);
      ctx.fillStyle = "#100D0A";
      ctx.fillRect(0, 0, W, H);

      var j = joint();
      var px = 470, py = 250;
      var upperLen = 250, lowerLen = 235;
      var ang = (angles[j.id] || 0) * Math.PI / 180;
      var twisting = !!(j.twist && twists[j.id]);
      // Frozen at one representative phase under reduced motion: the ring
      // still draws solid and the orbiting dot is still there, it simply
      // does not move. R6 — a complete experience, not a lesser one.
      var phase = motionReduced() ? 1.2 : spin;

      if (j.bend[1] > 0) {
        ctx.beginPath();
        ctx.moveTo(px, py);
        ctx.arc(px, py, lowerLen * 0.86, 0, -j.bend[1] * Math.PI / 180, true);
        ctx.closePath();
        ctx.fillStyle = "rgba(143,183,255,0.13)";
        ctx.fill();
        ctx.strokeStyle = "rgba(143,183,255,0.5)";
        ctx.setLineDash([6, 6]);
        ctx.lineWidth = 2;
        ctx.stroke();
        ctx.setLineDash([]);
        ctx.fillStyle = "#8FB7FF";
        ctx.font = '500 15px "DM Mono", ui-monospace, monospace';
        ctx.textAlign = "left";
        ctx.fillText("range of movement: 0 to " + j.bend[1] + " degrees",
                     px - 250, py + 92);
      } else {
        ctx.fillStyle = "#8FB7FF";
        ctx.font = '500 15px "DM Mono", ui-monospace, monospace';
        ctx.textAlign = "left";
        ctx.fillText("range of bending: none", px - 250, py + 92);
      }

      function bone(x1, y1, x2, y2) {
        ctx.lineCap = "round";
        ctx.strokeStyle = "#F4E9D8";
        ctx.lineWidth = 26;
        ctx.beginPath(); ctx.moveTo(x1, y1); ctx.lineTo(x2, y2); ctx.stroke();
        ctx.strokeStyle = "#100D0A";
        ctx.lineWidth = 3;
        ctx.beginPath(); ctx.moveTo(x1, y1); ctx.lineTo(x2, y2); ctx.stroke();
        ctx.strokeStyle = "#F4E9D8";
        ctx.lineWidth = 20;
        ctx.beginPath(); ctx.moveTo(x1, y1); ctx.lineTo(x2, y2); ctx.stroke();
      }

      bone(px - upperLen, py, px, py);
      var lx = px + Math.cos(-ang) * lowerLen;
      var ly = py + Math.sin(-ang) * lowerLen;
      bone(px, py, lx, ly);

      ctx.beginPath();
      ctx.arc(px, py, j.id === "ball" ? 27 : 20, 0, Math.PI * 2);
      ctx.fillStyle = j.id === "fixed" ? "#5C5249" : "#FFC53D";
      ctx.fill();
      ctx.strokeStyle = "#100D0A";
      ctx.lineWidth = 3;
      ctx.stroke();
      if (j.id === "hinge") {
        ctx.beginPath();
        ctx.moveTo(px - 20, py - 26); ctx.lineTo(px - 20, py + 26);
        ctx.moveTo(px + 20, py - 26); ctx.lineTo(px + 20, py + 26);
        ctx.strokeStyle = "#8FB7FF";
        ctx.lineWidth = 4;
        ctx.stroke();
      }
      if (j.id === "fixed") {
        ctx.strokeStyle = "#C6B9A7";
        ctx.lineWidth = 3;
        ctx.beginPath();
        for (var i = -30; i <= 30; i += 10) {
          ctx.moveTo(px + i, py - 22);
          ctx.lineTo(px + i + 5, py + 22);
        }
        ctx.stroke();
      }

      var mx = px + Math.cos(-ang) * lowerLen * 0.62;
      var my = py + Math.sin(-ang) * lowerLen * 0.62;
      ctx.save();
      ctx.translate(mx, my);
      ctx.rotate(-ang);
      ctx.beginPath();
      ctx.ellipse(0, 0, 20, 42, 0, 0, Math.PI * 2);
      if (j.twist) {
        ctx.strokeStyle = twisting ? "#FFC53D" : "#6E655D";
        ctx.setLineDash(twisting ? [] : [5, 5]);
        ctx.lineWidth = 3;
        ctx.stroke();
        ctx.setLineDash([]);
        if (twisting) {
          ctx.beginPath();
          ctx.arc(Math.sin(phase) * 20, Math.cos(phase) * 42, 8, 0, Math.PI * 2);
          ctx.fillStyle = "#FFC53D";
          ctx.fill();
        }
      } else {
        // The refusal, drawn: a dashed ring AND a struck-through cross.
        ctx.strokeStyle = "#6E655D";
        ctx.setLineDash([5, 5]);
        ctx.lineWidth = 3;
        ctx.stroke();
        ctx.setLineDash([]);
        ctx.strokeStyle = "#C6B9A7";
        ctx.lineWidth = 5;
        ctx.beginPath();
        ctx.moveTo(-14, -14); ctx.lineTo(14, 14);
        ctx.moveTo(14, -14); ctx.lineTo(-14, 14);
        ctx.stroke();
      }
      ctx.restore();

      ctx.font = '500 14px "DM Mono", ui-monospace, monospace';
      var label = (j.name || "").toUpperCase();
      var w = ctx.measureText(label).width + 30;
      ctx.fillStyle = "#221E1B";
      var rx = 24, ry = 24;
      ctx.beginPath();
      ctx.moveTo(rx + 12, ry);
      ctx.lineTo(rx + w - 12, ry);
      ctx.quadraticCurveTo(rx + w, ry, rx + w, ry + 12);
      ctx.lineTo(rx + w, ry + 26);
      ctx.quadraticCurveTo(rx + w, ry + 38, rx + w - 12, ry + 38);
      ctx.lineTo(rx + 12, ry + 38);
      ctx.quadraticCurveTo(rx, ry + 38, rx, ry + 26);
      ctx.lineTo(rx, ry + 12);
      ctx.quadraticCurveTo(rx, ry, rx + 12, ry);
      ctx.closePath();
      ctx.fill();
      ctx.strokeStyle = "#FFC53D";
      ctx.lineWidth = 2;
      ctx.stroke();
      ctx.fillStyle = "#FFC53D";
      ctx.textAlign = "left";
      ctx.fillText(label, rx + 15, ry + 25);
      ctx.textAlign = "center";
    }

    function alt(j) {
      return ALT.replace("{name}", (j.name || "").toLowerCase())
        .replace("{angle}", String(angles[j.id] || 0))
        .replace("{max}", String(j.bend[1]))
        .replace("{twist}", j.twist ? ALT_CAN : ALT_CANNOT);
    }

    function repaint() {
      var j = joint();
      var twisting = !!twists[j.id];
      var locked = j.bend[1] === 0;
      if (slider) {
        slider.min = String(j.bend[0]);
        slider.max = String(j.bend[1] || 1);
        slider.value = String(angles[j.id] || 0);
        if (locked) { slider.setAttribute("disabled", ""); }
        else { slider.removeAttribute("disabled"); }
      }
      if (angleLabel) { angleLabel.textContent = j.angle_label || ""; }
      if (angleValue) {
        angleValue.textContent = locked ? LOCKED
                                        : (angles[j.id] || 0) + "°";
      }
      if (twistBtn) {
        twistBtn.setAttribute("aria-pressed", twisting ? "true" : "false");
        twistBtn.textContent = twisting ? TW_ON : TW_OFF;
      }
      if (twistNote) {
        twistNote.textContent = twisting ? j.twist_yes
          : (j.twist ? TW_IDLE : j.twist_no);
      }
      tile("axes", j.axes || "");
      tile("where", j.where || "");
      tile("hold", j.hold || "");
      tile("trade", j.trade || "");
      if (canvas) { canvas.setAttribute("aria-label", alt(j)); }
      draw();
    }

    function touch(id) {
      tried[id] = true;
      var n = 0;
      for (var k in tried) { if (tried[k]) { n += 1; } }
      setCount(sec, n);
      if (n >= total) { markStage(sec, true); }
    }

    each(tabs, function (tab) {
      tab.addEventListener("click", function () {
        current = tab.getAttribute("data-joint");
        each(tabs, function (b) {
          b.setAttribute("aria-pressed",
            b.getAttribute("data-joint") === current ? "true" : "false");
        });
        touch(current);
        repaint();
      });
    });

    if (slider) {
      // BOTH events, deliberately: `input` is what a drag fires and
      // `change` is what a keyboard arrow lands on in older engines.
      each(["input", "change"], function (evt) {
        slider.addEventListener(evt, function () {
          var j = joint();
          angles[j.id] = Number(slider.value) || 0;
          touch(j.id);
          repaint();
        });
      });
    }
    if (twistBtn) {
      twistBtn.addEventListener("click", function () {
        var j = joint();
        twists[j.id] = !twists[j.id];
        touch(j.id);
        repaint();
      });
    }

    function tick(now) {
      var dt = Math.min(0.05, (now - (last || now)) / 1000);
      last = now;
      var j = joint();
      // Asked EVERY FRAME, not once at construction.
      if (j.twist && twists[j.id] && !motionReduced()) {
        spin += dt * 1.1;
        draw();
      }
      window.requestAnimationFrame(tick);
    }

    repaint();
    setCount(sec, 0);
    if (window.requestAnimationFrame) { window.requestAnimationFrame(tick); }
    wireBenchGate(sec);
  }

  /* ── muscle-pair (b2-03) ──
     The only B2 instrument with a continuous physical state, and the
     mechanism IS the teaching:

        both pulling → the joint LOCKS wherever it is
        biceps only  → 135°     triceps only → 6°     neither → 6°

     and falling (55 °/s) is SLOWER than pulling (90 °/s). "Gravity
     straightens a hanging arm for free" is taught by pressing Neither
     and watching it come down more slowly than it went up; equalise the
     two rates and the lesson is gone, leaving the animation.

     ⚠️ The settings counter is over a MIXED KEY SPACE — four mode ids
     and two kill ids — so "4 of 4 settings tried" is reachable as two
     modes plus two kills. That is Design's own behaviour and its own
     label; it is honest about "settings touched" and loose about "all
     four contraction modes tried". Reproduced as drawn and reported,
     because tightening it would contradict the label on the page. */
  function wireMusclePair(sec) {
    var wrap = sec.querySelector("[data-musclepair]");
    if (!wrap) { return; }
    var cfg;
    try { cfg = JSON.parse(wrap.getAttribute("data-cfg") || "{}"); }
    catch (err) { cfg = {}; }

    var canvas = wrap.querySelector("[data-muscle-canvas]");
    var statusEl = wrap.querySelector("[data-muscle-status]");
    var modeBtns = toArray(wrap.querySelectorAll(".ks3-muscle-mode"));
    var killBtns = toArray(wrap.querySelectorAll(".ks3-muscle-kill"));
    var total = parseInt(wrap.getAttribute("data-total"), 10) || 4;

    var targets = cfg.targets || {};
    var rates = cfg.rates || {};
    var notes = cfg.notes || {};
    var status = cfg.status || {};
    var states = cfg.states || {};
    var CL = cfg.canvas_labels || {};
    var ALT = cfg.alt || {};

    var mode = "none";
    each(modeBtns, function (b) {
      if (b.getAttribute("aria-pressed") === "true") {
        mode = b.getAttribute("data-mode");
      }
    });
    var dead = { biceps: false, triceps: false };
    var tried = {};
    var angle = Number(cfg.start_angle) || 0;
    var last = 0;

    function acting() {
      return {
        bi: (mode === "biceps" || mode === "both") && !dead.biceps,
        tri: (mode === "triceps" || mode === "both") && !dead.triceps
      };
    }
    function target() {
      var a = acting();
      if (a.bi && a.tri) { return angle; }   // both pulling: the joint locks
      if (a.bi) { return Number(targets.biceps); }
      if (a.tri) { return Number(targets.triceps); }
      return Number(targets.none);           // nothing pulling: it falls
    }

    function band(ctx, x1, y1, x2, y2, thick, colour) {
      var mx = (x1 + x2) / 2, my = (y1 + y2) / 2;
      var dx = x2 - x1, dy = y2 - y1;
      var len = Math.sqrt(dx * dx + dy * dy) || 1;
      var nx = -dy / len, ny = dx / len;
      ctx.beginPath();
      ctx.moveTo(x1, y1);
      ctx.quadraticCurveTo(mx + nx * thick, my + ny * thick, x2, y2);
      ctx.quadraticCurveTo(mx - nx * thick, my - ny * thick, x1, y1);
      ctx.closePath();
      ctx.fillStyle = colour;
      ctx.fill();
      ctx.strokeStyle = "#100D0A";
      ctx.lineWidth = 2.5;
      ctx.stroke();
    }

    function draw() {
      if (!canvas || !canvas.getContext) { return; }
      var ctx = canvas.getContext("2d");
      var W = 900, H = 370;
      ctx.setTransform(1, 0, 0, 1, 0, 0);
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      ctx.setTransform(2, 0, 0, 2, 0, 0);
      ctx.fillStyle = "#100D0A";
      ctx.fillRect(0, 0, W, H);

      var a = acting();
      var sh = { x: 380, y: 70 }, el = { x: 380, y: 232 };
      var ang = angle * Math.PI / 180;
      // 0° is the forearm hanging straight down; the angle opens to +x.
      var dirx = Math.sin(ang), diry = Math.cos(ang);
      var hand = { x: el.x + dirx * 168, y: el.y + diry * 168 };

      function bone(p, q, w) {
        ctx.lineCap = "round";
        ctx.strokeStyle = "#100D0A";
        ctx.lineWidth = w + 6;
        ctx.beginPath(); ctx.moveTo(p.x, p.y); ctx.lineTo(q.x, q.y); ctx.stroke();
        ctx.strokeStyle = "#F4E9D8";
        ctx.lineWidth = w;
        ctx.beginPath(); ctx.moveTo(p.x, p.y); ctx.lineTo(q.x, q.y); ctx.stroke();
      }

      // Muscles are drawn BEHIND the bones, and thickness encodes
      // contraction: a pulling belly is fatter as well as brighter, so
      // the state is legible without colour alone (R2).
      var bIns = { x: el.x + dirx * 46, y: el.y + diry * 46 };
      var tIns = { x: el.x - dirx * 30, y: el.y - diry * 30 };
      var bOrigin = { x: sh.x + 16, y: sh.y + 18 };
      var tOrigin = { x: sh.x - 16, y: sh.y + 18 };
      var bColour = dead.biceps ? "#4A4038" : (a.bi ? "#FFC53D" : "#8A7A62");
      var tColour = dead.triceps ? "#4A4038" : (a.tri ? "#FFC53D" : "#8A7A62");
      band(ctx, bOrigin.x, bOrigin.y, bIns.x, bIns.y, a.bi ? 34 : 20, bColour);
      band(ctx, tOrigin.x, tOrigin.y, tIns.x, tIns.y, a.tri ? 30 : 18, tColour);

      bone(sh, el, 22);
      bone(el, hand, 20);

      ctx.beginPath();
      ctx.arc(el.x, el.y, 15, 0, Math.PI * 2);
      ctx.fillStyle = "#C6B9A7";
      ctx.fill();
      ctx.strokeStyle = "#100D0A";
      ctx.lineWidth = 3;
      ctx.stroke();
      ctx.beginPath();
      ctx.arc(hand.x, hand.y, 16, 0, Math.PI * 2);
      ctx.fillStyle = "#F4E9D8";
      ctx.fill();
      ctx.strokeStyle = "#100D0A";
      ctx.lineWidth = 3;
      ctx.stroke();

      ctx.font = '500 15px "DM Mono", ui-monospace, monospace';
      ctx.textAlign = "left";
      ctx.fillStyle = dead.biceps ? "#6E655D" : "#FFC53D";
      ctx.fillText((CL.biceps || "")
        + (dead.biceps ? (CL.off || "") : (a.bi ? (CL.pulling || "")
                                               : (CL.relaxed || ""))),
        600, 44);
      ctx.fillStyle = dead.triceps ? "#6E655D" : "#FFC53D";
      ctx.fillText((CL.triceps || "")
        + (dead.triceps ? (CL.off || "") : (a.tri ? (CL.pulling || "")
                                                  : (CL.relaxed || ""))),
        40, 44);

      ctx.beginPath();
      ctx.arc(el.x, el.y, 58, Math.PI / 2, Math.PI / 2 - ang, true);
      ctx.strokeStyle = "#8FB7FF";
      ctx.lineWidth = 3;
      ctx.stroke();
      ctx.fillStyle = "#8FB7FF";
      ctx.textAlign = "left";
      ctx.font = '500 16px "DM Mono", ui-monospace, monospace';
      ctx.fillText(Math.round(angle) + "°", el.x + 34, el.y + 84);
      ctx.textAlign = "center";
    }

    function stateWord(muscle, pulling) {
      if (dead[muscle]) { return states.dead || ""; }
      return pulling ? (states.contracted || "") : (states.relaxed || "");
    }

    function noteKey() {
      var a = acting();
      if (dead.biceps && !dead.triceps) { return "biceps_dead"; }
      if (dead.triceps && !dead.biceps) { return "triceps_dead"; }
      if (dead.biceps && dead.triceps) { return "both_dead"; }
      if (a.bi && a.tri) { return "both"; }
      if (a.bi) { return "biceps"; }
      if (a.tri) { return "triceps"; }
      return "none";
    }
    function statusKey() {
      var a = acting();
      if (a.bi && a.tri) { return "both"; }
      if (a.bi) { return "biceps"; }
      if (a.tri) { return "triceps"; }
      return "none";
    }
    function altWordKey(muscle, pulling) {
      if (dead[muscle]) { return "dead"; }
      return pulling ? (muscle === "biceps" ? "biceps_pulling"
                                            : "triceps_pulling")
                     : "relaxed";
    }

    function tile(key, value) {
      var el = wrap.querySelector('[data-tile="' + key + '"]');
      if (el) { el.textContent = value; }
    }

    /* ⚠️ THE DEGREE TILE AND THE CANVAS UPDATE ON DIFFERENT CLOCKS, and
       that split is deliberate. The canvas repaints every frame while the
       arm travels; the readouts repaint only when a control changes,
       which is what Design's own render does. Driving the tiles at 60 Hz
       would repaint a third of the block sixty times a second for a
       number nobody can read while it moves. `settle()` writes the final
       angle once the arm has arrived. */
    function repaintReadouts() {
      var a = acting();
      var words = ALT.words || {};
      if (statusEl) { statusEl.textContent = status[statusKey()] || ""; }
      tile("angle", Math.round(angle) + "°");
      tile("biceps", stateWord("biceps", a.bi));
      tile("triceps", stateWord("triceps", a.tri));
      tile("note", notes[noteKey()] || "");
      if (canvas) {
        canvas.setAttribute("aria-label", (ALT.template || "")
          .replace("{biceps}", words[altWordKey("biceps", a.bi)] || "")
          .replace("{triceps}", words[altWordKey("triceps", a.tri)] || ""));
      }
      draw();
    }

    function touch(key) {
      tried[key] = true;
      var n = 0;
      for (var k in tried) { if (tried[k]) { n += 1; } }
      setCount(sec, n);
      if (n >= total) { markStage(sec, true); }
    }

    each(modeBtns, function (b) {
      b.addEventListener("click", function () {
        mode = b.getAttribute("data-mode");
        each(modeBtns, function (x) {
          x.setAttribute("aria-pressed",
            x.getAttribute("data-mode") === mode ? "true" : "false");
        });
        touch(mode);
        repaintReadouts();
      });
    });
    each(killBtns, function (b) {
      b.addEventListener("click", function () {
        var id = b.getAttribute("data-kill");
        dead[id] = !dead[id];
        b.setAttribute("aria-pressed", dead[id] ? "true" : "false");
        touch("off-" + id);
        repaintReadouts();
      });
    });

    function tick(now) {
      var dt = Math.min(0.05, (now - (last || now)) / 1000);
      last = now;
      var t = target();
      if (Math.abs(t - angle) > 0.3) {
        if (motionReduced()) {
          // R6 / contract R4 — reduced motion SNAPS to the mechanism's
          // answer. The arm still ends up where the physics says; it
          // just does not travel there. Asked every frame, so an OS
          // setting changed mid-lesson takes effect without a reload.
          angle = t;
          repaintReadouts();
        } else {
          var a = acting();
          var rate = (!a.bi && !a.tri) ? Number(rates.fall)
                                       : Number(rates.pull);
          var step = (t > angle ? 1 : -1) * rate * dt;
          angle = Math.abs(step) > Math.abs(t - angle) ? t : angle + step;
          draw();
          // The tile catches up the moment the arm arrives, so the
          // number a student reads is the number the arm is at.
          if (Math.abs(t - angle) <= 0.3) { tile("angle", Math.round(angle) + "°"); }
        }
      }
      window.requestAnimationFrame(tick);
    }

    repaintReadouts();
    setCount(sec, 0);
    if (window.requestAnimationFrame) { window.requestAnimationFrame(tick); }
    wireBenchGate(sec);
  }

  /* ═══ C2 · Atoms, elements and compounds (⊕ MRB-220) ═══════════════
     Nine instruments. NOTHING IN THIS UNIT ANIMATES — no rAF, no tick,
     no loop. Every canvas redraws on a control change and on nothing
     else, so `prefers-reduced-motion` has nothing to degrade here and
     the four canvases cost a browser nothing once they are painted. */

  /* ── claim-switch (c2-01 #s-model) ──
     Three claims as toggles; four observations that lose their text and
     gain a failure sentence when a claim they need goes off.

     ⚖️ THE STAGE TICKS ON TWO PRESSES IN ANY DIRECTION. Design's own
     rule (`touched >= 2`), and it counts switching a claim back ON. A
     component must not quietly tighten that to "two claims off": the
     lesson is that turning one off and back on is itself the
     investigation. */
  function wireClaimSwitch(sec) {
    var wrap = sec.querySelector("[data-claimswitch]");
    if (!wrap) { return; }
    var claims = toArray(wrap.querySelectorAll(".ks3-claim"));
    var rows = toArray(wrap.querySelectorAll(".ks3-obs-row"));
    var note = wrap.querySelector("[data-claimnote]");
    var doneAt = parseInt(wrap.getAttribute("data-done-at"), 10) || 2;
    var ON = wrap.getAttribute("data-on") || "ON";
    var OFF = wrap.getAttribute("data-off") || "OFF";
    var ALIVE = wrap.getAttribute("data-alive") || "";
    var DEAD = wrap.getAttribute("data-dead") || "";
    var ALL_ON = wrap.getAttribute("data-all-on") || "";
    var NONE = wrap.getAttribute("data-none-broken") || "";
    var SOME = wrap.getAttribute("data-some-broken") || "";
    var W1 = wrap.getAttribute("data-word-one") || "";
    var WN = wrap.getAttribute("data-word-many") || "";
    var off = {};
    var touched = 0;

    function repaint() {
      var offCount = 0, key;
      for (key in off) { if (off[key]) { offCount += 1; } }

      var broken = 0;
      each(rows, function (row) {
        var needs = (row.getAttribute("data-needs") || "").split(" ");
        var dead = false;
        for (var i = 0; i < needs.length; i++) {
          if (needs[i] && off[needs[i]]) { dead = true; }
        }
        if (dead) { broken += 1; }
        // Emit-both-show-one: both sentences are in the document, so no
        // text is ever assembled from an attribute and the author's
        // <em> survives in either state.
        row.setAttribute("data-dead", dead ? "1" : "0");
        setHidden(row.querySelector("[data-obs-alive]"), dead);
        setHidden(row.querySelector("[data-obs-dead]"), !dead);
        var v = row.querySelector("[data-obs-verdict]");
        if (v) { v.textContent = dead ? DEAD : ALIVE; }
      });

      if (note) {
        if (!offCount) {
          note.textContent = ALL_ON;
        } else if (!broken) {
          note.textContent = NONE;
        } else {
          note.textContent = SOME.replace("{n}", String(offCount))
            .replace("{claim}", offCount === 1 ? W1 : WN)
            .replace("{broken}", String(broken));
        }
      }
      setCount(sec, offCount);
    }

    each(claims, function (btn) {
      btn.addEventListener("click", function () {
        var id = btn.getAttribute("data-claim");
        off[id] = !off[id];
        btn.setAttribute("aria-pressed", off[id] ? "false" : "true");
        var chip = btn.querySelector("[data-claim-chip]");
        if (chip) { chip.textContent = off[id] ? OFF : ON; }
        touched += 1;
        repaint();
        if (touched >= doneAt) { markStage(sec, true); }
      });
    });

    repaint();
    wireBenchGate(sec);
  }

  /* ── mixture-compound-dish (c2-03 #s-bench) ──
     Iron and sulfur, stirred and then heated.

     ⚖️ THE PROPORTION CONTROL IS DISABLED ONCE HEATED, AND THAT IS THE
     LESSON — a compound's proportion is not adjustable. Enforced three
     ways: `disabled` on the button, a re-check inside the handler (as
     Design's own click guard does), and a heated drawing that has no
     ratio to draw. A generic tab group that stayed live would delete the
     whole argument and leave a picture. */
  function wireDish(sec) {
    var wrap = sec.querySelector("[data-dish]");
    if (!wrap) { return; }
    var cfg;
    try { cfg = JSON.parse(wrap.getAttribute("data-cfg") || "{}"); }
    catch (err) { cfg = {}; }
    var fracs = cfg.fracs || [];
    var caps = cfg.captions || {};
    var canvas = wrap.querySelector("[data-dish-canvas]");
    var noteEl = wrap.querySelector("[data-dish-note]");
    var stateBtns = toArray(wrap.querySelectorAll(".ks3-dish-state"));
    var ratioBtns = toArray(wrap.querySelectorAll(".ks3-dish-ratio"));
    var testBtns = toArray(wrap.querySelectorAll(".ks3-dish-test"));
    var cards = toArray(wrap.querySelectorAll("[data-testcard]"));
    var total = parseInt(wrap.getAttribute("data-total"), 10) || testBtns.length;
    var heated = false;
    var ratio = 0;
    var seen = {};

    var IRON = "#9AA0A6", SULFUR = "#E9C445";

    function draw() {
      if (!canvas || !canvas.getContext) { return; }
      var ctx = canvas.getContext("2d");
      var W = 850, H = 280;
      ctx.setTransform(1, 0, 0, 1, 0, 0);
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      ctx.setTransform(2, 0, 0, 2, 0, 0);
      ctx.fillStyle = "#100D0A";
      ctx.fillRect(0, 0, W, H);

      // Everything is clipped to the dish, then the dish is re-stroked —
      // so nothing can spill onto the bench and the outline stays crisp.
      ctx.save();
      ctx.beginPath();
      ctx.ellipse(W / 2, H / 2 + 10, 330, 96, 0, 0, Math.PI * 2);
      ctx.clip();
      ctx.fillStyle = heated ? "#2A2622" : "#1A1713";
      ctx.fillRect(0, 0, W, H);

      if (!heated) {
        // A hand-rolled LCG rather than Math.random: the mixture must be
        // the SAME scatter every repaint, or changing the proportion
        // would look like stirring rather than like a different mix.
        var frac = fracs[ratio];
        var n = 0;
        for (var i = 0; i < 120; i++) {
          n = (n * 1103515245 + 12345) % 2147483648;
          var a = n / 2147483648;
          n = (n * 1103515245 + 12345) % 2147483648;
          var b = n / 2147483648;
          n = (n * 1103515245 + 12345) % 2147483648;
          var k = n / 2147483648;
          var x = W / 2 + (a - 0.5) * 600, y = H / 2 + 10 + (b - 0.5) * 170;
          ctx.beginPath();
          ctx.arc(x, y, k < frac ? 9 : 7, 0, Math.PI * 2);
          ctx.fillStyle = k < frac ? IRON : SULFUR;
          ctx.fill();
          ctx.strokeStyle = "rgba(0,0,0,0.45)";
          ctx.lineWidth = 1.5;
          ctx.stroke();
        }
      } else {
        // ⚖️ One iron to one sulfur, joined, regular, repeating. It is a
        // giant structure and NOT molecules — the stub joins each pair to
        // its own partner and the grid goes on past the dish's edge,
        // which is what "repeating" has to look like.
        for (var row = 0; row < 5; row++) {
          for (var col = 0; col < 17; col++) {
            var px = W / 2 - 290 + col * 36, py = H / 2 - 58 + row * 34;
            ctx.beginPath();
            ctx.arc(px, py, 9, 0, Math.PI * 2);
            ctx.fillStyle = IRON;
            ctx.fill();
            ctx.beginPath();
            ctx.arc(px + 17, py, 7, 0, Math.PI * 2);
            ctx.fillStyle = SULFUR;
            ctx.fill();
            ctx.strokeStyle = "#6E655D";
            ctx.lineWidth = 3;
            ctx.beginPath();
            ctx.moveTo(px + 8, py);
            ctx.lineTo(px + 11, py);
            ctx.stroke();
          }
        }
      }
      ctx.restore();

      ctx.strokeStyle = "#5C5249";
      ctx.lineWidth = 4;
      ctx.beginPath();
      ctx.ellipse(W / 2, H / 2 + 10, 330, 96, 0, 0, Math.PI * 2);
      ctx.stroke();

      ctx.font = '500 15px "DM Mono", ui-monospace, monospace';
      ctx.textAlign = "left";
      ctx.fillStyle = "#FFC53D";
      ctx.fillText((heated ? caps.left_heated : caps.left_mixed) || "", 24, 28);
      ctx.textAlign = "right";
      ctx.fillStyle = "#C6B9A7";
      ctx.fillText((heated ? caps.right_heated : caps.right_mixed) || "",
                   W - 24, 28);
      // The legend is drawn as two coloured words rather than swatches:
      // the colour IS the label, so naming it in its own colour is the
      // shortest honest key.
      ctx.textAlign = "left";
      ctx.fillStyle = IRON;
      ctx.fillText(caps.iron || "", 24, H - 18);
      ctx.fillStyle = SULFUR;
      ctx.fillText(caps.sulfur || "", 80, H - 18);
      ctx.textAlign = "center";
      if (canvas.setAttribute) {
        canvas.setAttribute("aria-label",
          wrap.getAttribute(heated ? "data-alt-heated" : "data-alt-mixed") || "");
      }
    }

    function repaint() {
      each(ratioBtns, function (b) {
        // The refusal, enforced on the button as well as in the handler.
        if (heated) { b.setAttribute("disabled", ""); }
        else { b.removeAttribute("disabled"); }
      });
      if (noteEl) {
        noteEl.textContent =
          wrap.getAttribute(heated ? "data-note-heated" : "data-note-mixed") || "";
      }
      draw();
      var n = 0, k;
      for (k in seen) { if (seen[k]) { n += 1; } }
      setCount(sec, n);
      if (n >= total) { markStage(sec, true); }
    }

    each(stateBtns, function (b) {
      b.addEventListener("click", function () {
        heated = b.getAttribute("data-heated") === "1";
        each(stateBtns, function (x) {
          x.setAttribute("aria-pressed", x === b ? "true" : "false");
        });
        repaint();
      });
    });

    each(ratioBtns, function (b) {
      b.addEventListener("click", function () {
        // ⚖️ Re-checked here, not only on the attribute. Design's own
        // handler does the same, and it is the difference between a
        // control that is styled as refused and one that refuses.
        if (heated) { return; }
        ratio = parseInt(b.getAttribute("data-ratio"), 10) || 0;
        each(ratioBtns, function (x) {
          x.setAttribute("aria-pressed", x === b ? "true" : "false");
        });
        repaint();
      });
    });

    each(testBtns, function (b) {
      b.addEventListener("click", function () {
        var id = b.getAttribute("data-test");
        seen[id] = true;
        each(testBtns, function (x) {
          x.setAttribute("aria-pressed", x === b ? "true" : "false");
        });
        each(cards, function (c) {
          setHidden(c, c.getAttribute("data-testcard") !== id);
        });
        repaint();
      });
    });

    // The opening test is on screen, so it counts as seen — the same rule
    // Design's own `seenTests: {look: true}` seed sets, which is why three
    // taps finish the stage rather than four.
    if (testBtns.length) {
      seen[testBtns[0].getAttribute("data-test")] = true;
    }
    repaint();
    wireBenchGate(sec);
  }

  /* ── formula-builder (c2-05 #s-builder) ──
     Three pairs × three × three = 27 combinations, of which FIVE are
     substances.

     ⚖️ "NOT A SUBSTANCE" IS THE TEACHING, and it is the answer 22 times
     out of 27. A builder that only offered the real ones would teach
     that any formula you can write exists, which is exactly the idea
     this block is aimed at.

     ⊕ The opening substance is banked AT MOUNT, which Design's page does
     not do: `mark()` is wired to the three control groups only, so the
     H₂O the instrument opens on is displayed, named, drawn — and could
     never be counted. Addition inside a drawn component; contradicts
     nothing on the page. */
  function wireFormulaBuilder(sec) {
    var wrap = sec.querySelector("[data-fb]");
    if (!wrap) { return; }
    var cfg;
    try { cfg = JSON.parse(wrap.getAttribute("data-cfg") || "{}"); }
    catch (err) { cfg = {}; }
    var pairs = cfg.pairs || [];
    var known = cfg.known || {};
    var colours = cfg.colours || {};
    var nf = cfg.not_found || {};
    var caps = cfg.captions || {};
    if (!pairs.length) { return; }

    var canvas = wrap.querySelector("[data-fb-canvas]");
    var nameEl = wrap.querySelector("[data-fb-name]");
    var noteEl = wrap.querySelector("[data-fb-note]");
    var labelA = wrap.querySelector('[data-fb-label="a"]');
    var labelB = wrap.querySelector('[data-fb-label="b"]');
    var pairBtns = toArray(wrap.querySelectorAll(".ks3-fb-pair"));
    var countBtns = toArray(wrap.querySelectorAll(".ks3-fb-count"));
    var doneAt = parseInt(wrap.getAttribute("data-done-at"), 10) || 3;

    var pid = (cfg.start || {}).pair || pairs[0].id;
    var na = (cfg.start || {}).a || 1;
    var nb = (cfg.start || {}).b || 1;
    var seen = {};

    function pairOf(id) {
      for (var i = 0; i < pairs.length; i++) {
        if (pairs[i].id === id) { return pairs[i]; }
      }
      return pairs[0];
    }
    function key() { return pid + ":" + na + ":" + nb; }

    function name(p, found) {
      if (found) { return found.name || ""; }
      // ⚠️ ASCII digits here and subscripts in the authored names. Design's
      // own asymmetry (page line 641), reproduced rather than tidied.
      return (p.a || "") + (na > 1 ? na : "") + (p.b || "")
        + (nb > 1 ? nb : "") + (nf.name_suffix || "");
    }

    function draw(found) {
      if (!canvas || !canvas.getContext) { return; }
      var ctx = canvas.getContext("2d");
      var W = 850, H = 260;
      ctx.setTransform(1, 0, 0, 1, 0, 0);
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      ctx.setTransform(2, 0, 0, 2, 0, 0);
      ctx.fillStyle = "#100D0A";
      ctx.fillRect(0, 0, W, H);
      var cx = W / 2, cy = H / 2 + 6;
      ctx.textAlign = "center";

      if (!found) {
        // ⚖️ The refusal is DRAWN, in words, in the frame where a particle
        // would be. An empty frame would read as a bug.
        var lines = nf.canvas_lines || [];
        ctx.fillStyle = "#6E655D";
        ctx.font = '500 17px "DM Mono", ui-monospace, monospace';
        ctx.fillText(lines[0] || "", cx, cy - 6);
        ctx.font = '500 15px "DM Mono", ui-monospace, monospace';
        ctx.fillText(lines[1] || "", cx, cy + 24);
        return;
      }

      if (found.giant) {
        // A repeating stack, not a particle — every atom labelled, and the
        // grid runs off the frame on purpose.
        var step = 58;
        for (var row = 0; row < 4; row++) {
          for (var col = 0; col < 12; col++) {
            var x = cx - 320 + col * step, y = cy - 82 + row * step;
            var isNa = (row + col) % 2 === 0;
            ctx.beginPath();
            ctx.arc(x, y, isNa ? 19 : 23, 0, Math.PI * 2);
            ctx.fillStyle = isNa ? colours.Na : colours.Cl;
            ctx.fill();
            ctx.strokeStyle = "#100D0A";
            ctx.lineWidth = 2;
            ctx.stroke();
            ctx.fillStyle = "#100D0A";
            ctx.font = '800 13px "Bricolage Grotesque", system-ui, sans-serif';
            ctx.fillText(isNa ? "Na" : "Cl", x, y + 5);
          }
        }
        ctx.fillStyle = "#C6B9A7";
        ctx.font = '500 15px "DM Mono", ui-monospace, monospace';
        ctx.fillText(caps.giant || "", cx, H - 18);
        return;
      }

      ctx.strokeStyle = "#5C5249";
      ctx.lineWidth = 7;
      each(found.bonds || [], function (bd) {
        var p = found.atoms[bd[0]], q = found.atoms[bd[1]];
        ctx.beginPath();
        ctx.moveTo(cx + p.x, cy + p.y);
        ctx.lineTo(cx + q.x, cy + q.y);
        ctx.stroke();
      });
      each(found.atoms || [], function (at) {
        ctx.beginPath();
        ctx.arc(cx + at.x, cy + at.y, at.r, 0, Math.PI * 2);
        ctx.fillStyle = colours[at.s] || "#C6B9A7";
        ctx.fill();
        ctx.strokeStyle = "#100D0A";
        ctx.lineWidth = 2.5;
        ctx.stroke();
        ctx.fillStyle = "#100D0A";
        ctx.font = '800 16px "Bricolage Grotesque", system-ui, sans-serif';
        ctx.fillText(at.s, cx + at.x, cy + at.y + 6);
      });
      ctx.fillStyle = "#C6B9A7";
      ctx.font = '500 15px "DM Mono", ui-monospace, monospace';
      ctx.fillText(caps.molecule || "", cx, H - 18);
    }

    function repaint() {
      var p = pairOf(pid);
      var found = known[key()];
      if (found) { seen[key()] = true; }
      if (labelA) { labelA.textContent = p.aName || ""; }
      if (labelB) { labelB.textContent = p.bName || ""; }
      if (nameEl) { nameEl.textContent = name(p, found); }
      if (noteEl) { noteEl.textContent = (found && found.note) || nf.note || ""; }
      if (canvas && canvas.setAttribute) {
        // Three-way, and composed rather than authored because it quotes
        // the live substance name and the live drawing mode.
        var A = cfg.alt || {};
        canvas.setAttribute("aria-label", found
          ? (A.template || "").replace("{name}", found.name || "")
            + (found.giant ? (A.giant || "") : (A.molecule || ""))
          : (A.none || ""));
      }
      draw(found);
      var n = 0, k;
      for (k in seen) { if (seen[k]) { n += 1; } }
      setCount(sec, n);
      if (n >= doneAt) { markStage(sec, true); }
    }

    each(pairBtns, function (b) {
      b.addEventListener("click", function () {
        pid = b.getAttribute("data-pair");
        each(pairBtns, function (x) {
          x.setAttribute("aria-pressed", x === b ? "true" : "false");
        });
        repaint();
      });
    });
    each(countBtns, function (b) {
      b.addEventListener("click", function () {
        var axis = b.getAttribute("data-axis");
        var v = parseInt(b.getAttribute("data-n"), 10) || 1;
        if (axis === "a") { na = v; } else { nb = v; }
        each(countBtns, function (x) {
          if (x.getAttribute("data-axis") !== axis) { return; }
          x.setAttribute("aria-pressed", x === b ? "true" : "false");
        });
        repaint();
      });
    });

    repaint();
    wireBenchGate(sec);
  }

  /* ── balance-bench (c2-06 #s-balance) ──
     Two reactions × two vessels on one top-pan balance.

     ⚖️ THE THIRD TILE NEVER MEASURES. Two tiles report; the third reads
     "not measured — you work it out" for ever and takes no data. It is
     the QUANTITATIVE family's refusal-to-tell, and it is why this is an
     instrument rather than a readout.

     ⚖️ The vessel CHANGES THE PICTURE (a sealed flask gets a bung) and a
     finished run draws the gas leaving or joining. A control that
     changes only a number teaches that the apparatus is incidental.

     ⚠️ Changing either control RESETS the after-reading — Design's own
     rule, and the right one: it is a different run now, and the last
     run's after-mass is not a fact about this one. */
  function wireBalanceBench(sec) {
    var wrap = sec.querySelector("[data-bal]");
    if (!wrap) { return; }
    var cfg;
    try { cfg = JSON.parse(wrap.getAttribute("data-cfg") || "{}"); }
    catch (err) { cfg = {}; }
    var runs = cfg.runs || {};
    var L = cfg.labels || {};
    var DEC = cfg.decimals === undefined ? 2 : cfg.decimals;
    var canvas = wrap.querySelector("[data-bal-canvas]");
    var runBtn = wrap.querySelector("[data-bal-run]");
    var statusEl = wrap.querySelector("[data-bal-status]");
    var noteEl = wrap.querySelector("[data-bal-note]");
    var beforeTile = wrap.querySelector('[data-tile="before"]');
    var afterTile = wrap.querySelector('[data-tile="after"]');
    var rxnBtns = toArray(wrap.querySelectorAll(".ks3-bal-rxn"));
    var vesselBtns = toArray(wrap.querySelectorAll(".ks3-bal-vessel"));
    var doneAt = parseInt(wrap.getAttribute("data-done-at"), 10) || 3;

    var rxn = (cfg.start || {}).reaction;
    var vessel = (cfg.start || {}).vessel;
    var showAfter = false;
    var ran = {};

    function key() { return rxn + ":" + vessel; }
    function run() { return runs[key()] || {}; }
    function mass(v) {
      return v.toFixed(DEC) + " " + (L.unit || "g");
    }

    function draw() {
      if (!canvas || !canvas.getContext) { return; }
      var ctx = canvas.getContext("2d");
      var W = 850, H = 280;
      ctx.setTransform(1, 0, 0, 1, 0, 0);
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      ctx.setTransform(2, 0, 0, 2, 0, 0);
      ctx.fillStyle = "#100D0A";
      ctx.fillRect(0, 0, W, H);

      var r = run();
      var done = !!ran[key()] && showAfter;
      var cx = 300, base = 214;

      ctx.fillStyle = "#3E3730";
      ctx.beginPath();
      ctx.moveTo(cx - 150, base);
      ctx.lineTo(cx + 150, base);
      ctx.lineTo(cx + 132, base + 34);
      ctx.lineTo(cx - 132, base + 34);
      ctx.closePath();
      ctx.fill();
      ctx.fillStyle = "#5C5249";
      ctx.fillRect(cx - 128, base - 10, 256, 12);

      ctx.strokeStyle = "#C6B9A7";
      ctx.lineWidth = 4;
      ctx.beginPath();
      ctx.moveTo(cx - 22, base - 122);
      ctx.lineTo(cx - 22, base - 74);
      ctx.lineTo(cx - 62, base - 12);
      ctx.lineTo(cx + 62, base - 12);
      ctx.lineTo(cx + 22, base - 74);
      ctx.lineTo(cx + 22, base - 122);
      ctx.stroke();
      ctx.fillStyle = (cfg.liquids || {})[rxn] || "rgba(198,185,167,0.3)";
      ctx.beginPath();
      ctx.moveTo(cx - 54, base - 24);
      ctx.lineTo(cx + 54, base - 24);
      ctx.lineTo(cx + 40, base - 44);
      ctx.lineTo(cx - 40, base - 44);
      ctx.closePath();
      ctx.fill();

      // ⚖️ The bung is DRAWN. "Sealed" that changes only a number would
      // teach that the apparatus is incidental to the reading.
      if (vessel === "sealed") {
        ctx.fillStyle = "#8A7A62";
        ctx.fillRect(cx - 28, base - 132, 56, 16);
      }

      if (done && r.gas && r.gas !== "none") {
        ctx.fillStyle = r.gas === "out" ? "#8FB7FF" : "#FFC53D";
        for (var i = 0; i < 7; i++) {
          var y = base - 140 - i * 16;
          var x = cx + Math.sin(i * 1.7) * 26;
          ctx.beginPath();
          ctx.arc(x, y, 6 - i * 0.5, 0, Math.PI * 2);
          ctx.fill();
        }
        ctx.font = '500 15px "DM Mono", ui-monospace, monospace';
        ctx.textAlign = "left";
        ctx.fillText((cfg.gas_labels || {})[r.gas] || "", cx + 44, base - 168);
      }

      var dx = 570, dy = 96;
      ctx.fillStyle = "#221E1B";
      ctx.fillRect(dx, dy, 236, 86);
      ctx.strokeStyle = "#5C5249";
      ctx.lineWidth = 2.5;
      ctx.strokeRect(dx, dy, 236, 86);
      ctx.fillStyle = "#C6B9A7";
      ctx.font = '500 12px "DM Mono", ui-monospace, monospace';
      ctx.textAlign = "left";
      ctx.fillText(done ? (L.after_tag || "AFTER") : (L.before_tag || "BEFORE"),
                   dx + 16, dy + 24);
      ctx.fillStyle = "#FFC53D";
      ctx.font = '500 34px "DM Mono", ui-monospace, monospace';
      ctx.fillText((done ? r.after : r.before).toFixed(DEC), dx + 16, dy + 64);
      ctx.fillStyle = "#C6B9A7";
      ctx.font = '500 15px "DM Mono", ui-monospace, monospace';
      ctx.fillText(L.unit || "g", dx + 150, dy + 64);
      ctx.fillText(L[vessel] || "", dx, dy + 116);
      ctx.textAlign = "center";

      if (canvas.setAttribute) {
        var A = cfg.alt || {};
        canvas.setAttribute("aria-label", (A.template || "")
          .replace("{vessel}", A[vessel] || "")
          .replace("{mass}", (done ? r.after : r.before).toFixed(DEC))
          .replace("{when}", done ? (A.after || "") : (A.before || "")));
      }
    }

    function repaint() {
      var r = run();
      var done = showAfter;
      if (beforeTile) { beforeTile.textContent = mass(r.before); }
      if (afterTile) {
        afterTile.textContent = done ? mass(r.after) : (L.unmeasured || "—");
      }
      if (runBtn) {
        runBtn.textContent = (cfg.run_labels || L)[done ? "done" : "idle"]
          || runBtn.textContent;
        if (done) { runBtn.setAttribute("disabled", ""); }
        else { runBtn.removeAttribute("disabled"); }
      }
      if (statusEl) {
        statusEl.textContent = (L[done ? "status_done" : "status_idle"]) || "";
      }
      if (noteEl) {
        noteEl.textContent = done ? (r.note || "") : (L.idle_note || "");
      }
      draw();
      var n = 0, k;
      for (k in ran) { if (ran[k]) { n += 1; } }
      setCount(sec, n);
      if (n >= doneAt) { markStage(sec, true); }
    }

    function pick(btns, attr, setter) {
      each(btns, function (b) {
        b.addEventListener("click", function () {
          setter(b.getAttribute(attr));
          each(btns, function (x) {
            x.setAttribute("aria-pressed", x === b ? "true" : "false");
          });
          // A different run: the last one's after-mass is not a fact
          // about this one.
          showAfter = false;
          repaint();
        });
      });
    }
    pick(rxnBtns, "data-rxn", function (v) { rxn = v; });
    pick(vesselBtns, "data-vessel", function (v) { vessel = v; });

    if (runBtn) {
      runBtn.addEventListener("click", function () {
        if (showAfter) { return; }
        showAfter = true;
        ran[key()] = true;
        repaint();
      });
    }

    repaint();
    wireBenchGate(sec);
  }

  /* ── the part–whole cover bar (c2-06's rule block) ──
     The MRB-204 cover interaction on the shape the relationship
     actually has. Conservation of mass is a SUM, so it gets a bar.

     ⚠️ RADIO, NOT TOGGLE, and it STARTS COVERED — the opposite
     interaction contract from `wireTriangle`, which removes the cover on
     a second press. Uncovering everything would leave a bar with no
     question in it, and the block's whole demand is "cover the one you
     want". Two different components; the triangle is untouched. */
  function wireCoverBar(root) {
    each(root.querySelectorAll("[data-coverbar]"), function (bar) {
      var results;
      try { results = JSON.parse(bar.getAttribute("data-results") || "{}"); }
      catch (err) { results = {}; }
      var btns = toArray(bar.querySelectorAll(".ks3-bar-btn"));
      var plates = toArray(bar.querySelectorAll("[data-cover-plate]"));
      var resultEl = bar.querySelector("[data-bar-result]");
      var sentenceEl = bar.querySelector("[data-bar-sentence]");

      function show(id) {
        each(plates, function (p) {
          setHidden(p, p.getAttribute("data-cover-plate") !== id);
        });
        each(btns, function (b) {
          b.setAttribute("aria-pressed",
            b.getAttribute("data-cover") === id ? "true" : "false");
        });
        var r = results[id] || {};
        if (resultEl) { resultEl.textContent = r.result || ""; }
        if (sentenceEl) { sentenceEl.textContent = r.sentence || ""; }
        bar.setAttribute("data-covered", id);
      }

      each(btns, function (b) {
        b.addEventListener("click", function () {
          show(b.getAttribute("data-cover"));
        });
      });
      show(bar.getAttribute("data-covered") || "");
    });
  }

  /* ── fifa-pick (c2-06 #s-build) — MRB-204 part 4 ──
     Two multiple-choice ladders, a number and a unit. NOT
     `fifa-construct`, whose four free-text inputs and tick list are a
     different mechanism.

     ⚖️ THE BUTTON IS LOCKED UNTIL ALL FOUR PARTS ARE SET. The unit is
     its own commitment: "2.2" is not an answer to a question about mass.
     Once opened, every control locks — the model is on screen, so a
     changed pick would be choosing after reading the answer. */
  function wirePick(sec) {
    var wrap = sec.querySelector("[data-pick]");
    if (!wrap) { return; }
    var opts = toArray(wrap.querySelectorAll(".ks3-pick-opt"));
    var ans = wrap.querySelector("[data-pick-ans]");
    var unit = wrap.querySelector("[data-pick-unit]");
    var btn = wrap.querySelector("[data-pick-open]");
    var progress = wrap.querySelector("[data-pick-progress]");
    var reveal = wrap.querySelector("[data-reveal]");
    var closeEl = wrap.querySelector("[data-pick-close]");
    var TPL = wrap.getAttribute("data-close") || "";
    var BLANK = wrap.getAttribute("data-blank") || "—";
    var FMT = progress ? progress.textContent.replace(/^\d+/, "{n}") : "";
    var DONE = wrap.getAttribute("data-done-label") || "";
    var picked = {};
    var open = false;

    function committed() {
      var n = 0;
      if (picked["0"] !== undefined) { n += 1; }
      if (picked["1"] !== undefined) { n += 1; }
      if (ans && ans.value.trim() && unit && unit.value) { n += 1; }
      return n;
    }

    function repaint() {
      var n = committed();
      if (progress && !open) {
        progress.textContent = FMT.replace("{n}", String(n));
      }
      if (btn) {
        if (n >= 3 && !open) { btn.removeAttribute("disabled"); }
        else { btn.setAttribute("disabled", ""); }
      }
    }

    each(opts, function (b) {
      b.addEventListener("click", function () {
        if (open) { return; }
        var g = b.getAttribute("data-group");
        picked[g] = b.getAttribute("data-i");
        each(opts, function (x) {
          if (x.getAttribute("data-group") !== g) { return; }
          x.setAttribute("aria-pressed", x === b ? "true" : "false");
        });
        repaint();
      });
    });
    if (ans) {
      ans.addEventListener("input", repaint);
      ans.addEventListener("change", repaint);
    }
    if (unit) { unit.addEventListener("change", repaint); }

    if (btn) {
      btn.addEventListener("click", function () {
        if (open || committed() < 3) { return; }
        open = true;
        // Everything locks: the model is on screen now.
        each(opts, function (x) { x.setAttribute("disabled", ""); });
        if (ans) { ans.setAttribute("disabled", ""); }
        if (unit) { unit.setAttribute("disabled", ""); }
        btn.setAttribute("disabled", "");
        if (progress && DONE) { progress.textContent = DONE; }
        // ⚖️ The closing line quotes the student's OWN input back beside
        // the worked answer. Not a mark — a comparison they make.
        if (closeEl) {
          closeEl.textContent = TPL
            .replace("{answer}", (ans && ans.value.trim()) || BLANK)
            .replace("{unit}", (unit && unit.value) || "");
        }
        setHidden(reveal, false);
        markStage(sec, true);
      });
    }
    repaint();
  }

  /* ── verdict-cards (c2-03 #s-sort · c2-04 #s-sort · c2-04 #s-read) ──
     One-shot commit-and-reveal cards. NOT `sort-task` and NOT
     `sort-rows`: both of those gate every row behind one "open the
     answers" button, and this reveals EACH CARD the instant that card is
     decided — so a student finds out about card 1 before committing on
     card 2, which is what makes the sequence teach.

     ⚖️ Nothing marks correctness (R3 / MRB-196 R10). The chosen option
     keeps the ordinary chosen treatment, the rest dim, the CARD's border
     goes to ink, and the why paragraph is one tone either way. */
  function wireVerdictCards(sec) {
    var wrap = sec.querySelector("[data-vcards]");
    if (!wrap) { return; }
    var cards = toArray(wrap.querySelectorAll(".ks3-vcard"));
    var total = parseInt(wrap.getAttribute("data-total"), 10) || cards.length;
    var closer = wrap.querySelector("[data-vcards-close]");

    function decided() {
      var n = 0;
      each(cards, function (c) {
        if (c.getAttribute("data-open") === "1") { n += 1; }
      });
      return n;
    }

    each(cards, function (card) {
      var opts = toArray(card.querySelectorAll(".ks3-vcard-opt"));
      each(opts, function (btn) {
        btn.addEventListener("click", function () {
          // One commitment per card, and it is final: the reveal is
          // already on screen, so a second pick would be choosing after
          // reading the answer.
          if (card.getAttribute("data-open") === "1") { return; }
          each(opts, function (b) {
            b.setAttribute("aria-pressed", "false");
            b.setAttribute("disabled", "");
          });
          btn.setAttribute("aria-pressed", "true");
          card.setAttribute("data-open", "1");
          setHidden(card.querySelector("[data-reveal]"), false);
          var n = decided();
          setCount(sec, n);
          if (n >= total) {
            if (closer) { setHidden(closer, false); }
            markStage(sec, true);
          }
        });
      });
    });
    setCount(sec, 0);
  }

  /* ── test-budget-bench (c2-02 #s-bench) ──
     Six samples, four tests, and eight tests to spend across all six.

     ⚖️ THE BUDGET IS THE PEDAGOGY. It is GLOBAL, not per sample, and it
     is enforced here as well as by the `disabled` attribute — with
     unlimited tests a student runs everything and never discovers that
     shine, colour and conducting are the three most interesting results
     they can buy and all three are worthless.

     ⚖️ THE INSTRUMENT NEVER MARKS. The verdict panel opens on the
     student's verdict whether or not it was right, and it is the only
     place a sample is named. `element` is authored and read by nothing;
     R3 says a marker must not arrive here. */
  function wireBudgetBench(sec) {
    var wrap = sec.querySelector("[data-budgetbench]");
    if (!wrap) { return; }
    var budget = parseInt(wrap.getAttribute("data-budget"), 10) || 0;
    var total = parseInt(wrap.getAttribute("data-total"), 10) || 0;
    var MARK = wrap.getAttribute("data-marker") || "";
    var tabs = toArray(wrap.querySelectorAll(".ks3-sample-tab"));
    var panels = toArray(wrap.querySelectorAll(".ks3-sample"));
    var closer = wrap.querySelector("[data-bench-close]");
    var used = 0;
    var decided = {};

    function left() { return budget - used; }

    function repaint() {
      var n = 0, k;
      for (k in decided) { if (decided[k]) { n += 1; } }
      setCount(sec, n, { left: left() });
      each(tabs, function (tab) {
        var id = tab.getAttribute("data-sample");
        var lab = tab.querySelector("[data-tab-label]");
        if (!lab) { return; }
        var base = lab.getAttribute("data-base");
        if (base === null) {
          base = lab.textContent;
          lab.setAttribute("data-base", base);
        }
        // Design's only "done" affordance on a tab is a middot appended to
        // the label — a character, not a mark element, so it survives a
        // screen reader reading the button's name.
        lab.textContent = decided[id] ? base + MARK : base;
      });
      each(panels, function (panel) {
        var id = panel.getAttribute("data-sample");
        var spent = !!decided[id];
        each(toArray(panel.querySelectorAll(".ks3-test-btn")), function (b) {
          var ran = b.getAttribute("aria-pressed") === "true";
          if (ran || spent || left() <= 0) { b.setAttribute("disabled", ""); }
          else { b.removeAttribute("disabled"); }
        });
        each(toArray(panel.querySelectorAll(".ks3-verdict-btn")), function (b) {
          if (spent) { b.setAttribute("disabled", ""); }
          else { b.removeAttribute("disabled"); }
        });
      });
      if (n >= total) {
        if (closer) { setHidden(closer, false); }
        markStage(sec, true);
      }
    }

    each(tabs, function (tab) {
      tab.addEventListener("click", function () {
        var id = tab.getAttribute("data-sample");
        each(tabs, function (b) {
          b.setAttribute("aria-pressed",
            b.getAttribute("data-sample") === id ? "true" : "false");
        });
        // Emit-all-show-one: a sample returned to is found exactly as it
        // was left, because its results and verdict never left the DOM.
        each(panels, function (p) {
          setHidden(p, p.getAttribute("data-sample") !== id);
        });
      });
    });

    each(panels, function (panel) {
      var id = panel.getAttribute("data-sample");
      var list = panel.querySelector("[data-results]");
      var vpanel = panel.querySelector("[data-verdict-panel]");

      each(toArray(panel.querySelectorAll(".ks3-test-btn")), function (btn) {
        btn.addEventListener("click", function () {
          // Belt and braces on top of `disabled`: a double-spend here
          // would be the budget quietly not meaning what it says.
          if (btn.getAttribute("aria-pressed") === "true") { return; }
          if (decided[id] || left() <= 0) { return; }
          used += 1;
          btn.setAttribute("aria-pressed", "true");
          var row = panel.querySelector('[data-result="'
            + btn.getAttribute("data-test") + '"]');
          if (row) { setHidden(row, false); }
          if (list) { setHidden(list, false); }
          repaint();
        });
      });

      each(toArray(panel.querySelectorAll(".ks3-verdict-btn")), function (btn) {
        btn.addEventListener("click", function () {
          if (decided[id]) { return; }
          decided[id] = true;
          btn.setAttribute("aria-pressed", "true");
          if (vpanel) { setHidden(vpanel, false); }
          repaint();
        });
      });
    });

    repaint();
    wireBenchGate(sec);
  }

  /* ── scale-zoom (c2-01 #s-scale) ──
     Five steps from a centimetre of wire to the atoms, two buttons, one
     canvas. NOT `zoom-ladder`: that one is a slider over a validated set
     of five plant drawings and would raise on every name here.

     ⚖️ FOUR OF THE FIVE STEPS SHOW NOTHING NEW, and that is the lesson.
     The fourth drawing says "past the reach of any light microscope" in
     words on the canvas rather than showing a smaller orange thing.

     ⚖️ The stage needs every level reached BY STEPPING IN. `seen` seeds
     the opening level and only the in-button adds to it, so backing out
     and climbing again is the only route to the last one — which is
     exactly what Design's own tick condition says. */
  var SCALE_DRAW = {
    /* A cut length of wire, lit along its top edge. */
    "wire": function (ctx, W, H, cx, cy) {
      ctx.fillStyle = "#B7692F";
      ctx.fillRect(120, cy - 26, W - 240, 52);
      ctx.fillStyle = "#D98A4A";
      ctx.fillRect(120, cy - 26, W - 240, 16);
      ctx.fillStyle = "#8A4A1E";
      ctx.fillRect(120, cy + 14, W - 240, 12);
    },
    /* The cut end under a lens: grains, still unmistakably copper. */
    "grains": function (ctx, W, H, cx, cy) {
      ctx.fillStyle = "#B7692F";
      ctx.beginPath();
      ctx.arc(cx, cy, 118, 0, Math.PI * 2);
      ctx.fill();
      ctx.fillStyle = "rgba(217,138,74,0.75)";
      for (var i = 0; i < 40; i++) {
        var a = i * 2.4, r = 20 + (i % 7) * 14;
        ctx.beginPath();
        ctx.arc(cx + Math.cos(a) * r, cy + Math.sin(a) * r * 0.8,
                8 + (i % 3) * 3, 0, Math.PI * 2);
        ctx.fill();
      }
    },
    /* A school microscope's limit: scratches and grain boundaries. */
    "scratches": function (ctx, W, H) {
      ctx.fillStyle = "#A85F2A";
      ctx.fillRect(60, 34, W - 120, H - 88);
      ctx.strokeStyle = "#D98A4A";
      ctx.lineWidth = 3;
      for (var i = 0; i < 14; i++) {
        ctx.beginPath();
        ctx.moveTo(70 + i * 58, 40);
        ctx.lineTo(70 + i * 58 + 26, H - 56);
        ctx.stroke();
      }
      ctx.strokeStyle = "#8A4A1E";
      ctx.lineWidth = 5;
      for (var j = 0; j < 5; j++) {
        ctx.beginPath();
        ctx.moveTo(60, 60 + j * 44);
        ctx.bezierCurveTo(300, 50 + j * 44, 560, 90 + j * 44,
                          W - 60, 66 + j * 44);
        ctx.stroke();
      }
    },
    /* ⚖️ The honest step. Light cannot resolve this, so the canvas says
       so in words instead of drawing a smaller orange thing. */
    "beyond-light": function (ctx, W, H, cx, cy, caption) {
      ctx.fillStyle = "#7A4520";
      ctx.fillRect(60, 34, W - 120, H - 88);
      ctx.fillStyle = "rgba(217,138,74,0.30)";
      for (var i = 0; i < 26; i++) {
        ctx.beginPath();
        ctx.arc(90 + (i * 137) % (W - 180), 60 + (i * 79) % (H - 140),
                30 + (i % 4) * 12, 0, Math.PI * 2);
        ctx.fill();
      }
      ctx.fillStyle = "#C6B9A7";
      ctx.font = '500 16px "DM Mono", ui-monospace, monospace';
      ctx.textAlign = "center";
      ctx.fillText(caption || "", cx, cy);
    },
    /* The atoms: a hexagonally offset lattice, each with a highlight. */
    "lattice": function (ctx) {
      var step = 62;
      for (var row = -1; row < 5; row++) {
        for (var col = -1; col < 16; col++) {
          var x = 70 + col * step + (row % 2 ? step / 2 : 0);
          var y = 50 + row * step * 0.86;
          ctx.beginPath();
          ctx.arc(x, y, 25, 0, Math.PI * 2);
          ctx.fillStyle = "#D98A4A";
          ctx.fill();
          ctx.strokeStyle = "#5A3212";
          ctx.lineWidth = 2.5;
          ctx.stroke();
          ctx.beginPath();
          ctx.arc(x - 7, y - 8, 7, 0, Math.PI * 2);
          ctx.fillStyle = "rgba(255,255,255,0.28)";
          ctx.fill();
        }
      }
    }
  };

  function wireScaleZoom(sec) {
    var wrap = sec.querySelector("[data-scalezoom]");
    if (!wrap) { return; }
    var levels;
    try { levels = JSON.parse(wrap.getAttribute("data-levels") || "[]"); }
    catch (err) { levels = []; }
    if (!levels.length) { return; }

    var canvas = wrap.querySelector("[data-scale-canvas]");
    var readout = wrap.querySelector("[data-scale-readout]");
    var noteEl = wrap.querySelector("[data-scale-note]");
    var btns = toArray(wrap.querySelectorAll(".ks3-scale-btn"));
    var ALT = wrap.getAttribute("data-alt") || "";
    var z = parseInt(wrap.getAttribute("data-start"), 10) || 0;
    var seen = {};
    seen[z] = true;

    function alt(level) {
      return ALT.replace("{scale}", level.scale || "")
        .replace("{label}", (level.label || "").toLowerCase());
    }

    function draw() {
      if (!canvas || !canvas.getContext) { return; }
      var ctx = canvas.getContext("2d");
      var W = 900, H = 310;
      ctx.setTransform(1, 0, 0, 1, 0, 0);
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      ctx.setTransform(2, 0, 0, 2, 0, 0);
      ctx.fillStyle = "#100D0A";
      ctx.fillRect(0, 0, W, H);
      var cx = W / 2, cy = H / 2 + 6;
      var lv = levels[z] || levels[0];

      ctx.save();
      ctx.beginPath();
      ctx.rect(60, 34, W - 120, H - 88);
      ctx.clip();
      var fn = SCALE_DRAW[lv.drawing];
      if (fn) { fn(ctx, W, H, cx, cy, lv.caption); }
      ctx.restore();

      ctx.strokeStyle = "#5C5249";
      ctx.lineWidth = 2;
      ctx.strokeRect(60, 34, W - 120, H - 88);

      ctx.fillStyle = "#FFC53D";
      ctx.font = '500 15px "DM Mono", ui-monospace, monospace';
      ctx.textAlign = "left";
      ctx.fillText((lv.label || "").toUpperCase(), 62, 24);
      ctx.textAlign = "right";
      ctx.fillStyle = "#C6B9A7";
      ctx.fillText(lv.scale || "", W - 62, 24);
      ctx.textAlign = "center";

      // The step strip: how far in you are, drawn rather than counted.
      var bw = (W - 120) / levels.length;
      for (var i = 0; i < levels.length; i++) {
        ctx.fillStyle = i <= z ? "#FFC53D" : "#3E3730";
        ctx.fillRect(60 + i * bw + 3, H - 42, bw - 6, 9);
      }
      if (canvas.setAttribute) { canvas.setAttribute("aria-label", alt(lv)); }
    }

    function repaint() {
      var lv = levels[z] || levels[0];
      if (readout) { readout.textContent = lv.scale || ""; }
      if (noteEl) { noteEl.textContent = lv.note || ""; }
      each(btns, function (b) {
        var d = parseInt(b.getAttribute("data-step"), 10);
        var at = d < 0 ? z === 0 : z >= levels.length - 1;
        if (at) { b.setAttribute("disabled", ""); }
        else { b.removeAttribute("disabled"); }
      });
      draw();
      setCount(sec, z + 1);
      var n = 0, k;
      for (k in seen) { if (seen[k]) { n += 1; } }
      if (n >= levels.length) { markStage(sec, true); }
    }

    each(btns, function (b) {
      b.addEventListener("click", function () {
        var d = parseInt(b.getAttribute("data-step"), 10) || 0;
        var next = Math.max(0, Math.min(levels.length - 1, z + d));
        if (next === z) { return; }
        z = next;
        // Only stepping IN banks a level, which is Design's own rule and
        // is what makes the last step a thing a student went and got.
        if (d > 0) { seen[z] = true; }
        repaint();
      });
    });

    repaint();
  }

/* ═══ BEGIN C1 ═══ */
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


/* WIRE: each(root.querySelectorAll("[data-ebenchblock]"), wireEvidenceBench);
   — add to wireInstruments(), in the C1 group. Uses each / toArray /
   setHidden / setCount / markStage / appendAuthored, all already in scope. */

  /* ── evidence-bench (c1-06 #s-bench) ──
     Seven observations, each judged once and answered immediately. No gate:
     the seven judgements ARE the commitment, which is why this is the one
     flagship instrument in C1 that is open from the start.

     ⚖️ THE SCORED CALL IS LATCHED ON THE FIRST PRESS. Design recomputes the
     tally from live state, so a student who changes an answer after reading
     the verdict moves a number whose own sentence says "before opening the
     verdict". `data-called` records the first call and never moves; the
     buttons stay live because Design leaves them live and pressing again
     changes nothing else.

     ⚠️ NOTHING HERE MARKS THE STUDENT (R3 / MRB-196 R10). The verdict panel's
     ground is a fact about the model, decided at build time from `ok`. This
     function never compares a call to it except to count, and the count is
     never attached to a case. */
  function wireEvidenceBench(sec) {
    var wrap = sec.querySelector("[data-ebench]");
    if (!wrap) { return; }
    var cases = toArray(wrap.querySelectorAll(".ks3-ebench-case"));
    var total = parseInt(wrap.getAttribute("data-total"), 10) || cases.length;
    var panel = wrap.querySelector("[data-ebench-tally]");
    var line = wrap.querySelector("[data-tallyline]");
    var fmt = wrap.getAttribute("data-tally") || "";
    var allLabel = wrap.getAttribute("data-all") || "";
    // The block-head counter belongs to the shell, not to this instrument;
    // `setCount` writes it for every other counting block and this one only
    // reaches past it for the authored full-set label, which `_head_counter`
    // has no branch for.
    var counter = sec.querySelector("[data-count]");

    function judged() {
      var n = 0;
      each(cases, function (c) {
        if (c.getAttribute("data-open") === "1") { n += 1; }
      });
      return n;
    }

    /* How many the student CALLED right, from the latched first press. */
    function called() {
      var n = 0;
      each(cases, function (c) {
        var call = c.getAttribute("data-called");
        if (call !== null && call === c.getAttribute("data-ok")) { n += 1; }
      });
      return n;
    }

    function close() {
      if (line) {
        line.textContent = "";
        // Authored text, never textContent: the sentence carries an em dash
        // today and the helper is what draws → ✓ ✕ if one ever arrives.
        appendAuthored(line, fmt.split("{n}").join(String(called())));
      }
      if (panel) { setHidden(panel, false); }
      if (counter && allLabel) {
        counter.textContent = "";
        appendAuthored(counter, allLabel);
      }
      markStage(sec, true);
    }

    each(cases, function (c) {
      var btns = toArray(c.querySelectorAll(".ks3-ebench-btn"));
      each(btns, function (btn) {
        btn.addEventListener("click", function () {
          each(btns, function (b) { b.setAttribute("aria-pressed", "false"); });
          btn.setAttribute("aria-pressed", "true");
          if (c.getAttribute("data-called") === null) {
            c.setAttribute("data-called", btn.getAttribute("data-call"));
          }
          c.setAttribute("data-open", "1");
          setHidden(c.querySelector("[data-reveal]"), false);
          var n = judged();
          if (n >= total) { close(); } else { setCount(sec, n); }
        });
      });
    });

    setCount(sec, 0);
  }


/* WIRE: each(root.querySelectorAll("[data-gapblock]"), wireGapTestRig); */

  /* ── gap-test-rig (c1-01 #s-gap) ──

     ⚖️ THE RIG NEVER MARKS THE CHOICE. It packs the gap with whatever the
     student said is in it and then runs a test they already know the
     answer to from the top of the page. Three tests, and every wrong
     answer fails all three — which is an argument, not a verdict, and it
     stays an argument only as long as nothing here goes green or red.

     ⚠️ The discriminator is POSITIONAL and comes from the markup
     (`data-empty-choice`), never from the option's text. Design compares
     against a literal 3 written three lines from the list it indexes.

     Nothing animates: the two boxes are a before-and-after, not a
     process, so reduced motion loses nothing at all here. */
  function wireGapTestRig(sec) {
    var wrap = sec.querySelector("[data-gap]");
    if (!wrap) { return; }

    var EMPTY = parseInt(wrap.getAttribute("data-empty-choice"), 10);
    var ALT = wrap.getAttribute("data-alt") || "";
    var ALT_FILLED = wrap.getAttribute("data-alt-filled") || "";
    var ALT_EMPTY = wrap.getAttribute("data-alt-empty") || "";
    var L_EMPTY = wrap.getAttribute("data-label-empty") || "";
    var L_FILLED = wrap.getAttribute("data-label-filled") || "";
    var F_EMPTY = wrap.getAttribute("data-foot-empty") || "";
    var F_FILLED = wrap.getAttribute("data-foot-filled") || "";

    var rig = wrap.querySelector("[data-gap-rig]");
    var canvas = wrap.querySelector("[data-gap-canvas]");
    var opts = toArray(wrap.querySelectorAll(".ks3-option"));
    var testBtns = toArray(wrap.querySelectorAll(".ks3-gap-test"));
    var notes = toArray(wrap.querySelectorAll("[data-note]"));

    var choice = null;
    var test = null;

    // "Something is in the gap" — the state every test is about to
    // contradict. A choice not yet made is not a filled gap.
    function filled() { return choice !== null && choice !== EMPTY; }

    function draw() {
      if (!canvas || !canvas.getContext) { return; }
      var ctx = canvas.getContext("2d");
      var W = 900, H = 260;
      ctx.setTransform(1, 0, 0, 1, 0, 0);
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      ctx.setTransform(2, 0, 0, 2, 0, 0);
      ctx.fillStyle = "#100D0A";
      ctx.fillRect(0, 0, W, H);

      var half = W / 2;
      var packed = filled();

      function drawBox(x0, label, solid) {
        ctx.save();
        ctx.beginPath();
        ctx.rect(x0 + 34, 52, half - 68, H - 108);
        ctx.clip();
        // The fill IS the answer: the space between the particles stops
        // being space. Clipped to the box so it cannot read as a
        // background, and the particles are drawn identically in both
        // boxes so the only difference on screen is the gap.
        if (solid) {
          ctx.fillStyle = "#4A4038";
          ctx.fillRect(x0 + 34, 52, half - 68, H - 108);
        }
        for (var row = 0; row < 4; row++) {
          for (var col = 0; col < 7; col++) {
            var x = x0 + 62 + col * 54 + (row % 2 ? 16 : 0);
            var y = 78 + row * 44;
            ctx.beginPath();
            ctx.arc(x, y, 17, 0, Math.PI * 2);
            ctx.fillStyle = "#D98A4A";
            ctx.fill();
            ctx.strokeStyle = "#5A3212";
            ctx.lineWidth = 2;
            ctx.stroke();
          }
        }
        ctx.restore();
        ctx.strokeStyle = "#5C5249";
        ctx.lineWidth = 2;
        ctx.strokeRect(x0 + 34, 52, half - 68, H - 108);
        ctx.fillStyle = solid ? "#FF8A5B" : "#FFC53D";
        ctx.font = '500 14px "DM Mono", ui-monospace, monospace';
        ctx.textAlign = "center";
        ctx.fillText(label, x0 + half / 2, 40);
      }

      drawBox(0, L_EMPTY, false);
      drawBox(half, packed ? L_FILLED : L_EMPTY, packed);

      ctx.fillStyle = "#C6B9A7";
      ctx.font = '500 13px "DM Mono", ui-monospace, monospace';
      ctx.textAlign = "center";
      ctx.fillText(packed ? F_FILLED : F_EMPTY, W / 2, H - 20);

      if (canvas.setAttribute) {
        canvas.setAttribute("aria-label",
          ALT.replace("{right}", packed ? ALT_FILLED : ALT_EMPTY));
      }
    }

    function repaint() {
      // Which of the eight authored paragraphs is on screen. With a test
      // running it is that test's outcome — `on` when the gap is genuinely
      // empty, `off` when the student filled it — and before any test it
      // is one of the two opening lines.
      var want = test === null ? (filled() ? "filled" : "empty")
        : test + (filled() ? "-off" : "-on");
      each(notes, function (p) {
        setHidden(p, p.getAttribute("data-note") !== want);
      });
      draw();
      // One test run is the stage: the student has taken the model
      // somewhere it can be checked. Changing the answer afterwards
      // re-runs the same test against the new gap, which is the point.
      if (test !== null) { markStage(sec, true); }
    }

    each(opts, function (btn, i) {
      btn.addEventListener("click", function () {
        choice = i;
        each(opts, function (b) {
          b.setAttribute("aria-pressed", b === btn ? "true" : "false");
        });
        // Gating by absence, as everywhere else in the key stage: the rig
        // is not there to be looked at until a claim has been made about
        // what it is going to show.
        if (rig) { setHidden(rig, false); }
        repaint();
      });
    });

    each(testBtns, function (btn) {
      btn.addEventListener("click", function () {
        test = btn.getAttribute("data-test");
        each(testBtns, function (b) {
          b.setAttribute("aria-pressed", b === btn ? "true" : "false");
        });
        repaint();
      });
    });

    draw();
  }


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
      // ⊕ MRB-228. `{n} halvings` reads "after 1 halvings" at the first cut,
      // and this label IS the drawing for a screen reader — the piece, the
      // scale bar and the progress ticks are all on the canvas. The template
      // stays as Design wrote it, with the plural taken off the one value
      // where it is wrong, rather than a second template being authored for a
      // single word.
      return ALT.replace("{n} halvings", n === 1 ? "1 halving"
                                                 : String(n) + " halvings")
        .replace("{n}", String(n))
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


/* WIRE: each(root.querySelectorAll("[data-keyedblock]"), wireKeyedCommit);
   — add to wireInstruments(), in the C1 group. Uses each / toArray /
   setHidden / markStage, all already in scope. */

  /* ── keyed-commit (c1-06 #s-verdict, c1-03 #s-bubble) ──
     Four options, each carrying its own answer. The panel's first paragraph
     is the one the student earned; the rest is what everybody reads.

     Emit-both-show-one: all four replies are in the document and hidden, and
     this function swaps which one is shown. Nothing is assembled from an
     attribute, so `<em>`, em dashes and right single quotes survive intact —
     which matters here more than usual, because every reply is a sentence
     about what scientists actually did.

     ⚠️ R3 — NOTHING MARKS. The chosen option takes the ordinary chosen
     treatment and nothing else, and the panel opens on whatever was chosen.
     There is no `data-correct` anywhere in this instrument and there must not
     be: `answer_index` is checked at build time and never reaches the page.

     The choice stays changeable. The block is a commitment, not a question:
     a student who changes their mind reads the other answer, which is the
     block working rather than a leak. */
  function wireKeyedCommit(sec) {
    var wrap = sec.querySelector("[data-keyed]");
    if (!wrap) { return; }
    var opts = toArray(wrap.querySelectorAll(".ks3-option"));
    var panel = wrap.querySelector("[data-reveal]");
    var replies = toArray(wrap.querySelectorAll(".ks3-keyed-reply"));
    if (!opts.length || !panel) { return; }

    each(opts, function (btn) {
      btn.addEventListener("click", function () {
        var i = btn.getAttribute("data-i");
        each(opts, function (b) {
          b.setAttribute("aria-pressed",
            b.getAttribute("data-i") === i ? "true" : "false");
        });
        each(replies, function (p) {
          setHidden(p, p.getAttribute("data-reply") !== i);
        });
        if (panel.hasAttribute("hidden")) {
          setHidden(panel, false);
          // Announced for screen-reader users, who would otherwise get no
          // signal that a panel of new prose appeared below the buttons.
          panel.setAttribute("role", "status");
        }
        markStage(sec, true);
      });
    });
  }


/* WIRE: each(root.querySelectorAll("[data-mtlblock]"), wireModelTimeline);
   — add to wireInstruments(), in the C1 group. Uses each / toArray /
   setHidden / markStage, all already in scope. */

  /* ── model-timeline (c1-06 #s-history) ──
     Five models, one detail card, emit-all-show-one: every card is in the
     document and one is shown, so going back to a model finds it as it was
     and no authored sentence is ever rebuilt from an attribute.

     ⚖️ THE STAGE PREDICATE IS A SET AND IT NEVER EMPTIES. Design's page ticks
     on `history !== 1` — an inequality against the DEFAULT — so the stage
     ticks when any other model is opened and UNTICKS when a student who has
     read all five returns to Dalton. A rail stop that goes backwards is worse
     than one that never moved. What the page means is "has looked at more
     than the one it opened on", which is a set: seed it with the default,
     add on every press, tick at two, never remove. Same class of defect as
     c1-04's `Math.max(touched, N)`.

     No timer, no animation, nothing to scale under reduced motion. */
  function wireModelTimeline(sec) {
    var wrap = sec.querySelector("[data-mtl]");
    if (!wrap) { return; }
    var btns = toArray(wrap.querySelectorAll(".ks3-mtl-step"));
    var cards = toArray(wrap.querySelectorAll(".ks3-mtl-card"));
    if (!btns.length) { return; }

    // The row opens on Dalton, not on Democritus. Seeding the set with the
    // default is what makes "more than the default" mean what it says.
    var seen = {};
    seen[wrap.getAttribute("data-default") || "0"] = true;

    function counted() {
      var n = 0, k;
      for (k in seen) { if (seen[k]) { n += 1; } }
      return n;
    }

    each(btns, function (btn) {
      btn.addEventListener("click", function () {
        var i = btn.getAttribute("data-step");
        each(btns, function (b) {
          b.setAttribute("aria-pressed",
            b.getAttribute("data-step") === i ? "true" : "false");
        });
        each(cards, function (c) {
          setHidden(c, c.getAttribute("data-step") !== i);
        });
        seen[i] = true;
        // Sticky in one direction only: a stage that has been reached stays
        // reached, whatever the student looks at next.
        if (counted() >= 2) { markStage(sec, true); }
      });
    });
  }


// WIRE: each(root.querySelectorAll("[data-predictblock]"), wirePredictionStack);
//
// Splice point: `wireInstruments()` in shared/ks3.js, in the new
// "C1 · Particles and their behaviour" group, beside wireCollisionCounter.
// Uses the file's existing `each`, `toArray`, `setHidden` and `markStage`.

  /* ── prediction-stack (c1-04 #s-predict) ──
     Three predictions, one shared option set, one shared fallback.

     ⚖️ A PREDICTION MAY BE CHANGED. Design's state is a map from
     prediction id to index and a second press overwrites it, so a
     student who reads "go back to the bench and try it" can come back
     and answer again — which is exactly what that sentence asks them to
     do. Locking the row after one press would make the instruction
     impossible to follow.

     ⚖️ THE PANEL CARRIES THE VERDICT, NOT THE OPTION. The chosen button
     keeps the ordinary chosen treatment; what changes is the panel's
     border and which of the two notes is showing. Nothing inside the
     option list marks the student.

     Both notes are already in the document — this only unhides one, so
     no student-facing string is ever built here. */
  function wirePredictionStack(sec) {
    var wrap = sec.querySelector("[data-predictstack]");
    if (!wrap) { return; }
    var panels = toArray(wrap.querySelectorAll(".ks3-predict"));
    var total = parseInt(wrap.getAttribute("data-total"), 10) || panels.length;
    var answered = {};

    each(panels, function (panel) {
      var id = panel.getAttribute("data-prediction");
      var answer = parseInt(panel.getAttribute("data-answer"), 10);
      var opts = toArray(panel.querySelectorAll(".ks3-predict-btn"));
      var right = panel.querySelector('[data-tone="right"]');
      var wrong = panel.querySelector('[data-tone="wrong"]');

      each(opts, function (btn) {
        btn.addEventListener("click", function () {
          var i = parseInt(btn.getAttribute("data-i"), 10);
          each(opts, function (b) {
            b.setAttribute("aria-pressed", b === btn ? "true" : "false");
          });
          var ok = i === answer;
          panel.setAttribute("data-right", ok ? "1" : "0");
          setHidden(right, !ok);
          setHidden(wrong, ok);

          answered[id] = true;
          var n = 0, k;
          for (k in answered) { if (answered[k]) { n += 1; } }
          if (n >= total) { markStage(sec, true); }
        });
      });
    });
  }


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


// WIRE: (none — `scale-cards` registers no wire function and takes no line in
//        `wireInstruments()`.)
//
// This file exists so the question "where is the JS for scale-cards?" is
// answered once, in the place someone will look, instead of being re-asked
// every time the kind is touched.
//
// The component is STATIC. Three cards and a closing paragraph: no control, no
// state, no canvas, nothing to reveal and nothing to count. There is no
// behaviour to attach, so attaching an empty `wireScaleCards(sec)` would be a
// dispatch-table entry pretending to be a component — the exact thing the
// comment above `ACTIVITY_KIND_RENDERERS` warns about.
//
// Two consequences worth stating, because both look like omissions:
//
//   1. The section carries `data-instrument`, which has a real job even with
//      no wiring: it keeps `wirePredictions` out. There are no `.ks3-option`
//      elements inside this block today, so nothing would be mis-wired — but
//      the exclusion is a property of the kind, not of this instance, and a
//      future card that gained a control would otherwise inherit the generic
//      Law 4 wiring silently.
//
//   2. `data-scalecards` is the marker attribute the dispatch table names. It
//      selects nothing in `shared/ks3.js` and is not meant to: it is the hook
//      the stylesheet and the parity rows and any future behaviour attach to,
//      and having it means the day this kind DOES gain a control the selector
//      already exists rather than being invented then.
//
// The block is not a rail stop either, so it declares no `data-stage-done` and
// there is no `markStage` call to make. See the renderer's docstring.


/* WIRE: each(root.querySelectorAll("[data-sortcardsblock]"), wireSortCards);   // inside wireInstruments()

   Splice into shared/ks3.js beside the other C1 instruments. */

  /* ── sort-cards (c1-03 #s-think) ──
     Four everyday events and the word that fits each one.

     ⚠️ NOT one-shot. `job-sort` and `verdict-cards` disable a row the
     instant it is decided, because their reveal is the answer. This one
     stays open on purpose: Design's page lets a student change the word
     and follow the card as it changes, and the block's own lede says
     "the sorting is the point, not the score". A locked card would make
     it a test, which is what that sentence says it is not — and R3's own
     rule for an activity option is that it "stays enabled so the student
     can change their mind".

     ⚖️ The stage ticks on all four DECIDED, right or wrong, and it never
     unticks — a card that is re-answered was already answered. */
  function wireSortCards(sec) {
    var wrap = sec.querySelector("[data-sortcards]");
    if (!wrap) { return; }
    var cards = toArray(wrap.querySelectorAll(".ks3-sortcards-card"));
    var total = parseInt(wrap.getAttribute("data-total"), 10) || cards.length;
    var closer = wrap.querySelector("[data-sortcards-close]");
    var decided = {};

    function count() {
      var n = 0, k;
      for (k in decided) { if (decided[k]) { n += 1; } }
      return n;
    }

    each(cards, function (card) {
      var opts = toArray(card.querySelectorAll(".ks3-sortcards-opt"));
      var right = card.querySelector('[data-note="right"]');
      var wrong = card.querySelector('[data-note="wrong"]');
      var answer = card.getAttribute("data-answer");
      each(opts, function (btn) {
        btn.addEventListener("click", function () {
          var choice = btn.getAttribute("data-choice");
          var ok = choice === answer;
          each(opts, function (b) {
            b.setAttribute("aria-pressed", b === btn ? "true" : "false");
          });
          // Emit-both-show-one: both authored notes are already in the
          // document and one of them is unhidden. Nothing is composed.
          setHidden(right, !ok);
          setHidden(wrong, ok);
          // One attribute carries the card's whole marked state, so the
          // border rule lives in CSS and can be ruled on there.
          card.setAttribute("data-verdict", ok ? "right" : "wrong");
          decided[card.getAttribute("data-card")] = true;
          var n = count();
          setCount(sec, n);
          if (n >= total) {
            if (closer) { setHidden(closer, false); }
            markStage(sec, true);
          }
        });
      });
    });
  }


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


// WIRE: each(root.querySelectorAll("[data-smatrixblock]"), wireStateMatrix);
//
// ⚠️ Wire this AFTER `wireStateBench` in `wireInstruments()`, beside it. The
// order is tidiness rather than correctness: the matrix does a standing read of
// its own at wire time and the bench's resting attributes are in the markup
// from the build, so a matrix wired first still opens on the right row.

  /* ── state-matrix (c1-02 #s-matrix) ──
     Six properties against three states, with ONE ROW LIT by the bench
     above it.

     ⚖️ CROSS-BLOCK STATE, AND NO SECOND COPY OF IT. This is the first
     component in the key stage that reads another block's state, and the
     obvious build — keep `squash` and `trails` here too and update both
     from one handler — is the wrong one: two copies of a fact are two
     places for it to drift, and the bug that produces (a table lighting
     the row the bench stopped showing) is silent. So the bench PUBLISHES
     on `[data-sbench]` and the matrix READS. The broadcast it listens for
     carries no payload at all; it means "look again", nothing more.

     ⚖️ NOT A RAIL STOP. `markStage` is never called from here and the
     renderer emits no `data-stage-done`: this section asks the student for
     nothing, and MRB-208 rules the rail carries only sections that do.
     Design's own stage 3 ticks on the bench's predicate — see the
     renderer's docstring and the lesson module. */

  function wireStateMatrix(sec) {
    var wrap = sec.querySelector("[data-smatrix]");
    if (!wrap) { return; }
    var rows = toArray(wrap.querySelectorAll(".ks3-smatrix-row"));
    if (!rows.length) { return; }

    var from = wrap.getAttribute("data-from") || "";
    var LIT = {
      squash: wrap.getAttribute("data-lit-squash") || "",
      trails: wrap.getAttribute("data-lit-trails") || "",
      rest:   wrap.getAttribute("data-lit-rest") || ""
    };

    function bench() {
      var host = from ? document.getElementById(from) : null;
      return host ? host.querySelector("[data-sbench]") : null;
    }

    function paint() {
      var b = bench();
      // No bench on the page — a lesson that dropped it, or a build that
      // renamed the section. The table still reads correctly: it stays on the
      // resting row rather than lighting nothing, because the footnote under
      // it promises a highlight and an unlit table would make that a lie.
      var key = LIT.rest;
      if (b) {
        if (b.getAttribute("data-squash") === "1") { key = LIT.squash; }
        else if (b.getAttribute("data-trails") === "1") { key = LIT.trails; }
      }
      each(rows, function (tr) {
        var on = tr.getAttribute("data-row") === key;
        tr.setAttribute("data-lit", on ? "1" : "0");
        var head = tr.querySelector("th");
        if (!head) { return; }
        // R2 — the tint is never the only signal. Design draws colour alone
        // and the footnote promises the student a highlight, so the lit row
        // says so to a screen reader too.
        if (on) { head.setAttribute("aria-current", "true"); }
        else { head.removeAttribute("aria-current"); }
      });
    }

    document.addEventListener("ks3:statebench", paint);
    paint();
  }
/* ═══ END C1 ═══ */





/* ═══ BEGIN B2 ═══ */
/* WIRE: each(root.querySelectorAll("[data-leverblock]"), wireArmLever);
   — add to wireInstruments(), in the B2 group beside wireMusclePair. Uses
   each / toArray / setHidden / setCount / markStage / wireBenchGate, all
   already in scope. */

  /* ═══════════════════════════════════════════════════════════════
     ── arm-lever (b2-04 #s-bench) — the forearm rig ──

     ⚖️ THE INSTRUMENT WITHHOLDS ONE NUMBER AND THAT IS THE LESSON. Three
     readouts are handed over; the fourth says "not measured — you work it
     out" until the meter is fitted, and the muscle arrow on the canvas is
     labelled with a word and no magnitude. Both routes to the answer are
     closed by the same flag, so there is one thing to get wrong rather
     than two. If a future change makes the force readable before the
     meter, the lesson is gone and every gate on this page still passes.

     ⚖️ THE RAIL STOP IS A SET, NOT A COUNT. `touched` keys on the control
     NAME, so dragging the mass slider twenty times is one control moved.
     Design's own predicate is already a set and this keeps it one —
     `Math.max(touched, n)` is the shape that let c1-04 read "all controls
     tried" after a single button.

     ⚖️ NOTHING ANIMATES. The rig is a static drawing repainted when a
     control moves, so `prefers-reduced-motion` has nothing to degrade
     here (the same note `wireHalvingBench` and `wireClaimSwitch` carry)
     and the reduced-motion experience is the COMPLETE one rather than a
     lesser one. There is no tick to scale, and adding one would animate
     an arm that is deliberately held still — the whole page is about the
     case where nothing is moving.

     The number formatter and the aria-label composition are duplicated in
     `build_ks3.py` (`_lever_num`, `_lever_alt`) on purpose: the resting
     page has to render "20 N" and its label before any JS runs. Two
     implementations, one composition, checked at both ends of both
     sliders.
     ═══════════════════════════════════════════════════════════════ */
  function wireArmLever(sec) {
    var wrap = sec.querySelector("[data-lever]");
    if (!wrap) { return; }

    var G = parseFloat(wrap.getAttribute("data-g")) || 10;
    var DONE_AT = parseInt(wrap.getAttribute("data-done-at"), 10) || 2;
    var UNMEASURED = wrap.getAttribute("data-unmeasured") || "";
    var ALT = wrap.getAttribute("data-alt") || "";
    var ALT_MEASURED = wrap.getAttribute("data-alt-measured") || "";
    var C_TITLE = wrap.getAttribute("data-canvas-title") || "";
    var C_JOINT = wrap.getAttribute("data-canvas-joint") || "";
    var C_MUSCLE = wrap.getAttribute("data-canvas-muscle") || "";
    var C_LOAD = wrap.getAttribute("data-canvas-load") || "{n} N";
    var M_LABEL = wrap.getAttribute("data-meter-label") || "";
    var M_DONE = wrap.getAttribute("data-meter-done") || "";
    var M_NOTE = wrap.getAttribute("data-meter-note") || "";
    var M_NOTE_DONE = wrap.getAttribute("data-meter-note-done") || "";

    var canvas = wrap.querySelector("[data-lever-canvas]");
    var values = toArray(wrap.querySelectorAll("[data-lever-value]"));
    var outs = toArray(wrap.querySelectorAll("[data-lever-out]"));
    var inputs = toArray(wrap.querySelectorAll("[data-lever-input]"));
    var tabs = toArray(wrap.querySelectorAll("[data-lever-tab]"));
    var meterBtn = wrap.querySelector("[data-lever-meter]");
    var note = wrap.querySelector("[data-lever-note]");

    var dp = {
      load: parseInt(wrap.getAttribute("data-dp-load"), 10) || 0,
      ins: parseInt(wrap.getAttribute("data-dp-ins"), 10) || 0,
      hand: parseInt(wrap.getAttribute("data-dp-hand"), 10) || 0
    };
    var state = {
      load: parseFloat(wrap.getAttribute("data-load")),
      ins: parseFloat(wrap.getAttribute("data-ins")),
      hand: parseFloat(wrap.getAttribute("data-hand"))
    };
    var touched = {};
    var meterShown = false;

    /* Weight is mass × g; the turning effect of the load is weight × its
       distance from the joint; and the muscle, attached far closer in, must
       produce the same turning effect over a much smaller distance. Both
       distances go into metres, which cancels — the ratio is what matters —
       but they are converted anyway so the arithmetic here is the same
       arithmetic the student is asked to write down. */
    function weight() { return state.load * G; }
    function muscleForce() {
      return (weight() * (state.hand / 100)) / (state.ins / 100);
    }

    function num(v, places, fmt) {
      return (fmt || "{n}").replace("{n}", Number(v).toFixed(places));
    }

    /* ⚠️ "after 1 halvings" is why this exists. No control on this rig can
       currently reach a bare 1 — the two sliders render to one decimal and
       the tabs offer 32 and 16 — but the guard is cheap and a plural that
       breaks for one authored value is exactly the defect that ships. */
    function altText() {
      var out = ALT.replace("{load}", num(state.load, dp.load))
        .replace("{ins}", num(state.ins, dp.ins))
        .replace("{hand}", num(state.hand, dp.hand));
      if (meterShown && ALT_MEASURED) {
        out += ALT_MEASURED.replace("{force}", num(muscleForce(), 0));
      }
      return out.split(" 1 kilograms").join(" 1 kilogram")
        .split(" 1 centimetres").join(" 1 centimetre")
        .split(" 1 newtons").join(" 1 newton");
    }

    function arrow(ctx, x, y, dy, colour, label) {
      ctx.strokeStyle = colour;
      ctx.fillStyle = colour;
      ctx.lineWidth = 5;
      ctx.beginPath();
      ctx.moveTo(x, y);
      ctx.lineTo(x, y + dy);
      ctx.stroke();
      var s = dy > 0 ? 1 : -1;
      ctx.beginPath();
      ctx.moveTo(x, y + dy + s * 14);
      ctx.lineTo(x - 11, y + dy);
      ctx.lineTo(x + 11, y + dy);
      ctx.closePath();
      ctx.fill();
      ctx.font = '500 16px "DM Mono", ui-monospace, monospace';
      ctx.textAlign = "center";
      ctx.fillText(label, x, y + dy + s * 34);
    }

    function draw() {
      if (!canvas || !canvas.getContext) { return; }
      var ctx = canvas.getContext("2d");
      var W = 900, H = 350;
      ctx.setTransform(1, 0, 0, 1, 0, 0);
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      ctx.setTransform(2, 0, 0, 2, 0, 0);
      ctx.fillStyle = "#100D0A";
      ctx.fillRect(0, 0, W, H);

      var scale = 17;                       // px per cm
      var elx = 150, ely = 190;
      var handX = elx + state.hand * scale;
      var insX = elx + state.ins * scale;

      // Upper arm: an ink outline under a bone-coloured core, which is what
      // gives every limb on this canvas a drawn edge against the ink ground.
      ctx.lineCap = "round";
      ctx.strokeStyle = "#100D0A";
      ctx.lineWidth = 30;
      ctx.beginPath();
      ctx.moveTo(elx, ely);
      ctx.lineTo(elx, ely - 128);
      ctx.stroke();
      ctx.strokeStyle = "#F4E9D8";
      ctx.lineWidth = 24;
      ctx.beginPath();
      ctx.moveTo(elx, ely);
      ctx.lineTo(elx, ely - 128);
      ctx.stroke();

      // The muscle, curving from high on the upper arm down to its
      // attachment. The attachment point MOVES with the slider — that is the
      // whole variable, and a muscle drawn at a fixed angle would hide it.
      ctx.strokeStyle = "#FFC53D";
      ctx.lineWidth = 15;
      ctx.beginPath();
      ctx.moveTo(elx + 16, ely - 118);
      ctx.quadraticCurveTo(elx + 34, ely - 60, insX, ely - 12);
      ctx.stroke();

      // Forearm, held level.
      ctx.strokeStyle = "#100D0A";
      ctx.lineWidth = 28;
      ctx.beginPath();
      ctx.moveTo(elx, ely);
      ctx.lineTo(handX, ely);
      ctx.stroke();
      ctx.strokeStyle = "#F4E9D8";
      ctx.lineWidth = 22;
      ctx.beginPath();
      ctx.moveTo(elx, ely);
      ctx.lineTo(handX, ely);
      ctx.stroke();

      // The joint, named on the drawing: every distance on this page is
      // measured from it and an unlabelled pivot leaves "from the elbow"
      // pointing at nothing.
      ctx.beginPath();
      ctx.arc(elx, ely, 16, 0, Math.PI * 2);
      ctx.fillStyle = "#C6B9A7";
      ctx.fill();
      ctx.strokeStyle = "#100D0A";
      ctx.lineWidth = 3;
      ctx.stroke();
      ctx.fillStyle = "#C6B9A7";
      ctx.font = '500 14px "DM Mono", ui-monospace, monospace';
      ctx.textAlign = "center";
      ctx.fillText(C_JOINT, elx, ely + 44);

      // The hand, and the load hanging from it. The block grows with the
      // mass so the slider has something to say on the drawing as well as in
      // the readout.
      ctx.fillStyle = "#F4E9D8";
      ctx.beginPath();
      ctx.arc(handX, ely, 15, 0, Math.PI * 2);
      ctx.fill();
      ctx.strokeStyle = "#100D0A";
      ctx.lineWidth = 3;
      ctx.stroke();
      var bw = 34 + state.load * 7;
      ctx.fillStyle = "#8FB7FF";
      ctx.fillRect(handX - bw / 2, ely + 24, bw, 26 + state.load * 3);
      ctx.strokeRect(handX - bw / 2, ely + 24, bw, 26 + state.load * 3);

      // ⚖️ THE TWO ARROWS ARE NOT SYMMETRICAL, AND THAT IS THE GATE. The load
      // arrow carries its magnitude, because the rig measured it. The muscle
      // arrow carries a WORD and never a number, in every state including
      // after the meter is fitted — the meter reading lands in the tile,
      // where the student can hold it against their own working, and putting
      // it on the arrow would let them read the answer off the picture.
      arrow(ctx, insX, ely - 26, -58, "#FFC53D", C_MUSCLE);
      arrow(ctx, handX + 46, ely + 30, 62, "#8FB7FF",
            num(weight(), 0, C_LOAD));

      // The two distances, drawn as dimension lines in each one's own colour
      // so the muscle's short reach and the load's long one are one glance
      // apart. These exist only on the canvas, which is why the aria-label
      // has to carry both numbers.
      function dim(x1, x2, y, colour, label) {
        ctx.strokeStyle = colour;
        ctx.lineWidth = 2;
        ctx.beginPath();
        ctx.moveTo(x1, y - 8); ctx.lineTo(x1, y + 8);
        ctx.moveTo(x2, y - 8); ctx.lineTo(x2, y + 8);
        ctx.moveTo(x1, y); ctx.lineTo(x2, y);
        ctx.stroke();
        ctx.fillStyle = colour;
        ctx.font = '500 15px "DM Mono", ui-monospace, monospace';
        ctx.textAlign = "center";
        ctx.fillText(label, (x1 + x2) / 2, y - 14);
      }
      dim(elx, insX, ely + 92, "#FFC53D",
          num(state.ins, dp.ins) + " cm");
      dim(elx, handX, ely + 132, "#8FB7FF",
          num(state.hand, dp.hand) + " cm");

      ctx.fillStyle = "#C6B9A7";
      ctx.font = '500 14px "DM Mono", ui-monospace, monospace';
      ctx.textAlign = "left";
      ctx.fillText(C_TITLE, 30, 34);

      if (canvas.setAttribute) { canvas.setAttribute("aria-label", altText()); }
    }

    function repaint() {
      each(values, function (p) {
        var key = p.getAttribute("data-lever-value");
        p.textContent = num(state[key], dp[key],
                            p.getAttribute("data-format"));
      });
      each(outs, function (p) {
        var key = p.getAttribute("data-lever-out");
        var fmt = p.getAttribute("data-format");
        if (key === "force") {
          p.textContent = meterShown ? num(muscleForce(), 0, fmt) : UNMEASURED;
        } else if (key === "weight") {
          p.textContent = num(weight(), 0, fmt);
        } else {
          p.textContent = num(state[key], dp[key], fmt);
        }
      });
      each(tabs, function (b) {
        var key = b.getAttribute("data-lever-tab");
        b.setAttribute("aria-pressed",
          parseFloat(b.getAttribute("data-value")) === state[key]
            ? "true" : "false");
      });
      if (meterBtn) {
        meterBtn.textContent = meterShown ? M_DONE : M_LABEL;
        if (meterShown) { meterBtn.setAttribute("disabled", ""); }
      }
      if (note) { note.textContent = meterShown ? M_NOTE_DONE : M_NOTE; }
      setCount(sec, meterShown ? 1 : 0);
      draw();
      // ⚖️ A SET AND A FLAG, both required. Two DIFFERENT controls moved says
      // the student explored the trade; the meter says they committed to an
      // answer first and then checked it. Either alone is half the block.
      markStage(sec,
        Object.keys(touched).length >= DONE_AT && meterShown);
      // The steps block downstream is built out of this rig's live state, so
      // it is told rather than left to poll. `bubbles` so a listener on the
      // document catches it wherever the two blocks sit.
      if (wrap.dispatchEvent && window.CustomEvent) {
        wrap.dispatchEvent(new window.CustomEvent("ks3:lever", {
          bubbles: true,
          detail: {
            rig: wrap.getAttribute("data-rig"),
            load: state.load, ins: state.ins, hand: state.hand,
            g: G, dp: dp, weight: weight(), force: muscleForce()
          }
        }));
      }
    }

    each(inputs, function (input) {
      input.addEventListener("input", function () {
        var key = input.getAttribute("data-lever-input");
        state[key] = parseFloat(input.value);
        touched[key] = true;
        repaint();
      });
    });
    each(tabs, function (b) {
      b.addEventListener("click", function () {
        var key = b.getAttribute("data-lever-tab");
        state[key] = parseFloat(b.getAttribute("data-value"));
        touched[key] = true;
        repaint();
      });
    });
    if (meterBtn) {
      // One-way. What a student found out by fitting the meter cannot be
      // un-found by pressing it again, and re-hiding the reading would offer
      // a way to pretend the check never happened.
      meterBtn.addEventListener("click", function () {
        if (meterShown) { return; }
        meterShown = true;
        repaint();
      });
    }

    repaint();
    wireBenchGate(sec);
  }


/* WIRE: no new line in wireInstruments(). `wireTriangle(root)` is already
   called there (beside `wireCoverBar(root)`); REPLACE the existing
   `wireTriangle` with the one below. `wireCoverBar` is not touched, which is
   why c2-06's bar keeps its own contract. */

  /* ── cover-triangle · TRIANGLE variant (b1-02 #s-formula, b2-04's rule) ──

     ⚖️ TWO INTERACTION CONTRACTS, AND THE PAYLOAD PICKS ONE.

       TOGGLE (b1-02, the default and today's behaviour) — pressing the
       covered cell again UNCOVERS it. Right for a triangle being explored:
       a student wants to see the whole relationship back.

       RADIO (b2-04, `data-cover-mode="radio"`) — one cell is always covered
       and pressing the covered one changes nothing. Right for a block whose
       whole demand is "cover the one you want": an uncovered triangle asks
       nothing, and this lesson's every question solves for the same unknown,
       so it opens with that one already covered.

     A triangle with no `data-cover-mode` keeps the toggle exactly as it is
     today, which is the b1-02 guarantee.

     ⚠️ EMIT-BOTH-SHOW-ONE, for the results as well as the notes. Every
     arrangement and every sentence is already in the document and this
     function only swaps which pair is not hidden. Nothing is assembled from
     an attribute, so `÷`, `×` and the em dashes survive — the failure mode
     the bar variant's `textContent` route cannot rule out.

     ⚖️ NOTHING ANIMATES and nothing counts, so `prefers-reduced-motion` has
     nothing to degrade here: the cover's own 0.16s opacity fade is a CSS
     transition and the stylesheet's standing reduced-motion block already
     covers it. The reduced-motion experience is the complete one.

     ⚠️ NOT A RAIL STOP. There is no `markStage` call in this function and
     there must not be one: MRB-208 has the rail carrying only sections that
     require the student to do something, and this block is read. */
  function wireTriangle(root) {
    each(root.querySelectorAll("[data-triangle]"), function (tri) {
      var btns = toArray(tri.querySelectorAll(".ks3-tri-btn"));
      var notes = toArray(tri.querySelectorAll(".ks3-tri-note"));
      var results = toArray(tri.querySelectorAll(".ks3-tri-result"));
      var radio = tri.getAttribute("data-cover-mode") === "radio";

      function show(key) {
        tri.setAttribute("data-covered", key);
        each(btns, function (x) {
          x.setAttribute("aria-pressed",
            x.getAttribute("data-cover") === key ? "true" : "false");
        });
        each(notes, function (n) {
          setHidden(n, n.getAttribute("data-note") !== key);
        });
        each(results, function (r) {
          setHidden(r, r.getAttribute("data-result") !== key);
        });
      }

      function clear() {
        tri.removeAttribute("data-covered");
        each(btns, function (x) { x.setAttribute("aria-pressed", "false"); });
        each(notes, function (n) { setHidden(n, true); });
        each(results, function (r) { setHidden(r, true); });
      }

      each(btns, function (b) {
        b.addEventListener("click", function () {
          var key = b.getAttribute("data-cover");
          // The radio never uncovers. Pressing the covered cell is a no-op
          // rather than a state change, which is what keeps the figure and
          // the reading beside it always agreeing.
          if (!radio && tri.getAttribute("data-covered") === key) {
            clear();
            return;
          }
          show(key);
        });
      });
    });
  }


/* WIRE: each(root.querySelectorAll("[data-lstepblock]"), wireLeverSteps);
   — add to wireInstruments(), in the B2 group AFTER wireArmLever, so the rig
   has painted once and dispatched its first `ks3:lever` before this block
   subscribes. Uses each / toArray / setHidden / markStage, all already in
   scope. */

  /* ═══════════════════════════════════════════════════════════════
     ── lever-steps (b2-04 #s-build) — MRB-204 step 4 ──

     Three commitments — the rule, the insertion, and a number with a unit
     — then the worked version of the STUDENT'S OWN rig beside what they
     wrote.

     ⚖️ IT IS THE SAME PROBLEM AS THE BENCH, AND IT SAYS SO IN NUMBERS.
     The heading, the second ladder's three options, all four reveal steps
     and the closing line are templates over the rig's live state, refilled
     whenever a control up there moves. That is the whole difference from
     c2-06's `fifa-pick`, whose eight strings are static, and it is why the
     rig broadcasts `ks3:lever` rather than this block polling for it.

     ⚠️ THE TEMPLATES ARE READ OFF `data-template`, NEVER REBUILT. Each
     option button and each step line carries the authored string it came
     from, so there is exactly one copy of every sentence on this page and
     it is the one the build rendered. Nothing here composes prose.

     ⊕ CORRECTION — THE RAIL STOP DEMANDS SOMETHING. Design ticks this
     stage on `buildOpen`, i.e. on pressing "Show the four steps", so a
     student who committed to nothing could tick it with one tap. MRB-208
     has a rail stop requiring the student to do something, so it ticks on
     the three commitments instead: formula picked, insertion picked, and a
     non-empty answer WITH a unit. Strictly earlier than the button, which
     needs the same three — nothing gets harder, the stop just stops being
     reachable by pressing one thing.

     ⚖️ THE UNIT IS ITS OWN COMMITMENT. "160" is not an answer to a
     question about force. The placeholder option carries an empty value,
     so `unit.value` is falsy until a real unit is chosen.

     ⚖️ NOTHING ANIMATES and nothing counts, so `prefers-reduced-motion`
     has nothing to degrade here and the reduced-motion experience is the
     complete one.
     ═══════════════════════════════════════════════════════════════ */
  function wireLeverSteps(sec) {
    var wrap = sec.querySelector("[data-lstep]");
    if (!wrap) { return; }

    var RIG = wrap.getAttribute("data-rig") || "";
    var HEAD = wrap.getAttribute("data-head") || "";
    var TPL = wrap.getAttribute("data-close") || "";
    var BLANK = wrap.getAttribute("data-blank") || "—";
    var FMT = wrap.getAttribute("data-progress") || "";
    var DONE = wrap.getAttribute("data-done-label") || "";
    var TOTAL = parseInt(wrap.getAttribute("data-total"), 10) || 3;

    var opts = toArray(wrap.querySelectorAll(".ks3-lstep-opt"));
    var lines = toArray(wrap.querySelectorAll("[data-template]"));
    var ans = wrap.querySelector("[data-lstep-ans]");
    var unit = wrap.querySelector("[data-lstep-unit]");
    var btn = wrap.querySelector("[data-lstep-open]");
    var progress = wrap.querySelector("[data-lstep-progress]");
    var reveal = wrap.querySelector("[data-reveal]");
    var closeEl = wrap.querySelector("[data-lstep-close]");
    /* The shell emits the block's <h2> before any instrument renderer runs,
       so the build fills it through `_lever_steps_heading` and this repaints
       the same element. It is the ONLY <h2> inside this section — the reveal
       head, the panel labels and the questions are all paragraphs — which is
       what makes the plain selector safe. */
    var head = sec.querySelector("h2");

    var picked = {};
    var open = false;
    var subs = {};

    function fill(s) {
      var out = s || "";
      for (var k in subs) {
        if (Object.prototype.hasOwnProperty.call(subs, k)) {
          out = out.split(k).join(subs[k]);
        }
      }
      return out;
    }

    function pad(v, places) { return Number(v).toFixed(places); }

    /* The rig's state, turned into the nine substitutions every template on
       this block is written against. Identical composition to
       `_lever_steps_rig` in build_ks3.py, which renders the resting page.

       ⚠️ Two decimal places on the distances and the turning effect, none on
       the weight or the force. `0.04` and `0.32` are the metre conversions a
       student writes down; a weight and a force are whole newtons here. */
    function adopt(d) {
      var dM = d.ins / 100, dL = d.hand / 100;
      subs = {
        "{load}": pad(d.load, d.dp.load),
        "{ins}": pad(d.ins, d.dp.ins),
        "{hand}": pad(d.hand, d.dp.hand),
        "{W}": pad(d.weight, 0),
        "{dM}": pad(dM, 2),
        "{dL}": pad(dL, 2),
        "{TE}": pad(d.weight * dL, 2),
        "{F}": pad(d.force, 0),
        "{ratio}": pad(d.hand / d.ins, 1)
      };
    }

    function committed() {
      var n = 0;
      if (picked["0"] !== undefined) { n += 1; }
      if (picked["1"] !== undefined) { n += 1; }
      if (ans && ans.value.trim() && unit && unit.value) { n += 1; }
      return n;
    }

    function repaintText() {
      if (head && HEAD) { head.textContent = fill(HEAD); }
      each(lines, function (el) {
        el.textContent = fill(el.getAttribute("data-template"));
      });
      if (open && closeEl && TPL) {
        closeEl.textContent = fill(TPL)
          .split("{answer}").join(ans && ans.value.trim() ? ans.value.trim() : BLANK)
          .split("{unit}").join(unit && unit.value ? unit.value : "");
      }
    }

    function refresh() {
      var n = committed();
      if (progress) {
        progress.textContent = open ? DONE : FMT.split("{n}").join(String(n));
      }
      if (btn) {
        if (open || n < TOTAL) { btn.setAttribute("disabled", ""); }
        else { btn.removeAttribute("disabled"); }
      }
      // ⊕ The corrected predicate. Three commitments, not `buildOpen`.
      markStage(sec, n >= TOTAL);
    }

    each(opts, function (b) {
      b.addEventListener("click", function () {
        if (open) { return; }
        var group = b.getAttribute("data-group");
        picked[group] = b.getAttribute("data-i");
        each(opts, function (x) {
          if (x.getAttribute("data-group") !== group) { return; }
          x.setAttribute("aria-pressed",
            x.getAttribute("data-i") === picked[group] ? "true" : "false");
        });
        refresh();
      });
    });
    each([ans, unit], function (el) {
      if (!el) { return; }
      each(["input", "change"], function (evt) {
        el.addEventListener(evt, refresh);
      });
    });
    if (btn) {
      btn.addEventListener("click", function () {
        if (open || committed() < TOTAL) { return; }
        open = true;
        // Everything locks. The model is on screen, so a changed pick would
        // be choosing after reading the answer.
        each(opts, function (x) { x.setAttribute("disabled", ""); });
        if (ans) { ans.setAttribute("disabled", ""); }
        if (unit) { unit.setAttribute("disabled", ""); }
        setHidden(reveal, false);
        repaintText();
        refresh();
      });
    }

    /* ⚠️ SEEDED FROM THE RIG'S OWN ATTRIBUTES, NOT FROM ITS FIRST BROADCAST.
       `wireArmLever` paints once at construction and dispatches `ks3:lever`
       there, and it is wired BEFORE this block — so the first event has
       already gone by the time this function runs. Subscribing alone left
       `subs` empty until a student happened to move a control, and the
       closing line then rendered a literal `{F}`.

       Found by `lsteps-opened`'s own `/[{}]/` check in a real browser, which
       is exactly what that assertion is for: nothing about this is visible
       from reading either file, because both are individually correct.

       Reading the rig's build-time attributes rather than re-ordering the two
       wire calls is the fix that survives: a future instrument wired between
       them, or a rig that moves further down the page, would break the
       ordering fix and not this one. */
    function seed() {
      var rig = document.querySelector(
        RIG ? '[data-lever][data-rig="' + RIG + '"]' : "[data-lever]");
      if (!rig) { return; }
      var load = parseFloat(rig.getAttribute("data-load"));
      var ins = parseFloat(rig.getAttribute("data-ins"));
      var hand = parseFloat(rig.getAttribute("data-hand"));
      var g = parseFloat(rig.getAttribute("data-g"));
      if (isNaN(load) || isNaN(ins) || isNaN(hand) || isNaN(g) || !ins) {
        return;
      }
      adopt({
        load: load, ins: ins, hand: hand, g: g,
        dp: {
          load: parseInt(rig.getAttribute("data-dp-load"), 10) || 0,
          ins: parseInt(rig.getAttribute("data-dp-ins"), 10) || 0,
          hand: parseInt(rig.getAttribute("data-dp-hand"), 10) || 0
        },
        weight: load * g,
        force: (load * g * (hand / 100)) / (ins / 100)
      });
    }

    /* The rig broadcasts; this listens. `document` rather than the rig
       element, because the two blocks are siblings far apart in the document
       and the event bubbles — and because a page where the rig is missing
       must still render this block's resting state rather than throwing. */
    document.addEventListener("ks3:lever", function (ev) {
      if (!ev.detail || (RIG && ev.detail.rig !== RIG)) { return; }
      adopt(ev.detail);
      repaintText();
    });

    seed();
    refresh();
  }


/* WIRE: each(root.querySelectorAll("[data-metersblock]"), wireMeterCompare);
   — add to wireInstruments(), in the B2 group. Uses each / toArray /
   setHidden / setCount / markStage, all already in scope. */

  /* ═══════════════════════════════════════════════════════════════
     ── meter-compare (b2-04 #s-meters) — measured, not guessed ──

     Rank three muscle groups, then read what a force meter actually says
     about each of them: three readings and their mean.

     ⚖️ ONE COMMITMENT, ALL THREE CARDS. `job-sort` and `verdict-cards`
     reveal per item, the instant that item is decided, and that sequence
     is the pedagogy in both. It cannot be that here: the commitment is
     about the ORDER of the three groups, and revealing one card would
     give away part of the answer to the question still being asked.

     ⚠️ R3 — NOTHING MARKS. All three orderings render identically and all
     three open the same cards. There is no `data-correct` in this
     instrument and there must not be: `answer_index` is checked against
     the rows' own means at build time and never reaches the page. The
     choice also stays changeable — a student who reads the means and
     wants to change their mind is the block working, not a leak.

     ⚖️ THE MEAN IS THE SECOND LESSON, and it is why the readings are in
     the document rather than composed here: 312, 298 and 305 disagree,
     and the closing band says in words that one pull would have told you
     almost nothing. Nothing in this function builds a number.

     ⚖️ NOTHING ANIMATES and nothing counts, so `prefers-reduced-motion`
     has nothing to degrade and the reduced-motion experience is the
     complete one.
     ═══════════════════════════════════════════════════════════════ */
  function wireMeterCompare(sec) {
    var wrap = sec.querySelector("[data-meters]");
    if (!wrap) { return; }
    var opts = toArray(wrap.querySelectorAll(".ks3-option"));
    var panel = wrap.querySelector("[data-reveal]");
    if (!opts.length || !panel) { return; }

    each(opts, function (btn) {
      btn.addEventListener("click", function () {
        var i = btn.getAttribute("data-i");
        each(opts, function (b) {
          b.setAttribute("aria-pressed",
            b.getAttribute("data-i") === i ? "true" : "false");
        });
        if (panel.hasAttribute("hidden")) {
          setHidden(panel, false);
          // Announced for screen-reader users, who would otherwise get no
          // signal that three cards of data appeared below the buttons.
          panel.setAttribute("role", "status");
        }
        // The block-head readout is a two-state label here ("Not ranked yet"
        // → "Ranked"), not a count — there is one thing to report and it is
        // a boolean. `setCount` carries that shape.
        setCount(sec, 1);
        markStage(sec, true);   // `ranked`
      });
    });
  }
/* ═══ END B2 ═══ */

/* ═══ BEGIN B3 ═══ */
/* WIRE: each(root.querySelectorAll("[data-plateblock]"), wireBandCommit);
   — add to wireInstruments(), in a new B3 group. Uses each / toArray /
   setHidden / setCount / markStage, all already in scope. */

  /* ═══════════════════════════════════════════════════════════════
     ── band-commit (b3-01 #s-plate) — commit all seven, then open ──

     Seven nutrients, three amount bands, one reveal that is locked until
     every one of the seven has been placed.

     ⚖️ THE LOCK IS THE LESSON. The block's own lede says it: *a guess you
     did not make cannot be wrong, and a guess that is never wrong teaches
     you nothing.* Opening a row at a time — which is what `job-sort` does
     and what this looks like from a distance — would let a student read
     row one's answer before committing on row two, and the argument of
     the block is that the SPREAD is the surprise. Nobody is surprised by
     a spread they were shown a seventh at a time.

     ⚖️ THE ALL-SAME BRANCH IS THE POINT OF THE VERDICT. A student who
     puts all seven in one band is told so, in their own answer. That is
     the only place in the lesson where "balanced means equal amounts" is
     named back rather than argued against in the abstract, and it is why
     the branch is chosen here before the score is: a 0-of-7 all-same day
     and a 0-of-7 scattered day are different mistakes and get different
     sentences.

     ⚠️ R3 — NOTHING MARKS A CONTROL. The band buttons are not
     `.ks3-option`, they never gain a correct or wrong class, and once the
     answers are open the chosen one keeps exactly the treatment it had
     while the other two dim. What changes is the ROW and the words in its
     why panel. There is no `--ks3-ok`, no green, no drawn ✓ and no ✕
     anywhere in this instrument, and nothing here may grow one.

     Emit-both-show-one: every why panel, both band verdicts per row and
     all three closing branches are already in the document. This function
     only ever changes which of them is hidden — no authored sentence is
     assembled here, so the em dashes and the right single quotes survive.

     ⚖️ NOTHING ANIMATES and nothing runs on a clock, so
     `prefers-reduced-motion` has nothing to degrade and the reduced-motion
     experience is the complete one.
     ═══════════════════════════════════════════════════════════════ */
  function wireBandCommit(sec) {
    var wrap = sec.querySelector("[data-plate]");
    if (!wrap) { return; }
    var rows = toArray(wrap.querySelectorAll(".ks3-plate-row"));
    var openBtn = wrap.querySelector("[data-plate-open]");
    var countEl = wrap.querySelector("[data-plate-count]");
    var verdict = wrap.querySelector("[data-plate-verdict]");
    var total = parseInt(wrap.getAttribute("data-total"), 10) || rows.length;
    if (!rows.length || !openBtn || !verdict) { return; }

    var picks = {};       // row index -> band id
    var opened = false;

    function committed() {
      var n = 0, k;
      for (k in picks) {
        if (Object.prototype.hasOwnProperty.call(picks, k)) { n += 1; }
      }
      return n;
    }

    /* The block-head readout ("3 of 7 set") and the foot readout ("3 of 7
       committed") are two different sentences about the same number, and
       Design draws both. `setCount` owns the first; the second has its own
       format because it also has a bespoke DONE string ("Opened") that the
       count shape has no slot for. */
    function paintCount() {
      var n = committed();
      setCount(sec, n);
      if (!countEl) { return; }
      if (opened) {
        countEl.textContent = countEl.getAttribute("data-done") || "";
        return;
      }
      countEl.textContent = (countEl.getAttribute("data-format") || "")
        .split("{n}").join(String(n))
        .split("{total}").join(String(total));
    }

    function open() {
      if (opened || committed() < total) { return; }
      opened = true;
      var right = 0, chosen = {}, kinds = 0, k;

      each(rows, function (row, i) {
        var want = row.getAttribute("data-answer");
        var got = picks[i];
        var hit = got === want;
        if (hit) { right += 1; }
        chosen[got] = true;
        row.setAttribute("data-state", hit ? "hit" : "miss");
        each(row.querySelectorAll("[data-real]"), function (span) {
          setHidden(span, span.getAttribute("data-real") !== (hit ? "hit" : "miss"));
        });
        setHidden(row.querySelector("[data-why]"), false);
        each(row.querySelectorAll(".ks3-plate-band"), function (b) {
          b.disabled = true;
        });
      });

      for (k in chosen) {
        if (Object.prototype.hasOwnProperty.call(chosen, k)) { kinds += 1; }
      }

      var head = verdict.querySelector("[data-vhead]");
      if (head) {
        head.textContent = (head.getAttribute("data-format") || "")
          .split("{n}").join(String(right))
          .split("{total}").join(String(total));
      }
      /* ⚖️ ORDER MATTERS. All-same is tested FIRST and independently of the
         score, because it is a different mistake from a low score and gets a
         different sentence. A student who put all seven in "tens of grams"
         happens to score 3, which would otherwise fall through to the general
         branch and never hear the one thing this block exists to say. */
      var branch = kinds === 1 ? "all_same" : (right >= total - 1 ? "close" : "spread");
      each(verdict.querySelectorAll("[data-v]"), function (p) {
        setHidden(p, p.getAttribute("data-v") !== branch);
      });

      setHidden(verdict, false);
      openBtn.disabled = true;
      openBtn.setAttribute("aria-expanded", "true");
      paintCount();
      markStage(sec, true);      // `all_seven_committed_and_opened`
    }

    each(rows, function (row, i) {
      each(row.querySelectorAll(".ks3-plate-band"), function (btn) {
        btn.addEventListener("click", function () {
          if (opened) { return; }
          var id = btn.getAttribute("data-band");
          picks[i] = id;
          each(row.querySelectorAll(".ks3-plate-band"), function (b) {
            b.setAttribute("aria-pressed",
              b.getAttribute("data-band") === id ? "true" : "false");
          });
          paintCount();
          openBtn.disabled = committed() < total;
        });
      });
    });

    openBtn.addEventListener("click", open);
    paintCount();
  }


/* WIRE: each(root.querySelectorAll("[data-clinicblock]"), wireClinicCases);
   — add to wireInstruments(), in a new B3 group. Uses each / toArray /
   setHidden / setCount / markStage, all already in scope. */

  /* ── clinic-cases (b3-04 #s-cases) ──
     Five clinics. Tick every imbalance that applies, then open the
     diagnosis. Two of the five have two answers.

     ⚖️ MULTI-SELECT, NOT A PICKER, and every line below exists to keep it
     that way. A pick toggles rather than replacing the others, the reveal
     button unlocks on ONE tick rather than on a complete answer (a student
     who thinks one applies must be allowed to commit to that — being
     unwilling to tick two is the error the block is built to show, and it
     cannot be shown if the page refuses to accept the one-tick answer),
     and the picks freeze the moment the diagnosis opens.

     ⚠️ NOTHING MARKS. There is no `data-correct` in this instrument and
     there must not be. The correct kinds are not in the document as data
     at all — the answer is prose, in `.ks3-clinic-answer`, revealed
     identically to every student. The verdict LABEL is a fact about the
     case ("Two imbalances apply here"), authored per case, and it is not
     computed from what the student ticked; MRB-196 R10 replaced that
     computation with the self-check below.

     ⚖️ THE STAGE IS EVERY CLINIC DIAGNOSED, not every clinic looked at.
     Design's own predicate is the same and it is right: one clinic is one
     judgement, and the lesson's argument is the five held against each
     other — clinic 4 is a deficiency in a fed child, clinic 5 is not a
     diet problem at all, and neither means anything alone.

     ⚖️ NOTHING ANIMATES and nothing counts down, so `prefers-reduced-motion`
     has nothing to degrade here: the reduced-motion experience is the
     complete one. */
  function wireClinicCases(sec) {
    var wrap = sec.querySelector("[data-clinic]");
    if (!wrap) { return; }
    var tabs = toArray(wrap.querySelectorAll(".ks3-clinic-tab"));
    var panels = toArray(wrap.querySelectorAll(".ks3-clinic-panel"));
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

    function diagnosed() {
      var n = 0;
      each(panels, function (p) {
        if (p.getAttribute("data-open") === "1") { n += 1; }
      });
      return n;
    }

    function refreshStage() {
      var n = diagnosed();
      setCount(sec, n);
      var all = n >= panels.length;
      markStage(sec, all);
      /* The self-check has nothing to compare against until every answer is
         showing, so it does not exist in the layout until then. R10: the
         page asks, the student answers, and nothing is graded. */
      if (all && selfcheck) {
        setHidden(selfcheck, false);
        selfcheck.setAttribute("role", "status");
      }
    }

    each(panels, function (panel) {
      var picks = toArray(panel.querySelectorAll(".ks3-clinic-pick"));
      var btn = panel.querySelector("[data-clinic-reveal]");
      var count = panel.querySelector("[data-clinic-count]");
      var verdict = panel.querySelector("[data-reveal]");

      function ticked() {
        var n = 0;
        each(picks, function (p) {
          if (p.getAttribute("aria-pressed") === "true") { n += 1; }
        });
        return n;
      }

      function repaint() {
        var open = panel.getAttribute("data-open") === "1";
        var n = ticked();
        if (count) {
          /* Three authored states, all three in the document as attributes
             and none of them assembled here from words — only the number is
             substituted. */
          count.textContent = open
            ? (count.getAttribute("data-done") || "")
            : (n
               ? String(count.getAttribute("data-some") || "")
                   .split("{n}").join(String(n))
               : (count.getAttribute("data-none") || ""));
        }
        if (btn) {
          /* One tick is enough to commit. See the header: refusing the
             one-tick answer would hide the mistake being taught. */
          if (!n || open) { btn.setAttribute("disabled", ""); }
          else { btn.removeAttribute("disabled"); }
        }
      }

      each(picks, function (p) {
        p.addEventListener("click", function () {
          if (panel.getAttribute("data-open") === "1") { return; }
          /* TOGGLE, never replace. This is the one control in the key stage
             where more than one may be pressed at once. */
          p.setAttribute("aria-pressed",
            p.getAttribute("aria-pressed") === "true" ? "false" : "true");
          repaint();
        });
      });

      if (btn) {
        btn.addEventListener("click", function () {
          if (panel.getAttribute("data-open") === "1" || !ticked()) { return; }
          panel.setAttribute("data-open", "1");
          setHidden(verdict, false);
          /* ⚠️ NO SECOND `role="status"` HERE, deliberately. `keyed-commit`
             and `meter-compare` announce their revealed panel because they
             have no other live element; this panel has one — the count —
             and it goes to "Diagnosed" in the same turn. Announcing both
             reads the whole verdict over the top of the state change. One
             live region per panel; the count is it. */
          each(picks, function (p) { p.setAttribute("disabled", ""); });
          repaint();
          refreshStage();
        });
      }

      repaint();
    });

    refreshStage();
  }


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


/* WIRE: each(root.querySelectorAll("[data-foldblock]"), wireFoldBuilder);
   — add to wireInstruments(), in a new B3 group. Uses each / toArray /
   setHidden / setCount / markStage, all already in scope. */

  /* ═══════════════════════════════════════════════════════════════
     ── fold-builder (b3-07 #s-fold) — build the surface up ──

     Three toggles, three multipliers, one area. Start at half a square
     metre of plain tube and end at about thirty, with the length written
     beside it never moving.

     ⚖️ ONLY THE NUMBERS ARE BUILT HERE. All four notes are in the
     document — one per COUNT of levels, not one per level — and this
     function swaps which is shown. Every sentence a student reads about
     the folding was authored in the lesson record, so the em dashes and
     the `<em>` survive and nothing science-bearing is assembled from an
     attribute. What IS assembled is an area and a multiple, which is
     what an arithmetic readout is for.

     ⚠️ THE NUMBER FORMAT IS DUPLICATED, DELIBERATELY. `areaText` and
     `multText` below are the same rule as `_fold_area_text` /
     `_fold_multiple_text` in build_ks3.py, which fill the RESTING
     render. Two copies of four lines buys HTML that already says
     "0.50 m²" before any script runs — the same trade `head_counter`'s
     `start` makes one level up. `Math.round` and Python's `int(v + 0.5)`
     were matched on purpose; `round()` would have rounded half to even
     and disagreed at exactly 10.5.

     ⚖️ THE STOP LATCHES, and Design's own predicate does not. Design
     recomputes `s.on.folds && s.on.villi && s.on.microvilli` every
     render, so a student who builds all three levels and then switches
     one back off to look at it again has their rail stop taken away
     from them. MRB-208 ruled the rail records PARTICIPATION: a stop
     ticks when the activity is finished, and nothing un-finishes it.
     So `markStage` is only ever called with `true` here. The BAR and
     the NOTE still follow the live state, because those are claims
     about the model currently on screen and would be false if they
     latched.

     ⚖️ NOTHING TICKS AND NOTHING COUNTS DOWN. NOTES-B3 §6 is explicit
     that `enzyme-run` is the only instrument in the unit with a timer;
     the one animation here is a CSS width transition, which the
     stylesheet degrades under `prefers-reduced-motion` itself. There is
     no rate for this function to scale, and the reduced-motion
     experience is the complete one. (Same standing as `meter-compare`.)
     ═══════════════════════════════════════════════════════════════ */
  function wireFoldBuilder(sec) {
    var wrap = sec.querySelector("[data-fold]");
    if (!wrap) { return; }
    var levels = toArray(wrap.querySelectorAll("[data-level]"));
    if (!levels.length) { return; }

    var areaEl = wrap.querySelector("[data-fold-area]");
    var barEl = wrap.querySelector("[data-fold-bar]");
    var multEl = wrap.querySelector("[data-fold-multiple]");
    var notes = toArray(wrap.querySelectorAll("[data-note]"));

    var base = parseFloat(wrap.getAttribute("data-base"));
    if (!base || base <= 0) { return; }
    var areaFmt = wrap.getAttribute("data-area-format") || "{a}";
    var multFmt = wrap.getAttribute("data-multiple-format") || "{x}";

    function factorOf(li) {
      var f = parseFloat(li.getAttribute("data-factor"));
      return f > 0 ? f : 1;
    }

    // The full stack, computed once: the bar is a fraction of what the
    // finished model comes to, not of a magic number.
    var most = base;
    each(levels, function (li) { most *= factorOf(li); });

    function areaText(v) {
      if (v < 1) { return v.toFixed(2); }
      if (v < 10) { return v.toFixed(1); }
      return String(Math.round(v));
    }
    function multText(r) {
      return r < 10 ? r.toFixed(1) : String(Math.round(r));
    }

    function refresh() {
      var area = base, on = 0;
      each(levels, function (li) {
        if (li.getAttribute("data-on") === "1") {
          area *= factorOf(li);
          on += 1;
        }
      });
      if (areaEl) {
        areaEl.textContent = areaFmt.split("{a}").join(areaText(area));
      }
      if (multEl) {
        multEl.textContent = multFmt.split("{x}").join(multText(area / base));
      }
      if (barEl) {
        // A floor of 2%, so the plain tube is a visible sliver rather than
        // an empty track that reads as "no data" instead of "half a square
        // metre".
        barEl.style.width = Math.max(2, (area / most) * 100).toFixed(1) + "%";
        barEl.setAttribute("data-full", on === levels.length ? "1" : "0");
      }
      each(notes, function (p) {
        setHidden(p, p.getAttribute("data-note") !== String(on));
      });
      setCount(sec, on);
      if (on === levels.length) { markStage(sec, true); }
    }

    each(levels, function (li) {
      var btn = li.querySelector("[data-fold-toggle]");
      if (!btn) { return; }
      btn.addEventListener("click", function () {
        var on = li.getAttribute("data-on") !== "1";
        li.setAttribute("data-on", on ? "1" : "0");
        btn.setAttribute("aria-pressed", on ? "true" : "false");
        // Both faces were finished at build time — "Add this level" and
        // "On · ×7" — so nothing here composes a label out of a factor.
        btn.textContent = btn.getAttribute(on ? "data-label-on"
                                              : "data-label-off") || "";
        refresh();
      });
    });

    // Opens on the plain tube: 0 of 3, 0.50 m², ×1.0, note zero. That is
    // what the HTML already says, so this call changes nothing on load — it
    // is here so there is exactly one place the readout is computed.
    refresh();
  }


/* WIRE: each(root.querySelectorAll("[data-gutblock]"), wireGutJourney);
   — add to wireInstruments(), in the B3 group. Uses each / toArray /
   setHidden / setCount / markStage, all already in scope. */

  /* ── gut-journey (b3-05 #s-journey) ──
     Follow one meal through seven stops, with a time chart under them
     that contradicts the intuition the lesson opens with.

     ⚖️ NOTHING HERE BUILDS A NUMBER OR A WIDTH. Every bar width is inline
     in the document, computed in `r_gut_journey` from the same `hours`
     the printed figure beside it is authored from. This function moves
     the HIGHLIGHT — which row is lit, which panel is shown — and nothing
     else. A width set here would be a second source for one quantity,
     and the two would eventually stop agreeing.

     ⚖️ THE OPEN STOP IS SEEDED AS VISITED, and that is a real difference
     from the c1-02 precedent rather than a copy of Design's defect.
     c1-02's bench counted the state it was ABOUT to show while the whole
     instrument was still behind a commit gate, so the readout claimed
     something the student could not yet have seen. There is no gate here:
     stop one is on screen, complete, from first paint. "1 of 7 stops
     visited" is therefore true at rest — and the stage still needs six
     more taps, so nothing ticks on load (MRB-208).

     ⚖️ EVERY STOP, not five of seven. The stage is the whole journey
     because the journey is the block's argument: a student who stops at
     the small intestine has met the organ that does the work and not the
     two that follow it, and egestion-is-not-excretion is on the last one.

     ⚖️ NOTHING ANIMATES and nothing counts, so `prefers-reduced-motion`
     has nothing to degrade here — the only transition in the component is
     the highlight's colour, and the stylesheet's own reduced-motion block
     already removes it. The reduced-motion experience is the complete
     one. */
  function wireGutJourney(sec) {
    var wrap = sec.querySelector("[data-gut]");
    if (!wrap) { return; }
    var tabs = toArray(wrap.querySelectorAll(".ks3-gut-tab"));
    var panels = toArray(wrap.querySelectorAll(".ks3-gut-stop"));
    var rows = toArray(wrap.querySelectorAll(".ks3-gut-row"));
    var total = parseInt(wrap.getAttribute("data-total"), 10) || panels.length;
    if (!panels.length) { return; }

    var seen = {};

    function show(id) {
      each(tabs, function (tab) {
        tab.setAttribute("aria-pressed",
          tab.getAttribute("data-stop") === id ? "true" : "false");
      });
      each(panels, function (p) {
        setHidden(p, p.getAttribute("data-stop") !== id);
      });
      each(rows, function (r) {
        if (r.getAttribute("data-stop") === id) {
          r.setAttribute("data-lit", "1");
        } else {
          r.removeAttribute("data-lit");
        }
      });
      seen[id] = true;
      var n = 0, k;
      for (k in seen) { if (seen[k]) { n += 1; } }
      setCount(sec, n);
      markStage(sec, n >= total);
    }

    each(tabs, function (tab) {
      tab.addEventListener("click", function () {
        show(tab.getAttribute("data-stop"));
      });
    });

    /* Seed from the panel that is actually showing rather than from index
       zero, so the renderer stays free to open on a different stop without
       the count and the picture disagreeing. */
    var open = wrap.querySelector(".ks3-gut-stop:not([hidden])");
    if (open) { show(open.getAttribute("data-stop")); }
  }


/* WIRE: each(root.querySelectorAll("[data-jobswblock]"), wireJobSwitch);
   — add to wireInstruments(), in the B3 group, after wireFoldBuilder. Uses
   each / toArray / setHidden / setCount / markStage, all already in scope. */

  /* ═══════════════════════════════════════════════════════════════
     ── job-switch (b3-08 #s-jobs) — take one job away ──

     Five things gut bacteria do that your own cells cannot. Switch each
     off and read what the host loses; switch all five off and you have
     built the germ-free mouse from the hook.

     ⚖️ THE SUMMARY REPORTS THE PRESENT TENSE, and that is why this is
     not `system-switch`. `wireSwitch` and `wireJobSort` both count what
     has EVER been opened and fire their closing panel on that count —
     one-way, cumulative, and right for both of them. This panel says
     "You have just built the germ-free mouse", which is a claim about
     the configuration on screen: switch a job back on and the animal
     is no longer germ-free, so the panel has to go away again. A
     component that counts history cannot express a component that
     reports state.

     ⚖️ THE RAIL STOP LATCHES, and the panel does not. MRB-208 ruled the
     rail records PARTICIPATION — a stop ticks when the activity is
     finished and nothing un-finishes it — so `markStage` is only ever
     called with `true` here. Design's own `isDone` recomputes
     `JOBS.every(j => s.off[j.id])` on every render and would take a
     student's progress away for looking at a row again. The counter and
     the panel still follow the live state, because both are statements
     about what is true now.

     ⚖️ NOTHING MARKS. Five toggles, no answer, no `data-correct`. The
     block is an experiment, not a question, and a student who switches
     everything off and everything back on has done the experiment
     twice rather than got it wrong once.

     ⚖️ NOTHING ANIMATES and nothing counts down, so
     `prefers-reduced-motion` has nothing to degrade and the
     reduced-motion experience is the complete one. NOTES-B3 §6 is
     explicit that `enzyme-run` is the only instrument in this unit with
     a timer.
     ═══════════════════════════════════════════════════════════════ */
  function wireJobSwitch(sec) {
    var wrap = sec.querySelector("[data-jobsw]");
    if (!wrap) { return; }
    var jobs = toArray(wrap.querySelectorAll("[data-job]"));
    if (!jobs.length) { return; }

    var all = wrap.querySelector("[data-jobsw-all]");
    var total = parseInt(wrap.getAttribute("data-total"), 10) || jobs.length;

    function refresh() {
      var off = 0;
      each(jobs, function (job) {
        if (job.getAttribute("data-off") === "1") { off += 1; }
      });
      setCount(sec, off);
      if (all) {
        setHidden(all, off < total);
        // Announced once, for screen-reader users who would otherwise get
        // no signal that the block's conclusion had arrived below the last
        // row. On the NOTE, never on the section — a live region around the
        // whole instrument would re-read five job descriptions every time a
        // switch moved.
        if (off >= total && !all.getAttribute("role")) {
          all.setAttribute("role", "status");
        }
      }
      if (off >= total) { markStage(sec, true); }
    }

    each(jobs, function (job) {
      var btn = job.querySelector("[data-jobsw-toggle]");
      var note = job.querySelector("[data-reveal]");
      if (!btn) { return; }
      btn.addEventListener("click", function () {
        var off = job.getAttribute("data-off") !== "1";
        job.setAttribute("data-off", off ? "1" : "0");
        btn.setAttribute("aria-pressed", off ? "true" : "false");
        // Both faces were finished at build time — "Switch it off" and
        // "Switched off" — so nothing here composes a label.
        btn.textContent = btn.getAttribute(off ? "data-label-off"
                                              : "data-label-on") || "";
        if (note) {
          setHidden(note, !off);
          if (off && !note.getAttribute("role")) {
            note.setAttribute("role", "status");
          }
        }
        refresh();
      });
    });

    // Opens with every job doing its job: 0 of 5 switched off, no
    // consequences showing, no summary. That is what the HTML already says,
    // so this call changes nothing on load — it is here so there is exactly
    // one place the counter and the summary are decided.
    refresh();
  }


/* WIRE: each(root.querySelectorAll("[data-ledgerblock]"), wirePersonLedger);
   — add to wireInstruments(), in the B3 group. Uses each / toArray /
   setHidden / setCount / markStage, all already in scope. */

  /* ═══════════════════════════════════════════════════════════════
     ── person-ledger (b3-03 #s-ledger) — the person is the control ──

     Twelve foods, five eaters, one running total. Build a day, then move
     the person underneath it.

     ⚖️ CHANGING THE PERSON NEVER TOUCHES THE PLATE, and that is the
     whole instrument. The same food is a surplus for one body and a
     shortfall for another with nothing about the food having moved, and
     the match panel says so in words. A "clear on switch" would be tidier
     and would destroy the experiment, so the person tabs deliberately
     touch nothing but the requirement they are compared against.

     ⚖️ MRB-232 — B3'S SIDE OF THE SPLIT. Everything here is intake
     against requirement, in kJ. Nothing converts a unit, derives a joule
     from power and time, or explains what a joule is: that is P2's half
     of `KS3.B.NUT.02`, reached from this lesson by a `references` edge.
     A kJ↔kcal toggle added to this block later would move the seam.

     ⚠️ R3 — NOTHING MARKS. There is no `.ks3-option` in this instrument,
     no correct plate and no score. The bar's three colours are readings
     of a measurement — short, matched, over — and `--ks3-ok` is
     deliberately not one of them: green is the ladder's colour for a
     correct answer and a plate is not an answer.

     Every authored sentence is already in the document and this function
     only changes which is hidden. The three exceptions all quote a live
     number that does not exist until a plate has been built, and each is
     one authored template filled with digits — `_head_counter`'s own
     mechanism, and safe for its reason: none of them carries markup.

     ⚖️ NOTHING RUNS ON A CLOCK. The bar's width and colour move on a CSS
     transition that the stylesheet turns off under
     `prefers-reduced-motion`, and every number is in the document as
     text, so the reduced-motion experience is the complete one (R6).
     ═══════════════════════════════════════════════════════════════ */
  function wirePersonLedger(sec) {
    var wrap = sec.querySelector("[data-ledger]");
    if (!wrap) { return; }
    var bar = wrap.querySelector("[data-bar]");
    var totalEl = wrap.querySelector("[data-total]");
    var balanceEl = wrap.querySelector("[data-balance]");
    var portionEl = wrap.querySelector("[data-portions]");
    var matchEl = wrap.querySelector("[data-match]");
    var clearBtn = wrap.querySelector("[data-ledger-clear]");
    var foods = toArray(wrap.querySelectorAll(".ks3-ledger-food"));
    if (!bar || !totalEl || !balanceEl || !foods.length) { return; }

    var tolerance = (parseInt(wrap.getAttribute("data-tolerance"), 10) || 5) / 100;
    var maxPer = parseInt(wrap.getAttribute("data-max"), 10) || 6;
    var countFmt = wrap.getAttribute("data-count-format") || "×{n}";

    function group(n) { return Number(n).toLocaleString("en-GB"); }

    function fill(el, attr, values) {
      var s = el.getAttribute(attr) || "", k;
      for (k in values) {
        if (Object.prototype.hasOwnProperty.call(values, k)) {
          s = s.split("{" + k + "}").join(String(values[k]));
        }
      }
      return s;
    }

    function paint() {
      var person = wrap.getAttribute("data-person");
      var tab = wrap.querySelector(".ks3-ledger-tab[data-person='" + person + "']");
      var need = tab ? parseInt(tab.getAttribute("data-need"), 10) : 0;
      var total = 0, portions = 0;

      each(foods, function (b) {
        var n = parseInt(b.getAttribute("data-count"), 10) || 0;
        total += n * (parseInt(b.getAttribute("data-kj"), 10) || 0);
        portions += n;
        var label = b.querySelector("[data-count-label]");
        if (label) {
          label.textContent = n > 0 ? countFmt.split("{n}").join(String(n)) : "";
        }
      });

      each(wrap.querySelectorAll(".ks3-ledger-tab[data-person]"), function (b) {
        b.setAttribute("aria-pressed",
          b.getAttribute("data-person") === person ? "true" : "false");
      });
      each(wrap.querySelectorAll("[data-pname], [data-pneed], [data-pwhy]"),
        function (s) {
          var id = s.getAttribute("data-pname") || s.getAttribute("data-pneed")
            || s.getAttribute("data-pwhy");
          setHidden(s, id !== person);
        });

      var diff = total - need;
      var matched = portions > 0 && Math.abs(diff) <= need * tolerance;
      var frac = need ? total / need : 0;
      bar.style.width = Math.min(100, frac * 100).toFixed(1) + "%";
      bar.setAttribute("data-state",
        matched ? "matched" : (frac > 1 + tolerance ? "over" : "short"));

      totalEl.textContent = fill(totalEl, "data-format",
        { total: group(total), need: group(need) });

      if (!portions) {
        balanceEl.textContent = balanceEl.getAttribute("data-empty") || "";
      } else if (matched) {
        balanceEl.textContent = balanceEl.getAttribute("data-matched") || "";
      } else {
        balanceEl.textContent = fill(balanceEl,
          diff > 0 ? "data-surplus" : "data-short",
          { n: group(Math.abs(diff)) });
      }

      if (portionEl) {
        portionEl.textContent = portions
          ? fill(portionEl, "data-format",
              { n: portions, total: group(total) })
          : (portionEl.getAttribute("data-empty") || "");
      }

      if (matchEl) {
        setHidden(matchEl, !matched);
        each(matchEl.querySelectorAll("[data-mhead]"), function (p) {
          setHidden(p, p.getAttribute("data-mhead") !== person);
        });
      }

      setCount(sec, portions);
      markStage(sec, portions > 0);   // `food_on_the_plate`
    }

    each(wrap.querySelectorAll(".ks3-ledger-tab[data-person]"), function (b) {
      b.addEventListener("click", function () {
        // ⚖️ THE PLATE IS NOT TOUCHED. See the header — this is the experiment.
        wrap.setAttribute("data-person", b.getAttribute("data-person"));
        paint();
      });
    });

    each(foods, function (b) {
      b.addEventListener("click", function () {
        var n = (parseInt(b.getAttribute("data-count"), 10) || 0) + 1;
        // Design's own wrap-around: the count runs up to `max` and the next
        // tap clears that food. It is what makes one control both add and
        // remove, and the block's label says so.
        b.setAttribute("data-count", String(n > maxPer ? 0 : n));
        paint();
      });
    });

    if (clearBtn) {
      clearBtn.addEventListener("click", function () {
        each(foods, function (b) { b.setAttribute("data-count", "0"); });
        paint();
      });
    }

    paint();
  }


/* WIRE: each(root.querySelectorAll("[data-tbenchblock]"), wireTestBench);
   — add to wireInstruments(), in the B3 group. Uses each / toArray /
   setHidden / setCount / markStage, all already in scope. */

  /* ═══════════════════════════════════════════════════════════════
     ── test-bench (b3-02 #s-bench) — the prediction runs the test ──

     Five foods × four tests. Pick a pair, say what you expect, and the
     saying is what runs it: there is no separate run button, because a
     student who can see the colour first has not predicted anything.

     ⚖️ THE RUN LATCHES, AND SO DOES THE PREDICTION. Design re-reads the
     stored prediction every render, so a student who changed their answer
     after the tube had changed colour would be told "You predicted this"
     — the block would congratulate them for the thing it exists to stop.
     The first press of a combination is the one that scores it, exactly
     as c1-06's evidence bench latches its first call. Pressing again
     still MOVES the pressed state (R3 requires every option to render
     alike whichever was chosen), it simply does not rewrite history.

     ⚖️ NOTHING IS ASSEMBLED HERE. All twenty prompts, all twenty results,
     all twenty claim lines, the four methods and the nine tube-state
     names are already in the document, and this function only changes
     which is hidden. That is what keeps the em dashes, the curly quotes
     and the `<strong>` in the claim line intact — and every one of those
     sentences is the science of the lesson rather than chrome.

     ⚠️ R3 — NOTHING MARKS. The two prediction options are ordinary
     activity options: they show that they were chosen and nothing else,
     they are never disabled, and neither carries `data-correct`. The
     verdict line that follows reports whether the prediction matched the
     tube — which is a fact about the world, printed in the result panel,
     not a mark on a button.

     ⚖️ NOTHING RUNS ON A CLOCK. The tube's colour transition is a CSS
     one and `prefers-reduced-motion` turns it off in the stylesheet, so
     there is nothing to scale here and the reduced-motion experience is
     the complete one: the state line beside the tube says the colour in
     words either way (R2).
     ═══════════════════════════════════════════════════════════════ */
  function wireTestBench(sec) {
    var wrap = sec.querySelector("[data-tbench]");
    if (!wrap) { return; }
    var predictWrap = wrap.querySelector("[data-predict]");
    var opts = toArray(wrap.querySelectorAll(".ks3-option"));
    var tube = wrap.querySelector("[data-tube]");
    var state = wrap.querySelector("[data-state]");
    if (!predictWrap || !opts.length || !tube || !state) { return; }

    var target = parseInt(wrap.getAttribute("data-target"), 10) || 4;
    var ran = {};         // "food:test" -> the option index pressed FIRST
    var count = 0;

    function key() {
      return wrap.getAttribute("data-food") + ":" + wrap.getAttribute("data-test");
    }

    function paint() {
      var k = key();
      var food = wrap.getAttribute("data-food");
      var test = wrap.getAttribute("data-test");
      var testTab = wrap.querySelector(".ks3-tbench-tab[data-test='" + test + "']");
      var done = Object.prototype.hasOwnProperty.call(ran, k);
      var result = wrap.querySelector("[data-result='" + k + "']");

      each(wrap.querySelectorAll(".ks3-tbench-tab[data-food]"), function (b) {
        b.setAttribute("aria-pressed",
          b.getAttribute("data-food") === food ? "true" : "false");
      });
      each(wrap.querySelectorAll(".ks3-tbench-tab[data-test]"), function (b) {
        b.setAttribute("aria-pressed",
          b.getAttribute("data-test") === test ? "true" : "false");
      });
      each(wrap.querySelectorAll("[data-lfood]"), function (s) {
        setHidden(s, s.getAttribute("data-lfood") !== food);
      });
      each(wrap.querySelectorAll("[data-ltest]"), function (s) {
        setHidden(s, s.getAttribute("data-ltest") !== test);
      });
      each(wrap.querySelectorAll("[data-method]"), function (p) {
        setHidden(p, p.getAttribute("data-method") !== test);
      });
      each(wrap.querySelectorAll("[data-detects]"), function (p) {
        setHidden(p, p.getAttribute("data-detects") !== test);
      });
      each(wrap.querySelectorAll("[data-prompt]"), function (p) {
        setHidden(p, p.getAttribute("data-prompt") !== k);
      });
      each(wrap.querySelectorAll("[data-result]"), function (d) {
        setHidden(d, !done || d.getAttribute("data-result") !== k);
      });

      /* An unrun combination shows the reagent's UNCHANGED colour — the
         negative — because that is what is in the tube before the food goes
         in. The colours ride on the test tab for exactly this: the resting
         tube needs one before any result panel exists. */
      var colour = done && result
        ? result.getAttribute("data-colour")
        : (testTab ? testTab.getAttribute("data-neg") : "");
      if (colour) { tube.style.background = colour; }
      tube.setAttribute("data-run", done ? "1" : "0");

      // The state line: nine authored spans, one shown. Never composed.
      var outcome = done && result ? result.getAttribute("data-outcome") : "";
      var want = outcome ? test + ":" + outcome : "rest";
      each(state.querySelectorAll("[data-sname]"), function (s) {
        setHidden(s, s.getAttribute("data-sname") !== want);
      });

      // Gating by ABSENCE, as C6's bench gate does: a combination that has
      // been run has no question left to ask.
      setHidden(predictWrap, done);
      each(opts, function (b) {
        b.setAttribute("aria-pressed",
          done && String(ran[k]) === b.getAttribute("data-i") ? "true" : "false");
      });
      if (done && result) {
        /* Option 0 is "Yes — it will change colour" and option 1 is "No".
           The prediction matched if the yes/no the student pressed agrees
           with the outcome the payload records for this combination. */
        var hit = (ran[k] === 0) === (outcome === "pos");
        each(result.querySelectorAll("[data-verdict]"), function (p) {
          setHidden(p, p.getAttribute("data-verdict") !== (hit ? "hit" : "miss"));
        });
      }
      setCount(sec, count);
      if (count >= target) { markStage(sec, true); }   // `four_run`
    }

    each(wrap.querySelectorAll(".ks3-tbench-tab[data-food]"), function (b) {
      b.addEventListener("click", function () {
        wrap.setAttribute("data-food", b.getAttribute("data-food"));
        paint();
      });
    });
    each(wrap.querySelectorAll(".ks3-tbench-tab[data-test]"), function (b) {
      b.addEventListener("click", function () {
        wrap.setAttribute("data-test", b.getAttribute("data-test"));
        paint();
      });
    });

    each(opts, function (btn) {
      btn.addEventListener("click", function () {
        var k = key();
        // The FIRST press is the one that scores. A later press moves the
        // pressed state and nothing else — see the header.
        if (!Object.prototype.hasOwnProperty.call(ran, k)) {
          ran[k] = parseInt(btn.getAttribute("data-i"), 10);
          count += 1;
          paint();
          return;
        }
        each(opts, function (b) { b.setAttribute("aria-pressed", b === btn ? "true" : "false"); });
      });
    });

    paint();
  }
/* ═══ END B3 ═══ */

/* ═══ BEGIN B4 ═══ */

  /* ── B4 · Breathing and gas exchange (⊕ MRB-244) ──
     Five instruments, five wire functions, and one shared discipline:
     NOTHING HERE ANIMATES AND NOTHING HERE USES A TIMER. NOTES-B4 §6 says it
     of the unit and it is true of the engine — there is no rAF loop in any of
     these five, so there is no tick that would have to test
     `prefers-reduced-motion` inside itself (MRB-220 R4). The only motion in
     B4 is a CSS transition on a bar width or a panel height, and the
     stylesheet's reduced-motion block removes every one of them.

     Two of the five compute numbers in the browser and three do not, and the
     line between them is the CONTROL rather than a preference. `gas-compare`,
     `crossing-counter` and `fault-bench` have finite state — four rows, four
     states, three factors — so every figure they print and every bar width
     they draw is computed in `build_ks3.py` and ships as a finished string in
     the document; these functions move the highlight and nothing else, which
     is `gut-journey`'s rule. `bell-jar` and `two-process-ledger` are driven by
     a 0–100 slider, and 101 states cannot be enumerated, so those two carry
     their model's constants as attributes and evaluate them here. Where that
     happens, the constants are the AUTHORED ones and the format strings are
     the AUTHORED ones: no number and no sentence originates in this file. */

  /* ── gas-compare (b4-01 #s-air) ──
     Four gases, a prediction on each, then both bags.

     ⚖️ THE COUNT CHANGES WHAT IT IS COUNTING AT THE REVEAL. Before it, the
     line reads how many rows are committed; after it, how many were right.
     Both templates are authored and both ride as attributes, because each
     quotes a number that does not exist until the student has acted — the
     mechanism `_head_counter` already uses.

     ⚖️ NOTHING MARKS UNTIL THE REVEAL. R3: an option shows that it was chosen
     and nothing else. `data-verdict` is written on the ROW, once, at the
     moment the two bags appear — and by then the answer is on screen anyway,
     so it is a record of what the student predicted rather than a mark. */
  function wireGasCompare(sec) {
    var wrap = sec.querySelector("[data-gas]");
    if (!wrap) { return; }
    var rows = toArray(wrap.querySelectorAll(".ks3-gas-row"));
    var btn = wrap.querySelector("[data-gas-open]");
    var countEl = wrap.querySelector("[data-gas-count]");
    var table = wrap.querySelector("[data-gas-table]");
    var close = wrap.querySelector("[data-gas-close]");
    var total = parseInt(wrap.getAttribute("data-total"), 10) || rows.length;
    if (!rows.length || !btn) { return; }

    var COMMITTED = wrap.getAttribute("data-committed") || "";
    var SCORED = wrap.getAttribute("data-scored") || "";
    var picks = {};
    var open = false;

    function fill(tpl, n) {
      return tpl.split("{n}").join(String(n))
        .split("{total}").join(String(total));
    }

    function committed() {
      var n = 0, k;
      for (k in picks) { if (picks[k]) { n += 1; } }
      return n;
    }

    function refresh() {
      var n = committed();
      if (countEl) { countEl.textContent = fill(COMMITTED, n); }
      btn.disabled = n < total;
    }

    each(rows, function (row) {
      var id = row.getAttribute("data-gasrow");
      each(row.querySelectorAll(".ks3-gas-choice"), function (choice) {
        choice.addEventListener("click", function () {
          if (open) { return; }
          each(row.querySelectorAll(".ks3-gas-choice"), function (b) {
            b.setAttribute("aria-pressed", "false");
          });
          choice.setAttribute("aria-pressed", "true");
          picks[id] = choice.getAttribute("data-choice");
          refresh();
        });
      });
    });

    btn.addEventListener("click", function () {
      if (open || committed() < total) { return; }
      open = true;
      wrap.setAttribute("data-open", "1");
      btn.disabled = true;
      var right = 0;
      each(rows, function (row) {
        var id = row.getAttribute("data-gasrow");
        var ok = picks[id] === row.getAttribute("data-change");
        if (ok) { right += 1; }
        row.setAttribute("data-verdict", ok ? "right" : "wrong");
      });
      if (countEl) { countEl.textContent = fill(SCORED, right); }
      setHidden(table, false);
      setHidden(close, false);
      if (table) { table.setAttribute("role", "status"); }
      /* ⚖️ THE STAGE TICKS ON THE REVEAL, NOT ON THE FOURTH PREDICTION.
         Design's own `isDone` for this stop reads `airOpen`, and it is the
         right reading: a student who committed four predictions and never
         pressed the button has not seen the two bags, which is the whole
         activity. */
      markStage(sec, true);
    });

    refresh();
  }

  /* ── bell-jar (b4-02 #s-model) ──
     ⚖️ THE CHAIN IS THE INSTRUMENT, NOT THE PICTURE, and this function is
     written so that it could not become otherwise: all three chains are in the
     document, complete and authored, and what happens here is that one of them
     is shown and its number-bearing lines are refilled. Every sentence a
     student reads was written by the author; the only thing built at runtime
     is a decimal.

     ⚖️ THE PHASE IS DECIDED AGAINST `rest`, ONCE, and everything else follows
     from it — the chain, the note, the phase caption, the diaphragm caption
     and the air-movement readout. Five readouts, one decision, so they cannot
     disagree about which half of a breath is happening. */
  function wireBellJar(sec) {
    var wrap = sec.querySelector("[data-bell]");
    if (!wrap) { return; }
    var slider = wrap.querySelector("[data-bell-slider]");
    var chest = wrap.querySelector("[data-chest]");
    var lung = wrap.querySelector("[data-lung]");
    if (!slider) { return; }

    var REST = Number(wrap.getAttribute("data-rest"));
    var VBASE = Number(wrap.getAttribute("data-vbase"));
    var VSPAN = Number(wrap.getAttribute("data-vspan"));
    var PZERO = Number(wrap.getAttribute("data-pzero"));
    var PSPAN = Number(wrap.getAttribute("data-pspan"));

    /* The jar's geometry, and the ONLY numbers in this component that are not
       the author's. They are drawing — a rectangle's height and a circle's
       scale — and nothing student-readable comes out of either. */
    var CHEST_BASE = 28, CHEST_SPAN = 58;
    var LUNG_BASE = 0.62, LUNG_SPAN = 0.55;

    var steps = toArray(wrap.querySelectorAll(".ks3-bell-step"));
    var reads = {
      volume: wrap.querySelector('[data-read="volume"]'),
      pressure: wrap.querySelector('[data-read="pressure"]')
    };

    function phaseOf(dia) {
      return dia > REST ? "in" : (dia < REST ? "out" : "rest");
    }

    /* Two decimals for pressure, one for volume — Design's own precision, and
       it is not arbitrary: the pressure difference that fills a lung is a
       fraction of a kilopascal, and printed to one place the whole readout
       would sit at 0.0 through half the slider's travel. */
    function fill(tpl, vol, pres) {
      return tpl.split("{volume}").join(vol.toFixed(1))
        .split("{pressure_abs}").join(Math.abs(pres).toFixed(2))
        .split("{pressure}").join(pres.toFixed(2));
    }

    function showByAttr(attr, phase) {
      each(wrap.querySelectorAll("[data-" + attr + "]"), function (el) {
        setHidden(el, el.getAttribute("data-" + attr) !== phase);
      });
    }

    function draw() {
      var dia = Number(slider.value);
      var f = dia / 100;
      var vol = VBASE + f * VSPAN;
      var pres = -(f - PZERO) * PSPAN;
      var phase = phaseOf(dia);

      if (chest) {
        chest.style.height = (CHEST_BASE + f * CHEST_SPAN).toFixed(1) + "%";
        chest.setAttribute("data-phase-now", phase);
      }
      if (lung) {
        lung.style.transform =
          "scale(" + (LUNG_BASE + f * LUNG_SPAN).toFixed(2) + ")";
      }
      if (reads.volume) {
        reads.volume.textContent =
          (reads.volume.getAttribute("data-format") || "")
            .split("{volume}").join(vol.toFixed(1));
      }
      if (reads.pressure) {
        /* An explicit `+` on a positive pressure, because the row it sits
           above reads "0.00 kPa (atmospheric)" and the whole readout is a
           comparison against it. An unsigned 0.18 there says nothing about
           which side of atmospheric the chest is on. */
        reads.pressure.textContent =
          (reads.pressure.getAttribute("data-format") || "")
            .split("{pressure}")
            .join((pres >= 0 ? "+" : "") + pres.toFixed(2));
      }
      showByAttr("phase", phase);
      showByAttr("air", phase);
      showByAttr("dia", phase);
      showByAttr("chain", phase);
      showByAttr("note", phase);
      each(steps, function (step) {
        var tpl = step.getAttribute("data-format");
        if (tpl) { step.textContent = fill(tpl, vol, pres); }
      });
    }

    function onMove() {
      draw();
      /* ⚖️ THE STAGE TICKS WHEN THE MODEL HAS BEEN WORKED, which is Design's
         own `moved` flag. Not on load, and not on scroll: the block's argument
         is the ORDER the chain reports, and the order cannot be read without
         moving the sheet. */
      markStage(sec, true);
    }

    /* Bound to both, per NOTES-B4 §6. `input` is the live drag and `change`
       is the keyboard and the release; a slider on `change` alone does not
       move its readouts while it is being dragged. */
    slider.addEventListener("input", onMove);
    slider.addEventListener("change", onMove);

    each(wrap.querySelectorAll("[data-preset]"), function (btn) {
      btn.addEventListener("click", function () {
        slider.value = btn.getAttribute("data-preset");
        onMove();
      });
    });

    draw();
    markStage(sec, false);
  }

  /* ── crossing-counter (b4-03 #s-gradient) ──
     ⚖️ NOTHING HERE COMPUTES A COUNT OR A WIDTH. Both bar widths and all five
     printed figures were computed in `r_crossing_counter` from one pair of kPa
     values per state and ship as finished strings on that state's own note
     element. This function reads them across. That is `gut-journey`'s rule and
     it holds for the same reason: a width built here would be a second source
     for a number the document already carries, and the two would eventually
     stop agreeing.

     ⚖️ THE OUTWARD BAR IS NEVER SET TO ZERO BY THIS FUNCTION, because it is
     never set by this function at all — it is copied from a value the renderer
     already refused to accept as zero. There is no code path in B4 that can
     make molecules stop crossing outwards. */
  function wireCrossingCounter(sec) {
    var wrap = sec.querySelector("[data-cross]");
    if (!wrap) { return; }
    var notes = toArray(wrap.querySelectorAll(".ks3-cross-note"));
    var switches = toArray(wrap.querySelectorAll("[data-switch]"));
    if (notes.length !== 4 || switches.length !== 2) { return; }

    var tiles = {
      alveolar: wrap.querySelector('[data-tile="alveolar"]'),
      blood: wrap.querySelector('[data-tile="blood"]'),
      net: wrap.querySelector('[data-tile="net"]')
    };
    var vals = {
      "in": wrap.querySelector('[data-bar="in"]'),
      out: wrap.querySelector('[data-bar="out"]')
    };
    var fills = {
      "in": wrap.querySelector('[data-fill="in"]'),
      out: wrap.querySelector('[data-fill="out"]')
    };
    var state = { breathing: true, blood_flow: true };
    each(switches, function (sw) {
      state[sw.getAttribute("data-switch")] =
        sw.getAttribute("aria-pressed") === "true";
    });

    function key() {
      return (state.breathing ? "1" : "0") + "-" +
        (state.blood_flow ? "1" : "0");
    }

    function put(el, text) { if (el && text !== null) { el.textContent = text; } }

    function draw() {
      var k = key();
      var live = null;
      each(notes, function (note) {
        var on = note.getAttribute("data-state") === k;
        setHidden(note, !on);
        if (on) { live = note; }
      });
      if (!live) { return; }
      wrap.setAttribute("data-state", k);
      put(tiles.alveolar, live.getAttribute("data-alveolar"));
      put(tiles.blood, live.getAttribute("data-blood"));
      put(tiles.net, live.getAttribute("data-net"));
      put(vals["in"], live.getAttribute("data-in"));
      put(vals.out, live.getAttribute("data-out"));
      if (fills["in"]) {
        fills["in"].style.width = live.getAttribute("data-inw") + "%";
      }
      if (fills.out) {
        fills.out.style.width = live.getAttribute("data-outw") + "%";
      }
      each(switches, function (sw) {
        var id = sw.getAttribute("data-switch");
        var on = !!state[id];
        sw.setAttribute("aria-pressed", on ? "true" : "false");
        sw.textContent = sw.getAttribute(on ? "data-on-label" : "data-off-label");
      });
    }

    each(switches, function (sw) {
      sw.addEventListener("click", function () {
        var id = sw.getAttribute("data-switch");
        state[id] = !state[id];
        draw();
        /* ⚖️ ONE SWITCH IS ENOUGH TO TICK, which is Design's own `tried`.
           The block opens with both flows running and its argument is what
           happens when one stops, so the first stop IS the activity; requiring
           all four states would make the stop turn on exploring rather than on
           the thing being explored. */
        markStage(sec, true);
      });
    });

    draw();
  }

  /* ── fault-bench (b4-04 #s-bench) ──
     ⚖️ EVERY FACTOR KEEPS ITS OWN PICK AND ITS OWN OPENED FLAG, and the state
     lives in the DOM rather than in this closure: a factor's pick is the
     `aria-pressed` on its own hidden option set… except that there is one
     shared option set, so the picks are held here and re-applied on every tab
     change. Moving away from a factor and back finds it exactly as it was.

     ⚖️ THE REVEAL IS NEVER WITHHELD FOR A WRONG ANSWER. The verdict line says
     which of the two happened and the four rows follow either way. */
  function wireFaultBench(sec) {
    var wrap = sec.querySelector("[data-fault]");
    if (!wrap) { return; }
    var tabs = toArray(wrap.querySelectorAll(".ks3-fault-tab"));
    var scenarios = toArray(wrap.querySelectorAll(".ks3-fault-scenario"));
    var options = toArray(wrap.querySelectorAll(".ks3-option"));
    var reveals = toArray(wrap.querySelectorAll(".ks3-fault-reveal"));
    var btn = wrap.querySelector("[data-fault-open]");
    var hint = wrap.querySelector("[data-fault-hint]");
    var total = parseInt(wrap.getAttribute("data-total"), 10) || tabs.length;
    if (!tabs.length || !btn) { return; }

    var HINTS = {
      none: wrap.getAttribute("data-hint-none") || "",
      ready: wrap.getAttribute("data-hint-ready") || "",
      opened: wrap.getAttribute("data-hint-opened") || ""
    };
    var picks = {};
    var opened = {};
    var current = wrap.getAttribute("data-factor");

    function openedCount() {
      var n = 0, k;
      for (k in opened) { if (opened[k]) { n += 1; } }
      return n;
    }

    function draw() {
      var pick = picks[current];
      var isOpen = !!opened[current];

      each(tabs, function (tab) {
        tab.setAttribute("aria-pressed",
          tab.getAttribute("data-factor") === current ? "true" : "false");
      });
      each(scenarios, function (p) {
        setHidden(p, p.getAttribute("data-factor") !== current);
      });
      each(options, function (opt) {
        opt.setAttribute("aria-pressed",
          pick && opt.getAttribute("data-part") === pick ? "true" : "false");
        opt.disabled = isOpen;
      });
      each(reveals, function (r) {
        var on = isOpen && r.getAttribute("data-factor") === current;
        setHidden(r, !on);
        if (!on) { return; }
        var right = pick === r.getAttribute("data-answer");
        each(r.querySelectorAll("[data-verdict]"), function (v) {
          setHidden(v, v.getAttribute("data-verdict") !==
            (right ? "right" : "wrong"));
        });
        r.setAttribute("role", "status");
      });
      btn.disabled = isOpen || !pick;
      if (hint) {
        hint.textContent = isOpen ? HINTS.opened : (pick ? HINTS.ready : HINTS.none);
      }
      /* ⚖️ ALL THREE FACTORS. The block's argument is that different factors
         hit different parts of the same system, and a student who has opened
         one has met a case rather than the comparison. */
      markStage(sec, openedCount() >= total);
    }

    each(tabs, function (tab) {
      tab.addEventListener("click", function () {
        current = tab.getAttribute("data-factor");
        wrap.setAttribute("data-factor", current);
        draw();
      });
    });
    each(options, function (opt) {
      opt.addEventListener("click", function () {
        if (opened[current]) { return; }
        picks[current] = opt.getAttribute("data-part");
        draw();
      });
    });
    btn.addEventListener("click", function () {
      if (opened[current] || !picks[current]) { return; }
      opened[current] = true;
      draw();
    });

    draw();
  }

  /* ── two-process-ledger (b4-05 #s-ledger) ──
     ⚖️ THE RESPIRATION FILL IS NEVER TOUCHED BY THIS FUNCTION. Its width was
     written once, at build time, from the authored `resp_rate`, and there is
     no line below that selects it. That is the whole confrontation:
     `BREATH-12`/`BREATH-13` is the belief that plants respire only at night,
     and a student drags the light from midnight to noon and watches the top
     bar refuse to move. A respiration width computed here — even from a
     constant — would be one refactor away from acquiring a light term.

     ⚖️ THE MIDDLE BRANCH IS A THIRD THING, NOT A WEAK VERSION OF THE OTHER
     TWO. `balanced` takes its own colour and its own three paragraphs, because
     a flat line produced by two processes at full rate is the reading the
     lesson exists to explain, and a sensor cannot tell it from a dead plant. */
  function wireTwoProcessLedger(sec) {
    var wrap = sec.querySelector("[data-tpl]");
    if (!wrap) { return; }
    var slider = wrap.querySelector("[data-tpl-slider]");
    if (!slider) { return; }

    var RESP = Number(wrap.getAttribute("data-resp"));
    var MAX = Number(wrap.getAttribute("data-max"));
    var CONST = Number(wrap.getAttribute("data-const"));
    var SCALE = Number(wrap.getAttribute("data-scale"));
    var WINDOW = Number(wrap.getAttribute("data-window"));
    var RATE = wrap.getAttribute("data-rate-format") || "{v}";
    var IN = wrap.getAttribute("data-in-format") || "{v}";
    var OUT = wrap.getAttribute("data-out-format") || "{v}";

    var lightEl = wrap.querySelector("[data-light]");
    var photoVal = wrap.querySelector('[data-val="photo"]');
    var netVal = wrap.querySelector('[data-val="net"]');
    var photoFill = wrap.querySelector('[data-fill="photo"]');
    var netFill = wrap.querySelector('[data-fill="net"]');
    var notes = toArray(wrap.querySelectorAll("[data-note]"));
    var verdicts = toArray(wrap.querySelectorAll("[data-verdict]"));

    function draw() {
      var light = Number(slider.value);
      var photo = MAX * (1 - Math.exp(-light / CONST));
      var net = photo - RESP;
      var branch = Math.abs(net) < WINDOW
        ? "balanced" : (net > 0 ? "uptake" : "release");

      if (lightEl) {
        lightEl.textContent = light === 0
          ? (lightEl.getAttribute("data-dark") || "")
          : (lightEl.getAttribute("data-format") || "")
              .split("{n}").join(String(light));
      }
      if (photoVal) {
        photoVal.textContent = RATE.split("{v}").join(photo.toFixed(1));
      }
      if (netVal) {
        netVal.textContent = (net >= 0 ? IN : OUT)
          .split("{v}").join(Math.abs(net).toFixed(1));
      }
      if (photoFill) {
        photoFill.style.width = (photo / SCALE * 100).toFixed(1) + "%";
      }
      if (netFill) {
        netFill.style.width = (Math.abs(net) / SCALE * 100).toFixed(1) + "%";
        netFill.setAttribute("data-tone", branch);
      }
      each(notes, function (n) {
        setHidden(n, n.getAttribute("data-note") !== (light === 0 ? "dark" : "light"));
      });
      each(verdicts, function (v) {
        setHidden(v, v.getAttribute("data-verdict") !== branch);
      });
      each(wrap.querySelectorAll("[data-preset]"), function (b) {
        b.setAttribute("aria-pressed",
          Number(b.getAttribute("data-preset")) === light ? "true" : "false");
      });
    }

    function onMove() {
      draw();
      /* Design's own `moved`. The ledger opens in darkness with the net bar
         already reading a release, so ticking on load would credit a student
         for a reading they were handed. */
      markStage(sec, true);
    }

    slider.addEventListener("input", onMove);
    slider.addEventListener("change", onMove);
    each(wrap.querySelectorAll("[data-preset]"), function (btn) {
      btn.addEventListener("click", function () {
        slider.value = btn.getAttribute("data-preset");
        onMove();
      });
    });

    draw();
    markStage(sec, false);
  }

/* ═══ END B4 ═══ */


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
    // ⊕ B2 · Movement (MRB-220). Each of these owns every option inside
    // its section — `data-instrument` keeps `wirePredictions` out.
    each(root.querySelectorAll("[data-jobsort-block]"), wireJobSort);
    each(root.querySelectorAll("[data-switchblock]"), wireSwitch);
    each(root.querySelectorAll("[data-jointblock]"), wireJointBench);
    each(root.querySelectorAll("[data-muscleblock]"), wireMusclePair);
    // ⊕ C2 · Atoms, elements and compounds (MRB-220).
    each(root.querySelectorAll("[data-claimblock]"), wireClaimSwitch);
    each(root.querySelectorAll("[data-scaleblock]"), wireScaleZoom);
    each(root.querySelectorAll("[data-budgetblock]"), wireBudgetBench);
    each(root.querySelectorAll("[data-dishblock]"), wireDish);
    each(root.querySelectorAll("[data-vcardsblock]"), wireVerdictCards);
    each(root.querySelectorAll("[data-fbblock]"), wireFormulaBuilder);
    each(root.querySelectorAll("[data-balblock]"), wireBalanceBench);
    each(root.querySelectorAll("[data-pickblock]"), wirePick);
    // ═══ BEGIN C1 wiring ═══
    each(root.querySelectorAll("[data-counterblock]"), wireCollisionCounter);
    each(root.querySelectorAll("[data-ebenchblock]"), wireEvidenceBench);
    each(root.querySelectorAll("[data-gapblock]"), wireGapTestRig);
    each(root.querySelectorAll("[data-cutblock]"), wireHalvingBench);
    each(root.querySelectorAll("[data-hbblock]"), wireHeatingBench);
    each(root.querySelectorAll("[data-keyedblock]"), wireKeyedCommit);
    each(root.querySelectorAll("[data-mtlblock]"), wireModelTimeline);
    each(root.querySelectorAll("[data-predictblock]"), wirePredictionStack);
    each(root.querySelectorAll("[data-walkblock]"), wireRandomWalk);
    each(root.querySelectorAll("[data-sortcardsblock]"), wireSortCards);
    each(root.querySelectorAll("[data-sbenchblock]"), wireStateBench);
    each(root.querySelectorAll("[data-smatrixblock]"), wireStateMatrix);
    // ═══ END C1 wiring ═══
    // ═══ BEGIN B2 wiring ═══
    each(root.querySelectorAll("[data-leverblock]"), wireArmLever);
    each(root.querySelectorAll("[data-lstepblock]"), wireLeverSteps);
    each(root.querySelectorAll("[data-metersblock]"), wireMeterCompare);
    // ═══ END B2 wiring ═══
    // ═══ BEGIN B3 wiring ═══
    each(root.querySelectorAll("[data-plateblock]"), wireBandCommit);
    each(root.querySelectorAll("[data-clinicblock]"), wireClinicCases);
    each(root.querySelectorAll("[data-erunblock]"), wireEnzymeRun);
    each(root.querySelectorAll("[data-foldblock]"), wireFoldBuilder);
    each(root.querySelectorAll("[data-gutblock]"), wireGutJourney);
    each(root.querySelectorAll("[data-jobswblock]"), wireJobSwitch);
    each(root.querySelectorAll("[data-ledgerblock]"), wirePersonLedger);
    each(root.querySelectorAll("[data-tbenchblock]"), wireTestBench);
    // ═══ END B3 wiring ═══
    // ═══ BEGIN B4 wiring ═══
    each(root.querySelectorAll("[data-gasblock]"), wireGasCompare);
    each(root.querySelectorAll("[data-bellblock]"), wireBellJar);
    each(root.querySelectorAll("[data-crossblock]"), wireCrossingCounter);
    each(root.querySelectorAll("[data-faultblock]"), wireFaultBench);
    each(root.querySelectorAll("[data-tplblock]"), wireTwoProcessLedger);
    // ═══ END B4 wiring ═══
    wireCoverBar(root);
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
    wirePicker(document);
    // The page IS a lesson — record the visit. `data-ks3-lesson` is on
    // <body> for every lesson page, written or not, which is why the
    // ladder's own `data-lesson` could not be the source.
    markVisit(document.body ? document.body.getAttribute("data-ks3-lesson") : null);
    each(document.querySelectorAll(".ks3-rails"), wireRail);
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
