"""Physics · Energy — the MRB-338 expansion of `thermal-conductivity`.

One leaf only: AQA 8463 §6.1.3, physics only — thermal conductivity as a rate
property, why metals conduct and non-metals do not, the thickness / area /
temperature-difference rule, trapped air, the insulation applications, and RP2.
The original twelve rows in `energy.py` already own the definition, the unit,
the temperature-difference effect, thicker loft insulation, the metal-versus-
wooden spoon, cavity wall foam, a thickening tank jacket, RP2's list of control
variables, 100 mm against 200 mm of loft insulation, the vacuum in a flask, one
bubble-wrap-against-newspaper cooling comparison, and the fibreglass
misconception. This file takes what they leave: the free-electron mechanism and
its absence, classifying real materials, area as a variable, why trapped air
must be trapped, the applications they never reach (double glazing, a duvet, a
jumper, a wetsuit, snow, feathers, a flask stopper, a refrigerator's foam,
cryogenic storage, a foam mat), the misconception set from the wrong side, and
RP2 as a method to run, read and criticise rather than a list to recite.

The weight is FLAT at 14 / 14 / 14 because the CONTENT is flat. This subtopic
is triple-only and carries no equation a pupil substitutes into, so there is no
bank of one-step arithmetic to fill an `easier` band with; what it has instead
is a long list of real materials and real objects, each of which can be
recalled and classified at `easier`, explained at `standard` and compared or
criticised at `harder`. Every application in the list genuinely supports all
three rungs, so no band has to be padded and none is short.

Numbers here are conductivity-over-thickness and area-over-thickness ratios,
and rates of cooling in degrees C per minute. There is deliberately no mass, no
specific heat capacity and no m c change-in-temperature anywhere: that is
`energy-changes-in-systems`, and it would be that leaf's question wearing this
leaf's slug. Lubrication and streamlining are likewise absent — they belong to
`energy-transfers-in-a-system`. What this leaf owns is the MATERIAL and the
MECHANISM.
"""

TOPIC = "energy"
SUBJECT = "physics"

