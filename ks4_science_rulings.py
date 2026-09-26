#!/usr/bin/env python3
"""ks4_science_rulings.py — the 101 science-examiner rulings for the KS4 pilot.

Data-driven table of every "Required change" (section 2 of each file in
`docs/ks4/examination/`) across the 14 pilot lessons, PLUS the handful of
"applies to each route copy" findings from section 4 (the generated
`shared/ks4-source.js` copy) and the two documentation-only fixes (NOTES /
README). Row count per lesson, counted from the examiners' own `id` columns:

    L1  chemical-bonds                13   L8  properties-small-molecules  6
    L2  ionic-bonding                  4   L9  polymers                   10
    L3  ionic-compounds                9   L10 giant-covalent-structures   5
    L4  covalent-bonding               3   L11 metals-alloys              13
    L5  metallic-bonding               3   L12 nanoparticles               8
    L6  states-of-matter               2   L13 series-parallel-circuits    5
    L7  properties-ionic-compounds     6   L14 resistors                  14
                                                                   TOTAL  101

L11's count of 13 includes two commander's rulings (metals-alloys-C12, C13,
added 26 Sep 2026) beyond the examiner's original 11: dropping the CF/CH
quiz items that leaked chemistry-only steel recall (8462 4.10.3.2) onto
Combined routes, per the examiner's report §4.

Same pattern as `ks4_rulings.py` (which owns R1-R9, R-SLUG, R-PREVNEXT,
R-CONNECTS, R-BREADCRUMB — the PORT-MECHANICS rulings): every row is a
documented, MINIMAL, FAILS-LOUD transformation of Design's own text, never a
silent one. `_require` is copied from `ks4_rulings.py`'s pattern (imported
when available, else defined locally) so this file has no hard dependency on
the engine executor's file existing in a given worktree.

Layers:
  template  — Design's lesson `.dc.html` HTML inside `<x-dc>` (the part
              `template_and_logic()` returns as `tpl`).
  logic     — the `<script type="text/x-dc" data-dc-script>` class body (the
              part `template_and_logic()` returns as `logic`).
  asset     — a shared JS file such as `shared/ks4-diagrams.js`.
  source    — the GENERATED route copy in `shared/ks4-source.js` (the quiz/
              rp/key_note served for a route). Applied to the in-memory
              per-slug dict `build_source_record()` builds — see
              `apply_source()` below — never to the frozen
              `all_subtopics_*.py`.
  docs      — NOTES-KS4-pilot.md / README.txt. Record only: the delivery is
              committed unmodified, so these two rows are never applied,
              only asserted present in `--check`'s summary and named in the
              DEPARTURES register.

Two rows carry a `skip_apply` note instead of being applied by this file —
both because an examiner's finding turned out to be BYTE-IDENTICAL to a
ruling the engine executor had already built independently in
`ks4_rulings.py`:

  series-parallel-circuits-C1 — mirrors `ks4_rulings.R6` (flag 21, the
  "R_total = R1 + R2 is not on the equation sheet" chip on L13).

  metals-alloys-C8 — mirrors `ks4_rulings.R8` (flag 17, the "model data"
  relabel on L11's hardness-vs-carbon table).

Applying either a second time here would either double-fire (if this file
ran first, the engine's ruling would then find zero occurrences and raise)
or find nothing (if the engine's ruling ran first). Both stay in ROWS — with
`skip_apply=True` — so the row COUNTS (L13's 5, L11's 13, the 101 total) and
so `--check` still proves the examiner's finding was real against Design's
untouched reference file (`_selfcheck_mirrors()` additionally proves the two
copies of the text still agree). `apply()` never touches either row's text;
`applied_ids()` never reports either as fired. See the "Decisions" section
of the build report for the full reasoning.

Everything else fires normally.
"""

import copy
import json
import os
import re

try:
    from ks4_rulings import _require, RulingError
except Exception:  # pragma: no cover - ks4_rulings.py may be mid-edit by the engine lane
    class RulingError(SystemExit):
        pass

    def _require(text, needle, filename, ruling_id, expect=1):
        n = text.count(needle)
        if n != expect:
            raise RulingError(
                "ks4_science_rulings %s: expected %d occurrence(s) of a "
                "fixed string in %s, found %d.\n  looking for: %r"
                % (ruling_id, expect, filename, n, needle[:200]))

try:
    import ks4_lessons
    DESIGN_DIR = ks4_lessons.DESIGN_DIR
    LESSONS_BY_SLUG = {l["slug"]: l for l in ks4_lessons.LESSONS}
except Exception:  # pragma: no cover
    ks4_lessons = None
    DESIGN_DIR = os.path.join(
        "docs", "ks4", "design-reference", "pilot",
        "KS4 Lessons", "Pilot - Bonding and Electricity")
    LESSONS_BY_SLUG = {}

# Fallback slug -> design-file map, used only if ks4_lessons is unimportable
# (kept byte-identical to ks4_lessons.LESSONS so there is no second truth).
_DESIGN_FILE_FALLBACK = {
    "chemical-bonds": "ks4-chemistry-5.2.1.1-chemical-bonds.dc.html",
    "ionic-bonding": "ks4-chemistry-5.2.1.2-ionic-bonding.dc.html",
    "ionic-compounds": "ks4-chemistry-5.2.1.3-ionic-compounds.dc.html",
    "covalent-bonding": "ks4-chemistry-5.2.1.4-covalent-bonding.dc.html",
    "metallic-bonding": "ks4-chemistry-5.2.1.5-metallic-bonding.dc.html",
    "states-of-matter": "ks4-chemistry-5.2.2.1-states-of-matter.dc.html",
    "properties-ionic-compounds": "ks4-chemistry-5.2.2.3-properties-ionic-compounds.dc.html",
    "properties-small-molecules": "ks4-chemistry-5.2.2.4-properties-small-molecules.dc.html",
    "polymers": "ks4-chemistry-5.2.2.5-polymers.dc.html",
    "giant-covalent-structures": "ks4-chemistry-5.2.2.6-giant-covalent-structures.dc.html",
    "metals-alloys": "ks4-chemistry-5.2.2.7-metals-alloys.dc.html",
    "nanoparticles": "ks4-chemistry-5.2.3.3-nanoparticles.dc.html",
    "series-parallel-circuits": "ks4-physics-6.2.2-series-parallel-circuits.dc.html",
    "resistors": "ks4-physics-6.2.1.4-resistors-iv-required-practical.dc.html",
}


def design_file_for(slug):
    if slug in LESSONS_BY_SLUG:
        return LESSONS_BY_SLUG[slug]["design_file"]
    return _DESIGN_FILE_FALLBACK[slug]


# ═══════════════════════════════════════════════════════════════════════
# R6-equivalent text, kept here ONLY so --check can verify the examiner's
# finding was real (see the module docstring's "skip_apply" note). Copied
# from ks4_rulings.R6_FROM / R6_TO, 25 Sep 2026 — if ks4_rulings.py changes
# these strings, update this copy too (the two are asserted equal, along
# with the R8 mirror on metals-alloys-C8, in `_selfcheck_mirrors()`, called
# from `--check`).
# ═══════════════════════════════════════════════════════════════════════
_R6_MIRROR_FROM = (
    '<div style="padding: 16px 18px; border-radius: 14px; background: var(--ks3-card); border: 2px solid var(--ks3-option-border);">\n'
    '            <p style="margin: 0; font-family: var(--ks3-font-display); font-weight: 800; font-size: 28px;">R<sub>total</sub> = R₁ + R₂</p>')
_R6_MIRROR_TO = (
    '<div style="padding: 16px 18px; border-radius: 14px; background: var(--ks3-card); border: 2px solid var(--ks3-option-border);">\n'
    '            <span style="display: inline-block; margin-bottom: 8px; font-family: var(--ks3-font-mono); font-size: 13px; font-weight: 500; letter-spacing: .06em; text-transform: uppercase; padding: 3px 10px; border-radius: 99px; border: 2px solid var(--ks3-alert-border); color: var(--ks3-ink);">Not on the sheet · learn it</span>\n'
    '            <p style="margin: 0; font-family: var(--ks3-font-display); font-weight: 800; font-size: 28px;">R<sub>total</sub> = R₁ + R₂</p> <!-- ⊕ R6 -->')


