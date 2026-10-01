/* ═══════════════════════════════════════════════════════════════════════
   flashcard-breakdown.js — one pupil's flashcard set, for the teacher
   (Sharpen B3, 29 Sep 2026). The flashcard twin of shared/breakdown.js:
   the SAME shell (`.bd-overlay` fixed on <body>, the 880px `.bd-sheet`,
   eyebrow / title / prev / next / close), the same focus and scroll rules,
   styled by shared/breakdown.css. It imports none of breakdown.js's MCQ
   loaders — a deck has no questions table and no submission until done.

   Surface:  window.MRBFlashcardBreakdown.open({assignmentId, studentId,
                 classId, progress?, order?, chem?})
             .close()

   `progress` is a `flashcard_progress` payload the caller already holds
   (teacher/flashcards.html passes its own, so opening costs one read);
   without it the panel reads it. `order` is the pupil ids in the order the
   caller shows them (the table's current sort) — prev/next walk THAT
   order; without it, the RPC's own surname order.

   Reads, all through the signed-in teacher's client, definer-gated:
     rpc flashcard_progress      {p_assignment, p_now}   the roster + tiles
     rpc flashcard_pupil_detail  {p_assignment, p_pupil} one pupil's cards
     from assignments select subject:subjects(name)       formulae on/off

   ⚠️ DEGRADES ON THE PRE-MRB-352 FUNCTION. `ratings[].answer`,
   `ratings[].answer_check` and `cards[].shown` arrive with migration
   20260930090000_mrb352_flashcard_pupil_detail_answers (parked branch
   feat/mrb352-migrations). Until it lands:
     · the written answer is the make-pass answer (`mine`/`check`), else the
       box reads "No written answer";
     · TRIES COUNTS RATED PASSES (`ratings.length`), not the times the card
       was shown. After the migration it is the exact shown-count.

   ⚠️ NOTHING HERE BUILDS HTML FROM A STRING a pupil or teacher typed.
   Card sides and answers reach the page as text nodes, or through
   MRBFormulae.fill (which builds <sub> elements) on a Chemistry set.
   ═══════════════════════════════════════════════════════════════════════ */
