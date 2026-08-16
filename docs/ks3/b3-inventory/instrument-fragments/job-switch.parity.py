# ── PAGE CONSTANT ────────────────────────────────────────────────────────
# One drawn instance, on b3-08. Splice the constant beside the other unit
# constants in ks3_parity.py, inside the B3 group.
#
#     B3_BACTERIA = "biology/nutrition-and-digestion/bacteria-in-the-gut.html"


# ── COMPONENTS entries ───────────────────────────────────────────────────
# Mutation-tested: each rule was deliberately broken in shared/ks3.css and the
# row confirmed to fail before it was kept. Every hex below is read out of
# shared/tokens.css, not estimated.

    # ── job-switch (b3-08 #s-jobs) ──
    #
    # ⚠️ THE ROW THAT WOULD OTHERWISE SHIP BROKEN, and the only one in this
    # unit where the failure is total rather than subtle. The consequence
    # paragraph is CREAM (`--ks3-ground`) inside an ink-dark block, so its text
    # has to resolve to `--ks3-ink`. `.ks3-dark p` is (0,1,1) and a bare
    # `.ks3-jobsw-without` is (0,1,0): unscoped it paints `--ks3-on-dark-body`
    # #E7DECE on #FBF3E6, which is 1.1:1 — the sentence is in the DOM, is
    # correct, and cannot be read. Invisible to reading the stylesheet, and
    # the same defect class as B1's zoom instrument and B2's muscle bench.
    dict(name="the consequence is ink on the cream panel, not on-dark body",
         on=B3_BACTERIA, drive="jobs-one-off", sel=".ks3-jobsw-without",
         props={"color": "#221E1B", "background-color": "#FBF3E6",
                "font-size": "18px"}),
    # ⚖️ THE GROUND INVERTS, and it is the opposite way round from b3-07's
    # fold builder one lesson earlier. A job STILL BEING DONE sits on the
    # nested dark panel — it is a working part of the system. This row pins
    # the resting state so a later tidy-up cannot align the two instruments
    # and destroy the distinction.
    dict(name="a job still being done sits on the dark panel", on=B3_BACTERIA,
         sel=".ks3-jobsw-job",
         props={"background-color": "#3E3730",
                "border-top-left-radius": "20px",
                "border-top-width": "2px"}),
    # Switched off, the row loses the panel and gains the alert rule. Amber
    # marks a part that has been REMOVED, never a student who was wrong (§8),
    # and if this ever resolves to `--ks3-ok` #12A150 or `--ks3-ok-tint`
    # #E4F7EB an experiment has started marking (R3).
    dict(name="a switched-off job falls back to bare ink on an alert rule",
         on=B3_BACTERIA, drive="jobs-one-off", sel='.ks3-jobsw-job[data-off="1"]',
         props={"border-top-color": "#FFC53D", "border-top-width": "2px"}),
    # The payoff is a HEADLINE and is set in display type. As body copy it
    # would read as a sixth consequence rather than as the conclusion drawn
    # from all five — and the sentence it carries is the one the lesson is
    # built to deliver.
    dict(name="the germ-free-mouse payoff is a display headline", on=B3_BACTERIA,
         drive="jobs-all-off", sel=".ks3-jobsw-allhead",
         props={"font-family": "Bricolage Grotesque", "font-weight": "800",
                "font-size": "26px", "color": "#FBF3E6"}),


# ── DRIVES entries ───────────────────────────────────────────────────────

    # ONE job off, through that row's own button. The consequence paragraph
    # does not exist in the document's layout until it is pressed.
    "jobs-one-off": r"""
(function () {
  var sec = document.querySelector('[data-jobswblock]');
  if (!sec) { return "no job-switch on the page"; }
  var wrap = sec.querySelector('[data-jobsw]');
  if (!wrap) { return "the block has no job-switch in it"; }
  if (sec.getAttribute('data-stage-done') === '1') {
    return "the stop ticked on load";
  }
  if (wrap.querySelector('.ks3-jobsw-without:not([hidden])')) {
    return "a consequence was showing before any job was switched off";
  }
  var btn = wrap.querySelector('[data-jobsw-toggle]');
  if (!btn) { return "the block offers no job to switch off"; }
  btn.click();
  var job = wrap.querySelector('.ks3-jobsw-job[data-off="1"]');
  if (!job) { return "a job was switched off and the row did not change state"; }
  if (!job.querySelector('.ks3-jobsw-without:not([hidden])')) {
    return "a job was switched off and its consequence is still hidden";
  }
  // ⚖️ ONE JOB IS NOT THE ANIMAL. The summary panel is a claim about all
  // five at once and must stay shut until it is true.
  var all = wrap.querySelector('[data-jobsw-all]');
  if (all && !all.hasAttribute('hidden')) {
    return "the germ-free-mouse panel opened after one job";
  }
  if (sec.getAttribute('data-stage-done') === '1') {
    return "the stop ticked after one of five jobs";
  }
  return "";
})()
""",

    # ALL FIVE off, through the five buttons and nothing else. This is the
    # state the lesson exists to reach.
    "jobs-all-off": r"""
(function () {
  var sec = document.querySelector('[data-jobswblock]');
  if (!sec) { return "no job-switch on the page"; }
  var wrap = sec.querySelector('[data-jobsw]');
  var all = wrap && wrap.querySelector('[data-jobsw-all]');
  if (!all) { return "the block has no all-off summary to reach"; }
  var btns = wrap.querySelectorAll('[data-jobsw-toggle]');
  if (btns.length < 5) {
    return "the block offers " + btns.length + " jobs, not five";
  }
  for (var i = 0; i < btns.length; i++) { btns[i].click(); }
  if (all.hasAttribute('hidden')) {
    return "every job is off and the germ-free-mouse panel is still hidden";
  }
  if (wrap.querySelectorAll('.ks3-jobsw-without:not([hidden])').length
      !== btns.length) {
    return "a job was switched off without its consequence arriving";
  }
  if (sec.getAttribute('data-stage-done') !== '1') {
    return "every job is off and the stop has not ticked";
  }
  // ⚖️ THE PANEL FOLLOWS THE STATE AND THE RAIL DOES NOT. Switch one back on:
  // the animal is no longer germ-free, so the claim must go — but MRB-208
  // says a stop ticks when the activity is finished, and nothing un-finishes
  // it. This pair is the whole reason job-switch is not `system-switch`.
  btns[0].click();
  if (!all.hasAttribute('hidden')) {
    return "a job came back on and the panel still claims a germ-free mouse";
  }
  if (sec.getAttribute('data-stage-done') !== '1') {
    return "the stop un-ticked when a job was switched back on";
  }
  btns[0].click();
  if (all.hasAttribute('hidden')) {
    return "the panel did not come back when the last job went off again";
  }
  // R3, asserted here as well as globally: five toggles are not answers.
  if (wrap.querySelector('.ks3-option, [data-correct], .is-correct, .is-wrong')) {
    return "the job switch is marking something — this block asks no question";
  }
  return "";
})()
""",
