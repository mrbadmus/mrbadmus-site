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
]
