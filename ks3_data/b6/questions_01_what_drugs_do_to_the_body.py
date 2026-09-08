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
                     "judgement goes first, unnoticed", "correct": True},
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
                     "substances do the damage", "correct": True},
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

    # ── MRB-335 top-up ──────────────────────────────────────────────────
    #
    # Forty-two rows, mapped onto the lesson's distinct teachable points
    # rather than onto one point reworded: the three classes and what each
    # does to nerve signals, the four entry routes, the two claims of stages
    # 2 and 3, each drug's target, each drug's `elsewhere` organs one at a
    # time, the liver's fixed rate and the kidneys' filtering, dose as the
    # thing that decides, and the stretch layer's dose-response argument.
    # Nothing here states a dose, a threshold or a method for any substance
    # (NOTES-B6 §1), and the one calculation is a comparison of two TIMES.

    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "b6-01-e05",
        "band": "easier",
        "text": "Which class of drug do paracetamol, ibuprofen and morphine "
                "belong to?",
        "options": [
            {"text": "Depressants, because they slow the whole nervous "
                     "system down", "correct": False,
             "why": "A depressant slows the signals passing between nerve "
                    "cells throughout the brain, which is what alcohol does. "
                    "These three act on the pain signal."},
            {"text": "Painkillers, because they reduce or block the pain "
                     "signal", "correct": True},
            {"text": "Stimulants, because they make a person better able to "
                     "cope", "correct": False,
             "why": "Coping better is not the test. A stimulant makes nerve "
                    "signals pass more readily so heart rate and alertness "
                    "rise, and none of these three does that."},
            {"text": "Different classes, because morphine is controlled and "
                     "the others are not", "correct": False,
             "why": "Legal control is a decision a parliament makes. The "
                    "three classes sort drugs by what they do to nerve "
                    "signals, and on that test these three belong together."},
        ],
        "figure": None,
    },
    {
        "id": "b6-01-e06",
        "band": "easier",
        "text": "Which organ does most of the work of breaking a drug down "
                "down?",
        "options": [
            {"text": "The kidneys, because they are the organs that make "
                     "urine", "correct": False,
             "why": "The kidneys filter the broken-down drug out into the "
                    "urine, which is the last step. The breaking down itself "
                    "happens in the liver."},
            {"text": "The stomach, because that is where a tablet dissolves",
             "correct": False,
             "why": "Dissolving in the stomach is how a swallowed drug gets "
                    "into the blood, not how it is destroyed. The liver does "
                    "the breaking down."},
            {"text": "The brain, because that is where most drugs have their "
                     "effect", "correct": False,
             "why": "Where a drug acts and where it is broken down are two "
                    "different places. Acting on the brain does not use the "
                    "drug up."},
            {"text": "The liver, at a fixed rate that cannot be hurried",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b6-01-e07",
        "band": "easier",
        "text": "Caffeine is swallowed in coffee, tea, cola or an energy "
                "drink. What does it do once it reaches the brain?",
        "options": [
            {"text": "It slows nerve signals down, so a tired person stops "
                     "noticing that they are tired", "correct": False,
             "why": "Slowing nerve signals is what a depressant does. "
                    "Caffeine is a stimulant, and nerve cells go on firing "
                    "readily."},
            {"text": "It replaces the energy the body has used up during the "
                     "day", "correct": False,
             "why": "Caffeine supplies no energy at all — energy comes from "
                    "food. It changes how nerve cells behave, which is a "
                    "different thing entirely."},
            {"text": "It blocks the chemical signal that builds up through "
                     "the day to make you sleepy", "correct": True},
            {"text": "It blocks the pain signal, which is why coffee helps a "
                     "headache", "correct": False,
             "why": "Blocking a pain signal is a painkiller's job. Caffeine "
                    "acts on the signal that makes you feel sleepy, which is "
                    "a different signal."},
        ],
        "figure": None,
    },
    {
        "id": "b6-01-e08",
        "band": "easier",
        "text": "Alcohol is unusual among swallowed drugs because of where it "
                "is absorbed. Where does it cross into the blood?",
        "options": [
            {"text": "Through the stomach wall as well as the intestine, so "
                     "it arrives quickly", "correct": True},
            {"text": "Only through the wall of the small intestine, like "
                     "every other swallowed drug", "correct": False,
             "why": "That is the ordinary route, and caffeine and paracetamol "
                    "take it. Alcohol also crosses the stomach wall, which is "
                    "why it arrives in the blood so quickly."},
            {"text": "Through the thin alveoli walls, in the same way as an "
                     "inhaled drug", "correct": False,
             "why": "That is nicotine's route out of cigarette smoke. Alcohol "
                    "is swallowed, so it never reaches the alveoli on its way "
                    "into the blood."},
            {"text": "Through the lining of the mouth, before it has been "
                     "swallowed at all", "correct": False,
             "why": "The drink goes further than the mouth before anything "
                    "is absorbed. Alcohol crosses the stomach wall and the "
                    "intestine wall, and that is where it enters the "
                    "blood."},
        ],
        "figure": None,
    },
    {
        "id": "b6-01-e09",
        "band": "easier",
        "text": "Which word describes what a drug does to organs it was not "
                "taken for?",
        "options": [
            {"text": "Its dose", "correct": False,
             "why": "A dose is the amount of a drug taken. What that amount "
                    "then does elsewhere in the body is a side effect."},
            {"text": "A side effect", "correct": True},
            {"text": "Misuse of the drug", "correct": False,
             "why": "Misuse is using a substance in a way that damages "
                    "health. A side effect happens even when a drug is taken "
                    "exactly as it should be."},
            {"text": "An allergic reaction", "correct": False,
             "why": "An allergy is one person's body reacting to a substance "
                    "unusually. A side effect is what the drug does to every "
                    "organ the blood offered it to."},
        ],
        "figure": None,
    },
    {
        "id": "b6-01-e10",
        "band": "easier",
        "text": "The sedatives used in anaesthetics are grouped with alcohol. "
                "Which class is that?",
        "options": [
            {"text": "Painkillers, because a patient under anaesthetic feels "
                     "no pain", "correct": False,
             "why": "An anaesthetic and a painkiller are not the same thing. "
                    "These drugs are grouped with alcohol because they make "
                    "nerve signals pass less readily."},
            {"text": "Stimulants, because they act strongly on the nervous "
                     "system", "correct": False,
             "why": "Acting strongly is not the test. A stimulant makes nerve "
                    "signals pass more readily; these make them pass less "
                    "readily."},
            {"text": "Medicines, which is a fourth class beside the other "
                     "three", "correct": False,
             "why": "Medicine is not one of the classes. It says what a drug "
                    "is being used for, and a medicine belongs to whichever "
                    "class its effect on nerve signals puts it in."},
            {"text": "Depressants, because they make nerve signals pass less "
                     "readily", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b6-01-e11",
        "band": "easier",
        "text": "What does the word dose mean when it is used about a drug?",
        "options": [
            {"text": "The amount of the drug that is taken", "correct": True},
            {"text": "The strength of the effect the drug has",
             "correct": False,
             "why": "The effect follows from the amount, but the two are not "
                    "the same word. Dose is the amount taken."},
            {"text": "The time to leave between one tablet and the next",
             "correct": False,
             "why": "That is the dose interval, a separate number on the box. "
                    "The dose itself is how much is taken."},
            {"text": "The illness the drug is being taken for",
             "correct": False,
             "why": "The reason for taking a drug is not what dose means. "
                    "Dose is the amount, and it is what decides whether a "
                    "drug treats you or harms you."},
        ],
        "figure": None,
    },
    {
        "id": "b6-01-e12",
        "band": "easier",
        "text": "What does nicotine do when it reaches the brain?",
        "options": [
            {"text": "It blocks the signal that would otherwise make a person "
                     "feel sleepy", "correct": False,
             "why": "That is caffeine's effect on the sleepy signal. Nicotine "
                    "works on the brain's reward pathways instead."},
            {"text": "It slows the brain down, which is why a smoker feels "
                     "calmer", "correct": False,
             "why": "Nicotine is a stimulant, so signals pass more readily "
                    "rather than less. Slowing the brain down is what a "
                    "depressant such as alcohol does."},
            {"text": "It triggers a release of the brain's own reward "
                     "chemical", "correct": True},
            {"text": "It repairs the damage the rest of the smoke has done",
             "correct": False,
             "why": "Nothing in smoke repairs anything. Tar and the other "
                    "substances do the damage, and nicotine does not undo "
                    "it."},
        ],
        "figure": None,
    },
    {
        "id": "b6-01-e13",
        "band": "easier",
        "text": "Caffeine reaches the kidneys as well as the brain. What do "
                "the kidneys do in response?",
        "options": [
            {"text": "They break the caffeine down so that it stops working",
             "correct": False,
             "why": "Breaking a drug down is the liver's job. The kidneys "
                    "filter the broken-down drug out afterwards."},
            {"text": "They produce more urine, which is why coffee sends you "
                     "to the toilet", "correct": True},
            {"text": "They stop working until the caffeine has been cleared",
             "correct": False,
             "why": "Nothing shuts down. The kidneys carry on with their own "
                    "job and produce more urine while the caffeine is "
                    "there."},
            {"text": "Nothing, because caffeine travels only to the brain",
             "correct": False,
             "why": "There is no address on a dose. The blood offers the "
                    "caffeine to every organ, and the kidneys are one of the "
                    "organs it reaches."},
        ],
        "figure": None,
    },
    {
        "id": "b6-01-e14",
        "band": "easier",
        "text": "A drug has just been absorbed and is dissolved in the blood "
                "plasma. What does the molecule itself say about where it "
                "should go?",
        "options": [
            {"text": "It carries a marker that the organ needing it "
                     "recognises", "correct": False,
             "why": "There is no marker and no recognition step. The blood "
                    "simply offers the dose to everything it passes."},
            {"text": "It stays in the plasma until the right organ asks for "
                     "it", "correct": False,
             "why": "No organ asks. The blood makes the full circuit and "
                    "every organ is offered the drug, whether it needs it or "
                    "not."},
            {"text": "It goes to whichever organ is working hardest at the "
                     "time", "correct": False,
             "why": "Effort does not attract a drug. Where it acts is decided "
                    "by whether there is something there for it to act on."},
            {"text": "Nothing at all — the molecule carries no address",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b6-01-e15",
        "band": "easier",
        "text": "Roughly how long does the blood take to carry a dose once "
                "round the whole body?",
        "options": [
            {"text": "Under a minute", "correct": True},
            {"text": "About ten seconds", "correct": False,
             "why": "Ten seconds is how long inhaled nicotine takes to get "
                    "from the lungs to the brain. A full circuit of the body "
                    "takes longer than that."},
            {"text": "About an hour", "correct": False,
             "why": "An hour is roughly how long the liver takes to break "
                    "down one unit of alcohol. The blood itself moves round "
                    "far faster than that."},
            {"text": "About a day", "correct": False,
             "why": "A drug would then have no effect for hours after it was "
                    "taken. The blood completes the whole circuit in under a "
                    "minute."},
        ],
        "figure": None,
    },
    {
        "id": "b6-01-e16",
        "band": "easier",
        "text": "Paracetamol reduces pain, and it also acts on the "
                "temperature control centre of the brain. What does that "
                "second action do?",
        "options": [
            {"text": "It kills the bacteria that caused the infection",
             "correct": False,
             "why": "Paracetamol does nothing whatever to an injury or an "
                    "infection. Acting on the temperature control centre "
                    "brings a fever down."},
            {"text": "It warms a person up when they are cold",
             "correct": False,
             "why": "It is used the other way round. Acting on the "
                    "temperature control centre is what brings a fever "
                    "down."},
            {"text": "It brings a fever down", "correct": True},
            {"text": "It sends the person to sleep", "correct": False,
             "why": "Paracetamol is a painkiller, not a sedative. Its second "
                    "effect is on the temperature control centre, and that "
                    "brings a fever down."},
        ],
        "figure": None,
    },
    {
        "id": "b6-01-e17",
        "band": "easier",
        "text": "Nicotine narrows the blood vessels in the skin. What "
                "follows from that?",
        "options": [
            {"text": "The skin is better protected from the cold",
             "correct": False,
             "why": "Less blood reaching the surface protects nothing. It is "
                    "one reason wounds heal more slowly in smokers."},
            {"text": "Wounds heal more slowly, because less blood reaches "
                     "the surface", "correct": True},
            {"text": "The skin takes in oxygen from the air instead",
             "correct": False,
             "why": "Skin does not take oxygen from the air; the blood "
                    "delivers it. Narrowed vessels mean less blood reaching "
                    "the surface."},
            {"text": "Nicotine cannot reach the skin, because it acts on the "
                     "brain", "correct": False,
             "why": "The blood offers the dose to every organ, skin included. "
                    "Acting on the brain does not stop a drug reaching "
                    "everywhere else."},
        ],
        "figure": None,
    },
    {
        "id": "b6-01-e18",
        "band": "easier",
        "text": "Paracetamol can be bought without a prescription. What is "
                "printed on the box in place of a doctor's instructions?",
        "options": [
            {"text": "The name of the doctor who approved it",
             "correct": False,
             "why": "No doctor is involved in buying it, which is what "
                    "without a prescription means. What the box carries is a "
                    "dose limit."},
            {"text": "A promise that it has no side effects", "correct": False,
             "why": "No drug can promise that, because the blood carries it "
                    "to every organ. The box carries a dose limit instead."},
            {"text": "A list of the organs the drug will reach",
             "correct": False,
             "why": "The drug reaches all of them, so no such list would be "
                    "short. What the box carries is a dose limit."},
            {"text": "A dose limit saying how much may be taken",
             "correct": True},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "b6-01-s05",
        "band": "standard",
        "text": "Someone drinks a strong black coffee on an empty stomach and "
                "gets a burning pain in their stomach. What is the best "
                "explanation?",
        "options": [
            {"text": "The coffee was too hot; the caffeine is not involved", "correct": False,
             "why": "Heat is felt going down rather than as a burning pain "
                    "afterwards. The caffeine reached the stomach and made it "
                    "release more acid."},
            {"text": "The caffeine was broken down by the stomach lining, and "
                     "the burning is that reaction", "correct": False,
             "why": "Breaking a drug down is the liver's job, not the stomach "
                    "lining's, and it releases no burning of its own. The "
                    "pain comes from the extra acid the stomach releases."},
            {"text": "Caffeine reached the stomach too, and made it release "
                     "more acid", "correct": True},
            {"text": "The caffeine cannot be absorbed without food, so it "
                     "stayed in the stomach", "correct": False,
             "why": "Caffeine crosses the intestine wall whether or not there "
                    "is food there. What causes the pain is the extra acid "
                    "the stomach was made to release."},
        ],
        "figure": None,
    },
    {
        "id": "b6-01-s06",
        "band": "standard",
        "text": "A footballer takes a painkiller at half time so that an "
                "injured ankle stops hurting, and plays the second half. "
                "What is true of the ankle for the rest of the match?",
        "options": [
            {"text": "It is as injured as before, and the pain warning has "
                     "gone", "correct": True},
            {"text": "The pain will come back suddenly, and worse than it had "
                     "been before", "correct": False,
             "why": "The pain does return as the liver clears the drug, but "
                    "that is not the danger. The danger is that the injury is "
                    "unchanged while the warning is switched off."},
            {"text": "It will heal more slowly than it would have done with "
                     "rest", "correct": False,
             "why": "A painkiller does nothing to the injury in either "
                    "direction. It reduces the pain signal and leaves the "
                    "ankle exactly as it was."},
            {"text": "It has recovered enough to be used, because it no "
                     "longer hurts", "correct": False,
             "why": "Pain that stops being felt has not stopped being a "
                    "warning. The drug blocked the message, not the damage."},
        ],
        "figure": None,
    },
    {
        "id": "b6-01-s07",
        "band": "standard",
        "text": "Some stimulants are prescribed by doctors. A student says a "
                "prescribed stimulant must therefore belong to a different "
                "class from caffeine. Is that right?",
        "options": [
            {"text": "Yes — a prescribed drug is a medicine, and medicines "
                     "are not sorted into those classes", "correct": False,
             "why": "Medicine says what a drug is being used for, not what it "
                    "does to nerve signals. A medicine belongs to whichever "
                    "class its effect puts it in."},
            {"text": "No — the class describes what a drug does to nerve "
                     "signals, and both speed them up", "correct": True},
            {"text": "No — but only because a doctor could prescribe caffeine "
                     "as well if they chose to", "correct": False,
             "why": "Who may prescribe it is beside the point. The two are in "
                    "the same class because both make nerve signals pass more "
                    "readily."},
            {"text": "Yes — a prescribed stimulant is given at a controlled "
                     "dose, so it acts differently", "correct": False,
             "why": "A controlled dose changes how strong the effect is, not "
                    "what kind of effect it is. The class is about what "
                    "happens to nerve signals."},
        ],
        "figure": None,
    },
    {
        "id": "b6-01-s08",
        "band": "standard",
        "text": "A side effect is what a drug does to the organs it reached "
                "but was not taken for. Which of these is a side effect?",
        "options": [
            {"text": "Paracetamol bringing down the fever of someone who took "
                     "it for a fever", "correct": False,
             "why": "That is the effect it was taken for, so it is not a side "
                    "effect. A side effect is what the same dose did "
                    "somewhere else."},
            {"text": "The liver breaking a drug down once the drug has done "
                     "its job", "correct": False,
             "why": "Clearing a drug is the body removing it, not the drug "
                    "acting. A side effect is the drug acting where it was "
                    "not wanted."},
            {"text": "A painkiller failing to work on a particularly bad "
                     "headache", "correct": False,
             "why": "A drug not working is a disappointment rather than a "
                    "side effect. A side effect is something extra the drug "
                    "did, not something it failed to do."},
            {"text": "Caffeine speeding up the heart of someone who took it "
                     "to stay awake", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b6-01-s09",
        "band": "standard",
        "text": "A student argues that depressants must be safer than "
                "stimulants, because slowing the body down cannot do much "
                "harm. Are they right?",
        "options": [
            {"text": "They are right — a depressant only makes a person "
                     "sleepy, and sleep is harmless", "correct": False,
             "why": "A depressant is not simply something that causes sleep. "
                    "It worsens reactions, coordination and judgement, and "
                    "that is where the harm comes from."},
            {"text": "They are right about alcohol, though not about the "
                     "sedatives a doctor gives before surgery", "correct": False,
             "why": "Alcohol is the depressant that causes most harm of the "
                    "two, not the least. Slowing a nervous system down is not "
                    "a safe thing to do to it."},
            {"text": "Slower is not safer: the harm is in what a slowed "
                     "nervous system does", "correct": True},
            {"text": "They are wrong: a depressant speeds the heart up as "
                     "well", "correct": False,
             "why": "Speeding the heart up is a stimulant's effect. A "
                    "depressant's harm comes from worsened reactions, "
                    "coordination and judgement."},
        ],
        "figure": None,
    },
    {
        "id": "b6-01-s10",
        "band": "standard",
        "text": "Caffeine swallowed in a drink takes a few minutes to reach "
                "the blood, while alcohol swallowed in a drink arrives "
                "faster. Why?",
        "options": [
            {"text": "Alcohol crosses the stomach wall; caffeine waits for "
                     "the intestine",
             "correct": True},
            {"text": "There is less alcohol in a drink, so there is less of "
                     "it for the body to deal with", "correct": False,
             "why": "How much there is does not change how fast a drug "
                    "crosses into the blood. What matters is where it can "
                    "cross, and alcohol can cross the stomach wall."},
            {"text": "Alcohol is a depressant, and depressants are absorbed "
                     "faster than stimulants", "correct": False,
             "why": "The class describes what a drug does to nerve signals, "
                    "not how quickly it is absorbed. Alcohol is fast because "
                    "of where it crosses into the blood."},
            {"text": "Alcohol is absorbed through the lungs as you breathe, "
                     "which is why you can smell it on the breath", "correct": False,
             "why": "The smell on the breath is a trace leaving the blood, "
                    "not alcohol going in. It is absorbed in the stomach and "
                    "the intestine."},
        ],
        "figure": None,
    },
    {
        "id": "b6-01-s11",
        "band": "standard",
        "text": "A child with an infection is given paracetamol and their "
                "temperature falls. A parent says the infection has been "
                "treated. Where is that wrong?",
        "options": [
            {"text": "The temperature has not really fallen; the drug only "
                     "makes the child feel cooler to touch", "correct": False,
             "why": "The temperature really does fall, and a thermometer "
                    "would show it, because the drug acts on the brain's "
                    "temperature control centre. What has not changed is the "
                    "infection."},
            {"text": "The drug shortened the infection, which is why the "
                     "temperature came down", "correct": False,
             "why": "A fever is the body's response, not the infection "
                    "itself. Lowering it does nothing to whatever is causing "
                    "it."},
            {"text": "The drug will have killed some of the bacteria as well, "
                     "but not all of them", "correct": False,
             "why": "Paracetamol kills nothing. It acts on the pain pathways "
                    "and on the temperature control centre and leaves the "
                    "infection untouched."},
            {"text": "It acted on the brain's temperature centre, not the "
                     "infection", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b6-01-s12",
        "band": "standard",
        "text": "Someone uses nicotine because it makes them feel alert, and "
                "is surprised to hear that it raises their blood pressure. "
                "Why does it?",
        "options": [
            {"text": "Because a stimulant is bound to raise the blood "
                     "pressure first and the alertness only afterwards", "correct": False,
             "why": "There is no order of that kind. Blood pressure rises "
                    "because the same dose reached the heart and the blood "
                    "vessels on the same circuit."},
            {"text": "One dose reached the heart and the vessels: faster "
                     "beat, narrower vessels", "correct": True},
            {"text": "Because nicotine is broken down into a substance that "
                     "then raises the blood pressure", "correct": False,
             "why": "It is nicotine itself acting on the heart and vessels it "
                    "reached. Breaking a drug down is how it is removed, not "
                    "how it acts."},
            {"text": "It does not — the raised blood pressure comes from the "
                     "tar", "correct": False,
             "why": "Tar damages the airways and the alveoli. The faster "
                    "heart, the narrowed vessels and the raised blood "
                    "pressure are nicotine's."},
        ],
        "figure": None,
    },
    {
        "id": "b6-01-s13",
        "band": "standard",
        "text": "The blood carries every drug to every organ. Why, then, "
                "does caffeine not block pain, and paracetamol not keep you "
                "awake?",
        "options": [
            {"text": "Because each drug is broken down by the liver before it "
                     "can reach the second organ", "correct": False,
             "why": "Breaking down in the liver takes hours, long after the "
                    "circuit is complete. Both drugs really do reach both "
                    "places."},
            {"text": "Because the body sends each drug to the right organ", "correct": False,
             "why": "There is no sorting step. Both drugs are offered to "
                    "everything, which is exactly why side effects exist."},
            {"text": "A drug acts only where it fits, and neither fits the "
                     "other's target",
             "correct": True},
            {"text": "Because the amount of each drug is far too small for it "
                     "to manage two different jobs at once", "correct": False,
             "why": "A larger amount does not give a drug a new kind of "
                    "effect. Where a drug acts is decided by what it fits, "
                    "not by how much of it there is."},
        ],
        "figure": None,
    },
    {
        "id": "b6-01-s14",
        "band": "standard",
        "text": "Which of these is the order a swallowed tablet actually "
                "follows?",
        "options": [
            {"text": "It dissolves, crosses the gut wall into the blood, is "
                     "carried round the whole body, then acts where it fits",
             "correct": True},
            {"text": "It dissolves, acts where it fits, crosses the gut wall "
                     "into the blood, then is carried round the body",
             "correct": False,
             "why": "A drug cannot act before it has reached anything. It has "
                    "to be in the blood first, and the blood then takes it "
                    "everywhere."},
            {"text": "It crosses the gut wall, dissolves in the blood, acts "
                     "where it fits, then is carried round the body",
             "correct": False,
             "why": "A tablet has to dissolve before it can cross anything, "
                    "and being carried round the body comes before it acts "
                    "rather than after."},
            {"text": "It dissolves, is carried round the whole body, acts "
                     "where it fits, then crosses the gut wall",
             "correct": False,
             "why": "Crossing the gut wall is how the drug gets into the "
                    "blood in the first place, so it cannot be the last "
                    "step."},
        ],
        "figure": None,
    },
    {
        "id": "b6-01-s15",
        "band": "standard",
        "text": "Caffeine speeds the heart up, makes the kidneys produce more "
                "urine, and makes the stomach release more acid. Which of "
                "those three is why a person feels awake?",
        "options": [
            {"text": "The faster heart, because more blood then reaches the "
                     "brain", "correct": False,
             "why": "The faster heart is one of the things the caffeine did "
                    "on the way past. Feeling awake comes from what it does "
                    "at the brain itself."},
            {"text": "None of them — the alertness comes from what caffeine "
                     "does at the brain", "correct": True},
            {"text": "The extra acid, because a working stomach keeps a "
                     "person alert", "correct": False,
             "why": "Extra acid can hurt and does nothing for alertness. The "
                    "alertness is caffeine acting on the brain."},
            {"text": "The extra urine, because losing water makes a person "
                     "more alert", "correct": False,
             "why": "Losing water makes a person thirsty, not alert. All "
                    "three of those organs were simply on the route."},
        ],
        "figure": None,
    },
    {
        "id": "b6-01-s16",
        "band": "standard",
        "text": "Ibuprofen and morphine are both painkillers, yet morphine is "
                "a controlled drug and ibuprofen is not. What does the class "
                "name tell you, and what does it not?",
        "options": [
            {"text": "That the two are equally strong, and that the control "
                     "is about how each one is made", "correct": False,
             "why": "The class says nothing about strength — morphine sits at "
                    "the strong end. Control is about who may supply it, not "
                    "about manufacture."},
            {"text": "That morphine is a medicine and ibuprofen is not, "
                     "because only one of them is controlled", "correct": False,
             "why": "Both are medicines when they are used to treat "
                    "something. Being controlled is a decision about supply, "
                    "not about which one counts as a medicine."},
            {"text": "That neither has side effects, because both act only on "
                     "the pain signal", "correct": False,
             "why": "Both are carried to every organ by the blood, so both do "
                    "other things too. The class name says nothing at all "
                    "about side effects."},
            {"text": "That both reduce the pain signal; it says nothing about "
                     "strength or about the law", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b6-01-s17",
        "band": "standard",
        "text": "Someone is sick after a heavy evening's drinking and decides "
                "the food they ate must have been off. What else could "
                "explain it?",
        "options": [
            {"text": "The alcohol was broken down into something that caused "
                     "the sickness", "correct": False,
             "why": "The liver breaks alcohol down in order to remove it. The "
                    "sickness comes from the drink irritating the stomach "
                    "lining directly."},
            {"text": "The alcohol reached the brain, and sickness is a sign "
                     "the brain has been damaged", "correct": False,
             "why": "Sickness after a heavy evening is not brain damage. "
                    "Alcohol irritates the lining of the stomach it passed "
                    "through."},
            {"text": "Alcohol irritates the stomach lining directly, and "
                     "heavy drinking causes sickness", "correct": True},
            {"text": "Two causes cannot both be possible, so it has to be the "
                     "food", "correct": False,
             "why": "Two possible causes do not rule one another out; you "
                    "look for the more likely one. Alcohol irritating the "
                    "stomach lining is a known effect of a heavy evening."},
        ],
        "figure": None,
    },
    {
        "id": "b6-01-s18",
        "band": "standard",
        "text": "Somebody who drank heavily last night wakes extremely "
                "thirsty. Which of alcohol's effects explains that?",
        "options": [
            {"text": "It made the kidneys produce more urine, so the person "
                     "lost water", "correct": True},
            {"text": "It was broken down into water, which the body then had "
                     "to get rid of", "correct": False,
             "why": "Breaking alcohol down does not flood the body with "
                    "water. The thirst comes from the extra urine the kidneys "
                    "produced."},
            {"text": "It irritated the stomach lining, and a sore stomach "
                     "feels like thirst", "correct": False,
             "why": "An irritated stomach lining causes sickness rather than "
                    "thirst. The water was lost through the kidneys."},
            {"text": "It slowed the nervous system, so the person forgot to "
                     "drink during the evening", "correct": False,
             "why": "Alcohol does slow the nervous system, but thirst is not "
                    "a matter of memory. The person is short of water because "
                    "the kidneys produced more urine."},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "b6-01-h05",
        "band": "harder",
        "text": "Someone took more paracetamol yesterday than the box allows. "
                "Today they feel completely well and conclude that no harm "
                "was done. Is that conclusion safe?",
        "options": [
            {"text": "They are right, because the liver will have cleared the "
                     "whole amount overnight", "correct": False,
             "why": "The liver works at a fixed rate that cannot be hurried, "
                    "and clearing a drug is not the same as undoing what it "
                    "did to liver cells."},
            {"text": "Liver cells can be damaged permanently while the person "
                     "feels fine for a day or two", "correct": True},
            {"text": "They are right, provided they take nothing else for the "
                     "rest of the week", "correct": False,
             "why": "Waiting does not undo damage that has already been done. "
                    "Feeling well is not evidence that the liver was "
                    "unharmed."},
            {"text": "Feeling well proves the tablets were weaker than the "
                     "box claimed", "correct": False,
             "why": "How a person feels measures nothing about what was in a "
                    "tablet. Liver damage does not announce itself at the "
                    "time."},
        ],
        "figure": None,
    },
    {
        "id": "b6-01-h06",
        "band": "harder",
        "text": "The same drug is sold as a tablet and as a cream rubbed onto "
                "a sore knee. The cream causes far fewer effects elsewhere in "
                "the body. Why?",
        "options": [
            {"text": "The cream is a weaker version of the drug, so it does "
                     "less", "correct": False,
             "why": "Even a weaker tablet would still be carried to every "
                    "organ. What matters is that most of the cream never "
                    "joins the blood at all."},
            {"text": "A drug rubbed on the skin travels through the body to "
                     "the knee far more directly", "correct": False,
             "why": "There is no direct route from skin to knee. The point is "
                    "that most of the cream does not join the blood, so it is "
                    "never offered to everything."},
            {"text": "The cream is absorbed more slowly, giving the other "
                     "organs time to ignore it as it arrives", "correct": False,
             "why": "No organ ignores anything. An organ is affected if the "
                    "drug reaches it and fits, and how slowly it arrives does "
                    "not change that."},
            {"text": "Most of the cream never joins the blood, so other "
                     "organs never get it", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b6-01-h07",
        "band": "harder",
        "text": "Inhaled nicotine reaches the brain in about 10 seconds. A "
                "swallowed drug takes about 5 minutes to reach the blood. How "
                "many times longer is the swallowed route?",
        "options": [
            {"text": "About 0.5 times as long, because 5 divided by 10 is "
                     "0.5", "correct": False,
             "why": "The two times are in different units, so they cannot be "
                    "divided as they stand. Five minutes is 300 seconds, so "
                    "the sum is 300 divided by 10."},
            {"text": "About 10 times longer, taking the inhaled route as "
                     "half a minute", "correct": False,
             "why": "The inhaled route is 10 seconds, not 30. Converting the "
                    "5 minutes to 300 seconds gives 300 divided by 10."},
            {"text": "About 30 times longer, because 5 minutes is 300 "
                     "seconds", "correct": True},
            {"text": "About 50 times longer, because 5 minutes is 500 "
                     "seconds", "correct": False,
             "why": "A minute is 60 seconds rather than 100, so 5 minutes is "
                    "300 seconds. That gives 300 divided by 10, which is "
                    "30."},
        ],
        "figure": None,
    },
    {
        "id": "b6-01-h08",
        "band": "harder",
        "text": "A student says every substance belongs on one of two lists, "
                "safe or dangerous, and that all you have to do is find out "
                "which. Why is that not how it works?",
        "options": [
            {"text": "Amount decides: digoxin steadies a failing heart, a "
                     "little more stops it",
             "correct": True},
            {"text": "Because the lists move: a substance that is dangerous "
                     "in one country is sold legally in another", "correct": False,
             "why": "Laws differ between countries, but what a molecule does "
                    "to a body does not. It is the amount that decides, not "
                    "the border."},
            {"text": "Because a substance is only dangerous once the person "
                     "taking it has become addicted", "correct": False,
             "why": "Addiction is a separate property that some drugs have. A "
                    "substance harms the body at the wrong amount whether or "
                    "not anyone is addicted."},
            {"text": "Because natural things are safe and factory-made ones "
                     "are not", "correct": False,
             "why": "Where a molecule came from tells you nothing about what "
                    "it does. Digoxin grows in a hedgerow, and paracetamol is "
                    "made in a factory."},
        ],
        "figure": None,
    },
    {
        "id": "b6-01-h09",
        "band": "harder",
        "text": "Caffeine is described as a stimulant, and nicotine as a "
                "stimulant that is strongly addictive. What does that extra "
                "description tell you about how the classes work?",
        "options": [
            {"text": "That nicotine is a stronger stimulant than caffeine, "
                     "which is what addictive means", "correct": False,
             "why": "Addictive is not a measure of strength. It says the "
                    "brain adapts to expect the drug, which is a different "
                    "property altogether."},
            {"text": "That how addictive a drug is, is a separate question "
                     "from which class it belongs to", "correct": True},
            {"text": "That nicotine belongs in a fourth class of its own, "
                     "outside the three", "correct": False,
             "why": "There is no fourth class. Nicotine is a stimulant like "
                    "caffeine, and being addictive is an extra property "
                    "rather than a new class."},
            {"text": "That every stimulant is addictive, and nicotine is "
                     "simply the clearest example", "correct": False,
             "why": "Caffeine is a stimulant too and is not described that "
                    "way. Class and addictiveness are separate questions."},
        ],
        "figure": None,
    },
    {
        "id": "b6-01-h10",
        "band": "harder",
        "text": "A company changes a drug's molecule so that it no longer "
                "upsets the stomach. Testing then finds a new unwanted effect "
                "on the kidneys. Why is that not a surprise?",
        "options": [
            {"text": "Because changing a molecule always makes a drug more "
                     "dangerous than it was", "correct": False,
             "why": "It may well be an improvement overall. The point is that "
                    "any molecule in the blood is offered to every organ, so "
                    "it will fit something somewhere."},
            {"text": "Because the kidneys remove every drug, so they are "
                     "always harmed by one", "correct": False,
             "why": "Filtering a broken-down drug out is the kidneys' "
                    "ordinary job and does not harm them. The new effect is "
                    "the new molecule acting where it now fits."},
            {"text": "The new molecule still goes everywhere; the change "
                     "altered what it fits, not where it goes", "correct": True},
            {"text": "Because the stomach and the kidneys are joined, so the "
                     "effect moved from one to the other", "correct": False,
             "why": "Effects do not move between organs. Both organs were "
                    "reached by the blood all along, and what changed is "
                    "which one the molecule can act on."},
        ],
        "figure": None,
    },
    {
        "id": "b6-01-h11",
        "band": "harder",
        "text": "After a heavy evening someone is dehydrated, has an "
                "irritated stomach, and still has slowed reactions. Which "
                "explanation covers all three at once?",
        "options": [
            {"text": "Three different substances in the drink, and each did "
                     "one of the three things", "correct": False,
             "why": "One substance did all three. Alcohol was offered to "
                    "every organ, and it did something different at each of "
                    "them."},
            {"text": "The liver failed to break the alcohol down overnight, "
                     "so it built up in three separate places", "correct": False,
             "why": "The liver breaks it down at its own fixed rate, which is "
                    "why the reactions are still slowed. Nothing failed — the "
                    "dose simply reached everything."},
            {"text": "Dehydration caused the sickness and the slow reactions", "correct": False,
             "why": "None of the three caused the others. The blood carried "
                    "the same alcohol to the kidneys, the stomach and the "
                    "brain."},
            {"text": "One dose reached the kidneys, the stomach and brain, "
                     "acting at each", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b6-01-h12",
        "band": "harder",
        "text": "A surgeon asks a patient to stop smoking for several weeks "
                "before an operation, saying the wound will heal better. "
                "Which of nicotine's effects lies behind that?",
        "options": [
            {"text": "It narrows the blood vessels in the skin, so less blood "
                     "reaches the surface", "correct": True},
            {"text": "It blocks pain signals, so the patient would not notice "
                     "a wound reopening", "correct": False,
             "why": "Nicotine does not touch pain signals — that is a "
                    "painkiller's job. Its effect here is on the blood "
                    "vessels supplying the skin."},
            {"text": "It is broken down in the skin, using up the skin's own "
                     "repair chemicals", "correct": False,
             "why": "Drugs are broken down in the liver. Nicotine affects "
                    "healing by narrowing the vessels that carry blood to the "
                    "surface."},
            {"text": "It speeds the heart up, so blood passes the wound too "
                     "quickly to be useful", "correct": False,
             "why": "Blood moving faster does not stop it delivering "
                    "anything. The problem is narrowed vessels carrying less "
                    "blood to the surface."},
        ],
        "figure": None,
    },
    {
        "id": "b6-01-h13",
        "band": "harder",
        "text": "A painkiller does not stop working all at once — it fades "
                "over a few hours. What is happening to the drug in that "
                "time?",
        "options": [
            {"text": "The pain pathways get used to the drug, so the same "
                     "amount stops working on them", "correct": False,
             "why": "The drug is being removed rather than ignored. The liver "
                    "breaks it down and the kidneys pass it out, so less is "
                    "left in the blood each hour."},
            {"text": "The liver breaks it down at a fixed rate and the "
                     "kidneys pass it out, so less is left", "correct": True},
            {"text": "The drug is used up by the pain pathways as it works on "
                     "them", "correct": False,
             "why": "Acting on a pathway does not consume a drug. It is still "
                    "in the blood until the liver has broken it down."},
            {"text": "The blood carries it away from the pain pathways to "
                     "some other organ instead", "correct": False,
             "why": "The blood offers it to everything all along rather than "
                    "moving it from one place to another. The fading is the "
                    "drug being broken down and removed."},
        ],
        "figure": None,
    },
    {
        "id": "b6-01-h14",
        "band": "harder",
        "text": "Two students summarise the journey. One says the drug "
                "carries no address. The other says every organ is therefore "
                "offered it. Which statement explains why side effects "
                "happen?",
        "options": [
            {"text": "The first, because a drug with no address cannot act on "
                     "anything at all", "correct": False,
             "why": "It acts perfectly well; it simply has no say in where. "
                    "Side effects follow from what happens next, which is "
                    "every organ being offered it."},
            {"text": "Neither, because side effects come from taking too "
                     "large an amount", "correct": False,
             "why": "The whole dose goes round the circuit whatever its size. "
                    "Amount changes how strong an effect is, not whether "
                    "other organs were reached."},
            {"text": "The second — having no address matters only because the "
                     "blood then offers it everywhere", "correct": True},
            {"text": "Both say the same thing, so either one explains it "
                     "equally well", "correct": False,
             "why": "They are two different claims. The first is about the "
                    "molecule and the second about the journey, and it is the "
                    "journey that reaches the other organs."},
        ],
        "figure": None,
    },
    {
        "id": "b6-01-h15",
        "band": "harder",
        "text": "A drug new to you is described as making the signals between "
                "nerve cells pass less readily, so reactions lengthen. Which "
                "class is it, and what should its label warn about?",
        "options": [
            {"text": "A stimulant, and the label should warn about a racing "
                     "heart", "correct": False,
             "why": "A stimulant makes signals pass more readily. Signals "
                    "passing less readily is the definition of a "
                    "depressant."},
            {"text": "A painkiller, and the label should warn that the cause "
                     "of the pain is untouched", "correct": False,
             "why": "Nothing in the description mentions a pain signal. "
                    "Signals in general passing less readily is a "
                    "depressant."},
            {"text": "A depressant, and it needs no warning, because slowing "
                     "things down is the safer direction", "correct": False,
             "why": "It is a depressant, but slower is not safer. Most of "
                    "alcohol's harm comes from what a slowed nervous system "
                    "then does."},
            {"text": "A depressant, and the label should warn about driving "
                     "and using machinery", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b6-01-h16",
        "band": "harder",
        "text": "Nicotine reaches the brain in about ten seconds. Why does "
                "that speed matter for how hard smoking is to stop?",
        "options": [
            {"text": "Reward follows the smoke at once, and the brain adapts "
                     "to expect it", "correct": True},
            {"text": "The faster a drug arrives, the longer it will then stay "
                     "in the body afterwards", "correct": False,
             "why": "How fast a drug arrives and how long it takes to clear "
                    "are separate questions. The speed matters because the "
                    "reward follows the smoke almost immediately."},
            {"text": "Arriving quickly leaves less in the airways to damage", "correct": False,
             "why": "The airway damage is done by tar and the other "
                    "substances, not by how fast the nicotine travels. The "
                    "speed matters at the brain."},
            {"text": "A drug that arrives that quickly cannot be broken down "
                     "by the liver, so it stays for good", "correct": False,
             "why": "Nicotine is broken down like any other drug. Its speed "
                    "matters because of what it does at the brain, not "
                    "because it stays."},
        ],
        "figure": None,
    },
    {
        "id": "b6-01-h17",
        "band": "harder",
        "text": "The same caffeine that helps one person concentrate leaves "
                "another shaky and unable to sit still. What lies behind "
                "that?",
        "options": [
            {"text": "The second person is addicted, and shakiness is what "
                     "going without feels like", "correct": False,
             "why": "Being unable to sit still after taking caffeine is the "
                    "stimulant working, not the lack of it. Amount is what "
                    "separates a useful effect from an unpleasant one."},
            {"text": "The second person had a faulty batch, since one drug "
                     "cannot do two different things", "correct": False,
             "why": "One drug does many things, because it is offered to "
                    "every organ. How strong each effect is depends on the "
                    "amount taken."},
            {"text": "Amount decides: a stimulant that raises alertness "
                     "raises it further at a larger amount", "correct": True},
            {"text": "They are two different sorts of caffeine, one stronger "
                     "than the other", "correct": False,
             "why": "There is one caffeine molecule and it sits in one class. "
                    "What differs between the two people is the amount."},
        ],
        "figure": None,
    },
    {
        "id": "b6-01-h18",
        "band": "harder",
        "text": "Paracetamol acts on the pain pathways and on the brain's "
                "temperature control centre. A student says that proves the "
                "tablet was aimed at two places. What is the better "
                "explanation?",
        "options": [
            {"text": "The tablet splits in the stomach, and each half is sent "
                     "to a different place", "correct": False,
             "why": "A dissolved tablet is one substance in the blood rather "
                    "than two parcels, and nothing is sent anywhere."},
            {"text": "It was offered to every organ, and those are two of the "
                     "places where it fits", "correct": True},
            {"text": "The pain pathways pass the drug on to the temperature "
                     "control centre", "correct": False,
             "why": "Nothing is passed on between organs. The blood offered "
                    "the same dose to both, and it acts wherever it fits."},
            {"text": "Two targets means two separate doses must have been "
                     "taken", "correct": False,
             "why": "One dose reaches everything. Acting in two places is one "
                    "dose fitting in two places, not two doses."},
        ],
        "figure": None,
    },
]
