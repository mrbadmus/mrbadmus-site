# ── PAGE CONSTANT ────────────────────────────────────────────────────────
# One drawn instance, on b3-06.
#
#     B3_ENZ = "biology/nutrition-and-digestion/enzymes-in-digestion.html"


# ── COMPONENTS entries ───────────────────────────────────────────────────
# Every value below is read out of `shared/tokens.css`, not estimated:
#   --ks3-alert #FFC53D · --ks3-ok #12A150 · --ks3-on-dark #FBF3E6
#   --ks3-on-dark-muted #C6B9A7 · --ks3-dark-panel #3E3730 · --ks3-ink #221E1B
#   --ks3-ground #FBF3E6 · --ks3-r-panel 20px
# Mutation-tested: each rule was deliberately broken in shared/ks3.css and the
# row confirmed to fail before it was kept.

    # ── enzyme-run (b3-06 #s-bench) ──
    #
    # ⚠️ THE TWO DIAL FIGURES ARE THE SPECIFICITY PROOF. `.ks3-dark p` is
    # (0,1,1) and a bare `.ks3-erun-rate` is (0,1,0): unscoped, the rate and
    # the temperature resolve to `--ks3-on-dark-body` #E7DECE and stop reading
    # as instrument readings at all. That is invisible to reading the CSS and
    # obvious in a browser, which is exactly why it is a gate row.
    dict(name="the rate reads as an instrument figure, in amber mono",
         on=B3_ENZ, sel=".ks3-erun-rate",
         props={"font-family": "DM Mono", "font-size": "16px",
                "color": "#FFC53D"}),
    dict(name="the temperature figure takes the same treatment", on=B3_ENZ,
         sel=".ks3-erun-tempvalue",
         props={"font-family": "DM Mono", "font-size": "21px",
                "color": "#FFC53D"}),
    # ⚖️ THE COUNTER THAT NEVER MOVES HAS TO LOOK DIFFERENT FROM THE TWO THAT
    # DO, and this row is the one that matters pedagogically. The fixed bar
    # carries BOTH `.ks3-erun-bar` and `.ks3-erun-bar-fixed`, so the ink-scoped
    # sibling rule at (0,2,0) beats an unscoped `-fixed` at (0,1,0) and the
    # enzyme counter renders in the same muted grey as the substrate — three
    # identical bars, and the whole argument of the block invisible.
    #
    # ⚑ THE VALUE ITSELF IS FLAGGED FOR MIDE. `--ks3-ok` is documented in
    # tokens.css as the ladder's correctness green, and this is a bar meaning
    # "unchanged" on a block that marks nothing. Design drew it and it is
    # reproduced as drawn; this row is what makes the day it is re-ruled a
    # loud one. Same handling as `scale-cards`' amber distance label.
    dict(name="the enzyme counter's bar keeps Design's green on ink",
         on=B3_ENZ, sel=".ks3-erun-bar-fixed",
         props={"background-color": "#12A150"}),
    # ⚖️ THE VERDICT INVERTS. It sits on the cream ground inside an ink block,
    # so its text has to be pulled back to ink explicitly; left to
    # `.ks3-dark p` it paints #E7DECE on #FBF3E6 at about 1.2:1 — the answer
    # rendered invisible on the one panel that carries it.
    dict(name="the verdict panel inverts to cream and reads in ink",
         on=B3_ENZ, drive="erun-denatured", sel=".ks3-erun-verdict",
         props={"background-color": "#FBF3E6", "color": "#221E1B",
                "border-top-left-radius": "20px"}),


# ── DRIVES entries ───────────────────────────────────────────────────────

    # ⚖️ THE DRIVE IS THE MISCONCEPTION, END TO END, and it reaches the state
    # through the instrument's OWN controls: drag the slider past the
    # threshold, drag it back to the optimum, run. Nothing here sets an
    # attribute, and every assertion is about what the bench then says.
    "erun-denatured": r"""
(function () {
  var sec = document.querySelector('[data-erunblock]');
  if (!sec) { return "no enzyme-run on the page"; }
  if (sec.getAttribute('data-stage-done') === '1') {
    return "the stop ticked on load";
  }
  var wrap = sec.querySelector('[data-erun]');
  var cfg;
  try { cfg = JSON.parse(wrap.getAttribute('data-cfg') || '{}'); }
  catch (err) { return "the bench carries no readable config"; }
  var slider = wrap.querySelector('[data-temp]');
  var runBtn = wrap.querySelector('[data-run]');
  var rate = wrap.querySelector('[data-rate]');
  if (!slider || !runBtn || !rate) { return "the bench has no dial or no run button"; }

  function setTemp(v) {
    slider.value = String(v);
    slider.dispatchEvent(new Event('input', { bubbles: true }));
  }

  // The third counter, read BEFORE anything happens. It is the one readout
  // nothing in the instrument may move, and it is checked again at the end.
  var fixed = wrap.querySelector('.ks3-erun-bar-fixed');
  var enzCell = wrap.querySelector('.ks3-erun-counter[data-counter="enzyme"] .ks3-erun-countervalue');
  if (!fixed || !enzCell) { return "the bench draws no enzyme counter"; }
  if (enzCell.hasAttribute('data-value')) {
    return "the enzyme counter has a runtime handle — it must have none";
  }
  var enzBefore = enzCell.textContent;
  var widthBefore = fixed.style.width || '';

  // 1. Above the threshold: the rate must fall to zero WITHOUT a run.
  setTemp(Number(cfg.denature_c) + 10);
  if (!/(^|\D)0(\D|$)/.test(rate.textContent)) {
    return "heated past the threshold and the rate is not zero";
  }
  if (!wrap.querySelector('.ks3-erun-tempnote[data-note="denatured_hot"]:not([hidden])')) {
    return "heated past the threshold and the hot-denatured note is not showing";
  }

  // 2. Cooled back to the optimum: STILL zero. This is the latch, and it is
  // the whole reason the instrument exists.
  setTemp(Number(cfg.optimum_c));
  if (!/(^|\D)0(\D|$)/.test(rate.textContent)) {
    return "cooling a denatured enzyme brought the rate back — the latch is broken";
  }
  if (!wrap.querySelector('.ks3-erun-tempnote[data-note="denatured_cool"]:not([hidden])')) {
    return "cooled after denaturing and the cool-denatured note is not showing";
  }

  // 3. Run it anyway: nothing is digested and the verdict says so.
  runBtn.click();
  var v = wrap.querySelector('[data-reveal]');
  if (!v || v.hasAttribute('hidden')) {
    return "a denatured run finished and no verdict appeared";
  }
  if (!wrap.querySelector('.ks3-erun-verdicttext[data-verdict="denatured"]:not([hidden])')) {
    return "a denatured run showed a verdict that was not the denatured one";
  }
  var prod = wrap.querySelector('[data-value="product"]');
  if (prod && !/(^|\D)0(\D|$)/.test(prod.textContent)) {
    return "a denatured enzyme produced something";
  }
  if (sec.getAttribute('data-stage-done') !== '1') {
    return "the reaction was run and the stop has not ticked";
  }

  // 4. The counter that never moves has not moved.
  if (enzCell.textContent !== enzBefore || (fixed.style.width || '') !== widthBefore) {
    return "the enzyme counter moved — it is the one readout nothing may touch";
  }
  // R3: nothing in this block marks correctness.
  if (wrap.querySelector('[data-correct], .is-correct, .is-wrong')) {
    return "a bench control was marked — this block marks nothing";
  }
  return "";
})()
""",
