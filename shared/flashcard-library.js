/* ═══════════════════════════════════════════════════════════════════════
   shared/flashcard-library.js — "Your flashcards": every flashcard set a
   pupil has been all the way through, to flip and revise from.
   MRB-352 Stage D2 (docs/mrb351/STAGE-D-PLAN.md §3). Hand-written.

   WHAT A SET IS. One flashcard homework (`assignments`, quiz_type
   'flashcards') the pupil can read, with its frozen deck
   (`assignment_flashcards`), the pupil's own words per card, and the
   pupil's own name for it. A set is in the library once the pupil has
   rated every card at least once (decision 10). `student-live.js` works
   that out after the class page has painted and hands the ids to
   `offer()`; nothing here decides it.

   ⚠️ POOL OWNERSHIP (CLAUDE.md, MRB-288). The library serves the homework
   deck's own content and nothing else: `serveDeck()` below is the ONE read
   of `assignment_flashcards` question/answer on the whole site outside the
   homework's own RPC, and `pool_ownership.py` fails the build on a second.
   It never names the practice-card pool, the ladder mirror or either
   assignment bank.

   NO WRITES BUT A NAME (decision 12). Flipping a card is not evidence of
   recall: nothing here writes a rating, an event or a submission. The only
   write is the pupil's own name for a set, into `flashcard_set_names`
   (pupil-owned, RLS). Until that table exists (a parked migration), the
   name is kept on this device and nothing on screen says so (decision 15).

   OUTSIDE THE RUNTIME. The overlay is appended to <body>, a sibling of the
   `#mrb-student` mount the runtime empties on every redraw (the
   `set-work.js` pattern). It is built once and patched in place: flipping
   toggles an attribute, moving swaps two text nodes.

   ADDRESSES. `#sets` is the list, `#set=<assignment id>` one set, so a
   direct link works and Back steps out (set → list → the class page).
   ═══════════════════════════════════════════════════════════════════════ */
