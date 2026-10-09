#!/usr/bin/env python3
"""ks4_rulings.py — the standing, exact-match rulings on the KS4 pilot delivery.

Same pattern as `student_rulings.py`: every ruling is a documented, MINIMAL,
FAILS-LOUD transformation of Design's own text — never a silent one. A ruling
that stops matching means Design's delivery moved (or was fixed upstream) and
this file needs a human decision, not a wider regex to make it pass quietly.

`build_ks4.py` calls each `apply_*` function at the point in the pipeline
named in its docstring, and prints one line per ruling that actually fired.
Rulings are id'd R1..R8 to match `docs/ks4/pilot-build-contract.md`'s list,
plus the ones the contract named generically but did not spell out (prefixed
`R-`), the two the science examiners raised on 25 Sep 2026 (`R-SLUG`,
`RUNG1-FALLBACK` — the latter is a build-log WARNING, not a rewrite, and its
code lives in build_ks4.py's `check_rung1_fallback()` since it changes
nothing; noted here only so this file's ruling list stays the complete
index), R9 (25 Sep 2026, header badge gating) and R10 (26 Sep 2026, the
tutor CTA — live-audit finding D1). D2 (the same live audit) is a fix to
R-CONNECTS, not a new ruling number.

Mide's ruling (27 Sep 2026, the KS4 polish run): R11 (shared/ks4-lib.js's
`route()` gains the mount-prop-fed fields R12/R14 read), R12 (the header
route chip/switcher, replacing the two static pathway/tier chips), R13
(the two physics lessons' approved exam tips, replacing the never-approved
draft — see §0's flag 11 in the pilot report), R14 (the per-route AQA
spec section number, replacing the Combined-only number on Triple routes).
"""

import re

import ks4_lessons
from theme_head import THEME_SLOT


class RulingError(SystemExit):
    pass


def _require(text, needle, filename, ruling_id, expect=1):
    n = text.count(needle)
    if n != expect:
        raise RulingError(
            "ks4_rulings %s: expected %d occurrence(s) of a fixed string in "
            "%s, found %d. Design's delivery moved; read the diff before "
            "widening this ruling.\n  looking for: %r"
            % (ruling_id, expect, filename, n, needle[:200]))


# ═══════════════════════════════════════════════════════════════════════
# R1 — the Route <select> is a review affordance; the generator renders one
# route per URL and drops the control (contract §1, NOTES-KS4-pilot.md
# §10.6). Applies to every one of the 14 lesson TEMPLATES.
# ═══════════════════════════════════════════════════════════════════════
_ROUTE_SELECT_RE = re.compile(
    r'[ \t]*<label[^>]*>Route\s*<select[\s\S]*?</select>\s*</label>\n?')


def apply_r1_route_selector(design_file, template_text):
    hits = _ROUTE_SELECT_RE.findall(template_text)
    if len(hits) != 1:
        raise RulingError(
            "ks4_rulings R1: %s carries %d Route-selector block(s), expected "
            "exactly 1. Design's delivery moved." % (design_file, len(hits)))
    return _ROUTE_SELECT_RE.sub("", template_text, count=1)


# ═══════════════════════════════════════════════════════════════════════
# R2 — React appears in exactly four places (contract §1). All four call
# `React.createElement('div', {role:'img', 'aria-label':…, style:{maxWidth:…},
# dangerouslySetInnerHTML:{__html:…}})`; each is rewritten to return the
# runtime's figure MARKER object instead — `shared/ks4-runtime.js`'s
# `isFigMarker`/`patchFig` mount it exactly as React would have.
# ═══════════════════════════════════════════════════════════════════════
R2_KS4LIB_FROM = (
    "function fig(svgStr, alt, max) {\n"
    "    if (!svgStr) return null;\n"
    "    return React.createElement('div', { role: 'img', 'aria-label': alt || '', style: { maxWidth: max || '100%' }, dangerouslySetInnerHTML: { __html: svgStr } });\n"
    "  }")
R2_KS4LIB_TO = (
    "function fig(svgStr, alt, max) {\n"
    "    if (!svgStr) return null;\n"
    "    // ⊕ R2 (ks4_rulings.py): React.createElement(...) -> the runtime's figure marker.\n"
    "    return { __mrbFig: true, __html: svgStr, alt: alt || '', max: max || '100%' };\n"
    "  }")


def apply_r2_ks4lib(text):
    _require(text, R2_KS4LIB_FROM, "ks4-lib.js", "R2")
    return text.replace(R2_KS4LIB_FROM, R2_KS4LIB_TO, 1)


R2_CHOICE_FROM = (
    "figure: p.figureSvg ? React.createElement('div', { role: 'img', 'aria-label': p.figureAlt || '', style: { maxWidth: p.figureMax || '640px' }, dangerouslySetInnerHTML: { __html: p.figureSvg } }) : null,")
R2_CHOICE_TO = (
    "figure: p.figureSvg ? { __mrbFig: true, __html: p.figureSvg, alt: p.figureAlt || '', max: p.figureMax || '640px' } : null, // ⊕ R2")


def apply_r2_choice(text):
    _require(text, R2_CHOICE_FROM, "Ks4Choice.dc.html", "R2")
    return text.replace(R2_CHOICE_FROM, R2_CHOICE_TO, 1)


R2_WRITE_FROM = R2_CHOICE_FROM  # byte-identical line in Ks4Write.dc.html


def apply_r2_write(text):
    _require(text, R2_WRITE_FROM, "Ks4Write.dc.html", "R2")
    return text.replace(R2_WRITE_FROM, R2_CHOICE_TO, 1)


R2_LADDER_FROM = (
    "svg(str, alt) { return str ? React.createElement('div', { role: 'img', 'aria-label': alt || '', style: { maxWidth: '640px' }, dangerouslySetInnerHTML: { __html: str } }) : null; }")
R2_LADDER_TO = (
    "svg(str, alt) { return str ? { __mrbFig: true, __html: str, alt: alt || '', max: '640px' } : null; } // ⊕ R2")


def apply_r2_ladder(text):
    _require(text, R2_LADDER_FROM, "Ks4Ladder.dc.html", "R2")
    return text.replace(R2_LADDER_FROM, R2_LADDER_TO, 1)


# ═══════════════════════════════════════════════════════════════════════
# R3 — `KS4.ready()`'s setInterval polling, replaced by synchronous load
# order. VERIFIED AS A NO-OP: no lesson in the pilot calls `KS4.ready(`
# (grepped; zero hits) — every lesson polls `window.KS4 && window.KS4SRC &&
# window.KS4D` itself, inline, inside its OWN `componentDidMount`, which is
# lesson logic that ships verbatim and is untouched by this ruling. Since
# every `<script src>` KS4 needs is already loaded, in order, before the
# page's own mount script runs, that inline poll's first tick always finds
# everything ready — the concern the contract names is already satisfied by
# the page's script order, not by a code change. `ks4-lib.js`'s `ready()`
# function itself is left as delivered (dead code, called by nothing).
# ═══════════════════════════════════════════════════════════════════════
def check_r3_ready_unused(text):
    if "KS4.ready(" in text:
        raise RulingError(
            "ks4_rulings R3: a lesson now calls KS4.ready(), which this "
            "ruling assumed nobody did. Re-examine whether synchronous "
            "script load order still covers it.")


