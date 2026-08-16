/* WIRE: no new line in wireInstruments(). `wireTriangle(root)` is already
   called there (beside `wireCoverBar(root)`); REPLACE the existing
   `wireTriangle` with the one below. `wireCoverBar` is not touched, which is
   why c2-06's bar keeps its own contract. */

  /* ── cover-triangle · TRIANGLE variant (b1-02 #s-formula, b2-04's rule) ──

     ⚖️ TWO INTERACTION CONTRACTS, AND THE PAYLOAD PICKS ONE.

       TOGGLE (b1-02, the default and today's behaviour) — pressing the
       covered cell again UNCOVERS it. Right for a triangle being explored:
       a student wants to see the whole relationship back.

       RADIO (b2-04, `data-cover-mode="radio"`) — one cell is always covered
       and pressing the covered one changes nothing. Right for a block whose
       whole demand is "cover the one you want": an uncovered triangle asks
       nothing, and this lesson's every question solves for the same unknown,
       so it opens with that one already covered.

     A triangle with no `data-cover-mode` keeps the toggle exactly as it is
     today, which is the b1-02 guarantee.

     ⚠️ EMIT-BOTH-SHOW-ONE, for the results as well as the notes. Every
     arrangement and every sentence is already in the document and this
     function only swaps which pair is not hidden. Nothing is assembled from
     an attribute, so `÷`, `×` and the em dashes survive — the failure mode
     the bar variant's `textContent` route cannot rule out.

     ⚖️ NOTHING ANIMATES and nothing counts, so `prefers-reduced-motion` has
     nothing to degrade here: the cover's own 0.16s opacity fade is a CSS
     transition and the stylesheet's standing reduced-motion block already
     covers it. The reduced-motion experience is the complete one.

     ⚠️ NOT A RAIL STOP. There is no `markStage` call in this function and
     there must not be one: MRB-208 has the rail carrying only sections that
     require the student to do something, and this block is read. */
  function wireTriangle(root) {
    each(root.querySelectorAll("[data-triangle]"), function (tri) {
      var btns = toArray(tri.querySelectorAll(".ks3-tri-btn"));
      var notes = toArray(tri.querySelectorAll(".ks3-tri-note"));
      var results = toArray(tri.querySelectorAll(".ks3-tri-result"));
      var radio = tri.getAttribute("data-cover-mode") === "radio";

      function show(key) {
        tri.setAttribute("data-covered", key);
        each(btns, function (x) {
          x.setAttribute("aria-pressed",
            x.getAttribute("data-cover") === key ? "true" : "false");
        });
        each(notes, function (n) {
          setHidden(n, n.getAttribute("data-note") !== key);
        });
        each(results, function (r) {
          setHidden(r, r.getAttribute("data-result") !== key);
        });
      }

      function clear() {
        tri.removeAttribute("data-covered");
        each(btns, function (x) { x.setAttribute("aria-pressed", "false"); });
        each(notes, function (n) { setHidden(n, true); });
        each(results, function (r) { setHidden(r, true); });
      }

      each(btns, function (b) {
        b.addEventListener("click", function () {
          var key = b.getAttribute("data-cover");
          // The radio never uncovers. Pressing the covered cell is a no-op
          // rather than a state change, which is what keeps the figure and
          // the reading beside it always agreeing.
          if (!radio && tri.getAttribute("data-covered") === key) {
            clear();
            return;
          }
          show(key);
        });
      });
    });
  }
