/* shared/catch-up-sheet.js — the Catch-up lesson sheet (pupil side).

   A catch-up is a lesson plus questions the teacher set to named pupils. The
   pupil reads the lesson FIRST, and reads it without leaving the class page:
   this opens a sheet INSIDE the page — full-screen under the pupil's own
   header on a phone, a large panel on a desktop — holding a same-origin
   <iframe> of the existing lesson page. No lesson file is edited. The lesson
   page's own site chrome (its header, footer, tutor chat button) is hidden by
   a stylesheet injected into the frame from here, and navigation stays inside
   the frame: a link to anywhere that is not a lesson page does nothing.

   It is used by BOTH pupil pages (loaded from shared/student-live.js):

     class page       the sheet's one big button is "Start the questions" and
                      goes to student/assignment.html for that assignment.
     questions page   mode "back": the same sheet, reopened over the questions
                      without leaving them; the one button is "Back to the
                      questions" and only closes the sheet. Progress is saved
                      per answer already, and nothing here navigates away.

   Address: `#catchup=<assignment id>`. It opens the sheet on load, on a link
   click (hashchange) and after a reload, and Back closes it — the same
   fragment idea as `#cards=<id>` for the flashcard overlay. Closing drops the
   fragment (replaceState) so the same button opens it again.

   Registration: `MRBCatchUp.register([{ id, title, lessonUrl, questionsUrl }],
   { mode })`. The module knows nothing about Supabase or the backend; the
   caller resolves the lesson address (KS3 / KS4) and passes it in.

   The sheet is a sibling of <body>'s other children, NOT inside the runtime's
   mount host: shared/student-runtime.js empties that host on every setState,
   which would destroy an open sheet (and reload its iframe) on every tap. */
