"""Chemistry · Using resources — the MRB-338 expansion for `ceramics-polymers-composites`.

The shipped rows name soda-lime glass, contrast LDPE with HDPE and define a
composite, so the weight here falls on the material science those rows stand
on: what a ceramic is and why firing makes it hard and brittle, what cross-links
do to a polymer chain, and what the matrix and the reinforcement each contribute
to a composite rather than merely that a composite has both.

Round that sit the named materials the spec asks for — borosilicate glass and
thermal shock, fibreglass, carbon fibre reinforced plastic, cement and
aggregate — together with the selection questions an engineer actually faces:
furnace tiles, a turbine blade, a fire-door window, a boat hull. Four rows carry
percentage-composition arithmetic on glass and on composite panels.
"""

TOPIC = "resources"
SUBJECT = "chemistry"

QUESTIONS = [
    # ---------------------------------------------------------------- easier
    {
        "id": "ks4-ceramics-polymers-composites-e05",
        "subtopic_slug": "ceramics-polymers-composites",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Which substance is heated with sand to make the glass used "
                "for ovenproof dishes and laboratory glassware?",
        "options": [
            "Boron trioxide",
            "Sodium carbonate",
            "Calcium carbonate",
            "Aluminium oxide",
        ],
        "correct_index": 0,
        "why": "Borosilicate glass is made from sand and boron trioxide, which "
               "gives it a higher melting point than soda-lime glass.",
    },
    {
        "id": "ks4-ceramics-polymers-composites-e06",
        "subtopic_slug": "ceramics-polymers-composites",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Which set of properties best describes a fired clay ceramic?",
        "options": [
            "Soft, flexible and a good conductor of electricity and of heat",
            "Hard, brittle and a poor conductor of electricity",
            "Hard, malleable and a good conductor of heat",
            "Soft, brittle and a good conductor of heat",
        ],
        "correct_index": 1,
        "why": "Clay ceramics are hard and brittle, and they insulate rather "
               "than conduct, which is why they are used for electrical "
               "fittings and building materials.",
    },
    {
        "id": "ks4-ceramics-polymers-composites-e07",
        "subtopic_slug": "ceramics-polymers-composites",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "A polymer softens when it is heated and can be remoulded. "
                "Which structural feature explains this?",
        "options": [
            "Its chains are joined by cross-links into one network",
            "Its chains are held to each other by strong covalent bonds",
            "There are no cross-links joining its chains together",
            "Its chains carry a charge, so they repel one another",
        ],
        "correct_index": 2,
        "why": "With no cross-links the chains are held only by weak forces, "
               "so heating lets them slide past one another and the polymer "
               "softens.",
    },
    {
        "id": "ks4-ceramics-polymers-composites-e08",
        "subtopic_slug": "ceramics-polymers-composites",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Which material is a composite of glass fibres held in a "
                "polymer matrix?",
        "options": [
            "Borosilicate glass, which is used in a lab",
            "A clay ceramic, such as a roof tile",
            "Soda-lime glass, which is made from sand",
            "Fibreglass, which is also called GRP",
        ],
        "correct_index": 3,
        "why": "Fibreglass, or glass-reinforced plastic, is glass fibres set "
               "in a polymer resin, so it has two components and is a "
               "composite.",
    },
    {
        "id": "ks4-ceramics-polymers-composites-e09",
        "subtopic_slug": "ceramics-polymers-composites",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "In concrete, which material holds the sand and gravel "
                "together?",
        "options": [
            "Clay, which is fired in a hot kiln",
            "Cement, which sets hard around them",
            "Resin, which is a liquid polymer",
            "Glass, which is melted over them",
        ],
        "correct_index": 1,
        "why": "Cement is the matrix of concrete: it sets around the "
               "aggregate and binds the whole mixture into one solid.",
    },
    {
        "id": "ks4-ceramics-polymers-composites-e10",
        "subtopic_slug": "ceramics-polymers-composites",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "In carbon fibre reinforced plastic, which part is the "
                "reinforcement?",
        "options": [
            "The resin that surrounds everything",
            "Air bubbles trapped inside the resin",
            "The carbon fibres set into the resin",
            "The paint sprayed on the outside",
        ],
        "correct_index": 2,
        "why": "The fibres are the reinforcement; the polymer resin around "
               "them is the matrix.",
    },
    {
        "id": "ks4-ceramics-polymers-composites-e11",
        "subtopic_slug": "ceramics-polymers-composites",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Ceramics are non-metallic solids made by which process?",
        "options": [
            "Heating the starting materials to a high temperature",
            "Dissolving the starting materials in a strong acid and drying "
            "them",
            "Cooling the starting materials below freezing point",
            "Passing electricity through the molten materials",
        ],
        "correct_index": 0,
        "why": "A ceramic is formed by heating inorganic starting materials "
               "strongly, as when clay is fired or sand is melted into glass.",
    },
    {
        "id": "ks4-ceramics-polymers-composites-e12",
        "subtopic_slug": "ceramics-polymers-composites",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Sand is one of the raw materials for glass. Which compound "
                "is it?",
        "options": [
            "Sodium chloride",
            "Calcium sulfate",
            "Aluminium oxide",
            "Silicon dioxide",
        ],
        "correct_index": 3,
        "why": "Sand is silicon dioxide, SiO2, and it is the main source of "
               "the silicon in every kind of glass.",
    },
    {
        "id": "ks4-ceramics-polymers-composites-e13",
        "subtopic_slug": "ceramics-polymers-composites",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "In a composite, what is meant by the matrix?",
        "options": [
            "The short fibres that are added for strength",
            "The continuous material that binds the rest",
            "The mould that gives the finished part its final shape",
            "The coating that is sprayed on at the end",
        ],
        "correct_index": 1,
        "why": "The matrix is the continuous phase surrounding the "
               "reinforcement, holding it in place and passing forces to it.",
    },
    {
        "id": "ks4-ceramics-polymers-composites-e14",
        "subtopic_slug": "ceramics-polymers-composites",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Give the property of soda-lime glass that makes it suitable "
                "for a window.",
        "options": [
            "It conducts heat, so a room warms up quickly",
            "It is soft, so it can be cut to shape by hand",
            "It is flexible, so it bends in a strong wind",
            "It is transparent, so light passes through it",
        ],
        "correct_index": 3,
        "why": "Soda-lime glass is transparent, which is the whole reason a "
               "window is made of it rather than of brick or metal.",
    },
    {
        "id": "ks4-ceramics-polymers-composites-e15",
        "subtopic_slug": "ceramics-polymers-composites",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Give one everyday use of a clay ceramic.",
        "options": [
            "Bricks and roof tiles for a building",
            "Cling film for wrapping up food",
            "Carrier bags at a supermarket",
            "Fizzy drinks bottles and their lids",
        ],
        "correct_index": 0,
        "why": "Bricks and tiles are shaped from wet clay and fired, which "
               "makes them hard, rigid and weatherproof.",
    },
    {
        "id": "ks4-ceramics-polymers-composites-e16",
        "subtopic_slug": "ceramics-polymers-composites",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Which glass is least likely to crack when a hot dish from "
                "the oven is put straight into cold water?",
        "options": [
            "Soda-lime glass, which contains sodium",
            "Borosilicate glass, which contains boron",
            "Lead crystal glass, which contains lead oxide",
            "Bottle glass, which is made in a mould",
        ],
        "correct_index": 1,
        "why": "Borosilicate glass expands very little on heating, so a "
               "sudden temperature change sets up much less stress in it.",
    },
    {
        "id": "ks4-ceramics-polymers-composites-e17",
        "subtopic_slug": "ceramics-polymers-composites",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Ceramics are described as brittle. What does brittle mean?",
        "options": [
            "It can be pulled out into a long thin wire without snapping",
            "It returns to its own shape after bending",
            "It can be hammered out into a thin sheet",
            "It shatters or snaps without bending first",
        ],
        "correct_index": 3,
        "why": "A brittle material breaks suddenly under load instead of "
               "deforming, which is why a dropped tile snaps rather than bends.",
    },
    {
        "id": "ks4-ceramics-polymers-composites-e18",
        "subtopic_slug": "ceramics-polymers-composites",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State one property that makes a polymer suitable for a "
                "drinks bottle.",
        "options": [
            "It is hard and brittle, like a fired tile",
            "It is light and does not shatter if dropped",
            "It conducts electricity away from the drink",
            "It melts well above one thousand degrees",
        ],
        "correct_index": 1,
        "why": "A polymer bottle is low in density and deforms rather than "
               "shattering, so it survives being dropped.",
    },
    # -------------------------------------------------------------- standard
    {
        "id": "ks4-ceramics-polymers-composites-s05",
        "subtopic_slug": "ceramics-polymers-composites",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why a polymer whose chains are joined by cross-links "
                "cannot be melted down and remoulded.",
        "options": [
            "The cross-links lock the chains into one rigid network",
            "The cross-links make the chains far too short to move",
            "The cross-links make the polymer dissolve in hot water",
            "The cross-links give the chains an electrical charge",
        ],
        "correct_index": 0,
        "why": "Cross-links are covalent bonds between chains, so the chains "
               "cannot slide; heating strongly makes the polymer decompose "
               "rather than melt.",
    },
    {
        "id": "ks4-ceramics-polymers-composites-s06",
        "subtopic_slug": "ceramics-polymers-composites",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Suggest why the lining tiles inside a pottery kiln are made "
                "from a ceramic.",
        "options": [
            "A ceramic stores the heat and gives it back as fuel",
            "A ceramic conducts heat quickly out through the kiln walls and "
            "roof",
            "A ceramic keeps its shape at very high temperatures",
            "A ceramic expands a great deal as the kiln warms up",
        ],
        "correct_index": 2,
        "why": "Ceramics have very high melting points and are unreactive, so "
               "they survive repeated firing without softening or corroding.",
    },
    {
        "id": "ks4-ceramics-polymers-composites-s07",
        "subtopic_slug": "ceramics-polymers-composites",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Suggest why the hull of a small sailing dinghy is made from "
                "glass reinforced plastic rather than from sheet steel.",
        "options": [
            "It is denser, so the dinghy sits lower and is steadier",
            "It is strong but low in density, and it does not rust",
            "It conducts heat well, so the hull dries out after a sail",
            "It melts at a low temperature, so repairs are very cheap",
        ],
        "correct_index": 1,
        "why": "GRP gives the strength of the glass fibres at a fraction of "
               "the mass of steel, and neither the resin nor the glass "
               "corrodes in sea water.",
    },
    {
        "id": "ks4-ceramics-polymers-composites-s08",
        "subtopic_slug": "ceramics-polymers-composites",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Dried mud with straw mixed through it is much stronger than "
                "dried mud alone. Explain the job the straw does.",
        "options": [
            "The straw makes the mud dry out much more quickly",
            "The straw fibres carry the pulling forces the mud cannot",
            "The straw reacts with the mud to make a new compound",
            "The straw fills the gaps in the mud so the finished block weighs "
            "more",
        ],
        "correct_index": 1,
        "why": "Mud is weak in tension; the straw acts as the reinforcement "
               "and takes the pulling forces, exactly as steel does in "
               "reinforced concrete.",
    },
    {
        "id": "ks4-ceramics-polymers-composites-s09",
        "subtopic_slug": "ceramics-polymers-composites",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "A concrete mix contains 6 kg of cement for every 24 kg of "
                "aggregate. Calculate the percentage of the mix that is "
                "cement.",
        "options": [
            "25%",
            "20%",
            "24%",
            "4%",
        ],
        "correct_index": 1,
        "why": "The total mass is 6 + 24 = 30 kg, so the cement fraction is "
               "6 / 30 = 0.20, which is 20%.",
    },
    {
        "id": "ks4-ceramics-polymers-composites-s10",
        "subtopic_slug": "ceramics-polymers-composites",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Suggest why the outer shell of a cycling helmet is made from "
                "a fibre-reinforced polymer and not from plain glass.",
        "options": [
            "The composite spreads the force instead of shattering",
            "The composite is a great deal denser than plain glass",
            "The composite lets the rider see through the shell",
            "The composite melts on impact and absorbs the blow",
        ],
        "correct_index": 0,
        "why": "The fibres stop a crack running through the shell, so the "
               "composite deforms and spreads the load rather than breaking "
               "into sharp pieces.",
    },
    {
        "id": "ks4-ceramics-polymers-composites-s11",
        "subtopic_slug": "ceramics-polymers-composites",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "An airline replaces aluminium panels on its aircraft with "
                "composite panels of the same strength. Suggest why this "
                "saves the airline money.",
        "options": [
            "The composite panels cost less per kilogram to buy",
            "The composite panels can be melted down and reused",
            "A lighter aircraft burns less fuel on every flight",
            "A composite panel needs no paint or surface finish",
        ],
        "correct_index": 2,
        "why": "The composite has a much lower density than aluminium, so the "
               "same strength comes at a lower mass and the fuel bill falls.",
    },
    {
        "id": "ks4-ceramics-polymers-composites-s12",
        "subtopic_slug": "ceramics-polymers-composites",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "A fired clay pot cannot be softened and reshaped, but a "
                "poly(ethene) bowl can. Explain the difference.",
        "options": [
            "The pot is a giant rigid structure; the bowl has chains",
            "The pot has cross-links added to it; the bowl has much shorter "
            "chains",
            "The pot is a metal oxide; the bowl is a metal carbonate",
            "The pot was cooled slowly; the bowl was cooled quickly",
        ],
        "correct_index": 0,
        "why": "Firing fuses the clay into one giant network of strong bonds, "
               "while the polymer's separate chains only need weak forces "
               "overcome before they can slide.",
    },
    {
        "id": "ks4-ceramics-polymers-composites-s13",
        "subtopic_slug": "ceramics-polymers-composites",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "A 2.5 kg sample of carbon fibre reinforced plastic is 60% "
                "carbon fibre by mass. Calculate the mass of carbon fibre in "
                "the sample.",
        "options": [
            "0.60 kg",
            "1.0 kg",
            "1.5 kg",
            "4.2 kg",
        ],
        "correct_index": 2,
        "why": "60% of 2.5 kg is 0.60 x 2.5 = 1.5 kg of carbon fibre, leaving "
               "1.0 kg of polymer matrix.",
    },
    {
        "id": "ks4-ceramics-polymers-composites-s14",
        "subtopic_slug": "ceramics-polymers-composites",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "A fire door needs a small window that will survive a fire "
                "for 30 minutes. Suggest which material to use and why.",
        "options": [
            "A polymer sheet, because it flexes as the door heats",
            "An aluminium sheet, because it stays clear when it is hot",
            "A ceramic glass, because it holds its shape when hot",
            "A composite panel, because its glass fibres are very strong "
            "indeed",
        ],
        "correct_index": 2,
        "why": "Only the ceramic keeps a rigid, transparent shape at fire "
               "temperatures; a polymer would soften and a metal would not "
               "let anyone see through.",
    },
    {
        "id": "ks4-ceramics-polymers-composites-s15",
        "subtopic_slug": "ceramics-polymers-composites",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Suggest why sand is heated together with sodium carbonate "
                "rather than being melted on its own.",
        "options": [
            "The mixture melts at a lower temperature than sand",
            "The mixture reacts to make a brand new element",
            "The mixture sets much harder once it has cooled",
            "The mixture is easier to dig out of the ground",
        ],
        "correct_index": 0,
        "why": "Adding sodium carbonate lowers the temperature at which the "
               "mixture melts, which cuts the energy the furnace needs.",
    },
    {
        "id": "ks4-ceramics-polymers-composites-s16",
        "subtopic_slug": "ceramics-polymers-composites",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "A gardener wants plant pots that will survive being left "
                "outside through a hard frost. Suggest a material and a "
                "reason.",
        "options": [
            "Clay, because a ceramic bends slightly as ice forms",
            "Glass, because a transparent pot warms the roots up",
            "A polymer, because it flexes rather than shattering",
            "Cement, because concrete takes in water and holds it as it "
            "freezes",
        ],
        "correct_index": 2,
        "why": "A polymer deforms a little when trapped water freezes and "
               "expands, whereas a brittle ceramic pot cracks.",
    },
    {
        "id": "ks4-ceramics-polymers-composites-s17",
        "subtopic_slug": "ceramics-polymers-composites",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why the fibres in a composite must be firmly bonded "
                "into the matrix.",
        "options": [
            "A loose fibre would react with the matrix around it",
            "The matrix passes the force on, so a loose fibre carries none",
            "A loose fibre would lower the density of the whole part",
            "The matrix has to conduct heat away from every fibre",
        ],
        "correct_index": 1,
        "why": "Load reaches the reinforcement only through the matrix, so a "
               "fibre that slips takes no share of the force and the "
               "composite is no stronger than the matrix alone.",
    },
    {
        "id": "ks4-ceramics-polymers-composites-s18",
        "subtopic_slug": "ceramics-polymers-composites",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Suggest why the floor of a busy hospital corridor is tiled "
                "with a ceramic.",
        "options": [
            "A ceramic is hard, so trolleys do not wear it away",
            "A ceramic is soft, so footsteps make very little noise",
            "A ceramic conducts, so static charge cannot build up",
            "A ceramic is flexible, so the floor gives underfoot",
        ],
        "correct_index": 0,
        "why": "Ceramic tiles are hard and chemically unreactive, so they "
               "resist scratching and survive repeated cleaning.",
    },
    # ---------------------------------------------------------------- harder
    {
        "id": "ks4-ceramics-polymers-composites-h05",
        "subtopic_slug": "ceramics-polymers-composites",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A wind turbine blade is 80 m long. Explain why a carbon "
                "fibre composite is chosen for it rather than an aluminium "
                "alloy of the same strength.",
        "options": [
            "The composite conducts less heat, so the blade stays cooler",
            "The alloy would rust in rain, while the composite cannot rust",
            "The composite is far cheaper per kilogram than the alloy is",
            "The composite is far less dense, so the blade's own weight bends "
            "it less",
        ],
        "correct_index": 3,
        "why": "An 80 m blade is loaded mostly by its own mass, so cutting "
               "the density at equal strength cuts the bending force the "
               "blade has to carry.",
    },
    {
        "id": "ks4-ceramics-polymers-composites-h06",
        "subtopic_slug": "ceramics-polymers-composites",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain, in terms of structure, why a fired ceramic is "
                "brittle while a metal is malleable.",
        "options": [
            "The ceramic's bonds cannot re-form when layers shift; metal "
            "layers slide and stay bonded",
            "The ceramic has free electrons holding it rigid, while a metal "
            "has none of them",
            "The ceramic is made of small molecules with weak forces, while a "
            "metal is a giant molecule",
            "The ceramic is a mixture of two solids, while a metal is a pure "
            "element in a single layer",
        ],
        "correct_index": 0,
        "why": "In a ceramic the rigid directional bonds break when layers "
               "are forced past each other, while metallic bonding survives "
               "the layers sliding.",
    },
    {
        "id": "ks4-ceramics-polymers-composites-h07",
        "subtopic_slug": "ceramics-polymers-composites",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A student says a glass fibre composite must be weak because "
                "glass shatters. Evaluate this reasoning.",
        "options": [
            "Correct, because the composite shatters exactly as glass does",
            "Wrong, because the resin stops a crack running fibre to fibre",
            "Wrong, because the glass fibres melt before they can shatter",
            "Correct, because a composite is no better than its weakest "
            "single part",
        ],
        "correct_index": 1,
        "why": "A crack in one fibre is stopped by the surrounding resin, so "
               "the composite is tough even though bulk glass is brittle.",
    },
    {
        "id": "ks4-ceramics-polymers-composites-h08",
        "subtopic_slug": "ceramics-polymers-composites",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A composite panel is 30% glass fibre and 70% resin by mass. "
                "A boat builder has 45 kg of glass fibre. Calculate the mass "
                "of composite this makes.",
        "options": [
            "13.5 kg",
            "64.3 kg",
            "105 kg",
            "150 kg",
        ],
        "correct_index": 3,
        "why": "The fibre is 30% of the total, so the total is 45 / 0.30 = "
               "150 kg, of which 105 kg is resin.",
    },
    {
        "id": "ks4-ceramics-polymers-composites-h09",
        "subtopic_slug": "ceramics-polymers-composites",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Borosilicate glass costs about three times as much as "
                "soda-lime glass. Evaluate using it for every window in a "
                "house.",
        "options": [
            "Worth it, because the extra boron makes the pane much stronger",
            "Worth it, because soda-lime glass slowly dissolves in rainwater",
            "Not worth it, because a window is never heated in the way "
            "borosilicate is designed for",
            "Not worth it, because borosilicate glass is too cloudy to see "
            "out through",
        ],
        "correct_index": 2,
        "why": "The property being paid for is resistance to sudden heating, "
               "and a house window never meets that, so the extra cost buys "
               "nothing useful.",
    },
    {
        "id": "ks4-ceramics-polymers-composites-h10",
        "subtopic_slug": "ceramics-polymers-composites",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A racing car has a carbon fibre composite body but ceramic "
                "brake discs. Explain why two different materials are used.",
        "options": [
            "The composite is the heavier of the two, so it belongs low down",
            "The ceramic is transparent, so the driver can see the brakes",
            "The polymer matrix would soften at brake temperatures",
            "The ceramic is lighter than the composite, so it saves mass",
        ],
        "correct_index": 2,
        "why": "Brakes reach several hundred degrees, which is far above the "
               "temperature at which the composite's polymer matrix loses its "
               "strength, while a ceramic is unaffected.",
    },
    {
        "id": "ks4-ceramics-polymers-composites-h11",
        "subtopic_slug": "ceramics-polymers-composites",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Compare a plain polymer roof panel with the same polymer "
                "reinforced with glass fibres, for a garage carrying winter "
                "snow.",
        "options": [
            "The reinforced panel is stiffer, so it sags less under the snow",
            "The reinforced panel is softer, so it sheds the snow a great "
            "deal sooner",
            "The two panels behave the same, as the polymer does the work",
            "The plain panel is stronger, as the fibres weaken the polymer",
        ],
        "correct_index": 0,
        "why": "The glass fibres carry the tension in the underside of the "
               "panel, so the reinforced panel deflects far less for the same "
               "load of snow.",
    },
    {
        "id": "ks4-ceramics-polymers-composites-h12",
        "subtopic_slug": "ceramics-polymers-composites",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why the melting point of a ceramic is far higher "
                "than that of a polymer.",
        "options": [
            "The ceramic is made of heavier atoms, and heavy atoms hold on "
            "to each other more tightly",
            "The ceramic is one giant network of strong bonds; a polymer has "
            "weak forces between chains",
            "The ceramic has already been heated once in a kiln, so it cannot "
            "take in any more energy",
            "The ceramic contains no carbon, and carbon always lowers the "
            "melting point of a solid",
        ],
        "correct_index": 1,
        "why": "Melting a ceramic means breaking strong bonds throughout a "
               "giant structure, while melting a polymer only means "
               "overcoming the weak forces holding separate chains together.",
    },
    {
        "id": "ks4-ceramics-polymers-composites-h13",
        "subtopic_slug": "ceramics-polymers-composites",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A glass is 75% sand, 15% sodium carbonate and 10% limestone "
                "by mass. Calculate the mass of sand needed for 2.4 tonnes of "
                "the glass.",
        "options": [
            "0.24 tonnes",
            "0.36 tonnes",
            "1.8 tonnes",
            "3.2 tonnes",
        ],
        "correct_index": 2,
        "why": "75% of 2.4 tonnes is 0.75 x 2.4 = 1.8 tonnes of sand, with "
               "0.36 tonnes of sodium carbonate and 0.24 tonnes of limestone.",
    },
    {
        "id": "ks4-ceramics-polymers-composites-h14",
        "subtopic_slug": "ceramics-polymers-composites",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A car maker replaces a steel bumper with one moulded from a "
                "polymer that softens on heating. Evaluate the change.",
        "options": [
            "Lighter and free of rust, but it can deform on a hot day",
            "Heavier and free of rust, so the car handles a great deal better "
            "on a bend",
            "Lighter and much stiffer, so the bumper will never deform",
            "Lighter but it will rust faster than the steel bumper did",
        ],
        "correct_index": 0,
        "why": "The polymer cuts mass and cannot corrode, but with no "
               "cross-links it loses stiffness as it warms, which steel does "
               "not.",
    },
    {
        "id": "ks4-ceramics-polymers-composites-h15",
        "subtopic_slug": "ceramics-polymers-composites",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Predict what happens to a glass fibre composite canoe put on "
                "a bonfire, and explain your answer.",
        "options": [
            "Nothing happens, because a composite cannot burn at all",
            "The glass fibres burn away and the resin is left as a shell",
            "The whole canoe melts evenly into a single pool of liquid",
            "The resin burns away, leaving loose fibres with no strength",
        ],
        "correct_index": 3,
        "why": "The polymer matrix is the part that burns; without it nothing "
               "binds the glass fibres together, so the structure collapses.",
    },
    {
        "id": "ks4-ceramics-polymers-composites-h16",
        "subtopic_slug": "ceramics-polymers-composites",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A tennis racket is advertised as combining the best of both "
                "its materials. Explain what each part of the composite "
                "contributes.",
        "options": [
            "The fibres give the stiffness; the matrix holds them in shape",
            "The fibres give the colour; the matrix gives all the stiffness",
            "The fibres lower the mass; the matrix raises it back again",
            "The fibres conduct the shock away; the matrix stores the energy",
        ],
        "correct_index": 0,
        "why": "The reinforcement supplies strength and stiffness and the "
               "matrix supplies shape and load transfer, so the racket beats "
               "either material used alone.",
    },
    {
        "id": "ks4-ceramics-polymers-composites-h17",
        "subtopic_slug": "ceramics-polymers-composites",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why clay must be wet while it is being shaped but "
                "must then be fired.",
        "options": [
            "Water dissolves the clay, and firing makes it crystallise again",
            "Water lets the particles slide; firing drives it off and fuses "
            "them",
            "Water reacts with the clay, and firing reverses that reaction "
            "again",
            "Water cools the clay down, and firing melts it into a liquid "
            "glass",
        ],
        "correct_index": 1,
        "why": "Water acts as a lubricant so the particles can be moulded, "
               "and firing removes it and bonds the particles into one hard "
               "rigid solid.",
    },
    {
        "id": "ks4-ceramics-polymers-composites-h18",
        "subtopic_slug": "ceramics-polymers-composites",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Evaluate the use of reinforced concrete rather than a steel "
                "frame for a multi-storey car park.",
        "options": [
            "Cheaper and better in a fire, but the structure is far heavier",
            "Cheaper and far lighter, but it fails much sooner in a fire",
            "Dearer and heavier, but it can be taken apart and reused later",
            "Dearer but lighter, so the foundations can be made much smaller",
        ],
        "correct_index": 0,
        "why": "Concrete is cheap and insulates the steel inside it from "
               "fire, at the cost of a much greater mass that the "
               "foundations must carry.",
    },

    # -------------------------------------------------------- standard (top-up)
    {
        "id": "ks4-ceramics-polymers-composites-s19",
        "subtopic_slug": "ceramics-polymers-composites",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "State which form of poly(ethene) has branched chains that "
                "cannot pack closely together.",
        "options": [
            "Low-density poly(ethene)",
            "High-density poly(ethene)",
            "Both forms have branched chains",
            "Neither form has branched chains",
        ],
        "correct_index": 0,
        "why": "LDPE's chains branch, so they cannot pack as closely as "
               "HDPE's straight chains, which is why it is the lower-density "
               "of the two.",
    },
    {
        "id": "ks4-ceramics-polymers-composites-s20",
        "subtopic_slug": "ceramics-polymers-composites",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "State which form of poly(ethene) is chosen for a rigid milk "
                "bottle or a drain pipe.",
        "options": [
            "Low-density poly(ethene), because it is the more flexible of "
            "the two forms of the polymer",
            "High-density poly(ethene), because its closely packed chains "
            "give it more stiffness and strength",
            "Neither, because both forms are far too soft for either use",
            "A thermosetting polymer, because a rigid bottle is not "
            "expected to soften in ordinary use",
        ],
        "correct_index": 1,
        "why": "HDPE's unbranched chains pack tightly, giving the extra "
               "stiffness a bottle or a pipe needs to hold its shape.",
    },
    {
        "id": "ks4-ceramics-polymers-composites-s21",
        "subtopic_slug": "ceramics-polymers-composites",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Suggest why the plastic body of an electrical plug is made "
                "from a thermosetting polymer rather than a thermoplastic.",
        "options": [
            "A thermosetting polymer conducts electricity away safely if a "
            "fault occurs inside the plug",
            "A thermosetting polymer will not soften and lose its shape if "
            "the plug becomes hot",
            "A thermosetting polymer is far cheaper to mould than a "
            "thermoplastic of the same size",
            "A thermosetting polymer can be melted down and reused once the "
            "plug wears out",
        ],
        "correct_index": 1,
        "why": "A fault or overload can make a plug warm, and a "
               "cross-linked polymer keeps its rigid shape and insulating "
               "properties even then, unlike a thermoplastic.",
    },
    {
        "id": "ks4-ceramics-polymers-composites-s22",
        "subtopic_slug": "ceramics-polymers-composites",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Bone is a natural composite material. Name its matrix and "
                "its reinforcement.",
        "options": [
            "Collagen fibres are the matrix; calcium phosphate is the "
            "reinforcement",
            "Calcium phosphate is the matrix; collagen fibres are the "
            "reinforcement",
            "Water is the matrix; calcium phosphate is the reinforcement",
            "Calcium phosphate is both the matrix and the reinforcement",
        ],
        "correct_index": 1,
        "why": "The calcium phosphate forms the continuous mineral matrix, "
               "while the protein collagen fibres are set within it as the "
               "reinforcement.",
    },
    {
        "id": "ks4-ceramics-polymers-composites-s23",
        "subtopic_slug": "ceramics-polymers-composites",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "State the way in which plain, unreinforced concrete is weak.",
        "options": [
            "It is weak under compression, when it is squeezed",
            "It is weak under tension, when it is stretched",
            "It is weak in both compression and tension equally",
            "It has no particular weakness once it has fully set",
        ],
        "correct_index": 1,
        "why": "Concrete resists being squeezed well but cracks easily when "
               "stretched, which is why steel rods are added wherever a "
               "structure will be pulled or bent.",
    },
    {
        "id": "ks4-ceramics-polymers-composites-s24",
        "subtopic_slug": "ceramics-polymers-composites",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain, in terms of structure, why HDPE is denser and "
                "stiffer than LDPE.",
        "options": [
            "HDPE's unbranched chains can pack closely together, while "
            "LDPE's branches keep its chains further apart",
            "HDPE is made of heavier atoms than LDPE, which raises both its "
            "density and its stiffness",
            "HDPE contains cross-links between its chains, while LDPE "
            "has no cross-links of any kind between its own chains",
            "HDPE is cooled more slowly during manufacture, which is what "
            "raises its density",
        ],
        "correct_index": 0,
        "why": "Both are the same chemical repeating unit; it is the "
               "unbranched shape of HDPE's chains that lets them pack more "
               "closely and gives the extra density and stiffness.",
    },
    {
        "id": "ks4-ceramics-polymers-composites-s25",
        "subtopic_slug": "ceramics-polymers-composites",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "A crucible used to melt a metal in a school laboratory is "
                "made from a ceramic. State the property that makes this "
                "suitable.",
        "options": [
            "It is soft, so it cannot scratch the metal being melted inside "
            "it as the temperature rises",
            "It conducts electricity well, which is needed to heat the "
            "metal placed inside it",
            "It has a very high melting point and does not react with the "
            "molten metal",
            "It is transparent, so the level of the molten metal can be "
            "seen from outside",
        ],
        "correct_index": 2,
        "why": "A crucible must survive temperatures far above the metal's "
               "melting point without melting or reacting itself, which is "
               "exactly what a ceramic offers.",
    },
    {
        "id": "ks4-ceramics-polymers-composites-s26",
        "subtopic_slug": "ceramics-polymers-composites",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "State one way in which LDPE and HDPE are similar to each "
                "other, despite their different densities.",
        "options": [
            "Both are thermosetting polymers with cross-links running "
            "between their chains",
            "Both are thermoplastics with no cross-links, so both can be "
            "melted and reshaped",
            "Both are composites made from a matrix and a fibre "
            "reinforcement set inside it",
            "Both are ceramics formed by heating their raw materials "
            "together in a kiln",
        ],
        "correct_index": 1,
        "why": "The branching differs, but neither form has cross-links "
               "between its chains, so both soften on heating and can be "
               "recycled in the same way.",
    },

    # ---------------------------------------------------------- harder (top-up)
    {
        "id": "ks4-ceramics-polymers-composites-h19",
        "subtopic_slug": "ceramics-polymers-composites",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why a bone can bend very slightly under load without "
                "snapping, unlike a plain ceramic object of the same shape.",
        "options": [
            "The collagen fibres let the structure flex a little, while the "
            "mineral matrix still carries most of the load",
            "Bone contains no mineral whatsoever, which is why it does not "
            "behave like an ordinary ceramic material",
            "Bone is far less dense than any ceramic, and low density "
            "generally prevents brittle failure of a structure",
            "Bone is warmed by the body, and warming an ordinary ceramic "
            "usually stops it being so brittle",
        ],
        "correct_index": 0,
        "why": "As in a synthetic composite, the fibrous reinforcement adds "
               "a little give that a plain mineral structure lacks, so the "
               "combination resists snapping under a load that would crack "
               "a brittle ceramic.",
    },
    {
        "id": "ks4-ceramics-polymers-composites-h20",
        "subtopic_slug": "ceramics-polymers-composites",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "An engineer casts a concrete beam with no steel rods "
                "embedded in it, to save money. Predict what happens to the "
                "underside of the beam once it is loaded so that surface is "
                "stretched, and explain why.",
        "options": [
            "It stays intact, because concrete resists tension exactly as "
            "well as it resists compression",
            "It cracks, because plain concrete is weak under the tension "
            "that stretching produces",
            "It is crushed, because the load places the underside under "
            "compression rather than tension",
            "It becomes stronger, because the load compacts the concrete "
            "further as it is stretched",
        ],
        "correct_index": 1,
        "why": "The underside of a loaded beam is stretched, and "
               "unreinforced concrete is weak precisely under that kind of "
               "force, which is why the steel rods are needed there.",
    },
    {
        "id": "ks4-ceramics-polymers-composites-h21",
        "subtopic_slug": "ceramics-polymers-composites",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Compare carbon fibre reinforced plastic with glass "
                "reinforced plastic, and explain why aircraft use the first "
                "and small boats more often use the second.",
        "options": [
            "CFRP is heavier but far cheaper, which suits a boat hull more "
            "than an aircraft",
            "CFRP gives a higher strength for a lower mass but costs far "
            "more, which aircraft can justify and small boats usually "
            "cannot",
            "GRP is stronger than CFRP for the same mass, which is why "
            "aircraft avoid it",
            "The two composites have identical strength and identical cost "
            "in practice, so the choice made is simply a matter of tradition",
        ],
        "correct_index": 1,
        "why": "Carbon fibre gives the best strength-to-mass ratio but at "
               "a high price, which an aircraft's fuel savings can justify "
               "far more easily than a small boat's budget can.",
    },
    {
        "id": "ks4-ceramics-polymers-composites-h22",
        "subtopic_slug": "ceramics-polymers-composites",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Evaluate the claim that a thermosetting polymer is always "
                "the better choice for any high-temperature application.",
        "options": [
            "Sound, because a thermosetting polymer withstands any "
            "temperature a ceramic can withstand",
            "Sound, because a thermoplastic always melts below room "
            "temperature",
            "Unsound: a thermosetting polymer still decomposes at a high "
            "enough temperature, and only a ceramic survives the most "
            "extreme heat",
            "Unsound, because a thermosetting polymer conducts heat too "
            "well to be used near any source of heat",
        ],
        "correct_index": 2,
        "why": "A thermosetting polymer resists softening far better than "
               "a thermoplastic, but it still decomposes eventually, while "
               "a ceramic's much higher melting point is needed for the "
               "most extreme temperatures.",
    },
    {
        "id": "ks4-ceramics-polymers-composites-h23",
        "subtopic_slug": "ceramics-polymers-composites",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A kiln lining must withstand repeated heating to 1200 °C. A "
                "candidate polymer melts at 300 °C and a candidate ceramic "
                "melts at 1800 °C. Explain why only the ceramic is suitable.",
        "options": [
            "The polymer's melting point is far below the working "
            "temperature, while the ceramic's is comfortably above it",
            "The polymer is the cheaper material, so cost alone rules it "
            "out for this use",
            "The ceramic conducts heat away faster, which is the only "
            "property that matters inside a kiln",
            "The polymer would react chemically with the bricks inside the "
            "kiln",
        ],
        "correct_index": 0,
        "why": "A lining has to survive well above its working temperature "
               "with a safety margin, and only the ceramic's melting point "
               "clears 1200 °C by a wide margin.",
    },
    {
        "id": "ks4-ceramics-polymers-composites-h24",
        "subtopic_slug": "ceramics-polymers-composites",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "An engineer proposes replacing the steel rods in reinforced "
                "concrete with rods of a thermosetting polymer, since the "
                "polymer will not rust. Evaluate this proposal.",
        "options": [
            "A good proposal, because rust-resistance is the only property "
            "that matters for reinforcement",
            "A good proposal, because a thermosetting polymer is always "
            "stronger under tension than steel is",
            "A poor proposal: a polymer rod is far less strong and less "
            "stiff under tension than a steel rod of the same size",
            "A poor proposal, because a thermosetting polymer cannot be "
            "shaped into a rod at all",
        ],
        "correct_index": 2,
        "why": "Not rusting is a real advantage, but the rods must still "
               "carry the tension the concrete cannot, and a polymer rod "
               "falls far short of steel's strength and stiffness for that "
               "job.",
    },
    {
        "id": "ks4-ceramics-polymers-composites-h25",
        "subtopic_slug": "ceramics-polymers-composites",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A hybrid composite panel of mass 12 kg is 50% carbon fibre, "
                "20% glass fibre and the remainder resin, all by mass. "
                "Calculate the mass of resin in the panel.",
        "options": [
            "2.4 kg",
            "3.6 kg",
            "6.0 kg",
            "8.4 kg",
        ],
        "correct_index": 1,
        "why": "The resin is 100 − 50 − 20 = 30% of the mass, and "
               "0.30 × 12 kg = 3.6 kg.",
    },
    {
        "id": "ks4-ceramics-polymers-composites-h26",
        "subtopic_slug": "ceramics-polymers-composites",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Evaluate whether unreinforced concrete, with no steel rods "
                "at all, would be suitable for a short, thick pillar that "
                "only ever carries a load pressing straight down on it.",
        "options": [
            "Unsuitable, because concrete is weak under compression, which "
            "is the only force a pillar like this experiences",
            "Suitable, because the load places the pillar under "
            "compression, which plain concrete already resists well",
            "Unsuitable, because concrete can never be used without steel "
            "reinforcement under any circumstances",
            "Suitable, but only if the pillar is also coated with a "
            "polymer to keep out moisture",
        ],
        "correct_index": 1,
        "why": "Steel reinforcement is needed where concrete would be "
               "stretched; a pillar loaded straight down is under "
               "compression throughout, which is exactly the force plain "
               "concrete handles well on its own.",
    },
]
