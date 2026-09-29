/* ⊕ MRB-351 PUPIL FLOW — THE HOMEWORK CARD'S SIZE AND THE PHONE KEYBOARD.
 *
 * docs/mrb351/PUPIL-FLOW.md §6 (A9, A10), rewritten by STAGE-D-PLAN.md §2.3.
 *
 * WHY. The flashcard overlay is `position:fixed;inset:0` and its dialog is
 * `height:min(100%,760px)`. iOS Safari and Android Chrome (108+) shrink only
 * `window.visualViewport` when the keyboard opens, not the layout viewport,
 * so the fixed dialog keeps its full height and the answer box sits under
 * the keyboard. This listens to `visualViewport`.
 *
 * ⊕ STAGE D (Mide, 29 Sep 2026: "when I click the answer textbox, the screen
 * goes up… reduce the amount of space the question takes"). Two changes:
 *
 *   · THE CARD SIZES TO ITS CONTENT. In homework mode the card is no longer
 *     Design's `flex:1` (every spare pixel): its height is the taller of its
 *     two faces' content, at least 140px, at most 46% of the dialog (never
 *     over 420px) — or, under a keyboard, 34% of what the keyboard leaves.
 *     A height that depends only on content cannot change on focus. The
 *     answer box gets the room back (96px tall on a tall dialog).
 *   · COMPACT MODE ONLY UNDER A REAL KEYBOARD: `innerHeight − visual height
 *     ≥ 100`. A desktop never enters it, so focusing the box moves nothing.
 *     On a phone the dialog is pinned to the visual viewport and the strip
 *     keeps only its headline — what the keyboard forces, nothing more.
 *
 * The practice deck is untouched: every rule is scoped by `data-hw-fit`,
 * which only a homework dialog (the strip `[data-hw="strip"]` exists) gets.
 *
 * The overlay is REBUILT on every state change (A10), so nothing here is set
 * once: it is all re-derived in `__MRB_AFTER_DRAW__`, and on every
 * `visualViewport` resize/scroll.
 *
 * It also owns one more thing about the answer box: when the card in front
 * changes while the box stays on screen (‹ Back), the runtime would carry
 * the old card's text into the new box. The box is given the text the
 * engine holds for ITS card instead.
 *
 * Loaded by shared/student-live.js (STAMPED_DEPS in build_student_port.py).
 */
