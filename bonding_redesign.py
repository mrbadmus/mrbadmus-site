# -*- coding: utf-8 -*-
"""
Bonding redesign — theory-block decomposition (MRB-113 Phase B, Path B).

WHAT THIS IS
------------
The canonical Bonding Theory Block Library, as DATA + a static-HTML renderer.
The generator (`generate_site_v5.py`) imports this and, for any bonding page
listed in BONDING_REDESIGN, renders its In-Depth Theory from these blocks
instead of the old `.theory-line` prose.

CONTENT FREEZE
--------------
The frozen source fields in `all_subtopics_chemistry*.py` (`theory`,
`common_mistake`, `key_note`, `matching`, …) are NEVER edited. The block
content below is authored *from* that frozen prose as presentation only —
condensed to the library's pacing rule, no fact added or changed. The byte
snapshot of the source fields therefore stays identical (see the port map §9).

THE VOCABULARY (10 blocks)
--------------------------
Static (rendered here as HTML): lead · feature-cards · compare-cards ·
step-sequence · example-callout · aside-callout · examiner-tip.
Interactive (rendered by shared/heroes/theory-blocks.js): mistake-check ·
compare-reveal — this module emits their host div + hands the generator a
config to serialise inline, exactly like a hero.

The site-wide `examiner_tip` FIELD (one per page, like common_mistake) renders
through the examiner-tip block on .rd pages — see render_examiner_tip(). On
non-redesigned pages the generator renders the same field as a flat amber
callout (.examiner-box in shared/styles.css).

LOCKED RULES (from the block library)
-------------------------------------
1. Colour = meaning. tone 'good' (green) = conducts / mobile charge /
   favourable; 'limit' (red) = does not / limitation; 'neutral' = a plain
   fact (DEFAULT). Never tint for decoration.
2. Pacing. One idea per block, short lines. Past ~2 lines of prose → split.
3. Parallel & mistake-first. compare-cards keep the same rows both sides;
   `highlight` marks the payoff row. Misconceptions stated first, then fixed.
"""

import html as _html
import json as _json


# ─────────────────────────────────────────────────────────────
#  Block CSS — Locked-token shell, scoped to `.rd`. Colours are the
#  block library's exact signed-off values; fonts resolve through the
#  Locked tokens (Space Grotesk / IBM Plex) on `.rd` pages. Compare-cards
#  add a mobile stack the desktop design doc did not need.
# ─────────────────────────────────────────────────────────────
BLOCK_CSS = """
/* Theory Block Library — static blocks (MRB-113 Phase B) */
.rd .rd-blocks { display: flex; flex-direction: column; gap: 18px; }
.rd .rd-blk-lead { margin: 0; font-family: var(--font-body,sans-serif); font-size: calc(16.5px * var(--rd-fs-scale, 1)); line-height: 1.6; color: #211B15; max-width: 72ch; }
.rd .rd-blk-lead b { color: var(--ink,#1A1714); }
/* feature-cards */
.rd .rd-blk-feature { display: grid; grid-template-columns: repeat(auto-fit,minmax(210px,1fr)); gap: 12px; }
.rd .rd-fcard { border-radius: 14px; padding: 16px 18px; border: 1px solid; }
.rd .rd-fcard__hd { display: flex; align-items: center; gap: 8px; margin-bottom: 6px; }
.rd .rd-fcard__hd b { font-family: var(--font-display,sans-serif); font-weight: 700; font-size: calc(15px * var(--rd-fs-scale, 1)); line-height: 1.3; }
.rd .rd-fcard__body { font-size: calc(13.5px * var(--rd-fs-scale, 1)); line-height: 1.55; color: #211B15; }
.rd .rd-fcard--good { background: #E7F3EA; border-color: #B9DCC1; }
.rd .rd-fcard--good .rd-fcard__hd b { color: #3E6B47; }
.rd .rd-fcard--limit { background: #FBE4DE; border-color: #EFC0B4; }
.rd .rd-fcard--limit .rd-fcard__hd b { color: #B5341A; }
.rd .rd-fcard--neutral { background: #F7F2E8; border-color: #E4DCCB; }
.rd .rd-fcard--neutral .rd-fcard__hd b { color: #B5341A; }
/* compare-cards */
.rd .rd-blk-compare .rd-cmp-grid { display: grid; gap: 14px; }
.rd .rd-cmp-col { background: #FFFDF8; border: 1px solid #E4DCCB; border-radius: 16px; overflow: hidden; }
.rd .rd-cmp-col__hd { display: flex; align-items: center; gap: 10px; padding: 14px 18px; border-bottom: 1px solid #EFE7D8; background: #F7F2E8; }
.rd .rd-cmp-col__hd b { font-family: var(--font-display,sans-serif); font-weight: 700; font-size: calc(17px * var(--rd-fs-scale, 1)); color: #1A1714; }
.rd .rd-cmp-row { display: flex; flex-direction: column; gap: 2px; padding: 11px 18px; border-bottom: 1px solid #F2ECDD; }
.rd .rd-cmp-row:last-child { border-bottom: none; }
.rd .rd-cmp-row__k { font-family: var(--font-mono,monospace); font-size: calc(12px * var(--rd-fs-scale, 1)); font-weight: 700; letter-spacing: .06em; color: #716A60; text-transform: uppercase; }
.rd .rd-cmp-row__v { font-family: var(--font-display,sans-serif); font-weight: 700; font-size: calc(14.5px * var(--rd-fs-scale, 1)); color: #211B15; line-height: 1.35; }
.rd .rd-cmp-row--hl { padding: 12px 18px; }
.rd .rd-cmp-row--hl.tone-good { background: #E7F3EA; border-top: 2px solid #7FB98A; }
.rd .rd-cmp-row--hl.tone-good .rd-cmp-row__k { color: #55735B; } .rd .rd-cmp-row--hl.tone-good .rd-cmp-row__v { color: #3E6B47; }
.rd .rd-cmp-row--hl.tone-limit { background: #FBE4DE; border-top: 2px solid #E0897B; }
.rd .rd-cmp-row--hl.tone-limit .rd-cmp-row__k { color: #9C5342; } .rd .rd-cmp-row--hl.tone-limit .rd-cmp-row__v { color: #B5341A; }
.rd .rd-cmp-row--hl.tone-neutral { background: #F7F2E8; border-top: 2px solid #D8CFBD; }
.rd .rd-cmp-row--hl.tone-neutral .rd-cmp-row__k { color: #716A60; } .rd .rd-cmp-row--hl.tone-neutral .rd-cmp-row__v { color: #211B15; }
.rd .rd-cmp-verdict { margin-top: 12px; text-align: center; font-family: var(--font-display,sans-serif); font-weight: 700; font-size: calc(14.5px * var(--rd-fs-scale, 1)); color: #95270F; background: #F8D2C4; border: 1px solid #EBAF9B; border-radius: 999px; padding: 9px 18px; }
@media (max-width: 560px) { .rd .rd-blk-compare .rd-cmp-grid { grid-template-columns: 1fr !important; } }
/* MRB-124 — feature-cards clip at narrow width: repeat(auto-fit,minmax(210px,1fr))
   demands 2×210px+gap on a ~400px viewport, so a second track overflows and drags
   the whole page into horizontal scroll. Stack to a single column at the same
   breakpoint the compare-cards use. Later source order → wins over the base rule. */
@media (max-width: 560px) { .rd .rd-blk-feature { grid-template-columns: 1fr; } }
/* step-sequence */
.rd .rd-blk-steps { display: flex; flex-direction: column; gap: 8px; }
.rd .rd-step { display: flex; gap: 14px; align-items: flex-start; background: #F7F2E8; border-radius: 12px; padding: 13px 16px; }
.rd .rd-step__n { font-family: var(--font-display,sans-serif); font-weight: 700; font-size: calc(14px * var(--rd-fs-scale, 1)); color: #fff; background: #C0392B; min-width: 26px; height: 26px; border-radius: 50%; display: flex; align-items: center; justify-content: center; flex: none; }
.rd .rd-step__t { font-size: calc(14.5px * var(--rd-fs-scale, 1)); line-height: 1.55; color: #211B15; padding-top: 3px; }
/* example-callout */
.rd .rd-blk-example { background: #FBEEE9; border-left: 4px solid #C0392B; border-radius: 12px; padding: 16px 20px; }
.rd .rd-blk-example__hd { display: flex; align-items: center; gap: 8px; margin-bottom: 8px; }
.rd .rd-blk-example__hd b { font-family: var(--font-display,sans-serif); font-weight: 700; font-size: calc(15.5px * var(--rd-fs-scale, 1)); color: #B5341A; }
.rd .rd-blk-example__lines { display: flex; flex-direction: column; gap: 5px; }
.rd .rd-blk-example__lines div { font-size: calc(14px * var(--rd-fs-scale, 1)); line-height: 1.5; color: #3A2A26; }
/* aside-callout */
.rd .rd-blk-aside { background: #F6E9CE; border-left: 4px solid #C7861F; border-radius: 12px; padding: 15px 20px; }
.rd .rd-blk-aside b { display: block; font-family: var(--font-display,sans-serif); font-weight: 700; font-size: calc(15px * var(--rd-fs-scale, 1)); color: #7A5510; margin-bottom: 4px; }
.rd .rd-blk-aside__body { font-size: calc(14px * var(--rd-fs-scale, 1)); line-height: 1.55; color: #4A3A1E; }
/* examiner-tip — exam-technique callout. Amber/gold with its own left-border,
   deliberately distinct from the red example-callout (#C0392B), the red Common
   Mistake, and the burnt-orange brand accent (--accent-strong). */
.rd .rd-blk-examiner { background: #FEF6E0; border-left: 4px solid #E0A21A; border-radius: 12px; padding: 15px 20px; }
.rd .rd-blk-examiner__hd { display: flex; align-items: center; gap: 8px; margin-bottom: 6px; }
.rd .rd-blk-examiner__hd b { font-family: var(--font-display,sans-serif); font-weight: 700; font-size: calc(15px * var(--rd-fs-scale, 1)); color: #8A5E0A; }
.rd .rd-blk-examiner__body { font-size: calc(14px * var(--rd-fs-scale, 1)); line-height: 1.55; color: #4A3A12; }
.rd .rd-blk-examiner__body b { color: #6E4A00; }
"""


