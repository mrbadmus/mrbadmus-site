# DISPATCH: "scale-cards": ("ks3-scards-block", " data-instrument data-scalecards"),
#
# NOTE THE ABSENT `data-stage-done`. This kind has no completion contract —
# see the docstring — so it takes the same entry shape as `confrontation`
# rather than the instrument shape. Emitting the attribute would declare a
# contract the section can never discharge, and the stage would sit at 0 for
# ever.
#
# Plus the two lines `r_activity` needs:
#
#     if kind == "scale-cards":
#         parts.append(r_scale_cards(a, act_id))
#
# Place after `r_random_walk_bench` in build_ks3.py. Needs `e`, `t`, `rich`.


def r_scale_cards(a, act_id):
    """⊕ c1-05 `#s-scale` — a distance, a time, and what that costs biology.

    ⚠️ **NOT `reveal-cards`, and this is a build decision with a gate behind
    it.** The nearest existing shape is `r_cards`, and it is wrong three times
    over: these do not flip, there is nothing behind them to reveal, and
    `verify_ks3.py` §5.1.2(a) requires every card grid to ask for a commitment
    in words before the tap. This block asks for nothing — it is the pay-off
    after the bench, not another task — so forcing it into `reveal-cards` would
    either fail that gate or, worse, make somebody write a fake commit prompt
    to satisfy it. A static three-up panel is its own component.

    ⚠️ INK-DARK, so every `<p>` rule in the stylesheet is scoped past
    `.ks3-dark p`, which is (0,1,1) and beats a bare instrument class at
    (0,1,0). The 28px display TIME is the one that would visibly break: it
    would fall back to on-dark BODY colour and read as a caption.

    ⚑ `--ks3-alert` on the distance label is Design's, and the map flags it
    (§5.5.2). Amber on ink is established for CONTROLS since B1; this is amber
    for BODY LABELLING, which is new, and README.txt's "amber is reserved for
    misconceptions" is about blocks rather than either. Reproduced as drawn and
    left flagged — a build is not the place to re-rule a palette question. The
    parity row registers the value, so the day it IS re-ruled the gate says so.
    """
    cards = a.get("scale_cards") or []
    if len(cards) < 2:
        raise ValueError(
            "scale-cards %r draws %d card(s); the panel is a comparison and "
            "needs at least two." % (act_id, len(cards)))
    for i, c in enumerate(cards):
        missing = [k for k in ("distance", "time", "text") if not c.get(k)]
        if missing:
            raise ValueError(
                "scale-cards %r card %d is missing %s. All three lines carry "
                "the comparison — a card with no time says nothing."
                % (act_id, i + 1, ", ".join(missing)))
    if not a.get("close"):
        raise ValueError(
            "scale-cards %r declares no `close`. The closing line is what "
            "turns three numbers into a rule (\"double the distance and "
            "diffusion takes four times as long\"); without it the panel is "
            "three facts and no argument." % act_id)

    grid = "".join(
        '<div class="ks3-scard">'
        '<p class="ks3-scard-distance">%s</p>'
        '<p class="ks3-scard-time">%s</p>'
        '<p class="ks3-scard-text">%s</p></div>'
        % (t(c["distance"]), t(c["time"]), rich(c["text"]))
        for c in cards)

    return ('<div class="ks3-scards">%s</div>'
            '<p class="ks3-scards-close">%s</p>' % (grid, rich(a["close"])))
