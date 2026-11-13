"""ks3_art.c2 — C2's drawers, instruments and registrations.

ONE UNIT, ONE FILE. Nothing here is read by any other unit; nothing
here may be added to any other unit's module. Moved verbatim out of
``build_ks3.py`` by MRB-271 so that two content lanes can build two
units at once without editing the same file.
"""

import json
import re
from ks3_art.kit import (
    _SVG_ACCENT_TEXT,
    _SVG_BAND,
    _SVG_CARD,
    _SVG_INK,
    _SVG_INK_FAINT,
    _SVG_INSET,
    _SVG_RULE,
    _canvas_frame,
    _circle,
    _label,
    _line,
    _mono,
    _path,
    _rect,
    _svg_open,
    e,
    r_bench_gate,
    rich,
    sci,
    t,
)


def r_claim_switch(a, act_id):
    """⊕ c2-01 `#s-model` — three claims as toggles, four observations as
    dependants.

    ⚠️ A LIGHT `.ks3-block`, not a practical. The map calls this out by name:
    it is the flagship of a MODEL lesson and it looks like a bench, and
    painting it on ink resolves every text token wrong.

    ⚖️ THE FAILURE SENTENCE IS THE TEACHING. An observation whose claim is off
    does not grey out or get a cross — its text is REPLACED by the sentence
    saying why it stops being explained. Both sentences are in the document and
    one is hidden (emit-both-show-one), so no text is ever assembled from an
    attribute and `<em>` survives in either.

    ⚠️ `touched >= 2` counts EVERY press, including switching a claim back on.
    That is Design's rule as written (map §2.4) and a component must not tighten
    it silently to "two claims off".
    """
    claims = a.get("claims") or []
    obs = a.get("observations") or []
    if not claims or not obs:
        raise ValueError(
            "claim-switch %r needs both claims[] and observations[]." % act_id)
    ids = {c["id"] for c in claims}
    for o in obs:
        missing = [n for n in (o.get("needs") or []) if n not in ids]
        if missing:
            raise ValueError(
                "claim-switch %r observation %r needs claim(s) %s, which are "
                "not declared." % (act_id, o.get("id"), missing))

    # ⊕ MRB-257 phase 4 — EVERY CLAIM MUST BE LOAD-BEARING, and the note says
    # so out loud: the `none_broken` branch reads "Nothing has broken — which
    # would mean that claim was doing no work. Look again: every one of
    # Dalton's three is holding something up." That sentence is true of the
    # shipped payload and is UNREACHABLE because of it, which is the right
    # relationship between a defensive branch and its precondition — but
    # nothing was checking the precondition. A claim no observation needs
    # would make the branch reachable and the block pointless: a student could
    # switch something off and be told, correctly, that it did nothing.
    idle = sorted(c["id"] for c in claims
                  if not any(c["id"] in (o.get("needs") or []) for o in obs))
    if idle:
        raise ValueError(
            "claim-switch %r declares claim(s) %s that no observation needs, "
            "so switching one off breaks nothing and the block teaches the "
            "opposite of its own note ('every one of them is holding "
            "something up'). Either an observation is missing or the claim is."
            % (act_id, ", ".join(map(repr, idle))))

    gate = dict(a.get("gate") or {})
    # ⊕ The gate's options ARE the three claim texts, lettered (map §2.5). They
    # are read from `claims` rather than authored twice: a second copy of a
    # science-bearing sentence is a second place for it to drift, and R5's
    # point is that every authored key has exactly one meaning.
    if gate and not gate.get("options") and gate.get("options_from") == "claims":
        gate["options"] = [c.get("text", "") for c in claims]
    gate_html, hide = r_bench_gate(gate)

    labels = a.get("labels") or {}
    verdicts = a.get("verdicts") or {}
    note = a.get("note") or {}

    rows = "".join(
        '<button type="button" class="ks3-claim" data-claim="%s" '
        'aria-pressed="true"><span class="ks3-claim-chip" data-claim-chip>%s'
        '</span><span class="ks3-claim-text">%s</span></button>'
        % (e(c["id"]), t(labels.get("on") or "ON"), rich(c.get("text", "")))
        for c in claims)

    obs_rows = "".join(
        '<div class="ks3-obs-row" data-obs="%s" data-needs="%s">'
        '<div class="ks3-obs-texts">'
        '<p class="ks3-obs-text" data-obs-alive>%s</p>'
        '<p class="ks3-obs-text" data-obs-dead hidden>%s</p></div>'
        '<p class="ks3-obs-verdict" data-obs-verdict>%s</p></div>'
        % (e(o.get("id", "")), e(" ".join(o.get("needs") or [])),
           rich(o.get("text", "")), rich(o.get("fail", "")),
           t(verdicts.get("alive") or ""))
        for o in obs)

    words = note.get("claim_word") or {}
    return (gate_html
            + '<div class="ks3-claimswitch" data-claimswitch%s data-total="%d" '
              'data-done-at="%d" data-on="%s" data-off="%s" '
              'data-alive="%s" data-dead="%s" data-all-on="%s" '
              'data-none-broken="%s" data-some-broken="%s" data-word-one="%s" '
              'data-word-many="%s">'
              '<p class="ks3-claims-label">%s</p>'
              '<div class="ks3-claims">%s</div>'
              '<p class="ks3-claims-label ks3-obs-label">%s</p>'
              '<div class="ks3-obs">%s</div>'
              '<p class="ks3-claim-note" data-claimnote role="status">%s</p>'
              '</div>'
            % (hide, len(claims), int(a.get("done_at") or 2),
               e(labels.get("on") or "ON"), e(labels.get("off") or "OFF"),
               e(verdicts.get("alive") or ""), e(verdicts.get("dead") or ""),
               e(note.get("all_on") or ""), e(note.get("none_broken") or ""),
               e(note.get("some_broken") or ""),
               e(words.get("one") or ""), e(words.get("many") or ""),
               t(labels.get("claims") or ""), rows,
               t(labels.get("observations") or ""), obs_rows,
               rich(note.get("all_on") or "")))
# The five drawings c2-01's zoom ladder steps through, validated at build time
# so a typo is a build error and never a blank canvas.
#
# ⚠️ This is NOT `zoom-ladder`. That kind is B1's plant→cell ladder — a slider,
# a tick row, an authored orange next-box per level, and its own validated
# `ZOOM_DRAWINGS` set that would raise on every name below. c2-01 has two step
# buttons, no ticks, no next-box and five drawings that do not exist there. Two
# different instruments that share the word zoom.
SCALE_DRAWINGS = {"wire", "grains", "scratches", "beyond-light", "lattice"}
def _scale_alt(alt, level):
    """The zoom canvas's aria-label. Same composition in Python and in JS."""
    return (alt.get("template", "")
            .replace("{scale}", level.get("scale", ""))
            .replace("{label}", (level.get("label") or "").lower()))
