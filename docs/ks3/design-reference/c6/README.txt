MrBadmusAI — KS3 Chemistry
C6: Acids and alkalis — seven lessons, complete unit

Open any .dc.html file directly in a browser. No connection needed.

  c6-01-acids-and-alkalis.dc.html             Acids and alkalis            CLASSIFY
  c6-02-indicators-and-the-ph-scale.dc.html   The pH scale and indicators  MODEL
  c6-03-neutralisation.dc.html                Neutralisation               PROCESS
  c6-04-acids-and-metals.dc.html              Acid + metal                 PROCESS
  c6-05-acids-and-carbonates.dc.html          Acid + carbonate             PROCESS
  c6-06-making-a-salt.dc.html                 Making a pure dry salt       INVESTIGATION
  c6-07-catalysts.dc.html                     Catalysts                    MODEL

Keep the folder structure intact: each lesson loads support.js and the
design-system stylesheets and fonts from _ds/ alongside it.

Read NOTES-C6.md before reviewing. Two things need a ruling:
  - lesson 05 is acid + carbonate, where §7 specifies acid + alkali (§2)
  - the ACID misconception family needs its prefix approving (§6)

Covers KS3.C.CR.04 to CR.08. All five statements owned by C6 are addressed.

Standing conventions, same as B1, P3, B2 and C1-C5:
  - Progress rail ticks only on completed activities, right or wrong.
  - One KEY FACT box per lesson. Amber is reserved for misconceptions.
  - Only the mastery ladder marks correctness.
  - No year or half-term appears anywhere in a lesson page.

Packaged 21 Aug 2026 — this folder is the current build.
Every .dc.html here is byte-identical to the working copy it was authored from,
and the _ds/ assets are the same files those working copies load.

Checked before packaging: no U+2192, U+2713, U+2715 or U+2126 anywhere in a
lesson, and no Unicode subscript or superscript digits — formulae use real
<sub> elements in markup and plain digits inside instrument payloads.
Changed in this pass: the word equations in c6-03, c6-04 and c6-05 now draw
their arrow as inline SVG, and ion notation in c6-01 and c6-03 uses <sup>.
See the change log in NOTES-C6.md.
