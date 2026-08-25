"""ks3_art.p5 — P5 *Pressure*, the unit where a force meets an area.

Every instrument here is authored against Claude Design's delivered pages in
`docs/ks3/design-reference/p5/`. Her page wins outright: a shape that is not
in her drawing is not in this module, and where her NOTES and her drawing
disagree the DRAWING IS MEASURED and the note is reported.

── ⚖️ MRB-204 · ONE TRIANGLE IN FOUR LESSONS, AND IT IS `p5-01` ───────────

    p5-01  pressure = force ÷ area     a PRODUCT rearranged   TRIANGLE
    p5-02  pressure at a depth         a SUM OF LAYERS        STACK
    p5-03  left over = weight − upthrust   a DIFFERENCE       BEAM
    p5-04  air pressure                a SUM OF LAYERS        STACK

`p5-01` is the only product in the unit and the only triangle. The triangle
asserts `force = pressure × area`, which is TRUE, and the lesson's own
relationship is that product rearranged — so `A = B × C` holds and the
figure encodes a relationship that exists.

`p5-02` and `p5-04` are the same shape carrying different physics: the new
content in both is WHERE THE FORCE COMES FROM — a sum of layers — and the
arithmetic is `p5-01`'s division. `p5-04`'s bands are unequal because air is
squashable, and the drawer refuses equal bands there for exactly that reason.

── ⚖️ NONE OF THE THREE NON-TRIANGLE FIGURES HAS COVER BUTTONS ────────────

Design's flag 0a, and it is right. A part–whole bar keeps its buttons
because covering a part asks a real question; a STACK and a BALANCE do not,
because covering a layer of water means nothing and covering one of two
opposed arrows asks nothing. `r_cover_bar` in the engine is the buttoned
variant and nothing here reaches it.

── ⚠️ `p5-02` REPORTS GAUGE PRESSURE, AND THE PAGE SAYS SO ────────────────

The probe reads the pressure of the LIQUID ALONE. The atmosphere is pressing
on the surface as well and adds about 100 000 Pa everywhere in the tank, so
a reader who does not know that will think the tank is at 0 Pa at the
surface in an absolute sense. Design puts it in the legal line; the renderer
requires that line to exist.

── ⚠️ RESERVED PAYLOAD KEYS ───────────────────────────────────────────────

`r_activity` renders `cards`, `sim`, `fifa` and `scorecards` ITSELF, with no
opt-out. Nothing here uses any of the four.

── ⚠️ SHELL CLASSES ARE UNIQUE ACROSS THE WHOLE REGISTRY ─────────────────

`ks3_art.load()` asserts it since MRB-279, and it caught `ks3-srig-` in P4
on the first run. Checked again before these were written.

── ⚠️ BAND VALUES ─────────────────────────────────────────────────────────

Full words — `easier`, `standard`, `harder`. Never `s` or `h`.
"""

from ks3_art.kit import e, r_cfifa_attempt, rich, t


# ⚠️ `ground` IS A RESERVED PAYLOAD KEY AND THIS MODULE MUST NOT USE IT.
# `r_activity` reads `a["ground"]` on EVERY instrument payload with no
# opt-out and admits only band / card / ground / inset, so a bench that
# used `ground` for a y-coordinate crashed the build with
# `unknown ground 470`. Both benches that need a base line now say
# `base_y`, and emit `data-base-y`. The same applies to `cards`, `sim`,
# `fifa` and `scorecards`: every key, exactly one renderer.

# ═══ shared P5 primitives ════════════════════════════════════════════════

def _seg(cls, label, pressed=False, **attrs):
    bits = "".join(' %s="%s"' % (k.replace("_", "-"), e(str(v)))
                   for k, v in sorted(attrs.items()))
    return ('<button type="button" class="%s" aria-pressed="%s"%s>%s</button>'
            % (e(cls), "true" if pressed else "false", bits, t(label)))


def _gate(act_id, family, gate, hook):
    """The commit gate every P5 bench opens behind. All four have one."""
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
    """The readout row. `sub` is Design's second line — the working."""
    cells = ""
    for s in specs:
        sub = ('<p class="ks3-%s-tile-sub" data-%s-sub="%s"></p>'
               % (hook, hook, e(s["id"]))) if s.get("sub") else ""
        cells += ('<div class="ks3-%s-tile">'
                  '<p class="ks3-%s-tile-label" data-%s-label="%s">%s</p>'
                  '<p class="ks3-%s-tile-value" data-%s-out="%s">%s</p>%s'
                  '</div>'
                  % (hook, hook, hook, e(s["id"]), t(s["label"]),
                     hook, hook, e(s["id"]), t(s.get("value", "—")), sub))
    return '<div class="ks3-%s-tiles">%s</div>' % (hook, cells)


def _head(hook, a):
    """⊕ MRB-223, 25 Aug 2026 — RETURNS NOTHING, DELIBERATELY. A live defect.

    This used to draw a second head row — eyebrow, `<h2>` and a progress
    paragraph — inside every bench in this unit. `r_activity` had ALREADY
    drawn Design's row (`.ks3-blockhead`, from the same `eyebrow` /
    `heading` / `progress` keys), so every shipped bench in P4, P5 and P6
    printed its eyebrow and its heading twice. Measured in the built bytes:
    one duplicated `<h2>` on all 22 lesson pages; 16 placements in P6 alone.
    P7 onwards never drew the second row (see `ks3_art/p7.py`); this brings
    the three earlier units to the same shape without touching any of the
    templates that call it. The wiring now writes the readout into the
    shell's own `[data-count]`, which is the element the student was always
    reading first.
    """
    return ""


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


# ═══ p5-01 · #s-bench · the block on sand ════════════════════════════════

