# -*- coding: utf-8 -*-
"""B6 lesson 01 — What drugs do to the body: twelve questions (MRB-269).

The lesson makes one argument twice over: a drug is any substance that changes
the way the body works, and once it is dissolved in the plasma it carries no
address, so it is offered to every organ and acts wherever it fits. Everything
here probes some part of that — the three classes and what they do to nerve
signals, the four entry routes at the tracer, what each drug does at its target
and everywhere else it reached, the liver's fixed clearance rate, and the
dose-response argument in the stretch layer.

The distractors are built from the lesson's two declared misconceptions and
from the further errors its own copy exists to correct. DRUG-01 ("drugs are
illegal substances") supplies the options that sort drugs by law rather than by
what they do — caffeine and nicotine put in different classes because one is
sold to children, morphine "stopping being a drug" once prescribed, a hospital
version being "a different, safer substance". DRUG-02 ("a painkiller goes to
the part that hurts") supplies the options that give a dose a destination — a
tablet "used up" by the pathways it acted on, a drug that only shows side
effects at large doses. The page's unminted third wrong idea — that *poison* is
a category of substance, and that *natural* implies *gentle* — supplies h01.
Four further errors the copy corrects directly are worked as well: that a
depressant makes you sad, that a painkiller treats the cause of the pain, that
nicotine is what damages the lungs, and that addiction is a weakness of
character.

No question restates a ladder rung. The rungs already own the definition of a
drug stated flat, the swallowed paracetamol's route, the caffeine tablet and
the racing heart, and the second paracetamol dose taken early — so the bank
works around all four: the definition is reached through morphine and through a
herbal tea rather than asked directly, the route is taken through nicotine and
alcohol rather than paracetamol, the caffeine-and-heart explanation is left
alone entirely, and paracetamol appears as where the dose finally leaves you
rather than as how much of it to take.

`figure` is `None` throughout — the lesson declares no figures (NOTES-B6
flag 14), and every stem here is self-contained. Nothing in this file states a
dose, a threshold or a method for any substance; NOTES-B6 §1 rules that a gate
on the unit and it binds the question bank exactly as it binds the page.
"""

UNIT = "B6"
LESSON = "what-drugs-do-to-the-body"
LESSON_NUMBER = 1