def r_mixture_compound_dish(a, act_id):
    """⊕ c2-03 `#s-bench` — iron and sulfur, before and after heating.

    ⚖️ **THE PROPORTION CONTROL IS DISABLED ONCE HEATED, AND THAT IS THE
    LESSON.** NOTES §3.3 is explicit. In the mixture a student picks any of
    three proportions and the drawing changes; heat it and the control refuses,
    because a compound's proportion is not adjustable. A generic tab group that
    stays live would delete the entire argument of the lesson and leave a
    picture. The refusal is enforced in the markup (`disabled`), in the JS
    (a re-check inside the handler, exactly as Design's own click guard does)
    and in the drawing (the heated state has no ratio to draw).

    ⚖️ The CONTRAST spine: three of the four tests give a vivid answer in both
    states and settle nothing; the quiet one — weigh what actually combines —
    settles everything. `settles` is authored per test and drives which of the
    two verdict words is emitted, so the pattern is data rather than prose.

    ⚑ NOTES flag 8 is the drawing Design most wants an examiner's eye on: iron
    sulfide is a 1:1 giant structure and the lattice is a fair KS3 picture of
    it, but it is not molecules. The 5 × 17 grid draws one iron and one sulfur
    joined by a stub, repeating — which is the honest reading.
    """
    tests = a.get("tests") or []
    ratios = a.get("ratios") or []
    states = a.get("states") or []
    if len(states) != 2:
        raise ValueError(
            "mixture-compound-dish %r takes exactly two states (before and "
            "after heating); got %d." % (act_id, len(states)))
    if not tests:
        raise ValueError("mixture-compound-dish %r declares no tests[]." % act_id)
    fracs = a.get("ratio_fracs") or []
    if len(fracs) != len(ratios):
        raise ValueError(
            "mixture-compound-dish %r declares %d ratio label(s) and %d "
            "fraction(s). The label a student reads and the mix the canvas "
            "draws are the same control and must not drift."
            % (act_id, len(ratios), len(fracs)))

    gate_html, hide = r_bench_gate(a.get("gate"))
    labels = a.get("labels") or {}
    words = a.get("verdict_words") or {}
    alt = a.get("dish_alt") or {}
    notes = a.get("dish_note") or {}
    caps = a.get("captions") or {}

    state_btns = "".join(
        '<button type="button" class="ks3-sim-seg-btn ks3-dish-state" '
        'data-heated="%s" aria-pressed="%s">%s</button>'
        % ("1" if st.get("heated") else "0",
           "true" if i == 0 else "false", t(st.get("label", "")))
        for i, st in enumerate(states))
    ratio_btns = "".join(
        '<button type="button" class="ks3-sim-seg-btn ks3-dish-ratio" '
        'data-ratio="%d" aria-pressed="%s">%s</button>'
        % (i, "true" if i == int(a.get("start_ratio") or 0) else "false",
           t(lab))
        for i, lab in enumerate(ratios))
    test_btns = "".join(
        '<button type="button" class="ks3-sim-seg-btn ks3-dish-test" '
        'data-test="%s" aria-pressed="%s">%s</button>'
        % (e(tt["id"]), "true" if i == 0 else "false", t(tt.get("name", "")))
        for i, tt in enumerate(tests))

    cards = []
    for i, tt in enumerate(tests):
        cards.append(
            '<div class="ks3-dish-result" data-testcard="%s"%s>'
            '<p class="ks3-dish-testname">%s</p>'
            '<div class="ks3-dish-cols">'
            '<div class="ks3-dish-col ks3-dish-before">'
            '<p class="ks3-dish-collabel">%s</p><p class="ks3-dish-body">%s</p>'
            '</div>'
            '<div class="ks3-dish-col ks3-dish-after">'
            '<p class="ks3-dish-collabel">%s</p><p class="ks3-dish-body">%s</p>'
            '</div></div>'
            '<p class="ks3-dish-verdict"><strong>%s</strong> %s</p></div>'
            % (e(tt["id"]), "" if i == 0 else " hidden",
               t(tt.get("name", "")),
               t(labels.get("before") or ""), rich(tt.get("before", "")),
               t(labels.get("after") or ""), rich(tt.get("after", "")),
               t(words.get("settles" if tt.get("settles") else "not") or ""),
               rich(tt.get("verdict", ""))))

    cfg = {"fracs": fracs, "captions": caps}
    canvas = ('<canvas class="ks3-dish-canvas" width="1700" height="560" '
              'role="img" aria-label="%s" data-dish-canvas></canvas>'
              % e(alt.get("mixed", "")))
    foot = ('<p class="ks3-dish-note" data-dish-note>%s</p>'
            % t(notes.get("mixed", "")))
    return (gate_html
            + '<div class="ks3-dish" data-dish%s data-total="%d" '
              'data-cfg="%s" data-alt-mixed="%s" data-alt-heated="%s" '
              'data-note-mixed="%s" data-note-heated="%s">'
              '<div class="ks3-dish-groups">'
              '<div class="ks3-dish-group"><p class="ks3-dish-grouplabel">%s</p>'
              '<div class="ks3-dish-btns">%s</div></div>'
              '<div class="ks3-dish-group"><p class="ks3-dish-grouplabel">%s</p>'
              '<div class="ks3-dish-btns">%s</div></div></div>'
              '%s'
              '<div class="ks3-dish-tests">%s</div>%s</div>'
            % (hide, len(tests),
               e(json.dumps(cfg, separators=(",", ":"), sort_keys=True,
                            ensure_ascii=False)),
               e(alt.get("mixed", "")), e(alt.get("heated", "")),
               e(notes.get("mixed", "")), e(notes.get("heated", "")),
               t(labels.get("dish") or ""), state_btns,
               t(labels.get("ratio") or ""), ratio_btns,
               _canvas_frame(canvas, foot), test_btns, "".join(cards)))
# `verdict-cards` and `origin-grid` are ONE component with two layouts and
# three headline types (map §10.2). They differ only in how the cards are laid
# out and what the card leads with; the contract — one shot per card, the
# unchosen options dim, the row's border goes to ink, a display-font answer
# word and a why paragraph — is identical, and three instances across two
# lessons is exactly the case for building it once.
_CARD_LAYOUTS = {"column", "grid"}
_CARD_HEADLINES = {"prose", "formula", "symbol"}
def r_verdict_cards(a, act_id):
    """⊕ c2-03 `#s-sort` · c2-04 `#s-read` · c2-04 `#s-sort`.

    One-shot commit-and-reveal cards. Nearest shipped kinds are `sort-rows`
    (chips into named columns) and `sort-task` (`ks3-hard`), and it is neither:
    both of those gate EVERY row behind one "open the answers" button, and
    this reveals each card the instant that card is decided.

    ⚠️ R3 / MRB-196 R10 — nothing marks correctness. The chosen option keeps
    the ordinary chosen treatment, the unchosen ones dim, the CARD's border
    goes to ink, and the why paragraph is one tone whether the student had it
    or not. The answer word is display type because it is the answer, not
    because it is a verdict on the student.

    ⚠️ NO ANSWER VALIDATION against the offered options, deliberately, and for
    the same reason `job-sort` has none: c2-04's `answer` strings are counts
    ("Three") offered against `['One','Two','Three','Four']`, but c2-03's are
    sentences that are not any of `['Mixture','Compound']`. Validating would
    refuse Design's payload at build time.
    """
    items = a.get("items") or []
    if not items:
        raise ValueError("verdict-cards %r declares no items[]." % act_id)
    layout = a.get("layout") or "column"
    headline = a.get("headline") or "prose"
    if layout not in _CARD_LAYOUTS:
        raise ValueError("verdict-cards %r layout %r; the drawn set is %s."
                         % (act_id, layout, ", ".join(sorted(_CARD_LAYOUTS))))
    if headline not in _CARD_HEADLINES:
        raise ValueError("verdict-cards %r headline %r; the drawn set is %s."
                         % (act_id, headline, ", ".join(sorted(_CARD_HEADLINES))))
    shared = a.get("options") or []

    cards = []
    for it in items:
        opts = it.get("options") or shared
        if not opts:
            raise ValueError(
                "verdict-cards %r item %r offers no options and the activity "
                "declares no shared options[]." % (act_id, it.get("id")))
        btns = "".join(
            '<button type="button" class="ks3-seg-btn ks3-vcard-opt" '
            'data-i="%d" aria-pressed="false">%s</button>' % (i, t(lab))
            for i, lab in enumerate(opts))
        # Three headline shapes, one element. `symbol` is c2-04's 42px display
        # letter set; `formula` is its mono 26px `CaCO₃`; `prose` is c2-03's
        # sentence. A `sub` line under the headline exists only where Design
        # draws one, which is `symbol` and `formula`.
        head = ('<p class="ks3-vcard-head" data-headline="%s">%s</p>'
                % (e(headline), rich(it.get("headline") or it.get("text", ""))))
        sub = ('<p class="ks3-vcard-sub">%s</p>' % rich(it["sub"])
               if it.get("sub") else "")
        # ⚠️ The answer WORD is optional, and its absence is Design's. c2-03's
        # and c2-04's `#s-read` cards open with a display-font answer ("Mixture."
        # / "Three elements.") before the reason; c2-04's `#s-sort` cards open
        # with the reason alone, because the bucket the student just pressed IS
        # the answer and repeating it would be the card telling them what they
        # already said. Emitting an empty `<strong>` would put a stray space
        # and an empty element on nine cards.
        answer = (('<strong class="ks3-vcard-answer">%s</strong> '
                   % t(it["answer"])) if it.get("answer") else "")
        cards.append(
            '<div class="ks3-vcard" data-vcard="%s">%s%s'
            '<div class="ks3-vcard-opts">%s</div>'
            '<p class="ks3-vcard-why" hidden data-reveal>%s%s</p></div>'
            % (e(it.get("id", "")), head, sub, btns,
               answer, rich(it.get("why", ""))))

    close = ('<div class="ks3-vcards-close" hidden data-vcards-close>'
             '<p>%s</p></div>' % rich(a["close"])) if a.get("close") else ""
    return ('<div class="ks3-vcards" data-vcards data-layout="%s" '
            'data-total="%d">%s%s</div>'
            % (e(layout), len(items), "".join(cards), close))
