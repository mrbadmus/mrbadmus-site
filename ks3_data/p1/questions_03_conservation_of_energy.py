"""P1 lesson 03 — Conservation of energy: twelve questions.

⊕ RUN 1's TWELVE WERE USED AS RAW MATERIAL, NOT ADOPTED (MRB-223).

Two separate problems with the inherited set, and the second is the one that
mattered:

**1 · Three of them quote figures that never existed.** Run 1's own
provenance audit flags `e04`, `s01` and `h02` as built on a five-machine
bench it invented — the LED 4000→1200→2800 split, the filament's 5-in-100,
and the kettle at 90%. Design's `p1-03` has no such bench: her instruments
are a pendulum running total and a balance beam, and neither produces a
joule figure for any appliance. Those three are dropped rather than repaired.

**2 · Most of the rest are aimed at `p1-02`.** Efficiency, wasted energy and
useful output are the before-and-after lesson's material and are already
covered by `questions_02`. Her `p1-03` is about the TOTAL: that it does not
move, that "stopped" and "out of energy" are different statements, and that
a machine which appears to lose energy has dissipated it.

    CHANGED — four stems kept, every option set rewritten (4):
        e01  what conservation actually says
        s01  the bouncing ball, re-pointed at the total
        h01  why you cannot run the room backwards
        h02  "lost" is the word to avoid

    NEW — her content had no question covering it (8):
        e02  the pendulum that has stopped
        e03  friction has no mechanism for destroying anything
        e04  a closed system
        s02  the beam is a sum, not a product
        s03  naming the mechanism rather than saying "energy"
        s04  the brake discs are where to look
        h03  the perpetual-motion claim and what to measure
        h04  the neutrino — conservation strong enough to predict a particle

    DROPPED — invented data or `p1-02` material (8):
        run 1's e02 (efficiency arithmetic), e03, e04 (LED figures),
        s01 (filament figures), s02, s03, s04 (kettle mass), h02 (kettle 90%).

⚠️ The correct answer's position cycles 0, 1, 2, 3 through the twelve.
⚠️ Every distractor is written to the correct answer's own length (MRB-177).

The lesson carries no figures, so every question is figure=None.
"""

