/* ═══════════════════════════════════════════════════════════════════════
   flashcard-decks.js — MRB-351. The flashcard DECK: where one comes from,
   the review table a teacher checks it in, and the list they pick it from.

   Surface (window):
     MRBDeckApi      — the reads and writes, over the guard's supabase client
                       and the `flashcard-extract` edge function.
     MRBDeckEditor   — .create(opts): the review table, one screen.
     MRBDeckSource   — .create(opts): Upload · Paste · Type · My decks ·
                       Shared, and the extraction progress between them.
     MRBDeckPanel    — .open(label, node, onClose): the overlay the deck
                       library page puts either of the above in.

   Two callers, one component: the Set work sheet (shared/set-work.js, which
   loads this file on demand the first time Flashcards is chosen) and the
   deck library (teacher/decks.html). Neither owns a copy of any of this.

   ── RULES THIS FILE KEEPS ─────────────────────────────────────────────
   · NO innerHTML. A card is a teacher's text, and it is set with
     textContent or drawn by `MRBFormulae.fill` (text nodes and <sub>).
   · FORMULAE ARE DRAWN, NEVER STORED. An editing field holds the flat string
     (`CO2`); the read-only line under it and every list title draws CO₂.
   · NO SENTENCES. Labels, counts, button verbs and short status nouns. A
     disabled Save and an outlined field are the whole of validation.
   · The chrome is set-work.css's: `.sw-label`, `.sw-chip`, `.sw-row`,
     `.sw-btn`, `.sw-input`. flashcard-decks.css adds only the card rows,
     the progress bar and the icon buttons.
   ═══════════════════════════════════════════════════════════════════════ */
