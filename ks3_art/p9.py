"""ks3_art.p9 — P9 *Static electricity*, the unit where nothing is created.

Every instrument here is authored against Claude Design's delivered pages in
`docs/ks3/design-reference/p9/`. Her page wins outright: a shape that is not
in her drawing is not in this module, and where her NOTES and her drawing
disagree the DRAWING IS MEASURED and the note is reported in
`DEPARTURES-P9.md` beside the delivery.

── ⚖️ MRB-204 · NO FORMULA BLOCK IN THIS UNIT, AND NONE IS MISSING ───────

    p9-01  no block — see the ruling below. It REPORTS a charge and asks no
           arithmetic; `Q = n × e` needs the coulomb and the elementary
           charge, both GCSE, and `STAT.01` names neither.
    p9-02  no block — Coulomb's law is A level and `STAT.01b` is qualitative.
    p9-03  no block — field strength as force per unit charge is GCSE, and
           `STAT.02` says *the idea of* an electric field.

No worked example either. Design's own audit: *"P9 and P10 have no worked
examples, correctly: nothing in either unit is quantitative, and the rule is
not to invent a calculation to fill the block."*

── ⚖️ RULED 21 Aug 2026 (Mide) · THE CHARGE MODEL HAS A CEILING ─────────

A model that climbs forever teaches *rub harder, get more, without limit*.
Real charge plateaus: it leaks away and the air eventually breaks down.

⚠️ **HER NOTES AND HER PAGE DISAGREE, AND THE PAGE HAS IT RIGHT.** FLAG 8
of `NOTES-P8-P9.md` says *"`p9-01`'s charge model has no ceiling … the model
would keep climbing if the slider went further"*. Her `p9-01` page carries

    const STROKE_TAU  = 14;
    const STROKE_CEIL = 26.3;
    const strokeFactor = STROKE_CEIL * (1 - Math.exp(-rubs / STROKE_TAU));

and her legal line says *"the stroke term levels off towards a ceiling rather
than climbing without limit, because a real charge leaks away and because the
air eventually breaks down"*. Measured, ported exactly, and the ruling is
therefore satisfied by her own drawing — a *considered, not changed* row.

`r_transfer_pair` REFUSES a payload with no ceiling, so the ruling cannot be
lost by a later edit that only looks like tidying.

── ⚖️ RULED 21 Aug 2026 (Mide) · INDUCTION IN RELATIVE WORDS ONLY ────────

`p9-02`'s induced-attraction coefficient (her FLAG 9) is ACCEPTED, and the
effect is reported in relative words and never as a force in newtons —
nowhere on the page, in no tile, note, legal line or rung. Her page already
holds that line: the neutral-pair strength tile reads *"a small fraction of
the charged pair at this gap"* and prints no figure at all. The like/unlike
cases keep her RELATIVE scale, on which 100 is the closest fully charged pair
and which her legal line declares as a scale rather than a measurement.
`r_charge_pair` refuses a payload naming newtons anywhere in it.

── ⚠️ RESERVED PAYLOAD KEYS ───────────────────────────────────────────────

`r_activity` renders `cards`, `sim`, `fifa` and `scorecards` ITSELF, with no
opt-out. Nothing here uses any of the four — the band block's payloads are
`ladder`, `matrix` and `triple`.

── ⚠️ SHELL CLASSES ARE UNIQUE ACROSS THE WHOLE REGISTRY ─────────────────

`ks3_art.load()` asserts it since MRB-279. Checked before these were written,
and it mattered: `ks3-cpair-` — the obvious stem for a pair of charged
spheres — is already C4's `change-pairs`. This unit uses `ks3-chpair-`.

── ⚠️ `charge-think` IS A SHELL, NOT A DRAWING, AND HERE IS WHY ──────────

`p9-01` is the only lesson in the key stage whose rail includes `#s-think`.
Design's `DONE` says so — `if (id === 's-think') return s.gate !== null;` —
and MRB-205 makes her page the authority. `ks3_parity`'s own note records the
opposite as a fact about the corpus ("`#s-think` is on no rail on any page");
it was true of the first 137 lessons and it is not true of this one.

A rail anchor has to satisfy two gates that a plain `predict` confrontation
cannot:

  * `check_rail_reachable` wants a signal `doneByDom()` reads. A
    confrontation has no options, no reveal and no rungs.
  * `check_nothing_ticks_on_load` wants any `data-instrument` section that is
    a rail anchor to declare `data-stage-done="0"` **in the shipped bytes**,
    because the rail's first paint runs before the instruments wire.

`ks3_art/core.py`'s shared `confrontation` shell emits `data-instrument` and
NO declaration, so it fails the second gate — and that file is shared by ten
units, so widening it to suit one page is exactly the change `docs/ks3/
worktrees.md` §2 says to announce rather than make. So P9 registers its own
family for the one section that needs it.

`r_charge_think` draws NOTHING, deliberately, and that is not a hole:
`r_activity` renders a `misconception` BLOCK's whole body from its block type
(`r_confrontation`, both quotes and both bodies) before the kind's renderer is
reached, and sets `head_emitted_content` so the empty-activity gate is
satisfied by real content rather than bypassed. If this drawer ever returned
markup it would be markup Design did not draw, and it would land UNDER her
second quote.

`p9-02` and `p9-03` keep the ordinary `predict` kind, because their
`#s-think` is off the rail exactly as everywhere else in the key stage.

── ⚠️ BAND VALUES ─────────────────────────────────────────────────────────

Full words — `easier`, `standard`, `harder`. Never `s` or `h`.
"""

from ks3_art.kit import e, rich, t


# ═══ shared P9 primitives ════════════════════════════════════════════════

def _seg(cls, label, pressed=False, **attrs):
    bits = "".join(' %s="%s"' % (k.replace("_", "-"), e(str(v)))
                   for k, v in sorted(attrs.items()))
    return ('<button type="button" class="%s" aria-pressed="%s"%s>%s</button>'
            % (e(cls), "true" if pressed else "false", bits, t(label)))


def _gate(act_id, family, gate, hook):
    """The commit gate every P9 bench opens behind.

    All three of Design's benches are locked until a prediction is made, and
    on all three her `DONE` for the SYNTHESIS section beside the bench reads
    `s.gate !== null` — so the gate is not decoration, it is the thing that
    ticks two of the four rail stops.
    """
    if not gate.get("prompt") or len(gate.get("options") or []) < 3:
        raise ValueError(
            "%s %r has no commit gate. A bench read before a commitment "
            "confirms whatever the student already believed."
            % (family, act_id))
    opts = "".join(
        '<li><button type="button" class="ks3-option" data-%s-gopt="%d" '
        'aria-pressed="false"><span class="ks3-opt-mark" aria-hidden="true">'
        '%s</span><span class="ks3-opt-label">%s</span></button></li>'
        % (hook, i, chr(65 + i), t(o))
        for i, o in enumerate(gate["options"]))
    return ('<div class="ks3-%s-gate" data-%s-gate><p class="ks3-commit">%s'
            '</p><ul class="ks3-options">%s</ul></div>'
            % (hook, hook, t(gate["prompt"]), opts))


