"""C8 lesson 02 — Mendeleev and the table that predicted: twelve questions.

The lesson's argument is one shape: an arrangement that only organises what
you already know is a filing cabinet, and one that tells you what you will
find is a theory. The page teaches it by making the student predict germanium
from its four neighbours and then showing them the 1886 measurements.

These twelve probe the angles the mastery ladder leaves alone: what the
ordering rule actually was, what a gap commits you to, and what makes a
prediction worth anything.

The distractors are built from the lesson's two declared misconceptions.

`PTAB-03` (the table was accepted because it was tidy) drives the wrong
options in e02, s02, h01 and h04. Each substitutes an aesthetic or social
reason — neatness, fame, being first — for an evidential one. h04 is the one
that matters: it hands the student a rival table that is tidier and asks what
would settle between them, so tidiness has nowhere left to stand.

`PTAB-04` (a gap in a table is a weakness in it) drives e03, s01 and h02,
where an empty square is read as missing information rather than as a claim.

A third strand, on the page and in neither register entry, is the
tellurium/iodine swap: s04 and h03 are built on it, because "he was right for a
reason he could not have known" is the hardest and best idea in the lesson.

⚠️ MRB-278 · ANSWER POSITION. The correct answer's index cycles 0, 1, 2, 3
through each band, so this file holds three of each.

⚠️ BAND VALUES ARE FULL WORDS — `easier`, `standard`, `harder`, never the
letters. See the note in `questions_01_metals_and_non_metals.py`.
"""

