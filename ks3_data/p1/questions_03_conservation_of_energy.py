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
            {"text": "The total has fallen by the same fraction as the "
                     "height the ball failed to reach",
             "correct": False,
             "why": "The height fell; the total did not. Height measures one "
                    "store, not the whole account."},
            {"text": "The total has fallen because the floor absorbed "
                     "part of it and destroyed it",
             "correct": False,
             "why": "The floor received it and is very slightly warmer. "
                    "Absorbing is not destroying."},
            {"text": "The total is unchanged, because the ball will "
                     "eventually bounce back up to 1 m",
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
            {"text": "Because a triangle is only used for the sort of "
                     "equations students meet later on",
             "correct": False,
             "why": "It is not about when you meet it. It is about what "
                    "shape the relationship actually has."},
            {"text": "Because the relationship is a sum on each side, and a "
                     "triangle means multiply or divide",
             "correct": True},
            {"text": "Because a beam can show four stores at once and a "
                     "triangle can only ever show three",
             "correct": False,
             "why": "The count is not the reason. A triangle would be wrong "
                    "even with exactly three stores."},
            {"text": "Because energy is measured in joules and formula "
                     "triangles only work for other units",
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
             "why": "A balance cannot follow energy from one store to "
                    "another. It would read the same either way and "
                    "settle nothing."},
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

    # ── MRB-335 top-up · easier ──────────────────────────────────────────
    {
        "id": "p1-03-e05",
        "band": "easier",
        "text": "What does it mean to say energy has been dissipated?",
        "options": [
            {"text": "It has been spread thinly into thermal stores in the "
                     "surroundings",
             "correct": True},
            {"text": "It has been destroyed and no longer counts in the "
                     "total",
             "correct": False,
             "why": "Dissipated energy still exists and still counts. It is "
                    "spread out, not gone."},
            {"text": "It has been gathered back into a single useful store",
             "correct": False,
             "why": "That is the opposite of dissipation, and it is the thing "
                    "that never happens on its own."},
            {"text": "It has been turned into a new kind of energy",
             "correct": False,
             "why": "There are no new kinds. Energy has simply moved into "
                    "thermal stores."},
        ],
        "figure": None,
    },
    {
        "id": "p1-03-e06",
        "band": "easier",
        "text": "How many exceptions to the law of conservation of energy "
                "have ever been found?",
        "options": [
            {"text": "A few, in nuclear reactions", "correct": False,
             "why": "Nuclear reactions were checked especially hard, and the "
                    "total balances there too."},
            {"text": "None have ever been found", "correct": True},
            {"text": "Many, which is why it is only called a rule",
             "correct": False,
             "why": "It is called a law precisely because no exception has "
                    "survived checking."},
            {"text": "One, which physicists have not yet explained",
             "correct": False,
             "why": "The one famous gap, in radioactive decay, turned out to "
                    "be a missing particle rather than missing energy."},
        ],
        "figure": None,
    },
    {
        "id": "p1-03-e07",
        "band": "easier",
        "text": "A firework explodes and the energy spreads out in every "
                "direction. What is the total energy afterwards?",
        "options": [
            {"text": "Smaller, because the energy has spread out",
             "correct": False,
             "why": "Spreading out changes how useful energy is, never how "
                    "much of it there is."},
            {"text": "Larger, because the explosion released extra energy",
             "correct": False,
             "why": "Nothing is released from outside the account; the "
                    "chemical store supplied all of it."},
            {"text": "Impossible to say without weighing the firework",
             "correct": False,
             "why": "The total is the same whatever the firework weighs — "
                    "that is what the law says."},
            {"text": "Exactly the same as before", "correct": True},
        ],
        "figure": None,
    },

    # ── MRB-335 top-up · standard ────────────────────────────────────────
    {
        "id": "p1-03-s05",
        "band": "standard",
        "text": "A child on a swing is given one push and then left alone. "
                "Why does each swing rise a little less high?",
        "options": [
            {"text": "Because the gravitational store is slowly being used up "
                     "as the child swings",
             "correct": False,
             "why": "No store is used up. It empties into thermal stores in "
                    "the air and the pivot."},
            {"text": "Because energy is dissipated to thermal stores by air "
                     "resistance",
             "correct": True},
            {"text": "Because gravity gets stronger the longer the swing "
                     "goes on",
             "correct": False,
             "why": "Gravity is unchanged throughout; nothing about the pull "
                    "on the child alters."},
            {"text": "Because the child gets heavier as they tire",
             "correct": False,
             "why": "The mass does not change, and a heavier child would not "
                    "swing lower anyway."},
        ],
        "figure": None,
    },
    {
        "id": "p1-03-s06",
        "band": "standard",
        "text": "A hot drink cools in a room. Where must the boundary of the "
                "closed system be drawn?",
        "options": [
            {"text": "Around the drink only", "correct": False,
             "why": "Energy crosses that boundary as the drink cools, so the "
                    "total inside it falls."},
            {"text": "Around the mug and the table it stands on",
             "correct": False,
             "why": "The air is carrying energy away too, so this boundary "
                    "still leaks."},
            {"text": "Around the drink and the whole room", "correct": True},
            {"text": "Around the drink and the person waiting to drink it",
             "correct": False,
             "why": "The room takes most of the energy, and it is outside "
                    "this boundary."},
        ],
        "figure": None,
    },
    {
        "id": "p1-03-s07",
        "band": "standard",
        "text": "A group measures 500 J going into a pulley and 470 J coming "
                "out, and concludes the law is broken. What should they do "
                "next?",
        "options": [
            {"text": "Repeat the experiment until the two numbers match "
                     "exactly",
             "correct": False,
             "why": "They will never match at the useful end. The missing "
                    "30 J is real and needs finding, not removing."},
            {"text": "Report that conservation of energy does not hold for "
                     "pulleys",
             "correct": False,
             "why": "No exception has ever survived checking, and this one is "
                    "explained by friction."},
            {"text": "Add the 30 J on at the end so the totals balance",
             "correct": False,
             "why": "Writing in a number is not accounting for it. The 30 J "
                    "has to be found somewhere real."},
            {"text": "Look for the missing 30 J in thermal stores in the "
                     "rope and axle",
             "correct": True},
        ],
        "figure": None,
    },

    # ── MRB-335 top-up · harder ──────────────────────────────────────────
    {
        "id": "p1-03-h05",
        "band": "harder",
        "text": "Water falls 40 m through a hydroelectric turbine. Only part "
                "of the energy reaches the generator. Which account is "
                "right?",
        "options": [
            {"text": "The rest fills thermal stores in the water and pipes, "
                     "so the total holds",
             "correct": True},
            {"text": "The rest is destroyed by the turbine blades",
             "correct": False,
             "why": "Blades cannot destroy energy; they can only pass it to "
                    "other stores."},
            {"text": "The rest never existed, because only useful energy "
                     "counts",
             "correct": False,
             "why": "The whole gravitational store emptied, so all of it has "
                    "to be accounted for."},
            {"text": "The rest stays in the water's gravitational store at "
                     "the bottom",
             "correct": False,
             "why": "The water has already fallen, so that store has emptied "
                    "by the time it leaves."},
        ],
        "figure": None,
    },
    {
        "id": "p1-03-h06",
        "band": "harder",
        "text": "A student says conservation of energy means nothing can ever "
                "run out. What has been confused?",
        "options": [
            {"text": "The total staying fixed with a useful store staying "
                     "full",
             "correct": True},
            {"text": "Conservation with efficiency, which many people think "
                     "are the same idea",
             "correct": False,
             "why": "They are different: efficiency is the share that goes "
                    "where you wanted, and conservation is about the total."},
            {"text": "Energy with power, which is measured in watts",
             "correct": False,
             "why": "Power is energy per second. Nothing in the student's "
                    "claim is about time."},
            {"text": "Nothing — a fuel really does last for ever",
             "correct": False,
             "why": "A tank empties. Its energy still exists, but spread "
                    "through the surroundings where nothing can use it."},
        ],
        "figure": None,
    },
    {
        "id": "p1-03-h07",
        "band": "harder",
        "text": "A sealed vacuum flask of hot water is left for a week and "
                "its temperature has fallen a little. What is the best "
                "conclusion?",
        "options": [
            {"text": "Energy has been destroyed slowly over the week",
             "correct": False,
             "why": "A week is no different from a second: energy is not "
                    "destroyed at any rate."},
            {"text": "The flask is not a truly closed system, so energy "
                     "escapes",
             "correct": True},
            {"text": "The law of conservation of energy fails over long "
                     "enough periods",
             "correct": False,
             "why": "It has been tested over far longer than a week and has "
                    "never failed."},
            {"text": "The water has turned some of its energy into cold",
             "correct": False,
             "why": "Cold is not a substance and not a store. There is only "
                    "less energy in the water."},
        ],
        "figure": None,
    },
]