# ═══════════════════════════════════════════════════════════════════════
# THE 99 ROWS
# ═══════════════════════════════════════════════════════════════════════
ROWS = [

    # ─── L1 chemical-bonds (13) ──────────────────────────────────────────
    dict(id="chemical-bonds-C1", lesson="chemical-bonds", layer="logic",
         old="hydrogen is not, even though it sits at the top of the table above sodium.",
         new="hydrogen is not, even though, like sodium, it has one outer electron.",
         why="Contradicts the page's own grid (H drawn above Group 4, as on the AQA data sheet); the one-outer-electron fact is table-independent.",
         spec="8462 4.1.1.7 / 4.2.1.1"),
    dict(id="chemical-bonds-C2", lesson="chemical-bonds", layer="logic",
         old="'Hydrogen sits above Group 1, but it is a non-metal. '",
         new="'Hydrogen has one outer electron, like Group 1, but it is a non-metal. '",
         why="As C1.", spec="4.2.1.1"),
    dict(id="chemical-bonds-C3", lesson="chemical-bonds", layer="logic",
         old="'Hydrogen sits above Group 1 but it is a non-metal. Two non-metals share.'",
         new="'Hydrogen has one outer electron like Group 1, but it is a non-metal. Two non-metals share.'",
         why="As C1.", spec="4.2.1.1"),
    dict(id="chemical-bonds-C4", lesson="chemical-bonds", layer="logic",
         old="'Hydrogen is a non-metal, even though it sits above Group 1.'",
         new="'Hydrogen is a non-metal, even though it has one outer electron like Group 1.'",
         why="As C1.", spec="4.2.1.1"),
    dict(id="chemical-bonds-C5", lesson="chemical-bonds", layer="template",
         old="A metal atom has one, two or three outer electrons and gives them away. A non-metal atom has four to seven and takes more in, or shares.",
         new="Most metal atoms have one, two or three outer electrons and give them away. Most non-metal atoms have four to seven and take more in, or share.",
         why="Excludes hydrogen (1 outer electron, non-metal) and Group 4 metals as written.",
         spec="4.1.1.7, 4.2.1.1"),
    dict(id="chemical-bonds-C6", lesson="chemical-bonds", layer="template",
         old="held by strong attraction all the way through, so they melt only when very hot.",
         new="held by strong attraction all the way through, so most melt only when very hot.",
         why="Spec says 'most metals'; Na (98°C) and K (63°C) are in this page's tray.",
         spec="4.2.2.7"),
    dict(id="chemical-bonds-C7", lesson="chemical-bonds", layer="logic",
         old="'Ions form when a metal gives electrons to a non-metal. With no non-metal here, nothing takes the electrons. '",
         new="'Ionic bonding needs a non-metal to take the electrons. With no non-metal here, nothing takes them, so no negative ions form. '",
         why="A metal is a lattice of positive ions; 'ions form when...' denies that and contradicts the verdict body that follows.",
         spec="4.2.1.5"),
    dict(id="chemical-bonds-C8", lesson="chemical-bonds", layer="logic",
         old="It builds giant covalent networks such as diamond and graphite, not small molecules.",
         new="It usually builds giant covalent structures such as diamond and graphite, not small molecules.",
         why="Fullerenes are molecules of carbon (core content). 'Giant covalent structures' is the spec's term.",
         spec="4.2.1.4, 5.2.3.3"),
    dict(id="chemical-bonds-C9", lesson="chemical-bonds", layer="logic",
         old="reply: 'Mass matters less than you might think here.'",
         new="reply: 'Mass does not decide which type of bond forms.'",
         why="Original implies mass partly decides bond type.", spec="4.2.1.1"),
    dict(id="chemical-bonds-C10", lesson="chemical-bonds", layer="logic",
         old="'\\u2070\\u00b9\\u00b2\\u00b3'[n]", new="'\\u2070\\u00b9\\u00b2\\u00b3\\u2074'[n]",
         why="Index 4 is undefined: every metal + carbon pair renders 'Cundefined⁻'. "
             "(File stores the superscripts as literal JS \\u escapes, not the unicode "
             "characters — old/new written to match the file's real bytes.)",
         spec="render defect carrying science text"),
    dict(id="chemical-bonds-C11", lesson="chemical-bonds", layer="logic",
         old="title = 'Ionic: ' + res.name + ', ' + res.formula;",
         new="title = 'Ionic: ' + res.name + (res.X.s === 'C' ? '' : ', ' + res.formula);",
         why="Metal + carbon formulae (calcium carbide etc.) are false for the named compounds; carbon ions are outside 4.2.1.2's scope.",
         spec="4.2.1.2"),
    dict(id="chemical-bonds-C12", lesson="chemical-bonds", layer="logic",
         old="if (res.X.s === 'C') body += ' Carbon rarely forms simple ions, so GCSE questions pair metals with Groups 6 and 7 instead.';",
         new="if (res.X.s === 'C') body = cap(res.M.n) + ' is a metal and carbon is a non-metal, so the GCSE rule calls this ionic. Carbon rarely forms simple ions, so no formula is given; GCSE questions pair metals with Groups 6 and 7 instead.';",
         why="Replaces the body so it no longer states a 'C⁴⁻' ion or a false ratio.",
         spec="4.2.1.2"),
    dict(id="chemical-bonds-C13", lesson="chemical-bonds", layer="logic",
         old="return D.svg(900, 300, D.T(450, 150, res.formula, 96)",
         new="if (res.X.s === 'C') return D.svg(900, 300, D.T(450, 160, res.M.s + ' + C', 96) + D.T(450, 230, 'metal with non-metal: ionic by the GCSE rule', 26, { weight: 'normal' }), res.name); return D.svg(900, 300, D.T(450, 150, res.formula, 96)",
         why="The chamber figure otherwise prints the false formula and 'C⁴⁻' ratio.",
         spec="4.2.1.2", old_survives=True),

    # ─── L2 ionic-bonding (4) ────────────────────────────────────────────
    dict(id="ionic-bonding-C1", lesson="ionic-bonding", layer="template",
         old="Both end up with the electron arrangement of a noble gas.",
         new="For Groups 1, 2, 6 and 7, both end up with the electron arrangement of a noble gas.",
         why="Stated for every metal + non-metal; false for transition-metal ions (4.1.3.2).",
         spec="8462 4.2.1.2 / 8464 5.2.1.2"),
    dict(id="ionic-bonding-C2", lesson="ionic-bonding", layer="logic",
         old="fLocked: fWorked || fZero, fBtnStyle: this.seg(false, fWorked || fZero),",
         new="fLocked: fWorked || fMin, fBtnStyle: this.seg(false, fWorked || fMin),",
         why="At a balanced but non-simplest box the verdict says 'Empty the box' while the button is disabled; locking only on the simplest ratio fixes the contradiction.",
         spec="8462 4.2.1.3"),
    dict(id="ionic-bonding-C3", lesson="ionic-bonding", layer="logic",
         old="fZero, fHasNext: s.f < 2,",
         new="fZero, fHasNext: fMin && s.f < 2,",
         why="A non-simplest ratio can be banked as 'balanced' and the pupil moved on.",
         spec="8462 4.2.1.3"),
    dict(id="ionic-bonding-C4", lesson="ionic-bonding", layer="logic",
         old="fProgress: s.fDone.length + ' of 3 balanced'",
         new="fProgress: (s.fDone.length + (s.f === 2 && fMin ? 1 : 0)) + ' of 3 balanced'",
         why="The third compound has no Next button, so it is never added to fDone; a correct Ca3N2 shows '2 of 3 balanced'.",
         spec="self-contradiction"),

    # ─── L3 ionic-compounds (9: C1-C7 logic, C8-C9 source) ──────────────
    dict(id="ionic-compounds-C1", lesson="ionic-compounds", layer="logic",
         old="Rock salt that has never been dissolved is cubic as well.",
         new="A dry crystal crushed with no water near it breaks into cubes too.",
         why="Rock salt formed by evaporation of seawater, so it HAS been dissolved; the replacement uses the page's own crushing evidence.",
         spec="8462 4.2.1.3 / 8464 5.2.1.3"),
    dict(id="ionic-compounds-C2", lesson="ionic-compounds", layer="logic",
         old="left, right, above and below it on the page.",
         new="left and right of it, and one row up and one row down.",
         why="'above and below' is used for the out-of-plane layers in the next tab and figure; reused for in-plane neighbours it self-contradicts.",
         spec="4.2.1.3"),
    dict(id="ionic-compounds-C3", lesson="ionic-compounds", layer="logic",
         old="so there is a layer in front and a layer behind.",
         new="so there is a layer above this one and a layer below it.",
         why="Aligns the note with the tab and figure labels it narrates.",
         spec="4.2.1.3"),
    dict(id="ionic-compounds-C4", lesson="ionic-compounds", layer="logic",
         old="No NaCl unit ever exists on its own.",
         new="In the solid, no NaCl unit exists on its own.",
         why="'ever' over-claims (NaCl ion pairs exist in the vapour); scoping to the solid keeps it true.",
         spec="4.2.1.3"),
    dict(id="ionic-compounds-C5", lesson="ionic-compounds", layer="logic",
         old="Gives no idea of the crystal being three-dimensional.",
         new="Shows the alternating pattern, but flat, with no depth.",
         why="Equally true of figure A (dot-and-cross), contradicting the 'exactly one model' prompt.",
         spec="4.2.1.3 bullet 2"),
    dict(id="ionic-compounds-C6", lesson="ionic-compounds", layer="logic",
         old="Draws sticks, as if each force acts along one line to one neighbour.",
         new="Joins the 3D cube with sticks, as if each force acts along one line.",
         why="Figure B (KS4D.lattice) also joins ions with lines; tying the item to the 3D model makes it unique to C.",
         spec="4.2.1.3 bullet 2"),
    dict(id="ionic-compounds-C7", lesson="ionic-compounds", layer="logic",
         old="Leaves big gaps between ions that really touch.",
         new="Spreads the 3D cube out, with big gaps between ions that really touch.",
         why="Figure B also leaves gaps; tying it to the 3D model makes it unique to C.",
         spec="4.2.1.3 bullet 2"),
    dict(id="ionic-compounds-C8", lesson="ionic-compounds", layer="source",
         op="edit", field="quiz", routes=["CH", "TH"],
         stem="wrong_explanations[3] on the giant-covalent-vs-ionic conduction item (CH8/TH8)",
         old="Giant covalent substances do not conduct when molten (graphite excepted), and their bonds do not 'melt' into charge carriers.",
         new="Giant covalent substances have no ions to free on melting (graphite conducts, but as a solid), and their bonds do not 'melt' into charge carriers.",
         why="'graphite excepted' implies molten graphite conducts where others don't; graphite sublimes (~3650°C) and conducts as a solid, not molten.",
         spec="8462 4.2.3.2"),
    dict(id="ionic-compounds-C9", lesson="ionic-compounds", layer="source",
         op="edit", field="quiz", routes=["CH", "TH"],
         stem="wrong_explanations[2] on the solubility item (CH10/TH10)",
         old="Water dissolves many ionic compounds (non-metal-containing), not just metals.",
         new="Water dissolves many ionic compounds, such as sodium chloride; it does not dissolve metals.",
         why="The parenthetical is meaningless and the sentence implies water dissolves metals.",
         spec="8462 4.2.1.3 / 4.2.2.3"),

    # ─── L4 covalent-bonding (3: C1-C2 logic, C3 source) ────────────────
    dict(id="covalent-bonding-C1", lesson="covalent-bonding", layer="template",
         old="like diamond and sand, where",
         new="like diamond and silicon dioxide (sand), where",
         why="'Sand' is a mixture; the spec names the substance, silicon dioxide.",
         spec="8462 4.2.1.4 / 8464 5.2.1.4"),
    dict(id="covalent-bonding-C2", lesson="covalent-bonding", layer="logic",
         old="why: 'If it were, it could not condense back into water on a cold window.'",
         new="why: 'Steam is H₂O molecules. Boiling only overcomes the weak forces between them; the O–H bonds stay.'",
         why="The current reason is a non-sequitur and gives no chemistry.",
         spec="8462 4.2.2.4 / 8464 5.2.2.4"),
    dict(id="covalent-bonding-C3", lesson="covalent-bonding", layer="source",
         op="edit", field="quiz", routes=["CF", "CH", "TF", "TH"],
         stem="quiz item 2 (O2 bonding) wrong_explanations[2]",
         old="Atoms of the same element do repel slightly, but covalent bonding (sharing) creates a stronger overall attraction.",
         new="Pairing up does not cancel a repulsion. Two O atoms bond because sharing two pairs gives each a full outer shell of 8.",
         why="States as fact that neutral atoms of the same element repel — not a GCSE idea and not correct as a general statement.",
         spec="8462 4.2.1.1 / 4.2.1.4"),

    # ─── L5 metallic-bonding (3) ─────────────────────────────────────────
    dict(id="metallic-bonding-C1", lesson="metallic-bonding", layer="logic",
         old="K.find(slug, R.route, 'Name the particles that are free to move in a metal') || K.find(slug, R.route, 'Describe the structure of a metal')",
         new="K.find(slug, R.route, 'Describe the structure of a metal') || K.find(slug, R.route, 'Name the particles that are free to move in a metal')",
         why="On CF/TF rung 1 is a 'Name' item shown under a 'Describe' chip with a why that answers a different question; the Describe item exists in all four route copies.",
         spec="4.2.1.5; AQA command words"),
    dict(id="metallic-bonding-C2", lesson="metallic-bonding", layer="logic",
         old="'The hot end vibrates hardest · energy spreads along'",
         new="'The hot end vibrates hardest · delocalised electrons carry the energy'",
         why="Caption named only ion vibration; the credited mechanism in a metal is delocalised electrons.",
         spec="8462 4.2.2.8 / 8464 5.2.2.8"),
    dict(id="metallic-bonding-C3", lesson="metallic-bonding", layer="logic",
         old="'Ions near the heated end vibrate strongly and the vibration spreads along the lattice'",
         new="'Ions near the heated end vibrate strongly and fast-moving delocalised electrons carry the energy along the lattice'",
         why="Same omission in the figure's accessible description.",
         spec="8462 4.2.2.8 / 8464 5.2.2.8"),

    # ─── L6 states-of-matter (2) ─────────────────────────────────────────
    dict(id="states-of-matter-C1", lesson="states-of-matter", layer="logic",
         old="The molecules separate from each other, but nothing inside them breaks.",
         new="The molecules break free of their fixed positions, but nothing inside them breaks.",
         why="In a liquid particles are still close together; 'separate from each other' describes boiling and contradicts the page's own explainer.",
         spec="8464 5.2.2.1 / 8462 4.2.2.1"),
    dict(id="states-of-matter-C2", lesson="states-of-matter", layer="logic",
         old="The tube is sealed off from the bath: only energy gets in.",
         new="The glass keeps the bath water out: only energy gets in.",
         why="A boiling tube in a water bath is open, not sealed.",
         spec="practical context of 5.2.2.1"),

    # ─── L7 properties-ionic-compounds (6) ──────────────────────────────
    dict(id="properties-ionic-compounds-C1", lesson="properties-ionic-compounds", layer="logic",
         old="{ text: '0 marks', correct: false, reply: 'It does say something creditworthy about the solution.' }",
         new="{ text: '0 marks', correct: true, reply: 'Zero. Having charged particles is not a marking point without free to move, and the solid does have charged particles.' }",
         why="The specimen meets none of the page's own three marking points; AQA would award 0.",
         spec="8462 4.2.2.3 / 8464 5.2.2.3; AQA MS convention"),
    dict(id="properties-ionic-compounds-C2", lesson="properties-ionic-compounds", layer="logic",
         old="{ text: '1 mark', correct: true, reply: 'One mark at most, for the solution containing charged particles, and some examiners would withhold even that.' }",
         new="{ text: '1 mark', correct: false, reply: 'Too generous. The solution having charged particles is not the marking point. The ions being free to move is, and it is never said.' }",
         why="Rewards the exact idea key-note line 6 says 'scores nothing' — a self-contradiction.",
         spec="8462 4.2.2.3; AQA MS"),
    dict(id="properties-ionic-compounds-C3", lesson="properties-ionic-compounds", layer="template",
         old="Say what will happen and give the reason from the structure.",
         new="Give a plausible outcome. Add the reason from the structure when the question also says explain.",
         why="AQA defines Predict as 'give a plausible outcome'; a reason is not required, and this lesson's own r2 asks for none.",
         spec="AQA command-word list"),
    dict(id="properties-ionic-compounds-C4", lesson="properties-ionic-compounds", layer="logic",
         old="(on ? ' \\u00b7 bulb on' : ' \\u00b7 switch open')",
         new="(on ? ' \\u00b7 bulb on' : ' \\u00b7 before the test')",
         why="beaker() draws a complete circuit with no switch, so 'switch open' names a component not drawn.",
         spec="circuit-diagram convention (8464 6.2.1.1)"),
    dict(id="properties-ionic-compounds-C5", lesson="properties-ionic-compounds", layer="logic",
         old="Free ions between two electrodes, before the switch is closed.",
         new="Free ions between two electrodes, before the bulb is tested.",
         why="Alt text names the same undrawn switch as C4.", spec="as C4"),
    dict(id="properties-ionic-compounds-C6", lesson="properties-ionic-compounds", layer="logic",
         old="{ command: 'State', marks: 1, why: 'Melt it or dissolve it in water: both free the ions to move.' }",
         new="{ command: R.isHigher ? 'Explain' : 'State', marks: 1, why: 'Melting or dissolving frees the ions to move, so they can carry charge; in the solid they are fixed.' }",
         why="On CH/TH, K.find falls back to an 'Explain' stem while the chip says 'State' and the why answers a different question.",
         spec="AQA command words; 4.2.2.3"),

    # ─── L8 properties-small-molecules (6) ──────────────────────────────
    dict(id="properties-small-molecules-C1", lesson="properties-small-molecules", layer="template",
         old="Small molecules also never conduct electricity:",
         new="Small-molecule substances also do not conduct electricity:",
         why="'Never' is false: HCl(aq) and other acids made from small molecules conduct.",
         spec="8462 4.2.2.4; 4.4.2.4"),
    dict(id="properties-small-molecules-C2", lesson="properties-small-molecules", layer="logic",
         old="Now try the other molecules: the bigger the molecule, the hotter you have to go.",
         new="Now try the other molecules: for chlorine, bromine and iodine, the bigger the molecule, the hotter you have to go.",
         why="Methane is bigger than water and boils 261°C lower, so the unscoped rule contradicts the bench.",
         spec="8462 4.2.2.4; 4.1.2.6"),
    dict(id="properties-small-molecules-C3", lesson="properties-small-molecules", layer="template",
         old="but at atmospheric pressure it does melt at 114 °C.",
         new="but at atmospheric pressure it does melt at 114 °C. Water boils far higher than its small size suggests: its molecules have an extra, stronger kind of intermolecular force, which GCSE does not require.",
         why="The bench shows water beside larger methane with no explanation of the anomaly.",
         spec="8462 4.2.2.4", old_survives=True),
    dict(id="properties-small-molecules-C4", lesson="properties-small-molecules", layer="template",
         old="The molecules are drawn to scale.",
         new="The molecules are drawn roughly to scale.",
         why="Drawn radii exaggerate the real Cl:Br:I size ratio.",
         spec="8462 4.2.1.4"),
    dict(id="properties-small-molecules-C5", lesson="properties-small-molecules", layer="logic",
         old="molecules drawn to scale, getting larger",
         new="molecules drawn roughly to scale, getting larger",
         why="As C4 (alt text).", spec="8462 4.2.1.4"),
    dict(id="properties-small-molecules-C6", lesson="properties-small-molecules", layer="logic",
         old="label: 'The state of hexane at 25 \\u00b0C'",
         new="label: 'The state of hexane at 25 \\u00b0C (it melts at \\u221295 \\u00b0C)'",
         why="'Use the data' cannot decide solid against liquid without a melting point, and the model answer cites one the pupil was never given.",
         spec="8462 4.2.2.1"),

    # ─── L9 polymers (10: C1-C3 logic, C4-C5 docs, C6-C10 source) ──────
    dict(id="polymers-C1", lesson="polymers", layer="logic",
         old="r1: Object.assign(K.find(slug, R.route, 'State what is meant by a monomer') || K.find(slug, R.route, 'Name the small molecules that join together') || { options: [] }, { command: 'State', marks: 1, why: 'A small molecule that joins with many others to make a polymer.' }),",
         new="r1: Object.assign((R.isTriple ? K.find(slug, R.route, 'State what is meant by a monomer') : K.find(slug, 'Combined Foundation', 'State what a polymer is')) || { options: [] }, { command: 'State', marks: 1, why: R.isTriple ? 'A small molecule that joins with many others to make a polymer.' : 'A polymer is a very large molecule made of many repeating units.' }),",
         why="'Monomer' is chemistry-only vocabulary (4.7.3.1); Combined routes must get the base item instead.",
         spec="8462 4.7.3.1; 8464 5.2.2.5, 5.2.1.4"),
    dict(id="polymers-C2", lesson="polymers", layer="template",
         old="Addition polymerisation · AQA 4.7.3.1 (chemistry only)",
         new="Addition polymerisation · AQA 4.7.3.1, 4.10.3.3 (chemistry only)",
         why="The block also teaches thermosoftening/thermosetting, which is 4.10.3.3.",
         spec="8462 4.10.3.3"),
    dict(id="polymers-C3", lesson="polymers", layer="template",
         old="Addition polymerisation and thermosetting polymers are separate-science content",
         new="Addition polymerisation, thermosoftening and thermosetting polymers are separate-science content",
         why="Thermosoftening is chemistry-only too; the line implied it was base.",
         spec="8462 4.10.3.3"),
    dict(id="polymers-C4", lesson="polymers", layer="docs",
         file="NOTES-KS4-pilot.md",
         old="| Thermosoftening / thermosetting polymers | `triple` | 8462 4.10.4.3 (chemistry only) |",
         new="| Thermosoftening / thermosetting polymers | `triple` | 8462 4.10.3.3 (chemistry only) |",
         why="Wrong section number (4.10.4 = Haber process / NPK). Documentation; the tag itself is right.",
         spec="8462 4.10.3.3"),
    dict(id="polymers-C5", lesson="polymers", layer="docs",
         file="README.txt",
         old="thermosoftening and thermosetting 4.10.4.3",
         new="thermosoftening and thermosetting 4.10.3.3",
         why="Same wrong number. Documentation.", spec="8462 4.10.3.3"),
    dict(id="polymers-C6", lesson="polymers", layer="source",
         op="edit", field="quiz", routes=["CF", "TF"],
         stem="'State what a polymer is.' wrong explanation",
         old="Polymers are non-metals, not metals.",
         new="Polymers are made of non-metal atoms, not metal atoms.",
         why="'Non-metal' classifies elements, not compounds.",
         spec="8464 5.2.1.1"),
    dict(id="polymers-C7", lesson="polymers", layer="source",
         op="drop_item", field="quiz", routes=["CF"],
         stems=[
             "Ethene (CH₂=CH₂) can be used to make poly(ethene), but ethane (C₂H₆) cannot. Explain why.",
             "Describe how a polymer forms from monomers.",
             "State what is meant by a monomer.",
             "Name the small molecules that join together to make a polymer.",
             "Identify the monomer used to make poly(ethene).",
             "State the type of bond in a monomer that allows addition polymerisation to happen.",
         ],
         why="Each tests addition polymerisation / monomer / C=C functional group — 8462 4.7.3.1, chemistry only.",
         spec="8462 4.7.3.1; 8464 5.7.1.4"),
    dict(id="polymers-C8", lesson="polymers", layer="source",
         op="drop_item", field="quiz", routes=["CH"],
         stems=[
             "Ethene (CH₂=CH₂) can be used to make poly(ethene), but ethane (C₂H₆) cannot. Explain why.",
             "Describe how a polymer forms from monomers.",
             "State what is meant by a monomer.",
             "Explain, in terms of the double bond, how addition polymerisation forms poly(ethene) from ethene.",
             "In addition polymerisation, explain why no small molecule is lost when the monomers join together.",
             "PVC is stiffer and higher-melting than poly(ethene). Suggest why, in terms of intermolecular forces.",
         ],
         why="4.7.3.1 chemistry-only items, plus PVC polarity (outside GCSE, flag-6 precedent).",
         spec="8462 4.7.3.1; 8464 5.2.2.5"),
    dict(id="polymers-C9", lesson="polymers", layer="source",
         op="drop_item", field="quiz", routes=["TH"],
         stems=["PVC is stiffer and higher-melting than poly(ethene). Suggest why, in terms of intermolecular forces."],
         why="Credited answer rests on bond polarity, not in 8462.",
         spec="8462 4.2.2.5, 4.10.3.3"),
    dict(id="polymers-C10", lesson="polymers", layer="source",
         op="edit", field="quiz", routes=["TH"],
         stem="TH12 stem",
         old="Explain why polymers are described as having a simple molecular structure, even though the molecules are very large.",
         new="Explain why a polymer is a molecular substance, not a giant covalent structure, even though its molecules are very large.",
         why="AQA classifies small molecules/polymers/giant structures as three separate kinds; 'simple molecular' is the small-molecule category and contradicts the page's own decider.",
         spec="8464 5.2.1.4, 5.2.2.5"),

    # ─── L10 giant-covalent-structures (5) ──────────────────────────────
    dict(id="giant-covalent-structures-C1", lesson="giant-covalent-structures", layer="template",
         old='prompt="Same element, same very high melting point. What differs?"',
         new='prompt="Same element, both very high melting points. What differs?"',
         why="Diamond and graphite do not have the SAME melting point; the spec only says both are very high.",
         spec="5.2.2.6"),
    dict(id="giant-covalent-structures-C2", lesson="giant-covalent-structures", layer="logic",
         old="right: 'Like diamond: every electron in a bond, bonds in every direction.'",
         new="right: 'Like diamond: strong covalent bonds in every direction, and no delocalised electrons or ions.'",
         why="In SiO2 the oxygen atoms keep lone pairs, so 'every electron in a bond' is false.",
         spec="5.2.2.6"),
    dict(id="giant-covalent-structures-C3", lesson="giant-covalent-structures", layer="logic",
         old="wrong: 'Silicon dioxide is bonded like diamond: a rigid network, all outer electrons in bonds.'",
         new="wrong: 'Silicon dioxide is bonded like diamond: a rigid network of strong covalent bonds, with no delocalised electrons or ions.'",
         why="Same error as C2.", spec="5.2.2.6"),
    dict(id="giant-covalent-structures-C4", lesson="giant-covalent-structures", layer="logic",
         old="'Both are giant covalent structures of carbon atoms, so both have very high melting points.'",
         new="'Both are giant covalent structures of carbon atoms: many strong covalent bonds must be broken to melt them, so both have very high melting points.'",
         why="The indicative point must carry the structure-to-property link the lesson's own Level 3 descriptor demands.",
         spec="5.2.2.6"),
    dict(id="giant-covalent-structures-C5", lesson="giant-covalent-structures", layer="logic",
         old="{ command: 'Identify', marks: 1, why: 'Hardness comes from the rigid network of strong covalent bonds.' }",
         new="{ command: R.isHigher ? 'Explain' : 'Identify', marks: 1, why: 'Hardness and the very high melting point both come from the rigid network of strong covalent bonds.' }",
         why="On CH/TH rung 1 resolves to an 'Explain' item; the 'Identify' chip then contradicts the stem, and the why omits melting point.",
         spec="5.2.3.1"),

    # ─── L11 metals-alloys (11) ──────────────────────────────────────────
    dict(id="metals-alloys-C1", lesson="metals-alloys", layer="template",
         old="Alloys as useful materials · AQA 4.10.4.2 (chemistry only)",
         new="Alloys as useful materials · AQA 4.10.3.2 (chemistry only)",
         why="Wrong spec reference; 4.10.4.2 is NPK fertilisers.", spec="8462 4.10.3.2"),
    dict(id="metals-alloys-C2", lesson="metals-alloys", layer="template",
         old="Most wedding rings are 18-carat",
         new="Many wedding rings are 18-carat",
         why="'Most' is an unsupported factual claim (9-carat is at least as common in the UK).",
         spec="8462 4.10.3.2 (context)"),
    dict(id="metals-alloys-C3", lesson="metals-alloys", layer="logic",
         old="The other metal atoms are a different size from gold atoms.",
         new="Copper atoms are a different size from gold atoms.",
         why="Silver, which the hook names, is the same size as gold (both 144 pm); copper is genuinely different.",
         spec="5.2.2.7"),
    dict(id="metals-alloys-C4", lesson="metals-alloys", layer="logic",
         old="so they catch on each other and cannot slide. The alloy is harder.",
         new="so they catch on each other and cannot slide easily. The alloy is harder.",
         why="Agrees with the key fact, chain and key note; alloys are harder, not undeformable.",
         spec="5.2.2.7"),
    dict(id="metals-alloys-C5", lesson="metals-alloys", layer="logic",
         old="Ionic compounds need melting because their charge carriers are ions, locked in place.",
         new="Ionic compounds need melting or dissolving because their charge carriers are ions, locked in place in the solid.",
         why="The credited option must include dissolving; 'locked in place' is true only in the solid.",
         spec="5.2.2.3"),
    dict(id="metals-alloys-C6", lesson="metals-alloys", layer="template",
         old="Steels are iron with carbon or other metals.",
         new="Steels are iron with carbon, and sometimes other metals.",
         why="Every steel contains carbon.", spec="8462 4.10.3.2"),
    dict(id="metals-alloys-C7", lesson="metals-alloys", layer="logic",
         old="why: 'A mixture of a metal with at least one other element, usually another metal.'",
         new="why: 'An alloy is a mixture of a metal with at least one other element; its different-sized atoms distort the regular layers of the pure metal.'",
         why="On CH/TH rung 1 serves 'Describe the difference in structure...', not 'State what an alloy is'; the why must fit both questions.",
         spec="5.2.2.7"),
    dict(id="metals-alloys-C8", lesson="metals-alloys", layer="logic",
         old="prompt: 'The table shows the hardness of iron mixed with different percentages of carbon.',",
         new="prompt: 'The table shows model data for the hardness of iron mixed with different percentages of carbon.', // ⊕ R8",
         why="The numbers are illustrative, not a cited data set (flag 17). "
             "BYTE-IDENTICAL to ks4_rulings.R8 (apply_r8_model_data) — same "
             "file, same flag 17, same fix. skip_apply=True: never applied "
             "by THIS file (see module docstring).",
         spec="WS 3.5; flag 17", skip_apply=True, mirrors="ks4_rulings.R8"),
    dict(id="metals-alloys-C9", lesson="metals-alloys", layer="logic",
         old="'Metals have giant structures: positive ions in regular layers, surrounded by delocalised electrons.'",
         new="'Metals have giant structures with strong metallic bonding, so most have high melting and boiling points.'",
         why="The 5.2.2.7 melting/boiling-point statement is otherwise absent from the page.",
         spec="5.2.2.7"),
    dict(id="metals-alloys-C10", lesson="metals-alloys", layer="template",
         old="with one delocalised electron per ion left out for clarity",
         new="with the delocalised electrons left out for clarity",
         why="Electrons per ion varies by metal (Na 1, Mg 2, Al 3).", spec="5.2.1.5"),
    dict(id="metals-alloys-C11", lesson="metals-alloys", layer="template",
         old="Named alloys and their uses are separate-science content and show only on Triple routes.",
         new="Recalling named alloys and their uses is separate-science content, taught only on Triple routes; elsewhere an alloy's make-up is given in the question.",
         why="Removes the self-contradiction — brass, steel and 18-carat gold appear on all routes as given information.",
         spec="8462 4.10.3.2 vs 8464 5.2.2.7"),
    dict(id="metals-alloys-C12", lesson="metals-alloys", layer="source",
         op="drop_item", field="quiz", routes=["CF"],
         stems=["Identify the correct description of steel."],
         why="Pure recall of steel's composition — 8462 4.10.3.2, chemistry only; "
             "8464 names no steel. TF9 keeps the item.",
         spec="8462 4.10.3.2; 8464 §4"),
    dict(id="metals-alloys-C13", lesson="metals-alloys", layer="source",
         op="drop_item", field="quiz", routes=["CH"],
         stems=["Stainless steel is used to make cutlery. Suggest two properties "
                "that make it suitable and relate them to its structure."],
         why="The credited answer depends on recalling that stainless steel "
             "resists corrosion — 8462 4.10.3.2 ('Steels containing chromium "
             "and nickel (stainless steels) are hard and resistant to "
             "corrosion'), chemistry only; not supplied in the stem. TH7 "
             "keeps the item.",
         spec="8462 4.10.3.2; 8464 §4"),

    # ─── L12 nanoparticles (8) ───────────────────────────────────────────
    dict(id="nanoparticles-C1", lesson="nanoparticles", layer="logic",
         old="a large fraction of the atoms sit on the surface",
         new="a far larger fraction of the atoms sit on the surface",
         why="A 25 nm gold particle has about 7% of its atoms on the surface; 'a large fraction' reads as 'most'.",
         spec="8462 4.2.4.1"),
    dict(id="nanoparticles-C2", lesson="nanoparticles", layer="template",
         old="A nanoparticle holds only a few hundred atoms; an atom is about 0.1 nm across.",
         new="Nanoparticles are of the order of a few hundred atoms; an atom has a radius of about 0.1 nm.",
         why="The spec's 0.1 nm is a RADIUS, not a diameter; 'only a few hundred' hardens 'of the order of' and contradicts the page's own 25 nm particle.",
         spec="8462 4.1.1.4; 4.2.4.1"),
    dict(id="nanoparticles-C3", lesson="nanoparticles", layer="logic",
         old="'A cube of side 1000 nm sliced into ' + (k * k * k) + ' smaller cubes, each of side '",
         new="'A cube of side 1000 nm sliced (drawn schematically, not to scale) into smaller cubes, each of side '",
         why="The alt text gives false counts (8 instead of 1000, etc.).", spec="MS 5c"),
    dict(id="nanoparticles-C4", lesson="nanoparticles", layer="template",
         old="The cube splitter draws a cube of each size sliced into smaller cubes of the same total volume.",
         new="The cube splitter draws a cube of each size sliced into smaller cubes of the same total volume; the number of slices drawn is schematic, not to scale.",
         why="The drawing shows 2, 4 and 8 slices per edge — the model-limits line must say this is schematic.",
         spec="MS 5c"),
    dict(id="nanoparticles-C5", lesson="nanoparticles", layer="logic",
         old="0.02 = 300, a thousand times too big.",
         new="0.02 = 300 per micrometre, a thousand times too big for an answer per nanometre.",
         why="300 µm⁻¹ is a correct value; the error is only in the unit asked for.",
         spec="MS 1b"),
    dict(id="nanoparticles-C6", lesson="nanoparticles", layer="template",
         old="Say how many times bigger: divide one ratio by the other.",
         new="Describe the similarities or differences; with ratios, say how many times bigger by dividing one by the other.",
         why="AQA defines 'Compare' as describing similarities and/or differences.",
         spec="AQA command-word glossary"),
    dict(id="nanoparticles-C7", lesson="nanoparticles", layer="logic",
         old="K.find(slug, R.route, 'State the range of sizes') || ",
         new="",
         why="On TF the needle hits a 'State' item while the rung carries command 'Describe' and a why for a different question; TF3/TH3 is the same verbatim item, so removing this needle gives both routes the same consistent rung.",
         spec="8462 4.2.4.1"),
    dict(id="nanoparticles-C8", lesson="nanoparticles", layer="logic",
         old="They contain a few hundred atoms.",
         new="They are of the order of a few hundred atoms.",
         why="Restores the spec's 'of the order of' (see C2); this is the key-note line pupils memorise.",
         spec="8462 4.2.4.1"),

    # ─── L13 series-parallel-circuits (5: C1 mirrors R6/skip, C2-C4 logic, C5 source) ──
    dict(id="series-parallel-circuits-C1", lesson="series-parallel-circuits", layer="template",
         old=_R6_MIRROR_FROM, new=_R6_MIRROR_TO,
         why="Flag 21: R_total = R1 + R2 is not on either June 2026 equation sheet. "
             "BYTE-IDENTICAL to ks4_rulings.R6 (apply_r6_rtotal_chip) — see module "
             "docstring. skip_apply=True: never applied by THIS file.",
         spec="8463 4.2.2 / 8464 6.2.2; AQA equation sheets, June 2026",
         skip_apply=True, mirrors="ks4_rulings.R6"),
    dict(id="series-parallel-circuits-C2", lesson="series-parallel-circuits", layer="logic",
         old="R\\u2081 is still across the battery: 12 V, and its lamp would stay lit.",
         new="R\\u2081 is still across the battery, so it still has the full 12 V and still carries 3 A.",
         why="There is no lamp in the circuit. (File stores the subscript as a literal "
             "\\u2081 escape, not the unicode character — old/new written to match.)",
         spec="4.2.2"),
    dict(id="series-parallel-circuits-C3", lesson="series-parallel-circuits", layer="logic",
         old="name: 'R\\u2082 removed'",
         new="name: 'R\\u2082 branch broken'",
         why="The step title is 'The R2 branch breaks.', but the drawn open switch is labelled "
             "'removed'. (The file stores the subscript as a literal \\u2082 escape, not the "
             "unicode character — fixed here to match the file's real bytes.)",
         spec="4.2.1.1, 4.2.2"),
    dict(id="series-parallel-circuits-C4", lesson="series-parallel-circuits", layer="template",
         old="Show every line. The unit earns its own mark.",
         new="Show every line. If the answer line does not print the unit, give it: it can carry a mark.",
         why="States a marking rule AQA does not apply; the unit is usually printed on the answer line.",
         spec="AQA command-word glossary; mark-scheme convention"),
    dict(id="series-parallel-circuits-C5", lesson="series-parallel-circuits", layer="source",
         op="edit", field="rp", routes=["CF", "CH", "TF", "TH"],
         old="RP15 (Physics) — Construct series and parallel circuits; measure I and V at different points to verify rules.",
         new="RP15 (Combined Science) / RP3 (Physics) — Use circuit diagrams to set up and check appropriate circuits to investigate the factors affecting the resistance of electrical circuits, including the length of a wire at constant temperature and combinations of resistors in series and parallel.",
         why="The source describes a practical that does not exist; also mislabels the Combined number as 'Physics'.",
         spec="8464 6.2.1.3 RP15 / 8463 4.2.1.3 RP3"),

    # ─── L14 resistors (14: C1-C9 lesson, C10-C12 asset, C13-C14 source) ──
    dict(id="resistors-C1", lesson="resistors", layer="template",
         old="Repeat for a range of p.d. values, switching off between readings so the component does not heat up.",
         new="Repeat for a range of p.d. values, switching off between readings so that the resistor stays at a constant temperature.",
         why="The method covers the filament lamp too, which MUST heat — that heating is the effect being measured.",
         spec="8463 RP4 / 8464 RP16; 4.2.1.4"),
    dict(id="resistors-C2", lesson="resistors", layer="logic",
         old="Keep it steady; switching off between readings helps.",
         new="Keep it steady, so that the only thing heating the filament is the current through it.",
         why="Switching off does not control room temperature.", spec="WS 2.2; 4.2.1.4"),
    dict(id="resistors-C3", lesson="resistors", layer="logic",
         old="and the negative half is a mirror of the positive half.",
         new="and the negative readings lie on the same straight line.",
         why="An ohmic I-V line continues through the origin; 'mirror' suggests a reflection (V shape).",
         spec="4.2.1.4"),
    dict(id="resistors-C4", lesson="resistors", layer="logic",
         old="One reading sits well below the curve: an anomaly, to be left out of the line of best fit.",
         new="A reading that sits well off the curve is an anomaly: leave it out of the line of best fit.",
         why="The anomaly is only planted if the 5th recorded reading is positive; the new sentence holds whichever order the pupil took readings in.",
         spec="WS 3.5, WS 3.7"),
    dict(id="resistors-C5", lesson="resistors", layer="logic",
         old="answer: 13.3, tol: 0.1,",
         new="answer: 13.3, tol: 0.35,",
         why="Tolerance is absolute; with 2-s.f. data (2.0 V, 150 mA) AQA credits 13 Ω, which the old tolerance rejects.",
         spec="4.2.1.3; MS 2a / WS 4.6"),
    dict(id="resistors-C6", lesson="resistors", layer="logic",
         old="a range of p.d. values set with the variable resistor, readings in both directions, and how the results are presented.",
         new="a range of p.d. values set with the variable resistor, readings recorded and repeated, and how the results are presented.",
         why="AQA's Level 3 is holistic; reversal is credited indicative content, not a gate.",
         spec="AQA 6-mark level-of-response convention; RP4/RP16"),
    dict(id="resistors-C7", lesson="resistors", layer="logic",
         old="'Lamp in series with an ammeter, a variable resistor and a battery.'",
         new="'Lamp in series with an ammeter, a variable resistor and a battery (or use a variable power supply).'",
         why="AQA credits either way of varying the p.d.", spec="RP4/RP16"),
    dict(id="resistors-C8", lesson="resistors", layer="logic",
         old="'Take a range of readings (e.g. at least 5) up to the lamp\\u2019s rated p.d.'",
         new="'Take a range of readings (e.g. at least 5) up to the lamp\\u2019s rated p.d.; repeat them and calculate means.'",
         why="Repeat readings and means are standard AQA indicative content for an RP method.",
         spec="WS 2.6, WS 3.7; MS 2b"),
    dict(id="resistors-C9", lesson="resistors", layer="template",
         old='<p style="margin: 0; font-family: var(--ks3-font-display); font-weight: 800; font-size: 28px;">V = I R</p>',
         new='<span style="display: inline-block; margin-bottom: 8px; font-family: var(--ks3-font-mono); font-size: 13px; font-weight: 500; letter-spacing: .06em; text-transform: uppercase; padding: 3px 10px; border-radius: 99px; border: 2px solid var(--ks3-ink);">Equation sheet</span><p style="margin: 0; font-family: var(--ks3-font-display); font-weight: 800; font-size: 28px;">V = I R</p>',
         why="V = I R is on both June 2026 sheets; L13's identical card carries the chip, L14's should match.",
         spec="8463/8464 June 2026 equation sheets", old_survives=True),
    dict(id="resistors-C10", lesson="shared", layer="asset", file="ks4-diagrams.js",
         old="cell: function (x, y, it) { return leads(x, y, 36) +",
         new="cell: function (x, y, it) { return leads(x, y, 18) +",
         why="Without this the leads stop 9px short of the plates, drawing every cell as an open circuit.",
         spec="8463 4.2.1.1 (cell symbol)"),
    dict(id="resistors-C11", lesson="shared", layer="asset", file="ks4-diagrams.js",
         old="battery: function (x, y, it) { var s = leads(x, y, 70); [-22, 14].forEach(function (dx) {",
         new='battery: function (x, y, it) { var s = leads(x, y, 52) + line(x - 10, y, x + 10, y, 2, C.stroke, \' stroke-dasharray="4 5"\'); [-26, 10].forEach(function (dx) {',
         why="Centres the two cells, brings leads to the outer plates, and joins the cells with AQA's dashed link.",
         spec="8463 4.2.1.1 (battery symbol)"),
    dict(id="resistors-C12", lesson="shared", layer="asset", file="ks4-diagrams.js",
         old="circ(x - 30, y, 5, C.stroke) + circ(x + 30, y, 5, C.stroke)",
         new="circ(x - 30, y, 6, C.cream, C.stroke, 2.5) + circ(x + 30, y, 6, C.cream, C.stroke, 2.5)",
         why="AQA's switch contacts are hollow circles; filled dots mean junctions.",
         spec="8463 4.2.1.1 (switch open/closed)"),
    dict(id="resistors-C13", lesson="resistors", layer="source",
         op="edit", field="rp", routes=["CF", "CH", "TF", "TH"],
         old="RP16 (Physics) — Construct circuits to investigate I–V characteristics of a filament lamp, diode and resistor. Plot graphs and interpret each.",
         new="RP16 (Combined Science) / RP4 (Physics) — Construct circuits to investigate the I–V characteristics of a filament lamp, a diode and a resistor at constant temperature. Plot graphs and interpret each.",
         why="RP16 is the 8464 number, not the Physics one (8463 RP4); also restores 'at constant temperature'.",
         spec="8463 §8.2.4 RP4; 8464 RP16"),
    dict(id="resistors-C14", lesson="resistors", layer="source",
         op="edit", field="key_note", routes=["CF", "CH", "TF", "TH"],
         old="RP16: investigate I–V graphs for resistor, lamp, diode.",
         new="Required practical (RP16 Combined / RP4 Physics): investigate I–V graphs for resistor, lamp, diode.",
         why="Same numbering error as C13; only matters if the port ever serves key_note verbatim.",
         spec="8463 RP4; 8464 RP16"),
]

