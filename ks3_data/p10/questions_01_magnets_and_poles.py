"""P10 lesson 01 — Magnets and poles: twelve questions (MRB-223).

Written against Design's page. The five-object drawer, the three-outcome
figure and the four rungs are hers.

The discriminations, in the order the lesson builds them:

  · a magnet has TWO poles and they come as a pair (`MAG-03`);
  · like repels and unlike attracts, with equal and opposite forces;
  · only some materials respond at all — "metal" is not "magnetic"
    (`MAG-01`), and a magnet does nothing whatever to the rest (`MAG-04`);
  · a magnet magnetises plain steel, so attraction proves nothing and only
    repulsion does (`MAG-02`) — the harder band sits here.

⚠️ NO FORCE IN NEWTONS APPEARS IN ANY QUESTION, and no tesla. Ruled for the
whole unit: every comparison here is relative ("much smaller", "the same
size"), because the equation for the force between two magnets is well beyond
this stage and any number would be invented rather than measured.

⚠️ POSITION IS AUTHORED — 0,1,2,3 · 1,2,3,0 · 2,3,0,1, three of each.

⚠️ NO RUNG IS RESTATED. The ladder owns the unlabelled bar attracted both
ways, the 4 cm to 2 cm repulsion, the clip hanging from either pole and the
scrapyard belt; nothing here reuses any of the four.
"""

