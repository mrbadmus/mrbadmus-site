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
        "options": [
            {"text": "The chemical store of a battery", "correct": True},
            {"text": "A beam of light crossing a room", "correct": False,
             "why": "Light is a pathway — a way energy travels — not "
                    "somewhere it sits and waits."},
            {"text": "An electric current in a wire", "correct": False,
             "why": "A current carries energy from one store to another. "
                    "Nothing is held in the current itself."},
            {"text": "A sound wave travelling through air", "correct": False,
             "why": "Sound is a pathway too; the energy is on its way from "
                    "one store to another."},
        ],
        "figure": None,
    },
    {
        "id": "p1-01-e06",
        "band": "easier",
        "text": "A mug of hot tea holds energy in which store?",
        "options": [
            {"text": "The chemical store", "correct": False,
             "why": "A chemical store fills when bonds are rearranged, as in "
                    "a battery or a fuel — not by being warmed."},
            {"text": "The thermal store", "correct": True},
            {"text": "The kinetic store", "correct": False,
             "why": "The mug as a whole is not moving. The particles are, and "
                    "that is counted as the thermal store."},
            {"text": "The elastic store", "correct": False,
             "why": "An elastic store fills when something is stretched or "
                    "squashed, which the tea is not."},
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
        "options": [
            {"text": "The elastic store empties and the kinetic store fills",
             "correct": True},
            {"text": "The kinetic store empties and the elastic store fills",
             "correct": False,
             "why": "That is the pull-back, not the release. On release the "
                    "stretched rubber is what empties."},
            {"text": "The chemical store empties and the kinetic store fills",
             "correct": False,
             "why": "Nothing chemical happens in a catapult. The chemical "
                    "store emptied earlier, in the arm that pulled it."},
            {"text": "The elastic store empties and the thermal store fills "
                     "only",
             "correct": False,
             "why": "A little does warm the rubber, but the point of a "
                    "catapult is the kinetic store of the stone."},
        ],
        "figure": None,
    },
    {
        "id": "p1-01-s06",
        "band": "standard",
        "text": "A wind-up radio is cranked and then plays music. Which "
                "sequence of stores is right?",
        "options": [
            {"text": "Chemical in the arm, then elastic in the spring, then "
                     "thermal and sound leaving",
             "correct": True},
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
            {"text": "Thermal in the arm, then kinetic in the spring, then "
                     "chemical in the speaker",
             "correct": False,
             "why": "The muscles empty a chemical store, and a wound spring "
                    "is stretched, so its store is elastic."},
        ],
        "figure": None,
    },
    {
        "id": "p1-01-s07",
        "band": "standard",
        "text": "Why is it wrong to call electricity a store of energy?",
        "options": [
            {"text": "Because electricity is far too fast to be stored "
                     "anywhere",
             "correct": False,
             "why": "Speed has nothing to do with it. A pathway is defined by "
                    "carrying energy, not by how quickly."},
            {"text": "Because an electric current carries energy between "
                     "stores rather than holding it",
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
            {"text": "The gravitational store empties, the kinetic store is "
                     "unchanged, thermal stores in the air fill",
             "correct": True},
            {"text": "The gravitational store empties and the kinetic store "
                     "fills at the same rate",
             "correct": False,
             "why": "The speed is constant, so the kinetic store is not "
                    "changing at all."},
            {"text": "No store changes, because the speed is not changing",
             "correct": False,
             "why": "The skydiver is still losing height, so the "
                    "gravitational store is emptying every second."},
            {"text": "The kinetic store empties into the thermal store of the "
                     "air",
             "correct": False,
             "why": "The kinetic store stays the same size. What is emptying "
                    "is the gravitational store."},
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
            {"text": "Its kinetic store is empty, but its gravitational store "
                     "is at its fullest",
             "correct": True},
            {"text": "It has no energy at all until the brakes are released",
             "correct": False,
             "why": "Being high up is precisely what fills the gravitational "
                    "store; the release only lets it empty."},
            {"text": "Both its stores are empty, because it is not moving",
             "correct": False,
             "why": "Height fills a store whether or not anything is moving, "
                    "which is why the drop works."},
            {"text": "Its kinetic store is full, because it is about to move",
             "correct": False,
             "why": "A store counts what is there now. About to move is not "
                    "moving."},
        ],
        "figure": None,
    },
]