def _tiles(hook, specs):
    cells = ""
    for s in specs:
        sub = ('<p class="ks3-%s-tile-sub" data-%s-sub="%s">%s</p>'
               % (hook, hook, e(s["id"]), t(s.get("sub", "")))
               ) if s.get("sub") else ""
        cells += ('<div class="ks3-%s-tile">'
                  '<p class="ks3-%s-tile-label">%s</p>'
                  '<p class="ks3-%s-tile-value" data-%s-out="%s">%s</p>%s'
                  '</div>'
                  % (hook, hook, t(s["label"]), hook, hook, e(s["id"]),
                     t(s.get("value", "—")), sub))
    return '<div class="ks3-%s-tiles">%s</div>' % (hook, cells)


# ⚠️ THERE IS NO `_head` HERE, AND THAT IS A REPAIR RATHER THAN AN OMISSION.
#
# P4, P5 and P6 each define one — eyebrow, `<h2>` and a right-aligned progress
# line — and each of their benches calls it. So does `r_activity`'s own shell,
# from the SAME payload keys, whenever the block authors `progress` or
# `head_counter`: `<div class="ks3-blockhead"><div><p class="ks3-eyebrow">…
# </p><h2>…</h2></div>` plus `_progress_readout(pg)`. Both draw, so the block
# ships the eyebrow, the heading and the readout TWICE.
#
# ⚠️ IT IS ON A LIVE PAGE. `ks3/physics/waves-and-sound/sound-needs-a-medium
# .html` renders `<h2>Same bang. Change what is in the way.</h2>` twice, one
# line under the other, and so does every other P4/P5/P6 bench that authors a
# `progress`. Found by screenshotting this unit's first bench and reading it,
# which is the only way it can be found: every gate in the build counts
# elements or asserts they respond, and two correct head rows are two correct
# head rows.
#
# `_kinds_consuming` is why it escapes. It decides whether the SHELL should
# draw the readout by searching the drawer's own source for
# `a.get("progress")` — and in P4/P5/P6 that string is inside `_head`, a
# different function, so the search finds nothing and the shell draws one too.
# The mechanism is sound; a helper hid the read from it.
#
# So P9 does not have a `_head`. The shell owns the head row, which is what it
# was built for and what gives Design's layout for free — eyebrow and heading
# left, readout right — and the wiring drives the readout through the engine's
# own `setCountState`. Nothing is duplicated and there is ~30 lines less CSS.
#
# ⚠️ `progress` IS AUTHORED AS A MAP OF NAMED STATES, not as a string. A
# string routes to `_head_counter` as a COUNT FORMAT; the dict routes to
# `_progress_readout`, which is the shape these three benches actually have —
# two named states, no number in either.
#
# The P4/P5/P6 duplication is NOT fixed here. It is four units' worth of
# built pages and it belongs to whoever owns them; it is reported instead.


def _slider(act_id, hook, spec, key=""):
    k = key or "v"
    return ('<div class="ks3-%s-row"><div class="ks3-%s-rowhead">'
            '<label for="%s-%s">%s</label>'
            '<p class="ks3-%s-reading" data-%s-out="%s">%s</p></div>'
            '<input class="ks3-%s-slider" type="range" id="%s-%s" '
            'min="%s" max="%s" step="%s" value="%s" data-%s-slider="%s">'
            '</div>'
            % (hook, hook, e(act_id), e(k), t(spec["label"]),
               hook, hook, e(k), t(spec.get("value", "—")),
               hook, e(act_id), e(k), e(spec["min"]), e(spec["max"]),
               e(spec["step"]), e(spec["start"]), hook, e(k)))


def _sibling(a):
    """`data-sibling` — the section this bench ticks, at its own count.

    All three P9 benches have one, and on all three Design's own `DONE` gives
    the section beside the bench the GATE alone while the bench itself needs
    the gate AND a control touched:

        p9-01  #s-think  (the confrontation — the only one in the key stage)
        p9-02  #s-matrix (the nine-case table)
        p9-03  #s-reach  (the three-field figure)

    Same shape as P4's and P6's, and `mirrors` would be wrong twice: it would
    tick the stop LATE, and `ks3_rail_manifest` derives the mirror map from
    her `isDone()` — which returns two DIFFERENT expressions here — so a
    declared mirror fails `check_rail_matches_design` outright.
    """
    # ⚠️ A TYPO HERE SHIPS A DEAD RAIL STOP, IN SILENCE, AND IT DID IN P6.
    # `p6-08` and `p6-09` were authored with `sibling` / `sibling_at`, which
    # this function does not read, so nothing ever ticked `#s-chart` or
    # `#s-uses`. MRB-208's gate cannot catch it: a band section carries
    # `data-stage-done="0"`, which IS one of the signals `doneByDom()` looks
    # for, so the stop reads as reachable and simply never becomes true.
    for wrong in ("sibling", "sibling_at", "band", "mirror", "mirrors"):
        if wrong in a:
            raise ValueError(
                "%r carries %r. The keys this drawer reads are `band_anchor` "
                "and `band_at`, and a near-miss is silently ignored — which "
                "ships a rail stop that can never tick and that MRB-208's "
                "gate reads as reachable." % (a.get("id"), wrong))
    sib = a.get("band_anchor")
    if not sib:
        return ""
    at = a.get("band_at")
    if not isinstance(at, int) or at < 1:
        raise ValueError(
            "%r names a band sibling %r with no `band_at` count."
            % (a.get("id"), sib))
    return ' data-sibling="%s" data-sibling-at="%d"' % (e(sib), at)


def _unique(rows, act_id, family, what, key="id"):
    seen, dupes = set(), []
    for r in rows:
        rid = r.get(key)
        if rid in seen:
            dupes.append(rid)
        seen.add(rid)
    if dupes:
        raise ValueError(
            "%s %r has two %ss with %s %s. The second is unreachable and the "
            "failure is silent."
            % (family, act_id, what, key, sorted(set(dupes))))


def _branches(hook, a, need, act_id, family):
    """The per-state note AND the words that go beside it, as one seam.

    ⚖️ **A VERDICT WORD IS CONTENT AND LIVES IN THE LESSON RECORD.** P6 put
    its verdict strings in the wiring (`"Silence, at any distance"`,
    `"The blow arrives"`) and they work, but they are sentences a student
    reads, and a sentence a student reads that lives in `shared/ks3.js` is a
    sentence no content gate can see and no examiner can find. Every branch
    here carries its note and its readout words together, from the record.

    A branch may be a bare string — the note alone — or a dict carrying
    `note` plus any of `verdict`, `sub` and `dir`. Both shapes emit the same
    hidden `<span>`, so the wiring reads one thing.
    """
    spec = a.get("branches") or {}
    missing = [k for k in need
               if not (spec.get(k) or {} if isinstance(spec.get(k), dict)
                       else spec.get(k))]
    if missing:
        raise ValueError(
            "%s %r has no note for state(s) %s. Every reachable state has "
            "something true to say (5A.1), and a branch that renders nothing "
            "ships a bench with an empty note panel — the p5-01 defect."
            % (family, act_id, ", ".join(missing)))
    out = ""
    for k in need:
        v = spec[k]
        if isinstance(v, str):
            v = {"note": v}
        if not v.get("note"):
            raise ValueError("%s %r branch %r has no `note`."
                             % (family, act_id, k))
        bits = "".join(
            ' data-%s="%s"' % (name, e(v[name]))
            for name in ("note", "verdict", "sub", "sub_alt", "dir")
            if v.get(name))
        out += ('<span data-%s-branch="%s"%s hidden></span>'
                % (hook, e(k), bits))
    return out


