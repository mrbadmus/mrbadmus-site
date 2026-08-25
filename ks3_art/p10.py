"""ks3_art.p10 — P10 *Magnetism and electromagnetism*, five lessons.

Every instrument here is authored against Claude Design's delivered pages in
`docs/ks3/design-reference/p10/`. Her page wins outright: a shape that is not
in her drawing is not in this module, and where her NOTES and her drawing
disagree the DRAWING IS MEASURED and the note is reported in
`DEPARTURES-P10.md` beside the delivery.

── ⚖️ MRB-204 · NO FORMULA BLOCK IN THIS UNIT, AND NONE IS MISSING ───────

Design's §2, ruled: *"KS3 magnetism names no quantity with a unit that a
student can calculate. Field strength in tesla is GCSE; `F = BIL` is GCSE; the
turns-and-current relationship in `p10-04` is a genuine product but has no
named quantity and no unit at this stage, so writing it as a formula would
mean inventing notation to fill the badges."* Her own audit adds that *"P9 and
P10 have no worked examples, correctly"*. No block, no CFIFA, no triangle.

── ⚖️ RELATIVE SCALES, AND EVERY ONE NAMES ITS REFERENCE ────────────────

Her §9 ruling 2. **No tesla and no newton appears anywhere in this unit** —
not in a tile, a note, a legal line, a rung or the bank. Every figure a
student can read is either a real angle in degrees, a real current in amps, a
count of paper clips, or a RELATIVE figure whose readout says what 100 is.
`_no_units` walks each bench's whole payload and refuses one that names either
unit, so the ruling cannot be lost to a later edit that only looks like
tidying.

── ⚠️ THE FIVE BENCHES, AND THE STATES EACH ONE HAS ──────────────────────

Measured by enumerating each of her `renderVals()` models in full rather than
by reading her §4 table, and the two agree exactly:

    track-pair       5 × 5 objects × 6 gaps       150   nothing 102 · repel 12
                                                        attract 12 · induced 24
    compass-plot     4 layouts × 25 positions     100   on the metal 4
                                                        neutral point 1 · 95 readings
    dip-circle       9 lats × 3 objects × 2 mounts  54   magnet 18 · steel 4
                                                        flat 16 · tipped 15 · pole 1
    solenoid-bench   5 × 5 × 3 cores × 2 switch   150   off 75 · iron 25
                                                        air 25 · plastic 25
    motor-coil       2 × 2 × 2 × 4 currents        32   never 8 · keeps 12 · stops 12

⚠️ **THREE OF HER BRANCH PREDICATES DO NOT DIVIDE THE STATE SPACE THE WAY
THEIR OWN SENTENCES CLAIM, AND ALL THREE ARE CORRECTED HERE.** Each is a
`DEPARTURES-P10.md` row with the measurement in it:

  * `compass-plot`'s neutral point was `rel < 0.6` — a proxy for zero. It
    fires in **17 of 100 states** and exactly **one** of them is a neutral
    point; the other sixteen are ordinary weak-field spots, ten of them on the
    horseshoe, which has no neutral point at all. The note printed there says
    *"they cancel and the total is zero — not weak, zero"*, which is the exact
    distinction the lesson's own Going further turns on. Replaced by a
    CANCELLATION test — the vector sum against the sum of the individual pole
    magnitudes — which is zero at a true null and 0.30 at the nearest other
    state. A gap of two orders of magnitude with nothing in it.
  * `dip-circle`'s *"barely — it is sluggish"* is unreachable: `horizRel < 12`
    is true at no latitude on her list except the pole, which has its own
    branch. Her rung 4 is about precisely that state. Threshold moved to 40 so
    70° north reads it, which is the latitude the rung is written about.
  * `solenoid-bench` and `compass-plot` both print a relative figure to one
    decimal place, so nine of the solenoid's on-states print **`0.0`** for a
    field that is small and not zero — on a page whose own tile says *"zero,
    not merely small"*. Below 0.1 the figure now takes two decimals, which is
    `p10-01`'s own convention for its `< 1` band.

── ⚠️ RESERVED PAYLOAD KEYS ───────────────────────────────────────────────

`r_activity` renders `cards`, `sim`, `fifa` and `scorecards` ITSELF, with no
opt-out. Nothing here uses any of the four — the band block's payload keys are
`tiles`, `panels` and `close`.

── ⚠️ SHELL CLASSES ARE UNIQUE ACROSS THE WHOLE REGISTRY ─────────────────

`ks3_art.load()` asserts it since MRB-279, on the CLASS and not only on the
family name. All six stems here were checked against every module, every line
of `shared/ks3.js` and every rule in `shared/ks3.css` before they were
written, and all six were free.

── ⚠️ NO HEAD ROW IS DRAWN HERE ──────────────────────────────────────────

`r_activity`'s shell owns the eyebrow, the `<h2>` and the right-aligned
progress readout, from `eyebrow` / `heading` / `progress` on the activity. P4,
P5 and P6 each define a `_head` of their own AND author `progress`, so every
one of their benches ships its heading twice on a live page. P9 fixed that by
not having a `_head`; this module does the same. The readout is driven from
the wiring through the engine's own `setCountState`.

── ⚠️ BAND VALUES ─────────────────────────────────────────────────────────

Full words — `easier`, `standard`, `harder`. Never `s` or `h`.
"""

from ks3_art.kit import e, rich, t


# ═══ shared P10 primitives ═══════════════════════════════════════════════

def _seg(cls, label, pressed=False, **attrs):
    bits = "".join(' %s="%s"' % (k.replace("_", "-"), e(str(v)))
                   for k, v in sorted(attrs.items()))
    return ('<button type="button" class="%s" aria-pressed="%s"%s>%s</button>'
            % (e(cls), "true" if pressed else "false", bits, t(label)))


def _gate(act_id, family, gate, hook):
    """The commit gate every P10 bench opens behind.

    All five of Design's benches are locked until a prediction is made, and on
    all five her own `DONE` gives the SECTION BESIDE the bench `s.gate !==
    null` — so the gate is not decoration, it is what ticks two of the four
    rail stops.
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
    """Design's readout row: a label, a value, and sometimes a line under it."""
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


def _slider(act_id, hook, spec, key):
    return ('<div class="ks3-%s-row"><div class="ks3-%s-rowhead">'
            '<label for="%s-%s">%s</label>'
            '<p class="ks3-%s-reading" data-%s-out="%s">%s</p></div>'
            '<input class="ks3-%s-slider" type="range" id="%s-%s" '
            'min="%s" max="%s" step="%s" value="%s" data-%s-slider="%s">'
            '</div>'
            % (hook, hook, e(act_id), e(key), t(spec["label"]),
               hook, hook, e(key), t(spec.get("value", "—")),
               hook, e(act_id), e(key), e(spec["min"]), e(spec["max"]),
               e(spec["step"]), e(spec["start"]), hook, e(key)))


def _picker(hook, label, buttons):
    return ('<div class="ks3-%s-picker">'
            '<p class="ks3-%s-pickerlabel">%s</p>'
            '<div class="ks3-%s-tabrow">%s</div></div>'
            % (hook, hook, t(label), hook, buttons))


def _sibling(a):
    """`data-sibling` — the section this bench ticks, at its own count.

    All five P10 benches have one, and on all five Design's `DONE` gives the
    section beside the bench the GATE alone while the bench itself needs the
    gate AND a control touched:

        p10-01  #s-proof   the three outcomes
        p10-02  #s-rules   the four rules
        p10-03  #s-earth   the three norths
        p10-04  #s-uses    the four jobs
        p10-05  #s-parts   the four parts

    Same shape as P4's, P6's and P9's. `mirrors` would be wrong twice over: it
    would tick the stop LATE, and `ks3_rail_manifest` derives the mirror map
    from her `isDone()` — which returns two DIFFERENT expressions here — so a
    declared mirror fails `check_rail_matches_design` outright. The manifest
    records `—` in the mirrors column for all five rows.
    """
    # ⚠️ A TYPO HERE SHIPS A DEAD RAIL STOP, IN SILENCE, AND IT DID IN P6.
    # `p6-08` and `p6-09` were authored with `sibling` / `sibling_at`, which
    # nothing reads, so `#s-chart` and `#s-uses` never ticked. MRB-208's gate
    # cannot catch it: a band section carries `data-stage-done="0"`, which IS
    # one of the signals `doneByDom()` looks for, so the stop reads as
    # reachable and simply never becomes true.
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
    """The per-state note AND the readout words that go beside it, as one seam.

    ⚖️ **A VERDICT WORD IS CONTENT AND LIVES IN THE LESSON RECORD.** P6 put its
    verdict strings in the wiring and they work, but they are sentences a
    student reads, and a sentence a student reads that lives in
    `shared/ks3.js` is a sentence no content gate can see and no examiner can
    find. Every branch here carries its note and its readout words together,
    from the record.

    A branch may be a bare string — the note alone — or a dict carrying `note`
    plus any of `verdict`, `sub`, `proof`, `nav` and `keep`. Both shapes emit
    the same hidden `<span>`, so the wiring reads one thing.

    ⚠️ EVERY NAMED STATE MUST BE PRESENT. A branch that renders nothing ships a
    bench with an empty note panel in a state a student can reach (5A.1), and
    every gate in the build reads an empty panel as a live instrument.
    """
    spec = a.get("branches") or {}
    missing = [k for k in need
               if not (spec.get(k) or {} if isinstance(spec.get(k), dict)
                       else spec.get(k))]
    if missing:
        raise ValueError(
            "%s %r has no note for state(s) %s. Every reachable state has "
            "something true to say (5A.1), and a branch that renders nothing "
            "ships a bench with an empty note panel."
            % (family, act_id, ", ".join(missing)))
    extra = sorted(set(spec) - set(need))
    if extra:
        raise ValueError(
            "%s %r authors branch(es) %s, which nothing reaches. A branch that "
            "cannot be reached is authored copy no student will ever read "
            "(5A.1)." % (family, act_id, ", ".join(extra)))
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
            for name in ("note", "verdict", "sub", "proof", "nav", "keep",
                         "spin", "core", "crowd", "turn")
            if v.get(name))
        out += ('<span data-%s-branch="%s"%s hidden></span>'
                % (hook, e(k), bits))
    return out


