/* ═══════════════════════════════════════════════════════════════════════
   breakdown.js — the Answer Breakdown panel (Mide's item 9, 24 Sep 2026).
   Self-contained, patched in place, mounted on <body> where the compiled
   runtime cannot reach it — the same reason `shared/set-work.js` lives
   outside; read that file's header before changing this one.

   Surface:  window.MRBBreakdown.open({classId, studentId, submissionId})
             .close()

   ── WHY IT IS NOT A COMPILED COMPONENT ──────────────────────────────────

   `shared/student-runtime.js`'s `draw()` empties the WHOLE `#mrb-teacher`
   mount host and rebuilds it from scratch on every `setState`. Prev/Next
   inside this panel re-populate the panel's OWN content in place — the same
   discipline set-work.js keeps for its own selections — so a compiled node
   would be torn down under the panel the moment anything on the page BEHIND
   it re-rendered (a background poll, a roster edit). Appended to
   `document.body`, a SIBLING of the mount host, `draw()` can never reach it.

   ── WHAT IT LOADS, AND WHY IT IS THIS FEW ROUND TRIPS ───────────────────

   One open() does, at most: the class (key stage), the roster (for
   Prev/Next, in surname order), the assignment, its questions
   (`assignment_questions`), EVERY pupil's submission for that one
   assignment, and EVERY attempt on those submissions — ONE read each,
   regardless of roster size. Prev/Next NEVER re-fetch: every pupil's
   submission and every attempt for the whole class is already in memory
   after open(), so paging through a class of thirty costs zero network
   calls. The bank is read once more, ONLY for the figure ids the fetched
   attempts actually name — never for the stem or the options, which the
   attempts already snapshot (`assignment_question_attempts.question_text` /
   `selected_answer` / `correct_answer` are what the pupil actually saw;
   see `supabase/migrations/20260818231201_assignment_questions.sql`).

   ⚠️ A PUPIL WHO NEVER ANSWERED A QUESTION HAS NO ATTEMPT ROW FOR IT, SO
   THIS PANEL BORROWS A CLASSMATE'S. Every pupil in a class is served the
   SAME composed set for one assignment, so another pupil's attempt at the
   same `question_index` names the same stem, the same `question_ref` and
   the same correct answer — it is read for THOSE THREE FIELDS ONLY, never
   for what that other child answered. If literally nobody in the class has
   reached a question yet there is nothing to borrow, and the row says so
   rather than guessing.

   ── FIGURES ──────────────────────────────────────────────────────────────

   Resolved exactly the way the pupil's own assignment page resolves them:
   `question_ref` -> the bank row -> its `figure` id -> `window.MRBFigures`,
   loaded from `/shared/figures-ks3.js` or `figures-ks4.js` by the class's
   key stage. Copied from `shared/set-work.js`'s `loadFigures`/`drawFigure`
   verbatim in shape: the only innerHTML sink in this file, fed exclusively
   from the manifest, never from a stem or an option. An id the manifest
   cannot resolve draws nothing, the same rule the "fig" node in
   student-runtime.js and set-work.js both keep.

   ── RIGHT / WRONG, NEVER BY COLOUR ALONE ────────────────────────────────

   A tick, a cross or a ring — three different SHAPES — carry the state;
   colour is the second signal, not the first. Same rule as the marking
   grid's `cellStyle` in teacher_rulings.py, and the same reason: a mark
   that is only a colour is invisible to a teacher who cannot tell red from
   green apart, on the exact page whose whole job is telling them apart.

   ── KEYBOARD ─────────────────────────────────────────────────────────────

   Esc closes. Left/Right arrow (outside a form field) is Prev/Next, mirrors
   the two on-screen buttons, and Tab is trapped inside the sheet — same
   idiom as set-work.js. The one `focus()` call is at OPEN, never after a
   state change (set-work.js's RISKS A1, kept here on purpose: focusing the
   sheet after every Prev/Next would fight a teacher tabbing through it).
   ═══════════════════════════════════════════════════════════════════════ */
