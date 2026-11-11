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
    if (open) { creditKnowledge(card, viaSwipe); }
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
      return;
    }
    el = closest(t, "[data-lean-word]");
    if (el) { el.setAttribute("aria-expanded", el.getAttribute("aria-expanded") === "true" ? "false" : "true"); }
  }, true);

  /* Swipe across a card toggles it. touch-action: pan-y on .lean-card (lean.css) leaves
     the vertical scroll to the browser and sends us the horizontal part. */
  var down = null;
  document.addEventListener("pointerdown", function (e) {
    var card = closest(e.target, ".lean-card");
    if (!card || (e.pointerType === "mouse" && e.button !== 0)) { down = null; return; }
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

  /* Give every control its aria-expanded, now and whenever the page builds more. */
  function init(root) {
    each((root || document).querySelectorAll(
      ".lean-card-btn, .lean-deeper-btn, [data-lean-cell], [data-lean-word]"), function (b) {
      if (!b.hasAttribute("aria-expanded")) { b.setAttribute("aria-expanded", "false"); }
    });
    each((root || document).querySelectorAll("[data-lean-showall]"), function (b) {
      if (!b.hasAttribute("aria-pressed")) { b.setAttribute("aria-pressed", "false"); }
    });
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

  window.MrBadmusLean = { init: init, toggleCard: toggleCard };
})();
