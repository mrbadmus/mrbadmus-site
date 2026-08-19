"""B1 lesson 02 — Using a microscope: twelve questions (MRB-269).

These probe the four things the lesson actually teaches and the two things it
exists to correct. The formula is tested backwards (total ÷ eyepiece) and as a
spot-the-error on units, never as a straight repeat of the ladder's ×15 × ×40
rung. Field of view and depth of field are tested as *consequences* — climb the
magnification and you hand back width and depth together — because that is the
evidence the bench readout gives the student.

The distractors are built from the lesson's own declared misconceptions.
CELL-01 ("those neat round circles are the cells") drives the bubble options in
e02 and h02: a coverslip laid flat traps air, and air is round with a thick dark
rim. CELL-02 ("the highest magnification always shows you the most") drives the
"same amount, bigger" option in s02, the "identical, the totals match" option in
h01 and the "turn the wheel further and it will all sharpen" option in h03. The
"multiply, never add" key fact supplies the 10 + 40 = 50 option in s04 and the
100 − 10 option in s01, and the no-unit half of that key fact supplies the rest
of s04.

`figure` is None throughout. Both of this lesson's figures are micrographs with
`status: "needed"` — they render as "Photo coming soon", so a question that
depended on one would be unanswerable in the pool as it ships.
"""