assert len(ROWS) == 101, "ks4_science_rulings: expected 101 rows, found %d" % len(ROWS)

# Expected row count per lesson slug, counted from each examination file's
# own §2 "Required changes" table (resistors' asset-layer rows C10-C12 are
# filed under lesson="shared" since they touch the shared `ks4-diagrams.js`,
# not a single lesson file — so "resistors" below is 14 - 3 = 11).
_EXPECTED_PER_LESSON = {
    "chemical-bonds": 13, "ionic-bonding": 4, "ionic-compounds": 9,
    "covalent-bonding": 3, "metallic-bonding": 3, "states-of-matter": 2,
    "properties-ionic-compounds": 6, "properties-small-molecules": 6,
    "polymers": 10, "giant-covalent-structures": 5, "metals-alloys": 13,
    "nanoparticles": 8, "series-parallel-circuits": 5, "resistors": 11,
    "shared": 3,  # resistors-C10..C12 (asset: ks4-diagrams.js)
}
_actual_per_lesson = {}
for _r in ROWS:
    _actual_per_lesson[_r["lesson"]] = _actual_per_lesson.get(_r["lesson"], 0) + 1
assert _actual_per_lesson == _EXPECTED_PER_LESSON, (
    "ks4_science_rulings: per-lesson row count drifted from the examiners' "
    "own counts.\n  expected: %r\n  actual:   %r"
    % (_EXPECTED_PER_LESSON, _actual_per_lesson))