def _words(hook, a, need, act_id, family):
    """The short readout strings — the ones that are not a whole sentence.

    Same argument as `_branches` and the same seam: `zero on this scale`,
    `feels no force`, `short of electrons` are all strings a student reads,
    so they are authored beside the physics rather than typed into the
    engine. Emitted as one hidden `<span>` per key.
    """
    spec = a.get("words") or {}
    missing = [k for k in need if not spec.get(k)]
    if missing:
        raise ValueError(
            "%s %r has no `words` entry for %s. These are strings a student "
            "READS; a missing one renders as an empty readout tile, which "
            "every gate in the build reads as a live instrument."
            % (family, act_id, ", ".join(missing)))
    extra = sorted(set(spec) - set(need))
    if extra:
        raise ValueError(
            "%s %r authors `words` %s, which nothing reads. An authored key "
            "no renderer looks at is what `ks3_key_audit` is for, and a "
            "string a student was meant to see and never does is worse than "
            "a missing one." % (family, act_id, ", ".join(extra)))
    return "".join(
        '<span data-%s-word="%s" data-text="%s" hidden></span>'
        % (hook, e(k), e(spec[k])) for k in need)


def _no_newtons(a, act_id, family):
    """⚖️ RULED — NO ABSOLUTE FORCE ANYWHERE ON `p9-02`.

    Walked over the whole payload rather than over a list of keys, because
    the ruling is about what a student READS and a newton figure can arrive
    in a tile label, a branch note, a caption or a readout sub equally well.
    `n` and `N` on their own are not searched for: they are the electron
    count's own letter and the start of half the words in the unit.
    """
    hits = []

    def walk(node, path):
        if isinstance(node, dict):
            for k, v in node.items():
                walk(v, "%s.%s" % (path, k))
        elif isinstance(node, (list, tuple)):
            for i, v in enumerate(node):
                walk(v, "%s[%d]" % (path, i))
        elif isinstance(node, str):
            low = node.lower()
            if "newton" in low or " n)" in low or " nn" in low:
                hits.append(path)

    walk(a, family)
    if hits:
        raise ValueError(
            "%s %r names a force in newtons at %s. Ruled 21 Aug 2026: the "
            "induced-attraction coefficient is CHOSEN rather than measured, "
            "so this bench reports strength in relative words and on its own "
            "declared scale, and no absolute force appears anywhere on the "
            "page." % (family, act_id, ", ".join(sorted(set(hits)))))


# ═══ p9-01 · #s-rub · two dry insulators, rubbed ═════════════════════════

def r_transfer_pair(a, act_id):
    """⊕ p9-01 `#s-rub` — pick the pair, count the rubs.

    ⚖️ **THE SAME-MATERIAL BRANCH IS REAL AND IT IS THE COMMIT GATE'S OWN
    ANSWER.** Design's drawing puts NOTHING in the gap when both hands hold
    the same material — no arrow, no dots, no signs — and her note for that
    state says in terms that rubbing on its own does nothing, that it takes
    two DIFFERENT materials. A bench that drew a faint transfer there would
    teach the opposite of the gate it opens behind. This drawer requires the
    branch, and the wiring paints it.

    ⚖️ **THE TWO CHARGES ARE EQUAL AND OPPOSITE AND THE FOURTH TILE SAYS SO
    IN NUMBERS.** `0.0 nC · nothing was created` is a constant, and it is
    constant on purpose: it is the one reading on the bench that never
    changes however hard a student rubs, which is the lesson.

    ⚖️ **THE SIGN ROWS ARE CAPPED AT SIX.** Design's `signs()` draws
    `Math.min(6, count)` marks, so the drawing says *more* without pretending
    to be a count — the electron figure in the tile is where the number
    lives. Six is her number and it is kept.

    ⚖️ **THE CHARGE HAS A CEILING** (Mide, 21 Aug 2026, and her own page).
    `nC = ceil × (1 − e^(−rubs / tau)) × per × steps × 1.602e−10`. A payload
    with no ceiling is refused here rather than allowed to drift back to a
    straight line: the ruling is about what a model TEACHES, and a model that
    climbs for ever teaches "rub harder, get more, without limit".

    ⚠️ **PROTONS ARE NAMED ON THE FACE OF THE DRAWING.** Her fixed caption
    `PROTONS DO NOT MOVE` sits under both blocks, because `CHRG-02` is
    exactly the belief that something positive was added.

    HOOKS: `data-xfer` (wrapper, `data-per`, `data-tau`, `data-ceil`) ·
    `data-xfer-gate` · `data-xfer-gopt` · `data-xfer-body` ·
    `data-xfer-mat` (carrying `data-side` and `data-rank`) ·
    `data-xfer-slider` · `data-xfer-signs` · `data-xfer-arrow` ·
    `data-xfer-dots` · `data-xfer-fill` · `data-xfer-out` · `data-xfer-note`.
    """
    mats = a.get("materials") or []
    if len(mats) != 7:
        raise ValueError(
            "transfer-pair %r declares %d material(s). Design's ladder is "
            "seven, from human hair down to PVC, and the count is the figure "
            "beside the bench as well as the deck in it — a shorter list "
            "would make the two disagree." % (act_id, len(mats)))
    _unique(mats, act_id, "transfer-pair", "material")
    for m in mats:
        for f in ("id", "label", "name"):
            if not m.get(f):
                raise ValueError(
                    "transfer-pair %r material %r has no %r. `label` is the "
                    "tab, `name` is the caption over the block."
                    % (act_id, m.get("id"), f))

    per = float(a.get("per") or 0)
    tau = float(a.get("stroke_tau") or 0)
    ceil = float(a.get("stroke_ceil") or 0)
    if per <= 0:
        raise ValueError(
            "transfer-pair %r has no `per` — the electrons that cross per "
            "step of the ladder per unit of stroke factor." % act_id)
    if tau <= 0 or ceil <= 0:
        raise ValueError(
            "transfer-pair %r has no charge ceiling (`stroke_ceil` / "
            "`stroke_tau`). RULED 21 Aug 2026: a model that climbs for ever "
            "teaches `rub harder, get more, without limit`, and real charge "
            "stops rising because it leaks away and because the air "
            "eventually breaks down. Design's own page carries the ceiling "
            "(26.3) and the time constant (14) even though her FLAG 8 says "
            "it does not — the drawing was measured." % act_id)

    rubs = a.get("rubs") or {}
    for k in ("min", "max", "step", "start", "label"):
        if k not in rubs:
            raise ValueError("transfer-pair %r rubs control has no %r."
                             % (act_id, k))

    # ⚠️ THE SAME-MATERIAL STATE IS NOT FILLER: it is the answer to the
    # bench's own commit gate, it is reachable at seven of the forty-nine
    # pairs, and the drawing goes deliberately empty there — so the note is
    # the only thing on screen that says what happened.
    branch_data = _branches("xfer", a,
                            ("same", "left_above", "left_below"),
                            act_id, "transfer-pair")
    word_data = _words("xfer", a,
                       ("unchanged", "short", "extra", "ceiling",
                        "ceiling_near"),
                       act_id, "transfer-pair")

    def tabs(side, start):
        return "".join(
            _seg("ks3-seg-btn ks3-xfer-mat", m["label"],
                 pressed=(i == int(start)),
                 data_xfer_mat=m["id"], data_side=side, data_rank=i,
                 data_name=m["name"], data_label=m["label"])
            for i, m in enumerate(mats))

    # Design's own 1000×400 viewBox. Two blocks, the gap between them, and
    # four fixed captions that never change — so they are literal `<text>`,
    # which is what MRB-254 asks for. Everything that varies is an
    # absolutely positioned HTML span over the wrapper.
    svg = (
        '<svg class="ks3-xfer-svg" viewBox="0 0 1000 400" role="img" '
        'aria-label="" data-xfer-alt>'
        '<rect class="ks3-xfer-block" x="110" y="110" width="270" '
        'height="170" rx="18"/>'
        '<rect class="ks3-xfer-block" x="620" y="110" width="270" '
        'height="170" rx="18"/>'
        '<path class="ks3-xfer-signs" data-xfer-signs="a" d="M0 0"/>'
        '<path class="ks3-xfer-signs" data-xfer-signs="b" d="M0 0"/>'
        '<path class="ks3-xfer-arrow" data-xfer-arrow d="M0 0"/>'
        '<path class="ks3-xfer-dots" data-xfer-dots d="M0 0"/>'
        '<text class="ks3-xfer-caption" x="500" y="160" '
        'text-anchor="middle">%s</text>'
        '<text class="ks3-xfer-caption" x="245" y="320" '
        'text-anchor="middle">%s</text>'
        '<text class="ks3-xfer-caption" x="755" y="320" '
        'text-anchor="middle">%s</text>'
        '<text class="ks3-xfer-caption" x="500" y="368" '
        'text-anchor="middle">%s</text></svg>'
        % (t(a.get("gap_label", "ELECTRONS")),
           t(a.get("left_label", "LEFT HAND")),
           t(a.get("right_label", "RIGHT HAND")),
           t(a.get("proton_label", "PROTONS DO NOT MOVE"))))

    fills = "".join(
        '<span class="ks3-xfer-fill ks3-xfer-%s" data-xfer-fill="%s"></span>'
        % (k, k) for k in ("aname", "bname", "acharge", "bcharge", "transfer"))

    lead = ('<p class="ks3-xfer-lead">%s</p>' % rich(a["lead"])
            if a.get("lead") else "")

    return ('<div class="ks3-xfer" data-xfer data-per="%s" data-tau="%s" '
            'data-ceil="%s" data-start-a="%s" data-start-b="%s"%s>%s%s'
            '<div class="ks3-xfer-body" data-xfer-body hidden>'
            '<div class="ks3-xfer-controls">'
            '<div class="ks3-xfer-picker">'
            '<p class="ks3-xfer-pickerlabel">%s</p>'
            '<div class="ks3-xfer-tabrow">%s</div></div>'
            '<div class="ks3-xfer-picker">'
            '<p class="ks3-xfer-pickerlabel">%s</p>'
            '<div class="ks3-xfer-tabrow">%s</div></div>%s</div>'
            '<div class="ks3-xfer-figwrap">%s%s</div>%s'
            '<p class="ks3-xfer-note" data-xfer-note></p>%s%s</div></div>'
            % (e(per), e(tau), e(ceil),
               e(a.get("start_a", 0)), e(a.get("start_b", 0)), _sibling(a),
               lead,
               _gate(act_id, "transfer-pair", a.get("gate") or {}, "xfer"),
               t(a.get("a_label", "In your left hand")), tabs("a", a.get("start_a", 0)),
               t(a.get("b_label", "In your right hand")), tabs("b", a.get("start_b", 0)),
               _slider(act_id, "xfer", rubs, "rubs"),
               svg, fills, _tiles("xfer", a.get("readouts") or []),
               branch_data, word_data))


