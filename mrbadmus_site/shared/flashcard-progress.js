/* ═══════════════════════════════════════════════════════════════════════
   flashcard-progress.js — MRB-351 §5, the teacher's view of one flashcard
   set: teacher/flashcards.html?assignment=<id>.

   Reads (all through the signed-in teacher's own client, RLS/definer-gated):
     rpc flashcard_progress      {p_assignment, p_now}   the table + strip
     (one pupil's cards: shared/flashcard-breakdown.js, the per-pupil panel)
     rpc flashcard_edit_assignment {p_id, p_title, p_due_at, p_note,
                                    p_release_at}        Edit
     POST functions/v1/flashcard-answer-check {assignment_id}
                                                         fire and forget, on open

   ⚠️ NOTHING HERE BUILDS HTML FROM A STRING. Every pupil name, card side and
   note reaches the page as a text node (or through MRBFormulae.fill, which
   builds <sub> elements), so no card can become markup.

   ⚠️ LONDON TIME. Anything SENT is converted by MRBSetWork.londonToUtcIso;
   Intl with timeZone is used for DISPLAY only.

   The pure half (sorting, statuses, formats, CSV) is exported on
   `window.MRBFlashcardProgress` so `flashcard_progress_drive.py` can prove it
   directly as well as through the page.
   ═══════════════════════════════════════════════════════════════════════ */