QUESTIONS = [

    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "b6-01-e01",
        "band": "easier",
        "text": "Caffeine and nicotine are put in the same class of drug. "
                "Which class is it, and what does that class do?",
        "options": [
            {"text": "Stimulants — nerve signals pass more readily, so heart "
                     "rate and alertness rise", "correct": True},
            {"text": "Depressants — signals between nerve cells pass less "
                     "readily, so reactions worsen", "correct": False,
             "why": "That is alcohol, and the sedatives used in anaesthetics. "
                    "Caffeine and nicotine do the opposite: they make nerve "
                    "signals pass more readily."},
            {"text": "Painkillers — the pain signal is blocked on its way to "
                     "the brain", "correct": False,
             "why": "That class is paracetamol, ibuprofen and morphine. "
                    "Neither caffeine nor nicotine touches a pain signal at "
                    "all."},
            {"text": "Different classes — one is legal at any age and the "
                     "other is not", "correct": False,
             "why": "Legality is a decision a parliament makes, and it can "
                    "change. The three classes sort drugs by what they do to "
                    "nerve signals, and on that test these two belong "
                    "together."},
        ],
        "figure": None,
    },
    {
        "id": "b6-01-e02",
        "band": "easier",
        "text": "Alcohol is called a depressant. What does that word tell you "
                "about what it does?",
        "options": [
            {"text": "It makes the person sad and low in mood",
             "correct": False,
             "why": "A depressant does not make you sad. The word is a "
                    "statement about signalling speed, not about mood."},
            {"text": "It reduces the pain signal on its way to the brain",
             "correct": False,
             "why": "That is what a painkiller does. Alcohol slows every "
                    "signal passing between nerve cells, not only the ones "
                    "carrying pain."},
            {"text": "It slows the signals passing between nerve cells down",
             "correct": True},
            {"text": "It makes a person keep taking it once they have "
                     "started", "correct": False,
             "why": "Being addictive is a separate property some drugs have. "
                    "Nicotine is a stimulant and strongly addictive — the "
                    "class name tells you about nerve signals, not about "
                    "addiction."},
        ],
        "figure": None,
    },
    {
        "id": "b6-01-e03",
        "band": "easier",
        "text": "Nicotine is inhaled rather than swallowed. How does it get "
                "from the smoke into the blood?",
        "options": [
            {"text": "Through the wall of the small intestine, a few minutes "
                     "after it is taken", "correct": False,
             "why": "That is the route a swallowed drug like caffeine takes. "
                    "Inhaled nicotine never goes near the gut."},
            {"text": "Straight across the thin alveoli walls, reaching the "
                     "brain in about ten seconds", "correct": True},
            {"text": "Straight through the stomach wall, which is why it "
                     "arrives so quickly", "correct": False,
             "why": "Alcohol is the drug that does that, and it is unusual "
                    "for doing it. Nicotine is breathed in, so it crosses "
                    "into the blood in the lungs."},
            {"text": "Through the lining of the mouth and throat as the smoke "
                     "passes", "correct": False,
             "why": "The lesson follows the smoke further than that. Nicotine "
                    "crosses the thin alveoli walls, which is why it reaches "
                    "the brain faster than any swallowed drug."},
        ],
        "figure": None,
    },
    {
        "id": "b6-01-e04",
        "band": "easier",
        "text": "A painkiller has taken away someone's toothache. What has it "
                "done to the tooth that was causing the pain?",
        "options": [
            {"text": "Reduced the swelling that was pressing on the nerve "
                     "inside it", "correct": False,
             "why": "The drug acts on the pathways carrying the pain signal, "
                    "not on the tooth. Nothing about the tooth has changed."},
            {"text": "Started to heal it, which is why the pain fades",
             "correct": False,
             "why": "A painkiller blocks the message. The cause of the pain is "
                    "untouched, and pain that stops being felt has not stopped "
                    "being a warning."},
            {"text": "Killed the bacteria that were causing the infection",
             "correct": False,
             "why": "That is a different job for a different drug. A "
                    "painkiller reduces the pain signal and leaves the "
                    "infection exactly as it was."},
            {"text": "Nothing at all — only the pain signal has been blocked",
             "correct": True},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "b6-01-s01",
        "band": "standard",
        "text": "Someone who has been drinking says they feel fine and are "
                "certain they can walk home safely. Why is that judgement "
                "itself part of the problem?",
        "options": [
            {"text": "Alcohol is a depressant, so feeling fine means it has "
                     "not taken effect yet", "correct": False,
             "why": "Depressant is a statement about signalling speed, not "
                    "about mood. Feeling fine is what slowed judgement feels "
                    "like from the inside."},
            {"text": "The alcohol has not reached the brain yet, because it "
                     "must pass through the intestine first", "correct": False,
             "why": "Alcohol is unusual: it is absorbed straight through the "
                    "stomach wall as well as through the intestine, so it "
                    "arrives in the blood quickly."},
            {"text": "Alcohol slows signals throughout the brain, and "
                     "judgement goes first — the thing least able to notice "
                     "itself", "correct": True},
            {"text": "Only their coordination is affected, and walking is "
                     "something the body does automatically", "correct": False,
             "why": "Alcohol slows the signals passing between nerve cells "
                    "throughout the brain. Reactions, coordination and "
                    "judgement all worsen together."},
        ],
        "figure": None,
    },
    {
        "id": "b6-01-s02",
        "band": "standard",
        "text": "Morphine is a controlled drug, and it is also given to "
                "patients in hospital every day. What does that tell you "
                "about the words drug and medicine?",
        "options": [
            {"text": "They describe overlapping sets — a medicine is simply a "
                     "drug used to treat something", "correct": True},
            {"text": "The hospital version must be a different, safer "
                     "substance from the controlled one", "correct": False,
             "why": "It is the same molecule. What changes is the dose and who "
                    "decides on it, not what the molecule does once it is in "
                    "the blood."},
            {"text": "Morphine stops being a drug at the moment a doctor "
                     "prescribes it", "correct": False,
             "why": "Prescribing changes who may have it. A drug is any "
                    "substance that changes the way the body works, and a "
                    "prescription does not alter that."},
            {"text": "The law has it wrong, because a substance used in "
                     "hospitals cannot be harmful", "correct": False,
             "why": "Legal and safe are not the same word, and neither are "
                    "illegal and harmful. Morphine does both jobs, which is "
                    "exactly why its supply is controlled."},
        ],
        "figure": None,
    },
    {
        "id": "b6-01-s03",
        "band": "standard",
        "text": "A dose of paracetamol has done its job on a headache. What "
                "happens to the drug after that, and how does it leave you?",
        "options": [
            {"text": "It is used up by the pain pathways it acted on, so "
                     "there is nothing left to remove", "correct": False,
             "why": "Acting on a pathway does not consume the drug. It is "
                    "still in the blood, and it still has to be broken down "
                    "and removed."},
            {"text": "The stomach acid that dissolved the tablet breaks it "
                     "down again", "correct": False,
             "why": "Dissolving in the stomach is only how it got into the "
                    "blood. Breaking it down is the liver's job, at a fixed "
                    "rate it cannot exceed."},
            {"text": "It stays in the body for good, which is why the box "
                     "sets a dose interval", "correct": False,
             "why": "The interval matters because the liver clears the drug "
                    "at a rate that cannot be hurried, not because the drug "
                    "never leaves at all."},
            {"text": "The liver breaks it down, and the kidneys filter the "
                     "broken-down drug out into the urine", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b6-01-s04",
        "band": "standard",
        "text": "A smoker says that nicotine is the substance damaging their "
                "lungs. Where is that wrong?",
        "options": [
            {"text": "Nicotine damages the lungs first, and the rest of the "
                     "smoke adds to it later", "correct": False,
             "why": "Nicotine's own effects are on the brain, the heart and "
                    "the blood vessels. The airway and lung damage is done by "
                    "tar and the other substances in the smoke."},
            {"text": "Nicotine is why they keep smoking; tar and the other "
                     "substances in the smoke do that damage", "correct": True},
            {"text": "Nicotine never reaches the lungs at all, because it "
                     "goes straight to the brain", "correct": False,
             "why": "It reaches the brain by crossing the thin alveoli walls, "
                    "so the lungs are how it gets there. What matters is what "
                    "it does once it is in the blood."},
            {"text": "It is nicotine narrowing the blood vessels that damages "
                     "the lung tissue", "correct": False,
             "why": "Nicotine does narrow blood vessels — in the skin, which "
                    "is one reason wounds heal more slowly in smokers. The "
                    "lung damage is other substances in the smoke."},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "b6-01-h01",
        "band": "harder",
        "text": "A herbal tea is sold with the line “completely natural, "
                "so it cannot do you any harm”. What is wrong with that "
                "reasoning?",
        "options": [
            {"text": "Nothing — a natural substance is gentler, because the "
                     "body recognises it", "correct": False,
             "why": "“It is natural, so it must be gentle” is a "
                    "claim about where a molecule came from, not about what it "
                    "does. Foxglove grows in a hedgerow and is one of the most "
                    "dangerous plants in Britain."},
            {"text": "Where a molecule came from says nothing about what it "
                     "does to the body", "correct": True},
            {"text": "Natural substances are not drugs, so the claim is about "
                     "food rather than about medicine", "correct": False,
             "why": "A drug is any substance that changes the way the body "
                    "works, whatever it came from. Digoxin comes from the "
                    "foxglove and has been prescribed for two hundred years."},
            {"text": "It is only wrong if the tea turns out to have caffeine "
                     "in it as well", "correct": False,
             "why": "The reasoning fails whatever is in the cup. Poison is not "
                    "a category of substance — it is a statement about "
                    "quantity, and even water follows that rule."},
        ],
        "figure": None,
    },
    {
        "id": "b6-01-h02",
        "band": "harder",
        "text": "A company advertises a new painkiller as the first one with "
                "no side effects at all. Why should you doubt that before you "
                "know anything else about it?",
        "options": [
            {"text": "The blood offers the dose to every organ, so it will act "
                     "wherever else it fits", "correct": True},
            {"text": "Because no company tests a new drug carefully enough to "
                     "be able to promise that", "correct": False,
             "why": "This is not about how carefully it was tested. A side "
                    "effect is the unavoidable consequence of delivering a "
                    "drug through a system that goes everywhere."},
            {"text": "Because side effects only show up at large amounts, and "
                     "the advert means an ordinary one", "correct": False,
             "why": "The whole dose goes round the circuit whatever its size. "
                    "Amount changes how strong an effect is, not whether the "
                    "drug reached organs it was not taken for."},
            {"text": "Because a painkiller leaves the cause of the pain "
                     "untouched, and that is the side effect", "correct": False,
             "why": "A painkiller does leave the cause untouched, but that is "
                    "not what a side effect means. A side effect is what the "
                    "same dose did to the other organs it reached."},
        ],
        "figure": None,
    },
    {
        "id": "b6-01-h03",
        "band": "harder",
        "text": "Someone who has smoked for years says they could stop "
                "tomorrow if they simply had more willpower. What does this "
                "lesson say is actually going on in their brain?",
        "options": [
            {"text": "Nothing physical — a habit is a decision repeated, and "
                     "it is broken by deciding to break it", "correct": False,
             "why": "The lesson is explicit: the wanting is a physical state "
                    "of the nervous system rather than a weakness of "
                    "character."},
            {"text": "Nicotine slows the brain down until making any decision "
                     "becomes impossible", "correct": False,
             "why": "Nicotine is a stimulant — it makes signals pass more "
                    "readily. Slowing signals down is what a depressant such "
                    "as alcohol does."},
            {"text": "The tar in the smoke is the part that keeps people "
                     "coming back to it", "correct": False,
             "why": "Tar and the other substances in smoke do most of the "
                    "damage. Nicotine is the reason people keep smoking — the "
                    "two are different molecules in the same smoke."},
            {"text": "The brain has adapted to expect the reward chemical "
                     "nicotine releases, so the wanting is physical",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b6-01-h04",
        "band": "harder",
        "text": "Two people take the same drug at the same moment. One "
                "swallows it and the other inhales it. Who feels it first, "
                "and why?",
        "options": [
            {"text": "The one who swallowed it — the stomach absorbs a dose "
                     "straight away", "correct": False,
             "why": "Alcohol is unusual in crossing the stomach wall, and even "
                    "that is slower than crossing into the blood in the lungs, "
                    "which takes about ten seconds to reach the brain."},
            {"text": "The one who swallowed it, because a whole tablet is "
                     "more drug than a single breath", "correct": False,
             "why": "The question is how fast the dose reaches the blood, not "
                    "how much of it there is. A larger amount does not travel "
                    "round the circuit any faster."},
            {"text": "The one who inhaled it — the drug crosses the thin "
                     "alveoli walls straight into the blood", "correct": True},
            {"text": "Both at the same time, because the blood completes the "
                     "whole circuit in under a minute", "correct": False,
             "why": "The circuit does take under a minute, but that clock "
                    "starts when the dose reaches the blood. The two doses do "
                    "not get there at the same moment."},
        ],
        "figure": None,
    },
]