(function (root) {
  "use strict";
  var doc = root.document;
  var NAMES_KEY = "mrbadmusai.fcset.v1.names";
  var UUID = /^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$/i;
  var MISSING_TABLE = { "42P01": 1, "PGRST205": 1 };

  var S = {
    sb: null, uid: null, counts: {},
    sets: null,          // [{id, title, className, classId, subject, n}] newest first
    setsLoading: null,   // the in-flight load, so two opens share one read
    names: {},           // server names {assignment_id: name}
    deviceMode: false,   // the names table is not there: names live on this device
    decks: {},           // {id: [{id, position, question, answer, mine}]} — this page's reads
    screen: null,        // "sets" | "set" | null (closed)
    set: null,           // the open set's id
    order: [], pos: 0, flipped: false, shuffled: false,
    renaming: false, hooked: false, returnTo: null
  };
  var els = null;

  function ready() {
    var r = root.__MRB_LIBRARY_READY__;
    return Array.isArray(r) ? r.filter(function (x) { return UUID.test(String(x)); }) : [];
  }

  /* ── the device's copy of names (degrade mode, and a failed write) ── */
  function deviceNames() {
    try { var v = JSON.parse(root.localStorage.getItem(NAMES_KEY) || "{}"); return (v && typeof v === "object") ? v : {}; }
    catch (e) { return {}; }
  }
  function saveDeviceNames(m) {
    try {
      if (Object.keys(m).length) { root.localStorage.setItem(NAMES_KEY, JSON.stringify(m)); }
      else { root.localStorage.removeItem(NAMES_KEY); }
    } catch (e) { /* private mode: the name lasts this page */ }
  }
  function nameOf(set) {
    var dev = deviceNames();
    return S.names[set.id] || dev[set.id] || set.title;
  }

  /* ── the stylesheet, stamped like every other shared asset ────────── */
  function stamped(src) {
    var map = root.__MRB_ASSET_V__, v = map && map[src.replace(/^\/shared\//, "")];
    return v ? src + "?v=" + v : src;
  }
  function loadCss() {
    if (!doc || doc.querySelector("link[data-mrb-library-css]")) { return; }
    var l = doc.createElement("link");
    l.rel = "stylesheet";
    l.href = stamped("/shared/flashcard-library.css");
    l.setAttribute("data-mrb-library-css", "1");
    doc.head.appendChild(l);
  }

  /* ═════════════════════════════════════════════════════════════════════
     THE BUTTON ON THE CLASS PAGE — under the FLASHCARDS card, only when a
     set qualifies. An after-draw hook, because the runtime rebuilds the
     page on every state change and anything inserted once is gone 12ms
     later (the `drawReminder` precedent, student-live.js).
     ═════════════════════════════════════════════════════════════════════ */
  function place(host) {
    var scope = host || doc;
    var surface = scope.querySelector('[data-bench-surface="cards"]');
    if (!surface) { return; }
    var btn = surface.querySelector("[data-mrb-library-open]");
    if (!ready().length) { if (btn) { btn.parentNode.removeChild(btn); } return; }
    if (btn) { return; }
    btn = doc.createElement("button");
    btn.type = "button";
    btn.setAttribute("data-mrb-library-open", "");
    btn.setAttribute("data-port-action", "flashcard-library");
    btn.setAttribute("style", "position:relative;margin-top:10px;width:100%;min-height:48px;"
      + "border-radius:14px;border:1.5px solid var(--st-rule);background:var(--st-paper);"
      + "color:var(--st-body);font:600 15px var(--st-ui);text-align:center;cursor:pointer;");
    btn.textContent = "View your flashcards";
    btn.addEventListener("click", function () { go("#sets", 1); });
    surface.appendChild(btn);
  }

  /* ═════════════════════════════════════════════════════════════════════
     READS — all as the pupil, under RLS. No service role, no backend.
     ═════════════════════════════════════════════════════════════════════ */
  function probeNames() {
    return Promise.resolve(S.sb.from("flashcard_set_names").select("assignment_id, name"))
      .then(function (r) {
        if (r.error) {
          if (MISSING_TABLE[r.error.code]) { S.deviceMode = true; }
          return;
        }
        S.deviceMode = false;
        var m = {};
        (r.data || []).forEach(function (row) { m[row.assignment_id] = row.name; });
        S.names = m;
        /* The table has arrived since this device kept names: write each one
           the server does not have up once, then forget the local copy. */
        var dev = deviceNames(), up = Object.keys(dev).filter(function (id) { return !m[id]; });
        if (!Object.keys(dev).length) { return; }
        return Promise.all(up.map(function (id) {
          return writeName(id, dev[id]).then(function (ok) { if (ok) { S.names[id] = dev[id]; } return ok; });
        })).then(function (oks) {
          if (oks.every(Boolean)) { saveDeviceNames({}); }
        });
      })
      .catch(function () { /* names are a nicety: the teacher's titles stand */ });
  }

  function loadSets() {
    if (S.setsLoading) { return S.setsLoading; }
    var ids = ready();
    S.setsLoading = Promise.all([
      Promise.resolve(S.sb.from("assignments")
        .select("id, title, class_id, subject_id, created_at, release_at, subject:subject_id(name), class:class_id(name)")
        .in("id", ids).eq("quiz_type", "flashcards").is("deleted_at", null)
        .order("created_at", { ascending: false })),
      probeNames()
    ]).then(function (res) {
      var r = res[0];
      if (r.error) { throw r.error; }
      S.sets = (r.data || []).map(function (a) {
        return {
          id: String(a.id).toLowerCase(), title: a.title || "Flashcards",
          classId: a.class_id, className: (a["class"] && a["class"].name) || "",
          subject: String((a.subject && a.subject.name) || "").toLowerCase(),
          n: S.counts[a.id] || S.counts[String(a.id).toLowerCase()] || 0,
          at: Date.parse(a.created_at || a.release_at || 0) || 0
        };
      }).sort(function (x, y) { return y.at - x.at; });
      return S.sets;
    }).catch(function (e) {
      S.setsLoading = null;
      throw e;
    });
    return S.setsLoading;
  }

  /* THE ONE SERVING READ of the homework deck's content (pool_ownership). */
  function serveDeck(id) {
    return S.sb.from("assignment_flashcards").select("id, position, question, answer")
      .eq("assignment_id", id).order("position", { ascending: true });
  }

  var deckLoading = {};
  function loadDeck(id) {
    if (S.decks[id]) { return Promise.resolve(S.decks[id]); }
    if (deckLoading[id]) { return deckLoading[id]; }
    deckLoading[id] = Promise.all([
      Promise.resolve(serveDeck(id)),
      /* the pupil's own words: make mode's first answer wins; otherwise the
         latest answer they wrote in review. Both are their own rows. */
      Promise.resolve(S.sb.from("flashcard_pupil_cards").select("card_id, pupil_answer")
        .eq("assignment_id", id)).catch(function () { return { data: [] }; }),
      Promise.resolve(S.sb.from("flashcard_reviews").select("card_id, answer, rated_at")
        .eq("assignment_id", id).not("answer", "is", null)
        .order("rated_at", { ascending: false })).catch(function () { return { data: [] }; })
    ]).then(function (res) {
      if (res[0].error) { throw res[0].error; }
      var mine = {};
      ((res[2] && !res[2].error && res[2].data) || []).forEach(function (row) {
        var t = String(row.answer || "").trim();
        if (t && !(row.card_id in mine)) { mine[row.card_id] = t; }
      });
      ((res[1] && !res[1].error && res[1].data) || []).forEach(function (row) {
        var t = String(row.pupil_answer || "").trim();
        if (t) { mine[row.card_id] = t; }
      });
      var deck = (res[0].data || []).map(function (c) {
        return { id: c.id, position: c.position, question: c.question || "", answer: c.answer || "",
                 mine: mine[c.id] || "" };
      });
      if (!deck.length) { throw new Error("empty deck"); }
      S.decks[id] = deck;
      delete deckLoading[id];
      return deck;
    }, function (err) { delete deckLoading[id]; throw err; });
    return deckLoading[id];
  }

  function writeName(id, name) {
    var sb = S.sb;
    var q = name
      ? sb.from("flashcard_set_names").upsert({ pupil_id: S.uid, assignment_id: id, name: name },
                                              { onConflict: "pupil_id,assignment_id" })
      : sb.from("flashcard_set_names").delete().eq("pupil_id", S.uid).eq("assignment_id", id);
    return Promise.resolve(q).then(function (r) {
      if (r && r.error) {
        if (MISSING_TABLE[r.error.code]) { S.deviceMode = true; }
        return false;
      }
      return true;
    }).catch(function () { return false; });
  }

  /* ═════════════════════════════════════════════════════════════════════
     THE OVERLAY — built once.
     ═════════════════════════════════════════════════════════════════════ */
  function h(tag, attrs, kids) {
    var e = doc.createElement(tag);
    Object.keys(attrs || {}).forEach(function (k) { e.setAttribute(k, attrs[k]); });
    (kids || []).forEach(function (k) { e.appendChild(typeof k === "string" ? doc.createTextNode(k) : k); });
    return e;
  }
  function svg(d) {
    var s = doc.createElementNS("http://www.w3.org/2000/svg", "svg");
    s.setAttribute("viewBox", "0 0 24 24"); s.setAttribute("width", "16"); s.setAttribute("height", "16");
    s.setAttribute("fill", "none"); s.setAttribute("stroke", "currentColor"); s.setAttribute("stroke-width", "2.4");
    s.setAttribute("stroke-linecap", "round"); s.setAttribute("stroke-linejoin", "round"); s.setAttribute("aria-hidden", "true");
    var p = doc.createElementNS("http://www.w3.org/2000/svg", "path"); p.setAttribute("d", d); s.appendChild(p);
    return s;
  }
  var CHEV_L = "M15 5l-7 7 7 7", CHEV_R = "M9 5l7 7-7 7", CROSS = "M6 6l12 12M18 6L6 18";

  function build() {
    if (els) { return els; }
    loadCss();
    var e = {};
    e.back = h("button", { type: "button", "data-lib": "back", "aria-label": "Back to your sets", "class": "mrbl-icon" }, [svg(CHEV_L)]);
    e.title = h("h2", { "data-lib": "title", "class": "mrbl-title" }, ["Your flashcards"]);
    e.name = h("button", { type: "button", "data-lib": "name", "aria-label": "Rename this set", "class": "mrbl-title mrbl-name" });
    e.input = h("input", { type: "text", "data-lib": "name-input", maxlength: "60", "class": "mrbl-title mrbl-input",
                           "aria-label": "Rename this set", autocomplete: "off", enterkeyhint: "done" });
    e.close = h("button", { type: "button", "data-lib": "close", "aria-label": "Close", "class": "mrbl-icon" }, [svg(CROSS)]);
    e.head = h("div", { "class": "mrbl-head" }, [e.back, e.title, e.name, e.input, e.close]);

    e.list = h("div", { "data-lib": "list", "class": "mrbl-list" });
    e.err = h("div", { "data-lib": "err", "class": "mrbl-err" }, [
      h("p", {}, ["Your flashcards did not load."]),
      (e.retry = h("button", { type: "button", "data-lib": "retry", "class": "mrbl-btn" }, ["Try again"]))
    ]);
    e.sets = h("div", { "data-lib-screen": "sets", "class": "mrbl-body" }, [e.list, e.err]);

    e.q = h("span", { "data-lib": "q", "class": "mrbl-q" });
    e.a = h("span", { "data-lib": "a", "class": "mrbl-a" });
    e.mineText = h("span", { "data-lib": "mine", "class": "mrbl-mine-text" });
    e.mine = h("span", { "data-lib": "mine-block", "class": "mrbl-mine" }, [
      h("span", { "class": "mrbl-eyebrow mrbl-muted" }, ["YOUR ANSWER"]), e.mineText]);
    e.front = h("span", { "class": "mrbl-face mrbl-front", "data-lib": "front" }, [
      h("span", { "class": "mrbl-eyebrow" }, ["QUESTION"]), e.q]);
    e.backFace = h("span", { "class": "mrbl-face mrbl-back", "data-lib": "back-face" }, [
      h("span", { "class": "mrbl-eyebrow" }, ["ANSWER"]), e.a, e.mine]);
    e.flipHint = h("span", { id: "mrbl-flip-hint", "class": "mrbl-sr" }, ["Flip the card"]);
    e.card = h("button", { type: "button", "data-lib": "card", "class": "mrbl-card", "data-flip": "0",
                           "aria-describedby": "mrbl-flip-hint" }, [e.front, e.backFace]);
    e.stage = h("div", { "class": "mrbl-stage" }, [e.card, e.flipHint]);
    e.prev = h("button", { type: "button", "data-lib": "prev", "aria-label": "Previous card", "class": "mrbl-icon mrbl-step" }, [svg(CHEV_L)]);
    e.pos = h("span", { "data-lib": "pos", "class": "mrbl-pos", "aria-live": "polite" });
    e.next = h("button", { type: "button", "data-lib": "next", "aria-label": "Next card", "class": "mrbl-icon mrbl-step" }, [svg(CHEV_R)]);
    e.shuffle = h("button", { type: "button", "data-lib": "shuffle", "aria-pressed": "false", "class": "mrbl-btn mrbl-shuffle" }, ["Shuffle"]);
    e.nav = h("div", { "class": "mrbl-nav" }, [e.prev, e.pos, e.next]);
    e.setErr = h("div", { "data-lib": "set-err", "class": "mrbl-err" }, [
      h("p", {}, ["Your flashcards did not load."]),
      (e.setRetry = h("button", { type: "button", "data-lib": "set-retry", "class": "mrbl-btn" }, ["Try again"]))
    ]);
    e.setBody = h("div", { "data-lib": "set-body", "class": "mrbl-setbody" }, [e.stage, e.nav, e.shuffle]);
    e.set = h("div", { "data-lib-screen": "set", "class": "mrbl-body" }, [e.setBody, e.setErr]);

    e.dlg = h("div", { "class": "mrbl-dlg", role: "dialog", "aria-modal": "true", "aria-label": "Your flashcards",
                       tabindex: "-1" }, [e.head, e.sets, e.set]);
    e.root = h("div", { "data-mrb-library": "", "class": "mrbl-scrim", hidden: "" }, [e.dlg]);
    doc.body.appendChild(e.root);
    els = e;
    wire();
    return e;
  }

  function show(el, on) { if (on) { el.removeAttribute("hidden"); } else { el.setAttribute("hidden", ""); } }

  /* ── screen 1: the sets ─────────────────────────────────────────── */
  function drawSets() {
    var e = els;
    show(e.back, false); show(e.title, true); show(e.name, false); show(e.input, false);
    show(e.sets, true); show(e.set, false); show(e.err, false);
    if (!S.sets) { e.list.textContent = ""; }
    loadSets().then(function () {
      if (S.screen !== "sets") { return; }
      var many = {}; S.sets.forEach(function (s) { many[s.classId] = 1; });
      var spans = Object.keys(many).length > 1;
      e.list.textContent = "";
      S.sets.forEach(function (s) {
        var meta = (s.n ? s.n + (s.n === 1 ? " CARD" : " CARDS") : "")
                 + (spans && s.className ? (s.n ? " · " : "") + s.className.toUpperCase() : "");
        var row = h("button", { type: "button", "class": "mrbl-row", "data-lib": "set-row", "data-set": s.id }, [
          h("span", { "class": "mrbl-row-name" }, [nameOf(s)]),
          h("span", { "class": "mrbl-row-meta" }, [meta]),
          svg(CHEV_R)
        ]);
        row.addEventListener("click", function () { go("#set=" + s.id, 1); });
        e.list.appendChild(row);
      });
      show(e.err, false);
    }).catch(function () {
      if (S.screen !== "sets") { return; }
      e.list.textContent = "";
      show(e.err, true);
    });
  }

  /* ── screen 2: one set ──────────────────────────────────────────── */
  function current() {
    var deck = S.decks[S.set];
    return deck ? deck[S.order[S.pos]] : null;
  }
  function chem() {
    var s = (S.sets || []).filter(function (x) { return x.id === S.set; })[0];
    return !!s && s.subject === "chemistry";
  }
  function fillText(el, text) {
    if (chem() && root.MRBFormulae && typeof root.MRBFormulae.fill === "function") {
      root.MRBFormulae.fill(el, text);
    } else {
      el.textContent = text;
    }
  }
  /* A long question steps down from Design's 29px to no lower than 18px
     before the face falls back to scrolling (student-live.js's fit loop). */
  function fit() {
    [[els.front, els.q, 29], [els.backFace, els.a, 21]].forEach(function (t) {
      var face = t[0], text = t[1], size = t[2];
      text.style.fontSize = "";
      var guard = 0;
      while (face.scrollHeight > face.clientHeight + 1 && size > 18 && guard++ < 12) {
        size -= 1.5;
        text.style.fontSize = size + "px";
      }
    });
  }
  function drawCard() {
    var e = els, deck = S.decks[S.set], c = current();
    if (!deck || !c) { return; }
    fillText(e.q, c.question);
    fillText(e.a, c.answer);
    e.mineText.textContent = c.mine;
    show(e.mine, !!c.mine);
    e.card.setAttribute("data-flip", S.flipped ? "1" : "0");
    e.front.setAttribute("aria-hidden", S.flipped ? "true" : "false");
    e.backFace.setAttribute("aria-hidden", S.flipped ? "false" : "true");
    e.pos.textContent = (S.pos + 1) + " / " + deck.length;
    e.shuffle.setAttribute("aria-pressed", S.shuffled ? "true" : "false");
    var one = deck.length < 2;
    e.prev.disabled = one; e.next.disabled = one; e.shuffle.disabled = one;
    fit();
  }
  function drawName() {
    var s = (S.sets || []).filter(function (x) { return x.id === S.set; })[0];
    els.name.textContent = s ? nameOf(s) : "";
  }
  function drawSet() {
    var e = els, id = S.set;
    show(e.back, true); show(e.title, false); show(e.name, !S.renaming); show(e.input, S.renaming);
    show(e.sets, false); show(e.set, true); show(e.setErr, false);
    show(e.setBody, !!S.decks[id]);
    Promise.all([loadSets(), loadDeck(id)]).then(function () {
      if (S.screen !== "set" || S.set !== id) { return; }
      if (!S.sets.some(function (s) { return s.id === id; })) { go("#sets", 0); return; }
      if (S.order.length !== S.decks[id].length) {
        S.order = S.decks[id].map(function (_, i) { return i; });
        S.pos = 0;
      }
      drawName();
      show(e.setBody, true);
      drawCard();
    }).catch(function () {
      if (S.screen !== "set" || S.set !== id) { return; }
      show(e.setBody, false);
      show(e.setErr, true);
    });
  }
  function openSet(id) {
    if (S.set !== id) {
      S.set = id; S.pos = 0; S.flipped = false; S.shuffled = false;
      S.order = [];
    }
    drawSet();
  }
  function step(d) {
    var deck = S.decks[S.set];
    if (!deck || deck.length < 2) { return; }
    S.pos = (S.pos + d + deck.length) % deck.length;
    S.flipped = false;
    drawCard();
  }
  function flip() { S.flipped = !S.flipped; drawCard(); }
  function toggleShuffle() {
    var deck = S.decks[S.set];
    if (!deck || deck.length < 2) { return; }
    var at = S.order[S.pos];
    S.shuffled = !S.shuffled;
    if (S.shuffled) {
      var o = deck.map(function (_, i) { return i; });
      /* a shuffle that lands on the same order is no shuffle at all */
      for (var tries = 0; tries < 8; tries++) {
        for (var i = o.length - 1; i > 0; i--) {
          var j = Math.floor(Math.random() * (i + 1)), t = o[i]; o[i] = o[j]; o[j] = t;
        }
        if (o.some(function (v, k) { return v !== k; })) { break; }
      }
      S.order = o; S.pos = 0;
    } else {
      S.order = deck.map(function (_, i) { return i; });
      S.pos = at;
    }
    S.flipped = false;
    drawCard();
  }

  /* ── rename in place ───────────────────────────────────────────── */
  function startRename() {
    var s = (S.sets || []).filter(function (x) { return x.id === S.set; })[0];
    if (!s) { return; }
    S.renaming = true;
    els.input.value = nameOf(s);
    show(els.name, false); show(els.input, true);
    els.input.focus({ preventScroll: true });
    els.input.select();
  }
  function endRename(save) {
    if (!S.renaming) { return; }
    S.renaming = false;
    var s = (S.sets || []).filter(function (x) { return x.id === S.set; })[0];
    show(els.input, false); show(els.name, true);
    if (!save || !s) { drawName(); return; }
    var v = els.input.value.replace(/\s+/g, " ").trim().slice(0, 60);
    /* blank, or the teacher's own title: the set goes back to the title */
    var name = (v && v !== s.title) ? v : "";
    if (name) { S.names[s.id] = name; } else { delete S.names[s.id]; }
    var dev = deviceNames();
    if (S.deviceMode) {
      if (name) { dev[s.id] = name; } else { delete dev[s.id]; }
      saveDeviceNames(dev);
      drawName();
      return;
    }
    if (dev[s.id]) { delete dev[s.id]; saveDeviceNames(dev); }
    drawName();
    writeName(s.id, name).then(function (ok) {
      if (ok) { return; }
      /* not saved on the server (no table yet, or offline): keep it here */
      var d = deviceNames();
      if (name) { d[s.id] = name; } else { delete d[s.id]; }
      saveDeviceNames(d);
    });
  }

  /* ═════════════════════════════════════════════════════════════════════
     OPEN / CLOSE / ADDRESSES
     ═════════════════════════════════════════════════════════════════════ */
  function depth() {
    var st = root.history && root.history.state;
    return (st && typeof st.mrbLib === "number") ? st.mrbLib : 0;
  }
  /* `push`: 1 = a new history entry (Back returns here); 0 = replace. */
  function go(hash, push) {
    var base = root.location.pathname + root.location.search;
    try {
      if (push) { root.history.pushState({ mrbLib: depth() + 1 }, "", base + hash); }
      else { root.history.replaceState({ mrbLib: depth() }, "", base + hash); }
    } catch (e) { root.location.hash = hash; return; }
    route();
  }
  function parse() {
    var hsh = root.location.hash || "";
    if (hsh === "#sets") { return { screen: "sets" }; }
    var m = /^#set=([0-9a-f-]{36})$/i.exec(hsh);
    if (m) { return { screen: "set", id: m[1].toLowerCase() }; }
    return null;
  }
  function route() {
    var want = parse();
    if (!want || !S.sb || !ready().length) { if (S.screen) { hide(); } return; }
    var opening = !S.screen;
    build();
    if (opening) {
      var active = doc.activeElement;
      S.returnTo = active && active !== doc.body ? active : null;
      show(els.root, true);
      doc.documentElement.setAttribute("data-mrb-library-open", "");
    }
    if (S.renaming) { endRename(false); }
    S.screen = want.screen;
    if (want.screen === "set") { openSet(want.id); } else { drawSets(); }
    if (opening) { els.dlg.focus({ preventScroll: true }); }
  }
  function hide() {
    if (!els) { S.screen = null; return; }
    if (S.renaming) { endRename(true); }
    S.screen = null;
    /* the next open of any set starts at card 1, face up, in order */
    S.set = null; S.order = []; S.pos = 0; S.flipped = false; S.shuffled = false;
    show(els.root, false);
    doc.documentElement.removeAttribute("data-mrb-library-open");
    var back = S.returnTo && doc.contains(S.returnTo) ? S.returnTo : doc.querySelector("[data-mrb-library-open]");
    S.returnTo = null;
    if (back && typeof back.focus === "function") { back.focus({ preventScroll: true }); }
  }
  /* × and Escape: step back out of every entry the library pushed, so Back
     afterwards goes where it went before the library opened. */
  function close() {
    var n = depth();
    if (n > 0 && parse()) { root.history.go(-n); return; }
    try { root.history.replaceState(null, "", root.location.pathname + root.location.search); } catch (e) {}
    hide();
  }
  function toSets() {
    if (depth() > 1) { root.history.back(); return; }
    go("#sets", 0);
  }

  var FOCUSABLE = "button,input,[tabindex]";
  function focusables() {
    return Array.prototype.filter.call(els.dlg.querySelectorAll(FOCUSABLE), function (n) {
      if (n.disabled || n.getAttribute("tabindex") === "-1") { return false; }
      for (var p = n; p && p !== els.dlg; p = p.parentNode) { if (p.hasAttribute && p.hasAttribute("hidden")) { return false; } }
      return true;
    });
  }

  function wire() {
    var e = els;
    e.close.addEventListener("click", close);
    e.back.addEventListener("click", toSets);
    e.retry.addEventListener("click", function () { S.setsLoading = null; drawSets(); });
    e.setRetry.addEventListener("click", function () { S.setsLoading = S.sets ? S.setsLoading : null; drawSet(); });
    e.card.addEventListener("click", flip);
    e.prev.addEventListener("click", function () { step(-1); });
    e.next.addEventListener("click", function () { step(1); });
    e.shuffle.addEventListener("click", toggleShuffle);
    e.name.addEventListener("click", startRename);
    e.input.addEventListener("keydown", function (ev) {
      if (ev.key === "Enter") { ev.preventDefault(); endRename(true); e.name.focus({ preventScroll: true }); }
      else if (ev.key === "Escape") { ev.preventDefault(); ev.stopPropagation(); endRename(false); e.name.focus({ preventScroll: true }); }
    });
    e.input.addEventListener("blur", function () { endRename(true); });
    /* a tap on the scrim, outside the column, closes */
    e.root.addEventListener("click", function (ev) { if (ev.target === e.root) { close(); } });
    doc.addEventListener("keydown", function (ev) {
      if (!S.screen) { return; }
      if (ev.key === "Escape") { ev.preventDefault(); close(); return; }
      if (ev.key === "Tab") {
        var items = focusables();
        if (!items.length) { return; }
        var first = items[0], last = items[items.length - 1], here = doc.activeElement;
        if (ev.shiftKey && (here === first || !e.dlg.contains(here) || here === e.dlg)) { ev.preventDefault(); last.focus(); }
        else if (!ev.shiftKey && (here === last || !e.dlg.contains(here))) { ev.preventDefault(); first.focus(); }
        return;
      }
      if (S.screen !== "set" || S.renaming) { return; }
      var tag = (ev.target && ev.target.tagName) || "";
      if (tag === "INPUT" || tag === "TEXTAREA") { return; }
      if (ev.key === "ArrowLeft") { ev.preventDefault(); step(-1); }
      else if (ev.key === "ArrowRight") { ev.preventDefault(); step(1); }
    });
    root.addEventListener("resize", function () { if (S.screen === "set") { fit(); } });
  }

  root.addEventListener && root.addEventListener("hashchange", route);

  /* ═════════════════════════════════════════════════════════════════════
     THE ENTRY POINT — student-live.js, after the class page has painted.
     `sb` is the pupil's own Supabase client; `counts` is {assignment id:
     number of cards} for the sets in `__MRB_LIBRARY_READY__`.
     ═════════════════════════════════════════════════════════════════════ */
  function offer(sb, uid, counts) {
    S.sb = sb; S.uid = uid; S.counts = counts || {};
    S.sets = null; S.setsLoading = null;
    if (!S.hooked) {
      S.hooked = true;
      root.__MRB_AFTER_DRAW__ = root.__MRB_AFTER_DRAW__ || [];
      root.__MRB_AFTER_DRAW__.push(function (host) { place(host); });
    }
    loadCss();
    place(doc.getElementById("mrb-student") || doc);
    if (parse()) { route(); }
  }

  root.MRBFlashcardLibrary = {
    offer: offer, close: close,
    _state: function () { return S; }
  };
})(window);
