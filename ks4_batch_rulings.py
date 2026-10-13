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
    # ⊕ Batch 8: its Triple-only lessons draw the pathway pill as plain "Triple" (batch 7 wrote "Triple only"). The
    # batch 4-7 candidates are tried first, in the same order, so their builds cannot move.
    triple = std.replace("Combined · Triple", "Triple")
    if tpl.count(std) == 1:
        pathway = std
    elif tpl.count(only) == 1 or tpl.count(triple) != 1:
        pathway = only
    else:
        pathway = triple
    _require(tpl, pathway, slug, "B-R12 (pathway span)")
    return tpl.replace(pathway, ks4_rulings.R12_CHIP_BLOCK, 1)


# ⊕ Batch 5 (Prompt AB): a connects link may also name a lesson of ANOTHER batch,
# written by Design as `../KS4 Batch 4/<file>.dc.html`. The prefix is optional so every
# batch-4 href matches and resolves exactly as before. A file in neither this batch nor
# any other registered batch is a loud failure, never a left-over `.dc.html`.
# ⊕ Batch 6: Design's cross-batch prefix is `../../Batch 5/lessons/` (batch 5 wrote `../KS4 Batch 4/`), so the
# prefix is any run of `../`, an optional `KS4 `, `Batch N/` and an optional `lessons/`. A superset of batch 5's.
_XB = r"(?:(?:\.\./)+(?:KS4 )?Batch \d+/(?:lessons/)?)?"
_HREF_RE = re.compile(r"href: '" + _XB + r"([\w.\-]+)\.dc\.html'")


def apply_connects(source_file, logic, slug_by_file, other_slug_by_file=None):
    replaced = []
    other = other_slug_by_file or {}
    # ⊕ Batch 7: its renderVals holds the route flags on `const c = this.common(done)`, with no bare `R`
    # (the batch-4..6 pages spread `R`). The batch-4..6 spelling is unchanged.
    rvar = "c" if "const c = this.common(" in logic and "Object.assign({}, R," not in logic else "R"

    def sub(m):
        f = m.group(1) + ".dc.html"
        slug = slug_by_file.get(f) or other.get(f)
        if not slug:
            raise RulingError(
                "ks4_batch_rulings B-CONNECTS: %s links to %r, which is not "
                "one of this batch's lessons nor any registered lesson." % (source_file, f))
        replaced.append(slug)
        return "href: KS4.hrefFor('%s', %s)" % (slug, rvar)
    return _HREF_RE.sub(sub, logic), replaced


# ⊕ B-INLINE-LINKS (batch 5): an in-text `<a href="ks4-….dc.html">` in a template. A static
# attribute cannot carry a per-route URL, so each becomes a bound value, filled by renderVals
# from KS4.hrefFor (the same resolver the connects use). Fail-loud on every unmatched file and
# on a renderVals that does not return through the route helper.
_TPL_HREF_RE = re.compile(r'href="' + _XB + r'([\w.\-]+)\.dc\.html"')
_RV_ANCHOR = "return Object.assign({}, R, {"
_RV_ANCHOR_C = "return Object.assign(c, {"


