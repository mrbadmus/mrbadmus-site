"""C8 L2 — Mendeleev and the table that predicted (MODEL).

Authored against Claude Design's approved page,
`docs/ks3/design-reference/c8/c8-02-mendeleev-and-the-table-that-predicted.dc.html`,
and her author's notes `NOTES-C8.md` §1, §3, §4, §5 flags 5–8, §6 (`PTAB-03`,
`PTAB-04`) and §7.

⚠️ THE SLUG IS `structure.py`'s, NOT THE PAGE'S. Design's file is
`c8-02-mendeleev-and-the-table-that-predicted`; the skeleton's slot is
`mendeleev`. The slug is permanent (§8.4) and it is what every index,
breadcrumb and rail link already points at. The TITLE is the page's — "Mendeleev
and the table that predicted" — because a title is not a URL. Nothing else
moves. Same call `ks3_data/c6/lesson_04_acid_plus_metal.py` made.

── ⭐ THE ARCHETYPE MOVED BACK TO MODEL (MRB-281, R3) ────────────────────

`structure.py` carried this slot as INVESTIGATION, and `NOTES-C8.md` §2 records
that the archetype "was authored as MODEL and has been corrected to
INVESTIGATION per §7", while noting that the lesson body "was written to the
MODEL shape and still reads as one".

**The correction ran the wrong way and is reversed.** An archetype describes
what the STUDENT DOES, and what the student does here is predict into a gap
from neighbouring elements — there is no plan to critique, no variable to
control and no messy data to evaluate, which is the whole of what §6's
INVESTIGATION family is. §7's label was aspirational; the lesson is the
artefact and the measurement, so the LABEL changes.

⊕ Two adjacent MODELs (this lesson and c8-03) is fine and was ruled so: §6's
warning is against an identical block LINEUP arriving as a default, and a
gap-filler with a 3 x 3 neighbour grid and a tappable twenty-element table are
not the same instrument in any respect but their family name.

── ⚑ MRB-278 · ANSWER POSITION ──────────────────────────────────────────

This lesson holds **index 2** (recall) and **index 3** (apply) of C8's twelve.
Design put both at index 0. Only the ORDER moves; every option keeps its text
except where MRB-177 required the DISTRACTOR re-authored, and every `feedback`
key is re-keyed to the index its own option now sits at.

⚑ AND BOTH RUNGS' DISTRACTORS ARE RE-AUTHORED FOR LENGTH (MRB-177). Design's
recall answer is 11 words against 3, 7 and 6; her apply answer is 14 against 8,
9 and 8. In both the answer is the long one and can be picked without reading
it. The fix is made AT THE DISTRACTOR — each is rewritten as a wrong RULE in
the answer's own shape, not trimmed from the answer.

── SCIENCE FLAGS, AND THE COMMANDER'S RULINGS ───────────────────────────

⚑ Flag 5 — germanium's figures: predicted mass 72 against measured 72.6,
predicted density 5.5 against 5.32, predicted oxide XO2 against GeO2. KEPT
(R4), all correct as historically recorded.

⚑ Flag 6 — NEWLANDS STAYS, AND THE FRAMING IS THE RULING (R4). The anecdote is
kept because it is **what was done to him**, not our verdict on him: the page
says he "was laughed at for it" and that "one chemist asked whether he had
tried arranging the elements alphabetically". Both are reports of the
profession's behaviour in 1866. Nothing on the page calls his work wrong — it
was not — and the point the anecdote carries is that ridicule is not an
argument, which is the same point the lesson makes about tidiness.

⚑ Flag 7 — the tellurium / iodine swap explained by proton number, including
"he got the right answer for a reason he could not have known". KEPT. This is
the nature-of-science framing and it is the best sentence on the page.

⚑ Flag 8 — the noble gases absent from Mendeleev's table. KEPT and correct:
argon was isolated in 1894, twenty-five years after the table. It sets up
c8-06's hook.

⚑ FONT LAW, CORRECTED 30 Aug 2026 (MRB-295/MRB-302 close-out). This used to
say the oxide formulae here are ALL plain digits because "markup is not
available" through an instrument hole. That was never true — every one of
these strings passes through `sci()`/`rich()` same as any other lesson prose,
which is exactly why `SiO2`, `SnO2` and `GeO2` render with real `<sub>`
digits on the built page. `XO2` and `X2O3` were the odd ones out, and for a
different reason: `X` is Mendeleev's placeholder for an undiscovered
element, and `ks3_art/kit.py`'s formula regex only subscripted a token where
every symbol was a genuine element — correctly, since that is what stops it
mangling lesson codes like `C1` or `KS3` — so it declined to touch `X`.
Hand-authoring `<sub>` here does NOT fix it: `sci()` escapes its input before
scanning for formulae (options and table cells are data, never a markup
pass-through — R3), so a hand-typed tag comes out as the literal characters
`&lt;sub&gt;`, which is worse than plain digits. The actual fix is in
`ks3_art/kit.py`: `X` is now in the recognised symbol set FOR THIS PURPOSE
ONLY (subscripting), commented there as Mendeleev's placeholder rather than
a real element, so it needs no special-casing here — `XO2` and `X2O3` are
still authored flat, same as `SiO2`, and render subscripted wherever
`sci()`/`rich()` already touches them.
"""