# ═══════════════════════════════════════════════════════════════════════
# R4 — best score / retry storage. VERIFIED AS A NO-OP, not a rewrite.
# Ks4Ladder.dc.html's OWN verbatim logic (ships as-is, a shared BLOCK, not a
# lesson) already keys localStorage as `'ks4-best-' + (this.props.slug ||
# 'x')` via `KS4.load`/`KS4.save` — already KS4-namespaced, already distinct
# from KS3's `ks3_ladder4_<slug>` / `ks3_work_<slug>` keys, and it never
# calls any server-submission endpoint at all. So the contract's storage
# plan (borrow KS3's ks3_ladder4_/ks3_work_ scheme with a ks4_ prefix) and
# its safety concern (never submit a score the backend cannot key by key
# stage) are BOTH already true of the verbatim block, with no code change —
# the "same server submission only if API-CONTRACT.md already lets the
# endpoint distinguish key stages" clause is moot because there IS no
# server submission to gate. Checked, not assumed: the exact string below
# must still be present, or this note is stale.
# ═══════════════════════════════════════════════════════════════════════
R4_LADDER_KEY = "const key = 'ks4-best-' + (this.props.slug || 'x');"


def check_r4_storage_key(text):
    _require(text, R4_LADDER_KEY, "Ks4Ladder.dc.html", "R4")


# ═══════════════════════════════════════════════════════════════════════
# R5 — nanoparticles' spec LABEL. USED TO BE VERIFIED AS A NO-OP: the
# delivered FILENAME still says 5.2.3.3 (frozen — see ks4_lessons/
# __init__.py's comment), and the PAGE ITSELF already showed "AQA Chemistry
# 4.2.4 (chemistry only)" — flag 2 in NOTES-KS4-pilot.md §9 said exactly
# this: "the page shows 4.2.4".
#
# ⊕ D13 (theme-run audit, 27 Sep 2026) — genuinely a real rewrite now, for
# the first time. R14's own docstring names WHY nanoparticles sits outside
# that ruling's lesson set: "its eyebrow/key-note ALREADY show the correct,
# verified 8462 number — nothing to swap." That reasoning has a hole:
# "4.2.4" is the correct SECTION, but nowhere on the page did it ever say
# "8462" — the SPEC CODE its 13 combined/triple siblings all carry
# (`build_ks4.SPEC_TEXT`, every "triple" entry). A pupil reading "AQA
# Chemistry 4.2.4 (chemistry only)" has no way to tell that "4.2.4" is an
# 8462 section rather than, say, an 8464 one — the exact ambiguity R14
# closes everywhere else. Two literals, both in the same template file:
# the eyebrow (`<p class="ks3-eyebrow">`) and the `Ks4KeyNote` `spec="..."`
# attribute. Both get "(8462)" inserted in the same position their
# siblings' equivalent strings carry their own code (right after the
# section number, before any trailing annotation).
# ═══════════════════════════════════════════════════════════════════════
_R5_EYEBROW_FROM = "AQA Chemistry 4.2.4 (chemistry only) · Quantitative"
_R5_EYEBROW_TO = "AQA Chemistry (8462) 4.2.4 (chemistry only) · Quantitative"
_R5_KEYNOTE_FROM = 'spec="AQA 4.2.4 (chemistry only)"'
_R5_KEYNOTE_TO = 'spec="AQA 4.2.4 (8462) (chemistry only)"'


def apply_r5_nanoparticles_spec(text):
    _require(text, _R5_EYEBROW_FROM, "ks4-chemistry-5.2.3.3-nanoparticles.dc.html", "R5 (eyebrow)")
    _require(text, _R5_KEYNOTE_FROM, "ks4-chemistry-5.2.3.3-nanoparticles.dc.html", "R5 (keynote)")
    text = text.replace(_R5_EYEBROW_FROM, _R5_EYEBROW_TO, 1)
    text = text.replace(_R5_KEYNOTE_FROM, _R5_KEYNOTE_TO, 1)
    return text


# ═══════════════════════════════════════════════════════════════════════
# R6 — flag 21 (NOTES-KS4-pilot.md §9): R_total = R₁ + R₂ is a series
# RULE, not one of the 35 AQA equation-sheet equations, and its card in L13
# carried no chip at all (only V = I R, in the sibling card, is chipped
# "Equation sheet"). Mide's instruction (relayed via the contract) is to
# chip it "Not on the sheet · learn it".
# ═══════════════════════════════════════════════════════════════════════
R6_FROM = (
    '<div style="padding: 16px 18px; border-radius: 14px; background: var(--ks3-card); border: 2px solid var(--ks3-option-border);">\n'
    '            <p style="margin: 0; font-family: var(--ks3-font-display); font-weight: 800; font-size: 28px;">R<sub>total</sub> = R₁ + R₂</p>')
R6_TO = (
    '<div style="padding: 16px 18px; border-radius: 14px; background: var(--ks3-card); border: 2px solid var(--ks3-option-border);">\n'
    '            <span style="display: inline-block; margin-bottom: 8px; font-family: var(--ks3-font-mono); font-size: 13px; font-weight: 500; letter-spacing: .06em; text-transform: uppercase; padding: 3px 10px; border-radius: 99px; border: 2px solid var(--ks3-alert-border); color: var(--ks3-ink);">Not on the sheet · learn it</span>\n'
    '            <p style="margin: 0; font-family: var(--ks3-font-display); font-weight: 800; font-size: 28px;">R<sub>total</sub> = R₁ + R₂</p> <!-- ⊕ R6 -->')


def apply_r6_rtotal_chip(text):
    _require(text, R6_FROM, "ks4-physics-6.2.2-series-parallel-circuits.dc.html", "R6")
    return text.replace(R6_FROM, R6_TO, 1)


# ═══════════════════════════════════════════════════════════════════════
# R7 — flag 11: no examiner tip exists for either physics lesson in the
# checked source; Design drafted one in the fixed slot, chipped "Draft ·
# awaiting approval". The contract's instruction is to ship WITHOUT that
# slot until it is approved — a pupil must see no draft chip on a live page.
# The two drafted texts are preserved verbatim in
# docs/ks4/pilot-inventory/draft-exam-tips.md so nothing is lost, only
# hidden from students.
#
# ⊕ SUPERSEDED 27 Sep 2026 (Mide's ruling, R13, below). `apply_r7_remove_
# draft_tip` is kept — the regex it shares with R13 (`_exam_tip_section_re`)
# still has to find the SAME section — but `compile_lesson()` in
# build_ks4.py no longer calls it: it calls `apply_r13_approved_exam_tip`
# instead, which replaces this section with the FINAL approved text rather
# than deleting it. Left defined, not deleted, in case a future lesson
# genuinely needs the old "remove, don't replace" behaviour.
# ═══════════════════════════════════════════════════════════════════════
def _exam_tip_section_re():
    return re.compile(
        r'[ \t]*<section style="margin: 28px 0 0; padding: 20px 22px; '
        r'border-radius: var\(--ks3-r-panel\); background: var\(--ks3-card\); '
        r'border: 2px solid var\(--ks3-ink\);">\s*'
        r'<div style="display: flex; align-items: center; gap: 10px; flex-wrap: wrap;">\s*'
        r'<p style="margin: 0; font-family: var\(--ks3-font-mono\); font-size: 13px; '
        r'font-weight: 500; letter-spacing: \.09em; text-transform: uppercase; '
        r'color: var\(--ks3-accent-text\);">Examiner tip</p>\s*'
        r'<span style="font-family: var\(--ks3-font-mono\); font-size: 12px; '
        r'padding: 2px 9px; border-radius: 99px; border: 2px solid '
        r'var\(--ks3-alert-border\); color: var\(--ks3-ink\);">Draft · awaiting approval</span>\s*'
        r'</div>\s*'
        r'<p style="margin: 8px 0 0; font-size: 19px; line-height: 1\.6;">(?P<tip>.*?)</p>\s*'
        r'</section>\n?', re.S)


