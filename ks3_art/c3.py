"""ks3_art.c3 — C3's drawer, instruments and registrations.

ONE UNIT, ONE FILE. Nothing here is read by any other unit; nothing here may
be added to any other unit's module. C3 is *Mixtures and separation*: seven
lessons, NINE instrument families and one drawn figure, all DOM, no canvas
anywhere in the unit.

═══════════════════════════════════════════════════════════════════════════
WHAT THIS FILE IS RESPONSIBLE FOR, AND WHAT IT IS NOT
═══════════════════════════════════════════════════════════════════════════

MARKUP ONLY. Everything an instrument has to COMPUTE at run time is the JS's
job; this file emits the data it needs (as ``data-`` attributes, or as one
compact JSON payload per instrument) and the RESTING DOM — the state the page
is in before a line of JavaScript has run, which is also the state a crawler
and a no-JS reader see. A resting render that disagrees with the payload is a
wrong number in the bytes, not a flicker.

Two conventions run through every renderer below and both are load-bearing:

  · EMIT-BOTH-SHOW-ONE, wherever a panel has a small closed set of states.
    Every state's text is in the document and one is shown. Nothing is ever
    assembled out of an attribute, so ``<em>``, ``<strong>`` and an ampersand
    survive exactly as the author wrote them, and no sentence is duplicated
    between Python and JS where the two could drift.
  · A JSON ``data-cfg`` ONLY for what genuinely has to be recomputed — a
    number, a colour, a geometry. Never for a sentence.

═══════════════════════════════════════════════════════════════════════════
THE HOOKS ARE AN INTERFACE
═══════════════════════════════════════════════════════════════════════════

Every ``data-`` attribute emitted below is named systematically off the
family's short name (psort / dlab / seq / cryst / still / chroma / mpb /
mchoice / critiq) and is the contract ``shared/ks3.js`` binds against.
Renaming one here without renaming it there is a silent dead instrument, so
they are documented in each renderer's docstring as well as in the report.

⚠️ ``data-critiq``, NOT ``data-critique``. ``wireCritique`` already claims
``[data-critique]`` for a biology family; the two are different instruments
and a shared selector would wire this one to that one's handler.

═══════════════════════════════════════════════════════════════════════════
THE RULES THAT BIND ALL NINE
═══════════════════════════════════════════════════════════════════════════

  · Every C3 instrument sits in a LIGHT ``ks3-block``. There is no ink-dark
    practical block anywhere in the unit.
  · ONLY THE LADDER MARKS. Nothing green and nothing red reaches any control
    in any of these nine. A verdict panel says in words what happened; the
    chosen option keeps the ordinary chosen treatment and the unchosen ones
    dim. No ``data-correct`` on any activity option, ever.
  · All nine tick a rail stop, so all nine carry ``data-stage-done="0"``.
    NOTHING IS TICKED ON LOAD.
  · Author text reaches the page through ``e()`` / ``t()`` / ``rich()``.
    ``e()`` for attribute values — it is the only one safe there, because
    ``t()`` can emit an SVG mark carrying double quotes — ``rich()`` for
    prose, ``t()`` for labels.
"""

import json

from ks3_art.kit import (
    _SVG_INK,
    _SVG_INK_BODY,
    _SVG_INSET,
    _SVG_RULE_STRONG,
    _circle,
    _label,
    _line,
    _mono,
    _rect,
    _svg_open,
    e,
    option_letter,
    rich,
    t,
)


def _cfg(obj):
    """One JSON payload, deterministically ordered, safe in an attribute.

    ``sort_keys`` so two builds of the same payload are byte-identical, and
    ``ensure_ascii=False`` so a degree sign stays a degree sign rather than
    becoming six characters of escape inside an attribute nobody reads.
    """
    return e(json.dumps(obj, separators=(",", ":"), sort_keys=True,
                        ensure_ascii=False))


def _seg(cls, pressed, label, **attrs):
    """One segmented-control button.

    ``.ks3-seg-btn`` is the system's ONE segmented control (shared/ks3.css,
    the Drift-4 ruling). Every dial in C3 is that control with a family class
    beside it for layout, so a tenth instrument inherits a measured box rather
    than growing a tenth copy of the same border and padding.

    ⚠️ R2 — the pressed state carries ``aria-pressed``, a WORD, not colour
    alone.
    ⚠️ R3 — there is no ``data-correct`` parameter and there must never be one.
    """
    extra = "".join(' %s="%s"' % (k.replace("_", "-"), e(v))
                    for k, v in sorted(attrs.items()) if v is not None)
    return ('<button type="button" class="ks3-seg-btn %s"%s '
            'aria-pressed="%s">%s</button>'
            % (e(cls), extra, "true" if pressed else "false", t(label)))


def _lettered(options, hook, pressed=None):
    """A lettered A/B/C commit list, inside an instrument.

    The same markup ``r_activity_options`` emits — ``.ks3-options`` /
    ``.ks3-option`` with the letter as the resting mark — because Design draws
    the SAME control for a prediction whether it stands alone in a block or
    sits inside a bench.

    ⚠️ It gets a hook of its own because the shell's ``wirePredictions``
    refuses to touch anything inside ``[data-instrument]`` (build_ks3.py's
    marker, and ks3.js line 372). An instrument owns every option inside it,
    which means it also has to wire them.
    """
    return ('<ul class="ks3-options" role="list" %s>%s</ul>'
            % (hook,
               "".join(
                   '<li><button type="button" class="ks3-option" data-i="%d" '
                   'aria-pressed="%s"><span class="ks3-opt-mark" '
                   'aria-hidden="true">%s</span>'
                   '<span class="ks3-opt-label">%s</span></button></li>'
                   % (i, "true" if pressed == i else "false",
                      option_letter(i), t(o))
                   for i, o in enumerate(options))))


# ═══ c3-01 · purity-sorter ═══════════════════════════════════════════════

def r_purity_sorter(a, act_id):
    """⊕ c3-01 `#s-sorter` — eight samples, one question, eight commitments.

    ⚖️ **THE REPEATED APPLICATION OF ONE QUESTION IS THE TEACHING**, which is
    why this is a grid of INDEPENDENT commitments and deliberately not C2's
    `test-budget-bench`. NOTES §2 says so in as many words: the lesson is not
    the economics of evidence, it is asking "one substance, or more than one?"
    eight times and finding that looking settles none of them.

    ⚖️ ONE COMMITMENT PER CARD AND IT IS FINAL. Both buttons disable on
    commit — not to punish a change of mind, but because the reveal is already
    on screen by then and a second press would be a student choosing an answer
    they can see. Design's own click guard does the same (page line 404): the
    handler re-checks and returns null.

    ⚠️ `ingredients` IS HIDDEN UNTIL THE CARD IS DECIDED and that is the whole
    exercise. "Water, three sugars, citric acid, pulp, vitamin C, and more" is
    the answer to the question being asked; printing it beside the question
    turns eight commitments into eight readings.

    ⚠️ THE PARTICLE STRIP CARRIES ITS OWN `aria-label`, naming what THAT
    sample's diagram shows. Eight different sentences, authored per sample as
    `diagramLabel`, because the strip is the only route to that information
    for a student who cannot see it — and "a particle diagram" repeated eight
    times would be a label that passes a grep and tells nobody anything.

    ⚠️ Each dot's inline `style` is AUTHORED DATA, passed through whole. The
    author composed the full declaration (size, colour, radius, hairline) per
    dot; splitting it into a class here would mean this file and the payload
    both deciding what a particle looks like.

    HOOKS: `data-psort` (wrapper, with `data-total`) · `data-psort-card`
    (per card, valued with the sample id) · `data-psort-opt` (a verdict
    button, valued 0/1 to index `options`) · `data-psort-ingredients` ·
    `data-psort-reveal` · `data-psort-close`. The head tally is the SHELL's
    `[data-count]`, rendered by `_head_counter` from `head_counter`.
    """
    samples = a.get("samples") or []
    options = a.get("options") or []
    if not samples:
        raise ValueError("purity-sorter %r declares no samples[]." % act_id)
    if len(options) != 2:
        raise ValueError(
            "purity-sorter %r offers %d option(s); it is a radio group of two "
            "— pure or mixture — and the whole unit is built on there being "
            "exactly those two answers." % (act_id, len(options)))
    for s in samples:
        if s.get("dots") and not s.get("diagramLabel"):
            raise ValueError(
                "purity-sorter %r sample %r draws a particle strip with no "
                "`diagramLabel`. The strip is the only route to what the "
                "diagram SHOWS for a student who cannot see it, and a strip "
                "of unlabelled circles is decoration."
                % (act_id, s.get("id")))
        for key in ("verdict", "why"):
            if not s.get(key):
                raise ValueError(
                    "purity-sorter %r sample %r has no %r. Every card opens a "
                    "reveal the instant it is decided; a card with nothing to "
                    "reveal is a commitment that goes nowhere."
                    % (act_id, s.get("id"), key))

    label_tpl = a.get("sample_label") or "Sample {n}"
    cards = []
    for i, s in enumerate(samples):
        strip = ""
        if s.get("dots"):
            strip = ('<span class="ks3-psort-dots" role="img" aria-label="%s">'
                     '%s</span>'
                     % (e(s["diagramLabel"]),
                        "".join('<span class="ks3-psort-dot" style="%s">'
                                '</span>' % e(d.get("style", ""))
                                for d in s["dots"])))
        btns = "".join(
            _seg("ks3-psort-opt", False, opt, data_psort_opt=str(j))
            for j, opt in enumerate(options))
        ingredients = (
            '<p class="ks3-psort-ingredients" hidden '
            'data-psort-ingredients>%s</p>' % rich(s["ingredients"])
            if s.get("ingredients") else "")
        cards.append(
            '<div class="ks3-psort-card" data-psort-card="%s">'
            '<p class="ks3-psort-num">%s</p>'
            '<p class="ks3-psort-name">%s</p>'
            '<p class="ks3-psort-look">%s</p>'
            '%s%s'
            '<div class="ks3-psort-opts">%s</div>'
            '<div class="ks3-psort-reveal" hidden data-psort-reveal>'
            '<p class="ks3-psort-verdict">%s</p>'
            '<p class="ks3-psort-why">%s</p></div></div>'
            % (e(s.get("id", "")),
               t(label_tpl.replace("{n}", str(i + 1))),
               t(s.get("name", "")), rich(s.get("look", "")),
               strip, ingredients, btns,
               t(s["verdict"]), rich(s["why"])))

    close = ('<div class="ks3-psort-close" hidden data-psort-close>'
             '<p>%s</p></div>' % rich(a["close"])) if a.get("close") else ""
    return ('<div class="ks3-psort" data-psort data-total="%d">'
            '<div class="ks3-psort-grid">%s</div>%s</div>'
            % (len(samples), "".join(cards), close))


# ═══ c3-02 · dissolve-lab ════════════════════════════════════════════════

