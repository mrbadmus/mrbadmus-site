"""ks3_art.c2 — C2's drawers, instruments and registrations.

ONE UNIT, ONE FILE. Nothing here is read by any other unit; nothing
here may be added to any other unit's module. Moved verbatim out of
``build_ks3.py`` by MRB-271 so that two content lanes can build two
units at once without editing the same file.
"""

import json
import re
from ks3_art.kit import (
    _canvas_frame,
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