# ═══ p9-02 · #s-spheres · two spheres on insulating stands ═══════════════

def r_charge_pair(a, act_id):
    """⊕ p9-02 `#s-spheres` — charge them, move them.

    ⚖️ **NINE STATES, AND THE ONE THAT DOES NOTHING IS ONE OF THEM.** Three
    charge states each over seventeen separations is 153 reachable states,
    and Design's four branches key them to what the PAIR does: nothing, repel,
    attract, attract weakly by induction. The both-neutral case is the only
    one of the nine that gives no force, and her figure's own lead says the
    usual summary of this topic mentions two.

    ⚖️ **INDUCED ATTRACTION IS REPORTED IN WORDS, NEVER IN NEWTONS** (Mide,
    21 Aug 2026). The strength tile's sub-line for a neutral pair is
    Design's own *"a small fraction of the charged pair at this gap"* — a
    comparison, with no figure in it, because the coefficient behind it is
    chosen rather than measured. `_no_newtons` walks the whole payload.

    ⚖️ **THE FORCE ON EACH SPHERE IS `equal and opposite`, WHATEVER THE
    PAIR.** A student who has understood everything else still expects the
    bigger charge to push harder, so it is a tile of its own rather than a
    clause in a note.

    ⚖️ **THE INDUCED SIGNS SIT ON THE NEAR AND FAR FACES AND THE TOTAL STAYS
    ZERO.** One `−` and one `+`, on the same neutral sphere, on the two faces
    — which is `CHRG-05` drawn rather than described: the paper is neutral
    the whole time.

    ⚠️ **THE STRENGTH WORD IS COMPUTED FROM THE VALUE, NEVER AUTHORED PER
    STATE.** Design's seven bands run from *no force at all* to *very
    strong*, and the equal state and the zero state both have to be true by
    construction — 5A.1's rule, and the reason a comparative label is never
    a second source for a fact the numbers already carry.

    HOOKS: `data-chpair` (wrapper, `data-k`, `data-ind-k`, `data-ref-d`) ·
    `data-chpair-gate` · `data-chpair-gopt` · `data-chpair-body` ·
    `data-chpair-state` (carrying `data-side`, `data-q`, `data-word`) ·
    `data-chpair-slider` · `data-chpair-sphere` · `data-chpair-sign` ·
    `data-chpair-ind` · `data-chpair-arrow` · `data-chpair-stand` ·
    `data-chpair-dim` · `data-chpair-fill` · `data-chpair-out` ·
    `data-chpair-note`.
    """
    _no_newtons(a, act_id, "charge-pair")

    states = a.get("states") or []
    if len(states) != 3:
        raise ValueError(
            "charge-pair %r declares %d state(s). The set is three — "
            "positive, neutral, negative — and the neutral one is the whole "
            "second half of the lesson." % (act_id, len(states)))
    _unique(states, act_id, "charge-pair", "state")
    if not any(int(s.get("q", 0)) == 0 for s in states):
        raise ValueError(
            "charge-pair %r has no neutral state in the deck. Induction is "
            "the case the lesson is named after, and it is unreachable "
            "without one." % act_id)
    for s in states:
        for f in ("id", "label", "word"):
            if not s.get(f):
                raise ValueError("charge-pair %r state %r has no %r."
                                 % (act_id, s.get("id"), f))

    k = float(a.get("k") or 0)
    ind_k = float(a.get("ind_k") or 0)
    ref_d = float(a.get("ref_d") or 0)
    if k <= 0 or ind_k <= 0 or ref_d <= 0:
        raise ValueError(
            "charge-pair %r needs `k`, `ind_k` and `ref_d`. The charged pair "
            "falls as `k × (ref_d ÷ d)²` — the real relationship — and the "
            "induced case as `ind_k × (ref_d ÷ d)⁴`, which is right in KIND "
            "(it falls faster) with a coefficient chosen to be readable. Her "
            "FLAG 9 says so and her legal line declares it." % act_id)
    if ind_k >= k:
        raise ValueError(
            "charge-pair %r gives induction a coefficient of %s against the "
            "charged pair's %s. The whole point of the case is that it is "
            "much weaker, and a bench that made it comparable would teach "
            "that a neutral object is as good as a charged one."
            % (act_id, ind_k, k))

    sep = a.get("sep") or {}
    for key in ("min", "max", "step", "start", "label"):
        if key not in sep:
            raise ValueError("charge-pair %r sep control has no %r."
                             % (act_id, key))

    bands = a.get("strength_bands") or []
    if len(bands) < 5:
        raise ValueError(
            "charge-pair %r declares %d strength band(s). Design's ladder is "
            "seven words from `no force at all` to `very strong`, and the "
            "word is the only channel the reading has — the tile prints no "
            "figure at all for the induced case." % (act_id, len(bands)))
    for b in bands:
        if "at_least" not in b or not b.get("word"):
            raise ValueError(
                "charge-pair %r strength band %r needs `at_least` and `word`."
                % (act_id, b))

    branch_data = _branches("chpair", a,
                            ("none", "repel", "attract", "induced"),
                            act_id, "charge-pair")
    word_data = _words("chpair", a,
                       ("zero_word", "zero_sub", "scale_sub", "pair",
                        "pair_none"),
                       act_id, "charge-pair")

    def tabs(side, start):
        return "".join(
            _seg("ks3-seg-btn ks3-chpair-state", s["label"],
                 pressed=(i == int(start)),
                 data_chpair_state=s["id"], data_side=side,
                 data_q=s.get("q", 0), data_word=s["word"],
                 data_label=s["label"])
            for i, s in enumerate(states))

    band_data = "".join(
        '<span data-chpair-band="%s" data-word="%s" hidden></span>'
        % (e(b["at_least"]), e(b["word"])) for b in bands)

    # Design's own 1000×400 viewBox: a bench line, two insulating stands,
    # two spheres whose centres are computed from the separation, the signs
    # inside them, the induced pair on a neutral sphere's two faces, the
    # force arrows and a dimension line under them.
    svg = (
        '<svg class="ks3-chpair-svg" viewBox="0 0 1000 400" role="img" '
        'aria-label="" data-chpair-alt>'
        '<path class="ks3-chpair-bench" d="M40 340 H960"/>'
        '<path class="ks3-chpair-stand" data-chpair-stand d="M0 0"/>'
        '<circle class="ks3-chpair-sphere" data-chpair-sphere="a" cx="330" '
        'cy="180" r="48"/>'
        '<circle class="ks3-chpair-sphere" data-chpair-sphere="b" cx="670" '
        'cy="180" r="48"/>'
        '<path class="ks3-chpair-sign" data-chpair-sign="a" d="M0 0"/>'
        '<path class="ks3-chpair-sign" data-chpair-sign="b" d="M0 0"/>'
        '<path class="ks3-chpair-ind" data-chpair-ind d="M0 0"/>'
        '<path class="ks3-chpair-arrow" data-chpair-arrow d="M0 0"/>'
        '<path class="ks3-chpair-dim" data-chpair-dim d="M0 0"/>'
        '<text class="ks3-chpair-caption" x="500" y="384" '
        'text-anchor="middle">%s</text></svg>'
        % t(a.get("bench_label", "INSULATING STANDS ON A BENCH")))

    fills = "".join(
        '<span class="ks3-chpair-fill ks3-chpair-%s" '
        'data-chpair-fill="%s"></span>'
        % (key, key) for key in ("alabel", "blabel", "sep", "verdict"))

    lead = ('<p class="ks3-chpair-lead">%s</p>' % rich(a["lead"])
            if a.get("lead") else "")

    return ('<div class="ks3-chpair" data-chpair data-k="%s" data-ind-k="%s" '
            'data-ref-d="%s" data-start-a="%s" data-start-b="%s" '
            'data-induced-sub="%s"%s>%s%s'
            '<div class="ks3-chpair-body" data-chpair-body hidden>'
            '<div class="ks3-chpair-controls">'
            '<div class="ks3-chpair-picker">'
            '<p class="ks3-chpair-pickerlabel">%s</p>'
            '<div class="ks3-chpair-tabrow">%s</div></div>'
            '<div class="ks3-chpair-picker">'
            '<p class="ks3-chpair-pickerlabel">%s</p>'
            '<div class="ks3-chpair-tabrow">%s</div></div>%s</div>'
            '<div class="ks3-chpair-figwrap">%s%s</div>%s'
            '<p class="ks3-chpair-note" data-chpair-note></p>%s%s%s'
            '</div></div>'
            % (e(k), e(ind_k), e(ref_d),
               e(a.get("start_a", 0)), e(a.get("start_b", 0)),
               e(a.get("induced_sub", "")), _sibling(a),
               lead,
               _gate(act_id, "charge-pair", a.get("gate") or {}, "chpair"),
               t(a.get("a_label", "Left sphere")), tabs("a", a.get("start_a", 0)),
               t(a.get("b_label", "Right sphere")), tabs("b", a.get("start_b", 0)),
               _slider(act_id, "chpair", sep, "d"),
               svg, fills, _tiles("chpair", a.get("readouts") or []),
               branch_data, band_data, word_data))