def apply_inline_links(source_file, tpl, logic, slug_by_file, other_slug_by_file=None):
    found = []
    other = other_slug_by_file or {}

    def sub(m):
        f = m.group(1) + ".dc.html"
        slug = slug_by_file.get(f) or other.get(f)
        if not slug:
            raise RulingError(
                "ks4_batch_rulings B-INLINE-LINKS: %s links to %r, which is not "
                "one of this batch's lessons nor any registered lesson." % (source_file, f))
        if slug not in found:
            found.append(slug)
        return 'href="{{ mrbLink_%s }}"' % slug.replace("-", "_")
    tpl = _TPL_HREF_RE.sub(sub, tpl)
    if found:
        # ⊕ Batch 7: its renderVals builds `const c = this.common(done)` and returns
        # `Object.assign(c, {...})`; the route flags live on `c`, not on a bare `R`. The batch-4..6
        # anchor is tried first and unchanged, so those builds cannot move.
        anchor, rvar = _RV_ANCHOR, "R"
        if logic.count(_RV_ANCHOR) == 0 and logic.count(_RV_ANCHOR_C) == 1:
            anchor, rvar = _RV_ANCHOR_C, "c"
        if logic.count(anchor) != 1:
            raise RulingError(
                "ks4_batch_rulings B-INLINE-LINKS: %s needs %r exactly once in renderVals (found %d)."
                % (source_file, anchor, logic.count(anchor)))
        vals = " ".join("mrbLink_%s: (KS4.hrefFor('%s', %s) || '#')," % (sl.replace("-", "_"), sl, rvar) for sl in found)
        logic = logic.replace(anchor, anchor + " " + vals, 1)
    return tpl, logic, found


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
    # ═══ Batch 5 science rulings (Prompt AB, 8 Oct 2026; audit by the lead) ═══
    # earths-resources 8.3 (lane): the spec sentence, 8464 5.10.1.1 / 8462 4.10.1.1,
    # verbatim (pack examination/earths-resources.md:15). Template, "Sustainable development" card.
    dict(id="B5-ER-SPEC", slug="earths-resources", layer="template",
         old="Development that meets the needs of current generations without compromising the ability of future generations to meet their own needs. Chemistry plays an important role, improving agricultural and industrial processes to provide new products.",
         new="Chemistry plays an important role in improving agricultural and industrial processes to provide new products and in sustainable development, which is development that meets the needs of current generations without compromising the ability of future generations to meet their own needs."),
    # energy-resources ENERGY-RESOURCES-F6: q2 wx2 is shown; intermittent = variable, weather-dependent (wx1's words).
    dict(id="B5-ENR-F6", slug="energy-resources", layer="logic",
         old="specifically means UNPREDICTABLE output dependent on weather, not overproduction.",
         new="means VARIABLE, WEATHER-DEPENDENT output, not overproduction."),
    # energy-resources 4.2 (lane: keep the made-up country, labelled as not real data): label it
    # where the pupil reads the chart, not only in the end note.
    dict(id="B5-ENR-LABEL", slug="energy-resources", layer="template",
         old="Exams give you a chart like this one and ask you to describe the trend, then explain it.",
         new="This country is made up and its figures are not real data. Exams give you a chart like this one and ask you to describe the trend, then explain it."),
    # plant-tissues PLANT-TISSUES-F6: drop the doubtful concession; it contradicts rung 4's reject "Stomata take in water."
    dict(id="B5-PT-F6", slug="plant-tissues", layer="logic",
         old="Stomata can absorb some water vapour in humid conditions, but their primary function is gas EXCHANGE, not water absorption.",
         new="Stomata are pores for gas EXCHANGE, not water absorption: water enters the plant through the roots."),
    # metals-non-metals 2.2: boron (3 outer electrons) is shown as a non-metal straight after
    # "metals have 1, 2 or 3"; name it as the exception, as hydrogen's line already does.
    dict(id="B5-MNM-B", slug="metals-non-metals", layer="logic",
         old="else if (pl.g === 4 || pl.g === 3) line = out + ' outer electrons. It shares electrons in covalent bonds and does not form positive ions.';",
         new="else if (pl.g === 4 || pl.g === 3) line = out + ' outer electrons' + (pl.g === 3 ? ', but boron is a non-metal' : '') + '. It shares electrons in covalent bonds and does not form positive ions.';"),
    # metals-non-metals 2.2: hydrogen's info head read "Group 1"; the page says it "sits on its own at the top".
    dict(id="B5-MNM-H", slug="metals-non-metals", layer="logic",
         old="const grp = pl.g === 8 ? 'Group 0' : 'Group ' + pl.g;",
         new="const grp = e[0] === 'H' ? 'not in a group' : pl.g === 8 ? 'Group 0' : 'Group ' + pl.g;"),
    # reactivity-series: the displacement feedback starts a sentence with the metal's name, which
    # NAME stores in lower case ("Not this time. copper is less reactive…"). Capitalise it; words unchanged.
    dict(id="B5-RS-CAP-1", slug="reactivity-series", layer="logic",
         old="      ? NAME[strip] + ' is more reactive than '",
         new="      ? NAME[strip].charAt(0).toUpperCase() + NAME[strip].slice(1) + ' is more reactive than '"),
    dict(id="B5-RS-CAP-2", slug="reactivity-series", layer="logic",
         old="      : NAME[strip] + ' is less reactive than '",
         new="      : NAME[strip].charAt(0).toUpperCase() + NAME[strip].slice(1) + ' is less reactive than '"),
    # ── Batch 5 port mechanic (not a science ruling) ───────────────────────
    # red-shift-big-bang: its renderVals returns a fresh object rather than spreading the
    # route helper (as batch 4's infrared did), so the one route chip (B-R12) got no words
    # and no menu. Same repair as B4-IRB-CHIP.
    dict(id="B5-RSBB-CHIP", slug="red-shift-big-bang", layer="logic",
         old="      route, onRoute: R.onRoute,\n      tripleOptions:",
         new="      route, onRoute: R.onRoute, routeWords: R.routeWords, routeSwitchOptions: R.routeSwitchOptions,\n      tripleOptions:"),
    # ═══ Batch 6 science rulings (Prompt AB, 8 Oct 2026; audit by the lead) ═══
    # animal-plant-cells 5.3: the estimation task keys "about three quarters", but the vacuole is
    # drawn at 92x58 in a 118x78 cell (58%, reads as about half). Redraw so the figure matches the
    # taught answer. FINAL GEOMETRY (builder): vacuole 95x70 at (x+17, y+4) = 6650 = 72.3% of the 118x78
    # cell (9204) and 75.4% of its inside once the 2-wide wall is taken off (116x76 = 8816); nucleus r6
    # at (x+8, y+39) spans x+2..x+14, against the wall and 3 clear of the vacuole's left edge (x+17).
    dict(id="B6-APC-VACUOLE-1", slug="animal-plant-cells", layer="logic",
         old="""b += '<rect x="' + (x + 14) + '" y="' + (y + 10) + '" width="92" height="58" rx="8" fill="#FBF3DD" stroke="#C9A75A" stroke-width="1"/>';""",
         new="""b += '<rect x="' + (x + 17) + '" y="' + (y + 4) + '" width="95" height="70" rx="8" fill="#FBF3DD" stroke="#C9A75A" stroke-width="1"/>';"""),
    dict(id="B6-APC-VACUOLE-2", slug="animal-plant-cells", layer="logic",
         old="b += D.circ(x + 20, y + 20, 7, '#A97B2E', 'none', 0);",
         new="b += D.circ(x + 8, y + 39, 6, '#A97B2E', 'none', 0);"),
    # culturing-microorganisms: school cultures are kept at or below 25 C for SAFETY (the page's own
    # Think again), not because warmth speeds growth.
    dict(id="B6-CM-HOOK", slug="culturing-microorganisms", layer="template",
         old="Warmth speeds growth, which is why school cultures are kept no warmer than 25",
         new="Warmth speeds growth. For safety, school cultures are kept no warmer than 25"),
    # digestive-system: bread contains protein (about 8-10%) and turns Biuret purple; the simulator's
    # starch-only food becomes cornflour. BUILDER: check no other string on the page still says bread
    # for this sample.
    dict(id="B6-DS-FOOD", slug="digestive-system", layer="logic",
         old="{ label: 'Bread', r: [true, false, false, false] }",
         new="{ label: 'Cornflour', r: [true, false, false, false] }"),
    # transpiration 13.4: dist() clamped at 4 mm, so in two toggle cases a change the note calls
    # faster left the bubble still. Every toggle now moves it; range 4-36 mm on the 0-40 mm scale.
    dict(id="B6-TR-DIST", slug="transpiration", layer="logic",
         old="dist(f) { return Math.max(4, 12 + (f.t ? 8 : 0) + (f.l ? 6 : -8) + (f.h ? -8 : 0) + (f.w ? 10 : 0)); }",
         new="dist(f) { return 16 + (f.t ? 6 : 0) + (f.l ? 6 : -6) + (f.h ? -6 : 0) + (f.w ? 8 : 0); }"),
    # translocation: a potato is a stem tuber, not a root, and a carrot stores mainly sugar.
    dict(id="B6-TL-SINK", slug="translocation", layer="logic",
         old="note: 'Down the phloem to the root, where the sugar is stored, for example as starch in a carrot or potato.'",
         new="note: 'Down the phloem to the root, where the sugar is stored, for example in a carrot.'"),
    # group-1 2.2: lilac is potassium's flame colour, not hydrogen's (pack examination/group-1.md §5).
    dict(id="B6-G1-LILAC-1", slug="group-1", layer="logic",
         old="note: 'Potassium reacts very vigorously. The hydrogen ignites at once with a lilac flame.'",
         new="note: 'Potassium reacts very vigorously. The hydrogen ignites at once, and potassium colours the flame lilac.'"),
    dict(id="B6-G1-LILAC-2", slug="group-1", layer="logic",
         old="potassium reacts very vigorously and the hydrogen ignites with a lilac flame.",
         new="potassium reacts very vigorously; the hydrogen ignites, and potassium colours the flame lilac."),
    # group-1: the prediction feedback starts a sentence in lower case ("You predicted gentler. it is
    # the other way."). Capitalise it; words unchanged. (From the batch-6 pupil walk.)
    dict(id="B6-G1-CAP", slug="group-1", layer="logic",
         old="'it is the other way. '", new="'It is the other way. '"),

    # ── Batch 6 port mechanics (not science rulings) ───────────────────────
    # culturing-microorganisms, factors-affecting-food-security, stellar-evolution: each renderVals
    # returns a fresh object rather than spreading the route helper (as batch 4's infrared and batch 5's
    # red-shift did), so the one route chip (B-R12) got no words and no menu. Same repair as B4-IRB-CHIP.
    dict(id="B6-CM-CHIP", slug="culturing-microorganisms", layer="logic",
         old="      route, onRoute: R.onRoute, isHigher: H,\n      tripleOptions:",
         new="      route, onRoute: R.onRoute, isHigher: H, routeWords: R.routeWords, routeSwitchOptions: R.routeSwitchOptions,\n      tripleOptions:"),
    dict(id="B6-FS-CHIP", slug="factors-affecting-food-security", layer="logic",
         old="      route, onRoute: R.onRoute,\n      tripleOptions:",
         new="      route, onRoute: R.onRoute, routeWords: R.routeWords, routeSwitchOptions: R.routeSwitchOptions,\n      tripleOptions:"),
    dict(id="B6-SE-CHIP", slug="stellar-evolution", layer="logic",
         old="      route, onRoute: R.onRoute,\n      tripleOptions:",
         new="      route, onRoute: R.onRoute, routeWords: R.routeWords, routeSwitchOptions: R.routeSwitchOptions,\n      tripleOptions:"),

    # ── Batch 6 pointers Design left as plain text ("Code to wire", NOTES 5.1 and 10.4) ──
    # Her words are unchanged; only the lesson's name becomes a link to the live page for the pupil's
    # route (KS4.hrefFor, the same resolver every connects link uses). Both targets exist on all four routes.
    dict(id="B6-PTR-MICRO-1", slug="animal-plant-cells", layer="template",
         old="are in the Microscopy lesson.",
         new='are in the <a href="{{ mrbLink_microscopy }}">Microscopy lesson</a>.'),
    dict(id="B6-PTR-MICRO-2", slug="animal-plant-cells", layer="logic",
         old="    return Object.assign({}, R, {",
         new="    return Object.assign({}, R, { mrbLink_microscopy: ((window.KS4 && window.KS4.hrefFor('microscopy', R)) || '#'),"),
    dict(id="B6-PTR-ENZ-1", slug="digestive-system", layer="template",
         old="is in the Enzymes lesson.",
         new='is in the <a href="{{ mrbLink_enzymes }}">Enzymes lesson</a>.'),
    dict(id="B6-PTR-ENZ-2", slug="digestive-system", layer="logic",
         old="    return Object.assign({}, R, {",
         new="    return Object.assign({}, R, { mrbLink_enzymes: ((window.KS4 && window.KS4.hrefFor('enzymes', R)) || '#'),"),

    # ═══ Batch 7 science rulings (Prompt AC, 12 Oct 2026; rulings by the lead) ═══
    # drug-discovery-development: thalidomide is not in the spec (the lesson's own NOTES 7.4 says
    # Code may drop the line and q3 together). The paragraph under the gate figure goes ...
    dict(id="B7-DD-THAL", slug="drug-discovery-development", layer="template",
         old=r'''        <p style="margin: 14px 0 0; font-size: 17px; line-height: 1.55; max-width: 62ch;">Thalidomide, a 1950s drug for morning sickness, had not been tested for its effects on unborn babies. It caused severe birth defects, and drug testing was made much stricter.</p>
''',
         new=""),
    # ... and q3 ("the key lesson from the thalidomide tragedy") is replaced by the KS4 bank item (the lead
    # changed e07 to e08: her ladder rung 2 already asks for the three things a drug is tested for)
    # ks4-drug-discovery-development-e08, in her object format, key first. The bank stays five.
    dict(id="B7-DD-Q3", slug="drug-discovery-development", layer="logic",
         old=r'''      { q: 'What was the key lesson from the thalidomide tragedy?', opts: [['Drugs must be rigorously tested for all potential effects including effects on embryos \u2014 testing requirements were significantly strengthened', true], ['Natural drugs are always safer than synthetic ones', false], ['Sedatives should never be prescribed during pregnancy', false], ['Clinical trials are unnecessary if a drug has been shown to be safe in adults', false]],
        wrong_explanations: { 1: 'Thalidomide was a synthetic drug \u2014 but many synthetic drugs are completely safe. The lesson was specifically about testing for effects on ALL groups, especially embryos.', 2: 'The lesson was specifically about testing for ALL effects in ALL populations \u2014 not a blanket ban on sedatives in pregnancy.', 3: 'The thalidomide case showed exactly WHY clinical trials must be thorough \u2014 an adult-safe drug was devastating to embryos.' } },
''',
         new=r'''      { q: 'State what is meant by the efficacy of a drug.', opts: [['How well it works', true], ['How harmful the drug is to the body of the patient who is taking it', false], ['How long the drug remains active inside the body after it has been swallowed', false], ['How much of the drug has to be given in order to produce any effect', false]],
        wrong_explanations: { 1: 'That is toxicity: how harmful the drug is.', 2: 'Drugs are tested for toxicity, efficacy and dose. Efficacy is how well the drug works.', 3: 'That is the dose: how much of the drug to give.' } },
'''),
    # ── Batch 7 science rulings, lessons 1-16 (the lead's examination) ──
    # the 'resistant bacteria multiply' step drew ten live non-resistant bacteria again, as if the killed ones grew back
    dict(id='B7-BD-RESFIG', slug='bacterial-diseases', layer='logic',
         old='const resistant = n < 3 ? R.indexOf(i) >= 0 : true;',
         new='const resistant = n < 2 ? R.indexOf(i) >= 0 : true;'),
    # rung 2's key needs it taught (spec 4.3.1.2 words)
    dict(id='B7-VD-FATAL', slug='viral-diseases', layer='logic',
         old="{ t: 'Most young children are vaccinated against it', d: 0 }",
         new="{ t: 'Can be fatal if complications arise, so most young children are vaccinated against it', d: 0 }"),
    dict(id='B7-VD-CHLORO', slug='viral-diseases', layer='logic',
         old='TMV gives a distinctive mosaic pattern of discolouration on the leaves. Less of the leaf',
         new='TMV gives a distinctive mosaic pattern of discolouration on the leaves: the pale patches have less chlorophyll. Less of the leaf'),
    # bank q1's key needs the reason taught
    dict(id='B7-AB-VIRUS', slug='antibiotics-painkillers', layer='logic',
         old='Nothing happens to the virus: antibiotics cannot kill viral pathogens.',
         new='Nothing happens to the virus: antibiotics cannot kill viral pathogens. A virus has none of the bacterial structures that antibiotics attack.'),
    dict(id='B7-VAC-HERD', slug='vaccination', layer='template',
         old='the spread of the pathogen is very much reduced. Set how many people are immune',
         new='the spread of the pathogen is very much reduced. This is called herd immunity. Set how many people are immune'),
    dict(id='B7-VAC-MEMORY', slug='vaccination', layer='template',
         old='If the same pathogen re-enters the body, the white blood cells respond quickly',
         new='Some of these white blood cells stay in the body as memory cells. If the same pathogen re-enters the body, the white blood cells respond quickly'),
    # labels must match what the 25-person grid draws
    dict(id='B7-VAC-GRID', slug='vaccination', layer='logic',
         old="{ k: '50% immune', n: 12 }, { k: '95% immune', n: 23 }",
         new="{ k: '48% immune', n: 12 }, { k: '96% immune', n: 24 }"),
    dict(id='B7-CD-MEMORY', slug='communicable-diseases-defence', layer='template',
         old='If the same pathogen comes back, white blood cells make the right antibodies quickly: in ',
         new='Some white blood cells stay in the blood as memory cells, so if the same pathogen comes back the right antibodies are made quickly: more in '),
    # aphids are Triple-only; this is shown on Combined
    dict(id='B7-FP-APHID', slug='fungal-protist-diseases', layer='logic',
         old="{ text: 'By insects such as aphids', correct: false,",
         new="{ text: 'By insects', correct: false,"),
    dict(id='B7-FP-WX3', slug='fungal-protist-diseases', layer='logic',
         old='Black spot spreads by water, so wetting the leaves won\\u2019t help.',
         new='Black spot spreads by water, so wetting the leaves could help it spread.'),
    # one glycerol + three fatty acids is 4 units, not a 6-bead chain
    dict(id='B7-MET-LIPID', slug='metabolism', layer='logic',
         old='chain(250, 120, 6, col)',
         new='chain(250, 120, i === 1 ? 4 : 6, col)'),
    # respiration breaks down glucose, which is one unit, not a 6-bead polymer
    dict(id='B7-MET-GLUCOSE', slug='metabolism', layer='logic',
         old='chain(30, 120, 6, col)',
         new='(i === 3 ? D.circ(85, 120, 22, col, C.stroke, 2) : chain(30, 120, 6, col))'),
    dict(id='B7-MET-UREA', slug='metabolism', layer='logic',
         old="small: 'urea', big: 'excess protein'",
         new="small: 'amino acids, then urea', big: 'excess protein'"),
    dict(id='B7-MET-PLANTS', slug='metabolism', layer='logic',
         old="'Building up: glucose and nitrate ions form amino acids",
         new="'Building up: in plants, glucose and nitrate ions form amino acids"),
    dict(id='B7-MET-WX2', slug='metabolism', layer='logic',
         old="2: 'CO\\u2082 is transported in the blood and exhaled \\u2014 it is not converted to urea.'",
         new="2: 'Urea contains nitrogen, which comes from amino acids. Carbon dioxide and water contain no nitrogen.'"),
    dict(id='B7-MET-KIDNEY', slug='metabolism', layer='logic',
         old="3: 'The kidneys filter urea.' }",
         new="3: 'Urea is carried to the kidneys for excretion.' }"),
    # distance is lamp-to-pondweed: the 0 cm tick sits at the pondweed
    dict(id='B7-RP-ZERO-1', slug='rate-of-photosynthesis', layer='logic',
         old='lx = tx - 60 - d * 8',
         new='lx = tx - d * 8'),
    dict(id='B7-RP-ZERO-2', slug='rate-of-photosynthesis', layer='logic',
         old='const x = tx - 60 - k * 8',
         new='const x = tx - k * 8'),
    # heat shield narrowed and moved between the pondweed and the nearest (10 cm) lamp position
    dict(id='B7-RP-ZERO-3', slug='rate-of-photosynthesis', layer='logic',
         old="b += BOX(tx - 115, 110, 60, 118, '#DDEEF6') + D.T(tx - 85, 100, 'heat shield', 11, { weight: 'normal', fill: C.stroke });",
         new="b += BOX(tx - 42, 110, 22, 118, '#DDEEF6') + D.T(tx - 20, 88, 'heat shield', 11, { anchor: 'end', weight: 'normal', fill: C.stroke });"),
    # the written equation is RELATIVE light intensity
    dict(id='B7-RP-REL-1', slug='rate-of-photosynthesis', layer='logic',
         old='light intensity (L) = 1 \\u00f7 d\\u00b2',
         new='relative light intensity (L) = 1 \\u00f7 d\\u00b2'),
    # lines 321, 327, 334, 336, 366 (lower case)
    dict(id='B7-RP-REL-2', slug='rate-of-photosynthesis', layer='logic',
         old='light intensity = 1 \\u00f7 d\\u00b2',
         new='relative light intensity = 1 \\u00f7 d\\u00b2', count=5),
    # line 390 (key note, capital L)
    dict(id='B7-RP-REL-3', slug='rate-of-photosynthesis', layer='logic',
         old='Light intensity = 1 \\u00f7 d\\u00b2, both',
         new='Relative light intensity = 1 \\u00f7 d\\u00b2, both'),
    # the limiting idea is Higher-only and the key fact shows on every route
    dict(id='B7-RP-KEYFACT', slug='rate-of-photosynthesis', layer='template',
         old='The factor in shortest supply limits the rate.',
         new='Temperature, light intensity, carbon dioxide concentration and the amount of chlorophyll all affect the rate.'),
    # H is declared at the top of renderVals (const H = c.isHigher)
    dict(id='B7-EX-R4-1', slug='response-to-exercise', layer='logic',
         old="prompt: 'Explain how the body responds to a period of vigorous exercise, and why breathing stays fast afterwards.'",
         new="prompt: H ? 'Explain how the body responds to a period of vigorous exercise, and why breathing stays fast afterwards.' : 'Explain how the body responds to a period of vigorous exercise.'"),
    dict(id='B7-EX-R4-2', slug='response-to-exercise', layer='logic',
         old="'The build-up of lactic acid creates an oxygen debt, so breathing stays fast after.'",
         new="'The build-up of lactic acid creates an oxygen debt.'"),
    # links 2 and 3 could be swapped; link 3 now follows from link 2
    dict(id='B7-EX-CHAIN', slug='response-to-exercise', layer='logic',
         old="'Blood carries the lactic acid to the liver, where it is converted back into glucose.'",
         new="'So breathing stays fast until the lactic acid has been removed.'"),
    dict(id='B7-PS-CHAIN', slug='photosynthesis', layer='logic',
         old="'Carbon dioxide diffuses into the leaf through the stomata, and reaches the chloroplasts.'",
         new="'The water reaches the chloroplasts, along with carbon dioxide that diffused in through the stomata.'"),
    dict(id='B7-AR-CHAIN', slug='aerobic-respiration', layer='logic',
         old="'Aerobic respiration happens in the mitochondria.'",
         new="'So they need a high rate of aerobic respiration, which happens in the mitochondria.'"),
    # muscle fibres are among the largest cells, so the old distractor may be true
    dict(id='B7-AR-Q5-1', slug='aerobic-respiration', layer='logic',
         old="['They are the largest cells in the body', false]",
         new="['They need very little energy', false]"),
    # FLAGS F1 bans ATP numbers
    dict(id='B7-AN-ATP', slug='anaerobic-respiration', layer='logic',
         old='Anaerobic respiration produces FAR LESS ATP (~2 vs ~36) \\u2014 it is not chosen for maximum performance.',
         new='Anaerobic respiration transfers much LESS energy than aerobic \\u2014 it is not chosen for maximum performance.'),
    dict(id='B7-UG-WP', slug='uses-of-glucose', layer='logic',
         old='it doesn\\u2019t affect osmosis or water potential inside cells',
         new='it doesn\\u2019t affect osmosis'),
    dict(id='B7-UG-POTATO', slug='uses-of-glucose', layer='template',
         old='A potato is mostly food the plant made',
         new='A potato is packed with food the plant made'),
    dict(id='B7-PD-MIMIC', slug='plant-disease-detection-defence', layer='logic',
         old="'Mechanical: tricks animals, for example by looking like something else.'",
         new="'Mechanical: tricks animals, for example leaf spots that look like butterfly eggs, so butterflies don\\u2019t lay eggs there.'"),
    dict(id='B7-PD-BARK', slug='plant-disease-detection-defence', layer='logic',
         old="'The dead cells fall off, taking pathogens on them away.'",
         new="'Also, the dead cells fall off, and any pathogens on them fall off too.'"),
    dict(id='B7-AR-Q5-2', slug='aerobic-respiration', layer='logic',
         old="1: 'Mitochondria number follows energy demand, not cell size.'",
         new="1: 'They need a lot of energy: the number of mitochondria follows energy demand.'"),
    # ── Batch 7: fixes from the pupil walk (the lead, after the independent walk of c850c51ba) ──
    # converting BOTH distances is also correct, so the old distractors marked a right method wrong; converting only one is genuinely wrong
    dict(id='B7W-RP-CONV', slug='rate-of-photosynthesis', layer='logic',
         old="convOptions: ['Nothing to convert: both in cm', 'Convert cm to m: divide by 100', 'Convert cm to mm: multiply by 10']",
         new="convOptions: ['Nothing to convert: both in cm', 'Convert only the 30 cm to m: divide by 100', 'Convert only the 10 cm to mm: multiply by 10']"),
    # a disease's table row fills when ANY clue for it is answered (the reply already reveals the disease), not only on a correct pick
    dict(id='B7W-VD-CLUES', slug='viral-diseases', layer='logic',
         old='got: i === CL.d && s.got.indexOf(i) < 0 ? s.got.concat([i]) : s.got',
         new='got: s.got.indexOf(CL.d) < 0 ? s.got.concat([CL.d]) : s.got'),
    # chain link forced by the one before
    dict(id='B7W-FP-CHAIN', slug='fungal-protist-diseases', layer='logic',
         old="'Nets stop mosquitoes biting people while they sleep.'",
         new="'Nets stop these mosquitoes biting people while they sleep.'"),
    # the old second link could still refer back to the question, so the order drug -> specific -> delivers also read sensibly and
    # was rejected. Each link now follows only from the one before: specific -> binds only to them; the drug bound to the antibody is
    # carried to those cells; so only those cells are reached.
    dict(id='B7W-MA-CHAIN', slug='monoclonal-antibodies', layer='logic',
         old="['The antibody is specific to an antigen on the cancer cells.', 'A toxic drug, radioactive substance or growth-stopping chemical is bound to it.', 'It delivers the substance to the cancer cells only, so other cells aren\\u2019t harmed.']",
         new="['The antibody is specific to an antigen on the cancer cells, so it binds only to them.', 'A toxic drug, radioactive substance or growth-stopping chemical bound to the antibody is carried to those cells.', 'So the substance reaches the cancer cells only, and other cells aren\\u2019t harmed.']"),
    # CH TH rung 2b has ONE wrong-answer string for any wrong convert/number/unit, so it says what the right method is.
    dict(id='B7W-RP-CONVFB', slug='rate-of-photosynthesis', layer='logic',
         old="wrong: 'Square each distance: 100 and 900. 900 \\u00f7 100 = 9.'",
         new="wrong: 'Both distances are already in cm, so there is nothing to convert. Square each distance: 100 and 900. 900 \\u00f7 100 = 9.'"),
    # target includes the next link's opening so it cannot match the wrong_explanations string of the same words
    dict(id='B7W-AB-CHAIN-1', slug='antibiotics-painkillers', layer='logic',
         old="'Antibiotics cannot kill viral pathogens.', 'Prescribing",
         new="'Antibiotics cannot kill viral pathogens, so they won\\u2019t work on it.', 'Prescribing"),
    dict(id='B7W-AB-CHAIN-2', slug='antibiotics-painkillers', layer='logic',
         old="'Completing the course kills all the bacteria, so none survive to form resistant strains.'",
         new="'So completing the course kills all the bacteria, and none survive to form resistant strains.'"),
    dict(id='B7W-PD-Q2KEY', slug='plant-disease-detection-defence', layer='logic',
         old='It provides a waterproof physical barrier that prevents pathogens from landing and colonising the leaf surface',
         new='It provides a waterproof physical barrier that stops pathogens getting into the leaf'),
    dict(id='B7W-VAC-WX3', slug='vaccination', layer='logic',
         old="'Natural immunity after infection DOES contribute to herd immunity \\u2014 but vaccination is the safer way to achieve it without suffering the disease.'",
         new="'That is one person\\u2019s immunity. Herd immunity is when enough of the population is immune that the pathogen cannot spread.'"),
    dict(id='B7W-PS-ROOTS', slug='photosynthesis', layer='logic',
         old="how: 'Water is absorbed by the roots and carried up the xylem to the leaves.'",
         new="how: 'Water is absorbed by the roots and carried up the xylem to the leaves. Root cells get no light and have no chloroplasts, so they do not photosynthesise.'"),
    # the one-line label ran past the SVG's right edge; two lines, right of the curve
    dict(id='B7W-RP-TEMP-LABEL', slug='rate-of-photosynthesis', layer='logic',
         old="D.T(345, 150, 'enzymes denatured', 12, { anchor: 'start', weight: 'normal', fill: C.stroke })",
         new="D.T(345, 142, 'enzymes', 12, { anchor: 'start', weight: 'normal', fill: C.stroke }) + D.T(345, 157, 'denatured', 12, { anchor: 'start', weight: 'normal', fill: C.stroke })"),
    # the label sat on the title 'oxygen for the muscles'; it now sits inside the dashed shortfall box
    dict(id='B7W-EX-SHORTFALL', slug='response-to-exercise', layer='logic',
         old="D.T(265, 250 - need - 8, 'shortfall', 12, { fill: C.red })",
         new="D.T(265, 250 - (need + got) / 2 + 4, 'shortfall', 12, { fill: C.red })"),
    # moved into the shaded area below both curves
    dict(id='B7W-EX-DEBT-LABEL', slug='response-to-exercise', layer='logic',
         old="D.T(X0 + 10.4 * dx, Y0 - 90, 'oxygen debt', 12, { fill: C.blue })",
         new="D.T(X0 + 9.2 * dx, Y0 - 80, 'oxygen debt', 12, { fill: C.blue })"),
    # 'immune cells attacked' overflowed its box: two lines; the other two boxes are unchanged
    dict(id='B7W-VD-HIV-LABEL', slug='viral-diseases', layer='logic',
         old='D.T(x + 62, 106, t, 13, { fill: i <= n ? C.stroke : C.muted })',
         new="(t.length > 18 ? [t.slice(0, t.lastIndexOf(' ')), t.slice(t.lastIndexOf(' ') + 1)] : [t]).map((ln, k, a) => D.T(x + 62, 106 + (k - (a.length - 1) / 2) * 16, ln, 13, { fill: i <= n ? C.stroke : C.muted })).join('')"),
    # 'Anaerobic: plants, yeast' was wider than its column header; only that header breaks onto two lines
    dict(id='B7W-AN-HEAD', slug='anaerobic-respiration', layer='logic',
         old='D.T(x + 78, 50, c.k, 13, { fill: C.stroke })',
         new="(c.k.length > 18 ? c.k.split(': ').map((ln, q) => D.T(x + 78, 41 + q * 17, ln, 13, { fill: C.stroke })).join('') : D.T(x + 78, 50, c.k, 13, { fill: C.stroke }))"),
    # the box label was wider than its box; the figure's own ': ' two-line split now breaks it (the colon is not drawn)
    dict(id='B7W-FP-CYCLE-LABEL', slug='fungal-protist-diseases', layer='logic',
         old="[330, 90, 'protist develops in mosquito']",
         new="[330, 90, 'protist develops: in mosquito']"),
    # the block already says 'Fair guess.'
    dict(id='B7W-FP-REPLY', slug='fungal-protist-diseases', layer='logic',
         old="reply: 'A fair guess, but the mosquito carries",
         new="reply: 'But the mosquito carries"),
    # the data note already says 'Yes.'
    dict(id='B7W-VAC-DATA', slug='vaccination', layer='logic',
         old="r: 'Yes: from about 800 a year",
         new="r: 'From about 800 a year"),
    # 'Pick a distance.' was shown three times before any press; it now shows once, in the live note beside the figure
    dict(id='B7W-RP-PICK-1', slug='rate-of-photosynthesis', layer='template',
         old=' Count the bubbles of oxygen given off in one minute. Pick a distance.</p>',
         new=' Count the bubbles of oxygen given off in one minute.</p>'),
    dict(id='B7W-RP-PICK-2', slug='rate-of-photosynthesis', layer='logic',
         old="readings: readings.length ? readings : ['Pick a distance.'],",
         new='readings: readings,'),
    # M3 (pupil walk): the six gates were one row in a 660-wide drawing, shown at about 5.7 px at 390 px. Two rows of
    # three in a 340-wide drawing doubles the text. Labels, order, dots and every state are unchanged; this also
    # carries the two-line wrap of B7W-DD-GATE-LABEL (that entry is folded in here).
    dict(id='B7W-DD-GATES', slug='drug-discovery-development', layer='logic',
         old="    GATES.forEach((g, i) => {\n      const x = 14 + i * 108;\n      b += BOX(x, 40, 98, 70, i === n ? '#F6D9D0' : i < n ? '#FFFDF8' : '#E9E2CF', C.stroke, i === n ? 3.5 : 2);\n      const w = g.k.split(', ');\n      w.forEach((t, k) => { b += D.T(x + 49, 72 + k * 18 - (w.length - 1) * 9, t, 12, { fill: i <= n ? C.stroke : C.muted }); });\n      for (let j = 0; j < 24; j++) { const cx = x + 14 + (j % 6) * 14, cy = 132 + Math.floor(j / 6) * 14; const on = j < left[i] && i <= n; b += D.circ(cx, cy, 4.5, on ? C.blue : 'none', on ? 'none' : C.muted, on ? 0 : 1); }\n    });\n    if (n === 4) {\n      b += BOX(150, 210, 360, 76, '#FFFDF8') + D.T(330, 234, 'who knows who got the drug?', 13, { fill: C.stroke });\n      b += D.T(250, 262, 'patients: no', 13, { weight: 'normal', fill: C.stroke }) + D.T(410, 262, 'doctors: no', 13, { weight: 'normal', fill: C.stroke });\n    } else b += D.T(330, 250, GATES[n].who, 14, { fill: C.stroke, style: 'italic' });\n    b += D.T(330, 22, 'blue dots: drug candidates still in the running', 12, { weight: 'normal', fill: C.stroke });\n    return D.svg(660, 300, b,",
         new="    GATES.forEach((g, i) => {\n      const x = 14 + (i % 3) * 108, oy = Math.floor(i / 3) * 150;\n      b += BOX(x, 40 + oy, 98, 70, i === n ? '#F6D9D0' : i < n ? '#FFFDF8' : '#E9E2CF', C.stroke, i === n ? 3.5 : 2);\n      const w = (g.k.indexOf(', ') < 0 && g.k.length > 14) ? [g.k.slice(0, g.k.lastIndexOf(' ')), g.k.slice(g.k.lastIndexOf(' ') + 1)] : g.k.split(', ');\n      w.forEach((t, k) => { b += D.T(x + 49, 72 + oy + k * 18 - (w.length - 1) * 9, t, 12, { fill: i <= n ? C.stroke : C.muted }); });\n      for (let j = 0; j < 24; j++) { const cx = x + 14 + (j % 6) * 14, cy = 132 + oy + Math.floor(j / 6) * 14; const on = j < left[i] && i <= n; b += D.circ(cx, cy, 4.5, on ? C.blue : 'none', on ? 'none' : C.muted, on ? 0 : 1); }\n    });\n    if (n === 4) {\n      b += BOX(14, 340, 310, 76, '#FFFDF8') + D.T(169, 364, 'who knows who got the drug?', 13, { fill: C.stroke });\n      b += D.T(99, 392, 'patients: no', 13, { weight: 'normal', fill: C.stroke }) + D.T(239, 392, 'doctors: no', 13, { weight: 'normal', fill: C.stroke });\n    } else b += D.T(169, 360, GATES[n].who, 14, { fill: C.stroke, style: 'italic' });\n    b += D.T(169, 22, 'blue dots: drug candidates still in the running', 12, { weight: 'normal', fill: C.stroke });\n    return D.svg(340, 430, b,"),
]