def _dlab_seconds(base, factor, stir, powder, timing):
    """The clock. THE SAME ARITHMETIC IN PYTHON AND IN JS, and no other.

    ⚖️ Stirring and grinding divide the TIME and touch nothing else. That is
    not a styling detail — it is lesson c3-02, entire. `grams` is not a
    parameter of this function and cannot become one.
    """
    secs = float(base) * float(factor)
    if stir:
        secs /= float(timing.get("stirred_divisor") or 1)
    if powder:
        secs /= float(timing.get("powder_divisor") or 1)
    return int(round(secs))


def _dlab_mix(water_n, water_colour, water_size, sol_n, sol_colour, sol_size):
    """Water dots with solute dots threaded evenly through them.

    Design's own interleave (page line 508): every `n`th water particle is
    followed by a solute particle, so the picture reads as *spread evenly
    among them* rather than as a stripe of one colour beside a stripe of the
    other. Reproduced here because the RESTING render has to be the same
    picture the runtime draws, not an approximation of it.
    """
    out = []
    every = max(2, int(round(water_n / float(sol_n)))) if sol_n else 10 ** 9
    wi = si = 0
    while wi < water_n or si < sol_n:
        k = 0
        while k < every and wi < water_n:
            out.append((water_colour, water_size))
            wi += 1
            k += 1
        if si < sol_n:
            out.append((sol_colour, sol_size))
            si += 1
    return out


def _dlab_dots(pairs, cls):
    """Generated particles: the class carries the shape, the style the state.

    Unlike `purity-sorter`, whose dot styles are authored strings, these are
    composed here — so only what VARIES between two states (the diameter and
    the colour) is inline, and the hairline, the radius and the flex behaviour
    belong to `.ks3-dlab-dot` in the stylesheet.
    """
    return "".join(
        '<span class="%s" style="width:%dpx;height:%dpx;background:%s">'
        '</span>' % (e(cls), size, size, e(colour))
        for colour, size in pairs)


def _dlab_num(v):
    """`36.4`, `190`, `0.001` — the authored number, not a re-rounded one.

    An integer-valued float prints without its `.0`, which is what Design's
    page does (JavaScript numbers have no trailing zero) and what the author
    wrote: 190 g, not 190.0 g.
    """
    if isinstance(v, float) and v == int(v):
        return str(int(v))
    return str(v)


def _dlab_alt(beaker, sol, soluble):
    """The beaker's `aria-label`. Composed the same way in Python and in JS."""
    key = "alt_soluble" if soluble else "alt_insoluble"
    return (beaker.get(key, "")
            .replace("{solute}", (sol.get("name") or "").lower()))


def _dlab_verdict(verdict, sol, soluble, stir, powder):
    """The verdict sentence. Composed identically in both languages.

    ⚠️ The tail is chosen by whether the student has TOUCHED the two rate
    dials, and both tails say the same thing about the grams — that they did
    not move. That is deliberate: the sentence has to be true and useful in
    the state where nothing has been stirred as well as in the state where
    everything has.
    """
    if not soluble:
        return (verdict.get("insoluble", "")
                .replace("{Solute}", sol.get("name", ""))
                .replace("{note}", sol.get("note", "")))
    tail = verdict.get("tail_worked" if (stir or powder) else "tail_still", "")
    return (verdict.get("soluble", "")
            .replace("{Solute}", sol.get("name", ""))
            .replace("{note}", sol.get("note", ""))
            .replace("{tail}", tail))


def r_dissolve_lab(a, act_id):
    """⊕ c3-02 `#s-lab` — four dials, forty-eight reachable states, one point.

    ⚖️ **THE RATE/AMOUNT SPLIT IS THE WHOLE LESSON AND IT IS LOAD-BEARING IN
    CODE.** `grams` comes from `solutes[].grams[temp]` and from nowhere else.
    `stir` and `powder` divide the TIME. If stirring ever moves the grams the
    lesson teaches the misconception it was built to confront (`MIX-04`,
    "stirring harder makes more dissolve") — so the split is enforced three
    times over: the config below carries `grams` keyed ONLY by temperature,
    `_dlab_seconds` cannot see the grams at all, and the two readouts are two
    separate nodes with two separate hooks.

    ⚖️ SALT IS ON THE BENCH BECAUSE ITS SOLUBILITY BARELY MOVES — 35.8 g cold
    against 38.1 g hot. A student who has only ever seen sugar leaves
    believing "hot water dissolves more" as a rule; the salt column is the
    counter-example that makes it a question about the solute, and the summary
    says so out loud.

    ⚠️ THE BENCH IS LOCKED BY AN ACTIVITY THAT IS NOT PART OF IT.
    `locked_by: "gate-which-dial"` names the `predict` block ABOVE this one on
    the page, and Design wraps the entire `<section>` in that gate
    (`<sc-if value="{{ labOpen }}">`, page line 132) rather than greying the
    controls. This renderer cannot hide the shell it is rendered into, so it
    emits the instrument `hidden` and names the gate; `wireDissolveLab` hides
    the whole `[data-activity]` section and unhides it when the named block is
    answered. Gating by ABSENCE, exactly as `r_bench_gate` does — but the gate
    is a sibling block here, not a panel inside the bench.

    ⚠️ `demo_mode` OPENS THE BENCH WITHOUT THE GATE and is authored `false`.
    It is the front-of-class dial (NOTES §6) and it must never default true in
    a student build, so it is emitted as the payload's value and never as an
    absence that a truthy default could fill.

    ⚠️ An insoluble solute is a REACHABLE, HONEST state, not an error: sand
    reads `none` / `never` / `cloudy`, draws undissolved solid on the bottom,
    and gets its own verdict template. Two of the four solutes are insoluble,
    so half the solute dial lands there.

    HOOKS: `data-dlab` (wrapper: `data-dlab-lock`, `data-dlab-demo`,
    `data-dlab-done-at`, `data-cfg`) · `data-dlab-group` (a dial's row) ·
    `data-dlab-opt` with `data-dlab-for` + `data-dlab-val` (a dial button) ·
    `data-dlab-out` / `data-dlab-outnote` (a readout's value and its note) ·
    `data-dlab-beaker` (the `role="img"` wrapper whose `aria-label` is
    recomposed) · `data-dlab-dots` · `data-dlab-bottom` ·
    `data-dlab-bottomdots` · `data-dlab-bottomnote` · `data-dlab-verdict` ·
    `data-dlab-summary`.
    """
    solutes = a.get("solutes") or []
    temps = a.get("temps") or []
    dials = a.get("dials") or []
    readouts = a.get("readouts") or []
    beaker = a.get("beaker") or {}
    timing = a.get("timing") or {}
    verdict = a.get("verdict") or {}
    start = a.get("start_state") or {}
    if not (solutes and temps and dials and readouts):
        raise ValueError(
            "dissolve-lab %r needs solutes[], temps[], dials[] and readouts[]."
            % act_id)
    temp_ids = [tp["id"] for tp in temps]
    for s in solutes:
        gaps = [k for k in temp_ids if k not in (s.get("grams") or {})]
        if gaps:
            raise ValueError(
                "dissolve-lab %r solute %r has no `grams` for temperature(s) "
                "%s. The amount comes from the solute and the temperature and "
                "from nothing else on this bench, so every reachable pair "
                "must have one." % (act_id, s.get("id"), gaps))
    factors = timing.get("temperature") or {}
    absent = [k for k in temp_ids if k not in factors]
    if absent:
        raise ValueError(
            "dissolve-lab %r declares no timing factor for temperature(s) %s. "
            "A dial that is drawn must be modelled." % (act_id, absent))

    by_id = dict((s["id"], s) for s in solutes)
    s0 = by_id.get(start.get("solute") or solutes[0]["id"], solutes[0])
    t0 = start.get("temp") or temp_ids[0]
    stir0 = bool(start.get("stir"))
    pow0 = bool(start.get("powder"))
    show_g = a.get("show_solubility_numbers") is not False

    # ── the dials ────────────────────────────────────────────────────────
    # `solute` and `temp` take their options from the payload's own lists;
    # `stir` and `powder` author theirs inline as two-value toggles. One loop,
    # because they are one control in Design's page and differ only in where
    # their options come from.
    chosen = {"solute": s0["id"], "temp": t0,
              "stir": "1" if stir0 else "0", "powder": "1" if pow0 else "0"}
    sources = {
        "solute": [(x["id"], x.get("name", "")) for x in solutes],
        "temp": [(x["id"], x.get("label", "")) for x in temps],
    }
    dial_html = []
    for d in dials:
        did = d.get("id")
        if did in sources:
            opts = sources[did]
        else:
            opts = [("1" if o.get("value") else "0", o.get("label", ""))
                    for o in (d.get("options") or [])]
            if not opts:
                raise ValueError(
                    "dissolve-lab %r dial %r offers nothing to press. A dial "
                    "that is drawn must be modelled." % (act_id, did))
        dial_html.append(
            '<div class="ks3-dlab-dial" data-dlab-group="%s">'
            '<p class="ks3-dlab-diallabel">%s</p>'
            '<div class="ks3-dlab-btns">%s</div></div>'
            % (e(did), t(d.get("label", "")),
               "".join(_seg("ks3-dlab-opt", chosen.get(did) == str(val), lab,
                            data_dlab_for=str(did), data_dlab_val=str(val))
                       for val, lab in opts)))

    # ── the resting readouts ─────────────────────────────────────────────
    # Computed here from the opening state so the bytes are right before any
    # JS runs. Every one of these three is recomputed by `wireDissolveLab`
    # from `data-cfg`; none of them is ever assembled from a sentence.
    soluble = bool(s0.get("soluble"))
    grams = (s0.get("grams") or {}).get(t0)
    secs = _dlab_seconds(s0.get("base_seconds") or 0, factors[t0],
                         stir0, pow0, timing)
    rest = {}
    for r in readouts:
        rid = r.get("id")
        if not soluble:
            value = r.get("value_insoluble") or ""
            note = r.get("note_insoluble")
            if note is None:
                note = s0.get("note") or ""
        elif rid == "amount":
            value = (r.get("value_format", "{grams} g")
                     .replace("{grams}", _dlab_num(grams))
                     if show_g else (r.get("value_hidden") or ""))
            note = r.get("note") or ""
        elif rid == "time":
            value = r.get("value_format", "{seconds} s").replace(
                "{seconds}", str(secs))
            note = r.get("note") or ""
        else:
            value = r.get("value") or ""
            note = r.get("note") or ""
        rest[rid] = (value, note)

    readout_html = "".join(
        '<div class="ks3-dlab-readout">'
        '<p class="ks3-dlab-rlabel">%s</p>'
        '<p class="ks3-dlab-rvalue" data-dlab-out="%s">%s</p>'
        '<p class="ks3-dlab-rnote" data-dlab-outnote="%s">%s</p></div>'
        % (t(r.get("label", "")), e(r.get("id", "")),
           t(rest[r.get("id")][0]), e(r.get("id", "")),
           rich(rest[r.get("id")][1]))
        for r in readouts)

    # ── the beaker ───────────────────────────────────────────────────────
    diss = (beaker.get("dissolved_dots") or {}).get(s0["id"], 0) if soluble \
        else 0
    mixed = _dlab_mix(int(beaker.get("water_dots") or 0),
                      beaker.get("water_colour") or "",
                      int(beaker.get("water_dot_size") or 11),
                      int(diss), s0.get("colour") or "",
                      int(beaker.get("solute_dot_size") or 9))
    bottom_n = 0 if soluble else int(beaker.get("undissolved_dots") or 0)
    bottom = [(s0.get("colour") or "",
               int(beaker.get("undissolved_dot_size") or 13))] * bottom_n
    alt0 = _dlab_alt(beaker, s0, soluble)
    note0 = (beaker.get("bottom_note") or "").replace(
        "{Solute}", s0.get("name", ""))

    cfg = {
        "solutes": [{"id": s["id"], "name": s.get("name", ""),
                     "colour": s.get("colour", ""),
                     "soluble": bool(s.get("soluble")),
                     "grams": s.get("grams") or {},
                     "base": s.get("base_seconds") or 0,
                     "note": s.get("note", "")} for s in solutes],
        "temps": temp_ids,
        "timing": timing,
        "readouts": readouts,
        "beaker": beaker,
        "verdict": verdict,
        "show_grams": show_g,
        "start": {"solute": s0["id"], "temp": t0,
                  "stir": stir0, "powder": pow0,
                  "seen": list(start.get("seen") or [])},
    }
    summary = a.get("summary") or {}
    return ('<div class="ks3-dlab" data-dlab hidden data-dlab-lock="%s" '
            'data-dlab-demo="%s" data-dlab-done-at="%d" data-cfg="%s">'
            '<div class="ks3-dlab-dials">%s</div>'
            '<div class="ks3-dlab-readouts">%s</div>'
            '<div class="ks3-dlab-beaker" role="img" aria-label="%s" '
            'data-dlab-beaker>'
            '<p class="ks3-dlab-caption">%s</p>'
            '<div class="ks3-dlab-jar">'
            '<div class="ks3-dlab-dots" data-dlab-dots>%s</div>'
            '<div class="ks3-dlab-bottom"%s data-dlab-bottom>'
            '<div class="ks3-dlab-bottomdots" data-dlab-bottomdots>%s</div>'
            '<p class="ks3-dlab-bottomnote" data-dlab-bottomnote>%s</p>'
            '</div></div></div>'
            '<div class="ks3-dlab-verdict"><p data-dlab-verdict>%s</p></div>'
            '<div class="ks3-dlab-summary" hidden data-dlab-summary>'
            '<p>%s</p></div></div>'
            % (e(a.get("locked_by") or ""),
               "1" if a.get("demo_mode") else "0",
               int(summary.get("after_temperatures_seen") or len(temp_ids)),
               _cfg(cfg),
               "".join(dial_html), readout_html,
               e(alt0), t(beaker.get("caption", "")),
               _dlab_dots(mixed, "ks3-dlab-dot"),
               "" if bottom else " hidden",
               _dlab_dots(bottom, "ks3-dlab-dot ks3-dlab-dot-solid"),
               t(note0),
               rich(_dlab_verdict(verdict, s0, soluble, stir0, pow0)),
               rich(summary.get("text", ""))))