# ═══ p9-03 · #s-field · a field map and one test point ═══════════════════

def r_field_grid(a, act_id):
    """⊕ p9-03 `#s-field` — move the test point around.

    ⚖️ **THE WHOLE FIELD IS ONE PATH STRING.** Thirteen columns by seven rows
    is ninety-one sample points, each with a shaft and two head strokes, and
    Design's own note for the generator says it in terms: *no `<sc-for>`
    inside an `<svg>` anywhere; repeated marks are built as one path string*.
    The wiring composes it in `paint()`.

    ⚖️ **POINTS TOO CLOSE TO A CHARGE ARE LEFT BLANK, AND SO IS THE READING
    THERE.** The model treats a charge as a point, so within 62 units of one
    it gives no sensible value — and a bench that drew an enormous arrow
    there would teach a number the model cannot support. The tiles say *no
    value here* rather than printing one, and the note says why.

    ⚖️ **THE NULL POINT IS ITS OWN BRANCH AND IT IS REACHABLE.** Two equal
    positives at 350 and 650 put the exact mid-point at 500, which is step 12
    of the slider's 25 — so the state is not a limit the student approaches,
    it is a stop the slider lands on. Its note says the thing the whole rung
    turns on: *a point like this is not a place where the field is weak, it
    is a place where it cancels*. `r_field_grid` refuses an arrangement whose
    null point the slider cannot reach.

    ⚖️ **EVERY ARROW POINTS THE WAY A SMALL POSITIVE CHARGE WOULD BE PUSHED**
    and the drawing says so along its bottom edge, because the two tiles
    underneath — a small positive here, a small negative here — are the
    lesson's real discrimination and neither is legible without the
    convention.

    HOOKS: `data-fgrid` (wrapper, `data-eref`) · `data-fgrid-gate` ·
    `data-fgrid-gopt` · `data-fgrid-body` · `data-fgrid-setup` (carrying
    `data-charges`) · `data-fgrid-slider` · `data-fgrid-grid` ·
    `data-fgrid-charges` · `data-fgrid-signs` · `data-fgrid-test` ·
    `data-fgrid-point` · `data-fgrid-fill` · `data-fgrid-out` ·
    `data-fgrid-note`.
    """
    setups = a.get("setups") or []
    if len(setups) != 4:
        raise ValueError(
            "field-grid %r declares %d arrangement(s). Design's four are one "
            "positive, one negative, a dipole and two positives, and the "
            "fourth is the only one with a null point in it."
            % (act_id, len(setups)))
    _unique(setups, act_id, "field-grid", "arrangement")
    for s in setups:
        if not s.get("label") or not s.get("charges"):
            raise ValueError("field-grid %r arrangement %r is incomplete."
                             % (act_id, s.get("id")))
        for c in s["charges"]:
            if "x" not in c or "q" not in c:
                raise ValueError(
                    "field-grid %r arrangement %r has a charge with no x or q."
                    % (act_id, s.get("id")))

    pos = a.get("pos") or {}
    for key in ("min", "max", "step", "start", "label"):
        if key not in pos:
            raise ValueError("field-grid %r pos control has no %r."
                             % (act_id, key))

    x0 = float(a.get("x0", 80))
    dx = float(a.get("dx", 35))
    near = float(a.get("near", 62))

    # ⚠️ THE NULL POINT MUST BE A STOP THE SLIDER LANDS ON, NOT A LIMIT IT
    # APPROACHES. Two equal like charges have a null exactly between them,
    # and the whole of rung 2 and the commit gate are about that one state.
    # If the arithmetic ever moves — a different `x0`, a different step, a
    # charge nudged sideways — the state silently becomes unreachable and
    # the branch note becomes copy no student will ever read (5A.1).
    nulls = 0
    for s in setups:
        cs = s["charges"]
        if len(cs) == 2 and cs[0]["q"] == cs[1]["q"]:
            mid = (float(cs[0]["x"]) + float(cs[1]["x"])) / 2.0
            step = (mid - x0) / dx
            if abs(step - round(step)) < 1e-9 and \
                    float(pos["min"]) <= round(step) <= float(pos["max"]):
                nulls += 1
    if not nulls:
        raise ValueError(
            "field-grid %r has no reachable null point. Two equal like "
            "charges cancel exactly half-way between them, the commit gate "
            "asks about precisely that point and rung 2 turns on it — so the "
            "slider has to LAND there rather than pass either side of it."
            % act_id)

    # ⚠️ THE NULL POINT IS ITS OWN BRANCH BECAUSE IT IS NOT A WEAK FIELD, and
    # `on_charge` is its own because the model gives no value there at all.
    branch_data = _branches("fgrid", a,
                            ("on_charge", "single_positive",
                             "single_negative", "dipole", "two_positive",
                             "null_point"),
                            act_id, "field-grid")
    word_data = _words("fgrid", a,
                       ("no_value", "on_charge_dir", "zero_dir", "right",
                        "left", "no_force", "pushed", "scale", "zero_scale",
                        "zero_word", "close_word"),
                       act_id, "field-grid")

    bands = a.get("strength_bands") or []
    if len(bands) < 4:
        raise ValueError(
            "field-grid %r declares %d strength band(s); the verdict is a "
            "WORD, never a colour, and it needs a ladder to come off."
            % (act_id, len(bands)))
    for b in bands:
        if "at_least" not in b or not b.get("word"):
            raise ValueError(
                "field-grid %r strength band %r needs `at_least` and `word`."
                % (act_id, b))

    tabs = "".join(
        _seg("ks3-seg-btn ks3-fgrid-setup", s["label"],
             pressed=(i == int(a.get("start_setup", 0))),
             data_fgrid_setup=s["id"], data_label=s["label"],
             data_charges=" ".join("%s:%s" % (c["x"], c["q"])
                                   for c in s["charges"]))
        for i, s in enumerate(setups))

    band_data = "".join(
        '<span data-fgrid-band="%s" data-word="%s" hidden></span>'
        % (e(b["at_least"]), e(b["word"])) for b in bands)

    # Design's own 1000×500 viewBox. The centre line the test point runs
    # along is dashed and fixed; the grid, the charges, their signs and the
    # test arrow are all computed.
    svg = (
        '<svg class="ks3-fgrid-svg" viewBox="0 0 1000 500" role="img" '
        'aria-label="" data-fgrid-alt>'
        '<path class="ks3-fgrid-grid" data-fgrid-grid d="M0 0"/>'
        '<path class="ks3-fgrid-axis" d="M60 250 H940"/>'
        '<path class="ks3-fgrid-charges" data-fgrid-charges d="M0 0"/>'
        '<path class="ks3-fgrid-signs" data-fgrid-signs d="M0 0"/>'
        '<path class="ks3-fgrid-test" data-fgrid-test d="M0 0"/>'
        '<circle class="ks3-fgrid-point" data-fgrid-point cx="500" cy="250" '
        'r="13"/>'
        '<text class="ks3-fgrid-caption" x="500" y="484" '
        'text-anchor="middle">%s</text></svg>'
        % t(a.get("convention_label",
                  "EVERY ARROW POINTS THE WAY A SMALL POSITIVE CHARGE "
                  "WOULD BE PUSHED")))

    fills = ('<span class="ks3-fgrid-fill ks3-fgrid-reading" '
             'data-fgrid-fill="reading"></span>')

    lead = ('<p class="ks3-fgrid-lead">%s</p>' % rich(a["lead"])
            if a.get("lead") else "")

    return ('<div class="ks3-fgrid" data-fgrid data-eref="%s" data-x0="%s" '
            'data-dx="%s" data-near="%s" data-start-setup="%s"%s>%s%s'
            '<div class="ks3-fgrid-body" data-fgrid-body hidden>'
            '<div class="ks3-fgrid-controls">'
            '<div class="ks3-fgrid-picker">'
            '<p class="ks3-fgrid-pickerlabel">%s</p>'
            '<div class="ks3-fgrid-tabrow">%s</div></div>%s</div>'
            '<div class="ks3-fgrid-figwrap">%s%s</div>%s'
            '<p class="ks3-fgrid-note" data-fgrid-note></p>%s%s%s'
            '</div></div>'
            % (e(a.get("eref", 2.5e-4)), e(x0), e(dx), e(near),
               e(a.get("start_setup", 0)), _sibling(a),
               lead,
               _gate(act_id, "field-grid", a.get("gate") or {}, "fgrid"),
               t(a.get("setup_label", "What is making the field")), tabs,
               _slider(act_id, "fgrid", pos, "pos"),
               svg, fills, _tiles("fgrid", a.get("readouts") or []),
               branch_data, band_data, word_data))


