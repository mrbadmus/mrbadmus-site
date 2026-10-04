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
  /* "21 May, 05:19" — day, month and time; the year is noise on a panel
     about this term's work. */
  function fmtShort(iso) {
    if (!iso) { return ""; }
    var d = new Date(iso);
    if (isNaN(d.getTime())) { return ""; }
    try {
      var p = {};
      new Intl.DateTimeFormat("en-GB", { timeZone: "Europe/London", day: "numeric",
        month: "numeric", hour: "2-digit", minute: "2-digit", hourCycle: "h23" })
        .formatToParts(d).forEach(function (x) { p[x.type] = x.value; });
      var M = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"];
      return (+p.day) + " " + M[(+p.month) - 1] + ", " + p.hour + ":" + p.minute;
    } catch (e) { return fmtDateTime(iso); }
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

  /* ⊕ SPEC-E / "Prompt X" (4 Oct 2026) — the reveal-columns capability
     probes. `answers_revealed_at`/`latest_score` (submissions) and
     `first_option_letter`/`answered_at` (attempts) ship in a migration that
     may sit PARKED for days before it reaches this project (supabase/
     migrations/20261004010000_x_reopen_fair_scoring.sql). PostgREST 400s a
     WHOLE select if any named column is missing, so this panel — a staff
     screen 135+ pupils' marks flow through — must never name them unprobed.
     Cached only on a definite "column does not exist", same shape as every
     other capability probe in this estate; a transient failure re-probes
     next open() rather than latching a false "unsupported" for the rest of
     the staff member's session. */
  var _submissionRevealCols = null, _attemptRevealCols = null;
  async function submissionRevealColsSupported(sb) {
    if (_submissionRevealCols !== null) { return _submissionRevealCols; }
    try {
      var r = await sb.from("assignment_submissions")
        .select("answers_revealed_at, latest_score").limit(0);
      if (!r.error) { _submissionRevealCols = true; return true; }
      if (r.error.code === "42703" || r.error.code === "PGRST204") {
        _submissionRevealCols = false; return false;
      }
      return false;
    } catch (e) { return false; }
  }
  async function attemptRevealColsSupported(sb) {
    if (_attemptRevealCols !== null) { return _attemptRevealCols; }
    try {
      var r = await sb.from("assignment_question_attempts")
        .select("first_option_letter, answered_at").limit(0);
      if (!r.error) { _attemptRevealCols = true; return true; }
      if (r.error.code === "42703" || r.error.code === "PGRST204") {
        _attemptRevealCols = false; return false;
      }
      return false;
    } catch (e) { return false; }
  }

  /* EVERY pupil's submission ROW for this assignment — before dedup, so a
     retaking pupil can appear twice here. `keepFirstAttempt` below reduces
     it to one per student_id, the same rule the rest of the estate uses. */
  async function loadSubmissions(sb, assignmentId) {
    var extra = (await submissionRevealColsSupported(sb))
      ? ", answers_revealed_at, latest_score" : "";
    return fetchPaged("submissions", function (from, to) {
      return sb.from("assignment_submissions")
        /* ⊕ Sharpen C5 — `updated_at`, for "changed after answers shown". */
        .select("id, student_id, score, max_score, status, completed_at, " +
                "submitted_at, updated_at, is_late, total_time_seconds, attempts, attempt_no" + extra)
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
    var extra = (await attemptRevealColsSupported(sb))
      ? ", first_option_letter, answered_at" : "";
    return fetchPaged("attempts", function (from, to) {
      return sb.from("assignment_question_attempts")
        .select("id, submission_id, question_index, question_text, selected_answer, " +
                "correct_answer, is_correct, time_spent_seconds, attempt_number, " +
                "created_at, question_ref, selected_option_letter, " +
                "correct_option_letter, rung, criteria_met, criteria_total" + extra)
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
  /* ⊕ Sharpen C5 (29 Sep 2026), made truthful by SPEC-E (4 Oct 2026).
     HEURISTIC — the pre-migration fallback, byte for byte what this always
     was: complete, and `updated_at` more than 2 s after the completion
     stamp (an answer in flight when Complete landed rescores a moment
     later; the slack keeps that out). Still what server.js's `isRevised()`
     and teacher-live.js's `isRevisedSub()` fall back to when the reveal
     columns are absent. */
  var REVISED_SLACK_MS = 2000;
  function isRevisedHeuristic(sub) {
    if (!sub || sub.status !== "complete" || !sub.updated_at) { return false; }
    var done = sub.completed_at || sub.submitted_at;
    if (!done) { return false; }
    var u = Date.parse(sub.updated_at), d = Date.parse(done);
    if (isNaN(u) || isNaN(d)) { return false; }
    return u > d + REVISED_SLACK_MS;
  }
  /* TRUTHFUL — an attempt whose CURRENTLY STORED answer was given or
     changed after `answers_revealed_at` (the server's reveal stamp, never
     a client value): EXISTS a row in `myAttempts` with `answered_at` past
     the reveal (plus the same 2-second slack, for the same MRB-292
     in-flight-answer race the heuristic above guards against). Covers both
     ways a set is "changed after the reveal" — an answer that was edited,
     and a question left blank at hand-in and answered afterwards — because
     both advance that row's `answered_at` and nothing else does (a plain
     re-save of the SAME letter leaves it where it was — see
     `mrb_attempt_track_first_answer` in the migration). Falls back to the
     heuristic when the reveal columns or `myAttempts` are not available. */
  function isRevised(sub, myAttempts) {
    if (!sub || sub.status !== "complete") { return false; }
    if (!sub.answers_revealed_at || !myAttempts) { return isRevisedHeuristic(sub); }
    var cutoff = Date.parse(sub.answers_revealed_at) + REVISED_SLACK_MS;
    return myAttempts.some(function (a) {
      var t = Date.parse(a.answered_at || "");
      return !isNaN(t) && t > cutoff;
    });
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
    /* ⊕ Sharpen C2 — hidden from the start (loading and error states never
       reach `renderHeader`), kept so the shell keeps its shape. */
    subtitle.hidden = true;
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
  /* ⊕ Design port A — "7 / 10" with the denominator de-emphasised
     (Design's `.pn-stat-v small`), same content as `statTile`, just the
     "/ N" portion wrapped so CSS can size it down. */
  function statTileSplit(label, main, suffix, sub) {
    var d = el("div", "bd-stat");
    d.appendChild(el("div", "bd-stat-label", label));
    var v = el("div", "bd-stat-value");
    v.appendChild(document.createTextNode(main));
    if (suffix) { v.appendChild(el("small", null, suffix)); }
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
      /* ⊕ Sharpen C6 (T40) — the score in one form, no "90%" under "9 / 10".
         ⊕ design-port-b, 30 Sep 2026 — `totalQ` (this panel's OWN
         `S.questions.length`, loaded two lines up), not `sub.max_score`.
         `max_score` is written by the backend's `rescore()` as "however
         many questions were marked the LAST TIME it ran", which for a
         submission completed after being left part-way and resumed (C5's
         "Finish it") can be smaller than the set's real size if a caller
         ever reads it between a partial save and the final one — the same
         defect SHARPEN-REPORT item 7 names for the class page's score
         cells. `totalQ` is the set's own row count and cannot be stale.
         Falls back to `max_score` only if `totalQ` is somehow 0/unknown. */
      scoreTile = statTileSplit("SCORE", String(sub.score), " / " + (totalQ || sub.max_score), null);
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
      /* ⊕ Sharpen C6 (T41) — the moment alone; the label says "handed in". */
      handedTile = statTile("HANDED IN", value, fmtShort(completedIso(sub)));
      if (late === true) { handedTile.valueNode.classList.add("is-late"); }
      if (late === false) { handedTile.valueNode.classList.add("is-good"); }
      /* ⊕ Sharpen C5, corrected by SPEC-E (4 Oct 2026) — the pupil changed
         something after being shown the correct answers. ⚠️ THE SCORE TILE
         IS NO LONGER "ALREADY THE LATEST" — under Mide's option A, `sub.score`
         is the COUNTED figure (answers given before the reveal only) and is
         DELIBERATELY unmoved by a post-reveal change; `sub.latest_score` is
         "if I marked it today". When they differ, say so once, here, rather
         than leaving the SCORE tile looking wrong next to this note. */
      if (isRevised(sub, myAttempts)) {
        /* ⊕ re-audit — changed the same day it was handed in: the time
           alone ("Changed after answers shown · 22:31"); another day:
           "Changed after answers shown · 29 Sep, 21:10". */
        var handedS = fmtShort(completedIso(sub)), revS = fmtShort(sub.updated_at);
        var sameDay = handedS.split(",")[0] === revS.split(",")[0];
        var rv = el("div", "bd-stat-sub", "Changed after answers shown · " +
                    (sameDay ? (revS.split(", ")[1] || revS) : revS));
        rv.setAttribute("data-bd-revised", "1");
        handedTile.node.appendChild(rv);
        if (sub.latest_score != null && sub.score != null && sub.latest_score !== sub.score) {
          var nowRv = el("div", "bd-stat-sub", "Now " + sub.latest_score + " / " + (totalQ || sub.max_score));
          nowRv.setAttribute("data-bd-latest-score", "1");
          scoreTile.node.appendChild(nowRv);
        }
      }
    } else {
      var st = statusWord(sub, S.assignment);
      handedTile = statTile("HANDED IN", st.word,
        S.assignment.due_at ? "Due " + fmtDateTime(S.assignment.due_at) : "No due date set");
    }
    wrap.appendChild(handedTile.node);

    return wrap;
  }

  /* ⊕ Design port A — one 34x34 square per question: filled right, ring
     wrong, dashed not-answered. The SAME mark (`.bd-qmap-sq`) draws the
     per-question row below (`buildQuestionRow`), so the strip works as a
     key for the list under it, as drawn. The class-wide "most of the
     class got this wrong" underline/label is cut with the classline/
     follow-up above — see that comment. Each square scrolls to its row. */
  function buildQuestionMap(rows) {
    var wrap = el("div", "bd-qmap");
    rows.forEach(function (row) {
      var state = row.answered
        ? (row.isCorrect === true ? "right" : (row.isCorrect === false ? "wrong" : "unscored"))
        : "unscored";
      var sq = btn("bd-qmap-sq" + (state === "right" ? " is-right" : state === "wrong" ? " is-wrong" : " is-blank"));
      sq.textContent = String(row.position);
      var label = "Question " + row.position + ": " +
        (state === "right" ? "right" : state === "wrong" ? "wrong" : "not answered");
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
     any) and the class-wide flag computed once in open(). `sub` is this
     pupil's submission row — SPEC-E needs it here (not just in
     `buildSummary`) for the per-question "changed after answers shown ·
     was B" mark, which depends on the SAME reveal stamp. */
  function buildRows(myAttempts, sub) {
    var myByQ = {};
    myAttempts.forEach(function (a) { myByQ[a.question_index] = a; });
    var revealCutoff = (sub && sub.answers_revealed_at)
      ? Date.parse(sub.answers_revealed_at) + REVISED_SLACK_MS : null;
    return S.questions.map(function (q) {
      var qi = q.position - 1;
      var mine = myByQ[qi] || null;
      var flag = S.flagByQ[qi] || { flagged: false, wrong: 0, total: 0 };
      var classAttempt = S.repByQ[qi] || null;
      var rep = mine || classAttempt;
      var bank = (rep && rep.question_ref) ? S.bankById[rep.question_ref] : null;
      /* ⊕ SPEC-E — this ONE question was changed (or first answered) after
         the reveal: `answered_at` past the cutoff AND the letter now stored
         differs from the FIRST one ever given (so a re-save of the same
         answer, or a question answered only once, never says "was X" about
         itself). `first_option_letter` is immutable once set — see the
         migration — so this can never show a letter the pupil didn't
         actually give first. */
      var changedAfterReveal = false, wasLetter = null;
      if (mine && revealCutoff != null && mine.first_option_letter) {
        var answeredAt = Date.parse(mine.answered_at || "");
        if (!isNaN(answeredAt) && answeredAt > revealCutoff &&
            mine.first_option_letter !== mine.selected_option_letter) {
          changedAfterReveal = true;
          wasLetter = mine.first_option_letter;
        }
      }
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
        changedAfterReveal: changedAfterReveal,
        wasLetter: wasLetter,
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

  /* ⊕ Design port A — the numbered square IS the mark (S7's separate
     tick/cross disc is cut, as ruled: "the numbered square does both
     jobs, and it matches the strip" — Design's NOTES.md). S4's per-
     question class flag and "quiet positive" note are cut with the
     class-wide line above (see that comment) — Design's own drawing of
     this row carries neither. Answers render as a <dl> (Answered/Correct,
     shortened from "Correct answer") matching Design's `.pn-ans`. */
  function buildQuestionRow(row) {
    var markState = row.answered
      ? (row.isCorrect === true ? "right" : (row.isCorrect === false ? "wrong" : "unscored"))
      : "unscored";
    var li = el("li", "bd-q" +
      (markState === "right" ? " is-right" : (markState === "wrong" ? " is-wrong" : "")) +
      (row.figure ? " has-fig" : ""));
    li.setAttribute("data-bd-q", String(row.position));
    if (row.sourceRef) { li.setAttribute("data-bd-qref", row.sourceRef); }
    if (row.figure) { li.setAttribute("data-bd-figure", row.figure); }

    var markWord = markState === "right" ? "right" : markState === "wrong" ? "wrong" : "not answered";
    var sq = el("span", "bd-qmap-sq" + (markState === "right" ? " is-right" : markState === "wrong" ? " is-wrong" : " is-blank"));
    sq.setAttribute("aria-hidden", "true");
    sq.textContent = String(row.position);
    li.appendChild(sq);
    li.appendChild(el("span", "bd-sr", "Question " + row.position + ", " + markWord));

    var mainCol = el("div", "bd-q-main");
    mainCol.appendChild(el("div", "bd-q-stem",
      row.stem || ("Question " + row.position + " — not yet available")));

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
    /* ⊕ SPEC-E (4 Oct 2026) — this ONE row was changed (or first answered)
       after the pupil was shown the correct answers; the mark that counts
       for the teacher is whatever this question was BEFORE that moment
       (`isCorrect` above already reflects it, via `sub.score`'s formula —
       no change needed here), so saying which letter it used to be is the
       one genuinely new fact this row can tell a teacher. */
    if (row.changedAfterReveal) {
      metaBits.push("Changed after answers shown" + (row.wasLetter ? " · was " + row.wasLetter : ""));
    }
    if (metaBits.length) { mainCol.appendChild(el("div", "bd-q-meta", metaBits.join(" · "))); }

    var answers = el("dl", "bd-q-answers");
    if (!row.answered) {
      /* ⊕ 1 Oct 2026 (sweep fix C9) — "Answer", not "Answered", labelling
         a value that already says "Not answered": the row used to read
         "Answered — Not answered", the same word twice to say one thing
         (SWEEP C9, `t20-breakdown`). */
      answers.appendChild(el("dt", "bd-q-answer-label", "Answer"));
      answers.appendChild(el("dd", "bd-q-answer-text is-none", "Not answered"));
    } else {
      var pupilCls = row.isCorrect === true ? " is-right"
        : (row.isCorrect === false ? " is-wrong" : "");
      answers.appendChild(el("dt", "bd-q-answer-label", "Answered"));
      answers.appendChild(el("dd", "bd-q-answer-text" + pupilCls, row.pupilAnswer || "—"));
    }
    if (row.isCorrect === false && row.correctAnswer) {
      answers.appendChild(el("dt", "bd-q-answer-label", "Correct"));
      answers.appendChild(el("dd", "bd-q-answer-text is-right", row.correctAnswer));
    }
    if (row.criteriaTotal != null) {
      answers.appendChild(el("dt", "bd-q-answer-label", "Self-marked"));
      answers.appendChild(el("dd", "bd-q-answer-text",
        (row.criteriaMet == null ? "—" : row.criteriaMet) +
        " of " + row.criteriaTotal + " criteria met"));
    }
    mainCol.appendChild(answers);

    li.appendChild(mainCol);

    var fig = row.figure ? figureNode(row.figure) : null;
    if (fig) {
      var figCol = el("div", "bd-q-fig-col");
      figCol.appendChild(fig);
      li.appendChild(figCol);
    }
    return li;
  }

  /* ⊕ Design port A, 30 Sep 2026 — the topic-group headers and tallies are
     CUT, as ruled and as drawn: one flat, numbered list, matching the
     question-map strip above it. `groupByTopic` is UNCHANGED and still
     runs (see renderBody's "weakest topic first" sort under Wrong-only,
     COULD-1) — only the render side stops turning a group into a visible
     section. */
  function renderQuestionList(rows) {
    if (!rows.length) {
      return el("div", "bd-empty", "No questions in this set.");
    }
    var ol = el("ol", "bd-qlist");
    ol.setAttribute("aria-label", "Answers");
    rows.forEach(function (row) { ol.appendChild(buildQuestionRow(row)); });
    return ol;
  }

  /* ⊕ Design port A, 30 Sep 2026 — MUST-6's "Open Set work for…" follow-up
     and S5's "The class struggled with…" line are CUT from this PUPIL
     panel (Mide's ruling via the design-port brief, 30 Sep 2026): both are
     class-wide facts, and Design's redrawn panel — built pupil-first —
     carries neither. The assignment page's own Reteach banner already
     says both things at the class level; this panel never repeated it
     structurally (MUST-6 only ever opened Set work unfiltered), so
     nothing downstream loses a capability. `S.classStruggled` is still
     COMPUTED in `computeFlags` below (cheap, and `S.repByQ` in the same
     function is load-bearing — see its own comment) but nothing renders
     it any more. `buildFollowupRow`/`buildClassLine` are deleted rather
     than left dead, per the same reasoning `MRBSetWork.open` calls
     nowhere else in this file rely on them.

     S13 — remembered on S, which lives for the length of one open()
     session (survives Previous/Next, resets on the next open()). */
  function buildToggle(rows) {
    var wrongCount = rows.filter(function (r) { return r.isCorrect === false; }).length;
    var wrap = el("div", "bd-toggle");
    var all = btn("bd-toggle-btn" + (!S.wrongOnly ? " is-on" : ""));
    all.textContent = "All " + rows.length;
    all.setAttribute("data-mrb-added", "breakdown-wrong-only-all");
    /* ⊕ Stream N, 25 Sep 2026 (experience run, item 10 / NF8) — the
       selected state was shown by the `is-on` class alone, with nothing in
       the accessibility tree saying either chip was a toggle or which one
       was pressed. `aria-pressed`, kept in step with the same `S.wrongOnly`
       flag `is-on` already reads, the same fix N8 already gave the bulk
       shoutout sheet's per-pupil chips (`teacher_rulings.BIND_ATTR[644]`)
       and the Set-work sheet's own chips. */
    all.setAttribute("aria-pressed", String(!S.wrongOnly));
    all.addEventListener("click", function () { setWrongOnly(false); });
    var wrong = btn("bd-toggle-btn" + (S.wrongOnly ? " is-on" : ""));
    wrong.textContent = "Wrong " + wrongCount;
    wrong.disabled = wrongCount === 0;
    wrong.setAttribute("data-mrb-added", "breakdown-wrong-only");
    wrong.setAttribute("aria-pressed", String(S.wrongOnly));
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
    /* ⊕ Sharpen C2, 29 Sep 2026 — no "Pupil N of M · Due …". The position
       is what Previous/Next already show (their names), and the due date
       is the page's, not the pupil's. The node stays, empty and hidden, so
       the shell keeps its shape; `announcePupil` still says the position
       to a screen reader. */
    els.subtitle.textContent = "";
    els.subtitle.hidden = true;
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
    var rows = buildRows(myAttempts, sub);

    els.body.textContent = "";
    els.body.appendChild(buildSummary(sub, myAttempts));

    var mapRow = el("div", "bd-qmap-wrap");
    mapRow.appendChild(buildQuestionMap(rows));
    mapRow.appendChild(buildToggle(rows));
    /* ⊕ Sharpen C6 (T43) — no map and no "All 0 / Wrong 0" over nothing. */
    if (rows.length) { els.body.appendChild(mapRow); }

    /* MUST-5 — a pupil with genuinely nothing answered gets the empty
       state, then the real questions with blank answers behind a
       collapsed disclosure — never a wall of "No answer given" cards at
       rest. A pupil who has answered SOME (Erin-shaped: in progress) still
       sees their real cards at rest; this only fires at zero. */
    if (!myAttempts.length) {
      var st = statusWord(sub, S.assignment);
      /* ⊕ Sharpen C6 (T42) — a sitting WITH a score but no per-question
         rows is not "hasn't started": the tiles above show its score. */
      if (isComplete(sub) && sub.score != null) {
        els.body.appendChild(el("div", "bd-empty", "No question-by-question marks for this sitting."));
        return;
      }
      var msg = st.word === "Missing"
        ? student.name + " didn't hand this in. It was due " + fmtDateTime(S.assignment.due_at) + "."
        : student.name + " hasn't started this set yet.";
      els.body.appendChild(el("div", "bd-empty", msg));
      var details = document.createElement("details");
      details.className = "bd-disclosure";
      var summary = document.createElement("summary");
      summary.textContent = "Show the questions";
      details.appendChild(summary);
      var glist = renderQuestionList(rows);
      if (glist.tagName === "OL") {
        Array.prototype.forEach.call(glist.querySelectorAll("[data-bd-q]"), function (c) {
          c.setAttribute("data-bd-collapsed", "1");
        });
      }
      details.appendChild(glist);
      els.body.appendChild(details);
      return;
    }

    var visible = S.wrongOnly ? rows.filter(function (r) { return r.isCorrect === false; }) : rows;
    var ordered = visible;
    /* COULD-1 — weakest topic first, but only while filtering to Wrong;
       the ordinary read keeps the set's own teaching order. `groupByTopic`
       is used purely as a SORT KEY here — ⊕ Design port A cut the
       rendered topic sections (see renderQuestionList's comment), so the
       grouping never reaches the screen, only the row order does. Right/
       total is restored from the UNFILTERED rows (Stream L, N6) so the
       sort reflects the pupil's actual weakest topics, not a degenerate
       0/N tie across every group of purely-wrong rows. */
    if (S.wrongOnly) {
      var groups2 = groupByTopic(visible);
      var fullByTopic = {};
      groupByTopic(rows).forEach(function (g) { fullByTopic[g.key] = g; });
      groups2.forEach(function (g) {
        var full = fullByTopic[g.key];
        if (full) { g.right = full.right; g.total = full.total; }
      });
      groups2.sort(function (a, b) { return (a.right / a.total) - (b.right / b.total); });
      ordered = [];
      groups2.forEach(function (g) { g.rows.forEach(function (r) { ordered.push(r); }); });
    }
    els.body.appendChild(renderQuestionList(ordered));
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