def r_block_on_sand(a, act_id):
    """⊕ p5-01 `#s-bench` — same weight, different face, different hole.

    ⚖️ **ONE SOLID, THREE FACES, AND THE AREAS ARE CHECKED AGAINST THE
    DIMENSIONS.** Design's block is 0.20 × 0.10 × 0.05 m, so its three faces
    are 0.020, 0.010 and 0.005 m². The renderer multiplies each face's own
    stated dimensions and refuses a payload where the product does not match
    the declared area — because the whole lesson is that the AREA is what
    changed, and a face whose area does not follow from its dimensions is a
    bench arguing against itself.

    ⚖️ **THE SAND'S LIMIT IS A TEACHING THRESHOLD AND THE PAGE SAYS SO.**
    Fixed at 6000 Pa so that failure is reachable. Real ground has no single
    failure pressure — it varies with grain size, packing and how wet it is,
    and it gives way gradually. The legal line declares it, and the renderer
    asserts that at least one (face, mass) pair clears the limit and at least
    one does not, or half the bench is unauthored.

    ⚠️ **THE WEIGHT ARROW HAS ITS OWN SCALE.** The block is drawn to scale in
    metres; the arrow is drawn in px per newton. They are different
    quantities and one scale for both would be meaningless.

    HOOKS: `data-sand` (wrapper, `data-limit`, `data-scale`, `data-wscale`) ·
    `data-sand-gate` · `data-sand-gopt` · `data-sand-body` ·
    `data-sand-face` (carrying `data-area`, `data-w`, `data-h`, `data-dims`)
    · `data-sand-mass` · `data-sand-block` · `data-sand-line` ·
    `data-sand-was` · `data-sand-shaft` · `data-sand-head` · `data-sand-dim`
    · `data-sand-out` · `data-sand-sub` · `data-sand-note`.
    """
    faces = a.get("faces") or []
    if len(faces) != 3:
        raise ValueError(
            "block-on-sand %r declares %d face(s). One solid has three "
            "different faces to stand on, and the contrast needs all three."
            % (act_id, len(faces)))
    for f in faces:
        w, h = f.get("m_w"), f.get("m_h")
        if not (isinstance(w, (int, float)) and isinstance(h, (int, float))):
            raise ValueError(
                "block-on-sand %r face %r has no footprint dimensions."
                % (act_id, f.get("id")))
        if abs(w * h - float(f.get("area") or 0)) > 1e-9:
            raise ValueError(
                "block-on-sand %r face %r says %s m² but its footprint is "
                "%s × %s = %s m². The lesson's whole claim is that the AREA "
                "is what changed; a face whose area does not follow from its "
                "own dimensions is a bench arguing against itself."
                % (act_id, f.get("id"), f.get("area"), w, h, w * h))

    mass = a.get("mass") or {}
    for k in ("min", "max", "step", "start"):
        if k not in mass:
            raise ValueError("block-on-sand %r mass has no %r." % (act_id, k))
    limit = float(a.get("limit") or 0)
    g = float(a.get("g") or 10)
    if limit <= 0:
        raise ValueError(
            "block-on-sand %r has no giving-way pressure. Without a "
            "threshold the bench reports a number and asks nothing."
            % act_id)

    lo = float(mass["min"]) * g / max(float(f["area"]) for f in faces)
    hi = float(mass["max"]) * g / min(float(f["area"]) for f in faces)
    if hi < limit:
        raise ValueError(
            "block-on-sand %r: the largest pressure reachable is %.0f Pa "
            "against a limit of %.0f Pa, so the sand can never give way and "
            "the whole sinking half of the bench is a dead state."
            % (act_id, hi, limit))
    if lo >= limit:
        raise ValueError(
            "block-on-sand %r: even the smallest pressure, %.0f Pa, is over "
            "the %.0f Pa limit, so the surface never holds."
            % (act_id, lo, limit))

    # ⚠️ THE THREE BRANCH NOTES WERE AUTHORED AND NEVER READ. This drawer
    # took no `branches` key at all, so `p5-01`'s note panel was empty in
    # every state — the JS looks for `[data-sand-branch="…"]` and nothing
    # emitted one. Same defect as `p6-08`'s, found the same way: by reading
    # the built bytes rather than the payload. The three states are the
    # sinking one, the one that holds at any face, and the one that holds
    # only on this face — and the third is the interesting one, so all
    # three are required.
    branches = a.get("branches") or {}
    need = ("sinks", "holds_any", "holds_for_now")
    missing = [k for k in need if not branches.get(k)]
    if missing:
        raise ValueError(
            "block-on-sand %r has no note for state(s) %s. Holding on every "
            "face and holding only on this one are different things to know, "
            "and a bench with one holding note cannot say which it is."
            % (act_id, ", ".join(missing)))
    branch_data = "".join(
        '<span data-sand-branch="%s" data-note="%s" hidden></span>'
        % (e(k), e(branches[k])) for k in need)

    tabs = "".join(
        _seg("ks3-seg-btn ks3-sand-face", f["label"],
             pressed=(i == int(a.get("start_face", 0))),
             data_sand_face=i, data_area=f["area"],
             data_arealabel=f["area_label"], data_w=f["m_w"], data_h=f["m_h"],
             # ⚠️ THE FOOTPRINT AND THE SIDE ELEVATION ARE DIFFERENT
             # RECTANGLES, and drawing one with the other's numbers changes
             # the block's VOLUME as the face is switched — which is the one
             # thing this bench must hold constant. `m_w`/`m_h` are the face
             # ON THE SAND, and their product IS the area the lesson is
             # about; `draw_w`/`draw_h` are what the block looks like from
             # the side, standing on that face. The 0.20 × 0.10 × 0.05 block
             # is 0.20 × 0.05 seen from the side when it is flat, and
             # 0.10 × 0.20 when it is on end. Both were authored from the
             # start and only the footprint pair was emitted, so the drawing
             # showed a block that grew and shrank. `ks3_key_audit` found it
             # the way it was meant to: two authored keys read by nothing.
             data_draww=f["draw_w"], data_drawh=f["draw_h"],
             data_dims=f["dims"], data_name=f["name"])
        for i, f in enumerate(faces))

    # Design's own 1000×600 viewBox (page lines 162–190).
    svg = (
        '<svg class="ks3-sand-svg" viewBox="0 0 1000 600" role="img" '
        'aria-label="" data-sand-alt>'
        '<path class="ks3-sand-grit" d="M60 480 h880 M60 502 h880 '
        'M60 524 h880"/>'
        '<path class="ks3-sand-was" data-sand-was d="M0 0" hidden/>'
        '<path class="ks3-sand-line" data-sand-line d="M60 470 H940"/>'
        '<rect class="ks3-sand-block" data-sand-block x="0" y="0" width="0" '
        'height="0" rx="6"/>'
        '<path class="ks3-sand-shaft" data-sand-shaft d="M0 0"/>'
        '<path class="ks3-sand-head" data-sand-head d="M0 0"/>'
        '<path class="ks3-sand-dim" data-sand-dim d="M0 0"/></svg>')

    fills = "".join(
        '<span class="ks3-sand-fill ks3-sand-%s" data-sand-fill="%s"></span>'
        % (k, k) for k in ("weight", "area", "verdict"))

    lead = ('<p class="ks3-sand-lead">%s</p>'
            % rich(a["lead"]).replace("{limit}", "%s Pa" % int(limit))
            ) if a.get("lead") else ""

    return ('<div class="ks3-sand" data-sand data-limit="%s" data-g="%s" '
            'data-scale="%s" data-wscale="%s" data-base-y="%s" '
            'data-cx="%s" data-start-face="%s">%s%s%s'
            '<div class="ks3-sand-body" data-sand-body hidden>'
            '<div class="ks3-sand-controls">'
            '<div class="ks3-sand-picker"><p class="ks3-sand-pickerlabel">%s'
            '</p><div class="ks3-sand-tabrow">%s</div></div>'
            '<div class="ks3-sand-row"><div class="ks3-sand-rowhead">'
            '<label for="%s-mass">%s</label>'
            '<p class="ks3-sand-reading" data-sand-out="mass">%s kg</p></div>'
            '<input class="ks3-sand-slider" type="range" id="%s-mass" '
            'min="%s" max="%s" step="%s" value="%s" data-sand-mass></div>'
            '</div>'
            '<div class="ks3-sand-figwrap">%s%s</div>%s'
            '<p class="ks3-sand-note" data-sand-note></p>%s</div></div>'
            % (e(int(limit)), e(g), e(a.get("scale", 1400)),
               e(a.get("w_scale", 1.6)), e(a.get("base_y", 470)),
               e(a.get("cx", 420)), e(a.get("start_face", 0)),
               _head("sand", a), lead,
               _gate(act_id, "block-on-sand", a.get("gate") or {}, "sand"),
               t(a.get("face_label", "Face on the sand")), tabs,
               e(act_id), t(mass.get("label", "Mass on the sand")),
               e(mass["start"]), e(act_id), e(mass["min"]), e(mass["max"]),
               e(mass["step"]), e(mass["start"]),
               svg, fills, _tiles("sand", a.get("readouts") or []),
               branch_data))


