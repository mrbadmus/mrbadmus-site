/* ═══════════════════════════════════════════════════════════════════════
   wrapped.js — MrBadmus Wrapped. A full-screen vertical story of a half
   term, for a pupil, and the same player for a teacher's class.

   Surface:  window.MRBWrapped.open()   .close()

   Plain JS, no framework, no CDN. Motion is CSS keyframes plus a
   requestAnimationFrame clock; reduced motion keeps every card and drops
   the animation, and numbers land at their value.

   ── WHY IT IS AN OVERLAY ON <body> ────────────────────────────────────
   student-runtime.js draw() empties the whole mount host on every setState.
   Anything that must survive that (a running story) lives OUTSIDE the host,
   exactly as shared/set-work.js does. Only the trigger button is inside the
   host, and it is re-placed after every redraw.

   ── WHAT COMES FROM THE DATABASE ──────────────────────────────────────
   wrapped_status / wrapped_pupil / wrapped_class (docs/wrapped/PLAN.md §1).
   The database sends only cards that have good news; this file renders
   exactly the cards it is sent, in order, and never invents one. If the
   functions are missing (production before the migration) or error, this
   file does nothing at all.

   There is NO demo data on the live site. `open({data})` and `dev()` work on
   localhost only, for the test harness.
   ═══════════════════════════════════════════════════════════════════════ */