QUESTIONS = [
    # ══ easier · e05–e18 ═════════════════════════════════════════════════
    # Classifying real materials, the free-electron mechanism and its
    # absence, area and thickness as variables, trapped air, the direction of
    # transfer, and RP2's two measured variables.
    {
        "id": "ks4-thermal-conductivity-e05",
        "subtopic_slug": "thermal-conductivity",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State which of these materials transfers thermal energy by "
                "conduction the fastest.",
        "options": [
            "Copper, because it is a metal and metals have very high thermal "
            "conductivities",
            "Polystyrene, because the gas pockets inside it hand energy on "
            "from one to the next rapidly",
            "Dry wood, because its fibres are packed tightly enough to pass "
            "energy quickly along their length",
            "Wool, because the air held between its fibres conducts better "
            "than any metal does",
        ],
        "correct_index": 0,
        "why": "Metals have far higher thermal conductivities than wood, wool "
               "or polystyrene, so energy passes through copper fastest for "
               "the same thickness.",
    },
    {
        "id": "ks4-thermal-conductivity-e06",
        "subtopic_slug": "thermal-conductivity",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State the reason metals such as copper and aluminium conduct "
                "thermal energy so well.",
        "options": [
            "They are denser than other materials, so more mass is there to "
            "hold the energy",
            "Their surfaces are shiny, so they take in more thermal radiation",
            "Their particles sit further apart, so energy crosses the gaps "
            "between them freely",
            "They contain free electrons, which carry energy through the "
            "metal quickly",
        ],
        "correct_index": 3,
        "why": "Free electrons move throughout a metal and carry energy with "
               "them, which is a much faster route than vibration alone.",
    },
    {
        "id": "ks4-thermal-conductivity-e07",
        "subtopic_slug": "thermal-conductivity",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State why a material such as wood or polystyrene conducts "
                "thermal energy poorly.",
        "options": [
            "It is colder than a metal to begin with, so the energy inside it "
            "has further to travel",
            "It reflects thermal energy away from its surface before any of "
            "it can enter the material",
            "It has no free electrons, so energy passes only by particles "
            "vibrating against each other",
            "It has no particles inside it, so there is nothing there able to "
            "pass the energy along",
        ],
        "correct_index": 2,
        "why": "Without free electrons the only route left is vibration "
               "handed on from particle to particle, which is slow.",
    },
    {
        "id": "ks4-thermal-conductivity-e08",
        "subtopic_slug": "thermal-conductivity",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Name the material in this list that would make the best "
                "thermal insulator for a loft.",
        "options": [
            "Aluminium sheeting, because a smooth metal surface refuses to "
            "let energy through it",
            "Fibreglass, because it is a poor conductor and holds still air "
            "between its fibres",
            "Steel mesh, because the gaps in the mesh leave the energy "
            "nowhere to travel through",
            "Copper foil, because copper carries energy sideways across the "
            "loft instead of upwards",
        ],
        "correct_index": 1,
        "why": "Fibreglass combines a low conductivity of its own with "
               "pockets of still air, which is why it is the standard loft "
               "insulator.",
    },
    {
        "id": "ks4-thermal-conductivity-e09",
        "subtopic_slug": "thermal-conductivity",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Copper has a thermal conductivity of about 400 W/m K and "
                "glass about 1 W/m K. State which of them transfers energy "
                "faster through a layer of the same thickness.",
        "options": [
            "Glass, because a smaller conductivity means less resistance to "
            "the energy",
            "Copper, because a higher thermal conductivity means a faster "
            "transfer",
            "They transfer at the same rate, since the layers are equally "
            "thick",
            "Glass, because it is transparent and lets the energy through",
        ],
        "correct_index": 1,
        "why": "Thermal conductivity is a rate property, so the material with "
               "the larger value transfers faster for the same thickness and "
               "temperature difference.",
    },
    {
        "id": "ks4-thermal-conductivity-e10",
        "subtopic_slug": "thermal-conductivity",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State the effect on the rate of energy transfer through a "
                "window of fitting a larger pane of the same glass at the "
                "same thickness.",
        "options": [
            "The rate rises, because a larger area gives a wider path for "
            "conduction",
            "The rate falls, because the energy is spread over more square "
            "metres",
            "The rate is unchanged, because the glass used and its thickness "
            "are the same",
            "The rate drops to nothing, because a large pane cools and stops "
            "conducting",
        ],
        "correct_index": 0,
        "why": "Rate of transfer rises with area, so a bigger window of the "
               "same glass and thickness loses energy faster.",
    },
    {
        "id": "ks4-thermal-conductivity-e11",
        "subtopic_slug": "thermal-conductivity",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "A saucepan has a metal base and a plastic handle. State the "
                "reason the handle is made of plastic.",
        "options": [
            "Plastic has the higher conductivity, so it carries energy from "
            "the hand",
            "Plastic cannot be warmed by a pan, so the handle stays cold",
            "Plastic weighs less than metal, and light things stay cool",
            "Plastic is a poor conductor, so the handle stays cool enough to "
            "hold",
        ],
        "correct_index": 3,
        "why": "The base needs a high conductivity to pass energy to the "
               "food, while the handle needs a low one so little energy "
               "reaches the hand.",
    },
    {
        "id": "ks4-thermal-conductivity-e12",
        "subtopic_slug": "thermal-conductivity",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State why trapped air is one of the best thermal insulators "
                "available.",
        "options": [
            "Air is a poor conductor, and trapping it also stops convection "
            "carrying energy away",
            "Air is a poor conductor, but only once it has been warmed up to "
            "the temperature of the room",
            "Air carries energy well, so trapping it locks that energy inside "
            "the pockets where it sits",
            "Air is a poor conductor, and it also stops thermal radiation "
            "from crossing the gap",
        ],
        "correct_index": 0,
        "why": "Trapping does two jobs at once: the air itself conducts "
               "poorly, and holding it still removes the convection route as "
               "well.",
    },
    {
        "id": "ks4-thermal-conductivity-e13",
        "subtopic_slug": "thermal-conductivity",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "In the required practical on thermal insulators, beakers of "
                "hot water are wrapped in different materials. State the "
                "independent variable.",
        "options": [
            "The temperature of the water at the start",
            "The time each beaker is left to cool for",
            "The type of material used as the wrapping",
            "The temperature the water has fallen to",
        ],
        "correct_index": 2,
        "why": "The independent variable is the one deliberately changed "
               "between beakers, which here is the insulating material.",
    },
    {
        "id": "ks4-thermal-conductivity-e14",
        "subtopic_slug": "thermal-conductivity",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State the effect on a woollen jumper's ability to insulate "
                "when it becomes soaked through with water.",
        "options": [
            "It insulates better, because the water soaked into the fibres "
            "stores a great deal of energy",
            "It insulates just as well, because the wool fibres themselves "
            "are what block the transfer",
            "It insulates better, because a layer of water on the outside "
            "seals the jumper against the cold",
            "It insulates far less well, because water fills the spaces that "
            "held the trapped air",
        ],
        "correct_index": 3,
        "why": "Wool works because of the air trapped between its fibres. "
               "Water conducts far better than air does, so once it has "
               "driven the air out the jumper conducts much faster.",
    },
    {
        "id": "ks4-thermal-conductivity-e15",
        "subtopic_slug": "thermal-conductivity",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State what a thermal insulator does to an unwanted energy "
                "transfer.",
        "options": [
            "It stops the transfer completely, if the layer is thick enough",
            "It reverses the transfer, sending the energy back",
            "It removes the temperature difference, so no energy moves",
            "It slows the transfer down, and never stops it completely",
        ],
        "correct_index": 3,
        "why": "Every material conducts to some extent, so insulation only "
               "ever reduces the rate of a transfer rather than ending it.",
    },
    {
        "id": "ks4-thermal-conductivity-e16",
        "subtopic_slug": "thermal-conductivity",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State the direction in which energy is transferred by "
                "conduction through the wall of a warm house on a cold day.",
        "options": [
            "From the cold air outside inwards into the warmer rooms of the "
            "house",
            "In both directions at once and equally, so the wall itself stays "
            "at a single temperature",
            "From the warm rooms inside out to the colder air outside, and "
            "never the reverse",
            "Sideways along the wall, rather than through it from the inner "
            "face to the outer one",
        ],
        "correct_index": 2,
        "why": "Conduction carries energy from the hotter place to the colder "
               "one, so the transfer is outwards whenever the house is warmer "
               "than the air.",
    },
    {
        "id": "ks4-thermal-conductivity-e17",
        "subtopic_slug": "thermal-conductivity",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "In a standard double-glazed window, name what is sealed in "
                "the narrow gap between the two panes of glass.",
        "options": [
            "A thin sheet of copper, which spreads the energy out",
            "Trapped air, which conducts thermal energy poorly",
            "A layer of water, which soaks up the energy",
            "A block of solid glass, which doubles the path",
        ],
        "correct_index": 1,
        "why": "The gap holds air, whose conductivity is far lower than "
               "glass, and sealing it keeps the air still.",
    },
    {
        "id": "ks4-thermal-conductivity-e18",
        "subtopic_slug": "thermal-conductivity",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Two mugs are made of the same pottery, one with a thick wall "
                "and one with a thin wall. State which keeps a hot drink warm "
                "for longer.",
        "options": [
            "The thin-walled mug, because there is less pottery there to warm "
            "up",
            "Neither, because the two mugs have been made of exactly the same "
            "pottery",
            "The thick-walled mug, because a greater thickness slows the "
            "transfer",
            "The thin-walled mug, because a thin wall holds the drink's "
            "energy in place",
        ],
        "correct_index": 2,
        "why": "For the same material and temperature difference, a greater "
               "thickness gives a slower rate of transfer.",
    },
    # ══ standard · s05–s18 ═══════════════════════════════════════════════
    # The applications, each one explained: why a material feels cold, why
    # trapped air works, and one RP2 control and one RP2 reading.
    {
        "id": "ks4-thermal-conductivity-s05",
        "subtopic_slug": "thermal-conductivity",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "A bathroom has a tiled area and a carpeted area, both at the "
                "same temperature. Explain why the tiles feel colder "
                "underfoot.",
        "options": [
            "The tiles are colder than the carpet, because a hard material "
            "always sits at a lower temperature",
            "The tiles conduct energy away from the skin faster, so the foot "
            "cools more quickly",
            "The tiles hold more energy in every kilogram, so they draw the "
            "warmth out of the foot",
            "The carpet gives out energy of its own, and that is what warms "
            "the foot standing on it",
        ],
        "correct_index": 1,
        "why": "Feeling cold is about how fast energy leaves the skin, and "
               "tile conducts far faster than carpet at the same temperature.",
    },
    {
        "id": "ks4-thermal-conductivity-s06",
        "subtopic_slug": "thermal-conductivity",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain how a thick duvet keeps a person warm on a cold "
                "night.",
        "options": [
            "The duvet produces energy of its own, which it then passes down "
            "into the person beneath it",
            "The duvet is warmer than the person, so energy is transferred "
            "out of it into the body",
            "The duvet traps air, which conducts poorly, so the body's energy "
            "escapes only slowly",
            "The duvet removes the temperature difference between the person "
            "and the cold air of the room",
        ],
        "correct_index": 2,
        "why": "The body supplies the energy; the duvet's trapped air simply "
               "slows the rate at which that energy reaches the room.",
    },
    {
        "id": "ks4-thermal-conductivity-s07",
        "subtopic_slug": "thermal-conductivity",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "A bottle of chilled water is wrapped in a thick duvet and "
                "left standing in a warm room. Explain what happens to the "
                "water.",
        "options": [
            "It warms up, but more slowly than it would unwrapped, because "
            "the duvet only slows the transfer",
            "It warms up faster than it would unwrapped, because a duvet is "
            "made to keep its contents warm",
            "It stays at exactly the temperature it started at, because the "
            "duvet seals the energy out",
            "It cools down further, because a duvet always drives energy out "
            "of whatever it is wrapped around",
        ],
        "correct_index": 0,
        "why": "Insulation works the same way in both directions: energy "
               "still passes from the warm room into the cold water, just "
               "more slowly.",
    },
    {
        "id": "ks4-thermal-conductivity-s08",
        "subtopic_slug": "thermal-conductivity",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why the sealed gap between the two panes of a "
                "double-glazed window is only a few millimetres wide rather "
                "than several centimetres.",
        "options": [
            "A narrow gap holds less of the sealed gas, so there is less "
            "material in the window able to conduct",
            "A narrow gap keeps the window lighter, and it is that lower "
            "weight which reduces the transfer",
            "A narrow gap lets the two panes touch, so the energy is shared "
            "evenly between the pair of them",
            "In a wide gap the sealed gas would circulate, so convection "
            "would carry energy across it",
        ],
        "correct_index": 3,
        "why": "A gas is a poor conductor, but given room to circulate it "
               "becomes a good carrier of energy by convection, so the gap is "
               "kept too narrow for that.",
    },
    {
        "id": "ks4-thermal-conductivity-s09",
        "subtopic_slug": "thermal-conductivity",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain how a woollen jumper reduces the energy a person "
                "loses on a cold day.",
        "options": [
            "The wool fibres are excellent conductors, spreading the energy "
            "evenly",
            "The jumper warms the air of the room around the person until the "
            "room is no longer cold",
            "The fibres hold still air against the body, and still air is a "
            "very poor conductor",
            "The jumper seals the skin over completely, so the energy the "
            "body releases has nowhere to go",
        ],
        "correct_index": 2,
        "why": "It is the still air held between the fibres, rather than the "
               "wool itself, that does most of the insulating.",
    },
    {
        "id": "ks4-thermal-conductivity-s10",
        "subtopic_slug": "thermal-conductivity",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "On a cold morning a metal bench feels much colder to sit on "
                "than a wooden one beside it, although both are at the same "
                "temperature. Explain why.",
        "options": [
            "Metal has a much higher thermal conductivity, so it draws energy "
            "from the body faster",
            "Metal sits at a lower temperature than wood on a cold morning, "
            "whatever a thermometer may read",
            "Metal holds far more energy in every kilogram, so it needs more "
            "energy from the body to warm",
            "Metal gives out cold into the body, whereas wood has no cold of "
            "its own to give out",
        ],
        "correct_index": 0,
        "why": "The skin judges the rate at which energy leaves it, and metal "
               "conducts that energy away far faster than wood does.",
    },
    {
        "id": "ks4-thermal-conductivity-s11",
        "subtopic_slug": "thermal-conductivity",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "In an investigation of insulating materials, explain why the "
                "same volume of hot water must be used in every beaker.",
        "options": [
            "So that the water in each beaker begins at exactly the same "
            "temperature as all the others",
            "Because a larger volume of water cools more slowly, which would "
            "hide the material's effect",
            "So that each of the beakers can then be wrapped in the very same "
            "thickness of material",
            "Because water of a different volume has a different thermal "
            "conductivity from the rest",
        ],
        "correct_index": 1,
        "why": "Volume affects the rate of cooling on its own, so leaving it "
               "free would confuse the comparison between the materials.",
    },
    {
        "id": "ks4-thermal-conductivity-s12",
        "subtopic_slug": "thermal-conductivity",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Two identical beakers of hot water are wrapped, one in wool "
                "and one in cotton. The wool-wrapped water takes 15 minutes "
                "to fall by 20 degrees C; the cotton-wrapped water takes 9 "
                "minutes to fall by the same 20 degrees C. Determine which "
                "material is the better insulator.",
        "options": [
            "Cotton, because it reached the 20 degrees C fall in the shorter "
            "of the two times",
            "Neither, because the water in both of the beakers fell by the "
            "very same 20 degrees C",
            "Cotton, because a quicker fall in temperature is a sign that "
            "energy is leaving more slowly",
            "Wool, because it took longer for the same fall, so energy left "
            "more slowly",
        ],
        "correct_index": 3,
        "why": "The better insulator gives the slower rate of cooling: about "
               "1.3 degrees C per minute for the wool against about 2.2 for "
               "the cotton.",
    },
    {
        "id": "ks4-thermal-conductivity-s13",
        "subtopic_slug": "thermal-conductivity",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "The walls of a refrigerator are filled with a foam holding "
                "many tiny sealed pockets of gas. Explain why this is a "
                "better choice than filling them with solid plastic.",
        "options": [
            "Solid plastic would be heavier, and a heavier wall always "
            "transfers energy more quickly than a light one",
            "Solid plastic would conduct nothing at all, so the food stored "
            "inside would end up frozen solid",
            "Gas conducts far worse than solid plastic, and sealing it in "
            "pockets stops it circulating",
            "The pockets of gas send the energy of the kitchen back out again "
            "before it can enter the wall",
        ],
        "correct_index": 2,
        "why": "The gas is the poor conductor, and dividing it into small "
               "sealed pockets removes the convection route that an open "
               "space would allow.",
    },
    {
        "id": "ks4-thermal-conductivity-s14",
        "subtopic_slug": "thermal-conductivity",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "On a freezing day a small bird fluffs up its feathers until "
                "it looks almost round. Explain how this helps it to stay "
                "warm.",
        "options": [
            "Fluffing traps a thicker layer of air in the feathers, and air "
            "conducts very poorly",
            "Fluffing makes the bird larger, and a larger surface gives off "
            "less energy",
            "Fluffing warms the feathers, which pass that energy back inwards",
            "Fluffing presses the feathers flat together, sealing the skin so "
            "that no energy leaves it",
        ],
        "correct_index": 0,
        "why": "A thicker layer of trapped air between the feathers means a "
               "slower rate of transfer from the bird's body to the cold air "
               "outside.",
    },
    {
        "id": "ks4-thermal-conductivity-s15",
        "subtopic_slug": "thermal-conductivity",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "The stopper of a vacuum flask is made of plastic rather than "
                "metal. Explain the reason for this choice.",
        "options": [
            "Plastic weighs less than metal, and a lighter stopper lets less "
            "energy out of the drink below it",
            "Plastic sends the energy of the drink back down into the liquid "
            "instead of letting it rise",
            "Plastic starts off warmer than metal, so less energy is needed "
            "to bring the stopper up to temperature",
            "Plastic conducts poorly, so little energy is carried out through "
            "the neck of the flask",
        ],
        "correct_index": 3,
        "why": "A metal stopper would give the energy a high-conductivity "
               "path straight out of the neck, undoing the work of the "
               "vacuum in the walls.",
    },
    {
        "id": "ks4-thermal-conductivity-s16",
        "subtopic_slug": "thermal-conductivity",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "A wetsuit is made of neoprene, a rubber holding thousands of "
                "tiny trapped gas bubbles. Explain how it keeps a swimmer "
                "warm in cold water.",
        "options": [
            "The rubber gives out energy as it flexes, and that warms the "
            "body",
            "The trapped gas conducts poorly, so energy leaves the swimmer's "
            "body far more slowly",
            "The bubbles make the suit float, so a swimmer held at the "
            "surface stops losing energy",
            "The rubber conducts better than skin, so it carries the cold of "
            "the water away sideways",
        ],
        "correct_index": 1,
        "why": "The gas in the bubbles has a very low thermal conductivity, "
               "so the suit slows the transfer from the swimmer to the water "
               "around them.",
    },
    {
        "id": "ks4-thermal-conductivity-s17",
        "subtopic_slug": "thermal-conductivity",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Mountain rescuers report that a shelter dug into deep snow "
                "is far warmer inside than the open air. Explain why snow is "
                "a good insulator.",
        "options": [
            "Snow is made of ice, and ice conducts energy more poorly than "
            "any other solid material does",
            "Snow is white, so it sends the energy of the person sheltering "
            "straight back towards their body",
            "Snow is mostly air trapped between ice crystals, and trapped air "
            "conducts very poorly",
            "Snow is colder than the air outside, so energy is drawn from the "
            "outside into the shelter",
        ],
        "correct_index": 2,
        "why": "Fresh snow is largely air held still between crystals, which "
               "gives it a far lower conductivity than solid ice.",
    },
    {
        "id": "ks4-thermal-conductivity-s18",
        "subtopic_slug": "thermal-conductivity",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "A homeowner stacks heavy boxes on top of the loft "
                "insulation, squashing it flat. Explain the effect on the "
                "energy transferred through the roof.",
        "options": [
            "More is transferred, because squashing forces out the trapped "
            "air and thins the layer",
            "Less is transferred, because squashing packs the fibres and "
            "seals the gaps",
            "The same is transferred, because exactly the same mass of "
            "insulating material is there",
            "None is transferred, because the stacked boxes add a further "
            "insulating layer above the fibres",
        ],
        "correct_index": 0,
        "why": "Crushing the fibres removes most of the still air and reduces "
               "the thickness, and both changes raise the rate of transfer.",
    },
    # ══ harder · h05–h18 ═════════════════════════════════════════════════
    # Multi-variable ratios, two-design comparisons, evaluations of claims,
    # unfamiliar contexts, and RP2 criticised rather than recited.
    {
        "id": "ks4-thermal-conductivity-h05",
        "subtopic_slug": "thermal-conductivity",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Wall X is 0.20 m thick and made of a material of thermal "
                "conductivity 1.0 W/m K. Wall Y is 0.10 m thick with a "
                "conductivity of 0.040 W/m K. Determine which transfers "
                "energy faster for the same area and temperature difference.",
        "options": [
            "Wall Y, because it is the thinner of the two and a thinner wall "
            "always transfers energy faster",
            "They transfer at equal rates, because Y makes up in thinness "
            "exactly what X gains in conductivity",
            "Wall X, because its conductivity divided by its thickness is far "
            "the larger of the two",
            "Wall Y, because its conductivity and its thickness are both the "
            "smaller of the two numbers",
        ],
        "correct_index": 2,
        "why": "Rate depends on conductivity divided by thickness: X gives "
               "1.0 / 0.20 = 5.0 and Y gives 0.040 / 0.10 = 0.40, so X "
               "transfers energy about twelve times faster.",
    },
    {
        "id": "ks4-thermal-conductivity-h06",
        "subtopic_slug": "thermal-conductivity",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Two identical refrigerators each hold their inside at 4 "
                "degrees C. One stands in a garage at 30 degrees C and the "
                "other in a kitchen at 18 degrees C. Predict which has more "
                "energy entering it each second.",
        "options": [
            "The one in the garage, because the temperature difference across "
            "its walls is larger",
            "The one in the kitchen, because a cooler room drives energy "
            "inwards faster",
            "Both by the same amount, because the two appliances are "
            "identical and set to 4 degrees C",
            "Neither, because an insulated wall stops energy entering however "
            "warm the outside room is",
        ],
        "correct_index": 0,
        "why": "A 26 degrees C difference drives a faster transfer than a 14 "
               "degrees C one through the same walls, so the garage "
               "refrigerator gains energy faster.",
    },
    {
        "id": "ks4-thermal-conductivity-h07",
        "subtopic_slug": "thermal-conductivity",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Evaluate the claim that a material could be developed which "
                "stops conduction through a wall completely.",
        "options": [
            "The claim is right, because a thick enough layer of any ordinary "
            "insulator will stop conduction",
            "The claim is right, because a sheet of foil turns the vibrating "
            "particles back into the wall before they can hand energy on",
            "The claim is wrong, because every material is found to conduct "
            "better as it is made thicker",
            "The claim is wrong, because every material conducts to some "
            "extent, so a transfer is always slowed and never stopped",
        ],
        "correct_index": 3,
        "why": "There is no perfect insulator: adding material lowers the "
               "rate of transfer but can never bring it to zero.",
    },
    {
        "id": "ks4-thermal-conductivity-h08",
        "subtopic_slug": "thermal-conductivity",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Compare a 100 mm layer of fibreglass with a 100 mm slab of "
                "solid glass as a loft insulator.",
        "options": [
            "The glass slab is better, because a solid material leaves no "
            "gaps for the energy to travel through",
            "The fibreglass is better, because the still air between its "
            "fibres conducts far worse than glass",
            "They are equally good, because both are made of glass and both "
            "are laid at the very same thickness",
            "The glass slab is better, because a heavier layer holds the "
            "energy back more strongly than a light one",
        ],
        "correct_index": 1,
        "why": "Glass conducts at about 1 W/m K, while the still air trapped "
               "in fibreglass is some forty times lower, so the fibrous layer "
               "wins at equal thickness.",
    },
    {
        "id": "ks4-thermal-conductivity-h09",
        "subtopic_slug": "thermal-conductivity",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A student compares insulators but uses a 250 cm3 beaker for "
                "one material and a 100 cm3 beaker for another, filling each "
                "to the brim. Identify the main problem with the "
                "investigation.",
        "options": [
            "Nothing is wrong, because each beaker was filled right up and so "
            "neither of them was short of water",
            "The thermometer reads differently in the two beakers, because "
            "the two of them are of different widths",
            "The volume and the surface area both change, so the difference "
            "in cooling is not only due to the material",
            "The larger beaker holds its water at a higher temperature, "
            "because more water means more energy in it",
        ],
        "correct_index": 2,
        "why": "Two variables have been left free alongside the material, so "
               "no conclusion about the materials can be drawn from the "
               "cooling times.",
    },
    {
        "id": "ks4-thermal-conductivity-h10",
        "subtopic_slug": "thermal-conductivity",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "In an insulation test a student covers one beaker with a lid "
                "and leaves the rest open. Explain why the comparison is no "
                "longer fair.",
        "options": [
            "The covered beaker also loses less by evaporation, so the "
            "wrapping is not the only difference between them",
            "The covered beaker cannot be reached by a thermometer, so no "
            "reading can be taken from that one at all",
            "The lid conducts energy down into the water, so the covered "
            "beaker finishes up the warmer of the two",
            "A lid makes no difference to cooling, so the only unfairness is "
            "the time spent fitting it to the beaker",
        ],
        "correct_index": 0,
        "why": "A lid closes off evaporation and convection from the water "
               "surface, so that beaker differs from the others in more than "
               "its wrapping.",
    },
    {
        "id": "ks4-thermal-conductivity-h11",
        "subtopic_slug": "thermal-conductivity",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A first aider must keep a casualty lying outdoors warm. "
                "Evaluate lying them on bare concrete against lying them on a "
                "thick foam mat.",
        "options": [
            "Concrete is better, because a solid surface holds a person's own "
            "energy against their body",
            "The two are equally good, because it is the blanket over the "
            "casualty that matters and not the ground",
            "Concrete is better, because its large surface spreads the "
            "casualty's energy out thinly and slowly",
            "The mat is better, because concrete conducts energy away from "
            "the body far faster",
        ],
        "correct_index": 3,
        "why": "Concrete has a much higher conductivity than foam and is in "
               "contact over a large area, so it drains energy from the body "
               "quickly.",
    },
    {
        "id": "ks4-thermal-conductivity-h12",
        "subtopic_slug": "thermal-conductivity",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Pane A has an area of 1.5 m2 and is 4.0 mm thick. Pane B has "
                "an area of 3.0 m2 and is 8.0 mm thick. Both are the same "
                "glass with the same temperature difference across them. "
                "Determine which transfers energy faster.",
        "options": [
            "Pane B, because it has the larger area, and area is the only "
            "thing that decides the rate",
            "Neither, because doubling both the area and the thickness leaves "
            "the rate unchanged",
            "Pane A, because it is the thinner of the two, and thickness is "
            "what decides the rate of transfer",
            "Pane B, because both its area and its thickness are larger, and "
            "larger values give a faster transfer",
        ],
        "correct_index": 1,
        "why": "Rate rises with area and falls with thickness, so 1.5 / 4.0 "
               "and 3.0 / 8.0 both come to 0.375 and the two rates are equal.",
    },
    {
        "id": "ks4-thermal-conductivity-h13",
        "subtopic_slug": "thermal-conductivity",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A loft already has 100 mm of insulation. Evaluate the claim "
                "that adding a further 200 mm of the same material will save "
                "three times as much energy as the first 100 mm did.",
        "options": [
            "The claim is right, because three times the thickness of "
            "insulation must save three times the energy",
            "The claim is right, because each extra layer of fibres traps "
            "three times as much air as the layer below it",
            "The claim is wrong, because the rate of transfer is already much "
            "reduced, so the extra layers save less than the first did",
            "The claim is wrong, because insulation thicker than 100 mm makes "
            "no difference to the transfer at all",
        ],
        "correct_index": 2,
        "why": "The rate falls roughly in proportion to one over the "
               "thickness, so the first 100 mm halves the loss while the next "
               "200 mm removes only part of what is left.",
    },
    {
        "id": "ks4-thermal-conductivity-h14",
        "subtopic_slug": "thermal-conductivity",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A student concludes that wool is the best insulator because "
                "its beaker stayed hottest, but the wool was wrapped twice as "
                "thickly as every other material. Evaluate the conclusion.",
        "options": [
            "It is not safe, because the extra thickness could explain the "
            "slower cooling on its own",
            "It is safe, because wool would have won by the very same margin "
            "at any thickness at all",
            "It is not safe, because thickness has no effect on cooling and "
            "so the wool result must be an anomaly",
            "It is safe, because thickness is the dependent variable and is "
            "meant to differ from material to material",
        ],
        "correct_index": 0,
        "why": "Thickness affects the rate of transfer by itself, so with it "
               "left uncontrolled the result cannot be credited to the wool.",
    },
    {
        "id": "ks4-thermal-conductivity-h15",
        "subtopic_slug": "thermal-conductivity",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Liquid nitrogen at -196 degrees C is stored in a laboratory "
                "at 20 degrees C. Explain why its vessel needs extremely good "
                "insulation.",
        "options": [
            "To stop the cold of the nitrogen escaping into the laboratory "
            "and chilling the people working there",
            "Because the very large temperature difference drives a fast "
            "transfer into the nitrogen, boiling it away",
            "Because nitrogen has a very high thermal conductivity and would "
            "carry energy out through the walls of the vessel",
            "Because a cold liquid transfers energy outwards faster than a "
            "hot one, so more of it has to be held back",
        ],
        "correct_index": 1,
        "why": "A difference of 216 degrees C drives a rapid transfer inwards, "
               "and any energy arriving boils more of the liquid away.",
    },
    {
        "id": "ks4-thermal-conductivity-h16",
        "subtopic_slug": "thermal-conductivity",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Predict whether two thin jumpers worn together or one thick "
                "jumper of the same total thickness keeps a walker warmer, "
                "and explain your answer.",
        "options": [
            "The single thick jumper, because one unbroken layer leaves no "
            "seams to leak through",
            "Either of them, because the same total thickness slows the "
            "transfer equally",
            "The single thick jumper, because two thin layers squeeze the "
            "trapped air out",
            "The two thin jumpers, because a further layer of air is trapped "
            "between them",
        ],
        "correct_index": 3,
        "why": "Layering adds an extra pocket of still air between the "
               "garments, and still air conducts more poorly than the fibre "
               "itself.",
    },
    {
        "id": "ks4-thermal-conductivity-h17",
        "subtopic_slug": "thermal-conductivity",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A beaker of hot water is left to cool in a cool room. "
                "Predict how the number of degrees it falls in each "
                "successive minute changes, and explain why.",
        "options": [
            "The fall gets smaller each minute, because the temperature "
            "difference driving the transfer is always shrinking",
            "The fall gets larger each minute, because the water has less "
            "energy left in it and so parts with it faster",
            "The fall stays the same each minute, because neither the beaker "
            "nor the room has been changed in any way",
            "The fall gets smaller each minute, because the cooling water "
            "gradually turns into a better insulator itself",
        ],
        "correct_index": 0,
        "why": "Rate of transfer depends on the temperature difference, which "
               "shrinks as the water cools, so each minute costs fewer "
               "degrees than the one before.",
    },
    {
        "id": "ks4-thermal-conductivity-h18",
        "subtopic_slug": "thermal-conductivity",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A chef claims that a copper-based pan heats food more evenly "
                "than a steel-based one of the same thickness. Evaluate the "
                "claim.",
        "options": [
            "The claim is wrong, because the material of a pan's base plays "
            "no part in how energy reaches the food",
            "The claim is wrong, because steel is the better conductor of the "
            "two and so spreads the energy more evenly",
            "The claim is right, because copper's much higher conductivity "
            "spreads energy across the base faster",
            "The claim is right, because copper holds far more energy in "
            "every kilogram than steel does",
        ],
        "correct_index": 2,
        "why": "Copper conducts at roughly 400 W/m K against about 50 for "
               "steel, so hot spots from the burner even out across a copper "
               "base much faster.",
    },
]