# ═══ c3-03 · sequence-rebuild (two phases, one family) ═══════════════════

_SEQ_PHASES = ("watch", "rebuild")


def _seq_watch(a, act_id, steps):
    """The revealed stepper, with the prediction gate before `gate.after`."""
    gate = a.get("gate") or {}
    gate_at = -1
    if gate and a.get("require_prediction") is not False:
        ids = [s.get("id") for s in steps]
        if gate.get("after") not in ids:
            raise ValueError(
                "sequence-rebuild %r gates before step %r, which is not one "
                "of %s. A gate attached to no step never fires and the "
                "prediction is silently skipped."
                % (act_id, gate.get("after"), ids))
        gate_at = ids.index(gate["after"])

    label_tpl = a.get("reveal_label") or "Show step {n}"
    items = []
    for i, s in enumerate(steps):
        label = label_tpl.replace("{n}", str(i + 1))
        # The FIRST step is the only one whose button is open at rest: the
        # stepper opens on nothing revealed, and the next-step button walks
        # down the list from there.
        gate_html = ""
        if i == gate_at:
            gate_html = (
                '<div class="ks3-seq-gate" hidden data-seq-gate>'
                '<p class="ks3-commit">%s</p>%s</div>'
                % (t(gate.get("prompt", "")),
                   _lettered(gate.get("options") or [], "data-seq-gate-opts")))
        items.append(
            '<li class="ks3-seq-step" data-seq-step="%s" data-seq-i="%d">'
            '<span class="ks3-seq-num" aria-hidden="true">%d</span>'
            '<div class="ks3-seq-stepbody">'
            '<p class="ks3-seq-title">%s</p>'
            '<div class="ks3-seq-body" hidden data-seq-body>'
            '<p class="ks3-seq-detail">%s</p>'
            '<p class="ks3-seq-why">%s</p></div>'
            '<button type="button" class="ks3-reveal-btn ks3-seq-open"%s '
            'data-seq-open="%d" data-seq-label="%s">%s</button>'
            '%s</div></li>'
            % (e(s.get("id", "")), i, i + 1,
               rich(s.get("title", "")), rich(s.get("detail", "")),
               rich(s.get("why", "")),
               "" if i == 0 else " hidden", i, e(label), t(label),
               gate_html))

    close = ('<div class="ks3-seq-close" hidden data-seq-close><p>%s</p></div>'
             % rich(a["summary"])) if a.get("summary") else ""
    return ('<div class="ks3-seq ks3-seq-watch" data-seq data-phase="watch" '
            'data-total="%d" data-seq-gate-at="%d">'
            '<ol class="ks3-seq-steps" role="list">%s</ol>%s</div>'
            % (len(steps), gate_at, "".join(items), close))


def _seq_rebuild(a, act_id, steps):
    """The shuffled bank, the growing order, and the consequence report."""
    order = a.get("shuffled") or list(range(len(steps)))
    if sorted(order) != list(range(len(steps))):
        raise ValueError(
            "sequence-rebuild %r shuffles %s over %d steps. The bank is a "
            "permutation of the steps — a repeated or missing index would put "
            "one step on the bench twice and another not at all."
            % (act_id, order, len(steps)))
    report = a.get("report") or {}
    for key in ("right_title", "right_text", "wrong_title", "wrong_text"):
        if not report.get(key):
            raise ValueError(
                "sequence-rebuild %r report has no %r. Both branches have to "
                "say something: an order that came out right and an order "
                "that did not are two different things that happened on the "
                "bench." % (act_id, key))

    bank = "".join(
        _seg("ks3-seq-chip", False, steps[i].get("short", ""),
             data_seq_chip=str(i), data_seq_short=steps[i].get("short", ""))
        for i in order)
    # Emitted in AUTHORED order and hidden. The runtime MOVES these nodes, so
    # the titles never round-trip through an attribute.
    slots = "".join(
        '<li class="ks3-seq-slot" hidden data-seq-slot="%d">%s</li>'
        % (i, rich(s.get("title", ""))) for i, s in enumerate(steps))

    tpl = {"wrong_title": report["wrong_title"],
           "wrong_text": report["wrong_text"],
           "when": report.get("when") or {},
           "shorts": [s.get("short", "") for s in steps],
           "too_soon": [s.get("tooSoon", "") for s in steps]}
    return ('<div class="ks3-seq ks3-seq-rebuild" data-seq '
            'data-phase="rebuild" data-total="%d" data-seq-report="%s">'
            '<div class="ks3-seq-bank">%s</div>'
            '<ol class="ks3-seq-order" hidden data-seq-order role="list">%s'
            '</ol>'
            '<div class="ks3-seq-foot">'
            '<button type="button" class="ks3-retry ks3-seq-clear" '
            'data-seq-clear>%s</button></div>'
            '<div class="ks3-seq-report" hidden data-seq-report-panel>'
            '<div data-seq-right hidden>'
            '<p class="ks3-seq-reporttitle">%s</p>'
            '<p class="ks3-seq-reporttext">%s</p></div>'
            '<div data-seq-wrong hidden>'
            '<p class="ks3-seq-reporttitle" data-seq-wrong-title></p>'
            '<p class="ks3-seq-reporttext" data-seq-wrong-text></p>'
            '</div></div></div>'
            % (len(steps), _cfg(tpl), bank, slots,
               t(a.get("clear_label") or ""),
               t(report["right_title"]), rich(report["right_text"])))


def r_sequence_rebuild(a, act_id):
    """⊕ c3-03 `#s-steps` (watch) and `#s-build` (rebuild).

    **ONE FAMILY, TWO PHASES, ONE RENDERER, ONE REGISTRATION.** `phase`
    selects the branch. Minting a second family for the rebuild would give the
    unit two names for one instrument and two places for the five steps to
    drift apart — and they are literally the same five records, authored once
    per activity and identical.

    `phase: "watch"` — five steps revealed one at a time. Each closed step
    shows only its title; opening it shows the detail and the why. A
    PREDICTION GATE fires before the step named by `gate.after` and blocks it:
    the gate panel takes the *next-step* slot, so a student cannot walk past
    the question by scrolling. Ticks when all five are open.

    `phase: "rebuild"` — the same five steps as a bank in `shuffled` order,
    tapped into a sequence. A tapped chip disables. Ticks when all five are
    ordered.

    ⚖️ **WRONG ORDERS ARE ANSWERED WITH CONSEQUENCES, NEVER WITH MARKS.** The
    report names what happened *on the bench* using the offending step's own
    `tooSoon` string — "you poured before the paper and funnel were ready, so
    the sand went into the flask with the water". Nothing green, nothing red,
    no score, and the order that works is given in the same breath. R3 is not
    relaxed for a construct task.

    ⚠️ THE ORDERED LIST IS EMITTED, HIDDEN, IN AUTHORED ORDER — one `<li>` per
    step carrying that step's title as real markup. `wireSequenceRebuild`
    REORDERS THE NODES rather than writing text into an empty list, so the
    titles never make a round trip through an attribute and a future authored
    `<em>` survives it. `data-seq-slot` is the step index the node belongs to.

    HOOKS (watch): `data-seq` (wrapper: `data-phase`, `data-total`,
    `data-seq-gate-at`) · `data-seq-step` (an `<li>`, valued with the step id,
    plus `data-seq-i`) · `data-seq-body` (the detail+why, hidden) ·
    `data-seq-open` (the reveal button, valued with the index, with
    `data-seq-label` carrying that step's authored button text) ·
    `data-seq-gate` / `data-seq-gate-opts` · `data-seq-close`.

    HOOKS (rebuild): `data-seq` (wrapper: `data-phase`, `data-total`,
    `data-seq-report` carrying the wrong-branch TEMPLATE only) ·
    `data-seq-chip` (a bank button, valued with the step index, with
    `data-seq-short`) · `data-seq-order` (the `<ol>`) · `data-seq-slot` (a
    hidden `<li>`, valued with the step index) · `data-seq-clear` ·
    `data-seq-report-panel` · `data-seq-right` (the whole static right-order
    report, emitted as real DOM) · `data-seq-wrong` with
    `data-seq-wrong-title` / `data-seq-wrong-text` (the two nodes the template
    composes into).
    """
    phase = a.get("phase")
    if phase not in _SEQ_PHASES:
        raise ValueError(
            "sequence-rebuild %r declares phase %r; the two drawn phases are "
            "%s. The phase selects the branch — a third name would be a "
            "second instrument wearing this one's registration."
            % (act_id, phase, " and ".join(_SEQ_PHASES)))
    steps = a.get("steps") or []
    if len(steps) < 2:
        raise ValueError(
            "sequence-rebuild %r declares %d step(s); a sequence needs at "
            "least two." % (act_id, len(steps)))
    for s in steps:
        if not s.get("tooSoon"):
            raise ValueError(
                "sequence-rebuild %r step %r has no `tooSoon`. That string IS "
                "the consequence a wrong order is answered with, and without "
                "it the only thing left to say is that the student was wrong."
                % (act_id, s.get("id")))

    if phase == "watch":
        return _seq_watch(a, act_id, steps)
    return _seq_rebuild(a, act_id, steps)