# ═══ p5-02 · #s-bench · the probe in the tank ════════════════════════════

def r_depth_probe(a, act_id):
    """⊕ p5-02 `#s-bench` — same probe, same liquid, just lower.

    ⚖️ **EVERY BRANCH NAMES THE SAME DEPTH IN ANOTHER LIQUID.** Design's own
    rule for this bench: the liquid is never the only thing that changed. A
    student who moves the probe AND swaps the liquid would otherwise have two
    variables and no way to tell which did what, so every note carries the
    comparison alongside.

    ⚖️ **THE PROBE READS THE LIQUID ALONE — GAUGE PRESSURE.** The atmosphere
    is pressing on the surface as well and adds about 100 000 Pa everywhere
    in the tank. Without that disclosure a reader takes the surface reading
    of 0 Pa as an absolute vacuum, which is the one way this bench can
    actively mislead. The renderer requires the note.

    ⚖️ **THE WEIGHT ABOVE IS DERIVED FROM THE PRESSURE, NOT AUTHORED.** It is
    `pressure × face area`, so the tile and the reading cannot disagree — and
    it comes out right physically: a 2 m column over 0.02 m² is 0.04 m³ of
    water, 40 kg, 400 N, which is what `20 000 Pa × 0.02 m²` gives.

    ⚠️ **THE ROSETTE IS FOUR ARROWS AT THE FACE, ALWAYS.** A liquid presses
    equally in every direction at one depth, and that is `PRESS-07`. The
    drawing says it whatever the depth, including zero.

    HOOKS: `data-dprobe` (wrapper, `data-face`, `data-px-per-m`) ·
    `data-dprobe-gate` · `data-dprobe-gopt` · `data-dprobe-body` ·
    `data-dprobe-liquid` (carrying `data-rho`) · `data-dprobe-depth` ·
    `data-dprobe-col` · `data-dprobe-probe` · `data-dprobe-rosette` ·
    `data-dprobe-dim` · `data-dprobe-out` · `data-dprobe-note`.
    """
    liquids = a.get("liquids") or []
    if len(liquids) < 2:
        raise ValueError(
            "depth-probe %r declares %d liquid(s). Every branch compares the "
            "same depth in another liquid, so there has to be another one."
            % (act_id, len(liquids)))
    _unique(liquids, act_id, "depth-probe", "liquid")
    rhos = {float(x["rho"]) for x in liquids}
    if len(rhos) < 2:
        raise ValueError(
            "depth-probe %r gives every liquid the same density, so the "
            "comparison sentence would say two different names and one "
            "number." % act_id)

    depth = a.get("depth") or {}
    for k in ("min", "max", "step", "start", "per_step"):
        if k not in depth:
            raise ValueError("depth-probe %r depth has no %r." % (act_id, k))
    if not a.get("face"):
        raise ValueError("depth-probe %r has no probe face area." % act_id)

    branches = a.get("branches") or {}
    need = ("surface", "shallow", "deep")
    missing = [k for k in need if not branches.get(k)]
    if missing:
        raise ValueError(
            "depth-probe %r has no note for state(s) %s. The surface is its "
            "own branch because it is the honest zero of the experiment, not "
            "a shallow reading with a small number."
            % (act_id, ", ".join(missing)))

    tabs = "".join(
        _seg("ks3-seg-btn ks3-dprobe-liquid", x["label"],
             pressed=(i == int(a.get("start_liquid", 0))),
             data_dprobe_liquid=i, data_rho=x["rho"], data_name=x["name"])
        for i, x in enumerate(liquids))

    # Design's own 1000×600 viewBox (page lines 150–178).
    svg = (
        '<svg class="ks3-dprobe-svg" viewBox="0 0 1000 600" role="img" '
        'aria-label="" data-dprobe-alt>'
        '<rect class="ks3-dprobe-tank" x="280" y="90" width="600" '
        'height="440" rx="8"/>'
        '<rect class="ks3-dprobe-liquid" x="282" y="92" width="596" '
        'height="436"/>'
        '<rect class="ks3-dprobe-col" data-dprobe-col x="380" y="90" '
        'width="120" height="0"/>'
        '<path class="ks3-dprobe-cable" data-dprobe-cable d="M440 90 V90"/>'
        '<rect class="ks3-dprobe-probe" data-dprobe-probe x="380" y="0" '
        'width="120" height="26" rx="6"/>'
        '<path class="ks3-dprobe-rosette" data-dprobe-rosette d="M0 0"/>'
        '<path class="ks3-dprobe-dim" data-dprobe-dim d="M0 0"/>'
        '<text class="ks3-dprobe-surfacelabel" x="880" y="80" '
        'text-anchor="end">%s</text></svg>'
        % t(a.get("surface_label", "SURFACE")))

    fills = "".join(
        '<span class="ks3-dprobe-fill ks3-dprobe-%s" data-dprobe-fill="%s">'
        '</span>' % (k, k) for k in ("depth", "col", "dir"))

    branch_data = "".join(
        '<span data-dprobe-branch="%s" data-note="%s" hidden></span>'
        % (e(k), e(branches[k])) for k in need)

    lead = ('<p class="ks3-dprobe-lead">%s</p>'
            % rich(a["lead"]).replace("{face}", "%s m²" % a["face"])
            ) if a.get("lead") else ""

    return ('<div class="ks3-dprobe" data-dprobe data-face="%s" '
            'data-px-per-m="%s" data-surface="%s" data-per-step="%s" '
            'data-start-liquid="%s">%s%s%s'
            '<div class="ks3-dprobe-body" data-dprobe-body hidden>'
            '<div class="ks3-dprobe-controls">'
            '<div class="ks3-dprobe-picker">'
            '<p class="ks3-dprobe-pickerlabel">%s</p>'
            '<div class="ks3-dprobe-tabrow">%s</div></div>'
            '<div class="ks3-dprobe-row"><div class="ks3-dprobe-rowhead">'
            '<label for="%s-depth">%s</label>'
            '<p class="ks3-dprobe-reading" data-dprobe-out="depth">—</p>'
            '</div><input class="ks3-dprobe-slider" type="range" '
            'id="%s-depth" min="%s" max="%s" step="%s" value="%s" '
            'data-dprobe-depth></div></div>'
            '<div class="ks3-dprobe-figwrap">%s%s</div>%s'
            '<p class="ks3-dprobe-note" data-dprobe-note></p>%s</div></div>'
            % (e(a["face"]), e(a.get("px_per_m", 90)),
               e(a.get("surface_y", 90)), e(depth["per_step"]),
               e(a.get("start_liquid", 0)),
               _head("dprobe", a), lead,
               _gate(act_id, "depth-probe", a.get("gate") or {}, "dprobe"),
               t(a.get("liquid_label", "What the tank holds")), tabs,
               e(act_id), t(depth.get("label", "Depth of the probe")),
               e(act_id), e(depth["min"]), e(depth["max"]),
               e(depth["step"]), e(depth["start"]),
               svg, fills, _tiles("dprobe", a.get("readouts") or []),
               branch_data))