UNIT = "C8"
LESSON = "mendeleev"
LESSON_NUMBER = 2

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "c8-02-e01",
        "band": "easier",
        "text": "What did Mendeleev use to decide the order of the elements "
                "in his table?",
        "options": [
            {"text": "Atomic mass, starting a new row where the properties "
                     "repeated",
             "correct": True},
            {"text": "Atomic number, starting a new row every eight elements",
             "correct": False,
             "why": "Atomic number was unknown in 1869. The modern table uses "
                    "it, and it quietly fixes his swaps."},
            {"text": "Alphabetical order, so that any element could be found "
                     "quickly",
             "correct": False,
             "why": "That was suggested as a joke against Newlands. "
                    "Alphabetical order groups nothing."},
            {"text": "Date of discovery, with the oldest known elements "
                     "first",
             "correct": False,
             "why": "Discovery order is a fact about people, not about "
                    "elements."},
        ],
        "figure": None,
    },
    {
        "id": "c8-02-e02",
        "band": "easier",
        "text": "Why was Mendeleev's table accepted when earlier arrangements "
                "were not?",
        "options": [
            {"text": "Because he was the most famous chemist working at the "
                     "time",
             "correct": False,
             "why": "He was not especially famous in 1869. The table made his "
                    "name, not the other way round."},
            {"text": "Because its predictions about missing elements turned "
                     "out to be right",
             "correct": True},
            {"text": "Because it was neater than every other arrangement "
                     "published",
             "correct": False,
             "why": "Tidiness convinces nobody. Newlands had a neat repeating "
                    "pattern and was laughed at."},
            {"text": "Because it was the first arrangement anyone had ever "
                     "attempted",
             "correct": False,
             "why": "Several chemists had noticed the repeat before him, "
                    "including Newlands five years earlier."},
        ],
        "figure": None,
    },
    {
        "id": "c8-02-e03",
        "band": "easier",
        "text": "Mendeleev left several squares in his table empty. What did "
                "an empty square mean?",
        "options": [
            {"text": "That the element there had been lost from the records",
             "correct": False,
             "why": "Nothing had been lost. The elements had not been "
                    "discovered."},
            {"text": "That the table had run out of room at that point",
             "correct": False,
             "why": "The table had as many squares as it needed. The gap was "
                    "deliberate."},
            {"text": "That an undiscovered element belonged there",
             "correct": True},
            {"text": "That the elements either side had been measured wrongly",
             "correct": False,
             "why": "That was his reasoning for a SWAP, which is a different "
                    "decision from a gap."},
        ],
        "figure": None,
    },
    {
        "id": "c8-02-e04",
        "band": "easier",
        "text": "Mendeleev predicted the missing element below silicon would "
                "have a mass of about 72. Germanium was measured at 72.6. "
                "What does that show?",
        "options": [
            {"text": "That his prediction was wrong, because 72 is not 72.6",
             "correct": False,
             "why": "A prediction made from an empty square landing within "
                    "one per cent is a success, not a failure."},
            {"text": "That germanium was measured wrongly, because he "
                     "predicted 72",
             "correct": False,
             "why": "This is the reasoning he used for the swaps, and here it "
                    "runs the wrong way — the measurement is the check."},
            {"text": "That mass can be worked out from the two elements above "
                     "and below",
             "correct": False,
             "why": "True, and it is HOW he did it — but the question is what "
                    "the match SHOWS, which is that the method works."},
            {"text": "That the table could describe an element nobody had "
                     "found",
             "correct": True},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "c8-02-s01",
        "band": "standard",
        "text": "A critic in 1871 called the gaps a weakness in the table. "
                "What is the strongest reply?",
        "options": [
            {"text": "A gap says what will be found, so it can be checked and "
                     "could have failed",
             "correct": True},
            {"text": "A gap is only a weakness if there are more than three "
                     "of them",
             "correct": False,
             "why": "The number is not the point. One gap that gets filled "
                    "correctly is worth more than none."},
            {"text": "A gap is not part of the table, so a critic cannot "
                     "object to it",
             "correct": False,
             "why": "The gaps are the most deliberate part of the table. "
                    "Refusing the objection is not answering it."},
            {"text": "A gap is a weakness, and Mendeleev admitted as much at "
                     "the time",
             "correct": False,
             "why": "He treated them as the table's strongest feature and "
                    "staked his reputation on them."},
        ],
        "figure": None,
    },
    {
        "id": "c8-02-s02",
        "band": "standard",
        "text": "What is the difference between an arrangement of facts and a "
                "scientific theory?",
        "options": [
            {"text": "A theory is longer and covers more facts than an "
                     "arrangement does",
             "correct": False,
             "why": "Length is not the difference. A short theory that "
                    "predicts beats a long list that does not."},
            {"text": "A theory says something about what has not been "
                     "measured yet",
             "correct": True},
            {"text": "A theory has been agreed by more scientists than an "
                     "arrangement has",
             "correct": False,
             "why": "Agreement follows evidence. Newlands' pattern was "
                    "correct and agreed by nobody."},
            {"text": "A theory is written down and an arrangement is only "
                     "drawn out",
             "correct": False,
             "why": "Both are written down. The difference is what they "
                    "commit you to."},
        ],
        "figure": None,
    },
    {
        "id": "c8-02-s03",
        "band": "standard",
        "text": "Silicon forms SiO<sub>2</sub> and tin forms SnO<sub>2</sub>. "
                "What did that let Mendeleev predict about the element "
                "between them?",
        "options": [
            {"text": "That it would be a gas, because the column changes "
                     "state downwards",
             "correct": False,
             "why": "Silicon and tin are both solids. Nothing in the column "
                    "suggests a gas between them."},
            {"text": "That it would form no oxide at all, being between two "
                     "that do",
             "correct": False,
             "why": "A group is a family. An element that behaved completely "
                    "differently would not belong in it."},
            {"text": "That its oxide would have the formula XO<sub>2</sub>",
             "correct": True},
            {"text": "That its oxide would be exactly halfway between the two "
                     "in formula",
             "correct": False,
             "why": "There is no formula halfway between two identical "
                    "ratios. The ratio is what the group fixes."},
        ],
        "figure": None,
    },
    {
        "id": "c8-02-s04",
        "band": "standard",
        "text": "Tellurium has a greater atomic mass than iodine, yet "
                "Mendeleev placed iodine after it. Why?",
        "options": [
            {"text": "Because iodine had been discovered first and had "
                     "priority",
             "correct": False,
             "why": "Discovery order never enters the arrangement anywhere."},
            {"text": "Because he made an arithmetical mistake that nobody "
                     "checked",
             "correct": False,
             "why": "It was a deliberate decision he defended in print, not "
                    "a slip."},
            {"text": "Because tellurium was a newly discovered element and "
                     "less trusted",
             "correct": False,
             "why": "Both were long established. It was the MASS he "
                    "distrusted, not the element."},
            {"text": "Because iodine behaved like the other elements in that "
                     "column",
             "correct": True},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "c8-02-h01",
        "band": "harder",
        "text": "John Newlands published a repeating pattern in the elements "
                "five years before Mendeleev and was ridiculed. What does "
                "that episode show about how science works?",
        "options": [
            {"text": "That being right is not the same as being believed at "
                     "the time",
             "correct": True},
            {"text": "That a pattern published early is always taken more "
                     "seriously",
             "correct": False,
             "why": "The opposite happened. Being first bought Newlands "
                    "nothing at all."},
            {"text": "That ridicule from other chemists is a reliable test of "
                     "an idea",
             "correct": False,
             "why": "Ridicule is not an argument. It settled nothing then and "
                    "settles nothing now."},
            {"text": "That his pattern must have been wrong, or it would have "
                     "been accepted",
             "correct": False,
             "why": "His pattern was substantially right. What it lacked was "
                    "a prediction that could be checked."},
        ],
        "figure": None,
    },
    {
        "id": "c8-02-h02",
        "band": "harder",
        "text": "A modern researcher arranges twenty new compounds into a "
                "table and every column looks consistent. What would have to "
                "happen before the table counted as more than a filing "
                "system?",
        "options": [
            {"text": "It would have to be published in a journal that other "
                     "researchers read",
             "correct": False,
             "why": "Publication spreads a claim. It does not test one."},
            {"text": "It would have to predict a property nobody has measured "
                     "yet",
             "correct": True},
            {"text": "It would have to include every compound of that type "
                     "ever made",
             "correct": False,
             "why": "Completeness is organisation. Mendeleev's table was "
                    "incomplete on purpose and that was its strength."},
            {"text": "It would have to be redrawn until no column had a gap "
                     "in it",
             "correct": False,
             "why": "Filling every gap by hand removes exactly the thing that "
                    "could have been tested."},
        ],
        "figure": None,
    },
    {
        "id": "c8-02-h03",
        "band": "harder",
        "text": "The modern table is ordered by atomic number rather than "
                "mass. What does that change about Mendeleev's swapped pairs?",
        "options": [
            {"text": "It shows the swaps were mistakes that the modern table "
                     "corrects",
             "correct": False,
             "why": "The modern table puts those pairs exactly where he put "
                    "them. It vindicates the swaps."},
            {"text": "It leaves them unexplained, because atomic number was "
                     "unknown to him",
             "correct": False,
             "why": "Being unknown to him does not leave them unexplained — "
                    "it explains them, after the fact."},
            {"text": "It makes them unnecessary, because the true order "
                     "already puts them right",
             "correct": True},
            {"text": "It reverses them, so tellurium now comes after iodine",
             "correct": False,
             "why": "Tellurium has 52 protons and iodine 53, so tellurium "
                    "still comes first — as he placed it."},
        ],
        "figure": None,
    },
    {
        "id": "c8-02-h04",
        "band": "harder",
        "text": "Two rival tables of the elements are proposed. One is tidier "
                "and has no gaps; the other has three gaps with described "
                "properties. What would settle which is better science?",
        "options": [
            {"text": "The number of elements each table manages to include",
             "correct": False,
             "why": "Both include what is known. Coverage of the known is "
                    "what neither is being tested on."},
            {"text": "How many chemists find each table easier to read and "
                     "use",
             "correct": False,
             "why": "Usability is real and is not evidence. The tidy table "
                    "would win it and still be worse."},
            {"text": "Which of them was published first in a scientific "
                     "journal",
             "correct": False,
             "why": "Priority decides credit, never correctness. Newlands "
                    "had priority and no traction."},
            {"text": "Whether the described gaps are later filled by elements "
                     "that match",
             "correct": True},
        ],
        "figure": None,
    },
]
