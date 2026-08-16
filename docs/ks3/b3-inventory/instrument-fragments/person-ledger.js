/* WIRE: each(root.querySelectorAll("[data-ledgerblock]"), wirePersonLedger);
   — add to wireInstruments(), in the B3 group. Uses each / toArray /
   setHidden / setCount / markStage, all already in scope. */

  /* ═══════════════════════════════════════════════════════════════
     ── person-ledger (b3-03 #s-ledger) — the person is the control ──

     Twelve foods, five eaters, one running total. Build a day, then move
     the person underneath it.

     ⚖️ CHANGING THE PERSON NEVER TOUCHES THE PLATE, and that is the
     whole instrument. The same food is a surplus for one body and a
     shortfall for another with nothing about the food having moved, and
     the match panel says so in words. A "clear on switch" would be tidier
     and would destroy the experiment, so the person tabs deliberately
     touch nothing but the requirement they are compared against.

     ⚖️ MRB-232 — B3'S SIDE OF THE SPLIT. Everything here is intake
     against requirement, in kJ. Nothing converts a unit, derives a joule
     from power and time, or explains what a joule is: that is P2's half
     of `KS3.B.NUT.02`, reached from this lesson by a `references` edge.
     A kJ↔kcal toggle added to this block later would move the seam.

     ⚠️ R3 — NOTHING MARKS. There is no `.ks3-option` in this instrument,
     no correct plate and no score. The bar's three colours are readings
     of a measurement — short, matched, over — and `--ks3-ok` is
     deliberately not one of them: green is the ladder's colour for a
     correct answer and a plate is not an answer.

     Every authored sentence is already in the document and this function
     only changes which is hidden. The three exceptions all quote a live
     number that does not exist until a plate has been built, and each is
     one authored template filled with digits — `_head_counter`'s own
     mechanism, and safe for its reason: none of them carries markup.

     ⚖️ NOTHING RUNS ON A CLOCK. The bar's width and colour move on a CSS
     transition that the stylesheet turns off under
     `prefers-reduced-motion`, and every number is in the document as
     text, so the reduced-motion experience is the complete one (R6).
     ═══════════════════════════════════════════════════════════════ */
  function wirePersonLedger(sec) {
    var wrap = sec.querySelector("[data-ledger]");
    if (!wrap) { return; }
    var bar = wrap.querySelector("[data-bar]");
    var totalEl = wrap.querySelector("[data-total]");
    var balanceEl = wrap.querySelector("[data-balance]");
    var portionEl = wrap.querySelector("[data-portions]");
    var matchEl = wrap.querySelector("[data-match]");
    var clearBtn = wrap.querySelector("[data-ledger-clear]");
    var foods = toArray(wrap.querySelectorAll(".ks3-ledger-food"));
    if (!bar || !totalEl || !balanceEl || !foods.length) { return; }

    var tolerance = (parseInt(wrap.getAttribute("data-tolerance"), 10) || 5) / 100;
    var maxPer = parseInt(wrap.getAttribute("data-max"), 10) || 6;
    var countFmt = wrap.getAttribute("data-count-format") || "×{n}";

    function group(n) { return Number(n).toLocaleString("en-GB"); }

    function fill(el, attr, values) {
      var s = el.getAttribute(attr) || "", k;
      for (k in values) {
        if (Object.prototype.hasOwnProperty.call(values, k)) {
          s = s.split("{" + k + "}").join(String(values[k]));
        }
      }
      return s;
    }

    function paint() {
      var person = wrap.getAttribute("data-person");
      var tab = wrap.querySelector(".ks3-ledger-tab[data-person='" + person + "']");
      var need = tab ? parseInt(tab.getAttribute("data-need"), 10) : 0;
      var total = 0, portions = 0;

      each(foods, function (b) {
        var n = parseInt(b.getAttribute("data-count"), 10) || 0;
        total += n * (parseInt(b.getAttribute("data-kj"), 10) || 0);
        portions += n;
        var label = b.querySelector("[data-count-label]");
        if (label) {
          label.textContent = n > 0 ? countFmt.split("{n}").join(String(n)) : "";
        }
      });

      each(wrap.querySelectorAll(".ks3-ledger-tab[data-person]"), function (b) {
        b.setAttribute("aria-pressed",
          b.getAttribute("data-person") === person ? "true" : "false");
      });
      each(wrap.querySelectorAll("[data-pname], [data-pneed], [data-pwhy]"),
        function (s) {
          var id = s.getAttribute("data-pname") || s.getAttribute("data-pneed")
            || s.getAttribute("data-pwhy");
          setHidden(s, id !== person);
        });

      var diff = total - need;
      var matched = portions > 0 && Math.abs(diff) <= need * tolerance;
      var frac = need ? total / need : 0;
      bar.style.width = Math.min(100, frac * 100).toFixed(1) + "%";
      bar.setAttribute("data-state",
        matched ? "matched" : (frac > 1 + tolerance ? "over" : "short"));

      totalEl.textContent = fill(totalEl, "data-format",
        { total: group(total), need: group(need) });

      if (!portions) {
        balanceEl.textContent = balanceEl.getAttribute("data-empty") || "";
      } else if (matched) {
        balanceEl.textContent = balanceEl.getAttribute("data-matched") || "";
      } else {
        balanceEl.textContent = fill(balanceEl,
          diff > 0 ? "data-surplus" : "data-short",
          { n: group(Math.abs(diff)) });
      }

      if (portionEl) {
        portionEl.textContent = portions
          ? fill(portionEl, "data-format",
              { n: portions, total: group(total) })
          : (portionEl.getAttribute("data-empty") || "");
      }

      if (matchEl) {
        setHidden(matchEl, !matched);
        each(matchEl.querySelectorAll("[data-mhead]"), function (p) {
          setHidden(p, p.getAttribute("data-mhead") !== person);
        });
      }

      setCount(sec, portions);
      markStage(sec, portions > 0);   // `food_on_the_plate`
    }

    each(wrap.querySelectorAll(".ks3-ledger-tab[data-person]"), function (b) {
      b.addEventListener("click", function () {
        // ⚖️ THE PLATE IS NOT TOUCHED. See the header — this is the experiment.
        wrap.setAttribute("data-person", b.getAttribute("data-person"));
        paint();
      });
    });

    each(foods, function (b) {
      b.addEventListener("click", function () {
        var n = (parseInt(b.getAttribute("data-count"), 10) || 0) + 1;
        // Design's own wrap-around: the count runs up to `max` and the next
        // tap clears that food. It is what makes one control both add and
        // remove, and the block's label says so.
        b.setAttribute("data-count", String(n > maxPer ? 0 : n));
        paint();
      });
    });

    if (clearBtn) {
      clearBtn.addEventListener("click", function () {
        each(foods, function (b) { b.setAttribute("data-count", "0"); });
        paint();
      });
    }

    paint();
  }
