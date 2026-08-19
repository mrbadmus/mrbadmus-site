# -*- coding: utf-8 -*-
"""B6 lesson 02 — Alcohol and smoking: twelve questions (MRB-269).

The lesson makes two arguments and this bank probes both. One: alcohol is a
depressant, it leaves almost entirely through the liver, and the liver's rate
is set by how much enzyme it holds — so the bench's six interventions all give
the same number of hours, and the only one that does anything real (food)
moves the peak and not the clock. Two: tobacco smoke is three separate harms
with three separate mechanisms — nicotine for the dependence, carbon monoxide
in the blood, tar and the other substances in the airways — and a claim that
touches one of them has not touched the other two.

The distractors are built from the lesson's three declared misconceptions.
DRUG-03 ("coffee, a cold shower or fresh air will sober you up") supplies the
options that give an intervention a rate: sweat through the skin, dilution by
water, flushing through the kidneys, deep breathing as a route out, and sleep
slowing the liver. DRUG-04 ("a few cigarettes now and then is basically fine")
supplies the weekly-number options in the harder band. DRUG-08 ("filters make
cigarettes safer") supplies the filter question's three wrong readings. Four
further errors the lesson's own cards exist to correct are worked as well: that
a liver used to alcohol gets better at clearing it, that scarring heals, that
nicotine is what causes the disease, and that "less harmful than cigarettes"
and "safe" are the same claim.

No question restates a ladder rung. The rungs already own the six-units-at-
midnight clock, the two black coffees, the carbon monoxide explanation and the
energy-drink mixer, so the bank works around all four: the clock is put as a
two-drink build and as a two-person comparison, coffee appears only inside
other options, carbon monoxide is asked about as a mechanism to be separated
from nicotine's rather than as breathlessness, and the stimulant-meets-
depressant argument is left entirely to rung 4.

The filter question deliberately does not touch the lesson's ventilation-hole
clause — see the report.

`figure` is `None` throughout: the lesson declares no figures (NOTES-B6 flag
14, measured absence), and every stem here is self-contained.
"""

UNIT = "B6"
LESSON = "alcohol-and-smoking"
LESSON_NUMBER = 2

