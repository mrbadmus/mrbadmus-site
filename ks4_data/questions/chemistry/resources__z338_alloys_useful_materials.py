"""Chemistry · Using resources — the MRB-338 expansion for `alloys-useful-materials`.

The shipped rows name the compositions — bronze, brass, steel, stainless steel —
and do the carat arithmetic once, so the weight here falls on the explanation
those rows assume and never ask for: why a pure metal is soft, what
different-sized atoms do to the layers, and why the same change that makes steel
harder also makes it more brittle and less malleable.

Round that sits the alloy-design strand the spec asks for: low-carbon against
high-carbon steel, tungsten in high-speed steel, chromium content against
corrosion resistance, cupronickel in coinage, nitinol in a frame that springs
back, and gold alloyed for a ring but used pure in a connector. Five rows carry
percentage-composition arithmetic, in both directions between carats and mass.
"""

TOPIC = "resources"
SUBJECT = "chemistry"

QUESTIONS = [
    {
        "id": "ks4-alloys-useful-materials-e05",
        "subtopic_slug": "alloys-useful-materials",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "In a pure metal, why can layers of atoms slide over one another easily?",
        "options": [
            "The atoms are all the same size and sit in regular layers",
            "The atoms are held together by weak covalent bonds",
            "The atoms are arranged at random with large gaps left between them all",
            "The atoms carry no charge, so nothing holds them in place",
        ],
        "correct_index": 0,
        "why": "Identical atoms pack into even layers, and an even layer has "
               "nothing to stop it sliding when a force is applied.",
    },
    {
        "id": "ks4-alloys-useful-materials-e06",
        "subtopic_slug": "alloys-useful-materials",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "An alloy is often described as a mixture of metals. State "
                "whether an alloy may also contain a non-metal.",
        "options": [
            "Yes, because a metal can be mixed with a non-metal as well as "
            "with another metal",
            "No, because a non-metal would react with the metal rather than "
            "mixing evenly into it",
            "No, because only metal atoms are able to sit in the layers of "
            "the structure",
            "Yes, but only where the non-metal makes up more than half of "
            "the mixture",
        ],
        "correct_index": 0,
        "why": "Steel is iron mixed with a small amount of a non-metal, so an "
               "alloy does not have to be made of metals alone.",
    },
    {
        "id": "ks4-alloys-useful-materials-e07",
        "subtopic_slug": "alloys-useful-materials",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State why pure gold is unsuitable for a ring that is worn daily.",
        "options": [
            "It corrodes in air, so the surface of the ring loses its shine within a few weeks",
            "It has too high a melting point to be cast into a ring shape",
            "It is too soft, so it scratches and bends out of shape",
            "It is too brittle, so it snaps when the ring is pushed on",
        ],
        "correct_index": 2,
        "why": "The layers of atoms in pure gold slide readily, so the metal marks "
               "and distorts in ordinary wear.",
    },
    {
        "id": "ks4-alloys-useful-materials-e08",
        "subtopic_slug": "alloys-useful-materials",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Which element is added to iron to make the high-speed steel used in drill bits?",
        "options": [
            "Zinc",
            "Chromium",
            "Tin",
            "Tungsten",
        ],
        "correct_index": 3,
        "why": "Tungsten lets the steel keep its hardness when the cutting edge "
               "becomes hot, which ordinary high-carbon steel does not.",
    },
    {
        "id": "ks4-alloys-useful-materials-e09",
        "subtopic_slug": "alloys-useful-materials",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "A steel is described as low carbon. State the approximate "
                "carbon content this describes.",
        "options": [
            "Less than about 0.3%, with almost all of the rest being iron",
            "About 3%, so three parts in every hundred of the steel are carbon",
            "About 10%, which would make a tenth of the whole mass carbon",
            "About 30%, so nearly a third of the mass would be carbon",
        ],
        "correct_index": 0,
        "why": "A low carbon steel holds only a few tenths of one per cent of "
               "carbon; that small amount is enough to disrupt the layers and "
               "harden the iron.",
    },
    {
        "id": "ks4-alloys-useful-materials-e10",
        "subtopic_slug": "alloys-useful-materials",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Which two metals make up the cupronickel used for coins?",
        "options": [
            "Copper and tin, mixed in roughly equal proportions by mass",
            "Copper and nickel, which give a hard-wearing coin",
            "Copper and zinc, which give the coin a golden colour",
            "Iron and nickel, which make the coin magnetic in a slot",
        ],
        "correct_index": 1,
        "why": "Cupronickel is copper alloyed with nickel, chosen because it is "
               "durable and does not corrode in a pocket.",
    },
    {
        "id": "ks4-alloys-useful-materials-e11",
        "subtopic_slug": "alloys-useful-materials",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Besides chromium, which metal is added to iron to make stainless steel?",
        "options": [
            "Manganese",
            "Zinc",
            "Nickel",
            "Aluminium",
        ],
        "correct_index": 2,
        "why": "Stainless steel is typically about 18% chromium and 8% nickel, with "
               "the remainder iron.",
    },
    {
        "id": "ks4-alloys-useful-materials-e12",
        "subtopic_slug": "alloys-useful-materials",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Which alloy is traditionally used to cast church bells?",
        "options": [
            "Brass",
            "Stainless steel",
            "Cupronickel",
            "Bronze",
        ],
        "correct_index": 3,
        "why": "Bronze is harder than copper and rings clearly, which is why it has "
               "been used for bells and cymbals for centuries.",
    },
    {
        "id": "ks4-alloys-useful-materials-e13",
        "subtopic_slug": "alloys-useful-materials",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State why pure aluminium is unsuitable for the body of an aircraft.",
        "options": [
            "It is too weak to carry the loads an aircraft puts on it",
            "It is too dense, so the aircraft would be far too heavy",
            "It conducts heat too well, so the cabin could not be warmed",
            "It corrodes rapidly in air, so it would not last a season",
        ],
        "correct_index": 0,
        "why": "Pure aluminium has a usefully low density but not the strength an "
               "airframe needs, which is why it is alloyed.",
    },
    {
        "id": "ks4-alloys-useful-materials-e14",
        "subtopic_slug": "alloys-useful-materials",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Which kind of steel is used for the body panels of a car?",
        "options": [
            "High carbon steel, which is the hardest of the steels available",
            "Low carbon steel, which is tough and easily pressed into shape",
            "Stainless steel, which contains both chromium and nickel as well as the iron",
            "High-speed steel, which contains tungsten as well as carbon",
        ],
        "correct_index": 1,
        "why": "A panel must be pressed into a curve without cracking, so a tough "
               "ductile steel is wanted rather than a hard brittle one.",
    },
    {
        "id": "ks4-alloys-useful-materials-e15",
        "subtopic_slug": "alloys-useful-materials",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Name the alloy of nickel and titanium that returns to its original shape when warmed.",
        "options": [
            "Bronze",
            "Brass",
            "Nitinol",
            "Cupronickel",
        ],
        "correct_index": 2,
        "why": "Nitinol is a shape-memory alloy, used in spectacle frames and in "
               "stents that open once they are in place.",
    },
    {
        "id": "ks4-alloys-useful-materials-e16",
        "subtopic_slug": "alloys-useful-materials",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State one property of gold that makes it suitable for an electrical connector.",
        "options": [
            "It is the cheapest metal that conducts electricity",
            "It is magnetic, so the connector holds itself",
            "It is soft, so the connector bends into any shape",
            "It conducts well and does not corrode, so contact is reliable",
        ],
        "correct_index": 3,
        "why": "A corroded contact conducts badly, and gold's resistance to "
               "corrosion is what keeps the connection good over years.",
    },
    {
        "id": "ks4-alloys-useful-materials-e17",
        "subtopic_slug": "alloys-useful-materials",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Compared with pure iron, steel is described how?",
        "options": [
            "Harder and stronger than the pure metal",
            "Softer and weaker than the pure metal",
            "Lower in density than the pure metal",
            "A better conductor than the pure metal",
        ],
        "correct_index": 0,
        "why": "Adding carbon disrupts the layers of iron atoms, so they resist "
               "sliding and the metal resists being deformed.",
    },
    {
        "id": "ks4-alloys-useful-materials-e18",
        "subtopic_slug": "alloys-useful-materials",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "A bracelet is stamped 24 carat. State what this tells you about the gold.",
        "options": [
            "It is 24% gold, the rest being silver and copper mixed together",
            "It is pure gold, with no other metal mixed into it",
            "It weighs 24 grams, which is the standard mass for a bracelet",
            "It is 24 times harder than an ordinary gold alloy",
        ],
        "correct_index": 1,
        "why": "The carat scale runs to 24, so 24 carat means 24 parts in 24, which "
               "is gold and nothing else.",
    },
    {
        "id": "ks4-alloys-useful-materials-s05",
        "subtopic_slug": "alloys-useful-materials",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Rose gold and white gold hold the same proportion of gold as "
                "each other. Explain why they differ in colour.",
        "options": [
            "Different metals are mixed with the gold, and copper gives the reddish tint",
            "The gold atoms themselves change colour once another metal is mixed among them",
            "The two alloys are cast at different temperatures, and the casting sets the colour",
            "A dye is added while the finished piece is polished, and the two dyes differ",
        ],
        "correct_index": 0,
        "why": "The colour of a gold alloy comes from the metals mixed with "
               "the gold: copper gives a reddish tone, while silver or "
               "palladium gives a paler one.",
    },
    {
        "id": "ks4-alloys-useful-materials-s06",
        "subtopic_slug": "alloys-useful-materials",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why steel is less malleable than pure iron.",
        "options": [
            "Steel contains carbon, and carbon is a non-metal that simply cannot be hammered into shape",
            "Steel is denser, so a hammer blow is spread over a much larger mass of metal",
            "Steel has a higher melting point, so it has to be hot before it can be shaped",
            "The carbon atoms stop the layers sliding, and malleability depends on sliding",
        ],
        "correct_index": 3,
        "why": "Malleability is the ability of layers to slide into a new shape, so "
               "whatever makes an alloy harder also makes it less malleable.",
    },
    {
        "id": "ks4-alloys-useful-materials-s07",
        "subtopic_slug": "alloys-useful-materials",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "An 18 carat gold ring has a mass of 8.0 g. Calculate the mass of gold in it.",
        "options": [
            "1.8 g, reading the carat figure as a proportion of the ring's mass",
            "2.0 g, which is the mass of the other metals rather than of the gold",
            "6.0 g, since 18 carat is 75% gold and 75% of 8.0 g is 6.0 g",
            "8.0 g, since the whole ring is described as being gold",
        ],
        "correct_index": 2,
        "why": "18 carat is 18 parts in 24, or 75%, and 0.75 multiplied by 8.0 g "
               "gives 6.0 g.",
    },
    {
        "id": "ks4-alloys-useful-materials-s08",
        "subtopic_slug": "alloys-useful-materials",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why raising the carbon content of a steel makes it more brittle.",
        "options": [
            "More carbon locks the layers so firmly that the metal cracks instead of bending",
            "More carbon lowers the melting point, and a low melting point causes cracking",
            "More carbon makes the steel lighter, and light metals break more readily",
            "More carbon turns the steel into a compound, and compounds are brittle",
        ],
        "correct_index": 0,
        "why": "Hardness and brittleness go together: a lattice that cannot deform "
               "at all has no way to absorb a blow except by fracturing.",
    },
    {
        "id": "ks4-alloys-useful-materials-s09",
        "subtopic_slug": "alloys-useful-materials",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Suggest two reasons brass is chosen for a trumpet.",
        "options": [
            "It is magnetic and it is cheap, so the instrument can be held firmly on a metal stand",
            "It is soft and it is dense, so the instrument absorbs unwanted vibration",
            "It is harder than copper and it has good acoustic properties",
            "It is brittle and light, so the instrument is easy to carry",
        ],
        "correct_index": 2,
        "why": "The tubing has to hold its shape in use and it has to ring well, and "
               "brass does both better than pure copper.",
    },
    {
        "id": "ks4-alloys-useful-materials-s10",
        "subtopic_slug": "alloys-useful-materials",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why a bearing is made from bronze rather than from pure copper.",
        "options": [
            "Bronze conducts heat better, so the bearing runs cooler in use",
            "Bronze is less dense, so the moving part is easier to turn",
            "Bronze melts at a lower temperature, so the bearing is easier to cast",
            "Bronze is harder than copper, so the bearing surface wears away far more slowly",
        ],
        "correct_index": 3,
        "why": "A bearing is rubbed constantly, so resistance to wear is the "
               "property that matters, and the alloy is the harder metal.",
    },
    {
        "id": "ks4-alloys-useful-materials-s11",
        "subtopic_slug": "alloys-useful-materials",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "A brass fitting is 65% copper and 35% zinc by mass. Calculate the mass of zinc in a 200 g fitting.",
        "options": [
            "70 g, which is 35% of the 200 g total mass",
            "35 g, reading the percentage figure directly as a mass in grams",
            "130 g, which is the mass of the copper rather than of the zinc",
            "571 g, dividing the mass by the percentage",
        ],
        "correct_index": 0,
        "why": "35% of 200 g is 0.35 multiplied by 200, which is 70 g.",
    },
    {
        "id": "ks4-alloys-useful-materials-s12",
        "subtopic_slug": "alloys-useful-materials",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why a higher-carat gold ring costs more but wears out sooner.",
        "options": [
            "More gold is present, and gold is both the costlier metal and the softer one",
            "More gold is present, and gold reacts with the skin to form a tarnish that rubs off in wear",
            "Less gold is present, so the ring is cheaper to make and harder in use",
            "More gold is present, and a heavier ring is knocked against things more often",
        ],
        "correct_index": 0,
        "why": "Raising the carat raises both the gold content and the softness, so "
               "price and wear move in opposite directions.",
    },
    {
        "id": "ks4-alloys-useful-materials-s13",
        "subtopic_slug": "alloys-useful-materials",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Suggest why an alloy softens over a range of temperatures rather than melting sharply at one.",
        "options": [
            "The alloy is a mixture, and a mixture has no single fixed melting point",
            "The alloy contains a non-metal, and non-metals do not have melting points",
            "The alloy is heated unevenly, so different parts of it reach the same point rather later",
            "The alloy contains trapped air, which has to escape before melting starts",
        ],
        "correct_index": 0,
        "why": "A fixed sharp melting point belongs to a pure substance; the varied "
               "composition of a mixture spreads the change over a range.",
    },
    {
        "id": "ks4-alloys-useful-materials-s14",
        "subtopic_slug": "alloys-useful-materials",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "State the effect of increasing the chromium content of a stainless steel.",
        "options": [
            "It becomes a better conductor of electricity than ordinary steel is",
            "It becomes less dense, which makes it useful in aircraft construction",
            "It resists attack by its surroundings better than a lower-chromium steel",
            "It becomes softer, so it can be pressed into much thinner sheets for making cutlery",
        ],
        "correct_index": 2,
        "why": "Chromium is the element that gives stainless steel its resistance, so "
               "more of it gives a steel that survives harsher surroundings.",
    },
    {
        "id": "ks4-alloys-useful-materials-s15",
        "subtopic_slug": "alloys-useful-materials",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Suggest why a chisel blade and a car door panel are pressed from different steels.",
        "options": [
            "The chisel must be shaped when cold and the panel must be shaped when hot",
            "The chisel needs hardness to hold an edge, the panel needs to bend without cracking",
            "The chisel needs to be light in the hand, while the panel needs to be heavy on the car body itself",
            "The chisel is used indoors and the panel outdoors, so each needs a different metal",
        ],
        "correct_index": 1,
        "why": "The two jobs want opposite ends of the same trade-off, which is why "
               "the carbon content is chosen differently for each.",
    },
    {
        "id": "ks4-alloys-useful-materials-s16",
        "subtopic_slug": "alloys-useful-materials",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why an aluminium alloy is used for a bicycle frame.",
        "options": [
            "It is strong enough for the loads and still low in density",
            "It is the cheapest metal available for making a frame from",
            "It conducts heat well, so the frame does not overheat in the sun",
            "It is magnetic, so accessories can be clipped onto the frame",
        ],
        "correct_index": 0,
        "why": "A rider wants a frame that is light to pedal and stiff enough not to "
               "flex, and alloying supplies the strength pure aluminium lacks.",
    },
    {
        "id": "ks4-alloys-useful-materials-s17",
        "subtopic_slug": "alloys-useful-materials",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "A 9 carat gold chain has a mass of 12 g. Calculate the mass of gold in it.",
        "options": [
            "9.0 g, reading the carat figure directly as a mass in grams",
            "4.5 g, since 9 carat is 37.5% gold and 37.5% of 12 g is 4.5 g",
            "7.5 g, which is the mass of the other metals in the chain",
            "32 g, dividing the mass of the chain by the percentage of gold",
        ],
        "correct_index": 1,
        "why": "9 carat is 9 parts in 24, which is 37.5%, and 0.375 multiplied by "
               "12 g is 4.5 g.",
    },
    {
        "id": "ks4-alloys-useful-materials-s18",
        "subtopic_slug": "alloys-useful-materials",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why household wiring is drawn from pure copper rather than from a copper alloy.",
        "options": [
            "A pure metal is cheaper to produce than any alloy made from it would be",
            "An alloy cannot be drawn into a wire, because alloys are brittle materials",
            "An alloy would corrode inside the wall, whereas pure copper would not",
            "The disrupted lattice of an alloy conducts electricity less well than the pure metal",
        ],
        "correct_index": 3,
        "why": "The same irregularity that stops layers sliding also scatters the "
               "delocalised electrons, so an alloy is the poorer conductor.",
    },
    {
        "id": "ks4-alloys-useful-materials-h05",
        "subtopic_slug": "alloys-useful-materials",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain, in terms of the arrangement of atoms, why an alloy resists being bent out of shape.",
        "options": [
            "Atoms of different sizes break up the even layers, so the layers cannot slip past each other",
            "Atoms of different sizes attract one another more strongly than identical atoms do",
            "Atoms of different sizes pack more closely, so there is no room left for movement",
            "Atoms of different sizes share electrons in pairs, which fixes them in position",
        ],
        "correct_index": 0,
        "why": "Deformation of a metal is layers of atoms slipping, and an uneven "
               "lattice offers obstacles at every layer.",
    },
    {
        "id": "ks4-alloys-useful-materials-h06",
        "subtopic_slug": "alloys-useful-materials",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Determine which of 18 carat and 9 carat gold is the harder, and explain your reasoning.",
        "options": [
            "18 carat, because a higher carat number means a harder and more valuable metal",
            "9 carat, because it holds more of the other metals that disrupt the lattice",
            "Neither, because hardness depends on how the ring was cast and not on its carat",
            "18 carat, because the gold atoms themselves are the hardest atoms present",
        ],
        "correct_index": 1,
        "why": "9 carat is only 37.5% gold, so more of the lattice is made of "
               "differently sized atoms and the layers slide less readily.",
    },
    {
        "id": "ks4-alloys-useful-materials-h07",
        "subtopic_slug": "alloys-useful-materials",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A ring of total mass 6.0 g contains 4.5 g of gold. Determine its carat value.",
        "options": [
            "9 carat, since 4.5 g is the mass of gold in a 9 carat item",
            "12 carat, since 4.5 g is close to three quarters of 6.0 g",
            "18 carat, since 4.5 divided by 6.0 is 75%, which is 18 parts in 24",
            "24 carat, since the whole of the mass given is accounted for as being gold",
        ],
        "correct_index": 2,
        "why": "The gold is 4.5/6.0 = 0.75 of the mass, and 75% of 24 carats is "
               "18 carat.",
    },
    {
        "id": "ks4-alloys-useful-materials-h08",
        "subtopic_slug": "alloys-useful-materials",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Evaluate a proposal to make a water tap from pure copper instead of brass.",
        "options": [
            "A good proposal, because pure copper conducts heat better and warms the water faster",
            "A good proposal, because pure copper is harder than brass and so lasts longer in use",
            "A poor proposal, because pure copper cannot be machined into a threaded fitting",
            "A poor proposal: pure copper is softer, so the threads and handle would wear",
        ],
        "correct_index": 3,
        "why": "A tap is turned and tightened repeatedly, so it needs the harder "
               "alloy; the pure metal would deform at the threads.",
    },
    {
        "id": "ks4-alloys-useful-materials-h09",
        "subtopic_slug": "alloys-useful-materials",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A railway rail must resist wear from wheels but must not shatter under a heavy impact. Determine the steel to use, and justify it.",
        "options": [
            "Pure iron, because a soft metal absorbs an impact without any risk of shattering",
            "A medium-carbon steel, because it is hard enough to resist wear yet not brittle",
            "The highest-carbon steel available, because wear resistance is the one thing that counts here",
            "Stainless steel, because chromium and nickel make a steel stronger than carbon can",
        ],
        "correct_index": 1,
        "why": "Carbon content trades hardness against brittleness, and a rail needs "
               "a working compromise rather than either extreme.",
    },
    {
        "id": "ks4-alloys-useful-materials-h10",
        "subtopic_slug": "alloys-useful-materials",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Evaluate the claim that adding more of the second element to an alloy makes it a better material.",
        "options": [
            "The claim holds, because every property of an alloy improves as its composition changes",
            "The claim holds, because more of the second element means fewer identical layers to slip",
            "The claim is weak: more carbon hardens a steel but also makes it more brittle",
            "The claim is weak, because an alloy's proportions are fixed and cannot change",
        ],
        "correct_index": 2,
        "why": "Composition is a trade-off, and the right amount depends on which "
               "property the job actually needs.",
    },
    {
        "id": "ks4-alloys-useful-materials-h11",
        "subtopic_slug": "alloys-useful-materials",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A cupronickel coin of mass 6.0 g is 75% copper and 25% nickel by mass. Calculate the mass of nickel.",
        "options": [
            "4.5 g, taking the 75% of copper instead",
            "1.5 g, since 25% of 6.0 g is 1.5 g",
            "0.25 g, reading the 25% directly as a mass",
            "24 g, dividing 6.0 g by the 25%",
        ],
        "correct_index": 1,
        "why": "25% of 6.0 g is 0.25 multiplied by 6.0, which is 1.5 g.",
    },
    {
        "id": "ks4-alloys-useful-materials-h12",
        "subtopic_slug": "alloys-useful-materials",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "An alloy has its two metals spread evenly throughout. Explain why it is still classed as a mixture.",
        "options": [
            "Because the two metals are present in the same proportions everywhere in the sample",
            "Because the metals can be separated again by melting the alloy down once more",
            "Because a mixture is any material containing more than one kind of atom in it",
            "Because the metals are not chemically bonded and their proportions can be varied",
        ],
        "correct_index": 3,
        "why": "Being evenly spread is not the test; what makes a compound is a "
               "chemical bond in a fixed ratio, and an alloy has neither.",
    },
    {
        "id": "ks4-alloys-useful-materials-h13",
        "subtopic_slug": "alloys-useful-materials",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Determine why a drill running hot enough to glow needs high-speed steel rather than high carbon steel.",
        "options": [
            "High-speed steel keeps its hardness when hot, whereas high carbon steel softens",
            "High-speed steel conducts heat away faster, so the cutting edge stays cool",
            "High-speed steel contains no carbon of any kind, so there is nothing in it that can soften",
            "High-speed steel is more brittle, and a brittle edge cuts metal more cleanly",
        ],
        "correct_index": 0,
        "why": "Tungsten lets the steel hold its hardness at working temperature, "
               "which is exactly where high carbon steel loses its edge.",
    },
    {
        "id": "ks4-alloys-useful-materials-h14",
        "subtopic_slug": "alloys-useful-materials",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Evaluate the claim that the harder an alloy is, the better it will be for making a hand tool.",
        "options": [
            "The claim holds, because a hand tool is chosen on hardness and on nothing else",
            "The claim is weak: a very hard alloy is brittle and a tool may need to survive a blow",
            "The claim holds, because hardness and toughness are simply two names for one and the same property",
            "The claim is weak, because hardness cannot be measured for an alloy in any way",
        ],
        "correct_index": 1,
        "why": "A cold chisel struck with a hammer has to be hard at the edge but "
               "must not shatter, so hardness alone is not the whole answer.",
    },
    {
        "id": "ks4-alloys-useful-materials-h15",
        "subtopic_slug": "alloys-useful-materials",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A bronze bell of mass 500 g contains 12% tin by mass. Calculate the mass of copper in it.",
        "options": [
            "60 g, taking the tin instead of the copper",
            "440 g, since 88% of 500 g is 440 g",
            "488 g, subtracting the 12 from the 500 g",
            "4167 g, dividing 500 g by the 12%",
        ],
        "correct_index": 1,
        "why": "If 12% is tin then 88% is copper, and 0.88 multiplied by 500 g is "
               "440 g.",
    },
    {
        "id": "ks4-alloys-useful-materials-h16",
        "subtopic_slug": "alloys-useful-materials",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Suggest why gold is alloyed for a ring but used almost pure in an electrical contact.",
        "options": [
            "A ring must resist wear, while a contact needs the pure metal's conductivity",
            "A ring must conduct electricity, while a contact must resist being scratched",
            "A ring is worn in air and a contact is sealed away, so neither needs alloying",
            "A ring is made in a factory and a contact by hand, which fixes the purity",
        ],
        "correct_index": 0,
        "why": "The two jobs want different properties: hardness for the ring, and "
               "the undisrupted lattice of the pure metal for the contact.",
    },
    {
        "id": "ks4-alloys-useful-materials-h17",
        "subtopic_slug": "alloys-useful-materials",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A spectacle frame made of nitinol is bent out of shape and springs back when it is warmed in the hand. Determine which property is being used.",
        "options": [
            "Its shape memory, which returns the alloy to the form it was set in",
            "Its low density, which lets the frame move freely under its own weight",
            "Its high melting point, which stops the frame deforming when it is warmed",
            "Its good conductivity, which spreads the warmth evenly along the frame",
        ],
        "correct_index": 0,
        "why": "Nitinol is a shape-memory alloy: warming it restores the shape it "
               "was originally set into, which is why it suits frames and stents.",
    },
    {
        "id": "ks4-alloys-useful-materials-h18",
        "subtopic_slug": "alloys-useful-materials",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "An engineer proposes replacing an aircraft wing's aluminium alloy with pure aluminium of twice the thickness. Evaluate the proposal.",
        "options": [
            "A good proposal, because doubling the thickness doubles the strength and saves the alloying cost",
            "A good proposal, because pure aluminium resists corrosion better than any alloy of it",
            "A poor proposal, because pure aluminium melts at too low a temperature for a wing",
            "A poor proposal: the wing would be far heavier and still softer than the alloy",
        ],
        "correct_index": 3,
        "why": "Doubling thickness doubles the mass, which an aircraft cannot "
               "afford, and the metal still deforms more readily than the alloy.",
    },
]