def apply_r7_remove_draft_tip(design_file, template_text):
    """Returns (new_text, drafted_tip_text). Removes the whole section."""
    matches = list(_exam_tip_section_re().finditer(template_text))
    if len(matches) != 1:
        raise RulingError(
            "ks4_rulings R7: %s carries %d draft-exam-tip section(s), "
            "expected exactly 1." % (design_file, len(matches)))
    m = matches[0]
    tip_text = m.group("tip")
    new_text = template_text[:m.start()] + template_text[m.end():]
    return new_text, tip_text


# ═══════════════════════════════════════════════════════════════════════
# R8 — flag 17: the hardness-vs-carbon numbers in L11's rung 2 (70/120/155/
# 220, illustrative data-book values) are relabelled "model data" rather
# than presented as measured figures needing an examiner's check.
# ═══════════════════════════════════════════════════════════════════════
R8_FROM = "prompt: 'The table shows the hardness of iron mixed with different percentages of carbon.',"
R8_TO = "prompt: 'The table shows model data for the hardness of iron mixed with different percentages of carbon.', // ⊕ R8"


def apply_r8_model_data(text):
    _require(text, R8_FROM, "ks4-chemistry-5.2.2.7-metals-alloys.dc.html", "R8")
    return text.replace(R8_FROM, R8_TO, 1)


# ═══════════════════════════════════════════════════════════════════════
# R9 — examiner finding (26 Sep 2026): the header "Contains Higher"/
# "Contains Triple" badges are plain unconditional `<span>`s in three
# lessons, unlike the actual tagged CONTENT further down the page (which
# IS correctly wrapped in `sc-if value="{{ isHigher }}"`/`{{ isTriple }}` —
# checked, not assumed). A Foundation pupil on states-of-matter was being
# told the page "Contains Higher" content they cannot see. "Required
# practical · …" (L14 only) is left unconditional on purpose — it names a
# fixed AQA practical, not route-varying content, exactly as the
# coordinator's instruction distinguishes it.
#
#   lesson              badge             gate
#   states-of-matter    Contains Higher   isHigher
#   polymers            Contains Triple   isTriple
#   metals-alloys       Contains Triple   isTriple
# ═══════════════════════════════════════════════════════════════════════
R9_TARGETS = {
    "states-of-matter": ("isHigher", "Contains Higher",
                          "border: 2px solid var(--ks3-stretch); background: var(--ks3-stretch-tint); color: var(--ks3-stretch-text);"),
    "polymers": ("isTriple", "Contains Triple",
                 "border: 2px solid var(--ks3-blue); background: var(--ks3-blue-tint); color: var(--ks3-blue-text);"),
    "metals-alloys": ("isTriple", "Contains Triple",
                       "border: 2px solid var(--ks3-blue); background: var(--ks3-blue-tint); color: var(--ks3-blue-text);"),
}


def apply_r9_badge_gate(site_slug, template_text):
    hit = R9_TARGETS.get(site_slug)
    if hit is None:
        return template_text, False
    flag, label, style_tail = hit
    span_from = ('<span style="font-family: var(--ks3-font-mono); font-size: '
                 '13px; font-weight: 500; letter-spacing: .06em; '
                 'text-transform: uppercase; padding: 4px 11px; '
                 'border-radius: 99px; %s">%s</span>' % (style_tail, label))
    _require(template_text, span_from, site_slug, "R9")
    span_to = '<sc-if value="{{ %s }}">%s</sc-if> <!-- ⊕ R9 -->' % (flag, span_from)
    return template_text.replace(span_from, span_to, 1), True


# ═══════════════════════════════════════════════════════════════════════
# R10 — live-audit finding D1 (26 Sep 2026, docs/ks4/pilot-live-audit.md):
# Ks4End's "Ask about this lesson" CTA is Design's `<a href="#s-ladder">`,
# which just jumps to the ladder anchor. `shared/mrbadmus.v2.js` only opens
# the chat overlay from a `[data-open-chat]` control (grepped: exactly one
# binding, `document.querySelectorAll('[data-open-chat]')...addEventListener
# ('click', open)`), and there is no other such control on a KS4 pilot page
# — so the tutor is loaded and `MrBadmus.init(...)`-ed but UNREACHABLE on
# all 54 pages. `build_ks3.py`'s own lesson-end tutor CTA
# (`tutor_mount()`/§4.8 there) carries exactly this hook, as a real
# `<button type="button">` rather than an anchor — a KS3 gate (`verify_
# ks3.py`) asserts every interactive control on a KS3 page is a real button,
# not a link doing a click's job, and the same reasoning applies here: this
# control performs an action (opens a panel), it does not navigate. Design's
# own class (`ks3-tutor-cta`) and text ("Ask about this lesson") are kept
# byte-identical — only the element and the hook change.
# ═══════════════════════════════════════════════════════════════════════
R10_FROM = '<a class="ks3-tutor-cta" href="#s-ladder">Ask about this lesson</a>'
R10_TO = '<button type="button" class="ks3-tutor-cta" data-open-chat>Ask about this lesson</button> <!-- ⊕ R10 -->'


def apply_r10_tutor_cta(text):
    _require(text, R10_FROM, "Ks4End.dc.html", "R10")
    return text.replace(R10_FROM, R10_TO, 1)


# ═══════════════════════════════════════════════════════════════════════
# R-SLUG — examiner finding (25 Sep 2026): three lessons' internal
# `const slug = '…'` (and the matching `Ks4Ladder slug="…"` template
# attribute, which drives the `ks4-best-<slug>` storage key) do not match
# the SITE slug `shared/ks4-source.js` is generated under. Without this,
# `KS4.find`/`KS4.bank`/`KS4.tip`/`KS4.keyLines`/`KS4.commonMistake` all
# read `window.KS4SRC[design_slug]`, which does not exist in a source file
# keyed by site slug — rung 1, the question bank and the exam tip all come
# back empty. Rewriting the CONSTANT (not aliasing the lookup function) is
# the examiners' preferred fix because it is the one change that makes
# every one of those five call sites correct at once, including the
# storage key, with nothing left depending on which name is "real".
#
#   design slug          site slug (URL/filename)
#   'metals-and-alloys'   'metals-alloys'          (L11)
#   'series-and-parallel' 'series-parallel-circuits' (L13)
#   'resistors-iv'        'resistors'              (L14)
#
# Every OTHER lesson's `const slug` already equals its site slug (verified
# across all 14 by grep before this file was written) — this ruling only
# ever fires on these three.
# ═══════════════════════════════════════════════════════════════════════
SLUG_MISMATCHES = {
    "metals-alloys": "metals-and-alloys",
    "series-parallel-circuits": "series-and-parallel",
    "resistors": "resistors-iv",
}


def apply_r_slug(site_slug, logic_text, template_text):
    design_slug = SLUG_MISMATCHES.get(site_slug)
    if design_slug is None:
        return logic_text, template_text, False
    from_const = "const slug = '%s';" % design_slug
    to_const = "const slug = '%s'; // ⊕ R-SLUG (site slug; was %r)" % (site_slug, design_slug)
    _require(logic_text, from_const, site_slug + " (logic)", "R-SLUG")
    logic_text = logic_text.replace(from_const, to_const, 1)

    from_attr = 'Ks4Ladder" slug="%s"' % design_slug
    to_attr = 'Ks4Ladder" slug="%s"' % site_slug
    _require(template_text, from_attr, site_slug + " (template)", "R-SLUG")
    template_text = template_text.replace(from_attr, to_attr, 1)
    return logic_text, template_text, True


