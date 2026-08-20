"""C4 lesson 02 — Reactions rearrange atoms: twelve questions (MRB-246).

The lesson is one sentence long — a reaction breaks joins and makes new ones,
and it can only ever use the atoms it was given — and everything else on the
page is that sentence being counted, or that sentence being tested to
destruction by asking for something the atoms cannot spell. These twelve probe
the angles the mastery ladder leaves alone: where a named atom actually ENDS
UP, what "the same atoms" rules out as well as what it rules in, and the rule
carried into places the lesson never visits.

The distractors are built from the lesson's two declared misconceptions.

`REACT-03` (in a reaction the atoms themselves change into other kinds of atom)
drives the wrong options in e01, s01, s04 and h03. Each of them takes a real
change — a white powder, a black powder, a different substance — and locates
that change INSIDE the atom, which is exactly the move `#s-think` takes apart.
h03 is deliberately the copper case, because `REACT-03` is C2's `ATOM-01` grown
up and copper is the substance `ATOM-01` was minted on: a student who has met
both should feel them join.

`REACT-04` (new atoms can be made if the conditions are right) drives e04, s02,
h02 and h04, where heat, pressure, a catalyst or simply more effort is imagined
to supply an atom that was never there. Every one of those distractors is a
CONDITION offered as a source of matter, which is the shape the belief actually
takes in a classroom — nobody says "atoms can be created", they say "not yet,
they haven't found the right way".

A third strand runs through e02, e03, s03 and h01 and is in neither register
entry: that matter can be spent. Burnt up, used up, split into pieces, turned
into heat. It is the same wrong rule as `REACT-04` read backwards, and it is
the one that makes a student comfortable with an equation whose sides do not
match — which is where `c4-05` starts.

⚑ h01 and h04 both carry the nuclear hedge (Design's science flag 7,
CONFIRMED). h01 credits a student who says transmutation is real and is not
chemistry; nothing here marks "elements never change" as right, because the
lesson does not say that and a question bank that did would contradict the page
it belongs to.

⚑ h04 specifies PURE OXYGEN, not air, and the word is load-bearing. Air is
about four-fifths nitrogen, so a flame in air genuinely can make nitrogen
compounds and the question's own answer would be false. This is the kind of
detail that turns a good question into a wrong one, and it is called out here
so a later edit does not tidy "pure oxygen" back to "air".

Every question here is new prose — a question bank is the one place in these
two files where that is true — and the bar is §13's: each distractor is a WRONG
RULE in the correct answer's own shape, and each is a mistake a real student
makes.

Every option set was measured for the MRB-177 length tell before this file was
handed back, and none of the twelve is one: the correct option is never the
longest in its set. Three sets — e04, s01 and h03 — had their options REORDERED
afterwards, and it is worth saying why, because moving an answer index is the
one repair §13 forbids. It forbids it as a way of FIXING A LENGTH TELL, and
there was no tell to fix in any of the three. The correct answer had simply
landed at position C six times out of twelve, which is a different tell and a
worse one — a student who notices it can score without reading any of the
twelve. No text was touched by the reorder; the spread is now three at each
position.
"""