def _esc(s):
    return _html.escape(str(s), quote=False)


def _boldify(text, bolds):
    """Escape text, then wrap any bold substrings in <b>. Bold spans are
    plain words, so escaping does not alter them."""
    out = _esc(text)
    for b in (bolds or []):
        eb = _esc(b)
        out = out.replace(eb, "<b>%s</b>" % eb)
    return out


# ─── per-block static renderers (return HTML strings) ───

def _r_lead(b):
    return '<p class="rd-blk-lead">%s</p>' % _boldify(b["text"], b.get("bold"))


def _r_feature(b):
    cards = ""
    for c in b["cards"]:
        tone = c.get("tone", "neutral")
        cards += (
            '<div class="rd-fcard rd-fcard--%s">'
            '<div class="rd-fcard__hd"><span style="font-size: calc(17px * var(--rd-fs-scale, 1));">%s</span><b>%s</b></div>'
            '<div class="rd-fcard__body">%s</div></div>'
        ) % (tone, _esc(c.get("emoji", "")), _esc(c["title"]), _esc(c["body"]))
    return '<div class="rd-blk-feature">%s</div>' % cards


def _r_compare(b):
    cols = b["columns"]
    hl = b.get("highlight")
    cols_html = ""
    for col in cols:
        rows_html = ""
        for ri, r in enumerate(col["rows"]):
            is_hl = hl is not None and ri == hl
            tone = r.get("tone", "neutral")
            cls = "rd-cmp-row" + (" rd-cmp-row--hl tone-%s" % tone if is_hl else "")
            rows_html += (
                '<div class="%s"><span class="rd-cmp-row__k">%s</span>'
                '<span class="rd-cmp-row__v">%s</span></div>'
            ) % (cls, _esc(r["k"]), _esc(r["v"]))
        cols_html += (
            '<div class="rd-cmp-col"><div class="rd-cmp-col__hd">'
            '<span style="font-size: calc(20px * var(--rd-fs-scale, 1));">%s</span><b>%s</b></div>%s</div>'
        ) % (_esc(col.get("emoji", "")), _esc(col["title"]), rows_html)
    grid = '<div class="rd-cmp-grid" style="grid-template-columns:repeat(%d,1fr);">%s</div>' % (
        len(cols), cols_html)
    verdict = ('<div class="rd-cmp-verdict">%s</div>' % _esc(b["verdict"])) if b.get("verdict") else ""
    return '<div class="rd-blk-compare">%s%s</div>' % (grid, verdict)


def _r_steps(b):
    steps = ""
    for i, s in enumerate(b["steps"]):
        steps += (
            '<div class="rd-step"><span class="rd-step__n">%d</span>'
            '<span class="rd-step__t">%s</span></div>'
        ) % (i + 1, _esc(s))
    return '<div class="rd-blk-steps">%s</div>' % steps


def _r_example(b):
    lines = "".join("<div>%s</div>" % _esc(l) for l in b["lines"])
    return (
        '<div class="rd-blk-example"><div class="rd-blk-example__hd">'
        '<span style="font-size: calc(17px * var(--rd-fs-scale, 1));">%s</span><b>%s</b></div>'
        '<div class="rd-blk-example__lines">%s</div></div>'
    ) % (_esc(b.get("emoji", "")), _esc(b["title"]), lines)


def _r_aside(b):
    return (
        '<div class="rd-blk-aside"><b>%s</b><div class="rd-blk-aside__body">%s</div></div>'
    ) % (_esc(b["title"]), _esc(b["body"]))


def _r_examiner_tip(b):
    """Amber/gold ⭐ exam-technique callout. `text` (+ optional `bold` spans)."""
    return (
        '<div class="rd-blk-examiner"><div class="rd-blk-examiner__hd">'
        '<span style="font-size: calc(17px * var(--rd-fs-scale, 1));">⭐</span>'
        '<b>Examiner Tip</b></div>'
        '<div class="rd-blk-examiner__body">%s</div></div>'
    ) % _boldify(b["text"], b.get("bold"))


_STATIC = {
    "lead": _r_lead, "feature-cards": _r_feature, "compare-cards": _r_compare,
    "step-sequence": _r_steps, "example-callout": _r_example, "aside-callout": _r_aside,
    "examiner-tip": _r_examiner_tip,
}
_INTERACTIVE = {"mistake-check": "mistakeCheck", "compare-reveal": "compareReveal"}


def render_theory_blocks(blocks, st_id):
    """Return (html, interactive_specs).

    html: the In-Depth Theory body, blocks in order. Interactive blocks are
    emitted as an empty host div; their config is returned so the generator
    can serialise an init call (like a hero).
    interactive_specs: list of dicts {ns, host_id, config}.
    """
    parts = []
    interactive = []
    for i, b in enumerate(blocks):
        t = b["type"]
        if t in _STATIC:
            parts.append(_STATIC[t](b))
        elif t in _INTERACTIVE:
            host_id = "tb-%s-%s-%d" % (_INTERACTIVE[t].lower(), st_id, i)
            parts.append('<div id="%s"></div>' % host_id)
            cfg = {k: v for k, v in b.items() if k != "type"}
            interactive.append({"ns": _INTERACTIVE[t], "host_id": host_id, "config": cfg})
        else:
            raise ValueError("Unknown theory block type: %r" % t)
    html = '<div class="rd-blocks">%s</div>' % "".join(parts)
    return html, interactive


