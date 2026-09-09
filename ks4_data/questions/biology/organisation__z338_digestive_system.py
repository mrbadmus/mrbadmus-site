"""Biology · Organisation — the MRB-338 expansion of `digestive-system`.

One leaf only: AQA 8461 §4.2.2, the digestive system as an ORGAN SYSTEM. The
original twelve rows in `organisation.py` take the products of lipase, the
Biuret test, the oesophagus, the gall bladder as a store, the two jobs of
stomach acid, mechanical against chemical digestion, why starch cannot be
absorbed, a missing gall bladder, missing pancreatic lipase, the villus wall
and blood supply, why bile's alkalinity matters, and fast transit through the
large intestine. This file takes what they leave: the definition of digestion
itself, gastric juice, the salivary glands, the rectum, peristalsis, villi,
the route a meal takes organ by organ, the iodine and ethanol tests and the
water bath, egestion against excretion, emulsification as a PHYSICAL change,
bile's release site, the small intestine's length and its flattened lining,
water absorption in the large intestine, the composition of faeces, and the
misconception set — bile as an enzyme, bile digesting fat, the stomach as the
site of absorption, and the large intestine as a site of digestion.

The weight follows the CONTENT. `easier` stays at eight because recall in this
leaf is a short list of organs and two colour changes, and asking it a ninth
way is the same question wearing new words. The demand lives in tracing one
food group through the whole gut, in reasoning from a broken organ back to a
symptom, and in separating the three things bile is confused with, so
`standard` and `harder` carry twenty-two each.

The numbers here are the ones the anatomy actually supplies: the surface-area
gain when one fat droplet becomes a thousand, and the multiplication the
intestinal lining performs on a smooth tube of the same length. Enzyme theory
— the active site, denaturing, and the temperature and pH curves — belongs to
`enzymes`, and the cell-tissue-organ ladder belongs to
`principles-of-organisation`; an enzyme is named here only where the anatomy
requires it.
"""

TOPIC = "organisation"
SUBJECT = "biology"

