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


B11_HIGHER_ONLY_PILL = (ks4_rulings._INDENT10 + '<span style="font-family: var(--ks3-font-mono); font-size: 13px; font-weight: 500; '
                        'letter-spacing: .06em; text-transform: uppercase; padding: 4px 11px; border-radius: 99px; '
                        'background: var(--ks3-ink); color: var(--ks3-ground);">Higher only</span>\n')


def _chip(slug, tpl):
    # ⊕ B10-ALL-FOUR-PILL: batch 10 draws ONE header pill, "All four routes", on its four-route pages (no tier pill
    # beside it). That single pill is what the route chip replaces. Taken only when the tier pill is absent and the
    # pill is there exactly once, so batches 4-8 (which all carry the tier pill) cannot reach it.
    allfour = ks4_rulings.R12_PATHWAY_STD_SPAN.replace("Combined · Triple", "All four routes")
    if tpl.count(ks4_rulings.R12_TIER_LINE) == 0 and tpl.count(allfour) == 1:
        return tpl.replace(allfour, ks4_rulings.R12_CHIP_BLOCK, 1)
    # ⊕ B11-HIGHER-PILL: batch 11's three Higher-only Chemistry pages (moles, amounts-in-equations, strong-weak-acids: CH TH)
    # draw a filled "Higher only" pill and the "Combined · Triple" pill, and NO "Foundation · Higher" tier pill. "Higher only"
    # is the tier pill in other words (the eyebrow beside the title already reads "· Higher only"), and the route chip's own
    # words name the tier, so the pill goes and the pathway pill becomes the chip. Taken only when the tier pill is absent
    # and both pills are there exactly once: batches 4-8 all carry the tier pill, so none of them can reach it.
    if (tpl.count(ks4_rulings.R12_TIER_LINE) == 0 and tpl.count(B11_HIGHER_ONLY_PILL) == 1
            and tpl.count(ks4_rulings.R12_PATHWAY_STD_SPAN) == 1):
        tpl = tpl.replace(B11_HIGHER_ONLY_PILL, "", 1)
        return tpl.replace(ks4_rulings.R12_PATHWAY_STD_SPAN, ks4_rulings.R12_CHIP_BLOCK, 1)
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

# ⊕ B11W-PM (batch 11 only, applied to batch 11's OWN copy of Ks4Practice by compile_block): the calc rung reads the
# answer with parseFloat, which is NaN on a leading ± so "±0.10" was marked wrong. A leading ± or + is stripped first.
# Scoped by design_dir exactly as END-EMPTY-CONNECTS is, so batches 4-10 stay byte-identical.
PRACTICE_PM_FROM = ")(st.num); // \u2295 B-PRACTICE-PARSE (R16 for Ks4Practice)"
PRACTICE_PM_TO = ")(String(st.num).replace(/^\\s*[\\u00b1+]\\s*/, '')); // \u2295 B-PRACTICE-PARSE (R16 for Ks4Practice) + B11W-PM"


def apply_practice_pm(text):
    _require(text, PRACTICE_PM_FROM, "Ks4Practice.dc.html", "B11W-PM")
    return text.replace(PRACTICE_PM_FROM, PRACTICE_PM_TO, 1)



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
_COMMON_DONE_FFR = "const c = this.common(done, F, ready);"   # ⊕ batch 10: common(done, F, ready)
_COMMON_DONE_RAIL = "const c = this.common(done, F, ready, rail);"        # ⊕ batch 11
_COMMON_DONE_RAIL_CM = "const cm = this.common(done, F, ready, rail);"   # ⊕ batch 11 (electrolysis-molten)


def apply_lnk_links(source_file, logic):
    if _LNK_DEF not in logic:
        return logic, 0, 0
    # ⊕ Batch 10: its pages call `this.common(done, F, ready)`. Batch 8's spelling is tried first and unchanged.
    common = _COMMON_DONE if (logic.count(_COMMON_DONE) == 1 and logic.count(_COMMON_DONE_FFR) == 0) else _COMMON_DONE_FFR
    cvar = "c"
    # ⊕ Batch 11: two more spellings, tried ONLY when neither of the batch 8 / batch 10 spellings is present, so no earlier
    # page can reach them. Her mass-changes, oxidation-reduction, ph-scale and electrolysis-principles pages pass the rail as
    # a fourth argument (`common(done, F, ready, rail)`); electrolysis-molten also names the result `cm`, because `c` is its
    # compound picker. The resolver's route is set from whichever name the page really uses.
    if logic.count(_COMMON_DONE) == 0 and logic.count(_COMMON_DONE_FFR) == 0:
        for cand, var in ((_COMMON_DONE_RAIL, "c"), (_COMMON_DONE_RAIL_CM, "cm")):
            if logic.count(cand) == 1:
                common, cvar = cand, var
                break
    if len(_FILE_RE.findall(logic)) != 1 or logic.count(_LNK_DEF) != 1 or logic.count(common) != 1:
        raise RulingError("ks4_batch_rulings B8-LNK: %s does not carry exactly one FILE map, one LNK helper and one "
                          "`%s`." % (source_file, common))
    logic = _FILE_RE.sub("const FILE = {}; // \u2295 B8-LNK: links resolve through KS4.hrefFor", logic, count=1)
    logic = logic.replace(_LNK_DEF, "let LNK_R = null; // \u2295 B8-LNK\n"
                          "const LNK = (k, label) => ({ href: ((window.KS4 && LNK_R) ? window.KS4.hrefFor(k, LNK_R) : null), label });", 1)
    logic = logic.replace(common, common + " LNK_R = %s;" % cvar, 1)
    n = []
    for rx, key, prop in ((_LNK_PREV_RE, "endPrev", "prev"), (_LNK_NEXT_RE, "endNext", "next")):
        if ("%s: this.props.mrbPrevNext.%s," % (key, prop)) in logic:
            n.append(0)     # already swapped by B-PREVNEXT (e.g. `endNext: null,`)
            continue
        if len(rx.findall(logic)) != 1:
            raise RulingError("ks4_batch_rulings B8-LNK: %s needs exactly one `%s:` line." % (source_file, key))
        # ⊕ Batch 10: her endNext line also CLOSES the object (`... : null };`); keep that closer. Batch 8's lines do not.
        logic = rx.sub(lambda m: "%s%s: this.props.mrbPrevNext.%s,%s\n" % (m.group(1), key, prop, " };" if m.group(0).rstrip().endswith("};") else ""), logic, count=1)
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

# ═══ Transpiration: fixes from the pupil walk ═══
SCIENCE.extend([
    # the label ran past the right edge of the stoma figure in the open state; it is now right-aligned inside the 440-wide drawing (the closed state has no such label)
    dict(id='B6F-TR-VAPOUR', slug='transpiration', layer='logic',
         old="D.T(340, 70, 'water vapour out', 13, { anchor: 'start', fill: '#3B82F6' })",
         new="D.T(432, 70, 'water vapour out', 13, { anchor: 'end', fill: '#3B82F6' })"),
    # the keyed order starts at the leaf; the old stem invited starting at the roots
    dict(id='B6F-TR-CHAINQ', slug='transpiration', layer='logic',
         old="prompt: 'Explain how water moves from the roots to the air around a leaf. Put the links in order.'",
         new="prompt: 'Explain how water evaporating from a leaf draws water up from the roots. Put the links in order.'"),
])

# B10-FILE-REFS (engine): batch 10 binds in-text link hrefs (`pcHref: FILE['population-competition']`) straight off the
# FILE map, which B8-LNK has emptied. Each `FILE['key']` / `FILE.key` is rewritten to the same resolver LNK uses, routed
# per pupil (null on a route the target lacks -> '#', like B-INLINE-LINKS), and a FILE key whose name differs from the
# live slug is mapped here. Runs only if such a reference exists (batches 4-8 have none after B8-LNK), fail-loud on an
# unmapped key via KS4.hrefFor returning null -> '#', which the G3/dead-link checks in batch_check catch.
_FILE_KEY_TO_SLUG = {"food-security": "factors-affecting-food-security"}
_FILE_REF_RE = re.compile(r"\bFILE(?:\['([\w-]+)'\]|\.([a-z][\w]*))")


def apply_file_refs(source_file, logic):
    def sub(m):
        key = m.group(1) or m.group(2)
        return "(LNK('%s', '').href || '#')" % _FILE_KEY_TO_SLUG.get(key, key)
    if "let LNK_R = null;" not in logic:
        if _FILE_REF_RE.search(logic):
            raise RulingError("ks4_batch_rulings B10-FILE-REFS: %s reads FILE[...] but has no B8-LNK resolver." % source_file)
        return logic, []
    found = [m.group(1) or m.group(2) for m in _FILE_REF_RE.finditer(logic)]
    return _FILE_REF_RE.sub(sub, logic), found


# ── Batch 10 port mechanics (not science rulings) ──────────────────────
# B10-<SLUG>-CHIP, one per batch-10 lesson: her `common(done, F, ready)` returns a FRESH object (route: F.route, ...
# onRoute: F.R.onRoute ...), so B-R12's one route chip got no words and no menu. Same repair as B7/B8-<SLUG>-CHIP,
# spelled for her F.R shape.
_B10_SLUGS = ["ecosystems", "population-competition", "abiotic-biotic-factors", "adaptations", "food-chains-webs",
              "sampling-techniques", "environmental-change", "deforestation", "maintaining-biodiversity",
              "trophic-levels", "pyramids-of-biomass", "transfer-of-biomass", "farming-techniques",
              "sustainable-fisheries", "role-of-biotechnology"]
SCIENCE.extend(
    dict(id="B10-%s-CHIP" % sl.upper(), slug=sl, layer="logic",
         old="onRoute: F.R.onRoute || (() => {}), isHigher: F.H,",
         new="onRoute: F.R.onRoute || (() => {}), routeWords: F.R.routeWords, routeSwitchOptions: F.R.routeSwitchOptions, isHigher: F.H,")
    for sl in _B10_SLUGS)

# B10-<SLUG>-FOODSEC: her FILE key `food-security` is the live slug `factors-affecting-food-security` (Triple only, so the
# link is simply absent on a Combined route). Label unchanged.
SCIENCE.extend(
    dict(id="B10-%s-FOODSEC" % sl.upper(), slug=sl, layer="logic",
         old="LNK('food-security', 'Food security')",
         new="LNK('factors-affecting-food-security', 'Food security')")
    for sl in ["deforestation", "sustainable-fisheries", "farming-techniques", "role-of-biotechnology"])