(function () {
  "use strict";

  var MAX_CARDS = 200;
  var Q_MAX = 400;
  var A_MAX = 600;
  var REF_MAX = 40;
  var TITLE_MAX = 120;
  var LOW_CONFIDENCE = 0.6;
  var POLL_MS = 1000;
  var POLL_LIMIT_MS = 4 * 60 * 1000;
  var BLANK_ROWS = 3;

  var ACCEPT = ".pptx,.docx,.pdf,.xlsx,.csv,.txt,.md,.png,.jpg,.jpeg,.heic";

  var SAY = {
    upload: "Upload",
    paste: "Paste",
    type: "Type",
    myDecks: "My decks",
    shared: "Shared",
    chooseFile: "Choose file",
    makeCards: "Make cards",
    reading: function (p) { return "Reading… " + p + "%"; },
    useBefore: "Use the cards extracted before",
    readAgain: "Read it again",
    deckTitle: "Deck title",
    subject: "Subject",
    subjects: { biology: "Biology", chemistry: "Chemistry", physics: "Physics" },
    question: "Question",
    answer: "Answer",
    source: "Source",
    move: "Move",
    up: "Up",
    down: "Down",
    swap: "Swap",
    swapAll: "Swap all",
    del: "Delete",
    addCard: "Add card",
    saveDeck: "Save deck",
    tryAgain: "Try extraction again",
    blank: "Start from blank",
    check: "Check",
    search: "Search",
    edit: "Edit",
    draft: "Draft",
    loading: "Loading",
    unavailable: "Unavailable",
    notSaved: "Not saved",
    noDecks: "No decks yet",
    noMatch: "No decks",
    close: "Close",
    cards: function (n) { return n + (n === 1 ? " card" : " cards"); },
    needAnswer: function (n) { return n + (n === 1 ? " needs an answer" : " need an answer"); },
    needQuestion: function (n) { return n + (n === 1 ? " needs a question" : " need a question"); },
    /* The server's refusal codes, as the short noun each one is. */
    err: {
      too_big: "Over 25 MB",
      unsupported_type: "Unsupported file",
      empty_paste: "Nothing pasted",
      nothing_to_read: "Nothing to read",
      no_file: "No file",
      too_many_pages: "Over 60 pages",
      heic_unconverted: "HEIC unreadable",
      unreadable_file: "Unreadable file",
      deck_not_found: "Deck not found",
      not_your_deck: "Not your deck"
    }
  };

  /* ═════════════════════════════════════════════════════════════════════
     DOM helpers
     ═════════════════════════════════════════════════════════════════════ */

  function el(tag, cls, text) {
    var n = document.createElement(tag);
    if (cls) { n.className = cls; }
    if (text !== undefined && text !== null) { n.textContent = text; }
    return n;
  }
  function btn(cls, text) {
    var b = el("button", cls, text);
    b.type = "button";
    return b;
  }
  function mark(n, name) { n.setAttribute("data-fd", name); return n; }

  var SVGNS = "http://www.w3.org/2000/svg";
  function icon(paths, size) {
    var s = document.createElementNS(SVGNS, "svg");
    var z = String(size || 18);
    s.setAttribute("width", z); s.setAttribute("height", z);
    s.setAttribute("viewBox", "0 0 20 20"); s.setAttribute("fill", "none");
    s.setAttribute("aria-hidden", "true");
    paths.forEach(function (d) {
      var p = document.createElementNS(SVGNS, "path");
      p.setAttribute("d", d);
      p.setAttribute("stroke", "currentColor");
      p.setAttribute("stroke-width", "1.7");
      p.setAttribute("stroke-linecap", "round");
      p.setAttribute("stroke-linejoin", "round");
      s.appendChild(p);
    });
    return s;
  }
  var ICONS = {
    grip: ["M7 5h.01", "M13 5h.01", "M7 10h.01", "M13 10h.01", "M7 15h.01", "M13 15h.01"],
    up: ["M10 15V5", "M5.5 9.5L10 5l4.5 4.5"],
    down: ["M10 5v10", "M5.5 10.5L10 15l4.5-4.5"],
    swap: ["M6 3v12", "M3 12l3 3 3-3", "M14 17V5", "M11 8l3-3 3 3"],
    del: ["M5 5l10 10", "M15 5L5 15"]
  };
  function iconBtn(name, label, dataName) {
    var b = btn("fd-icon", null);
    b.setAttribute("aria-label", label);
    b.title = label;
    b.appendChild(icon(ICONS[name]));
    return mark(b, dataName);
  }

  function formulae() { return window.MRBFormulae || null; }

  /* Read-only text: formulae drawn with <sub>. Editing fields never pass
     through here — they hold the flat string the teacher typed. */
  function draw(node, text) {
    var F = formulae();
    if (F && F.fill) { F.fill(node, String(text == null ? "" : text)); }
    else { node.textContent = String(text == null ? "" : text); }
    return node;
  }
  function hasFormula(text) {
    var F = formulae();
    if (!F || !F.segments || !text) { return false; }
    var segs = F.segments(String(text));
    for (var i = 0; i < segs.length; i++) {
      if (segs[i].sub !== undefined) { return true; }
    }
    return false;
  }

  /* "12 Sep 2026", in London — the same three-letter months the Set work
     sheet writes (`londonDateLabel`), never ICU's "Sept". Display only. */
  var MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
                "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"];
  var LDN_DATE = null;
  function dateLabel(iso) {
    var ms = Date.parse(iso || "");
    if (isNaN(ms)) { return ""; }
    try {
      LDN_DATE = LDN_DATE || new Intl.DateTimeFormat("en-GB", {
        timeZone: "Europe/London", day: "numeric", month: "numeric", year: "numeric"
      });
      var parts = {};
      LDN_DATE.formatToParts(new Date(ms)).forEach(function (x) { parts[x.type] = x.value; });
      return Number(parts.day) + " " + MONTHS[Number(parts.month) - 1] + " " + parts.year;
    } catch (e) { return new Date(ms).toISOString().slice(0, 10); }
  }

  var UUID_RE = /^[0-9a-f-]{36}$/i;

  /* ═════════════════════════════════════════════════════════════════════
     THE DATA SEAM — every read and write this feature makes from a teacher
     page. The client is the guard's; RLS is the boundary, not this file.
     ═════════════════════════════════════════════════════════════════════ */

  function sb() {
    var g = window.MrBadmusTeacherGuard;
    var c = (g && g.getClient) ? g.getClient() : null;
    if (!c) { throw new Error("flashcards: no data layer"); }
    return c;
  }

  function session() {
    return Promise.resolve().then(function () {
      return sb().auth.getSession();
    }).then(function (r) {
      var s = r && r.data && r.data.session;
      if (!s || !s.access_token) { throw new Error("flashcards: not signed in"); }
      return s;
    });
  }

  /* supabase-js answers {data, error}; a refusal's `error.message` is the
     server's code. Turned into a rejection carrying that code. */
  function unwrap(r) {
    if (r && r.error) {
      var e = new Error(String(r.error.message || r.error.code || "error"));
      e.code = String(r.error.message || r.error.code || "error");
      throw e;
    }
    return r ? r.data : null;
  }

  var DECK_COLS = "id,title,card_count,created_by,shared_with_school,status," +
                  "source_kind,source_file_name,subject,updated_at,deleted_at";
  var CARD_COLS = "id,position,question,answer,source_ref,confidence,flagged";

  function personName(p) {
    if (!p) { return ""; }
    if (p.display_name) { return String(p.display_name); }
    return [p.first_name, p.last_name].filter(Boolean).join(" ");
  }

  var api = {
    uid: function () {
      return session().then(function (s) { return (s.user && s.user.id) || ""; });
    },

    /* Every deck this teacher can see — their own (deleted ones included, so
       the library can say a deleted deck is still in use) and the school's
       shared ones — each with its author's name and `mine`. */
    list: function () {
      var me = "";
      return api.uid().then(function (u) {
        me = u;
        return sb().from("flashcard_decks").select(DECK_COLS)
          .order("updated_at", { ascending: false });
      }).then(function (r) {
        var decks = unwrap(r) || [];
        var ids = [];
        decks.forEach(function (d) {
          if (d.created_by && ids.indexOf(d.created_by) < 0) { ids.push(d.created_by); }
        });
        if (!ids.length) { return { decks: decks, people: [] }; }
        return sb().from("profiles").select("id,first_name,last_name,display_name")
          .in("id", ids).then(function (pr) {
            return { decks: decks, people: (pr && pr.data) || [] };
          }, function () { return { decks: decks, people: [] }; });
      }).then(function (o) {
        var names = {};
        o.people.forEach(function (p) { names[p.id] = personName(p); });
        return {
          uid: me,
          decks: o.decks.map(function (d) {
            var x = {};
            for (var k in d) { if (Object.prototype.hasOwnProperty.call(d, k)) { x[k] = d[k]; } }
            x.mine = !!me && d.created_by === me;
            x.author = names[d.created_by] || "";
            return x;
          })
        };
      });
    },

    deck: function (id) {
      return sb().from("flashcard_decks").select(DECK_COLS).eq("id", id)
        .maybeSingle().then(unwrap);
    },

    cards: function (id) {
      return sb().from("flashcard_cards").select(CARD_COLS).eq("deck_id", id)
        .order("position").then(function (r) { return unwrap(r) || []; });
    },

    /* How many live assignments (that this viewer can see) are made from it. */
    usage: function (id) {
      return sb().from("assignments").select("id", { count: "exact", head: true })
        .eq("deck_id", id).is("deleted_at", null).then(function (r) {
          if (r && r.error) { throw new Error(String(r.error.message || "error")); }
          return (r && typeof r.count === "number") ? r.count : 0;
        });
    },

    save: function (deckId, title, cards, meta, finalise) {
      return sb().rpc("flashcard_deck_save", {
        p_deck: deckId || null,
        p_title: title,
        p_cards: cards,
        p_meta: meta || {},
        p_finalise: finalise !== false
      }).then(unwrap);
    },

    duplicate: function (id) {
      return sb().rpc("flashcard_deck_duplicate", { p_deck: id }).then(unwrap);
    },

    share: function (id, on) {
      return sb().from("flashcard_decks").update({ shared_with_school: !!on })
        .eq("id", id).then(unwrap);
    },

    remove: function (id) {
      return sb().from("flashcard_decks")
        .update({ deleted_at: new Date().toISOString() })
        .eq("id", id).then(unwrap);
    },

    /* POST to the extraction function. `body` is a FormData (a file) or an
       object ({paste,title} | {deck_id,rerun:true}). Resolves
       {status, ok, body}; never rejects on an HTTP refusal. */
    extract: function (body) {
      var c = window.MrBadmusConfig || {};
      return session().then(function (s) {
        var headers = { Authorization: "Bearer " + s.access_token,
                        apikey: c.SUPABASE_ANON_KEY || "" };
        var payload = body;
        if (!(typeof FormData !== "undefined" && body instanceof FormData)) {
          headers["Content-Type"] = "application/json";
          payload = JSON.stringify(body);
        }
        return fetch(String(c.SUPABASE_URL || "") + "/functions/v1/flashcard-extract",
                     { method: "POST", headers: headers, body: payload });
      }).then(function (res) {
        return res.json().then(
          function (d) { return { status: res.status, ok: res.ok, body: d }; },
          function () { return { status: res.status, ok: res.ok, body: null }; });
      });
    },

    /* Poll one extraction job until it settles. `onTick(row)` on every read;
       `alive()` false abandons it (the teacher moved on). */
    poll: function (jobId, onTick, alive) {
      var started = Date.now();
      return new Promise(function (resolve) {
        function again() {
          if (Date.now() - started > POLL_LIMIT_MS) {
            resolve({ status: "failed", error: "timeout" });
            return;
          }
          setTimeout(tick, POLL_MS);
        }
        function tick() {
          if (alive && !alive()) { resolve(null); return; }
          var q;
          try {
            q = sb().from("flashcard_extractions")
              .select("status,progress,error,pairs_found,needs_answer,method")
              .eq("id", jobId).maybeSingle();
          } catch (e) { again(); return; }
          q.then(function (r) {
            if (alive && !alive()) { resolve(null); return; }
            var row = r && r.data;
            if (row && onTick) { onTick(row); }
            if (row && (row.status === "done" || row.status === "failed")) {
              resolve(row);
              return;
            }
            again();
          }, again);
        }
        tick();
      });
    }
  };

  /* A HEIC photo, redrawn as a JPEG where this browser can decode one
     (Safari can; most others cannot, and the server then says so). */
  function heicToJpeg(file) {
    var isHeic = /\.heic$/i.test(file.name || "") || /heic|heif/i.test(file.type || "");
    if (!isHeic || typeof createImageBitmap !== "function") { return Promise.resolve(file); }
    return createImageBitmap(file).then(function (bmp) {
      var cv = document.createElement("canvas");
      cv.width = bmp.width; cv.height = bmp.height;
      cv.getContext("2d").drawImage(bmp, 0, 0);
      return new Promise(function (resolve) {
        cv.toBlob(function (blob) {
          if (!blob) { resolve(file); return; }
          var name = String(file.name || "photo.heic").replace(/\.hei[cf]$/i, ".jpg");
          try { resolve(new File([blob], name, { type: "image/jpeg" })); }
          catch (e) { blob.name = name; resolve(blob); }
        }, "image/jpeg", 0.9);
      });
    }).catch(function () { return file; });
  }

  function baseName(name) {
    return String(name || "").replace(/\.[^.]+$/, "").replace(/[_]+/g, " ").trim()
      .slice(0, TITLE_MAX);
  }

  /* ═════════════════════════════════════════════════════════════════════
     THE REVIEW TABLE
     opts: { deck: {id, title, subject, source_kind}, cards: [...],
             onSaved(deck), onRerun(deck), onBlank(deck) }
     ═════════════════════════════════════════════════════════════════════ */

  function needsLook(c) {
    if (!String(c.question || "").trim() || !String(c.answer || "").trim()) { return true; }
    if (c.reviewed) { return false; }
    if (c.flagged) { return true; }
    return typeof c.confidence === "number" && c.confidence < LOW_CONFIDENCE;
  }

  function createEditor(opts) {
    var o = opts || {};
    var deck = o.deck || {};
    var cards = [];
    var saving = false;
    var badTitle = false;
    /* Anything the teacher has changed since the last save. A deck with
       unsaved edits is not a deck that can be set. */
    var dirty = false;
    function touch() { dirty = true; }

    var root = mark(el("div", "fd-editor"), "editor");

    root.appendChild(el("div", "sw-label", SAY.deckTitle));
    var titleWrap = el("div", "sw-fields");
    var title = mark(document.createElement("input"), "title");
    title.type = "text";
    title.className = "sw-input";
    title.maxLength = TITLE_MAX;
    title.setAttribute("aria-label", SAY.deckTitle);
    title.value = String(deck.title || "");
    titleWrap.appendChild(title);
    root.appendChild(titleWrap);

    root.appendChild(el("div", "sw-label", SAY.subject));
    var subjHost = mark(el("div", "sw-chips"), "subject");
    var subject = deck.subject || "";
    var subjChips = ["biology", "chemistry", "physics"].map(function (k) {
      var b = btn("sw-chip", SAY.subjects[k]);
      b.setAttribute("data-fd-key", k);
      b.addEventListener("click", function () {
        subject = (subject === k) ? "" : k;
        touch();
        syncSubject();
        sync();
      });
      subjHost.appendChild(b);
      return { key: k, node: b };
    });
    root.appendChild(subjHost);

    var bar = el("div", "fd-bar");
    var count = mark(el("div", "fd-count"), "count");
    count.setAttribute("aria-live", "polite");
    var swapAll = mark(btn("sw-btn", SAY.swapAll), "swap-all");
    bar.appendChild(count); bar.appendChild(swapAll);
    root.appendChild(bar);

    var rows = mark(el("div", "fd-rows"), "rows");
    root.appendChild(rows);

    var add = mark(btn("sw-btn sw-add", SAY.addCard), "add");
    root.appendChild(add);

    var foot = el("div", "fd-foot");
    var save = mark(btn("sw-btn sw-btn-primary", SAY.saveDeck), "save");
    var rerun = mark(btn("sw-btn", SAY.tryAgain), "rerun");
    var blank = mark(btn("sw-btn", SAY.blank), "blank");
    var saveNote = mark(el("div", "sw-row-tag", SAY.notSaved), "save-note");
    saveNote.hidden = true;
    foot.appendChild(save); foot.appendChild(rerun); foot.appendChild(blank);
    root.appendChild(foot);
    root.appendChild(saveNote);

    function syncSubject() {
      subjChips.forEach(function (c) {
        c.node.classList.toggle("is-on", c.key === subject);
        c.node.setAttribute("aria-pressed", c.key === subject ? "true" : "false");
      });
    }

    function renderLine(node, text) {
      var show = hasFormula(text);
      node.hidden = !show;
      if (show) { draw(node, text); } else { node.textContent = ""; }
    }

    function buildRow(c) {
      var row = mark(el("div", "fd-card"), "card");
      var head = el("div", "fd-card-head");
      var handle = iconBtn("grip", SAY.move, "handle");
      handle.classList.add("fd-handle");
      var n = el("span", "fd-n", "");
      var flag = mark(el("span", "fd-flag", SAY.check), "flag");
      var spacer = el("span", "fd-spacer");
      var up = iconBtn("up", SAY.up, "up");
      var down = iconBtn("down", SAY.down, "down");
      var sw = iconBtn("swap", SAY.swap, "swap");
      var del = iconBtn("del", SAY.del, "delete");
      head.appendChild(handle); head.appendChild(n); head.appendChild(flag);
      head.appendChild(spacer);
      head.appendChild(up); head.appendChild(down); head.appendChild(sw); head.appendChild(del);

      var q = mark(document.createElement("textarea"), "q");
      q.className = "sw-input fd-text";
      q.rows = 2;
      q.maxLength = Q_MAX;
      q.placeholder = SAY.question;
      q.setAttribute("aria-label", SAY.question);
      q.value = c.question || "";
      var qLine = mark(el("div", "fd-render"), "q-render");

      var a = mark(document.createElement("textarea"), "a");
      a.className = "sw-input fd-text";
      a.rows = 2;
      a.maxLength = A_MAX;
      a.placeholder = SAY.answer;
      a.setAttribute("aria-label", SAY.answer);
      a.value = c.answer || "";
      var aLine = mark(el("div", "fd-render"), "a-render");

      var refWrap = el("label", "fd-ref-wrap");
      refWrap.appendChild(el("span", "fd-ref-label", SAY.source));
      var ref = mark(document.createElement("input"), "ref");
      ref.type = "text";
      ref.className = "fd-ref";
      ref.maxLength = REF_MAX;
      ref.setAttribute("aria-label", SAY.source);
      ref.value = c.source_ref || "";
      refWrap.appendChild(ref);

      row.appendChild(head);
      row.appendChild(q); row.appendChild(qLine);
      row.appendChild(a); row.appendChild(aLine);
      row.appendChild(refWrap);

      c.els = { row: row, n: n, flag: flag, q: q, a: a, qLine: qLine, aLine: aLine,
                ref: ref, up: up, down: down };

      q.addEventListener("input", function () {
        c.question = q.value; c.reviewed = true; touch(); renderLine(qLine, q.value); sync();
      });
      a.addEventListener("input", function () {
        c.answer = a.value; c.reviewed = true; touch(); renderLine(aLine, a.value); sync();
      });
      ref.addEventListener("input", function () { c.source_ref = ref.value; touch(); sync(); });
      sw.addEventListener("click", function () { swapOne(c); touch(); sync(); });
      del.addEventListener("click", function () {
        var i = cards.indexOf(c);
        if (i < 0) { return; }
        cards.splice(i, 1);
        if (row.parentNode) { row.parentNode.removeChild(row); }
        touch();
        sync();
      });
      up.addEventListener("click", function () { moveBy(c, -1); });
      down.addEventListener("click", function () { moveBy(c, 1); });
      wireDrag(handle, c);

      renderLine(qLine, c.question);
      renderLine(aLine, c.answer);
      return row;
    }

    function swapOne(c) {
      var t = c.question;
      c.question = c.answer;
      c.answer = t;
      c.els.q.value = c.question || "";
      c.els.a.value = c.answer || "";
      renderLine(c.els.qLine, c.question);
      renderLine(c.els.aLine, c.answer);
    }

    function moveBy(c, d) {
      var i = cards.indexOf(c), j = i + d;
      if (i < 0 || j < 0 || j >= cards.length) { return; }
      cards.splice(i, 1);
      cards.splice(j, 0, c);
      var ref = cards[j + 1] ? cards[j + 1].els.row : null;
      rows.insertBefore(c.els.row, ref);
      touch();
      sync();
    }

    /* Drag by the handle: pointer events, so a finger and a mouse are one
       code path. The row moves in the DOM as the pointer crosses another
       row's midpoint; the order is read back from the DOM on release. */
    function wireDrag(handle, c) {
      var active = false;
      handle.addEventListener("pointerdown", function (e) {
        if (e.button !== undefined && e.button !== 0) { return; }
        active = true;
        try { handle.setPointerCapture(e.pointerId); } catch (x) { /* old engine */ }
        c.els.row.classList.add("is-drag");
        e.preventDefault();
      });
      /* ⚠️ THE DRAGGED ROW IS NEVER DETACHED. Moving it with insertBefore
         removes it from the tree for an instant, which releases the pointer
         capture, and the release then lands on whatever is underneath —
         measured: `lostpointercapture` and no `pointerup`, so the order was
         never read back. The NEIGHBOURS move past it instead. */
      handle.addEventListener("pointermove", function (e) {
        if (!active) { return; }
        var y = e.clientY, me = c.els.row, r, sib;
        sib = me.nextElementSibling;
        while (sib) {
          r = sib.getBoundingClientRect();
          if (y <= r.top + r.height / 2) { break; }
          rows.insertBefore(sib, me);
          sib = me.nextElementSibling;
        }
        sib = me.previousElementSibling;
        while (sib) {
          r = sib.getBoundingClientRect();
          if (y >= r.top + r.height / 2) { break; }
          rows.insertBefore(sib, me.nextElementSibling);
          sib = me.previousElementSibling;
        }
      });
      function end() {
        if (!active) { return; }
        active = false;
        c.els.row.classList.remove("is-drag");
        var order = Array.prototype.slice.call(rows.children);
        cards.sort(function (x, y) {
          return order.indexOf(x.els.row) - order.indexOf(y.els.row);
        });
        touch();
        sync();
      }
      handle.addEventListener("pointerup", end);
      handle.addEventListener("pointercancel", end);
      handle.addEventListener("lostpointercapture", end);
    }

    function counts() {
      var needA = 0, needQ = 0;
      cards.forEach(function (c) {
        if (!String(c.question || "").trim()) { needQ += 1; }
        if (!String(c.answer || "").trim()) { needA += 1; }
      });
      return { n: cards.length, needAnswer: needA, needQuestion: needQ };
    }

    function valid() {
      var k = counts();
      var t = String(title.value || "").trim();
      return k.n > 0 && k.n <= MAX_CARDS && !k.needAnswer && !k.needQuestion &&
             t.length >= 1 && t.length <= TITLE_MAX && !saving;
    }

    function sync() {
      var k = counts();
      var parts = [SAY.cards(k.n)];
      if (k.needAnswer) { parts.push(SAY.needAnswer(k.needAnswer)); }
      if (k.needQuestion) { parts.push(SAY.needQuestion(k.needQuestion)); }
      count.textContent = parts.join(" · ");
      cards.forEach(function (c, i) {
        c.els.n.textContent = String(i + 1);
        var look = needsLook(c);
        c.els.row.classList.toggle("is-flag", look);
        c.els.flag.hidden = !look;
        c.els.q.classList.toggle("sw-bad", !String(c.question || "").trim() && c.touched);
        c.els.a.classList.toggle("sw-bad", !String(c.answer || "").trim() && c.touched);
        c.els.up.disabled = (i === 0);
        c.els.down.disabled = (i === cards.length - 1);
      });
      title.classList.toggle("sw-bad", badTitle || !String(title.value || "").trim());
      add.disabled = cards.length >= MAX_CARDS;
      swapAll.disabled = !cards.length;
      save.disabled = !valid();
      rerun.hidden = !(deck.id && deck.source_kind === "upload" && o.onRerun);
      blank.hidden = !o.onBlank;
      if (o.onChange) { o.onChange(api2); }
    }

    function load(list, sortFlagged) {
      rows.textContent = "";
      cards = (list || []).map(function (x) {
        return {
          id: (x.id && UUID_RE.test(String(x.id))) ? String(x.id) : "",
          question: String(x.question || ""),
          answer: String(x.answer || ""),
          source_ref: x.source_ref ? String(x.source_ref) : "",
          confidence: (typeof x.confidence === "number") ? x.confidence : null,
          flagged: !!x.flagged,
          reviewed: false,
          touched: false
        };
      });
      /* Rows that need a look go first, in their own order, when the table
         first opens. Afterwards the order is the teacher's. */
      if (sortFlagged) {
        var look = [], rest = [];
        cards.forEach(function (c) { (needsLook(c) ? look : rest).push(c); });
        cards = look.concat(rest);
      }
      cards.forEach(function (c) { rows.appendChild(buildRow(c)); });
      sync();
    }

    function blankCard() {
      return { id: "", question: "", answer: "", source_ref: "", confidence: null,
               flagged: false, reviewed: true, touched: false };
    }

    add.addEventListener("click", function () {
      if (cards.length >= MAX_CARDS) { return; }
      var c = blankCard();
      cards.push(c);
      touch();
      rows.appendChild(buildRow(c));
      sync();
      try { c.els.q.focus(); } catch (e) { /* gone */ }
    });

    swapAll.addEventListener("click", function () {
      cards.forEach(swapOne);
      touch();
      sync();
    });

    title.addEventListener("input", function () { badTitle = false; touch(); sync(); });

    rerun.addEventListener("click", function () {
      if (o.onRerun) { o.onRerun(deck); }
    });
    blank.addEventListener("click", function () {
      if (o.onBlank) { o.onBlank(deck); }
    });

    save.addEventListener("click", function () {
      /* A card left empty is outlined only once Save has been tried or the
         field has been typed in — never on a table that just opened. */
      cards.forEach(function (c) { c.touched = true; });
      if (!valid()) { sync(); return; }
      saving = true;
      saveNote.hidden = true;
      sync();
      var t = String(title.value || "").trim();
      var payload = cards.map(function (c) {
        var x = {
          question: String(c.question || "").trim(),
          answer: String(c.answer || "").trim(),
          flagged: !!(c.flagged && !c.reviewed)
        };
        if (c.id) { x.id = c.id; }
        if (String(c.source_ref || "").trim()) { x.source_ref = String(c.source_ref).trim(); }
        if (typeof c.confidence === "number") { x.confidence = c.confidence; }
        return x;
      });
      var meta = { source_kind: deck.source_kind || "typed", subject: subject || null };
      api.save(deck.id || null, t, payload, meta, true).then(function (r) {
        saving = false;
        var out = {
          id: (r && r.deck_id) || deck.id,
          title: t,
          card_count: (r && typeof r.card_count === "number") ? r.card_count : payload.length,
          status: (r && r.status) || "ready",
          subject: subject || null,
          source_kind: deck.source_kind || "typed",
          mine: true
        };
        deck.id = out.id;
        deck.title = t;
        dirty = false;
        sync();
        if (o.onSaved) { o.onSaved(out); }
      }, function (e) {
        saving = false;
        if (e && e.code === "bad_title") { badTitle = true; }
        saveNote.hidden = false;
        sync();
      });
    });

    var api2 = {
      node: root,
      load: load,
      counts: counts,
      valid: valid,
      dirty: function () { return dirty; },
      deck: function () { return deck; },
      title: function () { return String(title.value || "").trim(); }
    };

    syncSubject();
    load(o.cards || [], o.sortFlagged !== false);
    return api2;
  }

  /* ═════════════════════════════════════════════════════════════════════
     THE DECK STEP — where a deck comes from.
     opts: { picker: bool (My decks / Shared chips), chips: bool (default
             true), onReady(deck), onChange() }
     ═════════════════════════════════════════════════════════════════════ */

  function createSource(opts) {
    var o = opts || {};
    var picker = !!o.picker;
    var seq = 0;                   // bumped whenever the teacher moves on
    var view = "";
    var chosen = null;             // a READY deck, picked or saved
    var editor = null;
    var lastFile = null;
    var lastDeckId = "";
    var listCache = null;
    var listSeq = 0;

    var root = mark(el("div", "fd-source"), "source");

    var chipDefs = [
      { key: "upload", label: SAY.upload },
      { key: "paste", label: SAY.paste },
      { key: "type", label: SAY.type }
    ];
    if (picker) {
      chipDefs.push({ key: "mine", label: SAY.myDecks });
      chipDefs.push({ key: "shared", label: SAY.shared });
    }
    var chipHost = mark(el("div", "sw-chips fd-source-chips"), "source-chips");
    var chips = chipDefs.map(function (d) {
      var b = btn("sw-chip", d.label);
      b.setAttribute("data-fd-key", d.key);
      b.addEventListener("click", function () { show(d.key); });
      chipHost.appendChild(b);
      return { key: d.key, node: b };
    });
    if (o.chips === false) { chipHost.hidden = true; }
    root.appendChild(chipHost);

    /* ── panes ── */
    function pane(name) {
      var p = mark(el("div", "fd-pane"), "pane-" + name);
      p.hidden = true;
      root.appendChild(p);
      return p;
    }

    var pUpload = pane("upload");
    var fileLabel = el("label", "sw-btn fd-file");
    var fileInput = mark(document.createElement("input"), "file");
    fileInput.type = "file";
    fileInput.accept = ACCEPT;
    fileInput.className = "fd-file-input";
    fileLabel.appendChild(el("span", null, SAY.chooseFile));
    fileLabel.appendChild(fileInput);
    pUpload.appendChild(fileLabel);

    var pPaste = pane("paste");
    var pasteBox = mark(document.createElement("textarea"), "paste");
    pasteBox.className = "sw-input fd-paste";
    pasteBox.rows = 8;
    pasteBox.setAttribute("aria-label", SAY.paste);
    var makeBtn = mark(btn("sw-btn sw-btn-primary fd-make", SAY.makeCards), "make");
    makeBtn.disabled = true;
    pPaste.appendChild(pasteBox);
    pPaste.appendChild(makeBtn);

    var pProgress = pane("progress");
    var progLabel = mark(el("div", "fd-prog-label", SAY.reading(0)), "progress-label");
    var track = el("div", "fd-track");
    track.setAttribute("role", "progressbar");
    track.setAttribute("aria-valuemin", "0");
    track.setAttribute("aria-valuemax", "100");
    var fill = mark(el("div", "fd-fill"), "progress-fill");
    track.appendChild(fill);
    pProgress.appendChild(progLabel);
    pProgress.appendChild(track);

    var pCached = pane("cached");
    var cachedTitle = mark(el("div", "fd-cached-title"), "cached-title");
    var useBefore = mark(btn("sw-btn sw-btn-primary", SAY.useBefore), "use-before");
    var readAgain = mark(btn("sw-btn", SAY.readAgain), "read-again");
    var cachedBtns = el("div", "fd-foot");
    cachedBtns.appendChild(useBefore); cachedBtns.appendChild(readAgain);
    pCached.appendChild(cachedTitle);
    pCached.appendChild(cachedBtns);

    var pFail = pane("failed");
    var failNote = mark(el("div", "sw-row-tag", SAY.unavailable), "fail-note");
    var failRerun = mark(btn("sw-btn", SAY.tryAgain), "fail-rerun");
    var failBlank = mark(btn("sw-btn", SAY.blank), "fail-blank");
    var failBtns = el("div", "fd-foot");
    failBtns.appendChild(failRerun); failBtns.appendChild(failBlank);
    pFail.appendChild(failNote);
    pFail.appendChild(failBtns);

    var pEditor = pane("editor");

    var pList = pane("list");
    var search = mark(document.createElement("input"), "search");
    search.type = "search";
    search.className = "sw-input";
    search.placeholder = SAY.search;
    search.setAttribute("aria-label", SAY.search);
    var listWrap = el("div", "sw-fields");
    listWrap.appendChild(search);
    var listHost = mark(el("div", "sw-tree"), "deck-list");
    var listNote = mark(el("div", "sw-row-tag", ""), "list-note");
    listNote.hidden = true;
    pList.appendChild(listWrap);
    pList.appendChild(listNote);
    pList.appendChild(listHost);

    var panes = { upload: pUpload, paste: pPaste, progress: pProgress, cached: pCached,
                  failed: pFail, editor: pEditor, list: pList };

    function setPane(name) {
      for (var k in panes) {
        if (Object.prototype.hasOwnProperty.call(panes, k)) { panes[k].hidden = (k !== name); }
      }
      root.setAttribute("data-fd-pane", name);
    }

    function changed() { if (o.onChange) { o.onChange(self); } }

    function syncChips() {
      chips.forEach(function (c) {
        c.node.classList.toggle("is-on", c.key === view);
        c.node.setAttribute("aria-pressed", c.key === view ? "true" : "false");
      });
    }

    function show(key) {
      seq += 1;                          // abandon any poll in flight
      view = key;
      chosen = null;                     // a new view is a new choice
      syncChips();
      if (key === "upload") { setPane("upload"); }
      else if (key === "paste") { setPane("paste"); }
      else if (key === "type") {
        openEditor({ id: "", title: "", subject: null, source_kind: "typed" },
                   blanks(BLANK_ROWS), false);
      } else if (key === "mine" || key === "shared") {
        setPane("list");
        drawList();
      }
      changed();
    }

    function blanks(n) {
      var out = [];
      for (var i = 0; i < n; i++) { out.push({ question: "", answer: "" }); }
      return out;
    }

    function openEditor(deck, cards, sortFlagged) {
      pEditor.textContent = "";
      editor = createEditor({
        deck: deck,
        cards: cards,
        sortFlagged: sortFlagged,
        onSaved: function (d) {
          chosen = d;
          listCache = null;
          changed();
          if (o.onReady) { o.onReady(d, "saved"); }
        },
        onRerun: function (d) { rerunDeck(d.id); },
        onBlank: function (d) {
          openEditor({ id: d.id || "", title: editor ? editor.title() : (d.title || ""),
                       subject: d.subject || null, source_kind: d.source_kind || "typed" },
                     blanks(BLANK_ROWS), false);
        },
        onChange: function (ed) {
          if (chosen && ed.dirty()) { chosen = null; }
          changed();
        }
      });
      pEditor.appendChild(editor.node);
      setPane("editor");
      changed();
    }

    /* A deck that already exists, into the review table. */
    function editDeck(d) {
      var mine = ++seq;
      setPane("progress");
      progLabel.textContent = SAY.loading;
      fill.style.width = "0%";
      return api.cards(d.id).then(function (cards) {
        if (mine !== seq) { return; }
        openEditor({ id: d.id, title: d.title, subject: d.subject || null,
                     source_kind: d.source_kind || "typed" }, cards, true);
      }, function () {
        if (mine !== seq) { return; }
        fail("", d.id);
      });
    }

    function fail(code, deckId) {
      lastDeckId = deckId || lastDeckId;
      failNote.textContent = SAY.err[code] || SAY.unavailable;
      failRerun.hidden = !lastDeckId;
      setPane("failed");
      changed();
    }

    function progress(p) {
      var n = Math.max(0, Math.min(100, Math.round(Number(p) || 0)));
      progLabel.textContent = SAY.reading(n);
      fill.style.width = n + "%";
      track.setAttribute("aria-valuenow", String(n));
    }

    /* The extraction reply, whatever started it. */
    function handleReply(r, mine) {
      if (mine !== seq) { return; }
      var b = (r && r.body) || {};
      if (r && r.status === 200 && b.cached) {
        cachedTitle.textContent = "";
        draw(cachedTitle, String(b.cached.title || ""));
        var meta = el("span", "sw-row-tag", SAY.cards(Number(b.cached.card_count) || 0));
        cachedTitle.appendChild(meta);
        pCached.__cached = b.cached;
        setPane("cached");
        changed();
        return;
      }
      if (!r || !r.ok || !b.job_id) {
        fail(b.error || "", b.deck_id || "");
        return;
      }
      lastDeckId = b.deck_id || lastDeckId;
      setPane("progress");
      progress(10);
      api.poll(b.job_id, function (row) {
        if (mine === seq) { progress(row.progress); }
      }, function () { return mine === seq; }).then(function (row) {
        if (!row || mine !== seq) { return; }
        if (row.status !== "done") { fail(row.error || "", b.deck_id); return; }
        return Promise.all([api.deck(b.deck_id), api.cards(b.deck_id)]).then(function (res) {
          if (mine !== seq) { return; }
          var d = res[0] || { id: b.deck_id, title: "", source_kind: "upload" };
          openEditor({ id: d.id || b.deck_id, title: d.title || "", subject: d.subject || null,
                       source_kind: d.source_kind || "upload" }, res[1] || [], true);
        }, function () { if (mine === seq) { fail("", b.deck_id); } });
      });
    }

    function start(body) {
      var mine = ++seq;
      setPane("progress");
      progress(0);
      changed();
      return api.extract(body).then(function (r) { handleReply(r, mine); },
        function () { if (mine === seq) { fail("", ""); } });
    }

    function sendFile(file, force) {
      lastFile = file;
      var mine = ++seq;
      setPane("progress");
      progress(0);
      changed();
      return heicToJpeg(file).then(function (f) {
        if (mine !== seq) { return; }
        var fd = new FormData();
        fd.append("file", f, f.name || file.name || "upload");
        var t = baseName(file.name);
        if (t) { fd.append("title", t); }
        if (force) { fd.append("force", "1"); }
        return api.extract(fd).then(function (r) { handleReply(r, mine); },
          function () { if (mine === seq) { fail("", ""); } });
      });
    }

    function rerunDeck(id) {
      if (!id) { return; }
      lastDeckId = id;
      return start({ deck_id: id, rerun: true });
    }

    /* One selection is one upload. Some engines raise `change` twice for
       one pick (and a programmatic `files` assignment raises it on its own),
       so the same File object is never sent twice in a row. */
    var lastPicked = null;
    fileInput.addEventListener("change", function () {
      var f = fileInput.files && fileInput.files[0];
      if (!f || f === lastPicked) { return; }
      lastPicked = f;
      sendFile(f, false);
      try { fileInput.value = ""; } catch (e) { /* read-only in old engines */ }
    });

    pasteBox.addEventListener("input", function () {
      makeBtn.disabled = !String(pasteBox.value || "").trim();
    });
    makeBtn.addEventListener("click", function () {
      var text = String(pasteBox.value || "");
      if (!text.trim()) { return; }
      var first = text.trim().split(/\r?\n/)[0].trim().slice(0, 60);
      start({ paste: text, title: first || SAY.paste });
    });

    useBefore.addEventListener("click", function () {
      var c = pCached.__cached;
      if (!c || !c.deck_id) { return; }
      var mine = ++seq;
      /* A colleague's deck is theirs: it is copied first, and the copy is
         what this teacher checks and edits. */
      var idP = c.mine ? Promise.resolve(c.deck_id) : api.duplicate(c.deck_id);
      setPane("progress");
      progLabel.textContent = SAY.loading;
      idP.then(function (id) {
        if (mine !== seq) { return; }
        return Promise.all([api.deck(id), api.cards(id)]).then(function (res) {
          if (mine !== seq) { return; }
          var d = res[0] || { id: id, title: c.title, source_kind: "upload" };
          openEditor({ id: d.id || id, title: d.title || c.title || "", subject: d.subject || null,
                       source_kind: d.source_kind || "upload" }, res[1] || [], true);
        });
      }).catch(function () { if (mine === seq) { fail("", ""); } });
    });
    readAgain.addEventListener("click", function () {
      if (lastFile) { sendFile(lastFile, true); }
    });
    failRerun.addEventListener("click", function () { rerunDeck(lastDeckId); });
    failBlank.addEventListener("click", function () {
      openEditor({ id: lastDeckId || "", title: "", subject: null,
                   source_kind: lastDeckId ? "upload" : "typed" },
                 blanks(BLANK_ROWS), false);
    });

    /* ── the lists (My decks / Shared) ── */
    function loadList() {
      if (listCache) { return Promise.resolve(listCache); }
      var mine = ++listSeq;
      return api.list().then(function (r) {
        if (mine === listSeq) { listCache = r; }
        return r;
      });
    }

    function drawList() {
      listHost.textContent = "";
      listNote.hidden = false;
      listNote.textContent = SAY.loading;
      var forView = view;
      loadList().then(function (r) {
        if (view !== forView) { return; }
        var q = String(search.value || "").trim().toLowerCase();
        var decks = (r.decks || []).filter(function (d) {
          if (d.deleted_at) { return false; }
          if (forView === "mine") { return d.mine; }
          return !d.mine && d.shared_with_school && d.status === "ready";
        }).filter(function (d) {
          return !q || String(d.title || "").toLowerCase().indexOf(q) > -1;
        });
        listHost.textContent = "";
        if (!decks.length) {
          listNote.textContent = q ? SAY.noMatch : SAY.noDecks;
          listNote.hidden = false;
          return;
        }
        listNote.hidden = true;
        decks.forEach(function (d) { listHost.appendChild(deckRow(d)); });
      }, function () {
        if (view !== forView) { return; }
        listNote.textContent = SAY.unavailable;
        listNote.hidden = false;
      });
    }

    function deckRow(d) {
      var head = el("div", "sw-node-head");
      var row = mark(btn("sw-row", null), "deck");
      row.setAttribute("data-fd-id", String(d.id));
      var main = el("span", "sw-row-main");
      main.appendChild(draw(el("span", "sw-row-name"), d.title || ""));
      main.appendChild(el("span", "sw-row-tag", deckMeta(d)));
      row.appendChild(main);
      head.appendChild(row);
      var on = !!(chosen && chosen.id === d.id);
      row.classList.toggle("is-on", on);
      row.setAttribute("aria-pressed", on ? "true" : "false");
      row.addEventListener("click", function () {
        if (d.status !== "ready") { editDeck(d); return; }
        chosen = d;
        Array.prototype.forEach.call(listHost.querySelectorAll("[data-fd=deck]"), function (n) {
          var me = n === row;
          n.classList.toggle("is-on", me);
          n.setAttribute("aria-pressed", me ? "true" : "false");
        });
        changed();
        if (o.onReady) { o.onReady(d, "picked"); }
      });
      if (d.mine) {
        var e = mark(btn("sw-btn fd-edit", SAY.edit), "deck-edit");
        e.addEventListener("click", function () { editDeck(d); });
        head.appendChild(e);
      }
      return head;
    }

    search.addEventListener("input", function () { drawList(); });

    var self = {
      node: root,
      show: show,
      editDeck: editDeck,
      chosen: function () { return chosen; },
      view: function () { return view; },
      editor: function () { return editor; },
      reset: function (first) {
        seq += 1;
        chosen = null;
        editor = null;
        listCache = null;
        lastFile = null;
        lastDeckId = "";
        pasteBox.value = "";
        makeBtn.disabled = true;
        search.value = "";
        pEditor.textContent = "";
        view = "";
        syncChips();
        setPane("");
        if (first) { show(first); }
      }
    };
    setPane("");
    return self;
  }

  function deckMeta(d) {
    var parts = [SAY.cards(Number(d.card_count) || 0)];
    if (d.author) { parts.push(d.author); }
    var when = dateLabel(d.updated_at);
    if (when) { parts.push(when); }
    if (d.status && d.status !== "ready") { parts.push(SAY.draft); }
    return parts.join(" · ");
  }

  /* ═════════════════════════════════════════════════════════════════════
     THE PANEL — the library page's overlay, in the sheet's own chrome
     (`.sw-overlay` / `.sw-sheet` / `.sw-head`), so a deck is edited in the
     same frame whichever door the teacher came through.
     ═════════════════════════════════════════════════════════════════════ */

  var panel = null;
  function openPanel(label, content, onClose) {
    if (!panel) {
      var overlay = mark(el("div", "sw-overlay fd-overlay"), "panel");
      overlay.hidden = true;
      var sheet = el("div", "sw-sheet");
      sheet.setAttribute("role", "dialog");
      sheet.setAttribute("aria-modal", "true");
      sheet.tabIndex = -1;
      var head = el("div", "sw-head");
      var closeB = mark(btn("sw-btn", SAY.close), "panel-close");
      var step = el("div", "sw-step", "");
      var pad = el("span", "fd-head-pad");
      head.appendChild(closeB); head.appendChild(step); head.appendChild(pad);
      var body = el("div", "sw-body");
      sheet.appendChild(head); sheet.appendChild(body);
      overlay.appendChild(sheet);
      document.body.appendChild(overlay);
      panel = { overlay: overlay, sheet: sheet, step: step, body: body, close: closeB,
                onClose: null };
      var shut = function () {
        if (panel.overlay.hidden) { return; }
        panel.overlay.hidden = true;
        panel.body.textContent = "";
        var cb = panel.onClose;
        panel.onClose = null;
        if (cb) { cb(); }
      };
      panel.shut = shut;
      closeB.addEventListener("click", shut);
      overlay.addEventListener("click", function (e) { if (e.target === overlay) { shut(); } });
      document.addEventListener("keydown", function (e) {
        if (e.key === "Escape" && !panel.overlay.hidden) { shut(); }
      });
    }
    panel.step.textContent = label || "";
    panel.sheet.setAttribute("aria-label", label || "");
    panel.body.textContent = "";
    panel.body.appendChild(content);
    panel.onClose = onClose || null;
    panel.overlay.hidden = false;
    panel.sheet.scrollTop = 0;
    try { panel.sheet.focus({ preventScroll: true }); } catch (e) { /* old engine */ }
    return { close: function () { panel.shut(); } };
  }

  window.MRBDeckApi = api;
  window.MRBDeckEditor = { create: createEditor, SAY: SAY };
  window.MRBDeckSource = { create: createSource, deckMeta: deckMeta, SAY: SAY };
  window.MRBDeckPanel = { open: openPanel };
  window.MRBDecks = { SAY: SAY, draw: draw, dateLabel: dateLabel, deckMeta: deckMeta,
                      MAX_CARDS: MAX_CARDS };
})();