# ═══════════════════════════════════════════════════════════════════════
# R-PREVNEXT — `endPrev`/`endNext` are REPLACED, not just re-pointed.
#
# Design's hardcoded neighbours assume ONE pilot-internal narrative order
# (…nanoparticles → series-and-parallel → resistors-iv, end). The REAL
# per-route order (all_subtopics_physics*.py's own `electricity` topic list)
# puts `resistors` BEFORE `series-parallel-circuits` — the two are reversed
# from what Design assumed, and `series-parallel-circuits`'s real next is
# `direct-alternating-pd`, an UNPORTED lesson outside this pilot entirely.
# Contract §1 requires prev/next "computed exactly as make_pathway_
# subtopic_page does", which settles it: the real per-route order wins, even
# where it disagrees with Design's page and even where it points at a
# lesson this pilot never touched ("old neighbours already link here").
#
# Because a single compiled lesson mounts at up to 4 routes, and prev/next
# genuinely differ BY ROUTE (a Foundation Combined class stops one lesson
# short of Higher Triple's neighbour set), the computed value cannot be a
# JS literal baked into the shared logic text at all — it has to arrive as
# a MOUNT PROP, one Python dict per (lesson, route), computed once by
# `build_ks4.compute_prev_next()` from the same per-route subtopic data
# `shared/ks4-source.js` is generated from. So this ruling does not write a
# real href anywhere; it swaps Design's entire hardcoded object literal for
# a read of `this.props.mrbPrevNext`, which `build_ks4.py` populates per
# page at mount time with `{prev: {href,label}|null, next: {...}|null}`.
# ═══════════════════════════════════════════════════════════════════════
_ENDPREV_RE = re.compile(r"endPrev:\s*(?:\{[^}]*\}|null),?")
_ENDNEXT_RE = re.compile(r"endNext:\s*(?:\{[^}]*\}|null),?")


def apply_r_prevnext(design_file, logic_text):
    n1 = len(_ENDPREV_RE.findall(logic_text))
    n2 = len(_ENDNEXT_RE.findall(logic_text))
    if n1 > 1 or n2 > 1:
        raise RulingError(
            "ks4_rulings R-PREVNEXT: %s carries %d endPrev / %d endNext "
            "literal(s); expected at most one of each." % (design_file, n1, n2))
    logic_text = _ENDPREV_RE.sub("endPrev: this.props.mrbPrevNext.prev,", logic_text)
    logic_text = _ENDNEXT_RE.sub("endNext: this.props.mrbPrevNext.next,", logic_text)
    return logic_text, n1, n2


# ═══════════════════════════════════════════════════════════════════════
# R-CONNECTS — `endConnects` is Design's own curated "related lessons"
# picks, not a sequence — there is no `make_pathway_subtopic_page`
# equivalent to compute it from, so her CHOICE of which lessons to link
# stands. Only the URL is wrong, for the same reason R-PREVNEXT's was: a
# sibling `.dc.html` filename does not exist on the live site. Every
# `.dc.html` cross-reference among the 14 lessons was enumerated by hand (44
# of them, none pointing outside the pilot) and each remaining one (i.e.
# every one NOT already consumed by R-PREVNEXT above) is rewritten to a call
# to `KS4.hrefFor(slug, R)` — a small, documented ADDITION to `shared/
# ks4-lib.js` (Design's page never needed a real href) that builds
# `/{pathway}/{tier}/{subject}/{topic}/{slug}.html` from the CURRENT page's
# route flags `R` (already in scope in every renderVals() as `const R =
# K.route(this)`).
#
# ⊕ D2 fix (26 Sep 2026, docs/ks4/pilot-live-audit.md) — `hrefFor` used to
# FALL BACK to the Triple pathway at the same tier when the target did not
# ship on the current page's pathway (nanoparticles is Triple-only, and
# giant-covalent-structures' `endConnects` links to it). That sent a
# Combined pupil out of their route into chemistry-only content: audit D2,
# the only offender among all 14 lessons' `endConnects` (checked by hand,
# same as the original 44). `hrefFor` (shared/ks4-lib.js, generated by
# `build_ks4.build_ks4_lib_js()`) now returns `null` for an unavailable
# target instead of substituting Triple.
#
# The DROP itself (filtering a null-href entry out of what renders) is done
# in `Ks4End`'s own `renderVals()` — see `apply_r_end_connects_filter` below
# — deliberately NOT here. `apply_r_connects` runs on each of the 14
# LESSONS' own logic text, which is exactly what `ks4_lessons/frozen.json`
# hashes for an examiner-reviewed lesson (docs/ks4/pilot-build-contract.md's
# freeze mechanism: template + logic + source record). Touching that text
# for an engine-only change — no AQA fact, quiz answer or key note differs —
# would move all 14 freeze hashes and read as if 14 examined lessons had
# been silently re-edited. `Ks4End` is a shared BLOCK, compiled separately
# by `compile_block()`, and carries no per-lesson freeze hash at all, so the
# drop lives there instead: same effect, zero freeze impact.
# ═══════════════════════════════════════════════════════════════════════
_HREF_RE = re.compile(r"href: '([\w.\-]+)\.dc\.html'")


def apply_r_connects(design_file, logic_text):
    replaced = []

    def sub(m):
        target_file = m.group(1) + ".dc.html"
        target = ks4_lessons.LESSON_BY_DESIGN_FILE.get(target_file)
        if target is None:
            raise RulingError(
                "ks4_rulings R-CONNECTS: %s links to %r, which is not one "
                "of the 14 pilot lessons. Every cross-reference in this "
                "pilot was checked to stay inside it; a new one needs its "
                "own decision." % (design_file, target_file))
        replaced.append(target["slug"])
        return "href: KS4.hrefFor('%s', R)" % target["slug"]

    new_text = _HREF_RE.sub(sub, logic_text)
    return new_text, replaced


# ═══════════════════════════════════════════════════════════════════════
# D2 fix, continued — Ks4End.dc.html's `renderVals()` passes `p.connects`
# straight through (`connects: p.connects || []`). Once `hrefFor` can
# return null (above), this drops any entry whose href came back null
# before Ks4End's own `<sc-for list="{{ connects }}">` renders it — so on a
# route where the target has no page the "Connects to" list simply has
# fewer items, and on Triple routes (where nanoparticles DOES ship) nothing
# changes. Applied to the ONE shared Ks4End block, not to any lesson.
# ═══════════════════════════════════════════════════════════════════════
R_END_CONNECTS_FROM = "connects: p.connects || [], tutorLine:"
R_END_CONNECTS_TO = ("connects: (p.connects || []).filter(function (c) { "
                      "return !!c.href; }), tutorLine:")


def apply_r_end_connects_filter(text):
    _require(text, R_END_CONNECTS_FROM, "Ks4End.dc.html", "R-CONNECTS (D2 filter)")
    return text.replace(R_END_CONNECTS_FROM, R_END_CONNECTS_TO, 1)


# ═══════════════════════════════════════════════════════════════════════
# R-TUTOR-LABEL — live-audit finding D4 (26 Sep 2026): `build_ks4.tutor_
# block()` reuses `build_ks3.KS3_CHAT_OVERLAY` verbatim (the two chat panels
# are otherwise identical markup/hooks — that reuse is intentional and
# stays), but its subtitle hardcodes "KS3 Science Tutor". The pre-pilot KS4
# lesson pages (generate_site_v5.py) say "GCSE Science Tutor" — grepped and
# confirmed via `git show`. Checked, not assumed: the rest of
# `KS3_CHAT_OVERLAY`'s markup carries no other "KS3" or "Year 7–9" string —
# every other label ("Mr. Badmus AI", "Ask Mr Badmus anything about this
# lesson", the aria-labels) is already key-stage-neutral.
# ═══════════════════════════════════════════════════════════════════════
R_TUTOR_LABEL_FROM = "KS3 Science Tutor"
R_TUTOR_LABEL_TO = "GCSE Science Tutor"