def r_formula_builder(a, act_id):
    """⊕ c2-05 `#s-builder` — three pairs × three × three, five substances.

    ⚖️ **"NOT A SUBSTANCE" IS THE TEACHING.** Twenty-two of the twenty-seven
    reachable combinations say so, and Design's NOTES §8 calls that "the first
    honest thing a formula builder can teach". A builder that only offered the
    five real ones would teach that any formula you can write exists, which is
    the misconception the block is aimed at.

    ⊕ **The opening substance is banked at mount, which Design's page does
    not do.** `mark()` is passed as the setState callback of the three control
    groups only, so the H₂O the instrument OPENS on is displayed, is one of the
    five, and can never be counted unless the student navigates away and back
    (map F6). That is an addition INSIDE a component Design drew and it
    contradicts nothing on the page: the substance is on screen, named, and
    drawn. Without it the progress readout opens at "0 of 5" while showing one.

    ⚠️ The not-a-substance name composes with ASCII DIGITS — `H3O2`, not
    `H₃O₂` — while every authored name in `known` uses proper subscripts. That
    is Design's page as written (line 641) and the page wins; changing it is a
    content decision, not a build one.
    """
    pairs = a.get("pairs") or []
    known = a.get("known") or {}
    counts = a.get("counts") or [1, 2, 3]
    if not pairs or not known:
        raise ValueError(
            "formula-builder %r needs both pairs[] and known{}." % act_id)
    ids = {p["id"] for p in pairs}
    for key in known:
        pid = key.split(":")[0]
        if pid not in ids:
            raise ValueError(
                "formula-builder %r knows %r, whose pair %r is not offered. "
                "A substance the controls cannot reach is a substance no "
                "student can find." % (act_id, key, pid))
    start = a.get("start") or {}
    gate_html, hide = r_bench_gate(a.get("gate"))
    labels = a.get("labels") or {}
    nf = a.get("not_found") or {}

    def first(p_id):
        return next(p for p in pairs if p["id"] == p_id)

    p0 = first(start.get("pair") or pairs[0]["id"])
    a0 = int(start.get("a") or counts[0])
    b0 = int(start.get("b") or counts[0])
    k0 = "%s:%d:%d" % (p0["id"], a0, b0)
    found0 = known.get(k0)

    pair_btns = "".join(
        '<button type="button" class="ks3-sim-seg-btn ks3-fb-pair" '
        'data-pair="%s" aria-pressed="%s">%s</button>'
        % (e(p["id"]), "true" if p["id"] == p0["id"] else "false",
           t("%s and %s" % (p.get("a", ""), p.get("b", ""))))
        for p in pairs)

    def count_btns(axis, chosen):
        return "".join(
            '<button type="button" class="ks3-sim-seg-btn ks3-fb-count" '
            'data-axis="%s" data-n="%d" aria-pressed="%s">%d</button>'
            % (axis, n, "true" if n == chosen else "false", n)
            for n in counts)

    # ⊕ 30 Aug 2026 (MRB-295/MRB-302 close-out). `known` is stored FLAT
    # ("H2O — water") because JS's own `name()` composes the not-found
    # branch the same way and the two have to agree. But the visible
    # caption is set with `.textContent` on every repaint — including the
    # one call made at mount — so without this, JS was overwriting the
    # server-rendered `sci(...)` subscripts (below) with the flat string
    # within milliseconds of the page loading. `name_html` carries the
    # already-subscripted form for JS to use on the FOUND branch only; the
    # not-found branch's ASCII digits are Design's own asymmetry (see
    # `_fb_name`'s docstring) and stay untouched.
    known_json = {k: dict(v, name_html=sci(v["name"])) if "name" in v else v
                  for k, v in known.items()}
    cfg = {"pairs": pairs, "known": known_json, "counts": counts,
           "colours": a.get("colours") or {},
           "not_found": nf, "captions": a.get("captions") or {},
           "alt": a.get("alt") or {},
           "start": {"pair": p0["id"], "a": a0, "b": b0}}
    canvas = ('<canvas class="ks3-fb-canvas" width="1700" height="520" '
              'role="img" aria-label="%s" data-fb-canvas></canvas>'
              % e(_fb_alt(a, found0)))
    foot = ('<p class="ks3-fb-name" data-fb-name>%s</p>'
            '<p class="ks3-fb-note" data-fb-note>%s</p>'
            % (sci(_fb_name(p0, a0, b0, found0, nf)),
               rich((found0 or {}).get("note") or nf.get("note", ""))))
    return (gate_html
            + '<div class="ks3-fb" data-fb%s data-total="%d" data-done-at="%d" '
              'data-cfg="%s">'
              '<div class="ks3-fb-groups">'
              '<div class="ks3-fb-group"><p class="ks3-fb-grouplabel">%s</p>'
              '<div class="ks3-fb-btns">%s</div></div>'
              '<div class="ks3-fb-group">'
              '<p class="ks3-fb-grouplabel" data-fb-label="a">%s</p>'
              '<div class="ks3-fb-btns">%s</div></div>'
              '<div class="ks3-fb-group">'
              '<p class="ks3-fb-grouplabel" data-fb-label="b">%s</p>'
              '<div class="ks3-fb-btns">%s</div></div></div>%s</div>'
            % (hide, len(known), int(a.get("done_at") or len(known)),
               e(json.dumps(cfg, separators=(",", ":"), sort_keys=True,
                            ensure_ascii=False)),
               t(labels.get("pairs") or ""), pair_btns,
               t(p0.get("aName", "")), count_btns("a", a0),
               t(p0.get("bName", "")), count_btns("b", b0),
               _canvas_frame(canvas, foot)))
def _fb_name(pair, na, nb, found, nf):
    """The name under the drawing. Composed the same way in Python and in JS.

    ⚠️ ASCII digits on the not-found branch, subscripts on the authored names.
    Design's own asymmetry (page line 641), reproduced rather than tidied.
    """
    if found:
        return found.get("name", "")
    return "%s%s%s%s%s" % (pair.get("a", ""), na if na > 1 else "",
                           pair.get("b", ""), nb if nb > 1 else "",
                           nf.get("name_suffix", ""))
def _fb_alt(a, found):
    """The builder canvas's aria-label. Three-way, composed in both languages."""
    alt = a.get("alt") or {}
    if not found:
        return alt.get("none", "")
    tail = alt.get("giant" if found.get("giant") else "molecule", "")
    return alt.get("template", "").replace("{name}", found.get("name", "")) + tail