# ═══ c3-04 · crystal-bench and method-choice ═════════════════════════════

def r_crystal_bench(a, act_id):
    """⊕ c3-04 `#s-bench` — three solutes × three methods, and one yield.

    ⚖️ **`recovered_mass` IS ONE AUTHORED VALUE, IDENTICAL IN ALL NINE STATES,
    AND THAT IS THE TEACHING.** The method changes the crystal and never the
    yield; `MIX-09` is "faster evaporation gives more product" and this bench
    exists to refuse it. So the mass tile is rendered ONCE, from the one
    authored string, and it is the only readout on this bench WITH NO DATA
    HOOK AT ALL. That is deliberate and it is the strongest guarantee
    available in markup: there is nothing for the runtime to write into, so
    nine masses cannot be computed even by accident.

    ⚠️ THE PREDICT GATE IS PER-RUN AND DOES NOT DISAPPEAR. This is NOT
    `r_bench_gate` — Design resets the prediction whenever a dial moves (page
    lines 513 and 517) and shows the Run button only once a prediction is in.
    A gate that vanished after the first answer would let the student run the
    remaining eight states without ever predicting again, which is the eight
    times it actually matters.

    ⚠️ The bench opens on `start_solute` / `start_method` with NOTHING RUN, so
    the resting DOM carries the dials in their opening position and no
    readouts. "Nothing has been run yet" is a reachable state with something
    true to say, and the something is the prediction question.

    HOOKS: `data-cryst` (wrapper: `data-total`, `data-cfg`) ·
    `data-cryst-group` (a dial's row) · `data-cryst-opt` with
    `data-cryst-for` + `data-cryst-val` · `data-cryst-gate-opts` ·
    `data-cryst-run` (the run button, hidden until a prediction is in, with
    `data-cryst-runlabel` carrying the template) · `data-cryst-panel` ·
    `data-cryst-out` (valued `time` or `quality`; THE MASS HAS NO HOOK) ·
    `data-cryst-dish` (the `role="img"` whose `aria-label` is recomposed) ·
    `data-cryst-crystals` · `data-cryst-verdict` · `data-cryst-hazard` ·
    `data-cryst-summary`.
    """
    solutes = a.get("solutes") or []
    methods = a.get("methods") or []
    if not solutes or not methods:
        raise ValueError(
            "crystal-bench %r needs both solutes[] and methods[]." % act_id)
    if not a.get("recovered_mass"):
        raise ValueError(
            "crystal-bench %r declares no `recovered_mass`. The mass that "
            "does not change is the lesson; without it the bench shows three "
            "different crystals and argues nothing." % act_id)
    labels = a.get("readout_labels") or {}
    for key in ("time", "quality", "mass"):
        if not labels.get(key):
            raise ValueError(
                "crystal-bench %r has no readout label for %r. A tile with a "
                "value and no name is a number nobody can read."
                % (act_id, key))

    dial_labels = a.get("dial_labels") or {}
    s0 = a.get("start_solute") or solutes[0]["id"]
    m0 = a.get("start_method") or methods[0]["id"]
    dials = "".join(
        '<div class="ks3-cryst-dial" data-cryst-group="%s">'
        '<p class="ks3-cryst-diallabel">%s</p>'
        '<div class="ks3-cryst-btns">%s</div></div>'
        % (e(key), t(dial_labels.get(key, "")),
           "".join(_seg("ks3-cryst-opt", x["id"] == chosen,
                        x.get("name") or x.get("label", ""),
                        data_cryst_for=key, data_cryst_val=x["id"])
                   for x in items))
        for key, items, chosen in (("solute", solutes, s0),
                                   ("method", methods, m0)))

    gate = a.get("gate") or {}
    run_tpl = a.get("run_label") or "Run it"
    tiles = (
        '<div class="ks3-cryst-tile"><p class="ks3-cryst-tilelabel">%s</p>'
        '<p class="ks3-cryst-value" data-cryst-out="time"></p></div>'
        '<div class="ks3-cryst-tile"><p class="ks3-cryst-tilelabel">%s</p>'
        '<p class="ks3-cryst-value" data-cryst-out="quality"></p></div>'
        # ⚠️ NO HOOK. One authored value, nine states, nothing to write into.
        '<div class="ks3-cryst-tile"><p class="ks3-cryst-tilelabel">%s</p>'
        '<p class="ks3-cryst-value ks3-cryst-mass">%s</p></div>'
        % (t(labels["time"]), t(labels["quality"]), t(labels["mass"]),
           t(a["recovered_mass"])))

    cfg = {
        "solutes": [{"id": s["id"], "name": s.get("name", ""),
                     "colour": s.get("colour", ""),
                     "shape": s.get("shape", ""),
                     "product": s.get("product", ""),
                     "hard": s.get("hard", ""), "slow": s.get("slow", "")}
                    for s in solutes],
        "methods": [{"id": m["id"], "label": m.get("label", ""),
                     "time": m.get("time", ""), "size": m.get("size", 0),
                     "count": m.get("count", 0),
                     "quality": m.get("quality", ""),
                     "note": m.get("note", ""), "hazard": m.get("hazard", "")}
                    for m in methods],
        "dish_alt": a.get("dish_alt") or {},
        "run_label": run_tpl,
        "show_timings": a.get("show_timings") is not False,
        "timings_hidden": a.get("timings_hidden") or "",
        "start": {"solute": s0, "method": m0},
    }
    m0rec = next(m for m in methods if m["id"] == m0)
    return ('<div class="ks3-cryst" data-cryst data-total="%d" data-cfg="%s">'
            '<div class="ks3-cryst-dials">%s</div>'
            '<div class="ks3-cryst-gate">'
            '<p class="ks3-commit">%s</p>%s'
            '<button type="button" class="ks3-reveal-btn ks3-cryst-run" '
            'hidden data-cryst-run data-cryst-runlabel="%s">%s</button></div>'
            '<div class="ks3-cryst-panel" hidden data-cryst-panel>'
            '<div class="ks3-cryst-tiles">%s</div>'
            '<div class="ks3-cryst-dish" role="img" aria-label="" '
            'data-cryst-dish>'
            '<p class="ks3-cryst-caption">%s</p>'
            '<div class="ks3-cryst-crystals" data-cryst-crystals></div></div>'
            '<div class="ks3-cryst-verdict">'
            '<p data-cryst-verdict></p><p data-cryst-hazard></p></div></div>'
            '<div class="ks3-cryst-summary" hidden data-cryst-summary>'
            '<p>%s</p></div></div>'
            % (len(methods), _cfg(cfg), dials,
               t(gate.get("prompt", "")),
               _lettered(gate.get("options") or [], "data-cryst-gate-opts"),
               e(run_tpl),
               t(run_tpl.replace("{method}",
                                 (m0rec.get("label") or "").lower())),
               tiles, t(a.get("dish_caption", "")),
               rich(a.get("summary", ""))))


def r_method_choice(a, act_id):
    """⊕ c3-04 `#s-jobs` — three real jobs, one method each.

    ⚖️ **ONE OF THE THREE CANNOT BE DONE THIS WAY AT ALL**, and that option is
    offered as an equal third rather than hidden. A method sorter whose every
    item has a method teaches that the technique in front of you is always the
    technique — which is the habit c3-05 then has to undo.

    ⚠️ THERE IS NO `correct` KEY IN THE PAYLOAD AND THIS RENDERER MUST NEVER
    GROW ONE. The author dropped it deliberately: reading it would mark an
    option outside the mastery ladder, which R3 forbids. The reveal names the
    method in `answer` and explains it in `why`; a student who chose otherwise
    reads the same panel in the same tone, and works out the difference
    themselves. That is the whole design.

    One shot per item — the other buttons disable on commit, because the
    answer is on screen from that moment. Same contract as `purity-sorter`.

    HOOKS: `data-mchoice` (wrapper, `data-total`) · `data-mchoice-item`
    (valued with the item id) · `data-mchoice-opt` (valued with the option id)
    · `data-mchoice-reveal`.
    """
    items = a.get("items") or []
    options = a.get("options") or []
    if not items:
        raise ValueError("method-choice %r declares no items[]." % act_id)
    if len(options) < 2:
        raise ValueError(
            "method-choice %r offers %d option(s); a commitment needs "
            "something to choose between." % (act_id, len(options)))
    for it in items:
        for key in ("answer", "why"):
            if not it.get(key):
                raise ValueError(
                    "method-choice %r item %r has no %r. The reveal is the "
                    "only thing this instrument says — nothing here marks, so "
                    "a missing reveal leaves the student with nothing at all."
                    % (act_id, it.get("id"), key))

    cards = "".join(
        '<div class="ks3-mchoice-item" data-mchoice-item="%s">'
        '<p class="ks3-mchoice-task">%s</p>'
        '<div class="ks3-mchoice-opts">%s</div>'
        '<div class="ks3-mchoice-reveal" hidden data-mchoice-reveal>'
        '<p class="ks3-mchoice-answer">%s</p>'
        '<p class="ks3-mchoice-why">%s</p></div></div>'
        % (e(it.get("id", "")), rich(it.get("task", "")),
           "".join(_seg("ks3-mchoice-opt", False, o.get("label", ""),
                        data_mchoice_opt=o.get("id", ""))
                   for o in options),
           t(it["answer"]), rich(it["why"]))
        for it in items)
    return ('<div class="ks3-mchoice" data-mchoice data-total="%d">%s</div>'
            % (len(items), cards))


# ═══ c3-05 · still-run ═══════════════════════════════════════════════════

