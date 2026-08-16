# ── PAGE CONSTANT ────────────────────────────────────────────────────────
# One drawn instance, on b2-04. It is the only ink-dark instrument in the
# lesson, which is why three of the four rows below exist.
#
#     B2_BIO = "biology/movement-skeleton-and-muscles/biomechanics-forces-in-the-body.html"


# ── COMPONENTS entries ───────────────────────────────────────────────────
# Mutation-tested: each rule was deliberately broken in shared/ks3.css and the
# row confirmed to fail before it was kept.

    # ── arm-lever (b2-04 #s-bench) ──
    #
    # ⚠️ THIS ROW IS THE SPECIFICITY GUARD, and it is the reason the rest of
    # the block's rules are written `.ks3-dark …`. `.ks3-dark p` is (0,1,1);
    # a bare `.ks3-lever-tile-label` is (0,1,0) and LOSES, so an unscoped
    # colour renders the mono uppercase caption in `--ks3-on-dark-body` — the
    # same tone as the value under it, which stops the tile reading as a
    # caption over a number. Legible, so nobody reports it; wrong, so the
    # three measured tiles quietly stop being tiles. B1's zoom instrument
    # shipped exactly this and the joint bench nearly repeated it.
    dict(name="rig tile caption is mono muted on the dark panel, not body copy",
         on=B2_BIO, drive="lever-opened", sel=".ks3-lever-tile-label",
         props={"color": "#C6B9A7", "font-size": "13px",
                "text-transform": "uppercase"}),
    # ⚖️ THE TWO TILE TREATMENTS ARE THE GATE MADE VISIBLE. The three measured
    # tiles are mono 25px and the force tile is 19px/700 prose type, because
    # until the meter is fitted it holds a sentence. A single treatment would
    # set "not measured — you work it out" in a 25px readout face, which reads
    # as a broken number rather than as a refusal.
    dict(name="a measured tile is a 25px mono readout", on=B2_BIO,
         drive="lever-opened",
         sel='.ks3-lever-tile-value[data-lever-out="weight"]',
         props={"font-size": "25px", "font-weight": "500",
                "color": "#FBF3E6"}),
    dict(name="the withheld force tile is prose type, not a readout",
         on=B2_BIO, drive="lever-opened",
         sel='.ks3-lever-tile-value[data-lever-out="force"]',
         props={"font-size": "19px", "font-weight": "700"}),
    # The rig's frame matches the joint bench's value for value — same 2px
    # muted rule, same card radius. Two canvases framed differently on two
    # pages of one unit is drift a student notices before an adult does.
    dict(name="rig canvas frame is a 2px muted rule on a card radius",
         on=B2_BIO, drive="lever-opened", sel=".ks3-lever-stage",
         props={"border-top-color": "#C6B9A7", "border-top-width": "2px",
                "border-top-left-radius": "22px"}),


# ── DRIVES entries ───────────────────────────────────────────────────────

    # Nothing inside the rig exists in the document's layout until the commit
    # gate is answered — `r_bench_gate` hides the whole body rather than
    # greying it, so every measurement above needs this first. Which gate
    # option is deliberately unspecified: under R3 all four render identically
    # and open the same instrument.
    "lever-opened": r"""
(function () {
  var sec = document.querySelector('[data-leverblock]');
  if (!sec) { return "no arm-lever on the page"; }
  var opt = sec.querySelector('[data-benchgate] .ks3-option');
  if (!opt) { return "the rig offers no commit gate"; }
  opt.click();
  var body = sec.querySelector('[data-lever]');
  if (!body || body.hasAttribute('hidden')) {
    return "the gate was answered and the rig is still hidden";
  }
  if (!body.querySelector('[data-lever-canvas]')) {
    return "the rig opened with no canvas in it";
  }
  return "";
})()
""",
    # ⚖️ THE WITHHELD NUMBER, ASSERTED RATHER THAN TRUSTED. This drive is what
    # stops the lesson being quietly deleted by a refactor: it proves the
    # force is unreadable before the meter, readable after it, and that the
    # canvas label follows the same gate — a screen-reader user must not be
    # handed the answer a sighted student has to work out.
    "lever-metered": r"""
(function () {
  var sec = document.querySelector('[data-leverblock]');
  if (!sec) { return "no arm-lever on the page"; }
  var opt = sec.querySelector('[data-benchgate] .ks3-option');
  if (opt) { opt.click(); }
  var body = sec.querySelector('[data-lever]');
  if (!body) { return "the rig never opened"; }
  var tile = body.querySelector('[data-lever-out="force"]');
  var canvas = body.querySelector('[data-lever-canvas]');
  if (!tile || !canvas) { return "the rig has no force tile or no canvas"; }
  var withheld = body.getAttribute('data-unmeasured');
  if (tile.textContent.trim() !== withheld.trim()) {
    return "the force tile reads " + tile.textContent + " before the meter was fitted";
  }
  // The distances legitimately carry digits, so the label is checked against
  // the MEASURED CLAUSE's own opening words rather than against "any number".
  if (body.getAttribute('data-alt-measured')
      && canvas.getAttribute('aria-label').indexOf(
           body.getAttribute('data-alt-measured').split('{force}')[0]) >= 0) {
    return "the canvas label carried the meter reading before the meter was fitted";
  }
  if (sec.getAttribute('data-stage-done') === '1') {
    return "the rail stop ticked before any control was moved";
  }
  var slider = body.querySelector('[data-lever-input="load"]');
  var tabs = body.querySelectorAll('[data-lever-tab="hand"]');
  if (!slider || tabs.length < 2) { return "the rig is missing its controls"; }
  slider.value = '4';
  slider.dispatchEvent(new Event('input', { bubbles: true }));
  tabs[1].click();
  var btn = body.querySelector('[data-lever-meter]');
  if (!btn) { return "the rig has no meter button"; }
  btn.click();
  if (!/\d/.test(tile.textContent)) {
    return "the meter was fitted and the force tile still has no number in it";
  }
  if (!btn.hasAttribute('disabled')) {
    return "the meter button is still live after being fitted — it is one-way";
  }
  if (sec.getAttribute('data-stage-done') !== '1') {
    return "two controls moved and the meter fitted, and the stop has not ticked";
  }
  return "";
})()
""",