# ═══ p5-03 · #s-bench · five blocks, one tank ════════════════════════════

def r_float_tank(a, act_id):
    """⊕ p5-03 `#s-bench` — every block is one litre; only the weight changes.

    ⚖️ **ONE LITRE EVERY TIME, AND THAT IS THE CONTROL.** The commit gate
    asks which of pine and steel gets the bigger upthrust, and the answer is
    that they are the same — because each pushes aside one litre. A bench
    where the blocks differed in volume could not ask that question. The
    renderer requires every block to be the same volume and says so.

    ⚖️ **A FLOATER SITS AT `weight ÷ litre` OF ITS DEPTH.** Ice at 0.92 kg
    floats with 92 per cent under, which is the real figure and is why an
    iceberg shows so little. Nothing is fudged: the fraction falls out of the
    weights.

    ⚖️ **A SINKER STILL GETS ITS FULL UPTHRUST, AND THE BALANCE READING SAYS
    SO.** `PRESS-10` is *only things that float get upthrust*, and the tile
    that kills it is the spring-balance reading — weight minus upthrust —
    which is visibly less than the weight in air.

    ⚠️ **THE WEIGHT ARROW IS FIXED AND THE UPTHRUST ARROW IS SCALED AGAINST
    IT**, with a minimum so a small upthrust still draws and a clip so a
    large one still fits. The two compare but neither measures, and Design's
    legal line says exactly that.

    HOOKS: `data-ftank` (wrapper, `data-litre`, `data-warrow`) ·
    `data-ftank-gate` · `data-ftank-gopt` · `data-ftank-body` ·
    `data-ftank-block` (carrying `data-mass`) · `data-ftank-hold` ·
    `data-ftank-box` · `data-ftank-shaft` · `data-ftank-head` ·
    `data-ftank-out` · `data-ftank-note`.
    """
    blocks = a.get("blocks") or []
    if len(blocks) < 4:
        raise ValueError(
            "float-tank %r declares %d block(s). The deck has to hold both "
            "floaters and sinkers, with more than one of each, or the "
            "comparison is a single case." % (act_id, len(blocks)))
    _unique(blocks, act_id, "float-tank", "block")

    litre = float(a.get("litre_n") or 0)
    g = float(a.get("g") or 10)
    if litre <= 0:
        raise ValueError(
            "float-tank %r has no weight for one litre of water. Every "
            "upthrust on this bench is that number." % act_id)

    floaters = [b for b in blocks if float(b["mass"]) * g < litre]
    sinkers = [b for b in blocks if float(b["mass"]) * g >= litre]
    if not floaters or not sinkers:
        raise ValueError(
            "float-tank %r has %d floater(s) and %d sinker(s). The lesson is "
            "the contrast, and a deck that is all one way makes the verdict "
            "tile a constant." % (act_id, len(floaters), len(sinkers)))

    branches = a.get("branches") or {}
    need = ("floating", "held_under", "sinking")
    missing = [k for k in need if not branches.get(k)]
    if missing:
        raise ValueError(
            "float-tank %r has no note for state(s) %s. Held-under is its "
            "own branch because it is the state the hook is about — the "
            "ball that fights you." % (act_id, ", ".join(missing)))

    tabs = "".join(
        _seg("ks3-seg-btn ks3-ftank-block", b["label"],
             pressed=(i == int(a.get("start_block", 0))),
             data_ftank_block=i, data_mass=b["mass"], data_name=b["name"])
        for i, b in enumerate(blocks))

    # Design's own 1000×620 viewBox (page lines 158–184).
    svg = (
        '<svg class="ks3-ftank-svg" viewBox="0 0 1000 620" role="img" '
        'aria-label="" data-ftank-alt>'
        '<rect class="ks3-ftank-tank" x="180" y="120" width="640" '
        'height="440" rx="8"/>'
        '<rect class="ks3-ftank-water" x="182" y="200" width="636" '
        'height="358"/>'
        '<path class="ks3-ftank-surface" d="M182 200 H818"/>'
        '<rect class="ks3-ftank-box" data-ftank-box x="440" y="0" '
        'width="120" height="120" rx="8"/>'
        '<path class="ks3-ftank-shaft ks3-ftank-up" '
        'data-ftank-shaft="up" d="M0 0"/>'
        '<path class="ks3-ftank-head ks3-ftank-up" data-ftank-head="up" '
        'd="M0 0"/>'
        '<path class="ks3-ftank-shaft" data-ftank-shaft="w" d="M0 0"/>'
        '<path class="ks3-ftank-head" data-ftank-head="w" d="M0 0"/>'
        '</svg>')

    # ⊕ MRB-254 · THE "LEFT OVER" CAPTION IS AN HTML SPAN, NOT AN SVG
    # `<text>`. It was a `<text>` at x=500 y=600 filled by JS, and the gate
    # was right to refuse it: an SVG `<text>` that ships empty renders
    # nothing at all to a reader without JavaScript, and nothing a
    # screen-reader can announce from the figure's own accessible name.
    # The remedy is the one Design applied to her own ten bench captions
    # and the one `p4` uses: an overlay span at the matching viewBox
    # percentage, positioned in CSS because this one never moves.
    fills = "".join(
        '<span class="ks3-ftank-fill ks3-ftank-%s" data-ftank-fill="%s">'
        '</span>' % (k, k) for k in ("up", "w", "leftword"))

    branch_data = "".join(
        '<span data-ftank-branch="%s" data-note="%s" hidden></span>'
        % (e(k), e(branches[k])) for k in need)

    lead = ('<p class="ks3-ftank-lead">%s</p>'
            % rich(a["lead"]).replace("{litre}", "%s N" % int(litre))
            ) if a.get("lead") else ""

    return ('<div class="ks3-ftank" data-ftank data-litre="%s" data-g="%s" '
            'data-warrow="%s" data-surface="%s" data-box="%s" '
            'data-start-block="%s">%s%s%s'
            '<div class="ks3-ftank-body" data-ftank-body hidden>'
            '<div class="ks3-ftank-controls">'
            '<div class="ks3-ftank-picker"><p class="ks3-ftank-pickerlabel">'
            '%s</p><div class="ks3-ftank-tabrow">%s</div></div>'
            '<div class="ks3-ftank-picker"><p class="ks3-ftank-pickerlabel">'
            # ⚠️ BOTH LABELS TRAVEL WITH THE BUTTON. The JS used to hardcode
            # "Hold it right under" and "Let it go", so `hold_on` was an
            # authored string read by nothing — which `ks3_key_audit` calls
            # exactly what it is: content that never reaches a student. The
            # words on a control are content, and they are authored here.
            '%s</p><button type="button" class="ks3-seg-btn ks3-ftank-hold" '
            'data-ftank-hold aria-pressed="false" data-on="%s" '
            'data-off="%s">%s</button></div></div>'
            '<div class="ks3-ftank-figwrap">%s%s</div>%s'
            '<p class="ks3-ftank-note" data-ftank-note></p>%s</div></div>'
            % (e(int(litre)), e(g), e(a.get("w_arrow", 120)),
               e(a.get("surface_y", 200)), e(a.get("box_px", 120)),
               e(a.get("start_block", 0)),
               _head("ftank", a), lead,
               _gate(act_id, "float-tank", a.get("gate") or {}, "ftank"),
               t(a.get("block_label", "The block")), tabs,
               t(a.get("hold_label", "Your hand")),
               e(a.get("hold_on", "Let it go")),
               e(a.get("hold_off", "Hold it right under")),
               t(a.get("hold_off", "Hold it right under")),
               svg, fills, _tiles("ftank", a.get("readouts") or []),
               branch_data))


