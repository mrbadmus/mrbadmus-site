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
            {"text": "All three read 0.00 A", "correct": True},
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
            {"text": "Exactly the same", "correct": True},
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
]
