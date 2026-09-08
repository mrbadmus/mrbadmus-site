/* ═══════════════════════════════════════════════════════════════════════
   student-bell.js — the student's messages, on every logged-in surface.

   MRB-337, 8 Sep 2026. Mide's words: "the student page should have a
   notification like bell icon where they can check all their messages, but I
   still like that the message appears at the top the way it does currently,
   and when they have a new unread message, this should reflect on the bell
   icon."

   ONE FILE, SIX SURFACES, TWO PALETTES. The KS3 studio pages (student/class,
   student/assignment) and the KS4 chrome pages (leaderboard, weekly-challenge,
   my-challenges, revision, student/classes) share no tokens at all, so nothing
   here hardcodes a colour that only works on one of them: every paint goes
   through a `--mbell-*` variable which `tone()` fills from THAT page's own
   token names.

   ⚠️ THE PANEL IS A CHILD OF `document.body`, NEVER OF A MOUNT HOST, and that
   is the fix for a real defect rather than a style preference. `draw()` in
   shared/student-runtime.js empties the whole mount host and rebuilds the
   template on every `setState`; it restores focus and form values but keeps no
   record of any element's `scrollTop`. A panel living inside that host would be
   destroyed — open state, scroll position and all — every time the student
   pressed anything. shared/set-work.js owns one body-level overlay for the
   teacher's sheet for exactly this reason; this is the student's half of the
   same ruling.

   The BUTTON does live in the page header, because that is where Mide asked
   for it. It survives the rebuild the way the reminder banner does — through
   `window.__MRB_AFTER_DRAW__`, re-inserted idempotently — and it carries no
   state of its own: the unread count lives in `state`, so a button that has
   just been rebuilt paints the same number the old one had.

   ⚠️ ONE SOURCE OF TRUTH FOR "UNREAD", AND IT IS `state.items`. The badge
   counts it. The class page's reminder banner is governed by it (see
   `markReadLocal` and the `change` listener in student-live.js). Neither keeps
   its own tally, because two tallies of one fact drift.
   ═══════════════════════════════════════════════════════════════════════ */
