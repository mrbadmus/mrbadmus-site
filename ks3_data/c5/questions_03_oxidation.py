"""C5 lesson 03 — Oxidation: twelve questions (MRB-246).

The lesson's argument has two halves and both are easy to half-learn. The
first is that oxidation is a substance GAINING oxygen, so the product is
heavier than what you started with, and speed has nothing to do with the
name. The second is what a controlled investigation is for: four tubes whose
results mean nothing apart and something together, and the two in the middle
doing the work. These twelve probe the angles the mastery ladder leaves
alone — the ladder takes tube 3 and the sacrificial block, so nothing here
repeats either.

The distractors are built from the lesson's two declared misconceptions.
`REACT-15` (rusting needs water only, or air only) drives the wrong options
in e03, e04, s01, s03 and h03, where one tube is asked to carry a conclusion
that needs four, or an accelerator is promoted to a requirement.
`REACT-14` (aluminium and stainless steel do not oxidise) drives s02, h01 and
h02 — each treats "it does not go orange" as "it does not react", and each
offers a mechanism for that which sounds like chemistry and is not:
reactivity being used up, a metal being treated so that it cannot oxidise, an
alloy made by two metals touching.

A third strand runs through e01, e02, s04 and h04 and belongs to neither
register entry: the belief that burning DESTROYS matter and that oxidation is
therefore a kind of loss. It is `PART-05` and `REACT-07` in an oxidation
costume — the mass goes UP, and it goes up by exactly the oxygen that joined
on. e02 and s04 carry the same belief in its classification form, where a
change that is fast, or that ends with something that looks nothing like the
metal, is imagined to be a different kind of reaction from one that is slow.

Every question here is new prose — a question bank is the one place in these
two files where that is true, and the bar is §13's: each distractor is a
WRONG RULE in the correct answer's own shape, and each is a mistake a real
student in a real lab makes. Every option set was measured; no correct option
is strictly the longest by four words or by 1.4×.
"""

