"""P1 lesson 01 — Energy stores: twelve questions (MRB-223).

⊕ WRITTEN IN RUN 1 AND KEPT, AFTER BEING CHECKED AGAINST DESIGN'S PAGE.

Run 1 authored these against a lesson it had invented, because it believed
Design had drawn nothing. She had. Every one of the twelve was then re-read
against `docs/ks3/design-reference/p1/p1-01-energy-stores.dc.html` — her
eight stores, her six sort cards, her five ledger scenarios and her four
rungs — and all twelve survive on the science, because the discrimination
they probe is the one her page is built around. Two of them land on her own
material directly: the wind-up torch in `h04` is her Rung 3 scenario, and the
"stored in the bulb as light energy" sentence in `h01` is the shape of her
Rung 4.

ONE thing changed: the misconception cited below was `ENER-09` in run 1's
numbering and is `ENER-10` here, because the register's ids were renumbered
when the family was confirmed as `ENER` rather than the `ENERGY` Design's
notes assume. No question text, option or `why` was altered.


These probe the one discrimination the lesson exists for: a STORE is
something a situation holds and would still hold tomorrow; a PATHWAY is
something that only exists while it is happening. The distractors are built
from the lesson's declared misconception ENER-10 — that sound, light and
electricity are kinds of energy things store — and from the three habits the
sorter is aimed at: reading "energy" as a substance, treating a store as a
property of an object rather than of a situation, and taking an empty store
for a missing one.

⚠️ The correct answer's position cycles 1, 2, 3, 0 through the twelve, so the
lesson contributes three of each index and no button beats reading (MRB-278).

The lesson carries no figures, so every question is figure=None.
"""

