/* shared/lean.js: behaviour for the lean lesson shape. Markup: lean_blocks.py. Look: lean.css.
   Loaded ONLY by lean pages (KS3 and KS4). Plain script, no dependencies.

   What it does
     - a card opens and closes on tap, Enter or Space (its button is a real <button>),
       and on a horizontal swipe across the card
     - a reveal-table cell shows its answer when tapped; "Show all" shows every cell
     - Dive deeper opens on tap
     - a key-word chip with a definition opens it on tap
     - keeps aria-expanded true to the visible state

   State is kept in attributes the page template never writes (`data-lean-open`
   on the wrapper, `aria-expanded` on the button), because KS4's runtime rewrites
   any attribute its template names on every render. So everything here survives a
   redraw, and the controls are given their aria-expanded on load, and again for
   anything the runtime builds later (MutationObserver).

   Swipes never start from a control. A swipe that begins on an input, select, textarea or a
   button inside the card (a slider, a preset), on anything inside [data-no-swipe], or on an
   element that scrolls sideways, is the control's or the scroller's own gesture, not a toggle.
   The card's own header button still starts a swipe.

   Figures. A diagram inside a lean card (`.lean-fig`, written by lean_blocks.fig_wrap) is FITTED
   to the card width (`data-lean-fits`) only when its smallest label still draws at 11px or more
   there. A drawing that would read smaller keeps the page's own sideways-scrolling frame, at the
   width where its labels reach 11px. The attribute is set here, never by a template, so KS4's
   patch-in-place renderer leaves it alone.

   Rail credit. KS3's rail reads `data-stage-done` on a section (shared/ks3.js
   doneByDom), so the Key knowledge section is marked done the first time anything
   in it opens, and `ks3:progress` is announced so the bar repaints. KS4's rail is
   redrawn by its component on a click inside `#s-knowledge`; a swipe is not a
   click, so a swipe sends one to the section.
*/
(function () {
  "use strict";
  if (window.MrBadmusLean) { return; }

  var SWIPE_MIN = 48;        // px across
  var SWIPE_RATIO = 1.8;     // across must beat down by this much, so a scroll never counts
  var swallowClick = 0;      // timestamp until which a click after a swipe is ignored

  function each(list, fn) { for (var i = 0; i < list.length; i++) { fn(list[i], i); } }
  function closest(el, sel) {
    while (el && el.nodeType === 1) {
      if (el.matches ? el.matches(sel) : el.msMatchesSelector(sel)) { return el; }
      el = el.parentNode;
    }
    return null;
  }

  function setOpen(wrap, btn, open) {
    if (open) { wrap.setAttribute("data-lean-open", ""); } else { wrap.removeAttribute("data-lean-open"); }
    if (btn) { btn.setAttribute("aria-expanded", open ? "true" : "false"); }
  }

  function creditKnowledge(from, viaSwipe) {
    var sec = closest(from, '[data-lean-sec="knowledge"]');
    if (!sec) { return; }
    if (sec.hasAttribute("data-stage-done") && sec.getAttribute("data-stage-done") !== "1") {
      sec.setAttribute("data-stage-done", "1");
      var ev;
      try { ev = new CustomEvent("ks3:progress", { bubbles: true }); }
      catch (err) { ev = document.createEvent("Event"); ev.initEvent("ks3:progress", true, false); }
      sec.dispatchEvent(ev);
    }
    if (viaSwipe) {
      var click;
      try { click = new MouseEvent("click", { bubbles: false }); }
      catch (err2) { click = document.createEvent("Event"); click.initEvent("click", false, false); }
      sec.dispatchEvent(click);
    }
  }

  function toggleCard(card, viaSwipe) {
    var btn = card.querySelector(".lean-card-btn");
    var open = !card.hasAttribute("data-lean-open");
    setOpen(card, btn, open);
    if (open) { initFigs(card); creditKnowledge(card, viaSwipe); }
  }

  function toggleCell(cell) {
    var open = cell.getAttribute("aria-expanded") !== "true";
    cell.setAttribute("aria-expanded", open ? "true" : "false");
    if (open) { creditKnowledge(cell, false); }
  }

  function toggleAll(btn) {
    var reveal = closest(btn, "[data-lean-reveal]");
    if (!reveal) { return; }
    var on = !reveal.hasAttribute("data-lean-all");
    if (on) { reveal.setAttribute("data-lean-all", ""); } else { reveal.removeAttribute("data-lean-all"); }
    btn.setAttribute("aria-pressed", on ? "true" : "false");
    each(reveal.querySelectorAll("[data-lean-cell]"), function (c) {
      c.setAttribute("aria-expanded", on ? "true" : "false");
    });
    if (on) { creditKnowledge(reveal, false); }
  }

  document.addEventListener("click", function (e) {
    if (Date.now() < swallowClick) { e.stopPropagation(); e.preventDefault(); return; }
    var t = e.target;
    var el = closest(t, ".lean-card-btn");
    if (el) { toggleCard(closest(el, ".lean-card"), false); return; }
    el = closest(t, "[data-lean-cell]");
    if (el) { toggleCell(el); return; }
    el = closest(t, "[data-lean-showall]");
    if (el) { toggleAll(el); return; }
    el = closest(t, ".lean-deeper-btn");
    if (el) {
      var box = closest(el, "[data-lean-deeper]");
      setOpen(box, el, !box.hasAttribute("data-lean-open"));
      initFigs(box);
      return;
    }
    el = closest(t, "[data-lean-word]");
    if (el) { el.setAttribute("aria-expanded", el.getAttribute("aria-expanded") === "true" ? "false" : "true"); }
  }, true);

  /* Where a swipe must NOT start: a control's own gesture, or a sideways scroller's. */
  function ignoresSwipe(target, card) {
    for (var el = target; el && el !== card; el = el.parentNode) {
      if (el.nodeType !== 1) { continue; }
      var tag = el.tagName;
      if (tag === "INPUT" || tag === "SELECT" || tag === "TEXTAREA") { return true; }
      if (tag === "BUTTON" && !(el.classList && el.classList.contains("lean-card-btn"))) { return true; }
      if (el.hasAttribute && el.hasAttribute("data-no-swipe")) { return true; }
      if (el.scrollWidth > el.clientWidth + 1) {
        var ox = window.getComputedStyle ? window.getComputedStyle(el).overflowX : "";
        if (ox === "auto" || ox === "scroll") { return true; }
      }
    }
    return false;
  }

  /* Swipe across a card toggles it. touch-action: pan-y on .lean-card (lean.css) leaves
     the vertical scroll to the browser and sends us the horizontal part. */
  var down = null;
  document.addEventListener("pointerdown", function (e) {
    var card = closest(e.target, ".lean-card");
    if (!card || (e.pointerType === "mouse" && e.button !== 0) || ignoresSwipe(e.target, card)) { down = null; return; }
    down = { card: card, x: e.clientX, y: e.clientY, id: e.pointerId };
  }, true);
  document.addEventListener("pointerup", function (e) {
    var d = down; down = null;
    if (!d || d.id !== e.pointerId) { return; }
    var dx = e.clientX - d.x, dy = e.clientY - d.y;
    if (Math.abs(dx) >= SWIPE_MIN && Math.abs(dx) > Math.abs(dy) * SWIPE_RATIO) {
      swallowClick = Date.now() + 350;
      toggleCard(d.card, true);
    }
  }, true);
  document.addEventListener("pointercancel", function () { down = null; }, true);

  /* ── figures: fitted to the card only where the text stays readable ──
     A drawing is fitted (data-lean-fits) when its smallest label still draws at 11px or more at
     the card's width. Otherwise nothing here touches it, and the page's own frame applies: KS4's
     text floor (figFit, a sideways scroller with an edge fade) or KS3's .ks3-figure-scroll. There
     is no button that shrinks a drawing below 11px text (gate ks4_figure_text presses every one). */
  var FLOOR_PX = 11;
  function smallestFont(svg) {                                     // in viewBox units, as the audit reads it
    var min = Infinity;
    each(svg.querySelectorAll("text, tspan"), function (t) {
      if (t.tagName.toLowerCase() === "text" && t.querySelector("tspan")) { return; }
      if (t.hasAttribute("baseline-shift") || !(t.textContent || "").trim()) { return; }
      var fs = parseFloat(window.getComputedStyle(t).fontSize);
      if (fs > 0 && fs < min) { min = fs; }
    });
    return min;
  }
  function readableWidth(svg, box) {                               // narrowest width at which every label is >= 11px
    var v = svg.viewBox && svg.viewBox.baseVal;
    var vbw = (v && v.width) || parseFloat(box.style.getPropertyValue("--fig-vb")) || 0;
    var fs = parseFloat(box.style.getPropertyValue("--fig-fs"));
    if (!(fs > 0)) { fs = smallestFont(svg); }
    if (!(vbw > 0) || !(fs > 0) || fs === Infinity) { return 0; } // no text: it reads at any width
    return FLOOR_PX * vbw / fs;
  }
  function updateFig(fig) {
    var svg = fig.querySelector("svg");
    if (!svg) { return; }
    var box = svg.parentNode;
    var cs = window.getComputedStyle(box);
    var room = box.clientWidth - (parseFloat(cs.paddingLeft) || 0) - (parseFloat(cs.paddingRight) || 0);
    if (!(room > 0)) { return; }                                    // inside a closed card: measured when it opens
    var fits = readableWidth(svg, box) <= room;
    if (fits !== fig.hasAttribute("data-lean-fits")) {
      if (fits) { fig.setAttribute("data-lean-fits", ""); } else { fig.removeAttribute("data-lean-fits"); }
    }
  }
  var figRO = (typeof ResizeObserver === "function") ? new ResizeObserver(function (entries) {
    each(entries, function (en) { updateFig(en.target); });
  }) : null;
  function initFigs(root) {
    each((root || document).querySelectorAll("[data-lean-fig]"), function (fig) {
      if (!fig.__leanFig) { fig.__leanFig = true; if (figRO) { figRO.observe(fig); } }
      updateFig(fig);
    });
  }

  /* Give every control its aria-expanded, now and whenever the page builds more. */
  function init(root) {
    each((root || document).querySelectorAll(
      ".lean-card-btn, .lean-deeper-btn, [data-lean-cell], [data-lean-word]"), function (b) {
      if (!b.hasAttribute("aria-expanded")) { b.setAttribute("aria-expanded", "false"); }
    });
    each((root || document).querySelectorAll("[data-lean-showall]"), function (b) {
      if (!b.hasAttribute("aria-pressed")) { b.setAttribute("aria-pressed", "false"); }
    });
    initFigs(root);
  }
  var queued = false;
  function later() {
    if (queued) { return; }
    queued = true;
    (window.requestAnimationFrame || setTimeout)(function () { queued = false; init(); });
  }
  function start() {
    init();
    if (window.MutationObserver && document.body) {
      new MutationObserver(later).observe(document.body, { childList: true, subtree: true });
    }
  }
  if (document.readyState === "loading") { document.addEventListener("DOMContentLoaded", start); }
  else { start(); }

  window.addEventListener("resize", function () { initFigs(); });
  window.MrBadmusLean = { init: init, toggleCard: toggleCard, ignoresSwipe: ignoresSwipe };
})();
