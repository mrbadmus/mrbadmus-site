"""Chemistry · Atomic structure and the periodic table — development of the
periodic table · the MRB-338 expansion.

Fifty-two rows on how the table was arrived at and why it was believed. The
weight falls on the working-scientifically point the spec is really testing —
a model earns acceptance by predicting what nobody has seen yet — and on the
three named steps that got there: Newlands' octaves and why they failed,
Mendeleev's gaps and his willingness to put chemistry above mass, and
Moseley's atomic numbers, which removed the last disagreements.

The modern table's layout belongs to the `periodic-table` leaf and the
isotope arithmetic behind a mass-order reversal to `relative-atomic-mass`;
this leaf stays on the history and the reasoning.
"""

TOPIC = "atomic-structure"
SUBJECT = "chemistry"

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────
    {
        "id": "ks4-development-periodic-table-e05",
        "subtopic_slug": "development-periodic-table",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State how far along the list of known elements Newlands' "
                "pattern held good.",
        "options": [
            "Only as far as about the first sixteen elements",
            "As far as the first sixty elements",
            "All the way to the end of the list",
            "Only for the metals, at any point in the list",
        ],
        "correct_index": 0,
        "why": "The octaves worked for the lightest elements and then broke "
               "down, which is one reason the idea was rejected.",
    },
    {
        "id": "ks4-development-periodic-table-e06",
        "subtopic_slug": "development-periodic-table",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the element Mendeleev called eka-silicon before anyone "
                "had found it.",
        "options": [
            "Gallium",
            "Germanium",
            "Scandium",
            "Silicon",
        ],
        "correct_index": 1,
        "why": "Eka-silicon was found in 1886 and named germanium, and its "
               "properties matched Mendeleev's prediction closely.",
    },
    {
        "id": "ks4-development-periodic-table-e07",
        "subtopic_slug": "development-periodic-table",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State why Mendeleev's predictions persuaded other scientists "
                "to accept his table.",
        "options": [
            "The predictions were published a long time before anyone else's "
            "were, which secured him the credit for them",
            "The predictions were made about elements that were already well "
            "known to every chemist of the day",
            "The predicted elements were later found, with the properties he "
                "had said they would have",
            "They were checked against Newlands' earlier list",
        ],
        "correct_index": 2,
        "why": "A model that correctly foretells something nobody has seen is "
               "far stronger evidence than one that only tidies up the known.",
    },
    {
        "id": "ks4-development-periodic-table-e08",
        "subtopic_slug": "development-periodic-table",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State what Mendeleev said about the elements that would one "
                "day fill the spaces in his table.",
        "options": [
            "That there were no such elements left to find",
            "That they would all turn out to be metals",
            "That they would prove too unstable ever to be isolated in a "
            "laboratory",
            "That he could say in advance what their properties would be",
        ],
        "correct_index": 3,
        "why": "He used the pattern of each gap's neighbours to set out the "
               "properties the missing element would have.",
    },
    {
        "id": "ks4-development-periodic-table-e09",
        "subtopic_slug": "development-periodic-table",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "The noble gases were found after Mendeleev's table was "
                "published. State where they were put.",
        "options": [
            "Into a new column of their own at the edge of the table",
            "Into the spaces Mendeleev had already left as gaps",
            "Into the column that already held the alkali metals",
            "Into a separate table, kept apart from the other elements",
        ],
        "correct_index": 0,
        "why": "They shared very similar properties, so they formed a new "
               "group together rather than disturbing the existing ones.",
    },
    {
        "id": "ks4-development-periodic-table-e10",
        "subtopic_slug": "development-periodic-table",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State one reason why other scientists rejected Newlands' "
                "arrangement.",
        "options": [
            "He had refused to publish any of the measurements his arrangement "
            "rested on",
            "He forced elements into columns where the properties did not "
            "match",
            "He had ordered the elements by their melting points rather than by "
            "mass",
            "He had included several elements that nobody else had ever heard "
            "of",
        ],
        "correct_index": 1,
        "why": "With no gaps allowed, every later element was pushed into the "
               "next place along whether it belonged there or not.",
    },
    {
        "id": "ks4-development-periodic-table-e11",
        "subtopic_slug": "development-periodic-table",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State what scientists do with a model when new evidence does "
                "not fit it.",
        "options": [
            "They keep the model unchanged and set the evidence aside",
            "They wait for a second piece of evidence before doing anything",
            "They publish the evidence but leave the model to someone else",
            "They change the model, or replace it with a better one",
        ],
        "correct_index": 3,
        "why": "A model is judged by how well it accounts for the evidence, "
               "so evidence that does not fit forces a revision.",
    },
    {
        "id": "ks4-development-periodic-table-e12",
        "subtopic_slug": "development-periodic-table",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State which came first, Newlands' law of octaves or "
                "Mendeleev's table.",
        "options": [
            "Newlands' law of octaves",
            "Mendeleev's table",
            "The two were published in the same year",
            "Neither, because both came after Moseley's work",
        ],
        "correct_index": 0,
        "why": "Newlands set out his octaves first; Mendeleev's table came "
               "five years later and built on the same idea of periodicity.",
    },

    # ── standard ────────────────────────────────────────────────────
    {
        "id": "ks4-development-periodic-table-s05",
        "subtopic_slug": "development-periodic-table",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why the gaps in Mendeleev's table were a strength "
                "rather than a weakness.",
        "options": [
            "Each gap was a claim that could be tested, and testing it "
            "supported the pattern behind the whole table",
            "Each gap made the table shorter and therefore easier for a "
            "chemist to read and use",
            "Each gap allowed him to leave out an element whose properties he "
            "had not measured",
            "Each gap kept the columns the same length as one another",
        ],
        "correct_index": 0,
        "why": "A gap is a prediction; when germanium turned up with the "
               "predicted properties, the model was confirmed.",
    },
    {
        "id": "ks4-development-periodic-table-s06",
        "subtopic_slug": "development-periodic-table",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Germanium was discovered in 1886 and matched Mendeleev's "
                "predicted properties closely. Describe the effect this had.",
        "options": [
            "It forced Mendeleev to redraw his table around the new element, "
            "since no space had been left for it",
            "It persuaded the scientific community to accept his table",
            "It showed that ordering by relative atomic mass had been wrong "
            "all along, and that a new quantity was needed",
            "It had no effect, because germanium had already been predicted "
            "by Newlands some years earlier",
        ],
        "correct_index": 1,
        "why": "A successful prediction is the strongest evidence a model "
               "can offer, and this was one of three.",
    },
    {
        "id": "ks4-development-periodic-table-s07",
        "subtopic_slug": "development-periodic-table",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why Newlands' pattern broke down once he reached the "
                "heavier elements.",
        "options": [
            "The heavier elements had not had their relative atomic masses "
            "measured by anyone at the time when he was working",
            "Those elements repeat every ninth place rather than every eighth, "
            "and his rule made no allowance for that at all",
            "With no gaps left for undiscovered elements, each later element "
            "was pushed into a place that did not suit it",
            "The heavier elements were all metals, and his rule had been "
            "written for the non-metals",
        ],
        "correct_index": 2,
        "why": "Undiscovered elements shift everything after them along by "
               "one, and a rule with no gaps cannot absorb that.",
    },
    {
        "id": "ks4-development-periodic-table-s08",
        "subtopic_slug": "development-periodic-table",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Tellurium has a larger relative atomic mass than iodine, yet "
                "Mendeleev placed tellurium first. Suggest his reason.",
        "options": [
            "He had measured tellurium's relative atomic mass wrongly and "
            "never went back to check the figure",
            "He was ordering the two by their melting points at that point in "
            "the table rather than by mass",
            "He wanted each of his rows to contain the same number of "
            "elements as the row above it",
            "Tellurium's chemistry matched the group it went into, and he put "
            "chemical properties first",
        ],
        "correct_index": 3,
        "why": "Iodine behaves like the other halogens and tellurium does "
               "not, so strict mass order had to give way.",
    },
    {
        "id": "ks4-development-periodic-table-s09",
        "subtopic_slug": "development-periodic-table",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Describe how Mendeleev's table differed from a simple list "
                "of the elements that were known at the time.",
        "options": [
            "It set out a pattern that held for elements nobody had yet found",
            "It was written out in alphabetical order rather than by mass",
            "It contained every element that is known to chemists today",
            "It gave the relative atomic mass of each element to a greater "
            "number of decimal places than a list would",
        ],
        "correct_index": 0,
        "why": "A list records what is known; Mendeleev's table made claims "
               "about what was not yet known.",
    },
    {
        "id": "ks4-development-periodic-table-s10",
        "subtopic_slug": "development-periodic-table",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Three of Mendeleev's predicted elements were later found. "
                "Explain why three successes counted for more than one would "
                "have.",
        "options": [
            "Three elements filled every gap in his table, leaving nothing "
            "further to be predicted about it",
            "One correct prediction could be luck, while three make the "
            "pattern behind them far harder to doubt",
            "The three elements were heavier than the others, and heavier "
            "elements carry more weight as evidence",
            "Three elements gave chemists enough material to work with in a "
            "laboratory, where one would not have",
        ],
        "correct_index": 1,
        "why": "Repeating a successful prediction rules out coincidence, "
               "which is what makes evidence convincing.",
    },
    {
        "id": "ks4-development-periodic-table-s11",
        "subtopic_slug": "development-periodic-table",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "State what Mendeleev's arrangement could do that Newlands' "
                "could not.",
        "options": [
            "Place the elements in order of increasing relative atomic mass",
            "Group together elements whose chemical reactions were alike",
            "Set out the properties of elements that had not been discovered",
            "Show that the properties of the elements repeat at intervals",
        ],
        "correct_index": 2,
        "why": "Both men saw the repeating pattern; only Mendeleev used it to "
               "say what a missing element would be like.",
    },
    {
        "id": "ks4-development-periodic-table-s12",
        "subtopic_slug": "development-periodic-table",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why the periodic table is described as a model "
                "rather than as a record.",
        "options": [
            "Because it was drawn up by one person working alone",
            "Because chemists still disagree with one another about exactly "
            "where several of the elements ought to be placed",
            "Because several parts of it have still to be filled in by "
            "experiments that nobody has yet managed to carry out",
            "Because it explains why the elements behave as they do and "
            "predicts how ones not yet studied will behave",
        ],
        "correct_index": 3,
        "why": "A record stores observations; a model accounts for them and "
               "goes beyond them, which is what the table does.",
    },
    {
        "id": "ks4-development-periodic-table-s13",
        "subtopic_slug": "development-periodic-table",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest why Mendeleev's table was more useful to a working "
                "chemist than Newlands' arrangement was.",
        "options": [
            "Its columns held elements that genuinely behaved alike, so a "
            "chemist could predict a reaction from an element's position",
            "It was printed on one single sheet, so it could be pinned up on "
            "the wall of a laboratory in a way that Newlands' could not be",
            "It gave the relative atomic masses to more decimal places, which "
            "made calculations more accurate",
            "It listed a greater number of elements than any other "
            "arrangement available at the time",
        ],
        "correct_index": 0,
        "why": "A table is useful when position predicts behaviour, and "
               "Newlands' forced misfits broke that link.",
    },
    {
        "id": "ks4-development-periodic-table-s14",
        "subtopic_slug": "development-periodic-table",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Predict what would have happened to Mendeleev's table if the "
                "elements he predicted had never been found.",
        "options": [
            "Nothing, because a table is judged on the elements already in it "
            "rather than on the ones it predicts",
            "It would have been far less convincing, and chemists would have "
            "had good reason to doubt the pattern",
            "It would have been accepted anyway, because the gaps could "
            "simply have been closed up",
            "It would have been rejected outright the moment the first "
            "prediction went untested",
        ],
        "correct_index": 1,
        "why": "The predictions were the evidence; without them the table "
               "would have been one arrangement among several.",
    },
    {
        "id": "ks4-development-periodic-table-s15",
        "subtopic_slug": "development-periodic-table",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why ordering the elements by atomic number works "
                "better than ordering them by relative atomic mass.",
        "options": [
            "Atomic number is a whole number, and whole numbers are easier to "
            "place in order",
            "Atomic number is measured far more accurately than relative "
            "atomic mass is",
            "Atomic number fixes how many electrons an atom has, and the "
            "electrons are what decide an element's chemistry",
            "Atomic number rises more steeply along a row, so the elements "
            "are easier to tell apart",
        ],
        "correct_index": 2,
        "why": "Group and period follow from the electron arrangement, which "
               "follows from the proton count and not from the mass.",
    },
    {
        "id": "ks4-development-periodic-table-s16",
        "subtopic_slug": "development-periodic-table",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why two elements with almost the same relative "
                "atomic mass can sit far apart in the modern table.",
        "options": [
            "Because the modern table takes no account of mass at any point",
            "Because a similar mass usually means the two were discovered at "
            "about the same time, and discovery date sets the position",
            "Because the heavier of any two similar elements is always moved "
            "to the row below the other one",
            "Because position follows the proton count, and two elements of "
            "similar mass can have quite different proton counts",
        ],
        "correct_index": 3,
        "why": "Argon and calcium have masses of 40 either side, but 18 and "
               "20 protons, so they land in different groups and periods.",
    },
    {
        "id": "ks4-development-periodic-table-s17",
        "subtopic_slug": "development-periodic-table",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "State what Newlands was comparing the elements to when he "
                "chose the word octaves.",
        "options": [
            "The notes of a musical scale",
            "The eight sides of an octagon",
            "The eight legs of an octopus",
            "The eight planets then known",
        ],
        "correct_index": 0,
        "why": "In a musical scale the eighth note sounds like the first, "
               "which is the pattern he thought he saw in the elements.",
    },
    {
        "id": "ks4-development-periodic-table-s18",
        "subtopic_slug": "development-periodic-table",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest why comparing the elements to musical notes did "
                "Newlands' case no good with other chemists.",
        "options": [
            "Because the comparison had already been used by another chemist "
            "some years before he published his own version of it",
            "Because it sounded like a coincidence rather than a chemical "
            "reason, and his rule also broke down in places",
            "Because music and chemistry were taught by the same people at "
            "the time, so the comparison was thought obvious",
            "Because the scientists judging his work were musicians, and they "
            "did not accept that the comparison was a fair one",
        ],
        "correct_index": 1,
        "why": "A name borrowed from music offered no mechanism, and the "
               "pattern itself failed for the heavier elements.",
    },
    {
        "id": "ks4-development-periodic-table-s19",
        "subtopic_slug": "development-periodic-table",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why leaving a gap took more confidence than filling "
                "it with the next element along.",
        "options": [
            "A gap made the table longer, and a longer table was harder to "
            "print in the journals of the time",
            "A gap meant admitting that several of the measured masses must "
            "have been wrong",
            "A gap was a public claim that an unknown element existed, and it "
            "could be shown to be mistaken",
            "A gap left a column shorter than the others, which looked untidy "
            "beside a complete arrangement",
        ],
        "correct_index": 2,
        "why": "Filling in with the nearest element hides the problem; a gap "
               "states a testable claim that may fail.",
    },
    {
        "id": "ks4-development-periodic-table-s20",
        "subtopic_slug": "development-periodic-table",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Describe the rule Mendeleev followed when he decided where "
                "an element should go.",
        "options": [
            "Strict order of increasing relative atomic mass, with no "
            "departures allowed from it at all",
            "Order of increasing melting point, with the gases placed at the "
            "start of each of the rows",
            "Order of discovery, so that the elements found first came "
            "earliest in the arrangement",
            "Increasing relative atomic mass, except where chemical "
            "properties called for a swap",
        ],
        "correct_index": 3,
        "why": "Mass gave the backbone of the order and chemistry overruled "
               "it in the few places where the two disagreed.",
    },
    {
        "id": "ks4-development-periodic-table-s21",
        "subtopic_slug": "development-periodic-table",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "State what finally settled the question of whether "
                "Mendeleev's arrangement was right.",
        "options": [
            "Evidence — the predicted elements were found and matched",
            "A vote taken among the chemists of the day",
            "The opinion of the scientist with the greatest reputation",
            "The fact that his arrangement was the tidiest one available",
        ],
        "correct_index": 0,
        "why": "Scientific ideas are settled by evidence, and the found "
               "elements were exactly that.",
    },
    {
        "id": "ks4-development-periodic-table-s22",
        "subtopic_slug": "development-periodic-table",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Mendeleev's table held about 60 elements and the modern one "
                "holds 118. Suggest what this shows about a scientific model.",
        "options": [
            "That a model is wrong until the last piece of evidence for it "
            "has finally been gathered in",
            "That a model can grow as evidence accumulates without its main "
            "idea having to be abandoned",
            "That the number of elements in the universe has been rising "
            "steadily since Mendeleev's day",
            "That a model becomes less reliable the more observations are "
            "added to the ones it began with",
        ],
        "correct_index": 1,
        "why": "The periodic idea itself survived; what changed was how much "
               "evidence it had to account for.",
    },
    {
        "id": "ks4-development-periodic-table-s23",
        "subtopic_slug": "development-periodic-table",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why Mendeleev was able to move two elements out of "
                "mass order while Newlands was not.",
        "options": [
            "Newlands had far fewer elements to work with, so a move of that "
            "kind would have been noticed by everyone at once",
            "Newlands was ordering by melting point, which leaves no room for "
            "a move of that kind",
            "Newlands' rule fixed every element in the next place along, so "
            "nothing could be moved without breaking it",
            "Newlands had already moved several of his elements, and moving "
            "any more would have made his whole table useless",
        ],
        "correct_index": 2,
        "why": "An octave rule with no gaps and no swaps determines every "
               "position, so it cannot accommodate an awkward element.",
    },
    {
        "id": "ks4-development-periodic-table-s24",
        "subtopic_slug": "development-periodic-table",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Describe, in order, the three steps by which the periodic "
                "table reached the form used today.",
        "options": [
            "Ordering by atomic number, then by relative atomic mass, then "
            "grouping elements that behave alike",
            "Grouping elements that behave alike, then ordering by melting "
            "point, then ordering by relative atomic mass",
            "Ordering by relative atomic mass, then ordering by melting "
            "point, then ordering by atomic number",
            "A pattern spotted in mass order, then gaps left for missing "
            "elements, then reordering by atomic number",
        ],
        "correct_index": 3,
        "why": "Newlands saw the repeat, Mendeleev left the gaps, and "
               "Moseley replaced mass with atomic number.",
    },
    {
        "id": "ks4-development-periodic-table-s25",
        "subtopic_slug": "development-periodic-table",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest why so many elements were still undiscovered when "
                "Mendeleev drew up his table.",
        "options": [
            "Many are present in small amounts and are hard to separate from "
            "the compounds they occur in",
            "Many had been discovered but their discoverers had chosen not to "
            "publish any of the details",
            "Many are made in a laboratory, and there were no laboratories at "
            "the time he was working",
            "Many are gases, and no method of collecting a gas was known "
            "before the twentieth century",
        ],
        "correct_index": 0,
        "why": "Separating a rare element from its ore needed methods and "
               "instruments that came later.",
    },
    {
        "id": "ks4-development-periodic-table-s26",
        "subtopic_slug": "development-periodic-table",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Predict what Mendeleev would have done with an element whose "
                "properties matched none of his existing groups.",
        "options": [
            "Placed it in the nearest group and noted that the fit was poor",
            "Left it out and looked for a group it might belong to later",
            "Put it at the end of the table, after every other element",
            "Renamed one of his groups so that the new element would fit into "
            "it",
        ],
        "correct_index": 1,
        "why": "This is what happened with the noble gases: rather than being "
               "forced in, they eventually formed a group of their own.",
    },

    # ── harder ──────────────────────────────────────────────────────
    {
        "id": "ks4-development-periodic-table-h05",
        "subtopic_slug": "development-periodic-table",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Evaluate the claim that Mendeleev's table was accepted "
                "because it looked tidier than Newlands' arrangement.",
        "options": [
            "Sound — a tidy arrangement is what chemists were looking for at "
            "the time, and his was by far the tidiest",
            "Sound, because Newlands' arrangement had columns of unequal "
            "length and Mendeleev's did not",
            "Unsound — it was accepted because its predictions were tested "
            "and found to be right",
            "Unsound — it was accepted because Mendeleev was the better known "
            "of the two men",
        ],
        "correct_index": 2,
        "why": "Appearance persuades nobody in science; the discovery of "
               "germanium, gallium and scandium did.",
    },
    {
        "id": "ks4-development-periodic-table-h06",
        "subtopic_slug": "development-periodic-table",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a model that predicts new observations is "
                "valued more highly than one that only organises known facts.",
        "options": [
            "Because organising known facts is work that anyone can do, "
            "whereas a prediction takes real skill",
            "Because a model that organises facts cannot be written down in a "
            "form other scientists are able to check",
            "Because a prediction is always easier to test than an "
            "explanation of something already observed",
            "Because a prediction can turn out wrong, so a model that "
            "survives one has been tested against evidence it did not choose",
        ],
        "correct_index": 3,
        "why": "An arrangement of what is already known can always be made to "
               "fit; a prediction risks being refuted, and that is the test.",
    },
    {
        "id": "ks4-development-periodic-table-h07",
        "subtopic_slug": "development-periodic-table",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Mendeleev predicted eka-silicon would have a density of "
                "about 5.5 g/cm3; germanium's density is 5.32 g/cm3. Evaluate "
                "how well the prediction matched.",
        "options": [
            "Very well — the two agree to within about 0.2 g/cm3, which is "
            "close for a property predicted from a pattern alone",
            "Poorly — the two values differ, so the prediction has to be "
            "counted as a failure",
            "It cannot be judged, because a density has to be quoted at a "
            "stated temperature before the figure means very much",
            "Very well — the two values are identical once each has been "
            "rounded to the nearest whole number",
        ],
        "correct_index": 0,
        "why": "5.5 against 5.32 is a difference of about 3%, which is a "
               "strikingly good prediction for an unknown element.",
    },
    {
        "id": "ks4-development-periodic-table-h08",
        "subtopic_slug": "development-periodic-table",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest why Moseley's measurements could settle an argument "
                "that chemical evidence alone had not.",
        "options": [
            "They were carried out much later, and later measurements carry "
            "more authority than earlier ones do",
            "They gave a whole number for each element that no chemical test "
            "could argue with",
            "They were repeated by a great many other scientists, which no "
            "chemical test had been",
            "They measured relative atomic mass far more accurately than any "
            "earlier method had managed to",
        ],
        "correct_index": 1,
        "why": "A proton count is a fixed whole number for an element, so it "
               "gives an order with nothing left to interpret.",
    },
    {
        "id": "ks4-development-periodic-table-h09",
        "subtopic_slug": "development-periodic-table",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare the evidence Newlands had to work from with the "
                "evidence available to Moseley.",
        "options": [
            "Both had atomic numbers, but Moseley's numbers had been measured "
            "with the greater accuracy of the two",
            "Newlands had atomic numbers while Moseley worked from relative "
            "atomic masses and reaction data",
            "Newlands had masses and reactions only; Moseley could measure "
            "the proton count inside the atom itself",
            "Both had the same evidence in front of them, and the difference "
            "lay in how each of them chose to arrange it",
        ],
        "correct_index": 2,
        "why": "Subatomic particles were unknown in the 1860s, so the inside "
               "of the atom was simply not available as evidence.",
    },
    {
        "id": "ks4-development-periodic-table-h10",
        "subtopic_slug": "development-periodic-table",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why ordering by relative atomic mass and ordering by "
                "atomic number give the same sequence for nearly every "
                "element.",
        "options": [
            "Because relative atomic mass is defined as roughly twice the "
            "atomic number for all but a handful of elements",
            "Because the two orders were deliberately made to agree when the "
            "modern table was drawn up",
            "Because relative atomic mass has been re-measured time and again "
            "until it agrees with the atomic number order",
            "Because an atom with more protons usually has more neutrons too, "
            "so it is usually the heavier atom as well",
        ],
        "correct_index": 3,
        "why": "Mass and proton count climb together, so they disagree only "
               "where an element's isotope mixture is unusually heavy.",
    },
    {
        "id": "ks4-development-periodic-table-h11",
        "subtopic_slug": "development-periodic-table",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Argon has the larger relative atomic mass of argon and "
                "potassium, although it has the smaller proton count. Explain "
                "how that can happen.",
        "options": [
            "Argon's common isotope carries more neutrons than potassium's "
            "does, and neutrons add mass without adding proton number",
            "Argon's atoms hold extra electrons, and electrons contribute a "
            "great deal to the mass of an atom",
            "Argon is a gas, and the mass of a gas is measured differently "
            "from the mass of a solid",
            "Argon's relative atomic mass was measured long before "
            "potassium's was, and the method used at that time was far less "
            "accurate",
        ],
        "correct_index": 0,
        "why": "Argon is mostly argon-40 (18 protons, 22 neutrons) while "
               "potassium is mostly potassium-39 (19 protons, 20 neutrons).",
    },
    {
        "id": "ks4-development-periodic-table-h12",
        "subtopic_slug": "development-periodic-table",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Evaluate the statement: 'Newlands was simply wrong, so his "
                "work contributed nothing.'",
        "options": [
            "Sound — an idea that fails for the majority of the elements it "
            "covers adds nothing to the knowledge that came before it",
            "Unsound — he was the first to set out that the properties repeat "
            "at intervals, which is the idea the table rests on",
            "Sound — his pattern held for the first sixteen of the elements "
            "purely by coincidence and for no deeper reason than that",
            "Unsound — his arrangement was accepted at the time and was "
            "questioned many years later by the chemists who followed him",
        ],
        "correct_index": 1,
        "why": "Periodicity itself was his contribution; what failed was the "
               "rigid rule he expressed it with.",
    },
    {
        "id": "ks4-development-periodic-table-h13",
        "subtopic_slug": "development-periodic-table",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest why a scientist would choose to publish a "
                "prediction that could later be shown to be wrong.",
        "options": [
            "Because a prediction that fails can be quietly withdrawn later on "
            "without anyone noticing that it has gone at all",
            "Because publishing first secures the credit for any element "
            "another scientist later discovers",
            "Because a claim that can be tested and survives the test is far "
            "stronger evidence than one nobody can check",
            "Because a journal will not accept a paper unless it contains a "
            "prediction of some kind",
        ],
        "correct_index": 2,
        "why": "A claim that could not fail proves nothing; the risk is what "
               "gives a successful prediction its weight.",
    },
    {
        "id": "ks4-development-periodic-table-h14",
        "subtopic_slug": "development-periodic-table",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Determine which of these elements was NOT among those "
                "Mendeleev predicted from a gap in his table.",
        "options": [
            "Gallium",
            "Germanium",
            "Scandium",
            "Argon",
        ],
        "correct_index": 3,
        "why": "Argon was found in 1894 with no gap waiting for it; the noble "
               "gases formed a new group instead.",
    },
    {
        "id": "ks4-development-periodic-table-h15",
        "subtopic_slug": "development-periodic-table",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Mendeleev's table held about 60 elements and the modern one "
                "holds 118. Calculate the percentage increase, to the nearest "
                "whole number.",
        "options": [
            "97%",
            "58%",
            "49%",
            "197%",
        ],
        "correct_index": 0,
        "why": "The increase is 118 − 60 = 58, and 58 ÷ 60 × 100 = 96.7%, "
               "which is 97% to the nearest whole number.",
    },
    {
        "id": "ks4-development-periodic-table-h16",
        "subtopic_slug": "development-periodic-table",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare what fixed an element's place in Mendeleev's table "
                "with what fixes it in the modern one.",
        "options": [
            "Mendeleev used the proton count while the modern table uses "
            "relative atomic mass",
            "Mendeleev used mass, overruled by chemical properties; the "
            "modern table uses proton count alone",
            "Both use relative atomic mass, and the difference between them "
            "lies in how many elements each contains",
            "Mendeleev used chemical properties alone while the modern table "
            "uses melting and boiling points",
        ],
        "correct_index": 1,
        "why": "Proton count needs no override, because it is the thing that "
               "sets the electron arrangement and so the chemistry.",
    },
    {
        "id": "ks4-development-periodic-table-h17",
        "subtopic_slug": "development-periodic-table",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest why the noble gases were among the last of the "
                "common elements to be discovered.",
        "options": [
            "They occur in rocks deep underground, and those rocks could not "
            "be reached by anyone until the 1890s",
            "They were mistaken for one another, so a single gas was long "
            "thought to be the whole of the group",
            "They form almost no compounds, so there was very little for a "
            "chemical test to detect them by",
            "They were known much earlier but were counted as mixtures rather "
            "than as elements",
        ],
        "correct_index": 2,
        "why": "Nineteenth-century chemistry found an element through its "
               "reactions, and these gases would hardly react at all.",
    },
    {
        "id": "ks4-development-periodic-table-h18",
        "subtopic_slug": "development-periodic-table",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Evaluate the claim that the modern table could not have "
                "been drawn before subatomic particles were discovered.",
        "options": [
            "Unsound — the modern order could have been worked out from "
            "chemical reactions alone, given enough of them",
            "Unsound — a table of that kind needs nothing beyond the relative "
            "atomic masses, which were already known",
            "Sound — but only because the instruments needed were invented at "
            "about the same time as the particles were found",
            "Sound — the modern order is by proton count, and nobody can "
            "count protons before knowing that protons exist",
        ],
        "correct_index": 3,
        "why": "The ordering quantity itself was unavailable, which is why "
               "mass had to serve as a stand-in for it.",
    },
    {
        "id": "ks4-development-periodic-table-h19",
        "subtopic_slug": "development-periodic-table",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why re-measuring an element's relative atomic mass "
                "more precisely never changes its place in the modern table.",
        "options": [
            "Because position is set by the proton count, and re-measuring a "
            "mass leaves the proton count untouched",
            "Because relative atomic masses are rounded before they are "
            "printed, so small changes disappear",
            "Because the elements are too far apart in mass for any "
            "re-measurement to reach a neighbour's value",
            "Because a relative atomic mass, once published, is not allowed "
            "to be changed by later work",
        ],
        "correct_index": 0,
        "why": "Mass is printed on the table but no longer orders it, which "
               "is precisely the improvement Moseley made.",
    },
    {
        "id": "ks4-development-periodic-table-h20",
        "subtopic_slug": "development-periodic-table",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A newly made element is placed in Group 2 of a later "
                "period. Suggest what chemists would expect of it before any "
                "test was run.",
        "options": [
            "That it would be an unreactive gas, forming no compounds with any "
            "of the other elements in the table",
            "That it would be a metal forming a 2+ ion, and more reactive "
            "than the Group 2 elements above it",
            "That it would be a brittle non-metal forming a 2- ion, in the way "
            "the elements above it in the group do",
            "That nothing could be expected of it until it had been tested in "
            "a laboratory by somebody or other",
        ],
        "correct_index": 1,
        "why": "This is exactly the reasoning Mendeleev used: a position in "
               "the pattern carries the properties of its neighbours.",
    },
    {
        "id": "ks4-development-periodic-table-h21",
        "subtopic_slug": "development-periodic-table",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Evaluate which of Newlands and Mendeleev made the larger "
                "contribution to the table we use now.",
        "options": [
            "Newlands, because ordering the elements by mass was the harder "
            "of the two pieces of work",
            "Mendeleev, because he was the only one of the two to notice that "
            "the properties repeat at intervals",
            "Mendeleev, because the gaps and predictions turned a pattern "
            "into a model that could be tested",
            "Neither, because the modern table came entirely from Moseley's "
            "work and owes nothing to either of them",
        ],
        "correct_index": 2,
        "why": "Newlands supplied the idea of periodicity, but it was the "
               "testable predictions that made the table science.",
    },
    {
        "id": "ks4-development-periodic-table-h22",
        "subtopic_slug": "development-periodic-table",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why Mendeleev could not have known that his "
                "ordering rule would one day need correcting.",
        "options": [
            "Because he had not measured the relative atomic masses himself "
            "and so could not judge how reliable they were",
            "Because the elements that break mass order had not yet been "
            "discovered when he was working",
            "Because he had never intended his arrangement to be more than a "
            "temporary convenience",
            "Because the reason for the exceptions lies inside the atom, and "
            "the inside of the atom was unknown to him",
        ],
        "correct_index": 3,
        "why": "Isotopes and proton counts explain the reversals, and neither "
               "idea existed in 1869.",
    },
    {
        "id": "ks4-development-periodic-table-h23",
        "subtopic_slug": "development-periodic-table",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Deduce what has to be true of two elements for them to swap "
                "places when the ordering changes from mass to proton count.",
        "options": [
            "The heavier of the two must have the smaller proton count",
            "The two must have exactly the same proton count as one another does",
            "The lighter of the two must be a gas and the heavier a solid",
            "The two must sit in the same group of the table",
        ],
        "correct_index": 0,
        "why": "Only then do the two orderings disagree; argon and potassium "
               "are the standard example.",
    },
    {
        "id": "ks4-development-periodic-table-h24",
        "subtopic_slug": "development-periodic-table",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Mendeleev predicted eka-boron would have a relative atomic "
                "mass of about 44; scandium's is 45. Calculate the percentage "
                "difference from the measured value, to the nearest whole "
                "number.",
        "options": [
            "1%",
            "2%",
            "4%",
            "44%",
        ],
        "correct_index": 1,
        "why": "The difference is 1, and 1 ÷ 45 × 100 = 2.2%, which is 2% to "
               "the nearest whole number.",
    },
    {
        "id": "ks4-development-periodic-table-h25",
        "subtopic_slug": "development-periodic-table",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why Mendeleev's decision to put chemistry ahead of "
                "mass turned out to be the right one.",
        "options": [
            "Because his measured masses were later shown to have been wrong "
            "in exactly those places",
            "Because chemistry is a more reliable guide than any measurement "
            "made with an instrument",
            "Because the proton count, which really does set the order, "
            "happens to agree with the chemistry and not with the mass",
            "Because the elements he moved were later found to belong in "
            "neither of the groups concerned",
        ],
        "correct_index": 2,
        "why": "Chemistry follows the electron arrangement, which follows "
               "proton count — so it was the better guide all along.",
    },
    {
        "id": "ks4-development-periodic-table-h26",
        "subtopic_slug": "development-periodic-table",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Evaluate the claim that the modern table is simply "
                "Mendeleev's table with more elements added to it.",
        "options": [
            "Sound — the layout is the same and the only change has been the "
            "arrival of further elements",
            "Sound, provided the noble gases are counted as one more of the "
            "additions rather than as a change to the rule itself",
            "Unsound — the modern table shares none of its features with the "
            "arrangement that Mendeleev once published",
            "Unsound — the elements were added, but the ordering quantity "
            "itself changed from mass to proton count",
        ],
        "correct_index": 3,
        "why": "The shape survives, but the rule underneath it was replaced, "
               "and that is what removed the exceptions.",
    },
]