def _words(hook, a, need, act_id, family):
    """The short readout strings — the ones that are not a whole sentence.

    Same argument as `_branches` and the same seam: `no reading here`, `the
    compass is on the metal`, `not a pole — there is no field` are all strings
    a student READS, so they are authored beside the physics rather than typed
    into the engine. Emitted as one hidden `<span>` per key.
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
            "%s %r authors `words` %s, which nothing reads. An authored key no "
            "renderer looks at is what `ks3_key_audit` is for, and a string a "
            "student was meant to see and never does is worse than a missing "
            "one." % (family, act_id, ", ".join(extra)))
    return "".join(
        '<span data-%s-word="%s" data-text="%s" hidden></span>'
        % (hook, e(k), e(spec[k])) for k in need)


def _bands(hook, rows, act_id, family, what, minimum=4):
    """A ladder of thresholds and the WORD each one carries.

    ⚠️ A COMPARATIVE LABEL IS COMPUTED FROM THE VALUE, NEVER AUTHORED BESIDE
    IT (5A.1). That is what makes it true in the equal state and the zero
    state by construction rather than by somebody remembering — and both of
    those states are reachable on four of these five benches.
    """
    if len(rows) < minimum:
        raise ValueError(
            "%s %r declares %d %s band(s); a verdict is a WORD, never a "
            "colour, and it needs a ladder to come off."
            % (family, act_id, len(rows), what))
    for b in rows:
        if "at_least" not in b or not b.get("word"):
            raise ValueError("%s %r %s band %r needs `at_least` and `word`."
                             % (family, act_id, what, b))
    return "".join(
        '<span data-%s-%sband="%s" data-word="%s" hidden></span>'
        % (hook, what, e(b["at_least"]), e(b["word"])) for b in rows)


def _no_units(a, act_id, family):
    """⚖️ RULED (Design §9.2, applied) — NO TESLA AND NO NEWTON IN P10.

    Walked over the whole payload rather than over a list of keys, because the
    ruling is about what a student READS and an invented unit can arrive in a
    tile label, a branch note, a caption or a readout sub equally well.

    ⚠️ `T` and `N` on their own are NOT searched for: `N` is the north pole's
    own letter and it is on the face of three of these five drawings, and `T`
    opens a third of the sentences in the unit. The search is for the words.
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
            for bad in ("tesla", "newton", " nm", "n/kg"):
                if bad in low:
                    hits.append("%s (%r)" % (path, bad.strip()))

    walk(a, family)
    if hits:
        raise ValueError(
            "%s %r names an invented unit at %s. RULED: KS3 magnetism names "
            "no quantity a student can calculate, so every figure on these "
            "benches is a real angle, a real current, a count, or a RELATIVE "
            "figure whose readout says what 100 is. A tesla or a newton here "
            "would be invented rather than measured."
            % (family, act_id, ", ".join(sorted(set(hits)))))


def _wrap(hook, act_id, a, attrs, controls, svg, fills, tiles, extras):
    """Design's bench shell: lead, gate, then the body the gate opens.

    ⚠️ THE FIGURE HAS TWO NESTED DIVS AND BOTH ARE LOAD-BEARING. The outer one
    is the padded, rounded panel; the INNER one is bare, and it is what the
    overlay spans are positioned against. Every live label on these five
    benches is placed at a percentage read straight off the SVG's viewBox, so
    the box those percentages resolve against has to BE the SVG's box. Hang
    them off the padded panel instead and every one of them is displaced by
    `36f − 18` px — nothing at the centre, eighteen pixels at either edge, and
    always outwards. It is Design's own structure, and it is why she has an
    inner `position: relative` div that does nothing else.
    """
    lead = ('<p class="ks3-%s-lead">%s</p>' % (hook, rich(a["lead"]))
            if a.get("lead") else "")
    attr_s = "".join(' %s="%s"' % (k, e(v)) for k, v in attrs)
    return ('<div class="ks3-%s" data-%s%s%s>%s%s'
            '<div class="ks3-%s-body" data-%s-body hidden>'
            '<div class="ks3-%s-controls">%s</div>'
            '<div class="ks3-%s-figwrap"><div class="ks3-%s-fig">%s%s'
            '</div></div>%s'
            '<p class="ks3-%s-note" data-%s-note></p>%s</div></div>'
            % (hook, hook, attr_s, _sibling(a), lead,
               _gate(act_id, hook, a.get("gate") or {}, hook),
               hook, hook, hook, controls, hook, hook, svg, fills, tiles,
               hook, hook, extras))


# ═══ p10-01 · #s-bench · two objects on a low-friction track ═════════════