# ═══ Batch 10: lane ruling (Mide) - batch 9 is not live, so every pointer to a batch 9 page is dropped ═══
# Each entry is one named drop; the before/after text is in the batch 10 port report so batch 9 can restore it.
SCIENCE.extend([
    dict(id="B10-ADAPTATIONS-B9-CONNECT", slug="adaptations", layer="logic",
         old="LNK('evolution-natural-selection', 'Evolution and natural selection'), ",
         new=""),
    dict(id="B10-ADAPTATIONS-B9-NSHREF-BIND", slug="adaptations", layer="logic",
         old="nsHref: (LNK('evolution-natural-selection', '').href || '#'), ",
         new=""),
    dict(id="B10-ADAPTATIONS-B9-NSLINK", slug="adaptations", layer="template",
         old='<a href="{{ nsHref }}">natural selection</a>',
         new="natural selection"),
    dict(id="B10-ENVIRONMENTAL-CHANGE-B9-CONNECT", slug="environmental-change", layer="logic",
         old=", LNK('variation', 'Variation')",
         new=""),
    dict(id="B10-FARMING-TECHNIQUES-B9-CONNECT", slug="farming-techniques", layer="logic",
         old=", LNK('resistant-bacteria', 'Resistant bacteria')",
         new=""),
    dict(id="B10-ROLE-OF-BIOTECHNOLOGY-B9-CONNECT", slug="role-of-biotechnology", layer="logic",
         old="LNK('genetic-engineering', 'Genetic engineering'), ",
         new=""),
    dict(id="B10-ROLE-OF-BIOTECHNOLOGY-B9-GEHREF-BIND", slug="role-of-biotechnology", layer="logic",
         old=" geHref: (LNK('genetic-engineering', '').href || '#'),",
         new=""),
    dict(id="B10-ROLE-OF-BIOTECHNOLOGY-B9-GELINK", slug="role-of-biotechnology", layer="template",
         old=' How the gene is moved is in <a href="{{ geHref }}">Genetic engineering</a>; here the chain is the point.',
         new=""),
])


# ═══ Batch 10 (examination): the lead's rulings on b10-a/b/c, exact strings from the examiners' files ═══
SCIENCE.extend([
    dict(id='B10-ECO-COMP', slug='ecosystems', layer='template',
         old='<p style="margin: 12px 0 0; max-width: 62ch;">Competition, and what plants and animals compete for, is taught in <a href="{{ pcHref }}">Population and competition</a>.</p>',
         new='<p style="margin: 12px 0 0; max-width: 62ch;">Plants in a community often compete with each other for light and space, and for water and mineral ions from the soil; animals often compete with each other for food, mates and territory. Competition is taught in full in <a href="{{ pcHref }}">Population and competition</a>.</p>'),
    dict(id='B10-ECO-ART', slug='ecosystems', layer='template',
         old='<p style="margin: 12px 0 0; max-width: 62ch;">A habitat is the place where an organism lives: the woodland floor, the canopy, a pond.</p>',
         new='<p style="margin: 12px 0 0; max-width: 62ch;">A habitat is the place where an organism lives: the woodland floor, the canopy, a pond.</p>\n        <p style="margin: 12px 0 0; max-width: 62ch;">People make artificial ecosystems too: farmland growing a single crop has far fewer species than a natural wood, because one crop dominates and most other species are removed.</p>'),
    dict(id='B10-ECO-WEB-1', slug='ecosystems', layer='logic',
         old="ar('grass', 'deer');",
         new="ar('grass', 'deer'); ar('flowers', 'deer');"),
    dict(id='B10-ECO-WEB-2', slug='ecosystems', layer='logic',
         old='Grass and shrubs feed deer, which feed wolves.',
         new='Grass, shrubs and flowering plants feed deer, which feed wolves.'),
    dict(id='B10-ECO-CHAIN', slug='ecosystems', layer='logic',
         old="'Their food supply falls.'",
         new="'So their food supply falls.'"),
    dict(id='B10-ECO-HOOK', slug='ecosystems', layer='logic',
         old='Nothing eats a flower’s bees, yet the flowers still need them',
         new='Flowers don’t eat bees, yet they still need them'),
    dict(id='B10-PC-YR-1', slug='population-competition', layer='logic',
         old="'Year 4: lynx peak, about a year and a half after the hare peak. Hares falling fast.'",
         new="'Year 4: lynx just past their peak, which came about a year and a half after the hare peak. Hares falling fast.'"),
    dict(id='B10-PC-YR-2', slug='population-competition', layer='logic',
         old='lynx go hungry and start to fall.',
         new='lynx go hungry and are falling.'),
    dict(id='B10-PC-NQ-1', slug='population-competition', layer='template',
         old='At year 5 the hares are falling fast.',
         new='At year 4 the hares are falling fast.'),
    dict(id='B10-PC-NQ-2', slug='population-competition', layer='logic',
         old='as the graph shows at years 5 to 7.',
         new='as the graph shows at years 4 to 6.'),
    dict(id='B10-PC-LAG', slug='population-competition', layer='logic',
         old='Y = (v) => 270 - v * 1.9',
         new='Y = (v) => 270 - v * 1.6'),
    dict(id='B10-ABF-CHAIN', slug='abiotic-biotic-factors', layer='logic',
         old="'Fish need dissolved oxygen for respiration.'",
         new="'So the fish get less of the dissolved oxygen they need for respiration.'"),
    dict(id='B10-ABF-PATH', slug='abiotic-biotic-factors', layer='logic',
         old='A pathogen is a living microorganism. A new disease',
         new='A pathogen is a living microorganism, such as a bacterium or a fungus. A new disease'),
    dict(id='B10-ABF-POND', slug='abiotic-biotic-factors', layer='logic',
         old="'The oxygen fell first; the fish depended on it.'",
         new="'Fewer fish would use less oxygen, not more; the warmer water held less.'"),
    dict(id='B10-ABF-OXY', slug='abiotic-biotic-factors', layer='logic',
         old='Warm or polluted water holds less.',
         new='Warm water holds less, and some pollution lowers it too.'),
    dict(id='B10-AD-FOX', slug='adaptations', layer='logic',
         old="{ name: 'Blood flow to its paws is reduced in the cold', t: 2, why: 'A process inside the body: less heat carried to the surface.' }",
         new="{ name: 'Thick fur on the soles of its paws', t: 0, why: 'A body part: insulates its feet from the snow and ice.' }"),
    dict(id='B10-AD-HUMP-1', slug='adaptations', layer='logic',
         old='storing fat in a hump.',
         new='surviving the loss of a lot of body water.'),
    dict(id='B10-AD-HUMP-2', slug='adaptations', layer='logic',
         old="'Fat in the hump (functional) is an energy store; it is not water.'",
         new="'Fat stored in the hump is an energy store; it is not water.'"),
    dict(id='B10-AD-JERB', slug='adaptations', layer='logic',
         old="and it never drinks, getting water from its food. Which is a functional adaptation?', 'Getting all its water from food: a process inside the body.', ['Getting all its water from its food'",
         new="and its kidneys make very concentrated urine. Which is a functional adaptation?', 'Making very concentrated urine: a process inside the body.', ['Making very concentrated urine'"),
    dict(id='B10-AD-CACT', slug='adaptations', layer='logic',
         old="['Spines instead of leaves give a small surface, so little water is lost.', 'The thick waxy stem stores water and stops it escaping.', 'Wide shallow roots take up rain quickly before it drains away.']",
         new="['Wide shallow roots take up rain quickly before it drains away.', 'The thick waxy stem stores that water and stops it escaping.', 'Spines instead of leaves give a small surface, so little of the stored water is lost.']"),
    dict(id='B10-AD-NS', slug='adaptations', layer='logic',
         old="so more of them survived and bred.'",
         new="so more of them survived, bred and passed the feature on to their offspring.'"),
    dict(id='B10-AD-PROD', slug='adaptations', layer='logic',
         old="['Producers', 'Some may be, but the name for organisms of very extreme environments is extremophiles.']",
         new="['Herbivores', 'Herbivores eat plants; the name for organisms of very extreme environments is extremophiles.']"),
    dict(id='B10-FCW-LVL-1', slug='food-chains-webs', layer='logic',
         old='chFig() {',
         new='chFig(T) {'),
    dict(id='B10-FCW-LVL-2', slug='food-chains-webs', layer='logic',
         old="+ TXN(x + 65, 212, 'level ' + (i + 1), 13, { fill: '#8A8378' });",
         new="+ (T ? TXN(x + 65, 212, 'level ' + (i + 1), 13, { fill: '#8A8378' }) : '');"),
    dict(id='B10-FCW-LVL-3', slug='food-chains-webs', layer='logic',
         old='chFig: fig(() => this.chFig()),',
         new='chFig: fig(() => this.chFig(T)),'),
    dict(id='B10-SAMP-STILL', slug='sampling-techniques', layer='logic',
         old='Thousands of daisies, and they do not stay still for you.',
         new='Thousands of daisies, far too many to count one by one.'),
    dict(id='B10-SAMP-YES', slug='sampling-techniques', layer='logic',
         old="yes: 'Yes. Random means every point in the habitat has the same chance",
         new="yes: 'Right. Random means every point in the habitat has the same chance"),
    dict(id='B10-ENV-MAP-1', slug='environmental-change', layer='template',
         old='A made-up butterfly, the hedge brown, was recorded in 10 km squares of Great Britain in 1980 and again in 2020.',
         new='A butterfly, the hedge brown, was recorded in grid squares across Great Britain in 1980 and again in 2020 (the records here are made up).'),
    dict(id='B10-ENV-MAP-2', slug='environmental-change', layer='template',
         old='The hedge brown butterfly, the river and all numbers are made up for practice.',
         new='The hedge brown records, the river and all numbers are made up for practice.'),
    dict(id='B10-ENV-MISMATCH', slug='environmental-change', layer='logic',
         old='Warmer springs: flowers bloom and insects emerge earlier; some species spread north or uphill, while species at the warm edge of their range lose ground.',
         new='Warmer springs: flowers bloom and insects emerge earlier; some species spread north or uphill, while species at the warm edge of their range lose ground. If a bird’s nesting does not shift as far as its food does, the two fall out of step and fewer chicks survive.'),
    dict(id='B10-ENV-EVOL-1', slug='environmental-change', layer='logic',
         old='Forty years is too short for evolution; the butterfly spread into places that had become warm enough.',
         new='Spreading into new squares is moving, not evolving; the butterfly may have spread into places that had become warm enough.'),
    dict(id='B10-ENV-EVOL-2', slug='environmental-change', layer='logic',
         old='Too fast for evolution; it moved into newly suitable areas.',
         new='A range shift is the species moving into newly suitable areas, not evolving.'),
    dict(id='B10-DEF-ARROW-1', slug='deforestation', layer='logic',
         old='D.arrow(340, 250, 340, 106, GREEN, 6)',
         new='D.arrow(340, 106, 340, 250, GREEN, 6)'),
    dict(id='B10-DEF-ARROW-2', slug='deforestation', layer='logic',
         old='D.arrow(170, 250, 170, 106, GREEN, 3)',
         new='D.arrow(170, 106, 170, 250, GREEN, 3)'),
    dict(id='B10-DEF-CHAIN-1', slug='deforestation', layer='logic',
         old="'Burning the felled trees releases carbon dioxide.'",
         new="'As well as that, burning the felled trees releases carbon dioxide.'"),
    dict(id='B10-DEF-CHAIN-2', slug='deforestation', layer='logic',
         old="'Microorganisms decaying the leftover wood respire, releasing more carbon dioxide.'",
         new="'Then microorganisms decaying the wood left after burning respire, releasing more carbon dioxide.'"),
    dict(id='B10-DEF-RAIL', slug='deforestation', layer='logic',
         old="short: 'CO2'",
         new="short: 'CO₂'"),
    dict(id='B10-MB-LABEL', slug='maintaining-biodiversity', layer='logic',
         old="TX(340, 28, 'hedgerow', 14, { fill: PAPER })",
         new="TX(340, 28, 'hedgerow', 14, { fill: INK })"),
    dict(id='B10-MB-CHAIN', slug='maintaining-biodiversity', layer='logic',
         old="'Recycling resources means less waste goes to landfill, so less land is lost and less pollution is made.'",
         new="'So recycling helps: less waste goes to landfill, so less land is lost and less pollution is made.'"),
    dict(id='B10-TL-ARROWS', slug='trophic-levels', layer='template',
         old='Further trophic levels are numbered subsequently according to how far the organism is along the food chain.</p>',
         new='Further trophic levels are numbered subsequently according to how far the organism is along the food chain. Each arrow points from the organism that is eaten to the organism that eats it: the direction in which energy and biomass are transferred.</p>'),
    dict(id='B10-PYR-TENTH', slug='pyramids-of-biomass', layer='logic',
         old="'Only about 10% passes to each level, so each bar is about a tenth of the one below.'",
         new="'Only about 10% passes to each level on average, so each bar is much narrower than the one below (here a fifth, then a tenth).'"),
    dict(id='B10-PYR-CHAIN', slug='pyramids-of-biomass', layer='logic',
         old="'Some absorbed material is lost as carbon dioxide and water in respiration, and as urea and water in urine.'",
         new="'Then some of the absorbed material is lost as carbon dioxide and water in respiration, and as urea and water in urine.'"),
    dict(id='B10-PYR-META', slug='pyramids-of-biomass', layer='template',
         old='divide every value by it. This is a drawing scale, not a spec equation, so there is no triangle.</p>',
         new='divide every value by it.</p>'),
    dict(id='B10-TOB-FARM', slug='transfer-of-biomass', layer='template',
         old='Less biomass at each level supports fewer organisms, so food chains rarely go beyond four or five levels.</p>',
         new='Less biomass at each level supports fewer organisms, so food chains rarely go beyond four or five levels. Farmers use this: limiting an animal’s movement means less of its food is used in respiration, so more becomes body mass.</p>'),
    dict(id='B10-TOB-CHAIN', slug='transfer-of-biomass', layer='logic',
         old="'Eating the grain directly is one transfer, so about ten times more biomass reaches the people.'",
         new="'So eating the grain directly, one transfer, passes about ten times more biomass to the people.'"),
    dict(id='B10-TOB-FOX', slug='transfer-of-biomass', layer='logic',
         old="'The spec’s losses are inside the fox: faeces, respiration, urine.'",
         new="'A fox eats most of a rabbit. The main losses are inside the fox: faeces, respiration, urine.'"),
    dict(id='B10-TOB-UNIT', slug='transfer-of-biomass', layer='logic',
         old="unit: 'g/m\\u00b2 or kg'",   # her source spells the superscript as the JS escape \u00b2 (same string as the examiner's literal ²)
         new="unit: 'g/m\\u00b2, kg/m\\u00b2 or kg (same unit for both)'", count=2),
    dict(id='B10-FT-SPLIT', slug='farming-techniques', layer='logic',
         old="'respiration: movement and heat '",
         new="'respiration, faeces, urine '"),
    dict(id='B10-FT-BATTERY', slug='farming-techniques', layer='logic',
         old='Battery chickens cannot exhibit natural behaviours',
         new='Intensively farmed chickens cannot exhibit natural behaviours'),
    dict(id='B10-FT-BATTERY-2', slug='farming-techniques', layer='logic',
         old='Battery farming produces more greenhouse gases',
         new='Intensive farming produces more greenhouse gases'),
    dict(id='B10-FT-JUDGE', slug='farming-techniques', layer='logic',
         old=', which the higher free-range price reflects',
         new='; free range avoids these but its meat costs twice as much, so the choice depends on how they are weighed'),
    dict(id='B10-FT-WARM', slug='farming-techniques', layer='template',   # examiner file said logic; the sentence is a Ks4Choice reveal attribute in her template
         old='no need to keep warm',
         new='less need to keep warm'),
    dict(id='B10-SF-STEADY', slug='sustainable-fisheries', layer='logic',
         old="['It rose steadily from 60 000 to 160 000 tonnes'",
         new="['It rose from 60 000 to 160 000 tonnes'"),
    dict(id='B10-SF-STEADY-2', slug='sustainable-fisheries', layer='logic',
         old="'The stock rose steadily, from 60 000 to 160 000 tonnes.'",
         new="'The stock rose, slowly at first, from 60 000 to 160 000 tonnes.'"),
    dict(id='B10-SF-STEADY-3', slug='sustainable-fisheries', layer='logic',
         old="'Nothing in the data says that; the stock rose steadily after the quota.'",
         new="'Nothing in the data says that; the stock rose after the quota.'"),
    dict(id='B10-SF-GRAPH', slug='sustainable-fisheries', layer='template',
         old='Use the graph',
         new='Use the data', count=2),
    dict(id='B10-SF-GRAPH-2', slug='sustainable-fisheries', layer='logic',
         old='Use the graph',
         new='Use the data', count=2),
    dict(id='B10-RB-FLOW', slug='role-of-biotechnology', layer='logic',
         old="why: 'Concerns about GM crops include the effect on populations of wild flowers and insects.' }",
         new="why: 'Concerns about GM crops include the effect on populations of wild flowers and insects. For example, a gene for herbicide resistance might spread in pollen to wild relatives of the crop, making weeds that are hard to control.' }"),
    dict(id='B10-RB-HERB', slug='role-of-biotechnology', layer='logic',
         old="GM crops are designed to withstand herbicide — they don't absorb more into edible tissue. The concern is about GENE FLOW to wild plants.",
         new='Herbicide residues in food are a separate, regulated question. The environmental concern is about GENE FLOW to wild plants.'),
    dict(id='B10-RB-RESP', slug='role-of-biotechnology', layer='template',
         old='because there is no animal respiring most of it away',
         new='because the fungus does not move or keep itself warm, so far less of the glucose is respired away'),
    dict(id='B10-RB-CHAIN', slug='role-of-biotechnology', layer='logic',
         old="'Air is supplied so the conditions are aerobic and the fungus grows.'",
         new="'Air is bubbled through the syrup, so the conditions are aerobic and the fungus grows.'"),
    dict(id='B10-RB-MADEUP', slug='role-of-biotechnology', layer='template',
         old='Information · made-up data for practice',
         new='Information'),
])


