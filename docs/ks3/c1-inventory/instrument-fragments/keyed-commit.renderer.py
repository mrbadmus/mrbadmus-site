# DISPATCH: "keyed-commit": ("ks3-keyed-block", ' data-instrument data-keyedblock data-stage-done="0"'),
#
# and in `r_activity`, beside the other kind branches:
#     if kind == "keyed-commit":
#         parts.append(r_keyed_commit(a, act_id))
#
# ⚠️ TWO GUARDS ARE REQUIRED IN `r_activity`, and the component is wrong
# without them. This kind owns its whole body — the option list AND the panel —
# so neither of the shell's generic branches may fire on the same payload:
#
#     if a.get("options") and kind != "keyed-commit":
#         parts.append(r_activity_options(a["options"]))
#     ...
#     if a.get("reveal") and kind != "keyed-commit":
#
# Without the first, `r_activity_options` calls `t()` on a dict and renders its
# repr as four answer buttons under the four real ones. Without the second, a
# lesson that spells the static paragraphs `reveal` gets a SECOND
# `.ks3-reveal-panel` that nothing ever unhides — an invisible duplicate of the
# closing prose, which is the worst of the three failure modes because it looks
# fine.
#
# THE SHARED CONTRACT (c1-03 `#s-bubble` and c1-06 `#s-verdict`), so the two
# lessons author the same shape:
#
#     options:       [{text, reply}] × 4    (or commit_options, same shape)
#     answer_index:  int                    validated here, never marked
#     closing:       [str, …]               static paragraphs, after the reply
#
# ⚠️ As delivered, c1-06 spells the last one `closing` and c1-03 spells it
# `reveal`. Both are read here, because the two lessons landed in parallel and
# refusing one would fail the build over a synonym — but ONE of them should
# win at integration and the other be renamed. `closing` is the better name: it
# is not the shell's `reveal` (which is one gated string), it never gates
# anything on its own, and the collision with the shell's key is exactly what
# makes the second guard above necessary.
#
# Place the function next to `r_evidence_bench`. Needs `e`, `t`, `rich`,
# `_option_li`.


def r_keyed_commit(a, act_id):
    """⊕ c1-06 `#s-verdict` · c1-03 `#s-bubble` — one commit, four answers.

    The nearest shipped shape is the generic `predict`, which carries prompt,
    options and ONE reveal string. Here the first paragraph of the reveal is
    the chosen option's own reply and the paragraphs after it are static, so
    the panel says something different to each of four students and then says
    the same thing to all of them. A single `reveal` cannot express that, and
    branching in code (which is what c1-03's page does — three responses keyed
    on the index) puts science-bearing prose inside the engine.

    ⚖️ PAYLOAD-MAP §6.5.2 ruled the c1-06 shape for both: the reply hangs off
    the option. That is what makes a fifth option a data change rather than a
    fifth branch, and it is why c1-03's `{correct, index_3_special_case, other}`
    is expressed as four replies here.

    ⚠️ R3 — NOTHING MARKS. `answer_index` is read at BUILD TIME only, to check
    it is in range and that the option it names carries a reply. It reaches no
    attribute, no class and no student. An activity option shows that it was
    chosen and nothing else; only the ladder marks correctness.

    Emit-both-show-one: all four replies are in the document, hidden, and one
    is unhidden. No authored sentence is rebuilt in JS, and the em dashes and
    `<em>` survive.

    ⚠️ BOTH DRAWN INSTANCES SIT ON INK. `.ks3-dark p` is (0,1,1) and beats a
    bare instrument class at (0,1,0), so every text rule in the stylesheet is
    scoped `.ks3-dark …`. There is a light fallback beside it; see the CSS.
    """
    opts = a.get("options") or a.get("commit_options") or []
    if not opts:
        raise ValueError("keyed-commit %r declares no options[]." % act_id)
    for i, o in enumerate(opts):
        if not isinstance(o, dict):
            raise ValueError(
                "keyed-commit %r option %d is %r, not a {text, reply} record. "
                "This kind takes an option that carries its own answer — that "
                "is the whole difference from a generic `predict`."
                % (act_id, i, type(o).__name__))
        if not o.get("text") or not o.get("reply"):
            raise ValueError(
                "keyed-commit %r option %d needs both `text` and `reply`; a "
                "reply-less option opens an empty panel."% (act_id, i))

    # ⚠️ Read at build time and nowhere else. It names, for the examiner, the
    # option the lesson is arguing for; a drift in the payload that moved the
    # answer past the end of the list would otherwise be silent.
    ans = a.get("answer_index")
    if ans is not None:
        if not isinstance(ans, int) or isinstance(ans, bool):
            raise ValueError(
                "keyed-commit %r answer_index is %r; it is an index into "
                "options[]." % (act_id, ans))
        if not 0 <= ans < len(opts):
            raise ValueError(
                "keyed-commit %r answer_index %d is out of range for %d "
                "option(s)." % (act_id, ans, len(opts)))

    # `reveal` is c1-03's spelling of the same list. See the header: both are
    # read, one should win at integration, and the shell's own `reveal` branch
    # must be guarded either way.
    closing = a.get("closing") or a.get("reveal") or []
    if isinstance(closing, str):
        closing = [closing]

    buttons = "".join(
        _option_li(i, o["text"], ' aria-pressed="false"')
        for i, o in enumerate(opts))

    replies = "".join(
        '<p class="ks3-keyed-reply" data-reply="%d" hidden>%s</p>'
        % (i, rich(o["reply"])) for i, o in enumerate(opts))

    statics = "".join('<p class="ks3-keyed-static">%s</p>' % rich(p)
                      for p in closing)

    return ('<div class="ks3-keyed" data-keyed>'
            '<ul class="ks3-options ks3-keyed-options" role="list">%s</ul>'
            '<div class="ks3-keyed-reveal" hidden data-reveal>%s%s</div>'
            '</div>' % (buttons, replies, statics))
