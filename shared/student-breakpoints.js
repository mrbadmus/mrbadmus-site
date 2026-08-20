/* ═══════════════════════════════════════════════════════════════════════
   student-breakpoints.js — Design's discrete switches, at runtime.
   GENERATED CONSUMER: the table it applies is `student_switches.json`,
   measured out of Design's own delivery by `student_switches.py`.
   ═══════════════════════════════════════════════════════════════════════

   WHY THIS EXISTS
   ---------------
   Design builds responsiveness two ways, and says so in §6 of both handoff
   notes. Everything CONTINUOUS is a `clamp(min, Ncqw, max)` in the element's
   own inline style, resolved by a container query — correct before any script
   runs and correct at every width in between. Everything DISCRETE is a value
   computed in JavaScript from the measured root width, and those "cannot be
   interpolated".

   The generated pages are a snapshot of Design's rendered DOM taken at 1460px,
   so every discrete value in them is frozen at its desktop setting and no
   amount of resizing moves it. This puts them back.

   DESIGN SWITCHES THREE WAYS, and this handles two and a half of them.
   Measured by driving Design's own file at 360, 390, 820 and 1460:

     1. BY INLINE STYLE — 19 declarations across 16 elements. Reapplied here.
        (Design's own note lists ten and says "there are no others"; the file
        has twelve. The two it omits are the docket's inner grid and its four
        fact rows, and both are genuinely discrete.)
     2. BY TEXT — 1 string. Swapped here, in place, at a recorded depth.
     3. BY PRESENCE — 95 nodes Design renders at desktop and not below: hidden
        here, which is the faithful reproduction of not rendering them. And 52
        nodes Design renders BELOW desktop and not at it, which is the half
        that cannot be done:

     · the assignment's 320px rail (69 nodes incl. 15 marker cells) exists only
       at desktop; the marker strip and readout row (46 nodes) exist only below
       it. Neither is in the snapshot's other state.
     · the class view's `PROD` chip, the name "Ayo", the Settings and Sign out
       links and the work rows' week column exist only at desktop; the work
       rows' mono meta line (`W04 · DUE THU 18:00`) exists only below it.
     · the breadcrumb note reads `AUTUMN TERM · WEEK 04 / 12` at desktop and
       `WK 04 / 12` below.

   A snapshot cannot carry DOM it does not contain. Those 52 nodes are recorded
   in the table's `absent` list, counted onto the root as `data-mrb-absent` so
   the parity gate reads a number rather than an impression, and they close when
   the behaviour is ported and the page renders from data rather than from a
   photograph.

   THE MEASUREMENT METHOD IS DESIGN'S, AND IS NOT TO BE IMPROVED ON
   ---------------------------------------------------------------
   A synchronous read as soon as the DOM is usable, so the first paint is
   already at the right breakpoint; then `resize`, `orientationchange` and
   `visualViewport` listeners, plus a 250ms settle poll for the first six
   seconds to catch font load and scrollbar arrival.

   ⚠️ NO `ResizeObserver`. Design records that one on a `container-type`
   element did not deliver reliably in testing, and asks that it not be
   reintroduced as the only source. It is not reintroduced at all.
*/
(function () {
  "use strict";

  var ROOT_SEL = '.rd[data-mode="ks3"]';

  /* Design's thresholds, and they are MEASURED rather than transcribed.
     Across the 19 switched declarations: 360 and 390 differ in 0 of them
     (Design: "same layout as 390 throughout — no further breakpoint"), 390 and
     820 differ in 3 (the term spine, the work-row grid and the chaser grid —
     exactly the three Design's table splits at tablet), and 820 and 1460
     differ in 16. So three bands, split at 720 and 1024, as drawn. */
  function bandFor(w) {
    if (w >= 1024) { return "1460"; }
    if (w >= 720) { return "820"; }
    return "390";
  }

  /* Every element carrying a `data-dc-tpl`, in document order, keyed the way
     `student_switches.py` keys them: the template index, then which occurrence
     of it this is. That pair is stable across bands because it identifies the
     node in Design's TEMPLATE rather than in the tree — and the tree is
     exactly what changes. */
  function keyed(root) {
    var seen = {}, out = {};
    var els = root.querySelectorAll('[data-dc-tpl]');
    for (var i = 0; i < els.length; i++) {
      var d = els[i].getAttribute('data-dc-tpl');
      seen[d] = (seen[d] || 0) + 1;
      out[d + '#' + seen[d]] = els[i];
    }
    return out;
  }

  /* PRESENCE. Design does not restyle these nodes at a narrower band; it does
     not render them at all. The snapshot was taken at desktop, so it HAS them,
     and hiding is the faithful reproduction of not rendering.

     ⚠️ THE OTHER DIRECTION IS NOT FIXABLE HERE and is not attempted. Nodes
     Design renders only BELOW desktop — the assignment's marker strip and
     readout row, the class view's per-row mono meta line — are not in a
     desktop snapshot and no shim can conjure them. They are recorded in the
     table's "absent" list and asserted by the parity gate so the gap is a
     measured number rather than an impression. */
  function presence(root, hide, band) {
    var map = keyed(root), n = 0;
    for (var k in hide) {
      if (!Object.prototype.hasOwnProperty.call(hide, k)) { continue; }
      var el = map[k];
      if (!el) { continue; }
      var off = hide[k].indexOf(band) > -1;
      if (off) {
        el.setAttribute('data-mrb-off', '1');
        el.style.setProperty('display', 'none', 'important');
        n += 1;
      } else if (el.getAttribute('data-mrb-off')) {
        el.removeAttribute('data-mrb-off');
        el.style.removeProperty('display');
      }
    }
    return n;
  }

  /* TEXT. Design's third discrete mechanism: the breadcrumb note reads
     `AUTUMN TERM · WEEK 04 / 12` at 820 and up and `WK 04 / 12` below, and at
     360px the long one measures 206px inside a 360px page.

     The address is a DEPTH, not a selector. `student_switches.py` found the
     string by walking down a single-child chain from the tpl-bearing element,
     and this walks the identical chain back down and writes the text node's
     `nodeValue`. Design's compiler wraps every interpolation in its own span,
     so writing `textContent` on the outer element would delete that span; this
     leaves the structure exactly as Design rendered it and changes only the
     characters. */
  function texts(root, text, band) {
    var map = keyed(root), n = 0;
    for (var k in text) {
      if (!Object.prototype.hasOwnProperty.call(text, k)) { continue; }
      var want = text[k][band];
      if (want === null || want === undefined) { continue; }
      var el = map[k];
      if (!el) { continue; }
      var cur = el, steps = text[k]._d || 0;
      while (steps-- > 0 && cur && cur.childNodes.length === 1) {
        cur = cur.childNodes[0];
      }
      if (cur && cur.nodeType === 3 && cur.nodeValue !== want) {
        cur.nodeValue = want;
        n += 1;
      }
    }
    return n;
  }

  function apply(root, table, band) {
    var styles = table.styles || {};
    var applied = 0, mismatched = [];
    for (var tpl in styles) {
      if (!Object.prototype.hasOwnProperty.call(styles, tpl)) { continue; }
      var els = root.querySelectorAll('[data-dc-tpl="' + tpl + '"]');
      if (!els.length) { continue; }
      var props = styles[tpl];
      for (var prop in props) {
        if (!Object.prototype.hasOwnProperty.call(props, prop)) { continue; }
        var want = props[prop][band];
        if (want === null || want === undefined) { continue; }
        for (var i = 0; i < els.length; i++) {
          /* ⚠️ THE FIRST PASS CHECKS ITS OWN AIM. `data-dc-tpl` is a template
             index and is unique only within one component's template, so a
             nested design-system component could in principle carry the same
             number. Before the first write, the element's CURRENT value must
             be the desktop value the table recorded — the snapshot was taken
             at 1460, so it must be. If it is not, this row is pointed at the
             wrong element and writing it would move something Design never
             meant to move. Recorded on the root for the gate to read rather
             than thrown, because half-applied is worse than not applied. */
          if (!root.__mrbAimed) {
            var now = els[i].style.getPropertyValue(prop).trim();
            var desktop = String(props[prop]["1460"]).trim();
            if (now && desktop && now !== desktop) {
              mismatched.push(tpl + " " + prop + ": page has " +
                              JSON.stringify(now) + ", table expected " +
                              JSON.stringify(desktop));
              continue;
            }
          }
          els[i].style.setProperty(prop, want);
          applied += 1;
        }
      }
    }
    var hidden = presence(root, table.hide || {}, band);
    var swapped = texts(root, table.text || {}, band);
    root.__mrbAimed = true;
    root.setAttribute("data-mrb-band", band);
    root.setAttribute("data-mrb-applied", String(applied));
    root.setAttribute("data-mrb-hidden", String(hidden));
    root.setAttribute("data-mrb-text", String(swapped));
    /* The nodes Design renders at this band that this page does not have. Put
       on the root as a NUMBER so the parity gate reads a fact rather than
       inferring one from a screenshot. */
    root.setAttribute("data-mrb-absent", String(countAbsent(table, band)));
    if (mismatched.length) {
      root.setAttribute("data-mrb-mismatch", String(mismatched.length));
      if (window.console && console.error) {
        console.error("student-breakpoints: " + mismatched.length +
                      " switch row(s) did not match the page they aim at:\n  " +
                      mismatched.join("\n  "));
      }
    }
    return applied;
  }

  function countAbsent(table, band) {
    var absent = table.absent || {}, n = 0;
    for (var k in absent) {
      if (Object.prototype.hasOwnProperty.call(absent, k) &&
          absent[k].indexOf(band) > -1) { n += 1; }
    }
    return n;
  }

  function start(table) {
    var root = document.querySelector(ROOT_SEL);
    if (!root || !table) { return; }
    var last = null;

    function tick() {
      /* The ROOT's width, not the window's — the root is the container the
         `clamp(…cqw…)` literals resolve against, and Design's own measurement
         reads the same box. On a page with a scrollbar the two differ by
         15px, which is the wrong side of no threshold today and would be the
         wrong side of one eventually. */
      var w = Math.round(root.getBoundingClientRect().width) ||
              document.documentElement.clientWidth;
      var band = bandFor(w);
      if (band !== last) { last = band; apply(root, table, band); }
    }

    tick();                                  /* before first paint if we can */

    window.addEventListener("resize", tick, {passive: true});
    window.addEventListener("orientationchange", tick, {passive: true});
    if (window.visualViewport) {
      window.visualViewport.addEventListener("resize", tick, {passive: true});
    }
    /* The settle poll: fonts arriving and a scrollbar appearing both change
       the root's width without firing anything reliable. Six seconds at 250ms
       is Design's, and it stops rather than running for the life of the page. */
    var polls = 0;
    var timer = setInterval(function () {
      tick();
      if (++polls >= 24) { clearInterval(timer); }
    }, 250);
  }

  window.MrBadmusStudentBreakpoints = {
    start: start, bandFor: bandFor, ROOT_SEL: ROOT_SEL
  };

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", function () {
      if (window.__MRB_SWITCHES__) { start(window.__MRB_SWITCHES__); }
    });
  } else if (window.__MRB_SWITCHES__) {
    start(window.__MRB_SWITCHES__);
  }
})();
