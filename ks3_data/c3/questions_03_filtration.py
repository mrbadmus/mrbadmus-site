"""C3 lesson 03 — Filtration: twelve questions (MRB-269).

The lesson's argument is one sentence long — filtration separates an
insoluble solid from a liquid and never separates anything dissolved — and
everything else on the page is either how to do it without ruining it, or what
follows from the second half of that sentence. These twelve probe the angles
the mastery ladder leaves alone: the REASON behind each step rather than its
order, what a wrong order actually does on the bench, and the second half of
the sentence carried into places the lesson does not visit.

The distractors are built from the lesson's two declared misconceptions.
MIX-06 (filtered water is clean water) drives the wrong options in e02, s04,
h02 and h03 — each of them treats "the water looks different" as "the water
is different", and each is the mistake that ends with somebody drinking it.
MIX-07 (a fine enough filter would separate salt from water) drives e01, e03,
s02, h01 and h04, where fineness, a second pass, a fold or a pressure is
imagined to do what no gap in any paper can. A third strand, everywhere in the
stepper and in neither register entry, is that a step's reason is the obvious
one: that the funnel tip touches the wall for speed, that the paper is wetted
to hold it still, that rinsing is tidiness. e04, s01, s03 and h02 each carry a
distractor that does exactly that.

Every question here is new prose — a question bank is the one place in these
two files where that is true, and the bar is §4's: each distractor is a WRONG
RULE in the correct answer's own shape, and each is a mistake a real student
in a real lab makes.
"""

