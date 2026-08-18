"""B7 — Photosynthesis. Four lessons, Biology.

The thin unit wrapper. The lesson records live one per module under
`ks3_data/b7/`, authored against Claude Design's approved reference screens in
`docs/ks3/design-reference/b7/` under the MRB-220 build contract, and against the payload
schema written before dispatch at `docs/ks3/b7-inventory/PAYLOAD-SCHEMA.md`.

**Statutory coverage: all three PHOT statements, three lessons, no split.**

    L1 the-photosynthesis-reaction          KS3.B.PHOT.01  + KS3.B.NUT.06
    L2 leaves-built-for-the-job             KS3.B.PHOT.03
    L3 testing-a-leaf-for-starch            KS3.WS.EXP.03 / .04  (no subject statement)
    L4 why-almost-all-life-depends-on-it    KS3.B.PHOT.02

Nothing needed splitting: PHOT's three bullets map one-to-one onto three
lessons. `B.NUT.06` — carbohydrates made in leaves, minerals and water from the
soil — is covered by b7-01's van Helmont treatment, which is the only place in
the key stage where a student is shown that the soil is not the food.

**L3 deliberately claims no subject statement.** It is the practical the other
three are argued from, which is why it sits third rather than second. Its
`covers` is anchored on `KS3.WS.*` per §5.7.1, as every INVESTIGATION lesson
does; §10.2 requires `covers` to be non-empty, and WS ids are exempt from the
exactly-once ownership check. All three PHOT statements therefore stay with
L1/L2/L4 and nothing is claimed twice.

**⊕ REVERSED 18 Aug 2026 (MRB-249): four rail stops per page, all four tick.**
This note used to say three could tick and that the fourth was dropped. On every
page one stop is anchored to a static card section whose completion predicate is
Design's own, stated a second time for the instrument beside it — a MIRROR, not
a copy. All four stops are declared, `mirrors` names the section each borrows
from, and `wireRail`'s `paint()` resolves them at rail level instead of hunting
for DOM signals inside the section. Anchors are unchanged, so hash links and
`elicited_by` values resolve exactly as before. Full treatment, including the
`#s-tuner` renderer hazard, in `ks3_data/b7/__init__.py`.

**⚑ Three science corrections were made to approved pages, and they are Mide's
to confirm** (§5.10 — he is the sole science gate):

1. *b7-04, job three.* Design wrote "Photosynthesis is the only large-scale
   process that removes it" and "the one route out of the atmosphere". False as
   written: ocean dissolution is a physical sink comparable to the whole land
   biosphere, and silicate weathering is the geological one. The card also
   contradicted itself, already naming *ocean sediment* as a destination.
   Narrowed to "the only large-scale **biological** process" and "the **living
   world's** one route out". The teaching point is unchanged.
2. *b7-03, Going further.* "would draw water in by osmosis until it burst" — a
   walled plant cell does not burst, and `b1-03` teaches the opposite three
   times on a live page. Now "would pull water in after it and swell hard
   against its wall", which sharpens the closing glycogen parallel rather than
   weakening it: the animal cell is the one with no wall.
3. *b7-03, Going further.* "osmosis" named twice. KS3 does not name it — zero
   student-facing uses anywhere in `ks3_data/`, and `b4-05` teaches guard cells
   going turgid without it. NOTES-B7 flag 15 asked exactly this and the answer
   was yes. The idea is kept; only the untaught label goes.

**⚑ Also corrected across the unit: build-internal lesson codes in student
prose.** Design's pages print `b4-05` and similar into teaching copy. A student
cannot resolve a slot code, and §8.10 bars platform self-explanation. Ruled once
for the unit (MRB-245) and resolved to the lesson TITLE everywhere it occurred;
destinations are carried as real `references` edges instead. b7-03's two inline
links additionally pointed at the delivery deck's flat filenames, which the
built site does not serve — carrying them would have shipped 404s inside
teaching prose.

**⚠️ b7-03's safety wording is the most load-bearing copy in the unit** and is
lifted whole — key note, method card 3, the legal line, rung 3's criterion, and
the `method-breaker`'s flame branch. This is the one lesson in the build where a
student could read the page as permission to do something. NOTES-B7 flag 14 and
MRB-233: it needs the person who signs the risk assessments, not only the
examiner gate. Nothing in it was paraphrased, softened or merged.

**Four marked rungs were length tells as Design drew them** — b7-01 rung 2,
b7-02 rung 2, b7-03 rung 2 (the widest in the unit, 17 words against 5/5/6) and
both of b7-04's. Under MRB-177, ruled 17 Aug 2026, their distractors were
rewritten as wrong RULES in the correct answer's own shape. Every correct
option, every `answer` index and every one of Design's corrections is unchanged
and byte-identical — which is the test of whether a rewrite moved what the
question measures. Those distractors are ours, not Design's, and go to Mide's
gate as new science-bearing copy.

**`figures: []` on all four, measured not assumed.** No page draws an image or a
placeholder. NOTES-B7 flag 12's leaf cross-section is not in the diagram
manifest and is not invented here. See `ks3_data/b7/__init__.py`.

**review_state is `draft` on every lesson.** Mide is the sole science gate
(§5.10); `draft` → `examiner-reviewed` → `frozen`. Since MRB-221 the field no
longer gates publishing and no page carries a review marker — it records review
position, nothing more.
"""

from .b7 import lessons as _b7_lessons

UNIT = {
    "code":            "B7",
    "slug":            "photosynthesis",
    "title":           "Photosynthesis",
    "discipline":      "biology",
    "statutory_area":  "Material cycles and energy",
    "split_rationale": None,
    "intro":           "A tree weighing tonnes was built almost entirely out of "
                       "a gas you cannot see, and a small amount of water. This "
                       "unit is about the reaction that does it, the leaf built "
                       "to run it, and why almost everything alive depends on "
                       "something else having run it first.",
    "lessons": _b7_lessons(),
}
