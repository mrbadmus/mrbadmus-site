"""C6 lesson 03 — Neutralisation: twelve questions (MRB-269).

The lesson's argument is one shape: an acid and a base react, they make two new
substances, and neutral is a point rather than a region. These twelve probe the
angles the mastery ladder leaves alone — where the atoms went, why the curve is
flat then steep then flat, and the four places outside a laboratory where this
reaction is somebody's job.

The distractors are built from the lesson's two declared misconceptions.

`ACID-05` (neutralising an acid destroys it; only water is left) drives e02,
s01, s04 and h01. h01 is the one that matters: it weighs the beaker before and
after, so "the acid was destroyed" has to explain a balance that has not moved.

`ACID-06` (the pH climbs steadily as alkali is added) drives e04, s02 and h02.
s02 is the register's own case put as a question about the shape rather than
about a single drop, and h02 asks what would happen if the alkali were added
five drops at a time — where a steady-climb model predicts the same reading and
the real curve says you would step straight over the answer.

A third strand, everywhere on the page and in neither register entry, is that
NEUTRALISING MEANS MAKING SAFE. e03 and h03 are built on it: pushing an acid
past 7 is not making it safer, and a river needs near-neutral rather than
alkaline.

A fourth strand is that a salt is table salt. e01 and s03 separate the family
from the member.

Every question here is new prose, and the bar is §13's. No correct answer is
strictly the longest in its set by four words or by 1.4x, and the twelve are
authored level across the four answer positions — three apiece (MRB-278).
"""