def apply_r_tutor_label(text):
    _require(text, R_TUTOR_LABEL_FROM, "build_ks3.KS3_CHAT_OVERLAY (as reused by build_ks4.tutor_block)", "R-TUTOR-LABEL")
    return text.replace(R_TUTOR_LABEL_FROM, R_TUTOR_LABEL_TO, 1)


# ═══════════════════════════════════════════════════════════════════════
# R-TOPBAR — Stage B of the phone run (28 Sep 2026). Ks4Chrome's whole
# header — `<nav class="ks3-nav" …>` holding Design's retired mark, a
# divider and a four-rung breadcrumb that wraps — is replaced by the ONE
# pupil top bar (topbar.py), the same bar every KS3 page and the leaderboard
# now carry. Measured before: 184px tall at 390px, over four rows.
#
# Matched STRUCTURALLY, not by a byte copy of Design's nav: the nav holds
# KS3's retired mark, and this file carries no copy of it (see R-BRAND). The
# first `<nav class="ks3-nav" style="flex-wrap: wrap; gap: 6px 0;">` up to
# its own `</nav>` (it contains no nested nav), exactly once, and it must
# still carry the breadcrumb, `{{ unit }}` and `{{ title }}` — so a moved or
# redrawn delivery fails here rather than being half-replaced.
#
# The title is `{{ unit }}`, linked to the UNIT's own topic page. ⊕ This
# DEVIATES from the Stage B plan's `/ks4.html`: a link that says "Bonding,
# structure and properties" and lands on the GCSE landing is a link that
# lies. The topic page is `<route dir>.html` — /combined/higher/chemistry/
# bonding/ionic-bonding.html → /combined/higher/chemistry/bonding.html —
# which exists for all 54 pages because generate_site_v5.py writes it for
# every topic. `unitHref` is derived in Ks4Chrome's renderVals from
# `location.pathname`, the only per-route fact the shared block can see
# (one compiled Ks4Chrome serves up to four routes).
#
# ⊖ RETIRES R-BREADCRUMB (the four `href="README.md"` it rewrote are gone
# with the nav), R15 (the theme slot is part of the bar) and R-BRAND's
# chrome half (the bar draws brand.py's lockup). Their functions stay below,
# uncalled, as the record of what they did; R-BRAND's footer half still runs.
# ═══════════════════════════════════════════════════════════════════════
_R_TOPBAR_NAV_RE = re.compile(
    r'<nav class="ks3-nav" style="flex-wrap: wrap; gap: 6px 0;">(?:(?!<nav\b).)*?</nav>', re.S)
R_TOPBAR_UNIT_FROM = "unit: this.props.unit || '',"
R_TOPBAR_UNIT_TO = ("unit: this.props.unit || '', "
                    "unitHref: window.location.pathname.replace(/\\/[^\\/]*$/, '') + '.html',")


def apply_r_topbar(text):
    import topbar
    hits = _R_TOPBAR_NAV_RE.findall(text)
    if len(hits) != 1:
        raise RulingError(
            "ks4_rulings R-TOPBAR: Ks4Chrome.dc.html carries %d header nav(s), "
            "expected exactly 1. Design's delivery moved." % len(hits))
    for must in ('aria-label="Breadcrumb"', "{{ unit }}", "{{ title }}"):
        if must not in hits[0]:
            raise RulingError(
                "ks4_rulings R-TOPBAR: the header nav no longer carries %r — "
                "Design redrew it; read the diff before re-anchoring." % must)
    bar = topbar.topbar("{{ unit }}", "{{ unitHref }}", kind="ks4", host_class="ks3-nav")
    return _R_TOPBAR_NAV_RE.sub(lambda m: bar, text, count=1)


def apply_r_topbar_logic(logic):
    _require(logic, R_TOPBAR_UNIT_FROM, "Ks4Chrome.dc.html (logic)", "R-TOPBAR")
    return logic.replace(R_TOPBAR_UNIT_FROM, R_TOPBAR_UNIT_TO, 1)


# ═══════════════════════════════════════════════════════════════════════
# R-BREADCRUMB — Ks4Chrome's brand link and three breadcrumb links
# (`href="README.md"`) point at Design's local review index, which does not
# exist on the live site. Rewritten to `/ks4.html`, the real GCSE landing
# page, uniformly — a bounded simplification, not full precision: the
# subject/unit crumbs do not deep-link to their own hub/topic page. Noted as
# a Decision in the engine report; a future ruling can make them route-aware
# via the same `KS4.hrefFor`-style helper if that precision is wanted.
# ═══════════════════════════════════════════════════════════════════════
def apply_r_breadcrumb(text):
    _require(text, 'href="README.md"', "Ks4Chrome.dc.html", "R-BREADCRUMB", expect=4)
    return text.replace('href="README.md"', 'href="/ks4.html"')


# ═══════════════════════════════════════════════════════════════════════
# R-BRAND — the one-mark ruling (Mide, 13 Sep 2026; one-mark run 27 Sep
# 2026). Design's Ks4Chrome draws KS3's retired mark — a cream single
# chevron in a 34px accent tile + "MrBadmusAI" — and Ks4End's footer signs
# off "MrBadmusAI · GCSE {{ subject }}". Every page on the site now wears
# ONE lockup, drawn by brand.py and styled by shared/brand/brand.css, and
# says "MrBadmus". Applied to Ks4Chrome AFTER R-BREADCRUMB (so the brand's
# href has already become /ks4.html and R-BREADCRUMB's count of 4 is
# untouched). The old anchor is matched by its href and the retired
# wordmark (its class only as "some ks3- class"), never by the drawing, so
# this file carries no copy of the old mark and the exactly-one count below
# still fails loud if Design's header moves. The lockup's own href is the site root, like every other
# page's.
# ═══════════════════════════════════════════════════════════════════════
_R_BRAND_RE = re.compile(
    r'<a class="ks3-[a-z]+" href="/ks4\.html">(?:(?!</a>).)*?MrBadmusAI</a>', re.S)
R_BRAND_FOOTER_FROM = "<p>MrBadmusAI · GCSE {{ subject }}</p>"
R_BRAND_FOOTER_TO = "<p>MrBadmus · GCSE {{ subject }}</p>"


def apply_r_brand_chrome(text):
    import brand
    hits = _R_BRAND_RE.findall(text)
    if len(hits) != 1:
        raise RulingError(
            "ks4_rulings R-BRAND: Ks4Chrome.dc.html carries %d old brand "
            "anchor(s), expected exactly 1. Design's delivery moved." % len(hits))
    return _R_BRAND_RE.sub(lambda m: brand.brand_lockup("/"), text, count=1)


def apply_r_brand_footer(text):
    _require(text, R_BRAND_FOOTER_FROM, "Ks4End.dc.html", "R-BRAND")
    return text.replace(R_BRAND_FOOTER_FROM, R_BRAND_FOOTER_TO)


