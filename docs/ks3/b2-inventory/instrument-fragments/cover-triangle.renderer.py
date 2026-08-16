# ⚠️ NO DISPATCH ROW — DO NOT ADD ONE, AND DO NOT WRITE THE WORD ABOVE IN
# THE SPLICE MARKER'S OWN SHAPE.
#
# `cover-triangle` is NOT an activity kind and must not become one: it is a
# `formula` BLOCK sub-key, exactly as its bar variant is. There is no
# ACTIVITY_KIND_RENDERERS entry, no ACTIVITY_KIND_FN entry and no
# `data-stage-done` — the block is read, not done, and MRB-208 keeps it off
# the rail.
#
# (This header used to open `# DISPATCH: none. …`. The splice tool matched the
# marker, took the prose after it as a table row and emitted
# `none. \`cover-triangle\` is NOT an activity kind and must not become,` into
# ACTIVITY_KIND_RENDERERS, which is a SyntaxError in build_ks3.py. A marker
# that means "no row" has to not be the marker.)
#
# ── HOW THIS SPLICES, and why it is a widening rather than a fork ─────────
#
# `cover-triangle` already ships in TWO forms and this fragment touches only
# one of them:
#
#   BAR variant      `r_cover_bar(cov)`, reached from `r_formula` via
#                    `block["cover"]` with `shape: "bar"`. c2-06's part–whole
#                    model. **NOT TOUCHED BY THIS FRAGMENT AT ALL** — no line
#                    of `r_cover_bar`, `.ks3-bar-*` or `wireCoverBar` changes,
#                    which is why c2-06 is byte-identical by construction
#                    rather than by inspection.
#   TRIANGLE variant `r_formula_triangle(tri)`, reached from `r_formula` via
#                    `block["triangle"]`. b1-02's magnification triangle ships
#                    it today. THIS is what widens.
#
# ⊕ THE SPLICE IS SELF-APPLYING. Both functions below go in verbatim and
# nothing else in `build_ks3.py` needs touching: `r_formula` is unchanged,
# `_triangle_geometry()` is unchanged, `TRI_W/TRI_H/TRI_PAD/TRI_DIV_Y` are
# unchanged, and the old `r_formula_triangle` at ~1562 can stay exactly where
# it is. The delegate at the foot of this file REBINDS that name, and because
# this fragment lands after it in the module, the later binding is the one
# `r_formula` resolves at call time. The superseded body is then dead code and
# should be deleted in a follow-up tidy — but the splice is correct with it
# still there, which is the property worth having.
#
# ⚠️ b1-02 MUST COME OUT BYTE-IDENTICAL, and the four new keys are what makes
# that true: `result`, `order`, `covered` and a dict-shaped `close` are all
# OPT-IN. b1-02 authors none of them, so every widened branch below collapses
# to the empty string and the emitted markup is the same characters in the same
# order. The evidence is a diff of the built page across the splice, and it is
# in the report.
#
# Place `r_cover_triangle` where `r_formula_triangle` is now (build_ks3.py
# ~1562), immediately after `_triangle_geometry()`. Needs `e`, `t`, `rich`,
# `hashlib` — all already in scope.

_TRI_CELLS = ("top", "left", "right")