UNIT = "C5"
LESSON = "oxidation"
LESSON_NUMBER = 3

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "c5-03-e01",
        "band": "easier",
        "text": "A strip of magnesium is weighed, burned in air, and the white "
                "powder left behind is weighed. What has happened to the "
                "mass?",
        "options": [
            {"text": "It has gone up, because oxygen from the air is now part "
                     "of the powder", "correct": True},
            {"text": "It has gone down, because some of the magnesium burned "
                     "away as smoke and was lost", "correct": False,
             "why": "Nothing is destroyed by burning. Every magnesium atom "
                    "that went in is still in the powder — what is different "
                    "is that oxygen atoms out of the air are now joined to "
                    "them, and those weigh something."},
            {"text": "It has stayed the same, because all of the magnesium is "
                     "still there in the powder", "correct": False,
             "why": "All of the magnesium is still there, and that is only "
                    "half the count. Something has been ADDED to it: the "
                    "oxygen in magnesium oxide came out of the air and has "
                    "mass of its own."},
            {"text": "It has gone down, because the light and heat given out "
                     "carried some of the mass away", "correct": False,
             "why": "Energy leaving is not a substance leaving. The only "
                    "things that moved were the magnesium and the oxygen it "
                    "joined with, and both are on the balance afterwards."},
        ],
        "figure": None,
    },
    {
        "id": "c5-03-e02",
        "band": "easier",
        "text": "Which one of these is an oxidation?",
        "options": [
            {"text": "Ice melting into water in a jug left in a warm room",
             "correct": False,
             "why": "Nothing gains oxygen, and nothing new is made — the "
                    "water was already water. Melting is a physical change, "
                    "which is why it can be undone in a freezer."},
            {"text": "Iron turning to rust on a gate left out in the rain",
             "correct": True},
            {"text": "Sugar dissolving into a mug of hot tea and disappearing",
             "correct": False,
             "why": "The sugar is still sugar, spread out through the tea. "
                    "Something vanishing from sight is not the same as "
                    "something reacting, and no oxygen has joined anything."},
            {"text": "Copper carbonate breaking down into copper oxide when "
                     "it is heated", "correct": False,
             "why": "An oxide is made, and the copper gains no oxygen — it "
                    "already had some, in the carbonate. That is thermal "
                    "decomposition: one substance broken apart by heat, with "
                    "no oxygen needed from outside."},
        ],
        "figure": None,
    },
    {
        "id": "c5-03-e03",
        "band": "easier",
        "text": "Two identical nails are left for four weeks. One is half in "
                "tap water with the tube open to the air. The other is in a "
                "bunged tube of dry air, with a drying agent in it. Which "
                "rusts?",
        "options": [
            {"text": "Both of them, because air is what makes iron rust and "
                     "both tubes had air", "correct": False,
             "why": "Air on its own is not enough, and the dry tube is what "
                    "shows it. The nail in dry air stays as shiny as the day "
                    "it went in, for as long as you care to leave it."},
            {"text": "Only the nail in the dry air, because water washes the "
                     "rust off the other one", "correct": False,
             "why": "Water does not wash rust away — rust is a solid that "
                    "clings to the nail and then flakes. The tube with water "
                    "in it is the one that rusts, and it rusts worst at the "
                    "water line."},
            {"text": "Only the nail in the tap water, because that tube has "
                     "both air and water", "correct": True},
            {"text": "Neither of them, because four weeks is not long enough "
                     "for any rust to form", "correct": False,
             "why": "Four weeks is plenty on a bare nail in tap water — the "
                    "orange shows at the water line well before that. Slow "
                    "does not mean invisible."},
        ],
        "figure": None,
    },
    {
        "id": "c5-03-e04",
        "band": "easier",
        "text": "Cars rust faster near the sea, and faster again after a "
                "winter of gritted roads. What is the salt doing?",
        "options": [
            {"text": "It is one of the things rusting needs, alongside oxygen "
                     "and water", "correct": False,
             "why": "A nail in plain tap water rusts perfectly well with no "
                    "salt anywhere near it. Salt cannot be a requirement for "
                    "something that happens without it."},
            {"text": "It makes the rust orange — without salt the iron would "
                     "corrode invisibly", "correct": False,
             "why": "The colour belongs to the rust itself, not to the salt. "
                    "The nail in plain tap water goes just as orange; the "
                    "salted one simply goes there faster and further."},
            {"text": "It stops the iron gaining oxygen, so the damage is a "
                     "different reaction", "correct": False,
             "why": "Salt does the opposite of stopping it — the salted tube "
                    "was the worst of the four in the same four weeks. And it "
                    "is the same reaction throughout: iron gaining oxygen."},
            {"text": "It speeds the rusting up, without being needed for it "
                     "to happen", "correct": True},
                   ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "c5-03-s01",
        "band": "s",
        "text": "In the tube of boiled water under oil, the nail shows the "
                "faintest trace of rust where the oil did not quite seal. "
                "What should the conclusion say about it?",
        "options": [
            {"text": "That the trace is where a little air got in, which "
                     "supports the conclusion rather than spoiling it",
             "correct": True},
            {"text": "That the experiment failed and this tube should be left "
                     "out of the results", "correct": False,
             "why": "A result that is not perfect is not a failed result. "
                    "Throwing out the tube that does not fit is how a wrong "
                    "conclusion survives, and this one fits — it is a trace "
                    "exactly where a little air got in."},
            {"text": "That water on its own can cause rusting, given enough "
                     "time and a sealed tube", "correct": False,
             "why": "The trace is where the seal failed, which is the one "
                    "place air reached the nail. Reading it as water acting "
                    "alone means reading the one part of the tube that was "
                    "not sealed as though it were."},
            {"text": "That the oil caused the trace, so oil is not a good "
                     "barrier against rusting after all", "correct": False,
             "why": "The oil is keeping air out, not putting anything in. "
                    "Blaming the trace on the oil confuses the method with "
                    "the thing being tested — the same mistake in the "
                    "opposite direction."},
                   ],
        "figure": None,
    },
    {
        "id": "c5-03-s02",
        "band": "s",
        "text": "Stainless steel cutlery is mostly iron, and it does not "
                "rust. Why not?",
        "options": [
            {"text": "The iron in it has been treated so that it can no "
                     "longer oxidise at all", "correct": False,
             "why": "Nothing can be done to iron that removes its ability to "
                    "react with oxygen. What an alloy changes is what the "
                    "surface becomes, not what the iron is capable of."},
            {"text": "The chromium in it oxidises into a tough layer that "
                     "seals the surface", "correct": True},
            {"text": "Stainless steel has no iron in it, which is why there "
                     "is nothing there to rust", "correct": False,
             "why": "It is mostly iron — the chromium and nickel are the "
                    "smaller part of it. If the iron were gone it would not "
                    "be steel."},
            {"text": "It is polished so smoothly that oxygen and water cannot "
                     "settle on it", "correct": False,
             "why": "A polished plain-steel nail rusts just as fast as a dull "
                    "one. Smoothness is not a barrier; a layer of oxide "
                    "that clings to the metal is."},
        ],
        "figure": None,
    },
    {
        "id": "c5-03-s03",
        "band": "s",
        "text": "A student sets up only two tubes: a nail in tap water open "
                "to the air, and a nail in boiled water under a layer of oil. "
                "After four weeks only the first has rusted. What can they "
                "conclude?",
        "options": [
            {"text": "That both oxygen and water are needed, since one tube "
                     "rusted and one did not", "correct": False,
             "why": "Both tubes had water in them, so nothing here tests "
                    "water at all. Only one thing was changed between them, "
                    "so only one thing can be concluded."},
            {"text": "That water is not needed, because the tube that was "
                     "full of water did not rust", "correct": False,
             "why": "That tube was also missing its air, which is the thing "
                    "that was changed. Blaming the water means blaming the "
                    "variable that stayed the same in both tubes."},
            {"text": "That oxygen is needed — and nothing yet about whether "
                     "water is needed too", "correct": True},
            {"text": "That oxygen is the only thing needed, since taking it "
                     "away stopped the rusting", "correct": False,
             "why": "Taking one thing away and seeing the rusting stop shows "
                    "that thing is needed. It says nothing about whether "
                    "anything else is needed as well — that takes a tube "
                    "which removes the water instead."},
        ],
        "figure": None,
    },
    {
        "id": "c5-03-s04",
        "band": "s",
        "text": "Magnesium burning and iron rusting are both oxidations, "
                "even though one takes two seconds and the other takes twenty "
                "years. Why does the difference in speed not change the name?",
        "options": [
            {"text": "Speed does change it — burning is called combustion, so "
                     "rusting cannot be oxidation too", "correct": False,
             "why": "Combustion and oxidation are not two alternatives to "
                    "choose between. Every combustion IS an oxidation; "
                    "combustion is the name for the fast kind that makes a "
                    "flame."},
            {"text": "Speed is not being measured here, so it cannot be used "
                     "to name anything at all", "correct": False,
             "why": "Speed is measured all the time in chemistry, and it "
                    "still does not name a reaction. The reason is what "
                    "the name describes, not whether it was timed."},
            {"text": "They are only loosely called the same thing; strictly, "
                     "rusting is a physical change", "correct": False,
             "why": "Rust is a new substance — orange, crumbly and nothing "
                    "like iron — and no amount of drying gets the nail back. "
                    "That is a chemical change by the ordinary test."},
            {"text": "A reaction is named for what happens to the substances, "
                     "not for how fast it happens", "correct": True},
                   ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "c5-03-h01",
        "band": "h",
        "text": "A galvanised gate and a painted gate are both scratched down "
                "to the steel underneath. Only the painted one starts to "
                "rust. Why?",
        "options": [
            {"text": "The zinc round the scratch corrodes in preference to "
                     "the iron; paint only covers", "correct": True},
            {"text": "The scratch in the paint is deeper, so more of the "
                     "steel underneath is exposed", "correct": False,
             "why": "Both are scratched to the steel, so both expose it. What "
                    "differs is what sits around the scratch: zinc goes on "
                    "protecting the bare metal beside it, and paint does "
                    "nothing at all once it is broken."},
            {"text": "Zinc is less reactive than iron, so the steel beside it "
                     "is left alone", "correct": False,
             "why": "Zinc is MORE reactive than iron, and that is exactly why "
                    "the method works. A less reactive coating would sit "
                    "there while the iron corroded."},
            {"text": "The zinc turns the exposed steel into stainless steel "
                     "where the two touch", "correct": False,
             "why": "An alloy is made by melting metals together, not by two "
                    "of them being in contact. The zinc stays zinc and the "
                    "steel stays steel — what changes is which one corrodes."},
        ],
        "figure": None,
    },
    {
        "id": "c5-03-h02",
        "band": "h",
        "text": "Aluminium is more reactive than iron, yet an aluminium "
                "window frame lasts decades outdoors while an iron one rusts "
                "through. What explains it?",
        "options": [
            {"text": "Aluminium uses up all its reactivity in the first "
                     "reaction and has none left afterwards", "correct": False,
             "why": "Reactivity is not a fuel tank that empties. The "
                    "aluminium under the oxide is exactly as reactive as it "
                    "ever was — it is simply sealed off from the air."},
            {"text": "Aluminium oxide clings to the metal and seals it, while "
                     "rust flakes off and exposes fresh iron", "correct": True},
            {"text": "Aluminium is only more reactive at high temperatures, "
                     "and a window frame is always cold", "correct": False,
             "why": "Aluminium oxidises the instant it meets air at ordinary "
                    "temperatures, which is why a fresh cut goes dull "
                    "immediately. Heat is not what decides this."},
            {"text": "The aluminium frame is coated in a paint that an iron "
                     "frame is never given", "correct": False,
             "why": "Bare, unpainted aluminium lasts outdoors just as well. "
                    "The layer doing the protecting is one the metal grew "
                    "itself, before anybody painted anything."},
                   ],
        "figure": None,
    },
    {
        "id": "c5-03-h03",
        "band": "h",
        "text": "A student says the salt-water tube proves that rusting needs "
                "salt, because that tube rusted the most of the four. What is "
                "wrong with the claim?",
        "options": [
            {"text": "The salt-water tube also had oxygen and water, so the "
                     "salt cannot have done anything", "correct": False,
             "why": "It clearly did something — that tube rusted far worse "
                    "than the one without salt, in the same four weeks. The "
                    "problem is what KIND of something, not whether there was "
                    "any."},
            {"text": "Salt is needed, but only in sea air, so the claim is "
                     "true for a car near the coast", "correct": False,
             "why": "A requirement does not switch on and off with a "
                    "postcode. If rusting needed salt, the plain water tube "
                    "would still be shiny, and it is not."},
            {"text": "The plain water tube had no salt and rusted anyway, so "
                     "salt cannot be a requirement", "correct": True},
            {"text": "Rusting the most is what proves a factor is needed, so "
                     "the reasoning has been done backwards", "correct": False,
             "why": "Rusting the most is not what proves anything is needed. "
                    "The only test for needed is removing it and seeing "
                    "whether the reaction still happens."},
                   ],
        "figure": None,
    },
    {
        "id": "c5-03-h04",
        "band": "h",
        "text": "Lemon juice squeezed onto a cut apple stops the surface "
                "going brown. What is happening?",
        "options": [
            {"text": "The juice makes a waterproof layer that keeps all of "
                     "the oxygen off the apple", "correct": False,
             "why": "Lemon juice is mostly water and seals nothing. If a "
                    "barrier were the answer, plain water would work just as "
                    "well, and it does not."},
            {"text": "The acid kills the reaction, because oxidation cannot "
                     "happen in acid at all", "correct": False,
             "why": "Plenty of oxidations happen in acid — rusting is faster "
                    "in it. The active ingredient here is the vitamin C, not "
                    "the sourness."},
            {"text": "The juice replaces the oxygen inside the apple with "
                     "something that cannot oxidise", "correct": False,
             "why": "Nothing is swapped out of the apple. The oxygen is in "
                    "the air above it and stays there; what changes is which "
                    "substance gets to it first."},
            {"text": "Vitamin C in the juice is oxidised instead, so the "
                     "apple's own substances are not", "correct": True},
        ],
        "figure": None,
    },
]