(function (win) {
  "use strict";
  var doc = win.document;
  if (!doc || win.MRBWrapped) { return; }

  var script = doc.currentScript;
  var ROLE = (script && script.getAttribute("data-wrapped")) === "teacher" ? "teacher" : "pupil";
  var DUR = 7000;          /* ms a card stays */
  var HOLD_MS = 220;       /* press this long to pause */
  var MARK_URL = "/shared/brand/mrbadmus-chevron.svg";
  var IS_LOCAL = /^(localhost|127\.0\.0\.1)$/.test(win.location.hostname);

  /* ── The palette. [field, ink, accent for big type, shape] ─────────────
     Light fields are the subject colours with ink on them; dark fields are
     deep tints of the same hue with the vivid colour as the type. */
  var PAL = {
    opener:      { l: ["#E4572E", "#1A1714", "#1A1714", "#FBF3E6"], d: ["#2E160E", "#FBF3E6", "#F2946E", "#E4572E"] },
    flashcards:  { l: ["#6BCB77", "#1A1714", "#1A1714", "#FBF3E6"], d: ["#10281A", "#FBF3E6", "#6BCB77", "#6BCB77"] },
    homework:    { l: ["#FFD93D", "#1A1714", "#1A1714", "#E4572E"], d: ["#2B2208", "#FBF3E6", "#FFD93D", "#FFD93D"] },
    best_topic:  { l: ["#FFD2E6", "#1A1714", "#A93411", "#E4572E"], d: ["#331A28", "#FBF3E6", "#FFD2E6", "#FFD2E6"] },
    streak:      { l: ["#4ECDC4", "#1A1714", "#1A1714", "#FBF3E6"], d: ["#0C2A28", "#FBF3E6", "#4ECDC4", "#4ECDC4"] },
    top_band:    { l: ["#1A1714", "#FBF3E6", "#FFD93D", "#E4572E"], d: ["#15110C", "#FBF3E6", "#FFD93D", "#E4572E"] },
    forward:     { l: ["#FBF3E6", "#1A1714", "#A93411", "#E4572E"], d: ["#1E1913", "#FBF3E6", "#F2946E", "#E4572E"] },
    summary:     { l: ["#FBF3E6", "#1A1714", "#A93411", "#E4572E"], d: ["#15110C", "#FBF3E6", "#F2946E", "#E4572E"] }
  };
  PAL.most_secured = PAL.flashcards;
  PAL.revisit = PAL.streak;
  PAL.top3 = PAL.homework;
  PAL.zero = PAL.opener;

  var STAR = "M12 2l2.9 6.6 7.1.6-5.4 4.7 1.7 7-6.3-3.8-6.3 3.8 1.7-7L2 9.2l7.1-.6z";
  var ICON = {
    close: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round"><path d="M5 5l14 14M19 5L5 19"/></svg>',
    share: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M12 15V3M7 8l5-5 5 5M5 13v6a2 2 0 002 2h10a2 2 0 002-2v-6"/></svg>',
    save: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3v12M7 10l5 5 5-5M5 20h14"/></svg>',
    star: '<svg viewBox="0 0 24 24"><path d="' + STAR + '"/></svg>',
    spark: '<svg viewBox="0 0 24 24"><path d="M12 1l2.4 7.6L22 11l-7.6 2.4L12 21l-2.4-7.6L2 11l7.6-2.4zM19 15l1 3 3 1-3 1-1 3-1-3-3-1 3-1z"/></svg>'
  };

  var S = {
    sb: null, classId: "", preview: false, status: null, shown: false, bootTried: false,
    ov: null, stage: null, cardsHost: null, barsHost: null, cards: [], idx: 0, elapsed: 0,
    held: false, userPause: false, tabHidden: false, done: false, raf: 0, last: 0,
    tok: 0, holdTimer: 0, opener: null, prevFocus: null, locked: null, data: null,
    rm: false, busy: false
  };

  /* ── tiny helpers ─────────────────────────────────────────────────────── */
  function h(tag, cls, text) {
    var e = doc.createElement(tag);
    if (cls) { e.className = cls; }
    if (text != null) { e.textContent = text; }
    return e;
  }
  function svg(markup) { var s = h("span"); s.innerHTML = markup; return s.firstChild; }
  function pl(n, one, many) { return n === 1 ? one : many; }
  function isDark() { return doc.documentElement.getAttribute("data-theme") === "dark"; }
  function debug(m) { try { if (win.console && console.debug) { console.debug("[wrapped]", m); } } catch (e) { /* none */ } }
  function qs() {
    try { return new win.URLSearchParams(win.location.search); } catch (e) { return { get: function () { return null; } }; }
  }
  function clamp(n, a, b) { return Math.max(a, Math.min(b, n)); }

  /* ═════════════════════════════════════════════════════════════════════
     1. READS
     ═════════════════════════════════════════════════════════════════════ */
  function client() {
    try {
      var g = ROLE === "teacher" ? win.MrBadmusTeacherGuard : win.MrBadmusStudentGuard;
      if (!g || !win.supabase || !win.supabase.createClient || typeof g.getClient !== "function") { return null; }
      return g.getClient() || null;
    } catch (e) { return null; }
  }
  function rpc(name) {
    var args = { p_class_id: S.classId, p_preview: S.preview };
    return Promise.resolve(S.sb.rpc(name, args)).then(function (r) {
      if (!r || r.error) { throw new Error((r && r.error && (r.error.code || r.error.message)) || "rpc"); }
      return r.data;
    });
  }

  /* ═════════════════════════════════════════════════════════════════════
     2. THE TRIGGER BUTTON
     ═════════════════════════════════════════════════════════════════════ */
  function buttonText() { return ROLE === "teacher" ? "Class Wrapped" : "Your half-term Wrapped"; }

  function place() {
    if (!S.shown) { return; }
    var host = doc.getElementById(ROLE === "teacher" ? "mrb-teacher" : "mrb-student");
    if (!host) { return; }
    var anchor, mode;
    if (ROLE === "teacher") {
      anchor = host.querySelector('[data-dc-tpl="213"]'); mode = "row";
    } else {
      anchor = host.querySelector('[data-dc-tpl="40"]');
      if (!anchor) { var h1 = host.querySelector("main h1"); anchor = h1 && h1.parentNode; }
      mode = "hero";
    }
    var have = doc.querySelector('[data-mrb-added="wrapped-open"]');
    if (have && (!anchor || anchor.contains(have)) && doc.body.contains(have)) { return; }
    if (have && have.parentNode) { have.parentNode.removeChild(have); }
    var b = h("button", "wr-open" + (mode === "row" ? " wr-open-row" : "") + (anchor ? "" : " wr-open-float"));
    b.type = "button";
    b.setAttribute("data-mrb-added", "wrapped-open");
    b.appendChild(svg(ICON.spark));
    b.appendChild(doc.createTextNode(buttonText()));
    b.addEventListener("click", function (ev) { ev.preventDefault(); S.opener = b; open(); });
    (anchor || doc.body).appendChild(b);
  }

  function watch() {
    place();
    if (ROLE === "pupil") {
      win.__MRB_AFTER_DRAW__ = win.__MRB_AFTER_DRAW__ || [];
      win.__MRB_AFTER_DRAW__.push(function () { place(); });
    } else if (win.MutationObserver) {
      var host = doc.getElementById("mrb-teacher") || doc.body, pending = false;
      new win.MutationObserver(function () {
        if (pending) { return; }
        pending = true;
        (win.requestAnimationFrame || win.setTimeout)(function () { pending = false; place(); }, 0);
      }).observe(host, { childList: true, subtree: true });
    }
  }

  function boot(tries) {
    if (S.bootTried) { return; }
    tries = tries || 0;
    S.sb = client();
    var q = qs();
    S.classId = q.get("class") || "";
    S.preview = q.get("wrapped") === "preview";
    if (!S.classId) { S.bootTried = true; return; }
    /* The SDK arrives from the page's own loader; give it a few seconds. A
       fixture or a signed-out page never gets one, and this stays silent. */
    if (!S.sb) { if (tries < 8) { win.setTimeout(function () { boot(tries + 1); }, 1500); } return; }
    S.bootTried = true;
    rpc("wrapped_status").then(function (st) {
      S.status = st || {};
      var ok = st && st.open && (ROLE === "teacher" ? st.role === "teacher"
        : (st.role === "pupil" && (st.has_activity || st.show_zero)));
      if (!ok) { return; }
      S.shown = true;
      watch();
      if (S.preview) { open(); }
    }).catch(function (e) { debug("status unavailable: " + e.message); });
  }

  function whenIdle(fn) {
    function go() {
      if (win.requestIdleCallback) { win.requestIdleCallback(fn, { timeout: 4000 }); } else { win.setTimeout(fn, 1500); }
    }
    if (doc.readyState === "complete") { win.setTimeout(go, 600); } else { win.addEventListener("load", function () { win.setTimeout(go, 600); }); }
  }

  /* ═════════════════════════════════════════════════════════════════════
     3. CARDS — each returns an element; `data-count` numbers count up
     ═════════════════════════════════════════════════════════════════════ */
  function numEl(n) {
    var e = h("span", "wr-num wr-d" + Math.min(4, String(n).length), String(n));
    e.setAttribute("data-count", String(n));
    return e;
  }
  function wordsEl(tag, cls, text) {
    var e = h(tag, cls), words = String(text).split(/\s+/), i, w;
    for (i = 0; i < words.length; i++) {
      w = h("span", "wr-w", words[i]); w.style.setProperty("--i", i); e.appendChild(w);
    }
    return e;
  }
  function artEl(cls, n, tag) {
    var a = h("div", "wr-art " + cls), i;
    for (i = 0; i < n; i++) { var c = h(tag || "i"); c.style.setProperty("--i", i); a.appendChild(c); }
    return a;
  }
  function card(kind, extraCls) {
    var c = h("section", "wr-card" + (extraCls ? " " + extraCls : ""));
    c.setAttribute("data-kind", kind);
    return c;
  }

  function displayName(nm) {
    nm = nm || {};
    return { first: nm.first || "", username: nm.username || "" };
  }

  var BUILD = {
    opener: function (c, P) {
      var el = card("opener"), n = displayName(P.name), big = h("h2", "wr-big wr-name");
      el.appendChild(h("div", "wr-art wr-ghost")).appendChild(h("img")).src = MARK_URL;
      var br = h("div", "wr-brand"), im = h("img"); im.src = MARK_URL; im.alt = "";
      br.appendChild(im); br.appendChild(h("span", null, "MrBadmus")); el.appendChild(br);
      var i, word = h("span", "wr-fit-word");
      for (i = 0; i < n.first.length; i++) {
        var l = h("span", "wr-ltr", n.first.charAt(i)); l.style.setProperty("--i", i); word.appendChild(l);
      }
      big.appendChild(word);
      if (n.username) { big.appendChild(h("span", "wr-un", "(" + n.username + ")")); }
      el.appendChild(big);
      big.setAttribute("data-fit", "1");
      el.appendChild(h("p", "wr-line", "your half term on MrBadmus."));
      return el;
    },
    flashcards: function (c) {
      var el = card("flashcards");
      var dk = artEl("wr-deck", 6);
      dk.lastChild.innerHTML = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 12.8l5 5L20 6.5"/></svg>';
      el.appendChild(dk);
      el.appendChild(numEl(c.secured));
      el.appendChild(h("p", "wr-sub", pl(c.secured, "flashcard secured", "flashcards secured")));
      if (c.decks_finished > 0) { el.appendChild(h("p", "wr-line", "and " + c.decks_finished + " " + pl(c.decks_finished, "deck", "decks") + " finished")); }
      return el;
    },
    homework: function (c) {
      var el = card("homework"), a = artEl("wr-sheets", 5), b = h("div", "wr-art wr-burst"), i;
      el.appendChild(a);
      if (c.stars > 0) {
        for (i = 0; i < 9; i++) {
          var s = svg(ICON.star), ang = -Math.PI * (0.1 + 0.8 * (i / 8)), r = 24 + (i % 3) * 8;
          s.style.setProperty("--i", i);
          s.style.setProperty("--dx", "calc(var(--wr-u) * " + Math.round(Math.cos(ang) * r) + ")");
          s.style.setProperty("--dy", "calc(var(--wr-u) * " + Math.round(Math.sin(ang) * r * 1.1) + ")");
          s.style.setProperty("--r", (i * 47) % 160 - 80 + "deg");
          b.appendChild(s);
        }
        el.appendChild(b);
      }
      el.appendChild(numEl(c.handed_in));
      el.appendChild(h("p", "wr-sub", pl(c.handed_in, "piece of homework handed in", "pieces of homework handed in")));
      if (c.stars > 0) {
        var ln = h("p", "wr-line"); ln.appendChild(svg(ICON.star));
        ln.appendChild(doc.createTextNode(c.stars + " " + pl(c.stars, "star", "stars") + " earned"));
        el.appendChild(ln);
      }
      return el;
    },
    best_topic: function (c) {
      var el = card("best_topic");
      el.appendChild(h("div", "wr-art wr-ghost")).appendChild(h("img")).src = MARK_URL;
      el.appendChild(h("p", "wr-lab", "Best topic"));
      var ph = wordsEl("h2", "wr-phrase", c.topic); ph.setAttribute("data-fit", "1"); el.appendChild(ph);
      el.appendChild(h("span", "wr-sweep"));
      el.appendChild(h("p", "wr-line", c.source === "deck" ? "Every card secured" : c.pct + "% on your homework"));
      return el;
    },
    streak: function (c) {
      var el = card("streak"), a = h("div", "wr-art wr-steps"), n = Math.min(12, c.weeks), i;
      for (i = 0; i < n; i++) { var s = h("i", i === n - 1 && c.current ? "wr-now" : ""); s.style.setProperty("--i", i); a.appendChild(s); }
      el.appendChild(a);
      el.appendChild(numEl(c.weeks));
      el.appendChild(h("p", "wr-sub", pl(c.weeks, "week in a row", "weeks in a row")));
      if (c.current) { el.appendChild(h("p", "wr-line", "and still going")); }
      return el;
    },
    top_band: function (c) {
      var el = card("top_band"), big, line;
      el.appendChild(artEl("wr-rings", 4));
      if (c.scope === "year") {
        big = ["Top", c.band + "%"]; line = "of Year " + c.year_group + " on " + c.topic;
      } else if (c.scope === "class") {
        big = ["Top", String(c.top)]; line = "in " + c.class_name + " on " + c.topic;
      } else {
        big = ["Every", "card"]; line = "You secured every " + c.topic + " card";
      }
      var w = h("div", "wr-slam");
      w.appendChild(h("p", "wr-top", big[0]));
      var b = h("h2", "wr-big", big[1]); b.style.fontSize = "calc(var(--wr-u) * " + (big[1].length > 3 ? 26 : 40) + ")";
      b.style.overflow = "visible";
      w.appendChild(b); el.appendChild(w);
      var ln = h("p", "wr-line", line); ln.setAttribute("data-fit-line", "1"); el.appendChild(ln);
      return el;
    },
    forward: function (c) {
      var el = card("forward"), cards = c.metric !== "homework";
      var rise = h("div", "wr-art wr-rise");
      rise.innerHTML = '<svg viewBox="0 0 100 60"><path pathLength="1" d="M2 56 C 30 54, 46 46, 62 28 S 86 6, 96 4"/></svg>';
      el.appendChild(rise);
      el.appendChild(h("p", "wr-pre", cards ? "Keep this pace and you'd secure" : "Keep this pace and you'd hand in"));
      var n = numEl(c.projected); n.setAttribute("data-from", String(c.now)); n.className = n.className.replace(/wr-d\d/, "wr-d" + Math.min(4, String(c.projected).length));
      el.appendChild(n);
      el.appendChild(h("p", "wr-sub", cards ? "cards by Christmas" : "pieces of homework by Christmas"));
      var tr = h("div", "wr-track"); tr.style.setProperty("--p", clamp(c.now / Math.max(1, c.projected), 0.04, 1) * 100 + "%");
      tr.appendChild(h("u")); tr.appendChild(h("b")); el.appendChild(tr);
      return el;
    },
    zero: function (c, P) {
      var el = card("zero");
      el.appendChild(h("div", "wr-art wr-ghost")).appendChild(h("img")).src = MARK_URL;
      var big = h("h2", "wr-big", "Your Wrapped starts now"); big.setAttribute("data-fit", "1"); el.appendChild(big);
      el.appendChild(h("p", "wr-line", "Hand in homework and secure flashcards. December's Wrapped will show it off."));
      var acts = h("div", "wr-acts"), b = h("button", "wr-btn", "Back to my class");
      b.type = "button"; b.addEventListener("click", function () { close(true); });
      acts.appendChild(b); el.appendChild(acts);
      return el;
    },
    /* teacher */
    t_opener: function (c, P) {
      var el = card("opener");
      var br = h("div", "wr-brand"), im = h("img"); im.src = MARK_URL; im.alt = "";
      br.appendChild(im); br.appendChild(h("span", "", "MrBadmus")); el.appendChild(br);
      el.appendChild(h("div", "wr-art wr-ghost")).appendChild(h("img")).src = MARK_URL;
      var big = h("h2", "wr-big", ((P.class && P.class.name) || "") + "'s half term"); big.setAttribute("data-fit", "1"); el.appendChild(big);
      el.appendChild(h("p", "wr-line", c.active + " of " + c.pupils + " pupils took part"));
      return el;
    },
    t_homework: function (c) {
      var el = BUILD.homework({ handed_in: c.handed_in, stars: 0 }); return el;
    },
    t_flashcards: function (c) {
      return BUILD.flashcards({ secured: c.secured, decks_finished: c.decks });
    },
    most_secured: function (c) {
      var el = card("most_secured");
      el.appendChild(h("div", "wr-art wr-ghost")).appendChild(h("img")).src = MARK_URL;
      el.appendChild(h("p", "wr-lab", "Most secured"));
      var ph = wordsEl("h2", "wr-phrase", c.topic); ph.setAttribute("data-fit", "1"); el.appendChild(ph);
      el.appendChild(h("span", "wr-sweep"));
      el.appendChild(h("p", "wr-line", c.pct + "% of cards secured"));
      return el;
    },
    revisit: function (c) {
      var el = card("revisit");
      el.appendChild(h("div", "wr-art wr-ghost")).appendChild(h("img")).src = MARK_URL;
      el.appendChild(h("p", "wr-lab", "Next to revisit"));
      var ph = wordsEl("h2", "wr-phrase", c.topic); ph.setAttribute("data-fit", "1"); el.appendChild(ph);
      el.appendChild(h("span", "wr-sweep"));
      el.appendChild(h("p", "wr-line", c.pct + "% so far"));
      return el;
    },
    top3: function (c) {
      var el = card("top3"), ul = h("ul", "wr-podium"), i;
      el.appendChild(h("div", "wr-art wr-ghost")).appendChild(h("img")).src = MARK_URL;
      el.appendChild(h("p", "wr-lab", "Top three"));
      for (i = 0; i < Math.min(3, c.pupils.length); i++) {
        var p = c.pupils[i], li = h("li");
        li.style.setProperty("--i", i);
        var left = h("span", "wr-pn"); left.appendChild(h("span", "wr-rk", String(i + 1))); left.appendChild(doc.createTextNode(p.first_name));
        var right = h("span", "wr-ps"); right.appendChild(svg(ICON.star)); right.appendChild(h("span", "", String(p.stars)));
        li.appendChild(left); li.appendChild(right); ul.appendChild(li);
      }
      el.appendChild(ul);
      return el;
    }
  };

  /* The summary card: also the shape of the share image. */
  function summaryStats(cards) {
    var by = {}, out = [], i;
    for (i = 0; i < cards.length; i++) { by[cards[i].kind] = cards[i]; }
    if (by.flashcards) { out.push({ pal: "flashcards", num: by.flashcards.secured, label: pl(by.flashcards.secured, "flashcard secured", "flashcards secured") }); }
    if (by.homework) { out.push({ pal: "homework", num: by.homework.handed_in, label: pl(by.homework.handed_in, "piece of homework", "pieces of homework") }); }
    if (by.homework && by.homework.stars > 0) { out.push({ pal: "opener", num: by.homework.stars, label: pl(by.homework.stars, "star earned", "stars earned") }); }
    if (by.streak) { out.push({ pal: "streak", num: by.streak.weeks, label: pl(by.streak.weeks, "week in a row", "weeks in a row") }); }
    var tb = by.top_band;
    if (tb && tb.scope === "year") { out.push({ pal: "top_band", phrase: "Top " + tb.band + "%", label: "of Year " + tb.year_group + " on " + tb.topic }); }
    else if (tb && tb.scope === "personal") { out.push({ pal: "top_band", phrase: "Every card", label: "secured on " + tb.topic }); }
    if (by.best_topic) { out.push({ pal: "best_topic", phrase: by.best_topic.topic, label: "Best topic" }); }
    return out.slice(0, 4);
  }
  function nameText(P) { var n = displayName(P.name); return n.username ? n.first + " (" + n.username + ")" : n.first; }

  function tileColors(pal) {
    var p = PAL[pal][isDark() ? "d" : "l"];
    return { bg: p[0], fg: p[1], hi: p[2] };
  }

  BUILD.summary = function (c, P) {
    var el = card("summary", "wr-sum"), stats = summaryStats(P.cards);
    var hd = h("div", "wr-sh"), im = h("img"); im.src = MARK_URL; im.alt = "";
    hd.appendChild(im); hd.appendChild(h("span", "", "MrBadmus")); el.appendChild(hd);
    var nm = h("h2", "wr-sname", nameText(P)); nm.setAttribute("data-fit", "1"); el.appendChild(nm);
    var grid = h("div", "wr-tiles" + (stats.length < 4 ? " wr-col" : "")), i;
    for (i = 0; i < stats.length; i++) {
      var s = stats[i], col = tileColors(s.pal), t = h("div", "wr-tile");
      /* Tiles keep their own colours, light or dark: the field behind them is the page's. */
      if (isDark()) { col = { bg: col.bg, fg: col.fg, hi: col.hi }; }
      t.style.setProperty("--t-bg", col.bg); t.style.setProperty("--t-fg", col.fg); t.style.setProperty("--t-hi", col.hi);
      t.style.setProperty("--i", i);
      if (s.phrase) {
        var ph = h("div", "wr-tp", s.phrase); ph.setAttribute("data-fit-tile", "1"); t.appendChild(ph);
      } else {
        var tn = h("div", "wr-tn", String(s.num)); tn.setAttribute("data-count", String(s.num)); t.appendChild(tn);
      }
      t.appendChild(h("div", "wr-tl", s.label));
      grid.appendChild(t);
    }
    el.appendChild(grid);
    el.appendChild(h("p", "wr-url", "mrbadmus.com"));
    var acts = h("div", "wr-acts"), canShare = canShareFiles();
    if (canShare) {
      var sb = h("button", "wr-btn"); sb.type = "button"; sb.appendChild(svg(ICON.share)); sb.appendChild(doc.createTextNode("Share"));
      sb.addEventListener("click", function () { doShare("share", P, sb); });
      acts.appendChild(sb);
    }
    var db = h("button", "wr-btn" + (canShare ? " wr-ghostbtn" : "")); db.type = "button"; db.appendChild(svg(ICON.save)); db.appendChild(doc.createTextNode("Save image"));
    db.addEventListener("click", function () { doShare("save", P, db); });
    acts.appendChild(db);
    el.appendChild(acts);
    el.appendChild(h("p", "wr-note"));
    return el;
  };

  /* Turn the database's card list into the story's card list. */
  function compose(P) {
    var out = [], cards = P.cards || [], i, c;
    if (ROLE === "teacher") {
      for (i = 0; i < cards.length; i++) {
        c = cards[i];
        var key = { opener: "t_opener", homework: "t_homework", flashcards: "t_flashcards" }[c.kind] || c.kind;
        if (BUILD[key]) { out.push({ kind: c.kind, c: c, build: BUILD[key] }); }
      }
      return out;
    }
    if (P.zero) { return [{ kind: "zero", c: {}, build: BUILD.zero, end: true }]; }
    for (i = 0; i < cards.length; i++) {
      c = cards[i];
      if (BUILD[c.kind]) { out.push({ kind: c.kind, c: c, build: BUILD[c.kind] }); }
    }
    out.push({ kind: "summary", c: {}, build: BUILD.summary, end: true });
    return out;
  }

  /* ═════════════════════════════════════════════════════════════════════
     4. THE PLAYER
     ═════════════════════════════════════════════════════════════════════ */
  function layout() {
    if (!S.ov) { return; }
    var vw = win.innerWidth, vh = win.innerHeight, w, hh;
    if (vw / vh <= 9 / 16 + 0.001) { w = vw; hh = vh; S.ov.className = S.ov.className.replace(/\s*wr-wide/, ""); }
    else {
      hh = Math.min(vh - 24, 960); w = Math.round(hh * 9 / 16);
      if (!/wr-wide/.test(S.ov.className)) { S.ov.className += " wr-wide"; }
    }
    S.stage.style.width = w + "px"; S.stage.style.height = hh + "px";
    S.ov.style.setProperty("--wr-u", (w / 100) + "px");
    fitAll();
  }

  function fitBox(el, maxPx, minPx, box) {
    var px = maxPx;
    el.style.fontSize = px + "px";
    while (px > minPx && (el.scrollWidth > el.clientWidth + 1 || el.scrollHeight > (box || el.clientHeight) + 1)) {
      px -= 2; el.style.fontSize = px + "px";
    }
  }
  function fitAll() {
    var cur = S.cardsHost && S.cardsHost.firstChild;
    if (!cur) { return; }
    var u = (S.stage.clientWidth || 360) / 100, nodes, i;
    nodes = cur.querySelectorAll("[data-fit]");
    for (i = 0; i < nodes.length; i++) {
      var e = nodes[i], isName = e.className.indexOf("wr-name") > -1, isSum = e.className.indexOf("wr-sname") > -1;
      e.style.maxHeight = ""; e.style.fontSize = "";
      var maxH = (isSum ? 15 : isName ? 50 : 56) * u;
      e.style.maxHeight = maxH + "px"; e.style.overflow = "hidden";
      fitBox(e, (isName ? 62 : isSum ? 12 : 17) * u, (isSum ? 6 : 6) * u, maxH);
    }
    nodes = cur.querySelectorAll("[data-fit-line]");
    for (i = 0; i < nodes.length; i++) { nodes[i].style.maxWidth = "100%"; }
    nodes = cur.querySelectorAll("[data-fit-tile]");
    for (i = 0; i < nodes.length; i++) {
      nodes[i].style.fontSize = "";
      nodes[i].style.maxHeight = (nodes[i].parentNode.clientHeight * 0.55) + "px";
      fitBox(nodes[i], 8.4 * u, 4.2 * u, nodes[i].clientHeight || 0);
    }
  }

  function countUps(el, tok) {
    var nodes = el.querySelectorAll("[data-count]"), i;
    for (i = 0; i < nodes.length; i++) { (function (n) {
      var to = parseInt(n.getAttribute("data-count"), 10) || 0;
      var from = parseInt(n.getAttribute("data-from") || "0", 10) || 0;
      if (S.rm || to === from) { n.textContent = String(to); return; }
      n.textContent = String(from);
      var t0 = null, dur = clamp(700 + (to - from) * 6, 900, 1800), delay = 250;
      function step(t) {
        if (tok !== S.tok) { return; }
        if (t0 === null) { t0 = t; }
        var k = clamp((t - t0 - delay) / dur, 0, 1), e = 1 - Math.pow(1 - k, 3);
        n.textContent = String(Math.round(from + (to - from) * e));
        if (k < 1) { win.requestAnimationFrame(step); } else { n.textContent = String(to); }
      }
      win.requestAnimationFrame(step);
    })(nodes[i]); }
  }

  function paint(kind) {
    var p = PAL[kind] || PAL.opener, a = p[isDark() ? "d" : "l"], st = S.stage.style;
    st.setProperty("--wr-bg", a[0]); st.setProperty("--wr-fg", a[1]); st.setProperty("--wr-hi", a[2]); st.setProperty("--wr-sh", a[3]);
  }

  function show(i) {
    var item = S.cards[i];
    if (!item) { return; }
    S.idx = i; S.elapsed = 0; S.done = false; S.tok++;
    paint(item.kind);
    var el = item.build(item.c, S.data);
    S.cardsHost.innerHTML = "";
    S.cardsHost.appendChild(el);
    var bars = S.barsHost.children, k;
    for (k = 0; k < bars.length; k++) { bars[k].firstChild.style.transform = "scaleX(" + (k < i ? 1 : 0) + ")"; }
    S.stage.setAttribute("aria-label", "Card " + (i + 1) + " of " + S.cards.length);
    fitAll();
    countUps(el, S.tok);
    var focusMe = el.querySelector("button");
    if (focusMe && item.end) { /* leave focus on the close control; Tab reaches the buttons */ }
  }
  function next() { if (S.idx < S.cards.length - 1) { show(S.idx + 1); } }
  function prev() { if (S.idx > 0) { show(S.idx - 1); } else { show(0); } }

  function tick(t) {
    S.raf = win.requestAnimationFrame(tick);
    var dt = S.last ? t - S.last : 0; S.last = t;
    if (S.held || S.userPause || S.tabHidden || S.done || S.busy) { return; }
    S.elapsed += Math.min(dt, 100);
    var p = clamp(S.elapsed / DUR, 0, 1), bar = S.barsHost.children[S.idx];
    if (bar) { bar.firstChild.style.transform = "scaleX(" + p + ")"; }
    if (p >= 1) { if (S.idx < S.cards.length - 1) { show(S.idx + 1); } else { S.done = true; } }
  }

  /* press-and-hold pauses; a quick tap navigates */
  function onDown(ev) {
    if (ev.target.closest && ev.target.closest("button, a")) { return; }
    if (ev.button != null && ev.button > 0) { return; }
    S.downAt = Date.now(); S.downX = ev.clientX; S.heldFlag = false;
    win.clearTimeout(S.holdTimer);
    S.holdTimer = win.setTimeout(function () { S.held = true; S.heldFlag = true; }, HOLD_MS);
    S.tracking = true;
  }
  function onUp(ev) {
    if (!S.tracking) { return; }
    S.tracking = false;
    win.clearTimeout(S.holdTimer);
    var wasHeld = S.heldFlag;
    S.held = false;
    if (wasHeld) { return; }
    var r = S.stage.getBoundingClientRect(), x = (ev.clientX - r.left) / r.width;
    if (x < 0.32) { prev(); } else { next(); }
  }
  function onCancel() { S.tracking = false; win.clearTimeout(S.holdTimer); S.held = false; }

  function onKey(ev) {
    if (!S.ov) { return; }
    var k = ev.key;
    if (k === "Escape") { ev.preventDefault(); close(); return; }
    if (k === "ArrowRight") { ev.preventDefault(); next(); return; }
    if (k === "ArrowLeft") { ev.preventDefault(); prev(); return; }
    if ((k === " " || k === "Spacebar") && !(ev.target.closest && ev.target.closest("button"))) { ev.preventDefault(); S.userPause = !S.userPause; return; }
    if (k === "Tab") {
      var f = S.ov.querySelectorAll("button:not([disabled])");
      if (!f.length) { return; }
      var first = f[0], last = f[f.length - 1];
      if (!S.ov.contains(doc.activeElement)) { ev.preventDefault(); first.focus(); }
      else if (ev.shiftKey && doc.activeElement === first) { ev.preventDefault(); last.focus(); }
      else if (!ev.shiftKey && doc.activeElement === last) { ev.preventDefault(); first.focus(); }
    }
  }
  function onVis() { S.tabHidden = !!doc.hidden; }

  function lockScroll() {
    var de = doc.documentElement, b = doc.body;
    S.locked = { h: de.style.overflow, b: b.style.overflow };
    de.style.overflow = "hidden"; b.style.overflow = "hidden";
  }
  function unlockScroll() {
    if (!S.locked) { return; }
    doc.documentElement.style.overflow = S.locked.h; doc.body.style.overflow = S.locked.b; S.locked = null;
  }

  function buildShell() {
    var ov = h("div", "wr-ov"), stage = h("div", "wr-stage");
    ov.setAttribute("role", "dialog"); ov.setAttribute("aria-modal", "true");
    ov.setAttribute("aria-label", ROLE === "teacher" ? "Class Wrapped" : "Your half-term Wrapped");
    S.rm = !!(win.matchMedia && win.matchMedia("(prefers-reduced-motion: reduce)").matches);
    if (S.rm) { ov.className += " wr-rm"; }
    var bars = h("div", "wr-bars"), x = h("button", "wr-x"), host = h("div", "wr-cards");
    bars.setAttribute("aria-hidden", "true");
    x.type = "button"; x.setAttribute("aria-label", "Close"); x.innerHTML = ICON.close;
    x.addEventListener("click", function (ev) { ev.stopPropagation(); close(); });
    host.setAttribute("aria-live", "polite");
    stage.appendChild(host); stage.appendChild(bars); stage.appendChild(x);
    ov.appendChild(stage);
    stage.addEventListener("pointerdown", onDown);
    stage.addEventListener("pointerup", onUp);
    stage.addEventListener("pointercancel", onCancel);
    stage.addEventListener("pointerleave", function () { if (S.tracking) { onCancel(); } });
    stage.addEventListener("contextmenu", function (e) { e.preventDefault(); });
    ov.addEventListener("pointerdown", function (e) { if (e.target === ov) { e.preventDefault(); } });
    ov.addEventListener("click", function (e) { if (e.target === ov) { close(); } });
    S.ov = ov; S.stage = stage; S.cardsHost = host; S.barsHost = bars; S.closeBtn = x;
  }

  function loading() {
    var c = card("loading", "wr-load");
    var im = h("img"); im.src = MARK_URL; im.alt = ""; c.appendChild(im);
    paint("opener");
    S.cardsHost.innerHTML = ""; S.cardsHost.appendChild(c);
  }

  function fontsReady() {
    if (!doc.fonts || !doc.fonts.load) { return Promise.resolve(); }
    var t = new Promise(function (r) { win.setTimeout(r, 1500); });
    return Promise.race([Promise.all([
      doc.fonts.load("800 40px 'Bricolage Grotesque'"), doc.fonts.load("600 40px 'Bricolage Grotesque'"),
      doc.fonts.load("500 40px 'DM Mono'"), doc.fonts.load("500 20px 'Instrument Sans'")
    ]), t]).catch(function () { /* fall back to whatever is loaded */ });
  }

  function start(P) {
    S.data = P; S.cards = compose(P);
    if (!S.cards.length) { close(); return; }
    S.barsHost.innerHTML = "";
    var i;
    for (i = 0; i < S.cards.length; i++) { var s = h("i"); s.appendChild(h("b")); S.barsHost.appendChild(s); }
    S.last = 0;
    show(0);
    if (!S.raf) { S.raf = win.requestAnimationFrame(tick); }
  }

  function open(opts) {
    if (S.ov) { return; }
    opts = opts || {};
    S.prevFocus = doc.activeElement;
    buildShell();
    doc.body.appendChild(S.ov);
    lockScroll();
    layout(); loading();
    win.addEventListener("resize", layout);
    doc.addEventListener("keydown", onKey, true);
    doc.addEventListener("visibilitychange", onVis);
    S.tabHidden = !!doc.hidden;
    S.closeBtn.focus();
    var fetch;
    if (opts.data && IS_LOCAL) { fetch = Promise.resolve(opts.data); }
    else { fetch = rpc(ROLE === "teacher" ? "wrapped_class" : "wrapped_pupil"); }
    Promise.all([fetch, fontsReady()]).then(function (r) {
      if (!S.ov) { return; }
      var P = r[0] || {};
      if (P.state && P.state !== "open") { debug("state " + P.state); close(); return; }
      start(P);
    }).catch(function (e) { debug("story unavailable: " + e.message); close(); });
  }

  function close(toWork) {
    if (!S.ov) { return; }
    win.cancelAnimationFrame(S.raf); S.raf = 0; S.tok++;
    win.clearTimeout(S.holdTimer);
    win.removeEventListener("resize", layout);
    doc.removeEventListener("keydown", onKey, true);
    doc.removeEventListener("visibilitychange", onVis);
    if (S.ov.parentNode) { S.ov.parentNode.removeChild(S.ov); }
    S.ov = S.stage = S.cardsHost = S.barsHost = null;
    S.held = S.userPause = S.done = false;
    unlockScroll();
    var back = S.opener && doc.body.contains(S.opener) ? S.opener : doc.querySelector('[data-mrb-added="wrapped-open"]');
    if (toWork) {
      var w = doc.querySelector('[data-dc-tpl="55"]') || doc.querySelector("main");
      if (w && w.scrollIntoView) { w.scrollIntoView({ behavior: S.rm ? "auto" : "smooth", block: "start" }); }
      if (back && back.focus) { try { back.focus({ preventScroll: true }); } catch (e) { /* none */ } }
      return;
    }
    var f = back || S.prevFocus;
    if (f && f.focus) { try { f.focus({ preventScroll: true }); } catch (e) { /* none */ } }
  }

  /* ═════════════════════════════════════════════════════════════════════
     5. THE SHARE IMAGE — drawn straight to a 1080x1920 canvas
     ═════════════════════════════════════════════════════════════════════ */
  function canShareFiles() {
    try {
      if (!win.navigator.canShare || !win.navigator.share || !win.File) { return false; }
      return win.navigator.canShare({ files: [new win.File([""], "a.png", { type: "image/png" })] });
    } catch (e) { return false; }
  }

  function loadMark() {
    return new Promise(function (res) {
      var im = new win.Image();
      im.onload = function () { res(im); }; im.onerror = function () { res(null); };
      im.src = MARK_URL;
    });
  }

  function rrect(g, x, y, w, hh, r) {
    g.beginPath(); g.moveTo(x + r, y); g.arcTo(x + w, y, x + w, y + hh, r); g.arcTo(x + w, y + hh, x, y + hh, r);
    g.arcTo(x, y + hh, x, y, r); g.arcTo(x, y, x + w, y, r); g.closePath();
  }
  function fitFont(g, text, family, weight, maxW, startPx, minPx) {
    var px = startPx;
    for (; px > minPx; px -= 4) { g.font = weight + " " + px + "px " + family; if (g.measureText(text).width <= maxW) { break; } }
    g.font = weight + " " + px + "px " + family;
    return px;
  }
  function wrapLines(g, text, maxW) {
    var words = String(text).split(/\s+/), lines = [], cur = "", i;
    for (i = 0; i < words.length; i++) {
      var t = cur ? cur + " " + words[i] : words[i];
      if (g.measureText(t).width > maxW && cur) { lines.push(cur); cur = words[i]; } else { cur = t; }
    }
    if (cur) { lines.push(cur); }
    return lines;
  }

  var BRIC = "'Bricolage Grotesque', sans-serif", MONO = "'DM Mono', monospace", UI = "'Instrument Sans', sans-serif";

  function drawImageCanvas(P) {
    var faces = ["800 120px " + BRIC, "600 60px " + BRIC, "500 120px " + MONO, "600 40px " + UI];
    return Promise.all(faces.map(function (f) { return doc.fonts && doc.fonts.load ? doc.fonts.load(f) : null; }))
      .then(function () { return doc.fonts && doc.fonts.ready; })
      .then(loadMark)
      .then(function (mark) {
        var W = 1080, H = 1920, cv = doc.createElement("canvas"); cv.width = W; cv.height = H;
        var g = cv.getContext("2d"), dark = isDark(), sp = PAL.summary[dark ? "d" : "l"];
        var ink = dark ? "#FBF3E6" : "#1A1714";
        g.fillStyle = sp[0]; g.fillRect(0, 0, W, H);
        /* a big faded block of the field's own colour behind the name */
        var pad = 84, y = 150;
        if (mark) { g.drawImage(mark, pad, y - 52, 84, 84); }
        g.fillStyle = ink; g.textBaseline = "alphabetic";
        g.font = "600 76px " + BRIC; g.fillText("MrBadmus", pad + 84 + 22, y + 22);
        /* name */
        var name = nameText(P);
        g.fillStyle = ink;
        var px = fitFont(g, name, BRIC, 800, W - pad * 2, 230, 90);
        g.fillText(name, pad, 470);
        g.font = "600 56px " + BRIC; g.fillText("My half term, wrapped.", pad, 470 + 40 + 56);
        /* tiles */
        var stats = summaryStats(P.cards), n = stats.length, top = 700, bottom = 1700, gap = 28, i;
        var cols = n === 4 ? 2 : 1, rows = Math.ceil(n / cols);
        var tw = (W - pad * 2 - gap * (cols - 1)) / cols, th = Math.min(n === 4 ? 460 : 340, (bottom - top - gap * (rows - 1)) / rows);
        for (i = 0; i < n; i++) {
          var s = stats[i], col = tileColors(s.pal);
          var cx = pad + (i % cols) * (tw + gap), cy = top + Math.floor(i / cols) * (th + gap);
          g.fillStyle = col.bg; rrect(g, cx, cy, tw, th, 44); g.fill();
          var ix = cx + 44, iw = tw - 88;
          g.fillStyle = col.hi;
          var labelPx = cols === 2 ? 44 : 52, big;
          if (s.phrase) {
            g.font = "800 100px " + BRIC;
            var lines, fs = cols === 2 ? 92 : 124;
            for (; fs > 44; fs -= 4) { g.font = "800 " + fs + "px " + BRIC; lines = wrapLines(g, s.phrase, iw); if (lines.length * fs * 1.0 <= th - labelPx * 2.6 - 40) { break; } }
            lines = wrapLines(g, s.phrase, iw);
            for (var li = 0; li < lines.length; li++) { g.fillText(lines[li], ix, cy + 44 + fs * 0.88 + li * fs); }
          } else {
            big = fitFont(g, String(s.num), MONO, 500, iw, cols === 2 ? 190 : 230, 80);
            g.fillText(String(s.num), ix, cy + 44 + big * 0.82);
          }
          g.fillStyle = col.fg; g.font = "600 " + labelPx + "px " + BRIC;
          var ll = wrapLines(g, s.label, iw), lj;
          for (lj = 0; lj < Math.min(2, ll.length); lj++) { g.fillText(ll[lj], ix, cy + th - 44 - (Math.min(2, ll.length) - 1 - lj) * (labelPx * 1.15)); }
        }
        /* footer */
        g.fillStyle = ink; g.font = "500 54px " + MONO; g.fillText("mrbadmus.com", pad, 1830);
        return cv;
      });
  }

  function download(blob) {
    var u = win.URL.createObjectURL(blob), a = h("a");
    a.href = u; a.download = "mrbadmus-wrapped.png"; a.style.display = "none";
    doc.body.appendChild(a); a.click();
    win.setTimeout(function () { if (a.parentNode) { a.parentNode.removeChild(a); } win.URL.revokeObjectURL(u); }, 4000);
  }

  function doShare(mode, P, btn) {
    if (S.sharing) { return; }
    S.sharing = true; btn.disabled = true;
    var note = S.ov && S.ov.querySelector(".wr-note");
    function done() { S.sharing = false; btn.disabled = false; }
    drawImageCanvas(P).then(function (cv) {
      cv.toBlob(function (blob) {
        if (!blob) { if (note) { note.textContent = "Couldn't make the picture. Try again."; } done(); return; }
        var file = null;
        try { file = new win.File([blob], "mrbadmus-wrapped.png", { type: "image/png" }); } catch (e) { file = null; }
        if (mode === "share" && file && win.navigator.canShare && win.navigator.canShare({ files: [file] })) {
          win.navigator.share({ files: [file], title: "My half term on MrBadmus" }).then(done, function (err) {
            if (!err || err.name !== "AbortError") { download(blob); }
            done();
          });
        } else { download(blob); done(); }
      }, "image/png");
    }).catch(function (e) { debug("image failed: " + e.message); if (note) { note.textContent = "Couldn't make the picture. Try again."; } done(); });
  }

  /* ═════════════════════════════════════════════════════════════════════
     6. LOCALHOST DEV HOOK (test harness only; inert on the live site)
     ═════════════════════════════════════════════════════════════════════ */
  function dev(o) {
    if (!IS_LOCAL) { return false; }
    S.shown = true; if (o && o.role) { ROLE = o.role; }
    place();
    return true;
  }

  win.MRBWrapped = { open: open, close: close, dev: dev };

  if (script && script.hasAttribute("data-wrapped")) { whenIdle(function () { boot(0); }); }
})(window);