(function () {
  "use strict";

  var TZ = "Europe/London";
  var MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep",
                "Oct", "Nov", "Dec"];

  /* One word per state — the tile says on time / late, so the chip never
     repeats it. */
  var STATUS = {
    done: "Done", done_late: "Done", in_progress: "In progress",
    not_started: "Not started", missing: "Missing"
  };
  var RATING = { got_it: "Got it", nearly: "Nearly", not_yet: "Not yet" };
  var VERDICT = { match: "Right", partial: "Nearly", no: "Wrong",
                  blank: "Blank", pending: "Checking" };

  /* ── pure helpers (exported for the drive) ────────────────────────────── */
  function pad2(n) { return (n < 10 ? "0" : "") + n; }

  function nameOf(p) {
    var n = [p && p.first_name, p && p.last_name].filter(Boolean).join(" ").trim();
    return n || (p && p.display_name) || "Pupil";
  }

  function clock(ms) {
    if (ms == null || !isFinite(ms)) { return "—"; }
    var s = Math.max(0, Math.round(ms / 1000));
    var h = Math.floor(s / 3600), m = Math.floor((s % 3600) / 60), r = s % 60;
    return h ? (h + ":" + pad2(m) + ":" + pad2(r)) : (m + ":" + pad2(r));
  }

  function londonParts(iso) {
    var d = new Date(iso);
    if (!iso || isNaN(d.getTime())) { return null; }
    var o = {};
    new Intl.DateTimeFormat("en-GB", {
      timeZone: TZ, day: "numeric", month: "numeric", year: "numeric",
      hour: "2-digit", minute: "2-digit", hourCycle: "h23"
    }).formatToParts(d).forEach(function (p) { o[p.type] = p.value; });
    return o;
  }

  // "28 Sep 2026 at 20:45", London wall clock
  function whenLong(iso) {
    var p = londonParts(iso);
    if (!p) { return ""; }
    return (+p.day) + " " + MONTHS[(+p.month) - 1] + " " + p.year + " at " + p.hour + ":" + p.minute;
  }

  /* B2 — the verdict split, in words, zero buckets left out. */
  function verdictLine(a) {
    a = a || {};
    var bits = [];
    if (a.match) { bits.push(a.match + " right"); }
    if (a.partial) { bits.push(a.partial + " nearly"); }
    if (a.no) { bits.push(a.no + " wrong"); }
    if (a.blank) { bits.push(a.blank + " blank"); }
    if (a.pending) { bits.push(a.pending + " checking"); }
    return bits.join(" · ");
  }

  function latestRating(c) {
    var rs = (c && c.ratings) || [], best = null;
    rs.forEach(function (r) {
      if (!best || String(r.at || "") >= String(best.at || "")) { best = r; }
    });
    return best;
  }

  /* The ONE state chip on a card. */
  function cardState(c) {
    if (c.secured) { return { key: "secured", word: "Secured" }; }
    var r = latestRating(c);
    if (r && RATING[r.rating]) { return { key: r.rating, word: RATING[r.rating] }; }
    return { key: "unseen", word: "Not seen" };
  }

  /* The latest written answer: a review rating that carried one (MRB-352
     keys), else the make pass, else nothing. */
  function latestAnswer(c) {
    var rs = ((c && c.ratings) || []).filter(function (r) {
      return r.answer != null && String(r.answer) !== "";
    });
    if (rs.length) {
      var r = rs.reduce(function (a, b) { return String(b.at || "") >= String(a.at || "") ? b : a; });
      return { text: String(r.answer), check: r.answer_check || null, from: "review" };
    }
    /* A blank make-pass answer ("" with check `blank`) IS an answer — the
       pupil wrote nothing and the Blank verdict says so. */
    if (c && c.mine != null && (String(c.mine) !== "" || c.check === "blank")) {
      return { text: String(c.mine), check: c.check || null, from: "make" };
    }
    return null;
  }

  /* ⊕ Fable review, 29 Sep 2026 — WHEN TO SAY "No written answer". Only
     for a card the pupil has not touched (no rating, no make answer). On
     the pre-MRB-352 function a REVIEW answer is never returned, so a rated
     review-mode card with no answer in the payload says nothing rather
     than claiming the pupil wrote nothing. */
  function answerBox(c) {
    var ans = latestAnswer(c);
    if (ans) { return { kind: "answer", ans: ans }; }
    if (((c && c.ratings) || []).length) { return { kind: "omit" }; }
    return { kind: "none" };
  }

  /* Until the migration lands this counts RATED passes; after it, the
     number of times the card was shown. */
  function tries(c) {
    if (c && typeof c.shown === "number") { return c.shown; }
    /* Never "Tries: 0" beside an answer the pupil wrote. */
    return Math.max(((c && c.ratings) || []).length, latestAnswer(c) ? 1 : 0);
  }

  /* ── DOM helpers ──────────────────────────────────────────────────────── */
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
  function sci(tag, cls, text) {
    var e = el(tag, cls);
    if (S && S.chem && window.MRBFormulae && window.MRBFormulae.fill) { window.MRBFormulae.fill(e, text || ""); }
    else { e.textContent = text || ""; }
    return e;
  }
  function client() {
    var g = window.MrBadmusTeacherGuard;
    return (g && g.getClient) ? g.getClient() : null;
  }

  /* ── the shell: breakdown.js's, structurally ─────────────────────────── */
  var els = null, opener = null, session = 0, opens = 0, S = null, prevOverflow = null;

  function buildShell() {
    if (els) { return; }
    var overlay = el("div", "bd-overlay fb-overlay");
    overlay.hidden = true;
    overlay.setAttribute("data-fb", "overlay");

    var sheet = el("div", "bd-sheet");
    sheet.setAttribute("role", "dialog");
    sheet.setAttribute("aria-modal", "true");
    sheet.tabIndex = -1;
    sheet.setAttribute("data-fb", "sheet");

    var head = el("div", "bd-head");
    var close = btn("bd-close");
    close.setAttribute("aria-label", "Close");
    close.setAttribute("data-fb", "close");
    close.innerHTML = '<svg width="16" height="16" viewBox="0 0 16 16" fill="none" ' +
      'aria-hidden="true"><path d="M3 3l10 10M13 3L3 13" stroke="currentColor" ' +
      'stroke-width="1.6" stroke-linecap="round"/></svg>' +
      '<span class="bd-close-label">Close</span>';

    var main = el("div", "bd-head-main");
    var eyebrow = el("div", "bd-eyebrow");
    eyebrow.id = "fb-panel-heading";
    var titleRow = el("div", "fb-titlerow");
    var title = el("div", "bd-title");
    var chip = el("span", "fb-status");
    chip.setAttribute("data-fb", "status");
    titleRow.appendChild(title); titleRow.appendChild(chip);
    /* C2 — no "Pupil N of M", no due line. The node stays (hidden) so the
       shell keeps breakdown.js's shape for Design's redesign. */
    var subtitle = el("div", "bd-subtitle");
    subtitle.hidden = true;
    main.appendChild(eyebrow); main.appendChild(titleRow); main.appendChild(subtitle);
    sheet.setAttribute("aria-labelledby", "fb-panel-heading");

    var nav = el("div", "bd-nav");
    var prev = btn("bd-nav-btn");
    prev.setAttribute("data-fb", "prev");
    prev.innerHTML = '<svg width="14" height="14" viewBox="0 0 14 14" fill="none" ' +
      'aria-hidden="true"><path d="M8.5 2.5L4 7l4.5 4.5" stroke="currentColor" ' +
      'stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>' +
      '<span class="bd-nav-word"></span>';
    var next = btn("bd-nav-btn");
    next.setAttribute("data-fb", "next");
    next.innerHTML = '<span class="bd-nav-word"></span>' +
      '<svg width="14" height="14" viewBox="0 0 14 14" fill="none" aria-hidden="true">' +
      '<path d="M5.5 2.5L10 7l-4.5 4.5" stroke="currentColor" stroke-width="1.6" ' +
      'stroke-linecap="round" stroke-linejoin="round"/></svg>';
    nav.appendChild(prev); nav.appendChild(next);

    head.appendChild(close); head.appendChild(main); head.appendChild(nav);
    var body = el("div", "bd-body");
    var live = el("div", "bd-sr");
    live.setAttribute("aria-live", "polite");

    sheet.appendChild(head); sheet.appendChild(body); sheet.appendChild(live);
    overlay.appendChild(sheet);
    document.body.appendChild(overlay);

    els = { overlay: overlay, sheet: sheet, close: close, eyebrow: eyebrow,
            title: title, chip: chip, subtitle: subtitle, prev: prev, next: next,
            body: body, live: live };
    wireShell();
  }

  var FOCUSABLE = "button,[href],input,select,textarea,summary,[tabindex]";
  function focusables() {
    var all = els.sheet.querySelectorAll(FOCUSABLE), out = [];
    for (var i = 0; i < all.length; i++) {
      var n = all[i];
      if (n.disabled || n.getAttribute("tabindex") === "-1") { continue; }
      if (!n.offsetParent && n !== els.sheet) { continue; }
      out.push(n);
    }
    return out;
  }

  function wireShell() {
    els.overlay.addEventListener("click", function (e) { if (e.target === els.overlay) { close(); } });
    els.close.addEventListener("click", close);
    els.prev.addEventListener("click", function () { go(-1); });
    els.next.addEventListener("click", function () { go(1); });
    document.addEventListener("keydown", function (e) {
      if (!S || els.overlay.hidden) { return; }
      if (e.key === "Escape") { e.stopPropagation(); close(); return; }
      if (e.key === "ArrowLeft") { e.preventDefault(); go(-1); return; }
      if (e.key === "ArrowRight") { e.preventDefault(); go(1); return; }
      if (e.key !== "Tab") { return; }
      var items = focusables();
      if (!items.length) { return; }
      var first = items[0], last = items[items.length - 1], here = document.activeElement;
      if (e.shiftKey && (here === first || !els.sheet.contains(here))) { e.preventDefault(); last.focus(); }
      else if (!e.shiftKey && (here === last || !els.sheet.contains(here))) { e.preventDefault(); first.focus(); }
    }, true);
  }

  function close() {
    if (!els) { return; }
    session += 1;
    els.overlay.hidden = true;
    S = null;
    if (prevOverflow != null) { document.documentElement.style.overflow = prevOverflow; prevOverflow = null; }
    if (opener && opener.focus) { try { opener.focus({ preventScroll: true }); } catch (e) { /* gone */ } }
    opener = null;
  }

  function isOpen() { return !!(els && !els.overlay.hidden && S); }

  /* ── render ───────────────────────────────────────────────────────────── */
  function statTile(label, value, sub, cls) {
    var d = el("div", "bd-stat");
    d.appendChild(el("div", "bd-stat-label", label));
    var v = el("div", "bd-stat-value" + (cls ? " " + cls : ""), value);
    d.appendChild(v);
    if (sub) { d.appendChild(el("div", "bd-stat-sub", sub)); }
    return d;
  }

  function renderHeader() {
    var p = S.roster[S.idx];
    els.eyebrow.textContent = S.title || "Flashcards";
    els.title.textContent = nameOf(p);
    els.subtitle.textContent = "";
    var st = p.status || "not_started";
    els.chip.textContent = STATUS[st] || STATUS.not_started;
    els.chip.setAttribute("data-status", st);
    els.overlay.setAttribute("data-fb-student", p.pupil_id);
    var prevP = S.idx > 0 ? S.roster[S.idx - 1] : null;
    var nextP = S.idx < S.roster.length - 1 ? S.roster[S.idx + 1] : null;
    els.prev.disabled = !prevP;
    els.next.disabled = !nextP;
    els.prev.querySelector(".bd-nav-word").textContent = prevP ? nameOf(prevP) : "";
    els.next.querySelector(".bd-nav-word").textContent = nextP ? nameOf(nextP) : "";
    els.prev.setAttribute("aria-label", "Previous pupil" + (prevP ? ": " + nameOf(prevP) : ""));
    els.next.setAttribute("aria-label", "Next pupil" + (nextP ? ": " + nameOf(nextP) : ""));
  }

  function buildTiles(p, d) {
    var wrap = el("div", "bd-summary");
    var n = S.n || 0;
    wrap.appendChild(statTile("SECURED", (p.secured || 0) + " / " + n,
      S.make ? "made " + (p.made || 0) + " / " + n : null));
    var ses = (d && d.sessions) || [];
    var ms = ses.reduce(function (t, s) { return t + (s.active_ms || 0); }, 0);
    var sittings = ses.length || p.sittings || 0;
    var sub = sittings ? (sittings + (sittings === 1 ? " sitting" : " sittings")) + (p.rushed ? " · rushed" : "") : null;
    wrap.appendChild(statTile("TIME", ms ? clock(ms) : "—", sub));
    var st = p.status;
    /* ⊕ 1 Oct 2026 (sweep fix C6, corrected) — the ORIGINAL fallback was
       the single word "Not yet" for EVERY status that was neither done
       nor done_late — including "missing" (the due date has passed) —
       while the row pill one screen over (shared/flashcard-progress.js)
       says "Missing" for that same pupil. SWEEP C6 caught it on Aisha: the
       table said Missing, this sheet said Not yet, for the identical row.

       ⛔ THE FIRST FIX READ `STATUS[st]`, WHICH IS THE SAME WORD THE
       STATUS CHIP DIRECTLY ABOVE THIS TILE ALREADY SHOWS (`els.chip`,
       `renderHeader`, a few lines up) — it fixed the contradiction by
       making this tile repeat its neighbour, which is exactly the
       redundant-text rule this estate is held to (CLAUDE.md, 28 Sep;
       REVIEW.md #6). The chip already says why a pupil has not handed
       in; this tile does not need to say it a second time in different
       words. It now reads "—" for every one of those states, the same
       convention the TIME tile above uses for "nothing to report" (ms
       falsy → "—") — so the two "not handed in" tiles on this sheet
       agree with each other as well as with the chip. */
    var handed = st === "done" ? "On time" : (st === "done_late" ? "Late" : "—");
    wrap.appendChild(statTile("HANDED IN", handed,
      p.completed_at ? "Handed in " + whenLong(p.completed_at) : null,
      st === "done" ? "is-good" : (st === "done_late" ? "is-late" : null)));
    return wrap;
  }

  function buildToggle(cards) {
    var open = cards.filter(function (c) { return !c.secured; }).length;
    var wrap = el("div", "bd-toggle");
    var all = btn("bd-toggle-btn" + (!S.notSecured ? " is-on" : ""));
    all.textContent = "All " + cards.length;
    all.setAttribute("aria-pressed", String(!S.notSecured));
    all.setAttribute("data-fb", "filter-all");
    all.addEventListener("click", function () { setFilter(false); });
    var ns = btn("bd-toggle-btn" + (S.notSecured ? " is-on" : ""));
    ns.textContent = "Not secured " + open;
    ns.disabled = open === 0;
    ns.setAttribute("aria-pressed", String(S.notSecured));
    ns.setAttribute("data-fb", "filter-open");
    ns.addEventListener("click", function () { setFilter(true); });
    wrap.appendChild(all); wrap.appendChild(ns);
    return wrap;
  }
  function setFilter(on) {
    if (!S || S.notSecured === on) { return; }
    S.notSecured = on;
    renderBody();
  }

  function ratingChips(c) {
    /* Moved verbatim from flashcard-progress.js's old drawer: ratings are
       grouped under a small "while writing" / "in review" label, but only
       when the distinction exists on this card or the set is make mode. */
    var rs = c.ratings || [];
    var makeR = rs.filter(function (r) { return r.phase === "make"; });
    var revR = rs.filter(function (r) { return r.phase !== "make"; });
    var labelled = S.make || (makeR.length > 0 && revR.length > 0);
    var rates = el("div", "fb-rates");
    function chips(group, phaseWord) {
      if (!group.length) { return; }
      if (labelled) {
        var pl = el("span", "fb-phase", phaseWord);
        pl.setAttribute("data-fb-phase-label", phaseWord);
        rates.appendChild(pl);
      }
      group.forEach(function (r) {
        var lab = RATING[r.rating] || r.rating;
        var chipEl = el("span", "fb-rate fb-rate-" + r.rating, lab);
        chipEl.setAttribute("data-rating", r.rating);
        chipEl.setAttribute("data-phase", r.phase || "");
        var when = r.at ? whenLong(r.at) : "";
        chipEl.title = lab + (labelled ? " · " + phaseWord : "") + (when ? " · " + when : "");
        rates.appendChild(chipEl);
      });
    }
    chips(makeR, "while writing");
    chips(revR, "in review");
    return rates;
  }

  /* ⊕ Design port A, 30 Sep 2026 — the row is now a hairline-split list
     item matching the MCQ breakdown's `.bd-q` (Design's NOTES.md: "Rows
     are split by hairlines, not cards with borders"), with a plain
     zero-padded number (`.fb-qn`) as its own 34px column — not "Q1"
     inside the head. `.fb-card-body` is a new wrapper (no class hook any
     drive reads — confirmed no drive queries `.fb-card-head`/`.fb-pair`
     structurally) so the number column and the rest can sit in a
     `34px minmax(0,1fr)` grid, the same shape `.bd-q` uses. Every id,
     data attribute and class the drives DO read (`data-card`, `.fb-card`, `.fb-state`,
     `.fb-ans`/`data-fb="answer"`, `.fb-ans-text`/`data-fb-data="mine"`,
     `.fb-verdict`, `.fb-model`/`.fb-model-text`/`.fb-model-label`,
     `.fb-tries`, `.fb-history`) is unchanged. */
  function buildCard(c, i) {
    var li = el("li", "fb-card");
    li.setAttribute("data-card", c.id);
    var n = i + 1;
    li.appendChild(el("span", "fb-qn", (n < 10 ? "0" : "") + n));

    var col = el("div", "fb-card-body");

    var head = el("div", "fb-card-head");
    var q = sci("div", "fb-q", c.question);
    q.setAttribute("data-fb-data", "question");
    head.appendChild(q);
    var st = cardState(c);
    var chip = el("span", "fb-state fb-state-" + st.key, st.word);
    chip.setAttribute("data-state", st.key);
    head.appendChild(chip);
    col.appendChild(head);

    var pair = el("div", "fb-pair");
    var ab = answerBox(c);
    if (ab.kind !== "omit") {
      var ans = ab.ans;
      var box = el("div", "fb-ans" + (ans ? "" : " is-none"));
      box.setAttribute("data-fb", "answer");
      /* ⊕ Design port A — a header row, matching the model box's own
         (Design's `.fc-box-h`): "Latest answer" beside the verdict, so
         the two boxes read as a symmetric pair. */
      var ansHead = el("div", "fb-box-h");
      ansHead.appendChild(el("span", "fb-model-label", "Latest answer"));
      if (ans && ans.check) {
        var v = el("span", "fb-verdict fb-verdict-" + ans.check, VERDICT[ans.check] || ans.check);
        v.setAttribute("data-check", ans.check);
        ansHead.appendChild(v);
      }
      box.appendChild(ansHead);
      var t = sci("div", "fb-ans-text", ans ? ans.text : "No written answer");
      if (ans) { t.setAttribute("data-fb-data", "mine"); }
      box.appendChild(t);
      pair.appendChild(box);
    }

    var model = el("div", "fb-model");
    var modelHead = el("div", "fb-box-h");
    modelHead.appendChild(el("span", "fb-model-label", "Model answer"));
    model.appendChild(modelHead);
    var mt = sci("div", "fb-model-text", c.answer);
    mt.setAttribute("data-fb-data", "answer");
    model.appendChild(mt);
    pair.appendChild(model);
    col.appendChild(pair);

    var foot = el("div", "fb-foot");
    foot.appendChild(el("span", "fb-tries", "Tries: " + tries(c)));
    var rates = ratingChips(c);
    if (rates.firstChild) {
      var det = el("details", "fb-history");
      det.appendChild(el("summary", null, "History"));
      det.appendChild(rates);
      foot.appendChild(det);
    }
    col.appendChild(foot);

    li.appendChild(col);
    return li;
  }

  function buildSittings(ses) {
    var det = el("details", "fb-history fb-sittings");
    det.setAttribute("data-fb", "sittings");
    det.appendChild(el("summary", null, "History"));
    var ol = el("ol", "fb-sessions");
    ses.forEach(function (s) {
      var li = el("li", "fb-session");
      li.appendChild(el("span", "fb-ses-when", whenLong(s.started_at)));
      li.appendChild(el("span", "fb-ses-len", clock(s.active_ms)));
      li.appendChild(el("span", "fb-ses-n", (s.cards_rated || 0) + " rated"));
      if (s.rushed) { li.appendChild(el("span", "fb-rushed", "Rushed")); }
      if (s.open) { li.appendChild(el("span", "fb-ses-open", "Open")); }
      ol.appendChild(li);
    });
    det.appendChild(ol);
    return det;
  }

  function renderBody() {
    if (!S) { return; }
    var p = S.roster[S.idx];
    var d = S.detail[p.pupil_id];
    els.body.textContent = "";
    if (d === undefined) {
      els.body.appendChild(buildTiles(p, null));
      els.body.appendChild(el("div", "bd-empty", "Loading…"));
      return;
    }
    if (d === null) {
      els.body.appendChild(buildTiles(p, null));
      els.body.appendChild(el("div", "bd-empty", "Couldn't load this pupil. Try again in a moment."));
      return;
    }
    els.body.appendChild(buildTiles(p, d));
    if (S.make) {
      var words = verdictLine(p.answers);
      if (words) {
        var vl = el("div", "fb-verdicts", words);
        vl.setAttribute("data-fb", "verdicts");
        els.body.appendChild(vl);
      }
    }
    var cards = d.cards || [];
    var ses = d.sessions || [];
    var started = ses.length > 0 || cards.some(function (c) { return (c.ratings || []).length || c.mine; });
    if (!started && (p.status === "not_started" || p.status === "missing" || !p.status)) {
      els.body.appendChild(el("div", "bd-empty", p.status === "missing"
        ? nameOf(p) + " didn't do this set."
        : nameOf(p) + " hasn't started this set yet."));
      var det = el("details", "bd-disclosure");
      det.appendChild(el("summary", null, "Show the cards"));
      var list0 = el("ol", "fb-cards");
      cards.forEach(function (c, i) { list0.appendChild(buildCard(c, i)); });
      det.appendChild(list0);
      els.body.appendChild(det);
      return;
    }
    var bar = el("div", "bd-qmap-wrap fb-filter");
    bar.appendChild(buildToggle(cards));
    els.body.appendChild(bar);
    var shown = S.notSecured ? cards.filter(function (c) { return !c.secured; }) : cards;
    var list = el("ol", "fb-cards");
    shown.forEach(function (c) { list.appendChild(buildCard(c, cards.indexOf(c))); });
    els.body.appendChild(list);
    if (ses.length) { els.body.appendChild(buildSittings(ses)); }
  }

  function render() { renderHeader(); renderBody(); }

  /* One read per pupil per open; neighbours fetched ahead so prev/next is
     instant. A failed read is cached as null and retried on the next open. */
  function loadDetail(pid, mySession) {
    if (!S || S.pending[pid] || S.detail[pid] !== undefined) { return S && S.pending[pid]; }
    var sb = S.sb;
    S.pending[pid] = Promise.resolve()
      .then(function () { return sb.rpc("flashcard_pupil_detail", { p_assignment: S.id, p_pupil: pid }); })
      .then(function (r) { return (r && !r.error && r.data) ? r.data : null; },
            function () { return null; })
      .then(function (data) {
        if (mySession !== session || !S) { return; }
        S.detail[pid] = data;
        delete S.pending[pid];
        if (S.roster[S.idx] && S.roster[S.idx].pupil_id === pid) { renderBody(); }
      });
    return S.pending[pid];
  }

  function loadAround(mySession) {
    var ids = [S.idx, S.idx + 1, S.idx - 1];
    ids.forEach(function (i) {
      if (i >= 0 && i < S.roster.length) { loadDetail(S.roster[i].pupil_id, mySession); }
    });
  }

  function go(delta) {
    if (!S) { return; }
    var n = S.idx + delta;
    if (n < 0 || n >= S.roster.length) { return; }
    S.idx = n;
    render();
    els.live.textContent = nameOf(S.roster[S.idx]);
    els.sheet.scrollTop = 0;
    loadAround(session);
  }

  function renderError(msg) {
    els.title.textContent = "Flashcards";
    els.chip.textContent = "";
    els.prev.disabled = true; els.next.disabled = true;
    els.body.textContent = "";
    els.body.appendChild(el("div", "bd-empty", msg));
  }

  async function open(opts) {
    var o = opts || {};
    buildShell();
    opener = (document.activeElement && document.activeElement !== document.body) ? document.activeElement : null;
    session += 1;
    var mySession = session;
    els.overlay.hidden = false;
    opens += 1;
    els.overlay.setAttribute("data-fb-opens", String(opens));
    els.sheet.focus({ preventScroll: true });
    if (prevOverflow == null) {
      prevOverflow = document.documentElement.style.overflow || "";
      document.documentElement.style.overflow = "hidden";
    }
    S = null;
    els.eyebrow.textContent = "";
    els.title.textContent = "Loading…";
    els.chip.textContent = "";
    els.prev.disabled = true; els.next.disabled = true;
    els.body.textContent = "";
    els.body.appendChild(el("div", "bd-empty", "Loading…"));

    var sb = client();
    if (!sb || !o.assignmentId) { renderError("This page is not signed in. Reload and try again."); return; }
    try {
      var prog = o.progress || null, chem = o.chem;
      var reads = [];
      if (!prog) {
        reads.push(sb.rpc("flashcard_progress", { p_assignment: o.assignmentId, p_now: new Date().toISOString() })
          .then(function (r) { if (r.error) { throw new Error(r.error.message || "progress"); } prog = r.data; }));
      }
      if (chem == null) {
        reads.push(Promise.resolve(sb.from("assignments").select("subject:subjects(name)")
          .eq("id", o.assignmentId).maybeSingle())
          .then(function (r) {
            var nm = r && r.data && r.data.subject && r.data.subject.name;
            chem = String(nm || "").toLowerCase() === "chemistry";
          }, function () { chem = false; }));
      }
      await Promise.all(reads);
      if (mySession !== session) { return; }
      var pupils = (prog && prog.pupils) || [];
      var byId = {};
      pupils.forEach(function (p) { byId[p.pupil_id] = p; });
      var roster = pupils;
      if (o.order && o.order.length) {
        roster = o.order.map(function (id) { return byId[id]; }).filter(Boolean);
        pupils.forEach(function (p) { if (roster.indexOf(p) < 0) { roster.push(p); } });
      }
      var idx = -1;
      for (var i = 0; i < roster.length; i++) { if (roster[i].pupil_id === o.studentId) { idx = i; break; } }
      /* Never fall back to pupil 1 for a real id (breakdown.js MUST-1). */
      if (idx < 0) { renderError("This pupil isn't in this class now."); return; }
      var a = (prog && prog.assignment) || {};
      S = {
        sb: sb, id: o.assignmentId, classId: o.classId || a.class_id, title: a.title,
        make: a.mode === "make", n: prog.n || 0, chem: !!chem,
        roster: roster, idx: idx, detail: {}, pending: {}, notSecured: false
      };
      render();
      els.live.textContent = nameOf(roster[idx]);
      loadAround(mySession);
    } catch (err) {
      if (mySession !== session) { return; }
      console.error("[flashcard-breakdown]", err);
      renderError("Couldn't load this set. Try again in a moment.");
    }
  }

  window.MRBFlashcardBreakdown = {
    open: open, close: close, isOpen: isOpen,
    // pure, for the drive
    verdictLine: verdictLine, cardState: cardState, latestAnswer: latestAnswer,
    answerBox: answerBox,
    tries: tries, whenLong: whenLong, STATUS: STATUS, VERDICT: VERDICT
  };
})();
