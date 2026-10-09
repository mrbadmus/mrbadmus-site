# Batch 6 — science log

Every science decision made while porting Design's batch 6 (14 lessons), with its source. Design's lesson files stay
byte-identical on disk (`docs/ks4/design-reference/batch-6/`, `MD5SUMS`). Changes are NAMED rulings in
`ks4_batch_rulings.py` (`SCIENCE`), applied at compile time, each failing the build if its target text is not found
exactly once. "Pack" = `docs/ks4/packs/batch-6/`. Rulings were made by the lead (Prompt AB, 8 Oct 2026, audit by the
lead); the builder applied them verbatim, except that the two vacuole geometry strings were a starting point the
builder had to finalise (below).

## Rulings applied (eight science rulings in six lessons, plus port mechanics)

| id | lesson | layer | decision |
|---|---|---|---|
| B6-APC-VACUOLE-1 | animal-plant-cells | logic | Onion-cell figure: the vacuole is redrawn so it fills about three quarters of the cell, matching the estimation task's key ("most of it, about three quarters"). Was 92 x 58 in a 118 x 78 cell (58%, reads as about half). **Final: 95 x 70 at (x+17, y+4), rx 8.** |
| B6-APC-VACUOLE-2 | animal-plant-cells | logic | The nucleus sits against the cell wall and clear of the vacuole. **Final: circle r 6 at (x+8, y+39).** |
| B6-CM-HOOK | culturing-microorganisms | template | "Warmth speeds growth. For safety, school cultures are kept no warmer than 25" (was "…which is why school cultures are kept no warmer than 25"): 25 C is a safety limit, not because warmth speeds growth. |
| B6-DS-FOOD | digestive-system | logic | The food-test simulator's starch-only sample is "Cornflour", not "Bread" (bread contains protein, about 8 to 10%, and turns Biuret purple). |
| B6-TR-DIST | transpiration | logic | `dist(f)` no longer clamps at 4 mm. Now `16 + (f.t ? 6 : 0) + (f.l ? 6 : -6) + (f.h ? -6 : 0) + (f.w ? 8 : 0)`; range 4 to 36 mm on the 0 to 40 mm scale. Every toggle now moves the bubble in the direction the note names. |
| B6-TL-SINK | translocation | logic | Storage-root note: "…where the sugar is stored, for example in a carrot." (a potato is a stem tuber, not a root; a carrot stores mainly sugar). |
| B6-G1-LILAC-1 | group-1 | logic | Potassium note: "…The hydrogen ignites at once, and potassium colours the flame lilac." Lilac is potassium's flame colour, not hydrogen's. |
| B6-G1-LILAC-2 | group-1 | logic | Rung 4 mark-scheme point: "…potassium reacts very vigorously; the hydrogen ignites, and potassium colours the flame lilac." |
| B6-CM-CHIP, B6-FS-CHIP, B6-SE-CHIP | culturing-microorganisms, factors-affecting-food-security, stellar-evolution | logic | **Port mechanic, not science.** Each `renderVals` returns a fresh object instead of spreading the route helper, so the one route chip (B-R12) had no words or menu. Same repair as B4-IRB-CHIP / B5-RSBB-CHIP. |
| B6-PTR-MICRO-1/2, B6-PTR-ENZ-1/2 | animal-plant-cells, digestive-system | template + logic | **Port mechanic, not science.** Design's "in the Microscopy lesson" and "in the Enzymes lesson" (marked "Code to wire") become links to the live pages for the pupil's route. Her words are unchanged; no new words. |

Each applied exactly once (the build would have stopped otherwise).

### Vacuole geometry: final numbers and area working

The cell is the 118 x 78 rectangle (wall stroke 2). Vacuole 95 x 70 = 6,650.

- Against the full 118 x 78 = 9,204: **72.3%**.
- Against the cell's inside once the 2-wide wall is taken off, 116 x 76 = 8,816: **75.4%**.
- So the vacuole is 72 to 75% by either measure, inside the 72 to 76% target.

