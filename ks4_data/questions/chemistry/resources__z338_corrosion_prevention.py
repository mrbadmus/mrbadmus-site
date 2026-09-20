"""Chemistry · Using resources — the MRB-338 expansion for `corrosion-prevention`.

The shipped rows own the two rusting requirements, the three-nail experiment,
the tin can and the zinc-against-copper scratch, so the weight here falls on the
rest of 4.10.3.1: corrosion as a general idea rather than rusting alone, why the
aluminium oxide layer behaves differently from flaking rust, and the conditions
that make rusting faster — dissolved salt as an electrolyte, acid, road salt in
winter.

The prevention methods are taken one at a time and then set against each other
on the grounds the spec names: cost, where the metal sits, appearance and how
much maintenance each needs. Two rows carry arithmetic, on the consumption of a
sacrificial anode and on the mass an iron sample gains as it rusts. Everything
here is at Foundation depth: no half equations.
"""

TOPIC = "resources"
SUBJECT = "chemistry"

QUESTIONS = [
    {
        "id": "ks4-corrosion-prevention-e05",
        "subtopic_slug": "corrosion-prevention",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State what is meant by corrosion.",
        "options": [
            "The destruction of a metal by reaction with substances around it",
            "The melting of a metal when it is heated above its melting point",
            "The wearing away of a metal by rubbing against another surface",
            "The change in shape of a metal when a large force is applied",
        ],
        "correct_index": 0,
        "why": "Corrosion is a chemical process: the metal reacts with its "
               "surroundings and is converted into a compound.",
    },
    {
        "id": "ks4-corrosion-prevention-e06",
        "subtopic_slug": "corrosion-prevention",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Rusting is an example of which type of reaction?",
        "options": [
            "Neutralisation, because an acid is used up as the iron reacts away",
            "Oxidation, because the iron gains oxygen as it reacts",
            "Thermal decomposition, because the iron breaks down when warmed",
            "Displacement, because the oxygen replaces the iron",
        ],
        "correct_index": 1,
        "why": "The iron combines with oxygen to form an oxide, which is oxidation.",
    },
    {
        "id": "ks4-corrosion-prevention-e07",
        "subtopic_slug": "corrosion-prevention",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Which metal is used to galvanise steel?",
        "options": [
            "Tin",
            "Zinc",
            "Copper",
            "Chromium",
        ],
        "correct_index": 1,
        "why": "Galvanising means coating with zinc, which is more reactive than "
               "iron and so protects it sacrificially as well as as a barrier.",
    },
    {
        "id": "ks4-corrosion-prevention-e08",
        "subtopic_slug": "corrosion-prevention",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Name the process used to coat a steel tap with a thin layer of chromium.",
        "options": [
            "Galvanising, in which the steel is dipped right into a bath of the molten metal",
            "Smelting, in which the steel and the chromium are melted together",
            "Electroplating, in which the coating is deposited by electrolysis",
            "Distillation, in which the chromium is condensed onto the surface",
        ],
        "correct_index": 2,
        "why": "In electroplating the object is made the negative electrode and the "
               "metal ions in the solution are deposited onto it.",
    },
    {
        "id": "ks4-corrosion-prevention-e09",
        "subtopic_slug": "corrosion-prevention",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Which of these is used to protect the moving chain of a bicycle from corrosion?",
        "options": [
            "A thick coat of gloss paint over the whole chain",
            "A block of magnesium bolted beside the chain",
            "A layer of oil or grease worked into the links",
            "A sheet of zinc wrapped tightly round the chain",
        ],
        "correct_index": 2,
        "why": "Oil and grease keep water and oxygen off a surface that has to keep "
               "moving, which a rigid paint film could not do.",
    },
    {
        "id": "ks4-corrosion-prevention-e10",
        "subtopic_slug": "corrosion-prevention",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Iron will not rust if it is kept in dry air. State why.",
        "options": [
            "Dry air contains no oxygen, and oxygen is the gas that attacks iron",
            "Dry air is too cold, and rusting happens just in warm conditions",
            "Dry air is at a lower pressure, so the oxygen cannot reach the iron",
            "Water is needed as well as oxygen, and dry air supplies no water",
        ],
        "correct_index": 3,
        "why": "Both oxygen and water have to be present, so removing either one "
               "stops the reaction.",
    },
    {
        "id": "ks4-corrosion-prevention-e11",
        "subtopic_slug": "corrosion-prevention",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Which of these makes iron rust faster?",
        "options": [
            "Dissolved salt in the water touching the iron",
            "A coating of clean dry grease on the iron",
            "Storing the iron in a sealed jar of dry air",
            "Bolting a block of magnesium to the iron",
        ],
        "correct_index": 0,
        "why": "Dissolved salt makes the water a better conductor, which speeds up "
               "the electrochemical process of rusting.",
    },
    {
        "id": "ks4-corrosion-prevention-e12",
        "subtopic_slug": "corrosion-prevention",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Give the two ways in which any method of preventing corrosion can work.",
        "options": [
            "By painting the metal, or by keeping the metal somewhere warm and dry",
            "By making the metal harder, or by polishing its surface until it shines",
            "By cooling the metal below freezing, or by coating it with a second metal",
            "By forming a barrier, or by using a more reactive metal sacrificially",
        ],
        "correct_index": 3,
        "why": "Every method either keeps oxygen and water away from the metal or "
               "offers a more reactive metal to corrode in its place.",
    },
    {
        "id": "ks4-corrosion-prevention-e13",
        "subtopic_slug": "corrosion-prevention",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Which metal is plated onto the steel of a food can?",
        "options": [
            "Zinc",
            "Tin",
            "Magnesium",
            "Aluminium",
        ],
        "correct_index": 1,
        "why": "Tin is unreactive enough not to corrode into the food and is "
               "non-toxic, so it makes a safe barrier layer inside a can.",
    },
    {
        "id": "ks4-corrosion-prevention-e14",
        "subtopic_slug": "corrosion-prevention",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State what is attached to a steel ship's hull to give sacrificial protection.",
        "options": [
            "Blocks of a more reactive metal, such as zinc or magnesium",
            "Sheets of a less reactive metal, such as copper or silver",
            "Strips of a plastic that swells when it is wet through",
            "Rods of carbon, which conduct the corrosion harmlessly away",
        ],
        "correct_index": 0,
        "why": "The more reactive metal corrodes in preference to the iron, so the "
               "hull is protected for as long as the blocks last.",
    },
    {
        "id": "ks4-corrosion-prevention-e15",
        "subtopic_slug": "corrosion-prevention",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Name the compound that forms the protective layer on the surface of aluminium.",
        "options": [
            "Aluminium chloride",
            "Aluminium oxide",
            "Aluminium sulfate",
            "Aluminium carbonate",
        ],
        "correct_index": 1,
        "why": "Aluminium reacts with oxygen in the air to give a thin dense layer "
               "of aluminium oxide that seals the metal beneath it.",
    },
    {
        "id": "ks4-corrosion-prevention-e16",
        "subtopic_slug": "corrosion-prevention",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State one reason a chromium-plated finish is chosen for a bathroom tap.",
        "options": [
            "The plating adds weight, which stops the tap working loose over time",
            "It makes the tap conduct heat, so the water warms more quickly",
            "It gives a bright shiny surface that also resists corrosion",
            "It makes the tap softer, so the shape can be adjusted on site",
        ],
        "correct_index": 2,
        "why": "Chromium plating is chosen for appearance as well as protection, "
               "which is one of the grounds on which a method is picked.",
    },
    {
        "id": "ks4-corrosion-prevention-e17",
        "subtopic_slug": "corrosion-prevention",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "A painted steel gate develops a chip in the paint. State what happens at the chip.",
        "options": [
            "The paint spreads back over the chip and seals it again",
            "The steel there is exposed to air and water, and begins to rust",
            "The steel there becomes harder, because it has been work-hardened",
            "Nothing happens, because paint protects steel sacrificially",
        ],
        "correct_index": 1,
        "why": "Paint is a barrier and nothing more, so a break in it lets oxygen "
               "and water reach the metal.",
    },
    {
        "id": "ks4-corrosion-prevention-e18",
        "subtopic_slug": "corrosion-prevention",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Copper on an old roof turns green over many years. State what this shows.",
        "options": [
            "That copper is corroding, because it is reacting with its surroundings",
            "That copper is melting slowly, because a roof is warmed by the sun all day long in summer",
            "That copper is rusting, because rust can be green as well as orange",
            "That copper is dissolving, because rainwater is a solvent for metals",
        ],
        "correct_index": 0,
        "why": "Corrosion covers any metal attacked by its environment; only iron "
               "and steel corrode by rusting.",
    },
    {
        "id": "ks4-corrosion-prevention-s05",
        "subtopic_slug": "corrosion-prevention",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why a break in a zinc coating does not stop the zinc protecting the steel.",
        "options": [
            "The zinc flows slowly across the break and closes the gap over a few days",
            "Zinc is more reactive than iron, so it still corrodes in the steel's place",
            "Zinc is less reactive than iron, so the steel is left completely untouched",
            "The break fills with zinc oxide, which is a hard and impermeable barrier",
        ],
        "correct_index": 1,
        "why": "Sacrificial protection depends on reactivity and electrical contact, "
               "not on the coating being unbroken.",
    },
    {
        "id": "ks4-corrosion-prevention-s06",
        "subtopic_slug": "corrosion-prevention",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why galvanising is described as giving two kinds of protection.",
        "options": [
            "It protects against water and separately against oxygen, which are two quite different attackers of steel",
            "It coats the steel twice over, once on the outside and once on the inside surface",
            "It gives a barrier and it hardens the steel underneath, so the steel resists damage",
            "It keeps air and water off the steel, and the zinc also corrodes in the steel's place",
        ],
        "correct_index": 3,
        "why": "An unbroken zinc layer is a barrier, and once it is scratched the "
               "zinc's greater reactivity takes over.",
    },
    {
        "id": "ks4-corrosion-prevention-s07",
        "subtopic_slug": "corrosion-prevention",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why rust does not protect the iron beneath it the way an oxide layer protects aluminium.",
        "options": [
            "Rust is a different colour, so it absorbs more heat and drives the reaction on much faster",
            "Rust contains water, and water is one of the two substances needed for rusting",
            "Rust is flaky and porous, so it falls away and exposes fresh metal underneath",
            "Rust is a better conductor than aluminium oxide, so the reaction keeps going",
        ],
        "correct_index": 2,
        "why": "The aluminium oxide layer is thin, dense and impermeable, whereas "
               "rust crumbles off and leaves new iron open to attack.",
    },
    {
        "id": "ks4-corrosion-prevention-s08",
        "subtopic_slug": "corrosion-prevention",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why cars rust more quickly in places where salt is spread on winter roads.",
        "options": [
            "Salt reacts directly with the iron in the bodywork to form a soluble salt of iron that washes off",
            "Salt raises the freezing point of the water, so ice stays on the bodywork longer",
            "Salt makes the water on the car a better conductor, which speeds the corrosion up",
            "Salt scratches the paintwork as the wheels throw it up against the bodywork",
        ],
        "correct_index": 2,
        "why": "Rusting is an electrochemical process, and a salt solution carries "
               "charge far better than pure water does.",
    },
    {
        "id": "ks4-corrosion-prevention-s09",
        "subtopic_slug": "corrosion-prevention",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Suggest why painting is chosen for a garden bench but sacrificial blocks are chosen for an oil platform.",
        "options": [
            "Paint is cheap and enough in air, whereas a structure standing in the sea needs more",
            "Paint cannot be applied to any structure larger than a few metres across, however it is sprayed on",
            "Sacrificial blocks work in air but come loose as soon as they are submerged in water",
            "Sacrificial blocks are cheaper than paint, so they are used wherever cost matters",
        ],
        "correct_index": 0,
        "why": "The choice turns on cost and on where the metal sits: sea water is "
               "an electrolyte, so a barrier alone is not reliable enough.",
    },
    {
        "id": "ks4-corrosion-prevention-s10",
        "subtopic_slug": "corrosion-prevention",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Describe how the mass of a piece of iron changes as it rusts, and explain why.",
        "options": [
            "It falls, because the iron is worn away and carried off by the water",
            "It stays the same, because rusting just changes the colour of the surface",
            "It falls, because oxygen is released from the iron as the rust forms",
            "It rises, because oxygen and water are added to the iron to form rust",
        ],
        "correct_index": 3,
        "why": "Rust is hydrated iron(III) oxide, so the atoms of oxygen and water "
               "taken in add to the mass of the sample.",
    },
    {
        "id": "ks4-corrosion-prevention-s11",
        "subtopic_slug": "corrosion-prevention",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "A steel bucket is galvanised and an identical one is painted. Predict which lasts longer outdoors, and why.",
        "options": [
            "The painted bucket, because a film of paint is very much thicker than any coating of zinc metal",
            "The galvanised bucket, because the zinc goes on protecting once it is scratched",
            "The painted bucket, because paint can be renewed but zinc cannot be renewed",
            "Both last the same time, because each of them keeps air and water off the steel surface",
        ],
        "correct_index": 1,
        "why": "Paint fails at the first chip, whereas a scratched zinc layer still "
               "corrodes in preference to the iron.",
    },
    {
        "id": "ks4-corrosion-prevention-s12",
        "subtopic_slug": "corrosion-prevention",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why aluminium is used for window frames even though it is more reactive than iron.",
        "options": [
            "Aluminium does not react with oxygen in the air, so no protection of any sort is needed for it",
            "Aluminium is a poorer conductor of electricity, so it cannot corrode in the rain",
            "Its oxide layer is dense and impermeable, so it seals the metal beneath",
            "Aluminium is painted at the factory, and the paint is what protects it",
        ],
        "correct_index": 2,
        "why": "Reactivity tells you the metal reacts readily; what matters here is "
               "that the product of that reaction stops any further attack.",
    },
    {
        "id": "ks4-corrosion-prevention-s13",
        "subtopic_slug": "corrosion-prevention",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Zinc anodes on a hull lose 12 kg a year. Calculate how long a 60 kg set of anodes lasts.",
        "options": [
            "5 years, since 60 kg divided by 12 kg a year is 5",
            "48 years, found by subtracting 12 kg from the 60 kg fitted",
            "0.2 years, dividing the annual loss by the mass fitted",
            "720 years, multiplying the mass fitted by the annual loss",
        ],
        "correct_index": 0,
        "why": "60 divided by 12 is 5, so the anodes need replacing after about "
               "five years.",
    },
    {
        "id": "ks4-corrosion-prevention-s14",
        "subtopic_slug": "corrosion-prevention",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why a nail in salty water rusts faster than an identical nail in distilled water.",
        "options": [
            "The dissolved ions let charge move more easily, which speeds the reaction up",
            "Salty water holds much more dissolved oxygen than distilled water can hold",
            "Salt particles scratch away the surface of the nail and expose fresh iron to further attack",
            "Salty water has a higher boiling point, so it stays liquid against the nail",
        ],
        "correct_index": 0,
        "why": "The salt solution is an electrolyte, and rusting proceeds by charge "
               "moving between different parts of the metal surface.",
    },
    {
        "id": "ks4-corrosion-prevention-s15",
        "subtopic_slug": "corrosion-prevention",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Describe how weathering steel protects itself on a modern bridge.",
        "options": [
            "It is coated at the works with a thick zinc layer that will last for the whole life of the bridge",
            "It contains no iron whatever, so there is nothing in the steel that is able to rust",
            "It forms a tight rust layer on the surface that keeps further air and water out",
            "It is warmed electrically in wet weather so that the surface stays dry",
        ],
        "correct_index": 2,
        "why": "Weathering steel is designed so that its first layer of corrosion "
               "adheres and seals, instead of flaking away like ordinary rust.",
    },
    {
        "id": "ks4-corrosion-prevention-s16",
        "subtopic_slug": "corrosion-prevention",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why a sacrificial block must be in electrical contact with the steel it protects.",
        "options": [
            "The block has to touch the steel so that the two metals can be welded together",
            "The two metals must be in contact so that the block can act as a barrier layer",
            "The block has to touch the steel so that the steel is held still in the water",
            "Charge must be able to pass between them, or the block cannot corrode instead",
        ],
        "correct_index": 3,
        "why": "Sacrificial protection works by electrons passing from the more "
               "reactive metal to the iron, which needs a conducting path.",
    },
    {
        "id": "ks4-corrosion-prevention-s17",
        "subtopic_slug": "corrosion-prevention",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why acidic rainwater makes a steel structure corrode more quickly.",
        "options": [
            "The acid raises the pH at the surface, and a high pH is what attacks iron",
            "The acid coats the steel in a film of salt, which holds water against it",
            "The acid removes the oxygen from the water, and iron corrodes fastest without oxygen",
            "The lower pH speeds up the reaction between the iron and its surroundings",
        ],
        "correct_index": 3,
        "why": "Acidic conditions increase the rate at which the iron is attacked, "
               "which is why industrial and coastal air is so hard on steelwork.",
    },
    {
        "id": "ks4-corrosion-prevention-s18",
        "subtopic_slug": "corrosion-prevention",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "In an experiment on rusting, four nails are left in water at four temperatures. State the variable that must be kept the same.",
        "options": [
            "The temperature of the water in each of the four separate tubes",
            "The number of days each nail is left standing in the water",
            "The mass of rust that has formed on each nail at the end",
            "The colour of the tube in which each of the nails is placed",
        ],
        "correct_index": 1,
        "why": "Temperature is the independent variable and the rust formed is the "
               "dependent one, so the time allowed must be controlled.",
    },
    {
        "id": "ks4-corrosion-prevention-h05",
        "subtopic_slug": "corrosion-prevention",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A steel pipe is wrapped in plastic and buried, and the wrapping is torn during backfilling. Evaluate how well the pipe is protected.",
        "options": [
            "Well protected, because plastic protects steel sacrificially at every point where they touch",
            "Well protected, because soil holds neither the water nor the oxygen needed",
            "Poorly protected: the plastic is a barrier only, so the tear exposes bare steel",
            "Poorly protected, because plastic reacts with iron to produce more rust",
        ],
        "correct_index": 2,
        "why": "A barrier method fails at any break, which is why buried pipelines "
               "also carry sacrificial magnesium blocks.",
    },
    {
        "id": "ks4-corrosion-prevention-h06",
        "subtopic_slug": "corrosion-prevention",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A designer wants a protection method for a steel handrail that will be touched daily and seen by the public. Determine the best choice and justify it.",
        "options": [
            "Magnesium blocks, because they give the strongest protection of any method known",
            "Nothing, because a handrail is touched too often for rust to settle on it",
            "A thick layer of grease, because grease keeps both air and water off the steel",
            "Chromium electroplating, because it resists corrosion and looks good in use",
        ],
        "correct_index": 3,
        "why": "The rail has to be both protected and presentable, and appearance is "
               "one of the grounds on which a method is chosen.",
    },
    {
        "id": "ks4-corrosion-prevention-h07",
        "subtopic_slug": "corrosion-prevention",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why iron corrodes all the way through a bar while aluminium corrodes only at its surface.",
        "options": [
            "Aluminium is less reactive than iron, so its reaction stops after a short time",
            "Aluminium bars are thicker than iron bars, so the corrosion cannot reach the middle",
            "Iron oxide flakes off and lets attack continue, while aluminium oxide seals the surface",
            "Iron is a better conductor, so it carries the corrosion inwards through the metal",
        ],
        "correct_index": 2,
        "why": "The difference is in the corrosion product: one adheres and blocks "
               "the reaction, the other crumbles and exposes fresh metal.",
    },
    {
        "id": "ks4-corrosion-prevention-h08",
        "subtopic_slug": "corrosion-prevention",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A boat owner bolts a copper plate beside the steel hull, expecting it to protect the steel. Predict the outcome and explain it.",
        "options": [
            "The steel corrodes faster, because copper is less reactive than iron",
            "The copper corrodes first, because a bolted plate corrodes before the hull does",
            "Neither metal corrodes, because two metals in contact cancel out",
            "The steel is protected, because any second metal in contact will protect it",
        ],
        "correct_index": 0,
        "why": "Only a MORE reactive metal protects iron; a less reactive one makes "
               "the iron corrode in preference, which is worse than nothing.",
    },
    {
        "id": "ks4-corrosion-prevention-h09",
        "subtopic_slug": "corrosion-prevention",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A 5.6 g sample of iron is fully converted to rust and the product has a mass of 8.0 g. Calculate the mass of oxygen and water taken in.",
        "options": [
            "2.4 g, which is the increase from 5.6 g to 8.0 g",
            "5.6 g, which is the mass of the iron that reacted",
            "8.0 g, which is the mass of the rust that was formed",
            "13.6 g, obtained by adding the two masses given together",
        ],
        "correct_index": 0,
        "why": "Mass is conserved, so the gain of 8.0 - 5.6 = 2.4 g is the mass of "
               "the oxygen and water that combined with the iron.",
    },
    {
        "id": "ks4-corrosion-prevention-h10",
        "subtopic_slug": "corrosion-prevention",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Evaluate the claim that a galvanised roof needs no maintenance for the whole of its life.",
        "options": [
            "The claim holds, because zinc does not corrode under any weather conditions",
            "The claim holds, because a galvanised surface repairs itself after any damage",
            "The claim is weak: the zinc is gradually used up and eventually stops protecting",
            "The claim is weak, because zinc coatings wash away within a year of being fitted",
        ],
        "correct_index": 2,
        "why": "Sacrificial protection consumes the zinc, so a galvanised coating "
               "has a long life but not an indefinite one.",
    },
    {
        "id": "ks4-corrosion-prevention-h11",
        "subtopic_slug": "corrosion-prevention",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Determine which of zinc and tin is the safer coating for an outdoor steel bin, and justify your choice.",
        "options": [
            "Tin, because it is less reactive and lasts longer outdoors",
            "Tin, because it is used inside food cans and so must be tougher",
            "Either would do, because both are barriers on the bin",
            "Zinc, because a damaged zinc layer still protects while a damaged tin layer does not",
        ],
        "correct_index": 3,
        "why": "An outdoor bin will be scratched, and after a scratch tin makes the "
               "iron corrode faster while zinc corrodes instead of it.",
    },
    {
        "id": "ks4-corrosion-prevention-h12",
        "subtopic_slug": "corrosion-prevention",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Iron nails are left in four liquids: distilled water, salt solution, dilute acid, and oil. Predict the order of rusting from fastest to slowest.",
        "options": [
            "Acid, salt solution, distilled water, oil",
            "Oil, distilled water, salt solution, acid",
            "Salt solution, oil, acid, distilled water",
            "Distilled water, acid, oil, salt solution",
        ],
        "correct_index": 0,
        "why": "Acid and dissolved salt both speed up the electrochemical process, "
               "distilled water is slower, and oil keeps out air and water.",
    },
    {
        "id": "ks4-corrosion-prevention-h13",
        "subtopic_slug": "corrosion-prevention",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why a dented tin can is discarded but a scratched galvanised bucket is not.",
        "options": [
            "Tin becomes toxic as soon as it has been scratched, whereas zinc stays entirely safe to handle or touch",
            "A can holds food and a bucket does not, which is the whole of the difference",
            "Tin is less reactive than iron, so a broken tin layer makes the steel corrode faster",
            "A can is thinner than a bucket, so the same scratch goes right through the metal",
        ],
        "correct_index": 2,
        "why": "The two coatings sit on opposite sides of iron in the reactivity "
               "series, so damage has opposite consequences.",
    },
    {
        "id": "ks4-corrosion-prevention-h14",
        "subtopic_slug": "corrosion-prevention",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A bridge owner compares repainting every 8 years at 400 000 pounds with galvanising once at 1 500 000 pounds. Determine after how many years galvanising becomes the cheaper option.",
        "options": [
            "After 8 years, when the first repainting would fall due on the bridge",
            "After 16 years, when two repaintings have cost 800 000 pounds in total",
            "After 32 years, when four repaintings have cost 1 600 000 pounds in total",
            "After 24 years, once three repaintings have cost a total of 1 200 000 pounds between them",
        ],
        "correct_index": 2,
        "why": "Three repaintings cost 1 200 000 pounds, still less than galvanising, "
               "but the fourth takes the total to 1 600 000 pounds.",
    },
    {
        "id": "ks4-corrosion-prevention-h15",
        "subtopic_slug": "corrosion-prevention",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Suggest why a car is protected by paint and also by a coating applied inside its hollow sections.",
        "options": [
            "Paint cannot be applied inside a hollow section, yet water collects there",
            "Paint on the inside would add too much mass to the body of the car",
            "The inside of a car body is made of aluminium, which paint will not stick to",
            "Paint works just where it is exposed to sunlight, which the inside is not",
        ],
        "correct_index": 0,
        "why": "Hidden cavities trap damp air and road salt, and rust that starts "
               "there is neither visible nor reachable with a brush.",
    },
    {
        "id": "ks4-corrosion-prevention-h16",
        "subtopic_slug": "corrosion-prevention",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Evaluate the claim that a metal which resists corrosion must be unreactive.",
        "options": [
            "The claim holds: an unreactive metal alone survives damp air",
            "The claim is weak, because reactivity and corrosion are unconnected",
            "The claim holds, since reactivity measures how fast a metal corrodes",
            "The claim is weak: aluminium is reactive, and it is its own oxide that protects it",
        ],
        "correct_index": 3,
        "why": "What matters is whether the corrosion product seals the surface, and "
               "a reactive metal can form exactly such a layer.",
    },
    {
        "id": "ks4-corrosion-prevention-h17",
        "subtopic_slug": "corrosion-prevention",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A student says the three-nail rusting experiment would give the same result if the boiled water were not covered with oil. Explain why it would not.",
        "options": [
            "Without the oil the water would evaporate, leaving the nail in dry air",
            "Without the oil the water would freeze, and frozen nails do not rust",
            "Without the oil the water would turn acidic and rust the nail faster",
            "Without the oil, oxygen would dissolve back into the water and the nail would rust",
        ],
        "correct_index": 3,
        "why": "Boiling drives dissolved oxygen out, and the oil layer is what stops "
               "the air putting it back.",
    },
    {
        "id": "ks4-corrosion-prevention-h18",
        "subtopic_slug": "corrosion-prevention",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Determine why a steel pipeline running through wet ground needs magnesium blocks rather than zinc ones for the longest protection.",
        "options": [
            "Magnesium is cheaper per kilogram, so more of it can be fitted for the money",
            "Magnesium is further above iron in the reactivity series, so it drives protection harder",
            "Magnesium is heavier than zinc, so a block of it lasts proportionally longer",
            "Magnesium conducts heat better, so it keeps the pipeline warm and dry",
        ],
        "correct_index": 1,
        "why": "The greater the reactivity difference, the more strongly the "
               "sacrificial metal is corroded in preference to the iron.",
    },

    # ── standard (top-up) ──────────────────────────────────────────────
    {
        "id": "ks4-corrosion-prevention-s19",
        "subtopic_slug": "corrosion-prevention",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "State the name given to the process by which aluminium's "
                "thin oxide layer protects it from any further reaction with "
                "the air.",
        "options": [
            "Passivation",
            "Galvanising",
            "Electroplating",
            "Sacrificial protection",
        ],
        "correct_index": 0,
        "why": "Passivation is the name given to a surface layer that "
               "stops a reactive metal reacting any further.",
    },
    {
        "id": "ks4-corrosion-prevention-s20",
        "subtopic_slug": "corrosion-prevention",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why a thicker layer of galvanising protects steel "
                "for longer than a thin one.",
        "options": [
            "A thicker layer is a better barrier, so no water can ever reach "
            "the steel through it",
            "There is more zinc available to corrode sacrificially before "
            "the steel is left unprotected",
            "A thicker layer conducts electricity less well, which slows the "
            "corrosion reaction down",
            "A thicker layer makes the surface of the steel harder, which "
            "resists corrosion directly",
        ],
        "correct_index": 1,
        "why": "Sacrificial protection lasts only as long as there is zinc "
               "left to be consumed, so more zinc means a longer working "
               "life for the coating.",
    },
    {
        "id": "ks4-corrosion-prevention-s21",
        "subtopic_slug": "corrosion-prevention",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "A rusting nail gains mass of 0.1 g, 0.2 g, 0.3 g and 0.4 g "
                "after 1, 2, 3 and 4 days respectively. Assuming the same "
                "steady rate continues, predict the mass gained after 6 days.",
        "options": [
            "0.5 g",
            "0.6 g",
            "0.8 g",
            "1.0 g",
        ],
        "correct_index": 1,
        "why": "The mass rises by 0.1 g each day, so after 6 days the gain "
               "is 6 × 0.1 = 0.6 g.",
    },
    {
        "id": "ks4-corrosion-prevention-s22",
        "subtopic_slug": "corrosion-prevention",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "A homeowner chooses galvanised steel guttering over "
                "stainless steel guttering for a new roof. Suggest the most "
                "likely reason.",
        "options": [
            "Galvanised steel is a far better electrical conductor, which "
            "guttering has to be",
            "Galvanised steel is cheaper and gives corrosion resistance that "
            "is good enough for the job",
            "Galvanised steel is harder than stainless steel, so it "
            "survives falling roof tiles far better",
            "Galvanised steel needs noticeably less maintenance over its "
            "life than stainless steel does",
        ],
        "correct_index": 1,
        "why": "Guttering does not need the appearance or the extra "
               "corrosion resistance of stainless steel, so the cheaper "
               "galvanised option is usually chosen instead.",
    },
    {
        "id": "ks4-corrosion-prevention-s23",
        "subtopic_slug": "corrosion-prevention",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain, in terms of electrons, why zinc corrodes in "
                "preference to iron when the two metals are in contact.",
        "options": [
            "Zinc gives up its electrons more readily than iron does, so it "
            "reacts in the iron's place",
            "Zinc takes electrons from the iron, which forces the iron to "
            "react instead",
            "Zinc conducts electrons away from the iron before they can "
            "reach the oxygen in the air",
            "Zinc has no electrons of its own to lose, so the iron is left "
            "completely unaffected",
        ],
        "correct_index": 0,
        "why": "Zinc is the more reactive metal, so it loses its outer "
               "electrons to form ions more easily than iron does, which is "
               "what sacrificial protection depends on.",
    },
    {
        "id": "ks4-corrosion-prevention-s24",
        "subtopic_slug": "corrosion-prevention",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Compare how galvanising and how stainless steel each resist "
                "corrosion.",
        "options": [
            "Galvanising coats the surface with a more reactive metal; "
            "stainless steel is alloyed throughout with chromium",
            "Galvanising is alloyed throughout with zinc; stainless steel "
            "instead coats just the surface with a layer of chromium",
            "Both work by coating the surface, one with zinc and the other "
            "with chromium",
            "Both work by alloying a second metal all through the steel",
        ],
        "correct_index": 0,
        "why": "Galvanising is a coating that also protects sacrificially; "
               "stainless steel's chromium is mixed through the whole alloy "
               "and forms its own protective oxide.",
    },
    {
        "id": "ks4-corrosion-prevention-s25",
        "subtopic_slug": "corrosion-prevention",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Suggest why a gas company pays to inspect and replace the "
                "sacrificial anodes on a buried pipeline every few years, "
                "even though this adds an ongoing cost.",
        "options": [
            "It is a legal requirement that has no real connection to "
            "preventing corrosion of the pipeline itself",
            "It is far cheaper than repairing a leak from a corroded section "
            "of pipeline later",
            "It raises the value of the land the pipeline runs beneath",
            "It is required just the once, with any further inspection "
            "left as optional after that first check",
        ],
        "correct_index": 1,
        "why": "A leak in a buried gas pipeline is expensive and dangerous "
               "to repair, so the smaller ongoing cost of maintaining "
               "sacrificial protection is worth paying.",
    },
    {
        "id": "ks4-corrosion-prevention-s26",
        "subtopic_slug": "corrosion-prevention",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "State the term used for the corrosion process that speeds "
                "up when a dissolved electrolyte, such as salt, is present in "
                "the water touching a metal.",
        "options": [
            "Thermal decomposition",
            "Neutralisation",
            "Electrolysis",
            "Electrochemical corrosion",
        ],
        "correct_index": 3,
        "why": "Rusting proceeds by charge moving through the water at the "
               "metal's surface, which is why it is described as an "
               "electrochemical process.",
    },

    # ── harder (top-up) ─────────────────────────────────────────────────
    {
        "id": "ks4-corrosion-prevention-h19",
        "subtopic_slug": "corrosion-prevention",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "An engineer claims that an underground aluminium cable "
                "sheath needs no paint because the metal 'protects itself'. "
                "Evaluate this claim.",
        "options": [
            "Unsound: aluminium is more reactive than iron, so it needs a "
            "barrier coating just as badly, if not more so",
            "Sound: the oxide layer reseals itself if lightly scratched, so "
            "paint adds little extra corrosion protection",
            "Unsound, because aluminium's oxide layer forms specifically "
            "once the metal has already been painted over",
            "Sound, because aluminium is generally considered not to react "
            "with oxygen under ordinary conditions",
        ],
        "correct_index": 1,
        "why": "Passivation is a genuine form of self-protection, unlike "
               "flaking rust, so for corrosion resistance alone the claim "
               "largely holds.",
    },
    {
        "id": "ks4-corrosion-prevention-h20",
        "subtopic_slug": "corrosion-prevention",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A galvanised coating is 20 micrometres thick and loses zinc "
                "at 2 micrometres per year in a coastal climate. Determine "
                "how many more years of protection remain once 8 micrometres "
                "has already been lost.",
        "options": [
            "4 years",
            "6 years",
            "10 years",
            "12 years",
        ],
        "correct_index": 1,
        "why": "20 − 8 = 12 micrometres of zinc remain, and at 2 micrometres "
               "a year that gives 12 ÷ 2 = 6 more years.",
    },
    {
        "id": "ks4-corrosion-prevention-h21",
        "subtopic_slug": "corrosion-prevention",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain, in terms of electrons, why bolting a copper plate "
                "to a steel hull makes the steel corrode faster rather than "
                "protecting it.",
        "options": [
            "Copper gives its electrons to the steel, which speeds up the "
            "steel's own reaction with oxygen",
            "Iron gives up its electrons more readily than copper does, so "
            "the iron becomes the one that reacts",
            "Copper reacts with the water first, releasing acid that attacks "
            "the steel directly",
            "Copper is a poor conductor, so it forces the electrons to build "
            "up inside the steel instead",
        ],
        "correct_index": 1,
        "why": "Between iron and a less reactive metal it is iron that "
               "loses electrons more easily, so contact with copper reverses "
               "the direction protection normally works in.",
    },
    {
        "id": "ks4-corrosion-prevention-h22",
        "subtopic_slug": "corrosion-prevention",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Replacing a corroded pipeline costs 2 000 000 pounds. "
                "Fitting and replacing sacrificial anodes over the same "
                "30-year period costs 150 000 pounds in total. Calculate how "
                "many times more expensive the replacement would be.",
        "options": [
            "About 1.3 times",
            "About 4 times",
            "About 13 times",
            "About 30 times",
        ],
        "correct_index": 2,
        "why": "2 000 000 ÷ 150 000 is about 13.3, so replacement costs "
               "roughly thirteen times as much as the anode programme.",
    },
    {
        "id": "ks4-corrosion-prevention-h23",
        "subtopic_slug": "corrosion-prevention",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A ship's aluminium hull is constantly rubbed against a "
                "gravel seabed as the tide rises and falls. Evaluate whether "
                "passivation still protects the hull under these conditions.",
        "options": [
            "Yes, because passivation reforms instantly and needs no real "
            "time to reseal a fresh scratch in the surface",
            "Yes, because continuous abrasion has little effect on how well "
            "an oxide layer is able to protect a metal underneath it",
            "No: constant abrasion can wear the oxide away faster than it "
            "can reform, exposing bare metal continuously",
            "No, because passivation is thought to work on metals kept "
            "completely away from any water whatsoever",
        ],
        "correct_index": 2,
        "why": "Passivation copes well with an occasional scratch, but "
               "continuous mechanical wear can strip the oxide away faster "
               "than it rebuilds, which a single scratch does not.",
    },
    {
        "id": "ks4-corrosion-prevention-h24",
        "subtopic_slug": "corrosion-prevention",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Sodium is far more reactive than iron, yet it is never used "
                "as a sacrificial anode. Explain why.",
        "options": [
            "Sodium is too expensive to be used in any industrial "
            "application of this kind",
            "Sodium reacts violently and dangerously with water, making it "
            "impractical and unsafe to fit and handle",
            "Sodium is less reactive than zinc, so it would fail to protect "
            "the iron in any meaningful way",
            "Sodium conducts electricity too well, which would damage the "
            "steel structure it was meant to protect",
        ],
        "correct_index": 1,
        "why": "A sacrificial anode has to be safe to install and handle; "
               "sodium's violent reaction with water rules it out even "
               "though its reactivity would in principle work.",
    },
    {
        "id": "ks4-corrosion-prevention-h25",
        "subtopic_slug": "corrosion-prevention",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A council is choosing a finish for a steel slide in a "
                "children's playground, where sharp flakes of rust would be a "
                "safety hazard. Determine the most suitable method and "
                "justify it.",
        "options": [
            "Grease, because it is the cheapest way to keep water off any "
            "outdoor structure a council might own",
            "Galvanising, because a scratched coating still protects and "
            "will not flake into sharp rust",
            "A sacrificial block bolted nearby, since that method works well "
            "for a ship's hull in the open sea",
            "No coating whatsoever, since children rub the surface smooth "
            "as they play on the slide",
        ],
        "correct_index": 1,
        "why": "Galvanising resists damage from play and, even if scratched, "
               "corrodes as zinc rather than leaving the flaking, sharp rust "
               "an unprotected surface would produce.",
    },
    {
        "id": "ks4-corrosion-prevention-h26",
        "subtopic_slug": "corrosion-prevention",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why a permanently submerged steel structure is "
                "usually fitted with bolted sacrificial blocks rather than "
                "relying on galvanising alone, even though galvanising also "
                "gives sacrificial protection.",
        "options": [
            "A thin galvanised layer is used up quickly under constant "
            "immersion, while replaceable blocks can be renewed as needed",
            "Galvanising works well in air but stops giving any real "
            "protection once it is placed permanently underwater",
            "Bolted blocks conduct electricity better than a thin coating "
            "does, which is the property that matters most underwater",
            "Galvanising reacts with seawater to form a substance that "
            "actively attacks the steel beneath it",
        ],
        "correct_index": 0,
        "why": "Continuous immersion consumes a sacrificial coating far "
               "faster than intermittent exposure, so a thin galvanised "
               "layer would not last; large replaceable blocks are used "
               "instead so protection can be renewed.",
    },
]
