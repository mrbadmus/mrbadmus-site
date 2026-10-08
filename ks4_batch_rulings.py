#!/usr/bin/env python3
"""ks4_batch_rulings.py — the port mechanics for a batch whose lessons are
DESIGN'S OWN delivery, placed verbatim (docs/ks4/design-reference/batch-4/).

Batches 2 and 3 were authored in their final form (docs/ks4/batch-engine.md
§2), so their compile path has nothing to fix up. Batch 4 is Design's
delivery, which still carries the review-tool shape the pilot's rulings
remove: a Route <select>, two static "Combined · Triple" / "Foundation ·
Higher" chips, hard-coded `.dc.html` prev/next and connects hrefs, and the
Ks4Practice number parse. This module applies exactly the pilot's rulings
for each of those, GENERICALLY (the pilot's own functions in ks4_rulings.py
are keyed by pilot design_file / slug and stay untouched), so the lesson
files on disk remain byte-identical to Design's (MD5SUMS) and every change
is a named, fail-loud ruling rather than a hand edit.

  B-R1      Route <select> dropped            (= ks4_rulings R1)
  B-R12     two header chips -> ONE route chip (= ks4_rulings R12; a
            Triple-only lesson's "Triple only" chip is the pathway span)
  B-PREVNEXT endPrev/endNext -> this.props.mrbPrevNext (= R-PREVNEXT)
  B-CONNECTS `X.dc.html` hrefs -> KS4.hrefFor('<slug>', R) (= R-CONNECTS,
            resolved against THIS batch's source files)
  B-PRACTICE-PARSE Ks4Practice's calc number parse reads "6,3" as 6.3 and
            "63,000" as 63000 (= R16 for the new block)

Applied only to a lesson record carrying `port_rulings=True`; batches 2 and
3 never carry it, so their bytes cannot move.
"""
import re

import ks4_rulings
from ks4_rulings import RulingError, _require


def _chip(slug, tpl):
    _require(tpl, ks4_rulings.R12_TIER_LINE, slug, "B-R12 (tier span)")
    tpl = tpl.replace(ks4_rulings.R12_TIER_LINE, "", 1)
    std = ks4_rulings.R12_PATHWAY_STD_SPAN
    only = std.replace("Combined · Triple", "Triple only")
    if tpl.count(std) == 1:
        pathway = std
    else:
        pathway = only
    _require(tpl, pathway, slug, "B-R12 (pathway span)")
    return tpl.replace(pathway, ks4_rulings.R12_CHIP_BLOCK, 1)


_HREF_RE = re.compile(r"href: '([\w.\-]+)\.dc\.html'")


def apply_connects(source_file, logic, slug_by_file):
    replaced = []

    def sub(m):
        f = m.group(1) + ".dc.html"
        if f not in slug_by_file:
            raise RulingError(
                "ks4_batch_rulings B-CONNECTS: %s links to %r, which is not "
                "one of this batch's lessons." % (source_file, f))
        replaced.append(slug_by_file[f])
        return "href: KS4.hrefFor('%s', R)" % slug_by_file[f]
    return _HREF_RE.sub(sub, logic), replaced


PRACTICE_PARSE_FROM = "const v = parseFloat(String(st.num).replace(/[\\s,]/g, ''));"
PRACTICE_PARSE_TO = ("const v = (" + ks4_rulings.R16_PARSE_FN + ")(st.num); // ⊕ B-PRACTICE-PARSE (R16 for Ks4Practice)")


def apply_practice_parse(text):
    _require(text, PRACTICE_PARSE_FROM, "Ks4Practice.dc.html", "B-PRACTICE-PARSE")
    return text.replace(PRACTICE_PARSE_FROM, PRACTICE_PARSE_TO, 1)


# ═══════════════════════════════════════════════════════════════════════
# SCIENCE RULINGS — named, fail-loud (exactly one occurrence), each logged in
# docs/ks4/BATCH4-SCIENCE-LOG.md with its source line. Design's files stay
# byte-identical on disk; these are applied at compile time only.
# ═══════════════════════════════════════════════════════════════════════
_P_TRANS_OLD = ('<p style="margin: 14px 0 0; font-size: 17px; line-height: 1.55; max-width: 62ch;">'
                'The transition metals, between Groups 2 and 3, have their own lesson on the Triple route.</p>')