def r_model_limit(a, act_id):
    """⊕ c2-05 `#s-limit` — the MODEL family's *where it breaks* step.

    Two cards, a commit and an ungated reveal. The light/ink asymmetry IS the
    argument and is not decoration: the molecule sits on a card and the giant
    structure sits on ink, so the thing the model does not cover looks
    different before a word of it is read.

    ⚠️ THREE options, not four. Every other commit in KS3 offers four, and
    this is recorded (map N9) so it is not "corrected" to four by a later pass.

    ⚠️ The reveal is UNGATED BY THE ANSWER — it opens on any commitment.
    Commitment, never marking (R3).
    """
    cards = a.get("panels") or []
    if len(cards) != 2:
        raise ValueError(
            "model-limit %r takes exactly two contrast cards; got %d. The "
            "light/ink pair is the argument, and one card cannot make it."
            % (act_id, len(cards)))
    grounds = [c.get("ground") for c in cards]
    if sorted(grounds) != ["card", "ink"]:
        raise ValueError(
            "model-limit %r draws grounds %s; it takes one `card` and one "
            "`ink`. Two cards on the same ground is a comparison table, which "
            "is not what Design drew." % (act_id, grounds))
    # The commit line sits BETWEEN the cards and the options, which is the one
    # slot `r_activity`'s fixed order does not have — the shell's `prompt` is
    # already the lede above the cards. It belongs to the component because
    # Design draws it inside the block, at 19px/700, not as a second lede.
    commit = ('<p class="ks3-limit-commit">%s</p>' % t(a["commit"])
              if a.get("commit") else "")
    return ('<div class="ks3-limit" data-limit>'
            '<div class="ks3-limit-cards">%s</div>%s</div>'
            % ("".join(
                '<div class="ks3-limit-card" data-ground="%s">'
                '<p class="ks3-limit-caption">%s</p>'
                '<p class="ks3-limit-body">%s</p></div>'
                % (e(c.get("ground", "card")), sci(c.get("caption", "")),
                   rich(c.get("text", "")))
                for c in cards), commit))
def r_balance_bench(a, act_id):
    """⊕ c2-06 `#s-balance` — two reactions × two vessels on one balance.

    ⚖️ **THE THIRD TILE NEVER MEASURES ANYTHING**, and it is the whole
    QUANTITATIVE move. `Mass before` and `Mass after` are read off the display;
    `Where it went` reads *not measured — you work it out* and takes no data,
    for ever. It is the same refusal `p3-01`'s light gates make. It has to be a
    real tile beside the two that do report, or the refusal reads as prose
    somebody forgot to fill in.

    ⚖️ The VESSEL CHANGES THE PICTURE — a sealed flask gets a drawn bung — and
    a run that moves gas draws the gas leaving or joining. A control that
    changes only a number teaches that the apparatus is incidental.

    ⚠️ `showAfter` RESETS on every control change (Design's own rule): switch
    reaction or vessel and the balance goes back to its before-reading, because
    it is now a different run and the after-mass of the last one is not a fact
    about this one.
    """
    runs = a.get("runs") or {}
    reactions = a.get("reactions") or []
    vessels = a.get("vessels") or []
    if not runs or not reactions or not vessels:
        raise ValueError(
            "balance-bench %r needs runs{}, reactions[] and vessels[]." % act_id)
    for r in reactions:
        for v in vessels:
            key = "%s:%s" % (r["id"], v["id"])
            if key not in runs:
                raise ValueError(
                    "balance-bench %r offers %r but declares no run for it. "
                    "Every combination the controls can reach must have a "
                    "reading." % (act_id, key))
    tiles = a.get("tiles") or []
    if len(tiles) != 3:
        raise ValueError(
            "balance-bench %r draws %d tile(s); it takes three, and the third "
            "is the one that refuses to measure." % (act_id, len(tiles)))

    gate_html, hide = r_bench_gate(a.get("gate"))
    labels = a.get("labels") or {}
    dec = int(a.get("decimals", 2))
    r0, v0 = reactions[0]["id"], (a.get("start_vessel") or vessels[0]["id"])
    first = runs["%s:%s" % (r0, v0)]

    def group(cls, key, items, chosen):
        return "".join(
            '<button type="button" class="ks3-sim-seg-btn %s" data-%s="%s" '
            'aria-pressed="%s">%s</button>'
            % (cls, key, e(i["id"]), "true" if i["id"] == chosen else "false",
               t(i.get("label", "")))
            for i in items)

    tile_html = "".join(
        '<div class="ks3-bal-tile"><p class="ks3-bal-tile-label">%s</p>'
        '<p class="ks3-bal-tile-value%s"%s>%s</p></div>'
        % (t(tl.get("label", "")),
           "" if tl.get("body") else " ks3-bal-tile-mono",
           "" if tl.get("body") else ' data-tile="%s"' % e(tl.get("id", "")),
           t(tl.get("body") or _mass(first["before"] if tl.get("id") == "before"
                                     else None, dec, labels)))
        for tl in tiles)

    cfg = {"runs": runs, "labels": labels, "decimals": dec,
           "run_labels": a.get("run_labels") or {},
           "liquids": a.get("liquid_colours") or {},
           "gas_labels": a.get("gas_labels") or {},
           "alt": a.get("alt") or {},
           "start": {"reaction": r0, "vessel": v0}}
    canvas = ('<canvas class="ks3-bal-canvas" width="1700" height="560" '
              'role="img" aria-label="%s" data-bal-canvas></canvas>'
              % e(_bal_alt(a, v0, first["before"], False, dec)))
    foot = ('<button type="button" class="ks3-bal-run" data-bal-run>%s</button>'
            '<p class="ks3-bal-status" data-bal-status>%s</p>'
            % (t((a.get("run_labels") or {}).get("idle", "")),
               t(labels.get("status_idle", ""))))
    return (gate_html
            + '<div class="ks3-bal" data-bal%s data-total="%d" '
              'data-done-at="%d" data-cfg="%s">'
              '<div class="ks3-bal-groups">'
              '<div class="ks3-bal-group"><p class="ks3-bal-grouplabel">%s</p>'
              '<div class="ks3-bal-btns">%s</div></div>'
              '<div class="ks3-bal-group"><p class="ks3-bal-grouplabel">%s</p>'
              '<div class="ks3-bal-btns">%s</div></div></div>'
              '%s<div class="ks3-bal-tiles">%s</div>'
              '<p class="ks3-bal-note" data-bal-note>%s</p></div>'
            % (hide, len(runs), int(a.get("done_at") or len(runs)),
               e(json.dumps(cfg, separators=(",", ":"), sort_keys=True,
                            ensure_ascii=False)),
               t(labels.get("reaction") or ""),
               group("ks3-bal-rxn", "rxn", reactions, r0),
               t(labels.get("vessel") or ""),
               group("ks3-bal-vessel", "vessel", vessels, v0),
               _canvas_frame(canvas, foot, row=True), tile_html,
               rich(labels.get("idle_note", ""))))
def _mass(value, dec, labels):
    """`152.00 g`, or the em-dash the After tile shows before a run."""
    if value is None:
        return labels.get("unmeasured") or "—"
    return ("%%.%df %%s" % dec) % (value, labels.get("unit") or "g")
def _bal_alt(a, vessel, mass, after, dec):
    """The balance canvas's aria-label. Composed the same way in JS."""
    alt = a.get("alt") or {}
    return (alt.get("template", "")
            .replace("{vessel}", alt.get(vessel, ""))
            .replace("{mass}", ("%%.%df" % dec) % mass)
            .replace("{when}", alt.get("after" if after else "before", "")))
