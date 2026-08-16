/* WIRE: each(root.querySelectorAll("[data-jobswblock]"), wireJobSwitch);
   — add to wireInstruments(), in the B3 group, after wireFoldBuilder. Uses
   each / toArray / setHidden / setCount / markStage, all already in scope. */

  /* ═══════════════════════════════════════════════════════════════
     ── job-switch (b3-08 #s-jobs) — take one job away ──

     Five things gut bacteria do that your own cells cannot. Switch each
     off and read what the host loses; switch all five off and you have
     built the germ-free mouse from the hook.

     ⚖️ THE SUMMARY REPORTS THE PRESENT TENSE, and that is why this is
     not `system-switch`. `wireSwitch` and `wireJobSort` both count what
     has EVER been opened and fire their closing panel on that count —
     one-way, cumulative, and right for both of them. This panel says
     "You have just built the germ-free mouse", which is a claim about
     the configuration on screen: switch a job back on and the animal
     is no longer germ-free, so the panel has to go away again. A
     component that counts history cannot express a component that
     reports state.

     ⚖️ THE RAIL STOP LATCHES, and the panel does not. MRB-208 ruled the
     rail records PARTICIPATION — a stop ticks when the activity is
     finished and nothing un-finishes it — so `markStage` is only ever
     called with `true` here. Design's own `isDone` recomputes
     `JOBS.every(j => s.off[j.id])` on every render and would take a
     student's progress away for looking at a row again. The counter and
     the panel still follow the live state, because both are statements
     about what is true now.

     ⚖️ NOTHING MARKS. Five toggles, no answer, no `data-correct`. The
     block is an experiment, not a question, and a student who switches
     everything off and everything back on has done the experiment
     twice rather than got it wrong once.

     ⚖️ NOTHING ANIMATES and nothing counts down, so
     `prefers-reduced-motion` has nothing to degrade and the
     reduced-motion experience is the complete one. NOTES-B3 §6 is
     explicit that `enzyme-run` is the only instrument in this unit with
     a timer.
     ═══════════════════════════════════════════════════════════════ */
  function wireJobSwitch(sec) {
    var wrap = sec.querySelector("[data-jobsw]");
    if (!wrap) { return; }
    var jobs = toArray(wrap.querySelectorAll("[data-job]"));
    if (!jobs.length) { return; }

    var all = wrap.querySelector("[data-jobsw-all]");
    var total = parseInt(wrap.getAttribute("data-total"), 10) || jobs.length;

    function refresh() {
      var off = 0;
      each(jobs, function (job) {
        if (job.getAttribute("data-off") === "1") { off += 1; }
      });
      setCount(sec, off);
      if (all) {
        setHidden(all, off < total);
        // Announced once, for screen-reader users who would otherwise get
        // no signal that the block's conclusion had arrived below the last
        // row. On the NOTE, never on the section — a live region around the
        // whole instrument would re-read five job descriptions every time a
        // switch moved.
        if (off >= total && !all.getAttribute("role")) {
          all.setAttribute("role", "status");
        }
      }
      if (off >= total) { markStage(sec, true); }
    }

    each(jobs, function (job) {
      var btn = job.querySelector("[data-jobsw-toggle]");
      var note = job.querySelector("[data-reveal]");
      if (!btn) { return; }
      btn.addEventListener("click", function () {
        var off = job.getAttribute("data-off") !== "1";
        job.setAttribute("data-off", off ? "1" : "0");
        btn.setAttribute("aria-pressed", off ? "true" : "false");
        // Both faces were finished at build time — "Switch it off" and
        // "Switched off" — so nothing here composes a label.
        btn.textContent = btn.getAttribute(off ? "data-label-off"
                                              : "data-label-on") || "";
        if (note) {
          setHidden(note, !off);
          if (off && !note.getAttribute("role")) {
            note.setAttribute("role", "status");
          }
        }
        refresh();
      });
    });

    // Opens with every job doing its job: 0 of 5 switched off, no
    // consequences showing, no summary. That is what the HTML already says,
    // so this call changes nothing on load — it is here so there is exactly
    // one place the counter and the summary are decided.
    refresh();
  }
