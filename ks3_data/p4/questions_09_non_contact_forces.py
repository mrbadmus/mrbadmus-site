"""P4 lesson 09 — Non-contact forces: twelve questions (MRB-223).

Written against Design's page. The balloon and the hair, the eight-case
sorter and the three cards are hers.

The discriminations, in the order the lesson builds them:

  · a contact force vanishes the moment the objects separate;
  · air resistance is CONTACT, because particles strike the surface —
    a gap you cannot see is not a gap;
  · gravity only ever attracts, and the other two can repel
    (`FORCE-46`);
  · nothing needs to be in the gap (`FORCE-44`);
  · astronauts float because they are falling, not because gravity has
    gone (`FORCE-45`) — the harder band sits here.

⚠️ POSITION IS AUTHORED — index cycles 2, 3, 1, 0, giving three of each.

⚠️ Rung 1 (which of these is non-contact) and Rung 2 (why astronauts
float) are NOT restated; check 6 of `verify_questions.py` forbids it.
"""

UNIT = "P4"
LESSON = "non-contact-forces"
LESSON_NUMBER = 9

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "p4-09-e01",
        "band": "easier",
        "text": "Which of these is NOT one of the three non-contact forces "
                "named at Key Stage 3?",
        "options": [
            {"text": "Gravity", "correct": False,
             "why": "Gravity is one of the three, and it is the one holding "
                    "you to the planet."},
            {"text": "Magnetism", "correct": False,
             "why": "Magnetism is one of the three — a magnet works "
                    "through paper, air or a vacuum."},
            {"text": "Friction", "correct": True},
            {"text": "The electrostatic force", "correct": False,
             "why": "It is one of the three, and it is the one lifting the "
                    "hair towards the balloon."},
        ],
        "figure": None,
    },
    {
        "id": "p4-09-e02",
        "band": "easier",
        "text": "Which of these can only ever ATTRACT?",
        "options": [
            {"text": "Magnetism", "correct": False,
             "why": "Like poles repel. A magnet can push as well as pull."},
            {"text": "The electrostatic force", "correct": False,
             "why": "Like charges repel. Two rubbed balloons push each other "
                    "apart."},
            {"text": "Friction", "correct": False,
             "why": "Friction is a contact force, and it neither attracts "
                    "nor repels — it resists sliding."},
            {"text": "Gravity", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p4-09-e03",
        "band": "easier",
        "text": "A magnet holds a note to a steel fridge door, and it still "
                "holds with a sheet of paper slipped between them. What does "
                "that show?",
        "options": [
            {"text": "That paper is magnetic.", "correct": False,
             "why": "It is not. The pull is between the magnet and the "
                    "steel, straight through the paper."},
            {"text": "That the force does not need the two to be touching.",
             "correct": True},
            {"text": "That the magnet is stuck by friction against the door",
             "correct": False,
             "why": "Friction needs the surfaces to press together, and it "
                    "would not survive the paper."},
            {"text": "That the note is very light.", "correct": False,
             "why": "It is, but that is not what the paper test shows. The "
                    "test is about whether contact is needed."},
        ],
        "figure": None,
    },
    {
        "id": "p4-09-e04",
        "band": "easier",
        "text": "A magnet is brought near a copper coin and nothing happens. "
                "Why?",
        "options": [
            {"text": "The coin is too heavy.", "correct": False,
             "why": "A steel paperclip of the same mass would jump to it."},
            {"text": "The magnet has run out of magnetism.", "correct": False,
             "why": "The same magnet still attracts iron and steel. Nothing "
                    "about it has been used up."},
            {"text": "The air in between is blocking the pull, so a thicker "
                     "gap would block more of it",
             "correct": False,
             "why": "Magnetism crosses air perfectly well — and a vacuum "
                    "too."},
            {"text": "Copper is not a magnetic material — a magnet does "
                     "not attract all metals.", "correct": True},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "p4-09-s01",
        "band": "standard",
        "text": "Why is air resistance filed as a CONTACT force?",
        "options": [
            {"text": "Because air is heavy enough to press down.",
             "correct": False,
             "why": "Its weight is a separate matter. What makes it contact "
                    "is that it touches the surface."},
            {"text": "Because air is made of particles, and they strike the "
                     "surface.", "correct": True},
            {"text": "Because it only acts on objects that are touching the "
                     "ground.", "correct": False,
             "why": "It acts hardest on things that are touching nothing at "
                    "all — a skydiver, for instance."},
            {"text": "Because it is a kind of friction, and friction is "
                     "contact.", "correct": False,
             "why": "Close, but circular. The reason friction is a contact "
                    "force is the same reason: surfaces touching."},
        ],
        "figure": None,
    },
    {
        "id": "p4-09-s02",
        "band": "standard",
        "text": "A compass needle swings to point north. What kind of force "
                "acts on it, and what does the force DO?",
        "options": [
            {"text": "Gravity, and it pulls the needle down.",
             "correct": False,
             "why": "Gravity does act on the needle, but it is not what "
                    "points it north."},
            {"text": "A contact force from the case, and it turns the "
                     "needle.", "correct": False,
             "why": "Remove the case and the needle still points north. The "
                    "force acts across a gap."},
            {"text": "Magnetism, and it moves the needle sideways.",
             "correct": False,
             "why": "The kind is right. But the needle does not travel "
                    "sideways — it turns on its pivot."},
            {"text": "Magnetism, and it turns the needle — a moment.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p4-09-s03",
        "band": "standard",
        "text": "A rubbed balloon lifts someone's hair across a clear gap of "
                "a centimetre. What could you do to show it is a force "
                "rather than moving air?",
        "options": [
            {"text": "Blow gently at the hair and compare, since moving air "
                     "would do the same job",
             "correct": False,
             "why": "That shows air CAN move hair. It does not rule it out "
                    "as the cause here."},
            {"text": "Hold the balloon perfectly still just above the hair "
                     "and see whether the hair still rises.", "correct": True},
            {"text": "Rub the balloon harder.", "correct": False,
             "why": "That makes the effect bigger, and a moving-air "
                    "explanation would predict the same."},
            {"text": "Use a bigger balloon.", "correct": False,
             "why": "Size changes how much charge it can carry, but it does "
                    "not separate the two explanations."},
        ],
        "figure": None,
    },
    {
        "id": "p4-09-s04",
        "band": "standard",
        "text": "Which pair of objects is the force between, when a stone "
                "falls after being dropped?",
        "options": [
            {"text": "The stone and the air.", "correct": False,
             "why": "Air resistance is real and it is a contact force, but "
                    "it is not what makes the stone fall."},
            {"text": "The stone and your hand.", "correct": False,
             "why": "Your hand's force ended the moment you let go."},
            {"text": "The stone and the Earth.", "correct": True},
            {"text": "The stone and the ground it is heading for.",
             "correct": False,
             "why": "The ground is part of the Earth, but the pull is from "
                    "the whole planet and acts long before contact."},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "p4-09-h01",
        "band": "harder",
        "text": "A magnet attracts a paperclip inside a jar. The air is then "
                "pumped out. What is the modern explanation for the pull "
                "continuing?",
        "options": [
            {"text": "A thin layer of air always remains and carries it.",
             "correct": False,
             "why": "The pull works in a hard vacuum, and between the Earth "
                    "and the Moon, where there is no air to remain."},
            {"text": "The magnet changes the SPACE around it — a field — "
                     "and anything magnetic entering that space feels a "
                     "force.", "correct": True},
            {"text": "The glass of the jar conducts the magnetism.",
             "correct": False,
             "why": "Glass is not magnetic and is doing nothing. Remove the "
                    "jar entirely and the pull is the same."},
            {"text": "The paperclip pulls itself towards the magnet using "
                     "its own magnetism, which the magnet has switched on", "correct": False,
             "why": "It becomes magnetised, but that is half the pair — "
                    "the force still acts between two objects across a gap."},
        ],
        "figure": None,
    },
    {
        "id": "p4-09-h02",
        "band": "harder",
        "text": "Gravity is by far the WEAKEST of the three non-contact "
                "forces — a small magnet beats the whole Earth on a "
                "paperclip. So why is gravity the one that shapes planets "
                "and galaxies?",
        "options": [
            {"text": "Because gravity gets stronger over long distances.",
             "correct": False,
             "why": "It gets weaker with distance, like the others."},
            {"text": "Because gravity acts instantly and the others do not.",
             "correct": False,
             "why": "None of them acts instantly — a change in any field "
                    "spreads at the speed of light."},
            {"text": "Because gravity never repels, so it only ever adds up "
                     "— while the other two come in two signs and nearly "
                     "cancel on any large object.", "correct": True},
            {"text": "Because planets are made of a special kind of matter, "
                     "and ordinary matter does not pull on anything at all "
                     "however much of it there is",
             "correct": False,
             "why": "They are made of ordinary atoms, and every one of them "
                    "pulls."},
        ],
        "figure": None,
    },
    {
        "id": "p4-09-h03",
        "band": "harder",
        "text": "A maglev train floats a centimetre above its track. Sort "
                "the forces on it correctly.",
        "options": [
            {"text": "Lift and drive magnetic; weight gravitational; air "
                     "resistance contact.", "correct": True},
            {"text": "Everything is non-contact, because nothing is "
                     "touching.", "correct": False,
             "why": "Air resistance is still acting and it is a contact "
                    "force — the air particles strike the train."},
            {"text": "Lift is magnetic; everything else is contact.",
             "correct": False,
             "why": "Its weight is the Earth's gravitational pull, which is "
                    "non-contact, and so is the magnetic drive."},
            {"text": "There are no forces on it while it is floating.",
             "correct": False,
             "why": "It has weight, lift, drive and air resistance. It is "
                    "floating because they balance vertically."},
        ],
        "figure": None,
    },
    {
        "id": "p4-09-h04",
        "band": "harder",
        "text": "The space station orbits about 400 km up. Roughly how "
                "strong is the Earth's pull there compared with at ground "
                "level?",
        "options": [
            {"text": "Zero — that is why astronauts float.",
             "correct": False,
             "why": "With zero pull the station would leave in a straight "
                    "line. It is falling, which is why the crew float."},
            {"text": "About a hundredth of it.", "correct": False,
             "why": "Far too small a figure. 400 km is a small addition to "
                    "the Earth's 6 400 km radius."},
            {"text": "About half of it.", "correct": False,
             "why": "Still too weak. You would have to go several thousand "
                    "kilometres up for that."},
            {"text": "Only slightly weaker.", "correct": True},
        ],
        "figure": None,
    },

    # ── MRB-335 top-up · easier ──────────────────────────────────────────
    {
        "id": "p4-09-e05",
        "band": "easier",
        "text": "Which of these materials is attracted to a magnet?",
        "options": [
            {"text": "Copper", "correct": False,
             "why": "Copper is a metal, but not a magnetic one — magnets do "
                    "not attract every metal."},
            {"text": "Steel", "correct": True},
            {"text": "Aluminium", "correct": False,
             "why": "Aluminium is a metal too, and a magnet has no effect on "
                    "it at all."},
            {"text": "Plastic", "correct": False,
             "why": "Plastic is not a metal and is not magnetic, so nothing "
                    "happens."},
        ],
        "figure": None,
    },

    # ── MRB-335 top-up · standard ────────────────────────────────────────
    {
        "id": "p4-09-s05",
        "band": "standard",
        "text": "Two north poles are pushed towards each other and the "
                "magnets resist without ever touching. What does that show?",
        "options": [
            {"text": "That a force can act across a gap with nothing in "
                     "between",
             "correct": True},
            {"text": "That the air between them is being squashed and pushing "
                     "back",
             "correct": False,
             "why": "The same happens with the air pumped out, so the air is "
                    "not what carries it."},
            {"text": "That magnetism only works when the poles are the same",
             "correct": False,
             "why": "Opposite poles attract across a gap just as well; both "
                    "are non-contact."},
            {"text": "That the two magnets are touching at a scale too small "
                     "to see",
             "correct": False,
             "why": "The gap can be centimetres wide and the force still "
                    "acts."},
        ],
        "figure": None,
    },

    # ── MRB-335 top-up · harder ──────────────────────────────────────────
    {
        "id": "p4-09-h05",
        "band": "harder",
        "text": "A satellite circles the Earth with nothing touching it and "
                "its engines off. Which account of the force is right?",
        "options": [
            {"text": "There is no force on it, which is why it keeps going "
                     "round",
             "correct": False,
             "why": "Going round is a constant change of direction, and that "
                    "needs a resultant force."},
            {"text": "A contact force from the thin air up there holds it in "
                     "its path",
             "correct": False,
             "why": "The air is far too thin to steer a satellite, and it "
                    "slows them rather than turning them."},
            {"text": "Gravity acts across the gap and keeps changing its "
                     "direction",
             "correct": True},
            {"text": "Gravity acts across the gap and keeps increasing its "
                     "speed",
             "correct": False,
             "why": "Its speed stays steady; what the force changes is the "
                    "direction it travels in."},
        ],
        "figure": None,
    },

    # ── MRB-338 night 3 expansion · easier ────────────────────────────────
    {
        "id": "p4-09-e06",
        "band": "easier",
        "text": "What is a contact force?",
        "options": [
            {"text": "A force that only acts while two objects are "
                     "touching", "correct": True},
            {"text": "A force that acts across empty space", "correct": False,
             "why": "That describes a non-contact force, the opposite of "
                    "what is being asked."},
            {"text": "A force that just acts on solid objects", "correct": False,
             "why": "Liquids and gases can also exert contact forces, such "
                    "as air resistance."},
            {"text": "A force caused by electricity alone", "correct": False,
             "why": "Many contact forces, like friction and the push of a "
                    "table, have nothing to do with electricity."},
        ],
        "figure": None,
    },
    {
        "id": "p4-09-e07",
        "band": "easier",
        "text": "What is a non-contact force?",
        "options": [
            {"text": "A force that needs the two objects to be pressed together", "correct": False,
             "why": "That describes a CONTACT force. A non-contact force "
                    "needs no touching at all."},
            {"text": "A force that acts across a gap, with nothing needed "
                     "in between", "correct": True},
            {"text": "A force that just acts on magnets", "correct": False,
             "why": "Gravity and the electrostatic force are non-contact "
                    "too, and neither is magnetism-only."},
            {"text": "A force that cannot be measured in newtons", "correct": False,
             "why": "Every non-contact force is measured in newtons, "
                    "exactly like a contact force."},
        ],
        "figure": None,
    },
    {
        "id": "p4-09-e08",
        "band": "easier",
        "text": "Name the three non-contact forces studied at Key Stage 3.",
        "options": [
            {"text": "Friction, tension and air resistance", "correct": False,
             "why": "All three of these are contact forces, not "
                    "non-contact ones."},
            {"text": "Gravity, friction and magnetism", "correct": False,
             "why": "Friction needs the surfaces to be touching, so it "
                    "does not belong on this list."},
            {"text": "Gravity, magnetism and the electrostatic force",
             "correct": True},
            {"text": "Magnetism, tension and the electrostatic force",
             "correct": False,
             "why": "Tension is a contact force — it needs a rope or "
                    "string pulled taut."},
        ],
        "figure": None,
    },
    {
        "id": "p4-09-e09",
        "band": "easier",
        "text": "Why is air resistance classed as a contact force rather "
                "than a non-contact one?",
        "options": [
            {"text": "Because slowing something down is the work of a contact force, and air resistance does nothing else", "correct": False,
             "why": "Non-contact forces can slow things too — gravity, "
                    "for instance, slows a ball thrown upwards."},
            {"text": "Because it is too weak a push to count as one of the real non-contact forces", "correct": False,
             "why": "How strong a force is has nothing to do with whether "
                    "it needs contact."},
            {"text": "Because it just acts on objects that are falling",
             "correct": False,
             "why": "Air resistance acts on anything moving through air, "
                    "falling or not."},
            {"text": "Because air is made of particles, and they "
                     "physically strike the surface", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p4-09-e10",
        "band": "easier",
        "text": "Friction is a…",
        "options": [
            {"text": "contact force, because it needs two surfaces "
                     "touching", "correct": True},
            {"text": "non-contact force, because you cannot see the "
                     "surfaces touching", "correct": False,
             "why": "The surfaces genuinely are touching, even if the "
                    "contact is too fine to see clearly."},
            {"text": "non-contact force, because it can act through the "
                     "air", "correct": False,
             "why": "Friction only exists between surfaces that are in "
                    "contact with each other."},
            {"text": "contact force, but just between two magnets",
             "correct": False,
             "why": "Friction has nothing to do with magnets — it happens "
                    "between any two touching surfaces."},
        ],
        "figure": None,
    },
    {
        "id": "p4-09-e11",
        "band": "easier",
        "text": "The tension in a stretched rope is a…",
        "options": [
            {"text": "non-contact force, because the rope can be very long", "correct": False,
             "why": "Length makes no difference — tension needs the rope "
                    "to be attached and pulled taut."},
            {"text": "contact force, because the rope is touching whatever "
                     "it is attached to", "correct": True},
            {"text": "non-contact force, because ropes are flexible",
             "correct": False,
             "why": "Flexibility has nothing to do with whether contact "
                    "is needed."},
            {"text": "contact force, but just in ropes made of metal wire",
             "correct": False,
             "why": "Tension works the same way whatever the rope is made "
                    "from, as long as it is touching."},
        ],
        "figure": None,
    },
    {
        "id": "p4-09-e12",
        "band": "easier",
        "text": "A book presses down on a table, and the table pushes back "
                "up on the book. What kind of force is this?",
        "options": [
            {"text": "Non-contact, because the book and table are separate objects", "correct": False,
             "why": "Being separate objects is not the test — whether "
                    "they are touching is."},
            {"text": "Non-contact, because the push is invisible",
             "correct": False,
             "why": "Many contact forces are invisible to look at, but "
                    "this one is still delivered by direct touching."},
            {"text": "Contact, because the book and table are pressed "
                     "together", "correct": True},
            {"text": "Contact, but just because the table is made of wood", "correct": False,
             "why": "The material the table is made from makes no "
                    "difference — what matters is that the two are "
                    "touching."},
        ],
        "figure": None,
    },
    {
        "id": "p4-09-e13",
        "band": "easier",
        "text": "Which of these materials would a magnet attract?",
        "options": [
            {"text": "Gold", "correct": False,
             "why": "Gold is a metal, but it is not magnetic."},
            {"text": "Brass", "correct": False,
             "why": "Brass is a metal, but it is not magnetic either."},
            {"text": "Aluminium", "correct": False,
             "why": "Aluminium is a common metal, and a magnet has no "
                    "effect on it."},
            {"text": "Nickel", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p4-09-e14",
        "band": "easier",
        "text": "What do the electrostatic force and magnetism have in "
                "common, that gravity does not?",
        "options": [
            {"text": "They can both push things apart as well as pull "
                     "them together", "correct": True},
            {"text": "They just work in a vacuum", "correct": False,
             "why": "Both work perfectly well in air, or through paper, "
                    "or through a vacuum."},
            {"text": "They both need a battery to work", "correct": False,
             "why": "Rubbing a balloon or bringing a magnet near iron "
                    "needs no battery at all."},
            {"text": "They are both types of friction", "correct": False,
             "why": "Friction is a contact force; these two act across a "
                    "gap."},
        ],
        "figure": None,
    },
    {
        "id": "p4-09-e15",
        "band": "easier",
        "text": "A rubbed balloon and a piece of fur, or a plastic comb and "
                "dry hair, both produce the same effect. What is that "
                "effect called?",
        "options": [
            {"text": "Magnetism", "correct": False,
             "why": "Rubbing plastic does not make it magnetic — it only "
                    "produces the electrostatic force."},
            {"text": "The electrostatic force", "correct": True},
            {"text": "Gravity", "correct": False,
             "why": "Rubbing has no effect on gravity, which depends only "
                    "on mass."},
            {"text": "Air resistance", "correct": False,
             "why": "Air resistance is caused by moving through air, not "
                    "by rubbing two dry materials together."},
        ],
        "figure": None,
    },
    {
        "id": "p4-09-e16",
        "band": "easier",
        "text": "What happens to the electrostatic force on a rubbed "
                "balloon after a while?",
        "options": [
            {"text": "It gets stronger the longer you wait", "correct": False,
             "why": "The charge does not build up by itself once the "
                    "rubbing has stopped."},
            {"text": "It turns into magnetism", "correct": False,
             "why": "The electrostatic force and magnetism are two "
                    "separate forces; one does not become the other."},
            {"text": "It fades away as the charge leaks away", "correct": True},
            {"text": "It stays exactly the same forever", "correct": False,
             "why": "The charge on the balloon gradually leaks away, and "
                    "the force fades with it."},
        ],
        "figure": None,
    },
    {
        "id": "p4-09-e17",
        "band": "easier",
        "text": "A magnet is brought near a steel paperclip inside a sealed "
                "glass jar with all the air pumped out. What happens?",
        "options": [
            {"text": "Nothing, because a vacuum blocks magnetism completely", "correct": False,
             "why": "Magnetism crosses a vacuum perfectly well — that is "
                    "exactly what happens between the Earth and the "
                    "Moon."},
            {"text": "The paperclip melts, because the vacuum makes it very hot", "correct": False,
             "why": "Pumping the air out has no effect on temperature."},
            {"text": "The magnet loses its magnetism instantly", "correct": False,
             "why": "A magnet's own magnetism does not depend on there "
                    "being air around it."},
            {"text": "The paperclip is still attracted to the magnet",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p4-09-e18",
        "band": "easier",
        "text": "Which of these can gravity NEVER do?",
        "options": [
            {"text": "Push two objects apart", "correct": True},
            {"text": "Act between two planets", "correct": False,
             "why": "Gravity acts between any two objects that have "
                    "mass, including planets."},
            {"text": "Get weaker over a larger distance", "correct": False,
             "why": "Gravity really does get weaker the further apart two "
                    "objects are."},
            {"text": "Act on something with no other forces touching it",
             "correct": False,
             "why": "That is exactly what gravity does — it needs no "
                    "contact at all."},
        ],
        "figure": None,
    },
    {
        "id": "p4-09-e19",
        "band": "easier",
        "text": "What does gravity act between?",
        "options": [
            {"text": "Only very large objects, like planets and moons",
             "correct": False,
             "why": "Gravity acts between ANY two objects with mass, "
                    "however small — it is just too weak to notice "
                    "between small everyday objects."},
            {"text": "Anything that has mass", "correct": True},
            {"text": "Only objects that are magnetic", "correct": False,
             "why": "Gravity has nothing to do with whether something is "
                    "magnetic."},
            {"text": "Only objects on Earth", "correct": False,
             "why": "Gravity also holds the Moon in orbit and holds the "
                    "planets around the Sun."},
        ],
        "figure": None,
    },
    {
        "id": "p4-09-e20",
        "band": "easier",
        "text": "Tides in the sea rise and fall partly because of the pull "
                "of the Moon on the ocean. What kind of force is this?",
        "options": [
            {"text": "A contact force, because the sea touches the shore",
             "correct": False,
             "why": "The Moon is not touching the sea at all — its pull "
                    "acts right across the gap of space."},
            {"text": "The electrostatic force, because water conducts electricity", "correct": False,
             "why": "The Moon's pull on the sea is not related to "
                    "electric charge at all."},
            {"text": "Gravity, acting across the gap between the Moon and "
                     "the Earth", "correct": True},
            {"text": "Magnetism, because the Moon is attracted to metal "
                     "in the sea", "correct": False,
             "why": "Seawater is not particularly magnetic, and the "
                    "Moon's pull works on any mass, not just magnetic "
                    "material."},
        ],
        "figure": None,
    },
    {
        "id": "p4-09-e21",
        "band": "easier",
        "text": "A doctor's surgery has old-fashioned scales that use a "
                "spring inside to show your weight. What force is being "
                "measured?",
        "options": [
            {"text": "The contact force between your feet and the scale's platform", "correct": False,
             "why": "That contact force exists, but the reading itself "
                    "is standing in for a different force altogether."},
            {"text": "The electrostatic force between you and the floor",
             "correct": False,
             "why": "Standing on scales has nothing to do with electric "
                    "charge."},
            {"text": "The magnetism between you and the Earth", "correct": False,
             "why": "Your body is not attracted to the Earth by "
                    "magnetism — very little of a person is magnetic "
                    "material."},
            {"text": "Gravity, the pull of the Earth on your mass",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p4-09-e22",
        "band": "easier",
        "text": "Which everyday device works by attracting tiny particles "
                "of toner powder onto paper using static electricity?",
        "options": [
            {"text": "A photocopier", "correct": True},
            {"text": "A fridge magnet", "correct": False,
             "why": "A fridge magnet works through magnetism, not "
                    "electrostatic attraction, and it does not use toner "
                    "powder."},
            {"text": "A kettle", "correct": False,
             "why": "A kettle simply heats water and has nothing to do "
                    "with electrostatic attraction."},
            {"text": "A torch", "correct": False,
             "why": "A torch produces light from a battery and bulb, "
                    "with no electrostatic attraction involved."},
        ],
        "figure": None,
    },
    {
        "id": "p4-09-e23",
        "band": "easier",
        "text": "Clothes taken straight from a tumble dryer sometimes cling "
                "together. What force causes this?",
        "options": [
            {"text": "Gravity, since a tumble dryer's drum spins the clothes and gravity pulls them back down",
             "correct": False,
             "why": "Gravity would pull clothes down and apart, not stick "
                    "them to each other."},
            {"text": "The electrostatic force, built up by the clothes "
                     "rubbing together", "correct": True},
            {"text": "Magnetism, since the metal drum magnetises the "
                     "fabric as it spins", "correct": False,
             "why": "Fabric is not normally magnetic, however much it "
                    "has been tumbled."},
            {"text": "Friction, which keeps acting on the clothes after "
                     "the drum has stopped turning", "correct": False,
             "why": "Friction happens while the clothes are moving and "
                    "rubbing, but the clinging afterwards is a different, "
                    "non-contact force."},
        ],
        "figure": None,
    },
    {
        "id": "p4-09-e24",
        "band": "easier",
        "text": "Which of these is an example of a magnetic material?",
        "options": [
            {"text": "Copper", "correct": False,
             "why": "Copper is a metal, but magnets have no effect on "
                    "it."},
            {"text": "Plastic", "correct": False,
             "why": "Plastic is not a metal and is not magnetic."},
            {"text": "Cobalt", "correct": True},
            {"text": "Wood", "correct": False,
             "why": "Wood is not a metal and is not magnetic."},
        ],
        "figure": None,
    },
    {
        "id": "p4-09-e25",
        "band": "easier",
        "text": "What is the correct way to describe how the electrostatic "
                "force starts on a balloon rubbed against a jumper?",
        "options": [
            {"text": "The rubbing creates brand new charge out of nothing, adding to the total charge in the room", "correct": False,
             "why": "Rubbing does not create charge from nothing — it "
                    "moves existing charge from one surface to the "
                    "other."},
            {"text": "The rubbing heats the balloon until it becomes charged by the warmth", "correct": False,
             "why": "Heat is not what causes this — it is the physical "
                    "transfer of charge between the two surfaces."},
            {"text": "The rubbing makes the balloon magnetic instead of electrically charged", "correct": False,
             "why": "Rubbing a balloon never makes it magnetic; it "
                    "produces the electrostatic force instead."},
            {"text": "The rubbing moves electric charge from the jumper "
                     "onto the balloon", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p4-09-e26",
        "band": "easier",
        "text": "A field, in the sense used for any of the non-contact forces, is best described as…",
        "options": [
            {"text": "the region of space around an object where its "
                     "force can be felt", "correct": True},
            {"text": "a type of contact force that happens to act at a "
                     "short range", "correct": False,
             "why": "A field is exactly what makes contact unnecessary — "
                    "it is central to how non-contact forces work."},
            {"text": "a measurement of an object's weight, given in a "
                     "different unit", "correct": False,
             "why": "Weight is a force in newtons; a field is the region "
                    "of space where a force can act."},
            {"text": "a solid, physical material that carries the force "
                     "across the gap", "correct": False,
             "why": "Nothing solid needs to be present — the modern "
                    "explanation is a field, not a substance."},
        ],
        "figure": None,
    },
    {
        "id": "p4-09-e27",
        "band": "easier",
        "text": "Which pair correctly matches a force to what it fades "
                "away with, over time?",
        "options": [
            {"text": "Gravity fades as its own charge slowly leaks away",
             "correct": False,
             "why": "Gravity has no charge to leak away — it depends "
                    "only on mass, which does not disappear on its own."},
            {"text": "The electrostatic force fades as its charge leaks "
                     "away", "correct": True},
            {"text": "Magnetism fades as the magnet's own poles wear out "
                     "with age", "correct": False,
             "why": "A magnet's poles do not wear out simply from "
                    "sitting there — a magnet can stay magnetic for a "
                    "very long time."},
            {"text": "All three non-contact forces fade at exactly the "
                     "same steady rate", "correct": False,
             "why": "They do not fade in the same way — gravity does not "
                    "fade with time the way charge does."},
        ],
        "figure": None,
    },
    {
        "id": "p4-09-e28",
        "band": "easier",
        "text": "The push you feel from a swimming pool's water when you "
                "kick against it is a…",
        "options": [
            {"text": "non-contact force, because water is a liquid and not a solid", "correct": False,
             "why": "Being a liquid does not make it non-contact — the "
                    "water is still physically touching your leg."},
            {"text": "non-contact force, because the push happens while you are underwater", "correct": False,
             "why": "Location does not decide it — what matters is that "
                    "the water and your leg are touching."},
            {"text": "contact force, because the water is touching your "
                     "leg", "correct": True},
            {"text": "a type of gravity acting sideways instead of "
                     "downwards", "correct": False,
             "why": "Gravity is a completely separate, non-contact force "
                    "between masses, not the push of water against your "
                    "leg."},
        ],
        "figure": None,
    },
    {
        "id": "p4-09-e29",
        "band": "easier",
        "text": "What is the correct way to describe the force between "
                "two magnets placed with their north poles facing each "
                "other?",
        "options": [
            {"text": "Contact, because the poles are held close together on purpose", "correct": False,
             "why": "The poles do not have to touch for the force to act "
                    "— it works perfectly well across a gap."},
            {"text": "Non-contact, but just if the magnets happen to be touching", "correct": False,
             "why": "This contradicts itself — a non-contact force is "
                    "defined by NOT needing the objects to touch."},
            {"text": "Gravity acting between the two nearby magnets",
             "correct": False,
             "why": "Any two masses do attract by gravity, but the much "
                    "stronger force here between like poles is "
                    "magnetism."},
            {"text": "Non-contact, because like poles repel across a gap",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p4-09-e30",
        "band": "easier",
        "text": "A wireless charging pad can charge a phone's battery "
                "without any cable plugged into the phone. What kind of "
                "force makes this possible?",
        "options": [
            {"text": "A non-contact force, transferring energy across the "
                     "small gap between the pad and the phone",
             "correct": True},
            {"text": "A contact force, since the phone is simply resting "
                     "on top of the pad", "correct": False,
             "why": "The phone resting on the pad is not what does the "
                    "charging — the energy crosses the gap using a "
                    "non-contact effect."},
            {"text": "Friction between the phone's case and the surface "
                     "of the pad", "correct": False,
             "why": "Friction plays no part in wireless charging."},
            {"text": "Air resistance slowing the electricity down as it "
                     "crosses the gap", "correct": False,
             "why": "Air resistance acts on objects moving through air; "
                    "it has nothing to do with charging a battery."},
        ],
        "figure": None,
    },

    # ── MRB-338 night 3 expansion · standard ───────────────────────────────
    {
        "id": "p4-09-s06",
        "band": "standard",
        "text": "A fridge magnet holds a note against a steel door even "
                "with a sheet of card slipped in between. A friend argues "
                "this must be a contact force because the magnet is "
                "touching the card. What is wrong with that argument?",
        "options": [
            {"text": "The magnet is touching the card, not the door — "
                     "the pull on the door acts straight through the "
                     "card and the gap", "correct": True},
            {"text": "Nothing is wrong, because the magnet passes its pull along through the card and into the door by touching it",
             "correct": False,
             "why": "Whether the magnet touches the card is beside the "
                    "point; what matters is that no touching is needed "
                    "between the magnet and the steel door it is "
                    "pulling on."},
            {"text": "The card being there proves the force must be electrostatic instead of magnetic, as card builds up charge", "correct": False,
             "why": "Nothing about a card changes which force is at "
                    "work — it is still magnetism, and it still crosses "
                    "the gap."},
            {"text": "The argument is correct, because the pull would stop with a thick enough card in the way to hold them both apart",
             "correct": False,
             "why": "The pull continues however thick the card, right up "
                    "to the point the magnet is simply too far away — "
                    "thickness does not turn a non-contact force into a "
                    "contact one."},
        ],
        "figure": None,
    },
    {
        "id": "p4-09-s07",
        "band": "standard",
        "text": "A satellite dish is bolted firmly to the side of a "
                "house, and gravity pulls down on both the dish and the "
                "house. Someone claims gravity must be a contact force "
                "here, since the dish is touching the house. What is the "
                "flaw in that claim?",
        "options": [
            {"text": "There is no flaw, because the dish feels the pull of gravity through the solid bolts that join it to the house and to the ground below", "correct": False,
             "why": "Gravity is non-contact wherever it acts, whether or "
                    "not the two objects happen to also be touching for "
                    "an unrelated reason."},
            {"text": "The dish and house touching each other is "
                     "irrelevant — gravity pulls each of them down from "
                     "the Earth, across the gap to the planet",
             "correct": True},
            {"text": "The claim is correct because the dish is made of metal, and metal carries gravity between whatever it touches", "correct": False,
             "why": "The material the dish is made from makes no "
                    "difference to how gravity behaves."},
            {"text": "Gravity does not act on bolted-down objects like this dish, because the bolts leave it with no weight of its own", "correct": False,
             "why": "Gravity acts on every object with mass, bolted down "
                    "or not."},
        ],
        "figure": None,
    },
    {
        "id": "p4-09-s08",
        "band": "standard",
        "text": "A student sorts 'the push of a table on a book' and 'the "
                "pull of a magnet on a fridge door' into the same "
                "category, both labelled non-contact. What has gone "
                "wrong?",
        "options": [
            {"text": "Nothing, because the table's push reaches the book across the thin layer of air between the two", "correct": False,
             "why": "The push of the table needs the book and table to "
                    "be touching, which makes it a CONTACT force."},
            {"text": "The magnet example should instead be moved into the contact category", "correct": False,
             "why": "The magnet's pull on the door does not need "
                    "touching, so non-contact is the correct label for "
                    "it."},
            {"text": "The table example should instead be sorted as "
                     "contact, since the book and table are touching",
             "correct": True},
            {"text": "Both examples should be sorted as gravity, since every push or pull we meet comes from the Earth", "correct": False,
             "why": "Neither of these examples is gravity — one is a "
                    "contact push, the other is magnetism."},
        ],
        "figure": None,
    },
    {
        "id": "p4-09-s09",
        "band": "standard",
        "text": "Explain why a compass needle points north even when it "
                "is sealed inside a plastic case.",
        "options": [
            {"text": "Because plastic conducts magnetism perfectly, carrying the pull along the case and into the needle inside it",
             "correct": False,
             "why": "Plastic does not need to conduct anything — "
                    "magnetism, as a non-contact force, does not need a "
                    "conducting path at all."},
            {"text": "Because the needle inside is touching the Earth through the plastic case and the bench it rests on, giving the pull a path to travel along", "correct": False,
             "why": "The needle is nowhere near touching the Earth — the "
                    "force crosses the whole distance as a genuine "
                    "non-contact force."},
            {"text": "Because the plastic case is thin enough to let a small amount of contact through to the needle, which is all a magnetic pull needs", "correct": False,
             "why": "No amount of thinness is relevant — a non-contact "
                    "force does not need any contact, however small a "
                    "gap remains."},
            {"text": "Because magnetism is a non-contact force and can "
                     "act straight through non-magnetic materials like "
                     "plastic", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p4-09-s10",
        "band": "standard",
        "text": "A student says: 'Non-contact forces must be weaker than "
                "contact forces, since they don't even need to touch.' "
                "Evaluate this claim using an example.",
        "options": [
            {"text": "It's false — a large crane's electromagnet can "
                     "lift a whole car, easily overpowering the small "
                     "contact force of the car's weight on the ground",
             "correct": True},
            {"text": "It's true, because a force crossing a gap has to spread itself out over that whole distance, which leaves it far too weak to lift a whole car up",
             "correct": False,
             "why": "An electromagnet lifting a car shows a non-contact "
                    "force can be very strong indeed."},
            {"text": "It's true for gravity, the weakest of the three non-contact forces, and the other two behave in the same way as it does",
             "correct": False,
             "why": "Gravity being weak does not make the general claim "
                    "true — magnetism and the electrostatic force are "
                    "non-contact too, and can be very strong."},
            {"text": "It cannot be tested, because contact and non-contact forces are measured on two different scales that will not line up",
             "correct": False,
             "why": "Forces of any kind are measured in newtons, so they "
                    "can always be compared directly."},
        ],
        "figure": None,
    },
    {
        "id": "p4-09-s11",
        "band": "standard",
        "text": "A rubbed party balloon sticks to a wall for a while, "
                "then falls off later. Explain both parts of what "
                "happens, using the word 'charge'.",
        "options": [
            {"text": "The balloon becomes magnetic when rubbed, then loses that magnetism gradually as the rubber cools back down",
             "correct": False,
             "why": "Rubbing a balloon does not make it magnetic — it "
                    "transfers electric charge, a different force "
                    "entirely."},
            {"text": "Rubbing transfers charge onto the balloon, which "
                     "attracts the wall; it falls once enough of that "
                     "charge has leaked away", "correct": True},
            {"text": "The balloon sticks because rubbing lowers the air pressure behind it, and it falls as that pressure slowly creeps back up",
             "correct": False,
             "why": "Air pressure plays no part here — both the sticking "
                    "and the falling are explained by electric charge "
                    "building up and then leaking away."},
            {"text": "The wall pulls the balloon in by gravity, and lets "
                     "go once the wall gets tired of holding it",
             "correct": False,
             "why": "Gravity would only ever pull the balloon downward, "
                    "and it does not weaken with time the way this "
                    "describes."},
        ],
        "figure": None,
    },
    {
        "id": "p4-09-s12",
        "band": "standard",
        "text": "A physics teacher demonstrates that a magnet held above "
                "a paperclip on a table will lift it clean off the "
                "surface. Explain why this shows the magnetic force must "
                "be bigger than the paperclip's weight at that moment.",
        "options": [
            {"text": "It doesn't show that, because the paperclip is picked up by the static electricity gathered on the magnet as it is moved about", "correct": False,
             "why": "Static electricity plays no part in a "
                    "straightforward magnet-and-paperclip demonstration."},
            {"text": "It shows the paperclip has temporarily lost its own weight, because the magnet has taken over from the Earth the job of holding it", "correct": False,
             "why": "The paperclip's weight, caused by gravity, does not "
                    "change at all during this demonstration."},
            {"text": "For the paperclip to leave the table, the upward "
                     "magnetic pull on it must be bigger than the "
                     "downward pull of gravity on it", "correct": True},
            {"text": "It shows that contact forces are generally stronger than non-contact forces overall", "correct": False,
             "why": "This example shows the exact opposite — a "
                    "non-contact force here overcomes gravity acting on "
                    "the paperclip's weight."},
        ],
        "figure": None,
    },
    {
        "id": "p4-09-s13",
        "band": "standard",
        "text": "A model rocket, once launched, is acted on by gravity, "
                "air resistance, and (while the engine burns) thrust from "
                "the exhaust. Sort these three by whether each is contact "
                "or non-contact, and explain your reasoning.",
        "options": [
            {"text": "All three are non-contact, because a rocket in the air is not touching the ground that each of its forces comes from",
             "correct": False,
             "why": "Not touching the ground is irrelevant — air "
                    "resistance and thrust both involve direct contact "
                    "with particles of air or exhaust gas."},
            {"text": "Gravity and thrust are contact forces, and air resistance is the non-contact one", "correct": False,
             "why": "This has it backwards — thrust and air resistance "
                    "both involve particles striking a surface, making "
                    "them contact, while gravity needs no touching at "
                    "all."},
            {"text": "All three are contact forces, because the rocket is a physical object and every force on it has to be delivered by something it touches", "correct": False,
             "why": "Gravity acts on the rocket across a gap from the "
                    "Earth, with nothing physically touching it to cause "
                    "that pull."},
            {"text": "Gravity is non-contact; air resistance and thrust "
                     "are both contact, since both involve particles "
                     "striking a surface", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p4-09-s14",
        "band": "standard",
        "text": "Why can two bar magnets be made to attract OR repel each "
                "other, while two objects attracting by gravity can never "
                "be made to repel?",
        "options": [
            {"text": "Magnetism has two kinds of pole that can be "
                     "matched or mismatched; mass has no equivalent "
                     "'negative' version to reverse the pull",
             "correct": True},
            {"text": "Because magnets are stronger than gravity, so a magnet can overpower the Earth's own pull on a nearby magnet and turn it into a push", "correct": False,
             "why": "Strength has nothing to do with WHETHER a force can "
                    "repel — it is about whether the force has two "
                    "opposite kinds, like poles or charges."},
            {"text": "Because gravity works on Earth alone, while magnets keep working far out in space where there is nothing to pull on", "correct": False,
             "why": "Gravity works everywhere there is mass, not only on "
                    "Earth — that is not the reason for the difference."},
            {"text": "Because magnets need batteries to work and gravity "
                     "does not need one", "correct": False,
             "why": "No magnet needs a battery to be magnetic — a "
                    "permanent magnet works without any power source."},
        ],
        "figure": None,
    },
    {
        "id": "p4-09-s15",
        "band": "standard",
        "text": "A small fridge magnet can lift a paperclip off a table, "
                "easily beating the whole Earth's gravitational pull on "
                "that same paperclip. Explain how this can be true.",
        "options": [
            {"text": "It can't be true, because the Earth is so much bigger than the magnet that its pull on a small paperclip has to be the stronger of them", "correct": False,
             "why": "It genuinely happens, and it is a standard "
                    "demonstration of just how weak gravity is compared "
                    "with magnetism at short range."},
            {"text": "Gravity is an extremely weak force compared with "
                     "magnetism, so at short range a small magnet's pull "
                     "easily outdoes the whole planet", "correct": True},
            {"text": "The paperclip briefly loses its own weight while the magnet is held nearby", "correct": False,
             "why": "The paperclip's weight, caused by gravity, does not "
                    "change — the magnet simply supplies a bigger force "
                    "in the opposite direction."},
            {"text": "The Earth's gravity acts on very large objects like planets and moons, and is far too spread out to reach something as small as a paperclip", "correct": False,
             "why": "Gravity acts on the paperclip too, just far more "
                    "weakly than the nearby magnet's pull."},
        ],
        "figure": None,
    },
    {
        "id": "p4-09-s16",
        "band": "standard",
        "text": "Explain why gravity, despite being the weakest of the "
                "three non-contact forces, is the one that shapes the "
                "orbits of every planet in the solar system.",
        "options": [
            {"text": "Because gravity gets much stronger over very large distances, unlike the other two non-contact forces, which fade away after a few metres",
             "correct": False,
             "why": "Gravity actually gets WEAKER with distance, exactly "
                    "like magnetism and the electrostatic force."},
            {"text": "Because the Sun itself is magnetic, as well as having gravity of its own", "correct": False,
             "why": "The Sun's gravity, not its magnetism, is what holds "
                    "the planets in orbit — that is the force being "
                    "asked about here."},
            {"text": "Because gravity only ever attracts and never "
                     "cancels out, so the pull of every particle of mass "
                     "adds up across a whole planet or star",
             "correct": True},
            {"text": "Because planets carry no electric charge and no magnetism of their own, leaving gravity as the one force with anything left to act on out in space",
             "correct": False,
             "why": "Planets do contain charge, but on the huge scale of "
                    "a solar system the charges balance out, unlike "
                    "gravity, which never does."},
        ],
        "figure": None,
    },
    {
        "id": "p4-09-s17",
        "band": "standard",
        "text": "A wireless phone charger, an induction hob, and a "
                "maglev train's lifting magnets all rely on the same "
                "underlying kind of force. Explain what they have in "
                "common.",
        "options": [
            {"text": "They all use ordinary contact forces disguised as non-contact ones by parts that meet in the casing", "correct": False,
             "why": "None of these disguises anything — each genuinely "
                    "transfers its effect across a real gap, with "
                    "nothing touching."},
            {"text": "They all use gravity in a specially engineered, "
                     "focused way", "correct": False,
             "why": "None of the three relies on gravity — all three use "
                    "magnetic effects that act across a gap."},
            {"text": "They all rely on air resistance in the gap to carry their effect silently from one part across to the other", "correct": False,
             "why": "Air resistance is a contact force between moving "
                    "air and a surface; none of these three depends on "
                    "air — they would work in a vacuum too."},
            {"text": "They all use a magnetic effect that acts across a "
                     "gap, without the two objects needing to touch",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p4-09-s18",
        "band": "standard",
        "text": "Suggest one way you could test whether a rubbed balloon "
                "lifting someone's hair is really a force, rather than "
                "just moving air around.",
        "options": [
            {"text": "Hold the balloon completely still, close to the "
                     "hair, and see whether the hair still rises",
             "correct": True},
            {"text": "Rub the balloon for even longer and see if the hair rises higher, showing the balloon lifts it", "correct": False,
             "why": "This would only show the effect gets bigger with "
                    "more charge — it would not rule out moving air as "
                    "the real cause."},
            {"text": "Ask someone else to hold their own hair up at exactly the same moment, and compare how high each head of hair rises", "correct": False,
             "why": "This tells you nothing about whether the balloon or "
                    "moving air is responsible for the original effect."},
            {"text": "Measure the exact distance between the balloon and "
                     "the person's hair", "correct": False,
             "why": "A distance measurement alone does not distinguish "
                    "between a genuine force and air simply being blown "
                    "about."},
        ],
        "figure": None,
    },
    {
        "id": "p4-09-s19",
        "band": "standard",
        "text": "A student argues that because air resistance needs "
                "particles to strike a surface, gravity should also be a "
                "contact force, since gravity involves particles of mass "
                "too. What is wrong with this argument?",
        "options": [
            {"text": "Nothing is wrong, because the particles of mass in two objects have to meet before any gravitational pull between them can begin to act", "correct": False,
             "why": "Having mass is not the same as physically touching "
                    "another object — gravity's mass never needs to "
                    "strike anything for the pull to act."},
            {"text": "Having mass is not the same as touching — air "
                     "resistance needs real physical collisions, while "
                     "gravity acts with no collisions at all", "correct": True},
            {"text": "The argument is right, but just for objects with a very large mass, since a huge mass presses on things through its particles", "correct": False,
             "why": "The size of an object's mass makes no difference to "
                    "whether gravity needs contact — it never does, for "
                    "any mass."},
            {"text": "Gravity has no particles involved in it, so the comparison makes no sense, as a force with nothing in it cannot pull on solids", "correct": False,
             "why": "Mass is made of particles, but the comparison still "
                    "fails for the real reason — gravity's pull does not "
                    "depend on any particle striking anything."},
        ],
        "figure": None,
    },
    {
        "id": "p4-09-s20",
        "band": "standard",
        "text": "A steel ball bearing is dropped down a long plastic tube "
                "with a strong magnet fixed halfway down, outside the "
                "tube. Predict and explain what you would observe as the "
                "ball passes the magnet.",
        "options": [
            {"text": "Nothing unusual, because the plastic tube blocks the magnetic force, since a magnetic pull travels through metal but not plastic",
             "correct": False,
             "why": "Plastic is not a magnetic material, so it does not "
                    "block the magnetic force — the ball would still "
                    "respond to the magnet."},
            {"text": "The ball speeds up steadily the whole way down, completely unaffected by the magnet, since it falls past far too quickly to be pulled",
             "correct": False,
             "why": "This ignores the magnet altogether — a strong "
                    "nearby magnet noticeably changes the ball's motion "
                    "as it passes."},
            {"text": "The ball would slow down as it approaches the "
                     "magnet, since the pull acts against gravity there, "
                     "then speed up again once past it", "correct": True},
            {"text": "The ball stops completely and stays stuck to the outside of the tube forever, held flat against the plastic", "correct": False,
             "why": "The ball is inside the tube and the magnet is "
                    "outside it — nothing bridges that gap to actually "
                    "hold the ball in place."},
        ],
        "figure": None,
    },
    {
        "id": "p4-09-s21",
        "band": "standard",
        "text": "Explain why an old television that uses magnets inside "
                "to steer a beam of particles onto the screen can have "
                "its picture distorted by bringing a strong magnet close "
                "to the outside of the screen.",
        "options": [
            {"text": "Because the outside magnet melts part of the screen's own glass surface, so the picture spreads where it softens", "correct": False,
             "why": "A hand-held magnet has nowhere near enough energy "
                    "to melt glass — nothing here is a heating effect."},
            {"text": "Because the outside magnet simply blocks light from escaping the screen, so the picture bends around its edge", "correct": False,
             "why": "This is not about blocking light — it is about a "
                    "magnetic force acting on the moving particles "
                    "inside."},
            {"text": "Because the television's own internal magnets get permanently demagnetised by the new one, so they now steer the beam wrongly",
             "correct": False,
             "why": "A brief, ordinary magnet nearby does not usually "
                    "erase the television's own internal magnets."},
            {"text": "Because the outside magnet's non-contact force "
                     "reaches through the glass and deflects the beam of "
                     "particles moving inside", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p4-09-s22",
        "band": "standard",
        "text": "A cyclist has their speed measured by a magnet fixed to "
                "their wheel, which passes close to a sensor on the "
                "frame on every turn without ever touching it. Explain "
                "why this design works.",
        "options": [
            {"text": "The magnet's non-contact force can be detected by "
                     "the fixed sensor across the small gap on every "
                     "pass", "correct": True},
            {"text": "The magnet has to briefly touch the sensor on every turn for it to register, as the sensor counts each tap", "correct": False,
             "why": "The whole point of using a magnet here is that it "
                    "can be detected WITHOUT any touching at all."},
            {"text": "The sensor is detecting the sound of the wheel spinning, as each turn of it makes a faint click", "correct": False,
             "why": "The design specifically uses a magnetic detector, "
                    "which senses the magnet's non-contact force, not "
                    "sound."},
            {"text": "The magnet slightly heats up the sensor on every pass, and each rise in temperature counts as a turn", "correct": False,
             "why": "This kind of sensor detects a magnetic effect "
                    "directly — it does not rely on any heating."},
        ],
        "figure": None,
    },
    {
        "id": "p4-09-s23",
        "band": "standard",
        "text": "A large industrial crane uses an electromagnet, rather "
                "than a mechanical claw, to move scrap steel around a "
                "yard. Explain one advantage this has when moving a pile "
                "of loose steel pieces.",
        "options": [
            {"text": "It can move one single piece of steel at a time, because the pull reaches the closest piece", "correct": False,
             "why": "An electromagnet lifting a loose pile will "
                    "typically pick up many pieces at once, not exactly "
                    "one."},
            {"text": "It can lift many separate pieces at once, without "
                     "needing to grip each one individually", "correct": True},
            {"text": "It needs no switching off, because a non-contact force keeps its pull going by itself", "correct": False,
             "why": "An electromagnet's pull depends on an electric "
                    "current, which can be switched off, dropping the "
                    "load — that is one of its key advantages."},
            {"text": "It works equally well on steel, aluminium and copper, since an electromagnet pulls on whatever metal is put beneath it", "correct": False,
             "why": "An electromagnet only attracts magnetic materials "
                    "like steel and iron — it has no effect on aluminium "
                    "or copper."},
        ],
        "figure": None,
    },
    {
        "id": "p4-09-s24",
        "band": "standard",
        "text": "A teacher rubs two identical balloons on the same "
                "jumper, then holds them near each other by their "
                "strings. Predict what happens and explain why.",
        "options": [
            {"text": "They stick together immediately, because both balloons carry the same charge, and equal charges pull towards each other",
             "correct": False,
             "why": "Two balloons charged the SAME way by the same "
                    "material actually push each other apart, not "
                    "together."},
            {"text": "Nothing happens, since two identical objects cannot push on one another when their charges match",
             "correct": False,
             "why": "Charged objects do not need to be different to "
                    "exert a force on each other — what matters is the "
                    "SIGN of the charge."},
            {"text": "They push apart, because rubbing them on the same "
                     "material gave them the same kind of charge, and "
                     "like charges repel", "correct": True},
            {"text": "One balloon becomes magnetic and simply pushes the other away, as rubbing makes poles in its surface", "correct": False,
             "why": "Rubbing a balloon produces the electrostatic force, "
                    "not magnetism — the two are separate effects."},
        ],
        "figure": None,
    },
    {
        "id": "p4-09-s25",
        "band": "standard",
        "text": "A satellite in deep space, far from any planet or star, "
                "drifts along in a straight line at constant speed. "
                "Explain what this tells you about gravity out there.",
        "options": [
            {"text": "It shows there is no gravity acting on the satellite there, because gravity is made at a planet's surface and fades away", "correct": False,
             "why": "Gravity from distant masses is still acting a "
                    "little, just far too weakly to notice at that "
                    "distance."},
            {"text": "It shows gravity has switched off completely once you leave a planet's atmosphere, because gravity needs air around it before it can pull", "correct": False,
             "why": "Gravity does not switch off at any distance — it "
                    "merely gets weaker, following the same rule "
                    "everywhere."},
            {"text": "It shows the satellite has become immune to all three non-contact forces out there, since a body moving at a steady speed stops responding to them", "correct": False,
             "why": "No real object becomes immune to gravity, "
                    "magnetism or the electrostatic force — the "
                    "satellite is simply far from any strong source."},
            {"text": "It tells you the resultant force on the satellite "
                     "is close to zero, because any gravity acting there "
                     "is now too weak to measurably curve its path",
             "correct": True},
        ],
        "figure": None,
    },

    # ── MRB-338 night 3 expansion · harder ─────────────────────────────────
    {
        "id": "p4-09-h06",
        "band": "harder",
        "text": "A student claims: 'Since air resistance is caused by "
                "particles, and gravity is caused by particles of mass "
                "too, both must ultimately be contact forces at a small "
                "enough scale.' Explain why this reasoning fails.",
        "options": [
            {"text": "Air resistance involves real physical collisions; "
                     "gravity is explained by a field a mass creates in "
                     "space, with no collision needed at any scale",
             "correct": True},
            {"text": "The reasoning is correct, because a mass has to be in touch with the tiny grains of space around it before its gravitational pull can be passed on",
             "correct": False,
             "why": "Gravity's own explanation, a field extending "
                    "through space, involves no touching at any scale — "
                    "the reasoning does not hold."},
            {"text": "Air resistance and gravity are both fields spreading outwards from an object, so each one reaches its target across a gap rather than by touching",
             "correct": False,
             "why": "Air resistance genuinely does involve direct "
                    "particle collisions with a surface, which is "
                    "exactly what makes it a contact force."},
            {"text": "Particles of mass are just a handy way of speaking rather than real objects, so there is nothing solid to set beside the particles in the air", "correct": False,
             "why": "Mass is a genuine physical property of matter — "
                    "the flaw is elsewhere, in confusing 'made of "
                    "particles' with 'needs to touch.'"},
        ],
        "figure": None,
    },
    {
        "id": "p4-09-h07",
        "band": "harder",
        "text": "The Moon's gravity pulls on the Earth's oceans, causing "
                "tides, and the Moon is roughly 384,000 km away with "
                "nothing but vacuum in between. Contrast this with a "
                "rope pulling a boat: explain the essential physical "
                "difference between the two situations.",
        "options": [
            {"text": "There is no essential difference, because the Moon's pull takes hold of the ocean's surface and draws it along, in the way a rope takes hold of a boat", "correct": False,
             "why": "A rope is a real, touching, physical connection; a "
                    "gravitational pull crosses genuinely empty space "
                    "with nothing physically joining the two objects."},
            {"text": "The rope is a continuous object in contact with "
                     "both ends; gravity needs no such physical link, "
                     "acting through the vacuum of space itself",
             "correct": True},
            {"text": "The Moon's gravity is carried by an invisible thread of space dust, which is drawn out between any two bodies and tightens as they pull on it",
             "correct": False,
             "why": "There is no physical medium carrying gravity across "
                    "space — the modern explanation is a field, not a "
                    "substance of any kind."},
            {"text": "Both are contact forces, since the Moon's surface touches the vacuum beside it and that vacuum touches the sea, handing the pull along",
             "correct": False,
             "why": "Touching a vacuum is not touching anything at all — "
                    "the Moon's gravity acts on the ocean across "
                    "genuinely empty space."},
        ],
        "figure": None,
    },
    {
        "id": "p4-09-h08",
        "band": "harder",
        "text": "A scientist proposes cutting a powerful bar magnet "
                "exactly in half, hoping to end up with one piece that is "
                "purely a north pole and one piece that is purely a south "
                "pole. Evaluate whether this would work, and relate it "
                "to why magnetism can cancel out on a large scale while "
                "gravity cannot.",
        "options": [
            {"text": "It would work perfectly, because the north-seeking and south-seeking ends sit at opposite ends of the bar, so a clean cut down the middle parts two things that were already apart", "correct": False,
             "why": "Cutting a magnet in half always produces two new, "
                    "complete magnets, each with its own north AND south "
                    "pole — a single pole cannot be isolated this way."},
            {"text": "It would destroy the magnetism in both pieces, because the cut opens the bar up and lets the stored magnetic force escape from the fresh ends", "correct": False,
             "why": "Cutting a magnet does not destroy its magnetism — "
                    "each half remains a fully magnetised, complete "
                    "magnet."},
            {"text": "It would not work — each half becomes a new "
                     "complete magnet with both poles, which is why "
                     "magnetism's ever-present opposite poles can cancel "
                     "out on a large scale, unlike gravity", "correct": True},
            {"text": "It would work with a magnet of a rare metal such as samarium, whose two poles are held far enough apart inside the bar for a fine saw to pass between them", "correct": False,
             "why": "This is true of no ordinary magnet material — "
                    "cutting any bar magnet in half always yields two "
                    "complete magnets."},
        ],
        "figure": None,
    },
    {
        "id": "p4-09-h09",
        "band": "harder",
        "text": "A spacecraft accelerates away from Earth using its "
                "engine's thrust, then switches its engine off and "
                "coasts. Explain, in terms of contact and non-contact "
                "forces, what changes about the forces acting on it the "
                "moment the engine switches off, and what does not "
                "change.",
        "options": [
            {"text": "All the forces on it disappear the instant the engine switches off, because a craft that has stopped burning fuel has nothing pushing or pulling it", "correct": False,
             "why": "Gravity, a non-contact force, keeps acting on the "
                    "spacecraft regardless of whether the engine is "
                    "running."},
            {"text": "Gravity switches off along with the thrust, since it is the running engine that holds the craft in the Earth's pull", "correct": False,
             "why": "Gravity has nothing to do with the spacecraft's own "
                    "engine — it comes from the pull of nearby masses, "
                    "and continues whether or not the engine runs."},
            {"text": "Air resistance takes over from the thrust once the engine stops, since a coasting craft is pressed back by the empty space it is travelling through", "correct": False,
             "why": "Far from Earth there is essentially no air to "
                    "produce air resistance — this contact force is not "
                    "relevant once the spacecraft has left the "
                    "atmosphere."},
            {"text": "The contact force of thrust stops the instant the "
                     "engine switches off, while gravity, a non-contact "
                     "force, continues exactly as before", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p4-09-h10",
        "band": "harder",
        "text": "In the 17th century, some scientists refused to accept "
                "Newton's law of gravity because it seemed to require "
                "forces acting across empty space with nothing carrying "
                "them. Explain what the modern explanation offers that "
                "eases this particular objection, and what it does not "
                "fully resolve even today.",
        "options": [
            {"text": "The modern field explanation replaces 'nothing "
                     "carrying the force' with a physical field, though "
                     "what a field ultimately IS remains a genuinely "
                     "hard question in physics", "correct": True},
            {"text": "It settles the objection completely, because a field is a solid substance filling the space between two masses, so the pull is handed along it much as a rope passes on a tug", "correct": False,
             "why": "A field is not a solid substance in the way a rope "
                    "is — describing it that way overstates how "
                    "completely the puzzle has been solved."},
            {"text": "It shows that Newton was mistaken, because the field packs the gap between two masses with something, so no force has to reach across empty space as he had claimed",
             "correct": False,
             "why": "Gravity genuinely does act across empty space — the "
                    "field concept explains HOW, without denying that "
                    "this is what happens."},
            {"text": "It proves that every kind of force, including contact forces, is "
                     "quietly non-contact",
             "correct": False,
             "why": "Contact forces genuinely do require the objects to "
                    "be touching — the field explanation is specific to "
                    "how non-contact forces work."},
        ],
        "figure": None,
    },
    {
        "id": "p4-09-h11",
        "band": "harder",
        "text": "A designer wants a conveyor belt system that sorts steel "
                "cans from aluminium cans automatically, without anyone "
                "touching the cans, using a non-contact force. Explain "
                "how this could be done, and why the same method would "
                "fail for sorting aluminium cans from plastic ones.",
        "options": [
            {"text": "A strong magnet above the belt would lift all three kinds of can clear of it, since any material feels a pull once the magnet chosen is strong enough to reach down to it", "correct": False,
             "why": "A magnet attracts the steel cans but has no effect "
                    "on either the aluminium or the plastic ones — it "
                    "cannot tell those two apart."},
            {"text": "A magnet would pull the steel cans up and away, "
                     "leaving aluminium on the belt; but since neither "
                     "aluminium nor plastic is magnetic, it could not "
                     "then separate those two", "correct": True},
            {"text": "Gravity would separate all three, since each material has its own weight and the heavier cans drop off the end of the belt sooner than the lighter ones do",
             "correct": False,
             "why": "A sorting system like this relies on a MAGNETIC "
                    "difference between the materials, not on their "
                    "weight."},
            {"text": "The electrostatic force would sort all three just as well, since rubbing the belt leaves each material carrying its own charge and sends each of them to a different bin", "correct": False,
             "why": "While static could weakly attract light materials, "
                    "the reliable way to pull out steel specifically is "
                    "with a magnet, which electrostatic attraction does "
                    "not match for this task."},
        ],
        "figure": None,
    },
    {
        "id": "p4-09-h12",
        "band": "harder",
        "text": "Two identical charged balloons are held near each other "
                "and repel with a certain force. If the charge on EACH "
                "balloon were doubled, without changing the distance "
                "between them, predict what would happen to the force "
                "between them.",
        "options": [
            {"text": "The force would stay the same, since the gap between the balloons is what sets how strongly they push apart",
             "correct": False,
             "why": "Distance is only one factor — the amount of charge "
                    "on each object also affects the size of the force."},
            {"text": "The force would simply double, since doubling the charge on a balloon doubles the push that it gives out", "correct": False,
             "why": "BOTH balloons' charges have doubled here, not just "
                    "one, so the effect is bigger than a simple "
                    "doubling."},
            {"text": "The force would increase by more than double, "
                     "since it depends on the charge on both balloons",
             "correct": True},
            {"text": "The force would disappear completely once both charges happen to be equal", "correct": False,
             "why": "Two EQUAL like charges still repel strongly — equal "
                    "charge is not the same as no charge at all."},
        ],
        "figure": None,
    },
    {
        "id": "p4-09-h13",
        "band": "harder",
        "text": "A student is asked to design an experiment testing "
                "whether a hovering drone stays aloft because of a "
                "contact force (air pushed downward by its propellers) "
                "and NOT a non-contact force. Suggest a fair test, and "
                "explain what result would support the contact-force "
                "explanation.",
        "options": [
            {"text": "Fly the drone inside a sealed vacuum chamber; if it still hovers there, the spinning blades must be lifting it by pushing against themselves", "correct": False,
             "why": "This is the right idea in reverse — if the drone "
                    "could NOT hover in a vacuum, that would support air "
                    "being essential, not the other way round."},
            {"text": "Bring a strong magnet close to the hovering drone and see whether it moves, since anything held up without contact would be tugged off course", "correct": False,
             "why": "This tests whether magnetism affects the drone, not "
                    "whether the propellers' effect on the air is what "
                    "holds it up."},
            {"text": "Measure how loud the drone is while it is hovering, since the sound waves it sends downwards are what carry its weight", "correct": False,
             "why": "Loudness does not distinguish between a contact and "
                    "a non-contact explanation for what is holding the "
                    "drone up."},
            {"text": "Fly the drone inside a sealed vacuum chamber; if "
                     "it CANNOT hover without air present, that supports "
                     "the propellers pushing on air", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p4-09-h14",
        "band": "harder",
        "text": "A website claims that satellites 'defy gravity' by "
                "using a secret non-contact 'anti-gravity' force. Using "
                "what you know about orbits and free fall, write a "
                "scientific rebuttal of this claim.",
        "options": [
            {"text": "Satellites do not defy gravity — they are "
                     "continuously falling under it, and their sideways "
                     "speed means that fall permanently misses the "
                     "Earth, which is exactly what an orbit is",
             "correct": True},
            {"text": "The claim is correct, because a satellite stays at the same height above the ground for years on end, and anything still being pulled downwards by the Earth would have come down long ago",
             "correct": False,
             "why": "A satellite IS falling, in exactly the same sense "
                    "as a dropped stone — its fall simply curves around "
                    "the planet instead of hitting it, because of its "
                    "sideways speed."},
            {"text": "Satellites carry powerful magnets that push against the Earth's own magnetism, and this cancels the downward pull and holds them at a steady height above the surface of the planet below",
             "correct": False,
             "why": "No ordinary magnet could ever cancel a planet's "
                    "gravity, and satellites carry no such device — they "
                    "orbit by falling, not by cancelling gravity."},
            {"text": "Satellites are simply too far away for gravity to reach them, so nothing pulls them down", "correct": False,
             "why": "Gravity reaches every satellite in Earth orbit — at "
                    "typical orbital heights it is barely weaker than at "
                    "the ground, which is precisely why they orbit "
                    "rather than drift away."},
        ],
        "figure": None,
    },
    {
        "id": "p4-09-h15",
        "band": "harder",
        "text": "Explain why an astronaut performing a spacewalk outside "
                "the International Space Station does not go flying off "
                "into space, given that nothing is holding them by force "
                "except a safety tether.",
        "options": [
            {"text": "Because there is no gravity so far above the ground, the pull of the Earth having faded away to nothing a few hundred kilometres up", "correct": False,
             "why": "Gravity at the station's altitude is only slightly "
                    "weaker than at the ground — it is very much still "
                    "acting on the astronaut."},
            {"text": "Because the astronaut, like the station, is in "
                     "free fall around the Earth at the same speed, so "
                     "both keep pace with each other", "correct": True},
            {"text": "Because the vacuum around them presses in evenly from every side of the suit and pins them where they are", "correct": False,
             "why": "A vacuum is empty space — it exerts no force on "
                    "anything at all, holding or otherwise."},
            {"text": "Because the metal hull of the station attracts their spacesuit magnetically and keeps drawing them gently back in towards itself", "correct": False,
             "why": "A spacesuit is not magnetically attached to the "
                    "station — what keeps astronaut and station together "
                    "is that both are falling around the Earth at the "
                    "same rate."},
        ],
        "figure": None,
    },
    {
        "id": "p4-09-h16",
        "band": "harder",
        "text": "A speaker uses a coil of wire and a magnet to make the "
                "speaker cone vibrate without the moving cone ever "
                "touching the magnet. Explain why keeping the cone and "
                "magnet from touching is actually essential to how the "
                "speaker works.",
        "options": [
            {"text": "It isn't essential, since a cone resting firmly against the magnet would be pushed and pulled by the contact between the two of them just as well",
             "correct": False,
             "why": "If the cone were fixed against the magnet it could "
                    "not vibrate freely back and forth, which is what "
                    "actually produces sound."},
            {"text": "Touching would make the magnetic force grow so strong that the cone would be dragged hard enough to tear the speaker apart", "correct": False,
             "why": "The reason to avoid contact is about allowing FREE "
                    "MOVEMENT of the cone, not about the force becoming "
                    "uncontrollably strong."},
            {"text": "The magnetic, non-contact force can push and pull "
                     "the cone freely, precisely because nothing is "
                     "physically touching or obstructing its movement",
             "correct": True},
            {"text": "It has nothing to do with the force being magnetic, since a cone of any material sitting near the coil would be moved in the same way", "correct": False,
             "why": "The mechanism specifically relies on a magnetic, "
                    "non-contact force acting on the coil; an ordinary "
                    "non-magnetic material near the magnet would not be "
                    "pushed and pulled in the same way."},
        ],
        "figure": None,
    },
    {
        "id": "p4-09-h17",
        "band": "harder",
        "text": "Explain why a scientist testing whether a newly "
                "discovered material is magnetic would get a misleading "
                "result if they only tested it near a very powerful "
                "magnet, rather than an ordinary one.",
        "options": [
            {"text": "A misleading result is impossible here, since a sample that is drawn towards a magnet of any strength has shown the very property the scientist set out to test", "correct": False,
             "why": "This ignores the possibility that the material "
                    "might not be significantly magnetic itself, yet "
                    "still show some faint response purely because the "
                    "test magnet is unusually powerful."},
            {"text": "The powerful magnet would pull the new material apart before any reading could be taken, since the pull climbs steeply with the strength of the magnet being used",
             "correct": False,
             "why": "An ordinary powerful magnet does not destroy most "
                    "materials just by being brought near them."},
            {"text": "A powerful magnet cannot be used for a fair test, since a fair test calls for the weakest equipment the laboratory has",
             "correct": False,
             "why": "Powerful magnets are used for testing all the time; "
                    "the issue is about interpreting a faint result "
                    "correctly, not about whether they can be used."},
            {"text": "An extremely powerful magnet can produce a small, "
                     "measurable attraction even in a barely magnetic "
                     "material, making it seem more magnetic than it "
                     "really is", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p4-09-h18",
        "band": "harder",
        "text": "A student measures the force between two magnets at "
                "several distances and plots a graph, finding the force "
                "gets rapidly weaker as distance increases, much faster "
                "than it does for gravity between two everyday objects "
                "at the same distances. Suggest why this might be, "
                "without contradicting the general rule that all these "
                "non-contact forces weaken with distance.",
        "options": [
            {"text": "All three non-contact forces weaken with distance, "
                     "but the exact rate each one weakens at is a "
                     "separate detail, not required to match", "correct": True},
            {"text": "It shows that magnetism holds its full strength however far apart the magnets are, so the falling readings must come from the balance drifting", "correct": False,
             "why": "The description explicitly says the magnetic force "
                    "IS getting weaker with distance, just more quickly "
                    "than gravity does in this comparison."},
            {"text": "It proves gravity is not a true non-contact force, since a real one would fade away as quickly as the pull between the magnets did", "correct": False,
             "why": "Gravity is a textbook example of a non-contact "
                    "force — this result is only about how quickly it "
                    "weakens compared with magnetism."},
            {"text": "The measurements must be wrong, since non-contact forces obey a single rule for weakening with distance and so are bound to fade at matching rates",
             "correct": False,
             "why": "Nothing requires every non-contact force to weaken "
                    "with distance in exactly the same way — that "
                    "assumption is the flaw here, not the measurements."},
        ],
        "figure": None,
    },
    {
        "id": "p4-09-h19",
        "band": "harder",
        "text": "A model is proposed in which contact forces are simply non-contact forces acting across an extremely small gap that is too tiny to see. Which piece of evidence is hardest to explain using that model?",
        "options": [
            {"text": "Air resistance clearly increases with speed, which this model cannot explain, because a gap far too small to see would stay exactly the same width however fast the object moved",
             "correct": False,
             "why": "Air resistance increasing with speed is a real, "
                    "separate fact, but it does not by itself test "
                    "whether contact is really a 'tiny non-contact "
                    "gap.'"},
            {"text": "A magnet's pull crosses a real vacuum gap without "
                     "weakening to nothing, while friction vanishes the "
                     "instant a real gap opens up — the model does not "
                     "explain this difference", "correct": True},
            {"text": "Gravity is far too weak a force to test this model with, since a pull that faint would be swamped by the air in the room long before the gap mattered", "correct": False,
             "why": "Gravity's weakness is not directly related to "
                    "testing whether contact forces are secretly "
                    "tiny-gap non-contact forces."},
            {"text": "The model is obviously correct, since atoms hardly touch even at the smallest scale, so friction carries on working across a visible gap just as a magnet's pull does",
             "correct": False,
             "why": "Even if surfaces never touch at the atomic scale, a "
                    "real, visible gap makes a genuine contact force "
                    "vanish at once — unlike a true non-contact force, "
                    "which persists across a visible gap."},
        ],
        "figure": None,
    },
    {
        "id": "p4-09-h20",
        "band": "harder",
        "text": "An engineer designs maglev train brakes that work by "
                "increasing magnetic resistance rather than using "
                "friction pads. Explain one advantage this offers over a "
                "traditional friction brake, in terms of wear.",
        "options": [
            {"text": "It offers no advantage, since all brakes wear out at the same rate in the end, because stopping a train of that mass costs the same rubbing wherever it happens",
             "correct": False,
             "why": "A magnetic brake with no physical pad pressed "
                    "against a moving surface has nothing there to wear "
                    "away in the same manner as a friction pad."},
            {"text": "Friction brakes hardly wear out either, so there is no real difference between the two, as brake pads are made from material harder than the surface they grip", "correct": False,
             "why": "Friction pads genuinely do wear down with repeated "
                    "use, which is precisely the problem a non-contact "
                    "magnetic brake avoids."},
            {"text": "Since the braking force is magnetic, there is no "
                     "physical pad pressing and rubbing against a "
                     "surface, so nothing wears down as a friction pad "
                     "would", "correct": True},
            {"text": "It offers no advantage, because a magnetic force is far weaker than friction and would have to be held on for much longer to stop the train", "correct": False,
             "why": "A magnetic brake on a real train is engineered to "
                    "provide plenty of braking force — the advantage "
                    "claimed here is about wear, not raw strength."},
        ],
        "figure": None,
    },
    {
        "id": "p4-09-h21",
        "band": "harder",
        "text": "Explain why a scientist studying the electrostatic "
                "force between two charged spheres would need to control "
                "the humidity of the room, relating this to how the "
                "electrostatic force behaves over time.",
        "options": [
            {"text": "Humidity changes the mass of the spheres as water settles on them, which alters the gravitational pull acting between the two",
             "correct": False,
             "why": "Humidity has a negligible effect on the spheres' "
                    "mass — the real issue concerns their electric "
                    "charge, not their mass or gravity."},
            {"text": "Damp air makes the spheres look brighter than they are, so the gap between them is read as smaller than it really is", "correct": False,
             "why": "This is not about visibility — it is about a "
                    "physical effect on the charge itself."},
            {"text": "Damp air turns metal spheres magnetic, adding a second pull that is counted as part of the force being measured", "correct": False,
             "why": "Humidity does not make ordinary spheres magnetic — "
                    "the concern is a different non-contact force "
                    "altogether."},
            {"text": "Damp air lets electric charge leak away from a "
                     "charged object more quickly, so the force could "
                     "fade faster during the experiment", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p4-09-h22",
        "band": "harder",
        "text": "A very large, uncharged metal sphere is brought near a "
                "small charged ball on a string, and the ball is seen to "
                "swing towards the uncharged sphere. Suggest an "
                "explanation for why an uncharged object could attract a "
                "charged one.",
        "options": [
            {"text": "The charged ball's field rearranges the charge "
                     "already inside the uncharged sphere, creating a "
                     "temporary attraction despite zero overall charge",
             "correct": True},
            {"text": "The uncharged sphere must have picked up a charge of its own beforehand, since an object carrying no charge can produce no force on anything near it",
             "correct": False,
             "why": "The sphere genuinely can have zero overall charge "
                    "and still show this effect, through a temporary "
                    "rearrangement of the charge already inside it."},
            {"text": "Gravity alone is pulling the ball across, since the metal sphere is so much heavier that its pull outweighs anything the charge could do", "correct": False,
             "why": "A swing specifically towards the metal sphere due "
                    "to nearby charge is a much bigger, faster effect "
                    "than the tiny extra gravity from the sphere's own "
                    "mass at this scale."},
            {"text": "The string holding the ball must be slightly magnetic, so it is the string that the metal sphere draws towards itself, not the ball", "correct": False,
             "why": "An ordinary string is not the explanation here — "
                    "the interesting physics is in how the ball's charge "
                    "interacts with the metal sphere."},
        ],
        "figure": None,
    },
    {
        "id": "p4-09-h23",
        "band": "harder",
        "text": "A hard disk drive's read head flies a few nanometres "
                "above the spinning disk surface without ever touching "
                "it, cushioned partly by air the spinning disk drags "
                "along, and reads data using a magnetic sensor. Identify "
                "which of these TWO effects is contact and which is "
                "non-contact, and justify each.",
        "options": [
            {"text": "Both are non-contact, since a gap of a few nanometres leaves the head hovering clear of the disk, and a force across a gap is a non-contact force",
             "correct": False,
             "why": "However small, the air-cushion effect genuinely "
                    "involves physical air molecules being dragged along "
                    "and pushing on the head — that makes it a contact "
                    "force, however tiny the gap looks."},
            {"text": "The air cushion is a contact force, since real air "
                     "molecules push on the head; the magnetic sensing "
                     "is non-contact, since nothing needs to touch",
             "correct": True},
            {"text": "Both are contact forces, since the head sits so close to the spinning disk that the gap left is far too narrow for a field to cross", "correct": False,
             "why": "Being extremely close is not the same as touching "
                    "— the magnetic sensing specifically works by NOT "
                    "needing any contact at all, however close the head "
                    "sits."},
            {"text": "The magnetic sensing is the contact force here, since the sensor has to meet the disk's magnetism directly, while the air cushion holds the head clear",
             "correct": False,
             "why": "This is the wrong way round — magnetism senses "
                    "across a gap with nothing touching, while the air "
                    "cushion genuinely involves particles physically "
                    "pushing on the head."},
        ],
        "figure": None,
    },
    {
        "id": "p4-09-h24",
        "band": "harder",
        "text": "Two different non-contact forces, gravity and the "
                "electrostatic force, both follow a rule where the force "
                "gets weaker the further apart the two objects are. "
                "Explain why this shared pattern does NOT mean the two "
                "forces are secretly the same force.",
        "options": [
            {"text": "It does mean they are the same force, simply seen in two different situations, since two rules that weaken with distance in the same way must share one cause", "correct": False,
             "why": "The two behave very differently in other ways — "
                    "gravity only ever attracts, for instance, while the "
                    "electrostatic force can also repel, which alone "
                    "shows they are not the same force."},
            {"text": "Gravity and the electrostatic force cancel each other out when both act together, which is why a charged object weighs less than an uncharged one",
             "correct": False,
             "why": "Nothing about these two forces makes them cancel "
                    "each other out just by both being present — they "
                    "act independently, each following its own rule."},
            {"text": "Sharing a pattern of weakening with distance does "
                     "not make two forces identical — gravity only ever "
                     "attracts, while the electrostatic force can attract "
                     "OR repel", "correct": True},
            {"text": "The pattern applies to gravity alone, and the electrostatic force gets stronger with distance instead, since a charge spreads out as it travels and reaches further", "correct": False,
             "why": "The electrostatic force also gets weaker with "
                    "distance, following a similar pattern to gravity, "
                    "even though the two forces are not the same."},
        ],
        "figure": None,
    },
    {
        "id": "p4-09-h25",
        "band": "harder",
        "text": "A textbook states that 'non-contact forces act "
                "instantaneously, the moment one object moves.' Using "
                "the idea that changes in a field travel rather than "
                "appearing everywhere at once, explain why this "
                "statement is an oversimplification.",
        "options": [
            {"text": "The statement is entirely correct, since a field fills the whole of space the moment it is created, so a change to it is passed on everywhere at the same instant",
             "correct": False,
             "why": "Modern physics holds that a change in a field takes "
                    "time to travel outward, rather than being felt "
                    "everywhere in the universe at the very same "
                    "instant."},
            {"text": "Non-contact forces are not real forces, so a question about how fast they travel does not arise; what looks like a pull across a gap is something else",
             "correct": False,
             "why": "Non-contact forces are real, well-tested effects — "
                    "the question here is specifically about how quickly "
                    "a CHANGE in one travels, not whether they exist."},
            {"text": "Gravity alone is instantaneous, while magnetism and the electrostatic force both take time, because gravity needs no material to carry it across the gap",
             "correct": False,
             "why": "None of the three non-contact forces is thought to "
                    "act truly instantaneously — a change in any of "
                    "their fields spreads outward rather than appearing "
                    "everywhere at once."},
            {"text": "A change in a field spreads outward rather than "
                     "being felt everywhere at the same instant, so "
                     "'instantaneous' oversimplifies how the force "
                     "actually propagates", "correct": True},
        ],
        "figure": None,
    },

    # ── MRB-338 night 3 expansion · standard (top-up to 30) ────────────────
    {
        "id": "p4-09-s26",
        "band": "standard",
        "text": "A student claims that a magnet works differently in "
                "air than it does in water, because water is a much "
                "denser substance for the force to cross. Evaluate this "
                "claim.",
        "options": [
            {"text": "The claim is correct, because water is a far denser medium for the pull to cross, so it weakens among the packed particles",
             "correct": False,
             "why": "A non-contact force does not need a medium at all "
                    "to travel through — density of the surrounding "
                    "substance is not what governs it."},
            {"text": "The claim is false — a magnet's pull crosses air, "
                     "water or a vacuum without needing anything to "
                     "carry it across the gap", "correct": True},
            {"text": "The claim is correct just for salt water, since salt makes water conductive, and the liquid carries the pull",
             "correct": False,
             "why": "Magnetism does not rely on the water conducting "
                    "electricity — it acts across water exactly as it "
                    "acts across air."},
            {"text": "The claim cannot be tested, since magnets rust the moment they touch water, so no magnet lasts long enough", "correct": False,
             "why": "Rusting is a separate, slow chemical change to the "
                    "metal — it says nothing about whether magnetism "
                    "itself needs a medium."},
        ],
        "figure": None,
    },
    {
        "id": "p4-09-s27",
        "band": "standard",
        "text": "A magician appears to make a small ball hover using an "
                "electromagnet hidden in a hat above it, controlled by a "
                "wire the audience cannot see. Explain what non-contact "
                "force is really at work, and why the ball is likely to "
                "be a particular kind of metal.",
        "options": [
            {"text": "The electrostatic force is at work, and the ball is likely to be plastic, as charge grips light plastic best", "correct": False,
             "why": "A hidden electromagnet controlled by a wire uses "
                    "magnetism, not static charge; plastic is not "
                    "attracted to a magnet at all."},
            {"text": "Magnetism is at work, and the ball is likely to be "
                     "made of a magnetic metal such as steel or iron",
             "correct": True},
            {"text": "Gravity is at work, reduced by a hidden mechanism under the stage that takes away the ball's weight", "correct": False,
             "why": "Gravity cannot be switched off or reduced by any "
                    "hidden device — an electromagnet is the far more "
                    "plausible explanation."},
            {"text": "Friction is at work between invisible threads and the air, gripping the ball tightly enough to hold it", "correct": False,
             "why": "Friction is a contact force between two touching "
                    "surfaces — it could not hold a ball floating in "
                    "mid-air on its own."},
        ],
        "figure": None,
    },
    {
        "id": "p4-09-s28",
        "band": "standard",
        "text": "Explain why rubbing a balloon on your hair works well "
                "on a dry winter's day, but barely works at all on a "
                "humid summer's day.",
        "options": [
            {"text": "Because balloons are made of a different material in summer, which takes charge poorly", "correct": False,
             "why": "The balloon's material does not change with the "
                    "season — the difference is in the air around it."},
            {"text": "Because damp air lets the charge built up by "
                     "rubbing leak away much more quickly", "correct": True},
            {"text": "Because hair is heavier when it is humid, so it is harder for any force to move it", "correct": False,
             "why": "Humid hair is not significantly heavier — the real "
                    "difference is how quickly the charge leaks away in "
                    "damp air."},
            {"text": "Because magnetism is weaker in humid air, so the balloon's pull drops away", "correct": False,
             "why": "Rubbing a balloon produces the electrostatic force, "
                    "not magnetism, so magnetism's strength is not "
                    "relevant here."},
        ],
        "figure": None,
    },
    {
        "id": "p4-09-s29",
        "band": "standard",
        "text": "A satellite dish receives a signal from a satellite 36,000 km above the Earth. Someone claims this proves radio waves must be a fourth non-contact force, to be added to the three named at this stage. Explain why this claim is mistaken.",
        "options": [
            {"text": "The claim is right, because anything crossing 36,000 km of empty space without touching must be a non-contact force", "correct": False,
             "why": "Radio waves are not classed as one of the three "
                    "non-contact forces studied here, even though they "
                    "also cross a gap."},
            {"text": "Radio waves are a form of light, not a force at "
                     "all, and are simply outside the three forces named "
                     "at this stage", "correct": True},
            {"text": "The claim is right, but just because 36,000 km is further than gravity can reach, so a fourth force takes over", "correct": False,
             "why": "Gravity reaches every distance, just growing "
                    "weaker — the issue is that radio waves are not one "
                    "of the three named non-contact forces at all."},
            {"text": "Satellite dishes work through a hidden wire connection to the ground, so nothing crosses open space", "correct": False,
             "why": "A satellite dish receives its signal wirelessly, "
                    "with no physical wire reaching up to the satellite."},
        ],
        "figure": None,
    },
    {
        "id": "p4-09-s30",
        "band": "standard",
        "text": "Explain why an MRI scanner, which uses an extremely "
                "powerful magnet, requires patients to remove all metal "
                "jewellery and be screened for metal implants before "
                "they go near it.",
        "options": [
            {"text": "Because the magnet could heat any metal on the patient to a dangerously high temperature, as metal warms fast in a field this strong",
             "correct": False,
             "why": "Heating is not the main hazard here — the greater "
                    "danger is the powerful, non-contact pulling force "
                    "the magnet exerts on magnetic metal."},
            {"text": "Because a strong enough magnet can exert a "
                     "dangerous non-contact pull on magnetic metal, even "
                     "through a person's skin and clothing", "correct": True},
            {"text": "Because metal jewellery would get permanently stuck to the patient's skin, welding itself in place as the scanner's magnet is switched on",
             "correct": False,
             "why": "The real danger is the metal being pulled violently "
                    "towards the magnet, not sticking to the skin."},
            {"text": "Because metal in the room would block the scanner from producing an image, soaking up its signal before it returns", "correct": False,
             "why": "Image quality can be affected, but the more urgent "
                    "reason for the rule is patient safety from the "
                    "magnetic pull itself."},
        ],
        "figure": None,
    },

    # ── MRB-338 night 3 expansion · harder (top-up to 30) ──────────────────
    {
        "id": "p4-09-h26",
        "band": "harder",
        "text": "A student proposes testing whether the electrostatic "
                "force obeys the same 'weaker with distance' rule as "
                "gravity and magnetism, by measuring how a charged rod "
                "attracts small bits of paper at different distances. "
                "Suggest one practical difficulty specific to this "
                "particular force that would not affect a similar test "
                "of a magnet.",
        "options": [
            {"text": "The charge on the rod is likely to leak away "
                     "noticeably during the measurements, changing the "
                     "force being tested as time passes", "correct": True},
            {"text": "The rod would need to be kept in a vacuum, since the electrostatic force cannot cross a gap of air the way a magnetic force can",
             "correct": False,
             "why": "The electrostatic force works perfectly well "
                    "through air — that is exactly how rubbing a balloon "
                    "produces its effect."},
            {"text": "Paper is too heavy for the electrostatic force to lift, so the rod has to be brought close enough to touch before anything moves", "correct": False,
             "why": "Small bits of paper are light enough that the "
                    "electrostatic force can and does move them, which "
                    "is precisely why this is a classic demonstration."},
            {"text": "The rod would need to be magnetised before any charge would stay on it, since it is the magnetism that holds the charge in place", "correct": False,
             "why": "Magnetism and electric charge are separate "
                    "properties — a rod does not need to be magnetised "
                    "before it can carry charge."},
        ],
        "figure": None,
    },
    {
        "id": "p4-09-h27",
        "band": "harder",
        "text": "A ship's compass works reliably at sea, but is known to give false readings when the ship is carrying a large cargo of iron ore. Explain why the cargo interferes with the compass.",
        "options": [
            {"text": "The iron ore blocks the Earth's magnetic field from reaching the needle, since a thick mass of metal stops a field passing through",
             "correct": False,
             "why": "The Earth's field is not blocked by nearby iron — "
                    "instead, the iron itself becomes a second source of "
                    "magnetism that competes with it."},
            {"text": "The large mass of iron ore creates its own "
                     "magnetic pull on the needle, which competes with "
                     "the much weaker pull from the Earth itself",
             "correct": True},
            {"text": "Iron ore is not magnetic until it has been smelted, so the false readings must come from the ship's electrical wiring instead", "correct": False,
             "why": "Iron ore is a magnetic material, and a large enough "
                    "quantity of it can genuinely affect a compass "
                    "needle nearby."},
            {"text": "The ship's own gravity rises when it carries heavy cargo, and that extra pull drags the needle round towards the hold",
             "correct": False,
             "why": "A compass needle is not steered by gravity at all "
                    "— it is a magnetic effect, and the extra cargo mass "
                    "makes no meaningful difference to gravity's pull on "
                    "it."},
        ],
        "figure": None,
    },
    {
        "id": "p4-09-h28",
        "band": "harder",
        "text": "Explain why two objects released together inside a "
                "freely falling lift (with its cable cut) appear to "
                "float relative to each other and to the lift itself, "
                "even though gravity has certainly not disappeared.",
        "options": [
            {"text": "Gravity switches itself off inside a falling lift, which is why nothing in there has any weight left to press down with on anything around it", "correct": False,
             "why": "Gravity is still fully acting on the lift and "
                    "everything inside it — nothing about falling "
                    "switches gravity off."},
            {"text": "The lift, the objects and the person inside are "
                     "all falling under gravity at exactly the same "
                     "rate, so nothing presses on anything else",
             "correct": True},
            {"text": "The lift's metal cage acts as a shield, blocking the Earth's gravity from reaching whatever is held inside it", "correct": False,
             "why": "Gravity cannot be blocked by any kind of cage or "
                    "shielding — it acts on every object with mass "
                    "regardless of what surrounds it."},
            {"text": "Air resistance on the falling lift exactly cancels gravity, leaving the objects inside with no resultant force acting on them", "correct": False,
             "why": "Air resistance would need to be enormous to cancel "
                    "gravity, and this floating effect happens even in "
                    "the earliest instant of the fall, before much air "
                    "resistance builds up."},
        ],
        "figure": None,
    },
    {
        "id": "p4-09-h29",
        "band": "harder",
        "text": "A designer wants to build a set of kitchen scales using "
                "a permanent magnet's repulsion from another fixed "
                "magnet, instead of a stretching spring, to measure "
                "weight. Suggest one property this design would need, "
                "for the readings to be trustworthy across its whole "
                "range.",
        "options": [
            {"text": "The repulsive force would need to change in a "
                     "known, consistent way with the gap between the two "
                     "magnets, across the whole range used", "correct": True},
            {"text": "The two magnets would need to be made from different metals, since two of the same metal sit at one fixed gap and read the same weight every time",
             "correct": False,
             "why": "What matters is how the force between the two "
                    "magnets changes with distance, not what particular "
                    "metals they happen to be made from."},
            {"text": "The scale would need to be sealed inside a vacuum, since air trapped between the two magnets weakens the repulsion pushing them apart", "correct": False,
             "why": "Magnetism works perfectly well in ordinary air — a "
                    "vacuum is not required for a magnetic scale to "
                    "function."},
            {"text": "The magnets would need topping up with static electricity before each weighing, as the repulsion between them drains away a little each time",
             "correct": False,
             "why": "Magnetism and static electricity are different "
                    "effects — a permanent magnet does not need "
                    "recharging with electric charge to keep working."},
        ],
        "figure": None,
    },
    {
        "id": "p4-09-h30",
        "band": "harder",
        "text": "A physicist argues that if every non-contact force is explained by a field, then the historical debate about forces needing 'something in between' has been completely settled with nothing left to explain. Evaluate this claim.",
        "options": [
            {"text": "The claim is entirely fair, since once a force has been given a mechanism there is nothing further to ask, and the idea of a field accounts for the whole of what happens in the gap between two objects", "correct": False,
             "why": "Naming the field explains HOW a force can act "
                    "without touching, but deeper questions about what a "
                    "field ultimately is remain active areas of physics."},
            {"text": "The claim overstates things — naming the "
                     "mechanism as a 'field' answers the original 'how "
                     "does it cross the gap' question, but does not by "
                     "itself explain what a field ultimately is at the "
                     "deepest level", "correct": True},
            {"text": "The claim is wrong because fields do not exist as real things, and physicists keep the word as a convenient way of picturing forces they cannot see", "correct": False,
             "why": "Fields are a genuine, well-tested part of physics, "
                    "not just a habit of speech — the issue is about how "
                    "completely they explain the deepest questions, not "
                    "whether they exist."},
            {"text": "The claim is wrong because these three forces are described by equations rather than by fields, and an equation says nothing about crossing a gap",
             "correct": False,
             "why": "The field concept is the standard modern "
                    "explanation for how all three of these forces act "
                    "across a gap, not merely a set of equations."},
        ],
        "figure": None,
    },
]