# ═══════════════════════════════════════════════════════════════════════
# R11 — Mide's ruling (27 Sep 2026): shared/ks4-lib.js's `route(cmp)` gains
# four fields, all sourced from mount PROPS build_ks4.py now computes per
# (lesson, route) — the same "one route per URL" pattern R-PREVNEXT already
# established for `mrbPrevNext` (contract §1: a value that genuinely
# differs by route cannot be a JS literal baked into the shared logic text,
# because one compiled lesson mounts at up to 4 routes).
#
#   routeWords / routeSwitchOptions — feed R12's header chip/switcher.
#   specEyebrow / specNote          — feed R14's per-route spec citation.
#
# Both mrbRouteSwitch and mrbSpecNote are computed by build_ks4.py from data
# ks4_lessons.LESSONS already carries (routes) or from docs/theme/
# spec-numbers.md's verified table (build_ks4.SPEC_TEXT) — nothing here
# invents a number or a URL; this only surfaces what Python already computed
# onto `R`, which every lesson's `renderVals()` already spreads via
# `Object.assign({}, R, {...})`, so no per-lesson logic edit is needed for
# either feature.
# ═══════════════════════════════════════════════════════════════════════
R11_ROUTE_FN_FROM = (
    "function route(cmp) {\n"
    "    var r = (cmp.state && cmp.state.route) || cmp.props.route || 'Triple Higher';\n"
    "    var f = flags(r);\n"
    "    return { route: r, isHigher: f.higher, isTriple: f.triple, isTH: f.higher && f.triple, notHigher: !f.higher, notTriple: !f.triple,\n"
    "      routeOptions: ROUTES.map(function (x) { return { value: x, label: x }; }),\n"
    "      eqSheetHref: f.triple ? EQ.triple : EQ.combined, eqSheetLabel: (f.triple ? 'GCSE Physics (8463)' : 'Combined Science: Trilogy and Synergy (8464/8465)') + ' · June ' + EQ_YEAR,\n"
    "      onRoute: function (e) { cmp.setState({ route: e.target.value }); } };\n"
    "  }"
)
R11_ROUTE_FN_TO = (
    "function route(cmp) {\n"
    "    var r = (cmp.state && cmp.state.route) || cmp.props.route || 'Triple Higher';\n"
    "    var f = flags(r);\n"
    "    var rs = cmp.props.mrbRouteSwitch || {}; // ⊕ R11\n"
    "    var sn = cmp.props.mrbSpecNote || {}; // ⊕ R11\n"
    "    return { route: r, isHigher: f.higher, isTriple: f.triple, isTH: f.higher && f.triple, notHigher: !f.higher, notTriple: !f.triple,\n"
    "      routeOptions: ROUTES.map(function (x) { return { value: x, label: x }; }),\n"
    "      eqSheetHref: f.triple ? EQ.triple : EQ.combined, eqSheetLabel: (f.triple ? 'GCSE Physics (8463)' : 'Combined Science: Trilogy and Synergy (8464/8465)') + ' · June ' + EQ_YEAR,\n"
    "      onRoute: function (e) { cmp.setState({ route: e.target.value }); },\n"
    "      routeWords: rs.words || r, routeSwitchOptions: rs.options || [],\n"
    "      specEyebrow: sn.eyebrow || '', specNote: sn.keynote || '' };\n"
    "  }"
)


def apply_r11_route_lib(text):
    _require(text, R11_ROUTE_FN_FROM, "ks4-lib.js", "R11")
    return text.replace(R11_ROUTE_FN_FROM, R11_ROUTE_FN_TO, 1)


# ═══════════════════════════════════════════════════════════════════════
# R12 — Mide's ruling (27 Sep 2026): the header's two static "Combined ·
# Triple" / "Foundation · Higher" chips said nothing a pupil didn't already
# know from being on the page — every one of the 54 URLs IS one route. They
# are replaced by ONE chip stating the page's own route in words, built as
# a native <details>/<summary> disclosure: Enter/Space toggles it and Tab
# reaches the menu's plain links with no script at all (the links are
# already in the STATIC, prerendered HTML — R11's routeSwitchOptions is a
# build-time mount prop, not a runtime fetch). shared/ks4-runtime.js adds
# only what native disclosure does not supply on its own: Esc closes the
# switcher and returns focus to the chip, and aria-expanded tracks the open
# state (kept in the runtime because the native 'toggle' event does not
# bubble in every engine — see the comment there).
#
# Nanoparticles carries a DIFFERENT (Triple-only, blue-styled) pathway span
# ("Triple" rather than "Combined · Triple") in place of the standard one;
# both variants are replaced by the same new block — its routeWords/
# routeSwitchOptions mount props already know it ships Triple-only.
# "Contains Higher"/"Contains Triple" (R9) and any "Required practical"
# badge sit AFTER these two spans in every lesson and are untouched.
# ═══════════════════════════════════════════════════════════════════════
_CHIP_STYLE = ('font-family: var(--ks3-font-mono); font-size: 13px; font-weight: 500; '
               'letter-spacing: .06em; text-transform: uppercase; padding: 4px 11px; '
               'border-radius: 99px; border: 2px solid var(--ks3-ink);')
_INDENT10 = "          "
R12_TIER_LINE = '%s<span style="%s">Foundation · Higher</span>\n' % (_INDENT10, _CHIP_STYLE)
R12_PATHWAY_STD_SPAN = '<span style="%s">Combined · Triple</span>' % _CHIP_STYLE
R12_PATHWAY_TRIPLE_SPAN = (
    '<span style="font-family: var(--ks3-font-mono); font-size: 13px; font-weight: 500; '
    'letter-spacing: .06em; text-transform: uppercase; padding: 4px 11px; border-radius: 99px; '
    'border: 2px solid var(--ks3-blue); background: var(--ks3-blue-tint); '
    'color: var(--ks3-blue-text);">Triple</span>')
R12_CHIP_BLOCK = (
    '<details class="ks3-route-switch">\n'
    '            <summary class="ks3-route-chip" aria-expanded="false"><span>{{ routeWords }}</span>'
    '<svg aria-hidden="true" focusable="false" width="12" height="12" viewBox="0 0 12 12">'
    '<path d="M2 4l4 4 4-4" fill="none" stroke="currentColor" stroke-width="1.6" '
    'stroke-linecap="round" stroke-linejoin="round"></path></svg></summary>\n'
    '            <ul class="ks3-route-menu" role="list">\n'
    '              <sc-for list="{{ routeSwitchOptions }}" as="o">'
    '<li><a href="{{ o.href }}">{{ o.label }}</a></li></sc-for>\n'
    '            </ul>\n'
    '          </details>'
)


def apply_r12_route_chip(site_slug, template_text):
    _require(template_text, R12_TIER_LINE, site_slug, "R12 (tier span)")
    template_text = template_text.replace(R12_TIER_LINE, "", 1)
    pathway_span = (R12_PATHWAY_TRIPLE_SPAN if site_slug == "nanoparticles"
                     else R12_PATHWAY_STD_SPAN)
    _require(template_text, pathway_span, site_slug, "R12 (pathway span)")
    return template_text.replace(pathway_span, R12_CHIP_BLOCK, 1)


# ═══════════════════════════════════════════════════════════════════════
# R13 — Mide's ruling (27 Sep 2026): the two physics lessons' draft exam
# tips (flag 11 in the pilot report §0 — never approved, so both lessons
# shipped with NO tip slot at all) are replaced with the FINAL, approved
# text, word for word, in the SAME fixed slot the other 12 lessons use — a
# plain `<section>` reading `{{ examTip }}`, no "Draft · awaiting approval"
# badge. The approved strings are NOT hardcoded here: they live in the ONE
# place every other lesson's tip already lives —
# `all_subtopics_physics_triple_higher.py`'s `examiner_tip` field for these
# two subtopics — so `K.tip(slug)` (shared/ks4-lib.js) serves them exactly
# like every other lesson's tip, on every route (`examiner_tip` is not
# itself route-varying: `build_ks4.build_source_record()` takes every
# non-quiz field from the TRIPLE HIGHER record only).
# ═══════════════════════════════════════════════════════════════════════
R13_APPROVED_SECTION = (
    '<section style="margin: 28px 0 0; padding: 20px 22px; border-radius: var(--ks3-r-panel); '
    'background: var(--ks3-card); border: 2px solid var(--ks3-ink);">\n'
    '        <p style="margin: 0; font-family: var(--ks3-font-mono); font-size: 13px; '
    'font-weight: 500; letter-spacing: .09em; text-transform: uppercase; '
    'color: var(--ks3-accent-text);">Examiner tip</p>\n'
    '        <p style="margin: 8px 0 0; font-size: 19px; line-height: 1.6;">{{ examTip }}</p>\n'
    '      </section>'
)