def r_still_run(a, act_id):
    """⊕ c3-05 `#s-still` — boil to separate, cool to collect.

    ⚖️ **THE NO-COOLING BRANCH IS A LEGITIMATE, REACHABLE STATE THAT COLLECTS
    NOTHING, AND IT IS NOT AN ERROR.** `warm_condenser` is the point of the
    lesson: turn the condenser water off and the boiling still separates the
    mixture perfectly — the flask proves it — and you end up with an empty
    beaker and a room that smells of it. Doing one of distillation's two jobs
    gets you nothing. So that branch is drawn with the same weight as the
    successful run, and `completion.requires_cooling` means it does not tick
    the rail: the student has seen something true and has not yet distilled
    anything.

    ⚠️ THE LAST STAGE HAS ITS OWN WARM TEXT, `warm_final`, AND IT MATTERS.
    Design's page overrides only stage 3 when the cooling is off (page line
    546) and leaves stage 4 saying "Clear drops run into the beaker" — which
    contradicts the stage above it and is the one place the branch stops being
    honest. The payload authors a per-mixture `warm_final` for exactly that
    slot; it is used, and the discrepancy is reported rather than silently
    reconciled.

    ⚠️ EMIT-BOTH-SHOW-ONE, HARD. Three mixtures × (a predict panel, four
    stages with up to two texts each, a result panel) are all in the document
    and one set is shown. Nothing composes a stage's sentence at run time, so
    every authored `<em>` survives, and switching mixture cannot lose text.

    ⚠️ The stage HEADINGS ("Stage 1" … "Stage 4") are structural and composed
    here at build time, as Design composes them. They are the numbering of a
    list, in the same class as the ladder's A/B/C letters — not authored copy.

    HOOKS: `data-still` (wrapper, `data-cfg`) · `data-still-group` (a dial's
    row) · `data-still-opt` with `data-still-for` + `data-still-val` ·
    `data-still-predict` (valued with the mixture id; one shown) ·
    `data-still-predict-opts` (the lettered list inside it) ·
    `data-still-body` · `data-still-gauge` (a tile) with `data-still-gval` on
    its value node · `data-still-stages` (valued with the mixture id) ·
    `data-still-stage` (an `<li>`, valued with the 0-based index) ·
    `data-still-stagebody` (the wrapper that opens) · `data-still-text` /
    `data-still-warm` (the two bodies of a stage) · `data-still-next`
    (carrying `data-still-start-label` and `data-still-next-label`) ·
    `data-still-reset` · `data-still-result` (valued with a mixture id, or
    `warm` for the no-cooling branch).
    """
    mixtures = a.get("mixtures") or []
    dials = a.get("dials") or []
    gauges = a.get("gauges") or []
    warm = a.get("warm_condenser") or {}
    controls = a.get("controls") or {}
    if not mixtures or not dials or not gauges:
        raise ValueError(
            "still-run %r needs mixtures[], dials[] and gauges[]." % act_id)
    if not warm.get("stage_text") or not warm.get("result_text"):
        raise ValueError(
            "still-run %r declares no `warm_condenser` text. Turning the "
            "cooling off is a reachable state and the whole argument of the "
            "lesson; a state with nothing to say is the one defect this "
            "instrument cannot carry." % act_id)
    counts = set(len(m.get("stages") or []) for m in mixtures)
    if len(counts) != 1 or 0 in counts:
        raise ValueError(
            "still-run %r declares stage counts %s. Every mixture runs the "
            "same still through the same stages; a mixture with fewer would "
            "leave the stepper's controls pointing at nothing."
            % (act_id, sorted(counts)))
    n_stages = counts.pop()
    warm_at = int(warm.get("stage") or 0) - 1

    # ── the two dials ────────────────────────────────────────────────────
    names = dict((m["id"], m.get("name", "")) for m in mixtures)
    dial_html = []
    for d in dials:
        did = d.get("id")
        opts = []
        for o in (d.get("options") or []):
            if isinstance(o, dict):
                opts.append((o.get("id", ""), o.get("label", "")))
            else:
                opts.append((o, names.get(o, o)))
        if not opts:
            raise ValueError(
                "still-run %r dial %r offers nothing to press."
                % (act_id, did))
        start = d.get("start") or opts[0][0]
        dial_html.append(
            '<div class="ks3-still-dial" data-still-group="%s">'
            '<p class="ks3-still-diallabel">%s</p>'
            '<div class="ks3-still-btns">%s</div></div>'
            % (e(did), t(d.get("label", "")),
               "".join(_seg("ks3-still-opt", val == start, lab,
                            data_still_for=str(did), data_still_val=str(val))
                       for val, lab in opts)))
    m0 = next((d.get("start") for d in dials if d.get("id") == "mixture"),
              None) or mixtures[0]["id"]
    m0rec = next(m for m in mixtures if m["id"] == m0)

    # ── the per-mixture predict panels ───────────────────────────────────
    predicts = "".join(
        '<div class="ks3-still-predict"%s data-still-predict="%s">'
        '<p class="ks3-commit">%s</p>%s</div>'
        % ("" if m["id"] == m0 else " hidden", e(m["id"]),
           t(m.get("predict", "")),
           _lettered(m.get("options") or [], "data-still-predict-opts"))
        for m in mixtures)

    # ── the gauges, at rest ──────────────────────────────────────────────
    gauge_html = []
    for g in gauges:
        if g.get("before_from") == "name":
            before = m0rec.get("name", "")
        else:
            before = g.get("before", "")
        if g.get("id") == "thermometer" and g.get("show_thermometer") is False:
            before = g.get("hidden_value") or before
        gauge_html.append(
            '<div class="ks3-still-gauge" data-still-gauge="%s">'
            '<p class="ks3-still-glabel">%s</p>'
            '<p class="ks3-still-gvalue" data-still-gval="%s">%s</p></div>'
            % (e(g.get("id", "")), t(g.get("label", "")),
               e(g.get("id", "")), t(before)))

    # ── the per-mixture stage lists ──────────────────────────────────────
    stage_lists = []
    for m in mixtures:
        rows = []
        for i, text in enumerate(m.get("stages") or []):
            warm_text = ""
            if i == warm_at:
                warm_text = warm.get("stage_text", "")
            elif i == n_stages - 1 and m.get("warm_final"):
                warm_text = m["warm_final"]
            warm_node = ('<p class="ks3-still-stagetext" hidden '
                         'data-still-warm>%s</p>' % rich(warm_text)
                         if warm_text else "")
            rows.append(
                '<li class="ks3-still-stage" data-still-stage="%d">'
                '<span class="ks3-still-num" aria-hidden="true">%d</span>'
                '<div class="ks3-still-stagebody">'
                '<p class="ks3-still-stagetitle">Stage %d</p>'
                '<div class="ks3-still-stagetexts" hidden '
                'data-still-stagebody>'
                '<p class="ks3-still-stagetext" data-still-text>%s</p>%s'
                '</div></div></li>'
                % (i, i + 1, i + 1, rich(text), warm_node))
        stage_lists.append(
            '<ol class="ks3-still-stages"%s data-still-stages="%s" '
            'role="list">%s</ol>'
            % ("" if m["id"] == m0 else " hidden", e(m["id"]), "".join(rows)))

    # ── the results, including the no-cooling one ────────────────────────
    results = "".join(
        '<div class="ks3-still-result" hidden data-still-result="%s">'
        '<p class="ks3-still-resulttitle">%s</p>'
        '<p class="ks3-still-resulttext">%s</p></div>'
        % (e(m["id"]), t(m.get("result_title", "")),
           rich(m.get("result_text", "")))
        for m in mixtures)
    results += ('<div class="ks3-still-result" hidden '
                'data-still-result="warm">'
                '<p class="ks3-still-resulttitle">%s</p>'
                '<p class="ks3-still-resulttext">%s</p></div>'
                % (t(warm.get("result_title", "")),
                   rich(warm.get("result_text", ""))))

    completion = a.get("completion") or {}
    cfg = {
        "stages": n_stages,
        "warm_at": warm_at,
        "gauges": [{"id": g.get("id"), "reads": g.get("reads"),
                    "before": g.get("before", ""),
                    "before_from": g.get("before_from", ""),
                    "warm_value": g.get("warm_value", ""),
                    "hidden_value": g.get("hidden_value", ""),
                    "show": g.get("show_thermometer") is not False}
                   for g in gauges],
        "mixtures": [{"id": m["id"], "name": m.get("name", ""),
                      "temp": m.get("temp", ""), "left": m.get("left", ""),
                      "collected": m.get("collected", "")}
                     for m in mixtures],
        "completion": {
            "runs": int(completion.get("runs_required") or 1),
            "requires_cooling":
                completion.get("requires_cooling") is not False},
        "start": {"mixture": m0},
    }
    return ('<div class="ks3-still" data-still data-cfg="%s">'
            '<div class="ks3-still-dials">%s</div>%s'
            '<div class="ks3-still-body" hidden data-still-body>'
            '<div class="ks3-still-gauges">%s</div>%s'
            '<div class="ks3-still-controls">'
            '<button type="button" class="ks3-reveal-btn ks3-still-next" '
            'data-still-next data-still-start-label="%s" '
            'data-still-next-label="%s">%s</button>'
            '<button type="button" class="ks3-retry ks3-still-reset" '
            'data-still-reset>%s</button></div>%s</div></div>'
            % (_cfg(cfg), "".join(dial_html), predicts,
               "".join(gauge_html), "".join(stage_lists),
               e(controls.get("start", "")), e(controls.get("next", "")),
               t(controls.get("start", "")), t(controls.get("reset", "")),
               results))


# ═══ c3-06 · chroma-run ══════════════════════════════════════════════════

def _chroma_bottom(rf, geom):
    """A spot's height as a PERCENTAGE of the lane. Never a pixel.

    ⚠️ `baseline_pct + rf × span_pct`, exactly as Design composes it, and the
    reason it is proportional is written into NOTES §3.4: a real photographed
    chromatogram can replace the drawn lane without touching the payload, so
    long as the geometry stays a ratio. The lane's own height is the only
    absolute number, and it is authored once as `height_px`.
    """
    return (float(geom.get("baseline_pct") or 0)
            + float(rf) * float(geom.get("span_pct") or 0))