# ── Batch 7 port mechanics (not science rulings) ───────────────────────
# B7-<slug>-CHIP, one per batch-7 lesson: every batch-7 page builds its render values in a
# `common()` helper that returns a FRESH object ({ route, rk, onRoute: R.onRoute || ..., ...})
# rather than spreading the route helper, so B-R12's one route chip got no words and no menu
# (as batch 4's infrared, batch 5's red-shift and batch 6's three did). Same one-line repair as
# B4-IRB-CHIP: pass routeWords / routeSwitchOptions through. B-R12 still fails loud without it.
# monoclonal-antibodies is the one-route page: it has no chip to feed (B7-ONE-ROUTE below),
# but the pass-through is harmless and keeps the 16 pages identical in shape.
_B7_SLUGS = ["communicable-diseases-defence", "viral-diseases", "bacterial-diseases",
             "fungal-protist-diseases", "vaccination", "antibiotics-painkillers",
             "drug-discovery-development", "monoclonal-antibodies", "plant-disease-detection-defence",
             "photosynthesis", "rate-of-photosynthesis", "uses-of-glucose", "aerobic-respiration",
             "anaerobic-respiration", "response-to-exercise", "metabolism"]
SCIENCE.extend(
    dict(id="B7-%s-CHIP" % sl.upper(), slug=sl, layer="logic",
         old="return { route, rk, onRoute: R.onRoute || (() => {}),",
         new="return { route, rk, onRoute: R.onRoute || (() => {}), routeWords: R.routeWords, routeSwitchOptions: R.routeSwitchOptions,")
    for sl in _B7_SLUGS)