UNIT = "C6"
LESSON = "neutralisation"
LESSON_NUMBER = 3

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "c6-03-e01",
        "band": "easier",
        "text": "In chemistry, what does the word “salt” mean?",
        "options": [
            {"text": "A whole family of compounds made when an acid reacts "
                     "with a base", "correct": True},
            {"text": "Only sodium chloride, the white stuff that goes on "
                     "chips", "correct": False,
             "why": "Sodium chloride is one salt out of thousands. It is a "
                    "member of the family, not the family."},
            {"text": "Any white crystalline solid left after a liquid "
                     "evaporates", "correct": False,
             "why": "Plenty of white crystals are not salts — sugar is one. "
                    "What makes a salt is what made it."},
            {"text": "Anything that tastes salty when it is dissolved in "
                     "water", "correct": False,
             "why": "Most salts are never tasted and some are poisonous. "
                    "Taste is not how the family is defined."},
        ],
        "figure": None,
    },
    {
        "id": "c6-03-e02",
        "band": "easier",
        "text": "Hydrochloric acid is neutralised with sodium hydroxide. What "
                "is in the beaker afterwards?",
        "options": [
            {"text": "Nothing but water, because both were destroyed",
             "correct": False,
             "why": "Boil the water off and white crystals are left in the "
                    "dish. They were not in either bottle at the start."},
            {"text": "A salt dissolved in water, made from both of them",
             "correct": True},
            {"text": "A weaker acid, watered down until it stopped mattering",
             "correct": False,
             "why": "Nothing was watered down. Both reactants were used up "
                    "making two new substances."},
            {"text": "The same acid and alkali, sitting there side by side",
             "correct": False,
             "why": "They reacted. If both were still there the mixture would "
                    "still burn, and it does not."},
        ],
        "figure": None,
    },
    {
        "id": "c6-03-e03",
        "band": "easier",
        "text": "An acid at pH 2 has so much alkali added that it reaches pH "
                "12. Is it safer than it was?",
        "options": [
            {"text": "Yes, because anything that has been neutralised is safe",
             "correct": False,
             "why": "It was neutral for one drop and then went straight past. "
                    "pH 12 is a strong alkali."},
            {"text": "Yes, because the acid has all gone", "correct": False,
             "why": "The acid has gone and something just as corrosive has "
                    "taken its place on the other side of 7."},
            {"text": "No, because pH 12 is about as far from neutral as pH 2 "
                     "was", "correct": True},
            {"text": "No, because adding anything to an acid always makes it "
                     "worse", "correct": False,
             "why": "Adding the right amount of alkali makes it harmless. "
                    "What went wrong here is the amount, not the idea."},
        ],
        "figure": None,
    },
    {
        "id": "c6-03-e04",
        "band": "easier",
        "text": "Alkali is added to acid one drop at a time and the pH is "
                "recorded. What shape does the graph make?",
        "options": [
            {"text": "A straight line climbing evenly from start to finish",
             "correct": False,
             "why": "For the first nine drops the reading barely moves. A "
                    "steady climb is what a student expects and not what "
                    "happens."},
            {"text": "A curve that rises fastest at the very beginning",
             "correct": False,
             "why": "The beginning is the flattest part. There is far more "
                    "acid than alkali there, so each drop is used up at once."},
            {"text": "A line that falls, because adding alkali lowers the pH",
             "correct": False,
             "why": "Alkali raises the pH. Adding it can never send the "
                    "reading back down."},
            {"text": "A flat stretch, then a sudden jump, then flat again",
             "correct": True},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "c6-03-s01",
        "band": "standard",
        "text": "A neutralised beaker is left on a windowsill until all the "
                "water has gone. What is left in it?",
        "options": [
            {"text": "Crystals of the salt that the reaction made",
             "correct": True},
            {"text": "Nothing at all, because everything in it evaporated",
             "correct": False,
             "why": "Water evaporates and a solid salt does not. What is left "
                    "is the crystals."},
            {"text": "The original acid, concentrated back to its old "
                     "strength", "correct": False,
             "why": "The acid was used up in the reaction. Removing water "
                    "cannot bring back a substance that no longer exists."},
            {"text": "A film of alkali, which does not evaporate the way acid "
                     "does", "correct": False,
             "why": "The alkali was used up too. What stayed behind is the "
                    "new compound both of them became."},
        ],
        "figure": None,
    },
    {
        "id": "c6-03-s02",
        "band": "standard",
        "text": "Nine drops of alkali barely move the reading and the tenth "
                "sends it from 3 to 11. Why?",
        "options": [
            {"text": "The tenth drop was larger than the ones before it",
             "correct": False,
             "why": "Every drop came out of the same dropper. What changed "
                    "was what was waiting for it in the beaker."},
            {"text": "The last of the acid was used up, so nothing consumed "
                     "that drop", "correct": True},
            {"text": "The indicator reached its limit and stopped reporting "
                     "properly", "correct": False,
             "why": "The indicator reported faithfully. The change it "
                    "reported was real and it was sudden."},
            {"text": "The mixture had warmed up enough to change its own pH",
             "correct": False,
             "why": "It warms a little and warming does not move a solution "
                    "across the scale by eight units."},
        ],
        "figure": None,
    },
    {
        "id": "c6-03-s03",
        "band": "standard",
        "text": "A tank of dilute sulfuric acid must be disposed of safely. "
                "What is done first?",
        "options": [
            {"text": "Add much more water, so the acid is too dilute to harm "
                     "anything", "correct": False,
             "why": "Dilution lowers the concentration and the water going "
                    "into the river is still acidic. A river needs near "
                    "neutral."},
            {"text": "Boil it off, so the acid leaves as a vapour",
             "correct": False,
             "why": "Boiling removes water and leaves the acid behind more "
                    "concentrated than it started."},
            {"text": "Add a stronger acid, so the two cancel each other out",
             "correct": False,
             "why": "Two acids never cancel. Cancelling an acid takes "
                    "something from the other side of 7."},
            {"text": "Add a base until it is neutral, then measure the pH "
                     "before releasing it", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c6-03-s04",
        "band": "standard",
        "text": "A beaker of acid and alkali is weighed before mixing and "
                "again afterwards. What does the balance read?",
        "options": [
            {"text": "Less, because the acid was destroyed in the reaction",
             "correct": False,
             "why": "Nothing is destroyed. The atoms are all still in the "
                    "beaker, rearranged into a salt and water."},
            {"text": "Less, because some of the mixture escaped as a gas",
             "correct": False,
             "why": "An acid with an alkali gives no gas at all. That is what "
                    "an acid with a CARBONATE does."},
            {"text": "More, because two substances have become two new ones",
             "correct": False,
             "why": "Two into two does not add mass. The same atoms are on "
                    "the balance in a different arrangement."},
            {"text": "Exactly the same, because mass is conserved in every "
                     "reaction", "correct": True},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "c6-03-h01",
        "band": "harder",
        "text": "A student says neutralisation destroys the acid. Which "
                "single piece of evidence refutes it?",
        "options": [
            {"text": "The mixture warms up while the reaction is happening",
             "correct": False,
             "why": "Warming shows a reaction happened and says nothing about "
                    "what is left. Plenty of reactions warm up."},
            {"text": "Universal indicator comes out green at the end",
             "correct": False,
             "why": "Green shows the mixture is neutral, which is what the "
                    "student already believes. It settles nothing."},
            {"text": "Boiling the water off leaves white crystals in the dish",
             "correct": True},
            {"text": "The mixture can be poured down the sink afterwards",
             "correct": False,
             "why": "Being safe to pour away is not the same as being empty. "
                    "The salt goes down the sink dissolved in the water."},
        ],
        "figure": None,
    },
    {
        "id": "c6-03-h02",
        "band": "harder",
        "text": "The same titration is repeated adding five drops at a time "
                "instead of one. What is lost?",
        "options": [
            {"text": "Nothing, because the same total volume goes in either "
                     "way", "correct": False,
             "why": "The total is the same and the resolution is not. The "
                    "reading crosses 7 inside a single one of those five-drop "
                    "steps."},
            {"text": "The exact point of neutrality, because the reading "
                     "steps straight over it", "correct": True},
            {"text": "The colour change, because five drops dilute the "
                     "indicator", "correct": False,
             "why": "The colour still changes and it changes just as "
                    "sharply. What is lost is knowing exactly when."},
            {"text": "The reaction itself, because it needs time between "
                     "drops", "correct": False,
             "why": "The reaction is essentially instant. Adding faster does "
                    "not stop it happening."},
        ],
        "figure": None,
    },
    {
        "id": "c6-03-h03",
        "band": "harder",
        "text": "Lime is added to an acidic lake to save the fish. Why is it "
                "added gradually rather than all at once?",
        "options": [
            {"text": "Because lime dissolves slowly and would sink to the "
                     "bottom", "correct": False,
             "why": "How fast it dissolves is a practical detail. The reason "
                    "is what happens to the water if too much goes in."},
            {"text": "Because the fish need time to move away from the "
                     "treated area", "correct": False,
             "why": "The fish cannot leave a lake. What harms them is the "
                    "change in the water they are already in."},
            {"text": "Because a large amount would push the lake past 7 and "
                     "make it alkaline", "correct": True},
            {"text": "Because lime reacts violently with water and would boil "
                     "the lake", "correct": False,
             "why": "Slaked lime added to a lake does nothing dramatic. The "
                    "danger is the pH it produces, not the heat."},
        ],
        "figure": None,
    },
    {
        "id": "c6-03-h04",
        "band": "harder",
        "text": "Toothpaste is described as mildly alkaline. Why mildly, "
                "rather than strongly?",
        "options": [
            {"text": "Because a strong alkali would damage the mouth far more "
                     "than the acid does", "correct": True},
            {"text": "Because a strong alkali would not neutralise the acid "
                     "properly", "correct": False,
             "why": "A strong alkali neutralises acid very well indeed. The "
                    "problem is what it does to everything else."},
            {"text": "Because the acid from bacteria is itself very weak",
             "correct": False,
             "why": "That acid takes enamel below pH 5.5, which is not weak "
                    "in its effect. The limit is on what a mouth can hold."},
            {"text": "Because toothpaste has to stay neutral to be safe to "
                     "use", "correct": False,
             "why": "It is not neutral — it is above 7 on purpose, which is "
                    "how it works against the acid."},
        ],
        "figure": None,
    },

    # ── easier · MRB-335 top-up ─────────────────────────────────────────
    {
        "id": "c6-03-e05",
        "band": "easier",
        "text": "What is neutralisation?",
        "options": [
            {"text": "The reaction between an acid and a base",
             "correct": True},
            {"text": "Diluting an acid with so much water that its pH climbs "
                     "all the way up to 7 and it stops behaving as an acid",
             "correct": False,
             "why": "Diluting never reaches 7 and makes nothing new. "
                    "Neutralisation is a reaction between two substances"},
            {"text": "Boiling an acid until it is gone",
             "correct": False,
             "why": "Nothing here is boiled, and boiling would concentrate "
                    "the acid rather than remove it"},
            {"text": "Any reaction that ends at pH 7",
             "correct": False,
             "why": "The reaction is between an acid and a base, and it ends "
                    "at 7 only if the amounts match exactly"},
        ],
        "figure": None,
    },
    {
        "id": "c6-03-e06",
        "band": "easier",
        "text": "What is an equivalence point?",
        "options": [
            {"text": "The point at which the two solutions are at exactly the "
                     "same temperature as each other, so that the reaction "
                     "can proceed evenly",
             "correct": False,
             "why": "Temperature is not what the word is about. It marks the "
                    "moment the acid runs out"},
            {"text": "The moment when exactly enough alkali has been added to "
                     "use up all the acid",
             "correct": True},
            {"text": "The point where the two liquids have the same volume",
             "correct": False,
             "why": "Volumes rarely match. What has to match is how much acid "
                    "and how much alkali"},
            {"text": "The pH of the acid before anything is added",
             "correct": False,
             "why": "That is where you start. The equivalence point is the "
                    "one drop where the reading jumps"},
        ],
        "figure": None,
    },
    {
        "id": "c6-03-e07",
        "band": "easier",
        "text": "Someone has indigestion — stomach acid where it should not "
                "be. What is in the tablet they take?",
        "options": [
            {"text": "A stronger acid, which pushes the stomach acid further "
                     "down the pH scale until it is too far from neutral to "
                     "do any more damage",
             "correct": False,
             "why": "More acid makes it worse. The pH has to come UP towards "
                    "7, which needs a base"},
            {"text": "A dye that shows where the acid is",
             "correct": False,
             "why": "An indicator would report the problem and do nothing "
                    "about it"},
            {"text": "A base, which neutralises the acid",
             "correct": True},
            {"text": "A catalyst, which speeds the acid up",
             "correct": False,
             "why": "Speeding it up is the last thing anyone wants, and a "
                    "catalyst would not remove it"},
        ],
        "figure": None,
    },
    {
        "id": "c6-03-e08",
        "band": "easier",
        "text": "What is a titration?",
        "options": [
            {"text": "Boiling a solution until crystals of the salt in it "
                     "start to appear on a cold glass rod",
             "correct": False,
             "why": "That is crystallising, which comes after the reaction. A "
                    "titration is the measuring"},
            {"text": "Testing a solution with litmus paper",
             "correct": False,
             "why": "That gives a side of neutral. A titration gives a "
                    "volume"},
            {"text": "Filtering a mixture to remove what has not reacted",
             "correct": False,
             "why": "Filtering separates a solid out. A titration measures "
                    "how much of one solution the other needs"},
            {"text": "Adding one solution to another a little at a time until "
                     "the reaction is exactly complete, and measuring how much "
                     "it took",
             "correct": True},
        ],
        "figure": None,
    },

    # ── standard · MRB-335 top-up ───────────────────────────────────────
    {
        "id": "c6-03-s05",
        "band": "standard",
        "text": "Hydrochloric acid is neutralised with sodium hydroxide. "
                "Which salt is made?",
        "options": [
            {"text": "Sodium chloride",
             "correct": True},
            {"text": "Sodium hydroxide chloride, taking one word from each of "
                     "the two substances that were poured into the beaker",
             "correct": False,
             "why": "No salt is named like that. The metal names it and the "
                    "acid gives the ending"},
            {"text": "Hydrogen chloride",
             "correct": False,
             "why": "That is the acid itself. The hydrogen is swapped for the "
                    "metal, which is what makes a salt"},
            {"text": "Sodium sulfate",
             "correct": False,
             "why": "Sulfates come from sulfuric acid. Hydrochloric acid "
                    "gives chlorides"},
        ],
        "figure": None,
    },
    {
        "id": "c6-03-s06",
        "band": "standard",
        "text": "Power station chimneys are sprayed with calcium hydroxide to "
                "catch sulfur dioxide before it leaves. Which reaction is "
                "that?",
        "options": [
            {"text": "Filtration on a very large scale, with the spray acting "
                     "as a wet screen that the gas particles cannot pass "
                     "through",
             "correct": False,
             "why": "Nothing is being sieved by size. The gas is reacting "
                    "with the spray"},
            {"text": "Neutralisation — a base catching an acidic gas",
             "correct": True},
            {"text": "Distillation, because the gas is condensed by the cold "
                     "spray",
             "correct": False,
             "why": "Nothing is condensed and collected. A new substance is "
                    "made, and it is a solid"},
            {"text": "Crystallisation, because a solid comes out of it",
             "correct": False,
             "why": "A solid is produced, and it is a product of a reaction "
                    "rather than something coming out of a solution"},
        ],
        "figure": None,
    },
    {
        "id": "c6-03-s07",
        "band": "standard",
        "text": "25 cm³ of acid needs exactly 20 cm³ of a particular alkali "
                "to neutralise it. What happens if 30 cm³ of that alkali is "
                "added instead?",
        "options": [
            {"text": "The extra alkali reacts with the salt that has already "
                     "been made, and the pH comes back down towards 7 on its "
                     "own",
             "correct": False,
             "why": "The salt does not react with the extra alkali. The "
                    "excess simply sits in the beaker"},
            {"text": "Nothing changes after 20 cm³, because the reaction has "
                     "finished",
             "correct": False,
             "why": "The reaction has finished and the beaker has not stopped "
                    "receiving alkali. What goes in stays in"},
            {"text": "The mixture ends up alkaline, with 10 cm³ of unreacted "
                     "alkali in it",
             "correct": True},
            {"text": "The mixture ends up acidic, because the extra alkali "
                     "makes the salt acidic",
             "correct": False,
             "why": "Excess alkali pushes the pH up, not down. Sodium "
                    "chloride solution is neutral"},
        ],
        "figure": None,
    },
    {
        "id": "c6-03-s08",
        "band": "standard",
        "text": "Why does a chemist measuring an unknown acid use a sharp "
                "one-colour indicator rather than universal indicator?",
        "options": [
            {"text": "Because universal indicator would react with the acid",
             "correct": False,
             "why": "The few drops of indicator change nothing measurable. "
                    "The problem is reading the end point"},
            {"text": "Because universal indicator does not work on strong "
                     "acids",
             "correct": False,
             "why": "It works right across the scale. It simply changes too "
                    "gradually to mark one drop"},
            {"text": "Because a sharp indicator gives a pH number and "
                     "universal indicator does not",
             "correct": False,
             "why": "Exactly backwards. Universal indicator is the one that "
                    "gives a number"},
            {"text": "Because they need to see the exact drop where the "
                     "colour flips, and a gradual change hides it",
             "correct": True},
        ],
        "figure": None,
    },

    # ── harder · MRB-335 top-up ─────────────────────────────────────────
    {
        "id": "c6-03-h05",
        "band": "harder",
        "text": "Sulfur dioxide from a chimney is caught with calcium "
                "hydroxide, and the salt produced is calcium sulfate — which "
                "is sold as plasterboard. What does that show?",
        "options": [
            {"text": "That the salt from a neutralisation is a real substance "
                     "with uses of its own",
             "correct": True},
            {"text": "That neutralisation always produces something useful, "
                     "which is why industry is willing to pay for the "
                     "chemicals that go into it in the first place",
             "correct": False,
             "why": "Plenty of neutralisations give a salt nobody wants. This "
                    "one happens to give a valuable one"},
            {"text": "That the sulfur dioxide was not really an acid",
             "correct": False,
             "why": "It is acidic, which is why a base catches it. That is "
                    "the whole design"},
            {"text": "That plasterboard is dangerous",
             "correct": False,
             "why": "The salt is harmless. Being made from something "
                    "unpleasant does not make a product unpleasant"},
        ],
        "figure": None,
    },
    {
        "id": "c6-03-h06",
        "band": "harder",
        "text": "A beaker of acid is neutralised and the water is boiled off. "
                "The crystals left behind are weighed. How does their mass "
                "compare with the acid and alkali that went in?",
        "options": [
            {"text": "Heavier than both put together, because the two "
                     "solutions have combined and their masses add up in the "
                     "solid that is left",
             "correct": False,
             "why": "Water was made as well and has been boiled away. The "
                    "crystals are only part of what went in"},
            {"text": "Less, because the water that was made has been boiled "
                     "off",
             "correct": True},
            {"text": "Exactly the same, because mass is always conserved",
             "correct": False,
             "why": "Mass IS conserved — across everything, including the "
                    "water in the air. The crystals alone are not everything"},
            {"text": "Less, because some of the acid was destroyed",
             "correct": False,
             "why": "Nothing is destroyed. The acid's atoms are in the salt "
                    "and in the water"},
        ],
        "figure": None,
    },
    {
        "id": "c6-03-h07",
        "band": "harder",
        "text": "A student neutralises acid with alkali and then says the "
                "beaker holds pure water. Which single test would show they "
                "are wrong?",
        "options": [
            {"text": "Test it with universal indicator and check that the "
                     "reading really is 7 rather than something a little "
                     "above or below it",
             "correct": False,
             "why": "A correct neutralisation does read 7 — and so does pure "
                    "water. The test cannot tell them apart"},
            {"text": "Weigh the beaker before and after the reaction",
             "correct": False,
             "why": "The mass is unchanged either way. Conservation of mass "
                    "does not distinguish the two"},
            {"text": "Evaporate it to dryness and see the salt left behind",
             "correct": True},
            {"text": "Smell it",
             "correct": False,
             "why": "Salt solution and water both smell of nothing, and "
                    "smelling a beaker is not a test"},
        ],
        "figure": None,
    },
    {
        "id": "c6-03-h08",
        "band": "harder",
        "text": "25 cm³ of an acid is exactly neutralised by 20 cm³ of an "
                "alkali. The same alkali is used on 50 cm³ of the same acid. "
                "How much is needed?",
        "options": [
            {"text": "20 cm³",
             "correct": False,
             "why": "That treats the alkali as deciding the volume. The volume "
                    "needed depends on how much acid there is, and there is "
                    "now twice as much of it"},
            {"text": "25 cm³",
             "correct": False,
             "why": "The two volumes do not have to match. It took 20 cm³ for "
                    "25 cm³ of acid, not 25"},
            {"text": "45 cm³",
             "correct": False,
             "why": "Volumes of two different solutions cannot be added like "
                    "that. Twice the acid needs twice the alkali"},
            {"text": "40 cm³",
             "correct": True},
        ],
        "figure": None,
    },

    # ── MRB-338 expansion ───────────
    {
        "id": "c6-03-e09",
        "band": "easier",
        "text": "What happens to the temperature of the mixture while an acid and an "
                "alkali react?",
        "options": [
            {"text": "It rises and then falls below the start", "correct": False,
             "why": "It warms and then cools back to room temperature. It does not "
                    "go below where it began."},
            {"text": "It falls sharply", "correct": False,
             "why": "Nothing here takes heat in. The beaker is warmer afterwards, "
                    "not colder."},
            {"text": "It stays exactly the same", "correct": False,
             "why": "The warming is easy to feel through the glass, which is one "
                    "sign a reaction is happening."},
            {"text": "It rises", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c6-03-e10",
        "band": "easier",
        "text": "An acid and an alkali are mixed. When does the mixture end up at "
                "exactly pH 7?",
        "options": [
            {"text": "Whenever any alkali at all is added", "correct": False,
             "why": "A little alkali in a lot of acid leaves the beaker acidic. It "
                    "takes the right amount."},
            {"text": "Only if the amounts match exactly", "correct": True},
            {"text": "Whenever the two are the same strength", "correct": False,
             "why": "Strength is not the whole story. The volumes matter as well as "
                    "what is in them."},
            {"text": "Whenever the mixture has been stirred", "correct": False,
             "why": "Stirring spreads the two together. It does not decide how much "
                    "of each went in."},
        ],
        "figure": None,
    },
    {
        "id": "c6-03-e11",
        "band": "easier",
        "text": "What is a burette used for?",
        "options": [
            {"text": "Holding the acid while it is warmed", "correct": False,
             "why": "It is a measuring instrument, not a heating vessel, and nothing"
                    " is warmed in it."},
            {"text": "Stirring the flask steadily as the reaction runs", "correct": False,
             "why": "Stirring is done by swirling the flask. A burette stands still "
                    "above it."},
            {"text": "Running one solution in and measuring the volume", "correct": True},
            {"text": "Filtering the solid out of the mixture", "correct": False,
             "why": "Filtering needs paper and a funnel. A burette holds liquid and "
                    "delivers it a drop at a time."},
        ],
        "figure": None,
    },
    {
        "id": "c6-03-e12",
        "band": "easier",
        "text": "An acid is cancelled out by a base that will not dissolve in water. "
                "Is that neutralisation?",
        "options": [
            {"text": "No — only an alkali can do that", "correct": False,
             "why": "Neutralisation is the reaction of an acid with a base. Alkalis "
                    "are simply the bases that dissolve."},
            {"text": "No — it has to dissolve first", "correct": False,
             "why": "An insoluble base reacts perfectly well while sitting on the "
                    "bottom of the beaker."},
            {"text": "Yes, but only if it is heated", "correct": False,
             "why": "Warming speeds it up, but the reaction happens at room "
                    "temperature without any help."},
            {"text": "Yes", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c6-03-e13",
        "band": "easier",
        "text": "Which of these is a salt?",
        "options": [
            {"text": "Sodium chloride", "correct": True},
            {"text": "Sodium hydroxide", "correct": False,
             "why": "That is an alkali, and it is one of the things a salt can be "
                    "made from."},
            {"text": "Hydrochloric acid", "correct": False,
             "why": "That is an acid. A salt is what is left once its hydrogen has "
                    "been swapped for a metal."},
            {"text": "Calcium hydroxide", "correct": False,
             "why": "That is an alkali too, spread on fields as lime."},
        ],
        "figure": None,
    },
    {
        "id": "c6-03-e14",
        "band": "easier",
        "text": "Why is an indicator added to the acid before a titration is started?",
        "options": [
            {"text": "To make the reaction start, since it will not begin without one", "correct": False,
             "why": "The reaction runs the moment the two meet. The dye only watches"
                    " it."},
            {"text": "To speed the reaction up so that the whole titration takes a "
                      "good deal less time", "correct": False,
             "why": "Nothing about the rate changes. An indicator reports rather "
                    "than helps."},
            {"text": "To colour the salt that is made so that it can be seen in the "
                      "flask", "correct": False,
             "why": "The salt stays dissolved and invisible. The colour belongs to "
                    "the dye, not the product."},
            {"text": "So that the moment the acid is used up can be seen", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c6-03-e15",
        "band": "easier",
        "text": "In acid + alkali makes salt + water, where do the atoms in the water"
                " come from?",
        "options": [
            {"text": "From the acid and the alkali, both", "correct": True},
            {"text": "From the air above the beaker", "correct": False,
             "why": "Nothing is taken from the air. Seal the beaker and the same "
                    "water is made."},
            {"text": "From the glass of the beaker itself", "correct": False,
             "why": "The glass takes no part. It is the container and nothing more."},
            {"text": "From the indicator that was added", "correct": False,
             "why": "A drop of dye is far too little, and the same water forms with "
                    "no indicator at all."},
        ],
        "figure": None,
    },
    {
        "id": "c6-03-e16",
        "band": "easier",
        "text": "Sodium hydroxide is neutralised by an acid. Where does the metal in "
                "the salt come from?",
        "options": [
            {"text": "From the acid", "correct": False,
             "why": "The acid supplies the second half of the salt's name. The metal"
                    " comes from the other side."},
            {"text": "From the water that is made", "correct": False,
             "why": "Water is made of hydrogen and oxygen. There is no metal in it "
                    "at all."},
            {"text": "From the alkali", "correct": True},
            {"text": "From the indicator", "correct": False,
             "why": "The dye is there to be looked at. It contributes nothing to "
                    "either product."},
        ],
        "figure": None,
    },
    {
        "id": "c6-03-e17",
        "band": "easier",
        "text": "Why does a school titration use dilute solutions of both the acid "
                "and the alkali?",
        "options": [
            {"text": "Because dilute solutions react and concentrated ones do not", "correct": False,
             "why": "Concentrated solutions react very readily. That is the problem "
                    "rather than the solution."},
            {"text": "Because concentrated ones would warm enough to boil and spit", "correct": True},
            {"text": "Because a dilute solution is no longer really an acid or an "
                      "alkali at all", "correct": False,
             "why": "Diluting changes how fiercely it acts, never what kind of "
                    "substance it is."},
            {"text": "Because an indicator will not work in a concentrated solution", "correct": False,
             "why": "The dye works either way. The reason for using dilute solutions"
                    " is the heat."},
        ],
        "figure": None,
    },
    {
        "id": "c6-03-e18",
        "band": "easier",
        "text": "Neutralisation needs no heating, no light and no catalyst. What does"
                " that tell you about it?",
        "options": [
            {"text": "That it is not really a chemical reaction of any kind at all", "correct": False,
             "why": "New substances are made and heat is given out, which is a "
                    "chemical reaction by any test."},
            {"text": "That it only works with very dilute solutions", "correct": False,
             "why": "Concentrated solutions react too, and faster. Needing no help "
                    "is not about strength."},
            {"text": "That it starts as soon as the two are mixed", "correct": True},
            {"text": "That it takes several hours to finish", "correct": False,
             "why": "It is over in moments. Needing no conditions is exactly why it "
                    "is so quick."},
        ],
        "figure": None,
    },
    {
        "id": "c6-03-e19",
        "band": "easier",
        "text": "A beaker of acid and alkali warms up and new substances appear in "
                "it. What kind of change is that?",
        "options": [
            {"text": "A physical change", "correct": False,
             "why": "A salt is present that was in neither bottle, and that is a new"
                    " substance rather than a new temperature."},
            {"text": "A change of state", "correct": False,
             "why": "Nothing melted, froze or boiled. The substances themselves are "
                    "different at the end."},
            {"text": "No change at all", "correct": False,
             "why": "Plenty happened. Boil the water off and the crystals left "
                    "behind are the evidence."},
            {"text": "A chemical change", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c6-03-e20",
        "band": "easier",
        "text": "A school titration mixture is poured down the sink at the end of the"
                " lesson. Why is that allowed?",
        "options": [
            {"text": "Because salt solution evaporates before it reaches the drains", "correct": False,
             "why": "It goes down the pipe as a liquid. Evaporation has nothing to "
                    "do with it."},
            {"text": "Because acid is always perfectly safe once it has been watered "
                      "down a little", "correct": False,
             "why": "Dilute acid is still acid. What makes this safe is that there "
                    "is none of it left."},
            {"text": "Because the mixture is neutral and holds only salt and water", "correct": True},
            {"text": "Because the drains are made of metal and metal resists acid", "correct": False,
             "why": "Reactive metals are attacked by acid, which is why acid is not "
                    "poured away untreated."},
        ],
        "figure": None,
    },
    {
        "id": "c6-03-e21",
        "band": "easier",
        "text": "One drop of alkali falls into a large beaker of acid at the start of"
                " a titration. What happens to that drop?",
        "options": [
            {"text": "It floats on top without mixing in at all", "correct": False,
             "why": "Both are water-based solutions and mix readily. Nothing floats."},
            {"text": "It turns the whole beaker alkaline at once", "correct": False,
             "why": "One drop against a beaker of acid changes the reading hardly at"
                    " all."},
            {"text": "It sinks straight to the bottom and stays there unchanged", "correct": False,
             "why": "It reacts as soon as it arrives. Nothing is left to sit at the "
                    "bottom."},
            {"text": "It is used up at once by the acid already there", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c6-03-e22",
        "band": "easier",
        "text": "Which of these would neutralise an acid?",
        "options": [
            {"text": "Sodium hydroxide", "correct": True},
            {"text": "Sulfuric acid", "correct": False,
             "why": "Adding a second acid makes the mixture more acidic, not less."},
            {"text": "Sodium chloride", "correct": False,
             "why": "Table salt is already neutral and has nothing left to give an "
                    "acid."},
            {"text": "Pure water", "correct": False,
             "why": "Water dilutes an acid but does not react with it, so the acid "
                    "is still there."},
        ],
        "figure": None,
    },
    {
        "id": "c6-03-e23",
        "band": "easier",
        "text": "Alkali is run into an acid a little at a time. Which way does the pH"
                " reading move?",
        "options": [
            {"text": "Down, away from 7", "correct": False,
             "why": "Down is further into the acid half. Adding alkali moves the "
                    "reading the other way."},
            {"text": "Up, towards 7 and then past it", "correct": True},
            {"text": "It does not move until the very last drop", "correct": False,
             "why": "It creeps up from the start. What is sudden is the jump near "
                    "the end, not the beginning."},
            {"text": "Up to 7 and then no further, whatever is added", "correct": False,
             "why": "Once the acid is used up, more alkali carries the reading "
                    "straight past 7."},
        ],
        "figure": None,
    },
    {
        "id": "c6-03-e24",
        "band": "easier",
        "text": "Which pair would react together in a neutralisation?",
        "options": [
            {"text": "Hydrochloric acid and sulfuric acid", "correct": False,
             "why": "Two acids sit on the same side of 7 and have nothing to cancel "
                    "in one another."},
            {"text": "Sodium hydroxide and calcium hydroxide", "correct": False,
             "why": "Two alkalis, both above 7. Neither can neutralise the other."},
            {"text": "Nitric acid and calcium hydroxide", "correct": True},
            {"text": "Sodium chloride and pure water", "correct": False,
             "why": "Both are neutral already. Salt simply dissolves, and no "
                    "reaction takes place."},
        ],
        "figure": None,
    },
    {
        "id": "c6-03-s09",
        "band": "standard",
        "text": "A flask is swirled constantly while alkali runs into it from a "
                "burette. Why?",
        "options": [
            {"text": "So air is mixed in, which the reaction needs in order to go to "
                      "completion", "correct": False,
             "why": "No air is involved. The two solutions have everything the "
                    "reaction needs."},
            {"text": "So the mixture is kept warm enough for the reaction to carry on"
                      " at all", "correct": False,
             "why": "Swirling does not warm anything, and the reaction needs no "
                    "warming."},
            {"text": "So the indicator is stopped from settling out at the bottom of "
                      "the flask", "correct": False,
             "why": "The dye is dissolved and stays spread through the liquid on its"
                    " own."},
            {"text": "So each drop meets acid throughout the flask rather than only "
                      "where it lands", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c6-03-s10",
        "band": "standard",
        "text": "Explain why a beaker of acid and alkali is warmer after the reaction"
                " than before it.",
        "options": [
            {"text": "Because stirring the two together puts energy into the liquid", "correct": False,
             "why": "The beaker warms whether or not it is stirred, and stirring "
                    "could never supply that much."},
            {"text": "Because the reaction gives out energy as it happens", "correct": True},
            {"text": "Because the acid and the alkali were already warm when they "
                      "were poured", "correct": False,
             "why": "Both start at room temperature, and the mixture ends up above "
                    "it."},
            {"text": "Because the salt formed holds heat better than water does", "correct": False,
             "why": "The heat has to come from somewhere. Holding it is not the same"
                    " as producing it."},
        ],
        "figure": None,
    },
    {
        "id": "c6-03-s11",
        "band": "standard",
        "text": "One student stops a titration at the first hint of a colour change; "
                "another carries on until the colour is strong. Whose result is "
                "better?",
        "options": [
            {"text": "The second, because a strong colour is easier to see and so "
                      "easier to repeat", "correct": False,
             "why": "By then several extra drops have gone in, and the volume "
                    "recorded is too large."},
            {"text": "Neither, because the colour is unreliable and only a meter can "
                      "settle a titration", "correct": False,
             "why": "A sharp indicator is the standard tool for this, and it is "
                    "entirely reliable."},
            {"text": "The first, because the change happens on a single drop and "
                      "anything beyond it overshoots", "correct": True},
            {"text": "The second, because the reaction is not finished until the "
                      "colour has stopped changing", "correct": False,
             "why": "The reaction finishes at the drop where the acid runs out, not "
                    "when the colour deepens."},
        ],
        "figure": None,
    },
    {
        "id": "c6-03-s12",
        "band": "standard",
        "text": "A factory neutralises a tank of acid and then measures the pH before"
                " releasing it. Why measure rather than simply calculate?",
        "options": [
            {"text": "Because a calculation cannot be done at all until the reaction "
                      "has finished", "correct": False,
             "why": "The arithmetic can be done in advance. The point is whether the"
                    " tank matches it."},
            {"text": "Because the pH of a tank is always different from the pH of a "
                      "beaker", "correct": False,
             "why": "Scale does not change the chemistry. What changes is how "
                    "certain you can be of the amounts."},
            {"text": "Because measuring is quicker than working the volumes out on "
                      "paper", "correct": False,
             "why": "Speed is not the reason. A wrong release cannot be undone, so "
                    "it has to be checked."},
            {"text": "Because the exact amounts are never certain, and a release "
                      "cannot be taken back", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c6-03-s13",
        "band": "standard",
        "text": "A salt's name has two parts. Which part does the acid decide?",
        "options": [
            {"text": "The first part — the metal in the salt", "correct": False,
             "why": "The metal comes from the base. The acid supplies the other half"
                    " of the name."},
            {"text": "The second part — chloride, sulfate or nitrate", "correct": True},
            {"text": "Both parts — the metal and the ending", "correct": False,
             "why": "Two things react, and each leaves its mark. One name could not "
                    "tell you both."},
            {"text": "Neither part — the chemist who first made it", "correct": False,
             "why": "Salt names are built from what made them, which is why the name"
                    " reads as a recipe."},
        ],
        "figure": None,
    },
    {
        "id": "c6-03-s14",
        "band": "standard",
        "text": "Why is neutralisation called a reaction rather than a dilution?",
        "options": [
            {"text": "Because two new substances are made, rather than the acid being"
                      " spread thinner", "correct": True},
            {"text": "Because a dilution only happens when the water is added from a "
                      "tap rather than from a bottle", "correct": False,
             "why": "Where the water comes from is beside the point. What matters is"
                    " whether anything new is formed."},
            {"text": "Because the mixture ends up at pH 7, which a dilution could "
                      "never reach at all", "correct": False,
             "why": "Enough water brings an acid very close to 7, so the reading "
                    "alone does not separate them."},
            {"text": "Because a reaction always gives out heat and a dilution never "
                      "gives out any", "correct": False,
             "why": "Some dissolvings warm and some cool. Heat is a clue rather than"
                    " the definition."},
        ],
        "figure": None,
    },
    {
        "id": "c6-03-s15",
        "band": "standard",
        "text": "A titration is repeated three times and the volumes are 20.1, 20.0 "
                "and 20.2 cm³. What should be reported?",
        "options": [
            {"text": "20.2 cm³, since the largest reading is the one that used all "
                      "the acid", "correct": False,
             "why": "All three finished the reaction. The largest is not "
                    "automatically the most complete."},
            {"text": "20.0 cm³, the roundest reading", "correct": False,
             "why": "A result is chosen because it represents the readings, not "
                    "because it is tidy."},
            {"text": "About 20.1 cm³, the mean of the three", "correct": True},
            {"text": "All three separately, since averaging hides how much they "
                      "differed", "correct": False,
             "why": "The spread is worth stating, but the measurement itself is "
                    "reported as one value."},
        ],
        "figure": None,
    },
    {
        "id": "c6-03-s16",
        "band": "standard",
        "text": "An acid at pH 1 and an alkali at pH 13 are mixed in exactly matching"
                " amounts. Predict the pH and the temperature.",
        "options": [
            {"text": "pH 7, and noticeably warmer than either started", "correct": True},
            {"text": "pH 7, and colder, because the two cancel their heat out as well", "correct": False,
             "why": "Cancelling applies to the acid and the alkali. Energy is "
                    "released, not cancelled."},
            {"text": "pH 14, and warmer, the readings added", "correct": False,
             "why": "pH values are not added. Matching amounts leave neither in "
                    "excess, which is 7."},
            {"text": "pH 1, and unchanged, because the stronger of the two always "
                      "wins", "correct": False,
             "why": "Neither wins when the amounts match. Both are used up together."},
        ],
        "figure": None,
    },
    {
        "id": "c6-03-s17",
        "band": "standard",
        "text": "A student must neutralise 25 cm³ of acid but has no indicator at "
                "all. Suggest the best alternative.",
        "options": [
            {"text": "Add alkali until the beaker stops warming", "correct": False,
             "why": "The warming fades gradually and gives no sharp signal, so the "
                    "end point would be guessed."},
            {"text": "Add alkali until the mixture stops fizzing", "correct": False,
             "why": "An acid and an alkali do not fizz at any stage, so there is "
                    "nothing to watch."},
            {"text": "Add alkali until the solution turns cloudy", "correct": False,
             "why": "Both products stay dissolved, so the mixture is clear from "
                    "start to finish."},
            {"text": "Add alkali with a pH meter in the beaker and stop at 7", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c6-03-s18",
        "band": "standard",
        "text": "A neutralised beaker is left uncovered on a bench for a week and the"
                " mass falls. Explain why.",
        "options": [
            {"text": "The salt escapes into the air as a fine powder", "correct": False,
             "why": "The salt stays behind in the dish. It is the water that leaves."},
            {"text": "The reaction is still going and is using the contents up", "correct": False,
             "why": "The reaction finished the moment the two were mixed. Nothing is"
                    " still being consumed."},
            {"text": "Water evaporates, leaving the salt behind", "correct": True},
            {"text": "A gas is given off slowly as the products settle", "correct": False,
             "why": "An acid and an alkali make no gas at all. There is nothing to "
                    "be given off."},
        ],
        "figure": None,
    },
    {
        "id": "c6-03-s19",
        "band": "standard",
        "text": "Why is acid + base a better statement of neutralisation than acid + "
                "alkali?",
        "options": [
            {"text": "Because alkali is an old word that chemists no longer use for "
                      "anything", "correct": False,
             "why": "Alkali is still in daily use. It simply names a smaller group "
                    "than base does."},
            {"text": "Because bases that will not dissolve neutralise acid just as "
                      "well", "correct": True},
            {"text": "Because a base makes only water, while an alkali makes a salt "
                      "as well", "correct": False,
             "why": "Both make a salt and water. The difference between them is "
                    "whether they dissolve."},
            {"text": "Because an alkali reacts only with the strong acids while a "
                      "base reacts with any of them", "correct": False,
             "why": "Alkalis react with weak acids perfectly well. Strength is not "
                    "what separates the two words."},
        ],
        "figure": None,
    },
    {
        "id": "c6-03-s20",
        "band": "standard",
        "text": "Why is it a poor description to say that neutralisation cancels an "
                "acid out and leave it there?",
        "options": [
            {"text": "Because nothing is cancelled and the acid is still present at "
                      "the end", "correct": False,
             "why": "The acid really is used up. What the word hides is what took "
                    "its place."},
            {"text": "Because cancelling is a word from mathematics and cannot be "
                      "used about chemistry", "correct": False,
             "why": "Borrowed words are fine. The trouble is what this one leaves "
                    "out."},
            {"text": "Because two new substances are formed, and the word hides both "
                      "of them", "correct": True},
            {"text": "Because the mixture is never exactly neutral, so the word is "
                      "wrong in every case", "correct": False,
             "why": "Matching amounts really do give 7. The word is incomplete "
                    "rather than false."},
        ],
        "figure": None,
    },
    {
        "id": "c6-03-s21",
        "band": "standard",
        "text": "Describe what has happened to the particles at the moment an acid "
                "has been exactly neutralised.",
        "options": [
            {"text": "Every particle of acid has met one of alkali, and both are gone", "correct": True},
            {"text": "The acid particles have all been pushed down to the bottom of "
                      "the flask by the alkali", "correct": False,
             "why": "Nothing settles out. The products are dissolved and spread "
                    "through the liquid."},
            {"text": "Half have reacted and half are waiting for alkali",
             "correct": False,
             "why": "At the exact point there is no acid left waiting. That is what "
                    "makes it the exact point."},
            {"text": "The acid particles have been diluted until they are too spread "
                      "out to act", "correct": False,
             "why": "Dilution spreads particles out but does not remove them. Here "
                    "they have genuinely reacted away."},
        ],
        "figure": None,
    },
    {
        "id": "c6-03-s22",
        "band": "standard",
        "text": "The reaction of an acid with an alkali makes no gas at all. What "
                "does that rule out as a way of following it?",
        "options": [
            {"text": "Watching the pH with a meter as the alkali goes in", "correct": False,
             "why": "A meter works perfectly here and is one of the standard ways of"
                    " following this reaction."},
            {"text": "Collecting and measuring the volume given off", "correct": True},
            {"text": "Adding a dye and watching for the colour to change", "correct": False,
             "why": "That is exactly how a school titration is followed, and it "
                    "needs no gas at all."},
            {"text": "Feeling the outside of the flask as the reaction runs", "correct": False,
             "why": "The flask genuinely warms, so this gives a rough signal even "
                    "though no gas appears."},
        ],
        "figure": None,
    },
    {
        "id": "c6-03-h09",
        "band": "harder",
        "text": "20 cm³ of alkali exactly neutralises 25 cm³ of an acid. The acid is "
                "then diluted with an equal volume of water. Predict the volume of "
                "alkali 25 cm³ of the new solution needs.",
        "options": [
            {"text": "40 cm³", "correct": False,
             "why": "Diluting spreads the same acid through more water. It cannot "
                    "create any."},
            {"text": "10 cm³", "correct": True},
            {"text": "20 cm³", "correct": False,
             "why": "The volume is the same but only half as much acid is in it, so "
                    "half the alkali is needed."},
            {"text": "None at all", "correct": False,
             "why": "It is still an acid, and every bit of it still has to be "
                    "reacted away."},
        ],
        "figure": None,
    },
    {
        "id": "c6-03-h10",
        "band": "harder",
        "text": "A titration trace is flat at the start, jumps, then is flat again. "
                "Explain why it is flat at BOTH ends.",
        "options": [
            {"text": "At the start the acid consumes each drop; at the end there is "
                      "no acid left to consume anything", "correct": True},
            {"text": "At both ends the indicator has stopped responding to the "
                      "solution", "correct": False,
             "why": "The dye reports faithfully throughout. What is flat is the "
                    "solution, not the instrument."},
            {"text": "At both ends the solutions are too dilute to change the reading", "correct": False,
             "why": "The same solutions produce an enormous change one drop later, "
                    "so dilution is not the reason."},
            {"text": "At both ends the reaction has stopped, and it only runs during "
                      "the jump itself", "correct": False,
             "why": "The reaction runs from the first drop to the last of the acid. "
                    "The jump is when the acid runs out."},
        ],
        "figure": None,
    },
    {
        "id": "c6-03-h11",
        "band": "harder",
        "text": "A student argues that because mass is conserved, a neutralised "
                "beaker is no safer than the acid it started as. Evaluate that.",
        "options": [
            {"text": "Correct, because nothing has left the beaker and so nothing "
                      "about it can have changed", "correct": False,
             "why": "The atoms are all present but they are in different substances,"
                    " and it is the substance that bites."},
            {"text": "Correct, because the acid is still in there and has only been "
                      "hidden by the water", "correct": False,
             "why": "The acid has reacted away. It is not hidden; it is no longer "
                    "there as acid."},
            {"text": "Wrong, because the corrosive substances have been used up in "
                      "making salt and water", "correct": True},
            {"text": "Wrong, because mass is not actually conserved when two "
                      "solutions react together", "correct": False,
             "why": "Mass is conserved. The student's arithmetic is fine; the "
                    "conclusion drawn from it is not."},
        ],
        "figure": None,
    },
    {
        "id": "c6-03-h12",
        "band": "harder",
        "text": "Explain why a neutralised mixture reads 7 only when the amounts "
                "match, in terms of what is left over.",
        "options": [
            {"text": "Because the water made in the reaction dilutes whatever is left"
                      " until it reads 7", "correct": False,
             "why": "The small amount of water made cannot hide an excess. A "
                    "leftover acid still reads below 7."},
            {"text": "Because the salt formed is acidic if there is too much acid and"
                      " alkaline if too much alkali", "correct": False,
             "why": "The salt here is neutral either way. What moves the reading is "
                    "the unreacted leftover."},
            {"text": "Because a mixture can only reach 7 if exactly equal volumes of "
                      "the two are used", "correct": False,
             "why": "Equal volumes only work if the two are equally strong. It is "
                    "the amounts that must match."},
            {"text": "Because whichever of the two is in excess stays in the beaker "
                      "and sets the reading", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c6-03-h13",
        "band": "harder",
        "text": "A student overshoots a titration by two drops, then adds one drop of"
                " acid to bring the colour back. Evaluate that as a method.",
        "options": [
            {"text": "Sound, because the colour has been restored and the colour is "
                      "what marks the end point", "correct": False,
             "why": "The colour is a signal about the flask, not about the burette "
                    "reading that has to be recorded."},
            {"text": "Sound, because adding acid back undoes the overshoot exactly", "correct": False,
             "why": "It repairs the flask but not the record. The volume run in is "
                    "still too large."},
            {"text": "Unsound, because the burette reading no longer matches the acid"
                      " that was in the flask", "correct": True},
            {"text": "Unsound, because acid and alkali cannot be mixed twice in the "
                      "same flask", "correct": False,
             "why": "They can be mixed as often as you like. The problem is what the"
                    " measurement now means."},
        ],
        "figure": None,
    },
    {
        "id": "c6-03-h14",
        "band": "harder",
        "text": "Equal volumes of two acid samples are titrated with the same alkali."
                " One needs 15 cm³ and the other needs 30 cm³. What does that show?",
        "options": [
            {"text": "That the second is twice as dangerous", "correct": False,
             "why": "How much acid there is and how fiercely it acts are separate "
                    "questions."},
            {"text": "That the second sample contains twice as much acid", "correct": True},
            {"text": "That the second sample was titrated twice as slowly as the "
                      "first one was", "correct": False,
             "why": "Speed changes nothing about the volume needed. The same acid "
                    "needs the same alkali."},
            {"text": "That the second sample has a pH exactly half that of the first "
                      "sample", "correct": False,
             "why": "pH does not halve like that, and it reports how acidic rather "
                    "than how much."},
        ],
        "figure": None,
    },
    {
        "id": "c6-03-h15",
        "band": "harder",
        "text": "Neutralisation gives out heat. Explain why that matters when "
                "concentrated solutions are mixed.",
        "options": [
            {"text": "Because the heat destroys the salt before it can form properly", "correct": False,
             "why": "The salt forms perfectly well. The hazard is the liquid leaving"
                    " the container."},
            {"text": "Because the heat makes the mixture acidic again once it has "
                      "cooled", "correct": False,
             "why": "Cooling does not undo a reaction. A neutral mixture stays "
                    "neutral."},
            {"text": "Because enough heat is released to boil the mixture and throw "
                      "it out of the beaker", "correct": True},
            {"text": "Because the heat has to be supplied from outside before "
                      "concentrated solutions will react", "correct": False,
             "why": "Nothing has to be supplied. The reaction produces the heat "
                    "rather than needing it."},
        ],
        "figure": None,
    },
    {
        "id": "c6-03-h16",
        "band": "harder",
        "text": "Explain why the products are always the same two things, whichever "
                "acid and whichever alkali are used.",
        "options": [
            {"text": "Because every acid and every alkali is really the same "
                      "substance under a different name", "correct": False,
             "why": "They are genuinely different substances, which is why the salts"
                    " they make have different names."},
            {"text": "Because part of the acid joins part of the alkali to make "
                      "water, and what is left makes the salt", "correct": True},
            {"text": "Because water is the only substance that can ever be made when "
                      "two solutions are mixed together", "correct": False,
             "why": "Two products are made here, and other mixtures make quite "
                    "different things."},
            {"text": "Because the salt is always sodium chloride, whatever the two "
                      "starting bottles were", "correct": False,
             "why": "The salt changes with the pair used. Only the two families of "
                    "product stay the same."},
        ],
        "figure": None,
    },
    {
        "id": "c6-03-h17",
        "band": "harder",
        "text": "Compare what a pH meter and a sharp one-colour indicator each give "
                "you during a titration.",
        "options": [
            {"text": "The meter gives one signal at the end and the indicator gives a"
                      " number throughout", "correct": False,
             "why": "This is the two the wrong way round. The meter is the one that "
                    "reads continuously."},
            {"text": "Both give exactly the same information, so the choice between "
                      "them makes no real difference", "correct": False,
             "why": "One gives a trace and the other a single moment, and that "
                    "difference decides which job each suits."},
            {"text": "The meter gives a number all the way through; the indicator "
                      "gives one sharp signal at the end", "correct": True},
            {"text": "The meter works only above 7 and the indicator works only below"
                      " it", "correct": False,
             "why": "Both work across the whole scale. Neither is limited to one "
                    "half of it."},
        ],
        "figure": None,
    },
    {
        "id": "c6-03-e25",
        "band": "easier",
        "text": "Alkali is added drop by drop to an acid and the pH is recorded after"
                " every drop. How many of those readings can be exactly 7?",
        "options": [
            {"text": "None", "correct": False,
             "why": "The mixture does pass through 7; it is crossing it that "
                    "takes so little."},
            {"text": "One at most", "correct": True},
            {"text": "About five, while the mixture sits at neutral",
             "correct": False,
             "why": "Neutral is not a stretch the mixture rests in for several "
                    "drops."},
            {"text": "Every reading after the acid is used up", "correct": False,
             "why": "Once the acid is gone the alkali piles up and the readings "
                    "climb well past 7."},
        ],
        "figure": None,
    },
    {
        "id": "c6-03-e26",
        "band": "easier",
        "text": "Sodium chloride is one salt. Roughly how many different salts are"
                " there altogether?",
        "options": [
            {"text": "Three", "correct": False,
             "why": "One for each common acid is the idea behind this. Each "
                    "acid makes a whole family, one for every metal it can be "
                    "paired with."},
            {"text": "Thousands", "correct": True},
            {"text": "One for each element", "correct": False,
             "why": "A salt is made from two parts, so the count is far larger "
                    "than the list of elements."},
            {"text": "Just one, table salt", "correct": False,
             "why": "Table salt is a single member of a very large family."},
        ],
        "figure": None,
    },
    {
        "id": "c6-03-e27",
        "band": "easier",
        "text": "Which acid produces salts whose names end in nitrate?",
        "options": [
            {"text": "Hydrochloric acid", "correct": False,
             "why": "Hydrochloric acid gives chlorides."},
            {"text": "Sulfuric acid", "correct": False,
             "why": "Sulfuric acid gives sulfates."},
            {"text": "Carbonic acid", "correct": False,
             "why": "Carbonic acid gives carbonates, not nitrates."},
            {"text": "Nitric acid", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c6-03-e28",
        "band": "easier",
        "text": "A salt called magnesium chloride has been made by neutralising an"
                " acid. Which acid was it?",
        "options": [
            {"text": "Hydrochloric acid", "correct": True},
            {"text": "Nitric acid", "correct": False,
             "why": "Nitric acid would have given magnesium nitrate."},
            {"text": "Dilute sulfuric acid", "correct": False,
             "why": "Sulfuric acid would have given magnesium sulfate."},
            {"text": "Citric acid", "correct": False,
             "why": "Citric acid gives citrates, and the name of this salt does "
                    "not carry that ending."},
        ],
        "figure": None,
    },
    {
        "id": "c6-03-e29",
        "band": "easier",
        "text": "In the drop-by-drop run on this lesson's bench, which solution is in"
                " the burette?",
        "options": [
            {"text": "The alkali, which is added a drop at a time",
             "correct": True},
            {"text": "The acid, which is added a drop at a time", "correct": False,
             "why": "The acid is the solution already measured into the flask."},
            {"text": "The indicator, so that more can be added as needed",
             "correct": False,
             "why": "A few drops of indicator go into the flask at the start and "
                    "no more are needed."},
            {"text": "Pure water, to keep the flask from drying out",
             "correct": False,
             "why": "Adding water would change the mixture without moving the "
                    "reaction on at all."},
        ],
        "figure": None,
    },
    {
        "id": "c6-03-e30",
        "band": "easier",
        "text": "An acid is neutralised by an alkali. Where does the hydrogen that was"
                " in the acid end up?",
        "options": [
            {"text": "In the salt, alongside the metal", "correct": False,
             "why": "The metal has taken its place in the salt, which is what "
                    "makes it a salt."},
            {"text": "Released as a gas from the beaker", "correct": False,
             "why": "No gas is produced when an acid meets an alkali."},
            {"text": "In the water that is made", "correct": True},
            {"text": "Left dissolved in the mixture, unchanged", "correct": False,
             "why": "It has reacted rather than staying as it was, which is why "
                    "the acid stops behaving as an acid."},
        ],
        "figure": None,
    },
    {
        "id": "c6-03-e31",
        "band": "easier",
        "text": "A beaker has just been neutralised and looks like nothing but water,"
                " although a salt has been made. Why can the salt not be seen?",
        "options": [
            {"text": "It has sunk to the bottom in a thin layer", "correct": False,
             "why": "There is nothing at the bottom; a layer of solid would be "
                    "plain to see."},
            {"text": "It is dissolved in the water", "correct": True},
            {"text": "It has escaped into the air as the mixture warmed",
             "correct": False,
             "why": "The salt stays in the beaker, which is why crystals appear "
                    "when the water goes."},
            {"text": "Only a tiny amount of it was made", "correct": False,
             "why": "A full beaker's worth is made, and it is all still there."},
        ],
        "figure": None,
    },
    {
        "id": "c6-03-e32",
        "band": "easier",
        "text": "One more drop of alkali is added after all the acid has already been"
                " used up. What happens to the reading?",
        "options": [
            {"text": "It falls back towards 7", "correct": False,
             "why": "Adding alkali never brings a reading down."},
            {"text": "It stays exactly where it is", "correct": False,
             "why": "With no acid left to use the drop up, it adds to what is "
                    "already there."},
            {"text": "It drops sharply, as it did at the cliff", "correct": False,
             "why": "The sharp change happened once, when the acid ran out, and "
                    "it went upwards."},
            {"text": "It climbs further above 7", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c6-03-s23",
        "band": "standard",
        "text": "Sulfuric acid is neutralised with sodium hydroxide. Name the salt"
                " that is made.",
        "options": [
            {"text": "Sodium sulfate", "correct": True},
            {"text": "Sodium chloride", "correct": False,
             "why": "Chlorides come from hydrochloric acid, which is not the acid "
                    "here."},
            {"text": "Sulfur hydroxide", "correct": False,
             "why": "The metal comes from the alkali, so sodium is the first part "
                    "of the name."},
            {"text": "Sodium hydrogen", "correct": False,
             "why": "The hydrogen goes into the water; it is not part of the salt "
                    "at all."},
        ],
        "figure": None,
    },
    {
        "id": "c6-03-s24",
        "band": "standard",
        "text": "As the last drop goes in, the indicator passes through green so fast"
                " that nobody sees it sit there. Explain why.",
        "options": [
            {"text": "Green is a weak colour that the other colours hide",
             "correct": False,
             "why": "Green shows clearly in any neutral solution; the trouble is "
                    "how briefly the mixture is neutral."},
            {"text": "The reading crosses 7 within a single drop", "correct": True},
            {"text": "The indicator is used up by the time the acid runs out",
             "correct": False,
             "why": "The indicator is not consumed and keeps reporting long after "
                    "the acid has gone."},
            {"text": "Green appears only in solutions that have no salt in them",
             "correct": False,
             "why": "The salt has no effect on the indicator, which reports the "
                    "pH alone."},
        ],
        "figure": None,
    },
    {
        "id": "c6-03-s25",
        "band": "standard",
        "text": "25 cm³ of acid needs exactly 20 cm³ of a particular alkali. Only"
                " 15 cm³ of that alkali is added. Predict the pH of the mixture.",
        "options": [
            {"text": "Exactly 7, because some of the acid has been neutralised",
             "correct": False,
             "why": "Neutral needs all of the acid used up, not some of it."},
            {"text": "Above 7, because alkali was added",
             "correct": False,
             "why": "Alkali only pushes a mixture past 7 once there is no acid "
                    "left to use it."},
            {"text": "Below 7, because acid is still left over", "correct": True},
            {"text": "Below 7, because alkali always makes a mixture more acidic",
             "correct": False,
             "why": "Alkali moves a reading up; the acid left over is what keeps "
                    "this one down."},
        ],
        "figure": None,
    },
    {
        "id": "c6-03-s26",
        "band": "standard",
        "text": "A burette is read with the eye level with the liquid surface rather"
                " than from above it. Explain why.",
        "options": [
            {"text": "Because looking down warms the burette and moves the liquid",
             "correct": False,
             "why": "A glance does not warm glass, and the error is in the "
                    "looking rather than the liquid."},
            {"text": "Because the scale is printed on only one side of the tube",
             "correct": False,
             "why": "The scale can be read from any height; where the eye sits is "
                    "what shifts the value."},
            {"text": "Because a reading taken from above comes out wrong",
             "correct": True},
            {"text": "Because the tap can only be turned while the eye is level",
             "correct": False,
             "why": "The tap works from any position; this is about reading "
                    "rather than pouring."},
        ],
        "figure": None,
    },
    {
        "id": "c6-03-s27",
        "band": "standard",
        "text": "A class has neither an indicator nor a pH meter. Suggest how they"
                " could still tell when the acid had been used up.",
        "options": [
            {"text": "Watch for bubbles, which stop at the end point",
             "correct": False,
             "why": "No gas is produced at any stage of this reaction, so there "
                    "are no bubbles to stop."},
            {"text": "Watch the temperature, which stops rising at the end point",
             "correct": True},
            {"text": "Watch the colour of the mixture, which clears at the end "
                      "point", "correct": False,
             "why": "Both solutions are colourless throughout, so nothing clears."},
            {"text": "Watch the level in the flask, which falls at the end point",
             "correct": False,
             "why": "The level only rises, because alkali keeps being added to it."},
        ],
        "figure": None,
    },
    {
        "id": "c6-03-s28",
        "band": "standard",
        "text": "A neutralised mixture holding a dissolved salt is released into a"
                " river and the fish are unharmed. Explain why.",
        "options": [
            {"text": "The salt is too dilute for anything to notice it",
             "correct": False,
             "why": "Dilution helps, but the reason it is allowed out at all is "
                    "what the substance now is."},
            {"text": "The corrosive substances have been used up making salt and "
                      "water", "correct": True},
            {"text": "The salt settles on the river bed long before it reaches any fish", "correct": False,
             "why": "A dissolved salt travels with the water rather than settling "
                    "out of it."},
            {"text": "The acid is still there but the river neutralises it in "
                      "turn", "correct": False,
             "why": "The acid was used up in the tank; the river is not being "
                    "asked to finish the job."},
        ],
        "figure": None,
    },
    {
        "id": "c6-03-s29",
        "band": "standard",
        "text": "A works could get rid of a tank of dilute acid by adding a great deal"
                " more water instead of neutralising it. Explain why that is not"
                " allowed.",
        "options": [
            {"text": "Because the water released would still be acidic",
             "correct": True},
            {"text": "Because adding water to an acid makes it more concentrated",
             "correct": False,
             "why": "Adding water makes it more dilute; the trouble is that "
                    "dilute acid is still acid."},
            {"text": "Because diluting an acid turns it into an alkali",
             "correct": False,
             "why": "Water moves a reading towards 7 and never carries it past."},
            {"text": "Because the tank would be too heavy to move afterwards",
             "correct": False,
             "why": "Weight is a practical nuisance rather than the reason the "
                    "method is refused."},
        ],
        "figure": None,
    },
    {
        "id": "c6-03-s30",
        "band": "standard",
        "text": "Calcium hydroxide is sprayed as a fine mist into a power station"
                " chimney rather than held in a tank at the bottom. Suggest why.",
        "options": [
            {"text": "So that the gas meets the alkali before it leaves the "
                      "chimney", "correct": True},
            {"text": "So that the alkali is warmed by the hot gas before it reacts with it",
             "correct": False,
             "why": "The reaction needs no warming, and the point is to catch the "
                    "gas rather than heat anything."},
            {"text": "So that the alkali falls back down and can be collected",
             "correct": False,
             "why": "What matters is the meeting with the gas, not the recovery "
                    "of the spray."},
            {"text": "So that less alkali is needed than a tank would hold",
             "correct": False,
             "why": "The amount is set by how much gas there is, not by how it is "
                    "delivered."},
        ],
        "figure": None,
    },
    {
        "id": "c6-03-s31",
        "band": "standard",
        "text": "The indicator is added to the flask holding the acid rather than to"
                " the alkali in the burette. Explain why.",
        "options": [
            {"text": "Because the colour has to be seen in the mixture as the acid "
                      "runs out", "correct": True},
            {"text": "Because indicator reacts with alkalis and would be destroyed",
             "correct": False,
             "why": "Indicator is not destroyed by an alkali; it simply takes its "
                    "alkaline colour."},
            {"text": "Because the burette would be stained and could not be read",
             "correct": False,
             "why": "Glass rinses clean, and staining is not what decides where "
                    "the dye goes."},
            {"text": "Because the indicator has to be measured as carefully as the "
                      "alkali", "correct": False,
             "why": "A few drops are enough and the amount is not measured at "
                    "all."},
        ],
        "figure": None,
    },
    {
        "id": "c6-03-s32",
        "band": "standard",
        "text": "A works neutralises a tank and the meter reads pH 8.5. The tank is"
                " held back rather than released. Explain why.",
        "options": [
            {"text": "Because the reading is too close to 7 to be trusted at all",
             "correct": False,
             "why": "The reading is trusted; it is where it sits that is the "
                    "problem."},
            {"text": "Because a meter cannot report a tank that has been stirred",
             "correct": False,
             "why": "Stirring makes a reading more representative rather than "
                    "less."},
            {"text": "Because the tank is now alkaline rather than neutral",
             "correct": True},
            {"text": "Because the salt made in the tank has not dissolved yet",
             "correct": False,
             "why": "The salt dissolves as it forms, and it is not what the "
                    "reading is reporting."},
        ],
        "figure": None,
    },
    {
        "id": "c6-03-h18",
        "band": "harder",
        "text": "20 cm³ of an alkali exactly neutralises 25 cm³ of an acid. A second"
                " alkali is twice as concentrated. Predict the volume of acid that"
                " 20 cm³ of the second one would neutralise.",
        "options": [
            {"text": "25 cm³",
             "correct": False,
             "why": "The volume added is the same, but each cm³ now carries "
                    "twice as much alkali."},
            {"text": "50 cm³", "correct": True},
            {"text": "12.5 cm³",
             "correct": False,
             "why": "A more concentrated alkali neutralises more acid, not "
                    "less — it is not used up sooner."},
            {"text": "40 cm³",
             "correct": False,
             "why": "The alkali volume has not changed; only what is dissolved in "
                    "it has."},
        ],
        "figure": None,
    },
    {
        "id": "c6-03-h19",
        "band": "harder",
        "text": "A works proposes disposing of a tank of dilute acid by boiling it"
                " until the liquid has gone. Evaluate the plan.",
        "options": [
            {"text": "Sound, because boiling breaks the acid down into harmless "
                      "gases", "correct": False,
             "why": "The acid is not broken down by boiling; the water is simply "
                    "driven off."},
            {"text": "Sound, because an empty tank cannot pollute a river",
             "correct": False,
             "why": "The tank is not empty at the end; what is left is the worst "
                    "part of it."},
            {"text": "Unsound, because the water leaves and the acid is left "
                      "behind", "correct": True},
            {"text": "Unsound, because boiling an acid turns it alkaline",
             "correct": False,
             "why": "Heating does not move a substance to the other side of the "
                    "scale."},
        ],
        "figure": None,
    },
    {
        "id": "c6-03-h20",
        "band": "harder",
        "text": "Three runs of the same titration give volumes that differ from one"
                " another by well over 1 cm³. What does that spread suggest?",
        "options": [
            {"text": "That the acid changed between one run and the next",
             "correct": False,
             "why": "The same acid was used throughout, so the sample is not what "
                    "moved."},
            {"text": "That the end point is not being judged the same way each "
                      "time", "correct": True},
            {"text": "That three runs are too few for any titration",
             "correct": False,
             "why": "Three runs are plenty when the method is consistent; the "
                    "spread is the finding."},
            {"text": "That the alkali becomes weaker each time the burette is "
                      "refilled", "correct": False,
             "why": "Refilling from the same bottle gives the same alkali every "
                    "time."},
        ],
        "figure": None,
    },
    {
        "id": "c6-03-h21",
        "band": "harder",
        "text": "A salt is described as an acid with something swapped. Explain"
                " precisely what has been swapped for what.",
        "options": [
            {"text": "The hydrogen of the acid has been replaced by a metal",
             "correct": True},
            {"text": "The metal of the alkali has been replaced by hydrogen",
             "correct": False,
             "why": "That runs the swap backwards; the hydrogen is the part that "
                    "leaves."},
            {"text": "The water in the acid has been replaced by the alkali",
             "correct": False,
             "why": "Water is made by the reaction rather than being a part that "
                    "gets swapped out."},
            {"text": "The oxygen of the acid has been replaced by a metal",
             "correct": False,
             "why": "Oxygen stays where it is; hydrogen is what the metal takes "
                    "the place of."},
        ],
        "figure": None,
    },
    {
        "id": "c6-03-h22",
        "band": "harder",
        "text": "A thermometer in the flask shows the temperature rising drop by drop"
                " and then holding steady. Explain why it stops rising.",
        "options": [
            {"text": "Because the mixture has reached the temperature of the room",
             "correct": False,
             "why": "It is well above room temperature by then and is on its way "
                    "back down, not stuck."},
            {"text": "Because the salt made is now preventing further heating",
             "correct": False,
             "why": "The salt takes no part; it is a product sitting in the "
                    "water."},
            {"text": "Because there is no acid left, so the reaction has finished",
             "correct": True},
            {"text": "Because the alkali being added is colder than the mixture",
             "correct": False,
             "why": "Every drop was the same temperature, including the ones that "
                    "did warm it."},
        ],
        "figure": None,
    },
    {
        "id": "c6-03-h23",
        "band": "harder",
        "text": "Neutralisation is used on an acidic lake, an acidic field, an acidic"
                " stomach and a tank of acidic waste. State what all four have in"
                " common.",
        "options": [
            {"text": "A base is added to bring the pH up towards 7",
             "correct": True},
            {"text": "An acid is added to bring the pH down towards 7",
             "correct": False,
             "why": "All four problems are already acidic, so adding acid would "
                    "make each of them worse."},
            {"text": "Water is added until the pH reaches 7", "correct": False,
             "why": "Water moves a reading towards 7 without ever getting there, "
                    "and none of the four is treated that way."},
            {"text": "The acid is boiled away until nothing is left",
             "correct": False,
             "why": "None of these is treated by heating, and a lake or a field "
                    "could not be."},
        ],
        "figure": None,
    },
    {
        "id": "c6-03-h24",
        "band": "harder",
        "text": "A works neutralises thousands of litres of acid with a cheap"
                " insoluble base rather than with sodium hydroxide. Suggest two"
                " advantages.",
        "options": [
            {"text": "It costs far less, and any excess does not leave a strong "
                      "alkali in the water", "correct": True},
            {"text": "It costs far less, and it neutralises acid that no soluble base could deal with", "correct": False,
             "why": "Both kinds neutralise the same acid; solubility does not "
                    "extend what can be treated."},
            {"text": "It works faster, and it makes a salt that cannot dissolve "
                      "in water", "correct": False,
             "why": "An insoluble base reacts more slowly, and the salt made is "
                    "usually soluble."},
            {"text": "It needs no measuring, and it cannot push the tank past "
                      "neutral at all", "correct": False,
             "why": "An excess of any base can carry a tank past 7, so the "
                    "measuring still matters."},
        ],
        "figure": None,
    },
    {
        "id": "c6-03-h25",
        "band": "harder",
        "text": "A student runs the acid into the alkali instead of the alkali into"
                " the acid. Predict the effect on the volumes at which the two"
                " exactly cancel.",
        "options": [
            {"text": "Less acid will be needed, because it is going in second",
             "correct": False,
             "why": "Which solution goes in second does not change how much of "
                    "each is required."},
            {"text": "The same volumes cancel, whichever order they are mixed",
             "correct": True},
            {"text": "More acid will be needed, because the alkali is spread out",
             "correct": False,
             "why": "Spreading a solution out does not alter how much of it there "
                    "is to react."},
            {"text": "No exact cancelling is possible in that direction",
             "correct": False,
             "why": "The point of exact cancelling is reached from either "
                    "direction."},
        ],
        "figure": None,
    },
    {
        "id": "c6-03-h26",
        "band": "harder",
        "text": "A student argues that because neutralisation involves heat, the"
                " beaker must be warmed before the reaction will start. Evaluate.",
        "options": [
            {"text": "Sound, because a reaction involving heat has to be heated "
                      "first", "correct": False,
             "why": "Some reactions need heating and some release it; this one "
                    "releases it."},
            {"text": "Sound, because the beaker is warm while the reaction is "
                      "happening", "correct": False,
             "why": "It is warm because the reaction is warming it, which is the "
                    "opposite of what is claimed."},
            {"text": "Unsound, because the reaction gives heat out and starts on "
                      "mixing", "correct": True},
            {"text": "Unsound, because the reaction neither takes in nor gives "
                      "out heat", "correct": False,
             "why": "A thermometer in the flask plainly shows the temperature "
                    "rising."},
        ],
        "figure": None,
    },
    {
        "id": "c6-03-h27",
        "band": "harder",
        "text": "Two beakers of the same acid are neutralised, one with a soluble"
                " alkali and one with an insoluble base, and too much is added to"
                " each. Compare what can be seen in the two beakers.",
        "options": [
            {"text": "Both look the same, because every base dissolves once it "
                      "has reacted", "correct": False,
             "why": "A base that will not dissolve does not dissolve merely "
                    "because some of it has reacted."},
            {"text": "The excess alkali stays dissolved; the excess base is left "
                      "as a solid", "correct": True},
            {"text": "The excess alkali is left as a solid; the excess base "
                      "dissolves", "correct": False,
             "why": "An alkali is by definition the one that dissolves, so that "
                    "is the wrong way round."},
            {"text": "Both beakers hold a solid, because an excess always settles "
                      "out", "correct": False,
             "why": "Excess alkali remains in solution and cannot be seen at all."},
        ],
        "figure": None,
    },
    {
        "id": "c6-03-h28",
        "band": "harder",
        "text": "25 cm³ of an acid needs 20 cm³ of alkali. A student pours the same"
                " 25 cm³ of acid into a flask, adds 20 cm³ of water to it, and"
                " titrates again. Predict the volume of alkali now needed.",
        "options": [
            {"text": "10 cm³, because the acid has been halved", "correct": False,
             "why": "Adding water spreads the acid out; it does not remove any of "
                    "it."},
            {"text": "40 cm³, because the flask now holds twice as much liquid",
             "correct": False,
             "why": "The volume of liquid has grown, but the amount of acid in it "
                    "has not."},
            {"text": "20 cm³, because the amount of acid is unchanged",
             "correct": True},
            {"text": "None, because the acid is now too dilute to react",
             "correct": False,
             "why": "A dilute acid reacts perfectly well; it simply takes longer "
                    "to meet the alkali."},
        ],
        "figure": None,
    },
    {
        "id": "c6-03-h29",
        "band": "harder",
        "text": "A field is limed in the autumn and reads the same pH as before when"
                " it is tested a year later. Suggest the most likely explanation.",
        "options": [
            {"text": "The lime has been used up and the soil has gone on turning "
                      "acidic", "correct": True},
            {"text": "Lime cannot change the pH of a soil for more than a few hours at a time", "correct": False,
             "why": "Liming holds a field for a season or more, which is why it "
                    "is worth doing."},
            {"text": "The pH meter has been used on the wrong part of the field",
             "correct": False,
             "why": "That would explain one odd reading rather than a year's "
                    "worth of farming."},
            {"text": "The lime has turned acidic where it lay in the ground",
             "correct": False,
             "why": "A base does not become an acid by sitting in soil."},
        ],
        "figure": None,
    },
    {
        "id": "c6-03-h30",
        "band": "harder",
        "text": "A student is told to neutralise 25 cm³ of acid exactly, but has only"
                " a measuring cylinder to add the alkali with. Evaluate that.",
        "options": [
            {"text": "Sound, because a cylinder measures volume just as a burette "
                      "does", "correct": False,
             "why": "Both measure volume, and only one of them can deliver a "
                    "single drop at the end."},
            {"text": "Sound, because the exact point does not matter as long as "
                      "the colour changes", "correct": False,
             "why": "The exact point is the whole purpose of the measurement."},
            {"text": "Unsound, because the last drop cannot be added or read "
                      "finely enough", "correct": True},
            {"text": "Unsound, because a measuring cylinder cannot hold an "
                      "alkali safely", "correct": False,
             "why": "A cylinder holds dilute alkali perfectly safely; precision "
                    "is what it lacks."},
        ],
        "figure": None,
    },
    {
        "id": "c6-03-h31",
        "band": "harder",
        "text": "A works adds exactly the calculated mass of base to a tank of acid"
                " and the meter then reads 6.2. Suggest the most likely reason.",
        "options": [
            {"text": "The acid was more concentrated than the calculation assumed",
             "correct": True},
            {"text": "The base reacted with the tank instead of with the acid",
             "correct": False,
             "why": "A tank built for acid is not consuming the base, and that "
                    "would not leave the reading acidic by so little."},
            {"text": "The reading is wrong, because a neutralised tank must read 7",
             "correct": False,
             "why": "A tank reads 7 only when the amounts matched, and here they "
                    "evidently did not."},
            {"text": "Too much base was added, which pushes a reading below 7",
             "correct": False,
             "why": "Excess base carries a reading above 7, not below it."},
        ],
        "figure": None,
    },
    {
        "id": "c6-03-h32",
        "band": "harder",
        "text": "Compare what happens to the pH of an acid when water is added to it"
                " with what happens when alkali is added.",
        "options": [
            {"text": "Water carries it past 7; alkali stops it just short of 7",
             "correct": False,
             "why": "That reverses the two: water is the one that cannot reach 7."},
            {"text": "Both carry the reading past 7 in the end", "correct": False,
             "why": "However much water is added, some acid remains in every "
                    "sample of the mixture."},
            {"text": "Water moves it towards 7 and stops; alkali carries it past",
             "correct": True},
            {"text": "Both leave the reading where it was, since neither is an "
                      "acid", "correct": False,
             "why": "Alkali plainly moves the reading, which is what a titration "
                    "records."},
        ],
        "figure": None,
    },
]