def r_fifa_pick(lesson, a, act_id):
    """⊕ c2-06 `#s-build` — MRB-204 part 4, and NOT `fifa-construct`.

    The shipped `fifa-construct` renders four free-text inputs, a Check button,
    a model `<ol>` and a success-criteria tick list, and asserts
    `len(fields) == len(model) == len(success)`. Design's page is a different
    mechanism: two multiple-choice ladders of three, one number field beside a
    unit `<select>`, and a four-step ink reveal that quotes the student's own
    input back. Three commitments against four model lines and no criteria at
    all — the existing assertions would raise on it, and rightly.

    ⚖️ The two ladders are MULTIPLE CHOICE ON PURPOSE. A student who cannot yet
    write `152.00 = 149.80 + mass of gas` can still recognise it, and the two
    distractors are the two real errors — conserving only the solid, and adding
    the gas to the wrong side. A free-text box would fail them silently.

    ⚖️ THE BUTTON IS LOCKED UNTIL ALL FOUR PARTS ARE SET — both picks, a
    number, and a unit. The unit is a separate commitment because "2.2" is not
    an answer to a question about mass.
    """
    steps = a.get("steps") or []
    picks = a.get("picks") or []
    field = a.get("field") or {}
    if len(picks) != 2:
        raise ValueError(
            "fifa-pick %r declares %d pick ladder(s); it takes two — the rule "
            "and the insertion." % (act_id, len(picks)))
    if not steps:
        raise ValueError("fifa-pick %r reveals no steps[]." % act_id)
    if not field.get("units"):
        raise ValueError(
            "fifa-pick %r offers no units[]. The unit is a separate "
            "commitment: `2.2` is not an answer to a question about mass."
            % act_id)

    panels = []
    for i, p in enumerate(picks):
        opts = "".join(
            '<button type="button" class="ks3-pick-opt" data-group="%d" '
            'data-i="%d" aria-pressed="false">%s</button>' % (i, j, t(o))
            for j, o in enumerate(p.get("options") or []))
        panels.append(
            '<div class="ks3-pick-panel"><p class="ks3-pick-label">%s</p>'
            '<div class="ks3-pick-opts">%s</div></div>'
            % (t(p.get("label", "")), opts))

    # ⊕ N10 — the visually-hidden label. No `.ks3-sr-only` existed in
    # `shared/ks3.css`; Design inlines `position:absolute; left:-9999px` twice.
    # One class now, because the next form control will want it too.
    aid, uid = "%s-ans" % act_id, "%s-unit" % act_id
    # ⚠️ THE PLACEHOLDER OPTION CARRIES AN EMPTY VALUE, and that is
    # load-bearing rather than tidy: the unit is one of the four commitments
    # the open button waits for, and a placeholder with its own value ("choose
    # a unit") satisfies `unit.value` — so the gate opens on a student who
    # never chose a unit. Measured in a browser, not read off the source.
    units = ('<option value="">%s</option>' % t(field["unit_placeholder"])
             if field.get("unit_placeholder") else "")
    units += "".join('<option value="%s">%s</option>' % (e(u), t(u))
                     for u in field["units"])
    panels.append(
        '<div class="ks3-pick-panel"><p class="ks3-pick-label">%s</p>'
        '<div class="ks3-pick-answer">'
        '<label class="ks3-sr-only" for="%s">%s</label>'
        '<input class="ks3-pick-input" type="text" inputmode="decimal" '
        'id="%s" placeholder="%s" data-pick-ans>'
        '<label class="ks3-sr-only" for="%s">%s</label>'
        '<select class="ks3-sim-units ks3-pick-unit" id="%s" data-pick-unit>'
        '%s</select></div></div>'
        # ⚠️ NO `value` attribute on the input. B1 already fixed this once:
        # an authored `value` is an attribute, the runtime re-renders, and the
        # student's own typing is wiped on the next state change.
        % (t(field.get("label", "")), e(aid), t(field.get("hint", "")),
           e(aid), e(field.get("placeholder", "")), e(uid),
           t(field.get("unit_hint", "")), e(uid), units))

    reveal = "".join(
        '<div class="ks3-pick-step">'
        '<span class="ks3-pick-chip" aria-hidden="true">%s</span>'
        '<div class="ks3-pick-stepbody"><p class="ks3-pick-steplabel">%s</p>'
        '<p class="ks3-pick-stepline">%s</p>'
        '<p class="ks3-pick-stepnote">%s</p></div></div>'
        % (t(s.get("letter", "")), t(s.get("label", "")),
           t(s.get("line", "")), rich(s.get("note", "")))
        for s in steps)

    close = a.get("close") or {}
    return ('<div class="ks3-pick" data-pick data-total="3" '
            'data-close="%s" data-blank="%s" data-done-label="%s">'
            '<div class="ks3-pick-panels">%s</div>'
            '<div class="ks3-pick-foot">'
            '<button type="button" class="ks3-reveal-btn ks3-pick-btn" '
            'data-pick-open disabled>%s</button>'
            '<span class="ks3-pick-progress" data-pick-progress>%s</span>'
            '</div>'
            '<div class="ks3-pick-reveal" hidden data-reveal>'
            '<p class="ks3-pick-revealhead">%s</p>%s'
            '<p class="ks3-pick-close" data-pick-close></p></div></div>'
            % (e(close.get("template", "")), e(close.get("blank") or "—"),
               e((a.get("progress") or {}).get("done", "")),
               "".join(panels),
               t(a.get("button", "")),
               t((a.get("progress") or {}).get("format", "")
                 .replace("{n}", "0")),
               t(a.get("reveal_head", "")), reveal))
def r_test_budget_bench(a, act_id):
    """⊕ c2-02 `#s-bench` — six samples, four tests, and eight tests to spend.

    ⚖️ **THE BUDGET IS THE PEDAGOGY, NOT A GAME MECHANIC.** With unlimited
    tests a student runs everything and learns nothing about which evidence
    discriminates; the whole lesson is discovering that *looks like a metal*,
    *conducts* and *is shiny* are the three most interesting results you can
    buy and all three are worthless. Design's NOTES §3.2 says it in as many
    words: "if Code drops the budget the lesson quietly becomes a
    click-through." So the budget is required, it is validated as reachable,
    and it is GLOBAL across all six samples rather than per-sample.

    ⚠️ THE INSTRUMENT NEVER MARKS. The verdict panel fires on the student's
    verdict whether or not that verdict was right, and it is the only place a
    sample is named. `element` is authored on every sample and read by nothing
    (map N16) — it is correctness data waiting for a marker that R3 says must
    not arrive here. Kept, and flagged rather than deleted.

    ⚠️ Emit-all-show-one, as the board does: every sample panel is in the
    document and one is shown, so returning to a sample finds its results and
    its verdict exactly as they were left and no state lives outside the DOM.
    """
    samples = a.get("samples") or []
    tests = a.get("tests") or []
    if not samples or not tests:
        raise ValueError(
            "test-budget-bench %r needs both samples[] and tests[]." % act_id)
    budget = int(a.get("budget") or 0)
    if budget < len(samples):
        # Fewer tests than samples means a sample that can never be tested at
        # all, which is not a hard lesson — it is a broken one.
        raise ValueError(
            "test-budget-bench %r has a budget of %d over %d samples. A budget "
            "below one test per sample makes the bench unusable rather than "
            "demanding." % (act_id, budget, len(samples)))
    for s in samples:
        missing = [t["id"] for t in tests if t["id"] not in (s.get("results") or {})]
        if missing:
            raise ValueError(
                "test-budget-bench %r sample %r has no result for test(s) %s. "
                "A test a student can spend a budget point on must say "
                "something." % (act_id, s.get("id"), missing))

    gate_html, hide = r_bench_gate(a.get("gate"))
    labels = a.get("labels") or {}
    verdicts = a.get("verdicts") or []

    tabs = "".join(
        '<button type="button" class="ks3-seg-btn ks3-sample-tab" '
        'data-sample="%s" aria-pressed="%s"><span data-tab-label>%s</span>'
        '</button>'
        % (e(s["id"]), "true" if i == 0 else "false", t(s.get("tab", "")))
        for i, s in enumerate(samples))

    panels = []
    for i, s in enumerate(samples):
        test_btns = "".join(
            '<button type="button" class="ks3-seg-btn ks3-test-btn" '
            'data-test="%s" aria-pressed="false">%s</button>'
            % (e(tt["id"]), t(tt.get("label", ""))) for tt in tests)
        results = "".join(
            '<li class="ks3-result" data-result="%s" hidden>'
            '<p class="ks3-result-test">%s</p>'
            '<p class="ks3-result-body">%s</p></li>'
            % (e(tt["id"]), t(tt.get("label", "")),
               rich((s.get("results") or {}).get(tt["id"], "")))
            for tt in tests)
        vbtns = "".join(
            '<button type="button" class="ks3-seg-btn ks3-verdict-btn" '
            'data-verdict="%s" aria-pressed="false">%s</button>'
            % (e(v.get("id", "")), t(v.get("label", "")))
            for v in verdicts)
        panels.append(
            '<div class="ks3-sample" data-sample="%s"%s>'
            '<p class="ks3-sample-name">%s</p>'
            '<p class="ks3-sample-look">%s</p>'
            '<div class="ks3-sample-tests">%s</div>'
            '<ul class="ks3-results" hidden data-results role="list">%s</ul>'
            '<div class="ks3-sample-verdict">'
            '<p class="ks3-sample-ask">%s</p>'
            '<div class="ks3-verdict-btns">%s</div>'
            '<div class="ks3-verdict-panel" hidden data-verdict-panel>'
            '<p class="ks3-verdict-name">%s</p>'
            '<p class="ks3-verdict-why">%s</p></div></div></div>'
            % (e(s["id"]), "" if i == 0 else " hidden",
               t(s.get("name", "")), rich(s.get("look", "")), test_btns,
               results, t(labels.get("ask") or ""), vbtns,
               t(s.get("name2", "")), rich(s.get("why", ""))))

    close = ('<div class="ks3-bench-close" hidden data-bench-close><p>%s</p>'
             '</div>' % rich(a["close"])) if a.get("close") else ""
    return (gate_html
            + '<div class="ks3-budget" data-budgetbench%s data-budget="%d" '
              'data-total="%d" data-marker="%s">'
              '<div class="ks3-sample-tabs">%s</div>%s%s</div>'
            % (hide, budget, len(samples), e(labels.get("decided") or " ·"),
               tabs, "".join(panels), close))
