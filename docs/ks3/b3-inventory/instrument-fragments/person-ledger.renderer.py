# DISPATCH: "person-ledger": ("ks3-ledger-block", ' data-instrument data-ledgerblock data-stage-done="0"'),
#
# and in ACTIVITY_KIND_FN, beside the other B3 rows:
#     "person-ledger":          r_person_ledger,
#
# Place `r_person_ledger` after `r_test_bench` in the B3 group. Needs `e`, `t`,
# `rich`.
#
# ⚠️ THIS RENDERER CONSUMES NEITHER `options` NOR `reveal`. The block has no
# commitment to make: it is a ledger, and its argument is made by the student
# moving the person under a plate they have already built.


def r_person_ledger(a, act_id):
    """⊕ b3-03 `#s-ledger` — the requirement is a property of the PERSON.

    ⚖️ THE PERSON IS A CONTROL, NOT A CONSTANT, and that is the whole
    instrument. NOTES-B3 §2 says it in one line: *requirement is a property of
    the person, so the person is a control.* The plate is built once and then
    the person is changed underneath it, and the same food turns from a
    shortfall into a surplus with nothing about the food having moved. A ledger
    with one fixed eater would be a calculator.

    ⚖️ THE MATCH PANEL'S COPY IS THE EXPERIMENT. It appears only within the
    tolerance and it tells the student to switch person **without changing the
    food** — NOTES-B3 §3.3 flags that instruction as the thing that must not be
    lost, because without it a student who lands on a match reads it as having
    finished. `match.why` is required and this renderer raises without it.

    ⚖️ MRB-232 — THIS BLOCK STAYS ON B3'S SIDE OF THE SPLIT. It reports an
    intake, a requirement and the gap between them, all in kJ. It does not
    teach what a joule is, it derives nothing from power and time, and it
    performs no unit conversion: that clause of `KS3.B.NUT.02` belongs to
    Physics P2 and is reached from this lesson by a `references` edge, never by
    prose and never by a control in here. A future pass that adds a kJ↔kcal
    toggle or an energy-transfer readout to this instrument has moved the seam.

    ⚠️ R3 — NOTHING MARKS, AND NOTHING HERE IS AN ANSWER. Twelve food buttons,
    five person tabs and a clear. No `.ks3-option`, no correct plate, no score.
    The bar changes colour at the tolerance because it is a MEASUREMENT
    readout — short, matched, over — and the panel beside it says in words that
    a match is not an achievement but the start of the experiment.

    ⚠️ ON INK. `.ks3-dark p` is (0,1,1); the match panel is CREAM inside the
    ink block and its three paragraphs are the ones that would silently lose.
    Every text rule in the stylesheet is scoped `.ks3-dark …`.

    Every authored sentence is emitted into the document and switched by
    hiding: the five names, the five requirement lines, the five explanations
    and the five match headlines. The only strings assembled at runtime are the
    three that quote a live NUMBER — the total line, the balance line and the
    portion count — and each is one authored template filled with digits, the
    same mechanism `_head_counter` already uses for every counter in the key
    stage.
    """
    people = a.get("people") or []
    if len(people) < 2:
        raise ValueError(
            "person-ledger %r declares %d person(s). The block's argument is "
            "that the same plate means different things to different bodies, "
            "and one body cannot make it." % (act_id, len(people)))
    for p in people:
        for key in ("id", "label", "name", "lower", "why"):
            if not p.get(key):
                raise ValueError(
                    "person-ledger %r person %r is missing %r. `lower` is the "
                    "in-sentence form (“That day matches an Olympic rower in "
                    "training.”); lower-casing `name` at runtime would strip "
                    "the capital from Olympic."
                    % (act_id, p.get("id"), key))
        if not isinstance(p.get("need"), int) or p["need"] <= 0:
            raise ValueError(
                "person-ledger %r person %r has need %r; it is a whole number "
                "of kilojoules per day." % (act_id, p["id"], p.get("need")))

    foods = a.get("foods") or []
    if len(foods) < 2:
        raise ValueError("person-ledger %r declares %d food(s)." % (act_id, len(foods)))
    for f in foods:
        if not f.get("id") or not f.get("name") or not f.get("kj_label"):
            raise ValueError(
                "person-ledger %r food %r needs `id`, `name` and `kj_label`. "
                "`kj_label` is authored rather than composed because the "
                "zero-energy row reads “0 kJ” and every other row reads "
                "“780 kJ each” — a single template would print “0 kJ each”, "
                "which claims a portion size for a glass of water."
                % (act_id, f.get("id")))
        if not isinstance(f.get("kj"), int) or f["kj"] < 0:
            raise ValueError(
                "person-ledger %r food %r has kj %r; it is a whole number of "
                "kilojoules per portion." % (act_id, f["id"], f.get("kj")))

    balance = a.get("balance") or {}
    missing = sorted({"empty", "matched", "surplus", "short"} - set(balance))
    if missing:
        raise ValueError(
            "person-ledger %r declares no %s balance line. All four states are "
            "reachable from the controls, and a state with no sentence is a "
            "readout that goes blank." % (act_id, ", ".join(missing)))
    match = a.get("match") or {}
    if not (match.get("head") and match.get("why")):
        raise ValueError(
            "person-ledger %r declares no match panel. Its copy is the "
            "experiment — *switch person without changing the food* — and "
            "without it a student who lands on a match reads it as having "
            "finished." % act_id)

    def grouped(n):
        """9500 → 9,500. A NUMBER format, applied to no authored text."""
        return "{:,}".format(int(n))

    first = people[0]
    for p in people:
        if p["id"] == a.get("start_person"):
            first = p
            break

    tabs = "".join(
        '<button type="button" class="ks3-ledger-tab" data-person="%s" '
        'data-need="%d" aria-pressed="%s">%s</button>'
        % (e(p["id"]), p["need"], "true" if p is first else "false",
           t(p["label"]))
        for p in people)

    need_fmt = a.get("need_format") or "Needs {need} kJ / day"

    def switched(cls, attr, value_of):
        return "".join(
            '<span class="%s" data-%s="%s"%s>%s</span>'
            % (cls, attr, e(p["id"]), "" if p is first else " hidden",
               value_of(p))
            for p in people)

    names = switched("ks3-ledger-nameval", "pname", lambda p: t(p["name"]))
    needs = switched("ks3-ledger-needval", "pneed",
                     lambda p: t(need_fmt.replace("{need}", grouped(p["need"]))))
    whys = switched("ks3-ledger-whyval", "pwhy", lambda p: rich(p["why"]))

    food_html = "".join(
        '<li><button type="button" class="ks3-ledger-food" data-food="%s" '
        'data-kj="%d" data-count="0">'
        '<span class="ks3-ledger-foodrow">'
        '<span class="ks3-ledger-foodname">%s</span>'
        '<span class="ks3-ledger-foodcount" data-count-label></span></span>'
        '<span class="ks3-ledger-foodkj">%s</span></button></li>'
        % (e(f["id"]), f["kj"], t(f["name"]), t(f["kj_label"]))
        for f in foods)

    heads = "".join(
        '<p class="ks3-ledger-mhead" data-mhead="%s" hidden>%s</p>'
        % (e(p["id"]), t(match["head"].replace("{person}", p["lower"])))
        for p in people)

    portions = a.get("portions") or {}
    total_fmt = a.get("total_format") or "{total} kJ of {need} kJ"

    # ⚠️ The four balance sentences and the two portion sentences ride as
    # attributes, which is the ONE place this instrument does not emit its text
    # as text. They have to: each quotes a number that does not exist until the
    # student has built a plate, so there is no finished string to emit. This is
    # `_head_counter`'s own mechanism — `data-format`, `data-zero`, `data-off`,
    # `data-on` — and it is safe for exactly the reason that is: the strings
    # carry no markup, so `textContent` loses nothing, and `e()` is the
    # attribute escaper. A sentence that carries `<em>` may never travel this
    # way, and none of these does.
    return ('<div class="ks3-ledger" data-ledger data-person="%s" '
            'data-tolerance="%d" data-max="%d" data-count-format="%s">'
            '<div class="ks3-ledger-who">'
            '<p class="ks3-ledger-grouplabel">%s</p>'
            '<div class="ks3-ledger-tabs">%s</div></div>'
            '<div class="ks3-ledger-panel">'
            '<div class="ks3-ledger-head">'
            '<p class="ks3-ledger-name">%s</p>'
            '<p class="ks3-ledger-need">%s</p></div>'
            '<p class="ks3-ledger-why">%s</p>'
            '<div class="ks3-ledger-bar">'
            '<span class="ks3-ledger-fill" data-bar data-state="short"></span>'
            '</div>'
            '<div class="ks3-ledger-figures">'
            '<p class="ks3-ledger-total" data-total data-format="%s">%s</p>'
            '<p class="ks3-ledger-balance" data-balance role="status" '
            'data-empty="%s" data-matched="%s" data-surplus="%s" '
            'data-short="%s">%s</p></div></div>'
            '<p class="ks3-ledger-foodlabel">%s</p>'
            '<ul class="ks3-ledger-foods" role="list">%s</ul>'
            '<div class="ks3-ledger-foot">'
            '<button type="button" class="ks3-reveal-btn ks3-ledger-clear" '
            'data-ledger-clear>%s</button>'
            '<span class="ks3-ledger-portions" data-portions data-empty="%s" '
            'data-format="%s">%s</span></div>'
            '<div class="ks3-ledger-match" hidden data-match>'
            '<p class="ks3-ledger-mlabel">%s</p>%s'
            '<p class="ks3-ledger-mwhy">%s</p></div></div>'
            % (e(first["id"]), int(a.get("tolerance") or 5),
               int(a.get("max_per_food") or 6),
               e(a.get("count_format") or "×{n}"),
               t(a.get("group_label") or "Who is eating"), tabs,
               names, needs, whys,
               e(total_fmt),
               t(total_fmt.replace("{total}", "0")
                 .replace("{need}", grouped(first["need"]))),
               e(balance["empty"]), e(balance["matched"]),
               e(balance["surplus"]), e(balance["short"]),
               t(balance["empty"]),
               t(a.get("food_label") or ""), food_html,
               t(a.get("clear_label") or "Empty the day"),
               e(portions.get("empty") or ""),
               e(portions.get("some") or "{n} portions, {total} kJ"),
               t(portions.get("empty") or ""),
               t(match.get("eyebrow") or ""), heads, rich(match["why"])))
