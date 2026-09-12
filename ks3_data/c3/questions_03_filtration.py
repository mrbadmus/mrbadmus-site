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

    # ── easier · MRB-335 top-up ─────────────────────────────────────────
    {
        "id": "c3-03-e05",
        "band": "easier",
        "text": "Before the mixture is poured in, the folded cone is seated "
                "in the funnel and wetted. What is the wetting for?",
        "options": [
            {"text": "It makes the paper stick to the funnel, so nothing can "
                     "run down between the two",
             "correct": True},
            {"text": "It rinses any dust off the paper first, so that "
                     "nothing already on it can end up in the filtrate and "
                     "spoil the result",
             "correct": False,
             "why": "Filter paper is clean when you take it from the box. The "
                    "wetting is about the seal"},
            {"text": "It makes the holes in the paper swell up and close",
             "correct": False,
             "why": "Nothing about the paper changes size. A wet paper filters "
                    "the same as a dry one, once it is seated"},
            {"text": "It stops the paper tearing under the weight of the "
                     "liquid",
             "correct": False,
             "why": "A wet paper is weaker, not stronger. The reason is the "
                    "seal against the glass"},
        ],
        "figure": None,
    },
    {
        "id": "c3-03-e06",
        "band": "easier",
        "text": "Coffee is made by pouring hot water through ground beans in "
                "a paper. Which part of that is the residue?",
        "options": [
            {"text": "The coffee in the cup, since that is the part you "
                     "actually wanted to keep and the grounds are thrown away",
             "correct": False,
             "why": "Which one you want does not decide the name. The residue "
                    "is whatever the paper holds back"},
            {"text": "The ground beans left in the paper",
             "correct": True},
            {"text": "The hot water before it is poured",
             "correct": False,
             "why": "Neither word is used before the filtering. They name the "
                    "two things you end up with"},
            {"text": "The paper itself",
             "correct": False,
             "why": "The paper is the equipment. The residue is the solid "
                    "caught in it"},
        ],
        "figure": None,
    },
    {
        "id": "c3-03-e07",
        "band": "easier",
        "text": "In chemistry the word dissolved has a precise meaning. "
                "What is it?",
        "options": [
            {"text": "Broken into pieces small enough to pass through filter "
                     "paper",
             "correct": False,
             "why": "A dissolved substance is single particles, thousands of "
                    "times smaller than the fibres. Size alone is not the "
                    "definition either"},
            {"text": "Destroyed by the liquid it was put into",
             "correct": False,
             "why": "Nothing is destroyed. Boil the liquid off and it is all "
                    "still there"},
            {"text": "Broken up into single particles, spread evenly through "
                     "the liquid",
             "correct": True},
            {"text": "Melted by the liquid it was put into",
             "correct": False,
             "why": "Melting needs heat and one substance. Salt dissolves in "
                    "cold water and melts at 801 °C"},
        ],
        "figure": None,
    },

    # ── standard · MRB-335 top-up ───────────────────────────────────────
    {
        "id": "c3-03-s05",
        "band": "standard",
        "text": "A student pours a muddy mixture through the funnel as fast "
                "as it will go, and the filtrate comes out slightly cloudy. "
                "What should they do?",
        "options": [
            {"text": "Pour it through again, more slowly this time",
             "correct": True},
            {"text": "Use two papers on top of each other, since a single "
                     "sheet is clearly not thick enough to hold everything "
                     "back at that speed",
             "correct": False,
             "why": "Doubling the paper is not the fix. Pouring slowly lets "
                    "the same paper catch what it was pushing through"},
            {"text": "Accept it, because a filtrate is never completely "
                     "clear",
             "correct": False,
             "why": "A properly poured filtration gives a clear filtrate "
                    "every time"},
            {"text": "Warm the mixture first, so that it runs through more "
                     "easily",
             "correct": False,
             "why": "Running through MORE easily is the problem, not the "
                    "cure. Faster flow pushes particles through"},
        ],
        "figure": None,
    },
    {
        "id": "c3-03-s06",
        "band": "standard",
        "text": "Sand and water are filtered, and it is the SAND that is "
                "wanted. Which part do you keep, and where is it?",
        "options": [
            {"text": "The filtrate, in the flask underneath the funnel",
             "correct": False,
             "why": "The filtrate is the liquid that came through. The sand "
                    "never reached the flask"},
            {"text": "The residue, in the filter paper",
             "correct": True},
            {"text": "The residue, in the flask underneath the funnel",
             "correct": False,
             "why": "Right word, wrong place. The residue is what stays in "
                    "the paper"},
            {"text": "Both, because the sand ends up spread between the paper "
                     "and the flask and has to be collected from each of them",
             "correct": False,
             "why": "None of the sand passes through. It is insoluble and in "
                    "lumps far larger than the gaps"},
        ],
        "figure": None,
    },
    {
        "id": "c3-03-s07",
        "band": "standard",
        "text": "Muddy water is filtered until the filtrate is completely "
                "clear. The filtrate is then boiled dry and a white residue is "
                "left. What does that show?",
        "options": [
            {"text": "That the filter paper was faulty and let some mud "
                     "through",
             "correct": False,
             "why": "Mud is brown and visible, and the filtrate was clear. "
                    "What is left is something that was dissolved"},
            {"text": "That boiling has made a new substance out of the "
                     "water",
             "correct": False,
             "why": "Boiling is a change of state and makes nothing new. The "
                    "white solid was in the water all along"},
            {"text": "That something was dissolved in the water, and "
                     "filtering never removed it",
             "correct": True},
            {"text": "That the water was pure, since only pure water leaves a "
                     "clean white solid",
             "correct": False,
             "why": "Pure water boils dry and leaves nothing at all. A "
                    "residue is proof it was a mixture"},
        ],
        "figure": None,
    },

    # ── harder · MRB-335 top-up ─────────────────────────────────────────
    {
        "id": "c3-03-h05",
        "band": "harder",
        "text": "A filter paper's widest gap is quoted as 8 micrometres, yet "
                "it also stops some particles half that size. How?",
        "options": [
            {"text": "The paper is a tangle of fibres, so a particle can hit "
                     "one, stick to one, or be trapped in a bend below the "
                     "surface",
             "correct": True},
            {"text": "The quoted size is an average, so about half the gaps "
                     "are narrower than that",
             "correct": False,
             "why": "The quoted figure is the widest gap, not an average — "
                    "and a particle can be caught well away from any gap at "
                    "all"},
            {"text": "The first particles caught block the gaps, and after "
                     "that nothing gets through",
             "correct": False,
             "why": "Blocking does happen and it slows the flow. It does not "
                    "explain the very first small particles being caught"},
            {"text": "Small particles clump together in the liquid until they "
                     "are too big to pass",
             "correct": False,
             "why": "Some do clump, and the paper stops single small "
                    "particles too. The tangle is the reason"},
        ],
        "figure": None,
    },
    {
        "id": "c3-03-h06",
        "band": "harder",
        "text": "Rock salt is salt mixed with insoluble grit. Which order of "
                "steps gives you clean dry salt?",
        "options": [
            {"text": "Filter the rock salt as it is, then dissolve what is "
                     "caught in the paper",
             "correct": False,
             "why": "Filtering a dry solid separates nothing. The salt has to "
                    "be dissolved BEFORE the grit can be filtered off"},
            {"text": "Dissolve in water, then filter, then evaporate the "
                     "filtrate",
             "correct": True},
            {"text": "Evaporate first, then dissolve in water, then filter",
             "correct": False,
             "why": "There is nothing to evaporate at the start — the rock "
                    "salt is dry"},
            {"text": "Dissolve in water, then evaporate, then filter",
             "correct": False,
             "why": "Evaporating first leaves the salt and the grit together "
                    "in the dish, exactly as they started"},
        ],
        "figure": None,
    },
    {
        "id": "c3-03-h07",
        "band": "harder",
        "text": "Why can filtration never separate two liquids that mix "
                "completely, such as alcohol and water?",
        "options": [
            {"text": "Because a liquid cannot be a residue, and a filter can "
                     "only ever hold back a solid",
             "correct": False,
             "why": "Nearly the right shape, and it is not about being a "
                    "liquid: a filter sorts by size, and neither is in "
                    "lumps"},
            {"text": "Because the two liquids would react with each other in "
                     "the paper and make a third substance that runs through "
                     "with them",
             "correct": False,
             "why": "Nothing reacts. Both simply pass through, unchanged"},
            {"text": "Because both are single particles far smaller than any "
                     "gap, so neither is held back",
             "correct": True},
            {"text": "Because the paper would dissolve in the alcohol",
             "correct": False,
             "why": "Filter paper stands up to alcohol perfectly well. The "
                    "problem is that neither liquid can be caught"},
        ],
        "figure": None,
    },
    # ── easier · MRB-338 expansion ──────────────────────────────────────
    {
        "id": "c3-03-e08",
        "band": "easier",
        "text": "Filtration separates one particular kind of mixture. "
                "Which one?",
        "options": [
            {"text": "A dissolved solid from the liquid it is dissolved in",
             "correct": False,
             "why": "Nothing dissolved is held back by paper. A dissolved "
                    "solid goes wherever the liquid goes."},
            {"text": "An insoluble solid from a liquid", "correct": True},
            {"text": "Two liquids that have mixed completely together",
             "correct": False,
             "why": "Both liquids pour through the paper together. A filter "
                    "can only hold back something that is in lumps."},
            {"text": "Two dry solids of different colours", "correct": False,
             "why": "A filter needs a liquid to carry the mixture through. "
                    "Two dry powders simply sit in the paper together."},
        ],
        "figure": None,
    },
    {
        "id": "c3-03-e09",
        "band": "easier",
        "text": "Filtering a mixture always gives two things to collect. "
                "What are the two called?",
        "options": [
            {"text": "A residue and a filtrate", "correct": True},
            {"text": "A solute and a solvent", "correct": False,
             "why": "Those are the words for dissolving. Filtering separates "
                    "something that never dissolved in the first place."},
            {"text": "A solution and a suspension", "correct": False,
             "why": "A suspension is the cloudy mixture you start with, not "
                    "something that filtering produces."},
            {"text": "A crystal and a distillate", "correct": False,
             "why": "Those two are collected by boiling a liquid off or by "
                    "boiling and cooling it, which are other techniques."},
        ],
        "figure": None,
    },
    {
        "id": "c3-03-e10",
        "band": "easier",
        "text": "Which piece of apparatus is the folded filter paper put "
                "into?",
        "options": [
            {"text": "A measuring cylinder", "correct": False,
             "why": "A measuring cylinder is for measuring volume, and it has "
                    "no opening at the bottom for a filtrate to leave by."},
            {"text": "An evaporating basin", "correct": False,
             "why": "An evaporating basin is a shallow dish for driving a "
                    "liquid off, and it has no outlet at all."},
            {"text": "A funnel", "correct": True},
            {"text": "A conical flask", "correct": False,
             "why": "The flask stands underneath and catches the filtrate. "
                    "Paper put inside it would never meet the mixture."},
        ],
        "figure": None,
    },
    {
        "id": "c3-03-e11",
        "band": "easier",
        "text": "What is stood underneath the funnel during a filtration, and why?",
        "options": [
            {
             "text": "An evaporating basin, so the filtrate boils away",
             "correct": False,
             "why": "Nothing is heated during filtering, and the filtrate is usually the part you want to keep.",
            },
            {
             "text": "A second funnel, so it is filtered twice",
             "correct": False,
             "why": "A second pass adds nothing. The first paper has already held back everything it is able to hold back.",
            },
            {
             "text": "A Bunsen burner, so the liquid is driven through",
             "correct": False,
             "why": "Filtering is driven by gravity, not by heat, and a flame under a funnel of mixture is unsafe.",
            },
            {
             "text": "A conical flask, so the filtrate is caught",
             "correct": True,
            },
        ],
        "figure": None,
    },
    {
        "id": "c3-03-e12",
        "band": "easier",
        "text": "Sand stirred into water makes a cloudy mixture in which the "
                "solid slowly settles out. What is a mixture like that "
                "called?",
        "options": [
            {"text": "A suspension", "correct": True},
            {"text": "A solution", "correct": False,
             "why": "A solution is clear and never settles, because the solid "
                    "has broken up into single particles."},
            {"text": "A solvent", "correct": False,
             "why": "A solvent is the liquid that does the dissolving, not "
                    "the name for a whole mixture."},
            {"text": "A filtrate", "correct": False,
             "why": "A filtrate is the liquid collected after filtering, not "
                    "the cloudy mixture that is poured in."},
        ],
        "figure": None,
    },
    {
        "id": "c3-03-e13",
        "band": "easier",
        "text": "Which is larger: one grain of sand, or one particle of dissolved salt?",
        "options": [
            {
             "text": "The grain of sand, by thousands of times",
             "correct": True,
            },
            {
             "text": "The dissolved salt particle, because it swells up",
             "correct": False,
             "why": "Dissolving breaks a solid up into single particles. It never makes anything bigger than it was.",
            },
            {
             "text": "They are about the same size, so a filter catches both",
             "correct": False,
             "why": "A grain of sand is millions of particles stuck together; a dissolved particle is one particle on its own.",
            },
            {
             "text": "It depends how long the salt has been stirred",
             "correct": False,
             "why": "Stirring makes dissolving happen faster. The size of a single dissolved particle is always the same.",
            },
        ],
        "figure": None,
    },
    {
        "id": "c3-03-e14",
        "band": "easier",
        "text": "Does ordinary filter paper take the bacteria out of water?",
        "options": [
            {
             "text": "Yes, because bacteria are solid, so the paper holds every one of them back",
             "correct": False,
             "why": "Being solid is not enough to be caught. Most bacteria are far smaller than the mud a paper holds back.",
            },
            {
             "text": "Yes, as long as the water is poured through very slowly",
             "correct": False,
             "why": "Pouring slowly does give a cleaner filtrate, but it does not turn paper into a barrier to something that small.",
            },
            {
             "text": "No, because most bacteria pass straight through it",
             "correct": True,
            },
            {
             "text": "No, because bacteria dissolve in water and dissolved things pass through",
             "correct": False,
             "why": "Bacteria do not dissolve. They are solid specks carried along by the water, and they pass because they are small, not because they are dissolved.",
            },
        ],
        "figure": None,
    },
    {
        "id": "c3-03-e15",
        "band": "easier",
        "text": "Loose tea is brewed in a pot, sugar is stirred in, and the drink is poured out through a tea strainer. What does the strainer catch?",
        "options": [
            {
             "text": "The tea leaves and the sugar",
             "correct": False,
             "why": "The sugar dissolved, so it is spread through the drink as single particles and pours straight through.",
            },
            {
             "text": "The tea leaves only",
             "correct": True,
            },
            {
             "text": "The sugar only",
             "correct": False,
             "why": "The order things are added in makes no difference. Dissolved sugar passes any strainer, every time.",
            },
            {
             "text": "Neither of them",
             "correct": False,
             "why": "A strainer's holes are narrower than a tea leaf, which is exactly why the leaves are left behind in it.",
            },
        ],
        "figure": None,
    },
    {
        "id": "c3-03-e16",
        "band": "easier",
        "text": "Cooked pasta is tipped into a colander and the water runs away through the holes. Which part is the residue?",
        "options": [
            {
             "text": "The water that ran through the holes",
             "correct": False,
             "why": "The part that passes through is the filtrate. The residue is the solid that is held back.",
            },
            {
             "text": "Both the pasta and the water",
             "correct": False,
             "why": "Being wet does not make the water part of the residue. The residue is only the solid that could not pass.",
            },
            {
             "text": "Neither, a colander is not a filter paper",
             "correct": False,
             "why": "Changing the apparatus does not change the words. Whatever is held back on the way through is the residue.",
            },
            {
             "text": "The pasta, left in the colander",
             "correct": True,
            },
        ],
        "figure": None,
    },
    {
        "id": "c3-03-e17",
        "band": "easier",
        "text": "A vacuum cleaner pulls air through a filter. Which two "
                "things is that filter separating?",
        "options": [
            {"text": "Solid dust from air", "correct": True},
            {"text": "Dissolved dust from air", "correct": False,
             "why": "Dust is not dissolved in air. It is solid specks being "
                    "carried along by the moving air."},
            {"text": "Solid dust from water", "correct": False,
             "why": "There is no liquid inside a vacuum cleaner. Air is the "
                    "only thing flowing through the filter."},
            {"text": "One gas from another gas", "correct": False,
             "why": "A filter holds back pieces of solid. Gases flow through "
                    "it together and come out unchanged."},
        ],
        "figure": None,
    },
    {
        "id": "c3-03-e18",
        "band": "easier",
        "text": "Which mixture would not be separated at all by pouring it through a filter paper?",
        "options": [
            {
             "text": "Chalk powder stirred into water",
             "correct": False,
             "why": "Chalk is insoluble, so it stays in lumps and the paper holds it back as a residue.",
            },
            {
             "text": "Sand stirred into water",
             "correct": False,
             "why": "Sand grains are far wider than the gaps in the paper, so they are all left behind in it.",
            },
            {
             "text": "Sugar dissolved in water",
             "correct": True,
            },
            {
             "text": "Sawdust floating in water",
             "correct": False,
             "why": "Sawdust is insoluble, so the paper catches it whether it floats on the water or sinks through it.",
            },
        ],
        "figure": None,
    },
    {
        "id": "c3-03-e19",
        "band": "easier",
        "text": "A student sets out to filter chalk powder out of water. "
                "Which piece of apparatus has no part to play?",
        "options": [
            {"text": "A filter funnel, to hold the folded paper",
             "correct": False,
             "why": "The funnel holds the paper in shape and guides the "
                    "filtrate down into the flask below."},
            {"text": "A Bunsen burner, because nothing is heated",
             "correct": True},
            {"text": "A filter paper, to hold the chalk back",
             "correct": False,
             "why": "The paper is the thing that does the separating. Without "
                    "it there is nothing to catch the chalk."},
            {"text": "A beaker, to collect what comes through",
             "correct": False,
             "why": "Something has to stand under the funnel, or the filtrate "
                    "simply runs out onto the bench."},
        ],
        "figure": None,
    },
    {
        "id": "c3-03-e20",
        "band": "easier",
        "text": "In an ordinary school filtration, what makes the liquid move down through the paper?",
        "options": [
            {
             "text": "The paper soaking it up and squeezing it out",
             "correct": False,
             "why": "Paper does soak liquid up, but nothing squeezes it out again. It keeps falling because it is pulled down.",
            },
            {
             "text": "Warmth from the room driving it through",
             "correct": False,
             "why": "A filtration works just as well in a cold room, because nothing is being heated or evaporated.",
            },
            {
             "text": "The funnel sucking it down its stem",
             "correct": False,
             "why": "A plain glass funnel sucks at nothing. It only guides what has already been pulled through the paper.",
            },
            {
             "text": "Gravity, pulling it downwards",
             "correct": True,
            },
        ],
        "figure": None,
    },
    {
        "id": "c3-03-e21",
        "band": "easier",
        "text": "How full should the filter paper be as the mixture is "
                "poured in?",
        "options": [
            {"text": "About two thirds full, with the level below the rim of "
                     "the paper", "correct": True},
            {"text": "Right up to the top of the paper, to get it finished "
                     "sooner", "correct": False,
             "why": "Anything that goes over the rim has not been through the "
                    "paper at all, so the filtrate is spoilt."},
            {"text": "Right up to the top of the funnel, above the paper",
             "correct": False,
             "why": "The mixture would run down between the paper and the "
                    "glass and reach the flask unfiltered."},
            {"text": "A few drops at a time, so that the paper never tears",
             "correct": False,
             "why": "Paper does not tear under a normal load, and filling it "
                    "that slowly would take a whole lesson."},
        ],
        "figure": None,
    },
    {
        "id": "c3-03-e22",
        "band": "easier",
        "text": "Why should the filter paper never be poked or squeezed to "
                "hurry the filtering along?",
        "options": [
            {"text": "It packs the fibres together, so nothing passes at all",
             "correct": False,
             "why": "Pressing does not close the gaps in a paper up. It "
                    "damages the paper instead."},
            {"text": "It makes the residue dissolve into the liquid below",
             "correct": False,
             "why": "An insoluble solid does not dissolve because it is "
                    "pressed. It is insoluble however it is treated."},
            {"text": "It tears, and the residue goes through into the "
                     "filtrate", "correct": True},
            {"text": "It warms the mixture up, which spoils the separation",
             "correct": False,
             "why": "A finger cannot warm a mixture enough to change "
                    "anything, and warmth would not spoil a filtration."},
        ],
        "figure": None,
    },
    {
        "id": "c3-03-e23",
        "band": "easier",
        "text": "The mixture is poured into the funnel down a stirring rod. "
                "What is the rod there for?",
        "options": [
            {"text": "To keep stirring the mixture so the solid stays moving",
             "correct": False,
             "why": "The rod is held still while the pouring is done. Its job "
                    "is where the mixture lands, not keeping it mixed."},
            {"text": "To break the solid into smaller pieces on the way in",
             "correct": False,
             "why": "Smaller pieces would be harder to catch, not easier, and "
                    "nothing is being crushed as it is poured."},
            {"text": "To push the liquid through the paper more quickly",
             "correct": False,
             "why": "The rod never reaches the pool of liquid in the paper. "
                    "Gravity does the moving on its own."},
            {"text": "To guide the mixture in without splashing over the rim",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c3-03-e24",
        "band": "easier",
        "text": "At a water treatment works the water is passed through beds "
                "of sand. What does that step do?",
        "options": [
            {"text": "It kills the bacteria that are in the water",
             "correct": False,
             "why": "Killing microbes is a later step, done with chlorine or "
                    "with ultraviolet light rather than with sand."},
            {"text": "It takes out small pieces of solid that the water is "
                     "carrying", "correct": True},
            {"text": "It takes out the substances dissolved in the water",
             "correct": False,
             "why": "Dissolved substances pass through a bed of sand exactly "
                    "as they pass through a filter paper."},
            {"text": "It puts minerals in the water to improve the taste",
             "correct": False,
             "why": "A sand bed only takes things out. Nothing at all is "
                    "added to the water as it passes through."},
        ],
        "figure": None,
    },
    {
        "id": "c3-03-e25",
        "band": "easier",
        "text": "What is a filter paper actually made of?",
        "options": [
            {
             "text": "A tangle of cellulose fibres",
             "correct": True,
            },
            {
             "text": "A thin sheet with holes punched in it",
             "correct": False,
             "why": "There are no punched holes in it. The gaps are the spaces left between fibres lying across each other.",
            },
            {
             "text": "A fine metal mesh with a coating",
             "correct": False,
             "why": "Filter paper is paper. A metal mesh is a different piece of apparatus, with much wider gaps in it.",
            },
            {
             "text": "A layer of tightly packed sand",
             "correct": False,
             "why": "Beds of sand are used at a treatment works, but a filter paper holds nothing like sand in it.",
            },
        ],
        "figure": None,
    },
    {
        "id": "c3-03-e26",
        "band": "easier",
        "text": "A filter paper has a small tear in it, and a sand and water mixture is poured in anyway. What ends up in the flask?",
        "options": [
            {
             "text": "Liquid with some of the sand in it",
             "correct": True,
            },
            {
             "text": "Liquid only, with none of the sand",
             "correct": False,
             "why": "A tear is a gap far wider than a grain of sand, which is why solid gets through one so easily.",
            },
            {
             "text": "Nothing — it all runs out onto the bench",
             "correct": False,
             "why": "The tear is in the paper inside the funnel, so whatever goes through it still lands in the flask.",
            },
            {
             "text": "Sand only, with none of the liquid",
             "correct": False,
             "why": "A tear cannot hold a liquid back. Liquid passes an undamaged paper, let alone a torn one.",
            },
        ],
        "figure": None,
    },
    {
        "id": "c3-03-e27",
        "band": "easier",
        "text": "A dry filter paper has a mass of 1.1 g. After filtering, "
                "the paper and the dried residue together have a mass of "
                "4.6 g. What is the mass of the residue?",
        "options": [
            {"text": "5.7 g", "correct": False,
             "why": "That is the two masses added together. The residue is "
                    "the difference between them, not the total."},
            {"text": "4.6 g", "correct": False,
             "why": "That is the paper and the residue weighed together. The "
                    "paper's own mass still has to come off."},
            {"text": "3.5 g", "correct": True},
            {"text": "1.1 g", "correct": False,
             "why": "That is the mass of the paper on its own, measured "
                    "before anything had been filtered through it."},
        ],
        "figure": None,
    },
    {
        "id": "c3-03-e28",
        "band": "easier",
        "text": "200 cm³ of muddy water is filtered and 185 cm³ of filtrate "
                "is collected. Where is the other 15 cm³?",
        "options": [
            {"text": "It evaporated as the mixture ran through the funnel",
             "correct": False,
             "why": "Nothing is heated during filtering, and 15 cm³ could not "
                    "evaporate from a cold funnel in a few minutes."},
            {"text": "It went through the paper as a gas and escaped",
             "correct": False,
             "why": "Water does not turn into a gas by passing through paper. "
                    "It is still liquid the whole way down."},
            {"text": "It was destroyed, because filtering always loses some "
                     "water", "correct": False,
             "why": "Nothing is destroyed by filtering. Every drop is still "
                    "there, and some of it is still in the funnel."},
            {"text": "It is soaked into the paper and the wet residue",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c3-03-e29",
        "band": "easier",
        "text": "A student filters sand out of water and wants to find the "
                "mass of the sand. Why must the sand be dried first?",
        "options": [
            {"text": "Because water left in it would be weighed as though it "
                     "were sand", "correct": True},
            {"text": "Because damp sand slowly dissolves, so some would be "
                     "lost", "correct": False,
             "why": "Sand does not dissolve at all, wet or dry. That is "
                    "exactly why it could be filtered out."},
            {"text": "Because a balance cannot give a reading for anything "
                     "damp", "correct": False,
             "why": "A balance weighs whatever is put on it. The difficulty "
                    "is what that reading includes, not the reading itself."},
            {"text": "Because drying turns the sand back into the substance "
                     "it was", "correct": False,
             "why": "The sand was never changed into anything. Filtering and "
                    "drying leave it exactly as it went in."},
        ],
        "figure": None,
    },
    {
        "id": "c3-03-e30",
        "band": "easier",
        "text": "Sand has settled on the bottom of a beaker of water, and "
                "the water is carefully poured off without disturbing it. "
                "What is that called?",
        "options": [
            {"text": "Filtering", "correct": False,
             "why": "Filtering means pouring a mixture through a paper, and "
                    "nothing is being poured through anything here."},
            {"text": "Decanting", "correct": True},
            {"text": "Evaporating", "correct": False,
             "why": "Evaporating drives a liquid off as a gas. Here the "
                    "liquid is simply poured away as a liquid."},
            {"text": "Dissolving", "correct": False,
             "why": "Dissolving is a solid breaking up into a liquid. This "
                    "sand has done the opposite and settled out."},
        ],
        "figure": None,
    },
    {
        "id": "c3-03-e31",
        "band": "easier",
        "text": "A gardener shakes soil through a wire sieve and the stones stay behind. What does that have in common with filtering?",
        "options": [
            {
             "text": "Both of them separate a dissolved substance from its liquid",
             "correct": False,
             "why": "Neither of them can do that. Anything dissolved goes wherever the liquid it is dissolved in goes.",
            },
            {
             "text": "Both of them need a liquid to carry the mixture through",
             "correct": False,
             "why": "A sieve works on dry soil, and a filter paper is poured through as a liquid mixture — but neither of them needs one to hold a lump back.",
            },
            {
             "text": "Both of them hold back the pieces that are too big to pass",
             "correct": True,
            },
            {
             "text": "Both of them work faster the finer the gaps are made",
             "correct": False,
             "why": "Finer gaps hold more back, but everything then passes through more slowly rather than more quickly.",
            },
        ],
        "figure": None,
    },
    {
        "id": "c3-03-e32",
        "band": "easier",
        "text": "A student has finished filtering one mixture and wants to "
                "filter a different one. What should they do about the "
                "filter paper?",
        "options": [
            {"text": "Tip the residue out and use the same paper again",
             "correct": False,
             "why": "Residue is pressed down into the fibres and cannot all "
                    "be tipped out, so some would join the next filtrate."},
            {"text": "Turn it inside out and use the other side of it",
             "correct": False,
             "why": "Both sides are the same tangle of fibres, and the "
                    "residue is caught inside the paper, not on one face."},
            {"text": "Rinse it under the tap and use it again", "correct": False,
             "why": "Tap water carries dissolved solids of its own, and "
                    "rinsing drives the old residue deeper into the fibres."},
            {"text": "Fold a fresh paper and start again", "correct": True},
        ],
        "figure": None,
    },
    # ── standard · MRB-338 expansion ────────────────────────────────────
    {
        "id": "c3-03-s08",
        "band": "standard",
        "text": "A student is filtering a solution and wants none of the dissolved substance left behind with the residue. What should they do?",
        "options": [
            {
             "text": "Squeeze the paper out over the flask to force the last of it through",
             "correct": False,
             "why": "Squeezing tears the paper, and the residue then drops into the filtrate along with the liquid.",
            },
            {
             "text": "Wash the residue with a little distilled water and keep the washings",
             "correct": True,
            },
            {
             "text": "Pour the filtrate back through the same paper to pick up what is left",
             "correct": False,
             "why": "The filtrate already holds the dissolved substance, so pouring it back over the residue leaves just as much clinging to it as before.",
            },
            {
             "text": "Tip the residue into the flask so that nothing is left behind in the paper",
             "correct": False,
             "why": "That puts the solid straight into the filtrate, which undoes the whole filtration.",
            },
        ],
        "figure": None,
    },
    {
        "id": "c3-03-s09",
        "band": "standard",
        "text": "A student fills the filter paper right to the top, and some "
                "of the mixture runs over the rim of the paper. What does "
                "that do to the result?",
        "options": [
            {"text": "Nothing, because the mixture still has to pass down the "
                     "funnel's stem", "correct": False,
             "why": "The stem is a wide open tube that holds nothing back. "
                    "Whatever goes over the rim runs straight down it."},
            {"text": "Nothing, as long as the paper was wetted before the "
                     "pouring started", "correct": False,
             "why": "Wetting makes the paper cling to the glass. It does not "
                    "raise the rim or stop an overflow going past it."},
            {"text": "Some of the mixture reaches the flask without being "
                     "filtered at all", "correct": True},
            {"text": "It slows the filtering down, but the filtrate itself is "
                     "unaffected", "correct": False,
             "why": "Mixture going over the rim arrives faster, not slower, "
                    "and it brings solid into the flask with it."},
        ],
        "figure": None,
    },
    {
        "id": "c3-03-s10",
        "band": "standard",
        "text": "The residue is rinsed at the end with distilled water rather "
                "than with tap water. Why does it matter which is used?",
        "options": [
            {"text": "Tap water has dissolved solids in it, which would dry "
                     "onto the residue", "correct": True},
            {"text": "Tap water is colder, so it would wash the residue down "
                     "through the paper", "correct": False,
             "why": "Temperature makes no difference to an insoluble residue, "
                    "and neither rinse washes it through the paper."},
            {"text": "Tap water would dissolve part of the residue and lose "
                     "it", "correct": False,
             "why": "The residue is insoluble, which is why it was caught in "
                    "the first place. Neither kind of water dissolves it."},
            {"text": "Tap water flows more quickly and would tear the wet "
                     "paper", "correct": False,
             "why": "Both are poured in gently from a wash bottle, and "
                    "neither has the force to damage a paper."},
        ],
        "figure": None,
    },
    {
        "id": "c3-03-s11",
        "band": "standard",
        "text": "A folded filter cone has three thicknesses of paper on one "
                "side and a single thickness on the other. Why is the "
                "mixture poured in against the three-thickness side?",
        "options": [
            {"text": "Because three layers hold back the dissolved "
                     "substances that one layer misses", "correct": False,
             "why": "No number of layers holds anything dissolved back. "
                    "Thickness changes the support, not what passes."},
            {"text": "Because the liquid filters faster through three layers "
                     "than through one", "correct": False,
             "why": "More layers slow a liquid down rather than speeding it "
                    "up, so speed is not the reason for pouring there."},
            {"text": "Because the single layer is where the residue is meant "
                     "to collect", "correct": False,
             "why": "Residue collects all over the inside of the cone, "
                    "wherever the solid settles out of the mixture."},
            {"text": "Because three layers support the paper where the stream "
                     "lands", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c3-03-s12",
        "band": "standard",
        "text": "A student pushes the funnel into the flask through a tight "
                "rubber bung so that nothing can spill. The filtering slows "
                "and then stops. Why?",
        "options": [
            {"text": "The air in the flask cannot get out, so the filtrate "
                     "cannot come down", "correct": True},
            {"text": "The bung squeezes the funnel, which closes up the gaps "
                     "in the paper", "correct": False,
             "why": "The bung grips the outside of the glass stem, and it "
                    "cannot reach the paper or change it at all."},
            {"text": "The filtrate is pushed back up through the paper by the "
                     "bung", "correct": False,
             "why": "Nothing pushes the filtrate upwards. It simply stops "
                    "arriving, rather than going back the way it came."},
            {"text": "The residue has blocked the paper because of the "
                     "tighter fit", "correct": False,
             "why": "How the funnel is held in place has nothing to do with "
                    "whether the paper clogs up."},
        ],
        "figure": None,
    },
    {
        "id": "c3-03-s13",
        "band": "standard",
        "text": "Sea water is filtered. The filtrate conducts electricity, "
                "while distilled water does not. What does that show?",
        "options": [
            {"text": "That the filter paper released something into the water "
                     "as it went through", "correct": False,
             "why": "Filter paper is cellulose fibre, and it dissolves "
                    "nothing at all into the filtrate."},
            {"text": "That filtering gives water an electrical charge as it "
                     "passes through", "correct": False,
             "why": "Filtering changes nothing about the water itself. It "
                    "only removes what was in lumps."},
            {"text": "That some of the salt was held back in the paper",
             "correct": False,
             "why": "Salt held back would make the filtrate conduct less, and "
                    "in any case none of it was caught."},
            {"text": "That the dissolved salt passed straight through the "
                     "paper", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c3-03-s14",
        "band": "standard",
        "text": "18.0 g of rock salt is stirred into water and the mixture "
                "is filtered. The residue is dried and has a mass of 2.4 g. "
                "What mass of the rock salt dissolved?",
        "options": [
            {"text": "15.6 g", "correct": True},
            {"text": "2.4 g", "correct": False,
             "why": "That is the insoluble part, caught in the paper. The "
                    "dissolved part is what is missing from the 18.0 g."},
            {"text": "20.4 g", "correct": False,
             "why": "The two masses have been added. Nothing can dissolve "
                    "that was not in the 18.0 g to start with."},
            {"text": "9.0 g", "correct": False,
             "why": "The sample has been halved, but nothing says the "
                    "soluble and insoluble parts were equal."},
        ],
        "figure": None,
    },
    {
        "id": "c3-03-s15",
        "band": "standard",
        "text": "A student weighs out 50.0 g of rock salt, dissolves it, "
                "filters the mixture and dries what the paper holds, which "
                "comes to 4.0 g. What percentage of the original sample "
                "could not dissolve?",
        "options": [
            {"text": "4.0%", "correct": False,
             "why": "That is the mass of the residue in grams, written down "
                    "as though it were already a percentage."},
            {"text": "8.0%", "correct": True},
            {"text": "12.5%", "correct": False,
             "why": "That is 50.0 divided by 4.0. The residue belongs on top "
                    "of the fraction, not underneath it."},
            {"text": "92.0%", "correct": False,
             "why": "That is the percentage that dissolved. The question asks "
                    "for the part the paper kept."},
        ],
        "figure": None,
    },
    {
        "id": "c3-03-s16",
        "band": "standard",
        "text": "A student weighs the residue before it has finished drying. "
                "What effect does that have on the mass recorded?",
        "options": [
            {"text": "It is too low, because wet residue sticks to the paper "
                     "and is left behind", "correct": False,
             "why": "The residue is weighed in the paper, so anything stuck "
                    "to it is still on the balance."},
            {"text": "It is unchanged, because water has almost no mass",
             "correct": False,
             "why": "Water has plenty of mass: 1 cm³ of it weighs about 1 g, "
                    "which is more than many residues weigh in total."},
            {"text": "It is too high, because the water in it is weighed too",
             "correct": True},
            {"text": "It is too low, because some residue dissolves in the "
                     "water left in it", "correct": False,
             "why": "The residue is insoluble, so the water still in it "
                    "dissolves none of it at all."},
        ],
        "figure": None,
    },
    {
        "id": "c3-03-s17",
        "band": "standard",
        "text": "Some of the chalk stays stuck to the inside of the beaker "
                "and never reaches the funnel. What does that do to the mass "
                "of residue the student records?",
        "options": [
            {"text": "Makes it too high, because the beaker is weighed with "
                     "the rest", "correct": False,
             "why": "The beaker never goes on the balance. Only the paper and "
                    "what it holds are weighed."},
            {"text": "Makes no difference, as long as all the liquid was "
                     "poured out", "correct": False,
             "why": "It is the solid that is being weighed, so solid left in "
                    "the beaker is mass missing from the result."},
            {"text": "Makes no difference, because the chalk left behind "
                     "dissolves later", "correct": False,
             "why": "Chalk is insoluble and never dissolves. It simply stays "
                    "where it is on the glass."},
            {"text": "Makes it too low, because part of the solid was never "
                     "collected", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c3-03-s18",
        "band": "standard",
        "text": "Sand has settled on the bottom of a beaker of water. "
                "Compare pouring the water off with filtering the whole "
                "mixture.",
        "options": [
            {"text": "Pouring off is quicker, but filtering takes out the "
                     "last of the sand as well", "correct": True},
            {"text": "Pouring off is quicker and takes out more sand, since "
                     "none is lost in a paper", "correct": False,
             "why": "Some sand is always stirred up and poured off with the "
                    "water, and a paper loses none of it."},
            {"text": "Filtering is quicker, since the whole mixture goes at "
                     "once instead of being poured slowly", "correct": False,
             "why": "Filtering is the slower of the two, because the liquid "
                    "has to pass through paper a drop at a time."},
            {"text": "They give the same result, since the sand is insoluble "
                     "either way", "correct": False,
             "why": "Insolubility is why both work at all, but pouring off "
                    "always leaves a little sand in the liquid."},
        ],
        "figure": None,
    },
    {
        "id": "c3-03-s19",
        "band": "standard",
        "text": "Sand has been filtered out of salt water, and the salt is "
                "now wanted. What should be done with the filtrate?",
        "options": [
            {"text": "Filter it again through a finer grade of paper",
             "correct": False,
             "why": "No paper holds a dissolved substance back, so a second "
                    "filtering collects nothing whatever the grade."},
            {"text": "Add more water, so the salt separates out of the "
                     "solution", "correct": False,
             "why": "Adding water only dilutes it. The salt stays dissolved, "
                    "and there is now more liquid to deal with."},
            {"text": "Heat it, so the water evaporates and the salt is left",
             "correct": True},
            {"text": "Pour it through a bed of clean sand, which holds the "
                     "salt back", "correct": False,
             "why": "A bed of sand has far wider gaps than paper, so a "
                    "dissolved substance passes it even more easily."},
        ],
        "figure": None,
    },
    {
        "id": "c3-03-s20",
        "band": "standard",
        "text": "At a treatment works the water is settled, then filtered "
                "through sand, then treated with chlorine. Which of those "
                "steps deals with the microbes?",
        "options": [
            {"text": "The settling, because microbes are heavy and sink "
                     "first", "correct": False,
             "why": "Microbes are far too small to settle out of water. They "
                    "stay spread through it however long it stands."},
            {"text": "The filtering, because a sand bed is fine enough to "
                     "hold them all", "correct": False,
             "why": "Most microbes are small enough to pass through a bed of "
                    "sand along with the water."},
            {"text": "All three equally, because each removes a share of "
                     "them", "correct": False,
             "why": "The first two steps work on solid you can see. Only the "
                    "chlorine deals with what is left after that."},
            {"text": "The chlorine, because the first two steps leave most of "
                     "them", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c3-03-s21",
        "band": "standard",
        "text": "Tap water in a hard-water area leaves a white scale in the "
                "kettle. A student filters the tap water through paper "
                "first. Will the kettle still scale up?",
        "options": [
            {"text": "No, because the paper catches the scale before it "
                     "reaches the kettle", "correct": False,
             "why": "The scale forms in the kettle out of something "
                    "dissolved; there is no solid in the cold water to "
                    "catch."},
            {"text": "Yes, because the substances that make the scale are "
                     "dissolved", "correct": True},
            {"text": "No, because filtering removes everything that is not "
                     "water", "correct": False,
             "why": "Filtering removes what is in lumps. Everything dissolved "
                    "passes through the paper untouched."},
            {"text": "Yes, but only if the paper was torn as the water went "
                     "through", "correct": False,
             "why": "Dissolved substances pass an undamaged paper exactly as "
                    "easily as they pass a torn one."},
        ],
        "figure": None,
    },
    {
        "id": "c3-03-s22",
        "band": "standard",
        "text": "A student separates 21.0 g of a dry sand and salt mixture. They dry the sand from the filter paper and get 6.0 g, and they boil the filtrate dry and get 14.0 g of salt. Why do the two masses not add up to 21.0 g?",
        "options": [
            {
             "text": "Some of the salt was destroyed by the heat when the filtrate was boiled dry",
             "correct": False,
             "why": "Boiling drives the water off as a gas and leaves the salt behind in the dish. Heating a solution dry destroys none of it.",
            },
            {
             "text": "Small amounts of both were left behind in the beaker and on the paper",
             "correct": True,
            },
            {
             "text": "Some of the sand dissolved and was lost with the water",
             "correct": False,
             "why": "Sand is insoluble, which is why the paper could catch it. Anything that had dissolved would have been left in the dish when the filtrate was boiled dry.",
            },
            {
             "text": "The missing mass is the water that was stirred in at the start",
             "correct": False,
             "why": "The 21.0 g was weighed out dry, before any water was added, and all of that water has since been driven off.",
            },
        ],
        "figure": None,
    },
    {
        "id": "c3-03-s23",
        "band": "standard",
        "text": "A muddy sample contains very fine clay particles. After "
                "filtering it through an undamaged paper the filtrate is "
                "still faintly cloudy. What does that show?",
        "options": [
            {"text": "That some of the particles are small enough to get "
                     "through the gaps", "correct": True},
            {"text": "That the clay dissolved in the water while it stood",
             "correct": False,
             "why": "A dissolved substance leaves a clear liquid. Cloudiness "
                    "means solid particles are still floating in it."},
            {"text": "That the paper was put into the funnel the wrong way "
                     "round", "correct": False,
             "why": "Both faces of a filter paper are the same tangle of "
                    "fibres, so there is no wrong way round."},
            {"text": "That the water was too cold for the paper to work "
                     "properly", "correct": False,
             "why": "Temperature changes neither the gaps in the paper nor "
                    "the size of the clay particles."},
        ],
        "figure": None,
    },
    {
        "id": "c3-03-s24",
        "band": "standard",
        "text": "Two students filter identical mixtures using the same grade "
                "of paper. One uses a large funnel and a large paper, the "
                "other a small one. Whose finishes first, and why?",
        "options": [
            {"text": "The small one, because the liquid is pushed through a "
                     "narrower space", "correct": False,
             "why": "A narrow funnel gives the liquid less paper to pass "
                    "through, so it takes longer rather than less time."},
            {"text": "They finish together, because the grade of paper is the "
                     "same", "correct": False,
             "why": "The grade is the same but the area is not, and it is the "
                    "area that sets how fast the liquid gets through."},
            {"text": "The large one, because more paper is in contact with "
                     "the liquid", "correct": True},
            {"text": "The small one, because a small funnel grips the paper "
                     "more tightly", "correct": False,
             "why": "How tightly the paper sits decides whether liquid leaks "
                    "round the edge, not how fast it passes through."},
        ],
        "figure": None,
    },
    {
        "id": "c3-03-s25",
        "band": "standard",
        "text": "Salt water is filtered and nothing at all is caught in the "
                "paper. The paper is left to dry and a faint white mark "
                "appears on it. Explain that mark.",
        "options": [
            {"text": "The paper caught a little of the salt after all, and it "
                     "has now shown up", "correct": False,
             "why": "Nothing was caught on the way through. The salt arrived "
                    "in the solution that soaked into the paper."},
            {"text": "The paper reacted with the salt water and changed "
                     "colour where it was wet", "correct": False,
             "why": "No reaction takes place. The paper is unchanged, and "
                    "something has simply been left lying on it."},
            {"text": "The paper was wet with salt solution, and the salt "
                     "stayed as it dried", "correct": True},
            {"text": "The paper has dried unevenly, and there is no salt in "
                     "the mark at all", "correct": False,
             "why": "Plain water dries off a paper and leaves no mark, so "
                    "something must have been left behind by this liquid."},
        ],
        "figure": None,
    },
    {
        "id": "c3-03-s26",
        "band": "standard",
        "text": "A student has a sieve with 1 mm holes and wants to use it "
                "to separate chalk powder from water. Will it work?",
        "options": [
            {"text": "Yes, because chalk is insoluble, and a sieve holds back "
                     "anything insoluble", "correct": False,
             "why": "Being insoluble is not enough. The pieces also have to "
                    "be wider than the gaps they are poured through."},
            {"text": "Yes, as long as the mixture is poured through the sieve "
                     "very slowly", "correct": False,
             "why": "Pouring slowly does not make a 1 mm hole any narrower "
                    "than a particle of chalk powder."},
            {"text": "No, because the water would not pass through holes that "
                     "size", "correct": False,
             "why": "Water passes a 1 mm hole freely. The difficulty is that "
                    "the chalk goes through with it."},
            {"text": "No, because the chalk particles are far narrower than "
                     "1 mm", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c3-03-s27",
        "band": "standard",
        "text": "250 g of a sand and water mixture is filtered. 235 g of "
                "filtrate is collected, and the paper with the wet residue "
                "has gained 15 g. What does that show?",
        "options": [
            {"text": "That 15 g of the water was destroyed on its way through "
                     "the paper", "correct": False,
             "why": "Nothing is destroyed by filtering. That 15 g is the "
                    "liquid still held in the paper and the wet sand."},
            {"text": "That all the mass is still there, shared between the "
                     "two parts", "correct": True},
            {"text": "That 15 g of the sand dissolved into the filtrate as it "
                     "passed", "correct": False,
             "why": "Sand is insoluble, and anything dissolved would be part "
                    "of the filtrate's mass rather than missing from it."},
            {"text": "That the balance is faulty, since the two parts should "
                     "both be 125 g", "correct": False,
             "why": "There is no reason for the two parts to be equal. The "
                    "mixture was mostly water to begin with."},
        ],
        "figure": None,
    },
    {
        "id": "c3-03-s28",
        "band": "standard",
        "text": "Two grades of filter paper are available: grade A has wider "
                "gaps than grade B. A student needs the clearest filtrate "
                "they can get. Which should they use, and at what cost?",
        "options": [
            {"text": "Grade B, and the filtering will take longer",
             "correct": True},
            {"text": "Grade B, and the filtering will be over sooner",
             "correct": False,
             "why": "Narrower gaps always slow a liquid down, whatever they "
                    "do for the clarity of the filtrate."},
            {"text": "Grade A, and the residue will come out cleaner",
             "correct": False,
             "why": "Wider gaps let more solid through, so the residue is "
                    "worse as well as the filtrate."},
            {"text": "Grade A, because a wider gap catches more on the way "
                     "past", "correct": False,
             "why": "A wider gap catches less, which is exactly what makes "
                    "the filtrate cloudier."},
        ],
        "figure": None,
    },
    {
        "id": "c3-03-s29",
        "band": "standard",
        "text": "Halfway through filtering a very cloudy mixture the "
                "dripping slows almost to a stop, although the paper is not "
                "torn and the funnel is not full. Explain.",
        "options": [
            {"text": "The paper has soaked up as much liquid as it can hold",
             "correct": False,
             "why": "A paper soaks up only a few drops, and liquid keeps "
                    "passing through it once it has taken them up."},
            {"text": "The residue building up is blocking the gaps in the "
                     "paper", "correct": True},
            {"text": "The mixture left in the funnel is the part with no "
                     "liquid in it", "correct": False,
             "why": "The mixture is the same all the way through. There is no "
                    "part of it without liquid in it."},
            {"text": "The gaps in the paper close up once it has been wet a "
                     "while", "correct": False,
             "why": "Wet paper keeps exactly the same gaps. What has "
                    "collected on top of them is what is in the way."},
        ],
        "figure": None,
    },
    {
        "id": "c3-03-s30",
        "band": "standard",
        "text": "A student says that filtering sand out of water is a "
                "chemical change, because the sand and the water end up in "
                "different places. Evaluate that.",
        "options": [
            {"text": "Right, because the mixture cannot be put back together "
                     "afterwards", "correct": False,
             "why": "It can be put back together in seconds, by tipping the "
                    "sand into the water and stirring."},
            {"text": "Right, because the sand has become a residue, which is "
                     "a new substance", "correct": False,
             "why": "Residue is only a name for where the sand ended up. The "
                    "sand itself is the same substance throughout."},
            {"text": "Wrong, because no new substance is made and both parts "
                     "are unchanged", "correct": True},
            {"text": "Wrong, because a chemical change always needs heating "
                     "to happen", "correct": False,
             "why": "Plenty of chemical changes happen cold. What settles it "
                    "here is that nothing new was made."},
        ],
        "figure": None,
    },
    {
        "id": "c3-03-s31",
        "band": "standard",
        "text": "Why can filtration not be used to separate a mixture of "
                "sugar and salt?",
        "options": [
            {"text": "Because both of them dissolve, so neither stays in the "
                     "paper", "correct": True},
            {"text": "Because sugar dissolves and salt does not, so only one "
                     "would be caught", "correct": False,
             "why": "Both of them dissolve in water. Salt is one of the most "
                    "soluble solids a laboratory has."},
            {"text": "Because their particles are too nearly the same size "
                     "for a paper to tell apart", "correct": False,
             "why": "Size is not the difficulty here, because the paper would "
                    "hold back neither of them however they compared."},
            {"text": "Because they are both white, and a filter separates by "
                     "colour", "correct": False,
             "why": "A filter separates by size alone. Colour plays no part "
                    "in what it holds back."},
        ],
        "figure": None,
    },
    {
        "id": "c3-03-s32",
        "band": "standard",
        "text": "A student has a white powder and wants to find out whether "
                "it is soluble in water. How could filtering answer that?",
        "options": [
            {"text": "Filter the dry powder, and see how much passes through "
                     "the paper", "correct": False,
             "why": "A dry powder sits in the paper whatever it is, because "
                    "there is no liquid to carry it through."},
            {"text": "Stir it into water and filter: a cloudy filtrate means "
                     "it dissolved", "correct": False,
             "why": "A cloudy filtrate means solid got through the paper. "
                    "Anything dissolved gives a clear one."},
            {"text": "Filter the water first, then add the powder to the "
                     "filtrate and watch", "correct": False,
             "why": "Filtering the water beforehand tells you nothing about a "
                    "powder that has not met it yet."},
            {"text": "Stir it into water and filter: powder left in the paper "
                     "was insoluble", "correct": True},
        ],
        "figure": None,
    },
    # ── harder · MRB-338 expansion ──────────────────────────────────────
    {
        "id": "c3-03-h08",
        "band": "harder",
        "text": "A dialysis machine uses a membrane that lets dissolved "
                "waste through while holding blood cells back. Why does that "
                "not show that a fine enough paper could hold salt back?",
        "options": [
            {"text": "Because the membrane is the same fibre as filter paper, "
                     "only made thinner", "correct": False,
             "why": "A membrane is not paper at all, and the comparison would "
                    "not help even if it were."},
            {"text": "Because the membrane lets the dissolved particles "
                     "through, exactly as paper does", "correct": True},
            {"text": "Because the membrane holds the dissolved waste back and "
                     "passes the cells", "correct": False,
             "why": "It works the other way round. The cells are the large "
                    "things, and they are the part that stays behind."},
            {"text": "Because a dialysis membrane has no gaps in it at all, "
                     "unlike a paper", "correct": False,
             "why": "A membrane is full of tiny gaps. That is how the "
                    "dissolved waste crosses it in the first place."},
        ],
        "figure": None,
    },
    {
        "id": "c3-03-h09",
        "band": "harder",
        "text": "In a laboratory a filter funnel can be connected to a pump that lowers the air pressure in the flask below it. What does that change?",
        "options": [
            {
             "text": "Dissolved substances are pulled out and held in the paper",
             "correct": False,
             "why": "Lowering the pressure moves the liquid along faster. It does nothing at all to what is dissolved in it.",
            },
            {
             "text": "The gaps in the paper are pulled wider",
             "correct": False,
             "why": "The paper is unchanged. What changes is how hard the liquid is pushed against it from above.",
            },
            {
             "text": "The residue dissolves into the filtrate",
             "correct": False,
             "why": "An insoluble residue does not dissolve because the pressure beneath it has fallen.",
            },
            {
             "text": "The liquid is pushed through the paper faster",
             "correct": True,
            },
        ],
        "figure": None,
    },
    {
        "id": "c3-03-h10",
        "band": "harder",
        "text": "A hot solution is filtered to remove an insoluble "
                "impurity, but it cools on the way and crystals of the "
                "dissolved solid appear in the paper. Explain what has "
                "happened.",
        "options": [
            {"text": "Less of the solid stays dissolved when it is cold, so "
                     "some has come out", "correct": True},
            {"text": "The paper has cooled the solution enough to turn some "
                     "of the water solid", "correct": False,
             "why": "It is the dissolved solid that has crystallised. The "
                    "water is nowhere near cold enough to freeze."},
            {"text": "The solid has reacted with the filter paper and formed "
                     "crystals on it", "correct": False,
             "why": "Nothing reacts with filter paper. The crystals are the "
                    "same substance that was dissolved in the liquid."},
            {"text": "The crystals were in the solution all along and have "
                     "only now been caught", "correct": False,
             "why": "The solution was clear while it was hot, so the crystals "
                    "must have formed on the way, as it cooled."},
        ],
        "figure": None,
    },
    {
        "id": "c3-03-h11",
        "band": "harder",
        "text": "A 40.0 g sample of sea salt contains some insoluble sand. "
                "Dissolving and filtering leaves 2.8 g of dried residue, and "
                "evaporating what comes through gives 37.2 g of salt. What "
                "percentage of the sample was salt?",
        "options": [
            {"text": "7.0%", "correct": False,
             "why": "That is the insoluble share, 2.8 g out of 40.0 g. The "
                    "question asks for the salt instead."},
            {"text": "37.2%", "correct": False,
             "why": "That is the mass of salt in grams read as a percentage. "
                    "It still has to be compared with the 40.0 g."},
            {"text": "93.0%", "correct": True},
            {"text": "2.8%", "correct": False,
             "why": "That is the residue's mass in grams, read as a "
                    "percentage without dividing by anything."},
        ],
        "figure": None,
    },
    {
        "id": "c3-03-h12",
        "band": "harder",
        "text": "A student shakes 30.0 g of a white powder with water, filters it, and dries whatever the paper holds. That comes to 30.0 g. What does the result show?",
        "options": [
            {
             "text": "That the powder dissolved and was recovered",
             "correct": False,
             "why": "Anything dissolved stays in the filtrate, so it could not be in the paper waiting to be weighed.",
            },
            {
             "text": "That the residue was weighed while still wet",
             "correct": False,
             "why": "Wet residue would weigh more than the 30.0 g put in, rather than exactly the same.",
            },
            {
             "text": "That half of it dissolved",
             "correct": False,
             "why": "Half would leave 15.0 g in the paper. All 30.0 g of the powder is accounted for there.",
            },
            {
             "text": "That none of the powder dissolved",
             "correct": True,
            },
        ],
        "figure": None,
    },
    {
        "id": "c3-03-h13",
        "band": "harder",
        "text": "A student is finding the percentage of insoluble grit in rock salt, and the paper tears so that some grit reaches the flask. What happens to the percentage they calculate?",
        "options": [
            {
             "text": "It comes out too low, because some grit was never weighed",
             "correct": True,
            },
            {
             "text": "It comes out too high, because the grit is counted twice",
             "correct": False,
             "why": "Grit in the flask is not counted at all. It is simply missing from what the paper holds.",
            },
            {
             "text": "It comes out too high, because the residue stays wetter",
             "correct": False,
             "why": "A tear lets liquid through faster if anything, and it is the missing grit that changes the answer.",
            },
            {
             "text": "It is unaffected, because the sample's mass has not changed",
             "correct": False,
             "why": "The sample is unchanged, but the measured residue is smaller, so the fraction comes out smaller too.",
            },
        ],
        "figure": None,
    },
    {
        "id": "c3-03-h14",
        "band": "harder",
        "text": "A mixture of sand and salt water is to be separated so that the sand ends up clean and dry. Which order of steps does that?",
        "options": [
            {
             "text": "Filter, dry the sand, then rinse it with distilled water",
             "correct": False,
             "why": "Rinsing after drying wets the sand all over again, and the salt it was carrying has already dried into it.",
            },
            {
             "text": "Evaporate the whole mixture, then pick the sand out",
             "correct": False,
             "why": "Evaporating leaves every bit of the salt behind on the sand, which is the one thing to be avoided.",
            },
            {
             "text": "Filter, rinse the sand in the paper, then dry it",
             "correct": True,
            },
            {
             "text": "Add distilled water, then filter and dry the sand",
             "correct": False,
             "why": "Diluting it first still leaves salt solution in the sand when it is filtered, and that dries into it.",
            },
        ],
        "figure": None,
    },
    {
        "id": "c3-03-h15",
        "band": "harder",
        "text": "Two students filter sand out of salt water and dry the "
                "sand. One rinses the residue with distilled water first and "
                "the other does not. Whose dried sand has the greater mass?",
        "options": [
            {"text": "The one who rinsed, because rinsing washes extra solid "
                     "down into the paper", "correct": False,
             "why": "Rinsing washes solution out of the residue. It adds "
                    "nothing solid to what is already there."},
            {"text": "The one who did not rinse, because salt dried into the "
                     "sand", "correct": True},
            {"text": "The one who did not rinse, because a rinse dissolves "
                     "some of the sand away", "correct": False,
             "why": "Sand is insoluble, so distilled water cannot dissolve "
                    "any of it however much is poured over it."},
            {"text": "Neither, because a rinse only adds water, which dries "
                     "off anyway", "correct": False,
             "why": "The rinse carries dissolved salt away as well, and salt "
                    "does not dry off the way water does."},
        ],
        "figure": None,
    },
    {
        "id": "c3-03-h16",
        "band": "harder",
        "text": "Only 2 cm³ of a cloudy mixture is available and the liquid is the part that is wanted. Why might a centrifuge be a better choice than a filter funnel?",
        "options": [
            {
             "text": "Because a paper would soak up much of so small a volume",
             "correct": True,
            },
            {
             "text": "Because a centrifuge separates dissolved substances too",
             "correct": False,
             "why": "A centrifuge sorts by density. Anything dissolved stays in the liquid however fast it is spun.",
            },
            {
             "text": "Because a paper cannot hold back particles this fine",
             "correct": False,
             "why": "Nothing here says the particles are unusually fine. The difficulty is how little liquid there is.",
            },
            {
             "text": "Because spinning makes the solid dissolve",
             "correct": False,
             "why": "Spinning a mixture dissolves nothing. It makes the solid settle out more quickly than it would.",
            },
        ],
        "figure": None,
    },
    {
        "id": "c3-03-h17",
        "band": "harder",
        "text": "River water carries clay so fine that it neither settles "
                "nor is held back by a filter. What does a treatment works "
                "do about it?",
        "options": [
            {"text": "Filters it through a grade of paper narrow enough to "
                     "catch the clay", "correct": False,
             "why": "Gaps that narrow clog almost at once at that scale, and "
                    "the finest particles pass them anyway."},
            {"text": "Boils the water, so the clay is destroyed by the heat",
             "correct": False,
             "why": "Clay is not destroyed by boiling, and boiling every "
                    "litre a town drinks could never be done."},
            {"text": "Adds a chemical that makes the fine particles clump "
                     "together", "correct": True},
            {"text": "Adds more water, to dilute the clay until it cannot be "
                     "seen", "correct": False,
             "why": "Diluting removes nothing, and a works has no spare clean "
                    "water to dilute anything with."},
        ],
        "figure": None,
    },
    {
        "id": "c3-03-h18",
        "band": "harder",
        "text": "A treatment works filters the water through sand before it "
                "adds the chlorine, rather than afterwards. Suggest why that "
                "order is chosen.",
        "options": [
            {"text": "Because chlorine would dissolve the sand in the beds if "
                     "it went in first", "correct": False,
             "why": "Chlorine does not dissolve sand. Sand is among the least "
                    "reactive things a works handles."},
            {"text": "Because the sand beds would filter the chlorine straight "
                     "back out again", "correct": False,
             "why": "Chlorine dissolves in the water, so a bed of sand lets "
                    "it through exactly as paper would."},
            {"text": "Because chlorine only works on water that is already "
                     "pure", "correct": False,
             "why": "Chlorine works perfectly well in ordinary water. It is "
                    "simply used up by any solid that is there."},
            {"text": "Because solid particles use the chlorine up and shield "
                     "the microbes", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c3-03-h19",
        "band": "harder",
        "text": "Three papers are tested on the same mixture. Paper P has "
                "20 micrometre gaps and takes 40 s, paper Q has 8 "
                "micrometre gaps and takes 95 s, paper R has 2.5 micrometre "
                "gaps and takes 210 s. What do the results show?",
        "options": [
            {"text": "The narrower the gaps, the quicker the filtering is "
                     "over", "correct": False,
             "why": "The times rise as the gaps narrow: 40 s, then 95 s, then "
                    "210 s for the narrowest paper of the three."},
            {"text": "The narrower the gaps, the longer the filtering takes",
             "correct": True},
            {"text": "The time depends on how thick each paper is rather than "
                     "on its gaps", "correct": False,
             "why": "Nothing in the results says anything about thickness. "
                    "The gap size is the one thing that was changed."},
            {"text": "All three separate at the same rate once the first "
                     "drops appear", "correct": False,
             "why": "The three times are 40 s, 95 s and 210 s, which is not "
                    "the same rate by any reading."},
        ],
        "figure": None,
    },
    {
        "id": "c3-03-h20",
        "band": "harder",
        "text": "A blue solid is stirred into water together with some sand. After filtering, the residue is grey and the filtrate is blue. What does that show about the blue solid?",
        "options": [
            {
             "text": "That it reacted with the sand and lost its colour",
             "correct": False,
             "why": "The colour is in the filtrate because the substance is. Nothing has reacted with anything.",
            },
            {
             "text": "That it was caught in the paper but its colour ran on",
             "correct": False,
             "why": "Colour does not travel on its own. It goes wherever the substance carrying it goes.",
            },
            {
             "text": "That it was heavier than the sand and sank through",
             "correct": False,
             "why": "A dissolved substance does not sink through paper. It is carried along by the liquid it is in.",
            },
            {
             "text": "That it dissolved, so it went through with the water",
             "correct": True,
            },
        ],
        "figure": None,
    },
    {
        "id": "c3-03-h21",
        "band": "harder",
        "text": "A car engine's oil filter takes tiny pieces of metal out of the oil, but the additives dissolved in that oil pass through untouched. Explain why.",
        "options": [
            {
             "text": "The metal is in lumps wider than the gaps; the additives are dissolved",
             "correct": True,
            },
            {
             "text": "The additives are designed to pass the filter and the metal is not",
             "correct": False,
             "why": "Nothing about additives is built into the filter. It holds back lumps and passes everything else.",
            },
            {
             "text": "Oil is too thick for a filter to hold back anything dissolved in it",
             "correct": False,
             "why": "How thick the oil is decides how fast it flows, not whether a dissolved particle can be caught.",
            },
            {
             "text": "The additives are too light to be caught, and the metal pieces are heavy enough to drop out",
             "correct": False,
             "why": "A filter sorts by size, not by weight. A heavy particle small enough to fit through a gap goes through it.",
            },
        ],
        "figure": None,
    },
    {
        "id": "c3-03-h22",
        "band": "harder",
        "text": "A cafetière presses coffee through a metal mesh and a "
                "little fine grit reaches the cup. A paper filter leaves "
                "none. Explain the difference.",
        "options": [
            {"text": "The mesh is metal, and metal holds back nothing made "
                     "from a plant", "correct": False,
             "why": "What a filter is made of does not decide what it "
                    "catches. The width of its gaps does."},
            {"text": "The paper dissolves the finest grounds before they "
                     "reach the cup", "correct": False,
             "why": "Paper dissolves nothing. It holds the fine grounds back "
                    "among its fibres instead."},
            {"text": "The mesh has wider gaps, so the finest grounds get "
                     "through it", "correct": True},
            {"text": "The paper is used hotter than the mesh, and heat holds "
                     "the fine grounds back", "correct": False,
             "why": "Temperature has nothing to do with what a filter "
                    "catches. The width of its gaps decides that."},
        ],
        "figure": None,
    },
    {
        "id": "c3-03-h23",
        "band": "harder",
        "text": "A vacuum cleaner separates dust from air using a filter. Is it right to call that filtration?",
        "options": [
            {
             "text": "No, because the dust is held in a bag rather than on a paper",
             "correct": False,
             "why": "What the solid is caught in does not decide the name. A bag and a paper both let something flow through while the solid cannot.",
            },
            {
             "text": "No, because the dust is dissolved in the air rather than carried by it",
             "correct": False,
             "why": "Dust is not dissolved in anything. It is solid specks being carried along by the moving air.",
            },
            {
             "text": "Yes, because the air passes and the solid is held back by size",
             "correct": True,
            },
            {
             "text": "Yes, because the air is held back and the dust passes through",
             "correct": False,
             "why": "It is the other way round. The air goes through and the dust is the part that stays behind.",
            },
        ],
        "figure": None,
    },
    {
        "id": "c3-03-h24",
        "band": "harder",
        "text": "A treatment works filters millions of litres a day through "
                "beds of sand rather than through filter paper. Suggest why "
                "sand is used.",
        "options": [
            {"text": "A bed of sand is enormous, hard-wearing, and can be "
                     "washed out and used again", "correct": True},
            {"text": "Sand catches the dissolved substances that paper would "
                     "let through", "correct": False,
             "why": "Sand has far wider gaps than paper, so it catches less "
                    "rather than more."},
            {"text": "Paper would separate the water itself into its parts",
             "correct": False,
             "why": "Paper does not break water into anything. It only holds "
                    "back solid that is too big to pass."},
            {"text": "Sand can be heated to kill the microbes caught in it",
             "correct": False,
             "why": "The beds are never heated, and the microbes are dealt "
                    "with later on, by the chlorine."},
        ],
        "figure": None,
    },
    {
        "id": "c3-03-h25",
        "band": "harder",
        "text": "A student stirs 5.0 g of mud into water, filters it, and "
                "finds the dried residue has a mass of only 3.6 g. Give the "
                "most likely reasons.",
        "options": [
            {"text": "Some of the mud dissolved and was carried into the "
                     "flask", "correct": False,
             "why": "Mud is insoluble, which is why it can be filtered at "
                    "all. Dissolving is not where it went."},
            {"text": "Some stayed in the beaker, and the finest particles "
                     "passed through", "correct": True},
            {"text": "Some of the mud was destroyed by being stirred so "
                     "vigorously", "correct": False,
             "why": "Stirring breaks lumps into smaller lumps. It destroys "
                    "none of the solid that is there."},
            {"text": "Some of the mud evaporated while the residue was "
                     "drying", "correct": False,
             "why": "Drying drives the water off. The solid mud stays exactly "
                    "where it is in the paper."},
        ],
        "figure": None,
    },
    {
        "id": "c3-03-h26",
        "band": "harder",
        "text": "Filtering sea water leaves it as salty as before, but "
                "boiling it and catching what rises gives water with no salt "
                "in it. What is the difference in principle?",
        "options": [
            {"text": "It makes the salt particles larger, so they can be "
                     "caught afterwards", "correct": False,
             "why": "The salt is unchanged by heating. It is simply left in "
                    "the pan as the water leaves."},
            {"text": "It destroys the salt with the heat, so nothing is left "
                     "to separate", "correct": False,
             "why": "Nothing is destroyed. The salt stays in the pan and can "
                    "be scraped out at the end."},
            {"text": "It dissolves the salt more thoroughly, so the water can "
                     "be poured off", "correct": False,
             "why": "Dissolving it further would make it harder, and "
                    "dissolved salt cannot be poured off a solution."},
            {"text": "It moves the water away from the salt instead of "
                     "holding the salt back", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c3-03-h27",
        "band": "harder",
        "text": "Two cloudy mixtures are filtered through identical papers. "
                "One filtrate comes out clear and the other stays cloudy. "
                "What is the most likely difference between them?",
        "options": [
            {"text": "The particles in the second one are narrower than the "
                     "gaps in the paper", "correct": True},
            {"text": "The second one was a clear solution rather than a cloudy "
                     "suspension of solid", "correct": False,
             "why": "A solution is clear before it is filtered. A cloudy "
                    "liquid has solid particles floating in it."},
            {"text": "The second one contained a greater volume of liquid",
             "correct": False,
             "why": "How much liquid there is changes how long it takes, not "
                    "what manages to get through."},
            {"text": "The second one was poured into the funnel more slowly",
             "correct": False,
             "why": "Pouring slowly gives a cleaner filtrate, so that would "
                    "make the second one clearer rather than cloudier."},
        ],
        "figure": None,
    },
    {
        "id": "c3-03-h28",
        "band": "harder",
        "text": "After filtering, the filtrate weighs less than the mixture "
                "that was poured in. A student says that mass has been lost. "
                "Evaluate that.",
        "options": [
            {"text": "Right, because some mass is always lost when a mixture "
                     "is separated", "correct": False,
             "why": "Separating a mixture moves mass from one place to "
                    "another; it never removes any of it."},
            {"text": "Right, because the solid has been turned into something "
                     "lighter", "correct": False,
             "why": "The solid is not changed by filtering at all, so its "
                    "mass is exactly what it was before."},
            {"text": "Wrong, because the rest of it is in the paper and the "
                     "residue", "correct": True},
            {"text": "Wrong, because the filtrate always weighs the same as "
                     "the mixture", "correct": False,
             "why": "The filtrate weighs less, because the wet paper and the "
                    "residue are holding the remainder."},
        ],
        "figure": None,
    },
    {
        "id": "c3-03-h29",
        "band": "harder",
        "text": "A mixture contains sand, chalk powder and water. Can "
                "filtering separate the sand from the chalk?",
        "options": [
            {"text": "Yes, because the sand grains are larger and are caught "
                     "higher up the paper", "correct": False,
             "why": "Both are held at the paper together, and nothing sorts "
                    "them by size once they are sitting there."},
            {"text": "Yes, because chalk dissolves slowly and the sand does "
                     "not", "correct": False,
             "why": "Chalk is insoluble in water, so neither of the two "
                    "dissolves and neither passes through."},
            {"text": "No, because the water carries both of them into the "
                     "flask", "correct": False,
             "why": "Both are insoluble lumps, so both are held back rather "
                    "than carried through with the water."},
            {"text": "No, because both are insoluble and stay in the paper "
                     "together", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c3-03-h30",
        "band": "harder",
        "text": "The same mass of chalk is filtered twice: once as coarse "
                "grains, and once ground to a fine powder. Which filtering "
                "takes longer, and why?",
        "options": [
            {"text": "The fine powder, because its particles pack into the "
                     "gaps in the paper", "correct": True},
            {"text": "The fine powder, because more of it dissolves and has "
                     "to be filtered twice", "correct": False,
             "why": "Chalk is insoluble however finely it is ground, and "
                    "nothing here is filtered twice."},
            {"text": "The coarse grains, because large lumps are harder to "
                     "push through a paper", "correct": False,
             "why": "Nothing is pushed through. The grains sit on the paper "
                    "while the liquid runs past them."},
            {"text": "Neither, because the mass is the same, so the time must "
                     "be the same", "correct": False,
             "why": "It is the size of the particles, not their total mass, "
                    "that decides how easily the liquid gets past."},
        ],
        "figure": None,
    },
    {
        "id": "c3-03-h31",
        "band": "harder",
        "text": "A treatment works filters 4 000 litres of water every "
                "minute. A school funnel filters 200 cm³ in 5 minutes. How "
                "many school funnels would match the works? "
                "(1 litre = 1 000 cm³)",
        "options": [
            {"text": "20 000", "correct": False,
             "why": "That uses 200 cm³ each minute and forgets that the "
                    "funnel takes five minutes to do it."},
            {"text": "100 000", "correct": True},
            {"text": "1 000", "correct": False,
             "why": "That is the number of cm³ in a litre, not a comparison "
                    "of the two rates."},
            {"text": "100", "correct": False,
             "why": "That is the answer with three noughts dropped, as though "
                    "a litre were the same as 1 cm³."},
        ],
        "figure": None,
    },
    {
        "id": "c3-03-h32",
        "band": "harder",
        "text": "A 2.0 litre sample of river water is filtered and the dried "
                "residue has a mass of 0.48 g. What mass of insoluble solid "
                "does the river carry in each litre?",
        "options": [
            {"text": "0.96 g", "correct": False,
             "why": "That is the residue multiplied by 2.0. Dividing by the "
                    "volume is what gives the mass in one litre."},
            {"text": "0.48 g", "correct": False,
             "why": "That is the residue from the whole 2.0 litre sample, not "
                    "from one litre of it."},
            {"text": "4.17 g", "correct": False,
             "why": "That is 2.0 divided by 0.48. The mass belongs on top of "
                    "the fraction, not underneath it."},
            {"text": "0.24 g", "correct": True},
        ],
        "figure": None,
    },
]