# ═══ the fixed figures · the ladder, the matrix, the three fields ════════

def r_charge_band(a, act_id):
    """⊕ The fixed figure Design puts beside each of the three benches.

    ⚖️ **`ladder`, `matrix` and `triple` — NOT `cards`.** `cards` is claimed
    by `r_activity` itself with NO opt-out, so a payload using it gets two
    renderers and renders blank. The keys are deliberately different for that
    reason and no other.

    ⚖️ **TWO OF THE THREE ARE TICKED BY THE BENCH BESIDE THEM.** `#s-matrix`
    and `#s-reach` carry no control: they are the payoff of the instrument, in
    exactly MRB-249's sense, and each bench marks its own sibling at Design's
    own earlier threshold. `p9-01`'s ladder is the exception — Design puts it
    on NO rail stop at all, so it takes no anchor the rail names.

    Three shapes go through here and the payload decides which:
      `p9-01`  `ladder`  seven materials, numbered badges, a spanning arrow
      `p9-02`  `matrix`  the three-by-three of every charge combination
      `p9-03`  `triple`  gravitational, magnetic, electric, side by side

    ⚠️ **NOTHING HERE HOLDS A LIVE VALUE.** Every string is a constant at
    build time, which is why the labels are SVG `<text>` and not overlay
    spans — MRB-254 forbids a `<text>` that ships empty to be filled later,
    and none of these is.
    """
    lead = ('<p class="ks3-chband-lead">%s</p>' % rich(a["lead"])
            if a.get("lead") else "")
    close = ('<p class="ks3-chband-close">%s</p>' % rich(a["close"])
             if a.get("close") else "")

    body = ""
    if a.get("ladder"):
        body += _ladder(a["ladder"], act_id)
    if a.get("matrix"):
        body += _matrix(a["matrix"], act_id)
    if a.get("triple"):
        body += _triple(a["triple"], act_id)

    if not body:
        raise ValueError(
            "charge-band %r renders nothing — no ladder, matrix or triple. "
            "An empty band block is a section heading with a gap under it."
            % act_id)

    # ⚠️ NO EYEBROW AND NO HEADING HERE. `r_activity`'s shell has already
    # emitted both from the same two payload keys — the eyebrow always, the
    # `<h2>` whenever the block authors no head-row readout, which a fixed
    # figure never does. Drawing them again is the P4/P5/P6 duplication in a
    # second shape; see the long note where `_head` is not, above.
    return ('<div class="ks3-chband" data-chband>%s%s%s</div>'
            % (lead, body, close))


