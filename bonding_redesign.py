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
}