# ═══ Batch 10: fixes from the pupil walk (batch-10-walk.md; the lead's rulings) ═══
SCIENCE.extend([
    dict(id='B10W-AD-EARS', slug='adaptations', layer='logic',
         old="Ears don't store water — water is stored in fat (camels) or conserved through concentrated urine (kangaroo rats). The large ear surface area is for cooling.",
         new="Ears don't store water; desert animals save water in other ways, such as very concentrated urine (kangaroo rats). The large ear surface area is for cooling."),
    dict(id='B10W-DEF-DECAY', slug='deforestation', layer='logic',
         old='D.arrow(535, 250, 535, 106, RED, 6)',
         new='D.arrow(535, 222, 535, 106, RED, 6)'),
    dict(id='B10W-ECO-OAK', slug='ecosystems', layer='logic',
         old="D.line(230, 215, 230, 150, 5, GREEN) + D.circ(230, 135, 28, LEAF, INK, 2) + TXN(230, 240, 'oak', 13)",
         new="D.line(120, 218, 120, 184, 4, GREEN) + D.circ(120, 170, 14, LEAF, INK, 2) + TXN(120, 232, 'oak', 13)"),
    dict(id='B10W-ECO-WORM', slug='ecosystems', layer='logic',
         old="TXN(450, 240, 'earthworm', 13)",
         new="TXN(450, 232, 'earthworm', 13)"),
    dict(id='B10W-TL-MOLECULES', slug='trophic-levels', layer='logic',
         old="TXN(140, 200, 'small soluble molecules', 14, { fill: BLUE, anchor: 'start' })",
         new="TXN(470, 200, 'small soluble molecules', 14, { fill: BLUE, anchor: 'start' })"),
    dict(id='B10W-ABF-OUTCOMPETING', slug='abiotic-biotic-factors', layer='logic',
         old="'one species outcompeting', 'another'",
         new="'one species', 'outcompeting another'"),
    dict(id='B10W-TL-SPARROWHAWK', slug='trophic-levels', layer='logic',
         old='TX(x + 65, 154, it[0], 18)',
         new='TX(x + 65, 154, it[0], it[0].length > 9 ? 16 : 18)'),
    dict(id='B10W-SAMP-PAIRS', slug='sampling-techniques', layer='logic',
         old="'3, 7   8, 2   5, 4'",
         new="'(3, 7)  (8, 2)  (5, 4)'"),
    dict(id='B10W-SAMP-DAISY', slug='sampling-techniques', layer='logic',
         old="TR[s.tr][2] + ' daisies. '",
         new="TR[s.tr][2] + (TR[s.tr][2] === 1 ? ' daisy. ' : ' daisies. ')"),
    dict(id='B10W-TOB-TAB', slug='transfer-of-biomass', layer='logic',
         old="tab: 'Verbatim'",
         new="tab: 'Matching units'"),
    dict(id='B10W-PYR-LABELS', slug='pyramids-of-biomass', layer='logic',
         old='Math.max(w / 2, 70)',
         new='Math.min(Math.max(w / 2, 70), 250)', count=2),
    dict(id='B10W-FCW-QUOTES', slug='food-chains-webs', layer='template',
         old='The arrow means “eats”.&rdquo;',
         new='The arrow means ‘eats’.&rdquo;'),
    dict(id='B10W-DEF-HEADING', slug='deforestation', layer='template',
         old='Two arrows change.',
         new='Carbon in, carbon out.'),
    dict(id='B10W-DEF-LEAD', slug='deforestation', layer='template',
         old='watch both arrows.',
         new='watch the arrows change.'),
    dict(id='B10W-FCW-RABBITS-FX', slug='food-chains-webs', layer='logic',
         old="label: 'Rabbits double', fx: { grass: -1, fox: 1, shrew: -1 },",
         new="label: 'Rabbits double', fx: { grass: -1, rabbit: 1, fox: 1, shrew: -1, owl: -1 },"),
    dict(id='B10W-FCW-RABBITS-T', slug='food-chains-webs', layer='logic',
         old="more foxes also eat more shrews, so shrews fall.'",
         new="more foxes also eat more shrews, so shrews fall. Owls, which eat only shrews, have less food and fall.'"),
    dict(id='B10W-MY-1', slug='role-of-biotechnology', layer='logic',
         old="{ t: 'A large fermenter is filled with glucose syrup: the food for the fungus.' }",
         new="{ t: 'A large fermenter is filled with glucose syrup.' }"),
    dict(id='B10W-MY-2', slug='role-of-biotechnology', layer='logic',
         old="{ t: 'The fungus Fusarium is added. Air is bubbled through: aerobic conditions, so the fungus respires aerobically and grows fast.', gate:",
         new="{ t: 'The fungus Fusarium is added.', gate:"),
    dict(id='B10W-MY-3', slug='role-of-biotechnology', layer='logic',
         old="{ t: 'The fungus multiplies, filling the tank with fungal biomass.', gate:",
         new="{ t: 'Air is bubbled through: aerobic conditions, so the fungus respires aerobically and grows fast. The fungus multiplies, filling the tank with fungal biomass.', gate:"),
    dict(id='B10W-ECO-CASCADE', slug='ecosystems', layer='logic',
         old=' But the cascade of effects described is accurate.',
         new=''),
    dict(id='B10W-AD-INFO', slug='adaptations', layer='template',
         old='Information · made-up data for practice',
         new='Information'),
    # Re-walk: the figure drew "air in (aerobic)" from step 1, before the pupil predicts why air is bubbled
    # through; it now appears from step 2, where the text gives the reason (B10W-MY-3).
    dict(id='B10W-MY-AIRFIG', slug='role-of-biotechnology', layer='logic',
         old="if (i >= 1) { b += D.arrow(120, 250, 226, 250, BLUE, 3)",
         new="if (i >= 2) { b += D.arrow(120, 250, 226, 250, BLUE, 3)"),
    # Re-walk: "soil, water, temperature" ran across the Community box's bottom border at the Ecosystem step.
    dict(id='B10W-ECO-ABIOTIC-LBL', slug='ecosystems', layer='logic',
         old="TXN(90, 290, 'soil, water, temperature', 13, { anchor: 'start' })",
         new="TXN(90, 298, 'soil, water, temperature', 13, { anchor: 'start' })"),
])