# ═══ p5-04 · #s-bench · up the mountain ══════════════════════════════════

def r_altitude_column(a, act_id):
    """⊕ p5-04 `#s-bench` — same objects, less air above them.

    ⚖️ **SEA LEVEL IS ITS OWN BRANCH BECAUSE IT IS THE STATE EVERYTHING ELSE
    IS COMPARED WITH.** Design gives it a note that names the palm force and
    says why you never notice it; every other height is written as a
    comparison against it. Two branches times three objects covers all
    eighteen states, and the renderer requires both branches and a clause per
    object.

    ⚖️ **THE PRESSURES ARE STANDARD-ATMOSPHERE VALUES AND THE PAGE SAYS SO.**
    Real pressure moves several kilopascals with the weather, which is what
    makes a barometer useful at all. The hedge is what keeps six figures
    honest, and the legal line carries it.

    ⚖️ **THE BANDS ARE UNEQUAL AND THAT IS THE PHYSICS.** Air is squashable,
    so most of its mass is packed into the lowest few kilometres and the
    pressure drops fastest near the ground. `p5-02`'s stack has equal layers
    because water is not. The stack drawer refuses equal bands here.

    ⚠️ **THE BAROMETER NEEDLE IS AN ATTRIBUTE-HOLE ROTATION**, not a redrawn
    path — Design's own note. A rotated `transform` is one attribute; a
    redrawn needle is geometry rebuilt in JS.

    HOOKS: `data-alt` (wrapper, `data-sea`, `data-palm`) ·
    `data-alt-gate` · `data-alt-gopt` · `data-alt-body` · `data-alt-height`
    (carrying `data-kpa`, `data-boil`) · `data-alt-case` · `data-alt-air` ·
    `data-alt-marker` · `data-alt-bag` · `data-alt-pan` · `data-alt-needle`
    · `data-alt-out` · `data-alt-note`.
    """
    alts = a.get("heights") or []
    cases = a.get("cases") or []
    if len(alts) < 4 or len(cases) < 2:
        raise ValueError(
            "altitude-column %r declares %d height(s) and %d case(s)."
            % (act_id, len(alts), len(cases)))
    _unique(cases, act_id, "altitude-column", "case")

    prev = None
    for x in alts:
        if prev is not None and float(x["kpa"]) >= prev:
            raise ValueError(
                "altitude-column %r: pressure does not fall with height at "
                "%s. The whole statement this lesson owns is that "
                "atmospheric pressure DECREASES with increase of height."
                % (act_id, x.get("label")))
        prev = float(x["kpa"])

    branches = a.get("branches") or {}
    if not branches.get("sea") or not branches.get("above"):
        raise ValueError(
            "altitude-column %r needs a `sea` branch and an `above` branch. "
            "Sea level is the state everything else is compared with, so it "
            "is not a height with a small number." % act_id)
    for c in cases:
        if not c.get("clause_sea") or not c.get("clause_above"):
            raise ValueError(
                "altitude-column %r case %r has no clause for one of the two "
                "branches, so some of the eighteen states would carry half a "
                "sentence." % (act_id, c.get("id")))

    height_tabs = "".join(
        _seg("ks3-seg-btn ks3-alt-height", x["label"],
             pressed=(i == int(a.get("start_height", 0))),
             data_alt_height=i, data_kpa=x["kpa"], data_m=x["m"],
             data_boil=x["boil"], data_name=x["name"])
        for i, x in enumerate(alts))
    case_tabs = "".join(
        _seg("ks3-seg-btn ks3-alt-case", c["label"],
             pressed=(i == int(a.get("start_case", 0))),
             data_alt_case=c["id"], data_tile=c["tile"],
             data_clause_sea=c["clause_sea"],
             data_clause_above=c["clause_above"])
        for i, c in enumerate(cases))

    # Design's own 1000×620 viewBox (page lines 154–190).
    svg = (
        '<svg class="ks3-alt-svg" viewBox="0 0 1000 620" role="img" '
        'aria-label="" data-alt-alt>'
        '<rect class="ks3-alt-shaft" x="120" y="40" width="180" '
        'height="520"/>'
        '<rect class="ks3-alt-air" data-alt-air x="122" y="40" width="176" '
        'height="0"/>'
        '<path class="ks3-alt-ground" d="M60 560 H360"/>'
        '<path class="ks3-alt-marker" data-alt-marker d="M0 0"/>'
        '<g data-alt-case-shape="bag" hidden>'
        '<rect class="ks3-alt-bag" data-alt-bag x="0" y="0" width="0" '
        'height="0" rx="16"/>'
        '<path class="ks3-alt-bagseal" data-alt-bagseal d="M0 0"/></g>'
        '<g data-alt-case-shape="pan" hidden>'
        '<rect class="ks3-alt-pan" x="590" y="330" width="220" '
        'height="100" rx="8"/>'
        '<rect class="ks3-alt-panwater" data-alt-panwater x="594" y="0" '
        'width="212" height="0"/>'
        '<path class="ks3-alt-flame" d="M640 450 q20 -30 40 0 '
        'M700 450 q20 -30 40 0 M760 450 q20 -30 40 0"/></g>'
        '<g data-alt-case-shape="baro" hidden>'
        '<circle class="ks3-alt-dial" cx="700" cy="360" r="120"/>'
        '<path class="ks3-alt-needle" data-alt-needle d="M700 360 V262"/>'
        '<circle class="ks3-alt-pin" cx="700" cy="360" r="10"/></g>'
        '</svg>')

    fills = "".join(
        '<span class="ks3-alt-fill ks3-alt-%s" data-alt-fill="%s"></span>'
        % (k, k) for k in ("height", "case"))

    branch_data = "".join(
        '<span data-alt-branch="%s" data-note="%s" hidden></span>'
        % (e(k), e(branches[k])) for k in ("sea", "above"))

    lead = ('<p class="ks3-alt-lead">%s</p>' % rich(a["lead"])
            if a.get("lead") else "")

    return ('<div class="ks3-alt" data-alt data-sea="%s" data-palm="%s" '
            'data-base-y="%s" data-top="%s" data-span="%s" '
            'data-start-height="%s" data-start-case="%s">%s%s%s'
            '<div class="ks3-alt-body" data-alt-body hidden>'
            '<div class="ks3-alt-controls">'
            '<div class="ks3-alt-picker"><p class="ks3-alt-pickerlabel">%s'
            '</p><div class="ks3-alt-tabrow">%s</div></div>'
            '<div class="ks3-alt-picker"><p class="ks3-alt-pickerlabel">%s'
            '</p><div class="ks3-alt-tabrow">%s</div></div></div>'
            '<div class="ks3-alt-figwrap">%s%s</div>%s'
            '<p class="ks3-alt-note" data-alt-note></p>%s</div></div>'
            % (e(a.get("sea_kpa", 101)), e(a.get("palm", 0.01)),
               e(a.get("base_y", 560)), e(a.get("top", 40)),
               e(a.get("span_m", 12000)),
               e(a.get("start_height", 0)),
               e(a.get("start_case", 0)),
               _head("alt", a), lead,
               _gate(act_id, "altitude-column", a.get("gate") or {}, "alt"),
               t(a.get("height_label", "Height above sea level")),
               height_tabs,
               t(a.get("case_label", "What to watch")), case_tabs,
               svg, fills, _tiles("alt", a.get("readouts") or []),
               branch_data))


