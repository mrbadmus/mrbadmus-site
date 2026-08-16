# ── PAGE CONSTANT ────────────────────────────────────────────────────────
# Add beside C2_ATOM … C2_MASS. All three of c1-06's instruments render only
# here, so all three are measured here — a component registered on a page that
# does not render it reports "selector not present" and passes, which is the
# absence-of-assertion failure this gate exists to close.
#
# C1_TEST = "chemistry/particles-and-their-behaviour/testing-the-model.html"


# ── COMPONENTS entries ───────────────────────────────────────────────────
# Each row pins the property that makes the component DISTINCT, not the ones it
# shares with every other panel. Mutation-test each before keeping it: break the
# rule in shared/ks3.css and confirm the row fails.

    # ══ C1 · Testing the model (⊕ MRB-228) ═══════════════════════════════

    # ── evidence-bench (c1-06 #s-bench) ──
    # The topology. A statement that can shrink beside a button pair that
    # cannot: if this ever resolves to `block`, the two calls drop under a
    # 54ch sentence and the seven cases stop being scannable as a column.
    dict(name="evidence case puts the calls beside the statement", on=C1_TEST,
         sel=".ks3-ebench-row",
         props={"display": "grid", "column-gap": "16px",
                "align-items": "start"}),

    # ⚖️ THE TWO-TONE VERDICT IS A FACT ABOUT THE MODEL, NOT ABOUT THE STUDENT.
    # A failure takes the BAND ground behind a 6px accent edge — the KEY FACT
    # treatment, deliberately not a red and not a dim. Both rows are driven,
    # because neither panel exists in the document's layout until its case is
    # judged, and both are measured in one document so the pair cannot drift
    # apart unnoticed.
    dict(name="a FAILING verdict is band behind a 6px accent edge", on=C1_TEST,
         drive="ebench-judged",
         sel='.ks3-ebench-case[data-ok="0"] .ks3-ebench-verdict',
         props={"background-color": "#F4E9D8", "border-left-color": "#E4572E",
                "border-left-width": "6px"}),
    dict(name="a HANDLED verdict is inset behind a quiet edge", on=C1_TEST,
         drive="ebench-judged",
         sel='.ks3-ebench-case[data-ok="1"] .ks3-ebench-verdict',
         props={"background-color": "#F7EFE1", "border-left-color": "#C3B191",
                "border-left-width": "6px"}),

    # The whole-set close. 24px display is what separates the counted line from
    # the paragraph under it; at body size the two read as one block of prose
    # and the number stops being the thing that lands.
    dict(name="evidence tally line is display 700 at 24px", on=C1_TEST,
         drive="ebench-all-judged", sel=".ks3-ebench-tallyline",
         props={"font-family": "Bricolage Grotesque", "font-weight": "700",
                "font-size": "24px"}),

# ⊖ NOT registered here, deliberately: `.ks3-ebench-case`'s resting card ground
# and its ink border once decided. That is the same two-value pattern already
# gated on `.ks3-jobsort-item` (rows 942 and 946) — one border going to ink on
# commitment — and re-asserting it on a second class buys coverage of a rule
# nobody can break independently.


# ── DRIVES entries ───────────────────────────────────────────────────────
# Add to DRIVES. Each reaches its state through the instrument's OWN control,
# so a regression in the interaction path fails here rather than being measured
# around.

    # One handled case and one failing case, in a single document, so both
    # verdict grounds can be measured against each other.
    "ebench-judged": r"""
(function () {
  var ok = document.querySelector('.ks3-ebench-case[data-ok="1"]');
  var bad = document.querySelector('.ks3-ebench-case[data-ok="0"]');
  if (!ok || !bad) { return "need one handled and one failing case"; }
  ok.querySelector('.ks3-ebench-btn').click();
  bad.querySelector('.ks3-ebench-btn').click();
  if (ok.getAttribute('data-open') !== '1' || bad.getAttribute('data-open') !== '1') {
    return "a case did not open after its call was pressed";
  }
  return "";
})()
""",
    # All seven judged, which is the only way the tally panel exists at all.
    "ebench-all-judged": r"""
(function () {
  var cases = document.querySelectorAll('.ks3-ebench-case');
  if (!cases.length) { return "no evidence bench on the page"; }
  for (var i = 0; i < cases.length; i++) {
    cases[i].querySelector('.ks3-ebench-btn').click();
  }
  var panel = document.querySelector('[data-ebench-tally]');
  if (!panel || panel.hasAttribute('hidden')) {
    return "every case judged and the tally is still hidden";
  }
  return "";
})()
""",
