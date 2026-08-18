"""B8 — Respiration. Five lessons, Biology.

The thin unit wrapper. The lesson records live one per module under
`ks3_data/b8/`, authored against Claude Design's approved reference screens in
`docs/ks3/design-reference/b8/` under the MRB-220 build contract, and against the payload
schema written before dispatch at `docs/ks3/b8-inventory/PAYLOAD-SCHEMA.md`.

    L1 aerobic-respiration                 mass-ledger
    L2 why-every-cell-respires             cell-demand
    L3 anaerobic-respiration-in-humans     oxygen-debt
    L4 fermentation                        fermenter
    L5 aerobic-vs-anaerobic                route-decider

**Slugs match `ks3_data/structure.py` character for character.** They are the
join for scheme-of-work rows, progress records and every `requires` edge, and
they are permanent (§8.4).

**⊕ REVERSED 18 Aug 2026 (MRB-249): four rail stops per page, all four tick.**
This note used to say three could tick and that the fourth was dropped. On every
page one stop is anchored to the BAND section, which renders as a static
`ks3-rule` and carries none of the five DOM signals `doneByDom()` reads —
because Design's `isDone()` completes it on the instrument's predicate instead.
All four stops are declared, `mirrors` names the section each borrows from, and
the tick is resolved at rail level. Anchors are unchanged, so hash links and
`elicited_by` / `confronted_by` values resolve exactly as before. Full treatment
in `ks3_data/b8/__init__.py`.

**⚑ One science correction was made to an approved page, and it is Mide's to
confirm** (§5.10 — he is the sole science gate):

*b8-04, the fermenter's product panel.* Design computes which product list to
show with `aerobic = out.line.indexOf('oxygen') >= 0` — a string sniff on the
reaction text. It is wrong on one live branch. Yoghurt bacteria in an **open,
stirred** vessel take `line = "contaminated"`, which contains no `"oxygen"`, so
the sniff falls through to the anaerobic bacteria list and the bench prints
**"Lactic acid 100 units"** underneath its own heading *"Poor conditions for
these bacteria"*. An aerobic branch produces no lactic acid: lactic acid is
what the fermentation route makes, and that route is the one that runs when
oxygen is absent. The panel contradicts itself and it contradicts the science.

Fixed structurally rather than by patching the sniff: `products` is **authored
per branch** and is never derived from `line`, so the branch reports what
aerobic conditions actually produce. `r_fermenter` refuses a branch with no
`products`, and refuses any oxygen-open branch that declares a fermentation
product with a positive value — so the defect cannot be re-introduced by a
later edit. This is contract §1 (MRB-205, *page wins over engine*) yielding to
fact: where an approved page contradicts a matter of fact, the fact wins.

**⚖️ The yeast open-and-stirred branch is NOT a failure state**, and the
renderer does not style it as one. It is how yeast is manufactured — the branch
text says so in its own words — and it is the branch that teaches why a brewer
seals the vessel. Its rate is 100 and its tone is not amber. NOTES-B8 flag 16
asks Mide to confirm the claim; confirming or softening the science does not
make it a failure.

**⚖️ b8-03's breathing bar is driven by LACTATE, not by pace**, and that is the
entire teaching point of the lesson. Design's own line, measured off the page:
`breathing = min(100, round(20 + supply × 0.6 + lactate × 0.5))`. Neither
`pace` nor `demand` appears in it. When the runner stops, the demand bar
collapses from 150 to 25 and the breathing bar stays at 90%. A breathing bar
that fell when the runner stopped would teach the opposite of the lesson.

**⚖️ b8-01's energy figure sits OUTSIDE both mass totals, on purpose.** It is
the visual form of the argument that energy is not a substance, and rung 2 and
the second `#s-think` paragraph both depend on the student having seen it there.
The ledger balances exactly at all four amounts by construction — per gram of
glucose both sides come to 2.0667 — and `r_mass_ledger` asserts that before it
draws anything. 15.6 kJ per gram is NOTES-B8 flag 2 and stays on Mide's gate.

**`figures: []` on all five, measured not assumed.** No page draws an image or
a placeholder. NOTES-B8 flag 21's mitochondrion and gas-flow diagram are not in
`docs/ks3/diagram-manifest.md` and are not invented here.

**The `RESP` misconception family is opened by this unit** — `RESP-01`..`10`,
two per lesson, in `docs/ks3/misconception-register.md`. NOTES-B8 §5 claims they
were already written there; they were not. Third delivery in a row to describe
register work as done when it was not.

**review_state is `draft` on every lesson.** Mide is the sole science gate
(§5.10); `draft` → `examiner-reviewed` → `frozen`. Since MRB-221 the field no
longer gates publishing and no page carries a review marker — it records review
position, nothing more.
"""

from .b8 import lessons as _b8_lessons

UNIT = {
    "code":            "B8",
    "slug":            "respiration",
    "title":           "Respiration",
    "discipline":      "biology",
    "statutory_area":  "Material cycles and energy",
    "split_rationale": None,
    "intro":           "Every cell you own is running the same reaction right "
                       "now, and has not stopped since you were an embryo. "
                       "This unit is about what that reaction takes in, what it "
                       "gives out, what happens when the oxygen runs short, and "
                       "why a brewery and a yoghurt factory are both built "
                       "around it.",
    "lessons": _b8_lessons(),
}