UNIT = "C4"
LESSON = "reactions-rearrange-atoms"
LESSON_NUMBER = 2

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "c4-02-e01",
        "band": "easier",
        "text": "Magnesium burns in oxygen and leaves a white powder called "
                "magnesium oxide. What is that powder made of?",
        "options": [
            {"text": "Magnesium atoms and oxygen atoms, joined to each other",
             "correct": True},
            {"text": "Magnesium oxide atoms, which are a brand new kind of "
                     "atom", "correct": False,
             "why": "There is no such thing as a magnesium oxide atom. "
                    "Magnesium oxide is a compound: magnesium atoms and "
                    "oxygen atoms held together, and both are still exactly "
                    "the atoms they were before the flame."},
            {"text": "Oxygen atoms only, because the magnesium was burnt "
                     "away", "correct": False,
             "why": "Nothing is burnt away. Every magnesium atom that was in "
                    "the ribbon is in the powder, which is why the powder "
                    "weighs more than the ribbon did rather than less."},
            {"text": "Magnesium atoms only, with the oxygen turned into heat "
                     "instead", "correct": False,
             "why": "Heat is not something an atom can turn into. The oxygen "
                    "atoms came out of the air and are part of the powder — "
                    "that is where the extra mass comes from."},
        ],
        "figure": None,
    },
    {
        "id": "c4-02-e02",
        "band": "easier",
        "text": "Hydrogen and oxygen react and water appears. Where did the "
                "atoms in that water come from?",
        "options": [
            {"text": "The flame made them out of the energy it was giving "
                     "out", "correct": False,
             "why": "Energy is not made of atoms and cannot be turned into "
                    "them. A flame can start a reaction and it can heat the "
                    "room, but it cannot add a single atom to what is there."},
            {"text": "From the hydrogen and the oxygen that were there "
                     "already", "correct": True},
            {"text": "The two gases made water atoms where they touched each "
                     "other", "correct": False,
             "why": "There is no such thing as a water atom. Water is two "
                    "hydrogen atoms joined to one oxygen atom, and all three "
                    "were in the balloons before anything happened."},
            {"text": "Half from the gases, and half from the air in the room "
                     "around", "correct": False,
             "why": "The atoms are all accounted for without the room: four "
                    "hydrogens and two oxygens go in, and the same four and "
                    "two come out as two water particles."},
        ],
        "figure": None,
    },
    {
        "id": "c4-02-e03",
        "band": "easier",
        "text": "Four hydrogen atoms and two oxygen atoms are on a table, and "
                "there is nothing else. How many oxygen atoms can be in the "
                "products?",
        "options": [
            {"text": "One, because a particle of water needs only one",
             "correct": False,
             "why": "One water particle needs one, and there is enough here "
                    "for two of them. The number you can use is set by the "
                    "table, not by the recipe for one particle."},
            {"text": "Four, because there are four hydrogen atoms to pair "
                     "up", "correct": False,
             "why": "Counting the hydrogens tells you nothing about the "
                    "oxygens. There are two oxygen atoms on the table, so two "
                    "is how many the products can contain."},
            {"text": "Two, because two is how many there were to start with",
             "correct": True},
            {"text": "However many the reaction turns out to need at the "
                     "time", "correct": False,
             "why": "A reaction cannot fetch an atom it was not given. If it "
                    "needs a third oxygen atom, the reaction does not happen "
                    "— the atoms do not appear to meet the need."},
        ],
        "figure": None,
    },
    {
        "id": "c4-02-e04",
        "band": "easier",
        "text": "A student says lead could be turned into gold by a chemical "
                "reaction if it were hot enough. What is wrong with that?",
        "options": [
            {"text": "Nobody has yet found the right catalyst to make it "
                     "happen", "correct": False,
             "why": "A catalyst changes how fast a reaction goes, not which "
                    "atoms exist. No catalyst has ever made an atom, and none "
                    "ever will — that is not the kind of thing they do."},
            {"text": "Gold is far too heavy to be made in a school "
                     "laboratory", "correct": False,
             "why": "Weight is not the obstacle. A gram of gold is a gram, "
                    "and it is no easier to make in a big laboratory than a "
                    "small one, because it cannot be made by a reaction at "
                    "all."},
            {"text": "Lead and gold are two metals that do not react "
                     "together", "correct": False,
             "why": "The problem is not that they will not react. Even if "
                    "they did, gold atoms would have to be there beforehand — "
                    "and if they were, you already had gold."},
            {"text": "A chemical reaction can only rearrange the atoms it is "
                     "given", "correct": True},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "c4-02-s01",
        "band": "standard",
        "text": "Methane burns in oxygen to make carbon dioxide and water. "
                "There is one carbon atom in the methane. Where is it "
                "afterwards?",
        "options": [
            {"text": "Destroyed by the flame, which is why no black solid is "
                     "left", "correct": False,
             "why": "The flame does not destroy atoms. The carbon atom leaves "
                    "as part of a colourless gas, which is why you see "
                    "nothing left behind rather than nothing existing."},
            {"text": "In the carbon dioxide, joined to two of the oxygen "
                     "atoms", "correct": True},
            {"text": "Turned into a carbon dioxide atom by the heat of the "
                     "burning", "correct": False,
             "why": "There is no such thing as a carbon dioxide atom. Carbon "
                    "dioxide is one carbon atom joined to two oxygen atoms, "
                    "and the carbon atom is still a carbon atom inside it."},
            {"text": "Split into smaller pieces and shared out between both "
                     "products", "correct": False,
             "why": "Chemical reactions do not split atoms — they only "
                    "change what each atom is joined to. One carbon atom went "
                    "in, so one carbon atom comes out, whole."},
        ],
        "figure": None,
    },
    {
        "id": "c4-02-s02",
        "band": "standard",
        "text": "A strip of magnesium is weighed, burned in an open dish, and "
                "the powder is weighed. The powder is heavier. Why?",
        "options": [
            {"text": "Oxygen atoms from the air have joined the magnesium "
                     "atoms", "correct": True},
            {"text": "New magnesium atoms were made by the reaction as it "
                     "ran", "correct": False,
             "why": "No reaction has ever made an atom. Every magnesium atom "
                    "in the powder was in the ribbon first — the extra mass "
                    "arrived from the air, not from nowhere."},
            {"text": "The heat from the flame was added to the magnesium "
                     "itself", "correct": False,
             "why": "Heat has no mass to add. What went into the dish and "
                    "stayed there is oxygen, and oxygen atoms are matter that "
                    "a balance can read."},
            {"text": "The magnesium atoms grew heavier while they were "
                     "burning", "correct": False,
             "why": "An atom of magnesium is the same atom before and after. "
                    "There are just as many of them as there were, and each "
                    "one has exactly the mass it always had."},
        ],
        "figure": None,
    },
    {
        "id": "c4-02-s03",
        "band": "standard",
        "text": "A reaction is run in a sealed flask, so nothing can get in "
                "or out. What must be true of the atoms inside it?",
        "options": [
            {"text": "There are fewer at the end, because some were used up "
                     "reacting", "correct": False,
             "why": "Being used up means being joined to something else, not "
                    "ceasing to exist. Count them at the end and every one is "
                    "still in the flask, in a new arrangement."},
            {"text": "There are exactly as many of each kind as there were "
                     "before", "correct": True},
            {"text": "There are more at the end, because new substances have "
                     "appeared", "correct": False,
             "why": "A new substance is a new arrangement, not new matter. "
                    "The atoms in it are the atoms that were already in the "
                    "flask before you started."},
            {"text": "The number changes depending on how long it is left "
                     "sealed", "correct": False,
             "why": "Time changes how far a reaction has got, not how many "
                    "atoms exist. Sealed for a second or sealed for a year, "
                    "the count of each kind is the same."},
        ],
        "figure": None,
    },
    {
        "id": "c4-02-s04",
        "band": "standard",
        "text": "Water and hydrogen peroxide are both built from hydrogen and "
                "oxygen only, but they are different substances. How can "
                "that be?",
        "options": [
            {"text": "Peroxide also contains a small amount of a third "
                     "element", "correct": False,
             "why": "It does not. Hydrogen peroxide is two hydrogen atoms "
                    "and two oxygen atoms and nothing else — the difference "
                    "from water is one extra oxygen atom, not a new "
                    "ingredient."},
            {"text": "The oxygen in peroxide is a stronger kind of oxygen "
                     "atom", "correct": False,
             "why": "There is one kind of oxygen atom and both substances "
                    "have it. An atom does not take on the properties of "
                    "whatever it happens to be part of."},
            {"text": "The atoms are joined in different numbers and a "
                     "different arrangement", "correct": True},
            {"text": "Peroxide was made at a much higher temperature than "
                     "the water", "correct": False,
             "why": "How a substance was made does not decide what it is. "
                    "Two hydrogens and two oxygens is hydrogen peroxide "
                    "whether it was made hot or cold."},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "c4-02-h01",
        "band": "harder",
        "text": "Inside a nuclear reactor, uranium atoms split and become "
                "atoms of other elements. Why is that not a chemical "
                "reaction?",
        "options": [
            {"text": "It happens far too quickly to be counted as a chemical "
                     "reaction", "correct": False,
             "why": "Speed does not decide it. An explosion is fast and "
                    "chemical; rusting is slow and chemical. What makes this "
                    "different is that the atoms themselves are changing."},
            {"text": "Nothing new is made, so there is no reaction there at "
                     "all", "correct": False,
             "why": "New substances certainly are made — that is the whole "
                    "problem with nuclear waste. The change is real; it is "
                    "just not the kind of change chemistry describes."},
            {"text": "A chemical reaction changes what atoms are joined to, "
                     "not the atoms", "correct": True},
            {"text": "Chemical reactions do the same thing when they are hot "
                     "enough", "correct": False,
             "why": "No temperature a chemist can reach turns one element "
                    "into another. Heat gives atoms enough energy to break "
                    "and make joins, and that is the limit of what it does."},
        ],
        "figure": None,
    },
    {
        "id": "c4-02-h02",
        "band": "harder",
        "text": "A company claims its new firework mixture, which contains no "
                "gold, produces sparks of real gold. What is the strongest "
                "reason to doubt it?",
        "options": [
            {"text": "Gold is an element, so gold atoms would have to be "
                     "there first", "correct": True},
            {"text": "A firework does not burn hot enough to produce a metal "
                     "like gold", "correct": False,
             "why": "Temperature is not what is missing. However hot the "
                    "firework burns, it is rearranging the atoms in the "
                    "mixture, and none of them is a gold atom."},
            {"text": "The gold would be destroyed by the explosion before "
                     "anyone saw it", "correct": False,
             "why": "An explosion does not destroy atoms either. If gold "
                    "atoms were in there they would still be gold atoms "
                    "afterwards — the point is that they were never in "
                    "there."},
            {"text": "Gold would cost the company far too much to put in a "
                     "firework", "correct": False,
             "why": "That is a reason they would not want to, not a reason "
                    "they could not. The claim fails on chemistry before it "
                    "gets anywhere near the price."},
        ],
        "figure": None,
    },
    {
        "id": "c4-02-h03",
        "band": "harder",
        "text": "Copper is orange, soft and conducts electricity. Copper "
                "oxide is a black powder that does not conduct. What has "
                "changed about the copper atoms?",
        "options": [
            {"text": "They have turned black, which is what makes the powder "
                     "black", "correct": False,
             "why": "An atom is not a tiny piece of the substance it belongs "
                    "to. A copper atom is not orange in the metal and it has "
                    "not become black in the powder — colour belongs to the "
                    "substance, not to one atom."},
            {"text": "They have become copper oxide atoms during the "
                     "reaction", "correct": False,
             "why": "There is no such thing as a copper oxide atom. Copper "
                    "oxide is copper atoms joined to oxygen atoms, and each "
                    "one is still exactly the atom it was."},
            {"text": "They have lost the parts of them that carried the "
                     "current", "correct": False,
             "why": "Chemical reactions do not take atoms to pieces. "
                    "Conducting is something the metal does as a whole, and "
                    "the powder does not do it because the atoms are "
                    "arranged differently."},
            {"text": "Nothing at all — they are joined to oxygen atoms now",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c4-02-h04",
        "band": "harder",
        "text": "Methane is burned in pure oxygen. A student writes the "
                "products as carbon dioxide, water and a little ammonia. Why "
                "can ammonia not be one of them?",
        "options": [
            {"text": "Ammonia would need more energy than a flame is able to "
                     "give", "correct": False,
             "why": "Energy is not the missing thing. Ammonia is nitrogen "
                    "joined to hydrogen, and no amount of energy will produce "
                    "a nitrogen atom that was not there to begin with."},
            {"text": "Ammonia only forms when a reaction is run under high "
                     "pressure", "correct": False,
             "why": "Pressure changes how well a reaction goes, not which "
                    "atoms exist. With no nitrogen in the methane or the "
                    "oxygen, no pressure would help."},
            {"text": "Ammonia is a gas, and every product listed here is a "
                     "liquid", "correct": False,
             "why": "Carbon dioxide is a gas too, so that rule would rule out "
                    "one of the right answers. Being a gas is not what "
                    "excludes ammonia."},
            {"text": "Ammonia contains nitrogen, and neither reactant has "
                     "any", "correct": True},
        ],
        "figure": None,
    },
]
