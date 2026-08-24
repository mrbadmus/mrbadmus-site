MrBadmusAI — KS3 Physics
P2: Energy at home — five lessons, complete unit

Open any .dc.html file directly in a browser. No connection needed.

  p2-01-energy-in-food.dc.html                  Energy in food                  QUANTITATIVE
  p2-02-power-ratings-in-watts.dc.html           Power ratings in watts          QUANTITATIVE
  p2-03-calculating-energy-transferred.dc.html   Calculating energy transferred  QUANTITATIVE
  p2-04-reading-a-fuel-bill.dc.html              Reading a fuel bill             QUANTITATIVE
  p2-05-fuels-and-energy-resources.dc.html       Fuels and energy resources      CLASSIFY

Keep the folder structure intact: each lesson loads support.js and the
design-system stylesheets and fonts from _ds/ alongside it.

Read NOTES-P2.md before reviewing. Two items need Mide's ruling:
  - ENERGY-12, ENERGY-13, ENERGY-14 are cited here; all draft.
  - p2-04 uses the balance beam for the bill total (a sum of products) and
    the triangle for a single row. Same precedent as c2-06 and p1-03.

p2-01 is the OWNER of energy-in-food (structure.py §4.6). Biology B3's
a-balanced-diet references this lesson and must not duplicate it.

Standing conventions, same as B1, P3, B2, C2, C1 and P1:
  - Progress rail ticks only on completed activities, right or wrong.
  - One KEY FACT box per lesson. Amber is reserved for misconceptions.
  - Only the mastery ladder marks correctness.
  - No year or half-term appears anywhere in a lesson page.

Packaged 21 Aug 2026.

Changed 23 Aug 2026 — CFIFA and the structural conventions
----------------------------------------------------------
p2-01 and p2-03 rebuilt on the five-step block. p2-02 and p2-04 were
declared QUANTITATIVE and had no worked example at all; both now have one.
All five lessons gained a [data-key-fact] block and a second misconception
quote. Rails cut to four stops throughout.

Worked examples in this unit now run CFIFA: Convert, Formula, Insert,
Fine-tune, Answer, revealed one step at a time, with two worked examples
(one where nothing needs converting, one where a quantity arrives in the
wrong size) and two write-it-out student attempts labelled only Question 1
and Question 2. The block itself is Cfifa.dc.html, sitting beside the
lessons in this folder — one implementation, mounted by every lesson that
needs it.

Every lesson carries four rail stops, one [data-key-fact] block and two
misconception quotes.

The full record is in PHYSICS-AUDIT-2026-08-23.md.