SCIENCE = [
    # Mide's ruling (TASK-AA): hot-metal colours. A 700 C stop is added (the
    # slider's six stops had no stop at which "dull red" was true); the Planck
    # functions and every peak value are untouched.
    dict(id="B4-IRB-GLOW-1", slug="infrared-black-bodies", layer="logic",
         old="const TEMPS = [500, 1000, 1500, 2500, 3500, 5500];",
         new="const TEMPS = [500, 700, 1000, 1500, 2500, 3500, 5500]; // \u2295 B4-IRB-GLOW"),
    dict(id="B4-IRB-GLOW-2", slug="infrared-black-bodies", layer="logic",
         old=("  ['A dull red glow.', 'Enough of the longest visible wavelengths are now emitted to see.'],\n"
              "  ['Orange.', 'More of the visible band is emitted, and more at shorter wavelengths. The peak is still in the infrared.'],\n"
              "  ['Yellow-white.', 'All visible wavelengths are emitted strongly. The peak is still in the infrared.'],\n"
              "  ['White.', 'The peak has nearly reached the visible band.'],\n"),
         new=("  ['A dull red glow.', 'Enough of the longest visible wavelengths are now emitted to see. The peak is still in the infrared.'],\n"
              "  ['Orange.', 'More of the visible band is emitted, and more at shorter wavelengths. The peak is still in the infrared.'],\n"
              "  ['Yellow-white.', 'All visible wavelengths are emitted strongly. The peak is still in the infrared.'],\n"
              "  ['White.', 'All the visible wavelengths mix, so it looks white. The peak is still in the infrared.'],\n"
              "  ['White.', 'The peak has nearly reached the visible band.'],\n")),
    dict(id="B4-IRB-GLOW-3", slug="infrared-black-bodies", layer="logic",
         old="hook: null, ti: 1, moved: false,", new="hook: null, ti: 2, moved: false,"),
    dict(id="B4-IRB-GLOW-4", slug="infrared-black-bodies", layer="template",
         old='min="0" max="5" step="1" value="{{ ti }}"', new='min="0" max="6" step="1" value="{{ ti }}"'),
    # infrared: its renderVals returns a fresh object rather than spreading the
    # route helper, so the one route chip (B-R12) got no words or menu.
    dict(id="B4-IRB-CHIP", slug="infrared-black-bodies", layer="logic",
         old="route, onRoute: R.onRoute, isHigher,",
         new="route, onRoute: R.onRoute, isHigher, routeWords: R.routeWords, routeSwitchOptions: R.routeSwitchOptions,"),

    # ── Stage 2b ────────────────────────────────────────────────────────
    # biodiversity 11.2 (Mide): the sort covers the three threats only;
    # hedgerows, breeding programmes and field margins belong to
    # maintaining-biodiversity. One bin would be a degenerate sort, so the
    # bins become the three threats and the cards are examples of each, worded
    # from Design's own "Human activity" section.
    dict(id="B4-BIO-SORT-1", slug="biodiversity", layer="template",
         old=('title="Reduces biodiversity, or helps maintain it?" prompt="Place each human activity." '),
         new=('title="Which threat is it?" prompt="Place each example with the human activity behind it." ')),
    dict(id="B4-BIO-SORT-2", slug="biodiversity", layer="template",
         old=('done-note="Pollution, habitat destruction and climate change reduce biodiversity; protecting and recreating habitats helps maintain it."'),
         new=('done-note="Waste pollutes, deforestation destroys habitats and global warming changes them: each reduces biodiversity."')),
    dict(id="B4-BIO-SORT-3", slug="biodiversity", layer="logic",
         old=r"""      sortBins: [{ id: 'r', label: 'Reduces biodiversity' }, { id: 'm', label: 'Helps maintain it' }],
      sortItems: [
        { text: 'Dumping waste into a river', bin: 'r', why: 'Pollution kills organisms.' },
        { text: 'Clearing rainforest for farmland', bin: 'r', why: 'Habitats are destroyed.' },
        { text: 'Global warming shifting habitats', bin: 'r', why: 'Some species can\u2019t adapt or move fast enough.' },
        { text: 'Replanting hedgerows around fields', bin: 'm', why: 'Hedgerows are habitats for many species.' },
        { text: 'Breeding programmes for endangered species', bin: 'm', why: 'They protect species at risk.' },
        { text: 'Leaving field margins to grow wild', bin: 'm', why: 'More plants support more insects and birds.' }
      ],""",
         new=r"""      sortBins: [{ id: 'w', label: 'Waste' }, { id: 'd', label: 'Deforestation' }, { id: 'g', label: 'Global warming' }],
      sortItems: [
        { text: 'Dumping waste into a river', bin: 'w', why: 'Pollution kills organisms.' },
        { text: 'Pollution of the air', bin: 'w', why: 'Pollution of land, water and air kills plants and animals.' },
        { text: 'Clearing rainforest for farmland', bin: 'd', why: 'Habitats are destroyed.' },
        { text: 'Cutting down the trees many species live in', bin: 'd', why: 'The species lose their habitat.' },
        { text: 'Global warming shifting habitats', bin: 'g', why: 'Some species can\u2019t adapt or move fast enough.' },
        { text: 'A climate that changes faster than species can cope', bin: 'g', why: 'Habitats change faster than some species can cope with.' }
      ],"""),


    # ── Stage 2b review fixes (display only; no words or numbers change) ────
    # efficiency: at the default 10% preset the wasted-energy arrowhead ends at
    # y = 387 in a 380-high drawing, so it overshoots the box (0% reaches 396).
    dict(id="B4-EFF-SANKEY", slug="efficiency", layer="logic",
         old="return D.svg(620, 380, p, 'Sankey diagram to scale",
         new="return D.svg(620, 410, p, 'Sankey diagram to scale"),
    # transport: the three one-line captions under the membrane panels are each
    # wider than their panel, so they overlap and clip at phone width. Each is
    # split at its own middle dot onto two lines (Design's words, unchanged).
    dict(id="B4-TIC-CAPTIONS-1", slug="transport-in-cells", layer="logic",
         old="D.T(ox + 106, 284, sub, 13, { weight: 'normal', fill: C.stroke })",
         new=("sub.split(' ' + String.fromCharCode(183) + ' ').map((ln, k) => D.T(ox + 106, 280 + k * 17, ln, 13, "
              "{ weight: 'normal', fill: C.stroke })).join('')")),
    dict(id="B4-TIC-CAPTIONS-2", slug="transport-in-cells", layer="logic",
         old="return D.svg(644, 300, b, 'Three panels across a membrane.",
         new="return D.svg(644, 308, b, 'Three panels across a membrane."),

    # thermal-conductivity: the "about the same" verdict described the changes
    # the wrong way round (a third as thick would raise the rate ninefold).
    dict(id="B4-TC-VERDICT", slug="thermal-conductivity", layer="logic",
         old=("One change raises the rate as much as the other lowers it: here the material conducts about "
              "three times better but the wall is a third as thick, or the reverse."),
         new="One change raises the rate threefold and the other lowers it threefold, so they cancel out."),
    # periodic-table: pack F1 — transition metals are Triple only; a pointer to
    # "the Triple route" is shown on Triple routes only.
    dict(id="B4-PT-F1", slug="periodic-table", layer="template", old=_P_TRANS_OLD,
         new='<sc-if value="{{ isTriple }}">' + _P_TRANS_OLD + '</sc-if>'),
    # development-periodic-table: potassium was known long before argon.
    dict(id="B4-DPT-F3", slug="development-periodic-table", layer="template",
         old="Argon and potassium, found later, show the same thing.",
         new="Argon, found later, and potassium show the same thing."),
    # atmospheric-pollutants: a camping stove flame does make some NOx; the
    # reply must not say it is "not hot enough". And catalytic converters are
    # off-spec (pack F2/F8): not even as a distractor in practice.
    dict(id="B4-AP-STOVE", slug="atmospheric-pollutants", layer="logic",
         old="A camping stove is not hot enough; the issue is the oxygen running out.",
         new="Oxides of nitrogen are linked to the high temperatures in engines. Here the danger is the oxygen running out."),
    dict(id="B4-AP-F2", slug="atmospheric-pollutants", layer="logic",
         old="['The catalytic converter', false]", new="['The engine oil', false]"),

    # ── Lane rulings (Prompt AB, 8 Oct 2026) ─────────────────────────────
    # uses-em-waves CH TH: the ionosphere item ("radio waves reflect off it" is
    # true only of long/medium/short-wave radio) and the UV-sterilisation item
    # (off-spec, and the lesson itself says gamma sterilises equipment) go.
    # Each is replaced by a "why it suits the job" item on the SAME wave, from
    # the lesson's own Higher list of uses; the Higher bank stays five.
    dict(id="B4-UEM-HQ", slug="uses-em-waves", layer="logic",
         old=r'''    const hq = [
      { q: 'Why are microwaves used for satellite communications rather than radio waves?', opts: [['Microwaves pass through the ionosphere \u2014 radio waves reflect off it, preventing them from reaching satellites in orbit', true], ['Microwaves are more powerful \u2014 they reach greater distances than radio waves', false], ['Radio waves are dangerous at high altitude \u2014 microwaves are safer for satellite use', false], ['Satellites can only detect microwaves \u2014 their receivers are not compatible with radio waves', false]],
        wrong_explanations: { 1: 'Power determines signal strength at a given distance \u2014 but all EM waves travel at the same speed. The key distinction is IONOSPHERE INTERACTION.', 2: 'Safety is not the relevant factor \u2014 the ionosphere physically reflects (most) radio waves back to Earth.', 3: 'This is backwards \u2014 it\u2019s the PHYSICS of ionosphere reflection, not receiver incompatibility, that determines which EM type is used.' } },
      { q: 'UV light is used to sterilise medical equipment. Why is UV effective for this?', opts: [['UV has enough energy to damage DNA in microorganisms \u2014 killing or inactivating bacteria and viruses', true], ['UV heats the equipment to high temperatures, killing microorganisms by heat', false], ['UV is absorbed by metal \u2014 heating the equipment surface to kill bacteria', false], ['UV converts oxygen to ozone, which then kills bacteria chemically', false]],
        wrong_explanations: { 1: 'UV can cause some warming but it\u2019s not the primary mechanism \u2014 UV sterilisation works through DNA damage (photochemical action), not significant heating.', 2: 'UV sterilisation is used for transparent surfaces, water, and air \u2014 metal surfaces are typically sterilised by heat or chemicals.', 3: 'UV can produce some ozone, but the primary sterilisation mechanism is direct DNA damage from UV photons \u2014 not ozone.' } }
    ];
''',
         new=r'''    const hq = [
      { q: 'Why are microwaves used to cook food?', opts: [['They are absorbed by water molecules in the food, transferring energy to its thermal store', true], ['They pass straight through the food without being absorbed', false], ['They are ionising, so they break up the molecules in the food', false], ['They are reflected by the food, which heats its surface', false]],
        wrong_explanations: { 1: 'If they passed straight through, no energy would be transferred to the food. Water molecules in the food absorb them.', 2: 'Microwaves are not ionising. They heat food because water molecules in it absorb them.', 3: 'The food absorbs microwaves, mostly in its outer layers; the inside heats by conduction.' } },
      { q: 'Why is ultraviolet used in energy efficient lamps?', opts: [['A coating inside the lamp absorbs the ultraviolet and gives out visible light', true], ['Ultraviolet is visible, so the lamp shines it straight out', false], ['Ultraviolet heats the glass until it glows', false], ['Ultraviolet passes through the coating and lights the room directly', false]],
        wrong_explanations: { 1: 'Ultraviolet is not visible. The coating inside the lamp absorbs it and gives out visible light.', 2: 'The lamp does not glow because it is hot. The coating absorbs the ultraviolet and gives out visible light.', 3: 'The coating absorbs the ultraviolet. The light you see is the visible light the coating gives out.' } }
    ];
'''),
    # atmospheric-pollutants: the predictor's limited-oxygen line follows the
    # spec, "carbon monoxide and/or carbon (soot)", not "CO and soot together".
    dict(id="B4-AP-ANDOR", slug="atmospheric-pollutants", layer="logic",
         old="'Too little oxygen: carbon monoxide and particulates as well as carbon dioxide.'",
         new="'Too little oxygen: carbon monoxide and/or carbon (soot), as well as carbon dioxide.'"),
]
APPLIED = []


