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

  /* ── MRB-235: record a finished ladder server-side ───────────────
     KS3 lesson pages carry no Supabase SDK (mirrors mrbadmus.v2.js's
     approach on topic pages), so the session token is read straight out
     of the same localStorage blob the SDK itself writes. A logged-out
     student has no token — the ladder still works, nothing is sent, and
     no error is shown, exactly as a logged-out chat degrades. subject /
     topic / subtopic come from the URL path (/ks3/<discipline>/<unit>/
     <lesson>.html), the same stable identifier assignment_questions'
     source_ref uses, because both need a lesson address that survives a
     content regeneration untouched by any database id. */
  function submitLadderScore(slug, got, total, rungs) {
    var token = null;
    try {
      var raw = window.localStorage.getItem("sb-urklkrwevjtlfbwnipjn-auth-token");
      token = raw && JSON.parse(raw).access_token;
    } catch (e) { /* private mode, or no session — degrade silently */ }
    if (!token) { return; }

    var parts = window.location.pathname.split("/").filter(Boolean);
    // .../ks3/<discipline>/<unit>/<lesson>.html
    var ks3At = parts.indexOf("ks3");
    var discipline = ks3At >= 0 ? parts[ks3At + 1] : "";
    var unit = ks3At >= 0 ? parts[ks3At + 2] : "";

    /* ⊕ MRB-262 — what each field is now, and why it was wrong before.

       question_text held `r.key`: the RUNG NAME — "recall", "apply",
       "explain", "produce". Per MRB-239 this row is the SNAPSHOT: the thing
       that preserves what was on screen when the content later changes. A
       rung label preserves nothing. Worse, the gap grid (MRB-157) and the
       Do Now generator (MRB-158) both read this field to tell a teacher
       WHICH question the class got wrong, and four rows all reading
       "explain" cannot answer that. It now carries the question the student
       actually saw, off `.ks3-rung-q`.

       ⊕ RESOLVED 19 Aug 2026. The rung is worth keeping — difficulty on a
       ladder is DEFINED by rung — and it now has a column
       (`quiz_question_attempts.rung`, migration 20260819122539) and a line
       in the backend's attempts map, so it persists rather than being
       silently dropped. It is no longer recoverable-by-assuming that every
       ladder is recall/apply/explain/produce in that order, which was the
       implicit coupling that argued for the column.

       selected_answer / correct_answer held the option letter GLUED to the
       option text — "ANothing at all" — because both were read off the
       button's textContent, and the letter badge is inside the button. No
       consumer could split them: an option beginning with a capital is
       indistinguishable from the prefix. That breaks per-distractor
       analysis, which is the main reason the question grain was ruled in —
       knowing nineteen students all chose the SAME wrong option is what
       turns a mark into a lesson plan. Letter and text are now read from
       their own elements and joined with a TAB, which authored prose from
       the HTML cannot contain. Free-text rungs carry no letter and so no
       separator. Two real columns remain the right answer and are still
       open; the tab is the unambiguous separator available without one, and
       it is now the payload's separator generally — MRB-239 uses it for the
       success-criteria list on free-text rungs too.

       time_spent_seconds was null on every row. Mide's per-student
       difficulty case is explicitly "finishes in four minutes with full
       marks", and that judgement cannot be made from a column that is
       always null. See stampTime(). */
    var attempts = rungs.map(function (r, i) {
      return {
        question_index: i,
        /* ⊕ MRB-270 phase 5 — the `|| r.key` FALLBACK IS GONE. It read
             question_text: r.question || r.key,
           and it is the same defect MRB-262 fixed, left with a back door: on
           any rung whose `.ks3-rung-q` failed to resolve, the rung NAME
           silently went back into the question column, indistinguishable from
           a real question and impossible to spot afterwards. A missing
           question is now an empty string — visibly missing, which is what a
           gap should look like.

           The IDENTITY of a ladder question is not this prose. It is
           (subtopic, rung), and both are already carried: subtopic on the
           quiz_scores row, rung in its own column since 20260819122539. That
           pair resolves back to the authored ladder, and verify_questions
           check 9 gates exactly that round trip. This field is the SNAPSHOT —
           what was on screen at the time — which is a different job and the
           reason it is stored at all. */
        question_text: r.question || "",
        rung: r.key,
        selected_answer: r.selectedText || "",
        correct_answer: r.correctText || "",
        /* ⊕ MRB-270 phase 5 — the letter, beside the text rather than glued
           to the front of it. Null on a free-text rung, which has no lettered
           option to record. See `answerParts()`. */
        selected_option_letter: r.selectedLetter || null,
        correct_option_letter: r.correctLetter || null,
        // ⊕ MRB-239 — self-marked rungs only. Marked rungs leave both null,
        // which is what the columns mean there: there were no criteria.
        criteria_met: r.criteriaMet || null,
        criteria_total: r.criteriaTotal == null ? null : r.criteriaTotal,
        /* ⊕ MRB-269 phase 4a (Mide, 20 Aug 2026). This line used to read
             is_correct: !!r.met,
           on every rung. On a SELF-marked rung `r.met` means one thing only:
           the student ticked every box. Nothing here reads their prose, so
           this page cannot know whether the answer is right — and it said
           `true` anyway. The proof is in the data it wrote: a `produce` rung
           whose answer was "test tsgd test tesb,da,hsc czlg test tsgd" landed
           as is_correct=true.

           Null is the honest value, and the column was made nullable to hold
           it (migration 20260820002…). What the student CLAIMED is already
           carried, in `criteria_met` / `criteria_total`, and that is real
           data — it is the claim that is being labelled as a claim.

           `got` is deliberately NOT touched: the student's own screen still
           scores all four rungs, which is what R8 ruled and what the ladder's
           "You marked rungs 3 and 4 yourself" line already discloses. */
        is_correct: r.mode === "self" ? null : !!r.met,
        time_spent_seconds: r.timeSpent
      };
    });

    try {
      fetch("https://mrbadmus-backend.onrender.com/api/quiz-score", {
        method: "POST",
        // ⊕ MRB-239 — `keepalive` is what lets this survive the unload that
        // triggered it. Without it the pagehide send is a request the
        // browser is entitled to cancel on its way out, which is exactly
        // when it is most needed.
        keepalive: true,
        headers: { "Content-Type": "application/json", "Authorization": "Bearer " + token },
        body: JSON.stringify({
          subject: discipline, topic: unit, subtopic: slug,
          score: got, max_score: total,
          attempts: attempts
        })
      }).catch(function () { /* best-effort — the ladder itself never waits on this */ });
    } catch (e) { /* private mode, or fetch unavailable — degrade silently */ }
  }

  /* ── the visit log (MRB-212) ────────────────────────────────────
     ks3_visits2 — { "<slug>": { t: <epoch ms>, done: <bool> } }

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
  /* MRB-257 decision 1 — the key is versioned at the C2 fix. Every "done"
     mark ever written was earned under the one-rung bug (`if (resolved)`
     on a COUNT), so the old store is discarded rather than migrated:
     grandfathering wrong marks into the pilot term would poison the first
     dashboard reads. `ks3_visits` is simply abandoned in place. */
  var VISITS_KEY = "ks3_visits2";
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

  /* MRB-257 (5.43) — where a result APPEARS and the control that produced
     it DISABLES in the same breath, a keyboard user is dropped to
     `<body>` and has to tab the whole page back to find what they just
     made happen. Four B10/B11 benches, the enzyme run (the only timed
     one, so the only one where the result lands after focus is already
     gone) and the food-tests bench all did exactly that. The panel takes
     a programmatic-only `tabindex="-1"` — it never enters the tab order —
     and is focused BEFORE the button is disabled, which is the half that
     matters: disable first and the browser has already moved focus.
     No-ops on a panel that is missing or still hidden, so a payload
     without one is unaffected. */
  function focusReveal(el) {
    if (!el || el.hasAttribute("hidden")) { return; }
    if (!el.hasAttribute("tabindex")) { el.setAttribute("tabindex", "-1"); }
    if (el.focus) {
      try { el.focus({ preventScroll: true }); }
      catch (err) { el.focus(); }
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
    var submitted = false;
    var armTimer = null;

    /* ⊕ MRB-262 — per-rung time.

       Defined as the interval between the previous rung being RESOLVED (or
       the ladder loading, for whichever rung is resolved first) and this one
       being resolved. Ordered by when the student actually finished each
       rung, not by page order, so the sitting is partitioned across the
       rungs with no overlap and no gaps and the four values sum to the time
       on the ladder — which is the figure Mide's "finishes in four minutes
       with full marks" judgement needs.

       Stamped from the INTERACTION handlers only, never from the restore
       path: a returning student's rung is already resolved when the page
       loads, and stamping there would record the reload rather than the
       work. Such a rung keeps `timeSpent: null`, which is honest — we do
       not know how long a previous sitting took.

       Capped at 30 minutes. Beyond that it is a tab left open, not
       thinking, and one 4-hour rung would swamp a class average. */
    var TIME_CAP_S = 30 * 60;
    var lastResolvedAt = Date.now();

    function stampTime(rec) {
      var now = Date.now();
      var secs = Math.round((now - lastResolvedAt) / 1000);
      if (secs < 0) { secs = 0; }
      rec.timeSpent = secs > TIME_CAP_S ? TIME_CAP_S : secs;
      lastResolvedAt = now;
    }
    /* MRB-257 (C3) — the score and note lines describe THIS sitting. A
       returning student's self-marked work is restored on load (wireSelf
       below), which used to make `resolved` non-zero before anything was
       touched: the ladder read "You got 2 of 4. Your best so far is 4 of
       4." over an untouched page, and the note was overwritten with the
       past-tense "You marked rungs 3 and 4 yourself." while the score
       still said "Not started yet.". Neither line is written until the
       student has actually done something here, which leaves the
       authored resting strings ("Not started yet." / "Rungs 3 and 4 you
       mark yourself.") in place. */
    var touched = false;
    var restScore = scoreEl ? scoreEl.textContent : "";
    var restNote = noteEl ? noteEl.textContent : "";

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

    // `live` marks a refresh caused by the student acting on the page, as
    // opposed to the one refresh at load that only reflects restored work.
    function refresh(live) {
      if (live) { touched = true; }
      var got = 0, resolved = 0, misses = 0, total = rungs.length;
      rungs.forEach(function (r) {
        if (r.resolved) { resolved += 1; }
        if (r.met) { got += 1; }
        // A miss: page-marked and answered wrongly, or self-marked, shown,
        // and not every criterion ticked.
        if (r.resolved && !r.met) { misses += 1; }
      });

      // MRB-257 (C3) — either a claim about THIS sitting, or the authored
      // resting strings left exactly as the build wrote them. Untouched, the
      // ladder says nothing at all; and "Retry my misses" can empty it
      // again, at which point it is genuinely not started.
      var claiming = touched && resolved > 0;
      if (claiming) {
        var lead = "";
        if (bestAtLoad !== null) {
          if (got > bestAtLoad) {
            lead = "That's your best yet — up " + (got - bestAtLoad) + ". ";
          } else if (got < bestAtLoad) {
            lead = "Your best so far is " + bestAtLoad + " of " + total + ". ";
          }
        }
        if (scoreEl) {
          scoreEl.textContent = "You got " + got + " of " + total + ".";
        }
        if (noteEl) { noteEl.textContent = lead + WHO; }
      } else if (touched) {
        if (scoreEl) { scoreEl.textContent = restScore; }
        if (noteEl) { noteEl.textContent = restNote; }
      }
      if (resolved && (bestSaved === null || got > bestSaved)) {
        bestSaved = got;
        writeStore(BEST_PREFIX + slug, { got: got, total: total });
      }
      /* MRB-212: all four rungs resolved means finished, whatever the
         score. The picker stops offering it — "pick up where you left
         off" is about unfinished work, not about marks.
         MRB-257 (C2) — this read `if (resolved)`, and `resolved` is a
         COUNT, so ONE rung marked a lesson finished on all 58 lessons.
         Same form as the MRB-235 guard immediately below. */
      if (total > 0 && resolved === total) { markVisit(slug, true); }
      setHidden(retryWrap, misses === 0);
      /* MRB-235 — record the attempt server-side once all four rungs are
         resolved. Once per page load: `submitted` guards a re-fire when
         "Retry my misses" resolves the ladder a second time in the same
         sitting, which would otherwise double-count the attempt.

         ⊕ MRB-239, 19 Aug 2026 — IT USED TO SEND HERE, AND THAT MADE THE
         NEW COLUMNS STRUCTURALLY EMPTY. A self-marked rung becomes
         `resolved` the instant "Check my answer" is pressed — which is the
         moment the criteria list OPENS, before the student has ticked a
         single one. Rungs 3 and 4 are the free-text ones on every lesson,
         so the last rung to resolve is always a self-marked one, and the
         payload left with `criteria_met: []` on it every single time.
         "19 of 24 students never tick criterion 3" would have been an
         artefact of the send timing, true of 24 of 24, forever. Driven on
         a real lesson before this fix: rung 4 posted `[]` while its boxes
         were being ticked a second later.

         So resolution ARMS the send instead of firing it, and any further
         self-marking re-arms it. It goes when the student stops — or, more
         reliably, when the page goes away. `submitted` still guarantees
         exactly one send. */
      if (resolved === total && !submitted) { arm(); }
    }

    /* Send when the marking has actually stopped.
       Two triggers, whichever comes first, both behind the one latch:
         · quiet for QUIET_MS with the ladder resolved — the student is done
           and still on the page;
         · the page is going away (`pagehide`, or hidden on mobile, where
           `pagehide` is unreliable) — send what we have, immediately.
       The quiet window is generous because reading five success criteria
       and judging your own answer against each is slow, deliberate work,
       and a short debounce would fire in the middle of it. Nothing is lost
       by waiting: the page-hide path is the real backstop. */
    var QUIET_MS = 20000;

    function arm() {
      if (submitted) { return; }
      if (armTimer) { clearTimeout(armTimer); }
      armTimer = setTimeout(send, QUIET_MS);
    }

    function send() {
      if (submitted) { return; }
      var got = 0, resolved = 0;
      rungs.forEach(function (r) {
        if (r.resolved) { resolved += 1; }
        if (r.met) { got += 1; }
      });
      // Only ever send a COMPLETE ladder — the arming path guarantees this,
      // and the page-hide path must not turn a half-done lesson into an
      // attempt row.
      if (!rungs.length || resolved !== rungs.length) { return; }
      submitted = true;
      if (armTimer) { clearTimeout(armTimer); armTimer = null; }
      submitLadderScore(slug, got, rungs.length, rungs);
    }

    window.addEventListener("pagehide", send);
    document.addEventListener("visibilitychange", function () {
      if (document.visibilityState === "hidden") { send(); }
    });

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

      /* ⊕ MRB-262 — letters read HERE, at wire time, and text read from
         `.ks3-opt-label` rather than from the button.

         The button's textContent is badge + label run together, which is how
         "ANothing at all" reached the database. Reading the two spans
         separately is the fix; reading the letter at wire time is what keeps
         it correct, because the moment a rung is answered every badge's
         innerHTML is replaced with a tick or cross SVG and the letter is
         gone from the DOM. */
      var letters = options.map(function (b) {
        var m = b.querySelector(".ks3-opt-mark");
        return m ? (m.textContent || "").trim() : "";
      });

      // Letter and text, joined by a TAB — a character authored prose out of
      // the HTML cannot contain, so a consumer can split on it with no
      // ambiguity at all. Separate columns are the right answer and are
      // proposed to Mide; this is the unambiguous form available today.
      /* ⊕ MRB-270 phase 5 — this RETURNS THE PARTS now, and the caller puts
         each in its own field. It used to return `letter + "\t" + text`.

         The tab was MRB-239's fix for a worse bug (letter and label read off
         one element and concatenated, so "ANothing at all" reached the
         column) and it chose the one separator authored prose cannot
         contain. That made the value SPLITTABLE, which is not the same as
         SPLIT, and MRB-239's own note said so: "two real columns remain the
         right answer and are still open".

         They are open now — `selected_option_letter` / `correct_option_letter`,
         migration 20260820091934 — because per-distractor analysis is the main
         reason the question grain was ruled in at all. Nineteen students
         choosing the SAME wrong option is what turns a mark into a lesson
         plan, and that wants a letter you can GROUP BY rather than a prefix
         whose length every consumer has to guess. An option beginning with a
         capital is indistinguishable from a prefix.

         A rung with no lettered options returns letter "" — the caller sends
         null, and null here means "there was no lettered option", not "we
         failed to read one". */
      function answerParts(i, btn) {
        var labelEl = btn.querySelector(".ks3-opt-label");
        var text = ((labelEl ? labelEl.textContent : btn.textContent) || "").trim();
        return { letter: letters[i] || "", text: text };
      }

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
          stampTime(rec);                                   // ⊕ MRB-262
          var chosen = answerParts(options.indexOf(btn), btn);
          rec.selectedText = chosen.text;
          rec.selectedLetter = chosen.letter;
          options.forEach(function (b, i) {
            if (b.getAttribute("data-correct") === "1") {
              var right = answerParts(i, b);
              rec.correctText = right.text;
              rec.correctLetter = right.letter;
            }
          });
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
          refresh(true);
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

      /* ⊕ MRB-239 — THE CRITERIA ARE THE MODEL ANSWER, so they are what
         `correct_answer` carries. Read here, at wire time, from the elements
         the build wrote them into, for the same reason `rec.question` is:
         this row is the SNAPSHOT, and it has to survive the lesson being
         regenerated with different words.

         The numeral is stripped — `.ks3-tick-num` is furniture the renderer
         adds, not part of the criterion, and leaving it in would put "1 " on
         the front of every stored string. */
      var criteria = boxes.map(function (b) {
        var lab = (b.nextElementSibling && b.nextElementSibling.tagName === "LABEL")
          ? b.nextElementSibling
          : (ticks && b.id ? ticks.querySelector('label[for="' + b.id + '"]') : null);
        if (!lab) { return ""; }
        var clone = lab.cloneNode(true);
        var num = clone.querySelector(".ks3-tick-num");
        if (num) { num.parentNode.removeChild(num); }
        return (clone.textContent || "").replace(/\s+/g, " ").trim();
      });
      /* Set at WIRE time, not in `tell()`. Every rung is sent, including
         ones the student never opened, and the model answer for an
         unattempted rung is still the model answer — a row that reported no
         criteria would read as a rung that had none. `tell()` then only
         moves `criteriaMet`. */
      rec.correctText = criteria.join("\t");
      rec.criteriaTotal = boxes.length;
      rec.criteriaMet = [];

      /* ⊕ RULING (Mide, 19 Aug 2026) — NO SELF-MARKING BEFORE A COMMITMENT.
         R8 already said the criteria "are not on the page until the student
         has written an answer, because a visible checklist is the answer"
         (see the load-bearing note on `.ks3-ticks` in ks3.css). What shipped
         only ever required a BUTTON PRESS: press it with an empty box and
         the whole success-criteria list — the model answer — arrived before
         a word had been written. This is the missing half of R8.

         The gate is LENGTH, and only length. Sixty characters is about a
         dozen words: enough to be an attempt at a sentence, low enough that
         a terse but genuine answer still gets through. Nothing here reads
         what was written — no keywords, no parsing, no judgement of any
         kind. It is the COMMITMENT that is required, not the correctness,
         and a page that marked the words before the student asked it to
         would be doing the very thing R8 exists to stop (R3 / MRB-196 R10).

         ⚠️ NO COPY, deliberately — §8.10. No "write at least 60 characters",
         no character counter, no nag. The control is simply not active yet
         and looks the way an inactive control looks. This is therefore the
         one dimmed control in the key stage with no progress readout beside
         it explaining the lock; that is Mide's ruling, taken knowingly, and
         WCAG 1.4.3 exempts an inactive component either way.

         ⚖️ THE GATE IS SPENT ONCE THE LIST HAS OPENED. From then on the
         button is a fold/unfold for work already committed, and taking it
         away because the student trimmed a sentence would strand them with
         the list open. `reopen()` clears `shown`, so a retry re-arms it —
         and a retry keeps the writing, so a real answer stays through. */
      var MIN_COMMIT = 60;

      function committed() {
        return !answer || (answer.value || "").trim().length >= MIN_COMMIT;
      }

      function gate() {
        if (!checkBtn) { return; }
        checkBtn.disabled = !(rec.shown || committed());
      }

      function tell() {
        var n = 0, all = boxes.length;
        boxes.forEach(function (b) { if (b.checked) { n += 1; } });
        rec.met = all > 0 && n === all;
        rec.selectedText = answer ? answer.value : "";
        /* ⊕ MRB-239 (Mide, 19 Aug 2026). This line used to read
             rec.correctText = n + " of " + all + " criteria ticked";
           — a RESULT, in a column whose every other row holds answer text,
           and a computed summary in a column that exists to be a snapshot.
           It could not answer the question the per-question grain was ruled
           in for. "19 of 24 students never tick criterion 3" is a lesson
           plan; "0 of 5" can never become one, however it is aggregated.

           So `correct_answer` carries the criteria themselves, tab-separated
           — TAB being the separator this payload already uses precisely
           because authored prose out of the HTML cannot contain one — and
           WHICH were ticked goes in its own columns. */
        rec.correctText = criteria.join("\t");
        rec.criteriaTotal = all;
        rec.criteriaMet = [];
        boxes.forEach(function (b, i) {
          if (b.checked) { rec.criteriaMet.push(i + 1); }   // 1-based
        });
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
        gate();
        tell();
      }

      // Folding the list away again is purely visual — the rung keeps
      // whatever it was marked.
      function collapse() {
        setHidden(ticks, true);
        setHidden(tally, true);
        if (checkBtn) {
          checkBtn.setAttribute("aria-expanded", "false");
          checkBtn.textContent = "Complete";
        }
        gate();
      }

      if (checkBtn) {
        checkBtn.setAttribute("aria-expanded", "false");
        checkBtn.addEventListener("click", function () {
          // A disabled button fires no click, so this is belt and braces —
          // but it keeps the invariant readable at the one place it matters.
          if (!rec.shown && !committed()) { return; }
          if (checkBtn.getAttribute("aria-expanded") === "true") { collapse(); }
          else {
            // ⊕ MRB-262 — stamp on the FIRST check, which is the moment the
            // writing stopped. Folding the list away and opening it again is
            // purely visual and must not restart the clock; and this sits in
            // the click handler rather than in show() because show() is also
            // how restored work is put back at load.
            var first = !rec.shown;
            show();
            if (first) { stampTime(rec); }
          }
          saveWork();
          refresh(true);
        });
      }
      boxes.forEach(function (b) {
        b.addEventListener("change", function () {
          tell(); saveWork(); refresh(true);
          // ⊕ MRB-239 — still marking, so push the send back. Without this
          // the quiet window would expire mid-way through a careful read of
          // the criteria and capture a half-finished self-mark.
          arm();
        });
      });
      if (answer) {
        answer.addEventListener("input", function () { gate(); saveWork(); });
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
      gate();
    }

    each(ladder.querySelectorAll(".ks3-rung"), function (rung) {
      var mode = rung.getAttribute("data-mode");
      var hasTicks = !!rung.querySelector("[data-ticks]");
      var hasOptions = rung.querySelectorAll(".ks3-option").length > 0;
      var self = mode === "self" || (!mode && hasTicks);
      // ⊕ MRB-262 — the question the student actually saw, captured at wire
      // time from the element the build writes it into. This is what the
      // snapshot is FOR: it has to survive the lesson being regenerated.
      var qEl = rung.querySelector(".ks3-rung-q");
      var rec = {
        key: rung.getAttribute("data-rung") || ("rung" + (rungs.length + 1)),
        question: qEl ? (qEl.textContent || "").trim() : "",
        el: rung,
        mode: self ? "self" : "marked",
        resolved: false,
        met: false,
        shown: false,
        timeSpent: null,
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
      refresh(true);
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
  /* ⊕ C3 (MRB-272) — A CARD GRID NOW TICKS ITS RAIL STOP.
     On c3-01, c3-02 and c3-05 `#s-words` is a rail stop, and before this the
     grid flipped cards and told the rail nothing: `doneByDom` finds no
     `.ks3-rung`, no `[data-reveal]` and no `.ks3-option` in a card grid, so
     the stop could never reach done. Design's own `DONE('s-words')` is "every
     card turned", and that is what is implemented here.

     ⚖️ TURNED, NOT LEFT OPEN. Credit is for having turned each card once, so
     a student who folds them back up keeps it — `markStage` is a ratchet and
     `seen` is never emptied. Reading a definition and then hiding it again is
     how you test yourself, and it must not cost the stop.

     ⚠️ Counted per GRID, not per page: a lesson may hold more than one, and
     `data-cards-total` is the denominator the renderer wrote. */
  function wireCards(root) {
    each(root.querySelectorAll("[data-cards]"), function (grid) {
      var sec = grid.closest(".ks3-keywords");
      var btns = toArray(grid.querySelectorAll(".ks3-card-btn"));
      var total = parseInt(grid.getAttribute("data-cards-total"), 10)
        || btns.length;
      var seen = {};

      each(btns, function (btn, i) {
        var back = btn.querySelector(".ks3-card-back");
        btn.setAttribute("aria-expanded", "false");
        btn.addEventListener("click", function () {
          var open = btn.getAttribute("aria-expanded") === "true";
          btn.setAttribute("aria-expanded", open ? "false" : "true");
          btn.classList.toggle("is-flipped", !open);
          setHidden(back, open);
          // Only OPENING a card counts as having met the word.
          if (!open) {
            seen[i] = true;
            var n = 0, k;
            for (k in seen) { if (seen[k]) { n += 1; } }
            if (n >= total) { markStage(sec, true); }
          }
        });
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
            /* MRB-257 (5.44) — "About 1½ onion cells fit across… Some of
               them show a small dark nucleus." At ×400 the view holds one
               cell and half of its neighbour, and "some of them" is a
               plural about that. The clause agrees with what is actually
               in the view. */
            + (CELL_W * ppm > 22
               ? (fovMM() / CELL_W < 2
                  ? " There is a small dark nucleus inside it."
                  : " Some of them show a small dark nucleus.") : "")
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

  /* MRB-257 decision 2 — rail credit is a RATCHET. MRB-208's rule is
     "nothing un-finishes it", and two instruments were breaking it by
     recomputing a live predicate every repaint: b8-04's "Empty the day"
     took a student from 2/4 to 0/4 (5.28), and b6-04's route tracer
     withdrew credit for exploring a second drug (5.29). Both, and every
     future caller, are fixed here rather than at each call site: a
     `markStage(sec, false)` that would LOWER an already-earned stage is a
     no-op. The wire-time `markStage(sec, false)` inits still work — the
     build emits `data-stage-done="0"`, so there is nothing to lower. */
  function markStage(sec, done) {
    if (!sec) { return; }
    if (!done && sec.getAttribute("data-stage-done") === "1") { return; }
    sec.setAttribute("data-stage-done", done ? "1" : "0");
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

    /* MRB-253 (5.1) — seed from the PRESSED button, not from DOM order.
       The markup ships `aria-pressed="true"` on the leaf, DOM order puts
       cheek first, and `refresh()` never repainted the buttons: the page
       said "Leaf cell" while the engine drew and answered for a cheek
       cell, under a gate question about a leaf cell. Zero interaction
       required to be taught the inverse of the lesson. */
    function pressedAttr(btns, attr, fallback) {
      for (var i = 0; i < btns.length; i++) {
        if (btns[i].getAttribute("aria-pressed") === "true") {
          return btns[i].getAttribute(attr);
        }
      }
      return btns.length ? btns[0].getAttribute(attr) : fallback;
    }
    var specimen = pressedAttr(specBtns, "data-specimen", spec.specimens[0].id);
    var view = pressedAttr(viewBtns, "data-view", "diagram");
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

    /* MRB-253 (5.2) — `alt`, `caption` and `tally` are authored as
       VIEW-KEYED dicts ({diagram, scope, "scope+stain"}), and were being
       assigned straight to `textContent`: students read the literal
       string "[object Object]" in the caption, the tally and the canvas's
       accessible name, on load, on the only drawn cell diagram in B1.
       Indexed by the live view key, with the plain view as the fallback
       for the "+extra" forms — `paint()` hardcodes `stained = false` and
       no stain control ships, so "scope+stain" is currently unreachable
       and falling back to "scope" is what a student should read.
       A plain string is still honoured, so a specimen authored without
       per-view text keeps working. */
    function viewText(field) {
      if (field === null || field === undefined) { return ""; }
      if (typeof field === "string") { return field; }
      var stained = false;                       // no stain control ships yet
      var exact = stained ? (view + "+stain") : view;
      if (typeof field[exact] === "string") { return field[exact]; }
      if (typeof field[view] === "string") { return field[view]; }
      return "";
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
      canvas.setAttribute("aria-label", viewText(sp.alt));
      if (caption) { caption.textContent = viewText(sp.caption); }
      if (tally) { tally.textContent = viewText(sp.tally); }
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
      /* MRB-253 (5.1) — the controls are repainted from the state on every
         readout, not only inside their own click handlers, so a control can
         never claim a specimen or a view the engine is not rendering. */
      each(specBtns, function (b) {
        b.setAttribute("aria-pressed",
          b.getAttribute("data-specimen") === specimen ? "true" : "false");
      });
      each(viewBtns, function (b) {
        b.setAttribute("aria-pressed",
          b.getAttribute("data-view") === view ? "true" : "false");
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
      if (clearBtn) {
        clearBtn.textContent = L.clear || "";
        /* MRB-257 (5.48) — "Strip it back out" was enabled over an empty
           cell, where there is nothing to strip: an enabled control that
           does nothing. Same rule as the Run button on the line below. */
        clearBtn.disabled = !count();
      }
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

  /* ── a loop that stops, and the one thing that has to wake it (⊕ MRB-257,
     audit 3.20) ────────────────────────────────────────────────────────────
     `motionReduced()` is asked EVERY FRAME on purpose: an OS setting or the
     page's own motion toggle changed mid-lesson takes effect without a
     reload, and two benches' comments say so. That property is free while a
     loop runs forever, and it is the property a loop that stops would lose —
     a student who turns reduced motion OFF would sit in front of a bench that
     never restarts, because nothing was scheduled to notice.
     So the loops stop, and this is what wakes them. Both sources, because
     there are two: the media query, and the `data-motion` attribute
     `wireMotion` writes on <html>. Listeners are attached once, on first
     registration, and only on a page that has an animated bench. */
  var MOTION_LISTENERS = null;
  function onMotionChange(fn) {
    if (!MOTION_LISTENERS) {
      MOTION_LISTENERS = [];
      var fire = function () {
        for (var i = 0; i < MOTION_LISTENERS.length; i++) { MOTION_LISTENERS[i](); }
      };
      if (B2_RM) {
        if (B2_RM.addEventListener) { B2_RM.addEventListener("change", fire); }
        else if (B2_RM.addListener) { B2_RM.addListener(fire); }
      }
      if (window.MutationObserver) {
        new window.MutationObserver(fire).observe(document.documentElement,
          { attributes: true, attributeFilter: ["data-motion"] });
      }
    }
    MOTION_LISTENERS.push(fn);
  }

  /* ⊕ MRB-277 — the narrow-viewport half of `data-format-narrow`.

     `setCount` is called with the live numbers and then forgets them, so a
     student who ROTATES the phone would keep whichever form was chosen at
     the last interaction until the next one. These remember the last call
     per element and replay it when the query flips, which is the only way
     the compact form can be correct at both orientations without the
     instruments each learning about viewports.

     360px rather than 320: the readout has to fit the narrowest phone in
     use, and the breakpoint is the width at which the full sentence stops
     fitting rather than the width of any particular device. */
  var NARROW_Q = "(max-width: 360px)";
  var narrowCounters = [];

  function isNarrowViewport() {
    return !!(window.matchMedia && window.matchMedia(NARROW_Q).matches);
  }

  function rememberNarrowCounter(sec, el, n, extra) {
    for (var i = 0; i < narrowCounters.length; i++) {
      if (narrowCounters[i].el === el) {
        narrowCounters[i].n = n;
        narrowCounters[i].extra = extra;
        return;
      }
    }
    narrowCounters.push({ sec: sec, el: el, n: n, extra: extra });
  }

  if (window.matchMedia) {
    var narrowMql = window.matchMedia(NARROW_Q);
    var replayNarrow = function () {
      // A copy, because `setCount` calls `rememberNarrowCounter` again.
      var all = narrowCounters.slice(0);
      for (var i = 0; i < all.length; i++) {
        setCount(all[i].sec, all[i].n, all[i].extra);
      }
    };
    if (narrowMql.addEventListener) {
      narrowMql.addEventListener("change", replayNarrow);
    } else if (narrowMql.addListener) {
      narrowMql.addListener(replayNarrow);
    }
  }

  /* The block head's live progress readout. Three authored shapes — a count
     ("3 of 6 decided"), a two-state label ("Meter fitted") and a count with
     a bespoke zero ("All three claims on" → "2 switched off") — one element
     and one updater, so a fourth cannot arrive as a fourth copy. */
  function setCount(sec, n, extra) {
    var el = sec && sec.querySelector("[data-count]");
    if (!el) { return; }
    var fmt = el.getAttribute("data-format");
    /* ⊕ MRB-277 — `data-format-narrow`, the COMPACT form, and it is the
       mirror of `data-zero` / `data-full` / `data-format-one` rather than a
       fifth shape. Measured at 320px, c2-02's readout — "8 of 8 tests left ·
       0 of 6 decided", 33 characters of 15px mono at `flex: 0 0 auto` — put
       the page 342px wide and made it scroll sideways.

       ⚖️ RULED (Mide, 21 Aug 2026): SHORTEN THE FORMAT, DO NOT WRAP IT. A
       wrapped mono readout changes height as its numbers change, so the
       block would jump under the student's finger while they were reading
       it. What the counter SAYS at any width is the author's sentence; only
       which of the author's two sentences is chosen depends on the viewport.

       Opt-in, so all 102 other counters are byte-identical, and read BEFORE
       the `extra` substitution below so the compact form carries the same
       live numbers as the full one. */
    var narrow = el.getAttribute("data-format-narrow");
    if (fmt && narrow && isNarrowViewport()) { fmt = narrow; }
    if (narrow) { rememberNarrowCounter(sec, el, n, extra); }
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
      /* ⊕ MRB-250 — `total > 0`, because a counter with NO denominator emits
         `data-total="0"` and a clamp against zero is not a clamp, it is a
         readout stuck on its opening value for ever. b9-02's head row is
         "year 0" → "year 26": one sentence, one number, and no denominator
         anywhere on the page, because there is nothing the years are counting
         towards. Without this narrowing the field can be run for a century and
         the readout still says year zero. A zero denominator was previously
         unreachable in a format that also names {n}, so no shipped counter
         moves. */
      if (!isNaN(total) && total > 0 && n > total) { n = total; }
      /* ⊕ MRB-244 / B6 — `data-full`, the mirror of `data-zero`. b6-01's
         readout is "not started" → "stage 3 of 5" → "all five stages", and
         the top end is a bespoke sentence for the same reason the bottom end
         is: "stage 5 of 5" says the student is standing on the last stage,
         not that the dose has been followed the whole way round. Opt-in, and
         read AFTER the clamp so it cannot be reached by an over-count. */
      var full = el.getAttribute("data-full");
      if (full && !isNaN(total) && total > 0 && n >= total) {
        el.textContent = full;
        return;
      }
      /* ⊕ MRB-248 / B11 — `data-format-one`, the SINGULAR, and the mirror of
         `data-zero` and `data-full` rather than a fourth shape. b11-03's
         readout is "1 combination tried" → "4 combinations tried" and b11-04's
         does the same with "field": the noun agrees with the count, and one is
         a state every student passes through on the way to the second.
         The author writes the noun once, as "combination(s) tried"; the ENGINE
         splits the `(s)` and hands both halves down. Opt-in, read after the
         clamp and after `data-full`, so no shipped counter moves. */
      var single = el.getAttribute("data-format-one");
      if (single && n === 1) { fmt = single; }
      el.textContent = fmt.replace("{n}", String(n))
        .replace("{total}", el.getAttribute("data-total") || "");
    } else {
      el.textContent = n ? (el.getAttribute("data-on") || "")
                         : (el.getAttribute("data-off") || "");
    }
  }

  /* ⊕ MRB-244 / B6 — the same head-row paragraph, driven by a NAMED STATE
     rather than by a tally. b6-02's readout is "clock not started" → "clock
     running" → "cleared": three authored sentences, no number in any of them,
     and the transitions decided by two independent facts rather than by one
     counter crossing a line. The instrument names its state and this prints
     the author's sentence for it — nothing here composes a string, and a
     state with no authored label is left alone rather than blanked, because a
     blank readout is worse than a stale one.

     ⊕ MRB-245 / B7 — `extra`, and it is the same idea `setCount` already has.
     b7-03's readout is "not run yet" → "full method" → "{n} steps skipped":
     four named states, two of which quote a number, and the transitions are
     decided by two independent facts (has the bench been run, how many steps
     differ from the full method) rather than by one counter crossing a line.
     Composing "3 steps skipped" out of a count would need a denominator that
     appears nowhere on the page; substituting into the author's own sentence
     needs nothing but the number. Opt-in, so every shipped readout that names
     no placeholder is byte-identical across the change. */
  function setCountState(sec, name, extra) {
    var el = sec && sec.querySelector("[data-count]");
    if (!el) { return; }
    var label = el.getAttribute("data-state-" + name);
    if (label === null) { return; }
    if (extra) {
      for (var k in extra) {
        if (Object.prototype.hasOwnProperty.call(extra, k)) {
          label = label.split("{" + k + "}").join(String(extra[k]));
        }
      }
    }
    el.setAttribute("data-state", name);
    el.textContent = label;
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
      /* MRB-257 (5.26) — `j.twist &&`, exactly as `draw()` has it. Without
         it, pressing "Try to twist it" on a hinge or a fixed joint set
         `aria-pressed="true"`, relabelled the button "Twisting" and — worse
         — replaced `j.twist_no` ("It will not. The end of one bone sits in
         a groove in the other.") with the empty `j.twist_yes`, deleting the
         explanation the press exists to produce, while the canvas went on
         drawing the struck-through refusal. Two readouts of one fact, and
         they disagreed. */
      var twisting = !!(j.twist && twists[j.id]);
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
        pump();
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
          pump();
        });
      });
    }
    if (twistBtn) {
      twistBtn.addEventListener("click", function () {
        var j = joint();
        twists[j.id] = !twists[j.id];
        touch(j.id);
        repaint();
        pump();
      });
    }

    /* ⊕ MRB-257 · audit 3.20 — THIS LOOP USED TO RUN FOR EVER, FROM LOAD, WITH
       NOTHING ANIMATING. The old `tick` re-scheduled itself unconditionally
       and only the DRAWING was gated on `spinning()`. Verified by patching
       `requestAnimationFrame` before the document's own scripts: `joints`
       scheduled frames continuously at idle with zero interaction, and at the
       same 60fps with `prefers-reduced-motion: reduce` emulated, while 16
       other pages in the same slice scheduled none. Nothing was visibly wrong
       — the cost was a permanent wake-up on a school Chromebook, which is the
       machine this whole key stage is built for.
       Now the loop exists only while something is actually turning, and
       `pump()` is called from every control that could start it. */
    var raf = 0;
    function spinning() {
      var j = joint();
      return !!(j.twist && twists[j.id] && !motionReduced());
    }
    function pump() {
      if (raf || !window.requestAnimationFrame) { return; }
      if (!spinning()) { last = 0; return; }
      raf = window.requestAnimationFrame(tick);
    }
    function tick(now) {
      raf = 0;
      var dt = Math.min(0.05, (now - (last || now)) / 1000);
      last = now;
      // Still asked every frame, so a preference changed mid-spin still lands
      // on the next one — and `onMotionChange` below covers the other
      // direction, where there is no next frame to land on.
      if (spinning()) {
        spin += dt * 1.1;
        draw();
        pump();
      } else {
        last = 0;
      }
    }

    repaint();
    setCount(sec, 0);
    onMotionChange(pump);
    pump();
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

     ⚠️ The settings counter counts THE FOUR CONTRACTION MODES and nothing
     else. It used to run over a mixed key space — four mode ids and two
     kill ids — so "4 of 4 settings tried" was reachable as two modes plus
     two kills, and the stop ticked without the student ever pressing
     "Both" (the joint locks) or "Neither" (it falls), which is what the
     block exists to teach. MRB-257 (5.49). The denominator on the page is
     4 and there are exactly four modes, so this is the label meaning what
     it says; the kill switches still change the arm, they just do not
     count towards a total they were never part of. */
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

    /* Only the four contraction modes are counted — see the header. */
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
        pump();
      });
    });
    each(killBtns, function (b) {
      b.addEventListener("click", function () {
        var id = b.getAttribute("data-kill");
        dead[id] = !dead[id];
        b.setAttribute("aria-pressed", dead[id] ? "true" : "false");
        repaintReadouts();
        pump();
      });
    });

    /* ⊕ MRB-257 · audit 3.20 — the same permanent idle loop as `joints`, on
       the same two pages the audit measured. Here the condition is physical
       rather than a preference: the arm is either travelling towards its
       target or it has arrived, and there is nothing to draw once it has. */
    var raf = 0;
    function travelling() { return Math.abs(target() - angle) > 0.3; }
    function pump() {
      if (raf || !window.requestAnimationFrame) { return; }
      if (!travelling()) { last = 0; return; }
      raf = window.requestAnimationFrame(tick);
    }
    function tick(now) {
      raf = 0;
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
        pump();
      } else {
        last = 0;
      }
    }

    repaintReadouts();
    setCount(sec, 0);
    // Reduced motion SNAPS rather than travels, so switching it ON while the
    // arm is mid-flight needs one more frame to land the snap, and switching
    // it OFF needs the loop back. One registration covers both.
    onMotionChange(pump);
    pump();
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
    /* ⊕ RULING (Mide, 19 Aug 2026) — PRESSURE IS A NUMBER, IN KILOPASCALS.
       The bar carried no value, so `PRESSURE` was a label with nothing
       beside it and the one quantity the lesson is about was the only
       readout on the bench a student could not read off. See `draw()`. */
    var KPA = Number(cfg.kpa_per_hit) || 7;
    /* ⊕ RULING (Mide, 19 Aug 2026) — THE READOUT IS SETTLED, NOT LIVE.
       `SMOOTH` is how much simulation the displayed number averages over;
       `SHOW` is how often the display is allowed to change. Both are
       teaching decisions in exactly the way `window_ms` is, so both are
       authored in the payload beside it.

       ⚑ ANSWERING THE FLAG ON `kpa_per_hit`, which reads: "A reading that
       curved, floored, capped or smoothed would quietly teach the
       opposite. Do not add any of those." The flag is kept and answered
       rather than deleted, because what it protects is still protected.
       It guards ONE property — that pressure is exactly proportional to
       the hit rate — and that property is untouched: `shownKpa` is
       `shownHits * KPA` and nothing else, so a student who checks the
       arithmetic on screen finds it holds at every setting. What is
       smoothed is the MEASUREMENT NOISE, not the relationship. The live
       count swung 11 → 16 hits (77 → 112 kPa) several times a second on
       the shipped bench, which does not teach proportionality either — it
       hides it behind a number nobody can read. A curve, a floor or a cap
       would all change `kpa` as a function of `hits`; averaging the hits
       changes only how steady the pair is. */
    var SMOOTH = Number(cfg.smooth_ms) || 900;
    var SHOW = Number(cfg.readout_ms) || 500;
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

    /* The settled readout. `samples` holds one hits-per-second estimate per
       frame over the last `SMOOTH` ms; `shownHits` is the integer latched
       out of their mean every `SHOW` ms, and it is the ONLY hit figure that
       reaches the drawing, the bar or the aria-label. `moveAt` is when it
       last stepped to a different value, which is what the accent fade on
       the big number is timed from. */
    var samples = [];
    var shownHits = 0;
    var lastShow = 0;
    var moveAt = -1e9;
    /* When the gas last changed. Hits counted under the PREVIOUS gas are
       not evidence about this one, so a control press drops them — and
       until a full `WINDOW` has elapsed the rate is measured over however
       much time has actually passed, rather than over a second that has
       not happened yet. Without that the first reading after every press
       dips towards zero and then climbs, which reads as the opposite of
       the change the student just made. */
    var regimeAt = 0;

    function nowTs() {
      return (window.performance && window.performance.now)
        ? window.performance.now() : last;
    }

    function newRegime(now) {
      hits = [];
      samples = [];
      regimeAt = now;
      /* NOT `now - SHOW`. Latching immediately would average an empty
         sample buffer and drop the readout to zero for half a second on
         the way to a value that is usually higher — a dip the student did
         not cause. The number holds its last settled value for one cadence
         and then steps to the new one. */
      lastShow = now;
    }

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
      /* ⊕ MRB-257 phase 4 — THE CONTAINER DIAL WAS DRAWN AND NEVER MODELLED.
         `VOLS[].scale` reached `draw()` and nothing else: the simulation runs
         in NORMALISED box coordinates with walls fixed at 0.02/0.98, and
         `draw()` maps that unit square onto the scaled rectangle. So the
         picture showed a smaller box with the particles filling it, while the
         normalised free path — and therefore the wall-hit rate — never moved.

         Measured before the fix, warm, 24 particles, fourteen one-second
         samples each: Large 14.7/s, Half size 14.3/s, Quarter size 14.9/s.
         The lesson's FIRST prediction is "the container is made smaller and
         nothing else changes — what happens to the wall hits?", marked "Up …
         same speed, shorter trip, more arrivals", and the resting note says
         "Smaller box, same particles, same speed — and the count is up". The
         bench disproved all of it, on the one dial the lesson opens with.

         The particles have a fixed DRAWN radius (r = 9) and a fixed absolute
         speed; what shrinks is the box. So the normalised step has to be
         divided by the box scale, which is the same statement. Nothing about
         the drawing moves — the particles still fill the box — and the Large
         setting is arithmetically unchanged, so the resting page is untouched.
         Temperature and particle count were always modelled and are not
         touched here. */
      // ⊕ MRB-254 (carrying MRB-257) — the dial is a VOLUME factor, and the
      // wall-hit rate is `1 / volume`. Half the volume is exactly twice the
      // hits; a quarter is exactly four times. That is `P ∝ 1/V`, and it is
      // the relationship the lesson's first prediction asks about, so the
      // instrument had better be it rather than approximate it: the old
      // linear 0.62 / 0.40 gave ×1.6 and ×2.5 under labels reading half and
      // quarter.
      var box = Number(VOLS[state.vol].volume) || 1;
      var speed = (Number(TEMPS[state.temp].speed_multiplier) || 0)
        * scale * STEP * dt * 60 / box;
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

      /* Hits per second, still COUNTED — the divisor is the time actually
         spent counting, capped at the window. A floor of 200 ms keeps the
         first two or three frames after a control press from dividing by
         something near zero. */
      var span = Math.min(WINDOW, Math.max(200, now - regimeAt)) / 1000;
      samples.push({ t: now, v: hits.length / span });
      while (samples.length && now - samples[0].t > SMOOTH) { samples.shift(); }
    }

    /* Latched twice a second, from the mean of the last `SMOOTH` ms of
       estimates. Everything downstream reads `shownHits`, so the drawing,
       the bar and the label always agree with one another and with the
       arithmetic a student can do on screen. */
    function settle(now) {
      if (now - lastShow < SHOW) { return; }
      lastShow = now;
      var mean = 0, i;
      if (samples.length) {
        for (i = 0; i < samples.length; i++) { mean += samples[i].v; }
        mean = mean / samples.length;
      }
      var next = Math.round(mean);
      if (next !== shownHits) {
        shownHits = next;
        moveAt = now;
        setAlt();
      }
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

      // ⊕ MRB-254 (carrying MRB-257) — √volume, so the AREA reads as the
      // label. The dial says "Half size"; a box drawn at linear 0.5 shows a
      // QUARTER of the paper, and a student who reads the label off the
      // picture learns that halving something quarters it. Linear √0.5 =
      // 0.7071 puts half the area on screen, which is what "half size" means
      // for a container.
      var scale = Math.sqrt(Number(VOLS[state.vol].volume) || 1);
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

      /* ── the live readout ──
         ⊕ SUPERSEDES NOTES flag 6, ruled by Mide on 19 Aug 2026. The flag
         said "a COUNT and a BAR, never a pascal", and what shipped was a
         `PRESSURE` caption over an unlabelled bar — a dial with no value
         on it. A bar without a number teaches nothing quantitative, and
         pressure is the quantity this lesson exists to build.

         ⚖️ THE NUMBER IS A STATED CALIBRATION, NOT A CALCULATION, and
         nothing on the page pretends otherwise. Twelve particles in a box
         have no meaningful pressure; computing one from first principles
         would give something like 10⁻²³ kPa and would be a lie wearing
         rigour. This bench is a model of a SAMPLE of a real gas, so the
         honest treatment is to anchor it: the resting bench — warm, large
         box, 24 particles — runs at 14.4 wall hits per second, and
         `kpa_per_hit` is authored at 7 so that reads ~101 kPa, which is
         atmospheric, the one pressure a student meets everywhere else.

         ⚖️ AND IT IS EXACTLY LINEAR IN THE HIT RATE, by construction:
         `kpa = count * KPA` and nothing else. Double the hits, double the
         pressure, at every one of the 27 control combinations — that
         proportionality IS the lesson, and a reading that drifted away
         from the count would teach its opposite. Anything that makes this
         a curve, a floor, a cap or a smoothed average breaks it.

         Whole kilopascals; one decimal below 10, so a cold, large, sparse
         box reads a small pressure rather than "0 kPa". */
      /* ⊕ RULING (Mide, 19 Aug 2026) — PRESSURE IS THE BIG NUMBER.
         The two readouts have swapped positions. Wall hits per second was
         in the 58px slot and pressure was a 20px value beside the bar,
         which put the instrument's typography behind the quantity the
         lesson is NOT about: hits are the mechanism, kilopascals are the
         science. The shapes are unchanged and simply exchanged — big
         value under a mono caption, and the caption-left / value-right row
         — so nothing new was drawn, only re-ranked. The bar stays with
         pressure, where it always belonged.

         Both figures come from `shownHits`, never from `hits.length`, so
         `pressure = hits × 7` is exact on what is ON SCREEN and not merely
         on a value that flickered past between two paints. */
      var count = shownHits;
      var kpa = count * KPA;
      var kpaText = (kpa < 10 ? kpa.toFixed(1) : String(Math.round(kpa)));
      var kpaUnit = " " + (CL.pressure_unit || "kPa");
      var px = 620;
      var barW = 220, barH = 22;

      ctx.fillStyle = COUNTER_INK.label;
      ctx.font = '500 12px "DM Mono", ui-monospace, monospace';
      ctx.fillText(CL.pressure || "", px, 66);

      // The unit rides at caption size beside the figure rather than inside
      // it: "1015 kPa" at 58px would run off the panel, and a dial's unit
      // is not the same size as its reading anywhere else either.
      ctx.font = '700 58px "Bricolage Grotesque", system-ui, sans-serif';
      var numW = ctx.measureText(kpaText).width;
      ctx.fillStyle = COUNTER_INK.line;
      ctx.fillText(kpaText, px, 122);
      /* ⊕ The moment the number moves, marked in the accent and faded out
         over `FLASH` — the same colour and the same decay the wall-hit
         rings already use, so this is the instrument's existing vocabulary
         rather than a second one. It exists because a settled readout that
         simply appears at a new value can be missed; the lesson is the
         CHANGE, so the change is what is marked. */
      var moveAge = (now - moveAt) / FLASH;
      if (moveAge >= 0 && moveAge < 1) {
        ctx.fillStyle = "rgba(" + COUNTER_INK.flash + ","
          + (1 - moveAge).toFixed(3) + ")";
        ctx.fillText(kpaText, px, 122);
      }
      ctx.fillStyle = COUNTER_INK.label;
      ctx.font = '500 12px "DM Mono", ui-monospace, monospace';
      ctx.fillText(kpaUnit, px + numW, 122);

      ctx.fillStyle = COUNTER_INK.dash;
      ctx.fillRect(px, 138, barW, barH);
      ctx.fillStyle = COUNTER_INK.bar;
      ctx.fillRect(px, 138, barW * Math.min(1, count / FULL), barH);
      ctx.strokeStyle = COUNTER_INK.line;
      ctx.lineWidth = 2;
      ctx.strokeRect(px, 138, barW, barH);

      // Wall hits per second, demoted to the row the pressure value used to
      // occupy: caption left, value right, same sizes as before.
      ctx.fillStyle = COUNTER_INK.label;
      ctx.font = '500 12px "DM Mono", ui-monospace, monospace';
      ctx.fillText(CL.hits || "", px, 184);
      ctx.textAlign = "right";
      ctx.fillStyle = COUNTER_INK.line;
      ctx.font = '700 20px "Bricolage Grotesque", system-ui, sans-serif';
      ctx.fillText(String(count), px + barW, 184);
      ctx.textAlign = "left";

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

    /* ⊕ The pressure number joins the label for the same reason the hit
       count did (map §4.6): every readout on this bench is drawn INSIDE
       the canvas, so `aria-label` is the only route to any of it. Ruling
       "pressure must be shown as a number" is not met by showing it to
       sighted students only. Same rounding as the drawing. */
    function altText(h) {
      var k = h * KPA;
      return (ALT.template || "")
        .split("{temp}").join((TEMPS[state.temp].label || "").toLowerCase())
        .split("{vol}").join((VOLS[state.vol].label || "").toLowerCase())
        .split("{n}").join(String(live()))
        .split("{hits}").join(String(h))
        .split("{kpa}").join((k < 10 ? k.toFixed(1) : String(Math.round(k)))
          + " " + (CL.pressure_unit || "kPa"));
    }

    /* ⊕ The SETTLED figure, not the instantaneous one. A screen-reader
       student and a sighted student have to be reading the same bench, and
       `shownHits * KPA` is the pair the arithmetic holds on. */
    function setAlt() {
      if (canvas) { canvas.setAttribute("aria-label", altText(shownHits)); }
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
        /* The gas has changed, so the second of hits already banked was
           measured on a different gas. Dropping it is what lets the
           readout reach its new level inside a second instead of drifting
           there through a blend of the two. */
        newRegime(nowTs());
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
      // The clock starts at the first frame, not at the time origin: hits
      // are only counted from here, so the rate must be divided from here.
      if (!regimeAt) { regimeAt = now; lastShow = now; }
      step(now, dt);
      settle(now);
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

    /* ⊕ RULING (Mide, 19 Aug 2026) — A TEST HAS TO RUN.
       ⚑ ANSWERING THE FLAG ABOVE ("Nothing animates: the two boxes are a
       before-and-after, not a process"), kept rather than deleted. The
       boxes were a before-and-after of the CHOICE, and the flag is right
       about that much. But the three buttons are the argument of the whole
       lesson, and what they did was swap a paragraph: `draw()` never read
       `test` at all, so a student pressed `Squash the gas` under a caption
       reading "run a test and watch it fail" and watched nothing happen.
       Prose describing a demonstration is not a demonstration. Each test
       is now a process — squash, pour, spread — and it fails on screen
       when the gaps are filled. Reduced motion now has something real to
       degrade, and degrades to the END STATE rather than to nothing: the
       compressed box, the risen level, the stalled particle. */
    var RUN_MS = 1500;
    var testAt = -1e9;
    var raf = 0;

    function nowMs() {
      return (window.performance && window.performance.now)
        ? window.performance.now() : new Date().getTime();
    }

    function pump() {
      if (!raf && window.requestAnimationFrame) {
        raf = window.requestAnimationFrame(frame);
      }
    }

    function frame() {
      raf = 0;
      draw();
      if (test !== null && nowMs() - testAt < RUN_MS
          && window.requestAnimationFrame) {
        raf = window.requestAnimationFrame(frame);
      }
    }

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

      /* ── running a test ──
         `u` is how far through the demonstration we are, 0 → 1, and it
         holds at 1 so the end state stays on screen to be read. `solid`
         is the only thing that differs between the two boxes, so every
         effect below is written once and asked the same question: what
         does this test do when there is somewhere to go, and what does it
         do when there is not. */
      var u = 0;
      if (test !== null) {
        u = Math.min(1, Math.max(0, (nowMs() - testAt) / RUN_MS));
        u = 1 - Math.pow(1 - u, 3);
      }

      function drawBox(x0, label, solid) {
        var bx = x0 + 34, by = 52, bw = half - 68, bh = H - 108;

        /* SQUASH — the wall comes in. With gaps the particles are pushed
           closer and the gas gives; packed, there is nothing left to
           squash and the wall stops almost at once. */
        var sq = 0;
        if (test === "squash") { sq = (solid ? 0.03 : 0.38) * u; }
        var iw = bw * (1 - sq);

        ctx.save();
        ctx.beginPath();
        ctx.rect(bx, by, iw, bh);
        ctx.clip();
        // The fill IS the answer: the space between the particles stops
        // being space. Clipped to the box so it cannot read as a
        // background, and the particles are drawn identically in both
        // boxes so the only difference on screen is the gap.
        if (solid) {
          ctx.fillStyle = "#4A4038";
          ctx.fillRect(bx, by, iw, bh);
        }

        /* MIX — small particles are poured in. With gaps they fall into
           the spaces between the large ones and the level does not rise
           to meet the sum; packed, they have nowhere to go but on top,
           and the level lands exactly on the dashed prediction. */
        var poured = test === "mix";

        for (var row = 0; row < 4; row++) {
          for (var col = 0; col < 7; col++) {
            var x = bx + 28 + col * 54 + (row % 2 ? 16 : 0);
            var y = 78 + row * 44;
            x = bx + (x - bx) * (1 - sq);
            ctx.beginPath();
            ctx.arc(x, y, 17, 0, Math.PI * 2);
            ctx.fillStyle = "#D98A4A";
            ctx.fill();
            ctx.strokeStyle = "#5A3212";
            ctx.lineWidth = 2;
            ctx.stroke();
          }
        }

        if (poured) {
          /* Twelve small particles poured in from above.

             With gaps, they DROP INTO the spaces between the large ones —
             two rows of six, in the interstices — and the level does not
             rise to meet the prediction. That is 50 + 50 = 97 on screen.

             Packed, there is no interstice to drop into, so they come to
             rest in a single layer ON TOP of the pile, and the level rises
             to land exactly on the dashed line. That is the failure: with
             the gap filled the volumes must simply add, and they do not. */
          for (var k = 0; k < 12; k++) {
            var tx = solid ? bx + 26 + k * ((bw - 52) / 11)
                           : bx + 89 + (k % 6) * 54;
            var ty1 = solid ? 68 : 100 + Math.floor(k / 6) * 88;
            var ty = 30 + (ty1 - 30) * u;
            ctx.beginPath();
            ctx.arc(tx, ty, 7, 0, Math.PI * 2);
            ctx.fillStyle = "#FFC53D";
            ctx.fill();
            ctx.strokeStyle = "#6B4A12";
            ctx.lineWidth = 1.5;
            ctx.stroke();
          }
        }

        /* SMELL — one particle tries to cross. With gaps it works its way
           the full width of the box; packed, it gets a fraction of the
           way and stops dead against the fill. */
        if (test === "smell") {
          var reach = solid ? 0.07 : 0.92;
          var sx = bx + 30 + (bw - 60) * reach * u;
          var sy = 100 + Math.sin(u * 9) * 30;
          ctx.beginPath();
          ctx.moveTo(bx + 30, 100);
          var t2;
          for (t2 = 0; t2 <= u; t2 += 0.02) {
            ctx.lineTo(bx + 30 + (bw - 60) * reach * t2,
                       100 + Math.sin(t2 * 9) * 30);
          }
          ctx.strokeStyle = "rgba(255,197,61,0.45)";
          ctx.lineWidth = 2;
          ctx.setLineDash([5, 4]);
          ctx.stroke();
          ctx.setLineDash([]);
          ctx.beginPath();
          ctx.arc(sx, sy, 12, 0, Math.PI * 2);
          ctx.fillStyle = "#FFC53D";
          ctx.fill();
          ctx.strokeStyle = "#6B4A12";
          ctx.lineWidth = 2;
          ctx.stroke();
        }
        ctx.restore();

        // The dashed prediction line: where the level would sit if the two
        // volumes simply added. Drawn on both boxes so the comparison is
        // between them and not against a memory.
        if (poured) {
          // Where the level would sit if the two volumes simply added.
          // Drawn on BOTH boxes at the same height, so the comparison a
          // student makes is between the two lines and not against memory.
          ctx.strokeStyle = "rgba(255,197,61,0.55)";
          ctx.lineWidth = 2;
          ctx.setLineDash([6, 5]);
          ctx.beginPath();
          ctx.moveTo(bx, 58);
          ctx.lineTo(bx + iw, 58);
          ctx.stroke();
          ctx.setLineDash([]);
          // The level actually reached: up to the prediction when the gap
          // is packed, short of it when the gap did the absorbing.
          var lvl = 84 - (solid ? 26 * u : 0);
          ctx.strokeStyle = "#FF8A5B";
          ctx.lineWidth = 3;
          ctx.beginPath();
          ctx.moveTo(bx, lvl);
          ctx.lineTo(bx + iw, lvl);
          ctx.stroke();
        }

        ctx.strokeStyle = "#5C5249";
        ctx.lineWidth = 2;
        ctx.strokeRect(bx, by, iw, bh);

        // The plunger, drawn only while squashing — it is what the moving
        // wall IS, and without it the box merely gets narrower.
        if (test === "squash") {
          ctx.fillStyle = "#8A7B6B";
          ctx.fillRect(bx + iw, by, 12, bh);
          ctx.strokeStyle = "#5C5249";
          ctx.lineWidth = 2;
          ctx.strokeRect(bx + iw, by, 12, bh);
        }

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
        // "Changing the answer afterwards re-runs the same test against
        // the new gap, which is the point" — so it re-runs, rather than
        // repainting the old test's finished frame with a new gap in it.
        if (test !== null && !motionReduced()) { testAt = nowMs(); }
        repaint();
        if (test !== null && !motionReduced()) { pump(); }
      });
    });

    each(testBtns, function (btn) {
      btn.addEventListener("click", function () {
        test = btn.getAttribute("data-test");
        each(testBtns, function (b) {
          b.setAttribute("aria-pressed", b === btn ? "true" : "false");
        });
        /* Under reduced motion the run is over before it starts: `u`
           computes to 1 on the first paint, so the student gets the whole
           result and none of the movement. Pressing the same button again
           re-runs it, which is what a student does when they missed it. */
        testAt = motionReduced() ? -1e9 : nowMs();
        repaint();
        if (test !== null && !motionReduced()) { pump(); }
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

     ⊕ SUPERSEDED BY MIDE, 19 Aug 2026; kept, because it records what was
     believed. Ten halvings IS the journey — it is the same journey the
     single-cut button makes, ten times, and the intermediate sizes are the
     evidence that the piece keeps halving right down to the floor. Jumping
     to the end state showed a student the destination and none of the road.
     The run is played at `STEP_MS` per cut instead. Reduced motion still
     has the complete instrument, and now has something real to degrade: it
     loses the sub-second glide between sizes and keeps every size, every
     cut and every zoom announcement.

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
    // ⊕ The zoom annotation. Authored in the lesson record like every other
    // string set into this drawing; the fallback exists only so a payload
    // that predates the ruling renders rather than printing "undefined".
    var L_ZOOM = wrap.getAttribute("data-label-zoom") || "ZOOMED IN ×{n}";

    var canvas = wrap.querySelector("[data-cut-canvas]");
    var outCount = wrap.querySelector('[data-cut-out="count"]');
    var outSize = wrap.querySelector('[data-cut-out="size"]');
    var verdicts = toArray(wrap.querySelectorAll("[data-verdict]"));
    var notes = toArray(wrap.querySelectorAll("[data-note]"));
    var btns = toArray(wrap.querySelectorAll(".ks3-cut-btn"));
    var counter = sec.querySelector("[data-count]");

    var n = 0;
    var reached = false;

    /* ═══ ⊕ RULING (Mide, 19 Aug 2026) — THE PIECE VISIBLY SHRINKS ═══════
       ⚑ ANSWERING TWO FLAGS, both kept above and in the renderer's
       docstring rather than deleted, because they record what was believed
       and this records what replaced it.

       Flag: "NOTHING ANIMATES … ten halvings is not a journey".
       Flag: "THE NUMBERS ARE THE LESSON, NOT THE PICTURE … a drawing that
       stays deliberately dull."

       What shipped drew the piece at a fixed 176px at every one of the 24
       cuts. A student pressed `Cut it in half` five times and watched a
       number change beside a picture that did not — so the claim the unit
       rests on, that halving TERMINATES, was being made by a caption while
       the drawing quietly said the opposite. The flags were protecting the
       instrument against decoration; a piece that does not halve when you
       halve it is not restraint, it is the instrument contradicting its own
       readout. Mide's rule governs: what matters is that a student SEES the
       science happen.

       ⚖️ HOW 24 HONEST HALVINGS FIT ON ONE CANVAS. They do not — the span
       is a factor of 16 million — so the view RESCALES IN STAGES and says
       so. Inside a stage each cut halves the drawn edge for real: 240 → 120
       → 60. The fourth would land near 30px, which is below reading size,
       so the view zooms and the piece is drawn large again. The rhythm the
       student learns is shrink, shrink, shrink, ZOOM — and the zoom is
       itself the powers-of-ten lesson, which is why it is announced on the
       canvas rather than performed silently.

       ⚖️ THE GRAIN PHASE RE-ANCHORS ITS STAGE, and that is not a tidy-up.
       `across` is 2^(FLOOR - n) particles per edge, so within a stage the
       box and the particle count halve together and the drawn PARTICLE
       RADIUS is constant — particles do not shrink, the piece does, which
       is the whole claim. Anchoring the stage at `FLOOR - GRAIN` puts a
       zoom exactly where the block resolves into countable particles, and
       leaves the floor as one large particle instead of a 15px dot. */
    var BASE = 240;
    var STAGE = 3;
    var TWEEN = 260;
    var ZOOM_MS = 1100;
    var STEP_MS = 130;

    // Where the current stage starts. The smooth run anchors at 0; the
    // grain phase anchors at its own first cut.
    function anchor(k) { return k >= FLOOR - GRAIN ? FLOOR - GRAIN : 0; }
    function level(k) { return (k - anchor(k)) % STAGE; }
    function boxFor(k) { return BASE / Math.pow(2, level(k)); }

    /* The magnification the view gained arriving at `k` from `k - 1`, or 0
       for an ordinary cut. The piece halved in truth, so the factor is the
       change in drawn size times two — computed, never assumed, because the
       jump into the grain stage is ×4 where every other one is ×8. */
    function zoomInto(k) {
      if (k <= 0) { return 0; }
      var f = (boxFor(k) / boxFor(k - 1)) * 2;
      return f > 1.01 ? Math.round(f) : 0;
    }

    var drawnBox = boxFor(0);
    var tweenFrom = drawnBox, tweenTo = drawnBox, tweenAt = -1e9;
    var zoomBy = 0, zoomAt = -1e9;
    var queue = 0, queueAt = 0;
    var raf = 0;

    function ms() {
      return (window.performance && window.performance.now)
        ? window.performance.now() : new Date().getTime();
    }

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
      var W = 900, H = 380;
      ctx.setTransform(1, 0, 0, 1, 0, 0);
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      ctx.setTransform(2, 0, 0, 2, 0, 0);
      ctx.fillStyle = "#FFFDF8";
      ctx.fillRect(0, 0, W, H);

      /* ⊕ THE PIECE HANGS FROM A FIXED BASELINE, and it has to now that the
         piece changes size. Everything under the drawing — the particle
         count, the scale bar, the ruler — is positioned at `cy + box / 2`,
         which was a constant while `box` was pinned at 176 and would
         otherwise now swing 90px between stages and push the ruler clean
         off the canvas. Anchoring the BOTTOM edge keeps every one of those
         expressions untouched and makes them all constant again: the piece
         grows upward out of the ruler, which is also the right picture. */
      var BOTTOM = 258;
      var cx = W / 2;
      // The PAINTED edge, which is the tween's current value rather than
      // the resting size for `n` — so a cut is watched, not discovered.
      var box = drawnBox;
      var cy = BOTTOM - box / 2;

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

      /* ⊕ THE ZOOM SAYS SO. A view that rescales without saying it has
         rescaled teaches that the piece stopped shrinking, which is the
         defect this whole change exists to remove. Terse mono in the
         accent, fading out over `ZOOM_MS` — the instrument's own caption
         voice, no new words on the page and no new colour. It is drawn
         under reduced motion too: the tween is what degrades, never the
         announcement. */
      var zAge = (ms() - zoomAt) / ZOOM_MS;
      if (zoomBy && zAge >= 0 && zAge < 1) {
        ctx.fillStyle = "rgba(228,87,46," + (1 - zAge * zAge).toFixed(3) + ")";
        ctx.font = '500 13px "DM Mono", ui-monospace, monospace';
        // Top left, clear of both the piece at its largest and the ghost's
        // own caption, which starts at `cx - box`.
        ctx.textAlign = "left";
        ctx.fillText(L_ZOOM.replace("{n}", String(zoomBy)), 60, 26);
      }

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
      pump();
      if (n >= FLOOR) { reached = true; }
      if (reached) { markStage(sec, true); }
    }

    /* ── the animation loop ──
       Runs only while something is in flight: a size tween, a fading zoom
       annotation, or a queued run of cuts. It stops itself, so an idle
       bench costs nothing and the resting page still paints exactly once.

       ⚖️ REDUCED MOTION DROPS THE TWEEN, NOT THE SEQUENCE. The sizes
       still step, one state at a time, because those states ARE the
       lesson and skipping to the end is what the shipped bench did. What
       goes is the sub-second glide between them. */
    function easeOut(u) { return 1 - Math.pow(1 - u, 3); }

    function frame() {
      raf = 0;
      var now = ms();
      var busy = false;

      if (queue) {
        if (now - queueAt >= STEP_MS) {
          queueAt = now;
          var dir = queue > 0 ? 1 : -1;
          var was = queue;
          stepOne(dir);
          // `stepOne` zeroes the queue when it runs out of ladder, so the
          // decrement only applies when a cut actually happened.
          if (queue === was) { queue = was - dir; }
        }
        if (queue) { busy = true; }
      }

      var u = (now - tweenAt) / TWEEN;
      if (u < 1) {
        drawnBox = tweenFrom + (tweenTo - tweenFrom) * easeOut(Math.max(0, u));
        busy = true;
      } else {
        drawnBox = tweenTo;
      }
      if (zoomBy && now - zoomAt < ZOOM_MS) { busy = true; }

      draw();
      // `stepOne` → `repaint` → `pump` may already have booked the next
      // frame from inside this one; booking a second would fork the loop.
      if (busy && !raf && window.requestAnimationFrame) {
        raf = window.requestAnimationFrame(frame);
      }
    }

    function pump() {
      if (!raf && window.requestAnimationFrame) {
        raf = window.requestAnimationFrame(frame);
      } else if (!window.requestAnimationFrame) {
        drawnBox = tweenTo;
        draw();
      }
    }

    /* One cut, or one undo. Everything that moves the bench goes through
       here, so the tween, the zoom announcement and the readouts can never
       disagree about which cut the piece is on. */
    function stepOne(dir) {
      var next = Math.max(0, Math.min(FLOOR, n + dir));
      if (next === n) { queue = 0; return; }
      var z = dir > 0 ? zoomInto(next) : 0;
      n = next;
      tweenFrom = drawnBox;
      tweenTo = boxFor(n);
      if (motionReduced()) {
        drawnBox = tweenTo;
        tweenAt = -1e9;
      } else {
        tweenAt = ms();
      }
      // Undo walks back down the ladder without announcing a zoom: the
      // student is retracing, not discovering.
      if (z) { zoomBy = z; zoomAt = ms(); }
      repaint();
    }

    each(btns, function (b) {
      b.addEventListener("click", function () {
        var step = parseInt(b.getAttribute("data-step"), 10) || 0;
        if (b.getAttribute("data-act") === "undo") { step = -step; }
        if (!step) { return; }
        /* ⊕ A RUN OF CUTS IS PLAYED, NOT JUMPED. `Cut ten more times` used
           to move the count by ten in one frame. Ten halvings IS a journey
           — it is the same journey the single-cut button makes, ten times
           over, and the intermediate sizes are the evidence. Played at
           `STEP_MS` so it is quick and still perceptible. */
        var want = Math.max(0, Math.min(FLOOR, n + step)) - n;
        if (!want) { return; }
        /* THE FIRST CUT LANDS ON THE CLICK, the rest are played. A control
           that does nothing until the next animation frame feels broken on
           a single press, and it would also make the count unreadable to
           anything driving the bench synchronously — the parity gate cuts
           to the floor in a tight loop and reads `[data-cut-out]` between
           clicks. The readouts stay a direct consequence of the press; only
           the SIZES are what take time. */
        var dir = want > 0 ? 1 : -1;
        queue = want - dir;
        queueAt = ms();
        stepOne(dir);
        if (queue) { pump(); }
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
    /* ⊕ MRB-257 phase 4 — THE NOTE'S OWN LATCH, and it is NOT `everEven`.
       `even` is a threshold on a noisy count (|right − N/2| < N × 0.09,
       sampled 3×/s), so once the tank has evened out it crosses the line
       back and forth: measured on the shipped bench, warm, 16 flips in 181
       one-second samples after the first Yes. The live Yes/No readout
       flickering is honest — the balance IS dynamic, and that is the lesson
       — but the NOTE is not a reading, it is a claim about how far through
       the run you are, and it opens "Early on, far more particles cross
       left-to-right…". A student watching an evenly-spread tank at 100
       seconds was being told they were early on, repeatedly.
       Separate from `everEven` because that one drives the rail and must
       never un-finish (MRB-208); this one describes the TANK and so is
       cleared by `reset()`, which puts the dye back on the left. */
    var evenSeen = false;
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
      // The dye is back on the left, so the tank has not evened out — but
      // the rail keeps what it earned (MRB-208).
      evenSeen = false;
      even = false;
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
      if (even) { evenSeen = true; }
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
      if (evenSeen) { return "even"; }
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
      /* MRB-257 (5.27) — once the four steps are open, this block is a
         RECORD of the problem the student answered, and the rig above it
         has stopped being its subject. Adopting a later rig state rewrote
         the worked answer underneath a locked, disabled answer box: a
         student who wrote 320 N, was told "the worked answer is 320 N",
         then nudged the load slider, was told "You wrote 320 N. The worked
         answer is 80 N." — marked wrong for having been right. The picks,
         the box and the unit all lock at the same moment; the numbers now
         lock with them. */
      if (open) { return; }
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
    /* MRB-257 (5.51) — the verdict is DECIDED WHEN THE RUN ENDS and then
       held. `repaint()` used to re-derive it from the live rate, so
       finishing a run and then pressing a different pH flipped the verdict
       while the three counters underneath it did not move: the panel
       described a run that had not happened. */
    var finishedWhich = "";
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
      /* MRB-255 S4 — `opt_ph` IS A SET and the gap is to the NEAREST
         optimum in it. One protease with a scalar optimum of 2 put pH 8
         six units away against a span of 4.5, so protease in the small
         intestine read 0% and the verdict said "the conditions are simply
         wrong for it" — under a rule card reading "Best at pH 2 in the
         stomach, 8 in the small intestine". Pepsin ~2, trypsin ~8. A
         scalar still works and means a one-element set. `_erun_rate` in
         build_ks3.py IS THIS FUNCTION; a change to one is a change to
         both. */
      var opts = OPT[enzyme];
      if (!(opts instanceof Array)) { opts = [opts]; }
      var gap = Infinity;
      for (var oi = 0; oi < opts.length; oi++) {
        gap = Math.min(gap, Math.abs(ph - Number(opts[oi])));
      }
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
      if (finished && !running && finishedWhich) {
        each(verdicts, function (el) {
          setHidden(el, el.getAttribute("data-verdict") !== finishedWhich);
        });
        var wasHidden = verdict && verdict.hasAttribute("hidden");
        setHidden(verdict, false);
        /* MRB-257 (5.43) — this is the only TIMED instrument on the estate,
           so it is the only one where the result arrives after the Run
           button has already disabled and dropped focus to `<body>`. Once,
           on the transition, so a later repaint does not steal focus back. */
        if (wasHidden) { focusReveal(verdict); }
      }

      setCount(sec, everRan ? 1 : 0);
      markStage(sec, everRan);
    }

    /* ⊕ Design's branch order, unchanged — denatured first, then a rate too
       low to be doing anything, then the run that worked — with one branch
       added in front of "slow".
       MRB-257 (5.7) — "A little product, slowly" was printed over `Rate 0%`
       and `0 units made` on protease + pH 7, lipase + pH 2 and carbohydrase
       + pH 2: nothing was produced, and the sentence says a little was. The
       honest branch is `product === 0`, tested BEFORE the rate. It needs an
       authored `[data-verdict="nothing"]` span, which no payload carries
       yet, so the branch falls back to Design's three when the page has not
       shipped one — see HANDOFF. */
    function verdictFor() {
      var pct = Math.round(rateFor() * 100);
      if (denatured) { return "denatured"; }
      if (product === 0 && hasVerdict("nothing")) { return "nothing"; }
      return pct < SLOW ? "slow" : "worked";
    }

    function hasVerdict(key) {
      for (var i = 0; i < verdicts.length; i++) {
        if (verdicts[i].getAttribute("data-verdict") === key) { return true; }
      }
      return false;
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
        finishedWhich = verdictFor();
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
        finishedWhich = "";
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
      finishedWhich = "";
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
        finishedWhich = "";
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
      /* MRB-257 (5.18) — the note is keyed to WHICH levels are on, not to
         how many. Keyed on the count, villi-only printed "Corrugating the
         wall triples it" (that is the folds), microvilli-only printed the
         same note about a level that "needs an electron microscope", and
         folds+microvilli printed "Villi are where most of the gain comes
         from. Ten square metres" with the villi switched off.
         Three ways to choose a note, in order:
           1. an authored set note — `data-note-set="folds+villi"`;
           2. the cumulative note, but ONLY when the levels that are on are
              the first `on` levels in document order, which is the stack
              the four shipped notes were written for;
           3. nothing. A blank line is worse than a stale one, but it is
              better than a sentence describing a level that is switched
              off, and the area, the multiple and the bar all still read.
         The eight authored set notes are a records job — see HANDOFF. */
      var onIds = [], prefix = true;
      each(levels, function (li, i) {
        var lit = li.getAttribute("data-on") === "1";
        if (lit) { onIds.push(li.getAttribute("data-level") || String(i)); }
        if (lit !== (i < on)) { prefix = false; }
      });
      var setKey = onIds.join("+");
      var hasSet = false;
      each(notes, function (p) {
        if (p.getAttribute("data-note-set") === setKey) { hasSet = true; }
      });
      each(notes, function (p) {
        var show = hasSet
          ? p.getAttribute("data-note-set") === setKey
          : (prefix && p.getAttribute("data-note") === String(on)
             && !p.hasAttribute("data-note-set"));
        setHidden(p, !show);
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
        /* MRB-257 (5.44) — the singular. This line reads "1 portions,
           2,400 kJ" on a plate holding one thing, which is a state every
           student passes through on the way to the second. `data-format-one`
           is the same opt-in `setCount` has carried since MRB-248, read
           here for the same reason; no payload carries one yet, so nothing
           shipped moves until it does — see HANDOFF. */
        var pFmt = (portions === 1 && portionEl.getAttribute("data-format-one"))
          ? "data-format-one" : "data-format";
        portionEl.textContent = portions
          ? fill(portionEl, pFmt, { n: portions, total: group(total) })
          : (portionEl.getAttribute("data-empty") || "");
      }

      if (matchEl) {
        setHidden(matchEl, !matched);
        each(matchEl.querySelectorAll("[data-mhead]"), function (p) {
          setHidden(p, p.getAttribute("data-mhead") !== person);
        });
      }

      setCount(sec, portions);
      /* `food_on_the_plate`. MRB-257 (5.28) — this is a LIVE predicate, so
         "Empty the day" used to take the rail from 2/4 to 0/4 and strip the
         ticks off the ledger stop and its mirror. `markStage` is a ratchet
         now (MRB-257 decision 2), so the first portion ticks it and nothing
         un-ticks it — MRB-208's "nothing un-finishes it", enforced once at
         the writer rather than at each of fifty call sites. */
      markStage(sec, portions > 0);
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
          /* MRB-257 (5.43) — committing the prediction removes the whole
             predict block, which is where focus was: a keyboard user was
             ejected past the result panel AND the two tab rows into the
             mastery ladder. The result is the thing they just made happen,
             so it is where they should be. */
          focusReveal(wrap.querySelector("[data-result='" + k + "']"));
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
      /* MRB-257 (C1) — the BLOCK HEAD's readout, which is a different
         element from the bench's own count line and was never written:
         `data-format="{n} of 4 predicted"` sat at "0 of 4 predicted" for
         ever, including after the reveal. The reveal is gated on
         `committed() === total`, so this line is already at 4 of 4 by the
         time the two bags appear. */
      setCount(sec, n);
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
      /* MRB-257 (5.48) — the twelve gas-choice buttons are SPENT once the
         bags are open. The handler already early-returns on `open`, but the
         buttons stayed enabled and in the tab order, so a keyboard user
         tabbed through twelve controls that do nothing. */
      each(rows, function (row) {
        each(row.querySelectorAll(".ks3-gas-choice"), function (choice) {
          choice.disabled = true;
        });
      });
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
      /* MRB-257 (C1) — and so does the head readout, off the same flag.
         `data-on="model worked"` was unreachable, so the head said "not
         moved yet" over a worked model. Sticky, like the stage: sliding
         back to rest does not un-work the model. */
      setCount(sec, 1);
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
    var kpaFoot = wrap.querySelector("[data-cross-kpa]");
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
      /* MRB-257 (6.15) — the partial pressures, in the footnote where the
         audit puts them. Still copied, never computed: `r_crossing_counter`
         derives this line from the same pair of values the side labels come
         from, so the footnote cannot disagree with the tiles above it. */
      put(kpaFoot, live.getAttribute("data-kpa"));
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
        /* MRB-257 (C1) — the head readout ticks with the stage and off the
           same fact. `data-on="switches used"` was unreachable, so the head
           read "both flows running" with a flow switched off. Sticky, to
           match the stage and the past tense of the authored label. */
        setCount(sec, 1);
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
      /* MRB-257 (C1) — the head readout counts the same thing the stage
         does. `data-format="{n} of 3 opened"` was never written, so it read
         "0 of 3 opened" after all three were opened. */
      setCount(sec, openedCount());
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
        /* MRB-257 (5.44) — "1 units" at the bottom of the slider's travel.
           `data-format-one` is the MRB-248 opt-in; no payload carries one
           yet — see HANDOFF. */
        var lFmt = (light === 1 && lightEl.getAttribute("data-format-one"))
          ? lightEl.getAttribute("data-format-one")
          : (lightEl.getAttribute("data-format") || "");
        lightEl.textContent = light === 0
          ? (lightEl.getAttribute("data-dark") || "")
          : lFmt.split("{n}").join(String(light));
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
      /* MRB-257 (C1) — the head readout, which was never written: it said
         "currently dark" beside a light readout of 100 units, on every
         state, for ever. Keyed to the LIGHT rather than to a moved flag,
         because "currently dark" is a claim about the state and not about
         the student — dragged back to zero, the ledger is dark again and
         the head should say so. */
      setCount(sec, light > 0 ? 1 : 0);
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

/* ═══ BEGIN B6 ═══ */

  /* ── B6 · Health and drugs (⊕ MRB-244) ──
     Three instruments, three wire functions, and the same discipline B4 set:
     NOTHING HERE ANIMATES AND NOTHING HERE USES A TIMER. NOTES-B6 §4 says it
     of the unit — "all DOM-only; nothing animates, nothing uses a timer, no
     canvas" — so there is no rAF loop in this section to test
     `prefers-reduced-motion` inside (MRB-220 R4), and the platform-wide
     reduced-motion rule already removes the CSS transitions these carry.

     ⚠️ AND NOTHING HERE COMPUTES A QUANTITY OF A SUBSTANCE. The unit's tone
     gate reaches into the engine: no dose, no threshold, no method, anywhere.
     Every sentence a student reads in these three was written by the author
     and shipped in the document; what these functions do is decide which of
     them is showing. */

  /* ── route-tracer (b6-01 #s-dose) ──
     ⚖️ FIVE STAGES IN ORDER, AND THE STUDENT CANNOT SKIP ONE. There is one
     advance control and it moves by exactly one. `DRUG-02` — a painkiller goes
     to the part that hurts — survives being told; it does not survive being
     walked past stage 3 on the way to stage 4.

     ⚖️ CHANGING DRUG RESETS TO STAGE 0. Design's own reset, and it is what
     stops the closing panel being reachable without its route: the panel is
     hidden unless BOTH the drug matches and the journey is complete, so there
     is no order of taps that opens nicotine's consequences having followed
     caffeine's dose.

     ⚠️ THE STOP DOES NOT UNTICK WHEN THE ROUTE IS RESTARTED. ⊕ MRB-257
     (5.29) — it used to. Design's `isDone` for this stop is `step >= 5`, a
     pure function of the state, and this comment used to defend that as
     deliberate: press "New dose" and you are mid-journey again, so the rail
     says so. The audit measured what that costs a student — complete
     caffeine, rail 2/4, then click Nicotine to explore the second of the
     four drugs the instrument's own copy invites, and the rail drops to
     0/4. Exploring is punished. MRB-208 rules the rail records
     PARTICIPATION, and `markStage` is a ratchet, so the predicate below is
     unchanged and what it can no longer do is take credit back. */
  function wireRouteTracer(sec) {
    var wrap = sec.querySelector("[data-route]");
    if (!wrap) { return; }
    var next = wrap.querySelector("[data-route-next]");
    var reset = wrap.querySelector("[data-route-reset]");
    var tabs = toArray(wrap.querySelectorAll("[data-pick]"));
    var groups = toArray(wrap.querySelectorAll("[data-for]"));
    var elses = toArray(wrap.querySelectorAll("[data-else]"));
    var steps = toArray(wrap.querySelectorAll(".ks3-route-step"));
    var total = parseInt(wrap.getAttribute("data-total"), 10) || 0;
    if (!next || !tabs.length || !total) { return; }

    var LABELS = {
      start: next.getAttribute("data-label-start") || "",
      more: next.getAttribute("data-label-more") || "",
      done: next.getAttribute("data-label-done") || ""
    };
    var drug = wrap.getAttribute("data-drug");
    var step = 0;

    function draw() {
      wrap.setAttribute("data-drug", drug);
      wrap.setAttribute("data-step", String(step));

      each(tabs, function (b) {
        b.setAttribute("aria-pressed",
          b.getAttribute("data-pick") === drug ? "true" : "false");
      });
      each(groups, function (el) {
        setHidden(el, el.getAttribute("data-for") !== drug);
      });
      /* Two conditions on one panel, and both are load-bearing: the right
         drug's consequences, and only once its route has been followed. */
      each(elses, function (el) {
        setHidden(el, el.getAttribute("data-else") !== drug || step < total);
      });
      each(steps, function (li) {
        var n = parseInt(li.getAttribute("data-step"), 10);
        var reached = step >= n;
        if (n === step) { li.setAttribute("data-state", "current"); }
        else if (reached) { li.setAttribute("data-state", "reached"); }
        else { li.removeAttribute("data-state"); }
        setHidden(li.querySelector(".ks3-route-stepbody"), !reached);
      });

      next.disabled = step >= total;
      next.textContent = step === 0
        ? LABELS.start
        : (step >= total ? LABELS.done : LABELS.more);
      setCount(sec, step);
      markStage(sec, step >= total);
    }

    each(tabs, function (b) {
      b.addEventListener("click", function () {
        var id = b.getAttribute("data-pick");
        if (id === drug) { return; }
        drug = id;
        step = 0;
        draw();
      });
    });
    next.addEventListener("click", function () {
      if (step >= total) { return; }
      step += 1;
      draw();
    });
    if (reset) {
      reset.addEventListener("click", function () { step = 0; draw(); });
    }

    draw();
  }

  /* ── the B6 plural rule ──
     ⚖️ `{s}` IS THE PLURAL SUFFIX OF THE NUMBER PLACEHOLDER IMMEDIATELY
     BEFORE IT. Two of b6-02's templates carry two numbers and two suffixes,
     and the pairing is crossed between them — "{h} hour{s} elapsed · {r}
     unit{s} left" against "{r} unit{s} still in the blood after {h}
     hour{s}." — so a single global plural would print "1 units" on one of
     them whichever number it chose. Left to right, the suffix belongs to the
     number it just followed, which is how the sentence is read. Identical to
     `_plural_fill` in build_ks3.py, and it has to stay identical: the resting
     render comes from there and every later one from here. */
  function b6Fill(tpl, vals) {
    var last = null;
    return String(tpl).replace(/\{(n|r|h|s)\}/g, function (m, key) {
      if (key === "s") { return last === 1 ? "" : "s"; }
      if (!Object.prototype.hasOwnProperty.call(vals, key)) { return m; }
      last = vals[key];
      return String(vals[key]);
    });
  }

  /* ── clearance-clock (b6-02 #s-clock) ──
     ⚖️ NO INTERVENTION CHANGES THE NUMBER OF HOURS, AND THAT IS THE
     INSTRUMENT. Not "most of them do not" — none of them does, and a student
     finds that out by trying to beat it with six things people genuinely
     believe in. This function is written so that it could not become
     otherwise: `fix` is read in exactly one place below, to decide which
     authored note is showing, and appears in no expression that produces a
     number. `hours` is `units`, computed in one line, from one quantity.

     ⚖️ THE ONE HONEST EXCEPTION IS A SENTENCE, NOT A BRANCH. *A big meal
     first* lowers the PEAK and not the clock, and Design says exactly that in
     that fix's own note. There is no code path here that treats it
     differently from the other five, and there must never be one: a special
     case would teach that one trick works.

     ⚠️ THE BAR IS `remaining / units`, NOT `remaining / max`. Design's own,
     and it means a two-unit evening and a twelve-unit evening both open full.
     The bar says how far through THIS clearance you are; the hours readout
     beside it is the only thing that says how long the evening is. */
  function wireClearanceClock(sec) {
    var wrap = sec.querySelector("[data-clearance]");
    if (!wrap) { return; }
    var waitBtn = wrap.querySelector("[data-clock-wait]");
    var resetBtn = wrap.querySelector("[data-clock-reset]");
    var unitsEl = wrap.querySelector("[data-clock-units]");
    var hoursEl = wrap.querySelector("[data-clock-hours]");
    var fillEl = wrap.querySelector("[data-clock-fill]");
    var remainEl = wrap.querySelector("[data-clock-remaining]");
    var verdictEl = wrap.querySelector("[data-clock-verdict]");
    var notes = toArray(wrap.querySelectorAll("[data-fixnote]"));
    var fixBtns = toArray(wrap.querySelectorAll("[data-fix]"));
    var addBtns = toArray(wrap.querySelectorAll("[data-add]"));
    if (!waitBtn) { return; }

    var MAX = parseInt(wrap.getAttribute("data-max"), 10) || 0;
    var T = {
      units: wrap.getAttribute("data-units-label") || "",
      hours: wrap.getAttribute("data-hours-label") || "",
      none: wrap.getAttribute("data-hours-none") || "",
      remaining: wrap.getAttribute("data-remaining-label") || "",
      wait: wrap.getAttribute("data-wait-label") || "",
      clear: wrap.getAttribute("data-clear-label") || "",
      vEmpty: wrap.getAttribute("data-verdict-empty") || "",
      vClear: wrap.getAttribute("data-verdict-clear") || "",
      vRunning: wrap.getAttribute("data-verdict-running") || ""
    };

    var units = parseInt(wrap.getAttribute("data-units"), 10) || 0;
    var hour = parseInt(wrap.getAttribute("data-hour"), 10) || 0;
    var fix = wrap.getAttribute("data-fix");
    var everRan = false;

    function draw() {
      /* ⚠️ THE WHOLE MODEL, AND `fix` IS NOT IN IT. One unit an hour: the
         hours to clear ARE the units drunk, and what remains is what has not
         yet had its hour. Three lines, one quantity, nothing to weight. */
      var remaining = Math.max(0, units - hour);
      var clear = remaining === 0;

      wrap.setAttribute("data-units", String(units));
      wrap.setAttribute("data-hour", String(hour));
      wrap.setAttribute("data-fix", fix);

      if (unitsEl) { unitsEl.textContent = b6Fill(T.units, {n: units}); }
      if (hoursEl) {
        hoursEl.textContent = units === 0 ? T.none : b6Fill(T.hours, {n: units});
      }
      if (fillEl) {
        /* MRB-257 (5.20) — normalised to the bench's own ceiling, not to the
           evening's own total. Under a label reading "Alcohol still in the
           blood", one unit drew 274px and six units drew 137px: one unit
           was twice as long as six, because every evening was being scaled
           to itself. `data-max` is the most the Add buttons can reach, so
           two evenings on this bench are now comparable by eye — which is
           the only reason to draw a bar at all. */
        var span = MAX > 0 ? MAX : units;
        fillEl.style.width =
          (span > 0 ? Math.min(100, (remaining / span) * 100) : 0)
            .toFixed(1) + "%";
      }
      if (remainEl) {
        remainEl.textContent = b6Fill(T.remaining, {h: hour, r: remaining});
      }
      /* The ONE place `fix` is read. */
      each(notes, function (p) {
        setHidden(p, p.getAttribute("data-fixnote") !== fix);
      });
      each(fixBtns, function (b) {
        b.setAttribute("aria-pressed",
          b.getAttribute("data-fix") === fix ? "true" : "false");
      });

      waitBtn.disabled = units === 0 || clear;
      /* MRB-257 (5.48) — "Blood is clear" is a statement about a person who
         drank and has finished clearing it. Pressing "Empty the glass" as a
         first action used to put it on the button about someone who has not
         had a drink; the verdict line beside it already says the honest
         thing ("Nothing drunk, nothing to clear."). */
      waitBtn.textContent = (units > 0 && clear) ? T.clear : T.wait;

      if (verdictEl) {
        verdictEl.textContent = units === 0
          ? b6Fill(T.vEmpty, {n: units, h: hour, r: remaining})
          : (clear ? b6Fill(T.vClear, {n: units, h: hour, r: remaining})
                   : b6Fill(T.vRunning, {n: units, h: hour, r: remaining}));
        setHidden(verdictEl, !everRan);
      }

      setCountState(sec, everRan ? (clear ? "clear" : "running") : "idle");
      /* Design's own `isDone`: the clock has been run. Not on load — the
         block opens with an evening already poured, and ticking for that
         would credit a student with a reading they were handed. */
      markStage(sec, everRan);
    }

    each(addBtns, function (b) {
      b.addEventListener("click", function () {
        units = Math.min(MAX, units + (parseInt(b.getAttribute("data-add"), 10) || 0));
        /* MRB-257 (5.19) — the elapsed hours STAY. This used to reset
           `hour` to 0 while keeping the gross total, so 4 units → wait 2 h
           (2 left) → add 1 unit read "0 hours elapsed · 5 units left" with
           the bar back at full: two hours of the liver's work were handed
           back. In this model the total drunk IS the total hours, so five
           units take five hours, two of which have passed and three of
           which have not — which is what all three lines now say, and what
           "one unit an hour, nothing else has a vote" means. */
        draw();
      });
    });
    each(fixBtns, function (b) {
      b.addEventListener("click", function () {
        fix = b.getAttribute("data-fix");
        draw();
      });
    });
    waitBtn.addEventListener("click", function () {
      if (units === 0 || units - hour <= 0) { return; }
      hour += 1;
      everRan = true;
      draw();
    });
    if (resetBtn) {
      resetBtn.addEventListener("click", function () {
        units = 0;
        hour = 0;
        draw();
      });
    }

    draw();
  }

  /* ── claim-check (b6-03 #s-claims) ──
     ⚖️ THE BENCH DOES NOT MARK RIGHT AND WRONG (MRB-208 R10, and Design's own
     comment on the page). There is no line below that adds a class to a fault
     button, and none that reads whether the pick was correct in order to style
     one: a button shows that it was CHOSEN, the unchosen ones dim once the
     claim is checked, and a separate cream panel NAMES the fault in a
     sentence. Only the mastery ladder marks correctness.

     ⚖️ THE REVEAL IS NEVER WITHHELD FOR A WRONG ANSWER, and the answer line
     is the CORRECT fault's text either way. A student who picked wrongly is
     shown the right fault named in full — the pool is one-to-one, so the one
     they picked was a true statement about a different claim, and that is
     worth knowing too.

     ⚖️ EVERY CLAIM KEEPS ITS OWN PICK AND ITS OWN CHECKED FLAG, over ONE
     shared fault list. Same arrangement as `wireFaultBench`, for the same
     reason: moving away from a claim and back finds it exactly as it was. */
  function wireClaimCheck(sec) {
    var wrap = sec.querySelector("[data-ccheck]");
    if (!wrap) { return; }
    var tabs = toArray(wrap.querySelectorAll("[data-pick]"));
    var groups = toArray(wrap.querySelectorAll("[data-for]"));
    var options = toArray(wrap.querySelectorAll(".ks3-ccheck-fault"));
    var reveals = toArray(wrap.querySelectorAll(".ks3-ccheck-verdict"));
    var btn = wrap.querySelector("[data-ccheck-open]");
    var tally = wrap.querySelector("[data-ccheck-tally]");
    var total = parseInt(wrap.getAttribute("data-total"), 10) || tabs.length;
    if (!tabs.length || !btn) { return; }

    var CHECK = wrap.getAttribute("data-check-label") || "";
    var CHECKED = wrap.getAttribute("data-checked-label") || "";
    var TALLY = wrap.getAttribute("data-tally") || "";
    var TALLY_DONE = wrap.getAttribute("data-tally-done") || "";
    var picks = {};
    var opened = {};
    var current = wrap.getAttribute("data-claim");

    function openedCount() {
      var n = 0, k;
      for (k in opened) { if (opened[k]) { n += 1; } }
      return n;
    }

    function draw() {
      var pick = picks[current];
      var isOpen = !!opened[current];
      var done = openedCount();

      wrap.setAttribute("data-claim", current);
      each(tabs, function (tab) {
        tab.setAttribute("aria-pressed",
          tab.getAttribute("data-pick") === current ? "true" : "false");
      });
      each(groups, function (el) {
        setHidden(el, el.getAttribute("data-for") !== current);
      });
      each(options, function (opt) {
        /* The ONLY state a fault button carries. Not is-correct, not
           is-wrong, and never both halves of a mark. */
        opt.setAttribute("aria-pressed",
          pick && opt.getAttribute("data-fault") === pick ? "true" : "false");
        opt.disabled = isOpen;
      });
      each(reveals, function (r) {
        var on = isOpen && r.getAttribute("data-verdict") === current;
        setHidden(r, !on);
        if (!on) { return; }
        var right = pick === r.getAttribute("data-answer");
        each(r.querySelectorAll("[data-word]"), function (v) {
          setHidden(v, v.getAttribute("data-word") !== (right ? "right" : "wrong"));
        });
        r.setAttribute("role", "status");
      });

      btn.disabled = isOpen || !pick;
      btn.textContent = isOpen ? CHECKED : CHECK;
      if (tally) {
        /* Counts DOWN — how many claims are still to check — and the last one
           is a sentence rather than "0 still to check". */
        tally.textContent = done >= total
          ? TALLY_DONE
          : TALLY.split("{n}").join(String(total - done))
                 .split("{total}").join(String(total));
      }
      setCount(sec, done);
      /* ⚖️ ALL FIVE. Design's own `isDone`, and it is the right reading: the
         block's argument is that five different-looking claims fail in five
         different ways, and a student who has checked one has met a claim
         rather than the comparison. */
      markStage(sec, done >= total);
    }

    each(tabs, function (tab) {
      tab.addEventListener("click", function () {
        current = tab.getAttribute("data-pick");
        draw();
      });
    });
    each(options, function (opt) {
      opt.addEventListener("click", function () {
        if (opened[current]) { return; }
        picks[current] = opt.getAttribute("data-fault");
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

/* ═══ END B6 ═══ */

/* ═══ BEGIN B5 ═══ */

  /* ── B5 · Reproduction (⊕ MRB-244) ──
     Eight instruments, THREE wire functions, and the same discipline B4 and
     B6 set: NOTHING HERE ANIMATES AND NOTHING HERE USES A TIMER. NOTES-B5 §2
     says it of the unit — "All six are DOM-only. Nothing in this unit
     animates, nothing uses a timer, and there is no canvas" — so there is no
     rAF loop in this section to test `prefers-reduced-motion` inside
     (MRB-220 R4, the b2-03 slip), and the B5 stylesheet deliberately adds no
     transition for the platform-wide rule to have to remove.

     ⚖️ THREE FUNCTIONS FOR EIGHT INSTRUMENTS, and the sharing is the point.
     Five of the eight are the SAME BLOCK — b5-01, b5-04, b5-05, b5-06 and
     b5-08 — and NOTES-B5 §6 says so in terms: "b5-05 reuses b5-04's
     instrument shape deliberately … If Code refactors either one, keep them
     identical — the repetition is the argument." Two more, b5-02 and b5-07,
     are one comparison table drawn twice so the plant and the animal sit in
     the same shape. Writing them out eight times would let them drift; one
     function each is what makes drifting impossible.

     ⚠️ AND NONE OF THESE THREE MARKS ANYTHING (MRB-196 R10). A chosen option
     shows that it was CHOSEN and takes no verdict class, no green, no red,
     ever — open or not. What names the verdict is a mono eyebrow on the cream
     panel, and it appears whichever way the pick went. Only the mastery
     ladder marks correctness. */

  /* ── the commit family (b5-01 #s-jobs · b5-04 / b5-05 #s-cross ·
     b5-06 #s-parts · b5-08 #s-sort) ──

     ⚖️ EVERY ITEM KEEPS ITS OWN PICK AND ITS OWN CHECKED FLAG, and the whole
     per-item state is in the DOM: one option list, one panel row and one
     reveal per item, all but the current one `hidden`. A student who checks
     the testes and moves to the sperm duct finds the duct uncommitted and the
     testes exactly as they left them, and coming back is a class change
     rather than a re-render.

     ⚖️ THE STOP TICKS ON ALL OF THEM. Design's own `isDone` for every one of
     these five blocks is the full count — eight structures, six substances,
     nine parts, eight specimens — and it is the right reading: the block's
     argument is the SET, not any one member of it. A student who has checked
     one has met a structure rather than the system.

     ⚖️ AND THE REVEAL IS NEVER WITHHELD FOR A WRONG PICK. It opens either
     way and names the right answer in full, which is the only thing that
     makes a wrong guess worth making. */
  function wireB5Commit(sec) {
    var w = sec.querySelector("[data-b5c]");
    if (!w) { return; }
    var tabs = toArray(w.querySelectorAll("[data-b5c-pick]"));
    var groups = toArray(w.querySelectorAll("[data-for]"));
    var opts = toArray(w.querySelectorAll(".ks3-b5c-opt"));
    var reveals = toArray(w.querySelectorAll("[data-b5c-reveal]"));
    var btn = w.querySelector("[data-b5c-check]");
    var hint = w.querySelector("[data-b5c-hint]");
    var total = parseInt(w.getAttribute("data-total"), 10) || tabs.length;
    if (!tabs.length || !btn) { return; }

    var H_IDLE = w.getAttribute("data-hint-idle") || "";
    var H_READY = w.getAttribute("data-hint-ready") || "";
    var H_DONE = w.getAttribute("data-hint-done") || "";
    var picks = {};
    var opened = {};
    var current = w.getAttribute("data-item");

    function openedCount() {
      var n = 0, k;
      for (k in opened) { if (opened[k]) { n += 1; } }
      return n;
    }

    function draw() {
      var pick = picks[current];
      var isOpen = !!opened[current];
      var done = openedCount();

      w.setAttribute("data-item", current);
      each(tabs, function (tab) {
        tab.setAttribute("aria-pressed",
          tab.getAttribute("data-b5c-pick") === current ? "true" : "false");
      });
      each(groups, function (el) {
        setHidden(el, el.getAttribute("data-for") !== current);
      });
      each(opts, function (opt) {
        var owner = opt.getAttribute("data-owner");
        /* The ONLY state an option carries. Not is-correct, not is-wrong, and
           never both halves of a mark — R10. */
        opt.setAttribute("aria-pressed",
          picks[owner] && opt.getAttribute("data-opt") === picks[owner]
            ? "true" : "false");
        opt.disabled = !!opened[owner];
      });
      each(reveals, function (r) {
        var id = r.getAttribute("data-b5c-reveal");
        var on = !!opened[id] && id === current;
        setHidden(r, !on);
        if (!on) { return; }
        var right = picks[id] === r.getAttribute("data-answer");
        each(r.querySelectorAll("[data-word]"), function (v) {
          setHidden(v,
            v.getAttribute("data-word") !== (right ? "right" : "wrong"));
        });
        r.setAttribute("role", "status");
      });

      btn.disabled = isOpen || !pick;
      if (hint) {
        hint.textContent = isOpen ? H_DONE : (pick ? H_READY : H_IDLE);
      }
      setCount(sec, done);
      markStage(sec, done >= total);
    }

    each(tabs, function (tab) {
      tab.addEventListener("click", function () {
        current = tab.getAttribute("data-b5c-pick");
        draw();
      });
    });
    each(opts, function (opt) {
      opt.addEventListener("click", function () {
        var owner = opt.getAttribute("data-owner");
        if (opened[owner]) { return; }
        picks[owner] = opt.getAttribute("data-opt");
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

  /* ── the comparison rows (b5-02 #s-compare · b5-07 #s-becomes) ──

     ⚖️ THE WHOLE ROW IS THE BUTTON — NOTES-B5 §2.5: "the whole row is the
     button, as in `gamete-compare`. No separate chevron control." So there is
     one control per row and it is the row.

     ⚠️ THE COUNT IS OF ROWS EVER OPENED, NOT OF ROWS CURRENTLY OPEN, and it
     is Design's own semantics rather than a convenience: `open` is a map whose
     keys are never deleted, so `Object.keys(s.open).length` counts every row
     the student has touched. Counting the open ones would untick the rail stop
     when a student tidied up after themselves, which is a rail that punishes
     reading twice. */
  function wireCompareRows(sec) {
    var w = sec.querySelector("[data-cmprows]");
    if (!w) { return; }
    var btns = toArray(w.querySelectorAll("[data-cmp-open]"));
    if (!btns.length) { return; }
    var total = parseInt(w.getAttribute("data-total"), 10) || btns.length;
    var everOpened = {};

    function count() {
      var n = 0, k;
      for (k in everOpened) { if (everOpened[k]) { n += 1; } }
      return n;
    }

    each(btns, function (b) {
      var id = b.getAttribute("data-cmp-open");
      var row = w.querySelector('[data-cmp-row="' + id + '"]');
      var why = w.querySelector('[data-cmp-why="' + id + '"]');
      b.addEventListener("click", function () {
        var open = b.getAttribute("aria-pressed") !== "true";
        b.setAttribute("aria-pressed", open ? "true" : "false");
        setHidden(why, !open);
        if (row) {
          if (open) { row.setAttribute("data-open", ""); }
          else { row.removeAttribute("data-open"); }
        }
        if (why) { why.setAttribute("role", "status"); }
        if (open) { everOpened[id] = true; }
        var n = count();
        setCount(sec, n);
        markStage(sec, n >= total);
      });
    });
  }

  /* ── cycle-dial (b5-03 #s-dial) ──

     ⚖️ THE RELEASE DAY IS DERIVED HERE TOO — `length - luteal`, every draw,
     and there is nowhere in the markup it could have been stored. NOTES-B5
     §2.1: "the release day is derived as `length − 14`, never stored. That is
     the instrument's whole argument, and hard-coding release days would
     destroy it." A lookup table of 7 / 14 / 21 would behave identically and
     would teach that day 14 is a fact about people — `REPRO-05`, the
     misconception this lesson exists to confront.

     ⚖️ THE STOP TICKS ON TWO DIFFERENT LENGTHS SEEN, NOT ON REACHING THE END
     OF THE SLIDER. §2.1 again: "Rail credit is given for viewing two
     different lengths, not for reaching the end of the slider." Walking all
     28 days proves nothing; watching the alert line MOVE when the length
     changes is the lesson.

     ⚠️ AND THE OPENING LENGTH IS ALREADY SEEN. Design's state is
     `seen: { 28: true }`, so the readout opens at "1 of 3 lengths tried".
     Nothing is TICKED on load — the stop needs two — but the counter does not
     open at zero, which is why `_KIND_HEAD_START` fills the resting number in
     the built HTML as well.

     ⚠️ THE DAY IS CLAMPED WHEN THE LENGTH SHORTENS. A student on day 30 of a
     35-day cycle who switches to 21 days would otherwise be standing on a day
     that no longer exists, and the marker would sit off the end of its own
     track. */
  function wireCycleDial(sec) {
    var w = sec.querySelector("[data-dial]");
    if (!w) { return; }
    var chips = toArray(w.querySelectorAll("[data-dial-len]"));
    var slider = w.querySelector("[data-dial-day]");
    if (!chips.length || !slider) { return; }

    var LUTEAL = parseInt(w.getAttribute("data-luteal"), 10);
    var SHED = parseInt(w.getAttribute("data-shed"), 10);
    var CREDIT = parseInt(w.getAttribute("data-credit"), 10) || 2;
    var DAY_FMT = w.getAttribute("data-day-format") || "";
    var REL_FMT = w.getAttribute("data-track-release") || "";
    var LAST_FMT = w.getAttribute("data-track-last") || "";
    var NOTE_PROMPT = w.getAttribute("data-note-prompt") || "";

    var shedEl = w.querySelector("[data-dial-shed]");
    var relEl = w.querySelector("[data-dial-release]");
    var markEl = w.querySelector("[data-dial-marker]");
    var relLabel = w.querySelector("[data-dial-rellabel]");
    var lastLabel = w.querySelector("[data-dial-lastlabel]");
    var dayRead = w.querySelector("[data-dial-dayread]");
    var phaseRead = w.querySelector("[data-dial-phaseread]");
    var ovaryEl = w.querySelector("[data-dial-ovary]");
    var uterusEl = w.querySelector("[data-dial-uterus]");
    var noteEl = w.querySelector("[data-dial-note]");

    var phases = {};
    each(w.querySelectorAll("[data-dial-phase]"), function (p) {
      phases[p.getAttribute("data-dial-phase")] = {
        label: p.getAttribute("data-label") || "",
        ovary: p.getAttribute("data-ovary") || "",
        uterus: p.getAttribute("data-uterus") || ""
      };
    });
    var notes = {};
    each(chips, function (c) {
      notes[c.getAttribute("data-dial-len")] = c.getAttribute("data-note") || "";
    });

    var length = parseInt(w.getAttribute("data-length"), 10);
    var day = parseInt(w.getAttribute("data-day"), 10) || 1;
    /* Design's own opening state: the length the block opens on has been
       seen, because the student is looking at it. */
    var seen = {};
    seen[String(length)] = true;

    function seenCount() {
      var n = 0, k;
      for (k in seen) { if (seen[k]) { n += 1; } }
      return n;
    }

    function pct(n) { return ((n - 0.5) / length) * 100; }

    function phaseAt(n, release) {
      if (n <= SHED) { return "shed"; }
      if (n < release) { return "build"; }
      if (n === release) { return "release"; }
      return "held";
    }

    var prev = w.querySelector("[data-dial-prev]");
    var next = w.querySelector("[data-dial-next]");

    function draw() {
      /* ⚖️ DERIVED. Not looked up, not stored, not cached. */
      var release = length - LUTEAL;
      if (day > length) { day = length; }
      if (day < 1) { day = 1; }

      each(chips, function (c) {
        c.setAttribute("aria-pressed",
          parseInt(c.getAttribute("data-dial-len"), 10) === length
            ? "true" : "false");
      });
      if (shedEl) { shedEl.style.width = (SHED / length) * 100 + "%"; }
      if (relEl) { relEl.style.left = pct(release) + "%"; }
      if (markEl) { markEl.style.left = pct(day) + "%"; }
      if (relLabel) {
        relLabel.textContent = REL_FMT.split("{n}").join(String(release));
      }
      if (lastLabel) {
        lastLabel.textContent = LAST_FMT.split("{n}").join(String(length));
      }
      slider.max = String(length);
      if (slider.value !== String(day)) { slider.value = String(day); }
      if (dayRead) {
        dayRead.textContent = DAY_FMT.split("{n}").join(String(day));
      }
      var ph = phases[phaseAt(day, release)] || { label: "", ovary: "", uterus: "" };
      if (phaseRead) { phaseRead.textContent = ph.label; }
      if (ovaryEl) { ovaryEl.textContent = ph.ovary; }
      if (uterusEl) { uterusEl.textContent = ph.uterus; }

      var n = seenCount();
      if (noteEl) {
        noteEl.textContent = n < CREDIT
          ? NOTE_PROMPT
          : (notes[String(length)] || NOTE_PROMPT);
      }
      /* MRB-257 (5.48) — the day steppers stop at the ends of the cycle.
         They stayed enabled and focusable at day 1 and at the last day, so
         five presses produced no DOM change at all: an enabled control that
         does nothing, which reads as a broken instrument rather than as a
         boundary. `draw()` already clamps, so this is the clamp made
         visible. */
      if (prev) { prev.disabled = day <= 1; }
      if (next) { next.disabled = day >= length; }
      w.setAttribute("data-length", String(length));
      w.setAttribute("data-day", String(day));
      setCount(sec, n);
      markStage(sec, n >= CREDIT);
    }

    each(chips, function (c) {
      c.addEventListener("click", function () {
        length = parseInt(c.getAttribute("data-dial-len"), 10);
        seen[String(length)] = true;
        draw();
      });
    });
    /* MRB-210 §2 — bound on `input` AND `change`, through the one helper. */
    onRange(slider, function () {
      day = parseInt(slider.value, 10) || 1;
      draw();
    });
    if (prev) {
      prev.addEventListener("click", function () { day -= 1; draw(); });
    }
    if (next) {
      next.addEventListener("click", function () { day += 1; draw(); });
    }

    draw();
  }

/* ═══ END B5 ═══ */

/* ═══ BEGIN B7 ═══ */

  /* ── B7 · Photosynthesis (⊕ MRB-245) ──
     Four instruments, four wire functions, and NOTHING SHARED — because
     nothing in this unit is the same block twice. Where B5 had one commit
     chassis five times over and NOTES-B5 §6 made the repetition the argument,
     B7's four benches ask four different questions: take one thing away, tune
     two readouts against each other, break a working method, and walk a chain
     backwards. A shared chassis here would be a coincidence enforced.

     ⚠️ NOTHING HERE ANIMATES AND NOTHING HERE USES A TIMER. NOTES-B7 §3 says
     it of the unit and all four pages bear it out, so there is no rAF loop in
     this section to test `prefers-reduced-motion` inside (MRB-220 R4, the
     b2-03 slip), and the B7 stylesheet deliberately adds no transition for the
     platform-wide reduced-motion rule to have to remove.

     ⚠️ AND NONE OF THESE FOUR MARKS ANYTHING (MRB-196 R10). A chosen dial
     setting shows that it was CHOSEN — the alert ground Design paints — and
     takes no verdict class, no green, no red, ever. What these benches show is
     a CONSEQUENCE: the starch a leaf did or did not make, the habitat a leaf
     could live in, what a broken method licenses you to conclude, and where a
     meal came from. None of that is a mark on the student. Only the mastery
     ladder marks correctness.

     ⚠️ THE STAGE PREDICATE IS MONOTONIC ON ALL FOUR, and on b7-02 that is a
     deliberate divergence from Design. Her `isDone('s-tuner')` is `s.moved`,
     and `Start again` sets `moved: false` — so the rail stop UNTICKS when a
     student tidies up after themselves. MRB-208 ruled the rail records
     participation; B5's compare rows count rows EVER opened for the same
     reason. So `everMoved` drives the rail while `moved` drives the counter,
     which is what keeps Design's own readout ("nothing changed yet" after a
     reset) intact without a rail that punishes starting over. */

  /* ── reactant-remover (b7-01 #s-bench) ──

     ⚖️ RATE IS THE PRODUCT OF THE FOUR DIALS, so removing any one takes it to
     zero. Not a weighted sum: the four are jointly necessary, and a sum would
     let a student switch the light off and still make three-quarters of the
     starch.

     ⚖️ SEVEN BRANCHES, AND THE ORDER BELOW IS DESIGN'S. Each single-dial
     branch is guarded by exactly one thing missing, so at most one can match
     and precedence cannot change an outcome — unlike b7-03, where it is the
     whole pedagogy. `< 50` is Design's own threshold for the faint reading and
     is kept as she wrote it. */
  function wireReactantRemover(sec) {
    var w = sec.querySelector("[data-rr]");
    if (!w) { return; }
    var opts = toArray(w.querySelectorAll(".ks3-rr-opt"));
    var setupEl = w.querySelector("[data-rr-setup]");
    var rateEl = w.querySelector("[data-rr-rate]");
    var testBtn = w.querySelector("[data-rr-test]");
    var resetBtn = w.querySelector("[data-rr-reset]");
    var readouts = toArray(w.querySelectorAll("[data-rr-readout]"));
    var bars = toArray(w.querySelectorAll("[data-rr-bar]"));
    var panels = toArray(w.querySelectorAll("[data-rr-verdict]"));
    if (!opts.length || !testBtn) { return; }

    var ALL = w.getAttribute("data-all-present") || "";
    var PREFIX = w.getAttribute("data-missing-prefix") || "";
    var RATE_SUFFIX = w.getAttribute("data-rate-suffix") || "";
    var TEST = w.getAttribute("data-test-label") || "";
    var TESTED = w.getAttribute("data-tested-label") || "";

    /* The opening state IS the markup: the bench opens intact and every dial's
       first option is already pressed, so there is nothing to seed here and no
       second copy of the defaults to fall out of step with the page. */
    var start = {}, order = [], names = {};
    each(opts, function (o) {
      var d = o.getAttribute("data-dial");
      if (order.indexOf(d) < 0) {
        order.push(d);
        start[d] = o.getAttribute("data-opt");
        var label = w.querySelector('.ks3-rr-dialname[data-dial="' + d + '"]');
        names[d] = label ? label.textContent : d;
      }
    });
    var picks = {}, k;
    for (k in start) {
      if (Object.prototype.hasOwnProperty.call(start, k)) { picks[k] = start[k]; }
    }
    var tested = false, everTested = false;

    function factor(dial) {
      for (var i = 0; i < opts.length; i++) {
        if (opts[i].getAttribute("data-dial") === dial &&
            opts[i].getAttribute("data-opt") === picks[dial]) {
          return parseFloat(opts[i].getAttribute("data-f"));
        }
      }
      return 1;
    }

    /* Design lower-cases the dial names inside the sentence — "Missing: light"
       — because the name is a heading elsewhere and a clause here. */
    /* MRB-257 (5.32) — WHAT IS MISSING IS NAMED BY THE OPTION, not by the
       dial, where the option says something different. Three dials name the
       thing they remove ("light", "carbon dioxide", "water") but the fourth
       is "The leaf tested", and its zero option is "White part of a
       variegated leaf" — so choosing it printed "Missing: the leaf tested"
       with the leaf plainly present. What is missing is chlorophyll, which
       is the control's entire teaching point, and the same wrong name leaked
       into the multi-fault line ("carbon dioxide and the leaf tested").
       `data-missing` on the option carries the true name; no payload ships
       one yet, so this falls back to the dial name — see HANDOFF. */
    function missingName(dial) {
      for (var i = 0; i < opts.length; i++) {
        if (opts[i].getAttribute("data-dial") === dial &&
            opts[i].getAttribute("data-opt") === picks[dial]) {
          var authored = opts[i].getAttribute("data-missing");
          if (authored) { return authored; }
        }
      }
      return (names[dial] || dial).toLowerCase();
    }

    function missing() {
      var out = [], i;
      for (i = 0; i < order.length; i++) {
        if (factor(order[i]) === 0) { out.push(missingName(order[i])); }
      }
      return out;
    }

    function branchFor(rate, ratePct, gone) {
      if (gone.length === 1) {
        for (var i = 0; i < order.length; i++) {
          if (factor(order[i]) === 0) { return order[i]; }
        }
      }
      if (rate === 0) { return "multiple"; }
      if (ratePct < 50) { return "low"; }
      return "none";
    }

    function draw() {
      var rate = 1, i;
      for (i = 0; i < order.length; i++) { rate *= factor(order[i]); }
      var ratePct = Math.round(rate * 100);
      var gone = missing();

      each(opts, function (o) {
        o.setAttribute("aria-pressed",
          picks[o.getAttribute("data-dial")] === o.getAttribute("data-opt")
            ? "true" : "false");
      });
      if (setupEl) {
        setupEl.textContent = gone.length ? (PREFIX + gone.join(", ")) : ALL;
      }
      if (rateEl) { rateEl.textContent = ratePct + RATE_SUFFIX; }

      each(readouts, function (el) {
        var scale = parseFloat(el.getAttribute("data-scale"));
        var zero = el.getAttribute("data-zero") || "";
        var suffix = el.getAttribute("data-suffix") || "";
        if (ratePct === 0) { el.textContent = zero; return; }
        var value = Math.round(rate * scale);
        el.textContent = value +
          (/^[A-Za-z0-9]/.test(suffix) ? " " : "") + suffix;
      });
      /* The BAR is the rate percentage on all three, independent of `scale` —
         Design's own arithmetic, and it is what says the three readouts are
         three views of one number. */
      each(bars, function (b) { b.style.width = ratePct + "%"; });

      var branch = branchFor(rate, ratePct, gone);
      each(panels, function (p) {
        setHidden(p, !tested || p.getAttribute("data-rr-verdict") !== branch);
      });
      if (tested) {
        var open = w.querySelector('[data-rr-verdict="' + branch + '"]');
        if (open) {
          /* `{missing}` is filled from the template the paragraph itself
             shipped with, cached on first read. One copy of the string in the
             bytes, and the un-filled form only ever exists inside a panel that
             is `hidden`. */
          var why = open.querySelector(".ks3-rr-why");
          if (why) {
            if (why.getAttribute("data-tmpl") === null) {
              why.setAttribute("data-tmpl", why.innerHTML);
            }
            why.innerHTML = why.getAttribute("data-tmpl")
              .split("{missing}").join(gone.join(" and "));
          }
          open.setAttribute("role", "status");
        }
      }

      testBtn.textContent = tested ? TESTED : TEST;
      testBtn.disabled = tested;
      setCountState(sec, everTested ? "after" : "before");
      markStage(sec, everTested);
    }

    each(opts, function (o) {
      o.addEventListener("click", function () {
        picks[o.getAttribute("data-dial")] = o.getAttribute("data-opt");
        /* Turning a dial un-tests the leaf: the verdict on screen belonged to
           the jar as it was. `everTested` is untouched — the stop stays
           ticked, because the student HAS run the test. */
        tested = false;
        draw();
      });
    });
    testBtn.addEventListener("click", function () {
      tested = true;
      everTested = true;
      draw();
    });
    if (resetBtn) {
      resetBtn.addEventListener("click", function () {
        var key;
        for (key in start) {
          if (Object.prototype.hasOwnProperty.call(start, key)) {
            picks[key] = start[key];
          }
        }
        tested = false;
        draw();
      });
    }

    draw();
  }

  /* ── leaf-tuner (b7-02 #s-tuner) ──

     ⚖️ THE CASCADE IS SHIPPED, NOT WRITTEN TWICE. `data-rules` is the ordered
     list `build_ks3.py` used to decide which verdict the OPENING leaf earns,
     so the static page and the live page cannot disagree about which habitat a
     leaf can live in. There is no expression to parse: a rule is a set of
     bounds and this is four comparisons.

     ⚖️ AND THE BAR IS THE PERCENTAGE HALVED, CLAMPED AT 100 — a full bar means
     200% of an oak leaf. Design's arithmetic, and it is the only reason the
     opening leaf's water bar can be seen to be off the end of the scale. */
  function wireLeafTuner(sec) {
    var w = sec.querySelector("[data-lt]");
    if (!w) { return; }
    var opts = toArray(w.querySelectorAll(".ks3-lt-opt"));
    var oakBtn = w.querySelector("[data-lt-oak]");
    var resetBtn = w.querySelector("[data-lt-reset]");
    var panels = toArray(w.querySelectorAll("[data-lt-verdict]"));
    if (!opts.length) { return; }

    var rules = [], start = {}, oak = {};
    try { rules = JSON.parse(w.getAttribute("data-rules") || "[]"); } catch (x) {}
    try { start = JSON.parse(w.getAttribute("data-start") || "{}"); } catch (x) {}
    try { oak = JSON.parse(w.getAttribute("data-oak") || "{}"); } catch (x) {}
    if (!rules.length) { return; }

    var picks = {}, order = [], k;
    each(opts, function (o) {
      var d = o.getAttribute("data-dial");
      if (order.indexOf(d) < 0) { order.push(d); }
    });
    function apply(preset) {
      for (k in preset) {
        if (Object.prototype.hasOwnProperty.call(preset, k)) {
          picks[k] = preset[k];
        }
      }
    }
    apply(start);
    var moved = false, everMoved = false;

    function factor(dial, key) {
      for (var i = 0; i < opts.length; i++) {
        if (opts[i].getAttribute("data-dial") === dial &&
            opts[i].getAttribute("data-opt") === picks[dial]) {
          return parseFloat(opts[i].getAttribute("data-" + key));
        }
      }
      return 1;
    }

    function product(key) {
      var out = 1, i;
      for (i = 0; i < order.length; i++) { out *= factor(order[i], key); }
      return out;
    }

    /* MRB-257 (5.52) — the bar's SCALE, measured off the dials rather than
       assumed. Both bars were `min(100, pct / 2)`, which saturates at 200%,
       and the water loss reaches 363%: moving a dial took the readout from
       363% to 242% while the bar sat at 100% both times — a control with no
       visible effect on the graphic it drives. The largest product the dials
       can actually produce is the top of the track, so every setting is
       somewhere on it and every press moves something. */
    function maxProduct(key) {
      var out = 1, i, j, best, f;
      for (i = 0; i < order.length; i++) {
        best = 0;
        for (j = 0; j < opts.length; j++) {
          if (opts[j].getAttribute("data-dial") !== order[i]) { continue; }
          f = parseFloat(opts[j].getAttribute("data-" + key));
          if (!isNaN(f) && f > best) { best = f; }
        }
        out *= best;
      }
      return out;
    }

    var MAX_R = maxProduct("r") * 100;
    var MAX_W = maxProduct("w") * 100;

    function verdictFor(ratePct, waterPct) {
      for (var i = 0; i < rules.length; i++) {
        var rule = rules[i], ok = true, key;
        for (key in rule) {
          if (!Object.prototype.hasOwnProperty.call(rule, key)) { continue; }
          if (key === "id") { continue; }
          var value = key.indexOf("rate") === 0 ? ratePct : waterPct;
          var bound = rule[key], test = key.split("_")[1];
          if (test === "gt" && !(value > bound)) { ok = false; }
          else if (test === "gte" && !(value >= bound)) { ok = false; }
          else if (test === "lt" && !(value < bound)) { ok = false; }
          else if (test === "lte" && !(value <= bound)) { ok = false; }
        }
        if (ok) { return rule.id; }
      }
      return rules[rules.length - 1].id;
    }

    function draw() {
      var ratePct = Math.round(product("r") * 100);
      var waterPct = Math.round(product("w") * 100);

      each(opts, function (o) {
        o.setAttribute("aria-pressed",
          picks[o.getAttribute("data-dial")] === o.getAttribute("data-opt")
            ? "true" : "false");
      });
      each(w.querySelectorAll("[data-lt-readout]"), function (el) {
        var id = el.getAttribute("data-lt-readout");
        var pct = id === "rate" ? ratePct : waterPct;
        var suffix = el.getAttribute("data-suffix") || "";
        el.textContent = pct +
          (/^[A-Za-z0-9]/.test(suffix) ? " " : "") + suffix;
      });
      each(w.querySelectorAll("[data-lt-bar]"), function (b) {
        var isRate = b.getAttribute("data-lt-bar") === "rate";
        var pct = isRate ? ratePct : waterPct;
        var top = isRate ? MAX_R : MAX_W;
        b.style.width =
          (top > 0 ? Math.min(100, (pct / top) * 100) : 0).toFixed(1) + "%";
      });

      var id = verdictFor(ratePct, waterPct);
      each(panels, function (p) {
        setHidden(p, p.getAttribute("data-lt-verdict") !== id);
      });

      /* Design's own readout: the two percentages once the leaf has been
         touched, and her fixed sentence before it. `moved` follows her and
         resets with `Start again`; `everMoved` drives the rail, which does
         not — see the section note. */
      setCount(sec, moved ? 1 : 0, { rate: ratePct, water: waterPct });
      markStage(sec, everMoved);
    }

    each(opts, function (o) {
      o.addEventListener("click", function () {
        picks[o.getAttribute("data-dial")] = o.getAttribute("data-opt");
        moved = true;
        everMoved = true;
        draw();
      });
    });
    if (oakBtn) {
      oakBtn.addEventListener("click", function () {
        apply(oak);
        moved = true;
        everMoved = true;
        draw();
      });
    }
    if (resetBtn) {
      resetBtn.addEventListener("click", function () {
        apply(start);
        moved = false;
        draw();
      });
    }

    draw();
  }

  /* ── method-breaker (b7-03 #s-bench) ──

     ⚖️ PRECEDENCE IS READ FROM THE PAGE AND IT IS THE PEDAGOGY. Safety first —
     a naked flame stops the bench outright — then the faults that DESTROY the
     result, then the ones that only OBSCURE it. Report "the leaf crumbled"
     ahead of "you skipped the destarching" and the bench has taught that a torn
     leaf and an undatable result are the same size of mistake.

     ⚠️ THE SUB-STEP DIMS WITH ITS PARENT. Skip the ethanol and there is
     nothing to heat, so there is no fire to have — which is why the flame
     branch's own condition names the ethanol step as well as the heat one, and
     why the row goes to `.45`. Both fall out of `data-parent`, which
     `build_ks3.py` derived from the authored step number `3b`. */
  function wireMethodBreaker(sec) {
    var w = sec.querySelector("[data-mb]");
    if (!w) { return; }
    var opts = toArray(w.querySelectorAll(".ks3-mb-opt"));
    var rows = toArray(w.querySelectorAll(".ks3-mb-step"));
    var runBtn = w.querySelector("[data-mb-run]");
    var resetBtn = w.querySelector("[data-mb-reset]");
    var panels = toArray(w.querySelectorAll("[data-mb-verdict]"));
    if (!opts.length || !runBtn) { return; }

    var precedence = [], conditions = {}, full = {};
    try {
      precedence = JSON.parse(w.getAttribute("data-precedence") || "[]");
      conditions = JSON.parse(w.getAttribute("data-conditions") || "{}");
      full = JSON.parse(w.getAttribute("data-full") || "{}");
    } catch (x) { return; }

    var RUN = w.getAttribute("data-run-label") || "";
    var RUN_DONE = w.getAttribute("data-run-done-label") || "";

    var picks = {}, k;
    function reset() {
      for (k in full) {
        if (Object.prototype.hasOwnProperty.call(full, k)) { picks[k] = full[k]; }
      }
    }
    reset();
    var ran = false, everRan = false;

    function outcome() {
      for (var i = 0; i < precedence.length; i++) {
        var branch = precedence[i], cond = conditions[branch] || [], ok = true;
        for (var j = 0; j < cond.length; j++) {
          if (picks[cond[j].step] !== cond[j].is) { ok = false; }
        }
        if (ok && cond.length) { return branch; }
      }
      return "full";
    }

    /* MRB-257 (5.31) — a SKIP is a step not done at all, and that is not the
       same as a step done differently. `heat` offers "water bath" or "Bunsen,
       directly": both heat the ethanol, so choosing the Bunsen skips nothing
       — it is a method choice, and a dangerous one, which is why it still
       takes its own verdict branch. Counting any pick that differed from the
       full method read "1 step skipped" over a method with every step in it,
       and "2 steps skipped" for one real skip plus the Bunsen.
       "no" is the payload's own word for an omitted step and never appears
       in `data-full`; `data-skip` on the option overrides it if a future
       bench needs a different vocabulary. */
    function isSkip(step, pick) {
      if (pick === full[step]) { return false; }
      var btn = w.querySelector('.ks3-mb-opt[data-step="' + step +
        '"][data-opt="' + pick + '"]');
      if (btn && btn.hasAttribute("data-skip")) {
        return btn.getAttribute("data-skip") === "1";
      }
      return pick === "no";
    }

    function faults() {
      var n = 0, key;
      for (key in full) {
        if (Object.prototype.hasOwnProperty.call(full, key) &&
            isSkip(key, picks[key])) { n += 1; }
      }
      return n;
    }

    function draw() {
      each(opts, function (o) {
        o.setAttribute("aria-pressed",
          picks[o.getAttribute("data-step")] === o.getAttribute("data-opt")
            ? "true" : "false");
      });
      /* A sub-step whose parent was skipped is dimmed, not disabled: a student
         may still press it, and the bench simply has no fire to report. */
      each(rows, function (r) {
        var parent = r.getAttribute("data-parent");
        if (!parent) { return; }
        if (picks[parent] !== full[parent]) { r.setAttribute("data-dim", ""); }
        else { r.removeAttribute("data-dim"); }
      });

      var branch = outcome();
      each(panels, function (p) {
        setHidden(p, !ran || p.getAttribute("data-mb-verdict") !== branch);
      });
      if (ran) {
        var open = w.querySelector('[data-mb-verdict="' + branch + '"]');
        if (open) { open.setAttribute("role", "status"); }
      }

      runBtn.textContent = ran ? RUN_DONE : RUN;
      runBtn.disabled = ran;

      /* Four named states, and the two that count carry `{n}`. Before the
         first run the readout says so; after it, it reports the method
         currently set, which is what makes the counter answer "what am I about
         to run" rather than "what did I run once". */
      var n = faults();
      if (!everRan) { setCountState(sec, "idle"); }
      else if (!n) { setCountState(sec, "full"); }
      else { setCountState(sec, n === 1 ? "one" : "many", { n: n }); }
      markStage(sec, everRan);
    }

    each(opts, function (o) {
      o.addEventListener("click", function () {
        picks[o.getAttribute("data-step")] = o.getAttribute("data-opt");
        /* Changing the method un-runs it: the result on screen belonged to the
           method as it was. `everRan` is untouched. */
        ran = false;
        draw();
      });
    });
    runBtn.addEventListener("click", function () {
      ran = true;
      everRan = true;
      draw();
    });
    if (resetBtn) {
      resetBtn.addEventListener("click", function () {
        reset();
        ran = false;
        draw();
      });
    }

    draw();
  }

  /* ── trace-it-back (b7-04 #s-trace) ──

     ⚖️ THE CHAIN IS WALKED BACKWARDS, ONE LINK PER PRESS, and the verdict
     lands only when it is complete. Every link is drawn from the start and
     only its NOTE arrives, so a student reads how far there is to go before
     taking a step — which is the sentence the prompt makes to them: the number
     of steps changes and the destination does not.

     ⚠️ THE DENOMINATOR MOVES WITH THE TAB. Six chains of three, four and five
     links, so `data-total` on the head counter is rewritten per food; the
     shipped bytes carry the FIRST food's length so the resting page is not
     "step 1 of 0". And Design's own readout says "chain traced" from the
     moment one chain has been walked, on every food after it, which is
     `everArrived` rather than a count reaching its total. */
  function wireTraceItBack(sec) {
    var w = sec.querySelector("[data-tb]");
    if (!w) { return; }
    var tabs = toArray(w.querySelectorAll("[data-tb-food]"));
    var foods = toArray(w.querySelectorAll("[data-tb-panel]"));
    var backBtn = w.querySelector("[data-tb-back]");
    var resetBtn = w.querySelector("[data-tb-reset]");
    if (!tabs.length || !foods.length || !backBtn) { return; }

    var STEP = w.getAttribute("data-step-label") || "";
    var DONE = w.getAttribute("data-done-label") || "";
    var IDLE = w.getAttribute("data-steps-idle") || "";
    var STEPS_DONE = w.getAttribute("data-steps-done") || "";

    var current = w.getAttribute("data-food");
    var shown = 1, everArrived = false;

    function panel() {
      return w.querySelector('[data-tb-panel="' + current + '"]');
    }
    function total() {
      var p = panel();
      return p ? (parseInt(p.getAttribute("data-total"), 10) || 1) : 1;
    }

    function draw() {
      var t = total(), arrived = shown >= t;

      each(tabs, function (tab) {
        tab.setAttribute("aria-pressed",
          tab.getAttribute("data-tb-food") === current ? "true" : "false");
      });
      each(foods, function (f) {
        setHidden(f, f.getAttribute("data-tb-panel") !== current);
      });

      var p = panel();
      if (p) {
        each(p.querySelectorAll(".ks3-tb-link"), function (li) {
          var i = parseInt(li.getAttribute("data-i"), 10);
          var on = i < shown;
          if (on) { li.setAttribute("data-shown", ""); }
          else { li.removeAttribute("data-shown"); }
          setHidden(li.querySelector(".ks3-tb-note"), !on);
        });
        var steps = p.querySelector("[data-tb-steps]");
        if (steps) {
          steps.textContent = arrived
            ? STEPS_DONE.split("{n}").join(String(t - 1))
            : IDLE;
        }
        var verdict = p.querySelector("[data-tb-verdict]");
        setHidden(verdict, !arrived);
        if (verdict && arrived) { verdict.setAttribute("role", "status"); }
      }

      backBtn.textContent = arrived ? DONE : STEP;
      backBtn.disabled = arrived;

      /* The head counter's denominator is this food's chain length.
         MRB-257 (5.34) — the READOUT reports where the student is standing,
         `everArrived` reports what they have done, and the two are not the
         same thing. Feeding the sticky flag into the count made `data-full`
         fire at the top of the count for ever: "Start again", or switching
         food, reset the bench to link one and the head still read "chain
         traced" — on Salmon it said so at step 1 of 5. The RAIL stays
         sticky (MRB-208, and `markStage` is a ratchet): what the student
         found out is not un-found by starting a second chain. */
      var count = sec.querySelector("[data-count]");
      if (count) { count.setAttribute("data-total", String(t)); }
      setCount(sec, Math.min(shown, t));
      markStage(sec, everArrived);
    }

    each(tabs, function (tab) {
      tab.addEventListener("click", function () {
        current = tab.getAttribute("data-tb-food");
        w.setAttribute("data-food", current);
        shown = 1;
        draw();
      });
    });
    backBtn.addEventListener("click", function () {
      shown = Math.min(total(), shown + 1);
      if (shown >= total()) { everArrived = true; }
      draw();
    });
    if (resetBtn) {
      resetBtn.addEventListener("click", function () { shown = 1; draw(); });
    }

    draw();
  }

/* ═══ END B7 ═══ */

/* ═══ BEGIN B8 ═══ */

  /* ── B8 · Respiration (⊕ MRB-248) ──
     Five instruments, five wire functions, and NOTHING SHARED — because
     nothing in this unit is the same block twice. The five ask five different
     questions: weigh both sides of a reaction, cut the oxygen to five
     different cells, run and then stop and watch what does not stop, set four
     dials and read what you have made, and decide which route is running. A
     shared chassis here would be a coincidence enforced.

     ⚠️ NOTHING HERE ANIMATES AND NOTHING HERE USES A TIMER. No canvas, no
     `requestAnimationFrame`, no `setTimeout`, no `setInterval` — grepped
     across all five approved pages and zero on every term. So there is no rAF
     loop in this section to test `prefers-reduced-motion` inside (MRB-220 R4,
     the b2-03 slip), and the B8 stylesheet deliberately adds no transition for
     the platform-wide reduced-motion rule to have to remove.

     ⚠️ AND NONE OF THESE FIVE MARKS ANYTHING (MRB-196 R10). A chosen tab shows
     that it was CHOSEN — the alert ground Design paints — and takes no verdict
     class, no green, no red, ever. What these benches show is a CONSEQUENCE:
     what a reaction must take in and give out, what a cell loses when its
     oxygen goes, what the breathing rate does after the running stops, what
     four dials have made, and which route the situation is running. Only the
     mastery ladder marks correctness.

     ⚠️ THE STAGE PREDICATE IS MONOTONIC ON ALL FIVE. Every one of them ticks
     on something the student HAS done and never unticks — MRB-208 ruled the
     rail records participation. */

  /* ── mass-ledger (b8-01 #s-bench) ──

     ⚖️ EVERY PRINTED FIGURE IS DERIVED FROM ONE PER-GRAM MODEL, which is why
     the two totals agree at every amount rather than at the four somebody
     checked. `data-factors` is the same map `build_ks3.py` used for the
     resting render, so the static page and the live page cannot come to
     different arithmetic.

     ⚖️ AND THE ENERGY IS NOT IN EITHER TOTAL. It is computed from its own
     per-gram figure, printed on the same row, and never added to anything.
     That separation is the argument the whole block exists to make.

     ⚠️ `_b8_group` RATHER THAN `toLocaleString()`. Design writes the latter,
     which is the browser's locale and not ours — a student whose machine is
     set to a European locale would read `1.404 kJ` for one thousand four
     hundred and four. The grouping is authored and applied explicitly at both
     ends. */
  function wireMassLedger(sec) {
    var w = sec.querySelector("[data-ml]");
    if (!w) { return; }
    var tabs = toArray(w.querySelectorAll(".ks3-ml-tab"));
    var runBtn = w.querySelector("[data-ml-run]");
    var panel = w.querySelector("[data-ml-exitspanel]");
    var nameEl = w.querySelector("[data-ml-name]");
    var noteEl = w.querySelector("[data-ml-note]");
    var rows = toArray(w.querySelectorAll("[data-ml-row]"));
    var totals = toArray(w.querySelectorAll("[data-ml-total]"));
    var energyEl = w.querySelector("[data-ml-energy]");
    if (!tabs.length || !runBtn) { return; }

    var factors = {};
    try {
      factors = JSON.parse(w.getAttribute("data-factors") || "{}");
    } catch (x) { return; }
    var KJ = parseFloat(w.getAttribute("data-kj")) || 0;
    var MASS = w.getAttribute("data-mass-unit") || "";
    var ENERGY = w.getAttribute("data-energy-unit") || "";
    var DP = parseFloat(w.getAttribute("data-dp")) || 0;
    var GROUP = w.getAttribute("data-group") === "1";
    var RUN = w.getAttribute("data-run-label") || "";
    var RAN = w.getAttribute("data-ran-label") || "";

    /* The opening state IS the markup: the amount Design opens on is already
       pressed, so there is nothing to seed and no second copy of the default
       to fall out of step with the page. */
    var current = tabs[0];
    each(tabs, function (tb) {
      if (tb.getAttribute("aria-pressed") === "true") { current = tb; }
    });
    var exits = false;

    function mass(x) {
      return (x >= DP ? String(Math.round(x)) : x.toFixed(1)) + MASS;
    }
    /* Thousands grouped by hand, for the locale reason above. */
    function group(n) {
      var s = String(Math.round(n));
      if (!GROUP) { return s; }
      var out = "", i = 0, j;
      for (j = s.length - 1; j >= 0; j--) {
        out = s.charAt(j) + out;
        i += 1;
        if (i % 3 === 0 && j > 0) { out = "," + out; }
      }
      return out;
    }

    function draw() {
      var grams = parseFloat(current.getAttribute("data-grams")) || 0;
      each(tabs, function (tb) {
        tb.setAttribute("aria-pressed", tb === current ? "true" : "false");
      });
      if (nameEl) { nameEl.textContent = current.getAttribute("data-name") || ""; }
      if (noteEl) { noteEl.textContent = current.getAttribute("data-note") || ""; }

      /* ⚖️ THE TOTALS ARE SUMMED FROM THE FACTORS, NOT FROM THE PRINTED
         STRINGS. Design sums the unrounded values and rounds once; summing the
         rounded ones would let the two columns disagree by a tenth at exactly
         the amount the student is being asked to compare them at, on the one
         bench in the key stage whose whole claim is that they are equal.

         Which column a row belongs to is carried on the row itself
         (`data-ml-side`), authored at build time from `rows_in` / `rows_out`.
         Deriving it from DOM position would make the arithmetic depend on the
         layout, and the layout is a grid that reflows at 560px. */
      var sums = { "in": 0, "out": 0 };
      each(rows, function (el) {
        var f = factors[el.getAttribute("data-ml-row")];
        if (typeof f !== "number") { return; }
        var v = grams * f;
        el.textContent = mass(v);
        var side = el.getAttribute("data-ml-side");
        if (Object.prototype.hasOwnProperty.call(sums, side)) {
          sums[side] += v;
        }
      });
      each(totals, function (el) {
        el.textContent = mass(sums[el.getAttribute("data-ml-total")]);
      });
      if (energyEl) { energyEl.textContent = group(grams * KJ) + ENERGY; }

      runBtn.textContent = exits ? RAN : RUN;
      runBtn.disabled = exits;
      if (panel) { setHidden(panel, !exits); }
      setCountState(sec, exits ? "after" : "before");
      markStage(sec, exits);
    }

    each(tabs, function (tb) {
      tb.addEventListener("click", function () { current = tb; draw(); });
    });
    /* ⚖️ ONE-WAY. Design has no un-reveal: the exits panel is the completion of
       the bench and a student who has seen where the carbon goes has seen it. */
    runBtn.addEventListener("click", function () {
      exits = true;
      if (panel) { panel.setAttribute("role", "status"); }
      draw();
    });

    draw();
  }

  /* ── cell-demand (b8-02 #s-bench) ──

     ⚖️ THE CUT IS PER CELL AND ONE-WAY, AND THE DOM IS THE STATE. Every cell's
     panel is in the document with its own button and its own hidden `fails`
     line, so switching tabs cannot lose a cut and there is no second copy of
     the record to fall out of step with the page. A student who cuts the
     muscle cell, wanders off to the sperm cell and comes back finds the muscle
     cell exactly as they left it — which is what makes five separate failures
     accumulate into one argument.

     ⚖️ AND THE STOP COUNTS DISTINCT CELLS, NOT PRESSES. Design's own threshold
     is `seen >= 3` over the set of cut cells; counting presses would let three
     jabs at the same button tick a stop that is supposed to mean the student
     has seen the same failure in three different kinds of cell. */
  function wireCellDemand(sec) {
    var w = sec.querySelector("[data-cd]");
    if (!w) { return; }
    var tabs = toArray(w.querySelectorAll(".ks3-cd-tab"));
    var panels = toArray(w.querySelectorAll("[data-cd-panel]"));
    if (!tabs.length || !panels.length) { return; }

    var TOTAL = parseInt(w.getAttribute("data-total"), 10) || panels.length;
    var AFTER = parseInt(w.getAttribute("data-done-after"), 10) || 1;
    var RUN = w.getAttribute("data-run-label") || "";
    var RAN = w.getAttribute("data-ran-label") || "";
    var cut = {};

    function count() {
      var n = 0, k;
      for (k in cut) {
        if (Object.prototype.hasOwnProperty.call(cut, k) && cut[k]) { n += 1; }
      }
      return n;
    }

    function show(id) {
      each(tabs, function (tb) {
        tb.setAttribute("aria-pressed",
          tb.getAttribute("data-cd-cell") === id ? "true" : "false");
      });
      each(panels, function (p) {
        setHidden(p, p.getAttribute("data-cd-panel") !== id);
      });
    }

    function refresh() {
      var n = count();
      setCountState(sec, n ? "some" : "zero", { n: n, total: TOTAL });
      markStage(sec, n >= AFTER);
    }

    each(tabs, function (tb) {
      tb.addEventListener("click", function () {
        show(tb.getAttribute("data-cd-cell"));
      });
    });

    each(panels, function (p) {
      var id = p.getAttribute("data-cd-panel");
      var btn = p.querySelector("[data-cd-cut]");
      var fails = p.querySelector("[data-cd-fails]");
      if (!btn) { return; }
      btn.addEventListener("click", function () {
        if (cut[id]) { return; }
        cut[id] = true;
        if (fails) {
          setHidden(fails, false);
          fails.setAttribute("role", "status");
        }
        btn.textContent = RAN;
        btn.disabled = true;
        refresh();
      });
      /* The resting label is in the markup already; naming it here as well
         would put Design's own string in the bytes twice. */
      if (btn.textContent === "") { btn.textContent = RUN; }
    });

    refresh();
  }

  /* ── oxygen-debt (b8-03 #s-bench) ──

     ⚖️ THE BREATHING BAR IS DRIVEN BY LACTATE, NOT BY PACE. This is the whole
     lesson and it is one line of arithmetic:

         breathing = min(100, round(20 + supply × 0.6 + lactate × 0.5))

     Neither `pace` nor `demand` appears in it. When the runner stops, the
     demand bar collapses from 150 to 25 and the breathing bar stays at 90% —
     and the note names it: the muscles are not asking for this oxygen, the
     lactic acid is. `build_ks3.py` simulates exactly that sequence at build
     time and refuses to draw the bench if breathing follows demand down, so a
     regression here is a red build rather than a lesson quietly teaching its
     own misconception.

     ⚖️ RECOVERY LOWERS `supply` TOO, while lactate remains. Without that term
     breathing would fall on the supply half as well and the effect would be
     muddied; with it, the only thing holding the bar up after a stop is the
     lactate.

     ⚠️ THREE WIDTH RULES, NOT ONE. `bar_divisor` scales `demand` and `aerobic`
     ONLY — those two run past 100 in arbitrary units. `lactate` fills at its
     own value against its own maximum and `breathing` at its own percentage.
     Dividing all four by 1.6 would cap a maxed breathing bar at 62% and cost
     the lesson its punchline: the bar visibly topping out, and STAYING there
     after the runner stops, is the evidence the student is meant to read.

     ⚠️ NO TIMER. "Run for 10 s" advances the model by one step per press. The
     seconds are a label, not a clock — there is no `setInterval` in this unit
     and nothing here animates. */
  function wireOxygenDebt(sec) {
    var w = sec.querySelector("[data-od]");
    if (!w) { return; }
    var tabs = toArray(w.querySelectorAll(".ks3-od-tab"));
    var runBtn = w.querySelector("[data-od-run]");
    var stopBtn = w.querySelector("[data-od-stop]");
    var resetBtn = w.querySelector("[data-od-reset]");
    var phaseEl = w.querySelector("[data-od-phase]");
    var shortEl = w.querySelector("[data-od-shortfall]");
    var noteEl = w.querySelector("[data-od-note]");
    var values = toArray(w.querySelectorAll("[data-od-bar]"));
    var fills = toArray(w.querySelectorAll("[data-od-fill]"));
    if (!tabs.length || !runBtn || !stopBtn) { return; }

    var M, LABELS, PHASES, SHORT, NOTES;
    try {
      M = JSON.parse(w.getAttribute("data-model") || "{}");
      LABELS = JSON.parse(w.getAttribute("data-labels") || "{}");
      PHASES = JSON.parse(w.getAttribute("data-phases") || "{}");
      SHORT = JSON.parse(w.getAttribute("data-shortfall") || "{}");
      NOTES = JSON.parse(w.getAttribute("data-notes") || "{}");
    } catch (x) { return; }
    var LACT_MAX = parseFloat(w.getAttribute("data-lactate-max")) || 100;
    var DIV = parseFloat(w.getAttribute("data-bar-divisor")) || 1;

    var pace = tabs[0];
    each(tabs, function (tb) {
      if (tb.getAttribute("aria-pressed") === "true") { pace = tb; }
    });

    var supply, lactate, seconds, phase, peakLactate, everRecovered = false;
    function reset() {
      supply = M.supply_rest;
      lactate = 0;
      /* MRB-257 (5.13) — the HIGHEST lactate reached since the last reset.
         Recovery used to print "Lactic acid cleared… The debt is paid" off
         `lactate <= 1`, which is also true of a student who never made any:
         Walking → Run 10 s → Recover 30 s reads "the debt is paid" with the
         acid bar at 0 units throughout. A debt has to be incurred before it
         can be repaid. */
      peakLactate = 0;
      seconds = 0;
      phase = "ready";
    }
    reset();

    function paceDemand() {
      return parseFloat(pace.getAttribute("data-demand")) || 0;
    }

    /* Design's own reads, and the only copy of them in the runtime. */
    function read() {
      /* MRB-257 (5.15) — the ready phase's demand. It reused `supply_rest`,
         which is the resting SUPPLY, so standing on the line cost 25 units
         and walking cost 20: the bench said walking is cheaper than standing
         still. `demand_rest` is the authored resting demand; no shipped
         payload carries one yet, so the fallback is the old value and this
         finding is only half-fixed from here — see HANDOFF. */
      var restDemand = typeof M.demand_rest === "number"
        ? M.demand_rest : M.supply_rest;
      var demand = phase === "recovering" ? M.recover_demand
        : (phase === "ready" ? restDemand : paceDemand());
      var b = M.breathing;
      return {
        demand: demand,
        aerobic: Math.min(supply, demand),
        lactate: Math.round(lactate),
        breathing: Math.min(b.max, Math.round(
          b.base + supply * b.per_supply + lactate * b.per_lactate)),
        shortfall: Math.max(0, demand - supply)
      };
    }

    function width(id, v) {
      if (id === "breathing") { return Math.min(100, v); }
      if (id === "lactate") { return Math.min(100, v * 100 / LACT_MAX); }
      return Math.min(100, v / DIV);
    }

    function fill(tpl, n) {
      return String(tpl || "").split("{n}").join(String(n));
    }

    function noteFor(r) {
      if (phase === "ready") { return NOTES.rest; }
      if (phase === "recovering") {
        if (lactate > 1) { return NOTES.debt; }
        /* MRB-257 (5.13) — nothing was borrowed, so there is nothing to
           repay. `NOTES.rest` is the authored sentence for exactly this
           state ("no lactic acid is being made") and is true of a student
           who has stopped without ever going anaerobic; an authored
           `nothing_to_repay` takes precedence if one is ever written. */
        if (peakLactate <= 1) { return NOTES.nothing_to_repay || NOTES.rest; }
        return NOTES.cleared;
      }
      if (r.shortfall > 0) { return fill(NOTES.shortfall, r.shortfall); }
      /* MRB-257 (5.14) — supply has caught up, so nothing further is being
         made; but `within` says "nothing is building up" over an acid bar
         still reading 4 units, indefinitely. The two facts are different and
         need two sentences. No shipped payload carries the second one yet,
         so this falls back to `within` — see HANDOFF. */
      if (lactate > 1 && NOTES.within_with_lactate) {
        return NOTES.within_with_lactate;
      }
      return NOTES.within;
    }

    function draw() {
      var r = read();
      each(tabs, function (tb) {
        tb.setAttribute("aria-pressed", tb === pace ? "true" : "false");
      });
      each(values, function (el) {
        var id = el.getAttribute("data-od-bar");
        var suffix = el.getAttribute("data-suffix") || "";
        el.textContent = r[id] +
          (/^[A-Za-z0-9]/.test(suffix) ? " " : "") + suffix;
      });
      each(fills, function (el) {
        var id = el.getAttribute("data-od-fill");
        el.style.width = width(id, r[id]) + "%";
      });

      if (phaseEl) {
        phaseEl.textContent = phase === "ready" ? PHASES.ready
          : (phase === "recovering" ? PHASES.recovering
             : (pace.getAttribute("data-label") || ""));
      }
      if (shortEl) {
        shortEl.textContent = phase === "recovering" ? SHORT.repaying
          : (r.shortfall > 0 ? fill(SHORT.borrowed, r.shortfall)
                             : SHORT.aerobic);
      }
      if (noteEl) { noteEl.textContent = noteFor(r); }

      runBtn.textContent = phase === "running" ? LABELS.running : LABELS.run;
      stopBtn.textContent = phase === "recovering" ? LABELS.recovering
                                                   : LABELS.stop;
      /* MRB-257 (5.50) — "Recover another 30 s" kept adding thirty seconds
         after the acid was gone and the supply was back at rest: 190 s →
         220 s with every other readout identical. Once there is nothing left
         to recover, there is nothing left for the button to do. Pressing Run
         puts the bench back into `running` and re-enables it. */
      stopBtn.disabled = phase === "ready" ||
        (phase === "recovering" && lactate <= 0 && supply <= M.supply_rest);

      /* The clock lives in the block's head row, as three named states — two
         of which quote the seconds. See `_KIND_HEAD_FROM` in build_ks3.py. */
      setCountState(sec, seconds === 0 ? "zero"
        : (phase === "recovering" ? "recovering" : "running"), { n: seconds });
      markStage(sec, everRecovered);
    }

    runBtn.addEventListener("click", function () {
      supply = Math.min(M.supply_max, supply + M.supply_step);
      var gap = Math.max(0, paceDemand() - supply);
      lactate = Math.min(M.lactate_max, lactate + gap * M.lactate_factor);
      if (lactate > peakLactate) { peakLactate = lactate; }
      seconds += M.run_seconds;
      phase = "running";
      draw();
    });

    stopBtn.addEventListener("click", function () {
      if (phase === "ready") { return; }
      lactate = Math.max(0, lactate - M.recover_clear);
      /* ⚖️ SUPPLY COMES DOWN TOO, while there is still acid to clear — and
         snaps to rest once there is not. Without this the breathing bar would
         fall on the supply half as well and the lactate term would stop being
         the only thing holding it up. */
      supply = lactate > 0 ? Math.max(M.supply_rest, supply - M.supply_decay)
                           : M.supply_rest;
      seconds += M.recover_seconds;
      phase = "recovering";
      /* ⚖️ ONE-WAY, AND ONLY AT ZERO. A student who presses once and leaves has
         watched breathing fall from 100% to 90%, which is the wrong story: the
         debt has barely been touched. The stop ticks when the acid is gone. */
      if (lactate === 0) { everRecovered = true; }
      draw();
    });

    each(tabs, function (tb) {
      tb.addEventListener("click", function () { pace = tb; draw(); });
    });
    if (resetBtn) {
      /* ⚠️ `everRecovered` AND `pace` SURVIVE A RESET. The rail records what
         the student has done (MRB-208), and the pace is a setting rather than
         a state — Design's own `onReset` leaves both alone. */
      resetBtn.addEventListener("click", function () { reset(); draw(); });
    }

    draw();
  }

  /* ── fermenter (b8-04 #s-bench) ──

     ⛔ THIS RUNTIME PICKS A BRANCH. IT DOES NOT BUILD ONE. Every branch is
     already in the document, drawn in full by `build_ks3.py` and hidden, and
     all this does is unhide the first one whose pins agree with the dials.

     That is the fix for a real defect. Design decided which product list to
     show with `out.line.indexOf('oxygen') >= 0` — a string sniff on the
     reaction text — and it is wrong on one live branch: yoghurt bacteria in an
     open stirred vessel take `line = "contaminated"`, which contains no
     "oxygen", so the sniff fell through to the anaerobic list and the bench
     printed "Lactic acid 100 units" under its own heading "Poor conditions for
     these bacteria". `products` is authored per branch, the sniff is gone, and
     `r_fermenter` refuses any aerobic branch that reports a fermentation
     product — so it cannot come back.

     ⚖️ AND NO BRANCH IS AN ERROR STATE. Yeast open-and-stirred is how yeast is
     manufactured; it gets the same panel as every other outcome. Nothing here
     adds a class, a tone or an attribute to single a branch out.

     ⚠️ DRAWING IN THE BROWSER WOULD ALSO BREAK THE ARROW. The reaction lines
     carry `→`, which no shipped font subset contains — `t()` swaps it for a
     drawn `<svg>` at build time. A line assigned to `textContent` here would
     ship the raw codepoint and render as tofu mid-equation. */
  function wireFermenter(sec) {
    var w = sec.querySelector("[data-fm]");
    if (!w) { return; }
    var opts = toArray(w.querySelectorAll(".ks3-fm-opt"));
    var presets = toArray(w.querySelectorAll("[data-fm-preset]"));
    var blocks = toArray(w.querySelectorAll("[data-fm-branch]"));
    if (!opts.length || !blocks.length) { return; }

    var branches = [], picks = {};
    try {
      branches = JSON.parse(w.getAttribute("data-branches") || "[]");
      picks = JSON.parse(w.getAttribute("data-start") || "{}");
    } catch (x) { return; }
    if (!branches.length) { return; }
    var AFTER = parseInt(w.getAttribute("data-done-after"), 10) || 1;
    /* MRB-257 (5.49) — DISTINCT SET-UPS, not presses. The head readout says
       "{n} set-up{s} tried", and it used to count every press: pressing the
       already-selected Yeast option five times read "5 set-ups tried" with
       the panel unchanged, and the bench reached "19 set-ups tried" with ten
       distinct set-ups on the dials. A set-up is a combination of the four
       dials, so that is what is counted — the opening combination included,
       because it is on screen from the first paint. This replaces the older
       "every press counts, including one that changes nothing" reading: a
       press that changes nothing has not tried anything. */
    var tried = {}, seen = 0;
    function noteSetup() {
      var sig = [], d;
      for (d in picks) {
        if (Object.prototype.hasOwnProperty.call(picks, d)) {
          sig.push(d + "=" + picks[d]);
        }
      }
      sig.sort();
      var key = sig.join("|");
      if (!tried[key]) { tried[key] = true; seen += 1; }
    }

    /* Design's own first-match-wins. Order is the pedagogy: killed beats
       starved beats aerobic beats fermenting — a dead culture is dead whatever
       else is set, and a culture with no sugar has nothing to respire however
       perfect the other three dials are. Read from the shipped list, never
       from an object's key order. */
    function current() {
      for (var i = 0; i < branches.length; i++) {
        var when = branches[i].when, ok = true, d;
        for (d in when) {
          if (Object.prototype.hasOwnProperty.call(when, d)
              && picks[d] !== when[d]) { ok = false; break; }
        }
        if (ok) { return branches[i].id; }
      }
      return branches[branches.length - 1].id;
    }

    function draw() {
      var id = current();
      each(opts, function (o) {
        o.setAttribute("aria-pressed",
          picks[o.getAttribute("data-dial")] === o.getAttribute("data-opt")
            ? "true" : "false");
      });
      each(blocks, function (bl) {
        setHidden(bl, bl.getAttribute("data-fm-branch") !== id);
      });
      /* The opening combination is on the dials and its panel is on screen,
         but it is not something the student TRIED — the readout opens on
         "nothing changed yet" and stays there until they act. */
      setCountState(sec, seen ? "some" : "zero",
        { n: seen, s: seen === 1 ? "" : "s" });
      markStage(sec, seen >= AFTER);
    }

    each(opts, function (o) {
      o.addEventListener("click", function () {
        picks[o.getAttribute("data-dial")] = o.getAttribute("data-opt");
        noteSetup();
        draw();
      });
    });
    each(presets, function (btn) {
      btn.addEventListener("click", function () {
        var next = {};
        try {
          next = JSON.parse(btn.getAttribute("data-fm-preset") || "{}");
        } catch (x) { return; }
        var d;
        for (d in next) {
          if (Object.prototype.hasOwnProperty.call(next, d)) {
            picks[d] = next[d];
          }
        }
        noteSetup();
        draw();
      });
    });

    draw();
  }

/* ═══ END B8 ═══ */

/* ═══ BEGIN B9 ═══ */

  /* ── B9 · Ecosystems and interdependence (⊕ MRB-250) ──
     Six instruments, six wire functions, and NOTHING SHARED between them
     except four number formatters — because nothing in this unit is the same
     block twice. The six ask six different questions: climb a chain and watch
     what arrives at the top, run a field for twenty-six years and find the
     lag, take a species out of a wood and follow it three rounds, empty a
     supermarket shelf, climb the same chain with a chemical on it, and
     estimate a population you can then check your answer against.

     ⚠️ NOTHING HERE ANIMATES AND NOTHING HERE USES A TIMER. No canvas, no
     `requestAnimationFrame`, no `setTimeout`, no `setInterval` — grepped
     across all six approved pages and zero on every term. So there is no rAF
     loop in this section to test `prefers-reduced-motion` inside (MRB-220 R4),
     and the B9 stylesheet adds no transition for the platform-wide
     reduced-motion rule to have to remove.

     ⚠️ AND NONE OF THESE SIX MARKS ANYTHING (MRB-196 R10). A chosen tab shows
     that it was CHOSEN — the alert ground Design's own `seg()` paints — and
     takes no verdict class, no green, no red, ever. What these benches show is
     a CONSEQUENCE. Only the mastery ladder marks correctness, and amber here
     is a quantity above a threshold, never a student being wrong.

     ⚠️ THE STAGE PREDICATE IS MONOTONIC ON ALL SIX, and on b9-04 and b9-06
     that is a departure from Design made under MRB-208 rather than against it.
     Her `isDone()` for those two reads live state a student can turn back off
     — bringing the pollinators back, re-sampling the field — so her rail stop
     unticks when a student tidies up after themselves. The rail records
     PARTICIPATION. What ticks is unchanged; what unticks is nothing.

     ⚠️ AND EACH BENCH'S MARKER IS READ TWICE (MRB-249). The band section
     beside it — `s-roles`, `s-cycle`, `s-rules`, `s-who`, `s-two` — carries no
     control of its own and its rail entry MIRRORS `s-bench`, resolved in
     `wireRail`'s `paint()`. So a threshold moved for convenience here moves
     two stops, not one. */

  /* `toLocaleString()` is the BROWSER's locale and not ours: a student whose
     machine is set to a European locale would read `10.000 kJ` for ten
     thousand. Design writes the locale call on four of the six pages; the port
     groups explicitly, and `build_ks3.py`'s `_b8_group` does the identical
     thing at the other end so the static bytes and the live page cannot
     disagree. */
  function b9Group(n) {
    var s = String(Math.round(n)), out = "", i = 0, j;
    for (j = s.length - 1; j >= 0; j--) {
      out = s.charAt(j) + out;
      i += 1;
      if (i % 3 === 0 && j > 0 && s.charAt(j - 1) !== "-") { out = "," + out; }
    }
    return out;
  }

  /* A bare amount: grouped when it is a whole number of one or more, printed
     plainly when it is not. `String(0.1)` is "0.1" and `String(0.01)` is
     "0.01", which is exactly what Design's concatenation produces. */
  function b9Amount(v) {
    return (v >= 1 && v === Math.floor(v)) ? b9Group(v) : String(v);
  }

  /* `x.toFixed(2).replace(/\.?0+$/, '')` — Design's own percentage rule, and
     the difference between `0.1` and `0.01` is the difference between a
     four-level chain and a five-level one. Kept, not tidied. */
  function b9Strip2(x) {
    return x.toFixed(2).replace(/\.?0+$/, "") || "0";
  }

  /* Design's four-branch concentration rule: ≥10 → 0 dp · ≥1 → 1 dp ·
     ≥0.01 → 3 dp · else 4 dp. THE THRESHOLD IS PER VALUE, so the same column
     prints `0.0030` and `300` and that is the rule applied honestly. */
  function b9Ppm(x) {
    if (x >= 10) { return x.toFixed(0); }
    if (x >= 1) { return x.toFixed(1); }
    if (x >= 0.01) { return x.toFixed(3); }
    return x.toFixed(4);
  }

  function b9Json(el, name) {
    try { return JSON.parse(el.getAttribute(name) || "{}"); }
    catch (x) { return null; }
  }

  /* ── chain-ledger (b9-01 #s-bench) ──

     ⚖️ THE PRODUCER IS AT THE BOTTOM AND THE ENERGY GOES UP. The list is
     `column-reverse` in the stylesheet, so `data-i="0"` — the grass, the ten
     thousand kilojoules — is drawn last and therefore lowest. Everything here
     indexes from the producer regardless, which is why the arithmetic does not
     care about the drawing order and the drawing order does not care about the
     arithmetic.

     ⚖️ THE VERDICT IS COMPUTED FROM THE CHAIN'S LENGTH, from the same three
     authored fragments `build_ks3.py` used for the resting render. A fourth
     chain therefore needs no new prose, and the line cannot disagree with the
     ladder of figures above it.

     ⚠️ SWITCHING CHAIN RESTARTS THE CLIMB. Design resets `shown` to 1 on every
     tab press, so the panels do not each keep their own progress: one count
     lives here and the panels are redrawn from it. */
  function wireChainLedger(sec) {
    var w = sec.querySelector("[data-cl]");
    if (!w) { return; }
    var tabs = toArray(w.querySelectorAll(".ks3-cl-tab"));
    var panels = toArray(w.querySelectorAll("[data-cl-chainpanel]"));
    var up = w.querySelector("[data-cl-up]");
    var resetBtn = w.querySelector("[data-cl-reset]");
    var verdictEl = w.querySelector("[data-cl-verdict]");
    if (!tabs.length || !panels.length || !up) { return; }

    var START = parseFloat(w.getAttribute("data-start-kj")) || 0;
    var FACTOR = parseFloat(w.getAttribute("data-factor")) || 10;
    var STEP = w.getAttribute("data-step-label") || "";
    var SPENT = w.getAttribute("data-step-spent-label") || "";
    var LEAD = w.getAttribute("data-verdict-lead") || "";
    var MID = w.getAttribute("data-verdict-mid") || "";
    var TAIL = w.getAttribute("data-verdict-tail") || "";
    /* MRB-257 (5.53) — the widget has carried `data-energy-unit=" kJ"` since
       it shipped and this function never read it, so the verdict printed a
       bare "…and 10 arrived here" (and "1 arrived here" on the sea chain)
       while every other figure on the block reads "10 kJ". */
    var UNIT = w.getAttribute("data-energy-unit") || "";

    /* The opening state IS the markup: the chain Design opens on is already
       pressed, so there is no second copy of the default to fall out of step
       with the page. */
    var current = tabs[0];
    each(tabs, function (tb) {
      if (tb.getAttribute("aria-pressed") === "true") { current = tb; }
    });
    var shown = 1, everTopped = false;

    function panelFor(id) {
      var found = panels[0], i;
      for (i = 0; i < panels.length; i++) {
        if (panels[i].getAttribute("data-cl-chainpanel") === id) {
          found = panels[i];
        }
      }
      return found;
    }

    function draw() {
      var panel = panelFor(current.getAttribute("data-cl-chain"));
      each(tabs, function (tb) {
        tb.setAttribute("aria-pressed", tb === current ? "true" : "false");
      });
      each(panels, function (p) { setHidden(p, p !== panel); });

      var levels = toArray(panel.querySelectorAll(".ks3-cl-level"));
      var total = levels.length;
      if (shown > total) { shown = total; }
      each(levels, function (li, i) {
        var on = i < shown;
        if (on) { li.setAttribute("data-shown", ""); }
        else { li.removeAttribute("data-shown"); }
        if (i === shown - 1) { li.setAttribute("data-top", ""); }
        else { li.removeAttribute("data-top"); }
        setHidden(li.querySelector("[data-cl-readout]"), !on);
      });

      var topped = shown >= total;
      up.textContent = topped ? SPENT : STEP;
      up.disabled = topped;
      if (verdictEl) {
        if (topped) {
          verdictEl.textContent =
            LEAD + b9Amount(START / Math.pow(FACTOR, total - 1)) + UNIT + MID +
            b9Strip2(100 / Math.pow(FACTOR, total - 1)) + TAIL;
        }
        setHidden(verdictEl, !topped);
      }

      /* ⚠️ THE DENOMINATOR FOLLOWS THE TAB. The chains are deliberately
         different lengths — that is the argument — so "level 1 of 4" has to
         become "level 1 of 5" on the sea chain. `build_ks3.py` seeds the
         resting value from the FIRST chain for the same reason. */
      var count = sec.querySelector("[data-count]");
      if (count) { count.setAttribute("data-total", String(total)); }
      setCount(sec, shown);

      if (topped) { everTopped = true; }
      markStage(sec, everTopped);
    }

    each(tabs, function (tb) {
      tb.addEventListener("click", function () {
        current = tb;
        shown = 1;
        draw();
      });
    });
    up.addEventListener("click", function () { shown += 1; draw(); });
    if (resetBtn) {
      resetBtn.addEventListener("click", function () { shown = 1; draw(); });
    }
    draw();
  }

  /* ── cycle-runner (b9-02 #s-bench) ──

     ⚖️ K IS THE GRASS SUPPLY AND IT IS WHY THIS IS A LESSON. Take the
     predators out and the rabbits climb, then STOP — crowded and hungry at the
     ceiling the grass sets — instead of drawing the exponential curve that
     would teach the belief `#s-think` exists to break. The logistic term
     `R * prey * (1 - prey / K)` is the whole of that, and the two clamps
     (`K * prey_cap_mult` above, a hard floor at `pred_floor` below) are what
     stop a DISCRETE model overshooting or oscillating negative.

     ⚖️ THE TWO SERIES ARE SCALED INDEPENDENTLY, each with its own floor. On
     one scale the fox line flattens into the axis and the LAG — the entire
     lesson, and what both marked rungs test — becomes unreadable. The caption
     says so in words because the chart cannot.

     ⚠️ *REMOVE EVERY FOX* IS NOT A RESET. It toggles the predators between
     zero and their starting number, pushes ONE history point and advances the
     year by one, so the chart records the intervention as a year like any
     other and the rabbits' response to it is read off the years that follow. */
  function wireCycleRunner(sec) {
    var w = sec.querySelector("[data-cy]");
    if (!w) { return; }
    var M = b9Json(w, "data-model"), NOTES = b9Json(w, "data-notes");
    var chart = w.querySelector("[data-cy-chart]");
    var preyEl = w.querySelector("[data-cy-prey]");
    var predEl = w.querySelector("[data-cy-pred]");
    var noteEl = w.querySelector("[data-cy-note]");
    var yearBtn = w.querySelector("[data-cy-year]");
    var tenBtn = w.querySelector("[data-cy-ten]");
    var cullBtn = w.querySelector("[data-cy-cull]");
    var resetBtn = w.querySelector("[data-cy-reset]");
    if (!M || !NOTES || !chart || !cullBtn) { return; }

    var CULL = w.getAttribute("data-cull-label") || "";
    var RESTORE = w.getAttribute("data-restore-label") || "";
    var PREY_FILL = w.getAttribute("data-prey-fill") || "--ks3-alert";
    var PRED_FILL = w.getAttribute("data-pred-fill") || "--ks3-ok";

    var prey = M.start_prey, pred = M.start_pred, year = 0, everTen = false;
    var hist = [{ prey: prey, pred: pred }];

    function advance(n) {
      var i, nextPrey, nextPred;
      for (i = 0; i < n; i++) {
        nextPrey = prey + M.r * prey * (1 - prey / M.k) - M.a * prey * pred;
        nextPred = pred + M.b * M.a * prey * pred - M.m * pred;
        prey = Math.max(0, Math.min(M.k * M.prey_cap_mult, nextPrey));
        pred = Math.max(0, Math.min(M.k, nextPred));
        /* The extinction floor, and not a rounding artefact: below one animal
           there is no breeding pair, and a discrete model left to carry 0.3 of
           a fox would let the population climb back out of nothing. */
        if (pred < M.pred_floor) { pred = 0; }
        hist.push({ prey: prey, pred: pred });
      }
      while (hist.length > M.history) { hist.shift(); }
      year += n;
      draw();
    }

    /* ⚖️ SIX BRANCHES, IN DESIGN'S EVALUATION ORDER, FIRST MATCH WINS — and
       `no_pred_at_ceiling` MUST be tested before `no_pred` or the ceiling note
       never fires and *Remove every fox* stops teaching carrying capacity.
       Tested on the ROUNDED values, as Design does, so "no foxes" means the
       number on screen rather than a hundredth of one. */
    /* MRB-257 (5.11) — has the oscillation stopped? Measured over the drawn
       window: if the highest and lowest prey counts in it differ by less than
       a per cent of the high, the model has arrived at its fixed point.
       MRB-255 S5 rules that the MATHS STAYS — a discrete logistic
       Lotka–Volterra damps to 667 rabbits / 267 foxes by year 260, and a
       neutral model that cycled forever at its starting amplitude would look
       like perpetual motion — so what has to give is any string promising a
       cycle that continues undiminished. That is a records job, and so is
       the `settled` note itself; this branch fires only when one is authored,
       so nothing shipped moves until it is. See HANDOFF. */
    function settledNow() {
      if (hist.length < M.history) { return false; }
      var lo = hist[0].prey, hi = hist[0].prey, i;
      for (i = 1; i < hist.length; i++) {
        if (hist[i].prey < lo) { lo = hist[i].prey; }
        if (hist[i].prey > hi) { hi = hist[i].prey; }
      }
      return hi > 0 && (hi - lo) / hi < 0.01;
    }

    function noteId(p, q) {
      if (year === 0) { return "year_zero"; }
      if (q === 0 && p > M.k * 0.9) { return "no_pred_at_ceiling"; }
      if (q === 0) { return "no_pred"; }
      if (NOTES.settled && settledNow()) { return "settled"; }
      if (p > 1200 && q < 200) { return "prey_high_pred_low"; }
      if (p < 500) { return "prey_low"; }
      return "steady";
    }

    function bar(series, token, v, max) {
      var s = document.createElement("span");
      s.className = "ks3-cy-bar";
      s.setAttribute("data-series", series);
      s.style.setProperty("--cy-fill", "var(" + token + ")");
      s.style.height = Math.max(2, (v / max) * 100) + "%";
      return s;
    }

    function draw() {
      var p = Math.round(prey), q = Math.round(pred), i;
      var maxPrey = 600, maxPred = 150;
      for (i = 0; i < hist.length; i++) {
        if (hist[i].prey > maxPrey) { maxPrey = hist[i].prey; }
        if (hist[i].pred > maxPred) { maxPred = hist[i].pred; }
      }
      while (chart.firstChild) { chart.removeChild(chart.firstChild); }
      for (i = 0; i < hist.length; i++) {
        var col = document.createElement("span");
        col.className = "ks3-cy-year";
        col.appendChild(bar("prey", PREY_FILL, hist[i].prey, maxPrey));
        col.appendChild(bar("pred", PRED_FILL, hist[i].pred, maxPred));
        chart.appendChild(col);
      }
      if (preyEl) { preyEl.textContent = String(p); }
      if (predEl) { predEl.textContent = String(q); }
      if (noteEl) { noteEl.textContent = NOTES[noteId(p, q)] || ""; }
      cullBtn.textContent = q === 0 ? RESTORE : CULL;
      setCount(sec, year);
      if (year >= 10) { everTen = true; }
      markStage(sec, everTen);
    }

    if (yearBtn) {
      yearBtn.addEventListener("click", function () { advance(1); });
    }
    if (tenBtn) {
      tenBtn.addEventListener("click", function () { advance(10); });
    }
    cullBtn.addEventListener("click", function () {
      pred = pred === 0 ? M.start_pred : 0;
      hist.push({ prey: prey, pred: pred });
      while (hist.length > M.history) { hist.shift(); }
      year += 1;
      draw();
    });
    if (resetBtn) {
      resetBtn.addEventListener("click", function () {
        prey = M.start_prey;
        pred = M.start_pred;
        year = 0;
        hist = [{ prey: prey, pred: pred }];
        draw();
      });
    }
    draw();
  }

  /* ── remove-a-species (b9-03 #s-bench) ──

     ⚖️ THE BEES HAVE NO FEEDING LINE AND STILL EMPTY THE WEB. Nothing here
     special-cases them and nothing needs to: the web is prose, the rounds are
     authored, and the instrument's job is to make the student take three steps
     before the verdict lands. What that buys is the sentence — feeding is not
     the only kind of dependence — arriving after the consequence rather than
     as a claim.

     ⚠️ EVERY SPECIES' PANEL IS IN THE DOCUMENT and only one is shown, so a
     reader with JS off gets a whole removal rather than an empty shell.
     Switching species resets the round count, as Design does. */
  function wireRemoveASpecies(sec) {
    var w = sec.querySelector("[data-rs]");
    if (!w) { return; }
    var tabs = toArray(w.querySelectorAll(".ks3-rs-tab"));
    var panels = toArray(w.querySelectorAll("[data-rs-panel]"));
    var next = w.querySelector("[data-rs-next]");
    var resetBtn = w.querySelector("[data-rs-reset]");
    if (!tabs.length || !panels.length || !next) { return; }

    var STILL = w.getAttribute("data-still-label") || "";
    var REMOVED = w.getAttribute("data-removed-label") || "";
    var FIRST = w.getAttribute("data-first-label") || "";
    var STEP = w.getAttribute("data-step-label") || "";
    var SPENT = w.getAttribute("data-spent-label") || "";

    var current = tabs[0];
    each(tabs, function (tb) {
      if (tb.getAttribute("aria-pressed") === "true") { current = tb; }
    });
    var shown = 0, everDone = false;

    function panelFor(id) {
      var found = panels[0], i;
      for (i = 0; i < panels.length; i++) {
        if (panels[i].getAttribute("data-rs-panel") === id) {
          found = panels[i];
        }
      }
      return found;
    }

    function draw() {
      var panel = panelFor(current.getAttribute("data-rs-species"));
      each(tabs, function (tb) {
        tb.setAttribute("aria-pressed", tb === current ? "true" : "false");
      });
      each(panels, function (p) { setHidden(p, p !== panel); });

      var rounds = toArray(panel.querySelectorAll(".ks3-rs-round"));
      var total = rounds.length;
      if (shown > total) { shown = total; }
      var name = panel.getAttribute("data-label") || "";
      var headline = panel.querySelector("[data-rs-headline]");
      if (headline) {
        headline.textContent =
          (shown === 0 ? STILL : REMOVED).split("{name}").join(name);
      }
      each(rounds, function (li, i) {
        var on = i < shown;
        if (on) { li.setAttribute("data-shown", ""); }
        else { li.removeAttribute("data-shown"); }
        if (i === shown - 1) { li.setAttribute("data-cur", ""); }
        else { li.removeAttribute("data-cur"); }
        setHidden(li.querySelector(".ks3-rs-roundbody"), !on);
      });

      var done = shown >= total;
      next.textContent = shown === 0 ? FIRST : (done ? SPENT : STEP);
      next.disabled = done;
      setHidden(panel.querySelector("[data-rs-verdict]"), !done);
      setCount(sec, shown);
      if (done) { everDone = true; }
      markStage(sec, everDone);
    }

    each(tabs, function (tb) {
      tb.addEventListener("click", function () {
        current = tb;
        shown = 0;
        draw();
      });
    });
    next.addEventListener("click", function () { shown += 1; draw(); });
    if (resetBtn) {
      resetBtn.addEventListener("click", function () { shown = 0; draw(); });
    }
    draw();
  }

  /* ── supermarket-shelf (b9-04 #s-bench) ──

     ⚖️ THE GAP BETWEEN THE TWO BARS IS THE ENTIRE LESSON, and this function's
     one job is to keep them apart. Two percentages, computed from two separate
     shares of two separate totals, written into two separate bars that the
     stylesheet lays out side by side and wraps to two ROWS rather than
     merging. `build_ks3.py` refuses a payload whose two bars land on the same
     figure with the pollinators gone; there is nothing here that could combine
     them, and that is deliberate.

     ⚠️ THREE STATES, TWO BUTTONS, AND NO PATH FROM `half` BACK TO `all`.
     Design's, measured, and left alone. */
  function wireSupermarketShelf(sec) {
    var w = sec.querySelector("[data-ss]");
    if (!w) { return; }
    var SHARES = b9Json(w, "data-shares");
    var NOTES = b9Json(w, "data-notes");
    var tiles = toArray(w.querySelectorAll("[data-ss-food]"));
    var bars = toArray(w.querySelectorAll("[data-ss-bar]"));
    var noteEl = w.querySelector("[data-ss-note]");
    var toggle = w.querySelector("[data-ss-toggle]");
    var half = w.querySelector("[data-ss-half]");
    if (!SHARES || !NOTES || !tiles.length || !toggle) { return; }

    var REMOVE = w.getAttribute("data-remove-label") || "";
    var RESTORE = w.getAttribute("data-restore-label") || "";
    var GONE = w.getAttribute("data-gone-label") || "";
    var UNAFFECTED = w.getAttribute("data-unaffected-label") || "";
    var PART = w.getAttribute("data-part-label") || "";

    var level = "all", ever = false;

    function draw() {
      var loss = level === "none" ? 1 : (level === "half" ? 0.5 : 0);
      var cal = 0, vit = 0, calMax = 0, vitMax = 0, i;
      for (i = 0; i < SHARES.length; i++) {
        var remaining = 1 - SHARES[i][2] * loss;
        cal += SHARES[i][0] * remaining;
        vit += SHARES[i][1] * remaining;
        calMax += SHARES[i][0];
        vitMax += SHARES[i][1];
      }
      var pct = {
        cal: Math.round((cal / calMax) * 100),
        vit: Math.round((vit / vitMax) * 100)
      };

      each(tiles, function (li) {
        var dep = parseFloat(li.getAttribute("data-dep")) || 0;
        var remaining = 1 - dep * loss;
        var gone = remaining < 0.2;
        var status = li.querySelector("[data-ss-status]");
        if (gone) { li.setAttribute("data-gone", "1"); }
        else { li.removeAttribute("data-gone"); }
        if (!status) { return; }
        /* ⚖️ AT FULL POLLINATION THE TILE SHOWS *HOW*, NOT A STATUS. The dial
           doubles as the teaching label, so a student reads why a food is
           about to survive before finding out that it does. */
        if (loss === 0) {
          status.textContent = li.getAttribute("data-how") || "";
        } else if (gone) {
          status.textContent = GONE;
        } else if (remaining < 0.85 + 1e-6) {
          /* MRB-257 (5.24) — `<` against a value a tile lands on EXACTLY.
             Milk is `data-dep="0.15"`, so at zero pollinators `remaining`
             is exactly 0.85 and the strict test failed: the tile printed
             "unaffected" in every state including none, while its 15% was
             inside the calorie arithmetic pulling the total down. */
          status.textContent =
            PART.split("{n}").join(String(Math.round(remaining * 100)));
        } else {
          status.textContent = UNAFFECTED;
        }
      });

      each(bars, function (b) {
        var id = b.getAttribute("data-ss-bar");
        var v = b.querySelector("[data-ss-value]");
        var fill = b.querySelector(".ks3-ss-fill");
        if (v) { v.textContent = pct[id] + "%"; }
        if (fill) { fill.style.width = pct[id] + "%"; }
      });

      if (noteEl) {
        noteEl.textContent = (NOTES[level] || "")
          .split("{cal}").join(String(pct.cal))
          .split("{vit}").join(String(pct.vit));
      }
      /* MRB-257 (5.25) — the way back is signposted from EVERY state. From
         "half" the toggle used to read "Remove every insect pollinator", so
         the only route to the intact shelf was to empty it first; and the
         half button was still enabled at half, where a second press
         produced an identical DOM. Now the toggle is intact ↔ none and
         says which it will do, and the half button is spent once the shelf
         is at half. */
      toggle.textContent = level === "all" ? REMOVE : RESTORE;
      if (half) { half.disabled = level === "half"; }
      setCountState(sec, level);
      if (level !== "all") { ever = true; }
      markStage(sec, ever);
    }

    toggle.addEventListener("click", function () {
      level = level === "all" ? "none" : "all";
      draw();
    });
    if (half) {
      half.addEventListener("click", function () {
        if (level === "half") { return; }
        level = "half";
        draw();
      });
    }
    draw();
  }

  /* ── bioaccumulation (b9-05 #s-bench) ──

     ⚖️ THE ×1 SETTING IS THE CONTROL AND IT MUST DRAW A FLAT LINE. Its verdict
     is the one branch that quotes no number, because there is no number to
     quote: the concentration in the water was the whole story. That is what
     proves the mechanism is PERSISTENCE, NOT TOXICITY. Nothing here varies how
     poisonous the chemical is, and the dial's labels never suggest it does.

     ⚠️ THE HARM FLAG IS PER ROW AND PER SETTING, so a row that is safe on the
     slow chemical and harmful on the persistent one changes both its colour
     and its words when the tab moves. Neither is a mark: it is a quantity
     against a threshold. */
  function wireBioaccumulation(sec) {
    var w = sec.querySelector("[data-ba]");
    if (!w) { return; }
    var tabs = toArray(w.querySelectorAll(".ks3-ba-tab"));
    var levels = toArray(w.querySelectorAll(".ks3-ba-level"));
    var up = w.querySelector("[data-ba-up]");
    var resetBtn = w.querySelector("[data-ba-reset]");
    var noteEl = w.querySelector("[data-ba-chemnote]");
    var verdictEl = w.querySelector("[data-ba-verdict]");
    if (!tabs.length || !levels.length || !up) { return; }

    var HARM = parseFloat(w.getAttribute("data-harm")) || 0;
    var SUFFIX = w.getAttribute("data-ppm-suffix") || "";
    var HARMV = w.getAttribute("data-harm-verdict") || "";
    var SAFEV = w.getAttribute("data-safe-verdict") || "";
    var STEP = w.getAttribute("data-step-label") || "";
    var SPENT = w.getAttribute("data-step-spent-label") || "";
    var FLAT = w.getAttribute("data-verdict-flat") || "";
    var HARMFUL = w.getAttribute("data-verdict-harmful") || "";
    var BELOW = w.getAttribute("data-verdict-below") || "";

    var current = tabs[0];
    each(tabs, function (tb) {
      if (tb.getAttribute("aria-pressed") === "true") { current = tb; }
    });
    var shown = 1, everTopped = false;
    var total = levels.length;

    /* MRB-257 (5.23) — the bars are LOGARITHMIC, over one domain shared by
       every chemical.
       Linear, and rescaled per tab, they were unreadable and incomparable
       at once: 0.0030, 0.030, 0.300 and 3.0 ppm all drew at the 1% floor —
       including the step from "no measurable effect" to "above the level
       that causes harm", drawn as no change — while 0.729 ppm on one tab
       drew 72.9% against 300 ppm at 100% on another. A hundred-thousandfold
       range is what the lesson is about, and a linear axis cannot show it.
       The domain runs from the lowest starting concentration on any tab to
       the highest top (or the harm line, whichever is greater), so one
       decade is the same width everywhere and the three chemicals can be
       read against each other. */
    var logMin = 0, logSpan = 0;
    (function () {
      var lo = 0, hi = HARM;
      each(tabs, function (tb) {
        var st = parseFloat(tb.getAttribute("data-start")) || 0;
        var fa = parseFloat(tb.getAttribute("data-factor")) || 1;
        if (st > 0 && (lo === 0 || st < lo)) { lo = st; }
        var tp = st * Math.pow(fa, total - 1);
        if (tp > hi) { hi = tp; }
      });
      if (lo > 0 && hi > lo) {
        logMin = Math.log(lo);
        logSpan = Math.log(hi) - logMin;
      }
    }());

    function barPct(conc) {
      if (!(conc > 0)) { return 1; }
      var pct = logSpan > 0
        ? ((Math.log(conc) - logMin) / logSpan) * 100
        : 100;
      return Math.max(1, Math.min(100, pct));
    }

    function draw() {
      var factor = parseFloat(current.getAttribute("data-factor")) || 1;
      var start = parseFloat(current.getAttribute("data-start")) || 0;
      var top = start * Math.pow(factor, total - 1);
      each(tabs, function (tb) {
        tb.setAttribute("aria-pressed", tb === current ? "true" : "false");
      });
      if (noteEl) { noteEl.textContent = current.getAttribute("data-note") || ""; }

      each(levels, function (li, i) {
        var conc = start * Math.pow(factor, i);
        var harmful = conc >= HARM;
        var on = i < shown;
        if (on) { li.setAttribute("data-shown", ""); }
        else { li.removeAttribute("data-shown"); }
        if (i === shown - 1) { li.setAttribute("data-cur", ""); }
        else { li.removeAttribute("data-cur"); }
        if (harmful) { li.setAttribute("data-harmful", "1"); }
        else { li.removeAttribute("data-harmful"); }
        var ppm = li.querySelector("[data-ba-ppm]");
        var lv = li.querySelector("[data-ba-lvlverdict]");
        var bar = li.querySelector("[data-ba-bar]");
        if (ppm) { ppm.textContent = b9Ppm(conc) + SUFFIX; }
        if (lv) { lv.textContent = harmful ? HARMV : SAFEV; }
        if (bar) { bar.style.width = barPct(conc) + "%"; }
        setHidden(li.querySelector(".ks3-ba-readout"), !on);
      });

      var topped = shown >= total;
      up.textContent = topped ? SPENT : STEP;
      up.disabled = topped;
      if (verdictEl) {
        if (topped) {
          var text;
          if (factor === 1) {
            text = FLAT;
          } else if (top >= HARM) {
            text = HARMFUL.split("{ppm}").join(b9Ppm(top))
              .split("{times}").join(b9Group(Math.round(top / start)));
          } else {
            text = BELOW.split("{ppm}").join(b9Ppm(top));
          }
          verdictEl.textContent = text;
        }
        setHidden(verdictEl, !topped);
      }
      setCount(sec, shown);
      if (topped) { everTopped = true; }
      markStage(sec, everTopped);
    }

    each(tabs, function (tb) {
      tb.addEventListener("click", function () {
        current = tb;
        shown = 1;
        draw();
      });
    });
    up.addEventListener("click", function () { shown += 1; draw(); });
    if (resetBtn) {
      resetBtn.addEventListener("click", function () { shown = 1; draw(); });
    }
    draw();
  }

  /* ── quadrat-bench (b9-06 #s-bench) ──

     ⚖️ MORE QUADRATS FIXES CHANCE AND DOES NOTHING FOR BIAS, and that falls
     out of the POOLS rather than out of any special-casing here. The corner
     pool is twenty-five squares entirely inside the cluster, so the
     twenty-five-quadrat setting EXHAUSTS it: the largest sample on the biased
     dial is deterministic, and the answer stops wobbling without getting any
     better. `build_ks3.py` measures both biased pools against the field's own
     model and refuses a set that is not biased in both directions.

     ⚠️ THE FIELD IS BUILT HERE, UNSEEDED, ONCE PER PAGE LOAD. This is the only
     `Math.random()` in B9 — a hundred calls at wire time. Two students never
     see the same field and no student sees the same one twice, so the estimate
     cannot be memorised and the reveal cannot be spoiled. It is also why the
     shipped grid is a hundred EMPTY cells: that is not a placeholder for the
     live page, it is exactly what an unsurveyed field looks like. */
  function wireQuadratBench(sec) {
    var w = sec.querySelector("[data-qb]");
    if (!w) { return; }
    var F = b9Json(w, "data-field");
    var VERDICTS = b9Json(w, "data-verdicts");
    var DIRECTION = b9Json(w, "data-direction");
    var cells = toArray(w.querySelectorAll(".ks3-qb-cell"));
    var methodTabs = toArray(w.querySelectorAll("[data-qb-method]"));
    var countTabs = toArray(w.querySelectorAll("[data-qb-count]"));
    var figuresEl = w.querySelector("[data-qb-figures]");
    var captionEl = w.querySelector("[data-qb-caption]");
    var gridEl = w.querySelector("[data-qb-grid]");
    var sampleBtn = w.querySelector("[data-qb-sample]");
    var truthBtn = w.querySelector("[data-qb-truth]");
    var verdictEl = w.querySelector("[data-qb-verdict]");
    if (!F || !VERDICTS || !cells.length || !sampleBtn || !truthBtn) { return; }

    var SIDE = parseInt(w.getAttribute("data-side"), 10) || 10;
    var SAMPLE = w.getAttribute("data-sample-label") || "";
    var RESAMPLE = w.getAttribute("data-resample-label") || "";
    var CAP_UN = w.getAttribute("data-caption-unsampled") || "";
    var CAP_S = w.getAttribute("data-caption-sampled") || "";
    var CAP_R = w.getAttribute("data-caption-revealed") || "";
    var HIDDEN = w.getAttribute("data-hidden-value") || "";
    /* MRB-257 (5.6) — the error a random sample lands on, in per cent, at or
       below which the sample counts as a good one. Read from the widget so
       the number stays the author's; the fallback is only there because no
       shipped payload carries the attribute yet. */
    var GOOD_WITHIN = Number(w.getAttribute("data-good-within"));
    if (!(GOOD_WITHIN > 0)) { GOOD_WITHIN = 10; }

    /* The clustering model, term for term as `build_ks3.py` asserts against
       it. The square on the richness is what makes a tight CLUSTER rather than
       a gradient, and a gradient would leave every method very nearly right. */
    var field = [], r, c;
    for (r = 0; r < SIDE; r++) {
      for (c = 0; c < SIDE; c++) {
        var richness = Math.max(0, 1 - (Math.abs(c - F.centre_col) +
          Math.abs(r - F.centre_row)) / F.reach);
        var base = F.base + richness * richness * F.peak;
        field.push(Math.max(0,
          Math.round(base + (Math.random() - 0.5) * F.noise)));
      }
    }
    var realTotal = 0;
    for (r = 0; r < field.length; r++) { realTotal += field[r]; }

    var method = "random", count = parseInt(w.getAttribute("data-count"), 10) || 8;
    each(methodTabs, function (tb) {
      if (tb.getAttribute("aria-pressed") === "true") {
        method = tb.getAttribute("data-qb-method");
      }
    });
    var picked = [], truthShown = false, everRevealed = false;

    function pool(m) {
      var out = [], i, rr, cc;
      for (i = 0; i < SIDE * SIDE; i++) {
        rr = Math.floor(i / SIDE);
        cc = i % SIDE;
        if (m === "corner" && !(rr >= SIDE / 2 && cc <= (SIDE / 2) - 1)) { continue; }
        if (m === "path" && rr > 2) { continue; }
        out.push(i);
      }
      return out;
    }

    function takeSample() {
      var p = pool(method), n = Math.min(count, p.length), i;
      picked = [];
      /* Without replacement — `splice`, as Design does. With replacement the
         twenty-five-quadrat corner setting would stop being deterministic and
         the "it just stops wobbling" claim would stop being true. */
      for (i = 0; i < n; i++) {
        picked.push(p.splice(Math.floor(Math.random() * p.length), 1)[0]);
      }
      truthShown = false;
      draw();
    }

    function fig(id, value) {
      var el = w.querySelector('[data-qb-fig="' + id + '"]');
      if (el) { el.textContent = value; }
    }

    function draw() {
      var sampled = picked.length > 0, i, sum = 0;
      for (i = 0; i < picked.length; i++) { sum += field[picked[i]]; }
      var mean = sampled ? sum / picked.length : 0;
      /* MRB-257 (5.5) — the estimate is computed from the mean AS PRINTED,
         not from the unrounded one. It used to print "Mean per quadrat 9.1"
         beside "Estimated total 913", so a student doing the bench's own
         arithmetic — the method card's "divide by the number of quadrats…
         then multiply", which rung 1 marks — was wrong about two runs in
         three. Two decimals, because the mean is what a student writes down
         and then multiplies; the error line follows the estimate that is
         actually on screen. */
      var meanText = mean.toFixed(2);
      var estimate = Math.round(Number(meanText) * SIDE * SIDE);
      var errPct = sampled
        ? Math.round(((estimate - realTotal) / realTotal) * 100) : 0;

      each(methodTabs, function (tb) {
        tb.setAttribute("aria-pressed",
          tb.getAttribute("data-qb-method") === method ? "true" : "false");
      });
      each(countTabs, function (tb) {
        tb.setAttribute("aria-pressed",
          parseInt(tb.getAttribute("data-qb-count"), 10) === count
            ? "true" : "false");
      });

      each(cells, function (el, i2) {
        var inSample = picked.indexOf(i2) >= 0;
        var show = inSample || truthShown;
        var shade = Math.min(0.75, field[i2] / F.shade_max);
        el.textContent = show ? String(field[i2]) : "";
        el.style.backgroundColor = "rgba(228, 87, 46, " +
          (truthShown ? shade : (inSample ? Math.max(0.35, shade) : 0.08)) + ")";
        if (inSample) { el.setAttribute("data-in-sample", "1"); }
        else { el.removeAttribute("data-in-sample"); }
      });

      var capNow = truthShown ? CAP_R : (sampled ? CAP_S : CAP_UN);
      if (captionEl) { captionEl.textContent = capNow; }
      /* MRB-257 (5.55) — the grid is `role="img"`, so its `aria-label` IS
         the picture for a screen-reader user. It was authored once and
         never updated, leaving "one hundred square metres, contents
         hidden" after every square had been revealed. Same string the
         sighted caption gets, which is the point: one description. */
      if (gridEl) { gridEl.setAttribute("aria-label", capNow); }
      fig("mean", meanText);
      fig("estimate", b9Group(estimate));
      fig("real", truthShown ? b9Group(realTotal) : HIDDEN);
      if (figuresEl) { setHidden(figuresEl, !sampled); }
      var realEl = w.querySelector('[data-qb-figure="real"]');
      if (realEl) {
        if (truthShown) { realEl.setAttribute("data-revealed", "1"); }
        else { realEl.removeAttribute("data-revealed"); }
      }

      sampleBtn.textContent = sampled ? RESAMPLE : SAMPLE;
      truthBtn.disabled = !sampled || truthShown;

      if (verdictEl) {
        if (truthShown) {
          /* ⚖️ FOUR BRANCHES IN DESIGN'S ORDER, AND THE THIRD IS TESTED LAST
             OF THE THREE THAT CAN FIRE. Bias is named before chance, because a
             biased three-quadrat sample is biased AND unlucky and only one of
             those is the thing more work cannot fix. */
          /* MRB-257 (5.6) — the last branch tests the ERROR, not the sample
             size. It used to read `picked.length <= 3`, so eight quadrats
             28% out were congratulated ("the sample size kept it steady")
             and three quadrats 2% out were scolded — on the one bench in
             the key stage built to teach the difference between chance
             error and bias. Bias is still named first, for the reason
             below. */
          var key = method === "corner" ? "corner"
            : (method === "path" ? "path"
              : (Math.abs(errPct) > GOOD_WITHIN ? "chance" : "good"));
          verdictEl.textContent = (VERDICTS[key] || "")
            .split("{err}").join(String(Math.abs(errPct)))
            .split("{n}").join(String(picked.length))
            .split("{dir}").join(errPct > 0
              ? (DIRECTION && DIRECTION.over) || ""
              : (DIRECTION && DIRECTION.under) || "");
        }
        setHidden(verdictEl, !truthShown);
      }

      setCount(sec, picked.length);
      if (truthShown) { everRevealed = true; }
      markStage(sec, everRevealed);
    }

    each(methodTabs, function (tb) {
      tb.addEventListener("click", function () {
        method = tb.getAttribute("data-qb-method");
        picked = [];
        truthShown = false;
        draw();
      });
    });
    each(countTabs, function (tb) {
      tb.addEventListener("click", function () {
        count = parseInt(tb.getAttribute("data-qb-count"), 10) || count;
        picked = [];
        truthShown = false;
        draw();
      });
    });
    sampleBtn.addEventListener("click", takeSample);
    truthBtn.addEventListener("click", function () {
      truthShown = true;
      draw();
    });
    draw();
  }

/* ═══ END B9 ═══ */

/* ═══ BEGIN B10 ═══ */

  /* ── B10 · Inheritance and DNA (⊕ MRB-248) ──
     Five instruments, five wire functions. All five are DOM-only: no canvas,
     no `requestAnimationFrame`, no `setTimeout`, no `setInterval` — grepped
     across all five of Design's approved pages and zero on every term
     (schema §0.1). So there is no rAF loop in this section to test
     `prefers-reduced-motion` inside (contract R4, the b2-03 slip), and the
     unit's one transition is covered by R6's platform rule.

     ⚠️ AND THE STAGE PREDICATE IS MONOTONIC ON ALL FIVE. MRB-208 ruled the
     rail records PARTICIPATION: what a student found out cannot be un-found
     by switching tabs or starting again. Every threshold below counts a
     STICKY set, never live state.

     ⚠️ AND EACH BENCH'S MARKER IS READ TWICE (MRB-249). The band section
     beside it — `s-two`, `s-model`, `s-who`, `s-steps`, `s-test` — carries no
     control of its own and its rail entry MIRRORS `s-bench`, resolved in
     `wireRail`'s `paint()`. So a threshold moved for convenience here moves
     two stops, not one. Design states each one in her own `isDone()` and the
     renderer in `build_ks3.py` refuses a payload that cannot reach it.

     ⛔ AND THREE OF THE FIVE ADJUDICATE A COMMITMENT — b10-01's prediction,
     b10-03's evidence, b10-05's verdict — which is a deliberate departure
     from B7 §0.6, recorded in schema §0.6 and measured off Design's own
     pages. The verdict is WORDS on a cream panel, in one tone whichever way
     it went. No green, no red, no badge, no mark on an option button, and
     never the amber `is-wrong` ladder treatment. Only the mastery ladder
     marks correctness (MRB-196 R10). */

  /* ── variation-plotter (b10-01 #s-bench) ──

     ⚖️ THE STUDENT CANNOT SEE THE GRAPH BEFORE COMMITTING TO A SHAPE. The
     plot button is disabled until this characteristic has a prediction, and
     once plotted it cannot be re-run and its predict buttons go away. That is
     Law 4 built into the instrument rather than layered over it, and it is
     why there is NO RESET: six characteristics, one prediction each, is the
     whole exercise.

     ⚖️ THE BAR GAP IS NOT SET HERE AND MUST NOT BE. It is a pure function of
     `data-vp-type` in the stylesheet — continuous bars fill their column and
     touch, discontinuous bars are 6px narrower and stand apart — so the
     histogram / bar-chart convention cannot be overridden by a payload or by
     a runtime branch. See the rule pair in `shared/ks3.css`.

     ⚖️ THE VERDICT JUDGES THE PREDICTION, IN WORDS, IN ONE TONE. Both tags
     are already in the document; this only chooses which one is shown. It
     never adds a class to an option button, and the prediction the student
     made keeps exactly the ground it had — a wrong idea is corrected on the
     cream panel, not marked on the button. */
  function wireVariationPlotter(sec) {
    var w = sec.querySelector("[data-vp]");
    if (!w) { return; }
    var tabs = toArray(w.querySelectorAll(".ks3-vp-tab"));
    var panels = toArray(w.querySelectorAll("[data-vp-charpanel]"));
    var plotBtn = w.querySelector("[data-vp-plot]");
    if (!tabs.length || !panels.length || !plotBtn) { return; }

    var RUN = w.getAttribute("data-run-label") || "";
    var RUN_DONE = w.getAttribute("data-run-done-label") || "";
    /* Design's own `isDone()` threshold, emitted by the renderer rather than
       written twice. The `s-two` band stop mirrors this stop, so the number
       is read by two rail entries. */
    var NEED = parseInt(w.getAttribute("data-threshold"), 10) || 0;

    /* The opening state IS the markup: the characteristic Design opens on is
       already pressed, so there is no second copy of the default here to fall
       out of step with the shipped bytes. */
    var current = tabs[0];
    each(tabs, function (tb) {
      if (tb.getAttribute("aria-pressed") === "true") { current = tb; }
    });
    /* `plotted` is STICKY and there is no control that clears it. */
    var plotted = {};

    function panelFor(id) {
      var found = panels[0], i;
      for (i = 0; i < panels.length; i++) {
        if (panels[i].getAttribute("data-vp-charpanel") === id) {
          found = panels[i];
        }
      }
      return found;
    }

    function predictionIn(panel) {
      var chosen = panel.querySelector('.ks3-vp-pred[aria-pressed="true"]');
      return chosen ? chosen.getAttribute("data-vp-pred") : null;
    }

    function draw() {
      var id = current.getAttribute("data-vp-char");
      var panel = panelFor(id);
      var done = !!plotted[id];
      var n = 0, k;
      for (k in plotted) { if (plotted[k]) { n += 1; } }

      each(tabs, function (tb) {
        tb.setAttribute("aria-pressed", tb === current ? "true" : "false");
      });
      each(panels, function (p) { setHidden(p, p !== panel); });

      /* Once plotted the prediction is spent: the buttons go, and the graph
         and its verdict arrive in the space they were holding. */
      setHidden(panel.querySelector("[data-vp-predict]"), done);
      setHidden(panel.querySelector("[data-vp-graph]"), !done);

      /* ⚖️ ONE TAG, CHOSEN, NEVER COMPOSED. Both sentences are in the
         document already, so nothing science-bearing is assigned to
         `textContent` and a reader with JS off has both. */
      var right = predictionIn(panel) ===
        panel.querySelector(".ks3-vp-chart").getAttribute("data-vp-type");
      setHidden(panel.querySelector('[data-vp-tag="right"]'),
                !done || !right);
      setHidden(panel.querySelector('[data-vp-tag="wrong"]'),
                !done || right);

      plotBtn.textContent = done ? RUN_DONE : RUN;
      plotBtn.disabled = done || !predictionIn(panel);

      setCount(sec, n);
      /* ⚠️ MONOTONIC, and free to be: `plotted` is sticky and there is no
         reset on this bench. Switching characteristic cannot untick a stop a
         student has already reached — and two stops read this one call. */
      markStage(sec, n >= NEED);
    }

    each(tabs, function (tb) {
      tb.addEventListener("click", function () { current = tb; draw(); });
    });

    each(w.querySelectorAll(".ks3-vp-pred"), function (btn) {
      btn.addEventListener("click", function () {
        var panel = btn.closest ? btn.closest("[data-vp-charpanel]") : null;
        if (!panel) { return; }
        /* A prediction already made cannot be changed once it has been
           plotted — the buttons are gone by then, and this is the guard for
           a keyboard or assistive path that reaches one anyway. */
        if (plotted[panel.getAttribute("data-vp-charpanel")]) { return; }
        each(panel.querySelectorAll(".ks3-vp-pred"), function (other) {
          other.setAttribute("aria-pressed",
                             other === btn ? "true" : "false");
        });
        draw();
      });
    });

    plotBtn.addEventListener("click", function () {
      var id = current.getAttribute("data-vp-char");
      /* The gate again, in the handler. `disabled` is the drawn half of it
         and this is the half a synthetic click cannot get past. */
      if (plotted[id] || !predictionIn(panelFor(id))) { return; }
      plotted[id] = true;
      draw();
      /* MRB-257 (5.43) — the graph has just replaced the prediction buttons
         and this button has just disabled. Focused after `draw()` because a
         hidden element cannot take focus. */
      focusReveal(panelFor(id).querySelector("[data-vp-graph]"));
    });

    draw();
  }

  /* ── zoom-bench (b10-02 #s-bench) ──

     ⚖️ EVERY LEVEL IS DRAWN FROM THE START AND ONLY THE `body` ARRIVES. The
     name and the scale are on screen at 45% from the first paint, so the
     SCALE COLUMN — which is the lesson's argument — is readable as a column
     before the journey begins. Nothing here hides a row.

     ⚠️ `Back out` GOES TO LEVEL ONE AND UNTELLS NOTHING. It resets the view,
     not the record: `everBottomed` is sticky, so a student who has been all
     the way down keeps the stop they reached (MRB-208, and the `s-model` band
     stop mirrors it, so an unticking reset would move two).

     ⚠️ AND THE SAY-IT-BACK PANEL GATES NOTHING AND MARKS NOTHING. The answers
     are already in the document, one per question; choosing a tab chooses
     which is shown. A pressed tab says which question is being looked at,
     never that anyone was right (MRB-196 R10). */
  function wireZoomBench(sec) {
    var w = sec.querySelector("[data-zb]");
    if (!w) { return; }
    var levels = toArray(w.querySelectorAll(".ks3-zb-level"));
    var inBtn = w.querySelector("[data-zb-in]");
    var outBtn = w.querySelector("[data-zb-out]");
    var closeEl = w.querySelector("[data-zb-close]");
    if (!levels.length || !inBtn) { return; }

    var IN = w.getAttribute("data-in-label") || "";
    var IN_DONE = w.getAttribute("data-in-done-label") || "";
    var TOTAL = levels.length;
    var shown = 1, everBottomed = false;

    function draw() {
      if (shown > TOTAL) { shown = TOTAL; }
      if (shown < 1) { shown = 1; }
      each(levels, function (li, i) {
        var on = i < shown;
        if (on) { li.setAttribute("data-shown", ""); }
        else { li.removeAttribute("data-shown"); }
        if (i === shown - 1) { li.setAttribute("data-here", ""); }
        else { li.removeAttribute("data-here"); }
        setHidden(li.querySelector(".ks3-zb-body"), !on);
      });

      var bottomed = shown >= TOTAL;
      inBtn.textContent = bottomed ? IN_DONE : IN;
      inBtn.disabled = bottomed;
      setHidden(closeEl, !bottomed);

      setCount(sec, shown);
      if (bottomed) { everBottomed = true; }
      /* ⚠️ MONOTONIC. Design's own `isDone()` is `s.shown >= LEVELS.length`,
         which UNTICKS the moment a student presses `Back out`. MRB-208 ruled
         the rail records participation, and two stops read this one — so what
         ticks is unchanged and what unticks is nothing. */
      markStage(sec, everBottomed);
    }

    inBtn.addEventListener("click", function () {
      shown += 1;
      draw();
      /* MRB-257 (5.43) — the last press disables `Zoom in` and unhides the
         closing panel, which is where the reader now is. */
      if (shown >= TOTAL) { focusReveal(closeEl); }
    });
    if (outBtn) {
      outBtn.addEventListener("click", function () { shown = 1; draw(); });
    }

    /* The say-it-back panel. Its opening question is `opens_on` and it is
       ALREADY PRESSED in the markup — the second question, not the first,
       because that one states the whole nesting (schema §3.2). Nothing here
       needs to know which id that was. */
    var qtabs = toArray(w.querySelectorAll(".ks3-zb-qtab"));
    var answers = toArray(w.querySelectorAll("[data-zb-answer]"));
    each(qtabs, function (tb) {
      tb.addEventListener("click", function () {
        var id = tb.getAttribute("data-zb-q");
        each(qtabs, function (other) {
          other.setAttribute("aria-pressed", other === tb ? "true" : "false");
        });
        each(answers, function (p) {
          setHidden(p, p.getAttribute("data-zb-answer") !== id);
        });
      });
    });

    draw();
  }

  /* ── model-builder (b10-03 #s-bench) ──

     ⚖️⚖️ THE FOUR CARDS RE-EVALUATE LIVE ON EVERY DIAL PRESS. There is no run
     button and no reset button (schema §4.3) — the bench opens on Pauling's
     wrong model with all four cards red, and every dial the student touches
     can only improve it. Elimination as a monotone descent.

     ⚖️ A CARD PASSES WHEN EVERY `requires` PAIR MATCHES **AND** THE `forbids`
     MAP IS NOT MATCHED IN FULL. Three of Design's tests are a single equality;
     Pauling's is a negated conjunction, `!(strands==='3' && bases==='out')`.
     Read `forbids` as an OR and it fires on three strands alone — which would
     rule out a model the evidence does not rule out and break the
     "exactly one of twelve" claim `build_ks3.py` proves at build time.

     ⛔ THE VERDICT IS ON THE MODEL, NEVER ON THE STUDENT. A failing card takes
     the alert outline and unhides the elimination line; a passing one takes
     the green. The DIAL BUTTONS take no verdict class at any point — a pressed
     dial is "this is the model on the bench" and nothing more (MRB-196 R10).

     ⚠️ `solved` IS STICKY, by Design's own construction. A student who reaches
     the double helix and then goes back to break the model on purpose keeps
     the stop, and the `s-who` band stop mirrors it (MRB-249). */
  function wireModelBuilder(sec) {
    var w = sec.querySelector("[data-dh]");
    if (!w) { return; }
    var opts = toArray(w.querySelectorAll(".ks3-dh-opt"));
    var cards = toArray(w.querySelectorAll("[data-dh-card]"));
    var lineEl = w.querySelector("[data-dh-modelline]");
    var tagEl = w.querySelector("[data-dh-verdicttag]");
    var bodyEl = w.querySelector("[data-dh-verdictbody]");
    if (!opts.length || !cards.length) { return; }

    var CORRECT = b9Json(w, "data-target") || {};
    var TAG_PASS = w.getAttribute("data-tag-pass") || "";
    var TAG_ONE = w.getAttribute("data-tag-fail-one") || "";
    var TAG_MANY = w.getAttribute("data-tag-fail-many") || "";
    var V_PASS = w.getAttribute("data-verdict-pass") || "";
    var V_FAIL = w.getAttribute("data-verdict-fail") || "";
    var solved = false;

    /* The opening model IS the markup: the dials Design opens on are already
       pressed, so there is no second copy of Pauling's preset here to fall out
       of step with the shipped bytes. */
    function model() {
      var m = {};
      each(opts, function (b) {
        if (b.getAttribute("aria-pressed") === "true") {
          m[b.getAttribute("data-dh-dial")] = b.getAttribute("data-dh-opt");
        }
      });
      return m;
    }

    function passes(m, card) {
      var req = b9Json(card, "data-dh-requires") || {};
      var forb = b9Json(card, "data-dh-forbids") || {};
      var k, any = false, all = true;
      for (k in req) { if (m[k] !== req[k]) { return false; } }
      for (k in forb) { any = true; if (m[k] !== forb[k]) { all = false; } }
      return !(any && all);
    }

    function draw() {
      var m = model(), nFail = 0, phrases = [];

      /* The model line, `", ".join(phrase)` in DIAL ORDER — the order the
         decisions are drawn in, which is the order the sentence reads in.
         Built from the same `data-dh-phrase` attributes `build_ks3.py` used
         for the resting render, so the two cannot disagree. */
      each(opts, function (b) {
        if (b.getAttribute("aria-pressed") === "true") {
          phrases.push(b.getAttribute("data-dh-phrase") || "");
        }
      });
      if (lineEl) { lineEl.textContent = phrases.join(", "); }

      each(cards, function (card) {
        var ok = passes(m, card);
        if (ok) { card.setAttribute("data-pass", ""); }
        else { card.removeAttribute("data-pass"); nFail += 1; }
        setHidden(card.querySelector('[data-dh-tag="pass"]'), !ok);
        setHidden(card.querySelector('[data-dh-tag="fail"]'), ok);
        setHidden(card.querySelector(".ks3-dh-why"), ok);
      });

      if (tagEl) {
        tagEl.textContent = nFail === 0 ? TAG_PASS
          : (nFail === 1 ? TAG_ONE : TAG_MANY).replace("{n}", String(nFail));
      }
      if (bodyEl) { bodyEl.textContent = nFail === 0 ? V_PASS : V_FAIL; }

      setCount(sec, cards.length - nFail);
      var ok = true, k;
      for (k in CORRECT) { if (m[k] !== CORRECT[k]) { ok = false; } }
      if (ok) { solved = true; }
      markStage(sec, solved);
    }

    each(opts, function (b) {
      b.addEventListener("click", function () {
        var dial = b.getAttribute("data-dh-dial");
        each(opts, function (other) {
          if (other.getAttribute("data-dh-dial") === dial) {
            other.setAttribute("aria-pressed", other === b ? "true" : "false");
          }
        });
        draw();
      });
    });

    draw();
  }

  /* ── pea-cross (b10-04 #s-bench) ──

     ⚖️⚖️ THE RANDOMNESS IS REAL AND UNSEEDED AND STAYS THAT WAY (schema §5.1).
     One `Math.random()` per gamete, per parent, per seed. No PRNG, no seed,
     and no seed key — `r_pea_cross` refuses one. A 3:1 ratio is a SAMPLING
     result, not a property of any one litter, and a bench that delivered
     75/25 on cue would teach exactly the belief the page's legal line and rung
     4 are written to break. No student sees the same cross twice.

     ⚠️ CHANGING EITHER PARENT CLEARS THE TALLY AND THE LAST SEED. Without it a
     student accumulates counts across two DIFFERENT crosses and reads a ratio
     that describes neither. Design wires the clear on her own handler; so does
     this, and the drive asserts it.

     ⚠️ GROWING A HUNDRED HIDES THE MOST-RECENT-SEED CARD. One seed is the
     "chance decides each one" story, a hundred is the "only totals show the
     pattern" story, and they are never on screen together.

     ⚖️ AND THE LAST SEED'S GENOTYPE IS NORMALISED DOMINANT-FIRST: a seed that
     received `p` then `P` prints `Pp`, never `pP`. Two spellings of one
     genotype on one bench is two things as far as a student is concerned. */
  function wirePeaCross(sec) {
    var w = sec.querySelector("[data-pc]");
    if (!w) { return; }
    var genoBtns = toArray(w.querySelectorAll(".ks3-pc-geno"));
    var rows = toArray(w.querySelectorAll("[data-pc-row]"));
    var oneBtn = w.querySelector("[data-pc-one]");
    var manyBtn = w.querySelector("[data-pc-many]");
    var clearBtn = w.querySelector("[data-pc-clear]");
    if (!genoBtns.length || !rows.length || !oneBtn) { return; }

    var G = b9Json(w, "data-genotypes") || {};
    var DOM = w.getAttribute("data-dominant");
    var REC = w.getAttribute("data-recessive");
    var MANY = parseInt(w.getAttribute("data-many-n"), 10) || 100;
    var JOIN = w.getAttribute("data-cross-join") || "";
    var LAST_T = w.getAttribute("data-last-template") || "";
    var P_DOM = w.getAttribute("data-pheno-dominant") || "";
    var P_REC = w.getAttribute("data-pheno-recessive") || "";
    var RATIO_T = w.getAttribute("data-ratio-template") || "";
    var NOREC_T = w.getAttribute("data-no-recessive-template") || "";
    /* MRB-257 (5.45) — the mirror of NOREC_T. `pp × pp` grows a hundred white
       plants and printed "Ratio purple to white — 0.00 : 1"; so did any
       sample of one that came up white. A ratio needs both phenotypes.
       (5.44) — and both lines are counts, so both need a singular: "in 1
       seeds" is a state a student reaches here on purpose. */
    var NODOM_T = w.getAttribute("data-no-dominant-template") || "";
    var NOREC_1 = w.getAttribute("data-no-recessive-template-one") || "";
    var NODOM_1 = w.getAttribute("data-no-dominant-template-one") || "";
    var SUF_ONE = w.getAttribute("data-suffix-one") || "";
    var SUF_MANY = w.getAttribute("data-suffix-many") || "";

    var crossEl = w.querySelector("[data-pc-crossline]");
    var lastEl = w.querySelector("[data-pc-last]");
    var lastLine = w.querySelector("[data-pc-lastline]");
    var tallyEl = w.querySelector("[data-pc-tally]");
    var ratioEl = w.querySelector("[data-pc-ratio]");
    var notes = toArray(w.querySelectorAll("[data-pc-note]"));

    var tally = { dominant: 0, recessive: 0 };
    var last = null, everTwenty = false;
    var NEED = 20;

    function chosen(parentId) {
      var got = null;
      each(genoBtns, function (b) {
        if (b.getAttribute("data-pc-parent") === parentId &&
            b.getAttribute("aria-pressed") === "true") {
          got = b.getAttribute("data-pc-geno");
        }
      });
      return got;
    }

    function parentIds() {
      var ids = [];
      each(genoBtns, function (b) {
        var p = b.getAttribute("data-pc-parent");
        if (ids.indexOf(p) < 0) { ids.push(p); }
      });
      return ids;
    }

    /* Design's four-branch chain, in HER order, first match wins.
       `both_carriers` before `mixed` or Pp × Pp stops being Mendel's 3:1 and
       becomes the generic line. */
    function hasNote(id) {
      for (var i = 0; i < notes.length; i++) {
        if (notes[i].getAttribute("data-pc-note") === id) { return true; }
      }
      return false;
    }

    function noteId(g1, g2) {
      var a = G[g1] || [], b = G[g2] || [];
      function has(x, ch) { return x.indexOf(ch) >= 0; }
      function pure(x, ch) { return x.length === 2 && x[0] === ch && x[1] === ch; }
      if (!(has(a, REC) && has(b, REC)) && (pure(a, DOM) || pure(b, DOM))) {
        /* MRB-257 / MRB-255 (5.38) — ONE BRANCH WAS COVERING THREE CROSSES
           and its sentence is only true of one of them. It ends "…and some
           of them are quietly carrying p, which will show up in the
           generation after." That is right for PP × Pp; with both parents
           PP no offspring can carry p at all, and for PP × pp every single
           one does. A promise of hidden recessives that cannot exist is the
           misconception this lesson is built to remove, printed by the
           lesson.
           The split is here; the two new sentences are a records job, so
           each specific id falls back to the old branch until one is
           authored — see HANDOFF. */
        if (pure(a, DOM) && pure(b, DOM) && hasNote("both_pure_dominant")) {
          return "both_pure_dominant";
        }
        if (((pure(a, DOM) && pure(b, REC)) || (pure(a, REC) && pure(b, DOM)))
            && hasNote("pure_dominant_x_pure_recessive")) {
          return "pure_dominant_x_pure_recessive";
        }
        return "one_pure_dominant";
      }
      if (pure(a, REC) && pure(b, REC)) { return "both_pure_recessive"; }
      if (has(a, DOM) && has(a, REC) && has(b, DOM) && has(b, REC)) {
        return "both_carriers";
      }
      return "mixed";
    }

    function grow(n) {
      var ids = parentIds();
      var a = G[chosen(ids[0])] || [], b = G[chosen(ids[1])] || [];
      var i, g1, g2, seed = null;
      for (i = 0; i < n; i++) {
        /* ⚖️ ONE `Math.random()` PER GAMETE, PER PARENT, PER SEED. This is the
           lesson: each parent passes one of its two copies, chosen by chance.
           Nothing here is seeded and nothing here may become seeded. */
        g1 = a[Math.floor(Math.random() * a.length)];
        g2 = b[Math.floor(Math.random() * b.length)];
        if (g1 === REC && g2 === REC) { tally.recessive += 1; }
        else { tally.dominant += 1; }
        seed = { g1: g1, g2: g2 };
      }
      /* Growing more than one clears the single-seed card: the two stories are
         never on screen together. */
      last = n === 1 ? seed : null;
      draw();
    }

    function draw() {
      var ids = parentIds();
      var g1 = chosen(ids[0]), g2 = chosen(ids[1]);
      var total = tally.dominant + tally.recessive;

      if (crossEl) { crossEl.textContent = g1 + " " + JOIN + " " + g2; }

      setHidden(lastEl, !last);
      if (last && lastLine) {
        /* Dominant-first, always. `pP` is never printed. */
        var geno = (last.g1 === REC && last.g2 === DOM)
          ? DOM + REC : last.g1 + last.g2;
        var pheno = (last.g1 === REC && last.g2 === REC) ? P_REC : P_DOM;
        lastLine.textContent = LAST_T
          .replace("{g1}", last.g1).replace("{g2}", last.g2)
          .replace("{genotype}", geno).replace("{phenotype}", pheno);
      }

      setHidden(tallyEl, total === 0);
      each(rows, function (row) {
        var key = row.getAttribute("data-pc-row");
        var n = tally[key] || 0;
        var pct = total ? (n / total) * 100 : 0;
        row.querySelector("[data-pc-value]").textContent =
          total ? (n + " · " + Math.round(pct) + "%") : String(n);
        row.querySelector("[data-pc-bar]").style.width = pct + "%";
      });
      if (ratioEl) {
        /* MRB-257 (5.45) — a ratio needs both phenotypes. `pp × pp` grows a
           hundred white plants and printed "Ratio purple to white — 0.00 :
           1", and so did any sample of one that came up white; the mirror
           case already had its own authored line ("No white plants at all
           in {total} seeds"). With no dominant plants there is no ratio to
           state, so an authored line if one exists and otherwise nothing —
           see HANDOFF. A sample of one falls out of the same rule: one of
           the two counts is always zero. */
        if (tally.recessive === 0) {
          ratioEl.textContent = total
            ? ((total === 1 && NOREC_1) || NOREC_T)
                .replace("{total}", String(total)) : "";
        } else if (tally.dominant === 0) {
          ratioEl.textContent = total
            ? ((total === 1 && NODOM_1) || NODOM_T)
                .replace("{total}", String(total)) : "";
        } else {
          ratioEl.textContent = RATIO_T.replace("{ratio}",
            (tally.dominant / tally.recessive).toFixed(2));
        }
      }

      var want = noteId(g1, g2);
      each(notes, function (p) {
        setHidden(p, p.getAttribute("data-pc-note") !== want);
      });

      /* ⚠️ THE ONE READOUT IN THE KEY STAGE THAT NEEDS A SINGULAR. "1 seeds
         grown" would undercut the sentence beside it, and one seed is a state
         a student reaches here on purpose. */
      var count = sec.querySelector("[data-count]");
      if (count) {
        count.setAttribute("data-format",
                           "{n} " + (total === 1 ? SUF_ONE : SUF_MANY));
      }
      setCount(sec, total);

      if (total >= NEED) { everTwenty = true; }
      /* ⚠️ MONOTONIC. Clearing the plot is a view reset, not a record reset —
         MRB-208, and the `s-steps` band stop mirrors this marker. */
      markStage(sec, everTwenty);
    }

    each(genoBtns, function (b) {
      b.addEventListener("click", function () {
        var p = b.getAttribute("data-pc-parent");
        /* MRB-257 (5.45) — pressing the genotype that is ALREADY selected
           changes no cross, and used to wipe the plot anyway: a hundred
           grown seeds became "no seeds grown". */
        if (b.getAttribute("aria-pressed") === "true") { return; }
        each(genoBtns, function (other) {
          if (other.getAttribute("data-pc-parent") === p) {
            other.setAttribute("aria-pressed", other === b ? "true" : "false");
          }
        });
        /* ⚠️ A NEW CROSS IS A NEW EXPERIMENT. Counts from the old one would
           make the ratio describe neither. */
        tally = { dominant: 0, recessive: 0 };
        last = null;
        draw();
      });
    });
    oneBtn.addEventListener("click", function () { grow(1); });
    if (manyBtn) {
      manyBtn.addEventListener("click", function () { grow(MANY); });
    }
    if (clearBtn) {
      clearBtn.addEventListener("click", function () {
        tally = { dominant: 0, recessive: 0 };
        last = null;
        draw();
      });
    }

    draw();
  }

  /* ── species-cases (b10-05 #s-bench) ──

     ⚖️⚖️ THREE VERDICTS, AND THE THIRD IS THE INSTRUMENT. "The test does not
     settle it" is the correct answer for three of the seven cases, and a
     student who never selects it cannot score above four out of seven.

     ⚖️ COMMIT THEN REVEAL, PER CASE. The check button is disabled until a
     verdict is chosen; once pressed the pick is FROZEN and the unchosen
     verdicts drop to half opacity. Same gate as `variation-plotter`.

     ⛔ AND THE BENCH ADJUDICATES IN WORDS ONLY (schema §0.6). `That is the
     answer` or `Not quite` on the cream panel, one tone either way, above the
     verdict it should have been. The three buttons take NO verdict class: the
     chosen one keeps the alert outline it had, right or wrong, and the others
     dim. A wrong idea is corrected on the panel, never marked on the button
     (MRB-196 R10). */
  function wireSpeciesCases(sec) {
    var w = sec.querySelector("[data-sc]");
    if (!w) { return; }
    var tabs = toArray(w.querySelectorAll(".ks3-sc-tab"));
    var panels = toArray(w.querySelectorAll("[data-sc-panel]"));
    var checkBtn = w.querySelector("[data-sc-check]");
    var tallyEl = w.querySelector("[data-sc-tally]");
    if (!tabs.length || !panels.length || !checkBtn) { return; }

    var RUN = w.getAttribute("data-run-label") || "";
    var RUN_DONE = w.getAttribute("data-run-done-label") || "";
    var TALLY_ALL = w.getAttribute("data-tally-all") || "";
    var TALLY_SUF = w.getAttribute("data-tally-suffix") || "";
    var TOTAL = panels.length;
    var NEED = parseInt(w.getAttribute("data-threshold"), 10) || 0;

    var current = tabs[0];
    each(tabs, function (tb) {
      if (tb.getAttribute("aria-pressed") === "true") { current = tb; }
    });
    /* `opened` is STICKY per case and nothing clears it. */
    var opened = {};

    function panelFor(id) {
      var found = panels[0], i;
      for (i = 0; i < panels.length; i++) {
        if (panels[i].getAttribute("data-sc-panel") === id) {
          found = panels[i];
        }
      }
      return found;
    }

    function pickIn(panel) {
      var b = panel.querySelector('.ks3-sc-verdict[aria-pressed="true"]');
      return b ? b.getAttribute("data-sc-verdict") : null;
    }

    function draw() {
      var id = current.getAttribute("data-sc-case");
      var panel = panelFor(id);
      var isOpen = !!opened[id];
      var n = 0, k;
      for (k in opened) { if (opened[k]) { n += 1; } }

      each(tabs, function (tb) {
        tb.setAttribute("aria-pressed", tb === current ? "true" : "false");
      });
      each(panels, function (p) { setHidden(p, p !== panel); });

      each(panels, function (p) {
        if (opened[p.getAttribute("data-sc-panel")]) {
          p.setAttribute("data-sc-opened", "");
        } else {
          p.removeAttribute("data-sc-opened");
        }
      });

      setHidden(panel.querySelector("[data-sc-out]"), !isOpen);
      var right = pickIn(panel) === panel.getAttribute("data-sc-answer");
      setHidden(panel.querySelector('[data-sc-tag="right"]'),
                !isOpen || !right);
      setHidden(panel.querySelector('[data-sc-tag="wrong"]'),
                !isOpen || right);

      checkBtn.textContent = isOpen ? RUN_DONE : RUN;
      checkBtn.disabled = isOpen || !pickIn(panel);
      if (tallyEl) {
        tallyEl.textContent = n >= TOTAL
          ? TALLY_ALL : (TOTAL - n) + " " + TALLY_SUF;
      }

      setCount(sec, n);
      /* Sticky by construction, so monotonic for free — and the `s-test` band
         stop mirrors this marker (MRB-249). */
      markStage(sec, n >= NEED);
    }

    each(tabs, function (tb) {
      tb.addEventListener("click", function () { current = tb; draw(); });
    });

    each(w.querySelectorAll(".ks3-sc-verdict"), function (btn) {
      btn.addEventListener("click", function () {
        var panel = btn.closest ? btn.closest("[data-sc-panel]") : null;
        if (!panel) { return; }
        /* Once the case is opened the commitment is frozen. */
        if (opened[panel.getAttribute("data-sc-panel")]) { return; }
        each(panel.querySelectorAll(".ks3-sc-verdict"), function (other) {
          other.setAttribute("aria-pressed",
                             other === btn ? "true" : "false");
        });
        draw();
      });
    });

    checkBtn.addEventListener("click", function () {
      var id = current.getAttribute("data-sc-case");
      /* The gate again, in the handler: `disabled` is the drawn half and this
         is the half a synthetic click cannot get past. */
      if (opened[id] || !pickIn(panelFor(id))) { return; }
      opened[id] = true;
      draw();
      focusReveal(panelFor(id).querySelector("[data-sc-out]"));   // MRB-257 (5.43)
    });

    draw();
  }

/* ═══ END B10 ═══ */

/* ═══ BEGIN B11 ═════════════════════════════════════════════════════════════
   B11 · Evolution, extinction and biodiversity (⊕ MRB-248)

   ⚑ NO RANDOMNESS IN ANY OF THE FOUR, and it is load-bearing rather than
   incidental (schema §0.2). B11 teaches a process people wrongly imagine to be
   directed; a stochastic bench lets a student watch a run go "the wrong way"
   and conclude the model is broken, or watch a lucky one and conclude
   selection is a lottery. Nothing here calls `Math.random`.

   ⚑ AND NO SCIENCE-BEARING STRING IS EVER ASSIGNED TO `textContent` BY THESE
   FUNCTIONS. Every environment's five rationales, every verdict, every outcome
   text is in the shipped document, hidden — so a reader with JS off gets the
   same teaching a reader with JS on does, and the drawn marks `t()` produces
   never have to survive a `data-` attribute (`_b8_plain`'s hazard).

   ⚑ NO CANVAS, NO rAF, NO TIMER. There is no tick in this unit that would have
   to test `prefers-reduced-motion` inside itself (contract R4, the b2-03
   slip); the reduced-motion experience is the complete one (R6). */

  /* ── b11-01 `#s-bench` · advantage-bench ─────────────────────────────── */

  /* ⚖️ A SWITCHER, AND SWITCHING IS THE EXPERIMENT. There is no run button and
     no reset: five worlds, one set of animals, and the ranking reshuffles as
     the world changes underneath it.

     ⚠️ AND `seen` NEVER SHRINKS. Design's own predicate counts the truthy keys
     of a map she only ever adds to, and MRB-208 ruled that the rail records
     participation — so what ticks here is the number of worlds a student has
     LOOKED AT, and nothing unticks. Two rail stops read this: `s-bench` and
     the `s-three` band stop that mirrors it (MRB-249). */
  function wireAdvantageBench(sec) {
    var w = sec.querySelector("[data-ab]");
    if (!w) { return; }
    var tabs = toArray(w.querySelectorAll("[data-ab-env]"));
    var panels = toArray(w.querySelectorAll("[data-ab-envpanel]"));
    if (!tabs.length || !panels.length) { return; }

    var NEED = Number(w.getAttribute("data-threshold")) || 0;
    var seen = {}, nSeen = 0;

    function show(id) {
      if (!seen[id]) { seen[id] = true; nSeen += 1; }
      each(tabs, function (tb) {
        tb.setAttribute("aria-pressed",
                        tb.getAttribute("data-ab-env") === id ? "true" : "false");
      });
      each(panels, function (p) {
        setHidden(p, p.getAttribute("data-ab-envpanel") !== id);
      });
      setCount(sec, nSeen);
      markStage(sec, NEED > 0 && nSeen >= NEED);
    }

    each(tabs, function (tb) {
      tb.addEventListener("click", function () {
        show(tb.getAttribute("data-ab-env"));
      });
    });

    /* Opens on whichever environment the markup opened on, which is the first
       — Design's `env: 'winter'` with `seen: { winter: true }`. The count
       therefore starts at ONE, and `head_counter.start` already put a 1 in the
       shipped bytes so this repaint changes nothing on screen. */
    var open = w.querySelector("[data-ab-envpanel]:not([hidden])");
    show((open || panels[0]).getAttribute("data-ab-envpanel"));
  }

  /* ── b11-02 `#s-bench` · selection-runner ────────────────────────────── */

  /* ⚖️⚖️ THE RECURRENCE, AND IT IS THE WHOLE MODEL. With pale fraction `p`
     and the selected bark's two survival rates:

         survivors_pale = p · pale_surv
         survivors_dark = (1 − p) · dark_surv
         p′             = survivors_pale / (survivors_pale + survivors_dark)

     Population size is not modelled — only the fraction is carried, which is
     what the page's own legal line says. No sampling, no drift, no mutation,
     no `Math.random` (schema §0.2).

     ⚑ AND THE CONTROL SHORT-CIRCUITS RATHER THAN DIVIDING. Equal survival
     rates mean the proportion sits exactly where it was — but
     `p·0.7 / (p·0.7 + (1−p)·0.7)` is NOT bit-for-bit `p` in floating point:
     at p = 0.9 it lands on 0.9000000000000001, and fifty presses of that let
     the control creep. A control that drifts is a control you have to argue
     for instead of showing, and this bench's patchy bark is the one panel
     that shows selection NOT happening. Identical survival is identical
     survival; the division is what introduces noise the model does not have. */
  function nrStep(p, bark) {
    if (bark.control) { return p; }
    var sp = p * bark.pale, sd = (1 - p) * bark.dark;
    return sp / (sp + sd);
  }

  function wireSelectionRunner(sec) {
    var w = sec.querySelector("[data-nr]");
    if (!w) { return; }
    var M = b9Json(w, "data-model");
    var chart = w.querySelector("[data-nr-chart]");
    if (!M || !M.barks || !chart) { return; }

    var NEED = Number(w.getAttribute("data-threshold")) || 0;
    var tabs = toArray(w.querySelectorAll("[data-nr-bark]"));
    var barkNotes = toArray(w.querySelectorAll("[data-nr-barknote]"));
    var notes = toArray(w.querySelectorAll("[data-nr-note]"));
    var cols = toArray(w.querySelectorAll("[data-nr-col]"));
    var figures = toArray(w.querySelectorAll("[data-nr-series]"));
    var resetBtn = w.querySelector("[data-nr-reset]");

    var bark = M.opens_on, pale = M.start, gen = 0, everTen = false;
    var hist = [pale];

    /* ⚖️ SIX BRANCHES, IN DESIGN'S EVALUATION ORDER, FIRST MATCH WINS — with
       the gen-0 branch SPLIT IN TWO, which is the fix. Her `notes.start` fires
       on `gen === 0` alone and her reset sets `pale: 0.5, gen: 0`, so pressing
       *Start again at fifty-fifty* shows a fifty-fifty population under a
       sentence reading "Nine moths in ten are pale" (schema §3).

       ⚠️ `control` IS TESTED BEFORE THE PERCENTAGES, exactly as Design tests
       `bark === 'mixed'` before them, and it has to be: on patchy bark started
       at 90% pale, `palePct > 85` is true from the first frame and the control
       would never announce itself. */
    function noteId(palePct, darkPct) {
      if (gen === 0) { return pale === M.reset ? "reset" : "start"; }
      if (M.barks[bark].control) { return "control"; }
      if (darkPct > 85) { return "dark_high"; }
      if (palePct > 85 && M.barks[bark].pale_favoured) { return "pale_high"; }
      return "moving";
    }

    function draw() {
      var palePct = Math.round(pale * 100), darkPct = 100 - palePct, i;
      each(tabs, function (tb) {
        tb.setAttribute("aria-pressed",
                        tb.getAttribute("data-nr-bark") === bark ? "true" : "false");
      });
      each(barkNotes, function (p) {
        setHidden(p, p.getAttribute("data-nr-barknote") !== bark);
      });
      /* The chart's columns are DRAWN, all of them, and this unhides and
         resizes. Nothing is created, so there is no element churn on a
         ten-generation press and no way for a column to arrive without the
         stylesheet's rules on it. */
      for (i = 0; i < cols.length; i++) {
        var live = i < hist.length;
        setHidden(cols[i], !live);
        if (live) {
          cols[i].firstChild.style.height = (hist[i] * 100) + "%";
          cols[i].lastChild.style.height = ((1 - hist[i]) * 100) + "%";
          /* ⚠️ THE FRACTION AT FULL PRECISION, because the HEIGHT IS NOT
             READABLE AT FULL PRECISION. `style.height` goes through the
             CSSOM, which re-serialises a percentage to four decimal places —
             so the one property the control has to have, that it does not
             move at all, is invisible through the drawn value. Writing the
             fraction gives the parity gate something it can actually compare,
             and it is the model's own number rather than a rendering of it.
             Nothing reads this at runtime; it exists to be measured. */
          cols[i].setAttribute("data-nr-pale", String(hist[i]));
          /* MRB-257 (5.40) — WHICH generation this column is. The chart is a
             sliding window `M.history` wide, so past generation 23 the axis
             caption's "oldest on the left" stops being true: at generation
             50 column 0 was generation 27, and the whole change the lesson
             is about had scrolled out silently. Stamping the generation
             makes the window self-describing rather than implied.
             ⚠️ The window itself cannot be widened from here. `ks3_parity.py`
             asserts that after sixty generations EVERY drawn column equals
             the control's fraction, which is only true because the window
             flushes the selecting bark's run — so keeping generation 0 on
             screen turns that gate red. Widening the window and re-writing
             that assertion is one coordinated change across two files; see
             HANDOFF. */
          cols[i].setAttribute("data-nr-gen", String(gen - hist.length + 1 + i));
        } else {
          cols[i].removeAttribute("data-nr-pale");
          cols[i].removeAttribute("data-nr-gen");
        }
      }
      /* The axis caption names the window it is drawing, if the author has
         written it as a template. No payload carries one yet — see HANDOFF. */
      var axis = w.querySelector("[data-nr-axis]");
      if (axis && axis.getAttribute("data-format")) {
        axis.textContent = axis.getAttribute("data-format")
          .split("{from}").join(String(gen - hist.length + 1))
          .split("{to}").join(String(gen));
      }
      each(figures, function (f) {
        var which = f.getAttribute("data-nr-series");
        f.textContent = (f.getAttribute("data-label") || "") + " " +
          (which === "pale" ? palePct : darkPct) + "%";
      });
      var want = noteId(palePct, darkPct);
      each(notes, function (p) {
        setHidden(p, p.getAttribute("data-nr-note") !== want);
      });
      setCount(sec, gen);
      if (NEED > 0 && gen >= NEED) { everTen = true; }
      /* ⚠️ MONOTONIC. *Start again at fifty-fifty* sets `gen` back to 0, and
         Design's own `isDone()` would untick two rail stops with it. MRB-208
         ruled the rail records participation: a student who has run ten
         generations has run them, and pressing reset is using the bench, not
         undoing it. */
      markStage(sec, everTen);
    }

    function advance(n) {
      for (var i = 0; i < n; i += 1) {
        pale = nrStep(pale, M.barks[bark]);
        hist.push(pale);
      }
      while (hist.length > M.history) { hist.shift(); }
      gen += n;
      draw();
    }

    each(tabs, function (tb) {
      tb.addEventListener("click", function () {
        /* ⚖️ SWITCHING BARK DOES NOT TOUCH THE POPULATION, AND THAT IS THE
           BEST THING ON THIS BENCH. Run it sooty to 99% dark, switch to clean,
           run it again and watch it come back — which is `notes.pale_high`
           saying selection has no memory and no direction. */
        bark = tb.getAttribute("data-nr-bark");
        draw();
      });
    });
    each(w.querySelectorAll("[data-nr-run]"), function (btn) {
      btn.addEventListener("click", function () {
        advance(Number(btn.getAttribute("data-nr-run")) || 1);
      });
    });
    if (resetBtn) {
      resetBtn.addEventListener("click", function () {
        pale = M.reset;
        gen = 0;
        hist = [pale];
        draw();
      });
    }

    draw();
  }

  /* ── b11-03 `#s-bench` · pressure-bench ──────────────────────────────── */

  /* ⚖️ TWO AXES, AND THE COMBINATION IS THE UNIT. What is counted is the PAIR
     the student is looking at, not the number of buttons pressed — Design's
     `seen[species + '-' + pressure]`. A bench that counted axis presses would
     tick its stage for a student who had looked at four species under one
     pressure and never watched a row change, which is the whole lesson.

     ⚠️ `seen` NEVER SHRINKS, for MRB-208's reason: the rail records
     participation, and two stops read this marker (MRB-249). */
  function wirePressureBench(sec) {
    var w = sec.querySelector("[data-pb]");
    if (!w) { return; }
    var spTabs = toArray(w.querySelectorAll("[data-pb-species]"));
    var prTabs = toArray(w.querySelectorAll("[data-pb-pressure]"));
    var spPanels = toArray(w.querySelectorAll("[data-pb-speciespanel]"));
    var prPanels = toArray(w.querySelectorAll("[data-pb-pressurepanel]"));
    var cells = toArray(w.querySelectorAll("[data-pb-cell]"));
    if (!spTabs.length || !prTabs.length || !cells.length) { return; }

    var NEED = Number(w.getAttribute("data-threshold")) || 0;
    var opens = (w.getAttribute("data-opens-on") || "").split("|");
    var species = opens[0], pressure = opens[1];
    var seen = {}, nSeen = 0;

    function draw() {
      var key = species + "|" + pressure;
      if (!seen[key]) { seen[key] = true; nSeen += 1; }
      each(spTabs, function (tb) {
        tb.setAttribute("aria-pressed",
                        tb.getAttribute("data-pb-species") === species
                          ? "true" : "false");
      });
      each(prTabs, function (tb) {
        tb.setAttribute("aria-pressed",
                        tb.getAttribute("data-pb-pressure") === pressure
                          ? "true" : "false");
      });
      each(spPanels, function (p) {
        setHidden(p, p.getAttribute("data-pb-speciespanel") !== species);
      });
      each(prPanels, function (p) {
        setHidden(p, p.getAttribute("data-pb-pressurepanel") !== pressure);
      });
      each(cells, function (c) {
        setHidden(c, c.getAttribute("data-pb-cell") !== key);
      });
      setCount(sec, nSeen);
      markStage(sec, NEED > 0 && nSeen >= NEED);
    }

    each(spTabs, function (tb) {
      tb.addEventListener("click", function () {
        species = tb.getAttribute("data-pb-species");
        draw();
      });
    });
    each(prTabs, function (tb) {
      tb.addEventListener("click", function () {
        pressure = tb.getAttribute("data-pb-pressure");
        draw();
      });
    });

    draw();
  }

  /* ── b11-04 `#s-bench` · blight-bench ────────────────────────────────── */

  /* ⚖️ SWITCHING FIELD RE-ARMS THE BLIGHT, AND NOTHING UNTICKS. Design's tab
     handler is `{ field: x.id, released: false }` and her *Clear the field* is
     `{ released: false }` — `tried` is cleared by neither, so a student who
     has released the blight on two fields keeps both. MRB-208: the rail
     records participation, and two stops read this marker (MRB-249). */
  function wireBlightBench(sec) {
    var w = sec.querySelector("[data-bb]");
    if (!w) { return; }
    var tabs = toArray(w.querySelectorAll("[data-bb-field]"));
    var panels = toArray(w.querySelectorAll("[data-bb-fieldpanel]"));
    var runBtn = w.querySelector("[data-bb-run]");
    var clearBtn = w.querySelector("[data-bb-clear]");
    if (!tabs.length || !panels.length || !runBtn) { return; }

    var NEED = Number(w.getAttribute("data-threshold")) || 0;
    var RUN = w.getAttribute("data-run-label") || "";
    var RAN = w.getAttribute("data-ran-label") || "";
    var field = (panels[0] || {}).getAttribute
      ? panels[0].getAttribute("data-bb-fieldpanel") : "";
    var open = w.querySelector("[data-bb-fieldpanel]:not([hidden])");
    if (open) { field = open.getAttribute("data-bb-fieldpanel"); }
    var released = false, tried = {}, nTried = 0;

    function draw() {
      each(tabs, function (tb) {
        tb.setAttribute("aria-pressed",
                        tb.getAttribute("data-bb-field") === field ? "true" : "false");
      });
      each(panels, function (p) {
        var on = p.getAttribute("data-bb-fieldpanel") === field;
        setHidden(p, !on);
        /* ⚖️ THE SURVIVOR ROW HAS TWO DRAWN STATES and the release chooses
           between them. Before, every plant is standing and the bar is full;
           after, it is whatever the resistant varieties left. The student
           watches a full field become an empty one rather than watching an
           empty one appear. */
        each(p.querySelectorAll("[data-bb-surv]"), function (row) {
          setHidden(row, row.getAttribute("data-bb-surv") !==
                    (on && released ? "after" : "before"));
        });
        setHidden(p.querySelector("[data-bb-verdict]"), !(on && released));
      });
      runBtn.textContent = released ? RAN : RUN;
      runBtn.disabled = released;
      setCount(sec, nTried);
      markStage(sec, NEED > 0 && nTried >= NEED);
    }

    each(tabs, function (tb) {
      tb.addEventListener("click", function () {
        field = tb.getAttribute("data-bb-field");
        released = false;
        draw();
      });
    });
    runBtn.addEventListener("click", function () {
      /* The gate in the handler as well as on the element: `disabled` is the
         drawn half, and this is the half a synthetic click cannot get past. */
      if (released) { return; }
      released = true;
      if (!tried[field]) { tried[field] = true; nTried += 1; }
      draw();
      var live = w.querySelector('[data-bb-fieldpanel="' + field + '"]');
      if (live) { focusReveal(live.querySelector("[data-bb-verdict]")); }  // MRB-257 (5.43)
    });
    if (clearBtn) {
      clearBtn.addEventListener("click", function () {
        released = false;
        draw();
      });
    }

    draw();
  }

/* ═══ END B11 ═══ */




/* ═══ BEGIN C3 wiring ═══════════════════════════════════════════════════
   C3 · Mixtures and separation — NINE instrument families, all DOM, no
   canvas, and one page (filtration) that places one family twice.

   `ks3_art/c3.py` emits EMIT-BOTH-SHOW-ONE markup wherever a panel has a
   small closed set of states, and a JSON `data-cfg` only for what genuinely
   has to be recomputed — a number, a colour, a geometry. So almost nothing
   below writes a sentence: it chooses a node that is already in the
   document, and the three places that do compose (the dissolving bench's
   readouts and verdict, the sequence report, the crystal dish's alt) compose
   from a template the payload carries, with the SAME arithmetic the renderer
   used for the resting DOM.

   ⚖️ NOTHING GREEN AND NOTHING RED REACHES A CONTROL IN ANY OF THE NINE.
   A verdict panel says in words what happened; a chosen option keeps the
   ordinary chosen treatment and the rest dim. Only the mastery ladder marks
   correctness (R3 / MRB-196 R10).

   ⚖️ NOTHING ANIMATES AND NOTHING COUNTS DOWN in any of the nine — there is
   no rAF loop, no timer and no JS-driven transition anywhere in this block —
   so `prefers-reduced-motion` has nothing to degrade here. What motion the
   unit has is arrival/transition CSS, which `shared/ks3.css` degrades itself
   inside its own media query. If a later revision animates anything here it
   must ask `motionReduced()` INSIDE the tick, not once at construction
   (contract R4, the b2-03 slip).

   ⚠️ A DIAL BUTTON IS FOUND BY `data-<fam>-for`, NOT BY `data-<fam>-opt`.
   The renderer's `_seg()` composes a segmented button out of a CLASS plus
   whatever named attributes it is handed, and for the five dial families
   (dlab, cryst, still, chroma, mpb) it is handed `-for` and `-val` only. The
   docstrings and the hooks list name a `data-dlab-opt` / `data-cryst-opt` /
   `data-still-opt` / `data-chroma-opt` / `data-mpb-opt` that IS NOT IN THE
   BUILT MARKUP — binding to it wires nothing and fails silently, which is
   exactly how it presented the first time. The one-shot commit families
   (psort, mchoice, critiq, seq chips, chroma pens, mpb verdict buttons) do
   carry their own `-opt`-shaped hook, and those are used as named.

   ⚠️ THE NO-OP PRESS. Every dial below returns early when the value pressed
   is the value already pressed. Design's own handlers do not: on c3-04 and
   c3-06 pressing the dial that is already lit resets the prediction and
   withdraws the Run button, and on c3-05 it resets the run to stage 0. That
   is a control claiming to be pressed and then changing what is on screen,
   which the smoke gate asserts against. Corrected here rather than
   reproduced. */

  /* ── the six things all nine need ───────────────────────────────────── */

  function c3Cfg(el, attr) {
    try { return JSON.parse(el.getAttribute(attr || "data-cfg") || "{}"); }
    catch (err) { return {}; }
  }

  /* Authored text, through the file's own mark drawer. NEVER textContent:
     C3's copy uses → as chemistry notation and the shipped font subsets do
     not carry the character (SPEC §9.3). */
  function c3Say(el, text) {
    if (!el) { return; }
    while (el.firstChild) { el.removeChild(el.firstChild); }
    appendAuthored(el, text === null || text === undefined ? "" : text);
  }

  /* `{placeholder}` substitution, and the only string composition in the
     block. The templates are the payload's own — `_dlab_verdict`,
     `dish_alt.template`, `report.wrong_text` — so Python and JS are reading
     one authored sentence rather than keeping two. */
  function c3Fill(tpl, map) {
    var s = String(tpl === null || tpl === undefined ? "" : tpl), k;
    for (k in map) {
      if (Object.prototype.hasOwnProperty.call(map, k)) {
        s = s.split("{" + k + "}").join(String(map[k]));
      }
    }
    return s;
  }

  function c3By(list, id) {
    var i;
    for (i = 0; i < (list || []).length; i++) {
      if (list[i] && list[i].id === id) { return list[i]; }
    }
    return null;
  }

  function c3Empty(el) {
    if (!el) { return; }
    while (el.firstChild) { el.removeChild(el.firstChild); }
  }

  function c3Enable(btn, on) {
    if (!btn) { return; }
    if (on) { btn.removeAttribute("disabled"); }
    else { btn.setAttribute("disabled", ""); }
  }

  /* ── one commitment per card, and it is FINAL ────────────────────────
     Three of the nine are the same instrument with three sets of hooks:
     `purity-sorter` (c3-01, eight samples), `method-choice` (c3-04, three
     jobs) and `plan-critique` (c3-07, four judgements on somebody else's
     plan). All three are `wireVerdictCards`' contract — the reveal is on
     screen the instant the card is decided, so a second press would be a
     student choosing an answer they can already read, and every button on
     that card disables.

     They share this one body rather than three copies, because the thing
     that must not drift between them is exactly the rule above. */
  function c3CommitCards(sec, sel) {
    var wrap = sec.querySelector(sel.wrap);
    if (!wrap) { return; }
    var cards = toArray(wrap.querySelectorAll(sel.card));
    if (!cards.length) { return; }
    var total = parseInt(wrap.getAttribute("data-total"), 10) || cards.length;
    var closer = sel.close ? wrap.querySelector(sel.close) : null;

    function decided() {
      var n = 0;
      each(cards, function (c) {
        if (c.getAttribute("data-open") === "1") { n += 1; }
      });
      return n;
    }

    each(cards, function (card) {
      var opts = toArray(card.querySelectorAll(sel.opt));
      each(opts, function (btn) {
        btn.addEventListener("click", function () {
          /* The guard is here as well as on the elements: `disabled` is the
             drawn half, and this is the half a synthetic click cannot pass. */
          if (card.getAttribute("data-open") === "1") { return; }
          card.setAttribute("data-open", "1");
          each(opts, function (b) {
            b.setAttribute("aria-pressed", b === btn ? "true" : "false");
            c3Enable(b, false);
          });
          /* ⚠️ c3-01 only: the ingredients ARE the answer to the question
             being asked, so they are not on the page until the card is
             decided. No-ops where a family has none. */
          if (sel.also) { setHidden(card.querySelector(sel.also), false); }
          setHidden(card.querySelector(sel.reveal), false);
          var n = decided();
          if (sel.count) { setCount(sec, n); }
          if (n >= total) {
            setHidden(closer, false);
            markStage(sec, true);
          }
        });
      });
    });
    if (sel.count) { setCount(sec, 0); }
  }

  /* ── purity-sorter (c3-01 #s-sorter) ────────────────────────────────
     Eight samples, one question asked eight times, and looking settles none
     of them. The head counter is the shell's `[data-count]` — "0 of 8
     decided" through to "8 of 8 decided", a sentence whose noun does not
     inflect, which is why this counter carries no `data-format-one`. */
  function wirePuritySorter(sec) {
    c3CommitCards(sec, {
      wrap: "[data-psort]", card: "[data-psort-card]",
      opt: "[data-psort-opt]", reveal: "[data-psort-reveal]",
      also: "[data-psort-ingredients]", close: "[data-psort-close]",
      count: true
    });
  }

  /* ── method-choice (c3-04 #s-jobs) ──────────────────────────────────
     Three real jobs, and ONE OF THEM CANNOT BE DONE THIS WAY AT ALL. There
     is no `correct` key in the payload and nothing here looks for one: the
     reveal names the method and explains it, in the same tone whichever
     button was pressed. */
  function wireMethodChoice(sec) {
    c3CommitCards(sec, {
      wrap: "[data-mchoice]", card: "[data-mchoice-item]",
      opt: "[data-mchoice-opt]", reveal: "[data-mchoice-reveal]"
    });
  }

  /* ── plan-critique (c3-07 #s-critique) ──────────────────────────────
     Four judgements on somebody else's plan, and it comes BEFORE the bench:
     ruling on four steps that are all observations is what makes building a
     measurement a decision instead of a recipe.

     ⚠️ `data-critiq`, NOT `data-critique`. `wireCritique` above already
     claims `[data-critique]` for a B-unit family; a shared selector would
     hand this instrument to that one's handler and neither would work. */
  function wirePlanCritique(sec) {
    c3CommitCards(sec, {
      wrap: "[data-critiq]", card: "[data-critiq-item]",
      opt: "[data-critiq-opt]", reveal: "[data-critiq-reveal]",
      close: "[data-critiq-close]"
    });
  }

  /* ── dissolve-lab (c3-02 #s-lab, gated by #s-gate) ──────────────────
     Four dials — solute × temperature × stirring × grinding — and 48
     reachable states.

     ⚖️ THE RATE/AMOUNT SPLIT IS THE WHOLE LESSON AND IT IS LOAD-BEARING
     HERE. `grams` comes from `solutes[].grams[temp]` and from nowhere else;
     `c3DlabSeconds` divides the TIME and CANNOT SEE THE GRAMS — they are not
     a parameter of it and must never become one. If stirring ever moved the
     grams this bench would teach MIX-04 ("stirring harder makes more
     dissolve"), which is the misconception it exists to confront.

     ⚖️ SALT IS ON THE BENCH BECAUSE ITS SOLUBILITY BARELY MOVES: 35.8 g cold
     against 38.1 g hot, next to sugar's 190 against 360. Both come out of
     the same lookup, so the counter-example cannot be lost by a repaint.

     ⚠️ THE BENCH IS LOCKED BY AN ACTIVITY THAT IS NOT PART OF IT.
     `data-dlab-lock` names the predict block ABOVE it on the page and Design
     wraps the whole `<section>` in that gate rather than greying the
     controls, so the section is hidden here and arrives in the space the
     question was occupying. `data-dlab-demo` is the front-of-class dial: it
     opens the bench without the gate, it is authored `0`, and it is read as
     an explicit `"1"` so that a missing attribute can never open it.

     ⚠️ AN INSOLUBLE SOLUTE IS A REACHABLE, HONEST STATE — two of the four
     are — and it reads `none` / `never` / `cloudy` with undissolved solid
     drawn on the bottom, not an error. */

  function c3DlabSeconds(base, factor, stir, powder, timing) {
    var s = Number(base || 0) * Number(factor || 0);
    if (stir) { s = s / Number(timing.stirred_divisor || 1); }
    if (powder) { s = s / Number(timing.powder_divisor || 1); }
    return Math.round(s);
  }

  /* Design's interleave, and the renderer's: every `every`-th water particle
     is followed by a solute particle, so the picture reads as *spread evenly
     among them* rather than as a stripe of one colour beside a stripe of the
     other. Reproduced exactly, because the resting render is this picture
     and a repaint must not be an approximation of it. */
  function c3DlabMix(waterN, waterC, waterS, solN, solC, solS) {
    var out = [], wi = 0, si = 0, k;
    var every = solN ? Math.max(2, Math.round(waterN / solN)) : Infinity;
    while (wi < waterN || si < solN) {
      k = 0;
      while (k < every && wi < waterN) { out.push([waterC, waterS]); wi += 1; k += 1; }
      if (si < solN) { out.push([solC, solS]); si += 1; }
    }
    return out;
  }

  function c3DlabDot(cls, colour, size) {
    var d = document.createElement("span");
    d.className = cls;
    d.style.width = size + "px";
    d.style.height = size + "px";
    d.style.background = colour;
    return d;
  }

  function wireDissolveLab(sec) {
    var wrap = sec.querySelector("[data-dlab]");
    if (!wrap) { return; }
    var cfg = c3Cfg(wrap);
    var solutes = cfg.solutes || [];
    var temps = cfg.temps || [];
    var timing = cfg.timing || {};
    var factors = timing.temperature || {};
    var beaker = cfg.beaker || {};
    var readouts = cfg.readouts || [];
    var verdict = cfg.verdict || {};
    var start = cfg.start || {};
    if (!solutes.length || !temps.length) { return; }

    var DONE_AT = parseInt(wrap.getAttribute("data-dlab-done-at"), 10) || temps.length;
    var dials = toArray(wrap.querySelectorAll("[data-dlab-for]"));
    var beakerEl = wrap.querySelector("[data-dlab-beaker]");
    var dotsEl = wrap.querySelector("[data-dlab-dots]");
    var bottomEl = wrap.querySelector("[data-dlab-bottom]");
    var bottomDots = wrap.querySelector("[data-dlab-bottomdots]");
    var bottomNote = wrap.querySelector("[data-dlab-bottomnote]");
    var verdictEl = wrap.querySelector("[data-dlab-verdict]");
    var summaryEl = wrap.querySelector("[data-dlab-summary]");
    var outs = {}, notes = {};
    each(wrap.querySelectorAll("[data-dlab-out]"), function (el) {
      outs[el.getAttribute("data-dlab-out")] = el;
    });
    each(wrap.querySelectorAll("[data-dlab-outnote]"), function (el) {
      notes[el.getAttribute("data-dlab-outnote")] = el;
    });

    var pick = {
      solute: start.solute || solutes[0].id,
      temp: start.temp || temps[0],
      stir: start.stir ? "1" : "0",
      powder: start.powder ? "1" : "0"
    };
    var seen = {}, nSeen = 0;
    each(start.seen || [], function (k) {
      if (!seen[k]) { seen[k] = true; nSeen += 1; }
    });

    function paint() {
      var sol = c3By(solutes, pick.solute) || solutes[0];
      var soluble = !!sol.soluble;
      var grams = (sol.grams || {})[pick.temp];
      var secs = c3DlabSeconds(sol.base, factors[pick.temp],
                               pick.stir === "1", pick.powder === "1", timing);

      each(dials, function (b) {
        b.setAttribute("aria-pressed",
          pick[b.getAttribute("data-dlab-for")] === b.getAttribute("data-dlab-val")
            ? "true" : "false");
      });

      each(readouts, function (r) {
        var value, note;
        if (!soluble) {
          value = r.value_insoluble || "";
          /* An authored `null` means "this readout's insoluble note is the
             SOLUTE's note" — sand and chalk each say why. */
          note = (r.note_insoluble === null || r.note_insoluble === undefined)
            ? (sol.note || "") : r.note_insoluble;
        } else if (r.id === "amount") {
          /* ⚖️ THE GRAMS, AND THE ONLY PLACE THEY COME FROM. */
          value = cfg.show_grams === false
            ? (r.value_hidden || "")
            : c3Fill(r.value_format || "{grams} g",
                     { grams: (grams === null || grams === undefined) ? "" : grams });
          note = r.note || "";
        } else if (r.id === "time") {
          value = c3Fill(r.value_format || "{seconds} s", { seconds: secs });
          note = r.note || "";
        } else {
          value = (soluble ? r.value : r.value_insoluble) || "";
          note = r.note || "";
        }
        c3Say(outs[r.id], value);
        c3Say(notes[r.id], note);
      });

      if (beakerEl) {
        beakerEl.setAttribute("aria-label", c3Fill(
          beaker[soluble ? "alt_soluble" : "alt_insoluble"] || "",
          { solute: String(sol.name || "").toLowerCase() }));
      }
      var diss = soluble ? Number((beaker.dissolved_dots || {})[sol.id] || 0) : 0;
      c3Empty(dotsEl);
      if (dotsEl) {
        each(c3DlabMix(Number(beaker.water_dots || 0), beaker.water_colour || "",
                       Number(beaker.water_dot_size || 11), diss,
                       sol.colour || "", Number(beaker.solute_dot_size || 9)),
             function (p) { dotsEl.appendChild(c3DlabDot("ks3-dlab-dot", p[0], p[1])); });
      }
      var bn = soluble ? 0 : Number(beaker.undissolved_dots || 0);
      c3Empty(bottomDots);
      if (bottomDots) {
        for (var i = 0; i < bn; i++) {
          bottomDots.appendChild(c3DlabDot("ks3-dlab-dot ks3-dlab-dot-solid",
            sol.colour || "", Number(beaker.undissolved_dot_size || 13)));
        }
      }
      setHidden(bottomEl, bn === 0);
      c3Say(bottomNote, c3Fill(beaker.bottom_note || "", { Solute: sol.name || "" }));

      /* The verdict's tail is chosen by whether the two RATE dials have been
         touched, and both tails say the same thing about the grams — that
         they did not move. It has to be true in the state where nothing has
         been stirred as well as in the state where everything has. */
      c3Say(verdictEl, soluble
        ? c3Fill(verdict.soluble || "", {
            Solute: sol.name || "", note: sol.note || "",
            tail: (pick.stir === "1" || pick.powder === "1"
                   ? verdict.tail_worked : verdict.tail_still) || "" })
        : c3Fill(verdict.insoluble || "", {
            Solute: sol.name || "", note: sol.note || "" }));

      setHidden(summaryEl, nSeen < DONE_AT);
      markStage(sec, nSeen >= DONE_AT);
    }

    each(dials, function (btn) {
      btn.addEventListener("click", function () {
        var g = btn.getAttribute("data-dlab-for");
        var v = btn.getAttribute("data-dlab-val");
        if (pick[g] === undefined || pick[g] === v) { return; }
        pick[g] = v;
        /* The rail stop is three DIFFERENT temperatures seen, which is the
           only way the salt column and the sugar column can be compared. */
        if (g === "temp" && !seen[v]) { seen[v] = true; nSeen += 1; }
        paint();
      });
    });

    /* Gating by ABSENCE, and the gate is a SIBLING BLOCK rather than a panel
       inside the bench — so the whole section goes, and comes back when the
       named activity is answered. */
    function openBench() {
      setHidden(sec, false);
      setHidden(wrap, false);
    }
    var lock = wrap.getAttribute("data-dlab-lock") || "";
    if (wrap.getAttribute("data-dlab-demo") === "1" || !lock) {
      openBench();
    } else {
      var gate = null;
      each(document.querySelectorAll("[data-activity]"), function (b) {
        if (b.getAttribute("data-activity") === lock) { gate = b; }
      });
      if (!gate) {
        /* A lock naming a block that is not on the page would hide the bench
           for ever, which is worse than an ungated bench. */
        openBench();
      } else {
        setHidden(sec, true);
        var gopts = toArray(gate.querySelectorAll(".ks3-option"));
        var answered = false;
        each(gopts, function (b) {
          if (b.getAttribute("aria-pressed") === "true") { answered = true; }
        });
        if (answered) { openBench(); }
        else { each(gopts, function (b) { b.addEventListener("click", openBench); }); }
      }
    }
    paint();
  }

  /* ── sequence-rebuild (c3-03 #s-steps watch · #s-build rebuild) ──────
     ONE FAMILY, TWO PHASES, ONE WIRE FUNCTION. `data-phase` selects the
     branch, and the five steps are literally the same five records — minting
     a second family would give them two places to drift apart. */
  function wireSequenceRebuild(sec) {
    var wrap = sec.querySelector("[data-seq]");
    if (!wrap) { return; }
    if (wrap.getAttribute("data-phase") === "rebuild") { c3SeqRebuild(sec, wrap); }
    else { c3SeqWatch(sec, wrap); }
  }

  /* phase `watch` — five steps revealed one at a time, with a PREDICTION
     GATE taking the next-step slot before `pour` so that a student cannot
     walk past the question by scrolling. */
  function c3SeqWatch(sec, wrap) {
    var total = parseInt(wrap.getAttribute("data-total"), 10) || 0;
    var gateAt = parseInt(wrap.getAttribute("data-seq-gate-at"), 10);
    if (isNaN(gateAt)) { gateAt = -1; }
    var gate = wrap.querySelector("[data-seq-gate]");
    var closer = wrap.querySelector("[data-seq-close]");
    var btns = [], bodies = [];
    each(wrap.querySelectorAll("[data-seq-open]"), function (b) {
      btns[parseInt(b.getAttribute("data-seq-open"), 10)] = b;
    });
    each(wrap.querySelectorAll("[data-seq-step]"), function (li) {
      bodies[parseInt(li.getAttribute("data-seq-i"), 10)] =
        li.querySelector("[data-seq-body]");
    });
    if (!total) { return; }
    var opened = 0;
    var gateDone = !(gate && gateAt >= 0);

    /* The stepper offers exactly ONE control at a time: the next step's
       button, or the gate standing in its place. */
    function offer() {
      var i;
      for (i = 0; i < btns.length; i++) { if (btns[i]) { setHidden(btns[i], true); } }
      setHidden(gate, true);
      if (opened >= total) {
        setHidden(closer, false);
        markStage(sec, true);
        return;
      }
      if (opened === gateAt && !gateDone) { setHidden(gate, false); return; }
      if (btns[opened]) { setHidden(btns[opened], false); }
    }

    each(wrap.querySelectorAll("[data-seq-open]"), function (btn) {
      btn.addEventListener("click", function () {
        var i = parseInt(btn.getAttribute("data-seq-open"), 10);
        /* Only the step the stepper is standing on opens, and only once. */
        if (i !== opened) { return; }
        if (opened === gateAt && !gateDone) { return; }
        setHidden(bodies[i], false);
        opened = i + 1;
        offer();
      });
    });

    if (gate) {
      var gopts = toArray(gate.querySelectorAll(".ks3-option"));
      each(gopts, function (b) {
        b.addEventListener("click", function () {
          each(gopts, function (x) {
            x.setAttribute("aria-pressed", x === b ? "true" : "false");
          });
          if (gateDone) { return; }
          gateDone = true;
          offer();
        });
      });
    }
    offer();
  }

  /* phase `rebuild` — the same five steps as a shuffled bank, tapped into a
     sequence.

     ⚖️ WRONG ORDERS ARE ANSWERED WITH CONSEQUENCES, NEVER WITH MARKS. The
     report names what happened ON THE BENCH, out of the offending step's own
     `tooSoon` string — "you poured before the paper and funnel were ready,
     so the sand went into the flask with the water". Nothing green, nothing
     red, no score, and the order that works is given in the same breath.
     R3 is not relaxed for a construct task.

     ⚠️ THE NODES ARE MOVED, NOT REWRITTEN. Each `<li>` is emitted hidden in
     authored order carrying its step's title as real markup, and this
     appends it to the list; nothing round-trips through an attribute, so an
     authored `<em>` survives. */
  function c3SeqRebuild(sec, wrap) {
    var cfg = c3Cfg(wrap, "data-seq-report");
    var total = parseInt(wrap.getAttribute("data-total"), 10) || 0;
    var chips = toArray(wrap.querySelectorAll("[data-seq-chip]"));
    var listEl = wrap.querySelector("[data-seq-order]");
    var clearBtn = wrap.querySelector("[data-seq-clear]");
    var panel = wrap.querySelector("[data-seq-report-panel]");
    var rightEl = wrap.querySelector("[data-seq-right]");
    var wrongEl = wrap.querySelector("[data-seq-wrong]");
    var wrongTitle = wrap.querySelector("[data-seq-wrong-title]");
    var wrongText = wrap.querySelector("[data-seq-wrong-text]");
    var slots = [];
    each(wrap.querySelectorAll("[data-seq-slot]"), function (li) {
      slots[parseInt(li.getAttribute("data-seq-slot"), 10)] = li;
    });
    if (!chips.length || !total) { return; }
    var order = [];

    function report() {
      var firstWrong = -1, i;
      for (i = 0; i < order.length; i++) {
        if (order[i] !== i) { firstWrong = i; break; }
      }
      setHidden(panel, false);
      if (firstWrong < 0) {
        setHidden(wrongEl, true);
        setHidden(rightEl, false);
      } else {
        /* The step the student put THERE, and whether it was done before the
           steps that protect it or after the step it was protecting. */
        var s = order[firstWrong];
        setHidden(rightEl, true);
        setHidden(wrongEl, false);
        c3Say(wrongTitle, c3Fill(cfg.wrong_title, { n: firstWrong + 1 }));
        c3Say(wrongText, c3Fill(cfg.wrong_text, {
          short: (cfg.shorts || [])[s] || "",
          when: (cfg.when || {})[s > firstWrong ? "early" : "late"] || "",
          too_soon: (cfg.too_soon || [])[s] || ""
        }));
      }
      focusReveal(panel);  // MRB-257 (5.43)
      markStage(sec, true);
    }

    each(chips, function (chip) {
      chip.addEventListener("click", function () {
        if (chip.getAttribute("aria-pressed") === "true") { return; }
        if (order.length >= total) { return; }
        var i = parseInt(chip.getAttribute("data-seq-chip"), 10);
        order.push(i);
        chip.setAttribute("aria-pressed", "true");
        c3Enable(chip, false);
        setHidden(listEl, false);
        if (slots[i] && listEl) {
          listEl.appendChild(slots[i]);
          setHidden(slots[i], false);
        }
        if (order.length >= total) { report(); }
      });
    });

    if (clearBtn) {
      clearBtn.addEventListener("click", function () {
        /* Nothing placed, nothing to clear — and the rail credit already
           earned stays, because `markStage` is a ratchet. */
        if (!order.length) { return; }
        order = [];
        each(chips, function (c) {
          c.setAttribute("aria-pressed", "false");
          c3Enable(c, true);
        });
        var k;
        for (k = 0; k < slots.length; k++) { if (slots[k]) { setHidden(slots[k], true); } }
        setHidden(listEl, true);
        setHidden(panel, true);
        setHidden(rightEl, true);
        setHidden(wrongEl, true);
      });
    }
  }

  /* ── crystal-bench (c3-04 #s-bench) ──────────────────────────────────
     Three solutes × three methods = nine states, and ONE recovered mass.

     ⚖️ THE MASS IS THE SAME IN ALL NINE AND THAT IS THE TEACHING. The
     renderer prints it once from one authored string and gives it NO DATA
     HOOK, so there is nothing here to write into and nine masses cannot be
     computed even by accident. Nothing below looks for one. `MIX-09` is
     "faster evaporation gives more product"; this bench refuses it by
     changing the crystal and never the yield.

     ⚠️ THE PREDICT GATE IS PER-RUN AND DOES NOT DISAPPEAR. Moving a dial
     clears the prediction and withdraws the Run button, so the remaining
     eight states are each predicted before they are run — which is the eight
     times it actually matters.

     ⚠️ WHICH SOLUTE LINE JOINS THE HAZARD IS COMPUTED FROM THE METHODS, not
     keyed on a method id. `solutes[].hard` is what boiling hard does and
     `slow` is what slow growth gives, so the fastest method (the smallest
     drawn crystal) takes `hard`, the slowest (the largest) takes `slow`, and
     anything between takes the method's hazard alone. A comparative is
     computed from the values, never authored beside them. */

  function c3CrystSizeWord(words, size) {
    var i;
    for (i = 0; i < (words || []).length; i++) {
      if (Number(size) > Number(words[i][0])) { return words[i][1]; }
    }
    return "";
  }

  function wireCrystalBench(sec) {
    var wrap = sec.querySelector("[data-cryst]");
    if (!wrap) { return; }
    var cfg = c3Cfg(wrap);
    var solutes = cfg.solutes || [];
    var methods = cfg.methods || [];
    if (!solutes.length || !methods.length) { return; }
    var dishAlt = cfg.dish_alt || {};
    var total = parseInt(wrap.getAttribute("data-total"), 10) || methods.length;
    var dials = toArray(wrap.querySelectorAll("[data-cryst-for]"));
    var gopts = toArray(wrap.querySelectorAll("[data-cryst-gate-opts] .ks3-option"));
    var runBtn = wrap.querySelector("[data-cryst-run]");
    var panel = wrap.querySelector("[data-cryst-panel]");
    var dish = wrap.querySelector("[data-cryst-dish]");
    var crystals = wrap.querySelector("[data-cryst-crystals]");
    var verdictEl = wrap.querySelector("[data-cryst-verdict]");
    var hazardEl = wrap.querySelector("[data-cryst-hazard]");
    var summaryEl = wrap.querySelector("[data-cryst-summary]");
    var runTpl = runBtn ? (runBtn.getAttribute("data-cryst-runlabel") || "") : "";
    var outs = {};
    each(wrap.querySelectorAll("[data-cryst-out]"), function (el) {
      outs[el.getAttribute("data-cryst-out")] = el;
    });

    /* The two ends of the method dial, measured off the drawn crystal. */
    var minSize = null, maxSize = null, fastest = null, slowest = null;
    each(methods, function (m) {
      var z = Number(m.size || 0);
      if (minSize === null || z < minSize) { minSize = z; fastest = m.id; }
      if (maxSize === null || z > maxSize) { maxSize = z; slowest = m.id; }
    });
    if (minSize === maxSize) { fastest = null; slowest = null; }

    var pick = {
      solute: (cfg.start || {}).solute || solutes[0].id,
      method: (cfg.start || {}).method || methods[0].id
    };
    var predicted = false, ran = {}, methodsRun = {}, nMethods = 0;

    function draw(sol, met) {
      if (!crystals) { return; }
      c3Empty(crystals);
      var n = Number(met.count || 0), i, size, sp;
      for (i = 0; i < n; i++) {
        /* Design's jitter, so a dish reads as crystals rather than as a
           row of identical squares. */
        size = Math.round(Number(met.size || 0) * (1 + ((i % 3) - 1) * 0.12));
        sp = document.createElement("span");
        sp.className = "ks3-cryst-crystal";
        sp.setAttribute("data-shape", sol.shape || "");
        sp.style.width = size + "px";
        sp.style.height = size + "px";
        sp.style.background = sol.colour || "";
        sp.style.border = (size > 8 ? 2 : 1) + "px solid var(--ks3-ink)";
        sp.style.borderRadius = (size > 14 ? 3 : 1) + "px";
        if (sol.shape === "diamond" && size > 10) { sp.style.transform = "rotate(45deg)"; }
        crystals.appendChild(sp);
      }
    }

    function paint() {
      var sol = c3By(solutes, pick.solute) || solutes[0];
      var met = c3By(methods, pick.method) || methods[0];
      var isRan = !!ran[pick.solute + ":" + pick.method];

      each(dials, function (b) {
        b.setAttribute("aria-pressed",
          pick[b.getAttribute("data-cryst-for")] === b.getAttribute("data-cryst-val")
            ? "true" : "false");
      });
      each(gopts, function (b) {
        if (!predicted) { b.setAttribute("aria-pressed", "false"); }
      });
      if (runBtn) {
        c3Say(runBtn, c3Fill(runTpl, { method: String(met.label || "").toLowerCase() }));
        setHidden(runBtn, !(predicted && !isRan));
      }
      setHidden(panel, !isRan);
      if (isRan) {
        c3Say(outs.time, cfg.show_timings === false
          ? (cfg.timings_hidden || "") : (met.time || ""));
        c3Say(outs.quality, met.quality || "");
        draw(sol, met);
        if (dish) {
          /* The alt text is COMPOSED from the live count and a size word
             chosen off the method's own size, so it is true in every one of
             the nine states rather than in the one it was written for. */
          dish.setAttribute("aria-label", c3Fill(dishAlt.template || "", {
            count: met.count, product: sol.product || "",
            size_words: c3CrystSizeWord(dishAlt.size_words, met.size)
          }));
        }
        c3Say(verdictEl, met.note || "");
        c3Say(hazardEl,
          met.id === fastest ? (sol.hard || "") + " " + (met.hazard || "")
            : met.id === slowest ? (sol.slow || "") + " " + (met.hazard || "")
            : (met.hazard || ""));
      }
      setHidden(summaryEl, nMethods < total);
      markStage(sec, nMethods >= total);
    }

    each(dials, function (btn) {
      btn.addEventListener("click", function () {
        var g = btn.getAttribute("data-cryst-for");
        var v = btn.getAttribute("data-cryst-val");
        if (pick[g] === undefined || pick[g] === v) { return; }
        pick[g] = v;
        predicted = false;
        paint();
      });
    });
    each(gopts, function (b) {
      b.addEventListener("click", function () {
        each(gopts, function (x) {
          x.setAttribute("aria-pressed", x === b ? "true" : "false");
        });
        if (predicted) { return; }
        predicted = true;
        paint();
      });
    });
    if (runBtn) {
      runBtn.addEventListener("click", function () {
        var key = pick.solute + ":" + pick.method;
        if (!predicted || ran[key]) { return; }
        ran[key] = true;
        if (!methodsRun[pick.method]) { methodsRun[pick.method] = true; nMethods += 1; }
        paint();
        focusReveal(panel);  // MRB-257 (5.43)
      });
    }
    paint();
  }

  /* ── still-run (c3-05 #s-still) ──────────────────────────────────────
     Three mixtures × two condenser states, run a stage at a time.

     ⚖️ BOIL TO SEPARATE, COOL TO COLLECT — AND DOING ONE OF THEM GETS YOU
     NOTHING. The no-cooling branch is not an error and not a lesser state:
     the boiling separates the mixture perfectly, the flask proves it, and
     the beaker is empty because the vapour went out of the open end. It is
     drawn with the same weight as a successful run, every stage of it has
     something true to say, and per `completion.requires_cooling` it does NOT
     tick the rail — the student has seen something true and has not yet
     distilled anything.

     ⚠️ THE LAST STAGE HAS ITS OWN WARM TEXT. Design overrides only stage 3
     and leaves stage 4 saying "Clear drops run into the beaker" over a
     result panel that says the beaker is empty. The payload authors a
     per-mixture `warm_final` for that slot; the branch below is generic —
     ANY stage carrying a `[data-still-warm]` body uses it when the cooling
     is off — so both stages are honest and neither is special-cased.

     ⚠️ WHICH DIAL VALUE MEANS "COOLED" IS READ OFF THE OPENING STATE. The
     payload's `dials[].options[].cooling` flag does not survive into the
     markup or the config (see the delivery report), so the cooling group's
     value that is pressed at wire time — the authored `start`, and the state
     the bench is documented to open in — is the cooled one, and any other
     value in that group is the warm branch. */
  function wireStillRun(sec) {
    var wrap = sec.querySelector("[data-still]");
    if (!wrap) { return; }
    var cfg = c3Cfg(wrap);
    var mixtures = cfg.mixtures || [];
    var gauges = cfg.gauges || [];
    var nStages = parseInt(cfg.stages, 10) || 0;
    var comp = cfg.completion || {};
    var need = parseInt(comp.runs, 10) || 1;
    var requiresCooling = comp.requires_cooling !== false;
    if (!mixtures.length || !nStages) { return; }

    var dials = toArray(wrap.querySelectorAll("[data-still-for]"));
    var body = wrap.querySelector("[data-still-body]");
    var nextBtn = wrap.querySelector("[data-still-next]");
    var resetBtn = wrap.querySelector("[data-still-reset]");
    var predicts = toArray(wrap.querySelectorAll("[data-still-predict]"));
    var stageLists = toArray(wrap.querySelectorAll("[data-still-stages]"));
    var results = toArray(wrap.querySelectorAll("[data-still-result]"));
    var startLabel = nextBtn ? (nextBtn.getAttribute("data-still-start-label") || "") : "";
    var nextLabel = nextBtn ? (nextBtn.getAttribute("data-still-next-label") || "") : "";
    var gvals = {};
    each(wrap.querySelectorAll("[data-still-gval]"), function (el) {
      gvals[el.getAttribute("data-still-gval")] = el;
    });

    var pick = {}, coldVal = null;
    each(dials, function (b) {
      var g = b.getAttribute("data-still-for");
      if (pick[g] === undefined) { pick[g] = null; }
      if (b.getAttribute("aria-pressed") === "true") {
        pick[g] = b.getAttribute("data-still-val");
        if (g === "cooling") { coldVal = pick[g]; }
      }
    });
    if (pick.mixture === null || pick.mixture === undefined) {
      pick.mixture = (cfg.start || {}).mixture || mixtures[0].id;
    }
    var stage = 0, predicted = false, runs = {}, nRuns = 0;

    function cold() { return coldVal === null || pick.cooling === coldVal; }

    function paint() {
      var mix = c3By(mixtures, pick.mixture) || mixtures[0];
      var isCold = cold();
      var done = stage >= nStages;

      each(dials, function (b) {
        b.setAttribute("aria-pressed",
          pick[b.getAttribute("data-still-for")] === b.getAttribute("data-still-val")
            ? "true" : "false");
      });
      /* The predict panel is REPLACED by the bench, not greyed beside it. */
      each(predicts, function (p) {
        setHidden(p, predicted || p.getAttribute("data-still-predict") !== pick.mixture);
      });
      setHidden(body, !predicted);

      /* Every gauge has a resting reading of its own, so no gauge ever reads
         blank — including at stage 0, with the Bunsen not lit. */
      each(gauges, function (g) {
        var el = gvals[g.id];
        if (!el) { return; }
        var v;
        if (g.show === false) { v = g.hidden_value || g.before || ""; }
        else if (stage === 0) { v = g.before_from === "name" ? (mix.name || "") : (g.before || ""); }
        else if (!isCold && g.warm_value) { v = g.warm_value; }
        else { v = mix[g.reads] || ""; }
        c3Say(el, v);
      });

      each(stageLists, function (ol) {
        setHidden(ol, ol.getAttribute("data-still-stages") !== pick.mixture);
        each(ol.querySelectorAll("[data-still-stage]"), function (li) {
          var i = parseInt(li.getAttribute("data-still-stage"), 10);
          var warmEl = li.querySelector("[data-still-warm]");
          var useWarm = !isCold && !!warmEl;
          setHidden(li.querySelector("[data-still-stagebody]"), !(i < stage));
          setHidden(warmEl, !useWarm);
          setHidden(li.querySelector("[data-still-text]"), useWarm);
        });
      });

      if (nextBtn) {
        c3Say(nextBtn, stage === 0 ? startLabel : nextLabel);
        setHidden(nextBtn, done);
      }
      /* `warm` is a result of the same weight as the three mixtures'. */
      var which = done ? (isCold ? pick.mixture : "warm") : null;
      each(results, function (r) {
        setHidden(r, r.getAttribute("data-still-result") !== which);
      });
      markStage(sec, nRuns >= need);
    }

    each(dials, function (btn) {
      btn.addEventListener("click", function () {
        var g = btn.getAttribute("data-still-for");
        var v = btn.getAttribute("data-still-val");
        if (pick[g] === undefined || pick[g] === v) { return; }
        pick[g] = v;
        stage = 0;
        /* A different mixture is a different question, so the prediction
           goes with it; the condenser switch is the same question. */
        if (g === "mixture") { predicted = false; }
        paint();
      });
    });
    each(predicts, function (p) {
      var pOpts = toArray(p.querySelectorAll(".ks3-option"));
      each(pOpts, function (b) {
        b.addEventListener("click", function () {
          each(pOpts, function (x) {
            x.setAttribute("aria-pressed", x === b ? "true" : "false");
          });
          if (predicted) { return; }
          predicted = true;
          paint();
          focusReveal(body);  // MRB-257 (5.43)
        });
      });
    });
    if (nextBtn) {
      nextBtn.addEventListener("click", function () {
        if (stage >= nStages) { return; }
        stage += 1;
        if (stage >= nStages && (!requiresCooling || cold())) {
          if (!runs[pick.mixture]) { runs[pick.mixture] = true; nRuns += 1; }
        }
        paint();
        if (stage >= nStages) {
          var open = null;
          each(results, function (r) { if (!r.hasAttribute("hidden")) { open = r; } });
          focusReveal(open);  // MRB-257 (5.43)
        }
      });
    }
    if (resetBtn) {
      resetBtn.addEventListener("click", function () {
        if (!stage && !predicted) { return; }
        stage = 0;
        predicted = false;
        each(predicts, function (p) {
          each(p.querySelectorAll(".ks3-option"), function (x) {
            x.setAttribute("aria-pressed", "false");
          });
        });
        paint();
      });
    }
    paint();
  }

  /* ── chroma-run (c3-06 #s-lab) ───────────────────────────────────────
     Three decisions, three distinct ways of ruining the run, and a forensic
     verdict at the end of a readable one.

     ⚖️ EACH FAULT NAMES WHICH DECISION CAUSED IT. Never "you got it wrong":
     "You drew the baseline in pen. Pen ink is a mixture of dyes dissolved in
     a solvent — exactly the thing this experiment separates." `fault_order`
     gives precedence, so a run with two mistakes is diagnosed by the one
     that ruined it first, and the precedence is the payload's rather than
     the order the buttons happen to sit in.

     ⚖️ SPOTS ARE PLACED BY `rf` AS A PERCENTAGE OF THE LANE, using
     `lane_geometry`, and no pixel position is computed anywhere. A real
     photographed chromatogram can replace the drawn lane without a payload
     change so long as the geometry stays a ratio.

     ⚠️ THE VERDICT ROW EXISTS ONLY ON A READABLE RUN, and the rail ticks on
     the VERDICT, not on pressing Run — a ruined run is a thing that
     happened, not the question answered. */

  function c3Pct(v) {
    var s = Number(v).toFixed(4);
    if (s.indexOf(".") >= 0) { s = s.replace(/0+$/, "").replace(/\.$/, ""); }
    return s;
  }

  function wireChromaRun(sec) {
    var wrap = sec.querySelector("[data-chroma]");
    if (!wrap) { return; }
    var cfg = c3Cfg(wrap);
    var geom = cfg.geometry || {};
    var faults = cfg.faults || {};
    var order = cfg.fault_order || [];
    var lanes = cfg.lanes || [];
    var dials = toArray(wrap.querySelectorAll("[data-chroma-for]"));
    var runBtn = wrap.querySelector("[data-chroma-run]");
    var paper = wrap.querySelector("[data-chroma-paper]");
    var outcomes = wrap.querySelector("[data-chroma-outcomes]");
    var outEls = toArray(wrap.querySelectorAll("[data-chroma-outcome]"));
    var verdictEl = wrap.querySelector("[data-chroma-verdict]");
    var pens = toArray(wrap.querySelectorAll("[data-chroma-pen]"));
    var says = toArray(wrap.querySelectorAll("[data-chroma-say]"));
    var laneEls = toArray(wrap.querySelectorAll("[data-chroma-lane]"));
    var goodAlt = cfg.good_alt || (paper ? paper.getAttribute("aria-label") : "");
    if (!dials.length || !runBtn) { return; }

    var pick = {};
    each(dials, function (b) {
      if (b.getAttribute("aria-pressed") === "true") {
        pick[b.getAttribute("data-chroma-for")] = b.getAttribute("data-chroma-val");
      }
    });
    var ran = false, chosen = null;

    function faultNow() {
      var live = {}, i;
      each(dials, function (b) {
        if (pick[b.getAttribute("data-chroma-for")] !== b.getAttribute("data-chroma-val")) { return; }
        var f = b.getAttribute("data-chroma-fault");
        if (f) { live[f] = true; }
      });
      for (i = 0; i < order.length; i++) { if (live[order[i]]) { return order[i]; } }
      return null;
    }

    function drawPaper(fault) {
      var spec = fault ? (faults[fault] || {}) : {};
      var base = Number(geom.baseline_pct || 0);
      var span = Number(geom.span_pct || 0);
      each(laneEls, function (laneEl) {
        var line = laneEl.querySelector("[data-chroma-baseline]");
        if (line) {
          /* The baseline drawn in pen is a line of dissolved dyes, and it
             is drawn as one: darker and heavier than a graphite line. */
          if (spec.baseline === "ink") {
            line.style.background = "var(--ks3-ink)";
            line.style.height = "3px";
          } else {
            line.style.background = "";
            line.style.height = "";
          }
        }
        each(laneEl.querySelectorAll("[data-chroma-spot]"), function (sp, i) {
          var rf = Number(sp.getAttribute("data-rf"));
          var smear = false;
          if (spec.spots === "none") { setHidden(sp, true); return; }
          setHidden(sp, false);
          if (spec.spots === "smeared") {
            smear = true;
            rf = Number(spec.smear_start_rf || 0) + i * Number(spec.smear_step_rf || 0);
          } else if (spec.spots === "crushed") {
            rf = Math.min(Number(spec.crush_cap_rf || 1),
                          rf + (1 - rf) * Number(spec.crush_toward_front || 0));
          }
          sp.style.bottom = c3Pct(base + rf * span) + "%";
          /* Smeared spots are drawn as a band across the lane rather than a
             dot in it. Cleared rather than overwritten on a clean run, so
             the stylesheet keeps the drawing. */
          sp.style.width = smear ? "92%" : "";
          sp.style.height = smear ? "10px" : "";
          sp.style.borderRadius = smear ? "3px" : "";
          sp.style.opacity = smear ? "0.5" : "";
        });
      });
    }

    function paint() {
      var fault = faultNow();
      each(dials, function (b) {
        b.setAttribute("aria-pressed",
          pick[b.getAttribute("data-chroma-for")] === b.getAttribute("data-chroma-val")
            ? "true" : "false");
      });
      setHidden(paper, !ran);
      setHidden(outcomes, !ran);
      if (ran) {
        drawPaper(fault);
        if (paper) {
          paper.setAttribute("aria-label",
            fault ? ((faults[fault] || {}).alt || "") : goodAlt);
        }
        each(outEls, function (o) {
          setHidden(o, o.getAttribute("data-chroma-outcome") !== (fault || "good"));
        });
      }
      setHidden(verdictEl, !(ran && !fault));
      each(pens, function (b) {
        b.setAttribute("aria-pressed",
          b.getAttribute("data-chroma-pen") === chosen ? "true" : "false");
        c3Enable(b, chosen === null);
      });
      each(says, function (s) {
        setHidden(s, s.getAttribute("data-chroma-say") !== chosen);
      });
      markStage(sec, chosen !== null);
    }

    each(dials, function (btn) {
      btn.addEventListener("click", function () {
        var g = btn.getAttribute("data-chroma-for");
        var v = btn.getAttribute("data-chroma-val");
        if (pick[g] === undefined || pick[g] === v) { return; }
        pick[g] = v;
        /* A different paper is a different run: it has not been run yet, and
           the verdict is about a chromatogram that is no longer on screen. */
        ran = false;
        chosen = null;
        paint();
      });
    });
    runBtn.addEventListener("click", function () {
      if (ran) { return; }
      ran = true;
      paint();
      focusReveal(paper);  // MRB-257 (5.43)
    });
    each(pens, function (b) {
      b.addEventListener("click", function () {
        if (chosen !== null) { return; }
        chosen = b.getAttribute("data-chroma-pen");
        paint();
        var open = null;
        each(says, function (s) { if (!s.hasAttribute("hidden")) { open = s; } });
        focusReveal(open);  // MRB-257 (5.43)
      });
    });
    paint();
  }

  /* ── melting-point-bench (c3-07 #s-bench) ────────────────────────────
     Three samples, three runs each, two decisions.

     ⚖️ A PURE SAMPLE MELTS SHARPLY; AN IMPURE ONE MELTS LOWER AND OVER A
     RANGE. Both halves are in the numbers, and every number in the table is
     computed here from `samples[].runs` rather than read off a string.

     ⚖️ FAST HEATING MAKES A MEASURED RANGE READ NARROWER, and it is the
     right way round: the thermometer lags the block, so the start is
     recorded late and the end drifts up. `collapse` eats the bottom of the
     range and `end_shift` adds to the top. A student who heats fast gets
     repeats that agree beautifully — because the same error happened three
     times. THE BENCH IS THE MEASUREMENT: if a sentence ever disagrees with a
     number this produces, the number is right.

     ⚖️ THE ANOMALY IS REPORTED, NEVER DROPPED. Batch 3's second run melts
     47.5–52.0 while its other two melt within a degree. Nothing here filters
     `runs` and nothing may be added that does — the rows shown are the first
     `repeats` of them, in order, and the odd one is inside that.

     ⚠️ THE FAST BRANCH IS THE ONE THAT IS NOT `trusted_when.rate`. The
     payload names the rate whose data can carry a claim; the other value of
     a two-value dial is the one the lag model describes. Keyed on the
     payload rather than on the string "fast". */
  function wireMeltingPointBench(sec) {
    var wrap = sec.querySelector("[data-mpb]");
    if (!wrap) { return; }
    var cfg = c3Cfg(wrap);
    var samples = cfg.samples || [];
    if (!samples.length) { return; }
    var model = cfg.fast_model || {};
    var decimals = parseInt(cfg.decimals, 10);
    if (isNaN(decimals)) { decimals = 1; }
    var unit = cfg.unit || "";
    var wideAbove = Number(cfg.wide_above);
    var trust = cfg.trusted_when || {};
    var dials = toArray(wrap.querySelectorAll("[data-mpb-for]"));
    var runBtn = wrap.querySelector("[data-mpb-run]");
    var dataEl = wrap.querySelector("[data-mpb-data]");
    var notes = toArray(wrap.querySelectorAll("[data-mpb-note]"));
    var vBtns = toArray(wrap.querySelectorAll("[data-mpb-verdict-btn]"));
    var says = toArray(wrap.querySelectorAll("[data-mpb-say]"));
    var boxes = {};
    each(wrap.querySelectorAll("[data-mpb-sample]"), function (el) {
      boxes[el.getAttribute("data-mpb-sample")] = el;
    });
    var runLabel = runBtn ? (runBtn.getAttribute("data-mpb-runlabel") || "") : "";
    var rerunLabel = runBtn ? (runBtn.getAttribute("data-mpb-rerunlabel") || "") : "";

    var pick = {
      rate: String((cfg.start || {}).rate || ""),
      repeats: String((cfg.start || {}).repeats || "")
    };
    var ran = false, chosen = null;

    function reading(run, fast) {
      var s = Number(run.start), e = Number(run.end);
      if (fast) {
        s = s + (e - s) * Number(model.collapse || 0);
        e = e + Number(model.end_shift || 0);
      }
      return [s, e, e - s];
    }

    function paint() {
      var fast = !!trust.rate && pick.rate !== trust.rate;
      var reps = parseInt(pick.repeats, 10) || 0;

      each(dials, function (b) {
        b.setAttribute("aria-pressed",
          pick[b.getAttribute("data-mpb-for")] === b.getAttribute("data-mpb-val")
            ? "true" : "false");
      });
      if (runBtn) { c3Say(runBtn, ran ? rerunLabel : runLabel); }
      setHidden(dataEl, !ran);
      if (!ran) { markStage(sec, chosen !== null); return; }

      each(samples, function (sm) {
        var box = boxes[sm.id];
        if (!box) { return; }
        each(box.querySelectorAll("[data-mpb-row]"), function (tr) {
          var i = parseInt(tr.getAttribute("data-mpb-row"), 10);
          var run = (sm.runs || [])[i];
          setHidden(tr, i >= reps);
          if (!run) { return; }
          var r = reading(run, fast);
          each(tr.querySelectorAll("[data-mpb-cell]"), function (td) {
            var which = td.getAttribute("data-mpb-cell");
            var v = which === "start" ? r[0] : which === "end" ? r[1] : r[2];
            c3Say(td, v.toFixed(decimals) + " " + unit);
            if (which === "range") {
              td.setAttribute("data-mpb-wide", r[2] > wideAbove ? "1" : "0");
            }
          });
        });
      });

      var key = pick.rate + ":" + pick.repeats;
      each(notes, function (n) {
        setHidden(n, n.getAttribute("data-mpb-note") !== key);
      });

      /* Naming the right batch off untrustworthy data is not the same
         achievement as measuring it, and the say says so — one tail either
         way, both of them in the document. */
      var trusted = pick.rate === trust.rate
        && reps > Number(trust.repeats_above || 0);
      each(vBtns, function (b) {
        b.setAttribute("aria-pressed",
          b.getAttribute("data-mpb-verdict-btn") === chosen ? "true" : "false");
        c3Enable(b, chosen === null);
      });
      each(says, function (s) {
        var on = s.getAttribute("data-mpb-say") === chosen;
        setHidden(s, !on);
        setHidden(s.querySelector("[data-mpb-trusted]"), !(on && trusted));
        setHidden(s.querySelector("[data-mpb-untrusted]"), !(on && !trusted));
      });
      markStage(sec, chosen !== null);
    }

    each(dials, function (btn) {
      btn.addEventListener("click", function () {
        var g = btn.getAttribute("data-mpb-for");
        var v = btn.getAttribute("data-mpb-val");
        if (pick[g] === undefined || pick[g] === v) { return; }
        pick[g] = v;
        /* New settings, so the table on screen is not the table these
           settings produce, and the verdict was about the old one. */
        ran = false;
        chosen = null;
        paint();
      });
    });
    if (runBtn) {
      runBtn.addEventListener("click", function () {
        var first = !ran;
        ran = true;
        paint();
        if (first) { focusReveal(dataEl); }  // MRB-257 (5.43)
      });
    }
    each(vBtns, function (b) {
      b.addEventListener("click", function () {
        if (chosen !== null) { return; }
        chosen = b.getAttribute("data-mpb-verdict-btn");
        paint();
        var open = null;
        each(says, function (s) { if (!s.hasAttribute("hidden")) { open = s; } });
        focusReveal(open);  // MRB-257 (5.43)
      });
    });
    paint();
  }

/* ═══ END C3 wiring ═══ */

/* ═══ BEGIN C4 wiring ═══════════════════════════════════════════════════
   C4's instrument families. Added as ONE marked block so that a lane merging
   into this file resolves mechanically: nothing above this marker moves.
   ═══ */

/* ── from js_01.js ── */
  /* ── change-pairs (c4-01 #s-pairs) ──────────────────────────────────
     Three pairs, six commitments, and the shared clue never decides any of
     them. This is `c3CommitCards`' contract exactly — one commitment per
     card, final, with the reveal on screen the instant the card is decided,
     so a second press would be a student choosing an answer they can already
     read — so it shares that body rather than growing a fourth copy of the
     same rule. The nesting is the only difference and it costs nothing:
     `wrap.querySelectorAll(sel.card)` finds all six sides through the three
     pair panels.

     ⚠️ NOTHING HERE MARKS. There is no `correct` key in the payload and
     nothing below looks for one: the verdict panel opens in the same voice
     whichever button was pressed, and only the mastery ladder marks.

     ⚠️ NO `count: true`. Design draws no head counter on this block, and
     `setCount` would no-op on the missing `[data-count]` anyway — saying so
     here so that a future pass adding a counter knows it has to be drawn as
     well as wired. The rail stop ticks off the close panel instead: six of
     six decided opens it and calls `markStage`. */
  function wireChangePairs(sec) {
    c3CommitCards(sec, {
      wrap: "[data-cpair]", card: "[data-cpair-side]",
      opt: "[data-cpair-opt]", reveal: "[data-cpair-reveal]",
      close: "[data-cpair-close]"
    });
  }

  /* ── chain-build (c4-01 #s-chain) ───────────────────────────────────
     The CONTRAST family's linked-comparison step, and the one place in the
     unit where the model answer is shown in full.

     ⚖️ THE SENTENCE IS JOINED FROM THE BUTTONS THEMSELVES. Both clauses are
     already in the document, in the `.ks3-opt-label` of the pressed option,
     so nothing is duplicated between the renderer and this file and no clause
     can drift between the two. `appendAuthored` puts the joined text in, so
     an arrow or a tick in a clause is drawn rather than shipped as a
     character the font subsets do not carry.

     ⚖️ AND NEITHER NOTE IS A MARK. `data-chain-ideal` names the clause pair
     that makes a linked comparison, and all it chooses is which of the two
     authored paragraphs is unhidden — same panel, same ground, same voice.
     Every clause on offer is true; what the note is about is whether the two
     halves answer each other. No option is ticked, crossed or dimmed here.

     ⚠️ THE SLOTS DO NOT LOCK, which is Design's behaviour: her handler sets
     the index and nothing else, so a student can re-pick either half and
     watch the sentence and the note change. `markStage` is a ratchet, so a
     stop earned by the first complete pair cannot be unticked by re-picking.

     ⚠️ `focusReveal` runs on the FIRST open only. The panel arrives once and
     a keyboard user is taken to it; re-picking a clause updates it in place
     and must not yank focus off the control they are still using. */
  function wireChainBuild(sec) {
    var wrap = sec.querySelector("[data-chain]");
    if (!wrap) { return; }
    var slots = toArray(wrap.querySelectorAll("[data-chain-slot]"));
    if (slots.length < 2) { return; }
    var reveal = wrap.querySelector("[data-chain-reveal]");
    var out = wrap.querySelector("[data-chain-sentence]");
    var chosen = {};
    var opened = false;

    /* "a:0,b:0" — the clause pair that earns the marks, per slot id. */
    var ideal = {};
    each(String(wrap.getAttribute("data-chain-ideal") || "").split(","),
      function (bit) {
        var kv = bit.split(":");
        if (kv.length === 2) { ideal[kv[0]] = kv[1]; }
      });

    function labelOf(btn) {
      var el = btn.querySelector(".ks3-opt-label");
      return el ? el.textContent : "";
    }

    function paint() {
      var i, id, parts = [], isIdeal = true;
      for (i = 0; i < slots.length; i++) {
        id = slots[i].getAttribute("data-chain-slot");
        if (!chosen[id]) { return; }
        parts.push(labelOf(chosen[id]));
        if (String(chosen[id].getAttribute("data-i")) !== ideal[id]) {
          isIdeal = false;
        }
      }
      c3Empty(out);
      appendAuthored(out, parts.join(" "));
      each(wrap.querySelectorAll("[data-chain-note]"), function (p) {
        var want = isIdeal ? "ideal" : "other";
        setHidden(p, p.getAttribute("data-chain-note") !== want);
      });
      setHidden(reveal, false);
      markStage(sec, true);
      if (!opened) { opened = true; focusReveal(reveal); }
    }

    each(slots, function (slot) {
      var id = slot.getAttribute("data-chain-slot");
      var opts = toArray(slot.querySelectorAll("[data-i]"));
      each(opts, function (btn) {
        btn.addEventListener("click", function () {
          chosen[id] = btn;
          each(opts, function (b) {
            b.setAttribute("aria-pressed", b === btn ? "true" : "false");
          });
          paint();
        });
      });
    });
  }


/* ── from js_02.js ── */
  /* ═══ c4-02 · atom-rearranger + impossible-ask ══════════════════════════

     Two instruments, and between them the flagship of C4.

     ⚖️ NEITHER OF THESE COMPOSES A SENTENCE, A NUMBER OR A COLOUR. Every
     stage of every reaction and every verdict panel is in the document
     already, rendered by `ks3_art/c4.py`; all the code below does is decide
     which one is on screen. There is no `data-cfg` on either family and there
     is nothing here to parse, so nothing can drift between the Python that
     drew the page and the JavaScript that drives it.

     ⚖️ ONLY THE LADDER MARKS. Nothing green and nothing red reaches any
     control in either instrument. The gate options are COMMITMENTS: they take
     the ordinary pressed treatment, they carry no correctness flag, and the
     answer arrives as the next stage of the picture. The refusal panel is a
     panel of WORDS.

     ⊖ NOTHING ANIMATES, NOTHING COUNTS DOWN and there is no canvas — no rAF,
     no timer, no JS-driven transition — so `prefers-reduced-motion` has
     nothing to degrade here and neither function asks about it. If a later
     revision animates anything it must ask `motionReduced()` INSIDE the tick
     (contract R4). MRB-210's input+change rule has nothing to bind either:
     neither instrument draws a range.

     ⚠️ THE NO-OP PRESS. Both dials return early when the value pressed is the
     value already pressed. Design's own handlers do not: pressing the loaded
     reaction again resets it to stage 0 and discards the gate, which is a
     control claiming to be pressed and then undoing the student's work.
     Corrected here rather than reproduced. */

  /* ── atom-rearranger (c4-02 #s-rearr) ────────────────────────────────
     Three reactions x three stages, plus a commitment between stage 1 and
     stage 2. Nine views, and exactly one on screen at a time.

     ⚖️ CREDIT IS FOR CARRYING ALL THREE REACTIONS TO THEIR PRODUCTS, which
     is Design's own `DONE()`. `done` is never emptied — not by "Put it back",
     not by switching reaction — so a student can take a finished reaction
     apart again to look at it without losing the stop. `markStage` is the
     ratchet and this file does not write its own.

     ⚠️ THE STAGE RESETS WHEN THE REACTION CHANGES, and the gate goes with it.
     A different reaction is a different question — "how many oxygen atoms
     will be in the water" is not a question about methane — so carrying the
     old commitment across would leave a gate answered that was never asked.

     ⚠️ THE WHOLE STATE SPACE, and it is enumerated rather than sampled:
     3 reactions x 3 stages = 9 views, each with its own count table, its own
     commentary and its own `role="img"` label; the gate is open in exactly
     one of those nine (stage 1, before an option is pressed); the advance
     button is hidden in two of them (stage 2, and stage 1 with the gate
     open); and the resting state — reaction one, stage 0, nothing committed,
     nothing done — is the tenth thing that has to be right and is the one a
     page is in before anybody touches it. */
  function wireAtomRearranger(sec) {
    var wrap = sec.querySelector("[data-arr]");
    if (!wrap) { return; }
    var tabs = toArray(wrap.querySelectorAll("[data-arr-tab]"));
    if (!tabs.length) { return; }

    var total = parseInt(wrap.getAttribute("data-total"), 10) || tabs.length;
    var words = toArray(wrap.querySelectorAll("[data-arr-words]"));
    var heads = toArray(wrap.querySelectorAll("[data-arr-stagename]"));
    var views = toArray(wrap.querySelectorAll("[data-arr-groups]"));
    var bodies = toArray(wrap.querySelectorAll("[data-arr-counts]"));
    var pending = toArray(wrap.querySelectorAll("[data-arr-pending]"));
    var numbers = toArray(wrap.querySelectorAll("[data-arr-num]"));
    var says = toArray(wrap.querySelectorAll("[data-arr-stagetext]"));
    var gates = toArray(wrap.querySelectorAll("[data-arr-gate]"));
    var advance = wrap.querySelector("[data-arr-advance]");
    var advLabels = toArray(wrap.querySelectorAll("[data-arr-adv]"));
    var reset = wrap.querySelector("[data-arr-reset]");
    var closer = wrap.querySelector("[data-arr-done]");

    /* Read the opening reaction off the markup rather than assuming the
       first button: the renderer decides which tab is pressed at rest, and
       two places deciding that is two places to change it. */
    var rx = tabs[0].getAttribute("data-arr-tab");
    each(tabs, function (b) {
      if (b.getAttribute("aria-pressed") === "true") {
        rx = b.getAttribute("data-arr-tab");
      }
    });
    var stage = 0, gate = null, done = {}, nDone = 0;

    function gateOpen() { return stage === 1 && gate === null; }

    function clearGate() {
      each(wrap.querySelectorAll("[data-arr-gateopt]"), function (b) {
        b.setAttribute("aria-pressed", "false");
      });
    }

    function paint() {
      var key = rx + "|" + stage;
      var made = stage === 2;
      var needed = gateOpen();

      each(tabs, function (b) {
        b.setAttribute("aria-pressed",
          b.getAttribute("data-arr-tab") === rx ? "true" : "false");
      });
      each(words, function (p) {
        setHidden(p, p.getAttribute("data-arr-words") !== rx);
      });
      each(heads, function (p) {
        setHidden(p, p.getAttribute("data-arr-stagename") !== String(stage));
      });
      each(views, function (v) {
        setHidden(v, v.getAttribute("data-arr-groups") !== key);
      });
      each(bodies, function (tb) {
        setHidden(tb, tb.getAttribute("data-arr-counts") !== rx);
      });
      /* The After column reads an em dash until the products exist and the
         tallied number once they do. Both are in the document; neither is
         written here, and the accent treatment on the number is a stylesheet
         rule on a class rather than a colour assembled in JavaScript. */
      each(pending, function (el) { setHidden(el, made); });
      each(numbers, function (el) { setHidden(el, !made); });
      /* Stages 0 and 1 say the same thing whichever reaction is loaded;
         stage 2 is the reaction's own product text. */
      each(says, function (p) {
        setHidden(p, p.getAttribute("data-arr-stagetext") !==
          (made ? "2|" + rx : String(stage)));
      });
      each(gates, function (g) {
        setHidden(g, !(needed && g.getAttribute("data-arr-gate") === rx));
      });
      if (advance) {
        setHidden(advance, made || needed);
        each(advLabels, function (s) {
          setHidden(s, s.getAttribute("data-arr-adv") !== String(stage));
        });
      }
      setHidden(closer, nDone < total);
      markStage(sec, nDone >= total);
    }

    each(tabs, function (btn) {
      btn.addEventListener("click", function () {
        var v = btn.getAttribute("data-arr-tab");
        if (v === rx) { return; }        /* the no-op press */
        rx = v;
        stage = 0;
        gate = null;
        clearGate();
        paint();
      });
    });

    each(wrap.querySelectorAll("[data-arr-gateopt]"), function (btn) {
      btn.addEventListener("click", function () {
        /* Scope the pressed state to the gate the button is in, not to the
           whole instrument: all three gates are in the document and only one
           is on screen, so a wrap-wide sweep would silently un-press the
           other two reactions' commitments. */
        var panel = btn.closest ? btn.closest("[data-arr-gate]") : null;
        each((panel || wrap).querySelectorAll("[data-arr-gateopt]"),
          function (x) {
            x.setAttribute("aria-pressed", x === btn ? "true" : "false");
          });
        if (gate !== null) { return; }
        gate = parseInt(btn.getAttribute("data-arr-gateopt"), 10);
        paint();
        focusReveal(advance);            /* MRB-257 (5.43) */
      });
    });

    if (advance) {
      advance.addEventListener("click", function () {
        if (stage >= 2 || gateOpen()) { return; }
        stage += 1;
        if (stage === 2 && !done[rx]) { done[rx] = true; nDone += 1; }
        paint();
        if (stage === 2) {
          var open = null;
          each(says, function (p) {
            if (!p.hasAttribute("hidden")) { open = p; }
          });
          focusReveal(nDone >= total && closer ? closer : open);
        }
      });
    }

    if (reset) {
      reset.addEventListener("click", function () {
        if (stage === 0 && gate === null) { return; }
        stage = 0;
        gate = null;
        clearGate();
        /* `done` survives, deliberately: a reaction already carried to its
           products has been carried to its products, and taking it apart
           again to look at it is not undoing that. */
        paint();
      });
    }

    paint();
  }

  /* ── impossible-ask (c4-02 #s-impossible) ────────────────────────────
     Four asks, two of which the bench refuses, and the refusal is where
     balancing is born three lessons later.

     ⚖️ THE BRANCH IS NOT HERE AND MUST NOT COME HERE. Which asks are refused
     was decided in `ks3_art/c4.py`, from the atoms on the table against the
     atoms each product is built from, and it shows up in the DOM as which
     panel exists under which id. This function cannot tell a refusal from a
     build and has no reason to: it shows the panel belonging to the button
     that was pressed. A `possible` flag read here would be a second opinion
     about the chemistry, free to disagree with the first.

     ⚠️ THE RAIL TICKS ON ANY ASK, refused or built. What is being credited is
     having asked and read what came back — and a student who asks for water
     first, and only then for gold, has done the more thorough thing.

     ⚠️ FIVE STATES, and the fifth is the one the page loads in: nothing
     pressed, no panel open, `data-stage-done="0"`. */
  function wireImpossibleAsk(sec) {
    var wrap = sec.querySelector("[data-iask]");
    if (!wrap) { return; }
    var btns = toArray(wrap.querySelectorAll("[data-iask-ask]"));
    var panels = toArray(wrap.querySelectorAll("[data-iask-verdict]"));
    if (!btns.length || !panels.length) { return; }
    var open = null;

    each(btns, function (btn) {
      btn.addEventListener("click", function () {
        var id = btn.getAttribute("data-iask-ask");
        if (id === open) { return; }     /* the no-op press */
        open = id;
        each(btns, function (b) {
          b.setAttribute("aria-pressed", b === btn ? "true" : "false");
        });
        var shown = null;
        each(panels, function (p) {
          var on = p.getAttribute("data-iask-verdict") === id;
          setHidden(p, !on);
          if (on) { shown = p; }
        });
        markStage(sec, true);
        focusReveal(shown);              /* MRB-257 (5.43) */
      });
    });
  }


//
// Order between the two does not matter — neither reads the other's DOM and
// neither broadcasts. Both belong in a new "═══ BEGIN C4 wiring ═══" group.


/* ── from js_03.js ── */
  /* ── equation-builder (c4-03 #s-builder) ────────────────────────────
     Three cases, one bench, and a check that names the wrong RULE.

     ⚖️ THE DOM IS THE STATE, AT THE CASE LEVEL. All three cases are in the
     document and one is shown, so a case that has been checked is still
     checked when the student comes back to it — there is nothing to
     re-render and nothing to restore. What this file keeps is only what
     cannot be read off the markup: which side each substance was put on,
     and whether the case has been checked yet.

     ⚠️ NOT ONE SENTENCE IS COMPOSED HERE THAT IS NOT A TEMPLATE. The six
     distractor corrections, the four fixed titles, the "that is the
     equation" text and the three model equations are all authored markup
     that this file only shows. The two wrong-side sentences and the
     missing-substance sentence have a NAME substituted into them, and
     those three templates come out of `data-eqb-cfg` — the payload's own
     strings, so Python and JS are reading one authored sentence rather
     than keeping two.

     ⚠️ AND NOTHING HERE MARKS (R3). A placed chip shows that it was
     PLACED; the buttons keep the platform's ordinary pressed treatment
     whether the placement was right or wrong. The check panel is a panel
     of words, and it is the same panel whichever branch it lands on. */

  function c4EqbShowOnly(wrap, attr, id) {
    each(wrap.querySelectorAll("[" + attr + "]"), function (el) {
      setHidden(el, el.getAttribute(attr) !== id);
    });
  }

  function c4EqbOne(wrap, attr, id) {
    var found = null;
    each(wrap.querySelectorAll("[" + attr + "]"), function (el) {
      if (el.getAttribute(attr) === id) { found = el; }
    });
    return found;
  }

  /* Design's four branches, in her order and with her precedence: a
     distractor in the equation is reported before a substance on the wrong
     side, and a wrong side before a missing substance. The order is the
     teaching — "one thing in there does not belong" is a bigger finding
     than "magnesium oxide is on the wrong side", and being told the
     smaller one first would send a student looking in the wrong place. */
  function c4EqbVerdict(c, place) {
    var wrong = [], used = [], missing = [], i, n, p, isR, isP;
    for (i = 0; i < (c.names || []).length; i++) {
      n = c.names[i];
      p = place[n];
      isR = c.reactants.indexOf(n) >= 0;
      isP = c.products.indexOf(n) >= 0;
      if (p) {
        if (isR && p !== "left") { wrong.push(n); }
        else if (isP && p !== "right") { wrong.push(n); }
        else if (!isR && !isP) { used.push(n); }
      } else if (isR || isP) {
        missing.push(n);
      }
    }
    if (!wrong.length && !used.length && !missing.length) {
      return { branch: "perfect" };
    }
    if (used.length) { return { branch: "distractor", name: used[0] }; }
    if (wrong.length) {
      return { branch: "side", name: wrong[0],
               isProduct: c.products.indexOf(wrong[0]) >= 0 };
    }
    return { branch: "missing", names: missing };
  }

  function wireEquationBuilder(sec) {
    var wrap = sec.querySelector("[data-eqb]");
    if (!wrap) { return; }
    var cfg = c3Cfg(wrap, "data-eqb-cfg");
    var cases = cfg.cases || [];
    if (!cases.length) { return; }
    var verdict = cfg.verdict || {};
    var join = cfg.missing_join || " and ";
    var total = parseInt(wrap.getAttribute("data-eqb-total"), 10) || cases.length;
    var checkBtn = wrap.querySelector("[data-eqb-check]");
    var clearBtn = wrap.querySelector("[data-eqb-clear]");

    var active = cases[0].id;
    var places = {}, shown = {}, counted = {}, nChecked = 0;
    each(cases, function (c) { places[c.id] = {}; });

    function paintVerdict(c, panel) {
      var v = c4EqbVerdict(c, places[c.id] || {});
      each(panel.querySelectorAll("[data-eqb-branch]"), function (el) {
        setHidden(el, el.getAttribute("data-eqb-branch") !== v.branch);
      });
      /* The correction is the DISTRACTOR'S OWN, authored beside it and
         shown — never assembled, and never a generic "that does not go in
         an equation". Heat is not a substance for a different reason than
         limewater is not part of this reaction. */
      each(panel.querySelectorAll("[data-eqb-why]"), function (el) {
        setHidden(el, el.getAttribute("data-eqb-why") !== v.name);
      });
      if (v.branch === "side") {
        c3Say(panel.querySelector("[data-eqb-sidetitle]"),
              c3Fill(verdict.side_title, { Name: v.name }));
        c3Say(panel.querySelector("[data-eqb-sidetext]"),
              c3Fill(v.isProduct ? verdict.side_product
                                 : verdict.side_reactant,
                     { name: String(v.name).toLowerCase() }));
      } else if (v.branch === "missing") {
        var list = [];
        each(v.names, function (n) { list.push(String(n).toLowerCase()); });
        c3Say(panel.querySelector("[data-eqb-missingtext]"),
              c3Fill(verdict.missing_text, { names: list.join(join) }));
      }
    }

    function paint() {
      var c = c3By(cases, active) || cases[0];
      var place = places[c.id] || {};

      each(wrap.querySelectorAll("[data-eqb-tab]"), function (b) {
        b.setAttribute("aria-pressed",
          b.getAttribute("data-eqb-tab") === c.id ? "true" : "false");
      });
      c4EqbShowOnly(wrap, "data-eqb-story", c.id);
      c4EqbShowOnly(wrap, "data-eqb-bank", c.id);
      c4EqbShowOnly(wrap, "data-eqb-eq", c.id);

      var bank = c4EqbOne(wrap, "data-eqb-bank", c.id);
      var eq = c4EqbOne(wrap, "data-eqb-eq", c.id);
      /* A case in the payload with no panel in the markup is a build that
         went wrong, and it must not take the rest of the page's wiring
         down with it: everything after this in `init()` would be skipped
         by one thrown TypeError. */
      if (!bank || !eq) { return; }
      each(bank.querySelectorAll("[data-eqb-row]"), function (row) {
        var n = row.getAttribute("data-eqb-row");
        var cur = place[n] || "out";
        each(row.querySelectorAll("[data-eqb-place]"), function (b) {
          b.setAttribute("aria-pressed",
            b.getAttribute("data-eqb-place") === cur ? "true" : "false");
        });
        var chip = row.querySelector("[data-eqb-chip]");
        if (chip) {
          if (cur === "out") { chip.removeAttribute("data-eqb-placed"); }
          else { chip.setAttribute("data-eqb-placed", "1"); }
        }
      });

      /* The term nodes are MOVED, never rewritten, so a substance name
         never round-trips through an attribute and the plus signs stay
         real markup. Re-appending in the payload's own order on every
         paint is also what keeps the two sides reading in the order the
         bench lists them, however the student built them up. */
      var boxes = {}, ghosts = {}, terms = {}, counts = { left: 0, right: 0 };
      each(eq.querySelectorAll("[data-eqb-sidebox]"), function (el) {
        boxes[el.getAttribute("data-eqb-sidebox")] = el;
      });
      each(eq.querySelectorAll("[data-eqb-ghost]"), function (el) {
        ghosts[el.getAttribute("data-eqb-ghost")] = el;
      });
      each(eq.querySelectorAll("[data-eqb-term]"), function (el) {
        terms[el.getAttribute("data-eqb-term")] = el;
      });
      var store = eq.querySelector("[data-eqb-store]");
      each(c.names, function (n) {
        var el = terms[n];
        if (!el) { return; }
        var side = place[n];
        var box = (side === "left" || side === "right") ? boxes[side] : null;
        (box || store).appendChild(el);
        var plus = el.querySelector("[data-eqb-plus]");
        if (box) {
          setHidden(plus, counts[side] === 0);
          counts[side] += 1;
        } else {
          setHidden(plus, true);
        }
      });
      setHidden(ghosts.left, counts.left > 0);
      setHidden(ghosts.right, counts.right > 0);

      setHidden(checkBtn,
        !(counts.left > 0 && counts.right > 0 && !shown[c.id]));

      each(wrap.querySelectorAll("[data-eqb-checkpanel]"), function (panel) {
        var id = panel.getAttribute("data-eqb-checkpanel");
        setHidden(panel, id !== c.id || !shown[c.id]);
      });
      if (shown[c.id]) {
        paintVerdict(c, c4EqbOne(wrap, "data-eqb-checkpanel", c.id));
      }
    }

    each(wrap.querySelectorAll("[data-eqb-tab]"), function (b) {
      b.addEventListener("click", function () {
        active = b.getAttribute("data-eqb-tab");
        paint();
      });
    });

    each(wrap.querySelectorAll("[data-eqb-row]"), function (row) {
      var bank = row.parentNode;
      var caseId = bank ? bank.getAttribute("data-eqb-bank") : null;
      var n = row.getAttribute("data-eqb-row");
      each(row.querySelectorAll("[data-eqb-place]"), function (b) {
        b.addEventListener("click", function () {
          var side = b.getAttribute("data-eqb-place");
          var place = places[caseId] || (places[caseId] = {});
          if (side === "out") { delete place[n]; }
          else { place[n] = side; }
          /* Moving a chip retracts the check, exactly as Design does: the
             panel on screen described the equation as it was, and leaving
             it up beside a changed equation would be a verdict on
             something the student is no longer looking at. The rail credit
             does not retract — `markStage` is a ratchet. */
          shown[caseId] = false;
          paint();
        });
      });
    });

    if (checkBtn) {
      checkBtn.addEventListener("click", function () {
        if (shown[active]) { return; }
        /* The rail counts CASES CHECKED, not presses: checking the same
           case again after moving a chip is the student doing the thing
           this bench is for, and it is not a second case. */
        if (!counted[active]) { counted[active] = true; nChecked += 1; }
        shown[active] = true;
        paint();
        markStage(sec, nChecked >= total);
        focusReveal(c4EqbOne(wrap, "data-eqb-checkpanel", active));
      });
    }

    if (clearBtn) {
      clearBtn.addEventListener("click", function () {
        places[active] = {};
        shown[active] = false;
        paint();
      });
    }

    paint();
  }

  /* ── equation-read (c4-03 #s-read) ──────────────────────────────────
     One commitment per card and it is FINAL — `c3CommitCards`' contract,
     the same one the sorter, the jobs list and the plan critique take. The
     reply is on screen the instant the card is decided, so a second press
     would be a student choosing an answer they can already read; both
     buttons disable and the one that was not pressed dims.

     ⚠️ There is no answer key in this markup and none is needed. The reply
     names the reading that is right, and it is the same paragraph either
     way — only the ladder marks. */
  function wireEquationRead(sec) {
    c3CommitCards(sec, {
      wrap: "[data-eqr]",
      card: "[data-eqr-card]",
      opt: "[data-eqr-opt]",
      reveal: "[data-eqr-reply]"
    });
  }


/* ── from js_04.js ── */
  /* ═══ c4-04 · mass-in-a-reaction ═══════════════════════════════════════
     Four instruments: `mass-bench`, `mass-cover`, `mass-worked`,
     `mass-check`. All four tick a rail stop and NOTHING ticks on load
     (MRB-208) — `markStage` is already a ratchet and none of these writes
     `data-stage-done` itself.

     ⚖️ NOTHING IS COMPUTED IN THIS BLOCK. Not one number, not one sentence.
     Every state of every panel is already in the document (EMIT-BOTH-SHOW-ONE)
     and these four handlers do exactly one thing: choose which node is
     `hidden`. So an authored `<strong>`, an em dash and a minus sign survive
     as the author wrote them, no sentence exists twice, and the resting render
     cannot disagree with the runtime one. The single exception is the compare
     button's step number, which the RENDERER fills at build time from the
     step's own index — not here.

     ⚖️ NOTHING GREEN AND NOTHING RED REACHES A CONTROL. A pressed dial, a
     pressed prediction and a pressed cover button all take the platform's
     ordinary `aria-pressed` treatment; every verdict on this page is a PANEL
     OF WORDS. Only the mastery ladder marks (R3 / MRB-196 R10). There is no
     `data-correct` anywhere in these four instruments.

     ⚖️ NOTHING ANIMATES AND NOTHING COUNTS DOWN — no rAF, no timer, no
     JS-driven transition — so `prefers-reduced-motion` has nothing to degrade
     here and no tick has to re-test it (contract R4).

     ⚠️ `wireBalanceBench` IS ALREADY TAKEN, by C2's `[data-balblock]`. This
     bench is `wireMassBench` on `[data-bbenchblock]`, and its family is
     `mass-bench`; see the art fragment's header for why the contract's
     `balance-bench` could not be used. Binding a second handler to C2's hook
     would have wired c2-06's bench to this one's payload.

     ⚠️ THE NO-OP PRESS. Every dial and every cover button below returns early
     when the value pressed is the value already pressed. Design's own bench
     handler does not: pressing the dial that is already lit resets the
     prediction and withdraws the Run button, which is a control claiming to be
     pressed and then taking something off screen. Corrected here rather than
     reproduced — the same correction C3 made across five dials. */

  /* ── mass-bench (c4-04 #s-bench) ────────────────────────────────────
     Two dials, four runs, and the stop ticks only when all four have been
     run. Design's `DONE` is `Object.keys(s.ran).length >= 4`: two runs of one
     reaction say the lid matters, two reactions in one flask say the
     direction varies, and only all four say the reaction never changes the
     mass at all.

     The prediction gate holds the Run button (Law 4), and changing either
     dial withdraws both the prediction and the button — the prediction was
     about the flask the student has just left, so carrying it across would be
     crediting a commitment nobody made. That withdrawal is the one place a
     press does take something off screen, and it is correct there: the dial
     that changed is a DIFFERENT run. */
  function wireMassBench(sec) {
    var wrap = sec.querySelector("[data-bbench]");
    if (!wrap) { return; }
    var total = parseInt(wrap.getAttribute("data-total"), 10) || 0;
    var runBtn = wrap.querySelector("[data-bbench-run]");
    var closer = wrap.querySelector("[data-bbench-close]");
    var dials = toArray(wrap.querySelectorAll("[data-bbench-for]"));
    var predicts = toArray(wrap.querySelectorAll(
      "[data-bbench-predict] .ks3-option"));
    var panels = {};
    each(wrap.querySelectorAll("[data-bbench-panel]"), function (p) {
      panels[p.getAttribute("data-bbench-panel")] = p;
    });
    if (!total || !dials.length) { return; }

    /* The chosen value of each dial, and the dial ORDER, both read off the
       resting DOM rather than assumed. The renderer lights the payload's FIRST
       option and emits the dials in the payload's own order, and the run key
       is those values joined — so which dial comes first, and which value each
       one opens on, stay the payload's business rather than being written down
       a second time here where they could drift from it. */
    var chosen = {}, order = [];
    each(dials, function (b) {
      var name = b.getAttribute("data-bbench-for");
      if (order.indexOf(name) < 0) {
        order.push(name);
        /* Falls back to the first button of the dial, so a resting DOM with
           nothing pressed still produces a real key rather than "null:null". */
        chosen[name] = b.getAttribute("data-bbench-val");
      }
      if (b.getAttribute("aria-pressed") === "true") {
        chosen[name] = b.getAttribute("data-bbench-val");
      }
    });

    var predicted = false;
    var ran = {};

    function key() {
      var parts = [], i;
      for (i = 0; i < order.length; i++) { parts.push(chosen[order[i]]); }
      return parts.join(":");
    }

    function paint() {
      var k = key();
      var done = !!ran[k];
      var name;
      /* One panel visible, and it is this combination's — or none, if this
         combination has not been run. */
      for (name in panels) {
        if (Object.prototype.hasOwnProperty.call(panels, name)) {
          setHidden(panels[name], name !== k || !done);
        }
      }
      /* `canRun` — a prediction is on the table and this run has not happened
         yet. Exactly Design's condition. */
      setHidden(runBtn, !(predicted && !done));
      var n = 0, x;
      for (x in ran) {
        if (Object.prototype.hasOwnProperty.call(ran, x)) { n += 1; }
      }
      if (n >= total) {
        setHidden(closer, false);
        markStage(sec, true);
      }
    }

    each(dials, function (btn) {
      btn.addEventListener("click", function () {
        var name = btn.getAttribute("data-bbench-for");
        var val = btn.getAttribute("data-bbench-val");
        /* The no-op press. See the block header. */
        if (chosen[name] === val) { return; }
        chosen[name] = val;
        each(dials, function (b) {
          if (b.getAttribute("data-bbench-for") !== name) { return; }
          b.setAttribute("aria-pressed",
                         b.getAttribute("data-bbench-val") === val
                           ? "true" : "false");
        });
        /* A new combination is a new run, so the commitment is withdrawn. */
        predicted = false;
        each(predicts, function (p) { p.setAttribute("aria-pressed", "false"); });
        paint();
      });
    });

    each(predicts, function (btn) {
      btn.addEventListener("click", function () {
        if (btn.getAttribute("aria-pressed") === "true") { return; }
        each(predicts, function (p) {
          p.setAttribute("aria-pressed", p === btn ? "true" : "false");
        });
        predicted = true;
        paint();
      });
    });

    if (runBtn) {
      runBtn.addEventListener("click", function () {
        var k = key();
        if (ran[k]) { return; }
        if (!predicted) { return; }
        ran[k] = true;
        paint();
        focusReveal(panels[k]);  /* MRB-257 (5.43) */
      });
    }

    paint();
  }

  /* ── mass-cover (c4-04 #s-cover) ────────────────────────────────────
     MRB-204 part 2: the rule DRAWN, as a part–whole bar, with three cover
     buttons over it.

     ⚖️ THIS IS AN ACTIVITY WITH A REAL COMPLETION SIGNAL, AND THAT IS WHY IT
     TICKS. Design's `DONE('s-cover')` is `s.cover !== null` — a press. There
     is a comment in `build_ks3.py` saying the cover panel is read rather than
     done and belongs off the rail; that is true of C2's READ-ONLY bar and not
     of this one. See the art fragment's header before "fixing" it.

     ⚠️ RADIO, NEVER A TOGGLE. It opens with nothing covered (Design's
     `cover: null`) and from the first press exactly one cell is always
     covered: pressing the lit button again does nothing rather than
     uncovering, because an uncovered bar is a state the instrument had at the
     start and has no way back to that teaches anything.

     ⚠️ `markStage` is a RATCHET, so changing which cell is covered never
     withdraws the credit the first press earned. */
  function wireMassCover(sec) {
    var wrap = sec.querySelector("[data-mcov]");
    if (!wrap) { return; }
    var btns = toArray(wrap.querySelectorAll("[data-mcov-for]"));
    var out = wrap.querySelector("[data-mcov-out]");
    var plates = {}, results = {};
    each(wrap.querySelectorAll("[data-mcov-plate]"), function (p) {
      plates[p.getAttribute("data-mcov-plate")] = p;
    });
    each(wrap.querySelectorAll("[data-mcov-result]"), function (r) {
      results[r.getAttribute("data-mcov-result")] = r;
    });
    if (!btns.length) { return; }
    var covered = null;

    each(btns, function (btn) {
      btn.addEventListener("click", function () {
        var id = btn.getAttribute("data-mcov-for");
        /* The no-op press: this cell is already the covered one. */
        if (covered === id) { return; }
        covered = id;
        each(btns, function (b) {
          b.setAttribute("aria-pressed",
                         b.getAttribute("data-mcov-for") === id
                           ? "true" : "false");
        });
        var name;
        for (name in plates) {
          if (Object.prototype.hasOwnProperty.call(plates, name)) {
            setHidden(plates[name], name !== id);
          }
        }
        for (name in results) {
          if (Object.prototype.hasOwnProperty.call(results, name)) {
            setHidden(results[name], name !== id);
          }
        }
        setHidden(out, false);
        markStage(sec, true);
      });
    });
  }

  /* ── mass-worked (c4-04 #s-worked) ──────────────────────────────────
     MRB-204 part 3: four steps, one at a time, F / I / F / A badges visible
     on each.

     ⚖️ ONE-WAY, AND ONE CONTROL AT A TIME. There is no collapse — unshowing a
     step teaches nothing and gives a student a way to lose their place — and
     the button always opens the NEXT step, because the whole point of the
     pause is that the reader tries the next line before reading it.

     ⚠️ THE TWO BUTTON LABELS ARE BOTH IN THE DOM AND ONE IS SHOWN. "Show the
     first step" and "Show the next step" are authored sentences; §6 forbids a
     sentence round-tripping through a `data-` attribute, so this swaps which
     span is hidden and composes nothing. */
  function wireMassWorked(sec) {
    var wrap = sec.querySelector("[data-mwork]");
    if (!wrap) { return; }
    var total = parseInt(wrap.getAttribute("data-total"), 10) || 0;
    var btn = wrap.querySelector("[data-mwork-next]");
    var first = wrap.querySelector("[data-mwork-label=\"first\"]");
    var next = wrap.querySelector("[data-mwork-label=\"next\"]");
    var steps = [];
    each(wrap.querySelectorAll("[data-mwork-step]"), function (li) {
      steps[parseInt(li.getAttribute("data-mwork-step"), 10)] = li;
    });
    if (!total || !btn) { return; }
    var opened = 0;

    function paint() {
      var i;
      for (i = 0; i < steps.length; i++) {
        if (!steps[i]) { continue; }
        steps[i].setAttribute("data-open", i < opened ? "1" : "0");
        steps[i].setAttribute("data-next", i === opened ? "1" : "0");
        setHidden(steps[i].querySelector("[data-mwork-open]"), i >= opened);
      }
      setHidden(first, opened !== 0);
      setHidden(next, opened === 0);
      if (opened >= total) {
        setHidden(btn, true);
        markStage(sec, true);
      }
    }

    btn.addEventListener("click", function () {
      if (opened >= total) { return; }
      opened += 1;
      paint();
      if (steps[opened - 1]) { focusReveal(steps[opened - 1]); }
    });

    paint();
  }

  /* ── mass-check (c4-04 #s-check) ────────────────────────────────────
     MRB-204 part 4: the same four steps, done by the student, with a compare
     button PER STEP.

     ⚖️ **PER STEP, NOT ONE REVEAL AT THE END, AND THAT IS THE POINT OF THIS
     SECTION.** A student who writes four lines and then opens one panel has
     marked themselves; a student who commits to a line and opens THAT line is
     caught at the step they got wrong, before the error is carried into the
     three after it. It is why this costs a rail stop of its own rather than
     sharing `#s-worked`'s.

     Each step's PROMPT is on the page from the start and its ANSWER is not:
     that is the difference between scaffolding and a solution.

     ⚠️ The button label's step number is the RENDERER's, filled at build time
     from the step's own index. Nothing here writes a number. */
  function wireMassCheck(sec) {
    var wrap = sec.querySelector("[data-mchk]");
    if (!wrap) { return; }
    var total = parseInt(wrap.getAttribute("data-total"), 10) || 0;
    var closer = wrap.querySelector("[data-mchk-close]");
    var steps = [], btns = [];
    each(wrap.querySelectorAll("[data-mchk-step]"), function (li) {
      steps[parseInt(li.getAttribute("data-mchk-step"), 10)] = li;
    });
    each(wrap.querySelectorAll("[data-mchk-btn]"), function (b) {
      btns[parseInt(b.getAttribute("data-mchk-btn"), 10)] = b;
    });
    if (!total) { return; }
    var opened = 0;

    function paint() {
      var i;
      for (i = 0; i < steps.length; i++) {
        if (!steps[i]) { continue; }
        steps[i].setAttribute("data-open", i < opened ? "1" : "0");
        steps[i].setAttribute("data-next", i === opened ? "1" : "0");
        setHidden(steps[i].querySelector("[data-mchk-open]"), i >= opened);
      }
      /* Exactly one compare button is offered, and it is the next unopened
         step's — the same discipline as `#s-worked`, so the two halves of the
         treatment behave identically. */
      for (i = 0; i < btns.length; i++) {
        if (btns[i]) { setHidden(btns[i], i !== opened); }
      }
      if (opened >= total) {
        setHidden(closer, false);
        markStage(sec, true);
      }
    }

    /* A plain loop rather than `each`: `btns` is built by index and a hole in
       it would be SKIPPED by forEach, so a step whose button failed to render
       would silently become unopenable instead of failing. */
    for (var b = 0; b < btns.length; b++) {
      (function (i) {
        if (!btns[i]) { return; }
        btns[i].addEventListener("click", function () {
          /* Only the step the stepper is standing on opens, and only once. */
          if (i !== opened) { return; }
          opened = i + 1;
          paint();
          if (steps[i]) { focusReveal(steps[i]); }
        });
      }(b));
    }

    paint();
  }


/* ── from js_05.js ── */
  /* ═══ c4-05 · coefficient-balancer + forbidden-move ═══════════════════
     Fragment for `shared/ks3.js`. Two wire functions, one shared count.

     ⚖️ NOTHING HERE WRITES A SENTENCE. Every state's words are already in
     the document (EMIT-BOTH-SHOW-ONE, see `art_05.py`); these two functions
     choose which node is shown and write NUMBERS into spans that hold
     nothing else. The one sentence with a variable in it — the "not in its
     smallest numbers" note — was split around its span in Python, so no
     template lives in this file and a `{k}` cannot reach a student even if
     this script never runs.

     ⚖️ NOTHING GREEN AND NOTHING RED REACHES A CONTROL. A matched counter is
     a READING and takes the blue reading treatment. On this page in
     particular that is not a palette preference: `REACT-09` is "a balanced
     equation is a correct equation", and painting "the counts match" in the
     colour this platform uses for "you got it right" would be the
     misconception rendered in CSS, forty lines above the section that
     confronts it.

     ⚖️ NOTHING ANIMATES AND NOTHING COUNTS DOWN. No rAF loop, no timer, no
     JS-driven transition — so `prefers-reduced-motion` has nothing to
     degrade here, and `motionReduced()` is deliberately not consulted. If a
     later revision animates a counter it must ask INSIDE the tick, not once
     at construction (contract R4, the b2-03 slip).

     ⚠️ THE CAP IS `aria-disabled`, NOT `disabled`, AND THAT IS DELIBERATE.
     NOTES-C4 §5 flag 15 caps coefficients at 4 and the cap is a help; §11
     forbids narrating a control, so nothing on the page says so in words and
     the stepper simply stops at the bound. A real `disabled` attribute would
     make the browser drop focus the instant a keyboard user steps up to 4 —
     the control they are standing on vanishes from the tab order and focus
     falls to the document body. `aria-disabled` dims it, announces it and
     keeps it focusable; the guard below is what makes it inert.

     ⚠️ EVERY EQUATION IS REPAINTED, NOT ONLY THE VISIBLE ONE. The other
     three are `hidden`, and a hidden panel holding numbers from three
     presses ago is a wrong number in the DOM whether or not anyone is
     looking at it — and it becomes visible the moment a tab is pressed, so
     "nobody can see it" is not true either. Four equations of at most four
     terms is nothing to repaint. */

  /* The counters, and the ONLY arithmetic in this block.
     ⚖️ Identical to `_cbal_counts` in `ks3_art/c4.py`, term for term. Nothing
     anywhere prints a count that did not come out of one of the two. */
  function c4Counts(eq, coeffs) {
    var out = [], els = eq.els || [], atoms = eq.atoms || [], i, k;
    for (k = 0; k < els.length; k++) {
      var el = els[k], l = 0, r = 0;
      for (i = 0; i < eq.nl; i++) { l += (atoms[i][el] || 0) * coeffs[i]; }
      for (i = eq.nl; i < atoms.length; i++) { r += (atoms[i][el] || 0) * coeffs[i]; }
      out.push({ el: el, l: l, r: r });
    }
    return out;
  }

  /* Is this vector the target, and if not, what whole multiple of it is it?
     Returns 0 when the vector is not a clean multiple — which `_cbal_assert`
     proves cannot happen for any BALANCED vector in this unit's payload, and
     which is handled anyway rather than trusted. */
  function c4Multiple(target, coeffs) {
    var k = 0, i, ratio;
    for (i = 0; i < target.length; i++) {
      if (coeffs[i] % target[i]) { return 0; }
      ratio = coeffs[i] / target[i];
      if (k && ratio !== k) { return 0; }
      k = ratio;
    }
    return k;
  }

  function c4Same(a, b) {
    var i;
    if (!a || !b || a.length !== b.length) { return false; }
    for (i = 0; i < a.length; i++) { if (a[i] !== b[i]) { return false; } }
    return true;
  }

  /* ── coefficient-balancer (c4-05 #s-balance) ────────────────────────
     Four equations, a `+`/`−` in front of every formula and nothing at all
     attached to a subscript, because which number is theirs IS the lesson.

     ⚖️ `solved` IS THE TARGET AND `balanced` IS THE COUNTS, AND THEY ARE NOT
     THE SAME TEST. Each equation has exactly two balanced states inside the
     cap — its target and the target doubled — and only the target ticks the
     tab. At the doubled state the panel still says "Balanced.", because it
     is, and the note beside it swaps to the one that says it is not in its
     smallest numbers. That is the state Design's own "Going further"
     paragraph marks down, answered where the student made it rather than
     praised now and contradicted four sections later. */
  function wireCoefficientBalancer(sec) {
    var wrap = sec.querySelector("[data-cbal]");
    if (!wrap) { return; }
    var cfg = c3Cfg(wrap);
    var eqs = cfg.eqs || [];
    if (!eqs.length) { return; }
    var floor = Number(cfg.floor || 1);
    var cap = Number(cfg.cap || 4);

    var active = cfg.start || eqs[0].id;
    var coeffs = {}, solved = {}, nSolved = 0;
    each(eqs, function (eq) {
      var v = [], i;
      for (i = 0; i < (eq.target || []).length; i++) { v.push(floor); }
      coeffs[eq.id] = v;
    });

    var tabs = toArray(wrap.querySelectorAll("[data-cbal-tab]"));
    var blocks = {};
    each(wrap.querySelectorAll("[data-cbal-eq]"), function (el) {
      blocks[el.getAttribute("data-cbal-eq")] = el;
    });
    var summaryEl = wrap.querySelector("[data-cbal-summary]");
    var resetBtn = wrap.querySelector("[data-cbal-reset]");

    function paintEq(eq) {
      var block = blocks[eq.id];
      if (!block) { return; }
      var c = coeffs[eq.id];
      var counts = c4Counts(eq, c);
      var balanced = true, i;
      for (i = 0; i < counts.length; i++) {
        if (counts[i].l !== counts[i].r) { balanced = false; }
      }

      /* The coefficients. `data-cbal-lit` is the accent treatment Design
         gives a number that has been moved off 1 — a LIVE VALUE, not a mark. */
      each(block.querySelectorAll("[data-cbal-coeff]"), function (el) {
        var idx = Number(el.getAttribute("data-cbal-coeff"));
        c3Say(el, String(c[idx]));
        el.setAttribute("data-cbal-lit", c[idx] > floor ? "1" : "0");
      });

      /* The bounds, as a property of the control and never as a sentence. */
      each(block.querySelectorAll("[data-cbal-for]"), function (btn) {
        var idx = Number(btn.getAttribute("data-cbal-for"));
        var d = Number(btn.getAttribute("data-cbal-delta"));
        var next = c[idx] + d;
        btn.setAttribute("aria-disabled",
          (next < floor || next > cap) ? "true" : "false");
      });

      each(block.querySelectorAll("[data-cbal-counter]"), function (tile) {
        var el = tile.getAttribute("data-cbal-counter"), found = null, j;
        for (j = 0; j < counts.length; j++) {
          if (counts[j].el === el) { found = counts[j]; }
        }
        if (!found) { return; }
        c3Say(tile.querySelector("[data-cbal-left]"), String(found.l));
        c3Say(tile.querySelector("[data-cbal-right]"), String(found.r));
        tile.setAttribute("data-cbal-match", found.l === found.r ? "1" : "0");
        var want = found.l === found.r ? "matched"
          : (found.l > found.r ? "short_right" : "short_left");
        each(tile.querySelectorAll("[data-cbal-st]"), function (s) {
          setHidden(s, s.getAttribute("data-cbal-st") !== want);
        });
      });

      var panel = block.querySelector("[data-cbal-balanced]");
      setHidden(panel, !balanced);
      if (balanced) {
        var isTarget = c4Same(eq.target, c);
        var multiNote = block.querySelector('[data-cbal-note="multiple"]');
        var kEl = block.querySelector("[data-cbal-k]");
        /* A balanced state that is not the target is a whole multiple of it
           — `_cbal_assert` walks the whole space and refuses to build if any
           equation breaks that. `k` is DERIVED here and is never a literal,
           even though the cap of 4 admits only k = 2 today. */
        var k = isTarget ? 1 : c4Multiple(eq.target, c);
        if (!isTarget && multiNote && k > 1) {
          c3Say(kEl, String(k));
          setHidden(block.querySelector('[data-cbal-note="target"]'), true);
          setHidden(multiNote, false);
        } else {
          setHidden(block.querySelector('[data-cbal-note="target"]'), false);
          setHidden(multiNote, true);
        }
        if (isTarget && !solved[eq.id]) { solved[eq.id] = true; nSolved += 1; }
      }
    }

    function paint() {
      each(eqs, paintEq);
      each(tabs, function (btn) {
        var id = btn.getAttribute("data-cbal-tab");
        btn.setAttribute("aria-pressed", id === active ? "true" : "false");
        setHidden(blocks[id], id !== active);
        setHidden(wrap.querySelector('[data-cbal-tick="' + id + '"]'),
                  !solved[id]);
      });
      setHidden(summaryEl, nSolved < eqs.length);
      /* `markStage` is already a ratchet — never write another one. */
      markStage(sec, nSolved >= eqs.length);
    }

    each(wrap.querySelectorAll("[data-cbal-for]"), function (btn) {
      /* ⚠️ THE BUTTON'S OWN EQUATION, NOT THE ACTIVE ONE. Every equation's
         steppers are bound, and three of the four blocks are hidden at any
         moment — so reading `active` here would be an assumption about which
         block a click came from rather than a fact about the click. Resolved
         from the button's own ancestor, which cannot be wrong. */
      var block = btn.closest ? btn.closest("[data-cbal-eq]") : null;
      var owner = block ? block.getAttribute("data-cbal-eq") : null;
      btn.addEventListener("click", function () {
        /* The `aria-disabled` half of the bound. Nothing is said about it. */
        if (btn.getAttribute("aria-disabled") === "true") { return; }
        var eq = c3By(eqs, owner || active);
        if (!eq || !coeffs[eq.id]) { return; }
        var idx = Number(btn.getAttribute("data-cbal-for"));
        var next = coeffs[eq.id][idx] + Number(btn.getAttribute("data-cbal-delta"));
        if (next < floor || next > cap) { return; }
        coeffs[eq.id][idx] = next;
        paint();
      });
    });

    each(tabs, function (btn) {
      btn.addEventListener("click", function () {
        var id = btn.getAttribute("data-cbal-tab");
        /* THE NO-OP PRESS. Pressing the tab that is already lit changes
           nothing and must therefore DO nothing — a control that claims to
           be pressed and then repaints the screen is what the smoke gate
           asserts against. */
        if (id === active || !blocks[id]) { return; }
        active = id;
        paint();
      });
    });

    if (resetBtn) {
      resetBtn.addEventListener("click", function () {
        var eq = c3By(eqs, active), i;
        if (!eq) { return; }
        for (i = 0; i < coeffs[eq.id].length; i++) { coeffs[eq.id][i] = floor; }
        /* ⚠️ `solved` IS NOT CLEARED. MRB-208: credit is a RATCHET. An
           equation the student has already driven to its target stays
           credited when they set it back to 1 to try it again, and the rail
           never goes backwards. */
        paint();
      });
    }

    paint();
  }

  /* ── forbidden-move (c4-05 #s-forbidden) ────────────────────────────
     ⚖️ THE FORBIDDEN MOVE IS A BUTTON, NOT A WARNING. There is no refusal
     here, no confirm, no red and no interception: the student presses "Add a
     small 2 to the water", the equation balances, and the panel shows them
     that what they have just written says burning hydrogen makes bleach.
     Being allowed to make the move is the whole mechanism (NOTES-C4 §2) — a
     warning dialog would confront the misconception with an assertion
     instead of with the student's own equation.

     ⚖️ AND BOTH MOVES STAY AVAILABLE. Neither button is spent and neither
     disables: the comparison between the small 2 and the big 2 is the point,
     so a student who has seen one must be able to see the other.

     ⚑ `REACT-08` is elicited by `#forbidden-small-2` and confronted by
     `#forbidden-reveal`, both of which are ids the renderer emits by name for
     exactly this join (MRB-244). Renaming either without renaming the
     register entry in the same edit breaks a join that will still LOOK
     resolved in the record. */
  function wireForbiddenMove(sec) {
    var wrap = sec.querySelector("[data-forbid]");
    if (!wrap) { return; }
    var btns = toArray(wrap.querySelectorAll("[data-forbid-move]"));
    if (!btns.length) { return; }
    var reveal = wrap.querySelector("[data-forbid-reveal]");
    var products = toArray(wrap.querySelectorAll("[data-forbid-product]"));
    var texts = toArray(wrap.querySelectorAll("[data-forbid-text]"));

    each(btns, function (btn) {
      btn.addEventListener("click", function () {
        /* THE NO-OP PRESS again: re-pressing the move that is already open
           would move focus to a panel that has not changed. */
        if (btn.getAttribute("aria-pressed") === "true") { return; }
        var v = btn.getAttribute("data-forbid-move");
        each(btns, function (b) {
          b.setAttribute("aria-pressed", b === btn ? "true" : "false");
        });
        each(products, function (p) {
          setHidden(p, p.getAttribute("data-forbid-product") !== v);
        });
        each(texts, function (p) {
          setHidden(p, p.getAttribute("data-forbid-text") !== v);
        });
        setHidden(reveal, false);
        focusReveal(reveal);
        markStage(sec, true);
      });
    });
  }


  //
  // ⚠️⚠️ `data-cbalblock`, NOT `data-balblock`. The build contract §8 assigns
  // this family the prefix `bal`, and `[data-balblock]` is ALREADY BOUND, one
  // dispatch table above, to `wireBalanceBench` for C2's `balance-bench`.
  // Spliced as assigned, this section would be handed to that handler as well
  // as to this one — the `data-critiq` case exactly, which §8 itself cites as
  // the precedent for choosing a prefix that does not collide. `cbal` and
  // `forbid` are both measured free across this file, `shared/ks3.css` and
  // every `ks3_art/*.py`. Reported to the commander, not changed quietly.
  //
  // MRB-210 does not apply: there is no range control in either instrument.
  // Every control here is a real `<button>` and there is no `onclick=`
  // attribute anywhere in the markup.

/* ═══ END C4 wiring ═══ */

/* ═══ BEGIN C5 wiring ═══════════════════════════════════════════════════
   C5's instrument families. Added as ONE marked block so that a lane merging
   into this file resolves mechanically: nothing above this marker moves.
   ═══ */

/* ── from js_01.js ── */
  /* ═══ c5-01 · combustion ═══════════════════════════════════════════════
     Two instruments: `burner-bench` and `fuel-cards`. Both tick a rail stop
     and NOTHING ticks on load (MRB-208) — `markStage` is already a ratchet
     and neither of these writes `data-stage-done` itself.

     ⚖️ NOTHING IS COMPUTED IN THIS BLOCK. Not one number, not one sentence.
     Every state of every panel is already in the document (EMIT-BOTH-SHOW-ONE)
     and these two handlers do exactly one thing: choose which node is
     `hidden`. So an authored `<strong>`, an em dash and a degree sign survive
     as the author wrote them, no sentence exists twice, and the resting render
     cannot disagree with the runtime one.

     ⚖️ NOTHING GREEN AND NOTHING RED REACHES A CONTROL. A pressed dial, a
     pressed prediction and a pressed card option all take the platform's
     ordinary `aria-pressed` treatment; every verdict on this page is a PANEL
     OF WORDS. Only the mastery ladder marks (R3 / MRB-196 R10). There is no
     `data-correct` anywhere in either instrument.

     ⚖️ NOTHING ANIMATES AND NOTHING COUNTS DOWN — no rAF, no timer, no
     JS-driven transition — so `prefers-reduced-motion` has nothing to degrade
     here and no tick has to re-test it. There is no range control in either
     instrument either, so MRB-210's `input`-and-`change` pair has nothing to
     bind to; every control below is a real `<button>` and there is no
     `onclick=` attribute anywhere in the markup.

     ⚠️ THE NO-OP PRESS. Every dial and every prediction option below returns
     early when the value pressed is the value already pressed. Design's own
     handler does not, and pressing a lit dial there re-runs the whole paint —
     which on this bench would re-fire `focusReveal` and drag the page back up
     to a readout the student is already looking at. Corrected here rather than
     reproduced, which is the same correction C3 made across five dials and C4
     across two. */

  /* ── burner-bench (c5-01 #s-burner) ─────────────────────────────────
     Four fuels, two air settings, eight runs — and the stop ticks on the AIR
     dial, because the collar is what the lesson is about. Design's
     `DONE('s-burner')` is `Object.keys(s.seen).length >= 2` and her `seen`
     records air settings only.

     ⚠️ WHICH DIAL THE STOP WATCHES IS READ OFF THE DOM, NOT WRITTEN DOWN
     HERE. The renderer marks that dial's buttons `data-burner-track` and puts
     the number of settings on the wrapper as `data-seen-total`, both from the
     payload. So the claim lives in the lesson record, in one place, and this
     file cannot drift from it.

     ⚠️ TWO DEPARTURES FROM DESIGN'S OWN HANDLER, BOTH DELIBERATE:

     1. THE GATE STAYS ON SCREEN. Her `needPredict` removes it the moment it
        is answered, which takes the student's commitment away at the exact
        moment the readout arrives to be compared against it. Law 4 exists to
        create that comparison. Every gate in C3 and C4 stays put; so does
        this one, and nothing here hides it.

     2. THE CLOSING SUMMARY AND THE TICK WAIT FOR THE PREDICTION TOO. Her
        `sawBoth` is `Object.keys(s.seen).length >= 2` and is independent of
        the gate, so a student who presses both air buttons without ever
        committing gets the summary — "Same fuel, both air settings…" — having
        read no readout at all, and ticks the stop for it. The summary is a
        sentence about what you have just READ, so it waits until there has
        been something to read. That makes the stop's completion signal honest
        rather than a count of presses, which is what MRB-208 is for. */
  function wireBurnerBench(sec) {
    var wrap = sec.querySelector("[data-burner]");
    if (!wrap) { return; }
    var seenTotal = parseInt(wrap.getAttribute("data-seen-total"), 10) || 0;
    var closer = wrap.querySelector("[data-burner-close]");
    var dials = toArray(wrap.querySelectorAll("[data-burner-for]"));
    var predicts = toArray(wrap.querySelectorAll(
      "[data-burner-predict] .ks3-option"));
    var panels = {};
    each(wrap.querySelectorAll("[data-burner-panel]"), function (p) {
      panels[p.getAttribute("data-burner-panel")] = p;
    });
    if (!seenTotal || !dials.length) { return; }

    /* The chosen value of each dial, the dial ORDER, and which dial the stop
       watches — all three read off the resting DOM rather than assumed. The
       renderer lights each dial's first option and emits the dials in the
       payload's own order, and the run key is those values joined, so which
       dial comes first and which value each opens on stay the payload's
       business rather than being written down a second time here. */
    var chosen = {}, order = [], tracked = null;
    each(dials, function (b) {
      var name = b.getAttribute("data-burner-for");
      if (order.indexOf(name) < 0) {
        order.push(name);
        /* Falls back to the dial's first button, so a resting DOM with nothing
           pressed still produces a real key rather than "null:null". */
        chosen[name] = b.getAttribute("data-burner-val");
      }
      if (b.getAttribute("aria-pressed") === "true") {
        chosen[name] = b.getAttribute("data-burner-val");
      }
      if (b.getAttribute("data-burner-track") === "1") { tracked = name; }
    });

    var predicted = false;
    /* Seeded with the setting the bench OPENS on, because that setting has
       genuinely been shown — it is the run the readout gives first. One of two
       is not two, so nothing ticks on load. */
    var seen = {};
    if (tracked && chosen[tracked]) { seen[chosen[tracked]] = true; }

    function key() {
      var parts = [], i;
      for (i = 0; i < order.length; i++) { parts.push(chosen[order[i]]); }
      return parts.join(":");
    }

    function countSeen() {
      var n = 0, x;
      for (x in seen) {
        if (Object.prototype.hasOwnProperty.call(seen, x)) { n += 1; }
      }
      return n;
    }

    function paint() {
      var k = key();
      var name;
      /* One panel visible, and it is this combination's — or none, until the
         student has said what they expect. */
      for (name in panels) {
        if (Object.prototype.hasOwnProperty.call(panels, name)) {
          setHidden(panels[name], name !== k || !predicted);
        }
      }
      if (predicted && countSeen() >= seenTotal) {
        setHidden(closer, false);
        markStage(sec, true);
      }
    }

    each(dials, function (btn) {
      btn.addEventListener("click", function () {
        var name = btn.getAttribute("data-burner-for");
        var val = btn.getAttribute("data-burner-val");
        /* The no-op press. See the block header. */
        if (chosen[name] === val) { return; }
        chosen[name] = val;
        each(dials, function (b) {
          if (b.getAttribute("data-burner-for") !== name) { return; }
          b.setAttribute("aria-pressed",
                         b.getAttribute("data-burner-val") === val
                           ? "true" : "false");
        });
        if (name === tracked) { seen[val] = true; }
        paint();
      });
    });

    each(predicts, function (btn) {
      btn.addEventListener("click", function () {
        if (btn.getAttribute("aria-pressed") === "true") { return; }
        each(predicts, function (p) {
          p.setAttribute("aria-pressed", p === btn ? "true" : "false");
        });
        var first = !predicted;
        predicted = true;
        paint();
        /* MRB-257 (5.43) — only on the press that OPENS the readout. Moving
           focus on every later dial press would drag the page around while the
           student is deliberately comparing two runs. */
        if (first) { focusReveal(panels[key()]); }
      });
    });

    paint();
  }

  /* ── fuel-cards (c5-01 #s-fuels) ────────────────────────────────────
     One commitment per card and it is FINAL — `c3CommitCards`' contract, the
     same one the purity sorter, the jobs list and c4-03's equation cards take.
     The reply is on screen the instant the card is decided, so a second press
     would be a student choosing an answer they can already read; the siblings
     disable and the ones not pressed dim.

     ⚠️ There is no answer key in this markup and none is needed. The reply
     names the products and says why, and it is the same paragraph whichever
     button was pressed; only the ladder marks. There is no head counter here
     either — Design draws none on this section — so no `count`. */
  function wireFuelCards(sec) {
    c3CommitCards(sec, {
      wrap: "[data-fcard]",
      card: "[data-fcard-card]",
      opt: "[data-fcard-opt]",
      reveal: "[data-fcard-reveal]"
    });
  }


/* ── from js_02.js ── */
  /* ═══ c5-02 · tube-run + decomp-sort ═══════════════════════════════════

     ⚖️ NEITHER OF THESE COMPOSES A SENTENCE, A NUMBER OR A COLOUR. Every
     stage sentence, every mass reading, every finished panel and every sort
     verdict is in the document already, rendered by `ks3_art/c5.py`; all the
     code below does is decide which one is on screen. There is no `data-cfg`
     on either family and there is nothing here to parse, so nothing can drift
     between the Python that drew the page and the JavaScript that drives it.

     ⚖️ ONLY THE LADDER MARKS. Nothing green and nothing red reaches any
     control in either instrument. The cooling gate's three options are
     COMMITMENTS: they take the ordinary pressed treatment, they carry no
     correctness flag, and the answer arrives as the next STAGE OF THE RUN.
     The sort's verdict is a panel of WORDS, in the same voice whichever
     button was pressed.

     ⊖ NOTHING ANIMATES, NOTHING COUNTS DOWN and there is no canvas — no rAF,
     no timer, no JS-driven transition — so `prefers-reduced-motion` has
     nothing to degrade here and neither function asks about it. If a later
     revision animates anything it must ask `motionReduced()` INSIDE the tick
     (contract R4). MRB-210's input+change rule has nothing to bind either:
     neither instrument draws a range. */

  /* ── tube-run (c5-02 #s-tube) ────────────────────────────────────────
     Three substances × five stage positions (0 = nothing lit, through 4 =
     the flame is off), plus a commitment between stage 3 and stage 4.

     ⭐ THE COOLING GATE IS THE LESSON, AND IT BLOCKS. `gateNeeded()` is
     Design's own `stage === 3 && gate === null`, and while it is true the
     advance button is HIDDEN. That is the whole difference between a
     prediction and a caption: a student who can press "Let it cool" first has
     watched the answer and been asked about it afterwards. The gate is what
     elicits REACT-13 ("a decomposition reverses when it cools") and stage 4 is
     what confronts it, in the substance's own words.

     ⚖️ CREDIT IS FOR CARRYING ALL THREE SUBSTANCES TO THE END, which is
     Design's own `DONE()` (`Object.keys(s.done).length >= 3`). `done` is never
     emptied — not by "Fresh tube", not by switching substance — so a student
     can run a finished tube again to look at it without losing the stop.
     `markStage` is the ratchet and this file does not write its own.

     ⚠️ THE RUN RESETS WHEN THE SUBSTANCE CHANGES, and the commitment goes with
     it. A different substance is a different run — the limestone one takes far
     more heat than the copper one and says so — so carrying a stage across
     would leave the tiles reading one substance's mass over another's stages.
     Design's own tab handler does exactly this (`{ sub: k, stage: 0, gate:
     null }`).

     ⚠️ THE NO-OP PRESS. The dial returns early when the substance pressed is
     the substance already loaded. Design's handler does not: pressing the
     loaded tab again resets the run to stage 0 and discards the commitment,
     which is a control claiming to be pressed and then undoing the student's
     work. Corrected here rather than reproduced.

     ⚠️ THE WHOLE STATE SPACE, enumerated rather than sampled: 3 substances ×
     5 stage positions = 15 views, each with its own open stages, its own mass
     reading and its own heat reading; the gate is open in exactly three of
     those fifteen (stage 3, before an option is pressed); the advance button
     is hidden in six of them (stage 4 for each substance, and stage 3 with the
     gate open); the finished panel is on screen in three; the all-three panel
     depends on `done` rather than on the view and so crosses all fifteen; and
     the resting state — first substance, stage 0, nothing committed, nothing
     done, `data-stage-done="0"` — is the sixteenth thing that has to be right
     and is the one a page is in before anybody touches it. */
  function wireTubeRun(sec) {
    var wrap = sec.querySelector("[data-tuber]");
    if (!wrap) { return; }
    var tabs = toArray(wrap.querySelectorAll("[data-tuber-tab]"));
    if (!tabs.length) { return; }

    var total = parseInt(wrap.getAttribute("data-total"), 10) || tabs.length;
    var marks = toArray(wrap.querySelectorAll("[data-tuber-tabdone]"));
    var intros = toArray(wrap.querySelectorAll("[data-tuber-intro]"));
    var rows = toArray(wrap.querySelectorAll("[data-tuber-stage]"));
    var says = toArray(wrap.querySelectorAll("[data-tuber-text]"));
    var gate = wrap.querySelector("[data-tuber-gate]");
    var gateOpts = toArray(wrap.querySelectorAll("[data-tuber-gateopt]"));
    var masses = toArray(wrap.querySelectorAll("[data-tuber-mass]"));
    var limes = toArray(wrap.querySelectorAll("[data-tuber-lime]"));
    var heats = toArray(wrap.querySelectorAll("[data-tuber-heat]"));
    var next = wrap.querySelector("[data-tuber-next]");
    var nextLabels = toArray(wrap.querySelectorAll("[data-tuber-nextlabel]"));
    var reset = wrap.querySelector("[data-tuber-reset]");
    var panels = toArray(wrap.querySelectorAll("[data-tuber-done]"));
    var all = wrap.querySelector("[data-tuber-all]");

    /* The last stage index, and the number of moves, are read off the MARKUP
       rather than assumed to be four. The renderer decides how many stages
       there are and two places deciding that is two places to change it. */
    var moves = rows.length;
    var lastLabel = nextLabels.length ? nextLabels.length - 1 : 0;

    /* And so is the opening substance: the renderer decides which tab is
       pressed at rest. */
    var sub = tabs[0].getAttribute("data-tuber-tab");
    each(tabs, function (b) {
      if (b.getAttribute("aria-pressed") === "true") {
        sub = b.getAttribute("data-tuber-tab");
      }
    });
    var stage = 0, commit = null, done = {}, nDone = 0;

    function gateNeeded() { return stage === moves - 1 && commit === null; }

    function clearGate() {
      each(gateOpts, function (b) { b.setAttribute("aria-pressed", "false"); });
    }

    function paint() {
      var needed = gateNeeded();
      var over = stage >= moves;

      each(tabs, function (b) {
        b.setAttribute("aria-pressed",
          b.getAttribute("data-tuber-tab") === sub ? "true" : "false");
      });
      each(marks, function (s) {
        setHidden(s, !done[s.getAttribute("data-tuber-tabdone")]);
      });
      each(intros, function (p) {
        setHidden(p, p.getAttribute("data-tuber-intro") !== sub);
      });
      /* `data-open` is the stage the student has watched; `data-current` is
         the one the next press will open. Both are attributes the stylesheet
         reads, so no ground and no border is decided here. */
      each(rows, function (li) {
        var i = parseInt(li.getAttribute("data-tuber-stage"), 10);
        li.setAttribute("data-open", i < stage ? "1" : "0");
        li.setAttribute("data-current", i === stage ? "1" : "0");
      });
      each(says, function (p) {
        var k = p.getAttribute("data-tuber-text").split("|");
        setHidden(p, !(k[0] === sub && parseInt(k[1], 10) < stage));
      });
      setHidden(gate, !needed);
      /* The mass tile flips on the LAST press and not before: the gas has not
         left until the run is over, so a tube that is still being heated still
         reads its opening mass. */
      each(masses, function (s) {
        var k = s.getAttribute("data-tuber-mass").split("|");
        setHidden(s, !(k[0] === sub && k[1] === (over ? "1" : "0")));
      });
      each(limes, function (s) {
        setHidden(s, s.getAttribute("data-tuber-lime") !==
          (stage >= moves - 1 ? "1" : "0"));
      });
      /* Three heat states, keyed to WHICH part of the run is live rather than
         to how many presses have happened: nothing lit, the flame on, the
         flame off. */
      each(heats, function (s) {
        var want = stage === 0 ? "0" : (over ? "2" : "1");
        setHidden(s, s.getAttribute("data-tuber-heat") !== want);
      });
      if (next) {
        setHidden(next, over || needed);
        var lab = String(stage < lastLabel ? stage : lastLabel);
        each(nextLabels, function (s) {
          setHidden(s, s.getAttribute("data-tuber-nextlabel") !== lab);
        });
      }
      each(panels, function (d) {
        setHidden(d, !(over && d.getAttribute("data-tuber-done") === sub));
      });
      setHidden(all, nDone < total);
      markStage(sec, nDone >= total);
    }

    each(tabs, function (btn) {
      btn.addEventListener("click", function () {
        var v = btn.getAttribute("data-tuber-tab");
        if (v === sub) { return; }       /* the no-op press */
        sub = v;
        stage = 0;
        commit = null;
        clearGate();
        paint();
      });
    });

    each(gateOpts, function (btn) {
      btn.addEventListener("click", function () {
        each(gateOpts, function (x) {
          x.setAttribute("aria-pressed", x === btn ? "true" : "false");
        });
        if (commit !== null) { return; }
        commit = parseInt(btn.getAttribute("data-tuber-gateopt"), 10);
        paint();
        focusReveal(next);               /* MRB-257 (5.43) */
      });
    });

    if (next) {
      next.addEventListener("click", function () {
        if (stage >= moves || gateNeeded()) { return; }
        stage += 1;
        if (stage >= moves && !done[sub]) { done[sub] = true; nDone += 1; }
        paint();
        if (stage >= moves) {
          var open = null;
          each(panels, function (d) {
            if (!d.hasAttribute("hidden")) { open = d; }
          });
          focusReveal(nDone >= total && all ? all : open);
        }
      });
    }

    if (reset) {
      reset.addEventListener("click", function () {
        if (stage === 0 && commit === null) { return; }
        stage = 0;
        commit = null;
        clearGate();
        /* `done` survives, deliberately: a substance already carried to the
           end has been carried to the end, and running it again to watch it
           is not undoing that. */
        paint();
      });
    }

    paint();
  }

  /* ── decomp-sort (c5-02 #s-sort) ─────────────────────────────────────
     Five changes, one question asked five times, and heat is in all five so
     looking for a flame settles none of them.

     `c3CommitCards` is the contract — one commitment per item, final, with
     both buttons disabling and the answer on screen the instant it is decided
     — and this family shares that body rather than keeping a fourth copy of
     it. There is no `correct` key in the payload and nothing here looks for
     one: the reveal names the reaction type and explains it, in the same tone
     whichever button was pressed.

     No `close` and no `count`: Design draws neither a closing panel nor a head
     counter on this block. The rail stop ticks when the fifth item is decided,
     which `c3CommitCards` does against `data-total`. */
  function wireDecompSort(sec) {
    c3CommitCards(sec, {
      wrap: "[data-dcomp]", card: "[data-dcomp-item]",
      opt: "[data-dcomp-opt]", reveal: "[data-dcomp-reveal]"
    });
  }


//
// Order between the two does not matter — neither reads the other's DOM and
// neither broadcasts. Both belong in a new "═══ BEGIN C5 wiring ═══" group.
//
// ⚠️ `data-dcompblock`, NOT `data-dsortblock`. `ks3_art/b5.py` already
// registers `disperse-sort` with the shell class `ks3-dsort-block`; the marker
// attribute was free, but keeping a `dsort` prefix on one half of the pair and
// a `dcomp` class on the other is exactly the `data-critique` /
// `data-critiq` trap read backwards. One prefix, used everywhere. See the
// registration note at the foot of `art_02.py`.


/* ── from js_03.js ── */
  /* ── control-tubes (c5-03 #s-rust) ──────────────────────────────────
     Four tubes, four commitments, and ONE summary that opens only when all
     four are decided.

     ⚖️ THE GATE IS THE LESSON, AND IT IS `c3CommitCards`' `close` SLOT.
     Every other instrument that uses this helper opens a closer when the
     last card is decided as a convenience; here it is the argument. "Both
     oxygen and water are needed" is a conclusion no three of these tubes
     can support, so the panel that states it is not on screen until the
     fourth is opened — and the rail stop ticks at the same moment, which
     is Design's own `DONE('s-rust')` (`Object.keys(s.preds).length >=
     TUBES.length`).

     ⚖️ AND IT IS THE HELPER, NOT A COPY OF IT. Everything this family
     needs — one final commitment per card, both buttons disabled, the
     unpressed one dimmed, a reveal shown, a closer at the end and
     `markStage` at the same point — is already `c3CommitCards`' contract,
     the same one the purity sorter, the jobs list, the plan critique and
     c4-03's equation-read all take. A second implementation of it here
     would be four more places for the ratchet to be got wrong.

     ⚠️ NOTHING IS RECOMPUTED AND NO SENTENCE IS COMPOSED HERE. Every
     tube's result and reason, the whole summary and its drawn arrow are
     authored markup emitted by `ks3_art.c5` and shown — emit-both-show-one
     at the card level. There is no `data-cfg` on this family because there
     is nothing to recompute: no number, no colour, no geometry.

     ⚠️ AND NOTHING HERE MARKS (R3). A tube predicted wrong looks exactly
     like a tube predicted right: same pressed treatment, same ink panel,
     same two sentences. The correction, where there is one, is the result
     itself.

     ⊖ NO COUNTER. Design draws no readout on this block's head row, so
     `count` is deliberately absent — `setCount` would look for a
     `[data-count]` the shell was never asked to emit. */
  function wireControlTubes(sec) {
    c3CommitCards(sec, {
      wrap: "[data-ctube]",
      card: "[data-ctube-card]",
      opt: "[data-ctube-opt]",
      reveal: "[data-ctube-open]",
      close: "[data-ctube-summary]"
    });
  }

  /* ── rust-stop (c5-03 #s-stop) ──────────────────────────────────────
     Five real objects, one classification each, and the fifth does not fit
     the rule the student has just been given. The commitment is FINAL and
     the answer is on screen the instant the card is decided, so a second
     press would be a student choosing an answer they can already read.

     ⊖ NO `close` HERE, and that is the difference from the tubes above:
     these five are independent findings and there is no reading of them
     together to gate. The rail stop still ticks on the fifth, which is
     Design's `DONE('s-stop')`.

     ⚠️ There is no answer key in this markup and none is needed. The
     paragraph that opens is the same paragraph whichever button was
     pressed, and it names the kind rather than the press. */
  function wireRustStop(sec) {
    c3CommitCards(sec, {
      wrap: "[data-rstop]",
      card: "[data-rstop-card]",
      opt: "[data-rstop-opt]",
      reveal: "[data-rstop-answer]"
    });
  }


/* ── from js_04.js ── */
  /* ═══ c5-04 · displacement ═════════════════════════════════════════════
     Two instruments: `reactivity-grid` and `reactivity-use`. Both tick a rail
     stop and NOTHING ticks on load (MRB-208) — the build emits
     `data-stage-done="0"` and `markStage` is already a ratchet, so neither
     handler writes the attribute itself and neither can take back a stop that
     has been earned.

     ⚖️ NOT ONE SENTENCE IS COMPOSED IN THIS BLOCK. All sixteen cell panels,
     all sixteen verdicts, the six equations and the four paragraphs of the
     payoff are authored markup, already in the document, and these handlers do
     exactly one thing: choose which node is `hidden`. So `<strong>`, the em
     dashes and the degree of every observation survive as the author wrote
     them, no sentence exists twice in two languages, and the resting render
     cannot disagree with the runtime one.

     ⚖️ NOTHING GREEN AND NOTHING RED REACHES A CONTROL. A pressed cell and a
     pressed prediction take the platform's ordinary `aria-pressed` treatment.
     A run cell is painted by what the TUBE did, not by whether the student
     guessed it: `data-rgrid-state` becomes `reacts` or `none`, which are
     Design's two grounds, and nothing here ever compares the prediction with
     the outcome. Only the mastery ladder marks. */

  /* ── reactivity-grid (c5-04 #s-grid) ─────────────────────────────────
     Sixteen cells, one panel, one predict row.

     ⚖️ THE DOM IS THE STATE, at the panel level: every cell's setup line and
     every cell's result are in the document and one of each is shown, so a
     cell that has been run is still run when the student comes back to it and
     there is nothing to re-render. What this closure keeps is the one thing
     that cannot be read off the markup — WHICH PREDICTION was pressed on each
     cell, so that returning to it shows the choice still made.

     ⊖ Design's prototype HIDES the predict row on a cell that has been run
     (`needPredict: !ran`) and hard-codes `pressed: false` on both buttons, so
     a commitment leaves no trace at all. On a grid whose whole shape is
     "come back to a cell" that throws away the one thing the student put in.
     The row stays instead, both buttons disabled and the chosen one still
     pressed — which is what `c3CommitCards` does on every other commit-once
     control in the key stage, and what MRB-257 3.21 ruled `--ks3-dim-spent`
     for. Reported to the commander. */

  function wireReactivityGrid(sec) {
    var wrap = sec.querySelector("[data-rgrid]");
    if (!wrap) { return; }

    var cells = toArray(wrap.querySelectorAll("[data-rgrid-cell]"));
    if (!cells.length) { return; }
    var opts = toArray(wrap.querySelectorAll("[data-rgrid-opt]"));
    var pattern = wrap.querySelector("[data-rgrid-pattern]");
    var cfg = c3Cfg(wrap);
    var doneAt = parseInt(cfg.doneAt, 10);
    if (isNaN(doneAt) || doneAt < 1) { doneAt = cells.length; }

    /* key -> the option id pressed on that cell. Runtime state, never text. */
    var ran = {};
    var current = null;

    function only(root, attr, key) {
      each(root.querySelectorAll("[" + attr + "]"), function (el) {
        setHidden(el, el.getAttribute(attr) !== key);
      });
    }

    function tally() {
      var n = 0, k;
      for (k in ran) {
        if (Object.prototype.hasOwnProperty.call(ran, k)) { n += 1; }
      }
      return n;
    }

    function byKey(key) {
      var found = null;
      each(cells, function (b) {
        if (b.getAttribute("data-rgrid-cell") === key) { found = b; }
      });
      return found;
    }

    /* Show one cell: its setup line, its result if it has been run, and the
       predict row in the state that cell left it in. */
    function select(key) {
      current = key;
      each(cells, function (b) {
        b.setAttribute("aria-pressed",
          b.getAttribute("data-rgrid-cell") === key ? "true" : "false");
      });
      only(wrap, "data-rgrid-setup", key);
      /* A key no result carries hides all sixteen, which is exactly what an
         un-run cell wants. */
      only(wrap, "data-rgrid-result", ran[key] ? key : null);
      var chosen = ran[key] || null;
      each(opts, function (b) {
        b.setAttribute("aria-pressed",
          chosen && b.getAttribute("data-rgrid-opt") === chosen
            ? "true" : "false");
        c3Enable(b, !chosen);
      });
    }

    /* Run the selected cell. The prediction gates the reveal (Law 4) and is
       compared with nothing: both buttons open the same panel. */
    function run(key, choice) {
      if (!key || ran[key]) { return; }
      ran[key] = choice;
      var cell = byKey(key);
      if (cell) {
        var outcome = cell.getAttribute("data-rgrid-outcome");
        cell.setAttribute("data-rgrid-state", outcome);
        only(cell, "data-rgrid-mark", outcome);
        only(cell, "data-rgrid-say", outcome);
      }
      select(key);
      var n = tally();
      setCount(sec, n);
      if (n >= doneAt) {
        setHidden(pattern, false);
        markStage(sec, true);
      }
    }

    each(cells, function (b) {
      b.addEventListener("click", function () {
        var key = b.getAttribute("data-rgrid-cell");
        /* THE NO-OP PRESS. Pressing the cell that is already open changes
           nothing on screen, so it does nothing here either — a control that
           claims to be pressed and then repaints the same panel is what the
           smoke gate asserts against. */
        if (key === current) { return; }
        select(key);
      });
    });

    each(opts, function (b) {
      b.addEventListener("click", function () {
        /* The guard is here as well as on the element: `disabled` is the drawn
           half, and this is the half a synthetic click cannot pass. */
        if (!current || ran[current]) { return; }
        run(current, b.getAttribute("data-rgrid-opt"));
      });
    });

    /* Open on the cell the BUILD opened on, read off the markup rather than
       named again here — the resting DOM is the single statement of it. */
    each(cells, function (b) {
      if (b.getAttribute("aria-pressed") === "true") {
        current = b.getAttribute("data-rgrid-cell");
      }
    });
    if (!current) { current = cells[0].getAttribute("data-rgrid-cell"); }
    select(current);
    setCount(sec, 0);
  }

  /* ── reactivity-use (c5-04 #s-uses) ──────────────────────────────────
     Three consequence cards, one commitment each and it is FINAL: the answer
     is on screen the instant the card is decided, so a second press would be a
     student choosing something they can already read.

     ⚠️ There is no answer key in this markup and none is needed. The answer
     paragraph names the verdict itself, in the same box and the same voice
     whichever button was pressed — only the ladder marks. */
  function wireReactivityUse(sec) {
    c3CommitCards(sec, {
      wrap: "[data-ruse]",
      card: "[data-ruse-card]",
      opt: "[data-ruse-opt]",
      reveal: "[data-ruse-answer]"
    });
  }


/* ── from js_05.js ── */
  /* ═══ c5-05 · type-sorter + rule-write ═══════════════════════════════
     The unit's assessment in disguise. Eight reactions with the same five
     buttons under every one, then the student writing the rule themselves.
     Nothing here marks: no option takes green, red, a tick or a cross, and
     the answer panel opens in the same voice whichever button was pressed. */

  /* ── type-sorter (c5-05 #s-sort) ─────────────────────────────────────
     Eight independent commitments, one shared five-way list. This is
     `c3CommitCards`' contract exactly — one commitment per card, final,
     with the answer on screen the instant the card is decided, so a second
     press would be a student choosing something they can already read — so
     it shares that body rather than growing yet another copy of the same
     rule.

     ⚠️ `count: true`. Design DOES draw a head tally on this block ("0 of 8
     named", right-aligned and mono in the head row), unlike c4-01's pairs,
     so the counter is wired as well as drawn. The denominator is asserted
     against the number of reactions at build time — see `r_type_sorter` —
     because `setCount` clamps to `data-total` and a wrong denominator would
     freeze the readout while a card was still undecided.

     ⚠️ NOTHING HERE LOOKS FOR AN ANSWER. There is no `correct` key in the
     payload and no `data-correct` in the markup: the reaction's type is
     read at BUILD time, to guard the chemistry, and reaches the document
     only as the sentence in the reveal. The close panel opens on the eighth
     commitment and `c3CommitCards` calls `markStage` with it. */
  function wireTypeSorter(sec) {
    c3CommitCards(sec, {
      wrap: "[data-tsort]", card: "[data-tsort-card]",
      opt: "[data-tsort-opt]", reveal: "[data-tsort-reveal]",
      close: "[data-tsort-close]",
      count: true
    });
  }

  /* ── rule-write (c5-05 #s-rule) ──────────────────────────────────────
     Write the four rules, then read four to compare with. The one activity
     on the page that nothing marks, which is the point of it: a CLASSIFY
     lesson ends with the rule in the student's own words.

     ⚖️ THE SIXTY-CHARACTER UNLOCK, AND IT IS THE ENGINE'S OWN NUMBER.
     `wireSelf` gates the mastery ladder's self-marked rungs at 60 characters
     (Mide's ruling, 19 Aug 2026 — R8's missing half), and this block is the
     same bargain in a different place: a model answer that arrives before a
     word has been written IS the answer. Sixty is about a dozen words —
     enough to be an attempt at a sentence, low enough that a terse but
     genuine answer gets through. NOTHING HERE READS WHAT WAS WRITTEN: no
     keywords, no parsing, no judgement of any kind. It is the commitment
     that is required, not the correctness.

     ⚠️ §8.10 — NO COPY, deliberately. No "write at least 60 characters", no
     character counter, no nag. The control is simply not active yet and
     looks the way an inactive control looks; the empty box directly above it
     is the explanation.

     ⚠️ THE BUTTON SHIPS `disabled` IN THE HTML, so it is never briefly live
     in the window while this 800 KB deferred file is still arriving. The
     first thing below re-runs the gate anyway, because a browser that
     restored a prefilled textarea on a back-navigation would otherwise leave
     a real answer sitting behind a dead control.

     ⚖️ THE GATE IS SPENT ONCE THE PANEL HAS OPENED, and the control goes
     with it. Design's own handler sets `ruleShown: true` and offers no way
     back — the comparison stays on screen — so a button that stayed live
     would be a control that does nothing, and one that re-armed on an edit
     would be a control that reopens what is already open. It dims to the
     measured spent treatment instead, under the panel it produced.

     ⚠️ FOCUS MOVES BEFORE THE BUTTON DIES. Disabling the control a keyboard
     user just pressed drops them to `<body>`; `focusReveal` takes them to
     the panel first, which is what it exists for (MRB-257 5.43). The order
     of the three lines below is load-bearing. */
  function wireRuleWrite(sec) {
    var wrap = sec.querySelector("[data-rwrite]");
    if (!wrap) { return; }
    var field = wrap.querySelector("[data-rwrite-field]");
    var btn = wrap.querySelector("[data-rwrite-show]");
    var reveal = wrap.querySelector("[data-rwrite-reveal]");
    if (!field || !btn || !reveal) { return; }

    var MIN_COMMIT = 60;
    var shown = false;

    function gate() {
      if (shown) { return; }
      c3Enable(btn, (field.value || "").trim().length >= MIN_COMMIT);
    }

    /* MRB-210 — both events. `input` is what fires while a student types;
       `change` is what fires when a value arrives without typing, which is
       how a restored form and a paste from the context menu both land. */
    field.addEventListener("input", gate);
    field.addEventListener("change", gate);

    btn.addEventListener("click", function () {
      if (shown) { return; }
      shown = true;
      setHidden(reveal, false);
      btn.setAttribute("aria-expanded", "true");
      focusReveal(reveal);
      c3Enable(btn, false);
      markStage(sec, true);
    });

    gate();
  }

/* ═══ END C5 wiring ═══ */

/* ═══ BEGIN C7 wiring ═══════════════════════════════════════════════════
   C7's instrument families — *Energy changes in reactions*. Added as ONE
   marked block so that a lane merging into this file resolves mechanically:
   nothing above this marker moves.

   Six families, and three of them are `c3CommitCards` with three sets of
   hooks. That is deliberate: what must not drift between a plan critique, an
   eight-item sorter and a three-card judgement block is exactly the rule
   `c3CommitCards` owns — one final commitment per card, both buttons
   disabling, the reveal on screen the instant the card is decided, and
   `markStage` at the point the last card closes.

   ⚖️ NOTHING IS COMPUTED IN THIS BLOCK. Not one number, not one sentence.
   Every state of every panel is already in the document (EMIT-BOTH-SHOW-ONE)
   and these handlers do exactly one thing: choose which node is `hidden`. So
   an authored `<strong>`, an em dash and a degree sign survive as the author
   wrote them, no sentence exists twice, and the resting render cannot
   disagree with the runtime one. C7 leans on this harder than any unit so
   far — the heating curve alone carries eighteen readout states.

   ⚖️ NOTHING GREEN AND NOTHING RED REACHES A CONTROL. A pressed dial, a
   pressed prediction and a pressed card option all take the platform's
   ordinary `aria-pressed` treatment; every verdict in this unit is a PANEL OF
   WORDS. Only the mastery ladder marks (R3 / MRB-196 R10). There is no
   `data-correct` anywhere in any of the six.

   ⚖️ NOTHING ANIMATES AND NOTHING COUNTS DOWN — no rAF, no timer, no
   JS-driven transition — so `prefers-reduced-motion` has nothing to degrade
   here. There is no range control either, so MRB-210's `input`-and-`change`
   pair has nothing to bind to; every control below is a real `<button>` and
   there is no `onclick=` attribute anywhere in the markup.

   ⚠️ THE NO-OP PRESS. Every dial and every tab below returns early when the
   value pressed is the value already pressed. Design's own handlers do not,
   and pressing a lit dial there re-runs the whole paint — which on these two
   benches would re-fire `focusReveal` and drag the page back to a readout the
   student is already looking at. Corrected here rather than reproduced, which
   is the same correction C3 made across five dials, C4 across two and C5
   across the burner bench.
   ═══ */

  /* ── heating-curve (c7-01 #s-curve) ──────────────────────────────────
     One control, one thing it does, and eighteen taps. The eight consecutive
     readings at 100 °C are not a defect: NOTES-C7 §2 says the two flat steps
     "have to be experienced as *waiting*, which a static graph cannot do".

     ⚖️ THE STOP TICKS AT THE END OF THE RUN. Design's `DONE('s-curve')` is
     `s.minute >= 11` on a thirteen-point curve — one short of the end, which
     is an off-by-one in her own code rather than a rule: her closing panel
     opens on `seenEnd`, which is `minute >= CURVE.length - 1`. Both are the
     same moment here, at the last point, so the panel and the tick arrive
     together and the rail records what the student actually finished.

     ⚖️ AND CREDIT IS A RATCHET (MRB-208). `Start again` resets the readout to
     minute zero so the run can be watched again; it does NOT untick the stop
     and it does not re-hide the closing panel. A run already carried to the
     end has been carried to the end.

     ⚠️ THE BUTTON'S TWO LABELS ARE BOTH IN THE DOCUMENT. Swapping "Heat for
     one more minute" for "Run complete" is a choice between two authored
     spans, never a string built here. */
  function wireHeatingCurve(sec) {
    var wrap = sec.querySelector("[data-hcurve]");
    if (!wrap) { return; }
    var total = parseInt(wrap.getAttribute("data-total"), 10) || 0;
    var points = toArray(wrap.querySelectorAll("[data-hcurve-point]"));
    var bars = toArray(wrap.querySelectorAll("[data-hcurve-bar]"));
    var step = wrap.querySelector("[data-hcurve-step]");
    var reset = wrap.querySelector("[data-hcurve-reset]");
    var stepLabel = wrap.querySelector("[data-hcurve-steplabel]");
    var endLabel = wrap.querySelector("[data-hcurve-endlabel]");
    var closer = wrap.querySelector("[data-hcurve-close]");
    if (!total || !points.length || !step) { return; }

    var minute = 0;
    var last = total - 1;
    var reachedEnd = false;

    function paint() {
      each(points, function (p) {
        setHidden(p, parseInt(p.getAttribute("data-hcurve-point"), 10)
                     !== minute);
      });
      each(bars, function (b) {
        var i = parseInt(b.getAttribute("data-hcurve-bar"), 10);
        if (i <= minute) { b.className = "ks3-hcurve-bar is-lit"; }
        else { b.className = "ks3-hcurve-bar"; }
      });
      var done = minute >= last;
      setHidden(stepLabel, done);
      setHidden(endLabel, !done);
      c3Enable(step, !done);
    }

    step.addEventListener("click", function () {
      if (minute >= last) { return; }
      minute += 1;
      paint();
      if (minute >= last && !reachedEnd) {
        reachedEnd = true;
        setHidden(closer, false);
        markStage(sec, true);
        focusReveal(closer);
      }
    });

    if (reset) {
      reset.addEventListener("click", function () {
        if (minute === 0) { return; }
        minute = 0;
        /* `reachedEnd`, the closing panel and the tick all survive. See the
           block comment: credit is a ratchet. */
        paint();
      });
    }

    paint();
  }

  /* ── temp-bench (c7-02 #s-bench) ─────────────────────────────────────
     Five beakers, one thermometer, and a prediction in front of every
     reading.

     ⚖️ THE GATE STAYS ON SCREEN AFTER IT IS ANSWERED. Design's `needPredict`
     removes it, which takes the student's own commitment off the page at the
     exact moment the reading arrives to be compared against it — the
     comparison Law 4 exists to create. Every gate in C3, C4 and C5 stays put
     and so does this one; the buttons disable instead, so the commitment is
     still readable and no longer changeable.

     ⚖️ EACH BEAKER IS RUN INDEPENDENTLY AND THE DOM IS THE STATE. All five
     cards are in the document; switching tabs shows a card exactly as it was
     left, so nothing has to be remembered here.

     ⚖️ THE STOP TICKS ON THE FIFTH RUN, which is Design's own
     `DONE('s-bench')`. The closing panel says "Four went up. One went down."
     — a claim no four of these beakers can support — so it opens at the same
     moment. */
  function wireTempBench(sec) {
    var wrap = sec.querySelector("[data-tempb]");
    if (!wrap) { return; }
    var total = parseInt(wrap.getAttribute("data-total"), 10) || 0;
    var tabs = toArray(wrap.querySelectorAll("[data-tempb-tab]"));
    var cards = toArray(wrap.querySelectorAll("[data-tempb-card]"));
    var closer = wrap.querySelector("[data-tempb-close]");
    if (!total || !cards.length) { return; }

    var pick = cards[0].getAttribute("data-tempb-card");
    var ran = 0;

    function show(id) {
      each(tabs, function (b) {
        b.setAttribute("aria-pressed",
          b.getAttribute("data-tempb-tab") === id ? "true" : "false");
      });
      each(cards, function (c) {
        setHidden(c, c.getAttribute("data-tempb-card") !== id);
      });
    }

    each(tabs, function (btn) {
      btn.addEventListener("click", function () {
        var id = btn.getAttribute("data-tempb-tab");
        if (id === pick) { return; }          /* the no-op press */
        pick = id;
        show(id);
      });
    });

    each(cards, function (card) {
      var opts = toArray(card.querySelectorAll("[data-tempb-predict]"));
      var run = card.querySelector("[data-tempb-run]");
      each(opts, function (btn) {
        btn.addEventListener("click", function () {
          if (card.getAttribute("data-open") === "1") { return; }
          card.setAttribute("data-open", "1");
          each(opts, function (b) {
            b.setAttribute("aria-pressed", b === btn ? "true" : "false");
            c3Enable(b, false);
          });
          setHidden(run, false);
          focusReveal(run);
          ran += 1;
          setCount(sec, ran);
          if (ran >= total) {
            setHidden(closer, false);
            markStage(sec, true);
          }
        });
      });
    });

    show(pick);
    setCount(sec, 0);
  }

  /* ── energy-sorter (c7-03 #s-compare) ────────────────────────────────
     Eight changes, one question asked eight times, and three reversal pairs
     separated on purpose so a student commits to melting before freezing
     arrives to contradict them.

     `c3CommitCards` is the contract and this family shares that body rather
     than keeping another copy of it. The `close` slot is the argument, not a
     convenience: "run a change backwards and the energy runs backwards with
     it" is a rule no seven of these cards can support, so the panel that
     states it is not on screen until the eighth is decided — and the rail
     stop ticks at the same moment, which is Design's own
     `DONE('s-compare')`. */
  function wireEnergySorter(sec) {
    c3CommitCards(sec, {
      wrap: "[data-esort]",
      card: "[data-esort-item]",
      opt: "[data-esort-opt]",
      reveal: "[data-esort-reveal]",
      close: "[data-esort-close]",
      count: true
    });
  }

  /* ── energy-uses (c7-01, c7-02, c7-03 #s-uses) ───────────────────────
     ONE FAMILY, PLACED THREE TIMES. Design draws the same three-card
     judgement block on the first three pages of the unit, so it is one
     instrument used three times rather than three that look alike.

     ⊖ NO `close`. Design draws no closing panel on any of the three: the
     three cards are independent judgements and there is no reading of them
     together to gate. The rail stop still ticks on the third, which is her
     `DONE('s-uses')`.

     ⚠️ There is no answer key in this markup and none is needed. The
     paragraph that opens is the same paragraph whichever button was pressed,
     and it argues rather than adjudicating. */
  function wireEnergyUses(sec) {
    c3CommitCards(sec, {
      wrap: "[data-euse]",
      card: "[data-euse-card]",
      opt: "[data-euse-opt]",
      reveal: "[data-euse-reveal]",
      count: true
    });
  }

  /* ── rig-plan-critique (c7-04 #s-plan) ───────────────────────────────
     Five judgements on somebody else's method, and it comes BEFORE the rig:
     ruling on a plan that is not yours is what makes building one a decision
     instead of a recipe.

     ⚠️ `data-rplan`, NOT `data-critiq` or `data-critique`. Both are taken —
     `wirePlanCritique` above claims the first for c3-07 and `wireCritique`
     claims the second for a B-unit family — and a shared selector would hand
     this instrument to another one's handler, after which neither works. */
  function wireRigPlanCritique(sec) {
    c3CommitCards(sec, {
      wrap: "[data-rplan]",
      card: "[data-rplan-step]",
      opt: "[data-rplan-opt]",
      reveal: "[data-rplan-reveal]",
      count: true
    });
  }

  /* ── rig-builder (c7-04 #s-bench) ────────────────────────────────────
     Three dials, eight rigs, and a true value the student never reaches.

     ⚖️ THE RUN BUTTON IS A GATE, NOT A DIAL. Changing a dial hides the
     reading and puts the button back, because a reading left on screen under
     a changed label is the last rig's number wearing this rig's title. That
     is the same defect `r_rig_builder` refuses at build time for a MISSING
     combination, and it is reachable at run time for an unrun one.

     ⚖️ THE STOP TICKS AT THREE RIGS, which is Design's own
     `DONE('s-bench')` (`Object.keys(s.ran).length >= 3`). Three is enough to
     have compared arrangements; requiring all eight would make the stop a
     completionist errand rather than a record of the comparison.

     ⚖️ AND THE PAYOFF PANEL OPENS ONLY ON THE BEST RIG, whichever order it is
     found in. It says "you found the best rig — and it still reads low",
     which is a sentence that is only true standing on that rig. `data-best`
     carries the key from the payload, so the panel and the arithmetic in it
     cannot point at different rigs.

     ⚖️ RUNS ARE COUNTED ONCE EACH. A rig re-run is not a second run: the
     panel records it, and the tick is about how many arrangements were
     compared. */
  function wireRigBuilder(sec) {
    var wrap = sec.querySelector("[data-rigb]");
    if (!wrap) { return; }
    var dials = toArray(wrap.querySelectorAll("[data-rigb-for]"));
    var titles = toArray(wrap.querySelectorAll("[data-rigb-title]"));
    var panels = toArray(wrap.querySelectorAll("[data-rigb-panel]"));
    var runRow = wrap.querySelector("[data-rigb-runrow]");
    var run = wrap.querySelector("[data-rigb-run]");
    var closer = wrap.querySelector("[data-rigb-close]");
    var best = wrap.getAttribute("data-best");
    var needed = parseInt(wrap.getAttribute("data-done-after"), 10) || 0;
    if (!dials.length || !panels.length || !run) { return; }

    /* The chosen value of each dial and the dial ORDER are read off the
       resting DOM rather than assumed. The renderer lights each dial's first
       option and emits the dials in the payload's own order, and the rig key
       is those values joined — so which dial comes first and which value each
       opens on stay the payload's business rather than being written down a
       second time here. */
    var chosen = {}, order = [];
    each(dials, function (b) {
      var name = b.getAttribute("data-rigb-for");
      if (order.indexOf(name) < 0) {
        order.push(name);
        chosen[name] = b.getAttribute("data-rigb-val");
      }
      if (b.getAttribute("aria-pressed") === "true") {
        chosen[name] = b.getAttribute("data-rigb-val");
      }
    });

    var seen = {}, seenN = 0;

    function key() {
      var parts = [], i;
      for (i = 0; i < order.length; i++) { parts.push(chosen[order[i]]); }
      return parts.join("|");
    }

    function paint() {
      var k = key();
      var isRun = !!seen[k];
      each(titles, function (p) {
        setHidden(p, p.getAttribute("data-rigb-title") !== k);
      });
      each(panels, function (p) {
        setHidden(p, p.getAttribute("data-rigb-panel") !== k || !isRun);
      });
      setHidden(runRow, isRun);
    }

    each(dials, function (btn) {
      btn.addEventListener("click", function () {
        var name = btn.getAttribute("data-rigb-for");
        var val = btn.getAttribute("data-rigb-val");
        if (chosen[name] === val) { return; }     /* the no-op press */
        chosen[name] = val;
        each(dials, function (b) {
          if (b.getAttribute("data-rigb-for") !== name) { return; }
          b.setAttribute("aria-pressed",
                         b.getAttribute("data-rigb-val") === val
                           ? "true" : "false");
        });
        paint();
      });
    });

    run.addEventListener("click", function () {
      var k = key();
      if (seen[k]) { return; }
      seen[k] = true;
      seenN += 1;
      paint();
      var panel = null;
      each(panels, function (p) {
        if (p.getAttribute("data-rigb-panel") === k) { panel = p; }
      });
      focusReveal(panel);
      if (seenN >= needed) { markStage(sec, true); }
      if (best && k === best) { setHidden(closer, false); }
    });

    paint();
  }

/* ═══ END C7 wiring ═══ */

/* ═══ BEGIN C6 wiring ═══════════════════════════════════════════════════
   C6's instrument families. Added as ONE marked block so that a lane merging
   into this file resolves mechanically: nothing above this marker moves.
   ═══ */

  /* ── bottle-sorter (c6-01 #s-bench) ──────────────────────────────────
     Eight bottles, one question asked eight times, and looking settles none
     of them.

     `c3CommitCards` is the contract — one commitment per bottle, final, with
     every button on that bottle disabling and the answer on screen the
     instant it is decided — and this family shares that body rather than
     keeping a sixth copy of it. There is no answer key in the markup and
     none is needed: the verdict names what the bottle IS, in the same voice
     whichever button was pressed, and `r_bottle_sorter` checks the flag
     against that sentence at BUILD time.

     The head counter is the shell's `[data-count]` — "0 of 8 decided" through
     to "8 of 8 decided", a sentence whose noun does not inflect, so no
     `data-format-one`. The closing panel opens on the eighth, because seven
     bottles cannot show a distribution. */
  function wireBottleSorter(sec) {
    c3CommitCards(sec, {
      wrap: "[data-bottle]", card: "[data-bottle-card]",
      opt: "[data-bottle-opt]", reveal: "[data-bottle-reveal]",
      close: "[data-bottle-close]", count: true
    });
  }

  /* ── acid-judgements (five placements across five lessons) ───────────
     One family, five pages: c6-01 `#s-hazard`, c6-02 `#s-choose`, c6-03
     `#s-uses`, c6-04 `#s-test` and c6-07 `#s-uses`. Design draws the
     identical component on all five — a question, a small set of options, one
     commitment, one answer — and C3's `sequence-rebuild` is the precedent for
     one family placed more than once.

     Two of the five ask yes/no and three ask a three-way choice; the number
     of options is a property of the ITEM and `c3CommitCards` never counts
     them, so one function covers both shapes without a branch.

     No `close`: none of the five draws a closing panel. The head counter is
     the shell's and the rail stop ticks when the last item is decided. */
  function wireAcidJudgements(sec) {
    c3CommitCards(sec, {
      wrap: "[data-ajudge]", card: "[data-ajudge-card]",
      opt: "[data-ajudge-opt]", reveal: "[data-ajudge-reveal]",
      count: true
    });
  }

  /* ── ph-bench (c6-02 #s-bench) ───────────────────────────────────────
     Six samples, five bands, and the guess comes first.

     ⚖️ THE GATE STAYS ON SCREEN. Design's `sc-if needGuess` removes the band
     buttons the moment one is pressed, which takes the student's own
     commitment away at the exact moment the reading arrives to be compared
     against it — and that comparison is what Law 4 exists to create. Every
     gate in C3, C4 and C5 stays put. This one stays put, the pressed band
     stays pressed, and its siblings dim.

     ⚠️ THE COMMITMENT IS PER SAMPLE AND IS FINAL. A sample already tested
     shows its reading with its own guess still lit; switching to an untested
     sample re-enables the row. Nothing is ever re-committed, because the
     answer is on screen by then.

     ⚠️ THE NO-OP PRESS. The tab returns early when the sample pressed is the
     sample already loaded. Design's handler does not, and pressing the loaded
     tab there re-runs the whole paint for no change.

     ⚖️ CREDIT IS FOR TESTING `data-done-at` OF THEM, which is Design's own
     `DONE` (`>= 4`). The number is read off the markup rather than written
     here, so the claim lives in the lesson record in one place. */
  function wirePhBench(sec) {
    var wrap = sec.querySelector("[data-phbench]");
    if (!wrap) { return; }
    var tabs = toArray(wrap.querySelectorAll("[data-phbench-tab]"));
    if (!tabs.length) { return; }
    var names = toArray(wrap.querySelectorAll("[data-phbench-name]"));
    var setups = toArray(wrap.querySelectorAll("[data-phbench-setup]"));
    var bands = toArray(wrap.querySelectorAll("[data-phbench-guess]"));
    var results = toArray(wrap.querySelectorAll("[data-phbench-result]"));
    var doneAt = parseInt(wrap.getAttribute("data-done-at"), 10) || tabs.length;

    /* The opening sample is whichever tab the renderer built pressed. */
    var sample = tabs[0].getAttribute("data-phbench-tab");
    each(tabs, function (b) {
      if (b.getAttribute("aria-pressed") === "true") {
        sample = b.getAttribute("data-phbench-tab");
      }
    });
    var tested = {}, nTested = 0;

    function paint() {
      var guess = tested[sample];
      each(tabs, function (b) {
        b.setAttribute("aria-pressed",
          b.getAttribute("data-phbench-tab") === sample ? "true" : "false");
      });
      each(names, function (p) {
        setHidden(p, p.getAttribute("data-phbench-name") !== sample);
      });
      each(setups, function (p) {
        setHidden(p, p.getAttribute("data-phbench-setup") !== sample);
      });
      each(bands, function (b) {
        var on = guess !== undefined &&
                 b.getAttribute("data-phbench-guess") === guess;
        b.setAttribute("aria-pressed", on ? "true" : "false");
        c3Enable(b, guess === undefined);
      });
      each(results, function (d) {
        setHidden(d, !(guess !== undefined &&
                       d.getAttribute("data-phbench-result") === sample));
      });
      markStage(sec, nTested >= doneAt);
    }

    each(tabs, function (btn) {
      btn.addEventListener("click", function () {
        var v = btn.getAttribute("data-phbench-tab");
        if (v === sample) { return; }        /* the no-op press */
        sample = v;
        paint();
      });
    });

    each(bands, function (btn) {
      btn.addEventListener("click", function () {
        if (tested[sample] !== undefined) { return; }
        tested[sample] = btn.getAttribute("data-phbench-guess");
        nTested += 1;
        paint();
        var open = null;
        each(results, function (d) {
          if (d.getAttribute("data-phbench-result") === sample) { open = d; }
        });
        focusReveal(open);                   /* MRB-257 (5.43) */
      });
    });

    paint();
  }

  /* ── titration-dial (c6-03 #s-titrate) ───────────────────────────────
     Twenty drops, and one of them is a cliff.

     ⚖️ NOT ONE NUMBER HERE IS WRITTEN DOWN. The curve, the fifteen chart
     colours and the state each drop belongs to all arrive in `data-cfg`,
     computed and CHECKED by `r_titration_dial` at build time — which is where
     the assertions live that the curve only rises, that exactly one reading
     is 7, and that the step across it is a cliff rather than a climb.
     Design's own page hard-codes "the first nine drops", "the tenth" and
     `seenJump: next >= 11` in three separate places; none of those appear
     anywhere in this function.

     ⚖️ `seenJump` IS A RATCHET AND "START AGAIN" DOES NOT CLEAR IT. Design's
     `onReset` sets `drops: 0` and leaves `seenJump` alone, and that is right:
     a student who has seen the cliff has seen it, and running the titration
     again to look at the shape is not undoing that. `markStage` is a ratchet
     for the same reason (MRB-208).

     ⚠️ THE COUNT IS THE ONE STRING THIS BLOCK COMPOSES, and it composes a
     NUMBER into a slot rather than a sentence out of parts — the same
     mechanism `setCount` uses for every head counter in the key stage. */
  function wireTitrationDial(sec) {
    var wrap = sec.querySelector("[data-titr]");
    if (!wrap) { return; }
    var cfg;
    try { cfg = JSON.parse(wrap.getAttribute("data-cfg") || "{}"); }
    catch (err) { return; }
    var curve = cfg.curve || [];
    var colours = cfg.colours || [];
    var where = cfg.where || [];
    if (!curve.length) { return; }

    var beaker = wrap.querySelector("[data-titr-beaker]");
    var phs = toArray(wrap.querySelectorAll("[data-titr-ph]"));
    var count = wrap.querySelector("[data-titr-count]");
    var states = toArray(wrap.querySelectorAll("[data-titr-state]"));
    var notes = toArray(wrap.querySelectorAll("[data-titr-note]"));
    var bars = toArray(wrap.querySelectorAll("[data-titr-bar]"));
    var adds = toArray(wrap.querySelectorAll("[data-titr-add]"));
    var reset = wrap.querySelector("[data-titr-reset]");
    var closer = wrap.querySelector("[data-titr-close]");
    var doneAt = parseInt(wrap.getAttribute("data-done-at"), 10) || curve.length;
    var fmt = count ? (count.getAttribute("data-format") || "") : "";

    var drops = 0, seenJump = false;

    function paint() {
      var ph = curve[drops];
      var here = where[drops];
      if (beaker && colours[ph]) { beaker.style.background = colours[ph]; }
      each(phs, function (s) {
        setHidden(s, parseInt(s.getAttribute("data-titr-ph"), 10) !== ph);
      });
      if (count && fmt) {
        count.textContent = fmt.split("{n}").join(String(drops));
      }
      each(states, function (p) {
        setHidden(p, p.getAttribute("data-titr-state") !== here);
      });
      each(notes, function (p) {
        setHidden(p, p.getAttribute("data-titr-note") !== here);
      });
      each(bars, function (b) {
        b.setAttribute("data-on",
          parseInt(b.getAttribute("data-titr-bar"), 10) <= drops ? "1" : "0");
      });
      setHidden(closer, !seenJump);
      markStage(sec, drops >= doneAt);
    }

    each(adds, function (btn) {
      btn.addEventListener("click", function () {
        var n = parseInt(btn.getAttribute("data-titr-add"), 10) || 1;
        if (drops >= curve.length - 1) { return; }
        var before = seenJump;
        drops = Math.min(curve.length - 1, drops + n);
        /* The payoff panel opens the first time the reading goes past
           neutral. Derived from the curve, never from a drop number. */
        if (curve[drops] > 7) { seenJump = true; }
        paint();
        if (!before && seenJump) { focusReveal(closer); }
      });
    });

    if (reset) {
      reset.addEventListener("click", function () {
        if (drops === 0) { return; }
        drops = 0;
        paint();                             /* `seenJump` survives */
      });
    }

    paint();
  }

  /* ── acid-metal-grid (c6-04 #s-bench) ────────────────────────────────
     Four metals crossed with two acids, and the prediction comes first.

     ⚠️ NOT `reactivity-grid`. `ks3_art/c5.py` owns that family and the shell
     class `ks3-rgrid-block`; this is C6's own, with its own `amgrid` prefix.
     Two families wearing one class is MRB-279's gate and it fails silently.

     ⚖️ THE CELL'S MARK IS TWO SPANS, NOT AN ATTRIBUTE READ BACK. "?" and
     "fizzes" are both in the document and one is unhidden, so a cell can
     never show a value this file composed.

     ⚖️ CREDIT IS FOR RUNNING `data-done-at` OF THE EIGHT, which is Design's
     own threshold of six — enough to have met the copper row, which is the
     row that proves the rule. */
  function wireAcidMetalGrid(sec) {
    var wrap = sec.querySelector("[data-amgrid]");
    if (!wrap) { return; }
    var cells = toArray(wrap.querySelectorAll("[data-amgrid-cell]"));
    if (!cells.length) { return; }
    var titles = toArray(wrap.querySelectorAll("[data-amgrid-title]"));
    var setups = toArray(wrap.querySelectorAll("[data-amgrid-setup]"));
    var predicts = toArray(wrap.querySelectorAll("[data-amgrid-predict]"));
    var results = toArray(wrap.querySelectorAll("[data-amgrid-result]"));
    var closer = wrap.querySelector("[data-amgrid-close]");
    var doneAt = parseInt(wrap.getAttribute("data-done-at"), 10) || cells.length;

    var here = cells[0].getAttribute("data-amgrid-cell");
    each(cells, function (b) {
      if (b.getAttribute("aria-pressed") === "true") {
        here = b.getAttribute("data-amgrid-cell");
      }
    });
    var ran = {}, nRan = 0;

    function paint() {
      var done = ran[here] !== undefined;
      each(cells, function (b) {
        var k = b.getAttribute("data-amgrid-cell");
        b.setAttribute("aria-pressed", k === here ? "true" : "false");
        b.setAttribute("data-run", ran[k] !== undefined ? "1" : "0");
        setHidden(b.querySelector("[data-amgrid-unrun]"), ran[k] !== undefined);
        setHidden(b.querySelector("[data-amgrid-mark]"), ran[k] === undefined);
      });
      each(titles, function (p) {
        setHidden(p, p.getAttribute("data-amgrid-title") !== here);
      });
      each(setups, function (p) {
        setHidden(p, p.getAttribute("data-amgrid-setup") !== here);
      });
      each(predicts, function (b) {
        var on = done && b.getAttribute("data-amgrid-predict") === ran[here];
        b.setAttribute("aria-pressed", on ? "true" : "false");
        c3Enable(b, !done);
      });
      each(results, function (d) {
        setHidden(d, !(done && d.getAttribute("data-amgrid-result") === here));
      });
      setCount(sec, nRan);
      if (nRan >= doneAt) {
        setHidden(closer, false);
        markStage(sec, true);
      }
    }

    each(cells, function (btn) {
      btn.addEventListener("click", function () {
        var k = btn.getAttribute("data-amgrid-cell");
        if (k === here) { return; }          /* the no-op press */
        here = k;
        paint();
      });
    });

    each(predicts, function (btn) {
      btn.addEventListener("click", function () {
        if (ran[here] !== undefined) { return; }
        ran[here] = btn.getAttribute("data-amgrid-predict");
        nRan += 1;
        var opened = here;
        paint();
        var open = null;
        each(results, function (d) {
          if (d.getAttribute("data-amgrid-result") === opened) { open = d; }
        });
        focusReveal(nRan >= doneAt && closer ? closer : open);
      });
    });

    setCount(sec, 0);
    paint();
  }

  /* ── salt-namer (c6-06 #s-name) ──────────────────────────────────────
     Three acids crossed with four bases, and the name is committed before it
     is checked.

     ⚖️ THE ASK STAYS ON SCREEN. Design's `sc-if needName` removes the three
     buttons the moment one is pressed. Same ruling as every other gate in
     C3–C6: the commitment stays visible beside the answer it is being
     compared with.

     ⚖️ CREDIT IS FOR NAMING `data-done-at` COMBINATIONS — Design's own three,
     and her own sentence: "Twelve are possible — three is enough to see the
     rule." Twelve would make the stop a completion bar.

     ⚠️ NOTHING HERE KNOWS WHICH NAME IS RIGHT, and nothing needs to. The
     answer panel names the salt and draws the equation in the same voice
     whichever button was pressed; the rule that generates the name is run and
     asserted at BUILD time by `r_salt_namer`. */
  function wireSaltNamer(sec) {
    var wrap = sec.querySelector("[data-namer]");
    if (!wrap) { return; }
    var acids = toArray(wrap.querySelectorAll("[data-namer-acid]"));
    var bases = toArray(wrap.querySelectorAll("[data-namer-base]"));
    if (!acids.length || !bases.length) { return; }
    var titles = toArray(wrap.querySelectorAll("[data-namer-title]"));
    var rows = toArray(wrap.querySelectorAll("[data-namer-optrow]"));
    var opts = toArray(wrap.querySelectorAll("[data-namer-opt]"));
    var results = toArray(wrap.querySelectorAll("[data-namer-result]"));
    var doneAt = parseInt(wrap.getAttribute("data-done-at"), 10) || 3;

    function pressedOf(list, attr) {
      var v = list[0].getAttribute(attr);
      each(list, function (b) {
        if (b.getAttribute("aria-pressed") === "true") {
          v = b.getAttribute(attr);
        }
      });
      return v;
    }
    var acid = pressedOf(acids, "data-namer-acid");
    var base = pressedOf(bases, "data-namer-base");
    var named = {}, nNamed = 0;

    function key() { return acid + ":" + base; }

    function paint() {
      var k = key();
      var done = named[k] !== undefined;
      each(acids, function (b) {
        b.setAttribute("aria-pressed",
          b.getAttribute("data-namer-acid") === acid ? "true" : "false");
      });
      each(bases, function (b) {
        b.setAttribute("aria-pressed",
          b.getAttribute("data-namer-base") === base ? "true" : "false");
      });
      each(titles, function (p) {
        setHidden(p, p.getAttribute("data-namer-title") !== k);
      });
      each(rows, function (r) {
        setHidden(r, r.getAttribute("data-namer-optrow") !== k);
      });
      each(opts, function (b) {
        var parts = b.getAttribute("data-namer-opt").split("|");
        var mine = parts[0] === k;
        var chosen = named[parts[0]];
        b.setAttribute("aria-pressed",
          chosen !== undefined && chosen === parts[1] ? "true" : "false");
        c3Enable(b, !(mine && chosen !== undefined));
      });
      each(results, function (d) {
        setHidden(d, !(done && d.getAttribute("data-namer-result") === k));
      });
      markStage(sec, nNamed >= doneAt);
    }

    function dial(list, attr, set) {
      each(list, function (btn) {
        btn.addEventListener("click", function () {
          var v = btn.getAttribute(attr);
          if (!set(v)) { return; }           /* the no-op press */
          paint();
        });
      });
    }
    dial(acids, "data-namer-acid", function (v) {
      if (v === acid) { return false; }
      acid = v; return true;
    });
    dial(bases, "data-namer-base", function (v) {
      if (v === base) { return false; }
      base = v; return true;
    });

    each(opts, function (btn) {
      btn.addEventListener("click", function () {
        var parts = btn.getAttribute("data-namer-opt").split("|");
        if (parts[0] !== key() || named[parts[0]] !== undefined) { return; }
        named[parts[0]] = parts[1];
        nNamed += 1;
        var opened = parts[0];
        paint();
        var open = null;
        each(results, function (d) {
          if (d.getAttribute("data-namer-result") === opened) { open = d; }
        });
        focusReveal(open);                   /* MRB-257 (5.43) */
      });
    });

    paint();
  }

  /* ── method-order (c6-06 #s-method) ──────────────────────────────────
     Six steps, shuffled, tapped into order.

     ⚖️ NOTHING IS MARKED, INCLUDING THE ORDER. Design draws two closing
     lines — "That is the order, and every step earns its place" against "Not
     the order that works. Here is the sequence and what each step is for" —
     followed by the SAME six explanations either way, and that is reproduced
     exactly. No green, no red, no per-step tick: the six reasons are the
     point of the block whether the order came out right or not, and only the
     mastery ladder marks.

     ⚠️ THE ONLY THING THIS FUNCTION COMPUTES IS A POSITION NUMBER, and it
     writes it into a badge. `data-correct` is a list of ids and is compared
     as a list; the verdict is chosen between two paragraphs that are already
     in the document.

     ⚖️ "START THE ORDER AGAIN" CLEARS THE ORDER AND NOT THE CREDIT.
     `markStage` is a ratchet (MRB-208): a student who has placed all six has
     placed all six, and rearranging them to look at the reasons again does
     not take that back. There is no chemistry anywhere in this function —
     NOTES-C6 §4 declares the family generic and C10-03 is already named as
     its second placement. */
  function wireMethodOrder(sec) {
    var wrap = sec.querySelector("[data-morder]");
    if (!wrap) { return; }
    var steps = toArray(wrap.querySelectorAll("[data-morder-step]"));
    if (!steps.length) { return; }
    var correct;
    try { correct = JSON.parse(wrap.getAttribute("data-morder-key") || "[]"); }
    catch (err) { correct = []; }
    var total = parseInt(wrap.getAttribute("data-total"), 10) || steps.length;
    var clear = wrap.querySelector("[data-morder-clear]");
    var panel = wrap.querySelector("[data-morder-answer]");
    var verdicts = toArray(wrap.querySelectorAll("[data-morder-verdict]"));

    var order = [];

    function paint() {
      var full = order.length >= total;
      var right = full;
      var i;
      for (i = 0; i < order.length && right; i++) {
        if (order[i] !== correct[i]) { right = false; }
      }
      each(steps, function (b) {
        var id = b.getAttribute("data-morder-step");
        var at = order.indexOf(id);
        b.setAttribute("data-placed", at >= 0 ? "1" : "0");
        c3Enable(b, at < 0);
        var badge = b.querySelector("[data-morder-badge]");
        if (badge) { badge.textContent = at >= 0 ? String(at + 1) : ""; }
      });
      setHidden(panel, !full);
      each(verdicts, function (p) {
        var want = right ? "right" : "wrong";
        setHidden(p, !full || p.getAttribute("data-morder-verdict") !== want);
      });
      markStage(sec, full);
    }

    each(steps, function (btn) {
      btn.addEventListener("click", function () {
        var id = btn.getAttribute("data-morder-step");
        if (order.indexOf(id) >= 0) { return; }
        order.push(id);
        var full = order.length >= total;
        paint();
        if (full) { focusReveal(panel); }    /* MRB-257 (5.43) */
      });
    });

    if (clear) {
      clear.addEventListener("click", function () {
        if (!order.length) { return; }
        order = [];
        paint();                             /* the tick is a ratchet */
      });
    }

    paint();
  }

  /* ── catalyst-bench (c6-07 #s-bench) ─────────────────────────────────
     Five flasks, two controls, and one that is faster and still not a
     catalyst.

     ⚖️ CREDIT IS FOR RUNNING ALL FIVE, and here that is right rather than
     demanding: the argument is a comparison ACROSS the set and four flasks
     cannot make it — whichever four you leave out, one of the three claims
     the closing panel makes has no evidence. `data-total` is the number, read
     off the markup.

     ⚠️ WHICH TRIALS WERE FASTER, AND WHICH QUALIFY, ARE DECIDED AT BUILD
     TIME. `r_catalyst_bench` parses every volume, derives "faster" against
     the control's reading, and asserts that every declared catalyst is faster
     AND recovered, that at least one trial is faster and is NOT a catalyst,
     and that at least two change nothing. Nothing in this function knows any
     of that, and nothing in it should. */
  function wireCatalystBench(sec) {
    var wrap = sec.querySelector("[data-catb]");
    if (!wrap) { return; }
    var tabs = toArray(wrap.querySelectorAll("[data-catb-tab]"));
    if (!tabs.length) { return; }
    var titles = toArray(wrap.querySelectorAll("[data-catb-title]"));
    var setups = toArray(wrap.querySelectorAll("[data-catb-setup]"));
    var predicts = toArray(wrap.querySelectorAll("[data-catb-predict]"));
    var results = toArray(wrap.querySelectorAll("[data-catb-result]"));
    var closer = wrap.querySelector("[data-catb-close]");
    var total = parseInt(wrap.getAttribute("data-total"), 10) || tabs.length;

    var pick = tabs[0].getAttribute("data-catb-tab");
    each(tabs, function (b) {
      if (b.getAttribute("aria-pressed") === "true") {
        pick = b.getAttribute("data-catb-tab");
      }
    });
    var ran = {}, nRan = 0;

    function paint() {
      var done = ran[pick] !== undefined;
      each(tabs, function (b) {
        b.setAttribute("aria-pressed",
          b.getAttribute("data-catb-tab") === pick ? "true" : "false");
      });
      each(titles, function (p) {
        setHidden(p, p.getAttribute("data-catb-title") !== pick);
      });
      each(setups, function (p) {
        setHidden(p, p.getAttribute("data-catb-setup") !== pick);
      });
      each(predicts, function (b) {
        var on = done && b.getAttribute("data-catb-predict") === ran[pick];
        b.setAttribute("aria-pressed", on ? "true" : "false");
        c3Enable(b, !done);
      });
      each(results, function (d) {
        setHidden(d, !(done && d.getAttribute("data-catb-result") === pick));
      });
      setCount(sec, nRan);
      if (nRan >= total) {
        setHidden(closer, false);
        markStage(sec, true);
      }
    }

    each(tabs, function (btn) {
      btn.addEventListener("click", function () {
        var v = btn.getAttribute("data-catb-tab");
        if (v === pick) { return; }          /* the no-op press */
        pick = v;
        paint();
      });
    });

    each(predicts, function (btn) {
      btn.addEventListener("click", function () {
        if (ran[pick] !== undefined) { return; }
        ran[pick] = btn.getAttribute("data-catb-predict");
        nRan += 1;
        var opened = pick;
        paint();
        var open = null;
        each(results, function (d) {
          if (d.getAttribute("data-catb-result") === opened) { open = d; }
        });
        focusReveal(nRan >= total && closer ? closer : open);
      });
    });

    setCount(sec, 0);
    paint();
  }

/* ═══ END C6 wiring ═══ */

/* ═══ BEGIN C8 wiring ═══════════════════════════════════════════════════
   C8's instrument families — *The periodic table*. Added as ONE marked block
   so that a lane merging into this file resolves mechanically: nothing above
   this marker moves.

   Seven families. THREE of them are `c3CommitCards` with three sets of hooks,
   for the reason C7's block gives: what must not drift between a six-sample
   property sorter, a fifteen-card commit block and a gap-filler's three
   predictions is exactly the rule `c3CommitCards` owns — one final commitment
   per card, every button disabling, the reveal on screen the instant the card
   is decided, and `markStage` at the point the last card closes.

   ⚖️ NOTHING IS COMPUTED IN THIS BLOCK. Not one number, not one sentence.
   Every state of every panel is already in the document (EMIT-BOTH-SHOW-ONE)
   and these handlers do exactly one thing: choose which node is `hidden`. The
   halogen grid alone carries nine authored readouts and the periodic table
   twenty, and not one of them is assembled here — so an authored `<strong>`,
   an em dash and a degree sign survive as the author wrote them, no sentence
   exists twice, and the resting render cannot disagree with the runtime one.

   ⚖️ NOTHING GREEN AND NOTHING RED REACHES A CONTROL. A pressed cell, a
   pressed prediction and a pressed card option all take the platform's
   ordinary `aria-pressed` treatment; every verdict in this unit is a PANEL OF
   WORDS. Only the mastery ladder marks. There is no `data-correct` anywhere in
   any of the seven, and `ks3_art/c8.py` refuses a payload that carries one.

   ⚖️ NOTHING ANIMATES AND NOTHING COUNTS DOWN — no rAF, no timer, no
   JS-driven transition — so `prefers-reduced-motion` has nothing to degrade
   here. There is no range control either. Every control below is a real
   `<button>` and there is no `onclick=` attribute anywhere in the markup.

   ⚠️ THE NO-OP PRESS. Every selector below returns early when the value
   pressed is the value already showing. Design's own handlers do not, and
   pressing a lit cell there re-runs the whole paint — which on the table and
   the grid would re-fire `focusReveal` and drag the page back to a readout the
   student is already reading. Corrected here rather than reproduced, which is
   the same correction C3 made across five dials, C5 across the burner bench
   and C7 across two.
   ═══ */

  /* ── property-sorter (c8-01 #s-bench) ────────────────────────────────
     Six samples, one question asked six times, and one property settles none
     of them. The head counter is the shell's `[data-count]`. */
  function wirePropertySorter(sec) {
    c3CommitCards(sec, {
      wrap: "[data-prop]", card: "[data-prop-item]",
      opt: "[data-prop-opt]", reveal: "[data-prop-reveal]",
      close: "[data-prop-close]", count: true
    });
  }

  /* ── predict-cards (c8-02 #s-rules, c8-03 #s-read, c8-04 #s-predict,
        c8-06 #s-file and #s-uses) ───────────────────────────────────────
     ONE family, FIVE placements, one wiring. See `ks3_art/c8.py`'s header for
     why these are not five families: the payloads are identical apart from an
     optional `tag`, and five copies of this handler would be five chances for
     the commit rule to drift. */
  function wirePredictCards(sec) {
    c3CommitCards(sec, {
      wrap: "[data-pcard]", card: "[data-pcard-card]",
      opt: "[data-pcard-opt]", reveal: "[data-pcard-reveal]",
      close: "[data-pcard-close]", count: true
    });
  }

  /* ── gap-filler (c8-02 #s-gap) ───────────────────────────────────────
     Three parts, one rail stop. The neighbour grid and the 1871-against-1886
     table are STATIC — they are there to be read while the predictions are
     worked, which is the whole shape of the instrument — so the only wiring
     the block needs is the three commitments. */
  function wireGapFiller(sec) {
    c3CommitCards(sec, {
      wrap: "[data-gapf]", card: "[data-gapf-card]",
      opt: "[data-gapf-opt]", reveal: "[data-gapf-reveal]",
      close: "[data-gapf-close]", count: true
    });
  }

  /* ── shell-strip (c8-06 #s-shells) ───────────────────────────────────
     Four rows, each a real <button>, each opening one authored detail. No
     commitment is taken — the strip is a reference the student opens, and the
     rail stop ticks when all four have been opened.

     ⚠️ A ROW ONCE OPENED STAYS OPEN. MRB-208: rail credit is a ratchet, and a
     toggle that closed again could take the count back down. Pressing an open
     row is a no-op. */
  function wireShellStrip(sec) {
    var wrap = sec.querySelector("[data-shel]");
    if (!wrap) { return; }
    var rows = toArray(wrap.querySelectorAll("[data-shel-row]"));
    if (!rows.length) { return; }
    var total = parseInt(wrap.getAttribute("data-total"), 10) || rows.length;
    var closer = wrap.querySelector("[data-shel-close]");

    function opened() {
      var n = 0;
      each(rows, function (r) {
        if (r.getAttribute("data-open") === "1") { n += 1; }
      });
      return n;
    }

    each(rows, function (row) {
      var btn = row.querySelector("[data-shel-toggle]");
      if (!btn) { return; }
      btn.addEventListener("click", function () {
        if (row.getAttribute("data-open") === "1") { return; }
        row.setAttribute("data-open", "1");
        btn.setAttribute("aria-expanded", "true");
        setHidden(row.querySelector("[data-shel-detail]"), false);
        var n = opened();
        setCount(sec, n);
        if (n >= total) {
          setHidden(closer, false);
          markStage(sec, true);
        }
      });
    });
    setCount(sec, 0);
  }

  /* ── table-reader (c8-03 #s-table) ───────────────────────────────────
     Twenty squares, twenty authored readouts, one shown at a time. The
     readouts are ALL in the document already — this handler unhides one and
     hides the rest, and composes nothing.

     ⚠️ `[data-tread-readout]` is not a rail stop of its own and the table's
     stop is ticked by the hook, per MRB-249: the reference exists to be read
     while `#s-read` is worked beside it. So there is no counter and no
     `markStage` here. */
  function wireTableReader(sec) {
    var wrap = sec.querySelector("[data-tread]");
    if (!wrap) { return; }
    var cells = toArray(wrap.querySelectorAll("[data-tread-cell]"));
    var outs = toArray(wrap.querySelectorAll("[data-tread-out]"));
    var rest = wrap.querySelector(".ks3-tread-rest");
    if (!cells.length || !outs.length) { return; }
    var current = null;

    each(cells, function (btn) {
      btn.addEventListener("click", function () {
        var key = btn.getAttribute("data-tread-cell");
        if (key === current) { return; }          /* the no-op press */
        current = key;
        each(cells, function (b) {
          b.setAttribute("aria-pressed",
                         b.getAttribute("data-tread-cell") === key
                           ? "true" : "false");
        });
        setHidden(rest, true);
        var shown = null;
        each(outs, function (o) {
          var on = o.getAttribute("data-tread-out") === key;
          setHidden(o, !on);
          if (on) { shown = o; }
        });
        if (shown) { focusReveal(shown); }
      });
    });
  }

  /* ── water-trough (c8-04 #s-trough) ──────────────────────────────────
     Three metals, one at a time, each run once. A metal already run is a
     no-op press; the rail stop ticks when all three have been run.

     ⚠️ THE PREDICTION IS NOT GATED AND IS NOT MARKED. Design asks the student
     to predict before dropping the metal in, and the prediction buttons take
     the ordinary pressed treatment and nothing else — pressing one does not
     unlock the run and not pressing one does not block it. A gate here would
     make the prediction a password; the point of it is that the student has
     committed before they read, which is between them and the page. */
  function wireWaterTrough(sec) {
    var wrap = sec.querySelector("[data-trough]");
    if (!wrap) { return; }
    var picks = toArray(wrap.querySelectorAll("[data-trough-metal]"));
    var runs = toArray(wrap.querySelectorAll("[data-trough-run]"));
    var preds = toArray(wrap.querySelectorAll("[data-trough-opt]"));
    var rest = wrap.querySelector(".ks3-trough-rest");
    var closer = wrap.querySelector("[data-trough-close]");
    var total = parseInt(wrap.getAttribute("data-total"), 10) || runs.length;
    if (!picks.length || !runs.length) { return; }
    var seen = {}, seenN = 0, current = null;

    each(preds, function (btn) {
      btn.addEventListener("click", function () {
        each(preds, function (b) {
          b.setAttribute("aria-pressed", b === btn ? "true" : "false");
        });
      });
    });

    each(picks, function (btn) {
      btn.addEventListener("click", function () {
        var id = btn.getAttribute("data-trough-metal");
        if (id === current) { return; }           /* the no-op press */
        current = id;
        each(picks, function (b) {
          b.setAttribute("aria-pressed",
                         b.getAttribute("data-trough-metal") === id
                           ? "true" : "false");
        });
        setHidden(rest, true);
        var shown = null;
        each(runs, function (r) {
          var on = r.getAttribute("data-trough-run") === id;
          setHidden(r, !on);
          if (on) { shown = r; }
        });
        /* The prediction resets for the next metal — a press left standing
           from the previous run would read as a prediction about this one. */
        each(preds, function (b) { b.setAttribute("aria-pressed", "false"); });
        if (!seen[id]) { seen[id] = 1; seenN += 1; setCount(sec, seenN); }
        if (shown) { focusReveal(shown); }
        if (seenN >= total) {
          setHidden(closer, false);
          markStage(sec, true);
        }
      });
    });
    setCount(sec, 0);
  }

  /* ── halogen-grid (c8-05 #s-grid) ────────────────────────────────────
     Nine tubes, nine authored readouts, one shown at a time. The rail stop
     ticks when every cell has been opened, so no band of the argument can be
     missing when the closing panel appears — the panel reads the whole grid
     as an ORDER, and it cannot do that from six cells.

     ⚠️ `halogen-grid`, not `reactivity-grid`: C5 owns that name and its shell
     class. Same shape, own family. See `ks3_art/c8.py`'s header. */
  function wireHalogenGrid(sec) {
    var wrap = sec.querySelector("[data-hgrid]");
    if (!wrap) { return; }
    var cells = toArray(wrap.querySelectorAll("[data-hgrid-cell]"));
    var outs = toArray(wrap.querySelectorAll("[data-hgrid-out]"));
    var preds = toArray(wrap.querySelectorAll("[data-hgrid-opt]"));
    var rest = wrap.querySelector(".ks3-hgrid-rest");
    var closer = wrap.querySelector("[data-hgrid-close]");
    var total = parseInt(wrap.getAttribute("data-total"), 10) || cells.length;
    if (!cells.length || !outs.length) { return; }
    var seen = {}, seenN = 0, current = null;

    each(preds, function (btn) {
      btn.addEventListener("click", function () {
        each(preds, function (b) {
          b.setAttribute("aria-pressed", b === btn ? "true" : "false");
        });
      });
    });

    each(cells, function (btn) {
      btn.addEventListener("click", function () {
        var key = btn.getAttribute("data-hgrid-cell");
        if (key === current) { return; }          /* the no-op press */
        current = key;
        each(cells, function (b) {
          b.setAttribute("aria-pressed",
                         b.getAttribute("data-hgrid-cell") === key
                           ? "true" : "false");
        });
        setHidden(rest, true);
        var shown = null;
        each(outs, function (o) {
          var on = o.getAttribute("data-hgrid-out") === key;
          setHidden(o, !on);
          if (on) { shown = o; }
        });
        each(preds, function (b) { b.setAttribute("aria-pressed", "false"); });
        if (!seen[key]) { seen[key] = 1; seenN += 1; setCount(sec, seenN); }
        if (shown) { focusReveal(shown); }
        if (seenN >= total) {
          setHidden(closer, false);
          markStage(sec, true);
        }
      });
    });
    setCount(sec, 0);
  }
/* ═══ END C8 wiring ═══ */

/* ═══ BEGIN C9 wiring ═══════════════════════════════════════════════════
   C9's instrument families — *Metals and materials*. Added as ONE marked
   block so that a lane merging into this file resolves mechanically: nothing
   above this marker moves.

   Four families. One of them is `c3CommitCards` with its own hooks, for the
   reason C7's and C8's blocks give.

   ⚖️ NOTHING IS COMPUTED IN THIS BLOCK. Not one number, not one sentence, and
   not one VERDICT. The route bench alone carries twenty-four authored
   verdicts and the spec bench twenty-four computed ones, and every single one
   of them is already in the document (EMIT-BOTH-SHOW-ONE) with its own
   `data-works` / `data-fit` flag. These handlers choose which node is
   `hidden` and read a flag. They never decide whether a method works or a
   material fits — that judgement is made once, in `ks3_art/c9.py`, where it
   is authored and asserted.

   ⚖️ NOTHING GREEN AND NOTHING RED REACHES A CONTROL. Only the ladder marks,
   and `ks3_art/c9.py` refuses a payload carrying a `correct` key.

   ⚖️ NOTHING ANIMATES AND NOTHING COUNTS DOWN. Every control is a real
   `<button>` and there is no `onclick=` attribute anywhere in the markup.

   ⚠️ THE NO-OP PRESS, and on two of these it matters more than usual: the
   route bench and the spec bench each have TWO pickers, so a press that
   re-selects the value already selected would re-fire `focusReveal` and drag
   the page back to a readout the student is reading. Both return early.
   ═══ */

  /* ── reaction-audit (c9-01 #s-bench) ─────────────────────────────────
     Twelve tubes, twelve authored readouts, one shown at a time. The bands
     panel opens when every cell has been read, so no band can be empty when
     the panel that names its members appears. */
  function wireReactionAudit(sec) {
    var wrap = sec.querySelector("[data-raud]");
    if (!wrap) { return; }
    var cells = toArray(wrap.querySelectorAll("[data-raud-cell]"));
    var outs = toArray(wrap.querySelectorAll("[data-raud-out]"));
    var preds = toArray(wrap.querySelectorAll("[data-raud-opt]"));
    var rest = wrap.querySelector(".ks3-raud-rest");
    var bands = wrap.querySelector("[data-raud-bands]");
    var closer = wrap.querySelector("[data-raud-close]");
    var total = parseInt(wrap.getAttribute("data-total"), 10) || cells.length;
    if (!cells.length || !outs.length) { return; }
    var seen = {}, seenN = 0, current = null;

    each(preds, function (btn) {
      btn.addEventListener("click", function () {
        each(preds, function (b) {
          b.setAttribute("aria-pressed", b === btn ? "true" : "false");
        });
      });
    });

    each(cells, function (btn) {
      btn.addEventListener("click", function () {
        var key = btn.getAttribute("data-raud-cell");
        if (key === current) { return; }           /* the no-op press */
        current = key;
        each(cells, function (b) {
          b.setAttribute("aria-pressed",
                         b.getAttribute("data-raud-cell") === key
                           ? "true" : "false");
        });
        setHidden(rest, true);
        var shown = null;
        each(outs, function (o) {
          var on = o.getAttribute("data-raud-out") === key;
          setHidden(o, !on);
          if (on) { shown = o; }
        });
        each(preds, function (b) { b.setAttribute("aria-pressed", "false"); });
        if (!seen[key]) { seen[key] = 1; seenN += 1; setCount(sec, seenN); }
        if (shown) { focusReveal(shown); }
        if (seenN >= total) {
          setHidden(bands, false);
          setHidden(closer, false);
          markStage(sec, true);
        }
      });
    });
    setCount(sec, 0);
  }

  /* ── prediction-deck (c9-02 #s-deck) ─────────────────────────────────
     Eight proposals, one commitment each. `c3CommitCards` owns the rule that
     must not drift: one final commitment per card, both buttons disabling,
     the reveal on screen the instant the card is decided, and `markStage` at
     the point the last card closes. */
  function wirePredictionDeck(sec) {
    c3CommitCards(sec, {
      wrap: "[data-pdeck]", card: "[data-pdeck-card]",
      opt: "[data-pdeck-opt]", reveal: "[data-pdeck-reveal]",
      close: "[data-pdeck-close]", count: true
    });
  }

  /* ── extraction-route (c9-03 #s-bench) ───────────────────────────────
     Two pickers — a delivery and a method — and twenty-four authored
     verdicts. An ore counts as FOUND when the student opens a verdict that
     works for it, which the markup states as `data-works="1"`. The rail stop
     ticks on ores found, not on pairs opened: opening all twenty-four without
     ever finding a route would tick a stop the student has not finished. */
  function wireExtractionRoute(sec) {
    var wrap = sec.querySelector("[data-xroute]");
    if (!wrap) { return; }
    var ores = toArray(wrap.querySelectorAll("[data-xroute-ore]"));
    var meths = toArray(wrap.querySelectorAll("[data-xroute-method]"));
    var outs = toArray(wrap.querySelectorAll("[data-xroute-out]"));
    var rest = wrap.querySelector(".ks3-xroute-rest");
    var groups = wrap.querySelector("[data-xroute-groups]");
    var closer = wrap.querySelector("[data-xroute-close]");
    var total = parseInt(wrap.getAttribute("data-total"), 10) || ores.length;
    if (!ores.length || !meths.length) { return; }
    var ore = null, meth = null, found = {}, foundN = 0;

    function paint() {
      if (!ore || !meth) { return; }
      var key = ore + ":" + meth;
      setHidden(rest, true);
      var shown = null;
      each(outs, function (o) {
        var on = o.getAttribute("data-xroute-out") === key;
        setHidden(o, !on);
        if (on) { shown = o; }
      });
      if (!shown) { return; }
      focusReveal(shown);
      if (shown.getAttribute("data-works") === "1" && !found[ore]) {
        found[ore] = 1; foundN += 1; setCount(sec, foundN);
        if (foundN >= total) {
          setHidden(groups, false);
          setHidden(closer, false);
          markStage(sec, true);
        }
      }
    }

    each(ores, function (btn) {
      btn.addEventListener("click", function () {
        var v = btn.getAttribute("data-xroute-ore");
        if (v === ore) { return; }                 /* the no-op press */
        ore = v;
        each(ores, function (b) {
          b.setAttribute("aria-pressed",
                         b.getAttribute("data-xroute-ore") === v
                           ? "true" : "false");
        });
        paint();
      });
    });
    each(meths, function (btn) {
      btn.addEventListener("click", function () {
        var v = btn.getAttribute("data-xroute-method");
        if (v === meth) { return; }                /* the no-op press */
        meth = v;
        each(meths, function (b) {
          b.setAttribute("aria-pressed",
                         b.getAttribute("data-xroute-method") === v
                           ? "true" : "false");
        });
        paint();
      });
    });
    setCount(sec, 0);
  }

  /* ── spec-bench (c9-04 #s-bench) ─────────────────────────────────────
     Same two-picker shape as the route bench, and the same rule about where
     the judgement lives: `data-fit="1"` is computed in `ks3_art/c9.py` from
     the requirement tag sets and read here. A job counts as MATCHED when the
     student opens the material that fits it. */
  function wireSpecBench(sec) {
    var wrap = sec.querySelector("[data-specb]");
    if (!wrap) { return; }
    var jobs = toArray(wrap.querySelectorAll("[data-specb-job]"));
    var mats = toArray(wrap.querySelectorAll("[data-specb-mat]"));
    var outs = toArray(wrap.querySelectorAll("[data-specb-out]"));
    var rest = wrap.querySelector(".ks3-specb-rest");
    var closer = wrap.querySelector("[data-specb-close]");
    var total = parseInt(wrap.getAttribute("data-total"), 10) || jobs.length;
    if (!jobs.length || !mats.length) { return; }
    var job = null, mat = null, done = {}, doneN = 0;

    function paint() {
      if (!job || !mat) { return; }
      var key = job + ":" + mat;
      setHidden(rest, true);
      var shown = null;
      each(outs, function (o) {
        var on = o.getAttribute("data-specb-out") === key;
        setHidden(o, !on);
        if (on) { shown = o; }
      });
      if (!shown) { return; }
      focusReveal(shown);
      if (shown.getAttribute("data-fit") === "1" && !done[job]) {
        done[job] = 1; doneN += 1; setCount(sec, doneN);
        if (doneN >= total) {
          setHidden(closer, false);
          markStage(sec, true);
        }
      }
    }

    /* The job cards are the first picker. They are real buttons wrapped
       around the card, so the whole card is the target. */
    each(jobs, function (card) {
      var btn = card.querySelector("[data-specb-jbtn]") || card;
      btn.addEventListener("click", function () {
        var v = card.getAttribute("data-specb-job");
        if (v === job) { return; }                 /* the no-op press */
        job = v;
        each(jobs, function (c) {
          var on = c.getAttribute("data-specb-job") === v;
          c.setAttribute("data-open", on ? "1" : "0");
          var b = c.querySelector("[data-specb-jbtn]");
          if (b) { b.setAttribute("aria-pressed", on ? "true" : "false"); }
        });
        paint();
      });
    });
    each(mats, function (btn) {
      btn.addEventListener("click", function () {
        var v = btn.getAttribute("data-specb-mat");
        if (v === mat) { return; }                 /* the no-op press */
        mat = v;
        each(mats, function (b) {
          b.setAttribute("aria-pressed",
                         b.getAttribute("data-specb-mat") === v
                           ? "true" : "false");
        });
        paint();
      });
    });
    setCount(sec, 0);
  }
/* ═══ END C9 wiring ═══ */






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
    // ═══ BEGIN B6 wiring ═══
    each(root.querySelectorAll("[data-routeblock]"), wireRouteTracer);
    each(root.querySelectorAll("[data-clearblock]"), wireClearanceClock);
    each(root.querySelectorAll("[data-ccheckblock]"), wireClaimCheck);
    // ═══ END B6 wiring ═══
    // ═══ BEGIN B5 wiring ═══
    // Eight instruments, three wire functions. Five kinds share
    // `data-b5cblock` and two share `data-cmpblock`, which is what stops
    // b5-04's bench and b5-05's drifting apart (NOTES-B5 §6).
    each(root.querySelectorAll("[data-b5cblock]"), wireB5Commit);
    each(root.querySelectorAll("[data-cmpblock]"), wireCompareRows);
    each(root.querySelectorAll("[data-dialblock]"), wireCycleDial);
    // ═══ END B5 wiring ═══
    // ═══ BEGIN B7 wiring ═══
    // Four instruments, four markers, four functions. Nothing is shared,
    // because nothing in this unit is the same block twice — see the section
    // note above `wireReactantRemover`.
    each(root.querySelectorAll("[data-rrblock]"), wireReactantRemover);
    each(root.querySelectorAll("[data-ltblock]"), wireLeafTuner);
    each(root.querySelectorAll("[data-mbblock]"), wireMethodBreaker);
    each(root.querySelectorAll("[data-tbblock]"), wireTraceItBack);
    // ═══ END B7 wiring ═══

  /* ── b8-05 · route-decider ──────────────────────────────────────────────
     Five cases, three routes, one commitment each.

     ⚠️ NOTHING GREEN AND NOTHING RED REACHES A ROUTE BUTTON. The verdict panel
     names, in words, which route was running and whether the student had it.
     MRB-196 R10 and the house rule: only the ladder marks correctness.

     ⚖️ A SETTLED CASE STAYS SETTLED, AND STAYS SHOWING ITS VERDICT. Switching
     away and back must not un-settle one, or the rail stop would tick and then
     untick as the student browsed — and a student who has met the marathon
     cannot be allowed to un-meet it. `picked` is therefore write-once per case;
     `pending` holds an uncommitted selection so that browsing away and back
     does not silently discard it either. */
  function wireRouteDecider(sec) {
    var w = sec.querySelector("[data-rd]");
    if (!w) { return; }
    var caseBtns = toArray(w.querySelectorAll("[data-rd-case]"));
    var routeBtns = toArray(w.querySelectorAll("[data-rd-route]"));
    var run = w.querySelector("[data-rd-run]");
    var textEl = w.querySelector("[data-rd-text]");
    var vBox = w.querySelector("[data-rd-verdict]");
    var vWord = w.querySelector("[data-rd-word]");
    var vWhy = w.querySelector("[data-rd-why]");
    var progEl = w.querySelector("[data-rd-progress]");
    var tallyEl = w.querySelector("[data-rd-tally]");
    if (!caseBtns.length || !routeBtns.length || !run) { return; }

    var cases = [], verdicts = {}, tally = {}, labels = {};
    var progress = w.getAttribute("data-progress") || "";
    try {
      cases = JSON.parse(w.getAttribute("data-cases") || "[]");
      verdicts = JSON.parse(w.getAttribute("data-verdicts") || "{}");
      tally = JSON.parse(w.getAttribute("data-tally") || "{}");
      labels = JSON.parse(w.getAttribute("data-labels") || "{}");
    } catch (x) { return; }
    if (!cases.length) { return; }

    var AFTER = parseInt(w.getAttribute("data-done-after"), 10) || cases.length;
    var picked = {};      /* case id -> the route committed to. Write-once. */
    var pending = {};     /* case id -> a selection not yet checked. */
    var here = cases[0].id;

    function caseById(id) {
      var i;
      for (i = 0; i < cases.length; i++) {
        if (cases[i].id === id) { return cases[i]; }
      }
      return null;
    }

    function settledCount() {
      var n = 0, k;
      for (k in picked) {
        if (Object.prototype.hasOwnProperty.call(picked, k)) { n++; }
      }
      return n;
    }

    function showVerdict(c) {
      if (!vBox) { return; }
      var had = picked[c.id] === c.answer;
      if (vWord) { vWord.textContent = had ? verdicts.right : verdicts.wrong; }
      if (vWhy) { vWhy.textContent = c.why; }
      vBox.hidden = false;
    }

    function paint() {
      var c = caseById(here), done = settledCount(), i;
      if (!c) { return; }
      if (textEl) { textEl.textContent = c.text; }
      for (i = 0; i < caseBtns.length; i++) {
        caseBtns[i].setAttribute(
          "aria-pressed",
          caseBtns[i].getAttribute("data-rd-case") === here ? "true" : "false");
      }
      var sel = picked[here] || pending[here] || "";
      for (i = 0; i < routeBtns.length; i++) {
        routeBtns[i].setAttribute(
          "aria-pressed",
          routeBtns[i].getAttribute("data-rd-route") === sel ? "true" : "false");
      }
      if (picked[here]) {
        showVerdict(c);
        run.disabled = true;
        if (labels.ran) { run.textContent = labels.ran; }
      } else {
        if (vBox) { vBox.hidden = true; }
        run.disabled = !pending[here];
        if (labels.run) { run.textContent = labels.run; }
      }
      if (progEl && progress) {
        progEl.textContent = progress.replace("{n}", String(done))
                                     .replace("{total}", String(cases.length));
      }
      if (tallyEl) {
        tallyEl.textContent = done >= cases.length
          ? (tally.all || "")
          : String(tally.remaining || "").replace(
              "{n}", String(cases.length - done));
      }
      markStage(sec, done >= AFTER);
    }

    each(caseBtns, function (b) {
      b.addEventListener("click", function () {
        here = b.getAttribute("data-rd-case");
        paint();
      });
    });

    each(routeBtns, function (b) {
      b.addEventListener("click", function () {
        if (picked[here]) { return; }   /* a settled case does not re-open */
        pending[here] = b.getAttribute("data-rd-route");
        paint();
      });
    });

    run.addEventListener("click", function () {
      if (picked[here] || !pending[here]) { return; }
      picked[here] = pending[here];
      paint();
    });

    paint();
  }

    // ═══ BEGIN B8 wiring ═══
    // Five instruments, five markers. A kind that reaches this list but has no
    // wire function ships as static markup that never responds — which is the
    // §6.6 failure the dispatch gate above catches on the Python side and this
    // list is the JS half of.
    each(root.querySelectorAll("[data-mlblock]"), wireMassLedger);
    each(root.querySelectorAll("[data-cdblock]"), wireCellDemand);
    each(root.querySelectorAll("[data-odblock]"), wireOxygenDebt);
    each(root.querySelectorAll("[data-fmblock]"), wireFermenter);
    each(root.querySelectorAll("[data-rdblock]"), wireRouteDecider);
    // ═══ END B8 wiring ═══
    // ═══ BEGIN B9 wiring ═══
    // Six instruments, six markers. A kind that reaches the dispatch table and
    // not this list ships as static markup that never responds — the §6.6
    // failure, and this list is the JS half of the gate that catches it.
    each(root.querySelectorAll("[data-clblock]"), wireChainLedger);
    each(root.querySelectorAll("[data-cyblock]"), wireCycleRunner);
    each(root.querySelectorAll("[data-rsblock]"), wireRemoveASpecies);
    each(root.querySelectorAll("[data-ssblock]"), wireSupermarketShelf);
    each(root.querySelectorAll("[data-bablock]"), wireBioaccumulation);
    each(root.querySelectorAll("[data-qbblock]"), wireQuadratBench);
    // ═══ END B9 wiring ═══
    // ═══ BEGIN B10 wiring ═══
    // Five instruments, five markers. A kind that reaches the dispatch table
    // and not this list ships as static markup that never responds — the
    // contract §6.6 failure, and this list is the JS half of the gate that
    // catches it.
    each(root.querySelectorAll("[data-vpblock]"), wireVariationPlotter);
    each(root.querySelectorAll("[data-zbblock]"), wireZoomBench);
    each(root.querySelectorAll("[data-dhblock]"), wireModelBuilder);
    each(root.querySelectorAll("[data-pcblock]"), wirePeaCross);
    each(root.querySelectorAll("[data-scblock]"), wireSpeciesCases);
    // ═══ END B10 wiring ═══
    // ═══ BEGIN B11 wiring ═══
    // Four instruments, four markers. A kind that reaches the dispatch table
    // and not this list ships as static markup that never responds — the
    // contract §6.6 failure, and this list is the JS half of the gate that
    // catches it.
    each(root.querySelectorAll("[data-abblock]"), wireAdvantageBench);
    each(root.querySelectorAll("[data-nrblock]"), wireSelectionRunner);
    each(root.querySelectorAll("[data-pbblock]"), wirePressureBench);
    each(root.querySelectorAll("[data-bbblock]"), wireBlightBench);
    // ═══ END B11 wiring ═══
    // ═══ BEGIN C3 wiring ═══
    // Nine instruments, nine markers, nine functions. A kind that reaches the
    // dispatch table and not this list ships as static markup that never
    // responds — the contract §6.6 failure, and this list is the JS half of the
    // gate that catches it. `sequence-rebuild` is ONE family placed twice on
    // c3-03, so it is one line here and its `data-phase` picks the branch.
    each(root.querySelectorAll("[data-psortblock]"), wirePuritySorter);
    each(root.querySelectorAll("[data-dlabblock]"), wireDissolveLab);
    each(root.querySelectorAll("[data-seqblock]"), wireSequenceRebuild);
    each(root.querySelectorAll("[data-crystblock]"), wireCrystalBench);
    each(root.querySelectorAll("[data-mchoiceblock]"), wireMethodChoice);
    each(root.querySelectorAll("[data-stillblock]"), wireStillRun);
    each(root.querySelectorAll("[data-chromablock]"), wireChromaRun);
    each(root.querySelectorAll("[data-critiqueblock]"), wirePlanCritique);
    each(root.querySelectorAll("[data-mpbblock]"), wireMeltingPointBench);
    // ═══ END C3 wiring ═══
    // ═══ BEGIN C4 wiring ═══
    each(root.querySelectorAll("[data-cpairblock]"), wireChangePairs);
    each(root.querySelectorAll("[data-chainblock]"), wireChainBuild);
    each(root.querySelectorAll("[data-arrblock]"), wireAtomRearranger);
    each(root.querySelectorAll("[data-iaskblock]"), wireImpossibleAsk);
    each(root.querySelectorAll("[data-eqbblock]"), wireEquationBuilder);
    each(root.querySelectorAll("[data-eqrblock]"), wireEquationRead);
    each(root.querySelectorAll("[data-bbenchblock]"), wireMassBench);
    each(root.querySelectorAll("[data-mcovblock]"), wireMassCover);
    each(root.querySelectorAll("[data-mworkblock]"), wireMassWorked);
    each(root.querySelectorAll("[data-mchkblock]"), wireMassCheck);
    each(root.querySelectorAll("[data-cbalblock]"), wireCoefficientBalancer);
    each(root.querySelectorAll("[data-forbidblock]"), wireForbiddenMove);
    // ═══ END C4 wiring ═══
    // ═══ BEGIN C5 wiring ═══
    each(root.querySelectorAll("[data-burnerblock]"), wireBurnerBench);
    each(root.querySelectorAll("[data-fcardblock]"), wireFuelCards);
    each(root.querySelectorAll("[data-tuberblock]"), wireTubeRun);
    each(root.querySelectorAll("[data-dcompblock]"), wireDecompSort);
    each(root.querySelectorAll("[data-ctubeblock]"), wireControlTubes);
    each(root.querySelectorAll("[data-rstopblock]"), wireRustStop);
    each(root.querySelectorAll("[data-rgridblock]"), wireReactivityGrid);
    each(root.querySelectorAll("[data-ruseblock]"), wireReactivityUse);
    each(root.querySelectorAll("[data-tsortblock]"), wireTypeSorter);
    each(root.querySelectorAll("[data-rwriteblock]"), wireRuleWrite);
    // ═══ END C5 wiring ═══
    // ═══ BEGIN C7 wiring ═══
    each(root.querySelectorAll("[data-hcurveblock]"), wireHeatingCurve);
    each(root.querySelectorAll("[data-tempbblock]"), wireTempBench);
    each(root.querySelectorAll("[data-esortblock]"), wireEnergySorter);
    each(root.querySelectorAll("[data-euseblock]"), wireEnergyUses);
    each(root.querySelectorAll("[data-rplanblock]"), wireRigPlanCritique);
    each(root.querySelectorAll("[data-rigbblock]"), wireRigBuilder);
    // ═══ END C7 wiring ═══
    // ═══ BEGIN C6 wiring ═══
    each(root.querySelectorAll("[data-bottleblock]"), wireBottleSorter);
    each(root.querySelectorAll("[data-ajudgeblock]"), wireAcidJudgements);
    each(root.querySelectorAll("[data-phbenchblock]"), wirePhBench);
    each(root.querySelectorAll("[data-titrblock]"), wireTitrationDial);
    each(root.querySelectorAll("[data-amgridblock]"), wireAcidMetalGrid);
    each(root.querySelectorAll("[data-namerblock]"), wireSaltNamer);
    each(root.querySelectorAll("[data-morderblock]"), wireMethodOrder);
    each(root.querySelectorAll("[data-catbblock]"), wireCatalystBench);
    // ═══ END C6 wiring ═══
    // ═══ BEGIN C8 wiring ═══
    each(root.querySelectorAll("[data-propblock]"), wirePropertySorter);
    each(root.querySelectorAll("[data-gapfblock]"), wireGapFiller);
    each(root.querySelectorAll("[data-pcardblock]"), wirePredictCards);
    each(root.querySelectorAll("[data-treadblock]"), wireTableReader);
    each(root.querySelectorAll("[data-troughblock]"), wireWaterTrough);
    each(root.querySelectorAll("[data-hgridblock]"), wireHalogenGrid);
    each(root.querySelectorAll("[data-shelblock]"), wireShellStrip);
    // ═══ END C8 wiring ═══
    // ═══ BEGIN C9 wiring ═══
    each(root.querySelectorAll("[data-raudblock]"), wireReactionAudit);
    each(root.querySelectorAll("[data-pdeckblock]"), wirePredictionDeck);
    each(root.querySelectorAll("[data-xrouteblock]"), wireExtractionRoute);
    each(root.querySelectorAll("[data-specbblock]"), wireSpecBench);
    // ═══ END C9 wiring ═══
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

    // ⊕ MRB-249 — a stop may MIRROR an earlier stop. Design's `isDone()` is a
    // rail-level function and returns the same expression for two consecutive
    // ids on 33 of her 48 lesson pages: the synthesis section is the payoff of
    // the instrument beside it and carries no control of its own, because the
    // instrument already took the student's commitment. Resolved here rather
    // than in `doneByDom`, because `doneByDom` answers "is this SECTION
    // finished" and a mirror is a statement about the RAIL.
    //
    // Base states are computed for every stop first, then mirrors are resolved
    // against them — so a mirror never reads a half-built array, and a mirror
    // pointing at another mirror still lands on a real section's state. The
    // hop limit is a cycle guard: `mirrors` is authored, and an author who
    // writes a loop gets a stop that stays untocked rather than a hung tab.
    var anchorIndex = {};
    for (var a = 0; a < stages.length; a++) { anchorIndex[stages[a].anchor] = a; }

    function paint() {
      var done = 0;
      var base = [];
      for (var b = 0; b < stages.length; b++) { base[b] = doneByDom(sectionFor(b)); }
      function resolve(i) {
        var seen = 0, at = i;
        while (stages[at] && stages[at].mirrors && seen < stages.length) {
          var nxt = anchorIndex[stages[at].mirrors];
          if (nxt === undefined || nxt === at) { break; }
          at = nxt; seen++;
        }
        return base[at];
      }
      for (var i = 0; i < stages.length; i++) {
        var isDone = resolve(i);
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

  /* ── the sticky height, measured rather than guessed (⊕ MRB-229 comment 2)
     `shared/ks3.css` used to offset in-page anchors with
     `.ks3-lesson [id] { scroll-margin-top: 92px }`. `header.ks3-nav` is
     `position: sticky; top: 0` and its measured height runs from 86.3px to
     214.8px, so on 36 of 58 lesson pages a rail stop landed its section behind
     the header — up to 123.2px of it, an entire `<h2>`, or "START HERE" on
     eleven pages in B8–B11. That breaks the page's primary navigation on the
     viewport most students use.

     MRB-229 rules two fixes and says explicitly that they COMPOSE. The trail
     truncation (in the stylesheet) stops the header wrapping on most pages;
     this one makes the offset unable to be wrong on the rest. A second fixed
     number would drift again the moment a Chemistry or Physics unit title runs
     longer than Biology's, which is a matter of weeks.

     Two properties, because two different things need two different answers:

       --ks3-nav-h     the sticky header alone. `.ks3-railbar` sits AT this,
                       so that a bar which now genuinely sticks (audit 3.15)
                       sticks below the header rather than under it.
       --ks3-sticky-h  everything sticky stacked. What an anchor has to clear.

     A bar is only counted if it is really sticky and really visible: below
     1340px the rail is the top bar, above it the side rail is `position:
     fixed` and the bar is `display: none`, and measuring a hidden element's
     height would push every anchor 47px too far on desktop.

     Degrades rather than fails: without `ResizeObserver` the CSS fallbacks
     stand, which are the generous ones — landing a heading 30px low is a
     blemish and landing it behind the header is a broken link. */
  function wireStickyHeight() {
    var root = document.documentElement;
    var nav = document.querySelector("header.ks3-nav");
    if (!nav) { return; }
    var bar = document.querySelector(".ks3-railbar");

    function sticks(el) {
      if (!el) { return false; }
      var cs = window.getComputedStyle(el);
      if (cs.position !== "sticky" && cs.position !== "fixed") { return false; }
      return el.getBoundingClientRect().height > 0;
    }

    function measure() {
      var navH = nav.getBoundingClientRect().height;
      var total = navH + (sticks(bar) ? bar.getBoundingClientRect().height : 0);
      root.style.setProperty("--ks3-nav-h", navH.toFixed(2) + "px");
      root.style.setProperty("--ks3-sticky-h", total.toFixed(2) + "px");
    }

    measure();
    if (!window.ResizeObserver) {
      // No observer: still better than the old constant, and still live for
      // the one event that changes the header most — a rotation or a resize.
      window.addEventListener("resize", measure);
      return;
    }
    var ro = new ResizeObserver(measure);
    ro.observe(nav);
    // The bar's height is fixed but WHETHER IT COUNTS is not: crossing 1340px
    // swaps the rail variant, and `.ks3-rails` is `display: contents` so the
    // bar itself is what changes. Observing it is how the swap is noticed
    // without polling.
    if (bar) { ro.observe(bar); }
  }

  /* ⊕ MRB-254 — DOES THIS FIGURE ACTUALLY CONTINUE OFF THE EDGE?

     Audit 3.9 asked for an edge fade so that a figure cut off at 390px does
     not read as a finished one. It shipped as `@media (max-width: 747px)`,
     which is the right cue hung on a number derived from the only figure that
     existed: 760 units wide, in a column 48px narrower than the viewport.

     Fourteen more figures arrive at 860 and 900 units wide and there is no
     number that is right for all of them. A 900px plate overflows to a 948px
     viewport; the media query stops drawing the cue at 747. Between those two
     the figure ends in a hard edge and says nothing about it — which is the
     defect, not a version of the fix.

     So this measures. `scrollWidth > clientWidth` is the exact question the
     breakpoint was approximating, it is free to ask, and it cannot drift from
     the figure's width, the column's padding or the reader's zoom, because all
     three are already inside the two numbers being compared.

     ⚠️ `ResizeObserver`, not `resize`. The box changes width when the RAIL
     swaps variant at 1340px and when a font loads late, neither of which fires
     a window resize. Falls back to `resize` where the observer is missing, and
     to no cue at all where JavaScript is off — see the note in ks3.css for why
     that is the safe direction to fail in. */
  function wireFigureCues(root) {
    var boxes = root.querySelectorAll(".ks3-figure-scroll");
    if (!boxes.length) { return; }

    function measure() {
      each(boxes, function (box) {
        // A 1px tolerance: sub-pixel layout can leave scrollWidth a fraction
        // above clientWidth on a figure that fits exactly, and a fade drawn
        // over nothing is the failure the old rule had at the other end.
        var over = box.scrollWidth - box.clientWidth > 1;
        if (over) {
          box.classList.add("is-overflowing");
        } else {
          box.classList.remove("is-overflowing");
        }
      });
    }

    measure();
    if (!window.ResizeObserver) {
      window.addEventListener("resize", measure);
      return;
    }
    var ro = new ResizeObserver(measure);
    each(boxes, function (box) { ro.observe(box); });
  }

  function init() {
    wireStickyHeight();
    wireFigureCues(document);
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
