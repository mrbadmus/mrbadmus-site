/* ⊕ MRB-351 PUPIL FLOW — THE ANSWER BOX ABOVE THE PHONE KEYBOARD.
 *
 * docs/mrb351/PUPIL-FLOW.md §6, with review amendments A9 and A10.
 *
 * WHY. The flashcard overlay is `position:fixed;inset:0` and its dialog is
 * `height:min(100%,760px)`. iOS Safari and Android Chrome (108+) shrink only
 * `window.visualViewport` when the keyboard opens, not the layout viewport,
 * so the fixed dialog keeps its full height and the answer box sits under
 * the keyboard. Nothing listened to `visualViewport`. This does.
 *
 * WHAT, while a homework is open (the strip `[data-hw="strip"]` exists):
 *   · the overlay root is pinned to the VISUAL viewport — top = offsetTop,
 *     height = visual height — and the dialog carries `--fc-vh`;
 *   · the dialog body (Design's node 10328) scrolls inside it;
 *   · COMPACT MODE while the answer box has focus: the dialog gets
 *     `data-hw-typing="1"`, and the rules below shrink the card and hide
 *     everything in the strip but its headline. Every size is `!important`
 *     because the built card carries `_CARD_FIT`'s `!important` min-height
 *     (build_student_port.py) and Design's inline styles (A9);
 *   · the answer box is scrolled into view, and again 300 ms later (iOS
 *     animates the keyboard in).
 *
 * The overlay is REBUILT on every state change (A10), so nothing here is
 * set once: it is all re-derived in `__MRB_AFTER_DRAW__` from
 * `document.activeElement`, and on every `visualViewport` resize/scroll.
 *
 * ⊕ Sharpen (§13.4): in the "I don't know" learn state the dialog also
 * carries `data-hw-learn="1"`, and the card shrinks further to make room
 * for the ANSWER block above the box.
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

  var CSS =
    '[data-mrb-dialog="flashcards"][data-hw-typing="1"] [data-hw="strip"]{padding:8px 18px!important;gap:4px!important}' +
    '[data-mrb-dialog="flashcards"][data-hw-typing="1"] [data-hw="strip"] > :not([data-hw="progress"]){display:none!important}' +
    '[data-mrb-dialog="flashcards"][data-hw-typing="1"] [data-dc-tpl="10328"]{padding:12px 18px!important;gap:10px!important}' +
    '[data-mrb-dialog="flashcards"][data-hw-typing="1"] [data-card-fit]{flex:0 0 auto!important;' +
      'min-height:120px!important;height:max(120px,min(calc(var(--fc-vh) * .34),calc(var(--fc-vh) - 290px)))!important;' +
      'max-height:max(120px,calc(var(--fc-vh) * .34))!important}' +
    '[data-mrb-dialog="flashcards"][data-hw-typing="1"] [data-dc-tpl="10334"]{padding:14px 18px!important;gap:8px!important}' +
    '[data-mrb-dialog="flashcards"][data-hw-typing="1"] [data-dc-tpl="10340"]{font-size:18px!important;line-height:1.3!important}' +
    '[data-mrb-dialog="flashcards"][data-hw-typing="1"] [data-dc-tpl="10350"]{display:none!important}' +
    '[data-mrb-dialog="flashcards"][data-hw-typing="1"] [data-hw="check"]{min-height:44px!important}' +
    // ⊕ Sharpen §13.4 — the "I don't know" learn state adds the ANSWER block
    // between the card and the box: the card gives up the room for it.
    '[data-mrb-dialog="flashcards"][data-hw-typing="1"][data-hw-learn="1"] [data-card-fit]{' +
      'min-height:96px!important;height:max(96px,min(calc(var(--fc-vh) * .24),calc(var(--fc-vh) - 380px)))!important;' +
      'max-height:max(96px,calc(var(--fc-vh) * .24))!important}' +
    '[data-mrb-dialog="flashcards"][data-hw-typing="1"] [data-hw="learn"] > :last-child{' +
      'max-height:calc(var(--fc-vh) * .22)!important;overflow:auto!important}';

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

    var typing = !!(p.box && doc.activeElement === p.box);
    if (typing) { p.dialog.setAttribute("data-hw-typing", "1"); }
    else { p.dialog.removeAttribute("data-hw-typing"); }
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

  root.MRBFlashcardKeyboard = { apply: apply, vv: vv };
})(typeof window !== "undefined" ? window : globalThis);