def r_track_pair(a, act_id):
    """⊕ p10-01 `#s-bench` — put two things end to end.

    ⚖️ **THE NOTHING BRANCH IS 102 OF THE 150 STATES AND IT IS THE LESSON.**
    Two thirds of what a student can build on this bench does nothing at all,
    and that is not filler: `MAG-01` is *all metals are magnetic*, and the only
    way to break it is to put a magnet next to aluminium and watch the arrows
    stay away. Design gives the state three different sentences — neither
    object magnetic, both steel, or one of them inert — and all three are
    required here.

    ⚖️ **REPULSION IS THE ONLY PROOF, AND THE FOURTH TILE SAYS SO IN EVERY
    STATE.** *Does this prove both are magnets* reads `yes — repulsion proves
    it` on 12 of the 150 states and one of three different `no`s on the other
    138. That tile is the whole CONTRAST this lesson is classified as.

    ⚖️ **THE PULL ON STEEL IS REPORTED IN WORDS AND NEVER AS A FIGURE.** Her
    §8: how strongly a piece of steel magnetises depends on its shape, its
    carbon content and its history, so any coefficient here would be a guess.
    The strength tile prints `reported in words, not on the scale` for all 24
    magnet-and-steel states — the same discipline `p9-02` holds for induced
    attraction.

    ⚖️ **THE DRAWN GAP IS PROPORTIONAL TO THE GAP IN CENTIMETRES.** `gap_px`
    per cm, so 2 cm is 52 units and 12 cm is 312 — a factor of six, which is
    what the dimension line's own label claims. The force arrow's length runs
    with the square root of the relative strength, clamped at both ends, and
    the legal line says the clamp is there.

    ⚠️ **A NON-MAGNETIC OBJECT IS DRAWN WITH A DASHED OUTLINE**, so identity is
    never carried by hue alone — and the object's own name is printed under it
    either way.

    HOOKS: `data-tpair` (wrapper, `data-k`, `data-refgap`, `data-gappx`) ·
    `data-tpair-gate` · `data-tpair-gopt` · `data-tpair-body` ·
    `data-tpair-obj` (carrying `data-side`, `data-rank`, `data-kind`,
    `data-near`, `data-far`, `data-short`, `data-word`) · `data-tpair-slider` ·
    `data-tpair-abody` / `-bbody` · `data-tpair-apole` / `-bpole` ·
    `data-tpair-arrow` · `data-tpair-dim` · `data-tpair-fill` ·
    `data-tpair-out` · `data-tpair-note`.
    """
    _no_units(a, act_id, "track-pair")

    objs = a.get("objects") or []
    if len(objs) != 5:
        raise ValueError(
            "track-pair %r declares %d object(s). Design's drawer is five — "
            "a magnet either way round, an unmagnetised steel bar, aluminium "
            "and wood — and the count is load-bearing: drop the second magnet "
            "orientation and repulsion becomes unreachable, drop either "
            "non-magnetic object and `all metals are magnetic` has nothing to "
            "break it on." % (act_id, len(objs)))
    _unique(objs, act_id, "track-pair", "object")
    kinds = [o.get("kind") for o in objs]
    for want, why in (("mag", "there would be nothing magnetic on the bench"),
                      ("ferro", "the magnetise-the-steel case is the whole "
                                "reason attraction proves nothing"),
                      ("non", "nothing would show that a metal can ignore a "
                              "magnet completely")):
        if want not in kinds:
            raise ValueError(
                "track-pair %r has no %r object in the drawer, so %s."
                % (act_id, want, why))
    if kinds.count("mag") != 2:
        raise ValueError(
            "track-pair %r offers %d magnet(s). Design offers the SAME magnet "
            "twice, once each way round, because turning one round is the "
            "hook's whole question and a single entry would make repulsion "
            "unreachable." % (act_id, kinds.count("mag")))
    for o in objs:
        for f in ("id", "label", "short", "word"):
            if not o.get(f):
                raise ValueError(
                    "track-pair %r object %r has no %r. `label` is the tab, "
                    "`short` is the caption under the block, `word` is the "
                    "phrase the note and the aria label read."
                    % (act_id, o.get("id"), f))
        if o["kind"] == "mag" and not (o.get("near") and o.get("far")):
            raise ValueError(
                "track-pair %r magnet %r does not name the pole facing the "
                "gap. Which pole faces which is the only thing that changes "
                "between attract and repel." % (act_id, o.get("id")))

    gaps = a.get("gaps") or []
    if len(gaps) < 4 or sorted(gaps) != list(gaps):
        raise ValueError(
            "track-pair %r needs an ascending list of gaps; Design's six run "
            "2 cm to 12 cm, a factor of six, which is what makes the fourth "
            "power visible at all." % act_id)
    k = float(a.get("k") or 0)
    ref = float(a.get("ref_gap") or 0)
    gpx = float(a.get("gap_px") or 0)
    if k <= 0 or ref <= 0 or gpx <= 0:
        raise ValueError(
            "track-pair %r needs `k`, `ref_gap` and `gap_px`. Two bar magnets "
            "end to end fall as `k × (ref_gap ÷ d)⁴`, which is about right "
            "for this arrangement and is NOT the inverse square that applies "
            "to charges; `gap_px` is what makes the drawn gap proportional to "
            "the gap the label claims." % act_id)
    if float(gaps[0]) != ref:
        raise ValueError(
            "track-pair %r sets its reference at %s cm but its closest gap is "
            "%s cm. The readout says 100 is the closest pair of magnets, so "
            "the closest setting has to BE 100 — otherwise the top of the "
            "scale is a place the student cannot go, which is the defect "
            "measured on `p10-02`." % (act_id, ref, gaps[0]))

    ctl = a.get("gap_control") or {}
    for key in ("min", "max", "step", "start", "label"):
        if key not in ctl:
            raise ValueError("track-pair %r gap control has no %r."
                             % (act_id, key))
    if int(ctl["max"]) != len(gaps) - 1:
        raise ValueError(
            "track-pair %r has %d gaps and a slider that runs to %s. A "
            "setting the slider cannot reach is authored copy no student will "
            "read." % (act_id, len(gaps), ctl["max"]))

    band_data = _bands("tpair", a.get("strength_bands") or [], act_id,
                       "track-pair", "s")
    branch_data = _branches("tpair", a,
                            ("nothing_neither", "nothing_steel",
                             "nothing_inert", "repel", "attract", "induced"),
                            act_id, "track-pair")
    word_data = _words("tpair", a,
                       ("north", "south", "left", "right",
                        "nothing_word", "nothing_sub",
                        "steel_word", "steel_sub", "scale_sub"),
                       act_id, "track-pair")

    def tabs(side, start):
        return "".join(
            _seg("ks3-seg-btn ks3-tpair-obj", o["label"],
                 pressed=(i == int(start)),
                 data_tpair_obj=o["id"], data_side=side, data_rank=i,
                 data_kind=o["kind"], data_near=o.get("near", ""),
                 data_far=o.get("far", ""), data_short=o["short"],
                 data_word=o["word"], data_label=o["label"])
            for i, o in enumerate(objs))

    # Design's own 1000×400 viewBox: the track, two bodies whose x positions
    # are computed from the gap, the near-pole fill on a magnet, the force
    # arrows and a dimension line under them. One fixed caption, which never
    # changes and is therefore a literal `<text>` (MRB-254).
    svg = (
        '<svg class="ks3-tpair-svg" viewBox="0 0 1000 400" role="img" '
        'aria-label="" data-tpair-alt>'
        '<path class="ks3-tpair-track" d="M40 300 H960"/>'
        '<path class="ks3-tpair-body" data-tpair-abody d="M0 0"/>'
        '<path class="ks3-tpair-body" data-tpair-bbody d="M0 0"/>'
        '<path class="ks3-tpair-pole" data-tpair-apole d="M0 0"/>'
        '<path class="ks3-tpair-pole" data-tpair-bpole d="M0 0"/>'
        '<path class="ks3-tpair-arrow" data-tpair-arrow d="M0 0"/>'
        '<path class="ks3-tpair-dim" data-tpair-dim d="M0 0"/>'
        '<text class="ks3-tpair-caption" x="500" y="392" '
        'text-anchor="middle">%s</text></svg>'
        % t(a.get("track_label", "FREE TO SLIDE EITHER WAY")))

    fills = "".join(
        '<span class="ks3-tpair-fill ks3-tpair-%s" data-tpair-fill="%s">'
        '</span>' % (key, key)
        for key in ("aname", "bname", "anear", "afar", "bnear", "bfar", "gap"))

    controls = (_picker("tpair", a.get("a_label", "On the left"),
                        tabs("a", a.get("start_a", 0)))
                + _picker("tpair", a.get("b_label", "On the right"),
                          tabs("b", a.get("start_b", 0)))
                + _slider(act_id, "tpair", ctl, "d"))

    return _wrap("tpair", act_id, a,
                 [("data-k", k), ("data-refgap", ref), ("data-gappx", gpx),
                  ("data-gaps", " ".join(str(g) for g in gaps)),
                  ("data-start-a", a.get("start_a", 0)),
                  ("data-start-b", a.get("start_b", 0))],
                 controls, svg, fills, _tiles("tpair", a.get("readouts") or []),
                 band_data + branch_data + word_data)


# ═══ p10-02 · #s-bench · a plotting compass on a field map ═══════════════