# B7-ONE-ROUTE: a lesson that ships on ONE route (monoclonal-antibodies, TH only) has no Route
# <select> and no "Foundation · Higher" chip to remove: Design drew a single "Triple Higher only"
# pill and no picker (her NOTES 8.1). B-R1 and B-R12 are not applicable to it; they are skipped
# only for a record whose `routes` has exactly one entry, and ONLY if the template really has no
# select and no tier chip (otherwise it fails loud, so a delivery that grows a picker is caught).
# rulings-batch8.py — paste the SCIENCE entries into ks4_batch_rulings.SCIENCE (before the `]` that closes it, i.e. before
# the line `]` that precedes `# ── Batch 7 port mechanics`), and the mechanics block after it. Generated against her bytes;
# every target below was found exactly the stated number of times, in the stated layer.

# ═══ Batch 8 science rulings ═══
B8_SCIENCE = [
    # renderVals read TH inside `done = [...]` before `const H/TH = c.is…` is declared (a ReferenceError once the guarded step completes). The same flag is now computed first, by the same route helper common() uses (K.route -> OK-checked route -> rk).
    dict(id='B8-THE-BRAIN-TDZ', slug='the-brain', layer='logic',
         old='const done = [s.hook !== null, s.regs.length === 3, s.syms.length === 4 && (!TH || s.maps.length === 3), s.think !== null, s.sort, s.ladder];',
         new="const rk0 = { 'Combined Foundation': 'CF', 'Combined Higher': 'CH', 'Triple Foundation': 'TF', 'Triple Higher': 'TH' }[((r) => (OK.indexOf(r) >= 0 ? r : OK[OK.length - 1]))((window.KS4 ? window.KS4.route(this) : { route: OK[OK.length - 1] }).route)];\n    const done = [s.hook !== null, s.regs.length === 3, s.syms.length === 4 && (rk0 !== 'TH' || s.maps.length === 3), s.think !== null, s.sort, s.ladder];"),
    # renderVals read TH inside `done = [...]` before `const H/TH = c.is…` is declared (a ReferenceError once the guarded step completes). The same flag is now computed first, by the same route helper common() uses (K.route -> OK-checked route -> rk).
    dict(id='B8-THERMOREGULATION-TDZ', slug='thermoregulation', layer='logic',
         old='const done = [s.hook !== null, s.cen.length === 4, s.temps.indexOf(0) >= 0 && s.temps.indexOf(2) >= 0 && (!TH || s.ctxs.length === 2), s.think !== null, s.sort, s.ladder];',
         new="const rk0 = { 'Combined Foundation': 'CF', 'Combined Higher': 'CH', 'Triple Foundation': 'TF', 'Triple Higher': 'TH' }[((r) => (OK.indexOf(r) >= 0 ? r : OK[OK.length - 1]))((window.KS4 ? window.KS4.route(this) : { route: OK[OK.length - 1] }).route)];\n    const done = [s.hook !== null, s.cen.length === 4, s.temps.indexOf(0) >= 0 && s.temps.indexOf(2) >= 0 && (rk0 !== 'TH' || s.ctxs.length === 2), s.think !== null, s.sort, s.ladder];"),
    # renderVals read H inside `done = [...]` before `const H/TH = c.is…` is declared (a ReferenceError once the guarded step completes). The same flag is now computed first, by the same route helper common() uses (K.route -> OK-checked route -> rk).
    dict(id='B8-ENDOCRINE-SYSTEM-TDZ', slug='endocrine-system', layer='logic',
         old='const done = [s.hook !== null, s.gls.length === 6 && (!H || (s.hi.length === 2 && s.fbs.length === 2)), s.sent.length === 2, s.think !== null, s.sort, s.ladder];',
         new="const rk0 = { 'Combined Foundation': 'CF', 'Combined Higher': 'CH', 'Triple Foundation': 'TF', 'Triple Higher': 'TH' }[((r) => (OK.indexOf(r) >= 0 ? r : OK[OK.length - 1]))((window.KS4 ? window.KS4.route(this) : { route: OK[OK.length - 1] }).route)];\n    const done = [s.hook !== null, s.gls.length === 6 && (!(rk0 === 'CH' || rk0 === 'TH') || (s.hi.length === 2 && s.fbs.length === 2)), s.sent.length === 2, s.think !== null, s.sort, s.ladder];"),
    # renderVals read H inside `done = [...]` before `const H/TH = c.is…` is declared (a ReferenceError once the guarded step completes). The same flag is now computed first, by the same route helper common() uses (K.route -> OK-checked route -> rk).
    dict(id='B8-BLOOD-GLUCOSE-DIABETES-TDZ', slug='blood-glucose-diabetes', layer='logic',
         old='const done = [s.hook !== null, s.modes.length === 3 && (!H || s.lowDone), s.curves.length === 3 && s.types.length === 2, s.think !== null, s.sort, s.ladder];',
         new="const rk0 = { 'Combined Foundation': 'CF', 'Combined Higher': 'CH', 'Triple Foundation': 'TF', 'Triple Higher': 'TH' }[((r) => (OK.indexOf(r) >= 0 ? r : OK[OK.length - 1]))((window.KS4 ? window.KS4.route(this) : { route: OK[OK.length - 1] }).route)];\n    const done = [s.hook !== null, s.modes.length === 3 && (!(rk0 === 'CH' || rk0 === 'TH') || s.lowDone), s.curves.length === 3 && s.types.length === 2, s.think !== null, s.sort, s.ladder];"),
    # renderVals read H inside `done = [...]` before `const H/TH = c.is…` is declared (a ReferenceError once the guarded step completes). The same flag is now computed first, by the same route helper common() uses (K.route -> OK-checked route -> rk).
    dict(id='B8-HUMAN-REPRODUCTION-HORMONES-TDZ', slug='human-reproduction-hormones', layer='logic',
         old='const done = [s.hook !== null, s.pub.length === 3, s.sts.length === 4 && (!H || s.hors.length === 4), s.think !== null, s.sort, s.ladder];',
         new="const rk0 = { 'Combined Foundation': 'CF', 'Combined Higher': 'CH', 'Triple Foundation': 'TF', 'Triple Higher': 'TH' }[((r) => (OK.indexOf(r) >= 0 ? r : OK[OK.length - 1]))((window.KS4 ? window.KS4.route(this) : { route: OK[OK.length - 1] }).route)];\n    const done = [s.hook !== null, s.pub.length === 3, s.sts.length === 4 && (!(rk0 === 'CH' || rk0 === 'TH') || s.hors.length === 4), s.think !== null, s.sort, s.ladder];"),
    # renderVals read H inside `done = [...]` before `const H/TH = c.is…` is declared (a ReferenceError once the guarded step completes). The same flag is now computed first, by the same route helper common() uses (K.route -> OK-checked route -> rk).
    dict(id='B8-CONTRACEPTION-FERTILITY-TDZ', slug='contraception-fertility', layer='logic',
         old='const done = [s.hook !== null, s.ms.length === 7, s.needs.length === 3 && (!H || (s.ivfDone && s.ev.length === 3)), s.think !== null, s.sort, s.ladder];',
         new="const rk0 = { 'Combined Foundation': 'CF', 'Combined Higher': 'CH', 'Triple Foundation': 'TF', 'Triple Higher': 'TH' }[((r) => (OK.indexOf(r) >= 0 ? r : OK[OK.length - 1]))((window.KS4 ? window.KS4.route(this) : { route: OK[OK.length - 1] }).route)];\n    const done = [s.hook !== null, s.ms.length === 7, s.needs.length === 3 && (!(rk0 === 'CH' || rk0 === 'TH') || (s.ivfDone && s.ev.length === 3)), s.think !== null, s.sort, s.ladder];"),
    # hyperopia + concave lens drew converging rays; VERIFY ALL 6 VIEWS in a screenshot
    dict(id='B8-DE-WRONGLENS', slug='defects-of-the-eye', layer='logic',
         old='const atG = lens === 0 ? null : cy + s * (lens === 1 ? 42 : 58);',
         new='const atG = lens === 0 ? null : cy + s * (lens === 1 ? (def === 0 ? 42 : 16) : 58);'),
    dict(id='B8-NS-RUNG2', slug='nervous-system', layer='logic',
         old='Made-up data: touch to response took 0.15 s with the hand near the face and 0.18 s with the hand at the foot. Suggest why.',
         new='Made-up data: a person responded to a touch on the cheek in 0.15 s and to a touch on the foot in 0.18 s. Suggest why.'),
    dict(id='B8-DE-LASER', slug='defects-of-the-eye', layer='logic',
         old="{ name: 'Laser surgery', why: 'Changes the shape of the cornea. Benefit:",
         new="{ name: 'Laser surgery', why: 'Changes the shape of the cornea: for myopia it is made flatter, so it refracts light less. Benefit:"),
    dict(id='B8-DE-SPECS', slug='defects-of-the-eye', layer='logic',
         old='Risk: can break or be lost; the eye itself is unchanged.',
         new='Risk: can break or be lost.'),
    dict(id='B8-RT-MM', slug='reaction-time', layer='template',
         old='m × 100, mm ÷ 10.',
         new='m × 100; mm ÷ 10, so 120 mm = 12 cm.'),
    dict(id='B8-TR-EVAP', slug='thermoregulation', layer='logic',
         old='and sweat glands produce sweat. Both transfer energy',
         new='and sweat glands produce sweat, which evaporates from the skin. Both transfer energy'),
    dict(id='B8-NS-NT', slug='nervous-system', layer='logic',
         old="'The chemical reaches the next neurone and starts a new electrical impulse.'",
         new="'The chemical, a neurotransmitter, binds to receptors on the next neurone and starts a new electrical impulse.'"),
    dict(id='B8-EYE-ACC', slug='the-eye', layer='template',
         old='You look up from the far side of a field to a book in your hands.',
         new='You stop looking at the far side of a field and look at a book in your hands.'),
    # route split: CF TF get the bank e06 item, CH TH get the bank s15 item (CH TH already carry nGr, an LH-peak item, so e06 would give two LH-release items). Replaces the verbatim q1, whose wx mentions the corpus luteum.
    dict(id='B8-HR-Q1', slug='human-reproduction-hormones', layer='logic',
         old="const q1 = Q('Which hormone triggers ovulation?', 'LH (Luteinising Hormone) — a surge at around Day 14 releases the egg from the follicle', [['FSH — it stimulates the follicle to release the egg', 'FSH stimulates EGG MATURATION — it prepares the follicle but doesn’t trigger the release. The LH SURGE causes ovulation.'], ['Oestrogen — high oestrogen directly causes egg release', 'High oestrogen causes the RELEASE OF LH from the pituitary — it’s the subsequent LH surge that triggers ovulation, not oestrogen directly.'], ['Progesterone — it relaxes the follicle wall to release the egg', 'Progesterone is produced AFTER ovulation by the corpus luteum — it maintains the uterus lining. It does not trigger ovulation.']]);",
         new="const q1 = H ? Q('Explain why oestrogen levels rise before the LH surge rather than after it.', 'The rising oestrogen is what stimulates the pituitary to release LH', [['Oestrogen has to be used up before LH can be made by the pituitary', 'Oestrogen stimulates LH release; it is not used up first.'], ['LH cannot be carried in blood that already contains oestrogen', 'Both hormones are carried in the blood at the same time.'], ['Oestrogen is released by the egg once it has left the ovary', 'Oestrogen is made by the ovary, and it rises before the egg is released.']]) : Q('What does the hormone LH cause to happen?', 'Ovulation', [['It causes the lining of the uterus to be shed at the start of a cycle', 'Not LH: LH causes ovulation, the release of an egg from the ovary.'], ['It causes the uterus lining to thicken in readiness for an embryo', 'That is oestrogen. LH causes ovulation.'], ['It causes the follicle in the ovary to begin maturing an egg cell', 'That is FSH. LH causes the mature egg to be released.']]);"),
    # bank s04 on every route; replaces the verbatim q2 (corpus luteum in its wx). B8-HR-IMPLANT teaches it first.
    dict(id='B8-HR-Q2', slug='human-reproduction-hormones', layer='logic',
         old="const q2 = Q('What happens to progesterone levels if fertilisation does NOT occur?', 'Progesterone falls — the uterus lining breaks down — menstruation begins and the cycle restarts', [['Progesterone rises — signalling the body to prepare for pregnancy anyway', 'Progesterone rising would signal PREGNANCY — which hasn’t occurred. Without an embryo producing hormones, the corpus luteum degenerates and progesterone falls.'], ['Progesterone stays the same indefinitely until the next menstrual cycle', 'Progesterone cannot stay elevated indefinitely — the corpus luteum degenerates after about 14 days without an embryo implanting.'], ['Progesterone triggers FSH release to immediately start a new cycle', 'FSH is released at the start of a new cycle as progesterone falls — but it is oestrogen and progesterone levels, not progesterone directly stimulating FSH.']]);",
         new="const q2 = Q('If an embryo implants, progesterone stays high instead of falling. Explain why this matters.', 'It keeps the lining in place to support the embryo', [['It stops the embryo from dividing too quickly at first', 'Progesterone acts on the uterus lining, not on how fast the embryo divides.'], ['It restarts the cycle so a second egg can be released', 'High progesterone keeps the lining in place; it does not start a new cycle.'], ['It causes the lining to be shed and then rebuilt more thickly', 'Shedding would remove the lining the embryo needs. Progesterone maintains it.']]);"),
    # the rung's command-word chip is the first MCQ argument, so it changes with the stem (Give -> State, as the neighbouring rung already does)
    dict(id='B8-HR-GRAMMAR', slug='human-reproduction-hormones', layer='logic',
         old="MCQ('Give', 'Give how often an egg is released, approximately.',",
         new="MCQ('State', 'State approximately how often an egg is released.',"),
    dict(id='B8-BG-HOOK-TITLE', slug='blood-glucose-diabetes', layer='template',
         old='title="Skipped lunch." scene="You skip lunch and feel a bit shaky by mid-afternoon. A snack later, you feel fine again."',
         new='title="A big bowl of pasta." scene="You eat a big bowl of pasta and your blood glucose rises. Two hours later it is back where it started, though you have eaten nothing else."'),
    # the rail label (RAIL const, L141)
    dict(id='B8-BG-HOOK-RAIL', slug='blood-glucose-diabetes', layer='logic',
         old='"label":"Skipped lunch"',
         new='"label":"A big bowl of pasta"'),
    # plasmid rings ARE GCSE; spec 4.6.1.4 two strands forming a double helix
    dict(id='B8-DNA-CIRCLE', slug='dna-genome', layer='logic',
         old="['Circle', 'Not at GCSE.']",
         new="['Circle', 'DNA’s two strands twist into a double helix.']"),
    # red blood cells have no nucleus
    dict(id='B8-DNA-EVERY-1', slug='dna-genome', layer='template',
         old='is the instruction for that kept in every cell of your body, or only in some cells?',
         new='is the instruction for that kept in nearly every cell of your body, or only in some cells?'),
    dict(id='B8-DNA-EVERY-2', slug='dna-genome', layer='logic',
         old="{ text: 'In every cell', correct: true,",
         new="{ text: 'In nearly every cell', correct: true,"),
    # non-coding DNA is Triple Higher only
    dict(id='B8-DNA-NONCODING', slug='dna-genome', layer='logic',
         old="'Not all DNA codes for proteins — a significant portion of the genome is non-coding DNA. Genes are specifically the protein-coding sequences.'",
         new="'Not all DNA is genes. A gene is a small section of DNA that codes for a particular protein.'"),
    dict(id='B8-CF-DIAPHRAGM', slug='contraception-fertility', layer='logic',
         old="'Preventing sperm entering = BARRIER METHODS (condoms, diaphragm). The pill has no physical barrier effect.'",
         new="'Preventing sperm entering = a CONDOM, a barrier method. The pill has no physical barrier effect.'"),
    # age-appropriate: what a method blocks, not how it is used
    dict(id='B8-CF-IUD', slug='contraception-fertility', layer='logic',
         old="['It covers the penis', 'That is a male condom.']",
         new="['It stops eggs maturing', 'That is a hormonal method.']"),
    # ST[3] (L148); the target includes the following words because the sentence also occurs twice in rung chains; so the q2 replacement is taught first
    dict(id='B8-HR-IMPLANT', slug='human-reproduction-hormones', layer='logic',
         old="note: 'Oestrogen and progesterone maintain the uterus lining. If the egg",
         new="note: 'Oestrogen and progesterone maintain the uterus lining. If an embryo implants, progesterone keeps the lining in place. If the egg"),
    # q1 (TF TH) tests advantages taught two lessons later; the bank is the CF CH set on every route
    dict(id='B8-SAR-BANK', slug='sexual-asexual-reproduction', layer='logic',
         old='const BANK = TR ? [q1, q3, nPl, nMit, nVar] : [q3, nPl, nMit, nVar, nClo];',
         new='const BANK = [q3, nPl, nMit, nVar, nClo];'),
    dict(id='B8-ADV-WHEAT', slug='advantages-sexual-asexual', layer='logic',
         old="['Wheat', 'Not a named example.']",
         new="['Wheat', 'Wheat grows from seeds, not bulbs.']"),
]
SCIENCE.extend(B8_SCIENCE)