# ═══ the drawn figures ═══════════════════════════════════════════════════
#
# ⚠️ NONE OF THESE IS A TRIANGLE AND NONE OF THEM CAN BECOME ONE. `p5-01` is
# the unit's only product and it takes the engine's own `r_cover_triangle`;
# every figure below draws a SUM or a DIFFERENCE.
#
# ⚠️ NONE OF THEM HAS COVER BUTTONS EITHER. Design's flag 0a: a part–whole
# bar keeps its buttons because covering a part asks a real question, and a
# stack and a balance do not. Covering a layer of water means nothing.

def _stack(fig, act_id):
    """p5-02 and p5-04 — layers of fluid over one square metre.

    ⚖️ **THE RUNNING TOTAL IS DERIVED, NOT AUTHORED.** Each boundary's figure
    is the sum of the layers above it, computed here, so a stack whose totals
    do not add up cannot be authored. That arithmetic IS the teaching: every
    layer adds its weight to what is below it.

    ⚖️ **`equal` IS A CLAIM ABOUT THE FLUID AND IT IS ASSERTED.** Water is
    very nearly incompressible, so `p5-02`'s five layers are the same depth
    and the same weight. Air is squashable, so `p5-04`'s bands thin towards
    the top and the totals do not step evenly. Drawing air as equal layers
    would say a cubic metre of it at 11 km weighs what one at sea level does.
    """
    layers = fig.get("layers") or []
    if len(layers) < 3:
        raise ValueError(
            "stack %r draws %d layer(s). Fewer than three cannot show a "
            "running total." % (act_id, len(layers)))
    equal = bool(fig.get("equal"))
    weights = [float(x["weight"]) for x in layers]
    if equal and len(set(weights)) != 1:
        raise ValueError(
            "stack %r is declared `equal` but its layers weigh %s. A liquid "
            "is very nearly incompressible, which is what makes the equal "
            "layers true; if these are meant to differ, the stack is a gas "
            "and `equal` is the wrong claim." % (act_id, sorted(set(weights))))
    if not equal and len(set(weights)) == 1:
        raise ValueError(
            "stack %r is not `equal` yet every band weighs the same. A "
            "squashable fluid is drawn with unequal bands precisely because "
            "a cubic metre of it high up does not weigh what one near the "
            "ground does." % act_id)

    X, W, TOP = 30, 230, 24
    total_px = float(fig.get("height_px") or 400)
    span = sum(float(x.get("depth") or 1) for x in layers)
    y = float(TOP)
    body, running = "", 0.0
    for i, L in enumerate(layers):
        h = total_px * (float(L.get("depth") or 1) / span)
        running += float(L["weight"])
        # ⊕ MRB-254 · A BAND WITH NO LABEL DRAWS NO `<text>` AT ALL.
        # Four of p5-04's five bands are deliberately unlabelled — the
        # height-and-pressure total on the right identifies each one, and a
        # second caption inside the band would repeat it. Emitting an empty
        # `<text>` for them shipped four invisible elements, which is
        # exactly what the gate exists to catch. Blank means absent here,
        # never present-and-empty.
        label = ('<text class="ks3-p5fig-layerlabel" x="%.1f" y="%.1f" '
                 'text-anchor="middle">%s</text>'
                 % (X + W / 2.0, y + h / 2.0 + 8, t(L["label"]))
                 ) if L.get("label") else ""
        body += ('<rect class="ks3-p5fig-layer" x="%d" y="%.1f" width="%d" '
                 'height="%.1f"/>%s'
                 '<text class="ks3-p5fig-total" x="%d" y="%.1f">%s</text>'
                 % (X, y, W, h, label, X + W + 18, y + h - 6,
                    t(L.get("total") or fig.get("total_fmt", "%s")
                      % _group(running))))
        y += h
    foot = ('<path class="ks3-p5fig-floor" d="M%d %.1f H%d"/>'
            '<text class="ks3-p5fig-footlabel" x="%.1f" y="%.1f" '
            'text-anchor="middle">%s</text>'
            % (X, y + 16, X + W, X + W / 2.0, y + 38,
               t(fig.get("foot", "1 m² OF FLOOR"))))
    return ('<svg class="ks3-p5fig ks3-p5fig-stack" viewBox="0 0 520 %d" '
            'role="img" aria-label="%s">%s%s</svg>'
            % (int(y + 50), e(fig.get("aria_label", "")), body, foot))


