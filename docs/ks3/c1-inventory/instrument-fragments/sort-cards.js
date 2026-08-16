/* WIRE: each(root.querySelectorAll("[data-sortcardsblock]"), wireSortCards);   // inside wireInstruments()

   Splice into shared/ks3.js beside the other C1 instruments. */

  /* ── sort-cards (c1-03 #s-think) ──
     Four everyday events and the word that fits each one.

     ⚠️ NOT one-shot. `job-sort` and `verdict-cards` disable a row the
     instant it is decided, because their reveal is the answer. This one
     stays open on purpose: Design's page lets a student change the word
     and follow the card as it changes, and the block's own lede says
     "the sorting is the point, not the score". A locked card would make
     it a test, which is what that sentence says it is not — and R3's own
     rule for an activity option is that it "stays enabled so the student
     can change their mind".

     ⚖️ The stage ticks on all four DECIDED, right or wrong, and it never
     unticks — a card that is re-answered was already answered. */
  function wireSortCards(sec) {
    var wrap = sec.querySelector("[data-sortcards]");
    if (!wrap) { return; }
    var cards = toArray(wrap.querySelectorAll(".ks3-sortcards-card"));
    var total = parseInt(wrap.getAttribute("data-total"), 10) || cards.length;
    var closer = wrap.querySelector("[data-sortcards-close]");
    var decided = {};

    function count() {
      var n = 0, k;
      for (k in decided) { if (decided[k]) { n += 1; } }
      return n;
    }

    each(cards, function (card) {
      var opts = toArray(card.querySelectorAll(".ks3-sortcards-opt"));
      var right = card.querySelector('[data-note="right"]');
      var wrong = card.querySelector('[data-note="wrong"]');
      var answer = card.getAttribute("data-answer");
      each(opts, function (btn) {
        btn.addEventListener("click", function () {
          var choice = btn.getAttribute("data-choice");
          var ok = choice === answer;
          each(opts, function (b) {
            b.setAttribute("aria-pressed", b === btn ? "true" : "false");
          });
          // Emit-both-show-one: both authored notes are already in the
          // document and one of them is unhidden. Nothing is composed.
          setHidden(right, !ok);
          setHidden(wrong, ok);
          // One attribute carries the card's whole marked state, so the
          // border rule lives in CSS and can be ruled on there.
          card.setAttribute("data-verdict", ok ? "right" : "wrong");
          decided[card.getAttribute("data-card")] = true;
          var n = count();
          setCount(sec, n);
          if (n >= total) {
            if (closer) { setHidden(closer, false); }
            markStage(sec, true);
          }
        });
      });
    });
  }