# ── Batch 8 port mechanics (not science rulings) ───────────────────────
# B8-<SLUG>-CHIP, one per batch-8 lesson: as in batch 7, every page builds its render values in a `common()` helper that
# returns a FRESH object, so B-R12's one route chip got no words and no menu. Same one-line repair as B7-<SLUG>-CHIP.
_B8_SLUGS = ["homeostasis", "nervous-system", "reflex-actions", "reaction-time", "the-brain", "the-eye",
             "defects-of-the-eye", "thermoregulation", "endocrine-system", "blood-glucose-diabetes",
             "human-reproduction-hormones", "contraception-fertility", "sexual-asexual-reproduction", "meiosis",
             "advantages-sexual-asexual", "dna-genome"]
SCIENCE.extend(
    dict(id="B8-%s-CHIP" % sl.upper(), slug=sl, layer="logic",
         old="return { route, rk, onRoute: R.onRoute || (() => {}),",
         new="return { route, rk, onRoute: R.onRoute || (() => {}), routeWords: R.routeWords, routeSwitchOptions: R.routeSwitchOptions,")
    for sl in _B8_SLUGS)

# B8-INLINE-TRIPLE-PTR (two entries): a pointer Design wrote as plain words + a link to a TRIPLE-ONLY lesson, shown on every
# route. On Combined the link would resolve to nothing (B-INLINE-LINKS falls back to '#'), a dead link. Her own text labels it
# "(Triple)", so the pointer is shown on the Triple routes only (her words unchanged). These run AFTER B-INLINE-LINKS, so the
# targets carry the rewritten `{{ mrbLink_… }}` hrefs.
SCIENCE.extend([
    dict(id="B8-PTR-HOMEOSTASIS-THERMO", slug="homeostasis", layer="template",
         old='''<p style="margin: 14px 0 0; font-size: 17px; line-height: 1.55; max-width: 62ch;">How sweating and shivering work: <a href="{{ mrbLink_thermoregulation }}">Thermoregulation</a> (Triple).</p>''',
         new='''<sc-if value="{{ isTriple }}"><p style="margin: 14px 0 0; font-size: 17px; line-height: 1.55; max-width: 62ch;">How sweating and shivering work: <a href="{{ mrbLink_thermoregulation }}">Thermoregulation</a> (Triple).</p></sc-if>'''),
    dict(id="B8-PTR-REFLEX-EYE", slug="reflex-actions", layer="template",
         old='''How the pupil reflex works: <a href="{{ mrbLink_the_eye }}">The eye</a> (Triple). ''',
         new='''<sc-if value="{{ isTriple }}">How the pupil reflex works: <a href="{{ mrbLink_the_eye }}">The eye</a> (Triple). </sc-if>'''),
])