def render_examiner_tip(text, bold=None):
    """Render the site-wide `examiner_tip` FIELD as the canonical examiner-tip
    block. Used by the generator on .rd pages; non-redesigned pages render the
    same field as a flat amber callout (.examiner-box) instead."""
    return _r_examiner_tip({"type": "examiner-tip", "text": text, "bold": bold})


# ═════════════════════════════════════════════════════════════
#  FIFA STEP REVEAL — nanoparticles (MRB-113 · content-standards §2)
#  The WORKED spine is the frozen `fifas` field, read per variant
#  (Triple-Foundation vs Triple-Higher differ) — never edited. The
#  authored per-tier PRACTICE below (prompt / options / accept /
#  feedback + a step title & note) is NEW presentation scaffolding
#  that turns the static worked examples into the interactive practice
#  the standard requires. build_fifa_config() zips the two by tier and
#  by (example index, step index). ⚠ SCIENCE-SENSITIVE — every accept
#  value is flagged for Mide's full review (content-standards §7).
# ═════════════════════════════════════════════════════════════
_FORMULA_CHOICE_CUBE = {
    "prompt": "Which formula gives the surface area to volume ratio?", "kind": "choice",
    "options": [
        {"text": "surface area ÷ volume", "correct": True},
        {"text": "volume ÷ surface area"},
        {"text": "surface area × volume"},
    ],
    "feedback": {"wrong": "It is a ratio of area to volume — divide the surface area by the volume."},
}
_FORMULA_CHOICE_6L = {
    "prompt": "For a cube, which is the simplest form of the surface area to volume ratio?", "kind": "choice",
    "options": [
        {"text": "6 ÷ L", "correct": True},
        {"text": "L ÷ 6"},
        {"text": "6 × L"},
    ],
    "feedback": {"wrong": "6L² ÷ L³ cancels to 6 ÷ L."},
}

