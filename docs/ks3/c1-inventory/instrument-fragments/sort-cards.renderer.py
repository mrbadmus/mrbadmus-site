# DISPATCH: "sort-cards": ("ks3-sortcards-block", ' data-instrument data-sortcardsblock data-stage-done="0"'),
#
# Splice into build_ks3.py beside the other C1 instruments, plus the dispatch
# line in `r_activity`:
#
#     if kind == "sort-cards":
#         parts.append(r_sort_cards(a, act_id))
#
# ⚠️ It renders INSIDE the `misconception` shell (see ks3_data/c1/__init__.py's
# `_INSTRUMENT_SEGMENTS`), so `r_activity` emits the amber head, then
# `r_confrontation`'s quote, then the lede, then this. Nothing about the
# confrontation path changes.


def r_sort_cards(a, act_id):
    """⊕ c1-03 `#s-think` — four things, and the word that fits each one.

    ⚠️ NOT `verdict-cards` and NOT `job-sort`, and the difference is the whole
    mechanism. Both of those are ONE-SHOT: the first press disables the row's
    other options, because their reveal is an answer and a second press would
    be choosing after reading it. Design's sorter stays open — press Melting,
    read why it is not melting, press Dissolving, and the card follows you.
    That is the page as drawn, and it is also what the lede promises: *"the
    sorting is the point, not the score"*. Locking it would make the block a
    test, which is the thing the sentence says it is not.

    ⚠️ **THIS IS THE ONE PLACE IN C1 WHERE A CARD MARKS THE ANSWER**, and it
    is Design's rule as measured (map §3.5.3, page lines 767–770): the card's
    border goes to `--ks3-accent` when the choice matches and `--ks3-ink` when
    it does not, and the note is ink or accent-text to match. It is carried
    because the page wins over the engine, and it is expressed as ONE
    ATTRIBUTE — `data-verdict` on the card — so that if R3 is ever ruled to
    reach this component the change is two lines of CSS and nothing else
    moves. Note that the marking is never the ok/alert family: it cannot be
    confused with the ladder's verdict, and the wrong state takes exactly the
    neutral ink border every decided `job-sort` row already takes.

    ⚠️ Emit-both-show-one. Each card carries BOTH authored notes, one hidden;
    no sentence is ever assembled in JS from an attribute.
    """
    items = a.get("items") or []
    buttons = a.get("buttons") or []
    if not items:
        raise ValueError("sort-cards %r declares no items[]." % act_id)
    if len(buttons) != 2:
        raise ValueError(
            "sort-cards %r offers %d button(s); it is a binary verdict — one "
            "word against the other — and a third column is a different "
            "component." % (act_id, len(buttons)))
    values = [b.get("value") for b in buttons]
    if len(set(values)) != 2 or not all(values):
        raise ValueError(
            "sort-cards %r buttons need two distinct `value`s; got %r."
            % (act_id, values))
    for it in items:
        # ⚠️ ANSWER VALIDATION, unlike `job-sort` and `verdict-cards` — and it
        # is right here for the reason it is wrong there. Those two answer in
        # free sentences that are deliberately not one of the offered options;
        # this one answers with the button's own value, and the value decides
        # which of the two authored notes a student reads. An answer that
        # matches no button would show every card the wrong note, silently.
        if it.get("answer") not in values:
            raise ValueError(
                "sort-cards %r item %r answers %r, which is not one of the "
                "two buttons %r." % (act_id, it.get("id"), it.get("answer"),
                                     values))
        for side in ("right", "wrong"):
            if not it.get(side):
                raise ValueError(
                    "sort-cards %r item %r has no %r note. Both are authored "
                    "on Design's page and both are read: the card answers the "
                    "choice the student actually made."
                    % (act_id, it.get("id"), side))

    cards = []
    for it in items:
        opts = "".join(
            '<button type="button" class="ks3-seg-btn ks3-sortcards-opt" '
            'data-choice="%s" aria-pressed="false">%s</button>'
            % (e(b["value"]), t(b.get("label", "")))
            for b in buttons)
        cards.append(
            '<div class="ks3-sortcards-card" data-card="%s" data-answer="%s">'
            '<p class="ks3-sortcards-text">%s</p>'
            '<div class="ks3-sortcards-opts">%s</div>'
            '<p class="ks3-sortcards-note" data-note="right" hidden>%s</p>'
            '<p class="ks3-sortcards-note" data-note="wrong" hidden>%s</p>'
            '</div>'
            % (e(it.get("id", "")), e(it["answer"]), rich(it.get("text", "")),
               opts, rich(it["right"]), rich(it["wrong"])))

    # The whole-set summary, gated on all four. It is the payoff for sorting
    # rather than reading, so it does not exist in the document's flow until
    # the sorting is done.
    summary = ""
    if a.get("summary"):
        summary = ('<div class="ks3-sortcards-close" hidden '
                   'data-sortcards-close>%s</div>'
                   % "".join("<p>%s</p>" % rich(p) for p in a["summary"]))

    return ('<div class="ks3-sortcards" data-sortcards data-total="%d">'
            '<div class="ks3-sortcards-grid">%s</div>%s</div>'
            % (len(items), "".join(cards), summary))