def r_compass_plot(a, act_id):
    """⊕ p10-02 `#s-bench` — put the compass down and read it.

    ⚖️ **THE WHOLE FIELD IS ONE PATH STRING.** Thirteen columns by seven rows
    is ninety-one sample points, each with a shaft and two head strokes, and
    Design's own note for the generator says it in terms: *no `<sc-for>` inside
    an `<svg>` anywhere; repeated marks are built as one path string*. The
    wiring composes it in `paint()`.

    ⚖️ **EACH BAR MAGNET IS A PAIR OF POINT POLES.** That is the standard way
    of constructing a field map by hand and it gives the right shape
    everywhere except very close to the metal — which the legal line
    discloses, and which is why a sample inside a pole is dropped rather than
    drawn enormous.

    ⚖️ **THE NEUTRAL POINT IS A CANCELLATION, NOT A SMALL NUMBER.** Design
    tests `rel < 0.6`; measured over her own 100 states that fires 17 times
    and is a neutral point once. The test here is the vector sum against the
    sum of the individual pole magnitudes — 0.000 at the true null and 0.298
    at the next nearest state — so the note that says *"zero, not weak"* is
    only ever printed where the field is zero. `r_compass_plot` refuses an
    arrangement whose null point the button grid cannot land on, because the
    commit gate asks about precisely that spot and rung 4 turns on it.

    ⚖️ **100 IS A SPOT THE COMPASS CAN BE PUT ON.** Design's reference is the
    strongest point on the 13 × 7 LATTICE, which sits hard against a pole
    where no button can go: the highest reading a student could ever get on
    her scale is 18, `very strong` is unreachable, and 78 of the 96 readings
    fall in one band. The reference here is the strongest of the twenty-five
    reachable spots, which is what the readout says it is, and the four bands
    then run 20 / 24 / 27 / 24.

    ⚠️ **THE NEEDLE IS OMITTED AT THE NEUTRAL POINT AND ON THE METAL**, and the
    tiles say why in words in both cases. A needle drawn at a null would be a
    direction the model does not have.

    HOOKS: `data-cplot` (wrapper, `data-nullratio`) · `data-cplot-gate` ·
    `data-cplot-gopt` · `data-cplot-body` · `data-cplot-setup` (carrying
    `data-poles`, `data-bars`, `data-word`, `data-note`) · `data-cplot-spot` ·
    `data-cplot-grid` · `data-cplot-mag` · `data-cplot-north` ·
    `data-cplot-dial` · `data-cplot-needle` · `data-cplot-fill` ·
    `data-cplot-out` · `data-cplot-note`.
    """
    _no_units(a, act_id, "compass-plot")

    setups = a.get("setups") or []
    if len(setups) != 4:
        raise ValueError(
            "compass-plot %r declares %d arrangement(s). Design's four are one "
            "bar magnet, two unlike poles facing, two like poles facing and a "
            "horseshoe — and the third is the only one with a neutral point in "
            "it while the fourth is the only one that is nearly uniform."
            % (act_id, len(setups)))
    _unique(setups, act_id, "compass-plot", "arrangement")
    for s in setups:
        for f in ("id", "label", "word", "note"):
            if not s.get(f):
                raise ValueError(
                    "compass-plot %r arrangement %r has no %r. `note` is the "
                    "sentence in the middle of the reading note and it is "
                    "different for every layout — it is what makes the panel "
                    "say something about THIS map rather than about maps."
                    % (act_id, s.get("id"), f))
        if not s.get("poles") or not s.get("bars"):
            raise ValueError(
                "compass-plot %r arrangement %r has no `poles` or no `bars`. "
                "The poles are the model and the bars are the drawing; a "
                "layout with poles and no bar would put a field on the paper "
                "with nothing making it." % (act_id, s.get("id")))
        for p in s["poles"]:
            if "x" not in p or "y" not in p or "q" not in p:
                raise ValueError(
                    "compass-plot %r arrangement %r has a pole with no x, y "
                    "or q." % (act_id, s.get("id")))

    xs = a.get("spot_x") or []
    ys = a.get("spot_y") or []
    if len(xs) != 5 or len(ys) != 5:
        raise ValueError(
            "compass-plot %r offers a %d × %d grid of positions; Design's is "
            "five by five, and the centre of it is where the neutral point is."
            % (act_id, len(xs), len(ys)))

    ratio = float(a.get("null_ratio") or 0)
    if not 0 < ratio < 0.1:
        raise ValueError(
            "compass-plot %r sets `null_ratio` to %r. It is the fraction of "
            "the summed pole strengths that the VECTOR sum has to fall below "
            "before a spot counts as a neutral point, and it exists because a "
            "threshold on the reading alone cannot tell `cancels exactly` "
            "from `weak`. Measured on this payload the true null sits at 0.000 "
            "and the next nearest state at 0.298." % (act_id, a.get("null_ratio")))

    # ⚠️ THE NEUTRAL POINT MUST BE A SPOT A BUTTON LANDS ON, NOT A LIMIT THE
    # GRID APPROACHES. Two equal like poles facing each other cancel exactly
    # half-way between them; the commit gate asks about that spot by name and
    # rung 4 is written about it. If the arithmetic ever moves — a pole nudged
    # sideways, a different column — the state silently becomes unreachable
    # and its branch becomes copy no student will ever read (5A.1).
    def field_at(poles, px, py):
        fx = fy = scalar = 0.0
        for p in poles:
            dx, dy = px - float(p["x"]), py - float(p["y"])
            r2 = dx * dx + dy * dy
            if r2 < 100:
                return None
            r = r2 ** 0.5
            kk = float(p["q"]) / r2
            fx += kk * dx / r
            fy += kk * dy / r
            scalar += abs(kk)
        return (fx * fx + fy * fy) ** 0.5, scalar

    nulls = 0
    for s in setups:
        for px in xs:
            for py in ys:
                got = field_at(s["poles"], float(px), float(py))
                if got and got[1] > 0 and got[0] / got[1] < ratio:
                    nulls += 1
    if nulls != 1:
        raise ValueError(
            "compass-plot %r has %d reachable neutral point(s) across its "
            "hundred states. Exactly one is right: the commit gate asks what a "
            "compass does half-way between two north poles, and a bench where "
            "that spot is unreachable — or where four other spots claim to be "
            "one — teaches the opposite of the gate it opens behind."
            % (act_id, nulls))

    sband = _bands("cplot", a.get("strength_bands") or [], act_id,
                   "compass-plot", "s")
    cband = _bands("cplot", a.get("crowd_bands") or [], act_id,
                   "compass-plot", "c")
    branch_data = _branches("cplot", a,
                            ("on_magnet", "neutral", "reading"),
                            act_id, "compass-plot")
    word_data = _words("cplot", a,
                       ("no_reading", "on_metal", "no_direction", "is_zero",
                        "scale", "on_page", "compass_points"),
                       act_id, "compass-plot")

    tabs = "".join(
        _seg("ks3-seg-btn ks3-cplot-setup", s["label"],
             pressed=(i == int(a.get("start_setup", 0))),
             data_cplot_setup=s["id"], data_label=s["label"],
             data_word=s["word"], data_note=s["note"],
             data_poles=" ".join("%s:%s:%s" % (p["x"], p["y"], p["q"])
                                 for p in s["poles"]),
             data_bars=" ".join("%s:%s:%s:%s" % (b["x1"], b["x2"], b["y"],
                                                 b["left_pole"])
                                for b in s["bars"]))
        for i, s in enumerate(setups))

    spots = "".join(
        '<button type="button" class="ks3-cplot-spot" data-cplot-spot="%d:%d" '
        'aria-pressed="%s" aria-label="%s"></button>'
        % (ix, iy,
           "true" if (ix == int(a.get("start_x", 0))
                      and iy == int(a.get("start_y", 0))) else "false",
           e("Column %d, row %d" % (ix + 1, iy + 1)))
        for iy in range(len(ys)) for ix in range(len(xs)))

    svg = (
        '<svg class="ks3-cplot-svg" viewBox="0 0 1000 400" role="img" '
        'aria-label="" data-cplot-alt>'
        '<path class="ks3-cplot-grid" data-cplot-grid d="M0 0"/>'
        '<path class="ks3-cplot-mag" data-cplot-mag d="M0 0"/>'
        '<path class="ks3-cplot-north" data-cplot-north d="M0 0"/>'
        '<circle class="ks3-cplot-dial" data-cplot-dial cx="660" cy="128" '
        'r="30"/>'
        '<path class="ks3-cplot-needle" data-cplot-needle d="M0 0"/>'
        '</svg>')

    fills = "".join(
        '<span class="ks3-cplot-fill ks3-cplot-pole" data-cplot-fill="%s">'
        '</span>' % key for key in ("p0", "p1", "p2", "p3"))

    controls = (_picker("cplot", a.get("setup_label", "On the paper"), tabs)
                + '<div class="ks3-cplot-picker">'
                  '<p class="ks3-cplot-pickerlabel">%s</p>'
                  '<div class="ks3-cplot-grid-btns">%s</div></div>'
                  % (t(a.get("spot_label", "Where the compass goes")), spots))

    return _wrap("cplot", act_id, a,
                 [("data-nullratio", ratio),
                  ("data-spot-x", " ".join(str(v) for v in xs)),
                  ("data-spot-y", " ".join(str(v) for v in ys)),
                  ("data-start-setup", a.get("start_setup", 0)),
                  ("data-start-x", a.get("start_x", 0)),
                  ("data-start-y", a.get("start_y", 0))],
                 controls, svg, fills,
                 _tiles("cplot", a.get("readouts") or []),
                 sband + cband + branch_data + word_data)


# ═══ p10-03 · #s-bench · a compass free to tip, taken north ══════════════

