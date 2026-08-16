# PAGE CONSTANT (shared with heating-bench.parity.py — declare it once):
#
#     C1_STATE = "chemistry/particles-and-their-behaviour/changes-of-state.html"
#
# DRIVE (new — add to ks3_parity.DRIVES):
#
#     # One card sorted CORRECTLY and one sorted WRONGLY, which is the only
#     # way both card borders and both note tones exist in one document. The
#     # sorter is not one-shot, so the second click is a real second card and
#     # never a re-press of the first.
#     "sortcards-decided": r"""
# (function () {
#   var cards = document.querySelectorAll('.ks3-sortcards-card');
#   if (cards.length < 2) { return "need 2 sort cards, found " + cards.length; }
#   function pick(card, correct) {
#     var want = card.getAttribute('data-answer');
#     var opts = card.querySelectorAll('.ks3-sortcards-opt');
#     for (var j = 0; j < opts.length; j++) {
#       if ((opts[j].getAttribute('data-choice') === want) === correct) {
#         opts[j].click();
#         return true;
#       }
#     }
#     return false;
#   }
#   if (!pick(cards[0], true))  { return "no matching option on card 1"; }
#   if (!pick(cards[1], false)) { return "no other option on card 2"; }
#   if (cards[0].getAttribute('data-verdict') !== 'right'
#       || cards[1].getAttribute('data-verdict') !== 'wrong') {
#     return "cards did not record their verdicts";
#   }
#   return "";
# })()
# """,

    # ── sort-cards (c1-03 #s-think) ──
    # A cream card on the OPTION border, inside the amber misconception
    # shell. If this row ever reports `#FFF3D4` the card has taken the
    # shell's own ground and the student's working has become part of the
    # wrong idea being confronted.
    dict(name="sort card is a card on the option border", on=C1_STATE,
         sel=".ks3-sortcards-card",
         props={"background-color": "#FFFCF5", "border-top-color": "#DDCFB6",
                "border-top-width": "2px", "border-top-left-radius": "20px"}),

    # ⚖️ Design's own marking rule, and the only marked activity card in C1.
    # Both states in one row-pair so neither can drift alone: accent when the
    # word fits, plain ink when it does not — never the ok family, never a
    # drawn mark. If the "wrong" row ever reports a red or a green, R3 has
    # been broken here and the block has become a test.
    dict(name="a card that FITS takes the accent border", on=C1_STATE,
         drive="sortcards-decided", sel='.ks3-sortcards-card[data-verdict="right"]',
         props={"border-top-color": "#E4572E", "border-top-width": "2px"}),
    dict(name="a card that does not fit takes the plain INK border",
         on=C1_STATE, drive="sortcards-decided",
         sel='.ks3-sortcards-card[data-verdict="wrong"]',
         props={"border-top-color": "#221E1B", "border-top-width": "2px"}),

    # The correction is accent-TEXT at 16px — the only orange the key stage
    # allows below 24px, and the reason the note is not painted in
    # `--ks3-accent` to match the border it sits inside.
    dict(name="the correction note is accent-text, not accent", on=C1_STATE,
         drive="sortcards-decided",
         sel='.ks3-sortcards-note[data-note="wrong"]:not([hidden])',
         props={"color": "#A93411", "font-size": "16px"}),
