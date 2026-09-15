"""Physics · Energy — the MRB-338 expansion of `energy-transfers-in-a-system`.

One leaf only: AQA 8463 §4.1.2, dissipation and the reduction of unwanted
energy transfers. The original twelve rows in `energy.py` name dissipation,
do one wasted-energy subtraction, and take one example each of streamlining,
lubrication, thicker conductors and insulation. This file takes the four
methods as a SET — each one matched to the specific unwanted transfer it
reduces, and each one evaluated against a context where it is the wrong
choice — together with where the waste actually finishes in a named machine,
sound as an output that is useful in one device and wasted in another, and
why dissipated energy cannot be gathered back.

The weight follows the CONTENT. `easier` stays at eight because recall here is
four method names, one definition and one subtraction, and asking those a
seventh way would be the same question. The demand lives in `standard`, where
a method has to be matched to a machine and the cause explained, and in
`harder`, where two methods compete for one context and the pupil has to say
which earns its money — so that is where the twenty-two-row bands sit.

⚠️ Seam with `thermal-conductivity`: insulation appears here only as a METHOD
and as the transfer it reduces. Why one material conducts better than another,
the free-electron mechanism, the thickness rule and RP2 belong to that leaf.
⚠️ Seam with `efficiency`: waste is counted here in joules only. No ratio, no
percentage and no Sankey appears in this file.
"""

TOPIC = "energy"
SUBJECT = "physics"

