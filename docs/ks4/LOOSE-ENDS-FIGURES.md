# Figures parked for a phone redraw (loose-ends run, 17 Oct 2026, fix 7a)

The phone text floor (ks4-runtime.js `figFit()` + `KS4_FIG_CSS`) gives every Design figure a minimum width so its smallest label draws at 11px or more at 390px wide, and the frame scrolls sideways. A figure that needs MORE THAN TWO columns of scroll is shipped like that for now, but is the wrong shape for a phone and is parked here to be **redrawn for phone** (fewer or larger labels, or a stacked layout), after which the scroll goes away on its own.

Measured by `tools/ks4_figure_text_audit.py` at 390px, DPR 1, column about 314px: the rendered figure width after the floor, against the column. Every TH page, plus all four routes of the 28 lessons whose figures differ by route. Sorted worst first.

| lesson | figure (alt text) | width needed | x column | viewBox | routes |
|---|---|---|---|---|---|
| strong-weak-acids | Two beakers at the same concentration: hydrochloric acid fully split into H⁺ and | 990 px | 3.2 | 720x305 | CH, TH |
| stellar-evolution | Life cycle of a star. Shared: nebula, protostar, main sequence. Sun-sized: red g | 914 px | 2.9 | 1080x320 | TH |
| structure-of-atom | Atom, not to scale: nucleus of 3 protons and 4 neutrons, with 2 electrons at ene | 880 px | 2.8 | 520x360 | TH |
| structure-of-atom | Atom, not to scale: nucleus of 2 protons and 4 neutrons, with 2 electrons at ene | 880 px | 2.8 | 520x360 | TH |
| structure-of-atom | Atom, not to scale: nucleus of 3 protons and 3 neutrons, with 2 electrons at ene | 880 px | 2.8 | 520x360 | TH |
| structure-of-atom | Atom, not to scale: nucleus of 3 protons and 4 neutrons, with 1 electrons at ene | 880 px | 2.8 | 520x360 | TH |
| uses-em-waves | The electromagnetic spectrum from radio waves to gamma rays with a use under eac | 807 px | 2.6 | 880x184 | CF, CH, TF, TH |
| electrolysis-principles | Electrolysis cell: d.c. supply, cathode (negative) on the left, anode (positive) | 770 px | 2.5 | 700x320 | TH |
| reactions-of-acids | Four reactions of acids: with a metal, salt and hydrogen (squeaky pop test); wit | 762 px | 2.4 | 900x380 | TH |
| chemical-measurements | Burette (scale running downwards), pipette (one fixed volume) and measuring cyli | 760 px | 2.4 | 760x356 | TH |
| salts-neutralisation | Five stations of the required practical: warm the acid, add excess copper oxide, | 760 px | 2.4 | 760x280 | TH |
| factors-affecting-food-security | Six threats to food security around a central label: Birth rate (More people to  | 733 px | 2.3 | 800x400 | TH |
| cancer | Stage 1. Benign: A cell starts dividing without control. Malignant: A cell start | 733 px | 2.3 | 800x320 | TH |
| nervous-system | Stimulus, receptor, sensory neurone, CNS, motor neurone, effector, response. | 715 px | 2.3 | 780x160 | TH |
| nervous-system | The pathway with one link broken; everything after it is lost. | 715 px | 2.3 | 780x160 | TH |
| electronic-structure | The first twenty elements arranged by group (outer electrons) and period (number | 682 px | 2.2 | 620x280 | TH |
| transition-metals | Colour strip: copper(II) blue, iron(II) green, iron(III) orange-brown, nickel(II | 678 px | 2.2 | 740x235 | TF, TH |
| uses-of-glucose | Glucose branching to five uses: respiration, starch, fats and oils, cellulose, a | 670 px | 2.1 | 670x340 | TH |
| transition-metals | Bars comparing iron and sodium: melting point 1538 against 98 °C, density 7.9 ag | 660 px | 2.1 | 720x260 | TF, TH |
| chemical-measurements | Three titres 24.10, 24.30 and 24.20 on a number line; the range bracket spans 0. | 660 px | 2.1 | 720x225 | TH |
| transpiration | Potometer: leafy shoot in a sealed tube; the air bubble in the capillary tube mo | 660 px | 2.1 | 660x330 | TH |
| human-reproduction-hormones | Levels of FSH, oestrogen, LH and progesterone over a 28-day cycle; LH peaks just | 568 px | 2.1 | 620x280 | CH, TH |
| ionic-compounds | One layer of a sodium chloride lattice, alternating sodium and chloride ions | 644 px | 2.1 | 820x480 | TH |
| ionic-compounds | One sodium ion with its six chloride neighbours: four in its own layer and one d | 644 px | 2.1 | 820x480 | TH |
| relative-atomic-mass | Nuclear symbol of sodium-23 (mass number 23 over atomic number 11) next to the p | 643 px | 2.0 | 760x260 | TH |
| electrolysis-molten | Crucible of molten lead bromide with cathode on the left and anode on the right; | 642 px | 2.0 | 700x320 | CF, CH, TF, TH |
| electrolysis-molten | Crucible of molten calcium chloride with cathode on the left and anode on the ri | 642 px | 2.0 | 700x320 | CF, CH, TF, TH |
| electrolysis-molten | Crucible of molten zinc chloride with cathode on the left and anode on the right | 642 px | 2.0 | 700x320 | CF, CH, TF, TH |
| electrolysis-molten | Crucible of molten potassium iodide with cathode on the left and anode on the ri | 642 px | 2.0 | 700x320 | CF, CH, TF, TH |
| electrolysis-molten | Crucible of molten aluminium oxide with cathode on the left and anode on the rig | 642 px | 2.0 | 700x320 | CF, CH, TF, TH |
| rate-of-photosynthesis | Required practical set-up: lamp at 20 cm from pondweed in a tube of water, a bea | 640 px | 2.0 | 640x270 | CF, CH, TF, TH |
| rate-of-photosynthesis | Required practical set-up: lamp at 30 cm from pondweed in a tube of water, a bea | 640 px | 2.0 | 640x270 | CF, CH, TF, TH |
| rate-of-photosynthesis | Required practical set-up: lamp at 40 cm from pondweed in a tube of water, a bea | 640 px | 2.0 | 640x270 | CF, CH, TF, TH |
| homeostasis | Negative feedback: when the level rises the response brings it down; when it fal | 558 px | 2.0 | 660x230 | CH, TH |
| contraception-fertility | IVF: . | 558 px | 2.0 | 660x140 | CH, TH |
| contraception-fertility | IVF: FSH and LH given. | 558 px | 2.0 | 660x140 | CH, TH |

Not listed: any figure at 2.0 columns or under (it scrolls by about one screen).

Subscript digits (`<tspan baseline-shift="sub">` at 75%, written by the ks4-ext scripts) are not counted: they are part of a label that clears the floor.
