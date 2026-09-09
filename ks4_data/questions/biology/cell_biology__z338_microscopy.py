"""Biology · Cell biology — the MRB-338 expansion of `microscopy`.

One leaf only: AQA 8461 §4.1.1.5, the comparison of light and electron
microscopes and the magnification arithmetic that goes with it. The original
twelve rows in `cell_biology.py` take the SEM, the rearranged equation, the
light microscope's 200 nm resolution, a disadvantage of staining, two
magnification calculations, the wavelength answer, choosing an instrument for
a living pond organism, an image-size calculation, a units-mismatch
comparison, the empty-magnification claim and one scale-bar conversion.

This file puts its weight where the subtopic is distinctive rather than where
the arithmetic is easiest, because the neighbouring leaf `animal-plant-cells`
has already taken the scale bar, the water mount, the thin section and the
purpose of a stain. So the weight here falls on magnification and resolution
as two separate properties, on what fixes each instrument's limit, on the
consequences of the electron beam needing a vacuum, on the TEM/SEM split, on
the historical point that sub-cellular structure was described as the
instruments improved, and on orders of magnitude across mm, µm and nm.

Numbers come out exact: every conversion is a clean power of ten and every
magnification divides without a remainder.
"""

TOPIC = "cell-biology"
SUBJECT = "biology"