(function () {
  "use strict";

  if (window.MrBadmusBell) { return; }

  /* ── the words ────────────────────────────────────────────────────────
     Nouns, labels, numbers, dates and one button verb. Nothing here explains
     the platform to a child (CLAUDE.md §8.10). */
  var TITLE   = "Messages";
  var CLOSE   = "Close";
  var EMPTY   = "No messages";
  /* Said about the student's messages, never about a request or a server —
     the same shape as `SAY.generic` in student-live.js. */
  var FAILED  = "We could not load your messages just now.";
  /* ⚠️ THE FOURTH KIND IS `work`, NOT `new_work`, AND GETTING IT WRONG WAS
     SILENT. `NOTIF_SOURCES` on the backend is
     `['reminder','feedback','shoutout','work']` and the composite id is
     `<source>:<uuid>`, so a `work` entry arriving at a map that only knew
     `new_work` fell through the `KINDS[r.kind] ? r.kind : "reminder"`
     normaliser and was RELABELLED `Reminder` — the right message under the
     wrong heading, with nothing anywhere saying so. `new_work` is kept as a
     tolerated alias because it costs one line and it means a rename on either
     side degrades to the right word rather than to the wrong one. */
  var KINDS   = {
    reminder: "Reminder",
    feedback: "Feedback",
    shoutout: "Shoutout",
    work:     "New work",
    new_work: "New work"
  };
  /* ⚠️ AN UNKNOWN KIND IS NOT A REMINDER. It used to become one, which is a
     LIE about who sent the message and what it is about. A kind this build has
     never heard of gets the only honest heading there is. */
  var KIND_UNKNOWN = "Message";

  var PATH_LIST = "/api/student/notifications";
  var PATH_READ = "/api/student/notifications/";   // + <id> + "/read"

  /* A fetch has no timeout of its own. 20s is the warm budget student-live.js
     uses for a second backend call on an already-woken instance; the bell is
     never the thing a student is waiting for, so it does not get the 75s cold
     budget — a bell that never arrives simply does not appear. */
  var TIMEOUT_MS = 20000;
  /* visibilitychange fires on every tab flick. This is the floor between two
     refetches; it is NOT a poll, and there is no timer anywhere in this file
     that re-arms itself. */
  var REFETCH_FLOOR_MS = 15000;

  var state = {
    items: [],
    loaded: false,      // a successful fetch has happened at least once
    failed: false,
    open: false,
    fetchedAt: 0,
    inflight: null
  };

  var opts = null;      // set by mount()
  var mounted = false;  // an explicit mount() beats autoAttach()
  var bound = false;    // the visibilitychange listener is attached once
  var listeners = [];
  var panel = null;
  var listEl = null;
  var lastButton = null;

  // ── small helpers ──────────────────────────────────────────────────────

  function el(tag, css, text) {
    var n = document.createElement(tag);
    if (css) { n.style.cssText = css; }
    if (text != null) { n.textContent = text; }
    return n;
  }

  function backendBase() {
    var cfg = window.MrBadmusConfig || {};
    return cfg.BACKEND_URL || "https://mrbadmus-backend.onrender.com";
  }

  /* The Supabase project ref, so the stored-session key is right in BOTH
     universes. `sb-<ref>-auth-token` is the key CLAUDE.md names. */
  function projectRef() {
    var cfg = window.MrBadmusConfig || {};
    var url = cfg.SUPABASE_URL || "https://urklkrwevjtlfbwnipjn.supabase.co";
    var m = /^https?:\/\/([^.]+)\./.exec(url);
    return m ? m[1] : "urklkrwevjtlfbwnipjn";
  }

  /* ⚠️ THE FALLBACK READS THE STORED SESSION AND NEVER CREATES A CLIENT.
     Four of the six surfaces already own a Supabase client and two do not
     (revision.html reads localStorage directly and loads no SDK at all).
     Creating a second GoTrue client against the same storage key to serve a
     bell would put two token refreshers on one page — so the surfaces that
     have a client HAND IT OVER through `opts.token`, and the ones that do not
     get this, which is exactly what revision.html already does for its own
     signed URLs. A stale token here costs a bell, not a page. */
  function storedToken() {
    try {
      var raw = window.localStorage.getItem("sb-" + projectRef() + "-auth-token");
      if (!raw) { return null; }
      var s = JSON.parse(raw);
      var expMs = s && s.expires_at ? s.expires_at * 1000 : 0;
      if (!s || !s.access_token || (expMs && expMs <= Date.now())) { return null; }
      return s.access_token;
    } catch (e) { return null; }
  }

  function token() {
    if (opts && typeof opts.token === "function") {
      try { return Promise.resolve(opts.token()); }
      catch (e) { return Promise.resolve(null); }
    }
    return Promise.resolve(storedToken());
  }

  /* Every date a student sees is London, whatever their device says. C2 in
     RISKS.md forbids this on the server (it crashes Render); on the client it
     is the only honest answer for a UK school.

     ⚠️ INTL IS ASKED FOR THE NUMBERS, NEVER FOR THE SPELLING, and the array
     below is why. `en-GB`'s own short month for September is "Sept" — four
     letters, the only month that is not three — so a bare `month:"short"`
     would print `8 Sept` here beside `8 Sep` everywhere else on the same
     page. This is the same array, and the same ruling, as `MONTHS` in
     shared/student-live.js. */
  var MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
                "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"];
  var LONDON = null;
  function when(iso) {
    if (!iso) { return ""; }
    var t = Date.parse(iso);
    if (isNaN(t)) { return ""; }
    try {
      if (!LONDON) {
        LONDON = new Intl.DateTimeFormat("en-GB", {
          timeZone: "Europe/London", day: "numeric", month: "numeric",
          hour: "2-digit", minute: "2-digit", hour12: false
        });
      }
      var got = {};
      LONDON.formatToParts(new Date(t)).forEach(function (p) {
        got[p.type] = p.value;
      });
      var mi = Number(got.month) - 1;
      if (!(mi >= 0 && mi < 12)) { return ""; }
      return Number(got.day) + " " + MONTHS[mi] + ", " +
             got.hour + ":" + got.minute;
    } catch (e) {
      return new Date(t).toISOString().slice(0, 10);
    }
  }

  /* `class` and `env` travel, for the reason `carryParams` gives in
     student-live.js: dropping `class` sends a two-class student to whichever
     class the page picks, and dropping `env` moves a tester from the test
     project to production mid-journey. */
  function carry(path) {
    try {
      var q = new URLSearchParams(window.location.search);
      var keep = new URLSearchParams();
      ["class", "env", "api"].forEach(function (k) {
        if (q.get(k)) { keep.set(k, q.get(k)); }
      });
      var qs = keep.toString();
      return qs ? path + (path.indexOf("?") < 0 ? "?" : "&") + qs : path;
    } catch (e) { return path; }
  }

  /* An item's destination, or "" when it has none. Empty rather than a
     guessed path — a link that 404s is worse than a row that does not move. */
  function hrefFor(item) {
    if (!item) { return ""; }
    if (item.assignment_id) {
      var base = carry("/student/assignment.html");
      return base + (base.indexOf("?") < 0 ? "?" : "&") +
             "assignment=" + encodeURIComponent(item.assignment_id);
    }
    /* The contract allows "a link target where one exists". Only a
       same-origin absolute path is followed: an off-site URL arriving in a
       message row must never become a navigation. */
    var link = item.href || item.link || item.link_target || "";
    if (typeof link === "string" && /^\/[^/]/.test(link)) { return carry(link); }
    return "";
  }

  /* The raw row id inside the contract's composite id — `reminder:<uuid>`,
     `feedback:<uuid>` and so on. Matched from the RIGHT so a change to the
     prefix's spelling cannot silently stop the banner and the badge agreeing. */
  function rawId(id) {
    return String(id == null ? "" : id).split(":").pop();
  }

  function unread() {
    var n = 0;
    for (var i = 0; i < state.items.length; i++) {
      if (!state.items[i].read) { n++; }
    }
    return n;
  }

  function announce() {
    for (var i = 0; i < listeners.length; i++) {
      try { listeners[i](unread(), state.items.slice(), state.loaded); }
      catch (e) { /* a listener must never break the bell */ }
    }
  }

  // ── styling ────────────────────────────────────────────────────────────

  /* One <style> element, injected once. Kept here rather than in a .css file
     so the bell is ONE deployable asset on six pages, four of which do not
     share a stylesheet with the other two. */
  var STYLE_ID = "mrb-bell-style";
  function styles() {
    if (document.getElementById(STYLE_ID)) { return; }
    var s = document.createElement("style");
    s.id = STYLE_ID;
    s.textContent = [
      /* ⚠️ NOT `.nav-icon-link`. That class is `display:none` under 400px in
         shared/nav.css, which is BELOW the 390px this must be measured at —
         the bell would have vanished on exactly the phone most students use.
         Its own class, matching that pill's geometry by hand. */
      ".mrb-bell-btn{position:relative;display:inline-flex;align-items:center;",
      "justify-content:center;box-sizing:border-box;min-width:40px;min-height:40px;",
      "padding:0 8px;border:0;border-radius:999px;background:transparent;",
      "color:var(--mbell-muted);cursor:pointer;font:inherit;line-height:1;",
      "flex:none;transition:background .15s,color .15s}",
      ".mrb-bell-btn:hover{background:var(--mbell-soft);color:var(--mbell-accent)}",
      ".mrb-bell-btn:focus-visible{outline:2px solid var(--mbell-accent);outline-offset:2px}",
      ".mrb-bell-btn svg{width:20px;height:20px;display:block}",
      ".mrb-bell-badge{position:absolute;top:2px;right:1px;min-width:16px;height:16px;",
      "box-sizing:border-box;padding:0 4px;border-radius:999px;",
      "background:var(--mbell-accent);color:var(--mbell-on-accent);",
      "font:700 10px/16px ui-sans-serif,system-ui,-apple-system,sans-serif;",
      "text-align:center;letter-spacing:0}",

      "#mrb-bell-panel{position:fixed;z-index:1200;box-sizing:border-box;",
      "display:flex;flex-direction:column;max-height:min(70vh,520px);",
      "background:var(--mbell-paper);color:var(--mbell-ink);",
      "border:1px solid var(--mbell-rule);border-radius:12px;",
      "box-shadow:0 18px 44px rgba(0,0,0,.22);overflow:hidden}",
      "#mrb-bell-panel[hidden]{display:none}",
      ".mrb-bell-head{display:flex;align-items:center;gap:12px;flex:none;",
      "padding:12px 14px;border-bottom:1px solid var(--mbell-rule)}",
      ".mrb-bell-title{flex:1;font:700 .95rem/1.2 inherit;letter-spacing:-.01em}",
      ".mrb-bell-close{flex:none;min-height:40px;padding:0 12px;cursor:pointer;",
      "border:1px solid var(--mbell-rule);border-radius:8px;background:transparent;",
      "color:inherit;font:inherit;font-size:.85rem}",
      ".mrb-bell-close:hover{background:var(--mbell-soft)}",
      ".mrb-bell-list{flex:1 1 auto;min-height:0;overflow-y:auto;",
      "-webkit-overflow-scrolling:touch;margin:0;padding:0;list-style:none}",
      ".mrb-bell-row{display:block;width:100%;box-sizing:border-box;text-align:left;",
      "padding:12px 14px;border:0;border-bottom:1px solid var(--mbell-rule);",
      "background:transparent;color:inherit;font:inherit;cursor:default}",
      ".mrb-bell-row[data-go=\"1\"]{cursor:pointer}",
      ".mrb-bell-row:hover{background:var(--mbell-soft)}",
      ".mrb-bell-row:focus-visible{outline:2px solid var(--mbell-accent);outline-offset:-2px}",
      ".mrb-bell-row:last-child{border-bottom:0}",
      ".mrb-bell-kind{display:inline-flex;align-items:center;gap:6px;",
      "font:700 10px/1 ui-sans-serif,system-ui,-apple-system,sans-serif;",
      "letter-spacing:.12em;text-transform:uppercase;color:var(--mbell-muted)}",
      ".mrb-bell-dot{width:7px;height:7px;border-radius:50%;",
      "background:var(--mbell-accent);display:inline-block}",
      ".mrb-bell-text{display:block;margin-top:6px;font-size:.9rem;line-height:1.45;",
      "overflow-wrap:anywhere}",
      ".mrb-bell-row[data-unread=\"1\"] .mrb-bell-text{font-weight:600}",
      ".mrb-bell-when{display:block;margin-top:6px;font-size:.75rem;",
      "color:var(--mbell-muted)}",
      ".mrb-bell-say{margin:0;padding:22px 14px;font-size:.9rem;line-height:1.45;",
      "color:var(--mbell-muted);text-align:center}"
    ].join("");
    document.head.appendChild(s);
  }

  /* The two palettes. Every declaration names the PAGE'S OWN token with a
     literal fallback, so a surface that has not loaded its stylesheet yet
     still paints something legible rather than transparent-on-transparent. */
  var TONES = {
    studio: {
      "--mbell-ink":       "var(--st-ink,#2A2018)",
      "--mbell-muted":     "var(--st-ghost,#8A7B6B)",
      "--mbell-paper":     "var(--st-paper,#FFFCF5)",
      "--mbell-rule":      "var(--st-rule,#E0D2B9)",
      "--mbell-accent":    "var(--st-accent,#E4572E)",
      "--mbell-on-accent": "#FFFFFF",
      "--mbell-soft":      "var(--st-crumb-bg,rgba(228,87,46,.10))"
    },
    chrome: {
      "--mbell-ink":       "var(--text,#241C14)",
      "--mbell-muted":     "var(--muted,#6B5F51)",
      "--mbell-paper":     "var(--card,#FFFFFF)",
      "--mbell-rule":      "var(--border,#E4DAC6)",
      "--mbell-accent":    "var(--accent,#A63C12)",
      "--mbell-on-accent": "var(--on-accent,#FFFFFF)",
      "--mbell-soft":      "var(--accent-soft,rgba(166,60,18,.09))"
    }
  };

  function paint(node, toneName) {
    var t = TONES[toneName] || TONES.chrome;
    for (var k in t) {
      if (Object.prototype.hasOwnProperty.call(t, k)) {
        node.style.setProperty(k, t[k]);
      }
    }
  }

  // ── the button ─────────────────────────────────────────────────────────

  var BELL_SVG =
    '<svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false">' +
    '<path d="M12 3a6 6 0 0 0-6 6v3.6L4.4 16h15.2L18 12.6V9a6 6 0 0 0-6-6Z" ' +
    'stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"/>' +
    '<path d="M9.6 19a2.4 2.4 0 0 0 4.8 0" stroke="currentColor" ' +
    'stroke-width="1.8" stroke-linecap="round"/></svg>';

  function label() {
    var n = unread();
    if (!n) { return TITLE; }
    return TITLE + ", " + n + " unread";
  }

  function makeButton(toneName) {
    var b = document.createElement("button");
    b.type = "button";
    b.className = "mrb-bell-btn";
    b.setAttribute("data-mrb-bell", "1");
    b.setAttribute("aria-haspopup", "dialog");
    b.setAttribute("aria-expanded", "false");
    b.innerHTML = BELL_SVG;
    var badge = el("span", "", "");
    badge.className = "mrb-bell-badge";
    badge.setAttribute("data-mrb-bell-badge", "1");
    badge.hidden = true;
    b.appendChild(badge);
    paint(b, toneName);
    b.addEventListener("click", function (ev) {
      ev.preventDefault();
      ev.stopPropagation();
      toggle(b);
    });
    return b;
  }

  /* Repaints EVERY bell on the page. There is normally one, but a rebuilt
     header can briefly leave the old node attached, and a badge that says 3
     next to one that says 0 is worse than either. */
  function repaintButtons() {
    var n = unread();
    var text = n > 9 ? "9+" : String(n);
    var all = document.querySelectorAll("[data-mrb-bell]");
    for (var i = 0; i < all.length; i++) {
      var b = all[i];
      b.setAttribute("aria-label", label());
      var badge = b.querySelector("[data-mrb-bell-badge]");
      if (badge) {
        badge.textContent = text;
        badge.hidden = n === 0;      // hidden at 0, per the ruling
      }
    }
  }

  // ── the panel ──────────────────────────────────────────────────────────

  function ensurePanel(toneName) {
    if (panel && panel.isConnected) {
      paint(panel, toneName);
      return panel;
    }
    styles();
    panel = document.createElement("div");
    panel.id = "mrb-bell-panel";
    panel.setAttribute("role", "dialog");
    panel.setAttribute("aria-label", TITLE);
    panel.hidden = true;
    paint(panel, toneName);

    var head = el("div");
    head.className = "mrb-bell-head";
    var title = el("span", "", TITLE);
    title.className = "mrb-bell-title";
    var close = el("button", "", CLOSE);
    close.type = "button";
    close.className = "mrb-bell-close";
    close.addEventListener("click", function () { hide(true); });
    head.appendChild(title);
    head.appendChild(close);

    listEl = document.createElement("ul");
    listEl.className = "mrb-bell-list";

    panel.appendChild(head);
    panel.appendChild(listEl);
    document.body.appendChild(panel);
    return panel;
  }

  function renderList() {
    if (!listEl) { return; }
    listEl.textContent = "";

    if (!state.loaded && state.failed) {
      var f = el("p", "", FAILED);
      f.className = "mrb-bell-say";
      listEl.appendChild(f);
      return;
    }
    if (!state.items.length) {
      var e = el("p", "", EMPTY);
      e.className = "mrb-bell-say";
      listEl.appendChild(e);
      return;
    }

    for (var i = 0; i < state.items.length; i++) {
      listEl.appendChild(row(state.items[i]));
    }
  }

  function row(item) {
    var li = document.createElement("li");
    var b = document.createElement("button");
    b.type = "button";
    b.className = "mrb-bell-row";
    b.setAttribute("data-mrb-bell-row", String(item.id));
    b.setAttribute("data-unread", item.read ? "0" : "1");
    var go = hrefFor(item);
    b.setAttribute("data-go", go ? "1" : "0");

    var kind = el("span", "", "");
    kind.className = "mrb-bell-kind";
    if (!item.read) {
      var dot = el("span");
      dot.className = "mrb-bell-dot";
      kind.appendChild(dot);
    }
    kind.appendChild(document.createTextNode(
      KINDS[item.kind] || KIND_UNKNOWN));

    var text = el("span", "", item.text || "");
    text.className = "mrb-bell-text";

    var date = el("span", "", when(item.created_at));
    date.className = "mrb-bell-when";

    b.appendChild(kind);
    b.appendChild(text);
    if (date.textContent) { b.appendChild(date); }

    b.addEventListener("click", function () { press(item); });
    li.appendChild(b);
    return li;
  }

  /* Tapping a message marks it read and opens its work where it has any.
     ⚠️ THE READ IS NOT AWAITED BEFORE THE NAVIGATION, and `keepalive` is why
     it survives one: a page that unloads mid-request cancels an ordinary
     fetch, which is precisely how an answer used to die silently on this
     estate (see the sink in student-live.js). */
  function press(item) {
    markRead(item.id);
    var go = hrefFor(item);
    if (go) {
      hide(false);
      window.location.href = go;
    }
  }

  /* Under the bell, right-aligned to it, and FULL WIDTH at 390px — the gutter
     is 12px a side, so a 390px phone gets 366px of panel. `position:fixed`
     means the page behind it can be any length without the panel being
     dragged off the bottom of a sticky header. */
  function place(btn) {
    if (!panel || !btn) { return; }
    var r = btn.getBoundingClientRect();
    var vw = document.documentElement.clientWidth || window.innerWidth;
    var gutter = 12;
    /* ⚠️ THE CAP IS ABOVE 390, DELIBERATELY. Mide's ruling is FULL WIDTH at
       390px, and 390 − 24 = 366: a 360px cap would have left a six-pixel
       margin on the right and a panel that reads as floating rather than as
       the page's own. 380 is the widest it goes on a desktop, so on every
       phone the gutter is what decides the width. */
    var w = Math.min(380, vw - gutter * 2);
    panel.style.width = w + "px";
    var right = Math.max(gutter, Math.min(vw - r.right, vw - w - gutter));
    panel.style.right = right + "px";
    panel.style.left = "auto";
    panel.style.top = Math.max(gutter, r.bottom + 8) + "px";
  }

  function toggle(btn) { state.open ? hide(true) : show(btn); }

  function show(btn) {
    ensurePanel((opts && opts.tone) || "chrome");
    lastButton = btn || document.querySelector("[data-mrb-bell]");
    renderList();
    panel.hidden = false;
    state.open = true;
    place(lastButton);
    if (lastButton) { lastButton.setAttribute("aria-expanded", "true"); }
    document.addEventListener("keydown", onKey, true);
    document.addEventListener("click", onOutside, true);
    window.addEventListener("resize", onMove);
    window.addEventListener("scroll", onMove, true);
    /* Opening is a chance to be current; the floor keeps it from being a poll
       for a student who taps the bell repeatedly. */
    refresh();
  }

  function hide(focusBack) {
    if (panel) { panel.hidden = true; }
    state.open = false;
    document.removeEventListener("keydown", onKey, true);
    document.removeEventListener("click", onOutside, true);
    window.removeEventListener("resize", onMove);
    window.removeEventListener("scroll", onMove, true);
    var all = document.querySelectorAll("[data-mrb-bell]");
    for (var i = 0; i < all.length; i++) {
      all[i].setAttribute("aria-expanded", "false");
    }
    if (focusBack && lastButton && lastButton.isConnected) {
      try { lastButton.focus(); } catch (e) {}
    }
  }

  function onKey(ev) {
    if (ev.key === "Escape" || ev.key === "Esc") {
      ev.stopPropagation();
      hide(true);
    }
  }

  function onOutside(ev) {
    if (!state.open || !panel) { return; }
    var t = ev.target;
    if (panel.contains(t)) { return; }
    if (t && t.closest && t.closest("[data-mrb-bell]")) { return; }
    hide(false);
  }

  /* The button can be REBUILT under us by the student runtime's redraw, so
     the anchor is re-resolved rather than remembered. */
  function onMove() {
    if (!state.open) { return; }
    var b = document.querySelector("[data-mrb-bell]");
    if (b) { lastButton = b; }
    place(lastButton);
  }

  // ── the data ───────────────────────────────────────────────────────────

  function fetchWithDeadline(url, init) {
    var ctl = new AbortController();
    var timer = setTimeout(function () { ctl.abort(); }, TIMEOUT_MS);
    init = init || {};
    init.signal = ctl.signal;
    return fetch(url, init).then(function (r) {
      clearTimeout(timer);
      return r;
    }, function (e) {
      clearTimeout(timer);
      throw e;
    });
  }

  function normalise(rows) {
    var out = [];
    if (!Array.isArray(rows)) { return out; }
    for (var i = 0; i < rows.length; i++) {
      var r = rows[i] || {};
      if (!r.id) { continue; }
      out.push({
        id: String(r.id),
        /* Kept VERBATIM. `row()` decides the heading; normalising an unknown
           kind to a known one here would throw away the only evidence that
           the contract has moved. */
        kind: String(r.kind || ""),
        text: typeof r.text === "string" ? r.text : "",
        created_at: r.created_at || null,
        read: !!r.read,
        assignment_id: r.assignment_id || null,
        href: r.href || r.link || r.link_target || null
      });
    }
    /* Newest first. The contract says the route already orders them; sorting
       here means a route that changes its mind cannot silently reorder a
       child's messages. */
    out.sort(function (a, b) {
      return (Date.parse(b.created_at) || 0) - (Date.parse(a.created_at) || 0);
    });
    return out;
  }

  function refresh(force) {
    var now = Date.now();
    if (!force && state.inflight) { return state.inflight; }
    if (!force && state.loaded && now - state.fetchedAt < REFETCH_FLOOR_MS) {
      return Promise.resolve();
    }
    state.inflight = token().then(function (tk) {
      if (!tk) { throw new Error("no session"); }
      return fetchWithDeadline(backendBase() + PATH_LIST, {
        headers: { Authorization: "Bearer " + tk }
      });
    }).then(function (res) {
      if (!res.ok) { throw new Error("backend " + res.status); }
      return res.json();
    }).then(function (body) {
      var rows = Array.isArray(body) ? body
               : (body && Array.isArray(body.notifications)) ? body.notifications
               : (body && Array.isArray(body.messages)) ? body.messages
               : [];
      state.items = normalise(rows);
      state.loaded = true;
      state.failed = false;
      state.fetchedAt = Date.now();
    }).catch(function () {
      /* SILENT. A bell that cannot load is a bell with no badge; it must never
         put an error in front of a child looking at their class. The panel
         says so only if they open it. */
      state.failed = true;
      state.fetchedAt = Date.now();
    }).then(function () {
      state.inflight = null;
      repaintButtons();
      if (state.open) { renderList(); }
      announce();
    });
    return state.inflight;
  }

  /* Marks one message read — locally at once, so the badge answers the tap,
     and on the server without being waited for. `keepalive` because `press()`
     navigates immediately afterwards. */
  function markRead(id) {
    if (!id) { return; }
    markReadLocal([id]);
    token().then(function (tk) {
      if (!tk) { return; }
      return fetch(backendBase() + PATH_READ +
                   encodeURIComponent(String(id)) + "/read", {
        method: "POST",
        headers: { Authorization: "Bearer " + tk },
        keepalive: true
      });
    }).catch(function () { /* the row simply returns unread next load */ });
  }

  /* ⚠️ THE JOIN BETWEEN THE BADGE AND THE BANNER, AND IT GOES BOTH WAYS.
     student-live.js calls this with the reminder ids it has just marked read
     through its own single-column UPDATE (Dismiss, or opening the work), so
     the badge moves with the banner. The other direction is the `change`
     listener that file registers: when the bell has read every reminder, the
     banner goes. Neither side keeps a count — both read `state.items`.

     Ids are matched on the raw uuid, so the contract's composite `reminder:…`
     and the bare row id from the RPC join up. */
  function markReadLocal(ids) {
    if (!ids || !ids.length) { return; }
    var want = {};
    for (var i = 0; i < ids.length; i++) { want[rawId(ids[i])] = 1; }
    var moved = false;
    for (var j = 0; j < state.items.length; j++) {
      var it = state.items[j];
      if (!it.read && want[rawId(it.id)]) { it.read = true; moved = true; }
    }
    repaintButtons();
    if (state.open) { renderList(); }
    if (moved || state.loaded) { announce(); }
  }

  // ── mounting ───────────────────────────────────────────────────────────

  /* Idempotent, and it re-inserts rather than rebuilding state. The student
     pages call this from `__MRB_AFTER_DRAW__` after every rebuild of the mount
     host; the count lives in `state`, so the new button paints the old number. */
  function place_button(host, where, toneName) {
    if (!host || !host.isConnected) { return null; }
    var existing = host.querySelector(":scope > [data-mrb-bell]");
    if (existing) { paint(existing, toneName); repaintButtons(); return existing; }
    styles();
    var b = makeButton(toneName);
    if (where === "first" || !where) {
      host.insertBefore(b, host.firstChild);
    } else if (where && where.nodeType === 1 && where.parentNode === host) {
      host.insertBefore(b, where);
    } else {
      host.appendChild(b);
    }
    repaintButtons();
    return b;
  }

  /* opts:
       host   — element, or a function returning one, or a selector
       place  — "first" | "last" | an element already inside host
       tone   — "studio" | "chrome"
       token  — () => Promise<string|null>, the caller's access token   */
  function mount(o) {
    opts = o || {};
    mounted = true;
    styles();
    ensurePanel(opts.tone || "chrome");
    attach();
    if (!bound) { bind(); }
    refresh(true);
    return window.MrBadmusBell;
  }

  function resolveHost() {
    var h = opts && opts.host;
    if (typeof h === "function") { try { h = h(); } catch (e) { h = null; } }
    if (typeof h === "string") { h = document.querySelector(h); }
    return h && h.nodeType === 1 ? h : null;
  }

  /* Called on mount and again from every after-draw hook. */
  function attach() {
    var host = resolveHost();
    if (!host) { return null; }
    var where = opts.place;
    if (typeof where === "string" && where !== "first" && where !== "last") {
      where = host.querySelector(where) || "last";
    }
    return place_button(host, where, opts.tone || "chrome");
  }

  function bind() {
    bound = true;
    /* ⚠️ LOAD AND `visibilitychange`, AND NOTHING ELSE. No interval, no
       re-arming timeout: a bell that polls is a bell that wakes Render every
       thirty seconds for every student in the school. */
    document.addEventListener("visibilitychange", function () {
      if (!document.hidden) { refresh(); }
    });
  }

  // ── auto-attach, for the KS4 chrome pages ──────────────────────────────

  /* The five hand-written / generated chrome surfaces need one <script> tag
     and no per-page JavaScript. The student pages call mount() explicitly from
     student-live.js and an explicit mount always wins, so this never fires
     twice on one page.

     ⚠️ NOTHING HAPPENS WITHOUT A SESSION. weekly-challenge.html,
     my-challenges.html, revision.html and leaderboard.html are PUBLIC pages —
     a signed-out visitor must not be shown a bell at all. */
  function autoAttach() {
    if (mounted) { return; }
    if (!storedToken()) { return; }
    var host = document.querySelector(".nav-cluster") ||
               document.querySelector("nav.top-nav > div:last-of-type");
    if (!host) { return; }
    var before = host.querySelector("#nav-auth-area") ||
                 host.querySelector(".nav-burger") ||
                 host.querySelector(".signout-btn");
    mount({
      host: host,
      place: before && before.parentNode === host ? before : "last",
      tone: "chrome"
    });
  }

  window.MrBadmusBell = {
    mount: mount,
    attach: attach,
    refresh: refresh,
    markRead: markRead,
    markReadLocal: markReadLocal,
    unread: unread,
    items: function () { return state.items.slice(); },
    loaded: function () { return state.loaded; },
    open: function () { show(document.querySelector("[data-mrb-bell]")); },
    close: function () { hide(false); },
    on: function (fn) { if (typeof fn === "function") { listeners.push(fn); } }
  };

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", autoAttach);
  } else {
    autoAttach();
  }
})();