del _r


def rows_for(layer, name):
    if layer == "asset":
        # asset rows are keyed by their shared-file name (row["file"]), not
        # by a lesson slug — several lessons can share one asset file.
        return [r for r in ROWS if r["layer"] == "asset" and r.get("file") == name]
    return [r for r in ROWS if r["layer"] == layer and r["lesson"] == name]


def row_by_id(rid):
    for r in ROWS:
        if r["id"] == rid:
            return r
    raise KeyError(rid)


# ═══════════════════════════════════════════════════════════════════════
# applied_ids() bookkeeping
# ═══════════════════════════════════════════════════════════════════════
_FIRED = []


def reset_applied():
    _FIRED[:] = []


def applied_ids():
    return list(_FIRED)


# ═══════════════════════════════════════════════════════════════════════
# apply(layer, name, text) — template / logic / asset / docs rows.
# Called once per (layer, name) target. `name` is the LESSON SLUG for
# layer in ('template', 'logic'), the asset filename for layer == 'asset'
# (e.g. 'ks4-diagrams.js'), and the docs filename for layer == 'docs'
# (never actually applied — see module docstring).
# ═══════════════════════════════════════════════════════════════════════
def apply(layer, name, text):
    for row in rows_for(layer, name):
        if row.get("skip_apply"):
            continue
        if layer == "docs":
            continue  # record only — never applied to a committed delivery
        old, new = row["old"], row["new"]
        _require(text, old, "%s (%s)" % (name, layer), row["id"])
        text = text.replace(old, new, 1)
        _FIRED.append(row["id"])
    return text