def apply_r13_approved_exam_tip(design_file, template_text):
    matches = list(_exam_tip_section_re().finditer(template_text))
    if len(matches) != 1:
        raise RulingError(
            "ks4_rulings R13: %s carries %d draft-exam-tip section(s), "
            "expected exactly 1." % (design_file, len(matches)))
    m = matches[0]
    return template_text[:m.start()] + R13_APPROVED_SECTION + template_text[m.end():]


R13_LOGIC_ANCHOR = "railV, theme, ready, draftVisible: this.props.showDraft !== false,"


def apply_r13_exam_tip_logic(design_file, logic_text):
    _require(logic_text, R13_LOGIC_ANCHOR, design_file, "R13 (logic)")
    return logic_text.replace(
        R13_LOGIC_ANCHOR,
        R13_LOGIC_ANCHOR + "\n      examTip: ready ? K.tip(slug) : '', // ⊕ R13", 1)


# ═══════════════════════════════════════════════════════════════════════
# R14 — Mide's ruling (27 Sep 2026): every route used to show the Combined
# Science (8464) spec section number, even on a Triple/separate-science
# route. Triple routes now show the SEPARATE science's own number (8462
# Chemistry / 8463 Physics), verified section by section against the real
# AQA spec PDFs — docs/theme/spec-numbers.md is the citation table this
# ruling is built from; `build_ks4.SPEC_TEXT` is its machine copy.
#
# ⊕ D13 (theme-run audit, 27 Sep 2026) — "Combined routes are byte-identical
# to before" USED to be true here and is no longer: the literal text still
# moves from the template into `build_ks4.SPEC_TEXT[slug]["combined"]`
# unchanged BY THIS FUNCTION, but that dict's own "combined" values now
# carry "(8464)" where they used to carry nothing — Mide's ruling that the
# eyebrow/key-note should say WHICH spec a Combined pupil is reading, the
# same as a Triple pupil's page already did. This function's job (require
# the OLD literal, swap in the placeholder) is unaffected either way: it
# only cares that the literal it is told to find is still there, not what
# the machine-copy dict resolves the placeholder to afterwards.
#
# Nanoparticles is NOT in this ruling's lesson set: it has no Combined route
# at all (8462 §4.2.4 is chemistry-only), and its eyebrow/key-note ALREADY
# show the correct, verified 8462 number — nothing to swap.
# ═══════════════════════════════════════════════════════════════════════
def apply_r14_spec_number(site_slug, template_text, eyebrow_literal, keynote_literal):
    tpl = template_text
    eyebrow_from = '<p class="ks3-eyebrow">%s</p>' % eyebrow_literal
    _require(tpl, eyebrow_from, site_slug, "R14 (eyebrow)")
    tpl = tpl.replace(eyebrow_from, '<p class="ks3-eyebrow">{{ specEyebrow }}</p>', 1)
    keynote_from = 'spec="%s"' % keynote_literal
    _require(tpl, keynote_from, site_slug, "R14 (keynote)")
    tpl = tpl.replace(keynote_from, 'spec="{{ specNote }}"', 1)
    return tpl


# ═══════════════════════════════════════════════════════════════════════
# R15 — theme run (Mide's ruling 26 Sep 2026, THEME-CONTRACT.md): every page
# on the site carries a Light/Dark/System control. On these 54 pages the
# control goes into the SAME flex row R12's route chip lives in — the
# header's `<div style="margin-top: 16px; display: flex; flex-wrap: wrap;
# align-items: center; gap: 8px 10px;">` — because that row is already the
# lesson header's "status strip" and already carried the removed Route
# <select> at its right-hand end (R1, `margin-left: auto`). The slot takes
# over that same right-hand position: `margin-left:auto` on a flex child
# pushes ONLY itself (and nothing after it) to the row's far right, so it
# must be the row's LAST child — true for all 14 lessons at this point in
# the pipeline (R1 already removed the only other `margin-left:auto`
# element; R12's chip and R9's conditional badge, when present, both sit
# BEFORE this position, never after).
#
# Runs LAST of the header-row rulings (after R12, after R9) precisely so
# it lands after whatever they left behind — this function does not search
# for R12's chip or R9's badge by name, it anchors on the row's own opening
# `<div style=...>` tag (byte-identical across all 14 lessons, verified by
# grep) and inserts right before that div's own closing `</div>` (the first
# `</div>` after the opening tag — safe because nothing this ruling's
# predecessors leave inside that row is itself a `<div>`: R12's chip is a
# `<details>/<summary>/<ul>`, R9's badge is a `<span>` inside an `<sc-if>`).
#
# THEME_SLOT itself (`theme_head.THEME_SLOT`) is used byte-identical, per
# THEME-CONTRACT.md's "import these; never retype the snippet" — only the
# WRAPPER around it (for right-alignment in this specific flex row) is
# page-family-specific, exactly as different families position it
# differently in their own headers.
# ⊕ D11 (theme-run audit, 27 Sep 2026) — MOVED, not duplicated. R15 used to
# insert the theme slot into the LESSON's own header status-strip row (the
# `<div>` below, shared with R12's route chip) — which put the control
# inside the HERO, at y≈514 (1280px) / y≈658–733 (phone), rather than in
# the page's actual top header. Every other family on the site keeps the
# control in the SITE HEADER (the bar, or the drawer's Theme row) — the
# one place a pupil learns to look for it, on every OTHER page they read.
# The pilot's own header IS a real header row: Ks4Chrome's `<nav
# class="ks3-nav">` (brand + breadcrumb, shared across all 54 pages,
# compiled ONCE in `build_ks4.compile_block()` rather than per-lesson) —
# it simply never carried the slot before. `.ks3-nav` is `display:flex`
# in the bundle these pages load (`shared/ks4-ds.css`), which already has
# its own `margin-left:auto` idiom for "push to the row's far right"
# (`.ks3-nav-link`) — this reuses that exact idiom rather than inventing a
# second one. Moving it here also means one insertion point instead of
# fourteen: every lesson gets the control from the ONE shared Ks4Chrome
# block, so a future 15th lesson needs nothing added for this.
R15_CHROME_NAV_ANCHOR = (
    '<li aria-current="page" style="color: var(--ks3-ink-muted); '
    'font-weight: 500;">{{ title }}</li>\n    </ol>\n  </nav>'
)
R15_THEME_SLOT_WRAPPED = (
    '<span style="margin-left:auto;display:inline-flex;align-items:center;">'
    + THEME_SLOT + '</span>\n  </nav>'
)


def apply_r15_theme_slot(site_slug, template_text):
    _require(template_text, R15_CHROME_NAV_ANCHOR, site_slug, "R15")
    replacement = R15_CHROME_NAV_ANCHOR[:-len('</nav>')] + R15_THEME_SLOT_WRAPPED
    return template_text.replace(R15_CHROME_NAV_ANCHOR, replacement, 1)


