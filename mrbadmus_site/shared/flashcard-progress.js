/* ═══════════════════════════════════════════════════════════════════════
   flashcard-progress.js — MRB-351 §5, the teacher's view of one flashcard
   set: teacher/flashcards.html?assignment=<id>.

   Reads (all through the signed-in teacher's own client, RLS/definer-gated):
     rpc flashcard_progress      {p_assignment, p_now}   the table + strip
     rpc flashcard_pupil_detail  {p_assignment, p_pupil} the drawer
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
  var MODE = { make: "Pupils write the answers", review: "Ready-made cards" };
  var RULE = { secure: "Secure", quick: "Quick" };
  var RATING = { got_it: "Got it", nearly: "Nearly", not_yet: "Not yet" };
  var CHECK = { match: "Match", partial: "Partial", no: "No match",
                blank: "Blank", pending: "Checking" };
  var SAY = {
    notFound: "Flashcard set not found",
    failed: "Couldn't load this set",
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
  var COLUMNS = [
    { key: "pupil",    label: "Pupil" },
    { key: "status",   label: "Status" },
    { key: "made",     label: "Made",     make: true },
    { key: "secured",  label: "Secured" },
    { key: "sittings", label: "Sittings" },
    { key: "time",     label: "Time" },
    { key: "percard",  label: "Per card" },
    { key: "rushed",   label: "Rushed" },
    { key: "answers",  label: "Answers",  make: true },
    { key: "last",     label: "Last active" }
  ];

  function columnsFor(mode) {
    return COLUMNS.filter(function (c) { return !c.make || mode === "make"; });
  }

  function rank(p) { return (STATUS[p.status] || STATUS.not_started).rank; }

  function sortValue(p, key) {
    switch (key) {
      case "pupil": return ((p.last_name || "") + " " + (p.first_name || "") + " " + (p.display_name || "")).toLowerCase();
      case "status": return rank(p) * 100000 + (p.secured || 0);
      case "made": return p.made == null ? null : p.made;
      case "secured": return p.secured == null ? null : p.secured * 1000 + (p.known || 0);
      case "sittings": return p.sittings == null ? null : p.sittings;
      case "time": return p.active_ms == null ? null : p.active_ms;
      case "percard": return p.median_think_ms == null ? null : p.median_think_ms;
      case "rushed": return p.rushed ? 1 : 0;
      case "answers": {
        var a = p.answers || {};
        return (a.match || 0) * 1000 + (a.partial || 0);
      }
      case "last": return p.last_active ? Date.parse(p.last_active) : null;
    }
    return null;
  }

  function defaultCompare(a, b) {
    var r = rank(a) - rank(b);
    if (r) { return r; }
    var s = (a.secured || 0) - (b.secured || 0);
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

  function answersText(a) {
    a = a || {};
    var bits = [];
    if (a.match) { bits.push(a.match + " match"); }
    if (a.partial) { bits.push(a.partial + " partial"); }
    if (a.no) { bits.push(a.no + " no"); }
    if (a.blank) { bits.push(a.blank + " blank"); }
    if (a.pending) { bits.push(a.pending + " pending"); }
    return bits.join("; ");
  }

  function cellText(p, key, n, mode, rule, nowMs) {
    switch (key) {
      case "pupil": return nameOf(p);
      case "status": return (STATUS[p.status] || STATUS.not_started).label;
      case "made": return (p.made || 0) + "/" + n;
      case "secured": return (p.secured || 0) + "/" + n;
      case "sittings": return String(p.sittings || 0);
      case "time": return p.active_ms ? clock(p.active_ms) : "—";
      case "percard": return seconds(p.median_think_ms);
      case "rushed": return p.rushed ? "Rushed" : "";
      case "answers": return answersText(p.answers);
      case "last": return relative(p.last_active, nowMs);
    }
    return "";
  }

  function csvEscape(v) {
    var s = v == null ? "" : String(v);
    return /[",\r\n]/.test(s) ? '"' + s.replace(/"/g, '""') + '"' : s;
  }

  /* The table as displayed, in the order displayed. `Last active` is the
     London clock rather than "3 min ago", which means nothing in a file. */
  function buildCsv(data, rows) {
    var a = data.assignment || {}, n = data.n || 0;
    var cols = columnsFor(a.mode);
    var head = [];
    cols.forEach(function (c) {
      head.push(c.label);
      if (c.key === "secured" && a.rule === "secure") { head.push("Known once"); }
    });
    var lines = [head.map(csvEscape).join(",")];
    rows.forEach(function (p) {
      var out = [];
      cols.forEach(function (c) {
        if (c.key === "last") { out.push(p.last_active ? londonYmd(p.last_active) : ""); }
        else if (c.key === "percard") {
          out.push(p.median_think_ms == null ? "" : (Math.round(p.median_think_ms / 100) / 10).toFixed(1));
        } else if (c.key === "time") { out.push(p.active_ms ? clock(p.active_ms) : ""); }
        else if (c.key === "rushed") { out.push(p.rushed ? "Yes" : ""); }
        else { out.push(cellText(p, c.key, n, a.mode, a.rule)); }
        if (c.key === "secured" && a.rule === "secure") { out.push((p.known || 0) + "/" + n); }
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
  function sci(tag, cls, text) {
    var e = h(tag, cls);
    if (window.MRBFormulae && window.MRBFormulae.fill) { window.MRBFormulae.fill(e, text || ""); }
    else { e.textContent = text || ""; }
    return e;
  }
  function $(id) { return document.getElementById(id); }
  function clear(e) { while (e && e.firstChild) { e.removeChild(e.firstChild); } return e; }

  /* ── state ────────────────────────────────────────────────────────────── */
  var S = {
    id: null, sb: null, data: null, sortKey: null, sortDir: "asc",
    timer: null, inflight: false, detailFor: null, lastFocus: null
  };

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
  function chip(text, tone) {
    var c = h("span", "fp-chip" + (tone ? " fp-chip-" + tone : ""), text);
    return c;
  }

  function renderHead(d) {
    var a = d.assignment || {};
    var st = assignmentState(a, d.now || nowIso());
    var host = clear($("fp-head"));

    var crumb = h("div", "fp-eyebrow");
    var cls = h("a", "fp-crumb", a.class_name || "");
    var env = (window.MrBadmusConfig && window.MrBadmusConfig.environment === "test") ? "&env=test" : "";
    cls.href = "/teacher/class-detail.html?class=" + encodeURIComponent(a.class_id || "") + env;
    crumb.appendChild(cls);
    crumb.appendChild(h("span", "fp-sep", "·"));
    crumb.appendChild(h("span", null, "Flashcards"));

    var title = h("h1", "fp-title", a.title || "");
    var meta = h("div", "fp-meta");
    meta.appendChild(h("span", "fp-due", "Due " + londonWhen(a.due_at)));
    if (st === "scheduled") {
      meta.appendChild(h("span", "fp-sep", "·"));
      meta.appendChild(h("span", "fp-rel", "Opens " + londonWhen(a.release_at)));
    }
    var chips = h("div", "fp-chips");
    var stLabel = st === "scheduled" ? "Scheduled" : (st === "open" ? "Open" : "Closed");
    chips.appendChild(chip(stLabel, "state-" + st));
    chips.appendChild(chip(MODE[a.mode] || a.mode || ""));
    chips.appendChild(chip(RULE[a.rule] || a.rule || ""));
    chips.appendChild(chip(d.n + (d.n === 1 ? " card" : " cards")));

    var left = h("div", "fp-head-main");
    left.appendChild(crumb); left.appendChild(title); left.appendChild(meta); left.appendChild(chips);
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
    document.title = (a.title || "Flashcards") + " — Mr Badmus AI";
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
    tiles.appendChild(tile("Done", (c.done || 0) + "/" + (c.pupils || 0),
                           c.completion_pct == null ? "—" : c.completion_pct + "%", "fp-done"));
    tiles.appendChild(tile("Average sittings",
                           c.avg_sittings == null ? "—" : String(c.avg_sittings), null, "fp-avg"));
    host.appendChild(tiles);

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

  function securedCell(p, n, rule) {
    var w = h("div", "fp-sec");
    w.appendChild(h("span", "fp-sec-n", (p.secured || 0) + "/" + n));
    var bar = h("span", "fp-bar");
    bar.setAttribute("aria-hidden", "true");
    if (rule === "secure" && n) {
      var k = h("span", "fp-bar-known");
      k.style.width = Math.min(100, Math.round(((p.known || 0) / n) * 100)) + "%";
      bar.appendChild(k);
    }
    var s = h("span", "fp-bar-sec");
    s.style.width = n ? Math.min(100, Math.round(((p.secured || 0) / n) * 100)) + "%" : "0%";
    bar.appendChild(s);
    w.appendChild(bar);
    if (rule === "secure") {
      w.title = (p.known || 0) + " known once";
      w.setAttribute("data-known", String(p.known || 0));
    }
    return w;
  }

  function answersCell(a) {
    a = a || {};
    var w = h("div", "fp-ans");
    [["match", "✓", "match"], ["partial", "≈", "partial"], ["no", "✗", "no"],
     ["blank", "○", "blank"]].forEach(function (x) {
      if (!a[x[0]]) { return; }
      var s = h("span", "fp-ans-" + x[0], x[1] + a[x[0]]);
      s.setAttribute("aria-label", a[x[0]] + " " + x[2]);
      s.title = a[x[0]] + " " + x[2];
      w.appendChild(s);
    });
    if (a.pending) {
      var p = h("span", "fp-ans-pending", "…" + a.pending);
      p.setAttribute("aria-label", a.pending + " pending");
      p.title = a.pending + " pending";
      w.appendChild(p);
    }
    if (!w.firstChild) { w.appendChild(h("span", "fp-ghost", "—")); }
    return w;
  }

  function renderTable(d) {
    var a = d.assignment || {}, n = d.n || 0;
    var cols = columnsFor(a.mode);
    var table = $("fp-table");
    table.classList.toggle("fp-review", a.mode !== "make");
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
      cols.forEach(function (c) {
        var td = h(c.key === "pupil" ? "th" : "td", "fp-td fp-col-" + c.key);
        if (c.key === "pupil") {
          td.scope = "row";
          var b = h("button", "fp-name", nameOf(p));
          b.type = "button";
          b.addEventListener("click", function (e) { e.stopPropagation(); openDrawer(p); });
          td.appendChild(b);
        } else if (c.key === "status") {
          td.appendChild(statusChip(p.status));
        } else if (c.key === "secured") {
          td.appendChild(securedCell(p, n, a.rule));
        } else if (c.key === "answers") {
          td.appendChild(answersCell(p.answers));
        } else if (c.key === "rushed") {
          if (p.rushed) { td.appendChild(h("span", "fp-rushed", "Rushed")); }
        } else {
          td.textContent = cellText(p, c.key, n, a.mode, a.rule, nowMs);
          if (c.key === "last" && p.last_active) { td.title = londonWhen(p.last_active); }
        }
        row.appendChild(td);
      });
      row.addEventListener("click", function () { openDrawer(p); });
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
    if (!S.id || !S.sb) { return; }
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
    var text = buildCsv(S.data, rows);
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

  /* ── the drawer ───────────────────────────────────────────────────────── */
  function closeDrawer() {
    var back = $("fp-drawer-back");
    back.hidden = true;
    document.body.classList.remove("fp-locked");
    S.detailFor = null;
    if (S.lastFocus && S.lastFocus.focus) { try { S.lastFocus.focus(); } catch (e) {} }
  }

  async function openDrawer(p) {
    S.lastFocus = document.activeElement;
    S.detailFor = p.pupil_id;
    var back = $("fp-drawer-back");
    back.hidden = false;
    document.body.classList.add("fp-locked");
    $("fp-drawer-name").textContent = nameOf(p);
    var st = clear($("fp-drawer-status"));
    st.appendChild(statusChip(p.status));
    var body = clear($("fp-drawer-body"));
    body.appendChild(h("div", "fp-skel-line"));
    $("fp-drawer-close").focus();
    var r;
    try {
      r = await S.sb.rpc("flashcard_pupil_detail", { p_assignment: S.id, p_pupil: p.pupil_id });
    } catch (e) { r = { error: e }; }
    if (S.detailFor !== p.pupil_id) { return; }
    clear(body);
    if (!r || r.error || !r.data) { body.appendChild(h("div", "fp-empty", SAY.detailFailed)); return; }
    renderDetail(body, r.data, (S.data && S.data.assignment) || {});
  }

  function renderDetail(body, d, a) {
    var make = a.mode === "make";
    body.appendChild(h("div", "fp-dr-label", "Cards"));
    var list = h("ol", "fp-cards");
    (d.cards || []).forEach(function (c, i) {
      var li = h("li", "fp-card");
      li.setAttribute("data-card", c.id);
      var top = h("div", "fp-card-top");
      top.appendChild(h("span", "fp-card-n", "Q" + ((c.position != null ? c.position : i) + 1)));
      if (c.secured) {
        var t = h("span", "fp-secured", "✓ Secured");
        top.appendChild(t);
      }
      li.appendChild(top);
      var q = sci("div", "fp-card-q", c.question);
      q.setAttribute("data-fp-data", "question");
      li.appendChild(q);

      var pair = h("div", "fp-pair" + (make ? "" : " fp-pair-one"));
      if (make) {
        var mine = h("div", "fp-side fp-mine");
        mine.appendChild(h("div", "fp-side-label", "Their answer"));
        var mt = c.mine ? sci("div", "fp-side-text", c.mine) : h("div", "fp-side-text fp-ghost", "—");
        mt.setAttribute("data-fp-data", "mine");
        mine.appendChild(mt);
        var foot = h("div", "fp-side-foot");
        if (c.check) {
          var ck = h("span", "fp-check fp-check-" + c.check, CHECK[c.check] || c.check);
          ck.setAttribute("data-check", c.check);
          foot.appendChild(ck);
        }
        if (c.written_ms != null) { foot.appendChild(h("span", "fp-side-time", clock(c.written_ms))); }
        if (foot.firstChild) { mine.appendChild(foot); }
        pair.appendChild(mine);
      }
      var model = h("div", "fp-side fp-model");
      model.appendChild(h("div", "fp-side-label", make ? "Model answer" : "Answer"));
      var at = sci("div", "fp-side-text", c.answer);
      at.setAttribute("data-fp-data", "answer");
      model.appendChild(at);
      pair.appendChild(model);
      li.appendChild(pair);

      var rates = h("div", "fp-rates");
      (c.ratings || []).forEach(function (r) {
        var lab = RATING[r.rating] || r.rating;
        var chipEl = h("span", "fp-rate fp-rate-" + r.rating + (r.phase === "make" ? " fp-rate-make" : ""), lab);
        chipEl.setAttribute("data-rating", r.rating);
        chipEl.setAttribute("data-phase", r.phase || "");
        chipEl.title = (r.phase === "make" ? "Make · " : "") + lab + (r.at ? " · " + londonWhen(r.at) : "");
        if (r.phase === "make") { chipEl.setAttribute("aria-label", lab + ", make"); }
        rates.appendChild(chipEl);
      });
      if (rates.firstChild) { li.appendChild(rates); }
      list.appendChild(li);
    });
    body.appendChild(list);

    body.appendChild(h("div", "fp-dr-label", "Sittings"));
    var ses = d.sessions || [];
    if (!ses.length) {
      body.appendChild(h("div", "fp-empty", "None yet"));
    } else {
      var sl = h("ol", "fp-sessions");
      ses.forEach(function (s) {
        var li = h("li", "fp-session");
        li.appendChild(h("span", "fp-ses-when", londonWhen(s.started_at)));
        li.appendChild(h("span", "fp-ses-len", clock(s.active_ms)));
        li.appendChild(h("span", "fp-ses-n", (s.cards_rated || 0) + " rated"));
        if (s.rushed) { li.appendChild(h("span", "fp-rushed", "Rushed")); }
        if (s.open) { li.appendChild(h("span", "fp-ses-open", "Open")); }
        sl.appendChild(li);
      });
      body.appendChild(sl);
    }
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
      (/not_found|not_yours|42501|invalid input syntax/i.test(code)) ? SAY.notFound : SAY.failed;
    stopPolling();
  }

  /* ── boot ─────────────────────────────────────────────────────────────── */
  function wire() {
    $("fp-drawer-close").addEventListener("click", closeDrawer);
    $("fp-drawer-back").addEventListener("click", function (e) {
      if (e.target === $("fp-drawer-back")) { closeDrawer(); }
    });
    $("fp-ed-cancel").addEventListener("click", closeEdit);
    $("fp-ed-save").addEventListener("click", saveEdit);
    $("fp-edit-back").addEventListener("click", function (e) {
      if (e.target === $("fp-edit-back")) { closeEdit(); }
    });
    document.addEventListener("keydown", function (e) {
      if (e.key !== "Escape") { return; }
      if (!$("fp-edit-back").hidden) { closeEdit(); }
      else if (!$("fp-drawer-back").hidden) { closeDrawer(); }
    });
  }

  async function start() {
    wire();
    var q = new URLSearchParams(window.location.search);
    S.id = q.get("assignment");
    var guard = window.MrBadmusTeacherGuard;
    S.sb = guard && guard.getClient ? guard.getClient() : null;
    if (!S.id || !S.sb) { fail({ code: "not_found" }); return; }
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
