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

    # ── MRB-335 top-up ──────────────────────────────────────────────────
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "b1-02-e05",
        "band": "easier",
        "text": "What does the word specimen mean when you are using a "
                "microscope?",
        "options": [
            {"text": "The circle of light you see when you look down the "
                     "eyepiece.", "correct": False,
             "why": "That circle is the field of view. The specimen is the "
                    "thing itself — the onion skin or the pond water you have "
                    "mounted."},
            {"text": "The thing you are looking at under the microscope.",
             "correct": True},
            {"text": "The glass rectangle that the sample is mounted on.",
             "correct": False,
             "why": "That is the slide, with the coverslip over the top of "
                    "it. The specimen is the sample lying between them."},
            {"text": "The number of times bigger than real life it is being "
                     "viewed at.", "correct": False,
             "why": "That is the magnification, and it is a number rather "
                    "than a thing. The specimen is whatever you have put on "
                    "the stage."},
        ],
        "figure": None,
    },
    {
        "id": "b1-02-e06",
        "band": "easier",
        "text": "The slide has to be clipped onto the stage over the hole in "
                "the middle. Why?",
        "options": [
            {"text": "So that the clips have something solid to grip "
                     "against.", "correct": False,
             "why": "The clips grip the slide against the stage itself. The "
                    "hole is there for the light, which comes from "
                    "underneath."},
            {"text": "So that the objective cannot touch the slide as it "
                     "comes down.", "correct": False,
             "why": "The objective comes down from above and the hole is "
                    "below it. What the hole is for is the light travelling "
                    "up through the specimen."},
            {"text": "So that any spare water can drain away underneath "
                     "it.", "correct": False,
             "why": "Nothing is meant to drain anywhere — the water is held "
                    "in a thin layer under the coverslip. The hole lets the "
                    "lamp's light through."},
            {"text": "So that light from the lamp below can pass up through "
                     "the specimen.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b1-02-e07",
        "band": "easier",
        "text": "What is a coverslip?",
        "options": [
            {"text": "The thin square of glass laid over a specimen.",
             "correct": True},
            {"text": "The thick glass rectangle a specimen is mounted on.",
             "correct": False,
             "why": "That is the slide. The coverslip is the thin square that "
                    "goes on top of the specimen."},
            {"text": "The lens at the top of the microscope that you look "
                     "down.", "correct": False,
             "why": "That is the eyepiece. A coverslip is a piece of glass on "
                    "the slide, and not part of the microscope at all."},
            {"text": "The cover that keeps dust off the microscope between "
                     "lessons.", "correct": False,
             "why": "That is a dust cover. A coverslip is the thin square of "
                    "glass laid over the specimen."},
        ],
        "figure": None,
    },
    {
        "id": "b1-02-e08",
        "band": "easier",
        "text": "Light leaves the specimen and travels to your eye. Which "
                "lenses does it pass through, and in what order?",
        "options": [
            {"text": "The eyepiece first, then the objective.",
             "correct": False,
             "why": "That is the right pair in the wrong order. The objective "
                    "is the lens closest to the slide, so the light reaches "
                    "it first."},
            {"text": "The objective only — the eyepiece is a window you look "
                     "through.", "correct": False,
             "why": "The eyepiece is a lens, and it magnifies the image the "
                    "objective has made. That is why the two numbers are "
                    "multiplied together."},
            {"text": "The objective first, then the eyepiece.",
             "correct": True},
            {"text": "The eyepiece only — the objective holds the slide in "
                     "place.", "correct": False,
             "why": "The stage and its clips hold the slide. The objective is "
                    "the lens that swings round on the turret just above "
                    "it."},
        ],
        "figure": None,
    },
    {
        "id": "b1-02-e09",
        "band": "easier",
        "text": "You click round from a lower-powered objective to a "
                "higher-powered one. What happens to the field of view?",
        "options": [
            {"text": "It gets larger, because the whole image is being made "
                     "bigger.", "correct": False,
             "why": "The circle you look through stays the same size. What "
                    "changes is how much slide fits into it, and at higher "
                    "power that is less."},
            {"text": "It gets smaller, so less of the slide is in front of "
                     "you.", "correct": True},
            {"text": "It stays the same, because the eyepiece has not been "
                     "changed.", "correct": False,
             "why": "The objective is what sets the field of view. Change it "
                    "and the width of slide in the circle changes with it."},
            {"text": "It gets smaller, but only if the eyepiece is changed as "
                     "well.", "correct": False,
             "why": "The objective alone does it. Turning from the ×4 "
                    "objective to the ×40 takes the field of view from "
                    "4.5 mm to 0.45 mm."},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "b1-02-s05",
        "band": "standard",
        "text": "A microscope has a ×10 eyepiece. A student views a slide on "
                "the ×10 objective, then clicks round to the ×40. How many "
                "times more magnified is the second view?",
        "options": [
            {"text": "Thirty times more, because 40 − 10 = 30.",
             "correct": False,
             "why": "Subtracting compares the two objectives, not the two "
                    "views. Compare the totals: ×400 against ×100 is four "
                    "times."},
            {"text": "Four hundred times more, because the total is now "
                     "×400.", "correct": False,
             "why": "×400 is how much bigger than real life it looks, not how "
                    "much bigger than the last view. The first view was "
                    "already ×100, so it is 400 ÷ 100."},
            {"text": "Four times more, because ×400 is four times ×100.",
             "correct": True},
            {"text": "Ten times more, because the eyepiece is ×10.",
             "correct": False,
             "why": "The eyepiece never changed, so it cannot be what changed "
                    "the view. The objective went from ×10 to ×40, which is "
                    "four times."},
        ],
        "figure": None,
    },
    {
        "id": "b1-02-s06",
        "band": "standard",
        "text": "Onion skin is peeled away as a single layer rather than cut "
                "into a slice with a knife. Why does that matter?",
        "options": [
            {"text": "One layer lets light through and shows cells that are "
                     "not lying on top of each other.", "correct": True},
            {"text": "A knife would damage the cells, and cells that have "
                     "been damaged cannot be seen at all.", "correct": False,
             "why": "A clean cut damages very few cells, and damaged ones are "
                    "still visible. The trouble with a slice is its "
                    "thickness."},
            {"text": "The skin is the only part of an onion that is made of "
                     "cells.", "correct": False,
             "why": "Every part of the onion is made of cells. The skin is "
                    "used because it comes away one layer thick."},
            {"text": "A slice would be too small to find anywhere on the "
                     "stage.", "correct": False,
             "why": "A slice is usually easier to find, not harder. What "
                    "makes it useless is that light cannot pass cleanly "
                    "through several layers of cells."},
        ],
        "figure": None,
    },
    {
        "id": "b1-02-s07",
        "band": "standard",
        "text": "A student has hunted on the ×4 objective for a minute and "
                "found nothing. A friend tells her to turn to the ×40, "
                "because there is more to see there. Why is that bad advice?",
        "options": [
            {"text": "The ×40 objective shows less detail than the ×4, so "
                     "she would be going backwards in her "
                     "hunt.", "correct": False,
             "why": "It shows more detail, which is exactly why it is "
                    "tempting. What it does not do is help her find "
                    "anything."},
            {"text": "On the ×40 objective the image would be far too dark "
                     "for her to see anything at all in the field of "
                     "view.", "correct": False,
             "why": "The lamp still lights it. The real problem is how "
                    "little slide is in front of her, and how little of it "
                    "is in focus at once."},
            {"text": "She should change the eyepiece instead of the "
                     "objective.", "correct": False,
             "why": "The eyepiece is fixed on a school microscope, and "
                    "swapping it would not help her search. The point is to "
                    "hunt where the field of view is widest."},
            {"text": "On the ×40 she searches 0.45 mm of slide instead of "
                     "4.5 mm, so it is harder.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b1-02-s08",
        "band": "standard",
        "text": "A microscope has a ×10 eyepiece, and on the ×4 objective the "
                "field of view is 4.5 mm. The student clicks round to the ×10 "
                "objective. Which pair of numbers is right?",
        "options": [
            {"text": "Total ×20, field of view 4.5 mm.", "correct": False,
             "why": "×20 is 10 + 10, and the two lenses multiply: 10 × 10 = "
                    "×100. The field of view cannot stay the same either — a "
                    "higher objective always narrows it."},
            {"text": "Total ×100, field of view 1.8 mm.", "correct": True},
            {"text": "Total ×100, field of view 11.25 mm.", "correct": False,
             "why": "The total is right and the field of view has gone the "
                    "wrong way. Raising the magnification always shows you "
                    "less slide, never more."},
            {"text": "Total ×40, field of view 1.8 mm.", "correct": False,
             "why": "×40 was the total on the previous objective. With the "
                    "×10 objective in place the total is 10 × 10 = ×100."},
        ],
        "figure": None,
    },
    {
        "id": "b1-02-s09",
        "band": "standard",
        "text": "A dark hair-like line lies across the view. When the student "
                "slides the specimen across the stage, everything moves "
                "except that line. What is it?",
        "options": [
            {"text": "A crack in the slide, which is why it does not move "
                     "with the specimen.", "correct": False,
             "why": "A crack is in the slide, so it travels whenever the "
                    "slide does. Anything that stays put while the slide "
                    "moves is not on the slide at all."},
            {"text": "A fibre from the specimen, caught under the "
                     "coverslip.", "correct": False,
             "why": "Everything under the coverslip moves with the slide. "
                    "Something that stays still must be in the microscope, "
                    "not on it."},
            {"text": "A fibre or a hair on the eyepiece lens, with the slide "
                     "moving underneath it.", "correct": True},
            {"text": "An air bubble that has been stretched out under the "
                     "coverslip.", "correct": False,
             "why": "Bubbles are round with thick black rims, and they travel "
                    "with the slide like everything else underneath the "
                    "coverslip."},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "b1-02-h05",
        "band": "harder",
        "text": "A microscope's eyepiece has the field number 18 printed on "
                "it. With the ×40 objective clicked into place, what is the "
                "field of view?",
        "options": [
            {"text": "720 mm, because 18 × 40 = 720.", "correct": False,
             "why": "Multiplying makes the field of view grow as the "
                    "magnification grows, which is the opposite of what "
                    "happens. Divide: 18 ÷ 40 = 0.45 mm."},
            {"text": "0.045 mm, because the total magnification is ×400.",
             "correct": False,
             "why": "The field number is divided by the objective, not by the "
                    "total. 18 ÷ 40 = 0.45 mm, which is the same answer "
                    "180 ÷ 400 gives."},
            {"text": "4.5 mm, because that is where the field of view always "
                     "starts.", "correct": False,
             "why": "4.5 mm is the field of view on the ×4 objective. On the "
                    "×40 it is ten times narrower: 18 ÷ 40 = 0.45 mm."},
            {"text": "0.45 mm, because 18 ÷ 40 = 0.45.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b1-02-h06",
        "band": "harder",
        "text": "A student draws a cell 60 mm across and writes ×400 beside "
                "the drawing. How wide is the real cell?",
        "options": [
            {"text": "0.15 mm, because 60 ÷ 400 = 0.15.", "correct": True},
            {"text": "24 000 mm, because 60 × 400 = 24 000.",
             "correct": False,
             "why": "Multiplying magnifies the drawing a second time. To get "
                    "back to real life you divide by the magnification: "
                    "60 ÷ 400 = 0.15 mm."},
            {"text": "6.7 mm, because 400 ÷ 60 = 6.7.", "correct": False,
             "why": "The division is the wrong way round. The drawing is 400 "
                    "times bigger than the cell, so the cell is the drawing "
                    "divided by 400."},
            {"text": "0.15 cm, because 60 ÷ 400 = 0.15.", "correct": False,
             "why": "The number is right and the unit is not. 0.15 cm is "
                    "1.5 mm, ten times too big — the drawing was measured in "
                    "millimetres, so the answer is 0.15 mm."},
        ],
        "figure": None,
    },
    {
        "id": "b1-02-h07",
        "band": "harder",
        "text": "A student records: eyepiece ×10, objective ×40, total "
                "magnification ×400, field of view 4.5 mm. One of those four "
                "numbers cannot be right. Which?",
        "options": [
            {"text": "The total — 10 + 40 is ×50, not ×400.", "correct": False,
             "why": "The two lenses multiply, never add. ×400 is the one "
                    "number in the row that is certainly right."},
            {"text": "The objective — a ×40 objective cannot be used with a "
                     "×10 eyepiece.", "correct": False,
             "why": "That is the commonest pairing on a school microscope. "
                    "The objective is fine; it is the field of view that does "
                    "not fit."},
            {"text": "The field of view — at ×400 it is 0.45 mm, and 4.5 mm "
                     "belongs to ×40.", "correct": True},
            {"text": "The eyepiece — it would have to be ×100 for the total "
                     "to come to ×400.", "correct": False,
             "why": "10 × 40 already comes to ×400, so the eyepiece is right. "
                    "The field of view has been copied from the wrong row."},
        ],
        "figure": None,
    },
    {
        "id": "b1-02-h08",
        "band": "harder",
        "text": "A student wants to see a whole 3 mm insect leg in one view "
                "and also count the tiny hairs along it. Why can she not do "
                "both at once, and what should she do?",
        "options": [
            {"text": "She can do neither — 3 mm is far too large to go under "
                     "a microscope at all.", "correct": False,
             "why": "It sits easily on a slide, and 3 mm fits inside the "
                    "4.5 mm field of view on the lowest objective. What it "
                    "will not do is fit there at high power."},
            {"text": "At high power the field of view is narrower than the "
                     "leg, so view it whole on low power and climb to look at "
                     "parts.", "correct": True},
            {"text": "The hairs are too small to be seen at any "
                     "magnification, so she should draw the whole leg only.",
             "correct": False,
             "why": "They show up at higher power — that is what higher power "
                    "is for. The limit is how much of the leg fits in the "
                    "circle at once."},
            {"text": "She should turn the magnification up until the whole "
                     "leg and every one of the hairs along it are sharp at "
                     "the same time.", "correct": False,
             "why": "Turning it up does the opposite: every step up narrows "
                    "the field of view. There is no setting at which both are "
                    "in view."},
        ],
        "figure": None,
    },
    {
        "id": "b1-02-h09",
        "band": "harder",
        "text": "Across a field of view 4.5 mm wide, a student counts 15 "
                "onion cells lying end to end from one edge to the other. "
                "About how long is one cell?",
        "options": [
            {"text": "67.5 mm, because 4.5 × 15 = 67.5.", "correct": False,
             "why": "Multiplying makes each cell longer than the whole view. "
                    "The fifteen cells share the 4.5 mm between them, so each "
                    "one is 4.5 ÷ 15."},
            {"text": "3.3 mm, because 15 ÷ 4.5 = 3.3.", "correct": False,
             "why": "The division is the wrong way round — that is cells per "
                    "millimetre. One cell is 4.5 ÷ 15 = 0.3 mm."},
            {"text": "0.3 cm, because 4.5 ÷ 15 = 0.3.", "correct": False,
             "why": "The number is right and the unit is not. 0.3 cm is 3 mm, "
                    "ten times too long — the field of view was measured in "
                    "millimetres, so it is 0.3 mm."},
            {"text": "0.3 mm, because 4.5 ÷ 15 = 0.3.", "correct": True},
        ],
        "figure": None,
    },

    # ── MRB-338 expansion ───────────────────────────────────────────────
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "b1-02-e10",
        "band": "easier",
        "text": "What is the job of the stage on a light microscope?",
        "options": [
            {"text": "It holds the objective lenses and swings whichever one "
                     "you want into place.", "correct": False,
             "why": "That is the turret. The stage is the flat shelf "
                    "underneath, with the clips on it."},
            {"text": "It sets how many times bigger the specimen looks when it "
                     "is turned.", "correct": False,
             "why": "Magnification is set by the two lenses, not by the stage. "
                    "The stage only holds the slide still."},
            {"text": "It holds the slide still, over the hole the light comes "
                     "up through.", "correct": True},
            {"text": "It raises and lowers the lamp underneath the specimen.",
             "correct": False,
             "why": "The lamp is fixed in the base. The stage is the shelf the "
                    "slide is clipped onto above it."},
        ],
        "figure": None,
    },
    {
        "id": "b1-02-e11",
        "band": "easier",
        "text": "What does the coarse focus wheel do?",
        "options": [
            {"text": "It moves the lens and the slide closer together or "
                     "further apart.", "correct": True},
            {"text": "It makes the image brighter or dimmer as it is turned.",
             "correct": False,
             "why": "Brightness is set by the lamp underneath. The focus wheel "
                    "changes only the gap between the lens and the slide."},
            {"text": "It swaps one objective lens for the next one round on the "
                     "turret.", "correct": False,
             "why": "That is the turret, which clicks as it turns. The focus "
                    "wheel never changes which lens is in use."},
            {"text": "It magnifies the image a little more each time it is "
                     "turned.", "correct": False,
             "why": "Magnification changes only when a lens changes. Turning "
                    "the focus wheel makes the image sharper, never bigger."},
        ],
        "figure": None,
    },
    {
        "id": "b1-02-e12",
        "band": "easier",
        "text": "Which part of a light microscope is clicked round to change "
                "from one objective lens to another?",
        "options": [
            {"text": "The stage, which the slide is clipped onto over the "
                     "hole.", "correct": False,
             "why": "The stage holds the slide and does not turn. The lenses "
                    "sit on the turret just above it."},
            {"text": "The eyepiece, which is the lens at the top you look "
                     "down.", "correct": False,
             "why": "The eyepiece is fixed on a school microscope and is not "
                    "changed at all. It is the objectives that click round."},
            {"text": "The fine focus wheel, which sharpens the image at high "
                     "power.", "correct": False,
             "why": "The fine focus only shifts the lens up and down by a tiny "
                    "amount. It cannot bring a different lens into place."},
            {"text": "The turret, which carries the objectives above the "
                     "slide.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b1-02-e13",
        "band": "easier",
        "text": "A student has her cells almost sharp on the ×40 objective. "
                "Which control should she finish with?",
        "options": [
            {"text": "The coarse focus, turned as far as it will go.",
             "correct": False,
             "why": "The coarse focus moves the lens a long way, and at ×40 "
                    "there is almost no gap to give. That is how slides get "
                    "cracked."},
            {"text": "The fine focus, which moves the lens a tiny amount.",
             "correct": True},
            {"text": "The turret, clicked back one objective and then forward "
                     "again.", "correct": False,
             "why": "Clicking round changes the lens, not the sharpness. She "
                    "would only have to focus all over again."},
            {"text": "The clips, tightened down onto the slide until it stops "
                     "moving.", "correct": False,
             "why": "The clips hold the slide still, which they are already "
                    "doing. Sharpness is set by the gap between lens and "
                    "slide."},
        ],
        "figure": None,
    },
    {
        "id": "b1-02-e14",
        "band": "easier",
        "text": "What does the magnification of a microscope tell you?",
        "options": [
            {"text": "How much of the slide fits into the circle at one time.",
             "correct": False,
             "why": "That is the field of view, measured in millimetres. "
                    "Magnification is a number of times, with no unit."},
            {"text": "How thick a slice of the specimen is sharp at one time.",
             "correct": False,
             "why": "That is the depth of field. It shrinks as magnification "
                    "climbs, but it is not what magnification means."},
            {"text": "How many times bigger than real life something looks.",
             "correct": True},
            {"text": "How close two things can be and still be seen as two.",
             "correct": False,
             "why": "That is resolution — how much detail is separated. A big "
                    "magnification with poor resolution is just a bigger "
                    "blur."},
        ],
        "figure": None,
    },
    {
        "id": "b1-02-e15",
        "band": "easier",
        "text": "A microscope has a ×10 eyepiece. The ×4 objective is clicked "
                "into place. What is the total magnification?",
        "options": [
            {"text": "×14, because 10 + 4 = 14.", "correct": False,
             "why": "Adding is the commonest mistake here. The objective makes "
                    "an image and the eyepiece magnifies that image again, so "
                    "the two multiply: 10 × 4 = ×40."},
            {"text": "×40, because 10 × 4 = 40.", "correct": True},
            {"text": "×10, because the eyepiece is the lens you look down.",
             "correct": False,
             "why": "The eyepiece is only half of it. Whatever the objective "
                    "has already done gets magnified again by the eyepiece."},
            {"text": "×4, because the objective is the lens nearest the "
                     "specimen.", "correct": False,
             "why": "The objective is only half of it. Its image goes on to be "
                    "magnified by the eyepiece, so the total is 10 × 4 = ×40."},
        ],
        "figure": None,
    },
    {
        "id": "b1-02-e16",
        "band": "easier",
        "text": "Which of these is the right way to record a magnification of "
                "four hundred times?",
        "options": [
            {"text": "400 mm, a length in millimetres.", "correct": False,
             "why": "Millimetres measure the field of view, not how much "
                    "bigger something looks. Magnification carries no unit at "
                    "all."},
            {"text": "×400, a number of times bigger.", "correct": True},
            {"text": "400 cm, a length in centimetres.", "correct": False,
             "why": "Centimetres are a length as well, and the answer is not a "
                    "length. ×400 means four hundred times bigger than real "
                    "life."},
            {"text": "×400 mm, a number of times and a length.", "correct": False,
             "why": "The number is right and the millimetres do not belong. "
                    "Nothing goes after the number when you write a "
                    "magnification."},
        ],
        "figure": None,
    },
    {
        "id": "b1-02-e17",
        "band": "easier",
        "text": "Why is the lowest-power objective the one you turn in first?",
        "options": [
            {"text": "Because it is the only objective that will never touch "
                     "the slide.", "correct": False,
             "why": "No objective should ever touch the slide, whichever one is "
                    "in. You start low because it shows you the most slide to "
                    "search."},
            {"text": "Because the higher-power lenses only work once something "
                     "is already sharp.", "correct": False,
             "why": "They work whenever you use them. The trouble is finding "
                    "anything at high power, with so little slide in front of "
                    "you."},
            {"text": "Because the lower power shows the true colours of the "
                     "specimen.", "correct": False,
             "why": "Magnification does not change colour. It changes how much "
                    "slide you can see, and low power shows the most."},
            {"text": "Because it shows the widest piece of slide, so there is "
                     "most to find.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b1-02-e18",
        "band": "easier",
        "text": "Watching from the side, the objective has been brought down "
                "until it nearly touches the slide. Which way is the focus "
                "wheel turned now?",
        "options": [
            {"text": "Downwards, slowly, until the image comes into view.",
             "correct": False,
             "why": "There is no room left to go down. Focusing downwards from "
                    "here is exactly how the lens meets the glass."},
            {"text": "Downwards first and then upwards, so the focus is passed "
                     "twice.", "correct": False,
             "why": "Passing through it downwards means passing through the "
                    "glass. From nearly touching, the only safe direction is "
                    "away."},
            {"text": "Upwards, so the lens moves away from the slide.",
             "correct": True},
            {"text": "Neither — the slide is lifted up onto the lens instead.",
             "correct": False,
             "why": "The slide stays clipped to the stage. The focus wheel "
                    "moves the lens away, and the image sharpens on the way "
                    "up."},
        ],
        "figure": None,
    },
    {
        "id": "b1-02-e19",
        "band": "easier",
        "text": "A student focuses downwards while looking down the eyepiece. "
                "What is most likely to happen?",
        "options": [
            {"text": "The image goes dark, because the lens blocks the lamp "
                     "below.", "correct": False,
             "why": "The light comes up from underneath and the lens is above. "
                    "What actually happens is the lens reaching the glass."},
            {"text": "The objective is driven into the slide and cracks it.",
             "correct": True},
            {"text": "The magnification climbs as the lens gets closer to the "
                     "specimen.", "correct": False,
             "why": "Magnification is set by the two lenses and by nothing "
                    "else. Moving the lens closer changes the focus, not the "
                    "size."},
            {"text": "The slide slips out from under the clips and off the "
                     "stage.", "correct": False,
             "why": "The clips hold the slide down against the stage. The risk "
                    "from focusing downwards is the lens meeting the glass."},
        ],
        "figure": None,
    },
    {
        "id": "b1-02-e20",
        "band": "easier",
        "text": "How should a coverslip be put onto a drop of water on a "
                "slide?",
        "options": [
            {"text": "Dropped flat onto the drop from just above it.",
             "correct": False,
             "why": "Flat is what traps the air. Bubbles are round with thick "
                    "black rims, and they get drawn as cells every year."},
            {"text": "Pressed down hard so that the water spreads to the "
                     "edges.", "correct": False,
             "why": "Pressing hard cracks the coverslip and squashes the "
                    "specimen. The water spreads on its own as the glass comes "
                    "down."},
            {"text": "Slid flat across the slide from one end to the other.",
             "correct": False,
             "why": "Sliding drags the specimen out of place and still traps "
                    "air. Rest one edge down and lower the rest slowly."},
            {"text": "Rested on one edge, then lowered slowly onto the drop.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b1-02-e21",
        "band": "easier",
        "text": "Why is a stain such as iodine solution added to a slide?",
        "options": [
            {"text": "To make parts that are almost colourless show up "
                     "clearly against the rest.", "correct": True},
            {"text": "To magnify the parts of the cell that are too small to be "
                     "seen.", "correct": False,
             "why": "A stain changes colour, never size. Anything too small for "
                    "the lens stays too small however dark it is made."},
            {"text": "To hold the coverslip down onto the specimen "
                     "underneath.", "correct": False,
             "why": "The thin layer of liquid already holds the coverslip "
                    "down. A stain is added for contrast, so parts can be told "
                    "apart."},
            {"text": "To stop the water on the slide drying out under the "
                     "lamp.", "correct": False,
             "why": "A stain does not stop anything drying. It colours some "
                    "parts of the cell more than others, so they stand out."},
        ],
        "figure": None,
    },
    {
        "id": "b1-02-e22",
        "band": "easier",
        "text": "A drop of stain is placed at one edge of the coverslip. How is "
                "it drawn underneath?",
        "options": [
            {"text": "By pressing down on the middle of the coverslip.",
             "correct": False,
             "why": "Pressing on a coverslip cracks it and squashes what is "
                    "underneath. A piece of paper towel pulls the stain "
                    "through instead."},
            {"text": "By tilting the whole slide until the stain runs "
                     "underneath it.", "correct": False,
             "why": "Tilting runs the stain off the edge of the slide rather "
                    "than under the glass. Paper towel at the far edge draws it "
                    "through evenly."},
            {"text": "By touching paper towel to the opposite edge.",
             "correct": True},
            {"text": "By adding more and more stain until it flows under by "
                     "itself.", "correct": False,
             "why": "Extra stain floods the slide and darkens everything, "
                    "which hides the detail. One drop, drawn through with "
                    "paper towel, is enough."},
        ],
        "figure": None,
    },
    {
        "id": "b1-02-e23",
        "band": "easier",
        "text": "What does the depth of field mean?",
        "options": [
            {"text": "The thickness of specimen that is sharp at one time.",
             "correct": True},
            {"text": "The distance from the objective lens down to the slide "
                     "below it.", "correct": False,
             "why": "That is the gap the focus wheel sets. The depth of field "
                    "is how much of the specimen’s thickness is sharp at "
                    "once."},
            {"text": "The width of slide you can see down the eyepiece at "
                     "once.", "correct": False,
             "why": "That is the field of view — a measurement across the "
                    "slide. The depth of field is measured through it "
                    "instead."},
            {"text": "How deep the drop of water under the coverslip is.",
             "correct": False,
             "why": "The drop can be any depth you like. The depth of field is "
                    "how thick a slice of it the lens holds sharp."},
        ],
        "figure": None,
    },
    {
        "id": "b1-02-e24",
        "band": "easier",
        "text": "A student pushes the slide to the left. Which way does the "
                "image appear to move?",
        "options": [
            {"text": "To the left, the same way as the slide.", "correct": False,
             "why": "The lenses turn the image upside down and back to front, "
                    "so it always moves the opposite way to the slide."},
            {"text": "It stays still, and only becomes blurred.",
             "correct": False,
             "why": "Moving the slide moves what you see. Because the image is "
                    "inverted, it travels the opposite way — to the right."},
            {"text": "Upwards, because the lenses turn the image on its side.",
             "correct": False,
             "why": "The image is turned right round, not through a quarter "
                    "turn. A slide pushed left gives an image that moves "
                    "right."},
            {"text": "To the right, the opposite way to the slide.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b1-02-e25",
        "band": "easier",
        "text": "What happens to how bright the view looks as you climb to a "
                "higher-power objective?",
        "options": [
            {"text": "It gets brighter, because the lamp is closer to the "
                     "lens.", "correct": False,
             "why": "The lamp does not move at all. The higher lens takes its "
                    "light from a much smaller patch of slide, so the view "
                    "dims."},
            {"text": "It gets dimmer, so more light is usually needed to "
                     "see well.", "correct": True},
            {"text": "It stays the same, because the lamp is set to one "
                     "brightness.", "correct": False,
             "why": "The lamp is unchanged, but the view is not. Less slide is "
                    "lit into the same circle, so what you see is dimmer."},
            {"text": "It flickers, because less of the slide is over the lamp "
                     "below.", "correct": False,
             "why": "Nothing flickers — the light is steady. It is simply "
                    "dimmer, because it is gathered from a smaller patch of "
                    "slide."},
        ],
        "figure": None,
    },
    {
        "id": "b1-02-e26",
        "band": "easier",
        "text": "Which shows smaller detail: a school light microscope, or an "
                "electron microscope?",
        "options": [
            {"text": "The light microscope, because light travels faster than "
                     "electrons do.", "correct": False,
             "why": "Speed is not what decides it. An electron microscope "
                    "separates far smaller detail than any light microscope "
                    "can."},
            {"text": "Neither — they show the same detail at the same "
                     "magnification.", "correct": False,
             "why": "Magnification and detail are not the same thing. At the "
                    "same magnification the electron image still shows far "
                    "more."},
            {"text": "The electron microscope, which separates detail far "
                     "smaller than light can reach.", "correct": True},
            {"text": "It depends on which eyepiece has been fitted to each of "
                     "them.", "correct": False,
             "why": "An electron microscope has no eyepiece lens of that kind. "
                    "It separates far smaller detail whatever a light "
                    "microscope is fitted with."},
        ],
        "figure": None,
    },
    {
        "id": "b1-02-e27",
        "band": "easier",
        "text": "What does the resolution of a microscope mean?",
        "options": [
            {"text": "How close two things can be and still be seen as two.",
             "correct": True},
            {"text": "How many times bigger than real life the image looks.",
             "correct": False,
             "why": "That is magnification. Magnifying a blur only gives you a "
                    "bigger blur — resolution is what separates the detail."},
            {"text": "How much of the slide fits into the view at one time.",
             "correct": False,
             "why": "That is the field of view, measured in millimetres. "
                    "Resolution is about telling two close things apart."},
            {"text": "How bright the image is when the lamp is turned right "
                     "up.", "correct": False,
             "why": "Brightness helps you see, but it does not separate two "
                    "things that are very close together. That is resolution."},
        ],
        "figure": None,
    },
    {
        "id": "b1-02-e28",
        "band": "easier",
        "text": "How should a microscope be carried across the laboratory?",
        "options": [
            {"text": "By the eyepiece, which is the easiest part to take hold "
                     "of.", "correct": False,
             "why": "The eyepiece lifts straight out of its tube, and the rest "
                    "would drop. Carry it by the base and the arm."},
            {"text": "By the stage, with the slide left clipped in place.",
             "correct": False,
             "why": "The stage is not made to take the weight, and the slide "
                    "should come off first. One hand under the base, one on the "
                    "arm."},
            {"text": "By the two focus wheels, one in each hand.",
             "correct": False,
             "why": "The focus wheels turn, so they cannot hold the weight "
                    "steadily. The arm is the part shaped to be gripped."},
            {"text": "With one hand under the base and one on the arm.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b1-02-e29",
        "band": "easier",
        "text": "There is a fingerprint on an objective lens. What should it be "
                "cleaned with?",
        "options": [
            {"text": "A paper towel, rubbed hard until the mark has gone.",
             "correct": False,
             "why": "Paper towel is rough enough to scratch the glass, and a "
                    "scratched lens is ruined. Lens tissue is made for the "
                    "job."},
            {"text": "Lens tissue, wiped gently across the glass.",
             "correct": True},
            {"text": "Water from the tap, then left to dry on the bench.",
             "correct": False,
             "why": "Water gets inside the lens housing and dries leaving "
                    "marks. A gentle wipe with lens tissue is all that is "
                    "needed."},
            {"text": "A jumper sleeve, which is soft enough to do no harm.",
             "correct": False,
             "why": "A sleeve carries grit, and grit scratches. Lens tissue is "
                    "kept beside the microscopes for exactly this."},
        ],
        "figure": None,
    },
    {
        "id": "b1-02-e30",
        "band": "easier",
        "text": "A specimen has to be mounted on something before it goes onto "
                "the stage. What is that piece of glass called?",
        "options": [
            {"text": "The coverslip, which is the thin square laid on top of "
                     "the specimen.", "correct": False,
             "why": "The coverslip goes over the specimen. The piece it is "
                    "mounted on underneath is the slide."},
            {"text": "The stage, which is the shelf the clips are fixed to.",
             "correct": False,
             "why": "The stage is part of the microscope and is not made of "
                    "glass. The specimen goes onto a slide, which is clipped "
                    "to it."},
            {"text": "The slide, which is the long rectangle of glass a "
                     "specimen is mounted onto.", "correct": True},
            {"text": "The lens, which the specimen is placed directly onto.",
             "correct": False,
             "why": "Nothing is ever placed onto a lens. The specimen goes on a "
                    "slide, which sits on the stage below the lens."},
        ],
        "figure": None,
    },
    {
        "id": "b1-02-e31",
        "band": "easier",
        "text": "You click round from the ×4 objective to the ×10. What do you "
                "nearly always have to do next?",
        "options": [
            {"text": "Refocus, because the image will not be sharp any more.",
             "correct": True},
            {"text": "Make a new slide, because this one has now been used "
                     "up.", "correct": False,
             "why": "A slide can be looked at on every objective in turn. What "
                    "changes when you click round is the focus."},
            {"text": "Change the eyepiece so that it matches the new "
                     "objective.", "correct": False,
             "why": "The eyepiece is fixed on a school microscope and never "
                    "needs matching. The focus, though, has to be reset."},
            {"text": "Take the clips off so that the slide can be moved "
                     "freely.", "correct": False,
             "why": "The clips stay on, or the slide will drift. It is the "
                    "focus that has to be adjusted after every change of "
                    "lens."},
        ],
        "figure": None,
    },
    {
        "id": "b1-02-e32",
        "band": "easier",
        "text": "Before climbing to a higher-power objective, where should the "
                "thing you want to look at be?",
        "options": [
            {"text": "At the edge of the view, so there is room for it to grow "
                     "inwards.", "correct": False,
             "why": "Nothing grows inwards — the view narrows around the "
                    "middle. Anything at the edge is the first thing to fall "
                    "outside it."},
            {"text": "In the middle of the view, so that it stays there as "
                     "you climb.", "correct": True},
            {"text": "Anywhere in the view, because the higher power will find "
                     "it again.", "correct": False,
             "why": "The higher power searches nothing for you — it just shows "
                    "less slide. What was off to one side ends up outside the "
                    "view."},
            {"text": "Just outside the view, so the lens has a clear path "
                     "down.", "correct": False,
             "why": "The lens comes nowhere near what you are looking at. Put "
                    "what you want in the middle, then climb."},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "b1-02-s10",
        "band": "standard",
        "text": "A results sheet records a total of ×600 with the ×40 objective "
                "in use. Which eyepiece was fitted?",
        "options": [
            {"text": "×640, because the two lenses are added together.",
             "correct": False,
             "why": "They multiply, not add — that is what makes the total. To "
                    "come back from the total you divide: 600 ÷ 40 = ×15."},
            {"text": "×560, because 600 − 40 = 560.", "correct": False,
             "why": "Subtracting undoes adding, and these two were multiplied. "
                    "Divide instead: 600 ÷ 40 = ×15."},
            {"text": "×15, because 600 ÷ 40 = 15.", "correct": True},
            {"text": "×24 000, because 600 × 40 = 24 000.", "correct": False,
             "why": "Multiplying takes you forwards, from the two lenses to the "
                    "total. You already have the total, so divide back down to "
                    "×15."},
        ],
        "figure": None,
    },
    {
        "id": "b1-02-s11",
        "band": "standard",
        "text": "On the ×10 objective the view is 1.8 mm across. Onion cells "
                "are about 0.3 mm long. About how many fit end to end across "
                "it?",
        "options": [
            {"text": "6, because 1.8 ÷ 0.3 = 6.", "correct": True},
            {"text": "0.54, because 1.8 × 0.3 = 0.54.", "correct": False,
             "why": "Multiplying two lengths counts nothing. Ask how many "
                    "0.3 mm lengths fit inside 1.8 mm: 1.8 ÷ 0.3 = 6."},
            {"text": "18, because 1.8 mm is 18 lots of 0.1 mm.", "correct": False,
             "why": "That counts tenths of a millimetre, not cells. Each cell "
                    "is three of those tenths, so only 6 fit."},
            {"text": "0.17, because 0.3 ÷ 1.8 = 0.17.", "correct": False,
             "why": "That is the fraction of the view one cell fills, not the "
                    "number of cells. Turn the division round: 1.8 ÷ 0.3 = 6."},
        ],
        "figure": None,
    },
    {
        "id": "b1-02-s12",
        "band": "standard",
        "text": "A cell is 0.2 mm long in real life. How long will it look in a "
                "drawing made at ×100?",
        "options": [
            {"text": "0.002 mm, because 0.2 ÷ 100 = 0.002.", "correct": False,
             "why": "Dividing takes you from the drawing back to real life. "
                    "Going the other way you multiply: 0.2 × 100 = 20 mm."},
            {"text": "100.2 mm, because the magnification is added on.",
             "correct": False,
             "why": "Magnification multiplies a length, it does not add to it. "
                    "0.2 × 100 = 20 mm."},
            {"text": "2 mm, because 0.2 × 10 = 2.", "correct": False,
             "why": "A power of ten has gone missing. The magnification is "
                    "×100, not ×10, so the drawing is 20 mm across."},
            {"text": "20 mm, because 0.2 × 100 = 20.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b1-02-s13",
        "band": "standard",
        "text": "Lowering a coverslip slowly from one edge keeps the air out. "
                "Explain why that works.",
        "options": [
            {"text": "The angle makes the drop of water spread right out before "
                     "the glass ever touches it.", "correct": False,
             "why": "The water spreads because the glass presses it out, not "
                    "beforehand. What the angle does is give the air one way "
                    "out."},
            {"text": "The water touches one edge of the glass first and "
                     "pushes the air out ahead of it.", "correct": True},
            {"text": "The raised edge of the coverslip is warmer, so the air "
                     "rises away from underneath it.", "correct": False,
             "why": "Nothing here is warm enough for that to matter. The air "
                    "leaves because the advancing water sweeps it out."},
            {"text": "The tilted coverslip lets any spare water run off the end "
                     "of the slide first.", "correct": False,
             "why": "Spare water is mopped up afterwards with paper towel. The "
                    "angle is about the air, which is driven out ahead of the "
                    "water."},
        ],
        "figure": None,
    },
    {
        "id": "b1-02-s14",
        "band": "standard",
        "text": "Explain why the view gets dimmer every time you climb to a "
                "higher-power objective.",
        "options": [
            {"text": "The lamp dims by itself whenever a higher-power objective "
                     "is clicked in.", "correct": False,
             "why": "Nothing about the lamp changes when the turret turns. What "
                    "changes is how much slide the lens is gathering light "
                    "from."},
            {"text": "The high-power lens is made of much thicker glass, and "
                     "thick glass absorbs most of the light going through it.",
             "correct": False,
             "why": "Lens glass is clear and absorbs very little. The dimming "
                    "comes from gathering light off a far smaller patch of "
                    "slide."},
            {"text": "Light is gathered from a much smaller patch of slide "
                     "and spread across the same circle.", "correct": True},
            {"text": "The lens sits closer to the slide, so it blocks some of "
                     "the light coming up.", "correct": False,
             "why": "The light comes up through the specimen and into the lens, "
                    "so being close does not block it. The lit patch is simply "
                    "smaller."},
        ],
        "figure": None,
    },
    {
        "id": "b1-02-s15",
        "band": "standard",
        "text": "The cell you want is at the right-hand edge of the view. Which "
                "way should the slide be moved to bring it into the middle?",
        "options": [
            {"text": "To the right, because the image moves the opposite way.",
             "correct": True},
            {"text": "To the left, because whatever you see travels in the same "
                     "direction as the slide.", "correct": False,
             "why": "The image is upside down and back to front, so it travels "
                    "the opposite way. Move the slide right and the cell comes "
                    "left into the middle."},
            {"text": "Not at all — turning the fine focus will bring it in "
                     "instead.", "correct": False,
             "why": "The focus changes sharpness, never position. Only moving "
                    "the slide moves what is in the view."},
            {"text": "To the left first and then to the right, to settle it in "
                     "the centre.", "correct": False,
             "why": "Going left takes it further out of the view. One movement, "
                    "to the right, brings it in."},
        ],
        "figure": None,
    },
    {
        "id": "b1-02-s16",
        "band": "standard",
        "text": "A student floods her slide with iodine solution. What is she "
                "likely to see?",
        "options": [
            {"text": "Nothing at all, because iodine dissolves the cell walls "
                     "as it soaks into them.", "correct": False,
             "why": "Iodine dissolves nothing. Too much of it simply darkens "
                    "everything until the detail cannot be picked out."},
            {"text": "Brighter cells, because the extra colour makes the detail "
                     "stand out more.", "correct": False,
             "why": "More stain is not more contrast. Past a point every part "
                    "goes the same dark colour and the differences vanish."},
            {"text": "A clear view, because the coverslip squeezes the extra "
                     "stain out at the edges.", "correct": False,
             "why": "The coverslip traps the liquid rather than squeezing it "
                    "away. The view goes dark, not clear."},
            {"text": "A dark orange-brown view, with the detail lost inside "
                     "a colour that is the same everywhere.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b1-02-s17",
        "band": "standard",
        "text": "Two students compare the length of cells from two different "
                "onions. Why must both slides be viewed at the same total "
                "magnification?",
        "options": [
            {"text": "Because a change of magnification would put one of the "
                     "two slides out of focus for good.", "correct": False,
             "why": "Either slide can be refocused on any objective. The "
                    "problem is that a higher magnification makes cells look "
                    "bigger without being bigger."},
            {"text": "Because a cell looks bigger at a higher magnification "
                     "without being bigger.", "correct": True},
            {"text": "Because a stain only works properly at one "
                     "magnification.", "correct": False,
             "why": "A stain works the same whatever lens is in. It is the "
                    "apparent size that changes with magnification, which is "
                    "what has to be kept the same."},
            {"text": "Because cells from two different onions can only be "
                     "compared if both slides were made on the same day.",
             "correct": False,
             "why": "The day makes no difference to a mounted slide. The "
                    "magnification does, because it sets how big everything "
                    "looks."},
        ],
        "figure": None,
    },
    {
        "id": "b1-02-s18",
        "band": "standard",
        "text": "Which order of steps sets a microscope up properly?",
        "options": [
            {"text": "Clip the slide on · turn to the ×40 for the most detail · "
                     "focus downwards while looking down the eyepiece.",
             "correct": False,
             "why": "Two faults: the hunt starts on the lowest power, and "
                    "focusing downwards from the eyepiece is how slides get "
                    "cracked."},
            {"text": "Turn to the ×4 · focus down while looking down the "
                     "eyepiece · then clip the slide onto the stage.",
             "correct": False,
             "why": "Focusing before the slide is on gives you nothing to focus "
                    "on. Clip it down first, then bring the lens close from the "
                    "side."},
            {"text": "Clip the slide on · turn to the ×4 · lower the lens from "
                     "the side · focus upwards.", "correct": True},
            {"text": "Turn to the ×40 · clip the slide on · focus upwards until "
                     "something appears.", "correct": False,
             "why": "Focusing upwards is right, but starting at ×40 leaves only "
                    "0.45 mm of slide to search. Find it at ×4 and climb."},
        ],
        "figure": None,
    },
    {
        "id": "b1-02-s19",
        "band": "standard",
        "text": "A student has onion cells sharp on the ×4 objective. She "
                "clicks to the ×40 and the view is empty. Suggest why.",
        "options": [
            {"text": "The ×40 objective is too powerful to show onion cells at "
                     "all.", "correct": False,
             "why": "×40 with a ×10 eyepiece gives ×400, which shows onion "
                    "cells clearly. The view is empty because the cells are "
                    "outside it."},
            {"text": "The lamp is not bright enough for the ×40 objective to "
                     "work properly.", "correct": False,
             "why": "A dim view still shows shapes. An empty one means the "
                    "cells have fallen outside a view that is now ten times "
                    "narrower."},
            {"text": "The slide has to be turned over before a higher-power "
                     "objective will focus.", "correct": False,
             "why": "A slide is never turned over — the coverslip would fall "
                    "off. What matters is where the cells sat before she "
                    "climbed."},
            {"text": "The cells were not in the middle, so they now sit outside "
                     "a much narrower view.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b1-02-s20",
        "band": "standard",
        "text": "Why should the coarse focus never be used once the ×40 "
                "objective is in place?",
        "options": [
            {"text": "There is so little room under it that a small turn drives "
                     "it into the slide.", "correct": True},
            {"text": "It would change the total magnification away from ×400.",
             "correct": False,
             "why": "The focus wheel never changes magnification. The reason to "
                    "leave it alone at ×40 is the tiny gap above the glass."},
            {"text": "It only works when the lowest-power objective is clicked "
                     "in.", "correct": False,
             "why": "It works on every objective, which is the danger. On ×40 "
                    "there is barely any gap for it to move through."},
            {"text": "It moves the stage from side to side rather than up and "
                     "down at high power.", "correct": False,
             "why": "The focus wheel only ever changes the gap between lens and "
                    "slide. At ×40 that gap is almost nothing."},
        ],
        "figure": None,
    },
    {
        "id": "b1-02-s21",
        "band": "standard",
        "text": "Why is a specimen mounted in a drop of water rather than laid "
                "on a dry slide?",
        "options": [
            {"text": "Water magnifies the specimen a little before the lenses "
                     "reach it.", "correct": False,
             "why": "A thin layer of water does not magnify anything usefully. "
                    "It holds the specimen flat and stops it drying out."},
            {"text": "It holds the specimen flat and stops it drying and "
                     "shrivelling.", "correct": True},
            {"text": "Water makes the specimen thicker, so that it is easier to "
                     "find on the stage.", "correct": False,
             "why": "Thicker is worse, not better — light has to get through. "
                    "The water is there to keep the specimen flat and moist."},
            {"text": "Water washes away anything on the slide that is not part "
                     "of a cell.", "correct": False,
             "why": "The water washes nothing away under a coverslip. It "
                    "spreads the specimen into a thin flat layer and keeps it "
                    "from drying."},
        ],
        "figure": None,
    },
    {
        "id": "b1-02-s22",
        "band": "standard",
        "text": "A student cuts the letter e out of a newspaper, mounts it, and "
                "looks at it on the ×4 objective. What does she see?",
        "options": [
            {"text": "An e the right way up, only much bigger.",
             "correct": False,
             "why": "The lenses turn the image right round. It comes out upside "
                    "down and back to front as well as bigger."},
            {"text": "An e lying on its side.", "correct": False,
             "why": "That is a quarter turn. The microscope turns the image "
                    "through a half turn, so it is upside down and back to "
                    "front."},
            {"text": "An e upside down and back to front.", "correct": True},
            {"text": "An e the right way up but back to front.",
             "correct": False,
             "why": "Half the change is missing. The image is reversed both "
                    "ways at once, which is why the slide seems to move "
                    "backwards."},
        ],
        "figure": None,
    },
    {
        "id": "b1-02-s23",
        "band": "standard",
        "text": "Why is a specimen mounted as a thin layer under a coverslip "
                "rather than in a deep drop of water?",
        "options": [
            {"text": "A deep drop would spill off the slide as soon as the "
                     "stage was moved.", "correct": False,
             "why": "A coverslip holds the liquid in place. The reason for a "
                    "thin layer is that only a thin slice is ever sharp, and "
                    "light gets through it cleanly."},
            {"text": "Only a thin slice is sharp at once, and light gets "
                     "through cleanly.", "correct": True},
            {"text": "A deep drop would magnify the specimen more than the "
                     "lenses are set to.", "correct": False,
             "why": "Water does not add magnification. Depth costs you "
                    "sharpness and light, which is why the layer is kept "
                    "thin."},
            {"text": "A deep drop would be too heavy for the stage clips to "
                     "hold in place.", "correct": False,
             "why": "A drop of water weighs almost nothing. The trouble with "
                    "depth is that most of it lies outside the sharp slice."},
        ],
        "figure": None,
    },
    {
        "id": "b1-02-s24",
        "band": "standard",
        "text": "A student writes “×4.5” in the field-of-view column of her "
                "results table. What is wrong with it?",
        "options": [
            {"text": "Nothing at all — a field of view is recorded as a number "
                     "of times, like a magnification.", "correct": False,
             "why": "A field of view is a width across the slide, so it is a "
                    "length. The × sign belongs to magnification, which has no "
                    "unit."},
            {"text": "The number is wrong: no school microscope shows anything "
                     "at ×4.5.", "correct": False,
             "why": "The number 4.5 is fine — it is the width in millimetres on "
                    "the lowest objective. It is the × in front of it that does "
                    "not belong."},
            {"text": "It should read 4.5 with nothing after it, because units "
                     "are never written in a table.", "correct": False,
             "why": "Units always belong with the measurement, usually in the "
                    "column heading. The fault is the × sign, not the unit."},
            {"text": "A field of view is a width across the slide, so it is "
                     "a length: 4.5 mm.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b1-02-s25",
        "band": "standard",
        "text": "On the ×4 objective the view is so bright that the cells look "
                "washed out. What should be changed?",
        "options": [
            {"text": "Turn the lamp down, or close the diaphragm until the "
                     "detail comes back.", "correct": True},
            {"text": "Turn the fine focus slowly until the brightness settles "
                     "down.", "correct": False,
             "why": "The focus changes sharpness, not brightness. The light "
                    "itself is what has to come down."},
            {"text": "Click round to the ×40 objective and then back to the ×4 "
                     "again.", "correct": False,
             "why": "You would come back to exactly the same bright view. The "
                    "light needs turning down at the lamp or the diaphragm."},
            {"text": "Lay a second coverslip on top of the first to cut the "
                     "light down.", "correct": False,
             "why": "Extra glass adds reflections and pushes the specimen out "
                    "of focus. The lamp and the diaphragm are the controls for "
                    "brightness."},
        ],
        "figure": None,
    },
    {
        "id": "b1-02-s26",
        "band": "standard",
        "text": "Suggest why school laboratories use light microscopes rather "
                "than electron microscopes.",
        "options": [
            {"text": "Light microscopes separate far smaller detail than any "
                     "electron microscope can.", "correct": False,
             "why": "It is the other way round. Electron microscopes are kept "
                    "out of schools by their size, their cost and the "
                    "preparation they need."},
            {"text": "Electron microscopes cannot magnify enough for cells to "
                     "be seen at all.", "correct": False,
             "why": "They magnify far more than a light microscope. What rules "
                    "them out of a school is cost, size and the fact that the "
                    "specimen cannot be alive."},
            {"text": "They are huge, very expensive, and cannot show living "
                     "specimens.", "correct": True},
            {"text": "Electron microscopes give a full-colour image, which "
                     "schools have no use for.", "correct": False,
             "why": "Electron images are not in natural colour at all — any "
                    "colour has been added afterwards. The barriers are cost, "
                    "size and preparation."},
        ],
        "figure": None,
    },
    {
        "id": "b1-02-s27",
        "band": "standard",
        "text": "Two microscopes both give ×400. On one the cell wall shows as "
                "two clear lines; on the other it is a single thick smudge. "
                "What differs?",
        "options": [
            {"text": "Their magnification, because ×400 can mean different "
                     "things on different microscopes.", "correct": False,
             "why": "×400 means the same on both — four hundred times bigger. "
                    "What differs is how close two lines can be and still be "
                    "told apart."},
            {"text": "Their resolution — how close two things can be and still "
                     "be told apart.", "correct": True},
            {"text": "Their field of view, which must be wider on the clearer "
                     "one.", "correct": False,
             "why": "The field of view is how much slide you see, not how "
                    "sharply you see it. Detail is a question of resolution."},
            {"text": "Their depth of field, which must be deeper on the clearer "
                     "one.", "correct": False,
             "why": "Depth of field decides how much thickness is sharp at "
                    "once, not whether two lines can be separated at all."},
        ],
        "figure": None,
    },
    {
        "id": "b1-02-s28",
        "band": "standard",
        "text": "A student has no scale on her microscope but knows the view is "
                "4.5 mm across. How can she estimate the length of one cell?",
        "options": [
            {"text": "Measure the cell on her drawing with a ruler and record "
                     "that measurement.", "correct": False,
             "why": "That measures the drawing, which is hundreds of times too "
                    "big. Counting cells across a known width gives the real "
                    "length."},
            {"text": "Multiply 4.5 mm by the number of cells she can count "
                     "across the view.", "correct": False,
             "why": "Multiplying makes each cell longer than the whole view. "
                    "The cells share the 4.5 mm between them, so divide."},
            {"text": "Measure the width of the eyepiece lens and divide it by "
                     "the magnification.", "correct": False,
             "why": "The eyepiece's width is not what you are seeing. Use the "
                    "width of slide in view and how many cells fit across it."},
            {"text": "Count how many cells fit across the view and divide "
                     "4.5 mm by that number.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b1-02-s29",
        "band": "standard",
        "text": "Explain why the image has to be refocused every time you click "
                "to a higher-power objective.",
        "options": [
            {"text": "The new lens sits at a different height, and keeps a much "
                     "thinner slice sharp.", "correct": True},
            {"text": "The slide shifts slightly in the clips whenever the "
                     "turret is turned round.", "correct": False,
             "why": "The clips hold the slide still. What has changed is the "
                    "lens above it — a different height, and a far thinner "
                    "sharp slice."},
            {"text": "The eyepiece changes at the same moment as the objective "
                     "does.", "correct": False,
             "why": "The eyepiece is fixed and does not change at all. The new "
                    "objective sits at its own height and holds less depth in "
                    "focus."},
            {"text": "The lamp needs a moment to settle at its new brightness "
                     "level.", "correct": False,
             "why": "The lamp is unchanged, and brightness is not sharpness. "
                    "The focus goes because the new lens focuses at a different "
                    "height."},
        ],
        "figure": None,
    },
    {
        "id": "b1-02-s30",
        "band": "standard",
        "text": "A dark speck sits in the view. How can a student tell whether "
                "it is on the slide or on the eyepiece lens?",
        "options": [
            {"text": "Turn the fine focus: a speck on the slide will disappear "
                     "altogether.", "correct": False,
             "why": "Focusing blurs a speck on the slide but does not remove "
                    "it. Turning the eyepiece is the test — the speck turns "
                    "with it or it does not."},
            {"text": "Change the objective: a speck on the eyepiece will vanish "
                     "when the lens changes.", "correct": False,
             "why": "A speck on the eyepiece survives every objective, because "
                    "it is above them all. Rotate the eyepiece instead and "
                    "watch whether it turns."},
            {"text": "Rotate the eyepiece: a speck sitting on that lens "
                     "turns round with it.", "correct": True},
            {"text": "Turn the lamp up: a speck on the slide will be lit from "
                     "behind and disappear.", "correct": False,
             "why": "More light darkens nothing. The only test that separates "
                    "the two is whether the speck moves with the eyepiece or "
                    "with the slide."},
        ],
        "figure": None,
    },
    {
        "id": "b1-02-s31",
        "band": "standard",
        "text": "Why should only a small drop of pond water be put onto the "
                "slide?",
        "options": [
            {"text": "A big drop would be too heavy for the stage clips to hold "
                     "steady.", "correct": False,
             "why": "Weight is not the problem — a drop weighs almost nothing. "
                    "Depth is, because so little of it can be sharp at once."},
            {"text": "A deep drop lets organisms swim above and below the sharp "
                     "slice.", "correct": True},
            {"text": "A big drop would magnify the organisms and make them look "
                     "larger than they are.", "correct": False,
             "why": "Water does not magnify at this thickness. A deep drop just "
                    "gives the organisms room to swim out of focus."},
            {"text": "A big drop would dry out much faster under the warmth of "
                     "the lamp.", "correct": False,
             "why": "More water dries more slowly, not faster. The real trouble "
                    "is depth: the sharp slice is thinner than the drop."},
        ],
        "figure": None,
    },
    {
        "id": "b1-02-s32",
        "band": "standard",
        "text": "A student says the onion cells “grew” when she clicked round "
                "to ×400. What is wrong with the word grew?",
        "options": [
            {"text": "Nothing about the cells changed — only how big they "
                     "look.", "correct": True},
            {"text": "The cells did grow, because more light was reaching them "
                     "under the lamp.", "correct": False,
             "why": "Light does not grow a cell, and these were cut from an "
                    "onion. The change was in the lens, not the specimen."},
            {"text": "The cells swelled up in the water that was under the "
                     "coverslip.", "correct": False,
             "why": "Any swelling would take minutes and would not stop when "
                    "she stopped turning. The size changed the instant the "
                    "turret clicked."},
            {"text": "The word is right, because ×400 does make them four "
                     "hundred times bigger.", "correct": False,
             "why": "Four hundred times bigger to look at, not four hundred "
                    "times bigger in real life. The cell itself is exactly as "
                    "it was."},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "b1-02-h10",
        "band": "harder",
        "text": "A drawing of a cell measures 90 mm across. It was made with a "
                "×10 eyepiece and a ×40 objective. How wide is the real cell?",
        "options": [
            {"text": "9 mm, because the drawing came out ten times too big.",
             "correct": False,
             "why": "The drawing is the total magnification too big, and the "
                    "total is 10 × 40 = ×400. So 90 ÷ 400 = 0.225 mm."},
            {"text": "0.225 mm, because 90 ÷ 400 = 0.225.", "correct": True},
            {"text": "2.25 mm, because 90 ÷ 40 = 2.25.", "correct": False,
             "why": "That divides by the objective alone. The eyepiece "
                    "magnified the image again, so divide by the total of "
                    "×400."},
            {"text": "36 000 mm, because 90 × 400 = 36 000.", "correct": False,
             "why": "Multiplying magnifies the drawing a second time. Going "
                    "back to real life you divide by the magnification."},
        ],
        "figure": None,
    },
    {
        "id": "b1-02-h11",
        "band": "harder",
        "text": "The field number printed on an eyepiece is 18. With one "
                "objective in place the view measures 0.9 mm across. Which "
                "objective is it?",
        "options": [
            {"text": "×0.05, because 0.9 ÷ 18 = 0.05.", "correct": False,
             "why": "The division is upside down. The field number is divided "
                    "by the objective, so the objective is 18 ÷ 0.9 = ×20."},
            {"text": "×16.2, because 18 × 0.9 = 16.2.", "correct": False,
             "why": "Multiplying would make the view wider as the objective "
                    "climbs, which is backwards. Divide: 18 ÷ 0.9 = ×20."},
            {"text": "×9, because the view measures 0.9 mm across.",
             "correct": False,
             "why": "The 0.9 is a width in millimetres, not a lens. Work it out "
                    "from the field number: 18 ÷ 0.9 = ×20."},
            {"text": "×20, because 18 ÷ 20 = 0.9.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b1-02-h12",
        "band": "harder",
        "text": "A student records a total of ×400, a view 0.45 mm across, and "
                "six onion cells counted across it. Onion cells are about "
                "0.3 mm long. Why can the record not be right?",
        "options": [
            {"text": "×400 is too high a magnification for onion cells to be "
                     "seen at all.", "correct": False,
             "why": "×400 shows onion cells perfectly well. The record fails on "
                    "arithmetic: six cells of 0.3 mm need 1.8 mm of slide."},
            {"text": "Onion cells are 0.3 mm long only at ×40, and get shorter "
                     "as the magnification climbs.", "correct": False,
             "why": "A cell's real length never changes — only how big it looks "
                    "does. Six real cells simply will not fit into 0.45 mm."},
            {"text": "Six cells of 0.3 mm need 1.8 mm, and only 0.45 mm is in "
                     "view.", "correct": True},
            {"text": "She should have used the fine focus, which would have "
                     "brought fewer cells into the view.", "correct": False,
             "why": "The focus changes sharpness, not how many cells are "
                    "across. The numbers she wrote down cannot fit together."},
        ],
        "figure": None,
    },
    {
        "id": "b1-02-h13",
        "band": "harder",
        "text": "Two students want to find out whether cells from an onion’s "
                "outer layer are longer than cells from an inner layer. Which "
                "plan would settle it?",
        "options": [
            {"text": "Mount both layers, view each at the same magnification, "
                     "and count how many fit across the view.",
             "correct": True},
            {"text": "View the outer layer at ×40 and the inner layer at ×400, "
                     "then compare how big each one looks on the screen.",
             "correct": False,
             "why": "Different magnifications make the comparison worthless — "
                    "the ×400 cells look ten times bigger whatever their real "
                    "length."},
            {"text": "Look at one cell from each layer and say which of the two "
                     "drawings came out bigger on the page.",
             "correct": False,
             "why": "One cell each proves nothing, and drawing size depends on "
                    "the pencil. Count several across a known width instead."},
            {"text": "Stain the outer layer and leave the inner one unstained, "
                     "so that the two can be told apart.", "correct": False,
             "why": "That tells the slides apart but measures nothing. The "
                    "comparison needs the same magnification and a count across "
                    "the view."},
        ],
        "figure": None,
    },
    {
        "id": "b1-02-h14",
        "band": "harder",
        "text": "Which statement about electron microscopes is correct?",
        "options": [
            {"text": "They magnify more than light microscopes, but separate no "
                     "more detail than a light microscope does.",
             "correct": False,
             "why": "Detail is exactly what they add. Their resolution is far "
                    "better, which is why the extra magnification is worth "
                    "having."},
            {"text": "They can be used to watch living cells moving, which a "
                     "light microscope cannot do.", "correct": False,
             "why": "It is the other way round: a light microscope can show "
                    "living cells, and an electron microscope cannot."},
            {"text": "They separate far smaller detail than light can, but "
                     "the specimen cannot be alive.", "correct": True},
            {"text": "They use a much brighter lamp, and that is what lets them "
                     "show smaller detail.", "correct": False,
             "why": "They use a beam of electrons rather than a lamp. Detail "
                    "comes from resolution, not from brightness."},
        ],
        "figure": None,
    },
    {
        "id": "b1-02-h15",
        "band": "harder",
        "text": "A photograph taken down a microscope at ×400 is enlarged to "
                "twice its size on a photocopier. What has changed?",
        "options": [
            {"text": "Both the magnification and the detail, because everything "
                     "in the picture is now bigger.", "correct": False,
             "why": "Only the magnification. A copier cannot add detail that "
                    "the microscope never separated in the first place."},
            {"text": "The resolution, because the two lines of the cell wall "
                     "are now further apart on the paper.", "correct": False,
             "why": "Further apart on paper is not more separated by the lens. "
                    "If they were one smudge before, they are a bigger smudge "
                    "now."},
            {"text": "Nothing at all, because a photocopy shows the same thing "
                     "as the original did.", "correct": False,
             "why": "The magnification has genuinely doubled, to ×800. What has "
                    "not changed is the amount of detail in the picture."},
            {"text": "The magnification only, because a copier cannot add "
                     "detail that the microscope never separated.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b1-02-h16",
        "band": "harder",
        "text": "On the ×4 objective the slice in sharp focus is 0.10 mm deep. "
                "On the ×40 it is 0.008 mm deep. How many times thinner is it?",
        "options": [
            {"text": "12.5 times thinner, because 0.10 ÷ 0.008 comes to "
                     "12.5.", "correct": True},
            {"text": "0.08 times thinner, because 0.008 ÷ 0.10 = 0.08.",
             "correct": False,
             "why": "That is the fraction left, not how many times thinner. "
                    "Divide the larger by the smaller: 0.10 ÷ 0.008 = 12.5."},
            {"text": "10 times thinner, because the objective went up ten "
                     "times.", "correct": False,
             "why": "The depth does not shrink in step with the magnification. "
                    "Work with the two depths given: 0.10 ÷ 0.008 = 12.5."},
            {"text": "0.0008 times thinner, because 0.10 × 0.008 = 0.0008.",
             "correct": False,
             "why": "Multiplying two depths gives a number that means nothing "
                    "here. How many times thinner is a division: 12.5."},
        ],
        "figure": None,
    },
    {
        "id": "b1-02-h17",
        "band": "harder",
        "text": "A microscope has a fixed ×10 eyepiece and objectives of ×4, "
                "×10 and ×40. A student needs a total of ×200. What should she "
                "be told?",
        "options": [
            {"text": "Click the ×20 objective into place, which gives 10 × 20 = "
                     "×200.", "correct": False,
             "why": "There is no ×20 objective on this turret. Only ×4, ×10 and "
                    "×40 are fitted, so only ×40, ×100 and ×400 can be "
                    "reached."},
            {"text": "Use the ×40 objective and turn the fine focus about half "
                     "way, to halve it.", "correct": False,
             "why": "The focus wheel does not change magnification by any "
                    "amount. The three objectives are the only settings there "
                    "are."},
            {"text": "Use the ×10 objective and then the ×40 one after the "
                     "other, and average the two.", "correct": False,
             "why": "Averaging two views is not a magnification. Each objective "
                    "gives its own total, and none of them is ×200."},
            {"text": "It cannot be done — this microscope gives ×40, ×100 and "
                     "×400 only.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b1-02-h18",
        "band": "harder",
        "text": "A student lays a clear ruler on the stage and sees 4.5 mm "
                "across the view on the ×4 objective. She removes the ruler and "
                "clicks to the ×40. How wide is the view now?",
        "options": [
            {"text": "Still 4.5 mm, because the ruler is no longer there to "
                     "measure it with.", "correct": False,
             "why": "The width does not depend on being measured. Ten times the "
                    "objective gives a tenth of the width: 0.45 mm."},
            {"text": "0.45 mm, because ten times the magnification gives a "
                     "tenth of the view.", "correct": True},
            {"text": "45 mm, because the ×40 objective opens the view up ten "
                     "times wider.", "correct": False,
             "why": "Climbing narrows the view, it never widens it. Every step "
                    "up shows more detail of less slide."},
            {"text": "0.045 mm, because the total magnification has gone up a "
                     "hundred times.", "correct": False,
             "why": "The total went from ×40 to ×400, which is ten times, not a "
                    "hundred. So 4.5 ÷ 10 = 0.45 mm."},
        ],
        "figure": None,
    },
    {
        "id": "b1-02-h19",
        "band": "harder",
        "text": "A student cannot tell whether the round shapes on her slide "
                "are cells or trapped air. Which observation would settle it?",
        "options": [
            {"text": "They stay exactly where they are when the slide is moved "
                     "across the stage.", "correct": False,
             "why": "Anything that stays put while the slide moves is on the "
                    "eyepiece, not on the slide at all — neither a cell nor a "
                    "bubble."},
            {"text": "They get bigger when the ×40 objective is clicked into "
                     "place.", "correct": False,
             "why": "Everything gets bigger at a higher magnification, cells "
                    "and bubbles alike. That separates nothing."},
            {"text": "They are all different sizes and none are packed in "
                     "rows.", "correct": True},
            {"text": "They are darker in the middle than they are around the "
                     "edge of each shape.", "correct": False,
             "why": "Bubbles are the other way round — pale in the middle with "
                    "a thick black rim. Uneven sizes and no rows is the tell."},
        ],
        "figure": None,
    },
    {
        "id": "b1-02-h20",
        "band": "harder",
        "text": "Three slides: a single layer of onion skin, a leaf slice three "
                "cells thick, and a deep drop of pond water. Which is hardest "
                "to keep sharp at ×400?",
        "options": [
            {"text": "The pond water, because organisms swim through a sharp "
                     "slice thinner than the drop.", "correct": True},
            {"text": "The onion skin, because a single layer is too thin for "
                     "the lens to find at all.", "correct": False,
             "why": "One layer is the easiest of the three — the whole of it "
                    "sits inside the sharp slice and none of it moves."},
            {"text": "The leaf slice, because three layers of cells cannot be "
                     "lit by the lamp underneath.", "correct": False,
             "why": "Light gets through three layers well enough to see them. "
                    "They stay still, though, and swimming organisms do not."},
            {"text": "All three are the same, because the focus wheel works on "
                     "any slide you put under it.", "correct": False,
             "why": "The wheel works on all three, but only one of them keeps "
                    "moving out of the slice you have focused on."},
        ],
        "figure": None,
    },
    {
        "id": "b1-02-h21",
        "band": "harder",
        "text": "One student counts 15 onion cells across a view 4.5 mm wide. "
                "Another counts 6 across a view 1.8 mm wide. Do the two "
                "results agree?",
        "options": [
            {"text": "No — 15 cells and 6 cells cannot both be right for the "
                     "same kind of onion.", "correct": False,
             "why": "They were counted across different widths of slide. Work "
                    "out the cell length each time and both give 0.3 mm."},
            {"text": "No — the first student must have been working at a much "
                     "higher magnification.", "correct": False,
             "why": "She was working at a lower one, which is why she saw more "
                    "slide. Both counts still give a cell length of 0.3 mm."},
            {"text": "It cannot be decided without knowing both total "
                     "magnifications.", "correct": False,
             "why": "The widths of the two views are given, which is all the "
                    "calculation needs: 4.5 ÷ 15 and 1.8 ÷ 6 both give "
                    "0.3 mm."},
            {"text": "Yes — 4.5 ÷ 15 and 1.8 ÷ 6 both give the same cell "
                     "length of 0.3 mm.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b1-02-h22",
        "band": "harder",
        "text": "Eyepiece A has the field number 18 printed on it and eyepiece "
                "B has 20. Both are used with the same ×40 objective. Which "
                "shows more slide, and by how much?",
        "options": [
            {"text": "A, by 0.05 mm, because a smaller field number spreads the "
                     "view out wider.", "correct": False,
             "why": "A smaller field number gives a narrower view, not a wider "
                    "one. B wins: 20 ÷ 40 = 0.50 mm against 18 ÷ 40 = "
                    "0.45 mm."},
            {"text": "B, by 0.05 mm, because 20 ÷ 40 = 0.50 mm against "
                     "18 ÷ 40 = 0.45 mm.", "correct": True},
            {"text": "Neither, because the objective alone sets how much slide "
                     "is in the view.", "correct": False,
             "why": "The objective divides, but the field number is what it "
                    "divides into. Change the eyepiece's field number and the "
                    "view changes with it."},
            {"text": "B, by 2 mm, because 20 − 18 = 2 and that is the "
                     "difference.", "correct": False,
             "why": "The field numbers are divided by the objective before they "
                    "are compared: 0.50 mm − 0.45 mm = 0.05 mm."},
        ],
        "figure": None,
    },
    {
        "id": "b1-02-h23",
        "band": "harder",
        "text": "A hand lens magnifies ×10. Suggest why one cannot be used "
                "instead of a microscope to look at onion cells.",
        "options": [
            {"text": "A hand lens has no stage, so a slide cannot be held still "
                     "enough to look at.", "correct": False,
             "why": "A slide can be held steady on a bench. The real limit is "
                    "×10 — nowhere near enough to make out a cell."},
            {"text": "A hand lens turns the image upside down, which makes "
                     "cells hard to judge the size of.", "correct": False,
             "why": "A hand lens leaves the image the right way up; it is the "
                    "microscope that inverts it. The limit is how little it "
                    "magnifies."},
            {"text": "×10 is nowhere near enough — onion cells need ×40 or "
                     "more to be made out at all.", "correct": True},
            {"text": "A hand lens has no lamp, and daylight cannot pass through "
                     "a specimen on a slide.", "correct": False,
             "why": "Daylight passes through a thin specimen perfectly well. "
                    "The problem is the magnification, which stops at ×10."},
        ],
        "figure": None,
    },
    {
        "id": "b1-02-h24",
        "band": "harder",
        "text": "A student views onion cells at ×100 and cheek cells at ×400, "
                "and concludes that cheek cells are the larger of the two. "
                "Evaluate her conclusion.",
        "options": [
            {"text": "Not safe — the cheek cells were viewed at four times "
                     "the magnification the onion cells were.", "correct": True},
            {"text": "Safe, because she used the same microscope and the same "
                     "eyepiece for both of the slides.", "correct": False,
             "why": "The same microscope does not mean the same magnification. "
                    "She changed the objective, so the two views cannot be "
                    "compared."},
            {"text": "Not safe, because cheek cells cannot be seen at all "
                     "unless a stain has been used on them.", "correct": False,
             "why": "Staining helps, but it is not what breaks the comparison. "
                    "The two slides were viewed at different magnifications."},
            {"text": "Safe, because the higher magnification always gives the "
                     "more accurate measurement of size.", "correct": False,
             "why": "A higher magnification is not more accurate, it is just "
                    "bigger. To compare two cells you must view both the same "
                    "way."},
        ],
        "figure": None,
    },
    {
        "id": "b1-02-h25",
        "band": "harder",
        "text": "A drawing of a cell measures 7.5 cm across and is labelled "
                "×300. How wide is the real cell in millimetres?",
        "options": [
            {"text": "0.025 mm, because 7.5 ÷ 300 = 0.025 and the drawing was "
                     "measured in centimetres.", "correct": False,
             "why": "The answer was asked for in millimetres, so convert first: "
                    "7.5 cm is 75 mm, and 75 ÷ 300 = 0.25 mm."},
            {"text": "22 500 mm, because 75 × 300 = 22 500.", "correct": False,
             "why": "Multiplying magnifies the drawing all over again. Divide "
                    "by the magnification to get back to real life."},
            {"text": "4 mm, because 300 ÷ 75 = 4.", "correct": False,
             "why": "The division is the wrong way round. The drawing is 300 "
                    "times bigger than the cell, so the cell is 75 ÷ 300."},
            {"text": "0.25 mm, because 7.5 cm is 75 mm and 75 ÷ 300 = 0.25.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b1-02-h26",
        "band": "harder",
        "text": "While focusing downwards on the ×40 objective a student hears "
                "a small click, and the view stays blank whatever she does. "
                "What has most likely happened?",
        "options": [
            {"text": "The bulb has blown, and the microscope should be carried "
                     "to the front bench.", "correct": False,
             "why": "A blown bulb goes dark before you touch the focus, and "
                    "makes no click. Focusing down at ×40 means the lens has "
                    "met the glass."},
            {"text": "The lens has met the glass — stop, tell the teacher, make "
                     "a new slide.", "correct": True},
            {"text": "The turret has slipped between two objectives, and the "
                     "slide should be pressed down flat.", "correct": False,
             "why": "A turret between two lenses gives a dark view but no "
                    "click, and pressing on a slide is never the answer. The "
                    "click was glass."},
            {"text": "The specimen has dried out, and the coverslip should be "
                     "lifted so more water can be added.", "correct": False,
             "why": "Drying takes minutes and does not click. A click at ×40 "
                    "while focusing downwards is the objective reaching the "
                    "coverslip."},
        ],
        "figure": None,
    },
    {
        "id": "b1-02-h27",
        "band": "harder",
        "text": "Two microscopes have the same three objectives and eyepieces "
                "of the same field number, but one eyepiece is ×10 and the "
                "other ×5. Compare what they show.",
        "options": [
            {"text": "The ×5 one gives half the total and half the width of "
                     "slide at every objective.", "correct": False,
             "why": "Half the total, yes — but the width of slide comes from "
                    "the field number divided by the objective, so it is the "
                    "same on both."},
            {"text": "The ×5 one gives the same total as the other, but twice "
                     "the width of slide in view.", "correct": False,
             "why": "The total is halved, because the eyepiece is half as "
                    "strong. The width of slide is the same, not double."},
            {"text": "The ×5 one gives half the total, with the same width of "
                     "slide in view.", "correct": True},
            {"text": "They are identical, because it is the eyepiece that sets "
                     "the width of slide you can see.", "correct": False,
             "why": "The field number does that, and both eyepieces share it. "
                    "The magnifications are not identical: one total is half "
                    "the other."},
        ],
        "figure": None,
    },
    {
        "id": "b1-02-h28",
        "band": "harder",
        "text": "“A thicker slice is better, because there are more cells in "
                "it to look at.” Evaluate that claim.",
        "options": [
            {"text": "Wrong — less light gets through, and only one thin layer "
                     "is sharp at once.", "correct": True},
            {"text": "Right, as long as the coverslip is pressed down firmly "
                     "enough to flatten the slice out.", "correct": False,
             "why": "Pressing a coverslip cracks it and crushes the specimen. A "
                    "thick slice blocks light and lies mostly outside the sharp "
                    "slice."},
            {"text": "Right, because the extra cells make the specimen much "
                     "easier to find at low power.", "correct": False,
             "why": "Finding it is not the difficulty. Light cannot get cleanly "
                    "through several layers, and only one of them can be sharp "
                    "at a time."},
            {"text": "Wrong, because a thick specimen always cracks the "
                     "coverslip as it is lowered onto the slide.",
             "correct": False,
             "why": "A thick slice usually just holds the coverslip up. What "
                    "spoils the view is lost light and lost sharpness."},
        ],
        "figure": None,
    },
    {
        "id": "b1-02-h29",
        "band": "harder",
        "text": "A slide has been so heavily stained that everything on it is a "
                "uniform dark brown. What is the best thing to do?",
        "options": [
            {"text": "Rinse the whole slide under the tap and then look at it "
                     "again.", "correct": False,
             "why": "The rinse washes the specimen off with the stain, "
                    "coverslip and all. Start again with one drop, drawn "
                    "through."},
            {"text": "Turn the lamp right up until the detail shows through the "
                     "stain.", "correct": False,
             "why": "More light through a uniformly dark slide gives a brighter "
                    "uniform brown. The contrast has already been lost."},
            {"text": "Climb to the ×40 objective, where the stain will be "
                     "spread more thinly.", "correct": False,
             "why": "Magnifying does not thin a stain. It only makes a smaller "
                    "piece of the same dark view fill the circle."},
            {"text": "Make the slide again with one drop of stain, drawn "
                     "through with paper towel.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b1-02-h30",
        "band": "harder",
        "text": "A student states that the field of view at ×400 is 0.45 mm on "
                "every microscope. Evaluate the statement.",
        "options": [
            {"text": "Correct — 0.45 mm is simply what a total of ×400 always "
                     "gives you.", "correct": False,
             "why": "The width comes from the field number divided by the "
                    "objective. A different field number gives a different "
                    "answer at the same ×400."},
            {"text": "Not always — it depends on the field number printed on "
                     "the eyepiece.", "correct": True},
            {"text": "Not always — the width changes as the focus wheel is "
                     "turned through the specimen.", "correct": False,
             "why": "Focusing changes what is sharp, never how much slide is in "
                    "the circle. It is the field number that varies between "
                    "microscopes."},
            {"text": "Correct, so long as the eyepiece is ×10 and the objective "
                     "clicked in is the ×40.", "correct": False,
             "why": "Even then it holds only for a field number of 18. An "
                    "eyepiece marked 20 gives 0.50 mm at the very same ×400."},
        ],
        "figure": None,
    },
    {
        "id": "b1-02-h31",
        "band": "harder",
        "text": "An eyepiece has the field number 20. On the ×10 objective, how "
                "many moss-leaf cells 0.25 mm long fit across the view?",
        "options": [
            {"text": "80, because 20 ÷ 0.25 = 80 and the objective does not "
                     "come into it.", "correct": False,
             "why": "The field number has to be divided by the objective first: "
                    "20 ÷ 10 = 2.0 mm of slide, which holds 8 cells."},
            {"text": "0.5, because 2.0 × 0.25 = 0.5.", "correct": False,
             "why": "Multiplying the width by the cell length counts nothing. "
                    "Ask how many 0.25 mm cells fit into 2.0 mm: eight."},
            {"text": "8, because the view is 2.0 mm across and 2.0 ÷ 0.25 = 8.",
             "correct": True},
            {"text": "20, because the field number printed on the eyepiece is "
                     "20.", "correct": False,
             "why": "The field number is a starting point, not an answer. "
                    "Divide it by the objective, then by the cell length."},
        ],
        "figure": None,
    },
    {
        "id": "b1-02-h32",
        "band": "harder",
        "text": "A student wants to watch a pond organism swimming. Would an "
                "electron microscope help her?",
        "options": [
            {"text": "No — the specimen has to be dead and dried before it "
                     "goes in, so there is nothing left to watch swimming.",
             "correct": True},
            {"text": "Yes — the far better resolution would let her follow it "
                     "much more clearly than a light microscope could.",
             "correct": False,
             "why": "The resolution is better, but the organism would not be "
                    "alive to follow. A light microscope is the right tool for "
                    "watching living things."},
            {"text": "Yes — she could simply choose a lower magnification to "
                     "keep the swimming organism inside the view.",
             "correct": False,
             "why": "Magnification is not the obstacle. An electron microscope "
                    "cannot show a living specimen at any setting."},
            {"text": "No — an electron microscope magnifies far too little for "
                     "an organism that small.", "correct": False,
             "why": "It magnifies far more than a light microscope, not less. "
                    "The reason it will not help is that the specimen cannot be "
                    "alive."},
        ],
        "figure": None,
    },
]