(function () {
  "use strict";

  function el(tag, cls, text) {
    var e = document.createElement(tag);
    if (cls) { e.className = cls; }
    if (text != null) { e.textContent = text; }
    return e;
  }
  function btn(cls) {
    var b = document.createElement("button");
    b.type = "button";
    if (cls) { b.className = cls; }
    return b;
  }

  function client() {
    var g = window.MrBadmusTeacherGuard;
    return (g && g.getClient) ? g.getClient() : null;
  }

  function fullName(first, last) {
    var n = [first, last].filter(Boolean).join(" ");
    return n || "This student";
  }

  /* 'the-gas-exchange-system' -> 'The gas exchange system'. Same faithful
     reading `shared/student-live.js`'s `deslug` gives a lesson slug — the
     slug is the only readable name a `source_ref` carries here. */
  function deslug(slug) {
    if (!slug) { return ""; }
    var words = String(slug).split("-").filter(Boolean).join(" ");
    return words.charAt(0).toUpperCase() + words.slice(1);
  }

  function fmtDateTime(iso) {
    if (!iso) { return ""; }
    var d = new Date(iso);
    if (isNaN(d.getTime())) { return ""; }
    try {
      return d.toLocaleString("en-GB", {
        day: "numeric", month: "short", year: "numeric",
        hour: "2-digit", minute: "2-digit"
      });
    } catch (e) { return d.toISOString(); }
  }
  function fmtDate(iso) {
    if (!iso) { return ""; }
    var d = new Date(iso);
    if (isNaN(d.getTime())) { return ""; }
    try {
      return d.toLocaleDateString("en-GB", { day: "numeric", month: "short", year: "numeric" });
    } catch (e) { return d.toISOString().slice(0, 10); }
  }
  /* Never renders "0s" — the brief's own rule. A zero or negative span is
     "nothing worth reporting", not "instant". */
  function fmtDuration(seconds) {
    if (seconds == null || !isFinite(seconds) || seconds <= 0) { return null; }
    var m = Math.floor(seconds / 60), s = Math.round(seconds % 60);
    if (m <= 0) { return s + "s"; }
    if (s === 0) { return m + "m"; }
    return m + "m " + s + "s";
  }

  /* ═════════════════════════════════════════════════════════════════════
     FIGURES — copied in shape from shared/set-work.js's loadFigures /
     drawFigure. See the file header.
     ═════════════════════════════════════════════════════════════════════ */
  var figureLoads = {};
  function loadFigures(keyStage) {
    var name = (keyStage === "KS4") ? "figures-ks4.js" : "figures-ks3.js";
    if (figureLoads[name]) { return figureLoads[name]; }
    var map = window.__MRB_ASSET_V__;
    var v = map && map[name];
    if (!v) {
      figureLoads[name] = Promise.resolve(false);
      return figureLoads[name];
    }
    figureLoads[name] = new Promise(function (resolve) {
      var s = document.createElement("script");
      s.src = "/shared/" + name + "?v=" + v;
      s.onload = function () { resolve(true); };
      s.onerror = function () { resolve(false); };
      document.head.appendChild(s);
    });
    return figureLoads[name];
  }
  function figureNode(id) {
    var figs = window.MRBFigures;
    var rec = (id && typeof id === "string" && figs) ? figs[id] : null;
    if (!rec || typeof rec.svg !== "string") { return null; }
    var wrap = el("div", "bd-q-fig");
    wrap.innerHTML = rec.svg;
    var svg = wrap.firstElementChild;
    if (svg && rec.w) { svg.style.maxWidth = rec.w + "px"; }
    return wrap;
  }

  /* ═════════════════════════════════════════════════════════════════════
     DATA — one read per shape, never per pupil. All plain function
     expressions (no arrows) to match set-work.js's own style in this file
     family.
     ═════════════════════════════════════════════════════════════════════ */
  function bankTable(keyStage) {
    return keyStage === "KS4" ? "ks4_assignment_bank" : "ks3_assignment_bank";
  }

  async function loadClass(sb, classId) {
    var r = await sb.from("classes")
      .select("id, name, key_stage, science_pathway, tier")
      .eq("id", classId).limit(1);
    if (r.error || !r.data || !r.data.length) {
      throw new Error("breakdown: class unavailable");
    }
    return r.data[0];
  }

  /* Surname order — a register's own order — for Prev/Next. */
  async function loadRoster(sb, classId) {
    var r = await sb.from("class_members")
      .select("student_id, left_at, student:student_id(id, first_name, last_name, deleted_at)")
      .eq("class_id", classId)
      .is("deleted_at", null);
    if (r.error) { throw new Error("breakdown: roster unavailable"); }
    var rows = (r.data || []).filter(function (m) {
      return m.left_at == null && m.student && !m.student.deleted_at;
    });
    rows.sort(function (a, b) {
      var an = ((a.student.last_name || "") + " " + (a.student.first_name || "")).toLowerCase();
      var bn = ((b.student.last_name || "") + " " + (b.student.first_name || "")).toLowerCase();
      return an < bn ? -1 : (an > bn ? 1 : 0);
    });
    return rows.map(function (m) {
      return { id: m.student.id, name: fullName(m.student.first_name, m.student.last_name) };
    });
  }

  async function loadOneSubmission(sb, submissionId) {
    var r = await sb.from("assignment_submissions")
      .select("id, assignment_id, student_id")
      .eq("id", submissionId).limit(1);
    if (r.error || !r.data || !r.data.length) { return null; }
    return r.data[0];
  }

  async function loadAssignment(sb, assignmentId) {
    var r = await sb.from("assignments")
      .select("id, title, due_at, release_at, class_id")
      .eq("id", assignmentId).limit(1);
    if (r.error || !r.data || !r.data.length) {
      throw new Error("breakdown: set unavailable");
    }
    return r.data[0];
  }

  async function loadQuestions(sb, assignmentId) {
    var r = await sb.from("assignment_questions")
      .select("id, position, source_ref")
      .eq("assignment_id", assignmentId)
      .order("position", { ascending: true });
    if (r.error) { throw new Error("breakdown: questions unavailable"); }
    return r.data || [];
  }

  /* EVERY pupil's submission for this one assignment — the read that lets
     Prev/Next stay free, and the read "most of the class got this wrong"
     is computed from. */
  async function loadSubmissions(sb, assignmentId) {
    var r = await sb.from("assignment_submissions")
      .select("id, student_id, score, max_score, status, completed_at, " +
              "submitted_at, is_late, total_time_seconds")
      .eq("assignment_id", assignmentId)
      .is("deleted_at", null);
    if (r.error) { throw new Error("breakdown: submissions unavailable"); }
    return r.data || [];
  }

  /* EVERY attempt on those submissions — ONE read for the whole assignment,
     per the brief. */
  async function loadAllAttempts(sb, submissionIds) {
    if (!submissionIds.length) { return []; }
    var r = await sb.from("assignment_question_attempts")
      .select("submission_id, question_index, question_text, selected_answer, " +
              "correct_answer, is_correct, time_spent_seconds, attempt_number, " +
              "created_at, question_ref, selected_option_letter, " +
              "correct_option_letter, rung, criteria_met, criteria_total")
      .in("submission_id", submissionIds);
    if (r.error) { throw new Error("breakdown: attempts unavailable"); }
    return r.data || [];
  }

  /* Only for the figure id — the stem and the answers already came off the
     attempt rows. `ks4_assignment_bank.figure` is additive/nullable and, as
     of 24 Sep 2026, rehearsed on TEST only (MRB-352) — so a project that
     does not have the column yet gets everything else rather than nothing. */
  async function loadBankRows(sb, keyStage, ids) {
    if (!ids.length) { return {}; }
    var table = bankTable(keyStage);
    function indexBy(rows) {
      var out = {};
      (rows || []).forEach(function (row) { out[row.id] = row; });
      return out;
    }
    var r = await sb.from(table).select("id, figure").in("id", ids);
    if (!r.error) { return indexBy(r.data); }
    if (keyStage === "KS4") {
      var r2 = await sb.from(table).select("id").in("id", ids);
      if (!r2.error) { return indexBy(r2.data); }
    }
    console.error("[breakdown] bank read failed; figures will not draw", r.error);
    return {};
  }

  /* ═════════════════════════════════════════════════════════════════════
     STATUS — the same four words CLAUDE.md's Set-work-era definitions use
     on the student page history and the class roster dot: Complete
     (+ "· late"), In progress, Not started, Missing.
     ═════════════════════════════════════════════════════════════════════ */
  function paperClosed(assignment) {
    return !!(assignment.due_at && Date.parse(assignment.due_at) <= Date.now());
  }
  function completedIso(sub) {
    return (sub && (sub.completed_at || sub.submitted_at)) || null;
  }
  function isComplete(sub) {
    return !!(sub && (completedIso(sub) || sub.status === "complete"));
  }
  function lateness(sub, assignment) {
    if (!sub) { return null; }
    if (sub.is_late === true) { return true; }
    if (sub.is_late === false) { return false; }
    var done = completedIso(sub);
    if (done && assignment.due_at) { return Date.parse(done) > Date.parse(assignment.due_at); }
    return null;
  }
  function statusWord(sub, assignment) {
    if (isComplete(sub)) {
      var late = lateness(sub, assignment);
      return { word: "Complete" + (late === true ? " · late" : ""),
               tone: late === true ? "late" : "good" };
    }
    if (paperClosed(assignment)) { return { word: "Missing", tone: "late" }; }
    return { word: sub ? "In progress" : "Not started", tone: "muted" };
  }

  /* ═════════════════════════════════════════════════════════════════════
     THE SHELL
     ═════════════════════════════════════════════════════════════════════ */
  var els = null, opener = null, session = 0, opens = 0, S = null;
  var toastTimer = null;

  function buildShell() {
    if (els) { return; }
    var overlay = el("div", "bd-overlay");
    overlay.hidden = true;
    overlay.setAttribute("data-bd", "overlay");

    var sheet = el("div", "bd-sheet");
    sheet.setAttribute("role", "dialog");
    sheet.setAttribute("aria-modal", "true");
    sheet.setAttribute("aria-label", "Answer breakdown");
    sheet.tabIndex = -1;
    sheet.setAttribute("data-bd", "sheet");

    var head = el("div", "bd-head");
    var close = btn("bd-close");
    close.setAttribute("aria-label", "Close");
    close.setAttribute("data-mrb-added", "breakdown-close");
    close.innerHTML = '<svg width="16" height="16" viewBox="0 0 16 16" fill="none" ' +
      'aria-hidden="true"><path d="M3 3l10 10M13 3L3 13" stroke="currentColor" ' +
      'stroke-width="1.6" stroke-linecap="round"/></svg>';

    var main = el("div", "bd-head-main");
    var eyebrow = el("div", "bd-eyebrow");
    var title = el("div", "bd-title");
    var subtitle = el("div", "bd-subtitle");
    main.appendChild(eyebrow); main.appendChild(title); main.appendChild(subtitle);

    var nav = el("div", "bd-nav");
    var prev = btn("bd-nav-btn");
    prev.setAttribute("data-mrb-added", "breakdown-prev");
    prev.innerHTML = '<svg width="14" height="14" viewBox="0 0 14 14" fill="none" ' +
      'aria-hidden="true"><path d="M8.5 2.5L4 7l4.5 4.5" stroke="currentColor" ' +
      'stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>' +
      '<span class="bd-nav-word"></span>';
    var next = btn("bd-nav-btn");
    next.setAttribute("data-mrb-added", "breakdown-next");
    next.innerHTML = '<span class="bd-nav-word"></span>' +
      '<svg width="14" height="14" viewBox="0 0 14 14" fill="none" aria-hidden="true">' +
      '<path d="M5.5 2.5L10 7l-4.5 4.5" stroke="currentColor" stroke-width="1.6" ' +
      'stroke-linecap="round" stroke-linejoin="round"/></svg>';
    nav.appendChild(prev); nav.appendChild(next);

    head.appendChild(close); head.appendChild(main); head.appendChild(nav);

    var body = el("div", "bd-body");
    sheet.appendChild(head); sheet.appendChild(body);
    overlay.appendChild(sheet);

    var toastEl = el("div", "bd-toast");
    toastEl.setAttribute("role", "status");
    toastEl.hidden = true;

    /* Appended to <body>, not into #mrb-teacher — see the file header. */
    document.body.appendChild(overlay);
    document.body.appendChild(toastEl);

    els = {
      overlay: overlay, sheet: sheet, close: close,
      eyebrow: eyebrow, title: title, subtitle: subtitle,
      prev: prev, next: next, body: body, toast: toastEl
    };
    wireShell();
  }

  var FOCUSABLE = "button,[href],input,select,textarea,[tabindex]";
  function focusables() {
    var all = els.sheet.querySelectorAll(FOCUSABLE), out = [];
    for (var i = 0; i < all.length; i++) {
      var n = all[i];
      if (n.disabled) { continue; }
      if (n.getAttribute("tabindex") === "-1") { continue; }
      if (!n.offsetParent && n !== els.sheet) { continue; }
      out.push(n);
    }
    return out;
  }

  function isTypingTarget(t) {
    var tag = t && t.tagName && t.tagName.toLowerCase();
    return tag === "input" || tag === "textarea" || tag === "select" ||
           !!(t && t.isContentEditable);
  }

  function pushToast(msg) {
    if (!els) { return; }
    els.toast.textContent = msg;
    els.toast.hidden = false;
    if (toastTimer) { clearTimeout(toastTimer); }
    toastTimer = setTimeout(function () { if (els) { els.toast.hidden = true; } }, 3200);
  }

  function wireShell() {
    els.overlay.addEventListener("click", function (e) {
      if (e.target === els.overlay) { close(); }
    });
    els.close.addEventListener("click", close);
    els.prev.addEventListener("click", function () { go(-1); });
    els.next.addEventListener("click", function () { go(1); });
    document.addEventListener("keydown", function (e) {
      if (!S || els.overlay.hidden) { return; }
      if (e.key === "Escape") { close(); return; }
      if (isTypingTarget(e.target)) {
        if (e.key !== "Tab") { return; }
      } else if (e.key === "ArrowLeft") { e.preventDefault(); go(-1); return; }
      else if (e.key === "ArrowRight") { e.preventDefault(); go(1); return; }
      if (e.key !== "Tab") { return; }
      var items = focusables();
      if (!items.length) { return; }
      var first = items[0], last = items[items.length - 1];
      var here = document.activeElement;
      if (e.shiftKey && (here === first || !els.sheet.contains(here))) {
        e.preventDefault(); last.focus();
      } else if (!e.shiftKey && (here === last || !els.sheet.contains(here))) {
        e.preventDefault(); first.focus();
      }
    });
  }

  function close() {
    if (!els) { return; }
    session += 1;
    els.overlay.hidden = true;
    S = null;
    if (opener && opener.focus) {
      try { opener.focus({ preventScroll: true }); } catch (e) { /* gone */ }
    }
    opener = null;
  }

  /* ═════════════════════════════════════════════════════════════════════
     RENDER
     ═════════════════════════════════════════════════════════════════════ */
  function statTile(label, value, sub) {
    var d = el("div", "bd-stat");
    d.appendChild(el("div", "bd-stat-label", label));
    var v = el("div", "bd-stat-value", value);
    d.appendChild(v);
    if (sub) { d.appendChild(el("div", "bd-stat-sub", sub)); }
    return { node: d, valueNode: v };
  }

  function timeTakenFor(sub, myAttempts) {
    if (sub && sub.total_time_seconds != null && sub.total_time_seconds > 0) {
      return { seconds: sub.total_time_seconds, derived: false };
    }
    if (myAttempts.length >= 2) {
      var times = [];
      myAttempts.forEach(function (a) {
        var t = Date.parse(a.created_at);
        if (!isNaN(t)) { times.push(t); }
      });
      if (times.length >= 2) {
        var span = (Math.max.apply(null, times) - Math.min.apply(null, times)) / 1000;
        if (span > 0) { return { seconds: span, derived: true }; }
      }
    }
    return null;
  }

  function buildSummary(sub, myAttempts) {
    var wrap = el("div", "bd-summary");
    var st = statusWord(sub, S.assignment);

    wrap.appendChild(statTile(
      "SCORE",
      (sub && sub.score != null && sub.max_score != null)
        ? (sub.score + " / " + sub.max_score) : "—",
      (sub && sub.score != null && sub.max_score > 0)
        ? Math.round((sub.score / sub.max_score) * 100) + "%" : null
    ).node);

    var t = timeTakenFor(sub, myAttempts);
    wrap.appendChild(statTile(
      "TIME TAKEN",
      t ? fmtDuration(t.seconds) : "—",
      t && t.derived ? "Estimated from answer times" : null
    ).node);

    wrap.appendChild(statTile(
      "COMPLETION",
      myAttempts.length + " / " + S.questions.length + " answered",
      null
    ).node);

    var statusTile = statTile(
      "STATUS", st.word,
      S.assignment.due_at ? "Due " + fmtDate(S.assignment.due_at) : "No due date"
    );
    if (st.tone === "late") { statusTile.valueNode.classList.add("is-late"); }
    if (st.tone === "good") { statusTile.valueNode.classList.add("is-good"); }
    wrap.appendChild(statusTile.node);

    return wrap;
  }

  function topicTitle(sourceRef) {
    if (!sourceRef) { return "This set"; }
    var parts = String(sourceRef).split("/");
    return deslug(parts[parts.length - 1]) || sourceRef;
  }

  function computeGroups(myAttempts) {
    var myByQ = {};
    myAttempts.forEach(function (a) { myByQ[a.question_index] = a; });
    var order = [], byKey = {};
    S.questions.forEach(function (q) {
      var qi = q.position - 1;
      var mine = myByQ[qi] || null;
      var classList = S.byQ[qi] || [];
      var rep = mine || classList[0] || null;
      var key = q.source_ref || ("§" + qi);
      var g = byKey[key];
      if (!g) {
        g = { key: key, title: topicTitle(q.source_ref), rows: [], right: 0, total: 0 };
        byKey[key] = g;
        order.push(g);
      }
      var wrongCount = 0, answeredByClass = 0;
      classList.forEach(function (a) {
        if (a.is_correct === true || a.is_correct === false) { answeredByClass += 1; }
        if (a.is_correct === false) { wrongCount += 1; }
      });
      var classFlag = answeredByClass >= 3 && (wrongCount / answeredByClass) >= 0.5;
      var bank = (rep && rep.question_ref) ? S.bankById[rep.question_ref] : null;

      g.total += 1;
      if (mine && mine.is_correct === true) { g.right += 1; }

      g.rows.push({
        position: q.position,
        stem: (rep && rep.question_text) || null,
        figure: bank ? bank.figure : null,
        answered: !!mine,
        pupilAnswer: mine ? mine.selected_answer : null,
        correctAnswer: mine ? mine.correct_answer : (rep ? rep.correct_answer : null),
        isCorrect: mine ? mine.is_correct : null,
        attemptNumber: mine ? mine.attempt_number : null,
        timeSpent: mine ? mine.time_spent_seconds : null,
        criteriaMet: mine ? mine.criteria_met : null,
        criteriaTotal: mine ? mine.criteria_total : null,
        classFlag: classFlag
      });
    });
    return order;
  }

  function buildQuestionRow(row) {
    var markState = row.answered
      ? (row.isCorrect === true ? "right" : (row.isCorrect === false ? "wrong" : "unscored"))
      : "unscored";
    var card = el("div", "bd-q" +
      (markState === "right" ? " is-right" : (markState === "wrong" ? " is-wrong" : "")));

    var mark = el("div", "bd-q-mark is-" + markState);
    mark.setAttribute("aria-hidden", "true");
    mark.innerHTML = markState === "right"
      ? '<svg viewBox="0 0 20 20" fill="none"><path d="M4 10.5l4 4 8-9" ' +
        'stroke="currentColor" stroke-width="2.2" stroke-linecap="round" ' +
        'stroke-linejoin="round"/></svg>'
      : (markState === "wrong"
        ? '<svg viewBox="0 0 20 20" fill="none"><path d="M5 5l10 10M15 5L5 15" ' +
          'stroke="currentColor" stroke-width="2.2" stroke-linecap="round"/></svg>'
        : '<svg viewBox="0 0 20 20" fill="none"><circle cx="10" cy="10" r="6.4" ' +
          'stroke="currentColor" stroke-width="1.8"/></svg>');
    card.appendChild(mark);

    var head = el("div", "bd-q-head");
    head.appendChild(el("div", "bd-q-num", "Question " + row.position));
    var metaBits = [];
    /* Attempt 1 is the ordinary case and says nothing; a retry is the
       interesting fact, and the brief's own rule is "omit quietly when
       null" — a retry that never happened is not worth a line either. */
    if (row.attemptNumber != null && row.attemptNumber > 1) {
      metaBits.push("Attempt " + row.attemptNumber);
    }
    var dur = fmtDuration(row.timeSpent);
    if (dur) { metaBits.push(dur); }
    if (metaBits.length) { head.appendChild(el("div", "bd-q-meta", metaBits.join(" · "))); }
    card.appendChild(head);

    card.appendChild(el("div", "bd-q-stem",
      row.stem || ("Question " + row.position + " — not yet available")));

    var fig = row.figure ? figureNode(row.figure) : null;
    if (fig) { card.appendChild(fig); }

    var answers = el("div", "bd-q-answers");
    if (!row.answered) {
      var a1 = el("div", "bd-q-answer is-missing");
      a1.appendChild(el("div", "bd-q-answer-label", "Pupil's answer"));
      a1.appendChild(el("div", "bd-q-answer-text", "No answer given"));
      answers.appendChild(a1);
    } else {
      var pupilCls = row.isCorrect === true ? " is-pupil-right"
        : (row.isCorrect === false ? " is-pupil-wrong" : "");
      var a2 = el("div", "bd-q-answer" + pupilCls);
      a2.appendChild(el("div", "bd-q-answer-label", "Pupil's answer"));
      a2.appendChild(el("div", "bd-q-answer-text", row.pupilAnswer || "—"));
      answers.appendChild(a2);
    }
    if (row.isCorrect === false && row.correctAnswer) {
      var a3 = el("div", "bd-q-answer is-pupil-right");
      a3.appendChild(el("div", "bd-q-answer-label", "Correct answer"));
      a3.appendChild(el("div", "bd-q-answer-text", row.correctAnswer));
      answers.appendChild(a3);
    }
    if (row.criteriaTotal != null) {
      var a4 = el("div", "bd-q-answer");
      a4.appendChild(el("div", "bd-q-answer-label", "Self-marked"));
      a4.appendChild(el("div", "bd-q-answer-text",
        (row.criteriaMet == null ? "—" : row.criteriaMet) +
        " of " + row.criteriaTotal + " criteria met"));
      answers.appendChild(a4);
    }
    card.appendChild(answers);

    if (row.classFlag) {
      var foot = el("div", "bd-q-foot");
      foot.appendChild(el("span", "bd-q-tag is-classflag", "Most of the class got this wrong"));
      card.appendChild(foot);
    }
    return card;
  }

  function renderGroups(groups) {
    var container = el("div", "");
    if (!groups.length) {
      container.appendChild(el("div", "bd-empty", "No questions in this set."));
      return container;
    }
    groups.forEach(function (g) {
      var section = el("div", "bd-topic");
      var head = el("div", "bd-topic-head");
      head.appendChild(el("div", "bd-topic-name", g.title));
      head.appendChild(el("div", "bd-topic-tally", g.right + " of " + g.total + " right"));
      section.appendChild(head);
      var qlist = el("div", "bd-qlist");
      g.rows.forEach(function (row) { qlist.appendChild(buildQuestionRow(row)); });
      section.appendChild(qlist);
      container.appendChild(section);
    });
    return container;
  }

  /* ⊕ THE FOLLOW-UP BUTTON. Design drew no Set-work entry point on this
     panel — it does not exist yet — so this opens the SAME sheet
     `shared/set-work.js` owns, anchored on this class.

     ⚠️ NOT PRESELECTED ON THE MISSED TOPICS, AND THAT IS A NAMED GAP RATHER
     THAN A SILENT ONE. `MRBSetWork.open()` takes `{classId}` and has no
     `preselect`/scope-ref parameter today; adding one cleanly means
     touching `freshState()`, `loadScope()` and `syncTree()` inside a
     ~4,000-line, heavily-gated file this ticket did not have the budget to
     verify blind. The brief's own fallback is taken instead: open the
     sheet on the class, and say — in the toast, to the teacher pressing it
     — which topic to pick. */
  function buildFollowupRow(groups) {
    var missed = groups.filter(function (g) { return g.total > 0 && g.right < g.total; });
    var row = el("div", "bd-followup-row");
    var b = btn("bd-followup");
    b.textContent = "Set a follow-up on missed topics";
    b.setAttribute("data-mrb-added", "breakdown-followup");
    b.hidden = !missed.length;
    b.addEventListener("click", function () {
      if (!(window.MRBSetWork && window.MRBSetWork.open)) {
        pushToast("Set work isn't available on this page right now.");
        return;
      }
      window.MRBSetWork.open({ classId: S.classId });
      pushToast(missed.length === 1
        ? "Opened Set work — pick “" + missed[0].title + "” to follow up."
        : "Opened Set work — pick one of the " + missed.length +
          " missed topics to follow up.");
    });
    row.appendChild(b);
    return row;
  }

  function renderLoading() {
    els.eyebrow.textContent = "";
    els.title.textContent = "Loading…";
    els.subtitle.textContent = "";
    els.prev.disabled = true;
    els.next.disabled = true;
    els.body.textContent = "";
    els.body.appendChild(el("div", "bd-empty", "Loading this pupil's answers…"));
  }

  function renderError(msg) {
    els.title.textContent = "Answer breakdown";
    els.subtitle.textContent = "";
    els.prev.disabled = true;
    els.next.disabled = true;
    els.body.textContent = "";
    els.body.appendChild(el("div", "bd-empty", msg));
  }

  function render() {
    if (!S) { return; }
    var student = S.roster[S.idx];
    var sub = S.submissionsByStudent[student.id] || null;
    var myAttempts = sub ? (S.attemptsBySub[sub.id] || []) : [];

    els.prev.disabled = S.idx <= 0;
    els.next.disabled = S.idx >= S.roster.length - 1;
    var prevName = S.idx > 0 ? S.roster[S.idx - 1].name : "";
    var nextName = S.idx < S.roster.length - 1 ? S.roster[S.idx + 1].name : "";
    var prevWord = els.prev.querySelector(".bd-nav-word");
    var nextWord = els.next.querySelector(".bd-nav-word");
    if (prevWord) { prevWord.textContent = prevName; }
    if (nextWord) { nextWord.textContent = nextName; }
    els.prev.setAttribute("aria-label", "Previous pupil" + (prevName ? ": " + prevName : ""));
    els.next.setAttribute("aria-label", "Next pupil" + (nextName ? ": " + nextName : ""));

    els.eyebrow.textContent = S.assignment.title || "Set work";
    els.title.textContent = student.name;
    els.subtitle.textContent = S.assignment.due_at
      ? "Due " + fmtDateTime(S.assignment.due_at) : "No due date set";

    /* ⊕ READ BY `teacher_behaviour.py`'s `snap()`, the same instrument that
       already watches `shared/set-work.js`'s `[data-sw="overlay"]` — see
       that file's own note. Two attributes rather than one string: which
       pupil is on screen has to be legible on its own, because the sweep's
       generic "did the DOM change" diff cannot tell "re-opened, on a
       different pupil" apart from "re-opened, on the same one". */
    els.overlay.setAttribute("data-bd-student", student.id);

    els.body.textContent = "";
    els.body.appendChild(buildSummary(sub, myAttempts));
    var groups = computeGroups(myAttempts);
    els.body.appendChild(renderGroups(groups));
    els.body.appendChild(buildFollowupRow(groups));
  }

  function go(delta) {
    if (!S) { return; }
    var n = S.idx + delta;
    if (n < 0 || n >= S.roster.length) { return; }
    S.idx = n;
    render();
    els.sheet.scrollTop = 0;
  }

  /* ═════════════════════════════════════════════════════════════════════
     OPEN / CLOSE
     ═════════════════════════════════════════════════════════════════════ */
  async function open(opts) {
    var o = opts || {};
    buildShell();
    opener = (document.activeElement && document.activeElement !== document.body)
      ? document.activeElement : null;
    session += 1;
    var mySession = session;

    els.overlay.hidden = false;
    opens += 1;
    els.overlay.setAttribute("data-bd-opens", String(opens));
    /* The one focus() in this file, and it is at OPEN — never after a
       state change (set-work.js RISKS A1, kept here for the same reason:
       Prev/Next must not fight a teacher who is tabbing through the
       panel). */
    els.sheet.focus({ preventScroll: true });
    renderLoading();

    var sb = client();
    if (!sb) {
      renderError("This page is not signed in. Reload and try again.");
      return;
    }

    try {
      var klass = await loadClass(sb, o.classId);
      var roster = await loadRoster(sb, o.classId);

      var assignmentId = o.assignmentId || null;
      if (!assignmentId && o.submissionId) {
        var subRow = await loadOneSubmission(sb, o.submissionId);
        assignmentId = subRow && subRow.assignment_id;
      }
      if (!assignmentId) { throw new Error("breakdown: nothing to show"); }

      var assignment = await loadAssignment(sb, assignmentId);
      var questions = await loadQuestions(sb, assignmentId);
      var submissions = await loadSubmissions(sb, assignmentId);
      var subIds = submissions.map(function (s) { return s.id; });
      var attempts = await loadAllAttempts(sb, subIds);

      var byQ = {};
      attempts.forEach(function (a) {
        (byQ[a.question_index] = byQ[a.question_index] || []).push(a);
      });
      var refs = {};
      attempts.forEach(function (a) { if (a.question_ref) { refs[a.question_ref] = 1; } });
      var bankById = await loadBankRows(sb, klass.key_stage, Object.keys(refs));
      await loadFigures(klass.key_stage);

      if (mySession !== session) { return; }   // closed, or re-opened elsewhere

      var subById = {}, submissionsByStudent = {};
      submissions.forEach(function (s) {
        subById[s.id] = s;
        submissionsByStudent[s.student_id] = s;
      });
      var attemptsBySub = {};
      attempts.forEach(function (a) {
        (attemptsBySub[a.submission_id] = attemptsBySub[a.submission_id] || []).push(a);
      });

      var idx = 0;
      for (var i = 0; i < roster.length; i++) {
        if (roster[i].id === o.studentId) { idx = i; break; }
      }

      S = {
        classId: o.classId,
        keyStage: klass.key_stage,
        assignment: assignment,
        questions: questions,
        roster: roster,
        idx: idx,
        subById: subById,
        submissionsByStudent: submissionsByStudent,
        attemptsBySub: attemptsBySub,
        byQ: byQ,
        bankById: bankById
      };
      render();
    } catch (err) {
      if (mySession !== session) { return; }
      console.error("[breakdown]", err);
      renderError("Couldn't load this pupil's answers. Try again in a moment.");
    }
  }

  window.MRBBreakdown = { open: open, close: close };
})();