QUESTIONS = [
    # ══ easier · e05–e12 ═════════════════════════════════════════════════
    # The four method names, the definition of wasted energy, one subtraction,
    # sound as an unwanted output, and why the waste cannot be recovered.
    {
        "id": "ks4-energy-transfers-in-a-system-e05",
        "subtopic_slug": "energy-transfers-in-a-system",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the method used to reduce the energy wasted by friction "
                "between the moving parts of a machine.",
        "options": [
            "Streamlining",
            "Insulation",
            "Lubrication",
            "Conduction",
        ],
        "correct_index": 2,
        "why": "Lubrication puts a film of oil or grease between two surfaces "
               "so they slide rather than grip, and less energy is dissipated "
               "by heating.",
    },
    {
        "id": "ks4-energy-transfers-in-a-system-e06",
        "subtopic_slug": "energy-transfers-in-a-system",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the method used to reduce the energy a moving vehicle "
                "wastes in pushing air out of its way.",
        "options": [
            "Streamlining",
            "Lubrication",
            "Lagging",
            "Earthing",
        ],
        "correct_index": 0,
        "why": "Streamlining shapes a vehicle so the air flows smoothly "
               "around it, so less work is done against air resistance.",
    },
    {
        "id": "ks4-energy-transfers-in-a-system-e07",
        "subtopic_slug": "energy-transfers-in-a-system",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the method used to reduce the unwanted energy transfer "
                "from the warm inside of a house to the cold air outside.",
        "options": [
            "Lubrication",
            "Streamlining",
            "Earthing",
            "Insulation",
        ],
        "correct_index": 3,
        "why": "Insulation surrounds a warm space with a poor conductor, so "
               "energy is transferred out of it more slowly.",
    },
    {
        "id": "ks4-energy-transfers-in-a-system-e08",
        "subtopic_slug": "energy-transfers-in-a-system",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State what is meant by the wasted energy of a device.",
        "options": [
            "The energy supplied to it, subtracted from the useful amount that "
            "it manages to deliver",
            "The total energy supplied to it, minus the energy it transfers "
            "usefully",
            "The energy it does not need, which stays inside it until it is "
            "switched off",
            "The energy that passes through it without being transferred to "
            "anything at all",
        ],
        "correct_index": 1,
        "why": "Everything supplied either does the job or is dissipated, so "
               "the waste is the input with the useful output taken away.",
    },
    {
        "id": "ks4-energy-transfers-in-a-system-e09",
        "subtopic_slug": "energy-transfers-in-a-system",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "A food mixer is supplied with 520 J and transfers 340 J "
                "usefully to the blades. Calculate the energy wasted.",
        "options": [
            "860 J",
            "340 J",
            "180 J",
            "520 J",
        ],
        "correct_index": 2,
        "why": "Wasted energy is the input minus the useful output, so "
               "520 - 340 = 180 J is dissipated by heating and sound.",
    },
    {
        "id": "ks4-energy-transfers-in-a-system-e10",
        "subtopic_slug": "energy-transfers-in-a-system",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "A washing machine rattles loudly as its drum spins. Name the "
                "unwanted output, other than heating, that this represents.",
        "options": [
            "Light",
            "Sound",
            "Radiation",
            "Charge",
        ],
        "correct_index": 1,
        "why": "The drum makes the surrounding air vibrate, so some of the "
               "energy supplied leaves the machine as sound instead of "
               "turning the washing.",
    },
    {
        "id": "ks4-energy-transfers-in-a-system-e11",
        "subtopic_slug": "energy-transfers-in-a-system",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State why the energy dissipated by a machine is difficult to "
                "make use of afterwards.",
        "options": [
            "It has been spread thinly through the air and the objects around "
            "the machine",
            "It has been changed into a completely different substance inside "
            "the machine",
            "It has been sealed inside the metal of the machine, where no "
            "wire can reach it",
            "It has been slowed down so much that it can no longer move from "
            "place to place",
        ],
        "correct_index": 0,
        "why": "Dissipated energy ends up shared between a great many "
               "particles at close to room temperature, which is why so "
               "little can be done with it.",
    },
    {
        "id": "ks4-energy-transfers-in-a-system-e12",
        "subtopic_slug": "energy-transfers-in-a-system",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the unwanted energy transfer that using thicker copper "
                "wire in a circuit is intended to reduce.",
        "options": [
            "Sound produced as the current flows along the wire",
            "Air resistance acting on the outside of the wire",
            "Heating of the wire and the air around it",
            "Radiation given out by the insulation on the wire",
        ],
        "correct_index": 2,
        "why": "A thicker wire has a lower resistance, so less of the energy "
               "carried by the current is dissipated in warming the wire.",
    },

    # ══ standard · s05–s26 ═══════════════════════════════════════════════
    # Each method matched to a familiar machine with the cause explained, the
    # waste followed to where it finishes, and two subtractions in joules.
    {
        "id": "ks4-energy-transfers-in-a-system-s05",
        "subtopic_slug": "energy-transfers-in-a-system",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A cyclist oils a dry bicycle chain. Explain the effect on "
                "the energy wasted as the bicycle is ridden.",
        "options": [
            "More is wasted, because the oil adds mass that has to be carried "
            "up every hill",
            "Less is wasted, because the links slide over each other instead "
            "of gripping",
            "The same is wasted, because the same distance is travelled "
            "either way",
            "Less is wasted, because oil is a poor conductor and traps the "
            "energy inside the chain links",
        ],
        "correct_index": 1,
        "why": "Oil reduces the friction between the links, so less of the "
               "rider's energy is dissipated into the thermal stores of the "
               "chain and air.",
    },
    {
        "id": "ks4-energy-transfers-in-a-system-s06",
        "subtopic_slug": "energy-transfers-in-a-system",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A haulage firm fits a curved fairing to the roof of each cab "
                "and its fuel bills fall. Explain why.",
        "options": [
            "The fairing makes the lorry heavier, so it rolls downhill more "
            "easily and uses less fuel",
            "The fairing insulates the cab, so the engine does not have to "
            "warm the driver as much",
            "The air flows more smoothly over the lorry, so less energy is "
            "dissipated to the air",
            "The fairing collects the air rushing past and feeds it into the "
            "engine to burn the fuel",
        ],
        "correct_index": 2,
        "why": "A smoother shape reduces the work done against air "
               "resistance, so a larger share of the fuel's energy is left "
               "to move the lorry.",
    },
    {
        "id": "ks4-energy-transfers-in-a-system-s07",
        "subtopic_slug": "energy-transfers-in-a-system",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Describe the unwanted energy transfer that the thick foam "
                "walls of a cool box are there to slow down.",
        "options": [
            "The transfer from the warm air outside into the cold food inside",
            "The transfer from the cold food inside out into the warm air "
            "outside",
            "The transfer of sound from the room into the food that is packed "
            "inside the box",
            "The transfer of energy from the foam itself into the food that has "
            "been packed around it",
        ],
        "correct_index": 0,
        "why": "Energy is always transferred from the hotter place to the "
               "cooler one, so the unwanted transfer runs inwards and the "
               "foam slows it.",
    },
    {
        "id": "ks4-energy-transfers-in-a-system-s08",
        "subtopic_slug": "energy-transfers-in-a-system",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A hoist transfers 2700 J usefully and wastes 900 J. Calculate "
                "the energy supplied to it.",
        "options": [
            "1800 J",
            "2700 J",
            "3600 J",
            "900 J",
        ],
        "correct_index": 2,
        "why": "Everything supplied is either useful or wasted, so the input "
               "is 2700 + 900 = 3600 J.",
    },
    {
        "id": "ks4-energy-transfers-in-a-system-s09",
        "subtopic_slug": "energy-transfers-in-a-system",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why the tip of a drill bit is too hot to touch after "
                "it has cut through a steel plate.",
        "options": [
            "The steel plate passes some of its own thermal store into the bit, "
            "because steel is the hotter of the two materials",
            "The drill motor sends thermal energy down the bit to help it cut "
            "through the metal",
            "The bit is made of metal, and any metal becomes hot whenever it "
            "is turned quickly",
            "Work is done against friction at the tip, filling the thermal "
            "stores of the bit and the plate",
        ],
        "correct_index": 3,
        "why": "A force acting through a distance against friction does work, "
               "and that work is dissipated into the thermal stores of both "
               "the bit and the plate.",
    },
    {
        "id": "ks4-energy-transfers-in-a-system-s10",
        "subtopic_slug": "energy-transfers-in-a-system",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A coiled extension lead becomes noticeably warm while a "
                "2 kW heater is plugged into it. Explain why.",
        "options": [
            "The heater sends some of its own thermal energy back along the "
            "lead towards the socket",
            "The current does work against the resistance of the wire, "
            "filling its thermal store",
            "Charge builds up inside the coils of the lead until it is warm "
            "enough to be felt",
            "The plastic covering of the lead rubs against itself where the "
            "lead has been coiled up",
        ],
        "correct_index": 1,
        "why": "Every wire has some resistance, so a current through it "
               "dissipates energy by heating, and a large current makes that "
               "easy to feel.",
    },
    {
        "id": "ks4-energy-transfers-in-a-system-s11",
        "subtopic_slug": "energy-transfers-in-a-system",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A heavy door squeaks and is hard to push open. Identify the "
                "method that would reduce the energy wasted, and why.",
        "options": [
            "Streamlining the door, so that the air slips around its edge "
            "more smoothly",
            "Insulating the hinge, so that the energy wasted stays inside the "
            "metal of the pin",
            "Lubricating the hinge, so that the metal surfaces slide instead "
            "of catching",
            "Earthing the hinge, so that the charge built up by the rubbing "
            "can escape",
        ],
        "correct_index": 2,
        "why": "The squeak and the stiffness both come from friction between "
               "the hinge surfaces, and oil is what reduces friction between "
               "two solids.",
    },
    {
        "id": "ks4-energy-transfers-in-a-system-s12",
        "subtopic_slug": "energy-transfers-in-a-system",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Sound is the useful output of a loudspeaker but a wasted "
                "output of a washing machine. Explain how the same output can "
                "be both.",
        "options": [
            "Because a loudspeaker makes a louder sound than a washing "
            "machine ever does",
            "Because whether an output is useful depends on the job the "
            "device is bought to do",
            "Because the sound from a loudspeaker carries energy while the "
            "sound from a drum does not",
            "Because a washing machine turns its sound back into movement "
            "once the drum has stopped",
        ],
        "correct_index": 1,
        "why": "Useful and wasted describe the purpose of the device, not the "
               "kind of transfer, so the same sound is useful in one machine "
               "and waste in another.",
    },
    {
        "id": "ks4-energy-transfers-in-a-system-s13",
        "subtopic_slug": "energy-transfers-in-a-system",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why the gearbox of a car is filled with oil.",
        "options": [
            "The oil insulates the gears, so the energy wasted between the "
            "teeth is kept inside them",
            "The oil makes the gears heavier, so they keep turning for longer "
            "once the engine stops",
            "The oil fills the gaps between the teeth, so no air can get in "
            "to carry the energy away",
            "The oil separates the gear teeth, so less energy is dissipated "
            "as they slide past",
        ],
        "correct_index": 3,
        "why": "Meshing teeth rub against each other, and a film of oil "
               "between them cuts the friction so less energy is dissipated "
               "by heating.",
    },
    {
        "id": "ks4-energy-transfers-in-a-system-s14",
        "subtopic_slug": "energy-transfers-in-a-system",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why the front of a high-speed train is drawn out "
                "into a long tapered nose.",
        "options": [
            "The nose pushes the air aside gradually, so less energy is "
            "dissipated to the air",
            "The nose adds length to the train, so its mass is spread over "
            "more of the track",
            "The nose traps a cushion of still air, which insulates the "
            "carriages behind it",
            "The nose reduces the friction between the wheels and the rails "
            "beneath them",
        ],
        "correct_index": 0,
        "why": "Air resistance is the largest unwanted transfer at high "
               "speed, and a tapered shape lets the air flow around the train "
               "instead of piling up in front of it.",
    },
    {
        "id": "ks4-energy-transfers-in-a-system-s15",
        "subtopic_slug": "energy-transfers-in-a-system",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A conveyor belt motor is supplied with far more energy than "
                "the boxes on the belt gain. Identify where the difference "
                "finishes up.",
        "options": [
            "Inside the motor windings, held there until the belt is switched "
            "off again",
            "In the thermal stores of the bearings, the belt and the air, and "
            "in sound",
            "In the chemical store of the grease packed around the rollers of "
            "the belt",
            "In the gravitational potential store of the boxes travelling "
            "along the belt",
        ],
        "correct_index": 1,
        "why": "Friction at the rollers and bearings, and the vibration of "
               "the belt, dissipate the difference into the surroundings by "
               "heating and as sound.",
    },
    {
        "id": "ks4-energy-transfers-in-a-system-s16",
        "subtopic_slug": "energy-transfers-in-a-system",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A plumber fits foam sleeves along the hot water pipes in a "
                "cold loft. Explain how this saves energy.",
        "options": [
            "The foam makes the water travel faster, so it spends less time "
            "in the cold loft",
            "The foam collects the energy leaving the pipe and sends it back "
            "into the water",
            "The foam slows the transfer from the hot pipe to the cold loft "
            "air around it",
            "The foam removes the temperature difference between the pipe and "
            "the loft air",
        ],
        "correct_index": 2,
        "why": "The unwanted transfer is from the hot pipe to the cold air, "
               "and surrounding the pipe with a poor conductor slows it, so "
               "less has to be replaced by the boiler.",
    },
    {
        "id": "ks4-energy-transfers-in-a-system-s17",
        "subtopic_slug": "energy-transfers-in-a-system",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A skateboard's wheel bearings are clogged with grit. Predict "
                "the effect on the distance it rolls from one push, and "
                "explain.",
        "options": [
            "It rolls further, because the grit makes the wheels heavier and "
            "harder to stop",
            "It rolls the same distance, because the push given to it has not "
            "been changed",
            "It rolls a shorter distance, because the grit stops the wheels "
            "turning",
            "It rolls a shorter distance, because more energy is dissipated "
            "by friction at the bearings",
        ],
        "correct_index": 3,
        "why": "Gritty bearings raise the friction, so the kinetic store "
               "drains into thermal stores more quickly and the board stops "
               "sooner.",
    },
    {
        "id": "ks4-energy-transfers-in-a-system-s18",
        "subtopic_slug": "energy-transfers-in-a-system",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a physicist describes wasted energy as having "
                "reached a less useful store, rather than as there being less "
                "energy than before.",
        "options": [
            "Because the amount is unchanged and it is the usefulness that "
            "has fallen",
            "Because the amount does fall, but far too slightly for any "
            "instrument to measure it",
            "Because the energy has become a different quantity, and that "
            "quantity is not measured in joules",
            "Because the energy will return to its original store as soon as "
            "the machine cools down",
        ],
        "correct_index": 0,
        "why": "Dissipation moves energy to the thermal store of the "
               "surroundings, where the same number of joules is spread too "
               "thinly to drive anything.",
    },
    {
        "id": "ks4-energy-transfers-in-a-system-s19",
        "subtopic_slug": "energy-transfers-in-a-system",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A strip of brush is fitted along the bottom of a front door. "
                "Identify the unwanted transfer it reduces.",
        "options": [
            "The friction between the door and the frame as the door is "
            "opened and shut",
            "The conduction of energy along the metal door frame into the wall "
            "beside it",
            "The warm air of the hallway escaping through the gap to the cold "
            "outside",
            "The charge that builds up on the door handle as the door is "
            "pushed open",
        ],
        "correct_index": 2,
        "why": "A draught carries warmed air straight out of the house, so "
               "blocking the gap cuts an unwanted transfer that the heating "
               "would otherwise have to replace.",
    },
    {
        "id": "ks4-energy-transfers-in-a-system-s20",
        "subtopic_slug": "energy-transfers-in-a-system",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "The metal grille at the back of a refrigerator is warm when "
                "the appliance is running. Describe what this shows.",
        "options": [
            "The refrigerator is faulty, because a working one is cool at "
            "every point on its case",
            "The grille is deliberately warming the kitchen in order to balance "
            "the cold air inside the cabinet",
            "Energy is being transferred out of the appliance to the thermal "
            "store of the kitchen",
            "The grille holds the thermal energy of the food until the door "
            "is opened again",
        ],
        "correct_index": 2,
        "why": "The grille is where energy taken from the food, together with "
               "the energy wasted by the compressor, is dissipated into the "
               "kitchen air.",
    },
    {
        "id": "ks4-energy-transfers-in-a-system-s21",
        "subtopic_slug": "energy-transfers-in-a-system",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A lawnmower with a blunt blade needs more energy to cut the "
                "same lawn than one with a sharp blade. Explain why.",
        "options": [
            "A blunt blade has a larger mass, so more energy is needed to "
            "spin it at the same rate",
            "A blunt blade tears rather than slices, so more energy is "
            "dissipated by friction and sound",
            "A blunt blade spins more slowly, so the motor has to be left "
            "running for much longer",
            "A blunt blade insulates the motor, so the energy wasted cannot "
            "escape into the air",
        ],
        "correct_index": 1,
        "why": "A blunt edge drags through the grass instead of parting it, "
               "and that extra work against friction is dissipated by heating "
               "and as sound.",
    },
    {
        "id": "ks4-energy-transfers-in-a-system-s22",
        "subtopic_slug": "energy-transfers-in-a-system",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A phone charger is warm to the touch while it is charging. "
                "Explain what the warmth tells you about the energy supplied "
                "to it.",
        "options": [
            "All of it reaches the phone, and the warmth comes from the phone "
            "rather than the charger",
            "None of it reaches the phone until the charger has warmed up to "
            "its working temperature",
            "Some of it is dissipated by heating inside the charger rather "
            "than reaching the battery",
            "Some of it is stored in the charger, ready to be given to the "
            "phone on the next charge",
        ],
        "correct_index": 2,
        "why": "A warm case shows energy is being dissipated inside the "
               "charger, so the battery receives less than the mains "
               "supplies.",
    },
    {
        "id": "ks4-energy-transfers-in-a-system-s23",
        "subtopic_slug": "energy-transfers-in-a-system",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A cordless drill is supplied with 18.0 kJ and 12.6 kJ is "
                "transferred usefully to the drill bit. Calculate the energy "
                "wasted.",
        "options": [
            "30.6 kJ",
            "0.70 kJ",
            "12.6 kJ",
            "5.4 kJ",
        ],
        "correct_index": 3,
        "why": "The waste is the input with the useful output taken away: "
               "18.0 - 12.6 = 5.4 kJ, dissipated at the gears, the motor and "
               "the bit.",
    },
    {
        "id": "ks4-energy-transfers-in-a-system-s24",
        "subtopic_slug": "energy-transfers-in-a-system",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A metal playground slide is polished and children then "
                "travel down it faster. Explain this in terms of energy.",
        "options": [
            "Polishing lowers the friction, so less is dissipated and more "
            "fills the kinetic store",
            "Polishing makes the slide steeper, so the children are pulled "
            "down it with a larger force",
            "Polishing adds a layer of metal, so the slide holds more energy "
            "to give to the children",
            "Polishing reduces the air resistance, which is the largest "
            "unwanted transfer on a slide",
        ],
        "correct_index": 0,
        "why": "The gravitational potential store empties into the kinetic "
               "store and into friction at the surface, so cutting the "
               "friction leaves more for motion.",
    },
    {
        "id": "ks4-energy-transfers-in-a-system-s25",
        "subtopic_slug": "energy-transfers-in-a-system",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A cyclist rides the same flat route twice, the second time "
                "on soft under-inflated tyres, and finds it much harder work. "
                "Explain why.",
        "options": [
            "Soft tyres have a smaller mass of air in them, so the bicycle is "
            "lighter and less stable",
            "Soft tyres flex more, so more energy is dissipated into their "
            "thermal stores as they roll",
            "Soft tyres grip the road less, so the bicycle travels a longer "
            "distance along the route",
            "Soft tyres insulate the wheel rims, so the energy wasted cannot "
            "escape into the road",
        ],
        "correct_index": 1,
        "why": "A soft tyre is squashed and released at every turn of the "
               "wheel, and that repeated flexing dissipates energy by heating "
               "the rubber.",
    },
    {
        "id": "ks4-energy-transfers-in-a-system-s26",
        "subtopic_slug": "energy-transfers-in-a-system",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A vacuum cleaner is noisy and its motor housing becomes hot. "
                "Identify the two methods that would reduce those two "
                "unwanted transfers.",
        "options": [
            "Streamlining the handle, and insulating the flexible hose along "
            "its whole length",
            "Insulating the motor housing, and lubricating the plug where it "
            "meets the socket",
            "Lubricating the motor bearings, and using thicker wire in the "
            "windings",
            "Earthing the metal tube, and streamlining the brush head that "
            "runs over the carpet",
        ],
        "correct_index": 2,
        "why": "Noise and heating both come from friction at the bearings and "
               "from resistance in the windings, so oil and thicker wire "
               "attack the two causes.",
    },

    # ══ harder · h05–h26 ═════════════════════════════════════════════════
    # Two methods competing for one context, multi-step bookkeeping in joules,
    # and the evaluations — what a method does NOT achieve.
    {
        "id": "ks4-energy-transfers-in-a-system-h05",
        "subtopic_slug": "energy-transfers-in-a-system",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A heavy factory conveyor moves crates at walking pace. "
                "Compare lubrication and streamlining as ways of reducing the "
                "energy it wastes.",
        "options": [
            "Streamlining helps more, because air resistance is the largest "
            "transfer at any speed",
            "Both help equally, because every machine wastes the same amount "
            "to friction and to air",
            "Lubrication helps more, because at walking pace air resistance "
            "is very small",
            "Neither helps, because a conveyor carries its load horizontally "
            "and so wastes nothing",
        ],
        "correct_index": 2,
        "why": "Air resistance grows steeply with speed and is negligible at "
               "walking pace, so nearly all of this machine's waste is "
               "friction at its rollers and bearings.",
    },
    {
        "id": "ks4-energy-transfers-in-a-system-h06",
        "subtopic_slug": "energy-transfers-in-a-system",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "An electric milk float travels at about 6 m/s. Evaluate a "
                "proposal to fit it with an expensive streamlined body shell.",
        "options": [
            "A poor idea, because at that speed air resistance wastes little, "
            "so the saving is small",
            "A good idea, because a streamlined shell reduces the friction at "
            "the wheel bearings as well",
            "A good idea, because air resistance is the same on any vehicle "
            "however fast it moves",
            "A poor idea, because a streamlined shell would make the float "
            "heavier than the crates of milk it carries",
        ],
        "correct_index": 0,
        "why": "Streamlining pays for itself only where air resistance is "
               "large, and at 6 m/s it is a small part of what the float "
               "wastes.",
    },
    {
        "id": "ks4-energy-transfers-in-a-system-h07",
        "subtopic_slug": "energy-transfers-in-a-system",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A machine is supplied with 40 kJ, transfers 26 kJ usefully "
                "and dissipates 8 kJ at its bearings. Determine the energy "
                "leaving as sound and to the air.",
        "options": [
            "14 kJ",
            "34 kJ",
            "6 kJ",
            "18 kJ",
        ],
        "correct_index": 2,
        "why": "The total waste is 40 - 26 = 14 kJ, and 8 kJ of that is "
               "accounted for at the bearings, leaving 6 kJ.",
    },
    {
        "id": "ks4-energy-transfers-in-a-system-h08",
        "subtopic_slug": "energy-transfers-in-a-system",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A gearbox is re-oiled and then does exactly the same useful "
                "work as before. Predict what happens to the energy supplied "
                "and to the energy reaching the surroundings.",
        "options": [
            "Both rise, because the oil itself has to be warmed before the "
            "gearbox will turn",
            "Both fall, because less is dissipated while the useful work "
            "stays the same",
            "The supply falls, and the energy reaching the surroundings rises by "
            "exactly the same amount",
            "Both stay the same, because the useful work done has not been "
            "changed at all",
        ],
        "correct_index": 1,
        "why": "Less friction means fewer joules dissipated, so a smaller "
               "supply delivers the same useful work and less finishes in the "
               "surroundings.",
    },
    {
        "id": "ks4-energy-transfers-in-a-system-h09",
        "subtopic_slug": "energy-transfers-in-a-system",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Evaluate the claim that a machine could be built well enough "
                "to waste no energy at all.",
        "options": [
            "It is achievable, because oiling every surface removes friction "
            "completely",
            "It is achievable, because a machine sealed in a vacuum has "
            "nothing to waste energy to",
            "It is not achievable, because a machine large enough to be useful "
            "would collapse under the weight of its own moving parts",
            "It is not achievable, because some friction and some resistance "
            "are left however careful the design",
        ],
        "correct_index": 3,
        "why": "Every real surface has friction, every real wire has "
               "resistance and every real moving part vibrates, so some "
               "energy is always dissipated.",
    },
    {
        "id": "ks4-energy-transfers-in-a-system-h10",
        "subtopic_slug": "energy-transfers-in-a-system",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A delivery van spends its day in slow town traffic. Compare "
                "fitting a roof fairing with fitting harder tyres that flex "
                "less.",
        "options": [
            "The tyres help more, because rolling resistance dominates at low "
            "town speeds",
            "The fairing helps more, because it lowers the air resistance by the "
            "same amount at every speed",
            "Both help equally, because each reduces one unwanted transfer by "
            "the same amount",
            "Neither helps, because a van that keeps stopping wastes nothing "
            "between stops",
        ],
        "correct_index": 0,
        "why": "Air resistance is small at town speeds while the tyres flex "
               "on every turn of the wheel, so reducing rolling resistance "
               "saves more.",
    },
    {
        "id": "ks4-energy-transfers-in-a-system-h11",
        "subtopic_slug": "energy-transfers-in-a-system",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A hairdryer warms air and blows it through a nozzle. Identify "
                "which of its outputs is wasted, and why.",
        "options": [
            "The warm air, because a hairdryer is bought simply to move air "
            "past the hair",
            "The hum of its motor, because a hairdryer is bought to deliver "
            "warm moving air",
            "The moving air, because a hairdryer is bought simply to warm the "
            "air around it",
            "Both the warmth and the movement, because a hairdryer wastes "
            "more than it uses",
        ],
        "correct_index": 1,
        "why": "Warm moving air is exactly what a hairdryer is bought for, so "
               "the noise its motor makes is the output nobody wants.",
    },
    {
        "id": "ks4-energy-transfers-in-a-system-h12",
        "subtopic_slug": "energy-transfers-in-a-system",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Pump A is supplied with 1100 J and raises water by 880 J. "
                "Pump B is supplied with 1800 J and raises water by 1530 J. "
                "Determine which wastes more energy.",
        "options": [
            "Pump A, because 220 J is wasted against Pump B's 270 J",
            "Pump B, because 270 J is wasted against Pump A's 220 J",
            "Pump A, because it is supplied with less energy and so must work "
            "harder",
            "Neither, because both pumps raise water and so waste the same",
        ],
        "correct_index": 1,
        "why": "The waste is the input minus the useful output: A wastes "
               "1100 - 880 = 220 J and B wastes 1800 - 1530 = 270 J.",
    },
    {
        "id": "ks4-energy-transfers-in-a-system-h13",
        "subtopic_slug": "energy-transfers-in-a-system",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Evaluate a suggestion that wrapping a machine's metal casing "
                "in thick foam would reduce the energy it wastes.",
        "options": [
            "It would, because foam is a poor conductor and no energy could "
            "then leave the machine",
            "It would, because the foam returns the wasted energy to the "
            "moving parts inside",
            "It would not, because the foam slows the escape of the waste "
            "without reducing it",
            "It would not, because foam is a good conductor and would carry "
            "the waste away faster",
        ],
        "correct_index": 2,
        "why": "Insulation changes how quickly energy leaves a hot object; "
               "the friction and resistance producing the waste inside the "
               "machine are untouched.",
    },
    {
        "id": "ks4-energy-transfers-in-a-system-h14",
        "subtopic_slug": "energy-transfers-in-a-system",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "The rough inside surface of a long water pipe is replaced by "
                "a smooth lining. Predict the effect on the energy the pump "
                "must supply.",
        "options": [
            "It rises, because a smooth lining lets water travel further along "
            "the pipe",
            "It falls, because less energy is dissipated as the water rubs "
            "along the pipe wall",
            "It stays the same, because the same volume of water is delivered "
            "either way",
            "It falls, because a smooth lining insulates the pipe and keeps "
            "the water warm",
        ],
        "correct_index": 1,
        "why": "Water dragging over a rough wall dissipates energy by "
               "heating, so a smoother wall leaves more of the pump's supply "
               "moving the water.",
    },
    {
        "id": "ks4-energy-transfers-in-a-system-h15",
        "subtopic_slug": "energy-transfers-in-a-system",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A crane is supplied with 500 kJ to raise a load by 380 kJ. "
                "Its bearings are then lubricated and the waste falls by "
                "30 kJ. Determine the supply now needed for the same lift.",
        "options": [
            "530 kJ",
            "350 kJ",
            "410 kJ",
            "470 kJ",
        ],
        "correct_index": 3,
        "why": "The waste was 500 - 380 = 120 kJ and is now 90 kJ, so the "
               "supply needed is 380 + 90 = 470 kJ.",
    },
    {
        "id": "ks4-energy-transfers-in-a-system-h16",
        "subtopic_slug": "energy-transfers-in-a-system",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why an engineer cannot collect the energy a machine "
                "has dissipated into a workshop and feed it back in.",
        "options": [
            "Because it has been shared so widely, at so small a temperature "
            "rise, that nothing can gather it",
            "Because it has been destroyed by the friction that dissipated it "
            "in the first place",
            "Because it has turned into a form of energy that machines are "
            "unable to accept",
            "Because it has all left the building as radiation within a second "
            "or two, long before a collector could be set up",
        ],
        "correct_index": 0,
        "why": "The same joules are now spread through the air, the walls and "
               "the floor at close to room temperature, and thinly spread "
               "energy will not drive a machine.",
    },
    {
        "id": "ks4-energy-transfers-in-a-system-h17",
        "subtopic_slug": "energy-transfers-in-a-system",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Evaluate the claim that a quieter version of a machine must "
                "be wasting less energy than the noisy one.",
        "options": [
            "It must be, because sound is the largest unwanted output of any "
            "machine",
            "It must be, because a quiet machine has no vibration and so no "
            "friction",
            "Not necessarily, because sound is a small part of the waste and "
            "may become heating instead",
            "Not necessarily, because a quiet machine is simply running more "
            "slowly than the noisy one",
        ],
        "correct_index": 2,
        "why": "Sound carries only a small share of a machine's waste, and a "
               "damped part can dissipate the same energy into thermal stores "
               "without a sound.",
    },
    {
        "id": "ks4-energy-transfers-in-a-system-h18",
        "subtopic_slug": "energy-transfers-in-a-system",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A car is given both a smoother body shape and fresh engine "
                "oil. Predict which change saves more fuel on a long "
                "motorway journey, and explain.",
        "options": [
            "The oil, because friction inside an engine does not depend on "
            "how fast the car travels",
            "The oil, because air resistance falls away once a car is "
            "travelling at a steady speed",
            "Neither, because the two changes always save exactly the same "
            "amount of fuel",
            "The body shape, because air resistance grows steeply with speed "
            "and motorway speeds are high",
        ],
        "correct_index": 3,
        "why": "At motorway speed most of the fuel's energy goes on pushing "
               "air aside, so a smoother shape saves far more than a small "
               "cut in engine friction.",
    },
    {
        "id": "ks4-energy-transfers-in-a-system-h19",
        "subtopic_slug": "energy-transfers-in-a-system",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A pump is supplied with 12.0 kJ, the water gains 8.4 kJ and "
                "2.4 kJ is dissipated in the pipe. Determine the remaining "
                "energy and where it has gone.",
        "options": [
            "1.2 kJ, dissipated by heating and sound at the pump itself",
            "3.6 kJ, dissipated by heating and sound at the pump itself",
            "1.2 kJ, still held in the moving water as it leaves the pipe",
            "9.6 kJ, dissipated by heating and sound at the pump itself",
        ],
        "correct_index": 0,
        "why": "12.0 - 8.4 - 2.4 = 1.2 kJ is unaccounted for, and in a pump "
               "that is dissipated at the bearings, the motor and the "
               "impeller.",
    },
    {
        "id": "ks4-energy-transfers-in-a-system-h20",
        "subtopic_slug": "energy-transfers-in-a-system",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A rail operator can either grind its rails smooth or fit "
                "streamlined noses to its trains. Determine which change "
                "helps a 300 km/h service more.",
        "options": [
            "Grinding the rails, because the wheels touch them for the whole "
            "journey",
            "The streamlined noses, because air resistance is very large at "
            "that speed",
            "Grinding the rails, because a train is too heavy for its shape "
            "to matter",
            "Neither, because a train on rails wastes no energy once it has "
            "reached top speed",
        ],
        "correct_index": 1,
        "why": "Air resistance climbs steeply with speed and dominates at "
               "300 km/h, so shaping the train saves far more than smoother "
               "rails.",
    },
    {
        "id": "ks4-energy-transfers-in-a-system-h21",
        "subtopic_slug": "energy-transfers-in-a-system",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest why an old washing machine wastes more energy than "
                "an identical new one doing the same wash.",
        "options": [
            "Its parts have worn and its bearings have dried, so more energy "
            "is dissipated by friction",
            "Its metal has aged, so it now holds a larger amount of energy "
            "inside itself",
            "Its drum has become heavier with use, so the water inside it "
            "must be lifted further",
            "Its wiring has thickened with age, so the current through it is "
            "dissipated more quickly",
        ],
        "correct_index": 0,
        "why": "Worn surfaces and dry bearings raise the friction inside the "
               "machine, so more of the supply is dissipated and less turns "
               "the drum.",
    },
    {
        "id": "ks4-energy-transfers-in-a-system-h22",
        "subtopic_slug": "energy-transfers-in-a-system",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A ceiling fan hums and its motor runs hot. Determine which "
                "single change would cut the energy it wastes.",
        "options": [
            "Wrapping the motor in a felt sleeve to keep the hum inside the "
            "casing",
            "Fitting longer blades so that the motor turns more slowly than "
            "before",
            "Replacing the worn bushes the shaft turns in with freshly oiled "
            "ones",
            "Painting the blades a darker colour so that they radiate the waste "
            "away faster",
        ],
        "correct_index": 2,
        "why": "The hum and the heating both come from friction at the worn "
               "bushes, so replacing and oiling them reduces the waste at its "
               "source.",
    },
    {
        "id": "ks4-energy-transfers-in-a-system-h23",
        "subtopic_slug": "energy-transfers-in-a-system",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "An electric motor is connected to a larger supply so that a "
                "much larger current flows through the same windings. Predict "
                "the effect on the energy dissipated inside it.",
        "options": [
            "It falls, because a larger current passes through the windings "
            "more quickly",
            "It rises, because a larger current dissipates more energy in the "
            "resistance of the windings",
            "It stays the same, because the resistance of the windings has "
            "not been altered",
            "It falls, because a larger current lowers the resistance of the "
            "winding wire",
        ],
        "correct_index": 1,
        "why": "A wire's resistance dissipates energy whenever charge is "
               "driven through it, and a larger current means more energy "
               "dissipated by heating.",
    },
    {
        "id": "ks4-energy-transfers-in-a-system-h24",
        "subtopic_slug": "energy-transfers-in-a-system",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Two lamps give out the same amount of light, but one is too "
                "hot to touch and the other stays cool. Determine which "
                "wastes more energy, and why.",
        "options": [
            "The hot one, because the energy warming it is not the useful "
            "output wanted from a lamp",
            "The cool one, because a cool lamp must be leaking energy out of "
            "sight",
            "Both waste the same, because the light they give out is exactly "
            "the same",
            "The hot one, because a hot lamp gives light of a lower quality",
        ],
        "correct_index": 0,
        "why": "A lamp is wanted for light, so with equal light output the "
               "one that also warms its surroundings has been supplied with "
               "more and wasted the difference.",
    },
    {
        "id": "ks4-energy-transfers-in-a-system-h25",
        "subtopic_slug": "energy-transfers-in-a-system",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A food processor is fitted with a small cooling fan on its "
                "motor. Evaluate whether this reduces the energy the "
                "appliance wastes.",
        "options": [
            "It does, because the fan carries the wasted energy away before "
            "it can build up",
            "It does, because a cooler motor turns with less friction at "
            "every bearing",
            "It does not, because the waste is unchanged and the fan itself "
            "needs energy to turn",
            "It does not, because the fan blows the wasted energy straight "
            "back into the motor",
        ],
        "correct_index": 2,
        "why": "The fan moves the dissipated energy out of the motor faster, "
               "protecting it, but nothing about the friction and resistance "
               "producing that waste has changed.",
    },
    {
        "id": "ks4-energy-transfers-in-a-system-h26",
        "subtopic_slug": "energy-transfers-in-a-system",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A workshop has three machines. X is supplied with 2000 J "
                "and delivers 1700 J usefully, Y with 5000 J delivering "
                "4250 J, and Z with 800 J delivering 560 J. Determine which "
                "wastes the most energy.",
        "options": [
            "X, because 300 J is wasted",
            "Z, because 240 J is wasted",
            "Y, because 750 J is wasted",
            "All three waste the same amount as each other",
        ],
        "correct_index": 2,
        "why": "The wastes are 2000 - 1700 = 300 J, 5000 - 4250 = 750 J and "
               "800 - 560 = 240 J, so Y dissipates the most.",
    },
]
