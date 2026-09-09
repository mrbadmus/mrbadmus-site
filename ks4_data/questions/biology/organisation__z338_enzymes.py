"""Biology · Organisation — the MRB-338 expansion of `enzymes`.

One leaf only: AQA 8461 §4.2.2.2, the enzyme itself. The original twelve rows
in `organisation.py` take the protein, the 37 C optimum, the definition of a
catalyst, the iodine test in RP3, the 10-30 C rise, pancreatic enzymes dropped
into acid, what the RP3 timing measures, why the body does not run at 50 C,
5 C against 70 C, the word "killed", amylase reaching the stomach, and two
beakers at pH 7 and pH 3. This file takes what they leave: the active site,
the substrate, the enzyme-substrate complex and the lock-and-key mapping
itself; the three digestive families and their products and where they are
made; why a product has to be small and soluble; rate arithmetic with real
times; the control variables and the sampling error of RP3; and the
misconception set from the wrong side — the model reversed, the enzyme
confused with its substrate, an enzyme "used up", a boiled enzyme recovering
on cooling, a lower pH read as always faster, and two points read as a law.

The weight follows the CONTENT. `easier` stays at eight because recall here is
a short vocabulary — four named structures and three substrate-to-product
pairs — and a ninth way of asking it is the same question in new words. The
demand lives in applying specificity and optimum conditions to a context the
child has not met, and in arithmetic on times and rates, so `standard` and
`harder` carry twenty-two each.

Boundaries with the two leaves being written alongside this one: the named
digestive organs, the route food takes, bile and the food tests belong to
`digestive-system`; the cell-tissue-organ-system hierarchy belongs to
`principles-of-organisation`. What is here is the enzyme.

Numbers are the ones the biology supplies — clearance times, a mean of three
repeats, and rate as 1000 divided by the time — and every one comes out exact.
Chemical formulae stay flat, and no stem refers to a diagram, a graph or a
table.
"""

TOPIC = "organisation"
SUBJECT = "biology"

