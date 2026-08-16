# DISPATCH: "band-commit": ("ks3-plate-block", ' data-instrument data-plateblock data-stage-done="0"'),
#
# and in ACTIVITY_KIND_FN, beside the other B3 rows:
#     "band-commit":            r_band_commit,
#
# Place `r_band_commit` at the head of the B3 group (after the B2 rows,
# ~build_ks3.py 7056). Needs `e`, `t`, `rich`.
#
# ⚠️ THIS RENDERER DOES NOT CONSUME `options` OR `reveal`, and it must not
# start to. The block's controls are seven three-way band pickers, which are
# not answer buttons and are not `.ks3-option`; the activity authors neither
# key, so `_kinds_consuming()` correctly leaves both generic branches off.


def r_band_commit(a, act_id):
    """⊕ b3-01 `#s-plate` — commit all seven, then open all seven at once.

    ⚖️ THE GATE IS THE PEDAGOGY. Nothing opens until every one of the seven
    nutrients has been placed in a band, and the lede says why in as many
    words: *a guess you did not make cannot be wrong, and a guess that is never
    wrong teaches you nothing.* A per-row reveal — which is what `job-sort`
    does, and what this looks like from a distance — would let a student read
    row one's answer before committing on row two, and the whole argument of
    the block is that the SPREAD is the surprise. You cannot be surprised by a
    spread you were shown a seventh at a time.

    ⚖️ THE THREE-BRANCH VERDICT, and the branch that must not be dropped.
    NOTES-B3 §3.1 names it: a student who puts all seven in the same band gets
    a verdict that says so. That is the only place in the lesson where the
    target misconception — *balanced means equal amounts* — is read back to the
    student in their own answer rather than in the abstract. `verdicts` takes
    exactly three keys and this renderer raises without all three, because a
    missing branch is invisible: the block still works, it simply stops
    catching the one student it was built for.

    ⚠️ R3 / MRB-196 R10 — READ THIS BEFORE "TIDYING" THE MARKING.
    Nothing here is a `.ks3-option` and nothing takes a marking colour. The
    band buttons keep ONE chosen treatment whether the choice was right or
    wrong, before the reveal and after it; what changes on open is the ROW,
    which gains Design's own dark-ground selected treatment, and the row's why
    panel, which says "You had it" or "Actually tens of grams" in words. There
    is no `--ks3-ok`, no green, no drawn ✓ and no ✕ anywhere in this
    instrument. Design draws it exactly this way on the approved page and the
    distinction is real: the student is being told what the answer WAS, not
    being scored on having found it.

    ⚠️ EVERY TEXT RULE IN THE STYLESHEET IS SCOPED `.ks3-dark …`. This block is
    on ink on Design's page (`ks3-block ks3-dark ks3-practical`), `.ks3-dark p`
    is (0,1,1) and a bare `.ks3-plate-note` is (0,1,0) and loses. See the CSS.

    Emit-both-show-one throughout: all seven why panels, both band verdicts per
    row and all three closing branches are in the document, hidden, and the
    wiring only ever changes which is shown. No authored sentence is rebuilt in
    the browser, so the em dashes, the right single quotes and the `<em>`
    survive intact — and every one of these sentences is science.
    """
    bands = a.get("bands") or []
    if len(bands) < 2:
        raise ValueError(
            "band-commit %r offers %d band(s). The block asks a student to "
            "place a nutrient on a SCALE, and one band is not a scale."
            % (act_id, len(bands)))
    band_by_id = {}
    for i, b in enumerate(bands):
        for key in ("id", "label", "miss_label"):
            if not b.get(key):
                raise ValueError(
                    "band-commit %r band %d is missing %r. `miss_label` is the "
                    "sentence a student who missed this band reads back "
                    "(“Actually tens of grams”); composing it from "
                    "`label` in the browser would lower-case it there and put "
                    "an authored sentence inside the engine."
                    % (act_id, i, key))
        band_by_id[b["id"]] = b

    rows = a.get("rows") or []
    if not rows:
        raise ValueError("band-commit %r declares no rows[]." % act_id)
    for r in rows:
        for key in ("name", "hint", "band", "mass", "why"):
            if not r.get(key):
                raise ValueError(
                    "band-commit %r row %r is missing %r." % (act_id, r.get("name"), key))
        if r["band"] not in band_by_id:
            raise ValueError(
                "band-commit %r row %r sits in band %r, which is not one of "
                "%s. A row whose band no band offers can never be got right, "
                "and the verdict would be unreachable by construction."
                % (act_id, r["name"], r["band"], sorted(band_by_id)))

    verdicts = a.get("verdicts") or {}
    missing = sorted({"all_same", "close", "spread"} - set(verdicts))
    if missing:
        raise ValueError(
            "band-commit %r declares no %s verdict branch. All three are "
            "required: `all_same` is the only place the lesson's target "
            "misconception is named back to the student in their own answer, "
            "and a block that silently drops it still looks finished."
            % (act_id, ", ".join(missing)))

    hit_label = a.get("hit_label")
    if not hit_label:
        raise ValueError(
            "band-commit %r declares no `hit_label`." % act_id)

    row_html = []
    for i, r in enumerate(rows):
        band = band_by_id[r["band"]]
        picks = "".join(
            '<button type="button" class="ks3-plate-band" data-band="%s" '
            'aria-pressed="false">%s</button>' % (e(b["id"]), t(b["label"]))
            for b in bands)
        row_html.append(
            '<li class="ks3-plate-row" data-row="%d" data-answer="%s">'
            '<div class="ks3-plate-head">'
            '<p class="ks3-plate-name">%s</p>'
            '<p class="ks3-plate-hint">%s</p></div>'
            '<div class="ks3-plate-bands">%s</div>'
            '<div class="ks3-plate-why" hidden data-why>'
            '<p class="ks3-plate-real">'
            '<span data-real="hit" hidden>%s</span>'
            '<span data-real="miss" hidden>%s</span>'
            '<span class="ks3-plate-sep" aria-hidden="true"> · </span>'
            '<span class="ks3-plate-mass">%s</span></p>'
            '<p class="ks3-plate-note">%s</p></div></li>'
            % (i, e(r["band"]), t(r["name"]), t(r["hint"]), picks,
               t(hit_label), t(band["miss_label"]), t(r["mass"]),
               rich(r["why"])))

    # The three closing branches, all in the document and all hidden. `data-v`
    # is the branch name and nothing else — the sentences themselves never move
    # through an attribute.
    branches = "".join(
        '<p class="ks3-plate-vwhy" data-v="%s" hidden>%s</p>'
        % (e(k), rich(verdicts[k])) for k in ("all_same", "close", "spread"))

    return ('<div class="ks3-plate" data-plate data-total="%d">'
            '<ul class="ks3-plate-rows" role="list">%s</ul>'
            '<div class="ks3-plate-foot">'
            '<button type="button" class="ks3-reveal-btn ks3-plate-open" '
            'data-plate-open disabled aria-expanded="false">%s</button>'
            '<span class="ks3-plate-count" data-plate-count data-format="%s" '
            'data-done="%s">%s</span></div>'
            '<div class="ks3-plate-verdict" hidden data-plate-verdict>'
            '<p class="ks3-plate-vlabel">%s</p>'
            '<p class="ks3-plate-vhead" data-vhead data-format="%s" '
            'role="status"></p>%s</div></div>'
            % (len(rows), "".join(row_html),
               t(a.get("open_label") or "Show the real amounts"),
               e(a.get("commit_format") or "{n} of {total} committed"),
               e(a.get("commit_done") or "Opened"),
               t((a.get("commit_format") or "{n} of {total} committed")
                 .replace("{n}", "0").replace("{total}", str(len(rows)))),
               t(a.get("verdict_eyebrow") or "Your day, scored"),
               e(a.get("verdict_format") or "{n} of {total} in the right band."),
               branches))
