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
        "text": "Silicon forms SiO₂ and tin forms SnO₂. "
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
            {"text": "That its oxide would have the formula XO₂",
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

    # ── easier · MRB-335 top-up ─────────────────────────────────────────
    {
        "id": "c8-02-e05",
        "band": "easier",
        "text": "What is atomic mass?",
        "options": [
            {"text": "How heavy one atom of an element is compared with the "
                     "others",
             "correct": True},
            {"text": "The mass of a sample of the element, weighed out on a "
                     "balance in the laboratory before the experiment starts",
             "correct": False,
             "why": "That is a sample mass and it depends on how much you "
                    "took. Atomic mass is a property of the element"},
            {"text": "The number of protons in the nucleus of an atom",
             "correct": False,
             "why": "That is the atomic number, and it is what the MODERN "
                    "table is ordered by"},
            {"text": "How much space a single atom of the element takes up "
                     "when it is on its own",
             "correct": False,
             "why": "That is size rather than mass. The two do not run "
                    "together neatly"},
        ],
        "figure": None,
    },
    {
        "id": "c8-02-e06",
        "band": "easier",
        "text": "What makes a statement a prediction, in the sense this "
                "lesson uses?",
        "options": [
            {"text": "It sums up the measurements that have already been "
                     "taken, so that a reader can see the pattern in them "
                     "without having to work through the numbers",
             "correct": False,
             "why": "That is a summary. A prediction is about what has NOT "
                    "been measured"},
            {"text": "It is specific enough that it could turn out to be "
                     "wrong",
             "correct": True},
            {"text": "It is made by somebody with a reputation for being "
                     "right",
             "correct": False,
             "why": "Who says it makes no difference. What matters is whether "
                    "it can be checked"},
            {"text": "It is vague enough to fit whatever is found",
             "correct": False,
             "why": "That is the opposite. A statement nothing could "
                    "contradict predicts nothing"},
        ],
        "figure": None,
    },
    {
        "id": "c8-02-e07",
        "band": "easier",
        "text": "Which element did Mendeleev describe fifteen years before "
                "anyone dug it out of a silver ore?",
        "options": [
            {"text": "Argon",
             "correct": False,
             "why": "Argon was not predicted by anybody — it fitted nowhere "
                    "in his table until a whole new group was added"},
            {"text": "Silicon",
             "correct": False,
             "why": "Silicon was already known and sits above the gap. It is "
                    "one of the neighbours he predicted FROM"},
            {"text": "Germanium",
             "correct": True},
            {"text": "Iodine, which he had to swap with tellurium because the "
                     "two of them came out in the wrong order by mass",
             "correct": False,
             "why": "Both were already known. The swap is a different part of "
                    "the story"},
        ],
        "figure": None,
    },
    {
        "id": "c8-02-e08",
        "band": "easier",
        "text": "What is atomic number?",
        "options": [
            {"text": "The position of the element in the table, counted from "
                     "the top left corner along each row in turn until the "
                     "element is reached",
             "correct": False,
             "why": "The two happen to run together, and the number is a fact "
                    "about the atom rather than about the layout"},
            {"text": "How heavy the atom is",
             "correct": False,
             "why": "That is atomic mass, and it is what Mendeleev had to use "
                    "instead"},
            {"text": "The number of the group the element is in",
             "correct": False,
             "why": "The group number counts outer electrons. Chlorine is "
                    "group 7 and has atomic number 17"},
            {"text": "The number of protons in an atom",
             "correct": True},
        ],
        "figure": None,
    },

    # ── standard · MRB-335 top-up ───────────────────────────────────────
    {
        "id": "c8-02-s05",
        "band": "standard",
        "text": "Mendeleev never knew WHY the properties repeated. What was "
                "the reason, found about fifty years later?",
        "options": [
            {"text": "The way electrons are arranged around the nucleus",
             "correct": True},
            {"text": "That atomic masses run in a repeating pattern of their "
                     "own, which nobody had noticed because the measurements "
                     "of the time were not accurate enough to show it",
             "correct": False,
             "why": "Masses do not repeat. What repeats is the arrangement of "
                    "electrons"},
            {"text": "That elements were discovered in a repeating order",
             "correct": False,
             "why": "Discovery order is history. It could not make properties "
                    "come round again"},
            {"text": "That the table had been drawn to make them repeat",
             "correct": False,
             "why": "The repeat was found in the elements and then drawn. It "
                    "was not imposed on them"},
        ],
        "figure": None,
    },
    {
        "id": "c8-02-s06",
        "band": "standard",
        "text": "An entire column was missing from the 1869 table and "
                "Mendeleev never suspected it. Why had those elements left no "
                "trace?",
        "options": [
            {"text": "Because they are so rare in the air that the "
                     "instruments of the time could not detect them at all",
             "correct": False,
             "why": "Argon is nearly one per cent of the air, which is not "
                    "rare. The problem was that it formed no compounds"},
            {"text": "Because they form no compounds, so nothing in any "
                     "analysis pointed to them",
             "correct": True},
            {"text": "Because they are all radioactive and decay far too "
                     "quickly for anybody to collect them",
             "correct": False,
             "why": "Helium, neon and argon are perfectly stable. Only the "
                    "heaviest of the group is radioactive"},
            {"text": "Because they had been found and were thought to be "
                     "mixtures",
             "correct": False,
             "why": "They had not been found at all. The first was isolated "
                    "in 1894"},
        ],
        "figure": None,
    },
    {
        "id": "c8-02-s07",
        "band": "standard",
        "text": "What result would have counted as evidence AGAINST "
                "Mendeleev's table?",
        "options": [
            {"text": "A new element that fitted none of the gaps and had to "
                     "be given a group of its own on the end of the table",
             "correct": False,
             "why": "That is exactly what argon did, and the table absorbed "
                    "it. Adding a group is not a refutation"},
            {"text": "A gap in the table that stayed empty for many years",
             "correct": False,
             "why": "An unfilled gap is a prediction still waiting. It is not "
                    "a result at all"},
            {"text": "An element found in a gap whose properties did not "
                     "match the description",
             "correct": True},
            {"text": "Another chemist proposing a different arrangement of "
                     "exactly the same set of elements",
             "correct": False,
             "why": "A rival arrangement is an alternative, not evidence. "
                    "Evidence comes from measurement"},
        ],
        "figure": None,
    },
    {
        "id": "c8-02-s08",
        "band": "standard",
        "text": "Mendeleev predicted both the DENSITY of the missing element "
                "and the FORMULA of its oxide. Which of the two came from the "
                "column it sat in?",
        "options": [
            {"text": "The density, because the elements in one column get "
                     "steadily heavier going down it and the gap could be "
                     "read off between its neighbours",
             "correct": False,
             "why": "Density was estimated from the neighbours on all four "
                    "sides. It is the FORMULA that a group fixes"},
            {"text": "Both, since a column decides everything about an "
                     "element",
             "correct": False,
             "why": "A column fixes the combining ratio. Density came from "
                    "the neighbours in the row as well"},
            {"text": "Neither — both came from the row",
             "correct": False,
             "why": "A row runs from metal to non-metal and fixes no "
                    "formulae. Same-group elements share them"},
            {"text": "The formula of the oxide",
             "correct": True},
        ],
        "figure": None,
    },

    # ── harder · MRB-335 top-up ─────────────────────────────────────────
    {
        "id": "c8-02-h05",
        "band": "harder",
        "text": "When argon was isolated in 1894 it fitted nowhere, and a new "
                "group was added on the end. Why is that a sign of a STRONG "
                "theory?",
        "options": [
            {"text": "Because a whole unexpected family could be taken in "
                     "without anything already in the table having to be "
                     "abandoned",
             "correct": True},
            {"text": "Because a theory that can be changed to fit whatever "
                     "turns up will never be shown to be wrong, and a theory "
                     "that cannot be shown to be wrong is the safest kind",
             "correct": False,
             "why": "That is the mark of a WEAK idea. This table stayed "
                    "testable — the gaps could still have failed"},
            {"text": "Because argon was the very element Mendeleev had "
                     "predicted all along, and its arrival simply confirmed "
                     "everything he had said",
             "correct": False,
             "why": "He predicted nothing about it. That is what makes its "
                    "absorption interesting"},
            {"text": "Because it showed the original table had been wrong",
             "correct": False,
             "why": "The original table was incomplete rather than wrong. "
                    "Nothing in it had to be undone"},
        ],
        "figure": None,
    },
    {
        "id": "c8-02-h06",
        "band": "harder",
        "text": "Mendeleev swapped tellurium and iodine by hand, against "
                "their masses. What did doing that by hand cost him at the "
                "time?",
        "options": [
            {"text": "It cost him the whole of the prediction about "
                     "germanium, because a table with a swap in it cannot be "
                     "used to describe an element that has not been found",
             "correct": False,
             "why": "The gap predictions were unaffected. What the swap cost "
                    "was credibility"},
            {"text": "It looked like adjusting the evidence to fit, because "
                     "he had no reason to give for the swap",
             "correct": True},
            {"text": "It made the properties of both elements come out wrong, "
                     "so the two columns they were placed in no longer worked",
             "correct": False,
             "why": "The swap made their properties come out RIGHT. That was "
                    "his justification, and it was not a reason"},
            {"text": "Nothing at all — swaps of that kind were normal "
                     "practice among chemists then",
             "correct": False,
             "why": "Ordering by mass was the whole basis of the table. "
                    "Breaking it needed defending"},
        ],
        "figure": None,
    },
    {
        "id": "c8-02-h07",
        "band": "harder",
        "text": "Suppose germanium had been found and its properties had NOT "
                "matched the prediction. What should chemists have done?",
        "options": [
            {"text": "Widened the description until germanium fell inside it, "
                     "since the element was in the right square and the square "
                     "was what the table was really claiming",
             "correct": False,
             "why": "That empties the prediction of content. A description "
                    "that can be widened to fit anything predicts nothing"},
            {"text": "Concluded that the element had been misidentified",
             "correct": False,
             "why": "A possibility worth checking once, and not a general "
                    "answer. Repeating the measurement is checking; assuming "
                    "the theory is right is not"},
            {"text": "Treated the mismatch as evidence against the table and "
                     "looked for what was wrong with it",
             "correct": True},
            {"text": "Ignored it, since one element out of sixty proves "
                     "nothing either way about the table taken as a whole",
             "correct": False,
             "why": "The whole case for the table rested on those "
                    "predictions. A failure would have struck at the "
                    "argument"},
        ],
        "figure": None,
    },
    {
        "id": "c8-02-h08",
        "band": "harder",
        "text": "One chemist keeps strict mass order and lets the columns "
                "break; Mendeleev swaps two elements to keep the columns "
                "intact. Which was the better move?",
        "options": [
            {"text": "Strict mass order, because the rule the table was built "
                     "on should never be broken for the sake of a result the "
                     "person building it happens to prefer",
             "correct": False,
             "why": "Mass was a means to an end. Keeping the families was the "
                    "point of the table"},
            {"text": "The swap, because Mendeleev turned out in the end to be "
                     "right about where the two of them really belonged",
             "correct": False,
             "why": "Right verdict, and hindsight is not the reason. The swap "
                    "was defensible on the day it was made"},
            {"text": "Neither — both moves are guesses, and one guess is no "
                     "better than another",
             "correct": False,
             "why": "One of them produced testable predictions and the other "
                    "did not. That is what separates them"},
            {"text": "The swap, because keeping the families intact preserved "
                     "the pattern the predictions came from",
             "correct": True},
        ],
        "figure": None,
    },
    # ── easier · appended ───────────────────────────────────────────────
    {
        "id": "c8-02-e09",
        "band": "easier",
        "text": "Before he had a table at all, what did Mendeleev "
                "physically do with the known elements?",
        "options": [
            {"text": "He wrote each element on a card and laid the cards "
                     "out in a line",
             "correct": True},
            {"text": "He asked every chemist in Europe where each element "
                     "should go",
             "correct": False,
             "why": "Nobody was consulted. The arrangement came out of the "
                    "elements' own measured properties"},
            {"text": "He reacted every element with every other one and "
                     "recorded the results",
             "correct": False,
             "why": "That is thousands of experiments, many of them lethal, "
                    "and no such work was done"},
            {"text": "He copied an arrangement out of an older textbook and "
                     "corrected it",
             "correct": False,
             "why": "No such textbook existed. Arranging the elements was "
                    "the open problem of the day"},
        ],
        "figure": None,
    },
    {
        "id": "c8-02-e10",
        "band": "easier",
        "text": "What does the word periodic describe in the name periodic "
                "table?",
        "options": [
            {"text": "That the elements were found one after another",
             "correct": False,
             "why": "Discovery order is history. The word describes the "
                    "elements themselves, not the hunt for them"},
            {"text": "That the pattern of properties comes round again",
             "correct": True},
            {"text": "That the table is brought up to date now and then",
             "correct": False,
             "why": "The word describes the elements, not the printing. A "
                    "table nobody updated would still be periodic"},
            {"text": "That each element lasts for a fixed period of time",
             "correct": False,
             "why": "Nothing in the table is a measure of how long anything "
                    "lasts"},
        ],
        "figure": None,
    },
    {
        "id": "c8-02-e11",
        "band": "easier",
        "text": "About how many elements had been discovered by the time "
                "Mendeleev laid out his cards in 1869?",
        "options": [
            {"text": "About 8", "correct": False,
             "why": "Far too few. He had enough cards to cut the line into "
                    "several rows and still see columns"},
            {"text": "About 26", "correct": False,
             "why": "Still too few. His published table was already several "
                    "columns wide and eight rows deep"},
            {"text": "About 63", "correct": True},
            {"text": "About 118", "correct": False,
             "why": "That is roughly the number known today, after another "
                    "century and a half of searching"},
        ],
        "figure": None,
    },
    {
        "id": "c8-02-e12",
        "band": "easier",
        "text": "Mendeleev began a new row of his table whenever what "
                "happened?",
        "options": [
            {"text": "Whenever he ran out of room across the page",
             "correct": False,
             "why": "The rows were cut where the elements demanded, not "
                    "where the paper ended"},
            {"text": "Whenever ten more elements had been added",
             "correct": False,
             "why": "No fixed count was used, and his rows are not all the "
                    "same length"},
            {"text": "Whenever the masses had risen by one hundred",
             "correct": False,
             "why": "No fixed step in mass was used. The step between rows "
                    "is nothing like constant"},
            {"text": "Whenever the properties began repeating",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c8-02-e13",
        "band": "easier",
        "text": "A density of about 5.5 g/cm³ was predicted in 1871 for "
                "the empty square under silicon. What did the measurement "
                "in 1886 give?",
        "options": [
            {"text": "5.32 g/cm³", "correct": True},
            {"text": "2.30 g/cm³", "correct": False,
             "why": "That is silicon's own density. The missing element was "
                    "predicted to be much denser than the element above it"},
            {"text": "7.30 g/cm³", "correct": False,
             "why": "That is tin's density, from the square below the gap "
                    "rather than in it"},
            {"text": "0.53 g/cm³", "correct": False,
             "why": "Ten times too low. Nothing in that part of the table "
                    "floats on water"},
        ],
        "figure": None,
    },
    {
        "id": "c8-02-e14",
        "band": "easier",
        "text": "Which of the elements Mendeleev predicted was the first to "
                "be found?",
        "options": [
            {"text": "Scandium, in 1879", "correct": False,
             "why": "Second of the three, four years after the first one "
                    "turned up"},
            {"text": "Gallium, in 1875", "correct": True},
            {"text": "Argon, in 1894", "correct": False,
             "why": "Argon was never predicted. Nothing in the 1869 table "
                    "hinted that it existed"},
            {"text": "Iodine, in 1811", "correct": False,
             "why": "Iodine was already known in 1869 and had a square of "
                    "its own from the start"},
        ],
        "figure": None,
    },
    {
        "id": "c8-02-e15",
        "band": "easier",
        "text": "What did Mendeleev predict the missing element below "
                "silicon would look like?",
        "options": [
            {"text": "A colourless gas", "correct": False,
             "why": "Its neighbours on all four sides are solids, so a gas "
                    "was never on the cards"},
            {"text": "A silvery liquid", "correct": False,
             "why": "Only one metal is liquid at room temperature, and it is "
                    "nowhere near this square"},
            {"text": "A dark grey solid", "correct": True},
            {"text": "A bright yellow powder", "correct": False,
             "why": "Colour like that belongs to compounds, not to the "
                    "elements around this gap"},
        ],
        "figure": None,
    },
    {
        "id": "c8-02-e16",
        "band": "easier",
        "text": "When the missing element was finally found, chemists drew "
                "up a table with two columns. What did the two columns "
                "hold?",
        "options": [
            {"text": "The element's properties and its price per kilogram",
             "correct": False,
             "why": "What an element costs is a fact about mining and "
                    "demand, and it tests no arrangement of anything"},
            {"text": "The properties of the element above it and the one "
                     "below it",
             "correct": False,
             "why": "Those neighbours were where the prediction came from. "
                    "Comparing them with each other tests nothing"},
            {"text": "Two separate measurements of the same element",
             "correct": False,
             "why": "Repeating a measurement checks the apparatus. It says "
                    "nothing about whether the table was right"},
            {"text": "What had been predicted and what was measured",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c8-02-e17",
        "band": "easier",
        "text": "What has to happen to a prediction before it counts as "
                "evidence for a theory?",
        "options": [
            {"text": "It has to be checked against a new measurement",
             "correct": True},
            {"text": "It has to be agreed on by most of the scientists in "
                     "the field",
             "correct": False,
             "why": "Agreement is not evidence. A claim everybody accepts "
                    "can still be contradicted by one measurement"},
            {"text": "It has to be repeated in the same words by somebody "
                     "else",
             "correct": False,
             "why": "Repeating a claim does not test it. Only a measurement "
                    "does"},
            {"text": "It has to be shown to follow from an older theory",
             "correct": False,
             "why": "A prediction that follows from an older idea is still "
                    "untested until somebody goes and looks"},
        ],
        "figure": None,
    },
    {
        "id": "c8-02-e18",
        "band": "easier",
        "text": "How did other chemists treat Newlands' repeating pattern "
                "when he published it in 1866?",
        "options": [
            {"text": "They tested it and reported that it failed",
             "correct": False,
             "why": "Nobody tested it. That is the whole complaint against "
                    "them"},
            {"text": "They laughed at it", "correct": True},
            {"text": "They taught it",
             "correct": False,
             "why": "It was not taught for years. Mendeleev's table is the "
                    "one that won the argument"},
            {"text": "They asked him to publish it again with more elements",
             "correct": False,
             "why": "No such request was made. The response was mockery, not "
                    "a request for more work"},
        ],
        "figure": None,
    },
    {
        "id": "c8-02-e19",
        "band": "easier",
        "text": "Mendeleev trusted one pair of elements' chemistry over "
                "their measured masses. What did he therefore believe about "
                "those masses?",
        "options": [
            {"text": "That they were right but did not matter here",
             "correct": False,
             "why": "If they did not matter he would have had nothing to "
                    "explain away, and he spent a great deal of ink on it"},
            {"text": "That they would change once the elements were purer",
             "correct": False,
             "why": "Purity changes what is in a sample, not the atomic "
                    "mass of the element itself"},
            {"text": "That they had been measured wrongly",
             "correct": True},
            {"text": "That they had been printed in the wrong squares",
             "correct": False,
             "why": "The numbers sat beside the right elements. It was the "
                    "order those numbers gave that he rejected"},
        ],
        "figure": None,
    },
    {
        "id": "c8-02-e20",
        "band": "easier",
        "text": "What does a scientist risk by publishing a prediction "
                "about something nobody has measured?",
        "options": [
            {"text": "Being beaten to the measurement",
             "correct": False,
             "why": "Somebody else measuring it is the point of publishing, "
                    "not a cost of it"},
            {"text": "Being asked to repeat the work yourself",
             "correct": False,
             "why": "Repeating your own work tests nothing. The risk is "
                    "that somebody else's measurement disagrees"},
            {"text": "Losing the credit",
             "correct": False,
             "why": "Credit follows a dated published claim, which is "
                    "exactly what publishing secures"},
            {"text": "Being shown to be wrong", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c8-02-e21",
        "band": "easier",
        "text": "What did chemists do with the elements Mendeleev had "
                "described, once each one had been found?",
        "options": [
            {"text": "They compared the measurements with what he had "
                     "written down",
             "correct": True},
            {"text": "They gave each one the name he had chosen for it",
             "correct": False,
             "why": "Each was named by whoever found it, and the names he "
                    "used were only placeholders"},
            {"text": "They removed the squares from the table once they "
                     "were full",
             "correct": False,
             "why": "A filled square stays in the table. It is the element's "
                    "permanent place in it"},
            {"text": "They asked him to redraw the table around them",
             "correct": False,
             "why": "Nothing needed redrawing. The elements fitted the "
                    "squares that were already waiting"},
        ],
        "figure": None,
    },
    {
        "id": "c8-02-e22",
        "band": "easier",
        "text": "Mendeleev called his missing element eka-silicon. What did "
                "the eka- part mean?",
        "options": [
            {"text": "That it would be made out of silicon",
             "correct": False,
             "why": "It was a separate element, not a form of silicon or "
                    "anything built from it"},
            {"text": "That it sat one place below silicon",
             "correct": True},
            {"text": "That it would be found inside silicon ores",
             "correct": False,
             "why": "The name says where the element sits in the table, not "
                    "where anyone should go digging"},
            {"text": "That it was the eighth element after silicon",
             "correct": False,
             "why": "The prefix marks one step down a column, not a count "
                    "along a row"},
        ],
        "figure": None,
    },
    {
        "id": "c8-02-e23",
        "band": "easier",
        "text": "Which quantity, unknown in 1869, puts tellurium and iodine "
                "in the order Mendeleev wanted without any swapping?",
        "options": [
            {"text": "Their melting points", "correct": False,
             "why": "Melting points do not run in order along a row, so "
                    "they could never set the order of the table"},
            {"text": "Their densities", "correct": False,
             "why": "Density was one of the properties Mendeleev PREDICTED "
                    "from the table, so it cannot be what builds it"},
            {"text": "Their number of protons", "correct": True},
            {"text": "The year each one was discovered", "correct": False,
             "why": "Discovery dates are an accident of who looked first, "
                    "and they scatter the families completely"},
        ],
        "figure": None,
    },
    {
        "id": "c8-02-e24",
        "band": "easier",
        "text": "Three of the squares Mendeleev left empty in 1869 had been "
                "filled within roughly how long?",
        "options": [
            {"text": "Seventeen months", "correct": False,
             "why": "Far too quick. The first of the three took six years "
                    "on its own"},
            {"text": "Five years", "correct": False,
             "why": "None of them had been found by then — the first turned up "
                    "a year later, and the other two long after that"},
            {"text": "Eighty years", "correct": False,
             "why": "Much too long. The table had been accepted well inside "
                    "Mendeleev's own lifetime"},
            {"text": "Seventeen years", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c8-02-e25",
        "band": "easier",
        "text": "One whole family of elements was missing from the 1869 "
                "table and Mendeleev never suspected it. Which family?",
        "options": [
            {"text": "The noble gases", "correct": True},
            {"text": "The metals worked since ancient times",
             "correct": False,
             "why": "Copper, iron, tin, lead and silver had been in use for "
                    "thousands of years and every one of them had a square"},
            {"text": "The halogens",
             "correct": False,
             "why": "Chlorine, bromine and iodine were all in the 1869 "
                    "table, and iodine caused one of his famous swaps"},
            {"text": "The elements obtained from sea water",
             "correct": False,
             "why": "Sodium, chlorine and iodine all come from sea water, "
                    "and all three were in the 1869 table"},
        ],
        "figure": None,
    },
    {
        "id": "c8-02-e26",
        "band": "easier",
        "text": "Which sort of statement can never be shown to be wrong?",
        "options": [
            {"text": "One that gives a number to two decimal places",
             "correct": False,
             "why": "A precise number is the easiest kind of claim to "
                    "contradict, which is what makes it useful"},
            {"text": "One so vague that any result would fit it",
             "correct": True},
            {"text": "One about something that has not been found yet",
             "correct": False,
             "why": "Mendeleev's claims were about undiscovered elements "
                    "and every one of them could have failed"},
            {"text": "One written down before the measurement is made",
             "correct": False,
             "why": "Writing it first is what exposes it. It is the only "
                    "way a claim can be caught out"},
        ],
        "figure": None,
    },
    {
        "id": "c8-02-e27",
        "band": "easier",
        "text": "Which element, found in 1879, filled one of Mendeleev's "
                "empty squares?",
        "options": [
            {"text": "Sodium", "correct": False,
             "why": "Sodium had been isolated in 1807 and was in the table "
                    "from the start"},
            {"text": "Chlorine", "correct": False,
             "why": "Chlorine was already well known and filled no gap"},
            {"text": "Scandium", "correct": True},
            {"text": "Helium", "correct": False,
             "why": "Helium belongs to the family Mendeleev's table had no "
                    "column for at all"},
        ],
        "figure": None,
    },
    {
        "id": "c8-02-e28",
        "band": "easier",
        "text": "What were atoms believed to be in 1869, when the table was "
                "published?",
        "options": [
            {"text": "Made of a nucleus with electrons around it",
             "correct": False,
             "why": "That picture is decades later, and it is the one that "
                    "finally explained the repeat"},
            {"text": "Small lumps of the four ancient elements",
             "correct": False,
             "why": "Chemists had abandoned earth, air, fire and water long "
                    "before 1869"},
            {"text": "Too small to have any mass worth measuring",
             "correct": False,
             "why": "Atomic mass was the one number Mendeleev had, and the "
                    "whole table was built on it"},
            {"text": "Solid and impossible to divide", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c8-02-e29",
        "band": "easier",
        "text": "What separates a description from a prediction?",
        "options": [
            {"text": "A description is written after measuring and a "
                     "prediction before",
             "correct": True},
            {"text": "A description uses words and a prediction uses "
                     "numbers",
             "correct": False,
             "why": "Either can use both. Mendeleev's prediction used "
                    "numbers and colour words together"},
            {"text": "A description is longer than a prediction",
             "correct": False,
             "why": "Length has nothing to do with it. A one-line claim can "
                    "be a prediction"},
            {"text": "A description is certain and a prediction is a guess",
             "correct": False,
             "why": "A prediction is reasoned from evidence. Calling it a "
                    "guess misses what makes it testable"},
        ],
        "figure": None,
    },
    {
        "id": "c8-02-e30",
        "band": "easier",
        "text": "After publishing his table, what did Mendeleev have to "
                "wait for?",
        "options": [
            {"text": "For a better balance to be built so masses could be "
                     "trusted",
             "correct": False,
             "why": "The masses he had were good enough. What was missing "
                    "was the elements themselves"},
            {"text": "For somebody to find the elements he had described",
             "correct": True},
            {"text": "For his table to be printed in enough languages",
             "correct": False,
             "why": "It spread quickly, and spreading was never what the "
                    "case rested on"},
            {"text": "For the reason behind the repeating pattern to be "
                     "explained",
             "correct": False,
             "why": "The table was accepted decades before anybody could "
                    "say why the pattern was there"},
        ],
        "figure": None,
    },
    {
        "id": "c8-02-e31",
        "band": "easier",
        "text": "Which is the weakest kind of evidence that an arrangement "
                "of the elements is the right one?",
        "options": [
            {"text": "That a later element fitted",
             "correct": False,
             "why": "That is the strongest evidence there is, and it is "
                    "what settled the argument in the end"},
            {"text": "That it puts elements with similar reactions together",
             "correct": False,
             "why": "Grouping elements by how they behave is real evidence, "
                    "drawn from measurements"},
            {"text": "That experts admire how neat it looks",
             "correct": True},
            {"text": "That a measurement it forbids has never been made",
             "correct": False,
             "why": "An arrangement that forbids something and survives has "
                    "been tested, which admiration never is"},
        ],
        "figure": None,
    },
    {
        "id": "c8-02-e32",
        "band": "easier",
        "text": "What should happen to a scientific theory when a careful "
                "measurement disagrees with it?",
        "options": [
            {"text": "The measurement should be left out of the report",
             "correct": False,
             "why": "Leaving out awkward results is how a theory is "
                    "protected from ever being tested"},
            {"text": "The theory should be kept until something better "
                     "comes along",
             "correct": False,
             "why": "A theory contradicted by evidence is not held in place "
                    "by the absence of a rival"},
            {"text": "The measurement should be repeated until it agrees",
             "correct": False,
             "why": "Repeating until you get the answer you wanted is not "
                    "checking. It is choosing"},
            {"text": "The theory has to be changed or given up",
             "correct": True},
        ],
        "figure": None,
    },

    # ── standard · appended ─────────────────────────────────────────────
    {
        "id": "c8-02-s09",
        "band": "standard",
        "text": "Mendeleev estimated a missing element's properties by "
                "taking values between those of its neighbours. Why does "
                "that work at all?",
        "options": [
            {"text": "Because the values change steadily from one "
                     "neighbouring element to the next",
             "correct": True},
            {"text": "Because every element is an average of the elements "
                     "that surround it in the table",
             "correct": False,
             "why": "An element is not made from its neighbours. The "
                    "steady change is a pattern, not a recipe"},
            {"text": "Because all the elements in one column have almost "
                     "the same mass as each other",
             "correct": False,
             "why": "Masses rise sharply down a column. If they did not, "
                    "there would be nothing to estimate between"},
            {"text": "Because the neighbours had already been measured "
                     "more carefully than anything else",
             "correct": False,
             "why": "Care in measuring tells you how accurate a number is, "
                    "not what an unmeasured element will do"},
        ],
        "figure": None,
    },
    {
        "id": "c8-02-s10",
        "band": "standard",
        "text": "Why could Mendeleev build a table on atomic mass in 1869 "
                "but not on the number of protons?",
        "options": [
            {"text": "Protons change from one sample of an element to the "
                     "next, so no fixed order exists",
             "correct": False,
             "why": "Every atom of an element has the same number of "
                    "protons. That is what makes it that element"},
            {"text": "Masses could be measured then and protons could not "
                     "be counted at all",
             "correct": True},
            {"text": "Ordering by protons puts the elements in a "
                     "completely different order from mass",
             "correct": False,
             "why": "The two orders agree almost everywhere. They differ "
                    "for only a handful of pairs"},
            {"text": "Mass is the property that decides how an element "
                     "reacts, so it had to be used",
             "correct": False,
             "why": "Mass does not decide reactions. If it did, no pair "
                    "would ever have needed swapping"},
        ],
        "figure": None,
    },
    {
        "id": "c8-02-s11",
        "band": "standard",
        "text": "Why did Mendeleev refuse to move the next element up into "
                "an empty square?",
        "options": [
            {"text": "Because moving it would have made the table one "
                     "square shorter than the others",
             "correct": False,
             "why": "Length was never the issue. The issue was which "
                    "family each element ended up in"},
            {"text": "Because the element he would have moved had not yet "
                     "had its mass measured",
             "correct": False,
             "why": "Its mass was known. Knowing it is precisely what "
                    "showed it belonged further along"},
            {"text": "Because every element below it would then sit in the "
                     "wrong column",
             "correct": True},
            {"text": "Because an element can only ever be placed in the "
                     "square it was first written into",
             "correct": False,
             "why": "There is no such rule, and he moved two elements by "
                    "hand himself when the chemistry demanded it"},
        ],
        "figure": None,
    },
    {
        "id": "c8-02-s12",
        "band": "standard",
        "text": "The table was published in 1869 and the argument about it "
                "was not settled until 1886. Why did it take so long?",
        "options": [
            {"text": "Because the table had to be redrawn many times "
                     "before the columns came out right",
             "correct": False,
             "why": "The columns did not change over those years. What "
                    "changed was the evidence for them"},
            {"text": "Because his paper was in Russian and nobody outside "
                     "Russia could obtain it",
             "correct": False,
             "why": "It was read and translated quickly. Being read was "
                    "never the problem"},
            {"text": "Because chemists in the 1870s had no interest in how "
                     "the elements were arranged",
             "correct": False,
             "why": "Several of them were arranging the elements "
                    "themselves. Interest was not in short supply"},
            {"text": "Because its claims had to be tested, and that meant "
                     "waiting for elements to be found",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c8-02-s13",
        "band": "standard",
        "text": "The element missing below silicon was found by a chemist "
                "in Germany who had played no part in the prediction. Why "
                "does that make the match stronger evidence?",
        "options": [
            {"text": "Because the measurements were made by somebody with "
                     "no stake in the answer",
             "correct": True},
            {"text": "Because German laboratories in the 1880s had the "
                     "most accurate balances anywhere",
             "correct": False,
             "why": "Where the work was done is not the point. Who had "
                    "something to gain from the result is"},
            {"text": "Because an element found abroad counts as a more "
                     "difficult discovery to make",
             "correct": False,
             "why": "Distance from Russia adds nothing to the evidence. "
                    "Independence from the prediction does"},
            {"text": "Because two chemists working apart will always agree "
                     "more closely than one working alone",
             "correct": False,
             "why": "Working apart does not improve accuracy. It removes a "
                    "reason to doubt the result"},
        ],
        "figure": None,
    },
    {
        "id": "c8-02-s14",
        "band": "standard",
        "text": "Why did it matter that Mendeleev's description was "
                "published years before anyone found the element?",
        "options": [
            {"text": "Because publishing early gave other chemists time to "
                     "buy the equipment they would need",
             "correct": False,
             "why": "Equipment was not the obstacle. Nobody knew what to "
                    "look for until the description existed"},
            {"text": "Because a description written afterwards could be "
                     "shaped to fit whatever turned up",
             "correct": True},
            {"text": "Because the element could not have been recognised "
                     "without a name already given to it",
             "correct": False,
             "why": "Elements are recognised from their properties. The "
                    "name is a label attached afterwards"},
            {"text": "Because a prediction only counts once it has been "
                     "printed in more than one language",
             "correct": False,
             "why": "Translation spreads a claim. It is the date and the "
                    "detail that make it testable"},
        ],
        "figure": None,
    },
    {
        "id": "c8-02-s15",
        "band": "standard",
        "text": "A chemist writes four statements about an element nobody "
                "has yet found. Which one is a prediction in the sense "
                "this lesson means?",
        "options": [
            {"text": "It will have properties of some kind",
             "correct": False,
             "why": "Every substance has properties of some kind. A claim "
                    "nothing could contradict says nothing"},
            {"text": "It will probably be interesting to study",
             "correct": False,
             "why": "Interesting is a judgement about chemists, not a "
                    "measurement anybody could take"},
            {"text": "It will have a density close to 5.5 g/cm³",
             "correct": True},
            {"text": "It will behave a little like its neighbours",
             "correct": False,
             "why": "A little like is too loose to fail. Almost any "
                    "measurement could be squared with it"},
        ],
        "figure": None,
    },
    {
        "id": "c8-02-s16",
        "band": "standard",
        "text": "Mendeleev swapped tellurium and iodine because he thought "
                "their masses were wrong. The masses turned out to be "
                "right. Why does the swap still stand?",
        "options": [
            {"text": "Because a famous chemist's decision is not overturned "
                     "on the strength of one measurement",
             "correct": False,
             "why": "Reputation settles nothing. A measurement that "
                    "mattered would overturn anybody"},
            {"text": "Because the two elements are so alike that their "
                     "order in the table makes no difference",
             "correct": False,
             "why": "They sit in different columns and behave differently. "
                    "The order is exactly what was at stake"},
            {"text": "Because the masses were later re-measured and found "
                     "to agree with his ordering after all",
             "correct": False,
             "why": "They were re-measured and they did not change. The "
                    "reason he was right lies elsewhere"},
            {"text": "Because the real order is set by protons, and his "
                     "chemistry pointed the same way",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c8-02-s17",
        "band": "standard",
        "text": "A chemist builds a table in which every square is filled "
                "by an element already known. What is the most that table "
                "can do?",
        "options": [
            {"text": "Organise what is already known",
             "correct": True},
            {"text": "Rule out new elements",
             "correct": False,
             "why": "A full table shows only that nothing known has been "
                    "left over. It says nothing about what has not been "
                    "found"},
            {"text": "Show that the arrangement chosen is the right one",
             "correct": False,
             "why": "Many arrangements can be made to look complete. "
                    "Looking complete is not evidence"},
            {"text": "Predict the properties of the next element found",
             "correct": False,
             "why": "That is the one thing it has not committed to. "
                    "Nothing in it is at risk from a new discovery"},
        ],
        "figure": None,
    },
    {
        "id": "c8-02-s18",
        "band": "standard",
        "text": "Which is the stronger claim about an element nobody has "
                "measured: that its mass is about 44, or that its mass lies "
                "somewhere between 9 and 89?",
        "options": [
            {"text": "The range, because a wider claim is right more often "
                     "than a narrow one",
             "correct": False,
             "why": "Being right more often is easy if you claim little. "
                    "The question is what the claim rules out"},
            {"text": "The figure of 44, because it rules out far more "
                     "possible results",
             "correct": True},
            {"text": "The range, because giving one figure is guessing "
                     "while a range is reasoning",
             "correct": False,
             "why": "Both came from the same reasoning. One of them simply "
                    "committed to more"},
            {"text": "Neither, because a claim about something unmeasured "
                     "is worth nothing until it is checked",
             "correct": False,
             "why": "Both are worth something before checking, and that is "
                    "the point. One is worth more"},
        ],
        "figure": None,
    },
    {
        "id": "c8-02-s19",
        "band": "standard",
        "text": "A student says Mendeleev simply got lucky three times. "
                "What is the best reply?",
        "options": [
            {"text": "Luck is impossible in chemistry, because chemistry "
                     "follows fixed laws",
             "correct": False,
             "why": "Chance results happen all the time. The reply has to "
                    "be about how unlikely this run of them was"},
            {"text": "He did get lucky, and the table was accepted for "
                     "other reasons entirely",
             "correct": False,
             "why": "The predictions ARE the reason it was accepted. There "
                    "is no other case to fall back on"},
            {"text": "Three separate predictions each matched several "
                     "measured properties",
             "correct": True},
            {"text": "Luck would have shown up as one prediction being "
                     "closer than the other two",
             "correct": False,
             "why": "Uneven accuracy is normal in any set of measurements "
                    "and proves nothing either way"},
        ],
        "figure": None,
    },
    {
        "id": "c8-02-s20",
        "band": "standard",
        "text": "Mendeleev predicted the mass, the density, the appearance "
                "and the oxide formula of one missing element. Why does "
                "predicting four properties beat predicting one?",
        "options": [
            {"text": "Because four properties take four times as long to "
                     "work out from the neighbours",
             "correct": False,
             "why": "Effort is not evidence. A slow guess is still a guess"},
            {"text": "Because an element cannot be identified from a "
                     "single property on its own",
             "correct": False,
             "why": "True of identifying a sample, and not the reason. The "
                    "reason is about how the CLAIM can fail"},
            {"text": "Because whoever found the element could choose which "
                     "property to check",
             "correct": False,
             "why": "The finder checked them all. Offering a choice would "
                    "weaken the claim, not strengthen it"},
            {"text": "Because each property is another chance for the "
                     "description to be shown wrong",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c8-02-s21",
        "band": "standard",
        "text": "Atomic mass turned out not to be the quantity that really "
                "sets the order of the elements. Why did the table survive "
                "that?",
        "options": [
            {"text": "Because mass runs in almost the same order as "
                     "protons, so the columns barely moved",
             "correct": True},
            {"text": "Because the table was too well established by then "
                     "for chemists to want to change it",
             "correct": False,
             "why": "Reluctance does not keep a wrong table alive. The "
                    "order itself had to hold up"},
            {"text": "Because Mendeleev had already ordered the elements "
                     "by protons without saying so",
             "correct": False,
             "why": "He could not have. Nobody knew protons existed for "
                    "another forty years"},
            {"text": "Because a table's ordering rule does not affect "
                     "which elements end up in which column",
             "correct": False,
             "why": "The rule is exactly what puts elements in columns. "
                    "Change it enough and the families break"},
        ],
        "figure": None,
    },
    {
        "id": "c8-02-s22",
        "band": "standard",
        "text": "A chemist publishes a prediction from a new arrangement "
                "and the measurement comes out nothing like it. Was the "
                "work wasted?",
        "options": [
            {"text": "Yes, because a prediction that fails leaves the "
                     "arrangement exactly where it started",
             "correct": False,
             "why": "It leaves it worse off, which is useful. Something "
                    "has been learnt that was not known before"},
            {"text": "No, because the failure is a result, and it says the "
                     "arrangement needs changing",
             "correct": True},
            {"text": "Yes, because nothing can be published from a "
                     "measurement that disagrees with the theory",
             "correct": False,
             "why": "Disagreements are published all the time, and they "
                    "are often the most useful papers"},
            {"text": "No, because the measurement was probably taken "
                     "wrongly and can simply be repeated",
             "correct": False,
             "why": "Assuming the measurement is at fault is how a theory "
                    "is protected from ever being tested"},
        ],
        "figure": None,
    },
    {
        "id": "c8-02-s23",
        "band": "standard",
        "text": "Which is the better scientific prediction: that an element "
                "will be grey and fairly heavy, or that it will be dark grey "
                "with an atomic mass of about 72?",
        "options": [
            {"text": "The first, because it will still be counted correct "
                     "over a much wider set of results",
             "correct": False,
             "why": "Surviving everything is a weakness here. It means no "
                    "measurement could ever have caught it out"},
            {"text": "The first, because vague wording leaves room",
             "correct": False,
             "why": "Leaving room is exactly the problem. A claim that "
                    "cannot be pinned down cannot be tested"},
            {"text": "The second, because a single measurement could "
                     "contradict it",
             "correct": True},
            {"text": "The second, because two properties are always worth "
                     "more than one in any prediction",
             "correct": False,
             "why": "Both statements mention two properties. It is the "
                    "precision that separates them, not the count"},
        ],
        "figure": None,
    },
    {
        "id": "c8-02-s24",
        "band": "standard",
        "text": "A chemist in 1872 wants to test Mendeleev's table rather "
                "than admire it. Which piece of work would be a test?",
        "options": [
            {"text": "Redrawing the table more clearly and checking every "
                     "column reads sensibly",
             "correct": False,
             "why": "Redrawing changes how it looks. Nothing about the "
                    "elements is put at risk"},
            {"text": "Counting how many chemists in Europe were willing to "
                     "accept the arrangement",
             "correct": False,
             "why": "Opinion is not evidence. The table could be popular "
                    "and wrong, or unpopular and right"},
            {"text": "Listing every element already known and confirming "
                     "each one has a square",
             "correct": False,
             "why": "The table was built from those elements, so they "
                    "cannot fail to fit. Nothing is being tested"},
            {"text": "Measuring a newly isolated element against the "
                     "published description of a gap",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c8-02-s25",
        "band": "standard",
        "text": "A chemist responded to Newlands by asking whether he had "
                "tried arranging the elements alphabetically. Why is that "
                "not an argument against him?",
        "options": [
            {"text": "It produces no evidence for or against the pattern",
             "correct": True},
            {"text": "Alphabetical order does in fact group some of the "
                     "elements sensibly",
             "correct": False,
             "why": "It groups nothing. Names are accidents of history and "
                    "language"},
            {"text": "A chemist is not allowed to criticise work that has "
                     "already been published",
             "correct": False,
             "why": "Criticism is the point of publishing. What was "
                    "offered here was mockery, not criticism"},
            {"text": "Newlands had tried it and said it failed",
             "correct": False,
             "why": "He had not, and it would not have helped. The remark "
                    "was a joke rather than a proposal"},
        ],
        "figure": None,
    },
    {
        "id": "c8-02-s26",
        "band": "standard",
        "text": "Mendeleev estimated the missing element's properties from "
                "the elements above, below and on either side of the gap. "
                "Why use four neighbours rather than one?",
        "options": [
            {"text": "Because four elements together weigh enough to give "
                     "a reliable average",
             "correct": False,
             "why": "Nothing is being averaged by weight. The neighbours "
                    "are evidence, not ingredients"},
            {"text": "Because the estimates from each direction can be "
                     "checked against one another",
             "correct": True},
            {"text": "Because a square with fewer than four neighbours "
                     "cannot be predicted into at all",
             "correct": False,
             "why": "Squares at the edge of the table have fewer "
                    "neighbours and can still be reasoned about"},
            {"text": "Because the rules of the table require every "
                     "prediction to use four sources",
             "correct": False,
             "why": "There is no such rule. He used what had been measured "
                    "around the gap"},
        ],
        "figure": None,
    },
    {
        "id": "c8-02-s27",
        "band": "standard",
        "text": "One of Mendeleev's four claims about the missing element "
                "was its appearance, and the element turned out to be "
                "greyish-white, shiny and brittle. What should be made of "
                "that?",
        "options": [
            {"text": "The whole prediction fails, because one part of it "
                     "did not come out right",
             "correct": False,
             "why": "A description is judged as a whole. Three numerical "
                    "claims landed and one colour word did not"},
            {"text": "The colour proves the element found was not the one "
                     "he had described",
             "correct": False,
             "why": "Mass, density and oxide formula all matched. A shade "
                    "of grey cannot outweigh those"},
            {"text": "It was the loosest of his claims and the least "
                     "impressive when it landed near",
             "correct": True},
            {"text": "Colour is the property that identifies an element, "
                     "so this was his most serious error",
             "correct": False,
             "why": "Colour identifies almost nothing on its own, which is "
                    "why it was the weakest claim of the four"},
        ],
        "figure": None,
    },
    {
        "id": "c8-02-s28",
        "band": "standard",
        "text": "Mendeleev's gaps were filled in 1875, 1879 and 1886. Why "
                "did each one add to the case rather than simply repeat "
                "it?",
        "options": [
            {"text": "Because each discovery was reported in a different "
                     "country from the one before",
             "correct": False,
             "why": "Where the work happened is not what makes a test "
                    "count. Whether it could have failed is"},
            {"text": "Because the table was redrawn after each one and "
                     "improved every time",
             "correct": False,
             "why": "The table was not redrawn. That is part of why the "
                    "confirmations count for so much"},
            {"text": "Because each was a separate chance for the table to "
                     "be shown wrong",
             "correct": True},
            {"text": "Because three results are needed before any claim in "
                     "science can be accepted",
             "correct": False,
             "why": "There is no fixed number. One clear failure would "
                    "have counted against him just as heavily"},
        ],
        "figure": None,
    },
    {
        "id": "c8-02-s29",
        "band": "standard",
        "text": "Why did it matter that Mendeleev printed his predictions "
                "rather than keeping them in a notebook?",
        "options": [
            {"text": "The claim was on record and dated, so it could not "
                     "be adjusted afterwards",
             "correct": True},
            {"text": "A notebook would not have survived the fifteen years "
                     "before the element was found",
             "correct": False,
             "why": "Plenty of notebooks survive. Survival is not the "
                    "reason printing matters"},
            {"text": "Printed figures are more accurate than figures "
                     "copied out by hand",
             "correct": False,
             "why": "The numbers are the same either way. What changes is "
                    "who has seen them and when"},
            {"text": "A prediction has to be read by a certain number of "
                     "chemists before it counts",
             "correct": False,
             "why": "No number is required. What is required is that the "
                    "claim be fixed before the test"},
        ],
        "figure": None,
    },
    {
        "id": "c8-02-s30",
        "band": "standard",
        "text": "Sixty-three elements were known in 1869 and about one "
                "hundred and eighteen are known now. Why did the extra ones "
                "not destroy Mendeleev's arrangement?",
        "options": [
            {"text": "Because the arrangement was changed a little each "
                     "time a new element appeared",
             "correct": False,
             "why": "The columns did not have to be rearranged. That is "
                    "the whole surprise"},
            {"text": "Because they went into the gaps and onto the ends of "
                     "the columns, as the pattern allowed",
             "correct": True},
            {"text": "Because the new elements are all far too rare to "
                     "matter to the table",
             "correct": False,
             "why": "Rarity has nothing to do with it. A rare element out "
                    "of place would be just as damaging"},
            {"text": "Because every element found since 1869 has been made "
                     "in a laboratory rather than found",
             "correct": False,
             "why": "Many were dug out of ores. Gallium and scandium were "
                    "among the first"},
        ],
        "figure": None,
    },
    {
        "id": "c8-02-s31",
        "band": "standard",
        "text": "Mendeleev's table was published in Russian and translated "
                "within a few years. Why does a scientific claim have to "
                "travel beyond the person who made it?",
        "options": [
            {"text": "So that the work can be credited to the right person "
                     "when it is confirmed",
             "correct": False,
             "why": "Credit follows publication but is not the reason for "
                    "it. The reason is testing"},
            {"text": "So that the claim reaches enough chemists to be "
                     "voted on properly",
             "correct": False,
             "why": "Nothing is settled by a vote. It is settled by "
                    "measurements anyone can take"},
            {"text": "So that other people can test it, rather than its "
                     "author being its only judge",
             "correct": True},
            {"text": "So that it is written in a language every chemist "
                     "can already read",
             "correct": False,
             "why": "Translation helps it spread, and spreading is only "
                    "useful because of what others then do with it"},
        ],
        "figure": None,
    },
    {
        "id": "c8-02-s32",
        "band": "standard",
        "text": "How could Mendeleev be confident that an element existed "
                "for an empty square, rather than the square simply staying "
                "empty for ever?",
        "options": [
            {"text": "Because a table with a hole in it cannot be printed "
                     "and sold",
             "correct": False,
             "why": "It was printed with the holes in. The holes were the "
                    "point of it"},
            {"text": "Because he had already seen a sample of the element "
                     "without being able to name it",
             "correct": False,
             "why": "He had never seen it. That is what made the "
                    "description remarkable"},
            {"text": "Because chemists had promised to keep searching "
                     "until every square was full",
             "correct": False,
             "why": "Nobody had promised anything. The search began "
                    "because the square was there"},
            {"text": "Because every other square in that column held an "
                     "element, with no exception",
             "correct": True},
        ],
        "figure": None,
    },

    # ── harder · appended ───────────────────────────────────────────────
    {
        "id": "c8-02-h09",
        "band": "harder",
        "text": "A doctor claims that a newly described illness always "
                "begins with the same three symptoms, and says so before "
                "any further cases are seen. What makes that a scientific "
                "claim by this lesson's standard?",
        "options": [
            {"text": "It says in advance what the next case will look "
                     "like, so one case could refute it",
             "correct": True},
            {"text": "It was made by somebody qualified to judge what "
                     "counts as a symptom",
             "correct": False,
             "why": "Qualifications decide who is worth listening to, not "
                    "whether a claim can be tested"},
            {"text": "It fits every case of the illness that has been "
                     "written up so far",
             "correct": False,
             "why": "It was built from those cases, so it cannot fail to "
                    "fit them. Old cases test nothing"},
            {"text": "It describes three symptoms rather than resting on a "
                     "single one",
             "correct": False,
             "why": "Counting symptoms is not what makes a claim testable. "
                    "Saying something before the event is"},
        ],
        "figure": None,
    },
    {
        "id": "c8-02-h10",
        "band": "harder",
        "text": "Mendeleev's table made three successful predictions and "
                "also had no room at all for a whole family of elements. "
                "How can both be true of one table?",
        "options": [
            {"text": "The successes must have been coincidences, since a "
                     "table that misses a family is not a real theory",
             "correct": False,
             "why": "Three matched numerical descriptions are not "
                    "coincidence, and no theory has ever been complete"},
            {"text": "A theory can be incomplete and still make claims "
                     "that hold up where it does speak",
             "correct": True},
            {"text": "The missing family shows the three predictions were "
                     "about the wrong elements entirely",
             "correct": False,
             "why": "The three were measured against his descriptions "
                    "square by square. Which elements they were is settled"},
            {"text": "A theory with anything missing from it has to be "
                     "replaced rather than extended",
             "correct": False,
             "why": "This one was extended by a column and everything "
                    "already in it stayed put"},
        ],
        "figure": None,
    },
    {
        "id": "c8-02-h11",
        "band": "harder",
        "text": "Two defences of an arrangement of the elements: that no "
                "measurement has ever contradicted it, and that it said "
                "what would be found and it was found. Which is stronger?",
        "options": [
            {"text": "The first, because surviving every measurement ever "
                     "taken is the hardest test there is",
             "correct": False,
             "why": "Nothing was risked, so nothing was survived. An "
                    "arrangement that forbids nothing cannot be contradicted"},
            {"text": "Neither, because both are claims about the past and "
                     "tell you nothing about the next element",
             "correct": False,
             "why": "One of them is precisely a record of the next element "
                    "having been called correctly in advance"},
            {"text": "The second, because the first is also true of a "
                     "table nobody has ever tested",
             "correct": True},
            {"text": "The first, because a single contradiction would end "
                     "an arrangement and none has appeared",
             "correct": False,
             "why": "No contradiction has appeared because no chance to "
                    "contradict has been offered"},
        ],
        "figure": None,
    },
    {
        "id": "c8-02-h12",
        "band": "harder",
        "text": "A predicted density of 5.5 g/cm³ was measured as 5.32, "
                "about 3 per cent out; a predicted mass of 72 was measured "
                "as 72.6, under 1 per cent out. What is the fairest verdict?",
        "options": [
            {"text": "The density prediction failed, because it missed by "
                     "several times as much as the mass one did",
             "correct": False,
             "why": "Three per cent on a value nobody had ever measured is "
                    "a hit, not a miss"},
            {"text": "Only the mass prediction counts",
             "correct": False,
             "why": "Both were published claims and both could have "
                    "failed. The ordering quantity has no special standing"},
            {"text": "Neither counts, because a prediction has to be exact "
                     "before it can be called correct",
             "correct": False,
             "why": "No measurement of anything is exact. A claim is "
                    "judged by how much it ruled out"},
            {"text": "Both landed within a few per cent of values nobody "
                     "had measured",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c8-02-h13",
        "band": "harder",
        "text": "A student concludes that leaving gaps is always good "
                "practice, so every table should have some. What is wrong "
                "with that rule?",
        "options": [
            {"text": "A gap is worth something only when the pattern "
                     "demands it and what belongs there can be described",
             "correct": True},
            {"text": "Gaps should only ever be left by a chemist whose "
                     "earlier predictions have already been confirmed, since "
                     "nobody else has earned the right to leave one",
             "correct": False,
             "why": "Reputation does not decide it. The reasoning behind "
                    "the gap decides it"},
            {"text": "Gaps are acceptable in a table of elements and in "
                     "nothing else",
             "correct": False,
             "why": "The reasoning carries across subjects. What does not "
                    "carry across is leaving holes for effect"},
            {"text": "A table should have at most one gap, so that the "
                     "prediction can be checked cleanly",
             "correct": False,
             "why": "There is no limit. He left several, and each was a "
                    "separate testable claim"},
        ],
        "figure": None,
    },
    {
        "id": "c8-02-h14",
        "band": "harder",
        "text": "Which would damage an arrangement of the elements more: a "
                "square nobody can fill, or an element that fits no square "
                "in it?",
        "options": [
            {"text": "The empty square, because an arrangement with a hole "
                     "in it is incomplete",
             "correct": False,
             "why": "An empty square marks the edge of what is known and "
                    "says what will fill it. That is a claim, not a wound"},
            {"text": "The element that fits nowhere, because it "
                     "contradicts the pattern rather than extending it",
             "correct": True},
            {"text": "The empty square, because chemists cannot teach from "
                     "a table with pieces missing",
             "correct": False,
             "why": "Teaching convenience is not evidence, and the gaps "
                    "are the part of the story most worth teaching"},
            {"text": "Neither, because both are simply things that have "
                     "not been explained yet",
             "correct": False,
             "why": "One of them says what will be found and the other "
                    "says the pattern is broken. They are not alike"},
        ],
        "figure": None,
    },
    {
        "id": "c8-02-h15",
        "band": "harder",
        "text": "Assess Mendeleev's decision to swap tellurium and iodine "
                "as it stood in 1871, before anyone knew anything about "
                "protons.",
        "options": [
            {"text": "Indefensible, because he had no reason for the move "
                     "beyond wanting his columns to look tidy, and tidiness "
                     "is the very thing the table should not be judged on",
             "correct": False,
             "why": "He had a chemical reason. Iodine's behaviour matched "
                    "the column it was moved into"},
            {"text": "Defensible only because we now know he happened to "
                     "be right about the order",
             "correct": False,
             "why": "Hindsight cannot make a decision defensible. It "
                    "either had a reason on the day or it did not"},
            {"text": "A bet on chemical behaviour over a measurement, with "
                     "a stated consequence that could be checked",
             "correct": True},
            {"text": "Sound, because measurements of atomic mass in 1871 "
                     "were known to be worthless",
             "correct": False,
             "why": "They were good enough to build the whole table on. "
                    "He doubted two of them, not all of them"},
        ],
        "figure": None,
    },
    {
        "id": "c8-02-h16",
        "band": "harder",
        "text": "Suppose Mendeleev had left no gaps and made no "
                "predictions, but every column had still turned out to hold "
                "a real family. Would the table have been a theory?",
        "options": [
            {"text": "Yes, because the families are real whether or not "
                     "anybody predicted anything from them",
             "correct": False,
             "why": "The families being real is the finding. A theory has "
                    "to stake something on what comes next"},
            {"text": "Yes, because sorting sixty-three elements correctly "
                     "is itself a considerable achievement",
             "correct": False,
             "why": "It is an achievement, and achievement is not the "
                    "test. The test is whether anything was at risk"},
            {"text": "No, because a table without gaps cannot be printed "
                     "in the usual way",
             "correct": False,
             "why": "Nothing about printing is involved. Plenty of "
                    "complete tables have been printed"},
            {"text": "No, because nothing in it would ever have been at "
                     "risk from a new measurement",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c8-02-h17",
        "band": "harder",
        "text": "Ordering the table by the number of protons removes every "
                "swap Mendeleev had to make by hand. Is the modern table a "
                "better theory, or only a tidier one?",
        "options": [
            {"text": "Better, because one rule replaces a case-by-case "
                     "correction and explains why the swaps were needed",
             "correct": True},
            {"text": "Only tidier, because the elements end up in exactly "
                     "the same columns either way",
             "correct": False,
             "why": "They do end up in the same columns, and the reason "
                    "they do is now given rather than assumed"},
            {"text": "Better, because protons can be counted far more "
                     "accurately than masses can be measured",
             "correct": False,
             "why": "Accuracy is a bonus. The gain is that the order no "
                    "longer needs any exceptions"},
            {"text": "Only tidier, because once a theory's predictions "
                     "have been confirmed it is finished, and any later "
                     "change to it can only be a matter of presentation",
             "correct": False,
             "why": "Confirmed theories are improved constantly. This one "
                    "was, forty years after its predictions landed"},
        ],
        "figure": None,
    },
    {
        "id": "c8-02-h18",
        "band": "harder",
        "text": "Mendeleev could not say why the properties repeated, and "
                "the reason was not worked out for about fifty years. Does "
                "that weaken the 1869 table?",
        "options": [
            {"text": "Yes, because an arrangement with no explanation "
                     "behind it is only a description",
             "correct": False,
             "why": "It made claims about things nobody had measured, "
                    "which no mere description does"},
            {"text": "No, because a theory can be well supported by what "
                     "it predicts before anyone knows the mechanism",
             "correct": True},
            {"text": "Yes, because chemists were right to withhold their "
                     "agreement until the reason was known",
             "correct": False,
             "why": "They agreed decades before the reason was known, and "
                    "the evidence justified them"},
            {"text": "No, because Mendeleev did give the reason and later "
                     "work merely confirmed it",
             "correct": False,
             "why": "He gave no reason and could not have. Atoms were "
                    "thought to have no parts inside them"},
        ],
        "figure": None,
    },
    {
        "id": "c8-02-h19",
        "band": "harder",
        "text": "If mockery is not an argument, what should Newlands' "
                "critics have done with his repeating pattern in 1866?",
        "options": [
            {"text": "Waited to see whether a more respected chemist "
                     "published the same idea",
             "correct": False,
             "why": "Who says a thing has no bearing on whether it is "
                    "true. Waiting for a famous name tests nothing"},
            {"text": "Asked him to rewrite it until it looked more like "
                     "the chemistry of the day",
             "correct": False,
             "why": "Familiar presentation would not have made it more or "
                    "less correct"},
            {"text": "Worked out a consequence of his arrangement and gone "
                     "and measured it",
             "correct": True},
            {"text": "Rejected it, since an arrangement with no gaps in it "
                     "predicts nothing",
             "correct": False,
             "why": "Rejecting it without a test is the very thing they "
                    "did. A consequence could have been drawn out and checked"},
        ],
        "figure": None,
    },
    {
        "id": "c8-02-h20",
        "band": "harder",
        "text": "A sceptic says the chemist who found the missing element "
                "may have been swayed by knowing the prediction. How could "
                "that objection be ruled out?",
        "options": [
            {"text": "By pointing out that no chemist would knowingly "
                     "report a result to please somebody else",
             "correct": False,
             "why": "Trusting people's motives is not a check. A check has "
                    "to work whether or not they are trustworthy"},
            {"text": "By noting that the prediction was published years "
                     "earlier, which settles it on its own",
             "correct": False,
             "why": "Publishing early fixes the CLAIM. It does nothing "
                    "about how the later measurement was made"},
            {"text": "By showing that the element's properties agreed with "
                     "the table's columns as well",
             "correct": False,
             "why": "The columns are where the prediction came from, so "
                    "agreeing with them is not independent support"},
            {"text": "By having others re-measure it and comparing the "
                     "results with the dated published claim",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c8-02-h21",
        "band": "harder",
        "text": "Between 1869 and 1886 confidence in the table rose "
                "sharply, and not one square of it was redrawn. What does "
                "that say about where scientific confidence comes from?",
        "options": [
            {"text": "It comes from evidence arriving from outside the "
                     "idea itself",
             "correct": True},
            {"text": "It comes from an idea being repeated often enough "
                     "for people to grow used to it",
             "correct": False,
             "why": "Familiarity changes minds and changes nothing about "
                    "the evidence. Three measurements did the work here"},
            {"text": "It comes from an idea's author defending it",
             "correct": False,
             "why": "Mendeleev argued for his table, and what settled it "
                    "was elements he never handled"},
            {"text": "It comes from a theory being reworked until every "
                     "objection has been dealt with",
             "correct": False,
             "why": "The table was not reworked at all across those "
                    "seventeen years"},
        ],
        "figure": None,
    },
    {
        "id": "c8-02-h22",
        "band": "harder",
        "text": "Suppose the three predicted elements had all matched "
                "their predicted masses and matched nothing else. What "
                "would that have shown?",
        "options": [
            {"text": "That the table was completely wrong and should have "
                     "been abandoned",
             "correct": False,
             "why": "Three masses called correctly in advance is a real "
                    "result. It would have shown part of the idea working"},
            {"text": "That mass followed the pattern but the columns' "
                     "claim about chemistry did not hold",
             "correct": True},
            {"text": "That the elements had been misidentified, since "
                     "matching one property is impossible by chance",
             "correct": False,
             "why": "A mass can be landed by a pattern that says nothing "
                    "about chemistry. That is exactly the case described"},
            {"text": "That the predictions were correct, since mass is the "
                     "property the table was built on",
             "correct": False,
             "why": "Being built on mass is the reason the mass matches "
                    "prove least. The chemistry was the new claim"},
        ],
        "figure": None,
    },
    {
        "id": "c8-02-h23",
        "band": "harder",
        "text": "Evaluate this statement: a theory that can explain any "
                "result you get is the strongest kind of theory.",
        "options": [
            {"text": "Correct, because a theory that explains everything "
                     "has no gaps left in it",
             "correct": False,
             "why": "Explaining everything after the event is not the same "
                    "as having no gaps. It is having no risks"},
            {"text": "Correct, because explaining a surprising result is "
                     "the hardest thing a theory does",
             "correct": False,
             "why": "A result is only surprising if the theory forbade it. "
                    "One that forbids nothing is never surprised"},
            {"text": "Wrong, because it forbids nothing, so no result can "
                     "ever test it",
             "correct": True},
            {"text": "Wrong, because a theory should explain the results "
                     "in its own subject and no others",
             "correct": False,
             "why": "Reaching across subjects is a strength. The fault "
                    "here is being unable to fail"},
        ],
        "figure": None,
    },
    {
        "id": "c8-02-h24",
        "band": "harder",
        "text": "Why does moving from atomic mass to the number of protons "
                "count as an improvement to the THEORY rather than a "
                "correction to the DATA?",
        "options": [
            {"text": "Because the old atomic masses were thrown out and "
                     "measured again from scratch",
             "correct": False,
             "why": "The masses stood. Tellurium is still heavier than "
                    "iodine and always was"},
            {"text": "Because a theory is improved whenever any of its "
                     "numbers are made more accurate",
             "correct": False,
             "why": "Better numbers refine a theory's use. They do not "
                    "change what it says the order MEANS"},
            {"text": "Because the change was made by a different chemist "
                     "from the one who built the table, and only an author "
                     "can alter what his own theory says",
             "correct": False,
             "why": "Who made a change has no bearing on whether it is a "
                    "change of theory or of data"},
            {"text": "Because it changed what the order means and "
                     "explained the swaps instead of repairing numbers",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c8-02-h25",
        "band": "harder",
        "text": "A student says the table was accepted because chemists "
                "wanted it to be true. How would you answer?",
        "options": [
            {"text": "Each confirmation was an independent measurement "
                     "that could have gone the other way",
             "correct": True},
            {"text": "Chemists had no preference at all, since none of "
                     "them had anything to gain from the table",
             "correct": False,
             "why": "Several had rival arrangements of their own and "
                    "every reason to want it to fail"},
            {"text": "The table was accepted straight away in 1869, before "
                     "anyone had time to form a preference",
             "correct": False,
             "why": "It was resisted for years. Acceptance followed the "
                    "evidence rather than preceding it"},
            {"text": "Wanting something to be true has no effect on what "
                     "scientists conclude from evidence",
             "correct": False,
             "why": "It can have a large effect, which is why independent "
                    "measurement matters so much"},
        ],
        "figure": None,
    },
    {
        "id": "c8-02-h26",
        "band": "harder",
        "text": "A teacher shows the four-row comparison of prediction "
                "against measurement and says it proves Mendeleev was "
                "right. What is the most careful version of that claim?",
        "options": [
            {"text": "It proves the table, because four properties in a "
                     "row cannot agree by chance",
             "correct": False,
             "why": "Unlikely is not impossible, and proof is a word for "
                    "mathematics rather than for evidence"},
            {"text": "It supports the arrangement strongly, and a contrary "
                     "result later would still count against it",
             "correct": True},
            {"text": "It proves nothing, because a single element cannot "
                     "settle a claim about the whole table",
             "correct": False,
             "why": "One element is real evidence, and there were three. "
                    "The caution belongs on the word proves"},
            {"text": "It shows the prediction was lucky, since no reason "
                     "for the repeat was known in 1886",
             "correct": False,
             "why": "A prediction made from a stated pattern and matched "
                    "on four counts is not luck"},
        ],
        "figure": None,
    },
    {
        "id": "c8-02-h27",
        "band": "harder",
        "text": "Mendeleev predicted masses of 44, 68 and 72 for three "
                "missing elements. The three were later measured at 45, "
                "69.7 and 72.6. What does that pattern of results show?",
        "options": [
            {"text": "That his method was reliable for mass and untested "
                     "for every other property",
             "correct": False,
             "why": "The same predictions covered densities and oxide "
                    "formulae, and those were checked too"},
            {"text": "That the measurements must have been adjusted to sit "
                     "near the published figures, since three laboratories "
                     "working apart could not otherwise agree so closely",
             "correct": False,
             "why": "A serious charge with nothing behind it, and the "
                    "three were measured in different laboratories"},
            {"text": "That three separate numerical claims all landed "
                     "close, which fitting to known elements cannot do",
             "correct": True},
            {"text": "That mass can always be worked out from a position "
                     "in any table of anything",
             "correct": False,
             "why": "It works here because the elements' masses vary "
                    "steadily with position, which is not true of tables "
                    "in general"},
        ],
        "figure": None,
    },
    {
        "id": "c8-02-h28",
        "band": "harder",
        "text": "A rival in 1870 proposes ordering the elements by density "
                "instead of by mass. How should chemists decide between the "
                "two arrangements?",
        "options": [
            {"text": "By adopting whichever one more chemists were already "
                     "using in their teaching",
             "correct": False,
             "why": "Popularity is not evidence. A widely used arrangement "
                    "can still put elements in the wrong families"},
            {"text": "By choosing density, since it can be read straight "
                     "off a measurement while mass has to be worked out, and "
                     "the simpler quantity should always order a table",
             "correct": False,
             "why": "Ease of measurement does not decide which quantity "
                    "governs how elements behave"},
            {"text": "By keeping both, since two arrangements of the same "
                     "elements cannot disagree",
             "correct": False,
             "why": "They disagree as soon as they put a given element in "
                    "different columns, and these would"},
            {"text": "By seeing which order groups elements that behave "
                     "alike and which yields claims that can be checked",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c8-02-h29",
        "band": "harder",
        "text": "A new element is made in a laboratory today and given a "
                "position in the modern table. What has the table committed "
                "itself to before anything is measured?",
        "options": [
            {"text": "A set of expectations that can be measured and could "
                     "turn out wrong",
             "correct": True},
            {"text": "Nothing at all, because a modern table is only a "
                     "record of the elements already known",
             "correct": False,
             "why": "That describes a filing cabinet. The modern table "
                    "makes claims about a square before it is occupied"},
            {"text": "A guarantee that the element will behave exactly "
                     "like the one above it",
             "correct": False,
             "why": "Neighbours are alike, not identical, and properties "
                    "shift steadily as you move down"},
            {"text": "The name the element will eventually be given by "
                     "chemists",
             "correct": False,
             "why": "Names are decided by committee afterwards and are not "
                    "a scientific claim about anything"},
        ],
        "figure": None,
    },
    {
        "id": "c8-02-h30",
        "band": "harder",
        "text": "Mendeleev's order and the modern order disagree about a "
                "handful of pairs. Which is the best description of what "
                "happened to the older table?",
        "options": [
            {"text": "It was shown to be wrong, since a table that puts "
                     "any pair in the wrong order has failed",
             "correct": False,
             "why": "His pairs are in the order the modern table uses. It "
                    "is the RULE that changed, not his columns"},
            {"text": "Its ordering rule was replaced while its central "
                     "claim survived",
             "correct": True},
            {"text": "Nothing happened to it, because the modern table is "
                     "simply the same table redrawn",
             "correct": False,
             "why": "Something real changed. The order now follows from a "
                    "quantity Mendeleev could not have known"},
            {"text": "It was kept only for teaching",
             "correct": False,
             "why": "It was not kept as a simplified version. Its columns "
                    "are the modern table's columns"},
        ],
        "figure": None,
    },
    {
        "id": "c8-02-h31",
        "band": "harder",
        "text": "In 1886 a chemist was able to check Mendeleev's "
                "description of a missing element line by line. What "
                "feature of the description made that possible?",
        "options": [
            {"text": "It had been agreed in advance by the leading "
                     "chemists of the day",
             "correct": False,
             "why": "Nobody agreed it. Most of them doubted it, which is "
                    "part of why the check mattered"},
            {"text": "It listed more properties than any other prediction "
                     "in chemistry at the time",
             "correct": False,
             "why": "Sheer quantity is not what makes a check possible. "
                    "Each claim being specific is"},
            {"text": "It was specific, numerical and in print before the "
                     "element existed to anyone",
             "correct": True},
            {"text": "It used only properties that are easy to measure "
                     "with simple apparatus",
             "correct": False,
             "why": "Some of them needed careful work. Ease of measuring "
                    "is not what fixes a claim in advance"},
        ],
        "figure": None,
    },
    {
        "id": "c8-02-h32",
        "band": "harder",
        "text": "A student says a scientific theory is just somebody's "
                "idea until it has been proved. What does the story of the "
                "table suggest instead?",
        "options": [
            {"text": "That a theory becomes proved as soon as one of its "
                     "predictions is confirmed",
             "correct": False,
             "why": "One confirmation supports a theory. It leaves every "
                    "future measurement free to disagree"},
            {"text": "That a theory is proved once enough chemists have "
                     "agreed to teach it",
             "correct": False,
             "why": "Agreement follows evidence at best, and it is not "
                    "what makes a theory secure"},
            {"text": "That an idea nobody has tested is worth as much as "
                     "one that has survived testing, since neither of the two "
                     "has actually been proved",
             "correct": False,
             "why": "Surviving a test it could have failed is exactly what "
                    "separates the two"},
            {"text": "That theories are supported by surviving tests they "
                     "could have failed, rather than proved",
             "correct": True},
        ],
        "figure": None,
    },
]
