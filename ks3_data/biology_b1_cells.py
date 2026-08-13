"""B1 — Cells and organisation. Six lessons, Year 7 Biology.

⊖ **Authored as eight; six survive.** `stem-cells-and-meristems` and
`enzymes-and-rate` were removed on 2026-08-12 under MRB-199, ruled by Mide as
examiner: neither owned a statutory statement. The catalyst clause enzymes would
have carried, `KS3.B.NUT.04`, is already owned by B3's `enzymes-in-digestion`
slot, so the slot was dropped outright rather than moved — two lessons competing
for one ownable statement is the defect MRB-199 exists to close. Enzyme *rate*
(optimum temperature, denaturing, the shape of the curve) has no KS3 statutory
home at all and belongs in §7.6's Year 9 bridge unit when that is built.

⊖⊖ **Round one's authoring is superseded in full, 13 Aug 2026 (MRB-205).**

This file used to carry six lesson records inline, ~2,300 lines of them. It
carries none now: the records live one per module under `ks3_data/b1/` and this
file is the unit wrapper that collects them.

The reason is not tidiness. Mide ruled on 11 August that **Design plans every
KS3 lesson in full and draws its screens, and Code renders to them and never
invents a shape**, and then rejected the built B1 pages by name. The inventory
run that followed measured Design's six approved pages against what this file
produced, in a real browser, and the sharpest result was b1-04 — the SYSTEM
reference screen, 32 lesson slots behind it:

    "they are not the same lesson. Design teaches 'the same seven parts,
     tuned' across four cells with a sabotage engine. The generator teaches
     DIFFUSION, with a chemistry-borrowed sim and a system-parts graph. 11
     blocks against 20. No shared sequence, big question, hook, misconception,
     ladder or key note. Every block shell is pixel-identical and everything
     the page owns is a different document — which is precisely how a build
     passes every gate while looking nothing like what was designed."

So the content was not edited towards the approved pages; it was re-authored
from them, byte-identical where Design wrote a string, with `tools/
extract_design_payload.js` lifting each page's authored constants rather than
anyone retyping ~12,000 words of science-bearing copy that all crosses the
examiner gate.

**Round one's bodies survive in git history**, on `design/b1-content` and in
this file's own history — which is where MRB-199's ledger and MRB-211's note
about keeping the superseded authoring reachable both expect to find them.
Nothing was lost; it stopped being what the site emits.
"""

from .b1 import lessons as _b1_lessons

UNIT = {
    "code":            "B1",
    "slug":            "cells-and-organisation",
    "title":           "Cells and organisation",
    "discipline":      "biology",
    "statutory_area":  "Structure and function of living organisms",
    "split_rationale": None,
    "intro":           "You are built from about thirty trillion cells, and not "
                       "one of them knows you exist. This unit starts by asking "
                       "what makes something alive at all, goes down to a single "
                       "cell, and comes back up to a whole organism.",
    "lessons": _b1_lessons(),
}