QUESTIONS = [
    # ══ easier · e05–e12 ═════════════════════════════════════════════════
    # The two definitions the leaf turns on, the source of each instrument's
    # image, the light microscope's magnification ceiling, the electron
    # microscope's resolution, the TEM (e01 already names the SEM), and the
    # one unit conversion the rest of the leaf's arithmetic rests on.
    {
        "id": "ks4-microscopy-e05",
        "subtopic_slug": "microscopy",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State what is meant by the magnification of a microscope.",
        "options": [
            "How many times larger the image is than the real specimen",
            "How close together two points can be and still look separate",
            "The number of lenses fitted between the eye and the slide",
            "The smallest structure the instrument is able to show at all",
        ],
        "correct_index": 0,
        "why": "Magnification is a size comparison — how many times bigger "
               "the image is than the specimen itself.",
    },
    {
        "id": "ks4-microscopy-e06",
        "subtopic_slug": "microscopy",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Define the term resolution as it is used in "
                "microscopy.",
        "options": [
            "The total number of times the specimen has been enlarged by "
            "the lenses",
            "The brightness of the lamp shining underneath the stage",
            "The ability to tell two points close together apart as two "
            "separate points",
            "The thickness of specimen the instrument can be used on",
        ],
        "correct_index": 2,
        "why": "Resolution is about detail, not size: it is how close two "
               "points can be while still appearing separate.",
    },
    {
        "id": "ks4-microscopy-e07",
        "subtopic_slug": "microscopy",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name what a light microscope uses to form an image.",
        "options": [
            "Visible light, brought to a focus by a set of glass lenses",
            "X-rays passed through the specimen onto a photographic plate",
            "Sound waves reflected back from the surface of the specimen",
            "A beam of electrons steered by powerful magnets",
        ],
        "correct_index": 0,
        "why": "A light microscope focuses visible light through glass "
               "lenses, which is why it is also called an optical "
               "microscope.",
    },
    {
        "id": "ks4-microscopy-e08",
        "subtopic_slug": "microscopy",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name what an electron microscope uses in place of light.",
        "options": [
            "A very bright lamp fitted with a much finer filament",
            "A beam of electrons, brought to a focus by magnetic coils",
            "A stream of protons drawn out of the nuclei of atoms",
            "Ultraviolet light, which the human eye is unable to detect",
        ],
        "correct_index": 1,
        "why": "The image is formed by a beam of electrons, whose wavelength "
               "is thousands of times shorter than that of visible light.",
    },
    {
        "id": "ks4-microscopy-e09",
        "subtopic_slug": "microscopy",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the approximate maximum magnification of a light "
                "microscope.",
        "options": [
            "About ×20",
            "About ×200",
            "About ×2000",
            "About ×2 000 000",
        ],
        "correct_index": 2,
        "why": "A light microscope reaches roughly ×2000; past that the "
               "image is bigger but carries no extra detail.",
    },
    {
        "id": "ks4-microscopy-e10",
        "subtopic_slug": "microscopy",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the approximate resolution of an electron "
                "microscope.",
        "options": [
            "1000 nm",
            "0.1 nm",
            "200 nm",
            "0.1 µm",
        ],
        "correct_index": 1,
        "why": "An electron microscope resolves down to about 0.1 nm, some "
               "two thousand times finer than a light microscope.",
    },
    {
        "id": "ks4-microscopy-e11",
        "subtopic_slug": "microscopy",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the type of electron microscope whose beam passes "
                "through a very thin slice of the specimen.",
        "options": [
            "A dissecting microscope, used on whole small organisms",
            "A transmission electron microscope (TEM)",
            "A compound light microscope turned to its highest power",
            "A scanning electron microscope (SEM)",
        ],
        "correct_index": 1,
        "why": "In a TEM the electrons travel through the specimen, so the "
               "image shows what lies inside it.",
    },
        {
        "id": "ks4-microscopy-e12",
        "subtopic_slug": "microscopy",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Place these three units in order, from the largest to the "
                "smallest.",
        "options": [
            "Nanometre, micrometre, millimetre",
            "Micrometre, millimetre, nanometre",
            "Millimetre, micrometre, nanometre",
            "Millimetre, nanometre, micrometre",
        ],
        "correct_index": 2,
        "why": "A millimetre is a thousand micrometres, and a micrometre is a "
               "thousand nanometres, so each step down is a thousand times "
               "smaller.",
    },

    # ══ standard · s05–s26 ═══════════════════════════════════════════════
    # Choosing an instrument for a stated purpose, the cause behind each
    # limit, the vacuum and its consequences, the history, and the
    # arithmetic that needs the equation applied rather than recited.
    {
        "id": "ks4-microscopy-s05",
        "subtopic_slug": "microscopy",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A scientist needs to see the folded inner membranes of a "
                "mitochondrion. Suggest which microscope should be used, "
                "and why.",
        "options": [
            "A light microscope, because the folds take up methylene blue",
            "A scanning electron microscope, because it shows the outside "
            "of a specimen in three dimensions",
            "A transmission electron microscope, because its beam goes "
            "through a thin slice and shows internal detail",
            "A light microscope at ×2000, because that is the greatest "
            "magnification any instrument reaches",
        ],
        "correct_index": 2,
        "why": "A TEM drives electrons through an extremely thin slice, so "
               "structures inside an organelle can be seen.",
    },
    {
        "id": "ks4-microscopy-s06",
        "subtopic_slug": "microscopy",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest which microscope would best show the pattern of "
                "spikes on the outside of a pollen grain.",
        "options": [
            "A transmission electron microscope, because it reaches the "
            "highest magnification of any instrument",
            "A scanning electron microscope",
            "A light microscope, because the grain can be kept alive while "
            "it is being examined",
            "A hand lens, because the spikes are large enough to be seen "
            "without any microscope",
        ],
        "correct_index": 1,
        "why": "An SEM scans across the surface of a specimen, so it is the "
               "instrument that reveals external shape in three dimensions.",
    },
    {
        "id": "ks4-microscopy-s07",
        "subtopic_slug": "microscopy",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a specimen placed in an electron microscope "
                "cannot be alive.",
        "options": [
            "The magnification is so high that any movement would blur the "
            "picture beyond use",
            "The specimen must be stained with iodine, and iodine kills "
            "every cell",
            "The beam travels through a vacuum, and no living cell can "
            "survive being placed in one",
            "The electron beam heats the specimen until all its water has "
            "boiled away",
        ],
        "correct_index": 2,
        "why": "Air scatters electrons, so the column is emptied of air; a "
               "living specimen cannot survive a vacuum.",
    },
    {
        "id": "ks4-microscopy-s08",
        "subtopic_slug": "microscopy",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why enlarging an image beyond a microscope's "
                "resolution reveals no extra detail.",
        "options": [
            "Points already blurred into one just become a larger blur",
            "The lenses grow warm at high power and start to distort the "
            "picture that reaches the eye",
            "The specimen is cut too thinly to hold any more detail than "
            "the instrument is already showing",
            "Magnification and resolution are two different names for one "
            "and the same property",
        ],
        "correct_index": 0,
        "why": "Resolution decides whether two close points stay separate; "
               "once they have merged, magnifying only enlarges the merged "
               "blur.",
    },
    {
        "id": "ks4-microscopy-s09",
        "subtopic_slug": "microscopy",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain what sets the limit on the fineness of detail a "
                "light microscope can show.",
        "options": [
            "The number of glass lenses the manufacturer has fitted to it",
            "The wavelength of the visible light used to form the image",
            "The brightness of the lamp placed beneath the specimen stage",
            "The thickness of the coverslip lowered onto the specimen",
        ],
        "correct_index": 1,
        "why": "Two points closer than about half a wavelength of light "
               "cannot be separated, which fixes the limit near 200 nm.",
    },
    {
        "id": "ks4-microscopy-s10",
        "subtopic_slug": "microscopy",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Describe how scientists' understanding of sub-cellular "
                "structures changed during the twentieth century.",
        "options": [
            "It stayed as it was, because light microscopes had already "
            "shown everything",
            "It changed because new theories about cells were proposed, "
            "not because new instruments appeared",
            "It grew as microscopes improved, revealing sub-cellular "
            "structures nobody had seen before",
            "It shrank, because electron microscopes showed earlier "
            "drawings to be inventions",
        ],
        "correct_index": 2,
        "why": "Electron microscopes revealed ribosomes, the nuclear "
               "envelope and the inner detail of mitochondria, so "
               "understanding advanced as the instruments did.",
    },
    {
        "id": "ks4-microscopy-s11",
        "subtopic_slug": "microscopy",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why an electron microscope produces a black and "
                "white image.",
        "options": [
            "Every specimen is dyed black before the beam is switched on",
            "Electrons carry no colour, so the image records only how many "
            "of them get through",
            "The colour is stripped out deliberately so that the structures "
            "stand out more sharply",
            "The vacuum inside the column absorbs all of the coloured light "
            "before it reaches the screen",
        ],
        "correct_index": 1,
        "why": "The image is built from electrons rather than visible "
               "light, so it has no colour of its own.",
    },
    {
        "id": "ks4-microscopy-s12",
        "subtopic_slug": "microscopy",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest why school laboratories are equipped with light "
                "microscopes rather than electron microscopes.",
        "options": [
            "Light microscopes are cheap, small and simple enough for a "
            "class to use",
            "Light microscopes have the better resolution of the two",
            "Electron microscopes cannot magnify a plant cell, only a "
            "bacterial one",
            "Electron microscopes have been forbidden in schools on safety "
            "grounds",
        ],
        "correct_index": 0,
        "why": "An electron microscope costs a great deal, fills a room and "
               "needs a trained operator, so schools use light microscopes.",
    },
    {
        "id": "ks4-microscopy-s13",
        "subtopic_slug": "microscopy",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A bacterium is 2 µm long. Its image on a screen is 4000 µm "
                "long. Calculate the magnification.",
        "options": [
            "×2",
            "×8000",
            "×0.0005",
            "×2000",
        ],
        "correct_index": 3,
        "why": "Magnification = image ÷ actual = 4000 µm ÷ 2 µm = 2000, and "
               "both lengths are already in the same unit.",
    },
    {
        "id": "ks4-microscopy-s14",
        "subtopic_slug": "microscopy",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A ribosome is 20 nm across. Calculate the width of its "
                "image, in millimetres, at a magnification of ×500 000.",
        "options": [
            "10 000 mm",
            "0.01 mm",
            "10 mm",
            "25 000 mm",
        ],
        "correct_index": 2,
        "why": "20 nm × 500 000 = 10 000 000 nm, and 10 000 000 nm divided "
               "by 1 000 000 gives 10 mm.",
    },
    {
        "id": "ks4-microscopy-s15",
        "subtopic_slug": "microscopy",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Two structures inside a cell lie 150 nm apart. Describe "
                "what a light microscope would show.",
        "options": [
            "Two clearly separate structures, because 150 nm is a wide gap",
            "A single structure, because 150 nm is closer than the 200 nm "
            "the microscope can resolve",
            "Nothing whatever, because a light microscope cannot form an "
            "image of the inside of a cell",
            "Two structures, but only once the specimen has been stained "
            "with iodine solution first",
        ],
        "correct_index": 1,
        "why": "A light microscope resolves to about 200 nm, so anything "
               "closer than that merges into one point.",
    },
    {
        "id": "ks4-microscopy-s16",
        "subtopic_slug": "microscopy",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A ribosome is 20 nm across. Give this length in metres, in "
                "standard form.",
        "options": [
            "2 × 10⁻⁸ m",
            "2 × 10⁻⁹ m",
            "2 × 10⁻⁵ m",
            "2 × 10⁸ m",
        ],
        "correct_index": 0,
        "why": "1 nm is 1 × 10⁻⁹ m, so 20 nm is 20 × 10⁻⁹ m, written in "
               "standard form as 2 × 10⁻⁸ m.",
    },
    {
        "id": "ks4-microscopy-s17",
        "subtopic_slug": "microscopy",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A micrograph carries a scale bar labelled 10 µm. State "
                "what that label tells you.",
        "options": [
            "The width of the whole specimen shown in the micrograph",
            "The magnification at which the micrograph was printed",
            "The real length that the drawn bar actually stands for",
            "The finest detail the microscope was able to resolve",
        ],
        "correct_index": 2,
        "why": "The label gives the actual length represented by the bar "
               "itself, and the specimen's size is worked out from it.",
    },
    {
        "id": "ks4-microscopy-s18",
        "subtopic_slug": "microscopy",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A light microscope resolves 200 nm and an electron "
                "microscope 0.1 nm. Calculate how many times better the "
                "electron microscope's resolution is.",
        "options": [
            "20 times better",
            "200 times better",
            "20 000 times better",
            "2000 times better",
        ],
        "correct_index": 3,
        "why": "200 nm ÷ 0.1 nm = 2000, so the electron microscope "
               "separates points two thousand times closer together.",
    },
    {
        "id": "ks4-microscopy-s19",
        "subtopic_slug": "microscopy",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Two microscopes both magnify ×400, but one has a much "
                "better resolution. Explain which shows more detail.",
        "options": [
            "The one with the better resolution, because its close points "
            "stay separate",
            "Neither, because equal magnification always gives an equally "
            "detailed picture",
            "The one with the poorer resolution, because its image is less "
            "crowded with structures",
            "Both to the same degree, because resolution only matters above "
            "a magnification of ×1000",
        ],
        "correct_index": 0,
        "why": "At the same magnification it is resolution that decides "
               "whether fine detail stays sharp or merges together.",
    },
    {
        "id": "ks4-microscopy-s20",
        "subtopic_slug": "microscopy",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A researcher needs to count the ribosomes in a liver cell. "
                "Suggest which microscope is needed, and why.",
        "options": [
            "A light microscope, because the cell has to stay alive while "
            "the counting is done",
            "An electron microscope, because a ribosome is far smaller than "
            "200 nm",
            "A light microscope at ×2000, because ribosomes are about 20 µm "
            "across",
            "A hand lens, because ribosomes are attached to the outside of "
            "the cell membrane",
        ],
        "correct_index": 1,
        "why": "A ribosome is about 20 nm across, well below the 200 nm a "
               "light microscope can resolve, so only an electron "
               "microscope will show one.",
    },
    {
        "id": "ks4-microscopy-s21",
        "subtopic_slug": "microscopy",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student divides an image length in millimetres by an "
                "actual length in micrometres and reports a magnification "
                "of ×3. Explain the error.",
        "options": [
            "The two lengths should have been multiplied, not divided",
            "The equation is upside down; magnification is actual size "
            "divided by image size",
            "The magnification of the eyepiece lens has been left out of "
            "the calculation altogether",
            "The units were never matched, so the answer is 1000 times too "
            "small",
        ],
        "correct_index": 3,
        "why": "1 mm is 1000 µm, so leaving the image in millimetres makes "
               "the calculated magnification a thousand times too small.",
    },
    {
        "id": "ks4-microscopy-s22",
        "subtopic_slug": "microscopy",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A structure in a cell measures 0.0002 mm across. Calculate "
                "this width in nanometres.",
        "options": [
            "200 nm",
            "2 nm",
            "0.2 nm",
            "20 000 nm",
        ],
        "correct_index": 0,
        "why": "0.0002 mm × 1000 = 0.2 µm, and 0.2 µm × 1000 = 200 nm.",
    },
    {
        "id": "ks4-microscopy-s23",
        "subtopic_slug": "microscopy",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A light microscope has a ×10 eyepiece lens and a ×40 "
                "objective lens. Calculate the total magnification.",
        "options": [
            "×50",
            "×4",
            "×4000",
            "×400",
        ],
        "correct_index": 3,
        "why": "The total magnification of a compound microscope is "
               "eyepiece × objective, so 10 × 40 = 400.",
    },
    {
        "id": "ks4-microscopy-s24",
        "subtopic_slug": "microscopy",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student writes that an electron microscope works by "
                "shining a very bright light on the specimen. Give the "
                "correct version of that sentence.",
        "options": [
            "It shines ultraviolet light, which the specimen absorbs and "
            "then gives out again",
            "It uses the same lamp as a light microscope but a very much "
            "finer set of lenses",
            "It sends a beam of electrons through or across the specimen "
            "instead",
            "It shines a laser at the specimen and records the reflected "
            "light",
        ],
        "correct_index": 2,
        "why": "An electron microscope uses electrons, whose much shorter "
               "wavelength is what gives it the higher resolution — "
               "brightness has nothing to do with it.",
    },
    {
        "id": "ks4-microscopy-s25",
        "subtopic_slug": "microscopy",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "The DNA loop of a bacterial plasmid is about 2 nm thick. "
                "Explain why a light microscope cannot show it.",
        "options": [
            "Because 2 nm is a hundred times finer than the 200 nm a light "
            "microscope can resolve",
            "Because DNA has no colour and there is no stain that will "
            "attach itself to it",
            "Because a plasmid sits outside the cell and is washed away "
            "during mounting",
            "Because bacteria are far too small to be placed under a light "
            "microscope at all",
        ],
        "correct_index": 0,
        "why": "A light microscope cannot separate points closer than about "
               "200 nm, and the plasmid strand is a hundred times thinner "
               "than that.",
    },
    {
        "id": "ks4-microscopy-s26",
        "subtopic_slug": "microscopy",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "State why a scale bar is added to a biological drawing.",
        "options": [
            "It records which objective lens was in place at the time the "
            "drawing was made",
            "It shows the real size of the structures, whatever size the "
            "drawing is printed at",
            "It marks the edge of the field of view seen down the "
            "microscope",
            "It shows how much time the student spent making the drawing",
        ],
        "correct_index": 1,
        "why": "A scale bar is enlarged or reduced along with the drawing, "
               "so the actual sizes can always be recovered from it.",
    },

    # ══ harder · h05–h26 ═════════════════════════════════════════════════
    # Rearranged and multi-step arithmetic through two unit changes, orders
    # of magnitude, and the evaluations: better lenses, "always the better
    # instrument", the false-colour micrograph and the misread history.
    {
        "id": "ks4-microscopy-h05",
        "subtopic_slug": "microscopy",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A mitochondrion is 2 µm long. Determine the length of its "
                "image, in millimetres, on a micrograph printed at ×25 000.",
        "options": [
            "5 mm",
            "50 mm",
            "500 mm",
            "12 500 mm",
        ],
        "correct_index": 1,
        "why": "2 µm × 25 000 = 50 000 µm, and 50 000 µm ÷ 1000 = 50 mm.",
    },
    {
        "id": "ks4-microscopy-h06",
        "subtopic_slug": "microscopy",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A structure measures 8 mm on a micrograph printed at "
                "×40 000. Determine its actual length in nanometres.",
        "options": [
            "0.2 nm",
            "2000 nm",
            "320 000 nm",
            "200 nm",
        ],
        "correct_index": 3,
        "why": "8 mm is 8 000 000 nm, and 8 000 000 ÷ 40 000 = 200 nm.",
    },
    {
        "id": "ks4-microscopy-h07",
        "subtopic_slug": "microscopy",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "On a micrograph a bar labelled 2 µm measures 10 mm, and a "
                "mitochondrion measures 15 mm. Determine the "
                "mitochondrion's actual length.",
        "options": [
            "1.5 µm",
            "7.5 µm",
            "3 µm",
            "30 µm",
        ],
        "correct_index": 2,
        "why": "The bar gives a magnification of 10 000 µm ÷ 2 µm = 5000, "
               "so 15 mm is 15 000 µm ÷ 5000 = 3 µm.",
    },
    {
        "id": "ks4-microscopy-h08",
        "subtopic_slug": "microscopy",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A light microscope reaches about ×2000 and an electron "
                "microscope about ×2 000 000. Calculate how many times "
                "greater the electron microscope's maximum magnification "
                "is.",
        "options": [
            "1000 times greater",
            "100 times greater",
            "2000 times greater",
            "1 000 000 times greater",
        ],
        "correct_index": 0,
        "why": "2 000 000 ÷ 2000 = 1000, so the electron microscope "
               "magnifies a thousand times more strongly at its limit.",
    },
    {
        "id": "ks4-microscopy-h09",
        "subtopic_slug": "microscopy",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "An animal cell is 20 µm across and an electron microscope "
                "resolves 0.1 nm. Calculate how many times smaller that "
                "resolution limit is than the cell.",
        "options": [
            "200",
            "2000",
            "20 000 000",
            "200 000",
        ],
        "correct_index": 3,
        "why": "20 µm is 20 000 nm, and 20 000 ÷ 0.1 = 200 000.",
    },
    {
        "id": "ks4-microscopy-h10",
        "subtopic_slug": "microscopy",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student suggests that better glass lenses would let a "
                "light microscope show ribosomes. Evaluate this suggestion.",
        "options": [
            "Correct — lens quality is the only thing holding the detail "
            "back at present",
            "Wrong — the limit is set by the wavelength of light, not by "
            "the lenses",
            "Correct — provided the specimen is stained with methylene blue "
            "before it is viewed",
            "Wrong — ribosomes are found only in cells that no light is "
            "ever able to reach",
        ],
        "correct_index": 1,
        "why": "However good the lenses, light cannot resolve points closer "
               "than about 200 nm, and a ribosome is roughly 20 nm across.",
    },
    {
        "id": "ks4-microscopy-h11",
        "subtopic_slug": "microscopy",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student claims an electron microscope is the better "
                "instrument for every biological investigation. Evaluate "
                "this claim.",
        "options": [
            "Correct, because it has both the greater magnification and "
            "resolution",
            "Wrong, because its resolution is the poorer whenever a low "
            "magnification is used",
            "Correct, because a specimen can be put straight into it with "
            "no preparation of any kind",
            "Wrong, because its specimens must be dead in a vacuum, so no "
            "living process can be watched",
        ],
        "correct_index": 3,
        "why": "The beam needs a vacuum, so the specimen is dead; anything "
               "living has to be watched under a light microscope.",
    },
    {
        "id": "ks4-microscopy-h12",
        "subtopic_slug": "microscopy",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A scientist wants both the dimpled surface shape of a red "
                "blood cell and a view of its contents. Suggest which "
                "microscopes are needed.",
        "options": [
            "A scanning electron microscope for the surface and a "
            "transmission one for the contents",
            "A transmission electron microscope for the surface and a "
            "scanning one for the contents",
            "A scanning electron microscope alone, since it shows the "
            "surface and the contents together",
            "A light microscope alone, since both features are very much "
            "larger than 200 nm across",
        ],
        "correct_index": 0,
        "why": "An SEM scans the outside and gives the surface shape; a TEM "
               "sends electrons through a slice and gives what is inside.",
    },
    {
        "id": "ks4-microscopy-h13",
        "subtopic_slug": "microscopy",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Predict what would happen to a living cell placed inside "
                "an electron microscope.",
        "options": [
            "It would go on living, though its movement would blur the "
            "image",
            "It would divide more quickly, because the beam supplies it "
            "with extra energy",
            "It would be unaffected, because electrons pass straight "
            "through living matter",
            "It would die, because the air is pumped out of the column it "
            "sits in",
        ],
        "correct_index": 3,
        "why": "The specimen chamber is a vacuum, so a living cell cannot "
               "survive there — which is why electron micrographs never "
               "show a living process.",
    },
    {
        "id": "ks4-microscopy-h14",
        "subtopic_slug": "microscopy",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Cells had been drawn for nearly three centuries before the "
                "ribosome was described in the 1950s. Explain the delay.",
        "options": [
            "Ribosomes are about 20 nm across, far below what light can "
            "resolve",
            "Ribosomes first appeared in cells during the twentieth "
            "century, so earlier workers had none to draw",
            "Earlier scientists had no interest at all in what the inside "
            "of a cell was made of",
            "The stains used by earlier scientists happened to hide the "
            "ribosomes from view",
        ],
        "correct_index": 0,
        "why": "Structures below the 200 nm limit of light became visible "
               "only once electron microscopes were built.",
    },
    {
        "id": "ks4-microscopy-h15",
        "subtopic_slug": "microscopy",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Two points in a specimen lie 0.5 µm apart. Determine which "
                "microscopes could show them as two separate points.",
        "options": [
            "Neither, because 0.5 µm is finer than both resolution limits",
            "The electron microscope only, because 0.5 µm is finer than "
            "light is able to resolve",
            "The light microscope only, because an electron beam would pass "
            "straight between them",
            "Both, because 0.5 µm is 500 nm and each instrument resolves "
            "finer than that",
        ],
        "correct_index": 3,
        "why": "0.5 µm is 500 nm, larger than the light microscope's 200 nm "
               "limit and far larger than 0.1 nm.",
    },
    {
        "id": "ks4-microscopy-h16",
        "subtopic_slug": "microscopy",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "An image measures 45 mm and the specimen is 15 µm long. A "
                "student reports the magnification as ×3. Determine the "
                "correct magnification.",
        "options": [
            "×300",
            "×0.3",
            "×675",
            "×3000",
        ],
        "correct_index": 3,
        "why": "45 mm is 45 000 µm, and 45 000 ÷ 15 = 3000; the student "
               "divided millimetres by micrometres without converting.",
    },
    {
        "id": "ks4-microscopy-h17",
        "subtopic_slug": "microscopy",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A microscope has a ×10 eyepiece. A student turns the "
                "objective from ×10 to ×40. Describe the effect on the "
                "total magnification.",
        "options": [
            "It rises from ×20 to ×50, because the two lens values are "
            "added together",
            "It rises from ×100 to ×400, and the resolution rises four "
            "times over as well",
            "It rises from ×100 to ×400, so the image is four times wider",
            "It stays at ×400, because the eyepiece sets the total on its "
            "own",
        ],
        "correct_index": 2,
        "why": "Total magnification is eyepiece × objective, so it goes "
               "from 10 × 10 = 100 to 10 × 40 = 400; resolution is "
               "unchanged.",
    },
    {
        "id": "ks4-microscopy-h18",
        "subtopic_slug": "microscopy",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A hospital laboratory examines many blood samples each "
                "day. Evaluate its use of light microscopes rather than "
                "electron microscopes.",
        "options": [
            "Poor — only an electron microscope can magnify a blood cell at "
            "all",
            "Poor — an electron microscope would be quicker, since no slide "
            "has to be prepared for it",
            "Sound — blood cells are far larger than 200 nm, and light "
            "microscopy is quick and cheap",
            "Sound — but only because hospitals are not permitted to own an "
            "electron microscope",
        ],
        "correct_index": 2,
        "why": "A red blood cell is about 7 µm across, well within a light "
               "microscope's range, so the cheaper and faster instrument "
               "does the job.",
    },
    {
        "id": "ks4-microscopy-h19",
        "subtopic_slug": "microscopy",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A textbook prints a brightly coloured electron micrograph "
                "of a mitochondrion. Suggest how that colour came about.",
        "options": [
            "It was added to the black and white image afterwards, by "
            "computer",
            "The specimen was stained with coloured dyes before the beam "
            "was switched on",
            "The electron beam splits into colours as it travels through "
            "the specimen",
            "Mitochondria are naturally coloured and the microscope simply "
            "records that colour",
        ],
        "correct_index": 0,
        "why": "Electron micrographs are black and white, so any colour is "
               "false colour added digitally to tell structures apart.",
    },
    {
        "id": "ks4-microscopy-h20",
        "subtopic_slug": "microscopy",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A drawing of a cell is made at ×100. Determine how long a "
                "scale bar must be drawn if it is to stand for 20 µm.",
        "options": [
            "0.2 mm",
            "2 mm",
            "20 mm",
            "200 mm",
        ],
        "correct_index": 1,
        "why": "20 µm × 100 = 2000 µm, and 2000 µm ÷ 1000 = 2 mm.",
    },
    {
        "id": "ks4-microscopy-h21",
        "subtopic_slug": "microscopy",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why the air must be pumped out of the inside of an "
                "electron microscope.",
        "options": [
            "Air would make the specimen swell until the thin slice broke "
            "apart",
            "Air molecules would scatter the electrons before they reached "
            "the specimen",
            "Air carries dust, which would settle on the specimen and hide "
            "the finer detail",
            "Air would slow the electrons until they had stopped moving "
            "altogether",
        ],
        "correct_index": 1,
        "why": "Electrons are scattered by the particles in air, so a clean "
               "beam can only travel through a vacuum.",
    },
    {
        "id": "ks4-microscopy-h22",
        "subtopic_slug": "microscopy",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a specimen must be sliced extremely thinly for "
                "a transmission electron microscope but not for a scanning "
                "one.",
        "options": [
            "A TEM works at a far higher magnification, and thick specimens "
            "cannot be magnified",
            "A TEM has a stronger vacuum, which a thick specimen would not "
            "survive for long",
            "A TEM's beam must pass right through the specimen, while an "
            "SEM's only scans its surface",
            "A TEM needs the specimen stained, and a stain cannot soak into "
            "a thick piece of tissue",
        ],
        "correct_index": 2,
        "why": "Transmission means the electrons travel through the "
               "specimen, so it must be thin enough to let them out the "
               "other side; an SEM never needs that.",
    },
    {
        "id": "ks4-microscopy-h23",
        "subtopic_slug": "microscopy",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Place these in order of increasing size: a ribosome 20 nm, "
                "a mitochondrion 1.5 µm, a bacterium 0.003 mm, an animal "
                "cell 20 µm.",
        "options": [
            "Ribosome, bacterium, mitochondrion, animal cell",
            "Mitochondrion, ribosome, bacterium, animal cell",
            "Bacterium, ribosome, mitochondrion, animal cell",
            "Ribosome, mitochondrion, bacterium, animal cell",
        ],
        "correct_index": 3,
        "why": "In one unit these are 0.02 µm, 1.5 µm, 3 µm and 20 µm, so "
               "the ribosome is smallest and the animal cell largest.",
    },
    {
        "id": "ks4-microscopy-h24",
        "subtopic_slug": "microscopy",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Chloroplasts were seen under light microscopes for over a "
                "century. Suggest why their internal membranes were "
                "described only after 1950.",
        "options": [
            "Chloroplasts only grew internal membranes during the "
            "twentieth century",
            "No stain existed before then that would colour a chloroplast "
            "at all",
            "The membranes are far thinner than 200 nm, so only an electron "
            "beam resolves them",
            "Chloroplasts are destroyed by the lamp used in a light "
            "microscope",
        ],
        "correct_index": 2,
        "why": "A chloroplast is about 5 µm long and easily seen, but the "
               "membranes inside it lie far below the 200 nm limit of "
               "light.",
    },
    {
        "id": "ks4-microscopy-h25",
        "subtopic_slug": "microscopy",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A micrograph printed at ×15 000 shows a nucleus measuring "
                "90 mm across. Determine the nucleus's actual diameter in "
                "micrometres.",
        "options": [
            "0.6 µm",
            "6 µm",
            "60 µm",
            "1350 µm",
        ],
        "correct_index": 1,
        "why": "90 mm ÷ 15 000 = 0.006 mm, and 0.006 mm × 1000 = 6 µm.",
    },
    {
        "id": "ks4-microscopy-h26",
        "subtopic_slug": "microscopy",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare the state a specimen must be in for a light "
                "microscope and for a transmission electron microscope.",
        "options": [
            "Both must be dead, and both are cut to exactly the same "
            "thickness beforehand",
            "For light it must be dead; for the electron beam it may be "
            "kept alive inside the vacuum",
            "Neither needs any preparation, because both instruments work "
            "on whole living organisms",
            "For light it may be alive; for the electron beam it must be "
            "dead and far thinner",
        ],
        "correct_index": 3,
        "why": "A light microscope will take a living specimen mounted in "
               "water, while a TEM needs a dead, ultra-thin slice because "
               "the beam must pass through it in a vacuum.",
    },
]