(function (root) {
  "use strict";
  if (!root.document) { return; }
  var doc = root.document;

  var D = '[data-mrb-dialog="flashcards"]';
  var T = D + '[data-hw-typing="1"]';
  var CSS =
    // ── the card: its content's height (Stage D, decision 1) ──
    '.rd[data-mode="ks3"] ' + D + '[data-hw-fit] [data-card-fit],' +
    D + '[data-hw-fit] [data-card-fit]{flex:0 0 auto!important;min-height:0!important;' +
      'height:var(--hw-card-h)!important;max-height:none!important}' +
    // ── the answer box gets the room back (decision 3) ──
    D + '[data-hw-fit] [data-hw="answer"]{min-height:64px;height:64px}' +
    D + '[data-hw-fit][data-hw-tall="1"] [data-hw="answer"]{height:auto;min-height:96px}' +
    // ⊕ Stage D review — on a tall DESKTOP dialog the box takes the room the
    // card gave back (up to 200px). `data-hw-tall` never changes on focus
    // there (no keyboard), so neither does the box. Mouse-and-keyboard only:
    // a phone's box would otherwise shrink from 200 to 64 as its keyboard rose.
    '@media (hover:hover) and (pointer:fine){' +
      D + '[data-hw-fit][data-hw-tall="1"] [data-hw="write"]{flex:1 1 auto;min-height:0}' +
      D + '[data-hw-fit][data-hw-tall="1"] [data-hw="answer"]{flex:1 1 auto;max-height:200px}}' +
    // ── under a real keyboard only (decision 2) ──
    T + ' [data-hw="strip"]{padding:8px 18px!important;gap:4px!important}' +
    T + ' [data-hw="strip"] > :not([data-hw="progress"]){display:none!important}' +
    T + ' [data-dc-tpl="10328"]{padding:12px 18px!important;gap:10px!important}' +
    T + ' [data-dc-tpl="10334"]{padding:14px 18px!important;gap:8px!important}' +
    T + ' [data-dc-tpl="10340"]{font-size:18px!important;line-height:1.3!important}' +
    T + ' [data-dc-tpl="10350"]{display:none!important}' +
    T + ' [data-hw="check"]{min-height:44px!important}' +
    // ⊕ Sharpen §13.4 — the "I don't know" learn state adds the ANSWER block
    // between the card and the box; it scrolls inside itself if long.
    T + ' [data-hw="learn"] > :last-child{max-height:calc(var(--fc-vh) * .22)!important;overflow:auto!important}';

  function injectCss() {
    if (doc.getElementById("mrb-fc-keyboard-css")) { return; }
    var s = doc.createElement("style");
    s.id = "mrb-fc-keyboard-css";
    s.textContent = CSS;
    (doc.head || doc.documentElement).appendChild(s);
  }

  function vv() {
    var v = root.visualViewport;
    if (v && v.height) { return { height: v.height, offsetTop: v.offsetTop || 0 }; }
    return { height: root.innerHeight, offsetTop: 0 };
  }

  function parts() {
    var ov = doc.querySelector('[data-port-region="flashcards-overlay"]');
    if (!ov) { return null; }
    return {
      ov: ov,
      dialog: ov.querySelector('[data-mrb-dialog="flashcards"]'),
      body: ov.querySelector('[data-dc-tpl="10328"]'),
      strip: ov.querySelector('[data-hw="strip"]'),
      box: ov.querySelector('[data-hw="answer"]')
    };
  }

  var lastCard = null;
  var wasTyping = false;
  var lastH = 0;

  // A phone keyboard is up when it has taken 100px or more of the screen.
  // Browsers report it two ways: iOS Safari shrinks only the visual
  // viewport; this page's `interactive-widget=resizes-content` (the class
  // view's viewport meta) makes Android Chrome shrink the LAYOUT viewport
  // too, so `innerHeight` follows the keyboard down and innerHeight − visual
  // height reads 0 there. The height to measure against is therefore the
  // tallest layout viewport seen while the box was NOT focused (per width —
  // an orientation change starts over). A desktop window does not shrink on
  // focus: its rest height is its height, the difference is 0, never compact.
  var restH = 0, restW = 0;
  function boxFocused() {
    var a = doc.activeElement;
    return !!(a && a.getAttribute && a.getAttribute("data-hw") === "answer");
  }
  function keyboardUp() {
    var inner = root.innerHeight || 0, w = root.innerWidth || 0;
    if (w !== restW) { restW = w; restH = 0; }
    if (!boxFocused() || inner > restH) { restH = inner; }
    return Math.max(restH, inner) - vv().height >= 100;
  }

  // The taller face's CONTENT height. Both faces are `position:absolute;
  // inset:0`, so their box is the stage's; for one synchronous read each is
  // let go to `height:auto`, then put back (no paint happens in between).
  function contentHeight(face) {
    if (!face) { return 0; }
    var b = face.style.bottom, h = face.style.height;
    face.style.bottom = "auto";
    face.style.height = "auto";
    var n = face.offsetHeight;
    face.style.bottom = b;
    face.style.height = h;
    return n;
  }

  // A long question or answer steps down from Design's size, no lower than
  // 18px, before the face falls back to scrolling (the same rule as
  // student-live.js's fit loop, which then finds nothing to do).
  function shrinkToFit(faceSel, textSel) {
    var face = doc.querySelector(faceSel), text = doc.querySelector(textSel);
    if (!face || !text) { return; }
    var size = parseFloat(root.getComputedStyle(text).fontSize) || 24;
    var guard = 0;
    while (face.scrollHeight > face.clientHeight + 1 && size > 18 && guard++ < 12) {
      size -= 1.5;
      text.style.fontSize = size + "px";
    }
  }

  function fitCard(p, m, typing) {
    var front = p.dialog.querySelector('[data-dc-tpl="10334"]');
    var back = p.dialog.querySelector('[data-dc-tpl="10351"]');
    var learn = p.dialog.getAttribute("data-hw-learn") === "1";
    var dh = p.dialog.getBoundingClientRect().height || m.height;
    var cap = typing ? Math.max(learn ? 96 : 120, (learn ? 0.24 : 0.34) * m.height)
                     : Math.min(420, 0.46 * dh);
    var content = Math.max(contentHeight(front), contentHeight(back));
    // a card is at least 140px tall (120 under a keyboard, where every
    // pixel is the box's)
    var h = Math.round(Math.min(cap, Math.max(typing ? (learn ? 96 : 120) : 140, content)));
    p.dialog.style.setProperty("--hw-card-h", h + "px");
    p.dialog.setAttribute("data-hw-fit", "1");
    if (dh >= 700 && !typing) { p.dialog.setAttribute("data-hw-tall", "1"); }
    else { p.dialog.removeAttribute("data-hw-tall"); }
    shrinkToFit('[data-dc-tpl="10334"]', '[data-dc-tpl="10340"]');
    shrinkToFit('[data-dc-tpl="10351"]', '[data-dc-tpl="10353"]');
  }

  function apply() {
    var p = parts();
    if (!p || !p.strip || !p.dialog) { lastCard = null; wasTyping = false; return; }
    injectCss();
    var m = vv();
    // Pinned to the visual viewport instead of `inset:0`.
    p.ov.style.inset = "auto";
    p.ov.style.left = "0";
    p.ov.style.right = "0";
    p.ov.style.bottom = "auto";
    p.ov.style.top = m.offsetTop + "px";
    p.ov.style.height = m.height + "px";
    p.dialog.style.setProperty("--fc-vh", m.height + "px");
    p.dialog.style.height = "min(var(--fc-vh), 760px)";
    if (p.body) { p.body.style.overflowY = "auto"; }

    // The box shows the text the engine holds for THIS card.
    var H = root.MRBHomework, e = H && H.active;
    if (p.box) {
      var id = p.box.getAttribute("data-hw-card") || "";
      if (id !== lastCard) {
        var want = (e && e.view && e.view().draft) || "";
        if (p.box.value !== want) { p.box.value = want; }
        lastCard = id;
      }
    } else {
      lastCard = null;
    }

    if (p.dialog.querySelector('[data-hw="learn"]')) { p.dialog.setAttribute("data-hw-learn", "1"); }
    else { p.dialog.removeAttribute("data-hw-learn"); }

    var typing = !!(p.box && doc.activeElement === p.box) && keyboardUp();
    if (typing) { p.dialog.setAttribute("data-hw-typing", "1"); }
    else { p.dialog.removeAttribute("data-hw-typing"); }
    fitCard(p, m, typing);
    // ⊕ Sharpen §13.4 — also when the keyboard changes height while the
    // pupil is typing (iOS animates it in; the learn state is taller).
    if (typing && (!wasTyping || m.height !== lastH)) { reveal(); }
    wasTyping = typing;
    lastH = m.height;
  }

  // The row holding Check sits right under the box: bringing IT into view
  // ("nearest" = its foot to the visible foot) shows the box and Check both.
  function scrollBox() {
    var p = parts();
    if (!p || !p.box || doc.activeElement !== p.box) { return; }
    var row = p.ov.querySelector('[data-hw="act"]') || p.box;
    try { row.scrollIntoView({ block: "nearest" }); } catch (e) { /* old engines */ }
  }
  function reveal() {
    scrollBox();
    setTimeout(scrollBox, 300);
  }

  function restore() {
    // The overlay closing takes its element with it; nothing is left to undo.
    lastCard = null; wasTyping = false; lastH = 0;
  }

  root.__MRB_AFTER_DRAW__ = root.__MRB_AFTER_DRAW__ || [];
  root.__MRB_AFTER_DRAW__.push(function () { if (parts()) { apply(); } else { restore(); } });

  function onViewport() { apply(); }
  if (root.visualViewport && root.visualViewport.addEventListener) {
    root.visualViewport.addEventListener("resize", onViewport);
    root.visualViewport.addEventListener("scroll", onViewport);
  }
  root.addEventListener("resize", onViewport);
  doc.addEventListener("focusin", function (ev) {
    if (ev.target && ev.target.getAttribute && ev.target.getAttribute("data-hw") === "answer") { apply(); }
  });
  doc.addEventListener("focusout", function (ev) {
    if (ev.target && ev.target.getAttribute && ev.target.getAttribute("data-hw") === "answer") {
      // Let focus land first: a redraw that replaces the box re-focuses it.
      setTimeout(apply, 0);
    }
  });

  root.MRBFlashcardKeyboard = { apply: apply, vv: vv, keyboardUp: keyboardUp };
})(typeof window !== "undefined" ? window : globalThis);
