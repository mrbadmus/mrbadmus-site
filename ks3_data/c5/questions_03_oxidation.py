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
        "band": "standard",
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
        "band": "standard",
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
        "band": "standard",
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
        "band": "standard",
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
        "band": "harder",
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
        "band": "harder",
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
        "band": "harder",
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
        "band": "harder",
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

    # ── easier · MRB-335 top-up ─────────────────────────────────────────
    {
        "id": "c5-03-e05",
        "band": "easier",
        "text": "What happens to a substance in an oxidation?",
        "options": [
            {"text": "It is broken apart by heat into two or more simpler "
                     "substances, which is why an oxidation always needs a "
                     "flame under it",
             "correct": False,
             "why": "That is thermal decomposition, and rusting is an "
                    "oxidation that needs no heat at all"},
            {"text": "It gains oxygen",
             "correct": True},
            {"text": "It loses oxygen",
             "correct": False,
             "why": "That is reduction, which comes at GCSE. Oxidation is the "
                    "gain"},
            {"text": "It dissolves in water",
             "correct": False,
             "why": "Dissolving makes nothing new. An oxidation is a chemical "
                    "change"},
        ],
        "figure": None,
    },
    {
        "id": "c5-03-e06",
        "band": "easier",
        "text": "What is corrosion?",
        "options": [
            {"text": "A metal being worn away by rubbing against something "
                     "else, which is why a gate hinge wears thin where it "
                     "turns and nowhere else along its length",
             "correct": False,
             "why": "That is wear, and it is physical. Corrosion is a "
                    "chemical change"},
            {"text": "Rust, and nothing else",
             "correct": False,
             "why": "Rusting is one kind of corrosion. Aluminium and zinc "
                    "corrode too, and neither of them rusts"},
            {"text": "A metal being eaten away by reacting with its "
                     "surroundings",
             "correct": True},
            {"text": "A metal melting in the heat",
             "correct": False,
             "why": "Melting is a change of state and makes nothing new"},
        ],
        "figure": None,
    },
    {
        "id": "c5-03-e07",
        "band": "easier",
        "text": "Which two things does iron need before it will rust?",
        "options": [
            {"text": "Salt and water",
             "correct": False,
             "why": "Salt only speeds it up. A nail in plain tap water open "
                    "to the air rusts perfectly well"},
            {"text": "Heat and oxygen",
             "correct": False,
             "why": "Rusting happens at any ordinary temperature. Water is "
                    "the second thing it needs"},
            {"text": "Oxygen and salt, which is why cars rust so much faster "
                     "in a coastal town or after a winter of gritting",
             "correct": False,
             "why": "Salt makes it faster and is not required. Water is what "
                    "the four-tube experiment shows is needed"},
            {"text": "Oxygen and water",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c5-03-e08",
        "band": "easier",
        "text": "What is sacrificial protection?",
        "options": [
            {"text": "Attaching a more reactive metal so that it corrodes in "
                     "preference to the iron",
             "correct": True},
            {"text": "Coating iron in paint so that nothing can reach the "
                     "surface, which is the cheapest way of keeping a gate "
                     "from rusting for a season or two",
             "correct": False,
             "why": "That is a barrier. Sacrificial protection uses a metal "
                    "that corrodes INSTEAD of the iron"},
            {"text": "Keeping the metal dry so it never rusts",
             "correct": False,
             "why": "That works and is not what the name means. Nothing is "
                    "being sacrificed"},
            {"text": "Replacing iron with a metal that does not corrode",
             "correct": False,
             "why": "Then there would be no iron to protect. The point is to "
                    "keep the iron and lose something else"},
        ],
        "figure": None,
    },
    {
        "id": "c5-03-e09",
        "band": "easier",
        "text": "Rust flakes off an iron gate. What does aluminium oxide do "
                "instead?",
        "options": [
            {"text": "It dissolves into the rain and washes away, so no layer "
                     "of it ever builds up thickly enough to be seen on a "
                     "window frame",
             "correct": False,
             "why": "It stays put, which is exactly why the frame lasts. "
                    "Washing away would leave fresh metal exposed"},
            {"text": "It clings to the metal and seals the surface",
             "correct": True},
            {"text": "It never forms, because aluminium does not corrode",
             "correct": False,
             "why": "Aluminium is MORE reactive than iron and oxidises at "
                    "once. The layer it forms is what protects it"},
            {"text": "It flakes off as well, only more slowly",
             "correct": False,
             "why": "It does not flake at all. Clinging is the whole "
                    "difference between the two metals"},
        ],
        "figure": None,
    },
    {
        "id": "c5-03-e10",
        "band": "easier",
        "text": "What is a control tube for?",
        "options": [
            {"text": "To show what the experiment looks like when it is going "
                     "correctly, so that the other tubes can be compared "
                     "against a tube that is known to be right",
             "correct": False,
             "why": "The tube that rusts is the one going as expected. A "
                    "control has a variable taken OUT of it"},
            {"text": "To repeat the experiment and check the result",
             "correct": False,
             "why": "That is a repeat, and it changes nothing about the "
                    "conditions"},
            {"text": "To remove exactly one thing, so that what happens tells "
                     "you whether that thing was needed",
             "correct": True},
            {"text": "To hold the spare nails",
             "correct": False,
             "why": "It is a full experiment of its own, with one thing "
                    "deliberately missing"},
        ],
        "figure": None,
    },

    # ── standard · MRB-335 top-up ───────────────────────────────────────
    {
        "id": "c5-03-s05",
        "band": "standard",
        "text": "Why is the water in one of the four tubes boiled before the "
                "nail goes in?",
        "options": [
            {"text": "To drive the dissolved air out of it",
             "correct": True},
            {"text": "To sterilise it, so that nothing living in the water "
                     "can take part in the reaction and confuse the result",
             "correct": False,
             "why": "Rusting is chemistry rather than biology. Boiling is "
                    "there to drive the dissolved air out"},
            {"text": "To make the reaction go faster",
             "correct": False,
             "why": "The tube is left to cool, and the point is to REMOVE "
                    "something rather than to speed anything up"},
            {"text": "To make the oil float on top",
             "correct": False,
             "why": "Oil floats on cold water just as well. The boiling does "
                    "a different job"},
        ],
        "figure": None,
    },
    {
        "id": "c5-03-s06",
        "band": "standard",
        "text": "Glucose reacts with oxygen in your cells to give carbon "
                "dioxide and water. Which type of reaction is that?",
        "options": [
            {"text": "Thermal decomposition, because the glucose is broken "
                     "down into two simpler substances by the warmth of the "
                     "body",
             "correct": False,
             "why": "Two reactants, one of them oxygen. A decomposition has "
                    "one reactant and needs no oxygen"},
            {"text": "An oxidation",
             "correct": True},
            {"text": "A displacement",
             "correct": False,
             "why": "There are no metals here and nothing takes another's "
                    "place"},
            {"text": "Nothing chemical — it happens inside a living thing",
             "correct": False,
             "why": "The same chemistry runs whether it is in a cell or a "
                    "crucible. Being alive changes nothing about the "
                    "reaction"},
        ],
        "figure": None,
    },
    {
        "id": "c5-03-s07",
        "band": "standard",
        "text": "A cut apple browns within minutes on the bench. What is "
                "happening?",
        "options": [
            {"text": "The apple is drying out, and the brown is what is left "
                     "behind once the water in the exposed surface has "
                     "evaporated away into the room",
             "correct": False,
             "why": "A drying apple goes wrinkled rather than brown, and it "
                    "browns in a sealed damp box too"},
            {"text": "Bacteria from the knife are growing on the surface",
             "correct": False,
             "why": "It happens far too fast for that, and a sterile knife "
                    "makes no difference"},
            {"text": "Substances in the flesh are being oxidised by the air",
             "correct": True},
            {"text": "The apple is rusting",
             "correct": False,
             "why": "Only iron and steel rust. This is an oxidation of "
                    "something else"},
        ],
        "figure": None,
    },
    {
        "id": "c5-03-s08",
        "band": "standard",
        "text": "Steel wool is burned on an open balance and the reading "
                "rises. Which type of reaction, and what joined?",
        "options": [
            {"text": "Thermal decomposition, and nothing joined — the rise is "
                     "the ash settling back onto the pan after being lifted "
                     "by the heat",
             "correct": False,
             "why": "Nothing is lifted or settled. Oxygen from the air has "
                    "joined the iron, and it has mass"},
            {"text": "A displacement, and the iron took the place of the "
                     "oxygen",
             "correct": False,
             "why": "Displacement needs a metal and another metal's compound. "
                    "There is none here"},
            {"text": "An oxidation, and the mass rose because the wool "
                     "expanded",
             "correct": False,
             "why": "A balance weighs mass rather than size. Expanding "
                    "changes nothing on the pan"},
            {"text": "An oxidation, and oxygen from the air joined the iron",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c5-03-s09",
        "band": "standard",
        "text": "One nail is painted and another is greased, and both are "
                "left outdoors. What do the two coatings have in common?",
        "options": [
            {"text": "Both keep oxygen and water off the iron",
             "correct": True},
            {"text": "Both corrode in preference to the iron underneath, "
                     "which is why each of them has to be renewed every few "
                     "years before the protection runs out",
             "correct": False,
             "why": "Neither corrodes at all — they are barriers. Corroding "
                    "instead is what a sacrificial metal does"},
            {"text": "Both make the iron less reactive",
             "correct": False,
             "why": "The iron is unchanged underneath. Scratch either coating "
                    "and it rusts at once"},
            {"text": "Both add oxygen to the surface in a form that will not "
                     "flake",
             "correct": False,
             "why": "That describes aluminium's own oxide layer. Paint and "
                    "grease add no oxygen"},
        ],
        "figure": None,
    },
    {
        "id": "c5-03-s10",
        "band": "standard",
        "text": "A nail is sealed in a tube of dry air with a drying agent, "
                "and left for four weeks. What happens?",
        "options": [
            {"text": "It rusts slowly, because the air in the tube supplies "
                     "the oxygen and rusting needs nothing else",
             "correct": False,
             "why": "Rusting needs water as well, and the drying agent has "
                    "removed it"},
            {"text": "It does not rust",
             "correct": True},
            {"text": "It rusts as fast as a nail in the open",
             "correct": False,
             "why": "Both would need water. Only one of the two tubes has "
                    "any"},
            {"text": "It corrodes but does not rust",
             "correct": False,
             "why": "Rusting IS the corrosion of iron. With no water, neither "
                    "happens"},
        ],
        "figure": None,
    },

    # ── harder · MRB-335 top-up ─────────────────────────────────────────
    {
        "id": "c5-03-h05",
        "band": "harder",
        "text": "Burning glucose in a crucible and respiring it in a cell "
                "give the same products. What is the difference?",
        "options": [
            {"text": "The products, because a cell keeps the carbon dioxide "
                     "and releases only the water, while a crucible releases "
                     "both of them into the room",
             "correct": False,
             "why": "A cell releases both. Breathe onto cold glass and onto "
                    "limewater and you can show it"},
            {"text": "The speed — released slowly at 37 °C, the energy can be "
                     "used instead of setting the cell on fire",
             "correct": True},
            {"text": "The reactants — a cell uses no oxygen",
             "correct": False,
             "why": "A cell uses oxygen, which is most of why you breathe"},
            {"text": "Nothing at all — they are the same reaction",
             "correct": False,
             "why": "The chemistry is the same and the RATE is not, and the "
                    "rate is what makes one useful and the other fatal"},
        ],
        "figure": None,
    },
    {
        "id": "c5-03-h06",
        "band": "harder",
        "text": "A ship's zinc blocks are nearly gone after three years. Is "
                "the system working or failing?",
        "options": [
            {"text": "Failing — a protective coating that has been eaten away "
                     "is a coating that was not up to the job it was fitted "
                     "to do",
             "correct": False,
             "why": "It is not a coating. Being eaten away IS the method "
                    "working"},
            {"text": "Failing, because zinc should not corrode at all",
             "correct": False,
             "why": "Zinc is more reactive than iron and corrodes readily. "
                    "That is why it was chosen"},
            {"text": "Working — the blocks corroding instead of the hull is "
                     "the whole point of them",
             "correct": True},
            {"text": "Neither can be said without inspecting the hull",
             "correct": False,
             "why": "Inspecting the hull is sensible practice, and the state "
                    "of the blocks already tells you the method has been "
                    "doing its work"},
        ],
        "figure": None,
    },
    {
        "id": "c5-03-h07",
        "band": "harder",
        "text": "A steel food can is coated in tin, which is LESS reactive "
                "than iron. What happens if the coating is scratched?",
        "options": [
            {"text": "The tin corrodes in preference to the iron, as zinc "
                     "does",
             "correct": False,
             "why": "Only a MORE reactive metal does that. Tin is less "
                    "reactive than iron"},
            {"text": "Nothing, because tin seals the scratch as it corrodes",
             "correct": False,
             "why": "That is aluminium's oxide layer. A tin coating with a "
                    "hole in it stays a hole"},
            {"text": "The iron is protected, because the tin is a barrier",
             "correct": False,
             "why": "It is a barrier until it is scratched. After that the "
                    "iron is exposed and nothing corrodes in its place"},
            {"text": "The iron rusts, and the tin does nothing to stop it",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c5-03-h08",
        "band": "harder",
        "text": "An oxidation makes the product heavier, yet a badly rusted "
                "gate weighs less than it did when new. How do both hold?",
        "options": [
            {"text": "The rust is heavier than the iron it came from, and "
                     "what the gate has lost is rust falling off it",
             "correct": True},
            {"text": "Rusting is the one oxidation that makes a product "
                     "lighter, because the rust holds water rather than "
                     "oxygen and water is lighter than iron",
             "correct": False,
             "why": "Rust holds both, and it is heavier than the iron. "
                    "Nothing about it is an exception"},
            {"text": "The gate has lost oxygen to the air over the years",
             "correct": False,
             "why": "It has GAINED oxygen. That is what makes it rust"},
            {"text": "A rusted gate does not weigh less — the observation is "
                     "mistaken",
             "correct": False,
             "why": "A gate really can end up lighter, because the flakes end "
                    "up on the ground"},
        ],
        "figure": None,
    },
    {
        "id": "c5-03-h09",
        "band": "harder",
        "text": "Why does the lesson insist that only iron and steel RUST, "
                "when copper and aluminium clearly corrode too?",
        "options": [
            {"text": "Because copper and aluminium corrode so slowly that "
                     "nobody has ever needed a separate word for what happens "
                     "to them over an ordinary lifetime",
             "correct": False,
             "why": "Aluminium oxidises within seconds of being cut. The "
                    "distinction is about naming, not speed"},
            {"text": "Because rust names one specific product, and corrosion "
                     "is the general word for all of them",
             "correct": True},
            {"text": "Because only iron reacts with oxygen",
             "correct": False,
             "why": "Almost every metal does. Iron's product has its own "
                    "name"},
            {"text": "Because rusting needs water and other corrosion does "
                     "not",
             "correct": False,
             "why": "A real difference, and not the reason for the word. "
                    "Rust is the name of hydrated iron oxide"},
        ],
        "figure": None,
    },
    {
        "id": "c5-03-h10",
        "band": "harder",
        "text": "Tube 3 has BOTH boiled water and a layer of oil on top. Why "
                "are two precautions needed for one variable?",
        "options": [
            {"text": "Because oil alone would slow the rusting down without "
                     "stopping it, and boiling alone would stop it entirely — "
                     "so together they make the result unambiguous",
             "correct": False,
             "why": "Neither alone removes the air properly. They do "
                    "different halves of one job"},
            {"text": "Because the oil would otherwise react with the water",
             "correct": False,
             "why": "Oil and water do not react. The oil is a seal"},
            {"text": "Boiling removes the air already dissolved; the oil "
                     "stops more dissolving in",
             "correct": True},
            {"text": "Because boiling also removes the salt",
             "correct": False,
             "why": "There is no salt in that tube, and boiling would "
                    "concentrate salt rather than remove it"},
        ],
        "figure": None,
    },
]