def r_scale_zoom(a, act_id):
    """⊕ c2-01 `#s-scale` — five steps from a centimetre of wire to the atoms.

    ⚖️ The lesson is that FOUR OF THE FIVE STEPS SHOW NOTHING NEW. Copper stays
    copper down past the reach of any light microscope, and the fourth drawing
    says so in words on the canvas rather than showing a smaller orange thing.
    Collapsing the ladder to "wire, then atoms" would delete the argument and
    leave the picture.

    Stage 3 is done when all five levels have been REACHED BY STEPPING IN —
    `seenZoom` seeds level 0 and only the in-button adds to it (map §2.4), so
    backing out and climbing again is the only route. Reproduced, not tightened.
    """
    levels = a.get("levels") or []
    if len(levels) < 2:
        raise ValueError("scale-zoom %r declares %d level(s); it steps between "
                         "at least two." % (act_id, len(levels)))
    for lv in levels:
        if lv.get("drawing") not in SCALE_DRAWINGS:
            raise ValueError(
                "scale-zoom %r level %r names drawing %r; the drawn set is %s."
                % (act_id, lv.get("scale"), lv.get("drawing"),
                   ", ".join(sorted(SCALE_DRAWINGS))))
    labels = a.get("labels") or {}
    alt = a.get("alt") or {}
    start = int(a.get("start") or 0)
    first = levels[start]

    foot = ('<div class="ks3-scale-controls">'
            '<button type="button" class="ks3-sim-seg-btn ks3-scale-btn" '
            'data-step="-1"%s>%s</button>'
            '<button type="button" class="ks3-sim-seg-btn ks3-scale-btn" '
            'data-step="1"%s>%s</button>'
            '<p class="ks3-scale-readout" data-scale-readout>%s</p></div>'
            % (" disabled" if start == 0 else "", t(labels.get("out") or ""),
               " disabled" if start >= len(levels) - 1 else "",
               t(labels.get("in") or ""), t(first.get("scale", ""))))
    canvas = ('<canvas class="ks3-scale-canvas" width="1800" height="620" '
              'role="img" aria-label="%s" data-scale-canvas></canvas>'
              % e(_scale_alt(alt, first)))
    return ('<div class="ks3-scale" data-scalezoom data-total="%d" '
            'data-start="%d" data-levels="%s" data-alt="%s">%s'
            '<p class="ks3-scale-note" data-scale-note>%s</p></div>'
            % (len(levels), start,
               e(json.dumps(levels, separators=(",", ":"), sort_keys=True,
                            ensure_ascii=False)),
               e(alt.get("template", "")),
               _canvas_frame(canvas, foot), rich(first.get("note", ""))))


# ── registrations ────────────────────────────────────────────────────────
KIND_SHELL = {
    'claim-switch': ("ks3-claim-block",
                      ' data-instrument data-claimblock data-stage-done="0"'),
    'scale-zoom': ("ks3-scale-block",
                      ' data-instrument data-scaleblock data-stage-done="0"'),
    'test-budget-bench': ("ks3-budget-block",
                          ' data-instrument data-budgetblock '
                          'data-stage-done="0"'),
    'mixture-compound-dish': ("ks3-dish-block",
                              ' data-instrument data-dishblock '
                              'data-stage-done="0"'),
    'verdict-cards': ("ks3-vcards-block",
                      ' data-instrument data-vcardsblock data-stage-done="0"'),
    'formula-builder': ("ks3-fb-block",
                        ' data-instrument data-fbblock data-stage-done="0"'),
    'model-limit': ("ks3-limit-block", ""),
    'balance-bench': ("ks3-bal-block",
                      ' data-instrument data-balblock data-stage-done="0"'),
    'fifa-pick': ("ks3-pick-block",
                  ' data-instrument data-pickblock data-stage-done="0"'),
}

KIND_FN = {
    'claim-switch': r_claim_switch,
    'scale-zoom': r_scale_zoom,
    'test-budget-bench': r_test_budget_bench,
    'mixture-compound-dish': r_mixture_compound_dish,
    'verdict-cards': r_verdict_cards,
    'formula-builder': r_formula_builder,
    'model-limit': r_model_limit,
    'balance-bench': r_balance_bench,
    'fifa-pick': r_fifa_pick,
}


# ── lean wave · C2's drawn figures ──────────────────────────────────────
#
# "particle-boxes": labelled boxes stacked in one column (one per row, so each reads at full size
# on a phone), each holding circles marked with element symbols. fig["data"] =
#   {"arrow": bool,                      # optional drawn arrow between the first two boxes
#    "boxes": [{"label": str,            # 14px bold above the box ("2H2O" gets real subscripts)
#               "tag": str,              # optional, mono, under the label
#               "count": str,            # optional caption line under the box
#               "layout": "grid" | "spread" | "clumps" | "single",
#               # grid:   "atom": sym   or   "atoms": [a, b] with "pattern": "alternate";
#               #         "rows", "cols"; "edges": "continue" runs the lattice off every edge
#               # spread / single: "groups": [[sym, ...], ...], one joined molecule each;
#               #         "shape": "straight" (default) | "bent" (A-X-B, X central) | "chain" | "pyramid" (X-A-B-C: first atom central)
#               # clumps: "clumps": [[sym, ...], ...], each a touching cluster
#              }]}
# Atoms: a fixed fill per element with an ink outline; the symbol is drawn in a fixed dark or
# white ink chosen for that fill, so it reads in light AND dark themes.

_PB_R = {"H": 10, "O": 14, "C": 14, "N": 14, "He": 14, "Na": 13, "Cl": 15, "Cu": 15, "Fe": 15,
         "S": 14, "Co": 15, "Pb": 16, "Au": 14, "Mg": 15}
# fill, symbol ink
_PB_COL = {"H": ("#FFFFFF", "#221E1B"), "O": ("#D8412F", "#FFFFFF"), "C": ("#3B3835", "#FFFFFF"),
           "N": ("#3B6FD4", "#FFFFFF"), "Cu": ("#B8703A", "#FFFFFF"), "Fe": ("#9A9A9A", "#221E1B"),
           "S": ("#F2D23C", "#221E1B"), "Na": ("#8A5CC2", "#FFFFFF"), "Cl": ("#3E9B4F", "#FFFFFF"),
           "He": ("#E4D4F2", "#221E1B"), "Au": ("#E8B923", "#221E1B"), "Pb": ("#8C8C94", "#FFFFFF"),
           "Co": ("#5F7F9F", "#FFFFFF"), "Mg": ("#D6D6D6", "#221E1B")}
_PB_BW, _PB_BX = 310, 8


def _pb_atom(sym, cx, cy, text=True):
    if sym not in _PB_R:
        raise ValueError("particle-boxes: no drawing for element %r" % sym)
    fill, ink = _PB_COL[sym]
    return (_circle(cx, cy, _PB_R[sym], fill=fill, stroke=_SVG_INK, w=2, data_part="atom", data_key=sym)
            + (_label(cx, cy + 4.6, sym, size=13, fill=ink, weight="700", data_part="symbol", data_key=sym)
               if text else ""))