UNIT = "P10"
LESSON = "magnets-and-poles"
LESSON_NUMBER = 1

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "p10-01-e01",
        "band": "easier",
        "text": "Which of these is a magnetic material?",
        "options": [
            {"text": "Steel", "correct": True},
            {"text": "Copper", "correct": False,
             "why": "Copper is a metal, but a magnet does nothing to it at "
                    "all. Hold one against a copper pipe and nothing "
                    "happens."},
            {"text": "Aluminium", "correct": False,
             "why": "Aluminium is a metal a magnet ignores completely, which "
                    "is how a recycling plant separates it from steel."},
            {"text": "Brass", "correct": False,
             "why": "Brass is a metal and it is not magnetic. Only iron, "
                    "steel, nickel and cobalt respond."},
        ],
        "figure": None,
    },
    {
        "id": "p10-01-e02",
        "band": "easier",
        "text": "What are the two ends of a magnet called?",
        "options": [
            {"text": "Its positive end and its negative end, like a battery",
             "correct": False,
             "why": "Positive and negative are the words for charge, and for "
                    "a battery's terminals. A magnet's ends are poles, and "
                    "they are named for the direction each one seeks."},
            {"text": "Its north-seeking pole and its south-seeking pole",
             "correct": True},
            {"text": "Its magnetic end and its ordinary, unmagnetic end",
             "correct": False,
             "why": "Both ends are magnetic and both are the same steel. "
                    "What differs is which way each one points."},
            {"text": "Its strong pulling end and its weak pulling end",
             "correct": False,
             "why": "The two poles are equally strong. Turning a magnet round "
                    "changes which pole faces you, never how strong it is."},
        ],
        "figure": None,
    },
    {
        "id": "p10-01-e03",
        "band": "easier",
        "text": "The north pole of one magnet is brought up to the north pole "
                "of another. What happens?",
        "options": [
            {"text": "They pull together, because both of them are magnets",
             "correct": False,
             "why": "Both being magnets is what makes them act at all. What "
                    "decides push or pull is whether the two poles facing "
                    "each other are alike."},
            {"text": "Nothing at all, because two identical poles cancel out",
             "correct": False,
             "why": "Nothing happens only when neither object is a magnet. "
                    "Two north poles act on each other strongly."},
            {"text": "They push apart", "correct": True},
            {"text": "They pull together at first and then push apart",
             "correct": False,
             "why": "The direction of the force does not change as they get "
                    "closer. It gets bigger, and it stays a push."},
        ],
        "figure": None,
    },
    {
        "id": "p10-01-e04",
        "band": "easier",
        "text": "A bar magnet is snapped in half. What do you have?",
        "options": [
            {"text": "One piece that is a north pole and one that is a south "
                     "pole", "correct": False,
             "why": "A single pole on its own has never been found. Each "
                    "piece grows the pole it was missing."},
            {"text": "Two pieces of ordinary steel, because the break "
                     "destroyed the magnetism", "correct": False,
             "why": "Breaking it does not destroy the magnetism. Heating it "
                    "in a flame would; snapping it just makes it shorter."},
            {"text": "One magnet and one piece of plain steel",
             "correct": False,
             "why": "Both halves are magnets. The magnetism is spread through "
                    "the whole bar, not stored at the ends."},
            {"text": "Two shorter magnets, each with its own north and south "
                     "pole", "correct": True},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "p10-01-s01",
        "band": "standard",
        "text": "A large bar magnet and a very small one attract each other. "
                "Which statement about the two forces is right?",
        "options": [
            {"text": "The large magnet feels the larger force, because it is "
                     "the stronger magnet", "correct": False,
             "why": "Being stronger changes how big BOTH forces are. It never "
                    "makes one of the pair bigger than the other."},
            {"text": "They are equal in size and opposite in direction",
             "correct": True},
            {"text": "The small magnet feels the larger force, because it "
                     "moves further", "correct": False,
             "why": "The small one does move further, but that is because it "
                    "is lighter. The force on it is the same size."},
            {"text": "Only the small magnet feels a force, because the large "
                     "one is holding still", "correct": False,
             "why": "Both feel a force. Whether something moves depends on "
                    "its mass, not on whether a force is acting on it."},
        ],
        "figure": None,
    },
    {
        "id": "p10-01-s02",
        "band": "standard",
        "text": "A magnet is held near four objects in turn. Which one does "
                "it do nothing at all to?",
        "options": [
            {"text": "An iron nail", "correct": False,
             "why": "Iron is the material a magnet works on best of all. The "
                    "nail is pulled in."},
            {"text": "A cobalt disc", "correct": False,
             "why": "Cobalt is one of the four magnetic materials, along with "
                    "iron, steel and nickel."},
            {"text": "A brass key", "correct": True},
            {"text": "A steel paper clip", "correct": False,
             "why": "Steel is mostly iron, so the clip is magnetised by the "
                    "magnet and pulled towards it."},
        ],
        "figure": None,
    },
    {
        "id": "p10-01-s03",
        "band": "standard",
        "text": "A magnet holds a steel washer from close up. The washer is "
                "then moved to three times the distance. What happens to the "
                "pull on it?",
        "options": [
            {"text": "It stays the same, because the magnet has not changed",
             "correct": False,
             "why": "The magnet has not changed, but the force between two "
                    "objects depends on how far apart they are as well."},
            {"text": "It becomes three times smaller, in step with the "
                     "distance", "correct": False,
             "why": "The force does not simply track the distance. It falls "
                    "away far faster than that."},
            {"text": "It becomes slightly larger, because there is more air "
                     "in between to carry it", "correct": False,
             "why": "Air carries nothing here — the force works across a "
                    "vacuum too — and opening the gap always weakens it."},
            {"text": "It becomes very much smaller, far more than three times",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p10-01-s04",
        "band": "standard",
        "text": "Iron filings are sprinkled evenly over a bar magnet. Where "
                "do they collect most thickly?",
        "options": [
            {"text": "At the two ends", "correct": True},
            {"text": "Along the middle, half way between the ends",
             "correct": False,
             "why": "The middle is where the effect is weakest. Filings there "
                    "are barely held at all."},
            {"text": "Evenly all over, because the whole bar is magnetised",
             "correct": False,
             "why": "The whole bar is magnetised, but the effect is "
                    "concentrated at the poles, and that is where the filings "
                    "gather."},
            {"text": "Only at one end, because only one end attracts",
             "correct": False,
             "why": "Both poles attract unmagnetised iron equally well. That "
                    "is exactly why attraction proves nothing."},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "p10-01-h01",
        "band": "harder",
        "text": "Two identical bar magnets are held 3 cm apart and pull "
                "together. One is turned end for end, still 3 cm away. How "
                "does the size of the force compare with before?",
        "options": [
            {"text": "It is smaller, because a push is always weaker than a "
                     "pull", "correct": False,
             "why": "A push and a pull between the same two poles at the same "
                    "gap are the same size. Only the direction differs."},
            {"text": "It is larger, because the magnets are now working "
                     "against each other", "correct": False,
             "why": "Nothing about the magnets changed when one was turned. "
                    "The same two poles are the same distance apart."},
            {"text": "It is the same size, and the direction has reversed",
             "correct": True},
            {"text": "It is zero, because turning one round cancels the other",
             "correct": False,
             "why": "Turning one round swaps a pull for a push. It never "
                    "leaves nothing — that happens only when neither object "
                    "is a magnet."},
        ],
        "figure": None,
    },
    {
        "id": "p10-01-h02",
        "band": "harder",
        "text": "A student holds a magnet near an aluminium drinks can, sees "
                "no movement at all, and writes: “the can is not a metal.” "
                "What is wrong with that?",
        "options": [
            {"text": "Nothing is wrong — holding up a magnet is a fair test "
                     "of whether something is a metal", "correct": False,
             "why": "It is a test of whether something is MAGNETIC. Most "
                    "metals fail that test and are still metals."},
            {"text": "The can must have been held too far away for the "
                     "magnet to be able to reach across", "correct": False,
             "why": "Distance would weaken a real pull, but there is no pull "
                    "to weaken. Aluminium gives none at any distance."},
            {"text": "The can was probably painted, and a layer of paint "
                     "blocks a magnet's pull completely",
             "correct": False,
             "why": "A magnet acts straight through paint, paper and "
                    "cardboard. Nothing was blocking anything."},
            {"text": "Plenty of metals are not magnetic, so the test shows "
                     "the can is not made of iron or steel", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p10-01-h03",
        "band": "harder",
        "text": "An unlabelled bar is offered to one end of a magnet and is "
                "pushed firmly away. What does that tell you?",
        "options": [
            {"text": "The bar is a magnet", "correct": True},
            {"text": "The bar is a magnetic material, but it may or may not "
                     "be a magnet", "correct": False,
             "why": "That is what ATTRACTION leaves open. A push can only "
                    "come from another magnet."},
            {"text": "The bar is not a magnetic material, because it moved "
                     "the wrong way", "correct": False,
             "why": "A bar that is not a magnetic material does not move at "
                    "all. This one moved, firmly."},
            {"text": "Nothing certain, because a magnet can push plain steel "
                     "away if it is held close enough", "correct": False,
             "why": "It cannot, at any distance. Plain steel is magnetised "
                    "the opposite way round and is always pulled in."},
        ],
        "figure": None,
    },
    {
        "id": "p10-01-h04",
        "band": "harder",
        "text": "Paper clips can be hung from a magnet in a chain, each clip "
                "holding the next, with only the top one touching the magnet. "
                "Why does the second clip hold the third?",
        "options": [
            {"text": "The clips turn sticky once they have been touched by "
                     "a magnet, and stay that way",
             "correct": False,
             "why": "Nothing is sticking. Take the magnet away and the whole "
                    "chain falls apart at once."},
            {"text": "Each clip is magnetised while it is there, so it "
                     "behaves as a small magnet itself", "correct": True},
            {"text": "The magnet reaches past the first clip and pulls "
                     "directly on every clip below", "correct": False,
             "why": "It does reach past, but that would not explain why each "
                    "clip holds the one below it rather than falling off."},
            {"text": "The clips have shared out the magnet's magnetism "
                     "between them, a little each", "correct": False,
             "why": "The magnet does not lose anything. It lines the clips up "
                    "and keeps everything it had."},
        ],
        "figure": None,
    },
]
