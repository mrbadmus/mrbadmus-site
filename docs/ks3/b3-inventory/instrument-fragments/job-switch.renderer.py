# DISPATCH: "job-switch": ("ks3-jobsw-block", ' data-instrument data-jobswblock data-stage-done="0"'),
#
# and in ACTIVITY_KIND_FN, beside the other B3 rows:
#     "job-switch":             r_job_switch,
#
# Place `r_job_switch` in the B3 group, after `r_fold_builder`. Needs `e`, `t`,
# `rich`.
#
# ⚠️ THIS RENDERER DOES NOT CONSUME `options` OR `reveal`. Its controls are
# five state toggles, not answer buttons; the activity authors neither key, so
# `_kinds_consuming()` correctly leaves both generic branches off.
#
# ── WHY THIS IS NOT A WIDENING OF `system-switch` OR `job-sort` ──────────
#
# NOTES-B3 §3.6 describes it as "the B2 `system-switch` shape with five rows
# and no prediction gate", and that reading was tested against both shipped
# components before a new kind was written. It does not hold, on four measured
# counts, and the fourth is on its own decisive:
#
#   1. `system-switch` is TABBED — one panel visible, chosen by
#      `.ks3-switch-tab`. Here all five rows are on screen at once, because
#      the payoff is a claim about all five TOGETHER and a student cannot see
#      five simultaneous states through a tab strip.
#   2. `system-switch` GATES on a prediction: `wireSwitch` leaves the switch
#      button `disabled` until an option in that panel is pressed. With no
#      options authored, `r_system_switch` still emits `.ks3-switch-predict`
#      with an empty `<ul class="ks3-options">` and the button stays disabled
#      for ever — a dead control, not a narrower version of a live one.
#   3. `system-switch` reveals a LEVELLED CHAIN (`chain[]`, `.ks3-switch-chip`
#      keyed on "Cell"/"Tissue"/"Organ"/"Organism"). B3 job 3 is "harmful
#      species have nowhere to settle", which is an ecological consequence and
#      sits at no level of organisation at all. `show_levels: False` collapses
#      the chip and still demands the chain.
#   4. ⚖️ THE STATE MODEL IS DIFFERENT, and this is the one that settles it.
#      `wireSwitch` and `wireJobSort` are both ONE-WAY and CUMULATIVE — they
#      count panels that have EVER been opened, and `close_all` fires on that
#      count. This block's summary panel is a claim about the configuration
#      the student is looking at RIGHT NOW ("You have just built the germ-free
#      mouse"), so switching a job back on has to take it away again. A
#      component that counts what has happened cannot express a component that
#      reports what is true.
#
# And a fifth, which is about blast radius rather than shape: `system-switch`
# is a LIGHT `.ks3-block` and every `.ks3-switch-*` text rule in
# shared/ks3.css is written for ink on cream. This instrument is ink-dark.
# Widening would mean re-scoping that whole rule set past `.ks3-dark p`, which
# moves b2-01 — a page Mide has already approved — to serve a page he has not
# seen.
#
# `job-sort` was never close: its control is a choice among CATEGORIES with a
# per-row answer, and this block has no answer to give.