# B8-LNK (engine, not per lesson): batch 8 writes its prev/next/connects as `LNK('<slug>', '<label>')` over a
# `const FILE = {slug: '<file>.dc.html'}` map, not as `{ href: '<file>.dc.html' }` objects, so B-PREVNEXT and B-CONNECTS match
# nothing and the G3 guard would raise on the FILE map. This one function (called from port_lesson):
#   * empties the FILE map (no `.dc.html` text survives);
#   * makes LNK resolve through KS4.hrefFor(slug, c) -- the same resolver every connects link uses, so a Triple-only target
#     is simply null on a Combined route and Ks4End's filter drops it;
#   * sets the resolver's route (`LNK_R = c;`) right after `const c = this.common(done);`;
#   * swaps the single-line `endPrev:` / `endNext:` for the per-route mount props, like B-PREVNEXT.
# Fail-loud on every anchor. Lessons without the LNK helper (batches 4-7) are untouched.
_LNK_DEF = "const LNK = (k, label) => ({ href: FILE[k], label });"
_FILE_RE = re.compile(r"^const FILE = \{[^\n]*\};$", re.M)
_LNK_PREV_RE = re.compile(r"^(\s*)endPrev:[^\n]*\n", re.M)
_LNK_NEXT_RE = re.compile(r"^(\s*)endNext:[^\n]*\n", re.M)
_COMMON_DONE = "const c = this.common(done);"