def r_cover_triangle(tri, act_id=None):
    """MRB-204 step 2 — the formula drawn as a triangle, in KS3 tokens.

    ⚖️ A TRIANGLE IS THE PRODUCT'S FIGURE. `T = F × d` is a product, so it
    takes this; conservation of mass is a sum and takes the bar. Drawing a sum
    as a triangle — or a product as a beam — teaches a false relationship in
    order to make one rule fit two shapes.

    ⚠️ CORRECTED, AND THE CORRECTION IS INHERITED, NOT NEW. Design's three
    cover boxes overhang the sloping sides (the b1-02 `total` box by about 35
    units at its top edge). It is not a slip and it is not nudgeable: a
    rectangle inside a triangle always overhangs unless it is sized at its own
    narrowest edge, and a box that narrow cannot hold the word it exists to
    hide. The covers are therefore sized to their labels and CLIPPED to the
    triangle path. Both the boxes and the clip are derived from the frame;
    nothing is authored per lesson.

    ── ⊕ WIDENED FOR b2-04, four opt-in keys ────────────────────────────

    `result`   per cell. Design's b2-04 side panel says the ARRANGEMENT in
               display type ("F = T ÷ d") and then says WHY in a sentence.
               b1-02 has only the sentence. Folding the two into one note
               loses the line a student actually reads off the page, and
               emitting the arrangement into the sentence would put maths
               inside prose.
    `order`    the button order. Design's b2-04 is F, T, d — the unknown this
               lesson always solves for comes first — against the
               top/left/right default b1-02 ships.
    `covered`  the cell covered on load, and it is more than a default: a
               triangle that declares one becomes a RADIO. b1-02's toggle
               un-covers on a second press, which is right for a triangle
               being explored and wrong for one whose whole demand is "cover
               the one you want" — an uncovered triangle asks nothing. Both
               interactions are drawn, so both are kept, and the payload is
               what decides which. Emitted as `data-cover-mode="radio"`;
               `wireTriangle` reads it and b1-02, which emits no attribute,
               keeps the toggle.
    `close`    a STRING stays one closing paragraph, exactly as today. A DICT
               takes Design's three trailing blocks — a prose rule, a mono
               unit legend, and the balanced condition in display type. The
               condition is not a fourth arrangement of T, F and d; it is the
               statement that makes every question on the page solvable, and
               that is why Design sets it apart in display type.

    A triangle that authors any `result` also takes Design's TWO-COLUMN row
    (`data-tri-layout="row"`): the figure on the left, the buttons and the
    reading on the right. b1-02's stacked, centred column is untouched — it
    has no side panel to put beside anything.

    ⚠️ EMIT-BOTH-SHOW-ONE for both the notes and the results. Every cell's
    sentence and every cell's arrangement is in the document, hidden, and the
    wiring swaps which pair is shown. Nothing science-bearing is rebuilt in JS,
    so `÷`, `×` and the em dashes survive — which the bar variant's
    `textContent` route cannot promise.
    """
    cells = {k: (tri.get(k) or {}) for k in _TRI_CELLS}
    missing = [k for k in _TRI_CELLS if not cells[k].get("label")]
    if missing:
        raise ValueError(
            "cover-triangle %s has no label on cell(s) %s. All three corners "
            "are drawn and an unlabelled one is a blank corner of a figure."
            % (act_id or tri.get("heading") or "?", ", ".join(missing)))

    # ⊕ WIDENED. All three or none: a side panel that goes blank on one of the
    # three covers is worse than one that never had a result line, and it
    # would only be found by pressing the third button.
    with_result = [k for k in _TRI_CELLS if cells[k].get("result")]
    if with_result and len(with_result) != len(_TRI_CELLS):
        raise ValueError(
            "cover-triangle %s gives a `result` to %s and not to the others. "
            "The result line is a slot in the side panel: covering a cell "
            "that has none would empty it."
            % (act_id or "?", ", ".join(with_result)))
    wide = bool(with_result)

    order = tuple(tri.get("order") or _TRI_CELLS)
    if sorted(order) != sorted(_TRI_CELLS):
        raise ValueError(
            "cover-triangle %s orders its buttons %r; the three cells are %s "
            "and the order names each exactly once."
            % (act_id or "?", list(order), ", ".join(_TRI_CELLS)))

    covered = tri.get("covered")
    if covered is not None and covered not in _TRI_CELLS:
        raise ValueError(
            "cover-triangle %s opens with %r covered; the three cells are %s."
            % (act_id or "?", covered, ", ".join(_TRI_CELLS)))

    g = _triangle_geometry()
    # One triangle per page today; the id is derived from the aria-label so two
    # on one page would still not collide.
    clip_id = "ks3-tri-clip-%s" % hashlib.md5(
        (tri.get("aria_label", "") or "t").encode("utf-8")).hexdigest()[:8]
    ax, ay = g["apex"]
    x1, y1, x2, y2 = g["base"]
    dh = g["div_half"]

    def cover(key):
        x, y, w, h = g[key]
        return ('<rect class="ks3-tri-cover" data-cover="%s" x="%.2f" y="%.2f" '
                'width="%.2f" height="%.2f" rx="8"></rect>'
                % (e(key), x, y, w, h))

    labels = ""
    for key, (lx, ly) in (("top", (ax, TRI_DIV_Y - 42)),
                          ("left", (ax - 44, TRI_DIV_Y + 46)),
                          ("right", (ax + 44, TRI_DIV_Y + 46))):
        labels += ('<text class="ks3-tri-label" x="%.2f" y="%.2f" '
                   'text-anchor="middle">%s</text>'
                   % (lx, ly, t(cells[key].get("label", ""))))

    # ⊕ WIDENED. The pressed state opens on the covered cell rather than on
    # nothing, so the control and the figure agree before a student touches
    # either. With no `covered` every button is `false`, exactly as today.
    btns = "".join(
        '<button type="button" class="ks3-seg-btn ks3-tri-btn" '
        'data-cover="%s" aria-pressed="%s">%s</button>'
        % (e(k), "true" if k == covered else "false",
           t(cells[k].get("button", "")))
        for k in order)

    # ⊕ WIDENED. `hidden` unless this cell is the one covered on load. With no
    # `covered` all three stay hidden, which is today's output.
    notes = "".join(
        '<p class="ks3-tri-note" data-note="%s"%s>%s</p>'
        % (e(k), "" if k == covered else " hidden",
           rich(cells[k].get("text", "")))
        for k in _TRI_CELLS)

    results = "".join(
        '<p class="ks3-tri-result" data-result="%s"%s>%s</p>'
        % (e(k), "" if k == covered else " hidden", t(cells[k]["result"]))
        for k in _TRI_CELLS) if wide else ""

    # ⊕ WIDENED. A string is one paragraph and is what b1-02 authors; a dict is
    # Design's b2-04 stack of three.
    raw_close = tri.get("close")
    if isinstance(raw_close, dict):
        close = ""
        if raw_close.get("rule"):
            close += '<p class="ks3-tri-close">%s</p>' % rich(raw_close["rule"])
        if raw_close.get("units"):
            # `<br>`-joined rather than a list, because it is a legend of three
            # one-line glosses and a bulleted `<ul>` would read as three
            # instructions.
            close += ('<p class="ks3-tri-units">%s</p>'
                      % "<br>".join(t(u) for u in raw_close["units"]))
        if raw_close.get("condition"):
            close += ('<p class="ks3-tri-condition">%s</p>'
                      % t(raw_close["condition"]))
    else:
        close = ('<p class="ks3-tri-close">%s</p>' % rich(raw_close)
                 if raw_close else "")

    root_attrs = ""
    if covered is not None:
        root_attrs += ' data-covered="%s" data-cover-mode="radio"' % e(covered)
    if wide:
        root_attrs += ' data-tri-layout="row"'

    svg = ('<svg class="ks3-tri-svg" viewBox="0 0 %d %d" role="img" '
           'aria-label="%s">'
           '<defs><clipPath id="%s">'
           '<path d="M %.2f %.2f L %.2f %.2f L %.2f %.2f Z"/></clipPath></defs>'
           '<path class="ks3-tri-path" d="M %.2f %.2f L %.2f %.2f L %.2f %.2f Z"/>'
           '<line class="ks3-tri-div" x1="%.2f" y1="%d" x2="%.2f" y2="%d"/>'
           '<line class="ks3-tri-div" x1="%.2f" y1="%d" x2="%.2f" y2="%.2f"/>'
           '%s%s%s</svg>'
           % (TRI_W, TRI_H, e(tri.get("aria_label", "")),
              clip_id, ax, ay, x2, y2, x1, y1,
              ax, ay, x2, y2, x1, y1,
              ax - dh, TRI_DIV_Y, ax + dh, TRI_DIV_Y,
              ax, TRI_DIV_Y, ax, y2,
              labels,
              '<g clip-path="url(#%s)">%s</g>'
              % (clip_id, cover("top") + cover("left") + cover("right")), ""))

    head = ('<p class="ks3-eyebrow">%s</p><p class="ks3-tri-heading">%s</p>'
            % (t(tri.get("eyebrow", "")), t(tri.get("heading", ""))))
    controls = '<div class="ks3-tri-btns">%s</div>' % btns

    if not wide:
        # ⚠️ TODAY'S OUTPUT, CHARACTER FOR CHARACTER. Do not "tidy" this branch
        # into the row one — b1-02 is live and this is the whole byte-identity
        # claim.
        return ('<div class="ks3-triangle" data-triangle%s>%s%s%s%s%s</div>'
                % (root_attrs, head, svg, controls, notes, close))

    return ('<div class="ks3-triangle" data-triangle%s>%s'
            '<div class="ks3-tri-row">%s'
            '<div class="ks3-tri-side">%s%s%s%s</div></div></div>'
            % (root_attrs, head, svg, controls, results, notes, close))


def r_formula_triangle(tri):
    """⊖ SUPERSEDED NAME, kept so nothing above has to change.

    `r_formula` reaches the triangle through this name and b1-02 has shipped
    against it since MRB-204 landed. Rebinding it here rather than renaming
    the call site means the widening is one appended block and zero edits to
    working code — and b1-02 goes through the identical path it always did,
    because `r_cover_triangle` with none of the four opt-in keys emits the
    same characters in the same order.

    The original definition further up the module is now dead and should be
    deleted in a follow-up tidy. It is left in place deliberately for this
    splice: a delete is a change to working code and this pass is meant not
    to be one.
    """
    return r_cover_triangle(tri)