def r_job_switch(a, act_id):
    """⊕ b3-08 `#s-jobs` — take one job away and see what breaks.

    ⚖️ THE PAYOFF IS THE WHOLE BLOCK. Five jobs switched off at once IS the
    germ-free mouse from the hook, and the summary panel says so in those
    words. Every other beat here — the five rows, the five consequences, the
    counter — exists to make that one sentence land on a configuration the
    student built themselves rather than on a fact they were told.

    ⚠️ THE GROUND INVERTS, and it is the opposite way round from
    `fold-builder` on the lesson before. There, a level that is ON lights up,
    because the student is building something. Here a job that is STILL BEING
    DONE sits on the panel and a job that has been switched off falls back to
    the block's bare ink with an alert rule round it — the row visibly stops
    being a working part. Two instruments, one control, opposite directions,
    and the direction is the family: b3-07 builds a model up, b3-08 breaks a
    system down.

    ⚠️ NOTHING MARKS. There is no right number of jobs to switch off and no
    `answer_index` to check. The five toggles are `aria-pressed` toggle
    buttons and are deliberately not `.ks3-option`.

    ⚠️ INK-DARK, and the consequence paragraph is CREAM INSIDE IT — the one
    place on this page where ink type sits on the page ground inside an
    ink-dark block. `.ks3-dark p` is (0,1,1) and would paint it
    `--ks3-on-dark-body` #E7DECE on `--ks3-ground` #FBF3E6, which is a 1.1:1
    sentence: present, correct, and unreadable. Every text rule in the
    stylesheet is scoped to at least (0,2,0), and the parity fragment's first
    row is that assertion.

    Emit-both-show-one: all five consequences are in the document, hidden, and
    `wireJobSwitch` unhides them. No authored sentence is rebuilt in JS.
    """
    jobs = a.get("jobs") or []
    if len(jobs) < 2:
        raise ValueError(
            "job-switch %r declares %d job(s). The block's argument is that "
            "the losses ADD UP to one animal, and one loss is not an "
            "accumulation." % (act_id, len(jobs)))
    for j in jobs:
        for key in ("id", "tag", "name", "what", "without"):
            if not j.get(key):
                raise ValueError(
                    "job-switch %r job %r is missing %r. `without` is the "
                    "half that teaches — a job with no stated consequence is "
                    "a label, and the whole method here is switch it off and "
                    "follow what breaks."
                    % (act_id, j.get("id") or j.get("name"), key))

    labels = a.get("labels") or {}
    on_label = labels.get("on")
    off_label = labels.get("off")
    without_label = labels.get("without")
    if not on_label or not off_label:
        raise ValueError(
            "job-switch %r needs `labels.on` and `labels.off` — the button "
            "face is the only thing that says what pressing it will do."
            % act_id)

    # ⚖️ REQUIRED, not defaulted. The summary is what the five rows are for
    # (NOTES-B3 §3.6: "the payoff is the all-five-off summary panel"), and an
    # instrument that could quietly render without it would be five facts and
    # no conclusion.
    summary = a.get("all_off") or {}
    for key in ("tag", "headline", "body"):
        if not summary.get(key):
            raise ValueError(
                "job-switch %r is missing `all_off.%s`. Switching every job "
                "off is the moment the lesson exists for and it may not "
                "arrive silently." % (act_id, key))

    rows = []
    for j in jobs:
        rows.append(
            '<li class="ks3-jobsw-job" data-job="%s" data-off="0">'
            '<div class="ks3-jobsw-main">'
            '<div class="ks3-jobsw-what">'
            '<p class="ks3-jobsw-tag">%s</p>'
            '<p class="ks3-jobsw-name">%s</p>'
            '<p class="ks3-jobsw-does">%s</p></div>'
            '<button type="button" class="ks3-jobsw-toggle" data-jobsw-toggle '
            'aria-pressed="false" data-label-on="%s" data-label-off="%s">%s'
            '</button></div>'
            '<p class="ks3-jobsw-without" hidden data-reveal>'
            '%s%s</p></li>'
            % (e(j["id"]), t(j["tag"]), t(j["name"]), rich(j["what"]),
               e(on_label), e(off_label), t(on_label),
               ('<strong>%s</strong> ' % t(without_label))
               if without_label else "",
               rich(j["without"])))

    return ('<div class="ks3-jobsw" data-jobsw data-total="%d">'
            '<ul class="ks3-jobsw-list" role="list">%s</ul>'
            '<div class="ks3-jobsw-all" hidden data-jobsw-all>'
            '<p class="ks3-jobsw-alltag">%s</p>'
            '<p class="ks3-jobsw-allhead">%s</p>'
            '<p class="ks3-jobsw-allbody">%s</p></div></div>'
            % (len(jobs), "".join(rows), t(summary["tag"]),
               t(summary["headline"]), rich(summary["body"])))