def _group(n):
    """`50000` → `50 000`, with the narrow no-break space Design uses."""
    s = "%d" % round(n)
    if len(s) < 5:
        return s
    out, k = "", 0
    for ch in reversed(s):
        if k and k % 3 == 0:
            out = " " + out
        out = ch + out
        k += 1
    return out


def _opposed_beam(fig, act_id):
    """p5-03 — two panels to one scale: floating, and sinking.

    ⚖️ **BOTH PANELS SHARE A SCALE, OR THE RIGHT-HAND ONE PROVES NOTHING.**
    The claim is that equal-length arrows mean equal forces and that a longer
    one wins. Two panels drawn to fit would show the same numbers and assert
    nothing.

    ⚖️ **THE LEFTOVER IS DERIVED.** `weight − upthrust`, computed here, so
    the third mark cannot disagree with the two arrows it sits between.
    """
    panels = fig.get("panels") or []
    if len(panels) != 2:
        raise ValueError(
            "opposed-beam %r draws %d panel(s); the contrast is two."
            % (act_id, len(panels)))
    scale = float(fig.get("scale") or 0)
    if scale <= 0:
        raise ValueError("opposed-beam %r has no px-per-newton scale."
                         % act_id)

    out = ""
    for i, p in enumerate(panels):
        px = 20 + i * 340
        up = float(p.get("up") or 0)
        w = float(p.get("weight") or 0)
        over = round(w - up, 6)
        cx = px + 160
        out += ('<rect class="ks3-p5fig-panel" x="%d" y="150" width="320" '
                'height="430"/>'
                '<path class="ks3-p5fig-surface" d="M%d 150 H%d"/>'
                '<rect class="ks3-p5fig-box" x="%d" y="%d" width="100" '
                'height="64"/>'
                % (px, px, px + 320, cx - 50, 250 if over > 0 else 118))
        top = 250 if over > 0 else 118
        bot = top + 64
        ulen = up * scale
        wlen = w * scale
        out += ('<path class="ks3-p5fig-shaft" d="M%d %d V%.1f"/>'
                '<path class="ks3-p5fig-head" d="M%d %.1f L%d %.1f L%d %.1f '
                'Z"/>'
                % (cx, top, top - max(4, ulen - 22),
                   cx, top - ulen, cx - 14, top - ulen + 24,
                   cx + 14, top - ulen + 24))
        out += ('<path class="ks3-p5fig-shaft" d="M%d %d V%.1f"/>'
                '<path class="ks3-p5fig-head" d="M%d %.1f L%d %.1f L%d %.1f '
                'Z"/>'
                % (cx, bot, bot + max(4, wlen - 22),
                   cx, bot + wlen, cx - 14, bot + wlen - 24,
                   cx + 14, bot + wlen - 24))
        out += ('<text class="ks3-p5fig-arrowlabel" x="%d" y="%.1f" '
                'text-anchor="middle">%s</text>'
                '<text class="ks3-p5fig-arrowlabel" x="%d" y="%.1f" '
                'text-anchor="middle">%s</text>'
                % (cx, top - ulen - 16, t("UPTHRUST %s N" % p.get("up")),
                   cx, bot + wlen + 30, t("WEIGHT %s N" % p.get("weight"))))
        if over > 0:
            out += ('<path class="ks3-p5fig-over" d="M%d %d V%.1f"/>'
                    '<text class="ks3-p5fig-overlabel" x="%d" y="%.1f">%s'
                    '</text>'
                    % (cx + 84, bot, bot + wlen,
                       cx + 96, bot + wlen / 2.0,
                       t("%s N OVER" % (round(over, 2)))))
        else:
            out += ('<text class="ks3-p5fig-verdict" x="%d" y="330" '
                    'text-anchor="middle">%s</text>'
                    '<text class="ks3-p5fig-verdict" x="%d" y="360" '
                    'text-anchor="middle">%s</text>'
                    % (cx, t(p.get("verdict_a", "EQUAL")),
                       cx, t(p.get("verdict_b", "IT FLOATS"))))
    return ('<svg class="ks3-p5fig ks3-p5fig-opposed" viewBox="0 0 700 620" '
            'role="img" aria-label="%s">%s</svg>'
            % (e(fig.get("aria_label", "")), out))