# ═══════════════════════════════════════════════════════════════════════
# apply_source(src) — the `source` rows, against the in-memory per-slug
# dict `build_ks4.build_source_record()` builds (BEFORE it is serialised to
# `shared/ks4-source.js`). `src` is `{slug: {..fields.., "quiz": {route:
# [items...]}}}` for every one of the 14 lessons (build_source_js's
# `per_slug`) — see build_ks4.py STEP A. Mutates and returns a deep copy.
# ═══════════════════════════════════════════════════════════════════════
def _walk_replace(node, old, new):
    """Recursively replace `old` with `new` in every string leaf of `node`.
    Returns (new_node, count)."""
    if isinstance(node, str):
        n = node.count(old)
        if n:
            return node.replace(old, new), n
        return node, 0
    if isinstance(node, list):
        total = 0
        out = []
        for item in node:
            nv, c = _walk_replace(item, old, new)
            out.append(nv)
            total += c
        return out, total
    if isinstance(node, dict):
        total = 0
        out = {}
        for k, v in node.items():
            nv, c = _walk_replace(v, old, new)
            out[k] = nv
            total += c
        return out, total
    return node, 0


def apply_source(src):
    src = copy.deepcopy(src)
    for row in [r for r in ROWS if r["layer"] == "source"]:
        rid = row["id"]
        field = row["field"]
        routes = row["routes"]
        lesson_slug = row["lesson"]
        if True:
            rec = src.get(lesson_slug)
            if rec is None:
                raise RulingError(
                    "ks4_science_rulings %s: no source record for lesson %r "
                    "in the generated dict." % (rid, lesson_slug))
            if field != "quiz":
                # canonical single-value field (rp / key_note / examiner_tip /
                # common_mistake) — one shared value for the whole lesson,
                # taken from the Triple Higher record by build_source_record.
                old, new = row["old"], row["new"]
                cur = rec.get(field)
                if cur is None or old not in cur:
                    raise RulingError(
                        "ks4_science_rulings %s: expected to find the fixed "
                        "string in %s.%s, but it is not there.\n  looking "
                        "for: %r" % (rid, lesson_slug, field, old[:200]))
                n = cur.count(old)
                if n != 1:
                    raise RulingError(
                        "ks4_science_rulings %s: expected exactly 1 "
                        "occurrence in %s.%s, found %d."
                        % (rid, lesson_slug, field, n))
                rec[field] = cur.replace(old, new, 1)
                _FIRED.append(rid)
                continue

            quiz = rec.get("quiz", {})
            op = row.get("op", "edit")
            if op == "drop_item":
                stems = row["stems"]
                for route in routes:
                    items = quiz.get(route)
                    if items is None:
                        raise RulingError(
                            "ks4_science_rulings %s: route %r has no quiz "
                            "copy for %r." % (rid, route, lesson_slug))
                    before = len(items)
                    kept = [it for it in items if it.get("q") not in stems]
                    removed = before - len(kept)
                    if removed != len(stems):
                        raise RulingError(
                            "ks4_science_rulings %s: expected to drop %d "
                            "item(s) from %s/%s, actually dropped %d. "
                            "Design's delivery moved." %
                            (rid, len(stems), lesson_slug, route, removed))
                    quiz[route] = kept
                _FIRED.append(rid)
            else:  # edit
                old, new = row["old"], row["new"]
                for route in routes:
                    items = quiz.get(route)
                    if items is None:
                        raise RulingError(
                            "ks4_science_rulings %s: route %r has no quiz "
                            "copy for %r." % (rid, route, lesson_slug))
                    new_items, n = _walk_replace(items, old, new)
                    if n != 1:
                        raise RulingError(
                            "ks4_science_rulings %s: expected exactly 1 "
                            "occurrence of the fixed string in %s/%s's quiz, "
                            "found %d.\n  looking for: %r"
                            % (rid, lesson_slug, route, n, old[:200]))
                    quiz[route] = new_items
                _FIRED.append(rid)
            rec["quiz"] = quiz
    return src