LESSON = {
    "slug":  "mendeleev",
    "title": "Mendeleev and the table that predicted",
    "discipline": "chemistry",
    "unit": "The periodic table",
    "family": "MODEL",

    "covers": ["KS3.C.PT.02"],
    # The lesson USES the group idea throughout without owning it — PT.03a is
    # c8-03's. `touches` is the ungated field and this is what it is for.
    "touches": ["KS3.C.PT.03a"],
    "beyond_statutory": False,
    "threads": [{"id": "substances-and-reactions", "level": 3},
                {"id": "how-science-works", "level": 3}],
    "typical_year": 8,
    "typical_minutes": 55,

    "requires": ["metals-and-non-metals"],
    "assumes": [],
    "references": ["elements", "chemical-symbols"],
    "connects_heading": "Next in this unit",
    "ks4_links": [],

    "big_question": "Mendeleev described an element nobody had ever seen, "
                    "down to the density of the metal and the formula of its "
                    "oxide, and fifteen years later somebody dug it out of a "
                    "silver mine. How do you describe something that has not "
                    "been found?",

    "rail": [
        {"anchor": "s-hook",   "short": "HOOK",
         "label": "Sixty-three cards",     "done_when": "committed"},
        {"anchor": "s-gap",    "short": "GAP",
         "label": "Fill the gap",          "done_when": "all_three_predicted"},
        {"anchor": "s-rules",  "short": "CALLS",
         "label": "Three decisions",       "done_when": "all_three_decided"},
        {"anchor": "s-think",  "short": "THINK",
         "label": "Tidy is not the reason", "done_when": "committed"},
        {"anchor": "s-ladder", "short": "LADDER",
         "label": "Mastery ladder",        "done_when": "ladder_complete"},
    ],

    "phenomenon": {
        "kind": "narrative",
        "title": "Sixty-three elements, written on cards, laid out on a desk "
                 "in order of mass. Every eighth card, the properties come "
                 "round again.",
        "prompt": "Lay the cards in a long line and something odd shows up: "
                  "soft reactive metal, then several ordinary metals, then a "
                  "violent gas — and then a soft reactive metal again. The "
                  "pattern repeats. Cut the line into rows so the repeats "
                  "fall underneath each other and you have a table where "
                  "every column is a family.",
        "commit": "Except the pattern breaks in places. What should you do "
                  "when an element does not fit the column it lands in?",
        "options": [
            "Move the next element up so there are no holes",
            "Leave the square empty for something not yet discovered",
            "Start the whole table again in a different order",
            "Put it in the column anyway and ignore the mismatch",
        ],
        "reveal": "Leave a <strong>gap</strong>. Dmitri Mendeleev's decision "
                  "was that the pattern mattered more than the list of known "
                  "elements: if nothing known fitted the square, the square "
                  "belonged to something not yet discovered. He left several "
                  "empty, described what each missing element would be like, "
                  "and waited. Within seventeen years three of them had been "
                  "found — and they matched.",
    },

    "misconceptions": [
        {"id": "PTAB-03",
         "statement": "Mendeleev's table was accepted because it was tidy.",
         "elicited_by": "think-commit-tidy",
         "confronted_by": "think-commit-tidy"},

        # ⚑ NOTES-C8 §6 proposes `decision-3` / `decision-3-reveal`. Neither
        # is emitted: `r_predict_cards` gives each card a `data-pcard-card`
        # value, which is not an `id` and not a `data-activity`, so both would
        # name a real place in the author's head and no element the MRB-244
        # gate can resolve. The join names the ACTIVITY that owns both the
        # commitment and the reveal — the third decision IS the confrontation,
        # and it is on this block.
        {"id": "PTAB-04",
         "statement": "A gap in a table is a weakness in it.",
         "elicited_by": "rules-three",
         "confronted_by": "rules-three"},
    ],

    # ── the confrontation (Law 3) ───────────────────────────────────────
    # ⚠️ AUTHORED IN `activities`, NOT LIFTED FROM `core`. `_normalise`
    # lifts INSTRUMENT kinds only, so a `misconception` core block whose id
    # names no activity renders as NOTHING AT ALL — `r_activity` returns an
    # empty string and the section, its `id`, its `data-activity` and its
    # rail stop all vanish. The page still builds and still reads.
    #
    # ⚑ The QUOTE is not authored here: `_confrontations` takes it from the
    # row for `targets` in `docs/ks3/misconception-register.md`, so the
    # register and the page have one source and cannot drift.
    "activities": [
        {"id": "think-commit-tidy",
         "kind": "predict",
         "demand": "explain",
         "targets": "PTAB-03",
         "prompt": "Several chemists had noticed the repeating pattern before him."
                    " Commit before you read on.",
         "options": [
             "Right — it was the neatest arrangement anyone had produced",
             "Wrong — it was accepted because its predictions about missing"
             " elements came true",
             "Right, because he was the first to spot the repeating pattern",
             "Wrong — it was accepted because he was a famous chemist",
         ],
         "reveal": [
             "Tidiness convinces nobody. John Newlands had published a"
             " repeating pattern five years earlier and was laughed at for it"
             " — one chemist asked whether he had tried arranging the"
             " elements alphabetically. What Mendeleev's table did that the"
             " others did not was <strong>make predictions that could have"
             " been wrong</strong>.",
             "He named three missing elements and gave their masses,"
             " densities and the formulae of their compounds. Gallium turned"
             " up in 1875, scandium in 1879, germanium in 1886, and each one"
             " matched. <strong>An arrangement that only organises what you"
             " already know is a filing cabinet. One that tells you what you"
             " will find is a theory.</strong>",
         ]},
    ],

    "core": [
        {"type": "hook", "anchor": "s-hook", "id": "hook-commit"},

        {"type": "explainer",
         "text": "Mendeleev arranged the elements in order of "
                 "<strong>atomic mass</strong> and started a new row whenever "
                 "the properties began repeating. Elements with similar "
                 "behaviour ended up in the same column, which he called a "
                 "<strong>group</strong>."},
        {"type": "explainer",
         "text": "Two decisions made his table different from everyone "
                 "else's. He left <strong>gaps</strong> for elements not yet "
                 "found, and he <strong>swapped</strong> a few pairs out of "
                 "mass order when their properties demanded it. Both looked "
                 "like cheating at the time. Both turned out to be right."},

        # ── #s-gap — the gap-filler. Three parts, one rail stop.
        {"type": "gap-filler", "id": "gap-germanium", "anchor": "s-gap",
         "eyebrow": "Your turn · fill the gap",
         "heading": "Here is the square Mendeleev left empty. Its neighbours "
                    "are all you get.",
         "demand": "predict",
         "lead": "The missing element sits between silicon above and tin "
                 "below. Predict what it will be like from the elements "
                 "around it — that is exactly what Mendeleev did in 1871, "
                 "fifteen years before anyone found it.",
         "head_counter": {"format": "{n} of {total} predicted", "start": 0,
                          "total": 3},
         "cols": 3,
         "blank_label": "the missing element, below silicon and above tin",
         # ⚠️ FOUR CORNERS ARE `empty` SPACERS AND THE CENTRE IS THE `blank`
         # GAP. They are different things — see `r_gap_filler`. The grid is a
         # plus-shape cut out of the table, so the gap has a neighbour on all
         # four sides, which is what makes the prediction a reading rather
         # than a guess.
         "grid": [
             {"empty": True},
             {"symbol": "Si", "name": "Silicon", "data": "mass 28 · density 2.3"},
             {"empty": True},
             {"symbol": "Ga", "name": "Gallium", "data": "mass 70 · density 5.9"},
             {"blank": True},
             {"symbol": "As", "name": "Arsenic", "data": "mass 75 · density 5.7"},
             {"empty": True},
             {"symbol": "Sn", "name": "Tin", "data": "mass 119 · density 7.3"},
             {"empty": True},
         ],
         "predictions": [
             {"id": "p1",
              "q": "Silicon above has a mass of 28 and tin below has a mass "
                   "of 119. What mass would you predict for the missing "
                   "element?",
              "options": [{"id": "a", "label": "About 40"},
                          {"id": "b", "label": "About 72"},
                          {"id": "c", "label": "About 110"}],
              "answer": "About 72 — roughly halfway between its neighbours "
                        "above and below, which is how every other column in "
                        "the table behaves. Mendeleev predicted 72. The "
                        "measured value is 72.6."},
             {"id": "p2",
              "q": "Gallium to the left has a density of 5.9 and arsenic to "
                   "the right has 5.7. What density would you predict?",
              "options": [{"id": "a", "label": "About 2"},
                          {"id": "b", "label": "About 5.5"},
                          {"id": "c", "label": "About 9"}],
              "answer": "About 5.5 — between the two neighbours in the same "
                        "row. Mendeleev predicted 5.5 exactly. Germanium "
                        "turned out to be 5.32."},
             {"id": "p3",
              "q": "Silicon forms an oxide with the formula SiO2 and tin "
                   "forms SnO2. What formula would you predict for the "
                   "missing element's oxide?",
              "options": [{"id": "a", "label": "XO"},
                          {"id": "b", "label": "XO2"},
                          {"id": "c", "label": "X2O3"}],
              "answer": "XO2. Elements in the same group combine in the same "
                        "ratios — that is the most useful thing a group tells "
                        "you. Germanium oxide is GeO2, exactly as the column "
                        "requires."},
         ],
         "table_caption": "In 1886 the square was filled. The element is "
                          "germanium.",
         "predicted_head": "Mendeleev, 1871",
         "actual_head": "Measured, 1886",
         "table": [
             {"prop": "Atomic mass", "predicted": "72", "actual": "72.6"},
             {"prop": "Density", "predicted": "5.5 g/cm³",
              "actual": "5.32 g/cm³"},
             {"prop": "Appearance", "predicted": "dark grey solid",
              "actual": "greyish-white, shiny, brittle"},
             {"prop": "Formula of oxide", "predicted": "XO2",
              "actual": "GeO2"},
         ],
         "close_id": "gap-close",
         "close": [
             "Nobody had seen this element. Mendeleev described it from an "
             "empty square, and a German chemist dug it out of a silver mine "
             "fifteen years later and found the description fitted. "
             "<strong>That is the moment the table stopped being a filing "
             "system and became a theory.</strong>",
         ]},

        {"type": "key-fact", "ref": "gaps-were-filled"},

        # ── #s-rules — three decisions. `predict-cards`, placement 1 of 5.
        {"type": "predict-cards", "id": "rules-three", "anchor": "s-rules",
         "eyebrow": "Three decisions",
         "heading": "Would you have made the same calls?",
         "demand": "judge",
         "lead": "Each of these was a real objection raised against the table "
                 "at the time. Commit before you read.",
         "head_counter": {"format": "{n} of {total} decided", "start": 0,
                          "total": 3},
         # Design builds these two buttons as JS literals. Authored here
         # instead — emit-both-show-one, and a string a student reads should
         # not live in a renderer.
         "items": [
             {"id": "d1",
              "q": "No element known in 1869 fitted the square below silicon. "
                   "Mendeleev left it empty rather than moving the next "
                   "element up. Was that justified?",
              "options": [{"id": "yes", "label": "Justified"},
                          {"id": "no", "label": "Not justified"}],
              "answer": "Justified, and it was the boldest thing in the "
                        "table. Moving the next element up would have hidden "
                        "the problem and broken the column below it. Leaving "
                        "a gap turned an inconvenience into a prediction — "
                        "and a prediction can be checked, which is what "
                        "happened seventeen years later."},
             {"id": "d2",
              "q": "Tellurium has a greater atomic mass than iodine, but "
                   "iodine behaves like the other elements in the column "
                   "tellurium would land in. Mendeleev swapped them. Was that "
                   "justified?",
              "options": [{"id": "yes", "label": "Justified"},
                          {"id": "no", "label": "Not justified"}],
              "answer": "Justified. He trusted the chemistry over the "
                        "measurement, and assumed the masses had been "
                        "measured wrong. The masses were right — but the "
                        "table was still correct, because the true order is "
                        "by number of protons, not by mass. Tellurium has 52 "
                        "and iodine 53. He got the right answer for a reason "
                        "he could not have known."},
             {"id": "d3",
              "q": "A critic pointed out that the table contained squares "
                   "with nothing in them, and called it incomplete. Was that "
                   "a fair criticism?",
              "options": [{"id": "yes", "label": "Fair"},
                          {"id": "no", "label": "Not fair"}],
              "answer": "Fair at the time and wrong in the end. An empty "
                        "square is only a weakness if it stays empty. Every "
                        "gap Mendeleev left was filled within thirty years by "
                        "an element with the properties he had written down, "
                        "and the gaps became the strongest evidence that the "
                        "arrangement was real rather than convenient."},
         ]},

        {"type": "keyword", "anchor": "s-words",
         "eyebrow": "Five words",
         "lead": "Say your answer out loud before you turn each card over. "
                 "If you cannot say it, you do not know it yet.",
         "terms": ["Periodic table", "Atomic mass", "Group", "Prediction",
                   "Atomic number"]},

        {"type": "misconception", "id": "think-commit-tidy",
         "anchor": "s-think", "targets": "PTAB-03"},

        {"type": "quiz", "anchor": "s-ladder"},
        {"type": "summary"},
    ],

    "figures": [],

    "key_facts": [
        {"id": "gaps-were-filled", "placement": "top-level", "ground": "card",
         "eyebrow": "Key fact",
         "text": "Mendeleev ordered the elements by mass, started a new row "
                 "where the properties repeated, and left gaps for elements "
                 "nobody had found. The table was accepted because those gaps "
                 "were filled by exactly what he described."},
    ],

    "ladder": {
        # index 2 — moved from Design's 0; distractors re-authored (MRB-177).
        "recall": {
            "q": "How did Mendeleev order the elements in his table?",
            "options": [
                "Alphabetically by name, so that any element could be looked "
                "up quickly",
                "By the year of discovery, starting a new row for each decade",
                "By atomic mass, starting a new row where the properties "
                "repeated",
                "By how dangerous each one is, with the safest elements first",
            ],
            "answer": 2,
            "feedback": {
                0: "That was suggested as a joke against an earlier chemist. "
                   "Alphabetical order groups nothing.",
                1: "Discovery order tells you about history, not chemistry.",
                3: "There is no such scale, and it would not produce "
                   "repeating families.",
            }},

        # index 3 — moved from Design's 0; distractors re-authored (MRB-177).
        "apply": {
            "q": "Why is leaving a gap in a table stronger evidence than "
                 "filling every square?",
            "options": [
                "Because a table with no holes in it looks more scientific to "
                "a reader",
                "Because it leaves room for new elements to be invented later "
                "on",
                "Because a table with every square filled would be far too "
                "long",
                "Because the gap is a prediction that could later be shown to "
                "be wrong",
            ],
            "answer": 3,
            "feedback": {
                0: "Appearance persuades nobody. The strength is that a gap "
                   "can be tested.",
                1: "Elements are discovered, not invented — and the gap "
                   "specified what would be found.",
                2: "Length was never the issue. The issue was whether the "
                   "pattern was real.",
            }},

        "explain": {
            "q": "Explain how Mendeleev was able to describe germanium "
                 "fifteen years before it was discovered, and why chemists "
                 "took the table seriously once it was found.",
            "field_label": "Your explanation",
            "placeholder": "He used the elements around the gap to…",
            "success": [
                "Says he used the properties of the neighbouring elements "
                "above, below and either side.",
                "Says the element in a gap should fall between its "
                "neighbours in mass and density.",
                "Says elements in the same group form compounds with the same "
                "formulae.",
                "Says the measured properties of germanium matched the "
                "prediction closely.",
                "Says a successful prediction is stronger evidence than an "
                "arrangement of known facts.",
            ]},

        "produce": {
            "q": "A student arranges twenty unknown substances into a table "
                 "by colour, and every column looks neat. Explain what would "
                 "have to happen before that table could be called "
                 "scientifically useful.",
            "field_label": "Your answer",
            "placeholder": "A neat table is not enough because…",
            "success": [
                "Says a neat arrangement on its own only organises what is "
                "already known.",
                "Says the table would need to predict something not yet "
                "measured.",
                "Says that prediction must be specific enough to be wrong.",
                "Says the prediction then has to be tested against new "
                "evidence.",
                "Says colour may have nothing to do with the substances' "
                "behaviour, unlike mass and reactivity.",
            ]},
    },

    "key_note": "Mendeleev arranged the known elements in order of atomic "
                "mass and began a new row each time the properties repeated, "
                "so that similar elements fell into the same column. He left "
                "gaps for undiscovered elements and predicted their "
                "properties, and he swapped pairs that were out of order. "
                "When gallium, scandium and germanium were found and matched "
                "his descriptions, the table was accepted.",

    "stretch": [
        {"type": "explainer", "id": "why-it-works",
         "text": "Mendeleev never knew why his table worked. Atoms were still "
                 "thought to be indivisible, and the reason elements repeat "
                 "every so often — the arrangement of electrons around the "
                 "nucleus — was fifty years away. The modern table is ordered "
                 "by atomic number, the number of protons, rather than mass, "
                 "and that single change quietly repairs every pair Mendeleev "
                 "had to swap by hand. Tellurium and iodine sit in the right "
                 "order because tellurium has 52 protons and iodine 53, "
                 "whatever their masses do."},
        {"type": "explainer", "id": "the-missing-column",
         "text": "One whole column was missing from his table and he never "
                 "suspected it. The noble gases had not been discovered in "
                 "1869, because they react with nothing and so leave no trace "
                 "in any compound. When argon was isolated in 1894 it fitted "
                 "nowhere at all — until someone realised the table needed a "
                 "new group on the end. A theory that can absorb an entire "
                 "unexpected family without collapsing is a strong one."},
    ],

    "support": [],

    "vocabulary": [
        {"term": "Periodic table",
         "definition": "The arrangement of all the elements in order, set out "
                       "so that elements with similar properties fall in the "
                       "same column.",
         "note": "Periodic means the pattern comes round again."},
        {"term": "Atomic mass",
         "definition": "How heavy one atom of an element is compared with "
                       "the others.",
         "note": "The order Mendeleev used, and not quite the right one."},
        {"term": "Group",
         "definition": "A column of the periodic table. The elements in it "
                       "behave alike and form compounds with the same "
                       "formulae.",
         "note": "Mendeleev's own word for it."},
        {"term": "Prediction",
         "definition": "A statement about something not yet measured, "
                       "specific enough that it could turn out to be wrong.",
         "note": "The thing that separates a theory from a filing cabinet."},
        {"term": "Atomic number",
         "definition": "The number of protons in an atom. The modern table is "
                       "ordered by this rather than by mass.",
         "note": "Unknown in 1869, and it fixes every swap he had to make."},
    ],

    "safety_note": "",

    "tutor": {"prompt": "Ask Mr Badmus AI",
              "body": "Still not sure how you predict an element nobody has "
                      "seen?",
              "cta": "Ask about this lesson",
              "anchor": "s-gap"},

    "ks4_becomes": "Ordering by atomic number, electron configuration as the "
                   "reason for the repeat, and why the noble gases were "
                   "missed.",

    "ws": ["analysis-and-evaluation"],
    "review_state": "draft",
}
