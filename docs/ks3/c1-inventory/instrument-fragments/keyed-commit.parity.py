# ── PAGE CONSTANT ────────────────────────────────────────────────────────
# `keyed-commit` renders on two pages. Measured on c1-06, whose instance is the
# one PAYLOAD-MAP §6.5.2 ruled the shape from — four options each carrying a
# reply, against c1-03's three branched responses. The wider shape cannot pass
# on a rule the narrower one would fail.
#
# C1_TEST = "chemistry/particles-and-their-behaviour/testing-the-model.html"


# ── COMPONENTS entries ───────────────────────────────────────────────────
# Mutation-tested: each rule was deliberately broken in shared/ks3.css and the
# row confirmed to fail before it was kept.

    # ── keyed-commit (c1-06 #s-verdict) ──
    #
    # ⚠️ BOTH ROWS EXIST TO PROVE THE SPECIFICITY SCOPING. `.ks3-dark p` is
    # (0,1,1) and a bare `.ks3-keyed-reply` is (0,1,0): unscoped, the reply
    # loses and renders in `--ks3-on-dark-body` against the panel rather than
    # in the panel's own treatment. That is the defect B1 shipped with the zoom
    # instrument and B2 was bitten by again, and it is invisible to reading.
    dict(name="verdict panel is a dark panel on a muted rule", on=C1_TEST,
         drive="keyed-committed", sel=".ks3-keyed-reveal",
         props={"background-color": "#3E3730", "border-top-color": "#C6B9A7",
                "border-top-width": "2px",
                "border-top-left-radius": "20px"}),
    dict(name="the chosen reply is on-dark body copy, not muted", on=C1_TEST,
         drive="keyed-committed",
         sel='.ks3-keyed-reply:not([hidden])',
         props={"color": "#E7DECE", "font-size": "19px"}),
    # The reply and the static paragraphs must resolve IDENTICALLY. The panel's
    # argument is that the student's answer and the historical record are the
    # same kind of sentence; a reply painted differently from the paragraphs
    # under it would read as a verdict on the choice, which is exactly what R3
    # forbids here.
    dict(name="the static close matches the reply exactly", on=C1_TEST,
         drive="keyed-committed", sel=".ks3-keyed-static",
         props={"color": "#E7DECE", "font-size": "19px",
                "margin-top": "14px"}),
    # 36rem, Design's own measure on both pages. Full-width answer buttons on a
    # 60rem column are a target the eye has to travel.
    dict(name="commit options keep Design's 36rem measure", on=C1_TEST,
         sel=".ks3-keyed-options", props={"max-width": "576px"}),


# ── DRIVES entry ─────────────────────────────────────────────────────────

    # The panel does not exist in the document's layout until an option is
    # pressed, so every panel measurement needs this first. Which option is
    # deliberately unspecified: under R3 all four render identically and open
    # the same panel, and `check_r3_runtime()` asserts that rather than
    # trusting it.
    "keyed-committed": r"""
(function () {
  var wrap = document.querySelector('[data-keyed]');
  if (!wrap) { return "no keyed-commit on the page"; }
  var opt = wrap.querySelector('.ks3-option');
  if (!opt) { return "keyed-commit offers no options"; }
  opt.click();
  var panel = wrap.querySelector('[data-reveal]');
  if (!panel || panel.hasAttribute('hidden')) {
    return "an option was pressed and the panel is still hidden";
  }
  if (!wrap.querySelector('.ks3-keyed-reply:not([hidden])')) {
    return "the panel opened with no reply showing";
  }
  return "";
})()
""",