def r_dip_circle(a, act_id):
    """⊕ p10-03 `#s-bench` — take the same compass somewhere else.

    ⚖️ **A CENTRED DIPOLE ALIGNED WITH THE SPIN AXIS** (her §9 ruling 3, and
    the standard first model). `tan(dip) = 2 tan(latitude)`, and the sideways
    part of the field goes as `cos(latitude)` — 100 at the equator and zero at
    the pole. The legal line names the eleven-degree tilt this leaves out and
    says dip measured in the field differs by several degrees in most places;
    her §8 makes that hedge load-bearing and it stays.

    ⚖️ **`CLAMPED FLAT` REPORTS ZERO DIP AND SAYS THE MOUNTING IS HOLDING IT.**
    That is the point of the control: the reading is a fact about the clamp
    and not about the field, and a bench that printed 0° without saying so
    would teach that the field is level everywhere.

    ⚠️ **EXCEPT AT THE EQUATOR, WHERE THE FIELD IS LEVEL AND THE SENTENCE
    WOULD BE FALSE.** Her flat note reads *"not because the field is level — at
    {place} the field itself is running into the ground at {dip}°"*, and at the
    equator it renders *"…running into the ground at 0°"* while denying that
    the field is level. Two reachable states, its own branch here.

    ⚖️ **THE NEEDLE IS CAPTURED BY WHAT IS ON THE BENCH, AND THAT IS NOT A
    FAULT.** A speaker magnet beats the whole Earth at a few centimetres; a
    steel clamp stand beats what is left of it above 70°. Both say so, and
    both keep the compass pointing at the bench rather than at the pole —
    which is why a compass is used away from loudspeakers and steel railings.

    ⚠️ **THE NAVIGABILITY VERDICT HAS A MIDDLE BAND AND IT IS REACHABLE.**
    Design's `horizRel < 12` is true at no latitude on her own list, so
    *"barely — it is sluggish"* is copy no student can reach — while her rung 4
    asks the student to explain exactly that state. The threshold is 40 here,
    which 70° north reaches at 34.2 and 52° north does not at 61.6.

    ⚖️ **THE DRAWN TILT IS THE DIP ANGLE.** Not a proxy for it, not a scaled
    version of it: the needle is rotated by the number the tile prints, and the
    arc beside it subtends the same angle.

    HOOKS: `data-dipc` (wrapper, `data-navat`) · `data-dipc-gate` ·
    `data-dipc-gopt` · `data-dipc-body` · `data-dipc-slider` ·
    `data-dipc-near` · `data-dipc-mount` · `data-dipc-needle` ·
    `data-dipc-arc` · `data-dipc-you` · `data-dipc-fill` · `data-dipc-out` ·
    `data-dipc-note`.
    """
    _no_units(a, act_id, "dip-circle")

    lats = a.get("lats") or []
    if len(lats) < 7:
        raise ValueError(
            "dip-circle %r offers %d latitude(s). Design's nine run from 60° "
            "south to the magnetic pole, and both ends are needed: the "
            "southern ones are where the needle tips the OTHER way, which is "
            "the half a British classroom never sees." % (act_id, len(lats)))
    # ⚠️ KEYED ON `deg`, NOT ON `id`. A latitude has no id — it IS its
    # number — and two entries at the same latitude would give the slider two
    # stops that read differently and behave identically.
    _unique(lats, act_id, "dip-circle", "latitude", key="deg")
    if not any(float(l["deg"]) == 0 for l in lats):
        raise ValueError(
            "dip-circle %r has no equator in the list. It is the state where "
            "dip is genuinely zero and the sideways pull is at its strongest, "
            "and it is the reference the whole scale is declared against."
            % act_id)
    if not any(float(l["deg"]) < 0 for l in lats):
        raise ValueError(
            "dip-circle %r offers no southern latitude. The north-seeking end "
            "tips DOWN in the north and UP in the south, and a bench that only "
            "went north would teach the tipping as a property of compasses "
            "rather than of where you are standing." % act_id)
    if not any(abs(float(l["deg"])) >= 89 for l in lats):
        raise ValueError(
            "dip-circle %r never reaches the magnetic pole. The commit gate "
            "asks what a compass does standing on it and rung 4 asks the "
            "student to explain it, so the state has to be reachable." % act_id)
    for l in lats:
        if "deg" not in l or not l.get("name"):
            raise ValueError("dip-circle %r latitude %r needs `deg` and "
                             "`name`." % (act_id, l))

    near = a.get("near") or []
    mounts = a.get("mounts") or []
    if len(near) != 3 or len(mounts) != 2:
        raise ValueError(
            "dip-circle %r offers %d bench object(s) and %d mounting(s); "
            "Design's are nothing / steel / a magnet, and flat / free."
            % (act_id, len(near), len(mounts)))
    _unique(near, act_id, "dip-circle", "bench object")
    _unique(mounts, act_id, "dip-circle", "mounting")
    keys = [n.get("id") for n in near]
    for want in ("none", "steel", "magnet"):
        if want not in keys:
            raise ValueError(
                "dip-circle %r has no %r on its bench list. The three are a "
                "set: nothing is the control, steel is the case that only "
                "wins where the field is weak, and a magnet is the case that "
                "wins anywhere." % (act_id, want))
    if [m.get("id") for m in mounts] != ["flat", "free"]:
        raise ValueError(
            "dip-circle %r names its mountings %r; they are `flat` and `free` "
            "in that order, because flat is what an ordinary walking compass "
            "is and it is the resting state."
            % (act_id, [m.get("id") for m in mounts]))

    steel_at = a.get("steel_wins_at")
    if not isinstance(steel_at, (int, float)) or steel_at <= 0:
        raise ValueError(
            "dip-circle %r has no `steel_wins_at`. It is the latitude beyond "
            "which a steel clamp stand beats what is left of the Earth's "
            "sideways pull, and it is a claim the bench makes out loud — the "
            "note says the same stand at the equator would lose." % act_id)
    nav_at = a.get("nav_at")
    if not isinstance(nav_at, (int, float)) or not 0 < nav_at < 100:
        raise ValueError(
            "dip-circle %r has no `nav_at`, the sideways-pull reading below "
            "which the needle is called sluggish. Design's is 12, which no "
            "latitude on her own list reaches, so the verdict is unreachable "
            "and her rung 4 is written about a state the bench never shows."
            % act_id)
    reach = [100.0 * __import__("math").cos(float(l["deg"]) * 3.141592653589793
                                            / 180.0) for l in lats]
    if not any(0 < v < float(nav_at) for v in reach):
        raise ValueError(
            "dip-circle %r sets `nav_at` to %s, which no latitude in the list "
            "falls below without being the pole. That makes the middle "
            "verdict copy no student can reach (5A.1)." % (act_id, nav_at))

    ctl = a.get("lat_control") or {}
    for key in ("min", "max", "step", "start", "label"):
        if key not in ctl:
            raise ValueError("dip-circle %r latitude control has no %r."
                             % (act_id, key))
    if int(ctl["max"]) != len(lats) - 1:
        raise ValueError(
            "dip-circle %r has %d latitudes and a slider that runs to %s."
            % (act_id, len(lats), ctl["max"]))

    branch_data = _branches("dipc", a,
                            ("captured_magnet", "captured_steel", "flat",
                             "flat_level", "flat_at_pole", "at_pole",
                             "tipped"),
                            act_id, "dip-circle")
    word_data = _words("dipc", a,
                       ("not_a_reading", "on_bench", "held_level",
                        "north_down", "north_up", "level_label", "dip_tag",
                        "nav_yes", "nav_barely", "nav_none",
                        "tips_down", "tips_up", "end_down", "end_up"),
                       act_id, "dip-circle")

    controls = (_slider(act_id, "dipc", ctl, "lat")
                + _picker("dipc", a.get("near_label", "On the bench beside it"),
                          "".join(
                              _seg("ks3-seg-btn ks3-dipc-near", n["label"],
                                   pressed=(i == int(a.get("start_near", 0))),
                                   data_dipc_near=n["id"], data_rank=i,
                                   data_label=n["label"])
                              for i, n in enumerate(near)))
                + _picker("dipc", a.get("mount_label", "How it is mounted"),
                          "".join(
                              _seg("ks3-seg-btn ks3-dipc-mount", m["label"],
                                   pressed=(i == int(a.get("start_mount", 0))),
                                   data_dipc_mount=m["id"], data_rank=i,
                                   data_label=m["label"])
                              for i, m in enumerate(mounts))))

    # Design's own 1000×400 viewBox: a level dashed line with the needle
    # pivoted on it, an arc marking the dip, and a globe with a tilted bar
    # magnet drawn inside it and a marker for where you are standing.
    svg = (
        '<svg class="ks3-dipc-svg" viewBox="0 0 1000 400" role="img" '
        'aria-label="" data-dipc-alt>'
        '<path class="ks3-dipc-levelline" d="M120 200 H420"/>'
        '<circle class="ks3-dipc-pivot" cx="270" cy="200" r="8"/>'
        '<path class="ks3-dipc-needle" data-dipc-needle d="M0 0"/>'
        '<path class="ks3-dipc-arc" data-dipc-arc d="M0 0"/>'
        '<circle class="ks3-dipc-globe" cx="720" cy="200" r="128"/>'
        '<path class="ks3-dipc-lines" d="M720 72 C860 100 860 300 720 328 '
        'M720 72 C580 100 580 300 720 328 M720 72 C920 120 920 280 720 328 '
        'M720 72 C520 120 520 280 720 328"/>'
        '<path class="ks3-dipc-bar" d="M690 100 H750 V300 H690 Z"/>'
        '<path class="ks3-dipc-barnorth" d="M693 203 H747 V297 H693 Z"/>'
        '<circle class="ks3-dipc-you" data-dipc-you cx="720" cy="72" r="11"/>'
        '<text class="ks3-dipc-caption" x="270" y="360" '
        'text-anchor="middle">%s</text>'
        '<text class="ks3-dipc-caption" x="720" y="360" '
        'text-anchor="middle">%s</text></svg>'
        % (t(a.get("side_label", "SEEN FROM THE SIDE, LOOKING WEST")),
           t(a.get("globe_label", "WHERE YOU ARE ON THE PLANET"))))

    fills = "".join(
        '<span class="ks3-dipc-fill ks3-dipc-%s" data-dipc-fill="%s"></span>'
        % (key, key) for key in ("level", "dip"))

    return _wrap("dipc", act_id, a,
                 [("data-navat", nav_at), ("data-steelat", steel_at),
                  ("data-degs", " ".join(str(l["deg"]) for l in lats)),
                  ("data-names", "|".join(l["name"] for l in lats)),
                  ("data-start-near", a.get("start_near", 0)),
                  ("data-start-mount", a.get("start_mount", 0))],
                 controls, svg, fills,
                 _tiles("dipc", a.get("readouts") or []),
                 branch_data + word_data)


# ═══ p10-04 · #s-bench · a coil, a supply and a pile of paper clips ══════

