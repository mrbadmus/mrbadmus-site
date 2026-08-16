# ── PAGE CONSTANT ────────────────────────────────────────────────────────
# One drawn instance, on b3-03.
#
#     B3_ENERGY = "biology/nutrition-and-digestion/energy-in-food-and-what-you-need.html"


# ── COMPONENTS entries ───────────────────────────────────────────────────
# Mutation-tested: each rule was deliberately broken in shared/ks3.css and the
# row confirmed to fail before it was kept.

    # ── person-ledger (b3-03 #s-ledger) ──
    #
    # ⚠️ THE ROW THAT WOULD OTHERWISE SHIP BROKEN. The match panel is CREAM
    # inside an ink-dark block, so its copy has to resolve to `--ks3-ink`.
    # `.ks3-dark p` is (0,1,1) and a bare `.ks3-ledger-mwhy` is (0,1,0):
    # unscoped it paints #E7DECE on #FBF3E6, and the sentence lost is
    # *"Now switch person without changing the food"* — the one NOTES-B3 §3.3
    # names as the thing that must not be lost, because without it a match
    # reads as having finished.
    # ⚖️ CORRECTED (MRB-228) — see the note in band-commit.parity.py. The
    # background belongs to `.ks3-ledger-match`, not to the paragraph in it.
    dict(name="the match copy is ink on the cream panel", on=B3_ENERGY,
         drive="ledger-matched", sel=".ks3-ledger-mwhy",
         props={"color": "#221E1B", "font-size": "18px"}),
    dict(name="the match panel is the page ground on an ink block",
         on=B3_ENERGY, drive="ledger-matched", sel=".ks3-ledger-match",
         props={"background-color": "#FBF3E6"}),
    # ⚖️ THE MATCHED BAR IS NOT GREEN, AND THAT IS THE POINT. `--ks3-ok`
    # #12A150 is the ladder's colour for a correct answer and a plate is not an
    # answer; the bar reports a measurement. If this row ever resolves to
    # #12A150 or #E4F7EB the block has started marking (R3), and it would look
    # like an improvement.
    dict(name="a matched day reads as on target, never as correct",
         on=B3_ENERGY, drive="ledger-matched", sel='.ks3-ledger-fill[data-state="matched"]',
         props={"background-color": "#2F5CE0"}),
    # The running total is the block's headline number and is mono, not
    # display: it is a quantity being watched change, and setting it in the
    # display face would make it read as a conclusion.
    dict(name="the running total is readable mono, not display", on=B3_ENERGY,
         drive="ledger-matched", sel=".ks3-ledger-total",
         props={"font-family": "DM Mono", "font-size": "22px",
                "color": "#FBF3E6"}),
    # A food with portions on it takes the same lit treatment as a chosen tab —
    # alert on ink — because adding a portion IS a selection. Pinned so the two
    # cannot drift into two different "on" colours in one block.
    dict(name="a food with portions on it takes the lit treatment",
         on=B3_ENERGY, drive="ledger-matched",
         sel='.ks3-ledger-food[data-count]:not([data-count="0"])',
         props={"background-color": "#FFC53D", "color": "#221E1B",
                "min-height": "44px"}),


