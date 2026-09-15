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

    # ── MRB-338 night 3 top-up · easier ─────────────────────────────────
    {
        "id": "p1-03-e08",
        "band": "easier",
        "text": "A torch is left switched on until the battery is flat. Where "
                "is the energy that was in the battery's chemical store?",
        "options": [
            {"text": "In thermal stores in the bulb, the torch and the room",
             "correct": True},
            {"text": "Used up completely, which is exactly what a flat "
                     "battery means",
             "correct": False,
             "why": "Nothing is used up. A flat battery is one whose chemical "
                    "store has emptied into other stores."},
            {"text": "Destroyed by the bulb while it was making light",
             "correct": False,
             "why": "A bulb has no mechanism for destroying energy. It moves "
                    "it into light and thermal stores."},
            {"text": "Still in the battery, but now too weak to come out",
             "correct": False,
             "why": "The store has emptied. There is nothing weak sitting "
                    "inside waiting to be released."},
        ],
        "figure": None,
    },
    {
        "id": "p1-03-e09",
        "band": "easier",
        "text": "Before a change a system holds 400 J. Afterwards one store "
                "holds 250 J. How much is in the other stores?",
        "options": [
            {"text": "650 J", "correct": False,
             "why": "That is 400 + 250. The two figures are parts of one "
                    "total, so they are not added together."},
            {"text": "150 J", "correct": True},
            {"text": "400 J", "correct": False,
             "why": "That is the whole total. Some of it is already accounted "
                    "for in the store holding 250 J."},
            {"text": "0 J", "correct": False,
             "why": "The total has not changed, so 150 J must be somewhere. "
                    "An empty answer leaves the sum short."},
        ],
        "figure": None,
    },
    {
        "id": "p1-03-e10",
        "band": "easier",
        "text": "A car is parked on a drive with a full fuel tank. Which "
                "statement about its energy is correct?",
        "options": [
            {"text": "It has run out of energy, which is why it is not "
                     "moving at the moment",
             "correct": False,
             "why": "A full tank is an enormous store. Being still says "
                    "nothing about how much energy an object holds."},
            {"text": "It holds no energy at all until the engine has been "
                     "started up by the driver",
             "correct": False,
             "why": "The chemical store in the fuel is there whether the "
                    "engine runs or not."},
            {"text": "Its kinetic store is empty and its chemical store is "
                     "full",
             "correct": True},
            {"text": "Its energy was destroyed when it stopped and has to be "
                     "replaced with more fuel",
             "correct": False,
             "why": "Stopping destroys nothing. The fuel in the tank was "
                    "never touched by the car stopping."},
        ],
        "figure": None,
    },
    {
        "id": "p1-03-e11",
        "band": "easier",
        "text": "Can a machine create energy?",
        "options": [
            {"text": "Yes, if it is well enough designed and efficient "
                     "enough",
             "correct": False,
             "why": "Efficiency describes how the energy is shared out. No "
                    "amount of it creates any."},
            {"text": "Yes, but only in very small amounts at a time",
             "correct": False,
             "why": "Not in any amount. The law has no small print allowing a "
                    "little creation."},
            {"text": "Only an electric motor can; a lever cannot",
             "correct": False,
             "why": "A motor moves energy from an electrical supply. It "
                    "creates none of it."},
            {"text": "No — it can only move energy between stores",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p1-03-e12",
        "band": "easier",
        "text": "Does energy that has been dissipated into the surroundings "
                "still count in the total?",
        "options": [
            {"text": "Yes — it still exists, spread thinly through the "
                     "surroundings",
             "correct": True},
            {"text": "No — once it has spread out it stops counting",
             "correct": False,
             "why": "Spreading out changes how useful energy is, never "
                    "whether it exists."},
            {"text": "Only if somebody can still gather it up and put it "
                     "back to use again",
             "correct": False,
             "why": "Being useful is a separate question from being real. "
                    "It counts either way."},
            {"text": "Only while the system is still sealed shut",
             "correct": False,
             "why": "Sealing decides where the boundary is, not whether "
                    "dissipated energy exists."},
        ],
        "figure": None,
    },
    {
        "id": "p1-03-e13",
        "band": "easier",
        "text": "Why is “because it had energy” never a complete "
                "explanation of why something happened?",
        "options": [
            {"text": "Because energy explains electrical changes and "
                     "nothing else",
             "correct": False,
             "why": "It is used across all of physics. The trouble is what it "
                    "can and cannot explain."},
            {"text": "Because energy is conserved, so it is never used up and "
                     "never the cause",
             "correct": True},
            {"text": "Because you are expected to name the type of energy "
                     "involved in the change as well",
             "correct": False,
             "why": "Naming a type does not help either, and there are stores "
                    "and pathways rather than types."},
            {"text": "Because the amount of energy involved is usually far "
                     "too small to make a difference",
             "correct": False,
             "why": "The amount can be huge. It still explains nothing on its "
                    "own."},
        ],
        "figure": None,
    },
    {
        "id": "p1-03-e14",
        "band": "easier",
        "text": "A drill makes a hole in a plank and the bit is hot "
                "afterwards. Where is the extra energy?",
        "options": [
            {"text": "It went back up the cable into the electricity supply",
             "correct": False,
             "why": "Nothing travels back up a cable. The supply delivered "
                    "energy and did not take any back."},
            {"text": "It is stored inside the hole that was made",
             "correct": False,
             "why": "A hole is an absence of wood. It is not a store and "
                    "holds nothing."},
            {"text": "In thermal stores in the bit, the plank and the air",
             "correct": True},
            {"text": "It was destroyed by the cutting edges of the drill bit",
             "correct": False,
             "why": "Cutting cannot destroy energy. The hot bit is where a "
                    "lot of it ended up."},
        ],
        "figure": None,
    },
    {
        "id": "p1-03-e15",
        "band": "easier",
        "text": "Which machines obey the law of conservation of energy?",
        "options": [
            {"text": "Only the efficient ones", "correct": False,
             "why": "A wasteful machine obeys it just as exactly. Efficiency "
                    "is about where the energy goes."},
            {"text": "Only ones with no moving parts", "correct": False,
             "why": "Moving parts add friction, not exceptions. Every machine "
                    "obeys it."},
            {"text": "Only ones running in a sealed room", "correct": False,
             "why": "A room's walls do not change the law. They only change "
                    "where you draw the boundary."},
            {"text": "Every one, efficient or wasteful", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p1-03-e16",
        "band": "easier",
        "text": "A lamp is described as wasting most of the energy supplied "
                "to it. What does “wasted” mean here?",
        "options": [
            {"text": "It ended up somewhere useless rather than where it was "
                     "wanted",
             "correct": True},
            {"text": "It was destroyed instead of being transferred anywhere",
             "correct": False,
             "why": "Wasted energy is still all there. Only its usefulness "
                    "has gone."},
            {"text": "It never left the mains supply and was not delivered",
             "correct": False,
             "why": "It was delivered. You can feel it as warmth coming off "
                    "the lamp."},
            {"text": "It was put into storage inside the lamp for later use",
             "correct": False,
             "why": "A lamp stores nothing for later. The energy passed "
                    "straight through into the room."},
        ],
        "figure": None,
    },
    {
        "id": "p1-03-e17",
        "band": "easier",
        "text": "Which of these is closest to being a closed system?",
        "options": [
            {"text": "A saucepan of water boiling on an open gas hob in a "
                     "kitchen",
             "correct": False,
             "why": "Steam and warm air leave it constantly, so energy "
                    "crosses the boundary all the time."},
            {"text": "A sealed and well-insulated box with everything inside "
                     "it",
             "correct": True},
            {"text": "A room with its window wide open on a windy day",
             "correct": False,
             "why": "Air moving in and out carries energy with it, which is "
                    "exactly what a closed system rules out."},
            {"text": "A bicycle being ridden along a road on a cold morning",
             "correct": False,
             "why": "The rider, the road and the air are all exchanging "
                    "energy across every boundary you could draw."},
        ],
        "figure": None,
    },
    {
        "id": "p1-03-e18",
        "band": "easier",
        "text": "A pendulum that has stopped is pulled back to the top and "
                "released again. Where did the energy for the second run "
                "come from?",
        "options": [
            {"text": "From the room, handing back what it took during the "
                     "first run",
             "correct": False,
             "why": "The room keeps what it was given. None of it comes "
                    "back on its own."},
            {"text": "From the pendulum's own store, which refills itself "
                     "between runs",
             "correct": False,
             "why": "Nothing refills itself. The store was empty until "
                    "somebody lifted the bob."},
            {"text": "From the person who lifted the bob",
             "correct": True},
            {"text": "From nowhere in particular",
             "correct": False,
             "why": "Lifting the bob is real work. You can feel the effort "
                    "in your arm."},
        ],
        "figure": None,
    },
    {
        "id": "p1-03-e19",
        "band": "easier",
        "text": "A ball starts with 80 J in its gravitational store. Halfway "
                "down it holds 36 J gravitational and 42 J kinetic. How much "
                "has reached thermal stores?",
        "options": [
            {"text": "78 J", "correct": False,
             "why": "That is 36 + 42, the energy still in the two named "
                    "stores rather than the amount that has left them."},
            {"text": "158 J", "correct": False,
             "why": "That adds everything to the starting total. The two "
                    "readings are parts of the 80 J, not extras."},
            {"text": "0 J", "correct": False,
             "why": "The two readings come to 78 J, so 2 J has to be "
                    "somewhere else."},
            {"text": "2 J", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p1-03-e20",
        "band": "easier",
        "text": "What does friction do to energy?",
        "options": [
            {"text": "It moves it into thermal stores", "correct": True},
            {"text": "It destroys a small amount of it", "correct": False,
             "why": "Friction has no mechanism for destroying anything. It "
                    "only moves energy."},
            {"text": "It creates a little more", "correct": False,
             "why": "Nothing creates energy, and friction certainly never "
                    "gives you more than you started with."},
            {"text": "It stops it moving between stores", "correct": False,
             "why": "Friction is itself a way energy moves between stores, so "
                    "it does the opposite."},
        ],
        "figure": None,
    },
    {
        "id": "p1-03-e21",
        "band": "easier",
        "text": "A battery fan runs until the battery is flat, and the room "
                "ends up very slightly warmer. What is the total energy now?",
        "options": [
            {"text": "Smaller, because the fan used some of it up while it "
                     "was running",
             "correct": False,
             "why": "Nothing was used up. The warmer room is where the "
                    "battery's store went."},
            {"text": "The same as it was before the fan was switched on",
             "correct": True},
            {"text": "Larger, because the fan added warmth to the room that "
                     "was not there before",
             "correct": False,
             "why": "The warmth came out of the battery, so it is not an "
                    "addition to the total."},
            {"text": "Impossible to say without measuring the room's own "
                     "temperature first",
             "correct": False,
             "why": "No measurement is needed. The total after any change "
                    "equals the total before it."},
        ],
        "figure": None,
    },
    {
        "id": "p1-03-e22",
        "band": "easier",
        "text": "On the running-total bench, hiding the thermal store makes "
                "the total appear to fall. Why does it only appear to?",
        "options": [
            {"text": "Because hiding a store destroys the energy that was "
                     "inside it",
             "correct": False,
             "why": "Hiding something on a screen changes a display, not the "
                    "world."},
            {"text": "Because the law needs every store on show",
             "correct": False,
             "why": "The law holds whether you are looking or not. Only your "
                    "count changes."},
            {"text": "Because one real store has been left out of the count",
             "correct": True},
            {"text": "Because the pendulum slows down faster once the store "
                     "is hidden",
             "correct": False,
             "why": "The swing behaves identically. Only the bar on the "
                    "screen is different."},
        ],
        "figure": None,
    },
    {
        "id": "p1-03-e23",
        "band": "easier",
        "text": "A solar panel on a roof lights a lamp indoors. Where did the "
                "lamp's energy come from?",
        "options": [
            {"text": "The panel created it out of the sunlight falling on it",
             "correct": False,
             "why": "Nothing creates energy. The panel passes on what the "
                    "sunlight brought."},
            {"text": "From the lamp's own store, which the panel released",
             "correct": False,
             "why": "A lamp holds no store. It transfers what is supplied to "
                    "it and nothing else."},
            {"text": "From the air around the panel, which cooled slightly",
             "correct": False,
             "why": "The air is not the source. A panel in the dark lights "
                    "nothing, however warm the air is."},
            {"text": "From the Sun", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p1-03-e24",
        "band": "easier",
        "text": "An escalator runs all day and its motor is warm to the touch "
                "by the evening. What does the warmth show?",
        "options": [
            {"text": "Part of the supply has filled thermal stores instead of "
                     "lifting people",
             "correct": True},
            {"text": "The motor is creating extra energy that it has no way "
                     "of passing on to anyone",
             "correct": False,
             "why": "Nothing extra is created. The warmth came out of the "
                    "mains supply like the lifting did."},
            {"text": "Energy is being destroyed inside the motor as it turns",
             "correct": False,
             "why": "A motor destroys nothing. The warmth IS the energy, "
                    "arriving somewhere nobody wanted it."},
            {"text": "The escalator has saved the warmth for tomorrow",
             "correct": False,
             "why": "It saves nothing. The warmth leaks into the building and "
                    "is gone by morning."},
        ],
        "figure": None,
    },
    {
        "id": "p1-03-e25",
        "band": "easier",
        "text": "Two trolleys collide head-on and both stop dead. What is the "
                "total energy immediately afterwards?",
        "options": [
            {"text": "Zero, because neither trolley is moving any more",
             "correct": False,
             "why": "Not moving means the kinetic stores are empty. The total "
                    "is not the kinetic store."},
            {"text": "Halved, because two moving trolleys became two still "
                     "ones",
             "correct": False,
             "why": "Nothing halves. The whole amount is still there, in "
                    "different stores."},
            {"text": "Larger, because a collision releases energy",
             "correct": False,
             "why": "A collision moves energy about. It brings none in from "
                    "outside."},
            {"text": "Unchanged, with most of it now in thermal stores and "
                     "sound",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p1-03-e26",
        "band": "easier",
        "text": "A chemical hand warmer stays hot for twenty minutes and then "
                "goes cold. What has happened?",
        "options": [
            {"text": "Its chemical store emptied into thermal stores in your "
                     "hands and the air",
             "correct": True},
            {"text": "It used up all the energy it was carrying and now has "
                     "none of its own",
             "correct": False,
             "why": "Nothing is used up. The store emptied into the "
                    "surroundings, where it still is."},
            {"text": "The cold from outside got into it and cancelled out the "
                     "warmth inside",
             "correct": False,
             "why": "There is no cold to get in. Energy left the warmer, and "
                    "nothing arrived."},
            {"text": "It destroyed its energy slowly over the course of the "
                     "twenty minutes",
             "correct": False,
             "why": "No process destroys energy, quickly or slowly. It moved "
                    "into your hands and the air."},
        ],
        "figure": None,
    },
    {
        "id": "p1-03-e27",
        "band": "easier",
        "text": "An electric car's brakes put some energy back into the "
                "battery. Can they put all of it back?",
        "options": [
            {"text": "Yes, because energy cannot be destroyed anywhere",
             "correct": False,
             "why": "Conservation says where the energy is, not that it can "
                    "all be steered back into one store."},
            {"text": "Yes, if the car is driven slowly enough beforehand",
             "correct": False,
             "why": "Slower driving reduces the amount, not the share that "
                    "escapes into thermal stores."},
            {"text": "No, braking destroys some",
             "correct": False,
             "why": "None of it is destroyed. The part that does not return "
                    "is in the tyres, brakes and air."},
            {"text": "No — some always fills thermal stores",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p1-03-e28",
        "band": "easier",
        "text": "An archer bends a bow and then lets the arrow go. Which "
                "account of the stores is right?",
        "options": [
            {"text": "The elastic store emptied and the kinetic store filled",
             "correct": True},
            {"text": "The bow created new energy as it sprang back straight",
             "correct": False,
             "why": "A bow creates nothing. It gives back what the archer put "
                    "in while bending it."},
            {"text": "The archer's energy was destroyed by the bending of the "
                     "bow",
             "correct": False,
             "why": "It was transferred into the bow's elastic store, which "
                    "is where it waited."},
            {"text": "The arrow made its own energy in flight",
             "correct": False,
             "why": "An arrow in flight makes nothing. It carries what the "
                    "bow handed over."},
        ],
        "figure": None,
    },
    {
        "id": "p1-03-e29",
        "band": "easier",
        "text": "How exact is the law of conservation of energy?",
        "options": [
            {"text": "Roughly right for everyday situations", "correct": False,
             "why": "It is not an approximation. Every careful test has found "
                    "it exact."},
            {"text": "Exact only when there is no friction", "correct": False,
             "why": "Friction moves energy rather than removing it, so it "
                    "never spoils the sum."},
            {"text": "Exact every time, with no exception found",
             "correct": True},
            {"text": "Exact only for very small objects", "correct": False,
             "why": "It has been checked from particles to galaxies and holds "
                    "at every scale."},
        ],
        "figure": None,
    },
    {
        "id": "p1-03-e30",
        "band": "easier",
        "text": "A squash ball is noticeably warmer after a long rally than "
                "it was at the start. Where did that energy come from?",
        "options": [
            {"text": "The ball made it itself while it was bouncing about",
             "correct": False,
             "why": "A ball makes nothing. Every joule in it arrived from "
                    "somewhere outside."},
            {"text": "From the air in the court, which cooled down slightly",
             "correct": False,
             "why": "The air is not the source. It ends up slightly warmer "
                    "too, not cooler."},
            {"text": "From the walls, which were warm before play started",
             "correct": False,
             "why": "Court walls sit at room temperature and warm nothing. "
                    "The ball is far hotter than they are."},
            {"text": "From the players, through the ball being squashed on "
                     "every hit",
             "correct": True},
        ],
        "figure": None,
    },

    # ── MRB-338 night 3 top-up · standard ───────────────────────────────
    {
        "id": "p1-03-s08",
        "band": "standard",
        "text": "A hoist is supplied with 900 J and the load it raises gains "
                "620 J in its gravitational store. Which account is right?",
        "options": [
            {"text": "280 J has filled thermal stores in the motor, the cable "
                     "and the air",
             "correct": True},
            {"text": "280 J was destroyed by the friction in the cable and "
                     "gears",
             "correct": False,
             "why": "Friction moves energy into thermal stores. It has never "
                    "destroyed a joule of it."},
            {"text": "The total energy has fallen from 900 J to 620 J",
             "correct": False,
             "why": "The total has not moved. Only 620 J of it went where the "
                    "operator wanted."},
            {"text": "The hoist is faulty, since energy has to be conserved",
             "correct": False,
             "why": "A perfectly healthy hoist behaves exactly like this. "
                    "Conservation is not a promise of efficiency."},
        ],
        "figure": None,
    },
    {
        "id": "p1-03-s09",
        "band": "standard",
        "text": "A cyclist brakes and the blocks become hot. Which answer "
                "explains the heating rather than renaming it?",
        "options": [
            {"text": "Because the bicycle had a great deal of energy that had "
                     "to go",
             "correct": False,
             "why": "Every moving object has energy. That cannot be why these "
                    "blocks in particular became hot."},
            {"text": "Because rubbing on the rim makes the particles of both "
                     "surfaces vibrate more",
             "correct": True},
            {"text": "Because the kinetic energy was converted into heat "
                     "energy",
             "correct": False,
             "why": "That renames the situation in words. It names no "
                    "mechanism, and heat is a pathway rather than a store."},
            {"text": "Because brakes store energy as heat",
             "correct": False,
             "why": "Brakes store nothing. The energy passes through them "
                    "into the air within minutes."},
        ],
        "figure": None,
    },
    {
        "id": "p1-03-s10",
        "band": "standard",
        "text": "On the balance beam the total is 120 J. The gravitational "
                "store holds 62 J and the kinetic store 55 J. What must the "
                "thermal store hold?",
        "options": [
            {"text": "117 J", "correct": False,
             "why": "That is 62 + 55, the amount already accounted for rather "
                    "than the amount still missing."},
            {"text": "237 J", "correct": False,
             "why": "That adds the two readings to the whole total. They are "
                    "parts of the 120 J, not extras."},
            {"text": "3 J", "correct": True},
            {"text": "0 J", "correct": False,
             "why": "The beam only stays level if the three add to 120 J, and "
                    "62 + 55 is three short."},
        ],
        "figure": None,
    },
    {
        "id": "p1-03-s11",
        "band": "standard",
        "text": "A machine is advertised as 100% efficient. Is that the same "
                "as claiming energy for free?",
        "options": [
            {"text": "Yes — at 100% it must be making its own energy",
             "correct": False,
             "why": "Reaching 100% would mean wasting none of the supply, not "
                    "running without one."},
            {"text": "Yes, because no machine can reach 100%, so the claim "
                     "already breaks the law of conservation",
             "correct": False,
             "why": "It is an unlikely claim about friction, not an "
                    "impossible one about the total."},
            {"text": "No, because efficiency has nothing whatever to do with "
                     "the energy a machine is supplied with",
             "correct": False,
             "why": "It has everything to do with it: efficiency is the share "
                    "of the supply that goes where you wanted."},
            {"text": "No — it means none is wasted, not that none is needed",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p1-03-s12",
        "band": "standard",
        "text": "A student counts the energy of a marble rolling in a bowl "
                "and finds the total falling. What has been left out?",
        "options": [
            {"text": "The thermal stores of the air and the surfaces the "
                     "marble rubs against",
             "correct": True},
            {"text": "The marble's gravitational store, which nobody counted",
             "correct": False,
             "why": "That store is the obvious one and is always counted. The "
                    "missing one is the invisible one."},
            {"text": "Nothing at all — a total really does fall whenever "
                     "something slows down and comes to rest",
             "correct": False,
             "why": "A total never falls. That is precisely the claim the "
                    "law makes."},
            {"text": "The bowl's elastic store",
             "correct": False,
             "why": "A rigid bowl is barely squashed and gives back what "
                    "little it takes. It is not where the energy went."},
        ],
        "figure": None,
    },
    {
        "id": "p1-03-s13",
        "band": "standard",
        "text": "Compare a petrol engine that is 20% efficient with an "
                "electric motor that is 90% efficient. Which conserves energy "
                "better?",
        "options": [
            {"text": "The electric motor, because it wastes far less of the "
                     "supply",
             "correct": False,
             "why": "Wasting less is a fact about where the energy goes, not "
                    "about whether the total is kept."},
            {"text": "The petrol engine, because its fuel store is far bigger",
             "correct": False,
             "why": "Store size has nothing to do with it. Both obey the law "
                    "exactly whatever they hold."},
            {"text": "Neither — both conserve it exactly",
             "correct": True},
            {"text": "The electric motor, because electricity cannot be "
                     "destroyed",
             "correct": False,
             "why": "No form can be destroyed, and electricity is a pathway "
                    "rather than a form in the first place."},
        ],
        "figure": None,
    },
    {
        "id": "p1-03-s14",
        "band": "standard",
        "text": "A car's fuel tank is empty at the end of a long journey. Has "
                "the energy that was in the fuel been used up?",
        "options": [
            {"text": "Yes, which is exactly what the word fuel is meant to "
                     "mean",
             "correct": False,
             "why": "Fuel names a concentrated store, not something that "
                    "vanishes. The store emptied into other stores."},
            {"text": "No — it is spread through the road, the air and the "
                     "exhaust gases",
             "correct": True},
            {"text": "Yes, because the engine turned it into motion and then "
                     "the brakes turned that into heat",
             "correct": False,
             "why": "Both steps are transfers and neither destroys anything, "
                    "so nothing has been used up."},
            {"text": "No — it is still in the tank in an unburnable form",
             "correct": False,
             "why": "The tank really is empty. The energy left with the "
                    "exhaust and through the wheels."},
        ],
        "figure": None,
    },
    {
        "id": "p1-03-s15",
        "band": "standard",
        "text": "A ball has been dropped and is halfway to the ground. Which "
                "statement about its stores is right?",
        "options": [
            {"text": "Both stores are empty, because the ball is between the "
                     "two positions where it holds anything",
             "correct": False,
             "why": "A falling ball is moving, so its kinetic store is "
                    "certainly not empty."},
            {"text": "The kinetic store has been emptying into the "
                     "gravitational store on the way down",
             "correct": False,
             "why": "That is the journey in reverse. Falling empties the "
                    "gravitational store and fills the kinetic one."},
            {"text": "The gravitational store has partly emptied and the "
                     "kinetic store has filled",
             "correct": True},
            {"text": "The gravitational store is still full",
             "correct": False,
             "why": "It empties as the ball falls. Halfway down, roughly half "
                    "of it has already gone."},
        ],
        "figure": None,
    },
    {
        "id": "p1-03-s16",
        "band": "standard",
        "text": "A student opens the fridge door to cool the kitchen down. "
                "Why does the kitchen end up warmer instead?",
        "options": [
            {"text": "The fridge moves energy to the coils at its back and "
                     "adds its motor's share on top",
             "correct": True},
            {"text": "The fridge creates cold, which the warm air then "
                     "destroys",
             "correct": False,
             "why": "Nothing creates cold, and nothing destroys anything. "
                    "There is only energy, moving."},
            {"text": "The open door lets the cold escape from the fridge "
                     "before it has had time to cool anything down",
             "correct": False,
             "why": "Cold does not escape or travel. Energy moves into the "
                    "fridge from the kitchen."},
            {"text": "Nothing happens, because the kitchen stays at the "
                     "temperature it started",
             "correct": False,
             "why": "The motor runs continuously and everything it is "
                    "supplied with ends up in the room."},
        ],
        "figure": None,
    },
    {
        "id": "p1-03-s17",
        "band": "standard",
        "text": "On the bench, switching friction off makes the swing carry "
                "on for ever. Why can no real pendulum do that?",
        "options": [
            {"text": "Because a real pendulum eventually runs out of the "
                     "energy given",
             "correct": False,
             "why": "It runs down rather than running out. Every joule it was "
                    "given still exists in the room."},
            {"text": "Because the air and the pivot always take a share into "
                     "thermal stores",
             "correct": True},
            {"text": "Because gravity slowly weakens the longer a pendulum "
                     "keeps on swinging backwards and forwards",
             "correct": False,
             "why": "Gravity does not weaken. The pull on the bob is the same "
                    "at the first swing and the last."},
            {"text": "Because real string stretches, and stretching a string "
                     "destroys a little energy every time",
             "correct": False,
             "why": "Stretching stores energy and gives most of it back. "
                    "Nothing about it destroys any."},
        ],
        "figure": None,
    },
    {
        "id": "p1-03-s18",
        "band": "standard",
        "text": "A child on a pogo stick reaches the same height each bounce "
                "only while they keep pushing. Why is the pushing needed?",
        "options": [
            {"text": "Because the spring makes a little less energy each "
                     "bounce",
             "correct": False,
             "why": "A spring makes none at all. It gives back what was put "
                    "into it, minus a little to thermal stores."},
            {"text": "Because gravity takes a share of the energy away on "
                     "every single bounce and does not return it",
             "correct": False,
             "why": "Gravity hands the gravitational store back on the way "
                    "down. It keeps nothing."},
            {"text": "Because each bounce sends a share to thermal stores, so "
                     "it has to be topped up",
             "correct": True},
            {"text": "Because the child's mass rises slightly each bounce",
             "correct": False,
             "why": "Their mass does not change, and a heavier child would "
                    "not bounce lower for that reason anyway."},
        ],
        "figure": None,
    },
    {
        "id": "p1-03-s19",
        "band": "standard",
        "text": "An oven is switched off after cooking and is cold by "
                "morning. What has happened, in terms of conservation?",
        "options": [
            {"text": "The oven's energy was destroyed by the cold air "
                     "overnight",
             "correct": False,
             "why": "Cold air destroys nothing. It is simply the place the "
                    "energy moved to."},
            {"text": "The oven has run out of the energy it was given while "
                     "cooking",
             "correct": False,
             "why": "Nothing runs out. The energy left the oven and is now "
                    "spread through the kitchen."},
            {"text": "The kitchen's total has fallen overnight",
             "correct": False,
             "why": "The kitchen gained exactly what the oven lost, so its "
                    "total did not fall at all."},
            {"text": "Energy crossed out of the oven into the kitchen",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p1-03-s20",
        "band": "standard",
        "text": "A speaker plays loudly and then the music stops. Where has "
                "the energy that was carried by the sound gone?",
        "options": [
            {"text": "Into thermal stores in the walls, the furniture and the "
                     "air",
             "correct": True},
            {"text": "It faded away until none of it existed anywhere",
             "correct": False,
             "why": "Fading describes what you hear. The energy went "
                    "somewhere, and it is still there."},
            {"text": "It was absorbed by the walls and destroyed inside them",
             "correct": False,
             "why": "Absorbing is receiving. The walls are very slightly "
                    "warmer, which is where it is."},
            {"text": "It returned to the speaker to be used again",
             "correct": False,
             "why": "Nothing travels back into a speaker. The supply has to "
                    "provide it fresh every time."},
        ],
        "figure": None,
    },
    {
        "id": "p1-03-s21",
        "band": "standard",
        "text": "You stretch an elastic band, hold it, and then let go so "
                "that it flies across the room. Which account is right?",
        "options": [
            {"text": "The band created its own kinetic energy at the instant "
                     "it snapped back into shape again",
             "correct": False,
             "why": "It created nothing. Every joule it flew off with came "
                    "out of your arm."},
            {"text": "Stretching destroyed a little of the energy and letting "
                     "go made the same amount over again",
             "correct": False,
             "why": "Neither happens. Stretching filled a store and releasing "
                    "emptied it."},
            {"text": "Your chemical store filled the band's elastic store, "
                     "which then filled its kinetic store",
             "correct": True},
            {"text": "The band's elastic store refilled itself",
             "correct": False,
             "why": "Nothing refills itself. The store emptied as the band "
                    "took off and stayed empty."},
        ],
        "figure": None,
    },
    {
        "id": "p1-03-s22",
        "band": "standard",
        "text": "A nail hammered into wood is hot afterwards. What does that "
                "tell you about the energy of the hammer blows?",
        "options": [
            {"text": "It ended up in thermal stores in the nail, the hammer "
                     "and the wood",
             "correct": True},
            {"text": "It was destroyed at the instant the hammer stopped "
                     "moving against the head of the nail",
             "correct": False,
             "why": "Stopping destroys nothing. The hot nail is the evidence "
                    "of where it went."},
            {"text": "It was stored inside the nail, and could be hammered "
                     "back out again later if you wanted it",
             "correct": False,
             "why": "A nail holds no such store. Its warmth leaks into the "
                    "wood and the air within minutes."},
            {"text": "It all became the sound of the blow and nothing else",
             "correct": False,
             "why": "Sound carries a tiny share. The warm nail shows most of "
                    "it went somewhere quieter."},
        ],
        "figure": None,
    },
    {
        "id": "p1-03-s23",
        "band": "standard",
        "text": "A says a rolling ball's energy was destroyed when it "
                "stopped; B says it moved. Which observation supports B?",
        "options": [
            {"text": "The ball rolled a long way across the floor before "
                     "stopping",
             "correct": False,
             "why": "How far it rolled says nothing about where the energy "
                    "finished up. Both accounts predict it."},
            {"text": "The ball was already moving quickly when it was released",
             "correct": False,
             "why": "That is about the start, not the end. It cannot tell the "
                    "two accounts apart."},
            {"text": "The ball is at rest, so its kinetic store must be empty",
             "correct": False,
             "why": "Both students agree the kinetic store is empty. The "
                    "argument is about where its contents went."},
            {"text": "The ball and the floor are very slightly warmer",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p1-03-s24",
        "band": "standard",
        "text": "A pumped-storage station uses cheap night-time electricity "
                "to pump water uphill into a reservoir. Where is the energy "
                "while the water sits up there?",
        "options": [
            {"text": "In the water's gravitational store",
             "correct": True},
            {"text": "In the pump, which holds it until somebody needs it",
             "correct": False,
             "why": "The pump is a machine, not a store. It has finished with "
                    "the energy the moment the water is up."},
            {"text": "In the electricity, which waits in the cables",
             "correct": False,
             "why": "Electricity is a pathway. Nothing sits waiting in a "
                    "cable once the current has stopped."},
            {"text": "In the water's kinetic store, because it flowed uphill",
             "correct": False,
             "why": "The water is still once it arrives, so its kinetic store "
                    "is empty again."},
        ],
        "figure": None,
    },
    {
        "id": "p1-03-s25",
        "band": "standard",
        "text": "A rowing boat is allowed to glide and slowly comes to a stop "
                "in still water. Which account is right?",
        "options": [
            {"text": "Its kinetic store emptied into thermal stores in the "
                     "water and the hull of the boat",
             "correct": True},
            {"text": "Its kinetic store was destroyed by the resistance of the "
                     "water",
             "correct": False,
             "why": "Water resistance moves energy into the water. It has no "
                    "way of destroying any."},
            {"text": "The water pushed the energy back into the rower's "
                     "muscles",
             "correct": False,
             "why": "Nothing travels back to the rower. A body cannot be "
                    "recharged from a thermal store."},
            {"text": "The boat used up the energy the rower gave it",
             "correct": False,
             "why": "Nothing is used up. It is in the water, spread far too "
                    "thinly to notice."},
        ],
        "figure": None,
    },
    {
        "id": "p1-03-s26",
        "band": "standard",
        "text": "A wind turbine's blades leave the air behind them moving "
                "more slowly than the air in front. Where does the "
                "electricity's energy come from?",
        "options": [
            {"text": "The turbine makes it from nothing",
             "correct": False,
             "why": "Nothing creates energy. The slowed air is the evidence "
                    "of where it came from."},
            {"text": "From the kinetic store of the moving air",
             "correct": True},
            {"text": "From the generator's magnets, which hold a large store",
             "correct": False,
             "why": "Magnets hold no such store. A generator with no turning "
                    "force produces nothing at all."},
            {"text": "From the tower, which is pushed by the wind and holds it",
             "correct": False,
             "why": "A tower is a support. It stores nothing and passes "
                    "nothing on to the blades."},
        ],
        "figure": None,
    },
    {
        "id": "p1-03-s27",
        "band": "standard",
        "text": "A phone left switched on but untouched still goes flat after "
                "a few days. Why?",
        "options": [
            {"text": "Because energy leaks out of a battery and is destroyed "
                     "by the air around the phone",
             "correct": False,
             "why": "Nothing destroys it. It was supplied to the circuits and "
                    "ended up warming them."},
            {"text": "Because a flat battery is one whose energy has been "
                     "destroyed",
             "correct": False,
             "why": "A flat battery is an empty store, and emptying is not "
                    "destroying."},
            {"text": "Because energy is still supplied to the circuits, and "
                     "ends up warming them",
             "correct": True},
            {"text": "Because the battery gives its energy back to the charger",
             "correct": False,
             "why": "An unplugged phone has nothing to give anything back "
                    "to."},
        ],
        "figure": None,
    },
    {
        "id": "p1-03-s28",
        "band": "standard",
        "text": "The first hill of a rollercoaster is always the tallest on "
                "the ride. Why can no later hill be taller than it?",
        "options": [
            {"text": "Because the car can never gain energy it was not given "
                     "at the start",
             "correct": True},
            {"text": "Because a car on a taller later hill would be going too "
                     "fast",
             "correct": False,
             "why": "It would be moving slower, not faster. Safety is not "
                    "what sets the limit."},
            {"text": "Because the track is not built strongly enough to "
                     "support a taller hill further along the ride",
             "correct": False,
             "why": "Engineers could build one easily. No car would get over "
                    "it."},
            {"text": "Because the car loses all its energy at the bottom",
             "correct": False,
             "why": "At the bottom of the first drop its kinetic store is "
                    "fullest, which is the opposite."},
        ],
        "figure": None,
    },
    {
        "id": "p1-03-s29",
        "band": "standard",
        "text": "Two identical toy cars are released down the same slope, one "
                "onto carpet and one onto a smooth floor. What differs?",
        "options": [
            {"text": "How much energy each car was given at the top",
             "correct": False,
             "why": "Identical cars from the same height start with the same "
                    "amount. The slope does not know what is below it."},
            {"text": "Where the energy ends up, not how much of it there is",
             "correct": True},
            {"text": "How much of the energy is destroyed as each car crosses "
                     "its surface",
             "correct": False,
             "why": "None is destroyed on either surface. The carpet simply "
                    "takes its share sooner."},
            {"text": "Whether conservation of energy applies to the car on the "
                     "rougher surface",
             "correct": False,
             "why": "It applies identically to both. Roughness changes the "
                    "route, never the law."},
        ],
        "figure": None,
    },
    {
        "id": "p1-03-s30",
        "band": "standard",
        "text": "A hand-cranked generator is easy to turn until its lamp is "
                "connected, and then it becomes hard. Why?",
        "options": [
            {"text": "Because the generator begins creating extra energy that "
                     "pushes back",
             "correct": False,
             "why": "It creates none. Everything the lamp gives out has to "
                    "come through your arm."},
            {"text": "Because the wires become heavier once a current flows "
                     "along them",
             "correct": False,
             "why": "A current adds no weight. The extra effort is energy, "
                    "not mass."},
            {"text": "Because you must now supply the energy the lamp gives "
                     "out",
             "correct": True},
            {"text": "Because the lamp pulls the handle back with a magnetic "
                     "force",
             "correct": False,
             "why": "A lamp is not a magnet. The resistance you feel is the "
                    "energy the lamp is taking."},
        ],
        "figure": None,
    },
    # ── MRB-338 night 3 top-up · harder ─────────────────────────────────
    {
        "id": "p1-03-h08",
        "band": "harder",
        "text": "Energy is never destroyed, so why do governments talk about "
                "an energy crisis at all?",
        "options": [
            {"text": "Because useful, concentrated stores run out even though "
                     "the total never does",
             "correct": True},
            {"text": "Because the total amount of energy on Earth has been "
                     "slowly falling for centuries",
             "correct": False,
             "why": "The total is not falling. What is falling is the number "
                    "of concentrated stores left to draw on."},
            {"text": "Because energy really is destroyed inside a power "
                     "station when fuel is burnt",
             "correct": False,
             "why": "Burning transfers energy. A power station's own waste "
                    "heat is where the rest of it goes."},
            {"text": "Because conservation stops working on a national scale",
             "correct": False,
             "why": "Scale makes no difference. The law holds for a country "
                    "exactly as it holds for a pendulum."},
        ],
        "figure": None,
    },
    {
        "id": "p1-03-h09",
        "band": "harder",
        "text": "A sealed, perfectly insulated box holds a battery, a motor "
                "and a fan. The battery is left to run flat. What happens to "
                "the total energy inside the box?",
        "options": [
            {"text": "It falls steadily, because the battery is emptying all "
                     "the time the fan runs",
             "correct": False,
             "why": "The battery's store empties into other stores in the "
                    "box, so the total inside is untouched."},
            {"text": "It rises, because the motor adds energy of its own to "
                     "the air inside the box",
             "correct": False,
             "why": "A motor adds nothing. Everything it delivers came out "
                    "of the battery."},
            {"text": "It stays exactly the same, though it is shared out "
                     "differently",
             "correct": True},
            {"text": "It cannot be worked out without opening the box",
             "correct": False,
             "why": "Nothing crosses the boundary, so the total is known "
                    "without measuring anything."},
        ],
        "figure": None,
    },
    {
        "id": "p1-03-h10",
        "band": "harder",
        "text": "Why is a machine's “wasted” energy a statement "
                "about what you wanted rather than about what exists?",
        "options": [
            {"text": "Because a machine that works properly does not waste "
                     "any energy in the first place",
             "correct": False,
             "why": "Every real machine wastes some. Working properly is not "
                    "the same as wasting none."},
            {"text": "Because waste can only be measured once the machine is "
                     "off",
             "correct": False,
             "why": "It can be measured while the machine runs. Timing is "
                    "not what makes the word odd."},
            {"text": "Because the wasted share still exists in a store you "
                     "had no use for",
             "correct": True},
            {"text": "Because efficient machines waste none, so the word "
                     "cannot apply",
             "correct": False,
             "why": "No machine is perfectly efficient. Every one of them "
                    "fills a store somebody did not want."},
        ],
        "figure": None,
    },
    {
        "id": "p1-03-h11",
        "band": "harder",
        "text": "A pile driver's hammer holds 12 000 J at the top. At the "
                "instant of impact its kinetic store holds 11 400 J. What is "
                "the best conclusion?",
        "options": [
            {"text": "600 J was destroyed on the way down by the air pushed "
                     "aside",
             "correct": False,
             "why": "Air resistance moves energy into the air. It destroys "
                    "none of it on the way."},
            {"text": "The hammer must have been released from lower down "
                     "than the operator believed",
             "correct": False,
             "why": "The starting store was measured at 12 000 J. A "
                    "shortfall at the bottom does not undo that."},
            {"text": "600 J has already filled thermal stores in the air and "
                     "the guide rails",
             "correct": True},
            {"text": "Some of the gravitational store stayed behind and "
                     "never converted into anything",
             "correct": False,
             "why": "At the bottom the gravitational store is empty. There "
                    "is nothing left behind in it."},
        ],
        "figure": None,
    },
    {
        "id": "p1-03-h12",
        "band": "harder",
        "text": "A student says perpetual motion is only a matter of better "
                "engineering. What has been misunderstood?",
        "options": [
            {"text": "The law forbids the output exceeding the input, however "
                     "well a machine is built",
             "correct": True},
            {"text": "Better engineering would reduce friction, so the claim "
                     "is nearly right",
             "correct": False,
             "why": "Reducing friction gets you closer to breaking even, "
                    "never past it. The gap is not the problem."},
            {"text": "The law applies only to machines somebody has actually "
                     "built",
             "correct": False,
             "why": "It rules out designs before they are built, which is "
                    "why patent offices refuse to look at them."},
            {"text": "Perpetual motion is allowed, but nobody has found the "
                     "design",
             "correct": False,
             "why": "It is not allowed at all. No arrangement of any parts "
                    "can put out more than it takes in."},
        ],
        "figure": None,
    },
    {
        "id": "p1-03-h13",
        "band": "harder",
        "text": "Pauli's proposed particle went undetected for twenty-six "
                "years. Why was the proposal taken seriously meanwhile?",
        "options": [
            {"text": "Because Pauli was the best-known physicist of his "
                     "generation",
             "correct": False,
             "why": "Reputation is not evidence, and Pauli himself "
                    "apologised for how hard the idea was to test."},
            {"text": "Because conservation had survived every other test",
             "correct": True},
            {"text": "Because a particle nobody can detect cannot be disproved",
             "correct": False,
             "why": "That would be a reason to distrust it, not to accept "
                    "it. It was accepted once it was found."},
            {"text": "Because exactly the same amount was missing in every "
                     "decay",
             "correct": False,
             "why": "The shortfall varied from decay to decay, which is part "
                    "of what made it so puzzling."},
        ],
        "figure": None,
    },
    {
        "id": "p1-03-h14",
        "band": "harder",
        "text": "A skydiver under an open parachute falls at a steady speed. "
                "The gravitational store is emptying and the kinetic store is "
                "not filling. Where is the energy going?",
        "options": [
            {"text": "Back into the gravitational store, which is why the "
                     "speed stays steady",
             "correct": False,
             "why": "A store cannot refill itself from nothing, and the "
                    "skydiver is still going down."},
            {"text": "Into the parachute's elastic store as it stretches",
             "correct": False,
             "why": "The canopy stretches once, at opening, and then holds "
                    "its shape. It fills nothing after that."},
            {"text": "Into thermal stores in the air the parachute pushes "
                     "through",
             "correct": True},
            {"text": "Nowhere, since the speed is not changing",
             "correct": False,
             "why": "The skydiver is still descending, so the gravitational "
                    "store is still emptying into something."},
        ],
        "figure": None,
    },
    {
        "id": "p1-03-h15",
        "band": "harder",
        "text": "Why is “the total energy of the universe is fixed” "
                "a stronger claim than “energy is conserved in this "
                "experiment”?",
        "options": [
            {"text": "Because the universe is very much larger than any "
                     "experiment a laboratory could ever run",
             "correct": False,
             "why": "Size is not what makes it stronger. A boundary with "
                    "nothing outside it is."},
            {"text": "Because an experiment can be repeated many times over "
                     "and the universe cannot be repeated at all",
             "correct": False,
             "why": "Repeatability is about testing a claim, not about how "
                    "strong the claim itself is."},
            {"text": "Because it needs the boundary drawn round everything, "
                     "with nothing left outside",
             "correct": True},
            {"text": "Because the law has only been tested on the universe as "
                     "a whole",
             "correct": False,
             "why": "It is tested in laboratories constantly. The universe "
                    "is the hardest case, not the only one."},
        ],
        "figure": None,
    },
    {
        "id": "p1-03-h16",
        "band": "harder",
        "text": "A heat pump delivers 360 J into a house for every 120 J of "
                "electricity it is supplied with. Does that break the law?",
        "options": [
            {"text": "No — the other 240 J came from the cold air outside",
             "correct": True},
            {"text": "Yes — it gives out three times what it takes in, which "
                     "is forbidden",
             "correct": False,
             "why": "The law forbids energy appearing from nowhere. Here it "
                    "is arriving from somewhere nameable."},
            {"text": "No — a heat pump is more than 100% efficient, which is "
                     "allowed",
             "correct": False,
             "why": "Nothing exceeds 100% of what it is supplied with. The "
                    "pump has a second supply, which is the point."},
            {"text": "Yes, but slightly, so the figures are probably a "
                     "measurement error",
             "correct": False,
             "why": "The figures are right and repeatable. A heat pump "
                    "really does deliver more than it is wired for."},
        ],
        "figure": None,
    },
    {
        "id": "p1-03-h17",
        "band": "harder",
        "text": "Two students disagree: A says a closed system's total can "
                "never change, B says it can if energy enters. Who is right?",
        "options": [
            {"text": "A only, because a closed system's boundary can always be "
                     "redrawn",
             "correct": False,
             "why": "Widening the boundary is how you MAKE a system closed. "
                    "It does not make B wrong about an open one."},
            {"text": "Both — a system that energy enters is not closed",
             "correct": True},
            {"text": "B only, because no real system is ever completely closed",
             "correct": False,
             "why": "Real systems leak, which does not make A's statement "
                    "about a closed one false."},
            {"text": "Neither, because a total changes slowly in any system",
             "correct": False,
             "why": "Time changes nothing. A closed system's total is fixed "
                    "for a second or for a century."},
        ],
        "figure": None,
    },
    {
        "id": "p1-03-h18",
        "band": "harder",
        "text": "Why is “the energy went to heat” not a complete "
                "account of where a machine's energy ended up?",
        "options": [
            {"text": "Because heat cannot be measured, so the claim cannot be "
                     "checked",
             "correct": False,
             "why": "A thermometer checks it easily. The trouble is what the "
                    "word names, not whether it can be measured."},
            {"text": "Because no machine is actually able to produce any heat",
             "correct": False,
             "why": "Machines fill thermal stores constantly. The objection "
                    "is to the wording, not to the physics."},
            {"text": "Because heat names a pathway, and the store it filled "
                     "still has to be named",
             "correct": True},
            {"text": "Because only the useful share has to be accounted for",
             "correct": False,
             "why": "Every joule has to be accounted for. Usefulness does "
                    "not decide what counts."},
        ],
        "figure": None,
    },
    {
        "id": "p1-03-h19",
        "band": "harder",
        "text": "A student measures 620 J into a well-oiled pulley and 618 J "
                "out, and says the law is “nearly” obeyed. What "
                "is wrong with “nearly”?",
        "options": [
            {"text": "Nothing at all — the law is only ever approximately "
                     "true for any real machine",
             "correct": False,
             "why": "It is exact. No careful experiment has ever found it "
                    "approximate."},
            {"text": "The law is exact, so the missing 2 J is somewhere "
                     "rather than absent",
             "correct": True},
            {"text": "The measurement is too precise to trust in a school",
             "correct": False,
             "why": "The precision is not the issue. Even a rough "
                    "measurement leaves the 2 J needing a home."},
            {"text": "The 2 J was created by the pulley and should not be "
                     "there",
             "correct": False,
             "why": "Nothing was created. The input was the larger of the "
                    "two, which is the other way round."},
        ],
        "figure": None,
    },
    {
        "id": "p1-03-h20",
        "band": "harder",
        "text": "If a pendulum is always losing energy to the air, how can a "
                "pendulum clock keep good time for hours?",
        "options": [
            {"text": "Because the leak changes the height of the swing and "
                     "not the time each swing takes",
             "correct": True},
            {"text": "Because a pendulum is the only system anywhere in which "
                     "no energy at all leaks",
             "correct": False,
             "why": "Energy leaks from every pendulum. That is why a clock "
                    "needs winding or a weight."},
            {"text": "Because the clock's spring keeps creating the energy "
                     "the swing is losing",
             "correct": False,
             "why": "A spring creates nothing. It gives back what was put "
                    "into it when the clock was wound."},
            {"text": "Because the leak is so slow that nothing measurable "
                     "leaves in a few hours",
             "correct": False,
             "why": "It is fast enough to stop an unwound clock overnight, "
                    "which is why clocks are wound."},
        ],
        "figure": None,
    },
    {
        "id": "p1-03-h21",
        "band": "harder",
        "text": "Two identical toy cars run down the same slope, but one "
                "drives a small generator that lights a lamp. Compare their "
                "speeds at the bottom.",
        "options": [
            {"text": "Both arrive at the same speed from the same slope",
             "correct": False,
             "why": "They start with the same amount, but one of them spends "
                    "part of it on the lamp before the bottom."},
            {"text": "The one with the generator is slower",
             "correct": True},
            {"text": "The one with the generator is faster, because the lamp "
                     "adds energy",
             "correct": False,
             "why": "A lamp takes energy and gives none back. It can only "
                    "slow the car down."},
            {"text": "Neither speed can be predicted without knowing each "
                     "car's mass",
             "correct": False,
             "why": "The cars are identical, so mass is the same for both "
                    "and cannot explain any difference."},
        ],
        "figure": None,
    },
    {
        "id": "p1-03-h22",
        "band": "harder",
        "text": "Why is a running total of every store a better test of the "
                "law than simply watching a pendulum swing?",
        "options": [
            {"text": "Because a pendulum moves far too quickly for anybody to "
                     "watch it accurately by eye",
             "correct": False,
             "why": "A slow pendulum is easy to watch. Watching still misses "
                    "the store that matters."},
            {"text": "Because a calculated total is always more accurate",
             "correct": False,
             "why": "A total is only as good as the stores counted in it. "
                    "Accuracy is not the point."},
            {"text": "Because it counts the store you would never have "
                     "thought to look at",
             "correct": True},
            {"text": "Because a running total removes the friction that spoils "
                     "it",
             "correct": False,
             "why": "Counting something does not remove it. The friction is "
                    "still there, and now it is visible."},
        ],
        "figure": None,
    },
    {
        "id": "p1-03-h23",
        "band": "harder",
        "text": "A student writes: “the energy was transferred to the "
                "surroundings, so it is gone.” Which half is wrong?",
        "options": [
            {"text": "The first half — energy is never transferred to the "
                     "surroundings at all",
             "correct": False,
             "why": "It is transferred there constantly. That half of the "
                    "sentence is exactly right."},
            {"text": "Both halves — energy neither transfers anywhere nor goes "
                     "anywhere",
             "correct": False,
             "why": "Energy moves between stores all the time. The first "
                    "half describes that correctly."},
            {"text": "Neither half — transferring energy away is what losing "
                     "means",
             "correct": False,
             "why": "Losing suggests it stopped existing. Arriving in the "
                    "surroundings is the opposite of that."},
            {"text": "The second — transferred somewhere is the opposite of "
                     "gone",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p1-03-h24",
        "band": "harder",
        "text": "A scientist finds a shortfall in an energy sum. Which two "
                "ordinary explanations have to be ruled out before claiming "
                "a discovery?",
        "options": [
            {"text": "A store that was missed, and a measurement that was "
                     "wrong",
             "correct": True},
            {"text": "A store counted twice over, and a machine that was too "
                     "efficient",
             "correct": False,
             "why": "Double-counting would give a surplus, not a shortfall, "
                    "and efficiency changes no total."},
            {"text": "A closed system, and a change too quick to see",
             "correct": False,
             "why": "A closed system is what makes the sum checkable, and "
                    "speed does not hide energy."},
            {"text": "A total written down too large, and an experiment done "
                     "only once",
             "correct": False,
             "why": "The second is only worth checking; the first is just "
                    "one kind of measurement error."},
        ],
        "figure": None,
    },
    {
        "id": "p1-03-h25",
        "band": "harder",
        "text": "A bungee jumper is momentarily still at the very lowest "
                "point of the fall. Which stores hold the energy then?",
        "options": [
            {"text": "Mostly the cord's elastic store, with a little already "
                     "in thermal stores",
             "correct": True},
            {"text": "Entirely the jumper's kinetic store, which is largest "
                     "here",
             "correct": False,
             "why": "The jumper is momentarily still, so the kinetic store "
                    "is empty at that exact instant."},
            {"text": "None of them, because a jumper who is still holds no "
                     "energy",
             "correct": False,
             "why": "Being still empties one store. The cord is stretched "
                    "tight and is holding nearly all of it."},
            {"text": "Entirely the gravitational store, because the jumper "
                     "could still fall a long way",
             "correct": False,
             "why": "Most of that store emptied during the fall. What is "
                    "left is in the stretched cord."},
        ],
        "figure": None,
    },
    {
        "id": "p1-03-h26",
        "band": "harder",
        "text": "A student says the Sun proves energy can be created, because "
                "it has shone for billions of years. Reply.",
        "options": [
            {"text": "The Sun is the one exception to the law ever recorded",
             "correct": False,
             "why": "No exception has been found. The Sun's output is "
                    "accounted for by its own enormous store."},
            {"text": "The Sun creates energy, but so slowly that the law still "
                     "holds",
             "correct": False,
             "why": "It creates none, and the law is exact rather than "
                    "good enough."},
            {"text": "It is emptying an enormous store, not making energy",
             "correct": True},
            {"text": "The Sun is not a closed system, so the law does not "
                     "apply to it",
             "correct": False,
             "why": "Draw the boundary round the Sun and the space it lights "
                    "and it is closed. The law applies."},
        ],
        "figure": None,
    },
    {
        "id": "p1-03-h27",
        "band": "harder",
        "text": "Why do people find it easier to believe energy is destroyed "
                "than to believe it is conserved?",
        "options": [
            {"text": "Because conservation is a difficult idea few scientists "
                     "accept",
             "correct": False,
             "why": "It is the most tested claim in physics and is not in "
                    "dispute among scientists at all."},
            {"text": "Because energy really is destroyed in everyday "
                     "situations",
             "correct": False,
             "why": "It is destroyed in none of them. It simply ends up "
                    "somewhere nobody looks."},
            {"text": "Because the law was discovered recently and barely "
                     "checked",
             "correct": False,
             "why": "It is two hundred years old and has been checked more "
                    "than any other claim in physics."},
            {"text": "Because the stores it ends up in are invisible",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p1-03-h28",
        "band": "harder",
        "text": "Which observation would count as genuine evidence AGAINST "
                "conservation of energy?",
        "options": [
            {"text": "A sealed, insulated system whose total rose with "
                     "nothing entering it",
             "correct": True},
            {"text": "A machine that reliably gives out rather less energy "
                     "than it has been supplied with",
             "correct": False,
             "why": "That is what every machine does. The rest is in thermal "
                    "stores, not missing."},
            {"text": "A pendulum that stops swinging altogether after a few "
                     "hundred swings of the bob",
             "correct": False,
             "why": "Every real pendulum does that, and the law explains it "
                    "rather than being troubled by it."},
            {"text": "A room that becomes warmer while a motor runs inside it",
             "correct": False,
             "why": "The warmth came from the motor's supply. That is "
                    "conservation working, not failing."},
        ],
        "figure": None,
    },
    {
        "id": "p1-03-h29",
        "band": "harder",
        "text": "Why does the law say “in a closed system” "
                "rather than simply “always”?",
        "options": [
            {"text": "Because the law was only ever tested in sealed "
                     "containers",
             "correct": False,
             "why": "It is tested everywhere. The phrase is about "
                    "bookkeeping, not about apparatus."},
            {"text": "Because energy can cross a boundary, so a count only "
                     "holds if nothing does",
             "correct": True},
            {"text": "Because energy can be destroyed once it leaves a closed "
                     "system",
             "correct": False,
             "why": "It is not destroyed outside either. It is simply no "
                    "longer inside your count."},
            {"text": "Because only a closed system has stores that can be "
                     "counted",
             "correct": False,
             "why": "Any system has countable stores. Closing it is what "
                    "makes the total stay put."},
        ],
        "figure": None,
    },
    {
        "id": "p1-03-h30",
        "band": "harder",
        "text": "You want to check whether a toy car's energy is conserved as "
                "it rolls down a ramp and stops. Which set of measurements "
                "is enough?",
        "options": [
            {"text": "The car's speed at the top and bottom, and the "
                     "temperature of the track",
             "correct": True},
            {"text": "The car's speed at the top and at the bottom of the "
                     "ramp, and nothing else besides",
             "correct": False,
             "why": "That shows the kinetic store changing but never says "
                    "where the difference went."},
            {"text": "The mass of the car and the length of the ramp",
             "correct": False,
             "why": "Neither changes during the run, so neither can show "
                    "energy moving anywhere."},
            {"text": "The time taken to reach the bottom of the ramp, and "
                     "the height the ramp was set at",
             "correct": False,
             "why": "Those describe the journey. Nothing in them follows the "
                    "energy after the car stops."},
        ],
        "figure": None,
    },
]