def r_solenoid_bench(a, act_id):
    """⊕ p10-04 `#s-bench` — build one and see what it lifts.

    ⚖️ **TURNS AND CURRENT ARE TWO SEPARATE CONTROLS BECAUSE THEY ARE TWO
    SEPARATE REASONS.** `MAG-14` is *more turns means more wire, so more
    current*; the only way to break it is to let the student hold the current
    still and watch the field rise anyway. Field is `turns × current × core`,
    and the two sliders move independently.

    ⚖️ **THE PLASTIC FORMER IS MODELLED AS NO CORE, AND THE BENCH SAYS SO ON
    ITS FACE** (her §9 ruling 4). A control that is DRAWN must be MODELLED
    (5A.1) — and here the honest model is that it does nothing, so the note
    says that rather than leaving the student to notice that the number did
    not move.

    ⚖️ **SWITCHED OFF IS ZERO AND IS SAID TO BE ZERO.** Seventy-five of the
    hundred and fifty states are switch-open, and the readout reads `zero, not
    merely small` rather than a small number. `MAG-15` is *switching off
    leaves a weak field that drains away*, and a bench that printed 0.0 for
    off and 0.0 for a genuinely weak setting would confirm it.

    ⚠️ **WHICH IS WHY A SMALL FIELD NEVER PRINTS `0.0`.** Design's tile is
    `toFixed(1)`, so nine of the seventy-five on-states print `0.0` for a
    field that is real. Below 0.1 the figure takes two decimals here — which
    is `p10-01`'s own convention for its lowest band — so `zero` on this page
    only ever means zero.

    ⚖️ **THE COIL IS DRAWN AS EIGHT LOOPS WHATEVER THE TURN COUNT.** The
    drawing is a symbol and the number is the readout. Drawing 160 loops would
    be unreadable and drawing 10 would make the symbol a count that then lies
    at every other setting.

    ⚠️ **THE CLIP CHAIN IS CAPPED AT TEN DRAWN MARKS AND THE TILE CARRIES THE
    COUNT.** Same argument, and the tile uses the engine's own one/many
    handling so `1 paper clip` is never `1 paper clips`.

    HOOKS: `data-solen` (wrapper, `data-maxfield`, `data-cliprate`) ·
    `data-solen-gate` · `data-solen-gopt` · `data-solen-body` ·
    `data-solen-slider` · `data-solen-core` · `data-solen-switch` ·
    `data-solen-coil` · `data-solen-core-path` · `data-solen-switchpath` ·
    `data-solen-field` · `data-solen-clips` · `data-solen-fill` ·
    `data-solen-out` · `data-solen-note`.
    """
    _no_units(a, act_id, "solenoid-bench")

    turns = a.get("turns") or []
    currents = a.get("currents") or []
    if len(turns) < 4 or len(currents) < 4:
        raise ValueError(
            "solenoid-bench %r offers %d turn setting(s) and %d current "
            "setting(s). Design's are five and five, spanning a factor of "
            "sixteen and twenty, which is what makes the two controls "
            "visibly independent." % (act_id, len(turns), len(currents)))
    if sorted(turns) != list(turns) or sorted(currents) != list(currents):
        raise ValueError(
            "solenoid-bench %r has a slider whose settings are not in order. "
            "A slider that goes down as it moves right is a control that "
            "teaches the opposite of what it does." % act_id)

    cores = a.get("cores") or []
    if len(cores) != 3:
        raise ValueError(
            "solenoid-bench %r declares %d core(s). Design's three are "
            "nothing, a plastic former and soft iron, and the plastic one is "
            "not padding: it is the control that separates `the core does it` "
            "from `the current does it`." % (act_id, len(cores)))
    _unique(cores, act_id, "solenoid-bench", "core")
    factors = {}
    for c in cores:
        for f in ("id", "label", "with_phrase", "down_phrase"):
            if not c.get(f):
                raise ValueError(
                    "solenoid-bench %r core %r has no %r. `with_phrase` reads "
                    "after `with`, `down_phrase` reads before `down the "
                    "middle` — and they are two different phrasings because "
                    "the empty coil cannot use one string in both sentences."
                    % (act_id, c.get("id"), f))
        if not isinstance(c.get("factor"), (int, float)) or c["factor"] < 1:
            raise ValueError(
                "solenoid-bench %r core %r has no `factor` ≥ 1."
                % (act_id, c.get("id")))
        factors[c["id"]] = float(c["factor"])
    if factors.get("air") != factors.get("plastic"):
        raise ValueError(
            "solenoid-bench %r gives the plastic former a factor of %r "
            "against air's %r. RULED (Design §9.4): plastic is modelled as "
            "IDENTICAL to no core, and the bench says so on its face rather "
            "than leaving the student to infer it from a number that did not "
            "move." % (act_id, factors.get("plastic"), factors.get("air")))
    if not factors.get("iron", 0) > 5 * factors.get("air", 1):
        raise ValueError(
            "solenoid-bench %r gives soft iron a factor of %r. Rung 1's "
            "correct answer is that swapping the iron for plastic is the one "
            "change that does not help, and its correction calls the core "
            "`the single biggest change available on the bench` — so the "
            "factor has to be big enough for that to be visible."
            % (act_id, factors.get("iron")))

    switches = a.get("switches") or []
    if [s.get("id") for s in switches] != ["off", "on"]:
        raise ValueError(
            "solenoid-bench %r names its switch states %r; they are `off` and "
            "`on` in that order, because open is the resting state and the "
            "whole lesson is what happens when it closes."
            % (act_id, [s.get("id") for s in switches]))

    rate = a.get("clip_rate")
    if not isinstance(rate, (int, float)) or rate <= 0:
        raise ValueError(
            "solenoid-bench %r has no `clip_rate` — the clips held per unit "
            "of field. The count is the thing a student can see across the "
            "room, and a bench that reported only a relative figure would "
            "have nothing physical in it at all." % act_id)
    top = float(turns[-1]) * float(currents[-1]) * max(factors.values())
    if int(rate * top) < 20:
        raise ValueError(
            "solenoid-bench %r tops out at %d clip(s). A chain is what makes "
            "the strongest setting feel different from the middle one, and "
            "the drawing caps at ten marks, so the number has to run past "
            "that." % (act_id, int(rate * top)))

    for ctl_key, label in (("turns_control", "turns"),
                           ("current_control", "current")):
        ctl = a.get(ctl_key) or {}
        for key in ("min", "max", "step", "start", "label"):
            if key not in ctl:
                raise ValueError("solenoid-bench %r %s control has no %r."
                                 % (act_id, label, key))
    if int(a["turns_control"]["max"]) != len(turns) - 1 or \
            int(a["current_control"]["max"]) != len(currents) - 1:
        raise ValueError(
            "solenoid-bench %r has a slider that cannot reach every setting "
            "it declares." % act_id)

    band_data = _bands("solen", a.get("strength_bands") or [], act_id,
                       "solenoid-bench", "s")
    branch_data = _branches("solen", a,
                            ("off", "iron", "air", "plastic"),
                            act_id, "solenoid-bench")
    word_data = _words("solen", a,
                       ("no_field", "zero_sub", "scale_sub", "north_end",
                        "no_pole", "core_off", "core_iron", "core_plastic",
                        "core_air", "clip_none", "clip_chain", "clip_off",
                        "clip_zero", "clip_one", "clip_many"),
                       act_id, "solenoid-bench")

    controls = (_slider(act_id, "solen", a["turns_control"], "t")
                + _slider(act_id, "solen", a["current_control"], "i")
                + _picker("solen", a.get("core_label", "Down the middle"),
                          "".join(
                              _seg("ks3-seg-btn ks3-solen-core", c["label"],
                                   pressed=(i == int(a.get("start_core", 0))),
                                   data_solen_core=c["id"], data_rank=i,
                                   data_factor=c["factor"],
                                   data_with=c["with_phrase"],
                                   data_down=c["down_phrase"],
                                   data_label=c["label"])
                              for i, c in enumerate(cores)))
                + _picker("solen", a.get("switch_label", "The switch"),
                          "".join(
                              _seg("ks3-seg-btn ks3-solen-switch", s["label"],
                                   pressed=(i == int(a.get("start_switch", 0))),
                                   data_solen_switch=s["id"], data_rank=i,
                                   data_label=s["label"])
                              for i, s in enumerate(switches))))

    svg = (
        '<svg class="ks3-solen-svg" viewBox="0 0 1000 400" role="img" '
        'aria-label="" data-solen-alt>'
        '<path class="ks3-solen-wire" d="M120 120 H260 M120 120 V260 H260"/>'
        '<path class="ks3-solen-cell" d="M96 168 H144 M110 181 H130 '
        'M96 194 H144 M110 207 H130"/>'
        '<path class="ks3-solen-wire" data-solen-switchpath d="M0 0"/>'
        '<path class="ks3-solen-corepath" data-solen-core-path d="M0 0"/>'
        '<path class="ks3-solen-coil" data-solen-coil d="M0 0"/>'
        '<path class="ks3-solen-field" data-solen-field d="M0 0"/>'
        '<path class="ks3-solen-clips" data-solen-clips d="M0 0"/>'
        '<text class="ks3-solen-caption" x="120" y="300" '
        'text-anchor="middle">%s</text>'
        '<text class="ks3-solen-caption" x="620" y="376" '
        'text-anchor="middle">%s</text></svg>'
        % (t(a.get("supply_label", "SUPPLY")),
           t(a.get("clip_label", "PAPER CLIPS HANGING FROM THE END"))))

    fills = "".join(
        '<span class="ks3-solen-fill ks3-solen-%s" data-solen-fill="%s">'
        '</span>' % (key, key) for key in ("west", "east"))

    return _wrap("solen", act_id, a,
                 [("data-maxfield", top), ("data-cliprate", rate),
                  ("data-turns", " ".join(str(v) for v in turns)),
                  ("data-currents", " ".join(str(v) for v in currents)),
                  ("data-start-core", a.get("start_core", 0)),
                  ("data-start-switch", a.get("start_switch", 0))],
                 controls, svg, fills,
                 _tiles("solen", a.get("readouts") or []),
                 band_data + branch_data + word_data)


# ═══ p10-05 · #s-bench · a coil on an axle between two magnets ═══════════