QUESTIONS = [
    # ══ easier · e05–e12 ═════════════════════════════════════════════════
    # Digestion itself, gastric juice, the salivary glands, the rectum, the
    # iodine colour change, peristalsis, villi, and the emulsion result.
    {
        "id": "ks4-digestive-system-e05",
        "subtopic_slug": "digestive-system",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Describe what digestion does to the molecules in food.",
        "options": [
            "Breaking large, insoluble food molecules into small, soluble ones",
            "Moving the small, soluble food molecules out of the gut and into the bloodstream",
            "Passing large, insoluble molecules straight out of the body as faeces",
            "Releasing the energy held in small food molecules inside the cells",
        ],
        "correct_index": 0,
        "why": "Digestion is the breakdown of the large insoluble molecules in "
               "food into small soluble ones; moving those products into the "
               "blood is absorption, which is a separate step.",
    },
    {
        "id": "ks4-digestive-system-e06",
        "subtopic_slug": "digestive-system",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the fluid produced by the stomach lining that contains "
                "hydrochloric acid and pepsin.",
        "options": [
            "Chyme, the liquid the stomach passes on to the next organ",
            "Gastric juice, made by glands in the stomach lining",
            "Bile, which arrives in the stomach from the gall bladder",
            "Saliva, which is swallowed along with the food itself",
        ],
        "correct_index": 1,
        "why": "Glandular tissue in the stomach wall makes gastric juice, "
               "which contains hydrochloric acid and the protease pepsin; "
               "chyme is the mixture of food and gastric juice that results.",
    },
    {
        "id": "ks4-digestive-system-e07",
        "subtopic_slug": "digestive-system",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the glands that release amylase into the mouth.",
        "options": [
            "The gastric glands, in the lining of the stomach wall",
            "The glands of the gall bladder, tucked under the liver",
            "The salivary glands, which open into the mouth",
            "The glands of the pancreas, which drains into the mouth along a short duct",
        ],
        "correct_index": 2,
        "why": "The salivary glands release saliva into the mouth, and saliva "
               "contains amylase, which starts the digestion of starch.",
    },
    {
        "id": "ks4-digestive-system-e08",
        "subtopic_slug": "digestive-system",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the part of the digestive system that stores faeces "
                "before they leave the body.",
        "options": [
            "The gall bladder, which collects the waste left after digestion",
            "The pancreas, which lies behind the stomach itself",
            "The stomach, the muscular bag below the ribs",
            "The rectum, at the end of the large intestine",
        ],
        "correct_index": 3,
        "why": "Faeces are stored in the rectum and then expelled through the "
               "anus.",
    },
    {
        "id": "ks4-digestive-system-e09",
        "subtopic_slug": "digestive-system",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the colour change seen in the food test for starch "
                "when the result is positive.",
        "options": [
            "Orange-brown to blue-black",
            "Blue to cloudy white",
            "Blue to brick red",
            "Blue to purple",
        ],
        "correct_index": 0,
        "why": "Iodine solution is orange-brown and turns blue-black when "
               "starch is present.",
    },
    {
        "id": "ks4-digestive-system-e10",
        "subtopic_slug": "digestive-system",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the soft ball of food that the tongue shapes before it "
                "is swallowed.",
        "options": [
            "The mucus",
            "The bolus",
            "The pepsin",
            "The chyme",
        ],
        "correct_index": 1,
        "why": "The tongue shapes chewed food into a bolus, which is then "
               "swallowed into the oesophagus.",
    },
    {
        "id": "ks4-digestive-system-e11",
        "subtopic_slug": "digestive-system",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the finger-like folds that line the wall of the small "
                "intestine.",
        "options": [
            "Capillaries",
            "Alveoli",
            "Villi",
            "Cilia",
        ],
        "correct_index": 2,
        "why": "Villi are the finger-like folds of the small intestine "
               "lining; they give it a very large surface area.",
    },
    {
        "id": "ks4-digestive-system-e12",
        "subtopic_slug": "digestive-system",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "A food sample is shaken with ethanol and the mixture is then "
                "poured into water, where a cloudy white layer forms. State "
                "what this shows.",
        "options": [
            "The food contains starch",
            "The food contains protein",
            "The food contains sugar",
            "The food contains lipid",
        ],
        "correct_index": 3,
        "why": "A cloudy white emulsion in the ethanol test is a positive "
               "result for lipid.",
    },

    # ══ standard · s05–s26 ═══════════════════════════════════════════════
    # Applying the food tests, tracing one food group through the gut,
    # separating digestion from absorption and egestion, and the four things
    # bile is confused with.
    {
        "id": "ks4-digestive-system-s05",
        "subtopic_slug": "digestive-system",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student heats a food sample with Benedict's solution in a "
                "water bath and it turns brick red. Determine what the food "
                "contains.",
        "options": [
            "Sugar, because Benedict's solution changes colour when sugar is present",
            "Starch, because Benedict's solution goes red when any starch is heated in it",
            "Protein, because heating protein with Benedict's solution turns it red",
            "Lipid, because Benedict's solution reacts with any fat in the sample",
        ],
        "correct_index": 0,
        "why": "Benedict's solution is the test for sugars, and a brick-red "
               "precipitate is the positive result.",
    },
    {
        "id": "ks4-digestive-system-s06",
        "subtopic_slug": "digestive-system",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a Benedict's test is heated in a water bath "
                "rather than directly in a Bunsen flame.",
        "options": [
            "A water bath can heat the sample far above 100 degrees C, which a flame cannot",
            "A water bath heats the tube evenly and gently, so its contents do not spit out",
            "A water bath adds the extra water that the Benedict's reaction itself needs",
            "A water bath keeps the sample cold, so that the colour change is not spoiled",
        ],
        "correct_index": 1,
        "why": "A water bath gives gentle, even heating below 100 degrees C, "
               "so the tube's contents are not driven out by sudden boiling.",
    },
    {
        "id": "ks4-digestive-system-s07",
        "subtopic_slug": "digestive-system",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "The stomach churns food for several hours. Explain how this "
                "churning helps the chemical digestion of a meal.",
        "options": [
            "It warms the food to exactly body temperature, which is when digestion begins",
            "It breaks the chemical bonds in the food, so far fewer enzymes are needed",
            "It breaks the food into smaller pieces, giving enzymes a larger surface area",
            "It mixes acid right through every part of the food, so that no enzymes are needed there",
        ],
        "correct_index": 2,
        "why": "Churning is mechanical digestion: it makes the pieces smaller, "
               "which increases the surface area the enzymes can act on.",
    },
    {
        "id": "ks4-digestive-system-s08",
        "subtopic_slug": "digestive-system",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a food molecule that is small but does not "
                "dissolve in water cannot be absorbed into the blood.",
        "options": [
            "It is far too heavy to be pushed through the thin wall of the small intestine",
            "It would be broken apart by the bile long before it could ever reach the blood",
            "It has already been fully digested, so the body now has no further use for it",
            "It cannot dissolve in the blood plasma, so the blood could not carry it away",
        ],
        "correct_index": 3,
        "why": "Absorbed molecules have to dissolve in the plasma to be "
               "transported, so being small is not enough on its own — they "
               "must be soluble too.",
    },
    {
        "id": "ks4-digestive-system-s09",
        "subtopic_slug": "digestive-system",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Describe the difference between digestion and absorption.",
        "options": [
            "Digestion breaks molecules apart; absorption moves the products into the blood",
            "Digestion moves molecules into the blood; absorption breaks them up",
            "Digestion happens in the blood; absorption happens in the gut",
            "Digestion and absorption both break molecules apart in different organs",
        ],
        "correct_index": 0,
        "why": "Digestion is the chemical breakdown of large molecules; "
               "absorption is the passage of the small products through the "
               "gut wall into the blood.",
    },
    {
        "id": "ks4-digestive-system-s10",
        "subtopic_slug": "digestive-system",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why passing out faeces is called egestion and not "
                "excretion.",
        "options": [
            "Faeces leave the body through the anus, and excretion can only happen through the skin",
            "Faeces are mostly material that was never absorbed into the body at all",
            "Faeces are made only from substances that the body's own cells have produced",
            "Faeces contain a lot of water, and any waste containing water is egested",
        ],
        "correct_index": 1,
        "why": "Egestion removes material that never entered the body's cells; "
               "excretion removes the waste products the cells have made.",
    },
    {
        "id": "ks4-digestive-system-s11",
        "subtopic_slug": "digestive-system",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why emulsifying fat is described as a physical change "
                "rather than as digestion.",
        "options": [
            "The fat is warmed by the bile, and warming a substance is a physical change",
            "The fat dissolves completely in the bile, so no new substance at all is left behind",
            "The fat is only broken into smaller droplets; its molecules are unchanged",
            "The fat is broken into fatty acids, and a change of state is always physical",
        ],
        "correct_index": 2,
        "why": "Emulsification splits large droplets into small ones but "
               "breaks no chemical bonds, so the fat molecules themselves are "
               "exactly as they were.",
    },
    {
        "id": "ks4-digestive-system-s12",
        "subtopic_slug": "digestive-system",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Describe the two jobs that bile does when it reaches the "
                "small intestine.",
        "options": [
            "It kills the bacteria in the food and breaks fat into small droplets",
            "It digests fat and protein at the same time and in the same place",
            "It makes the intestine acidic and breaks starch down into sugars",
            "It neutralises stomach acid and breaks fat into small droplets",
        ],
        "correct_index": 3,
        "why": "Bile is alkaline, so it neutralises the acid arriving from the "
               "stomach, and it emulsifies fat into small droplets.",
    },
    {
        "id": "ks4-digestive-system-s13",
        "subtopic_slug": "digestive-system",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain how breaking one large fat droplet into many small "
                "droplets speeds up the digestion of that fat.",
        "options": [
            "The total surface area of the fat is much greater, so lipase acts faster",
            "The smaller droplets have already been digested, so less work is left to do",
            "The smaller droplets dissolve in water, so no lipase is needed on them",
            "The total mass of the fat is much smaller, so there is less of it to digest",
        ],
        "correct_index": 0,
        "why": "Many small droplets have a far greater total surface area than "
               "one large one, so lipase has more fat exposed to work on.",
    },
    {
        "id": "ks4-digestive-system-s14",
        "subtopic_slug": "digestive-system",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "State where bile is released into the gut, and suggest why "
                "it is not released into the stomach instead.",
        "options": [
            "Into the oesophagus, so that food is coated in bile before it is swallowed",
            "Into the small intestine; releasing it into the stomach would cancel the acid",
            "Into the stomach, where the acid already there gives bile exactly the conditions it needs",
            "Into the large intestine, which is where the last of the fat is broken down",
        ],
        "correct_index": 1,
        "why": "Bile is released into the small intestine. It is alkaline, so "
               "in the stomach it would neutralise the acid the stomach needs.",
    },
    {
        "id": "ks4-digestive-system-s15",
        "subtopic_slug": "digestive-system",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student says that most food is absorbed into the blood "
                "while it is still in the stomach. Explain why this is wrong.",
        "options": [
            "The stomach has no blood supply at all, so anything absorbed there could not be carried away",
            "Food in the stomach is still solid, so none of it can be absorbed anywhere",
            "The stomach wall is thick and has no villi, so very little can pass through it",
            "The stomach absorbs only water, which it then passes to the large intestine",
        ],
        "correct_index": 2,
        "why": "Almost all absorption happens in the small intestine, whose "
               "villi give a huge surface area and a wall one cell thick; the "
               "stomach has neither.",
    },
    {
        "id": "ks4-digestive-system-s16",
        "subtopic_slug": "digestive-system",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain how the folding of the small intestine lining into "
                "millions of tiny projections helps it do its job.",
        "options": [
            "They give it a much greater volume, so a great deal more food is stored in the gut",
            "They release the enzymes that finish the digestion of every food group",
            "They slow the food down, giving the stomach's acid much longer to work",
            "They give it a very large surface area, so absorption happens much faster",
        ],
        "correct_index": 3,
        "why": "Villi and the microvilli on them multiply the surface area of "
               "the lining, so digested food is absorbed far more quickly.",
    },
    {
        "id": "ks4-digestive-system-s17",
        "subtopic_slug": "digestive-system",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest why absorption would be slower if the lining of the "
                "small intestine were several cells thick.",
        "options": [
            "Digested molecules would have a longer distance to diffuse into the blood",
            "Digested molecules would be too large to fit between all the extra cells",
            "The extra cells would use up all the glucose before it reached the blood",
            "The extra cells would make the intestine much shorter, so there is less surface area",
        ],
        "correct_index": 0,
        "why": "A villus wall one cell thick keeps the diffusion distance very "
               "short; a thicker wall means a longer journey and slower "
               "absorption.",
    },
    {
        "id": "ks4-digestive-system-s18",
        "subtopic_slug": "digestive-system",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Describe what happens to a protein molecule between being "
                "eaten and reaching the blood.",
        "options": [
            "It is absorbed whole in the stomach, and is then broken up once it is in the blood",
            "It is digested in the stomach and small intestine, then absorbed as amino acids",
            "It is digested in the mouth by amylase, and then absorbed through the large intestine wall",
            "It is emulsified by bile in the small intestine, then absorbed unchanged",
        ],
        "correct_index": 1,
        "why": "Protease in the stomach and then from the pancreas breaks "
               "protein into amino acids, which are small and soluble enough "
               "to be absorbed in the small intestine.",
    },
    {
        "id": "ks4-digestive-system-s19",
        "subtopic_slug": "digestive-system",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Saliva contains mucus as well as amylase. Explain how the "
                "mucus helps.",
        "options": [
            "It digests the starch that the amylase has not managed to reach",
            "It neutralises any acid that has risen up out of the stomach",
            "It lubricates the food so that the bolus is easy to swallow",
            "It kills the bacteria in food before they can reach the stomach",
        ],
        "correct_index": 2,
        "why": "Mucus lubricates the food, so the bolus the tongue forms slips "
               "easily down the oesophagus.",
    },
    {
        "id": "ks4-digestive-system-s20",
        "subtopic_slug": "digestive-system",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why the material entering the large intestine "
                "contains almost no glucose or amino acids.",
        "options": [
            "They were destroyed by the acid while still inside the stomach",
            "They are absorbed by the large intestine as soon as they arrive in it",
            "They were never made, because glucose and amino acids are absorbed whole",
            "They were absorbed into the blood as the material passed along the small intestine",
        ],
        "correct_index": 3,
        "why": "The small intestine absorbs the products of digestion, so very "
               "little of them is left in the material that passes on.",
    },
    {
        "id": "ks4-digestive-system-s21",
        "subtopic_slug": "digestive-system",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Faeces are brown. State what gives them this colour.",
        "options": [
            "Pigments from the bile that was released into the small intestine",
            "Iron released from red blood cells that were broken down in the gut",
            "The undigested starch that the amylase failed to break down at all",
            "The dead bacteria that the acid in the stomach killed inside the food",
        ],
        "correct_index": 0,
        "why": "Faeces are undigested fibre, dead cells and bacteria, coloured "
               "brown by the pigments in bile.",
    },
    {
        "id": "ks4-digestive-system-s22",
        "subtopic_slug": "digestive-system",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A food is tested for protein and for sugar. The Biuret "
                "reagent stays blue, and the Benedict's solution stays blue "
                "after heating. Determine what these results show.",
        "options": [
            "The food contains both protein and sugar",
            "The food contains sugar but no protein at all",
            "The food contains protein but no sugar at all",
            "The food contains neither protein nor sugar",
        ],
        "correct_index": 3,
        "why": "Both tests are negative, so neither protein nor sugar is "
               "present in the sample.",
    },
    {
        "id": "ks4-digestive-system-s23",
        "subtopic_slug": "digestive-system",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "The stomach releases chyme into the small intestine a little "
                "at a time over several hours. Suggest one advantage of this.",
        "options": [
            "The small intestine is kept quite empty, so no food is ever wasted in the faeces",
            "The chyme is diluted on the way, which is what the intestine needs",
            "The small intestine has time to digest and absorb each small amount fully",
            "The chyme is made more acidic on the way, which the small intestine needs",
        ],
        "correct_index": 2,
        "why": "Releasing chyme slowly means the small intestine is never "
               "overloaded, so each portion can be digested and absorbed "
               "completely.",
    },
    {
        "id": "ks4-digestive-system-s24",
        "subtopic_slug": "digestive-system",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain how a person lying flat on their back is still able "
                "to move food from the mouth to the stomach.",
        "options": [
            "The food is pulled downwards by the suction that the stomach makes as it churns",
            "The saliva makes the food slippery enough to slide all of the way on its own",
            "The food is pushed downwards by the next mouthful arriving right behind it",
            "Waves of muscle contraction squeeze the food along, so gravity is not needed",
        ],
        "correct_index": 3,
        "why": "Peristalsis pushes the bolus along by muscular contraction, so "
               "food travels whatever position the body is in.",
    },
    {
        "id": "ks4-digestive-system-s25",
        "subtopic_slug": "digestive-system",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Describe the route a meal takes through the digestive "
                "system, naming the organs in the correct order.",
        "options": [
            "Mouth, oesophagus, stomach, small intestine, large intestine, rectum, anus",
            "Mouth, oesophagus, stomach, large intestine, small intestine, rectum, anus",
            "Mouth, stomach, oesophagus, small intestine, large intestine, rectum, anus",
            "Mouth, oesophagus, stomach, small intestine, pancreas, large intestine, anus",
        ],
        "correct_index": 0,
        "why": "Food is swallowed into the oesophagus, churned in the stomach, "
               "digested and absorbed in the small intestine, then loses water "
               "in the large intestine before being stored and egested.",
    },
    {
        "id": "ks4-digestive-system-s26",
        "subtopic_slug": "digestive-system",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest why a person whose small intestine has been "
                "shortened by surgery may lose weight even though they still "
                "eat normally.",
        "options": [
            "There is less room for food, so they cannot swallow as much at each meal",
            "There is less surface area, so less of the digested food is absorbed",
            "Their stomach acid becomes diluted, so no protein can be digested any more",
            "Their large intestine takes over, and it absorbs water rather than food",
        ],
        "correct_index": 1,
        "why": "A shorter small intestine has less lining, so less of the "
               "digested food is absorbed before the material passes on.",
    },

    # ══ harder · h05–h26 ═════════════════════════════════════════════════
    # Reasoning from a broken organ back to a symptom, two clean surface-area
    # calculations, and the evaluations: bile, the stomach, the food tests
    # and what a digestive system is actually for.
    {
        "id": "ks4-digestive-system-h05",
        "subtopic_slug": "digestive-system",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare the roles of the liver and the pancreas in the "
                "digestion of a fatty meal.",
        "options": [
            "The liver makes the lipase; the pancreas makes the bile that stores it",
            "Both organs make lipase, but only the liver ever releases it into the intestine",
            "The liver makes bile, which emulsifies the fat; the pancreas makes lipase",
            "The liver digests the fat directly; the pancreas neutralises the acid",
        ],
        "correct_index": 2,
        "why": "The liver's contribution is bile, which emulsifies fat "
               "physically; the pancreas supplies the lipase that chemically "
               "digests it.",
    },
    {
        "id": "ks4-digestive-system-h06",
        "subtopic_slug": "digestive-system",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Evaluate the statement: 'Bile digests fat.'",
        "options": [
            "It is right: bile is the enzyme that breaks fat down in the small intestine",
            "It is right: bile and lipase are two names for the same liver secretion",
            "It is wrong: bile has no effect at all on fat, and only lipase ever comes near to it",
            "It is wrong: bile only breaks fat into smaller droplets, and lipase digests it",
        ],
        "correct_index": 3,
        "why": "Bile is not an enzyme and breaks no bonds; it emulsifies fat "
               "so that lipase, which is the enzyme, can digest it faster.",
    },
    {
        "id": "ks4-digestive-system-h07",
        "subtopic_slug": "digestive-system",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why the small intestine is called the main site of "
                "digestion, even though digestion begins in the mouth.",
        "options": [
            "Enzymes for all three food groups act there, and bile arrives to help them",
            "It is the widest organ in the gut, so more food can be worked on there at one time",
            "It is the only organ in which any chemical digestion happens at all",
            "The mouth only warms the food up, and chemical digestion cannot begin there",
        ],
        "correct_index": 0,
        "why": "The small intestine receives amylase, protease and lipase from "
               "the pancreas as well as bile from the liver, so all three food "
               "groups are digested there.",
    },
    {
        "id": "ks4-digestive-system-h08",
        "subtopic_slug": "digestive-system",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A patient's bile duct is blocked, so no bile reaches the "
                "small intestine, although their pancreas is healthy. Explain "
                "why the digestion of fat is still much slower than normal.",
        "options": [
            "The pancreas stops making lipase when no bile arrives there to trigger its release",
            "The fat stays in large droplets, so lipase has far less surface area to work on",
            "The fat cannot be broken into smaller molecules at all, because only bile breaks those bonds",
            "The fat passes straight on into the large intestine, where no enzyme can reach it",
        ],
        "correct_index": 1,
        "why": "Without bile the fat is never emulsified, so its surface area "
               "stays small and the lipase the pancreas still supplies has far "
               "less fat exposed to act on.",
    },
    {
        "id": "ks4-digestive-system-h09",
        "subtopic_slug": "digestive-system",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A cube of fat with sides of 1.0 mm is emulsified into 1000 "
                "identical smaller cubes, each with sides of 0.1 mm. "
                "Calculate the total surface area of the 1000 smaller cubes.",
        "options": [
            "600 mm2",
            "6 mm2",
            "60 mm2",
            "0.06 mm2",
        ],
        "correct_index": 2,
        "why": "One small cube has a surface area of 6 x 0.1 x 0.1 = 0.06 mm2, "
               "and 1000 of them give 60 mm2 — ten times the 6 mm2 of the "
               "original cube.",
    },
    {
        "id": "ks4-digestive-system-h10",
        "subtopic_slug": "digestive-system",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "The small intestine is about 5 m long and the large "
                "intestine about 1.5 m. Explain why the small intestine needs "
                "to be the longer of the two.",
        "options": [
            "It has to hold a whole meal at once, which the large intestine never does",
            "It must be long enough to reach every organ that sends enzymes into it",
            "The food moves much faster through it, so a great deal more length is needed there",
            "Digestion and absorption both happen there, and both need time and surface",
        ],
        "correct_index": 3,
        "why": "The small intestine is the site of both digestion and "
               "absorption, so it needs a long path to give contact time and a "
               "very large surface area.",
    },
    {
        "id": "ks4-digestive-system-h11",
        "subtopic_slug": "digestive-system",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare the mechanical digestion that happens in the mouth "
                "with the mechanical digestion that happens in the stomach.",
        "options": [
            "Teeth grind the food into pieces; muscular churning mixes it into a liquid",
            "Teeth grind the food into pieces; the stomach then breaks the bonds in them",
            "Amylase softens the food; the stomach's muscles then dissolve it completely",
            "Both of them use enzymes, and the stomach's enzymes work far faster than saliva's",
        ],
        "correct_index": 0,
        "why": "Both are physical: the teeth cut and grind, while the stomach's "
               "muscular wall churns the food into the liquid called chyme.",
    },
    {
        "id": "ks4-digestive-system-h12",
        "subtopic_slug": "digestive-system",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Evaluate the claim that the stomach is the most important "
                "organ of the digestive system.",
        "options": [
            "It is: nearly all digestion and absorption happen in the stomach",
            "It is not: the small intestine digests all three food groups and absorbs them",
            "It is: the stomach is the only organ that digests anything",
            "It is not: the stomach plays no part in digesting our food",
        ],
        "correct_index": 1,
        "why": "The stomach digests protein and kills bacteria, but the small "
               "intestine finishes all three food groups and does virtually "
               "all the absorbing.",
    },
    {
        "id": "ks4-digestive-system-h13",
        "subtopic_slug": "digestive-system",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A tinned food carries a small number of bacteria. Suggest "
                "why a healthy person may eat it without becoming ill, while "
                "a person taking strong acid-reducing medicine may not.",
        "options": [
            "Stomach acid normally digests the bacteria into amino acids, and the medicine stops that",
            "The medicine makes the stomach alkaline, and bacteria can only grow in alkali",
            "Stomach acid normally kills most bacteria, and the medicine removes that defence",
            "The medicine speeds the gut up, so bacteria reach the blood before being killed",
        ],
        "correct_index": 2,
        "why": "Hydrochloric acid in gastric juice kills most of the bacteria "
               "swallowed with food, so reducing that acid leaves more of them "
               "alive.",
    },
    {
        "id": "ks4-digestive-system-h14",
        "subtopic_slug": "digestive-system",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A patient has fat in their faeces. A student concludes that "
                "the patient's pancreas must have stopped working. Evaluate "
                "this conclusion.",
        "options": [
            "It must be right, because the pancreas is the only organ that can act on fat",
            "It must be wrong, because fat in the faeces is perfectly normal after every meal",
            "It must be wrong, because the pancreas has nothing to do with fat at all",
            "It may be right, but a blocked bile duct would give exactly the same result",
        ],
        "correct_index": 3,
        "why": "Undigested fat points to a failure of either the lipase from "
               "the pancreas or the bile from the liver, so one result cannot "
               "settle which.",
    },
    {
        "id": "ks4-digestive-system-h15",
        "subtopic_slug": "digestive-system",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student chews a piece of bread for two minutes. The chewed "
                "bread is found to contain less starch and more sugar than an "
                "unchewed piece. Explain these results.",
        "options": [
            "Amylase in the saliva has broken some of the starch down into sugar",
            "Chewing has itself broken the chemical bonds in the starch, making sugar",
            "The bread's own sugar has been squeezed out of the starch by the teeth",
            "Acid from the mouth has dissolved the starch and left the sugar behind",
        ],
        "correct_index": 0,
        "why": "The salivary glands release amylase into the mouth, so starch "
               "digestion into sugar begins there, before the food is even "
               "swallowed.",
    },
    {
        "id": "ks4-digestive-system-h16",
        "subtopic_slug": "digestive-system",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why the large intestine is not described as a site "
                "of digestion, even though material stays inside it for a "
                "long time.",
        "options": [
            "The material inside it is already liquid, and only solid food can be digested",
            "No digestive enzymes are ever released into it, so nothing there is digested",
            "It lies furthest from the liver, so it is much too cool for any digestion",
            "Digestion stops the moment that food has passed through the pyloric sphincter",
        ],
        "correct_index": 1,
        "why": "No organ secretes digestive enzymes into the large intestine; "
               "its job is to absorb water from the undigested material that "
               "reaches it.",
    },
    {
        "id": "ks4-digestive-system-h17",
        "subtopic_slug": "digestive-system",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare what the small intestine absorbs with what the large "
                "intestine absorbs.",
        "options": [
            "The small intestine absorbs all of the water and the large intestine absorbs the food",
            "Both absorb digested food, and neither of them absorbs any water",
            "The small intestine absorbs digested food; the large intestine absorbs water",
            "Both absorb only water, and digested food is absorbed through the stomach",
        ],
        "correct_index": 2,
        "why": "Glucose, amino acids, fatty acids and glycerol are absorbed in "
               "the small intestine; the large intestine absorbs water from "
               "what is left.",
    },
    {
        "id": "ks4-digestive-system-h18",
        "subtopic_slug": "digestive-system",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a person who ate only foods made of small, "
                "soluble molecules would still produce faeces.",
        "options": [
            "Small soluble molecules cannot be absorbed, so all of them pass straight through",
            "The large intestine turns any of the food that it absorbs back into a solid waste again",
            "The water absorbed in the large intestine has to leave the body as faeces",
            "Faeces also contain dead cells, bacteria and bile pigments from the body itself",
        ],
        "correct_index": 3,
        "why": "Faeces are not only undigested food: they also contain dead "
               "cells shed from the gut lining, bacteria and the pigments left "
               "over from bile.",
    },
    {
        "id": "ks4-digestive-system-h19",
        "subtopic_slug": "digestive-system",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student tests a food with Benedict's solution and with "
                "Biuret reagent, and both tests are positive. The student "
                "concludes that the food contains sugar and protein only. "
                "Evaluate this conclusion.",
        "options": [
            "Unsound: starch and lipid were never tested for, so they cannot be ruled out",
            "Sound: two positive results are enough to identify everything in a food",
            "Unsound: a positive Benedict's result rules protein out of that sample entirely",
            "Sound: a food that contains sugar and protein cannot contain anything else",
        ],
        "correct_index": 0,
        "why": "A test can only report on what it detects; without an iodine "
               "test and an emulsion test, starch and lipid remain untested "
               "rather than absent.",
    },
    {
        "id": "ks4-digestive-system-h20",
        "subtopic_slug": "digestive-system",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "The lining of the small intestine has a surface area 600 "
                "times greater than a smooth tube of the same length would "
                "have. A smooth tube of that length would have a surface area "
                "of 0.50 m2. Calculate the surface area of the lining.",
        "options": [
            "1200 m2",
            "300 m2",
            "30 m2",
            "0.00083 m2",
        ],
        "correct_index": 1,
        "why": "0.50 x 600 = 300 m2 — the folding of the lining into villi and "
               "microvilli is what buys that six-hundred-fold gain.",
    },
    {
        "id": "ks4-digestive-system-h21",
        "subtopic_slug": "digestive-system",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Evaluate whether chewing a meal thoroughly makes any "
                "difference to how much of it is digested.",
        "options": [
            "It does not: enzymes break bonds, so piece size changes nothing",
            "It does: chewing breaks the bonds that enzymes cannot reach",
            "It does: smaller pieces give the enzymes more surface area in the time available",
            "It does not: all food is fully digested however long it is chewed for",
        ],
        "correct_index": 2,
        "why": "Chewing is mechanical digestion, and the surface area it "
               "creates lets the enzymes get through more of the meal in the "
               "hours it spends in the gut.",
    },
    {
        "id": "ks4-digestive-system-h22",
        "subtopic_slug": "digestive-system",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A long-term gut disease flattens the lining of a patient's "
                "small intestine, although their enzymes work normally. "
                "Explain why they still become short of nutrients.",
        "options": [
            "A flattened lining releases no enzymes at all, so none of the food is ever digested there",
            "The food passes on into the large intestine, which cannot digest any of it either",
            "The flattened lining pushes the food past too quickly for it to be absorbed",
            "The surface area for absorption is much smaller, so less food reaches the blood",
        ],
        "correct_index": 3,
        "why": "Digestion is unaffected, but flattened villi mean far less "
               "surface area, so the products of digestion are absorbed much "
               "more slowly.",
    },
    {
        "id": "ks4-digestive-system-h23",
        "subtopic_slug": "digestive-system",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare where amylase is produced in the human body with "
                "where lipase is produced.",
        "options": [
            "Amylase comes from the salivary glands and the pancreas; lipase from the pancreas",
            "Amylase comes from the pancreas alone; lipase from the salivary glands",
            "Amylase comes from the stomach and the liver; lipase from the small intestine",
            "Both of them are made in the liver and stored in the gall bladder until needed",
        ],
        "correct_index": 0,
        "why": "Amylase is made in the salivary glands and in the pancreas; "
               "lipase is made in the pancreas, and neither is made in the "
               "liver.",
    },
    {
        "id": "ks4-digestive-system-h24",
        "subtopic_slug": "digestive-system",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a glucose drink raises the blood glucose "
                "concentration faster than a slice of bread does.",
        "options": [
            "Glucose is a liquid, and every liquid of any kind is absorbed straight through the stomach wall",
            "Glucose is already small and soluble, so it is absorbed without being digested",
            "Bread has to be chewed first, and that chewing takes far longer than a drink does",
            "Bread contains no glucose at all, so none of it can ever reach the blood",
        ],
        "correct_index": 1,
        "why": "Glucose needs no digestion and can be absorbed as soon as it "
               "reaches the small intestine, while the starch in bread must "
               "first be broken down.",
    },
    {
        "id": "ks4-digestive-system-h25",
        "subtopic_slug": "digestive-system",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why emulsified fat droplets still cannot be absorbed "
                "into the blood.",
        "options": [
            "They are still coated in a layer of bile, and bile cannot pass through the gut wall",
            "They are still fat molecules, which are large and do not dissolve in water",
            "They are still inside the stomach, which has no villi at all with which to absorb",
            "They are still acidic from the stomach, and acid cannot cross the gut wall",
        ],
        "correct_index": 1,
        "why": "Emulsification changes the size of the droplets, not the "
               "molecules, so the fat must still be digested before it is "
               "small and soluble enough to be absorbed.",
    },
    {
        "id": "ks4-digestive-system-h26",
        "subtopic_slug": "digestive-system",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Evaluate the statement: 'The job of the digestive system is "
                "to break food down.'",
        "options": [
            "Complete: once the food has been broken down, the system's work is finished",
            "Wrong: breaking food down is done by the blood, not by the digestive system",
            "Incomplete: it must also absorb the products and egest what is left over",
            "Incomplete: it must also make the enzymes that respire the food in the cells",
        ],
        "correct_index": 2,
        "why": "Breaking food down achieves nothing on its own; the system "
               "must also absorb the small soluble products into the blood and "
               "egest the material that is left.",
    },
]