UNIT = "C3"
LESSON = "filtration"
LESSON_NUMBER = 3

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "c3-03-e01",
        "band": "easier",
        "text": "A circle of filter paper is folded into a cone before it is "
                "put into the funnel. What is the fold for?",
        "options": [
            {"text": "It makes the gaps between the fibres smaller, so less "
                     "gets through", "correct": False,
             "why": "Folding paper does not change the paper. The gaps "
                    "between its fibres are exactly the same size folded or "
                    "flat — what changes is the shape, and the shape is what "
                    "has to fit the funnel."},
            {"text": "It shapes the paper to the funnel, so nothing can run "
                     "round the edge", "correct": True},
            {"text": "It stops the dissolved substances passing through with "
                     "the liquid", "correct": False,
             "why": "Nothing about the paper stops a dissolved substance, and "
                    "no way of folding one changes that. Dissolved particles "
                    "go wherever the liquid goes."},
            {"text": "It holds more mixture at once, so the filtering is "
                     "finished sooner", "correct": False,
             "why": "A cone does hold the mixture, but that is not why it is "
                    "folded — a flat disc laid in the funnel leaves gaps at "
                    "the edge, and the mixture runs round the paper instead "
                    "of through it."},
        ],
        "figure": None,
    },
    {
        "id": "c3-03-e02",
        "band": "easier",
        "text": "Muddy pond water is poured through a filter paper and comes "
                "out clear. What has been taken out of it?",
        "options": [
            {"text": "Everything that could make somebody ill, which is what "
                     "made it look murky", "correct": False,
             "why": "Murky and dangerous are not the same thing. The mud is "
                    "what you could see and it is the least dangerous thing "
                    "in there; the bacteria are far smaller than the mud and "
                    "most of them pass straight through the paper."},
            {"text": "Everything that was dissolved in it, which is why it is "
                     "now clear", "correct": False,
             "why": "Nothing dissolved is removed by a filter at all. It was "
                    "already clear-looking while dissolved — what made the "
                    "water murky was solid mud floating in it."},
            {"text": "Nothing at all — the water only looks different from "
                     "the outside", "correct": False,
             "why": "The mud really has gone, and it is in the paper. The "
                    "mistake is the other way round: something was removed, "
                    "just far less than the clear water suggests."},
            {"text": "The solid bits that were big enough to see — the "
                     "mud and the grit", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c3-03-e03",
        "band": "easier",
        "text": "Salt water is poured through a filter paper. When it has all "
                "dripped through, what is in the paper?",
        "options": [
            {"text": "Nothing — the salt is dissolved, so it went "
                     "through with the water", "correct": True},
            {"text": "A thin layer of salt, because the paper catches a "
                     "little of it on the way past", "correct": False,
             "why": "Nothing is caught. A dissolved salt particle is on its "
                    "own and far smaller than the gaps, so there is no reason "
                    "for the paper to hold back any of it at all."},
            {"text": "Salt, as long as the grade of paper is fine enough for "
                     "the job", "correct": False,
             "why": "There is no grade that does it. Dissolved particles are "
                    "thousands of times smaller than the fibres, so no filter "
                    "paper stops the salt and passes the water."},
            {"text": "Damp salt, because the water runs through the paper "
                     "faster than the salt does", "correct": False,
             "why": "They do not travel at different speeds through the "
                    "paper. A dissolved particle moves with the water it is "
                    "dissolved in, and arrives with it."},
        ],
        "figure": None,
    },
    {
        "id": "c3-03-e04",
        "band": "easier",
        "text": "Which of these mixtures could be separated with a funnel and "
                "a filter paper?",
        "options": [
            {"text": "Sugar stirred into a cup of tea until it disappears",
             "correct": False,
             "why": "The sugar dissolved, which is what disappearing means "
                    "here. Filtering the tea gives you the same sweet tea "
                    "back, with nothing in the paper."},
            {"text": "Salt stirred into warm water until the water goes clear",
             "correct": False,
             "why": "Dissolved again. Going clear is the sign that the salt "
                    "is now single particles spread through the water, and "
                    "those pass through any paper."},
            {"text": "Chalk powder stirred into water, which stays cloudy",
             "correct": True},
            {"text": "Ink dropped into water, which spreads until the whole "
                     "beaker is coloured", "correct": False,
             "why": "The colouring is dissolved and spreads through the "
                    "water, so a filter takes none of it out. Separating that "
                    "one needs chromatography, not a paper in a funnel."},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "c3-03-s01",
        "band": "standard",
        "text": "The funnel is stood in the flask with the tip of its stem "
                "touching the inside wall. Why is it set up that way?",
        "options": [
            {"text": "So the filtrate cannot splash back up into the paper, "
                     "and cannot run down the outside", "correct": True},
            {"text": "So the liquid is pulled through faster and the "
                     "filtering is over sooner", "correct": False,
             "why": "Speed is not what it is for, and speed is not wanted "
                    "here — pouring fast is what pushes fine particles "
                    "through a paper that would otherwise have caught them."},
            {"text": "So the funnel is held steady and the paper cannot lift "
                     "off the glass", "correct": False,
             "why": "Wetting the paper is what stops it lifting. The tip "
                    "against the wall is about where the drops go once they "
                    "are through, not about the paper."},
            {"text": "So the dissolved substances are left behind on the "
                     "glass as the liquid runs down", "correct": False,
             "why": "Nothing is left behind on the way down. Whatever is "
                    "dissolved is still dissolved in the filtrate when it "
                    "reaches the bottom of the flask."},
        ],
        "figure": None,
    },
    {
        "id": "c3-03-s02",
        "band": "standard",
        "text": "A student filters salt water, then pours the filtrate "
                "through a fresh, clean paper a second time. How do the two "
                "filtrates compare?",
        "options": [
            {"text": "The second is less salty, because each pass takes a "
                     "share of the salt out", "correct": False,
             "why": "Nothing was taken out on the first pass, so there is no "
                    "share to take. A pass that removes none of the salt "
                    "removes none of it however many times it is repeated."},
            {"text": "They are the same — the salt was never held back, "
                     "so a second pass changes nothing", "correct": True},
            {"text": "The second is saltier, because some of the water was "
                     "held back in the first paper", "correct": False,
             "why": "A little water does stay damp in the paper, but it takes "
                    "its dissolved salt with it, so what is left is no "
                    "saltier than it was — just slightly less of it."},
            {"text": "The second is clear, because two passes are enough to "
                     "remove the salt", "correct": False,
             "why": "Both are already clear: salt water is clear from the "
                    "start. Clear was never the sign that the salt had gone, "
                    "and neither pass removed any of it."},
        ],
        "figure": None,
    },
    {
        "id": "c3-03-s03",
        "band": "standard",
        "text": "A student stands the funnel in the flask and pours the sand "
                "and water in before putting any paper in the funnel. What is "
                "in the flask?",
        "options": [
            {"text": "Water only, because the funnel itself holds the sand "
                     "back", "correct": False,
             "why": "A funnel is a shape, not a filter. It has one wide hole "
                    "and it directs whatever is poured into it straight down "
                    "the stem."},
            {"text": "Sand and water both, and the whole thing has to be done "
                     "again", "correct": True},
            {"text": "Water, with a little sand — the narrow stem stops "
                     "most of the grains", "correct": False,
             "why": "The stem is far wider than a grain of sand. Nothing "
                    "about the glassware sorts the mixture; that is entirely "
                    "the paper's job, and there was no paper."},
            {"text": "Nothing, because the mixture stays in the funnel until "
                     "a paper is put in", "correct": False,
             "why": "There is nothing to hold it. The mixture goes straight "
                    "through an empty funnel, which is why the paper is "
                    "folded, seated and wetted before anything is poured."},
        ],
        "figure": None,
    },
    {
        "id": "c3-03-s04",
        "band": "standard",
        "text": "Two students filter the same muddy stream water. One says it "
                "is safe to drink now, because it is clear. What is wrong "
                "with that?",
        "options": [
            {"text": "Nothing is wrong with it, as long as the paper was not "
                     "torn anywhere", "correct": False,
             "why": "An intact paper still passes everything dissolved and "
                    "almost every bacterium. A perfect filtration and a torn "
                    "one both leave water that is not safe to drink."},
            {"text": "Clear only means the visible solids have gone; "
                     "bacteria and dissolved substances went through with the "
                     "water", "correct": True},
            {"text": "The water is safe, but it would taste better after a "
                     "second filtering", "correct": False,
             "why": "Taste is not the question, and a second filtering "
                    "changes neither the taste nor the safety — whatever "
                    "gives it a taste is dissolved, and passed through the "
                    "first time."},
            {"text": "It is not safe yet, because the mud is still in there "
                     "in smaller pieces", "correct": False,
             "why": "The mud really did stay in the paper. What is still "
                    "there is what was never visible in the first place, and "
                    "that is the dangerous half."},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "c3-03-h01",
        "band": "harder",
        "text": "Sea water really is desalinated industrially by forcing it "
                "through a reverse osmosis membrane. Why does that not show "
                "that a fine enough filter paper would work?",
        "options": [
            {"text": "Because a membrane is not a paper, and it only works "
                     "because the water is forced through under enormous "
                     "pressure", "correct": True},
            {"text": "Because the membrane is simply a much finer grade of "
                     "the same paper, and a school laboratory is never sold "
                     "that grade", "correct": False,
             "why": "It is a different kind of barrier, not a finer version "
                    "of the same one. Poured rather than forced, it separates "
                    "nothing — the pressure is not an extra, it is the whole "
                    "mechanism."},
            {"text": "Because the membrane removes the water and leaves the "
                     "salt in the tank, which paper cannot do", "correct": False,
             "why": "That much is true of both, and it is not the difference. "
                    "A filter paper poured with sea water leaves nothing in "
                    "the tank and nothing in the paper."},
            {"text": "Because sea water is far saltier than anything filtered "
                     "in a school laboratory", "correct": False,
             "why": "How much salt there is makes no difference. A very "
                    "weak salt solution passes through filter paper exactly "
                    "as completely as sea water does."},
        ],
        "figure": None,
    },
    {
        "id": "c3-03-h02",
        "band": "harder",
        "text": "Sand is filtered out of salt water, and the sand in the "
                "paper is wanted. It is rinsed with a little distilled water "
                "before being dried. Why?",
        "options": [
            {"text": "Because rinsing washes the last of the salt solution "
                     "off it, which would otherwise dry into it", "correct": True},
            {"text": "Because rinsing washes off the dirt the sand picked up "
                     "from the filter paper", "correct": False,
             "why": "The paper adds nothing to the sand. What is clinging to "
                    "the grains is the filtrate they were sitting in, and "
                    "that filtrate has salt dissolved in it."},
            {"text": "Because a rinse is good practice at the end of any "
                     "practical, whatever is being separated", "correct": False,
             "why": "It is not a tidiness rule. Rinsing matters when the "
                    "residue is what you want — if the filtrate is what "
                    "you are after, rinsing only dilutes it."},
            {"text": "Because the water pushes the last of the sand through "
                     "into the flask where it belongs", "correct": False,
             "why": "The sand is the residue and it is meant to stay. "
                    "Pushing anything through the paper is what squeezing "
                    "and poking do, and it is exactly what ruins the result."},
        ],
        "figure": None,
    },
    {
        "id": "c3-03-h03",
        "band": "harder",
        "text": "A dry filter paper is weighed, salt water is filtered "
                "through it, and the paper is dried and weighed again. It "
                "weighs the same as before. What does that show?",
        "options": [
            {"text": "That the balance is not sensitive enough to weigh the "
                     "very small amount of salt the paper managed to catch",
             "correct": False,
             "why": "There is nothing caught for it to weigh. Blaming the "
                    "balance keeps the belief alive; a more sensitive one "
                    "would read the same, because the paper really is "
                    "unchanged."},
            {"text": "That the paper was not fine enough, so the salt escaped "
                     "through it", "correct": False,
             "why": "Escaped through it is right; not fine enough is not. No "
                    "grade of paper would have held it, so this result is the "
                    "one every paper gives."},
            {"text": "That the salt passed straight through, because a "
                     "dissolved substance is not held back at all",
             "correct": True},
            {"text": "That the salt was destroyed by being dissolved, so "
                     "there was nothing left to catch", "correct": False,
             "why": "Dissolving destroys nothing. Boil the filtrate dry and "
                    "every gram of the salt is there — it went through the "
                    "paper, it did not disappear in it."},
        ],
        "figure": None,
    },
    {
        "id": "c3-03-h04",
        "band": "harder",
        "text": "A filter paper is a tangle of fibres rather than a sheet "
                "with holes in it. Which result does that explain?",
        "options": [
            {"text": "That the same paper filters less cleanly when the "
                     "mixture is poured through it quickly", "correct": True},
            {"text": "That a paper poured slowly enough will eventually hold "
                     "back a dissolved substance", "correct": False,
             "why": "Slower pouring gives a particle more chances to meet a "
                    "fibre, and a dissolved particle is far smaller than any "
                    "gap in the tangle. No pouring speed brings it near to "
                    "being caught."},
            {"text": "That the same paper lets more through the longer it is "
                     "used, as the tangle opens up", "correct": False,
             "why": "The opposite happens: as residue builds up in the "
                    "tangle the paper clogs and runs more slowly, and clogged "
                    "paper holds back more, not less."},
            {"text": "That two papers stacked together stop dissolved "
                     "substances one paper misses", "correct": False,
             "why": "Two tangles are two chances for a solid particle and no "
                    "chance at all for a dissolved one, which is far smaller "
                    "than every gap in both of them."},
        ],
        "figure": None,
    },
]