# ═══ Batch 11: port mechanics (not science rulings) ═══
# B11-<SLUG>-CHIP, one per batch-11 lesson: her `common(done, F, ready[, rail])` returns a FRESH object with the same
# `onRoute: F.R.onRoute || (() => {}), isHigher: F.H,` as batch 10, so B-R12's route chip got no words and no menu.
# Same repair as B10-<SLUG>-CHIP.
_B11_SLUGS = ['model-of-the-atom', 'subatomic-particles', 'relative-atomic-mass', 'electronic-structure', 'group-7', 'transition-metals', 'mass-changes-reactions', 'chemical-measurements', 'moles', 'amounts-in-equations', 'oxidation-reduction', 'salts-neutralisation', 'ph-scale', 'strong-weak-acids', 'electrolysis-principles', 'electrolysis-molten']
SCIENCE.extend(
    dict(id="B11-%s-CHIP" % sl.upper(), slug=sl, layer="logic",
         old="onRoute: F.R.onRoute || (() => {}), isHigher: F.H,",
         new="onRoute: F.R.onRoute || (() => {}), routeWords: F.R.routeWords, routeSwitchOptions: F.R.routeSwitchOptions, isHigher: F.H,")
    for sl in _B11_SLUGS)

# B11-AIE-NOLINKS (lane ruling G2): amounts-in-equations ships CH TH, but Percentage yield and Atom economy are Triple-only
# pages (TF TH). On Combined Higher there is no such page, so the words stay and the link does not (no dead '#' anchor). On
# Triple Higher both link. Same rule as batch 8's "(Triple)" pointers. Inline <sc-if> inside the <p>.
SCIENCE.append(
    dict(id='B11-AIE-NOLINKS', slug='amounts-in-equations', layer='template',
         old='<a href="{{ pyHref }}">Percentage yield</a> and <a href="{{ aeHref }}">Atom economy</a>',
         new='<sc-if value="{{ isTriple }}"><a href="{{ pyHref }}">Percentage yield</a> and <a href="{{ aeHref }}">Atom economy</a></sc-if>'
             '<sc-if value="{{ notTriple }}">Percentage yield and Atom economy</sc-if>'))

