/* WIRE: each(root.querySelectorAll("[data-plateblock]"), wireBandCommit);
   — add to wireInstruments(), in a new B3 group. Uses each / toArray /
   setHidden / setCount / markStage, all already in scope. */

  /* ═══════════════════════════════════════════════════════════════
     ── band-commit (b3-01 #s-plate) — commit all seven, then open ──

     Seven nutrients, three amount bands, one reveal that is locked until
     every one of the seven has been placed.

     ⚖️ THE LOCK IS THE LESSON. The block's own lede says it: *a guess you
     did not make cannot be wrong, and a guess that is never wrong teaches
     you nothing.* Opening a row at a time — which is what `job-sort` does
     and what this looks like from a distance — would let a student read
     row one's answer before committing on row two, and the argument of
     the block is that the SPREAD is the surprise. Nobody is surprised by
     a spread they were shown a seventh at a time.

     ⚖️ THE ALL-SAME BRANCH IS THE POINT OF THE VERDICT. A student who
     puts all seven in one band is told so, in their own answer. That is
     the only place in the lesson where "balanced means equal amounts" is
     named back rather than argued against in the abstract, and it is why
     the branch is chosen here before the score is: a 0-of-7 all-same day
     and a 0-of-7 scattered day are different mistakes and get different
     sentences.

     ⚠️ R3 — NOTHING MARKS A CONTROL. The band buttons are not
     `.ks3-option`, they never gain a correct or wrong class, and once the
     answers are open the chosen one keeps exactly the treatment it had
     while the other two dim. What changes is the ROW and the words in its
     why panel. There is no `--ks3-ok`, no green, no drawn ✓ and no ✕
     anywhere in this instrument, and nothing here may grow one.

     Emit-both-show-one: every why panel, both band verdicts per row and
     all three closing branches are already in the document. This function
     only ever changes which of them is hidden — no authored sentence is
     assembled here, so the em dashes and the right single quotes survive.

     ⚖️ NOTHING ANIMATES and nothing runs on a clock, so
     `prefers-reduced-motion` has nothing to degrade and the reduced-motion
     experience is the complete one.
     ═══════════════════════════════════════════════════════════════ */
  function wireBandCommit(sec) {
    var wrap = sec.querySelector("[data-plate]");
    if (!wrap) { return; }
    var rows = toArray(wrap.querySelectorAll(".ks3-plate-row"));
    var openBtn = wrap.querySelector("[data-plate-open]");
    var countEl = wrap.querySelector("[data-plate-count]");
    var verdict = wrap.querySelector("[data-plate-verdict]");
    var total = parseInt(wrap.getAttribute("data-total"), 10) || rows.length;
    if (!rows.length || !openBtn || !verdict) { return; }

    var picks = {};       // row index -> band id
    var opened = false;

    function committed() {
      var n = 0, k;
      for (k in picks) {
        if (Object.prototype.hasOwnProperty.call(picks, k)) { n += 1; }
      }
      return n;
    }

    /* The block-head readout ("3 of 7 set") and the foot readout ("3 of 7
       committed") are two different sentences about the same number, and
       Design draws both. `setCount` owns the first; the second has its own
       format because it also has a bespoke DONE string ("Opened") that the
       count shape has no slot for. */
    function paintCount() {
      var n = committed();
      setCount(sec, n);
      if (!countEl) { return; }
      if (opened) {
        countEl.textContent = countEl.getAttribute("data-done") || "";
        return;
      }
      countEl.textContent = (countEl.getAttribute("data-format") || "")
        .split("{n}").join(String(n))
        .split("{total}").join(String(total));
    }

    function open() {
      if (opened || committed() < total) { return; }
      opened = true;
      var right = 0, chosen = {}, kinds = 0, k;

      each(rows, function (row, i) {
        var want = row.getAttribute("data-answer");
        var got = picks[i];
        var hit = got === want;
        if (hit) { right += 1; }
        chosen[got] = true;
        row.setAttribute("data-state", hit ? "hit" : "miss");
        each(row.querySelectorAll("[data-real]"), function (span) {
          setHidden(span, span.getAttribute("data-real") !== (hit ? "hit" : "miss"));
        });
        setHidden(row.querySelector("[data-why]"), false);
        each(row.querySelectorAll(".ks3-plate-band"), function (b) {
          b.disabled = true;
        });
      });

      for (k in chosen) {
        if (Object.prototype.hasOwnProperty.call(chosen, k)) { kinds += 1; }
      }

      var head = verdict.querySelector("[data-vhead]");
      if (head) {
        head.textContent = (head.getAttribute("data-format") || "")
          .split("{n}").join(String(right))
          .split("{total}").join(String(total));
      }
      /* ⚖️ ORDER MATTERS. All-same is tested FIRST and independently of the
         score, because it is a different mistake from a low score and gets a
         different sentence. A student who put all seven in "tens of grams"
         happens to score 3, which would otherwise fall through to the general
         branch and never hear the one thing this block exists to say. */
      var branch = kinds === 1 ? "all_same" : (right >= total - 1 ? "close" : "spread");
      each(verdict.querySelectorAll("[data-v]"), function (p) {
        setHidden(p, p.getAttribute("data-v") !== branch);
      });

      setHidden(verdict, false);
      openBtn.disabled = true;
      openBtn.setAttribute("aria-expanded", "true");
      paintCount();
      markStage(sec, true);      // `all_seven_committed_and_opened`
    }

    each(rows, function (row, i) {
      each(row.querySelectorAll(".ks3-plate-band"), function (btn) {
        btn.addEventListener("click", function () {
          if (opened) { return; }
          var id = btn.getAttribute("data-band");
          picks[i] = id;
          each(row.querySelectorAll(".ks3-plate-band"), function (b) {
            b.setAttribute("aria-pressed",
              b.getAttribute("data-band") === id ? "true" : "false");
          });
          paintCount();
          openBtn.disabled = committed() < total;
        });
      });
    });

    openBtn.addEventListener("click", open);
    paintCount();
  }