UNIT = "P1"
LESSON = "conservation-of-energy"
LESSON_NUMBER = 3

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "p1-03-e01",
        "band": "easier",
        "text": "What does the law of conservation of energy say?",
        "options": [
            {"text": "Energy cannot be created or destroyed, only "
                     "transferred between stores",
             "correct": True},
            {"text": "Energy should not be wasted, so machines must be made "
                     "as efficient as possible",
             "correct": False,
             "why": "That is advice about using energy well. The law is a "
                    "statement about what happens, not about what we ought "
                    "to do."},
            {"text": "Energy is always eventually destroyed by friction and "
                     "turned into heat",
             "correct": False,
             "why": "Friction moves energy into thermal stores. It has no "
                    "mechanism for destroying any of it."},
            {"text": "Energy can be created by a machine but never "
                     "afterwards destroyed",
             "correct": False,
             "why": "Neither half is allowed. A machine only ever moves "
                    "energy between stores."},
        ],
        "figure": None,
    },
    {
        "id": "p1-03-e02",
        "band": "easier",
        "text": "A pendulum swings until it hangs completely still. What is "
                "true of the total energy compared with the start?",
        "options": [
            {"text": "It is smaller, because the swinging used some of it up",
             "correct": False,
             "why": "Nothing uses energy up. The air and the pivot are very "
                    "slightly warmer than they were."},
            {"text": "It is exactly the same, but now all of it is in "
                     "thermal stores",
             "correct": True},
            {"text": "It is zero, because the pendulum is not moving any "
                     "more at all",
             "correct": False,
             "why": "Nothing moving means the KINETIC store is empty. The "
                    "total is not the kinetic store."},
            {"text": "It is smaller by a tiny amount that cannot be measured "
                     "exactly",
             "correct": False,
             "why": "Not by any amount. The sum is exact rather than "
                    "approximately right."},
        ],
        "figure": None,
    },
    {
        "id": "p1-03-e03",
        "band": "easier",
        "text": "A cyclist brakes hard and stops. Where should you look to "
                "find the energy that was in the kinetic store?",
        "options": [
            {"text": "Nowhere — braking is the process that removes it from "
                     "the world",
             "correct": False,
             "why": "Braking moves energy; it does not remove it. Something "
                    "nearby is warmer."},
            {"text": "In the air only, because that is what the bicycle "
                     "pushed against",
             "correct": False,
             "why": "Some goes to the air, but the brakes are where most of "
                    "it went and they are measurably hot."},
            {"text": "In the brake blocks, the wheel rims, the tyres and the "
                     "air",
             "correct": True},
            {"text": "Back in the cyclist's chemical store, ready to be used "
                     "again",
             "correct": False,
             "why": "Nothing returns it to the rider. A body cannot recharge "
                    "from a thermal store."},
        ],
        "figure": None,
    },
    {
        "id": "p1-03-e04",
        "band": "easier",
        "text": "What is meant by a closed system?",
        "options": [
            {"text": "A system that has been sealed so that no air can get "
                     "into or out of it",
             "correct": False,
             "why": "Sealing helps in practice, but the idea is about energy "
                    "crossing the boundary, not air."},
            {"text": "A system in which every transfer of energy is "
                     "perfectly efficient",
             "correct": False,
             "why": "No such system exists, and the law does not need one. "
                    "Efficiency is a different idea."},
            {"text": "A system that has stopped changing because it has "
                     "reached its final state",
             "correct": False,
             "why": "A closed system can be changing very fast. What matters "
                    "is where its boundary is drawn."},
            {"text": "Everything involved in a change, drawn widely enough "
                     "that no energy crosses out",
             "correct": True},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "p1-03-s01",
        "band": "standard",
        "text": "A ball is dropped from 1 m and bounces back to only 0.6 m. "
                "What is the best account of the total energy?",
        "options": [
            {"text": "The total is unchanged; some now sits in thermal "
                     "stores in the ball, floor and air",
             "correct": True},
            {"text": "The total has fallen by the fraction of the height the "
                     "ball failed to reach",
             "correct": False,
             "why": "The height fell; the total did not. Height measures one "
                    "store, not the whole account."},
            {"text": "The total has fallen because the floor absorbed and "
                     "destroyed part of it",
             "correct": False,
             "why": "The floor received it and is very slightly warmer. "
                    "Absorbing is not destroying."},
            {"text": "The total is unchanged because the ball will "
                     "eventually bounce back to 1 m",
             "correct": False,
             "why": "It never will. The total is unchanged anyway — the "
                    "energy has simply moved somewhere it cannot come back "
                    "from."},
        ],
        "figure": None,
    },
    {
        "id": "p1-03-s02",
        "band": "standard",
        "text": "Why is conservation of energy drawn as a balance beam "
                "rather than as a formula triangle?",
        "options": [
            {"text": "Because a triangle is only used for equations that "
                     "students meet later on",
             "correct": False,
             "why": "It is not about when you meet it. It is about what "
                    "shape the relationship actually has."},
            {"text": "Because the relationship is a sum on each side, and a "
                     "triangle means multiply or divide",
             "correct": True},
            {"text": "Because a beam can show four stores at once and a "
                     "triangle can only show three",
             "correct": False,
             "why": "The count is not the reason. A triangle would be wrong "
                    "even with exactly three stores."},
            {"text": "Because energy is measured in joules and triangles "
                     "only work for other units",
             "correct": False,
             "why": "Units have nothing to do with it. E = F × d is a "
                    "triangle and its answer is in joules too."},
        ],
        "figure": None,
    },
    {
        "id": "p1-03-s03",
        "band": "standard",
        "text": "“Why did the kettle's water get hot?” Which "
                "answer actually explains it?",
        "options": [
            {"text": "Because energy was supplied to it continuously from "
                     "the mains while it was switched on",
             "correct": False,
             "why": "True but empty. Energy is never the reason anything "
                    "happens — it is conserved, so it cannot be consumed."},
            {"text": "Because the water already had a great deal of energy "
                     "stored inside it beforehand",
             "correct": False,
             "why": "Cold water holds energy too. That cannot be why this "
                    "water got hot and other water did not."},
            {"text": "Because a current in the element makes its particles "
                     "vibrate, and they collide with the water",
             "correct": True},
            {"text": "Because electrical energy was converted into heat "
                     "energy inside the element of the kettle",
             "correct": False,
             "why": "This renames the situation rather than explaining it, "
                    "and both of those are pathways rather than stores."},
        ],
        "figure": None,
    },
    {
        "id": "p1-03-s04",
        "band": "standard",
        "text": "A student says “the brakes made the energy "
                "disappear”. What single measurement would settle it?",
        "options": [
            {"text": "Weigh the bicycle before and after braking to see if "
                     "anything was lost",
             "correct": False,
             "why": "Energy has no mass, so the balance would read the same "
                    "either way and settle nothing."},
            {"text": "Time how long the bicycle takes to stop from the same "
                     "speed twice",
             "correct": False,
             "why": "That measures the braking, not where the energy went. "
                    "It cannot distinguish the two claims."},
            {"text": "Measure the speed at the start and again once the bike "
                     "has stopped",
             "correct": False,
             "why": "That only tells you the kinetic store emptied, which "
                    "nobody disputes. The question is where it went."},
            {"text": "Put a thermometer on the brake blocks before and "
                     "immediately after braking",
             "correct": True},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "p1-03-h01",
        "band": "harder",
        "text": "If energy is never destroyed, why can you not gather the "
                "warmth of a room back into a battery?",
        "options": [
            {"text": "Because it is now shared among so many particles, "
                     "moving randomly, that it cannot be gathered",
             "correct": True},
            {"text": "Because energy in a thermal store is a different kind "
                     "of energy that batteries cannot hold",
             "correct": False,
             "why": "There are not different kinds that convert. There are "
                    "stores, and a battery's is chemical."},
            {"text": "Because some of the energy really was destroyed on the "
                     "way, despite the law",
             "correct": False,
             "why": "None of it was. The sum still balances exactly — that "
                    "is not what stops you."},
            {"text": "Because the room is not a closed system, so the law "
                     "does not apply to it at all",
             "correct": False,
             "why": "Draw the boundary wider and it is closed. The law "
                    "applies; the difficulty is practical."},
        ],
        "figure": None,
    },
    {
        "id": "p1-03-h02",
        "band": "harder",
        "text": "A student writes that a machine “loses” some "
                "energy. Why do physicists avoid that word?",
        "options": [
            {"text": "Because losing energy is only possible in a system "
                     "that is not properly closed",
             "correct": False,
             "why": "Even in an open system nothing is lost — it crosses a "
                    "boundary to somewhere you could name."},
            {"text": "Because “lost” suggests it is gone, when it "
                     "is somewhere a thermometer could find",
             "correct": True},
            {"text": "Because the correct technical word for what happens to "
                     "it is always “wasted”",
             "correct": False,
             "why": "Wasted is a judgement about intent. The objection to "
                    "“lost” is that it suggests non-existence."},
            {"text": "Because energy is never transferred out of a machine "
                     "once it has been put in",
             "correct": False,
             "why": "It very much is transferred out — into the "
                    "surroundings. That is the whole point."},
        ],
        "figure": None,
    },
    {
        "id": "p1-03-h03",
        "band": "harder",
        "text": "Someone claims a magnetic machine runs forever and lights a "
                "lamp with no fuel. What is the strongest objection?",
        "options": [
            {"text": "Magnets are not strong enough to keep a machine "
                     "turning for a long period",
             "correct": False,
             "why": "Strength is not the issue. No arrangement of any "
                    "strength can work, which is a much stronger claim."},
            {"text": "Friction would slow it down, so it would need oiling "
                     "regularly to keep going",
             "correct": False,
             "why": "Closer, but oiling only reduces friction. The objection "
                    "does not depend on how much there is."},
            {"text": "The lamp needs energy continuously, and no store is "
                     "named that could be supplying it",
             "correct": True},
            {"text": "The machine would gradually get warmer and warmer "
                     "until it eventually broke down",
             "correct": False,
             "why": "It would run down rather than heat up, and either way "
                    "that is a symptom rather than the reason."},
        ],
        "figure": None,
    },
    {
        "id": "p1-03-h04",
        "band": "harder",
        "text": "In the 1920s energy appeared to go missing in a kind of "
                "radioactive decay. What did physicists conclude?",
        "options": [
            {"text": "That conservation of energy holds only for large "
                     "everyday objects and not for atoms",
             "correct": False,
             "why": "The opposite. They trusted it at that scale enough to "
                    "predict something new from it."},
            {"text": "That the measurements were too unreliable to say "
                     "anything useful about the decay",
             "correct": False,
             "why": "The shortfall was real and repeatable, which is exactly "
                    "why it was worth explaining."},
            {"text": "That energy really can be destroyed, but only in "
                     "radioactive processes",
             "correct": False,
             "why": "No exception has ever been found, and this was not "
                    "one — the missing energy was located."},
            {"text": "That an undetected particle was carrying the missing "
                     "energy away, which was later found",
             "correct": True},
        ],
        "figure": None,
    },
]