def _pb_group(syms, shape="straight"):
    """[(sym, dx, dy)] for one joined molecule, atoms touching, plus (w, h) and the offset of its
    bounding box's top-left from the origin."""
    import math
    r = [_PB_R[s] for s in syms]
    pos = []
    if shape == "bent" and len(syms) == 3:
        d = r[1] + r[0]
        sx, sy = d * math.sin(math.radians(52)), d * math.cos(math.radians(52))
        pos = [(syms[0], -sx, sy), (syms[1], 0.0, 0.0), (syms[2], sx, sy)]
    elif shape == "pyramid" and len(syms) == 4:
        # the first atom in the middle, the other three touching it 120 degrees apart
        pos = [(syms[0], 0.0, 0.0)]
        for sym, ang in zip(syms[1:], (-90, 30, 150)):
            d = r[0] + _PB_R[sym]
            pos.append((sym, d * math.cos(math.radians(ang)), d * math.sin(math.radians(ang))))
    elif shape == "chain" and len(syms) == 4:
        d_h = r[0] + r[1]
        a = math.radians(55)
        o1x = 0.0
        o2x = r[1] + r[2]
        pos = [(syms[0], o1x - d_h * math.cos(a), -d_h * math.sin(a)),
               (syms[1], o1x, 0.0), (syms[2], o2x, 0.0),
               (syms[3], o2x + (r[2] + r[3]) * math.cos(a), (r[2] + r[3]) * math.sin(a))]
    else:
        x = 0.0
        for i, s in enumerate(syms):
            if i:
                x += r[i - 1] + r[i]
            pos.append((s, x, 0.0))
    x0 = min(p[1] - _PB_R[p[0]] for p in pos)
    x1 = max(p[1] + _PB_R[p[0]] for p in pos)
    y0 = min(p[2] - _PB_R[p[0]] for p in pos)
    y1 = max(p[2] + _PB_R[p[0]] for p in pos)
    return [(s, dx - x0, dy - y0) for s, dx, dy in pos], x1 - x0, y1 - y0


def _pb_clump(syms):
    """A touching cluster: rows of ceil(sqrt(n)) atoms, alternate rows nudged half a step."""
    import math
    n = len(syms)
    per = max(1, int(math.ceil(math.sqrt(n))))
    r = _PB_R[syms[0]]
    pos = []
    for i, s in enumerate(syms):
        row, col = divmod(i, per)
        pos.append((s, 2 * r * col + (r if row % 2 else 0) + r, row * 1.74 * r + r))
    w = max(p[1] for p in pos) + r
    h = max(p[2] for p in pos) + r
    return pos, w, h


