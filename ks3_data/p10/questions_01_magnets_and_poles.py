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
            # ⊕ MRB-297 · 1 Sep 2026 — "unmagnetic" is not a word a student
            # will meet anywhere else; the standard term is "non-magnetic",
            # and it is the term this estate uses everywhere else. This was
            # the only occurrence in ks3_data.
            {"text": "Its magnetic end and its ordinary, non-magnetic end",
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
            # ⊕ MRB-297 · 1 Sep 2026 — this was the only one of the four
            # with no reason attached, and so the shortest by a clear margin.
            # The reason is added; the claim itself is unchanged.
            {"text": "They push apart, because two like poles always "
                     "repel", "correct": True},
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
            # ⊕ MRB-297 · 1 Sep 2026 — this was the only one of the four
            # with no reason attached, and so the shortest by a clear margin.
            # The reason is added; the claim itself is unchanged.
            {"text": "The bar is a magnet, because only another magnet "
                     "is ever pushed away", "correct": True},
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

    # ── MRB-335 top-up · easier ──────────────────────────────────────────
    {
        "id": "p10-01-e05",
        "band": "easier",
        "text": "Which of these metals is NOT magnetic?",
        "options": [            {"text": "Iron", "correct": False,
             "why": "Iron is the commonest magnetic material of all."},
            {"text": "Cobalt", "correct": False,
             "why": "Cobalt is magnetic, along with iron, steel and nickel."},
            {"text": "Nickel", "correct": False,
             "why": "Nickel is one of the few metals a magnet acts on."},
            {"text": "Copper", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p10-01-e06",
        "band": "easier",
        "text": "Two unlike poles are brought together. What do they do?",
        "options": [            {"text": "Repel", "correct": False,
             "why": "Repulsion happens between two LIKE poles, both north or "
                    "both south."},
            {"text": "Cancel each other out", "correct": False,
             "why": "Neither pole is destroyed; they pull towards each "
                    "other."},
            {"text": "Do nothing until they touch", "correct": False,
             "why": "The force acts across a gap, and grows as the gap "
                    "closes."},
            {"text": "Attract", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p10-01-e07",
        "band": "easier",
        "text": "Can a magnet have a north pole with no south pole?",
        "options": [
            {"text": "Yes, if it is cut carefully enough", "correct": False,
             "why": "Cutting a magnet gives two magnets; each piece grows the "
                    "pole it was missing."},
            {"text": "Yes, if it is very small", "correct": False,
             "why": "Size makes no difference — even the smallest piece has "
                    "both."},
            {"text": "No — the poles always come as a pair", "correct": True},
            {"text": "No, unless it is an electromagnet", "correct": False,
             "why": "An electromagnet has two ends as well, a north and a "
                    "south."},
        ],
        "figure": None,
    },
    {
        "id": "p10-01-e08",
        "band": "easier",
        "text": "A magnet is moved further away from a steel washer. The "
                "force on the washer…",
        "options": [
            {"text": "gets stronger", "correct": False,
             "why": "Moving apart weakens it; moving closer is what "
                    "strengthens it."},
            {"text": "stays the same at any distance", "correct": False,
             "why": "It falls off sharply, which is why a fridge magnet must "
                    "sit flat against the door."},
            {"text": "gets weaker", "correct": True},
            {"text": "reverses and becomes a push", "correct": False,
             "why": "Nothing about distance turns an attraction into a "
                    "repulsion."},
        ],
        "figure": None,
    },
    {
        "id": "p10-01-e09",
        "band": "easier",
        "text": "Which observation PROVES that an unlabelled bar is a magnet?",
        "options": [
            {"text": "It is attracted to a known magnet", "correct": False,
             "why": "Unmagnetised steel is attracted too, so attraction "
                    "proves nothing."},
            {"text": "It sticks firmly to a fridge door", "correct": False,
             "why": "A plain steel bar sticks to a fridge door as well."},
            {"text": "It is pushed away by a known pole", "correct": True},
            {"text": "It picks up a paper clip", "correct": False,
             "why": "A bar that has been magnetised temporarily does that "
                    "too, and so does one held near a magnet."},
        ],
        "figure": None,
    },
    {
        "id": "p10-01-e10",
        "band": "easier",
        "text": "The two forces between two magnets are…",
        "options": [
            {"text": "larger on the stronger magnet", "correct": False,
             "why": "Strength does not change the pair; both feel the same "
                    "size of force."},
            {"text": "larger on the smaller magnet", "correct": False,
             "why": "Size makes no difference either; the two forces always "
                    "match."},
            {"text": "equal in size and opposite in direction", "correct": True},
            {"text": "acting on only one of the two magnets", "correct": False,
             "why": "Both are acted on, which is why both move when they are "
                    "free to."},
        ],
        "figure": None,
    },
    {
        "id": "p10-01-e11",
        "band": "easier",
        "text": "A magnet is held near a plastic ruler. What happens?",
        "options": [
            {"text": "The ruler is attracted", "correct": False,
             "why": "Plastic is not a magnetic material, so a magnet does "
                    "nothing to it."},
            {"text": "The ruler is repelled", "correct": False,
             "why": "Repulsion needs two magnets, and plastic is neither "
                    "magnetic nor a magnet."},
            {"text": "Nothing happens at all", "correct": True},
            {"text": "The ruler becomes a magnet", "correct": False,
             "why": "Only iron, steel, nickel and cobalt can be magnetised at "
                    "all."},
        ],
        "figure": None,
    },

    # ── MRB-335 top-up · standard ────────────────────────────────────────
    {
        "id": "p10-01-s05",
        "band": "standard",
        "text": "A known magnet attracts an unlabelled object. What might the "
                "object be?",
        "options": [
            {"text": "A magnet's opposite pole facing, or unmagnetised steel",
             "correct": True},
            {"text": "A magnet with its like pole facing", "correct": False,
             "why": "Two like poles repel, so it would be pushed away rather "
                    "than pulled in."},
            {"text": "Only a magnet — nothing else is attracted",
             "correct": False,
             "why": "Unmagnetised iron and steel are attracted too, which is "
                    "why attraction proves nothing."},
            {"text": "Only unmagnetised steel, since a magnet would repel it "
                     "instead",
             "correct": False,
             "why": "A magnet the other way round is attracted as strongly as "
                    "any steel bar."},
        ],
        "figure": None,
    },
    {
        "id": "p10-01-s06",
        "band": "standard",
        "text": "A magnet is held against a copper coin and the coin does not "
                "move at all. What does that show?",
        "options": [            {"text": "That the magnet is too weak", "correct": False,
             "why": "A far stronger magnet does nothing to copper either; the "
                    "material is what matters."},
            {"text": "That copper repels magnets very weakly", "correct": False,
             "why": "Nothing happens at all — there is no push and no pull."},
            {"text": "That the coin is already a magnet", "correct": False,
             "why": "A magnet would be attracted or repelled, not "
                    "unaffected."},
            {"text": "That copper is not a magnetic material", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p10-01-s07",
        "band": "standard",
        "text": "Two magnets repel at 4 cm apart and are moved to 8 cm. What "
                "happens to the force?",
        "options": [
            {"text": "It doubles", "correct": False,
             "why": "Moving apart always weakens a magnetic force, never "
                    "strengthens it."},
            {"text": "It stays the same, because the magnets have not "
                     "changed",
             "correct": False,
             "why": "The magnets are the same, but the force between them "
                    "depends strongly on the gap."},
            {"text": "It becomes much weaker", "correct": True},
            {"text": "It becomes exactly half as large", "correct": False,
             "why": "It falls away much faster than the distance grows, so "
                    "halving is too gentle."},
        ],
        "figure": None,
    },
    {
        "id": "p10-01-s08",
        "band": "standard",
        "text": "A steel paper clip hanging from a magnet can itself pick up "
                "a second clip. Why?",
        "options": [            {"text": "Because some of the magnet's magnetism has been used up "
                     "and passed on",
             "correct": False,
             "why": "Nothing is used up — the magnet is unchanged when the "
                    "clips are taken off."},
            {"text": "Because the second clip is attracted to the magnet "
                     "through the first",
             "correct": False,
             "why": "It hangs even when far enough away for the magnet alone "
                    "to be too weak; the first clip is genuinely magnetised."},
            {"text": "Because the clips are sticky when they are clean",
             "correct": False,
             "why": "It works with oiled clips, and only with magnetic "
                    "materials."},
            {"text": "Because the first clip has been magnetised by the "
                     "magnet's field",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p10-01-s09",
        "band": "standard",
        "text": "Why is attraction not proof that an object is a magnet?",
        "options": [            {"text": "Because attraction is too weak to be measured "
                     "reliably",
             "correct": False,
             "why": "It is easily strong enough to measure; it is what it "
                    "proves that is the problem."},
            {"text": "Because attraction happens between any two metals",
             "correct": False,
             "why": "Copper and aluminium are ignored completely, so it is "
                    "not any metal."},
            {"text": "Because only repulsion happens between two real "
                     "magnets",
             "correct": False,
             "why": "Two magnets attract when unlike poles face; repulsion is "
                    "simply the test that rules other things out."},
            {"text": "Because unmagnetised iron and steel are attracted too",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p10-01-s10",
        "band": "standard",
        "text": "A scrapyard belt carries crushed steel cans and aluminium "
                "cans. Which does the magnet lift out?",
        "options": [            {"text": "The aluminium cans", "correct": False,
             "why": "Aluminium is not magnetic, so a magnet does nothing to "
                    "it."},
            {"text": "Neither, because crushed cans are too heavy",
             "correct": False,
             "why": "The magnets used are easily strong enough; the material "
                    "is what decides."},
            {"text": "Both kinds, since both are metal", "correct": False,
             "why": "Being a metal is not enough — only iron, steel, nickel "
                    "and cobalt respond."},
            {"text": "The steel cans", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p10-01-s11",
        "band": "standard",
        "text": "A magnet is dipped into a tray of mixed sand and iron "
                "filings. What comes out on it?",
        "options": [
            {"text": "Both, because they are mixed together", "correct": False,
             "why": "Only the filings are held; the sand falls away."},
            {"text": "The sand", "correct": False,
             "why": "Sand is not magnetic, so nothing acts on it."},
            {"text": "Neither, because the mixture is not a magnet",
             "correct": False,
             "why": "The filings do not need to be magnets — magnetic "
                    "material is attracted."},
            {"text": "The iron filings", "correct": True},
        ],
        "figure": None,
    },

    # ── MRB-335 top-up · harder ──────────────────────────────────────────
    {
        "id": "p10-01-h05",
        "band": "harder",
        "text": "A bar magnet is snapped into four pieces. How many poles are "
                "there altogether?",
        "options": [
            {"text": "Two, as there were before", "correct": False,
             "why": "Each piece is a complete magnet with two poles of its "
                    "own."},
            {"text": "Four, one on each piece", "correct": False,
             "why": "A single pole cannot exist alone, so no piece can have "
                    "just one."},
            {"text": "Eight, two on each piece", "correct": True},
            {"text": "None, because breaking it destroys the magnetism",
             "correct": False,
             "why": "Each piece is still a magnet; breaking it makes more "
                    "magnets, not fewer."},
        ],
        "figure": None,
    },
    {
        "id": "p10-01-h06",
        "band": "harder",
        "text": "A steel screwdriver picks up screws after being stroked with "
                "a magnet. What has happened?",
        "options": [            {"text": "Some of the magnet's material has rubbed onto the "
                     "steel",
             "correct": False,
             "why": "Nothing is transferred; the magnet weighs the same "
                    "afterwards."},
            {"text": "The screwdriver is now attracted to every metal",
             "correct": False,
             "why": "It still ignores copper and aluminium, as any magnet "
                    "does."},
            {"text": "The screwdriver has become permanently magnetic and can "
                     "never lose it",
             "correct": False,
             "why": "Dropping it or heating it can knock the magnetism out "
                    "again."},
            {"text": "The screwdriver has been magnetised, and it may lose it "
                     "again",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p10-01-h07",
        "band": "harder",
        "text": "Why is an unmagnetised steel bar attracted to a magnet "
                "whichever pole is offered to it?",
        "options": [
            {"text": "Because steel is attracted to everything",
             "correct": False,
             "why": "It ignores copper, plastic and wood; only a magnetic "
                    "field acts on it."},
            {"text": "Because the bar already has a north pole at one end, "
                     "whichever way up",
             "correct": False,
             "why": "It is unmagnetised, so it has no poles until the magnet "
                    "gives it some."},
            {"text": "Because the magnet magnetises it, so the near end is "
                     "opposite",
             "correct": True},
            {"text": "Because attraction does not depend on poles at all",
             "correct": False,
             "why": "It depends on them entirely — which is why the induced "
                    "pole always comes out opposite."},
        ],
        "figure": None,
    },
    {
        "id": "p10-01-h08",
        "band": "harder",
        "text": "A magnet left beside a steel screwdriver for a week makes it "
                "slightly magnetic without ever touching it. What does that "
                "show?",
        "options": [            {"text": "That magnetism can travel through air as a substance",
             "correct": False,
             "why": "Nothing travels across; the field is already there in "
                    "the space between them."},
            {"text": "That the magnet has lost some of its own strength to "
                     "the steel",
             "correct": False,
             "why": "The magnet is unchanged; magnetising the steel takes "
                    "nothing away from it."},
            {"text": "That the screwdriver was already a magnet all along",
             "correct": False,
             "why": "It was tested before and did nothing; the change is "
                    "real."},
            {"text": "That the field acts across a gap and can magnetise a "
                     "material",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p10-01-h09",
        "band": "harder",
        "text": "A magnet picks up a steel pin through a sheet of paper. What "
                "does that show about the field?",
        "options": [
            {"text": "That paper is slightly magnetic", "correct": False,
             "why": "Paper is ignored completely; the field simply passes "
                    "through it."},
            {"text": "That the magnet is touching the pin through the fibres",
             "correct": False,
             "why": "It works through a thick book as well, with no contact "
                    "anywhere."},
            {"text": "That the field passes through non-magnetic materials",
             "correct": True},
            {"text": "That the pin has been thrown through the paper by the "
                     "force",
             "correct": False,
             "why": "The paper is undamaged; the pin is held against it from "
                    "the other side."},
        ],
        "figure": None,
    },
    {
        "id": "p10-01-h10",
        "band": "harder",
        "text": "A fridge magnet holds firmly on bare metal but slides off "
                "when a thick pad of card is put behind it. Why?",
        "options": [            {"text": "Because card is a magnetic shield", "correct": False,
             "why": "Card does not shield at all; it simply holds the magnet "
                    "further away."},
            {"text": "Because the magnet loses strength when it is not "
                     "touching metal",
             "correct": False,
             "why": "The magnet is unchanged; only the distance to the door "
                    "has grown."},
            {"text": "Because the card makes the magnet heavier",
             "correct": False,
             "why": "The card is not attached to the magnet, and its own "
                    "weight is not the issue."},
            {"text": "Because the extra gap weakens the force below the "
                     "magnet's weight",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p10-01-h11",
        "band": "harder",
        "text": "A student claims turning a magnet end for end makes it "
                "stronger. Which test settles it?",
        "options": [            {"text": "Count how many paper clips hang from it each way, at "
                     "any distance",
             "correct": False,
             "why": "Distance changes the count, so an uncontrolled test "
                    "proves nothing either way."},
            {"text": "Weigh the magnet each way round", "correct": False,
             "why": "Mass has nothing to do with magnetic strength, and does "
                    "not change with orientation."},
            {"text": "See which end picks up a steel bar and which does not",
             "correct": False,
             "why": "Both ends pick up steel, so this cannot separate the two "
                    "cases."},
            {"text": "Measure the force at the SAME distance with each end, "
                     "and compare",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p10-01-e12",
        "band": "easier",
        "text": "A magnet is held close to a gold ring. What happens?",
        "options": [
            {"text": "Nothing at all — gold is not a magnetic material", "correct": True},
            {"text": "The ring is pulled towards the magnet", "correct": False,
             "why": "Gold is not one of the four magnetic materials, so a magnet "
                    "does nothing to it at all."},
            {"text": "The ring is pushed away from the magnet, because every "
             "metal produces a small magnetic repulsion of its own", "correct": False,
             "why": "Repulsion needs two magnets facing like poles. The ring is "
                    "not a magnet and not a magnetic material either."},
            {"text": "The ring slowly becomes magnetised", "correct": False,
             "why": "Only iron, steel, nickel and cobalt can be turned into "
                    "magnets. Gold cannot, however long it sits near one."},
        ],
        "figure": None,
    },
    {
        "id": "p10-01-e13",
        "band": "easier",
        "text": "A pile of coins made from nickel is placed near a strong magnet. "
                "What happens to them?",
        "options": [
            {"text": "They only respond once they have been magnetised themselves "
             "first", "correct": False,
             "why": "Being near the magnet is what magnetises them — that is "
                    "exactly how induced attraction works, not something that has "
                    "to happen beforehand."},
            {"text": "They are pulled towards the magnet, because nickel is a "
             "magnetic material", "correct": True},
            {"text": "They are pushed away, because like poles always repel", "correct": False,
             "why": "The coins are not magnetised, so they have no pole of their "
                    "own to repel with."},
            {"text": "Nothing happens, because nickel is not on the list of magnetic "
             "materials", "correct": False,
             "why": "Nickel is one of the four: iron, steel, nickel and cobalt. It "
                    "responds to a magnet like the others do."},
        ],
        "figure": None,
    },
    {
        "id": "p10-01-e14",
        "band": "easier",
        "text": "A horseshoe magnet is bent into a U-shape instead of a straight "
                "bar. How many poles does it have?",
        "options": [
            {"text": "None — bending a magnet removes its poles entirely, leaving "
             "a demagnetised loop of ordinary steel", "correct": False,
             "why": "Bending changes the shape, not the magnetism. The two ends "
                    "still behave exactly like a bar magnet's poles."},
            {"text": "Four — two on each arm", "correct": False,
             "why": "Bending the shape does not add poles. Each end of the metal "
                    "is still just one pole."},
            {"text": "Two — one north and one south, same as a bar magnet", "correct": True},
            {"text": "One, shared between the two arms", "correct": False,
             "why": "A pole cannot be shared. Each end of the magnet is a separate "
                    "pole with its own identity."},
        ],
        "figure": None,
    },
    {
        "id": "p10-01-e15",
        "band": "easier",
        "text": "Two ordinary steel paperclips, neither of which has ever been near "
                "a magnet, are held close together. What happens?",
        "options": [
            {"text": "They attract, because both are made of a magnetic material", "correct": False,
             "why": "Being a magnetic material is not the same as being a magnet. "
                    "Two unmagnetised clips have no pole to attract with."},
            {"text": "They repel, because they are identical", "correct": False,
             "why": "Repulsion needs two like poles facing each other. Neither "
                    "clip has a pole at all."},
            {"text": "They attract only once they touch", "correct": False,
             "why": "They never move towards each other in the first place, "
                    "touching or not — there is nothing acting on either one."},
            {"text": "Nothing — neither paperclip is a magnet", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p10-01-e16",
        "band": "easier",
        "text": "A steel drinks can and an aluminium drinks can sit side by side. A "
                "magnet is brought up to both. Which one is pulled towards it?",
        "options": [
            {"text": "The steel can", "correct": True},
            {"text": "Neither can moves", "correct": False,
             "why": "The steel can is a magnetic material and is pulled in "
                    "strongly."},
            {"text": "The aluminium can", "correct": False,
             "why": "Aluminium is one of the metals a magnet ignores completely."},
            {"text": "Both cans move equally", "correct": False,
             "why": "Only the steel can is magnetic; the aluminium one does not "
                    "respond at all."},
        ],
        "figure": None,
    },
    {
        "id": "p10-01-e17",
        "band": "easier",
        "text": "A bar magnet's north pole picks up a steel nail. The magnet is "
                "then turned round so its south pole faces the same nail. What "
                "happens?",
        "options": [
            {"text": "The nail is pushed away instead", "correct": False,
             "why": "Pushing away only happens between two magnets. The nail is "
                    "not a magnet, so it cannot be repelled."},
            {"text": "The nail is picked up again, just as before", "correct": True},
            {"text": "The nail is picked up, but only half as strongly", "correct": False,
             "why": "Both poles are equally strong, so the pull on unmagnetised "
                    "steel is the same either way round."},
            {"text": "The nail falls off, because only the north pole attracts steel", "correct": False,
             "why": "Both poles attract unmagnetised steel equally well. Neither "
                    "pole is special for this."},
        ],
        "figure": None,
    },
    {
        "id": "p10-01-e18",
        "band": "easier",
        "text": "A fridge magnet holds a photograph flat against a steel fridge "
                "door. Why does this work even though there is no second magnet on "
                "the other side of the door?",
        "options": [
            {"text": "The door is repelled into place, pinning the photograph", "correct": False,
             "why": "Repulsion would push the door and magnet apart, not hold "
                    "anything flat against it. This is a straightforward "
                    "attraction."},
            {"text": "The steel door has its own weak magnetism already", "correct": False,
             "why": "An ordinary fridge door is not already magnetised. It is "
                    "attracted because it is a magnetic material, not because it "
                    "is already a magnet."},
            {"text": "Steel is a magnetic material, so the magnet attracts it "
             "directly", "correct": True},
            {"text": "The photograph itself becomes magnetised and pulls the door", "correct": False,
             "why": "Paper is not a magnetic material and cannot be magnetised. It "
                    "is the steel door being attracted, not the paper."},
        ],
        "figure": None,
    },
    {
        "id": "p10-01-e19",
        "band": "easier",
        "text": "A magnet is held near a brass door handle. What happens?",
        "options": [
            {"text": "The handle is pulled towards the magnet", "correct": False,
             "why": "Brass is not a magnetic material. A magnet does nothing to "
                    "it."},
            {"text": "The handle is pushed away", "correct": False,
             "why": "Repulsion needs two magnets. The handle is neither a magnet "
                    "nor a magnetic material."},
            {"text": "The handle slowly becomes magnetised", "correct": False,
             "why": "Only iron, steel, nickel and cobalt can be turned into "
                    "magnets by a nearby field."},
            {"text": "Nothing happens at all", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p10-01-e20",
        "band": "easier",
        "text": "A bar magnet is cut into three equal pieces. How many magnets do "
                "you end up with?",
        "options": [
            {"text": "Three separate magnets, each with its own north and south pole", "correct": True},
            {"text": "Three pieces with no poles, since cutting destroys the "
             "magnetism", "correct": False,
             "why": "Cutting a magnet does not destroy anything. Each new piece "
                    "grows the pole it is missing."},
            {"text": "One long magnet in three parts, sharing one north and one "
             "south pole", "correct": False,
             "why": "Cutting it separates the pieces completely. Each one becomes "
                    "its own independent magnet."},
            {"text": "Three pieces, but only two of them are magnets", "correct": False,
             "why": "Every piece keeps the property of being a magnet — none of "
                    "them is left as plain, unmagnetised steel."},
        ],
        "figure": None,
    },
    {
        "id": "p10-01-e21",
        "band": "easier",
        "text": "Two magnets pull together strongly and have to be pulled apart "
                "with real effort. What does the effort you feel show?",
        "options": [
            {"text": "That the air between them is being compressed", "correct": False,
             "why": "The force acts whether or not there is any air in the gap at "
                    "all. It does not come from the air."},
            {"text": "That a real force is acting between the two magnets", "correct": True},
            {"text": "That one of the magnets is losing its magnetism as it is "
             "pulled", "correct": False,
             "why": "Neither magnet loses anything by being separated. The effort "
                    "is about overcoming the force, not weakening a magnet."},
            {"text": "That the magnets are becoming demagnetised by the pulling", "correct": False,
             "why": "Pulling them apart does not demagnetise them — dropping them "
                    "hard or heating them would, but separating them by hand does "
                    "not."},
        ],
        "figure": None,
    },
    {
        "id": "p10-01-e22",
        "band": "easier",
        "text": "A steel nail hangs from the south pole of a magnet. What pole does "
                "the near end of the nail become?",
        "options": [
            {"text": "No pole at all, because the nail is not a magnet", "correct": False,
             "why": "Being near the magnet is exactly what turns the nail into a "
                    "weak magnet for as long as it stays there."},
            {"text": "A south pole, the same as the magnet's", "correct": False,
             "why": "The induced pole always comes out opposite the one facing it, "
                    "never the same."},
            {"text": "A north pole, opposite the magnet's south pole", "correct": True},
            {"text": "Both a north and a south pole at the same end", "correct": False,
             "why": "One end can only become one pole. The far end of the nail "
                    "becomes the matching opposite."},
        ],
        "figure": None,
    },
    {
        "id": "p10-01-e23",
        "band": "easier",
        "text": "What does it mean for a piece of steel to have become "
                "'magnetised'?",
        "options": [
            {"text": "It has had an electric current passed through it, which is "
             "how every permanent magnet is first made", "correct": False,
             "why": "A current can build a magnet in a coil of wire, but ordinary "
                    "steel is magnetised simply by being near a magnet's field."},
            {"text": "It has been coated in a special magnetic paint", "correct": False,
             "why": "Nothing is added to the surface. Magnetising is about how the "
                    "metal's own structure lines up."},
            {"text": "It has been heated until it glows red hot", "correct": False,
             "why": "Heating a magnet strongly enough actually destroys its "
                    "magnetism, rather than creating it."},
            {"text": "Its tiny magnetic regions have been lined up so it behaves as "
             "a magnet", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p10-01-e24",
        "band": "easier",
        "text": "A magnet is snapped into two pieces, one twice as long as the "
                "other. Does the shorter piece still have its own north and south "
                "pole?",
        "options": [
            {"text": "Yes — the length of the piece makes no difference", "correct": True},
            {"text": "No — only the longer piece keeps both poles", "correct": False,
             "why": "Every piece grows the pole it is missing, whatever its "
                    "length. Size does not decide this."},
            {"text": "No — the shorter piece has no poles at all", "correct": False,
             "why": "A piece of magnet without any pole has never been found, "
                    "however small it is cut."},
            {"text": "No — the shorter piece ends up with two south poles and no "
             "north", "correct": False,
             "why": "A magnet cannot have two poles of the same kind. Each piece "
                    "gets exactly one of each."},
        ],
        "figure": None,
    },
    {
        "id": "p10-01-e25",
        "band": "easier",
        "text": "Two horseshoe magnets are held so that a north pole on one faces a "
                "north pole on the other. What happens?",
        "options": [
            {"text": "They spin round until unlike poles are facing", "correct": False,
             "why": "Held in place, they simply push apart. Nothing turns them "
                    "round on its own."},
            {"text": "They push apart", "correct": True},
            {"text": "They pull together", "correct": False,
             "why": "Two north poles are LIKE poles, and like poles never pull "
                    "together."},
            {"text": "Nothing happens, because horseshoe magnets do not affect each "
             "other", "correct": False,
             "why": "A horseshoe magnet's poles behave exactly like a bar "
                    "magnet's. Two of them absolutely act on each other."},
        ],
        "figure": None,
    },
    {
        "id": "p10-01-e26",
        "band": "easier",
        "text": "A fruit-shaped fridge magnet sticks firmly to a steel fridge door. "
                "The same magnet is then pressed against a wooden cupboard door. "
                "What happens?",
        "options": [
            {"text": "It sticks just as firmly as before", "correct": False,
             "why": "Wood is not a magnetic material, so there is nothing for the "
                    "magnet to attract."},
            {"text": "It sticks, but only weakly", "correct": False,
             "why": "There is no pull at all on wood, not even a weak one."},
            {"text": "It falls off, because wood is not a magnetic material", "correct": True},
            {"text": "It sticks only if pressed on very hard, because enough "
             "pressure forces any material to respond a little", "correct": False,
             "why": "No amount of pressing creates a magnetic pull where there is "
                    "none. Wood simply does not respond."},
        ],
        "figure": None,
    },
    {
        "id": "p10-01-e27",
        "band": "easier",
        "text": "Which of these everyday objects would be attracted to a strong "
                "magnet?",
        "options": [
            {"text": "A rubber band", "correct": False,
             "why": "Rubber is not a magnetic material and is completely "
                    "unaffected."},
            {"text": "A glass marble", "correct": False,
             "why": "Glass contains no magnetic material at all."},
            {"text": "A plastic comb", "correct": False,
             "why": "Plastic, like glass and rubber, is ignored completely by a "
                    "magnet."},
            {"text": "A steel paperclip", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p10-01-e28",
        "band": "easier",
        "text": "A magnet is brought near a brass doorknob and then near a steel "
                "door hinge. Which one is attracted?",
        "options": [
            {"text": "The steel hinge", "correct": True},
            {"text": "Neither", "correct": False,
             "why": "The steel hinge is a magnetic material and responds strongly."},
            {"text": "The brass doorknob", "correct": False,
             "why": "Brass is not magnetic. Only the steel hinge is affected."},
            {"text": "Both, equally", "correct": False,
             "why": "Brass does not respond at all — only the steel hinge is "
                    "pulled in."},
        ],
        "figure": None,
    },
    {
        "id": "p10-01-e29",
        "band": "easier",
        "text": "Which pair of materials are BOTH magnetic?",
        "options": [
            {"text": "Gold and cobalt", "correct": False,
             "why": "Gold is not magnetic. Only the cobalt in this pair responds "
                    "to a magnet."},
            {"text": "Iron and steel", "correct": True},
            {"text": "Iron and aluminium", "correct": False,
             "why": "Aluminium is not one of the four magnetic materials, even "
                    "though iron is."},
            {"text": "Copper and nickel", "correct": False,
             "why": "Copper is not magnetic. Only the nickel in this pair responds "
                    "to a magnet."},
        ],
        "figure": None,
    },
    {
        "id": "p10-01-e30",
        "band": "easier",
        "text": "A bar magnet is snapped in half, and then one of those halves is "
                "snapped in half again. How many separate magnets are there now?",
        "options": [
            {"text": "One, because the pieces reassemble their fields", "correct": False,
             "why": "Nothing reassembles on its own. Each snap leaves the pieces "
                    "as separate, independent magnets."},
            {"text": "Two", "correct": False,
             "why": "The second snap makes another break, so there are more than "
                    "two pieces by the end."},
            {"text": "Three", "correct": True},
            {"text": "Four", "correct": False,
             "why": "Only two snaps were made in total, which makes three pieces, "
                    "not four."},
        ],
        "figure": None,
    },
    {
        "id": "p10-01-s12",
        "band": "standard",
        "text": "A student claims to have made a magnet with a north pole at "
                "both ends and no south pole anywhere on it. Why can a "
                "physicist be confident this has not really happened?",
        "options": [
            {"text": "Because a magnet must always have equal amounts of north and "
             "south, and a two-north magnet has never been produced", "correct": True},
            {"text": "Because two north poles this close together would instantly "
             "repel each other into separate pieces the moment the bar was made",
             "correct": False,
             "why": "Poles fixed inside one solid bar cannot fly apart. The real "
                    "reason is that a lone pole has never been found, not that the "
                    "bar would break."},
            {"text": "Because magnets can only be made with one pole labelled at a "
             "time", "correct": False,
             "why": "Labelling is not what fixes the poles. Every magnet has one "
                    "of each, however it is marked."},
            {"text": "Because a north pole always demagnetises after a few hours", "correct": False,
             "why": "A pole does not simply fade away on its own. The claim fails "
                    "because a matching south pole is missing entirely, not "
                    "because of decay."},
        ],
        "figure": None,
    },
    {
        "id": "p10-01-s13",
        "band": "standard",
        "text": "A repair shop demagnetises a screwdriver by heating it red hot and "
                "letting it cool. Why does this remove its magnetism?",
        "options": [
            {"text": "The heat evaporates the magnetic material out of the steel", "correct": False,
             "why": "Nothing leaves the metal. The steel is still there "
                    "afterwards, simply no longer magnetised."},
            {"text": "The strong heat knocks the lined-up magnetic regions out of "
             "alignment", "correct": True},
            {"text": "Heating makes the poles swap ends, cancelling each other out", "correct": False,
             "why": "The poles do not swap. The alignment inside the metal is "
                    "simply scrambled by the heat."},
            {"text": "Red-hot steel briefly becomes a non-magnetic material and "
             "stays that way", "correct": False,
             "why": "Steel is still a magnetic material once it cools. What is "
                    "lost is the alignment that made it act as a magnet."},
        ],
        "figure": None,
    },
    {
        "id": "p10-01-s14",
        "band": "standard",
        "text": "A magnet is dropped hard onto a concrete floor several times. What "
                "is the most likely effect on its magnetism?",
        "options": [
            {"text": "It swaps its north and south poles round", "correct": False,
             "why": "Dropping it does not reverse the poles. It disturbs the "
                    "alignment that gives the magnet its strength."},
            {"text": "It gets stronger, because the impact packs the regions closer "
             "together and lines up more of them at once", "correct": False,
             "why": "Impact does the opposite — it jars the aligned regions apart "
                    "rather than packing them closer."},
            {"text": "It weakens, because the impact knocks its lined-up magnetic "
             "regions out of alignment", "correct": True},
            {"text": "Nothing changes, because dropping a magnet cannot affect it", "correct": False,
             "why": "A hard enough impact genuinely disturbs the alignment inside "
                    "the metal, weakening the magnet."},
        ],
        "figure": None,
    },
    {
        "id": "p10-01-s15",
        "band": "standard",
        "text": "Inside an unmagnetised steel bar, tiny magnetic regions point in "
                "random directions, different from their neighbours. What is the "
                "effect on the bar's OVERALL magnetism?",
        "options": [
            {"text": "Only the regions near the surface matter, and those always "
             "line up on their own", "correct": False,
             "why": "Surface regions are just as randomly pointed as interior ones "
                    "until the bar is deliberately magnetised."},
            {"text": "The bar becomes a weak magnet at each end only", "correct": False,
             "why": "With random regions throughout, there is no overall alignment "
                    "anywhere in the bar, ends included."},
            {"text": "The regions add up to a strong, patchy magnetism", "correct": False,
             "why": "Pointing in random directions makes the regions cancel each "
                    "other out, not add up."},
            {"text": "The effects cancel out, so the bar shows no overall magnetism", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p10-01-s16",
        "band": "standard",
        "text": "Physicists have searched hard for a single, isolated magnetic pole "
                "with no opposite pole anywhere on the same object. What has every "
                "search found so far?",
        "options": [
            {"text": "No isolated pole has ever been found — every piece found has "
             "both a north and a south", "correct": True},
            {"text": "Isolated poles exist but only inside a magnet's very centre, "
             "never at its surface", "correct": False,
             "why": "The claim is not about where a lone pole hides — none has "
                    "ever been found anywhere, centre or surface."},
            {"text": "Isolated poles are common in electromagnets but never in "
             "permanent magnets", "correct": False,
             "why": "No isolated pole has been found in any kind of magnet at all."},
            {"text": "A handful of confirmed isolated poles, all inside extremely "
             "powerful magnets", "correct": False,
             "why": "No confirmed isolated pole has ever been found, however "
                    "powerful the magnet searched."},
        ],
        "figure": None,
    },
    {
        "id": "p10-01-s17",
        "band": "standard",
        "text": "A large horseshoe magnet is much stronger than a small bar magnet "
                "from the stock cupboard. A steel paperclip is held at the same "
                "distance from each in turn. Which paperclip is harder to pull away "
                "by hand?",
        "options": [
            {"text": "Neither — the pull on unmagnetised steel is fixed and does not "
             "depend on the magnet used", "correct": False,
             "why": "A stronger magnet does pull unmagnetised steel harder at the "
                    "same distance, not the same amount."},
            {"text": "The one held near the horseshoe magnet", "correct": True},
            {"text": "It is impossible to say without knowing which pole is facing "
             "the paperclip", "correct": False,
             "why": "Both poles of a magnet attract unmagnetised steel equally, so "
                    "which pole is used makes no difference here."},
            {"text": "The one held near the small bar magnet", "correct": False,
             "why": "A weaker magnet exerts a smaller pull at the same distance, "
                    "so its paperclip is the easier one to pull away."},
        ],
        "figure": None,
    },
    {
        "id": "p10-01-s18",
        "band": "standard",
        "text": "A steel bracket is bolted permanently right next to a large magnet "
                "inside a factory machine, in daily use for years. What is most "
                "likely true of the bracket after all that time?",
        "options": [
            {"text": "It has become non-magnetic, because constant exposure wears "
             "the magnetism away", "correct": False,
             "why": "Exposure to a field magnetises steel; it does not strip "
                    "magnetism from it."},
            {"text": "It has become a magnetic insulator, blocking the machine's "
             "magnet from working", "correct": False,
             "why": "Nothing blocks a magnetic field, and steel is not an "
                    "insulator of any kind for it."},
            {"text": "It has become a weak magnet itself, magnetised by the field "
             "nearby", "correct": True},
            {"text": "It has stayed completely unaffected, because bolting does not "
             "transfer magnetism", "correct": False,
             "why": "It is the nearby FIELD, not the bolting, that magnetises "
                    "steel over time — contact is not needed at all."},
        ],
        "figure": None,
    },
    {
        "id": "p10-01-s19",
        "band": "standard",
        "text": "Two students each hold one of a pair of magnets that attract each "
                "other, one magnet much heavier than the other. Both let go at the "
                "same moment. Which magnet moves further before they meet?",
        "options": [
            {"text": "Neither — they always meet exactly half way between their "
             "starting points", "correct": False,
             "why": "That would only be true if the two magnets had equal mass. "
                    "With one much heavier, the lighter one covers more of the "
                    "distance."},
            {"text": "It depends on which pole is facing which, not on their weights "
             "at all", "correct": False,
             "why": "Which poles are facing decides whether they attract or repel, "
                    "not how far each one travels once they do."},
            {"text": "The heavier one, because it has more magnetism to pull with", "correct": False,
             "why": "The force on each magnet is the same size. Mass, not extra "
                    "magnetism, is what changes how far each one moves."},
            {"text": "The lighter one, because the same-sized force moves a lighter "
             "object further", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p10-01-s20",
        "band": "standard",
        "text": "A magnet is used to test three unlabelled metal bars, one at a "
                "time. Bar A attracts it, bar B repels it, and bar C does nothing "
                "at all. What can be concluded about bar B?",
        "options": [
            {"text": "It is definitely a magnet, because only a magnet can be pushed "
             "away by a magnet", "correct": True},
            {"text": "It is definitely not a magnetic material at all", "correct": False,
             "why": "A material that is not magnetic would do nothing when tested, "
                    "not push the test magnet away."},
            {"text": "It is a magnetic material, but nothing more can be concluded", "correct": False,
             "why": "Repulsion tells you far more than that — it is the one result "
                    "that proves the bar is a magnet."},
            {"text": "It might be a magnet, or it might be unmagnetised steel — the "
             "test does not settle it", "correct": False,
             "why": "Unmagnetised steel is never pushed away by a magnet. "
                    "Repulsion settles the question completely."},
        ],
        "figure": None,
    },
    {
        "id": "p10-01-s21",
        "band": "standard",
        "text": "A magnet and an unmagnetised steel bar are the same size and "
                "shape, and both painted the same colour so they cannot be told "
                "apart by looking. A steel paperclip sticks to BOTH of them equally "
                "well. Does the paperclip test tell you which one is the real "
                "magnet?",
        "options": [
            {"text": "No — because paint blocks a magnetic field, so neither test "
             "result can be trusted", "correct": False,
             "why": "Paint does not block a magnetic field at all. The test fails "
                    "for a different reason: attraction alone never settles it."},
            {"text": "No — attraction happens with both, so this test proves nothing "
             "about which is which", "correct": True},
            {"text": "Yes — whichever one holds the paperclip more firmly must be "
             "the magnet", "correct": False,
             "why": "The question says both hold it equally well, so there is no "
                    "difference in firmness to go on here."},
            {"text": "Yes — only a real magnet can attract a paperclip at all", "correct": False,
             "why": "Unmagnetised steel attracts a paperclip perfectly well too, "
                    "which is exactly why this test cannot decide it."},
        ],
        "figure": None,
    },
    {
        "id": "p10-01-s22",
        "band": "standard",
        "text": "A steel object picks up a paperclip while resting against a "
                "magnet. Once moved well away from any magnet, it no longer picks "
                "anything up. What does this suggest?",
        "options": [
            {"text": "Moving an object always destroys any magnetism it has", "correct": False,
             "why": "A genuine, deliberately magnetised magnet keeps working after "
                    "being moved. Only the temporary, induced kind fades this way."},
            {"text": "The object was a genuine magnet that has now completely worn "
             "out from ordinary use over a long period of time", "correct": False,
             "why": "A genuine magnet does not simply stop being a magnet after "
                    "being moved. This behaviour fits a different explanation."},
            {"text": "The object's pull came from being magnetised temporarily by "
             "the nearby magnet, and it faded once that magnet was gone", "correct": True},
            {"text": "The paperclip must have lost its own magnetism in the meantime", "correct": False,
             "why": "An ordinary paperclip was never a magnet to begin with. What "
                    "changed is the steel object's induced magnetism."},
        ],
        "figure": None,
    },
    {
        "id": "p10-01-s23",
        "band": "standard",
        "text": "A magnet is used to pick up a mix of ten steel washers and five "
                "brass washers scattered together on a bench, in one go. How many "
                "washers come up on the magnet?",
        "options": [
            {"text": "Five — only the brass ones, since brass is often used in "
             "fittings", "correct": False,
             "why": "Brass is the metal that is ignored here. Steel is the one "
                    "that responds."},
            {"text": "It varies each time, unpredictably", "correct": False,
             "why": "Which washers respond is fixed by their material, not by "
                    "chance — the same ten steel ones every time."},
            {"text": "Fifteen — all of them, since washers are usually metal", "correct": False,
             "why": "Brass is a metal but not a magnetic one, so the five brass "
                    "washers are left behind."},
            {"text": "Ten — exactly the steel ones", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p10-01-s24",
        "band": "standard",
        "text": "A bar magnet is melted down and recast into exactly the same "
                "shape, using the very same steel. Is the new bar automatically a "
                "magnet again?",
        "options": [
            {"text": "No — melting and recasting scrambles the magnetic regions, so "
             "it starts unmagnetised", "correct": True},
            {"text": "Yes, because it is still the same total amount of steel as "
             "before", "correct": False,
             "why": "The amount of steel is not what matters. What matters is "
                    "whether the regions inside it are lined up, and melting "
                    "destroys that."},
            {"text": "No — melted and recast steel can never be magnetised again by "
             "anything, however strong the magnet used on it", "correct": False,
             "why": "It can absolutely be magnetised again, by the same means as "
                    "any other unmagnetised piece of steel. It simply is not one "
                    "automatically."},
            {"text": "Yes — the steel remembers its old shape and magnetism", "correct": False,
             "why": "Steel does not remember anything. Melting scrambles the "
                    "alignment that gave it its magnetism."},
        ],
        "figure": None,
    },
    {
        "id": "p10-01-s25",
        "band": "standard",
        "text": "A magnet is used to lift a steel bolt. A second, identical bolt is "
                "then hung from the bottom of the first, touching it but never "
                "touching the magnet directly. Does the second bolt also stick?",
        "options": [
            {"text": "Only if the two bolts are welded together first", "correct": False,
             "why": "Simply touching is enough — the induced magnetism is carried "
                    "through contact without any welding needed."},
            {"text": "Yes — the first bolt is magnetised by the magnet and can "
             "attract the second one itself", "correct": True},
            {"text": "No — only an object touching the magnet directly can ever be "
             "attracted", "correct": False,
             "why": "The first bolt becomes magnetised and passes the effect on, "
                    "so contact with the magnet itself is not required for the "
                    "second bolt."},
            {"text": "No — two identical bolts always repel each other, whichever "
             "way round they are held", "correct": False,
             "why": "The bolts are unmagnetised steel, not two magnets, so "
                    "repulsion is not the issue here at all."},
        ],
        "figure": None,
    },
    {
        "id": "p10-01-s26",
        "band": "standard",
        "text": "A student says that because both ends of a magnet are made of the "
                "exact same steel, they must behave identically in every way. Is "
                "the student right?",
        "options": [
            {"text": "Yes — poles are only a labelling convention with no real "
             "difference in behaviour, however the magnet is later tested", "correct": False,
             "why": "The two poles behave genuinely differently towards another "
                    "magnet's poles — one attracts where the other would repel."},
            {"text": "Yes — identical material always means identical behaviour at "
             "both ends", "correct": False,
             "why": "One end is north-seeking and the other south-seeking, and "
                    "they behave oppositely towards other magnets — the material "
                    "being the same does not make that untrue."},
            {"text": "No — one end always behaves as north-seeking and the other as "
             "south-seeking, even though the steel is identical", "correct": True},
            {"text": "No — the two ends are actually made of subtly different steel", "correct": False,
             "why": "Both ends really are the same steel throughout. What differs "
                    "is which direction each end seeks, not the material."},
        ],
        "figure": None,
    },
    {
        "id": "p10-01-s27",
        "band": "standard",
        "text": "A metal strip is welded together from two different materials: one "
                "half steel, one half aluminium. A magnet is run slowly along the "
                "whole strip. Over which half does it feel a pull?",
        "options": [
            {"text": "Over both halves equally, since it is one continuous strip", "correct": False,
             "why": "Being welded into one strip does not make the aluminium half "
                    "magnetic. The pull is felt only over the steel."},
            {"text": "Only over the aluminium half", "correct": False,
             "why": "Aluminium is the half that is ignored. The steel half is "
                    "where the pull is felt."},
            {"text": "Over neither half, because welding two different metals "
             "cancels their properties", "correct": False,
             "why": "Welding does not cancel a material's properties. The steel "
                    "half still responds exactly as steel does."},
            {"text": "Only over the steel half", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p10-01-s28",
        "band": "standard",
        "text": "A fridge magnet holds six sheets of paper plus a photo against a "
                "thin steel door. Moved to a much thicker steel door, twice the "
                "thickness, does it hold as many sheets?",
        "options": [
            {"text": "Yes — the thickness of the steel does not weaken the pull, "
             "only the gap to the magnet does", "correct": True},
            {"text": "No — thicker steel is always less magnetic than thin steel", "correct": False,
             "why": "Thickness is not linked to how magnetic the material is. "
                    "Steel is steel, thick or thin."},
            {"text": "It depends on the colour of the paint on each door", "correct": False,
             "why": "Paint colour plays no part in how strongly a magnet grips the "
                    "steel underneath."},
            {"text": "No — a thicker door needs a stronger pull to hold anything at "
             "all, however close the magnet sits against it", "correct": False,
             "why": "The thickness of the steel behind the surface does not weaken "
                    "the pull; only the gap to the magnet matters."},
        ],
        "figure": None,
    },
    {
        "id": "p10-01-s29",
        "band": "standard",
        "text": "A magnet holds up a hanging chain of ten identical steel washers, "
                "one below another, with only the top washer touching the magnet. "
                "Which washer is held on by the WEAKEST magnetism?",
        "options": [
            {"text": "The middle washer, because it is furthest from both ends of "
             "the chain", "correct": False,
             "why": "The chain's strength runs one way, from the real magnet down. "
                    "There is nothing special about the middle."},
            {"text": "The bottom washer, furthest from the real magnet", "correct": True},
            {"text": "All the washers are held equally strongly, since they are "
             "identical", "correct": False,
             "why": "Being identical washers does not stop the induced magnetism "
                    "weakening further down the chain, away from the real magnet."},
            {"text": "The top washer, because it carries the weight of all the "
             "others", "correct": False,
             "why": "The top washer is nearest the real magnet and is magnetised "
                    "most strongly, not weakest."},
        ],
        "figure": None,
    },
    {
        "id": "p10-01-s30",
        "band": "standard",
        "text": "Magnet X's pull on a fixed steel ball is much bigger than magnet "
                "Y's pull on the same ball, tested at the same distance. What can "
                "be concluded?",
        "options": [
            {"text": "The steel ball is a stronger magnetic material when near "
             "magnet X", "correct": False,
             "why": "The ball's material does not change between the two tests. "
                    "What differs is the strength of the magnet doing the pulling."},
            {"text": "Nothing can be concluded without knowing the size of each "
             "magnet", "correct": False,
             "why": "The pull itself is the evidence needed — a bigger pull at the "
                    "same distance means a stronger magnet, whatever its size."},
            {"text": "Magnet X is the stronger magnet", "correct": True},
            {"text": "Magnet Y must be further away, even though the question says "
             "the distance is the same", "correct": False,
             "why": "The distance is stated to be equal for both tests, so "
                    "distance cannot be the reason for the difference."},
        ],
        "figure": None,
    },
    {
        "id": "p10-01-h12",
        "band": "harder",
        "text": "Two identical-looking bars, P and Q, are brought together and pull "
                "towards each other. A student claims this proves BOTH are magnets. "
                "What is the best reason this claim is not safe?",
        "options": [
            {"text": "Attraction also happens when only one bar is a magnet and the "
             "other is unmagnetised steel, so this result cannot rule that "
             "out", "correct": True},
            {"text": "Two real magnets can never attract each other, only repel", "correct": False,
             "why": "Two magnets attract perfectly well when unlike poles face "
                    "each other. That is not what makes the claim unsafe here."},
            {"text": "Attraction only ever happens between two non-magnetic "
             "materials", "correct": False,
             "why": "Two non-magnetic materials would show no attraction at all. "
                    "Attraction needs at least one magnet involved."},
            {"text": "The bars must be touching for the test to count, and the "
             "question does not make clear whether they actually touched",
             "correct": False,
             "why": "Whether they touch is not the issue. The real problem is that "
                    "attraction alone cannot distinguish a magnet from magnetised "
                    "steel."},
        ],
        "figure": None,
    },
    {
        "id": "p10-01-h13",
        "band": "harder",
        "text": "The same two bars, P and Q, still pull together just as strongly "
                "when P is turned end for end. What does this tell you?",
        "options": [
            {"text": "The test is inconclusive and shows nothing new at all", "correct": False,
             "why": "It shows a great deal: consistent attraction whichever way "
                    "one bar is turned rules out both of them being magnets."},
            {"text": "At least one of the two bars is definitely not a magnet", "correct": True},
            {"text": "Both bars are definitely magnets, since the pull stayed the "
             "same size", "correct": False,
             "why": "If both were magnets, turning one round would swap the "
                    "interaction from attract to repel. Since it did not, at least "
                    "one bar cannot be a magnet."},
            {"text": "Neither bar can be a magnet, because a real magnet's pull "
             "always changes when it is turned", "correct": False,
             "why": "One of them could still be a genuine magnet — it is the OTHER "
                    "bar being plain steel that explains the unchanged pull, not "
                    "both being non-magnets."},
        ],
        "figure": None,
    },
    {
        "id": "p10-01-h14",
        "band": "harder",
        "text": "A bar magnet is cut into a hundred tiny equal pieces. In "
                "principle, could the cutting continue forever without ever "
                "producing a piece with just one pole?",
        "options": [
            {"text": "No — after enough cuts, a piece is eventually left with only a "
             "north pole", "correct": False,
             "why": "No single-pole piece has ever been produced by cutting, "
                    "however far the cutting goes."},
            {"text": "It depends on which half is cut, north-side pieces keep "
             "splitting but south-side pieces stop producing new poles after a "
             "few cuts", "correct": False,
             "why": "Both halves of any cut behave identically — each grows the "
                    "pole it is missing, regardless of which side it came from."},
            {"text": "Yes, in principle — every piece found, however small, has kept "
             "both poles, and no isolated pole has ever been found", "correct": True},
            {"text": "No — beyond a certain small size, pieces must lose their poles "
             "altogether", "correct": False,
             "why": "There is no known size limit at which pieces stop having "
                    "poles. The pattern of paired poles has held at every scale "
                    "tested."},
        ],
        "figure": None,
    },
    {
        "id": "p10-01-h15",
        "band": "harder",
        "text": "A manufacturer wants to build a fridge magnet with ONLY a south "
                "pole, so that it can be turned any way round without worrying "
                "about orientation. Based on this lesson, is this possible?",
        "options": [
            {"text": "Yes, but only if the magnet is made from cobalt rather than "
             "iron or steel, since cobalt behaves completely differently",
             "correct": False,
             "why": "The material used does not change this. Cobalt magnets still "
                    "always have one of each pole."},
            {"text": "No — but a magnet CAN be made with two souths and no north "
             "instead", "correct": False,
             "why": "A magnet cannot have two poles of the same kind either. Every "
                    "magnet needs exactly one north and one south."},
            {"text": "Yes, with a strong enough magnetising process", "correct": False,
             "why": "No process, however strong, has ever produced a magnet with "
                    "just one pole. Every magnet has both."},
            {"text": "No — every magnet must have a north pole to match its south "
             "pole; a single-pole magnet cannot be made", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p10-01-h16",
        "band": "harder",
        "text": "A steel bridge girder near a large industrial magnet becomes "
                "weakly magnetic after some months. An engineer wants to remove "
                "this magnetism completely without moving the girder. Which method "
                "would actually work?",
        "options": [
            {"text": "Heating the affected section to a very high temperature", "correct": True},
            {"text": "Spraying the girder with water to cool it down further", "correct": False,
             "why": "Cooling a magnet down does not remove its magnetism — if "
                    "anything, strong heat is what disrupts it, not cold."},
            {"text": "Leaving the girder in exactly the same spot for longer", "correct": False,
             "why": "Leaving it near the industrial magnet for longer would if "
                    "anything strengthen the induced magnetism, not remove it."},
            {"text": "Painting the girder a different colour", "correct": False,
             "why": "Paint is a surface coating and has no effect on the alignment "
                    "inside the steel."},
        ],
        "figure": None,
    },
    {
        "id": "p10-01-h17",
        "band": "harder",
        "text": "A magnet holds four steel washers in a hanging chain, one below "
                "another. The bottom washer is gently touched from below by a "
                "strong opposing magnet, with an unlike pole facing upwards. What "
                "is most likely to happen to the chain?",
        "options": [
            {"text": "The whole chain is pulled upward off the original magnet "
             "entirely", "correct": False,
             "why": "The opposing magnet's pull acts mainly on the nearest washer, "
                    "not on the whole chain equally, so it is more likely to break "
                    "the chain than lift it whole."},
            {"text": "The chain could break apart, because the opposing pull may "
             "overcome the weak induced magnetism holding the lower washers "
             "on", "correct": True},
            {"text": "The chain becomes permanently magnetised and stays together "
             "even without the original magnet, holding firm indefinitely from "
             "then on", "correct": False,
             "why": "The washers are only weakly and temporarily magnetised by "
                    "induction; nothing here makes that permanent."},
            {"text": "Nothing changes, because only the top washer is directly "
             "affected by any magnet", "correct": False,
             "why": "The bottom washer is now directly next to a strong opposing "
                    "magnet, which can easily overcome the weak induced magnetism "
                    "holding the chain together at that point."},
        ],
        "figure": None,
    },
    {
        "id": "p10-01-h18",
        "band": "harder",
        "text": "Two students each independently test the same unlabelled bar using "
                "their own separate magnets. Student A gets a push away; student B "
                "gets a pull towards. Both tests are done correctly. What can be "
                "concluded about the bar for certain?",
        "options": [
            {"text": "The bar cannot be a magnet, because a genuine magnet would "
             "give the exact same result to every single person who tested it",
             "correct": False,
             "why": "A magnet's interaction with another magnet depends on which "
                    "poles face each other, so different students testing with "
                    "different orientations can get different results from a "
                    "genuine magnet."},
            {"text": "One of the two students must have made an experimental mistake", "correct": False,
             "why": "Both results are entirely consistent with the bar being a "
                    "magnet tested with two differently-oriented magnets. No "
                    "mistake needs to be assumed."},
            {"text": "It is definitely a magnet, because only a magnet can push "
             "another magnet away — the other result does not change this", "correct": True},
            {"text": "The two results contradict each other, so neither test can be "
             "trusted", "correct": False,
             "why": "The results do not actually contradict — they simply depend "
                    "on which pole each student's own magnet offered the bar."},
        ],
        "figure": None,
    },
    {
        "id": "p10-01-h19",
        "band": "harder",
        "text": "A magnet strongly attracts a steel bolt from a box of assorted "
                "bolts, but completely ignores a second bolt of the same size and "
                "shape from the same box. What is the most likely explanation?",
        "options": [
            {"text": "The magnet must have run out of magnetism after the first bolt", "correct": False,
             "why": "A magnet does not use itself up on one object. It remains "
                    "just as able to attract a second magnetic object."},
            {"text": "The second bolt is further away, even though the question "
             "gives no reason to think so, and distance alone explains the "
             "difference", "correct": False,
             "why": "Nothing in the scenario suggests a different distance. A "
                    "material difference is the explanation that fits what is "
                    "described."},
            {"text": "Steel bolts only respond to a magnet on their first test, "
             "never afterwards", "correct": False,
             "why": "There is no such rule. A steel bolt is attracted every time "
                    "it is tested, not only once."},
            {"text": "The ignored bolt is probably made of a different, non-magnetic "
             "material such as brass, even though it looks similar", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p10-01-h20",
        "band": "harder",
        "text": "A recycling worker wants to separate three mixed piles of scrap "
                "using only a single magnet: pile A is steel screws, pile B is "
                "aluminium cans, and pile C is brass fittings. In one pass, which "
                "piles end up together on the magnet, and which are left behind?",
        "options": [
            {"text": "Pile A comes up on the magnet; piles B and C are both left "
             "behind together", "correct": True},
            {"text": "Piles A and C come up together, since both are metal fittings, "
             "leaving only pile B behind", "correct": False,
             "why": "Being metal is not enough — brass in pile C is not magnetic, "
                    "so it is left behind with the aluminium."},
            {"text": "All three piles come up together, since a strong enough magnet "
             "lifts any metal", "correct": False,
             "why": "No magnet, however strong, lifts aluminium or brass — "
                    "strength changes how hard something is pulled, never whether "
                    "a non-magnetic material responds at all."},
            {"text": "None of the piles respond, because mixed scrap cannot be "
             "separated this way", "correct": False,
             "why": "The steel screws in pile A are a magnetic material and "
                    "respond perfectly well, separating cleanly from the other two "
                    "piles."},
        ],
        "figure": None,
    },
    {
        "id": "p10-01-h21",
        "band": "harder",
        "text": "A magnet's pull on a steel washer is measured at a certain "
                "distance. The same test is repeated at the SAME distance using a "
                "magnet twice as strong. What is the most reasonable prediction?",
        "options": [
            {"text": "The pull exactly doubles, following the same rule that applies "
             "to distance", "correct": False,
             "why": "The steep fall-off rule measured on this bench is about "
                    "changing DISTANCE, not about changing the magnet's strength — "
                    "it cannot simply be reused here."},
            {"text": "The pull becomes bigger, but the exact size cannot be read off "
             "the distance rule, which is about distance, not magnet "
             "strength", "correct": True},
            {"text": "The pull stays exactly the same, because the distance has not "
             "changed", "correct": False,
             "why": "Changing the magnet's own strength absolutely changes the "
                    "force it exerts, even at a fixed distance."},
            {"text": "The pull becomes weaker, because two similar magnets always "
             "interfere with each other and cancel out some of the pull",
             "correct": False,
             "why": "There is only one magnet in this test, doing the pulling on a "
                    "plain steel washer — there is no second magnet to interfere "
                    "with anything."},
        ],
        "figure": None,
    },
    {
        "id": "p10-01-h22",
        "band": "harder",
        "text": "A magnet and a plain steel bar are glued together end to end, "
                "forming one longer object that cannot be taken apart. A steel "
                "paperclip sticks to the FAR end of the steel-bar half, well away "
                "from the magnet itself. What is the best explanation?",
        "options": [
            {"text": "The paperclip is being pulled by the magnet's field reaching "
             "straight through solid steel from the far side", "correct": False,
             "why": "A field does pass through non-magnetic materials, but here "
                    "the steel bar itself has been magnetised right along its "
                    "length by contact, which is the simpler explanation for a "
                    "pull at its far end."},
            {"text": "This cannot really happen, so the paperclip must be stuck by "
             "something other than magnetism", "correct": False,
             "why": "It genuinely can happen — a steel bar joined to a magnet "
                    "becomes magnetised along its own length."},
            {"text": "The magnet has magnetised the whole of the attached steel bar, "
             "including its far end, by direct contact", "correct": True},
            {"text": "The glue itself has become magnetic and is carrying the pull "
             "along", "correct": False,
             "why": "Ordinary glue is not a magnetic material. The steel bar "
                    "itself has been magnetised by the magnet it is joined to."},
        ],
        "figure": None,
    },
    {
        "id": "p10-01-h23",
        "band": "harder",
        "text": "A hospital scanner uses a magnet thousands of times stronger than "
                "a fridge magnet. A steel wheelchair and an aluminium wheelchair "
                "frame are both nearby when it is switched on. Which frame is at "
                "risk of being pulled towards the machine, and why does the huge "
                "strength of the magnet not change your answer?",
        "options": [
            {"text": "Both frames are at equal risk, since both are metal and the "
             "magnet is extremely strong", "correct": False,
             "why": "Being a metal is not enough on its own — aluminium is never "
                    "pulled by any magnet, however strong."},
            {"text": "Neither frame is at risk, because scanners are designed to "
             "only affect magnetic materials that are actually inside a "
             "patient's body", "correct": False,
             "why": "A powerful magnet acts on any nearby magnetic material, "
                    "inside or outside the body, which is exactly why the steel "
                    "frame is dangerous near one."},
            {"text": "The aluminium frame, because extreme strength eventually "
             "affects every metal, magnetic or not", "correct": False,
             "why": "No amount of strength makes a magnet act on aluminium. "
                    "Strength changes how hard a magnetic material is pulled, "
                    "never whether a non-magnetic one responds."},
            {"text": "The steel frame is at risk; strength changes how hard "
             "something magnetic is pulled, never whether a non-magnetic "
             "material responds at all", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p10-01-h24",
        "band": "harder",
        "text": "A fridge magnet holds one sheet of paper against a steel door "
                "easily, but falls off once eight extra sheets are added between it "
                "and the door. What has changed?",
        "options": [
            {"text": "The gap between the magnet and the steel has grown, weakening "
             "the pull below what is needed to hold the magnet's own weight", "correct": True},
            {"text": "The extra paper has become slightly magnetic and is repelling "
             "the magnet", "correct": False,
             "why": "Paper is not a magnetic material and cannot be magnetised or "
                    "repel anything. The failure is simply the growing gap."},
            {"text": "The magnet has lost strength from being handled while the "
             "sheets were added, since handling always weakens a magnet a "
             "little", "correct": False,
             "why": "Ordinary handling like this does not weaken a magnet. The "
                    "extra thickness of paper is what has increased the gap and "
                    "dropped the pull."},
            {"text": "The steel door has become less magnetic under the extra paper", "correct": False,
             "why": "The paper does not touch or affect the steel's own "
                    "properties. What has changed is purely the gap to the magnet."},
        ],
        "figure": None,
    },
    {
        "id": "p10-01-h25",
        "band": "harder",
        "text": "A steel nail hangs from a magnet's south pole, with its own near "
                "end induced as a north pole. While still hanging from the magnet, "
                "the nail's near end is carefully touched onto a second, separate "
                "unmagnetised steel nail lying on the bench. What is most likely to "
                "happen to the second nail?",
        "options": [
            {"text": "The first nail loses its induced magnetism the moment it "
             "touches the second nail", "correct": False,
             "why": "Touching a second object does not remove the first nail's "
                    "induced magnetism — it is still hanging from the real magnet, "
                    "which keeps inducing it."},
            {"text": "It becomes weakly magnetised too, and may be picked up by the "
             "first nail", "correct": True},
            {"text": "Nothing happens, because the second nail is not touching the "
             "magnet itself", "correct": False,
             "why": "Direct contact with the original magnet is not required — the "
                    "first nail has itself become a weak magnet and can pass the "
                    "effect on by touch."},
            {"text": "The two nails repel each other on contact", "correct": False,
             "why": "Repulsion needs two like poles of two real magnets facing. "
                    "The second nail starts unmagnetised, so there is nothing for "
                    "it to repel with."},
        ],
        "figure": None,
    },
    {
        "id": "p10-01-h26",
        "band": "harder",
        "text": "Steel ball bearings and glass beads of the same size, shape and "
                "colour are mixed together in one box. Explain why simply looking "
                "at the mixture cannot tell you which is which, while a magnet test "
                "can, in a single step.",
        "options": [
            {"text": "Because a magnet works by weight, and steel and glass of the "
             "same size weigh differently", "correct": False,
             "why": "A magnet does not sort by weight. It responds to whether a "
                    "material is magnetic, which glass never is."},
            {"text": "Because looking at a mixture always fails to identify any "
             "material, magnetic or not", "correct": False,
             "why": "Looking often does work when materials differ visibly. The "
                    "problem here is specifically that these two look identical."},
            {"text": "Because glass and steel look identical here, but only the "
             "steel responds to a magnetic field", "correct": True},
            {"text": "Because glass is actually a magnetic material too, just a "
             "weaker one than steel", "correct": False,
             "why": "Glass is not magnetic at all, not even weakly. It is steel "
                    "alone that responds to the field."},
        ],
        "figure": None,
    },
    {
        "id": "p10-01-h27",
        "band": "harder",
        "text": "A very long steel rail is tested for magnetism by holding a loose "
                "paperclip near one end only, and the paperclip is pulled in. Can "
                "you be sure this is a genuine, deliberately magnetised magnet "
                "rather than steel that has simply picked up a little magnetism "
                "from something nearby?",
        "options": [
            {"text": "Yes, provided the rail is tested at both ends rather than just "
             "one", "correct": False,
             "why": "Testing at both ends still only produces attraction either "
                    "way, from a magnet or from induced steel — it does not add "
                    "the missing repulsion test."},
            {"text": "No — nothing about a long rail can ever be tested for "
             "magnetism with a paperclip", "correct": False,
             "why": "A paperclip test works perfectly well on a long rail. The "
                    "limitation is what attraction alone can prove, not the length "
                    "of the object."},
            {"text": "Yes — a paperclip being pulled in only happens with a genuine, "
             "deliberately magnetised magnet, never with steel magnetised by "
             "chance", "correct": False,
             "why": "Steel that has been weakly magnetised by induction attracts a "
                    "paperclip just as well as a genuine magnet does. Attraction "
                    "alone cannot tell the two apart."},
            {"text": "No — attraction alone cannot distinguish a real magnet from "
             "steel that has picked up a little magnetism; only a repulsion "
             "test with a known magnet could settle it", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p10-01-h28",
        "band": "harder",
        "text": "A student argues: \"If both poles of a magnet attract unmagnetised "
                "steel equally, then poles must not really matter.\" Is the "
                "student's reasoning sound?",
        "options": [
            {"text": "Partly — poles do not matter for whether unmagnetised steel is "
             "attracted, but they matter completely for whether two magnets "
             "attract or repel", "correct": True},
            {"text": "No — even unmagnetised steel is only attracted by one "
             "particular pole", "correct": False,
             "why": "Both poles attract unmagnetised steel equally well — the "
                    "student is right about that specific case."},
            {"text": "No — poles do not exist for unmagnetised objects, so the "
             "comparison the student is making is meaningless from the very "
             "start", "correct": False,
             "why": "The comparison is between the magnet's two REAL poles and how "
                    "each affects unmagnetised steel, which is a meaningful and "
                    "testable question."},
            {"text": "Yes — this proves poles never matter for any magnetic "
             "interaction", "correct": False,
             "why": "Poles matter completely for whether two MAGNETS attract or "
                    "repel. The student's claim only holds for one specific case."},
        ],
        "figure": None,
    },
    {
        "id": "p10-01-h29",
        "band": "harder",
        "text": "A magnet is snapped into two pieces of very different size. The "
                "two pieces are later pushed back together at the broken faces, "
                "lined up exactly as before the snap. Does this restore ONE "
                "original two-pole magnet, or leave TWO magnets stuck together?",
        "options": [
            {"text": "It restores one original magnet, because the faces line up "
             "exactly as before", "correct": False,
             "why": "Lining the faces up does not undo the cut. Each piece kept "
                    "its own pair of poles the moment it was snapped."},
            {"text": "Two magnets stuck together — each piece kept its own pair of "
             "poles the moment it was cut", "correct": True},
            {"text": "Neither — pushing the pieces back together destroys both "
             "magnets' poles at the join", "correct": False,
             "why": "Nothing about contact destroys a pole. Both pieces remain "
                    "complete magnets with two poles each, simply touching."},
            {"text": "One magnet, but now with two north poles and no south", "correct": False,
             "why": "Each piece still has one north and one south of its own — "
                    "putting them back in contact does not merge or cancel any "
                    "poles."},
        ],
        "figure": None,
    },
    {
        "id": "p10-01-h30",
        "band": "harder",
        "text": "A shop sells a fridge magnet claiming to be twice as strong as an "
                "ordinary one. A customer wants a rough, one-step check of this "
                "claim using only a steel washer, with no measuring equipment for "
                "force. Which observation would be reasonable evidence FOR the "
                "claim?",
        "options": [
            {"text": "The stronger magnet is a different colour from the ordinary "
             "one", "correct": False,
             "why": "Colour has no connection to magnetic strength at all."},
            {"text": "The stronger magnet takes longer to stick once it is brought "
             "close", "correct": False,
             "why": "A stronger magnet, if anything, would grip sooner and from "
                    "further away, not take longer."},
            {"text": "The stronger magnet holds the washer firmly from noticeably "
             "further away than the ordinary one does", "correct": True},
            {"text": "The stronger magnet is noticeably heavier to pick up than the "
             "ordinary one, since extra strength always adds extra mass", "correct": False,
             "why": "Weight is about mass, not magnetic strength. A heavier magnet "
                    "is not necessarily a stronger one."},
        ],
        "figure": None,
    },
]