# ── DRIVES entries ───────────────────────────────────────────────────────

    # The match panel does not exist in the layout until the plate lands inside
    # the tolerance, so the rows above need this. It builds the day the way a
    # student does — repeated `.click()` on real food buttons — and stops the
    # moment the panel opens.
    "ledger-matched": r"""
(function () {
  var sec = document.querySelector('[data-ledgerblock]');
  if (!sec) { return "no person-ledger on the page"; }
  var wrap = sec.querySelector('[data-ledger]');
  if (!wrap) { return "the block drew no ledger"; }
  if (sec.getAttribute('data-stage-done') === '1') {
    return "the stop ticked on load";
  }
  var match = wrap.querySelector('[data-match]');
  if (!match || !match.hasAttribute('hidden')) {
    return "the match panel was open on an empty plate";
  }
  var foods = wrap.querySelectorAll('.ks3-ledger-food');
  if (foods.length < 2) { return "fewer than two foods to add"; }
  // Add portions until the bar lands in tolerance. The ledger's own
  // wrap-around clears a food once it passes `data-max`, so this walks across
  // the foods rather than hammering one and cycling it back to zero.
  var bar = wrap.querySelector('[data-bar]');
  var max = parseInt(wrap.getAttribute('data-max'), 10) || 6;
  // ⚖️ CORRECTED (MRB-228). The first cut advanced `guard` on a SKIP as well
  // as on a click, and the target index is derived from `guard` — so every
  // food already at `data-max` shifted the walk onto a different food, and the
  // total stepped straight past the tolerance window into `over`. The drive
  // then returned success on a bar reading `over`, and the row that measures
  // the matched fill found nothing.
  //
  // Walk the foods in order, one click at a time, and STOP the instant the bar
  // reports a match — the state is set synchronously in the click handler, so
  // reading it straight after the click is sound. Reachable in nine clicks.
  var guard = 0;
  for (var f = 0; f < foods.length && bar.getAttribute('data-state') !== 'matched'; f++) {
    while ((parseInt(foods[f].getAttribute('data-count'), 10) || 0) < max
           && bar.getAttribute('data-state') !== 'matched' && guard < 400) {
      foods[f].click();
      guard += 1;
    }
  }
  if (sec.getAttribute('data-stage-done') !== '1') {
    return "food is on the plate and the stop has not ticked";
  }
  if (bar.getAttribute('data-state') !== 'matched') {
    return "no combination of the offered portions lands inside the tolerance";
  }
  if (match.hasAttribute('hidden')) {
    return "the plate is inside the tolerance and the match panel is shut";
  }
  if (!match.querySelector('.ks3-ledger-mhead:not([hidden])')) {
    return "the match panel opened without naming who it matches";
  }
  if (match.querySelectorAll('.ks3-ledger-mhead:not([hidden])').length !== 1) {
    return "the match panel named more than one eater at once";
  }
  // ⚖️ THE EXPERIMENT: switching the person must NOT touch the plate. This is
  // the assertion the whole instrument exists for, and it is cheap to break by
  // "tidying" the tab handler into a reset.
  var before = wrap.querySelector('[data-portions]').textContent;
  var tabs = wrap.querySelectorAll('.ks3-ledger-tab[data-person]');
  var other = null;
  for (i = 0; i < tabs.length; i++) {
    if (tabs[i].getAttribute('aria-pressed') !== 'true') { other = tabs[i]; break; }
  }
  if (!other) { return "the ledger offers only one eater"; }
  var was = null;
  for (i = 0; i < tabs.length; i++) {
    if (tabs[i].getAttribute('aria-pressed') === 'true') { was = tabs[i]; break; }
  }
  other.click();
  if (wrap.querySelector('[data-portions]').textContent !== before) {
    return "switching the person changed the plate — the plate is the control";
  }
  // ⚖️ SWITCH BACK (MRB-228). The experiment above is the point of the
  // instrument, and it necessarily leaves the bar reading `over` — the plate
  // that matched one eater does not match the next, which is the whole lesson.
  // But this drive is named `ledger-matched` and four rows measure the matched
  // state after it, so it must END where its name says. Returning to the
  // original eater restores the match without touching the plate, which is
  // itself the same claim the experiment just made, in reverse.
  if (was) { was.click(); }
  if (bar.getAttribute('data-state') !== 'matched') {
    return "returning to the first eater did not restore the match";
  }
  // R3: there is no answer here and nothing may be marked.
  if (wrap.querySelector('.ks3-option, [data-correct], svg.ks3-mark')) {
    return "an answer control or a drawn mark appeared inside person-ledger";
  }
  return "";
})()
""",
