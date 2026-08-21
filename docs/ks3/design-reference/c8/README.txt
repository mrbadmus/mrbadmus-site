MrBadmusAI — KS3 Chemistry
C8: The periodic table — six lessons, INCOMPLETE against the register

Open any .dc.html file directly in a browser. No connection needed.

  c8-01-metals-and-non-metals.dc.html                Metals and non-metals         CONTRAST
  c8-02-mendeleev-and-the-table-that-predicted.dc.html  Mendeleev and the table    INVESTIGATION
  c8-03-groups-and-periods.dc.html                   Groups and periods            MODEL
  c8-04-group-1-the-alkali-metals.dc.html            Group 1 — the alkali metals   PATTERN
  c8-05-group-7-the-halogens.dc.html                 Group 7 — the halogens        PATTERN
  c8-06-group-0-and-why-groups-exist.dc.html         Group 0 and why groups exist  APPLY

Keep the folder structure intact: each lesson loads support.js and the
design-system stylesheets and fonts from _ds/ alongside it.

READ NOTES-C8.md BEFORE REVIEWING. This unit does not match §7 and is not
finished:

  - KS3.C.PT.06 (metal and non-metal oxides, acidity) has NO lesson. It is the
    only uncovered statutory statement in C1-C8.
  - c8-06 links forward to c8-07-metal-and-non-metal-oxides.html, which does
    not exist. That is an intra-unit dead link, not a soft forward link.
  - §7 specifies five lessons with groups 1, 7 and 0 merged into one. This build
    has them as three. NOTES §2 sets out three options and a recommendation.
  - c8-02's archetype was corrected to INVESTIGATION to match §7, but the lesson
    body was written to the MODEL shape and still reads as one.

Standing conventions, same as B1, P3, B2 and C1-C7:
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
Changed in this pass: oxide formulae in c8-02 and c8-03 payloads, and the
word equation in c8-04. See the change log in NOTES-C8.md.
