/* ═══════════════════════════════════════════════════════════════════════
   breakdown.js — the Answer Breakdown panel (Mide's item 9, 24 Sep 2026).
   Self-contained, patched in place, mounted on <body> where the compiled
   runtime cannot reach it — the same reason `shared/set-work.js` lives
   outside; read that file's header before changing this one.

   Surface:  window.MRBBreakdown.open({classId, studentId, submissionId})
             .close()

   ⊕ 25 Sep 2026 — REWORKED against an Opus design critique. The eight MUST
   items are marked inline (MUST-1 … MUST-8); the SHOULD items are S1 … S13;
   COULD items taken are C1/C2/C3/C6 (C4, and the J/K half of C5, are
   named and skipped — see the notes at each).

   ── MUST-1, THE WORST ONE: NEVER FALL BACK TO PUPIL 1 ──────────────────
   `loadRoster` returns ACTIVE members only. A pupil whose submission a
   teacher is reviewing may since have left the class, or `o.studentId`
   may simply not match any active member for a reason nobody anticipated.
   The old code fell through to `idx = 0` — Lydia's answers under Kale's
   name, in the critique's own words "the worst failure this surface has".
   `open()` now fetches that one profile directly and splices a synthetic
   roster row into the surname-sorted position when the id is not found.
   It NEVER defaults to index 0 for a real id.

   ── MUST-2: ONE SUBMISSION PER PUPIL, THE SAME ONE EVERY OTHER SCREEN
      PICKS ──────────────────────────────────────────────────────────────
   `assignment_submissions_attempt_uniq` is a real unique index on
   (assignment_id, student_id, attempt_no) — a retake is a SECOND SUBMISSION
   ROW, not a second attempt row. `shared/teacher-data.js`'s
   `pickFirstAttempts` is the estate's one answer to "which of a pupil's
   submission rows counts": lowest `attempts` wins, tie-break on earliest
   `submitted_at` (a null — still in progress — treated as WORST, so a
   completed first attempt beats an in-progress retake). Reproduced here
   verbatim as `keepFirstAttempt`, because a second implementation is a
   second place the two could disagree. Once submissions are one-per-pupil,
   `assignment_question_attempts_question_uniq` (unique on submission_id,
   question_index) guarantees at most one row per question for that one
   submission — so COMPLETION and the class flag are correct by
   construction, with no further per-question de-duplication needed.

   ── MUST-3: A FIGURE NEVER OUTLIVES ITS QUESTION ────────────────────────
   The panel only ever draws `S.bankById[rep.question_ref].figure` — a
   direct, single lookup keyed by the bank's own identity column, so there
   is no path in this file that could pair a figure with the wrong stem.
   The mismatch the critique found was in `breakdown_shots.py`'s OWN canned
   test data, not in this file; see that script's header for how it was
   fixed and verified against a real TEST bank row read under a real
   teacher session (`hz_rich@test.mrbadmus`). `data-bd-qref`/`data-bd-figure`
   are stamped on every card so the harness can assert the pairing in code,
   not just by eye.

   ── MUST-4: NOTHING IS SILENTLY CUT OFF AT 1000 ROWS ────────────────────
   PostgREST caps a read at 1000 rows by default. Every multi-row read here
   — roster, submissions, questions, attempts — pages with `.range()` until
   a short page comes back (`fetchPaged`), ordered on a stable column so
   pagination cannot skip or repeat a row.

   ── S12: PARALLEL WHERE THEY CAN BE, DRAWN BEFORE THE FIGURES ARRIVE ────
   `open()` resolves the assignment id, then runs class/roster/assignment/
   questions/submissions together, then attempts (needs the submission
   ids), then renders text immediately — the bank read (figures only) and
   the figure manifest load happen AFTER that first paint and re-render
   once they land, never blocking it.
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
  function fmtDuration(seconds) {
    if (seconds == null || !isFinite(seconds) || seconds <= 0) { return null; }
    var m = Math.floor(seconds / 60), s = Math.round(seconds % 60);
    if (m <= 0) { return s + "s"; }
    if (s === 0) { return m + "m"; }
    return m + "m " + s + "s";
  }
  function ordinal(n) {
    var s = ["th", "st", "nd", "rd"], v = n % 100;
    return n + (s[(v - 20) % 10] || s[v] || s[0]);
  }
  /* "Q1, Q7 and Q12" — an Oxford-less list because a list of two items
     with a comma before "and" reads oddly ("Q1, and Q7"). */
  function joinList(words) {
    if (words.length <= 1) { return words.join(""); }
    return words.slice(0, -1).join(", ") + " and " + words[words.length - 1];
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
    return wrap;
  }

  /* ═════════════════════════════════════════════════════════════════════
     DATA — one shape per read, never per pupil. Plain function
     expressions (no arrows), matching set-work.js's own style.
     ═════════════════════════════════════════════════════════════════════ */
  function bankTable(keyStage) {
    return keyStage === "KS4" ? "ks4_assignment_bank" : "ks3_assignment_bank";
  }

  /* MUST-4 — pages a `.range()`-filterable query until a short page comes
     back. `build(from, to)` must return an ALREADY ordered, already
     filtered query for that page; ordering is what keeps a page stable
     across requests, which `.range()` alone does not guarantee. */
  var PAGE = 1000;
  async function fetchPaged(what, build) {
    var out = [], from = 0;
    for (;;) {
      var r = await build(from, from + PAGE - 1);
      if (r.error) { throw new Error("breakdown: " + what + " — " + r.error.message); }
      var rows = r.data || [];
      out = out.concat(rows);
      if (rows.length < PAGE) { break; }
      from += PAGE;
    }
    return out;
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

  /* "Adeyemi lydia" not "lydia Adeyemi" — a register's own order. Sorting
     on the DISPLAY name ("First Last") sorts on first name, which is not
     surname order at all; `sortKey` is surname-first specifically so a
     class of Lydia Adeyemi / Annabel Brooks reads Adeyemi, Brooks, …, not
     Annabel, Dan, …, Lydia. */
  function rosterSortKey(first, last) {
    return ((last || "") + " " + (first || "")).toLowerCase();
  }
  function rosterEntryCompare(a, b) {
    var ak = a.sortKey || "", bk = b.sortKey || "";
    return ak < bk ? -1 : (ak > bk ? 1 : 0);
  }

  /* Surname order — a register's own order — for Prev/Next. */
  async function loadRoster(sb, classId) {
    var rows = await fetchPaged("roster", function (from, to) {
      return sb.from("class_members")
        .select("student_id, left_at, student:student_id(id, first_name, last_name, deleted_at)")
        .eq("class_id", classId)
        .is("deleted_at", null)
        .order("student_id", { ascending: true })
        .range(from, to);
    });
    var active = rows.filter(function (m) {
      return m.left_at == null && m.student && !m.student.deleted_at;
    });
    var out = active.map(function (m) {
      return {
        id: m.student.id,
        name: fullName(m.student.first_name, m.student.last_name),
        sortKey: rosterSortKey(m.student.first_name, m.student.last_name)
      };
    });
    out.sort(rosterEntryCompare);
    return out;
  }

  /* MUST-1 — the one pupil `loadRoster` did not return, fetched directly
     so the panel can still show their real name rather than "pupil 1". */
  async function loadOneProfile(sb, studentId) {
    var r = await sb.from("profiles")
      .select("id, first_name, last_name")
      .eq("id", studentId).limit(1);
    if (r.error || !r.data || !r.data.length) { return null; }
    return r.data[0];
  }

  async function loadOneSubmission(sb, submissionId) {
    var r = await sb.from("assignment_submissions")
      .select("id, assignment_id, student_id")
      .eq("id", submissionId).limit(1);
    if (r.error || !r.data || !r.data.length) { return null; }
    return r.data[0];
  }

  async function loadAssignment(sb, assignmentId) {
    /* ⊕ Stream J, 25 Sep 2026 (experience run, item 3) — `scope_kind`,
       `scope_ref` and `topic` added so `groupByTopic` has a real subtopic
       (or, failing that, a real topic/title) to fall back to when a KS4
       question's bank row cannot be read. Tried with the MRB-335 columns
       first; a project that has not carried that migration yet still gets
       everything else, the same guard `loadBankRows` already uses for
       `figure`. */
    var r = await sb.from("assignments")
      .select("id, title, topic, due_at, release_at, class_id, scope_kind, scope_ref")
      .eq("id", assignmentId).limit(1);
    if (r.error) {
      r = await sb.from("assignments")
        .select("id, title, due_at, release_at, class_id")
        .eq("id", assignmentId).limit(1);
    }
    if (r.error || !r.data || !r.data.length) {
      throw new Error("breakdown: set unavailable");
    }
    return r.data[0];
  }

  async function loadQuestions(sb, assignmentId) {
    return fetchPaged("questions", function (from, to) {
      return sb.from("assignment_questions")
        .select("id, position, source_ref")
        .eq("assignment_id", assignmentId)
        .order("position", { ascending: true })
        .range(from, to);
    });
  }

  /* EVERY pupil's submission ROW for this assignment — before dedup, so a
     retaking pupil can appear twice here. `keepFirstAttempt` below reduces
     it to one per student_id, the same rule the rest of the estate uses. */
  async function loadSubmissions(sb, assignmentId) {
    return fetchPaged("submissions", function (from, to) {
      return sb.from("assignment_submissions")
        .select("id, student_id, score, max_score, status, completed_at, " +
                "submitted_at, is_late, total_time_seconds, attempts, attempt_no")
        .eq("assignment_id", assignmentId)
        .is("deleted_at", null)
        .order("id", { ascending: true })
        .range(from, to);
    });
  }

  /* MUST-2 — `shared/teacher-data.js`'s `pickFirstAttempts`, reproduced
     verbatim (the sentinel, the tie-break, the "null is worst" rule) so
     this panel cannot pick a different pupil's "current" attempt than
     every other teacher screen does. */
  function keepFirstAttempt(submissions) {
    var bySid = {};
    submissions.forEach(function (s) {
      var key = s.student_id;
      var existing = bySid[key];
      if (!existing) { bySid[key] = s; return; }
      var exAtt = existing.attempts == null ? Number.MAX_SAFE_INTEGER : existing.attempts;
      var newAtt = s.attempts == null ? Number.MAX_SAFE_INTEGER : s.attempts;
      if (newAtt < exAtt) { bySid[key] = s; return; }
      if (newAtt === exAtt) {
        var exTs = existing.submitted_at || "￿";
        var newTs = s.submitted_at || "￿";
        if (newTs < exTs) { bySid[key] = s; }
      }
    });
    return bySid;
  }

  /* EVERY attempt on the CANONICAL submissions (post `keepFirstAttempt`) —
     one read for the whole assignment, per the brief. Restricted to
     canonical submission ids so a retaking pupil's abandoned first (or
     second) attempt cannot double-count in the class-wide flag. */
  async function loadAllAttempts(sb, submissionIds) {
    if (!submissionIds.length) { return []; }
    return fetchPaged("attempts", function (from, to) {
      return sb.from("assignment_question_attempts")
        .select("id, submission_id, question_index, question_text, selected_answer, " +
                "correct_answer, is_correct, time_spent_seconds, attempt_number, " +
                "created_at, question_ref, selected_option_letter, " +
                "correct_option_letter, rung, criteria_met, criteria_total")
        .in("submission_id", submissionIds)
        .order("id", { ascending: true })
        .range(from, to);
    });
  }

  /* Only for the figure id and the option list (S9's "C: the liver") — the
     stem and the pupil/correct answer text already came off the attempt
     rows. `ks4_assignment_bank.figure` is additive/nullable and, as of
     24 Sep 2026, rehearsed on TEST only (MRB-352) — so a project that does
     not have the column yet still gets everything else. */
  async function loadBankRows(sb, keyStage, ids) {
    if (!ids.length) { return {}; }
    var table = bankTable(keyStage);
    function indexBy(rows) {
      var out = {};
      (rows || []).forEach(function (row) { out[row.id] = row; });
      return out;
    }
    /* ⊕ Stream J, 25 Sep 2026 (experience run, item 3) — KS4 also reads
       `subtopic_slug`, the REAL subtopic a bank row was authored for
       (`ks4_assignment_bank_four_options`'s sibling column, NOT NULL since
       MRB-332's original table — unlike `figure`, it needs no TEST-only
       guard of its own). `groupByTopic` groups on this, never on the bank
       row's own `id` (a per-question id like `ks4-circuit-symbols-e03`,
       which is not a topic at all). */
    var cols = keyStage === "KS4" ? "id, figure, options, subtopic_slug" : "id, figure, options";
    var r = await sb.from(table).select(cols).in("id", ids);
    if (!r.error) { return indexBy(r.data); }
    if (keyStage === "KS4") {
      var r2 = await sb.from(table).select("id, options, subtopic_slug").in("id", ids);
      if (!r2.error) { return indexBy(r2.data); }
    }
    console.error("[breakdown] bank read failed; figures/option text will not draw", r.error);
    return {};
  }

  /* S9 — "C" -> the option text for C, when the bank carries it. KS3's
     `options` is `[{text,correct,why}]`; KS4's is a plain `text[]` — both
     positional, A=0..D=3, the same convention `LETTERS[option]` uses
     elsewhere in the estate (shared/student-live.js). Never throws: an
     unresolvable letter just means no augmentation, not a broken row. */
  function optionText(bankRow, letter) {
    if (!bankRow || !letter) { return null; }
    var idx = "ABCD".indexOf(String(letter).toUpperCase());
    if (idx < 0 || !bankRow.options || !bankRow.options[idx]) { return null; }
    var o = bankRow.options[idx];
    if (typeof o === "string") { return o; }
    if (o && typeof o.text === "string") { return o.text; }
    return null;
  }
  /* "C" (bare, from a lettered/figure question) -> "C: the liver". Leaves
     ordinary free-text answers ("Evaporating") alone. */
  function answerDisplay(text, letter, bankRow) {
    var bare = /^[A-D]$/i.test(String(text || "").trim());
    if (!bare && text) { return text; }
    var useLetter = bare ? String(text).trim().toUpperCase() : letter;
    if (!useLetter) { return text || null; }
    var opt = optionText(bankRow, useLetter);
    if (opt) { return useLetter + ": " + opt; }
    return text || useLetter || null;
  }

  /* ═════════════════════════════════════════════════════════════════════
     STATUS — the same four words CLAUDE.md's Set-work-era definitions use
     on the student page history and the class roster dot: Complete
     (+ late), In progress, Not started, Missing.
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
  function lateDays(sub, assignment) {
    var done = completedIso(sub);
    if (!done || !assignment.due_at) { return null; }
    var ms = Date.parse(done) - Date.parse(assignment.due_at);
    if (isNaN(ms) || ms <= 0) { return 0; }
    return Math.ceil(ms / 86400000);
  }
  function isLate(sub, assignment) {
    if (!sub) { return null; }
    if (sub.is_late === true) { return true; }
    if (sub.is_late === false) { return false; }
    var d = lateDays(sub, assignment);
    return d == null ? null : d > 0;
  }
  function statusWord(sub, assignment) {
    if (isComplete(sub)) {
      var late = isLate(sub, assignment);
      return { word: "Complete" + (late === true ? " · late" : ""), tone: late === true ? "late" : "good" };
    }
    if (paperClosed(assignment)) { return { word: "Missing", tone: "late" }; }
    return { word: sub ? "In progress" : "Not started", tone: "muted" };
  }

  /* ═════════════════════════════════════════════════════════════════════
     THE SHELL
     ═════════════════════════════════════════════════════════════════════ */
  var els = null, opener = null, session = 0, opens = 0, S = null;
  var toastTimer = null;
  var prevOverflow = null;

  function buildShell() {
    if (els) { return; }
    var overlay = el("div", "bd-overlay");
    overlay.hidden = true;
    overlay.setAttribute("data-bd", "overlay");

    var sheet = el("div", "bd-sheet");
    sheet.setAttribute("role", "dialog");
    sheet.setAttribute("aria-modal", "true");
    sheet.tabIndex = -1;
    sheet.setAttribute("data-bd", "sheet");

    var head = el("div", "bd-head");
    var close = btn("bd-close");
    close.setAttribute("aria-label", "Close");
    close.setAttribute("data-mrb-added", "breakdown-close");
    close.innerHTML = '<svg width="16" height="16" viewBox="0 0 16 16" fill="none" ' +
      'aria-hidden="true"><path d="M3 3l10 10M13 3L3 13" stroke="currentColor" ' +
      'stroke-width="1.6" stroke-linecap="round"/></svg>' +
      '<span class="bd-close-label">Close</span>';

    var main = el("div", "bd-head-main");
    /* S10/MUST-8 — the eyebrow now carries the SET TITLE and is what the
       dialog's accessible name points at (`aria-labelledby`), because the
       one thing that never changes across Previous/Next is the thing the
       panel's name should be. */
    var eyebrow = el("div", "bd-eyebrow");
    eyebrow.id = "bd-panel-heading";
    var title = el("div", "bd-title");
    var subtitle = el("div", "bd-subtitle");
    main.appendChild(eyebrow); main.appendChild(title); main.appendChild(subtitle);
    sheet.setAttribute("aria-labelledby", "bd-panel-heading");

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

    /* MUST-8 — announces "Pupil 3 of 28: <name>" on every Previous/Next.
       Visually hidden; the sighted header already says the same thing in
       the subtitle (S10). */
    var live = el("div", "bd-sr");
    live.setAttribute("aria-live", "polite");
    live.setAttribute("data-bd", "live");

    sheet.appendChild(head); sheet.appendChild(body); sheet.appendChild(live);
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
      prev: prev, next: next, body: body, toast: toastEl, live: live
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
    /* S11 — the page behind the panel stops scrolling while it is open;
       restore whatever the document had before (never assume "visible"). */
    if (prevOverflow != null) {
      document.documentElement.style.overflow = prevOverflow;
      prevOverflow = null;
    }
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

  /* S1/S2/S3 — three tiles: Score, Time taken, Handed in. Completion moved
     to the question map below; "Handed in" absorbs the old Status tile and
     says the hand-in time in words instead of repeating the header's due
     date over the word "Complete". */
  function buildSummary(sub, myAttempts) {
    var wrap = el("div", "bd-summary");
    var complete = isComplete(sub);

    var totalQ = S.questions.length;
    var correctSoFar = myAttempts.filter(function (a) { return a.is_correct === true; }).length;
    var scoreTile;
    if (complete && sub.score != null && sub.max_score != null) {
      scoreTile = statTile("SCORE", sub.score + " / " + sub.max_score,
        sub.max_score > 0 ? Math.round((sub.score / sub.max_score) * 100) + "%" : null);
    } else {
      /* S3 — never mislead an in-progress pupil with a 0% over one answer.
         Always the SET's own question count as the denominator, no
         percentage until they have hand something in. */
      scoreTile = statTile("SCORE", correctSoFar + " of " + totalQ,
        myAttempts.length ? myAttempts.length + " answered so far" : null);
    }
    wrap.appendChild(scoreTile.node);

    var t = timeTakenFor(sub, myAttempts);
    /* Wording check — "Estimated from answer times" is a tooltip on the
       value, not a permanent sub-line, once it is derived rather than
       measured. */
    var timeTile = statTile("TIME TAKEN", t ? fmtDuration(t.seconds) : "—",
      (!t || !t.derived) ? null : null);
    if (t && t.derived) { timeTile.valueNode.title = "Estimated from answer times"; }
    wrap.appendChild(timeTile.node);

    /* S2 — say "On time"/"Late: N days" in words, with the hand-in moment
       underneath; a due date the header already states is not repeated. */
    var handedTile;
    if (complete) {
      var late = isLate(sub, S.assignment);
      var days = lateDays(sub, S.assignment);
      var value = late === true
        ? "Late: " + (days === 1 ? "1 day" : days + " days")
        : (late === false ? "On time" : "Handed in");
      handedTile = statTile("HANDED IN", value,
        "Handed in " + fmtDateTime(completedIso(sub)));
      if (late === true) { handedTile.valueNode.classList.add("is-late"); }
      if (late === false) { handedTile.valueNode.classList.add("is-good"); }
    } else {
      var st = statusWord(sub, S.assignment);
      handedTile = statTile("HANDED IN", st.word,
        S.assignment.due_at ? "Due " + fmtDateTime(S.assignment.due_at) : "No due date set");
    }
    wrap.appendChild(handedTile.node);

    return wrap;
  }

  /* S1 — one 28x28 square per question: filled ok/tick, filled wrong/cross,
     outlined for unanswered, with a 3px accent underline when the class
     mostly missed it. Each square scrolls to its card. */
  function buildQuestionMap(rows) {
    var wrap = el("div", "bd-qmap");
    rows.forEach(function (row) {
      var state = row.answered
        ? (row.isCorrect === true ? "right" : (row.isCorrect === false ? "wrong" : "unscored"))
        : "unscored";
      var sq = btn("bd-qmap-sq" + (state === "right" ? " is-right" : state === "wrong" ? " is-wrong" : ""));
      if (row.classFlag) { sq.classList.add("is-flagged"); }
      sq.textContent = String(row.position);
      var label = "Question " + row.position + ": " +
        (state === "right" ? "right" : state === "wrong" ? "wrong" : "not answered") +
        (row.classFlag ? ". Most of the class got this wrong." : "");
      sq.setAttribute("aria-label", label);
      sq.addEventListener("click", function () { scrollToQuestion(row.position); });
      wrap.appendChild(sq);
    });
    return wrap;
  }

  function scrollToQuestion(position) {
    var card = els.body.querySelector('[data-bd-q="' + position + '"]');
    if (card) {
      if (card.hasAttribute("data-bd-collapsed")) {
        var details = card.closest("details");
        if (details) { details.open = true; }
      }
      card.scrollIntoView({ block: "center" });
    }
  }

  function topicTitle(sourceRef) {
    if (!sourceRef) { return "This set"; }
    var parts = String(sourceRef).split("/");
    return deslug(parts[parts.length - 1]) || sourceRef;
  }

  /* ⊕ Stream J, 25 Sep 2026 (experience run, item 3) — KS4's `source_ref`
     (== `assignment_questions.source_ref` == `question_ref`/`bank.id`) is a
     PER-QUESTION bank id ('ks4-circuit-symbols-e03'), never a topic —
     `topicTitle` above only makes sense for KS3, where `source_ref` is a
     lesson path ('unit/lesson'). Grouping KS4 rows on it put every question
     under its own "topic", titled with the bank id itself.

     The real subtopic a KS4 question was authored for is
     `ks4_assignment_bank.subtopic_slug`, carried onto the row as
     `subtopicSlug` in `buildRows` below. That is the group key and the
     source of the group's title everywhere it is readable.

     ⚠️ FALLBACK ORDER, for a row whose bank id could not be read (a
     deleted/unreadable bank row — `S.bankById` has nothing for it): the
     ASSIGNMENT's own scope — `scope_ref` when the teacher set a single
     subtopic (`scope_kind === 'subtopic'`), else its `topic`/`title` — is
     still a real curriculum fact, and still never a bank id. Grouping every
     unreadable row under ONE such fallback group (rather than one bucket per
     row, `topicTitle`'s old `"§" + row.position` behaviour) is deliberate:
     a fallback keyed per-question is the exact defect being fixed. */
  function ks4GroupTitle(slug) {
    return deslug(slug) || slug;
  }
  function groupKeyAndTitle(row) {
    if (S.keyStage !== "KS4") {
      return { key: row.sourceRef || ("§" + row.position), title: topicTitle(row.sourceRef) };
    }
    if (row.subtopicSlug) {
      return { key: "st:" + row.subtopicSlug, title: ks4GroupTitle(row.subtopicSlug) };
    }
    var a = S.assignment || {};
    if (a.scope_kind === "subtopic" && a.scope_ref) {
      return { key: "st:" + a.scope_ref, title: ks4GroupTitle(a.scope_ref) };
    }
    return { key: "assignment", title: a.topic || a.title || "This set" };
  }

  /* Every question, in position order, joined to this pupil's attempt (if
     any) and the class-wide flag computed once in open(). */
  function buildRows(myAttempts) {
    var myByQ = {};
    myAttempts.forEach(function (a) { myByQ[a.question_index] = a; });
    return S.questions.map(function (q) {
      var qi = q.position - 1;
      var mine = myByQ[qi] || null;
      var flag = S.flagByQ[qi] || { flagged: false, wrong: 0, total: 0 };
      var classAttempt = S.repByQ[qi] || null;
      var rep = mine || classAttempt;
      var bank = (rep && rep.question_ref) ? S.bankById[rep.question_ref] : null;
      return {
        position: q.position,
        sourceRef: q.source_ref,
        subtopicSlug: bank ? bank.subtopic_slug : null,
        stem: (rep && rep.question_text) || null,
        figure: bank ? bank.figure : null,
        answered: !!mine,
        pupilAnswer: mine ? answerDisplay(mine.selected_answer, mine.selected_option_letter, bank) : null,
        correctAnswer: mine
          ? answerDisplay(mine.correct_answer, mine.correct_option_letter, bank)
          : (rep ? answerDisplay(rep.correct_answer, rep.correct_option_letter, bank) : null),
        isCorrect: mine ? mine.is_correct : null,
        attemptNumber: mine ? mine.attempt_number : null,
        timeSpent: mine ? mine.time_spent_seconds : null,
        criteriaMet: mine ? mine.criteria_met : null,
        criteriaTotal: mine ? mine.criteria_total : null,
        classFlag: flag.flagged,
        classWrong: flag.wrong,
        classAnswered: flag.total
      };
    });
  }

  function groupByTopic(rows) {
    var order = [], byKey = {};
    rows.forEach(function (row) {
      var kt = groupKeyAndTitle(row);
      var g = byKey[kt.key];
      if (!g) {
        g = { key: kt.key, title: kt.title, rows: [], right: 0, total: 0 };
        byKey[kt.key] = g;
        order.push(g);
      }
      g.total += 1;
      if (row.isCorrect === true) { g.right += 1; }
      g.rows.push(row);
    });
    return order;
  }

  function buildQuestionRow(row) {
    var markState = row.answered
      ? (row.isCorrect === true ? "right" : (row.isCorrect === false ? "wrong" : "unscored"))
      : "unscored";
    var card = el("div", "bd-q" +
      (markState === "right" ? " is-right" : (markState === "wrong" ? " is-wrong" : "")) +
      (row.figure ? " has-fig" : ""));
    card.setAttribute("data-bd-q", String(row.position));
    if (row.sourceRef) { card.setAttribute("data-bd-qref", row.sourceRef); }
    if (row.figure) { card.setAttribute("data-bd-figure", row.figure); }

    /* S7 — a 26px filled disc, shape AND colour, with hidden text for a
       screen reader. */
    var mark = el("div", "bd-q-mark is-" + markState);
    var markWord = markState === "right" ? "Right" : markState === "wrong" ? "Wrong" : "Not answered";
    mark.appendChild(el("span", "bd-sr", markWord));
    var markIcon = document.createElementNS("http://www.w3.org/2000/svg", "svg");
    markIcon.setAttribute("viewBox", "0 0 16 16");
    markIcon.setAttribute("fill", "none");
    markIcon.setAttribute("aria-hidden", "true");
    if (markState === "right") {
      markIcon.innerHTML = '<path d="M3 8.5l3.2 3.2L13 5" stroke="currentColor" ' +
        'stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>';
    } else if (markState === "wrong") {
      markIcon.innerHTML = '<path d="M4 4l8 8M12 4l-8 8" stroke="currentColor" ' +
        'stroke-width="2" stroke-linecap="round"/>';
    }
    mark.appendChild(markIcon);
    card.appendChild(mark);

    var head = el("div", "bd-q-head");
    head.appendChild(el("div", "bd-q-num", "Question " + row.position));
    /* S4 — the class flag lives in the header now, with real numbers, in
       sentence case. */
    var flag = el("div", "bd-q-flag");
    flag.hidden = !row.classFlag;
    if (row.classFlag) {
      flag.textContent = row.classWrong + " of " + row.classAnswered + " in the class got this wrong";
    }
    head.appendChild(flag);
    var metaBits = [];
    if (row.attemptNumber != null && row.attemptNumber > 1) {
      /* COULD-3 — the retake as a short story rather than a bare count.
         The earlier wrong answer itself cannot be shown: the database
         UPDATES the one row on a changed answer (unique on submission_id,
         question_index), so no earlier text survives to disclose. */
      metaBits.push(row.isCorrect === true
        ? "Right on the " + ordinal(row.attemptNumber) + " try"
        : (row.attemptNumber === 2 ? "Wrong twice" : "Wrong " + row.attemptNumber + " times"));
    }
    var dur = fmtDuration(row.timeSpent);
    if (dur) { metaBits.push(dur); }
    var meta = el("div", "bd-q-meta", metaBits.join(" · "));
    meta.hidden = !metaBits.length;
    head.appendChild(meta);
    card.appendChild(head);

    var body = el("div", "bd-q-body");
    var mainCol = el("div", "bd-q-main");
    mainCol.appendChild(el("div", "bd-q-stem",
      row.stem || ("Question " + row.position + " — not yet available")));

    var answers = el("div", "bd-q-answers");
    if (!row.answered) {
      var a1 = el("div", "bd-q-answer is-missing");
      a1.appendChild(el("div", "bd-q-answer-label", "Answered"));
      a1.appendChild(el("div", "bd-q-answer-text", "No answer given"));
      answers.appendChild(a1);
    } else {
      var pupilCls = row.isCorrect === true ? " is-pupil-right"
        : (row.isCorrect === false ? " is-pupil-wrong" : "");
      var a2 = el("div", "bd-q-answer" + pupilCls);
      a2.appendChild(el("div", "bd-q-answer-label", "Answered"));
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
    mainCol.appendChild(answers);

    /* S4 — the quiet positive: this pupil beat a question most of the
       class missed. Only meaningful when they actually got it right. */
    var goodNote = el("div", "bd-q-good-note");
    var showGood = row.classFlag && row.isCorrect === true;
    goodNote.hidden = !showGood;
    if (showGood) { goodNote.textContent = "Most of the class missed this. " + S.firstName + " got it."; }
    mainCol.appendChild(goodNote);

    body.appendChild(mainCol);

    var fig = row.figure ? figureNode(row.figure) : null;
    if (fig) {
      var figCol = el("div", "bd-q-fig-col");
      figCol.appendChild(fig);
      body.appendChild(figCol);
    }
    card.appendChild(body);
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
      var tally = el("div", "bd-topic-tally", g.right + " of " + g.total + " right");
      if (g.right === 0) { tally.classList.add("is-zero"); }
      if (g.right === g.total && g.total > 0) { tally.classList.add("is-full"); }
      head.appendChild(tally);
      section.appendChild(head);
      var qlist = el("div", "bd-qlist");
      g.rows.forEach(function (row) { qlist.appendChild(buildQuestionRow(row)); });
      section.appendChild(qlist);
      container.appendChild(section);
    });
    return container;
  }

  /* MUST-6 — under the tiles/map, not after twenty cards; honest about
     what it does (opens the class's sheet, unfiltered — there is no
     `preselect` on `MRBSetWork.open()` yet) and who it is for (the CLASS,
     never one pupil — Set work sets to a class). */
  function buildFollowupRow(groups) {
    var missed = groups.filter(function (g) { return g.total > 0 && g.right < g.total; });
    var row = el("div", "bd-followup-row");
    var b = btn("bd-followup");
    b.textContent = "Open Set work for " + (S.className || "this class");
    b.setAttribute("data-mrb-added", "breakdown-followup");
    b.hidden = !missed.length;
    b.addEventListener("click", function () {
      if (!(window.MRBSetWork && window.MRBSetWork.open)) {
        pushToast("Set work isn't available on this page right now.");
        return;
      }
      window.MRBSetWork.open({ classId: S.classId });
      pushToast("Opened Set work for " + (S.className || "this class") + ".");
    });
    row.appendChild(b);
    return row;
  }

  /* S5 — "The class struggled with Q1, Q7 and Q12", computed once in
     open() (S.classStruggled) and reused on every render/pupil, since it
     is a fact about the CLASS, not about whoever is on screen. */
  function buildClassLine() {
    var line = el("div", "bd-classline");
    if (!S.classStruggled.length) { line.hidden = true; return line; }
    line.appendChild(document.createTextNode("The class struggled with "));
    S.classStruggled.forEach(function (pos, i) {
      var b = document.createElement("button");
      b.type = "button";
      b.textContent = "Q" + pos;
      b.addEventListener("click", function () { scrollToQuestion(pos); });
      line.appendChild(b);
      if (i < S.classStruggled.length - 2) { line.appendChild(document.createTextNode(", ")); }
      else if (i === S.classStruggled.length - 2) { line.appendChild(document.createTextNode(" and ")); }
    });
    line.appendChild(document.createTextNode("."));
    return line;
  }

  /* S13 — remembered on S, which lives for the length of one open()
     session (survives Previous/Next, resets on the next open()). */
  function buildToggle(rows) {
    var wrongCount = rows.filter(function (r) { return r.isCorrect === false; }).length;
    var wrap = el("div", "bd-toggle");
    var all = btn("bd-toggle-btn" + (!S.wrongOnly ? " is-on" : ""));
    all.textContent = "All " + rows.length;
    all.setAttribute("data-mrb-added", "breakdown-wrong-only-all");
    all.addEventListener("click", function () { setWrongOnly(false); });
    var wrong = btn("bd-toggle-btn" + (S.wrongOnly ? " is-on" : ""));
    wrong.textContent = "Wrong " + wrongCount;
    wrong.disabled = wrongCount === 0;
    wrong.setAttribute("data-mrb-added", "breakdown-wrong-only");
    wrong.addEventListener("click", function () { setWrongOnly(true); });
    wrap.appendChild(all); wrap.appendChild(wrong);
    return wrap;
  }
  function setWrongOnly(on) {
    if (!S || S.wrongOnly === on) { return; }
    S.wrongOnly = on;
    renderBody();
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

  /* The header and the aria-live announcement — split out of `render()`
     because `renderBody()` (the Wrong-only toggle) must NOT re-announce
     the pupil. */
  function renderHeader(student) {
    els.eyebrow.textContent = S.assignment.title || "Set work";
    els.title.textContent = student.name;
    var posLabel = "Pupil " + (S.idx + 1) + " of " + S.roster.length;
    els.subtitle.textContent = posLabel + " · " +
      (S.assignment.due_at ? "Due " + fmtDateTime(S.assignment.due_at) : "No due date set");
    els.overlay.setAttribute("data-bd-student", student.id);

    var prevName = S.idx > 0 ? S.roster[S.idx - 1].name : "";
    var nextName = S.idx < S.roster.length - 1 ? S.roster[S.idx + 1].name : "";
    els.prev.disabled = S.idx <= 0;
    els.next.disabled = S.idx >= S.roster.length - 1;
    var prevWord = els.prev.querySelector(".bd-nav-word");
    var nextWord = els.next.querySelector(".bd-nav-word");
    if (prevWord) { prevWord.textContent = prevName; }
    if (nextWord) { nextWord.textContent = nextName; }
    els.prev.setAttribute("aria-label", "Previous pupil" + (prevName ? ": " + prevName : ""));
    els.next.setAttribute("aria-label", "Next pupil" + (nextName ? ": " + nextName : ""));
  }

  function announcePupil(student) {
    els.live.textContent = "Pupil " + (S.idx + 1) + " of " + S.roster.length + ": " + student.name;
  }

  /* Rebuilds everything BELOW the summary tiles — the map, the toggle, the
     follow-up, the class line and the topic cards — without touching the
     header. Called on open, on Prev/Next, and on a Wrong-only toggle. */
  function renderBody() {
    if (!S) { return; }
    var student = S.roster[S.idx];
    var sub = S.submissionsByStudent[student.id] || null;
    var myAttempts = sub ? (S.attemptsBySub[sub.id] || []) : [];
    var rows = buildRows(myAttempts);

    els.body.textContent = "";
    els.body.appendChild(buildSummary(sub, myAttempts));

    var mapRow = el("div", "bd-qmap-wrap");
    mapRow.appendChild(buildQuestionMap(rows));
    mapRow.appendChild(buildToggle(rows));
    els.body.appendChild(mapRow);

    /* MUST-5 — a pupil with genuinely nothing answered gets the empty
       state, then the real questions with blank answers behind a
       collapsed disclosure — never a wall of "No answer given" cards at
       rest. A pupil who has answered SOME (Erin-shaped: in progress) still
       sees their real cards at rest; this only fires at zero. */
    if (!myAttempts.length) {
      var st = statusWord(sub, S.assignment);
      var msg = st.word === "Missing"
        ? student.name + " didn't hand this in. It was due " + fmtDateTime(S.assignment.due_at) + "."
        : student.name + " hasn't started this set yet.";
      els.body.appendChild(el("div", "bd-empty", msg));
      var groups = groupByTopic(rows);
      var details = document.createElement("details");
      details.className = "bd-disclosure";
      var summary = document.createElement("summary");
      summary.textContent = "Show the questions";
      details.appendChild(summary);
      var glist = renderGroups(groups);
      glist.querySelectorAll("[data-bd-q]").forEach(function (c) {
        c.setAttribute("data-bd-collapsed", "1");
      });
      details.appendChild(glist);
      els.body.appendChild(details);
      return;
    }

    els.body.appendChild(buildFollowupRow(groupByTopic(rows)));
    els.body.appendChild(buildClassLine());

    var visible = S.wrongOnly ? rows.filter(function (r) { return r.isCorrect === false; }) : rows;
    var groups2 = groupByTopic(visible);
    /* ⊕ Stream L, 25 Sep 2026 (experience run, item N6) — THE HEADING'S
       TALLY IS THE PUPIL'S REAL SCORE ON THE TOPIC, NOT A COUNT OF
       WHATEVER THE FILTER HAPPENS TO SHOW. `groups2` above is grouped from
       `visible`, which under "Wrong only" is every WRONG row and nothing
       else — so `g.right` (a count of `isCorrect === true` rows) is
       structurally 0 and `g.total` is the wrong-count, not the topic's
       question count. "Circuit symbols · 0 of 7 right" was true about the
       seven rows on screen and false about the pupil, who got 3 of 10
       right on the topic as a whole. Regrouping the UNFILTERED rows gives
       the real right/total per topic; only which ROWS are drawn stays
       filtered. */
    if (S.wrongOnly) {
      var fullByTopic = {};
      groupByTopic(rows).forEach(function (g) { fullByTopic[g.key] = g; });
      groups2.forEach(function (g) {
        var full = fullByTopic[g.key];
        if (full) { g.right = full.right; g.total = full.total; }
      });
    }
    /* COULD-1 — weakest topic first, but only while filtering to Wrong;
       the ordinary read keeps the set's own teaching order. Now sorts on
       the REAL right/total the block above just restored, so it reflects
       the pupil's actual weakest topics rather than a degenerate 0/N tie
       across every group. */
    if (S.wrongOnly) {
      groups2.sort(function (a, b) {
        return (a.right / a.total) - (b.right / b.total);
      });
    }
    els.body.appendChild(renderGroups(groups2));
  }

  function render() {
    if (!S) { return; }
    var student = S.roster[S.idx];
    renderHeader(student);
    renderBody();
  }

  function go(delta) {
    if (!S) { return; }
    var n = S.idx + delta;
    if (n < 0 || n >= S.roster.length) { return; }
    S.idx = n;
    /* S13 — Wrong-only is remembered ACROSS Previous/Next, on purpose; it
       only resets on a fresh open(). */
    render();
    announcePupil(S.roster[S.idx]);
    els.sheet.scrollTop = 0;
  }

  /* ═════════════════════════════════════════════════════════════════════
     THE CLASS-WIDE FLAG — computed ONCE in open(), never per render/pupil.
     A pupil's own answer never changes whether a QUESTION was hard for the
     class, so re-deriving it on every Prev/Next is wasted work for a
     32-pupil x 20-question set (per the critique's own performance note).
     ═════════════════════════════════════════════════════════════════════ */
  function computeFlags(questions, attempts) {
    var byQ = {};
    attempts.forEach(function (a) {
      (byQ[a.question_index] = byQ[a.question_index] || []).push(a);
    });
    var flagByQ = {}, repByQ = {}, struggled = [];
    questions.forEach(function (q) {
      var qi = q.position - 1;
      var list = byQ[qi] || [];
      repByQ[qi] = list[0] || null;
      var wrong = list.filter(function (a) { return a.is_correct === false; }).length;
      var total = list.filter(function (a) { return a.is_correct === true || a.is_correct === false; }).length;
      /* S4 — strictly greater than half, so "most" is actually true. */
      var flagged = total >= 3 && (wrong / total) > 0.5;
      flagByQ[qi] = { flagged: flagged, wrong: wrong, total: total };
      if (flagged) { struggled.push(q.position); }
    });
    struggled.sort(function (a, b) { return a - b; });
    return { flagByQ: flagByQ, repByQ: repByQ, struggled: struggled };
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
    /* S11 — the page behind the panel cannot scroll while it is open. */
    prevOverflow = document.documentElement.style.overflow || "";
    document.documentElement.style.overflow = "hidden";
    renderLoading();

    var sb = client();
    if (!sb) {
      renderError("This page is not signed in. Reload and try again.");
      return;
    }

    try {
      var assignmentId = o.assignmentId || null;
      if (!assignmentId && o.submissionId) {
        var subRow = await loadOneSubmission(sb, o.submissionId);
        assignmentId = subRow && subRow.assignment_id;
      }
      if (!assignmentId) { throw new Error("breakdown: nothing to show"); }

      /* S12 — everything that does not depend on another read yet, in
         parallel. */
      var loaded = await Promise.all([
        loadClass(sb, o.classId),
        loadRoster(sb, o.classId),
        loadAssignment(sb, assignmentId),
        loadQuestions(sb, assignmentId),
        loadSubmissions(sb, assignmentId)
      ]);
      var klass = loaded[0], roster = loaded[1], assignment = loaded[2],
          questions = loaded[3], rawSubmissions = loaded[4];

      if (mySession !== session) { return; }

      /* MUST-1 — never fall back to index 0. If the pupil this panel was
         asked to open on is not an active member (left the class, or a
         mismatched id), fetch their real name and splice them into the
         surname-sorted roster rather than silently showing pupil 1. */
      var idx = -1;
      for (var i = 0; i < roster.length; i++) {
        if (roster[i].id === o.studentId) { idx = i; break; }
      }
      if (idx < 0 && o.studentId) {
        var prof = await loadOneProfile(sb, o.studentId);
        var entry = {
          id: o.studentId,
          name: prof ? fullName(prof.first_name, prof.last_name) : "This pupil",
          sortKey: prof ? rosterSortKey(prof.first_name, prof.last_name) : "￿"
        };
        var pos = 0;
        while (pos < roster.length && rosterEntryCompare(roster[pos], entry) < 0) { pos++; }
        roster.splice(pos, 0, entry);
        idx = pos;
      } else if (idx < 0) {
        idx = 0;
      }
      if (mySession !== session) { return; }

      /* MUST-2 — one submission per pupil, the SAME one every other
         teacher screen would pick. */
      var subByStudent = keepFirstAttempt(rawSubmissions);
      var subById = {};
      Object.keys(subByStudent).forEach(function (sid) {
        subById[subByStudent[sid].id] = subByStudent[sid];
      });
      var canonicalIds = Object.keys(subById);

      var attempts = await loadAllAttempts(sb, canonicalIds);
      if (mySession !== session) { return; }

      var attemptsBySub = {};
      attempts.forEach(function (a) {
        (attemptsBySub[a.submission_id] = attemptsBySub[a.submission_id] || []).push(a);
      });

      /* ⊕ Stream L, 25 Sep 2026 (experience run, item N5) — THE CLASS-WIDE
         FLAG COUNTS FINISHED PUPILS ONLY. `attempts` carries a row from a
         pupil's FIRST ANSWER, not from completion — the same "started, not
         finished" shape `cellOf()` in teacher-live.js and `isDone()` on
         Today both have to guard against — so an in-progress submission
         with two machine-marked answers already contributed two rows here,
         and "3 of 3 in the class got this wrong" counted a pupil every
         other figure on the same set (2/8 submitted, the class mean) left
         out. `isComplete()` — completed_at/submitted_at, or
         status === 'complete', the SAME test this file already uses for
         "hasn't started yet" above — is the one gate; nothing else about
         `computeFlags` changes. */
      var completeAttempts = attempts.filter(function (a) {
        return isComplete(subById[a.submission_id]);
      });
      var flags = computeFlags(questions, completeAttempts);

      var openedStudent = roster[idx];
      S = {
        classId: o.classId,
        className: klass.name || null,
        keyStage: klass.key_stage,
        assignment: assignment,
        questions: questions,
        roster: roster,
        idx: idx,
        firstName: (openedStudent.name || "").split(" ")[0] || "This pupil",
        submissionsByStudent: subByStudent,
        attemptsBySub: attemptsBySub,
        flagByQ: flags.flagByQ,
        repByQ: flags.repByQ,
        classStruggled: flags.struggled,
        bankById: {},
        wrongOnly: false
      };
      /* S12 — draw text NOW; figures patch in once the bank/manifest land,
         never blocking the first paint. */
      render();
      announcePupil(openedStudent);

      var refs = {};
      attempts.forEach(function (a) { if (a.question_ref) { refs[a.question_ref] = 1; } });
      var bankById = await loadBankRows(sb, klass.key_stage, Object.keys(refs));
      await loadFigures(klass.key_stage);
      if (mySession !== session || !S) { return; }
      S.bankById = bankById;
      render();
    } catch (err) {
      if (mySession !== session) { return; }
      console.error("[breakdown]", err);
      renderError("Couldn't load this pupil's answers. Try again in a moment.");
    }
  }

  window.MRBBreakdown = { open: open, close: close };
})();