def r_p5_stack(fig):
    return _stack(fig, fig.get("id"))


def r_p5_opposed_beam(fig):
    return _opposed_beam(fig, fig.get("id"))


# ═══ the CFIFA attempt · #s-formula, under the worked examples ═══════════

def r_p5_attempt(a, act_id):
    """⊕ P5's half of Design's `Cfifa`: the student's own five lines.

    The drawing is `ks3_art.kit.r_cfifa_attempt` — shared with P4 and P6,
    because three copies of one block is how three copies drift. The FAMILY
    is P5's own, so `ks3_art.load()`'s one-family-one-module rule holds and
    the placement gates still see it as this unit's.
    """
    # ⊕ MRB-223 — ONE EYEBROW, NOT TWO. The `check` shell already prints
    # this activity's eyebrow in Design's `.ks3-blockhead`; the kit helper
    # printed it again. `None` tells the helper it is already on the page
    # (the P7 opt-out, applied here after it was measured on live pages).
    return r_cfifa_attempt(dict(a, eyebrow=None), act_id, "p5cfa")


# ═══ registration ════════════════════════════════════════════════════════
#
# ONE ROW PER RENDERER. `ks3_art.check_placements` gate 2 fails a family
# registered and never placed and gate 3 fails one placed and never
# registered. Every family is P5's own — `ks3_art/core.py` is untouched.

ART = {
    'p5-stack':        r_p5_stack,
    'p5-opposed-beam': r_p5_opposed_beam,
}

KIND_SHELL = {
    'block-on-sand':    ("ks3-sand-block-shell",
                         ' data-instrument data-sandblock '
                         'data-stage-done="0"'),
    'depth-probe':      ("ks3-dprobe-block",
                         ' data-instrument data-dprobeblock '
                         'data-stage-done="0"'),
    'float-tank':       ("ks3-ftank-block",
                         ' data-instrument data-ftankblock '
                         'data-stage-done="0"'),
    'altitude-column':  ("ks3-alt-block",
                         ' data-instrument data-altblock '
                         'data-stage-done="0"'),
    'p5-attempt':       ("ks3-p5cfa-block",
                         ' data-instrument data-p5cfablock '
                         'data-stage-done="0"'),
}

KIND_FN = {
    'block-on-sand':    r_block_on_sand,
    'depth-probe':      r_depth_probe,
    'float-tank':       r_float_tank,
    'altitude-column':  r_altitude_column,
    'p5-attempt':       r_p5_attempt,
}