UNIT = "P1"
LESSON = "energy-stores"
LESSON_NUMBER = 1

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "p1-01-e01",
        "band": "easier",
        "text": "What is energy measured in?",
        "options": [
            {"text": "Newtons",
             "correct": False,
             "why": "Newtons measure force — a push or a pull. Force and "
                    "energy are different quantities with different units."},
            {"text": "Joules",
             "correct": True},
            {"text": "Degrees Celsius",
             "correct": False,
             "why": "Degrees measure temperature, which is how hot something "
                    "is. A bath at 40 degrees holds far more energy than a "
                    "match at 800."},
            {"text": "Watts",
             "correct": False,
             "why": "Watts measure how fast energy is being transferred, not "
                    "how much there is. You will meet them properly in "
                    "Energy at home."},
        ],
        "figure": None,
    },
    {
        "id": "p1-01-e02",
        "band": "easier",
        "text": "A cyclist freewheels down a hill and speeds up. Which store "
                "is filling?",
        "options": [
            {"text": "The elastic store",
             "correct": False,
             "why": "Nothing is being stretched, squashed or bent. An elastic "
                    "store needs something that will spring back."},
            {"text": "The chemical store",
             "correct": False,
             "why": "She is freewheeling, so no substance is reacting. A "
                    "chemical store fills only when substances are made that "
                    "hold more."},
            {"text": "The kinetic store",
             "correct": True},
            {"text": "The thermal store",
             "correct": False,
             "why": "A thermal store fills when something gets hotter. She is "
                    "getting faster, not hotter."},
        ],
        "figure": None,
    },
    {
        "id": "p1-01-e03",
        "band": "easier",
        "text": "Which of these is a way of transferring energy rather than a "
                "store of it?",
        "options": [
            {"text": "A hot oven",
             "correct": False,
             "why": "Switch the oven off and come back in ten minutes: it is "
                    "still hot. Something still there later is a store."},
            {"text": "A stretched elastic band",
             "correct": False,
             "why": "Hold it stretched all afternoon and it is still loaded. "
                    "That is exactly what a store means."},
            {"text": "A charged battery",
             "correct": False,
             "why": "Leave the phone in a drawer for a week and the charge is "
                    "still there. A chemical store."},
            {"text": "An electric current",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p1-01-e04",
        "band": "easier",
        "text": "A book is lifted from the floor onto a high shelf. Which "
                "store fills?",
        "options": [
            {"text": "The gravitational store",
             "correct": True},
            {"text": "The kinetic store",
             "correct": False,
             "why": "The book ends up still, on a shelf. Its kinetic store is "
                    "empty at the end, exactly as it was at the start."},
            {"text": "The thermal store of the book",
             "correct": False,
             "why": "The book is no hotter on the shelf than it was on the "
                    "floor. Height is what changed."},
            {"text": "The elastic store of the shelf",
             "correct": False,
             "why": "The shelf bends by a tiny amount, but the store the "
                    "question is about filled by far more, and it filled all "
                    "the way up."},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "p1-01-s01",
        "band": "standard",
        "text": "A student says a parked car has no kinetic store. What is "
                "the better way to say it?",
        "options": [
            {"text": "The car has no store at all until it moves",
             "correct": False,
             "why": "It has a chemical store in its fuel and a thermal store "
                    "in everything about it. Stores do not appear and "
                    "disappear."},
            {"text": "Its kinetic store is there and is empty",
             "correct": True},
            {"text": "Its kinetic store has been transferred to the road",
             "correct": False,
             "why": "That would describe a car that had just braked. A car "
                    "that has been parked all night never had one to "
                    "transfer."},
            {"text": "Its kinetic store has turned into a gravitational one",
             "correct": False,
             "why": "Nothing turns into anything. And the car has not changed "
                    "height, so no gravitational store moved either way."},
        ],
        "figure": None,
    },
    {
        "id": "p1-01-s02",
        "band": "standard",
        "text": "A speaker plays loudly in an empty hall. Where is the sound "
                "energy stored?",
        "options": [
            {"text": "In the air of the hall, which fills up with it",
             "correct": False,
             "why": "Cut the power and the hall is silent within a fraction "
                    "of a second. Nothing that empties that fast was holding "
                    "anything."},
            {"text": "In the walls, which absorb it and hold it as sound",
             "correct": False,
             "why": "The walls do absorb it — and what fills is their THERMAL "
                    "store. Nothing anywhere holds sound."},
            {"text": "Nowhere. Sound is not a store",
             "correct": True},
            {"text": "In the speaker, which releases it slowly",
             "correct": False,
             "why": "The speaker holds a chemical or an electrical supply, "
                    "not sound. Unplug it and the sound stops at once."},
        ],
        "figure": None,
    },
    {
        "id": "p1-01-s03",
        "band": "standard",
        "text": "Which pair of situations fills the SAME store?",
        "options": [
            {"text": "A stretched catapult and a bowl of cold porridge",
             "correct": False,
             "why": "The catapult fills an elastic store and the porridge "
                    "holds a chemical one. Both are stores; they are not the "
                    "same store."},
            {"text": "A mug of hot tea and a skateboard rolling along",
             "correct": False,
             "why": "Thermal and kinetic. Getting hotter and getting faster "
                    "are different changes."},
            {"text": "A freshly charged battery and a book on a high shelf",
             "correct": False,
             "why": "Chemical and gravitational. The battery is about which "
                    "substances exist; the book is about height."},
            {"text": "A wound clock spring and a compressed sofa cushion",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p1-01-s04",
        "band": "standard",
        "text": "Why is a lump of clay squashed flat NOT an elastic store?",
        "options": [
            {"text": "Because the clay does not spring back",
             "correct": True},
            {"text": "Because clay is not a stretchy material",
             "correct": False,
             "why": "Close, but say what stretchy actually means here. A "
                    "material can be squashed easily and still fill no "
                    "elastic store."},
            {"text": "Because squashing does not transfer any energy",
             "correct": False,
             "why": "It certainly does — your muscles empty a chemical store "
                    "doing it. The question is where that energy ended up."},
            {"text": "Because clay is a solid rather than a spring",
             "correct": False,
             "why": "A steel bar is a solid too, and bending one fills an "
                    "elastic store. It is not about being solid."},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "p1-01-h01",
        "band": "harder",
        "text": "A student writes: \"electrical energy travels down the wire "
                "and is stored in the bulb as light energy\". How many "
                "separate errors is that?",
        "options": [
            {"text": "One — energy really does travel as electricity "
                     "down the wire",
             "correct": False,
             "why": "Look at the first half too. Electricity is something "
                    "that happens, not something a wire or a bulb holds."},
            {"text": "Two — electricity is not a store, and light is not "
                     "one either",
             "correct": True},
            {"text": "None — both halves are the normal way people say "
                     "it in class",
             "correct": False,
             "why": "It is a very common way of saying it, and that is "
                    "exactly why the lesson separates stores from pathways."},
            {"text": "Three — the wire, the bulb and the light are each "
                     "named wrongly",
             "correct": False,
             "why": "The wire and the bulb are real objects doing real jobs. "
                    "The errors are about the two things named as energies."},
        ],
        "figure": None,
    },
    {
        "id": "p1-01-h02",
        "band": "harder",
        "text": "Two identical bricks sit on a table, one on top of the "
                "other. A student says only the top one has a gravitational "
                "store. What is wrong with that?",
        "options": [
            {"text": "Nothing — the lower brick is not raised, so it has none",
             "correct": False,
             "why": "Raised compared with what? Push the table away and both "
                    "bricks fall, which means both had something to spend."},
            {"text": "Only the lower brick has one, because it is holding the "
                     "other up",
             "correct": False,
             "why": "Holding something up is a force, not a store. The lower "
                    "brick does have a gravitational store, but not for that "
                    "reason."},
            {"text": "Both have one, and it depends on where you measure "
                     "height from",
             "correct": True},
            {"text": "Neither has one, because neither is moving",
             "correct": False,
             "why": "Movement fills a kinetic store. A gravitational store is "
                    "about position, and a still object can have a very full "
                    "one."},
        ],
        "figure": None,
    },
    {
        "id": "p1-01-h03",
        "band": "harder",
        "text": "Which statement about a gravitational store is exactly "
                "right?",
        "options": [
            {"text": "It is stored inside the raised object",
             "correct": False,
             "why": "Take the Earth away and the store is gone, with the "
                    "object unchanged. So it cannot be inside the object."},
            {"text": "It is stored in the gravity around the object",
             "correct": False,
             "why": "Gravity is a force, measured in newtons. Asking how many "
                    "joules a force holds is a category mistake."},
            {"text": "It is stored in the air the object was lifted through",
             "correct": False,
             "why": "Lift the object in a vacuum and the store fills exactly "
                    "the same. The air plays no part in it."},
            {"text": "It belongs to the object and the Earth together",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p1-01-h04",
        "band": "harder",
        "text": "A wind-up torch is wound, then left on a shelf for a month, "
                "then switched on and it works. What does that month prove?",
        "options": [
            {"text": "The spring's elastic store is a real store",
             "correct": True},
            {"text": "The spring was making energy the whole month",
             "correct": False,
             "why": "Nothing makes energy. And if it had, the torch would "
                    "have got brighter over the month rather than staying the "
                    "same."},
            {"text": "Light was being stored in the bulb over that time",
             "correct": False,
             "why": "The bulb was never on. There was nothing for it to store "
                    "even if light could be stored, which it cannot."},
            {"text": "Springs work better after being left alone",
             "correct": False,
             "why": "The month changed nothing about the spring. That is the "
                    "point: what was there at the start was still there at "
                    "the end."},
        ],
        "figure": None,
    },

    # ── MRB-335 top-up · easier ──────────────────────────────────────────
    {
        "id": "p1-01-e05",
        "band": "easier",
        "text": "Which of these is an energy STORE?",
        "options": [            {"text": "A sound wave travelling through air", "correct": False,
             "why": "Sound is a pathway too; the energy is on its way from "
                    "one store to another."},
            {"text": "A beam of light crossing a room", "correct": False,
             "why": "Light is a pathway — a way energy travels — not "
                    "somewhere it sits and waits."},
            {"text": "An electric current in a wire", "correct": False,
             "why": "A current carries energy from one store to another. "
                    "Nothing is held in the current itself."},
            {"text": "The chemical store of a battery", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p1-01-e06",
        "band": "easier",
        "text": "A mug of hot tea holds energy in which store?",
        "options": [            {"text": "The chemical store", "correct": False,
             "why": "A chemical store fills when bonds are rearranged, as in "
                    "a battery or a fuel — not by being warmed."},
            {"text": "The elastic store", "correct": False,
             "why": "An elastic store fills when something is stretched or "
                    "squashed, which the tea is not."},
            {"text": "The kinetic store", "correct": False,
             "why": "The mug as a whole is not moving. The particles are, and "
                    "that is counted as the thermal store."},
            {"text": "The thermal store", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p1-01-e07",
        "band": "easier",
        "text": "A firework explodes. Which store is emptying?",
        "options": [
            {"text": "The kinetic store", "correct": False,
             "why": "The kinetic store FILLS as the pieces fly outwards; "
                    "something else had to empty to fill it."},
            {"text": "The gravitational store", "correct": False,
             "why": "The gravitational store only changes when something "
                    "rises or falls, not when it burns."},
            {"text": "The chemical store", "correct": True},
            {"text": "The elastic store", "correct": False,
             "why": "Nothing in a firework is stretched or squashed before it "
                    "goes off."},
        ],
        "figure": None,
    },

    # ── MRB-335 top-up · standard ────────────────────────────────────────
    {
        "id": "p1-01-s05",
        "band": "standard",
        "text": "A catapult is pulled back and released, firing a stone. "
                "Which store empties and which fills?",
        "options": [            {"text": "The elastic store empties and the thermal store fills "
                     "only",
             "correct": False,
             "why": "A little does warm the rubber, but the point of a "
                    "catapult is the kinetic store of the stone."},
            {"text": "The kinetic store empties and the elastic store fills",
             "correct": False,
             "why": "That is the pull-back, not the release. On release the "
                    "stretched rubber is what empties."},
            {"text": "The chemical store empties and the kinetic store fills",
             "correct": False,
             "why": "Nothing chemical happens in a catapult. The chemical "
                    "store emptied earlier, in the arm that pulled it."},
            {"text": "The elastic store empties and the kinetic store fills",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p1-01-s06",
        "band": "standard",
        "text": "A wind-up radio is cranked and then plays music. Which "
                "sequence of stores is right?",
        "options": [            {"text": "Thermal in the arm, then kinetic in the spring, then "
                     "chemical in the speaker",
             "correct": False,
             "why": "The muscles empty a chemical store, and a wound spring "
                    "is stretched, so its store is elastic."},
            {"text": "Elastic in the spring, then electrical stored in the "
                     "wires, then sound stored in the air",
             "correct": False,
             "why": "Neither electricity nor sound is a store. Both are "
                    "pathways carrying energy onwards."},
            {"text": "Sound in the spring, then chemical in the speaker, then "
                     "kinetic in the air",
             "correct": False,
             "why": "A wound spring holds an elastic store, and nothing in "
                    "the radio holds a chemical one."},
            {"text": "Chemical in the arm, then elastic in the spring, then "
                     "thermal and sound leaving",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p1-01-s07",
        "band": "standard",
        "text": "Why is it wrong to call electricity a store of energy?",
        "options": [
            {"text": "Because electricity travels much too fast for anything "
                     "to store it at all",
             "correct": False,
             "why": "Speed has nothing to do with it. A pathway is defined by "
                    "carrying energy, not by how quickly."},
            {"text": "Because a current carries energy between stores, not "
                     "holds it",
             "correct": True},
            {"text": "Because electricity is not really a form of energy at "
                     "all",
             "correct": False,
             "why": "It does deliver energy — that is exactly what makes it a "
                    "pathway."},
            {"text": "Because only chemicals and moving objects can hold "
                     "energy",
             "correct": False,
             "why": "There are eight stores, including thermal, elastic and "
                    "gravitational, so the list is far longer than that."},
        ],
        "figure": None,
    },

    # ── MRB-335 top-up · harder ──────────────────────────────────────────
    {
        "id": "p1-01-h05",
        "band": "harder",
        "text": "A skydiver falls at a constant speed under an open "
                "parachute. Which account of the stores is correct?",
        "options": [
            {"text": "The kinetic store empties into the thermal store of the "
                     "air",
             "correct": False,
             "why": "The kinetic store stays the same size. What is emptying "
                    "is the gravitational store."},
            {"text": "The gravitational store empties and the kinetic store "
                     "fills at exactly the same rate",
             "correct": False,
             "why": "The speed is constant, so the kinetic store is not "
                    "changing at all."},
            {"text": "No store changes, because the speed is not changing",
             "correct": False,
             "why": "The skydiver is still losing height, so the "
                    "gravitational store is emptying every second."},
            {"text": "The gravitational store empties, the kinetic store "
                     "holds steady, the air warms",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p1-01-h06",
        "band": "harder",
        "text": "A student lists light, heat, sound, electrical and chemical "
                "as five kinds of energy. Which item is genuinely a store?",
        "options": [
            {"text": "Sound, because you can hear the energy arriving",
             "correct": False,
             "why": "Hearing it is the energy passing through you. Sound is a "
                    "pathway, not a store."},
            {"text": "Light, because a bright object clearly holds a lot",
             "correct": False,
             "why": "The brightness shows energy leaving. Light carries it "
                    "away rather than holding it."},
            {"text": "Chemical, because a battery holds it while nothing "
                     "happens",
             "correct": True},
            {"text": "Electrical, because a charged battery holds it",
             "correct": False,
             "why": "The battery holds a CHEMICAL store; the current is the "
                    "pathway that takes it out."},
        ],
        "figure": None,
    },
    {
        "id": "p1-01-h07",
        "band": "harder",
        "text": "A roller-coaster car is held still at the top of the first "
                "hill. A student says it has no energy. What is the right "
                "account?",
        "options": [
            {"text": "Its kinetic store is empty, its gravitational store "
                     "full",
             "correct": True},
            {"text": "It has no energy at all until the brakes are released",
             "correct": False,
             "why": "Being high up is precisely what fills the gravitational "
                    "store; the release only lets it empty."},
            {"text": "Both its stores are empty, because it is not moving",
             "correct": False,
             "why": "Height fills a store whether or not anything is moving, "
                    "which is why the drop works."},
            {"text": "Its kinetic store is full, because it is about to move "
                     "downhill",
             "correct": False,
             "why": "A store counts what is there now. About to move is not "
                    "moving."},
        ],
        "figure": None,
    },

    # ── MRB-338 night 3 top-up · easier ──────────────────────────────────
    {
        "id": "p1-01-e08",
        "band": "easier",
        "text": "What does it mean to call something an energy store?",
        "options": [
            {"text": "Somewhere energy sits and can be counted while nothing "
                     "is happening",
             "correct": True},
            {"text": "A route along which energy travels from one object to "
                     "another",
             "correct": False,
             "why": "That describes a pathway. A pathway exists only while "
                    "the transfer is going on."},
            {"text": "A material that energy is poured into and later poured "
                     "back out of",
             "correct": False,
             "why": "Energy is not a liquid and there is nothing to pour. A "
                    "store is a number you work out."},
            {"text": "A machine that makes fresh energy whenever it is "
                     "switched on",
             "correct": False,
             "why": "No machine makes energy. A machine only moves it from "
                    "one store to another."},
        ],
        "figure": None,
    },
    {
        "id": "p1-01-e09",
        "band": "easier",
        "text": "What does a physicist mean by a pathway?",
        "options": [
            {"text": "A store that empties faster than the stores around it",
             "correct": False,
             "why": "How quickly a store empties does not change what it is. "
                    "A fast store is still a store."},
            {"text": "A way energy travels from one store to another",
             "correct": True},
            {"text": "A container that holds energy while it is on the move",
             "correct": False,
             "why": "Nothing holds energy on the move. Pause the world and "
                    "there is no light waiting to be counted."},
            {"text": "The part of a device that wastes least",
             "correct": False,
             "why": "That is a judgement about a device, and not the name of "
                    "anything in an energy account."},
        ],
        "figure": None,
    },
    {
        "id": "p1-01-e10",
        "band": "easier",
        "text": "Two magnets are pulled apart and held there. Which store has "
                "been filled?",
        "options": [
            {"text": "The elastic store",
             "correct": False,
             "why": "Neither magnet is stretched or squashed. Both are "
                    "exactly the shape they were."},
            {"text": "The kinetic store",
             "correct": False,
             "why": "They are held still at the end, so nothing is left "
                    "moving."},
            {"text": "The magnetic store",
             "correct": True},
            {"text": "The electrostatic store",
             "correct": False,
             "why": "That store is filled by separating electric charges, "
                    "not by separating magnets."},
        ],
        "figure": None,
    },
    {
        "id": "p1-01-e11",
        "band": "easier",
        "text": "A balloon is rubbed on a woollen jumper and then sticks to a "
                "wall. Which store did the rubbing fill?",
        "options": [
            {"text": "The magnetic store",
             "correct": False,
             "why": "A balloon carries no magnets, and rubbing wool on rubber "
                    "makes none."},
            {"text": "The chemical store",
             "correct": False,
             "why": "No new substances are made. The wool and the rubber are "
                    "the same materials afterwards."},
            {"text": "The elastic store",
             "correct": False,
             "why": "The balloon is no more stretched after the rubbing than "
                    "it was before."},
            {"text": "The electrostatic store",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p1-01-e12",
        "band": "easier",
        "text": "Which store is held inside the nucleus of an atom?",
        "options": [
            {"text": "The nuclear store",
             "correct": True},
            {"text": "The chemical store",
             "correct": False,
             "why": "The chemical store is about how atoms are joined to one "
                    "another, not about what is inside them."},
            {"text": "The electrostatic store",
             "correct": False,
             "why": "That store is filled by separating charges, which "
                    "happens well outside the nucleus."},
            {"text": "The thermal store",
             "correct": False,
             "why": "Every material has a thermal store, and it is about how "
                    "warm the material is."},
        ],
        "figure": None,
    },
    {
        "id": "p1-01-e13",
        "band": "easier",
        "text": "A lorry drives along a flat motorway at a steady speed. "
                "Which store is full?",
        "options": [
            {"text": "The elastic store",
             "correct": False,
             "why": "Nothing on the lorry is stretched or squashed as it "
                    "drives along."},
            {"text": "The kinetic store",
             "correct": True},
            {"text": "The gravitational store",
             "correct": False,
             "why": "That store fills when something is raised, and a flat "
                    "motorway raises nothing."},
            {"text": "The magnetic store",
             "correct": False,
             "why": "No magnets on the lorry are being held apart or pushed "
                    "together."},
        ],
        "figure": None,
    },
    {
        "id": "p1-01-e14",
        "band": "easier",
        "text": "The spring inside a click pen is squashed when the button is "
                "pressed. Which store fills?",
        "options": [
            {"text": "The chemical store",
             "correct": False,
             "why": "Nothing reacts inside a pen. The spring is the same "
                    "steel before and after."},
            {"text": "The thermal store",
             "correct": False,
             "why": "The spring is no warmer squashed than it was loose."},
            {"text": "The elastic store",
             "correct": True},
            {"text": "The gravitational store",
             "correct": False,
             "why": "The spring has not been raised, and a pen can be clicked "
                    "lying flat on a desk."},
        ],
        "figure": None,
    },
    {
        "id": "p1-01-e15",
        "band": "easier",
        "text": "A skier waits at the top of a slope without moving. Which "
                "store is full?",
        "options": [
            {"text": "The kinetic store of the skis",
             "correct": False,
             "why": "The skier is not moving yet, so that store is empty "
                    "until the run starts."},
            {"text": "The elastic store of the skis",
             "correct": False,
             "why": "Nothing on the skier is stretched or squashed while they "
                    "stand still."},
            {"text": "The nuclear store of the snow",
             "correct": False,
             "why": "Every atom has one, but nothing at the top of a ski "
                    "slope empties it."},
            {"text": "The gravitational store of the skier",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p1-01-e16",
        "band": "easier",
        "text": "A radiator is full of hot water. Which store does that water "
                "hold?",
        "options": [
            {"text": "The thermal store",
             "correct": True},
            {"text": "The chemical store",
             "correct": False,
             "why": "Water in a radiator is not reacting. Nothing about it is "
                    "being rearranged."},
            {"text": "The elastic store",
             "correct": False,
             "why": "Water in a radiator is not being stretched or "
                    "squashed."},
            {"text": "The magnetic store",
             "correct": False,
             "why": "No magnets are being held apart in a radiator, so that "
                    "store plays no part."},
        ],
        "figure": None,
    },
    {
        "id": "p1-01-e17",
        "band": "easier",
        "text": "A slice of toast is eaten. Which store did the toast hold?",
        "options": [
            {"text": "The elastic store",
             "correct": False,
             "why": "Toast is not a spring. Nothing about it is stretched or "
                    "squashed to hold energy."},
            {"text": "The chemical store",
             "correct": True},
            {"text": "The nuclear store",
             "correct": False,
             "why": "Digestion rearranges molecules. It never reaches inside "
                    "a nucleus."},
            {"text": "The thermal store",
             "correct": False,
             "why": "Cold toast feeds you just as well as warm toast, so "
                    "warmth is not the store being used."},
        ],
        "figure": None,
    },
    {
        "id": "p1-01-e18",
        "band": "easier",
        "text": "Which of these is a pathway rather than a store?",
        "options": [
            {"text": "A hot brick cooling on a bench",
             "correct": False,
             "why": "A hot brick holds a thermal store, and it still holds "
                    "one an hour later."},
            {"text": "A stretched spring held in a clamp",
             "correct": False,
             "why": "A stretched spring holds an elastic store for as long as "
                    "the clamp holds it."},
            {"text": "Heating a pan on a hob",
             "correct": True},
            {"text": "A drum of diesel in a locked shed",
             "correct": False,
             "why": "A drum of diesel holds a chemical store, and it holds it "
                    "for years."},
        ],
        "figure": None,
    },
    {
        "id": "p1-01-e19",
        "band": "easier",
        "text": "A stone is dropped down a deep well. Which store is filling "
                "on the way down?",
        "options": [
            {"text": "The electrostatic store",
             "correct": False,
             "why": "Nothing separates any charge as a stone drops down a "
                    "shaft."},
            {"text": "The elastic store",
             "correct": False,
             "why": "The stone is not stretched or squashed while it "
                    "falls."},
            {"text": "The gravitational store",
             "correct": False,
             "why": "That store is emptying as the stone gets lower, not "
                    "filling."},
            {"text": "The kinetic store",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p1-01-e20",
        "band": "easier",
        "text": "A gymnast lands on a trampoline and the mat is stretched as "
                "far down as it will go. Which store is full at that instant?",
        "options": [
            {"text": "The elastic store of the mat",
             "correct": True},
            {"text": "The kinetic store of the gymnast",
             "correct": False,
             "why": "At the lowest point the gymnast has stopped moving "
                    "downwards, so that store is empty."},
            {"text": "The chemical store of the mat",
             "correct": False,
             "why": "Nothing in the mat reacts. It is the same fabric "
                    "stretched as it is slack."},
            {"text": "The gravitational store of the gymnast",
             "correct": False,
             "why": "The gymnast is as low as they will get, so that store is "
                    "at its emptiest."},
        ],
        "figure": None,
    },
    {
        "id": "p1-01-e21",
        "band": "easier",
        "text": "A ball is thrown straight up into the air. Which store is "
                "filling as it rises?",
        "options": [
            {"text": "The elastic store",
             "correct": False,
             "why": "The ball is not stretched or squashed once it has left "
                    "the hand."},
            {"text": "The gravitational store",
             "correct": True},
            {"text": "The nuclear store",
             "correct": False,
             "why": "Nothing inside any nucleus changes as a ball flies "
                    "through the air."},
            {"text": "The kinetic store",
             "correct": False,
             "why": "The ball slows down as it rises, so that store is "
                    "emptying rather than filling."},
        ],
        "figure": None,
    },
    {
        "id": "p1-01-e22",
        "band": "easier",
        "text": "Which list contains energy stores only?",
        "options": [
            {"text": "Kinetic, chemical, light",
             "correct": False,
             "why": "Light is a pathway. It carries energy from one store to "
                    "another rather than holding it."},
            {"text": "Thermal, sound, elastic",
             "correct": False,
             "why": "Sound is a pathway. Nothing sits holding sound once the "
                    "room goes quiet."},
            {"text": "Nuclear, magnetic, thermal",
             "correct": True},
            {"text": "Chemical, electrical, kinetic",
             "correct": False,
             "why": "Electrical is a pathway. A current is the route out of a "
                    "battery, not the place it is kept."},
        ],
        "figure": None,
    },
    {
        "id": "p1-01-e23",
        "band": "easier",
        "text": "A candle burns down over an evening. Which store is "
                "emptying?",
        "options": [
            {"text": "The thermal store of the wax",
             "correct": False,
             "why": "The wax gets warmer as the candle burns, so that store "
                    "is filling rather than emptying."},
            {"text": "The elastic store of the wick",
             "correct": False,
             "why": "Nothing in a candle is stretched or squashed at any "
                    "point."},
            {"text": "The kinetic store of the flame",
             "correct": False,
             "why": "A flame flickers, but the energy a candle supplies does "
                    "not come from that movement."},
            {"text": "The chemical store of the wax",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p1-01-e24",
        "band": "easier",
        "text": "A hot oven and a cold fridge stand side by side in a "
                "kitchen. Which of them holds energy in a thermal store?",
        "options": [
            {"text": "Both, because every object has a thermal store",
             "correct": True},
            {"text": "Only the oven, because only warm things have one",
             "correct": False,
             "why": "Every object has a thermal store; a cold one simply has "
                    "less in it than a warm one."},
            {"text": "Only the fridge, because it is holding all the cold",
             "correct": False,
             "why": "Cold is not a thing that can be held. A fridge holds "
                    "less energy, not a store of cold."},
            {"text": "Neither, because neither is being heated at present",
             "correct": False,
             "why": "A thermal store is there whether or not anything is "
                    "heating the object at the time."},
        ],
        "figure": None,
    },
    {
        "id": "p1-01-e25",
        "band": "easier",
        "text": "Is sound a store or a pathway?",
        "options": [
            {"text": "A store, because a loud room holds more sound than a "
                     "quiet one",
             "correct": False,
             "why": "A room holds no sound at all. Stop the speaker and the "
                    "room is silent almost at once."},
            {"text": "A pathway, because sound carries energy through a "
                     "material",
             "correct": True},
            {"text": "A store, because the walls keep the sound that they "
                     "absorb",
             "correct": False,
             "why": "The walls absorb the energy, and what fills is their "
                    "thermal store rather than any store of sound."},
            {"text": "A pathway, because sound always travels faster than "
                     "light",
             "correct": False,
             "why": "Sound is far slower than light, and speed is not what "
                    "makes something a pathway."},
        ],
        "figure": None,
    },
    {
        "id": "p1-01-e26",
        "band": "easier",
        "text": "A student says energy is an invisible fuel that gets poured "
                "from one thing into another. What is the better description?",
        "options": [
            {"text": "It is an invisible gas that spreads out through a room",
             "correct": False,
             "why": "There is no gas. No instrument has ever collected a "
                    "sample of energy."},
            {"text": "It is a very light substance that no balance can weigh",
             "correct": False,
             "why": "It is not a substance at all, however light. There is "
                    "nothing there to weigh."},
            {"text": "It is a number you work out for a situation",
             "correct": True},
            {"text": "It is the force that moves things",
             "correct": False,
             "why": "Force and energy are different quantities, measured in "
                    "newtons and in joules."},
        ],
        "figure": None,
    },
    {
        "id": "p1-01-e27",
        "band": "easier",
        "text": "A bus brakes and comes to a complete stop on a level road. "
                "Which store is emptying as it slows?",
        "options": [
            {"text": "The gravitational store of the bus",
             "correct": False,
             "why": "The road is level, so the bus is no lower at the end "
                    "than it was at the start."},
            {"text": "The chemical store of the fuel",
             "correct": False,
             "why": "The engine is not driving the bus while it brakes; the "
                    "brakes are taking the energy."},
            {"text": "The elastic store of the tyres",
             "correct": False,
             "why": "The tyres squash a little, but that is not where the "
                    "energy of a moving bus sits."},
            {"text": "The kinetic store of the bus",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p1-01-e28",
        "band": "easier",
        "text": "A thundercloud builds up a huge separation of charge before "
                "a flash. Which store is filling?",
        "options": [
            {"text": "The electrostatic store",
             "correct": True},
            {"text": "The kinetic store",
             "correct": False,
             "why": "Movement fills a kinetic store. What a thundercloud "
                    "builds up is separated charge."},
            {"text": "The nuclear store",
             "correct": False,
             "why": "Nothing inside any nucleus changes as a thundercloud "
                    "builds up."},
            {"text": "The elastic store",
             "correct": False,
             "why": "Air can be squashed, but a cloud is not a spring and "
                    "holds nothing that way."},
        ],
        "figure": None,
    },
    {
        "id": "p1-01-e29",
        "band": "easier",
        "text": "Which of these could still be counted if everything in the "
                "universe froze in place?",
        "options": [
            {"text": "The sound coming out of a radio",
             "correct": False,
             "why": "Freeze everything and the sound stops existing; there is "
                    "nothing left to count."},
            {"text": "The chemical store of a battery",
             "correct": True},
            {"text": "The light crossing a dark room",
             "correct": False,
             "why": "Light is a journey. Freeze the world and there is no "
                    "light in transit to count."},
            {"text": "The current flowing through a lamp",
             "correct": False,
             "why": "A current is charge on the move. Stop the motion and "
                    "there is no current left."},
        ],
        "figure": None,
    },
    {
        "id": "p1-01-e30",
        "band": "easier",
        "text": "A bow is drawn and left drawn all night in a rack. What is "
                "true of its elastic store in the morning?",
        "options": [
            {"text": "It has leaked away into the wooden rack overnight",
             "correct": False,
             "why": "Nothing leaks. The bow would fire an arrow in the "
                    "morning exactly as it would have done."},
            {"text": "It has been used up by the effort of staying bent",
             "correct": False,
             "why": "Staying bent uses nothing up. A rack gets no more tired "
                    "than a clamp does."},
            {"text": "It is exactly as full as it was the night before",
             "correct": True},
            {"text": "It has slowly turned into a thermal store in the bow",
             "correct": False,
             "why": "The bow is no warmer in the morning than the room it "
                    "sat in all night."},
        ],
        "figure": None,
    },

    # ── MRB-338 night 3 top-up · standard ────────────────────────────────
    {
        "id": "p1-01-s08",
        "band": "standard",
        "text": "A magnet is pulled off a fridge door and held a few "
                "centimetres away. Which store has been filled, and where "
                "does it sit?",
        "options": [
            {"text": "The magnetic store, shared by the magnet and the door",
             "correct": True},
            {"text": "The elastic store, held in the magnet on its own",
             "correct": False,
             "why": "Neither the magnet nor the door is stretched or squashed "
                    "by being separated."},
            {"text": "The kinetic store, held in the hand that pulled it",
             "correct": False,
             "why": "The hand has stopped by the end, so nothing is left "
                    "moving to hold it."},
            {"text": "The chemical store, held in the steel of the door",
             "correct": False,
             "why": "No substances change. The door is the same steel a "
                    "centimetre away as it was in contact."},
        ],
        "figure": None,
    },
    {
        "id": "p1-01-s09",
        "band": "standard",
        "text": "Two magnets are turned so that they push each other apart, "
                "then forced together and held. What has happened to the "
                "magnetic store?",
        "options": [
            {"text": "It has emptied, because the magnets are now touching",
             "correct": False,
             "why": "Touching is not what decides it. Forcing repelling poles "
                    "together fills the store."},
            {"text": "It has filled, because they were pushed the way they "
                     "resist",
             "correct": True},
            {"text": "It has stayed the same, since nothing was stretched or "
                     "bent",
             "correct": False,
             "why": "Stretching is not the only way to fill a store. Moving "
                    "against a force fills one too."},
            {"text": "It has emptied into the thermal store of the magnets",
             "correct": False,
             "why": "The magnets are no warmer for being held together than "
                    "they were apart."},
        ],
        "figure": None,
    },
    {
        "id": "p1-01-s10",
        "band": "standard",
        "text": "A student rubs a balloon on a jumper for ten seconds. Name "
                "the store that empties and the store that fills.",
        "options": [
            {"text": "The elastic store empties and the electrostatic store "
                     "fills",
             "correct": False,
             "why": "Nothing elastic was loaded first. The rubbing is muscle "
                    "work, not a spring being released."},
            {"text": "The thermal store empties and the electrostatic store "
                     "fills",
             "correct": False,
             "why": "The jumper and the balloon both end up slightly warmer, "
                    "so their thermal stores fill."},
            {"text": "The chemical store empties and the electrostatic store "
                     "fills",
             "correct": True},
            {"text": "The electrostatic store empties and the thermal store "
                     "fills",
             "correct": False,
             "why": "That is the discharge, when the balloon finally loses "
                    "its charge, rather than the rubbing."},
        ],
        "figure": None,
    },
    {
        "id": "p1-01-s11",
        "band": "standard",
        "text": "The particles in a mug of hot tea are moving. Why is the "
                "tea's store called thermal rather than kinetic?",
        "options": [
            {"text": "Because particles are far too small to count as moving",
             "correct": False,
             "why": "Size has nothing to do with it. Small things move, and "
                    "their movement is perfectly real."},
            {"text": "Because a kinetic store can only be filled by a push",
             "correct": False,
             "why": "No push is required. Anything moving has a kinetic "
                    "store, however it came to be moving."},
            {"text": "Because the tea would have to be boiling to count",
             "correct": False,
             "why": "Temperature does not decide which store a name belongs "
                    "to."},
            {"text": "Because the kinetic store counts the whole object "
                     "moving",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p1-01-s12",
        "band": "standard",
        "text": "Which of these situations would still have a full store in a "
                "year's time?",
        "options": [
            {"text": "A drawn crossbow locked in its rack",
             "correct": True},
            {"text": "A kettle of water left boiling on a hob",
             "correct": False,
             "why": "The water would boil dry long before, and its thermal "
                    "store would spread into the kitchen."},
            {"text": "A torch left on in a cupboard",
             "correct": False,
             "why": "The cell would be flat within days, its chemical store "
                    "emptied into the cupboard."},
            {"text": "A ball rolling across a very smooth polished floor",
             "correct": False,
             "why": "No floor is smooth enough. The ball's kinetic store "
                    "empties into the floor and the air."},
        ],
        "figure": None,
    },
    {
        "id": "p1-01-s13",
        "band": "standard",
        "text": "An archer draws a bow and holds it steady at full draw. "
                "Which store emptied and which filled?",
        "options": [
            {"text": "The gravitational store emptied and the elastic store "
                     "filled",
             "correct": False,
             "why": "The archer lowered nothing. Their height is the same at "
                    "full draw as it was before."},
            {"text": "The chemical store emptied and the elastic store "
                     "filled",
             "correct": True},
            {"text": "The elastic store emptied and the kinetic store filled",
             "correct": False,
             "why": "That is the loose, when the arrow flies, rather than the "
                    "draw."},
            {"text": "The kinetic store emptied and the chemical store filled",
             "correct": False,
             "why": "Both halves are the wrong way round. Muscles supply "
                    "energy; they do not collect it."},
        ],
        "figure": None,
    },
    {
        "id": "p1-01-s14",
        "band": "standard",
        "text": "A stone is thrown straight up and is momentarily still at "
                "the very top of its flight. Which store is full and which is "
                "empty?",
        "options": [
            {"text": "Both the kinetic and the gravitational stores are empty",
             "correct": False,
             "why": "The stone is high up, and height alone fills the "
                    "gravitational store."},
            {"text": "The kinetic store is full and the gravitational store "
                     "is empty",
             "correct": False,
             "why": "The stone has stopped for an instant, so there is no "
                    "movement left to count."},
            {"text": "The gravitational store is full and the kinetic store "
                     "is empty",
             "correct": True},
            {"text": "Both stores are full, because the stone is high and "
                     "moving",
             "correct": False,
             "why": "It is not moving at that instant, which is what makes "
                    "the top of the flight special."},
        ],
        "figure": None,
    },
    {
        "id": "p1-01-s15",
        "band": "standard",
        "text": "Two identical cars drive past, one at 30 mph and one at 60 "
                "mph. What can you say about their kinetic stores?",
        "options": [
            {"text": "They are the same, because the cars are identical",
             "correct": False,
             "why": "The cars are identical, but the store counts the "
                    "movement, and one is moving far faster."},
            {"text": "The slower car has more, because it is out longer",
             "correct": False,
             "why": "Time taken does not fill a store. How fast the car is "
                    "going does."},
            {"text": "Neither has one until the brakes are used",
             "correct": False,
             "why": "The store is full while they move; braking is what "
                    "empties it again."},
            {"text": "The faster car has more in its kinetic store",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p1-01-s16",
        "band": "standard",
        "text": "The same parcel is put on a first-floor shelf, and later on "
                "a third-floor shelf. What is true of its gravitational "
                "store?",
        "options": [
            {"text": "It is fuller on the third floor than on the first",
             "correct": True},
            {"text": "It is the same on both, because the parcel is the same",
             "correct": False,
             "why": "The parcel is the same, but the store depends on how "
                    "high it has been raised."},
            {"text": "It is fuller on the first floor, being nearer the "
                     "ground",
             "correct": False,
             "why": "Nearer the ground is emptier, not fuller; there is less "
                    "height left to fall through."},
            {"text": "It is empty on both, because the parcel is not moving",
             "correct": False,
             "why": "Movement fills the kinetic store. A still parcel can "
                    "have a very full gravitational one."},
        ],
        "figure": None,
    },
    {
        "id": "p1-01-s17",
        "band": "standard",
        "text": "A wire carrying a current feels warm. Why is the current "
                "still called a pathway rather than a store?",
        "options": [
            {"text": "Because the warmth proves that the wire is faulty",
             "correct": False,
             "why": "Every wire warms a little when it carries a current. "
                    "That is normal rather than a fault."},
            {"text": "Because the current holds nothing; the warmth is a "
                     "thermal store filling",
             "correct": True},
            {"text": "Because a pathway is any part of a circuit you touch",
             "correct": False,
             "why": "What you can touch has nothing to do with it. A battery "
                    "is touchable and is a store."},
            {"text": "Because the warmth is stored in the current until a "
                     "device calls for it",
             "correct": False,
             "why": "A current holds nothing. Switch off and the current is "
                    "gone at once."},
        ],
        "figure": None,
    },
    {
        "id": "p1-01-s18",
        "band": "standard",
        "text": "A uranium fuel rod in a power station is used up over four "
                "years. Which store has been emptying?",
        "options": [
            {"text": "The chemical store of the uranium",
             "correct": False,
             "why": "Nothing is burning. The change is inside the nuclei, not "
                    "in how the atoms are joined."},
            {"text": "The thermal store of the reactor",
             "correct": False,
             "why": "The reactor's thermal store is filling, so something "
                    "else must be emptying to fill it."},
            {"text": "The nuclear store of the uranium",
             "correct": True},
            {"text": "The electrostatic store of the rod",
             "correct": False,
             "why": "No charge is being separated in a fuel rod."},
        ],
        "figure": None,
    },
    {
        "id": "p1-01-s19",
        "band": "standard",
        "text": "The Sun has shone for about five billion years. Which store "
                "is emptying to keep it going?",
        "options": [
            {"text": "The chemical store of the gases it is made from",
             "correct": False,
             "why": "Nothing burning could last that long. A Sun made of "
                    "burning fuel would be gone in a few thousand years."},
            {"text": "The gravitational store of the Sun",
             "correct": False,
             "why": "The Sun is not falling anywhere, and nothing is lowering "
                    "it."},
            {"text": "The thermal store of the Sun's surface",
             "correct": False,
             "why": "The surface stays at much the same temperature, so "
                    "something must keep refilling it."},
            {"text": "The nuclear store in the Sun's core",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p1-01-s20",
        "band": "standard",
        "text": "A student says the wind has wind energy. Which store does "
                "moving air actually hold?",
        "options": [
            {"text": "The kinetic store of the moving air",
             "correct": True},
            {"text": "The chemical store of the gases that make air",
             "correct": False,
             "why": "Air does not react as it blows. It is the same mixture "
                    "of gases before and after."},
            {"text": "The thermal store of the moving air",
             "correct": False,
             "why": "Air has a thermal store, but blowing is movement, and "
                    "movement is a different store."},
            {"text": "The elastic store of the moving air",
             "correct": False,
             "why": "Air can be squashed, but wind is air travelling rather "
                    "than air compressed."},
        ],
        "figure": None,
    },
    {
        "id": "p1-01-s21",
        "band": "standard",
        "text": "A chemical hand warmer is clicked and becomes hot within a "
                "minute. Describe the change in its stores.",
        "options": [
            {"text": "Its thermal store empties and its chemical store fills",
             "correct": False,
             "why": "Both are the wrong way round. The packet gets hotter, so "
                    "its thermal store is filling."},
            {"text": "Its chemical store empties and its thermal store fills",
             "correct": True},
            {"text": "Its elastic store empties and its thermal store fills",
             "correct": False,
             "why": "The click is a small metal disc snapping, which starts "
                    "the reaction rather than supplying it."},
            {"text": "Its nuclear store empties and its thermal store fills",
             "correct": False,
             "why": "Nothing inside a nucleus changes in a hand warmer."},
        ],
        "figure": None,
    },
    {
        "id": "p1-01-s22",
        "band": "standard",
        "text": "A student labels a moving car with the words movement "
                "energy. Which store name should be used, and what else does "
                "the car hold?",
        "options": [
            {"text": "Kinetic, and it holds nothing else while it moves",
             "correct": False,
             "why": "It also carries fuel and it is warm, so its chemical and "
                    "thermal stores are not empty."},
            {"text": "Elastic, and it also holds a chemical store in its fuel",
             "correct": False,
             "why": "The first half is wrong. A moving car's store is "
                    "kinetic; elastic needs something stretched."},
            {"text": "Kinetic, and it also holds chemical and thermal stores",
             "correct": True},
            {"text": "Kinetic, and everything else about it is a pathway",
             "correct": False,
             "why": "Its fuel and its warmth are both stores, not routes "
                    "energy is travelling along."},
        ],
        "figure": None,
    },
    {
        "id": "p1-01-s23",
        "band": "standard",
        "text": "A bicycle is left leaning against a wall at the top of a "
                "hill for a week. What has happened to its gravitational "
                "store?",
        "options": [
            {"text": "It has drained slowly into the wall it leans on",
             "correct": False,
             "why": "Nothing drains. The wall is doing nothing but holding "
                    "the bicycle up."},
            {"text": "It has emptied, because nothing has moved all week",
             "correct": False,
             "why": "Emptying it means coming down the hill. Standing still "
                    "changes nothing about it."},
            {"text": "It has been used up in holding the bicycle upright",
             "correct": False,
             "why": "Holding something up uses nothing up. A wall does not "
                    "get tired."},
            {"text": "It is exactly as full as it was a week ago",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p1-01-s24",
        "band": "standard",
        "text": "A skateboarder crouches down and then springs upward off "
                "the board. Which stores change?",
        "options": [
            {"text": "Chemical empties; kinetic then gravitational fill",
             "correct": True},
            {"text": "Elastic empties; kinetic then gravitational fill",
             "correct": False,
             "why": "The legs are not a spring loaded from outside. The "
                    "energy comes from the rider's own muscles."},
            {"text": "Gravitational empties; kinetic and thermal stores fill",
             "correct": False,
             "why": "The rider ends higher than they started, so the "
                    "gravitational store fills rather than empties."},
            {"text": "Kinetic empties; chemical and elastic stores fill",
             "correct": False,
             "why": "Every part of that is backwards. Muscles supply the "
                    "energy and the movement is the result."},
        ],
        "figure": None,
    },
    {
        "id": "p1-01-s25",
        "band": "standard",
        "text": "Raising a book fills the gravitational store. Which other "
                "store is filled in the same way, by separating two things "
                "that pull on each other?",
        "options": [
            {"text": "The elastic store",
             "correct": False,
             "why": "An elastic store needs something stretched or squashed, "
                    "not two objects separated."},
            {"text": "The magnetic store",
             "correct": True},
            {"text": "The kinetic store",
             "correct": False,
             "why": "A kinetic store needs movement at the end, and the "
                    "separated objects are then held still."},
            {"text": "The chemical store",
             "correct": False,
             "why": "A chemical store is about which substances are there, "
                    "not about how far apart two objects sit."},
        ],
        "figure": None,
    },
    {
        "id": "p1-01-s26",
        "band": "standard",
        "text": "A student says that only moving things have energy. Which "
                "example refutes that most directly?",
        "options": [
            {"text": "A car engine idling at the kerb",
             "correct": False,
             "why": "An idling engine is full of moving parts, so it does not "
                    "test the claim at all."},
            {"text": "A river running down a valley",
             "correct": False,
             "why": "A river is moving, so it is an example of the claim "
                    "rather than a case against it."},
            {"text": "A stretched catapult lying on a bench",
             "correct": True},
            {"text": "A fan turning slowly in a warm room",
             "correct": False,
             "why": "A turning fan is moving, however slowly, so it cannot "
                    "settle the point either."},
        ],
        "figure": None,
    },
    {
        "id": "p1-01-s27",
        "band": "standard",
        "text": "A goalkeeper catches a fast shot and their hands sting "
                "afterwards. Which store emptied and which filled?",
        "options": [
            {"text": "The chemical store emptied and the kinetic store filled",
             "correct": False,
             "why": "The keeper did not supply the energy; the ball arrived "
                    "carrying it."},
            {"text": "The gravitational store emptied and the thermal store "
                     "filled",
             "correct": False,
             "why": "The shot came in flat and fast rather than dropping from "
                    "a height."},
            {"text": "The elastic store emptied and the kinetic store filled",
             "correct": False,
             "why": "The gloves squash as the ball arrives, so that store "
                    "fills briefly rather than emptying."},
            {"text": "The kinetic store emptied and the thermal store filled",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p1-01-s28",
        "band": "standard",
        "text": "A wrecking ball is hauled back on its chain and released. "
                "From the moment of release, which store empties and which "
                "fills?",
        "options": [
            {"text": "The gravitational store empties and the kinetic store "
                     "fills",
             "correct": True},
            {"text": "The elastic store empties and the kinetic store fills",
             "correct": False,
             "why": "The chain is not a spring. Hauling the ball back raises "
                    "it rather than stretching anything."},
            {"text": "The kinetic store empties and the gravitational store "
                     "fills",
             "correct": False,
             "why": "That is the swing back up on the far side, not the first "
                    "half of the swing."},
            {"text": "The chemical store empties and the gravitational store "
                     "fills",
             "correct": False,
             "why": "That is the hauling, which happens before the ball is "
                    "released."},
        ],
        "figure": None,
    },
    {
        "id": "p1-01-s29",
        "band": "standard",
        "text": "An ice skater stops pushing and glides until they come to a "
                "stop, without using an edge to brake. Which store filled?",
        "options": [
            {"text": "The chemical store of the skater",
             "correct": False,
             "why": "The skater is doing nothing; no substance inside them is "
                    "being made or rearranged."},
            {"text": "The thermal store of the ice and the air",
             "correct": True},
            {"text": "The elastic store of the skates",
             "correct": False,
             "why": "The blades are not stretched or squashed by gliding "
                    "along flat ice."},
            {"text": "The gravitational store of the skater",
             "correct": False,
             "why": "A rink is level, so the skater is no higher at the end "
                    "than at the start."},
        ],
        "figure": None,
    },
    {
        "id": "p1-01-s30",
        "band": "standard",
        "text": "Which store is filled by changes inside a nucleus, and which "
                "by changes in how atoms are joined?",
        "options": [
            {"text": "Chemical inside the nucleus; nuclear in the joins",
             "correct": False,
             "why": "The names are the wrong way round. Nuclear is the one "
                    "that means inside the nucleus."},
            {"text": "Thermal inside the nucleus; chemical in the joins",
             "correct": False,
             "why": "A thermal store is about how warm something is, and has "
                    "nothing to do with nuclei."},
            {"text": "Nuclear inside the nucleus; chemical in the joins",
             "correct": True},
            {"text": "Nuclear inside the nucleus; elastic in the joins",
             "correct": False,
             "why": "The first half is right, but joining atoms is chemistry "
                    "rather than stretching."},
        ],
        "figure": None,
    },

    # ── MRB-338 night 3 top-up · harder ──────────────────────────────────
    {
        "id": "p1-01-h08",
        "band": "harder",
        "text": "A magnet is stuck flat against a fridge door. Is its "
                "magnetic store full or empty, and what would fill it?",
        "options": [
            {"text": "Empty, and pulling it off the door is what fills it",
             "correct": True},
            {"text": "Full, because a magnet is at its strongest when it is "
                     "stuck on",
             "correct": False,
             "why": "A magnet stuck on has already been pulled towards the "
                    "door, so the store has emptied."},
            {"text": "Full, because the magnet is holding up its own weight",
             "correct": False,
             "why": "Holding a weight up is a force, and a force held still "
                    "fills no store at all."},
            {"text": "Empty, and only warming the magnet would ever fill it",
             "correct": False,
             "why": "Warming a magnet fills its thermal store and weakens it; "
                    "it does not fill the magnetic one."},
        ],
        "figure": None,
    },
    {
        "id": "p1-01-h09",
        "band": "harder",
        "text": "One clock is driven by a wound spring and another by a "
                "slowly falling weight. Name the store each one empties.",
        "options": [
            {"text": "Both empty an elastic store as the clock runs",
             "correct": False,
             "why": "Only the spring is bent. The falling weight is not "
                    "stretched or squashed at all."},
            {"text": "Elastic for the spring clock, gravitational for the "
                     "weight clock",
             "correct": True},
            {"text": "Both empty a gravitational store as the clock runs",
             "correct": False,
             "why": "A spring clock works lying flat on a shelf, with nothing "
                    "falling anywhere."},
            {"text": "Elastic for the spring clock, and kinetic for the "
                     "slowly falling weight",
             "correct": False,
             "why": "The weight moves so slowly that its movement is not the "
                    "supply; its height is."},
        ],
        "figure": None,
    },
    {
        "id": "p1-01-h10",
        "band": "harder",
        "text": "A battery left in a drawer for two years is flat when it is "
                "found. A student says that proves chemical is not a real "
                "store. Evaluate that.",
        "options": [
            {"text": "They are right: a real store would keep its energy for "
                     "ever",
             "correct": False,
             "why": "No store is required to be sealed for ever. A store is "
                    "somewhere energy sits and can be counted."},
            {"text": "They are right: the energy was destroyed inside the "
                     "battery",
             "correct": False,
             "why": "Nothing destroyed it. Every joule can be found in the "
                    "battery's own warmth and the air."},
            {"text": "They are wrong: the store emptied slowly into thermal "
                     "stores",
             "correct": True},
            {"text": "They are wrong: a battery in a drawer never goes flat "
                     "at all",
             "correct": False,
             "why": "Batteries do slowly go flat on a shelf, which is exactly "
                    "the fact the student noticed."},
        ],
        "figure": None,
    },
    {
        "id": "p1-01-h11",
        "band": "harder",
        "text": "A student says the energy of a stretched band is in the "
                "rubber, the way water is in a sponge. What is wrong with "
                "that picture?",
        "options": [
            {"text": "Nothing: a stretched band really does hold a substance",
             "correct": False,
             "why": "There is no substance in it. An unstretched band "
                    "contains exactly the same rubber."},
            {"text": "The band holds no energy at all until it is released",
             "correct": False,
             "why": "It holds it the whole time it is stretched, which is why "
                    "it can fire an arrow an hour later."},
            {"text": "The energy sits in the air the rubber squeezed aside",
             "correct": False,
             "why": "The same band stretched in a vacuum holds its store in "
                    "exactly the same way."},
            {"text": "Energy is not a substance, so there is nothing to soak "
                     "up",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p1-01-h12",
        "band": "harder",
        "text": "Lightning flashes between a charged cloud and the ground. "
                "Which store empties, and what are the pathways?",
        "options": [
            {"text": "Electrostatic empties, with light, sound and heating as "
                     "pathways",
             "correct": True},
            {"text": "Electrostatic empties, and light and sound are the "
                     "stores it fills",
             "correct": False,
             "why": "Light and sound are pathways. What fills is a thermal "
                    "store in the air and the ground."},
            {"text": "Thermal empties, with light and sound carrying it to "
                     "the ground",
             "correct": False,
             "why": "The air is far hotter after the flash than before, so "
                    "its thermal store fills."},
            {"text": "Nuclear empties, with light and heating carrying it "
                     "outwards",
             "correct": False,
             "why": "Nothing inside a nucleus changes during a "
                    "thunderstorm."},
        ],
        "figure": None,
    },
    {
        "id": "p1-01-h13",
        "band": "harder",
        "text": "What is the real difference between the nuclear store and "
                "the chemical store?",
        "options": [
            {"text": "The nuclear store is dangerous and the chemical store "
                     "is safe",
             "correct": False,
             "why": "Danger is not what separates them. Petrol holds a "
                    "chemical store and it is not safe."},
            {"text": "One is inside the nucleus; the other is in how atoms "
                     "are joined",
             "correct": True},
            {"text": "The nuclear store holds more joules than a chemical "
                     "store can",
             "correct": False,
             "why": "A tanker of fuel holds far more than a single nucleus, "
                    "so size is not the distinction."},
            {"text": "One of them can be emptied and the other can only be "
                     "filled",
             "correct": False,
             "why": "Both empty. A nuclear store empties in a reactor and a "
                    "chemical store empties in a fire."},
        ],
        "figure": None,
    },
    {
        "id": "p1-01-h14",
        "band": "harder",
        "text": "A student writes that a hot brick contains heat. Which "
                "rewrite says it properly?",
        "options": [
            {"text": "The brick contains heat energy, which it gives out "
                     "slowly",
             "correct": False,
             "why": "There is no store called heat energy. Heating is the "
                    "route, not the place."},
            {"text": "The brick contains hot particles, which are the store "
                     "itself",
             "correct": False,
             "why": "The particles are not the store; the store is the energy "
                    "counted for their movement."},
            {"text": "The brick holds a thermal store, and heating is how it "
                     "empties",
             "correct": True},
            {"text": "The brick holds a thermal pathway, which the room can "
                     "empty",
             "correct": False,
             "why": "The brick holds a store. Heating is the pathway between "
                    "the brick and the room."},
        ],
        "figure": None,
    },
    {
        "id": "p1-01-h15",
        "band": "harder",
        "text": "Why was the older list of light energy, sound energy and "
                "electrical energy replaced by the eight stores?",
        "options": [
            {"text": "Because the newer list has more names, so it covers "
                     "more cases",
             "correct": False,
             "why": "Counting names is not the point. Two of the older names "
                    "were not stores at all."},
            {"text": "Because light, sound and electricity turned out to "
                     "carry no energy",
             "correct": False,
             "why": "All three carry energy. That is exactly what makes them "
                    "pathways."},
            {"text": "Because the older words were too hard for students to "
                     "remember",
             "correct": False,
             "why": "They are the easier words, not the harder ones. The "
                    "trouble was that they were wrong."},
            {"text": "Because the older list named routes as though they were "
                     "places",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p1-01-h16",
        "band": "harder",
        "text": "A student says stores are only a way of talking, since "
                "nobody has ever seen energy. What is the strongest reply?",
        "options": [
            {"text": "The number they give always comes out the same before "
                     "and after",
             "correct": True},
            {"text": "Energy has been seen in a laboratory, using the right "
                     "instrument",
             "correct": False,
             "why": "No instrument detects energy and no laboratory holds a "
                    "sample of it."},
            {"text": "You feel energy directly whenever you pick something "
                     "heavy up",
             "correct": False,
             "why": "What you feel is a force. Force is measured in newtons "
                    "and is a different quantity."},
            {"text": "Stores are only a way of talking, so the student is "
                     "quite right",
             "correct": False,
             "why": "A way of talking that predicts the answer every time is "
                    "a working model, not just talk."},
        ],
        "figure": None,
    },
    {
        "id": "p1-01-h17",
        "band": "harder",
        "text": "How full a chemical store is depends on which of these?",
        "options": [
            {"text": "On how warm the substance happens to be at the moment "
                     "it is weighed",
             "correct": False,
             "why": "A cold biscuit holds the same chemical store as a warm "
                    "one."},
            {"text": "On which substances are there and how their atoms are "
                     "joined",
             "correct": True},
            {"text": "On how fast the substance is moving at the time",
             "correct": False,
             "why": "Movement fills the kinetic store. A biscuit in a moving "
                    "car holds the same chemical store."},
            {"text": "On how high above the ground the substance is",
             "correct": False,
             "why": "Height fills the gravitational store. A biscuit upstairs "
                    "holds the same chemical store."},
        ],
        "figure": None,
    },
    {
        "id": "p1-01-h18",
        "band": "harder",
        "text": "Which example shows best that a store belongs to a situation "
                "rather than to one object on its own?",
        "options": [
            {"text": "A battery holds its chemical store on a shelf for a "
                     "year",
             "correct": False,
             "why": "That shows a store lasts, which is true of every store, "
                    "and tests nothing about how many objects it needs."},
            {"text": "A moving lorry holds a kinetic store while it is moving",
             "correct": False,
             "why": "A kinetic store lasts as long as the movement does, so "
                    "it does not test the point either."},
            {"text": "A raised book only has that store because the Earth is "
                     "there",
             "correct": True},
            {"text": "A hot brick holds a thermal store until the room cools "
                     "it",
             "correct": False,
             "why": "That shows a store emptying, which is a different idea "
                    "from how many objects a store needs."},
        ],
        "figure": None,
    },
    {
        "id": "p1-01-h19",
        "band": "harder",
        "text": "A stretched spring and a rolling cart are each worked out to "
                "hold 12 J. What does that tell you?",
        "options": [
            {"text": "They must hold the same invisible substance, since the "
                     "numbers match",
             "correct": False,
             "why": "There is no substance in either. The number is not a "
                    "measure of any stuff."},
            {"text": "The cart must be moving as fast as the spring is "
                     "stretched",
             "correct": False,
             "why": "Speed and stretch are two different quantities and "
                    "cannot be compared like that."},
            {"text": "One of the two must have been worked out wrongly",
             "correct": False,
             "why": "Two very different situations can genuinely give the "
                    "same number; that is what makes energy useful."},
            {"text": "Energy is a number, and two situations can share one",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p1-01-h20",
        "band": "harder",
        "text": "A student says a ceiling lamp stores light, because the room "
                "is bright while it is on. What single observation settles "
                "it?",
        "options": [
            {"text": "Switch the lamp off and the room is dark at once",
             "correct": True},
            {"text": "Cover the lamp and the light stops reaching your eye",
             "correct": False,
             "why": "Covering it only blocks the light. That says nothing "
                    "about whether the lamp holds any."},
            {"text": "Leave the lamp on and it becomes hot to the touch",
             "correct": False,
             "why": "That shows a thermal store filling, which does not "
                    "settle whether light is stored."},
            {"text": "Change the bulb and the room lights up just as brightly",
             "correct": False,
             "why": "That shows the new bulb works. It says nothing about "
                    "where the light goes."},
        ],
        "figure": None,
    },
    {
        "id": "p1-01-h21",
        "band": "harder",
        "text": "A student calls chemical, thermal and kinetic real stores, "
                "and magnetic and electrostatic unreal ones, because the last "
                "two cannot be felt. Evaluate that.",
        "options": [
            {"text": "They are right: a store you cannot feel is only a way "
                     "of talking",
             "correct": False,
             "why": "You cannot feel a chemical store either, and nobody "
                    "doubts that a battery holds one."},
            {"text": "They are wrong: both really can be counted, and both do "
                     "real work",
             "correct": True},
            {"text": "They are right, because magnets and charges act at a "
                     "distance",
             "correct": False,
             "why": "Acting at a distance is what gravity does, and a raised "
                    "book's store is not in doubt."},
            {"text": "They are wrong: magnetic and electrostatic are both "
                     "pathways",
             "correct": False,
             "why": "Both are stores. Separate two magnets and the energy is "
                    "there to be counted."},
        ],
        "figure": None,
    },
    {
        "id": "p1-01-h22",
        "band": "harder",
        "text": "Which change fills a store without anything moving faster, "
                "getting warmer, or being stretched?",
        "options": [
            {"text": "Striking a match and letting it burn right down",
             "correct": False,
             "why": "That empties a chemical store and fills a thermal one, "
                    "so something certainly gets warmer."},
            {"text": "Pushing a trolley from rest until it is rolling",
             "correct": False,
             "why": "That fills a kinetic store, which is exactly something "
                    "moving faster."},
            {"text": "Lifting a crate slowly onto a high shelf",
             "correct": True},
            {"text": "Bending a steel ruler and then holding it bent",
             "correct": False,
             "why": "That fills an elastic store, which is exactly something "
                    "being bent or stretched."},
        ],
        "figure": None,
    },
    {
        "id": "p1-01-h23",
        "band": "harder",
        "text": "A student writes that a moving lorry has kinetic energy "
                "stored in its engine. What is wrong with where they have put "
                "the store?",
        "options": [
            {"text": "Nothing: the engine makes the lorry move",
             "correct": False,
             "why": "Making it move is the engine's job, but the movement "
                    "that is counted belongs to the whole lorry."},
            {"text": "The store sits in the fuel tank rather than in the "
                     "engine",
             "correct": False,
             "why": "The tank holds a chemical store. The kinetic store is "
                    "about the movement, not the fuel."},
            {"text": "The store sits in the wheels, since they are the parts "
                     "turning",
             "correct": False,
             "why": "The wheels turn, but the whole lorry is moving, and all "
                    "of it is counted."},
            {"text": "A kinetic store belongs to the whole moving lorry",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p1-01-h24",
        "band": "harder",
        "text": "Appliance labels still say electrical energy. Why does that "
                "phrase survive if electricity is not a store?",
        "options": [
            {"text": "It is everyday shorthand for energy arriving by a "
                     "current",
             "correct": True},
            {"text": "Because electricity really is a store once it is inside "
                     "an appliance",
             "correct": False,
             "why": "Nothing in an appliance holds a current. Switch it off "
                    "and there is none left anywhere."},
            {"text": "Because the label means the appliance stores energy "
                     "overnight",
             "correct": False,
             "why": "An unplugged appliance holds nothing, which is why it "
                    "does nothing when the power fails."},
            {"text": "Because scientists agreed to keep two different "
                     "meanings",
             "correct": False,
             "why": "There is one meaning in physics. The label is ordinary "
                    "language, not a second definition."},
        ],
        "figure": None,
    },
    {
        "id": "p1-01-h25",
        "band": "harder",
        "text": "Two identical balls are dropped from 2 m, one onto deep sand "
                "and one onto concrete. Compare the stores at the moment each "
                "one stops.",
        "options": [
            {"text": "The sand ball ends with a fuller thermal store than the "
                     "other",
             "correct": False,
             "why": "Both started with the same gravitational store, so both "
                    "end with the same total in thermal stores."},
            {"text": "Both empty the same gravitational store into thermal "
                     "stores",
             "correct": True},
            {"text": "The concrete ball keeps some kinetic store, because it "
                     "bounces",
             "correct": False,
             "why": "The comparison is the moment each one stops, and a "
                    "stopped ball has no kinetic store."},
            {"text": "The sand ball loses energy and the concrete ball does "
                     "not",
             "correct": False,
             "why": "Neither loses any. In both cases every joule ends up "
                    "somewhere you could point at."},
        ],
        "figure": None,
    },
    {
        "id": "p1-01-h26",
        "band": "harder",
        "text": "A stone is exactly halfway down a well shaft. Where is its "
                "energy at that moment?",
        "options": [
            {"text": "All of it is in the kinetic store, because it is moving",
             "correct": False,
             "why": "It is moving, but it is also still well above the "
                    "bottom, so its gravitational store is not empty."},
            {"text": "All of it is in the gravitational store, being still "
                     "high up",
             "correct": False,
             "why": "It is high, but it is also moving quickly, and that "
                    "movement is counted too."},
            {"text": "Shared between the kinetic and gravitational stores",
             "correct": True},
            {"text": "None of it is anywhere, since it is between two stores",
             "correct": False,
             "why": "Energy is never between stores. At every instant every "
                    "store has a number."},
        ],
        "figure": None,
    },
    {
        "id": "p1-01-h27",
        "band": "harder",
        "text": "A student asks why heating is a pathway when thermal is a "
                "store, since both are about warmth. Which answer is right?",
        "options": [
            {"text": "They are the same thing said twice, so either word will "
                     "do",
             "correct": False,
             "why": "One names a place and the other names a route. They are "
                    "not interchangeable."},
            {"text": "Heating is the store and thermal is the route between "
                     "objects",
             "correct": False,
             "why": "The two are the wrong way round."},
            {"text": "Thermal is used of liquids and heating only of solids",
             "correct": False,
             "why": "Both words apply to any material at all."},
            {"text": "Thermal only names where energy sits; heating names how "
                     "it travels",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p1-01-h28",
        "band": "harder",
        "text": "A student says a magnet's store sits inside the magnet, the "
                "way a battery's chemical store sits inside the battery. What "
                "is the better account?",
        "options": [
            {"text": "The magnetic store belongs to the magnet and what it "
                     "acts on",
             "correct": True},
            {"text": "The magnetic store sits in the metal the magnet is made "
                     "from",
             "correct": False,
             "why": "Change nothing about the metal but move a second magnet "
                    "nearer, and the store changes."},
            {"text": "The magnetic store sits in the air between the two "
                     "magnets",
             "correct": False,
             "why": "Two magnets separated in a vacuum hold their store in "
                    "exactly the same way."},
            {"text": "The magnetic store sits in whichever magnet is the "
                     "stronger",
             "correct": False,
             "why": "Swap which of the two is stronger and the store between "
                    "them is unchanged."},
        ],
        "figure": None,
    },
    {
        "id": "p1-01-h29",
        "band": "harder",
        "text": "A squashed cushion, a stretched band and a bent ruler. How "
                "many different stores are involved?",
        "options": [
            {"text": "Three, because squashing, stretching and bending differ",
             "correct": False,
             "why": "All three change the shape of something that will spring "
                    "back, and that is one store."},
            {"text": "One, because all three will spring back into shape",
             "correct": True},
            {"text": "Two, because bending is really a kind of movement",
             "correct": False,
             "why": "A ruler held bent is not moving at all, and it still "
                    "holds its store."},
            {"text": "None, because only fuels and batteries hold energy",
             "correct": False,
             "why": "There are eight stores, and the elastic store is one of "
                    "them."},
        ],
        "figure": None,
    },
    {
        "id": "p1-01-h30",
        "band": "harder",
        "text": "A student says thermal cannot be a real store, because every "
                "hot object cools down in the end. Evaluate that.",
        "options": [
            {"text": "They are right: a store that empties itself is no store",
             "correct": False,
             "why": "Every store can empty. A battery goes flat and it is "
                    "still a store."},
            {"text": "They are right: the energy is destroyed as things cool",
             "correct": False,
             "why": "Nothing is destroyed. The room ends up very slightly "
                    "warmer by exactly as much."},
            {"text": "They are wrong: cooling is only the store emptying into "
                     "the room",
             "correct": True},
            {"text": "They are wrong: a hot object never cools on its own",
             "correct": False,
             "why": "It does cool. There is nothing wrong with the "
                    "observation, only with the conclusion."},
        ],
        "figure": None,
    },
]