NANO_FIFA = {
    "emoji": "⚽", "title": "Surface Area : Volume",
    "subtitle": "Formula → Insert → Fine-tune → Answer",
    "foundation": [
        {"name": "Cube · side 2", "given": [{"sym": "side length", "val": "2", "note": "a cube"}],
         "success": {"title": "Correct — ratio = 3 (3 : 1)", "sub": "Formula, surface area and volume, the division, and the ratio — all right."},
         "hint": "FIFA: Formula → Insert → Fine-tune → Answer. Ratio = surface area ÷ volume; a cube has 6 faces and volume = side³.",
         "steps": [
             {"title": "Write the formula", "note": "Compare the outside area with the inside volume.", "practice": _FORMULA_CHOICE_CUBE},
             {"title": "Work out surface area and volume", "note": "A cube has 6 identical faces (side × side); its volume is side × side × side.",
              "practice": {"prompt": "Work out the surface area and the volume of a cube of side 2.", "kind": "input",
                  "blanks": [{"prefix": "surface area = 6 × (2×2) =", "accept": ["24"]}, {"prefix": "volume = 2×2×2 =", "accept": ["8"]}],
                  "feedback": {"wrong": "Surface area = 6 × (2×2) = 24. Volume = 2 × 2 × 2 = 8."}}},
             {"title": "Set up the division", "note": "Divide the surface area by the volume.",
              "practice": {"prompt": "Which division gives the ratio?", "kind": "choice",
                  "options": [{"text": "24 ÷ 8", "correct": True}, {"text": "8 ÷ 24"}, {"text": "24 × 8"}],
                  "feedback": {"wrong": "Surface area ÷ volume = 24 ÷ 8."}}},
             {"title": "State the ratio", "note": "Work out the division; here the ratio has no unit.",
              "practice": {"prompt": "Work out 24 ÷ 8.", "kind": "input",
                  "blanks": [{"prefix": "ratio =", "suffix": "(or 3 : 1)", "accept": ["3", "3:1"]}],
                  "feedback": {"wrong": "24 ÷ 8 = 3, so the ratio is 3 (that is, 3 : 1)."}}},
         ]},
        {"name": "Cube · side 1", "given": [{"sym": "side length", "val": "1", "note": "a smaller cube"}],
         "success": {"title": "Correct — ratio = 6 (6 : 1)", "sub": "The smaller cube has the larger surface area to volume ratio."},
         "hint": "FIFA: Formula → Insert → Fine-tune → Answer. Ratio = surface area ÷ volume; a cube has 6 faces and volume = side³.",
         "steps": [
             {"title": "Write the formula", "note": "Same formula — area over volume.", "practice": _FORMULA_CHOICE_CUBE},
             {"title": "Work out surface area and volume", "note": "Same method: 6 faces, and side³ for the volume.",
              "practice": {"prompt": "Work out the surface area and the volume of a cube of side 1.", "kind": "input",
                  "blanks": [{"prefix": "surface area = 6 × (1×1) =", "accept": ["6"]}, {"prefix": "volume = 1×1×1 =", "accept": ["1"]}],
                  "feedback": {"wrong": "Surface area = 6 × 1 = 6. Volume = 1."}}},
             {"title": "Set up the division", "note": "Divide the surface area by the volume.",
              "practice": {"prompt": "Which division gives the ratio?", "kind": "choice",
                  "options": [{"text": "6 ÷ 1", "correct": True}, {"text": "1 ÷ 6"}, {"text": "6 × 1"}],
                  "feedback": {"wrong": "Surface area ÷ volume = 6 ÷ 1."}}},
             {"title": "State the ratio and compare", "note": "Compare with the side-2 cube (ratio 3).",
              "practice": {"prompt": "Work out 6 ÷ 1.", "kind": "input",
                  "blanks": [{"prefix": "ratio =", "suffix": "(or 6 : 1)", "accept": ["6", "6:1"]}],
                  "feedback": {"wrong": "6 ÷ 1 = 6 (6 : 1) — bigger than the side-2 cube's 3. The SMALLER cube has the LARGER ratio."}}},
         ]},
        {"name": "Cube · side 3", "given": [{"sym": "side length", "val": "3", "note": "a larger cube"}],
         "success": {"title": "Correct — ratio = 2 (2 : 1)", "sub": "The largest cube has the smallest surface area to volume ratio."},
         "hint": "FIFA: Formula → Insert → Fine-tune → Answer. Ratio = surface area ÷ volume; a cube has 6 faces and volume = side³.",
         "steps": [
             {"title": "Write the formula", "note": "Same formula — area over volume.", "practice": _FORMULA_CHOICE_CUBE},
             {"title": "Work out surface area and volume", "note": "6 faces of side × side, and side³ for the volume.",
              "practice": {"prompt": "Work out the surface area and the volume of a cube of side 3.", "kind": "input",
                  "blanks": [{"prefix": "surface area = 6 × (3×3) =", "accept": ["54"]}, {"prefix": "volume = 3×3×3 =", "accept": ["27"]}],
                  "feedback": {"wrong": "Surface area = 6 × 9 = 54. Volume = 3³ = 27."}}},
             {"title": "Set up the division", "note": "Divide the surface area by the volume.",
              "practice": {"prompt": "Which division gives the ratio?", "kind": "choice",
                  "options": [{"text": "54 ÷ 27", "correct": True}, {"text": "27 ÷ 54"}, {"text": "54 × 27"}],
                  "feedback": {"wrong": "Surface area ÷ volume = 54 ÷ 27."}}},
             {"title": "State the ratio", "note": "The biggest cube gives the smallest ratio.",
              "practice": {"prompt": "Work out 54 ÷ 27.", "kind": "input",
                  "blanks": [{"prefix": "ratio =", "suffix": "(or 2 : 1)", "accept": ["2", "2:1"]}],
                  "feedback": {"wrong": "54 ÷ 27 = 2 (2 : 1) — the LARGEST cube has the SMALLEST ratio."}}},
         ]},
    ],
    "higher": [
        {"name": "Nanoparticle · 10 nm", "given": [{"sym": "side length L", "val": "10 nm", "note": "model as a cube"}],
         "success": {"title": "Correct — ratio = 0.6 nm⁻¹", "sub": "6 ÷ L with L in nm gives the ratio in nm⁻¹."},
         "hint": "For a cube, surface area to volume ratio = 6 ÷ L. With L in nm the unit is nm⁻¹. Smaller L → larger ratio.",
         "steps": [
             {"title": "Write the formula", "note": "For a cube the ratio simplifies: 6L² ÷ L³ = 6 ÷ L.", "practice": _FORMULA_CHOICE_6L},
             {"title": "Insert the length", "note": "Substitute L = 10 nm.",
              "practice": {"prompt": "Insert L into 6 ÷ L.", "kind": "input",
                  "blanks": [{"prefix": "ratio = 6 ÷", "accept": ["10"]}],
                  "feedback": {"wrong": "L = 10 nm, so the ratio is 6 ÷ 10."}}},
             {"title": "Fine-tune: the unit", "note": "Length is in nm, so the ratio is per nm.",
              "practice": {"prompt": "What is the unit of the ratio when L is in nm?", "kind": "choice",
                  "options": [{"text": "nm⁻¹ (per nm)", "correct": True}, {"text": "nm"}, {"text": "nm²"}],
                  "feedback": {"wrong": "A number ÷ a length in nm → units of 1/nm = nm⁻¹."}}},
             {"title": "State the answer with its unit", "note": "Divide, then attach nm⁻¹.",
              "practice": {"prompt": "Work out 6 ÷ 10 and give the unit.", "kind": "input",
                  "blanks": [{"prefix": "ratio =", "placeholder": "value", "accept": ["0.6", ".6"]},
                             {"suffix": "(unit)", "placeholder": "unit", "accept": ["nm⁻¹", "nm-1", "1/nm", "per nm", "nm^-1"]}],
                  "feedback": {"wrong": "6 ÷ 10 = 0.6, and the unit is nm⁻¹."}}},
         ]},
        {"name": "Bulk grain · 1000 nm", "given": [{"sym": "side length L", "val": "1000 nm", "note": "same material, bigger"}],
         "success": {"title": "Correct — 0.006 nm⁻¹, 100× smaller than the nanoparticle", "sub": "Big particle → tiny ratio; nanoparticle → huge ratio."},
         "hint": "For a cube, surface area to volume ratio = 6 ÷ L. With L in nm the unit is nm⁻¹. Smaller L → larger ratio.",
         "steps": [
             {"title": "Write the formula", "note": "Same simplified form: 6 ÷ L.", "practice": _FORMULA_CHOICE_6L},
             {"title": "Insert the length", "note": "Substitute L = 1000 nm.",
              "practice": {"prompt": "Insert L into 6 ÷ L.", "kind": "input",
                  "blanks": [{"prefix": "ratio = 6 ÷", "accept": ["1000"]}],
                  "feedback": {"wrong": "L = 1000 nm, so the ratio is 6 ÷ 1000."}}},
             {"title": "Fine-tune: work it out", "note": "6 ÷ 1000 = 0.006.",
              "practice": {"prompt": "Work out 6 ÷ 1000 (in nm⁻¹).", "kind": "input",
                  "blanks": [{"prefix": "ratio =", "accept": ["0.006", ".006"]}],
                  "feedback": {"wrong": "6 ÷ 1000 = 0.006 nm⁻¹."}}},
             {"title": "Compare with the nanoparticle", "note": "The 10 nm nanoparticle was 0.6 nm⁻¹.",
              "practice": {"prompt": "How does this grain's ratio compare with the 10 nm nanoparticle (0.6 nm⁻¹)?", "kind": "choice",
                  "options": [{"text": "100 times smaller — far fewer atoms on the surface", "correct": True},
                              {"text": "100 times larger — more atoms on the surface"},
                              {"text": "about the same"}],
                  "feedback": {"wrong": "0.006 vs 0.6 → 100× smaller. The nanoparticle has far more of its atoms on the surface."}}},
         ]},
        {"name": "Work backwards · ratio 1.2", "given": [{"sym": "ratio", "val": "1.2 nm⁻¹", "note": "find the side length"}],
         "success": {"title": "Correct — L = 5 nm", "sub": "Rearranged the formula, substituted, and gave the length in nm."},
         "hint": "For a cube, surface area to volume ratio = 6 ÷ L. Rearranged: L = 6 ÷ ratio. The answer is a length, so its unit is nm.",
         "steps": [
             {"title": "Rearrange the formula", "note": "ratio = 6 ÷ L, so L = 6 ÷ ratio.",
              "practice": {"prompt": "Rearrange ratio = 6 ÷ L to make L the subject.", "kind": "choice",
                  "options": [{"text": "L = 6 ÷ ratio", "correct": True}, {"text": "L = ratio ÷ 6"}, {"text": "L = 6 × ratio"}],
                  "feedback": {"wrong": "Multiply both sides by L, then divide by the ratio: L = 6 ÷ ratio."}}},
             {"title": "Insert the ratio", "note": "Substitute ratio = 1.2 nm⁻¹.",
              "practice": {"prompt": "Insert the ratio into L = 6 ÷ ratio.", "kind": "input",
                  "blanks": [{"prefix": "L = 6 ÷", "accept": ["1.2"]}],
                  "feedback": {"wrong": "ratio = 1.2, so L = 6 ÷ 1.2."}}},
             {"title": "Fine-tune: the unit", "note": "The answer is a length, so the unit is nm.",
              "practice": {"prompt": "What unit will the answer have?", "kind": "choice",
                  "options": [{"text": "nm (a length)", "correct": True}, {"text": "nm⁻¹"}, {"text": "nm²"}],
                  "feedback": {"wrong": "You are finding a length L, so the unit is nm."}}},
             {"title": "State the answer with its unit", "note": "Divide, then attach nm.",
              "practice": {"prompt": "Work out 6 ÷ 1.2 and give the unit.", "kind": "input",
                  "blanks": [{"prefix": "L =", "placeholder": "value", "accept": ["5"]},
                             {"suffix": "(unit)", "placeholder": "unit", "accept": ["nm"]}],
                  "feedback": {"wrong": "6 ÷ 1.2 = 5, and the unit is nm."}}},
         ]},
    ],
}


def build_fifa_config(fifas, tier):
    """Zip the frozen `fifas` worked spine (per variant) with the authored
    per-tier practice in NANO_FIFA. Returns a fifaStepReveal config, or None
    if the shapes don't line up (defensive — never emit a broken hero)."""
    practice_set = NANO_FIFA.get(tier)
    if not fifas or not practice_set or len(fifas) != len(practice_set):
        return None
    examples = []
    for ex_i, fex in enumerate(fifas):
        pex = practice_set[ex_i]
        fsteps = fex.get("steps") or []
        if len(fsteps) != len(pex["steps"]):
            return None
        steps = []
        for st_i, (_letter, worked_text) in enumerate(fsteps):
            pstep = pex["steps"][st_i]
            steps.append({
                "title": pstep["title"], "worked": worked_text,
                "note": pstep["note"], "practice": pstep["practice"],
            })
        examples.append({
            "name": pex["name"], "problem": fex.get("question", ""),
            "given": pex.get("given", []), "steps": steps,
            "success": pex["success"], "hint": pex["hint"],
        })
    return {
        "emoji": NANO_FIFA["emoji"], "title": NANO_FIFA["title"],
        "subtitle": NANO_FIFA["subtitle"], "examples": examples,
    }


