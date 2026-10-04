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
    // ⊕ Y Unit 1 — the SAME cue, top edge, for the learn step's "the
    // question is still there, scroll up for it" case: once the card is
    // scrolled down to show the model answer, content is hidden ABOVE the
    // fold too, not only below. `markOverflow()` now checks both edges of
    // whatever scroll position the card is actually at (it used to assume
    // the card always starts at scrollTop 0, so "hidden above" never
    // applied before this).
    D + '[data-hw-fit] [data-card-fit][data-hw-overflow-top="1"]::before{content:"";' +
      'position:absolute;left:0;right:0;top:0;height:22px;border-radius:22px 22px 0 0;' +
      'pointer-events:none;background:linear-gradient(to top,transparent,var(--hw-fade-top))}' +
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
    //
    // ⊕ Y Unit 1 — no `min-height` here any more (it used to pin 96px,
    // which would have overridden a deliberately smaller `--hw-box-h` the
    // moment `fitCard()` shrinks the box's floor to 72px to keep a long
    // model answer fully visible — see fitCard()'s comment). The real
    // floor is enforced in JS (`Math.max(boxFloor, …)` in `fitBox()`); this
    // CSS fallback (96px) only ever paints before the first `apply()` call.
    D + '[data-hw-fit][data-hw-typing="1"] [data-hw="answer"]{height:var(--hw-box-h,96px);min-height:0}' +
    // ⊕ Y Unit 1 (Mide, phone report, 4 Oct 2026) — "it isn't obvious where
    // to type" + "unmistakably an input in both themes": the box's REST
    // border moved to `--pg-muted` at the markup (student_rulings.py,
    // measured 6.99:1 light / 6.28:1 dark against the box's own
    // `--pg-card` fill — the old `--pg-rule-strong` was 2.05/1.7:1, faint
    // cream on cream). This adds the part an inline style cannot: a
    // FOCUSED treatment, the same in every state (normal card or the
    // learn step reuse one box) and both themes — the border flips to the
    // accent, a soft accent-tinted ring appears outside it, and the caret
    // itself is drawn in the accent. `!important` is required: an inline
    // `style="border:…"` attribute outranks any selector here on
    // specificity alone, `:focus` or not.
    D + ' [data-hw="answer"]:focus{outline:none!important;' +
      'border-color:var(--pg-accent-text)!important;' +
      'box-shadow:0 0 0 3px var(--pg-tint)!important;' +
      'caret-color:var(--pg-accent-text)!important}' +
    // ⊕ Y Unit 1 — under a real keyboard, in the learn step, the ANSWER is
    // primary: the question steps down (smaller, the card's muted ink) so the room it
    // gives up can go to the model answer. Scoped to typing+learn only —
    // the question's normal size (its own `shrinkToFit()` loop, elsewhere)
    // is untouched at rest, on desktop, and for the plain write step.
    // ⊕ Y review — the CARD's muted ink (`--b-muted`, the "ANSWER"
    // label's own colour), never the page's: `--pg-muted` is a colour for
    // the cream page and read 1.8:1 on the dark card.
    D + '[data-hw-typing="1"][data-hw-learn="1"] [data-dc-tpl="10340"]{' +
      'font-size:15px!important;line-height:1.3!important;' +
      'font-weight:400!important;color:var(--b-muted)!important}' +
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
  // ⊕ Y review — the learn step's card scroll (see fitCard()).
  var learnKey = null, learnScroll = 0;
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
  // most one can straddle a single cut) whose box straddles it. Two
  // directions (⊕ Y Unit 1 added `dir`; the original caller — a card's
  // BOTTOM edge, always measured from scrollTop 0 — is `dir="floor"` and is
  // unchanged by the default):
  //   "floor" (default) — snap DOWN to that line's own top: hide the whole
  //     half-shown line rather than show any fraction of it. Right for a
  //     BOTTOM edge, where shrinking the visible window is the safe
  //     direction.
  //   "ceil"  — snap FORWARD to that line's own BOTTOM: hide the line
  //     entirely by scrolling PAST it rather than reveal it whole. Right for
  //     a scrolled window's TOP edge (fitCard()'s learn-under-keyboard case):
  //     moving scrollTop forward by a few px never reduces how much of the
  //     model answer stays visible, where floor's direction (moving it back)
  //     would widen the window and could push the answer's own bottom below
  //     the fold.
  // If no line straddles `h` (the cut already falls on a line boundary, or
  // beyond all content), `h` is returned unchanged either way.
  function snapToLineBoundary(face, h, dir) {
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
            // ⊕ Y review — any line that STARTS above the cut straddles it,
            // however little (a 0.4px overlap used to slip through ±0.5).
            if (top < out && bottom > out + 0.5) {
              out = dir === "ceil" ? Math.ceil(bottom) : Math.floor(top);
            }
          }
        }
        return;
      }
      for (var j = 0; j < kids.length; j++) { walk(kids[j]); }
    })(face);
    face.style.bottom = b;
    face.style.height = fh;
    return Math.max(dir === "ceil" ? 0 : 40, out);
  }

  // The full-content metrics of the learn block ([data-hw="learn"], the
  // rule + "ANSWER" label + model-answer text that now lives INSIDE the
  // front face — student_rulings.py's INSERT_AT(10334,10340)): its own
  // height, and its top/bottom offset from the FACE's own content top (not
  // the viewport — `front` is `position:absolute;inset:0`, so `bottom`/
  // `height` are let go to `auto` for one synchronous read, same trick
  // `contentHeight()` and `snapToLineBoundary()` above already use).
  function learnMetrics(front, learnEl) {
    if (!front || !learnEl) { return null; }
    var b = front.style.bottom, fh = front.style.height;
    front.style.bottom = "auto";
    front.style.height = "auto";
    var top0 = front.getBoundingClientRect().top;
    var lr = learnEl.getBoundingClientRect();
    // The model answer's own text (the block's last child; the rule and the
    // "ANSWER" label sit above it).
    var tx = learnEl.lastElementChild ? learnEl.lastElementChild.getBoundingClientRect() : lr;
    var content = front.offsetHeight;
    front.style.bottom = b;
    front.style.height = fh;
    return { top: lr.top - top0, bottom: lr.bottom - top0, height: lr.height, content: content,
             textTop: tx.top - top0 };
  }

  // The scroll cue (CSS, above): a fade in the VISIBLE face's own current
  // paint colour, shown only while that face genuinely has more below the
  // fold. `cardFit` (the stage) carries the attribute and the colour, not
  // the face itself — see the CSS comment for why.
  // ⊕ Y Unit 1 — now checks BOTH edges against the face's REAL scrollTop,
  // not just "is there more below" from an assumed scrollTop 0. The learn
  // step under a keyboard can legitimately start scrolled down (showing
  // the model answer, hiding the question above it — see fitCard()), and
  // that needs its OWN cue at the top, in the same live paint colour.
  function markOverflow(cardFit, face) {
    if (!cardFit) { return; }
    if (face && face.scrollHeight > face.clientHeight + 1) {
      var cs = root.getComputedStyle(face), bg = cs.backgroundColor;
      // ⊕ Y review — only TEXT counts as "more": a scroll that hides
      // nothing but the face's own padding draws no fade (it used to dim
      // the model answer's last line at 360px with nothing under it).
      var padB = parseFloat(cs.paddingBottom) || 0, padT = parseFloat(cs.paddingTop) || 0;
      if (face.scrollTop + face.clientHeight < face.scrollHeight - padB - 1) {
        cardFit.setAttribute("data-hw-overflow", "1");
        cardFit.style.setProperty("--hw-fade", bg);
      } else {
        cardFit.removeAttribute("data-hw-overflow");
        cardFit.style.removeProperty("--hw-fade");
      }
      if (face.scrollTop > padT + 1) {
        cardFit.setAttribute("data-hw-overflow-top", "1");
        cardFit.style.setProperty("--hw-fade-top", bg);
      } else {
        cardFit.removeAttribute("data-hw-overflow-top");
        cardFit.style.removeProperty("--hw-fade-top");
      }
    } else {
      cardFit.removeAttribute("data-hw-overflow");
      cardFit.style.removeProperty("--hw-fade");
      cardFit.removeAttribute("data-hw-overflow-top");
      cardFit.style.removeProperty("--hw-fade-top");
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
    var learnEl = front ? front.querySelector('[data-hw="learn"]') : null;
    var boxFloor = 96;
    if (typing && learnEl && p.write && p.act && p.body) {
      // ⊕ Y Unit 1 (Mide, phone report, 4 Oct 2026: "with the keyboard up
      // the pupil must be able to SEE THE ANSWER … it's meant to show they
      // are actually revising"). THE ANSWER IS PRIMARY under a keyboard, in
      // the learn step specifically: it outranks the box's 96px floor,
      // which outranks the question staying on screen at all.
      //
      //   1. can the WHOLE learn block (rule + "ANSWER" + the model answer
      //      text) be shown with the box still ≥96px? Size the card to
      //      exactly that need (never more — any slack goes to the box).
      //   2. if not, can it be shown by letting the box shrink to a ~2-line
      //      floor (72px)? Same again at that smaller floor.
      //   3. if even that isn't enough, the card takes everything up to the
      //      72px-floor cap, the box is pinned at 72px, and the answer's
      //      OWN FIRST LINE sits at the card's visible top — never a half
      //      line (see the ceil-snap below) — with the rest reachable by
      //      scrolling the card.
      //
      // In every case the question is what gives way (scrolled off, in
      // whole lines), never the answer and never the box below its floor.
      var cardFit = p.dialog.querySelector('[data-card-fit]');
      var cardTop = cardFit ? cardFit.getBoundingClientRect().top : 0;
      var bodyBottom = p.body.getBoundingClientRect().bottom;
      var bodyGap = parseFloat(root.getComputedStyle(p.body).rowGap) || 10;
      var writeGap = parseFloat(root.getComputedStyle(p.write).rowGap) || 10;
      var actH = p.act.getBoundingClientRect().height;
      var avail = bodyBottom - cardTop - bodyGap - writeGap - actH - 6;
      var lm = learnMetrics(front, learnEl);
      var learnH = lm ? lm.height : 0;
      var maxCardFullBox = Math.max(60, avail - 96);
      // The answer's own text plus the face's bottom padding.
      var textH = lm ? lm.bottom - lm.textTop + (parseFloat(root.getComputedStyle(front).paddingBottom) || 0) : 0;
      if (learnH <= maxCardFullBox) {
        h = Math.round(Math.min(content, maxCardFullBox));
      } else if (textH <= maxCardFullBox) {
        // ⊕ Y review — the rule and "ANSWER" label give way before the
        // box drops below 96: the answer text alone fits beside a full box.
        h = Math.round(textH);
      } else {
        boxFloor = 72;
        var maxCardShrunkBox = Math.max(60, avail - 72);
        // Sized to the answer TEXT (it is what starts at the top here), so
        // the card can always scroll far enough to hide the label above it.
        h = Math.round(Math.min(textH, maxCardShrunkBox));
      }
      p.dialog.style.setProperty("--hw-card-h", h + "px");
      p.dialog.setAttribute("data-hw-fit", "1");
      p.dialog.removeAttribute("data-hw-tall");
      // The scroll position itself: biased to show the WHOLE learn block
      // when `h` is tall enough for it (anchored to its bottom — any extra
      // room above shows as much of the question's tail as fits), or to its
      // own top otherwise (so the answer's first line is what's visible,
      // never its middle).
      if (lm) {
        var fits = h >= Math.round(learnH) - 0.5;
        // ⊕ Y review — when the whole block does not fit, it is the answer
        // TEXT that starts at the card's top, not the rule and "ANSWER"
        // label above it (at 360px those two lines were what pushed the
        // answer's last line under the fold).
        var desired = fits ? Math.max(0, lm.bottom - h) : lm.textTop;
        var maxScroll = Math.max(0, lm.content - h);
        desired = Math.min(desired, maxScroll);
        // TOP edge: never a half-shown line at the fold — push forward past
        // one if the candidate straddles it (never backward: that would
        // widen the window and could cut the answer's own bottom instead).
        // Whole pixels: scrollTop is (a 154.5 became 155 and shifted every
        // line half a pixel past the bottom snap below).
        var snappedTop = Math.ceil(Math.min(snapToLineBoundary(front, desired, "ceil"), maxScroll));
        // BOTTOM edge: same existing rule — shrink `h` if it still cuts a
        // line (safe: `fits` already guarantees enough room when true, so
        // this only ever bites in the "doesn't fit" branch).
        var bottomY = snappedTop + h;
        var snappedBottom = snapToLineBoundary(front, bottomY, "floor");
        if (snappedBottom < bottomY) {
          h = Math.max(40, Math.round(snappedBottom - snappedTop));
          p.dialog.style.setProperty("--hw-card-h", h + "px");
        }
        // ⊕ Y Unit 1 debugging note, kept because the trap is easy to
        // reintroduce: `scrollTop` is set LAST, after every
        // `snapToLineBoundary()`/`learnMetrics()` call above. Each of those
        // temporarily sets `front.style.height = "auto"` to measure natural
        // content size (the same trick `contentHeight()` uses) — which
        // REMOVES the clipping that makes `front` scrollable at all for
        // that instant, and a browser clamps `scrollTop` to 0 the moment an
        // element stops overflowing. Restoring `style.height` afterward
        // does not restore the scrollTop that got clamped away under it.
        // Setting it here, once, after all such measuring is done, is what
        // makes the assignment stick.
        // ⊕ Y review — set the answer-first position only when the layout
        // is NEW (another card, entering the learn step, or the card's
        // height changing as the keyboard settles). Every other apply() —
        // and iOS fires visualViewport scroll events all the time while the
        // pupil types — puts back wherever the pupil last scrolled the card
        // themselves (`learnScroll`, kept by the scroll listener below), so
        // scrolling up to re-read the question is never snapped away. The
        // measuring above zeroes scrollTop and a redraw rebuilds the face,
        // so the remembered NUMBER is the source, never the element.
        var key = (p.box ? p.box.getAttribute("data-hw-card") || "" : "") + "|" + h;
        if (key !== learnKey) {
          learnKey = key;
          learnScroll = snappedTop;
        }
        front.scrollTop = Math.min(learnScroll, maxScroll);
      }
      markOverflow(cardFit, front);
      return { h: h, boxFloor: boxFloor };
    }
    if (typing && p.write && p.act && p.body) {
      var cardFit2 = p.dialog.querySelector('[data-card-fit]');
      var cardTop2 = cardFit2 ? cardFit2.getBoundingClientRect().top : 0;
      var bodyBottom2 = p.body.getBoundingClientRect().bottom;
      var bodyGap2 = parseFloat(root.getComputedStyle(p.body).rowGap) || 10;
      var writeGap2 = parseFloat(root.getComputedStyle(p.write).rowGap) || 10;
      var actH2 = p.act.getBoundingClientRect().height;
      var minBox = 96; // ~3 lines at 17px/1.4
      var avail2 = bodyBottom2 - cardTop2 - bodyGap2 - writeGap2 - actH2 - 6;
      var maxCardH = Math.max(60, avail2 - minBox);
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
      var snapped = snapToLineBoundary(visFace, visFace.clientHeight, "floor");
      if (snapped < h) {
        h = Math.max(40, snapped);
        p.dialog.style.setProperty("--hw-card-h", h + "px");
      }
    }
    markOverflow(p.dialog.querySelector('[data-card-fit]'), visFace);
    return { h: h, boxFloor: boxFloor };
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
  function fitBox(p, typing, boxFloor) {
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
    // floor is `boxFloor` (96 normally; `fitCard()` passes 72 — ⊕ Y Unit 1
    // — on the learn step's own "answer can't fully fit even at 96"
    // escape hatch, never otherwise) because `fitCard()` now only ever
    // leaves the card up to `avail − boxFloor`, so a long card's leftover
    // is exactly that floor and a short card's is whatever `fitCard()`
    // didn't need.
    var avail = bodyBottom - writeTop - actH - gap - 6;
    var h = Math.max(boxFloor || 96, Math.min(500, Math.round(avail)));
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

    // ⊕ Y Unit 1 — the one-shot backstop for the "I don't know" tap
    // (student_rulings.py's hwIdk, which focuses the box itself and sets
    // this flag before the engine's state change). The component's own
    // path-based refocus (student-runtime.js) should already land back on
    // the box — this only fires if something else left it elsewhere.
    // Consumed exactly once per tap, regardless, so it can never fire on a
    // RESUMED learn step (a reload, or ‹ Back then Forward again, both of
    // which show `[data-hw="learn"]` with no gesture and never set the
    // flag) — that must not steal focus, per the brief.
    if (root.__MRB_FC_LEARN_FOCUS__) {
      root.__MRB_FC_LEARN_FOCUS__ = false;
      if (p.box && doc.activeElement !== p.box && p.box.focus) {
        try { p.box.focus({ preventScroll: true }); } catch (e) { /* old engines */ }
      }
    }

    var typing = !!(p.box && doc.activeElement === p.box) && keyboardUp();
    if (typing) { p.dialog.setAttribute("data-hw-typing", "1"); }
    else { p.dialog.removeAttribute("data-hw-typing"); }
    var fit = fitCard(p, m, typing);
    fitBox(p, typing, fit && fit.boxFloor);
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
    lastCard = null; wasTyping = false; lastH = 0; learnKey = null; learnScroll = 0;
  }

  root.__MRB_AFTER_DRAW__ = root.__MRB_AFTER_DRAW__ || [];
  root.__MRB_AFTER_DRAW__.push(function () { if (parts()) { apply(); } else { restore(); } });

  function onViewport() { apply(); }
  if (root.visualViewport && root.visualViewport.addEventListener) {
    root.visualViewport.addEventListener("resize", onViewport);
    root.visualViewport.addEventListener("scroll", onViewport);
  }
  root.addEventListener("resize", onViewport);
  // ⊕ Y review — remember where the pupil scrolls the learn step's card
  // (capture phase: scroll does not bubble). The face is rebuilt on every
  // redraw, so the position lives here, not on the element.
  doc.addEventListener("scroll", function (ev) {
    var t = ev.target;
    if (t && t.getAttribute && t.getAttribute("data-dc-tpl") === "10334" &&
        t.closest && t.closest(D + '[data-hw-learn="1"][data-hw-typing="1"]')) {
      learnScroll = t.scrollTop;
    }
    // The fades follow whatever the pupil scrolls to, on any homework card.
    if (t && t.getAttribute && (t.getAttribute("data-dc-tpl") === "10334" || t.getAttribute("data-dc-tpl") === "10351") &&
        t.closest && t.closest(D + "[data-hw-fit]")) {
      markOverflow(t.closest("[data-card-fit]"), t);
    }
  }, true);
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
