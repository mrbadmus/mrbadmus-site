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
`R-`) and the two the science examiners raised on 25 Sep 2026 (`R-SLUG`,
`RUNG1-FALLBACK` — the latter is a build-log WARNING, not a rewrite, and its
code lives in build_ks4.py's `check_rung1_fallback()` since it changes
nothing; noted here only so this file's ruling list stays the complete index).
"""

import re

import ks4_lessons


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
# R5 — nanoparticles' spec LABEL. VERIFIED AS A NO-OP: the delivered
# FILENAME still says 5.2.3.3 (frozen — see ks4_lessons/__init__.py's
# comment), but the PAGE ITSELF already shows "AQA Chemistry 4.2.4
# (chemistry only)". flag 2 in NOTES-KS4-pilot.md §9 says exactly this: "the
# page shows 4.2.4". If this assertion ever fails, the page has drifted back
# to 5.2.3.3 and this needs to become a real rewrite.
# ═══════════════════════════════════════════════════════════════════════
def check_r5_nanoparticles_spec(text):
    _require(text, "AQA Chemistry 4.2.4 (chemistry only)", "ks4-chemistry-5.2.3.3-nanoparticles.dc.html", "R5")


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
# K.route(this)`), falling back to the Triple pathway at the same tier when
# the target does not ship on the current page's pathway (nanoparticles is
# Triple-only, and two lessons' `endConnects` link to it from all 4 routes).
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