def interactive_init_js(interactive_specs):
    """Build the inline init JS for a page's interactive theory blocks."""
    if not interactive_specs:
        return ""
    lines = []
    for spec in interactive_specs:
        cfg = _json.dumps(spec["config"], ensure_ascii=False)
        lines.append(
            "    (function(){var h=document.getElementById('%s');"
            "if(h&&window.MrbTheoryBlocks&&MrbTheoryBlocks.%s)MrbTheoryBlocks.%s.init(h,%s);})();"
            % (spec["host_id"], spec["ns"], spec["ns"], cfg)
        )
    return "\n".join(lines)


# ═════════════════════════════════════════════════════════════
#  PER-PAGE DECOMPOSITIONS
#  Authored from the frozen prose. `hero` = None means a block-only
#  page (the teaching interaction lives in a mistake-check /
#  compare-reveal block). `activity` names the Categorise-Bins config
#  key in shared/heroes/bonding-configs.js.
# ═════════════════════════════════════════════════════════════
BONDING_REDESIGN = {

    # ── exemplar · giant-covalent-structures — theory retrofitted onto blocks (D2) ──
    # Hero (Two-State diamond/graphite), bins, quiz, tip and the static Common
    # Mistake are unchanged; only the In-Depth Theory moves prose → blocks. The
    # compare-cards deliberately mirror the hero as a static reference table.
    "giant-covalent-structures": {
        "hero": {"module": "two-state-compare", "ns": "twoStateCompare", "config_key": "giant-covalent-structures",
                 "kicker": "explore the two structures"},
        "activity": {"type": "bins", "config_key": "giant-covalent-structures-bins", "kicker": "sort the properties"},
        "theory_blocks": [
            {"type": "lead",
             "text": "Giant covalent structures (also called macromolecular) are substances where a huge number of atoms are all joined by covalent bonds throughout the whole structure — there are no separate molecules. Examples: diamond, graphite and silicon dioxide (SiO₂).",
             "bold": ["covalent bonds throughout"]},
            {"type": "feature-cards", "cards": [
                {"emoji": "🌡️", "title": "Very high melting point", "tone": "neutral",
                 "body": "Melting means breaking millions of strong covalent bonds, which takes a lot of energy."},
                {"emoji": "💎", "title": "Very hard & rigid", "tone": "neutral",
                 "body": "A rigid 3-D network of strong bonds holds every atom firmly in place."},
                {"emoji": "🚫", "title": "Usually don't conduct", "tone": "limit",
                 "body": "Most have no free electrons or ions to carry charge — graphite is the exception."},
            ]},
            {"type": "compare-cards", "columns": [
                {"emoji": "💎", "title": "Diamond", "rows": [
                    {"k": "Bonds per carbon", "v": "4 — rigid 3-D tetrahedral lattice"},
                    {"k": "Free electrons", "v": "None (all 4 used in bonds)"},
                    {"k": "Conducts electricity?", "v": "No"},
                    {"k": "Hardness", "v": "Hardest natural substance"},
                ]},
                {"emoji": "✏️", "title": "Graphite", "rows": [
                    {"k": "Bonds per carbon", "v": "3 — flat hexagonal layers"},
                    {"k": "Free electrons", "v": "1 delocalised per carbon"},
                    {"k": "Conducts electricity?", "v": "Yes"},
                    {"k": "Hardness", "v": "Soft & slippery (layers slide)"},
                ]},
            ], "highlight": 2,
             "verdict": "Both are pure carbon. The spare 4th electron and the sliding layers are why graphite conducts and is soft, while diamond does neither."},
            {"type": "example-callout", "emoji": "🛠️", "title": "Uses", "lines": [
                "Diamond: cutting tools, drill bits, gemstones, abrasives (very hard).",
                "Graphite: pencil leads and lubricants (layers slide); electrodes in electrolysis (conducts, unreactive).",
            ]},
        ],
    },

    # ── 1 · chemical-bonds — decision-rule page, block-only ──
    "chemical-bonds": {
        "hero": None,
        "activity": {"type": "bins", "config_key": "chemical-bonds-bins"},
        "theory_blocks": [
            {"type": "lead",
             "text": "Atoms form chemical bonds to reach a more stable arrangement — usually a full outer shell, like the noble gases.",
             "bold": ["full outer shell"]},
            {"type": "feature-cards", "cards": [
                {"emoji": "🔻", "title": "Metals lose", "tone": "neutral",
                 "body": "Group 1, 2 and 3 metals give away their outer electrons."},
                {"emoji": "🔺", "title": "Non-metals gain", "tone": "neutral",
                 "body": "Group 5, 6 and 7 non-metals take electrons in."},
                {"emoji": "🤝", "title": "Non-metals share", "tone": "neutral",
                 "body": "Two non-metals share electrons between them."},
            ]},
            {"type": "compare-cards", "columns": [
                {"emoji": "🧂", "title": "Ionic", "rows": [
                    {"k": "Between which atoms", "v": "Metal + non-metal"},
                    {"k": "What happens to electrons", "v": "Transferred, metal → non-metal"},
                    {"k": "Example", "v": "Sodium chloride, NaCl"},
                ]},
                {"emoji": "💧", "title": "Covalent", "rows": [
                    {"k": "Between which atoms", "v": "Non-metal + non-metal"},
                    {"k": "What happens to electrons", "v": "Shared in pairs"},
                    {"k": "Example", "v": "Water, H₂O"},
                ]},
                {"emoji": "🔩", "title": "Metallic", "rows": [
                    {"k": "Between which atoms", "v": "Metal atoms (pure metal)"},
                    {"k": "What happens to electrons", "v": "Delocalised into a shared sea"},
                    {"k": "Example", "v": "Copper, Cu"},
                ]},
            ], "highlight": 1,
             "verdict": "What the atoms ARE decides how their electrons behave — and that is the bond."},
            {"type": "feature-cards", "cards": [
                {"emoji": "🌡️", "title": "Ionic → high melting point", "tone": "neutral",
                 "body": "Strong forces between ions; conducts only when molten or dissolved."},
                {"emoji": "❄️", "title": "Simple covalent → low melting point", "tone": "neutral",
                 "body": "Weak forces between whole molecules are overcome easily."},
                {"emoji": "⚡", "title": "Metallic → conducts", "tone": "good",
                 "body": "Delocalised electrons carry charge and heat; metals bend, not shatter."},
            ]},
            {"type": "mistake-check",
             "claim": "“When a molecular substance like water melts, its covalent bonds break.”",
             "prompt": "What is the flaw in this reasoning?",
             "options": [
                 {"text": "Melting only overcomes the weak forces BETWEEN whole molecules — the strong covalent bonds inside each molecule stay intact.", "correct": True},
                 {"text": "The covalent bonds do break, but they instantly reform, so it looks as though nothing happened."},
                 {"text": "Water has no covalent bonds to break — it is held together by ionic bonds."},
             ],
             "fix": "Melting a simple molecular substance separates whole molecules by overcoming the weak intermolecular forces between them. The strong covalent bonds within each molecule are not broken — which is why a low melting point tells you nothing about how strong the covalent bonds themselves are."},
        ],
    },

    # ── 7 · properties-small-molecules — small-molecular vs giant, block-only ──
    "properties-small-molecules": {
        "hero": None,
        "activity": {"type": "bins", "config_key": "properties-small-molecules-bins"},
        "theory_blocks": [
            {"type": "lead",
             "text": "Simple molecular substances are made of small, separate molecules — each holds a fixed number of atoms joined by strong covalent bonds.",
             "bold": ["strong covalent bonds"]},
            {"type": "compare-cards", "columns": [
                {"emoji": "🔗", "title": "Bonds WITHIN a molecule", "rows": [
                    {"k": "Type of force", "v": "Covalent bonds"},
                    {"k": "Strength", "v": "Strong"},
                    {"k": "Broken when it melts?", "v": "No — they stay intact"},
                ]},
                {"emoji": "🌫️", "title": "Forces BETWEEN molecules", "rows": [
                    {"k": "Type of force", "v": "Weak intermolecular forces"},
                    {"k": "Strength", "v": "Weak"},
                    {"k": "Broken when it melts?", "v": "Yes — easily overcome"},
                ]},
            ], "highlight": 2,
             "verdict": "Melting overcomes the WEAK forces between molecules — not the strong bonds inside them. That is why the melting point is low."},
            {"type": "feature-cards", "cards": [
                {"emoji": "🚫", "title": "Do not conduct electricity", "tone": "limit",
                 "body": "Molecules have no overall charge and no free electrons or ions to carry current."},
                {"emoji": "🌡️", "title": "Bigger molecule → higher melting point", "tone": "neutral",
                 "body": "More electrons → stronger intermolecular forces → more energy to separate."},
                {"emoji": "💧", "title": "Solubility varies", "tone": "neutral",
                 "body": "“Like dissolves like” — some dissolve in water, others do not."},
            ]},
            {"type": "example-callout", "emoji": "🧪",
             "title": "Example — HCl gas dissolving in water",
             "lines": [
                 "HCl(g) + water → H⁺(aq) + Cl⁻(aq).",
                 "Dissolving splits the molecule into ions.",
                 "The solution (hydrochloric acid) now conducts — because ions are present.",
             ]},
            {"type": "mistake-check",
             "claim": "“Simple molecular substances melt easily, so their covalent bonds must be weak.”",
             "prompt": "What is the flaw in this reasoning?",
             "options": [
                 {"text": "The covalent bonds inside each molecule are strong — it is the weak forces BETWEEN molecules that are overcome on melting.", "correct": True},
                 {"text": "The covalent bonds really are weak, which is the whole reason the melting point is low."},
                 {"text": "Simple molecular substances have no covalent bonds — only intermolecular forces hold them together."},
             ],
             "fix": "The covalent bonds within each molecule are strong. What is weak are the intermolecular forces between the separate molecules — melting or boiling overcomes those and leaves the covalent bonds untouched, which is why the melting point is low."},
        ],
    },

    # ── 2 · states-of-matter — three states + changes + symbols (hero-less, mistake-check) ──
    "states-of-matter": {
        "hero": None,
        "activity": {"type": "match"},
        "theory_blocks": [
            {"type": "lead",
             "text": "All matter exists in one of three states — solid, liquid or gas. The difference is how the particles are arranged and how freely they move.",
             "bold": ["solid, liquid or gas"]},
            {"type": "compare-cards", "columns": [
                {"emoji": "🧊", "title": "Solid", "rows": [
                    {"k": "Arrangement", "v": "Regular, closely packed"},
                    {"k": "Movement", "v": "Vibrate about fixed positions"},
                    {"k": "Shape & volume", "v": "Fixed shape, fixed volume"},
                    {"k": "Compressible?", "v": "No"},
                ]},
                {"emoji": "💧", "title": "Liquid", "rows": [
                    {"k": "Arrangement", "v": "Close but random"},
                    {"k": "Movement", "v": "Flow past each other"},
                    {"k": "Shape & volume", "v": "Takes container shape, fixed volume"},
                    {"k": "Compressible?", "v": "No"},
                ]},
                {"emoji": "💨", "title": "Gas", "rows": [
                    {"k": "Arrangement", "v": "Far apart, spread out"},
                    {"k": "Movement", "v": "Fast, random, all directions"},
                    {"k": "Shape & volume", "v": "Fills any container"},
                    {"k": "Compressible?", "v": "Yes"},
                ]},
            ], "highlight": 1,
             "verdict": "How freely the particles move drives everything else — shape, volume and whether it can be compressed."},
            {"type": "feature-cards", "cards": [
                {"emoji": "🫠", "title": "Melting / Freezing", "tone": "neutral",
                 "body": "Solid ⇌ liquid. Melting adds energy; freezing removes it."},
                {"emoji": "♨️", "title": "Boiling / Condensing", "tone": "neutral",
                 "body": "Liquid ⇌ gas. Boiling adds energy; condensing removes it."},
                {"emoji": "❄️", "title": "Subliming", "tone": "neutral",
                 "body": "Some solids go straight to gas (iodine, dry ice). All these are physical changes."},
            ]},
            {"type": "example-callout", "emoji": "🔤", "title": "State symbols in equations", "lines": [
                "(s) solid · (l) liquid · (g) gas · (aq) dissolved in water.",
                "2H₂(g) + O₂(g) → 2H₂O(l)",
                "NaCl(s) → Na⁺(aq) + Cl⁻(aq)",
            ]},
            {"type": "mistake-check",
             "claim": "“Melting ice or boiling water must be a chemical change, because something clearly happens.”",
             "prompt": "What is the flaw in this reasoning?",
             "options": [
                 {"text": "It is a physical change — the particles gain energy and rearrange, but the substance is unchanged (ice, water and steam are all H₂O).", "correct": True},
                 {"text": "It is a chemical change, because the water turns into a different substance when it melts or boils."},
                 {"text": "It is a chemical change, because energy has to be taken in."},
             ],
             "fix": "Melting and boiling are physical changes: the particles gain energy and move apart, but no new substance forms — ice, liquid water and steam are all still H₂O. (Use the state symbol (aq) only for something dissolved in water, not for any liquid.)"},
        ],
    },

    # ── 3 · ionic-bonding — the transfer mechanism (hero: Dot-and-Cross; static mistake kept) ──
    "ionic-bonding": {
        "hero": {"module": "dot-cross-stepper", "ns": "dotCrossStepper", "config_key": "ionic-bonding",
                 "kicker": "transfer electrons step by step"},
        "activity": {"type": "match"},
        "theory_blocks": [
            {"type": "lead",
             "text": "Ionic bonding happens between a metal and a non-metal. The metal transfers its outer electrons to the non-metal, and the oppositely charged ions that form attract one another.",
             "bold": ["metal and a non-metal"]},
            {"type": "step-sequence", "steps": [
                "The metal atom loses one or more electrons from its outer shell.",
                "The non-metal atom gains those electrons into its outer shell.",
                "Both atoms now have full outer shells — stable, like a noble gas.",
                "The metal becomes a positive ion (it lost negative electrons).",
                "The non-metal becomes a negative ion (it gained negative electrons).",
                "Opposite charges attract — this strong electrostatic attraction IS the ionic bond.",
            ]},
            {"type": "feature-cards", "cards": [
                {"emoji": "➕", "title": "Metals → positive ions", "tone": "neutral",
                 "body": "Group 1 → +1 (Na⁺), Group 2 → +2 (Mg²⁺), Group 3 → +3 (Al³⁺)."},
                {"emoji": "➖", "title": "Non-metals → negative ions", "tone": "neutral",
                 "body": "Group 7 → −1 (Cl⁻), Group 6 → −2 (O²⁻), Group 5 → −3 (N³⁻)."},
                {"emoji": "⚖️", "title": "Charges must balance", "tone": "neutral",
                 "body": "An ionic compound is overall neutral — MgCl₂ needs two Cl⁻ for one Mg²⁺."},
            ]},
            {"type": "example-callout", "emoji": "⚛️", "title": "Dot-and-cross summaries", "lines": [
                "NaCl: Na 2.8.1 loses 1e → Na⁺ (2.8); Cl 2.8.7 gains 1e → Cl⁻ (2.8.8).",
                "MgO: Mg 2.8.2 loses 2e → Mg²⁺; O 2.6 gains 2e → O²⁻.",
                "MgCl₂: Mg loses 2e → Mg²⁺; each Cl gains 1e → two Cl⁻ balance one Mg²⁺.",
            ]},
        ],
    },

    # ── 4 · ionic-compounds — giant lattice + conduction-by-state (hero: State Toggle Lab) ──
    "ionic-compounds": {
        "hero": {"module": "state-toggle-lab", "ns": "stateToggleLab", "config_key": "ionic-compounds",
                 "kicker": "change the state, test the lattice"},
        "activity": {"type": "match"},
        "theory_blocks": [
            {"type": "lead",
             "text": "When an ionic compound forms, the ions don't stay in pairs — they build a giant ionic lattice: a regular 3-D arrangement of alternating positive and negative ions.",
             "bold": ["giant ionic lattice"]},
            {"type": "feature-cards", "cards": [
                {"emoji": "🧊", "title": "Regular 3-D lattice", "tone": "neutral",
                 "body": "Positive and negative ions alternate in all directions; in NaCl each ion is surrounded by 6 of the opposite charge."},
                {"emoji": "🔗", "title": "Strong forces all directions", "tone": "neutral",
                 "body": "Billions of ions are held by strong electrostatic attraction throughout the crystal."},
            ]},
            {"type": "feature-cards", "cards": [
                {"emoji": "🌡️", "title": "High melting & boiling point", "tone": "neutral",
                 "body": "A lot of energy is needed to overcome the strong forces (NaCl 801 °C, MgO 2852 °C)."},
                {"emoji": "🚫", "title": "No conduction when solid", "tone": "limit",
                 "body": "The ions are locked in fixed positions, so no charge can move."},
                {"emoji": "⚡", "title": "Conducts molten or dissolved", "tone": "good",
                 "body": "Now the ions are free to move, so they can carry charge."},
                {"emoji": "💥", "title": "Hard but brittle", "tone": "neutral",
                 "body": "A knock shifts the layers so like charges meet and repel — the crystal shatters."},
            ]},
            {"type": "example-callout", "emoji": "🧂", "title": "Example — sodium chloride & solubility", "lines": [
                "NaCl: Na⁺ and Cl⁻ in a 1:1 ratio throughout the lattice.",
                "Many ionic compounds dissolve — water molecules surround the ions and pull them from the lattice.",
                "Some are insoluble and precipitate: Ag⁺(aq) + Cl⁻(aq) → AgCl (white solid).",
            ]},
        ],
    },

    # ── 5 · properties-ionic-compounds — charge magnitude → MP (hero-less, compare-reveal) ──
    "properties-ionic-compounds": {
        "hero": None,
        "activity": {"type": "bins", "config_key": "properties-ionic-compounds-bins"},
        "theory_blocks": [
            {"type": "lead",
             "text": "Ionic compounds have a giant ionic lattice with strong electrostatic forces in all directions between alternating positive and negative ions. That one structure explains every property. The formula shows the simplest whole-number ratio of ions.",
             "bold": ["giant ionic lattice"]},
            {"type": "compare-cards", "columns": [
                {"emoji": "🧂", "title": "NaCl (charges ±1)", "rows": [
                    {"k": "Ion charges", "v": "Na⁺ and Cl⁻"},
                    {"k": "Force strength", "v": "Strong"},
                    {"k": "Melting point", "v": "801 °C"},
                ]},
                {"emoji": "🧲", "title": "MgO (charges ±2)", "rows": [
                    {"k": "Ion charges", "v": "Mg²⁺ and O²⁻"},
                    {"k": "Force strength", "v": "Much stronger (double charges)"},
                    {"k": "Melting point", "v": "2852 °C"},
                ]},
            ], "highlight": 2,
             "verdict": "Higher ion charges → stronger attraction → higher melting point. That is why MgO melts far above NaCl."},
            {"type": "feature-cards", "cards": [
                {"emoji": "💥", "title": "Hard but brittle", "tone": "neutral",
                 "body": "A force shifts the layers so like charges align and repel — the crystal shatters rather than bending."},
                {"emoji": "🚫", "title": "No conduction when solid", "tone": "limit",
                 "body": "Ions are fixed in the lattice, so nothing can carry charge."},
                {"emoji": "⚡", "title": "Conducts molten or dissolved", "tone": "good",
                 "body": "The ions become free to move and carry the current."},
            ]},
            {"type": "compare-reveal", "title": "Tap a property to reveal the structural cause",
             "items": [
                 {"property": "High melting point", "cause": "Many strong electrostatic forces throughout the giant lattice need a lot of energy to break."},
                 {"property": "Brittle", "cause": "A knock shifts the layers; like charges line up and repel strongly, so the crystal shatters."},
                 {"property": "Conducts only when molten or dissolved", "cause": "Only then are the ions free to move — in the solid they are locked in place. Ionic compounds have no free electrons."},
                 {"property": "Often soluble in water", "cause": "Polar water molecules surround the ions and pull them away from the lattice."},
             ]},
        ],
    },

    # ── 6 · covalent-bonding — the sharing mechanism (hero: Dot-and-Cross share) · ⭐ Higher box ──
    "covalent-bonding": {
        "hero": {"module": "dot-cross-stepper", "ns": "dotCrossStepper", "config_key": "covalent-bonding",
                 "kicker": "share a pair step by step"},
        "activity": {"type": "match"},
        "theory_blocks": [
            {"type": "lead",
             "text": "Covalent bonding happens between non-metal atoms. Instead of transferring electrons, they share pairs of electrons — and each shared pair is one covalent bond.",
             "bold": ["share pairs of electrons"]},
            {"type": "step-sequence", "steps": [
                "Two non-metal atoms come together, each needing more electrons for a full shell.",
                "They share a pair of electrons — one contributed from each atom.",
                "Each atom counts the shared pair as part of its own outer shell.",
                "Both atoms reach full outer shells without either losing electrons entirely.",
                "The shared pair is attracted to BOTH nuclei — that attraction holds the atoms together, and covalent bonds are strong.",
            ]},
            {"type": "feature-cards", "cards": [
                {"emoji": "1️⃣", "title": "Single bond — 1 shared pair", "tone": "neutral",
                 "body": "H₂ shares one pair. So do H₂O (O–H), NH₃ (N–H) and CH₄ (C–H)."},
                {"emoji": "2️⃣", "title": "Double bond — 2 shared pairs", "tone": "neutral",
                 "body": "O₂ shares two pairs. CO₂ has two C=O double bonds."},
                {"emoji": "3️⃣", "title": "Triple bond — 3 shared pairs", "tone": "neutral",
                 "body": "N₂ shares three pairs — which makes it very stable."},
            ]},
        ],
    },

    # ── 9 · metallic-bonding — the electron-sea model (hero: Two-State electron sea) ──
    "metallic-bonding": {
        "hero": {"module": "two-state-compare", "ns": "twoStateCompare", "config_key": "metallic-bonding",
                 "kicker": "electron sea on / off"},
        "activity": {"type": "match"},
        "theory_blocks": [
            {"type": "lead",
             "text": "Metallic bonding occurs in metals and alloys — a regular lattice of positive metal ions surrounded by a shared sea of delocalised electrons.",
             "bold": ["delocalised electrons"]},
            {"type": "step-sequence", "steps": [
                "Metal atoms release their outer electrons, which become delocalised — free to move through the whole structure.",
                "Each atom that lost electrons is now a positive metal ion.",
                "The positive ions sit in a regular lattice.",
                "The delocalised electrons move freely between and around the ions — the 'sea of electrons'.",
                "Strong electrostatic attraction between the positive ions and the electron sea holds the metal together — this IS the metallic bond.",
            ]},
            {"type": "feature-cards", "cards": [
                {"emoji": "🌡️", "title": "High melting & boiling point", "tone": "neutral",
                 "body": "Strong forces between the many positive ions and the electron sea take a lot of energy to overcome."},
                {"emoji": "⚡", "title": "Conducts electricity", "tone": "good",
                 "body": "Delocalised electrons are free to move and carry charge through the structure."},
                {"emoji": "🔥", "title": "Conducts heat", "tone": "good",
                 "body": "The same delocalised electrons transfer thermal energy rapidly through the metal."},
                {"emoji": "🔨", "title": "Malleable & ductile", "tone": "neutral",
                 "body": "Layers of ions slide and the electron sea re-surrounds them, so metals bend and draw into wires without breaking."},
            ]},
            {"type": "example-callout", "emoji": "🧱", "title": "Example — why alloys are harder", "lines": [
                "In a pure metal every ion is the same size, so layers slide easily → soft.",
                "An alloy mixes in different-sized atoms that disrupt the regular lattice.",
                "The layers can no longer slide as easily → the alloy is harder and stronger (steel, bronze, brass).",
            ]},
        ],
    },

    # ── 10 · metals-alloys — structure→property + alloys (hero: Two-State metalLayers + force) ──
    "metals-alloys": {
        "hero": {"module": "two-state-compare", "ns": "twoStateCompare", "config_key": "metals-alloys",
                 "kicker": "apply a force to pure metal vs alloy"},
        "activity": {"type": "match"},
        "theory_blocks": [
            {"type": "lead",
             "text": "Metals have giant metallic structures — a regular lattice of positive metal ions surrounded by a sea of delocalised electrons. That structure explains all their properties.",
             "bold": ["giant metallic structures"]},
            {"type": "feature-cards", "cards": [
                {"emoji": "🌡️", "title": "High melting & boiling point", "tone": "neutral",
                 "body": "Strong forces between the positive ions and the electron sea (exceptions: mercury and gallium are liquid near room temperature)."},
                {"emoji": "🔨", "title": "Malleable & ductile", "tone": "neutral",
                 "body": "Layers of ions slide and the electron sea re-accommodates them — so metals hammer into shape and draw into wires."},
                {"emoji": "⚡", "title": "Conducts electricity & heat (as a solid)", "tone": "good",
                 "body": "Delocalised electrons are free to move even in the solid, carrying both charge and thermal energy."},
                {"emoji": "⚖️", "title": "High density", "tone": "neutral",
                 "body": "A close-packed lattice of heavy atoms makes most metals dense."},
            ]},
            {"type": "example-callout", "emoji": "🏗️", "title": "Key alloys and their uses", "lines": [
                "Steel (iron + carbon) — much harder than iron → construction, tools, vehicles.",
                "Stainless steel (iron + chromium + nickel) — resists corrosion → cutlery, surgical instruments.",
                "Bronze (copper + tin) — harder than copper → propellers, statues, bearings.",
                "Brass (copper + zinc) — golden, harder than copper → instruments, taps.",
                "Aluminium alloys — strong and lightweight → aircraft, spacecraft.",
            ]},
        ],
    },

    # ── 11 · nanoparticles — SA:V + carbon nanostructures (hero: FIFA) · ⭐ Higher · Triple-only ──
    "nanoparticles": {
        "hero": {"module": "fifa-step-reveal", "ns": "fifaStepReveal", "build": "fifa",
                 "kicker": "work the surface-area-to-volume calculation"},
        "activity": {"type": "match"},
        "theory_blocks": [
            {"type": "lead",
             "text": "Nanoparticles are tiny particles 1–100 nm across (1 nm = 1×10⁻⁹ m), containing a few hundred to a few thousand atoms. At this scale a material can behave very differently from its bulk form.",
             "bold": ["1–100 nm"]},
            {"type": "compare-cards", "columns": [
                {"emoji": "🟡", "title": "Bulk gold", "rows": [
                    {"k": "Colour", "v": "Yellow"},
                    {"k": "Reactivity", "v": "Low — unreactive with most chemicals"},
                    {"k": "Melting point", "v": "1064 °C"},
                ]},
                {"emoji": "🔴", "title": "Gold nanoparticles", "rows": [
                    {"k": "Colour", "v": "Red / purple"},
                    {"k": "Reactivity", "v": "Much higher"},
                    {"k": "Melting point", "v": "Much lower"},
                ]},
            ], "highlight": 1,
             "verdict": "Same gold atoms — but a huge surface-area-to-volume ratio means far more atoms sit on the surface, so reactivity shoots up."},
            {"type": "feature-cards", "cards": [
                {"emoji": "▦", "title": "Graphene", "tone": "neutral",
                 "body": "A single layer of graphite, one atom thick — extremely strong, very light, and conducts electricity."},
                {"emoji": "⚽", "title": "Buckminsterfullerene (C₆₀)", "tone": "neutral",
                 "body": "60 carbon atoms in a hollow sphere ('buckyball') — can cage molecules; used in drug delivery and lubricants."},
                {"emoji": "🛢️", "title": "Carbon nanotube", "tone": "neutral",
                 "body": "A rolled-up graphene sheet forming a hollow tube — very strong along its length and conducts electricity."},
            ]},
            {"type": "example-callout", "emoji": "✅", "title": "Uses of nanoparticles", "lines": [
                "Sunscreen: TiO₂ nanoparticles are transparent but still block UV.",
                "Antibacterial: silver nanoparticles — high surface area → very reactive against bacteria.",
                "Catalysis: a high surface area makes them very effective catalysts.",
                "Drug delivery: they can carry medicine directly to target cells.",
            ]},
            {"type": "aside-callout", "title": "⚠️ Risks — why more research is needed",
             "body": "Nanoparticles are so small they may pass through cell membranes, be breathed deep into the lungs, and persist in the environment and food chains. Their long-term health and environmental effects are not yet fully understood."},
        ],
    },

    # ── 8 · polymers — long chains + addition polymerisation (hero-less, mistake-check) · Key Equations ──
    "polymers": {
        "hero": None,
        "activity": {"type": "match"},
        "theory_blocks": [
            {"type": "lead",
             "text": "Polymers are very large molecules made from many small repeating units called monomers, joined into long chains. The joining process is called polymerisation.",
             "bold": ["monomers"]},
            {"type": "feature-cards", "cards": [
                {"emoji": "🔹", "title": "Monomer", "tone": "neutral",
                 "body": "A small molecule that can join with others — e.g. ethene, CH₂=CH₂."},
                {"emoji": "⛓️", "title": "Polymer", "tone": "neutral",
                 "body": "The long chain formed from thousands of monomers — e.g. poly(ethene)."},
                {"emoji": "🔁", "title": "Repeating unit", "tone": "neutral",
                 "body": "Written in brackets with n outside: [—CH₂—CH₂—]ₙ."},
            ]},
            {"type": "step-sequence", "steps": [
                "Addition polymerisation uses monomers that contain a C=C double bond.",
                "The double bond opens up — one bond breaks and frees a pair of electrons.",
                "Those electrons form a new bond to the next monomer.",
                "The monomers link into a long saturated chain (no double bonds left) — and no atoms are lost.",
            ]},
            {"type": "feature-cards", "cards": [
                {"emoji": "🧊", "title": "Solid at room temperature", "tone": "neutral",
                 "body": "Long chains and reasonable intermolecular forces keep polymers solid and flexible."},
                {"emoji": "🚫", "title": "Electrical insulators", "tone": "limit",
                 "body": "No free electrons or ions, so they do not conduct electricity."},
                {"emoji": "🔥", "title": "Thermoplastic vs thermosetting", "tone": "neutral",
                 "body": "Thermoplastics soften when heated and reshape; thermosetting polymers form cross-links and stay hard."},
            ]},
            {"type": "mistake-check",
             "claim": "“Polymers must be giant covalent structures, because their chains are so huge.”",
             "prompt": "What is the flaw in this reasoning?",
             "options": [
                 {"text": "A polymer is a large molecule — its chains are held to each other only by weak intermolecular forces, not by covalent bonds running all the way through.", "correct": True},
                 {"text": "Polymers really are giant covalent structures, just like diamond."},
                 {"text": "Polymer chains are held together by ionic bonds between the monomers."},
             ],
             "fix": "A polymer is a very large molecule, but its separate chains are held together only by weak intermolecular forces — which is why polymers melt far below diamond, where strong covalent bonds run all the way through the structure."},
        ],
    },
}