def apply_science(slug, layer, text):
    for r in SCIENCE:
        if r["slug"] != slug or r["layer"] != layer:
            continue
        n = text.count(r["old"])
        if n != 1:
            raise RulingError("ks4_batch_rulings %s: expected exactly 1 occurrence in %s (%s), found %d.\n  looking for: %r"
                              % (r["id"], slug, layer, n, r["old"][:160]))
        text = text.replace(r["old"], r["new"], 1)
        APPLIED.append(r["id"])
    return text


def port_lesson(lesson, tpl, logic, slug_by_file):
    """-> (tpl, logic, report-dict)."""
    src = lesson["source_file"]
    tpl = ks4_rulings.apply_r1_route_selector(src, tpl)
    tpl = _chip(lesson["slug"], tpl)
    logic, n_prev, n_next = ks4_rulings.apply_r_prevnext(src, logic)
    logic, connects = apply_connects(src, logic, slug_by_file)
    tpl = apply_science(lesson["slug"], "template", tpl)
    logic = apply_science(lesson["slug"], "logic", logic)
    # B-R12's chip reads routeWords / routeSwitchOptions off the render values.
    if "Object.assign({}, R," not in logic and "routeWords" not in logic:
        raise RulingError("ks4_batch_rulings B-R12: %s's renderVals neither spreads the route helper nor "
                          "passes routeWords; the route chip would render empty." % lesson["slug"])
    return tpl, logic, dict(has_prev=bool(n_prev), has_next=bool(n_next), connects=connects)


