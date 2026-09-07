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

    # ── easier · MRB-335 top-up ─────────────────────────────────────────
    {
        "id": "c4-02-e05",
        "band": "easier",
        "text": "What is a reactant?",
        "options": [
            {"text": "A substance that takes part in the reaction without "
                     "being used up by it, so that it is still there in the "
                     "same amount at the end",
             "correct": False,
             "why": "That is a catalyst. A reactant is used up in making the "
                    "products"},
            {"text": "A substance the reaction makes",
             "correct": False,
             "why": "That is a product. Reactants go in, products come out"},
            {"text": "The container the reaction happens in",
             "correct": False,
             "why": "A flask is equipment. A reactant takes part"},
            {"text": "A substance you start with, before the reaction "
                     "happens",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c4-02-e06",
        "band": "easier",
        "text": "What does it mean to say a reaction REARRANGES atoms?",
        "options": [
            {"text": "It keeps the same atoms and puts them together "
                     "differently",
             "correct": True},
            {"text": "It swaps some of the atoms for different kinds, so that "
                     "the substance you end up with can have properties the "
                     "starting one could not have had",
             "correct": False,
             "why": "No atom changes kind in a chemical reaction. New "
                    "properties come from new PARTNERS"},
            {"text": "It moves the atoms into a tidier order",
             "correct": False,
             "why": "Nothing is being tidied. The joins between atoms are "
                    "broken and remade"},
            {"text": "It makes the atoms smaller so more will fit",
             "correct": False,
             "why": "Atoms never change size. Only what they are joined to "
                    "changes"},
        ],
        "figure": None,
    },
    {
        "id": "c4-02-e07",
        "band": "easier",
        "text": "What is a compound?",
        "options": [
            {"text": "A mixture of two substances that have been stirred "
                     "together thoroughly enough that no part of it can be "
                     "told apart from any other part",
             "correct": False,
             "why": "Stirring joins nothing. A compound has its atoms "
                    "chemically joined"},
            {"text": "A substance made of two or more kinds of atom joined "
                     "together",
             "correct": True},
            {"text": "Any substance with a long name",
             "correct": False,
             "why": "Names have nothing to do with it. Water is a compound "
                    "and has a short one"},
            {"text": "A substance made of one kind of atom",
             "correct": False,
             "why": "That is an element. A compound needs at least two"},
        ],
        "figure": None,
    },
    {
        "id": "c4-02-e08",
        "band": "easier",
        "text": "There is no such thing as a magnesium oxide atom. Why not?",
        "options": [
            {"text": "Because magnesium oxide is white, and an atom has no "
                     "colour of its own to give it",
             "correct": False,
             "why": "True about colour and beside the point. Magnesium oxide "
                    "is made of two kinds of atom joined"},
            {"text": "Because magnesium oxide is a mixture",
             "correct": False,
             "why": "It is a compound, with its atoms chemically joined in a "
                    "fixed ratio"},
            {"text": "Because magnesium oxide is a compound — magnesium atoms "
                     "joined to oxygen atoms",
             "correct": True},
            {"text": "Because its atoms are too small to have a name",
             "correct": False,
             "why": "Every atom has a name — the name of its element. There "
                    "simply is no element called magnesium oxide"},
        ],
        "figure": None,
    },
    {
        "id": "c4-02-e09",
        "band": "easier",
        "text": "Hydrogen and oxygen are the only atoms on the bench. Which "
                "of these can the bench build?",
        "options": [
            {"text": "Ammonia, which is built out of hydrogen and needs "
                     "nothing more than a supply of it and enough energy to "
                     "join the atoms up",
             "correct": False,
             "why": "Ammonia holds nitrogen as well, and there is no nitrogen "
                    "on the table"},
            {"text": "Methane",
             "correct": False,
             "why": "Methane needs carbon, and none is available"},
            {"text": "Sodium chloride",
             "correct": False,
             "why": "Neither sodium nor chlorine is on the table, so neither "
                    "can be in a product"},
            {"text": "Hydrogen peroxide",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c4-02-e10",
        "band": "easier",
        "text": "Copper reacts with oxygen to make copper oxide. How many "
                "copper atoms are in the product compared with the copper you "
                "started with?",
        "options": [
            {"text": "Exactly the same number",
             "correct": True},
            {"text": "Fewer, because some of them are used up in joining the "
                     "oxygen and are not available to appear in the product "
                     "afterwards",
             "correct": False,
             "why": "Joining uses no atoms up. Every copper atom you started "
                    "with is in the product"},
            {"text": "More, because the oxygen adds to them",
             "correct": False,
             "why": "The oxygen adds oxygen atoms. The number of copper atoms "
                    "is unchanged"},
            {"text": "It cannot be known without weighing the product",
             "correct": False,
             "why": "It can be known without weighing anything. Atoms are "
                    "never created or destroyed"},
        ],
        "figure": None,
    },

    # ── standard · MRB-335 top-up ───────────────────────────────────────
    {
        "id": "c4-02-s05",
        "band": "standard",
        "text": "Two hydrogen particles react with one oxygen particle. Each "
                "hydrogen particle holds two atoms and the oxygen particle "
                "holds two. How many water particles can be made?",
        "options": [
            {"text": "One, because there is only one oxygen particle and "
                     "every water particle has to contain a whole one of them",
             "correct": False,
             "why": "The oxygen particle holds TWO atoms, and each water "
                    "needs only one. It supplies two waters"},
            {"text": "Four",
             "correct": False,
             "why": "That is the number of hydrogen ATOMS. Each water takes "
                    "two of them, so four hydrogens make two waters"},
            {"text": "Three",
             "correct": False,
             "why": "There is no way to make three from four hydrogens and "
                    "two oxygens without leftovers that do not exist"},
            {"text": "Two",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c4-02-s06",
        "band": "standard",
        "text": "A reaction is asked to make ammonia from hydrogen and oxygen "
                "alone, and the bench refuses. What is the refusal telling "
                "you?",
        "options": [
            {"text": "That ammonia contains nitrogen, and no nitrogen was "
                     "supplied",
             "correct": True},
            {"text": "That the conditions on the bench are wrong, and that "
                     "with more heat or a catalyst the same two gases would "
                     "eventually give ammonia",
             "correct": False,
             "why": "Conditions change how a reaction goes, never which atoms "
                    "exist. No amount of heat makes nitrogen"},
            {"text": "That ammonia cannot be made by any reaction",
             "correct": False,
             "why": "It is made industrially by the tonne — from nitrogen and "
                    "hydrogen"},
            {"text": "That the bench is broken",
             "correct": False,
             "why": "The refusal is the rule working. A reaction can only "
                    "build from the atoms it is given"},
        ],
        "figure": None,
    },
    {
        "id": "c4-02-s07",
        "band": "standard",
        "text": "Water and hydrogen peroxide were both built from the same "
                "two elements on the bench. Which statement about them is "
                "right?",
        "options": [
            {"text": "They are the same substance written two different ways",
             "correct": False,
             "why": "One quenches thirst and one bleaches hair. Same "
                    "elements, different substances"},
            {"text": "Each peroxide particle holds one more oxygen atom than "
                     "a water particle",
             "correct": True},
            {"text": "Hydrogen peroxide is water with extra oxygen dissolved "
                     "in it",
             "correct": False,
             "why": "The extra oxygen is joined inside each particle rather "
                    "than dissolved between them"},
            {"text": "Hydrogen peroxide holds a different kind of hydrogen "
                     "atom",
             "correct": False,
             "why": "A hydrogen atom is a hydrogen atom. What differs is how "
                    "many oxygens it is joined to"},
        ],
        "figure": None,
    },
    {
        "id": "c4-02-s08",
        "band": "standard",
        "text": "Propane holds three carbon atoms in each particle. One "
                "particle burns completely. How many carbon dioxide particles "
                "are made?",
        "options": [
            {"text": "One, because all three carbon atoms end up joined "
                     "together inside a single particle of the gas that comes "
                     "out of the flame",
             "correct": False,
             "why": "Carbon dioxide holds ONE carbon atom. Three carbons need "
                    "three particles of it"},
            {"text": "Six, one for each carbon and one for each of the oxygen "
                     "atoms they join",
             "correct": False,
             "why": "The oxygens are inside those particles rather than "
                    "making particles of their own"},
            {"text": "Three",
             "correct": True},
            {"text": "It depends how much oxygen is supplied",
             "correct": False,
             "why": "Too little oxygen stops the burning being complete. The "
                    "question says it was, so all three carbons are used"},
        ],
        "figure": None,
    },
    {
        "id": "c4-02-s09",
        "band": "standard",
        "text": "Sodium is a soft metal that catches fire on water. Chlorine "
                "is a poisonous green gas. Table salt is neither. What has "
                "happened to the sodium atoms?",
        "options": [
            {"text": "They have been changed into a different kind of atom by "
                     "the violence of the reaction between the two elements",
             "correct": False,
             "why": "No atom changes kind in a chemical reaction, however "
                    "violent it is"},
            {"text": "They have been used up, and the salt is made of "
                     "chlorine only",
             "correct": False,
             "why": "Both elements are in the salt. Neither is used up in the "
                    "sense of ceasing to exist"},
            {"text": "They are still loose in the salt, which is why it "
                     "dissolves",
             "correct": False,
             "why": "They are joined, not loose. Dissolving does not release "
                    "sodium metal — a spoonful of salt in water does "
                    "nothing"},
            {"text": "Nothing, except that they are now joined to chlorine "
                     "atoms",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c4-02-s10",
        "band": "standard",
        "text": "A reaction warms its surroundings. Using the idea of joins "
                "between atoms, why?",
        "options": [
            {"text": "Because the new joins give back more energy than "
                     "breaking the old ones cost",
             "correct": True},
            {"text": "Because the reaction is fast, and fast reactions give "
                     "out heat",
             "correct": False,
             "why": "Speed has nothing to do with it. Slow rusting warms its "
                    "surroundings too"},
            {"text": "Because breaking joins always gives out energy",
             "correct": False,
             "why": "Exactly backwards. Breaking a join always COSTS energy; "
                    "making one gives it back"},
            {"text": "Because heat is one of the products",
             "correct": False,
             "why": "Heat is not a substance and is never a product. It is "
                    "the surplus from the bookkeeping on joins"},
        ],
        "figure": None,
    },

    # ── harder · MRB-335 top-up ─────────────────────────────────────────
    {
        "id": "c4-02-h05",
        "band": "harder",
        "text": "A balloon of hydrogen and oxygen sits unchanged for months, "
                "yet the reaction gives out an enormous amount of energy. Why "
                "does it need a flame?",
        "options": [
            {"text": "Because the two gases have to be mixed thoroughly first",
             "correct": False,
             "why": "They are already mixed. What is missing is payment for "
                    "the first joins to be broken"},
            {"text": "Because the reaction needs heat as one of its "
                     "reactants",
             "correct": False,
             "why": "Heat is a condition, not a reactant. It starts the "
                    "reaction rather than being consumed by it"},
            {"text": "Because hydrogen only burns above a certain "
                     "temperature, which is a property of the gas",
             "correct": False,
             "why": "This is the same fact described from the outside. What "
                    "the temperature buys is the first broken joins"},
            {"text": "Because breaking the first joins costs energy, and "
                     "nothing has paid for it",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c4-02-h06",
        "band": "harder",
        "text": "A reaction takes energy IN and everything around it gets "
                "colder. What does that say about its joins?",
        "options": [
            {"text": "That the new joins give back less energy than breaking "
                     "the old ones cost",
             "correct": True},
            {"text": "That no new joins are made at all, so all the energy "
                     "spent on breaking the old ones is simply lost to the "
                     "surroundings as the reaction goes on",
             "correct": False,
             "why": "New joins are always made — that is what produces the "
                    "products. They just give back less than was spent"},
            {"text": "That the reaction is running backwards",
             "correct": False,
             "why": "It is running forwards and making products. Which way it "
                    "runs is not what decides the energy"},
            {"text": "That the atoms are being destroyed to supply the "
                     "energy",
             "correct": False,
             "why": "No atom is destroyed in any chemical reaction. The "
                    "energy comes from the joins"},
        ],
        "figure": None,
    },
    {
        "id": "c4-02-h07",
        "band": "harder",
        "text": "Someone offers to make a diamond by reacting sand with "
                "water, arguing that both contain oxygen. Why can it not "
                "work?",
        "options": [
            {"text": "Because sand and water do not react with each other at "
                     "all, and two substances that are unreactive together "
                     "can never be made to produce anything new",
             "correct": False,
             "why": "The reaction failing is a symptom. Even a violent "
                    "reaction between them could not produce carbon"},
            {"text": "Because diamond is carbon, and neither sand nor water "
                     "contains any",
             "correct": True},
            {"text": "Because diamond can only be made under enormous "
                     "pressure",
             "correct": False,
             "why": "Pressure is a condition, and it is a real one. It is not "
                    "the reason this recipe is impossible"},
            {"text": "Because diamond is a compound and sand is an element",
             "correct": False,
             "why": "Both descriptions are the wrong way round. Diamond is an "
                    "element and sand is a compound"},
        ],
        "figure": None,
    },
    {
        "id": "c4-02-h08",
        "band": "harder",
        "text": "Two grams of hydrogen react with sixteen grams of oxygen to "
                "make eighteen grams of water. Which statement about the ATOMS "
                "follows from that?",
        "options": [
            {"text": "That eighteen grams' worth of new atoms have been "
                     "created out of the two starting materials by the "
                     "reaction between them",
             "correct": False,
             "why": "No atom is created. The eighteen grams are the same "
                    "atoms that went in"},
            {"text": "That the atoms have got heavier as they joined",
             "correct": False,
             "why": "An atom's mass does not change on joining. The total "
                    "adds up because nothing was lost"},
            {"text": "That every atom in the water was in the hydrogen or the "
                     "oxygen first",
             "correct": True},
            {"text": "That some hydrogen atoms became oxygen atoms",
             "correct": False,
             "why": "That would be a nuclear change. Chemistry only alters "
                    "what an atom is joined to"},
        ],
        "figure": None,
    },
    {
        "id": "c4-02-h09",
        "band": "harder",
        "text": "A firework maker says a mixture with no iron in it produces "
                "orange sparks that are iron. What single point defeats the "
                "claim?",
        "options": [
            {"text": "Orange sparks can be produced by several substances, so "
                     "the colour on its own is not enough to identify what is "
                     "burning in a firework",
             "correct": False,
             "why": "Perfectly true, and a weaker objection. Even if the "
                    "sparks looked exactly right, the iron could not be "
                    "there"},
            {"text": "Fireworks burn too quickly to make a metal",
             "correct": False,
             "why": "Speed is not the obstacle. The obstacle is that there "
                    "are no iron atoms to build from"},
            {"text": "Iron does not burn",
             "correct": False,
             "why": "Fine iron wool burns readily. That is not what is wrong "
                    "with the claim"},
            {"text": "Iron is an element, so iron atoms would have to be in "
                     "the mixture already",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c4-02-h10",
        "band": "harder",
        "text": "A student writes that the reaction “used up all the "
                "oxygen”, and concludes that those oxygen atoms no longer "
                "exist. What is the correction?",
        "options": [
            {"text": "They exist, and they are inside the products — used up "
                     "means no longer available as oxygen gas",
             "correct": True},
            {"text": "They exist, and they have been pushed out of the flask "
                     "into the room, where they are now mixed back in with "
                     "the rest of the air",
             "correct": False,
             "why": "They did not leave. They are chemically joined inside "
                    "the product, which is why it is heavier"},
            {"text": "Nothing is wrong — a reactant that is used up has been "
                     "destroyed",
             "correct": False,
             "why": "Used up describes a substance running out, never atoms "
                    "being destroyed"},
            {"text": "They have become a different kind of atom",
             "correct": False,
             "why": "Chemistry never changes what kind an atom is. Only its "
                    "partners change"},
        ],
        "figure": None,
    },
]