# ═══════════════════════════════════════════════════════════════════════
# expect_present(layer, name, text) — the post-build proof. Every `new`
# for this (layer, name) target must be present; every `old` must be
# absent (skip_apply rows are exempt from the second half, since this
# file never removes their `old` text itself).
# ═══════════════════════════════════════════════════════════════════════
def expect_present(layer, name, text):
    """For layer in ('template', 'logic', 'asset', 'docs'), `text` is the
    plain page/asset text and `name` is the lesson slug (or asset/docs
    filename). For layer == 'source', pass the lesson's RECORD DICT itself
    (the value `apply_source()` produced at `src[lesson_slug]`, i.e. a dict
    with a `"quiz"` sub-dict keyed by route) as `text`, and `name` as the
    lesson slug — route-scoping matters here (a stem dropped from CF's quiz
    can legitimately still be present in TF's), which a flat string check
    cannot express."""
    problems = []
    is_source_dict = isinstance(text, dict)
    for row in rows_for(layer, name):
        rid = row["id"]
        if row.get("skip_apply"):
            # Not applied by this file at all (e.g. series-parallel-circuits-C1,
            # which mirrors ks4_rulings.R6) — nothing to assert either way.
            continue
        if is_source_dict:
            quiz = text.get("quiz", {})
            if row.get("op") == "drop_item":
                for route in row["routes"]:
                    items = quiz.get(route, [])
                    for stem in row["stems"]:
                        if any(it.get("q") == stem for it in items):
                            problems.append(
                                "%s: dropped stem still present on %s: %r"
                                % (rid, route, stem[:60]))
            elif row["field"] == "quiz":
                for route in row["routes"]:
                    items = quiz.get(route, [])
                    _, n_new = _walk_replace(items, row["new"], row["new"])
                    if not n_new:
                        problems.append("%s: new text not found on %s"
                                         % (rid, route))
                    if not row.get("old_survives"):
                        _, n_old = _walk_replace(items, row["old"], row["old"])
                        if n_old:
                            problems.append("%s: old text still present on %s"
                                             % (rid, route))
            else:
                cur = text.get(row["field"], "") or ""
                if row["new"] not in cur:
                    problems.append("%s: new text not found in %s"
                                     % (rid, row["field"]))
                if not row.get("old_survives") and row["old"] in cur:
                    problems.append("%s: old text still present in %s"
                                     % (rid, row["field"]))
            continue
        if row["new"] and row["new"] not in text:
            problems.append("%s: new text not found" % rid)
        # `old_survives`: rows whose `new` text legitimately CONTAINS the old
        # text as a substring (e.g. new = "<inserted code> " + old) — old
        # being present is correct, not a sign the ruling failed to fire.
        if not row.get("old_survives") and row["old"] and row["old"] in text:
            problems.append("%s: old text still present" % rid)
    if problems:
        raise RulingError(
            "ks4_science_rulings expect_present(%s, %s): %s"
            % (layer, name, "; ".join(problems)))
    return True