def r_chroma_run(a, act_id):
    """⊕ c3-06 `#s-lab` — three decisions, each with its own failure mode.

    ⚖️ **EACH FAULT NAMES WHICH DECISION CAUSED IT.** Never "you got it
    wrong": "You drew the baseline in pen. Pen ink is a mixture of dyes
    dissolved in a solvent — exactly the thing this experiment separates."
    This is the only lesson in the unit where a student can produce an
    unreadable result, and the whole value of that is being told precisely
    which of the three decisions did it. `fault_order` gives precedence when
    more than one applies, so a run with two mistakes is diagnosed by the one
    that ruined it first.

    ⚖️ SPOTS ARE POSITIONED BY `rf` AS A PERCENTAGE OF THE LANE, using
    `lane_geometry`. No pixel positions anywhere: see `_chroma_bottom`.

    ⚠️ `R<sub>f</sub>` — the course convention since C2 flag 13 — uses a real
    `<sub>` element and never a Unicode subscript. It does NOT appear inside
    this instrument: Design's bench never quotes a value, and inventing one
    here would be authoring content in a renderer. The three places C3 does
    quote it — the explainer, the stretch panel and a self-check criterion —
    are rendered by the SHELL, and they land correctly on the built page,
    because `_RICH_OK` in `ks3_art/kit.py` admits `sub` alongside `em` and
    `strong` (the MRB-272 ruling of 20 Aug 2026). Verified in the built HTML
    rather than assumed: `chromatography.html` carries three real `<sub>`
    elements and no escaped one. Everything this renderer puts on the page
    goes through the same `rich()`, so an authored subscript would survive
    here too if a later payload wanted one.

    ⚠️ EMIT-BOTH-SHOW-ONE for all four outcomes (the clean run and the three
    faults) and all four verdict responses. The runtime chooses a node; it
    never writes a sentence.

    HOOKS: `data-chroma` (wrapper, `data-cfg`) · `data-chroma-group` (a
    decision's row) · `data-chroma-opt` with `data-chroma-for` +
    `data-chroma-val` + `data-chroma-fault` (empty string for the clean
    choice) · `data-chroma-run` · `data-chroma-paper` (the `role="img"` whose
    `aria-label` is swapped per outcome) · `data-chroma-lane` ·
    `data-chroma-strip` · `data-chroma-baseline` · `data-chroma-spot`
    (carrying `data-rf` and `data-c`) · `data-chroma-outcomes` /
    `data-chroma-outcome` (valued `good` or a fault id) ·
    `data-chroma-verdict` · `data-chroma-pen` (a verdict button) ·
    `data-chroma-say` (valued with a pen id).
    """
    decisions = a.get("decisions") or []
    lanes = a.get("lanes") or []
    geom = a.get("lane_geometry") or {}
    faults = a.get("faults") or {}
    good = a.get("good") or {}
    verdict = a.get("verdict") or {}
    if not decisions or not lanes:
        raise ValueError(
            "chroma-run %r needs both decisions[] and lanes[]." % act_id)
    for key in ("height_px", "baseline_pct", "span_pct"):
        if geom.get(key) is None:
            raise ValueError(
                "chroma-run %r lane_geometry has no %r. Spots are placed as a "
                "PERCENTAGE of the lane so a real photograph can replace the "
                "drawing without a payload change; without the geometry the "
                "only thing left is a pixel." % (act_id, key))
    named = set(o.get("fault") for d in decisions
                for o in (d.get("options") or []))
    named.discard(None)
    unknown = sorted(named - set(faults))
    if unknown:
        raise ValueError(
            "chroma-run %r offers decision(s) leading to fault(s) %s, which "
            "`faults` does not describe. A ruined run with nothing to say is "
            "the student told they failed and not told why."
            % (act_id, unknown))
    unordered = sorted(named - set(a.get("fault_order") or []))
    if unordered:
        raise ValueError(
            "chroma-run %r leaves fault(s) %s out of `fault_order`. Two "
            "mistakes at once need a rule for which one ruined the run first, "
            "or the diagnosis depends on dict order." % (act_id, unordered))

    # ── the three decisions ──────────────────────────────────────────────
    dial_html = []
    for d in decisions:
        opts = d.get("options") or []
        start = int(d.get("start") or 0)
        dial_html.append(
            '<div class="ks3-chroma-dial" data-chroma-group="%s">'
            '<p class="ks3-chroma-diallabel">%s</p>'
            '<div class="ks3-chroma-btns">%s</div></div>'
            % (e(d.get("id", "")), t(d.get("label", "")),
               "".join(_seg("ks3-chroma-opt", i == start, o.get("label", ""),
                            data_chroma_for=d.get("id", ""),
                            data_chroma_val=str(i),
                            data_chroma_fault=o.get("fault") or "")
                       for i, o in enumerate(opts))))

    # ── the paper, drawn in its CLEAN state ──────────────────────────────
    lane_html = []
    for ln in lanes:
        spots = "".join(
            '<span class="ks3-chroma-spot" data-chroma-spot data-rf="%s" '
            'data-c="%s" style="bottom:%.4g%%;background:%s"></span>'
            % (e(sp.get("rf")), e(sp.get("c", "")),
               _chroma_bottom(sp.get("rf") or 0, geom), e(sp.get("c", "")))
            for sp in (ln.get("spots") or []))
        lane_html.append(
            '<div class="ks3-chroma-lane" data-chroma-lane="%s">'
            '<div class="ks3-chroma-strip" data-chroma-strip '
            'style="height:%dpx">%s'
            '<span class="ks3-chroma-baseline" aria-hidden="true" '
            'data-chroma-baseline style="bottom:%.4g%%"></span></div>'
            '<p class="ks3-chroma-lanelabel">%s</p></div>'
            % (e(ln.get("id", "")), int(geom["height_px"]), spots,
               float(geom["baseline_pct"]), t(ln.get("label", ""))))

    # ── the four outcomes, all in the document ───────────────────────────
    outcomes = ('<div class="ks3-chroma-outcome" hidden '
                'data-chroma-outcome="good">'
                '<p class="ks3-chroma-outtitle">%s</p>'
                '<p class="ks3-chroma-outtext">%s</p></div>'
                % (t(good.get("title", "")), rich(good.get("text", ""))))
    outcomes += "".join(
        '<div class="ks3-chroma-outcome" hidden data-chroma-outcome="%s">'
        '<p class="ks3-chroma-outtitle">%s</p>'
        '<p class="ks3-chroma-outtext">%s</p></div>'
        % (e(fid), t(faults[fid].get("title", "")),
           rich(faults[fid].get("text", "")))
        for fid in (a.get("fault_order") or []))

    # ── the forensic verdict ─────────────────────────────────────────────
    match = verdict.get("match")
    says = "".join(
        '<div class="ks3-chroma-say" hidden data-chroma-say="%s">'
        '<p class="ks3-chroma-saytitle">%s</p>'
        '<p class="ks3-chroma-saytext">%s</p></div>'
        % (e(o.get("id", "")),
           t(verdict.get("hit_title" if o.get("id") == match
                         else "miss_title", "")),
           rich(verdict.get("hit_text", "") if o.get("id") == match
                else (verdict.get("miss_text") or {}).get(o.get("id"), "")))
        for o in (verdict.get("options") or []))

    cfg = {
        "geometry": geom,
        "fault_order": a.get("fault_order") or [],
        "faults": dict((k, dict((kk, vv) for kk, vv in v.items()
                                if kk not in ("title", "text")))
                       for k, v in faults.items()),
        "good_alt": good.get("alt", ""),
        "lanes": [{"id": ln.get("id"),
                   "spots": [{"c": sp.get("c"), "rf": sp.get("rf")}
                             for sp in (ln.get("spots") or [])]}
                  for ln in lanes],
        "match": match,
    }
    return ('<div class="ks3-chroma" data-chroma data-cfg="%s">'
            '<div class="ks3-chroma-dials">%s</div>'
            '<div class="ks3-chroma-foot">'
            '<button type="button" class="ks3-reveal-btn ks3-chroma-runbtn" '
            'data-chroma-run>%s</button></div>'
            '<div class="ks3-chroma-paper" role="img" aria-label="%s" hidden '
            'data-chroma-paper><div class="ks3-chroma-lanes">%s</div></div>'
            '<div class="ks3-chroma-outcomes" hidden data-chroma-outcomes>%s'
            '</div>'
            '<div class="ks3-chroma-verdict" hidden data-chroma-verdict>'
            '<p class="ks3-chroma-ask">%s</p>'
            '<p class="ks3-chroma-note">%s</p>'
            '<div class="ks3-chroma-pens">%s</div>%s</div></div>'
            % (_cfg(cfg), "".join(dial_html), t(a.get("run_label", "")),
               e(good.get("alt", "")), "".join(lane_html), outcomes,
               t(verdict.get("prompt", "")), rich(verdict.get("note", "")),
               "".join(_seg("ks3-chroma-pen", False, o.get("label", ""),
                            data_chroma_pen=o.get("id", ""))
                       for o in (verdict.get("options") or [])),
               says))


# ═══ c3-07 · plan-critique and melting-point-bench ══════════════════════

def r_plan_critique(a, act_id):
    """⊕ c3-07 `#s-critique` — four judgements on somebody else's plan.

    ⚖️ **CRITIQUE COMES BEFORE CONSTRUCT** (NOTES §2, and the map's rule for
    an INVESTIGATION lesson). This is the FIRST instrument on the page: a
    student rules on four steps of a plan that is not theirs, discovers that
    all four are observations rather than measurements with an expected value,
    and only then builds one. Judging somebody else's work first is what makes
    the construction a decision instead of a recipe.

    ⚠️ NOTHING MARKS. Two options, one shot, and a reveal that names what the
    step is actually worth — "Useful, and not enough", "Measures the balance,
    not the powder" — in the same tone whichever button was pressed.

    ⚠️ `data-critiq`, NOT `data-critique`. `wireCritique` in `shared/ks3.js`
    already claims `[data-critique]` for a different family; a shared selector
    would hand this instrument to that one's handler and neither would work.

    HOOKS: `data-critiq` (wrapper, `data-total`) · `data-critiq-item` (valued
    with the step id) · `data-critiq-opt` (valued with the option id) ·
    `data-critiq-reveal` · `data-critiq-close`.
    """
    steps = a.get("steps") or []
    options = a.get("options") or []
    if not steps:
        raise ValueError("plan-critique %r declares no steps[]." % act_id)
    if len(options) != 2:
        raise ValueError(
            "plan-critique %r offers %d option(s); Design draws a two-option "
            "judgement — could it settle the question, or could it not."
            % (act_id, len(options)))
    for s in steps:
        for key in ("answer", "why"):
            if not s.get(key):
                raise ValueError(
                    "plan-critique %r step %r has no %r. Nothing here marks, "
                    "so the reveal is the only thing the instrument says."
                    % (act_id, s.get("id"), key))

    cards = "".join(
        '<div class="ks3-critiq-item" data-critiq-item="%s">'
        '<p class="ks3-critiq-step">%s</p>'
        '<div class="ks3-critiq-opts">%s</div>'
        '<div class="ks3-critiq-reveal" hidden data-critiq-reveal>'
        '<p class="ks3-critiq-answer">%s</p>'
        '<p class="ks3-critiq-why">%s</p></div></div>'
        % (e(s.get("id", "")), rich(s.get("step", "")),
           "".join(_seg("ks3-critiq-opt", False, o.get("label", ""),
                        data_critiq_opt=o.get("id", ""))
                   for o in options),
           t(s["answer"]), rich(s["why"]))
        for s in steps)
    close = ('<div class="ks3-critiq-close" hidden data-critiq-close>'
             '<p>%s</p></div>' % rich(a["closing"])) if a.get("closing") else ""
    return ('<div class="ks3-critiq" data-critiq data-total="%d">%s%s</div>'
            % (len(steps), cards, close))


def _mpb_fix(v, decimals):
    return ("%%.%df" % int(decimals)) % float(v)


