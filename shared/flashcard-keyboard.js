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
 *     over 420px) at rest.
 *   · COMPACT MODE ONLY UNDER A REAL KEYBOARD: `innerHeight − visual height
 *     ≥ 100`. A desktop never enters it, so focusing the box moves nothing.
 *     On a phone the dialog is pinned to the visual viewport and the strip
 *     keeps only its headline — what the keyboard forces, nothing more.
 *
 * ⊕ MRB-354 unit B (Mide, 2 Oct 2026, from a phone screenshot: the question
 * card clipped mid-sentence with no visible way to read the rest, the model
 * answer not shown at all, the answer box stuck at two lines, and a dead
 * gap between Check and the keyboard). UNDER A REAL KEYBOARD the card and
 * the box now split the same budget instead of each assuming a fixed share
 * of it: the CARD gets priority, up to its own content height, capped so
 * the box keeps a ~3-line floor (96px, `fitCard()`); the BOX then gets
 * EVERYTHING left down to the Check row, which is that floor on a long
 * card and much more on a short one (`fitBox()`). If the card still
 * overflows after that (and after `shrinkToFit()`'s font step-down), its
 * visible height is snapped to the last WHOLE line of whichever face is
 * showing (`snapToLineBoundary()`) — never a half-cut line at the fold —
 * and a bottom fade in that face's own live paint colour marks it as
 * scrollable (`markOverflow()`, CSS below). None of this touches the REST
 * (no-keyboard) sizing or the desktop `data-hw-tall` growth, both unchanged.
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
    // ⊕ Design port (05) — the empty header row above the strip (node
    // 10321: its eyebrow is blank in every mode, its stack counter blank
    // on a homework) steps aside whenever the strip is drawing its own row
    // with Close in it (`[data-hw="close"]`, student_rulings.py `_hw_close`).
    // `:has()` is load-bearing, not decorative: this stylesheet is injected
    // once and stays on the page, so a plain (unscoped) rule would also hide
    // 10321 later, after the homework closes and the PRACTICE deck opens —
    // where 10321 is Design's own header, showing a real eyebrow/counter.
    // A browser without `:has()` (none the site supports) simply keeps
    // 10321 on screen underneath the new row: the old, safe look, not a
    // missing Close. Not `T`-scoped: this applies at every width.
    D + ':has([data-hw="close"]) [data-dc-tpl="10321"]{display:none!important}' +
    // ── the card: its content's height (Stage D, decision 1) ──
    '.rd[data-mode="ks3"] ' + D + '[data-hw-fit] [data-card-fit],' +
    D + '[data-hw-fit] [data-card-fit]{flex:0 0 auto!important;min-height:0!important;' +
      'height:var(--hw-card-h)!important;max-height:none!important;position:relative}' +
    // ⊕ MRB-354 unit B, commander follow-up (2 Oct 2026) — a visible scroll
    // cue when the card is cut, so a scrollable card never reads as broken.
    // `markOverflow()` sets `data-hw-overflow` and `--hw-fade` (the VISIBLE
    // face's own live `background-color`, read with `getComputedStyle`, not
    // a guessed token) on the STAGE (`[data-card-fit]`), not on the face
    // that scrolls — a fade drawn on the scrolling element would scroll
    // away with the text it is supposed to be covering. The stage never
    // scrolls, so this stays pinned to the card's visible foot, in both
    // themes, because it is built from whatever the face is actually
    // painted with right now rather than from a named CSS variable.
    D + '[data-hw-fit] [data-card-fit][data-hw-overflow="1"]::after{content:"";' +
      'position:absolute;left:0;right:0;bottom:0;height:28px;border-radius:0 0 22px 22px;' +
      'pointer-events:none;background:linear-gradient(to bottom,transparent,var(--hw-fade))}' +
    // ── the answer box gets the room back (decision 3) ──
    D + '[data-hw-fit] [data-hw="answer"]{min-height:64px;height:64px}' +
    D + '[data-hw-fit][data-hw-tall="1"] [data-hw="answer"]{height:auto;min-height:96px}' +
    // ⊕ MRB-354 unit B — under a REAL keyboard on a touch device (`T`,
    // never desktop — see `keyboardUp()`, which is only ever true when a
    // keyboard has actually shrunk the visual viewport), the 64px rule
    // above never applies here: `fitBox()` below measures exactly how much
    // room is left between the write block and the visible foot of the
    // dialog (the real keyboard top, because the dialog's own height
    // already tracks `visualViewport.height`), AFTER `fitCard()` has taken
    // only what it needs, and writes that to `--hw-box-h`. This selector is
    // one attribute more specific than the rule above
    // (`[data-hw-fit][data-hw-typing="1"]` vs `[data-hw-fit]`) so it wins
    // regardless of source order.
    D + '[data-hw-fit][data-hw-typing="1"] [data-hw="answer"]{height:var(--hw-box-h,96px);min-height:96px}' +
    // ⊕ Stage D review — on a tall DESKTOP dialog the box takes the room the
    // card gave back (up to 200px). `data-hw-tall` never changes on focus
    // there (no keyboard), so neither does the box. Mouse-and-keyboard only:
    // a phone's box would otherwise shrink from 200 to 64 as its keyboard rose.
    '@media (hover:hover) and (pointer:fine){' +
      D + '[data-hw-fit][data-hw-tall="1"] [data-hw="write"]{flex:1 1 auto;min-height:0}' +
      D + '[data-hw-fit][data-hw-tall="1"] [data-hw="answer"]{flex:1 1 auto;max-height:200px}}' +
    // ── under a real keyboard only (decision 2) ──
    T + ' [data-hw="strip"]{padding:8px 18px!important;gap:4px!important}' +
    // ⊕ Design port (05) — Close moved from the (now CSS-hidden) header row
    // into the strip's own row, `[data-hw="strip-row"]`: that row, not the
    // bare headline span it used to be keyed on, is the one thing this
    // compact mode keeps (bar/chips/secured/helper/offline/note still go).
    T + ' [data-hw="strip"] > :not([data-hw="strip-row"]){display:none!important}' +
    T + ' [data-dc-tpl="10328"]{padding:12px 18px!important;gap:10px!important}' +
    T + ' [data-dc-tpl="10334"]{padding:14px 18px!important;gap:8px!important}' +
    T + ' [data-dc-tpl="10340"]{font-size:18px!important;line-height:1.3!important}' +
    T + ' [data-dc-tpl="10350"]{display:none!important}' +
    // ⊕ design-port audit, must-fix 3 — Design hides the HOMEWORK tag row
    // (10335: card.tag "HOMEWORK" + the "FROM YOUR WORK" pill) under a
    // keyboard, same as she already hides the topic line (10350, above).
    // Without it, the "I don't know" learn step's model answer — inside
    // THIS SAME card, under a rule below the question — was measured
    // clipped at 390×508 (card 122px, content 141px): the tag row was
    // ~19-30px of the gap between them.
    T + ' [data-dc-tpl="10335"]{display:none!important}' +
    T + ' [data-hw="check"]{min-height:44px!important}' +
    // ⊕ Design port review — Design's `.end-1` is 40px; below 380px "10 of
    // 10 right" wraps onto two lines at that size (measured, not assumed —
    // see the drive), so a narrow phone gets 34px instead. A media query,
    // not an inline width check: `data-hw="end1"`'s inline style can't
    // answer "does this string wrap at this width" on its own, and this
    // rule does not depend on the keyboard (`D`, not `T`).
    '@media (max-width:379px){' + D + ' [data-hw="end1"]{font-size:34px!important}}';
  // ⊕ Design port (05) — the old `[data-hw="learn"] > :last-child{max-height:
  // …22vh}` keyboard rule is GONE: the model answer now lives INSIDE 10334
  // (student_rulings.py, INSERT_AT 10334/10340), which already scrolls its
  // own overflow (`STYLE_EDIT[10334]`) at every width, keyboard or not — one
  // scroll region for the question and the answer together, not a second one
  // nested inside it.

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
      box: ov.querySelector('[data-hw="answer"]'),
      write: ov.querySelector('[data-hw="write"]'),
      act: ov.querySelector('[data-hw="act"]')
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

  // A face's text is drawn in leaf elements (an element with no element
  // children but real text) stacked top to bottom, and a leaf that wraps
  // draws several VISUAL LINES — a `getBoundingClientRect()` on the leaf
  // itself covers all of them as one box, which cannot tell "the fold
  // falls between two of this leaf's own lines" from "the fold falls
  // inside one of them": a leaf's own box is "below the fold" the moment
  // ANY of its lines are, whether or not the cut is clean. `Range
  // .getClientRects()` gives the real, per-VISUAL-LINE boxes the browser
  // actually laid out — no guessed line-height, no arithmetic, so no
  // rounding can reopen the sliver it exists to close. Given a candidate
  // cut `h` (px, from the face's own content top), find the one line (at
  // most one can straddle a single cut) whose box straddles it, and floor
  // the cut to THAT line's own top — hide the whole half-shown line rather
  // than show any fraction of it. If no line straddles `h` (the cut
  // already falls on a line boundary, or beyond all content), `h` is
  // returned unchanged.
  function snapToLineBoundary(face, h) {
    if (!face) { return h; }
    var b = face.style.bottom, fh = face.style.height;
    face.style.bottom = "auto";
    face.style.height = "auto";
    var top0 = face.getBoundingClientRect().top;
    var out = h;
    (function walk(n) {
      if (!n || n.nodeType !== 1) { return; }
      var kids = [];
      for (var i = 0; i < n.childNodes.length; i++) {
        if (n.childNodes[i].nodeType === 1) { kids.push(n.childNodes[i]); }
      }
      if (!kids.length) {
        if (n.textContent && n.textContent.trim()) {
          var rg = doc.createRange();
          rg.selectNodeContents(n);
          var rects = rg.getClientRects();
          for (var k = 0; k < rects.length; k++) {
            var top = rects[k].top - top0, bottom = rects[k].bottom - top0;
            if (top < out - 0.5 && bottom > out + 0.5) { out = Math.floor(top); }
          }
        }
        return;
      }
      for (var j = 0; j < kids.length; j++) { walk(kids[j]); }
    })(face);
    face.style.bottom = b;
    face.style.height = fh;
    return Math.max(40, out);
  }

  // The scroll cue (CSS, above): a fade in the VISIBLE face's own current
  // paint colour, shown only while that face genuinely has more below the
  // fold. `cardFit` (the stage) carries the attribute and the colour, not
  // the face itself — see the CSS comment for why.
  function markOverflow(cardFit, face) {
    if (!cardFit) { return; }
    if (face && face.scrollHeight > face.clientHeight + 1) {
      cardFit.setAttribute("data-hw-overflow", "1");
      cardFit.style.setProperty("--hw-fade", root.getComputedStyle(face).backgroundColor);
    } else {
      cardFit.removeAttribute("data-hw-overflow");
      cardFit.style.removeProperty("--hw-fade");
    }
  }

  function fitCard(p, m, typing) {
    var front = p.dialog.querySelector('[data-dc-tpl="10334"]');
    var back = p.dialog.querySelector('[data-dc-tpl="10351"]');
    var dh = p.dialog.getBoundingClientRect().height || m.height;
    var content = Math.max(contentHeight(front), contentHeight(back));
    var h;
    // ⊕ MRB-354 unit B, commander follow-up — THE CARD GETS PRIORITY. Under
    // a real keyboard, give the card everything up to its own content
    // height, reserving only a ~3-line floor (96px) for the box; `fitBox()`
    // (below) then gives the box whatever is left, which is this floor on
    // a long card and much more on a short one. This replaces the old
    // percentage-of-viewport caps (34%/24%), which reserved a FIXED
    // fraction for the box regardless of whether the box ever used it —
    // exactly the room that went to waste as the dead gap this unit's
    // first pass fixed on the BOX side; this is the CARD side of the same
    // mistake.
    if (typing && p.write && p.act && p.body) {
      var cardFit = p.dialog.querySelector('[data-card-fit]');
      var cardTop = cardFit ? cardFit.getBoundingClientRect().top : 0;
      var bodyBottom = p.body.getBoundingClientRect().bottom;
      var bodyGap = parseFloat(root.getComputedStyle(p.body).rowGap) || 10;
      var writeGap = parseFloat(root.getComputedStyle(p.write).rowGap) || 10;
      var actH = p.act.getBoundingClientRect().height;
      var minBox = 96; // ~3 lines at 17px/1.4
      var avail = bodyBottom - cardTop - bodyGap - writeGap - actH - 6;
      var maxCardH = Math.max(60, avail - minBox);
      h = Math.round(Math.min(content, maxCardH));
    } else {
      var cap = typing ? Math.max(120, 0.34 * m.height) : Math.min(420, 0.46 * dh);
      h = Math.round(Math.min(cap, Math.max(140, content)));
    }
    p.dialog.style.setProperty("--hw-card-h", h + "px");
    p.dialog.setAttribute("data-hw-fit", "1");
    if (dh >= 700 && !typing) { p.dialog.setAttribute("data-hw-tall", "1"); }
    else { p.dialog.removeAttribute("data-hw-tall"); }
    shrinkToFit('[data-dc-tpl="10334"]', '[data-dc-tpl="10340"]');
    shrinkToFit('[data-dc-tpl="10351"]', '[data-dc-tpl="10353"]');

    // Whichever face is actually on screen (homework never flips on its
    // own — `flip` is a no-op until Check turns it — so this only ever
    // matters here because state C genuinely shows the back): if it still
    // overflows after shrinking its font, never leave a half-cut line —
    // snap the card down to the last whole line THAT FACE drew, so the cut
    // itself reads as "more below", and mark the fade cue.
    var flipEl = p.dialog.querySelector('[data-dc-tpl="10333"]');
    var flipped = !!(flipEl && flipEl.getAttribute("data-flip") === "1");
    var visFace = flipped ? back : front;
    if (visFace && visFace.scrollHeight > visFace.clientHeight + 1) {
      var snapped = snapToLineBoundary(visFace, visFace.clientHeight);
      if (snapped < h) {
        h = Math.max(40, snapped);
        p.dialog.style.setProperty("--hw-card-h", h + "px");
      }
    }
    markOverflow(p.dialog.querySelector('[data-card-fit]'), visFace);
    return h;
  }

  // ⊕ MRB-354 unit B — the box's height under a real keyboard, measured
  // rather than guessed. `write` and `act` (Back/I-don't-know/Check) don't
  // move or resize because of this call — only the box's CSS var does — so
  // nothing above it shifts and nothing "lifts" (the standing rule). The
  // dialog's own foot is already the real keyboard top: `apply()` sizes the
  // dialog to `visualViewport.height` before this runs, so `p.body`'s
  // bottom edge (its border-box, unaffected by its own scrollTop) IS that
  // foot. What's left between the write block's top (fixed by now — the
  // strip and the card above it have already taken their final height) and
  // that foot, minus the Back/IDK/Check row and the column's own gap, is
  // exactly the room the box may have without pushing Check under the
  // keyboard — which is the regression STAGE-D-PLAN.md records from the
  // first attempt at this (a `@media(min-height:700px)` guess, which an
  // iPhone always matches whether or not its keyboard is up, because the
  // LAYOUT viewport never shrinks on iOS). This reads real, already-laid-out
  // pixels instead, so it cannot make that mistake.
  function fitBox(p, typing) {
    if (!typing || !p.box || !p.write || !p.act || !p.body) {
      if (p.dialog) { p.dialog.style.removeProperty("--hw-box-h"); }
      return;
    }
    var bodyBottom = p.body.getBoundingClientRect().bottom;
    var writeTop = p.write.getBoundingClientRect().top;
    var actH = p.act.getBoundingClientRect().height;
    var gap = parseFloat(root.getComputedStyle(p.write).rowGap) || 10;
    // 6px of slack so the box's bottom border never sits flush against
    // Check's own, which would read as touching rather than spaced. The
    // floor is 96 (not 64) because `fitCard()` now only ever leaves the
    // card up to `avail − 96`, so a long card's leftover is exactly this
    // floor and a short card's is whatever `fitCard()` didn't need.
    var avail = bodyBottom - writeTop - actH - gap - 6;
    var h = Math.max(96, Math.min(500, Math.round(avail)));
    p.dialog.style.setProperty("--hw-box-h", h + "px");
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
    fitBox(p, typing);
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
