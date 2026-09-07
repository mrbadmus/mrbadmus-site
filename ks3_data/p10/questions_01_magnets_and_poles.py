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
            {"text": "A magnet with its opposite pole facing, or unmagnetised "
                     "steel",
             "correct": True},
            {"text": "A magnet with its like pole facing", "correct": False,
             "why": "Two like poles repel, so it would be pushed away rather "
                    "than pulled in."},
            {"text": "Only a magnet — nothing else is attracted",
             "correct": False,
             "why": "Unmagnetised iron and steel are attracted too, which is "
                    "why attraction proves nothing."},
            {"text": "Only unmagnetised steel — a magnet would repel",
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
            {"text": "Because the bar has a north pole at one end already",
             "correct": False,
             "why": "It is unmagnetised, so it has no poles until the magnet "
                    "gives it some."},
            {"text": "Because the magnet magnetises the bar first, so the "
                     "near end is always opposite",
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
]
