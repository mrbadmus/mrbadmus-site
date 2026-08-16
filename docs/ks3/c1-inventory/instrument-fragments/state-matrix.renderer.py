# DISPATCH: "state-matrix": ("ks3-smatrix-block", ' data-instrument data-smatrixblock'),
#
# ⚠️ NO `data-stage-done`. Deliberate, and the same shape as `confrontation`'s
# entry: the attribute declares a completion contract, and `#s-matrix` has
# nothing a student can discharge. See the docstring and the lesson module.
#
# Splice `r_state_matrix` into build_ks3.py beside the other C1 instruments, and
# add `if kind == "state-matrix": parts.append(r_state_matrix(a, act_id))` to
# `r_activity`'s dispatch run.


def r_state_matrix(a, act_id):
    """⊕ c1-02 `#s-matrix` — six properties, three states, one row lit.

    ⚠️ NOT `r_comparison`. That is b1-06's shape: a fixed TWO-column "this one
    against that one" table with a dark header row. This is a four-column
    property matrix with a live-highlighted row, and the highlight is driven by
    a DIFFERENT BLOCK's controls. Rendering it as a comparison would give the
    student two columns for a three-state contrast and drop the mechanism
    entirely (map §2.5.2).

    ⊕ CROSS-BLOCK STATE — the first of it in the key stage. No existing KS3
    component reads another block's state, and the temptation is to give this
    one its own copy of squash/paths and keep the two in step. It does not: the
    bench publishes its settings on `[data-sbench]` and the matrix READS them,
    so there is exactly one place the bench's state lives and no way for a
    second copy to drift. `highlight_from` names the section to look in;
    `highlight` maps a bench condition to a row key.

    ⚖️ IT IS NOT A RAIL STOP, and the lesson module does not list it as one.
    Design's stage 3 ticks on `Object.keys(seen).length >= 3` — stage 2's
    predicate, verbatim (page line 648). MRB-208 ruled the rail carries only
    sections that require the student to do something, and this section emits
    no control, no commit and no field: it is an eyebrow, a heading, a lede, a
    table and a footnote. The nearest thing to a demand of its own is the
    highlight, and that is worked from the BENCH's toggles in the bench's
    section — so a predicate over it would reproduce the same defect one
    control-group to the left. `ks3_parity.check_rail_reachable` names this
    exact case in its own docstring; it passes here because the stop is gone,
    not because a borrowed predicate was left in place.

    ⚑ Three of the six rows — `shape`, `volume`, `pour` — can be reached by no
    bench setting whatever, because the highlight answers squash / paths /
    neither and those three rows answer none of them. All six are authored
    anyway: the table is the lesson's reference and the three unreachable rows
    are three of the six answers a student needs. Reported rather than fixed
    with a control Design did not draw (map §2.5.2).
    """
    rows = a.get("rows") or []
    cols = a.get("columns") or []
    if not rows:
        raise ValueError("state-matrix %r declares no rows[]." % act_id)
    if len(cols) < 2:
        raise ValueError(
            "state-matrix %r declares %d column(s); it needs the property "
            "column and one per state." % (act_id, len(cols)))
    # The three state cells are keyed by name rather than by position, because
    # they are authored against a header the author can also see; this asserts
    # the two agree.
    cells = ("solid", "liquid", "gas")
    for r in rows:
        missing = [k for k in ("key", "label") + cells if not r.get(k)]
        if missing:
            raise ValueError(
                "state-matrix %r row %r is missing %s."
                % (act_id, r.get("key") or r.get("label"), ", ".join(missing)))
    if len(cols) != len(cells) + 1:
        raise ValueError(
            "state-matrix %r has %d columns and %d state cells per row; the "
            "header and the body have to describe the same table."
            % (act_id, len(cols), len(cells)))

    by_key = {r["key"]: r for r in rows}
    hl = a.get("highlight") or {}
    for cond in ("squash", "trails", "rest"):
        if hl.get(cond) not in by_key:
            raise ValueError(
                "state-matrix %r highlight[%r] names row %r, which is not one "
                "of %s. A renamed row must be a build error and never a table "
                "that quietly stops lighting."
                % (act_id, cond, hl.get(cond), ", ".join(sorted(by_key))))
    if not a.get("highlight_from"):
        raise ValueError(
            "state-matrix %r authors no `highlight_from`. The lit row is read "
            "off another block's published state and the matrix has to be told "
            "which section to read." % act_id)

    # The RESTING lit row is emitted lit, at build time, by the same rule the
    # runtime uses — squash first, then paths, then neither, and at rest it is
    # neither. Without this the table renders unlit for the instant before
    # `wireStateMatrix` corrects it, which is a wrong picture on screen and a
    # wrong picture in the HTML a search engine reads.
    lit_at_rest = hl["rest"]

    head = "".join('<th scope="col">%s</th>' % t(c) for c in cols)
    body = []
    for r in rows:
        on = r["key"] == lit_at_rest
        body.append(
            '<tr class="ks3-smatrix-row" data-row="%s" data-lit="%s">'
            # ⊕ `aria-current` is an ADDITION inside a component Design drew.
            # Design signals the lit row with `--ks3-accent-tint` and nothing
            # else, so a student who cannot separate the tint from the card is
            # told nothing at all — and the footnote under the table promises
            # them a highlight. R2 says colour is never the only signal on a
            # state. It costs no pixels and changes nothing Design drew.
            '<th scope="row"%s>%s</th>%s</tr>'
            % (e(r["key"]), "1" if on else "0",
               ' aria-current="true"' if on else "",
               t(r["label"]),
               "".join("<td>%s</td>" % t(r[k]) for k in cells)))

    foot = ('<p class="ks3-smatrix-foot">%s</p>' % t(a["footnote"])
            if a.get("footnote") else "")

    return ('<div class="ks3-smatrix" data-smatrix data-from="%s" '
            'data-lit-squash="%s" data-lit-trails="%s" data-lit-rest="%s">'
            '<div class="ks3-smatrix-scroll">'
            '<table class="ks3-smatrix-table">'
            '<thead><tr>%s</tr></thead><tbody>%s</tbody></table></div>%s</div>'
            % (e(a["highlight_from"]), e(hl["squash"]), e(hl["trails"]),
               e(hl["rest"]), head, "".join(body), foot))