# ═══ Batch 11 (examination): the lead's rulings, verbatim from the examiner files (RULINGS-b11) ═══
SCIENCE_B11 = [
    dict(id='B11-MOA-SORT', slug='model-of-the-atom', layer='template',
         old='title="Which model says this?"',
         new='title="Which model first said this?"'),
    dict(id='B11-MOA-CHAIN', slug='model-of-the-atom', layer='logic',
         old="'The electron was discovered: a particle much smaller than an atom, found inside atoms.'",
         new="'Then the electron was discovered: a particle much smaller than an atom, found inside atoms.'"),
    dict(id='B11-MOA-NAMES-1', slug='model-of-the-atom', layer='logic',
         old="{ t: 'Plum pudding model (about 1904): ",
         new="{ t: 'Plum pudding model (Thomson, about 1904): "),
    dict(id='B11-MOA-NAMES-2', slug='model-of-the-atom', layer='logic',
         old="{ t: 'Alpha-scattering experiment (1911): ",
         new="{ t: 'Rutherford’s alpha-scattering (gold foil) experiment (1911): "),
    dict(id='B11-SUB-KEYHT', slug='subatomic-particles', layer='logic',
         old="'Ions: atoms lose electrons to become positive, gain electrons to become negative. Protons never change. Neutrons = mass number − atomic number; electrons in an ion = protons − charge (²⁷₁₃Al³⁺: 13 p, 14 n, 10 e).', 'Higher: half equations such as Mg → Mg²⁺ + 2e⁻ and Cl₂ + 2e⁻ → 2Cl⁻ show the electrons lost or gained; the charge must balance on both sides.'],",
         new="'Ions: atoms lose electrons to become positive, gain electrons to become negative. Protons never change. Neutrons = mass number − atomic number; electrons in an ion = protons − charge (²⁷₁₃Al³⁺: 13 p, 14 n, 10 e).'].concat(F.H ? ['Higher: half equations such as Mg → Mg²⁺ + 2e⁻ and Cl₂ + 2e⁻ → 2Cl⁻ show the electrons lost or gained; the charge must balance on both sides.'] : []),"),
    dict(id='B11-SUB-CHAIN', slug='subatomic-particles', layer='logic',
         old="'The atomic number (bottom) is the number of protons.'",
         new="'Of that total, the atomic number (bottom) is the number of protons.'"),
    dict(id='B11-SUB-NEUTRAL', slug='subatomic-particles', layer='logic',
         old="no: ['', it.ch === 0 ? '' : 'That is the number of protons. The charge tells you electrons were ' + (it.ch > 0 ? 'lost' : 'gained') + '.', 'Wrong direction: a positive ion has lost electrons, a negative ion has gained them.'] });",
         new="no: ['', it.ch === 0 ? 'A neutral atom has as many electrons as protons: ' + it.Z + '.' : 'That is the number of protons. The charge tells you electrons were ' + (it.ch > 0 ? 'lost' : 'gained') + '.', it.ch === 0 ? 'A neutral atom has as many electrons as protons: ' + it.Z + '.' : 'Wrong direction: a positive ion has lost electrons, a negative ion has gained them.'] });"),
    dict(id='B11-SUB-SORTZ', slug='subatomic-particles', layer='logic',
         old="{ text: 'Its number is the atomic number', bin: 'p'",
         new="{ text: 'Its number is the atomic number, even in an ion', bin: 'p'"),
    dict(id='B11-RAM-21', slug='relative-atomic-mass', layer='logic',
         old="['21', 'That is the simple average of 10 and 11, with no abundances.']",
         new="['10.5', 'That is the simple average of 10 and 11, with no abundances.']"),
    dict(id='B11-RAM-AG', slug='relative-atomic-mass', layer='logic',
         old="CALC('Silver atoms are silver-107 and silver-109 in the ratio 13 : 12. Calculate the relative atomic mass of silver to 1 decimal place.', ['Nothing to convert', 'Convert the ratio to percentages: 52% and 48%', 'Convert the ratio to percentages: 13% and 12%'], 1, 107.96, 'no unit', ['no unit', 'g', '%'], '13 : 12 is 25 parts: 52% and 48%. [(52 × 107) + (48 × 109)] ÷ 100 = (5564 + 5232) ÷ 100 = 107.96, so 108.0.', 'Turn the ratio into percentages that add to 100 before inserting.', ['C · 13 : 12 = 52% and 48%', 'F · Ar = [Σ(% × mass number)] ÷ 100', 'I · Ar = [(52 × 107) + (48 × 109)] ÷ 100', 'F · Ar = 10 796 ÷ 100 = 107.96', 'A · 108.0 (no unit)'], 0.15)",
         new="CALC('Thallium atoms are thallium-203 and thallium-205 in the ratio 3 : 7. Calculate the relative atomic mass of thallium to 1 decimal place.', ['Nothing to convert', 'Convert the ratio to percentages: 30% and 70%', 'Convert the ratio to percentages: 3% and 7%'], 1, 204.4, 'no unit', ['no unit', 'g', '%'], '3 : 7 is 10 parts: 30% and 70%. [(30 × 203) + (70 × 205)] ÷ 100 = (6090 + 14 350) ÷ 100 = 204.4.', 'Turn the ratio into percentages that add to 100 before inserting.', ['C · 3 : 7 = 30% and 70%', 'F · Ar = [Σ(% × mass number)] ÷ 100', 'I · Ar = [(30 × 203) + (70 × 205)] ÷ 100', 'F · Ar = 20 440 ÷ 100 = 204.4', 'A · 204.4 (no unit)'], 0.15)"),
    dict(id='B11-RAM-ISOCHEM', slug='relative-atomic-mass', layer='template',
         old='Same atomic number, so the same element; different mass number.</p>',
         new='Same atomic number, so the same element; different mass number. Isotopes have the same number of electrons, and chemical reactions involve the electrons, so isotopes of an element have the same chemical properties.</p>'),
    dict(id='B11-RAM-CHAIN', slug='relative-atomic-mass', layer='logic',
         old="'About 75% of chlorine atoms are chlorine-35 and 25% are chlorine-37.'",
         new="'These isotopes are not equally common: about 75% of chlorine atoms are chlorine-35 and 25% are chlorine-37.'"),
    dict(id='B11-RAM-HERRING', slug='relative-atomic-mass', layer='logic',
         old="['Each chlorine atom has 17.5 neutrons.'",
         new="['Each chlorine atom has 18.5 neutrons.'"),
    dict(id='B11-RAM-UNIT', slug='relative-atomic-mass', layer='logic',
         old="{ letter: 'A', label: 'Answer', placeholder: 'with unit', line: a }",
         new="{ letter: 'A', label: 'Answer', placeholder: 'Ar has no unit', line: a }"),
    dict(id='B11-ES-OPTS', slug='electronic-structure', layer='logic',
         old="while (opts.length < 3) opts.push(right + ',1');",
         new="while (opts.length < 3) opts.push('1,' + cfg.slice(1, -1).concat([cfg[cfg.length - 1] + 1]).join(','));"),
    dict(id='B11-ES-CHAIN', slug='electronic-structure', layer='logic',
         old="'Elements with the same number of outer electrons are in the same group and have similar chemical properties.'",
         new="'So, like all elements with the same number of outer electrons, they are in the same group and have similar chemical properties.'"),
    dict(id='B11-G7-NOCHANGE-1', slug='group-7', layer='logic',
         old="(reacts ? ion.col : '#F3F0E7')",
         new='(reacts ? ion.col : h.col)'),
    dict(id='B11-G7-NOCHANGE-2', slug='group-7', layer='logic',
         old="' is less reactive than ' + ion.n + ', so nothing happens.'",
         new="' is less reactive than ' + ion.n + ', so nothing happens: the colour is just that of the halogen solution added.'"),
    dict(id='B11-G7-ORANGE', slug='group-7', layer='logic',
         old="['The solution turns orange', 'Orange would be bromine being displaced; here bromine is the one added, and it cannot displace chlorine.']",
         new="['The solution turns brown', 'Brown would be iodine forming. There is no iodide here, and bromine cannot displace chlorine.']"),
    dict(id='B11-G7-KEYHT', slug='group-7', layer='logic',
         old=", 'Higher: ionic equation Cl₂ + 2Br⁻ → 2Cl⁻ + Br₂. Chlorine gains electrons (reduced); bromide loses electrons (oxidised).'],",
         new="].concat(F.H ? ['Higher: ionic equation Cl₂ + 2Br⁻ → 2Cl⁻ + Br₂. Chlorine gains electrons (reduced); bromide loses electrons (oxidised).'] : []),"),
    dict(id='B11-G7-ELECTRONS', slug='group-7', layer='logic',
         old="'So chlorine takes the electrons from the bromide ions, forming chloride ions and bromine, which turns the solution orange.'",
         new="'So the more reactive chlorine displaces bromine from its salt, forming potassium chloride and bromine, which turns the solution orange.'"),
    dict(id='B11-G7-CHAIN1', slug='group-7', layer='logic',
         old="'Chlorine atoms gain an electron more readily than bromine atoms, because their outer shell is closer to the nucleus.'",
         new="'So chlorine is more reactive than bromine: it is above bromine in Group 7.'"),
    # B11W-G7-CHAIN-ORDER (re-ruled after the walk, D14): the three links now run reason → reactivity → displacement,
    # each leaning on the one before, so no second order reads sensibly.
    dict(id='B11W-G7-CHAIN-ORDER', slug='group-7', layer='logic',
         old="'Chlorine is above bromine in Group 7, so it is more reactive.'",
         new="'Chlorine atoms gain an electron more readily than bromine atoms, because their outer shell is closer to the nucleus.'"),
    dict(id='B11-G7-CHAIN2-1', slug='group-7', layer='logic',
         old="'Going down the group, atoms have more shells, so the outer shell is further from the nucleus.'",
         new="'Going down the group, atoms have more shells, so the outer shell, where that electron goes, is further from the nucleus.'"),
    dict(id='B11-G7-CHAIN2-2', slug='group-7', layer='logic',
         old="'The attraction between the nucleus and an incoming electron is weaker, so the electron is gained less easily.'",
         new="'So the attraction between the nucleus and an incoming electron is weaker, and the electron is gained less easily.'"),
    dict(id='B11-G7-MRCAUSE', slug='group-7', layer='template',
         old='Down the group the relative molecular mass, melting point and boiling point increase, because the intermolecular forces increase with the size of the molecules.',
         new='Down the group the relative molecular mass increases, and so do the melting point and boiling point, because the intermolecular forces increase with the size of the molecules.'),
    dict(id='B11-G7-CAPTION', slug='group-7', layer='logic',
         old="'boiling points: room temperature is about 20 °C, so chlorine is a gas, bromine a liquid, iodine a solid'",
         new="'boiling points; at room temperature (about 20 °C) chlorine is a gas, bromine a liquid, iodine a solid'"),
    dict(id='B11-G7-FIGLBL', slug='group-7', layer='logic',
         old='TX(x, y0 + h + 24, p[0], 16)',
         new='TX(x, y0 + h + 30, p[0], 16)'),
    dict(id='B11-G7-CASE', slug='group-7', layer='logic',
         old="no: [same ? 'Same element on both sides: nothing to displace.' : h.n + ' sits below ' + ion.n + ', so it cannot displace it.', h.n + ' is more reactive than ' + ion.n + ': it does displace it.']",
         new="no: [same ? 'Same element on both sides: nothing to displace.' : h.n[0].toUpperCase() + h.n.slice(1) + ' sits below ' + ion.n + ', so it cannot displace it.', h.n[0].toUpperCase() + h.n.slice(1) + ' is more reactive than ' + ion.n + ': it does displace it.']"),
    dict(id='B11-TM-CHAIN-1', slug='transition-metals', layer='logic',
         old="'Iron reacts only slowly with water and oxygen, so it lasts.'",
         new="'It also reacts only slowly with water and oxygen, so it lasts.'"),
    dict(id='B11-TM-CHAIN-2', slug='transition-metals', layer='logic',
         old="'Sodium is soft, melts at 98 °C and reacts vigorously with water and oxygen, so a structure made of it would fail.'",
         new="'Sodium, by contrast, is soft, melts at 98 °C and reacts vigorously with water and oxygen, so a structure made of it would fail.'"),
    dict(id='B11-MCR-KEYHT', slug='mass-changes-reactions', layer='logic',
         old=", 'Higher: predict the mass change from the balanced equation in three steps: n = m ÷ Ar, the molar ratio, then m = n × Mr. 4.8 g Mg gains 3.2 g of oxygen to make 8.0 g MgO.'],",
         new="].concat(F.H ? ['Higher: predict the mass change from the balanced equation in three steps: n = m ÷ Ar, the molar ratio, then m = n × Mr. 4.8 g Mg gains 3.2 g of oxygen to make 8.0 g MgO.'] : []),"),
    dict(id='B11-MCR-H2-1', slug='mass-changes-reactions', layer='logic',
         old="head: 'A beaker of acid and zinc has a mass of 0.5 kg at the start and 487 g at the end. Calculate the mass of hydrogen lost.'",
         new="head: 'A beaker of acid and marble chips has a mass of 0.5 kg at the start and 487 g at the end. Calculate the mass of carbon dioxide lost.'"),
    dict(id='B11-MCR-H2-2', slug='mass-changes-reactions', layer='logic',
         old="'13 g of hydrogen'",
         new="'13 g of carbon dioxide'"),
    dict(id='B11-MCR-H2-3', slug='mass-changes-reactions', layer='logic',
         old="'A tube of zinc and acid has a mass of 0.2 kg before and 196 g after. Calculate the mass of hydrogen lost.'",
         new="'A flask of marble chips and acid has a mass of 0.2 kg before and 196 g after. Calculate the mass of carbon dioxide lost.'"),
    dict(id='B11-MCR-H2-4', slug='mass-changes-reactions', layer='logic',
         old="'A tube of magnesium and acid has a mass of 0.3 kg before and 298 g after. Calculate the mass of hydrogen lost.'",
         new="'A flask of marble chips and acid has a mass of 0.3 kg before and 298 g after. Calculate the mass of carbon dioxide lost.'"),
    dict(id='B11-MCR-ALWAYS-1', slug='mass-changes-reactions', layer='template',
         old='The explanation is always a gas:',
         new='The explanation is usually a gas:'),
    dict(id='B11-MCR-ALWAYS-2', slug='mass-changes-reactions', layer='template',
         old='Every apparent change of mass in chemistry is a gas joining or leaving.',
         new='An apparent change of mass in a reaction is usually a gas joining or leaving.'),
    dict(id='B11-MCR-ALWAYS-3', slug='mass-changes-reactions', layer='logic',
         old='In chemistry a reading only rises when a gas joins the solid, as oxygen does when a metal burns.',
         new='A reading rises when a gas from the air joins the product, as oxygen does when a metal burns.'),
    dict(id='B11-CM-MENISCUS', slug='chemical-measurements', layer='logic',
         old='\'<path d="M604 160 q41 18 82 0" fill="\' + SKY + \'" stroke="\' + INK + \'" stroke-width="2"/>\' + \'<rect x="604" y="160" width="82" height="36" fill="\' + SKY + \'"/>\'',
         new='\'<path d="M604 160 q41 18 82 0 V196 H604 Z" fill="\' + SKY + \'"/>\' + \'<path d="M604 160 q41 18 82 0" fill="none" stroke="\' + INK + \'" stroke-width="2"/>\''),
    dict(id='B11-CM-REPRO', slug='chemical-measurements', layer='template',
         old='Reproducible: different investigators or equipment, similar results.',
         new='Reproducible: different investigators, different equipment, similar results.'),
    dict(id='B11-MOL-ATOMS', slug='moles', layer='template',
         old='The particles can be atoms, molecules, ions, electrons or formula units.</p>',
         new='The particles can be atoms, molecules, ions, electrons or formula units. Say which you are counting: one mole of water is 6.02 × 10<sup>23</sup> molecules, and each molecule has three atoms, so it is 3 × 6.02 × 10<sup>23</sup> atoms.</p>'),
    dict(id='B11-MOL-SFPICK-1', slug='moles', layer='template',
         old='= 1.204 × 10<sup>24</sup>. To divide',
         new='= 1.204 × 10<sup>24</sup>, because in standard form the front number must be between 1 and 10. To divide'),
    dict(id='B11-MOL-SFPICK-2', slug='moles', layer='template',
         old='What is 0.1 × 6.02 × 10<sup>23</sup>?</p>',
         new='What is 0.1 × 6.02 × 10<sup>23</sup> in standard form?</p>'),
    dict(id='B11-MOL-SF4', slug='moles', layer='logic',
         old="Avogadro constant = 6.02 × 10²³ per mole.',",
         new="Avogadro constant = 6.02 × 10²³ per mole. Give your answer in standard form.',"),
    dict(id='B11-MOL-CH1', slug='moles', layer='logic',
         old="'One mole contains 6.02 × 10²³ molecules.'",
         new="'Then use the Avogadro constant: one mole contains 6.02 × 10²³ molecules.'"),
    dict(id='B11-MOL-CH2', slug='moles', layer='logic',
         old="'The mass of a mole in grams equals the relative formula mass.'",
         new="'But the mass of a mole in grams equals the relative formula mass, which is different for each substance.'"),
    dict(id='B11-MOL-TAB', slug='moles', layer='logic',
         old="tab: 'Verbatim'",
         new="tab: 'Moles from mass'"),
    dict(id='B11-MOL-H2', slug='moles', layer='logic',
         old="why: 'Grams already: 4 ÷ 2 = 2 mol.'",
         new="why: 'Grams already; hydrogen gas is H₂, Mr 2: 4 ÷ 2 = 2 mol.'"),
    dict(id='B11-AIE-BRIDGE', slug='amounts-in-equations', layer='template',
         old='says two magnesium for every one oxygen, however much you make.',
         new='says two magnesium atoms for every one oxygen molecule, however much you make.'),
    dict(id='B11-AIE-RATIO', slug='amounts-in-equations', layer='template',
         old='Set the moles of magnesium and watch the oxygen and the oxide.</p>',
         new='Set the moles of magnesium and watch the oxygen and the oxide. To go from one substance to another, multiply by the wanted coefficient and divide by the given one.</p>'),
    dict(id='B11-AIE-O2MASS-1', slug='amounts-in-equations', layer='template',
         old='2 × 24 + 2 × 16',
         new='2 × 24 + 1 × 32'),
    dict(id='B11-AIE-O2MASS-2', slug='amounts-in-equations', layer='logic',
         old="'Count the coefficients: 2 × 24, 2 × 16 for O₂, 2 × 40.'",
         new="'Count the coefficients: 2 × 24, 1 × 32 for O₂, 2 × 40.'"),
    dict(id='B11-AIE-KEY1', slug='amounts-in-equations', layer='logic',
         old="'The balancing numbers in a symbol equation can be calculated from the masses of reactants and products by converting the masses in grams to amounts in moles; the coefficients are the mole ratio.'",
         new="'Chemical equations can be interpreted in terms of moles: Mg + 2HCl → MgCl₂ + H₂ shows that one mole of magnesium reacts with two moles of hydrochloric acid to produce one mole of magnesium chloride and one mole of hydrogen gas.'"),
    dict(id='B11-AIE-CH2', slug='amounts-in-equations', layer='logic',
         old="'The mass of one mole of a substance in grams is its Mr, so each coefficient × Mr gives a mass.'",
         new="'Then, because the mass of one mole of a substance in grams is its Mr, each coefficient × Mr gives a mass.'"),
    dict(id='B11-OXR-KEYFACT', slug='oxidation-reduction', layer='template',
         old='They always happen together. Higher: oxidation is loss of electrons, reduction is gain of electrons (OIL RIG).</p>',
         new='They always happen together.<sc-if value="{{ isHigher }}"> Higher: oxidation is loss of electrons, reduction is gain of electrons (OIL RIG).</sc-if></p>'),
    dict(id='B11-OXR-KEYNOTE', slug='oxidation-reduction', layer='logic',
         old="'Equations must balance. Chlorine and oxygen are Cl₂ and O₂.', 'Higher: oxidation is loss of electrons, reduction is gain of electrons (OIL RIG). Mg → Mg²⁺ + 2e⁻ (oxidised); Cu²⁺ + 2e⁻ → Cu (reduced); ionic equation Mg + Cu²⁺ → Mg²⁺ + Cu.', 'Higher: metals reacting with acids are redox: Mg + 2H⁺ → Mg²⁺ + H₂, magnesium oxidised, hydrogen ions reduced.'],",
         new="'Equations must balance. Chlorine and oxygen are Cl₂ and O₂.'].concat(F.H ? ['Higher: oxidation is loss of electrons, reduction is gain of electrons (OIL RIG). Mg → Mg²⁺ + 2e⁻ (oxidised); Cu²⁺ + 2e⁻ → Cu (reduced); ionic equation Mg + Cu²⁺ → Mg²⁺ + Cu.', 'Higher: metals reacting with acids are redox: Mg + 2H⁺ → Mg²⁺ + H₂, magnesium oxidised, hydrogen ions reduced.'] : []),"),
    dict(id='B11-OXR-CMDWRITE', slug='oxidation-reduction', layer='template',
         old='<div style="padding: 14px 16px; border-radius: var(--ks3-r-panel); background: var(--ks3-card); border: 2px solid var(--ks3-option-border);"><dt style="font-family: var(--ks3-font-display); font-weight: 800; font-size: 21px;">Write</dt><dd style="margin: 4px 0 0; font-size: 17px; line-height: 1.5;">(Higher) an ionic equation for a displacement reaction.</dd></div>',
         new='<sc-if value="{{ isHigher }}"><div style="padding: 14px 16px; border-radius: var(--ks3-r-panel); background: var(--ks3-card); border: 2px solid var(--ks3-option-border);"><dt style="font-family: var(--ks3-font-display); font-weight: 800; font-size: 21px;">Write</dt><dd style="margin: 4px 0 0; font-size: 17px; line-height: 1.5;">(Higher) an ionic equation for a displacement reaction.</dd></div></sc-if>'),
    dict(id='B11-OXR-ELECDIST', slug='oxidation-reduction', layer='logic',
         old="['Reduced: it loses electrons', 'In terms of oxygen, magnesium gains oxygen: oxidised.']",
         new="['Reduced: it loses oxygen', 'Magnesium gains oxygen; it does not lose it. Gaining oxygen is oxidation.']"),
    dict(id='B11-OXR-REDOX', slug='oxidation-reduction', layer='template',
         old='Oxidation is the gain of oxygen; reduction is the loss of oxygen. Watch the oxygen move',
         new='Oxidation is the gain of oxygen; reduction is the loss of oxygen. A reaction in which both happen is called a redox reaction. Watch the oxygen move'),
    dict(id='B11-OXR-ZNCHAIN', slug='oxidation-reduction', layer='logic',
         old="'The zinc oxide loses its oxygen and becomes zinc metal.'",
         new="'So the zinc oxide loses its oxygen to the carbon and becomes zinc metal.'"),
    dict(id='B11-OXR-LIGHTER', slug='oxidation-reduction', layer='logic',
         old="'Reduction is the loss of oxygen, named from the oxide losing mass, but it is a definition, not a weight test.'",
         new="'Reduction is the loss of oxygen. It is a definition, not a weight test.'"),
    dict(id='B11-OXR-CREACT', slug='oxidation-reduction', layer='template',
         old='Carbon reducing a metal oxide is how less reactive metals are extracted:',
         new='Metals less reactive than carbon can be extracted from their oxides by reduction with carbon:'),
    dict(id='B11-SN-H2O-1', slug='salts-neutralisation', layer='logic',
         old='["H₂ + O₂ → H₂O", false]',
         new='["2H₂ + O₂ → 2H₂O", false]'),
    dict(id='B11-SN-H2O-2', slug='salts-neutralisation', layer='logic',
         old="['H₂ + O₂ → H₂O', 'That is hydrogen burning.']",
         new="['2H₂ + O₂ → 2H₂O', 'That is hydrogen burning.']"),
    dict(id='B11-SN-STATE-1', slug='salts-neutralisation', layer='logic',
         old="['H⁺ + OH⁻ → H₂O', [",
         new="['H⁺(aq) + OH⁻(aq) → H₂O(l)', ["),
    dict(id='B11-SN-STATE-2', slug='salts-neutralisation', layer='logic',
         old='The ionic equation H⁺ + OH⁻ → H₂O shows the actual ions involved.',
         new='The ionic equation H⁺(aq) + OH⁻(aq) → H₂O(l) shows the actual ions involved.'),
    dict(id='B11-SN-SPECTATOR', slug='salts-neutralisation', layer='logic',
         old='"This is a precipitation ionic equation — it describes salt formation, not neutralisation."',
         new='"Na⁺ and Cl⁻ are spectator ions — they stay dissolved and do not react in neutralisation. Only H⁺ and OH⁻ react."'),
    dict(id='B11-SN-KEYTRIPLE', slug='salts-neutralisation', layer='logic',
         old="'Neutralisation: H⁺(aq) + OH⁻(aq) → H₂O(l). Triple: a salt from two soluble reactants is made by titration, then repeating without indicator.'],",
         new="'Neutralisation: H⁺(aq) + OH⁻(aq) → H₂O(l).'].concat(F.T ? ['Triple: a salt from two soluble reactants is made by titration, then repeating without indicator.'] : []),"),
    dict(id='B11-SN-CH2', slug='salts-neutralisation', layer='logic',
         old="'The excess solid is removed by filtering, leaving only the salt solution.'",
         new="'Finally the excess solid is removed by filtering, leaving only the salt solution.'"),
    dict(id='B11-SN-IONS', slug='salts-neutralisation', layer='template',
         old='The other ions (Na<sup>+</sup>, Cl<sup>−</sup>) are unchanged',
         new='The other ions (Na<sup>+</sup> and Cl<sup>−</sup>, for sodium hydroxide and hydrochloric acid) are unchanged'),
    dict(id='B11-SN-BASE-1', slug='salts-neutralisation', layer='template',
         old='The metal comes from the base.</p>',
         new='The metal comes from the base or carbonate.</p>'),
    dict(id='B11-SN-BASE-2', slug='salts-neutralisation', layer='logic',
         old="'Zinc carbonate is the base you started with.'",
         new="'Zinc carbonate is what you started with; the salt is named from the acid.'"),
    dict(id='B11-PH-CURVE', slug='ph-scale', layer='logic',
         old='const p = 7 + 6 / (1 + Math.exp(-(v - 25) * 0.9)) - 5.6 + (v < 25 ? -0.0 : 0);',
         new='const p = 1.4 + 11.2 / (1 + Math.exp(-(v - 25) * 0.9));'),
    dict(id='B11-PH-H2O2', slug='ph-scale', layer='logic',
         old="['H₂(g) + O₂(g) → H₂O(l)', 'That is hydrogen burning.']",
         new="['2H₂(g) + O₂(g) → 2H₂O(l)', 'That is hydrogen burning.']"),
    dict(id='B11-PH-KF-HT', slug='ph-scale', layer='template',
         old=' Higher: one pH unit is a factor of 10 in H<sup>+</sup> concentration.</p>',
         new='<sc-if value="{{ isHigher }}"> Higher: one pH unit is a factor of 10 in H<sup>+</sup> concentration.</sc-if></p>'),
    dict(id='B11-PH-KN-HT', slug='ph-scale', layer='logic',
         old="reaching it.', 'Higher: as the pH decreases by one unit, the hydrogen ion concentration increases by a factor of 10 (pH 1 has 100 times the H⁺ concentration of pH 3). Full treatment in Strong and weak acids.'],",
         new="reaching it.'].concat(F.H ? ['Higher: as the pH decreases by one unit, the hydrogen ion concentration increases by a factor of 10 (pH 1 has 100 times the H⁺ concentration of pH 3). Full treatment in Strong and weak acids.'] : []),"),
    dict(id='B11-PH-BIGQ', slug='ph-scale', layer='template',
         old='watch it climb as alkali is added to acid, and (Higher) know that each step is ten times.</p>',
         new='watch it climb as alkali is added to acid<sc-if value="{{ isHigher }}">, and know that each step is ten times</sc-if>.</p>'),
    dict(id='B11-PH-KF-SS', slug='ph-scale', layer='template',
         old='Neutralisation: H<sup>+</sup> + OH<sup>−</sup> → H<sub>2</sub>O.',
         new='Neutralisation: H<sup>+</sup>(aq) + OH<sup>−</sup>(aq) → H<sub>2</sub>O(l).'),
    dict(id='B11-PH-CH-SS', slug='ph-scale', layer='logic',
         old="'Hydrogen ions react with hydroxide ions to produce water: H⁺ + OH⁻ → H₂O.'",
         new="'Hydrogen ions react with hydroxide ions to produce water: H⁺(aq) + OH⁻(aq) → H₂O(l).'"),
    dict(id='B11-PH-WX3', slug='ph-scale', layer='logic',
         old='"3": "Unless you add enormous amounts of water, the pH approaches 7 gradually but never quite reaches it — you are diluting, not neutralising."',
         new='"3": "However much water you add, the pH approaches 7 gradually but never quite reaches it — you are diluting, not neutralising."'),
    dict(id='B11-PH-ROW', slug='ph-scale', layer='logic',
         old="no: ['Red and orange are the acids.', 'Green is neutral; purple is far above 7.', '']",
         new="no: ['Red, orange and yellow are the acids.', 'Green is neutral; purple is far above 7.', '']"),
    dict(id='B11-PH-EXACT', slug='ph-scale', layer='logic',
         old="'A pupil wants an exact pH value rather than an approximate one. What should she use?'",
         new="'A pupil wants a numerical pH value rather than an approximate one. What should she use?'"),
    dict(id='B11-SWA-CHAIN1', slug='strong-weak-acids', layer='logic',
         old="'Ethanoic acid is a weak acid, only partially ionised, so most molecules stay whole.'",
         new="'Ethanoic acid, by contrast, is a weak acid, only partially ionised, so most molecules stay whole.'"),
    dict(id='B11-SWA-NEARLY', slug='strong-weak-acids', layer='logic',
         old="'Hydrochloric acid is a strong acid, completely ionised, so nearly every molecule gives a hydrogen ion.'",
         new="'Hydrochloric acid is a strong acid, completely ionised, so every molecule gives a hydrogen ion.'"),
    dict(id='B11-SWA-CHAIN2', slug='strong-weak-acids', layer='logic',
         old="'Strong and weak describe the fraction of the acid that is ionised.'",
         new="'Strong and weak, by contrast, describe the fraction of the acid that is ionised.'"),
    dict(id='B11-SWA-2M', slug='strong-weak-acids', layer='logic',
         old="{ q: '2 mol/dm³ sulfuric acid', right: 0, yes: 'Strong and concentrated.', no: ['', '2 mol/dm³ is concentrated.', 'Sulfuric acid is strong.', 'Strong, and concentrated.'] },",
         new="{ q: '10 mol/dm³ sulfuric acid', right: 0, yes: 'Strong and concentrated.', no: ['', '10 mol/dm³ is concentrated.', 'Sulfuric acid is strong.', 'Strong, and concentrated.'] },"),
    dict(id='B11-SWA-PACK', slug='strong-weak-acids', layer='logic',
         old="tab: 'The pack’s example'",
         new="tab: 'Two units'"),
    dict(id='B11-SWA-HOOK', slug='strong-weak-acids', layer='logic',
         old="reply: 'Please not. Battery acid is sulfuric acid,",
         new="reply: 'Battery acid is sulfuric acid,"),
    dict(id='B11-SWA-ARROW', slug='strong-weak-acids', layer='template',
         old='The weak acid’s equation has a reversible arrow because most of it stays as molecules.',
         new='The weak acid’s ionisation is reversible, so its equation has a reversible arrow and most of it stays as molecules.'),
    dict(id='B11-EP-IONS-A', slug='electrolysis-principles', layer='logic',
         old="D.circ(gx, gy, 16, k % 2 ? LEAF : SKY, INK, 1.5) + TX(gx, gy + 4, k % 2 ? 'Br⁻' : 'Pb²⁺', 10)",
         new="D.circ(gx, gy, 16, k % 3 ? LEAF : SKY, INK, 1.5) + TX(gx, gy + 4, k % 3 ? 'Br⁻' : 'Pb²⁺', 10)"),
    dict(id='B11-EP-IONS-B', slug='electrolysis-principles', layer='logic',
         old="[390, 240, 'Pb²⁺']",
         new="[390, 240, 'Br⁻']"),
    dict(id='B11-EP-KN-HT', slug='electrolysis-principles', layer='logic',
         old="'A solid ionic compound cannot be electrolysed: its ions are fixed in the lattice.', 'Higher: at the cathode positive ions gain electrons (reduction); at the anode negative ions lose electrons (oxidation). Pb²⁺ + 2e⁻ → Pb; 2Br⁻ → Br₂ + 2e⁻.'],",
         new="'A solid ionic compound cannot be electrolysed: its ions are fixed in the lattice.'].concat(F.H ? ['Higher: at the cathode positive ions gain electrons (reduction); at the anode negative ions lose electrons (oxidation). Pb²⁺ + 2e⁻ → Pb; 2Br⁻ → Br₂ + 2e⁻.'] : []),"),
    dict(id='B11-EM-KN-HT', slug='electrolysis-molten', layer='logic',
         old="It is not a required practical: the electrolysis practical uses aqueous solutions.', 'Higher: half equations. Cathode (reduction): Pb²⁺ + 2e⁻ → Pb; Na⁺ + e⁻ → Na. Anode (oxidation): 2Br⁻ → Br₂ + 2e⁻; 2Cl⁻ → Cl₂ + 2e⁻. The charges balance.'],",
         new="It is not a required practical: the electrolysis practical uses aqueous solutions.'].concat(F.H ? ['Higher: half equations. Cathode (reduction): Pb²⁺ + 2e⁻ → Pb; Na⁺ + e⁻ → Na. Anode (oxidation): 2Br⁻ → Br₂ + 2e⁻; 2Cl⁻ → Cl₂ + 2e⁻. The charges balance.'] : []),"),
    dict(id='B11-EM-R4-P', slug='electrolysis-molten', layer='logic',
         old="explaining why the compound must be molten. (Higher: include the half equations.)',",
         new="explaining why the compound must be molten.' + (F.H ? ' Include the half equations.' : ''),"),
    dict(id='B11-EM-R4-PTS', slug='electrolysis-molten', layer='logic',
         old="'Higher: Na⁺ + e⁻ → Na at the cathode (reduction); 2Cl⁻ → Cl₂ + 2e⁻ at the anode (oxidation).', 'Overall: 2NaCl → 2Na + Cl₂.'],",
         new="F.H ? 'Na⁺ + e⁻ → Na at the cathode (reduction); 2Cl⁻ → Cl₂ + 2e⁻ at the anode (oxidation).' : null, 'Overall: 2NaCl → 2Na + Cl₂.'].filter(Boolean),"),
    dict(id='B11-EM-CMD', slug='electrolysis-molten', layer='template',
         old='<div style="padding: 14px 16px; border-radius: var(--ks3-r-panel); background: var(--ks3-card); border: 2px solid var(--ks3-option-border);"><dt style="font-family: var(--ks3-font-display); font-weight: 800; font-size: 21px;">Write</dt><dd style="margin: 4px 0 0; font-size: 17px; line-height: 1.5;">(Higher) balanced half equations for each electrode.</dd></div>',
         new='<sc-if value="{{ isHigher }}"><div style="padding: 14px 16px; border-radius: var(--ks3-r-panel); background: var(--ks3-card); border: 2px solid var(--ks3-option-border);"><dt style="font-family: var(--ks3-font-display); font-weight: 800; font-size: 21px;">Write</dt><dd style="margin: 4px 0 0; font-size: 17px; line-height: 1.5;">(Higher) balanced half equations for each electrode.</dd></div></sc-if>'),
    dict(id='B11-EM-Q1WX3', slug='electrolysis-molten', layer='logic',
         old='"3": "Electrolysis is done in an enclosed container — calcium doesn\'t react with air at this stage. The product is pure calcium metal."',
         new='"3": "Molten calcium chloride contains only Ca²⁺ and Cl⁻ ions — there is no oxygen in it. The product is pure calcium metal."'),
    dict(id='B11-EM-Q2WX3', slug='electrolysis-molten', layer='logic',
         old='Na⁺ and Cl⁻ (or Pb²⁺ and Br⁻) ions exist in the solid too',
         new='Pb²⁺ and Br⁻ ions exist in the solid too'),
]
SCIENCE.extend(SCIENCE_B11)

