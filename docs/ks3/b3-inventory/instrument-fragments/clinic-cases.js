/* WIRE: each(root.querySelectorAll("[data-clinicblock]"), wireClinicCases);
   — add to wireInstruments(), in a new B3 group. Uses each / toArray /
   setHidden / setCount / markStage, all already in scope. */

  /* ── clinic-cases (b3-04 #s-cases) ──
     Five clinics. Tick every imbalance that applies, then open the
     diagnosis. Two of the five have two answers.

     ⚖️ MULTI-SELECT, NOT A PICKER, and every line below exists to keep it
     that way. A pick toggles rather than replacing the others, the reveal
     button unlocks on ONE tick rather than on a complete answer (a student
     who thinks one applies must be allowed to commit to that — being
     unwilling to tick two is the error the block is built to show, and it
     cannot be shown if the page refuses to accept the one-tick answer),
     and the picks freeze the moment the diagnosis opens.

     ⚠️ NOTHING MARKS. There is no `data-correct` in this instrument and
     there must not be. The correct kinds are not in the document as data
     at all — the answer is prose, in `.ks3-clinic-answer`, revealed
     identically to every student. The verdict LABEL is a fact about the
     case ("Two imbalances apply here"), authored per case, and it is not
     computed from what the student ticked; MRB-196 R10 replaced that
     computation with the self-check below.

     ⚖️ THE STAGE IS EVERY CLINIC DIAGNOSED, not every clinic looked at.
     Design's own predicate is the same and it is right: one clinic is one
     judgement, and the lesson's argument is the five held against each
     other — clinic 4 is a deficiency in a fed child, clinic 5 is not a
     diet problem at all, and neither means anything alone.

     ⚖️ NOTHING ANIMATES and nothing counts down, so `prefers-reduced-motion`
     has nothing to degrade here: the reduced-motion experience is the
     complete one. */
  function wireClinicCases(sec) {
    var wrap = sec.querySelector("[data-clinic]");
    if (!wrap) { return; }
    var tabs = toArray(wrap.querySelectorAll(".ks3-clinic-tab"));
    var panels = toArray(wrap.querySelectorAll(".ks3-clinic-panel"));
    var selfcheck = sec.querySelector("[data-selfcheck]");
    if (!panels.length) { return; }

    function show(id) {
      each(tabs, function (tab) {
        tab.setAttribute("aria-pressed",
          tab.getAttribute("data-case") === id ? "true" : "false");
      });
      each(panels, function (p) {
        setHidden(p, p.getAttribute("data-case") !== id);
      });
    }
    each(tabs, function (tab) {
      tab.addEventListener("click", function () {
        show(tab.getAttribute("data-case"));
      });
    });

    function diagnosed() {
      var n = 0;
      each(panels, function (p) {
        if (p.getAttribute("data-open") === "1") { n += 1; }
      });
      return n;
    }

    function refreshStage() {
      var n = diagnosed();
      setCount(sec, n);
      var all = n >= panels.length;
      markStage(sec, all);
      /* The self-check has nothing to compare against until every answer is
         showing, so it does not exist in the layout until then. R10: the
         page asks, the student answers, and nothing is graded. */
      if (all && selfcheck) {
        setHidden(selfcheck, false);
        selfcheck.setAttribute("role", "status");
      }
    }

    each(panels, function (panel) {
      var picks = toArray(panel.querySelectorAll(".ks3-clinic-pick"));
      var btn = panel.querySelector("[data-clinic-reveal]");
      var count = panel.querySelector("[data-clinic-count]");
      var verdict = panel.querySelector("[data-reveal]");

      function ticked() {
        var n = 0;
        each(picks, function (p) {
          if (p.getAttribute("aria-pressed") === "true") { n += 1; }
        });
        return n;
      }

      function repaint() {
        var open = panel.getAttribute("data-open") === "1";
        var n = ticked();
        if (count) {
          /* Three authored states, all three in the document as attributes
             and none of them assembled here from words — only the number is
             substituted. */
          count.textContent = open
            ? (count.getAttribute("data-done") || "")
            : (n
               ? String(count.getAttribute("data-some") || "")
                   .split("{n}").join(String(n))
               : (count.getAttribute("data-none") || ""));
        }
        if (btn) {
          /* One tick is enough to commit. See the header: refusing the
             one-tick answer would hide the mistake being taught. */
          if (!n || open) { btn.setAttribute("disabled", ""); }
          else { btn.removeAttribute("disabled"); }
        }
      }

      each(picks, function (p) {
        p.addEventListener("click", function () {
          if (panel.getAttribute("data-open") === "1") { return; }
          /* TOGGLE, never replace. This is the one control in the key stage
             where more than one may be pressed at once. */
          p.setAttribute("aria-pressed",
            p.getAttribute("aria-pressed") === "true" ? "false" : "true");
          repaint();
        });
      });

      if (btn) {
        btn.addEventListener("click", function () {
          if (panel.getAttribute("data-open") === "1" || !ticked()) { return; }
          panel.setAttribute("data-open", "1");
          setHidden(verdict, false);
          /* ⚠️ NO SECOND `role="status"` HERE, deliberately. `keyed-commit`
             and `meter-compare` announce their revealed panel because they
             have no other live element; this panel has one — the count —
             and it goes to "Diagnosed" in the same turn. Announcing both
             reads the whole verdict over the top of the state change. One
             live region per panel; the count is it. */
          each(picks, function (p) { p.setAttribute("disabled", ""); });
          repaint();
          refreshStage();
        });
      }

      repaint();
    });

    refreshStage();
  }