def r_motor_coil(a, act_id):
    """⊕ p10-05 `#s-bench` — reverse one thing at a time.

    ⚖️ **THE COIL IS FROZEN HORIZONTAL** (her §9 ruling 5). Nothing here
    animates and nothing has a timer: the bench shows the pushes at the
    position where the turning effect is largest, and the legal line says both
    that this is the frozen best case and that a real single-coil motor's
    turning effect falls to nothing twice per turn.

    ⚖️ **REVERSE ONE THING AND IT REVERSES; REVERSE BOTH AND IT DOES NOT.**
    That is the whole lesson and it is a property of the arithmetic here rather
    than of four authored strings: the direction is the SIGN of `current ×
    field`, so the both-reversed case comes out identical by construction.
    `MAG-19` is exactly the belief that two changes must make two differences.

    ⚖️ **THE SPLIT RING DOES NOT MAKE IT TURN — IT MAKES IT KEEP TURNING.**
    The `plain rings` state still starts, and its note says so in its first two
    words, because `MAG-18` is the belief that the ring is what does the
    turning. Half of the twenty-four turning states are plain-ring states, so a
    student meets the distinction rather than reading it.

    ⚖️ **FRICTION IS REAL AND IT IS WHY THE LOWEST CURRENT DOES NOTHING.**
    Eight of the thirty-two states never start, and the note names the number
    the turning effect has to beat. That is the zero state driven on purpose:
    the pushes are drawn, they are in the right directions, and they are not
    enough.

    ⚠️ **A ROTATION ARC IS DRAWN ONLY WHERE THE COIL ACTUALLY TURNS.** An arc
    under a coil that is not moving is the one mark on this bench that could
    contradict its own readout.

    HOOKS: `data-mcoil` (wrapper, `data-friction`, `data-maxcurrent`) ·
    `data-mcoil-gate` · `data-mcoil-gopt` · `data-mcoil-body` ·
    `data-mcoil-dir` · `data-mcoil-mag` · `data-mcoil-comm` ·
    `data-mcoil-slider` · `data-mcoil-pole` · `data-mcoil-field` ·
    `data-mcoil-current` · `data-mcoil-force` · `data-mcoil-ring` ·
    `data-mcoil-spin` · `data-mcoil-fill` · `data-mcoil-out` ·
    `data-mcoil-note`.
    """
    _no_units(a, act_id, "motor-coil")

    for key, want, why in (
            ("dirs", 2, "the current runs one way or the other and there is "
                        "no third"),
            ("mags", 2, "the field runs one way or the other and there is no "
                        "third"),
            ("comms", 2, "the split ring is either fitted or it is not")):
        rows = a.get(key) or []
        if len(rows) != want:
            raise ValueError(
                "motor-coil %r declares %d %s; %s."
                % (act_id, len(rows), key, why))
        _unique(rows, act_id, "motor-coil", key)
        for r in rows:
            if not r.get("id") or not r.get("label"):
                raise ValueError("motor-coil %r %s entry %r needs `id` and "
                                 "`label`." % (act_id, key, r))
        if key == "comms":
            for r in rows:
                if not r.get("caption"):
                    raise ValueError(
                        "motor-coil %r commutator %r has no `caption`. It is "
                        "the label under the drawing, it changes with the "
                        "control, and it is a string a student reads — so it "
                        "is authored beside the physics rather than typed "
                        "into `shared/ks3.js`." % (act_id, r.get("id")))
    signs = sorted(int(r.get("sign", 0)) for r in a["dirs"])
    if signs != [-1, 1] or sorted(int(r.get("sign", 0))
                                  for r in a["mags"]) != [-1, 1]:
        raise ValueError(
            "motor-coil %r does not give its two current directions and its "
            "two field directions opposite signs. The direction the coil "
            "turns is the SIGN of the product, and that is what makes "
            "`reverse both and nothing changes` true by construction rather "
            "than by four authored sentences." % act_id)
    if [c.get("id") for c in a["comms"]] != ["split", "plain"]:
        raise ValueError(
            "motor-coil %r names its commutator states %r; they are `split` "
            "and `plain` in that order, because a working motor is the "
            "resting state and the plain ring is the fault."
            % (act_id, [c.get("id") for c in a["comms"]]))

    currents = a.get("currents") or []
    if len(currents) < 3 or sorted(currents) != list(currents):
        raise ValueError(
            "motor-coil %r needs an ascending list of at least three "
            "currents." % act_id)
    friction = a.get("friction")
    top = a.get("max_current")
    if not isinstance(friction, (int, float)) or friction <= 0:
        raise ValueError(
            "motor-coil %r has no `friction`. Without it every setting turns, "
            "the `never starts` branch is unreachable, and rung 2's whole "
            "premise — that a motor can be built and fail to move — has "
            "nothing on the bench behind it." % act_id)
    if not isinstance(top, (int, float)) or top <= 0:
        raise ValueError("motor-coil %r has no `max_current` reference."
                         % act_id)
    if float(currents[-1]) != float(top):
        raise ValueError(
            "motor-coil %r declares 100 at %s A while its slider reaches %s "
            "A. The readout says 100 is the strongest setting here, so the "
            "strongest setting has to read 100." % (act_id, top, currents[-1]))
    below = [c for c in currents if 100.0 * float(c) / float(top) < friction]
    if not below:
        raise ValueError(
            "motor-coil %r has no current setting below the friction at the "
            "axle, so the `never starts` branch is copy no student can reach "
            "(5A.1)." % act_id)
    if len(below) == len(currents):
        raise ValueError(
            "motor-coil %r has no current setting that beats friction, so the "
            "motor never runs at all." % act_id)

    ctl = a.get("current_control") or {}
    for key in ("min", "max", "step", "start", "label"):
        if key not in ctl:
            raise ValueError("motor-coil %r current control has no %r."
                             % (act_id, key))
    if int(ctl["max"]) != len(currents) - 1:
        raise ValueError(
            "motor-coil %r has %d currents and a slider that runs to %s."
            % (act_id, len(currents), ctl["max"]))

    branch_data = _branches("mcoil", a, ("never", "split", "plain"),
                            act_id, "motor-coil")
    word_data = _words("mcoil", a,
                       ("up", "down", "clockwise", "anticlockwise", "still",
                        "left_is", "right_is", "field_lr", "field_rl"),
                       act_id, "motor-coil")

    def row(key, hook_name, start):
        return "".join(
            _seg("ks3-seg-btn ks3-mcoil-%s" % hook_name, r["label"],
                 pressed=(i == int(start)),
                 **{"data_mcoil_%s" % hook_name: r["id"],
                    "data_rank": i, "data_sign": r.get("sign", 0),
                    "data_caption": r.get("caption", ""),
                    "data_label": r["label"]})
            for i, r in enumerate(a[key]))

    controls = (_picker("mcoil", a.get("dir_label", "Current round the coil"),
                        row("dirs", "dir", a.get("start_dir", 0)))
                + _picker("mcoil", a.get("mag_label", "The magnets"),
                          row("mags", "mag", a.get("start_mag", 0)))
                + _picker("mcoil", a.get("comm_label", "At the axle"),
                          row("comms", "comm", a.get("start_comm", 0)))
                + _slider(act_id, "mcoil", ctl, "i"))

    svg = (
        '<svg class="ks3-mcoil-svg" viewBox="0 0 1000 400" role="img" '
        'aria-label="" data-mcoil-alt>'
        '<path class="ks3-mcoil-magnet" d="M60 96 H180 V304 H60 Z '
        'M820 96 H940 V304 H820 Z"/>'
        '<path class="ks3-mcoil-pole" data-mcoil-pole d="M0 0"/>'
        '<path class="ks3-mcoil-field" data-mcoil-field d="M0 0"/>'
        '<path class="ks3-mcoil-loop" d="M360 120 H640 V280 H360 Z"/>'
        '<path class="ks3-mcoil-lead" d="M180 200 H360 M640 200 H820"/>'
        '<path class="ks3-mcoil-current" data-mcoil-current d="M0 0"/>'
        '<path class="ks3-mcoil-force" data-mcoil-force d="M0 0"/>'
        '<circle class="ks3-mcoil-axlepin" cx="500" cy="200" r="26"/>'
        '<path class="ks3-mcoil-ring" data-mcoil-ring d="M0 0"/>'
        '<path class="ks3-mcoil-spin" data-mcoil-spin d="M0 0"/></svg>')

    fills = "".join(
        '<span class="ks3-mcoil-fill ks3-mcoil-%s" data-mcoil-fill="%s">'
        '</span>' % (key, key) for key in ("axle", "leftpole", "rightpole"))

    return _wrap("mcoil", act_id, a,
                 [("data-friction", friction), ("data-maxcurrent", top),
                  ("data-currents", " ".join(str(v) for v in currents)),
                  ("data-start-dir", a.get("start_dir", 0)),
                  ("data-start-mag", a.get("start_mag", 0)),
                  ("data-start-comm", a.get("start_comm", 0))],
                 controls, svg, fills,
                 _tiles("mcoil", a.get("readouts") or []),
                 branch_data + word_data)


# ═══ the fixed figure beside each bench ══════════════════════════════════

def r_mag_band(a, act_id):
    """⊕ The band-ground figure Design puts between each bench and the ladder.

    ⚖️ **`tiles`, `panels` AND `close` — NOT `cards`.** `cards` is claimed by
    `r_activity` itself with NO opt-out, so a payload using it gets two
    renderers and renders blank. The keys are deliberately different for that
    reason and no other.

    ⚖️ **ALL FIVE ARE TICKED BY THE BENCH BESIDE THEM.** None carries a control
    of its own: each is the payoff of the instrument above it, in exactly
    MRB-249's sense, and Design's `DONE` gives all five `s.gate !== null` —
    the bench's own commitment, before the bench itself is finished. Each bench
    marks its sibling through `band_anchor` / `band_at`. `mirrors` is NOT used
    and would be wrong twice over; see `_sibling`.

    One shape, five payloads, because Design draws one shape five times:

      `p10-01`  `s-proof`  three outcome cards, each with a drawing, plus two
                           panels naming what a magnet works on
      `p10-02`  `s-rules`  four rule cards, each with a drawing
      `p10-03`  `s-earth`  three text cards and a closing panel
      `p10-04`  `s-uses`   four text cards and two summary panels
      `p10-05`  `s-parts`  four text cards and a closing panel

    ⚠️ **NOTHING HERE HOLDS A LIVE VALUE.** Every string is a constant at build
    time, which is why the labels inside the drawings are SVG `<text>` and not
    overlay spans — MRB-254 forbids a `<text>` that ships empty to be filled
    later, and none of these is.

    ⚠️ **NO EYEBROW AND NO HEADING ARE DRAWN HERE.** `r_activity`'s shell has
    already emitted both from the same two payload keys. Drawing them again is
    the P4/P5/P6 duplication in a second shape.
    """
    tiles = a.get("tiles") or []
    if len(tiles) < 3:
        raise ValueError(
            "mag-band %r draws %d tile(s). Every one of Design's five band "
            "figures is a grid of three or four; a figure with fewer is a "
            "heading with a sentence under it." % (act_id, len(tiles)))
    _unique(tiles, act_id, "mag-band", "tile")
    for tile in tiles:
        if not tile.get("body"):
            raise ValueError(
                "mag-band %r tile %r has no `body`. The drawing and the title "
                "are both optional here — three of the five figures have no "
                "drawing at all — but the sentence never is."
                % (act_id, tile.get("id")))
        if tile.get("art") and tile["art"] not in _BAND_ART:
            raise ValueError(
                "mag-band %r tile %r names art %r, which nothing draws. The "
                "drawn set is %s — a figure whose art has no drawer renders "
                "an empty box, which is the MRB-244 defect in miniature."
                % (act_id, tile.get("id"), tile["art"],
                   ", ".join(sorted(_BAND_ART))))
        if tile.get("art") and not tile.get("aria_label"):
            raise ValueError(
                "mag-band %r tile %r draws %r with no `aria_label`. A `<desc>` "
                "or aria label describes what is ACTUALLY DRAWN, and a "
                "drawing without one is the whole figure missing for a reader "
                "who cannot see it." % (act_id, tile.get("id"), tile["art"]))
    accents = [tile for tile in tiles if tile.get("accent")]
    if len(accents) != 1:
        raise ValueError(
            "mag-band %r marks %d tile(s) with the accent offset. Design "
            "marks exactly ONE on every band figure in this unit — the one "
            "that is the answer rather than one of the alternatives — and two "
            "marked tiles is two claims to be the point."
            % (act_id, len(accents)))

    lead = ('<p class="ks3-magband-lead">%s</p>' % rich(a["lead"])
            if a.get("lead") else "")

    cells = ""
    for tile in tiles:
        eyebrow = ('<p class="ks3-magband-eyebrow">%s</p>' % t(tile["eyebrow"])
                   if tile.get("eyebrow") else "")
        art = _BAND_ART[tile["art"]](tile["aria_label"]) if tile.get("art") \
            else ""
        title = ('<p class="ks3-magband-title">%s</p>' % t(tile["title"])
                 if tile.get("title") else "")
        cells += ('<div class="ks3-magband-tile%s">%s%s%s'
                  '<p class="ks3-magband-body">%s</p></div>'
                  % (" is-accent" if tile.get("accent") else "",
                     eyebrow, art, title, rich(tile["body"])))

    panels = ""
    for p in a.get("panels") or []:
        if not p.get("label") or not p.get("text"):
            raise ValueError("mag-band %r panel %r needs `label` and `text`."
                             % (act_id, p))
        panels += ('<div class="ks3-magband-panel">'
                   '<p class="ks3-magband-panellabel">%s</p>'
                   '<p class="ks3-magband-paneltext">%s</p></div>'
                   % (t(p["label"]), rich(p["text"])))
    if panels:
        panels = '<div class="ks3-magband-panels">%s</div>' % panels

    close = ('<p class="ks3-magband-close">%s</p>' % rich(a["close"])
             if a.get("close") else "")

    return ('<div class="ks3-magband" data-magband>%s'
            '<div class="ks3-magband-tiles">%s</div>%s%s</div>'
            % (lead, cells, panels, close))