def _ladder(spec, act_id):
    """p9-01's triboelectric ladder — HTML cards, and one SVG arrow.

    ⚖️ **THE ARROW IS THE FIGURE'S ARGUMENT AND IT IS DRAWN, NOT WRITTEN.**
    Design puts *loses electrons* at the top and *gains electrons* at the
    bottom with a single arrow running the height of the list between them,
    so the direction of transfer is a property of the PICTURE. A caption
    saying "higher means positive" would be the same claim with nothing to
    check it against.

    ⚖️ **THE CARDS ARE HTML, NOT SVG.** Seven rows of a badge, a name and a
    note reflow on a phone; an SVG of the same thing scales its text down
    below the legible floor. Nothing in the figure varies, so there is no
    live-label question to answer either way.

    ⚠️ **THE HEDGES SURVIVE.** `most likely to end up positive`, `most likely
    to end up negative`, `middling — poor at either job`. Real triboelectric
    series disagree with each other and the legal line says so; a row that
    read "ends up positive" would promote a likely outcome to a certainty,
    which is the single thing Design's §8 says must not be tidied here.
    """
    rows = spec.get("rows") or []
    if len(rows) != 7:
        raise ValueError(
            "tribo-ladder %r draws %d row(s). Design's list is seven, and the "
            "bench's own deck is the same seven — a figure with a different "
            "count would contradict the instrument above it."
            % (act_id, len(rows)))
    _unique(rows, act_id, "tribo-ladder", "row", key="name")
    for r in rows:
        if not r.get("num") or not r.get("name"):
            raise ValueError("tribo-ladder %r row %r needs `num` and `name`."
                             % (act_id, r.get("name")))
    if not spec.get("top_label") or not spec.get("bottom_label"):
        raise ValueError(
            "tribo-ladder %r has no `top_label` / `bottom_label`. The arrow "
            "between them is what makes the ORDER mean something; without "
            "them the figure is a list of seven materials." % act_id)

    # ⚖️ THREE BADGE TONES, AND THEY ARE A CHANNEL RATHER THAN DECORATION.
    # Design paints the top three badges in the accent tint, the middling one
    # in the band, and the bottom three in the blue tint — so the SPLIT the
    # list is about is visible before a word is read. Every row still carries
    # its number and its name, and the two rows the tone is a claim about
    # carry that claim in words as well, so the hue is never the only channel.
    for r in rows:
        if r.get("tone") not in ("loses", "middle", "gains"):
            raise ValueError(
                "tribo-ladder %r row %r has tone %r. The three Design paints "
                "are `loses`, `middle` and `gains`, and the tone is what "
                "makes the split legible without reading."
                % (act_id, r.get("name"), r.get("tone")))
    tones = [r["tone"] for r in rows]
    if tones.count("middle") != 1:
        raise ValueError(
            "tribo-ladder %r has %d `middle` row(s). Exactly one material on "
            "this list is poor at either job, and it is the one the figure "
            "warns a teacher off." % (act_id, tones.count("middle")))

    items = ""
    for r in rows:
        tell = ('<span class="ks3-chband-tell">%s</span>' % t(r["tell"])
                if r.get("tell") else "")
        items += ('<li class="ks3-chband-rung is-%s">'
                  '<span class="ks3-chband-num" aria-hidden="true">%s</span>'
                  '<span class="ks3-chband-name">%s</span>%s</li>'
                  % (e(r["tone"]), t(r["num"]), t(r["name"]), tell))

    arrow = ('<svg class="ks3-chband-arrowsvg" width="24" height="120" '
             'viewBox="0 0 24 120" aria-hidden="true">'
             '<path class="ks3-chband-arrow" d="M12 4 V116 M12 116 L4 100 '
             'M12 116 L20 100"/></svg>')

    return ('<div class="ks3-chband-ladder">'
            '<div class="ks3-chband-axis">'
            '<span class="ks3-chband-axislabel">%s</span>%s'
            '<span class="ks3-chband-axislabel">%s</span></div>'
            '<ol class="ks3-chband-rungs">%s</ol></div>'
            % (t(spec["top_label"]), arrow, t(spec["bottom_label"]), items))


def _matrix(spec, act_id):
    """p9-02's nine-case table — three states each, every combination.

    ⚖️ **NINE CELLS, AND THE FIGURE EXISTS BECAUSE ONE OF THEM SURPRISES.**
    The usual summary of this topic has two rules; the table has three
    outcomes and four of its nine cells are the third one. `_matrix` refuses
    a payload that is not square, because a missing row is a missing case and
    the whole claim is that the set is complete.

    ⚠️ **THE VERDICT IN EACH CELL IS A WORD PLUS A REASON**, and the two
    strong outcomes are marked with `<strong>` exactly as Design draws them —
    the induced case is deliberately NOT emphasised, because it is the weak
    one and the emphasis is carrying that.
    """
    cols = spec.get("columns") or []
    rows = spec.get("rows") or []
    if len(cols) != 3 or len(rows) != 3:
        raise ValueError(
            "state-matrix %r is %d × %d. Two objects with three states each "
            "is nine cases, and the figure's own claim is that it lists every "
            "one." % (act_id, len(rows), len(cols)))
    for r in rows:
        if not r.get("head") or len(r.get("cells") or []) != 3:
            raise ValueError(
                "state-matrix %r row %r does not have three cells."
                % (act_id, r.get("head")))

    head = "".join('<th scope="col">%s</th>' % t(c) for c in cols)
    body = ""
    for r in rows:
        cells = "".join(
            '<td%s>%s</td>' % (' class="is-strong"' if c.get("strong") else "",
                               rich(c["text"]))
            for c in r["cells"])
        body += ('<tr><th scope="row">%s</th>%s</tr>' % (t(r["head"]), cells))

    return ('<div class="ks3-chband-tablewrap">'
            '<table class="ks3-chband-table">'
            '<thead><tr><th scope="col">%s</th>%s</tr></thead>'
            '<tbody>%s</tbody></table></div>'
            % (t(spec.get("corner", "Left / right")), head, body))