UNIT = "B1"
LESSON = "using-a-microscope"
LESSON_NUMBER = 2

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "b1-02-e01",
        "band": "easier",
        "text": "Onion skin can be looked at under a microscope, but a whole "
                "onion cannot. Why not?",
        "options": [
            {"text": "Light shines down onto the slide from above, so the "
                     "specimen has to be flat.",
             "correct": False,
             "why": "The lamp is under the stage, which is why the slide is "
                    "clipped over the hole in the middle. The light travels up "
                    "through the specimen, so anything thick simply blocks it."},
            {"text": "Light has to pass through the specimen, and only the "
                     "skin is thin enough.",
             "correct": True},
            {"text": "Only the skin of an onion is made of cells, so the rest "
                     "is not worth looking at.",
             "correct": False,
             "why": "Every part of the onion is made of cells. The skin is used "
                    "because it peels away one layer thick, not because it is "
                    "the only part with cells in it."},
            {"text": "A microscope cannot magnify anything that is already big "
                     "enough to see.",
             "correct": False,
             "why": "A microscope magnifies whatever you put on the stage. The "
                    "problem with a whole onion is that no light gets through "
                    "it, not that it is too big to be worth magnifying."},
        ],
        "figure": None,
    },
    {
        "id": "b1-02-e02",
        "band": "easier",
        "text": "Sam lays the coverslip flat onto the drop of water instead of "
                "lowering it on one edge. Down the eyepiece he sees neat round "
                "shapes with thick black rims. What are they?",
        "options": [
            {"text": "Air bubbles, trapped underneath the coverslip when it "
                     "went down flat.",
             "correct": True},
            {"text": "The onion cells, which look round at this magnification.",
             "correct": False,
             "why": "This is the mistake that gets drawn as cells every year. "
                    "Onion cells are long boxes packed in rows, never perfect "
                    "circles with thick black rims — those rims are air."},
            {"text": "Drops of water that have not spread out under the "
                     "coverslip yet.",
             "correct": False,
             "why": "The coverslip spreads the water into a thin flat layer. "
                    "Round shapes with thick dark edges are trapped air, and "
                    "lowering the coverslip slowly on one edge stops them."},
            {"text": "Dust that has settled on the eyepiece lens.",
             "correct": False,
             "why": "Dust on the eyepiece stays put when you move the slide. "
                    "These circles move with the slide, because they are "
                    "trapped in the water underneath the coverslip."},
        ],
        "figure": None,
    },
    {
        "id": "b1-02-e03",
        "band": "easier",
        "text": "A student says the field of view is “how much bigger the cells "
                "look”. What is the field of view actually?",
        "options": [
            {"text": "How many times bigger than real life the specimen looks.",
             "correct": False,
             "why": "That is magnification. The field of view is how much of "
                    "the slide fits into the circle at once, and it gets "
                    "smaller every time the magnification goes up."},
            {"text": "The thickness of the specimen that is sharp at any one "
                     "time.",
             "correct": False,
             "why": "That is the depth of field — a measurement through the "
                    "slide, not across it. Both shrink as you climb, but the "
                    "field of view is the width of slide you can see."},
            {"text": "The distance between the objective lens and the slide "
                     "underneath it.",
             "correct": False,
             "why": "That is the gap the focus wheel sets. The field of view is "
                    "how much of the slide the circle shows — 4.5 mm at ×40, "
                    "and 0.45 mm at ×400."},
            {"text": "The circle of the specimen you can see down the "
                     "microscope at one time.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b1-02-e04",
        "band": "easier",
        "text": "Sam has found his cells and is ready to record them. Which of "
                "these is a proper biological drawing?",
        "options": [
            {"text": "Coloured in to match the slide, with shading where the "
                     "view looks darker.",
             "correct": False,
             "why": "A biological drawing is a record, not a picture. It is "
                    "left in pencil with no shading and no colouring in — those "
                    "hide the detail rather than showing it."},
            {"text": "Pencil, clear single lines, no shading, with the "
                     "magnification written beside it.",
             "correct": True},
            {"text": "Pencil single lines with no shading, and his name and the "
                     "date beside it.",
             "correct": False,
             "why": "Everything here is right except the one label that matters "
                    "most. Without the magnification written next to it, the "
                    "drawing says nothing about how big the thing really was."},
            {"text": "Drawn in pen so that the lines come out dark and easy to "
                     "see.",
             "correct": False,
             "why": "Pen cannot be corrected, and thick dark lines cover the "
                    "detail you are trying to record. A biological drawing is "
                    "single pencil lines, with the magnification beside it."},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "b1-02-s01",
        "band": "standard",
        "text": "You are told the total magnification is ×100 and the eyepiece "
                "is ×10. Which objective must be clicked into place?",
        "options": [
            {"text": "The ×90 objective.",
             "correct": False,
             "why": "That is 100 − 10. The eyepiece and the objective multiply "
                    "together, so to work backwards you divide: "
                    "100 ÷ 10 = ×10."},
            {"text": "The ×100 objective.",
             "correct": False,
             "why": "That is the total, which already includes the eyepiece. "
                    "The objective makes an image and the eyepiece magnifies it "
                    "again, so the objective must be 100 ÷ 10 = ×10."},
            {"text": "The ×10 objective.",
             "correct": True},
            {"text": "The ×1000 objective.",
             "correct": False,
             "why": "That is 100 × 10. Multiplying takes you forwards, from the "
                    "two lenses to the total. Going backwards from the total "
                    "you divide: 100 ÷ 10 = ×10."},
        ],
        "figure": None,
    },
    {
        "id": "b1-02-s02",
        "band": "standard",
        "text": "With the ×4 objective in place the total is ×40: the field of "
                "view is 4.5 mm and about 15 onion cells fit across it. You "
                "click round to the ×40 objective. What should you expect?",
        "options": [
            {"text": "A field of view of 0.45 mm, with about one and a half "
                     "cells filling it.",
             "correct": True},
            {"text": "A field of view of 45 mm, with about 150 cells across it.",
             "correct": False,
             "why": "Ten times the magnification gives a tenth of the field of "
                    "view, not ten times more. Every step up shows you more "
                    "detail of less slide."},
            {"text": "The same 4.5 mm of slide, with the 15 cells simply "
                     "looking bigger.",
             "correct": False,
             "why": "The circle does not stretch to hold what it held before. A "
                    "tenth of the slide fits into it now — 0.45 mm, which is "
                    "fewer than two onion cells."},
            {"text": "A field of view of 0.45 mm, still with about 15 cells "
                     "across it.",
             "correct": False,
             "why": "You have shrunk the field of view but kept the cells. If a "
                    "tenth of the slide fits in the circle, a tenth of the "
                    "cells fit too — about one and a half."},
        ],
        "figure": None,
    },
    {
        "id": "b1-02-s03",
        "band": "standard",
        "text": "Why should you watch from the side, rather than down the "
                "eyepiece, while the objective is coming down towards the "
                "slide?",
        "options": [
            {"text": "Looking down the eyepiece while the lens is moving makes "
                     "the image blur.",
             "correct": False,
             "why": "The image blurs while anything moves, whichever way you "
                    "look. You watch from the side because from above you "
                    "cannot judge how close the lens is to the glass."},
            {"text": "The lamp is bright enough to damage your eyes when the "
                     "lens is close.",
             "correct": False,
             "why": "The lamp is not the risk here. The risk is the objective "
                    "meeting the slide, and from the eyepiece you cannot see "
                    "the gap closing until the glass has already gone."},
            {"text": "You need to check that the slide is clipped over the hole "
                     "in the stage.",
             "correct": False,
             "why": "That check matters, but you do it before you start. "
                    "Watching from the side is about seeing a gap that the "
                    "eyepiece cannot show you at all."},
            {"text": "From the eyepiece you cannot see the gap closing, so the "
                     "lens can hit the glass.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b1-02-s04",
        "band": "standard",
        "text": "Riya's eyepiece is ×10 and her objective is ×40. She writes "
                "her final answer as “400 mm”. What is wrong with it?",
        "options": [
            {"text": "She should have added the two lenses: 10 + 40 gives ×50.",
             "correct": False,
             "why": "Multiply, never add. The objective makes an image and the "
                    "eyepiece magnifies that image again, so 10 × 40 = ×400. "
                    "Adding is the commonest wrong answer on this one."},
            {"text": "The number is right, but magnification has no unit — it "
                     "is written ×400.",
             "correct": True},
            {"text": "Nothing: millimetres are the unit for everything seen "
                     "under a microscope.",
             "correct": False,
             "why": "Millimetres measure the field of view — 4.5 mm at ×40. "
                    "Magnification is a number of times bigger, and it is "
                    "written with no unit after it at all."},
            {"text": "It should be 400 cm, because a millimetre is far too "
                     "small for a cell.",
             "correct": False,
             "why": "The answer is not a length at all, in any unit. "
                    "Magnification has no unit: ×400 means four hundred times "
                    "bigger than real life, never 400 of anything."},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "b1-02-h01",
        "band": "harder",
        "text": "Two microscopes stand side by side. A has a ×10 eyepiece with "
                "a ×40 objective. B has a ×40 eyepiece with a ×10 objective. "
                "Which statement is true?",
        "options": [
            {"text": "A magnifies more, because the stronger lens on A is the "
                     "objective.",
             "correct": False,
             "why": "Total magnification is eyepiece × objective, and both come "
                    "to ×400. What differs is how much slide sits in the "
                    "circle, and the objective is what sets that."},
            {"text": "They are identical, because the two totals come to the "
                     "same number.",
             "correct": False,
             "why": "The totals match; the fields of view do not. Field of view "
                    "is the field number divided by the objective, so a ×40 "
                    "objective gives 0.45 mm and a ×10 gives 1.8 mm."},
            {"text": "B magnifies more, because a ×40 eyepiece beats a ×40 "
                     "objective.",
             "correct": False,
             "why": "An eyepiece and an objective of the same number contribute "
                    "equally to the total, and both microscopes come to ×400. "
                    "The real difference is the width of slide you see."},
            {"text": "Both come to ×400, but B shows four times more slide at "
                     "once.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b1-02-h02",
        "band": "harder",
        "text": "A student drops a coverslip flat onto a drop of pond water "
                "and at ×100 reports “dozens of round organisms with dark "
                "edges”. What is the strongest reason to doubt her?",
        "options": [
            {"text": "A coverslip laid flat traps air, and bubbles are round "
                     "with thick dark rims.",
             "correct": True},
            {"text": "Pond water does not hold anything small enough to need a "
                     "microscope.",
             "correct": False,
             "why": "It does — that is why pond water gets mounted at all. The "
                    "doubt is about what she is looking at, not about the pond: "
                    "a coverslip laid flat traps air underneath it."},
            {"text": "×100 is too low a magnification for anything living to "
                     "show up.",
             "correct": False,
             "why": "×100 shows onion cells clearly enough to count them. The "
                    "problem is not the power she used, it is the air trapped "
                    "by putting the coverslip down flat."},
            {"text": "She should have started on the ×4 objective before "
                     "climbing to ×100.",
             "correct": False,
             "why": "Starting low is the right way to find something, and she "
                    "may well have done. It still would not explain round "
                    "shapes with thick dark rims — that is what air looks "
                    "like."},
        ],
        "figure": None,
    },
    {
        "id": "b1-02-h03",
        "band": "harder",
        "text": "A slice of moss leaf is three cell layers thick. At ×40 the "
                "whole slice looks sharp. At ×400 the student says it is "
                "“blurred and broken up”. What is happening?",
        "options": [
            {"text": "The slice is too thick for light to get through it at "
                     "high power.",
             "correct": False,
             "why": "The same light gets through as at ×40 — neither the lamp "
                    "nor the slide has changed. What has changed is the "
                    "thickness of the slice in focus, which shrinks as you "
                    "climb."},
            {"text": "The lens must be dirty, because a good slide is sharp at "
                     "every magnification.",
             "correct": False,
             "why": "No slide is sharp all the way through at high power. Every "
                    "step up hands back depth as well as field of view, and at "
                    "×400 the sharp slice is thinner than one cell."},
            {"text": "Only one thin layer is in focus at a time, so the layers "
                     "behind it stay blurred.",
             "correct": True},
            {"text": "She has gone past the focus, and turning the wheel "
                     "further will sharpen it all.",
             "correct": False,
             "why": "No position of the wheel holds all three layers at ×400. "
                    "Turning it swaps one sharp layer for another — that thin "
                    "sharp slice is the depth of field."},
        ],
        "figure": None,
    },
    {
        "id": "b1-02-h04",
        "band": "harder",
        "text": "Two students draw the same kind of plant cell, and both "
                "drawings come out the same size on the paper. One has ×100 "
                "written beside it; the other has nothing. Why is only one of "
                "them a useful record?",
        "options": [
            {"text": "Neither is useful — you would need a photograph to record "
                     "a real size.",
             "correct": False,
             "why": "A drawing with the magnification written beside it is a "
                    "proper scientific record. That is exactly why the "
                    "magnification goes next to every drawing you make."},
            {"text": "Only the labelled one lets you work back to how big the "
                     "real cell was.",
             "correct": True},
            {"text": "Both are equally useful, because the two drawings came "
                     "out the same size.",
             "correct": False,
             "why": "Same size on paper does not mean same size in real life. A "
                    "cell drawn at ×400 is far smaller in reality than one "
                    "drawn the same size at ×40 — the magnification tells them "
                    "apart."},
            {"text": "Only the unlabelled one, because labels are not allowed "
                     "on a biological drawing.",
             "correct": False,
             "why": "Labels and the magnification belong on a biological "
                    "drawing. It is shading and colouring in that are left off, "
                    "because they hide the detail rather than record it."},
        ],
        "figure": None,
    },
]
