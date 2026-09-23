"""P8 lesson 03 — Current at a junction: twelve questions (MRB-223).

Written against Design's page. The river round the island, the two-branch
bench, the part–whole bar and both worked examples are hers.

The discriminations, in the order the lesson builds them:

  · what arrives at a junction LEAVES it, because nothing is stored at a
    point;
  · the branches are not given equal shares — halving is a special case
    (`CIRC-09`);
  · adding a branch costs the SUPPLY, not the neighbouring branch
    (`CIRC-10`) — the harder band sits here;
  · a milliamp reading is converted BEFORE it is added or taken away.

⚠️ POSITION IS AUTHORED AND MEASURED —
3,1,2,0 · 0,2,1,3 · 2,0,3,1;
the twelve fall 3/3/3/3 across the four indices.

⚠️ Neither ladder rung is restated (the three-branch 0.85 A junction, the
two parallel lamps with one unscrewed), and neither are the figures in the
worked examples (0.45 A with 0.15 A, 1.20 A with 250 mA) or in the two
attempts (the live bench, and 0.80 A with 320 mA).
"""

UNIT = "P8"
LESSON = "current-at-a-junction"
LESSON_NUMBER = 3

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "p8-03-e01",
        "band": "easier",
        "text": "A junction is…",
        "options": [
            {"text": "the point where the battery joins the circuit",
             "correct": False,
             "why": "A battery terminal is a connection, not a junction. A "
                    "junction is where a path divides or two paths meet."},
            {"text": "any component that splits a current in half",
             "correct": False,
             "why": "It is not a component at all, and it does not halve "
                    "anything — the branches take what they take."},
            {"text": "the switch that chooses which branch is used",
             "correct": False,
             "why": "A junction has no moving parts and chooses nothing. "
                    "Both branches are live at once."},
            {"text": "a point where a wire divides, or where two wires meet",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p8-03-e02",
        "band": "easier",
        "text": "Two branches leave a junction carrying 0.20 A and 0.50 A. "
                "What does the main wire carry?",
        "options": [
            {"text": "0.30 A", "correct": False,
             "why": "That is one branch taken from the other. The branch "
                    "currents ADD to make the main one."},
            {"text": "0.70 A", "correct": True},
            {"text": "0.35 A", "correct": False,
             "why": "That is the average of the two. An average is not the "
                    "total that had to arrive."},
            {"text": "0.50 A", "correct": False,
             "why": "That is the larger branch alone. The main wire has to "
                    "carry both."},
        ],
        "figure": None,
    },
    {
        "id": "p8-03-e03",
        "band": "easier",
        "text": "Why do the currents leaving a junction add up to the current "
                "arriving?",
        "options": [
            {"text": "Because the wires are all the same thickness",
             "correct": False,
             "why": "Thickness changes resistance, not the bookkeeping at a "
                    "point."},
            {"text": "Because the branches are always identical",
             "correct": False,
             "why": "They usually are not, and the rule still holds. It does "
                    "not depend on the branches matching."},
            {"text": "Because charge is neither made nor stored at a point",
             "correct": True},
            {"text": "Because the battery decides how much to send down each "
                     "one", "correct": False,
             "why": "The battery decides nothing about the split. Each "
                    "branch draws its own current."},
        ],
        "figure": None,
    },
    {
        "id": "p8-03-e04",
        "band": "easier",
        "text": "250 mA written in amps is…",
        "options": [
            {"text": "0.250 A", "correct": True},
            {"text": "2.50 A", "correct": False,
             "why": "That divides by a hundred. There are a thousand "
                    "milliamps in an amp."},
            {"text": "25 000 A", "correct": False,
             "why": "That multiplies instead of dividing. A milliamp is "
                    "smaller than an amp, so the number gets smaller."},
            {"text": "250 A", "correct": False,
             "why": "That drops the prefix without converting. The unit "
                    "cannot change while the number stays the same."},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "p8-03-s01",
        "band": "standard",
        "text": "A main wire carries 0.36 A into a junction with two "
                "branches. One branch reads 0.24 A. What does the other "
                "read?",
        "options": [
            {"text": "0.12 A", "correct": True},
            {"text": "0.60 A", "correct": False,
             "why": "That adds the branch to the whole. The whole is already "
                    "given; the missing branch is what is left of it."},
            {"text": "0.18 A", "correct": False,
             "why": "That halves the main current. The branches are not "
                    "equal here — one is already measured at 0.24 A."},
            {"text": "0.24 A", "correct": False,
             "why": "That is the branch you were given. The two branches "
                    "have to add to 0.36 A."},
        ],
        "figure": None,
    },
    {
        "id": "p8-03-s02",
        "band": "standard",
        "text": "A lamp branch and a buzzer branch leave the same junction. "
                "Why does the lamp branch carry more?",
        "options": [
            {"text": "Because the lamp is nearer the battery",
             "correct": False,
             "why": "Nearer means nothing here. Both branches have the same "
                    "battery across them."},
            {"text": "Because the junction sends more down the branch that "
                     "needs it", "correct": False,
             "why": "A junction sends nothing anywhere, and it has no way of "
                    "knowing what a branch needs."},
            {"text": "Because the lamp resists less, so more charge goes that "
                     "way each second", "correct": True},
            {"text": "Because a lamp needs more energy than a buzzer",
             "correct": False,
             "why": "It may well, and that is a consequence rather than the "
                    "cause. What sets the current is the resistance."},
        ],
        "figure": None,
    },
    {
        "id": "p8-03-s03",
        "band": "standard",
        "text": "Both branches of a junction are left open — nothing is "
                "connected in either. What do the three ammeters read?",
        "options": [
            {"text": "The main wire reads the battery's full current and the "
                     "branches read zero", "correct": False,
             "why": "A battery has no current of its own to read. With no "
                    "complete path, nothing flows anywhere."},
            # ⊕ MRB-297 · 1 Sep 2026 — this was the only one of the four
            # with no reason attached, and so the shortest by a clear margin.
            # The reason is added; the claim itself is unchanged.
            {"text": "All three read 0.00 A, because no complete path "
                     "exists anywhere", "correct": True},
            {"text": "The branches read zero and the main wire cannot be "
                     "read at all", "correct": False,
             "why": "It can be read, and it reads zero. A meter in a broken "
                    "loop gives a true reading of nothing."},
            {"text": "All three read the same small current, because the "
                     "meters themselves complete the loop", "correct": False,
             "why": "The meters are in the branches, and the branches are "
                    "open. There is still no path."},
        ],
        "figure": None,
    },
    {
        "id": "p8-03-s04",
        "band": "standard",
        "text": "A junction has three branches carrying 0.10 A, 0.10 A and "
                "0.10 A. What does the main wire carry, and what does that "
                "tell you about the branches?",
        "options": [
            {"text": "0.10 A — the branches all carry the same, so the main "
                     "wire does too", "correct": False,
             "why": "The main wire carries the TOTAL, not one branch's "
                    "share. Three equal branches still add."},
            {"text": "0.033 A — the main current shared three ways",
             "correct": False,
             "why": "That is the sum run backwards. The branch readings are "
                    "given; the main wire is what they add to."},
            {"text": "0.30 A — and it tells you each branch must always "
                     "take a third of whatever the main wire carries",
             "correct": False,
             "why": "The total is right and the rule is not. Change one "
                    "branch's component and the shares stop being thirds, "
                    "while the sum still holds."},
            {"text": "0.30 A — and it tells you the three branches happen to "
                     "match", "correct": True},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "p8-03-h01",
        "band": "harder",
        "text": "A junction feeds two branches. A student removes the second "
                "branch entirely and predicts the first will now carry "
                "double. What actually happens?",
        "options": [
            {"text": "The first branch doubles, because it now has the whole "
                     "supply to itself", "correct": False,
             "why": "It always had the whole supply across it. Removing a "
                    "neighbour changes nothing about its own branch."},
            {"text": "The first branch halves, because the circuit is now "
                     "harder to get round", "correct": False,
             "why": "The circuit overall IS harder to get round, and the "
                    "surviving branch is unchanged — same p.d., same "
                    "resistance, same current."},
            {"text": "The first branch carries exactly what it carried "
                     "before, and the main wire drops", "correct": True},
            {"text": "Both readings drop, because a junction with one branch "
                     "is no longer a junction", "correct": False,
             "why": "It stops being a junction and the surviving branch does "
                    "not notice: it has the same battery across it either "
                    "way."},
        ],
        "figure": None,
    },
    {
        "id": "p8-03-h02",
        "band": "harder",
        "text": "A junction's main wire reads 1.50 A. One branch reads "
                "600 mA. What does the other branch carry?",
        "options": [
            {"text": "0.900 A", "correct": True},
            {"text": "898.5 A", "correct": False,
             "why": "That takes 1.50 from 600 without converting. The "
                    "milliamps have to become amps first."},
            {"text": "0.750 A", "correct": False,
             "why": "That halves the main reading. One branch is already "
                    "measured, so the split is not even."},
            {"text": "2.10 A", "correct": False,
             "why": "That adds the branch to the whole. The whole is given; "
                    "the missing branch is what is left of it."},
        ],
        "figure": None,
    },
    {
        "id": "p8-03-h03",
        "band": "harder",
        "text": "Where a parallel section rejoins, the two branch currents "
                "meet. What does the wire beyond that second junction carry, "
                "compared with the wire before the first one?",
        "options": [
            {"text": "Less, because some charge is used up in the branches",
             "correct": False,
             "why": "Nothing is used up in a branch. Energy is transferred "
                    "there; the charge all comes back."},
            {"text": "More, because two branches feed into one wire",
             "correct": False,
             "why": "Two branches feed it, and they only give back what the "
                    "first junction gave them."},
            {"text": "It depends which branch resists more", "correct": False,
             "why": "The split depends on that. The TOTAL does not — it is "
                    "the same at both junctions whatever the branches are."},
            # ⊕ MRB-297 · 1 Sep 2026 — this was the only one of the four
            # with no reason attached, and so the shortest by a clear margin.
            # The reason is added; the claim itself is unchanged.
            {"text": "Exactly the same, because charge is conserved",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p8-03-h04",
        "band": "harder",
        "text": "A four-way extension lead is rated at 13 A. Someone works "
                "out that the four appliances plugged into it draw 3 A, 5 A, "
                "2 A and 4 A, and says it is fine because the biggest is only "
                "5 A. What is the danger?",
        "options": [
            {"text": "There is none — the lead is rated for each socket "
                     "separately", "correct": False,
             "why": "The rating is for the CABLE, which carries all four "
                    "currents added together."},
            {"text": "The sockets are branches off one cable, so the cable "
                     "carries 14 A and overheats", "correct": True},
            {"text": "The appliances will each get less than they need, so "
                     "they will run badly", "correct": False,
             "why": "Each branch has the full mains p.d. and draws what it "
                    "wants. Nothing is rationed; the cable simply has to "
                    "carry the total."},
            {"text": "The biggest appliance will take priority and the "
                     "others will cut out", "correct": False,
             "why": "There is no priority at a junction. All four draw at "
                    "once, which is exactly the problem."},
        ],
        "figure": None,
    },

    # ── MRB-335 top-up · easier ──────────────────────────────────────────
    {
        "id": "p8-03-e05",
        "band": "easier",
        "text": "At a junction, the current arriving is…",
        "options": [
            {"text": "equal to the currents leaving, added together",
             "correct": True},
            {"text": "shared equally between the branches", "correct": False,
             "why": "Each branch draws its own current, so an easier branch "
                    "takes more than a harder one."},
            {"text": "halved, because there are two ways to go",
             "correct": False,
             "why": "Halving would only be right if the branches happened to "
                    "be identical, and it is never the rule."},
            {"text": "larger than the currents leaving, because some is left "
                     "behind",
             "correct": False,
             "why": "Nothing is stored at a junction, so nothing can be left "
                    "behind there."},
        ],
        "figure": None,
    },
    {
        "id": "p8-03-e06",
        "band": "easier",
        "text": "Three branches carry 0.10 A, 0.20 A and 0.30 A. What does "
                "the main wire carry?",
        "options": [            {"text": "0.30 A, the largest branch", "correct": False,
             "why": "The main wire carries all three branches together, not "
                    "just the biggest."},
            {"text": "0.20 A, the middle value", "correct": False,
             "why": "An average is not what a junction does; the currents "
                    "add."},
            {"text": "0.006 A", "correct": False,
             "why": "That multiplies the three. Currents at a junction are "
                    "added, never multiplied."},
            {"text": "0.60 A", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p8-03-e07",
        "band": "easier",
        "text": "400 mA written in amps is…",
        "options": [
            {"text": "400 A", "correct": False,
             "why": "The m is milli, meaning a thousandth, so the number must "
                    "get smaller."},
            {"text": "0.4 A", "correct": True},
            {"text": "4 A", "correct": False,
             "why": "That divides by 100. A milliamp is a thousandth of an "
                    "amp, not a hundredth."},
            {"text": "40 A", "correct": False,
             "why": "That divides by 10, and a milliamp is a thousandth."},
        ],
        "figure": None,
    },
    {
        "id": "p8-03-e08",
        "band": "easier",
        "text": "Is any charge stored at a junction while a circuit runs?",
        "options": [
            {"text": "Yes, a little, which is why the branches read less",
             "correct": False,
             "why": "The branches add to exactly the main wire's reading, so "
                    "nothing has been kept."},
            {"text": "Yes, enough to run the circuit for a moment after "
                     "switch-off",
             "correct": False,
             "why": "A plain junction is just a meeting of wires and holds "
                    "nothing at all."},
            {"text": "No — whatever arrives at a junction leaves it",
             "correct": True},
            {"text": "Only in a parallel circuit, where the branches divide",
             "correct": False,
             "why": "Dividing is exactly where the rule is tested, and "
                    "nothing is stored there either."},
        ],
        "figure": None,
    },

    # ── MRB-335 top-up · standard ────────────────────────────────────────
    {
        "id": "p8-03-s05",
        "band": "standard",
        "text": "A main wire carries 0.75 A into a junction with two "
                "branches. One branch reads 0.45 A. What does the other read?",
        "options": [
            {"text": "1.20 A", "correct": False,
             "why": "That adds the two readings; a branch cannot carry more "
                    "than the main wire brings."},
            {"text": "0.375 A, half the main wire", "correct": False,
             "why": "Branches are not given equal shares — the other one "
                    "already reads 0.45 A."},
            {"text": "0.30 A", "correct": True},
            {"text": "0.75 A, the same as the main wire", "correct": False,
             "why": "That would leave nothing for the first branch, which "
                    "already carries 0.45 A."},
        ],
        "figure": None,
    },
    {
        "id": "p8-03-s06",
        "band": "standard",
        "text": "A third branch is added to a parallel section. What happens "
                "to the current in the MAIN wire?",
        "options": [
            {"text": "It rises, because it now carries three branch currents",
             "correct": True},
            {"text": "It falls, because the current is shared out more "
                     "thinly",
             "correct": False,
             "why": "Nothing is shared out. Each branch draws its own, and "
                    "the main wire carries the total."},
            {"text": "It stays the same, because the battery is unchanged",
             "correct": False,
             "why": "The battery has to supply more, and the main wire is "
                    "what delivers it."},
            {"text": "It stays the same until a fourth branch is added",
             "correct": False,
             "why": "Every branch added raises the total, from the very first "
                    "one."},
        ],
        "figure": None,
    },
    {
        "id": "p8-03-s07",
        "band": "standard",
        "text": "A main wire reads 1.20 A and its only two branches read "
                "0.50 A and 0.50 A. What should you conclude?",
        "options": [
            {"text": "That 0.20 A has been lost in the junction",
             "correct": False,
             "why": "Nothing is lost at a junction; the readings must add "
                    "exactly."},
            {"text": "That one of the three readings is wrong and should be "
                     "taken again",
             "correct": True},
            {"text": "That the main wire always reads more than the branches",
             "correct": False,
             "why": "It reads their TOTAL, which here would be 1.00 A, not "
                    "more than it."},
            {"text": "That there must be a third branch somewhere",
             "correct": False,
             "why": "That is worth checking, but the question says these are "
                    "its only two branches."},
        ],
        "figure": None,
    },
    {
        "id": "p8-03-s08",
        "band": "standard",
        "text": "Two branches carry 250 mA and 0.35 A. What does the main "
                "wire carry, in amps?",
        "options": [
            {"text": "250.35 A", "correct": False,
             "why": "The milliamps were added as though they were amps; "
                    "250 mA is 0.25 A."},
            {"text": "0.60 A", "correct": True},
            {"text": "0.10 A", "correct": False,
             "why": "That subtracts. Currents leaving a junction are added to "
                    "give the current arriving."},
            {"text": "2.85 A", "correct": False,
             "why": "That adds 0.35 to 2.5, misreading 250 mA as 2.5 A."},
        ],
        "figure": None,
    },

    # ── MRB-335 top-up · harder ──────────────────────────────────────────
    {
        "id": "p8-03-h05",
        "band": "harder",
        "text": "A junction feeds three branches carrying 0.30 A, 250 mA and "
                "0.15 A. The main wire is rated at 0.65 A. Is it safe?",
        "options": [
            {"text": "Yes — no single branch is anywhere near 0.65 A",
             "correct": False,
             "why": "The rating applies to the main wire, which carries all "
                    "three branches together."},
            {"text": "Yes — the branches total 0.55 A", "correct": False,
             "why": "That reads 250 mA as 0.05 A. It is 0.25 A, so the total "
                    "is 0.70 A."},
            {"text": "No — the branches total 0.70 A, above the rating",
             "correct": True},
            {"text": "It cannot be judged without the supply voltage",
             "correct": False,
             "why": "A current rating is compared with a current, and all "
                    "three branch currents are given."},
        ],
        "figure": None,
    },
    {
        "id": "p8-03-h06",
        "band": "harder",
        "text": "A student finds the total at a junction by adding all four "
                "ammeter readings — the main wire and the three branches. "
                "What is wrong?",
        "options": [
            {"text": "The branches should be multiplied together, not added",
             "correct": False,
             "why": "Adding the branches is exactly right; it is the fourth "
                    "reading that does not belong."},
            {"text": "Only two branches may be added at a time",
             "correct": False,
             "why": "Any number of branches may be added; the rule does not "
                    "stop at two."},
            {"text": "The main wire's reading IS the total, so it is counted "
                     "twice",
             "correct": True},
            {"text": "The main wire should be subtracted rather than added",
             "correct": False,
             "why": "Subtracting it would give zero, which is not a total "
                    "either — it simply should not be in the sum."},
        ],
        "figure": None,
    },
    {
        "id": "p8-03-h07",
        "band": "harder",
        "text": "One of two identical branches is replaced by a component "
                "that resists twice as much. What happens to the main-wire "
                "current?",
        "options": [
            {"text": "It stays the same, because the number of branches has "
                     "not changed",
             "correct": False,
             "why": "The total is the sum of what the branches draw, and one "
                    "of them now draws less."},
            {"text": "It falls, because the new branch draws less current "
                     "than the old one",
             "correct": True},
            {"text": "It rises, because a harder branch pushes more current "
                     "into the other",
             "correct": False,
             "why": "Branches do not push current into one another; each "
                    "simply draws its own."},
            {"text": "It halves, because one branch resists twice as much",
             "correct": False,
             "why": "Only that branch halves. The other is unchanged, so the "
                    "total falls by less than half."},
        ],
        "figure": None,
    },
    {
        "id": "p8-03-h08",
        "band": "harder",
        "text": "A main wire reads 0.90 A. One branch is switched off and the "
                "remaining branch still reads 0.40 A. What did the "
                "switched-off branch carry?",
        "options": [
            {"text": "0.90 A, the whole main-wire reading", "correct": False,
             "why": "That would leave nothing for the branch that is still "
                    "carrying 0.40 A."},
            {"text": "0.40 A, the same as the other branch", "correct": False,
             "why": "Branches are not given equal shares; the sum has to come "
                    "to 0.90 A."},
            {"text": "1.30 A", "correct": False,
             "why": "That adds the two readings, and no branch can carry more "
                    "than the main wire delivers."},
            {"text": "0.50 A", "correct": True},
        ],
        "figure": None,
    },

    # ── MRB-338 night 3 top-up · easier ───────────────────────────────

    {"id": "p8-03-e09", "band": "easier",
     "text": "A junction has two branches leaving it, carrying 0.15 A and "
             "0.35 A. What does the wire arriving at the junction carry?",
     "options": [
         {"text": "0.50 A", "correct": True},
         {"text": "0.35 A, the larger of the two branches alone",
          "correct": False,
          "why": "The main wire has to carry both branches together, not "
                 "just whichever one happens to be bigger."},
         {"text": "0.175 A, the average of the two branches",
          "correct": False,
          "why": "An average is not what arrives at a junction; the two "
                 "branch currents add together instead."},
         {"text": "0.20 A, the difference between the two", "correct": False,
          "why": "Subtracting compares the two branches; the arriving "
                 "current is what they add up to, not their difference."},
     ], "figure": None},
    {"id": "p8-03-e10", "band": "easier",
     "text": "What word describes a point where a single wire divides into "
             "two, or where two wires join into one?",
     "options": [
         {"text": "A terminal", "correct": False,
          "why": "A terminal is a connection point on a cell or battery, "
                 "not a point where wires split or join."},
         {"text": "A junction", "correct": True},
         {"text": "A resistor", "correct": False,
          "why": "A resistor is a component that resists current; it is "
                 "not the name for a splitting or joining point."},
         {"text": "A loop", "correct": False,
          "why": "A loop describes a whole complete path, not the "
                 "specific point where paths divide or meet."},
     ], "figure": None},
    {"id": "p8-03-e11", "band": "easier",
     "text": "Two branches at a junction are drawn the same length in a "
             "diagram. Does that guarantee they carry the same current?",
     "options": [
         {"text": "No — only the components in each branch decide the "
                  "current, not how the diagram is drawn", "correct": True},
         {"text": "Yes — equal lengths on the diagram always mean equal "
                  "currents", "correct": False,
          "why": "Length on a diagram carries no information about "
                 "current at all; two very different components could "
                 "still be drawn the same length."},
         {"text": "Yes, but only when the two branches use the same "
                  "type of component", "correct": False,
          "why": "Even two of the same TYPE of component can have "
                 "different resistances, so equal diagram length still "
                 "guarantees nothing about the current."},
         {"text": "It depends on how far the branches are from the "
                  "battery in the diagram", "correct": False,
          "why": "Distance on a diagram, like length, carries no "
                 "information about current; only the branches' own "
                 "resistance decides that."},
     ], "figure": None},
    {"id": "p8-03-e12", "band": "easier",
     "text": "One branch of a junction carries 0.4 A and the other carries "
             "450 mA. Which branch carries the larger current?",
     "options": [
         {"text": "The 0.4 A branch, because 0.4 is the larger number of "
                  "the two written down", "correct": False,
          "why": "The two readings are in different units, so the bare "
                 "numbers cannot be compared: 450 mA is 0.45 A, which "
                 "beats 0.4 A."},
         {"text": "The 0.4 A branch, because amps are the larger unit of "
                  "the two", "correct": False,
          "why": "An amp is indeed larger than a milliamp, but there are "
                 "450 milliamps here, and 450 thousandths of an amp comes "
                 "to 0.45 A."},
         {"text": "The 450 mA branch, because 450 mA is 0.45 A",
          "correct": True},
         {"text": "Neither — the two readings cannot be compared until "
                  "both branches are measured again", "correct": False,
          "why": "They can be compared straight away by converting one "
                 "of them: 450 mA becomes 0.45 A, and 0.45 A is larger "
                 "than 0.4 A."},
     ], "figure": None},
    {"id": "p8-03-e13", "band": "easier",
     "text": "Is any charge ever created at a junction, to top up what "
             "arrives there?",
     "options": [
         {"text": "No — nothing is made or stored there, so what leaves "
                  "equals what arrives", "correct": True},
         {"text": "Yes, a little, whenever the branches are unequal",
          "correct": False,
          "why": "Unequal branches change how the current splits, not "
                 "whether any is created — nothing is ever made at a "
                 "junction."},
         {"text": "Yes, but only in a junction with three branches or "
                  "more", "correct": False,
          "why": "The number of branches makes no difference; a junction "
                 "never creates charge, whatever its shape."},
         {"text": "It depends on how much current is already flowing "
                  "through it", "correct": False,
          "why": "The size of the current does not change the rule — a "
                 "junction never creates or stores charge, whatever the "
                 "size of the flow."},
     ], "figure": None},
    {"id": "p8-03-e14", "band": "easier",
     "text": "A junction's main wire reads 0.90 A, and one branch reads "
             "0.90 A as well. What must be true of the other branch?",
     "options": [
         {"text": "It reads 0.90 A too, since both branches must match",
          "correct": False,
          "why": "The two branches must add to 0.90 A; if one already is "
                 "0.90 A, the other cannot be as well."},
         {"text": "It reads 0.00 A", "correct": True},
         {"text": "It cannot be worked out without more information",
          "correct": False,
          "why": "It can — the branches must add to the main reading, so "
                 "the second branch is 0.90 A minus 0.90 A."},
         {"text": "It reads 0.45 A, half of the main wire",
          "correct": False,
          "why": "Halving would only be right if the two branches were "
                 "equal, and here one branch already accounts for the "
                 "whole main reading."},
     ], "figure": None},
    {"id": "p8-03-e15", "band": "easier",
     "text": "A junction splits into three branches instead of two. Does "
             "the same \"currents add up\" rule still apply?",
     "options": [
         {"text": "No — the rule only works for exactly two branches",
          "correct": False,
          "why": "The rule comes from charge never being created or "
                 "stored at a point, which does not depend on how many "
                 "branches there are."},
         {"text": "No — with three or more branches you must average "
                  "them instead", "correct": False,
          "why": "Averaging is never the rule at a junction, whatever "
                 "the number of branches; they always add."},
         {"text": "Yes — the three branch currents simply add to give "
                  "the main current", "correct": True},
         {"text": "It depends on whether the three branches are "
                  "identical to each other", "correct": False,
          "why": "The branches do not need to be identical — whatever "
                 "they carry, their currents still add to the main "
                 "reading."},
     ], "figure": None},
    {"id": "p8-03-e16", "band": "easier",
     "text": "A branch current of 0.25 A, written in milliamps, is…",
     "options": [
         {"text": "0.00025 mA", "correct": False,
          "why": "That divides by a thousand. Going from amps to "
                 "milliamps means the number gets larger, not smaller."},
         {"text": "25 mA", "correct": False,
          "why": "That multiplies by a hundred. There are a thousand "
                 "milliamps in every amp, not a hundred."},
         {"text": "2.5 mA", "correct": False,
          "why": "That multiplies by ten, nowhere near enough: a "
                 "milliamp is a thousandth of an amp."},
         {"text": "250 mA", "correct": True},
     ], "figure": None},
    {"id": "p8-03-e17", "band": "easier",
     "text": "A junction's main wire carries 0.50 A. One branch is later "
             "found to carry 0.50 A on its own. Roughly how many other "
             "branches with any real current could there be?",
     "options": [
         {"text": "None — a second branch would need its own current, "
                  "and none is left over from the 0.50 A total",
          "correct": True},
         {"text": "Exactly one more, carrying another 0.50 A",
          "correct": False,
          "why": "The branches must add up to the main wire's 0.50 A; a "
                 "second branch carrying another 0.50 A would make the "
                 "total too large."},
         {"text": "As many as you like, since the main wire sets no "
                  "limit on the branches", "correct": False,
          "why": "The branches are limited by the main wire's total — "
                 "here they must add to exactly 0.50 A."},
         {"text": "Exactly two more, each carrying a small share",
          "correct": False,
          "why": "Any further branch would need some of the 0.50 A, but "
                 "the one known branch already accounts for all of it."},
     ], "figure": None},
    {"id": "p8-03-e18", "band": "easier",
     "text": "A student says a junction \"decides\" how much current each "
             "branch gets. Is that a fair description?",
     "options": [
         {"text": "Yes — the junction divides the arriving current evenly "
                  "between its branches before sending it on",
          "correct": False,
          "why": "Nothing at a junction divides anything, and the shares "
                 "are not even: an easier branch takes more current than "
                 "a harder one."},
         {"text": "No — a junction has no way of deciding anything; each "
                  "branch decides its own current", "correct": True},
         {"text": "Yes — a junction can send more current down whichever "
                  "branch happens to need it most", "correct": False,
          "why": "A junction has no means of sending or choosing "
                 "anything; each branch simply draws what it draws."},
         {"text": "Yes, but only when the branches are very different "
                  "from each other", "correct": False,
          "why": "Whether the branches are alike or very different, a "
                 "junction still decides nothing — each branch sets its "
                 "own current."},
     ], "figure": None},
    {"id": "p8-03-e19", "band": "easier",
     "text": "50 mA, written in amps, is…",
     "options": [
         {"text": "50 A", "correct": False,
          "why": "That leaves the number unchanged, but converting "
                 "milliamps to amps must make it smaller."},
         {"text": "500 A", "correct": False,
          "why": "That multiplies instead of dividing; milliamps convert "
                 "to a SMALLER number of amps."},
         {"text": "0.050 A", "correct": True},
         {"text": "5.0 A", "correct": False,
          "why": "That divides by 10 rather than 1000, giving a value a "
                 "hundred times too large."},
     ], "figure": None},
    {"id": "p8-03-e20", "band": "easier",
     "text": "A junction's main wire is found to read LESS than one of its "
             "own branches. What must be true?",
     "options": [
         {"text": "The junction has somehow removed some current",
          "correct": False,
          "why": "A junction cannot remove any current; nothing is ever "
                 "made or stored there."},
         {"text": "The branch must be measured in different units from "
                  "the main wire", "correct": False,
          "why": "Different units could explain a strange-looking "
                 "comparison, but not a genuine reading below what one "
                 "branch itself carries."},
         {"text": "This is normal whenever there are two or more "
                  "branches", "correct": False,
          "why": "It is never normal — the main wire always carries the "
                 "sum of the branches, which cannot be less than any one "
                 "of them."},
         {"text": "One of the two readings must simply be wrong",
          "correct": True},
     ], "figure": None},
    {"id": "p8-03-e21", "band": "easier",
     "text": "A junction has one branch carrying current and a second "
             "branch that is completely open, with nothing connected. "
             "What does the main wire carry?",
     "options": [
         {"text": "Exactly what the one working branch carries",
          "correct": True},
         {"text": "Half of what the one working branch carries",
          "correct": False,
          "why": "Halving would need two branches actually sharing the "
                 "load; an open branch contributes nothing to share."},
         {"text": "More than the working branch, since the junction "
                  "boosts the total", "correct": False,
          "why": "A junction never adds current of its own; the open "
                  "branch simply contributes nothing."},
         {"text": "Nothing, since one of the two branches is not "
                  "carrying anything", "correct": False,
          "why": "The open branch carrying nothing does not stop the "
                 "other branch's current from reaching the main wire."},
     ], "figure": None},
    {"id": "p8-03-e22", "band": "easier",
     "text": "In a parallel section, which carries the larger current — "
             "the main wire, or any one of the branches?",
     "options": [
         {"text": "Whichever of the two happens to have the thicker "
                  "wire", "correct": False,
          "why": "Wire thickness does not decide it. The main wire "
                 "carries every branch's current together, so it reads "
                 "more than any single branch whatever it is made of."},
         {"text": "The main wire, because it carries every branch's "
                  "current together", "correct": True},
         {"text": "They carry the same, because the current is the same "
                  "everywhere in a circuit", "correct": False,
          "why": "That is the rule for a single loop with no branches. "
                 "Once the path divides, each branch takes only part of "
                 "what the main wire brought."},
         {"text": "Any one branch, because the branches are where the "
                  "components actually sit", "correct": False,
          "why": "Where the components sit makes no difference to the "
                 "bookkeeping: the branch currents add up to make the "
                 "main wire's, so no branch can beat it."},
     ], "figure": None},
    {"id": "p8-03-e23", "band": "easier",
     "text": "A junction has four branches instead of two or three. Is "
             "there anything special about the rule for four branches?",
     "options": [
         {"text": "Yes — a junction with four branches shares the "
                  "current out equally between them", "correct": False,
          "why": "Branches are never given equal shares by the number of "
                 "them; each draws its own current regardless."},
         {"text": "Yes — with four branches the main wire carries the "
                  "largest branch's current rather than the total",
          "correct": False,
          "why": "The main wire carries the total of every branch, "
                 "whatever the number of them; the largest branch on its "
                 "own is never what it reads."},
         {"text": "No — the same adding rule applies whatever the number "
                  "of branches happens to be", "correct": True},
         {"text": "Yes — four branches need to be paired up and added "
                  "two at a time before finding the total",
          "correct": False,
          "why": "There is no pairing step; all the branch currents "
                 "simply add together directly, however many there are."},
     ], "figure": None},
    {"id": "p8-03-e24", "band": "easier",
     "text": "Which instrument would you use to measure the current "
             "arriving at a junction?",
     "options": [
         {"text": "A voltmeter, connected across the junction point",
          "correct": False,
          "why": "A junction is a single point, not a component with two "
                 "ends to connect a voltmeter across."},
         {"text": "An ammeter, connected across the junction rather than "
                  "wired into a wire", "correct": False,
          "why": "An ammeter has to be wired into the loop so the "
                 "current runs through it, not connected across a "
                 "point."},
         {"text": "A voltmeter, wired into the main wire", "correct": False,
          "why": "A voltmeter in the loop would almost stop the current "
                 "rather than measure it; that is an ammeter's job."},
         {"text": "An ammeter, wired directly into the main wire itself",
          "correct": True},
     ], "figure": None},
    {"id": "p8-03-e25", "band": "easier",
     "text": "A junction's main wire carries 0.65 A. Two branches leave "
             "it, one reading 0.40 A. What must the other read?",
     "options": [
         {"text": "0.25 A", "correct": True},
         {"text": "0.40 A, the same as the known branch", "correct": False,
          "why": "That is the branch you were already given — the two "
                 "branches have to add to 0.65 A, not both equal it."},
         {"text": "1.05 A, the two given values added together",
          "correct": False,
          "why": "That adds the branch to the whole; the missing branch "
                 "is what remains of the whole once the known branch is "
                 "taken away."},
         {"text": "0.325 A, half of the main wire", "correct": False,
          "why": "Halving only applies when the branches happen to "
                 "match; here one is already known to be 0.40 A."},
     ], "figure": None},
    {"id": "p8-03-e26", "band": "easier",
     "text": "Two branches carrying different currents rejoin further "
             "along the wire, back into a single path. What happens to "
             "the two currents at that point?",
     "options": [
         {"text": "The smaller one is discarded and only the larger one "
                  "continues", "correct": False,
          "why": "Nothing is discarded at a junction; both branch "
                 "currents continue on, added together."},
         {"text": "They add together to make the one single onward "
                  "current from there", "correct": True},
         {"text": "They stay separate, travelling side by side in the "
                  "same wire", "correct": False,
          "why": "Once wires join into one, there is only one wire and "
                 "one current in it, not two currents running side by "
                 "side."},
         {"text": "They cancel each other out, leaving no current at "
                  "all", "correct": False,
          "why": "Currents joining at a junction add together; they do "
                 "not cancel unless they happen to flow in opposite "
                 "directions, which is not the case here."},
     ], "figure": None},
    {"id": "p8-03-e27", "band": "easier",
     "text": "A single junction has three branches: one carries 0.10 A, "
             "one carries 0.20 A, and the third is completely open. What "
             "does the main wire carry?",
     "options": [
         {"text": "0.15 A, the average of the two working branches",
          "correct": False,
          "why": "Averaging is never the rule at a junction; the working "
                 "branches simply add together."},
         {"text": "0.20 A, the larger of the two working branches",
          "correct": False,
          "why": "The main wire carries both working branches added "
                 "together, not just the larger one on its own."},
         {"text": "0.30 A", "correct": True},
         {"text": "0.10 A, ignoring the open branch entirely and using "
                  "only the smaller reading", "correct": False,
          "why": "The main wire is not limited to the smaller of the "
                 "working branches; it carries the sum of both."},
     ], "figure": None},
    {"id": "p8-03-e28", "band": "easier",
     "text": "A junction has two branches. One is switched off. Is the "
             "junction itself switched off as well?",
     "options": [
         {"text": "Yes — a junction stops existing once any one of its "
                  "branches is switched off", "correct": False,
          "why": "The junction is just a point where wires meet; it "
                 "still exists whether or not every branch is working."},
         {"text": "Yes, but only if the switched-off branch was carrying "
                  "more current than the other", "correct": False,
          "why": "Which branch was carrying more makes no difference; "
                 "the junction remains a junction regardless."},
         {"text": "It depends on whether the main wire is also "
                  "switched off", "correct": False,
          "why": "The main wire's own switch state does not decide "
                 "whether the point where the branches meet still counts "
                 "as a junction."},
         {"text": "No — the junction still exists; it simply has one "
                  "fewer working branch feeding into it", "correct": True},
     ], "figure": None},
    {"id": "p8-03-e29", "band": "easier",
     "text": "350 mA, written in amps, is…",
     "options": [
         {"text": "0.350 A", "correct": True},
         {"text": "35.0 A", "correct": False,
          "why": "That divides by 10, a far smaller conversion than "
                 "milliamps to amps needs."},
         {"text": "350 A", "correct": False,
          "why": "That leaves the number unchanged; converting from "
                 "milliamps to amps has to make it smaller."},
         {"text": "3.50 A", "correct": False,
          "why": "That divides by 100 rather than 1000, giving ten times "
                 "too large a value."},
     ], "figure": None},
    {"id": "p8-03-e30", "band": "easier",
     "text": "A junction feeds a lamp branch and a buzzer branch. Does the "
             "lamp's own branch current depend on what the buzzer branch "
             "happens to be doing?",
     "options": [
         {"text": "It depends on which branch is drawn closer to the "
                  "battery in the diagram", "correct": False,
          "why": "Position on a diagram has no bearing on a branch's own "
                 "current; only its own resistance and the battery's "
                 "push decide that."},
         {"text": "No — each branch draws its own current, set by its "
                  "own resistance", "correct": True},
         {"text": "Yes — whichever branch switches on first draws more "
                  "current from the junction", "correct": False,
          "why": "Order of switching on makes no difference; each "
                 "branch's current depends only on its own resistance "
                 "and the battery's push."},
         {"text": "Yes — the two branches always share the total "
                  "current equally between them", "correct": False,
          "why": "Equal sharing only happens if the two branches happen "
                 "to resist the same amount; generally each draws its "
                 "own different current."},
     ], "figure": None},
    # ── MRB-338 night 3 top-up · standard ─────────────────────────────

    {"id": "p8-03-s09", "band": "standard",
     "text": "A junction's main wire carries 0.55 A. One branch reads "
             "300 mA. What does the other branch read, in amps?",
     "options": [
         {"text": "0.25 A", "correct": True},
         {"text": "0.52 A, subtracting 3 hundredths of an amp",
          "correct": False,
          "why": "That misreads 300 mA as 0.03 A; it is actually 0.30 A, "
                 "ten times larger."},
         {"text": "0.40 A, half the main wire", "correct": False,
          "why": "Halving is only right when the branches happen to "
                 "match; here one branch is already known to be 0.30 A."},
         {"text": "0.85 A, the two readings added without converting",
          "correct": False,
          "why": "That treats 300 mA as though it were 0.30 more amps "
                 "added on top, rather than a value to convert then "
                 "subtract."},
     ], "figure": None},
    {"id": "p8-03-s10", "band": "standard",
     "text": "A junction has three branches: 0.15 A, 0.25 A and an "
             "unknown third. The main wire reads 0.70 A. What does the "
             "third branch carry?",
     "options": [
         {"text": "0.233 A, sharing the main wire equally among three "
                  "branches", "correct": False,
          "why": "Equal sharing is not the rule here — two branches are "
                 "already measured unequally, so the third is whatever "
                 "is left of the total."},
         {"text": "0.30 A", "correct": True},
         {"text": "1.10 A, all three values added together",
          "correct": False,
          "why": "That adds the third branch's unknown value on top of "
                 "the total, but the total is already given as 0.70 A."},
         {"text": "0.40 A, the two known branches added", "correct": False,
          "why": "That gives the combined size of the two KNOWN "
                 "branches, not what remains for the third one."},
     ], "figure": None},
    {"id": "p8-03-s11", "band": "standard",
     "text": "A junction feeds a lamp and a heater. The heater is "
             "switched off partway through, while the lamp keeps running. "
             "What happens to the lamp's own branch current?",
     "options": [
         {"text": "It becomes impossible to predict without knowing the "
                  "heater's exact resistance", "correct": False,
          "why": "The heater's resistance does not matter here — the "
                 "lamp's branch is entirely independent of what the "
                 "heater's branch is doing."},
         {"text": "It rises, since it no longer has to share the "
                  "junction with the heater", "correct": False,
          "why": "Branches are never given a share to begin with, so "
                 "there is nothing extra for the lamp to inherit when "
                 "the heater switches off."},
         {"text": "Nothing changes for the lamp's own branch current; "
                  "only the main wire's total reading falls",
          "correct": True},
         {"text": "It falls, since the junction now has less total "
                  "current passing through it", "correct": False,
          "why": "The lamp's own branch is set by its own resistance and "
                 "the battery's push, not by the size of the total at "
                 "the junction."},
     ], "figure": None},
    {"id": "p8-03-s12", "band": "standard",
     "text": "Two ammeters are placed on either side of a junction that "
             "has only ONE branch connected (the rest are switched off or "
             "unconnected). Compare the two readings.",
     "options": [
         {"text": "The one after the junction reads higher, since the "
                  "branch adds its own push", "correct": False,
          "why": "A branch does not add any push of its own; the "
                 "current is unchanged from one side of the junction to "
                 "the other."},
         {"text": "They cannot be compared without knowing the branch's "
                  "resistance", "correct": False,
          "why": "With only one working branch, all the current has to "
                 "go through it, so the two readings must match "
                 "regardless of its resistance."},
         {"text": "The one before the junction reads higher, since it "
                  "has not yet been divided", "correct": False,
          "why": "Nothing is divided when there is only one working "
                 "branch; both readings show exactly the same current."},
         {"text": "They are identical, since the whole main current "
                  "simply passes into the one working branch",
          "correct": True},
     ], "figure": None},
    {"id": "p8-03-s13", "band": "standard",
     "text": "A junction feeds a branch that is just a plain wire link "
             "(no lamp or resistor) alongside a branch with a lamp in "
             "it. Which branch carries more current, and why?",
     "options": [
         {"text": "The wire-link branch, since it offers almost no "
                  "resistance compared with the lamp's branch",
          "correct": True},
         {"text": "The lamp's branch, since a lamp actively draws "
                  "current towards itself", "correct": False,
          "why": "A lamp does not draw current towards itself; it "
                 "simply resists the flow, which is exactly why the "
                 "plain wire carries more."},
         {"text": "Both branches carry the same current, since they are "
                  "both connected to the same junction", "correct": False,
          "why": "Sharing the same junction does not mean sharing the "
                 "same current; each branch draws according to its own "
                 "resistance."},
         {"text": "It cannot be judged without knowing the battery's "
                  "exact push", "correct": False,
          "why": "Whatever the battery's push, the branch with almost "
                 "no resistance always carries the larger current of "
                 "the two."},
     ], "figure": None},
    {"id": "p8-03-s14", "band": "standard",
     "text": "A junction has two branches. A student measures the main "
             "wire twice, a minute apart, and gets 0.40 A both times, but "
             "the two branch readings are different each time. Is that "
             "possible?",
     "options": [
         {"text": "It is possible just if one of the branches has been "
                  "physically swapped for a different component",
          "correct": False,
          "why": "A physical swap is one way the split could change, but "
                 "so is simply adjusting a variable resistor without "
                 "swapping anything."},
         {"text": "Yes — as long as the two branch readings still add to "
                  "0.40 A each time, the split between them can change",
          "correct": True},
         {"text": "No — identical main-wire readings must mean identical "
                  "branch readings every time", "correct": False,
          "why": "The main wire only fixes the TOTAL; the split between "
                 "the branches can shift, for instance if a variable "
                 "resistor is adjusted, while the total stays the same."},
         {"text": "No — a junction splits its current in a fixed ratio "
                  "between its branches every time", "correct": False,
          "why": "There is no fixed ratio at a junction; each branch "
                 "draws whatever its own resistance allows at the time."},
     ], "figure": None},
    {"id": "p8-03-s15", "band": "standard",
     "text": "A junction has three branches carrying 0.12 A, 0.18 A and "
             "0.20 A. A fourth branch is then added, carrying 0.10 A. "
             "What does the main wire now carry?",
     "options": [
         {"text": "0.50 A, ignoring the new fourth branch entirely",
          "correct": False,
          "why": "The new branch is a genuine addition to the junction "
                 "and has to be included in the total."},
         {"text": "0.15 A, the average of all four branches",
          "correct": False,
          "why": "Averaging is never the rule at a junction — every "
                 "branch current is added, not averaged."},
         {"text": "0.60 A", "correct": True},
         {"text": "0.40 A, the three smallest branches added, dropping "
                  "the largest", "correct": False,
          "why": "No branch is dropped from the sum; every branch, "
                 "however large or small its current, is added to the "
                 "total."},
     ], "figure": None},
    {"id": "p8-03-s16", "band": "standard",
     "text": "A junction feeds a lamp branch reading 0.30 A. A second, "
             "identical lamp is then added as a new branch off the SAME "
             "junction. What does the main wire read afterwards?",
     "options": [
         {"text": "0.90 A, since three lamps' worth of current is now "
                  "expected", "correct": False,
          "why": "There are only two lamps in this arrangement, not "
                 "three, so the total is twice one lamp's current, not "
                 "three times it."},
         {"text": "0.30 A, unchanged, since the lamps are identical",
          "correct": False,
          "why": "Being identical does not stop the second lamp from "
                 "adding its own current; the main wire has to carry "
                 "both branches now."},
         {"text": "0.15 A, since the current now splits between two "
                  "identical lamps", "correct": False,
          "why": "Splitting an existing current is not what happens "
                 "when a NEW branch is added — the first lamp's own "
                 "current is unaffected, and the new one adds its own."},
         {"text": "0.60 A", "correct": True},
     ], "figure": None},
    {"id": "p8-03-s17", "band": "standard",
     "text": "An extension lead rated at 10 A has two appliances plugged "
             "into it, drawing 400 mA and 3.5 A. Is the lead safe?",
     "options": [
         {"text": "Yes — the two currents add to about 3.9 A, "
                  "comfortably under the 10 A rating", "correct": True},
         {"text": "No — the lead's rating covers just one appliance at a "
                  "time, however small the currents are", "correct": False,
          "why": "A lead's rating is for the TOTAL current it carries, "
                 "which can come from several appliances plugged in "
                 "together."},
         {"text": "It cannot be judged without knowing the lead's own "
                  "resistance", "correct": False,
          "why": "The lead's own resistance is not needed here — its "
                 "safety is judged by comparing the total current drawn "
                 "with its stated rating."},
         {"text": "No — 400 mA is nearly half of 3.5 A, which makes the "
                  "combination too close to the rating", "correct": False,
          "why": "400 mA is only 0.4 A, a small fraction of 3.5 A, and "
                 "the combined total is nowhere near the 10 A rating."},
     ], "figure": None},
    {"id": "p8-03-s18", "band": "standard",
     "text": "A parallel section's two junctions — one where the branches "
             "divide, one further along where they rejoin — each have "
             "their own ammeter reading the total. Under what "
             "circumstance would you expect these two ammeters to "
             "disagree?",
     "options": [
         {"text": "They should never genuinely disagree; a real "
                  "difference points to a measurement or wiring fault, "
                  "not a real physical difference", "correct": True},
         {"text": "Whenever the two branches carry very different "
                  "currents from each other, since the bigger branch "
                  "reaches the rejoining point first", "correct": False,
          "why": "How unevenly the current splits between the branches "
                 "makes no difference — the TOTAL is still the same at "
                 "both junctions either way."},
         {"text": "Whenever one of the branches contains a resistor "
                  "rather than a lamp", "correct": False,
          "why": "The type of component in a branch changes how the "
                 "current splits, not whether the two junctions' totals "
                 "agree with each other."},
         {"text": "Whenever the parallel section has three or more "
                  "branches instead of two, since more branches leave "
                  "more room for the two totals to drift apart",
          "correct": False,
          "why": "The number of branches makes no difference; the total "
                 "passing the dividing junction always equals the total "
                 "passing the rejoining one."},
     ], "figure": None},
    {"id": "p8-03-s19", "band": "standard",
     "text": "Which measurement, on its own, tells you the LEAST about "
             "how current is split between two branches of a junction: "
             "the main wire's reading, or one branch's reading?",
     "options": [
         {"text": "Both tell you exactly the same amount about the "
                  "split", "correct": False,
          "why": "A single branch reading gives you one exact share of "
                 "the split; the main wire's total alone gives you none "
                 "of that detail."},
         {"text": "Neither reading tells you anything useful about the "
                  "junction whatsoever", "correct": False,
          "why": "A branch's own reading is genuinely useful — it tells "
                 "you that branch's exact current, which the main wire's "
                 "reading alone cannot."},
         {"text": "The main wire's reading, since it only gives the "
                  "total and says nothing about how it is divided",
          "correct": True},
         {"text": "One branch's reading, since a single branch says "
                  "nothing whatsoever about the junction",
          "correct": False,
          "why": "One branch reading at least tells you that branch's "
                 "own share exactly; the main wire's reading alone tells "
                 "you nothing about how the total is split."},
     ], "figure": None},
    {"id": "p8-03-s20", "band": "standard",
     "text": "A junction has two branches. One is rewired to have much "
             "less resistance than before; the other branch is left "
             "completely unchanged. What happens to the UNCHANGED "
             "branch's own current?",
     "options": [
         {"text": "It falls, since the other branch now takes a bigger "
                  "share of the total", "correct": False,
          "why": "Branches do not take a share from each other; the "
                 "unchanged branch keeps drawing exactly what its own "
                 "resistance and the battery's push give it."},
         {"text": "It rises, since a lower-resistance neighbour somehow "
                  "helps push more current through both branches",
          "correct": False,
          "why": "One branch's resistance has no direct effect on a "
                 "separate branch's own current; only its own "
                 "resistance and the shared push decide that."},
         {"text": "It becomes impossible to predict without recalculating "
                  "the whole junction from scratch", "correct": False,
          "why": "The unchanged branch's current follows directly from "
                 "its own unchanged resistance and the battery's "
                 "unchanged push — nothing needs recalculating for it."},
         {"text": "It stays exactly the same — its own resistance and "
                  "the battery's push have not changed", "correct": True},
     ], "figure": None},
    {"id": "p8-03-s21", "band": "standard",
     "text": "A junction's main wire reads 0.72 A, split between three "
             "branches reading 0.30 A, 0.22 A and an unmeasured third. "
             "What does the third branch carry?",
     "options": [
         {"text": "0.20 A", "correct": True},
         {"text": "1.24 A, adding all the given numbers together",
          "correct": False,
          "why": "That treats the main wire's own reading as another "
                 "branch to be added, rather than the total the "
                 "branches must add up to."},
         {"text": "0.52 A, adding the two known branches", "correct": False,
          "why": "That gives the combined size of the two KNOWN "
                 "branches, not what is left over for the unmeasured "
                 "one."},
         {"text": "0.24 A, sharing the main wire equally among three "
                  "branches", "correct": False,
          "why": "Equal sharing does not apply once two branches are "
                 "already measured unequally; the third is simply "
                 "whatever remains of the total."},
     ], "figure": None},
    {"id": "p8-03-s22", "band": "standard",
     "text": "A technician suspects the ammeter in one branch of a "
             "two-branch junction is reading too high. What extra "
             "measurement would let them test that suspicion?",
     "options": [
         {"text": "Read the same branch a second time with the same "
                  "meter, and compare the two readings", "correct": False,
          "why": "A meter that reads high reads high every time, so "
                 "repeating it with the same meter simply repeats the "
                 "same error."},
         {"text": "Read the main wire and the other branch, and check "
                  "that the two branches add up", "correct": True},
         {"text": "Read the p.d. across the suspect branch with a "
                  "voltmeter, which is the more sensitive of the two "
                  "instruments", "correct": False,
          "why": "A voltmeter measures a different quantity altogether, "
                 "and sensitivity is not the issue: no p.d. reading can "
                 "say whether a current reading is too high."},
         {"text": "Compare the reading with the same branch measured in "
                  "a completely different circuit of the same shape",
          "correct": False,
          "why": "A different circuit has its own resistances and its "
                 "own supply, so there is no reason its branch should "
                 "carry the same current as this one, whatever shape it "
                 "is drawn in."},
     ], "figure": None},
    {"id": "p8-03-s23", "band": "standard",
     "text": "A junction feeds a buzzer branch and a resistor branch. The "
             "resistor is then swapped for one with much MORE resistance. "
             "What happens to the buzzer's own branch current, and to "
             "the main wire's reading?",
     "options": [
         {"text": "The buzzer's current rises, taking over the resistor "
                  "branch's lost share", "correct": False,
          "why": "There is no share to take over; the buzzer's branch "
                 "simply keeps drawing exactly what it always drew."},
         {"text": "Neither changes, since just one of the two branches "
                  "was altered", "correct": False,
          "why": "The main wire carries the SUM of both branches, so a "
                 "fall in one branch's current does change the main "
                 "wire's total reading."},
         {"text": "The buzzer is unaffected; the main wire's reading "
                  "falls", "correct": True},
         {"text": "Both the buzzer's current and the main wire's reading "
                  "fall together", "correct": False,
          "why": "The buzzer's own branch depends only on its own "
                 "resistance and the shared push, neither of which has "
                 "changed."},
     ], "figure": None},
    {"id": "p8-03-s24", "band": "standard",
     "text": "A junction's main wire reads 1.20 A. Two branches read "
             "700 mA and 500 mA. Do these three readings agree with the "
             "junction rule?",
     "options": [
         {"text": "No — 700 mA and 500 mA add to just 1.20, so the "
                  "units must be wrong somewhere", "correct": False,
          "why": "Converting 700 mA and 500 mA to amps first gives 0.70 "
                 "A and 0.50 A, which do add to 1.20 A exactly — nothing "
                 "here disagrees."},
         {"text": "No — the two branches must be doubled before "
                  "comparing them with the main wire", "correct": False,
          "why": "No doubling step exists in the junction rule; "
                 "converting the units and adding directly is all that "
                 "is needed."},
         {"text": "It cannot be judged without knowing which branch "
                  "carries which component", "correct": False,
          "why": "Which component sits in which branch makes no "
                 "difference to whether the numbers themselves add up "
                 "correctly."},
         {"text": "Yes — 700 mA and 500 mA convert to 0.70 A and 0.50 A, "
                  "which add to exactly 1.20 A", "correct": True},
     ], "figure": None},

    {"id": "p8-03-s25", "band": "standard",
     "text": "A main wire carries 1.10 A into a junction with three "
             "branches. Two read 450 mA and 0.35 A. What does the third "
             "branch carry, in amps?",
     "options": [
         {"text": "0.80 A, the two known branches added without "
                  "converting 450 mA first", "correct": False,
          "why": "450 mA is 0.45 A, not 4.5 A or 0.045 A — converting it "
                 "correctly first is needed before adding."},
         {"text": "0.367 A, sharing the main wire equally between three "
                  "branches", "correct": False,
          "why": "Equal sharing does not apply once two branches are "
                 "already measured unequally; the third is simply what "
                 "remains of the total."},
         {"text": "0.30 A", "correct": True},
         {"text": "1.90 A, adding all three given numbers together",
          "correct": False,
          "why": "The main wire's own 1.10 A is the total to reach, not "
                 "another value to add on top of the branches."},
     ], "figure": None},
    {"id": "p8-03-s26", "band": "standard",
     "text": "A resistor is added into the MAIN wire of a parallel "
             "section, before the branches split — not into either "
             "branch. Does this change how the total current splits "
             "between the two branches?",
     "options": [
         {"text": "Yes — a resistor anywhere in the circuit changes the "
                  "split between the branches every time",
          "correct": False,
          "why": "The split depends only on the branches' OWN "
                 "resistances compared with each other, not on anything "
                 "added to the shared main wire before they divide."},
         {"text": "Yes, but just if the resistor is placed closer to "
                  "one branch than the other", "correct": False,
          "why": "Position along the shared main wire, before either "
                 "branch splits off, makes no difference to how the "
                 "current later divides between them."},
         {"text": "It cannot be judged without knowing the exact value "
                  "of the new resistor", "correct": False,
          "why": "Whatever value the new resistor has, it sits before "
                 "the split and so affects only the TOTAL current, not "
                 "how that total divides between the branches."},
         {"text": "No — the split is decided by the branches' own "
                  "resistances relative to each other", "correct": True},
     ], "figure": None},
    {"id": "p8-03-s27", "band": "standard",
     "text": "One branch of a junction is described as \"switched off\"; "
             "another, in a separate circuit, is described as "
             "\"physically disconnected\". Electrically, is there any "
             "difference in what the main wire reads in each case?",
     "options": [
         {"text": "No — both leave that branch carrying zero current, "
                  "so the main wire reads the same either way",
          "correct": True},
         {"text": "Yes — a disconnected branch still carries a tiny "
                  "current, unlike a switched-off one", "correct": False,
          "why": "Neither a switched-off branch nor a disconnected one "
                 "carries any current at all; both leave a complete gap "
                 "in that branch."},
         {"text": "Yes — switching off is temporary and disconnecting is "
                  "permanent, so the main wire reads differently",
          "correct": False,
          "why": "How long the gap lasts does not change what the "
                 "ammeter reads at any given instant; both give zero in "
                 "that branch either way."},
         {"text": "It depends on which component was in that branch",
          "correct": False,
          "why": "Whatever component was in the branch, both a switch "
                 "left open and a full disconnection leave it carrying "
                 "nothing."},
     ], "figure": None},
    {"id": "p8-03-s28", "band": "standard",
     "text": "Junction P has two equal branches, both reading 0.20 A. "
             "Junction Q, a separate circuit, has two unequal branches "
             "reading 0.10 A and 0.30 A. Compare the two main-wire "
             "readings.",
     "options": [
         {"text": "They cannot be compared without knowing each "
                  "junction's own resistance", "correct": False,
          "why": "No resistance values are needed to add up given "
                 "branch currents; both totals can be found directly "
                 "from the numbers given."},
         {"text": "They are the same, both 0.40 A, even though the "
                  "branches split very differently", "correct": True},
         {"text": "Junction P reads higher, since equal branches add to "
                  "more than unequal ones do", "correct": False,
          "why": "How the current happens to split between the "
                 "branches does not change the total; both pairs here "
                 "add to exactly 0.40 A."},
         {"text": "Junction Q reads higher, since one of its branches "
                  "alone already reaches 0.30 A", "correct": False,
          "why": "The main wire is the SUM of both branches, not "
                 "whichever single branch is largest; both totals come "
                 "to 0.40 A."},
     ], "figure": None},
    {"id": "p8-03-s29", "band": "standard",
     "text": "One branch of a junction contains TWO components wired one "
             "after another, rather than just one. Does this branch "
             "still count as a single branch for the addition rule?",
     "options": [
         {"text": "No — a branch may contain exactly one component and "
                  "no more", "correct": False,
          "why": "A branch can contain any number of components in "
                 "series within it; what makes it one branch is having "
                 "just one path, not having just one component."},
         {"text": "It depends on whether the two components are "
                  "identical to each other", "correct": False,
          "why": "Whether the two components match or not makes no "
                 "difference — the branch is still one single path "
                 "either way."},
         {"text": "Yes — it is still one path carrying one current, "
                  "however many components sit along it", "correct": True},
         {"text": "No — each component inside the branch must be "
                  "counted as its own separate branch", "correct": False,
          "why": "Components wired one after another share the same "
                 "single path and the same single current; they do not "
                 "create extra branches of their own."},
     ], "figure": None},
    {"id": "p8-03-s30", "band": "standard",
     "text": "A kitchen ring main has several sockets branching off it. A "
             "toaster, a kettle and a microwave are all switched on at "
             "once. What determines the current the main fuse box has to "
             "cope with?",
     "options": [
         {"text": "Just the single largest appliance's current, since "
                  "the others are considered negligible", "correct": False,
          "why": "The fuse box is fed by the shared main wire, which "
                 "carries the total of every branch, not just the "
                 "biggest one."},
         {"text": "The average of the three appliances' currents",
          "correct": False,
          "why": "An average is never the rule at a junction; the "
                 "branch currents add together to give the total."},
         {"text": "Whichever appliance was switched on most recently",
          "correct": False,
          "why": "Order of switching on makes no difference to the "
                 "total the main wire has to carry; all three currents "
                 "add together regardless of timing."},
         {"text": "The sum of all three appliances' currents added "
                  "together", "correct": True},
     ], "figure": None},
    # ── MRB-338 night 3 top-up · harder ───────────────────────────────

    {"id": "p8-03-h09", "band": "harder",
     "text": "A junction has two branches, X and Y. Branch X's resistance "
             "is doubled; branch Y is left completely unchanged. Explain "
             "what happens to branch Y's own current, the main wire's "
             "reading, and branch X's current, in that order.",
     "options": [
         {"text": "Y's current is unaffected; the main wire's reading "
                  "falls; X's own current falls, since it now resists "
                  "the flow more", "correct": True},
         {"text": "All three fall together, since doubling any "
                  "resistance in the junction always lowers everything "
                  "connected to it", "correct": False,
          "why": "Branch Y's own current is set only by its own "
                 "resistance and the shared push, neither of which has "
                 "changed here."},
         {"text": "Y's current rises to make up for X's fall, keeping "
                  "the main wire's reading exactly the same",
          "correct": False,
          "why": "Branches do not compensate for one another; Y simply "
                 "keeps drawing what it always drew, so the main "
                 "reading genuinely falls."},
         {"text": "X's current is unaffected, because doubling a "
                  "branch's resistance only changes what happens "
                  "beyond the junction, not within the branch itself",
          "correct": False,
          "why": "A branch's own resistance directly sets its own "
                 "current; doubling it necessarily lowers the current "
                 "through that very branch."},
     ], "figure": None},
    {"id": "p8-03-h10", "band": "harder",
     "text": "A junction feeds three branches: 0.20 A, 0.30 A and a "
             "third that is unknown. The main wire is rated to carry at "
             "most 0.80 A safely. What is the LARGEST the third branch "
             "could carry before the rating is exceeded?",
     "options": [
         {"text": "It cannot be worked out without knowing each "
                  "branch's exact resistance", "correct": False,
          "why": "No resistance values are needed — subtracting the two "
                 "known currents from the rating gives the answer "
                 "directly."},
         {"text": "0.30 A", "correct": True},
         {"text": "0.80 A, since that is the rating itself",
          "correct": False,
          "why": "The two known branches already use up 0.50 A of the "
                 "rating, so the third cannot reach the full 0.80 A on "
                 "its own without going over."},
         {"text": "0.50 A, the two known branches added together",
          "correct": False,
          "why": "That is how much of the rating is already used by "
                 "the first two branches, not how much is left for the "
                 "third."},
     ], "figure": None},
    {"id": "p8-03-h11", "band": "harder",
     "text": "A student measures a junction's three readings across a "
             "whole afternoon and finds the main wire's reading changes "
             "several times, while the two branches' SHARE of that total "
             "stays in the same fixed ratio throughout. What does this "
             "suggest about the two branches?",
     "options": [
         {"text": "One of the branches must be broken, since real "
                  "branches never keep a fixed ratio", "correct": False,
          "why": "A fixed ratio is exactly what you would expect from "
                 "two ordinary, unchanging branches — it is not a sign "
                 "of a fault."},
         {"text": "The two branches must be identical components",
          "correct": False,
          "why": "A fixed ratio only requires that neither branch's "
                 "resistance changes relative to the other; the two "
                 "branches do not need to be identical to each other at "
                 "all."},
         {"text": "Their resistances have stayed fixed relative to each "
                  "other", "correct": True},
         {"text": "The junction itself must be actively keeping the "
                  "ratio fixed on purpose", "correct": False,
          "why": "A junction has no mechanism for keeping anything "
                 "fixed; a steady ratio simply reflects two branches "
                 "whose own resistances have not changed relative to "
                 "each other."},
     ], "figure": None},
    {"id": "p8-03-h12", "band": "harder",
     "text": "A junction's main wire is rated at 5 A. It already feeds "
             "two branches at 1.8 A and 2.1 A. A third appliance drawing "
             "1.4 A is added. Explain the risk, and state by how much "
             "the rating is exceeded.",
     "options": [
         {"text": "There is no risk, since no single branch on its own "
                  "exceeds the 5 A rating", "correct": False,
          "why": "The rating applies to the MAIN wire, which has to "
                 "carry all three branches added together, not to any "
                 "one branch in isolation."},
         {"text": "The three branches add to 4.7 A, comfortably under "
                  "the rating", "correct": False,
          "why": "1.8 plus 2.1 plus 1.4 comes to 5.3 A, not 4.7 A — the "
                 "rating genuinely is exceeded."},
         {"text": "The risk cannot be assessed without knowing the "
                  "resistance of the main wire itself", "correct": False,
          "why": "Comparing the summed branch currents with the stated "
                 "rating is enough on its own; the wire's own resistance "
                 "is not needed for this comparison."},
         {"text": "The three branches add to 5.3 A, which is 0.3 A over "
                  "the main wire's 5 A rating", "correct": True},
     ], "figure": None},
    {"id": "p8-03-h13", "band": "harder",
     "text": "A junction's three ammeters — the main wire and its two "
             "branches — are read at the same instant, and all three "
             "readings are exactly equal. What does this tell you about "
             "one of the branches?",
     "options": [
         {"text": "One branch must be carrying no current at all, since "
                  "the other one alone equals the main wire's total",
          "correct": True},
         {"text": "Both branches must be carrying exactly half the main "
                  "wire's reading each, which is what makes all three "
                  "meters agree with one another", "correct": False,
          "why": "If both branches equalled half the main reading, "
                 "neither branch reading would match the main wire's "
                 "reading — but here every reading is exactly equal."},
         {"text": "The junction must be faulty, since three meters on one "
                  "junction cannot all show the same value", "correct": False,
          "why": "Equal readings across all three ammeters are a "
                 "perfectly ordinary sign of one branch carrying nothing "
                 "at all, not a fault."},
         {"text": "The two branches must be identical components to "
                  "each other", "correct": False,
          "why": "Identical components would usually split the current "
                 "evenly rather than give three IDENTICAL readings "
                 "including the main wire's own."},
     ], "figure": None},
    {"id": "p8-03-h14", "band": "harder",
     "text": "Explain why it is meaningless to ask \"what current does "
             "the junction itself use\", in the same way you might ask "
             "what current a lamp uses.",
     "options": [
         {"text": "The question only becomes meaningless once there are "
                  "three or more branches", "correct": False,
          "why": "The question is equally meaningless with any number "
                 "of branches — a junction is never a component that "
                 "takes energy from the charge."},
         {"text": "A junction is just a point where wires meet, with no "
                  "resistance of its own", "correct": True},
         {"text": "A junction does use current, but far too little to "
                  "measure with an ordinary ammeter", "correct": False,
          "why": "A junction is not a component with any resistance of "
                 "its own at all; it uses no current, however sensitive "
                 "the ammeter."},
         {"text": "A junction uses whatever is left over once the "
                  "branches have taken their shares", "correct": False,
          "why": "There is no current left over at a junction; every "
                 "bit of the current arriving is accounted for by the "
                 "branches leaving it."},
     ], "figure": None},
    {"id": "p8-03-h15", "band": "harder",
     "text": "Two junctions sit on either end of a parallel section: one "
             "where the branches divide, and one further along where "
             "they rejoin. A component is added into ONE of the branches "
             "between the two junctions. Compare the total current "
             "passing the first junction with the total passing the "
             "second.",
     "options": [
         {"text": "They are always equal, whatever is added into a "
                  "branch between them, since charge is conserved all "
                  "the way through", "correct": True},
         {"text": "The second junction now reads less, since the added "
                  "component uses up some of the charge on the way",
          "correct": False,
          "why": "Nothing uses up charge in a branch; whatever total "
                 "arrives at the dividing junction is exactly what "
                 "arrives back at the rejoining one."},
         {"text": "The second junction now reads more, since the added "
                  "component contributes extra current of its own",
          "correct": False,
          "why": "A component in a branch only resists the flow — it "
                 "never adds current of its own to the total."},
         {"text": "It depends on whether the added component increases "
                  "or decreases that branch's own resistance",
          "correct": False,
          "why": "Changing a branch's resistance can change how the "
                 "total SPLITS between the branches, but the total "
                 "passing each of the two junctions stays equal either "
                 "way."},
     ], "figure": None},
    {"id": "p8-03-h16", "band": "harder",
     "text": "A junction feeds four identical lamp branches, each drawing "
             "0.25 A. One by one, lamps are unscrewed until only one is "
             "left. Track the main wire's reading after each removal, "
             "and state what stays constant throughout for the "
             "surviving lamps.",
     "options": [
         {"text": "The main wire falls to zero the moment the first "
                  "lamp is removed, since the junction can no longer "
                  "balance", "correct": False,
          "why": "Removing one of several parallel branches leaves the "
                 "others working normally; the main wire simply drops by "
                 "that one branch's share, not to zero."},
         {"text": "The main wire falls 1.00, 0.75, 0.50, 0.25 A; each "
                  "surviving lamp stays at 0.25 A throughout",
          "correct": True},
         {"text": "The main wire stays at 1.00 A throughout, since the "
                  "surviving lamps take over the removed ones' share",
          "correct": False,
          "why": "Nothing is taken over — each removal genuinely lowers "
                 "the main wire's reading by that lamp's own 0.25 A."},
         {"text": "The main wire falls in the same steps, but each "
                  "surviving lamp's own current rises a little after "
                  "every removal", "correct": False,
          "why": "A surviving lamp's own branch is untouched by removing "
                 "a neighbour; it keeps drawing exactly 0.25 A "
                 "throughout, never more."},
     ], "figure": None},
    {"id": "p8-03-h17", "band": "harder",
     "text": "A junction's main wire is measured at 0.90 A using an "
             "ammeter with a small, known fault that always reads "
             "0.05 A too high. The two branches, measured with correctly "
             "working meters, read 0.40 A and 0.45 A. Explain the "
             "discrepancy, and state the junction's TRUE main-wire "
             "current.",
     "options": [
         {"text": "A hidden third branch must be carrying the missing "
                  "0.05 A", "correct": False,
          "why": "No third branch is needed once the known meter fault "
                 "is accounted for; the two given branches already "
                 "explain the true total."},
         {"text": "The true main-wire current is 0.90 A, and the two "
                  "branch meters must instead be the faulty ones",
          "correct": False,
          "why": "The question states the main-wire meter is the "
                 "faulty one; trusting the two correctly working branch "
                 "meters gives the true total instead."},
         {"text": "The branches genuinely add to 0.85 A; the faulty "
                  "meter's own 0.05 A error accounts for the "
                  "difference from its 0.90 A reading", "correct": True},
         {"text": "The junction rule has been broken here, since a real "
                  "junction can tolerate this size of mismatch",
          "correct": False,
          "why": "The junction rule is not broken — a faulty meter fully "
                 "explains the gap, and an ideal junction still requires "
                 "the true readings to add up exactly."},
     ], "figure": None},
    {"id": "p8-03-h18", "band": "harder",
     "text": "A designer wants a junction where removing any ONE of "
             "three branches leaves the other two completely unaffected, "
             "while the main wire's reading still visibly drops each "
             "time. Is a plain parallel junction of three branches enough "
             "to achieve this, or is something extra needed?",
     "options": [
         {"text": "An extra fuse is needed in each branch before the "
                  "requirement can possibly be met", "correct": False,
          "why": "A fuse would only add protection against overload; "
                 "the independence of the branches and the visible drop "
                 "in total current both already follow from plain "
                 "parallel wiring."},
         {"text": "This cannot be achieved at all, since removing a "
                  "branch always disturbs the others to some degree",
          "correct": False,
          "why": "Parallel branches genuinely do not disturb one "
                 "another; each keeps drawing exactly what its own "
                 "resistance and the shared push give it."},
         {"text": "It requires the three branches to be identical "
                  "components", "correct": False,
          "why": "The branches do not need to be identical for this "
                 "requirement — independence and a visible drop in the "
                 "total both hold whether or not the branches match."},
         {"text": "A plain parallel junction already does this on its "
                  "own — no extra component is needed", "correct": True},
     ], "figure": None},
    {"id": "p8-03-h19", "band": "harder",
     "text": "A junction's main wire reading is plotted over time as a "
             "component in one branch heats up and its resistance rises "
             "steadily. The OTHER branch is untouched throughout. "
             "Describe the shape of the main-wire graph, and the "
             "unchanged branch's own graph.",
     "options": [
         {"text": "The main wire falls steadily as that branch's "
                  "resistance rises; the unchanged branch stays flat",
          "correct": True},
         {"text": "Both graphs fall steadily together, since the "
                  "heating branch's rising resistance affects the whole "
                  "junction equally", "correct": False,
          "why": "The unchanged branch's own resistance and the shared "
                 "push have not altered, so its own current stays flat "
                 "however the other branch's resistance rises."},
         {"text": "The main wire's reading rises steadily, since higher "
                  "resistance branches somehow draw more current",
          "correct": False,
          "why": "Higher resistance in a branch lowers that branch's own "
                 "current, which lowers the main wire's total, not "
                 "raises it."},
         {"text": "The unchanged branch's reading rises to compensate "
                  "for the heating branch's fall", "correct": False,
          "why": "A branch does not compensate for a neighbour; the "
                 "unchanged branch simply keeps drawing what it always "
                 "drew, flat over time."},
     ], "figure": None},
    {"id": "p8-03-h20", "band": "harder",
     "text": "A junction has two branches. Branch A is fixed at 0.30 A. "
             "Branch B can be varied. State the RANGE of possible "
             "main-wire readings as branch B is varied from 0 A up to "
             "0.50 A, and explain why the main wire can never read less "
             "than 0.30 A.",
     "options": [
         {"text": "From 0.30 A up to 0.50 A, since the main wire can "
                  "never exceed the larger of the two branches",
          "correct": False,
          "why": "The main wire carries the SUM of the two branches, "
                 "which can exceed either one on its own — up to 0.80 A "
                 "here, not capped at 0.50 A."},
         {"text": "From 0.30 A up to 0.80 A; it can never read below "
                  "0.30 A because branch A alone already guarantees at "
                  "least that much", "correct": True},
         {"text": "From 0 A up to 0.80 A, since branch B could in "
                  "principle cancel branch A out entirely",
          "correct": False,
          "why": "Two ordinary branches in the same direction do not "
                 "cancel each other; the main wire is their sum, which "
                 "can never fall below branch A's own 0.30 A here."},
         {"text": "Always exactly 0.30 A, since branch A alone decides "
                  "the main-wire reading", "correct": False,
          "why": "Branch B's current adds to branch A's, so the main "
                 "wire's reading genuinely rises above 0.30 A as branch "
                 "B increases from zero."},
     ], "figure": None},
    {"id": "p8-03-h21", "band": "harder",
     "text": "A student claims: \"If I know the main wire's reading and "
             "the number of branches, I can always work out each "
             "branch's current by dividing.\" Under what specific "
             "condition, if any, would dividing actually give the right "
             "answer?",
     "options": [
         {"text": "Only when there are exactly two branches, never with "
                  "three or more", "correct": False,
          "why": "The number of branches is not what matters — dividing "
                 "works only when the branches happen to be equal, "
                 "whether there are two of them or many."},
         {"text": "Never — dividing can never give a genuinely correct "
                  "branch current under any circumstances",
          "correct": False,
          "why": "Dividing does give the right answer in the special "
                 "case where the branches are all equal; it is unreliable "
                 "only in general, not impossible in every case."},
         {"text": "Only when every branch happens to have exactly the "
                  "same resistance as the others", "correct": True},
         {"text": "Always, regardless of the branches, since dividing "
                  "is simply the reverse of adding", "correct": False,
          "why": "Dividing only reverses adding when the parts being "
                 "added were equal in the first place; unequal branches "
                 "need their own separate measurements."},
     ], "figure": None},
    {"id": "p8-03-h22", "band": "harder",
     "text": "A four-branch junction feeds branches reading 0.10 A, "
             "0.20 A, 0.30 A and 0.40 A. A single fault causes the SECOND "
             "branch (0.20 A) to carry no current at all, while the "
             "other three are entirely unaffected. State the main wire's "
             "reading before and after the fault.",
     "options": [
         {"text": "Before: 1.00 A. After: 1.00 A, since the other three "
                  "branches make up the difference", "correct": False,
          "why": "The other three branches are stated to be "
                 "unaffected, so they do not make up anything — the "
                 "total genuinely falls by the faulted branch's own "
                 "0.20 A."},
         {"text": "Before: 0.25 A, the average of the four branches. "
                  "After: 0.20 A", "correct": False,
          "why": "The main wire is the SUM of the branches, not their "
                 "average, so the before-reading is 1.00 A, not 0.25 A."},
         {"text": "Before: 1.00 A. After: 0.90 A, since the fault only "
                  "halves that branch's current rather than removing it",
          "correct": False,
          "why": "The fault is described as the branch carrying NO "
                 "current at all, not half of it, so the whole 0.20 A "
                 "is lost from the total."},
         {"text": "Before: 1.00 A. After: 0.80 A", "correct": True},
     ], "figure": None},
    {"id": "p8-03-h23", "band": "harder",
     "text": "Explain why the rule \"currents add at a junction\" is "
             "really just a restatement of \"charge cannot be created or "
             "destroyed\", rather than a separate, extra fact about "
             "electricity.",
     "options": [
         {"text": "If charge could vanish or appear at a point, the "
                  "branches would not need to add to the arriving "
                  "current at all", "correct": True},
         {"text": "The two ideas are unrelated; the addition rule "
                  "happens to be true for junctions specifically, for "
                  "different reasons", "correct": False,
          "why": "The addition rule is not a separate coincidence — it "
                 "is precisely what conservation of charge requires at "
                 "any single point."},
         {"text": "Charge conservation only applies to whole circuits, "
                  "while the addition rule applies only to single "
                  "points, so the two cannot be linked", "correct": False,
          "why": "Conservation of charge applies everywhere, including "
                 "at a single point, which is exactly why the addition "
                 "rule holds there."},
         {"text": "The addition rule is a rounding convention adopted "
                  "for convenience, not a consequence of any deeper "
                  "physical law", "correct": False,
          "why": "It is not a convenience or convention — it follows "
                 "directly and necessarily from the deeper law that "
                 "charge is conserved."},
     ], "figure": None},
    {"id": "p8-03-h24", "band": "harder",
     "text": "A junction feeds two branches. Branch A's component is "
             "swapped for one letting through TWICE as much current as "
             "before, while branch B is left alone. The main wire's "
             "reading rises from 0.50 A to 0.70 A. What was branch A's "
             "ORIGINAL current, before the swap?",
     "options": [
         {"text": "0.10 A, a tenth of the new main-wire reading",
          "correct": False,
          "why": "There is no reason to take a tenth here; working "
                 "from the RISE in the total (0.20 A) and doubling being "
                 "the branch's own change gives 0.20 A directly as its "
                 "original value."},
         {"text": "0.20 A", "correct": True},
         {"text": "0.35 A, half of the new main-wire reading",
          "correct": False,
          "why": "Halving the new total assumes the two branches are "
                 "equal, which is not given here and does not match the "
                 "rise described."},
         {"text": "0.40 A, doubling the 0.20 A rise in the total",
          "correct": False,
          "why": "The 0.20 A rise already IS branch A's original current, "
                 "because doubling a branch adds its original amount once "
                 "more; doubling that rise counts the change twice."},
     ], "figure": None},

    {"id": "p8-03-h25", "band": "harder",
     "text": "A junction's main wire is rated 2.0 A. Two branches read "
             "0.6 A and 0.5 A. A third branch, currently at 0.4 A, has "
             "its resistance halved, which doubles its own current. Is "
             "the junction still within its rating afterward, and by how "
             "much?",
     "options": [
         {"text": "Yes — the new total is 1.9 A, which is 0.1 A under "
                  "the 2.0 A rating", "correct": True},
         {"text": "No — the new total is 2.3 A, which is 0.3 A over the "
                  "rating", "correct": False,
          "why": "That treats the third branch's NEW current as 1.2 A "
                 "rather than 0.8 A; halving its resistance doubles "
                 "0.4 A to 0.8 A, not to 1.2 A."},
         {"text": "Yes — the new total is exactly 2.0 A, right at the "
                  "rating with no margin at all", "correct": False,
          "why": "0.6 A plus 0.5 A plus the doubled 0.8 A comes to "
                 "1.9 A, not exactly 2.0 A."},
         {"text": "It cannot be judged without knowing the exact "
                  "resistance values involved", "correct": False,
          "why": "The doubled current is already given directly (0.4 A "
                 "doubling to 0.8 A), so no resistance values are needed "
                 "to complete the comparison with the rating."},
     ], "figure": None},
    {"id": "p8-03-h26", "band": "harder",
     "text": "A student wants a junction where disconnecting any ONE "
             "branch causes the OTHER branches' own readings to change "
             "measurably. Is this possible with an ideal battery and "
             "ideal wires, or does it need something extra?",
     "options": [
         {"text": "Yes, but only once there are four or more branches "
                  "meeting at the same junction", "correct": False,
          "why": "The number of branches is not what creates this "
                 "effect; it comes from the battery itself no longer "
                 "being treated as ideal."},
         {"text": "Not with an ideal battery — that needs a REAL one, "
                  "whose push sags under a heavier load", "correct": True},
         {"text": "Yes — any ordinary parallel junction already causes "
                  "this, whether the battery is treated as ideal or not",
          "correct": False,
          "why": "In the ideal picture used in this course, each "
                 "branch's current depends only on its own resistance "
                 "and a battery push that never sags — so the other "
                 "branches are genuinely unaffected."},
         {"text": "No — this is never possible with any battery, ideal "
                  "or real", "correct": False,
          "why": "A REAL battery's push does sag a little under a "
                 "bigger total load, which would very slightly change "
                 "every branch's current when one is removed."},
     ], "figure": None},
    {"id": "p8-03-h27", "band": "harder",
     "text": "Circuit 1 has one junction where three branches all split "
             "off together. Circuit 2 uses the SAME three branches, but "
             "wired as three separate two-way splits in a row along the "
             "main wire. Does the FINAL main-wire reading differ between "
             "the two arrangements?",
     "options": [
         {"text": "Yes — one big junction always carries more current "
                  "than several smaller ones combined", "correct": False,
          "why": "A junction does not add current of its own, whether "
                 "it is one big split or several small ones; the total "
                 "is set only by what the branches themselves carry."},
         {"text": "It depends on the order the three branches are "
                  "wired in along the main wire", "correct": False,
          "why": "The order the branches split off in makes no "
                 "difference — the branch currents still simply add "
                 "together to the same final total."},
         {"text": "No — the same three currents combine to the same "
                  "total, whichever way they are split", "correct": True},
         {"text": "Yes — splitting at several separate points along the "
                  "way loses some current at each one", "correct": False,
          "why": "Nothing is lost at any splitting point — charge is "
                 "conserved at each one, so the same three currents "
                 "still combine to the same total either way."},
     ], "figure": None},
    {"id": "p8-03-h28", "band": "harder",
     "text": "A four-branch junction reads 0.12 A, 0.18 A, 0.22 A and a "
             "fourth meter that reports MINUS 0.05 A. In this ordinary "
             "dividing junction, no branch genuinely reverses direction. "
             "What does the negative reading most likely indicate?",
     "options": [
         {"text": "That branch genuinely carries current the opposite "
                  "way to the other three, which is entirely normal at "
                  "any junction", "correct": False,
          "why": "In an ordinary dividing junction fed from one supply, "
                 "there is no mechanism for one branch to carry current "
                 "backwards relative to the others."},
         {"text": "The main wire's total must itself be negative as "
                  "well, once this branch is included", "correct": False,
          "why": "A meter connected the wrong way round explains the "
                 "sign of just that one reading; it says nothing about "
                 "the main wire needing to be negative too."},
         {"text": "The junction rule breaks down once one branch reads "
                  "less than the others", "correct": False,
          "why": "A small reading is not the issue here — it is "
                 "specifically the NEGATIVE sign that points to a meter "
                 "connected backwards, not a broken rule."},
         {"text": "The fourth meter's leads are probably connected the "
                  "wrong way round", "correct": True},
     ], "figure": None},
    {"id": "p8-03-h29", "band": "harder",
     "text": "A junction's two branch currents are in the ratio 2:3. The "
             "main wire reads 1.00 A. What does each branch carry?",
     "options": [
         {"text": "0.40 A and 0.60 A", "correct": True},
         {"text": "0.20 A and 0.30 A, treating the ratio numbers "
                  "directly as amps", "correct": False,
          "why": "The ratio numbers are not amps themselves — they show "
                 "how the actual 1.00 A total is split, five parts in "
                 "total, two parts and three parts."},
         {"text": "0.50 A and 0.50 A, since a ratio of 2:3 is close "
                  "enough to equal", "correct": False,
          "why": "A 2:3 ratio is a genuinely unequal split, not "
                 "approximately equal; treating it as 50:50 ignores the "
                 "ratio given."},
         {"text": "0.67 A and 0.33 A", "correct": False,
          "why": "That splits the total in the ratio 2:1 rather than "
                 "2:3. A 2:3 split means five equal parts — two of them "
                 "and three of them — giving 0.40 A and 0.60 A."},
     ], "figure": None},
    {"id": "p8-03-h30", "band": "harder",
     "text": "Explain what a main fuse for a whole house, an ammeter "
             "beside a single cell, and the total current a "
             "many-branched torch's battery supplies all have in common, "
             "in terms of ONE general rule.",
     "options": [
         {"text": "The rule only applies to junctions with exactly two "
                  "branches, so it cannot cover all three examples",
          "correct": False,
          "why": "The addition rule applies to any number of branches "
                 "feeding a shared point, which is exactly what "
                 "connects all three examples here."},
         {"text": "In every case, the reading needed is the sum of "
                  "everything drawn from the branches sharing that "
                  "point", "correct": True},
         {"text": "They are unrelated examples that only happen to "
                  "involve the word \"current\"", "correct": False,
          "why": "All three are genuinely the same calculation at "
                 "different scales — adding up whatever is drawn from a "
                 "shared supply point."},
         {"text": "Each one measures a different, unrelated physical "
                  "quantity, despite the shared unit of amps",
          "correct": False,
          "why": "All three measure the very same quantity — current — "
                 "and all three are found the very same way, by summing "
                 "what every branch draws."},
     ], "figure": None},
]