# ═══════════════════════════════════════════════════════════════════════
# R16 — Ks4Ladder's Apply rung reads a typed number the way a pupil writes
# it (Mide's approval, 2 Oct 2026: "fix the exam ladder's reading of
# '63 000' / '63,000' … in the shared block"). Design's grader did
# `parseFloat(String(s.r2num).replace(',', '.'))`, so "63 000" parsed as 63
# (parseFloat stops at the space) and "63,000" as 63.0 (the comma became a
# decimal point) — both marked a correct 63 000 J answer WRONG. The parse
# now strips every space (incl. no-break / thin / narrow no-break, which
# AQA's own number style uses as a thousands separator), treats commas as
# thousands separators when they group digits in threes after a non-zero
# lead (1,234 / 63,000 / 1,234,567.5), and otherwise keeps Design's legacy
# reading of a single comma as a decimal comma (6,3 → 6.3; 0,500 → 0.5).
# A leading + / − is accepted (parseFloat already did). Shared block, so
# every pilot and batch page carrying a calc rung gets it; no lesson's
# constants or freeze hash move. Tested by `tests/ks4_ladder_parse_test.py` (runs this exact string in Node).
# ═══════════════════════════════════════════════════════════════════════
R16_LADDER_PARSE_FROM = "const v = parseFloat(String(s.r2num).replace(',', '.'));"
R16_PARSE_FN = (
    "function (raw) { var t = String(raw).replace(/[\\s\\u00a0\\u2009\\u202f]/g, ''); "
    "if (/^[+-]?[1-9]\\d{0,2}(,\\d{3})+(\\.\\d+)?$/.test(t)) t = t.replace(/,/g, ''); "
    "else t = t.replace(',', '.'); return parseFloat(t); }")
R16_LADDER_PARSE_TO = "const v = (" + R16_PARSE_FN + ")(s.r2num); // ⊕ R16"


def apply_r16_ladder_parse(text):
    _require(text, R16_LADDER_PARSE_FROM, "Ks4Ladder.dc.html", "R16")
    return text.replace(R16_LADDER_PARSE_FROM, R16_LADDER_PARSE_TO, 1)


# ═══════════════════════════════════════════════════════════════════════
# R17 — Ks4Sort reports completion, so its rail stop ticks (Mide's
# approval, 2 Oct 2026: "… and the sorting block's last-stop tick in the
# shared block"). Design's `onCheck` did
#     this.setState({ checked: true, reported: true });
#     if (!s.reported && …) p.onDone(…);
# reading `s.reported` AFTER the setState. Under React `s` is a snapshot
# and that read is still false; under `shared/ks4-runtime.js` `setState`
# assigns into the SAME `this.state` object `s` points at, so `s.reported`
# is already true, `onDone` never fires, the lesson's `sort` flag never
# sets, and the rail stop never ticks. The fix reads the flag FIRST — the
# exact shape Ks4Chain (the sibling block, which ticks correctly) already
# uses: `const first = !s.reported;` before its own setState.
# ═══════════════════════════════════════════════════════════════════════
R17_SORT_REPORT_FROM = (
    "        this.setState({ checked: true, reported: true });\n"
    "        if (!s.reported && typeof p.onDone === 'function') p.onDone({ correct: wrong.length === 0 });")
R17_SORT_REPORT_TO = (
    "        const first = !s.reported; // ⊕ R17: read before setState, as Ks4Chain does\n"
    "        this.setState({ checked: true, reported: true });\n"
    "        if (first && typeof p.onDone === 'function') p.onDone({ correct: wrong.length === 0 });")


def apply_r17_sort_report(text):
    _require(text, R17_SORT_REPORT_FROM, "Ks4Sort.dc.html", "R17")
    return text.replace(R17_SORT_REPORT_FROM, R17_SORT_REPORT_TO, 1)


# ═══════════════════════════════════════════════════════════════════════
# R18 — "Start here" is a two-option guess (Mide's rule 1, 2 Oct 2026,
# docs/ks4/architecture.md; docs/ks4/START-HERE-REWRITE.md). Design's pilot
# opens on a 4-option `Ks4Choice` test. This swaps the whole `#s-hook`
# section for Design's `Ks4Guess` (batch-4 copy, build_ks4.GUESS_BLOCK_DIR)
# carrying the lesson's record in ks4_lessons/start_here.py, and replaces
# the `hookOptions`…`hookReveal` span of the logic with the two options
# (the reveal paragraph has no place in Ks4Guess: each option's reply and
# the shared bridge do its job). Runs AFTER ks4_science_rulings, so every
# science row that corrected an old opener has already fired and passed its
# expect_present check; the new text carries those corrections itself.
# Nothing outside the opener changes.
# ═══════════════════════════════════════════════════════════════════════
_R18_SECTION_RE = re.compile(r'<section id="s-hook".*?</section>', re.S)
R18_LOGIC_START = "hookOptions: ["
R18_LOGIC_END = "onHook: (i) => this.setState({ hook: i }),"


def r18_slugs():
    from ks4_lessons import start_here
    return {s for s, r in start_here.START_HERE.items() if r["batch"] == "pilot"}


def apply_r18_start_here(site_slug, design_file, template_text, logic_text):
    """(template, logic, fired). A pilot lesson with no record is untouched."""
    from ks4_lessons import start_here
    rec = start_here.START_HERE.get(site_slug)
    if rec is None or rec["batch"] != "pilot":
        return template_text, logic_text, False
    hits = _R18_SECTION_RE.findall(template_text)
    if len(hits) != 1 or 'name="Ks4Choice"' not in hits[0]:
        raise RulingError(
            "ks4_rulings R18: %s should carry exactly one #s-hook section "
            "mounting Ks4Choice; found %d section(s). Design's delivery moved."
            % (design_file, len(hits)))
    template_text = _R18_SECTION_RE.sub(
        lambda m: start_here.render_section(site_slug), template_text, count=1)

    _require(logic_text, R18_LOGIC_START, design_file, "R18")
    _require(logic_text, R18_LOGIC_END, design_file, "R18")
    a = logic_text.index(R18_LOGIC_START)
    b = logic_text.index(R18_LOGIC_END)
    if not (a < b and "hookReveal:" in logic_text[a:b]):
        raise RulingError(
            "ks4_rulings R18: %s's hookOptions…onHook span does not hold "
            "hookReveal — Design's delivery moved." % design_file)
    logic_text = (logic_text[:a] + start_here.render_options_js(site_slug)
                  + logic_text[b:])
    for old, new in rec["logic_swaps"]:
        _require(logic_text, old, design_file, "R18")
        logic_text = logic_text.replace(old, new, 1)
    return template_text, logic_text, True


# ═══════════════════════════════════════════════════════════════════════
# R19 — the big question above "Start here" must not give the answer away
# (Mide's ruling, 9 Oct 2026, on docs/ks4/START-HERE-REWRITE.md "For Mide"
# §1). Each pilot lesson's header question (`ks3-bigq`) is swapped for the
# wording the report suggested, word for word. Batch 2–3 lessons carry the
# same ruling as direct edits to their authored sources; the pilot is
# Design's files, so it is a ruling. Applied AFTER R18. ks4_parity proves
# the new text with R19_BIGQ, the same table.
# ═══════════════════════════════════════════════════════════════════════
R19_BIGQ = {
    "states-of-matter": (
        "You keep heating a solid, but the thermometer stops rising. Where is "
        "the energy going, and how do you find a melting point from messy "
        "readings?",
        "You keep heating a solid until it melts. Where does the energy go, "
        "and how do you find a melting point from messy readings?"),
    "nanoparticles": (
        "Gold is yellow and unreactive. Grind it into particles a few "
        "nanometres across and it turns red and becomes a catalyst. Same "
        "atoms. What changed, and can you calculate it?",
        "Gold is yellow and unreactive. Grind it into particles a few "
        "nanometres across and it turns red and becomes a catalyst. What "
        "changed, and can you calculate it?"),
    "covalent-bonding": (
        "When two atoms both want electrons, neither will give any away. How "
        "do they still end up with full shells?",
        "What holds two non-metal atoms together, and how many bonds does "
        "each one form?"),
}


def apply_r19_big_question(site_slug, design_file, template_text):
    pair = R19_BIGQ.get(site_slug)
    if pair is None:
        return template_text
    old, new = pair
    needle = '<p class="ks3-bigq">%s</p>' % old
    _require(template_text, needle, design_file, "R19")
    return template_text.replace(
        needle, '<p class="ks3-bigq">%s</p> <!-- ⊕ R19 -->' % new)

