# DISPATCH: "evidence-bench": ("ks3-ebench-block", ' data-instrument data-ebenchblock data-stage-done="0"'),
#
# and in `r_activity`, beside the other kind branches:
#     if kind == "evidence-bench":
#         parts.append(r_evidence_bench(a, act_id))
#
# Place the function next to `r_claim_switch`. It needs `e`, `t`, `rich` only —
# no gate helper, because this instrument has none (see the docstring).


def r_evidence_bench(a, act_id):
    """⊕ c1-06 `#s-bench` — seven observations, judged one at a time.

    ⚠️ A LIGHT `.ks3-block`, and **NO GATE**. This is the only flagship
    instrument in C1 that is open from the start, and that is deliberate rather
    than an omission: the seven judgements ARE the commitment, so a fourth
    option in front of them would ask the student to commit to committing.
    `r_bench_gate` is not called and must not be added.

    The nearest shipped kinds are `test-board` and `removal-cases`, and both are
    the wrong shape. This is seven BINARY judgements, each with one authored
    verdict on a two-tone panel, plus a whole-set tally that reports how many
    the student called correctly **before** the verdicts opened. Nothing else in
    the key stage scores a call made before a reveal.

    ⚖️ THE TALLY SCORES THE FIRST CALL, NOT THE CURRENT ONE. Design recomputes
    it from live state (`rightCalls`, page line 488), so a student who flips an
    answer after reading the verdict raises a number whose own sentence says
    "before opening the verdict". The buttons stay live — Design leaves them
    live and the verdict does not change when they are pressed again — but the
    scored call is latched on the first press, in `data-called`. That is the
    smallest change that makes the drawn sentence true.

    ⚠️ R3 / MRB-196 R10 — NOTHING HERE MARKS THE STUDENT. The chosen button
    takes the ordinary chosen treatment, the case's border goes to ink, and the
    verdict panel's two grounds are a fact about THE MODEL (`ok`), not about the
    answer. A student who called every one wrong sees exactly the same panels.

    ⚠️ `benchProgress` has two shapes (page line 544): the running count, which
    is `head_counter`'s job, and a bespoke label once the set closes.
    `_head_counter` has no "full" branch, so `progress_all` rides on the
    instrument root and `wireEvidenceBench` writes it into the block-head
    counter. The alternative was retyping "all seven judged" into the engine.
    """
    cases = a.get("cases") or []
    if not cases:
        raise ValueError("evidence-bench %r declares no cases[]." % act_id)

    buttons = a.get("buttons") or {}
    if not (buttons.get("yes") and buttons.get("no")):
        raise ValueError(
            "evidence-bench %r needs buttons={'yes': …, 'no': …}; both labels "
            "are authored and neither has a default worth guessing." % act_id)

    labels = a.get("verdict_labels") or {}
    if not (labels.get("ok") and labels.get("fail")):
        raise ValueError(
            "evidence-bench %r needs verdict_labels={'ok': …, 'fail': …} — the "
            "pair the panel prints above each authored verdict." % act_id)

    tally = a.get("tally") or ""
    if "{n}" not in tally:
        raise ValueError(
            "evidence-bench %r tally carries no {n}: it is the one live number "
            "in the block and the sentence is meaningless without it." % act_id)

    for c in cases:
        if not c.get("id"):
            raise ValueError("evidence-bench %r has a case with no id." % act_id)
        if "ok" not in c:
            raise ValueError(
                "evidence-bench %r case %r declares no `ok`. It decides which "
                "verdict label and which of the two panel grounds the case "
                "takes, and there is no safe default."
                % (act_id, c.get("id")))
        if not c.get("verdict"):
            raise ValueError(
                "evidence-bench %r case %r has no verdict; the panel would open "
                "empty." % (act_id, c.get("id")))

    rows = []
    for c in cases:
        ok = bool(c["ok"])
        rows.append(
            '<div class="ks3-ebench-case" data-case="%s" data-ok="%s">'
            '<div class="ks3-ebench-row">'
            '<div class="ks3-ebench-what">'
            '<p class="ks3-ebench-tag">%s</p>'
            '<p class="ks3-ebench-text">%s</p></div>'
            '<div class="ks3-ebench-btns">'
            '<button type="button" class="ks3-ebench-btn" data-call="1" '
            'aria-pressed="false">%s</button>'
            '<button type="button" class="ks3-ebench-btn" data-call="0" '
            'aria-pressed="false">%s</button>'
            '</div></div>'
            # The verdict is in the document from the start and hidden, not
            # built on demand: the authored sentence carries an em dash and a
            # right single quote, and nothing science-bearing is ever assembled
            # in JS.
            '<div class="ks3-ebench-verdict" hidden data-reveal>'
            '<p class="ks3-ebench-vlabel">%s</p>'
            '<p class="ks3-ebench-vtext">%s</p></div></div>'
            % (e(c["id"]), "1" if ok else "0",
               t(c.get("tag", "")), rich(c.get("text", "")),
               t(buttons["yes"]), t(buttons["no"]),
               t(labels["ok"] if ok else labels["fail"]),
               rich(c["verdict"])))

    # ⚠️ The shared-cause paragraph is STATIC MARKUP, not the tally. NOTES §3
    # flag 9 says "the tally text says so" and it is wrong: the tally is the
    # count line, and the claim the whole C1 → C2 bridge rests on is this
    # paragraph — which is why it is authored prose with an <em> in it and
    # never touched by JS.
    cause = ('<p class="ks3-ebench-cause">%s</p>' % rich(a["shared_cause"])
             if a.get("shared_cause") else "")

    return ('<div class="ks3-ebench" data-ebench data-total="%d" '
            'data-tally="%s" data-all="%s">'
            '<div class="ks3-ebench-list">%s</div>'
            '<div class="ks3-ebench-tally" hidden data-ebench-tally>'
            '<p class="ks3-ebench-tallyline" data-tallyline role="status"></p>'
            '%s</div></div>'
            % (len(cases), e(tally), e(a.get("progress_all") or ""),
               "".join(rows), cause))