(function () {
  "use strict";

  var POLL_MS = 10000;
  var TZ = "Europe/London";

  /* ── vocabulary: the existing words, never new ones ───────────────────── */
  var STATUS = {
    missing:     { label: "Missing",     rank: 0, tone: "warn" },
    not_started: { label: "Not started", rank: 1, tone: "idle" },
    in_progress: { label: "In progress", rank: 2, tone: "busy" },
    done_late:   { label: "Done late",   rank: 3, tone: "late" },
    done:        { label: "Done",        rank: 4, tone: "ok" }
  };
  /* ⊕ Sharpen B1/B2/B3, 29 Sep 2026 — MODE/RULE (the header chips),
     CHECK/RATING (the drawer) and the Answers column are gone: the chips
     repeated what the table already shows, the verdict split moved to the
     per-pupil panel (shared/flashcard-breakdown.js), and so did the drawer. */
  var SAY = {
    notFound: "Flashcard set not found",
    failed: "Couldn't load this set",
    // ⊕ MRB-351 landing (27 Sep 2026) — a hand-typed/bookmarked URL, with no
    // schema on production, reads a calm sentence rather than "Couldn't
    // load this set" — which is a claim that something is temporarily
    // broken, when the honest answer is that the feature is not switched
    // on yet. See `start()`'s capability check below.
    notSwitchedOn: "Flashcard decks aren't switched on yet.",
    noPupils: "No pupils in this class",
    saved: "Saved",
    saveFailed: "Couldn't save",
    dueBeforeRelease: "Due must be after release",
    releasePast: "Release time has passed",
    badTitle: "Title needed",
    badNote: "Note too long",
    detailFailed: "Couldn't load this pupil"
  };

  /* ── pure helpers ─────────────────────────────────────────────────────── */
  function pad2(n) { return (n < 10 ? "0" : "") + n; }

  function nameOf(p) {
    var n = [p.first_name, p.last_name].filter(Boolean).join(" ").trim();
    return n || p.display_name || "Pupil";
  }

  function clock(ms) {
    if (ms == null || !isFinite(ms)) { return "—"; }
    var s = Math.max(0, Math.round(ms / 1000));
    var h = Math.floor(s / 3600), m = Math.floor((s % 3600) / 60), r = s % 60;
    return h ? (h + ":" + pad2(m) + ":" + pad2(r)) : (m + ":" + pad2(r));
  }

  function seconds(ms) {
    if (ms == null || !isFinite(ms)) { return "—"; }
    return (Math.round(ms / 100) / 10).toFixed(1) + " s";
  }

  var MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep",
                "Oct", "Nov", "Dec"];

  /* The London wall clock, for DISPLAY. Numeric month, named here: en-GB's
     own short name for September is "Sept" on some engines and "Sep" on
     others, and the teacher screens say "Sep". */
  function londonParts(iso) {
    var d = new Date(iso);
    if (isNaN(d.getTime())) { return null; }
    var f = new Intl.DateTimeFormat("en-GB", {
      timeZone: TZ, weekday: "short", day: "numeric", month: "numeric",
      year: "numeric", hour: "2-digit", minute: "2-digit", hourCycle: "h23"
    });
    var o = {};
    f.formatToParts(d).forEach(function (p) { o[p.type] = p.value; });
    o.mon = +o.month;
    o.month = MONTHS[o.mon - 1] || "";
    o.weekday = String(o.weekday || "").slice(0, 3);
    return o;
  }

  // "Fri 3 Oct, 15:00"
  function londonWhen(iso) {
    var p = iso ? londonParts(iso) : null;
    if (!p) { return "—"; }
    return p.weekday + " " + (+p.day) + " " + p.month + ", " + p.hour + ":" + p.minute;
  }

  function londonYmd(iso) {
    var p = iso ? londonParts(iso) : null;
    if (!p) { return ""; }
    return p.year + "-" + pad2(p.mon) + "-" + pad2(+p.day) + " " + p.hour + ":" + p.minute;
  }

  // "just now", "3 min ago", "2 h ago", "yesterday", "Mon 29 Sep"
  function relative(iso, nowMs) {
    if (!iso) { return "—"; }
    var t = Date.parse(iso);
    if (isNaN(t)) { return "—"; }
    var diff = Math.max(0, (nowMs == null ? Date.now() : nowMs) - t);
    var min = Math.floor(diff / 60000);
    if (min < 1) { return "just now"; }
    if (min < 60) { return min + " min ago"; }
    var p = londonParts(iso), n = londonParts(new Date(nowMs == null ? Date.now() : nowMs).toISOString());
    var sameDay = p && n && p.year === n.year && p.month === n.month && p.day === n.day;
    if (sameDay) { return Math.floor(min / 60) + " h ago"; }
    var y = londonParts(new Date((nowMs == null ? Date.now() : nowMs) - 86400000).toISOString());
    if (p && y && p.year === y.year && p.month === y.month && p.day === y.day) { return "yesterday"; }
    return p ? (p.weekday + " " + (+p.day) + " " + p.month) : "—";
  }

  function assignmentState(a, nowIso) {
    if (a.release_at && a.release_at > nowIso) { return "scheduled"; }
    if (!a.due_at || a.due_at > nowIso) { return "open"; }
    return "closed";
  }

  /* The sort. Default is least progress first: Missing and Not started,
     then In progress by secured ascending, then Done late, then Done.
     Every column sorts; a missing value always sinks, whichever way. */
  /* ⊕ Sharpen C1 — every column a FIXED width (`table-layout: fixed` +
     a <colgroup> from `w`), so no row's content moves a column; only the
     pupil column is flexible. Header words fit their widths at 12.5px mono.

     ⊕ Design port A, 30 Sep 2026 — "Per card" and "Rushed" are CUT, as
     ruled and as drawn ("it's Time ÷ cards" / "now a small 'RUSHED'
     marker in the Time cell"). Rushed rides inside the "time" cell's
     rendering (`renderTable`) and CSV text (`buildCsv`) instead of
     owning a column — see both functions' own comments. */
  var COLUMNS = [
    { key: "pupil",    label: "Pupil",       w: null },
    { key: "status",   label: "Status",      w: 290 },
    { key: "made",     label: "Made",        w: 90, make: true },
    { key: "secured",  label: "Secured",     w: 200 },
    { key: "sittings", label: "Sittings",    w: 120 },
    { key: "time",     label: "Time",        w: 150 },
    { key: "last",     label: "Last active", w: 150 }
  ];

  function columnsFor(mode) {
    return COLUMNS.filter(function (c) { return !c.make || mode === "make"; });
  }

  function rank(p) { return (STATUS[p.status] || STATUS.not_started).rank; }

  /* ⊕ MRB-354 §6 — every sort/display reads `p.known`, the RPC's secured
     count under the new rule (correct before and after the parked SQL);
     the OLD two-sitting `p.secured` is never shown or sorted on. */
  function sortValue(p, key) {
    switch (key) {
      case "pupil": return ((p.last_name || "") + " " + (p.first_name || "") + " " + (p.display_name || "")).toLowerCase();
      case "status": return rank(p) * 100000 + (p.known || 0);
      case "made": return p.made == null ? null : p.made;
      case "secured": return p.known == null ? null : p.known;
      case "sittings": return p.sittings == null ? null : p.sittings;
      case "time": return p.active_ms == null ? null : p.active_ms;
      case "last": return p.last_active ? Date.parse(p.last_active) : null;
    }
    return null;
  }

  function defaultCompare(a, b) {
    var r = rank(a) - rank(b);
    if (r) { return r; }
    var s = (a.known || 0) - (b.known || 0);
    if (s) { return s; }
    return sortValue(a, "pupil") < sortValue(b, "pupil") ? -1
         : (sortValue(a, "pupil") > sortValue(b, "pupil") ? 1 : 0);
  }

  function sortRows(rows, key, dir) {
    var list = rows.slice();
    if (!key) { return list.sort(defaultCompare); }
    var sign = dir === "desc" ? -1 : 1;
    return list.sort(function (a, b) {
      var va = sortValue(a, key), vb = sortValue(b, key);
      if (va == null && vb == null) { return defaultCompare(a, b); }
      if (va == null) { return 1; }
      if (vb == null) { return -1; }
      if (va < vb) { return -sign; }
      if (va > vb) { return sign; }
      return defaultCompare(a, b);
    });
  }

  function cellText(p, key, n, mode, rule, nowMs) {
    switch (key) {
      case "pupil": return nameOf(p);
      case "status": return (STATUS[p.status] || STATUS.not_started).label;
      case "made": return (p.made || 0) + "/" + n;
      case "secured": return (p.known || 0) + "/" + n;
      case "sittings": return String(p.sittings || 0);
      case "time": return p.active_ms ? clock(p.active_ms) : "—";
      case "last": return relative(p.last_active, nowMs);
    }
    return "";
  }

  function csvEscape(v) {
    var s = v == null ? "" : String(v);
    return /[",\r\n]/.test(s) ? '"' + s.replace(/"/g, '""') + '"' : s;
  }

  /* The table as displayed, in the order displayed. `Last active` is the
     London clock rather than "3 min ago", which means nothing in a file.
     ⊕ MRB-354 §6 — the "Known once" column is GONE (completion_rule no
     longer means anything to secured/done, so the distinction it existed to
     show is gone too); the Secured column itself is `p.known`. */
  function buildCsv(data, rows, truth) {
    var a = data.assignment || {}, n = data.n || 0;
    var cols = columnsFor(a.mode);
    var head = [];
    cols.forEach(function (c) { head.push(c.label); if (c.key === "secured") { head.push("Unsure"); } });
    var lines = [head.map(csvEscape).join(",")];
    rows.forEach(function (p) {
      var out = [];
      cols.forEach(function (c) {
        if (c.key === "last") { out.push(p.last_active ? londonYmd(p.last_active) : ""); }
        /* ⊕ Design port A — no separate Rushed column; the fact rides in
           the Time cell's own CSV text, as it does on screen. */
        else if (c.key === "time") { out.push((p.active_ms ? clock(p.active_ms) : "") + (p.rushed ? " (rushed)" : "")); }
        else { out.push(cellText(p, c.key, n, a.mode, a.rule)); }
        /* ⊕ round 3 — Unsure sits right after Secured; blank when there is no
           understanding data (never 0 for "unknown"). */
        if (c.key === "secured") {
          var T = window.MRBFlashcardTruth;
          out.push(truth && !truth.failed && T ? String(T.unsure(truth, p.pupil_id)) : "");
        }
      });
      lines.push(out.map(csvEscape).join(","));
    });
    return "﻿" + lines.join("\r\n") + "\r\n";
  }

  function csvFilename(a) {
    var base = [a.class_name || "class", a.title || "flashcards"].join(" ")
      .replace(/[^A-Za-z0-9]+/g, "-").replace(/^-+|-+$/g, "");
    return (base || "flashcards") + ".csv";
  }

  /* ── DOM helpers — text only ──────────────────────────────────────────── */
  function h(tag, cls, text) {
    var e = document.createElement(tag);
    if (cls) { e.className = cls; }
    if (text != null) { e.textContent = text; }
    return e;
  }
  /* ⊕ Set from class (M), 27 Sep 2026 — formulae are drawn only when the
     assignment is Chemistry (`S.chem`, read once in `start()`); otherwise the
     text shows exactly as typed (N2 can be Newton's second law). */
  function sci(tag, cls, text) {
    var e = h(tag, cls);
    if (S.chem && window.MRBFormulae && window.MRBFormulae.fill) { window.MRBFormulae.fill(e, text || ""); }
    else { e.textContent = text || ""; }
    return e;
  }
  function $(id) { return document.getElementById(id); }
  function clear(e) { while (e && e.firstChild) { e.removeChild(e.firstChild); } return e; }

  /* ── state ────────────────────────────────────────────────────────────── */
  var S = {
    id: null, sb: null, data: null, sortKey: null, sortDir: "asc",
    timer: null, inflight: false, lastFocus: null, chem: false,
    /* ⊕ Flashcards round 3 (teacher) — the TRUTH read; see refreshTruth().
       truth: null = not settled yet, {failed:true} = the read did not work,
       else shared/flashcard-truth.js's build() result. truthRows: the raw
       class-wide rows (null = not read, false = the read failed). */
    truth: null, truthRows: null, truthBusy: false, truthSig: null, truthFailAt: 0
  };

  /* ═════════════════════════════════════════════════════════════════════
     ⊕ Design port A follow-up, 30 Sep 2026 — the Secured strip's real
     five-state per-card breakdown (Secured/Got it/Nearly/Not yet/Not
     seen), not the three-bucket approximation the port shipped with.

     THE DERIVATION IS NOT REWRITTEN HERE. `window.MRBFlashcardBreakdown
     .cardState(card)` — shared/flashcard-breakdown.js, already used by
     the per-pupil sheet's own card chips — is the ONE place a card's
     rating history becomes a state word. This file calls it, never
     re-implements it. flashcard-breakdown.js loads before this file on
     teacher/flashcards.html (script order), so the global is always
     present by the time `stripCounts` below runs.

     THE READ: `flashcard_pupil_detail(p_assignment, p_pupil)` — the same
     RPC the per-pupil sheet already calls, the teacher can already read
     it, no new grant. `flashcard_progress` (this page's own read) has no
     per-card list, only per-pupil counts, so a pupil's true 5-state split
     is not knowable until their detail is fetched.

     THE COST CONTROL — three rules, all load-bearing:
     · a pupil with 0 sittings is skipped entirely (every card is Not
       seen by construction; no RPC can tell us anything a zero can't).
     · DETAIL_SIG remembers the (secured, known, sittings, last_active)
       tuple the cache reflects; a poll that re-fetches `flashcard_
       progress` and finds that tuple UNCHANGED for a pupil never queues
       a re-fetch of their detail — this is what keeps an idle 10s poll
       at 0 additional RPCs.
     · DETAIL_MAX caps concurrent `flashcard_pupil_detail` calls; a
       30-pupil first load queues 30 and drains them 4 at a time rather
       than firing 30 requests at once.

     UNTIL A PUPIL'S DETAIL ARRIVES (or if the RPC errors), `stripCounts`
     falls back to the count-based 3-bucket approximation the port
     shipped with — never a blank cell, never an error string. */
  var DETAIL_MAX = 4;
  var DETAIL_CACHE = {};   // pupil_id -> cards[] (real data) | null (fetched, empty/errored)
  var DETAIL_SIG = {};     // pupil_id -> the progress-row signature this cache entry reflects
  var DETAIL_QUEUE = [];   // pupil_ids waiting for a free slot
  var DETAIL_ACTIVE = 0;   // requests currently in flight

  function pupilSig(p) {
    return [p.secured, p.known, p.sittings, p.last_active].join("|");
  }

  function pumpDetailQueue() {
    while (DETAIL_ACTIVE < DETAIL_MAX && DETAIL_QUEUE.length) {
      fetchDetail(DETAIL_QUEUE.shift());
    }
  }

  function fetchDetail(pid) {
    DETAIL_ACTIVE++;
    S.sb.rpc("flashcard_pupil_detail", { p_assignment: S.id, p_pupil: pid })
      .then(function (r) {
        DETAIL_CACHE[pid] = (r && !r.error && r.data && r.data.cards) ? r.data.cards : null;
      }, function () { DETAIL_CACHE[pid] = null; })
      .then(function () {
        DETAIL_ACTIVE--;
        /* Redraw now so this one row fills in without waiting for the
           rest of the queue — never re-triggers ensureDetail (that only
           runs from a fresh `flashcard_progress` read, in render()). */
        if (S.data && !recomputeTruth()) { renderTable(S.data); }
        pumpDetailQueue();
      });
  }

  /* Called once per real progress read (initial load + every poll) —
     never from a plain re-sort, which reuses S.data and fetches nothing
     new. Queues exactly the pupils whose (secured, known, sittings,
     last_active) tuple has changed since the cache was last filled for
     them, which is the whole of the "0 RPCs on an idle poll" guarantee:
     nothing about a pupil's row changing means nothing about their cards
     could have changed either. */
  function ensureDetail(pupils) {
    (pupils || []).forEach(function (p) {
      if (!p.sittings) { return; }
      var sig = pupilSig(p);
      if (DETAIL_SIG[p.pupil_id] === sig) { return; }
      if (DETAIL_QUEUE.indexOf(p.pupil_id) !== -1) { return; }
      DETAIL_SIG[p.pupil_id] = sig;
      DETAIL_QUEUE.push(p.pupil_id);
    });
    pumpDetailQueue();
  }

  /* ⊕ MRB-354 (2 Oct 2026) — FOUR counts for one pupil's strip, best state
     first ("Got it" is gone — a card secures the moment any rating of it is
     got_it, so there is no separate "got it but not yet secured" bucket any
     more). Real data when `flashcard_pupil_detail` has landed for their
     CURRENT sig; otherwise the count-based fallback (`p.known` from
     `flashcard_progress` only — Nearly and Not yet can't be told apart from
     Not seen with counts alone, so both read 0 rather than guess). */
  function stripCounts(p, n) {
    if (!p.sittings) {
      return { secured: 0, nearly: 0, not_yet: 0, unseen: n };
    }
    var cards = DETAIL_CACHE[p.pupil_id];
    if (cards) {
      var FB = window.MRBFlashcardBreakdown;
      var counts = { secured: 0, nearly: 0, not_yet: 0, unseen: 0 };
      cards.forEach(function (c) {
        var st = (FB && FB.cardState) ? FB.cardState(c) : { key: "unseen" };
        var key = Object.prototype.hasOwnProperty.call(counts, st.key) ? st.key : "unseen";
        counts[key] += 1;
      });
      var counted = counts.secured + counts.nearly + counts.not_yet + counts.unseen;
      counts.unseen += Math.max(0, n - counted);
      return counts;
    }
    var secured = Math.max(0, Math.min(p.known || 0, n));
    var unseen = Math.max(0, n - secured);
    return { secured: secured, nearly: 0, not_yet: 0, unseen: unseen };
  }


  /* ═════════════════════════════════════════════════════════════════════
     ⊕ Flashcards round 3 (teacher), Oct 2026 — EFFORT is not UNDERSTANDING.

     The status chip says what a pupil DID; a pupil who presses "I don't
     know" on every card still reaches Done. So each refresh also reads, class
     wide and through the teacher's own client (RLS already lets a class
     teacher / school admin / SLT select all three):
       · flashcard_events  — answer_submitted rows whose answer is the IDK text
       · flashcard_reviews — rating + typed answer + the check's verdict
       · flashcard_pupil_cards — the make-pass answer + verdict
     and shared/flashcard-truth.js (pure, node-tested) folds them into "which
     cards is each pupil unsure of" and one class-wide reteach list.

     THE DECK comes from `flashcard_pupil_detail` (already fetched for the
     strip), never from `assignment_flashcards`: pool_ownership forbids any
     question/answer read of that table outside the library.

     A read that errors, or that returns nothing for a class that has done
     work, settles `S.truth = {failed:true}`: the page then says NOTHING about
     understanding and keeps the RPC's own reteach list. Never "all confident"
     without data. */
  var PAGE = 1000;
  var IDK_FILTER = "I don't know";

  async function readAll(make) {
    var out = [];
    for (var from = 0, guard = 0; guard < 200; guard++, from += PAGE) {
      var r = await make().range(from, from + PAGE - 1);
      if (!r || r.error) { throw (r && r.error) || new Error("read_failed"); }
      var rows = r.data || [];
      out = out.concat(rows);
      if (rows.length < PAGE) { return out; }
    }
    throw new Error("too_many_rows");
  }

  async function refreshTruth() {
    if (S.truthBusy || !S.data || !S.sb) { return; }
    var pupils = S.data.pupils || [];
    /* Re-read only when the class's ACTIVITY changed (each pupil's status,
       last_active, known, sittings and verdict split); an unchanged poll
       reuses S.truth. A failed read retries on a changed signature or after
       ~60 s, never every poll. */
    var sig = pupils.map(function (p) {
      return [p.pupil_id, p.status, p.last_active, p.known, p.sittings, JSON.stringify(p.answers || {})].join("|");
    }).join(";");
    if (S.truthSig === sig) {
      if (S.truthRows !== false) { return; }
      if (Date.now() - S.truthFailAt < 60000) { return; }
    }
    S.truthSig = sig;
    if (!pupils.some(function (p) { return p.sittings; })) {
      /* Nobody has done anything: nothing to read, and every line is blank. */
      S.truthRows = { idk: [], reviews: [], pupilCards: [], idle: true };
      recomputeTruth();
      return;
    }
    S.truthBusy = true;
    var id = S.id;
    try {
      var got = await Promise.all([
        readAll(function () {
          return S.sb.from("flashcard_events").select("pupil_id, card_id, type, answer")
            .eq("assignment_id", id).eq("type", "answer_submitted").eq("answer", IDK_FILTER).order("id");
        }),
        readAll(function () {
          return S.sb.from("flashcard_reviews").select("pupil_id, card_id, rating, answer, answer_check")
            .eq("assignment_id", id).order("id");
        }),
        readAll(function () {
          return S.sb.from("flashcard_pupil_cards").select("pupil_id, card_id, pupil_answer, answer_check")
            .eq("assignment_id", id).order("pupil_id").order("card_id");
        })
      ]);
      S.truthRows = { idk: got[0], reviews: got[1], pupilCards: got[2] };
    } catch (e) {
      console.warn("[flashcards] understanding read failed", e);
      S.truthRows = false;
      S.truthFailAt = Date.now();
    } finally {
      S.truthBusy = false;
    }
    recomputeTruth();
  }

  function deckFromDetails() {
    for (var pid in DETAIL_CACHE) {
      if (!Object.prototype.hasOwnProperty.call(DETAIL_CACHE, pid)) { continue; }
      var cards = DETAIL_CACHE[pid];
      if (cards && cards.length) {
        return cards.map(function (c) { return { id: c.id, position: c.position, question: c.question }; });
      }
    }
    return null;
  }

  /* Folds the rows into S.truth and repaints the two places it shows.
     Returns true when it repainted (so a caller need not paint again). */
  function recomputeTruth() {
    var T = window.MRBFlashcardTruth;
    if (!S.data) { return false; }
    var next;
    if (!T || S.truthRows === false) { next = { failed: true }; }
    else if (S.truthRows == null) { return false; }
    else if (S.truthRows.idle) { next = { byPupil: {}, reteach: [], n: 0 }; }
    else {
      var deck = deckFromDetails();
      if (!deck) {
        if (DETAIL_ACTIVE || DETAIL_QUEUE.length) { return false; }
        next = { failed: true };
      } else {
        next = T.build({ pupils: S.data.pupils || [], cards: deck, expectActivity: true,
                         idk: S.truthRows.idk, reviews: S.truthRows.reviews,
                         pupilCards: S.truthRows.pupilCards });
      }
    }
    S.truth = next;
    var body = $("fp-body");
    if (body) { body.setAttribute("data-truth", next.failed ? "failed" : "ok"); }
    renderStrip(S.data);
    renderTable(S.data);
    return true;
  }

  /* The understanding text beside a status chip ("" when there is none). */
  function understanding(p, n) {
    var T = window.MRBFlashcardTruth;
    return (T && S.truth) ? T.pupilLine(S.truth, p, n) : "";
  }

  function nowIso() { return new Date().toISOString(); }

  function rpcCode(err) {
    var m = (err && (err.message || err.code)) || "";
    return String(m).trim();
  }

  async function fetchProgress() {
    var r = await S.sb.rpc("flashcard_progress", { p_assignment: S.id, p_now: nowIso() });
    if (r.error) { var e = new Error(rpcCode(r.error)); e.code = rpcCode(r.error); throw e; }
    return r.data;
  }

  /* ── the header ───────────────────────────────────────────────────────── */
  function renderHead(d) {
    var a = d.assignment || {};
    var st = assignmentState(a, d.now || nowIso());
    var host = clear($("fp-head"));

    /* ⊕ Sharpen C6 (T46) — the parent class is the bar's "‹ 8r/Sc1" link,
       as on every generated teacher page; no eyebrow above the title. */
    var env = (window.MrBadmusConfig && window.MrBadmusConfig.environment === "test") ? "&env=test" : "";
    var bar = $("fp-bar-crumb");
    if (bar) {
      bar.textContent = "‹ " + (a.class_name || "");
      bar.href = "/teacher/class-detail.html?class=" + encodeURIComponent(a.class_id || "") + env;
      bar.hidden = !a.class_name;
    }

    var title = h("h1", "fp-title", a.title || "");
    var meta = h("div", "fp-meta");
    meta.appendChild(h("span", "fp-due", "Due " + londonWhen(a.due_at)));
    if (st === "scheduled") {
      meta.appendChild(h("span", "fp-sep", "·"));
      meta.appendChild(h("span", "fp-rel", "Opens " + londonWhen(a.release_at)));
    }

    var left = h("div", "fp-head-main");
    left.appendChild(title); left.appendChild(meta);
    if (a.note) {
      var note = h("p", "fp-note");
      note.setAttribute("data-fp-data", "note");
      note.textContent = a.note;
      left.appendChild(note);
    }

    var acts = h("div", "fp-actions");
    var edit = h("button", "btn fp-btn", "Edit");
    edit.type = "button"; edit.id = "fp-edit";
    edit.addEventListener("click", openEdit);
    var csv = h("button", "btn fp-btn", "Export CSV");
    csv.type = "button"; csv.id = "fp-csv";
    csv.addEventListener("click", exportCsv);
    acts.appendChild(edit); acts.appendChild(csv);

    host.appendChild(left); host.appendChild(acts);
    document.title = (a.title || "Flashcards") + " — MrBadmus";
  }

  /* ── the class strip ──────────────────────────────────────────────────── */
  function tile(label, value, sub, id) {
    var t = h("div", "fp-tile");
    if (id) { t.id = id; }
    t.appendChild(h("div", "fp-tile-label", label));
    t.appendChild(h("div", "fp-tile-value", value));
    if (sub) { t.appendChild(h("div", "fp-tile-sub", sub)); }
    return t;
  }

  function renderStrip(d) {
    var c = d.class || {};
    var host = clear($("fp-strip"));
    var tiles = h("div", "fp-tiles");
    /* ⊕ Sharpen C6 (T44) — "2/6", not "2/6" over "33%". */
    tiles.appendChild(tile("Done", (c.done || 0) + "/" + (c.pupils || 0), null, "fp-done"));
    tiles.appendChild(tile("Average sittings",
                           c.avg_sittings == null ? "—" : String(c.avg_sittings), null, "fp-avg"));
    host.appendChild(tiles);

    host.classList.toggle("fp-strip-solo", false);
    /* ONE reteach list. With the understanding read settled it is the
       per-card one (unsure pupils, hardest first); until then nothing; if the
       read failed, the RPC's own "Most often Not yet" so the teacher is not
       left blind. */
    if (S.truth && !S.truth.failed) {
      if (!S.truth.reteach.length) { host.classList.add("fp-strip-solo"); return; }
      var tc = h("div", "fp-reteach");
      tc.id = "fp-reteach";
      tc.appendChild(h("div", "fp-tile-label", "Reteach"));
      var tl = h("ol", "fp-rt-list fp-rt-scroll");
      S.truth.reteach.forEach(function (r) {
        var li = h("li", "fp-rt-row fp-rt-card");
        li.setAttribute("data-card", r.id);
        var top = h("div", "fp-rt-top");
        top.appendChild(h("span", "fp-rt-no", String((r.position || 0) + 1)));
        var q = sci("span", "fp-rt-q", r.question);
        q.setAttribute("data-fp-data", "question");
        top.appendChild(q);
        li.appendChild(top);
        var meta = h("div", "fp-rt-meta");
        var bits = [["don't know", r.idk, "fp-rt-i"],
                    ["Nearly/Wrong", r.weak, "fp-rt-w"], ["secured anyway", r.securedAnyway, "fp-rt-s"]];
        bits.forEach(function (b) {
          if (!b[1]) { return; }
          var sp = h("span", "fp-rt-bit " + b[2], b[1] + " " + b[0]);
          sp.setAttribute("data-bit", b[2]);
          meta.appendChild(sp);
        });
        li.appendChild(meta);
        tl.appendChild(li);
      });
      tc.appendChild(tl);
      host.appendChild(tc);
      return;
    }
    if (!S.truth) { host.classList.add("fp-strip-solo"); return; }
    var rt = (c.reteach || []).slice(0, 5);
    var card = h("div", "fp-reteach");
    card.id = "fp-reteach";
    card.appendChild(h("div", "fp-tile-label", "Most often Not yet"));
    if (!rt.length) {
      card.appendChild(h("div", "fp-empty", "None yet"));
    } else {
      var ol = h("ol", "fp-rt-list");
      rt.forEach(function (r) {
        var li = h("li", "fp-rt-row");
        var q = sci("span", "fp-rt-q", r.question);
        q.setAttribute("data-fp-data", "question");
        li.appendChild(q);
        var n = h("span", "fp-rt-n", String(r.not_yet));
        n.setAttribute("aria-label", r.not_yet + " Not yet");
        li.appendChild(n);
        ol.appendChild(li);
      });
      card.appendChild(ol);
    }
    host.appendChild(card);
  }

  /* ── the table ────────────────────────────────────────────────────────── */
  function statusChip(status) {
    var s = STATUS[status] || STATUS.not_started;
    var c = h("span", "fp-status fp-st-" + s.tone);
    c.appendChild(h("span", "fp-dot"));
    c.appendChild(h("span", null, s.label));
    c.setAttribute("data-status", status || "not_started");
    return c;
  }

  /* ⊕ MRB-354 (2 Oct 2026) — a per-card state strip, sorted best to worst,
     FOUR states now ("Got it" is gone — a card secures on one rating, so
     there is no separate "got it but not yet secured" bucket to show).
     `stripCounts` above (real detail when cached, the count-based fallback
     otherwise) is the one place that decides the numbers; this function
     only draws them, in the fixed best-to-worst cell order. The number is
     `p.known` — the RPC's `known`, which IS "secured" under the new rule,
     correct before and after the parked SQL (§6). The completion-rule
     ("Secure"/"Quick") distinction this cell used to show a tooltip for is
     gone along with the rest of that choice (§7) — completion_rule no
     longer means anything to secured/done. */
  function securedCell(p, n) {
    var w = h("div", "fp-sec");
    var num = h("span", "fp-sec-n");
    num.appendChild(document.createTextNode(String(p.known || 0)));
    num.appendChild(h("small", null, "/" + n));
    w.appendChild(num);
    var c = stripCounts(p, n);
    var strip = h("span", "strip");
    strip.setAttribute("role", "img");
    strip.setAttribute("aria-label", c.secured + " secured, " +
      c.nearly + " nearly, " + c.not_yet + " not yet, " + c.unseen + " not seen");
    [["k-sec", c.secured], ["k-near", c.nearly],
     ["k-no", c.not_yet], ["k-un", c.unseen]].forEach(function (pair) {
      for (var i = 0; i < pair[1]; i++) { strip.appendChild(h("i", pair[0])); }
    });
    w.appendChild(strip);
    return w;
  }

  function renderTable(d) {
    var a = d.assignment || {}, n = d.n || 0;
    var cols = columnsFor(a.mode);
    var table = $("fp-table");
    table.classList.toggle("fp-review", a.mode !== "make");
    var cg = table.querySelector("colgroup");
    if (!cg) { cg = h("colgroup"); table.insertBefore(cg, table.firstChild); }
    clear(cg);
    cols.forEach(function (c) {
      var col = h("col", "fp-cg-" + c.key);
      if (c.w) { col.style.width = c.w + "px"; }
      cg.appendChild(col);
    });
    var thead = clear(table.tHead || table.createTHead());
    var tr = h("tr");
    cols.forEach(function (c) {
      var th = h("th", "fp-th fp-col-" + c.key);
      th.scope = "col";
      var on = S.sortKey === c.key;
      th.setAttribute("aria-sort", on ? (S.sortDir === "desc" ? "descending" : "ascending") : "none");
      var b = h("button", "fp-sort", c.label);
      b.type = "button";
      b.setAttribute("data-sort", c.key);
      b.addEventListener("click", function () {
        if (S.sortKey === c.key) { S.sortDir = S.sortDir === "asc" ? "desc" : "asc"; }
        else { S.sortKey = c.key; S.sortDir = "asc"; }
        renderTable(S.data);
      });
      th.appendChild(b);
      tr.appendChild(th);
    });
    thead.appendChild(tr);

    var tbody = table.tBodies[0] || table.appendChild(h("tbody"));
    clear(tbody);
    var rows = sortRows(d.pupils || [], S.sortKey, S.sortDir);
    var nowMs = Date.now();
    if (!rows.length) {
      var er = h("tr"), td = h("td", "fp-empty", SAY.noPupils);
      td.colSpan = cols.length; er.appendChild(td); tbody.appendChild(er);
    }
    rows.forEach(function (p) {
      var row = h("tr", "fp-row");
      row.setAttribute("data-pupil", p.pupil_id);
      row.setAttribute("data-status", p.status || "");
      if (S.truth && !S.truth.failed && window.MRBFlashcardTruth) {
        row.setAttribute("data-unsure", String(window.MRBFlashcardTruth.unsure(S.truth, p.pupil_id)));
      }
      cols.forEach(function (c) {
        var td = h(c.key === "pupil" ? "th" : "td", "fp-td fp-col-" + c.key);
        if (c.key === "pupil") {
          td.scope = "row";
          var b = h("button", "fp-name", nameOf(p));
          b.type = "button";
          b.addEventListener("click", function (e) { e.stopPropagation(); openPupil(p); });
          td.appendChild(b);
          /* ⊕ Design port A — below 640px the Status COLUMN hides (ruled:
             "Pupil… and Secured only, nothing ellipsised") and this chip
             carries the same fact under the name instead. `ph-only` is
             CSS-only (display:none above 640px); no data any other cell
             doesn't already have. */
          var phChip = statusChip(p.status);
          phChip.classList.add("ph-only");
          td.appendChild(phChip);
          var phU = understanding(p, n);
          if (phU) {
            var phUe = h("span", "fp-und ph-only", phU);
            phUe.setAttribute("data-fp-und", "1");
            td.appendChild(phUe);
          }
        } else if (c.key === "status") {
          td.appendChild(statusChip(p.status));
          var u = understanding(p, n);
          if (u) {
            var ue = h("span", "fp-und", u);
            ue.setAttribute("data-fp-und", "1");
            td.appendChild(ue);
          }
        } else if (c.key === "secured") {
          td.appendChild(securedCell(p, n));
        } else if (c.key === "time") {
          td.appendChild(document.createTextNode(cellText(p, c.key, n, a.mode, a.rule, nowMs)));
          /* ⊕ Design port A — Rushed is a small inline marker INSIDE the
             Time cell now, never its own column (cut, as ruled). */
          if (p.rushed) { td.appendChild(h("span", "fp-rushed", "Rushed")); }
        } else {
          td.textContent = cellText(p, c.key, n, a.mode, a.rule, nowMs);
          if (c.key === "last" && p.last_active) { td.title = londonWhen(p.last_active); }
        }
        row.appendChild(td);
      });
      row.addEventListener("click", function () { openPupil(p); });
      tbody.appendChild(row);
    });
  }

  function render(d) {
    S.data = d;
    renderHead(d);
    renderStrip(d);
    renderTable(d);
    $("fp-skel").hidden = true;
    $("fp-body").hidden = false;
    /* Initial load AND every poll land here (both go through render()) —
       never a bare re-sort, which calls renderTable() directly on the
       same S.data. See ensureDetail's own comment for the 0-RPCs-when-
       nothing-changed guarantee this placement is what delivers. */
    ensureDetail(d.pupils || []);
    refreshTruth();
  }

  /* ── live: every 10 s while visible ───────────────────────────────────── */
  async function refresh() {
    if (S.inflight) { return; }
    S.inflight = true;
    try {
      render(await fetchProgress());
    } catch (e) {
      if (!S.data) { fail(e); }
      else { console.warn("[flashcards] refresh failed", e); }
    } finally {
      S.inflight = false;
    }
  }

  function startPolling() {
    stopPolling();
    if (document.visibilityState === "hidden") { return; }
    S.timer = setInterval(refresh, POLL_MS);
  }
  function stopPolling() { if (S.timer) { clearInterval(S.timer); S.timer = null; } }

  document.addEventListener("visibilitychange", function () {
    // ⊕ MRB-351 landing — `S.notSwitchedOn` (set by `start()`'s capability
    // check) stops a tab-focus refresh from re-attempting the same read
    // `start()` already declined to make.
    if (!S.id || !S.sb || S.notSwitchedOn) { return; }
    if (document.visibilityState === "hidden") { stopPolling(); }
    else { refresh(); startPolling(); }
  });

  /* ── answer check: fire and forget ────────────────────────────────────── */
  async function kickAnswerCheck() {
    try {
      var cfg = window.MrBadmusConfig || {};
      var sess = await S.sb.auth.getSession();
      var tok = sess && sess.data && sess.data.session && sess.data.session.access_token;
      if (!tok || !cfg.SUPABASE_URL) { return; }
      var res = await fetch(cfg.SUPABASE_URL + "/functions/v1/flashcard-answer-check", {
        method: "POST",
        headers: { "Content-Type": "application/json", Authorization: "Bearer " + tok,
                   apikey: cfg.SUPABASE_ANON_KEY || "" },
        body: JSON.stringify({ assignment_id: S.id })
      });
      if (res && res.ok) { refresh(); }
    } catch (e) { /* the pending answers stay "…" until the next open */ }
  }

  /* ── CSV ──────────────────────────────────────────────────────────────── */
  function exportCsv() {
    if (!S.data) { return; }
    var rows = sortRows(S.data.pupils || [], S.sortKey, S.sortDir);
    var text = buildCsv(S.data, rows, S.truth);
    var name = csvFilename(S.data.assignment || {});
    window.__MRB_FP_LAST_CSV__ = { name: name, text: text };
    try {
      var blob = new Blob([text], { type: "text/csv;charset=utf-8" });
      var url = URL.createObjectURL(blob);
      var link = document.createElement("a");
      link.href = url; link.download = name;
      document.body.appendChild(link); link.click();
      setTimeout(function () { URL.revokeObjectURL(url); link.remove(); }, 0);
    } catch (e) { console.warn("[flashcards] export failed", e); }
  }

  /* ── one pupil: the centred panel (shared/flashcard-breakdown.js) ───────
     ⊕ Sharpen B3 — replaces the right-hand drawer. Handed THIS page's
     payload and the table's current order, so prev/next walk the rows as
     the teacher sees them and opening costs one read. The panel keeps its
     own snapshot: the 10-second poll repaints the table, never the panel. */
  function openPupil(p) {
    var FB = window.MRBFlashcardBreakdown;
    if (!FB || !S.data) { return; }
    var order = sortRows(S.data.pupils || [], S.sortKey, S.sortDir)
      .map(function (x) { return x.pupil_id; });
    FB.open({ assignmentId: S.id, studentId: p.pupil_id,
              classId: (S.data.assignment || {}).class_id,
              progress: S.data, order: order, chem: S.chem });
  }

  /* ── Edit ─────────────────────────────────────────────────────────────── */
  function toast(text) {
    var t = $("fp-toast");
    t.textContent = text;
    t.hidden = false;
    clearTimeout(toast._t);
    toast._t = setTimeout(function () { t.hidden = true; }, 2600);
  }

  function lonParts(iso) {
    var SW = window.MRBSetWork;
    if (SW && SW.utcToLondonParts && iso) { return SW.utcToLondonParts(iso); }
    return { date: "", time: "" };
  }
  function lonIso(date, time) {
    var SW = window.MRBSetWork;
    return (SW && SW.londonToUtcIso) ? SW.londonToUtcIso(date, time) : null;
  }

  function openEdit() {
    if (!S.data) { return; }
    var a = S.data.assignment || {};
    var unreleased = !!(a.release_at && a.release_at > nowIso());
    $("fp-ed-title").value = a.title || "";
    var due = lonParts(a.due_at);
    $("fp-ed-due-date").value = due.date; $("fp-ed-due-time").value = due.time;
    $("fp-ed-note").value = a.note || "";
    $("fp-ed-rel-wrap").hidden = !unreleased;
    if (unreleased) {
      var rel = lonParts(a.release_at);
      $("fp-ed-rel-date").value = rel.date; $("fp-ed-rel-time").value = rel.time;
    }
    $("fp-ed-err").textContent = "";
    ["fp-ed-title", "fp-ed-due-date", "fp-ed-due-time", "fp-ed-rel-date", "fp-ed-rel-time", "fp-ed-note"]
      .forEach(function (id) { $(id).classList.remove("sw-bad"); });
    S.lastFocus = document.activeElement;
    $("fp-edit-back").hidden = false;
    $("fp-ed-title").focus();
  }
  function closeEdit() {
    $("fp-edit-back").hidden = true;
    if (S.lastFocus && S.lastFocus.focus) { try { S.lastFocus.focus(); } catch (e) {} }
  }

  async function saveEdit() {
    var a = S.data.assignment || {};
    var title = $("fp-ed-title").value.trim();
    var note = $("fp-ed-note").value.trim();
    var dueIso = lonIso($("fp-ed-due-date").value, $("fp-ed-due-time").value);
    var relOn = !$("fp-ed-rel-wrap").hidden;
    var relIso = relOn ? lonIso($("fp-ed-rel-date").value, $("fp-ed-rel-time").value) : null;
    var bad = [];
    if (!title || title.length > 120) { bad.push("fp-ed-title"); }
    if (!dueIso) { bad.push("fp-ed-due-date", "fp-ed-due-time"); }
    if (relOn && !relIso) { bad.push("fp-ed-rel-date", "fp-ed-rel-time"); }
    if (note.length > 300) { bad.push("fp-ed-note"); }
    ["fp-ed-title", "fp-ed-due-date", "fp-ed-due-time", "fp-ed-rel-date", "fp-ed-rel-time", "fp-ed-note"]
      .forEach(function (id) { $(id).classList.toggle("sw-bad", bad.indexOf(id) > -1); });
    if (bad.length) { return; }
    var btn = $("fp-ed-save");
    btn.disabled = true;
    var r;
    try {
      r = await S.sb.rpc("flashcard_edit_assignment", {
        p_id: S.id, p_title: title, p_due_at: dueIso, p_note: note || null,
        p_release_at: relOn ? relIso : null
      });
    } catch (e) { r = { error: e }; }
    btn.disabled = false;
    if (r && r.error) {
      var code = rpcCode(r.error);
      var msg = { due_before_release: SAY.dueBeforeRelease, release_past: SAY.releasePast,
                  bad_title: SAY.badTitle, bad_note: SAY.badNote }[code] || SAY.saveFailed;
      $("fp-ed-err").textContent = msg;
      return;
    }
    closeEdit();
    toast((title || a.title) + " · " + SAY.saved);
    refresh();
  }

  /* ── failure ──────────────────────────────────────────────────────────── */
  function fail(e) {
    var code = (e && (e.code || e.message)) || "";
    $("fp-skel").hidden = true;
    $("fp-body").hidden = true;
    var n = $("fp-notice");
    n.hidden = false;
    $("fp-notice-title").textContent =
      code === "not_switched_on" ? SAY.notSwitchedOn
        : (/not_found|not_yours|42501|invalid input syntax/i.test(code)) ? SAY.notFound
        : SAY.failed;
    stopPolling();
  }

  /* ── boot ─────────────────────────────────────────────────────────────── */
  function wire() {
    $("fp-ed-cancel").addEventListener("click", closeEdit);
    $("fp-ed-save").addEventListener("click", saveEdit);
    $("fp-edit-back").addEventListener("click", function (e) {
      if (e.target === $("fp-edit-back")) { closeEdit(); }
    });
    document.addEventListener("keydown", function (e) {
      if (e.key !== "Escape") { return; }
      if (!$("fp-edit-back").hidden) { closeEdit(); }
    });
  }

  async function start() {
    wire();
    var q = new URLSearchParams(window.location.search);
    S.id = q.get("assignment");
    var guard = window.MrBadmusTeacherGuard;
    S.sb = guard && guard.getClient ? guard.getClient() : null;
    if (!S.id || !S.sb) { fail({ code: "not_found" }); return; }
    /* ⊕ MRB-351 landing (27 Sep 2026) — the SAME shared, cached probe the
       Set work sheet and the "Flashcard decks" nav link both use
       (`window.MrBadmusAdminScope.flashcardsCapable()`). This page's own
       address is only ever reached from a live flashcard assignment row —
       which cannot exist without the schema, so this is unreachable in the
       ordinary click-through flow — but a hand-typed or bookmarked
       `?assignment=<id>` bypasses that. On `false`, `fetchProgress()` is
       never called: it would otherwise read `assignments`/the flashcard
       RPCs directly and fail (PGRST205/42703 on production today). */
    var scope = window.MrBadmusAdminScope;
    var capable = scope && scope.flashcardsCapableSettled
      ? await scope.flashcardsCapableSettled().catch(function () { return false; })
      : false;
    if (!capable) { S.notSwitchedOn = true; fail({ code: "not_switched_on" }); return; }
    /* ⊕ Set from class (M), 27 Sep 2026 — the progress RPC carries no
       subject, so one read decides whether formulae are drawn. Any failure
       leaves the text plain. */
    try {
      var subj = await S.sb.from("assignments").select("subject:subjects(name)")
        .eq("id", S.id).maybeSingle();
      var sname = subj && subj.data && subj.data.subject && subj.data.subject.name;
      S.chem = String(sname || "").toLowerCase() === "chemistry";
    } catch (e) { S.chem = false; }
    try {
      render(await fetchProgress());
    } catch (e) { fail(e); return; }
    kickAnswerCheck();
    startPolling();
  }

  window.MRBFlashcardProgress = {
    start: start,
    refresh: refresh,
    // pure, for the drive
    sortRows: sortRows, buildCsv: buildCsv, csvFilename: csvFilename,
    columnsFor: columnsFor, relative: relative, clock: clock, seconds: seconds,
    londonWhen: londonWhen, assignmentState: assignmentState,
    STATUS: STATUS, POLL_MS: POLL_MS,
    _state: S
  };
})();
