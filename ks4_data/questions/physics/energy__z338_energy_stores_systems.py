"""Physics · Energy — the MRB-338 expansion of `energy-stores-systems`.

One leaf only: AQA 8463 §4.1.1, the named stores, what a system is, and how a
change in a system is described as store-to-store with the pathway named. The
original twelve rows in `energy.py` cover four stores (elastic, thermal,
chemical, magnetic), two pathways and three worked chains; this file takes the
four stores they never name (kinetic, gravitational, electrostatic, nuclear),
the two pathways they never name (heating, radiation), the definitions of
`system` and of a closed system, the whole misconception set, and conservation
used as bookkeeping with real joules.

The weight follows the CONTENT. `easier` stays small because recall here is
eight stores, four pathways and two definitions and nothing else — asking it a
ninth way would be the same question. The demand in this subtopic lives in
`standard` and `harder`, where a store change has to be traced through an
unfamiliar system and the shortfall accounted for, so that is where the
twenty-two-row bands sit.

Numbers are pure conservation bookkeeping — a store falls by this, another
rises by that, account for the difference — rather than mgh or ½mv², which
belong to `changes-in-energy` and would be that leaf's question wearing this
leaf's slug.
"""

TOPIC = "energy"
SUBJECT = "physics"

QUESTIONS = [
    # ══ easier · e05–e12 ═════════════════════════════════════════════════
    # The four stores and two pathways the original twelve never name, plus
    # the two definitions (conservation, system) the rest of the leaf rests on.
    {
        "id": "ks4-energy-stores-systems-e05",
        "subtopic_slug": "energy-stores-systems",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the store of energy that empties inside the fuel rods "
                "of a nuclear power station.",
        "options": [
            "The nuclear store of the uranium",
            "The chemical store of the uranium, because the fuel is burned "
            "in a furnace",
            "The thermal store of the coolant water that surrounds the fuel "
            "rods",
            "The electrostatic store of the charged particles inside the "
            "reactor core",
        ],
        "correct_index": 0,
        "why": "Energy released when uranium nuclei split comes from the "
               "nuclear store, which is emptied by the splitting rather than "
               "by any burning.",
    },
    {
        "id": "ks4-energy-stores-systems-e06",
        "subtopic_slug": "energy-stores-systems",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "A plastic rod is rubbed with a dry cloth and gains a static "
                "charge. State the store that has been filled.",
        "options": [
            "The magnetic store, because a field is set up around the "
            "charged rod",
            "The electrostatic store of the charged rod",
            "The chemical store, because rubbing changes the surface of the "
            "plastic",
            "The elastic potential store, because the rod is bent slightly "
            "as it is rubbed",
        ],
        "correct_index": 1,
        "why": "Separating charge fills an electrostatic store, held in the "
               "field between the charges that have been pulled apart.",
    },
    {
        "id": "ks4-energy-stores-systems-e07",
        "subtopic_slug": "energy-stores-systems",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "A crate is lifted from the floor onto a high shelf. State "
                "which store is filled as it rises.",
        "options": [
            "The kinetic store of the crate",
            "The elastic potential store of the shelf",
            "The gravitational potential store of the crate and the Earth",
            "The thermal store of the person doing the lifting",
        ],
        "correct_index": 2,
        "why": "Raising a mass against gravity fills the gravitational "
               "potential store, which empties again the moment the crate "
               "falls.",
    },
    {
        "id": "ks4-energy-stores-systems-e08",
        "subtopic_slug": "energy-stores-systems",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State what an object must be doing for it to hold energy in "
                "its kinetic store.",
        "options": [
            "Being held above the ground",
            "Being stretched or squashed",
            "Being at a high temperature",
            "Moving",
        ],
        "correct_index": 3,
        "why": "Motion alone fills the kinetic store: a stationary object "
               "holds nothing in it, however heavy, high or hot it is.",
    },
    {
        "id": "ks4-energy-stores-systems-e09",
        "subtopic_slug": "energy-stores-systems",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "You feel warmer standing in sunlight. Name the pathway that "
                "carries energy from the Sun to your skin.",
        "options": [
            "Heating, because the air between the Sun and the Earth carries "
            "it along",
            "Radiation",
            "Mechanical work done by the Sun on your skin",
            "Electrical work",
        ],
        "correct_index": 1,
        "why": "Energy crosses the empty space between the Sun and the Earth "
               "as radiation, which needs no particles to travel through.",
    },
    {
        "id": "ks4-energy-stores-systems-e10",
        "subtopic_slug": "energy-stores-systems",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "The element inside an electric kettle is hotter than the "
                "water around it. Name the pathway from element to water.",
        "options": [
            "Heating",
            "Radiation from the plastic body of the kettle",
            "Mechanical work done by the bubbles that form in the water",
            "Electrical work done by the water on the element",
        ],
        "correct_index": 0,
        "why": "A temperature difference between two things transfers energy "
               "by heating, always from the hotter one to the cooler one.",
    },
    {
        "id": "ks4-energy-stores-systems-e11",
        "subtopic_slug": "energy-stores-systems",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the principle of conservation of energy.",
        "options": [
            "Energy is created inside a power station and destroyed again "
            "inside a lamp",
            "Energy always finishes in the kinetic store of something, "
            "because everything moves",
            "Energy is used up a little at a time whenever a device is "
            "switched on",
            "Energy can be transferred, stored or dissipated, but it cannot "
            "be created or destroyed",
        ],
        "correct_index": 3,
        "why": "Energy moves between stores and spreads out into the "
               "surroundings, but the total in a closed system never changes.",
    },
    {
        "id": "ks4-energy-stores-systems-e12",
        "subtopic_slug": "energy-stores-systems",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State what a physicist means by a system.",
        "options": [
            "A machine that changes one form of energy into another form of "
            "energy",
            "Any device that is plugged into the mains electricity supply",
            "An object, or a group of objects, being considered together",
            "The name for the total energy that an object holds",
        ],
        "correct_index": 2,
        "why": "A system is whatever has been chosen to look at — one object "
               "or several — and energy changes are described within it.",
    },

    # ══ standard · s05–s26 ═══════════════════════════════════════════════
    # Store changes traced through familiar systems, one pathway named each
    # time, plus the misconception set answered from the wrong side.
    {
        "id": "ks4-energy-stores-systems-s05",
        "subtopic_slug": "energy-stores-systems",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A tennis ball is thrown straight up and slows as it rises. "
                "Describe the energy change taking place while it climbs.",
        "options": [
            "Its gravitational potential store empties into its kinetic "
            "store, which is why it slows down",
            "Its kinetic store empties into the gravitational potential "
            "store of the ball and the Earth as it climbs higher",
            "Its kinetic store empties into the elastic potential store of "
            "the ball",
            "Its chemical store empties into its kinetic store as it carries "
            "on travelling upwards",
        ],
        "correct_index": 1,
        "why": "Rising against gravity fills the gravitational potential "
               "store, and the energy comes from the kinetic store, which is "
               "why the ball slows.",
    },
    {
        "id": "ks4-energy-stores-systems-s06",
        "subtopic_slug": "energy-stores-systems",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A car brakes and comes to a stop. Describe where the energy "
                "in its kinetic store ends up.",
        "options": [
            "It is destroyed by the friction between the brake pads and the "
            "discs",
            "It stays in the kinetic store of the car until the car is driven "
            "off again later",
            "It fills the thermal stores of the brakes, the tyres and the "
            "surrounding air",
            "It refills the chemical store of the fuel in the tank, ready to "
            "be used again tomorrow",
        ],
        "correct_index": 2,
        "why": "The brakes do work against friction, dissipating the kinetic "
               "store into the thermal stores of the brakes and the air "
               "around them.",
    },
    {
        "id": "ks4-energy-stores-systems-s07",
        "subtopic_slug": "energy-stores-systems",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Describe the energy transfer that takes place when an "
                "electric kettle boils a jug of water.",
        "options": [
            "Electrical work fills the thermal store of the water, and some "
            "also fills the thermal store of the kettle and the kitchen",
            "Heating fills the chemical store of the water until that store "
            "is full enough for the water to boil",
            "Radiation from the element fills the kinetic store of the water",
            "Electrical work fills the electrical store of the water for as "
            "long as the kettle is switched on",
        ],
        "correct_index": 0,
        "why": "Charge driven through the element does electrical work, and "
               "the energy finishes in the thermal store of the water and of "
               "everything it touches.",
    },
    {
        "id": "ks4-energy-stores-systems-s08",
        "subtopic_slug": "energy-stores-systems",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A battery-powered motor winds a string and raises a small "
                "load at a steady speed. Describe the main energy change.",
        "options": [
            "Electrical store of the cells → heating → kinetic store of the "
            "load",
            "Chemical store of the cells → mechanical work → chemical store "
            "of the motor",
            "Kinetic store of the motor → electrical work → elastic "
            "potential store of the winding string",
            "Chemical store of the cells → electrical work → gravitational "
            "potential store of the load",
        ],
        "correct_index": 3,
        "why": "The cells empty a chemical store, electrical work carries it "
               "to the motor, and raising the load fills a gravitational "
               "potential store.",
    },
    {
        "id": "ks4-energy-stores-systems-s09",
        "subtopic_slug": "energy-stores-systems",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A pupil says the energy in a phone battery is used up when "
                "the phone goes flat. Explain what is wrong with this.",
        "options": [
            "Nothing is wrong: energy really is used up, which is exactly "
            "why the battery has to be recharged",
            "The energy has been transferred to the surroundings and to "
            "light from the screen, not used up",
            "The energy is still inside the battery, but the phone can no "
            "longer reach it once the wires have cooled",
            "The energy has turned into electricity, which is a completely "
            "different kind of energy and cannot be stored",
        ],
        "correct_index": 1,
        "why": "Energy cannot be destroyed; a flat battery means its "
               "chemical store is empty because that energy is now dispersed "
               "in the surroundings.",
    },
    {
        "id": "ks4-energy-stores-systems-s10",
        "subtopic_slug": "energy-stores-systems",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A mug of tea and a bath of water are both at 40 degrees C. "
                "Explain why the bath transfers far more energy to a cold "
                "room.",
        "options": [
            "The bath is really at a higher temperature than the mug once "
            "its size has been taken into account",
            "The bath is bigger, so heat rises out of it more quickly than "
            "it rises out of the mug",
            "The bath has many more particles, so its thermal store holds "
            "far more energy",
            "Temperature and thermal store mean the same thing, so the two "
            "of them transfer exactly the same amount",
        ],
        "correct_index": 2,
        "why": "Temperature is the average kinetic energy of the particles; "
               "the thermal store also depends on how many particles there "
               "are.",
    },
    {
        "id": "ks4-energy-stores-systems-s11",
        "subtopic_slug": "energy-stores-systems",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why electrical energy is not counted as one of the "
                "energy stores.",
        "options": [
            "Because an electric current is far too fast for its energy to "
            "be stored anywhere",
            "Because the electric current is used up in the connecting wires "
            "before it ever reaches the appliance",
            "Because a current is a pathway that transfers energy between "
            "stores, not a place it sits",
            "Because electrical energy is really chemical energy that has "
            "been given another name",
        ],
        "correct_index": 2,
        "why": "Stores hold energy and pathways move it; a current does work "
               "as it flows and holds nothing at all once it stops.",
    },
    {
        "id": "ks4-energy-stores-systems-s12",
        "subtopic_slug": "energy-stores-systems",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why the palms of your hands get warmer when you rub "
                "them together quickly.",
        "options": [
            "Mechanical work against friction fills the thermal stores of "
            "your hands",
            "Rubbing creates new energy in your skin, which you then feel as "
            "warmth",
            "The chemical store of your hands is filled by the movement of "
            "the skin",
            "Radiation passes from one palm to the other because they are "
            "pressed together",
        ],
        "correct_index": 0,
        "why": "A force acting through a distance does mechanical work, and "
               "friction dissipates that work into thermal stores.",
    },
    {
        "id": "ks4-energy-stores-systems-s13",
        "subtopic_slug": "energy-stores-systems",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Describe what is meant by a closed system.",
        "options": [
            "A system with a lid on it, so that no air can get in or out",
            "A system in which no energy is transferred in or out, so its "
            "total energy stays constant however it moves between stores",
            "A system in which all of the energy stays inside one single "
            "store the whole time through",
            "A system that has been switched off, so that no transfers "
            "happen inside it",
        ],
        "correct_index": 1,
        "why": "A closed system exchanges nothing with its surroundings, so "
               "however the energy moves between stores the total is "
               "unchanged.",
    },
    {
        "id": "ks4-energy-stores-systems-s14",
        "subtopic_slug": "energy-stores-systems",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A falling stone's gravitational potential store falls by "
                "250 J while its kinetic store rises by 214 J. Calculate the "
                "energy transferred to the surrounding air.",
        "options": [
            "464 J",
            "214 J",
            "250 J",
            "36 J",
        ],
        "correct_index": 3,
        "why": "Conservation of energy: 250 J leaves the gravitational "
               "store, 214 J arrives in the kinetic store, so 36 J has been "
               "dissipated.",
    },
    {
        "id": "ks4-energy-stores-systems-s15",
        "subtopic_slug": "energy-stores-systems",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Two identical bricks are raised from the ground, the first "
                "by 1.0 m and the second by 3.0 m. Compare the gravitational "
                "potential stores they end up with.",
        "options": [
            "They are equal, because the two bricks have the same mass as "
            "each other",
            "The second brick's store is three times the first brick's store",
            "The second brick's store is nine times the first, because the "
            "height is used twice over",
            "The first brick's store is larger, because it was easier to "
            "lift so less energy was wasted",
        ],
        "correct_index": 1,
        "why": "For a fixed mass the gravitational potential store is "
               "proportional to height, so three times the height gives "
               "three times the energy.",
    },
    {
        "id": "ks4-energy-stores-systems-s16",
        "subtopic_slug": "energy-stores-systems",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A pendulum bob swings from one side to the other. Describe "
                "the stores at the highest point of a swing and at the "
                "lowest point.",
        "options": [
            "Gravitational potential is greatest at the top and kinetic is "
            "greatest at the bottom",
            "Kinetic is greatest at the top and the gravitational potential "
            "store is greatest at the bottom",
            "Elastic potential is greatest at the top and thermal is "
            "greatest at the bottom",
            "Both stores are greatest at the bottom, because that is where "
            "the bob is moving fastest of all",
        ],
        "correct_index": 0,
        "why": "At the top the bob is momentarily stationary and highest; at "
               "the bottom it is lowest and moving fastest.",
    },
    {
        "id": "ks4-energy-stores-systems-s17",
        "subtopic_slug": "energy-stores-systems",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A pupil writes that the Sun creates the energy reaching the "
                "Earth. Explain the correction an examiner would make.",
        "options": [
            "The Sun creates energy only in its core, and then transfers it "
            "from the surface",
            "The Sun collects energy from space and passes it on to the "
            "planets around it",
            "The Sun transfers energy from its chemical store as the "
            "hydrogen inside it burns",
            "The Sun transfers energy from its nuclear store; it does not "
            "create any",
        ],
        "correct_index": 3,
        "why": "Fusion empties the Sun's nuclear store, and no process "
               "anywhere creates energy.",
    },
    {
        "id": "ks4-energy-stores-systems-s18",
        "subtopic_slug": "energy-stores-systems",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A runner finishes a race hot and out of breath. Identify "
                "the store that has emptied and the stores that have been "
                "filled.",
        "options": [
            "The thermal store of the runner has emptied and the chemical "
            "store of the muscles has been filled",
            "The kinetic store of the runner has emptied and the elastic "
            "potential store of the running track has been filled completely",
            "The chemical store of the runner has emptied and the thermal "
            "stores of the runner and the air have been filled",
            "The gravitational potential store has emptied and the nuclear "
            "store of the muscles has been filled",
        ],
        "correct_index": 2,
        "why": "Respiration empties the chemical store from food, and most "
               "of it finishes as thermal energy in the runner and the air "
               "around her.",
    },
    {
        "id": "ks4-energy-stores-systems-s19",
        "subtopic_slug": "energy-stores-systems",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A dry comb rubbed on a jumper picks up small pieces of "
                "paper. Explain in terms of stores why the paper accelerates "
                "towards the comb.",
        "options": [
            "The magnetic store of the comb empties into the kinetic store "
            "of the paper, which is why the paper lifts",
            "The chemical store of the comb empties as it attracts the paper "
            "towards it",
            "The electrostatic store of the comb and paper empties into the "
            "kinetic store of the paper",
            "The paper's own thermal store empties, which is why a piece of "
            "paper feels cool after it has jumped",
        ],
        "correct_index": 2,
        "why": "Charge separated by rubbing fills an electrostatic store, "
               "and as the attraction pulls the paper in that store empties "
               "into its kinetic store.",
    },
    {
        "id": "ks4-energy-stores-systems-s20",
        "subtopic_slug": "energy-stores-systems",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "An iron nail is released close to a strong magnet and snaps "
                "onto it. Describe the energy change.",
        "options": [
            "The magnetic store empties into the nail's kinetic store, which "
            "then fills thermal stores on impact, warming the nail and the "
            "magnet",
            "The nail's kinetic store fills the magnetic store as it travels "
            "across the gap",
            "The chemical store of the iron empties, and that is what pulls "
            "the nail across the gap towards the magnet",
            "The electrostatic store empties, because the nail and the "
            "magnet must carry opposite charges",
        ],
        "correct_index": 0,
        "why": "Energy held in the field between the nail and the magnet is "
               "released as they come together, and the impact dissipates "
               "it.",
    },
    {
        "id": "ks4-energy-stores-systems-s21",
        "subtopic_slug": "energy-stores-systems",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A drummer strikes a drum and a listener on the far side "
                "of the hall hears it. Identify how the energy reaches the "
                "listener's ear.",
        "options": [
            "By heating, because the drum skin becomes slightly warm as it "
            "is struck by the drummer",
            "As a wave through the air, which is a pathway and not a store",
            "From a sound store that is held in the air between the drum "
            "and the listener",
            "From the elastic potential store of the drum skin, which "
            "travels across the hall to the ear",
        ],
        "correct_index": 1,
        "why": "A sound wave transfers energy through the air from the drum "
               "to the ear; it carries energy rather than holding any, which "
               "is what makes it a pathway.",
    },
    {
        "id": "ks4-energy-stores-systems-s22",
        "subtopic_slug": "energy-stores-systems",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why the gravitational potential store is said to "
                "belong to an object and the Earth together, rather than to "
                "the object on its own.",
        "options": [
            "Because the Earth is very much heavier than the object, so it "
            "holds most of the energy",
            "Because the object would still hold the same store if the Earth "
            "were taken away",
            "Because energy always has to be shared out equally between any "
            "two objects that make up a system",
            "Because the store depends on the pull between the two, so it "
            "exists only when both do",
        ],
        "correct_index": 3,
        "why": "Gravitational potential energy is a property of the "
               "attraction between two masses, so the store belongs to the "
               "system rather than to one object.",
    },
    {
        "id": "ks4-energy-stores-systems-s23",
        "subtopic_slug": "energy-stores-systems",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A toy is pressed down onto a spring, released, and jumps "
                "into the air. Describe the sequence of stores from the "
                "press to the highest point.",
        "options": [
            "Chemical store of the child → elastic potential store of the "
            "spring → kinetic store of the toy → gravitational potential "
            "store of the toy",
            "Elastic potential store of the spring → chemical store of the "
            "toy → gravitational potential store of the toy → kinetic store "
            "of the toy",
            "Kinetic store of the toy → elastic potential store of the "
            "spring → thermal store of the air → gravitational potential "
            "store of the toy",
            "Chemical store of the child → gravitational potential store of "
            "the toy → elastic potential store of the spring → kinetic store "
            "of the toy",
        ],
        "correct_index": 0,
        "why": "Pressing the spring fills its elastic store, releasing it "
               "fills the toy's kinetic store, and rising turns that into "
               "gravitational potential.",
    },
    {
        "id": "ks4-energy-stores-systems-s24",
        "subtopic_slug": "energy-stores-systems",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "An electric fan is switched on and reaches a steady speed. "
                "Describe what happens to the energy transferred to it from "
                "the mains.",
        "options": [
            "It all stays in the kinetic store of the spinning blades once "
            "the speed is steady",
            "It fills the kinetic store of the moving air and the thermal "
            "stores of the motor and room",
            "It is stored in the electrical store of the motor windings "
            "until the fan is switched off again",
            "It is destroyed by the air resistance acting on the blades as "
            "they turn",
        ],
        "correct_index": 1,
        "why": "At a steady speed the blades' kinetic store is constant, so "
               "every joule supplied goes on to the air or to warming the "
               "motor.",
    },
    {
        "id": "ks4-energy-stores-systems-s25",
        "subtopic_slug": "energy-stores-systems",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A filament lamp is supplied with 500 J by electrical work "
                "and radiates 25 J as light. Determine the energy "
                "transferred to the thermal store of the surroundings.",
        "options": [
            "525 J",
            "25 J",
            "20 J",
            "475 J",
        ],
        "correct_index": 3,
        "why": "Everything supplied that does not leave as light finishes as "
               "thermal energy, so 500 - 25 = 475 J warms the lamp and the "
               "air.",
    },
    {
        "id": "ks4-energy-stores-systems-s26",
        "subtopic_slug": "energy-stores-systems",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A hot drink is left on a table and cools to room "
                "temperature. Explain why the total energy of the drink and "
                "the room together has not changed.",
        "options": [
            "The drink's thermal store has emptied into the room, and energy "
            "cannot be destroyed",
            "The energy that left the drink has been destroyed by the cool "
            "air around it",
            "The drink's thermal store has emptied into the chemical store "
            "of the liquid inside the mug",
            "The room is very much larger, so its temperature rise exactly "
            "cancels the drink's fall",
        ],
        "correct_index": 0,
        "why": "Heating transfers energy from the hotter drink to the cooler "
               "room; taken together as one system, nothing has left and "
               "nothing is lost.",
    },

    # ══ harder · h05–h26 ═════════════════════════════════════════════════
    # Unfamiliar systems, multi-step bookkeeping, and the evaluations — where
    # the system boundary is drawn, and what 'lost' actually means.
    {
        "id": "ks4-energy-stores-systems-h05",
        "subtopic_slug": "energy-stores-systems",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A firework rocket is lit, rises high into the sky and "
                "explodes. Describe the energy changes from the moment it is "
                "lit.",
        "options": [
            "The elastic potential store of the cardboard tube empties, "
            "filling the kinetic store of the rocket and then lighting the "
            "sky",
            "The nuclear store of the gunpowder empties, filling the "
            "gravitational potential store of the rocket and the thermal "
            "store of the sky",
            "The thermal store of the match empties into the gravitational "
            "potential store of the rocket, and every joule of it is "
            "returned to the ground as the rocket falls back down",
            "The chemical store of the fuel empties, filling the rocket's "
            "kinetic and gravitational potential stores, with the rest "
            "carried away by light, sound and heating",
        ],
        "correct_index": 3,
        "why": "Combustion empties a chemical store; part fills the rocket's "
               "mechanical stores and the remainder leaves as radiation, "
               "sound and warmed air.",
    },
    {
        "id": "ks4-energy-stores-systems-h06",
        "subtopic_slug": "energy-stores-systems",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "The same ball is dropped from 1.2 m onto a thick carpet and "
                "then onto a tiled floor. Predict which rebound is higher "
                "and explain why.",
        "options": [
            "The carpet, because a soft surface pushes the ball back up with "
            "a larger force",
            "The tiles, because the tiles deform very little, so less energy "
            "fills thermal stores",
            "Both rebound to the same height, because the ball started with "
            "the same store",
            "The carpet, because the ball's kinetic store is held in the "
            "fibres and then given straight back to it",
        ],
        "correct_index": 1,
        "why": "Deforming the carpet dissipates more of the ball's energy "
               "into thermal stores, so less is left to lift it back up.",
    },
    {
        "id": "ks4-energy-stores-systems-h07",
        "subtopic_slug": "energy-stores-systems",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A cyclist freewheels down a hill. Her gravitational "
                "potential store falls by 8400 J and her kinetic store rises "
                "by 6300 J. Determine the percentage of the energy that was "
                "dissipated.",
        "options": [
            "25%",
            "75%",
            "2.5%",
            "33%",
        ],
        "correct_index": 0,
        "why": "2100 J of the 8400 J never reached the kinetic store, and "
               "2100 / 8400 = 0.25, which is 25%.",
    },
    {
        "id": "ks4-energy-stores-systems-h08",
        "subtopic_slug": "energy-stores-systems",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A pupil writes that energy is lost as a machine runs. "
                "Evaluate this wording.",
        "options": [
            "It is correct, because the energy no longer exists once the "
            "machine has finished with it",
            "It is correct, because the total energy of the universe falls a "
            "little every single time that work is done",
            "It is wrong: nothing is lost, and the energy is spread too "
            "thinly among the surroundings to be useful",
            "It is wrong: nothing leaves the machine at all, so all of the "
            "energy is still inside it",
        ],
        "correct_index": 2,
        "why": "Dissipated energy has been transferred to the thermal store "
               "of the surroundings, where it is spread thinly rather than "
               "destroyed.",
    },
    {
        "id": "ks4-energy-stores-systems-h09",
        "subtopic_slug": "energy-stores-systems",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A kettle transfers 180 kJ by electrical work, and 85% of it "
                "reaches the thermal store of the water. Determine the "
                "energy that warms the kettle body and the kitchen air.",
        "options": [
            "153 kJ",
            "15 kJ",
            "207 kJ",
            "27 kJ",
        ],
        "correct_index": 3,
        "why": "The water takes 0.85 x 180 = 153 kJ, so the remaining "
               "180 - 153 = 27 kJ is dissipated to the kettle and the "
               "kitchen.",
    },
    {
        "id": "ks4-energy-stores-systems-h10",
        "subtopic_slug": "energy-stores-systems",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Water in an insulated container is warmed by 2 degrees C, "
                "once with an immersion heater and once by stirring it hard "
                "with a paddle. Compare the two transfers.",
        "options": [
            "Only the heater transfers energy, because stirring can never "
            "change a temperature",
            "Both fill the water's thermal store, one by heating and one by "
            "mechanical work",
            "Both fill the thermal store by heating, because the paddle "
            "becomes hot before the water does",
            "The paddle fills the kinetic store of the water rather than its "
            "thermal store, so no warming happens",
        ],
        "correct_index": 1,
        "why": "Heating and mechanical work are two different pathways that "
               "can fill the same store, which is why either route produces "
               "the same rise.",
    },
    {
        "id": "ks4-energy-stores-systems-h11",
        "subtopic_slug": "energy-stores-systems",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Hot water is sealed in a vacuum flask and is still warm "
                "three hours later. Explain why the flask is only "
                "approximately a closed system.",
        "options": [
            "It is a perfect closed system, because the vacuum stops every "
            "transfer completely",
            "It is not closed at all, because the water's thermal store "
            "empties into its own chemical store",
            "A little energy still leaves by conduction through the stopper "
            "and the seal, so the total inside it falls slowly",
            "Energy inside it is slowly destroyed by the vacuum, which is "
            "why the water is cooler",
        ],
        "correct_index": 2,
        "why": "A closed system exchanges no energy with its surroundings, "
               "and a real flask only slows that transfer rather than "
               "stopping it.",
    },
    {
        "id": "ks4-energy-stores-systems-h12",
        "subtopic_slug": "energy-stores-systems",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "An astronaut raises an identical toolbox by 2.0 m on the "
                "Earth and by 2.0 m on the Moon, where the gravitational "
                "field strength is about one sixth as large. Compare the "
                "gravitational potential stores gained.",
        "options": [
            "They are the same, because the mass of the toolbox and the "
            "height raised are unchanged",
            "The store gained on the Moon is about six times the store "
            "gained on the Earth",
            "The store gained on the Moon is about one sixth of the store "
            "gained on the Earth",
            "No store is gained on the Moon at all, because there is no "
            "atmosphere there",
        ],
        "correct_index": 2,
        "why": "The gravitational potential store depends on the field "
               "strength as well as the mass and the height, so a weaker "
               "field gives a smaller store.",
    },
    {
        "id": "ks4-energy-stores-systems-h13",
        "subtopic_slug": "energy-stores-systems",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A ball is dropped from a point where its gravitational "
                "potential store is 30 J. It rebounds to a point where the "
                "store is 21 J, and after the next bounce to 14.7 J. "
                "Determine the fraction of the store kept at each bounce.",
        "options": [
            "0.70 at the first bounce and 0.70 at the second",
            "0.70 at the first bounce and 0.49 at the second",
            "0.30 at the first bounce and 0.30 at the second",
            "0.70 at the first bounce and 0.63 at the second, because the "
            "losses build up",
        ],
        "correct_index": 0,
        "why": "21 / 30 = 0.70 and 14.7 / 21 = 0.70, so the same fraction of "
               "the store survives each impact.",
    },
    {
        "id": "ks4-energy-stores-systems-h14",
        "subtopic_slug": "energy-stores-systems",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A car fitted with a crumple zone hits a wall. Explain, in "
                "terms of stores, what the crumple zone achieves.",
        "options": [
            "It holds the whole of the car's kinetic store inside the metal, "
            "so that nothing at all reaches the passengers",
            "It removes the car's kinetic store before the impact, so the "
            "car arrives with no energy",
            "It deforms, so the kinetic store empties over a longer time "
            "into thermal stores and bent metal",
            "It converts the kinetic store into a gravitational potential "
            "store as the front of the car lifts up",
        ],
        "correct_index": 2,
        "why": "Permanently bending metal takes both energy and time, so the "
               "kinetic store empties more gradually and the forces on the "
               "passengers are smaller.",
    },
    {
        "id": "ks4-energy-stores-systems-h15",
        "subtopic_slug": "energy-stores-systems",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "An archer draws one bow through 0.60 m and a stiffer bow "
                "through 0.30 m, doing the same work each time. Compare the "
                "elastic potential stores of the two bows when fully drawn.",
        "options": [
            "They are equal, because the archer transferred the same energy "
            "to each bow",
            "The bow drawn 0.60 m holds twice as much, because it was pulled "
            "twice as far",
            "The stiffer bow holds twice as much, because it needed twice as "
            "much force",
            "Neither holds a store until the arrow is released and begins to "
            "move forward",
        ],
        "correct_index": 0,
        "why": "The elastic potential store is filled by the work done on "
               "the bow, so equal work gives equal stores however the force "
               "and distance are shared.",
    },
    {
        "id": "ks4-energy-stores-systems-h16",
        "subtopic_slug": "energy-stores-systems",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "The dome of a Van de Graaff generator is charged and a "
                "spark jumps to an earthed sphere. Describe what happens to "
                "the store held by the dome.",
        "options": [
            "Its magnetic store empties into the kinetic store of the "
            "sphere, which is why a spark can be heard",
            "Its electrostatic store is doubled, because the spark carries "
            "charge back onto the dome",
            "Its chemical store empties, because the belt inside the "
            "generator is worn away as it turns",
            "Its electrostatic store empties, and the energy leaves as "
            "light, sound and warmed air",
        ],
        "correct_index": 3,
        "why": "The separated charge holds an electrostatic store, and the "
               "spark discharges it into the surroundings as radiation, "
               "sound and thermal energy.",
    },
    {
        "id": "ks4-energy-stores-systems-h17",
        "subtopic_slug": "energy-stores-systems",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A battery-powered drone hovers at a constant height. "
                "Explain why its chemical store keeps emptying even though "
                "neither its height nor its speed is changing.",
        "options": [
            "Because energy is needed simply to exist at a height, whether "
            "or not anything moves",
            "Because the drone's gravitational potential store slowly leaks "
            "away and has to be topped up again",
            "Because its rotors do work on the air, filling the kinetic and "
            "thermal stores of the air",
            "Because a battery's chemical store empties at a fixed rate once "
            "it is connected to anything",
        ],
        "correct_index": 2,
        "why": "Hovering means pushing air downwards continually, and the "
               "energy for that work comes from the chemical store even "
               "though the drone's own stores are constant.",
    },
    {
        "id": "ks4-energy-stores-systems-h18",
        "subtopic_slug": "energy-stores-systems",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A lift is fitted with a counterweight that falls as the "
                "lift car rises. Explain how this reduces the energy the "
                "motor must supply.",
        "options": [
            "The counterweight's store empties as the car's fills, so the "
            "motor supplies only the difference",
            "The counterweight makes the lift car lighter, so its "
            "gravitational store need not be filled",
            "The counterweight stores energy that would otherwise be "
            "destroyed by friction in the cables",
            "The counterweight fills its own kinetic store, which the motor "
            "is then able to borrow whenever it is needed",
        ],
        "correct_index": 0,
        "why": "One gravitational store empties while the other fills, so "
               "the motor only has to make up the shortfall between them.",
    },
    {
        "id": "ks4-energy-stores-systems-h19",
        "subtopic_slug": "energy-stores-systems",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "In an exam a pupil writes that the heat store of the water "
                "increases. Explain why this loses the mark.",
        "options": [
            "Because water cannot hold a store of energy while it is still a "
            "liquid",
            "Because the correct name is the thermal store; heat names the "
            "transfer, not the store",
            "Because the store increases only when the water is actually "
            "boiling rather than merely warming",
            "Because heat and temperature are the same thing, so the "
            "sentence really says nothing at all",
        ],
        "correct_index": 1,
        "why": "AQA names eight stores and heat is not one of them: heating "
               "is the pathway that fills the thermal store.",
    },
    {
        "id": "ks4-energy-stores-systems-h20",
        "subtopic_slug": "energy-stores-systems",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A nuclear power station supplies a house. Starting with the "
                "uranium fuel and ending with a lit lamp, identify the "
                "correct sequence of stores and pathways.",
        "options": [
            "Chemical store of the uranium fuel → heating → thermal store of "
            "the water → electrical work → kinetic store of the turbine → "
            "the lamp",
            "Nuclear store of the fuel → radiation → electrostatic store of "
            "the generator → heating → the lamp",
            "Thermal store of the reactor → mechanical work → nuclear store "
            "of the turbine → electrical work → the lamp",
            "Nuclear store of the fuel → heating → thermal store of the "
            "water → mechanical work on the turbine → electrical work → the "
            "lamp",
        ],
        "correct_index": 3,
        "why": "Splitting nuclei empties a nuclear store, heating fills the "
               "water's thermal store, the steam does mechanical work on the "
               "turbine and the generator does electrical work.",
    },
    {
        "id": "ks4-energy-stores-systems-h21",
        "subtopic_slug": "energy-stores-systems",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A ball leaves a hand with 30 J in its kinetic store, and at "
                "its highest point its gravitational potential store has "
                "risen by 26 J. Determine the energy given to the air on the "
                "way up, and predict the kinetic store when it returns to "
                "the hand.",
        "options": [
            "4 J to the air, and 30 J on return, because energy is always "
            "conserved",
            "4 J to the air, and less than 26 J on return",
            "56 J to the air, and 0 J on return, because the ball stops at "
            "the top",
            "4 J to the air, and exactly 26 J on return",
        ],
        "correct_index": 1,
        "why": "30 - 26 = 4 J is dissipated climbing, and more is dissipated "
               "falling, so the ball comes back with less than the 26 J it "
               "had at the top.",
    },
    {
        "id": "ks4-energy-stores-systems-h22",
        "subtopic_slug": "energy-stores-systems",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A match is struck and burns away completely. Compare the "
                "chemical store of the match head before and after, and "
                "state where any difference has gone.",
        "options": [
            "The store is unchanged, because the same atoms are present "
            "before and after burning",
            "The store is larger afterwards, because the burnt material is "
            "hotter than it was",
            "The store is smaller afterwards, and the difference has been "
            "destroyed by the reaction",
            "The store is smaller afterwards, and the difference has left by "
            "heating and radiation",
        ],
        "correct_index": 3,
        "why": "Burning empties a chemical store, and the energy leaves as "
               "radiation from the flame and as warming of the surrounding "
               "air.",
    },
    {
        "id": "ks4-energy-stores-systems-h23",
        "subtopic_slug": "energy-stores-systems",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A hot metal block is dropped into cold water in an "
                "insulated container and both settle at the same "
                "temperature. Determine what has happened to the total "
                "energy of the block and the water.",
        "options": [
            "It has fallen, because the block's temperature dropped by more "
            "than the water's rose",
            "It is unchanged, because the energy leaving the block is exactly "
            "the energy entering the water",
            "It has risen, because the water and the block now share the "
            "same final temperature",
            "It has fallen by half, because energy is always shared equally "
            "between objects in contact",
        ],
        "correct_index": 1,
        "why": "In an insulated system nothing crosses the boundary, so "
               "every joule that empties the block's thermal store fills the "
               "water's.",
    },
    {
        "id": "ks4-energy-stores-systems-h24",
        "subtopic_slug": "energy-stores-systems",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a physicist would say the total energy has "
                "fallen if a braking car alone is taken as the system, but "
                "not if the road and the air are included as well.",
        "options": [
            "Because energy really is destroyed in the brakes, and including "
            "the air simply hides that fact",
            "Because the car is not a closed system: energy crosses its "
            "boundary into the road and air",
            "Because the road and the air create new energy to make up the "
            "difference in the total",
            "Because a car is too complicated to count as a system, so its "
            "energy cannot be totalled",
        ],
        "correct_index": 1,
        "why": "Conservation of energy holds for a closed system, so drawing "
               "the boundary where energy crosses it makes the total inside "
               "appear to change.",
    },
    {
        "id": "ks4-energy-stores-systems-h25",
        "subtopic_slug": "energy-stores-systems",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A pendulum is set swinging and the swings get smaller until "
                "it stops. Predict what would happen in a vacuum with a "
                "frictionless pivot, and explain why.",
        "options": [
            "They would get smaller more quickly, because there is no air "
            "left to hold the bob up",
            "They would grow larger, because the energy that used to go to "
            "the air now stays with the bob instead",
            "The bob would not swing at all, because there is no air for it "
            "to push against",
            "They would stay the same size indefinitely, because no pathway "
            "is left to empty the system",
        ],
        "correct_index": 3,
        "why": "The swings shrink only because energy is dissipated to the "
               "air and the pivot; remove both pathways and the closed "
               "system keeps its energy.",
    },
    {
        "id": "ks4-energy-stores-systems-h26",
        "subtopic_slug": "energy-stores-systems",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A rollercoaster car at the top of a drop holds 480 kJ in "
                "its gravitational potential store, measured from the "
                "bottom. At the bottom its kinetic store is 432 kJ. "
                "Determine the energy dissipated and evaluate the claim that "
                "the car alone is a closed system.",
        "options": [
            "48 kJ dissipated; the claim is wrong, because that energy has "
            "crossed the boundary into the track and the air around it",
            "48 kJ dissipated; the claim is right, because the total energy "
            "of the car has not changed",
            "912 kJ dissipated; the claim is wrong, because the two stores "
            "have to be added together",
            "0 kJ dissipated; the claim is right, because the car reaches "
            "the bottom of the drop every single time",
        ],
        "correct_index": 0,
        "why": "480 - 432 = 48 kJ has left the car for the rails and the "
               "air, so the car on its own is not a closed system.",
    },
]