def _triple(spec, act_id):
    """p9-03's three fields — gravitational, magnetic, electric.

    ⚖️ **EACH CARD DRAWS THE SAME SHAPE: TWO BODIES, A DASHED GAP, AND A PAIR
    OF EQUAL OPPOSITE ARROWS.** That sameness IS the figure's argument — the
    electric field is not a special case, and three drawings that differed in
    layout would let a reader think it was. The bodies differ; nothing else
    does.

    ⚠️ **THE DASHED GAP IS THE POINT AND IT IS NEVER FILLED.** `CHRG-10` is
    *the air in the gap must be carrying the force*, and a card that drew
    something in the gap would be committing it.
    """
    cards = spec.get("cards") or []
    if len(cards) != 3:
        raise ValueError(
            "field-triple %r declares %d card(s). Design's figure is three — "
            "gravitational, magnetic, electric — and the claim is that they "
            "are the same shape, which two of them cannot make."
            % (act_id, len(cards)))
    for c in cards:
        for f in ("title", "kind", "body", "aria_label"):
            if not c.get(f):
                raise ValueError("field-triple %r card %r has no %r."
                                 % (act_id, c.get("title"), f))
        if c["kind"] not in ("gravity", "magnet", "charge"):
            raise ValueError(
                "field-triple %r card %r is kind %r; the three drawn are "
                "`gravity`, `magnet` and `charge`."
                % (act_id, c.get("title"), c["kind"]))

    def draw(kind, aria):
        # The shared half of every card: a dashed gap and two equal arrows
        # pointing into it. Design's own geometry, one viewBox for all three.
        arrows = ('<path class="ks3-chband-cardarrow" d="M98 24 H144 '
                  'M144 24 L132 16 M144 24 L132 32 M212 24 H166 '
                  'M166 24 L178 16 M166 24 L178 32"/>')
        if kind == "gravity":
            art = ('<circle class="ks3-chband-body" cx="56" cy="60" r="34"/>'
                   '<circle class="ks3-chband-body" cx="252" cy="60" r="16"/>'
                   '<path class="ks3-chband-gap" d="M96 60 H212"/>')
        elif kind == "magnet":
            art = ('<rect class="ks3-chband-body" x="22" y="38" width="74" '
                   'height="44" rx="6"/>'
                   '<rect class="ks3-chband-body" x="220" y="44" width="58" '
                   'height="32" rx="6"/>'
                   '<path class="ks3-chband-gap" d="M100 60 H214"/>')
        else:
            art = ('<circle class="ks3-chband-body" cx="56" cy="60" r="30"/>'
                   '<path class="ks3-chband-charge" d="M42 60 H70 M56 46 V74"/>'
                   '<circle class="ks3-chband-body" cx="248" cy="60" r="24"/>'
                   '<path class="ks3-chband-charge" d="M236 60 H260"/>'
                   '<path class="ks3-chband-gap" d="M90 60 H220"/>')
        return ('<svg class="ks3-chband-cardsvg" viewBox="0 0 300 120" '
                'role="img" aria-label="%s">%s%s</svg>'
                % (e(aria), art, arrows))

    cells = "".join(
        '<div class="ks3-chband-card">'
        '<p class="ks3-chband-cardtitle">%s</p>%s'
        '<p class="ks3-chband-cardbody">%s</p></div>'
        % (t(c["title"]), draw(c["kind"], c["aria_label"]), rich(c["body"]))
        for c in cards)
    return '<div class="ks3-chband-cards">%s</div>' % cells


# ═══ p9-01 · #s-think · the shell of a rail-bearing confrontation ════════

def r_charge_think(a, act_id):
    """⊕ `p9-01`'s `#s-think`. THE SHELL IS THE WHOLE COMPONENT.

    This renderer draws nothing, on purpose, and the reason is in the module
    docstring at length. Briefly: `p9-01` is the only lesson in the key stage
    whose rail includes `#s-think` — Design's `DONE` returns `s.gate !== null`
    for it — and a rail anchor has to declare `data-stage-done="0"` in the
    SHIPPED BYTES and carry a signal `doneByDom()` reads. The shared
    `confrontation` shell in `ks3_art/core.py` emits the marker without the
    declaration, and that file belongs to ten units.

    The block's content is already on the page when this is called:
    `r_activity` renders a `misconception` block's two quotes and two bodies
    from its BLOCK TYPE (`r_confrontation`), sets `head_emitted_content`, and
    only then reaches the kind's renderer. So the empty-activity gate is
    satisfied by real content rather than bypassed, and anything returned
    here would be markup Design did not draw, landing under her second quote.

    ⚠️ THE PAYLOAD IS STILL VALIDATED. A `charge-think` block with no
    `statements` would render the REGISTER's paraphrase of the belief rather
    than the page's own wording — the `b1-01` defect exactly, and the one
    `r_confrontation`'s docstring says is dangerous because it renders
    something and therefore looks finished.
    """
    if len(a.get("statements") or []) < 2:
        raise ValueError(
            "charge-think %r declares %d statement(s). Design draws TWO wrong "
            "ideas in this block, the second behind her amber divider, and a "
            "block with none falls back to the register's paraphrase — which "
            "renders, and therefore looks finished."
            % (act_id, len(a.get("statements") or [])))
    if not a.get("band_target"):
        raise ValueError(
            "charge-think %r does not name the bench that ticks it via "
            "`band_target`. This section is a RAIL STOP on p9-01 and carries "
            "no control of its own: the transfer-pair bench marks it through "
            "`band_anchor` / `band_at`, and if that pairing is ever broken "
            "the stop can never tick." % act_id)
    return ""


# ═══ registration ════════════════════════════════════════════════════════
#
# ONE ROW PER RENDERER. Every family is P9's own — `ks3_art/core.py` and
# `ks3_art/kit.py` are untouched. Shell stems checked against the whole
# registry first, and one of them had to move: `ks3-cpair-` is C4's.

ART = {}

KIND_SHELL = {
    'transfer-pair':  ("ks3-xfer-block",
                       ' data-instrument data-xferblock '
                       'data-stage-done="0"'),
    'charge-pair':    ("ks3-chpair-block",
                       ' data-instrument data-chpairblock '
                       'data-stage-done="0"'),
    'field-grid':     ("ks3-fgrid-block",
                       ' data-instrument data-fgridblock '
                       'data-stage-done="0"'),
    'charge-band':    ("ks3-chband-block",
                       ' data-instrument data-chbandblock '
                       'data-stage-done="0"'),
    # ⚠️ SHELL ONLY. See `r_charge_think`. The declaration is the component.
    'charge-think':   ("ks3-chthink",
                       ' data-instrument data-chthink '
                       'data-stage-done="0"'),
}

KIND_FN = {
    'transfer-pair':  r_transfer_pair,
    'charge-pair':    r_charge_pair,
    'field-grid':     r_field_grid,
    'charge-band':    r_charge_band,
    'charge-think':   r_charge_think,
}
