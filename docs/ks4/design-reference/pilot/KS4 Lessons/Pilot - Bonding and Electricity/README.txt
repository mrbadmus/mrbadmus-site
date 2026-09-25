KS4 pilot — Bonding (AQA Chemistry 5.2) + two electricity lessons (AQA Physics 6.2)
===================================================================================

Each lesson is one standalone page. Open any .dc.html directly in a browser;
nothing is installed and nothing is fetched from the network. support.js is the
runtime, _ds/ holds the design-system files, and the ks4-* files are shared by
every lesson:

  ks4-source.js     the checked science, extracted verbatim by script from
                    04-checked-science-source (every quiz copy, tip, FIFA, equation)
  ks4-lib.js        business logic only: route flags, verbatim quiz lookup, CFIFA
                    assembly, progress rail, best-score storage
  ks4-diagrams.js   the house figure style (cream #F3F0E7, sage labels, Georgia,
                    teal arrows) and the AQA circuit-symbol engine
  ks4-theme.css     dark-mode token remap (tokens only)
  Ks4*.dc.html      the shared blocks: Chrome, Choice, Sort, Chain, Write, Cfifa,
                    Ladder, KeyNote, QuizBank, End

src/ keeps a copy of the fourteen source files ks4-source.js was built from.

Every page has a Route selector in its header (Combined/Triple x
Foundation/Higher) so each route's rendering can be reviewed from one file.

Lessons, in unit order
----------------------
                                                         family          Higher  Triple
ks4-chemistry-5.2.1.1-chemical-bonds.dc.html              Classify          -       -
ks4-chemistry-5.2.1.2-ionic-bonding.dc.html               Process           -       -
ks4-chemistry-5.2.1.3-ionic-compounds.dc.html             Model             -       -
ks4-chemistry-5.2.1.4-covalent-bonding.dc.html            Process           -       -
ks4-chemistry-5.2.1.5-metallic-bonding.dc.html            Model             -       -
ks4-chemistry-5.2.2.1-states-of-matter.dc.html            Investigation    yes      -
ks4-chemistry-5.2.2.3-properties-ionic-compounds.dc.html  Contrast          -       -
ks4-chemistry-5.2.2.4-properties-small-molecules.dc.html  Model             -       -
ks4-chemistry-5.2.2.5-polymers.dc.html                    Classify          -      yes
ks4-chemistry-5.2.2.6-giant-covalent-structures.dc.html   Contrast          -       -
ks4-chemistry-5.2.2.7-metals-alloys.dc.html               Contrast          -      yes
ks4-chemistry-5.2.3.3-nanoparticles.dc.html               Quantitative      -   whole lesson
ks4-physics-6.2.2-series-parallel-circuits.dc.html        System            -       -
ks4-physics-6.2.1.4-resistors-iv-required-practical.dc.html  Required practical  -   -

All eight families appear. Higher content: states of matter (limitations of the
particle model, 5.2.2.1 HT only). Triple content: polymers (addition
polymerisation 4.7.3.1; thermosoftening and thermosetting 4.10.4.3), metals and
alloys (alloys as useful materials 4.10.4.2), nanoparticles (4.2.4, the whole
lesson). No pilot statement is both HT and separate-science, so the
Higher · Triple badge is specified in NOTES but not drawn on any page.

Spec coverage
-------------
Chemistry 5.2.1.1–5.2.1.5, 5.2.2.1–5.2.2.8, 5.2.3.1–5.2.3.3 and separate-science
4.2.4.1–4.2.4.2. Physics 6.2.1.4 (with the I–V characteristics required
practical) and 6.2.2. 5.2.2.2 (state symbols) sits inside states of matter and
5.2.2.8 (metals as conductors) inside metals and alloys, because the pilot has
no separate slots for them. 5.2.3.1–5.2.3.3 (diamond, graphite, graphene and
fullerenes) sit inside giant covalent structures, all untagged: they are core.

NOTES-KS4-pilot.md is the delivery record: blocks and template decisions for
Code, instrument configs, route-tag sources, and numbered science flags.

Draft — not yet science-reviewed. Every page says so on its face.

Packaged 24 Sep 2026.

Ks4Video.dc.html — optional lesson video slot (poster, captions, transcript). Fill KS4.VIDEOS in ks4-lib.js; empty = hidden.
Equation-sheet links: KS4.EQ_BY_YEAR / EQ_YEAR in ks4-lib.js — update each summer.