# ═══════════════════════════════════════════════════════════════════════
# --check : verify every row against Design's own delivery, with NO build.
# ═══════════════════════════════════════════════════════════════════════
def _split(path):
    src = open(path, encoding="utf-8").read()
    a = src.index("<helmet")
    m = re.search(r'<script[^>]*data-dc-script[^>]*>', src)
    if not m:
        raise SystemExit("ks4_science_rulings --check: %s has no <script data-dc-script>" % path)
    tpl = src[a:m.start()]
    logic = src[m.end():]
    logic = logic[:logic.rindex("</script>")]
    return tpl, logic


def _load_generated_source():
    """Reimplements build_ks4.load_subtopics_by_route() + build_source_record()
    minimally, so --check can run without importing build_ks4.py itself
    (which has side effects — it launches headless Chrome). Mirrors
    build_ks4.py's SOURCE_MODULES / SOURCE_ATTR / NONQUIZ_FIELDS exactly;
    if that shape changes, update both."""
    import importlib
    SOURCE_MODULES = {
        "chemistry": {"CF": "all_subtopics_chemistry",
                      "CH": "all_subtopics_chemistry_higher",
                      "TF": "all_subtopics_chemistry_triple_foundation",
                      "TH": "all_subtopics_chemistry_triple_higher"},
        "physics": {"CF": "all_subtopics_physics",
                    "CH": "all_subtopics_physics_higher",
                    "TF": "all_subtopics_physics_triple_foundation",
                    "TH": "all_subtopics_physics_triple_higher"},
    }
    SOURCE_ATTR = {"chemistry": "CHEMISTRY_SUBTOPICS_ALL", "physics": "PHYSICS_SUBTOPICS_ALL"}
    NONQUIZ_FIELDS = ["summary", "theory", "common_mistake", "examiner_tip",
                       "key_note", "matching", "fifas", "equations", "rp",
                       "variables", "higher"]
    data = {}
    for subject, routes in SOURCE_MODULES.items():
        data[subject] = {}
        for route, modname in routes.items():
            mod = importlib.import_module(modname)
            data[subject][route] = getattr(mod, SOURCE_ATTR[subject])

    def find_subtopic(subject, route, topic_id, slug):
        lst = data[subject][route].get(topic_id, [])
        return next((s for s in lst if s["id"] == slug), None)

    per_slug = {}
    for slug, lesson in LESSONS_BY_SLUG.items():
        subject, topic = lesson["subject"], lesson["topic_id"]
        canon = find_subtopic(subject, "TH", topic, slug)
        if canon is None:
            continue
        rec = {f: canon[f] for f in NONQUIZ_FIELDS if canon.get(f)}
        quiz = {}
        for route in lesson["routes"]:
            st = find_subtopic(subject, route, topic, slug)
            if st and st.get("quiz"):
                quiz[route] = st["quiz"]
        rec["quiz"] = quiz
        per_slug[slug] = rec
    return per_slug


