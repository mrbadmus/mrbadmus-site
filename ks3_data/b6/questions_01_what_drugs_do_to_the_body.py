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

    # ── MRB-338 expansion (12 Sep 2026) ─────────────────────────────────
    # 38 new rows (14 easier / 13 standard / 11 harder) continuing the
    # band id sequences from e19/s19/h19, against a target of 14/14/14.
    # New teachable points not covered by the original 54 rows or by the
    # mastery ladder: nicotine's effect on heart rate and blood pressure,
    # its reward-chemical mechanism, legal-vs-biological status across all
    # four drugs, paracetamol's kidney elimination route and the "every
    # other organ, no use for it" clause, the foxglove/digoxin
    # dose-response numbers, water as a dose-response example, and
    # cross-drug comparisons (entry mechanism, stomach irritation, kidney
    # effects, class labels). See the MRB-338 authoring report for the
    # full coverage list and the length/position self-checks. Standard is
    # one row short and harder three short of the 14-row target -
    # declined rather than padded once fresh, non-duplicating,
    # non-task-reproducing points ran out on an already densely-covered
    # lesson; see the report.

    {
        "id": "b6-01-e19",
        "band": "easier",
        "text": "Nicotine makes the heart beat faster and narrows blood vessels. What "
"does that combination do to blood pressure?",
        "options": [
            {"text": "It rises, because both a faster heart and narrower vessels push it "
"upward",
             "correct": True},
            {"text": "It falls, because a faster heart needs to pump against less "
"resistance",
             "correct": False,
             "why": "Narrower vessels add resistance rather than removing it, so the "
"pressure needed to pump blood does not fall."},
            {"text": "It stays the same, because the two effects cancel each other out",
             "correct": False,
             "why": "The two effects act in the same direction rather than opposite ones, "
"so they add together instead of cancelling."},
            {"text": "It only rises in people who already have heart problems",
             "correct": False,
             "why": "The lesson describes this as something nicotine does to the body in "
"general, not a risk limited to one group."},
        ],
        "figure": None,
    },
    {
        "id": "b6-01-e20",
        "band": "easier",
        "text": "Cigarettes and vapes are illegal to sell to under-18s in the UK. Is "
"nicotine legal for an adult to buy?",
        "options": [
            {"text": "No, nicotine is illegal for anyone of any age to buy",
             "correct": False,
             "why": "It is legal to sell nicotine to an adult; only sale to under-18s "
"is illegal."},
            {"text": "Yes, it is legal to sell to an adult in the UK",
             "correct": True},
            {"text": "Only with a doctor's prescription",
             "correct": False,
             "why": "No prescription is needed to buy cigarettes or vapes; the "
"restriction on them is an age limit."},
            {"text": "It depends on whether the nicotine is smoked or vaped",
             "correct": False,
             "why": "Both carry the same legal status: legal for adults, illegal to "
"sell to under-18s."},
        ],
        "figure": None,
    },
    {
        "id": "b6-01-e21",
        "band": "easier",
        "text": "After paracetamol has been broken down by the liver, what job do the "
"kidneys do with it?",
        "options": [
            {"text": "They break it down a second time to finish the job",
             "correct": False,
             "why": "The lesson gives the liver the breaking-down job; the kidneys' part "
"is filtering it out, not repeating that step."},
            {"text": "They store it in case the body needs the drug again later",
             "correct": False,
             "why": "No organ is described as storing a drug for later use anywhere in "
"the lesson."},
            {"text": "They filter the broken-down drug out into the urine",
             "correct": True},
            {"text": "They send it back into the blood so it can reach the brain again",
             "correct": False,
             "why": "The kidneys' job is described as removing the drug from the body, "
"the opposite of returning it to circulation."},
        ],
        "figure": None,
    },
    {
        "id": "b6-01-e22",
        "band": "easier",
        "text": "Besides the liver and kidneys, paracetamol also reaches every other "
"organ in the body through the blood. What happens to it at those "
"other organs?",
        "options": [
            {"text": "Each one stores a small amount in case it is needed later",
             "correct": False,
             "why": "No organ stores a drug for later use; these organs simply had no "
"use for it."},
            {"text": "Each one breaks down a share of the drug, alongside the liver",
             "correct": False,
             "why": "Breaking the drug down is the liver's job alone, not something "
"spread across every organ."},
            {"text": "Each one actively blocks the drug from having any effect",
             "correct": False,
             "why": "These organs do not resist the drug at all; they simply receive it "
"and have no use for it."},
            {"text": "They receive the drug and have no use for it at all",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b6-01-e23",
        "band": "easier",
        "text": "Which of these drugs is legal to buy at any age in the UK?",
        "options": [
            {"text": "Caffeine",
             "correct": True},
            {"text": "Alcohol",
             "correct": False,
             "why": "Alcohol is legal for adults, with age limits on buying it, not for "
"any age."},
            {"text": "Nicotine",
             "correct": False,
             "why": "Nicotine products are illegal to sell to under-18s, so they are not "
"legal at any age."},
            {"text": "Digoxin",
             "correct": False,
             "why": "Digoxin is prescribed by a doctor for a failing heart, so it "
"cannot be bought over a counter at any age."},
        ],
        "figure": None,
    },
    {
        "id": "b6-01-e24",
        "band": "easier",
        "text": "Roughly how long has digoxin been prescribed as a heart medicine?",
        "options": [
            {"text": "About ten years",
             "correct": False,
             "why": "Digoxin has been in medical use for far longer than ten years."},
            {"text": "About two hundred years",
             "correct": True},
            {"text": "About fifty years",
             "correct": False,
             "why": "Digoxin has been in medical use for considerably longer than fifty "
"years."},
            {"text": "Only since it was made in a factory",
             "correct": False,
             "why": "Digoxin comes from the foxglove plant rather than a factory, and it "
"was in use as a medicine long before anything was made in one."},
        ],
        "figure": None,
    },
    {
        "id": "b6-01-e25",
        "band": "easier",
        "text": "At the right dose, digoxin steadies a failing heart. What does a "
"dose a little above that do?",
        "options": [
            {"text": "It has no further effect, since the heart is already steadied",
             "correct": False,
             "why": "A slightly higher dose becomes dangerous rather than simply doing "
"nothing more."},
            {"text": "It steadies the heart even more effectively",
             "correct": False,
             "why": "A small increase in this dose becomes dangerous rather than more "
"effective."},
            {"text": "It stops the heart",
             "correct": True},
            {"text": "It is broken down before it can reach the heart",
             "correct": False,
             "why": "The body does not neutralise a higher dose before it acts; that is "
"exactly why the dose matters so much."},
        ],
        "figure": None,
    },
    {
        "id": "b6-01-e26",
        "band": "easier",
        "text": "Using the dose-response idea, can drinking water ever be "
"dangerous?",
        "options": [
            {"text": "No, water carries no risk at any amount",
             "correct": False,
             "why": "Water is the clearest example of the opposite: a substance nobody "
"calls a drug that is still dangerous at a high enough amount."},
            {"text": "Yes, but only when it is drunk alongside another drug",
             "correct": False,
             "why": "No other substance needs to be present; a large enough amount of "
"water alone is the risk."},
            {"text": "Only tap water is a risk; bottled water is not",
             "correct": False,
             "why": "Tap water and bottled water behave identically here; the amount is "
"what matters, not the source."},
            {"text": "Yes, several litres in an hour can dangerously dilute the blood",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b6-01-e27",
        "band": "easier",
        "text": "Caffeine's job is keeping you alert, yet it also makes the heart "
"beat faster. Is a faster heart caffeine's main job?",
        "options": [
            {"text": "No, the heart was simply on the route the dose travelled, not the "
"target",
             "correct": True},
            {"text": "Yes, alertness and a faster heartbeat are really the same effect",
             "correct": False,
             "why": "The lesson treats them as two separate things: one is caffeine's "
"target effect on the brain, the other is an effect on an organ the "
"dose simply passed through."},
            {"text": "No, and caffeine has no real effect on the heart at all",
             "correct": False,
             "why": "The lesson states plainly that caffeine does speed the heart up; "
"what it denies is that this is caffeine's purpose."},
            {"text": "Yes, because a faster heart is what makes the brain feel alert",
             "correct": False,
             "why": "The lesson gives the brain its own separate mechanism for alertness "
"and does not say the heart causes that feeling."},
        ],
        "figure": None,
    },
    {
        "id": "b6-01-e28",
        "band": "easier",
        "text": "What does nicotine trigger in the brain?",
        "options": [
            {"text": "A release of the chemical that normally makes you feel sleepy",
             "correct": False,
             "why": "That chemical signal is caffeine's target, not nicotine's; nicotine "
"triggers a reward chemical instead."},
            {"text": "A release of the brain's own reward chemical",
             "correct": True},
            {"text": "A drop in the chemical responsible for pain signals",
             "correct": False,
             "why": "Pain signals belong to the painkiller class's mechanism, not to "
"nicotine's."},
            {"text": "A slowing of the signals passing between nerve cells",
             "correct": False,
             "why": "Slowing signals is what a depressant such as alcohol does, the "
"opposite of a stimulant such as nicotine."},
        ],
        "figure": None,
    },
    {
        "id": "b6-01-e29",
        "band": "easier",
        "text": "Why are some stimulants prescribed by doctors, even though caffeine "
"and nicotine are stimulants too?",
        "options": [
            {"text": "Because prescribed stimulants are not really drugs at all",
             "correct": False,
             "why": "A drug is any substance that changes how the body works, and being "
"prescribed does not take a substance out of that definition."},
            {"text": "Because a doctor's approval removes any risk from the drug",
             "correct": False,
             "why": "What makes the effect useful is a controlled dose; a doctor's "
"approval does not remove the risk altogether."},
            {"text": "Because the effect is useful when the dose is carefully controlled",
             "correct": True},
            {"text": "Because prescribed stimulants belong to a different class entirely",
             "correct": False,
             "why": "A prescribed stimulant is still a stimulant; what changes is how "
"carefully the dose is controlled."},
        ],
        "figure": None,
    },
    {
        "id": "b6-01-e30",
        "band": "easier",
        "text": "Beer, wine and spirits are legal for adults in the UK, with age "
"limits on buying them. Who are they NOT legally sold to?",
        "options": [
            {"text": "Nobody; anyone of any age may buy them",
             "correct": False,
             "why": "There are age limits on buying alcohol, so it is not open to "
"anyone of any age."},
            {"text": "Only people who already own a medical prescription",
             "correct": False,
             "why": "No prescription is involved in buying alcohol; the restriction is "
"an age limit."},
            {"text": "Only people who have never tried it before",
             "correct": False,
             "why": "The restriction is about age, not about whether someone has drunk "
"before."},
            {"text": "People under the legal buying age",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b6-01-e31",
        "band": "easier",
        "text": "When a painkiller stops you feeling pain, has the underlying "
"problem gone away?",
        "options": [
            {"text": "Not necessarily, pain that stops being felt has not stopped being a "
"warning",
             "correct": True},
            {"text": "Yes, because painkillers treat the cause of the pain as well as the "
"feeling",
             "correct": False,
             "why": "A painkiller leaves the cause of the pain untouched; only the "
"signal is reduced or blocked."},
            {"text": "Yes, because pain always stops once the injury has healed",
             "correct": False,
             "why": "The question is about what the drug does, not about healing time; "
"the two are separate things."},
            {"text": "No, painkillers make the underlying problem worse while hiding it",
             "correct": False,
             "why": "A painkiller does not worsen the injury or infection; it blocks "
"the signal reporting it."},
        ],
        "figure": None,
    },
    {
        "id": "b6-01-e32",
        "band": "easier",
        "text": "Nicotine's class label is more than just 'stimulant'. What extra "
"word goes with it?",
        "options": [
            {"text": "Extremely dangerous",
             "correct": False,
             "why": "The word that goes with nicotine's label is addictive, not a "
"general danger warning."},
            {"text": "Strongly addictive",
             "correct": True},
            {"text": "Completely illegal",
             "correct": False,
             "why": "Nicotine is legal for adults to buy, so illegal is not the word "
"that goes with it."},
            {"text": "Medically prescribed",
             "correct": False,
             "why": "Nicotine in cigarettes and vapes is not something a doctor "
"prescribes."},
        ],
        "figure": None,
    },
    {
        "id": "b6-01-s19",
        "band": "standard",
        "text": "Someone tries a cigarette once, feels little effect, but a week "
"later finds themselves wanting one badly. Using what nicotine does "
"in the brain, explain what has changed.",
        "options": [
            {"text": "Nicotine triggered the brain's reward chemical, and the brain "
"adapted to expect that release",
             "correct": True},
            {"text": "Nothing has changed inside the body at all; wanting a cigarette "
"again is simply a decision, not a chemical reaction",
             "correct": False,
             "why": "The lesson describes the wanting as a physical adaptation of the "
"nervous system, not a decision with no biological cause."},
            {"text": "The nicotine from that first cigarette has stayed in the blood for a "
"week, still acting on the brain",
             "correct": False,
             "why": "The tracer describes a single dose leaving the body within hours, "
"not lingering for a week to cause a craving."},
            {"text": "Their body has grown more sensitive to the tar in the smoke, which "
"is what is now driving the craving",
             "correct": False,
             "why": "The reward-chemical mechanism the lesson describes belongs to "
"nicotine, not to tar."},
        ],
        "figure": None,
    },
    {
        "id": "b6-01-s20",
        "band": "standard",
        "text": "A doctor prescribes digoxin at a fixed, carefully measured dose to a "
"patient with a failing heart. Using the dose-response idea, explain "
"why the same substance can also be one of the most dangerous plants "
"in Britain.",
        "options": [
            {"text": "Digoxin from the plant is dangerous, but the medicine made in a "
"factory is a chemically different, safer substance",
             "correct": False,
             "why": "The lesson treats it as the same molecule at different amounts, not "
"a different, safer substance."},
            {"text": "The effect depends on the amount: the prescribed dose steadies the "
"heart, a little more stops it",
             "correct": True},
            {"text": "The plant is dangerous because it is natural, while the medicine is "
"safe simply because a doctor prescribed it",
             "correct": False,
             "why": "The lesson's point is that natural tells you nothing about safety; "
"only the dose does."},
            {"text": "The danger from a higher dose only applies to people who already "
"have an existing heart problem",
             "correct": False,
             "why": "The lesson ties the danger to the amount taken by anyone, not to a "
"pre-existing condition."},
        ],
        "figure": None,
    },
    {
        "id": "b6-01-s21",
        "band": "standard",
        "text": "Someone who has been drinking becomes tearful and says alcohol "
"obviously works on people's emotions. Using what a depressant actually "
"does, is that the correct explanation?",
        "options": [
            {"text": "Yes, depressant is simply another word in biology for a drug that "
"lowers a person's mood directly",
             "correct": False,
             "why": "A depressant is defined by its effect on nerve signal speed, not "
"by an effect on mood."},
            {"text": "No, alcohol has no effect on the brain at all, and acts only on the "
"liver instead",
             "correct": False,
             "why": "Alcohol's target is the brain, where it slows the signals passing "
"between nerve cells."},
            {"text": "Not quite, a depressant slows nerve signal speed; it is not defined "
"as acting on mood",
             "correct": True},
            {"text": "Yes, every depressant is specifically designed by its chemistry to "
"make people feel sad",
             "correct": False,
             "why": "A depressant does not make you sad; the word is about signalling "
"speed, not mood."},
        ],
        "figure": None,
    },
    {
        "id": "b6-01-s22",
        "band": "standard",
        "text": "Alcohol and nicotine both reach the blood unusually quickly for "
"their route into the body. Which pairing of reasons is correct?",
        "options": [
            {"text": "Alcohol is inhaled in the same way as nicotine, which explains why "
"both act within seconds of use",
             "correct": False,
             "why": "Alcohol is swallowed, not inhaled; only nicotine's route into the "
"blood is through the lungs."},
            {"text": "Both drugs cross the thin walls of the alveoli on the way in, which "
"is why both act within seconds of being taken",
             "correct": False,
             "why": "Only nicotine is described as crossing the alveoli walls; alcohol's "
"route is through the stomach and gut."},
            {"text": "Nicotine dissolves in saliva before being swallowed, reaching the "
"blood through the mouth lining",
             "correct": False,
             "why": "The lesson describes nicotine as inhaled, crossing the alveoli "
"walls, not swallowed or absorbed through the mouth."},
            {"text": "Alcohol crosses the stomach wall as well as the intestine; nicotine "
"crosses the thin walls of the alveoli",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b6-01-s23",
        "band": "standard",
        "text": "After exercise, someone drinks several litres of water very quickly, "
"believing more water is always better for the body. Using the "
"dose-response idea, is that necessarily true?",
        "options": [
            {"text": "No, even water can dangerously dilute the blood if enough is drunk "
"quickly",
             "correct": True},
            {"text": "Yes, water is not classed as a drug, so no amount of it can ever "
"cause any harm",
             "correct": False,
             "why": "Water shows exactly the opposite: a substance nobody calls a drug "
"can still be dangerous at a high enough dose."},
            {"text": "Yes, the kidneys are able to safely process any amount of water in "
"any length of time",
             "correct": False,
             "why": "Several litres drunk in an hour is a genuine risk; the kidneys "
"cannot clear water at any rate at all."},
            {"text": "No, plain water only becomes dangerous once it has been contaminated "
"by something else",
             "correct": False,
             "why": "The danger described comes from the amount of plain water itself, "
"not from any contamination."},
        ],
        "figure": None,
    },
    {
        "id": "b6-01-s24",
        "band": "standard",
        "text": "A doctor prescribes a stimulant medicine, and a friend says this is "
"strange because stimulants are the same as the ones in cigarettes "
"and energy drinks. Using the dose-response idea, explain what makes "
"the prescribed one different.",
        "options": [
            {"text": "A prescribed stimulant stops being a drug at all once a doctor is "
"the one giving it",
             "correct": False,
             "why": "A drug is defined by what it does to the body; being prescribed does "
"not remove it from that definition."},
            {"text": "The dose is carefully controlled, which is what makes the stimulant "
"effect useful rather than harmful",
             "correct": True},
            {"text": "Prescribed stimulants act on a completely different part of the "
"nervous system altogether",
             "correct": False,
             "why": "The lesson ties the difference to the controlled dose, not to a "
"different mechanism."},
            {"text": "The friend is right, and there genuinely is no real difference "
"between the two at all",
             "correct": False,
             "why": "The lesson explicitly says the prescribed stimulant's usefulness "
"comes from its dose being controlled."},
        ],
        "figure": None,
    },
    {
        "id": "b6-01-s25",
        "band": "standard",
        "text": "Someone argues that alcohol's danger lies entirely in slower "
"reactions and coordination themselves. Where does a large part of "
"alcohol's short-term harm also come from?",
        "options": [
            {"text": "From the particular taste and smell of the alcoholic drink itself",
             "correct": False,
             "why": "A drink's taste and smell have nothing to do with any harm it "
"causes."},
            {"text": "From the extra calories that alcoholic drinks happen to contain",
             "correct": False,
             "why": "The harm here is about nerve signalling and judgement, not about "
"calories."},
            {"text": "From what a person with impaired judgement then goes on to do",
             "correct": True},
            {"text": "Entirely from the slower reactions and coordination themselves, "
"exactly as the argument claims",
             "correct": False,
             "why": "Judgement fails first, and the actions that follow are a large "
"part of the harm on the night."},
        ],
        "figure": None,
    },
    {
        "id": "b6-01-s26",
        "band": "standard",
        "text": "Paracetamol reaches many organs that do nothing whatever with it "
"once it arrives, and other organs, like the kidneys, that actively "
"act on it. What is the key difference between the two?",
        "options": [
            {"text": "There is really no difference at all; every single organ the blood "
"carries the drug to is harmed by it in exactly the same way",
             "correct": False,
             "why": "Organs with no use for the drug are not harmed by simply "
"receiving it; the kidneys, by contrast, actively do something with it."},
            {"text": "Organs with no use for the drug are the ones that break it down "
"and remove it from the body",
             "correct": False,
             "why": "Breaking the drug down and filtering it out is exactly what the "
"second group does; an organ with no use for it does neither."},
            {"text": "The kidneys have no use for paracetamol either, exactly like every "
"other organ the drug happens to reach",
             "correct": False,
             "why": "The kidneys have a specific job here, filtering the broken-down "
"drug into urine, unlike organs with no use for it."},
            {"text": "One group simply receives the drug and does nothing with it; the "
"other group acts on it, breaking it down or filtering it out",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b6-01-s27",
        "band": "standard",
        "text": "Caffeine and alcohol are opposites in one specific way, according to "
"their classes. What is it?",
        "options": [
            {"text": "Caffeine speeds nerve signals up; alcohol slows them down",
             "correct": True},
            {"text": "Caffeine is illegal for under-18s to buy; alcohol is legal at any "
"age at all",
             "correct": False,
             "why": "The legal facts are the other way round in the lesson: caffeine is "
"legal at any age, alcohol has age limits."},
            {"text": "Caffeine works by treating pain directly; alcohol works by causing "
"pain instead",
             "correct": False,
             "why": "Neither drug is classed as a painkiller in the lesson; that is a "
"separate class entirely."},
            {"text": "Caffeine is a drug that is swallowed; alcohol is a drug that is "
"inhaled instead",
             "correct": False,
             "why": "Both caffeine and alcohol are described in the lesson as swallowed "
"drinks."},
        ],
        "figure": None,
    },
    {
        "id": "b6-01-s28",
        "band": "standard",
        "text": "Digoxin has been used safely as a medicine for around two hundred "
"years, yet the foxglove it comes from is still one of the most "
"dangerous plants in Britain. Explain how both statements can be "
"true.",
        "options": [
            {"text": "The plant only became dangerous recently, well after the medicine "
"had already been established",
             "correct": False,
             "why": "No timeline is given in which the plant's danger changed; both are "
"the same molecule at different amounts."},
            {"text": "The medicine is a small, controlled dose; the dangerous plant is an "
"uncontrolled, unmeasured amount",
             "correct": True},
            {"text": "Doctors actually use a chemically different, purified substance with "
"nothing to do with the plant",
             "correct": False,
             "why": "Digoxin is described as coming from the foxglove, the same molecule, "
"not a chemically unrelated substitute."},
            {"text": "Two hundred years of safe medical use proves the substance cannot "
"really be dangerous at all",
             "correct": False,
             "why": "The lesson uses this exact substance to make the opposite point: "
"safety depends on dose, not on a long history of use."},
        ],
        "figure": None,
    },
    {
        "id": "b6-01-s29",
        "band": "standard",
        "text": "Caffeine and nicotine both make the heart beat faster, but only one "
"of them is also described as narrowing blood vessels and raising "
"blood pressure. Which one, and how do you know?",
        "options": [
            {"text": "Caffeine, since a faster heart, narrowed blood vessels and raised "
"blood pressure are all caffeine's effects",
             "correct": False,
             "why": "Caffeine's listed effects are a faster heart, more urine and more "
"stomach acid; narrowed vessels are not among them."},
            {"text": "Both drugs equally, since the two have an identical list of "
"effects on the heart and vessels",
             "correct": False,
             "why": "The two drugs' lists of effects on the body are different from each "
"other, not identical."},
            {"text": "Nicotine, whose effects include narrowed blood vessels and raised "
"blood pressure alongside the faster heartbeat",
             "correct": True},
            {"text": "Neither drug at all, since blood pressure is never once mentioned "
"for either of the two substances",
             "correct": False,
             "why": "Blood pressure rising is one of nicotine's own listed effects."},
        ],
        "figure": None,
    },
    {
        "id": "b6-01-s30",
        "band": "standard",
        "text": "Nicotine products are illegal to sell to under-18s, while caffeine "
"is legal to buy at any age. Does this legal difference mean nicotine "
"changes the body more strongly than caffeine does?",
        "options": [
            {"text": "Yes, the law would never restrict nicotine unless it were truly the "
"biologically stronger of the two drugs",
             "correct": False,
             "why": "The lesson's argument is that legal rules and biological effects are "
"separate questions that need not line up."},
            {"text": "Yes, anything sold with an age limit is always more addictive than "
"anything sold without one",
             "correct": False,
             "why": "No general rule links an age limit to addictiveness; the lesson "
"treats law and biology as separate."},
            {"text": "No, the two drugs actually have identical effects on the body, and "
"only the law differs",
             "correct": False,
             "why": "The lesson lists different effects for caffeine and nicotine; it "
"does not claim they act identically."},
            {"text": "Not necessarily, legality is a rule made by people, a separate "
"question from what a drug does to the body",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b6-01-s31",
        "band": "standard",
        "text": "Caffeine and alcohol both upset the stomach, but by different "
"mechanisms. Which pairing is correct?",
        "options": [
            {"text": "Caffeine makes the stomach release more acid; alcohol irritates the "
"stomach lining directly",
             "correct": True},
            {"text": "Caffeine irritates the stomach lining directly; alcohol makes it "
"release more acid instead",
             "correct": False,
             "why": "These two mechanisms belong the other way round: it is caffeine "
"that raises the acid."},
            {"text": "Both drugs work by releasing more stomach acid, in exactly the same "
"way as each other",
             "correct": False,
             "why": "Alcohol works by directly irritating the lining rather than by "
"releasing more acid."},
            {"text": "Neither drug has any effect on the stomach at all",
             "correct": False,
             "why": "Both caffeine and alcohol reach the stomach and upset it, by two "
"different routes."},
        ],
        "figure": None,
    },
    {
        "id": "b6-01-h19",
        "band": "harder",
        "text": "Nicotine's class label is 'Stimulant, strongly addictive', while "
"caffeine's is simply 'Stimulant'. Why might that extra word matter "
"to someone trying to help a person stop using each?",
        "options": [
            {"text": "Stopping nicotine involves overcoming an adaptation the brain has "
"made, which caffeine's label does not describe",
             "correct": True},
            {"text": "It means caffeine has no effect on the brain whatsoever, quite "
"unlike nicotine's clear and immediate effect there",
             "correct": False,
             "why": "Caffeine is described as acting directly on the brain to block a "
"sleep signal; the difference is about addiction, not brain effect."},
            {"text": "It means nicotine is an illegal substance while caffeine remains "
"completely legal to sell",
             "correct": False,
             "why": "Both are legal; nicotine carries an age restriction on sale, but "
"neither drug is illegal outright."},
            {"text": "It simply means caffeine is a much weaker stimulant overall compared "
"with nicotine's stronger and longer-lasting effect",
             "correct": False,
             "why": "The extra word describes addictiveness, not the relative strength of "
"the stimulant effect."},
        ],
        "figure": None,
    },
    {
        "id": "b6-01-h20",
        "band": "harder",
        "text": "A simple five-stage model follows one dose from being swallowed to "
"leaving the body. Does a model like that show exactly how quickly a "
"real drug clears from every person?",
        "options": [
            {"text": "Yes, the five stages are stated to apply identically and exactly the "
"same way to every single person, no matter who",
             "correct": False,
             "why": "The real processes overlap in time and differ between people, "
"which is why the model is only a simplification."},
            {"text": "No, it is a simplified model, and real absorption, distribution "
"and breakdown differ between people",
             "correct": True},
            {"text": "Yes, but only for the four drugs the model happens to be drawn "
"for",
             "correct": False,
             "why": "The simplification is general; it is not something that applies to "
"four named drugs and no others."},
            {"text": "No, because such a model only ever shows a drug entering the "
"body, never leaving it again",
             "correct": False,
             "why": "The five stages run all the way to the drug leaving; the model is "
"a simplification because of individual differences and timing, not "
"because a stage is missing."},
        ],
        "figure": None,
    },
    {
        "id": "b6-01-h21",
        "band": "harder",
        "text": "A company advertises a new painkiller capsule with a special coating "
"claimed to 'send the drug straight to the sore joint and nowhere "
"else.' Is that consistent with how a swallowed drug actually travels "
"round the body?",
        "options": [
            {"text": "Yes, a special coating on a capsule genuinely changes exactly where "
"in the body the blood chooses to deliver a drug",
             "correct": False,
             "why": "The blood carries every dissolved drug to every organ whatever "
"the coating was; a coating affects the gut, not what happens after."},
            {"text": "Yes, the joint has its own separate blood supply that only pain "
"relief is able to enter",
             "correct": False,
             "why": "There is one blood system, reaching every organ; no route is "
"reserved for pain relief."},
            {"text": "No, once dissolved in the blood, the dose has no address and reaches "
"every organ the circulation reaches",
             "correct": True},
            {"text": "It cannot be judged at all without knowing which painkiller is "
"inside the capsule",
             "correct": False,
             "why": "Every drug dissolved in the blood travels the same way, so the "
"claim can be judged without naming the drug."},
        ],
        "figure": None,
    },
    {
        "id": "b6-01-h22",
        "band": "harder",
        "text": "Digoxin's dose decides whether it heals or kills. Does the AMOUNT "
"of a drug change how strong or dangerous its effect is, while its "
"class stays the same?",
        "options": [
            {"text": "No, a large enough dose of any stimulant turns it into a "
"depressant instead, so the class changes rather than the strength",
             "correct": False,
             "why": "No drug switches class with dose; what changes is the strength or "
"danger of its own effect."},
            {"text": "No, every drug becomes a painkiller once its dose is raised high "
"enough, whatever it started as",
             "correct": False,
             "why": "The three classes are tied to what a drug does to nerve signals or "
"to pain, not to a threshold every drug eventually crosses."},
            {"text": "It cannot be answered, since a drug's class is never fixed until "
"the dose has been chosen",
             "correct": False,
             "why": "A drug's class is settled by what it does to nerve signals or "
"pain, and that is the same at every dose."},
            {"text": "Yes, the class describes the kind of effect a drug produces, and "
"the dose decides how strong or dangerous that effect is",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b6-01-h23",
        "band": "harder",
        "text": "Nicotine is described as triggering a release of the brain's reward "
"chemical, while caffeine is described as blocking a chemical signal "
"that would otherwise build up. Both are called stimulants. What do "
"these two different mechanisms have in common that earns them the "
"same class label?",
        "options": [
            {"text": "Both make nerve signals pass more readily, raising alertness and "
"heart rate, even though they reach that outcome differently",
             "correct": True},
            {"text": "Both work by directly speeding up the heart rate first, with every "
"single other effect following on from that fact entirely",
             "correct": False,
             "why": "The heart effect is a side effect on the route in the lesson, not "
"the mechanism defining the stimulant class."},
            {"text": "Both are broken down by the liver in an identical way, which is what "
"the class label describes",
             "correct": False,
             "why": "The lesson never compares how the two drugs are broken down; the "
"label is about their effect on signals."},
            {"text": "Both are equally addictive, and addictiveness is exactly what "
"defines the stimulant class",
             "correct": False,
             "why": "Strong addictiveness is attached to nicotine specifically, not to "
"the stimulant class as a whole."},
        ],
        "figure": None,
    },
    {
        "id": "b6-01-h24",
        "band": "harder",
        "text": "Alcohol affects reactions, coordination and judgement, with "
"judgement going first. Why does that particular order make alcohol "
"especially dangerous?",
        "options": [
            {"text": "Because judgement is actually the very first of the three affected "
"abilities to return completely and fully to normal",
             "correct": False,
             "why": "Going first means affected earliest, not recovering earliest."},
            {"text": "Because judgement is the ability needed to notice you are impaired, "
"so it fails right when it is most needed",
             "correct": True},
            {"text": "Because judgement is controlled by a completely different organ from "
"reactions and coordination",
             "correct": False,
             "why": "All three come from the same mechanism, alcohol slowing signals "
"throughout the brain."},
            {"text": "Because losing judgement first means a drinker feels absolutely no "
"effect at all",
             "correct": False,
             "why": "The drinker does not feel nothing; they are simply least able to "
"judge how affected they are."},
        ],
        "figure": None,
    },
    {
        "id": "b6-01-h25",
        "band": "harder",
        "text": "A country changes the law so that nicotine products become fully "
"legal to sell to under-18s. Would that legal change alter what "
"nicotine does inside a 15-year-old's body?",
        "options": [
            {"text": "Yes, a substance stops being addictive the very moment it becomes "
"fully legal to sell to absolutely anyone in society",
             "correct": False,
             "why": "A change in the law changes nothing about how a molecule acts in "
"the body."},
            {"text": "Yes, the reward-chemical mechanism only switches on in people old "
"enough to buy the drug legally",
             "correct": False,
             "why": "The reward-chemical mechanism is a biological process, unconnected "
"to whether a sale is currently legal."},
            {"text": "No, legality is a decision made by people and can change, but the "
"molecule and its effect on the body are unaffected by it",
             "correct": True},
            {"text": "It cannot be answered, since nicotine has never been studied in "
"anyone under 18",
             "correct": False,
             "why": "The argument here is about law and biology being separate "
"questions, which holds at any age."},
        ],
        "figure": None,
    },
    {
        "id": "b6-01-h26",
        "band": "harder",
        "text": "Of caffeine, alcohol, nicotine and paracetamol, two make the "
"kidneys produce more urine. Which two?",
        "options": [
            {"text": "Paracetamol and alcohol, both are described as making the kidneys "
"produce more urine",
             "correct": False,
             "why": "The kidneys filter broken-down paracetamol into the urine; they do "
"not make more urine because of it."},
            {"text": "Caffeine and nicotine, both are described as making the kidneys "
"produce more urine",
             "correct": False,
             "why": "Nicotine's effects are on the heart and blood vessels, not on how "
"much urine the kidneys make."},
            {"text": "All four of the drugs make the kidneys produce noticeably more urine "
"than usual",
             "correct": False,
             "why": "Only caffeine and alcohol do this; the kidneys merely filter "
"paracetamol, and nicotine acts elsewhere."},
            {"text": "Caffeine and alcohol, both are described as making the kidneys "
"produce more urine",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b6-01-h27",
        "band": "harder",
        "text": "A customer complains to a manufacturer that their medicine causes "
"drowsiness as well as treating pain, and demands a refund because "
"the product must be 'faulty.' Using what a side effect actually is, "
"evaluate the complaint.",
        "options": [
            {"text": "Not necessarily faulty, a side effect is the unavoidable result of a "
"drug reaching everywhere through the blood, not a manufacturing "
"fault",
             "correct": True},
            {"text": "The complaint is fully justified, since a properly made medicine "
"would produce no side effects whatsoever",
             "correct": False,
             "why": "Reaching organs other than the target is unavoidable for any drug "
"carried in the blood."},
            {"text": "The complaint is fully justified, since drowsiness on its own proves "
"the medicine was made incorrectly",
             "correct": False,
             "why": "A side effect is tied to the drug reaching an organ it was not taken "
"for, not to a manufacturing error."},
            {"text": "It cannot be evaluated at all without knowing exactly which "
"medicine the customer bought",
             "correct": False,
             "why": "What a side effect is does not change from one medicine to "
"another, so the complaint can be judged without naming it."},
        ],
        "figure": None,
    },
    {
        "id": "b6-01-h28",
        "band": "harder",
        "text": "Digoxin at too high a dose, paracetamol taken well above the box's "
"limit, and water drunk by the litre are three very different "
"substances. What single idea explains why all three can become "
"dangerous?",
        "options": [
            {"text": "All three are secretly members of the very same underlying class of "
"drug, some kind of painkiller entirely",
             "correct": False,
             "why": "Digoxin, paracetamol and water are classed quite differently; none "
"of this depends on one shared class."},
            {"text": "Whether a substance treats you or harms you depends on the dose, not "
"on what kind of substance it is",
             "correct": True},
            {"text": "All three become illegal to possess once taken above a certain "
"specific amount",
             "correct": False,
             "why": "Nothing about the law changes with the amount taken; what changes "
"is the effect on the body."},
            {"text": "All three are dangerous purely because every single one of them "
"happens to be swallowed rather than inhaled",
             "correct": False,
             "why": "The route into the body is not where the danger comes from; the "
"dose is."},
        ],
        "figure": None,
    },
    {
        "id": "b6-01-h29",
        "band": "harder",
        "text": "Two mugs of ordinary coffee is enough for a measurable rise in "
"heart rate. What does that tell you about the size of caffeine's "
"effect?",
        "options": [
            {"text": "The effect only ever appears after drinking a great deal more than "
"two mugs of ordinary coffee each and every single morning",
             "correct": False,
             "why": "Two mugs is the amount at which the difference can already be "
"measured, not a minimum before anything happens at all."},
            {"text": "The effect is too small to matter unless someone drinks coffee non- "
"stop all day long",
             "correct": False,
             "why": "An effect measurable from two mugs does not support calling it too "
"small to matter."},
            {"text": "The effect is large enough to detect from an ordinary, everyday "
"amount of caffeine, not only from an extreme dose",
             "correct": True},
            {"text": "The effect only happens in people who rarely, if ever, drink "
"caffeine normally",
             "correct": False,
             "why": "Nothing limits this effect to people unused to caffeine; two mugs "
"raises an ordinary drinker's heart rate measurably too."},
        ],
        "figure": None,
    },

    # ── MRB-338 night 3 top-up — appended, never inserted ──────────────
    {
        "id": "b6-01-h30",
        "band": "harder",
        "text": "A tablet is swallowed at nine o'clock. A student argues that "
                "because blood completes a full circuit of the body very "
                "quickly, the tablet must be acting on the headache a minute "
                "later. Evaluate that.",
        "options": [
            {"text": "The circuit is that quick, but the blood reaches the "
                     "head before it reaches any other organ, so a minute is "
                     "enough",
             "correct": False,
             "why": "There is no order of delivery. The blood offers the dose "
                    "to every organ it passes, and no organ is served ahead "
                    "of the rest."},
            {"text": "The tablet is carried up to the head from the moment it "
                     "is swallowed, so neither dissolving nor the circuit "
                     "adds any delay",
             "correct": False,
             "why": "Nothing is carried anywhere until the tablet has "
                    "dissolved and crossed the gut wall into the blood, and "
                    "it has no address on it when it gets there."},
            {"text": "The circuit is that quick, but the tablet has to "
                     "dissolve and cross the gut wall first, which takes "
                     "several minutes",
             "correct": True},
            {"text": "The circuit is far slower than that, because the blood "
                     "has to pass through the liver and the kidneys before it "
                     "can reach the head",
             "correct": False,
             "why": "Blood does pass through those organs, but the full "
                    "circuit still takes under a minute. What delays the "
                    "tablet is dissolving and being absorbed."},
        ],
        "figure": None,
    },
]
