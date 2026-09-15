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

    # ── easier · MRB-338 top-up ─────────────────────────────────────────
    {
        "id": "c4-02-e11",
        "band": "easier",
        "text": "In a chemical reaction, what is a product?",
        "options": [
            {"text": "A substance that did not exist before the reaction ran",
             "correct": True},
            {"text": "A substance that is used up as the reaction runs",
             "correct": False,
             "why": "That is a reactant. Products are what the rearranged "
                    "atoms end up as"},
            {"text": "A substance that helps the reaction along without "
                     "changing",
             "correct": False,
             "why": "That is a catalyst. It is not made by the reaction"},
            {"text": "A substance that was present but took no part at all",
             "correct": False,
             "why": "Something that takes no part is neither a reactant nor a "
                    "product"},
        ],
        "figure": None,
    },
    {
        "id": "c4-02-e12",
        "band": "easier",
        "text": "Iron and sulfur are heated together and make iron sulfide. "
                "How many sulfur atoms are in the iron sulfide compared with "
                "the sulfur you started with?",
        "options": [
            {"text": "Fewer than before",
             "correct": False,
             "why": "Joining to iron does not use a sulfur atom up. Every one "
                    "of them is in the product"},
            {"text": "The same number",
             "correct": True},
            {"text": "More than before",
             "correct": False,
             "why": "Heating supplies energy, and energy is not made of atoms, "
                    "so it adds none"},
            {"text": "Half as many",
             "correct": False,
             "why": "Pairing up changes what an atom is joined to, not how "
                    "many of them there are"},
        ],
        "figure": None,
    },
    {
        "id": "c4-02-e13",
        "band": "easier",
        "text": "What is an element?",
        "options": [
            {"text": "A substance made of two or more kinds of atom joined",
             "correct": False,
             "why": "That is a compound. An element holds one kind of atom "
                    "and no more"},
            {"text": "A substance made of one kind of atom",
             "correct": True},
            {"text": "A substance that is dug out of the ground on its own",
             "correct": False,
             "why": "Where a substance is found decides nothing. Most elements "
                    "are mined already joined to something else"},
            {"text": "A substance that is pure",
             "correct": False,
             "why": "Pure means one substance, which water is. An element "
                    "means one kind of ATOM"},
        ],
        "figure": None,
    },
    {
        "id": "c4-02-e14",
        "band": "easier",
        "text": "A student asks whether a reaction could make a brand new "
                "kind of atom if the temperature were high enough. What is "
                "the answer?",
        "options": [
            {"text": "Yes, above about a thousand degrees",
             "correct": False,
             "why": "No temperature a chemist can reach makes an atom. Heat "
                    "breaks and makes joins, and stops there"},
            {"text": "Yes, but only inside a sealed flask",
             "correct": False,
             "why": "A sealed flask keeps atoms in. It cannot conjure one up"},
            {"text": "No — chemistry rearranges atoms and makes none",
             "correct": True},
            {"text": "No, because every kind of atom has been made already",
             "correct": False,
             "why": "The reason is not that the set is full. It is that a "
                    "reaction has no way of making one"},
        ],
        "figure": None,
    },
    {
        "id": "c4-02-e15",
        "band": "easier",
        "text": "A reaction would need one more nitrogen atom than the flask "
                "contains. What happens?",
        "options": [
            {"text": "The reaction borrows one from the glass of the flask",
             "correct": False,
             "why": "Glass is not made of nitrogen, and a reaction cannot take "
                    "atoms out of its container"},
            {"text": "The reaction makes the missing atom as it goes",
             "correct": False,
             "why": "Nothing a reaction does makes an atom. A missing atom "
                    "stays missing"},
            {"text": "The reaction runs more slowly until one turns up",
             "correct": False,
             "why": "Waiting supplies nothing. There is no source for an atom "
                    "that is not in the flask"},
            {"text": "That reaction cannot happen in the flask",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c4-02-e16",
        "band": "easier",
        "text": "Steel wool is burned in air and turns into a heavier dark "
                "solid. Where did the atoms that made it heavier come from?",
        "options": [
            {"text": "From the oxygen in the air",
             "correct": True},
            {"text": "From the heat of the flame",
             "correct": False,
             "why": "Heat carries no atoms. What joined the iron came out of "
                    "the air"},
            {"text": "From the iron atoms swelling up",
             "correct": False,
             "why": "An atom does not swell. The extra mass is extra atoms"},
            {"text": "From new atoms made in the burning",
             "correct": False,
             "why": "Burning makes no atoms. It joins the ones already there"},
        ],
        "figure": None,
    },
    {
        "id": "c4-02-e17",
        "band": "easier",
        "text": "What does a catalyst change about a reaction?",
        "options": [
            {"text": "Which kinds of atom it has to work with",
             "correct": False,
             "why": "Nothing changes that except what you put in. A catalyst "
                    "adds no atoms to the products"},
            {"text": "How many atoms come out",
             "correct": False,
             "why": "The count of each kind is fixed by what went in, catalyst "
                    "or no catalyst"},
            {"text": "How fast the reaction goes",
             "correct": True},
            {"text": "Whether atoms are created or destroyed",
             "correct": False,
             "why": "Neither happens in any reaction, so there is nothing here "
                    "for a catalyst to change"},
        ],
        "figure": None,
    },
    {
        "id": "c4-02-e18",
        "band": "easier",
        "text": "Which of these substances is an element?",
        "options": [
            {"text": "Water",
             "correct": False,
             "why": "Water holds hydrogen and oxygen, so it is a compound"},
            {"text": "Sulfur",
             "correct": True},
            {"text": "Carbon dioxide",
             "correct": False,
             "why": "Carbon dioxide holds carbon and oxygen, so it is a "
                    "compound"},
            {"text": "Magnesium oxide",
             "correct": False,
             "why": "Its name gives away two kinds of atom, so it is a "
                    "compound"},
        ],
        "figure": None,
    },
    {
        "id": "c4-02-e19",
        "band": "easier",
        "text": "Twenty carbon atoms are sealed in a flask and a reaction is "
                "run. How many carbon atoms are in the flask afterwards?",
        "options": [
            {"text": "Twenty",
             "correct": True},
            {"text": "Fewer than twenty",
             "correct": False,
             "why": "Used up means joined to something else. All twenty are "
                    "still in the flask"},
            {"text": "More than twenty",
             "correct": False,
             "why": "A new substance is a new arrangement of the same atoms, "
                    "not extra ones"},
            {"text": "It cannot be known",
             "correct": False,
             "why": "Nothing can get in or out, so the count is known without "
                    "opening anything"},
        ],
        "figure": None,
    },
    {
        "id": "c4-02-e20",
        "band": "easier",
        "text": "Sodium chloride is built from sodium atoms and chlorine "
                "atoms joined together. What does that make it?",
        "options": [
            {"text": "A mixture",
             "correct": False,
             "why": "The atoms are chemically joined here, and in a mixture "
                    "they are not"},
            {"text": "An element",
             "correct": False,
             "why": "An element holds one kind of atom, and this holds two "
                    "kinds"},
            {"text": "A compound",
             "correct": True},
            {"text": "A new kind of atom",
             "correct": False,
             "why": "There is no sodium chloride atom. Both kinds of atom are "
                    "still themselves"},
        ],
        "figure": None,
    },
    {
        "id": "c4-02-e21",
        "band": "easier",
        "text": "What is it about an atom that a chemical reaction changes?",
        "options": [
            {"text": "The size of each atom",
             "correct": False,
             "why": "An atom is the same size before and after. Only its "
                    "partners change"},
            {"text": "The kind of each atom",
             "correct": False,
             "why": "Changing one kind into another is nuclear, not chemical"},
            {"text": "The number of atoms",
             "correct": False,
             "why": "The count of each kind is identical on both sides"},
            {"text": "What each atom is joined to",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c4-02-e22",
        "band": "easier",
        "text": "A log burns away on a fire until only a little ash is left. "
                "What happened to the atoms that were in the log?",
        "options": [
            {"text": "They went into the ash, the smoke and the gases given "
                     "off",
             "correct": True},
            {"text": "They were destroyed by the heat of the fire",
             "correct": False,
             "why": "Fire destroys no atoms. It rearranges them into "
                    "substances that mostly float away"},
            {"text": "They turned into the heat and the light you could see",
             "correct": False,
             "why": "Heat and light are energy, and energy is not made of "
                    "atoms"},
            {"text": "They shrank down into the small pile of ash",
             "correct": False,
             "why": "Atoms do not shrink. Most of them left as gas, which is "
                    "why so little is left"},
        ],
        "figure": None,
    },
    {
        "id": "c4-02-e23",
        "band": "easier",
        "text": "What does a chemist mean by saying a reactant has been used "
                "up?",
        "options": [
            {"text": "Its atoms have been destroyed by the reaction",
             "correct": False,
             "why": "Nothing destroys an atom in chemistry. They are still "
                    "there, in the products"},
            {"text": "Its atoms are now part of something else",
             "correct": True},
            {"text": "Its atoms have escaped into the air above the flask",
             "correct": False,
             "why": "That would describe a gas leaving an open dish, which is "
                    "a different thing altogether"},
            {"text": "Its atoms have turned into a different kind of atom",
             "correct": False,
             "why": "No atom changes kind. It simply has new partners"},
        ],
        "figure": None,
    },
    {
        "id": "c4-02-e24",
        "band": "easier",
        "text": "A flask holds carbon atoms and oxygen atoms and nothing "
                "else. Which substance could the reaction never produce?",
        "options": [
            {"text": "Carbon monoxide",
             "correct": False,
             "why": "One carbon joined to one oxygen, and the flask holds both "
                    "kinds"},
            {"text": "Carbon dioxide",
             "correct": False,
             "why": "One carbon and two oxygens, and the flask holds both "
                    "kinds"},
            {"text": "Oxygen gas",
             "correct": False,
             "why": "Oxygen atoms joined in pairs, and there are oxygen atoms "
                    "in the flask"},
            {"text": "Water",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c4-02-e25",
        "band": "easier",
        "text": "Two substances react and a brand new substance appears. What "
                "has actually been made?",
        "options": [
            {"text": "New matter, which is where the new substance comes from",
             "correct": False,
             "why": "No matter is made. The new substance is old atoms with "
                    "new partners"},
            {"text": "New kinds of atom, one for each new substance",
             "correct": False,
             "why": "Chemistry mints no atoms. The kinds present are the kinds "
                    "you supplied"},
            {"text": "New joins between atoms that were there already",
             "correct": True},
            {"text": "New atoms, built out of the energy the reaction used",
             "correct": False,
             "why": "Energy starts and drives reactions. It never turns into "
                    "an atom"},
        ],
        "figure": None,
    },
    {
        "id": "c4-02-e26",
        "band": "easier",
        "text": "Copper oxide is heated with carbon and copper metal appears. "
                "Where did the copper atoms come from?",
        "options": [
            {"text": "The carbon, which turned into copper in the heat",
             "correct": False,
             "why": "Carbon cannot become copper. That would be a change of "
                    "element, which chemistry cannot do"},
            {"text": "They were in the copper oxide before it was heated",
             "correct": True},
            {"text": "The flame, which supplied them as it burned",
             "correct": False,
             "why": "A flame supplies energy and its own waste gases, and no "
                    "copper at all"},
            {"text": "They formed as the black powder broke into pieces",
             "correct": False,
             "why": "Breaking a powder into pieces makes smaller pieces of the "
                    "same substance, not new atoms"},
        ],
        "figure": None,
    },
    {
        "id": "c4-02-e27",
        "band": "easier",
        "text": "An oxygen atom is part of a water particle. Is it the same "
                "kind of atom as an oxygen atom in the air?",
        "options": [
            {"text": "No, because it has taken on the properties of water",
             "correct": False,
             "why": "An atom does not take on the properties of what it is in. "
                    "That is the copper mistake in another coat"},
            {"text": "No, because joining changes an atom into a new kind",
             "correct": False,
             "why": "Joining changes partners and nothing else about the atom"},
            {"text": "Yes, it is exactly the same kind of atom",
             "correct": True},
            {"text": "Yes, but only while the water stays cold",
             "correct": False,
             "why": "Temperature has nothing to do with what kind an atom is"},
        ],
        "figure": None,
    },
    {
        "id": "c4-02-e28",
        "band": "easier",
        "text": "Why can a chemist be sure that burning a candle does not "
                "destroy any atoms?",
        "options": [
            {"text": "Because the wax is a soft substance that cannot hold "
                     "atoms tightly",
             "correct": False,
             "why": "How hard or soft a substance is decides nothing about its "
                    "atoms"},
            {"text": "Because no chemical reaction destroys an atom",
             "correct": True},
            {"text": "Because the flame is not hot enough to destroy one",
             "correct": False,
             "why": "There is no temperature at which a flame destroys atoms"},
            {"text": "Because candle wax is made of only one kind of atom",
             "correct": False,
             "why": "Wax holds carbon and hydrogen, and the argument would not "
                    "depend on that anyway"},
        ],
        "figure": None,
    },
    {
        "id": "c4-02-e29",
        "band": "easier",
        "text": "Hydrogen peroxide breaks down into water and oxygen. Which "
                "kinds of atom can be in those two products?",
        "options": [
            {"text": "Hydrogen and oxygen, and nothing else",
             "correct": True},
            {"text": "Hydrogen, oxygen and a little carbon from the air",
             "correct": False,
             "why": "Nothing from outside joins in here, and carbon was never "
                    "in the peroxide"},
            {"text": "Whichever kinds the two products happen to need",
             "correct": False,
             "why": "A product is built from what was there. Needing a kind of "
                    "atom does not supply it"},
            {"text": "New kinds, because two substances came from one",
             "correct": False,
             "why": "One substance can break into two without a single new "
                    "kind of atom appearing"},
        ],
        "figure": None,
    },
    {
        "id": "c4-02-e30",
        "band": "easier",
        "text": "Which statement about the atoms in a compound is right?",
        "options": [
            {"text": "They are joined together and are still the atoms they "
                     "were",
             "correct": True},
            {"text": "They have merged into one bigger atom of the compound",
             "correct": False,
             "why": "Atoms do not merge. A compound is joined atoms, each one "
                    "still itself"},
            {"text": "They are loosely mixed and can be picked apart by hand",
             "correct": False,
             "why": "That describes a mixture. A compound's atoms are "
                    "chemically joined"},
            {"text": "They have each lost a small part of themselves to the "
                     "join",
             "correct": False,
             "why": "A chemical join takes no piece out of an atom"},
        ],
        "figure": None,
    },
    {
        "id": "c4-02-e31",
        "band": "easier",
        "text": "Why does a chemist say that a reaction has a budget of "
                "atoms?",
        "options": [
            {"text": "Because atoms are expensive and must not be wasted",
             "correct": False,
             "why": "Cost has nothing to do with it. The limit is what is "
                    "physically there"},
            {"text": "Because the products can hold only the atoms that went "
                     "in",
             "correct": True},
            {"text": "Because a reaction is allowed to use half of them",
             "correct": False,
             "why": "There is no such rule. A reaction may use all of them"},
            {"text": "Because the budget can be topped up by heating it",
             "correct": False,
             "why": "Heating supplies energy, and the atom count is untouched "
                    "by it"},
        ],
        "figure": None,
    },
    {
        "id": "c4-02-e32",
        "band": "easier",
        "text": "Zinc is added to copper sulfate solution, and copper appears "
                "while the zinc disappears. What happened to the zinc atoms?",
        "options": [
            {"text": "They were destroyed and copper atoms took their place",
             "correct": False,
             "why": "No atom is destroyed. The zinc atoms are in the solution "
                    "now, joined to the sulfate"},
            {"text": "They turned into copper atoms in the solution",
             "correct": False,
             "why": "One element cannot become another in a reaction. The "
                    "copper atoms were in the blue solution already"},
            {"text": "They went into the solution with new partners",
             "correct": True},
            {"text": "They sank to the bottom under the new copper",
             "correct": False,
             "why": "There is no zinc metal left at the bottom. The zinc "
                    "dissolved as part of a compound"},
        ],
        "figure": None,
    },

    # ── standard · MRB-338 top-up ───────────────────────────────────────
    {
        "id": "c4-02-s11",
        "band": "standard",
        "text": "Ammonia is one nitrogen atom joined to three hydrogen atoms. "
                "A flask holds six nitrogen atoms and twenty-one hydrogen "
                "atoms. What is the most ammonia that can be built?",
        "options": [
            {"text": "Six particles, with three hydrogen atoms left over",
             "correct": True},
            {"text": "Seven particles, because there are twenty-one hydrogens "
                     "and each one takes three",
             "correct": False,
             "why": "The hydrogens would stretch to seven, and there are only "
                    "six nitrogen atoms to go round"},
            {"text": "Twenty-one particles, one for each hydrogen atom",
             "correct": False,
             "why": "Each particle swallows three hydrogen atoms rather than "
                    "one"},
            {"text": "Nine particles, once the leftover atoms have joined up",
             "correct": False,
             "why": "Leftover hydrogen atoms cannot make ammonia on their own. "
                    "Every particle needs a nitrogen"},
        ],
        "figure": None,
    },
    {
        "id": "c4-02-s12",
        "band": "standard",
        "text": "Black copper oxide is heated with hydrogen. Copper metal and "
                "water are left. Where have the oxygen atoms gone?",
        "options": [
            {"text": "They were driven off as oxygen gas and lost into the room air",
             "correct": False,
             "why": "No oxygen gas is collected here. The oxygen left joined "
                    "to hydrogen, as water"},
            {"text": "They stayed in the copper, which is why it is a metal",
             "correct": False,
             "why": "The copper is copper alone. Any oxygen still joined to it "
                    "would leave it black"},
            {"text": "They are in the water, joined to hydrogen atoms",
             "correct": True},
            {"text": "They were destroyed, which is what removing them means",
             "correct": False,
             "why": "Removing an atom from a compound gives it a new partner. "
                    "It does not end the atom"},
        ],
        "figure": None,
    },
    {
        "id": "c4-02-s13",
        "band": "standard",
        "text": "Iron filings and sulfur are heated together and make a grey "
                "solid a magnet cannot pull apart. What has happened to the "
                "iron atoms?",
        "options": [
            {"text": "They have lost the part of them that a magnet pulls on",
             "correct": False,
             "why": "A chemical reaction takes no piece out of an atom. What "
                    "changed is the substance the atoms are in"},
            {"text": "They have become atoms of a brand new element that is "
                     "called iron sulfide",
             "correct": False,
             "why": "Iron sulfide is a compound, not an element. There is no "
                    "iron sulfide atom"},
            {"text": "They have been used up, so only sulfur is left in the "
                     "solid",
             "correct": False,
             "why": "Both kinds of atom are in the solid, in equal numbers"},
            {"text": "They are joined to sulfur atoms, and are still iron "
                     "atoms",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c4-02-s14",
        "band": "standard",
        "text": "Ethanol is built from carbon, hydrogen and oxygen atoms. It "
                "is burned in plenty of air. Which pair of products is "
                "possible?",
        "options": [
            {"text": "Carbon dioxide and water vapour",
             "correct": True},
            {"text": "Carbon dioxide and ammonia",
             "correct": False,
             "why": "Ammonia needs nitrogen, and neither the ethanol nor the "
                    "oxygen supplies one"},
            {"text": "Sulfur dioxide and water vapour",
             "correct": False,
             "why": "Sulfur dioxide needs sulfur, and there is none in the "
                    "ethanol"},
            {"text": "Methane and oxygen",
             "correct": False,
             "why": "Both of those are fuels or reactants here, and burning "
                    "makes neither"},
        ],
        "figure": None,
    },
    {
        "id": "c4-02-s15",
        "band": "standard",
        "text": "Iron sulfide is one iron atom joined to one sulfur atom. A "
                "tube holds eight iron atoms and five sulfur atoms. How much "
                "iron sulfide can be made?",
        "options": [
            {"text": "Eight units, with the sulfur atoms shared between them",
             "correct": False,
             "why": "A sulfur atom cannot be in two units at once. Five "
                    "sulfurs make five units"},
            {"text": "Five units, with three iron atoms left over",
             "correct": True},
            {"text": "Thirteen units, one for every atom in the tube",
             "correct": False,
             "why": "Each unit takes two atoms, one of each kind"},
            {"text": "Eight units, because the iron sets the number",
             "correct": False,
             "why": "The atom that runs out first sets the number, and here "
                    "that is sulfur"},
        ],
        "figure": None,
    },
    {
        "id": "c4-02-s16",
        "band": "standard",
        "text": "Two colourless solutions are mixed and a bright yellow solid "
                "settles out. Has a new kind of atom been made?",
        "options": [
            {"text": "Yes, because nothing yellow was there beforehand",
             "correct": False,
             "why": "Colour belongs to a substance rather than to an atom. New "
                    "colour means new partners"},
            {"text": "Yes, because a solid came out of two liquids",
             "correct": False,
             "why": "A change of state or of substance makes no atom. The "
                    "atoms were dissolved before"},
            {"text": "No, because the two solutions were colourless",
             "correct": False,
             "why": "The colour before tells you nothing about the atoms. The "
                    "reason is that reactions make no atoms"},
            {"text": "No — the atoms were all in the two solutions already",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c4-02-s17",
        "band": "standard",
        "text": "A student says the reaction destroyed the acid, because the "
                "acid is gone from the flask. What is the better way to say "
                "it?",
        "options": [
            {"text": "The acid reacted, so its atoms are now in the products",
             "correct": True},
            {"text": "The acid evaporated into the room during the reaction",
             "correct": False,
             "why": "Evaporating is a different event, and it would not "
                    "explain the new substances in the flask"},
            {"text": "The acid turned into energy as the reaction warmed up",
             "correct": False,
             "why": "No substance turns into energy in a chemical reaction. "
                    "Its atoms go into the products"},
            {"text": "The acid was broken down into smaller pieces of atom by "
                     "the water",
             "correct": False,
             "why": "Chemistry does not break atoms into pieces. It changes "
                    "what they are joined to"},
        ],
        "figure": None,
    },
    {
        "id": "c4-02-s18",
        "band": "standard",
        "text": "Carbon burns in a poor supply of air and makes carbon "
                "monoxide, one carbon joined to one oxygen, instead of carbon "
                "dioxide. Does that break the rule about atoms?",
        "options": [
            {"text": "Yes, because one of the oxygen atoms has gone missing from "
                     "the tube",
             "correct": False,
             "why": "None has gone missing. There were fewer oxygen atoms "
                    "available in the first place"},
            {"text": "No — the same atoms are joined up in a different way",
             "correct": True},
            {"text": "Yes, because a new substance has appeared from nowhere",
             "correct": False,
             "why": "Carbon monoxide is built entirely from carbon and oxygen "
                    "atoms that were there"},
            {"text": "No, because carbon monoxide has no oxygen in it",
             "correct": False,
             "why": "It holds one oxygen atom per carbon. The name says so"},
        ],
        "figure": None,
    },
    {
        "id": "c4-02-s19",
        "band": "standard",
        "text": "Two gases react and the product runs down the side of the "
                "flask as a liquid. How can a liquid come out of two gases?",
        "options": [
            {"text": "The gases were squeezed together hard enough to go "
                     "liquid",
             "correct": False,
             "why": "That would be a change of state and no reaction. The "
                    "product here is a different substance"},
            {"text": "One of the gases was really a liquid in disguise",
             "correct": False,
             "why": "Nothing is in disguise. Both reactants were gases and the "
                    "product is not either of them"},
            {"text": "New atoms formed that are heavier than the old ones",
             "correct": False,
             "why": "No atom is made and no atom changes mass. Only the "
                    "arrangement is new"},
            {"text": "The same atoms are joined differently, and the new "
                     "substance is a liquid",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c4-02-s20",
        "band": "standard",
        "text": "A factory wants to make a fertiliser containing nitrogen. "
                "What does that tell the chemists about the reactants they "
                "must buy?",
        "options": [
            {"text": "At least one reactant has to contain nitrogen atoms",
             "correct": True},
            {"text": "The reaction has to be run at a high enough pressure",
             "correct": False,
             "why": "Pressure changes how well a reaction runs. It supplies no "
                    "nitrogen"},
            {"text": "A catalyst has to be chosen that will supply the "
                     "nitrogen",
             "correct": False,
             "why": "A catalyst speeds a reaction up without adding atoms to "
                    "the product"},
            {"text": "The reactants have to be heated until nitrogen appears",
             "correct": False,
             "why": "Heating never produces an atom that was not there"},
        ],
        "figure": None,
    },
    {
        "id": "c4-02-s21",
        "band": "standard",
        "text": "Explain why a compound can have properties that neither of "
                "the elements in it has.",
        "options": [
            {"text": "Because the atoms in it are joined up in a new "
                     "arrangement",
             "correct": True},
            {"text": "Because the atoms in it have changed into new kinds of "
                     "atom",
             "correct": False,
             "why": "No atom changes kind. The elements are still there, with "
                    "new partners"},
            {"text": "Because the properties of the elements are destroyed by "
                     "the reaction",
             "correct": False,
             "why": "Nothing is destroyed. A property belongs to a substance, "
                    "and the substance is new"},
            {"text": "Because a compound holds a third element that is hidden "
                     "inside it",
             "correct": False,
             "why": "A compound holds exactly the kinds of atom its name "
                    "gives, and nothing hidden"},
        ],
        "figure": None,
    },
    {
        "id": "c4-02-s22",
        "band": "standard",
        "text": "Three carbon atoms and four oxygen atoms sit in a sealed "
                "tube. Carbon dioxide is one carbon joined to two oxygens. "
                "How many particles of it can be made?",
        "options": [
            {"text": "Three, because there are three carbon atoms",
             "correct": False,
             "why": "Three particles would need six oxygen atoms, and there "
                    "are four"},
            {"text": "Four, because there are four oxygen atoms",
             "correct": False,
             "why": "Each particle swallows two oxygen atoms, so four oxygens "
                    "reach two particles"},
            {"text": "Two, with one carbon atom left over",
             "correct": True},
            {"text": "Seven, one for each atom in the tube",
             "correct": False,
             "why": "Each particle is built from three atoms, so counting "
                    "atoms counts nothing useful here"},
        ],
        "figure": None,
    },
    {
        "id": "c4-02-s23",
        "band": "standard",
        "text": "A candle burns and the glass above it mists up. Which atoms "
                "from the wax have ended up in that mist?",
        "options": [
            {"text": "The carbon atoms, which make the mist look white",
             "correct": False,
             "why": "The carbon leaves as carbon dioxide. The mist is water, "
                    "and it is colourless"},
            {"text": "The hydrogen atoms, joined now to oxygen from the air",
             "correct": True},
            {"text": "None of them, because the mist came out of the air",
             "correct": False,
             "why": "The air supplied the oxygen, and the hydrogen in the "
                    "water came out of the wax"},
            {"text": "All of them, because everything in the wax rises",
             "correct": False,
             "why": "The carbon atoms leave as a gas instead, so the mist "
                    "holds only some of them"},
        ],
        "figure": None,
    },
    {
        "id": "c4-02-s24",
        "band": "standard",
        "text": "Vinegar is poured on baking powder and the mixture fizzes. "
                "Where did the atoms in the gas come from?",
        "options": [
            {"text": "From the air above the bowl, pulled down into it by the "
                     "fizzing",
             "correct": False,
             "why": "The gas comes out of the mixture rather than into it. Air "
                    "is not a reactant here"},
            {"text": "From the vinegar and the powder, rearranged",
             "correct": True},
            {"text": "They were made by the reaction as the bubbles formed",
             "correct": False,
             "why": "A bubble is a new arrangement of old atoms. Nothing about "
                    "it makes matter"},
            {"text": "From the water in the vinegar, which broke into gas",
             "correct": False,
             "why": "Water turning to gas would be boiling, and this happens "
                    "cold and gives a different gas"},
        ],
        "figure": None,
    },
    {
        "id": "c4-02-s25",
        "band": "standard",
        "text": "Which of these is beyond anything a chemical reaction can "
                "do?",
        "options": [
            {"text": "Make a coloured solid out of two colourless liquids",
             "correct": False,
             "why": "A new arrangement can easily have a colour neither "
                    "reactant had"},
            {"text": "Turn one element into a different element",
             "correct": True},
            {"text": "Make two substances out of one substance",
             "correct": False,
             "why": "That is a breakdown reaction, and the atoms simply split "
                    "into two groups"},
            {"text": "Make a gas out of two solids pressed together",
             "correct": False,
             "why": "Solids can react to give a gas. The atoms for it were in "
                    "the solids"},
        ],
        "figure": None,
    },
    {
        "id": "c4-02-s26",
        "band": "standard",
        "text": "Hydrogen sulfide is two hydrogen atoms joined to one sulfur "
                "atom. A flask holds ten hydrogen atoms and six sulfur atoms. "
                "How many particles can be built?",
        "options": [
            {"text": "Six, because the sulfur atoms decide it",
             "correct": False,
             "why": "Six particles would need twelve hydrogen atoms, and there "
                    "are ten"},
            {"text": "Ten, one for each hydrogen atom",
             "correct": False,
             "why": "Each particle takes two hydrogen atoms rather than one"},
            {"text": "Sixteen, one for every atom present",
             "correct": False,
             "why": "Each particle is built from three atoms, so the atom "
                    "total is not the answer"},
            {"text": "Five, with one sulfur atom left over",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c4-02-s27",
        "band": "standard",
        "text": "A student says a reaction that gives off a gas has lost some "
                "of its atoms. What is the correction?",
        "options": [
            {"text": "The atoms have left the flask, and they still exist in "
                     "the gas",
             "correct": True},
            {"text": "The atoms turned into gas, which is a form of energy",
             "correct": False,
             "why": "A gas is matter made of atoms. Energy is not, and one is "
                    "not the other"},
            {"text": "The atoms were lost, as gases are hard to weigh",
             "correct": False,
             "why": "A gas can be weighed, and nothing about being a gas loses "
                    "an atom"},
            {"text": "The atoms were used up in making the bubbles rise",
             "correct": False,
             "why": "Rising costs no atoms. The bubbles are made of them"},
        ],
        "figure": None,
    },
    {
        "id": "c4-02-s28",
        "band": "standard",
        "text": "Limestone is heated and gives off carbon dioxide, leaving "
                "quicklime behind. Which kinds of atom must the limestone "
                "have contained?",
        "options": [
            {"text": "Only calcium, because quicklime is a calcium compound",
             "correct": False,
             "why": "The carbon dioxide had to come from somewhere too, so "
                    "carbon and oxygen were in there as well"},
            {"text": "Calcium and carbon, but not oxygen",
             "correct": False,
             "why": "Carbon dioxide is mostly oxygen by count. Those atoms "
                    "were in the limestone"},
            {"text": "Calcium, carbon and oxygen",
             "correct": True},
            {"text": "Whichever kinds the heating happened to produce",
             "correct": False,
             "why": "Heating produces no kinds of atom. Everything in the "
                    "products was in the limestone"},
        ],
        "figure": None,
    },
    {
        "id": "c4-02-s29",
        "band": "standard",
        "text": "A chemist is offered a powder said to turn into silver when "
                "it is heated hard enough. What should be asked first?",
        "options": [
            {"text": "How hot the furnace would have to be",
             "correct": False,
             "why": "Temperature is not the question. No temperature makes a "
                    "silver atom"},
            {"text": "How long the heating would have to go on for",
             "correct": False,
             "why": "Time cannot supply an atom that the powder does not "
                    "contain"},
            {"text": "Whether the powder contains silver atoms already",
             "correct": True},
            {"text": "Whether a catalyst would make the change go faster",
             "correct": False,
             "why": "A catalyst changes the rate of a reaction that can "
                    "happen, and this one cannot"},
        ],
        "figure": None,
    },
    {
        "id": "c4-02-s30",
        "band": "standard",
        "text": "Explain why a chemist can predict which kinds of atom will "
                "be in the products before running a reaction at all.",
        "options": [
            {"text": "Because the products can hold only the kinds that were "
                     "in the reactants",
             "correct": True},
            {"text": "Because the products contain fewer kinds than the "
                     "reactants",
             "correct": False,
             "why": "The kinds are the same on both sides. Nothing drops out "
                    "of existence"},
            {"text": "Because a reaction chooses the simplest substances it "
                     "can build",
             "correct": False,
             "why": "Plenty of reactions build complicated products. The limit "
                    "is which atoms are there"},
            {"text": "Because heating decides which kinds of atom will appear "
                     "in them",
             "correct": False,
             "why": "Heating decides whether the reaction runs, and never "
                    "which kinds of atom exist"},
        ],
        "figure": None,
    },
    {
        "id": "c4-02-s31",
        "band": "standard",
        "text": "Sherbet fizzes on the tongue as two powders react in the "
                "water of your mouth. Which statement about the atoms is "
                "right?",
        "options": [
            {"text": "New atoms are made, and the fizzing feeling is those atoms "
                     "arriving",
             "correct": False,
             "why": "The feeling is a gas escaping. Nothing about it makes an "
                    "atom"},
            {"text": "The atoms of the powders are destroyed as they "
                     "dissolve",
             "correct": False,
             "why": "Dissolving separates particles and destroys nothing"},
            {"text": "Every atom in the gas came from the powders or the "
                     "water",
             "correct": True},
            {"text": "The water supplies extra atoms of its own making",
             "correct": False,
             "why": "The water may take part, and the atoms it brings were in "
                    "the water already"},
        ],
        "figure": None,
    },
    {
        "id": "c4-02-s32",
        "band": "standard",
        "text": "Why is a reaction that produces a completely new substance "
                "still not producing new matter?",
        "options": [
            {"text": "Because the new substance is only a new arrangement of "
                     "old atoms",
             "correct": True},
            {"text": "Because the new substance weighs the same as one "
                     "reactant",
             "correct": False,
             "why": "It usually does not, and the argument does not rest on "
                    "any one mass"},
            {"text": "Because new matter can be made, though not inside a school "
                     "laboratory",
             "correct": False,
             "why": "No laboratory of any size makes matter with a chemical "
                    "reaction"},
            {"text": "Because the new substance can be turned back again "
                     "afterwards",
             "correct": False,
             "why": "Plenty of reactions cannot be reversed, and the rule "
                    "holds for those too"},
        ],
        "figure": None,
    },

    # ── harder · MRB-338 top-up ─────────────────────────────────────────
    {
        "id": "c4-02-h11",
        "band": "harder",
        "text": "A tube holds ten nitrogen atoms and twenty-four hydrogen "
                "atoms. Ammonia is one nitrogen joined to three hydrogens. As "
                "much ammonia as possible is made. What is left over?",
        "options": [
            {"text": "Two nitrogen atoms",
             "correct": True},
            {"text": "Six hydrogen atoms, since the nitrogen runs out first "
                     "and leaves the spare hydrogen with nothing to join",
             "correct": False,
             "why": "The hydrogen runs out first: twenty-four of them build "
                    "eight particles, and that uses only eight nitrogens"},
            {"text": "Nothing at all",
             "correct": False,
             "why": "Ten nitrogens would need thirty hydrogen atoms, and there "
                    "are twenty-four"},
            {"text": "Two nitrogen atoms and six hydrogen atoms",
             "correct": False,
             "why": "Every hydrogen atom is used. Eight particles take exactly "
                    "twenty-four of them"},
        ],
        "figure": None,
    },
    {
        "id": "c4-02-h12",
        "band": "harder",
        "text": "Sand is built from silicon and oxygen. A company says it can "
                "get silicon metal out of sand. Is that claim the same kind of "
                "claim as making gold from lead?",
        "options": [
            {"text": "Yes, because both ask for a metal that is not there to "
                     "start with",
             "correct": False,
             "why": "The silicon IS there to start with, joined to oxygen. "
                    "Only the gold claim asks for an atom that is missing"},
            {"text": "No — the silicon atoms are in the sand already, so only "
                     "the joins have to change",
             "correct": True},
            {"text": "Yes, because sand is a compound and compounds cannot be "
                     "taken apart",
             "correct": False,
             "why": "Compounds are taken apart every day in industry. That is "
                    "what a reduction reaction does"},
            {"text": "No, because sand is an element and gold is a compound",
             "correct": False,
             "why": "Both descriptions are the wrong way round. Gold is the "
                    "element and sand is the compound"},
        ],
        "figure": None,
    },
    {
        "id": "c4-02-h13",
        "band": "harder",
        "text": "A reaction in a sealed flask makes the pressure inside rise. "
                "A student says extra atoms must have been made. What is the "
                "best answer?",
        "options": [
            {"text": "The same atoms are now in more separate particles, and "
                     "many of them are gas",
             "correct": True},
            {"text": "The flask has warmed up, and that is what raises a "
                     "pressure",
             "correct": False,
             "why": "Warming does raise pressure and it is not the only cause. "
                    "Here a solid has given off a gas"},
            {"text": "Extra atoms really are made whenever a gas is produced "
                     "inside a sealed container",
             "correct": False,
             "why": "A gas is made of atoms that were already in the flask, "
                    "arranged into separate particles"},
            {"text": "The atoms have grown larger, which leaves them less room "
                     "in the flask than before",
             "correct": False,
             "why": "An atom is the same size throughout. What changed is how "
                    "the atoms are grouped"},
        ],
        "figure": None,
    },
    {
        "id": "c4-02-h14",
        "band": "harder",
        "text": "A power station burns coal that contains sulfur, and sulfur "
                "dioxide comes out of the chimney. Why can no change of "
                "furnace conditions stop it forming?",
        "options": [
            {"text": "Because burning hotter would only make the reaction go "
                     "faster and produce the gas sooner than before",
             "correct": False,
             "why": "Rate is not the issue. The gas would form at any rate the "
                    "furnace ran at"},
            {"text": "Because sulfur dioxide is the one substance sulfur is "
                     "able to form in a furnace",
             "correct": False,
             "why": "Sulfur forms many compounds. The point is that its atoms "
                    "are in the coal and have to go somewhere"},
            {"text": "Because the sulfur atoms are in the coal, and conditions "
                     "cannot remove an atom",
             "correct": True},
            {"text": "Because the chimney supplies the oxygen the sulfur "
                     "needs",
             "correct": False,
             "why": "The oxygen comes from the air fed to the fire. The reason "
                    "is the sulfur in the fuel"},
        ],
        "figure": None,
    },
    {
        "id": "c4-02-h15",
        "band": "harder",
        "text": "A fuel burns and the only products are carbon dioxide and "
                "steam. Which two "
                "kinds of atom must the fuel have contained?",
        "options": [
            {"text": "Carbon and hydrogen",
             "correct": True},
            {"text": "Carbon and oxygen",
             "correct": False,
             "why": "The oxygen may all have come from the air, so it is not "
                    "one the fuel must have held"},
            {"text": "Hydrogen and oxygen",
             "correct": False,
             "why": "That would account for the water and leave the carbon in "
                    "the carbon dioxide unexplained"},
            {"text": "Carbon, hydrogen and oxygen",
             "correct": False,
             "why": "The fuel may contain oxygen, and it need not: the air can "
                    "supply all of it"},
        ],
        "figure": None,
    },
    {
        "id": "c4-02-h16",
        "band": "harder",
        "text": "One large particle is broken into two smaller ones in an oil "
                "refinery. Compare the number of atoms before and after.",
        "options": [
            {"text": "Fewer afterwards, because breaking a particle loses some "
                     "of the atoms that were holding it together in one piece",
             "correct": False,
             "why": "Breaking a particle breaks joins, not atoms. Every one of "
                    "them is in the two new particles"},
            {"text": "More afterwards, because there are now two particles "
                     "where there used to be one",
             "correct": False,
             "why": "The particle count doubled and the atom count did not. "
                    "The same atoms are shared between two groups"},
            {"text": "It depends on how hot the refinery runs the process",
             "correct": False,
             "why": "Conditions decide whether the break happens, never how "
                    "many atoms exist"},
            {"text": "The same number, shared between two particles instead of "
                     "one",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c4-02-h17",
        "band": "harder",
        "text": "A tablet sold for fish tanks is advertised as creating "
                "oxygen in the water. What must be true of the tablet if the "
                "advertisement works at all?",
        "options": [
            {"text": "It holds a substance with oxygen atoms in it",
             "correct": True},
            {"text": "It holds a catalyst strong enough to draw oxygen out of "
                     "the water it is dropped into",
             "correct": False,
             "why": "A catalyst adds no atoms. If the oxygen comes out of the "
                    "water, the water is the source and not the tablet"},
            {"text": "It holds enough stored energy to build oxygen atoms once "
                     "it begins to dissolve",
             "correct": False,
             "why": "Stored energy drives reactions and builds no atom of any "
                    "kind"},
            {"text": "It holds a metal that turns into oxygen as soon as it "
                     "meets the water in the tank",
             "correct": False,
             "why": "A metal cannot become oxygen. One element does not turn "
                    "into another in a reaction"},
        ],
        "figure": None,
    },
    {
        "id": "c4-02-h18",
        "band": "harder",
        "text": "Evaluate this claim: because a reaction makes no new atoms, "
                "it can never produce anything genuinely useful that did not "
                "exist before.",
        "options": [
            {"text": "Correct, because everything a reaction makes was in the "
                     "reactants",
             "correct": False,
             "why": "The ATOMS were present; the substance was not. A medicine "
                    "is new even though its atoms are old"},
            {"text": "Wrong — new arrangements are new substances, and that is "
                     "where new usefulness comes from",
             "correct": True},
            {"text": "Correct, because usefulness is a property of atoms "
                     "rather than a property of substances",
             "correct": False,
             "why": "Properties belong to substances. Carbon atoms sit in both "
                    "soot and diamond"},
            {"text": "Wrong, because a few reactions can make new atoms at "
                     "extreme conditions",
             "correct": False,
             "why": "No chemical reaction makes an atom at any conditions. The "
                    "claim fails for a different reason"},
        ],
        "figure": None,
    },
    {
        "id": "c4-02-h19",
        "band": "harder",
        "text": "A student reasons that because atoms are never created or "
                "destroyed, the number of PARTICLES must stay the same too. "
                "Where does the reasoning fail?",
        "options": [
            {"text": "It fails because atoms can be destroyed, so neither "
                     "count is safe to rely on in the first place",
             "correct": False,
             "why": "Atoms genuinely are conserved. The error is in the step "
                    "from atoms to particles"},
            {"text": "It fails because one particle can break into two, or two "
                     "can join into one",
             "correct": True},
            {"text": "It fails because particles are far too small for anybody "
                     "to be able to count them properly",
             "correct": False,
             "why": "Chemists count particles all the time. The objection is "
                    "that the number really does change"},
            {"text": "It does not fail: the number of particles is conserved "
                     "in every reaction",
             "correct": False,
             "why": "Two hydrogen particles and one oxygen particle give two "
                    "waters — three in, two out"},
        ],
        "figure": None,
    },
    {
        "id": "c4-02-h20",
        "band": "harder",
        "text": "On a spacecraft, carbon dioxide breathed out is passed over "
                "a chemical that takes it in, and oxygen is given back to the "
                "cabin. Where does that oxygen come from?",
        "options": [
            {"text": "It is made by the chemical out of the energy of the "
                     "reaction",
             "correct": False,
             "why": "Energy makes no atoms on a spacecraft or anywhere else"},
            {"text": "It is drawn in from outside the spacecraft through the "
                     "wall of the cabin",
             "correct": False,
             "why": "There is no oxygen outside to draw in, and the wall is "
                    "sealed"},
            {"text": "It comes from oxygen atoms already in the carbon dioxide "
                     "or in the chemical",
             "correct": True},
            {"text": "It is left behind when the carbon atoms are destroyed by "
                     "the chemical",
             "correct": False,
             "why": "The carbon atoms are held by the chemical, not destroyed. "
                    "Nothing destroys an atom"},
        ],
        "figure": None,
    },
    {
        "id": "c4-02-h21",
        "band": "harder",
        "text": "Two different pairs of reactants give exactly the same "
                "product. What must be true of both pairs?",
        "options": [
            {"text": "Both pairs must be made of the same substances under "
                     "two different names",
             "correct": False,
             "why": "Different substances can lead to one product. Only the "
                    "kinds of atom have to match"},
            {"text": "Both pairs must react at the same speed as each other",
             "correct": False,
             "why": "Rate has nothing to do with which atoms are present"},
            {"text": "Both pairs must be held at the same temperature while "
                     "they react",
             "correct": False,
             "why": "Conditions may differ freely. What cannot differ is the "
                    "atoms available"},
            {"text": "Both pairs must contain every kind of atom the product "
                     "contains",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c4-02-h22",
        "band": "harder",
        "text": "A battery is run flat and then recharged, and the reaction "
                "inside it goes back the way it came. What has happened to "
                "the atoms?",
        "options": [
            {"text": "Fresh atoms have been pushed in from the charger to "
                     "replace the ones the torch used while it was running",
             "correct": False,
             "why": "A charger supplies energy down a wire. It supplies no "
                    "atoms at all"},
            {"text": "The same atoms have been put back with their original "
                     "partners",
             "correct": True},
            {"text": "The atoms that were used up have been rebuilt inside the "
                     "battery from the energy that was supplied to it",
             "correct": False,
             "why": "Nothing was used up in the sense of ceasing to exist, and "
                    "energy rebuilds no atom"},
            {"text": "The atoms have changed into other kinds",
             "correct": False,
             "why": "No atom changes kind. Only which atoms are joined to "
                    "which has changed back"},
        ],
        "figure": None,
    },
    {
        "id": "c4-02-h23",
        "band": "harder",
        "text": "A student says that because burning gives out heat, some of "
                "the matter in the fuel must have turned into energy. What is "
                "the answer a chemist gives?",
        "options": [
            {"text": "The energy comes from the joins between atoms, and every "
                     "atom is still there",
             "correct": True},
            {"text": "The heat is stored inside the atoms of the fuel and is "
                     "released when they are broken open in the flame",
             "correct": False,
             "why": "Atoms are not broken open by a flame. The energy accounts "
                    "sit in the joins between them"},
            {"text": "A small part of the fuel is turned into heat, which is "
                     "why the ash left behind weighs less",
             "correct": False,
             "why": "The ash weighs less because gases left. No matter became "
                    "heat"},
            {"text": "The heat is matter in a very thin form",
             "correct": False,
             "why": "Heat is energy and is not made of matter at all"},
        ],
        "figure": None,
    },
    {
        "id": "c4-02-h24",
        "band": "harder",
        "text": "Fireworks burn with red, green and gold flames. A "
                "manufacturer is asked how the colours are produced. Which "
                "answer is the chemistry?",
        "options": [
            {"text": "The heat of the burning makes new kinds of atom, and "
                     "each new kind glows with a colour of its own",
             "correct": False,
             "why": "No new kind of atom is made. The colours come from metals "
                    "that were packed in"},
            {"text": "Different metal compounds are packed into the firework, "
                     "and each metal glows its own colour",
             "correct": True},
            {"text": "Ordinary gunpowder is burned at different temperatures, "
                     "and the temperature alone decides the colour seen",
             "correct": False,
             "why": "Temperature changes the brightness far more than the "
                    "colour. Which metal is present decides it"},
            {"text": "Coloured dyes are mixed into the powder and survive the "
                     "burning unchanged so that the colour shows",
             "correct": False,
             "why": "A dye would be destroyed as a substance in the flame. The "
                    "colour comes from the metal atoms themselves"},
        ],
        "figure": None,
    },
    {
        "id": "c4-02-h25",
        "band": "harder",
        "text": "Which observation is the strongest evidence that a reaction "
                "only rearranged the atoms it was given?",
        "options": [
            {"text": "The reaction gave out heat as it ran",
             "correct": False,
             "why": "Heat tells you about the joins. It says nothing about "
                    "which atoms exist"},
            {"text": "Every kind of atom in the products can be traced back to "
                     "one of the reactants",
             "correct": True},
            {"text": "The products look different from the reactants",
             "correct": False,
             "why": "A new appearance is expected either way, so it separates "
                    "nothing"},
            {"text": "The reaction went quickly once it had been started with "
                     "a flame",
             "correct": False,
             "why": "Speed is evidence about rate and about nothing else here"},
        ],
        "figure": None,
    },
    {
        "id": "c4-02-h26",
        "band": "harder",
        "text": "A chemist is asked to make water from carbon dioxide and "
                "hydrogen. Is the request possible in principle?",
        "options": [
            {"text": "No, because carbon dioxide holds no hydrogen of its own "
                     "to build the water with",
             "correct": False,
             "why": "The hydrogen is the other reactant. Between them the two "
                    "supply every atom water needs"},
            {"text": "No, because a gas cannot become a liquid product",
             "correct": False,
             "why": "Reactions change substances, and the new substance may "
                    "well be a liquid"},
            {"text": "Yes, and the carbon atoms would have to end up in some "
                     "other product",
             "correct": True},
            {"text": "Yes, and the carbon atoms would be destroyed in the "
                     "process of making the water",
             "correct": False,
             "why": "No atom is destroyed. The carbon has to leave in a "
                    "product of its own"},
        ],
        "figure": None,
    },
    {
        "id": "c4-02-h27",
        "band": "harder",
        "text": "A burnt match cannot be turned back into a fresh one. "
                "Which explanation of that is about the atoms?",
        "options": [
            {"text": "The atoms of the wood were destroyed by the flame, so "
                     "there is nothing left to rebuild the match out of",
             "correct": False,
             "why": "The atoms survive. They are in the ash, the smoke and the "
                    "gases that left"},
            {"text": "Most of the atoms left as gases and are now spread "
                     "through the room, so they cannot be gathered",
             "correct": True},
            {"text": "The atoms changed into other kinds as the match burned, "
                     "and there is no way of changing them back",
             "correct": False,
             "why": "No atom changed kind. Only the partners changed"},
            {"text": "The atoms are all still in the burnt match and have been "
                     "locked in a shape that cannot be undone",
             "correct": False,
             "why": "The burnt match holds only a small part of them. Most of "
                    "the mass left as gas"},
        ],
        "figure": None,
    },
    {
        "id": "c4-02-h28",
        "band": "harder",
        "text": "A student writes that heating a carbonate creates carbon "
                "dioxide. Rewrite the claim so that it is true of the atoms.",
        "options": [
            {"text": "Heating the carbonate makes carbon dioxide out of the "
                     "energy it is given",
             "correct": False,
             "why": "Energy builds no atoms. The gas is built from atoms that "
                    "were in the solid"},
            {"text": "Heating the carbonate turns some of its atoms into "
                     "carbon and oxygen atoms",
             "correct": False,
             "why": "The carbon and oxygen atoms were there from the start. No "
                    "atom was turned into another kind"},
            {"text": "Heating the carbonate releases gas that was trapped "
                     "inside it",
             "correct": False,
             "why": "There is no trapped gas. The carbon dioxide is assembled "
                    "as the joins in the solid break"},
            {"text": "Heating the carbonate rearranges its atoms, and some of "
                     "them leave as carbon dioxide",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c4-02-h29",
        "band": "harder",
        "text": "Why would a chemist refuse to fund research into making "
                "helium gas by a chemical reaction?",
        "options": [
            {"text": "Because helium is an element, so helium atoms would have "
                     "to be there already",
             "correct": True},
            {"text": "Because helium is far too light to be held in any "
                     "container a laboratory could build for it",
             "correct": False,
             "why": "Helium is stored in cylinders every day. The objection is "
                    "that it cannot be made"},
            {"text": "Because helium does not react, and a substance that does "
                     "not react cannot be produced by a reaction",
             "correct": False,
             "why": "Being unreactive is about what helium does next. Plenty "
                    "of unreactive products are made by reactions"},
            {"text": "Because helium is a compound whose parts are missing",
             "correct": False,
             "why": "Helium is an element and is found on Earth, in natural "
                    "gas wells"},
        ],
        "figure": None,
    },
    {
        "id": "c4-02-h30",
        "band": "harder",
        "text": "A mixture of two gases is reacted twice: once slowly at room "
                "temperature and once quickly with a catalyst. Compare the "
                "atoms in the two sets of products.",
        "options": [
            {"text": "The slow run keeps more of its atoms, because the fast "
                     "run drives some of them off as heat",
             "correct": False,
             "why": "Heat carries no atoms away, and neither run loses one"},
            {"text": "The fast run makes more atoms, because the catalyst "
                     "supplies extra as it works",
             "correct": False,
             "why": "A catalyst supplies no atoms. It is unchanged at the end"},
            {"text": "They cannot be compared unless both runs are done at one "
                     "temperature",
             "correct": False,
             "why": "Temperature changes the rate. The atom count is fixed by "
                    "what went in"},
            {"text": "The same kinds and numbers of atom in both",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c4-02-h31",
        "band": "harder",
        "text": "Explain why a chemist can say a proposed reaction is "
                "impossible without ever setting it up on a bench.",
        "options": [
            {"text": "Because the products ask for a kind of atom the "
                     "reactants do not contain",
             "correct": True},
            {"text": "Because no chemist would waste a bench on a reaction "
                     "that had not been done before by somebody else",
             "correct": False,
             "why": "New reactions are tried constantly. This one is refused "
                    "on the atoms"},
            {"text": "Because a reaction that has never been seen is taken to "
                     "be impossible until somebody manages it",
             "correct": False,
             "why": "Not seen yet and impossible are different claims, and "
                    "only one of them is provable in advance"},
            {"text": "Because every possible reaction is written down "
                     "already",
             "correct": False,
             "why": "No such list exists or could exist. The argument is about "
                    "the atoms"},
        ],
        "figure": None,
    },
    {
        "id": "c4-02-h32",
        "band": "harder",
        "text": "A flask holds twelve hydrogen atoms and six oxygen atoms. "
                "They are made into water, and the water is then split apart "
                "again. How many hydrogen atoms are in the flask at the end?",
        "options": [
            {"text": "Six, because half of them were used in making the "
                     "water",
             "correct": False,
             "why": "Making water uses no atom up. All twelve went into it and "
                    "all twelve came back out"},
            {"text": "Twelve",
             "correct": True},
            {"text": "Twenty-four, because splitting the water doubles what "
                     "was there",
             "correct": False,
             "why": "Splitting divides particles, never atoms. The count is "
                    "untouched"},
            {"text": "None, because splitting water gives just oxygen",
             "correct": False,
             "why": "Splitting water gives hydrogen as well, and it is the "
                    "same twelve atoms"},
        ],
        "figure": None,
    },
]