The lead's starting strings (104 x 66 at x+8, nucleus r 6 at x+9) gave 74.6% but the nucleus (x+3 to x+15) overlapped the
vacuole's left edge (x+8). Final: nucleus r 6 at (x+8, y+39) spans x+2 to x+14, 1 clear of the wall's inner edge;
vacuole from x+17 to x+112 is 3 clear of the nucleus and 6 clear of the right wall; y+4 to y+74. Checked in a 390 px
screenshot of the onion plate, viewed by the builder: large vacuole, nucleus a small dot against the wall, no overlap,
in every visible cell.

### Where each ruling is visible (390 px, after waiting for the redraw)

- VACUOLE-1/2: the onion-cell figure, all full cells (measured from the SVG: rect 95 x 70 at +17,+4; circle r 6 at +8,+39).
- CM-HOOK: culturing, pressing either opener card shows the bridge with the new sentence; the old sentence is absent.
- DS-FOOD: the food buttons read Cornflour, Glucose drink, Egg white, Olive oil; the test figure's label reads
  "Cornflour food tests". No other string names this sample bread: the only "bread" left on the page is the opener's
  toast scene ("does your body use the bread as it is…") and its reply, which are about toast being digested, not the sample.
- TR-DIST: all 16 toggle combinations (temperature, light, humidity, air movement) pressed; the note reads
  4, 10, 12, 16, 18, 22, 24, 28, 30 or 36 mm exactly as the formula gives, and every single-toggle step changes the
  number the right way (warm, bright, windy up; humid down). The old clamp's two still cases are gone.
- TL-SINK: "A storage root" button shows the new note; "starch in a carrot or potato" is gone.
- G1-LILAC-1: Lithium, Sodium, Potassium pressed in order; the potassium note shows the new wording.
- G1-LILAC-2: rung 4's "Show the mark scheme" lists the new point 3.

## DS-FOOD check: no other string calls the sample bread

`grep -i bread` over Design's digestive-system file finds four places: the opener's scene, question and bridge, its
reply, and `FOODS[0].label`. The first three are the toast hook; only the last is the simulator sample. Fixed.

## Kept as Design wrote them (lane rulings)

- **Group 1 boiling points: Li 1342, Na 883, K 759, Rb 688 C** kept (standard data, rung 2); all four present on the page.
- **4.4 Life cycle of a star hook** ("more massive stars burn faster and have shorter lives") kept as the reveal.
- **8.4 Stem cells: leukaemia and bone marrow transplant** kept as the adult-cell use.
- **9.2 Principles of organisation: no triangle for the size comparison** ("bigger divided by smaller" is a comparison by
  division, not an AQA equation). Design's file imports no Ks4Triangle; nothing added.
- **12.3 Cancer, bank question 1 wrong-answer 3** (mentions surgery and chemotherapy) kept; chemotherapy appears on the
  page only there.
- Design's other numbered flags (NOTES-KS4-batch-6.md) were resolved by Design in the delivery; none was reopened.

## Not done

- **Transpiration rate calculations pending from Design.** Her file has none (NOTES 13.3 says so and leaves it to Mide's
  call). Ported as it is; no calculation written.
- Translocation's hook and reply still say "the potato or carrot" (only the sink note was ruled).
- Superscripts in JS-built text stay plain Unicode in the system fallback font (Design's G1); subscripts are rendered
  by `ks4-ext-batch-6.js`.

## Frozen content

None of the 14 slugs is a frozen-correction slug (`docs/ks4/FROZEN-CORRECTIONS.md`); this branch touches no
`all_subtopics_*.py`. The batch is frozen after build (`ks4_lessons/frozen_batch-6.json`), `review_state`
`examiner-reviewed`, draft banner off, as batches 4 and 5.

## Fix from the independent pupil walk (lead, 9 Oct 2026)

| id | lesson | change | why |
|---|---|---|---|
| B6-G1-CAP | group-1 | Prediction feedback capitalises the start of its second sentence. Words unchanged. | "You predicted gentler. it is the other way." |