# ── block rulings (applied to a batch's OWN copy of a shared block, in compile_block) ──
TRI_CELL_FROM = "style: 'position:absolute;left:' + at[0] + '%;top:' + at[1] + '%;transform:translate(-50%,-50%);font:inherit;font-family:var(--ks3-font-display);font-weight:800;font-size:' + fs + 'px;"
TRI_CELL_TO = ("style: 'position:absolute;left:' + at[0] + '%;top:' + at[1] + '%;transform:translate(-50%,-50%);font:inherit;font-family:var(--ks3-font-display);font-weight:800;font-size:' + "
               "((key === 'top' && String(label).length >= 5) ? Math.round(fs * 0.7) : (key === 'top' && String(label).length === 4) ? Math.round(fs * 0.85) : fs) + 'px;")
TRI_AT_FROM = "top: { points: '150,0 225,130 75,130', at: P(150, 90) },"
TRI_AT_TO = "top: { points: '150,0 225,130 75,130', at: P(150, 94) },"


def apply_triangle_top_label(logic):
    """B4-TRI-TOP: the top label (useful, \u0394m, V, N, SA) is set in the same size as the
    bottom ones, so a long one ('useful') is wider than the apex it sits in and the triangle's
    sides cross its letters, with its underline hard against the divider. Long labels are set
    smaller and the whole label sits slightly lower; cells, hit areas and words are unchanged."""
    _require(logic, TRI_CELL_FROM, "Ks4Triangle.dc.html", "B4-TRI-TOP")
    _require(logic, TRI_AT_FROM, "Ks4Triangle.dc.html", "B4-TRI-TOP")
    return logic.replace(TRI_CELL_FROM, TRI_CELL_TO, 1).replace(TRI_AT_FROM, TRI_AT_TO, 1)