(function () {
  "use strict";
  if (window.MRBCatchUp) { return; }

  var HASH = /^#catchup=([0-9a-f-]{36})$/i;
  var items = {};          // lower-cased id -> item
  var mode = "class";      // "class" | "back"
  var openState = null;    // { id, root, frame, opener }
  var BACK_HOME = null;

  /* ── the chrome hidden inside the lesson frame ───────────────────────────
     KS3 lesson pages draw: header.mrb-topbar.ks3-nav (brand, title, theme,
     bell), footer.ks3-footer, #chatOverlay and its launcher.
     KS4 lesson pages (the compiled ks4-mount pages) draw the same header
     (header.mrb-topbar.ks3-nav inside #ks4-mount) and #chatOverlay, plus a
     footer. The lesson itself (main.ks3-main, the rails) is left alone. The
     rail bar sticks under the header at an offset, so the offset is zeroed. */
  var EMBED_CSS =
    "header.mrb-topbar,header.ks3-nav,.mrb-topbar,.ks3-nav,nav.nav,header.nav," +
    "footer,.ks3-footer,.site-footer," +
    "#chatOverlay,.chat-overlay,.chat-fab,.chat-launch,#chatBtn,#chatFab,#chatToggle," +
    "[data-mrb-bell],.mrb-bell,[data-mrb-theme]" +
    "{display:none!important}" +
    ":root{--ks3-nav-h:0px!important;--nav-h:0px!important;--topbar-h:0px!important}" +
    "html,body{scroll-padding-top:0!important}" +
    "body{padding-top:0!important;margin-top:0!important}";

  var LESSON_PATH = /^\/(ks3|combined|triple)\//;

  function css() {
    if (document.querySelector('style[data-mrb="catch-up-sheet"]')) { return; }
    var st = document.createElement("style");
    st.setAttribute("data-mrb", "catch-up-sheet");
    st.textContent =
      "[data-mrb-cu-sheet]{position:fixed;left:0;right:0;bottom:0;top:var(--mrb-cu-top,0px);z-index:55;" +
      "display:flex;flex-direction:column;background:var(--st-ground,var(--ks3-ground,#FBF3E6));" +
      "color:var(--st-ink,var(--ks3-ink,#221E1B));font-family:var(--st-ui,var(--ks3-font-body,system-ui,sans-serif));" +
      "overscroll-behavior:contain}" +
      "[data-mrb-cu-scrim]{display:none}" +
      "[data-mrb-cu-panel]{flex:1;min-height:0;display:flex;flex-direction:column;background:var(--st-paper,var(--ks3-card,#FFFCF5))}" +
      "[data-mrb-cu-bar]{flex:none;display:flex;align-items:center;gap:12px;padding:8px 14px;" +
      "border-bottom:1px solid var(--st-rule,var(--ks3-rule,#E0D2B9));background:var(--st-paper,var(--ks3-card,#FFFCF5))}" +
      "[data-mrb-cu-close]{all:unset;box-sizing:border-box;cursor:pointer;display:inline-flex;align-items:center;gap:8px;" +
      "min-height:44px;padding:0 12px 0 8px;border-radius:10px;font:600 15px/1 var(--st-ui,system-ui,sans-serif);" +
      "color:var(--st-ink,var(--ks3-ink,#221E1B));flex:none}" +
      "[data-mrb-cu-close]:hover{background:var(--st-num-well,var(--ks3-inset,#F1E6D2))}" +
      "[data-mrb-cu-close]:focus-visible,[data-mrb-cu-start]:focus-visible{outline:3px solid var(--st-accent,#E4572E);outline-offset:2px}" +
      "[data-mrb-cu-title]{min-width:0;flex:1;font:600 15px/1.25 var(--st-ui,system-ui,sans-serif);" +
      "overflow:hidden;text-overflow:ellipsis;white-space:nowrap;color:var(--st-body,var(--ks3-ink-muted,#5E5145))}" +
      "[data-mrb-cu-body]{position:relative;flex:1;min-height:0;background:var(--st-ground,var(--ks3-ground,#FBF3E6))}" +
      "[data-mrb-cu-frame]{position:absolute;inset:0;width:100%;height:100%;border:0;background:transparent;" +
      "visibility:hidden}" +
      "[data-mrb-cu-frame][data-ready]{visibility:visible}" +
      "[data-mrb-cu-note]{position:absolute;inset:0;display:none;align-items:center;justify-content:center;" +
      "padding:24px;text-align:center;font:500 16px/1.5 var(--st-ui,system-ui,sans-serif);" +
      "color:var(--st-body,var(--ks3-ink-muted,#5E5145))}" +
      "[data-mrb-cu-sheet][data-nolesson] [data-mrb-cu-note]{display:flex}" +
      "[data-mrb-cu-foot]{flex:none;display:flex;justify-content:flex-end;padding:10px 14px calc(10px + env(safe-area-inset-bottom,0px));" +
      "border-top:1px solid var(--st-rule,var(--ks3-rule,#E0D2B9));background:var(--st-paper,var(--ks3-card,#FFFCF5))}" +
      "[data-mrb-cu-start]{all:unset;box-sizing:border-box;cursor:pointer;display:flex;align-items:center;justify-content:center;gap:10px;" +
      "flex:1;min-height:48px;padding:0 22px;border-radius:var(--st-r-btn,12px);" +
      "background:var(--ks3-accent-text,#A63C12);color:var(--st-paper,#FFFCF5);font:600 16px/1 var(--st-ui,system-ui,sans-serif)}" +
      "[data-mrb-cu-sheet][data-mode=back] [data-mrb-cu-foot]{display:none}" +
      "@media (min-width:900px){" +
      "[data-mrb-cu-sheet]{background:rgba(20,16,12,.55);align-items:center;justify-content:center;padding:12px 24px 24px}" +
      "[data-mrb-cu-panel]{flex:none;width:min(1120px,100%);height:100%;border-radius:var(--st-r-frame,18px);overflow:hidden;" +
      "box-shadow:0 30px 80px -30px rgba(0,0,0,.6);border:1px solid var(--st-rule,var(--ks3-rule,#E0D2B9))}" +
      "[data-mrb-cu-start]{flex:none}" +
      "}";
    document.head.appendChild(st);
  }

  function el(tag, attrs, text) {
    var e = document.createElement(tag);
    if (attrs) { Object.keys(attrs).forEach(function (k) { e.setAttribute(k, attrs[k]); }); }
    if (text != null) { e.textContent = text; }
    return e;
  }

  function topOffset() {
    var h = document.querySelector(".mrb-topbar") || document.querySelector("header");
    if (!h || !h.getBoundingClientRect) { return 0; }
    return Math.max(0, Math.round(h.getBoundingClientRect().bottom));
  }

  /* Hide the lesson page's own chrome and keep the pupil inside it. Called on
     EVERY load of the frame (it is also called after an in-frame navigation). */
  function prepareFrame(frame) {
    var doc, win;
    try { doc = frame.contentDocument; win = frame.contentWindow; } catch (e) { doc = null; }
    if (!doc || !doc.head) { frame.setAttribute("data-ready", "1"); return; }
    if (!doc.getElementById("mrb-cu-embed")) {
      var st = doc.createElement("style");
      st.id = "mrb-cu-embed";
      st.textContent = EMBED_CSS;
      doc.head.appendChild(st);
    }
    /* the frame navigates only to lesson pages; everything else is a no-op */
    if (!doc.documentElement.hasAttribute("data-mrb-cu-links")) {
      doc.documentElement.setAttribute("data-mrb-cu-links", "1");
      doc.addEventListener("click", function (ev) {
        var a = ev.target && ev.target.closest ? ev.target.closest("a[href]") : null;
        if (!a) { return; }
        var raw = a.getAttribute("href") || "";
        if (raw.charAt(0) === "#") { return; }
        var u;
        try { u = new URL(a.href, doc.baseURI); } catch (e) { return; }
        if (u.origin !== window.location.origin) {
          a.setAttribute("target", "_blank");
          a.setAttribute("rel", "noopener noreferrer");
          return;
        }
        if (LESSON_PATH.test(u.pathname) && /\.html?$/.test(u.pathname)) {
          a.setAttribute("target", "_self");
          return;
        }
        ev.preventDefault();
      }, true);
    }
    /* hide the next page's first paint of chrome: the frame is shown again
       by the next load's prepareFrame */
    if (win && !frame.__mrbCuLeave) {
      frame.__mrbCuLeave = true;
      win.addEventListener("pagehide", function () { frame.removeAttribute("data-ready"); });
    }
    frame.setAttribute("data-ready", "1");
  }

  function build(item) {
    css();
    var root = el("div", { "data-mrb-cu-sheet": "1", role: "dialog", "aria-modal": "true",
                           "aria-label": item.title || "Catch-up lesson", "data-mode": mode });
    root.style.setProperty("--mrb-cu-top", topOffset() + "px");
    var scrim = el("div", { "data-mrb-cu-scrim": "1" });
    var panel = el("div", { "data-mrb-cu-panel": "1" });
    var bar = el("div", { "data-mrb-cu-bar": "1" });
    var close = el("button", { type: "button", "data-mrb-cu-close": "1" });
    close.innerHTML = '<svg aria-hidden="true" width="18" height="18" viewBox="0 0 22 22"><path d="M5 5 L17 17 M17 5 L5 17" ' +
      'fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round"/></svg>';
    close.appendChild(document.createTextNode(mode === "back" ? "Back to the questions" : "Close"));
    close.addEventListener("click", function () { api.close(); });
    bar.appendChild(close);
    bar.appendChild(el("div", { "data-mrb-cu-title": "1" }, item.title || ""));
    var body = el("div", { "data-mrb-cu-body": "1" });
    var frame = el("iframe", { "data-mrb-cu-frame": "1", title: item.title || "Lesson",
                               referrerpolicy: "same-origin" });
    body.appendChild(frame);
    body.appendChild(el("div", { "data-mrb-cu-note": "1" }, "This lesson isn't available here."));
    var foot = el("div", { "data-mrb-cu-foot": "1" });
    if (mode !== "back" && item.questionsUrl) {
      var go = el("a", { "data-mrb-cu-start": "1", href: item.questionsUrl }, "Start the questions");
      var svgNS = "http://www.w3.org/2000/svg";
      var svg = document.createElementNS(svgNS, "svg");
      svg.setAttribute("aria-hidden", "true"); svg.setAttribute("width", "12"); svg.setAttribute("height", "12");
      svg.setAttribute("viewBox", "0 0 22 22");
      var p = document.createElementNS(svgNS, "path");
      p.setAttribute("d", "M6 3.5 L13.5 11 L6 18.5"); p.setAttribute("fill", "none");
      p.setAttribute("stroke", "currentColor"); p.setAttribute("stroke-linecap", "round");
      p.setAttribute("stroke-linejoin", "round"); p.setAttribute("stroke-width", "3.4");
      svg.appendChild(p); go.appendChild(svg);
      foot.appendChild(go);
    }
    panel.appendChild(bar); panel.appendChild(body); panel.appendChild(foot);
    root.appendChild(scrim); root.appendChild(panel);
    /* a tap on the dimmed margin (desktop) closes, like the flashcard overlay */
    root.addEventListener("mousedown", function (ev) { if (ev.target === root) { api.close(); } });
    root.addEventListener("keydown", function (ev) {
      if (ev.key === "Escape") { ev.stopPropagation(); api.close(); }
    });
    frame.addEventListener("load", function () {
      if (frame.getAttribute("src") === "about:blank") { return; }
      prepareFrame(frame);
    });
    if (item.lessonUrl) {
      frame.setAttribute("src", item.lessonUrl);
    } else {
      root.setAttribute("data-nolesson", "1");
    }
    return { root: root, frame: frame, close: close };
  }

  function dropFragment() {
    if (!HASH.test(window.location.hash || "")) { return; }
    try { history.replaceState(null, "", window.location.pathname + window.location.search); }
    catch (e) { /* an old browser keeps the fragment; harmless */ }
  }

  var api = {
    register: function (list, opts) {
      if (opts && opts.mode) { mode = opts.mode; }
      (list || []).forEach(function (it) {
        if (it && it.id) { items[String(it.id).toLowerCase()] = it; }
      });
      api.openFromHash();
    },
    isOpen: function () { return !!openState; },
    open: function (id) {
      var key = String(id || "").toLowerCase();
      var item = items[key];
      if (!item) { return false; }
      if (openState && openState.id === key) { return true; }
      if (openState) { api.close(true); }
      var built = build(item);
      document.body.appendChild(built.root);
      openState = { id: key, root: built.root, frame: built.frame,
                    opener: document.activeElement, prevOverflow: document.documentElement.style.overflow };
      document.documentElement.style.overflow = "hidden";
      try { built.close.focus({ preventScroll: true }); } catch (e) { /* focus is a nicety */ }
      return true;
    },
    close: function (keepFragment) {
      if (!openState) { dropFragment(); return; }
      var s = openState;
      openState = null;
      try { s.frame.setAttribute("src", "about:blank"); } catch (e) { /* leaving anyway */ }
      if (s.root.parentNode) { s.root.parentNode.removeChild(s.root); }
      document.documentElement.style.overflow = s.prevOverflow || "";
      if (!keepFragment) { dropFragment(); }
      try { if (s.opener && s.opener.focus && document.contains(s.opener)) { s.opener.focus({ preventScroll: true }); } }
      catch (e) { /* focus is a nicety */ }
    },
    openFromHash: function () {
      var m = HASH.exec(window.location.hash || "");
      if (m) { api.open(m[1]); }
      else if (openState) { api.close(true); }
    },
    /* the fragment that opens a given catch-up's sheet */
    hrefFor: function (id) { return id ? "#catchup=" + encodeURIComponent(id) : ""; }
  };

  window.addEventListener("hashchange", api.openFromHash);
  /* a page restored from the back-forward cache comes back with the sheet's
     iframe gone; open or close to match the fragment */
  window.addEventListener("pageshow", function (ev) { if (ev && ev.persisted) { api.openFromHash(); } });
  window.MRBCatchUp = api;
})();
