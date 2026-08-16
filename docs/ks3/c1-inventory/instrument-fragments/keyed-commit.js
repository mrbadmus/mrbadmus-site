/* WIRE: each(root.querySelectorAll("[data-keyedblock]"), wireKeyedCommit);
   — add to wireInstruments(), in the C1 group. Uses each / toArray /
   setHidden / markStage, all already in scope. */

  /* ── keyed-commit (c1-06 #s-verdict, c1-03 #s-bubble) ──
     Four options, each carrying its own answer. The panel's first paragraph
     is the one the student earned; the rest is what everybody reads.

     Emit-both-show-one: all four replies are in the document and hidden, and
     this function swaps which one is shown. Nothing is assembled from an
     attribute, so `<em>`, em dashes and right single quotes survive intact —
     which matters here more than usual, because every reply is a sentence
     about what scientists actually did.

     ⚠️ R3 — NOTHING MARKS. The chosen option takes the ordinary chosen
     treatment and nothing else, and the panel opens on whatever was chosen.
     There is no `data-correct` anywhere in this instrument and there must not
     be: `answer_index` is checked at build time and never reaches the page.

     The choice stays changeable. The block is a commitment, not a question:
     a student who changes their mind reads the other answer, which is the
     block working rather than a leak. */
  function wireKeyedCommit(sec) {
    var wrap = sec.querySelector("[data-keyed]");
    if (!wrap) { return; }
    var opts = toArray(wrap.querySelectorAll(".ks3-option"));
    var panel = wrap.querySelector("[data-reveal]");
    var replies = toArray(wrap.querySelectorAll(".ks3-keyed-reply"));
    if (!opts.length || !panel) { return; }

    each(opts, function (btn) {
      btn.addEventListener("click", function () {
        var i = btn.getAttribute("data-i");
        each(opts, function (b) {
          b.setAttribute("aria-pressed",
            b.getAttribute("data-i") === i ? "true" : "false");
        });
        each(replies, function (p) {
          setHidden(p, p.getAttribute("data-reply") !== i);
        });
        if (panel.hasAttribute("hidden")) {
          setHidden(panel, false);
          // Announced for screen-reader users, who would otherwise get no
          // signal that a panel of new prose appeared below the buttons.
          panel.setAttribute("role", "status");
        }
        markStage(sec, true);
      });
    });
  }