# ═══ Batch 11: fixes from the pupil walk (batch-11-walk.md; the lead's rulings) ═══
# D3: the compiler drops the whitespace-only text node between a closing </sup>/<sub> and the next <span>, so "2e⁻ loses"
# read "2e⁻loses". Fixed per page by moving the space INSIDE the span (the compiler and runtime are not touched: that would
# move earlier batches). A scan of the raw files and all 56 built pages found exactly these four joins.
B11W = [
    dict(id='B11W-SPACE-OXR', slug='oxidation-reduction', layer='template',
         old='2e<sup>−</sup> <span style="color: var(--ks3-ink-muted); font-size: 15px;">loses electrons: oxidised',
         new='2e<sup>−</sup><span style="color: var(--ks3-ink-muted); font-size: 15px;"> loses electrons: oxidised'),
    dict(id='B11W-SPACE-EP', slug='electrolysis-principles', layer='template',
         old='2e<sup>−</sup> <span style="color: var(--ks3-ink-muted); font-size: 15px;">loses electrons: oxidation',
         new='2e<sup>−</sup><span style="color: var(--ks3-ink-muted); font-size: 15px;"> loses electrons: oxidation'),
    dict(id='B11W-SPACE-SWA-CL', slug='strong-weak-acids', layer='template',
         old='Cl<sup>−</sup> <span style="color: var(--ks3-ink-muted); font-size: 15px;">strong: complete',
         new='Cl<sup>−</sup><span style="color: var(--ks3-ink-muted); font-size: 15px;"> strong: complete'),
    dict(id='B11W-SPACE-SWA-H', slug='strong-weak-acids', layer='template',
         old='H<sup>+</sup> <span style="color: var(--ks3-ink-muted); font-size: 15px;">weak: partial, reversible',
         new='H<sup>+</sup><span style="color: var(--ks3-ink-muted); font-size: 15px;"> weak: partial, reversible'),
    # D1: the nuclide's two labels were clipped at the left edge of the figure.
    # Re-walk of batch 11 (the lead): three figure faults the first walk missed, and D1 not yet clear.
    dict(id='B11W-SUB-SCALE-LBL', slug='subatomic-particles', layer='logic',
         old="TXN(262, 142, 'about 1 × 10⁻¹⁰ m', 13)",
         new="TXN(262, 166, 'about 1 × 10⁻¹⁰ m', 13)"),
    dict(id='B11W-EM-SIGN-NEG', slug='electrolysis-molten', layer='logic',
         old="TX(292, 48, '−', 18, { anchor: 'end' })",
         new="TX(292, 34, '−', 18, { anchor: 'end' })"),
    dict(id='B11W-EM-SIGN-POS', slug='electrolysis-molten', layer='logic',
         old="TX(408, 48, '+', 18, { anchor: 'start' })",
         new="TX(408, 34, '+', 18, { anchor: 'start' })"),
    dict(id='B11W-EP-LABELS', slug='electrolysis-principles', layer='logic',
         old="TX(220, 96, 'cathode (−)', 13) + TX(480, 96, 'anode (+)', 13)",
         new="TX(212, 96, 'cathode (−)', 13, { anchor: 'end' }) + TX(488, 96, 'anode (+)', 13, { anchor: 'start' })"),
    dict(id='B11W-EP-SIGN-NEG', slug='electrolysis-principles', layer='logic',
         old="TX(292, 56, '−', 18, { anchor: 'end' })",
         new="TX(292, 42, '−', 18, { anchor: 'end' })"),
    dict(id='B11W-EP-SIGN-POS', slug='electrolysis-principles', layer='logic',
         old="TX(408, 56, '+', 18, { anchor: 'start' })",
         new="TX(408, 42, '+', 18, { anchor: 'start' })"),
    dict(id='B11W-EM-PRODUCTS', slug='electrolysis-molten', layer='logic',
         old="TX(230, 275, c.metal, 13, { fill: BLUE }) + TX(470, 275, c.nm, 13, { fill: RED })",
         new="TX(262, 268, c.metal, 13, { fill: BLUE }) + TX(438, 268, c.nm, 13, { fill: RED })"),
    dict(id='B11W-RAM-LABELS', slug='relative-atomic-mass', layer='logic',
         old="TXN(60, 118, 'mass number', 13, { anchor: 'end', fill: MUTED }) + TXN(60, 166, 'atomic number', 13, { anchor: 'end', fill: MUTED })",
         new="TXN(96, 118, 'mass number', 13, { anchor: 'end', fill: MUTED }) + TXN(96, 166, 'atomic number', 13, { anchor: 'end', fill: MUTED })"),
    # D2: the curve ran through both labels; the y axis had no title.
    dict(id='B11W-PH-LABELS', slug='ph-scale', layer='logic',
         old="TXN(x0 + 60, Y(1.6), 'acid: low pH', 12, { fill: MUTED }) + TXN(x0 + w - 70, Y(12.6), 'excess alkali: high pH', 12, { fill: MUTED })",
         new="TXN(x0 + 60, Y(2.4), 'acid: low pH', 12, { fill: MUTED }) + TXN(x0 + w - 70, Y(11.6), 'excess alkali: high pH', 12, { fill: MUTED }) + TXN(x0, y0 - 10, 'pH', 12, { fill: MUTED })"),
    # D4: an authoring note shown as a pupil tab label.
    dict(id='B11W-RAM-TAB', slug='relative-atomic-mass', layer='logic',
         old="tab: 'Verbatim (bracket corrected)'",
         new="tab: 'Percentages'"),
    # D5
    dict(id='B11W-CM-WORKED', slug='chemical-measurements', layer='template',
         old='Worked (verbatim): 25.0 cm',
         new='Worked: 25.0 cm'),
    # D6: three captions ran into each other at phone width; the cylinder's "100" touched its rim.
    dict(id='B11W-CM-CAP-1', slug='chemical-measurements', layer='logic',
         old="TXN(103, 334, 'variable volume, ±0.05 cm³ a reading', 11, { fill: MUTED })",
         new="TXN(103, 332, 'variable volume,', 11, { fill: MUTED }) + TXN(103, 346, '±0.05 cm³ a reading', 11, { fill: MUTED })"),
    dict(id='B11W-CM-CAP-2', slug='chemical-measurements', layer='logic',
         old="TXN(290, 334, 'the smallest uncertainty for that volume', 11, { fill: MUTED })",
         new="TXN(290, 332, 'the smallest uncertainty', 11, { fill: MUTED }) + TXN(290, 346, 'for that volume', 11, { fill: MUTED })"),
    dict(id='B11W-CM-CAP-3', slug='chemical-measurements', layer='logic',
         old="TXN(470, 334, 'bigger graduations, bigger uncertainty', 11, { fill: MUTED })",
         new="TXN(470, 332, 'bigger graduations,', 11, { fill: MUTED }) + TXN(470, 346, 'bigger uncertainty', 11, { fill: MUTED })"),
    dict(id='B11W-CM-100', slug='chemical-measurements', layer='logic',
         old="TXN(458, 254 - i * 40, String(i * 25), 11, { anchor: 'start' })",
         new="TXN(458, 254 - i * 40 + (i === 4 ? 6 : 0), String(i * 25), 11, { anchor: 'start' })"),
    dict(id='B11W-CM-SVGH', slug='chemical-measurements', layer='logic',
         old="return D.svg(760, 350, b, 'Burette",
         new="return D.svg(760, 356, b, 'Burette"),
    # D7: the radius label ran past the right edge; its note moves down to keep clear.
    dict(id='B11W-SUB-RADIUS', slug='subatomic-particles', layer='logic',
         old="TX(430, 84, 'nucleus radius about 1 × 10⁻¹⁴ m', 15, { anchor: 'start' }) + TXN(430, 106, 'less than 1/10 000 of the atom’s radius', 13, { anchor: 'start', fill: MUTED })",
         new="TX(430, 76, 'nucleus radius', 15, { anchor: 'start' }) + TX(430, 94, 'about 1 × 10⁻¹⁴ m', 15, { anchor: 'start' }) + TXN(430, 112, 'less than 1/10 000 of the atom’s radius', 13, { anchor: 'start', fill: MUTED })"),
    # D9: Higher wording on the Foundation routes. Each clause now sits in the Higher sc-if; the space at the join is
    # inside the sc-if where the clause starts a sentence.
    dict(id='B11W-MCR-BIGQ', slug='mass-changes-reactions', layer='template',
         old='Explain both with particles, and (Higher) predict the change from the equation.</p>',
         new='Explain both with particles<sc-if value="{{ isHigher }}">, and (Higher) predict the change from the equation</sc-if>.</p>'),
    dict(id='B11W-MCR-CMD', slug='mass-changes-reactions', layer='template',
         old='The mass of gas lost from two readings; (Higher) the mass gained from the equation.</dd>',
         new='The mass of gas lost from two readings<sc-if value="{{ isHigher }}">; (Higher) the mass gained from the equation</sc-if>.</dd>'),
    dict(id='B11W-OXR-BIGQ', slug='oxidation-reduction', layer='template',
         old='one never happens without the other. On Higher, the same two words describe electrons changing hands.</p>',
         new='one never happens without the other.<sc-if value="{{ isHigher }}"> On Higher, the same two words describe electrons changing hands.</sc-if></p>'),
    dict(id='B11W-OXR-CMD', slug='oxidation-reduction', layer='template',
         old='Why, in terms of oxygen (or electrons on Higher).</dd>',
         new='Why, in terms of oxygen<sc-if value="{{ isHigher }}"> (or electrons on Higher)</sc-if>.</dd>'),
    dict(id='B11W-OXR-LEGAL', slug='oxidation-reduction', layer='template',
         old='check the atoms and, on Higher, the charges."',
         new='check the atoms."'),
    # D11: the ion line asked "How many electrons?" and so did the pick under it.
    dict(id='B11W-SUB-IONLINE', slug='subatomic-particles', layer='logic',
         old="', atomic number ' + it.Z + '. How many electrons?', ionQ",
         new="', atomic number ' + it.Z + '.', ionQ"),
    # D12: the reply's last sentence repeated the bridge that follows it.
    dict(id='B11W-OXR-LOST', slug='oxidation-reduction', layer='logic',
         old=" Oxygen from the air joined it. Gaining oxygen is called oxidation.' }",
         new=" Oxygen from the air joined it.' }"),
    dict(id='B11W-PH-SOUR', slug='ph-scale', layer='logic',
         old="Citric acid, at about pH 2 to 3. Sour is the taste of acids. On the pH scale",
         new="Citric acid, at about pH 2 to 3. On the pH scale"),
    # D13: steps A-E beside options lettered A-D read as "A B, C, A, D, E". The steps are numbered 1-5 (A=1 ... E=5):
    # the key B,C,A,D,E becomes 2,3,1,4,5 and each distractor keeps the same wrong order, so its reply still fits.
    dict(id='B11W-SN-STEPS', slug='salts-neutralisation', layer='logic',
         old="Q('Put the required-practical steps in order: A filter; B warm the acid; C add excess solid; D heat on a water bath until crystals form; E cool and dry.', 'B, C, A, D, E', [['C, B, A, D, E', 'Warm the acid first, then add the solid.'], ['B, C, D, A, E', 'Filter off the excess solid before crystallising.'], ['B, A, C, D, E', 'There is nothing to filter until the solid has been added.']])",
         new="Q('Put the required-practical steps in order: 1 filter; 2 warm the acid; 3 add excess solid; 4 heat on a water bath until crystals form; 5 cool and dry.', '2, 3, 1, 4, 5', [['3, 2, 1, 4, 5', 'Warm the acid first, then add the solid.'], ['2, 3, 4, 1, 5', 'Filter off the excess solid before crystallising.'], ['2, 1, 3, 4, 5', 'There is nothing to filter until the solid has been added.']])"),
    # D15: the readouts were wider than their boxes.
    dict(id='B11W-MCR-BOX', slug='mass-changes-reactions', layer='logic',
         old="BOX(x - 90, 230, 180, 34, PAPER, INK, 2.5, 8)",
         new="BOX(x - 115, 230, 230, 34, PAPER, INK, 2.5, 8)"),
    # D16: the wires ran through the centred electrode labels.
    dict(id='B11W-EM-LABELS', slug='electrolysis-molten', layer='logic',
         old="TX(230, 80, 'cathode (−)', 13) + TX(470, 80, 'anode (+)', 13)",
         new="TX(222, 80, 'cathode (−)', 13, { anchor: 'end' }) + TX(478, 80, 'anode (+)', 13, { anchor: 'start' })"),
    # D17: "melting point" clipped, and iron's density value ran into sodium's bar. Iron's bars are 200 (was 240); sodium's are
    # scaled by the same 5/6 so the drawn ratios stay 15x (melting point) and 8x (density), as the labels say.
    dict(id='B11W-TM-LABEL', slug='transition-metals', layer='logic',
         old="TXN(80, y + 6, label, 13, { anchor: 'end', fill: MUTED })",
         new="TXN(92, y + 6, label, 13, { anchor: 'end', fill: MUTED })"),
    dict(id='B11W-TM-MELT', slug='transition-metals', layer='logic',
         old="row(80, 'melting point', 240, 16,",
         new="row(80, 'melting point', 200, 13.3,"),
    dict(id='B11W-TM-DENSITY', slug='transition-metals', layer='logic',
         old="row(130, 'density', 240, 30,",
         new="row(130, 'density', 200, 25,"),
    # R1: the two strong-weak calc rungs reject 10^3 / 10^2, so they now ask for a whole number.
    dict(id='B11W-SWA-WHOLE-1', slug='strong-weak-acids', layer='logic',
         old="how many times greater the hydrogen ion concentration is in A.'",
         new="how many times greater the hydrogen ion concentration is in A. Give your answer as a whole number.'"),
    dict(id='B11W-SWA-WHOLE-2', slug='strong-weak-acids', layer='logic',
         old="hydrogen ion concentration is in the pH 1 solution.'",
         new="hydrogen ion concentration is in the pH 1 solution. Give your answer as a whole number.'"),
    # R10: true minus signs on the boiling-point value labels.
    dict(id='B11W-G7-MINUS', slug='group-7', layer='logic',
         old="p[1] + ' °C', 13)",
         new="String(p[1]).replace('-', '−') + ' °C', 13)"),
]
SCIENCE.extend(B11W)


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
        # ⊕ B10-ONE-ROUTE-SELECT: batch 10's one-route page (environmental-change, TH only) still draws a Route picker
        # with a single option. It is removed by the same R1 rule as every other page's picker; batch 7's one-route page
        # has none, so its path is unchanged. The tier chip must still be absent.
        if "<select" in tpl:
            tpl = ks4_rulings.apply_r1_route_selector(src, tpl)
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
    logic, _file_refs = apply_file_refs(src, logic)         # ⊕ batch 10: FILE['key'] in-text hrefs
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
    # ⊕ B11-G3-KS4: batch 11 only. Her FILE map points seven pages at `/ks4/<slug>` placeholders (G2). B8-LNK empties the
    # FILE map and every link resolves through KS4.hrefFor, so no `/ks4/` text can survive; this proves it per page.
    if lesson.get("batch") == "batch-11":
        for layer, text in (("template", tpl), ("logic", logic)):
            if "/ks4/" in text:
                raise RulingError("ks4_batch_rulings B11-G3-KS4: %s still carries a `/ks4/` placeholder in its %s after the "
                                  "link rulings." % (src, layer))
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