def _mpb_row(run, fast, model, decimals, unit, wide_above):
    """One row of the table, as the BENCH measures it.

    ⚖️ **FAST HEATING MAKES A MEASURED RANGE READ NARROWER**, and it is the
    right way round: the thermometer lags the block, so the start is recorded
    late (the melt has already begun) and the end drifts up. `collapse` eats
    55% of the range from the bottom and `end_shift` adds 1.5 °C at the top.
    A student who heats fast gets repeats that agree beautifully — because the
    same error happened three times.

    ⚠️ THE BENCH IS THE MEASUREMENT AND THE PROSE FOLLOWS IT. If a sentence
    ever disagrees with a number this function produces, the number is right
    and the sentence is the thing that changes.
    """
    start, end = float(run["start"]), float(run["end"])
    if fast:
        start = start + (end - start) * float(model.get("collapse") or 0)
        end = end + float(model.get("end_shift") or 0)
    span = end - start
    return (_mpb_fix(start, decimals) + " " + unit,
            _mpb_fix(end, decimals) + " " + unit,
            _mpb_fix(span, decimals) + " " + unit,
            span > float(wide_above))


def r_melting_point_bench(a, act_id):
    """⊕ c3-07 `#s-bench` — three samples, two decisions, and an anomaly.

    ⚖️ **A PURE SAMPLE MELTS SHARPLY; AN IMPURE ONE MELTS LOWER AND OVER A
    RANGE.** Both halves point the same way in the data and in every sentence
    about it: batch 1 melts within a degree at 53 °C, batch 2 starts around
    45 °C and takes six or seven degrees to finish.

    ⚖️ **THE ANOMALY IS REPORTED, NEVER DROPPED.** Batch 3's second run melts
    47.5–52.0 while its other two melt within a degree. It stays in the table,
    at full weight, and the verdict for batch 3 says what to do with it — set
    it aside WITH A REASON WRITTEN DOWN. An instrument that hid the odd run
    would teach the opposite of the lesson's title. Nothing in this renderer
    filters `runs`, and nothing may be added that does.

    ⚖️ THE TRUST BRANCH. `trusted_when` is slow heating with more than one
    repeat; batch 2's verdict carries two tails, one for data that can carry
    the claim and one for data that points the right way and cannot. Both are
    in the document. Naming the right batch off untrustworthy data is not the
    same achievement as measuring it, and the instrument says so.

    ⚠️ THE RESTING TABLE IS THE AUTHORED DEFAULT — slow, three repeats — and
    is computed here rather than left blank, so the bytes carry the same nine
    rows the runtime would. Rows beyond the opening repeat count are in the
    document and hidden, so the repeats dial reveals rows rather than
    rebuilding a table.

    HOOKS: `data-mpb` (wrapper, `data-cfg`) · `data-mpb-group` (a dial's row)
    · `data-mpb-opt` with `data-mpb-for` + `data-mpb-val` · `data-mpb-run`
    (carrying `data-mpb-runlabel` and `data-mpb-rerunlabel`) ·
    `data-mpb-data` · `data-mpb-sample` (valued with the sample id) ·
    `data-mpb-row` (a `<tr>`, valued with the 0-based run index) ·
    `data-mpb-cell` (valued `start`, `end` or `range`; the range cell also
    carries `data-mpb-wide`) · `data-mpb-note` (valued `<rate>:<repeats>`;
    one shown) · `data-mpb-verdict-btn` · `data-mpb-say` (valued with a sample
    id) · `data-mpb-trusted` / `data-mpb-untrusted` (the two tails inside one
    say).
    """
    samples = a.get("samples") or []
    dials = a.get("dials") or []
    notes = a.get("notes") or []
    verdicts = a.get("verdicts") or []
    if not samples or not dials:
        raise ValueError(
            "melting-point-bench %r needs both samples[] and dials[]."
            % act_id)
    counts = set(len(s.get("runs") or []) for s in samples)
    if len(counts) != 1 or 0 in counts:
        raise ValueError(
            "melting-point-bench %r declares run counts %s. Every sample is "
            "run the same number of times — comparing three repeats of one "
            "batch against one of another is the thing the repeats dial "
            "exists to talk about, not a state of the data."
            % (act_id, sorted(counts)))
    decimals = int(a.get("decimals", 1))
    unit = a.get("unit") or ""
    model = a.get("fast_model") or {}
    wide_above = a.get("wide_above")
    if wide_above is None:
        raise ValueError(
            "melting-point-bench %r declares no `wide_above`. A range is only "
            "wide against a threshold, and the threshold is the whole reading "
            "of the table." % act_id)

    rate0 = next((d.get("default") for d in dials if d.get("id") == "rate"),
                 "slow")
    reps0 = int(next((d.get("default") for d in dials
                      if d.get("id") == "repeats"), 1))
    dial_html = []
    for d in dials:
        did = d.get("id")
        default = str(d.get("default"))
        dial_html.append(
            '<div class="ks3-mpb-dial" data-mpb-group="%s">'
            '<p class="ks3-mpb-diallabel">%s</p>'
            '<div class="ks3-mpb-btns">%s</div></div>'
            % (e(did), t(d.get("label", "")),
               "".join(_seg("ks3-mpb-opt", str(o.get("id")) == default,
                            o.get("label", ""), data_mpb_for=str(did),
                            data_mpb_val=str(o.get("id")))
                       for o in (d.get("options") or []))))

    columns = a.get("columns") or []
    head = "".join('<th scope="col">%s</th>' % t(c) for c in columns)
    tables = []
    for s in samples:
        rows = []
        for i, run in enumerate(s.get("runs") or []):
            start, end, span, wide = _mpb_row(run, rate0 == "fast", model,
                                              decimals, unit, wide_above)
            rows.append(
                '<tr data-mpb-row="%d"%s>'
                '<td>%d</td>'
                '<td data-mpb-cell="start">%s</td>'
                '<td data-mpb-cell="end">%s</td>'
                '<td class="ks3-mpb-range" data-mpb-cell="range" '
                'data-mpb-wide="%s">%s</td></tr>'
                % (i, "" if i < reps0 else " hidden", i + 1,
                   t(start), t(end), "1" if wide else "0", t(span)))
        tables.append(
            '<div class="ks3-mpb-sample" data-mpb-sample="%s">'
            '<p class="ks3-mpb-name">%s</p>'
            '<table class="ks3-mpb-table"><thead><tr>%s</tr></thead>'
            '<tbody>%s</tbody></table></div>'
            % (e(s.get("id", "")), t(s.get("name", "")), head, "".join(rows)))

    note_html = "".join(
        '<p class="ks3-mpb-note"%s data-mpb-note="%s:%s">%s</p>'
        % ("" if (n.get("rate") == rate0
                  and int(n.get("repeats") or 0) == reps0) else " hidden",
           e(n.get("rate", "")), e(n.get("repeats", "")),
           rich(n.get("text", "")))
        for n in notes)

    trusted = a.get("trusted_when") or {}
    says = []
    for v in verdicts:
        tails = ""
        if v.get("text_trusted") or v.get("text_untrusted"):
            tails = ('<span data-mpb-trusted hidden> %s</span>'
                     '<span data-mpb-untrusted hidden> %s</span>'
                     % (rich(v.get("text_trusted", "")),
                        rich(v.get("text_untrusted", ""))))
        says.append(
            '<div class="ks3-mpb-say" hidden data-mpb-say="%s">'
            '<p class="ks3-mpb-saytitle">%s</p>'
            '<p class="ks3-mpb-saytext">%s%s</p></div>'
            % (e(v.get("id", "")), t(v.get("title", "")),
               rich(v.get("text", "")), tails))

    cfg = {
        "samples": [{"id": s.get("id"), "runs": s.get("runs") or []}
                    for s in samples],
        "fast_model": model,
        "decimals": decimals,
        "unit": unit,
        "wide_above": wide_above,
        "trusted_when": {
            "rate": trusted.get("rate", ""),
            "repeats_above": int(trusted.get("repeats_above") or 0)},
        "start": {"rate": rate0, "repeats": reps0},
    }
    return ('<div class="ks3-mpb" data-mpb data-cfg="%s">'
            '<div class="ks3-mpb-dials">%s</div>'
            '<div class="ks3-mpb-foot">'
            '<button type="button" class="ks3-reveal-btn ks3-mpb-runbtn" '
            'data-mpb-run data-mpb-runlabel="%s" data-mpb-rerunlabel="%s">%s'
            '</button></div>'
            '<div class="ks3-mpb-data" hidden data-mpb-data>'
            '<div class="ks3-mpb-samples">%s</div>'
            '<div class="ks3-mpb-notes">%s</div>'
            '<div class="ks3-mpb-verdict">'
            '<p class="ks3-mpb-ask">%s</p>'
            '<div class="ks3-mpb-verdicts">%s</div>%s</div></div></div>'
            % (_cfg(cfg), "".join(dial_html),
               e(a.get("run_label", "")), e(a.get("rerun_label", "")),
               t(a.get("run_label", "")), "".join(tables), note_html,
               t(a.get("verdict_prompt", "")),
               "".join(_seg("ks3-mpb-verdict-btn", False, b.get("label", ""),
                            data_mpb_verdict_btn=b.get("id", ""))
                       for b in (a.get("verdict_buttons") or [])),
               "".join(says)))


# ═══ the drawn figure ════════════════════════════════════════════════════

def _wrap(text, width):
    """Greedy word wrap. SVG has no line box, so the lines are counted here."""
    words, lines, line = str(text).split(), [], ""
    for w in words:
        trial = (line + " " + w) if line else w
        if len(trial) > width and line:
            lines.append(line)
            line = w
        else:
            line = trial
    if line:
        lines.append(line)
    return lines


def _panels_desc(panels, colours, big_i, small_i, sizes, gap, fibre):
    """The `<desc>`: the drawing walked in reading order, as drawn.

    Composed rather than authored because the numbers in it — the counts, the
    diameters, the gap — are decided by the drawer. A hand-written description
    of a derived geometry is a second statement of the same fact and goes out
    of date the first time a particle is resized.
    """
    def side(i, held):
        p = panels[i]
        dots = p.get("dots") or []
        widths = sorted(set(float(x[1]) for x in dots))
        kinds = sorted(set(colours.get(x[0], x[0]) for x in dots))
        return (
            "The %s panel is labelled “%s”. Resting on top of the "
            "paper are %d round particles, drawn %s, in %d colour%s, with "
            "diameters of %s units. %s The note under the panel reads: "
            "“%s”"
            % ("left" if i == 0 else "right",
               p.get("label", ""), len(dots),
               "almost touching one another so that they read as one lump"
               if held else "spaced apart as separate particles",
               len(kinds), "" if len(kinds) == 1 else "s",
               " and ".join("%g" % w for w in widths),
               ("Every one of them is wider than a gap in the paper, so "
                "nothing at all is drawn below the paper on this side — the "
                "empty space under the band is the point of the panel."
                if held else
                "Every one of them is narrower than a gap, and three of them "
                "are drawn again below the paper, each sitting in a gap it "
                "has passed through."),
               p.get("text", "")))

    return (
        "A two-panel particle diagram, drawn to one scale, with the same "
        "filter paper in both panels. Across the middle of each panel runs "
        "the paper, seen edge on: a horizontal band closed top and bottom by "
        "a solid ink line, with short fibres %d units long between them and "
        "gaps of %d units between the fibres. %s %s The two panels sit side "
        "by side so that the same %d-unit gap can be compared with both sets "
        "of particles. Under a full-width rule at the foot of the plate, a "
        "line of small monospaced text gives the scale: gaps %d units, %s "
        "from %g to %g units, %s from %g to %g units."
        % (fibre, gap, side(big_i, True), side(small_i, False), gap, gap,
           (panels[big_i].get("label") or "").lower(),
           min(sizes[big_i]), max(sizes[big_i]),
           (panels[small_i].get("label") or "").lower(),
           min(sizes[small_i]), max(sizes[small_i])))