def apply_lnk_links(source_file, logic):
    if _LNK_DEF not in logic:
        return logic, 0, 0
    if len(_FILE_RE.findall(logic)) != 1 or logic.count(_LNK_DEF) != 1 or logic.count(_COMMON_DONE) != 1:
        raise RulingError("ks4_batch_rulings B8-LNK: %s does not carry exactly one FILE map, one LNK helper and one "
                          "`%s`." % (source_file, _COMMON_DONE))
    logic = _FILE_RE.sub("const FILE = {}; // \u2295 B8-LNK: links resolve through KS4.hrefFor", logic, count=1)
    logic = logic.replace(_LNK_DEF, "let LNK_R = null; // \u2295 B8-LNK\n"
                          "const LNK = (k, label) => ({ href: ((window.KS4 && LNK_R) ? window.KS4.hrefFor(k, LNK_R) : null), label });", 1)
    logic = logic.replace(_COMMON_DONE, _COMMON_DONE + " LNK_R = c;", 1)
    n = []
    for rx, key, prop in ((_LNK_PREV_RE, "endPrev", "prev"), (_LNK_NEXT_RE, "endNext", "next")):
        if ("%s: this.props.mrbPrevNext.%s," % (key, prop)) in logic:
            n.append(0)     # already swapped by B-PREVNEXT (e.g. `endNext: null,`)
            continue
        if len(rx.findall(logic)) != 1:
            raise RulingError("ks4_batch_rulings B8-LNK: %s needs exactly one `%s:` line." % (source_file, key))
        logic = rx.sub(lambda m: "%s%s: this.props.mrbPrevNext.%s,\n" % (m.group(1), key, prop), logic, count=1)
        n.append(1)
    return logic, n[0], n[1]

# ═══ Batch 8: fixes from the pupil walk (the lead, after the walk of b03b0002e) ═══
SCIENCE.extend([
    dict(id='B8W-BR-CHAIN-A', slug='the-brain', layer='logic',
         old="'Muscle coordination is the job of the cerebellum.'",
         new="'That coordination is the job of the cerebellum.'"),
    dict(id='B8W-BR-CHAIN-TF', slug='the-brain', layer='logic',
         old="'Unconscious activities are controlled by the medulla.'",
         new="'Unconscious activities like this are controlled by the medulla.'"),
    dict(id='B8W-BR-CHAIN-TH', slug='the-brain', layer='logic',
         old="['Patients with damage to one region lose a particular function.', 'Electrically stimulating a small area produces a particular response.', 'MRI scans show which regions are active during a task.']",
         new="['Patients with damage to one region lose a particular function.', 'Electrically stimulating that region produces a response linked to the same function.', 'MRI scans then confirm that the region is active when the function is used.']"),
    dict(id='B8W-TR-CHAIN-RISE', slug='thermoregulation', layer='logic',
         old="'Sweat glands produce sweat.'",
         new="'Sweat glands also produce sweat.'"),
    dict(id='B8W-TR-CHAIN-FALL', slug='thermoregulation', layer='logic',
         old="['Receptors in the thermoregulatory centre detect the fall in blood temperature.', 'Blood vessels supplying the skin constrict.', 'Sweating stops.', 'Skeletal muscles contract: shivering.']",
         new="['Receptors in the thermoregulatory centre detect the fall in blood temperature.', 'Blood vessels supplying the skin constrict and sweating stops, so less energy is transferred from the skin.', 'Skeletal muscles also contract: shivering.']"),
    # the target runs on into the distractors so it cannot match the rung-3 CH TH chain or the rung-2 bank (the four-link sentence list also appears in a second chain)
    dict(id='B8W-HR-CHAIN-JOBS', slug='human-reproduction-hormones', layer='logic',
         old="['FSH from the pituitary causes an egg to mature.', 'Oestrogen from the ovary rebuilds the uterus lining.', 'LH from the pituitary stimulates the release of the egg.', 'Oestrogen and progesterone maintain the uterus lining.'],\n            [['The ovaries make FSH and LH.'",
         new="['FSH from the pituitary causes an egg to mature.', 'Meanwhile, oestrogen from the ovary rebuilds the uterus lining.', 'Once the lining has been rebuilt, LH from the pituitary stimulates the release of that egg.', 'After ovulation, oestrogen and progesterone maintain the lining.'],\n            [['The ovaries make FSH and LH.'"),
    dict(id='B8W-CF-CHAIN-CONDOM', slug='contraception-fertility', layer='logic',
         old="['Condoms are a barrier method.', 'They prevent sperm reaching an egg.', 'They also protect against sexually transmitted infections.', 'And they contain no hormones.']",
         new="['Condoms are a barrier method.', 'They prevent sperm reaching an egg.', 'They also protect against sexually transmitted infections, and they contain no hormones.']"),
    dict(id='B8W-SAR-CHAIN-CUTTING', slug='sexual-asexual-reproduction', layer='logic',
         old="['Only one parent is involved.', 'There is no fusion of gametes, so no mixing of genetic information.', 'The new cells are made by mitosis.', 'So the new plant is a clone.']",
         new="['A cutting is part of one parent plant.', 'Its cells divide by mitosis, copying that parent’s genetic information exactly.', 'With no fusion of gametes, nothing is added to that genetic information, so the new plant is a clone.']"),
    # the old distractor contradicted the page's own sentence 'Oestrogen and progesterone maintain the uterus lining'
    dict(id='B8W-HR-Q3', slug='human-reproduction-hormones', layer='logic',
         old="['Maintains the uterus lining in the second half of the cycle', 'Maintaining the uterus lining in the second half = PROGESTERONE. Oestrogen rebuilds it in the first half.']",
         new="['Stimulates sperm production', 'That is testosterone.']"),
    # spec 4.5.3.2 words
    dict(id='B8W-BG-TYPES-KEY', slug='blood-glucose-diabetes', layer='logic',
         old="'Type 1: pancreas produces no insulin (autoimmune). Type 2: cells become resistant to insulin (lifestyle-related).'",
         new="'Type 1: the pancreas fails to produce sufficient insulin. Type 2: the body cells no longer respond to the insulin produced by the pancreas.'"),
    # removes only the off-spec 'tablets' claim
    dict(id='B8W-BG-TYPES-REPLY', slug='blood-glucose-diabetes', layer='logic',
         old='TYPE 2 is usually managed first with diet, exercise and tablets.',
         new='TYPE 2 is usually managed first with diet and exercise.'),
    # the Type 1 loop's last step (every route, section 1, completed to tick INSULIN) is where the page teaches 'treatment: insulin injections'
    dict(id='B8W-BG-INJECT', slug='blood-glucose-diabetes', layer='logic',
         old="'Blood glucose stays high. Treatment: insulin injections.'",
         new="'Blood glucose stays high. Treatment: insulin injections. Insulin is a protein, so it would be digested if swallowed; it is injected instead.'"),
    # the label ran off the left edge; the leader now ends further right so the text sits inside the figure
    dict(id='B8W-BR-CORTEX-LABEL', slug='the-brain', layer='logic',
         old="lab(200, 60, 120, 22, 'cerebral cortex', 0, 'end')",
         new="lab(200, 60, 170, 22, 'cerebral cortex', 0, 'end')"),
    # the figure's own '; ' two-line split now breaks it (the semicolon is not drawn)
    dict(id='B8W-CF-IVF-LABEL', slug='contraception-fertility', layer='logic',
         old="'1 or 2 embryos into the uterus'",
         new="'1 or 2 embryos; into the uterus'"),
    # hyperopia + concave focuses beyond the right edge; the label is held inside it (no other state has fx > 570 - verified by screenshot of all six)
    dict(id='B8W-DE-FOCUS-LABEL', slug='defects-of-the-eye', layer='logic',
         old='b += D.T(fx, 300, where, 14, { fill: C.red })',
         new='b += D.T(Math.min(fx, 570), 300, where, 14, { fill: C.red })'),
    # the red X covered the end of 'Coordination centre'; it now sits in the box's top-right corner, above the text
    dict(id='B8W-HO-X', slug='homeostasis', layer='logic',
         old='<line x1="\' + (x + 150) + \'" y1="36" x2="\' + (x + 176) + \'" y2="62"/><line x1="\' + (x + 176) + \'" y1="36" x2="\' + (x + 150) + \'" y2="62"/></g>\'',
         new='<line x1="\' + (x + 164) + \'" y1="31" x2="\' + (x + 176) + \'" y2="43"/><line x1="\' + (x + 176) + \'" y1="31" x2="\' + (x + 164) + \'" y2="43"/></g>\''),
    # the LH label ran into the 'ovulation' label
    dict(id='B8W-HR-LH-LABEL', slug='human-reproduction-hormones', layer='logic',
         old="[X(13.6), 44, 'LH']",
         new="[(+X(13.6) - 8).toFixed(1), 44, 'LH']"),
])