QUESTIONS = [
    # ══ easier · e05-e12 ═══════════════════════════════════════════════
    # The active site, the substrate, the enzyme-substrate complex, the
    # word for the permanent change, the three families' products, and the
    # organ that supplies all three.
    {
        "id": "ks4-enzymes-e05",
        "subtopic_slug": "enzymes",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the region of an enzyme molecule that a substrate binds "
                "to.",
        "options": [
            "The active site",
            "The enzyme-substrate complex",
            "The optimum pH",
            "The substrate",
        ],
        "correct_index": 0,
        "why": "The active site is the region of the folded protein whose "
               "shape the substrate fits into.",
    },
    {
        "id": "ks4-enzymes-e06",
        "subtopic_slug": "enzymes",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State what is meant by the substrate of an enzyme.",
        "options": [
            "The product the enzyme releases at the end of the reaction",
            "The protein that the enzyme itself is built from",
            "The energy that the enzyme uses up while it works",
            "The molecule that the enzyme acts on",
        ],
        "correct_index": 3,
        "why": "The substrate is the molecule that fits the active site and "
               "is changed by the enzyme.",
    },
    {
        "id": "ks4-enzymes-e07",
        "subtopic_slug": "enzymes",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the structure that forms when a substrate fits into an "
                "active site.",
        "options": [
            "A denatured enzyme",
            "An enzyme-substrate complex",
            "A second, empty active site",
            "A biological catalyst",
        ],
        "correct_index": 1,
        "why": "Substrate bound in the active site is called an "
               "enzyme-substrate complex; the products leave it afterwards.",
    },
    {
        "id": "ks4-enzymes-e08",
        "subtopic_slug": "enzymes",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the permanent change to an enzyme's active site caused "
                "by a very high temperature.",
        "options": [
            "Digestion",
            "Emulsification",
            "Denaturation",
            "Respiration",
        ],
        "correct_index": 2,
        "why": "Very high temperatures make the protein vibrate so much that "
               "the active site's shape is permanently changed — "
               "denaturation.",
    },
    {
        "id": "ks4-enzymes-e09",
        "subtopic_slug": "enzymes",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Carbohydrase enzymes such as amylase digest starch. State "
                "the products.",
        "options": [
            "Amino acids",
            "Simple sugars",
            "Fatty acids and glycerol",
            "Glycerol only",
        ],
        "correct_index": 1,
        "why": "A carbohydrase breaks a carbohydrate such as starch down into "
               "simple sugars.",
    },
    {
        "id": "ks4-enzymes-e10",
        "subtopic_slug": "enzymes",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the products made when a protease enzyme digests a "
                "protein.",
        "options": [
            "Simple sugars",
            "Fatty acids and glycerol",
            "Amino acids",
            "Glucose and glycerol",
        ],
        "correct_index": 2,
        "why": "Proteases break proteins down into amino acids, which the "
               "body then uses to build its own proteins.",
    },
    {
        "id": "ks4-enzymes-e11",
        "subtopic_slug": "enzymes",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State what the optimum pH of an enzyme tells you about that "
                "enzyme.",
        "options": [
            "The pH at which the enzyme is destroyed",
            "The pH found inside the stomach",
            "The pH at which the enzyme is made",
            "The pH at which the enzyme works fastest",
        ],
        "correct_index": 3,
        "why": "An enzyme's optimum pH is the pH at which its active site "
               "holds the shape that gives the fastest rate.",
    },
    {
        "id": "ks4-enzymes-e12",
        "subtopic_slug": "enzymes",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the organ that makes amylase, protease and lipase and "
                "releases all three into the small intestine.",
        "options": [
            "The pancreas",
            "The liver",
            "The stomach",
            "The gall bladder",
        ],
        "correct_index": 0,
        "why": "The pancreas produces all three families of digestive enzyme "
               "and secretes them into the small intestine.",
    },

    # ══ standard · s05-s26 ════════════════════════════════════════════
    # Specificity and optimum conditions applied to a familiar context,
    # the arithmetic of rate, and the control variables of RP3.
    {
        "id": "ks4-enzymes-s05",
        "subtopic_slug": "enzymes",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A very small mass of amylase can digest a very large mass of "
                "starch. Explain how this is possible.",
        "options": [
            "The amylase splits into two smaller enzymes each time, doubling "
            "the number of molecules present",
            "The amylase is released unchanged each time, so it catalyses the "
            "reaction again and again",
            "The amylase joins on to the starch for good, so a little spreads "
            "through the mixture",
            "The amylase grows larger as it works, so it can reach more "
            "starch as time passes",
        ],
        "correct_index": 1,
        "why": "An enzyme is a catalyst: it is not used up, so one molecule "
               "works on molecule after molecule of substrate.",
    },
    {
        "id": "ks4-enzymes-s06",
        "subtopic_slug": "enzymes",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A liver cell carries out hundreds of different chemical "
                "reactions. Explain why it must make many different enzymes "
                "rather than one.",
        "options": [
            "Each enzyme is destroyed by the reaction it catalyses, so a "
            "fresh one is needed",
            "Each enzyme works for only a short time each day, so a great "
            "many are needed",
            "Each active site fits only one substrate, so a different enzyme "
            "is needed for each reaction",
            "Enzymes wear out with use, so the cell keeps spare copies of the "
            "same one",
        ],
        "correct_index": 2,
        "why": "Enzymes are specific: the shape of the active site is "
               "complementary to one substrate only, so each reaction needs "
               "its own enzyme.",
    },
    {
        "id": "ks4-enzymes-s07",
        "subtopic_slug": "enzymes",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Starch was completely digested in 50 seconds. Rate can be "
                "calculated as 1000 divided by the time in seconds. Calculate "
                "the rate.",
        "options": [
            "0.05 per second",
            "50 per second",
            "500 per second",
            "20 per second",
        ],
        "correct_index": 3,
        "why": "1000 / 50 = 20 per second.",
    },
    {
        "id": "ks4-enzymes-s08",
        "subtopic_slug": "enzymes",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "An enzyme digested 60 mg of starch in 30 seconds. Calculate "
                "the rate of digestion.",
        "options": [
            "2 mg per second",
            "0.5 mg per second",
            "30 mg per second",
            "1800 mg per second",
        ],
        "correct_index": 0,
        "why": "Rate = amount / time = 60 / 30 = 2 mg per second.",
    },
    {
        "id": "ks4-enzymes-s09",
        "subtopic_slug": "enzymes",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Milk kept in a fridge at 4 C stays fresh far longer than "
                "milk left at 20 C. Explain why, in terms of the enzymes of "
                "the microorganisms that spoil it.",
        "options": [
            "The enzymes have had their shape changed for good by the cold, "
            "so they can never work again",
            "The molecules move more slowly, so fewer collide with an active "
            "site each second",
            "The microorganisms switch to making a different enzyme with no "
            "effect on milk at all",
            "The enzymes are used up much faster in the cold, so far fewer of "
            "them remain",
        ],
        "correct_index": 1,
        "why": "Cooling lowers kinetic energy, so there are fewer "
               "enzyme-substrate collisions each second and the rate falls.",
    },
    {
        "id": "ks4-enzymes-s10",
        "subtopic_slug": "enzymes",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student investigating pH uses a different volume of "
                "amylase solution in each mixture. Explain why the results "
                "cannot be trusted.",
        "options": [
            "The amount of enzyme has changed as well as the pH, so the cause "
            "of any difference is unknown",
            "The amylase would be used up in the mixtures that received the "
            "smaller volume of enzyme",
            "A larger volume of amylase cools each mixture down, and that is "
            "what changed the rate",
            "Extra amylase warms the mixture, which is what would change the "
            "rate instead",
        ],
        "correct_index": 0,
        "why": "Only the independent variable may change: if the enzyme "
               "volume varies too, a difference in time cannot be attributed "
               "to pH.",
    },
    {
        "id": "ks4-enzymes-s11",
        "subtopic_slug": "enzymes",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Digestive enzymes are released into the gut rather than "
                "being kept inside the body's cells. Suggest why this is "
                "necessary.",
        "options": [
            "Enzymes are too large to be held inside a cell, so they have to "
            "be let out of it",
            "Enzymes only work when they are in contact with the air that is "
            "in the gut",
            "The food molecules are too large to enter a cell, so they must "
            "be digested outside one",
            "The gut is much warmer than a cell is, so the enzymes work "
            "faster there",
        ],
        "correct_index": 2,
        "why": "Digestion happens in the gut cavity because starch, protein "
               "and lipid molecules are far too large to cross a cell "
               "membrane.",
    },
    {
        "id": "ks4-enzymes-s12",
        "subtopic_slug": "enzymes",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why the protein in a meal cannot be used to build a "
                "person's own body proteins until it has been digested.",
        "options": [
            "It must first be broken into simple sugars, which the body then "
            "rebuilds into its own proteins",
            "It must first be broken into amino acids, which the body then "
            "joins in its own order",
            "It must first be broken by stomach acid alone, because no enzyme "
            "acts on a whole protein",
            "It must first be dissolved by bile, which carries protein "
            "straight into the blood",
        ],
        "correct_index": 1,
        "why": "Proteases digest protein to amino acids; the body then "
               "assembles those amino acids into proteins of its own.",
    },
    {
        "id": "ks4-enzymes-s13",
        "subtopic_slug": "enzymes",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A protease is added to a starch solution at 37 C and left "
                "for an hour. Predict what happens, and explain why.",
        "options": [
            "No digestion, because the shape of the protease's active site "
            "does not fit starch",
            "Starch is digested slowly, because a protease acts on starch but "
            "far less quickly than amylase",
            "The protease is digested, because starch is the larger molecule "
            "and so acts on the enzyme",
            "All the starch is digested, because every enzyme breaks down any "
            "large food molecule",
        ],
        "correct_index": 0,
        "why": "Enzymes are specific: starch does not fit a protease's active "
               "site, so no enzyme-substrate complex can form.",
    },
    {
        "id": "ks4-enzymes-s14",
        "subtopic_slug": "enzymes",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Saliva contains amylase but no protease. Explain why the "
                "protein in a mouthful of food is not digested while it is in "
                "the mouth.",
        "options": [
            "Protein is too large for any enzyme to act on until it has been "
            "broken up into much smaller pieces",
            "Protein is digested in the mouth, but so slowly that the change "
            "could never be measured",
            "Amylase digests protein too, but only once the pH in the mouth "
            "has fallen to 2",
            "Amylase's active site fits starch, and there is no enzyme "
            "present that fits protein",
        ],
        "correct_index": 3,
        "why": "Chemical digestion needs an enzyme whose active site fits the "
               "substrate; saliva supplies one for starch only.",
    },
    {
        "id": "ks4-enzymes-s15",
        "subtopic_slug": "enzymes",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "The liquid leaving the stomach is strongly acidic. Explain "
                "why it must be made alkaline before the enzymes of the small "
                "intestine work at their fastest.",
        "options": [
            "Those enzymes have an optimum pH of about 8, and away from it "
            "the active site changes shape",
            "Acid dissolves those enzymes completely, so none of them would "
            "be left in the intestine",
            "Alkali is the substrate those enzymes act on, so they cannot "
            "begin to work at all",
            "Acid makes those enzymes work far too quickly for the food to be "
            "fully digested",
        ],
        "correct_index": 0,
        "why": "Pancreatic enzymes have an optimum pH of about 7-8; at a low "
               "pH the active site's shape is altered and the rate falls.",
    },
    {
        "id": "ks4-enzymes-s16",
        "subtopic_slug": "enzymes",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "An enzyme has been held at 90 C for ten minutes. Explain why "
                "it can no longer catalyse its reaction.",
        "options": [
            "It has run out of the energy it needs in order to hold a "
            "substrate in place while it is working",
            "The heat has used the enzyme up, so none of it is left in the "
            "mixture at all",
            "The shape of its active site has been changed, so the substrate "
            "no longer fits into it",
            "It has been killed, and a protein that has died can take no part "
            "in a reaction",
        ],
        "correct_index": 2,
        "why": "Heat above the optimum permanently alters the active site's "
               "shape, so no enzyme-substrate complex can form.",
    },
    {
        "id": "ks4-enzymes-s17",
        "subtopic_slug": "enzymes",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Amylase solution is boiled and then cooled back to 37 C "
                "before starch is added. Predict what happens to the starch.",
        "options": [
            "All of it is digested, but slowly, because boiling removes only "
            "some of the amylase there",
            "None is digested, because the change boiling made to the active "
            "site cannot be undone",
            "All of it is digested, because cooling returns the active site "
            "to the shape it held before",
            "None is digested, because boiling takes away the ability of the "
            "starch to dissolve",
        ],
        "correct_index": 1,
        "why": "Denaturation is permanent: cooling does not restore the shape "
               "of the active site.",
    },
    {
        "id": "ks4-enzymes-s18",
        "subtopic_slug": "enzymes",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Starch was cleared by amylase in 200 seconds at pH 4 and in "
                "50 seconds at pH 6. Calculate how many times faster the "
                "reaction was at pH 6.",
        "options": [
            "2 times faster",
            "150 times faster",
            "0.25 times faster",
            "4 times faster",
        ],
        "correct_index": 3,
        "why": "200 / 50 = 4, so the reaction at pH 6 was four times as fast.",
    },
    {
        "id": "ks4-enzymes-s19",
        "subtopic_slug": "enzymes",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "The rate of an enzyme-catalysed reaction fell from 25 units "
                "to 5 units when the pH was changed. Calculate the percentage "
                "decrease in rate.",
        "options": [
            "20%",
            "5%",
            "80%",
            "500%",
        ],
        "correct_index": 2,
        "why": "The fall is 25 - 5 = 20 units; 20 / 25 x 100 = 80%.",
    },
    {
        "id": "ks4-enzymes-s20",
        "subtopic_slug": "enzymes",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Starch was cleared in 125 seconds at pH 5 and in 40 seconds "
                "at pH 7. Taking rate as 1000 divided by the time in seconds, "
                "calculate the difference between the two rates.",
        "options": [
            "17 per second",
            "8 per second",
            "25 per second",
            "85 per second",
        ],
        "correct_index": 0,
        "why": "1000 / 125 = 8 and 1000 / 40 = 25, so the difference is 25 - "
               "8 = 17 per second.",
    },
    {
        "id": "ks4-enzymes-s21",
        "subtopic_slug": "enzymes",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "The concentration of amylase in a starch mixture is doubled "
                "and everything else is kept the same. Predict the effect on "
                "the time taken to digest the starch.",
        "options": [
            "It falls to zero, because twice as much enzyme digests all of "
            "the starch the instant it is added",
            "It falls, because more active sites are available for the starch "
            "to collide with",
            "It stays the same, because the mass of starch present sets the "
            "time, not the enzyme",
            "It rises, because the enzyme molecules now get in one another's "
            "way as they try to work",
        ],
        "correct_index": 1,
        "why": "More enzyme means more active sites, so more enzyme-substrate "
               "complexes form each second and the starch goes sooner.",
    },
    {
        "id": "ks4-enzymes-s22",
        "subtopic_slug": "enzymes",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Amylase is mixed with starch at 37 C. Explain why the "
                "reaction eventually stops even though the amylase has not "
                "been used up.",
        "options": [
            "All the starch has been digested, so there is no substrate left "
            "to bind to",
            "The amylase slowly changes shape at 37 C, so in the end it can "
            "no longer bind starch at all",
            "The sugars that are made stay stuck in the active sites and are "
            "never released",
            "The amylase reaches the end of the reactions any enzyme is able "
            "to catalyse",
        ],
        "correct_index": 0,
        "why": "The enzyme survives, but the reaction stops once the "
               "substrate has all been converted to product.",
    },
    {
        "id": "ks4-enzymes-s23",
        "subtopic_slug": "enzymes",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student leaves one amylase mixture on a warm windowsill "
                "and keeps the rest in a 37 C water bath. Explain why the "
                "results cannot be compared fairly.",
        "options": [
            "Sunlight destroys amylase, so the mixture on the windowsill has "
            "no working enzyme in it",
            "Amylase only works inside a water bath, so no digestion happens "
            "on a windowsill at all",
            "Temperature changes enzyme rate too, so a difference could be "
            "caused by warmth and not by pH",
            "The windowsill mixture ends up at a different pH, because warm "
            "liquid turns acidic",
        ],
        "correct_index": 2,
        "why": "Temperature is a control variable here: if it varies as well, "
               "the effect of pH cannot be separated from it.",
    },
    {
        "id": "ks4-enzymes-s24",
        "subtopic_slug": "enzymes",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why the starch solution and the amylase are each "
                "left in a 37 C water bath before they are mixed together.",
        "options": [
            "So that the amylase has time to build up the energy that the "
            "reaction is going to need",
            "So that both are already at the test temperature the moment the "
            "reaction begins",
            "So that the starch has time to dissolve completely before the "
            "enzyme arrives",
            "So that any bacteria in the two solutions are killed before the "
            "test",
        ],
        "correct_index": 1,
        "why": "Pre-warming means the reaction runs at the stated temperature "
               "from the start, rather than warming up during the timing.",
    },
    {
        "id": "ks4-enzymes-s25",
        "subtopic_slug": "enzymes",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A person's pancreas produces no lipase. Explain the effect "
                "on the food they eat.",
        "options": [
            "Lipids are digested more slowly, because bile on its own can "
            "still complete the job in good time",
            "Starch is not digested to simple sugars, so no sugar can be "
            "taken into the blood at all",
            "Proteins are not digested to amino acids, so none of them can be "
            "absorbed at all",
            "Lipids are not digested to fatty acids and glycerol, so they "
            "cannot be absorbed",
        ],
        "correct_index": 3,
        "why": "Lipase is the enzyme that digests lipids; without it they "
               "stay as large insoluble molecules and pass through "
               "undigested.",
    },
    {
        "id": "ks4-enzymes-s26",
        "subtopic_slug": "enzymes",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A biological washing powder contains protease. Explain why "
                "it removes a blood stain but has little effect on an oily "
                "stain.",
        "options": [
            "The protease's active site fits protein, and the oil is a lipid "
            "of a different shape",
            "The protease digests any stain given time, and an ordinary wash "
            "is simply far too short for oil",
            "The protease is broken apart by oil, so the enzyme is destroyed "
            "before it can act at all",
            "The protease works only on stains that are coloured, and oil has "
            "no colour",
        ],
        "correct_index": 0,
        "why": "Blood is stained by protein, which fits a protease's active "
               "site; oil is a lipid and would need lipase.",
    },

    # ══ harder · h05-h26 ══════════════════════════════════════════════
    # Unfamiliar contexts, rearranged and multi-step calculation, compare
    # and evaluate, and the misconception set met from the wrong side.
    {
        "id": "ks4-enzymes-h05",
        "subtopic_slug": "enzymes",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student writes that in the lock and key model the "
                "substrate is the lock and the enzyme is the key. Evaluate "
                "this statement.",
        "options": [
            "Wrong round: the model actually makes the product the lock and "
            "the enzyme the key that it turns",
            "Correct: the substrate is the larger of the two molecules, and "
            "so it must be the lock",
            "Wrong round: the enzyme's active site is the lock and the "
            "substrate is the key",
            "Correct: the substrate keeps its shape while the enzyme alters "
            "itself to fit it",
        ],
        "correct_index": 2,
        "why": "The active site is the lock, with a fixed shape; the "
               "substrate is the key that fits it.",
    },
    {
        "id": "ks4-enzymes-h06",
        "subtopic_slug": "enzymes",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Pepsin digests protein in the stomach and a pancreatic "
                "protease digests protein in the small intestine. Explain why "
                "the body makes two different protein-digesting enzymes.",
        "options": [
            "The two places have very different pH values, and each enzyme "
            "keeps its active site at one of them",
            "The two enzymes make different products, one giving sugars and "
            "the other giving amino acids",
            "One of them digests protein that came from an animal and the "
            "other from a plant",
            "Pepsin is used up as it works in the stomach, so a fresh enzyme "
            "is needed further along",
        ],
        "correct_index": 0,
        "why": "Each protease has an optimum pH matched to where it works — "
               "about 2 for pepsin, about 8 in the small intestine.",
    },
    {
        "id": "ks4-enzymes-h07",
        "subtopic_slug": "enzymes",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A reaction had a rate of 8 per second, where rate is 1000 "
                "divided by the time in seconds. Calculate the time the "
                "reaction took.",
        "options": [
            "8 seconds",
            "125 seconds",
            "8000 seconds",
            "0.008 seconds",
        ],
        "correct_index": 1,
        "why": "Rearranging, time = 1000 / rate = 1000 / 8 = 125 seconds.",
    },
    {
        "id": "ks4-enzymes-h08",
        "subtopic_slug": "enzymes",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "An enzyme digested 45 mg of starch in 90 seconds at 20 C, "
                "and the same 45 mg in 30 seconds at 37 C. Calculate the "
                "increase in rate.",
        "options": [
            "0.5 mg per second",
            "3.0 mg per second",
            "60 mg per second",
            "1.0 mg per second",
        ],
        "correct_index": 3,
        "why": "45 / 90 = 0.5 and 45 / 30 = 1.5 mg per second, so the "
               "increase is 1.0 mg per second.",
    },
    {
        "id": "ks4-enzymes-h09",
        "subtopic_slug": "enzymes",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Two identical samples of amylase are kept for twenty "
                "minutes, one at 45 C and one at 37 C. Both are then brought "
                "to 37 C and tested on starch. Predict which digests the "
                "starch faster.",
        "options": [
            "The sample kept at 45 C, because the extra warmth leaves its "
            "molecules with more energy",
            "The sample kept at 45 C, because warming an enzyme first makes "
            "its active site fit better",
            "The sample kept at 37 C, because heat above the optimum has "
            "altered the other's active site for good",
            "Neither, because both are at 37 C by the time the starch is "
            "added to them",
        ],
        "correct_index": 2,
        "why": "45 C is above human amylase's optimum, so that sample is "
               "partly denatured before the test and cannot recover.",
    },
    {
        "id": "ks4-enzymes-h10",
        "subtopic_slug": "enzymes",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student suggests that if the stomach were even more "
                "acidic, at pH 1, protein would be digested faster. Evaluate "
                "this suggestion.",
        "options": [
            "Right: the more acid that is present, the faster any protein in "
            "the stomach will be broken apart",
            "Wrong: pepsin's optimum is about pH 2, so moving further from it "
            "slows the enzyme down",
            "Wrong: pepsin has no optimum pH at all, so the acid in the "
            "stomach makes no difference to it",
            "Right: acid is the catalyst for protein digestion, so more "
            "always gives a faster rate",
        ],
        "correct_index": 1,
        "why": "Rate is highest at the optimum pH; below it, the active "
               "site's shape is altered and the rate falls.",
    },
    {
        "id": "ks4-enzymes-h11",
        "subtopic_slug": "enzymes",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Some bacteria live in hot springs at 80 C. Suggest what must "
                "be true of their enzymes.",
        "options": [
            "They keep the shape of their active site at a temperature that "
            "would change a human enzyme's",
            "They work without an active site at all, which is the reason "
            "that a high temperature cannot affect them",
            "They are not proteins, which is the reason the heat of the "
            "spring is unable to alter them",
            "They work only above 80 C, so they stop completely if the water "
            "of the spring cools",
        ],
        "correct_index": 0,
        "why": "An enzyme's optimum matches its organism's conditions; these "
               "enzymes stay correctly folded at temperatures that denature "
               "ours.",
    },
    {
        "id": "ks4-enzymes-h12",
        "subtopic_slug": "enzymes",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Enzymes are used in industry for reactions that would "
                "otherwise need high temperatures and strong acids. Suggest "
                "one advantage of using them.",
        "options": [
            "They keep working at every temperature and at every pH, so no "
            "condition has to be controlled",
            "They are turned into the product themselves, so less raw "
            "material has to be bought in",
            "They make a reaction happen that simply could not happen at any "
            "temperature",
            "They work quickly in mild conditions, so less energy is needed "
            "to run the process",
        ],
        "correct_index": 3,
        "why": "Enzymes catalyse reactions rapidly near room temperature and "
               "neutral pH, which cuts the energy the process needs.",
    },
    {
        "id": "ks4-enzymes-h13",
        "subtopic_slug": "enzymes",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student writes: 'The protein breaks pepsin down into amino "
                "acids.' Explain what is wrong with this sentence.",
        "options": [
            "Only the product is wrong: the protein breaks pepsin down into "
            "simple sugars rather than into amino acids",
            "Only the product is wrong: pepsin breaks protein down into fatty "
            "acids and glycerol, not amino acids",
            "The two molecules are the wrong way round: pepsin is the enzyme "
            "and protein is the substrate",
            "Nothing breaks pepsin down: the protein in the stomach is "
            "digested by the hydrochloric acid",
        ],
        "correct_index": 2,
        "why": "Pepsin is the enzyme and protein is its substrate, so pepsin "
               "digests the protein to amino acids.",
    },
    {
        "id": "ks4-enzymes-h14",
        "subtopic_slug": "enzymes",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A reaction makes 24 mg of product in the first two minutes "
                "and only 6 mg in the next two minutes. Explain the fall in "
                "rate.",
        "options": [
            "The product coats every enzyme molecule for good, so not one "
            "active site can ever be freed again",
            "The enzyme has been denatured by the product it made, which is "
            "why the rate falls away",
            "Nearly all the enzyme was used up in the first two minutes, so "
            "little of it is left",
            "Much of the substrate has already been used, so fewer collisions "
            "with active sites happen",
        ],
        "correct_index": 3,
        "why": "As substrate is converted, its concentration falls, so fewer "
               "enzyme-substrate complexes form each second.",
    },
    {
        "id": "ks4-enzymes-h15",
        "subtopic_slug": "enzymes",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Three repeats gave times of 76, 80 and 84 seconds. Taking "
                "rate as 1000 divided by the mean time in seconds, calculate "
                "the rate.",
        "options": [
            "12.0 per second",
            "12.5 per second",
            "80 per second",
            "4.2 per second",
        ],
        "correct_index": 1,
        "why": "The mean time is (76 + 80 + 84) / 3 = 80 s, and 1000 / 80 = "
               "12.5 per second.",
    },
    {
        "id": "ks4-enzymes-h16",
        "subtopic_slug": "enzymes",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Two proteases, A and B, have optimum pH values of 2 and 8. "
                "Both are added to a protein meal inside the stomach. Predict "
                "what happens.",
        "options": [
            "Both digest the protein, because they are both proteases and the "
            "stomach is at the right temperature too",
            "B digests the protein and A does not, because a higher optimum "
            "pH always means a faster enzyme",
            "Neither digests the protein, because two enzymes in one place "
            "block each other's active sites",
            "A digests the protein and B does not, because the stomach's pH "
            "is far from B's optimum",
        ],
        "correct_index": 3,
        "why": "The stomach is about pH 2, so A is at its optimum while B's "
               "active site is altered and it cannot work.",
    },
    {
        "id": "ks4-enzymes-h17",
        "subtopic_slug": "enzymes",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest why a very small change to the shape of an enzyme's "
                "active site can stop the enzyme working altogether.",
        "options": [
            "The active site is the only part of an enzyme that there is, so "
            "any change destroys the molecule",
            "A change of shape makes the enzyme heavier, so it can no longer "
            "reach the substrate it acts on",
            "A change of shape turns the enzyme into a substrate, which "
            "another enzyme digests",
            "The site and the substrate have to match exactly, so even a "
            "small change stops them binding",
        ],
        "correct_index": 3,
        "why": "Catalysis depends on the substrate fitting the active site "
               "exactly, so a small mismatch prevents the complex forming.",
    },
    {
        "id": "ks4-enzymes-h18",
        "subtopic_slug": "enzymes",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student tests a drop of the mixture with iodine every 30 "
                "seconds. Explain why the time recorded for the starch to "
                "disappear may be longer than the true time.",
        "options": [
            "The starch may have gone at any point during the 30 seconds "
            "before the test that showed it",
            "Each drop taken out cools the whole mixture to room temperature, "
            "so the reaction halts for a time",
            "The iodine slows the amylase down, so every single test adds "
            "time to the run that follows",
            "The iodine only shows starch after it has been in the mixture "
            "for a full 30 seconds",
        ],
        "correct_index": 0,
        "why": "Sampling at intervals can only detect the end point at the "
               "next test, so the recorded time is an overestimate.",
    },
    {
        "id": "ks4-enzymes-h19",
        "subtopic_slug": "enzymes",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student uses the same syringe for the starch and for the "
                "amylase without rinsing it. Suggest the effect on the "
                "recorded time.",
        "options": [
            "It is longer, because the starch left inside the syringe uses up "
            "part of the amylase for good",
            "It is shorter, because some digestion has already begun before "
            "the timing starts",
            "It is unchanged, because the volumes left inside a syringe are "
            "far too small to matter",
            "It is longer, because the amylase is diluted by the starch "
            "solution left in the syringe",
        ],
        "correct_index": 1,
        "why": "Enzyme carried over on the syringe starts digesting starch "
               "before timing begins, so the measured time is too short.",
    },
    {
        "id": "ks4-enzymes-h20",
        "subtopic_slug": "enzymes",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare the effect on amylase of lowering the temperature "
                "from 37 C to 15 C with the effect of lowering the pH from 7 "
                "to 2.",
        "options": [
            "Neither makes any difference, because amylase works at the same "
            "rate across all of these conditions",
            "Both slow it in the same way, and returning it to 37 C restores "
            "the rate in either case",
            "Cooling slows it and can be reversed; strong acid alters the "
            "active site and cannot be",
            "Cooling alters the active site for good; the acid only slows it "
            "until pH 7 returns",
        ],
        "correct_index": 2,
        "why": "Cold lowers collision frequency but leaves the enzyme intact; "
               "extreme pH denatures it permanently.",
    },
    {
        "id": "ks4-enzymes-h21",
        "subtopic_slug": "enzymes",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Starch was cleared in 120 seconds at pH 5, 60 seconds at pH "
                "6 and 40 seconds at pH 7. Deduce which is closest to the "
                "optimum pH and what further work would test it.",
        "options": [
            "pH 5, and test values below 5, because the longest time shows "
            "the enzyme working at its very hardest",
            "pH 6, and test nothing more, because the middle of three values "
            "is the optimum",
            "pH 7, and test values above 7 to see whether the time falls "
            "further or starts to rise",
            "pH 7, and repeat pH 7 alone, because the fastest result found is "
            "the optimum",
        ],
        "correct_index": 2,
        "why": "The shortest time is the fastest rate, so the optimum is at "
               "or beyond pH 7 and the range must be extended.",
    },
    {
        "id": "ks4-enzymes-h22",
        "subtopic_slug": "enzymes",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "In an investigation, lipase is added to a lipid and the pH "
                "of the mixture is recorded as the reaction runs. Suggest why "
                "the pH can be used to follow the rate.",
        "options": [
            "Glycerol is alkaline, so the pH climbs steadily as the lipid is "
            "digested",
            "The lipase itself is acidic, so the pH falls as more of it is "
            "used up",
            "Digestion gives off hydrogen gas, which turns the mixture more "
            "acidic",
            "Fatty acids are acidic, so the pH falls as more of them are "
            "released",
        ],
        "correct_index": 3,
        "why": "One product is an acid, so the pH of the mixture falls as the "
               "reaction proceeds and the fall tracks the rate.",
    },
    {
        "id": "ks4-enzymes-h23",
        "subtopic_slug": "enzymes",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student measures the rate at 20 C and at 40 C and "
                "concludes that 'the hotter it is, the faster an enzyme "
                "works'. Evaluate this conclusion.",
        "options": [
            "It cannot be judged at all: the rate of an enzyme reaction has "
            "nothing at all to do with temperature",
            "It goes beyond the evidence: only two points were tested, and "
            "above the optimum the rate falls",
            "It is quite wrong: those results actually show that an enzyme "
            "works faster when it is made colder",
            "It is fully supported: two results that show a rise are enough "
            "to state a general rule",
        ],
        "correct_index": 1,
        "why": "Two points below the optimum cannot support a general rule; "
               "past the optimum the enzyme denatures and the rate falls.",
    },
    {
        "id": "ks4-enzymes-h24",
        "subtopic_slug": "enzymes",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A fish's body temperature follows the temperature of the "
                "water it lives in. Suggest why it needs less food in winter "
                "than in summer.",
        "options": [
            "Its enzyme-controlled reactions run more slowly in the cold, so "
            "it uses energy more slowly",
            "Its enzymes are denatured by the cold water, so it is unable to "
            "digest any food at all in winter",
            "Cold water passes energy into the fish, so it has no need to "
            "release energy from food itself",
            "Its enzymes work faster in the cold, so it gets far more energy "
            "out of each mouthful of food",
        ],
        "correct_index": 0,
        "why": "Cold slows every enzyme-controlled reaction, so the fish's "
               "demand for energy from food falls.",
    },
    {
        "id": "ks4-enzymes-h25",
        "subtopic_slug": "enzymes",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Milk is cloudy because of the protein in it. Suggest how you "
                "could tell, without any chemical test, that a protease has "
                "digested that protein.",
        "options": [
            "The milk turns solid, because the amino acids released join up "
            "to form a firm curd",
            "The milk turns bright purple, which is the colour that protein "
            "digestion produces",
            "The milk turns clear, because the large protein molecules that "
            "scattered the light have gone",
            "The milk gives off a gas, because digesting protein releases "
            "carbon dioxide",
        ],
        "correct_index": 2,
        "why": "Digestion breaks the large protein molecules that scatter "
               "light into small soluble ones, so the milk clears.",
    },
    {
        "id": "ks4-enzymes-h26",
        "subtopic_slug": "enzymes",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "At the end of an experiment, iodine added to the mixture "
                "stayed orange-brown. A student concludes that the amylase "
                "must have been destroyed. Evaluate this conclusion.",
        "options": [
            "Right: an enzyme that had worked would have left the iodine "
            "blue-black at the very end",
            "Right: orange-brown shows the iodine could not reach the starch "
            "in the mixture",
            "Wrong: orange-brown shows the starch is still there, so nothing "
            "was digested",
            "Wrong: orange-brown means no starch is left, so the amylase had "
            "digested all of it",
        ],
        "correct_index": 3,
        "why": "Iodine goes blue-black only with starch, so an orange-brown "
               "result at the end shows the starch has been digested.",
    },
]