def _pb_flow(groups, inner_w, gap=16, row_gap=12):
    """Pack (pos, w, h) groups into balanced rows no wider than inner_w -> [[group,...], ...]."""
    n = len(groups)
    def rows_for(k):
        rows, cur, cw = [], [], 0
        for g in groups:
            if cur and cw + gap + g[1] > inner_w:
                rows.append(cur); cur, cw = [], 0
            cw = cw + (gap if cur else 0) + g[1]
            cur.append(g)
        rows.append(cur)
        return rows
    greedy = rows_for(n)
    k = max(len(r) for r in greedy)
    nrows = len(greedy)
    per = -(-n // nrows)
    balanced = [groups[i:i + per] for i in range(0, n, per)]
    ok = all(sum(g[1] for g in r) + gap * (len(r) - 1) <= inner_w for r in balanced)
    return balanced if ok else greedy


def _pb_text(x, y, s, **kw):
    """A label whose digits after a letter are real subscripts (only for space-free formula labels)."""
    node = _label(x, y, s, **kw)
    if " " in s or not re.search(r"[A-Za-z]\d", s):
        return node
    parts = re.sub(r"(?<=[A-Za-z])(\d+)", lambda m: "\x00" + m.group(1) + "\x01", s)
    parts = parts.replace("\x00", '<tspan baseline-shift="sub" font-size="75%">').replace("\x01", "</tspan>")
    return node.replace(">%s</text>" % s, ">%s</text>" % parts, 1)


def _particle_boxes(fig):
    from ks3_art.b4 import _b4_arrow
    data = fig.get("data") or {}
    boxes = data.get("boxes") or []
    if not boxes:
        raise ValueError("figure %r: particle-boxes needs data.boxes" % fig.get("id"))
    W, BX, BW = 326, _PB_BX, _PB_BW
    out, defs = [], []
    y = 6
    PAD = 14
    for bi, b in enumerate(boxes):
        label, tag, count = b["label"], b.get("tag"), b.get("count")
        out.append(_pb_text(BX, y + 15, label, size=14, weight="700", anchor="start",
                            data_part="box-label", data_key=label))
        top = y + 24
        if tag:
            out.append(_mono(BX, y + 32, tag, size=13, fill=_SVG_INK_FAINT, weight="600", anchor="start",
                             data_part="box-tag", data_key=label))
            top = y + 42
        lay = b.get("layout")
        body, h = [], 0
        if lay == "grid":
            syms = b.get("atoms") or [b["atom"]]
            alt = len(syms) > 1
            pitch = (_PB_R[syms[0]] + _PB_R[syms[1]]) if alt else 2 * _PB_R[syms[0]]
            rows, cols = b["rows"], b["cols"]
            cont = b.get("edges") == "continue"
            if cont:
                cols = int(BW // pitch) + 3
                h = rows * pitch
                x0 = BX + BW / 2 - cols * pitch / 2
                y0 = top
            else:
                h = rows * pitch + 2 * PAD
                x0 = BX + BW / 2 - cols * pitch / 2
                y0 = top + PAD
            for i in range(rows):
                for j in range(cols):
                    s = syms[(i + j) % 2] if alt else syms[0]
                    ax = x0 + pitch * (j + .5)
                    # a lattice that runs off the box edge: a clipped circle carries no half-letter
                    whole = (not cont) or (ax - _PB_R[s] >= BX and ax + _PB_R[s] <= BX + BW)
                    body.append(_pb_atom(s, ax, y0 + pitch * (i + .5), text=whole))
            if cont:
                cid = "%s-clip%d" % (fig["id"], bi)
                defs.append('<clipPath id="%s"><rect x="%s" y="%s" width="%s" height="%s" rx="10"/></clipPath>'
                            % (cid, BX, top, BW, h))
                body = ['<g clip-path="url(#%s)">' % cid] + body + ['</g>']
        elif lay in ("spread", "single", "clumps"):
            if lay == "clumps":
                groups = [_pb_clump(c) for c in b["clumps"]]
            else:
                shape = b.get("shape", "straight")
                groups = [_pb_group(g, shape) for g in b["groups"]]
            rows = _pb_flow(groups, BW - 2 * PAD)
            rh = [max(g[2] for g in r) for r in rows]
            h = sum(rh) + 12 * (len(rows) - 1) + 2 * PAD
            yy = top + PAD
            for r, hh in zip(rows, rh):
                rw = sum(g[1] for g in r) + 16 * (len(r) - 1)
                xx = BX + BW / 2 - rw / 2
                for pos, gw, gh in r:
                    oy = yy + (hh - gh) / 2
                    for s, dx, dy in pos:
                        body.append(_pb_atom(s, xx + dx, oy + dy))
                    xx += gw + 16
                yy += hh + 12
        else:
            raise ValueError("figure %r: particle-boxes layout %r" % (fig.get("id"), lay))
        out.append(_rect(BX, top, BW, h, rx=10, fill=_SVG_INSET, stroke=_SVG_INK, w=2.5,
                         data_part="box", data_key=label))
        out.extend(body)
        y = top + h
        if count:
            out.append(_mono(BX, y + 20, count, size=13, fill=_SVG_INK_FAINT, weight="600", anchor="start",
                             data_part="count", data_key=label))
            y += 28
        if bi < len(boxes) - 1:
            if data.get("arrow") and bi == 0:
                out.append(_b4_arrow(W / 2, y + 6, W / 2, y + 46, w=3, head=12, data_part="arrow"))
                y += 52
            else:
                y += 20
    H = y + 8
    return (_svg_open(fig, W, H) + ("<defs>%s</defs>" % "".join(defs) if defs else "")
            + '<g stroke-linecap="round" stroke-linejoin="round">' + "".join(out) + '</g></svg>')


# "open-sealed-flask": two set-ups stacked, each on a top-pan balance with a Before/After readout.
#   fig["data"] = {"panels": [{"label", "vessel": "flask" | "bottle", "before", "after",
#                              "arrow_label": str  (flask: drawn arrow out of the neck with this text)
#                              "note": str         (bottle: accent note beside the bottle)}]}
def _osf_panel(p, oy, cx=163):
    from ks3_art.b4 import _b4_arrow, _B4_BLUE, _B4_BLUE_TINT, _B4_LEADER
    out = []
    out.append(_label(8, oy + 16, p["label"], size=14, weight="700", anchor="start",
                      data_part="panel-label", data_key=p["label"]))
    vy = oy + 66            # top of the vessel
    pan_y = vy + 102
    if p["vessel"] == "flask":
        out.append(_path("M %s,%s L %s,%s L %s,%s L %s,%s Z" % (cx - 40, vy + 76, cx - 55, pan_y - 2,
                                                              cx + 55, pan_y - 2, cx + 40, vy + 76),
                         fill=_B4_BLUE_TINT, data_part="liquid"))
        out.append(_line(cx - 40, vy + 76, cx + 40, vy + 76, stroke=_B4_BLUE, w=2, data_part="liquid"))
        out.append(_path("M %s,%s L %s,%s L %s,%s L %s,%s L %s,%s" % (cx - 13, vy, cx - 13, vy + 30, cx - 55, pan_y - 2,
                                                                  cx + 55, pan_y - 2, cx + 13, vy + 30)
                         + " L %s,%s" % (cx + 13, vy), stroke=_SVG_INK, w=3, data_part="flask"))
        for dx, dy in ((-26, 16), (-6, 20), (16, 15), (30, 19), (-14, 10)):
            out.append(_path("M %s,%s l 7,-4 l 6,3 l -2,6 l -8,1 Z" % (cx + dx - 6, pan_y - 2 - dy),
                             fill="#9A948C", stroke=_SVG_INK, w=1.5, data_part="chip"))
        for bx, by, r in ((cx - 18, vy + 92, 3), (cx + 6, vy + 86, 3.5), (cx + 24, vy + 96, 3),
                          (cx - 4, vy + 70, 3.5), (cx + 2, vy + 48, 3), (cx - 2, vy + 24, 3)):
            out.append(_circle(bx, by, r, fill=_SVG_CARD, stroke=_SVG_ACCENT_TEXT, w=1.8, data_part="bubble"))
        out.append(_b4_arrow(cx, vy - 6, cx, vy - 36, stroke=_SVG_ACCENT_TEXT, w=3, data_part="gas"))
        al = p.get("arrow_label") or ""
        words = al.split()
        half = max(1, len(words) // 2 + (len(words) % 2))
        lines = [" ".join(words[:half]), " ".join(words[half:])] if len(words) > 1 else [al]
        for i, ln in enumerate([x for x in lines if x]):
            out.append(_label(cx + 18, vy - 24 + i * 17, ln, size=14, fill=_SVG_ACCENT_TEXT, weight="700",
                              anchor="start", data_part="gas-label", data_key=al))
    else:
        bw = 42
        out.append(_path("M %s,%s L %s,%s Q %s,%s %s,%s L %s,%s Q %s,%s %s,%s L %s,%s"
                         % (cx - 13, vy + 4, cx - 13, vy + 30, cx - bw, vy + 40, cx - bw, vy + 58,
                            cx - bw, pan_y - 12, cx - bw, pan_y - 2, cx - bw + 10, pan_y - 2,
                            cx + bw - 10, pan_y - 2) + " Q %s,%s %s,%s L %s,%s Q %s,%s %s,%s L %s,%s Z"
                         % (cx + bw, pan_y - 2, cx + bw, pan_y - 12, cx + bw, vy + 58, cx + bw, vy + 40,
                            cx + 13, vy + 30, cx + 13, vy + 4),
                         fill=_SVG_CARD, stroke=_SVG_INK, w=3, data_part="bottle"))
        out.append(_path("M %s,%s L %s,%s Q %s,%s %s,%s L %s,%s Q %s,%s %s,%s Z"
                         % (cx - bw + 1.5, vy + 74, cx - bw + 1.5, pan_y - 12, cx - bw + 1.5, pan_y - 3.5,
                            cx - bw + 10, pan_y - 3.5, cx + bw - 10, pan_y - 3.5, cx + bw - 1.5, pan_y - 3.5,
                            cx + bw - 1.5, pan_y - 12) + " L %s,%s Z" % (cx + bw - 1.5, vy + 74),
                         fill=_B4_BLUE_TINT, data_part="liquid"))
        out.append(_line(cx - bw + 1.5, vy + 74, cx + bw - 1.5, vy + 74, stroke=_B4_BLUE, w=2, data_part="liquid"))
        out.append(_rect(cx - 17, vy - 10, 34, 14, rx=3, fill=_SVG_BAND, stroke=_SVG_INK, w=2.5, data_part="cap"))
        for dx, dy in ((-24, 12), (-4, 16), (16, 11), (28, 15)):
            out.append(_path("M %s,%s l 7,-4 l 6,3 l -2,6 l -8,1 Z" % (cx + dx - 6, pan_y - 4 - dy),
                             fill="#9A948C", stroke=_SVG_INK, w=1.5, data_part="chip"))
        for bx, by, r in ((cx - 22, vy + 86, 3), (cx + 4, vy + 84, 3.5), (cx + 26, vy + 90, 3),
                          (cx - 12, vy + 64, 3.5), (cx + 14, vy + 58, 3), (cx - 6, vy + 46, 3),
                          (cx + 8, vy + 36, 3), (cx - 3, vy + 20, 3)):
            out.append(_circle(bx, by, r, fill=_SVG_CARD, stroke=_SVG_ACCENT_TEXT, w=1.8, data_part="bubble"))
        note = p.get("note")
        if note:
            words = note.split()
            lines = [" ".join(words[:2]), " ".join(words[2:])] if len(words) > 2 else [note]
            for i, ln in enumerate(lines):
                out.append(_label(cx + bw + 12, vy + 36 + i * 17, ln, size=14, fill=_SVG_ACCENT_TEXT,
                                  weight="700", anchor="start", data_part="gas-label", data_key=note))
    # the balance: pan, body, display
    out.append(_rect(cx - 70, pan_y, 140, 6, rx=3, fill=_SVG_INK, data_part="pan"))
    out.append(_rect(cx - 90, pan_y + 6, 180, 30, rx=6, fill=_SVG_BAND, stroke=_SVG_INK, w=3, data_part="balance"))
    out.append(_rect(cx + 40, pan_y + 13, 40, 16, rx=3, fill=_SVG_CARD, stroke=_SVG_INK, w=2, data_part="display"))
    # the readings
    ry = pan_y + 48
    changed = p["before"] != p["after"]
    out.append(_rect(cx - 100, ry, 200, 54, rx=8, fill=_SVG_CARD, stroke=_SVG_INK, w=2, data_part="readout"))
    for i, (k, v) in enumerate((("Before", p["before"]), ("After", p["after"]))):
        yy = ry + 21 + i * 22
        out.append(_label(cx - 88, yy, k, size=14, weight="600", anchor="start", data_part="reading-name", data_key=k))
        out.append(_label(cx + 88, yy, v, size=15, weight="700", anchor="end",
                          fill=_SVG_ACCENT_TEXT if (changed and k == "After") else _SVG_INK,
                          data_part="reading", data_key=k))
    return "".join(out), ry + 54


def _open_sealed_flask(fig):
    panels = (fig.get("data") or {}).get("panels") or []
    if len(panels) != 2:
        raise ValueError("figure %r: open-sealed-flask needs two panels" % fig.get("id"))
    W = 326
    out = []
    y = 4
    for i, p in enumerate(panels):
        svg, bottom = _osf_panel(p, y)
        out.append(svg)
        y = bottom + 14
        if i == 0:
            out.append(_line(8, y, 318, y, stroke=_SVG_RULE, w=1.5, data_part="divider"))
            y += 10
    H = y - 4
    return (_svg_open(fig, W, H) + '<g stroke-linecap="round" stroke-linejoin="round">'
            + "".join(out) + '</g></svg>')


ART = {
    'particle-boxes': _particle_boxes,
    'open-sealed-flask': _open_sealed_flask,
}