QUESTIONS = [

    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "b6-02-e01",
        "band": "easier",
        "text": "Alcohol is a depressant. What does calling it a depressant "
                "tell you?",
        "options": [
            {"text": "It slows the nervous system, so reactions, coordination "
                     "and judgement all worsen.", "correct": True},
            {"text": "It lowers the person's mood, which is what the word "
                     "depressant means.", "correct": False,
             "why": "Depressant is about nerve signals being slowed, not about "
                    "mood. It names what the drug does to the nervous system, "
                    "however the person happens to feel."},
            {"text": "It speeds the body up and raises the person's "
                     "alertness.", "correct": False,
             "why": "That is a stimulant, and nicotine and caffeine are both "
                    "stimulants. Alcohol does the opposite to nerve signals."},
            {"text": "It slows the liver down, which is why alcohol takes "
                     "hours to leave.", "correct": False,
             "why": "The liver's rate is set by how much enzyme it contains, "
                    "not by alcohol slowing it. Depressant describes the "
                    "effect on the nervous system."},
        ],
        "figure": None,
    },
    {
        "id": "b6-02-e02",
        "band": "easier",
        "text": "Almost all of the alcohol someone drinks is removed by one "
                "organ. Which one?",
        "options": [
            {"text": "The kidneys, which pass it out in the urine.",
             "correct": False,
             "why": "Only a trace leaves that way. Alcohol leaves the body "
                    "almost entirely through the liver, which breaks it "
                    "down."},
            {"text": "The skin, in sweat, which is why a cold shower is said "
                     "to help.", "correct": False,
             "why": "Nothing worth counting leaves through the skin, and cold "
                    "water does not reach the liver. The alcohol is in the "
                    "blood, where the shower cannot touch it."},
            {"text": "The liver, which breaks it down at about one unit an "
                     "hour.", "correct": True},
            {"text": "The stomach, where the drink lands in the first place.",
             "correct": False,
             "why": "The stomach is where alcohol is absorbed into the blood, "
                    "and food there slows that absorption down. The breaking "
                    "down itself happens in the liver."},
        ],
        "figure": None,
    },
    {
        "id": "b6-02-e03",
        "band": "easier",
        "text": "Which substance in tobacco smoke is the one that makes "
                "stopping hard?",
        "options": [
            {"text": "Tar, because the airways come to depend on the coating "
                     "it leaves.", "correct": False,
             "why": "Tar damages the airways and the alveoli. Nothing comes to "
                    "depend on it — the dependence is nicotine's, and it is in "
                    "the brain."},
            {"text": "Nicotine, because the brain's reward pathways adapt to "
                     "expect it.", "correct": True},
            {"text": "Carbon monoxide, because the blood gets used to carrying "
                     "less oxygen.", "correct": False,
             "why": "Carbon monoxide binds to haemoglobin in place of oxygen "
                    "and holds on. That leaves every tissue short of oxygen; "
                    "it does not create the dependence."},
            {"text": "None of them — smoking is a habit rather than a physical "
                     "dependence.", "correct": False,
             "why": "The body genuinely adapts. Nicotine reaches the brain in "
                    "about ten seconds and the reward pathways change to "
                    "expect it, which is why stopping is difficult."},
        ],
        "figure": None,
    },
    {
        "id": "b6-02-e04",
        "band": "easier",
        "text": "Over years, what does heavy drinking do to the liver itself?",
        "options": [
            {"text": "It grows larger and becomes better at clearing alcohol.",
             "correct": False,
             "why": "The opposite. Working cells are replaced by scar tissue, "
                    "and a damaged liver clears alcohol more slowly than a "
                    "healthy one, never faster."},
            {"text": "Nothing lasting — the liver repairs itself completely "
                     "once someone stops.", "correct": False,
             "why": "Early damage does recover if the drinking stops. Scarring "
                    "does not: those working cells are gone for good."},
            {"text": "The brain and the gut suffer, but the liver copes with "
                     "what it breaks down.", "correct": False,
             "why": "The brain and the gut are damaged too, but the liver is "
                    "not spared. It is the organ doing the breaking down and "
                    "it is scarred by it."},
            {"text": "Working cells are replaced by scar tissue, which does "
                     "not recover.", "correct": True},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "b6-02-s01",
        "band": "standard",
        "text": "At the bench you build an evening of a can of cider (2 units) "
                "and a pint of strong lager (3 units), then run the clock. How "
                "long until the blood is clear?",
        "options": [
            {"text": "About 3 hours — the strongest drink is the one that sets "
                     "the time.", "correct": False,
             "why": "Units add up, which is the whole point of measuring in "
                    "them. There are 5 units to break down and each one takes "
                    "about its own hour."},
            {"text": "About 5 hours — 5 units between them, at about an hour "
                     "each.", "correct": True},
            {"text": "About 5 hours, unless the person sleeps, which slows the "
                     "liver.", "correct": False,
             "why": "Sleep passes time and does nothing else. The rate is the "
                    "same whether the person is asleep, awake, worried or in a "
                    "hurry."},
            {"text": "Fewer than 5 hours, because they ate a big meal "
                     "alongside the drinks.", "correct": False,
             "why": "Food in the stomach slows absorption, so the peak in the "
                    "blood is lower. The total amount to break down has not "
                    "changed, so the hours have not changed."},
        ],
        "figure": None,
    },
    {
        "id": "b6-02-s02",
        "band": "standard",
        "text": "A breath test can measure the alcohol in someone's blood, yet "
                "breathing harder cannot clear it. How are both of those true "
                "at once?",
        "options": [
            {"text": "The machine detects the smell of the drink rather than "
                     "anything in the blood.", "correct": False,
             "why": "It measures alcohol that has crossed out of the blood "
                    "into the breath. That is why the reading tells you about "
                    "the blood and not about the last mouthful."},
            {"text": "The lungs are the main way out, so deep breathing really "
                     "does speed clearing up.", "correct": False,
             "why": "Only a trace leaves through the lungs. The rest goes "
                    "through the liver, which is exactly why breathing harder "
                    "cannot clear it."},
            {"text": "Alcohol sits on the skin and evaporates, so a cold "
                     "shower lowers the reading.", "correct": False,
             "why": "The alcohol is in the blood, not on the skin. A cold "
                    "shower gives you cold skin and a sharp intake of breath, "
                    "and changes nothing in the blood."},
            {"text": "A trace leaves in the breath — enough to measure, "
                     "nowhere near enough to clear.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b6-02-s03",
        "band": "standard",
        "text": "After a heavy evening someone drinks several pints of water "
                "before bed. What has the water done?",
        "options": [
            {"text": "Helped the dehydration, the headache and the thirst, and "
                     "nothing to the alcohol.", "correct": True},
            {"text": "Diluted the alcohol in the blood, so the person is less "
                     "affected by it.", "correct": False,
             "why": "You cannot dilute your way out of a fixed amount. The "
                    "same number of units is still there for the liver to "
                    "break down."},
            {"text": "Flushed the alcohol out through the kidneys, so it will "
                     "clear sooner.", "correct": False,
             "why": "Alcohol leaves almost entirely through the liver, at the "
                    "liver's own rate. Extra water gives the kidneys more to "
                    "pass, not the alcohol another way out."},
            {"text": "Nothing whatever — water has no effect on any part of "
                     "this.", "correct": False,
             "why": "It does something real, just not to the alcohol. The "
                    "dehydration, the headache and the thirst are genuinely "
                    "helped by it."},
        ],
        "figure": None,
    },
    {
        "id": "b6-02-s04",
        "band": "standard",
        "text": "Someone switches to a filtered brand and says the filter "
                "makes the cigarettes safer. What is wrong with that?",
        "options": [
            {"text": "Nothing is wrong — the filter takes out tar, and tar is "
                     "what does the damage.", "correct": False,
             "why": "It removes some tar, not all of it, and it does nothing "
                    "at all to the carbon monoxide. Tar is one of three harms, "
                    "not the whole list."},
            {"text": "The filter holds back the nicotine as well, so the "
                     "dependence gets worse instead.", "correct": False,
             "why": "A filter does not take out the nicotine and the "
                    "dependence is unchanged. What it changes is the taste and "
                    "the number in the test."},
            {"text": "It removes some tar, does nothing to carbon monoxide, "
                     "and smoother smoke is inhaled deeper.", "correct": True},
            {"text": "Filters were banned as soon as the link with cancer "
                     "became public knowledge.", "correct": False,
             "why": "Filters were introduced when that link became public, not "
                    "banned. They changed how the smoke feels, not how safe "
                    "the habit is."},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "b6-02-h01",
        "band": "harder",
        "text": "Someone whose liver is already scarred by years of drinking "
                "has an evening out. Next to the bench's one-unit-an-hour "
                "clock, how does their real clearance compare?",
        "options": [
            {"text": "Faster — a liver that deals with alcohol often gets "
                     "better at the job.", "correct": False,
             "why": "Scarring replaces the working cells that do the breaking "
                    "down, so there is less liver doing the job, not more. The "
                    "rate goes the other way."},
            {"text": "The same — one unit an hour is fixed, and it is the same "
                     "for every person.", "correct": False,
             "why": "One unit an hour is a teaching model. Real clearance "
                    "varies between people, and a damaged liver is exactly the "
                    "case where it runs slower."},
            {"text": "Slower — and because scarring does not recover, it stays "
                     "slower.", "correct": True},
            {"text": "Slower for now, but back to the model's rate once the "
                     "scarring heals.", "correct": False,
             "why": "Early damage recovers if the drinking stops. Scar tissue "
                    "does not, and that is the difference the long-term card "
                    "draws."},
        ],
        "figure": None,
    },
    {
        "id": "b6-02-h02",
        "band": "harder",
        "text": "A shop puts up a sign: “Vapes have no tar and no carbon "
                "monoxide — so they are safe.” Judge the sign.",
        "options": [
            {"text": "It removes two harms from the list and calls that safe; "
                     "the nicotine and the dependence stay.", "correct": True},
            {"text": "Correct as written — with no tar and no carbon monoxide "
                     "there is nothing left to do harm.", "correct": False,
             "why": "Nicotine is still delivered, often faster and in larger "
                    "amounts than a cigarette, so the dependence is the same "
                    "or stronger. The long-term studies do not exist yet."},
            {"text": "Wrong, because a vape is more harmful to a person than a "
                     "cigarette is.", "correct": False,
             "why": "The honest position is that vapes are very likely less "
                    "harmful than cigarettes. Overstating the harm is as "
                    "inaccurate as the sign that understates it."},
            {"text": "Wrong, because nothing at all is known about what vapes "
                     "do to a person.", "correct": False,
             "why": "Plenty is known: no tar, no carbon monoxide, nicotine "
                    "delivered fast. What is missing is the long-term picture, "
                    "because the devices are too new for it to exist."},
        ],
        "figure": None,
    },
    {
        "id": "b6-02-h03",
        "band": "harder",
        "text": "Two friends stop drinking at the same moment. Ade has had a "
                "large wine (3 units) with a plate of food. Kwame has had a "
                "half of beer and a single shot, and has eaten nothing all "
                "day. Whose blood is clear first?",
        "options": [
            {"text": "Ade, because the food taken with the drink speeds his "
                     "liver up.", "correct": False,
             "why": "Food slows absorption, so Ade's peak is lower. It does "
                    "not change how much there is to break down, and it does "
                    "nothing to the liver's rate."},
            {"text": "Kwame, but only by minutes, because his empty stomach "
                     "slows his clearing.", "correct": False,
             "why": "An empty stomach raises the peak; it does not change the "
                    "hours. Kwame is clear a whole hour earlier, and it is "
                    "because he drank one unit less."},
            {"text": "Both together, since the two of them stopped drinking at "
                     "the same moment.", "correct": False,
             "why": "The clock runs on units, not on when the evening ended. "
                    "Ade has 3 units to break down and Kwame has 2, so Ade "
                    "needs an hour more."},
            {"text": "Kwame, an hour before Ade — 2 units to clear against "
                     "Ade's 3.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b6-02-h04",
        "band": "harder",
        "text": "“I only smoke a few on a Saturday, so I cannot be "
                "dependent and it cannot be doing much harm.” Which reply "
                "is right?",
        "options": [
            {"text": "Right on both counts, provided the number each week "
                     "stays as low as it is.", "correct": False,
             "why": "Neither half holds. There is no number below which smoke "
                    "stops damaging tissue, and dependence is not counted by "
                    "the week."},
            {"text": "Neither holds — risk rises from the first cigarette, and "
                     "social smokers do become dependent.", "correct": True},
            {"text": "Right about the dependence, wrong about the harm — a "
                     "social smoker does not get hooked.", "correct": False,
             "why": "They do. Nicotine's grip is about how quickly it reaches "
                    "the brain — about ten seconds — rather than about how "
                    "many are smoked in a week."},
            {"text": "Wrong about the dependence, right about the harm — "
                     "nicotine is what causes the disease.", "correct": False,
             "why": "Nicotine causes the dependence, not the disease. The "
                    "damage comes from tar, from carbon monoxide and from the "
                    "other substances in the smoke."},
        ],
        "figure": None,
    },
]