# ── the seven drawings inside the band figures ───────────────────────────
#
# ⚠️ EVERY ONE OF THESE IS A CONSTANT. Nothing in them varies with anything a
# student does, which is why the captions are literal `<text>` rather than
# overlay spans: MRB-254's rule is about a `<text>` that ships EMPTY and is
# filled later, and none of these is ever empty.

def _band_svg(view, body, aria):
    return ('<svg class="ks3-magband-art" viewBox="%s" role="img" '
            'aria-label="%s">%s</svg>' % (view, e(aria), body))


def _art_repel(aria):
    """Two bars pushing apart. The one outcome that settles the question, so
    it is the only one of the three drawn on the accent."""
    return _band_svg(
        "0 0 260 90",
        '<rect class="ks3-magband-bar" x="12" y="30" width="96" height="34" '
        'rx="5"/><rect class="ks3-magband-bar" x="152" y="30" width="96" '
        'height="34" rx="5"/>'
        '<path class="ks3-magband-arrow" d="M104 16 H62 M62 16 L74 8 '
        'M62 16 L74 24 M156 16 H198 M198 16 L186 8 M198 16 L186 24"/>'
        '<text class="ks3-magband-artcap" x="130" y="84" '
        'text-anchor="middle">THEY PUSH APART</text>', aria)


def _art_attract(aria):
    """Two bars pulling together — one of them drawn plain, because the whole
    point is that the second could be either thing."""
    return _band_svg(
        "0 0 260 90",
        '<rect class="ks3-magband-bar" x="12" y="30" width="96" height="34" '
        'rx="5"/><rect class="ks3-magband-plain" x="152" y="30" width="96" '
        'height="34" rx="5"/>'
        '<path class="ks3-magband-quiet" d="M62 16 H104 M104 16 L92 8 '
        'M104 16 L92 24 M198 16 H156 M156 16 L168 8 M156 16 L168 24"/>'
        '<text class="ks3-magband-artcap" x="130" y="84" '
        'text-anchor="middle">THEY PULL TOGETHER</text>', aria)


def _art_nothing(aria):
    """Two bars sitting still. The second is DASHED — the same channel the
    bench uses for a non-magnetic material, so the two agree."""
    return _band_svg(
        "0 0 260 90",
        '<rect class="ks3-magband-bar" x="12" y="30" width="96" height="34" '
        'rx="5"/><rect class="ks3-magband-dashed" x="152" y="30" width="96" '
        'height="34" rx="5"/>'
        '<text class="ks3-magband-artcap" x="130" y="84" '
        'text-anchor="middle">NOTHING HAPPENS</text>', aria)


def _art_outin(aria):
    """A bar magnet with one line leaving N and curving into S."""
    return _band_svg(
        "0 0 240 110",
        '<rect class="ks3-magband-bar" x="76" y="46" width="88" height="24" '
        'rx="4"/>'
        '<path class="ks3-magband-line" d="M164 58 C206 58 214 12 120 12 '
        'C26 12 34 58 76 58"/>'
        '<path class="ks3-magband-head" d="M176 58 L164 51 L164 65 Z"/>'
        '<text class="ks3-magband-pole" x="88" y="66">S</text>'
        '<text class="ks3-magband-pole" x="146" y="66">N</text>'
        '<text class="ks3-magband-artcap" x="120" y="100" '
        'text-anchor="middle">OUT OF N, INTO S</text>', aria)


def _art_crowd(aria):
    """Five lines packed and three spread — the spacing IS the claim, so the
    two groups differ only in how much room the same marks are given."""
    return _band_svg(
        "0 0 240 110",
        '<path class="ks3-magband-line" d="M20 20 H120 M20 32 H120 '
        'M20 44 H120 M20 56 H120 M20 68 H120"/>'
        '<path class="ks3-magband-line" d="M140 16 H228 M140 44 H228 '
        'M140 72 H228"/>'
        '<text class="ks3-magband-artcap" x="70" y="100" '
        'text-anchor="middle">STRONG</text>'
        '<text class="ks3-magband-artcap" x="184" y="100" '
        'text-anchor="middle">WEAK</text>', aria)


def _art_nocross(aria):
    """Two dashed lines crossing, with the crossing struck through."""
    return _band_svg(
        "0 0 240 110",
        '<path class="ks3-magband-ghost" d="M40 20 L200 74 M40 74 L200 20"/>'
        '<circle class="ks3-magband-ring" cx="120" cy="47" r="21"/>'
        '<path class="ks3-magband-strike" d="M106 33 L134 61"/>'
        '<text class="ks3-magband-artcap" x="120" y="100" '
        'text-anchor="middle">NEVER</text>', aria)


def _art_readings(aria):
    """One curve with three small compasses sitting along it, each lying
    along the curve — the figure's claim is that the line IS the readings."""
    return _band_svg(
        "0 0 240 110",
        '<path class="ks3-magband-ghost" d="M18 74 C70 12 170 12 222 74"/>'
        '<circle class="ks3-magband-dial" cx="52" cy="42" r="15"/>'
        '<path class="ks3-magband-needle" d="M42 50 L62 34"/>'
        '<circle class="ks3-magband-dial" cx="120" cy="24" r="15"/>'
        '<path class="ks3-magband-needle" d="M109 24 H131"/>'
        '<circle class="ks3-magband-dial" cx="188" cy="42" r="15"/>'
        '<path class="ks3-magband-needle" d="M178 34 L198 50"/>'
        '<text class="ks3-magband-artcap" x="120" y="100" '
        'text-anchor="middle">THE LINE IS THE READING</text>', aria)


_BAND_ART = {
    "repel": _art_repel,
    "attract": _art_attract,
    "nothing": _art_nothing,
    "out-in": _art_outin,
    "crowd": _art_crowd,
    "no-cross": _art_nocross,
    "readings": _art_readings,
}


# ═══ registration ════════════════════════════════════════════════════════
#
# ONE ROW PER RENDERER. Every family is P10's own — `ks3_art/core.py` and
# `ks3_art/kit.py` are untouched. Every shell stem was checked against the
# whole registry, `shared/ks3.js` and `shared/ks3.css` first; all six were
# free.

ART = {}

KIND_SHELL = {
    'track-pair':      ("ks3-tpair-block",
                        ' data-instrument data-tpairblock '
                        'data-stage-done="0"'),
    'compass-plot':    ("ks3-cplot-block",
                        ' data-instrument data-cplotblock '
                        'data-stage-done="0"'),
    'dip-circle':      ("ks3-dipc-block",
                        ' data-instrument data-dipcblock '
                        'data-stage-done="0"'),
    'solenoid-bench':  ("ks3-solen-block",
                        ' data-instrument data-solenblock '
                        'data-stage-done="0"'),
    'motor-coil':      ("ks3-mcoil-block",
                        ' data-instrument data-mcoilblock '
                        'data-stage-done="0"'),
    # ⚠️ The band figure DECLARES `data-stage-done="0"` and carries no control
    # of its own. Both halves are load-bearing: the declaration is what
    # `check_nothing_ticks_on_load` reads out of the SHIPPED BYTES, and the
    # absence of a control is why the bench beside it has to do the marking.
    'mag-band':        ("ks3-magband-block",
                        ' data-instrument data-magbandblock '
                        'data-stage-done="0"'),
}

KIND_FN = {
    'track-pair':      r_track_pair,
    'compass-plot':    r_compass_plot,
    'dip-circle':      r_dip_circle,
    'solenoid-bench':  r_solenoid_bench,
    'motor-coil':      r_motor_coil,
    'mag-band':        r_mag_band,
}
