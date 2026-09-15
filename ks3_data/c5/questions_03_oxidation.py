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
            {"text": "Rust forming on iron, and nothing else that happens to "
                     "any other metal",
             "correct": False,
             "why": "Rusting is one kind of corrosion. Aluminium and zinc "
                    "corrode too, and neither of them rusts"},
            {"text": "A metal being eaten away by reacting with its "
                     "surroundings",
             "correct": True},
            {"text": "A metal melting away in the heat and running out of the "
                     "shape it had",
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
            {"text": "Replacing the iron altogether with some other metal that "
                     "does not corrode at all in the air",
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
            {"text": "To repeat the experiment under exactly the same "
                     "conditions and check that the result comes out the same",
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
            {"text": "The reactants — a cell uses no oxygen at all, while "
                     "burning glucose in a crucible obviously does need some",
             "correct": False,
             "why": "A cell uses oxygen, which is most of why you breathe"},
            {"text": "Nothing at all — they are the very same reaction, with "
                     "the same reactants and the same products in both cases",
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
            {"text": "Failing, because zinc is a metal that should not have "
                     "been corroding at all in the first place",
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
            {"text": "A rusted gate does not actually weigh any less than it "
                     "did when it was brand new, so the observation is "
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
            {"text": "Because rusting needs water to be present, and none of "
                     "the other kinds of corrosion needs any of it at all",
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
            {"text": "Because the oil would otherwise react with the water "
                     "that is lying underneath it in the tube",
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

    # ── easier · MRB-338 night-3 top-up ─────────────────────────────────
    #
    # The existing thirty rows work the four tubes and the aluminium oxide
    # layer hard and leave the five stopping METHODS, the named products and
    # the non-metal oxidations almost untouched. These twenty take those, plus
    # the vocabulary the page glosses and never asks for.
    #
    # ⚠️ The ladder owns tube 3 on its own (apply), the case for tubes 2 and 3
    # (explain) and the sacrificial block on a boat (produce). Nothing below
    # reproduces any of those three tasks; the rows that touch the same
    # apparatus ask a different question of it — a shed, waterlogged clay, a
    # second variable, the amount of salt.
    {
        "id": "c5-03-e11",
        "band": "easier",
        "text": "What is made when a metal gains oxygen?",
        "options": [
            {"text": "A metal oxide",
             "correct": True},
            {"text": "A pure sample of the metal",
             "correct": False,
             "why": "The metal is no longer on its own. Oxygen has joined it"},
            {"text": "A mixture of the metal and some oxygen",
             "correct": False,
             "why": "A mixture can be separated without a reaction. Here the "
                    "two are chemically joined"},
            {"text": "A metal carbonate",
             "correct": False,
             "why": "A carbonate holds carbon as well. Only oxygen joined "
                    "here"},
        ],
        "figure": None,
    },
    {
        "id": "c5-03-e12",
        "band": "easier",
        "text": "Which substance forms when magnesium reacts with the oxygen "
                "in the air?",
        "options": [
            {"text": "Magnesium that has been bleached by the light",
             "correct": False,
             "why": "Light does not bleach a metal. The powder is a new "
                    "substance"},
            {"text": "Magnesium oxide",
             "correct": True},
            {"text": "Ash blown in from the burning air around it",
             "correct": False,
             "why": "Air does not burn and leaves no ash. The powder came from "
                    "the ribbon"},
            {"text": "Magnesium carbonate",
             "correct": False,
             "why": "No carbon joined anything. What joined the magnesium was "
                    "oxygen"},
        ],
        "figure": None,
    },
    {
        "id": "c5-03-e13",
        "band": "easier",
        "text": "What substance is rust?",
        "options": [
            {"text": "Iron that has been worn thin by the weather",
             "correct": False,
             "why": "Nothing is worn away. A new substance has been made and "
                    "it weighs more"},
            {"text": "Iron mixed with dirt",
             "correct": False,
             "why": "It is one compound rather than a mixture, and it forms on "
                    "clean iron"},
            {"text": "Hydrated iron oxide",
             "correct": True},
            {"text": "Iron that has dried out and gone brittle",
             "correct": False,
             "why": "Rusting needs water, so drying out is the opposite of "
                    "what happened"},
        ],
        "figure": None,
    },
    {
        "id": "c5-03-e14",
        "band": "easier",
        "text": "In the four-tube rusting experiment, the nails are identical. "
                "Why does that matter?",
        "options": [
            {"text": "So that the nails rust at the same time as each other",
             "correct": False,
             "why": "They are meant to behave differently. What must not "
                    "differ is the nail itself"},
            {"text": "So that four results can be added together at the end",
             "correct": False,
             "why": "The four are compared rather than added. They are "
                    "different conditions"},
            {"text": "So that they all fit into tubes of the same size",
             "correct": False,
             "why": "Fitting is convenience. The reason is about what is being "
                    "tested"},
            {"text": "So that the nail is not one of the things that differs "
                     "between the tubes",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c5-03-e15",
        "band": "easier",
        "text": "Which of these stops rusting by putting a barrier between the "
                "iron and the air?",
        "options": [
            {"text": "Painting a bridge",
             "correct": True},
            {"text": "Bolting blocks of zinc below a ship's waterline",
             "correct": False,
             "why": "The blocks cover nothing at all. They work by corroding "
                    "instead of the hull"},
            {"text": "Choosing a metal that is more reactive than iron",
             "correct": False,
             "why": "A more reactive metal corrodes in the iron's place rather "
                    "than shielding it"},
            {"text": "Keeping a spanner in a box with a drying agent",
             "correct": False,
             "why": "That removes the water rather than putting anything "
                    "between the iron and the air"},
        ],
        "figure": None,
    },
    {
        "id": "c5-03-e16",
        "band": "easier",
        "text": "What does galvanising a steel gate mean?",
        "options": [
            {"text": "Painting it with a special rust-resistant paint",
             "correct": False,
             "why": "No paint is involved. The coating is a metal"},
            {"text": "Dipping it in molten zinc to leave a zinc coat",
             "correct": True},
            {"text": "Heating it until a tough oxide layer forms on it",
             "correct": False,
             "why": "That is closer to what aluminium does for itself. "
                    "Galvanising adds a different metal"},
            {"text": "Mixing chromium and nickel into the steel",
             "correct": False,
             "why": "That makes stainless steel, which is a different method "
                    "altogether"},
        ],
        "figure": None,
    },
    {
        "id": "c5-03-e17",
        "band": "easier",
        "text": "Why does a bicycle chain have to be oiled again every few "
                "weeks?",
        "options": [
            {"text": "Because oil turns into rust if it is left on too long",
             "correct": False,
             "why": "Oil does not become rust. It simply stops being there"},
            {"text": "Because a fresh layer corrodes in place of the chain",
             "correct": False,
             "why": "Oil does not corrode at all. It is a barrier and nothing "
                    "more"},
            {"text": "Because the oil wears off",
             "correct": True},
            {"text": "Because oil blocks water only",
             "correct": False,
             "why": "It keeps both water and air out while it is there. The "
                    "trouble is that it does not stay there"},
        ],
        "figure": None,
    },
    {
        "id": "c5-03-e18",
        "band": "easier",
        "text": "Stainless steel is iron mixed with two other metals. Which "
                "two?",
        "options": [
            {"text": "Zinc and tin",
             "correct": False,
             "why": "Zinc is used for galvanising and tin for lining cans. "
                    "Neither goes into stainless steel"},
            {"text": "Copper and aluminium",
             "correct": False,
             "why": "Neither of those is in stainless steel, though both "
                    "corrode in their own way"},
            {"text": "Lead and silver",
             "correct": False,
             "why": "Neither is used, and cutlery made of lead would be a very "
                    "poor idea"},
            {"text": "Chromium and nickel",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c5-03-e19",
        "band": "easier",
        "text": "How does aluminium's reactivity compare with iron's?",
        "options": [
            {"text": "Aluminium is the more reactive of the two",
             "correct": True},
            {"text": "Aluminium is the less reactive of the two",
             "correct": False,
             "why": "It is more reactive, which is why the oxide layer it "
                    "grows is such a surprise"},
            {"text": "They are equally reactive, and only the oxide differs",
             "correct": False,
             "why": "The oxide is what differs in behaviour, and the metals "
                    "are not equally reactive"},
            {"text": "Aluminium is unreactive, which is why it lasts outdoors",
             "correct": False,
             "why": "It is one of the more reactive metals you meet, and it "
                    "oxidises the moment it is cut"},
        ],
        "figure": None,
    },
    {
        "id": "c5-03-e20",
        "band": "easier",
        "text": "Which word equation describes rusting?",
        "options": [
            {"text": "iron + water makes hydrated iron oxide",
             "correct": False,
             "why": "Water on its own does not do it, as the boiled-water tube "
                    "shows"},
            {"text": "iron + oxygen + water makes hydrated iron oxide",
             "correct": True},
            {"text": "iron + oxygen makes hydrated iron oxide",
             "correct": False,
             "why": "Oxygen on its own does not do it either, as the dry-air "
                    "tube shows"},
            {"text": "iron + salt + water makes hydrated iron oxide",
             "correct": False,
             "why": "Salt is not needed at all. A nail in plain tap water "
                    "rusts perfectly well"},
        ],
        "figure": None,
    },
    {
        "id": "c5-03-e21",
        "band": "easier",
        "text": "Which of these speeds rusting up without being needed for it "
                "to happen?",
        "options": [
            {"text": "Oxygen",
             "correct": False,
             "why": "Oxygen is one of the two things rusting cannot happen "
                    "without"},
            {"text": "Water",
             "correct": False,
             "why": "Water is the other requirement. Take it away and no rust "
                    "forms"},
            {"text": "Salt",
             "correct": True},
            {"text": "Iron",
             "correct": False,
             "why": "The iron is the thing that rusts, so it is hardly an "
                    "extra"},
        ],
        "figure": None,
    },
    {
        "id": "c5-03-e22",
        "band": "easier",
        "text": "An apple is cut in half and left on the bench. What happens "
                "to the cut surface?",
        "options": [
            {"text": "It stays exactly as it was, because fruit does not react "
                     "with air",
             "correct": False,
             "why": "It browns within minutes, which is a reaction with the "
                    "air"},
            {"text": "It rusts, in the way an iron nail does",
             "correct": False,
             "why": "Rusting is what happens to iron and steel. This is an "
                    "oxidation of something else"},
            {"text": "It goes green, because the skin colour spreads inwards",
             "correct": False,
             "why": "No colour moves in from the skin. The flesh itself "
                    "changes"},
            {"text": "It browns, as substances in the flesh are oxidised",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c5-03-e23",
        "band": "easier",
        "text": "What does the word antioxidant mean on a food label?",
        "options": [
            {"text": "Something that is oxidised in the food's place",
             "correct": True},
            {"text": "Something that stops oxygen existing in the packet",
             "correct": False,
             "why": "Nothing removes oxygen from the world. The additive "
                    "reacts with it first"},
            {"text": "Something that makes the food heavier so it lasts longer",
             "correct": False,
             "why": "Mass has nothing to do with keeping. The additive reacts "
                    "in the food's place"},
            {"text": "Something that kills the bacteria growing on the food",
             "correct": False,
             "why": "That is a preservative of a different kind. Browning is "
                    "chemistry rather than biology"},
        ],
        "figure": None,
    },
    {
        "id": "c5-03-e24",
        "band": "easier",
        "text": "Which process inside your cells uses glucose and oxygen and "
                "releases energy?",
        "options": [
            {"text": "Digestion",
             "correct": False,
             "why": "Digestion breaks food down before it reaches a cell. It "
                    "uses no oxygen"},
            {"text": "Respiration",
             "correct": True},
            {"text": "Combustion",
             "correct": False,
             "why": "The chemistry is the same and there is no flame. Cells do "
                    "it far more slowly"},
            {"text": "Decomposition",
             "correct": False,
             "why": "A decomposition has one reactant. Here glucose and oxygen "
                    "are both used"},
        ],
        "figure": None,
    },
    {
        "id": "c5-03-e25",
        "band": "easier",
        "text": "Of the four rusting tubes, which nail rusted the most?",
        "options": [
            {"text": "The one in dry air with a drying agent",
             "correct": False,
             "why": "That nail did not rust at all. It stayed as shiny as the "
                    "day it went in"},
            {"text": "The one in boiled water under a layer of oil",
             "correct": False,
             "why": "That one showed no rust, or the faintest trace where the "
                    "oil did not quite seal"},
            {"text": "The one in salt water open to the air",
             "correct": True},
            {"text": "The one in plain tap water open to the air",
             "correct": False,
             "why": "That one rusted, and the salted tube was worse in the "
                    "same four weeks"},
        ],
        "figure": None,
    },
    {
        "id": "c5-03-e26",
        "band": "easier",
        "text": "What is a drying agent put into a tube for?",
        "options": [
            {"text": "To soak up any rust as soon as it forms on the nail",
             "correct": False,
             "why": "It does nothing to the rust. It acts on the air before "
                    "any rust can form"},
            {"text": "To keep the nail warm so the reaction can run faster",
             "correct": False,
             "why": "It changes no temperature. What it changes is how much "
                    "water is present"},
            {"text": "To stop the bung falling out of the top",
             "correct": False,
             "why": "It has no mechanical job at all"},
            {"text": "To take the moisture out of the air in the tube",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c5-03-e27",
        "band": "easier",
        "text": "What colour is rust?",
        "options": [
            {"text": "Orange",
             "correct": True},
            {"text": "Black",
             "correct": False,
             "why": "Black is the colour of copper oxide, which is a different "
                    "metal's oxide"},
            {"text": "White",
             "correct": False,
             "why": "White is magnesium oxide. Iron's oxide is orange"},
            {"text": "Green",
             "correct": False,
             "why": "Green is copper carbonate. Rust on a gate is orange"},
        ],
        "figure": None,
    },
    {
        "id": "c5-03-e28",
        "band": "easier",
        "text": "A nail is weighed, left to rust completely, and every flake "
                "is collected and weighed. Which is heavier?",
        "options": [
            {"text": "The nail",
             "correct": False,
             "why": "Nothing is eaten away into nothing. Oxygen and water have "
                    "joined the iron, and both of them have mass"},
            {"text": "The rust",
             "correct": True},
            {"text": "They weigh the same",
             "correct": False,
             "why": "The iron is all still there, and something has been added "
                    "to it as well"},
            {"text": "It depends how long it was left",
             "correct": False,
             "why": "Longer leaves more rust, and rust is the heavier of the "
                    "two whenever you stop"},
        ],
        "figure": None,
    },
    {
        "id": "c5-03-e29",
        "band": "easier",
        "text": "Which metal is used for the sacrificial blocks bolted to a "
                "steel ship?",
        "options": [
            {"text": "Copper",
             "correct": False,
             "why": "Copper is less reactive than iron, so the steel would "
                    "corrode instead"},
            {"text": "Tin",
             "correct": False,
             "why": "Tin is also less reactive than iron. It is used to line "
                    "cans, as a barrier"},
            {"text": "Zinc",
             "correct": True},
            {"text": "Chromium",
             "correct": False,
             "why": "Chromium goes into stainless steel, where it makes its "
                    "own oxide layer"},
        ],
        "figure": None,
    },
    {
        "id": "c5-03-e30",
        "band": "easier",
        "text": "A bright cut is made in a block of aluminium and within "
                "moments it looks dull. Why?",
        "options": [
            {"text": "The cut surface has cooled down from the heat of the saw",
             "correct": False,
             "why": "Cooling does not change how a metal looks. A reaction "
                    "does"},
            {"text": "Dust from the room has settled on it",
             "correct": False,
             "why": "It happens in a clean room too, and far faster than dust "
                    "could settle"},
            {"text": "The cut surface has been smoothed over by the blade",
             "correct": False,
             "why": "A smoothed surface would look brighter rather than "
                    "duller"},
            {"text": "It has oxidised in the air straight away",
             "correct": True},
        ],
        "figure": None,
    },

    # ── standard · MRB-338 night-3 top-up ───────────────────────────────
    {
        "id": "c5-03-s11",
        "band": "standard",
        "text": "Why does a small chip in the paint on a steel bridge matter "
                "so much?",
        "options": [
            {"text": "Rust starts at the chip and then spreads underneath the "
                     "paint",
             "correct": True},
            {"text": "The chip lets the paint peel off the whole bridge at "
                     "once",
             "correct": False,
             "why": "Paint does not fall off in one piece. What spreads is the "
                    "rusting underneath it"},
            {"text": "The exposed steel becomes more reactive than the steel "
                     "under the paint",
             "correct": False,
             "why": "It is the same steel. What has changed is that air and "
                    "water can now reach it"},
            {"text": "The chip lets the paint react with the steel beneath it",
             "correct": False,
             "why": "Paint does not react with steel. It keeps the air and "
                    "water off"},
        ],
        "figure": None,
    },
    {
        "id": "c5-03-s12",
        "band": "standard",
        "text": "Oiling a chain is described as a deliberately temporary "
                "barrier. What makes it temporary?",
        "options": [
            {"text": "It is used up by the rusting reaction as it works",
             "correct": False,
             "why": "It takes no part in the reaction. It is worn away "
                    "mechanically"},
            {"text": "It wears off in use and has to be put back on",
             "correct": True},
            {"text": "It dries out and turns into a powder on the metal",
             "correct": False,
             "why": "Oil does not dry to powder. It is rubbed and washed away"},
            {"text": "It corrodes in place of the chain until there is none "
                     "left",
             "correct": False,
             "why": "Corroding in the metal's place is what a sacrificial "
                    "metal does. Oil is a barrier"},
        ],
        "figure": None,
    },
    {
        "id": "c5-03-s13",
        "band": "standard",
        "text": "0.24 g of magnesium ribbon is burned and leaves 0.40 g of "
                "white powder. What mass of oxygen joined the magnesium?",
        "options": [
            {"text": "0.40 g",
             "correct": False,
             "why": "That is the whole of the powder, and most of it is the "
                    "magnesium that was already there"},
            {"text": "0.64 g",
             "correct": False,
             "why": "That adds the two figures. The 0.24 g is part of the "
                    "0.40 g rather than extra to it"},
            {"text": "0.16 g",
             "correct": True},
            {"text": "0.24 g",
             "correct": False,
             "why": "That is the magnesium you started with, which did not "
                    "join anything from outside"},
        ],
        "figure": None,
    },
    {
        "id": "c5-03-s14",
        "band": "standard",
        "text": "A nail is put in a tube filled to the brim with ordinary tap "
                "water and bunged, with no air space above it. Predict what "
                "happens over four weeks.",
        "options": [
            {"text": "No rust at all, because there is no air in the tube",
             "correct": False,
             "why": "Ordinary tap water has air dissolved in it, which is why "
                    "the other tube's water is boiled first"},
            {"text": "Heavy rusting, because the nail is completely "
                     "surrounded by water",
             "correct": False,
             "why": "Being surrounded by water supplies only one of the two "
                    "requirements"},
            {"text": "No rust, because rusting needs the nail to be half in "
                     "and half out",
             "correct": False,
             "why": "The water line is where rusting is worst rather than "
                    "where it is possible"},
            {"text": "Some rusting, because unboiled tap water still holds "
                     "dissolved air",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c5-03-s15",
        "band": "standard",
        "text": "A nail standing half in tap water rusts worst at the level "
                "where the water surface meets it. Why there?",
        "options": [
            {"text": "Because that is where the nail meets air and water "
                     "together",
             "correct": True},
            {"text": "Because the water is warmest at its surface",
             "correct": False,
             "why": "The tube is all one temperature, and warmth is not what "
                    "decides where rust forms"},
            {"text": "Because the surface of the water presses hardest on the "
                     "nail there",
             "correct": False,
             "why": "Pressure is greatest at the bottom, and it has nothing to "
                    "do with rusting"},
            {"text": "Because rust floats, so it collects at the top of the "
                     "water",
             "correct": False,
             "why": "Rust clings to the nail and then flakes downwards. It "
                    "does not gather at the surface"},
        ],
        "figure": None,
    },
    {
        "id": "c5-03-s16",
        "band": "standard",
        "text": "One gate is painted and another is galvanised, and neither "
                "is ever scratched. Is there any difference in how they are "
                "protected?",
        "options": [
            {"text": "Yes — the zinc corrodes in the iron's place even where "
                     "the coat is whole",
             "correct": False,
             "why": "While the coat is whole nothing reaches the iron, so "
                    "there is nothing for the zinc to do"},
            {"text": "No — while both coats are unbroken each is simply a "
                     "barrier",
             "correct": True},
            {"text": "Yes — paint is a barrier and zinc is not a barrier at "
                     "all",
             "correct": False,
             "why": "The zinc coat is a barrier as well. Its second trick only "
                    "matters once it is broken"},
            {"text": "No — neither is a barrier, because both are far too thin "
                     "to keep water out",
             "correct": False,
             "why": "A thin unbroken layer keeps water out perfectly well, "
                    "which is why paint works at all"},
        ],
        "figure": None,
    },
    {
        "id": "c5-03-s17",
        "band": "standard",
        "text": "A ship's hull is painted AND fitted with zinc blocks. Why use "
                "two methods rather than one?",
        "options": [
            {"text": "The paint keeps the water out and the zinc keeps the "
                     "paint on",
             "correct": False,
             "why": "The zinc does nothing to hold paint down. It protects the "
                    "metal, not the coating"},
            {"text": "Two barriers keep water out twice as well as one barrier "
                     "does",
             "correct": False,
             "why": "The blocks are not a barrier. They cover nothing at all"},
            {"text": "The paint keeps air and water off, and the zinc protects "
                     "wherever the paint is damaged",
             "correct": True},
            {"text": "The paint works in fresh water and the zinc works in salt "
                     "water",
             "correct": False,
             "why": "Both work in either. Salt speeds corrosion up without "
                    "changing which method does what"},
        ],
        "figure": None,
    },
    {
        "id": "c5-03-s18",
        "band": "standard",
        "text": "A steel spade left out all winter is rusted; the same spade "
                "kept in a dry shed is not. Which of the four tubes does the "
                "shed match?",
        "options": [
            {"text": "The salt-water tube, because grit gets everywhere",
             "correct": False,
             "why": "There is no salt in a shed, and the shed is the tube "
                    "where something has been REMOVED"},
            {"text": "The tap-water tube, because a shed still has damp air in "
                     "it",
             "correct": False,
             "why": "A dry shed is the one where the water is missing, which "
                    "is why the spade survives"},
            {"text": "The boiled-water tube, because the air has been driven "
                     "out of the shed",
             "correct": False,
             "why": "A shed is full of air. What it is short of is water"},
            {"text": "The dry-air tube, because the air is there and the water "
                     "is not",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c5-03-s19",
        "band": "standard",
        "text": "Why is the rusting investigation left for four weeks rather "
                "than being read at the end of the lesson?",
        "options": [
            {"text": "Because rusting is slow, and nothing would be visible in "
                     "an hour",
             "correct": True},
            {"text": "Because the oxygen has to dissolve into the water before "
                     "it can act",
             "correct": False,
             "why": "There is dissolved air in the tap water from the start. "
                    "The reaction itself is what takes time"},
            {"text": "Because the nails have to cool down to room temperature "
                     "first",
             "correct": False,
             "why": "The nails are at room temperature the whole time"},
            {"text": "Because the drying agent takes several weeks to remove "
                     "the moisture",
             "correct": False,
             "why": "It dries the air quickly. The wait is for the rusting in "
                    "the other tubes"},
        ],
        "figure": None,
    },
    {
        "id": "c5-03-s20",
        "band": "standard",
        "text": "A student predicts that every tube will rust, because every "
                "tube holds an iron nail. What have they missed?",
        "options": [
            {"text": "That iron does not always rust, depending on where it "
                     "was made",
             "correct": False,
             "why": "All four nails are identical. Where iron comes from does "
                    "not change its chemistry"},
            {"text": "That the nail is the same in all four, and what "
                     "surrounds it is not",
             "correct": True},
            {"text": "That rusting needs the nail to be scratched before it "
                     "can start",
             "correct": False,
             "why": "A smooth clean nail rusts perfectly well given air and "
                    "water"},
            {"text": "That four weeks is not long enough for every tube to "
                     "show a result",
             "correct": False,
             "why": "Two of the tubes give their result by showing nothing, "
                    "and that is the result"},
        ],
        "figure": None,
    },
    {
        "id": "c5-03-s21",
        "band": "standard",
        "text": "A cut apple browns within minutes but a whole apple in the "
                "same bowl does not. Why?",
        "options": [
            {"text": "The skin of a whole apple contains an antioxidant that "
                     "the flesh lacks",
             "correct": False,
             "why": "The skin keeps the air off rather than carrying a "
                    "chemical that stops the reaction"},
            {"text": "A whole apple is colder inside, so nothing can react in "
                     "there",
             "correct": False,
             "why": "Both are at room temperature, and temperature is not what "
                    "is missing"},
            {"text": "The flesh has to be exposed to the air before it can be "
                     "oxidised",
             "correct": True},
            {"text": "Cutting the apple heats the surface enough to start the "
                     "reaction",
             "correct": False,
             "why": "A knife warms nothing measurably. What it does is open "
                    "the flesh to the air"},
        ],
        "figure": None,
    },
    {
        "id": "c5-03-s22",
        "band": "standard",
        "text": "Cling film pressed onto the cut face of an apple slows the "
                "browning. Which of the anti-rusting methods is that most "
                "like?",
        "options": [
            {"text": "A sacrificial block, because the film is used up "
                     "instead of the apple",
             "correct": False,
             "why": "The film is unchanged when you peel it off. Nothing has "
                    "been used up"},
            {"text": "A drying agent, because the film takes the water out of "
                     "the apple",
             "correct": False,
             "why": "It keeps the apple's own moisture in. What it excludes is "
                    "the air"},
            {"text": "Stainless steel, because the film makes an oxide layer "
                     "on the surface",
             "correct": False,
             "why": "No oxide forms. The film is not part of the apple at all"},
            {"text": "Painting a bridge, because both are barriers that keep "
                     "the air off",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c5-03-s23",
        "band": "standard",
        "text": "Damp steel wool is sealed in a jar of air. After a week the "
                "wool is rusty and the air in the jar has shrunk slightly. "
                "Explain.",
        "options": [
            {"text": "The iron has taken oxygen out of the air, so less gas is "
                     "left",
             "correct": True},
            {"text": "The rust has soaked up the air the way a sponge soaks up "
                     "water",
             "correct": False,
             "why": "Rust does not absorb gas. Oxygen has become part of a new "
                    "compound"},
            {"text": "The damp has cooled the jar, so the air inside has "
                     "contracted",
             "correct": False,
             "why": "The jar is at room temperature throughout. A reaction has "
                    "used gas up"},
            {"text": "Some of the air has leaked out past the lid as the wool "
                     "rusted",
             "correct": False,
             "why": "A sealed jar keeps its gas. What left the air was the "
                    "oxygen, into the rust"},
        ],
        "figure": None,
    },
    {
        "id": "c5-03-s24",
        "band": "standard",
        "text": "Which of these ways of stopping rust goes on protecting the "
                "iron after the coating has been scratched through?",
        "options": [
            {"text": "Painting",
             "correct": False,
             "why": "A chip in paint is exactly where rusting starts, and it "
                    "spreads underneath"},
            {"text": "Galvanising",
             "correct": True},
            {"text": "Oiling",
             "correct": False,
             "why": "Oil is a barrier and nothing more. Wipe a line through it "
                    "and the iron is exposed"},
            {"text": "Tin-plating a food can",
             "correct": False,
             "why": "Tin is less reactive than iron, so a scratch leaves the "
                    "iron on its own"},
        ],
        "figure": None,
    },
    {
        "id": "c5-03-s25",
        "band": "standard",
        "text": "A boat owner paints over the zinc blocks on the hull, hoping "
                "to make them last longer. Why is that a mistake?",
        "options": [
            {"text": "The paint would react with the zinc and eat it away "
                     "faster",
             "correct": False,
             "why": "Paint does not react with zinc. The problem is that it "
                    "stops the zinc working"},
            {"text": "The blocks would rust under the paint instead of "
                     "corroding",
             "correct": False,
             "why": "Zinc does not rust, since rusting is what happens to "
                    "iron. The trouble is that it is sealed off"},
            {"text": "The blocks have to be in contact with the sea water to "
                     "corrode in the hull's place",
             "correct": True},
            {"text": "The paint would make the blocks less reactive than the "
                     "steel underneath",
             "correct": False,
             "why": "A coat of paint does not change how reactive a metal is"},
        ],
        "figure": None,
    },
    {
        "id": "c5-03-s26",
        "band": "standard",
        "text": "Which word equation describes magnesium burning in air?",
        "options": [
            {"text": "magnesium + air makes magnesium oxide",
             "correct": False,
             "why": "It is the oxygen in the air that reacts. Air is a mixture "
                    "and most of it takes no part"},
            {"text": "magnesium oxide makes magnesium + oxygen",
             "correct": False,
             "why": "That runs the reaction backwards. Magnesium is the "
                    "reactant here"},
            {"text": "magnesium + oxygen + water makes magnesium oxide",
             "correct": False,
             "why": "No water is needed. Water is a reactant for rusting and "
                    "not for burning a metal"},
            {"text": "magnesium + oxygen makes magnesium oxide",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c5-03-s27",
        "band": "standard",
        "text": "A nail is put into boiled water with NO layer of oil on top "
                "and left open to the room. Predict the result over four "
                "weeks.",
        "options": [
            {"text": "It rusts, because air redissolves into the water from "
                     "above",
             "correct": True},
            {"text": "It does not rust, because boiling removed the air once "
                     "and for all",
             "correct": False,
             "why": "Boiling drives air out at the time. Left open, the water "
                    "takes it up again"},
            {"text": "It does not rust, because boiled water has been changed "
                     "into a different substance",
             "correct": False,
             "why": "Boiling makes no new substance. The water is the same "
                    "water"},
            {"text": "It rusts faster than the salt-water tube, because "
                     "boiling makes water more reactive",
             "correct": False,
             "why": "Boiling does not make water more reactive, and the salted "
                    "tube was the worst of the four"},
        ],
        "figure": None,
    },
    {
        "id": "c5-03-s28",
        "band": "standard",
        "text": "Which pair of tubes shows most fairly that salt speeds "
                "rusting up?",
        "options": [
            {"text": "The dry-air tube against the salt-water tube",
             "correct": False,
             "why": "Two things differ between those, so nothing can be put "
                    "down to the salt alone"},
            {"text": "The tap-water tube against the salt-water tube",
             "correct": True},
            {"text": "The boiled-water tube against the salt-water tube",
             "correct": False,
             "why": "Those differ in air as well as in salt, so the comparison "
                    "proves nothing about salt"},
            {"text": "The dry-air tube against the boiled-water tube",
             "correct": False,
             "why": "Neither of those holds any salt, so the pair says nothing "
                    "about it"},
        ],
        "figure": None,
    },
    {
        "id": "c5-03-s29",
        "band": "standard",
        "text": "New cars are undersealed along the floor and wheel arches "
                "rather than only being painted on top. Why there?",
        "options": [
            {"text": "Because the underside is a more reactive metal",
             "correct": False,
             "why": "It is the same steel throughout. What differs is what "
                    "reaches it"},
            {"text": "Because paint cannot be made to stick to the underside "
                     "of a car at all",
             "correct": False,
             "why": "Paint sticks perfectly well underneath. The underside "
                    "simply needs more protection"},
            {"text": "Because water and road salt sit there longest",
             "correct": True},
            {"text": "Because the underside gets hottest, and heat is what "
                     "drives rusting",
             "correct": False,
             "why": "Rusting happens at any ordinary temperature, and heat is "
                    "not one of its requirements"},
        ],
        "figure": None,
    },
    {
        "id": "c5-03-s30",
        "band": "standard",
        "text": "Why is oxidation described as the widest of the four "
                "reaction types?",
        "options": [
            {"text": "Because it can happen to a bigger piece of material than "
                     "the others can",
             "correct": False,
             "why": "Size has nothing to do with it. What is wide is the range "
                    "of reactions it covers"},
            {"text": "Because it is the only one of the four that happens "
                     "outside a laboratory",
             "correct": False,
             "why": "A barbecue and a cake are both outside a laboratory, and "
                    "neither is an oxidation of that kind"},
            {"text": "Because it takes the longest time of the four to happen",
             "correct": False,
             "why": "Burning magnesium takes two seconds and is an oxidation. "
                    "Speed is not the measure"},
            {"text": "Because burning, rusting, browning and respiration are "
                     "all oxidations",
             "correct": True},
        ],
        "figure": None,
    },

    # ── harder · MRB-338 night-3 top-up ─────────────────────────────────
    {
        "id": "c5-03-h11",
        "band": "harder",
        "text": "An 8.0 g nail is left until it has rusted right through, and "
                "every flake is collected. The flakes weigh 11.4 g. Where did "
                "the extra 3.4 g come from?",
        "options": [
            {"text": "From the oxygen and water that are now part of the rust",
             "correct": True},
            {"text": "From dirt and grit that stuck to the flakes as they fell",
             "correct": False,
             "why": "Dirt would be an error in the measurement rather than the "
                    "chemistry. The gain is real"},
            {"text": "From the iron expanding as it turned into rust",
             "correct": False,
             "why": "Rust does take up more room, and a balance weighs mass "
                    "rather than volume"},
            {"text": "From the water that was clinging to the flakes when they "
                     "were weighed",
             "correct": False,
             "why": "Dry the flakes and the gain is still there, because the "
                    "water is chemically part of the rust"},
        ],
        "figure": None,
    },
    {
        "id": "c5-03-h12",
        "band": "harder",
        "text": "A student writes that aluminium does not corrode. Rewrite the "
                "claim so that it is true.",
        "options": [
            {"text": "Aluminium corrodes only where it has been scratched "
                     "through its coating",
             "correct": False,
             "why": "A fresh scratch oxidises at once and seals itself. There "
                    "is no lasting bare surface"},
            {"text": "Aluminium corrodes at once, and the oxide it makes "
                     "protects the metal beneath",
             "correct": True},
            {"text": "Aluminium corrodes far more slowly than iron because it "
                     "is less reactive",
             "correct": False,
             "why": "It is MORE reactive than iron. The difference is in the "
                    "oxide, not in the reactivity"},
            {"text": "Aluminium corrodes only in sea air, which is why window "
                     "frames last inland",
             "correct": False,
             "why": "It oxidises the instant it meets ordinary air, anywhere "
                    "at all"},
        ],
        "figure": None,
    },
    {
        "id": "c5-03-h13",
        "band": "harder",
        "text": "A steel hull and a bronze propeller are bolted together in "
                "sea water. Bronze is mostly copper, which is less reactive "
                "than iron. Which corrodes faster?",
        "options": [
            {"text": "The propeller, because a moving part always wears away "
                     "before a still one",
             "correct": False,
             "why": "Wear is a physical matter. The question is which metal "
                    "corrodes, and reactivity decides that"},
            {"text": "Neither, because two different metals in contact protect "
                     "each other",
             "correct": False,
             "why": "One protects the other, and the protection runs one way. "
                    "The more reactive one is the one that goes"},
            {"text": "The hull, because steel is the more reactive of the two",
             "correct": True},
            {"text": "The propeller, because bronze is a mixture and mixtures "
                     "corrode first",
             "correct": False,
             "why": "Stainless steel is a mixture and resists corrosion. Being "
                    "a mixture settles nothing"},
        ],
        "figure": None,
    },
    {
        "id": "c5-03-h14",
        "band": "harder",
        "text": "Somebody proposes bolting blocks of COPPER to a steel hull "
                "instead of zinc. What would happen?",
        "options": [
            {"text": "The copper would corrode in the steel's place, exactly "
                     "as the zinc did",
             "correct": False,
             "why": "Only a metal MORE reactive than iron does that, and "
                    "copper is less reactive"},
            {"text": "Nothing would change, because any metal bolted on "
                     "protects the one it is bolted to",
             "correct": False,
             "why": "Which metal is protected depends entirely on which is the "
                    "more reactive"},
            {"text": "The copper would form an oxide layer over the whole hull "
                     "and seal it",
             "correct": False,
             "why": "A block seals nothing. It is not a coating and it covers "
                    "no part of the hull"},
            {"text": "The steel would go on corroding, because copper is less "
                     "reactive than iron",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c5-03-h15",
        "band": "harder",
        "text": "All four rusting tubes are stood in the same cupboard for the "
                "four weeks. Why does that matter?",
        "options": [
            {"text": "Otherwise temperature would be a second thing differing "
                     "between them",
             "correct": True},
            {"text": "Otherwise the tubes would have to be opened to compare "
                     "them fairly",
             "correct": False,
             "why": "Where they stand has nothing to do with opening them. It "
                    "keeps a variable fixed"},
            {"text": "Otherwise the light would reach some of the nails and "
                     "not the others",
             "correct": False,
             "why": "Light is not one of the requirements for rusting. "
                    "Temperature is the one being held steady"},
            {"text": "Otherwise the salt in one tube could reach the nails in "
                     "the others",
             "correct": False,
             "why": "Every tube is sealed or separate. Nothing crosses between "
                    "them"},
        ],
        "figure": None,
    },
    {
        "id": "c5-03-h16",
        "band": "harder",
        "text": "Salt speeds rusting up. Describe a fair test to find whether "
                "MORE salt speeds it up further.",
        "options": [
            {"text": "Use one tube of salt water and one of plain water, and "
                     "compare them after four weeks",
             "correct": False,
             "why": "That is the test already done. It compares salt with no "
                    "salt rather than two amounts of salt"},
            {"text": "Use identical nails and volumes of water open to the "
                     "air, with only the amount of salt different",
             "correct": True},
            {"text": "Use the same amount of salt in every tube and change how "
                     "long each one is left",
             "correct": False,
             "why": "That measures time rather than the amount of salt, which "
                    "is what the question asks about"},
            {"text": "Use one tube of very salty water and leave it far longer "
                     "than the others",
             "correct": False,
             "why": "Two things differ at once, so nothing could be put down "
                    "to the salt"},
        ],
        "figure": None,
    },
    {
        "id": "c5-03-h17",
        "band": "harder",
        "text": "An iron nail dug out of waterlogged clay is found almost "
                "unrusted after a hundred years. Explain.",
        "options": [
            {"text": "Clay is slightly acidic, and acid stops iron reacting "
                     "with oxygen",
             "correct": False,
             "why": "Acid speeds corrosion up rather than stopping it, and "
                    "acidity is not what preserved this nail"},
            {"text": "A hundred years is not long enough for rusting to become "
                     "visible",
             "correct": False,
             "why": "A nail in tap water shows orange within weeks. A century "
                    "is very long indeed"},
            {"text": "Waterlogged clay holds almost no air, so one requirement "
                     "was missing",
             "correct": True},
            {"text": "Water surrounding a nail completely stops rust forming "
                     "on it",
             "correct": False,
             "why": "Water is one of the two things rusting needs. It is the "
                    "absent air that preserved this one"},
        ],
        "figure": None,
    },
    {
        "id": "c5-03-h18",
        "band": "harder",
        "text": "Most word equations you meet have two reactants. Why does the "
                "rusting one have three?",
        "options": [
            {"text": "Because the salt has to be written in as well as the air "
                     "and the water",
             "correct": False,
             "why": "Salt is not a reactant at all. It only changes the speed"},
            {"text": "Because rust is a mixture of three separate substances "
                     "rather than one",
             "correct": False,
             "why": "Rust is one compound. Three reactants can still give a "
                    "single product"},
            {"text": "Because iron rusts in two steps, and the equation shows "
                     "both of them at once",
             "correct": False,
             "why": "The equation shows one reaction. What makes it unusual is "
                    "how many things go into it"},
            {"text": "Because the iron needs oxygen AND water together before "
                     "it will react",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c5-03-h19",
        "band": "harder",
        "text": "A steel bridge is repainted every few years; a stainless "
                "steel sculpture is never coated at all. Compare the two kinds "
                "of protection.",
        "options": [
            {"text": "The paint is added and wears away, while the stainless "
                     "steel makes its own layer and remakes it if it is damaged",
             "correct": True},
            {"text": "Both are barriers put on from outside, and the "
                     "sculpture's was simply applied more thickly",
             "correct": False,
             "why": "Nothing was applied to the sculpture. The chromium in it "
                    "oxidises to make the layer"},
            {"text": "The paint is a barrier, and the stainless steel is "
                     "protected sacrificially instead",
             "correct": False,
             "why": "Nothing is sacrificed. The chromium's oxide seals the "
                    "surface, which is a barrier"},
            {"text": "The paint stops water and the stainless steel stops air, "
                     "so between them both requirements are covered",
             "correct": False,
             "why": "Each of them keeps both out. They are not a division of "
                    "labour"},
        ],
        "figure": None,
    },
    {
        "id": "c5-03-h20",
        "band": "harder",
        "text": "Respiration and burning turn the same reactants into the same "
                "products. What would happen to a cell if its reaction ran at "
                "the speed of burning?",
        "options": [
            {"text": "Nothing would change, because the products would be "
                     "exactly the same either way",
             "correct": False,
             "why": "The products are the same and the rate is not, and the "
                    "rate is what a cell can survive"},
            {"text": "The energy would arrive far too fast for the cell to "
                     "use, and would destroy it",
             "correct": True},
            {"text": "The cell would make more carbon dioxide than it does "
                     "now, from the same glucose",
             "correct": False,
             "why": "The same glucose gives the same carbon dioxide however "
                    "fast it goes"},
            {"text": "The reaction would stop, because a cell holds too little "
                     "glucose to sustain a flame",
             "correct": False,
             "why": "The problem is not that it would stop. It is what "
                    "releasing that energy at once would do"},
        ],
        "figure": None,
    },
    {
        "id": "c5-03-h21",
        "band": "harder",
        "text": "Lemon juice protects a cut apple because the vitamin C in it "
                "is oxidised first. What does that tell you about how long the "
                "protection lasts?",
        "options": [
            {"text": "It lasts as long as the juice is still wet on the "
                     "surface",
             "correct": False,
             "why": "Drying is not what ends it. The vitamin C is used up by "
                    "reacting"},
            {"text": "It lasts indefinitely, because the vitamin C is not "
                     "changed by protecting the apple",
             "correct": False,
             "why": "It is changed: being oxidised is a reaction, and it "
                    "cannot happen twice to the same molecule"},
            {"text": "It lasts until the vitamin C has all been oxidised",
             "correct": True},
            {"text": "It lasts until the apple has been cut a second time",
             "correct": False,
             "why": "A second cut would expose new flesh, and the juice on the "
                    "first surface is running out in any case"},
        ],
        "figure": None,
    },
    {
        "id": "c5-03-h22",
        "band": "harder",
        "text": "A nail standing half in tap water rusts badly at the water "
                "line, while a nail lying fully under the same water rusts far "
                "less. Explain.",
        "options": [
            {"text": "The water above the second nail is colder, so its "
                     "reaction runs more slowly",
             "correct": False,
             "why": "Both nails are in one beaker at one temperature"},
            {"text": "The second nail is held down by the water, and pressure "
                     "slows a reaction",
             "correct": False,
             "why": "Pressure of that kind changes nothing here. What differs "
                    "is how much air reaches the metal"},
            {"text": "The second nail has no salt reaching it, and salt is "
                     "what carries the oxygen in",
             "correct": False,
             "why": "There is no salt in either case, and salt carries nothing "
                    "in. It only speeds things up"},
            {"text": "Far less air reaches the metal under the water than at "
                     "the surface",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c5-03-h23",
        "band": "harder",
        "text": "Iron has to be extracted from iron oxide in a furnace, and "
                "then spends its life turning back into iron oxide on its own. "
                "What does that suggest?",
        "options": [
            {"text": "That the oxide is the form iron settles into, which is "
                     "why rusting needs nothing to drive it",
             "correct": True},
            {"text": "That the furnace never fully separated the iron from its "
                     "oxygen in the first place",
             "correct": False,
             "why": "The metal that comes out is iron. It gains its oxygen "
                    "again afterwards, from the air"},
            {"text": "That rusting is the same reaction as extraction, run at "
                     "a lower temperature",
             "correct": False,
             "why": "Extraction takes oxygen away and rusting adds it. They "
                    "run in opposite directions"},
            {"text": "That iron is the most reactive of all the metals, since "
                     "it reacts without being heated",
             "correct": False,
             "why": "Aluminium and zinc are both more reactive, and both "
                    "oxidise without heating too"},
        ],
        "figure": None,
    },
    {
        "id": "c5-03-h24",
        "band": "harder",
        "text": "Two identical pads of steel wool are left for a week, one "
                "damp and one in a sealed dry box. What would a balance show "
                "for each?",
        "options": [
            {"text": "The damp one lighter and the dry one unchanged, because "
                     "rust falls off",
             "correct": False,
             "why": "Nothing is lost if the pad is weighed whole. Oxygen and "
                    "water have been added to it"},
            {"text": "The damp one heavier and the dry one unchanged",
             "correct": True},
            {"text": "Both heavier, because air settles onto any metal left "
                     "standing",
             "correct": False,
             "why": "Air does not settle onto metal. It has to react, and the "
                    "dry pad has no water to react with"},
            {"text": "Both unchanged, because a week is far too short for "
                     "anything to be measurable",
             "correct": False,
             "why": "Damp steel wool rusts visibly within days, and the gain "
                    "can be weighed"},
        ],
        "figure": None,
    },
    {
        "id": "c5-03-h25",
        "band": "harder",
        "text": "A rusty nail is put into a warm dry cupboard for a year. Why "
                "does the rust not disappear?",
        "options": [
            {"text": "Because the cupboard is not warm enough to drive the "
                     "reaction backwards",
             "correct": False,
             "why": "No temperature a cupboard reaches would do it. Rusting is "
                    "not undone by removing a reactant"},
            {"text": "Because rust holds no water, so drying it out changes "
                     "nothing about it",
             "correct": False,
             "why": "Rust does hold water, chemically. Even so, drying it does "
                    "not reverse the reaction"},
            {"text": "Because rusting is a chemical change, and removing the "
                     "water never undoes it",
             "correct": True},
            {"text": "Because the nail has already lost the iron that the rust "
                     "would need to go back to",
             "correct": False,
             "why": "The iron is still there, inside the rust. Nothing has "
                    "gone anywhere"},
        ],
        "figure": None,
    },
    {
        "id": "c5-03-h26",
        "band": "harder",
        "text": "A student weighs a nail, leaves it four weeks until it looks "
                "rusty, and weighs it again. The reading has hardly moved. "
                "Suggest why.",
        "options": [
            {"text": "Because rust weighs the same as the iron it replaced",
             "correct": False,
             "why": "Rust is heavier than the iron it came from. That is the "
                    "rule the experiment tests"},
            {"text": "Because oxygen is a gas, and gases add no mass to a "
                     "solid",
             "correct": False,
             "why": "A gas has mass, and the oxygen in the rust brings it with "
                    "it"},
            {"text": "Because a thin layer of rust weighs too little for a "
                     "school balance to resolve",
             "correct": False,
             "why": "A school balance reads to a hundredth of a gram, which is "
                    "enough to show the gain"},
            {"text": "Because some of the rust has flaked off, so what is on "
                     "the balance is not everything the nail gained",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c5-03-h27",
        "band": "harder",
        "text": "A ship is repainted but its zinc blocks are not renewed. Six "
                "months later the hull is corroding wherever the paint is "
                "chipped. Explain both facts.",
        "options": [
            {"text": "The paint protects only where it is whole, and with the "
                     "blocks gone the bare metal has nothing left",
             "correct": True},
            {"text": "The new paint has made the steel more reactive than the "
                     "old paint did",
             "correct": False,
             "why": "Paint does not change how reactive steel is. It only "
                    "keeps things away from it"},
            {"text": "The blocks were what held the paint on, so the paint "
                     "chipped because they had gone",
             "correct": False,
             "why": "The blocks have no mechanical job. Paint chips on any "
                    "hull in use"},
            {"text": "Six months is too soon for paint to fail, so the "
                     "corrosion must have been there before",
             "correct": False,
             "why": "Paint on a working hull chips within weeks. The chips are "
                    "expected and the blocks are what covered for them"},
        ],
        "figure": None,
    },
    {
        "id": "c5-03-h28",
        "band": "harder",
        "text": "Magnesium burning and iron rusting are both oxidations. Why "
                "does only one of them give out light?",
        "options": [
            {"text": "Because magnesium is a metal and iron is an alloy, and "
                     "only metals glow",
             "correct": False,
             "why": "Iron is a metal too, and steel wool glows brightly when "
                    "it burns in oxygen"},
            {"text": "Because the fast one releases its energy quickly enough "
                     "to reach flame temperature",
             "correct": True},
            {"text": "Because rusting takes energy in, while burning gives "
                     "energy out",
             "correct": False,
             "why": "Both give energy out. What differs is how quickly it "
                    "comes out"},
            {"text": "Because magnesium oxide is white and rust is orange, and "
                     "white products glow",
             "correct": False,
             "why": "The colour of the product does not decide whether a "
                    "reaction gives out light"},
        ],
        "figure": None,
    },
    {
        "id": "c5-03-h29",
        "band": "harder",
        "text": "A student writes that rust is iron oxide. Why is the fuller "
                "name worth insisting on?",
        "options": [
            {"text": "Because iron oxide is what magnesium makes, and the two "
                     "must be told apart",
             "correct": False,
             "why": "Magnesium makes magnesium oxide. The reason is about the "
                    "water in rust"},
            {"text": "Because iron oxide is the name for the rust on steel "
                     "only, not on plain iron",
             "correct": False,
             "why": "Steel is mostly iron and rusts the same way. The "
                    "difference is not about which metal"},
            {"text": "Because the water is part of the product and not just "
                     "one of the reactants",
             "correct": True},
            {"text": "Because iron oxide describes a mixture and rust is a "
                     "compound",
             "correct": False,
             "why": "Both names describe compounds. The fuller one says that "
                    "water is built into it"},
        ],
        "figure": None,
    },
    {
        "id": "c5-03-h30",
        "band": "harder",
        "text": "Suppose rust behaved the way aluminium oxide does. What would "
                "happen to an iron gate left outdoors?",
        "options": [
            {"text": "It would rust right through in half the time, because "
                     "the layer would hold water against it",
             "correct": False,
             "why": "A clinging layer keeps water off rather than holding it "
                    "on. That is why aluminium survives"},
            {"text": "It would never oxidise at all, and would stay as bright "
                     "as the day it was made",
             "correct": False,
             "why": "Aluminium oxidises at once. What its oxide does is stop "
                    "the reaction going further"},
            {"text": "It would go orange and then turn back to iron as the "
                     "layer sealed itself",
             "correct": False,
             "why": "Nothing turns back. A sealing layer stops the reaction "
                    "rather than reversing it"},
            {"text": "A thin layer would form and then seal the surface, and "
                     "the gate would last far longer",
             "correct": True},
        ],
        "figure": None,
    },
]
