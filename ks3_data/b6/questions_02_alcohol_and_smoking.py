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
                     "and judgement worsen.", "correct": True},
            {"text": "It lowers the person's mood and energy, which is what "
                     "the word depressant means.", "correct": False,
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
                     "dependence gets worse instead of better.", "correct": False,
             "why": "A filter does not take out the nicotine and the "
                    "dependence is unchanged. What it changes is the taste and "
                    "the number in the test."},
            {"text": "It removes some tar, none of the carbon monoxide, and "
                     "smoother smoke goes deeper.", "correct": True},
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

    # ── MRB-335 top-up ──────────────────────────────────────────────────
    #
    # Thirty-nine rows across the lesson's own distinct material: the unit as
    # a measure and the drinks table that uses it, the liver's rate and where
    # that rate comes from, the six interventions one at a time rather than
    # six times over, each of the four rows on each long-term card, the three
    # separate harms in smoke with their three separate mechanisms, the
    # filter's ventilation holes, and the seven clauses of the vape
    # paragraph. Nothing states a dose, a threshold or a method; the
    # arithmetic rows are clearance in HOURS and drinks in UNITS, both of
    # which the lesson supplies.

    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "b6-02-e05",
        "band": "easier",
        "text": "Alcoholic drinks are measured in units. What is a unit for?",
        "options": [
            {"text": "It is the number of drinks a person is allowed to have "
                     "in a single evening.", "correct": False,
             "why": "A unit is not a permission or a limit. It is a measure of "
                    "how much alcohol a drink contains."},
            {"text": "It is the number of hours a drink will affect you for.", "correct": False,
             "why": "The hours follow from the units, at about one unit an "
                    "hour, but they are not the same thing. A unit measures "
                    "the alcohol in the glass."},
            {"text": "It measures the alcohol a drink holds, so drinks can be "
                     "compared.", "correct": True},
            {"text": "It measures how strong a drink is, whatever the size of "
                     "the glass it happens to come in.", "correct": False,
             "why": "Strength alone would not tell you enough — a small strong "
                    "drink and a large weak one can hold the same alcohol. "
                    "Units take the size and the strength together."},
        ],
        "figure": None,
    },
    {
        "id": "b6-02-e06",
        "band": "easier",
        "text": "Which substance in tobacco smoke binds to haemoglobin in "
                "place of oxygen and holds on?",
        "options": [
            {"text": "Carbon monoxide.", "correct": True},
            {"text": "Nicotine.", "correct": False,
             "why": "Nicotine acts on the brain's reward pathways and on the "
                    "heart and vessels. It is not what takes oxygen's place in "
                    "the blood."},
            {"text": "Tar.", "correct": False,
             "why": "Tar is the sticky mixture that damages the airways and "
                    "the alveoli. It does not travel in the red blood cells."},
            {"text": "Oxygen itself, once it has been heated by the smoke.",
             "correct": False,
             "why": "Heating does not change what oxygen is. The gas that "
                    "takes oxygen's places in haemoglobin is carbon "
                    "monoxide."},
        ],
        "figure": None,
    },
    {
        "id": "b6-02-e07",
        "band": "easier",
        "text": "Which part of the body does tar in tobacco smoke damage?",
        "options": [
            {"text": "The liver, which has to break it down.",
             "correct": False,
             "why": "The liver is the organ that clears alcohol. Tar stays "
                    "where the smoke goes, and that is the airways and the "
                    "alveoli."},
            {"text": "The red blood cells, whose oxygen it takes.",
             "correct": False,
             "why": "Taking oxygen's place in the red blood cells is carbon "
                    "monoxide's doing. Tar damages the airways and the "
                    "alveoli."},
            {"text": "The brain, whose reward pathways adapt to expect it.",
             "correct": False,
             "why": "That is nicotine, and it is why stopping is hard. Tar "
                    "does its damage where the smoke passes."},
            {"text": "The airways and the alveoli.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b6-02-e08",
        "band": "easier",
        "text": "Somebody who has been drinking is put under a cold shower. "
                "What does the cold water change?",
        "options": [
            {"text": "It lowers the alcohol, because alcohol evaporates from "
                     "the skin.", "correct": False,
             "why": "The alcohol is dissolved in the blood, not sitting on the "
                    "skin. Nothing leaves through the surface."},
            {"text": "Nothing at all — the liver is not on the outside of the "
                     "body.", "correct": True},
            {"text": "It speeds the liver up, because the body works harder "
                     "when it is cold.", "correct": False,
             "why": "The liver's rate is set by how much enzyme it holds, and "
                    "shivering does not add any. The rate is unchanged."},
            {"text": "It slows the alcohol down, so the person sobers up more "
                     "gradually.", "correct": False,
             "why": "There is nothing to slow. The alcohol is broken down at "
                    "the liver's own rate, and cold water on the skin does not "
                    "reach it."},
        ],
        "figure": None,
    },
    {
        "id": "b6-02-e09",
        "band": "easier",
        "text": "A half of beer and a single shot are each counted as one "
                "unit. How many units is a can of cider?",
        "options": [
            {"text": "Half a unit, because cider is not a spirit.",
             "correct": False,
             "why": "The kind of drink is not what decides it. Size and "
                    "strength together do, and a can of cider comes to two "
                    "units."},
            {"text": "One unit, the same as a half of beer.", "correct": False,
             "why": "A can of cider holds more alcohol than a half of beer. It "
                    "counts as two units."},
            {"text": "Two units, because it holds more alcohol than a "
                     "half.", "correct": True},
            {"text": "Three units, the same as a large wine.", "correct": False,
             "why": "Three units is a large wine or a pint of strong lager. A "
                    "can of cider is two."},
        ],
        "figure": None,
    },
    {
        "id": "b6-02-e10",
        "band": "easier",
        "text": "The liver clears alcohol at about one unit an hour. What "
                "sets that rate?",
        "options": [
            {"text": "How much enzyme the liver contains.", "correct": True},
            {"text": "How much the person wants to sober up.",
             "correct": False,
             "why": "The rate does not respond to encouragement. It depends on "
                    "how much enzyme the liver holds."},
            {"text": "How much water the person drinks afterwards.",
             "correct": False,
             "why": "Water helps the dehydration, the headache and the thirst. "
                    "It does nothing to the amount of alcohol or to the "
                    "liver's rate."},
            {"text": "How strong the drinks were that the person had.",
             "correct": False,
             "why": "Strength decides how many units were drunk, which sets "
                    "how many hours are needed. The rate itself is the same "
                    "either way."},
        ],
        "figure": None,
    },
    {
        "id": "b6-02-e11",
        "band": "easier",
        "text": "What happens to a heavy drinker's brain over many years?",
        "options": [
            {"text": "Nothing lasting, because the brain is protected from "
                     "everything in the blood.", "correct": False,
             "why": "Alcohol reaches the brain easily — that is why a person "
                    "gets drunk at all. Over years, brain tissue is lost."},
            {"text": "The brain produces more of its own reward chemical, "
                     "permanently.", "correct": False,
             "why": "That describes nicotine's effect on the reward pathways. "
                    "Alcohol over years costs the brain tissue."},
            {"text": "The brain is damaged only in people who are already "
                     "unwell.", "correct": False,
             "why": "The damage runs the other way round: memory and judgement "
                    "are affected long before anyone would call the person "
                    "unwell."},
            {"text": "Tissue is lost, and memory and judgement are affected.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b6-02-e12",
        "band": "easier",
        "text": "About how long does nicotine take to reach the brain after "
                "smoke is inhaled?",
        "options": [
            {"text": "About one minute.", "correct": False,
             "why": "A minute is roughly how long blood takes to go once round "
                    "the whole body. Nicotine reaches the brain from the lungs "
                    "in about ten seconds."},
            {"text": "About ten seconds.", "correct": True},
            {"text": "About ten minutes, which is why a smoker waits for the "
                     "effect.", "correct": False,
             "why": "Ten minutes would be slower than a swallowed drug. "
                    "Nicotine crosses the alveoli walls and is at the brain in "
                    "about ten seconds."},
            {"text": "About an hour, the same as a unit of alcohol.",
             "correct": False,
             "why": "An hour is how long the liver takes to clear one unit of "
                    "alcohol, which is a different measurement altogether."},
        ],
        "figure": None,
    },
    {
        "id": "b6-02-e13",
        "band": "easier",
        "text": "A vape contains no tar and no carbon monoxide. Why not?",
        "options": [
            {"text": "Because the nicotine in it has been made in a factory "
                     "rather than grown.", "correct": False,
             "why": "Where the nicotine came from makes no difference to what "
                    "else is in the vapour. Tar and carbon monoxide are absent "
                    "because nothing is burned."},
            {"text": "Because a filter removes both of them before the vapour "
                     "is breathed in.", "correct": False,
             "why": "No filter removes carbon monoxide, in a vape or in a "
                    "cigarette. They are absent because there is no burning to "
                    "produce them."},
            {"text": "Because nothing is burned, and burning is what "
                     "produces them.", "correct": True},
            {"text": "Because both of them are removed by law before a vape "
                     "can be sold.", "correct": False,
             "why": "No law could remove them from smoke. They are simply not "
                    "produced, because a vape burns nothing."},
        ],
        "figure": None,
    },
    {
        "id": "b6-02-e14",
        "band": "easier",
        "text": "What does food in the stomach do to alcohol drunk alongside "
                "it?",
        "options": [
            {"text": "It slows the alcohol's absorption into the blood.",
             "correct": True},
            {"text": "It soaks the alcohol up, so less of it is ever "
                     "absorbed.", "correct": False,
             "why": "Nothing soaks it up. The same alcohol reaches the blood "
                    "in the end, just more slowly."},
            {"text": "It speeds the liver up, so the alcohol clears sooner.",
             "correct": False,
             "why": "Food does not reach the liver's enzymes. The rate stays "
                    "at about one unit an hour whatever was eaten."},
            {"text": "It changes the alcohol into something the body can use "
                     "as energy.", "correct": False,
             "why": "Food does not change what alcohol is. All it does is slow "
                    "down how quickly the alcohol crosses into the blood."},
        ],
        "figure": None,
    },
    {
        "id": "b6-02-e15",
        "band": "easier",
        "text": "What does nicotine do to blood vessels?",
        "options": [
            {"text": "It widens them, so blood flows more easily.",
             "correct": False,
             "why": "It does the opposite. Vessels narrow, which is why blood "
                    "pressure rises."},
            {"text": "It blocks them with tar carried in the blood.",
             "correct": False,
             "why": "Tar stays in the airways and the alveoli rather than "
                    "travelling in the blood. Nicotine narrows the vessels "
                    "themselves."},
            {"text": "It has no effect on them, because it acts only on the "
                     "brain.", "correct": False,
             "why": "The blood carries nicotine to every organ. The heart and "
                    "the vessels are among the organs it reaches."},
            {"text": "It narrows them, so blood pressure rises.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b6-02-e16",
        "band": "easier",
        "text": "Besides the liver, the brain and the gut, what else does "
                "heavy drinking over years raise the risk of?",
        "options": [
            {"text": "Only accidents, since the other effects are all short "
                     "term.", "correct": False,
             "why": "Accidents are on the list, but so are several cancers, "
                    "high blood pressure and stroke. The long-term list is "
                    "longer than the one-night one."},
            {"text": "Several cancers, high blood pressure and stroke.",
             "correct": True},
            {"text": "Lung disease, from the same damage that smoking does.",
             "correct": False,
             "why": "The airways and alveoli are damaged by tar and the other "
                    "substances in smoke, which is smoking's list rather than "
                    "alcohol's."},
            {"text": "Nothing else — the damage is limited to the organs the "
                     "drink passes through.", "correct": False,
             "why": "Alcohol goes everywhere the blood goes, so the risks are "
                    "not limited to the gut and the liver. Cancers, high blood "
                    "pressure and stroke are all raised."},
        ],
        "figure": None,
    },
    {
        "id": "b6-02-e17",
        "band": "easier",
        "text": "What does the word dependence describe?",
        "options": [
            {"text": "The moment when a drug stops having any effect at all.",
             "correct": False,
             "why": "Dependence is not the effect disappearing. It is the body "
                    "having adapted to expect the drug, so that stopping is "
                    "physically difficult."},
            {"text": "The damage a drug does to the organ it acts on.",
             "correct": False,
             "why": "Damage and dependence are different things — nicotine "
                    "causes the dependence, and tar and carbon monoxide do "
                    "most of the damage."},
            {"text": "The body having adapted to expect a drug, so that "
                     "stopping is physically difficult.", "correct": True},
            {"text": "A choice a person makes to keep taking something they "
                     "enjoy.", "correct": False,
             "why": "The adaptation is real and physical. Calling it a choice "
                    "misses what has actually changed in the brain's reward "
                    "pathways."},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "b6-02-s05",
        "band": "standard",
        "text": "Someone who has been drinking goes for a hard run, saying "
                "they will sweat the alcohol out. What have they achieved?",
        "options": [
            {"text": "They have cleared some of it, because sweat is one of "
                     "the ways alcohol leaves.", "correct": False,
             "why": "Nothing worth counting leaves through the skin. Alcohol "
                    "leaves almost entirely through the liver."},
            {"text": "They have cleared it faster, because exercise raises the "
                     "body's rate of everything.", "correct": False,
             "why": "The liver's rate is set by how much enzyme it holds, and "
                    "running does not add any. The clock is unmoved."},
            {"text": "They have slowed the clearing down, because the blood "
                     "went to the muscles instead.", "correct": False,
             "why": "The liver is not starved of blood by a run, and the rate "
                    "is unchanged in either direction — it is fixed."},
            {"text": "Nothing at all to the alcohol: the same units are still "
                     "there for the liver.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b6-02-s06",
        "band": "standard",
        "text": "Someone finishes drinking 4 units and then waits 2 hours "
                "without another drink. Roughly how much is left, and what "
                "does that mean?",
        "options": [
            {"text": "None left — two hours is long enough for an evening of "
                     "that size.", "correct": False,
             "why": "Each unit takes about its own hour, so two hours clears "
                    "about two units. Two of the four are still in the "
                    "blood."},
            {"text": "About 2 units left, so reactions and judgement are still "
                     "affected.", "correct": True},
            {"text": "About 2 units left, but they are safe to drive because "
                     "they feel fine.", "correct": False,
             "why": "Feeling fine is what slowed judgement feels like from the "
                    "inside. With units still in the blood, reactions and "
                    "judgement are still affected."},
            {"text": "About half a unit left, because clearing speeds up as "
                     "the amount falls.", "correct": False,
             "why": "The rate does not change as the amount falls. It is about "
                    "one unit an hour from the first hour to the last."},
        ],
        "figure": None,
    },
    {
        "id": "b6-02-s07",
        "band": "standard",
        "text": "A packet gives a low tar figure, measured by a machine. Why "
                "might a smoker actually receive more tar than that figure?",
        "options": [
            {"text": "Ventilation holes let the machine draw in air; fingers "
                     "and lips cover them.", "correct": True},
            {"text": "The machine measures a freshly made cigarette, and more "
                     "tar builds up inside the packet over time.", "correct": False,
             "why": "Tar is produced by burning, not stored in the packet. The "
                    "gap comes from ventilation holes that a machine leaves "
                    "open and a smoker covers."},
            {"text": "Machines measure in different units from those used for "
                     "people.", "correct": False,
             "why": "The units are the same. What differs is how the "
                    "cigarette is held, because covered ventilation holes "
                    "change what is drawn through."},
            {"text": "The figure printed is for a single cigarette, and "
                     "smokers very rarely stop at just one.", "correct": False,
             "why": "That is true of any per-cigarette figure and is not the "
                    "fault here. Even for one cigarette, covered ventilation "
                    "holes mean more tar than the machine recorded."},
        ],
        "figure": None,
    },
    {
        "id": "b6-02-s08",
        "band": "standard",
        "text": "The long-term harms of alcohol include accidents and "
                "injuries, which are not diseases. Why are they on the list?",
        "options": [
            {"text": "Because people who drink heavily tend to be careless by "
                     "nature.", "correct": False,
             "why": "This is not a claim about the sort of person somebody is. "
                    "Alcohol slows the nervous system, and judgement is the "
                    "first thing to go."},
            {"text": "Because injuries take longer to heal when someone has "
                     "been drinking.", "correct": False,
             "why": "Healing is not the reason they are counted. They are "
                    "counted because a slowed nervous system leads to the "
                    "injuries happening in the first place."},
            {"text": "Because judgement goes first, so people do things they "
                     "otherwise would not.", "correct": True},
            {"text": "Because alcohol makes the bones and muscles weaker over "
                     "time.", "correct": False,
             "why": "Weakened bones are not one of alcohol's long-term "
                    "effects. Accidents are on the list because impaired "
                    "judgement and coordination cause them."},
        ],
        "figure": None,
    },
    {
        "id": "b6-02-s09",
        "band": "standard",
        "text": "Why can nobody yet say what vaping does to a person over "
                "forty years?",
        "options": [
            {"text": "Because vapour cannot be studied in a laboratory the way "
                     "smoke can.", "correct": False,
             "why": "It can be, and it is. What is missing is time, not a way "
                    "of measuring."},
            {"text": "Because the companies that make them refuse to allow any "
                     "research.", "correct": False,
             "why": "Research is being done. The gap is that the devices are "
                    "too new for anyone to have used one for forty years."},
            {"text": "Because vapes contain nothing that could do harm over "
                     "that length of time.", "correct": False,
             "why": "That is the very claim nobody can yet make. Not knowing a "
                    "harm and knowing there is none are different states."},
            {"text": "Because the devices are too new — the long-term studies "
                     "do not exist yet.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b6-02-s10",
        "band": "standard",
        "text": "A heavy drinker says they would know if drinking were "
                "harming them, because they feel perfectly well. Is that "
                "reasoning sound?",
        "options": [
            {"text": "They are right — the body gives clear warnings long "
                     "before any damage is done.", "correct": False,
             "why": "There is no such warning. Memory and judgement are "
                    "affected long before anyone would call the person "
                    "unwell."},
            {"text": "Memory and judgement are affected long before anyone "
                     "would call the person unwell.", "correct": True},
            {"text": "They are right for the brain, though not for the "
                     "liver.", "correct": False,
             "why": "The brain is one of the organs where damage runs ahead of "
                    "symptoms, not an exception to it."},
            {"text": "Feeling well proves the liver is still clearing the "
                     "alcohol properly.", "correct": False,
             "why": "How a person feels measures nothing about the liver. "
                    "Scarring builds without announcing itself."},
        ],
        "figure": None,
    },
    {
        "id": "b6-02-s11",
        "band": "standard",
        "text": "Why is alcohol measured in units rather than in glasses or "
                "cans?",
        "options": [
            {"text": "Because glasses and cans differ in size and strength, so "
                     "units let them be compared.", "correct": True},
            {"text": "Because a unit is the amount the liver clears in an "
                     "hour, so glasses would be too big.", "correct": False,
             "why": "The liver's rate is measured in units because units "
                    "already existed as a measure, not the other way round. "
                    "Units exist so that different drinks can be compared."},
            {"text": "Because units describe how drunk a person will feel "
                     "rather than what they drank.", "correct": False,
             "why": "A unit is a measure of the alcohol in the glass, not of "
                    "how anyone feels. Two people drinking the same units have "
                    "drunk the same alcohol."},
            {"text": "Because a unit is the same for everybody, while a glass "
                     "affects everybody differently.", "correct": False,
             "why": "The measurement is of the drink, not of the person. Units "
                    "exist because drinks differ in size and strength."},
        ],
        "figure": None,
    },
    {
        "id": "b6-02-s12",
        "band": "standard",
        "text": "Someone drinks heavily but has been told their liver is "
                "healthy, and concludes that alcohol is doing them no harm. "
                "Where is that wrong?",
        "options": [
            {"text": "A liver test cannot detect scarring, so the result tells "
                     "them nothing at all.", "correct": False,
             "why": "Liver damage can be looked for. The fault in the "
                    "reasoning is that the liver is only one of the organs "
                    "alcohol reaches."},
            {"text": "The liver damage will always come first, so it is only a "
                     "matter of waiting.", "correct": False,
             "why": "There is no fixed order. Brain, gut and whole-body risks "
                    "do not wait for the liver's turn."},
            {"text": "The brain, the gut and the whole-body risks are not "
                     "measured by a liver test.", "correct": True},
            {"text": "Only the liver is at risk, because it is the organ "
                     "that clears the alcohol.", "correct": False,
             "why": "It clears the alcohol, but it is not the only organ the "
                    "blood carried it to. Brain tissue, the gut lining and the "
                    "whole-body risks are all affected."},
        ],
        "figure": None,
    },
    {
        "id": "b6-02-s13",
        "band": "standard",
        "text": "A pupil says smoking is a lung problem, so somebody with "
                "clear lungs has nothing to worry about. What has that left "
                "out?",
        "options": [
            {"text": "Only the throat and the mouth, which the smoke also "
                     "passes through on its way.", "correct": False,
             "why": "Those are affected too, but the far bigger gap is the "
                    "blood and the heart. Carbon monoxide acts in the blood "
                    "and nicotine on the heart and vessels."},
            {"text": "That the lungs recover fully as soon as somebody "
                     "stops.", "correct": False,
             "why": "Whether the lungs recover is a separate question. What "
                    "the claim leaves out is the blood, the heart and the "
                    "vessels."},
            {"text": "That the damage takes many years to build up, so a "
                     "young smoker has nothing to fear yet.", "correct": False,
             "why": "There is no threshold below which smoke stops damaging "
                    "tissue. And the claim's real gap is that smoke harms far "
                    "more than the lungs."},
            {"text": "The blood and the heart: vessels narrow, pressure "
                     "rises, clots form.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b6-02-s14",
        "band": "standard",
        "text": "Why do people who drink heavily over years often bleed and "
                "vomit?",
        "options": [
            {"text": "Because alcohol thins the blood until it leaks out of "
                     "the vessels.", "correct": False,
             "why": "Alcohol does not thin blood out of its vessels. The gut "
                    "symptoms come from the gut itself, whose lining is "
                    "irritated and inflamed."},
            {"text": "Because the lining of the stomach and gut is irritated "
                     "and inflamed.", "correct": True},
            {"text": "Because the brain's control of swallowing has been "
                     "damaged.", "correct": False,
             "why": "Brain tissue is lost over years, and memory and judgement "
                    "suffer, but the bleeding and vomiting come from the "
                    "inflamed gut lining."},
            {"text": "Because the kidneys pass the alcohol back into the "
                     "stomach.", "correct": False,
             "why": "The kidneys pass water out as urine and send nothing back "
                    "to the stomach. The stomach is damaged by the drink it "
                    "held."},
        ],
        "figure": None,
    },
    {
        "id": "b6-02-s15",
        "band": "standard",
        "text": "Tobacco smoke does three separate kinds of harm. Which "
                "pairing of substance and harm is right?",
        "options": [
            {"text": "Nicotine causes the dependence; carbon monoxide cuts the "
                     "oxygen carried; tar damages the airways.",
             "correct": True},
            {"text": "Nicotine damages the airways; tar cuts the oxygen "
                     "carried; carbon monoxide causes the dependence.",
             "correct": False,
             "why": "All three are swapped. Nicotine works on the brain's "
                    "reward pathways, carbon monoxide occupies oxygen's places "
                    "in the blood, and tar damages the airways."},
            {"text": "Tar causes the dependence; nicotine cuts the oxygen "
                     "carried; carbon monoxide damages the airways.",
             "correct": False,
             "why": "Nothing comes to depend on tar, and nicotine does not "
                    "touch haemoglobin. The dependence is nicotine's and the "
                    "oxygen problem is carbon monoxide's."},
            {"text": "Carbon monoxide causes the dependence; nicotine damages "
                     "the airways; tar cuts the oxygen carried.",
             "correct": False,
             "why": "Carbon monoxide binds to haemoglobin rather than creating "
                    "a dependence, and the airway damage is tar's rather than "
                    "nicotine's."},
        ],
        "figure": None,
    },
    {
        "id": "b6-02-s16",
        "band": "standard",
        "text": "Someone says beer must be safer than spirits, because beer "
                "is weaker. What does the unit tell you?",
        "options": [
            {"text": "They are right — a weaker drink always holds less "
                     "alcohol.", "correct": False,
             "why": "Strength is only half of it. A pint of strong lager comes "
                    "to three units and a single shot to one."},
            {"text": "They are right for the liver, though not for the "
                     "brain.", "correct": False,
             "why": "The liver and the brain both deal with the same alcohol. "
                    "What matters is how many units were drunk, not what they "
                    "arrived in."},
            {"text": "Units count the alcohol however it arrives: strong "
                     "lager is three units a pint.", "correct": True},
            {"text": "Beer is cleared faster because there is more liquid to "
                     "dilute it.", "correct": False,
             "why": "You cannot dilute your way out of a fixed amount, and the "
                    "liver's rate does not change. The units decide the "
                    "hours."},
        ],
        "figure": None,
    },
    {
        "id": "b6-02-s17",
        "band": "standard",
        "text": "A shop sells a vape to a 16-year-old and says that is "
                "allowed, because a vape is not tobacco. Is that right?",
        "options": [
            {"text": "No: selling a vape or a cigarette to an under-18 is "
                     "illegal in the UK.", "correct": True},
            {"text": "Yes, because the rules were written for tobacco before "
                     "vapes existed.", "correct": False,
             "why": "The law covers both. Selling either to an under-18 is "
                    "illegal in the UK."},
            {"text": "Yes, because a vape delivers no nicotine at all and so "
                     "cannot cause any dependence.", "correct": False,
             "why": "A vape does deliver nicotine, often faster and in larger "
                    "amounts than a cigarette, so the dependence is the same "
                    "or stronger."},
            {"text": "No, but only because this particular vape happened to "
                     "contain tobacco.", "correct": False,
             "why": "Nothing turns on what is inside it. The age limit applies "
                    "to vapes and cigarettes alike."},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "b6-02-h05",
        "band": "harder",
        "text": "Someone finishes 8 units at 2 am and plans to drive at 8 am. "
                "Using the clearance rate, what is their position at 8 am?",
        "options": [
            {"text": "Clear — six hours of sleep is enough for any evening.",
             "correct": False,
             "why": "Sleep passes time and nothing else. Six hours clears "
                    "about six units, and eight were drunk."},
            {"text": "Clear, because the liver works faster overnight when "
                     "nothing else is being digested.", "correct": False,
             "why": "The rate is the same whether the person is asleep, awake "
                    "or in a hurry. It is set by the liver's enzymes, not by "
                    "the time of day."},
            {"text": "About 2 units still in the blood: not clear until "
                     "about 10 am.", "correct": True},
            {"text": "About 4 units still in the blood, because clearing slows "
                     "down during sleep.", "correct": False,
             "why": "Clearing does not slow during sleep. Six hours at about a "
                    "unit an hour leaves two of the eight units, not four."},
        ],
        "figure": None,
    },
    {
        "id": "b6-02-h06",
        "band": "harder",
        "text": "Carbon monoxide binds to haemoglobin and holds on. Why does "
                "that matter more than simply breathing in slightly less "
                "oxygen for a moment?",
        "options": [
            {"text": "Those places stay occupied, so the blood carries less "
                     "oxygen even in clean air.", "correct": True},
            {"text": "Because carbon monoxide is poisonous to the lungs, which "
                     "then take in less oxygen.", "correct": False,
             "why": "The problem is in the blood rather than the lungs. Lungs "
                    "that work perfectly still deliver less oxygen if the "
                    "haemoglobin is occupied."},
            {"text": "Because carbon monoxide destroys red blood cells, so "
                     "there are fewer of them.", "correct": False,
             "why": "The cells are not destroyed. Their haemoglobin is "
                    "occupied by a gas that will not let go quickly, which is "
                    "a different problem."},
            {"text": "Because it makes a person breathe more slowly, so less "
                     "air is taken in.", "correct": False,
             "why": "Breathing is not what is limited. The oxygen arrives at "
                    "the lungs and finds the places it would occupy already "
                    "taken."},
        ],
        "figure": None,
    },
    {
        "id": "b6-02-h07",
        "band": "harder",
        "text": "Someone who has never smoked takes up vaping and says they "
                "are better off than a smoker would be. What is the honest "
                "scientific reply?",
        "options": [
            {"text": "They are right, and should be encouraged, since vaping "
                     "is known to be safe.", "correct": False,
             "why": "Vapes are very likely less harmful than cigarettes and "
                    "are not known to be safe — the long-term studies do not "
                    "exist yet."},
            {"text": "They are wrong: vaping is more harmful than smoking.", "correct": False,
             "why": "Overstating the harm is as inaccurate as understating it. "
                    "The evidence points to vapes being less harmful than "
                    "cigarettes."},
            {"text": "They are wrong, because a vape delivers the same tar "
                     "and carbon monoxide as a cigarette.", "correct": False,
             "why": "It delivers neither, because nothing is burned. The "
                    "problem with the comparison is elsewhere."},
            {"text": "The comparison is wrong: a never-smoker only gains a "
                     "dependence.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b6-02-h08",
        "band": "harder",
        "text": "Why is one unit an hour described as a model rather than as a "
                "law that holds for everybody?",
        "options": [
            {"text": "Because the rate rises through an evening as the liver "
                     "warms to the work.", "correct": False,
             "why": "The rate does not rise as an evening goes on. It is "
                    "steady, and the model rounds real people to a single "
                    "figure."},
            {"text": "Real clearance varies between people, and a damaged "
                     "liver runs slower still.", "correct": True},
            {"text": "Because the figure was chosen to make the arithmetic "
                     "easy and has no basis at all.", "correct": False,
             "why": "It is close to what livers actually do, which is why it "
                    "is useful. What it hides is the variation between one "
                    "person and another."},
            {"text": "Because a person can change their own rate by drinking "
                     "regularly.", "correct": False,
             "why": "Regular heavy drinking scars the liver, which makes "
                    "clearance slower rather than faster. Nobody trains "
                    "themselves into a quicker one."},
        ],
        "figure": None,
    },
    {
        "id": "b6-02-h09",
        "band": "harder",
        "text": "Heavy drinking and smoking both raise the risk of a stroke, "
                "by different routes. Which pair of routes is right?",
        "options": [
            {"text": "Both by scarring the liver, so it cannot clean the "
                     "blood.", "correct": False,
             "why": "Smoke does not scar the liver, and a scarred liver is not "
                    "how either of them raises stroke risk."},
            {"text": "Alcohol by damaging the brain tissue directly; smoke by "
                     "removing the oxygen that the brain needs.", "correct": False,
             "why": "Both of those are real harms, but neither is the route to "
                    "a stroke. Raised blood pressure and clots forming more "
                    "readily are."},
            {"text": "Alcohol by raised blood pressure; smoke by narrowed "
                     "vessels and clots.", "correct": True},
            {"text": "Alcohol through dehydration, and smoke through the tar "
                     "that it carries into the blood.", "correct": False,
             "why": "Dehydration passes with a drink of water, and tar stays "
                    "in the airways. The stroke risk comes from blood pressure "
                    "and from vessels and clotting."},
        ],
        "figure": None,
    },
    {
        "id": "b6-02-h10",
        "band": "harder",
        "text": "Alcohol affects judgement on a single night and also over "
                "many years. What is the difference between the two?",
        "options": [
            {"text": "One passes as the liver clears it; the other is brain "
                     "tissue lost.",
             "correct": True},
            {"text": "There is no difference — the long-term effect is simply "
                     "many short-term ones.", "correct": False,
             "why": "One passes when the blood is clear. The other is brain "
                    "tissue that has been lost, and it does not return with "
                    "the morning."},
            {"text": "Only the long-term effect is real; the night's is not.", "correct": False,
             "why": "Both are real. On the night, signals between nerve cells "
                    "genuinely pass less readily; over years, tissue is "
                    "genuinely lost."},
            {"text": "The long-term effect only appears once a doctor has "
                     "told somebody that they are unwell.", "correct": False,
             "why": "It runs the other way round. Memory and judgement are "
                    "affected long before anyone would call the person "
                    "unwell."},
        ],
        "figure": None,
    },
    {
        "id": "b6-02-h11",
        "band": "harder",
        "text": "A nicotine patch delivers nicotine through the skin and no "
                "smoke at all. Using the three harms, what does a patch change "
                "and what does it not?",
        "options": [
            {"text": "It changes nothing at all, because nicotine is the "
                     "substance that causes the disease.", "correct": False,
             "why": "Nicotine causes the dependence, not the disease. The "
                    "damage comes from tar, carbon monoxide and the other "
                    "substances in smoke."},
            {"text": "It removes the dependence but leaves the tar and carbon "
                     "monoxide behind.", "correct": False,
             "why": "It is the other way round. A patch carries no smoke at "
                    "all, so no tar and no carbon monoxide, and the nicotine "
                    "is exactly what it does deliver."},
            {"text": "It removes everything, because nicotine on the skin "
                     "cannot reach the blood.", "correct": False,
             "why": "It reaches the blood — that is the point of a patch. What "
                    "it leaves behind is the tar and the carbon monoxide."},
            {"text": "No tar and no carbon monoxide, but the nicotine and the "
                     "dependence are still there.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b6-02-h12",
        "band": "harder",
        "text": "Someone can feel more affected half an hour after their last "
                "drink than they did when they put the glass down. How is that "
                "possible if the liver has been working all along?",
        "options": [
            {"text": "The liver stops working once a person stops drinking, so "
                     "the alcohol builds up.", "correct": False,
             "why": "The liver works steadily whether or not anyone is still "
                    "drinking. The rise comes from alcohol still crossing into "
                    "the blood."},
            {"text": "Alcohol is still crossing in from the stomach, so the "
                     "level rises.",
             "correct": True},
            {"text": "The alcohol has only reached the brain by then, having "
                     "taken a full half hour to travel there.", "correct": False,
             "why": "The blood goes once round the body in under a minute, so "
                    "the brain was reached long before. What is still "
                    "happening is absorption."},
            {"text": "The person has become dehydrated, and it is dehydration "
                     "that causes the impairment.", "correct": False,
             "why": "Dehydration causes the thirst and the headache. The "
                    "impairment is the alcohol acting on the nervous system, "
                    "and more of it is still arriving."},
        ],
        "figure": None,
    },
    {
        "id": "b6-02-h13",
        "band": "harder",
        "text": "One evening is two cans of cider. Another is a large wine and "
                "a half of beer. Which evening puts more alcohol into the "
                "blood?",
        "options": [
            {"text": "The two cans of cider, because a can is bigger than a "
                     "glass.", "correct": False,
             "why": "The size of the container is not the measure. Two cans of "
                    "cider is 2 + 2 = 4 units, and the wine and beer come to "
                    "3 + 1 = 4 as well."},
            {"text": "The wine and beer, because wine is the stronger "
                     "drink.", "correct": False,
             "why": "Strength alone does not settle it either. Both evenings "
                    "come to 4 units, so both hold the same alcohol."},
            {"text": "Neither — both come to 4 units, so both take about four "
                     "hours to clear.", "correct": True},
            {"text": "The wine and beer, because two different drinks are "
                     "harder for the liver than one.", "correct": False,
             "why": "The liver deals with alcohol, not with the labels on the "
                    "bottles. Four units is four units however it arrived."},
        ],
        "figure": None,
    },
    {
        "id": "b6-02-h14",
        "band": "harder",
        "text": "A big meal eaten before drinking is the one popular trick "
                "that does something real. What does it change, and what does "
                "it leave alone?",
        "options": [
            {"text": "It lowers the peak in the blood, but the number of hours "
                     "to clear is unchanged.", "correct": True},
            {"text": "It lowers the number of hours, because there is less "
                     "alcohol left to break down.", "correct": False,
             "why": "None of the alcohol is lost — it arrives more slowly. The "
                    "same units still have to be broken down at the same "
                    "rate."},
            {"text": "It raises the peak but shortens the evening, so the two "
                     "cancel out.", "correct": False,
             "why": "Food lowers the peak rather than raising it, by slowing "
                    "absorption. And the hours do not shorten at all."},
            {"text": "It changes neither, and the belief that it helps is "
                     "entirely mistaken.", "correct": False,
             "why": "It does something real: the peak is lower, so the person "
                    "is less impaired at their worst. What it does not change "
                    "is the clock."},
        ],
        "figure": None,
    },
    {
        "id": "b6-02-h15",
        "band": "harder",
        "text": "A medicine can have an amount that is safe to take, yet "
                "there is no safe number of cigarettes. Why the difference?",
        "options": [
            {"text": "Because a medicine is tested and tobacco never really "
                     "was.", "correct": False,
             "why": "Tobacco is one of the most heavily studied substances "
                    "there is. That is how we know the risk rises from the "
                    "first cigarette."},
            {"text": "Because smoke is taken in through the lungs, and "
                     "anything inhaled must be harmful.", "correct": False,
             "why": "Inhaling is not harmful in itself — air is inhaled all "
                    "day. What matters is that smoke damages tissue with no "
                    "threshold below which it stops."},
            {"text": "Because cigarettes contain nicotine, and any amount at "
                     "all of an addictive drug is dangerous.", "correct": False,
             "why": "Nicotine causes the dependence rather than the tissue "
                    "damage. The reason there is no safe number is that the "
                    "damage from smoke starts at the first one."},
            {"text": "A medicine has a safe dose; smoke damages tissue from "
                     "the first one.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b6-02-h16",
        "band": "harder",
        "text": "Why might the dependence from a vape be the same as, or "
                "stronger than, the dependence from cigarettes?",
        "options": [
            {"text": "Because a vape contains tar, which the brain also adapts "
                     "to expect.", "correct": False,
             "why": "A vape contains no tar, because nothing is burned. And "
                    "nothing adapts to tar in any case — the dependence is "
                    "nicotine's."},
            {"text": "Because it delivers nicotine too, often faster and in "
                     "larger amounts.", "correct": True},
            {"text": "Because vapour reaches the brain by a different route "
                     "that cigarettes cannot use.", "correct": False,
             "why": "The route is the same: across the thin alveoli walls into "
                    "the blood. What differs is how quickly and how much "
                    "nicotine arrives."},
            {"text": "Because a vape cannot be put out, so a person is never "
                     "reminded to stop.", "correct": False,
             "why": "How long a device lasts is not what the dependence "
                    "rests on. It rests on the nicotine arriving fast and in "
                    "larger amounts."},
        ],
        "figure": None,
    },
    {
        "id": "b6-02-h17",
        "band": "harder",
        "text": "A newspaper headline sums smoking up as damaging your "
                "lungs. What does that sentence leave out?",
        "options": [
            {"text": "Nothing important — the lungs are where the smoke goes, "
                     "so that is where the harm is.", "correct": False,
             "why": "The smoke goes to the lungs, but two of its three harms "
                    "act elsewhere. Carbon monoxide acts in the blood and "
                    "nicotine on the brain, heart and vessels."},
            {"text": "That the damage is done by nicotine rather than by tar.",
             "correct": False,
             "why": "It is the other way round: tar and the other substances "
                    "do the airway damage, and nicotine causes the "
                    "dependence."},
            {"text": "The blood and the brain — three harms with three "
                     "mechanisms, and only one is in the lungs.",
             "correct": True},
            {"text": "That lung damage can be reversed, which makes the "
                     "headline needlessly frightening.", "correct": False,
             "why": "The airway and alveoli damage is not something that "
                    "simply reverses. What the headline misses is everything "
                    "smoke does outside the lungs."},
        ],
        "figure": None,
    },
]