def _particle_panels(fig):
    """⊕ c3-03 — THE LOAD-BEARING FIGURE OF THE UNIT.

    ⚖️ **THIS IS WHY NO FILTER CAN HOLD BACK SALT**, and it is the one claim
    in C3 that a sentence cannot make. `MIX-07` is "a fine enough filter would
    separate salt from water"; the answer is a comparison of three sizes — the
    grain, the gap and the dissolved particle — and a comparison of sizes is a
    drawing or it is nothing.

    ⚖️ **SO THE GEOMETRY HAS TO EXPRESS THE FACT, NOT MERELY ACCOMPANY IT.**
    Every retained particle is drawn WIDER than the paper's gaps and every
    passing particle NARROWER, at one scale, against one paper. The gap is
    therefore DERIVED — the midpoint between the largest passing particle and
    the smallest retained one — and the drawer REFUSES a payload where the two
    sets overlap, because a drawing that says the opposite of its caption is
    worse than no drawing at all.

    ⚠️ Design's own dash rhythm is 9 units of fibre to 6 of gap, and at a
    6-unit gap the authored salt particles (7 and 10 units) are BIGGER than
    the holes they are said to pass through. Design's page carries the claim
    in words only, so the defect never showed there. The 3:2 ratio is kept;
    the absolute numbers now come from the particles.

    ⚠️ The `<desc>` is COMPOSED HERE, from what was actually drawn, and it
    replaces the figure record's 263-character summary. MRB-254 requires the
    description to walk the drawing in reading order, and only the drawer
    knows the reading order, the counts and the sizes. The authored `desc`
    also describes a different layout — one paper with sand above and salt
    below — from the two-panel arrangement Design drew and this reproduces;
    that discrepancy is in the delivery report.
    """
    d = fig.get("data") or {}
    panels = d.get("panels") or []
    colours = d.get("colours") or {}
    if len(panels) != 2:
        raise ValueError(
            "particle-panels figure %r declares %d panel(s). It is a PAIR: "
            "one sample the paper holds and one it cannot, against the same "
            "paper. A single panel shows some circles and argues nothing."
            % (fig.get("id"), len(panels)))
    sizes = []
    for p in panels:
        dots = p.get("dots") or []
        if not dots or not p.get("label") or not p.get("text"):
            raise ValueError(
                "particle-panels figure %r has a panel with no dots, no label "
                "or no text. The label says which sample it is, the dots are "
                "the claim, and the text is what the claim means."
                % fig.get("id"))
        for pair in dots:
            if float(pair[1]) <= 0:
                raise ValueError(
                    "particle-panels figure %r draws a particle of diameter "
                    "%r." % (fig.get("id"), pair[1]))
        sizes.append([float(x[1]) for x in dots])
    big_i = 0 if max(sizes[0]) >= max(sizes[1]) else 1
    small_i = 1 - big_i
    if min(sizes[big_i]) <= max(sizes[small_i]):
        raise ValueError(
            "particle-panels figure %r draws a retained particle of %g units "
            "and a passing particle of %g. The whole diagram is that every "
            "particle on one side is wider than the paper's gaps and every "
            "particle on the other is narrower; overlapping sets leave no gap "
            "width that makes the drawing true."
            % (fig.get("id"), min(sizes[big_i]), max(sizes[small_i])))

    # The gap sits between the two sets; the fibre keeps Design's 3:2 rhythm.
    gap = int(round((max(sizes[small_i]) + min(sizes[big_i])) / 2.0))
    fibre = int(round(gap * 1.5))

    PW, GAP_X, X0, PY = 416, 32, 8, 8
    W = X0 * 2 + PW * 2 + GAP_X
    INNER = PW - 44
    PAPER_TOP, BH = 130, 18
    PAPER_BOT = PAPER_TOP + BH
    TEXT_Y, LH, WRAP = 190, 24, 46

    wrapped = [_wrap(p.get("text", ""), WRAP) for p in panels]
    nlines = max(len(x) for x in wrapped)
    PH = (TEXT_Y - PY) + (nlines - 1) * LH + 22
    RULE_Y = PY + PH + 26
    H = RULE_Y + 34

    desc = _panels_desc(panels, colours, big_i, small_i, sizes, gap, fibre)
    out = [_svg_open(dict(fig, desc=desc), W, H)]
    for i, p in enumerate(panels):
        px = X0 + i * (PW + GAP_X)
        holds = (i == big_i)
        out.append(_rect(px, PY, PW, PH, rx=16, fill=_SVG_INSET,
                         stroke=_SVG_INK, w=2,
                         data_panel="held" if holds else "passes"))
        out.append(_mono(px + 22, PY + 30, p["label"], size=13,
                         spacing="0.06em", cls="ks3-pp-label"))

        # The particles, resting on the paper. The retained ones are drawn
        # nearly touching, because the text calls them one lump; the passing
        # ones are drawn apart, because the text calls them single particles.
        step_gap = 2 if holds else 10
        x = px + 24
        for pair in (p.get("dots") or []):
            colour_key, diameter = pair[0], float(pair[1])
            r = diameter / 2.0
            out.append(_circle(x + r, PAPER_TOP - r - 1, r,
                               fill=colours.get(colour_key, colour_key),
                               stroke=_SVG_INK, w=1.5, cls="ks3-pp-dot",
                               data_particle="held" if holds else "passes",
                               data_diameter="%g" % diameter))
            x += diameter + step_gap

        # The paper: two ink lines with a run of fibres between them, drawn
        # identically in both panels because it is the SAME paper.
        out.append(_line(px + 22, PAPER_TOP, px + 22 + INNER, PAPER_TOP,
                         stroke=_SVG_INK, w=2))
        out.append(_line(px + 22, PAPER_TOP + BH / 2.0,
                         px + 22 + INNER, PAPER_TOP + BH / 2.0,
                         stroke=_SVG_RULE_STRONG, w=BH - 4,
                         dash="%d %d" % (fibre, gap),
                         cls="ks3-pp-paper", data_gap=str(gap),
                         data_fibre=str(fibre)))
        out.append(_line(px + 22, PAPER_BOT, px + 22 + INNER, PAPER_BOT,
                         stroke=_SVG_INK, w=2))

        # Three particles drawn BELOW the paper on the passing side. Nothing
        # is drawn below it on the retained side, and that absence is the
        # argument.
        if not holds:
            # ⚠️ CENTRED ON THE GAPS, not merely below the band. The dash
            # pattern starts at the band's left edge, so the k-th gap runs
            # from `fibre + k(fibre + gap)` and its centre is half a gap
            # further on. A particle drawn under a FIBRE would be a particle
            # that went through the solid part of the paper, and the <desc>
            # says each one is sitting in a gap it passed through.
            for k, pair in enumerate((p.get("dots") or [])[:3]):
                colour_key, diameter = pair[0], float(pair[1])
                r = diameter / 2.0
                cx = px + 22 + fibre + gap / 2.0 + k * (fibre + gap)
                out.append(_circle(cx, PAPER_BOT + r + 7, r,
                                   fill=colours.get(colour_key, colour_key),
                                   stroke=_SVG_INK, w=1.5,
                                   cls="ks3-pp-dot ks3-pp-dot-through",
                                   data_particle="through",
                                   data_diameter="%g" % diameter))

        for j, line in enumerate(wrapped[i]):
            out.append(_label(px + 22, TEXT_Y + j * LH, line, size=17,
                              fill=_SVG_INK_BODY, weight="500",
                              anchor="start", cls="ks3-pp-text"))

    out.append(_line(0, RULE_Y, W, RULE_Y, stroke=_SVG_RULE_STRONG, w=2))
    out.append(_mono(X0, RULE_Y + 24,
                     "drawn to one scale · gaps %d units · %s "
                     "%g–%g · %s %g–%g"
                     % (gap, (panels[big_i].get("label") or "").lower(),
                        min(sizes[big_i]), max(sizes[big_i]),
                        (panels[small_i].get("label") or "").lower(),
                        min(sizes[small_i]), max(sizes[small_i])),
                     size=13, cls="ks3-pp-key"))
    out.append("</svg>")
    return "".join(out)


# ── registrations ────────────────────────────────────────────────────────
#
# Nine families and one drawer. The registry raises on a duplicate family
# across modules, on a family registered but never placed, and on a placement
# whose family nothing registers. If it refuses, it is right.
#
# ⚠️ EVERY ONE OF THE NINE TICKS A RAIL STOP, so every one carries
# `data-stage-done="0"`. `data-instrument` keeps `wirePredictions` out of the
# instrument's own options — every C3 instrument owns at least one commit
# control of its own, and three of them own a lettered prediction gate.

ART = {
    'particle-panels': _particle_panels,
}

KIND_SHELL = {
    'purity-sorter': ("ks3-psort-block",
                      ' data-instrument data-psortblock data-stage-done="0"'),
    'dissolve-lab': ("ks3-dlab-block",
                     ' data-instrument data-dlabblock data-stage-done="0"'),
    'sequence-rebuild': ("ks3-seq-block",
                         ' data-instrument data-seqblock data-stage-done="0"'),
    'crystal-bench': ("ks3-cryst-block",
                      ' data-instrument data-crystblock data-stage-done="0"'),
    'method-choice': ("ks3-mchoice-block",
                      ' data-instrument data-mchoiceblock '
                      'data-stage-done="0"'),
    'still-run': ("ks3-still-block",
                  ' data-instrument data-stillblock data-stage-done="0"'),
    'chroma-run': ("ks3-chroma-block",
                   ' data-instrument data-chromablock data-stage-done="0"'),
    'plan-critique': ("ks3-critique-block",
                      ' data-instrument data-critiqueblock '
                      'data-stage-done="0"'),
    'melting-point-bench': ("ks3-mpb-block",
                            ' data-instrument data-mpbblock '
                            'data-stage-done="0"'),
}

KIND_FN = {
    'purity-sorter': r_purity_sorter,
    'dissolve-lab': r_dissolve_lab,
    'sequence-rebuild': r_sequence_rebuild,
    'crystal-bench': r_crystal_bench,
    'method-choice': r_method_choice,
    'still-run': r_still_run,
    'chroma-run': r_chroma_run,
    'plan-critique': r_plan_critique,
    'melting-point-bench': r_melting_point_bench,
}