def _selfcheck_mirrors():
    """Every row with `skip_apply=True` mirrors a ruling that already lives
    in `ks4_rulings.py`; this proves the two copies of the text still agree
    (the engine lane owns the real one). Returns a list of result lines."""
    out = []
    try:
        import ks4_rulings as _KR
    except Exception:
        return ["SKIP <mirrors> ks4_rulings.py not importable (engine lane mid-edit?)"]
    checks = [
        ("series-parallel-circuits-C1", "R6", "R6_FROM", "R6_TO"),
        ("metals-alloys-C8", "R8", "R8_FROM", "R8_TO"),
    ]
    for rid, rname, from_attr, to_attr in checks:
        row = row_by_id(rid)
        try:
            engine_from = getattr(_KR, from_attr)
            engine_to = getattr(_KR, to_attr)
        except AttributeError:
            out.append("MISS <mirror-%s> ks4_rulings.%s no longer exists — "
                       "update %s's skip_apply note" % (rname, from_attr, rid))
            continue
        if row["old"] != engine_from or row["new"] != engine_to:
            out.append("MISS <mirror-%s> %s's mirrored text no longer matches "
                       "ks4_rulings.%s_FROM/%s_TO — update the copy in this "
                       "file" % (rname, rid, rname, rname))
        else:
            out.append("OK <mirror-%s>" % rname)
    return out


def run_check():
    lines = []
    ok = 0
    miss = 0

    if ks4_lessons is None:
        lines.append("MISS <import> ks4_lessons.py not importable")
        miss += 1

    # template / logic / docs rows — verify against the actual Design file.
    for lesson_slug in sorted(set(r["lesson"] for r in ROWS if r["layer"] in ("template", "logic"))):
        design_file = design_file_for(lesson_slug)
        path = os.path.join(DESIGN_DIR, design_file)
        try:
            tpl, logic = _split(path)
        except Exception as e:
            for row in rows_for("template", lesson_slug) + rows_for("logic", lesson_slug):
                lines.append("MISS <%s> could not split %s: %s" % (row["id"], design_file, e))
                miss += 1
            continue
        for layer, text in (("template", tpl), ("logic", logic)):
            for row in rows_for(layer, lesson_slug):
                old = row["old"]
                n = text.count(old)
                if n == 1:
                    lines.append("OK <%s>" % row["id"])
                    ok += 1
                else:
                    lines.append("MISS <%s> expected 1 occurrence of old in "
                                  "%s (%s), found %d" % (row["id"], design_file, layer, n))
                    miss += 1

    # asset rows
    for asset_name in sorted(set(r.get("file") for r in ROWS if r["layer"] == "asset")):
        path = os.path.join(DESIGN_DIR, asset_name)
        try:
            text = open(path, encoding="utf-8").read()
        except Exception as e:
            for row in [r for r in ROWS if r["layer"] == "asset" and r.get("file") == asset_name]:
                lines.append("MISS <%s> could not read %s: %s" % (row["id"], asset_name, e))
                miss += 1
            continue
        for row in [r for r in ROWS if r["layer"] == "asset" and r.get("file") == asset_name]:
            n = text.count(row["old"])
            if n == 1:
                lines.append("OK <%s>" % row["id"])
                ok += 1
            else:
                lines.append("MISS <%s> expected 1 occurrence of old in %s, found %d"
                              % (row["id"], asset_name, n))
                miss += 1

    # docs rows — record only
    for row in [r for r in ROWS if r["layer"] == "docs"]:
        path = os.path.join(DESIGN_DIR, row["file"])
        try:
            text = open(path, encoding="utf-8").read()
        except Exception as e:
            lines.append("MISS <%s> could not read %s: %s" % (row["id"], row["file"], e))
            miss += 1
            continue
        n = text.count(row["old"])
        if n == 1:
            lines.append("OK <%s> (docs — record only)" % row["id"])
            ok += 1
        else:
            lines.append("MISS <%s> expected 1 occurrence in %s, found %d"
                          % (row["id"], row["file"], n))
            miss += 1

    # source rows
    try:
        src = _load_generated_source()
    except Exception as e:
        for row in [r for r in ROWS if r["layer"] == "source"]:
            lines.append("MISS <%s> could not build generated source: %s" % (row["id"], e))
            miss += 1
        src = None

    if src is not None:
        for row in [r for r in ROWS if r["layer"] == "source"]:
            rid = row["id"]
            rec = src.get(row["lesson"])
            if rec is None:
                lines.append("MISS <%s> no generated record for %r" % (rid, row["lesson"]))
                miss += 1
                continue
            field = row["field"]
            if field != "quiz":
                cur = rec.get(field, "")
                n = cur.count(row["old"])
                if n == 1:
                    lines.append("OK <%s>" % rid)
                    ok += 1
                else:
                    lines.append("MISS <%s> expected 1 occurrence in %s.%s, found %d"
                                  % (rid, row["lesson"], field, n))
                    miss += 1
                continue
            quiz = rec.get("quiz", {})
            op = row.get("op", "edit")
            row_ok = True
            for route in row["routes"]:
                items = quiz.get(route)
                if items is None:
                    lines.append("MISS <%s> route %s has no quiz copy for %s"
                                  % (rid, route, row["lesson"]))
                    row_ok = False
                    continue
                if op == "drop_item":
                    present = [it.get("q") for it in items if it.get("q") in row["stems"]]
                    if len(present) != len(row["stems"]):
                        lines.append("MISS <%s> route %s: expected to find %d "
                                      "stem(s), found %d" % (rid, route, len(row["stems"]), len(present)))
                        row_ok = False
                else:
                    _, n = _walk_replace(items, row["old"], "")
                    if n != 1:
                        lines.append("MISS <%s> route %s: expected 1 occurrence, found %d"
                                      % (rid, route, n))
                        row_ok = False
            if row_ok:
                lines.append("OK <%s>" % rid)
                ok += 1
            else:
                miss += 1

    mirror_lines = _selfcheck_mirrors()
    lines.extend(mirror_lines)
    miss += sum(1 for l in mirror_lines if l.startswith("MISS"))

    for l in lines:
        print(l)
    print("\n%d OK, %d MISS (of %d rows + %d mirror self-checks)"
          % (ok, miss, len(ROWS), len(mirror_lines)))
    return miss == 0


if __name__ == "__main__":
    import sys
    if "--check" in sys.argv:
        ok = run_check()
        sys.exit(0 if ok else 1)
    print("usage: python3 ks4_science_rulings.py --check")