# ═══ Batch 6 fix: Design's updated transpiration (13 Oct 2026); the lead's rulings ═══
SCIENCE.extend([
    # the rail listed Think again before Rate of uptake and Step 1/Step 2, but the page (and done[]) are in the order calc, steps, think; the rail ticked the wrong sections
    dict(id='B6F-TR-RAIL', slug='transpiration', layer='logic',
         old="  { id: 's-think', label: 'Think again', short: 'THINK' },\n  { id: 's-calc', label: 'Rate of uptake', short: 'CFIFA' },\n  { id: 's-steps', label: 'Step 1, Step 2', short: 'STEPS' },\n",
         new="  { id: 's-calc', label: 'Rate of uptake', short: 'CFIFA' },\n  { id: 's-steps', label: 'Step 1, Step 2', short: 'STEPS' },\n  { id: 's-think', label: 'Think again', short: 'THINK' },\n"),
    # matches the 3 s.f. of 31.4 mm³ and the attempt's 15.7
    dict(id='B6F-TR-ROUND', slug='transpiration', layer='logic',
         old="{ letter: 'A', label: 'Answer', line: 'rate \\u2248 6.3 mm\\u00b3/min' }",
         new="{ letter: 'A', label: 'Answer', line: 'rate \\u2248 6.28 mm\\u00b3/min' }"),
    # the halving shares the Convert line
    dict(id='B6F-TR-HALVE', slug='transpiration', layer='logic',
         old="note: 'Halve the diameter to get the radius, as its own line.'",
         new="note: 'Halve the diameter to get the radius before using the formula.'"),
    # the triangle block already prints that instruction
    dict(id='B6F-TR-TAP', slug='transpiration', layer='template',
         old='so 90 s = 1.5 min. Tap the quantity you want to find.</p>',
         new='so 90 s = 1.5 min.</p>'),
])

APPLIED = []


def apply_science(slug, layer, text):
    for r in SCIENCE:
        if r["slug"] != slug or r["layer"] != layer:
            continue
        n = text.count(r["old"])
        want = r.get("count", 1)  # ⊕ batch 7: a ruling may name an expected count above 1; any other count fails
        if n != want:
            raise RulingError("ks4_batch_rulings %s: expected exactly %d occurrence(s) in %s (%s), found %d.\n  looking for: %r"
                              % (r["id"], want, slug, layer, n, r["old"][:160]))
        text = text.replace(r["old"], r["new"])
        APPLIED.append(r["id"])
    return text


def port_lesson(lesson, tpl, logic, slug_by_file, other_slug_by_file=None):
    """-> (tpl, logic, report-dict)."""
    src = lesson["source_file"]
    if len(lesson["routes"]) == 1:
        # ⊕ B7-ONE-ROUTE (see above): nothing to remove, and it must really be absent.
        if "<select" in tpl or ks4_rulings.R12_TIER_LINE in tpl:
            raise RulingError("ks4_batch_rulings B7-ONE-ROUTE: %s ships on one route but its template "
                              "still carries a Route picker or tier chip." % src)
        if "Triple Higher only" not in tpl:
            raise RulingError("ks4_batch_rulings B7-ONE-ROUTE: %s has no 'Triple Higher only' pill." % src)
    else:
        tpl = ks4_rulings.apply_r1_route_selector(src, tpl)
        tpl = _chip(lesson["slug"], tpl)
    logic, n_prev, n_next = ks4_rulings.apply_r_prevnext(src, logic)
    logic, n_prev2, n_next2 = apply_lnk_links(src, logic)   # ⊕ batch 8: LNK()/FILE links
    n_prev, n_next = n_prev + n_prev2, n_next + n_next2
    logic, connects = apply_connects(src, logic, slug_by_file, other_slug_by_file)
    tpl, logic, inline = apply_inline_links(src, tpl, logic, slug_by_file, other_slug_by_file)
    tpl = apply_science(lesson["slug"], "template", tpl)
    logic = apply_science(lesson["slug"], "logic", logic)
    # ⊕ G3 (batch 6): no Design file name may survive on a built page. Every `.dc.html` link was
    # either a connects href or an in-text link above, so a leftover is a pattern this module missed.
    for layer, text in (("template", tpl), ("logic", logic)):
        m = re.search(r"[\w.\-]+\.dc\.html|Batch \d+/lessons/", text)
        if m:
            raise RulingError("ks4_batch_rulings G3: %s still carries %r in its %s after the link rulings."
                              % (src, m.group(0), layer))
    # B-R12's chip reads routeWords / routeSwitchOptions off the render values.
    if "Object.assign({}, R," not in logic and "routeWords" not in logic:
        raise RulingError("ks4_batch_rulings B-R12: %s's renderVals neither spreads the route helper nor "
                          "passes routeWords; the route chip would render empty." % lesson["slug"])
    return tpl, logic, dict(has_prev=bool(n_prev), has_next=bool(n_next), connects=connects, inline_links=inline)


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


# ⊕ B7-END-EMPTY-CONNECTS (batch 7 only; applied to batch 7's OWN copy of Ks4End by compile_block).
# Design's connects for bacterial-diseases (Culturing microorganisms, Triple) and drug-discovery-development
# (Plant defences, Triple) are Triple-only, so on the two Combined routes R-CONNECTS' filter leaves an EMPTY
# list under a still-visible "Connects to" heading. The section is wrapped in sc-if and hidden when the
# filtered list is empty. Words, links and every non-empty page are unchanged. Fails loud if a target moved.
END_SEC_FROM = "    <section>\n      <h2>Connects to</h2>"
END_SEC_TO = "    <sc-if value=\"{{ hasConnects }}\"><section>\n      <h2>Connects to</h2>"
END_SEC_CLOSE_FROM = "      </ul>\n    </section>\n    <section class=\"ks3-tutor\">"
END_SEC_CLOSE_TO = "      </ul>\n    </section></sc-if>\n    <section class=\"ks3-tutor\">"
END_LOGIC_FROM = "connects: (p.connects || []).filter(function (c) { return !!c.href; }), tutorLine:"
END_LOGIC_TO = ("connects: (p.connects || []).filter(function (c) { return !!c.href; }), "
                "hasConnects: (p.connects || []).filter(function (c) { return !!c.href; }).length > 0, tutorLine:")


def apply_end_hide_empty_connects(tpl, logic):
    for text, frm in ((tpl, END_SEC_FROM), (tpl, END_SEC_CLOSE_FROM), (logic, END_LOGIC_FROM)):
        _require(text, frm, "Ks4End.dc.html", "B7-END-EMPTY-CONNECTS")
    tpl = tpl.replace(END_SEC_FROM, END_SEC_TO, 1).replace(END_SEC_CLOSE_FROM, END_SEC_CLOSE_TO, 1)
    return tpl, logic.replace(END_LOGIC_FROM, END_LOGIC_TO, 1)
